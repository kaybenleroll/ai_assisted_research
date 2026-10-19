# Contributing

## Setup

The host needs Git, `just`, and a container runtime (Podman preferred; Docker also works). Run `just setup` from the repository root to configure Git hooks, build the shared Pandoc image, and pull the R figure image. The command is safe to repeat. Set `IMAGE`, `ROCKER`, or the relevant runtime image variable in the environment to override an image. Install rendering libraries inside containers, never on the host.

| Role | Image and Pin | Override | Update |
|---|---|---|---|
| Pandoc renders | `localhost/primers-pandoc:latest`, built from `docker.io/pandoc/latex@sha256:bd7641edf35bb8fad1316bacdac15fcc15f4d8d4f89051da2edcace15a6366d8` | `IMAGE` | Verify the new base digest and Pandoc version, update `_shared/Dockerfile`, run `just setup`, and check sample renders. |
| R figures | `docker.io/rocker/tidyverse:4.5.1@sha256:e58774bc0b3e15dd67d4eef5b3f7b77b1fd01b9a85e1ff5ecdd376bb06f74acc` | `ROCKER` | Verify the new digest and R version, update `_shared/images.just`, run `just setup`, and check plot recipes. |
| README generation | `docker.io/library/python:3-slim@sha256:cfe2e24a75302a15934d37c2d86412893c0aa934dc3a97cbb439d04c01890ca9` | `PYTHON_IMAGE` | Verify the new digest, update `_shared/images.just`, then run `just readme-check`. |
| Executable-example Python | `localhost/primers-python-runtime:3.12.15`, built from `python:3.12.15-slim-bookworm@sha256:34386ef0cb081344d7ec1c103ba398e6e9f64e9ab3a1509accc92a4e24a07258` | `PYTHON_RUNTIME_IMAGE` | Review `_shared/runtime/python/requirements.lock`, verify the base digest and package releases, then run `just build-python-runtime probe-python-runtime`. |
| Executable-example CPU PyTorch | `localhost/primers-python-torch:2.14.1`, built on the executable-example Python image | `PYTHON_TORCH_IMAGE` | Review `_shared/runtime/python/requirements-pytorch.lock`, verify the PyTorch CPU wheel support, then run `just build-python-torch probe-python-torch`. |
| Executable-example R | `localhost/primers-r-runtime:4.5.3`, built from `rocker/r-ver:4.5.3@sha256:35394dcbf419ac29056848522006de3cd33c33191377abed182acaecd48eba37` and its P3M CRAN snapshot | `R_RUNTIME_IMAGE` | Review `_shared/runtime/r/`, the snapshot date, and the native torch lock, then run `just build-r-runtime probe-r-runtime`. |
| Executable-example Julia | `localhost/primers-julia-runtime:1.12.7`, built from the amd64 `julia:1.12.7-bookworm@sha256:83c49705e6702c8a6e674be67d3c57e489a50df3e50997c84da49b5594808563` image | `JULIA_RUNTIME_IMAGE` | Review `_shared/runtime/julia/Project.toml` and `Manifest.toml`, verify the base digest and package artifacts, then run `just build-julia-runtime probe-julia-runtime`. |
| Spelling lint | `localhost/primers-lint:1.51.1`, built from the same digest-pinned `PYTHON_IMAGE` and checksum-verified `typos` 1.51.1 | `LINT_IMAGE` | Verify the release asset digest in `_shared/Dockerfile.lint`, run `just build-lint-image`, then probe and run `just lint`. |
| Markdown structure lint | `docker.io/davidanson/markdownlint-cli2:v0.23.3` | `MDLINT_IMAGE` | Verify the new image tag, probe Pandoc syntax and Silo configuration, then run `just lint-md`. |
| Prose lint | `docker.io/jdkato/vale:v3.24.0` (observed digest `sha256:f51196961ed91e514047cd95d45ec8bc2ff8d54a285af29e56166b975a37e3bf`) | `VALE_IMAGE` | Verify the tag and digest, run `just lint-prose-test`, then run `just lint-prose` and review the advisory baseline. |
| Link checks | `docker.io/lycheeverse/lychee:0.23.0` (observed digest `sha256:3e6ba0031fdcb3e6b7a9c1a5947fd79d243194c05b7e814dd78548029540259c`) | `LYCHEE_IMAGE` | Verify the tag and digest, probe README and a built primer offline, then run `just lint-links`. |
| Workbook | `docker.io/rocker/tidyverse@sha256:c38f0fea583e3aa82d89d0038e5bb559a04fa813881031f61f6191e683954cf2` | `WORKBOOK_IMAGE_ID` | Follow the separate image process in `workbook_catmodel_elt_documents/render.env` and its Dockerfile. |

## Layout and Naming

Most documents live in `primer_<short>/` with a thin `Justfile`, one source Markdown file, and committed HTML and PDF. New sources use `<dir>.md`, retaining underscores; existing hyphenated filenames are frozen rather than renamed. The source H1 is the canonical title and must match the Justfile `TITLE`. Do not add refresh stamps to the H1 or title. The Silo project uses `gaming_` filenames; the catastrophe workbook uses `workbook_` filenames and a separate Quarto build.

Issue titles start with `[infra]` or the primer's short name (directory name without `primer_`, with hyphens). Use `<type>/<issue#>-<slug>` for branches. Keep generated intermediates out of commits. Before a content migration, compare old and proposed material to establish the actual scope; inspect companion documents and configuration or ignore-file outliers as well as the primary source.

## Building

The policy and architecture for selected runnable primer examples is documented in [docs/executable-examples.md](docs/executable-examples.md). Example execution is opt-in through per-primer manifests; ordinary fenced snippets remain illustrative unless explicitly listed.

Build and probe the shared Python example runtimes with `just build-python-runtimes`, `just probe-python-runtime`, and `just probe-python-torch`. These images are separate from the repository-check `PYTHON_IMAGE`, the Rocker figure image, and the catastrophe workbook image.

Build and probe the separate executable-example R runtime with `just build-r-runtime probe-r-runtime`. Its image tag defaults to `localhost/primers-r-runtime:4.5.3` and can be overridden with `R_RUNTIME_IMAGE`. The digest-pinned Rocker base supplies the explicit P3M CRAN snapshot; the MLverse CPU `torch` package and native payload are the documented exception. The existing `ROCKER` image and figure recipes remain unchanged.

The R runtime's last clean local build took 66 seconds on x86_64 and produced an image of 2,099,951,961 bytes. This is a measurement for planning, not a CI guarantee. Its direct package expectations are recorded in `_shared/runtime/r/packages.lock`, the CRAN snapshot date is in the Containerfile, and the CPU `torch` native payload is recorded in `_shared/runtime/r/native.lock`; the offline probe checks the R, package, and LibTorch versions.

Build and probe the separate executable-example Julia runtime with `just build-julia-runtime probe-julia-runtime`. Its image tag defaults to `localhost/primers-julia-runtime:1.12.7` and can be overridden with `JULIA_RUNTIME_IMAGE`. The amd64 digest-pinned official Julia image supplies Julia 1.12.7. The committed `Project.toml` and generated `Manifest.toml` pin the shared ForwardDiff and Zygote environment; package source and compiled artifacts are instantiated during the image build, so the probe itself runs without network access. The image is initially scoped to the automatic-differentiation examples; add numerical-analysis packages only when a selected example justifies them.

The Julia runtime's clean local build took 75 seconds and produced an image of 1,315,152,893 bytes on x86_64. This is a measurement for planning, not a CI guarantee. A runtime update must change the Julia base digest or committed project/manifest as one reviewed set, rebuild from a clean cache, rerun the offline probe, and check the package manifest against the selected Julia minor version. Julia package manifests pin package trees and versions, but platform-specific binary artifacts still require a probe on each supported architecture.

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
| `gaming_silo_rpg` | `silo-html` | `silo-pdf` | `silo-all` builds the index, four source documents, and four reference sheets |
| `workbook_catmodel_elt_documents` | `render-dev-container` | — | `render-full-container` renders the full Quarto package |

The root `Justfile` has selected project targets; use the directory recipes for complete project control. Root `html-dev` and `html-full` also run the workbook and may build PDFs through dependencies, so they are unsuitable for HTML-only sweeps. For those sweeps, run `html` per primer, `quick-html` for the Building AI companion, `html-variants` for the six opted-in maths primers, and `silo-html` for Silo.

Run `just readme` to generate the README catalogue and update block, then `just readme-check` to verify them. Edit document titles, descriptions, links, and row order in the registry in `scripts/update_readme_recent.py`; update the relevant Justfile `DATE` after a substantive review. Do not edit generated README rows directly.

Use wrapper recipes such as `full` to chain shared targets; `just` does not override an imported recipe. Render plots through the Rocker container and commit the generation script with figure outputs. The Mermaid Lua filter and Puppeteer configuration live in `_shared/filters/`; generated PNGs remain project-local in `.build/mermaid`. Prefer Mermaid to ASCII diagrams where PDF font coverage is unreliable. Set DejaVu Sans Mono for code containing Greek, because the default monospaced font lacks those glyphs. With a leading body H1 and numbered `##` sections, pair `--number-sections` with `--shift-heading-level-by=-1` so sections number from 1.

Maths variants use shared `html-mathml`, `html-mathjax`, and `html-variants` recipes. Opt in through `--metadata mathvariants=true` in `HTML_EXTRA`; `all` then builds both variants using the main page's structural flags. The opted-in primers are complex analysis, deep learning, digital signal processing, evaluation loop, information theory, numerical analysis, and political systems. All seven default to MathJax. A project without the opt-in cannot run `html-variants`. `doc_template.html` runs the MathJax `boldsymbol` extension, vendored in `_shared/vendor/mathjax/boldsymbol.js`, because an embedded bundle cannot load it. When Pandoc embeds a new MathJax version, replace the vendored file with `input/tex/extensions/boldsymbol.js` from `https://cdn.jsdelivr.net/npm/mathjax@<version>/` and re-render the maths primers; no check enforces the match, and MathJax's runtime `checkVersion` warns in the browser console on drift.

## Render QA

Render affected outputs in containers. Confirm that each PDF exists, has a non-trivial size, and opens with extractable text; inspect representative pages when layout changes. Capture the XeLaTeX log and search for actual failures with `grep -E 'Error|Missing \$|Undefined control' <build-log>`. A generic warning search can miss these failures.

For Mermaid changes, first render a small subset that exercises every new syntax feature, then run the full build. Pandoc can exit successfully even when the Mermaid CLI leaves raw fences in HTML. Search the rendered document for `graph LR`, `graph TB`, `subgraph`, `stroke-dasharray`, and `{.mermaid}`; inspect matches in context because embedded scripts may contain similar text. Confirm that every expected diagram has a rendered `figure` or `img` and that figure counts match the source. Check links, heading IDs, and `git diff --check` before committing.

Before renumbering or removing headings, search prose for embedded section references. When planning diagram replacements, inspect `text` code blocks. Agree a notation contract before parallel writers change mathematical content. When checking Markdown H1s, exclude fenced code blocks: `#` inside a fence may be a shell comment.

| Review Task | Procedure |
|---|---|
| Content passes and visual QA | Follow the [review checklist](docs/review-checklist.md); use this guide's Render QA section as the single source for build checks. |
| Mathematical notation and writing | Follow the [maths and notation guide](docs/math-notation.md) for symbols, theorem format, and renderer policy. |

## Adding a Document

Run `just new-primer <short> "<Full Title>"` from the repository root to create `primer_<short>/Justfile` and `primer_<short>/primer_<short>.md`. The recipe prints the remaining registration and publication steps. Replace the scaffold's AUTHOR placeholder and update DATE after a substantive review, write the primer under [STYLE_GUIDE.md](STYLE_GUIDE.md), add top-level build targets, register its source and outputs in `scripts/update_readme_recent.py`, and run `just readme`. Add and synchronise an `area:` label in `.github/labels.json` if this introduces a new class, and add the directory to the document-class list in [CLAUDE.md](CLAUDE.md). Render in containers and commit the source, Justfile, and required HTML/PDF outputs together.

## Dates

`AUTHOR` names the person. `DATE` in a Justfile is the date of the last substantive content review: the document owner updates it when facts or explanations are verified or revised. A spelling, heading-case, formatting, or other mechanical sweep does not bump it. Preserve month-only precision when the source supports only a month. Use prose dates such as `7 October 2026`; use ISO dates in README tables and machine-read fields. Do not add separate refresh stamps to document titles or H1s.

## Linting and CI

`just build-lint-image` builds the spelling checker from the digest-pinned Python image and the checksum-verified `typos` 1.51.1 release. `just lint` runs spelling, markdownlint-cli2, and Vale House prose rules on tracked primer Markdown, the root README, and Silo Markdown; it also runs offline link checks on tracked built HTML and README. `just lint-spell <path.md>`, `just lint-md <path.md>`, `just lint-prose <path.md>`, and `just lint-links <path.html>` run one checker, with no path selecting the full scope. `just lint-prose-test` checks every House rule's pass and fail fixtures in a container. `just lint-changed` checks Markdown added, modified, or renamed since `${BASE_REF:-origin/main}` using a three-dot diff and checks the full offline link baseline for CI. Markdown structure and prose lint exclude the reference-only `primer_political_systems/complete_prompt.md`; spelling still checks it. All three exclude the former `primer_building_ai_agents/README.md`. Set `OCI=podman` or `OCI=docker` to choose a container command; the default prefers Podman. Set `LINT_IMAGE`, `MDLINT_IMAGE`, `VALE_IMAGE`, or `LYCHEE_IMAGE` to use a different lint image.

`just lint-links` uses the tagged lychee container and `lychee.toml` with `--offline` and fragment checks. It reads each committed HTML file in place, so fragment IDs come from Pandoc's published output. The scope is built primer, Silo, and workbook HTML plus the root README; `doc_template.html` is a template. Each finding is `ENFORCED` for a path in `lint/enforced-links.txt` and `ADVISORY` otherwise. The manifest contains paths that were clean when the gate was added; stale or duplicate entries fail the command. Add newly clean published HTML after review. Data URIs and external URLs are excluded in offline mode by lychee, while `.scratch/` and the retired article HTML tree are excluded by configuration. `just lint-links-online` checks the published Markdown sources and README with network access and always reports rather than gating. The independent `links.yml` workflow runs that report weekly or on manual dispatch and uploads it as an artefact; it never files issues. Review the report before scheduling content fixes.

Every finding is printed with `ENFORCED` or `ADVISORY` and a source line. `lint/enforced-spelling.txt` lists zero-finding documents whose future findings fail the command. A manifest entry must be a current repository-relative in-scope path; stale entries are errors. Silo files remain advisory until #166, including the two zero-finding Silo files recorded in the initial manifest. Each sweep PR adds its cleared document to the manifest. The summary reports checked files, both finding counts, and the number of `<!-- typos: ignore-line -->` markers. Review those markers manually.

markdownlint-cli2 uses `.markdownlint-cli2.yaml` with the selected structure, markup and accessibility rules; `gaming_silo_rpg/.markdownlint-cli2.yaml` permits that class's asterisk bullets. MD040 (untagged code fences) and MD045 (images without alt text) fail for every markdownlint-scanned file. MD001 (heading increments), MD025 (one H1) and MD034 (bare URLs) fail only for primer paths in `lint/enforced-structure.txt`; other findings remain advisory. Add a primer to that manifest only after its #136 structure row is merged and all three rules are clear. Entries must be current repository-relative primer Markdown paths; stale or duplicate entries fail the command. The report gives source lines and per-file and per-rule baseline counts. Rules MD013, MD033, MD041, MD012, MD022, MD031, MD032, MD060 and MD007 remain disabled to avoid whitespace churn or changes that do not affect rendered output. An MD036 advisory on a multi-language code label usually means the bold label lacks its trailing colon (see M9 in the style guide).

Vale reads `.vale.ini` and the repository's House rules in `.vale/styles/House/`; no external style packages are loaded. `House.Hedging` is enforced everywhere prose lint runs, while `House.USDate` is enforced for `lint/enforced-spelling.txt` entries and `House.HeadingCase` plus `House.HeadingMinor` for primers listed in `lint/enforced-headings.txt`. The second heading rule explicitly checks S1's 20 minor words; both heading checks require human review for proper names and code identifiers. Add a primer to the heading manifest only after its heading sweep has cleared both rules. All other House findings remain advisory. `lint/vale-usdate-existing.txt` records one pre-existing US-date finding in an otherwise spelling-enforced primer; it is advisory until #141 removes it. New date findings still fail, and a stale or duplicated exception fails the reporter. The two-primer `House.FillerCluster` pilot covers evaluation loop and numerical analysis; `House.WeaselWords` runs only on the three contested-subject primers. The separate density check uses the single filler list in `House/Filler.yml` and reports rates above 1.0 per 1,000 prose words as advisory. Vale skips Markdown code; explicit token and block ignores cover inline and display maths. `House.LogicalPunctuation` requires human review for complete quoted sentences.

`_typos.toml` uses `en-gb` and ignores fenced code, inline code, maths, Markdown link targets, and explicitly marked lines because their spelling may be fixed by syntax or source material. The patterns cover ordinary Markdown forms; reviewers must still judge copied quotations, proper names, and unusual markup. An empty `[default.extend-words]` is intentional at the initial baseline: add an exception only for a verified proper name, standard, API, or paper title, with a reason comment. Do not exempt a technical concept merely because a source uses US spelling. The spelling scan does not change files, and advisory findings remain visible until the relevant sweep. Run the render and manual QA steps above where the PR changes published output.

### Checks

Run `just check` from the repository root. It uses the digest-pinned Python image from `_shared/images.just`, Python's standard library in isolated mode, and the `OCI` runtime setting. The default runtime is Podman when installed, otherwise Docker. The freshness check reads full Git history, so a shallow checkout is insufficient. Each check also has its own recipe:

| Recipe | What it verifies | Negative test on a disposable copy |
|---|---|---|
| `check-meta` | Every built Markdown source has a fence-aware H1 matching its Justfile or per-recipe title; author is a name or team, and review date has day or month precision. Known title differences must have a reason in `lint/check-meta-known.txt`. | Change one `TITLE` word in a primer Justfile, then run `just check-meta`. |
| `check-variants` | Each maths toggle has both variants and the Justfile opt-in; variants require maths outside code fences and inline code. | Remove one `.mathml.html` file, then run `just check-variants`. |
| `check-mermaid` | Published HTML has no raw Mermaid and has one filter-produced image for each source Mermaid fence. The filter's image caption, carried into the HTML accessibility label, identifies its images without counting plots. | Add `graph LR` to an HTML text node, then run `just check-mermaid`. |
| `check-fresh` | Each committed HTML and PDF output was last changed at or after its source in Git ancestry. The Building AI quick reference has HTML only. | Commit a one-word source edit without rendering, then run `just check-fresh`. |
| `check-readme` | Generated README tables match the registry and review dates. | Change one README table cell by hand, then run `just check-readme`. |

For negative tests, create a throwaway branch or copy under `.scratch/`, make only the named change, record the failed recipe and its message, and discard the disposable checkout. Do not run those mutations against the working branch. An empty known-mismatch file means there are no current exemptions; each future entry must use `source/path.md | reason`.

## Third-Party Content

Do not republish third-party material without a licence record; see `NOTICE` for the current attributions and reuse boundaries. A prompt file retained as a reference must carry a reference-only header identifying its source and status. Link to the upstream work when reuse rights are unclear.

## Silo Reference Sheets

A PR that changes a Silo bible's content updates its companion reference sheet in the same PR; purely mechanical sweeps are exempt. See the [Silo RPG README](gaming_silo_rpg/README.md) for the document-class conventions.

## Pull Request Workflow

Work issue-first and keep one issue per PR. Typos and single-line fixes may use a PR without a separate issue. Start the PR body with `Closes #N` for its issue; `Fixes #N` and `Resolves #N` are also accepted. Per-primer PRs under a sweep issue use `Refs #N` for the sweep; only the owner-designated final PR uses `Closes #N` for it. Cross-repository references such as `Closes owner/repo#N` are accepted. For a typo or single-line fix without an issue, start the body with `No-issue: <non-empty reason>`, for example `No-issue: typo in README`. The first non-blank line is checked on PR opening, editing, synchronisation, and reopening. Serialise work on a primer through #136, heading case, #141, and #138; avoid two open PRs on the same primer. A cross-primer sweep has one tracking issue with a per-primer checklist.

The PR workflow reports separate `checks` and `pr-body` statuses. `checks` builds the lint image, runs `just lint-changed` against the base branch, and runs `just check` with Docker. `pr-body` checks the opening reference or no-issue reason. The workflow does not render documents or check online links. Repository owners must require both statuses on `main` in Settings, Rules; the workflow cannot set that protection itself.

Use `<type>/<issue#>-<slug>` branches and never commit directly to `main`. `.github/labels.json` is the source of truth for one priority, one type, at least one area, and one effort label. Squash merge by default; explain a merge commit when preserving individual commits or a stacked chain matters. Check changed paths and generated outputs before opening the PR. Published pages link to Pages-excluded project instructions through GitHub blob URLs, because `_config.yml` excludes `CLAUDE.md`, `AGENTS.md`, `CONTRIBUTING.md`, and `docs/` from Pages.
