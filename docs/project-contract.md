# Project Contract

## Purpose and Scope

This repository publishes technical primers and related documents. Apply this
contract repository-wide, then follow more specific instructions for the task
and subdirectory. Explicit user instructions and higher-priority harness or
system instructions take precedence. This document is a collaboration
contract, not a permission or security boundary: the active environment owns
permissions, network access, sandboxing, and approval policy.

## Task Routing

| Task | Read |
|---|---|
| Repository process, setup, builds, render QA, or a new document | [Contributing](../CONTRIBUTING.md) |
| Authored prose, headings, examples, or citations | [Style guide](../STYLE_GUIDE.md) |
| Mathematical notation, theorem format, or maths rendering policy | [Maths notation](math-notation.md) |
| Content review passes and visual QA | [Review checklist](review-checklist.md) |
| Cross-harness handoffs and smoke tests | [Agent collaboration notes](agent-collaboration.md) |
| Catastrophe workbook | [Workbook README](../workbook_catmodel_elt_documents/README.md), then its Justfile |
| Silo RPG content | [Silo index](../gaming_silo_rpg/gaming_silo_index.md) first; use the mandate below |

## Repository Invariants

- Render in containers; do not install build libraries on the host.
- Never commit or push directly to `main`.
- Commit source documents and their required published outputs together; do not commit intermediate files.
- Use UK English in repository-authored prose. Follow [STYLE_GUIDE.md](../STYLE_GUIDE.md).
- Use [CONTRIBUTING.md](../CONTRIBUTING.md) for build and render commands. The Mermaid filter lives in `_shared/filters/`.
- Start a new Pandoc primer with `just new-primer <short> "<Full Title>"`; finish the printed registration steps in [CONTRIBUTING.md](../CONTRIBUTING.md).

<a id="primer-build-and-render-notes"></a>

## Document Classes

- Pandoc primers use thin per-project Justfiles and `_shared/common.just`. Directories: `primer_building_ai_agents`, `primer_claude_code_alternative`, `primer_codex_for_claude_code_users`, `primer_comparative_religion`, `primer_complex_analysis`, `primer_containerization`, `primer_deep_learning`, `primer_digital_signal_processing`, `primer_evaluation_loop`, `primer_fluid_mechanics`, `primer_hermes_server`, `primer_information_theory`, `primer_linux_git_workflows`, `primer_military_structure`, `primer_ml_optimisation`, `primer_numerical_analysis`, `primer_ohmyzsh`, `primer_openclaw`, `primer_pi_coding_agent`, `primer_political_systems`, `primer_python_for_r_users`, `primer_research_local_llms`, `primer_retrieval_rag`, `primer_spectral_graph_theory`.
- Gaming materials in `gaming_silo_rpg/` share the Pandoc infrastructure and retain their `gaming_` filenames.
- The repository-authored information theory article is being replaced by `primer_information_theory` under #163.
- `workbook_catmodel_elt_documents/` uses Quarto, R, and Python, with its own build system and `workbook_` filenames.

## Collaboration and Handoffs

The working tree, Git history, tests, build commands, and issue or pull request
are the durable state shared between Claude Code, Codex, Pi, and other
harnesses. A conversation is not. Before editing, inspect `git status`, the
current branch and the relevant diff. Preserve unrelated tracked and
untracked changes; stop if the observed state conflicts with the assigned
scope.

Serial hand-offs are safe when the first session stops and the second session
rechecks the working tree. Do not run two writers in one checkout at the same
time. Use separate branches and Git worktrees for independent concurrent work,
and assign one owner to integration and generated outputs. A reviewer should
work from a clean or committed state and should not silently become a second
implementer.

When a handoff needs more than the issue or PR, record a short note in ignored
`.scratch/` or an appropriate issue/PR comment. Include the objective and
issue, branch and starting revision, owned and changed paths, decisions and
evidence, exact checks and results, remaining work, and blockers. Do not put
credentials, private transcripts, or hidden reasoning in a handoff.

Native skills, subagents, hooks, MCP servers, commands, permissions, and
sandbox settings remain harness-specific. Share the underlying procedure in
repository documentation or a deterministic `just` recipe, then add a thin
native adapter only when a harness-specific entry point materially helps. Do
not infer that a file loaded by one harness is loaded by another, or that
similar names imply equivalent semantics.

## Issues and Pull Requests

Work issue-first, with one issue per PR. Branches follow
`<type>/<issue#>-<slug>`. `.github/labels.json` is the source of truth for
priority, type, area, and effort labels. Use `[infra]` or the primer short name
in issue titles. Open the PR body with `Closes #N` for its issue. For a
per-primer PR under a sweep issue, use `Refs #N`; only the owner-designated
final PR uses `Closes #N` for the sweep. A typo or single-line fix may use
`No-issue: <reason>` as documented in [CONTRIBUTING.md](../CONTRIBUTING.md).
Squash merge by default; use a merge commit when retaining a stacked chain or
individual commits matters.

## Silo Context Navigation Mandate

When asked anything about Silo RPG lore, rules, mechanics, setting, or campaign
content:

1. Read `gaming_silo_rpg/gaming_silo_index.md` first. It is the routing map.
2. Do not load the bibles whole. Never read `gaming_silo_comprehensive_bible.md`, `gaming_silo_player_guide.md`, `gaming_silo_gm_secrets.md`, or `gaming_silo_starter_campaign.md` in their entirety.
3. Use grep or line-range reads to pull only the specific sections identified by the index.

The source documents are `gaming_silo_player_guide.md`,
`gaming_silo_gm_secrets.md`, `gaming_silo_comprehensive_bible.md`, and
`gaming_silo_starter_campaign.md`. The compact reference sheets are
`gaming_reference_silo_index.md`, `gaming_reference_silo_player.md`,
`gaming_reference_silo_gm.md`, and `gaming_reference_silo_campaign.md`; they
are small enough to read whole after consulting the index.

## Definition of Done

1. Confirm the issue scope and inspect the affected source, companion documents, and build recipes.
2. Run the relevant commands in [CONTRIBUTING.md](../CONTRIBUTING.md): recipe checks, container renders where outputs change, render QA, and repository checks appropriate to the change.
3. Check links, committed outputs, `git diff --check`, and the exact changed-path scope before opening the PR.
4. State the commands run, results, and limitations in the PR, and link or reference the issue as required.

## Adapters and Limits

`AGENTS.md` is the canonical repository entry point. The active harness may
discover it, apply additional user or managed instructions, or use a
harness-specific adapter elsewhere. Read this contract explicitly when a
harness does not automatically follow local links. Nothing here grants tools,
permissions, network access, hooks, skills, or subagent isolation.
