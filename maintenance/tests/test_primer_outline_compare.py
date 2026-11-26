import importlib.util
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


SCRIPT = Path(__file__).resolve().parents[1] / "scripts/check/primer_outline_compare.py"
SPEC = importlib.util.spec_from_file_location("primer_outline_compare", SCRIPT)
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


class OutlineComparisonTests(unittest.TestCase):
    def test_partial_gate_fixture_reports_only_confirmed_missing_heading(self):
        root = Path(__file__).resolve().parent / "fixtures/primer_audit_behaviour/partial-gates"
        defective = root / "case-17"
        sound = root / "case-29"
        findings = MODULE.compare((defective / "source.md").read_text(),
                                  (defective / "rendered.html").read_text())
        self.assertTrue(any("Follow-up checks" in finding for finding in findings))
        self.assertEqual(MODULE.compare((sound / "source.md").read_text(),
                                        (sound / "rendered.html").read_text()), [])

    def test_common_inline_markup_and_fenced_headings(self):
        source = ("## A *simple* [link](https://example.org) &amp; `my_code` {#intro}\n"
                  "```md\n## Not a heading\n```\n### A **child**\n")
        html = ("<h2>A <em>simple</em> <a href='https://example.org'>link</a> &amp; "
                "<code>my_code</code></h2><h3>A <strong>child</strong></h3>")
        self.assertEqual(MODULE.compare(source, html), [])

    def test_embedded_marker_is_reported_even_when_html_also_omits_heading(self):
        source = "## Models\nExplanation.## Convolutional networks\n### Filters\n"
        html = "<h2>Models</h2><p>Explanation.## Convolutional networks</p><h3>Filters</h3>"
        findings = MODULE.compare(source, html)
        self.assertTrue(any("source:2" in item and "embedded" in item for item in findings))

    def test_pandoc_level_shift_section_numbers_and_missing_cnn(self):
        source = "## Introduction\n### Background\n## Convolutional Neural Networks\n### Filters\n## Results\n"
        html = ("<header><h1>Site header</h1></header><nav id='TOC'><h1>Contents</h1></nav>"
                "<h1 id='document-title'>Primer title</h1>"
                "<h1><span class='header-section-number'>1</span> Introduction</h1>"
                "<h2><span class='header-section-number'>1.1</span> Background</h2>"
                "<p>Convolutional Neural Networks</p>"
                "<h2><span class='header-section-number'>2.1</span> Filters</h2>"
                "<h1><span class='header-section-number'>3</span> Results</h1>")
        findings = MODULE.compare(source, html)
        self.assertEqual(len(findings), 1)
        self.assertIn("Convolutional Neural Networks", findings[0])
        self.assertEqual(MODULE.compare(source.replace("## Convolutional Neural Networks\n", ""), html, -1), [])
        self.assertEqual(MODULE.compare("## A\n#### Subsection\n", "<h1>A</h1><h3>Subsection</h3>", -1), [])

    def test_typographic_apostrophes_match_without_hiding_other_differences(self):
        source = "## Reader's Model\n### ‘Quoted’ Term\n"
        html = "<h1>Reader’s Model</h1><h2>'Quoted' Term</h2>"
        self.assertEqual(MODULE.analyse(source, html), ([], -1))
        findings = MODULE.compare(source, html.replace("Model", "Models"), -1)
        self.assertTrue(any("Reader's Model" in item for item in findings))
        self.assertTrue(any("Reader’s Models" in item for item in findings))

    def test_spectral_apostrophes_and_missing_heading(self):
        source = ("### Spectral Sweeps and Cheeger's Inequality\n"
                  "### A Compact Portfolio of Small Graphs\n"
                  "### Public-Data Community Case: Zachary's Karate Club\n")
        html = ("<h2>Spectral Sweeps and Cheeger’s Inequality</h2>"
                "<h2>Public-Data Community Case: Zachary’s Karate Club</h2>")
        findings, offset = MODULE.analyse(source, html)
        self.assertEqual(offset, -1)
        self.assertEqual(len(findings), 1)
        self.assertIn("A Compact Portfolio of Small Graphs", findings[0])

    def test_apostrophes_in_code_are_not_silently_normalised(self):
        source = "## Context\n### `user's` Identifier\n"
        html = "<h2>Context</h2><h3><code>user’s</code> Identifier</h3>"
        findings = MODULE.compare(source, html)
        self.assertTrue(any("ambiguous heading conversion" in item for item in findings))
        # Even identical apostrophes in code need human review: they are literal.
        self.assertTrue(any("ambiguous heading conversion" in item
                            for item in MODULE.compare(source, html.replace("user’s", "user's"))))
        # An apostrophe only in the rendered code is still flagged.
        self.assertTrue(any("ambiguous heading conversion" in item
                            for item in MODULE.compare("## Context\n### users Identifier\n", html)))

    def test_code_span_link_syntax_is_literal(self):
        self.assertEqual(MODULE.compare("## `[x](y)`\n", "<h2><code>[x](y)</code></h2>"), [])

    def test_setext_and_nested_fences_are_flagged(self):
        source = "## Valid\nSetext heading\n--------------\n- ```md\n## Not a heading\n  ```\n"
        findings = MODULE.compare(source, "<h2>Valid</h2>", 0)
        self.assertTrue(any("Setext" in item for item in findings))
        self.assertTrue(any("nested or indented fence" in item for item in findings))
        self.assertFalse(any("Not a heading" in item for item in findings))

    def test_missing_and_reordered_headings_are_reported(self):
        findings = MODULE.compare("## First\n### Second\n## Third\n", "<h2>Third</h2><h2>First</h2>")
        self.assertTrue(any("Second" in item for item in findings))
        self.assertTrue(any("Third" in item for item in findings))

    def test_ambiguous_markup_is_never_reported_as_clean_match(self):
        findings = MODULE.compare("## ![Icon](icon.png) Name\n", "<h2><img src='icon.png'> Name</h2>")
        self.assertTrue(any("ambiguous" in item for item in findings))

    def test_cli_is_read_only_and_reports_advisory_status(self):
        with tempfile.TemporaryDirectory() as tmp:
            source, html = Path(tmp) / "source.md", Path(tmp) / "output.html"
            source.write_text("## Heading\n", encoding="utf-8")
            html.write_text("<h2>Heading</h2>", encoding="utf-8")
            result = subprocess.run([sys.executable, str(SCRIPT), str(source), str(html)], capture_output=True, text=True)
            self.assertEqual(result.returncode, 0)
            self.assertIn("human review of hierarchy", result.stdout)
            self.assertIn("offset: +0 (inferred", result.stdout)
            self.assertIn("No ATX H2/H3 candidate differences", result.stdout)
            explicit = subprocess.run([sys.executable, str(SCRIPT), str(source), str(html), "--level-offset", "0"], capture_output=True, text=True)
            self.assertEqual(explicit.returncode, 0)
            self.assertIn("offset: +0 (explicit", explicit.stdout)
            self.assertEqual(source.read_text(), "## Heading\n")
            self.assertEqual(html.read_text(), "<h2>Heading</h2>")


if __name__ == "__main__":
    unittest.main()
