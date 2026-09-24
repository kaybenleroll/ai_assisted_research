# Claude Code — ai_assisted_research

## Repo Purpose

AI-generated technical primers rendered to HTML + PDF via pandoc, orchestrated with `just`. Source and outputs are both committed.

---

## Document Classes

**Pandoc primers** — source → HTML + PDF via `localhost/primers-pandoc:latest`; each has a thin `Justfile` importing `_shared/common.just`. Directories: `primer_building_ai_agents`, `primer_claude_code_alternative`, `primer_codex_for_claude_code_users`, `primer_comparative_religion`, `primer_containerization`, `primer_deep_learning`, `primer_evaluation_loop`, `primer_hermes_server`, `primer_military_structure`, `primer_numerical_analysis`, `primer_ohmyzsh`, `primer_openclaw`, `primer_pi_coding_agent`, `primer_political_systems`, `primer_python_for_r_users`, `primer_research_local_llms`.

**Gaming materials** — `gaming_silo_rpg/` uses the same Pandoc infrastructure but keeps a `gaming_` prefix for its documents.

**Article** — `article_info_theory/` is an article series, not a primer.

**Exception** — `workbook_catmodel_elt_documents/`: Quarto + R + Python pipeline, not pandoc, not `_shared/common.just`. Treat as a separate build system. Its documents and render scripts use the `workbook_` prefix.

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
- `primer_building_ai_agents` and `primer_numerical_analysis` have `html-mathml`/`html-mathjax` variant targets that `html-full`/`html-dev` don't regenerate — rebuild them explicitly when applying a fix across primers, or they silently carry pre-existing drift.
- Grep prose for embedded section references before stripping or renumbering headings
- Scan `text` code blocks before planning diagram replacement
- Pre-share a notation contract with all parallel agents writing mathematical content

---

## Silo RPG — Context-Navigation Mandate

When asked anything about Silo RPG lore, rules, mechanics, setting, or campaign content:

1. **Read `gaming_silo_rpg/gaming_silo_index.md` first.** It is the routing map. Do not skip it.
2. **Do not load the bibles whole.** Never read `gaming_silo_comprehensive_bible.md`, `gaming_silo_player_guide.md`, `gaming_silo_gm_secrets.md`, or `gaming_silo_starter_campaign.md` in their entirety — they are large.
3. **Surgical extraction only.** Use grep or line-range reads to pull the specific sections identified by the index.

Source documents:
- `gaming_silo_player_guide.md` — player-facing rules and setting knowledge
- `gaming_silo_gm_secrets.md` — GM-only lore and hidden mechanics
- `gaming_silo_comprehensive_bible.md` — full world reference
- `gaming_silo_starter_campaign.md` — the introductory campaign

---

## Workflow — Issues and PRs

Work is issue-first.

- **One issue per PR.** Every PR body opens with `Closes #N`. Unrelated changes (e.g. config tweaks already sitting on a branch) go in their own PR.
- **Branch names:** `<type>/<issue#>-<slug>`, e.g. `docs/88-issue-first-workflow`. Never commit to `main`.
- **Issue titles** carry a document prefix in brackets: `[pi]`, `[openclaw]`, `[infra]`, etc. Use the primer's short name (directory minus `primer_`).
- **Labels** follow the canonical scheme enforced by the issue hook: 1 Priority (`P0`–`P3`) + 1 Type + 1+ Area + 1 Effort. Primers are usually `area: ai-agent` (agent/coding-tool primers) or `area: devops` (build, infra, tooling).
- **Tracking issues:** each primer that needs ongoing upkeep gets one `type: research` tracking issue (e.g. verification and refresh cadence); sub-work is filed as separate issues linked to it.
- **Cross-primer sweeps** (e.g. a fix applied to every primer) get one issue with a per-primer checklist.
- **PR-only exceptions:** typos and single-line fixes may skip the issue.
- **Adding a primer** still follows the checklist above; the README row and top-level `Justfile` targets belong in the same PR as the primer.

---

## Writing Style

See `STYLE_GUIDE.md` for house style when generating or editing primer content.
