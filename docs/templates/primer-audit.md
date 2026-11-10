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

Use only `verified`, `gap`, `scope-reduced`, or `not-checked`. Record whether
evidence is whole-document or sampled; an inventory or green build is not a
correctness claim. Preserve the brief's stable `route_id` and `concept_id`.

For a process, system, or applied-method primer, complete this additional
trace. A curated fixture, schema validation, or successful smoke test is not
evidence of an end-to-end teaching case.

| Case stage | Source or section | Evidence and result | Status | Gap or limitation |
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
|---|---|---|---|---|
| | | | |

For each core concept, check mechanism or reasoning, significance, conditions or
limits, and the teaching device used. Do not treat word count or subsection
count as evidence of depth.

## Adversarial depth gate

For every route and core-concept row in the brief, record whether a reader can
learn the mechanism, perform or inspect the stated operation, interpret the
result, and recognise a material limit. A row is not verified by a definition,
heading, list, citation, fixture, or passing smoke test. Unresolved substantive
gaps block PR readiness for primary or alternative routes or require an explicit
scope reduction.

| route_id | route tier | concept_id | exact explanation locator | example/action locator | interpretation locator | limitation locator | evidence revision | reviewer | status (`verified`\|`gap`\|`scope-reduced`\|`not-checked`) | finding | scope decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| | | | | | | | | | | | |

A `scope-reduced` status must include the rationale in the scope decision. A
`gap` or `not-checked` row blocks readiness when its route tier is `primary` or
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
|---|---|---|---|
| Opening motivation | | | | |
| Formal or difficult passage | | | | |
| Worked example | | | | |
| Practical or real-world case | | | | |
| Table, code, figure, or equation page | | | | |

Choose samples by risk. Record the page, object, and defect separately for
visual checks; inspect figure meaning and accessibility in addition to file
existence.

## Reconcile earlier evidence

| Earlier finding or audit | Location and revision reported | Current status: confirmed, resolved, stale, or unverified | Evidence |
|---|---|---|---|
| | | | |

## Execution and render evidence

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
