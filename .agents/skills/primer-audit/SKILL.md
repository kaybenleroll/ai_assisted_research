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
establish this trace. Record where the case is executable, illustrative, or
measured; mark an untraceable case as a substantive gap unless the brief
explicitly justifies another teaching device.

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
