---
name: primer-handoff
description: Prepare an evidence-backed handoff or release note for primer work. Use when another harness, agent, or session will continue, review, or release the work.
compatibility: Requires Git state and the repository handoff template.
---

# Handoff or release

Resolve repository documents and recipes from the owning repository root;
resolve references bundled with this skill from the skill directory.

Use `docs/primer-workflow-skills.md` for routing and the shared decision
checklist. A handoff can occur at any bounded stage; it does not itself
authorise repair or release.

Read `docs/agent-collaboration.md`, `docs/primer-production-procedure.md`, and
the project contract. Recheck live Git state immediately before writing the
handoff. Use the portable template and include objective/issue, branch and
revision, dirty paths, scope and exclusions, decisions and evidence, changed
paths, exact validation results, remaining work, and blockers. Consume the
tracked brief and tracked audit, preserving their stable `route_id` and
`concept_id` values and recording the evidence revision and reviewer. Confirm
that the audit covers every brief row, uses only `verified`, `gap`,
`scope-reduced`, or `not-checked`, and gives a rationale for every
`scope-reduced` row.

Treat `gap` or `not-checked` on a primary or alternative route as a blocker.
Do not pass the content gate while such a row remains unresolved. A
reference-only route may remain outside the teaching spine when the brief says
so explicitly. Mechanical validation may establish shape and completeness, but
the handoff must report the human judgement that the evidence genuinely
teaches; render QA cannot supply that judgement or approve content depth.

Report separate content-gate and release-readiness decisions, each with its
status, evidence and revision, blockers, next action, and owner. A content pass
does not establish release readiness: assess output freshness, metadata,
required checks, review and render evidence separately. Mark missing or stale
evidence as unverified or blocking, as appropriate. Distinguish executed checks
from parsed examples, sampled visual checks, reported historical evidence, and
unavailable checks. Keep secrets, private transcripts, and hidden reasoning out.

For substantial or non-obvious primer work, include the verified commit map
described in the portable template in the handoff or PR. It explains change
history, not content quality; it sets no commit-count or merge-method quota.

For a PR, identify one primary issue on the first line, list related issues on
separate lines, state the milestone's completed and remaining work, and include
the review and render evidence. Merge or release only when the user-authorised
scope and repository definition of done are satisfied.
