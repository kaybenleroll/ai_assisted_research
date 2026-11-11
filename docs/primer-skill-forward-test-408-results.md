# Primer Skill Forward-Test Batch Results (#408)

**Status: completed with evidence.** A fresh rerun used three detached,
read-only worktrees at commit `a88574f` and captured exact before/after Git
status, unstaged and staged binary diffs, `HEAD`, and file/symlink inventories
outside the checkout for every invocation. All ten comparisons matched exactly
(empty `cmp` output); the read-only sandbox also prevented persistent edits.
The rerun logs and snapshots are retained in `/tmp/kg-forward-rerun` for this
session. This tracked record retains the reviewed conclusions and session
identifiers rather than private or redundant transcripts.

The [protocol](primer-skill-forward-test-408.md) defines the prompts, review criteria, and complete per-invocation record. The earlier manually applied subagent probes described there are historical task observations, not native activation results for this batch. Catalogue listing in this session is discovery only.

## Batch Scope

Candidate realistic calibration inputs are the revised [primer](../primer_knowledge_graph/primer_knowledge_graph.md), [brief](../primer_knowledge_graph/primer_knowledge_graph.brief.md), [audit](../primer_knowledge_graph/primer_knowledge_graph.audit.md), and [case contract](../primer_knowledge_graph/primer_knowledge_graph.case.md). Their audit records a scoped content pass and a separate not-ready release decision; the operator of each probe must independently pin and assess the actual input revisions and hashes. The batch has not independently verified those historical claims.

The following cases are planned. Each row represents an independent fresh session, including separate sessions for both synthetic audit cases.

| Case ID | Skill | Case | Native activation | Task execution | No-write verification | Overall |
|---|---|---|---|---|---|---|
| plan-synthetic | `primer-plan` | Synthetic planning | Observed | Supported | Exact snapshot match | Supported |
| plan-revised | `primer-plan` | Revised primer calibration | Observed | Supported with five planning-document alignment findings | Exact snapshot match | Supported |
| audit-valid | `primer-audit` | Valid synthetic audit | Observed | Supported | Exact snapshot match | Supported |
| audit-shallow | `primer-audit` | Shallow synthetic audit | Observed | Failed as expected: primary teaching gap | Exact snapshot match | Supported |
| audit-executed-shallow | `primer-audit` | Executed but shallow | Observed | Failed as expected: execution does not supply teaching depth | Exact snapshot match | Supported |
| audit-revision-replay | `primer-audit` | Source changed, audit rebound | Observed | Failed as expected: metadata-only rebound | Exact snapshot match | Supported |
| audit-revised | `primer-audit` | Revised primer calibration | Observed | Supported for stated illustrative scope | Exact snapshot match | Supported |
| audit-stale | `primer-audit` | Stale baseline re-scoping | Observed | Supported: historical findings re-scoped | Exact snapshot match | Supported |
| handoff-shallow | `primer-handoff` | Blocking synthetic gap | Observed | Supported: content blocked and release blocked | Exact snapshot match | Supported |
| handoff-release | `primer-handoff` | Content pass, release blocked | Observed | Supported: content pass separated from release block | Exact snapshot match | Supported |

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
| plan-synthetic | `01a1cb5a-373c-7840-bc55-07573c3d5a53` | Built a complete balance-equation teaching plan; noted the placeholder fixture's unresolved source and uncertainty evidence. |
| plan-revised | `01a1cb5a-d44d-7191-828a-6d1a6a41fc71` | Supported the current teaching spines but identified five planning-document alignment findings for #407. |
| audit-valid | `01a1cb5c-b636-7d11-ac50-faf8611a3895` | Confirmed the narrow worked transition, but identified weak audit locators and unverified revision binding. |
| audit-shallow | `01a1cb5d-3280-7e71-9ace-45b3e3f250c4` | Correctly rejected the claimed verification and readiness; marked the primary route as a gap. |
| audit-executed-shallow | `01a1cb5d-ab96-7403-bbdd-870a407156d2` | Correctly rejected execution as a substitute for intermediate reasoning, interpretation and teaching depth. |
| audit-revision-replay | `01a1cb5d-fed8-7c70-a78e-ad145ec431ea` | Correctly rejected a metadata-only rebound as a second audit and required renewed judgement. |
| audit-revised | `01a1cb60-eed9-7393-b613-bbbbb838f2a1` | Supported the current content pass for the illustrative primary and alternative routes; preserved release blockers and status inconsistencies. |
| audit-stale | `01a1cb62-8cac-7290-977a-dc83c99f122f` | Re-scoped historical citation/layout/execution findings, retaining accessibility and synthetic-evidence limitations. |
| handoff-shallow | `01a1cb64-609c-7ad2-8f79-bee79aa44bb0` | Separated the unsupported content claim from the blocked release decision and assigned remediation ownership. |
| handoff-release | `01a1cb65-63a6-7192-9a36-306dde3de682` | Preserved the scoped content pass while keeping release blocked by accessibility and freshness evidence. |

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
The complete retained snapshot comparisons now satisfy the protocol's no-write
condition for this matrix. The issues may be closed by merging the draft PR,
subject to normal review of the recorded evidence.

This does not authorise release of the knowledge-graph primer. The current
primer's content gate remains a scoped **pass** and release readiness remains
**not-ready**. This distinction is itself part of the evidence for #412; the
shared accessibility and output-freshness blockers remain outside this batch.

Individual outcomes apply only to the recorded inputs and runtime and do not
establish general reliability beyond this forward-test matrix.
