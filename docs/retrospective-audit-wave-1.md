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
partly sampled and require follow-up before any claim of complete review.

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

### Spectral Graph Theory — prioritised follow-up

The earlier pilot and this wave identified concrete issues requiring a content
follow-up:

- an R example selects the first positive eigenvalue while describing the
  Fiedler mode; R's documented descending eigenvalue order makes that target
  wrong;
- a route snippet uses `read_tsv()` and three column names while the cited CSV
  fixture has nine columns;
- a figure generator distinguishes multiple curves through colour alone,
  creating an accessibility risk;
- earlier audit notes describe an older output and must be reconciled before
  being treated as current evidence.

Disposition: open a focused primer-content PR with before/after coverage and
snippet-to-test maps. Do not fold those repairs into build-infrastructure work.

### Codex for Claude Code Users — editorial follow-up

Earlier editorial review remains relevant: the source repeats its central
bridge, approval/sandbox distinction, and workflow loop; the model chapter
needs one worked routing example; and feature translation would benefit from an
end-to-end hook/skill migration example. These are depth and organisation
improvements, not evidence that the primer lacks its major topics.

Disposition: consider a focused restructuring/content PR after current product
facts are refreshed. Preserve the existing interoperability coverage and use a
coverage map before consolidating repeated passages.

### Fluid Mechanics — no automatic rewrite

The primer is large, maths-heavy, figure-producing, and registered for maths
variants. This wave found no basis for deleting sections or treating its length
as a defect. It needs a dedicated content and render audit if its examples,
figures, and verification claims are to be changed.

Disposition: defer to a separately scoped maths-heavy audit; retain current
outputs until findings are reproduced.

### ML Optimisation — no automatic rewrite

The primer is registered for maths variants and has generated outputs. This
inventory did not establish a content gap or render defect. A future audit
should trace core optimisation concepts through worked calculations, practical
diagnostics, and stated limitations rather than relying on heading counts.

Disposition: defer; no change justified by this wave alone.

### Pi Coding Agent — evidence reconciliation

Earlier build and editorial evidence provides useful sampled PDF and source
checks, but it is historical evidence and must be reconciled against the
current commit before being used as a release claim. No new content defect was
established in this wave.

Disposition: retain as a candidate for a later volatile-product refresh, with
the harness version and source date recorded at that time.

## Incomplete checks and next actions

- No new full container renders were run in this wave.
- No new executable-example run was claimed; inspection and execution remain
  separate evidence states.
- Product-freshness checks were not repeated for the agent primers.
- Visual samples were reconciled from prior evidence where noted, not silently
  presented as new inspection.

Next actions are a focused Spectral Graph Theory content repair, followed by a
Codex primer editorial/product-freshness review. Fluid Mechanics, ML
Optimisation, and Pi remain queued rather than being mass-edited.
