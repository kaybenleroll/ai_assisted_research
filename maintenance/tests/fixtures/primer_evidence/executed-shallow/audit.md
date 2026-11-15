# Primer audit: executed shallow calibration

- Starting branch: issue/407-test
- Audit revision: audit-2
- Source revision: abcdef1234567
- Reviewer(s): reviewer
- Date: 2026-11-10
- Reviewed revision: abcdef1234567
- Brief reviewed: brief.md
- Review boundary: whole document
- Core-concept depth matrix: below
- Readiness decision: ready

## Adversarial depth gate

| Route tier | Route ID | Concept ID | Explanation locator | Example/action locator | Interpretation locator | Limitation locator | Evidence revision | Reviewer | Status | Finding | Scope decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| primary | route-one | concept-one | primer.md:3 | primer.md:3 | primer.md:5 | primer.md:5 | abcdef1234567 | reviewer | verified | Command ran | retain |

## Route transition evidence

| route_id | concept_id(s) | transition (from to) | linked input and reader operation | intermediate reasoning or decision | result | interpretation | material limitation | execution status | gap and reader consequence |
|---|---|---|---|---|---|---|---|---|---|
| route-one | concept-one | input to result | input and command | command subtracts output from input | loss=20 | loss is the unallocated input | steady operation | executed | The prose does not teach the reasoning or interpretation |
