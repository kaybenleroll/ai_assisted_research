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
import os
from pathlib import Path
import re
import shlex
import subprocess
import sys
import tarfile


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_IMAGE = "localhost/primers-pandoc:latest"


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


def run_container(args: list[str], capture=True) -> str:
    oci = os.environ.get("OCI") or ("podman" if subprocess.run(
        ["sh", "-c", "command -v podman >/dev/null"], capture_output=True
    ).returncode == 0 else "docker")
    image = os.environ.get("IMAGE", DEFAULT_IMAGE)
    mount = f"{ROOT}:/work" + (":Z" if oci == "podman" else "")
    # Poppler is installed during the disposable run, so the container must
    # start as root. Raster output is streamed back as an archive so the
    # container cannot leave root-owned files in the workspace.
    flags = []
    command = [oci, "run", "--rm", *flags, "--entrypoint", "sh", "-v", mount,
               "-w", "/work", image, "-c", *args]
    result = subprocess.run(command, text=True, capture_output=capture)
    if result.returncode:
        raise RuntimeError(result.stderr.strip() or "container command failed")
    return result.stdout


def pdf_probe(pdf: Path) -> tuple[str, str]:
    relative = pdf.relative_to(ROOT).as_posix()
    command = f"apk add --no-cache poppler-utils >/dev/null && pdfinfo {shlex.quote(relative)} && printf '\\n---TEXT---\\n' && pdftotext -layout {shlex.quote(relative)} -"
    output = run_container([command])
    metadata, text = output.split("\n---TEXT---\n", 1)
    return metadata, text


def choose_pages(text: str) -> dict[str, int]:
    pages = text.split("\f")
    candidates = {"opening": 1}
    # The opening page and table of contents often contain the same words as
    # later examples. Prefer substantive pages after the front matter.
    substantive = list(enumerate(pages[3:], 4)) or list(enumerate(pages, 1))
    table_header = re.compile(r"\btable\s+\d+\b", re.I)
    table_rows = re.compile(r"^\s*\S(?:.*\S)?\s{3,}\S", re.M)
    table_page = next((i for i, value in substantive if table_header.search(value)), None)
    if table_page is None:
        scored = [(len(table_rows.findall(value)), i) for i, value in substantive]
        score, table_page = max(scored, default=(0, None))
        if score < 5:
            table_page = None
    if table_page:
        candidates["table"] = table_page

    code_pattern = re.compile(r"\b(import|library)\s*\(|\bdef\s+\w+\s*\(|\bfunction\s*\(|\s<-\s")
    scored = [(len(code_pattern.findall(value)), i) for i, value in substantive]
    score, code_page = max(scored, default=(0, None))
    if score < 2:
        code_page = None
    if code_page:
        candidates["code"] = code_page

    figure_page = next((i for i, value in substantive if re.search(r"\bfigure\s+\d+\b", value, re.I)), None)
    if figure_page is None:
        figure_page = next((i for i, value in substantive if re.search(r"∑|λ|∫", value)), None)
    if figure_page:
        candidates["figure-or-equation"] = figure_page

    if len(pages) > 1:
        fallback = max(1, len(pages) // 2)
        for label in ("table", "code", "figure-or-equation"):
            candidates.setdefault(label, fallback)
    return candidates


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
    stem = source_stem(project)
    html = project / f"{stem}.html"
    pdf = project / f"{stem}.pdf"
    for path in (html, pdf):
        if not path.is_file() or path.stat().st_size == 0:
            raise SystemExit(f"missing or empty committed output: {path.relative_to(ROOT)}")

    parser_html = HTMLAudit()
    parser_html.feed(html.read_text())
    duplicate_ids = sorted({value for value in parser_html.ids if parser_html.ids.count(value) > 1})
    local_images = [src for src in parser_html.images if src and not src.startswith(("data:", "http:", "https:", "#"))]
    missing_images = [src for src in local_images if not (html.parent / src).exists()]
    if not parser_html.title.strip() or not parser_html.headings:
        raise SystemExit(f"HTML structure is incomplete: {html.relative_to(ROOT)}")
    if duplicate_ids or missing_images:
        raise SystemExit(f"HTML QA failed: duplicate IDs={duplicate_ids}, missing images={missing_images}")

    metadata, text = pdf_probe(pdf)
    pages_match = re.search(r"^Pages:\s+(\d+)", metadata, re.M)
    page_count = int(pages_match.group(1)) if pages_match else len(text.split("\f"))
    pages = choose_pages(text)
    output = args.output or (ROOT / ".scratch" / "render-qa" / project.name)
    output = output.resolve()
    if output.parent != (ROOT / ".scratch" / "render-qa") and not str(output).startswith(str(ROOT / ".scratch")):
        parser.error("output must be under .scratch")
    raster_pages(pdf, output, pages)
    report = output / "report.md"
    report.parent.mkdir(parents=True, exist_ok=True)
    lines = [
        f"# Render QA evidence: `{project.name}`",
        "",
        "This report is generated by `just render-qa`. Page choices are heuristic candidates for human visual inspection; rasterisation is not a visual pass.",
        "",
        "## Commands and outputs",
        "",
        f"- HTML: `{html.relative_to(ROOT)}` ({html.stat().st_size} bytes)",
        f"- PDF: `{pdf.relative_to(ROOT)}` ({pdf.stat().st_size} bytes; {page_count} pages)",
        "- PDF tools: installed inside the configured Pandoc container for this run",
        f"- HTML title: {parser_html.title.strip()}",
        f"- HTML headings: {len(parser_html.headings)}; embedded images: {len(parser_html.images)}",
        "- Duplicate HTML IDs: none",
        "- Missing local HTML images: none",
        "",
        "## Raster candidates",
        "",
        "| Purpose | Page | Evidence file | Human inspection |",
        "|---|---:|---|---|",
    ]
    for label, page in pages.items():
        lines.append(f"| {label} | {page} | `{label}-*.png` | pending |")
    lines += ["", "Update the final column after opening each PNG and record any layout defect in the PR.", ""]
    report.write_text("\n".join(lines))
    print(report.relative_to(ROOT))
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (OSError, RuntimeError, ValueError) as exc:
        raise SystemExit(f"render-qa: {exc}")
