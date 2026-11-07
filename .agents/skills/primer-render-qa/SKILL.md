---
name: primer-render-qa
description: Render and verify a primer's published HTML/PDF outputs and executable examples. Use after source or build changes when reproducible build and visual evidence are required.
compatibility: Requires the repository's pinned container runtime and project recipes.
---

# Render and verify

Resolve repository documents and recipes from the owning repository root;
resolve references bundled with this skill from the skill directory.

Use `docs/primer-workflow-skills.md` for routing and the shared decision
checklist. Inspect existing committed outputs when in scope and distinguish
that evidence from a new build. A failed check does not authorise repair.

Read `docs/primer-production-procedure.md`, `CONTRIBUTING.md`,
`docs/review-checklist.md`, and the target project's `Justfile`. Use the
project-specific `full` or equivalent recipe when it generates figures or
maths variants; never replace a specialist recipe with a generic command that
silently omits outputs.

If a build could overwrite tracked outputs outside the permitted write scope,
build an appropriate revision in isolation, preserving any relevant dirty
inputs, or stop and report the limitation. Identify which outputs were checked.

Record exact commands, image/runtime versions, and whether each example was
executed, parsed, or left illustrative. Run the applicable metadata, variant,
Mermaid, freshness, README, spelling, Markdown, prose, and link checks. Inspect
representative rasterised PDF pages: opening page, table, code, and figure or
equation. Check HTML structure, anchors, images, extracted text, and actual
render errors rather than relying on exit status or file existence.

If a required runtime or container is unavailable, record it as unverified and
stop at the safe boundary. Do not install repository build dependencies on the
host, delete generated files, or publish merely because a render succeeded.
