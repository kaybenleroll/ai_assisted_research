#!/usr/bin/env python3
"""Collect reproducible evidence for a committed primer render.

The script checks HTML locally and uses the pinned Pandoc container for PDF
metadata, text extraction, and rasterisation.  Page selection is deliberately
heuristic: the report identifies candidate pages for human visual inspection;
it does not claim to replace that inspection.
"""

from __future__ import annotations

import argparse
import base64
from io import BytesIO
from html.parser import HTMLParser
import json
import os
from pathlib import Path
import re
import shlex
import subprocess
import sys
import tarfile


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_IMAGE = "localhost/primers-pandoc:latest"
OUTPUT_SUFFIXES = (".mathml.html", ".mathjax.html", ".html", ".pdf")
COMMAND_LOG: list[str] = []


class HTMLAudit(HTMLParser):
    def __init__(self):
        super().__init__()
        self.ids: list[str] = []
        self.images: list[str] = []
        self.title = ""
        self.headings: list[str] = []
        self._in_title = False

    def handle_starttag(self, tag, attrs):
        values = dict(attrs)
        if "id" in values:
            self.ids.append(values["id"])
        if tag == "img":
            self.images.append(values.get("src", ""))
        if tag == "title":
            self._in_title = True
        if tag in {"h1", "h2", "h3"}:
            self.headings.append(tag)

    def handle_endtag(self, tag):
        if tag == "title":
            self._in_title = False

    def handle_data(self, data):
        if self._in_title:
            self.title += data


def source_stem(project: Path) -> str:
    match = re.search(r'^SOURCE_MD\s*:=\s*"([^"]+)"', (project / "Justfile").read_text(), re.M)
    if not match:
        raise SystemExit(f"{project}/Justfile: SOURCE_MD is missing")
    return Path(match.group(1)).stem


def oci_runtime() -> str:
    for candidate in ("podman", "docker"):
        if subprocess.run(["sh", "-c", f"command -v {candidate}"], capture_output=True).returncode == 0:
            return candidate
    raise RuntimeError("neither podman nor docker is available")


def tracked_published_outputs(project: Path) -> list[Path]:
    relative = project.relative_to(ROOT).as_posix()
    result = subprocess.run(
        ["git", "ls-files", "-z", "--", relative],
        cwd=ROOT,
        capture_output=True,
        check=True,
    )
    outputs = []
    for raw in result.stdout.split(b"\0"):
        if not raw:
            continue
        path = ROOT / raw.decode()
        if path.parent == project and path.name.endswith(OUTPUT_SUFFIXES) and source_for_output(path).is_file():
            outputs.append(path)
    if not outputs:
        raise RuntimeError(f"no tracked HTML/PDF outputs found for {relative}")
    return sorted(outputs)


def source_for_output(output: Path) -> Path:
    for suffix in OUTPUT_SUFFIXES:
        if output.name.endswith(suffix):
            return output.with_name(output.name[: -len(suffix)] + ".md")
    raise ValueError(f"unsupported published output: {output}")


def source_image_references(source: Path) -> list[str]:
    references = []
    in_fence = False
    image = re.compile(r"!\[[^\]]*\]\(([^)\s]+)\)")
    for line in source.read_text().splitlines():
        if line.lstrip().startswith("```"):
            in_fence = not in_fence
            continue
        if not in_fence:
            references.extend(image.findall(line))
    return [ref for ref in references if not ref.startswith(("http:", "https:", "data:", "#"))]


def git_provenance() -> tuple[str, str]:
    revision = subprocess.run(["git", "rev-parse", "HEAD"], cwd=ROOT, text=True, capture_output=True, check=True).stdout.strip()
    dirty = subprocess.run(["git", "status", "--porcelain=v1"], cwd=ROOT, text=True, capture_output=True, check=True).stdout.strip()
    return revision, dirty or "clean"


def image_identity(oci: str, image: str) -> str:
    result = subprocess.run([oci, "image", "inspect", image], text=True, capture_output=True)
    if result.returncode:
        return f"unavailable ({result.stderr.strip() or 'image inspect failed'})"
    try:
        data = json.loads(result.stdout)[0]
        image_id = data.get("Id", "unknown")
        digests = ", ".join(data.get("RepoDigests") or []) or "none reported"
        return f"id={image_id}; repo-digests={digests}"
    except (ValueError, IndexError, TypeError, KeyError):
        return "unavailable (unrecognised image inspect output)"


def run_container(args: list[str], capture=True) -> str:
    oci = os.environ.get("OCI") or oci_runtime()
    image = os.environ.get("IMAGE", DEFAULT_IMAGE)
    mount = f"{ROOT}:/work" + (":Z" if oci == "podman" else "")
    # Poppler is installed during the disposable run, so the container must
    # start as root. Raster output is streamed back as an archive so the
    # container cannot leave root-owned files in the workspace.
    flags = []
    command = [oci, "run", "--rm", *flags, "--entrypoint", "sh", "-v", mount,
               "-w", "/work", image, "-c", *args]
    COMMAND_LOG.append(shlex.join(command))
    result = subprocess.run(command, text=True, capture_output=capture)
    if result.returncode:
        raise RuntimeError(result.stderr.strip() or "container command failed")
    return result.stdout


def pdf_probe(pdf: Path) -> tuple[str, str, list[str]]:
    relative = pdf.relative_to(ROOT).as_posix()
    command = (
        "apk add --no-cache poppler-utils >/dev/null && "
        "printf '%s\\n' 'pandoc:' && pandoc --version | head -1 && "
        "printf '%s\\n' 'pdfinfo:' && pdfinfo -v 2>&1 | head -1 && "
        "printf '%s\\n' 'pdftotext:' && pdftotext -v 2>&1 | head -1 && "
        "printf '%s\\n' 'pdftoppm:' && pdftoppm -v 2>&1 | head -1 && "
        f"printf '\\n---PDFINFO---\\n' && pdfinfo {shlex.quote(relative)} && "
        f"printf '\\n---TEXT---\\n' && pdftotext -layout {shlex.quote(relative)} -"
    )
    output = run_container([command])
    versions, remainder = output.split("\n---PDFINFO---\n", 1)
    metadata, text = remainder.split("\n---TEXT---\n", 1)
    pages_match = re.search(r"^Pages:\s+(\d+)", metadata, re.M)
    if not pages_match or int(pages_match.group(1)) < 1 or not text.strip():
        raise RuntimeError(f"PDF probe found no usable pages or text: {pdf.relative_to(ROOT)}")
    return metadata, text, versions.splitlines()


def choose_pages(text: str) -> tuple[dict[str, int], dict[str, str]]:
    pages = text.rstrip("\f").split("\f")
    candidates = {"opening": 1}
    reasons = {"opening": "First page"}
    # The opening page and table of contents often contain the same words as
    # later examples. Prefer substantive pages after the front matter.
    substantive = list(enumerate(pages[3:], 4)) or list(enumerate(pages, 1))
    table_header = re.compile(r"\btable\s+\d+\b", re.I)
    table_row = re.compile(r"^\s*\S(?:.*\S)?\s{3,}\S")
    code_line = re.compile(r"<-|\b(?:def|import|from|library|function|return|for|if)\b|[{};]|(?:==|\$|\[|\]\s*<-)")
    contents_entry = re.compile(r"^\s*\d+(?:\.\d+)*\s+.+\s{3,}\d+\s*$")
    scored = []
    for i, value in substantive:
        lines = value.splitlines()
        rows = [line for line in lines if table_row.search(line) and not code_line.search(line)]
        # Contents often continues beyond page three and has aligned page numbers.
        if re.search(r"^\s*(?:table of )?contents\s*$", value, re.I | re.M):
            continue
        if rows and sum(bool(contents_entry.match(line)) for line in rows) >= max(3, len(rows) / 2):
            continue
        # A caption alone can be a reference in prose. Prefer actual aligned rows;
        # count only short runs so isolated indentation does not dominate.
        run = longest = 0
        for line in lines:
            if line in rows:
                run += 1
                longest = max(longest, run)
            elif line.strip():
                run = 0
        if longest >= 3:
            scored.append((longest, bool(table_header.search(value)), -i, i))
    table_page = max(scored)[-1] if scored else None
    if table_page:
        candidates["table"] = table_page
        reasons["table"] = "Uncertain: aligned text rows; confirm an actual table"

    code_pattern = re.compile(r"\b(import|library)\s*\(|\bdef\s+\w+\s*\(|\bfunction\s*\(|\s<-\s")
    scored = [(len(code_pattern.findall(value)), i) for i, value in substantive]
    score, code_page = max(scored, default=(0, None))
    if score < 2:
        code_page = None
    if code_page:
        candidates["code"] = code_page
        reasons["code"] = "Code-pattern match; confirm visually"

    figure_page = next((i for i, value in substantive if re.search(r"\bfigure\s+\d+\b", value, re.I)), None)
    if figure_page is None:
        figure_page = next((i for i, value in substantive if re.search(r"∑|λ|∫", value)), None)
    if figure_page:
        candidates["figure-or-equation"] = figure_page
        reasons["figure-or-equation"] = "Figure or equation pattern; confirm visually"

    fallback = max(1, len(pages) // 2)
    for label in ("table", "code", "figure-or-equation"):
        if label not in candidates:
            candidates[label] = fallback
            reasons[label] = "Uncertain: fallback page; find a suitable example"
    return candidates, reasons


def audit_html(html: Path, source: Path) -> tuple[HTMLAudit, list[str]]:
    parser_html = HTMLAudit()
    parser_html.feed(html.read_text())
    duplicate_ids = sorted({value for value in parser_html.ids if parser_html.ids.count(value) > 1})
    local_images = [src for src in parser_html.images if src and not src.startswith(("data:", "http:", "https:", "#"))]
    missing_images = [src for src in local_images if not (html.parent / src).exists()]
    source_refs = source_image_references(source)
    missing_source_assets = [ref for ref in source_refs if not (source.parent / ref).exists()]
    if not parser_html.title.strip() or not parser_html.headings:
        raise RuntimeError(f"HTML structure is incomplete: {html.relative_to(ROOT)}")
    if duplicate_ids or missing_images or missing_source_assets:
        raise RuntimeError(
            f"HTML QA failed for {html.relative_to(ROOT)}: duplicate IDs={duplicate_ids}, "
            f"missing images={missing_images}, missing source assets={missing_source_assets}"
        )
    if source_refs and len(parser_html.images) < len(source_refs):
        raise RuntimeError(
            f"HTML image parity failed for {html.relative_to(ROOT)}: "
            f"source references={len(source_refs)}, output images={len(parser_html.images)}"
        )
    return parser_html, source_refs


def raster_pages(pdf: Path, output: Path, pages: dict[str, int]) -> None:
    relative = pdf.relative_to(ROOT).as_posix()
    requests = " ".join(f"{shlex.quote(label)}:{page}" for label, page in pages.items())
    command = (
        "apk add --no-cache poppler-utils >/dev/null && mkdir -p /tmp/render-qa && "
        f"for request in {requests}; do label=${{request%%:*}}; page=${{request##*:}}; "
        f"pdftoppm -f $page -l $page -png -r 120 {shlex.quote(relative)} "
        f"/tmp/render-qa/$label >/dev/null; done; "
        "tar -czf - -C /tmp/render-qa . | base64 -w0"
    )
    encoded = run_container([command]).strip()
    output.mkdir(parents=True, exist_ok=True)
    with tarfile.open(fileobj=BytesIO(base64.b64decode(encoded)), mode="r:gz") as archive:
        archive.extractall(output, filter="data")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("project", help="primer directory, for example primer_spectral_graph_theory")
    parser.add_argument("--output", type=Path, help="evidence directory (default: .scratch/render-qa/<project>)")
    args = parser.parse_args()
    project = (ROOT / args.project).resolve()
    if project.parent != ROOT or not project.is_dir():
        parser.error("project must be a primer directory directly under the repository root")
    COMMAND_LOG.clear()
    outputs = tracked_published_outputs(project)
    for path in outputs:
        if not path.is_file() or path.stat().st_size == 0:
            raise SystemExit(f"missing or empty committed output: {path.relative_to(ROOT)}")
    html_outputs = [path for path in outputs if path.name.endswith(".html")]
    pdf_outputs = [path for path in outputs if path.name.endswith(".pdf")]
    html_audits = []
    for html in html_outputs:
        source = source_for_output(html)
        if not source.is_file():
            raise SystemExit(f"published output has no source: {html.relative_to(ROOT)} -> {source.relative_to(ROOT)}")
        parser_html, source_refs = audit_html(html, source)
        html_audits.append((html, parser_html, source_refs))

    pdf_audits = []
    all_versions = []
    for pdf in pdf_outputs:
        source = source_for_output(pdf)
        if not source.is_file():
            raise SystemExit(f"published output has no source: {pdf.relative_to(ROOT)} -> {source.relative_to(ROOT)}")
        metadata, text, versions = pdf_probe(pdf)
        pages_match = re.search(r"^Pages:\s+(\d+)", metadata, re.M)
        page_count = int(pages_match.group(1)) if pages_match else len(text.split("\f"))
        pages, reasons = choose_pages(text)
        pdf_audits.append((pdf, page_count, pages, reasons))
        all_versions.extend(versions)

    output = args.output or (ROOT / ".scratch" / "render-qa" / project.name)
    output = output.resolve()
    if output.parent != (ROOT / ".scratch" / "render-qa") and not str(output).startswith(str(ROOT / ".scratch")):
        parser.error("output must be under .scratch")
    for pdf, _page_count, pages, _reasons in pdf_audits:
        raster_output = output if len(pdf_audits) == 1 else output / pdf.stem
        raster_pages(pdf, raster_output, pages)
    report = output / "report.md"
    report.parent.mkdir(parents=True, exist_ok=True)
    oci = os.environ.get("OCI") or oci_runtime()
    image = os.environ.get("IMAGE", DEFAULT_IMAGE)
    revision, dirty = git_provenance()
    lines = [
        f"# Render QA evidence: `{project.name}`",
        "",
        "This report is generated by `just render-qa`. Page choices are heuristic candidates for human visual inspection; rasterisation is not a visual pass.",
        "",
        "## Provenance",
        "",
        f"- Git revision: `{revision}`",
        f"- Working tree: `{dirty}`",
        f"- Invocation: `{shlex.join([sys.executable, *sys.argv])}`",
        f"- OCI runtime: `{oci}`",
        f"- OCI image: `{image}`",
        f"- Image identity: `{image_identity(oci, image)}`",
        "- Tool versions:",
        *[f"  - `{version}`" for version in dict.fromkeys(all_versions) if version],
        "",
        "## Commands and outputs",
        "",
        *[f"- `{path.relative_to(ROOT)}` ({path.stat().st_size} bytes)" for path in outputs],
        "",
        "## HTML and source-asset checks",
        "",
        "| Output | Source | Title | Headings | Source images | Output images |",
        "|---|---|---|---:|---:|---:|",
        *[
            f"| `{html.relative_to(ROOT)}` | `{source_for_output(html).relative_to(ROOT)}` | {parser.title.strip()} | {len(parser.headings)} | {len(refs)} | {len(parser.images)} |"
            for html, parser, refs in html_audits
        ],
        "",
        "## Raster candidates",
        "",
        "| Output | Purpose | Page | Selection | Evidence file | Human inspection |",
        "|---|---|---:|---|---|---|",
    ]
    for pdf, page_count, pages, reasons in pdf_audits:
        prefix = "" if len(pdf_audits) == 1 else f"{pdf.stem}/"
        for label, page in pages.items():
            filename = f"{label}-{page:0{len(str(page_count))}d}.png"
            lines.append(f"| `{pdf.relative_to(ROOT)}` | {label} | {page} | {reasons[label]} | `{prefix}{filename}` | pending |")
    lines += [
        "",
        "Automated checks cover committed output presence, HTML structure, local assets, source-image assets, image-count parity, PDF metadata/text, and raster generation. They do not establish semantic correctness, factual accuracy, caption meaning, accessibility quality, or human visual acceptability.",
        "",
        "## Container commands",
        "",
        *[f"- `{command}`" for command in COMMAND_LOG],
        "",
        "Open every PNG listed above and replace `pending` with the human inspection result and any defect before using this report as release evidence.",
        "",
    ]
    report.write_text("\n".join(lines))
    print(report.relative_to(ROOT))
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (OSError, RuntimeError, ValueError) as exc:
        raise SystemExit(f"render-qa: {exc}")
