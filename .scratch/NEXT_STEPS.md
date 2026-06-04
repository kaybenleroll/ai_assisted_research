# random_llm_projects consolidation — Phases B, C, D

Branch: main | Last commit: 434dfeb

## What's done

Phase A complete (uncommitted, untracked in `_shared/`):
- `_shared/Dockerfile` — fat pandoc image (latex + fonts + mermaid + chromium)
- `_shared/pandoc-compact-code.latex` — canonical LaTeX fragment
- `_shared/common.just` — shared variables + base recipes

Validated: `just import`, `justfile_directory()` scoping, dry-run HTML/PDF expansions.
Full plan at: `/home/mcooney/.claude/plans/compressed-gathering-lynx.md`

## What's pending

### Phase B — Migrate the 6 pandoc primers

Convert each project to a thin Justfile that sets vars then `import '../_shared/common.just'`.

Per-project specifics:
| Project | HTML_EXTRA | Notes |
|---|---|---|
| `building_ai_agents` | `--mathjax --lua-filter=filters/mermaid-to-image.lua` | Also has `agent_quick_reference.md` companion; has 3 math-variant HTML targets to preserve |
| `political_systems` | `--number-sections` | Retire `political_systems/Dockerfile` |
| `numerical_analysis_primer` | `--mathjax` | Has mathml/mathjax variants to preserve |
| `claude_code_alternative` | `` (none) | No math flag |
| `openclaw_primer` | `` (none) | Convert `render.sh` → Justfile; delete render.sh after |
| `research_local_llms` | `` (none) | Convert `render.sh` → Justfile; delete render.sh after |

Then update the **top-level `Justfile`**: uniform `cd <project> && just <recipe>` calls;
add `build-image` target; keep `html-dev`/`html-full`; keep catmodel targets as-is.

### Phase C — Documentation (can run in parallel with B)

- `CLAUDE.md` at repo root: repo purpose, two-class taxonomy (pandoc primers vs
  computational documents), standard project layout, how to add a new primer, silo
  context-navigation guidance (absorb from `silo_rpg_primer/GEMINI.md`, then retire
  GEMINI.md and its AGENTS.md symlink).
- `STYLE_GUIDE.md` at repo root: writing tone/style, self-contained as AI prompt context.

### Phase D — Orphan rescue

- `silo_rpg_primer/Justfile` — 5 docs, each to HTML+PDF:
  `silo_index`, `silo_player_guide`, `silo_gm_secrets`, `silo_comprehensive_bible`,
  `silo_starter_campaign`. Cannot use single-SOURCE_MD pattern — needs 5 named recipes
  or a loop. Derive titles from each doc's H1.
- `info_theory_article/Justfile` — single combined markdown. Title: "Information Theory:
  A Series" (derive from H1). Leave `html_articles/` untouched (source material).
- Add both to top-level orchestration targets.

**Note on Phase D outputs:** Committed silo HTML are bare fragments (no `--standalone`,
no template). Committed info_theory HTML uses default pandoc template. Re-rendering
with `doc_template.html` will substantially change them — this is intended.

## Key decisions (all settled, do not re-derive)

- Single fat image `localhost/primers-pandoc:latest`
- `just import` of `../_shared/common.just`; per-project vars set BEFORE the import
- Outputs stay in git; `clean` doesn't touch HTML/PDF; `clobber` recipe for destructive removal
- `breezedark` everywhere (intentional visual change for openclaw + research_local_llms)
- `HTML_FLAGS_BASE` + `HTML_EXTRA` per-project (NOT a single shared flag string)
- Mermaid filter stays local to `building_ai_agents` only
- Separate `STYLE_GUIDE.md` from `CLAUDE.md`
- catmodel unchanged; stays in top-level orchestration

## Execution model

Main session orchestrates only. All implementation work goes to subagents.
All scratch/test files go in `.scratch/`, never `/tmp`.

Suggested dispatch:
- Phase A commit: 1 subagent to `git add _shared/ && git commit`
- Phase B: fan-out 6 subagents (one per project) + 1 for top-level Justfile
- Phase C: 1 subagent (independent of B, run in parallel)
- Phase D: 1-2 subagents (depends on A/B being done first)

## Verification

After Phase B Justfiles are written, build image once: `just build-image`
Then per-project: `just all` — check `git diff --stat` for expected output changes only.
Phase D: eyeball new HTML/PDF since no like-for-like baseline exists.
