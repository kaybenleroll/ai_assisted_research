import importlib.util
import subprocess
import tempfile
import unittest
from pathlib import Path


SCRIPT = Path(__file__).resolve().parents[1] / "scripts/check/primer_audit.py"
SPEC = importlib.util.spec_from_file_location("primer_audit", SCRIPT)
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(MODULE)


class PrimerAuditTests(unittest.TestCase):
    def test_current_checklist_accepts_independent_decisions_and_explanations(self):
        for content, release in (("pass", "ready"), ("pass", "not-ready"), ("fail", "not-ready")):
            with self.subTest(content=content, release=release):
                text = ("## Release readiness checklist\n"
                        f"- Content gate: **{content}**, for the reviewed scope.\n"
                        f"- Release readiness: **{release}** for this release.\n"
                        "  Further detail.\n"
                        "## Historical release readiness checklist\n"
                        "- Content gate: **fail**\n- Release readiness: **ready**\n")
                self.assertEqual(MODULE.checklist_findings(text), [])

    def test_current_checklist_rejects_missing_duplicate_and_malformed_content(self):
        valid = ("## Release readiness checklist\n"
                 "- Content gate: **pass**\n- Release readiness: **ready**\n")
        cases = {
            "missing section": "## Historical release readiness checklist\n" + valid.split("\n", 1)[1],
            "heading prefix": valid.replace("checklist\n", "checklist history\n"),
            "fenced section": "```md\n" + valid + "```\n",
            "duplicate section": valid + valid,
            "historical fields": ("## Release readiness checklist\n"
                                  "## Historical release readiness checklist\n" + valid.split("\n", 1)[1]),
            "subsection fields": ("## Release readiness checklist\n### Historical\n" + valid.split("\n", 1)[1]),
            "duplicate field": valid + "- Content gate: **fail**\n",
            "malformed duplicate": valid + "Content gate: pass\n",
            "invalid value": valid.replace("**pass**", "**pending**"),
            "unbolded value": valid.replace("**ready**", "ready"),
            "joined value": valid.replace("**pass**", "**pass**fail"),
            "contradiction": valid.replace("**pass**", "**fail**"),
            "fenced fields": "## Release readiness checklist\n```\n" + valid.split("\n", 1)[1] + "```\n",
        }
        for name, text in cases.items():
            with self.subTest(name=name):
                self.assertTrue(MODULE.checklist_findings(text))

    def test_locator_lines_are_checked_against_real_files(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            (root / "primer.md").write_text("one\ntwo\n", encoding="utf-8")
            audit = root / "audit.md"
            audit.write_text("## Adversarial depth gate\nprimer.md:2 primer.md:3\n", encoding="utf-8")
            self.assertEqual(
                MODULE.locator_findings(root, audit),
                ["audit:2: locator line 3 exceeds primer.md (2 lines)"],
            )

    def git_repo(self, root):
        subprocess.run(["git", "init", "-q"], cwd=root, check=True)
        subprocess.run(["git", "config", "user.email", "test@example.invalid"], cwd=root, check=True)
        subprocess.run(["git", "config", "user.name", "Test"], cwd=root, check=True)

    def commit(self, root, message):
        subprocess.run(["git", "add", "."], cwd=root, check=True)
        subprocess.run(["git", "commit", "-qm", message], cwd=root, check=True)
        return subprocess.run(["git", "rev-parse", "HEAD"], cwd=root, text=True,
                              capture_output=True, check=True).stdout.strip()

    def test_revision_and_source_content_are_bound_to_git(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            self.git_repo(root)
            source = root / "primer.md"
            source.write_text("one\ntwo\n", encoding="utf-8")
            revision = self.commit(root, "source")
            brief = root / "brief.md"
            brief.write_text(f"- Source revision: {revision}\n", encoding="utf-8")
            audit = root / "audit.md"
            audit.write_text(
                f"- Source revision: {revision}\n- Reviewed revision: {revision}\n"
                "## Release readiness checklist\n"
                "- Content gate: **pass**\n- Release readiness: **ready**\n"
                "## Adversarial depth gate\nprimer.md:2\n", encoding="utf-8"
            )
            self.assertEqual(MODULE.validate(root, source, brief, audit), [])
            source.write_text("changed\n", encoding="utf-8")
            self.assertTrue(any("working source differs" in error
                                for error in MODULE.validate(root, source, brief, audit)))

    def test_changed_ranges_report_affected_locators(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            self.git_repo(root)
            source = root / "primer.md"
            source.write_text("one\ntwo\n", encoding="utf-8")
            audit = root / "audit.md"
            audit.write_text("## Adversarial depth gate\nprimer.md:2\n", encoding="utf-8")
            base = self.commit(root, "source")
            source.write_text("one\nchanged\n", encoding="utf-8")
            ranges = MODULE.changed_ranges(root, base, source)
            self.assertEqual(ranges, [(2, 2)])
            self.assertEqual(MODULE.impacted_locators(root, audit, ranges), ["audit:2: primer.md:2"])


if __name__ == "__main__":
    unittest.main()
