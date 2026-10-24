#!/usr/bin/env python3
"""Offline consistency checks for the repository's committed documents."""

import argparse
from collections import Counter
from dataclasses import dataclass
from html.parser import HTMLParser
from pathlib import Path
import re
import sys

sys.dont_write_bytecode = True
sys.path.insert(0, str(Path(__file__).resolve().parent))
from git_history import GitHistory


ROOT = Path(__file__).resolve().parents[2]
MONTHS = "January February March April May June July August September October November December".split()
DATE_RE = re.compile(r"(?:[1-9]|[12][0-9]|3[01]) (?=" + "|".join(MONTHS) + r")(?:" + "|".join(MONTHS) + r") [0-9]{4}|(?:" + "|".join(MONTHS) + r") [0-9]{4}\Z")
ASSIGN_RE = re.compile(r'^([A-Z][A-Z_]+)\s*:=\s*"([^"]*)"', re.M)
RECIPE_RE = re.compile(r'(?m)^([\w-]+):[^\n]*\n((?:(?:  |\t)[^\n]*\n|\n)*)')
RENDER_RE = re.compile(r'([\w.-]+\.md)\s+-o\s+([\w.-]+\.html)')
META_RE = re.compile(r'--metadata\s+(title|author|date)="([^"]*)"')
FENCE_RE = re.compile(r'^ {0,3}(`{3,}|~{3,})(.*)$')
RAW_MERMAID_RE = re.compile(r'graph (?:LR|TB)|subgraph|stroke-dasharray|\{\.mermaid\}')
HEADING_RE = re.compile(r'^ {0,3}(#{1,6})(?:[ \t]+|$)(.*)$')
NAVIGATION_ONLY = '<!-- check-structure: navigation-only -->'


@dataclass(frozen=True)
class Document:
    source: Path
    html: Path
    title: str
    author: str
    date: str
    justfile: Path
    html_extra: str


def fail(message):
    print(message, file=sys.stderr)
    return 1


def documents():
    found = []
    for justfile in sorted(ROOT.glob("primer_*/Justfile")) + [ROOT / "gaming_silo_rpg/Justfile"]:
        body = justfile.read_text()
        variables = dict(ASSIGN_RE.findall(body))
        directory = justfile.parent.relative_to(ROOT)
        def add(source, html, metadata):
            found.append(Document(directory / source, directory / html,
                metadata.get("title", variables["TITLE"]),
                metadata.get("author", variables["AUTHOR"]),
                metadata.get("date", variables["DATE"]),
                justfile.relative_to(ROOT), next((line for line in body.splitlines() if line.startswith("HTML_EXTRA")), "")))
        source = variables["SOURCE_MD"]
        add(source, Path(source).with_suffix(".html").name, {})
        for _, recipe in RECIPE_RE.findall(body):
            expanded = recipe.replace("\\\n", " ")
            for name, value in variables.items():
                expanded = expanded.replace("{{" + name + "}}", value)
            match = RENDER_RE.search(expanded)
            if not match:
                continue
            metadata = dict(META_RE.findall(expanded))
            if match.group(1) == source and not metadata:
                continue
            add(*match.groups(), metadata)
        if "REFERENCE_MD" in variables and not any(d.source == directory / variables["REFERENCE_MD"] for d in found):
            raise RuntimeError(f"{justfile}: REFERENCE_MD has no built HTML recipe")
    # Explicit recipes replace the imported source recipe's metadata for Silo index.
    by_source = {item.source: item for item in found}
    return list(by_source.values())


def outside_fences(source):
    marker = None
    for line in source.splitlines():
        match = FENCE_RE.match(line)
        if marker:
            if match and match.group(1)[0] == marker[0] and len(match.group(1)) >= len(marker) and not match.group(2).strip():
                marker = None
            continue
        if match:
            marker = match.group(1)
            yield ("fence", match.group(2).strip())
        else:
            yield ("text", line)


def first_h1(source):
    for kind, line in outside_fences(source):
        if kind == "text" and line.startswith("# "):
            return re.sub(r"\s+#+\s*$", "", line[2:]).strip()
    return None


def without_comments(line, in_comment):
    """Remove HTML comments, including comments spanning source lines."""
    visible = []
    position = 0
    while position < len(line):
        if in_comment:
            end = line.find('-->', position)
            if end < 0:
                return ''.join(visible), True
            position = end + 3
            in_comment = False
        else:
            start = line.find('<!--', position)
            if start < 0:
                visible.append(line[position:])
                break
            visible.append(line[position:start])
            position = start + 4
            in_comment = True
    return ''.join(visible), in_comment


def is_prose_line(line):
    """Recognise ordinary paragraph text, not other Markdown block types."""
    stripped = line.strip()
    if not stripped or re.match(r'(?:[-*+]\s|\d+[.)]\s|>|\||:::|\$\$|\\\[|!\[|<|(?:---+|___+|\*\*\*+)\s*$)', stripped):
        return False
    if re.fullmatch(r'\[[^]]+\]\([^)]+\)', stripped):
        return False
    return bool(re.search(r'[A-Za-z]{2,}', without_inline_code(stripped)))


def structural_findings(source):
    """Return (line number, H2 title) for H2s lacking prose before their first H3.

    A navigation-only H2 may put <!-- check-structure: navigation-only -->
    on the first nonblank line after its heading. This is a report-only
    diagnostic; whether the prose is substantive remains a review decision.
    """
    findings = []
    h2 = None
    has_prose = False
    navigation_only = False
    marker_slot = False
    fence = None
    in_comment = False
    for number, raw in enumerate(source.splitlines(), 1):
        if fence:
            match = FENCE_RE.match(raw)
            if match and match.group(1)[0] == fence[0] and len(match.group(1)) >= len(fence) and not match.group(2).strip():
                fence = None
            continue
        if not in_comment and h2 and marker_slot and raw.strip() == NAVIGATION_ONLY:
            navigation_only = True
            marker_slot = False
            continue
        line, in_comment = without_comments(raw, in_comment)
        match = FENCE_RE.match(line)
        if match:
            fence = match.group(1)
            marker_slot = False
            continue
        heading = HEADING_RE.match(line)
        if heading:
            level = len(heading.group(1))
            if level <= 2:
                h2 = (number, re.sub(r'\s+#+\s*$', '', heading.group(2)).strip()) if level == 2 else None
                has_prose = False
                navigation_only = False
                marker_slot = level == 2
            elif level == 3 and h2:
                if not has_prose and not navigation_only:
                    findings.append(h2)
                h2 = None
            continue
        if line.strip():
            marker_slot = False
        if h2 and is_prose_line(line):
            has_prose = True
    return findings


def check_structure(paths):
    """Print advisory findings without affecting the command's exit status."""
    count = 0
    for path in paths:
        for number, title in structural_findings(path.read_text()):
            print(f"{path}:{number}: ADVISORY: H2 {title!r} has an H3 before any prose")
            count += 1
    print(f"check-structure: {len(paths)} Markdown files, {count} advisory findings")
    return 0


def known_mismatches():
    known = {}
    path = ROOT / "lint/check-meta-known.txt"
    for number, line in enumerate(path.read_text().splitlines(), 1):
        if line.startswith("#"):
            continue
        match = re.fullmatch(r"([^|]+)\s+\|\s+(.+)", line)
        if not match or not match.group(2).strip():
            raise RuntimeError(f"{path}:{number}: expected path | reason")
        known[match.group(1).strip()] = match.group(2).strip()
    return known


def check_meta(docs):
    known = known_mismatches()
    seen = set()
    errors = []
    for doc in docs:
        actual = first_h1((ROOT / doc.source).read_text())
        if actual != doc.title:
            key = doc.source.as_posix()
            if key in known:
                seen.add(key)
            else:
                errors.append(f"{doc.justfile}: {key}: TITLE {doc.title!r} != H1 {actual!r}")
        for name, value in (("AUTHOR", doc.author), ("DATE", doc.date)):
            if name == "DATE" and not DATE_RE.fullmatch(value):
                errors.append(f"{doc.justfile}: {doc.source}: invalid DATE {value!r}")
            if name == "AUTHOR" and (not re.search(r"[A-Za-z]", value) or DATE_RE.fullmatch(value)):
                errors.append(f"{doc.justfile}: {doc.source}: invalid AUTHOR {value!r}")
    errors.extend(f"{key}: obsolete known mismatch" for key in sorted(known.keys() - seen))
    for error in errors:
        fail(error)
    print(f"check-meta: {len(docs)} documents, {len(seen)} known title mismatches")
    return bool(errors)


def without_inline_code(line):
    return re.sub(r'(`+)(.*?)\1', '', line)


def has_maths(source):
    text = "\n".join(without_inline_code(line) for kind, line in outside_fences(source) if kind == "text")
    text = re.sub(r"\\\$", "", text)
    return bool(re.search(r"\$\$(?=\S)[\s\S]*?\$\$|(?<!\$)\$(?![\s$])[^\n$]*?\$(?!\$)", text))


def check_variants(docs):
    errors = []
    for doc in docs:
        html = ROOT / doc.html
        stem = html.with_suffix("")
        variants = [Path(str(stem) + suffix) for suffix in (".mathml.html", ".mathjax.html")]
        present = [path.exists() for path in variants]
        toggle = 'id="math-mode-toggle"' in html.read_text()
        opt_in = "mathvariants=true" in doc.html_extra if doc.source.name == dict(ASSIGN_RE.findall((ROOT / doc.justfile).read_text())).get("SOURCE_MD") else False
        maths = has_maths((ROOT / doc.source).read_text())
        if any(present) != all(present) or toggle != all(present) or opt_in != all(present):
            errors.append(f"{doc.html}: toggle={toggle}, variants={present}, opt-in={opt_in}")
        if any(present) and not maths:
            errors.append(f"{doc.source}: variants exist without source maths")
        for path in variants:
            if path.exists() and 'id="math-mode-toggle"' not in path.read_text():
                errors.append(f"{path.relative_to(ROOT)}: missing toggle")
    for error in errors:
        fail(error)
    print(f"check-variants: {len(docs)} documents")
    return bool(errors)


def mermaid_captions(source):
    captions = []
    for kind, info in outside_fences(source):
        if kind == "fence" and re.search(r"(?:^|[\s.{])mermaid(?:[\s}]|$)", info):
            caption = re.search(r'caption="([^"]+)"', info)
            captions.append(caption.group(1) if caption else "Mermaid diagram")
    return Counter(captions)


class ImagesAndText(HTMLParser):
    def __init__(self):
        super().__init__()
        self.images = []
        self.raw = []
        self.skip = 0

    def handle_starttag(self, tag, attrs):
        if tag in ("script", "style"):
            self.skip += 1
        if tag == "img":
            values = dict(attrs)
            if values.get("src", "").startswith("data:image/png"):
                self.images.append(values.get("aria-label") or values.get("alt", ""))

    def handle_endtag(self, tag):
        if tag in ("script", "style"):
            self.skip -= 1

    def handle_data(self, data):
        if not self.skip and RAW_MERMAID_RE.search(data):
            self.raw.append(data[:100])


def check_mermaid(docs):
    errors = []
    paths = sorted(set(path for doc in docs for path in [doc.html, Path(str(doc.html.with_suffix("")) + ".mathml.html"), Path(str(doc.html.with_suffix("")) + ".mathjax.html")] if (ROOT / path).exists()))
    for path in paths:
        parser = ImagesAndText()
        parser.feed((ROOT / path).read_text())
        if parser.raw:
            errors.append(f"{path}: raw Mermaid text: {parser.raw[0]!r}")
        doc = next(doc for doc in docs if path == doc.html or path.name.startswith(doc.html.stem + ".math"))
        expected = mermaid_captions((ROOT / doc.source).read_text())
        actual = Counter(label for label in parser.images if label in expected)
        if actual != expected:
            errors.append(f"{path}: Mermaid images {dict(actual)} != fences {dict(expected)}")
    for error in errors:
        fail(error)
    print(f"check-mermaid: {len(paths)} HTML files")
    return bool(errors)


def check_fresh(docs):
    history = GitHistory(ROOT)
    errors = []
    for doc in docs:
        source_commit = history.last_touch(doc.source.as_posix())
        if not source_commit:
            errors.append(f"{doc.source}: no source commit")
            continue
        outputs = [doc.html]
        if doc.source.name != "primer_agent_quick_reference.md":
            outputs.append(doc.html.with_suffix(".pdf"))
        for output in outputs:
            if not (ROOT / output).exists():
                errors.append(f"{output}: missing output")
                continue
            output_commit = history.last_touch(output.as_posix())
            if not output_commit or not history.is_ancestor(source_commit, output_commit):
                errors.append(f"{output}: output commit is older than {doc.source}")
    for error in errors:
        fail(error)
    print(f"check-fresh: {len(docs)} source/output pairs")
    return bool(errors)


def main():
    parser = argparse.ArgumentParser(epilog=(
        "structure is report-only. Use <!-- check-structure: navigation-only --> "
        "as the first nonblank line after a navigation-only H2. "
        "Optional paths limit the report; by default it scans built primer Markdown."))
    parser.add_argument("check", choices=("meta", "variants", "mermaid", "fresh", "structure"))
    parser.add_argument("paths", nargs="*", type=Path, help="Markdown paths for structure (default: built primers)")
    args = parser.parse_args()
    if args.check == "structure":
        paths = args.paths or sorted({ROOT / doc.source for doc in documents() if doc.source.parts[0].startswith("primer_")})
        return check_structure(paths)
    if args.paths:
        parser.error("paths are only accepted by the structure check")
    docs = documents()
    if args.check == "meta":
        return check_meta(docs)
    if args.check == "variants":
        return check_variants(docs)
    if args.check == "mermaid":
        return check_mermaid(docs)
    return check_fresh(docs)


if __name__ == "__main__":
    try:
        sys.exit(main())
    except (OSError, RuntimeError, KeyError) as exc:
        sys.exit(f"check: {exc}")
