"""Check the generated GLM maths navigation without executing JavaScript."""

import subprocess
import tempfile
import unittest
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


class NoScriptParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.in_noscript = False
        self.links = []
        self.styles = []
        self.in_style = False

    def handle_starttag(self, tag, attrs):
        if tag == "noscript":
            self.in_noscript = True
        elif self.in_noscript and tag == "a":
            self.links.append(dict(attrs).get("href"))
        elif self.in_noscript and tag == "style":
            self.in_style = True

    def handle_endtag(self, tag):
        if tag == "noscript":
            self.in_noscript = False
        elif tag == "style":
            self.in_style = False

    def handle_data(self, data):
        if self.in_style:
            self.styles.append(data)


class MathmlFallbackTest(unittest.TestCase):
    def test_default_and_explicit_mathjax_recipes_enable_fallback(self):
        for project in ("primer_glm", "primer_fluid_mechanics", "primer_numerical_analysis"):
            with self.subTest(project=project):
                result = subprocess.run(
                    ["just", "--dry-run", "--justfile", str(ROOT / project / "Justfile"), "html"],
                    check=True, capture_output=True, text=True,
                )
                self.assertIn("--metadata mathmlfallback=true", result.stderr)
                self.assertIn(f'{project}.mathml.html', result.stderr)

    def test_nonvariant_and_mathml_defaults_do_not_enable_fallback(self):
        common = ROOT / "maintenance/build/common.just"
        for extra in ("", "--mathml --metadata mathrenderer=mathml --metadata mathvariants=true"):
            with self.subTest(extra=extra), tempfile.TemporaryDirectory() as temporary:
                justfile = Path(temporary) / "Justfile"
                justfile.write_text(
                    'SOURCE_MD := "sample.md"\nPROJECT_DIR := "sample"\n'
                    'TITLE := "Sample"\nAUTHOR := "Author"\nDATE := "2026"\n'
                    f'HTML_EXTRA := "{extra}"\nPDF_EXTRA := ""\nimport "{common}"\n'
                )
                result = subprocess.run(
                    ["just", "--dry-run", "--justfile", str(justfile), "html"],
                    check=True, capture_output=True, text=True,
                )
                self.assertNotIn("--metadata mathmlfallback=true", result.stderr)

    def test_generated_variants(self):
        directory = ROOT / "primer_glm"
        for suffix in (".html", ".mathjax.html", ".mathml.html"):
            with self.subTest(suffix=suffix):
                parser = NoScriptParser()
                parser.feed((directory / ("primer_glm" + suffix)).read_text())
                self.assertIn("#math-mode-toggle { display: none; }", parser.styles)
                if suffix == ".mathml.html":
                    self.assertEqual(parser.links, [])
                else:
                    self.assertEqual(parser.links, ["primer_glm.mathml.html"])
                    self.assertTrue((directory / parser.links[0]).is_file())


if __name__ == "__main__":
    unittest.main()
