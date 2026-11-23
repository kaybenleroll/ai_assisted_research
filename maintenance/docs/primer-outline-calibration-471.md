# Primer outline calibration for #471

This report records behavioural probes of revised structural-audit guidance. It
does not establish a full primer audit, release readiness, or native skill
activation.

## GLM

The first blinded manual trial provisionally passed the structure despite a
truncated read and missed known issues. That result is a calibration failure,
not evidence that the primer met the user's requirements.

After the instructions were revised, a second independent trial identified the
placement of notation, a duplicated lone child heading, and missing subheadings
in the combined case. It initially marked the incomplete review as
`not-checked`; after reading the full source and rendered contents, it judged
the findings editorial improvements. The user has expressly said the primer is
not ready. Unmet user requirements block readiness regardless of that editorial
judgement.

The reviewed source was `primer_glm/primer_glm.md`, at source commit
`8417dba1d9183041213115f6361d84107ae40109`, SHA-256
`27d68fb0fdb9686588bf349404a88764702ae405e1d96cfc99f05d85f19cef07`.
The trials do not prove that every structural issue was found.

### Locator remapping failure

Following the GLM revision at source commit `0245c0356ecd5fb33d94f46ae8eac3ebf133ba58`,
the revision-bound checks for the brief `glm-brief-v6` and audit
`glm-content-audit-v4` passed their schema and locator-existence checks. A
subsequent semantic review found many route and concept cells bound to real but
incorrect passages, including headings, unrelated statements and a reference-only
route presented as a complete teaching transition. Thus the mechanical passes did
not establish that the cited passages supported the claims. Further locator
corrections and independent verification are in progress; this record does not
claim that those corrections have been validated.

Guidance commit `ab7bcd9` strengthens `.agents/skills/primer-audit/SKILL.md`
and `maintenance/docs/primer-production-procedure.md` to require semantic
checking of every retained or moved explanation, action, interpretation and
limitation locator after revision. This addresses the identified guidance gap;
it does not itself validate the GLM evidence or establish a complete technical
audit.

## Knowledge graph

A manual trial inspected the current outline and representative passages of
`primer_knowledge_graph/primer_knowledge_graph.md`, at source commit
`5924434d90d25eba7360d78172d74b21365462c6`, SHA-256
`74e0d4fb5a7add90685da8fc7f94461eeb67ce4c4d976658c0da8383144332f7`.
The brief was revision `kg-398-brief-r13`, SHA-256
`29bc428f153f9e7f4e3b0640b9f1bf76c26d6b85a467a96cd5fd01b43d6f18d5`.
The reviewer had already seen the earlier audit; this trial was not blind.

The short further-reading section was retained as navigation, and the
literature and installed-dependencies cases as distinct applications. The
introduction's repeated graph, storage, and ledger comparisons were a possible
non-blocking editorial improvement. The trial was partial: it did not review
every child relationship or complete the full audit. It cannot support a
structural-gate pass.

## Activation and evidence limits

A fresh Codex 0.171 prompt read the updated skill through a command. No
independent native activation event was established; this is manual application,
not evidence of native activation. The temporary raw log is
`/tmp/outline-skill-activation-471.jsonl`.

For the knowledge-graph trial, the uncommitted audit skill had SHA-256
`ca83cda52fe2af0e69f97af8b708640f944e63bba20ccad07f0541cea8d238e5`
and the uncommitted shared procedure had SHA-256
`de5f5e57d6d4d441b4095528357abe16f56d78649f77197a0fad0eec0955a568`.
The worktree HEAD was `e03baa554ff96cad286efb9caf32c9d82c9d6f4d`.
A later refinement to the wording about user requirements was not separately
behaviour-tested. No synthetic test result is claimed.

## Independent synthetic trial

A separate reviewer manually applied the revised workflow to a synthetic
request-error-rate primer without reading the fixture author's audit. The
reviewer identified a calculation fragmented across headings, a redundant
single-child orientation, and missing landmarks in a long worked case. A short
reference section was retained. The reviewer proposed incorporating a short
transition that the fixture author had retained; this disagreement requires
editorial adjudication and is not automatically a false positive. The fixture
had no rendered output, so the reviewer correctly recorded the structural gate
as not checked and release as not ready. This is a controlled fixture, not
real-primer validation or native skill activation. The temporary inputs and
review are under `/tmp/outline-fixture-471/`; their availability is not assumed
for a future audit.

A fresh, unnamed-task Codex 0.171 session selected `primer-audit`, read its
canonical skill file, and identified the fixture's fragmented calculation and
missing case landmarks while retaining the short reference. It stated that
rendered contents were unchecked but reported release readiness as unchecked,
rather than the required `not-ready`. After the skill was clarified, a second
fresh session selected and read the skill, found those same candidate issues,
and reported release readiness as `not-ready`. It did not explicitly label the
structural-gate decision despite the instruction to state both decisions. These
are partial behaviour observations on one synthetic fixture, not proof of
reliable activation or editorial judgement in other tasks. Raw temporary event
logs are `/tmp/outline-natural-probe-471.jsonl` and
`/tmp/outline-natural-retry-471.jsonl`.

After the instruction was refined to require both labels, a third fresh
unnamed-task session selected and read the audit workflow, identified the
fragmented calculation and missing case landmarks, retained the short
reference, and explicitly reported `Structural gate: not-checked` and
`Release readiness: not-ready` because rendered contents were not inspected.
This is one successful retry on the same fixture, following two partial or
failed trials, not evidence that the workflow will always be selected or
applied correctly. The temporary event log is
`/tmp/outline-natural-final-471.jsonl`.

The readiness checker now validates the shape and consistency of adopted
structural evidence, including the rendered-contents status. Historical audits
without either new marker remain exempt; an evidence row does not prove that
all boundaries were reviewed or that the editorial judgement is sound.

## Notation hierarchy conflict

The GLM structural review found that notation rule N1 required a literal `##`
heading, although the user requested notation within the introduction and
several established primers use a `### Notation` subsection. The rule now
permits either location while retaining the requirement to introduce notation
before mathematical use. This resolves a conflict in guidance; it does not
itself approve any specific primer outline.

## Readiness-decision and independent fixture trials

On 23 November 2026, guidance revision `bb8dd577934fc41cc04c8bb9f52f501355cc99f8` added an integrated reader judgement and a requirement to state each open item's risk, evidence needed, owner and blocking or advisory disposition. The [failure ledger](primer-audit-failure-ledger-471.md) separates instruction conflicts, missing guidance and application failures. Two independent reviewers received only one fixture each and the revised skill; the author-defined answer key was withheld. Inputs and key are preserved under `maintenance/tests/fixtures/primer_audit_behaviour/`. These short controlled fixtures are not full-size primers or proof of general reliability.

- **Sample A:** the reviewer identified the reachable but semantically wrong citation, unsupported ready statement, fragmented definitions and late notation; retained the short reference and correctly found no omitted contents entry. They reported content and structural failure and release not-ready. They noted that a contents extract does not establish complete output or visual QA.
- **Sample B:** the reviewer identified the wrong citation target, omitted rendered heading and contradictory release claim, and differentiated a pending check from a failed measurement. They identified the fragmented definitions and notation order, and retained the short checklist. They reported content and structural failure and release not-ready. They also suggested a numerical residual example or narrower reader promise; that is an editorial judgement beyond the objective answer key.

A fresh `codex exec` session received an unnamed read-only audit request for sample A at the same guidance revision. Its event log shows it announced use of primer-audit and read `.agents/skills/primer-audit/SKILL.md`; it identified the wrong citation, fragmented teaching and unsupported readiness, correctly found the contents extract consistent, and reported content and structural failure and release not-ready. This is observed selection and skill reading for one session, not a separately recorded native activation event or proof of reliable selection. The temporary event log is `/tmp/primer-audit-trials-471/native-probe.jsonl`; the manual independent reviewer and this fresh session both used sample A, so they are not independent fixtures.

Real-primer calibration at `bb8dd57` produced useful findings but both reviewers stopped short of a complete source reading after output truncation. Each correctly reported incomplete scope and did not claim a complete review; neither resumed using smaller batches. The GLM reviewer initially raised a potential multinomial fitted-comparison gap, then retracted it after checking the brief: the requirement that both examples share a fitted dataset had been invented by the reviewer. The deep-learning reviewer identified the malformed rendered CNN parent and proposed several technical checks; these are review findings, not independently adjudicated conclusions. The initial brief did not communicate the user's preference for introductory notation, so its back-matter recommendation cannot test compliance with that preference. Subsequent instructions ask reviewers to continue in bounded batches and include that preference. Guidance was amended to instruct recovery from truncated reads; the amendment requires its own behavioural test. Neither real-primer trial authorises source changes or constitutes a release decision.

### Follow-up on truncated real-primer trials

After explicit follow-up instructions to read contiguous batches, the deep-learning reviewer reported reading source lines 1–1401 and the full HTML contents. With the user's introductory-notation preference supplied, they recommended moving the existing notation table into the introduction. They retained the structural failure for the malformed CNN heading and reported additional potential technical defects, including an asserted derivative claim. These claims require independent technical adjudication; the trial did not run examples, build or source-verification checks.

The GLM reviewer retracted the initially asserted multinomial blocker after comparing it with the brief. On resumption, they reported a structural pass while also admitting that source lines 1307–1308 had not been read. This contradicted the incomplete-reading rule and is a failed verdict-consistency observation. After a further explicit prompt, they read those lines, confirmed the earlier conclusion, and maintained release not-ready because semantic trace-cell and technical checks remained incomplete. Neither recovery demonstrates that the revised skill will autonomously resume after truncation: both reviewers were specifically prompted to do so. The revised skill now calls for bounded recovery and prohibits inventing a shared-dataset requirement; fresh independent tests of those refinements remain outstanding.

A second fresh unnamed-task `codex exec` session on sample B used guidance revision `6901c02`. Its event log shows it announced and read the primer-audit skill. It found the wrong citation target, omitted contents entry and contradictory release statement; it also proposed developing the residual-check example, treated the checklist as an action aid, and reported content and structural failure and release not-ready. This is a second observed skill selection on a different short fixture, not evidence that the truncation or shared-case refinements work on long documents. The temporary event log is `/tmp/primer-audit-trials-471/native-probe-b.jsonl`.

A fresh independent real-primer trial of revision `6901c02` identified the deep-learning contents defect and the user-specified notation placement, but stopped after truncated source/output inspection without attempting recovery. It correctly marked the structural gate not-checked and release not-ready, yet failed the required complete audit. This demonstrates that the earlier recovery instruction was insufficient in this trial. The workflow now calls for planning bounded contiguous reads before reading a long source and verifying range coverage; a further fresh trial is required.
