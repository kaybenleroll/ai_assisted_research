---
name: primer-render-qa
description: Render and verify a primer's published HTML/PDF outputs and executable examples. Use after source or build changes when reproducible build and visual evidence are required.
compatibility: Requires the repository's pinned container runtime and project recipes.
---

# Render and verify

Resolve repository documents and recipes from the owning repository root;
resolve references bundled with this skill from the skill directory.

Use `maintenance/docs/primer-workflow-skills.md` for routing and the shared decision
checklist. Inspect existing committed outputs when in scope and distinguish
that evidence from a new build. A failed check does not authorise repair.

Read `maintenance/docs/primer-production-procedure.md`, `CONTRIBUTING.md`,
`maintenance/docs/review-checklist.md`, and the target project's `Justfile`. Use the
project-specific `full` or equivalent recipe when it generates figures or
maths variants; never replace a specialist recipe with a generic command that
silently omits outputs.

Render QA consumes the tracked brief/audit revision only to report provenance
and to detect missing or mismatched evidence artefacts. It may validate the
shape and completeness of their rows mechanically, but it must not decide
whether prose genuinely teaches a route or concept. In particular, a
successful build, executable example, rendered page, or visual inspection
cannot mark a teaching-depth row `verified`, clear a `gap` or `not-checked`, or
approve content depth. That judgement belongs to the human audit; report it as
unverified when the audit is absent, stale, incomplete, or unresolved.

If a build could overwrite tracked outputs outside the permitted write scope,
build an appropriate revision in isolation, preserving any relevant dirty
inputs, or stop and report the limitation. Identify which outputs were checked.

Record exact commands, image/runtime versions, and whether each example was
executed, parsed, or left illustrative. Run the applicable metadata, variant,
Mermaid, freshness, README, spelling, Markdown, prose, and link checks. Inspect
representative rasterised PDF pages: opening page, table, code, and figure or
equation. Check HTML structure, anchors, images, extracted text, and actual
render errors rather than relying on exit status or file existence. Keep these
output findings separate from the audit's human teaching-depth decision.

When a shared layout or pagination change can affect the whole document, widen
the visual sample beyond one page of each type. Inspect both sides of affected
page breaks, including where a figure may interrupt a code listing, sentence,
or equation. Check continuity across the boundary as well as the page layout.
Record the source and PDF revisions, page span, element, and inspection scope.
This is targeted sampling, not an exhaustive page-by-page review; record any
uninspected scope and its reason.

If a required runtime or container is unavailable, record it as unverified and
stop at the safe boundary. Do not install repository build dependencies on the
host, delete generated files, or publish merely because a render succeeded.
