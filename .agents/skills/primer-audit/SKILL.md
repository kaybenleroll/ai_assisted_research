---
name: primer-audit
description: Audit a primer after drafting or substantive revision. Use for whole-document coverage, technical claims, explanatory depth, structure, examples, sources, outputs, and residual uncertainty.
---

# Audit a primer

Resolve repository documents and recipes from the owning repository root;
resolve references bundled with this skill from the skill directory.

Use `maintenance/docs/primer-workflow-skills.md` for routing and the shared decision
checklist. Report findings and evidence within scope; a failed check does not
authorise repair.

Read `maintenance/docs/primer-production-procedure.md`,
`maintenance/docs/templates/primer-audit.md`, `maintenance/docs/review-checklist.md`, and
`STYLE_GUIDE.md`. Record the reviewed source revision and brief revision, not
only a branch name; the audit itself is a tracked artefact.

For a forward test of revised guidance, use the current revised primer and its
tracked brief and audit as the calibration baseline, recording their revisions.
Before testing, re-scope historical findings against the current artefacts:
identify what remains a gap, what has been addressed, what was explicitly
scope-reduced, and what has not been checked. Preserve the stable route and
concept IDs and assess findings against the current reader promise; do not
carry a historical gap forward without current evidence.

Report synthetic fixture results separately from realistic current-primer
evidence, with inputs, revisions, observations, and limits. A fixture can test a
known case or failure mode but cannot alone establish behaviour on the current
primer. Neither type of test replaces the human content judgement. Keep the
content gate (`pass` or `fail`) separate from release readiness (`ready` or
`not-ready`); unresolved primary or alternative gaps block the content gate.

Before the final verdict, read the document as one reader journey and state
whether the major sections develop their teaching jobs with enough reasoning,
application and limits for the promised audience. Check the opening and
rendered contents against any explicit user requirements. Explain retained
brief sections by their purpose; do not equate a populated matrix with a sound
whole-document judgement.

For every open item, identify the specific risk or reader consequence, the
evidence needed to decide it, who is responsible and whether it blocks content,
structure or release, or is an advisory limitation. Reconcile that item with
existing evidence before asking for more checks. Use risk-selected technical
verification: do not demand exhaustive independent reproduction merely
because a calculation or fit has not been independently rerun. An incomplete
required review blocks readiness; an unperformed optional check is not
automatically a defect. Give a reasoned decision, the remaining blockers and
the stopping boundary; do not leave an unexplained `pending` verdict.

After the human review, run `just primer-audit <primer-directory>` for a
tracked primer. This performs the structural evidence check, Git-backed
locator and revision check, opted-in examples, build, render QA, freshness,
and scoped link checks. Record its result in the audit. It does not replace
human judgement of depth, citations, accessibility meaning, or visual quality.

Before reading a long source, determine its line count and divide it into
contiguous, non-overlapping batches small enough for complete tool output.
Read every batch, tracking first and last line; if any output is truncated,
split and reread it before advancing. Verify there are no gaps between ranges.
Request and inspect one batch per tool call; do not combine multiple batch
outputs into a single response that can itself be truncated. Check the tool's
truncation indication and the returned line sequence, not just the first and
last lines. After any interrupted or truncated recovery, retry each missing
interval in smaller batches until it is received or a retry actually fails.
If tool output cannot be recovered, stop the whole-document verdict and record
the missing ranges and reason. For a new or migrated audit use `- Audit schema: 2` and record the
successfully received source lines in the audit outline section as `- Source read coverage: 1-120, 121-240`
using inclusive ranges (or `none` if no lines were read). Bind the record to
the reviewed source revision. It records coverage, not proof of comprehension;
never claim a range whose output was truncated or not inspected.

Read the complete source and perform a whole-document inventory against the
tracked, revision-bound brief. Check coverage, technical claims and
calculations, sources and freshness, prerequisites and explanatory depth,
dependency order and section fragmentation, examples and limitations,
figures/tables/equations/accessibility, and committed outputs. Record the
audited source revision and reviewer.

Inspect the actual source outline in sequence, using the shared outline review
in `maintenance/docs/primer-production-procedure.md` and recording evidence in
`maintenance/docs/templates/primer-audit.md`. Review every top-level boundary,
the purpose of parent and child sections, and whether siblings serve distinct
reader needs or develop one continuous task or argument. Record an explicit,
evidence-based decision for each boundary, including why it should be retained
or changed and the reader consequence. Cite passages on both sides and explain
the reader task each serves and how those tasks connect or differ. Where a
plausible alternative grouping or placement matters, describe it and compare its
effect on navigation and reasoning with the existing structure. Labels such as
“bounded” or “distinct purpose” alone do not justify retention. Distinguish an unresolved substantive
structural finding that blocks content readiness from an editorial improvement
that does not; an unmet user-specified structural requirement blocks readiness.
Do not infer either decision from heading counts alone.
For repository Pandoc HTML, run the advisory candidate comparison
`python3 -I maintenance/scripts/check/primer_outline_compare.py SOURCE.md OUTPUT.html`
and inspect each difference or ambiguity against the source and rendered
contents. It can expose missing headings, but heuristics, unmatched HTML
layouts and numbering can yield false positives or misses; it does not replace
the outline or contents review. Record the actual command, output and scope.

Inspect the rendered contents as well as the source outline, including the
opening orientation and placement of notation. Consider an isolated brief
chapter, a chapter with a single child heading, and a long undivided case as
candidates for review, not automatic defects. Compare plausible alternative
groupings and their effects on the reader before deciding whether to retain or
change the existing structure; do not merely justify the status quo.

If any required part of this review is incomplete, record its scope and reason
as `not-checked` and report release readiness as `not-ready`; do not use
`not-checked` as the release decision. State both decisions even for a scoped
review, using separate `Structural gate: not-checked` and `Release readiness:
not-ready` statements. Do not report a pass based on a truncated source read
or incomplete outline inspection. If a read is truncated, resume in bounded,
contiguous batches and record the inspected ranges; do not stop at the
truncation when further reading is available. If coverage still cannot be
completed, report the unreviewed ranges and their readiness consequence.

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
promised operation end to end. Distinguish genuinely separate examples from a
continuous case, but do not require every concept or different response type
to share one dataset unless the brief promises that connection. Judge whether
the reader can transfer between the examples, and record any material gap.

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
why it matters, and a material condition, consequence, or limitation. This
local check is necessary but not sufficient: a document can populate every
concept row while still reading as a compressed catalogue. Use the outline and
continuous reading to find catalogue-like clusters, abrupt section endings,
repeated heading-definition-list patterns, and reasoning that is asserted
rather than worked through.

Add a reader-scale depth pass for every major section and every section that
hosts a primary or alternative route. Record the section's teaching job, the
main reasoning spine or worked thread, the exact passage where the reader can
apply or interpret it, and the material limit or failure case. Then make an
explicit disposition: `expand`, `consolidate`, or `retain`. `retain` requires
an editorial reason when the section is intentionally brief (for example,
orientation, a transition, or a deliberately bounded reference branch). Explain
what the cited development enables the intended reader to do; where it is
insufficient, identify the missing reasoning and resulting reader consequence.
A brief or reference label alone does not establish that the section fulfils its
promised job.
For a major synthesis, practice, or reference section, identify the distinct
material reader outcomes promised by the brief and pose the decisions or
actions needed after the preceding route. Locate opportunities to carry them
out with the necessary information and feedback, or explain why those
opportunities or feedback are not promised. A single easy task does not
establish a different promised outcome. Where transfer to unfamiliar inputs is
promised, check whether practice supplies new inputs rather than only repeating
worked values, and whether the reader has enough evidence to make and justify
the requested decision. For representative multi-step exercises, trace the
answer's intermediate reasoning and check whether feedback helps a reader find
and correct a consequential mistake. Identify unsupported transfer and its
reader consequence. Judge the actual development independently of the title,
section label, or existence of earlier examples. This does not require an
exercise in every section, a fixed number of tasks, or a structural outcome.

Distinguish a promised reader action to recognise a boundary and decide what
information or approach is needed next from a specialist fitting route offered
only for reference. Assess the former against the tier and scope of the route
that promises it; the latter does not require a full teaching spine or become
blocking solely because it is reference-only.
For a promised recognition action, try a concrete unfamiliar observation or
design: can the reader distinguish a relevant boundary from a plausible
neighbour and identify the information needed next? Cite where the document
enables that decision, or record the missing link and its consequence. A
referral naming a method alone is not evidence of this action.
Expand a section when the reader cannot explain the mechanism, reproduce the
promised operation, interpret its result, or recognise its failure without
silently importing missing reasoning from another section. Consolidate
adjacent sections when their reasoning is continuous and separate headings
make the route feel fragmented. Do not use a fixed word, paragraph, heading,
or subsection count as a pass/fail rule; use length and density only as
signals that trigger this judgement. A section-level depth failure affecting a
primary or alternative route is blocking even when every individual concept
row is locally complete.

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

After an audit, any change to the primer, tracked brief, examples, or published
outputs triggers a second audit before readiness carries forward. Compare the
previously audited revisions with the current artefacts; identify every
changed artefact and the affected route/concept evidence rows. Re-review the
changed passages, dependent reader-path transitions, claims, examples, and
outputs within the affected scope, including any consequences for adjacent
material. Record the revisions compared, exact locations, scope, reviewer,
judgement and result in the tracked audit. Mark unresolved review or gaps as
blocking where the route requires it. Rebinding revision metadata or rerunning
a structural check alone is insufficient evidence of a fresh judgement.

After a revision, inspect each retained or moved explanation, example/action,
interpretation, and limitation locator against the passage it describes in the
current source. Correct wrong mappings; mark unverified evidence `not-checked`
and apply the route gate. A reachable line or anchor does not establish that it
contains the described evidence. Record this semantic locator check separately
from mechanical reachability and from the earlier content review; checking a
mapping does not itself repeat or renew that review.

Distinguish evidence retained from the earlier audit, with its original revision
and reason it remains applicable, from evidence newly reviewed or executed,
with its current revision, method and result. Carry that distinction into any
handoff and identify checks not repeated or still outstanding.

After the row-by-row pass, review the document as a reader: could the intended
reader explain the organising model, reproduce the central operation, interpret
its result, and recognise when it fails? A negative answer is a readiness
finding even when all mechanical and executable checks pass. Do not declare a
primer ready while an unresolved substantive depth gap remains in a primary or
alternative route.

Repeat that reader review at section boundaries. Ask whether each major
section advances the route or merely names adjacent topics, and whether its
opening, development, example or decision, interpretation, and limitation form
a coherent teaching unit. Record section-level findings separately from the
concept depth matrix so that a locally `verified` concept cannot hide a thin
or fragmented surrounding treatment. Re-check affected section dispositions
after any substantive revision, including a consolidation that changes
locators or route transitions.

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
