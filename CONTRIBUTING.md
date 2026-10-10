# Contributing

## Setup

The host needs Git, `just`, and a container runtime (Podman preferred; Docker also works). Run `just setup` from the repository root to configure Git hooks, build the shared Pandoc image, and pull the R figure image. The command is safe to repeat. Set `IMAGE` or `ROCKER` in the environment to override the respective image. Install rendering libraries inside containers, never on the host.

| Role | Image and Pin | Override | Update |
|---|---|---|---|
| Pandoc renders | `localhost/primers-pandoc:latest`, built from `docker.io/pandoc/latex@sha256:bd7641edf35bb8fad1316bacdac15fcc15f4d8d4f89051da2edcace15a6366d8` | `IMAGE` | Verify the new base digest and Pandoc version, update `_shared/Dockerfile`, run `just setup`, and check sample renders. |
| R figures | `docker.io/rocker/tidyverse:4.5.1@sha256:e58774bc0b3e15dd67d4eef5b3f7b77b1fd01b9a85e1ff5ecdd376bb06f74acc` | `ROCKER` | Verify the new digest and R version, update `_shared/images.just`, run `just setup`, and check plot recipes. |
| README generation | `docker.io/library/python:3-slim@sha256:cfe2e24a75302a15934d37c2d86412893c0aa934dc3a97cbb439d04c01890ca9` | `PYTHON_IMAGE` | Verify the new digest, update `_shared/images.just`, then run `just readme-check`. |
| Workbook | `docker.io/rocker/tidyverse@sha256:c38f0fea583e3aa82d89d0038e5bb559a04fa813881031f61f6191e683954cf2` | `WORKBOOK_IMAGE_ID` | Follow the separate image process in `workbook_catmodel_elt_documents/render.env` and its Dockerfile. |

## Layout and Naming

Most documents live in `primer_<short>/` with a thin `Justfile`, one source Markdown file, and committed HTML and PDF. New sources use `<dir>.md`, retaining underscores; existing hyphenated filenames are frozen rather than renamed. The source H1 is the canonical title and must match the Justfile `TITLE`. Do not add refresh stamps to the H1 or title. The Silo project uses `gaming_` filenames; the catastrophe workbook uses `workbook_` filenames and a separate Quarto build.

Issue titles start with `[infra]` or the primer's short name (directory name without `primer_`, with hyphens). Use `<type>/<issue#>-<slug>` for branches. Keep generated intermediates out of commits. Before a content migration, compare old and proposed material to establish the actual scope; inspect companion documents and configuration or ignore-file outliers as well as the primary source.

## Building

Run the command from the named directory (`cd <directory> && just <recipe>`). This table was checked against the current Justfiles and `_shared/common.just` on 10 October 2026. `html` and `pdf` are imported shared recipes; project-specific wrappers are shown where they perform additional work. Use `just --list` in the directory to inspect other recipes.

| Directory | Main HTML | Main PDF | Full or Additional Output |
|---|---|---|---|
| `primer_building_ai_agents` | `html` | `pdf` | `all-retained` adds `quick-html` for the companion reference; `docs` runs only `quick-html` |
| `primer_claude_code_alternative` | `html` | `pdf` | `all` |
| `primer_codex_for_claude_code_users` | `html` | `pdf` | `all` |
| `primer_comparative_religion` | `html` | `pdf` | `all` |
| `primer_complex_analysis` | `html` | `pdf` | `full` runs plots, both maths variants, and main HTML/PDF |
| `primer_containerization` | `html` | `pdf` | `all` |
| `primer_deep_learning` | `html` | `pdf` | `all` includes both maths variants |
| `primer_digital_signal_processing` | `html` | `pdf` | `full` runs plot generation/checks and `all`, including both maths variants |
| `primer_evaluation_loop` | `html` | `pdf` | `all` includes both maths variants |
| `primer_hermes_server` | `html` | `pdf` | `all` |
| `primer_military_structure` | `html` | `pdf` | `all` |
| `primer_numerical_analysis` | `html` | `pdf` | `full` runs plots, both maths variants, and main HTML/PDF |
| `primer_ohmyzsh` | `html` | `pdf` | `all` |
| `primer_openclaw` | `html` | `pdf` | `all` |
| `primer_pi_coding_agent` | `html` | `pdf` | `all` |
| `primer_political_systems` | `html` | `pdf` | `all` includes both maths variants |
| `primer_python_for_r_users` | `html` | `pdf` | `all` |
| `primer_research_local_llms` | `html` | `pdf` | `all` |
| `gaming_silo_rpg` | `silo-html` | `silo-pdf` | `silo-all` builds the index and four source documents |
| `workbook_catmodel_elt_documents` | `render-dev-container` | — | `render-full-container` renders the full Quarto package |

The root `Justfile` has selected project targets; use the directory recipes for complete project control. Root `html-dev` and `html-full` also run the workbook and may build PDFs through dependencies, so they are unsuitable for HTML-only sweeps. For those sweeps, run `html` per primer, `quick-html` for the Building AI companion, `html-variants` for the six opted-in maths primers, and `silo-html` for Silo.

Run `just readme` to generate the README catalogue and Recently Updated block, then `just readme-check` to verify them. Edit document titles, descriptions, links, and row order in the registry in `scripts/update_readme_recent.py`; update the relevant Justfile `DATE` after a substantive review. Do not edit generated README rows directly.

Use wrapper recipes such as `full` to chain shared targets; `just` does not override an imported recipe. Render plots through the Rocker container and commit the generation script with figure outputs. The Mermaid Lua filter and Puppeteer configuration live in `_shared/filters/`; generated PNGs remain project-local in `.build/mermaid`. Prefer Mermaid to ASCII diagrams where PDF font coverage is unreliable. Set DejaVu Sans Mono for code containing Greek, because the default monospaced font lacks those glyphs. With a leading body H1 and numbered `##` sections, pair `--number-sections` with `--shift-heading-level-by=-1` so sections number from 1.

Maths variants use shared `html-mathml`, `html-mathjax`, and `html-variants` recipes. Opt in through `--metadata mathvariants=true` in `HTML_EXTRA`; `all` then builds both variants using the main page's structural flags. The opted-in primers are complex analysis, deep learning, digital signal processing, evaluation loop, numerical analysis, and political systems. Complex analysis defaults to MathJax; the other five default to MathML. A project without the opt-in cannot run `html-variants`.

## Render QA

Render affected outputs in containers. Confirm that each PDF exists, has a non-trivial size, and opens with extractable text; inspect representative pages when layout changes. Capture the XeLaTeX log and search for actual failures with `grep -E 'Error|Missing \$|Undefined control' <build-log>`. A generic warning search can miss these failures.

For Mermaid changes, first render a small subset that exercises every new syntax feature, then run the full build. Pandoc can exit successfully even when the Mermaid CLI leaves raw fences in HTML. Search the rendered document for `graph LR`, `graph TB`, `subgraph`, `stroke-dasharray`, and `{.mermaid}`; inspect matches in context because embedded scripts may contain similar text. Confirm that every expected diagram has a rendered `figure` or `img` and that figure counts match the source. Check links, heading IDs, and `git diff --check` before committing.

Before renumbering or removing headings, search prose for embedded section references. When planning diagram replacements, inspect `text` code blocks. Agree a notation contract before parallel writers change mathematical content. When checking Markdown H1s, exclude fenced code blocks: `#` inside a fence may be a shell comment.

| Review Task | Procedure |
|---|---|
| Content passes and visual QA | Follow the [review checklist](docs/review-checklist.md); use this guide's Render QA section as the single source for build checks. |
| Mathematical notation and writing | Follow the [maths and notation guide](docs/math-notation.md) for symbols, theorem format, and renderer policy. |

## Adding a Document

Until `just new-primer` arrives in #162, create the project directory and its `<dir>.md` source, with an H1 equal to `TITLE`. Add a thin Justfile defining `SOURCE_MD`, `PROJECT_DIR`, `TITLE`, `AUTHOR`, `DATE`, `HTML_EXTRA`, and `PDF_EXTRA`, then import `../_shared/common.just`. Add appropriate root Justfile targets, register the source and outputs in `scripts/update_readme_recent.py`, and run `just readme` to update the catalogue. Add an `area:` label to `.github/labels.json` if the new document introduces a category, and synchronise that repository label. Render and commit the source, Justfile, and required HTML/PDF outputs in the same PR. Follow the style guide for prose and headings.

## Dates

`AUTHOR` names the person. `DATE` in a Justfile is the date of the last substantive content review: the document owner updates it when facts or explanations are verified or revised. A spelling, heading-case, formatting, or other mechanical sweep does not bump it. Preserve month-only precision when the source supports only a month. Use prose dates such as `7 October 2026`; use ISO dates in README tables and machine-read fields. Do not add separate refresh stamps to document titles or H1s.

## Linting and CI

`just lint` is planned under #155; `just check` is planned under #157; the PR checks workflow is planned under #158. Until they exist, run the relevant render and manual QA steps above and report the exact commands in the PR.

## Third-Party Content

Do not republish third-party material without a licence record; see `NOTICE` for the current attributions and reuse boundaries. A prompt file retained as a reference must carry a reference-only header identifying its source and status. Link to the upstream work when reuse rights are unclear.

## Silo Reference Sheets

A PR that changes a Silo bible's content updates its companion reference sheet in the same PR; purely mechanical sweeps are exempt.

## Pull Request Workflow

Work issue-first and keep one issue per PR. Typos and single-line fixes may use a PR without a separate issue. Open the PR body with `Closes #N` for its issue. Per-primer PRs under a sweep issue use `Refs #N` for the sweep; only the owner-designated final PR uses `Closes #N` for it. Serialise work on a primer through #136, heading case, #141, and #138; avoid two open PRs on the same primer. A cross-primer sweep has one tracking issue with a per-primer checklist.

Use `<type>/<issue#>-<slug>` branches and never commit directly to `main`. `.github/labels.json` is the source of truth for one priority, one type, at least one area, and one effort label. Squash merge by default; explain a merge commit when preserving individual commits or a stacked chain matters. Check changed paths and generated outputs before opening the PR. Published pages link to Pages-excluded project instructions through GitHub blob URLs, because `_config.yml` excludes `CLAUDE.md`, `AGENTS.md`, `CONTRIBUTING.md`, and `docs/` from Pages.
