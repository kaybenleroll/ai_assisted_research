import importlib.util
from pathlib import Path
from tempfile import TemporaryDirectory
from unittest.mock import patch
import unittest


SCRIPT = Path(__file__).resolve().parents[1] / "scripts/render_qa.py"
SPEC = importlib.util.spec_from_file_location("render_qa", SCRIPT)
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(MODULE)


class RenderQATests(unittest.TestCase):
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
        with TemporaryDirectory(dir=MODULE.ROOT / ".scratch") as directory:
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
