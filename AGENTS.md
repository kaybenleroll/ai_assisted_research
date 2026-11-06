# Repository Instructions

This is the canonical repository instruction file for Codex, Claude Code, Pi,
and other harnesses that discover `AGENTS.md`. Read the [project contract](docs/project-contract.md)
before repository work, then read the
task-specific documents it names. The contract contains the detailed
invariants, task routes, collaboration rules, and definition of done.

## Essential rules

- Use UK English in repository-authored prose.
- Preserve unrelated tracked and untracked work. Before editing, inspect
  `git status`, the current branch, and the relevant diff.
- Never commit or push directly to `main`. Work issue-first on a branch named
  `<type>/<issue#>-<slug>` and use one coherent milestone per pull request.
- Render published documents in the repository's pinned containers. Commit
  source documents and their required HTML/PDF outputs together; do not commit
  intermediate files.
- Run the relevant checks, `git diff --check`, link checks, and render QA
  before handoff. Report exact commands, results, and limitations.
- Use the active harness's capabilities and permissions. Claude-specific hooks,
  skills, settings, and rules are not automatically available to other
  harnesses, and similarly named features do not imply equivalent semantics.

## Task routing

Read [Contributing](CONTRIBUTING.md) for repository process, builds, rendering,
and new documents; [STYLE_GUIDE.md](STYLE_GUIDE.md) for authored prose;
[maths notation](docs/math-notation.md) for mathematical notation;
[the review checklist](docs/review-checklist.md) for content and visual QA;
and [agent collaboration notes](docs/agent-collaboration.md) for cross-harness
handoffs and smoke tests. For Silo RPG work, read
`gaming_silo_rpg/gaming_silo_index.md` first and follow its restricted-reading
mandate. For the catastrophe workbook, follow its README and Justfile.

The contract remains the detailed source of truth. If these short rules and
the contract appear to disagree, stop and resolve the discrepancy before
editing.
