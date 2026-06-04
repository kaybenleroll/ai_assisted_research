# Claude Code — ai_assisted_research

## Repo Purpose

Growing collection of AI-generated technical primers. Each primer is a long-form markdown document rendered to HTML and PDF via pandoc, committed alongside its source. The repo is orchestrated with `just`.

---

## Two Document Classes

### Pandoc Primers (most of the repo)

Markdown source → HTML + PDF via the `localhost/primers-pandoc:latest` container image.

Each primer lives in its own subdirectory with a thin `Justfile` that sets variables and imports shared recipes from `_shared/common.just`. Outputs (`.html`, `.pdf`) are committed; no intermediate files are tracked.

**Primer directories:**
- `building_ai_agents/`
- `political_systems/`
- `numerical_analysis_primer/`
- `claude_code_alternative/`
- `openclaw_primer/`
- `research_local_llms/`
- `silo_rpg_primer/`
- `info_theory_article/`

### Computational Documents (exception)

`catmodel_elt_documents/` only. Uses a Quarto + R + Python pipeline, not pandoc. Does **not** use `_shared/common.just`. Treat it as an entirely separate build system.

---

## Standard Primer Layout

```
<project>/
  <name>.md          # sole markdown source
  Justfile           # thin: vars + import '../_shared/common.just'
  <name>.html        # committed output
  <name>.pdf         # committed output
```

No intermediates, no generated subdirectories tracked in git.

---

## Adding a New Primer

1. Create `<project>/Justfile` with these variables, then import:

```just
SOURCE_MD   := "<name>.md"
PROJECT_DIR := "<project>"
TITLE       := "Full Title String"
AUTHOR      := "Month Year"
HTML_EXTRA  := ""          # pandoc flags appended to HTML invocation
PDF_EXTRA   := ""          # pandoc flags appended to PDF invocation

import '../_shared/common.just'
```

2. Add corresponding targets to the top-level `Justfile` (follow existing pattern).

3. Do not add intermediates to git. Commit only `.md`, `Justfile`, `.html`, `.pdf`.

---

## Silo RPG — Context-Navigation Mandate

When asked anything about Silo RPG lore, rules, mechanics, setting, or campaign content:

1. **Read `silo_rpg_primer/silo_index.md` first.** It is the routing map. Do not skip it.
2. **Do not load the bibles whole.** Never read `silo_comprehensive_bible.md`, `silo_player_guide.md`, `silo_gm_secrets.md`, or `silo_starter_campaign.md` in their entirety — they are large.
3. **Surgical extraction only.** Use grep or line-range reads to pull the specific sections identified by the index. Confirm you have what you need before expanding scope.

The four source documents and their roles:
- `silo_player_guide.md` — player-facing rules and setting knowledge
- `silo_gm_secrets.md` — GM-only lore and hidden mechanics
- `silo_comprehensive_bible.md` — full world reference
- `silo_starter_campaign.md` — the introductory campaign

---

## Writing Style

See `STYLE_GUIDE.md` for house style when generating or editing primer content.
