# Portable primer workflow skills

The canonical workflow skills live under `.agents/skills/`. They use the
portable Agent Skills directory shape: each skill is a directory containing a
`SKILL.md` with `name`, `description`, and direct instructions. The skills are
small entry points; the procedure, style guide, build system, review checklist,
and handoff template remain the authoritative sources.

## Choosing a skill

| Need | Inputs | Output | Stopping boundary |
|---|---|---|---|
| [`primer-plan`](../.agents/skills/primer-plan/SKILL.md): define a new or substantial revision | Issue, existing material, repository state and brief template | Brief, outline, examples and evidence plan | Stop at the agreed scope; draft only if authorised. |
| [`primer-audit`](../.agents/skills/primer-audit/SKILL.md): review content after drafting or revision | Brief, complete source, outputs and review guidance | Findings, evidence and unresolved risks | Report findings within scope; a failed check does not authorise repair. |
| [`primer-render-qa`](../.agents/skills/primer-render-qa/SKILL.md): check published outputs and build evidence | Committed outputs, build recipe, runtime and permitted scope | Check results, provenance and visual observations | Stop when a required check cannot run safely; do not overwrite outputs outside authorised scope. |
| [`primer-handoff`](../.agents/skills/primer-handoff/SKILL.md): transfer work at any bounded stage | Live repository state, decisions and available evidence | Handoff with remaining work and next owner | Stop at the handoff; release requires authorisation and required evidence. |

If your harness does not discover or activate skills, choose a task above,
open its linked `SKILL.md`, and follow its instructions manually alongside the
project contract and applicable repository guidance. Resolve repository
documents and recipes from the owning repository root; resolve references
bundled with a skill from that skill's directory.

Plan before drafting a new primer or substantial revision. Audit and render QA
are complementary: content review does not establish output quality, and a
successful render does not establish content correctness. Choose the skills
the task needs; there is no requirement to use all four or meet a quota. This
guidance is the shared router; it does not require a dedicated router skill.

## Decision checklist

Before starting and when handing off, establish:

- The objective, scope, revision, dirty paths and permitted writes, including
  whether existing outputs may be changed.
- The provenance of evidence: source or artefact, revision, commands and
  relevant runtime or source version. Identify stale or unavailable evidence.
- What was inspected, executed, sampled or reported historically. Record the
  extent and limits of each; inspection or sampling is not execution, and
  historical evidence is not a current check.
- The stopping boundary, unresolved findings, and the next action and owner.

A failed check identifies work to report; it does not itself authorise repair.

## Harness policy

The neutral `.agents/skills/` location is the source of truth. A harness may
discover it directly, expose it through a native skills directory, or require a
thin adapter. Discovery is not assumed from similar filenames. Do not add a
`.claude/skills/` adapter, copied skill bodies, or a root `CLAUDE.md` for this
purpose without evidence from the read-only [harness smoke test](agent-collaboration.md#harness-smoke-test)
that an adapter is needed. Any justified adapter is separate work. An
unavailable harness is unverified, not a pass.

The skills do not override user scope, force publication, select a vendor or
model, or require a particular number of agents. Delegation is capability-based:
workers have bounded ownership, explicit stop conditions, independent review
where appropriate, and durable checkpoints. Completed workers are closed.
