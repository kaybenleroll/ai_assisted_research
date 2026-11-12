import importlib.util
import os
from pathlib import Path
import shutil
import subprocess
from tempfile import TemporaryDirectory
from unittest.mock import patch
import unittest


SCRIPT = Path(__file__).resolve().parents[1] / "scripts/render_qa.py"
SPEC = importlib.util.spec_from_file_location("render_qa", SCRIPT)
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(MODULE)


class RenderQATests(unittest.TestCase):
    def test_heading_filter_preserves_shifted_tags_ids_and_numbering(self):
        pandoc = os.environ.get("PANDOC", "pandoc")
        if not shutil.which(pandoc):
            self.skipTest("Pandoc is required for the heading filter integration test")
        root = SCRIPT.parent.parent
        command = [pandoc, "--from=markdown", "--to=html", "--number-sections",
                   "--shift-heading-level-by=-1"]
        source = "## Section {#section}\n\n### Subsection {#subsection}\n"

        def render(extra):
            return subprocess.run(command + extra, input=source, text=True,
                                  capture_output=True, check=True).stdout

        original = render([])
        filtered = render([f"--lua-filter={root / '_shared/filters/html-heading-semantics.lua'}"])
        for fragment in ('<h1 data-number="1"', 'id="section"', '>1</span>',
                         '<h2 data-number="1.1"', 'id="subsection"', '>1.1</span>'):
            with self.subTest(fragment=fragment):
                self.assertIn(fragment, original)
                self.assertIn(fragment, filtered)
        audit = MODULE.HTMLAudit()
        audit.feed(filtered)
        self.assertEqual([(h["tag"], h["id"], h["aria-level"]) for h in audit.heading_details],
                         [("h1", "section", "2"), ("h2", "subsection", "3")])

    def test_page_candidates_skip_front_matter_and_find_content(self):
        pages = [
            "cover",
            "table of contents",
            "more contents",
            "ordinary prose",
            "Name   Meaning\nA   one\nB   two\nC   three\nD   four\nE   five",
            "ordinary prose\nordinary prose",
            "R code\nvertices <- data.frame()\nlibrary(igraph)",
            "Figure 1: a graph\nThe result.",
        ]
        candidates, reasons = MODULE.choose_pages("\f".join(pages))
        self.assertEqual(candidates["opening"], 1)
        self.assertEqual(candidates["table"], 5)
        self.assertEqual(candidates["code"], 7)
        self.assertEqual(candidates["figure-or-equation"], 8)
        self.assertIn("Uncertain", reasons["table"])

    def test_table_candidate_prefers_rows_to_contents_and_code(self):
        pages = [
            "cover", "contents", "contents continued",
            "Contents\n1 Introduction   7\n2 Methods   9\n3 Results   12\n4 Appendix   15",
            "R code\n" + "\n".join(f"  value{i} <- function(x)    x + {i}" for i in range(12)),
            "Results\nFit   Four neighbours   Eight neighbours\nHard   7.8874   9.3015\n"
            "Soft 0.1   8.7449   11.3494\nSoft 1   14.0720   17.9993",
        ]
        candidates, reasons = MODULE.choose_pages("\f".join(pages) + "\f")
        self.assertEqual(candidates["table"], 6)
        self.assertIn("Uncertain", reasons["table"])

    def test_fallback_is_explicit_for_code_and_contents_only(self):
        text = "cover\fintro\fintro\f1 Introduction   7\n2 Methods   9\n3 Results   12\f" + (
            "\n".join(f"  value{i} <- function(x)    x + {i}" for i in range(8))
        )
        candidates, reasons = MODULE.choose_pages(text)
        self.assertEqual(candidates["table"], 2)
        self.assertIn("Uncertain: fallback", reasons["table"])
        self.assertIn("Uncertain: fallback", MODULE.choose_pages("cover")[1]["table"])

    def test_table_can_share_page_with_code(self):
        page = (
            "  result <- function(x)    x + 1\n  print(result)\n\n"
            "Fit   Four neighbours   Eight neighbours\n"
            "Hard   7.8874   9.3015\nSoft 0.1   8.7449   11.3494\n"
            "Soft 1   14.0720   17.9993\n"
        )
        candidates, _ = MODULE.choose_pages("cover\fintro\fintro\f" + page)
        self.assertEqual(candidates["table"], 4)

    def test_html_audit_collects_ids_images_and_title(self):
        audit = MODULE.HTMLAudit()
        audit.feed('<html><head><title>Primer</title></head><body><h1 id="one">X</h1><img src="data:image/png;base64,x"></body></html>')
        self.assertEqual(audit.title, "Primer")
        self.assertEqual(audit.ids, ["one"])
        self.assertEqual(len(audit.images), 1)

    def test_semantic_html_audit_accepts_shared_template_contract(self):
        audit = MODULE.HTMLAudit()
        audit.feed("""<html><head><title>Primer</title></head><body>
        <a class='skip-link' href='#main-content'>Skip to main content</a>
        <nav id='TOC' aria-label='Table of contents'><button class='toc-toggle'
          aria-label='Toggle subsections of 1 Introduction' aria-controls='toc-subsections-1'
          aria-expanded='false'></button><ul id='toc-subsections-1'></ul></nav>
        <main id='main-content' aria-labelledby='document-title' tabindex='-1'>
          <h1 id='document-title'>Primer</h1>
          <h1 id='introduction' role='heading' aria-level='2'>Introduction</h1>
        </main></body></html>""")
        self.assertEqual(MODULE.semantic_html_errors(audit), [])

    def test_semantic_html_audit_rejects_duplicate_toggle_names_and_targets(self):
        audit = MODULE.HTMLAudit()
        audit.feed("""<a href='#main-content'>skip</a><nav id='TOC' aria-label='Table of contents'>
        <button class='toc-toggle' aria-label='Toggle subsections of Introduction'
          aria-controls='same' aria-expanded='false'></button>
        <button class='toc-toggle' aria-label='Toggle subsections of Introduction'
          aria-controls='same' aria-expanded='false'></button><ul id='same'></ul></nav>
        <main id='main-content' aria-labelledby='document-title'><h1 id='document-title'>X</h1>
        <h1 id='a' role='heading' aria-level='2'></h1></main>""")
        errors = MODULE.semantic_html_errors(audit)
        self.assertIn("TOC toggle names must be unique", errors)
        self.assertIn("TOC toggle targets must be unique", errors)

    def test_semantic_html_audit_checks_section_heading_levels(self):
        def errors(levels):
            audit = MODULE.HTMLAudit()
            headings = "".join(
                f"<h1 id='section-{i}' role='heading' aria-level='{level}'>Section</h1>"
                for i, level in enumerate(levels)
            )
            audit.feed("""<a href='#main-content'>skip</a>
                <nav id='TOC' aria-label='Table of contents'></nav>
                <main id='main-content' aria-labelledby='document-title'>
                <h1 id='document-title'>Title</h1>""" + headings + "</main>")
            return MODULE.semantic_html_errors(audit)

        message = "section heading aria-levels must start at 2 and not skip levels"
        self.assertEqual(errors([2, 3, 2]), [])
        for levels in ([3, 4], [2, 4], [1], ["invalid"]):
            with self.subTest(levels=levels):
                self.assertIn(message, errors(levels))

    def test_semantic_html_audit_rejects_missing_controlled_list(self):
        audit = MODULE.HTMLAudit()
        audit.feed("""<a href='#main-content'>skip</a><nav id='TOC' aria-label='Table of contents'>
        <button class='toc-toggle' aria-label='Toggle subsections of Introduction'
          aria-controls='missing' aria-expanded='false'></button></nav>
        <main id='main-content' aria-labelledby='document-title'><h1 id='document-title'>X</h1>
        <h1 id='a' role='heading' aria-level='2'></h1></main>""")
        self.assertIn("TOC toggles must reference existing controlled lists", MODULE.semantic_html_errors(audit))

    def test_source_for_output_strips_variant_suffixes(self):
        project = MODULE.ROOT / "primer_spectral_graph_theory"
        self.assertEqual(
            MODULE.source_for_output(project / "primer_spectral_graph_theory.mathml.html").name,
            "primer_spectral_graph_theory.md",
        )
        self.assertEqual(
            MODULE.source_for_output(project / "primer_spectral_graph_theory.pdf").name,
            "primer_spectral_graph_theory.md",
        )

    def test_tracked_output_discovery_is_limited_to_published_files(self):
        project = MODULE.ROOT / "primer_spectral_graph_theory"
        result = type("Result", (), {"stdout": (
            b"primer_spectral_graph_theory/primer_spectral_graph_theory.html\0"
            b"primer_spectral_graph_theory/primer_spectral_graph_theory.pdf\0"
            b"primer_spectral_graph_theory/Rplots.pdf\0"
        )})()
        with patch.object(MODULE.subprocess, "run", return_value=result):
            outputs = MODULE.tracked_published_outputs(project)
        self.assertEqual([path.name for path in outputs], [
            "primer_spectral_graph_theory.html",
            "primer_spectral_graph_theory.pdf",
        ])

    def test_source_image_references_ignore_fenced_examples(self):
        scratch = MODULE.ROOT / ".scratch"
        scratch.mkdir(exist_ok=True)
        with TemporaryDirectory(dir=scratch) as directory:
            source = Path(directory) / "example.md"
            source.write_text(
                "![real](figures/real.png)\n\n````markdown\n![code](figures/not-an-asset.png)\n````\n"
            )
            self.assertEqual(MODULE.source_image_references(source), ["figures/real.png"])

    def test_image_identity_reports_unavailable_inspection(self):
        result = type("Result", (), {"returncode": 1, "stderr": "not found"})()
        with patch.object(MODULE.subprocess, "run", return_value=result):
            identity = MODULE.image_identity("podman", "missing:image")
        self.assertIn("unavailable", identity)


if __name__ == "__main__":
    unittest.main()
