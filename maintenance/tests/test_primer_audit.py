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

OUTLINE = ("## Outline and hierarchy review\n- Rendered contents: **checked**, at the reviewed revision.\n"
           "| Actual section and hierarchy at reviewed revision | Purpose and parent/child relationship | Adjacent sibling boundary and rationale | Finding and disposition |\n"
           "|---|---|---|---|\n| Introduction | Establishes context | Precedes foundations | Retain |\n")


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

    def test_structural_gate_is_optional_but_constrains_readiness_when_present(self):
        for structural, release, valid in ((None, "ready", True), ("pass", "ready", True),
                                           ("pass", "not-ready", True), ("fail", "not-ready", True),
                                           ("not-checked", "not-ready", True), ("fail", "ready", False),
                                           ("not-checked", "ready", False)):
            with self.subTest(structural=structural, release=release):
                gate = f"- Structural gate: **{structural}**, with evidence.\n" if structural else ""
                text = (OUTLINE if structural == "pass" else "") + ("## Release readiness checklist\n- Content gate: **pass**\n" + gate
                        + f"- Release readiness: **{release}**\n")
                self.assertEqual(not MODULE.checklist_findings(text), valid)

    def test_structural_gate_rejects_malformed_and_duplicate_current_entries(self):
        valid = ("## Release readiness checklist\n- Content gate: **pass**\n"
                 "- Structural gate: **pass**\n- Release readiness: **ready**\n")
        for text in (valid.replace("**pass**\n- Release", "pass\n- Release"),
                     valid.replace("**pass**\n- Release", "**pending**\n- Release"),
                     valid + "- Structural gate: **pass**\n",
                     valid + "Structural gate: pass\n"):
            with self.subTest(text=text):
                self.assertTrue(MODULE.checklist_findings(text))

    def test_structural_gate_ignores_fenced_and_historical_entries(self):
        text = (OUTLINE + "## Release readiness checklist\n- Content gate: **pass**\n"
                "- Structural gate: **pass**\n- Release readiness: **ready**\n"
                "```md\n- Structural gate: **fail**\n```\n"
                "## Historical release readiness checklist\n- Structural gate: **fail**\n")
        self.assertEqual(MODULE.checklist_findings(text), [])

    def test_outline_review_requires_structural_gate(self):
        checklist = ("## Release readiness checklist\n- Content gate: **pass**\n"
                     "- Release readiness: **not-ready**\n")
        self.assertEqual(MODULE.checklist_findings(checklist), [])
        findings = MODULE.checklist_findings("## Outline and hierarchy review\nReview.\n" + checklist)
        self.assertTrue(any("exactly one Structural gate" in finding for finding in findings))
        for decision in ("pass", "fail", "not-checked"):
            with self.subTest(decision=decision):
                text = ((OUTLINE if decision == "pass" else "## Outline and hierarchy review\nReview.\n") + checklist
                        + f"- Structural gate: **{decision}**\n")
                self.assertEqual(MODULE.checklist_findings(text), [])

    def test_structural_pass_requires_outline_evidence_and_rendered_contents(self):
        checklist = ("## Release readiness checklist\n- Content gate: **pass**\n"
                     "- Structural gate: **pass**\n- Release readiness: **ready**\n")
        self.assertEqual(MODULE.checklist_findings(OUTLINE + checklist), [])
        cases = {
            "missing section": checklist,
            "duplicate section": OUTLINE + OUTLINE + checklist,
            "empty row": OUTLINE.replace("| Introduction | Establishes context | Precedes foundations | Retain |", "| | | | |") + checklist,
            "placeholder": OUTLINE.replace("Retain", "TBD") + checklist,
            "incomplete row": OUTLINE.replace("| Retain |", "| |") + checklist,
            "missing rendered check": OUTLINE.replace("- Rendered contents: **checked**, at the reviewed revision.\n", "") + checklist,
            "rendered not checked": OUTLINE.replace("**checked**", "**not-checked**") + checklist,
            "fenced evidence": OUTLINE.replace("| Introduction", "```\n| Introduction").replace("| Retain |\n", "| Retain |\n```\n") + checklist,
            "fenced section": "```md\n" + OUTLINE + "```\n" + checklist,
            "incomplete following row": OUTLINE + "| Other | Purpose | not-checked | not-checked |\n" + checklist,
            "conflicting rendered status": OUTLINE + "- Rendered contents: **not-checked**\n" + checklist,
            "malformed rendered duplicate": OUTLINE + "Rendered contents: checked\n" + checklist,
            "fence interrupts table": OUTLINE.replace("| Introduction", "```\nexample\n```\n| Introduction") + checklist,
        }
        for name, text in cases.items():
            with self.subTest(name=name):
                self.assertTrue(MODULE.checklist_findings(text))

    def test_fenced_and_historical_outline_headings_do_not_require_gate(self):
        text = ("```md\n## Outline and hierarchy review\n```\n"
                "## Historical audit\n### Outline and hierarchy review\n"
                "## Historical Outline and hierarchy review\n"
                "## Release readiness checklist\n- Content gate: **pass**\n"
                "- Release readiness: **ready**\n")
        self.assertEqual(MODULE.checklist_findings(text), [])

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

    def test_opt_in_source_read_coverage_ranges_and_gate(self):
        def audit(coverage, gate="pass", release="ready"):
            return (OUTLINE + (f"- Source read coverage: {coverage}\n" if coverage is not None else "")
                    + "## Release readiness checklist\n- Content gate: **pass**\n"
                    + f"- Structural gate: **{gate}**\n- Release readiness: **{release}**\n")

        source = b"one\ntwo\nthree"  # Last line need not end in a newline.
        for coverage in ("1-3", "2-2, 1-1, 3-3"):
            with self.subTest(coverage=coverage):
                self.assertEqual(MODULE.coverage_findings(audit(coverage), source), [])
        for coverage in ("1-2", "2-3", "1-1, 3-3", "none", "1-4", "0-2", "2-1",
                         "1-2, 2-3", "1-3, 1-3", "1", "1-3,", "pending"):
            with self.subTest(coverage=coverage):
                self.assertTrue(MODULE.coverage_findings(audit(coverage), source))
        for gate in ("fail", "not-checked"):
            text = audit("1-2", gate, "not-ready")
            self.assertEqual(MODULE.coverage_findings(text, source), [])
            self.assertEqual(MODULE.checklist_findings(text), [])
        self.assertTrue(MODULE.coverage_findings(audit("none"), b""))
        self.assertEqual(MODULE.coverage_findings(audit("none", "not-checked", "not-ready"), b""), [])
        self.assertTrue(MODULE.coverage_findings(audit("1-1"), b""))
        self.assertEqual(MODULE.coverage_findings(audit(None), source), [])
        self.assertTrue(MODULE.coverage_findings(audit("1-3") + "", b"one\ntwo\nthree\nfour\n"))
        duplicate = audit("1-3").replace("## Release readiness", "- Source read coverage: 1-3\n## Release readiness")
        self.assertTrue(MODULE.coverage_findings(duplicate, source))
        fenced = audit(None).replace("## Release readiness", "```md\n- Source read coverage: 1-1\n```\n## Release readiness")
        self.assertEqual(MODULE.coverage_findings(fenced, source), [])

    def test_schema_two_requires_coverage_in_current_outline(self):
        checklist = ("## Release readiness checklist\n- Content gate: **pass**\n"
                     "- Structural gate: **pass**\n- Release readiness: **ready**\n")
        prefix = "# Audit\n- Audit schema: 2\n"
        full = prefix + OUTLINE + "- Source read coverage: 1-2\n" + checklist
        self.assertEqual(MODULE.coverage_findings(full, b"one\ntwo\n"), [])
        missing = full.replace("- Source read coverage: 1-2\n", "")
        misplaced = missing + "- Source read coverage: 1-2\n"
        duplicate = full + "- Source read coverage: 1-2\n"
        for text in (missing, misplaced, duplicate, full.replace("schema: 2", "schema: 3"),
                     full.replace("- Audit schema: 2\n", "- Audit schema: 2\n- Audit schema: 2\n")):
            with self.subTest(text=text):
                self.assertTrue(MODULE.coverage_findings(text, b"one\ntwo\n"))
        partial = full.replace("1-2", "1-1").replace("**pass**\n- Release readiness", "**not-checked**\n- Release readiness").replace("**ready**", "**not-ready**")
        self.assertEqual(MODULE.coverage_findings(partial, b"one\ntwo\n"), [])
        self.assertEqual(MODULE.checklist_findings(partial), [])
        self.assertTrue(MODULE.coverage_findings(full.replace("1-2", "1-1"), b"one\ntwo\n"))
        self.assertEqual(MODULE.coverage_findings(missing.replace("- Audit schema: 2\n", ""), b"one\ntwo\n"), [])

    def test_coverage_is_bound_to_the_reviewed_source_revision(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            self.git_repo(root)
            source = root / "primer.md"
            source.write_bytes(b"one\ntwo")
            revision = self.commit(root, "source")
            brief, audit = root / "brief.md", root / "audit.md"
            brief.write_text(f"- Source revision: {revision}\n", encoding="utf-8")
            audit.write_text(f"- Source revision: {revision}\n- Reviewed revision: {revision}\n"
                             + OUTLINE + "- Source read coverage: 1-2\n"
                             + "## Release readiness checklist\n- Content gate: **pass**\n"
                             + "- Structural gate: **pass**\n- Release readiness: **ready**\n", encoding="utf-8")
            self.assertEqual(MODULE.validate(root, source, brief, audit), [])
            source.write_bytes(b"one\ntwo\nthree")
            self.assertTrue(any("working source differs" in error for error in MODULE.validate(root, source, brief, audit)))
            newer = self.commit(root, "changed source")
            audit.write_text(audit.read_text().replace(f"Reviewed revision: {revision}", f"Reviewed revision: {newer}"))
            self.assertTrue(any("resolve to different commits" in error for error in MODULE.validate(root, source, brief, audit)))

    def test_schema_two_coverage_end_to_end_at_reviewed_git_revision(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            self.git_repo(root)
            source = root / "primer.md"
            source.write_bytes(b"one\ntwo\nthree\nfour\nfive")
            revision = self.commit(root, "five source lines")
            brief, audit = root / "brief.md", root / "audit.md"
            brief.write_text(f"- Source revision: {revision}\n", encoding="utf-8")
            text = (f"# Audit\n- Audit schema: 2\n- Source revision: {revision}\n"
                    f"- Reviewed revision: {revision}\n" + OUTLINE
                    + "- Source read coverage: 1-3, 4-5\n"
                    + "## Release readiness checklist\n- Content gate: **pass**\n"
                    + "- Structural gate: **pass**\n- Release readiness: **ready**\n")
            audit.write_text(text, encoding="utf-8")
            self.assertEqual(MODULE.validate(root, source, brief, audit), [])
            audit.write_text(text.replace("1-3, 4-5", "1-3"), encoding="utf-8")
            self.assertTrue(any("complete Source read coverage" in error
                                for error in MODULE.validate(root, source, brief, audit)))
            source.write_bytes(b"one\ntwo\nthree\nfour\nfive\nsix\n")
            newer = self.commit(root, "six source lines")
            audit.write_text(text.replace(f"Reviewed revision: {revision}",
                                          f"Reviewed revision: {newer}"), encoding="utf-8")
            self.assertTrue(any("resolve to different commits" in error
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
