---
name: primer-audit
description: Audit a primer after drafting or substantive revision. Use for whole-document coverage, technical claims, explanatory depth, structure, examples, sources, outputs, and residual uncertainty.
---

# Audit a primer

Resolve repository documents and recipes from the owning repository root;
resolve references bundled with this skill from the skill directory.

Use `docs/primer-workflow-skills.md` for routing and the shared decision
checklist. Report findings and evidence within scope; a failed check does not
authorise repair.

Read `docs/primer-production-procedure.md`,
`docs/templates/primer-audit.md`, `docs/review-checklist.md`, and
`STYLE_GUIDE.md`. Record the reviewed source revision and brief revision, not
only a branch name; the audit itself is a tracked artefact.

Read the complete source and perform a whole-document inventory against the
tracked, revision-bound brief. Check coverage, technical claims and
calculations, sources and freshness, prerequisites and explanatory depth,
dependency order and section fragmentation, examples and limitations,
figures/tables/equations/accessibility, and committed outputs. Record the
audited source revision and reviewer.

For a process, system, or applied-method primer, read the teaching-case
contract and trace at least one case end to end: source input or declared
assumption, construction or extraction decision, intermediate representation,
stored or computed result, reader-facing query or operation, interpretation, and
failure or scope limit. A curated fixture or passing runtime check does not
establish this trace. Record the execution status of each stage; mark an
untraceable case as a substantive gap unless the brief
explicitly justifies another teaching device.

For every `primary` and `alternative` route, follow at least one complete
reader path from its stated input or assumption through the promised operation
to an interpreted result and material limit. Record each meaningful transition
in the template's transition evidence table, reusing the brief's `route_id` and
relevant `concept_id` values. Link the result of one step to the input of the
next with exact source locators. For each transition locate the input and reader
operation, intermediate reasoning or decision, result, interpretation, and
material limitation; inspect the actual passages rather than inferring a link
from headings or adjacent examples. State precisely what a missing or shallow
link prevents the reader from doing or understanding, including the dependent
step affected. A conceptual route can use a proof, worked calculation, or
explained comparison instead of code, provided the reader can follow the
promised operation end to end.

Give each transition one execution status: `executed` (the stated operation was
run on the stated input and its result checked), `parsed-only` (syntax or static
form checked without running the operation), `illustrative` (presented as a
walkthrough without an independent run), `proposed` (promised but not yet in
the source), or `not-checked` (the reviewer did not assess it). Record commands,
inputs, outputs, and revisions for executed or parsed-only claims. These are
evidence-provenance statuses, separate from the depth-gate statuses. Even
correctly executed code does not show that the prose teaches its decisions,
result, interpretation, or limits. Keep `reference-only` handling non-blocking;
record useful findings without requiring its full transition trace.

For each core concept, check that the prose explains its mechanism or reasoning,
why it matters, and a material condition, consequence, or limitation. Use the
outline to find catalogue-like clusters and compressed transitions, but do not
turn subsection count, paragraph count, or word count into acceptance criteria.

Run an adversarial depth gate against every `route_id` and `concept_id` in the
brief. Preserve each route tier as exactly `primary`, `alternative`, or
`reference-only`. The tracked audit must retain those identifiers and bind
each row to the evidence revision and reviewer. For each row record exact locators for the
explanation, example/action, interpretation, and limitation, plus `status`
(`verified`, `gap`, `scope-reduced`, or `not-checked`), finding, and scope
decision. A `scope-reduced` row requires a rationale. A primary or alternative
route with `gap` or `not-checked` is blocking; reference-only material may be
reported without the teaching spine. Mark a row as a gap when a locator is
absent or the passage merely defines, names, enumerates, or links to the
concept. Passing code, a populated fixture, a heading, or a short summary is
not teaching evidence. Mechanical checks may validate shape, completeness,
identifiers, revisions, and allowed values only; the human reviewer must judge
whether the prose genuinely teaches. If a promised route cannot meet the gate,
recommend narrowing or demoting it rather than adding a token paragraph.

For each missing or unsupported transition, name the exact reader consequence:
which operation cannot be reproduced, decision cannot be justified, result
cannot be interpreted, or condition under which the result fails cannot be
recognised. Link the finding to the affected depth-gate row and mark that row
`gap` or `not-checked` as appropriate; do not infer teaching from executable
success. A primary or alternative route with such an unresolved finding is
not ready until its teaching is developed or its scope is explicitly reduced.

After the row-by-row pass, review the document as a reader: could the intended
reader explain the organising model, reproduce the central operation, interpret
its result, and recognise when it fails? A negative answer is a readiness
finding even when all mechanical and executable checks pass. Do not declare a
primer ready while an unresolved substantive depth gap remains in a primary or
alternative route.

Then perform risk-selected technical verification and sampling: opening
orientation, difficult formal passage, worked example, practical case, and
representative rendered pages.
Record what was inventoried, independently verified or sampled, with exact
locations and limits; an inventory is not verification of every claim.
For code, map published snippets to tests or state that they are illustrative;
check fixtures, dependencies, ordering conventions, and expected results.
Reconcile earlier audits against the reviewed commit. Record verified,
unresolved, stale, and not-checked evidence separately.

Do not turn the audit into a score, word quota, or heading quota. Record false
positives, missed issues, reviewer effort, stopping boundaries, and issue-linked
follow-up work. A clean build or fresh output is not evidence that the content
is correct. Render QA, executable checks, and mechanical schema checks cannot
approve a content-depth row or replace the human depth review.
