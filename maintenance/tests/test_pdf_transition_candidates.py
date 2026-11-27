import importlib.util
import unittest
from pathlib import Path

spec = importlib.util.spec_from_file_location(
    "pdf_transition_candidates",
    Path(__file__).resolve().parents[1] / "scripts/pdf_transition_candidates.py",
)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


class CandidatesTest(unittest.TestCase):
    def test_page_numbers_and_caption_at_start(self):
        text = "Figure 1: first page\f\n Figure 2: candidate\nbody\fbody\nFigure 3: later\fFig. 4: candidate\f"
        self.assertEqual(list(module.candidates(text)), [
            (1, 2, "Figure 2: candidate"), (3, 4, "Fig. 4: candidate")
        ])

    def test_empty_extraction_is_not_a_candidate(self):
        self.assertEqual(list(module.candidates("\f\n\f")), [])


if __name__ == "__main__":
    unittest.main()
