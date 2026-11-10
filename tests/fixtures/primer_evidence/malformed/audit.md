# Primer audit: Test

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
| primary | route-one | concept-one | primer.md:10 | primer.md:20 | primer.md:30 | primer.md:40 | abcdef1234567 | reviewer | verified | Balance and assumptions reviewed | retain the concept |

## Route transition evidence

| route_id | concept_id(s) | transition (from to) | linked input and reader operation | intermediate reasoning or decision | result | interpretation | material limitation | execution status | gap and reader consequence |
|---|---|---|---|---|---|---|---|---|---|
| route-one | concept-one | input to result | input and operation | reasoning | result | interpretation | limitation | illustrative | none |
