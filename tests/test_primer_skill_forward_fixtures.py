import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
FIXTURES = ROOT / "tests/fixtures/primer_evidence"
HANDOFF_SKILL = ROOT / ".agents/skills/primer-handoff/SKILL.md"


class PrimerSkillForwardFixtureTests(unittest.TestCase):
    def test_executed_shallow_case_is_explicitly_calibrated(self):
        case = FIXTURES / "executed-shallow"
        for name in ("brief.md", "primer.md", "audit.md", "expected-review.md"):
            self.assertTrue((case / name).is_file(), name)
        audit = (case / "audit.md").read_text()
        expected = (case / "expected-review.md").read_text()
        self.assertIn("| executed |", audit)
        self.assertIn("teaching-depth gap", expected)

    def test_handoff_example_separates_content_and_release_decisions(self):
        # This checks the written example's structure, not native skill execution.
        skill = HANDOFF_SKILL.read_text()
        lines = skill.splitlines()
        header = "| Decision | Status | Evidence and revision | Blockers | Next action | Owner |"
        start = lines.index(header)

        def cells(line):
            return [cell.strip() for cell in line.strip().strip("|").split("|")]

        decisions = [cells(line) for line in lines[start + 2:start + 4]]
        self.assertEqual([len(row) for row in decisions], [6, 6])
        content, release = decisions
        self.assertEqual(content[:2], ["Content gate", "Pass"])
        self.assertEqual(release[:2], ["Release readiness", "Blocked"])
        for row in decisions:
            self.assertTrue(all(row[2:]), row)
        self.assertIn("revision", content[2])
        self.assertIn("revision", release[2])
        self.assertIn("unavailable", release[3])
        self.assertIn("actual check", skill)
        self.assertIn("historical evidence, not a current check", skill)
        self.assertIn("unavailable, not passed", skill)


if __name__ == "__main__":
    unittest.main()
