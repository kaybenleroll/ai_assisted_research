# Portable primer workflow skills

The canonical workflow skills live under `.agents/skills/`. They use the
portable Agent Skills directory shape: each skill is a directory containing a
`SKILL.md` with `name`, `description`, and direct instructions. The skills are
small entry points; the procedure, style guide, build system, review checklist,
and handoff template remain the authoritative sources.

| Skill | Use it for |
|---|---|
| `primer-plan` | Brief, scope, dependency-led outline, examples, evidence plan |
| `primer-audit` | Whole-document and risk-selected post-draft review |
| `primer-render-qa` | Container builds, examples, output checks, and visual QA |
| `primer-handoff` | Durable cross-harness handoff, PR evidence, and release boundary |

## Harness policy

The neutral `.agents/skills/` location is the source of truth. A harness may
discover it directly, expose it through a native skills directory, or require a
thin adapter. Discovery is not assumed from similar filenames. Before adding an
adapter, run the read-only smoke test in `docs/agent-collaboration.md` and
record the harness version, settings, discovered files, and task route. An
unavailable harness is unverified, not a pass.

The skills do not override user scope, force publication, select a vendor or
model, or require a particular number of agents. Delegation is capability-based:
workers have bounded ownership, explicit stop conditions, independent review
where appropriate, and durable checkpoints. Completed workers are closed.
