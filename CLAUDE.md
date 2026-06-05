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
- `deep_learning_primer/`
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

4. **Update `README.md`** at the repo root — add a row to the appropriate table with the document title linked to its `.html` file. The README is the GitHub Pages landing page; every new document must appear there.

---

## Primer Build and Render Notes

- Commit the generation script alongside figure outputs for reproducibility
- Add `--mathjax` to `HTML_EXTRA` to enable TeX math rendering in HTML output
- When grepping xelatex output for errors, use `Error|Missing \$|Undefined control` — generic warning grep misses actual failures
- Verify the rendered PDF exists and has non-trivial file size before committing
- Scan all ` ```text ``` ` blocks in a primer before planning diagram replacement — prevents missed diagrams during build work
- For important primer topics, use full coverage rather than cross-references to other documents
- Use wrapper recipes (e.g. `full`) to chain shared targets from `_shared/common.just` — `just` does not support override of imported recipes
- Grep document prose for embedded section references before stripping or renumbering headings
- Apply `--number-sections` (and any shift flags) consistently across all primers when setting the standard — piecemeal application was the original defect
- Primer plot generation uses R via the rocker container — the pandoc container has no pip
- Use `--shift-heading-level-by=-1` with `--number-sections` when the source has a body `# H1` followed by `##` sections — without the shift, `##` sections number as 1.1 not 1
- Configure DejaVu Sans Mono as monospace font in PDF headers when code blocks contain Greek characters — lmmono lacks Greek coverage
- Mermaid diagram support uses a Lua filter in `_shared/` that generates PNG intermediates before pandoc runs
- All rendering and computation must run in containers to ensure reproducibility; do not install libraries on the host for primer builds
- Pre-share a notation contract table with all parallel agents writing mathematical content

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
