# Primer skill forward-test protocol (#408)

This protocol defines future behavioural probes of `primer-plan`,
`primer-audit` and `primer-handoff`. No provider invocation or behavioural
result is recorded by creating this document. The fixture expectations are
human review targets, not labels inferred by the structural checker.

## Setup and boundaries

Choose the exact revision containing the skills and fixtures to be tested.
Use a disposable checkout with no concurrent writer. Record the full commit
ID, branch, any dirty changes, fixture paths and content hashes, and the full
revision or hashes of the three skill files and applicable guidance. Do not
compare results from different revisions as though the inputs were identical.
Record the harness and version, model identifier, reasoning effort, settings,
working directory, date and time, and any relevant permission controls. If the
harness cannot expose a setting or activation evidence, record it as unknown.

Run each prompt in a **fresh, independent session**, explicitly invoking the
named skill through the harness's native mechanism. Use read-only filesystem
permissions and prohibit writes, edits, builds, commits, network access and
subagents in the prompt and harness settings where supported. Capture responses
and logs outside the checkout. Do not supply expected-review notes or the
outcome of another probe to a session under test. Record the exact command,
complete prompt and activation evidence, including whether the native skill was
actually loaded. If native activation is unavailable, record that limitation;
a separately labelled manual-file fallback does not prove native activation.
Stop and report an unavailable provider, refused request, incomplete run or
uncertain activation; none is a pass.

Before and after each session, record `git status --porcelain=v1 --untracked-files=all`,
`git diff --binary`, `git diff --cached --binary`, and the full `HEAD` ID.
Also compare an inventory and content hashes of all files in the checkout,
including ignored files and symlinks, excluding Git administrative data; store
both inventories outside the checkout. Record exact inventory commands and
comparison results. Account for pre-existing changes rather than removing them.
A matching snapshot provides evidence of no persistent checkout changes, not
proof that no transient write was attempted. Record enforcement or tool logs
separately when available. A changed checkout or missing comparison makes
no-write verification fail or remain unverified; preserve evidence and stop.

## Prompts and observations

Replace `<native invocation>` with the harness's explicit skill syntax and
record the actual substituted prompt. Use the fixture paths relative to the
checkout root. These probes are deliberately bounded; the synthetic fixture is
not a complete primer or a real revision-bound audit.

### Planning

```text
<native invocation: primer-plan>
Work read-only. Do not edit files, invoke subagents, run builds, or access the
network. Using tests/fixtures/primer_evidence/valid/brief.md as a synthetic
brief, propose an in-response plan for a reader to estimate steady-state loss.
Identify the route and concept IDs, the required reasoning, a worked transition,
interpretation, limitation, and unresolved evidence. Do not draft a primer or
create a tracked brief. State what you inspected and what remains unverified.
```

Human review checks whether the plan connects input, balance, calculation,
result and limitation to the promised reader action, identifies missing evidence
and respects the boundary. A populated matrix alone is not sufficient.

### Audit

Run the following twice, in separate fresh sessions, once with `<case>` set to
`valid` and once to `shallow`. Do not reveal the expected judgement in the
prompt. The fixture's revision strings and readiness claims are synthetic.

```text
<native invocation: primer-audit>
Work read-only. Do not edit files, invoke subagents, run builds, or access the
network. Review tests/fixtures/primer_evidence/<case>/brief.md,
audit.md and primer.md as a bounded synthetic case, not a complete primer.
For route-one / concept-one, inspect the actual passage and report exact
locators, reasoning, worked operation and result, interpretation, limitation,
status and readiness consequence. Assess whether the audit's claimed status is
supported. State the scope and evidence limitations; do not repair the files.
```

After both runs, compare each response with its fixture's
`expected-review.md`. The shallow audit row is deliberately misleading: a
primary-route depth gap blocks readiness even when the structural checker
passes. Record unsupported claims, missed gaps, false positives and exact
response evidence. A correct fixture judgement does not establish a complete
primer audit.

### Required calibration cases

The forward-test set must also include these two cases. They are separate from
the structural evidence checker because both require human judgement about
whether the evidence teaches and whether a later review actually re-evaluated
changed material.

1. **Executed but shallow:** use `tests/fixtures/primer_evidence/executed-shallow/`.
   The operation is marked `executed` and the command/result may be present,
   but the reader-facing passage omits intermediate reasoning or interpretation.
   The structural checker may pass; the audit must still record a teaching-depth
   gap and block the affected primary route.
2. **Source changed, audit rebound:** use
   `tests/fixtures/primer_evidence/revision-replay/`. Compare the original
   source and audit with the changed source and a metadata-only rebound. A
   rebound that changes revision labels without recording affected passages,
   transitions, claims and a fresh judgement must fail the process test. A
   second audit that records those items may pass.

Record the response and judgement for each case separately. Do not count a
passing executable command, a changed revision string, or a structurally valid
table as proof of teaching depth or re-audit completeness.

### Handoff

```text
<native invocation: primer-handoff>
Work read-only. Do not edit files, invoke subagents, run builds, or access the
network. Prepare an in-response handoff for the synthetic case in
tests/fixtures/primer_evidence/shallow/: inspect brief.md, audit.md and
primer.md, and report the live checkout state, route and concept IDs,
evidence revision, reviewer, findings, readiness, checks actually performed,
limitations, next action and owner. Treat the fixture's revision and readiness
claims as claims to assess. Do not repair files or release anything.
```

Human review checks whether the handoff reports the missing intermediate
reasoning and result as a blocking primary-route gap, separates fixture claims
from observed evidence, and avoids inventing checks or authorising release.

## Results record template

Copy this section outside the test checkout for each independent invocation;
retain a durable reviewed record in an authorised location after the tests.
Do not include secrets, private transcripts or hidden reasoning.

- Date/time and operator:
- Case and skill; native activation mechanism and observed evidence:
- Harness/version, model identifier, effort and relevant settings:
- Checkout path, branch, full HEAD, dirty state and applicable permissions:
- Source/fixture paths and hashes; brief, audit, evidence and skill revisions
  or hashes; relevant guidance revisions:
- Exact command and complete prompt:
- Run outcome: completed / incomplete / unavailable; reason if applicable:
- Response or log location and relevant excerpts/locators:
- Human findings against the criteria, including false positives and misses:
- Scope, unverified claims and limitations:
- No-write controls, exact before/after inventory and Git commands, comparison
  results and any observed attempted writes:
- Conclusion for this invocation: supported / failed / inconclusive, with
  rationale; follow-up and owner:

Report each invocation separately. A single favourable response is evidence
only for the recorded inputs and runtime, not a general reliability claim.

## Preliminary subagent behavioural probes (not native activation)

Three read-only subagent behavioural probes were run against the skills at
branch HEAD `2acd65aeda7f829cfb542d7501c0e07d67139dfb`, using the knowledge-
graph input at branch HEAD `535f0fb4119eda5c447f52e21c77928eaa49ee0e`:

- **Plan probe:** blocked drafting because there were no route-keyed traces,
  the R handoff was unresolved, and expansion and scope decisions were
  missing.
- **Audit probe:** identified the primary gaps as curated temporal inputs,
  Q1–Q3 operation-to-result links, evaluation adjudication, and interpretation
  of `tidygraph` on the alternative route.
- **Handoff probe:** separated recorded content, render, evidence and freshness
  status. It found the synthetic shallow fixture's missing calculation and
  result to be a blocking gap.

These were subagent behavioural probes, not native Codex skill activation.
No provider calls or builds ran, and no files were edited during the probes.
The scope was limited to these three probe responses, the stated branch-HEAD
inputs and the synthetic fixture where applicable; this is not a native
forward-test result or evidence of general skill reliability. Native forward-
test results remain outstanding.
