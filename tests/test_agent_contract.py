import tempfile
import unittest
import importlib.util
from pathlib import Path

VALIDATOR = Path(__file__).resolve().parents[1] / "scripts/check_agent_contract.py"
SPEC = importlib.util.spec_from_file_location("check_agent_contract", VALIDATOR)
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(MODULE)
REQUIRED_H2 = MODULE.REQUIRED_H2
SKILLS = MODULE.SKILLS
check = MODULE.check


CONTRACT = "# Project Contract\n\n" + "\n\n".join(f"## {heading}\nText." for heading in REQUIRED_H2)
ADAPTER = "# Adapter\n\nRead the [project contract](docs/project-contract.md).\n"
ROUTER = "\n".join(
    f"[`{skill}`](../.agents/skills/{skill}/SKILL.md)" for skill in SKILLS
)


class AgentContractTests(unittest.TestCase):
    def make_root(self):
        temp = tempfile.TemporaryDirectory()
        root = Path(temp.name)
        (root / "docs").mkdir()
        (root / "gaming_silo_rpg").mkdir()
        (root / "workbook_catmodel_elt_documents").mkdir()
        (root / "docs/project-contract.md").write_text(CONTRACT, encoding="utf-8")
        for path in ("CONTRIBUTING.md", "STYLE_GUIDE.md"):
            (root / path).write_text("x", encoding="utf-8")
        for path in ("math-notation.md", "review-checklist.md", "agent-collaboration.md"):
            (root / "docs" / path).write_text("x", encoding="utf-8")
        (root / "workbook_catmodel_elt_documents/README.md").write_text("x", encoding="utf-8")
        (root / "gaming_silo_rpg/gaming_silo_index.md").write_text("x", encoding="utf-8")
        (root / "AGENTS.md").write_text(ADAPTER, encoding="utf-8")
        (root / "docs/primer-workflow-skills.md").write_text(ROUTER, encoding="utf-8")
        for skill in SKILLS:
            skill_dir = root / ".agents/skills" / skill
            skill_dir.mkdir(parents=True)
            (skill_dir / "SKILL.md").write_text("x", encoding="utf-8")
        return temp, root

    def test_valid_contract(self):
        temp, root = self.make_root()
        self.addCleanup(temp.cleanup)
        self.assertEqual(check(root), [])

    def test_missing_adapter_link_is_rejected(self):
        temp, root = self.make_root()
        self.addCleanup(temp.cleanup)
        (root / "AGENTS.md").write_text("# Adapter\n", encoding="utf-8")
        self.assertTrue(any("AGENTS.md" in error for error in check(root)))

    def test_missing_agents_is_rejected(self):
        temp, root = self.make_root()
        self.addCleanup(temp.cleanup)
        (root / "AGENTS.md").unlink()
        self.assertTrue(any("missing AGENTS.md" in error for error in check(root)))

    def test_root_claude_is_rejected(self):
        temp, root = self.make_root()
        self.addCleanup(temp.cleanup)
        (root / "CLAUDE.md").write_text("# Obsolete\n", encoding="utf-8")
        self.assertTrue(any("root CLAUDE.md" in error for error in check(root)))

    def test_missing_skill_link_is_rejected(self):
        temp, root = self.make_root()
        self.addCleanup(temp.cleanup)
        router = root / "docs/primer-workflow-skills.md"
        router.write_text(ROUTER.replace(ROUTER.splitlines()[0], "`primer-plan`"), encoding="utf-8")
        self.assertTrue(any("skill primer-plan must link" in error for error in check(root)))

    def test_wrong_and_duplicate_skill_links_are_rejected(self):
        temp, root = self.make_root()
        self.addCleanup(temp.cleanup)
        router = root / "docs/primer-workflow-skills.md"
        wrong = "[`primer-plan`](../.agents/skills/primer-audit/SKILL.md)"
        router.write_text(ROUTER + "\n" + wrong, encoding="utf-8")
        self.assertTrue(any("skill primer-plan must link" in error for error in check(root)))
        router.write_text(ROUTER.replace(ROUTER.splitlines()[0], wrong), encoding="utf-8")
        self.assertTrue(any("skill primer-plan must link" in error for error in check(root)))

    def test_missing_skill_target_is_rejected(self):
        temp, root = self.make_root()
        self.addCleanup(temp.cleanup)
        (root / ".agents/skills/primer-audit/SKILL.md").unlink()
        self.assertTrue(any("skill link target is missing" in error for error in check(root)))

    def test_missing_skill_router_is_rejected(self):
        temp, root = self.make_root()
        self.addCleanup(temp.cleanup)
        (root / "docs/primer-workflow-skills.md").unlink()
        self.assertIn("missing docs/primer-workflow-skills.md", check(root))

    def test_reordered_heading_is_rejected(self):
        temp, root = self.make_root()
        self.addCleanup(temp.cleanup)
        text = (root / "docs/project-contract.md").read_text(encoding="utf-8")
        text = text.replace("## Purpose and Scope", "## FIRST", 1)
        text = text.replace("## Task Routing", "## Purpose and Scope", 1)
        text = text.replace("## FIRST", "## Task Routing", 1)
        (root / "docs/project-contract.md").write_text(text, encoding="utf-8")
        self.assertTrue(any("H2 sequence" in error for error in check(root)))


if __name__ == "__main__":
    unittest.main()
