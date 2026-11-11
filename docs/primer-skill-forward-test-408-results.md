# Primer Skill Forward-Test Batch Results (#408)

**Status: task evidence completed; protocol close-out remains inconclusive.** Fresh native Codex sessions were run in three detached, read-only worktrees at commit `76eb5b566a225f74c52d38be1d85c07d7f535813`. The CLI logs observed the named skill invocation in each session. Post-run Git status and diffs were clean, and the read-only sandbox prevented persistent edits. A complete before/after inventory comparison was not retained for every invocation, so the protocol's strongest no-write condition remains unverified. Full CLI transcripts remain in the authorised temporary evidence directory `/tmp/kg-forward-*`; this tracked record retains the reviewed conclusions and session identifiers rather than private or redundant transcripts.

The [protocol](primer-skill-forward-test-408.md) defines the prompts, review criteria, and complete per-invocation record. The earlier manually applied subagent probes described there are historical task observations, not native activation results for this batch. Catalogue listing in this session is discovery only.

## Batch Scope

Candidate realistic calibration inputs are the revised [primer](../primer_knowledge_graph/primer_knowledge_graph.md), [brief](../primer_knowledge_graph/primer_knowledge_graph.brief.md), [audit](../primer_knowledge_graph/primer_knowledge_graph.audit.md), and [case contract](../primer_knowledge_graph/primer_knowledge_graph.case.md). Their audit records a scoped content pass and a separate not-ready release decision; the operator of each probe must independently pin and assess the actual input revisions and hashes. The batch has not independently verified those historical claims.

The following cases are planned. Each row represents an independent fresh session, including separate sessions for both synthetic audit cases.

| Case ID | Skill | Case | Native activation | Task execution | No-write verification | Overall |
|---|---|---|---|---|---|---|
| plan-synthetic | `primer-plan` | Synthetic planning | Observed | Supported | Post-run clean; full inventory not retained | Task supported; protocol inconclusive |
| audit-valid | `primer-audit` | Valid synthetic audit | Observed | Supported | Post-run clean; full inventory not retained | Task supported; protocol inconclusive |
| audit-shallow | `primer-audit` | Shallow synthetic audit | Observed | Failed as expected: primary teaching gap | Post-run clean; full inventory not retained | Task supported; protocol inconclusive |
| audit-executed-shallow | `primer-audit` | Executed but shallow | Observed | Failed as expected: execution does not supply teaching depth | Post-run clean; full inventory not retained | Task supported; protocol inconclusive |
| audit-revision-replay | `primer-audit` | Source changed, audit rebound | Observed | Failed as expected: metadata-only rebound | Post-run clean; full inventory not retained | Task supported; protocol inconclusive |
| audit-revised | `primer-audit` | Revised primer calibration | Observed | Supported for stated illustrative scope | Post-run clean; full inventory not retained | Task supported; protocol inconclusive |
| audit-stale | `primer-audit` | Stale baseline re-scoping | Observed | Supported: historical findings re-scoped | Post-run clean; full inventory not retained | Task supported; protocol inconclusive |
| handoff-shallow | `primer-handoff` | Blocking synthetic gap | Observed | Supported: content blocked and release blocked | Post-run clean; full inventory not retained | Task supported; protocol inconclusive |
| handoff-release | `primer-handoff` | Content pass, release blocked | Observed | Supported: content pass separated from release block | Post-run clean; full inventory not retained | Task supported; protocol inconclusive |

## Per-Invocation Record

For each run, add a separate entry with the fields below. Record unavailable information explicitly; do not replace it with an inferred pass. Keep full logs in an authorised durable location and link stable, non-sensitive excerpts or locators here.

- Case ID, date/time, operator and independent reviewer.
- Harness and version, model and effort, relevant settings, working directory, and permissions.
- Checkout branch, full HEAD and dirty state; input paths, hashes and revisions for source, fixtures, brief, audit, skills and guidance.
- Exact command and complete prompt, including the native invocation; run outcome and reason for any interruption.
- **Native activation:** mechanism, observed evidence and locator, status observed / not observed / unknown, and limitations. Record discovery and manual application separately.
- **Task execution:** response or log locator, criteria, exact supporting evidence, human findings, false positives, misses, limitations, and status supported / failed / inconclusive.
- No-write controls; exact before-and-after Git and inventory commands and comparison results; attempted writes or unavailable evidence.
- Overall supported / failed / inconclusive, rationale, next action and owner. A supported result requires observed native activation, supported task execution and a passed no-write comparison.

## Reviewed native results

All sessions used Codex `0.167.0`, model `gpt-6.1-sol`, medium reasoning, an
ephemeral session, and `read-only` sandboxing. The native activation finding is
based on the CLI session transcript showing the named `$primer-plan`,
`$primer-audit`, or `$primer-handoff` invocation and the model explicitly
loading the corresponding skill. Task-execution findings are separate from
that activation evidence. The session IDs are retained for traceability:

| Case | Session | Reviewed conclusion |
|---|---|---|
| plan-synthetic | `01a1cb49-782e-7ce0-9d6c-3767d4e5d1cd` | Built a complete balance-equation teaching plan; noted the placeholder fixture's unresolved source and uncertainty evidence. |
| audit-valid | `01a1cb4a-409e-74e1-8d69-9c9af557e4b4` | Confirmed the narrow worked transition, but identified weak audit locators and unverified revision binding. |
| audit-shallow | `01a1cb4b-fdc6-71a1-9cc2-5ba00293674a` | Correctly rejected the claimed verification and readiness; marked the primary route as a gap. |
| audit-executed-shallow | `01a1cb4c-a06a-7010-b963-0cb1c5f674f8` | Correctly rejected execution as a substitute for intermediate reasoning, interpretation and teaching depth. |
| audit-revision-replay | `01a1cb4d-12c6-7bd2-8ebd-5123e7292c8c` | Correctly rejected a metadata-only rebound as a second audit and required renewed judgement. |
| audit-revised | `01a1cb4d-b7f7-7933-b46c-36a090e50c47` | Supported the current content pass for the illustrative primary and alternative routes; preserved release blockers and status inconsistencies. |
| audit-stale | `01a1cb54-1787-7e43-91b8-44be0fc739d7` | Re-scoped historical citation/layout/execution findings, retaining accessibility and synthetic-evidence limitations. |
| handoff-shallow | `01a1cb4f-8b10-7370-8b35-98e40cfa0292` | Separated the unsupported content claim from the blocked release decision and assigned remediation ownership. |
| handoff-release | `01a1cb50-6f33-7ef3-8a9f-cfd9c4d52003` | Preserved the scoped content pass while keeping release blocked by accessibility and freshness evidence. |

The current-primer planning calibration (`primer-plan`, session
`01a1cb52-47c4-7d10-99e3-18ade865db76`) additionally found five planning-
document alignment issues: the case contract still describes the superseded
executable-primary promise; it lacks revision and route/concept binding; it
lacks an explicit post-draft checkpoint; transfer applications and branch
costs are under-mapped; and output-status wording is contradictory. These are
valid #407 findings and do not require changing the primer in this batch.

## Gate and issue disposition

The task judgements support the behavioural acceptance criteria for #408 and
the content-depth criteria exercised by #406. The handoff separation and the
current planning calibration support #412 and #407 respectively. The tests
also demonstrate the required negative controls: shallow teaching, executed
but shallow teaching, and metadata-only re-audit all fail rather than pass.
However, the missing retained before/after inventory comparison means the
protocol-level acceptance is not yet complete and the issues should remain
open until that evidence is captured or the protocol is explicitly amended.

This does not authorise release of the knowledge-graph primer. The current
primer's content gate remains a scoped **pass** and release readiness remains
**not-ready**. This distinction is itself part of the evidence for #412; the
shared accessibility and output-freshness blockers remain outside this batch.

Individual outcomes apply only to the recorded inputs and runtime and do not
establish general reliability beyond this forward-test matrix.
