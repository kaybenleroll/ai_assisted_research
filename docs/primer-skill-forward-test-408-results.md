# Primer Skill Forward-Test Batch Results (#408)

**Status: intentionally inconclusive.** This record defines the outstanding batch; no fresh native invocation or task-execution result is claimed here. The operator has not run the protocol in an isolated, disposable checkout with before-and-after inventories. The shared checkout has concurrent work, so it cannot supply the protocol's required independent no-write evidence for this batch. Whether a suitable native activation mechanism and observable activation logs are available in a fresh session remains unverified.

The [protocol](primer-skill-forward-test-408.md) defines the prompts, review criteria, and complete per-invocation record. The earlier manually applied subagent probes described there are historical task observations, not native activation results for this batch. Catalogue listing in this session is discovery only.

## Batch Scope

Candidate realistic calibration inputs are the revised [primer](../primer_knowledge_graph/primer_knowledge_graph.md), [brief](../primer_knowledge_graph/primer_knowledge_graph.brief.md), [audit](../primer_knowledge_graph/primer_knowledge_graph.audit.md), and [case contract](../primer_knowledge_graph/primer_knowledge_graph.case.md). Their audit records a scoped content pass and a separate not-ready release decision; the operator of each probe must independently pin and assess the actual input revisions and hashes. The batch has not independently verified those historical claims.

The following cases are planned. Each row represents an independent fresh session, including separate sessions for both synthetic audit cases.

| Case ID | Skill | Case | Native activation | Task execution | No-write verification | Overall |
|---|---|---|---|---|---|---|
| plan-synthetic | `primer-plan` | Synthetic planning | Unknown | Not run | Not run | Inconclusive |
| audit-valid | `primer-audit` | Valid synthetic audit | Unknown | Not run | Not run | Inconclusive |
| audit-shallow | `primer-audit` | Shallow synthetic audit | Unknown | Not run | Not run | Inconclusive |
| audit-executed-shallow | `primer-audit` | Executed but shallow | Unknown | Not run | Not run | Inconclusive |
| audit-revision-replay | `primer-audit` | Source changed, audit rebound | Unknown | Not run | Not run | Inconclusive |
| audit-revised | `primer-audit` | Revised primer calibration | Unknown | Not run | Not run | Inconclusive |
| audit-stale | `primer-audit` | Stale baseline re-scoping | Unknown | Not run | Not run | Inconclusive |
| handoff-shallow | `primer-handoff` | Blocking synthetic gap | Unknown | Not run | Not run | Inconclusive |
| handoff-release | `primer-handoff` | Content pass, release blocked | Unknown | Not run | Not run | Inconclusive |

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

Until all required cases have reviewed records, this batch remains inconclusive. Individual outcomes apply only to their recorded inputs and runtime and do not establish general reliability.
