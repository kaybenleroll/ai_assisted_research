# Repository Guide

## Purpose

This repository publishes technical primers and related documents. Sources and rendered HTML and PDF outputs are committed together. Read this guide as a route to the instructions for the task at hand.

## Read Before You Edit

| Task | Read |
|---|---|
| Repository process, setup, builds, render QA, or a new document | [CONTRIBUTING.md](CONTRIBUTING.md) |
| Authored prose, headings, examples, or citations | [STYLE_GUIDE.md](STYLE_GUIDE.md) |
| Content review passes and visual QA | [docs/review-checklist.md](docs/review-checklist.md) |
| Catastrophe workbook | [Workbook README](workbook_catmodel_elt_documents/README.md), then its Justfile |
| Silo RPG content | `gaming_silo_rpg/gaming_silo_index.md` first; see the mandate below |

## Document Classes

- Pandoc primers use thin per-project Justfiles and `_shared/common.just`. Directories: `primer_building_ai_agents`, `primer_claude_code_alternative`, `primer_codex_for_claude_code_users`, `primer_comparative_religion`, `primer_complex_analysis`, `primer_containerization`, `primer_deep_learning`, `primer_digital_signal_processing`, `primer_evaluation_loop`, `primer_hermes_server`, `primer_military_structure`, `primer_numerical_analysis`, `primer_ohmyzsh`, `primer_openclaw`, `primer_pi_coding_agent`, `primer_political_systems`, `primer_python_for_r_users`, `primer_research_local_llms`.
- Gaming materials in `gaming_silo_rpg/` share the Pandoc infrastructure and retain their `gaming_` filenames.
- A repository-authored information theory article is pending replacement in #163.
- `workbook_catmodel_elt_documents/` uses Quarto, R, and Python, with its own build system and `workbook_` filenames.

## Repository Invariants

- Render in containers; do not install build libraries on the host.
- Never commit or push directly to `main`.
- Commit source documents and their required published outputs together; do not commit intermediate files.
- Use UK English in repository-authored prose. Follow [STYLE_GUIDE.md](STYLE_GUIDE.md).
- Use [CONTRIBUTING.md](CONTRIBUTING.md) for build and render commands. The Mermaid filter now lives in `_shared/filters/`.

<a id="primer-build-and-render-notes"></a>

## Issues and Pull Requests

- Work issue-first, with one issue per PR. Branches follow `<type>/<issue#>-<slug>`.
- `.github/labels.json` is the source of truth for priority, type, area, and effort labels. Use `[infra]` or the primer short name in issue titles.
- Open the PR body with `Closes #N` for its issue. For a per-primer PR under a sweep issue, use `Refs #N`; only the owner-designated final PR uses `Closes #N` for the sweep.
- Squash merge by default; use a merge commit when retaining a stacked chain or individual commits matters. See [CONTRIBUTING.md](CONTRIBUTING.md) for the full workflow.

## Silo RPG Context Navigation Mandate

When asked anything about Silo RPG lore, rules, mechanics, setting, or campaign content:

1. **Read `gaming_silo_rpg/gaming_silo_index.md` first.** It is the routing map. Do not skip it.
2. **Do not load the bibles whole.** Never read `gaming_silo_comprehensive_bible.md`, `gaming_silo_player_guide.md`, `gaming_silo_gm_secrets.md`, or `gaming_silo_starter_campaign.md` in their entirety — they are large.
3. **Surgical extraction only.** Use grep or line-range reads to pull the specific sections identified by the index.

Source documents:
- `gaming_silo_player_guide.md` — player-facing rules and setting knowledge
- `gaming_silo_gm_secrets.md` — GM-only lore and hidden mechanics
- `gaming_silo_comprehensive_bible.md` — full world reference
- `gaming_silo_starter_campaign.md` — the introductory campaign

## Definition of Done

1. Confirm the issue scope and inspect the affected source, companion documents, and build recipes.
2. Run the relevant commands in [CONTRIBUTING.md](CONTRIBUTING.md): recipe checks, container renders where outputs change, render QA, and repository checks appropriate to the change.
3. Check links, committed outputs, `git diff --check`, and the exact changed-path scope before opening the PR.
4. State the commands run, results, and any limitations in the PR. Link or reference the issue as above.
