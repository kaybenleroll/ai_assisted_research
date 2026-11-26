"""Check the observable behaviour of the practical audit calibration fixtures."""

import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


FIXTURES = Path(__file__).resolve().parent / "fixtures/primer_audit_behaviour/state-transitions"


class StateTransitionFixtureTests(unittest.TestCase):
    def run_fixture(self, name, duplicate_header=False):
        with tempfile.TemporaryDirectory() as temporary:
            target = Path(temporary) / "fixture"
            shutil.copytree(FIXTURES / name, target)
            build = subprocess.run([sys.executable, "build.py"], cwd=target, capture_output=True, text=True)
            self.assertEqual(build.returncode, 0, build.stderr)
            published = target / "published/inventory.csv"
            if duplicate_header:
                published.write_text("sensor,count,count\neast,999,4\nnorth,888,7\nwest,777,3\n")
            verification = subprocess.run([sys.executable, "verify.py"], cwd=target, capture_output=True, text=True)
            return published.read_text(), verification

    def test_faulty_publication_receives_false_pass(self):
        published, result = self.run_fixture("case-17")
        self.assertNotIn("west,3", published)
        self.assertEqual(result.returncode, 0)
        self.assertIn("PASS", result.stdout)

    def test_revised_control_checks_published_state_and_rejects_ambiguous_header(self):
        published, result = self.run_fixture("case-29")
        self.assertIn("west,3", published)
        self.assertEqual(result.returncode, 0)
        _, ambiguous = self.run_fixture("case-29", duplicate_header=True)
        self.assertNotEqual(ambiguous.returncode, 0)
        self.assertIn("wrong header", ambiguous.stderr)

    def test_original_control_reproduces_reviewers_duplicate_header_finding(self):
        _, result = self.run_fixture("case-29-original", duplicate_header=True)
        self.assertEqual(result.returncode, 0)
        self.assertIn("PASS", result.stdout)


if __name__ == "__main__":
    unittest.main()
