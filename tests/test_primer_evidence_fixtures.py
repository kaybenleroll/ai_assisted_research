import subprocess
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts/check/primer_evidence.py"
FIXTURES = ROOT / "tests/fixtures/primer_evidence"


class PrimerEvidenceFixtureTests(unittest.TestCase):
    def run_fixture(self, name):
        case = FIXTURES / name
        self.assertTrue((case / "brief.md").is_file(), f"missing brief fixture: {case}")
        self.assertTrue((case / "audit.md").is_file(), f"missing audit fixture: {case}")
        return subprocess.run(
            [sys.executable, "-I", str(SCRIPT), str(case / "brief.md"), str(case / "audit.md")],
            capture_output=True, text=True, check=False,
        )

    def test_valid_pairs_pass(self):
        # Both audit pairs pass the shape check; expected-review.md records human
        # judgements separately. This test does not assess prose quality.
        for name in ("valid", "reference-not-checked", "shallow"):
            with self.subTest(fixture=name):
                result = self.run_fixture(name)
                self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
                self.assertIn("primer evidence check passed", result.stdout)

    def test_invalid_pairs_fail_for_the_expected_reason(self):
        cases = {
            "empty": "required matrix table is missing",
            "malformed": "malformed matrix row",
            "duplicate-unknown": "duplicate route_id/concept_id",
            "invalid-status": "invalid status",
            "stale-revision": "revision does not match",
            "primary-blocker": "blocking gap",
            "alternative-blocker": "blocking not-checked",
        }
        for name, diagnostic in cases.items():
            with self.subTest(fixture=name):
                result = self.run_fixture(name)
                self.assertEqual(result.returncode, 1, result.stdout + result.stderr)
                self.assertIn(diagnostic, result.stdout)


if __name__ == "__main__":
    unittest.main()
