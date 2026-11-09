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

Complete the brief template in the issue or an ignored `.scratch/` note. Define
the reader, prerequisites, motivating problem, exclusions, dependency-led route,
qualitative depth, examples, cases, figures, languages, evidence plan, and open
decisions. Explain why the proposed structure solves the reader's problem.

For a primer that teaches a process, system, or applied method, complete the
teaching-case contract in `docs/templates/primer-case-contract.md` before
drafting. Identify the source inputs or assumptions, transformations and
decisions, intermediate representation, useful questions or outputs, expected
interpretation, and failure modes or limits. State which stages are executable,
illustrative, or measured. A fixture that begins as curated final claims is not,
by itself, an end-to-end case. If no coherent case is appropriate, record the
reason and identify the alternative teaching device that will carry the
explanation.

Map each core concept in the brief to its mechanism or reasoning, significance,
conditions or limits, and an appropriate teaching device such as a worked case,
comparison, counterexample, proof, or failure case. Do not use a heading count
or word quota as a proxy for this mapping.

If delegation is useful, split bounded, disjoint questions by ownership. Give
each worker a concrete question, scope, stop condition, and requested evidence;
choose capability and reasoning depth for the question rather than freezing a
model name. Do not ask workers to duplicate the same survey. Record decisions
at a checkpoint before drafting and close completed workers.

Do not create a document, publish, merge, or broaden scope merely because this
skill was invoked. The user or issue controls those decisions.
