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
