# Primer Audit Behaviour Calibration

This record supports [#490](https://github.com/kaybenleroll/ai_assisted_research/issues/490).
It reports a scoped independent reading, not a complete primer audit or a
general reliability estimate. The source and guidance were at commit
`7575a008b027bba0bcb9808e3848bec7c9851722` on 26 November 2026.

## Spectral graph theory: unnamed guidance selection

- **Question:** In an independent, unnamed-guidance task, what can a reviewer
  observe about a real primer's reader journey and explanatory depth?
- **Prompt:** “Independent, read-only assessment in
  /home/mcooney/workspace/ai_assisted_research at main
  7575a008b027bba0bcb9808e3848bec7c9851722. Please assess whether
  primer_spectral_graph_theory has a coherent reader journey and sufficient
  explanatory depth, with specific locations and concrete examples of gaps
  and strengths. Inspect relevant repository instructions as normally
  appropriate to your task. You are not alone; do not modify tracked files,
  make commits, contact GitHub or delegate. Keep a concise factual record of
  the instructions and files you chose to consult, your actual actions,
  findings, limitations and exact commands or observations, returning them
  to the parent. Do not inspect other agents' worktrees or scratch trial
  materials. Stop after the report.”
- **Inputs:** `primer_spectral_graph_theory/primer_spectral_graph_theory.md`,
  SHA-256 `37a27a61a40eeb81bb3c35253de5be4483a92c1529ff5f8b01db9c017ed4cf7c`;
  `.agents/skills/primer-audit/SKILL.md`, SHA-256
  `8b0744aff0d49efead38f6bac7b3f93b0e660988cec95db28ae361d07f32d3f5`.
  The reviewer did not report a brief or rendered-output revision separately.
- **Configuration:** independent collaboration subagent, `gpt-6.1-terra`,
  medium effort, read-only task. The parent provided the prompt and received
  a final report; the underlying event record was unavailable to the parent.
- **Selection and actions:** the reviewer reported choosing and reading the
  audit skill, project contract and targeted style and review guidance,
  inventorying headings and source length, and sampling source passages. The
  prompt did not name a skill. The catalogue establishes discovery only; the
  reported read is self-reported selection, not an independently observed
  native activation event. The final report supplies no complete command log.
- **Findings:** the reviewer described strengths in the opening, kernel proof,
  sweep procedure and cross-operator synthesis. They identified practice
  exercises 5–6 as lacking worked cut and volume ledgers, and exercise 9 as
  lacking eigenvalues or modal coefficients for a numerical comparison. They
  considered the extension section a roadmap and noted that its sufficiency
  depends on the promised recognition or reference scope. The reviewer made
  no whole-document verdict: they reported sampling rather than reading all
  2,251 lines, and did not inspect rendered outputs, execute calculations or
  run build or audit checks.
- **Adjudication:** the record author checked source lines 1565–1593 and
  2184–2213 at the pinned revision. The practice asks for cut comparisons
  and sweep conductances but its self-check gives general outcomes rather
  than intermediate ledgers; this supports the stated feedback limitation.
  Exercise 9 gives no numerical modal values, but a symbolic comparison is
  possible; the reviewer acknowledged a qualitative comparison. The extension
  introduction expressly calls it an optional roadmap. Whether it meets any
  particular brief promise was not independently assessed, so the concern is
  not adjudicated as a defect or false positive. No exhaustive miss or false
  positive assessment was possible for this open-ended sample.
- **Truncation:** the reviewer reported one truncated combined output and a
  bounded reread of key excerpts. The delivered payload and retry events were
  unavailable for independent inspection; real truncation and autonomous
  recovery are unverified. This is not a controlled recovery trial.
- **Retention and limits:** the parent supplied the exact task prompt and a
  privacy-reviewed final report; this record retains only the relevant summary.
  Raw events are unavailable to the parent, and no private transcript or hidden
  reasoning is retained. The reviewer and record author are independent for
  the sampled source adjudication; neither claims a complete audit. One scoped
  result cannot establish general performance. Controlled recovery and
  unavailable controls remain outstanding.

## Synthetic sample B: unnamed guidance selection

An independent `gpt-6.1-terra` medium-effort reviewer was given this exact
prompt and instructed not to read the answer key. The shared filesystem did
not enforce that restriction:

> In /home/mcooney/workspace/ai_assisted_research at revision
> 7575a008b027bba0bcb9808e3848bec7c9851722, complete the review task in
> maintenance/tests/fixtures/primer_audit_behaviour/sample-b/PROMPT.md. Work
> read-only, inspect the supplied fixture files and any relevant instructions
> you independently select, and do not read ANSWER-KEY.md or other agents'
> materials. Do not delegate. Report precise findings, scope, any gate
> decisions, paths of guidance and files consulted, and a concise record of
> actual actions. Stop after your report.

The fixture's own tracked prompt asks for a complete review of its supplied
primer, reference extracts and rendered contents. Inputs at the revision above
are under `maintenance/tests/fixtures/primer_audit_behaviour/sample-b/`:
`PROMPT.md` SHA-256 `d20fc1eeaa63d42eaffed9925f554a4f32820f667dc92d1ba106f50f51725620`,
`primer.md` `af31e329b60c447eecd3778dadb94d308abf76d911196514d9a08357afab0f19`,
`reference.md` `11e20005074c73c77ec85f3382f81b40dc5ee6935dcf2f5fb699cd87872d796a`,
and `rendered-contents.txt` `8924802015bf3bf0e430e151171a70eda3828d2b412fd320586af5eca21b6c05`.
The skill hash is as recorded above. The answer key used for later adjudication
is `maintenance/tests/fixtures/primer_audit_behaviour/ANSWER-KEY.md`, SHA-256
`370c87aad257676daed77846188d164959ac43294cf96ba48d6700ca37773ab1`.

The reviewer reported reading all 46 primer lines, the other fixture files,
the project contract and the audit skill. They reported no build, visual
inspection, independent experiment or repository audit recipe. Their findings
included the unsupported handoff claim, missing rendered contents entry,
incorrect citation target, fragmented opening definitions and a need for a
more developed correction and residual example. They retained the short
notation and checklist as legitimate and reported content and structural
failure and release not-ready. They also reported that the example arithmetic
was correct, interpolation and extrapolation limits agreed, and fitted points
did not establish independent validation.

After the response, the record author compared it with the answer key. All
three seeded objective defects were reported and the short checklist was not
misclassified. The answer key also identifies late definition of the equation
parameters as a notation-ordering concern; the supplied result does not
establish that the reviewer noticed it, so it is a possible miss. The reported
residual-example improvement is a judgement, not a seeded objective error.
No other false positive is established from the supplied summary. This supports
task performance on these specific seeded defects only; it is not a complete
false-positive assessment or a real-primer audit.

The reviewer self-reported selecting and reading the skill without being
directed to it. Raw event records and delivered tool payloads were unavailable
to the parent, so the reported actions and complete read cannot be independently
confirmed and native activation is unknown. No truncation event was reported.
The parent supplied the exact prompt and a privacy-reviewed result summary;
the underlying transcript is not retained here. The reviewer did not access the
key according to the task instructions, but no event log is available to verify
that control independently. A controlled recovery trial remains outstanding.

## Synthetic sample B: manually directed application

A second independent `gpt-6.1-terra` medium-effort reviewer received the
same prompt as the preceding trial, with the additional sentence: “Read and
apply .agents/skills/primer-audit/SKILL.md within the fixture scope.” The
inputs, revision and answer key are the same. This direct instruction makes
the trial a manual-application test, not evidence of native selection.

The reviewer reported reading the skill and supplied fixture, including source
lines 1–46, and not reading the answer key. They noted that a source brief,
route IDs, HTML and PDF were absent. They reported content and structural
failure and release not-ready, finding the three seeded objective defects,
fragmented opening definitions, and insufficient worked residual and decision
feedback. They treated the short checklist and notation as not inherently
defective, while raising notation placement and an unspecified audience route
as editorial observations. The central arithmetic and interpolation were
reported sound, with no independent data.

The record author compared the summary with the answer key after the trial:
the three seeded defects match, as does the distinction between a useful short
checklist and fragmented explanatory sections. The notation-placement concern
matches the key's ordering judgement. The audience-route and residual-feedback
observations are unseeded editorial judgements; their status as false positives
or useful improvements is not established by the key. The underlying event
record and delivered outputs were unavailable to the parent; the reported reads,
key exclusion and application are self-reported. The parent supplied a
privacy-reviewed summary and the prompt; no raw transcript is retained.

Both sample reviewers reported the seeded objective defects, but the common
fixture, small sample, absent event records and open-ended editorial outcomes
do not establish that manual direction changes accuracy or that either approach
generalises. No guidance change is justified by these limited observations.

The current collaboration interface available to the record author exposes
agent status and messages, but no independent activation event or exact
tool payload delivered to the reviewer. Codex CLI 0.172.0 documents `--json`
as JSONL event output; its help does not establish that either observation is
available. Do not treat this interface inspection as proof that no other
instrumentation can expose them. Until the delivered payload is observable,
a real tool-layer truncation recovery test is unobservable, not passed.
