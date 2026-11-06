import importlib.util
from pathlib import Path
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
        candidates = MODULE.choose_pages("\f".join(pages))
        self.assertEqual(candidates["opening"], 1)
        self.assertEqual(candidates["table"], 5)
        self.assertEqual(candidates["code"], 7)
        self.assertEqual(candidates["figure-or-equation"], 8)

    def test_html_audit_collects_ids_images_and_title(self):
        audit = MODULE.HTMLAudit()
        audit.feed('<html><head><title>Primer</title></head><body><h1 id="one">X</h1><img src="data:image/png;base64,x"></body></html>')
        self.assertEqual(audit.title, "Primer")
        self.assertEqual(audit.ids, ["one"])
        self.assertEqual(len(audit.images), 1)


if __name__ == "__main__":
    unittest.main()
