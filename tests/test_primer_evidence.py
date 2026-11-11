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
- Brief revision: brief-1
- Source revision: abcdef1234567
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
- Audit revision: audit-1
- Source revision: abcdef1234567
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

## Route transition evidence

| route_id | concept_id(s) | transition (from to) | linked input and reader operation | intermediate reasoning or decision | result | interpretation | material limitation | execution status | gap and reader consequence |
|---|---|---|---|---|---|---|---|---|---|
| route-one | concept-one | input to result | input and operation | reasoning | result | interpretation | limitation | illustrative | none |
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

    def test_populated_unmodified_template_passes_and_statuses_block(self):
        template = (SCRIPT.parents[2] / "docs/templates/primer-audit.md").read_text(encoding="utf-8")
        metadata = {
            "Audit revision": "audit-1", "Source revision": "abcdef1234567",
            "Starting branch": "infra/407-test", "Reviewer(s)": "reviewer",
            "Date": "2026-11-10", "Reviewed revision": "abcdef1234567",
            "Brief reviewed": "docs/brief.md at brief-1", "Review boundary": "whole document",
            "Core-concept depth matrix": "below", "Readiness decision": "ready",
        }
        lines = template.splitlines()
        for i, line in enumerate(lines):
            for field, value in metadata.items():
                if line.startswith(f"- {field}:"):
                    lines[i] = f"- {field}: {value}"
        audit = "\n".join(lines)
        depth_row = ("| route-one | primary | concept-one | primer.md:10 | primer.md:20 | "
                     "primer.md:30 | primer.md:40 | abcdef1234567 | reviewer | verified | checked | retained |")
        transition_row = ("| route-one | concept-one | input to result | input and operation | reasoning | "
                          "result | interpretation | limitation | illustrative | none |")
        audit = audit.replace("| | | | | | | | | | | | |", depth_row, 1)
        audit = audit.replace("| | | | | | | | | | |", transition_row, 1)
        self.assertEqual(MODULE.validate(*self.files(audit=audit)), [])
        for tier in ("primary", "alternative"):
            for status in ("gap", "not-checked"):
                with self.subTest(tier=tier, status=status):
                    changed_brief = BRIEF.replace("| primary |", f"| {tier} |")
                    changed_audit = audit.replace("| route-one | primary |", f"| route-one | {tier} |").replace(
                        "| verified | checked | retained |", f"| {status} | checked | retained |")
                    errors = MODULE.validate(*self.files(audit=changed_audit, brief=changed_brief))
                    self.assertTrue(any(f"blocking {status}" in error for error in errors), errors)

    def test_valid_revision_bound_matrix(self):
        self.assertEqual(MODULE.validate(*self.files()), [])

    def test_transition_table_is_required_in_its_section(self):
        audit = AUDIT.split("## Route transition evidence")[0]
        errors = MODULE.validate(*self.files(audit=audit))
        self.assertTrue(any("required section 'Route transition evidence'" in e for e in errors))
        self.assertTrue(any("audit transition: required matrix table" in e for e in errors))

    def test_invalid_execution_status_and_missing_evidence(self):
        audit = AUDIT.replace("| illustrative |", "| guessed |").replace("| reasoning |", "| |")
        errors = MODULE.validate(*self.files(audit=audit))
        self.assertTrue(any("invalid execution status" in e for e in errors))
        self.assertTrue(any("missing or placeholder 'intermediate reasoning or decision'" in e for e in errors))
        audit = AUDIT.replace("| reasoning |", "| MISSING — not reviewed |")
        self.assertTrue(any("missing or placeholder" in e for e in MODULE.validate(*self.files(audit=audit))))

    def test_unresolved_transition_and_route_coverage(self):
        audit = AUDIT.replace("| verified |", "| not-checked |", 1).replace(
            "- Readiness decision: ready", "- Readiness decision: not-ready").replace(
            "| illustrative |", "| not-checked |").replace("| reasoning |", "| MISSING — not reviewed |")
        self.assertEqual(MODULE.validate(*self.files(audit=audit)), [])
        errors = MODULE.validate(*self.files(audit=AUDIT.replace("| illustrative |", "| proposed |")))
        self.assertTrue(any("cannot support a verified concept" in e for e in errors))
        errors = MODULE.validate(*self.files(audit=AUDIT.replace("| route-one | concept-one | input to result", "| unknown | concept-one | input to result")))
        self.assertTrue(any("missing coverage for route" in e for e in errors))
        self.assertTrue(any("no matching brief route/concept ID" in e for e in errors))

    def test_transition_multiple_concepts_are_checked(self):
        brief = BRIEF + "| primary | route-one | concept-two | do it | explain it | matters | example | result | meaning | boundary | downstream | source |\n"
        audit = AUDIT.replace("\n\n## Route transition evidence", "\n| primary | route-one | concept-two | primer.md:10 | primer.md:20 | primer.md:30 | primer.md:40 | abcdef1234567 | reviewer | verified | checked | retained |\n\n## Route transition evidence").replace("| route-one | concept-one | input to result", "| route-one | concept-one, concept-two | input to result")
        self.assertEqual(MODULE.validate(*self.files(audit=audit, brief=brief)), [])

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

    def test_unresolved_rows_may_record_missing_evidence(self):
        audit = AUDIT.replace("primer.md:10", "MISSING — not reviewed").replace(
            "primer.md:20", "MISSING — not reviewed").replace(
            "primer.md:30", "MISSING — not reviewed").replace(
            "primer.md:40", "MISSING — not reviewed").replace(
            "- Readiness decision: ready", "- Readiness decision: not-ready").replace(
                "| verified |", "| not-checked |", 1)
        self.assertEqual(MODULE.validate(*self.files(audit=audit)), [])

    def test_empty_and_malformed_matrices_are_rejected(self):
        empty_brief = BRIEF[:BRIEF.rfind("| primary |")]
        errors = MODULE.validate(*self.files(brief=empty_brief))
        self.assertTrue(any("at least one row" in e for e in errors))

        malformed = BRIEF + "| primary | route-two | concept-two | incomplete |\n"
        errors = MODULE.validate(*self.files(brief=malformed))
        self.assertTrue(any("malformed matrix row" in e for e in errors))


if __name__ == "__main__":
    unittest.main()
