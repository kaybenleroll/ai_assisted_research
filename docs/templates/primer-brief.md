# Primer brief: <title>

- Issue and milestone: <primary issue; related issues>
- Brief revision: <stable revision identifier>
- Source revision: <exact commit or source artefact revision>
- Tracked path: <repository path to this brief>
- Reader: <who this is for>
- Prerequisites: <knowledge, tools, or data>
- Problem and motivation: <what problem the subject solves and why it exists>
- Intended outcome: <what the reader can explain or do afterwards>
- Scope: <included topics>
- Exclusions: <explicitly out of scope>
- Proposed dependency-led route: <ordered concepts and rationale>
- Approximate depth: <qualitative target; do not turn this into a quota>
- Worked examples: <small examples and what each demonstrates>
- Real-world cases: <applications and selection rationale>
- Teaching-case contract: <path to the completed case contract, or the reason
  an alternative teaching device is appropriate>
- Worked-case trace: <route-keyed trace below, or why no continuous case applies>
- Core-concept depth matrix: <path to the matrix; preserve stable concept_id values>
- Route classification and teaching spines: <stable route_id and exactly one
  tier — primary, alternative, or reference-only — for each route; motivating
  problem, organising model, worked application, interpretation, and limit for
  each primary or alternative route>
- Figures, tables, and equations: <planned items and purpose>
- Languages and executable examples: <language/runtime and test intention>
- Evidence plan: <claims, primary sources, calculations, and freshness checks>
- Open decisions: <question, options, and evidence needed>

## Review plan

- Whole-document checks: <coverage, claims, structure, examples, sources, outputs>
- Representative samples: <passages/pages and why they represent risk>
- Planned independent reviewers: <bounded questions, not generic approval>
- Content gate: <how the central case and concept-depth matrix will be checked>
- Depth gate: <how each route and core-concept row can be rejected for labels,
  catalogues, or unsupported jumps before drafting or publication>
- Case acceptance: <check each applicable primary or alternative route's input
  through interpretation and failure/boundary; check stage handoffs, modes,
  evidence, and correction/re-evaluation where relevant>
- Scope acceptance: <check the displacement and reader benefit of each optional
  branch, and a recorded expand, narrow/demote, or remove decision for every
  unresolved concept; block drafting while an outcome-critical gap remains>

## Worked-Case Trace

For each primary or alternative route that teaches a process, system, or
applied method, use its stable `route_id` from the matrix and follow one case
through the stages below. Show the artefact or result passed from each stage to
the next; alternative routes may share an input but must identify where they
branch and how their results are compared. Mark each stage `executable`,
`illustrative`, or `reference-only`. Record commands or test IDs for executable
stages, a concrete example for illustrative stages, and the cited material for
reference-only stages. Record measurements separately with their provenance.
If a required stage remains reference-only, expand it or narrow or demote the
route before drafting. If no continuous case applies, explain which teaching
device carries the route instead.

| route_id | stage | case input or prior result | decision, operation, or observed result | output handed onwards | stage mode | planned evidence or check |
|---|---|---|---|---|---|---|
| | Input or assumptions | | | | | |
| | Transformation | | | | | |
| | Intermediate representation | | | | | |
| | Reader-facing operation | | | | | |
| | Interpretation | | | | | |
| | Failure or boundary | | | | | |
| | Correction and re-evaluation, if relevant | | | | | |

## Optional Branches and Unresolved Concepts

For every optional branch, state the reader need, the worked evidence it adds,
and which other optional material it displaces or shortens. Keep the primary
route's teaching spine intact; narrow, demote, or remove a branch whose cost
cannot be justified.

| route_id | optional branch | reader need | worked evidence added | material displaced or shortened | scope decision and reason |
|---|---|---|---|---|---|
| | | | | | |

For every unresolved concept, decide to `expand`, `narrow/demote`, or `remove`
it before drafting. Record the reason and effect on the reader outcome. Keep
retired IDs in this record and do not reuse them.

| route_id | concept_id | unresolved gap | decision and reason | effect on reader outcome |
|---|---|---|---|---|
| | | | | |

## Core-concept depth matrix

Use stable IDs. Every row must be complete; these are required planning fields,
not quotas. A teaching device may be a worked example, proof, comparison,
counterexample, failure case, figure, or another justified device.

| route_id | route tier | concept_id | concept | reader action | mechanism or reasoning | significance | teaching device | worked evidence | interpretation | limitations | downstream use | Evidence/source plan |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| | | | | | | | | | | | | |

Keep `route_id` and `concept_id` stable when this brief is revised. Use only
the route tiers `primary`, `alternative`, and `reference-only`; do not use row
position as an identifier. Do not impose word or heading quotas; the rows and
trace describe required understanding, not target counts.

Before handoff, follow each route's case from input to interpreted result and
boundary; verify stage hand-offs, classifications, planned evidence, and any
correction and re-evaluation. Confirm every optional branch has a scope balance
and every unresolved concept has a decision reflected in the reader promise.
Once the audit exists, run `just check-primer-evidence <brief> <audit>` to check
the matrix shape and matching IDs. Review the explanations and case manually;
the structural check cannot establish their teaching value.
