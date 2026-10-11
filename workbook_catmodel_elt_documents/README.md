# CAT Model ELT Workbook

This Quarto workbook documents and implements a catastrophe event-loss-table (ELT) modelling workflow in R and Python. It is a workbook with executable analysis, with its own sources, deterministic runtime settings, render scripts, and committed HTML outputs, separate from the Pandoc document build system.

The three Quarto source titles still use the word "Primer". Renaming those titles requires a workbook re-render and remains a follow-up; they are unchanged here.

## Files and Outputs

- `workbook_elt.qmd`: main workbook, covering the ELT pipeline and its modelling checks.
- `workbook_quickstart.qmd`: operational quickstart.
- `workbook_executable_index.qmd`: index of runnable scripts and render targets.
- `Dockerfile`: builds the workbook's container image.
- `Justfile`: defines image and render recipes.
- `render.env`: sets simulation counts, random seeds, output directory, and the pinned base image.
- `scripts/`: contains the workbook render scripts.
- `outputs/`: contains the committed HTML documents.

## Style Applicability

Workbook prose follows the style guide's language rules, including UK English. Code follows the idioms of its language, and factual claims follow the guide's evidence and source rules. The workbook's Quarto system governs its structure and heading mechanics; the guide's workbook row does not apply the document-structure rules or general markup rules beyond the specified code rules. The Pandoc-specific flags, heading shifts, and shared Mermaid filter do not apply here. The repository README generator does read this workbook's `DATE` from its `Justfile` for the Recently Updated catalogue.

## Deterministic Runtime Configuration

The runtime controls are in `render.env`:

- `DEV_N_SIMS` and `FULL_N_SIMS` set the simulation counts.
- `SEED_R` and `SEED_PY` set the R and Python random seeds.
- `OUTPUT_DIR` sets the output directory.
- `WORKBOOK_IMAGE_ID` pins the base image to `docker.io/rocker/tidyverse@sha256:c38f0fea583e3aa82d89d0038e5bb559a04fa813881031f61f6191e683954cf2`.

The same base-image digest is pinned in `Dockerfile` and `render.env`. The `DATE` variable in `Justfile` records the last substantive review and is read by the repository README generator.

## Build and Render

Build the local image from `Dockerfile`, then run either the development or full container render:

```bash
just image-build
just render-dev-container
just render-full-container
```

`mcooney/workbook_catmodel_elt_documents:latest` is the locally built image tag; it is not pulled as a prebuilt image from a registry. On a fresh machine, run `just image-build` before rendering. If the pinned base image cannot be pulled, the image cannot be built and the workbook cannot be rendered. The workbook render was recorded as environment-blocked in issue #134 when its container image was unavailable locally.

If Quarto and the required dependencies are already installed locally, the existing non-container recipes remain available:

```bash
just render-dev
just render-full
```

## Known Output Issue

As of October 2026, each committed HTML output contains a math-renderer toggle (`math-mode-toggle`) that links to `.mathml.html` and `.mathjax.html` variants that are not committed for this workbook. The shared template fix in #145 applies to Pandoc documents; the workbook outputs retain the toggle until they can be re-rendered.
