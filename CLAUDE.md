# Claude Code — ai_assisted_research

## Repo Purpose

AI-generated technical primers rendered to HTML + PDF via pandoc, orchestrated with `just`. Source and outputs are both committed.

---

## Document Classes

**Pandoc primers** — source → HTML + PDF via `localhost/primers-pandoc:latest`; each has a thin `Justfile` importing `_shared/common.just`. Directories: `building_ai_agents`, `deep_learning_primer`, `political_systems`, `numerical_analysis_primer`, `claude_code_alternative`, `openclaw_primer`, `research_local_llms`, `silo_rpg_primer`, `info_theory_article`.

**Exception** — `catmodel_elt_documents/`: Quarto + R + Python pipeline, not pandoc, not `_shared/common.just`. Treat as a separate build system.

---

## Standard Primer Layout

```
<project>/
  <name>.md          # sole markdown source
  Justfile           # thin: vars + import '../_shared/common.just'
  <name>.html        # committed output
  <name>.pdf         # committed output
```

No intermediates tracked in git.

---

## Adding a New Primer

1. Create `<project>/Justfile`:

```just
SOURCE_MD   := "<name>.md"
PROJECT_DIR := "<project>"
TITLE       := "Full Title String"
AUTHOR      := "Month Year"
HTML_EXTRA  := ""
PDF_EXTRA   := ""

import '../_shared/common.just'
```

2. Add targets to the top-level `Justfile` (follow existing pattern).
3. Commit only `.md`, `Justfile`, `.html`, `.pdf` — no intermediates.
4. **Update `README.md`** — add a row linking the `.html` file. The README is the GitHub Pages landing page.

---

## Primer Build and Render Notes

- All rendering must run in containers; never install libraries on the host
- Use wrapper recipes (e.g. `full`) to chain `_shared/common.just` targets — `just` does not support recipe overrides
- Add `--mathjax` to `HTML_EXTRA` for TeX math in HTML output
- Use `--number-sections` (and shift flags) consistently across all primers
- Use `--shift-heading-level-by=-1` with `--number-sections` on docs with a body `# H1` + `##` sections — without the shift, `##` numbers as 1.1 not 1
- Plots: use R via the rocker container (pandoc container has no pip); commit the generation script alongside figure outputs
- Mermaid: uses a Lua filter in `_shared/` generating PNG intermediates; prefer Mermaid for PDF output (ASCII fails in xelatex font rendering)
- Configure DejaVu Sans Mono as monospace font when code blocks contain Greek — lmmono lacks Greek coverage
- Grep xelatex output for `Error|Missing \$|Undefined control`; generic warning grep misses actual failures
- Verify rendered PDF exists and has non-trivial file size before committing
- Grep prose for embedded section references before stripping or renumbering headings
- Scan `text` code blocks before planning diagram replacement
- Pre-share a notation contract with all parallel agents writing mathematical content

---

## Silo RPG — Context-Navigation Mandate

When asked anything about Silo RPG lore, rules, mechanics, setting, or campaign content:

1. **Read `silo_rpg_primer/silo_index.md` first.** It is the routing map. Do not skip it.
2. **Do not load the bibles whole.** Never read `silo_comprehensive_bible.md`, `silo_player_guide.md`, `silo_gm_secrets.md`, or `silo_starter_campaign.md` in their entirety — they are large.
3. **Surgical extraction only.** Use grep or line-range reads to pull the specific sections identified by the index.

Source documents:
- `silo_player_guide.md` — player-facing rules and setting knowledge
- `silo_gm_secrets.md` — GM-only lore and hidden mechanics
- `silo_comprehensive_bible.md` — full world reference
- `silo_starter_campaign.md` — the introductory campaign

---

## Writing Style

See `STYLE_GUIDE.md` for house style when generating or editing primer content.
