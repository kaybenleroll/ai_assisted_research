import importlib.util
import tempfile
import unittest
from pathlib import Path


SCRIPT = Path(__file__).resolve().parents[1] / "scripts/check/primer_evidence.py"
SPEC = importlib.util.spec_from_file_location("primer_evidence", SCRIPT)
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(MODULE)


BRIEF = """# Primer brief: Test

- Issue and milestone: #400 validator
- Reviewed revision: abcdef1234567
- Reader: engineers
- Prerequisites: Python
- Problem and motivation: test
- Intended outcome: test
- Scope: test
- Exclusions: test
- Proposed dependency-led route: test
- Teaching-case contract: test
- Core-concept depth matrix: below
- Route classification and teaching spines: below

## Core-concept depth matrix

| Route tier | Route ID | Concept ID | Reader action | Mechanism or reasoning | Significance | Teaching device | Worked evidence | Interpretation | Limitations | Downstream use | Evidence/source plan |
|---|---|---|---|---|---|---|---|---|---|---|
| primary | route-one | concept-one | do it | explain it | matters | example | result | meaning | boundary | downstream | source |
"""


AUDIT = """# Primer audit: Test

- Starting branch: issue/400-test
- Reviewer(s): reviewer
- Date: 2026-11-10
- Reviewed revision: abcdef1234567
- Brief reviewed: docs/brief.md
- Review boundary: whole document
- Core-concept depth matrix: below
- Readiness decision: ready

## Adversarial depth gate

| Route tier | Route ID | Concept ID | Explanation locator | Example/action locator | Interpretation locator | Limitation locator | Evidence revision | Reviewer | Status | Finding | Scope decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| primary | route-one | concept-one | primer.md:10 | primer.md:20 | primer.md:30 | primer.md:40 | abcdef1234567 | reviewer | verified | checked | retained |
"""


class PrimerEvidenceTests(unittest.TestCase):
    def files(self, audit=AUDIT, brief=BRIEF):
        temp = tempfile.TemporaryDirectory()
        root = Path(temp.name)
        b, a = root / "brief.md", root / "audit.md"
        b.write_text(brief, encoding="utf-8")
        a.write_text(audit, encoding="utf-8")
        self.addCleanup(temp.cleanup)
        return b, a

    def test_valid_revision_bound_matrix(self):
        self.assertEqual(MODULE.validate(*self.files()), [])

    def test_duplicate_and_missing_coverage_are_rejected(self):
        duplicate = BRIEF.replace(
            "| primary | route-one | concept-one | route-one |",
            "| primary | route-one | concept-one | route-one |",
        )
        duplicate = BRIEF + "| primary | route-one | concept-one | do it | explain it | matters | example | result | meaning | boundary | downstream | source |\n"
        errors = MODULE.validate(*self.files(brief=duplicate))
        self.assertTrue(any("duplicate" in e for e in errors))

        extra = BRIEF.replace(
            "| primary | route-one | concept-one | do it | explain it | matters | example | result | meaning | boundary | downstream | source |",
            "| primary | route-one | concept-one | do it | explain it | matters | example | result | meaning | boundary | downstream | source |\n| primary | route-one | concept-two | do it | explain it | matters | example | result | meaning | boundary | downstream | source |",
        )
        errors = MODULE.validate(*self.files(brief=extra))
        self.assertTrue(any("missing coverage" in e for e in errors))

    def test_status_and_locator_shape_are_mechanical(self):
        audit = AUDIT.replace("| verified |", "| not-checked |", 1).replace("primer.md:10", "see chapter")
        errors = MODULE.validate(*self.files(audit=audit))
        self.assertTrue(any("invalid exact locator" in e for e in errors))
        self.assertTrue(any("blocking not-checked" in e for e in errors))

    def test_scope_reduced_requires_non_placeholder_decision(self):
        audit = AUDIT.replace("| verified | checked | retained |", "| scope-reduced | checked | <rationale> |")
        errors = MODULE.validate(*self.files(audit=audit))
        self.assertTrue(any("placeholder 'Scope decision'" in e for e in errors))

    def test_revision_mismatch_and_unknown_id_are_rejected(self):
        audit = AUDIT.replace("route-one", "other-route").replace("abcdef1234567", "123456789abcd")
        errors = MODULE.validate(*self.files(audit=audit))
        self.assertTrue(any("no matching brief" in e for e in errors))
        self.assertTrue(any("revision does not match" in e for e in errors))


if __name__ == "__main__":
    unittest.main()
