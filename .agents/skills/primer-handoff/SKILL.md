---
name: primer-handoff
description: Prepare an evidence-backed handoff or release note for primer work. Use when another harness, agent, or session will continue, review, or release the work.
compatibility: Requires Git state and the repository handoff template.
---

# Handoff or release

Read `docs/agent-collaboration.md`, `docs/primer-production-procedure.md`, and
the project contract. Recheck live Git state immediately before writing the
handoff. Use the portable template and include objective/issue, branch and
revision, dirty paths, scope and exclusions, decisions and evidence, changed
paths, exact validation results, remaining work, and blockers.

Distinguish executed checks from parsed examples, sampled visual checks,
reported historical evidence, and unavailable checks. State the next action
and its owner. Preserve secrets, private transcripts, and hidden reasoning.

For a PR, identify one primary issue on the first line, list related issues on
separate lines, state the milestone's completed and remaining work, and include
the review and render evidence. Merge or release only when the user-authorised
scope and repository definition of done are satisfied.
