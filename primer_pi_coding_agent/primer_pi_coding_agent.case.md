# Primer teaching-case contract: Pi and Rocker daily-temperature project

- Issue and milestone: #442 Pi current-documentation refresh, historical brief pi-current-docs-v1 and source c193c88ce7f16a2145c4be27dd53f7feb6668422. The case content is unchanged in #475.
- Reader capability: distinguish a supervised host agent from an isolated analysis runtime, state expected results independently, and decide what evidence supports accepting a proposed result.
- Case purpose: link Pi's context, research, code generation and session handoff to a concrete data-quality check without treating agent output as independent validation.
- Case boundary: synthetic five-row CSV for 1–2 January 2026, station groups A and B, R/Python implementations imagined under an R 4.6.1 Rocker image. Missing-only group is excluded. The primer does not supply complete cleaners, tests, `compare_outputs.py`, requirements or lockfiles, and this refresh did not execute the project. It is an illustrative case with hand-checked expected values, not a deliverable the reader can run by copying snippets alone.

## Trace

| Stage | Description | Evidence or artefact | Status |
|---|---|---|---|
| Source inputs or assumptions | Declare allowed `ok`/`missing`, dates, exact output fields, sorting and tolerance before asking Pi to implement. Agent runs on host; analysis code runs in a constrained container. | Source CSV, prose contract, expected CSV | illustrative |
| Construction, extraction, or transformation decisions | Reject unknown flags and malformed dates; omit missing rows and missing-only groups; group valid readings by date/station. Select separate R and Python implementations and write expected result independently. | Two A values 5.1 and 6.3; one B value 3.4 | illustrative |
| Intermediate records or representation | A valid group values `[5.1, 6.3]` has count 2, total 11.4 and mean 5.70; B has count 1 and mean 3.40; the next-day all-missing group has no aggregate. | Group values, count, min, max and mean | illustrative; arithmetic checked by inspection |
| Stored or computed result | Expected rows are `2026-01-01,A,2,5.70,5.10,6.30` and `2026-01-01,B,1,3.40,3.40,3.40`. Candidate R and Python files are hypothetical until the reader supplies and runs implementations. | Expected CSV; hypothetical `outputs/daily_summary_r.csv` and `outputs/daily_summary_py.csv` | illustrative |
| Reader-facing query or operation | Build from reviewed input locks, run `just qa` in constrained containers, and compare each output to expected with exact keys/counts/min/max and 0.01 mean tolerance; separately inspect host Git diff. | Planned scripts, container commands, comparator and diff | illustrative; missing cleaner, tests, comparator and lockfiles |
| Interpretation of the result | If actual independently observed tests and comparison pass and the contract and container config are unchanged, the fixture meets these declared checks. Disagreement, malformed inputs accepted, or altered boundaries reject acceptance. | Conditional pass/failure and reviewed change list | illustrative, no present run |
| Failure mode or scope limit | No fixture proves correctness on all data, and tests written by Pi need review. Writable host Pi can alter boundary files; digest pins image identity but moving `renv` bootstrap and other dependencies constrain reproducibility. A container cannot protect files mounted writable or credentials it receives. | Explicit boundaries and unexecuted work | illustrative |
| Correction and re-evaluation | Preserve prewritten contract and expected file; diagnose a mismatch, correct implementation or declared contract only through review, then rebuild and rerun independent checks and inspect diff again. | New observed test/comparison results, if later run | illustrative, no current measurement |

## Teaching decisions

- Executable stages: none promised by this refresh. The brief's separately tested fake RPC prototype is not execution of this case.
- Illustrative stages: full fixture-to-conditional-acceptance chain, Pi tasks, image recipe, commands and comparison. Missing artefacts must be written or supplied by the reader.
- Measured stages: none in this refresh. Any historical toy project run in the primer is historical evidence only, not a present runtime pass.
- Required alternatives: R and Python use the same input, expected rows and acceptance contract while remaining independent implementations. Comparison does not prove either is universally correct.
- Expected abstentions or failures: stop for an ambiguous contract; fail unknown flag, malformed date, nonnumeric required value or output mismatch; do not claim acceptance without actual results; do not claim host Pi is isolated by the analysis container.
- Evidence and freshness plan: Rocker reproducibility guide and OCI registry identity for the index digest; primary Podman, `renv`, pip and Pi documentation for operations. Registry body hash and amd64/arm64 index entries were checked by main on 19 November; no image pull/build or runtime, external package security review, or end-to-end project run was performed.
