"""Read Git history with the Python standard library, including packed objects.

The pinned Python slim image contains no Git executable. This reader needs only
commits and trees, but handles both loose objects and pack index v2 files.
"""

from functools import lru_cache
from pathlib import Path
import bisect
import struct
import zlib


class Pack:
    def __init__(self, index):
        data = index.read_bytes()
        if data[:8] != b"\xfftOc\x00\x00\x00\x02":
            raise RuntimeError(f"unsupported Git pack index: {index}")
        count = struct.unpack_from(">I", data, 8 + 255 * 4)[0]
        start = 8 + 256 * 4
        self.names = [data[start + i * 20:start + (i + 1) * 20] for i in range(count)]
        offsets_start = start + count * 24
        large_start = offsets_start + count * 4
        self.offsets = []
        for i in range(count):
            offset = struct.unpack_from(">I", data, offsets_start + i * 4)[0]
            if offset & 0x80000000:
                offset = struct.unpack_from(">Q", data, large_start + (offset & 0x7fffffff) * 8)[0]
            self.offsets.append(offset)
        self.pack = index.with_suffix(".pack").read_bytes()
        if self.pack[:4] != b"PACK":
            raise RuntimeError(f"invalid Git pack: {index}")

    def offset_for(self, oid):
        i = bisect.bisect_left(self.names, bytes.fromhex(oid))
        return self.offsets[i] if i < len(self.names) and self.names[i] == bytes.fromhex(oid) else None


def variable_int(data, pos):
    value = 0
    shift = 0
    while True:
        byte = data[pos]
        pos += 1
        value |= (byte & 0x7f) << shift
        if not byte & 0x80:
            return value, pos
        shift += 7


def apply_delta(base, delta):
    _, pos = variable_int(delta, 0)
    size, pos = variable_int(delta, pos)
    result = bytearray()
    while pos < len(delta):
        opcode = delta[pos]
        pos += 1
        if opcode & 0x80:
            offset = 0
            length = 0
            for bit in range(4):
                if opcode & (1 << bit):
                    offset |= delta[pos] << (8 * bit)
                    pos += 1
            for bit in range(3):
                if opcode & (1 << (bit + 4)):
                    length |= delta[pos] << (8 * bit)
                    pos += 1
            result.extend(base[offset:offset + (length or 65536)])
        elif opcode:
            result.extend(delta[pos:pos + opcode])
            pos += opcode
        else:
            raise RuntimeError("invalid Git delta opcode")
    if len(result) != size:
        raise RuntimeError("invalid Git delta length")
    return bytes(result)


class GitHistory:
    def __init__(self, root):
        dotgit = root / ".git"
        if dotgit.is_file():
            pointer = dotgit.read_text().strip()
            dotgit = (root / pointer.removeprefix("gitdir: ")).resolve()
        self.directory = dotgit
        self.packs = [Pack(path) for path in sorted((dotgit / "objects/pack").glob("*.idx"))]
        head = (dotgit / "HEAD").read_text().strip()
        if head.startswith("ref: "):
            ref = head[5:]
            loose = dotgit / ref
            if loose.exists():
                head = loose.read_text().strip()
            else:
                refs = dict(line.split(" ", 1)[::-1] for line in (dotgit / "packed-refs").read_text().splitlines() if line and not line.startswith(("#", "^")))
                head = refs[ref]
        self.head = head

    @lru_cache(maxsize=None)
    def object(self, oid):
        loose = self.directory / "objects" / oid[:2] / oid[2:]
        if loose.exists():
            header, content = zlib.decompress(loose.read_bytes()).split(b"\0", 1)
            return header.split(b" ", 1)[0].decode(), content
        for pack in self.packs:
            offset = pack.offset_for(oid)
            if offset is not None:
                return self._packed(pack, offset)
        raise RuntimeError(f"missing Git object {oid}; fetch full history")

    @lru_cache(maxsize=None)
    def _packed(self, pack, offset):
        data = pack.pack
        pos = offset
        first = data[pos]
        pos += 1
        kind = (first >> 4) & 7
        while first & 0x80:
            first = data[pos]
            pos += 1
        base = None
        if kind == 6:
            byte = data[pos]
            pos += 1
            distance = byte & 0x7f
            while byte & 0x80:
                byte = data[pos]
                pos += 1
                distance = ((distance + 1) << 7) | (byte & 0x7f)
            base = self._packed(pack, offset - distance)
        elif kind == 7:
            base_oid = data[pos:pos + 20].hex()
            pos += 20
            base = self.object(base_oid)
        decompressor = zlib.decompressobj()
        chunks = []
        while not decompressor.eof:
            part = data[pos:pos + 65536]
            if not part:
                raise RuntimeError("truncated Git pack object")
            chunks.append(decompressor.decompress(part))
            pos += len(part) - len(decompressor.unused_data)
        content = b"".join(chunks)
        if kind in (6, 7):
            return base[0], apply_delta(base[1], content)
        names = {1: "commit", 2: "tree", 3: "blob", 4: "tag"}
        return names[kind], content

    @lru_cache(maxsize=None)
    def commit(self, oid):
        kind, content = self.object(oid)
        if kind != "commit":
            raise RuntimeError(f"expected commit: {oid}")
        header = content.split(b"\n\n", 1)[0]
        tree = next(line[5:].decode() for line in header.splitlines() if line.startswith(b"tree "))
        parents = tuple(line[7:].decode() for line in header.splitlines() if line.startswith(b"parent "))
        return tree, parents

    @lru_cache(maxsize=None)
    def path_object(self, tree, path):
        parts = path.split("/")
        for part in parts:
            kind, body = self.object(tree)
            if kind != "tree":
                return None
            found = None
            pos = 0
            while pos < len(body):
                end = body.index(b"\0", pos)
                _, name = body[pos:end].split(b" ", 1)
                oid = body[end + 1:end + 21].hex()
                pos = end + 21
                if name.decode() == part:
                    found = oid
                    break
            if found is None:
                return None
            tree = found
        return tree

    @lru_cache(maxsize=None)
    def last_touch(self, path):
        current = self.head
        while current:
            tree, parents = self.commit(current)
            blob = self.path_object(tree, path)
            if not parents:
                return current if blob else None
            parent = parents[0]
            if blob != self.path_object(self.commit(parent)[0], path):
                return current
            current = parent
        return None

    def is_ancestor(self, ancestor, descendant):
        pending = [descendant]
        seen = set()
        while pending:
            oid = pending.pop()
            if oid == ancestor:
                return True
            if oid not in seen:
                seen.add(oid)
                pending.extend(self.commit(oid)[1])
        return False
