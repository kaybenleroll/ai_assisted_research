import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
FIXTURES = ROOT / "tests/fixtures/primer_evidence"


class PrimerSkillForwardFixtureTests(unittest.TestCase):
    def test_executed_shallow_case_is_explicitly_calibrated(self):
        case = FIXTURES / "executed-shallow"
        for name in ("brief.md", "primer.md", "audit.md", "expected-review.md"):
            self.assertTrue((case / name).is_file(), name)
        audit = (case / "audit.md").read_text()
        expected = (case / "expected-review.md").read_text()
        self.assertIn("| executed |", audit)
        self.assertIn("teaching-depth gap", expected)

if __name__ == "__main__":
    unittest.main()
