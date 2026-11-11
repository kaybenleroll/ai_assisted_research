# Retrospective audit: wave 1

Audit issue: [#337](https://github.com/kaybenleroll/ai_assisted_research/issues/337)

Reviewed revision: `8d96946` on 6 November 2026. This wave covers the five
most recently reviewed primary documents in the catalogue. It is an audit and
prioritisation record, not a quality score and not an authorisation for a mass
rewrite.

## Scope and method

The wave used the post-draft audit procedure in
[`docs/primer-production-procedure.md`](primer-production-procedure.md) and
the evidence fields in [`docs/templates/primer-audit.md`](templates/primer-audit.md).
The source and committed outputs were inventoried for all five primers. The
Codex, Spectral Graph Theory, and Pi primers also had earlier editorial or QA
evidence that was reconciled against the current revision. Spectral Graph
Theory received the deepest technical pilot review; the other documents remain
partly sampled in this wave. Later follow-ups are recorded below separately;
they do not turn the original inventory or samples into a complete review.

| Primer | Whole-document inventory | Representative samples | Execution/render boundary |
|---|---|---|---|
| Codex for Claude Code Users | Structure and existing editorial review reconciled | Earlier editorial findings reviewed | No new full render or product-freshness review in this wave |
| Spectral Graph Theory | Structure, examples, figures, tables, and outputs inventoried | Technical snippets and PDF pages sampled | Examples inspected, not executed; earlier pilot found concrete defects |
| Fluid Mechanics | Structure, outputs, figures, and maths-variant registration inventoried | No new content sample | No new execution or visual review |
| ML Optimisation | Structure, outputs, and maths-variant registration inventoried | No new content sample | No new execution or visual review |
| Pi Coding Agent | Structure and earlier build/QA evidence reconciled | Earlier PDF pages and editorial evidence reviewed | No new product-freshness review in this wave |

The wave does not claim that clean CI, fresh outputs, or a previous review prove
that current content is correct. It also does not claim that absent figures or
short operational sections are defects.

## Findings and disposition

### Spectral Graph Theory — focused follow-up completed

The earlier pilot and this wave recorded the following historical findings for
a content follow-up:

- an R example selects the first positive eigenvalue while describing the
  Fiedler mode; R's documented descending eigenvalue order makes that target
  wrong;
- a route snippet uses `read_tsv()` and three column names while the cited CSV
  fixture has nine columns;
- a figure generator distinguishes multiple curves through colour alone,
  creating an accessibility risk;
- earlier audit notes describe an older output and must be reconciled before
  being treated as current evidence.

Disposition: the focused repairs in closed issue
[#356](https://github.com/kaybenleroll/ai_assisted_research/issues/356) were
delivered in merged PR [#358](https://github.com/kaybenleroll/ai_assisted_research/pull/358).
The PR reports six executed examples, including the published R route companion,
and inspection of selected PDF pages. This later execution and sampled visual
evidence do not change the original wave's inspection-only boundary or establish
that every part of the primer was reviewed.

### Codex for Claude Code Users — refresh completed

Earlier editorial review reported that the source repeated its central
bridge, approval/sandbox distinction, and workflow loop; the model chapter
needed one worked routing example; and feature translation would benefit from an
end-to-end hook/skill migration example. These are depth and organisation
improvements, not evidence that the primer lacks its major topics.

Disposition: the interoperability and product-claim refresh in closed issue
[#362](https://github.com/kaybenleroll/ai_assisted_research/issues/362) was
delivered in merged PR [#364](https://github.com/kaybenleroll/ai_assisted_research/pull/364),
preserving practical interoperability coverage. Its examples remain illustrative;
visual inspection sampled selected pages. Account- and runtime-specific
behaviour, exhaustive accessibility, historical claims left unchanged, and
full cross-browser behaviour remained unverified in that PR. Product facts
may change after its review.

### Fluid Mechanics — no automatic rewrite

The primer is large, maths-heavy, figure-producing, and registered for maths
variants. This wave found no basis for deleting sections or treating its length
as a defect. It called for a dedicated content and render audit if its examples,
figures, and verification claims were to be changed.

Disposition: subsequent, separately scoped follow-ups completed the renderer
repair ([issue #359](https://github.com/kaybenleroll/ai_assisted_research/issues/359),
[PR #363](https://github.com/kaybenleroll/ai_assisted_research/pull/363)),
workflow pilot and evidence-backed repairs
([issue #376](https://github.com/kaybenleroll/ai_assisted_research/issues/376),
[PR #377](https://github.com/kaybenleroll/ai_assisted_research/pull/377)),
and style fixes ([issue #378](https://github.com/kaybenleroll/ai_assisted_research/issues/378),
[PR #379](https://github.com/kaybenleroll/ai_assisted_research/pull/379)).
All three issues are closed and the PRs merged. The renderer follow-up reports
five executed manifest examples and browser toggle checks; the pilot reports
representative visual inspection, not a page-by-page review, and did not execute
every illustrative snippet. The renderer PR records an untagged PDF and does not
claim full accessibility or cross-browser coverage. These later checks do not
retroactively add content sampling or execution to this wave.

### ML Optimisation — no automatic rewrite

The primer is registered for maths variants and has generated outputs. This
inventory did not establish a content gap or render defect. A future audit
should trace core optimisation concepts through worked calculations, practical
diagnostics, and stated limitations rather than relying on heading counts.

Disposition: further audit or revision is deferred; no change was justified by
this wave alone. Deferred does not mean complete or rejected.

### Pi Coding Agent — evidence reconciliation

Earlier build and editorial evidence provides useful sampled PDF and source
checks, but it is historical evidence and must be reconciled against the
current commit before being used as a release claim. No new content defect was
established in this wave.

Disposition: the volatile-product refresh is deferred pending a deliberate
later task, with the harness version and source date recorded at that time.
Deferred does not mean complete or rejected.

## Incomplete checks and next actions

- No new full container renders were run in this wave.
- No new executable-example run was claimed; inspection and execution remain
  separate evidence states.
- Product-freshness checks were not repeated for the agent primers.
- Visual samples were reconciled from prior evidence where noted, not silently
  presented as new inspection.

The completed follow-ups and their later evidence are identified above. ML
Optimisation and Pi remain deferred. The original wave's incomplete checks and
historical samples remain bounded as stated; no further audit is implied here.
