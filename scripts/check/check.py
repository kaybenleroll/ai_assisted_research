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
EXTENSION = ROOT / "_shared/vendor/mathjax/boldsymbol.js"
EXTENSION_RE = re.compile(r"checkVersion\(\"\[tex\]/boldsymbol\",\"([0-9][^\"]*)\"")
BUNDLE_VERSION_RE = re.compile(r"\bversion:(\w+)\b")
RAW_MERMAID_RE = re.compile(r'graph (?:LR|TB)|subgraph|stroke-dasharray|\{\.mermaid\}')


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


def check_mathjax(docs):
    """The vendored boldsymbol extension must match the MathJax core embedded in each output."""
    errors = []
    match = EXTENSION_RE.search(EXTENSION.read_text())
    if not match:
        fail(f"{EXTENSION.relative_to(ROOT)}: no checkVersion for [tex]/boldsymbol")
        return True
    wanted = match.group(1)
    checked = 0
    for doc in docs:
        for suffix in (".html", ".mathjax.html"):
            path = doc.html.with_suffix("").with_name(doc.html.stem + suffix)
            if not (ROOT / path).exists():
                continue
            body = (ROOT / path).read_text()
            # The bundle exports its version through a minified constant, so find that constant by use.
            found = {v for name in BUNDLE_VERSION_RE.findall(body)
                     for v in re.findall(r"\bconst " + re.escape(name) + r"=\"([0-9]+\.[0-9]+\.[0-9]+)\"", body)}
            if not found:
                continue
            checked += 1
            if found != {wanted}:
                errors.append(f"{path}: embedded MathJax {sorted(found)} != vendored boldsymbol {wanted}")
    if not checked:
        errors.append("no output embeds a MathJax bundle; version constant not found")
    for error in errors:
        fail(error)
    print(f"check-mathjax: boldsymbol {wanted} against {checked} HTML files")
    return bool(errors)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("check", choices=("meta", "variants", "mermaid", "mathjax", "fresh"))
    args = parser.parse_args()
    docs = documents()
    if args.check == "meta":
        return check_meta(docs)
    if args.check == "variants":
        return check_variants(docs)
    if args.check == "mermaid":
        return check_mermaid(docs)
    if args.check == "mathjax":
        return check_mathjax(docs)
    return check_fresh(docs)


if __name__ == "__main__":
    try:
        sys.exit(main())
    except (OSError, RuntimeError, KeyError) as exc:
        sys.exit(f"check: {exc}")
