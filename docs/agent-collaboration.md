# Agent Collaboration Notes

The project contract contains the rules that every coding-agent harness should
follow. This page gives the operational detail for switching between Claude
Code, Codex, Pi, and generic `AGENTS.md` readers.

## Choose a Checkout Model

Use one checkout for serial work. At each hand-off, record the current branch,
revision, dirty paths, intended scope, and validation results, then have the
next harness inspect those facts before editing.

Use one branch and worktree per writer for concurrent work:

```bash
git worktree add ../repo-claude -b agent/claude-task main
git worktree add ../repo-codex -b agent/codex-task main
```

Do not assign the same generated output, migration, or lock file to two
writers. Integrate in a third checkout or by an explicitly named owner, run the
repository checks there, and remove worktrees only after confirming their
branches are no longer needed.

## Portable Handoff Template

```text
# Handoff: <task>
- Objective and issue: <outcome and issue or URL>
- Repository state: <branch, revision, dirty paths, capture time>
- Scope and constraints: <owned paths, exclusions, stop conditions>
- Decisions and evidence: <decision and source path or URL>
- Changes: <paths and purpose>
- Validation: <exact command, directory, result>
- Remaining work and blockers: <specific next action or none>
```

Treat the note as a report, not as authority over live Git state. Recheck
branches, paths, diffs, and test results. Keep secrets and private session
transcripts out of it.

## Harness Smoke Test

When adding or changing a native adapter, use a disposable checkout and a
read-only task. Record the harness and version, working directory, discovered
entry files, contract sections it actually opened, selected task route, and
available permission/tool controls. Test at least a primer task, workbook
task, and Silo task. An unavailable harness is **unverified**, not a pass.

The static contract check verifies paths and structure only. It cannot prove
that a model followed an instruction, that a harness loaded a linked file, or
that permissions and sandboxing are equivalent.

## Repository discovery evidence

As of 6 November 2026, this repository uses `AGENTS.md` as its sole canonical
root instruction file. Record the Claude Code, Codex, and Pi versions with
every discovery smoke test because support and selection rules are
version- and configuration-dependent. Claude Code can discover `AGENTS.md`
directly when no higher-precedence `CLAUDE.md` applies, while Codex and Pi
have their own discovery chains. Native Claude Code rules, skills, hooks,
permissions, and Codex or Pi equivalents are not implied by the shared file.

A local session cannot establish Claude Code's default selection rule when
user settings explicitly request combined instruction loading. A valid smoke
test therefore records the harness version, working directory, relevant
settings, discovered files, and exact task. A file the model later opens is
not evidence that the harness discovered it automatically. Record unavailable
harnesses as unverified rather than as passes.
