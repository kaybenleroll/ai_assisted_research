#!/usr/bin/env python3
"""Run explicitly listed primer examples in the pinned language images."""

from __future__ import annotations

import argparse
import os
from pathlib import Path, PurePosixPath
import re
import shlex
import shutil
import subprocess
import sys
import tempfile
import tomllib
import uuid


REPO_ROOT = Path(__file__).resolve().parents[2]
PROFILES = {
    "python-base": ("python", "PYTHON_RUNTIME_IMAGE", "localhost/primers-python-runtime:3.12.15", "python", ".py"),
    "python-torch": ("python", "PYTHON_TORCH_IMAGE", "localhost/primers-python-torch:2.14.1", "python", ".py"),
    "r": ("r", "R_RUNTIME_IMAGE", "localhost/primers-r-runtime:4.5.3", "Rscript", ".R"),
    "julia": ("julia", "JULIA_RUNTIME_IMAGE", "localhost/primers-julia-runtime:1.12.7", "julia", ".jl"),
}
ROOT_FIELDS = {"schema_version", "examples"}
EXAMPLE_FIELDS = {"id", "language", "profile", "script", "markdown", "fence", "working_dir", "timeout_seconds"}
IDENTIFIER = re.compile(r"[A-Za-z][A-Za-z0-9_-]*\Z")
OPEN_FENCE = re.compile(r"^ {0,3}(`{3,}|~{3,})(.*)$")
FENCE_ID = re.compile(r"\{#([A-Za-z][A-Za-z0-9_-]*)\}")


class ManifestError(ValueError):
    """Invalid or unsafe example configuration."""


def safe_file(root: Path, value: str) -> Path:
    if not isinstance(value, str) or not value or "\\" in value:
        raise ManifestError(f"invalid relative path: {value!r}")
    parts = PurePosixPath(value).parts
    if value.startswith("/") or any(part in (".", "..", "") for part in value.split("/")) or ":" in parts[0]:
        raise ManifestError(f"absolute or traversal path: {value!r}")
    target = root.joinpath(*parts)
    current = root
    for part in parts:
        current = current / part
        if current.is_symlink():
            raise ManifestError(f"symlink path is not allowed: {value!r}")
    if not target.is_file() or not target.resolve().is_relative_to(root.resolve()):
        raise ManifestError(f"file is missing or escapes primer: {value!r}")
    return target


def safe_directory(root: Path, value: str) -> Path:
    if not isinstance(value, str) or not value or "\\" in value:
        raise ManifestError(f"invalid relative directory: {value!r}")
    parts = PurePosixPath(value).parts
    if value.startswith("/") or any(part in (".", "..", "") for part in value.split("/")) or ":" in parts[0]:
        raise ManifestError(f"absolute or traversal directory: {value!r}")
    target = root.joinpath(*parts)
    current = root
    for part in parts:
        current = current / part
        if current.is_symlink():
            raise ManifestError(f"symlink directory is not allowed: {value!r}")
    if not target.is_dir() or not target.resolve().is_relative_to(root.resolve()):
        raise ManifestError(f"directory is missing or escapes primer: {value!r}")
    return target


def extract_fence(markdown: Path, fence_id: str, language: str) -> str:
    matches = []
    opening = None
    lines = []
    for line in markdown.read_text(encoding="utf-8").splitlines(keepends=True):
        if opening is None:
            found = OPEN_FENCE.match(line)
            if found:
                opening = (found.group(1)[0], len(found.group(1)), found.group(2).strip())
                lines = []
            continue
        char, length, info = opening
        if re.fullmatch(rf" {{0,3}}{re.escape(char)}{{{length},}}\s*", line):
            ids = FENCE_ID.findall(info)
            if fence_id in ids:
                tag = info.split(maxsplit=1)[0].lower()
                if tag != language or len(ids) != 1:
                    raise ManifestError(f"{markdown}: fence #{fence_id} must be tagged {language}")
                matches.append("".join(lines))
            opening = None
        else:
            lines.append(line)
    if len(matches) != 1 or not matches[0].strip():
        raise ManifestError(f"{markdown}: expected exactly one non-empty fence #{fence_id}, found {len(matches)}")
    return matches[0]


def load_manifest(primer: Path, repo_root: Path = REPO_ROOT) -> list[dict]:
    repo_root = repo_root.resolve()
    primer = primer.resolve()
    if not primer.is_dir() or not primer.is_relative_to(repo_root):
        raise ManifestError(f"primer directory must be inside repository: {primer}")
    manifest = safe_file(primer, "examples/manifest.toml")
    try:
        data = tomllib.loads(manifest.read_text(encoding="utf-8"))
    except (tomllib.TOMLDecodeError, UnicodeError) as exc:
        raise ManifestError(f"{manifest}: {exc}") from exc
    if not isinstance(data, dict) or set(data) != ROOT_FIELDS or type(data["schema_version"]) is not int or data["schema_version"] != 1:
        raise ManifestError(f"{manifest}: require only schema_version = 1 and [[examples]]")
    entries = data["examples"]
    if not isinstance(entries, list) or not entries:
        raise ManifestError(f"{manifest}: [[examples]] must be a non-empty list")
    seen = set()
    result = []
    for entry in entries:
        if not isinstance(entry, dict) or set(entry) - EXAMPLE_FIELDS:
            raise ManifestError(f"{manifest}: unknown example fields: {set(entry) - EXAMPLE_FIELDS if isinstance(entry, dict) else entry!r}")
        name = entry.get("id")
        if not isinstance(name, str) or not IDENTIFIER.fullmatch(name) or name in seen:
            raise ManifestError(f"{manifest}: invalid or duplicate example id: {name!r}")
        seen.add(name)
        language, profile = entry.get("language"), entry.get("profile")
        if not isinstance(language, str) or language not in ("python", "r", "julia") or not isinstance(profile, str) or profile not in PROFILES or PROFILES[profile][0] != language:
            raise ManifestError(f"{manifest}: {name}: unknown or mismatched language/profile: {language!r}/{profile!r}")
        if ("script" in entry) == ("markdown" in entry) or ("fence" in entry) != ("markdown" in entry):
            raise ManifestError(f"{manifest}: {name}: specify script OR markdown with fence")
        timeout = entry.get("timeout_seconds", 120)
        if type(timeout) is not int or not 1 <= timeout <= 600:
            raise ManifestError(f"{manifest}: {name}: timeout_seconds must be 1..600")
        working_dir_value = entry.get("working_dir", ".")
        if not isinstance(working_dir_value, str) or working_dir_value in ("", "."):
            working_dir = primer
        else:
            working_dir = safe_directory(primer, working_dir_value)
        source = safe_file(primer, entry.get("script", entry.get("markdown")))
        if "script" in entry and source.suffix != PROFILES[profile][4]:
            raise ManifestError(f"{manifest}: {name}: script extension must be {PROFILES[profile][4]}")
        code = None
        if "markdown" in entry:
            fence = entry["fence"]
            if not isinstance(fence, str) or not IDENTIFIER.fullmatch(fence):
                raise ManifestError(f"{manifest}: {name}: invalid fence id")
            code = extract_fence(source, fence, language)
        result.append({"id": name, "language": language, "profile": profile, "source": source,
                       "code": code, "timeout": timeout, "working_dir": working_dir})
    return result


def container_command(oci: str, primer: Path, entry: dict, output: Path, repo_root: Path = REPO_ROOT) -> list[str]:
    language, image_var, default_image, interpreter, suffix = PROFILES[entry["profile"]]
    image = os.environ.get(image_var, default_image)
    if not image or image.startswith("-") or any(c.isspace() for c in image):
        raise ManifestError(f"invalid {image_var} image reference")
    source = entry["source"]
    if entry["code"] is not None:
        source = output / (entry["id"] + suffix)
        source.write_text(entry["code"], encoding="utf-8")
        container_source = "/out/" + source.name
    else:
        container_source = "/repo/" + source.relative_to(repo_root).as_posix()
    suffixes = ":ro,z" if oci == "podman" else ":ro"
    out_suffix = ":rw,z" if oci == "podman" else ":rw"
    command = [oci, "run", "--rm", "--name", "primer-example-" + uuid.uuid4().hex,
               "--pull=never", "--network=none", "--entrypoint", interpreter,
               "-v", f"{repo_root}:/repo{suffixes}", "-v", f"{output}:/out{out_suffix}",
               "-w", "/repo/" + entry["working_dir"].relative_to(repo_root).as_posix(),
               "-e", "LANG=C.UTF-8", "-e", "LC_ALL=C.UTF-8", "-e", "TZ=UTC",
               "-e", "HOME=/out", "-e", "TMPDIR=/out", "-e", "EXAMPLE_OUT=/out",
               "-e", "PYTHONDONTWRITEBYTECODE=1"]
    command += ["--userns=keep-id"] if oci == "podman" else ["--user", f"{os.getuid()}:{os.getgid()}"]
    command += [image]
    if language == "julia":
        command.append("--project=/opt/primer-julia")
    command.append(container_source)
    return command


def run_example(oci: str, primer: Path, entry: dict, repo_root: Path = REPO_ROOT) -> bool:
    with tempfile.TemporaryDirectory(prefix="primer-example-") as directory:
        command = container_command(oci, primer, entry, Path(directory), repo_root)
        label = f"{primer.relative_to(repo_root)}/{entry['id']} [{entry['language']}]"
        print(f"[{primer.relative_to(repo_root)}/{entry['id']}] {entry['language']} ({entry['profile']}): {shlex.join(command)}", flush=True)
        try:
            completed = subprocess.run(command, capture_output=True, text=True, timeout=entry["timeout"])
        except subprocess.TimeoutExpired as exc:
            subprocess.run([oci, "rm", "-f", command[4]], capture_output=True, timeout=15, check=False)
            print(f"FAIL {label}: timed out after {entry['timeout']}s", file=sys.stderr)
            for stream in (exc.stdout, exc.stderr):
                if stream:
                    print(stream.decode(errors="replace") if isinstance(stream, bytes) else stream, file=sys.stderr)
            return False
        except OSError as exc:
            print(f"FAIL {label}: {exc}", file=sys.stderr)
            return False
        if completed.returncode:
            print(f"FAIL {label}: exit {completed.returncode}", file=sys.stderr)
            if completed.stdout:
                print("stdout:\n" + completed.stdout, file=sys.stderr)
            if completed.stderr:
                print("stderr:\n" + completed.stderr, file=sys.stderr)
            return False
        print(f"PASS {entry['id']}")
        return True


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("primer_pos", nargs="?", type=Path, help="primer directory containing examples/manifest.toml")
    parser.add_argument("example_pos", nargs="*", help="run only these example IDs")
    parser.add_argument("--repo-root", type=Path, default=REPO_ROOT, help="repository root containing the primer")
    parser.add_argument("--primer", dest="primer_option", type=Path, help="primer directory, relative to --repo-root or absolute")
    parser.add_argument("--example", action="append", default=[], help="run only the named example (repeatable)")
    args = parser.parse_args(argv)
    try:
        if args.primer_pos is not None and args.primer_option is not None:
            parser.error("use either a positional primer or --primer, not both")
        primer_arg = args.primer_option or args.primer_pos
        if primer_arg is None:
            parser.error("a primer directory is required")
        repo_root = args.repo_root.resolve()
        primer = primer_arg if primer_arg.is_absolute() else repo_root / primer_arg
        entries = load_manifest(primer, repo_root)
        requested = args.example + args.example_pos
        missing = set(requested) - {entry["id"] for entry in entries}
        if missing:
            raise ManifestError(f"unknown example IDs: {', '.join(sorted(missing))}")
        oci = os.environ.get("OCI") or ("podman" if shutil.which("podman") else "docker")
        if oci not in ("podman", "docker") or not shutil.which(oci):
            raise ManifestError(f"container runtime unavailable: {oci}")
        selected = [entry for entry in entries if not requested or entry["id"] in requested]
        for entry in selected:
            if not run_example(oci, primer.resolve(), entry, repo_root):
                return 1
        return 0
    except ManifestError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
