---
name: primer-plan
description: Plan a new or substantially revised technical primer. Use when defining its audience, scope, dependency-led outline, examples, evidence plan, or unresolved decisions before drafting.
---

# Plan a primer

Resolve repository documents and recipes from the owning repository root;
resolve references bundled with this skill from the skill directory.

Use `docs/primer-workflow-skills.md` for routing and the shared decision
checklist. Planning precedes drafting; stop at the agreed plan unless drafting
is authorised.

Read `docs/primer-production-procedure.md`, `docs/templates/primer-brief.md`,
`STYLE_GUIDE.md`, and the relevant task routes in `docs/project-contract.md`.
Read the repository state before proposing edits: issue, branch, dirty paths,
existing source or companion documents, and build recipe.

When planning a forward test of revised guidance, calibrate against the current
revised primer and its tracked brief and audit at identified revisions. Before
testing, re-scope historical findings against those artefacts: distinguish gaps
that remain, findings already addressed, explicit scope reductions, and items
not checked. Retain stable route and concept IDs when relating the findings to
the current reader promise; do not treat an old finding as a current gap without
checking it.

Plan synthetic fixtures and realistic current-primer evidence separately.
Fixtures can exercise known cases and failure modes, but cannot by themselves
establish that the guidance works on the current primer. Record each test's
input, revision, intended observation, result, and limits. Primary and
alternative teaching gaps remain content blockers; plan the content gate and
release-readiness decision as separate judgements.

Create a tracked, revision-bound brief; an issue comment or ignored
`.scratch/` note is supporting material, not the release brief. Record the
brief revision and stable `route_id` and `concept_id` values; each concept row
must reference its `route_id`. Each route row
must use exactly one tier: `primary`, `alternative`, or `reference-only`.
Each concept row must cover reader action, mechanism/reasoning, significance,
teaching device, worked evidence, interpretation, limitations, downstream use,
and source plan. Define the reader, prerequisites, motivating problem,
exclusions, dependency-led route, qualitative depth, examples, cases, figures,
languages, evidence plan, and open decisions. Explain why the proposed
structure solves the reader's problem.

Treat coverage and explanatory quality as the primary planning criteria. Build a
coverage matrix for the topics a competent reader must understand and be able to
apply, then use the dependency-led route to determine the necessary depth. Word
count is an outcome of that coverage and depth: use a range only as a rough
planning estimate after the structure is established, never as an upper bound
that forces omissions or shallow treatment.

Classify every proposed route as primary, alternative, or reference-only before
drafting. A primary or alternative route needs a teaching spine: a motivating
problem, the organising model, at least one worked or executable application,
interpretation of its result, and a material failure mode or limit. A route that
cannot support that spine is too broad for the brief and must be narrowed,
demoted to reference material, or removed. Do not retain a route merely because
it is popular, technically interesting, or easy to list.

For a primer that teaches a process, system, or applied method, complete the
teaching-case contract in `docs/templates/primer-case-contract.md` before
drafting. In the brief, key a continuous worked-case trace to each applicable
primary or alternative `route_id`. Follow the same case from input or
assumptions through transformation, intermediate representation, reader-facing
operation, interpretation, and failure or boundary; include correction and
re-evaluation when the failure can be addressed. Show what each stage hands to
the next, the planned evidence, and whether that stage is `executable`,
`illustrative`, or `reference-only`. Record measured evidence separately when
relevant; a measurement is not a stage mode. A fixture that begins as curated
final claims is not, by itself, an end-to-end case. A required stage marked
`reference-only` does not establish a worked teaching spine: expand that stage
or narrow or demote the route. If no coherent case is appropriate, record the
reason and identify the alternative teaching device that will carry the
explanation.

Balance optional branches against the main route before adding them. Name the
reader need each branch serves, the worked evidence it adds, and the material
it displaces or shortens; retain the primary route's complete teaching spine.
If the trade-off cannot be justified, narrow, demote, or remove the branch.
For every unresolved concept, record an explicit decision to expand it, narrow
or demote its route, or remove it, with the reason and effect on reader outcomes.
Preserve retired `route_id` and `concept_id` values in the decision record;
never reuse them for a different subject.

Map each core concept in the brief to the schema fields above and to an
appropriate teaching device such as a worked case, comparison, counterexample,
proof, or failure case. Include downstream use and the source plan even when
the concept is concise. Do not impose word or heading quotas, or use an example
quota as a proxy for this mapping.

Before drafting, review the matrix adversarially: ask what a reader would do to
demonstrate understanding of each concept, what evidence in the primer would
let them do it, and where the explanation could still be mistaken for a label or
catalogue entry. Check that every applicable taught route has a trace whose
stage outputs feed the next stage, whose modes and evidence are explicit, and
whose interpretation and failure or boundary are supported. Check the optional
branch trade-offs and resolve each concept decision against the intended reader
outcome. Record unresolved rows as blocking planning gaps. A green build plan,
fixture, or example manifest does not discharge a missing explanation.
The later audit must retain the same identifiers and bind its evidence to the
reviewed source revision; do not silently rename, merge, or omit rows.
After drafting and before handing the source to audit, compare each drafted
primary and alternative route with its brief and worked-case trace, keyed by
`route_id`. Follow the reader-facing transitions from input through operation,
intermediate reasoning, result, interpretation, and limit; use the planned
alternative teaching device where a continuous case does not apply. Record draft
locators, gaps, and decisions in the brief's post-draft checkpoint. A passing
example or fixture does not establish that the prose explains those transitions.
An unsupported transition blocks audit handoff until the explanation is expanded
or the route is explicitly narrowed or demoted. Record any scope reduction,
its rationale, and its effect on the reader promise; revise the brief and reader
facing scope accordingly, retaining stable IDs. This is a qualitative check,
not a substitute for the independent audit.
Before handoff, check the brief against the trace and scope acceptance fields
in `docs/templates/primer-brief.md`, including the decision record for any
retired IDs. Once the audit exists, run
`just check-primer-evidence <brief> <audit>` for matrix structure and matching
IDs; this mechanical check does not judge the case's explanatory quality.

If delegation is useful, split bounded, disjoint questions by ownership. Give
each worker a concrete question, scope, stop condition, and requested evidence;
choose capability and reasoning depth for the question rather than freezing a
model name. Do not ask workers to duplicate the same survey. Record decisions
at a checkpoint before drafting and close completed workers.

Do not create a document, publish, merge, or broaden scope merely because this
skill was invoked. The user or issue controls those decisions.
