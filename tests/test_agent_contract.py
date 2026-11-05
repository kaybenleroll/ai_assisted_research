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
check = MODULE.check


CONTRACT = "# Project Contract\n\n" + "\n\n".join(f"## {heading}\nText." for heading in REQUIRED_H2)
ADAPTER = "# Adapter\n\nRead the [project contract](docs/project-contract.md).\n"


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
        for path in ("math-notation.md", "review-checklist.md"):
            (root / "docs" / path).write_text("x", encoding="utf-8")
        (root / "workbook_catmodel_elt_documents/README.md").write_text("x", encoding="utf-8")
        (root / "gaming_silo_rpg/gaming_silo_index.md").write_text("x", encoding="utf-8")
        (root / "AGENTS.md").write_text(ADAPTER, encoding="utf-8")
        (root / "CLAUDE.md").write_text(ADAPTER, encoding="utf-8")
        return temp, root

    def test_valid_contract(self):
        temp, root = self.make_root()
        self.addCleanup(temp.cleanup)
        self.assertEqual(check(root), [])

    def test_missing_adapter_link_is_rejected(self):
        temp, root = self.make_root()
        self.addCleanup(temp.cleanup)
        (root / "CLAUDE.md").write_text("# Adapter\n", encoding="utf-8")
        self.assertTrue(any("CLAUDE.md" in error for error in check(root)))

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
