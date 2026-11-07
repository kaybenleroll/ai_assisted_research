---
name: primer-audit
description: Audit a primer after drafting or substantive revision. Use for whole-document coverage, technical claims, explanatory depth, structure, examples, sources, outputs, and residual uncertainty.
compatibility: Requires the repository review checklist and an auditable working tree.
---

# Audit a primer

Use `docs/primer-workflow-skills.md` for routing and the shared decision
checklist. Report findings and evidence within scope; a failed check does not
authorise repair.

Read `docs/primer-production-procedure.md`,
`docs/templates/primer-audit.md`, `docs/review-checklist.md`, and
`STYLE_GUIDE.md`. Record the reviewed commit, not only a branch name.

Read the complete source and perform a whole-document inventory against the
brief. Check coverage, technical claims and calculations, sources and
freshness, prerequisites and explanatory
depth, dependency order and section fragmentation, examples and limitations,
figures/tables/equations/accessibility, and committed outputs.

Then perform risk-selected technical verification and sampling: opening
orientation, difficult formal passage, worked example, practical case, and
representative rendered pages.
Record what was inventoried, independently verified or sampled, with exact
locations and limits; an inventory is not verification of every claim.
For code, map published snippets to tests or state that they are illustrative;
check fixtures, dependencies, ordering conventions, and expected results.
Reconcile earlier audits against the reviewed commit. Record verified,
unresolved, stale, and not-checked evidence separately.

Do not turn the audit into a score, word quota, or heading quota. Record false
positives, missed issues, reviewer effort, stopping boundaries, and issue-linked
follow-up work. A clean build or fresh output is not evidence that the content
is correct.
