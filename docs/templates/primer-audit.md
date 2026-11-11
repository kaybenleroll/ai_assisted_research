# Primer audit: <title>

- Issue and milestone: <primary issue; related issues>
- Audit revision: <stable revision identifier>
- Source revision: <exact commit or source artefact revision>
- Tracked path: <repository path to this audit>
- Starting branch: <branch>
- Reviewer(s): <names or harnesses>
- Date: <YYYY-MM-DD>
- Reviewed revision: <commit, not only a branch>
- Brief reviewed: <tracked path and brief revision>
- Review boundary: <whole-document, sampled, executed, or not checked for each method>
- Teaching-case contract: <path, or documented reason it is not applicable>
- Core-concept depth matrix: <path and revision reviewed>

## Whole-document review

| Area | Scope and method | Exact evidence or location | Status | Finding or gap | Disposition |
|---|---|---|---|---|---|
| Brief coverage and scope | | | | | |
| Technical claims, derivations, and calculations | | | | | |
| Source quality, attribution, and freshness | | | | | |
| Explanatory depth and prerequisites | | | | | |
| Structure, dependency order, and section fragmentation | | | | | |
| Worked examples and interpretations | | | | | |
| Applications, limitations, and failure modes | | | | | |
| Figures, tables, equations, and accessibility | | | | | |
| HTML, PDF, metadata, and committed outputs | | | | | |
| Residual uncertainty and follow-up questions | | | | | |

For review status, use only `verified`, `gap`, `scope-reduced`, or
`not-checked`. Record whether evidence is whole-document or sampled; an
inventory or green build is not a correctness claim. Preserve the brief's
stable `route_id` and `concept_id`. Transition execution status is a separate
field defined below.

For a process, system, or applied-method primer, complete this additional
trace. A curated fixture, schema validation, or successful smoke test is not
evidence of an end-to-end teaching case.

| Case stage | Source or section | Evidence and result | Execution status | Gap or limitation |
|---|---|---|---|---|
| Input or assumptions | | | | |
| Construction or extraction decision | | | | |
| Intermediate representation | | | | |
| Stored or computed result | | | | |
| Reader-facing query or operation | | | | |
| Interpretation | | | | |
| Failure mode or scope limit | | | | |

## Brief and example traceability

| Brief promise or core concept | Section(s) and explanation | Example, case, or limitation | Evidence status and gap |
|---|---|---|---|
| | | | |

For each core concept, check mechanism or reasoning, significance, conditions or
limits, and the teaching device used. Do not treat word count or subsection
count as evidence of depth.

## Route transition evidence

For each `primary` and `alternative` route, trace at least one complete reader
path from a stated input or assumption through the promised reader operation
to its result, interpretation, and material limit. Use one row per meaningful
transition, in reader order; repeat stable `route_id` and relevant `concept_id`
values from the brief rather than assigning new IDs or using row numbers. Link
each result to the next row's input. Give exact locators at the reviewed source
revision for the input and operation, intermediate reasoning or choice, result,
interpretation, and limitation. Record the actual content of the link, not just
a list of locations. For a conceptual route, the operation may be a derivation,
worked calculation, proof, or explained comparison rather than running code.

| route_id | concept_id(s) | transition (from to) | linked input and reader operation | intermediate reasoning or decision | result | interpretation | material limitation | execution status | gap and reader consequence |
|---|---|---|---|---|---|---|---|---|---|
| | | | | | | | | | |

Use exactly one execution status per transition and case stage:
`executed` means the stated operation was performed on its stated input and
the result checked; `parsed-only` means syntax or static form was checked but
the operation was not run; `illustrative` means the walkthrough was presented
without an independent run; `proposed` means promised but not yet present in
the source; `not-checked` means the reviewer did not assess it. For `executed`
or `parsed-only`, identify the command or method, input, observed result, and
evidence revision under execution evidence below. A passing test of different
code does not make a transition `executed`. Passing code or a populated fixture
does not establish that the reader is taught the reasoning, interpretation, or
limit.

For any missing or weak transition, name what the intended reader cannot infer,
perform, or interpret and which next step depends on it. Carry substantive
gaps into the corresponding depth-gate finding; a `proposed` or `not-checked`
transition cannot support a `verified` depth-gate row. `Reference-only` routes
may receive findings but do not require this full trace and do not block the
teaching gate. Do not use word, heading, or transition counts as quotas.

## Adversarial depth gate

For every route and core-concept row in the brief, record whether a reader can
learn the mechanism, perform or inspect the stated operation, interpret the
result, and recognise a material limit. A row is not verified by a definition,
heading, list, citation, fixture, or passing smoke test. Unresolved substantive
gaps block PR readiness for primary or alternative routes or require an explicit
scope reduction.

| route_id | route tier | concept_id | explanation locator | example/action locator | interpretation locator | limitation locator | evidence revision | reviewer | status | finding | scope decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| | | | | | | | | | | | |

Allowed `status` values: `verified`, `gap`, `scope-reduced`, and
`not-checked`.

A `scope-reduced` status must include the rationale in the scope decision. For
each `gap`, state the concrete consequence for the reader and the dependent
step, not just that more depth is needed. A `gap` or `not-checked` row blocks
readiness when its route tier is `primary` or
`alternative`; a `reference-only` row does not block the teaching gate.
Mechanical checks may validate these columns, IDs, tiers, statuses, and
non-empty required cells. Human review must decide whether the cited prose
genuinely teaches the mechanism, action, interpretation, and limitation. Do not
add quotas.

For calibration, a catalogue entry that names a technique, lists features, and
cites a source remains a `gap` even if the row passes validation. A suitable
worked calculation, explained comparison or counterexample, or traceable case
shows the reasoning and reader action, supports an interpretation, and makes a
material limit clear. Cite the actual passages: for example,
`primer_example/primer_example.md`, section “Choosing a model”, paragraph
beginning “For this sample”, or a source line and named example, at the recorded
revision. Use distinct locators when the evidence is in different places.

The primary route teaches the main path; an alternative route promises another
taught path and must meet the same gate. Reference-only material is for lookup
and its gaps do not block that gate. For `scope-reduced`, identify the removed
or demoted promise, rationale, and corresponding changes to the brief and
reader-facing scope. An unaddressed omission is a `gap`, not a scope decision;
use `not-checked` when the evidence has not been reviewed.

For published code, map the reader-facing snippet to its executable example or
state that it is illustrative only. Check fixture schema, dependencies,
ordering conventions, and expected results; a smoke test that exercises a
different path does not verify the snippet.

| Published snippet or calculation | Test/manifest ID or illustrative status | Fixture and expected result checked | Gap |
|---|---|---|---|
| | | | |

## Representative sampling

Sampling supplements the whole-document pass. Record why each sample was
chosen; do not infer full-document coverage from these rows.

| Sample/page/object | Risk represented | Evidence and result | Status | Follow-up |
|---|---|---|---|---|
| Opening motivation | | | | |
| Formal or difficult passage | | | | |
| Worked example | | | | |
| Practical or real-world case | | | | |
| Table, code, figure, or equation page | | | | |

Choose samples by risk. Record the page, object, and defect separately for
visual checks; inspect figure meaning and accessibility in addition to file
existence.

## Revision-triggered second audit

After any primer, brief, example, or published output changes following an
audit, complete a second audit before readiness carries forward. Compare the
previous and current revisions, identify the changed artefacts and affected
route/concept evidence rows, and re-review changed passages, dependent
transitions, claims, examples, and outputs. Include adjacent material affected
by the changes. A revision metadata update or mechanical check alone does not
establish a fresh judgement.

| Previous and current revisions | Changed artefacts and exact passages | Affected route/concept rows, transitions, claims, examples and outputs | Review scope, reviewer, method and result | Remaining gaps and readiness consequence |
|---|---|---|---|---|
| | | | | |

Record retained evidence separately from newly reviewed or executed evidence;
include the original revision and reason for retaining it, or the new revision,
method and result. Identify checks not repeated and outstanding work. Include
this distinction in any handoff. If no earlier audit exists, state that this is
the initial audit.

| Evidence and affected rows | Retained or newly reviewed/executed | Revision, method, result and reason for retention | Limits or outstanding checks |
|---|---|---|---|
| | | | |

## Reconcile earlier evidence

| Earlier finding or audit | Location and revision reported | Current status: confirmed, resolved, stale, or unverified | Evidence |
|---|---|---|---|
| | | | |

## Release readiness checklist

Record the content gate and release-readiness decision separately. Use
`pass`/`fail` for the content gate and `ready`/`not-ready` for release
readiness. Mechanical checks supply evidence; human review remains responsible
for semantic depth, citation support, accessibility meaning, and visual quality.

| Gate | Decision | Required evidence or limitation |
|---|---|---|
| Brief and audit binding | | Source, brief, audit, and reviewed revisions agree. |
| Route/concept gate | | Stable IDs, exact locators, and no blocking primary/alternative rows. |
| Locator validity | | Git-backed source and line validation result. |
| Examples | | Manifest IDs, runtime, command, result, and execution status. |
| Rendered outputs | | HTML/PDF existence, metadata, freshness, and render-QA result. |
| Accessibility | | Heading order, table/code structure, alt text, and visual inspection status. |
| Sources | | Citation verification and freshness status. |
| Links | | Offline result and any online-check limitation. |
| Revision review | | Changed artefacts and affected evidence rows reviewed. |
| Handoff | | Remaining gaps, reviewer, branch, commands, and release decision. |

- Content gate: <pass or fail>
- Release readiness: <ready or not-ready>

## Execution and render evidence

- Transition checks: <route_id, concept_id, transition, command or method,
  stated input, observed result, evidence revision, and execution status>
- Commands actually run: <commands and results>
- Examples executed: <IDs and runtime, or “none; illustrative only”>
- Examples parsed but not executed: <IDs and reason>
- Visual QA pages: <page/type/pass or fail>
- Offline or unavailable checks: <what could not be verified>
- Reviewer effort: <rough time and friction, without a quality score>
- Stopping rule: <what was deliberately not checked and why>

## Pilot learning

- False positives: <findings that did not represent a real defect>
- Missed issues: <issues found later or by another reviewer>
- Procedure changes proposed: <specific change or “none”>
- Remaining work: <issue-linked next actions>
- Readiness decision: <ready only if all primary and alternative routes pass the
  adversarial depth gate; otherwise name the blocking gaps and scope decision>
