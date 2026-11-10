# Primer process audit for #399

- Issue: [#399](https://github.com/kaybenleroll/ai_assisted_research/issues/399)
- Reviewed revision: `d66653c26b94e70189670b7a0a542276d10769d4`
- Review date: 2026-11-10
- Reviewers: three independent read-only subagent reviews, integrated by the main session
- Boundary: repository contract, production procedure, skills, templates, validators, CI, render QA, and the release evidence for the knowledge-graph primer

## Conclusion

The repository has a strong documented route for planning and reviewing primers,
but only a partial release gate. It can establish that a primer is broad,
buildable, rendered, and partly executable. It does not yet establish that the
reader can learn and apply every promised primary or alternative route.

The central failure is not that a malformed document passed a syntax check. The
failure is that breadth and implementation evidence were durable enough to be
reported, while the required mechanism, reader action, interpretation, and
limitation evidence was left to reviewer assertion and was not retained as a
release artefact.

Confidence is high that the evidence gap exists. Confidence is medium that the
knowledge-graph primer is shallow in every section; that claim requires the
separate whole-document revision audit in #398.

## Current route and evidence inspected

The audit traced the route through:

- `docs/project-contract.md` and `docs/agent-collaboration.md`;
- `CONTRIBUTING.md`, `STYLE_GUIDE.md`, and `docs/primer-production-procedure.md`;
- `.agents/skills/primer-plan/SKILL.md`, `primer-audit/SKILL.md`,
  `primer-render-qa/SKILL.md`, and `primer-handoff/SKILL.md`;
- `docs/templates/primer-brief.md`, `docs/templates/primer-audit.md`, and
  `docs/review-checklist.md`;
- `scripts/check_agent_contract.py`, `tests/test_agent_contract.py`,
  `scripts/render_qa.py`, `scripts/check.py`, and the relevant CI recipes;
- the knowledge-graph primer release evidence and revision history through
  PR #396.

The knowledge-graph release contained substantial breadth: 13 H2 headings, 33
H3 headings, 13 code blocks, 8 tables, and a 47-page PDF. That is inventory
evidence, not evidence that each route teaches a mechanism, an operation, an
interpretation, and a failure mode.

## Failure-mode findings

| ID | Severity | Failure mode and evidence | Required control |
|---|---|---|---|
| F1 | High | The brief may exist only in an issue or ignored `.scratch` file. Nothing requires a non-placeholder brief, validates its depth matrix, or compares the PR with its acceptance criteria. See `docs/primer-production-procedure.md:38-67` and `docs/templates/primer-brief.md`. | Require a linked brief with stable route and concept identifiers before drafting and release; validate that the audit covers every identifier. |
| F2 | High | The depth gate is described as blocking, but no automation or required artefact enforces it. `check-structure` checks prose before child headings, not whether prose teaches a mechanism. See `docs/primer-production-procedure.md:124-155`, `docs/templates/primer-audit.md:56-72`, and `scripts/check.py`. | Require a completed, independently reviewed route/concept matrix with exact evidence for mechanism, reader action, interpretation, and limits. |
| F3 | High | “Core concept”, “primary route”, and “alternative route” have no formal inclusion rule. A plan can under-scope the matrix and omit difficult concepts from the gate. See `.agents/skills/primer-plan/SKILL.md` and `docs/templates/primer-brief.md`. | Require an inventory of all routes and concepts implied by scope, outcomes, prerequisites, headings, and examples, with explicit omission rationales. |
| F4 | High | Audit evidence is not defined tightly enough. Exact locations, reader tasks, observed results, interpretation, and limitations are requested but not schema-checked; status values are effectively self-certified. See `docs/templates/primer-audit.md:56-67`. | Define an evidence schema and constrained statuses such as `verified`, `gap`, `scope-reduced`, and `not-checked`; block readiness on unresolved primary or alternative gaps. |
| F5 | High | Release and handoff evidence is optional prose. The PR check validates the first issue-reference line, not the audit, depth decision, visual evidence, remaining work, or blockers. See `scripts/check_pr_body.py`, `CONTRIBUTING.md:147-176`, and `.agents/skills/primer-handoff/SKILL.md`. | Require a revision-bound audit and handoff artefact with an explicit readiness decision and no unresolved blocking findings. |
| F6 | High | Render QA produces `pending` visual results for human completion, but neither the command nor CI requires those results to be replaced. See `scripts/render_qa.py:347-365` and `docs/review-checklist.md:63-81`. | Require four inspected page types, recorded pass/fail results, and no pending visual status before release. |
| F7 | High | PR CI does not necessarily render the changed primer. Freshness and consistency checks do not prove that committed outputs were regenerated or visually inspected. See `.github/workflows/checks.yml`, `Justfile`, and `CONTRIBUTING.md:85-91`. | Add a changed-primer render route that validates source/output consistency and produces release-bound render evidence. |
| F8 | Medium | Executable examples are opt-in. A primer can promise that readers can perform a task while leaving the code illustrative, or a bounded fixture can be mistaken for source-to-release evidence. See `CONTRIBUTING.md:29-33`, `docs/executable-examples.md`, and the knowledge-graph source. | Map each actionable outcome and published snippet to an example ID and status: executed, parsed-only, illustrative, or proposed. Cross-check the map against manifests and audit claims. |
| F9 | Medium | Source maps, freshness checks, independent claim verification, and volatile-claim notes are workflow instructions rather than release evidence. See `docs/primer-production-procedure.md:69-83`, `STYLE_GUIDE.md:122-134`, and `CONTRIBUTING.md:115`. | Require a claim/source/freshness register with named checks and unresolved items when claims or software facts change. |
| F10 | Medium | Lint and structure findings can remain advisory outside enforcement manifests. A changed primer can therefore retain findings that are reported but do not fail the route. See `CONTRIBUTING.md:115-123` and `scripts/lint.sh`. | Enrol new or substantially revised primers in the applicable enforcement manifests, or fail findings for changed paths. |

## Concrete knowledge-graph failure path

The release evidence shows how the current process can over-credit a document:

1. The primer presents a broad route covering DuckDB, RDF, SPARQL, SHACL,
   PROV-O, Cypher, R, evaluation, privacy, and governance.
2. The Python example constructs bounded claims and merges them with curated
   rows. It is a useful teaching fixture, but it is not a general extractor or
   proof of source extraction, identity resolution, or evidence verification.
3. The R example uses hard-coded fixture data and a lossy projection that drops
   temporal, polarity, provenance, and claim identity. It is explicitly useful
   as a structural projection, but it does not demonstrate evidence-preserving
   analysis of the DuckDB graph.
4. RDF, property-graph, and storage examples are explicitly illustrative and
   unexecuted; the release sequence and Neo4j smoke test are also illustrative
   or prospective.
5. Builds, freshness, code execution, and output checks can all pass while no
   durable artefact demonstrates that a reader can perform, interpret, and
   critique each promised route.

This is not an argument that the examples are invalid. It is an argument that
their instructional boundaries and execution status need to be represented in
the release gate, rather than inferred from the document or a green build.

## Missing durable evidence

The reviewed release does not retain a primer-specific record of:

- primary, alternative, and reference-only routes;
- a complete core-concept depth matrix;
- a teaching-case trace from source input through construction, representation,
  operation, interpretation, and limitation;
- independent whole-document depth findings;
- exact sample pages and human visual-QA results;
- example execution logs or output artefacts;
- a handoff separating verified, reported, unresolved, and not-checked evidence.

The absence of these artefacts does not prove that no review occurred. It means
the release cannot now distinguish performed review from retrospective assertion.

## Prioritised controls

1. Add stable route and concept identifiers to the brief and audit, with a
   validator for completeness, duplicates, revision matching, and allowed
   statuses.
2. Define the depth-evidence schema: exact location, reader task, mechanism,
   interpretation, limitation, reviewer, and unresolved disagreement.
3. Make the semantic depth gate explicitly human and adversarial. Automation
   can validate completeness and form; it cannot decide whether prose genuinely
   explains a mechanism.
4. Require explicit route inventories and omission rationales.
5. Make release handoff consume the validated audit and block unresolved
   primary or alternative gaps.
6. Cross-check example IDs, execution status, fixtures, manifests, and audit
   claims.
7. Require changed-primer render and visual evidence rather than treating
   freshness or file existence as QA.
8. Require a claim/source/freshness register for substantive or volatile claims.

## False-positive controls

The new process must not introduce quotas or punish valid concise writing. It
must not reject reference-only RDF, Cypher, or Neo4j material merely because it
is unexecuted when the scope is honest. Synthetic data is acceptable when its
instructional boundary is explicit, but it must not be credited as evidence of
real-world extraction or coverage. A lossy R projection is acceptable when the
lost semantics and intended use are explained. Absence of figures is not itself
evidence of shallow pedagogy; the text, tables, and diagrams must be judged for
the job they are intended to do.

## Disposition

This audit finds a process and evidence gap, not a sufficient basis for making
specific content claims about every section of the knowledge-graph primer. The
contract and skills should be strengthened first under #400 and #401. The
primer should then be re-audited and revised under #398.
