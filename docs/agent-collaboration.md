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

Before adding or changing a native adapter, use a disposable checkout and
read-only tasks. Test at least a primer task, workbook task, and Silo task.
For skills, record separately:

- Startup catalogue discovery: whether each skill appears before a task or
  manual file read, and what evidence the harness exposes.
- Explicit activation: whether a named skill can be invoked and its
  instructions are loaded.
- Model-selected activation: whether an unprompted skill choice occurs for a
  suitable task and what evidence shows it was loaded.
- Manual fallback: whether opening the linked `SKILL.md` and following its
  instructions works when native discovery or activation is unavailable.

Record the harness and version, relevant settings, working directory, results
from both the repository root and a nested directory, discovered entry files,
contract sections actually opened, exact tasks and routes, permission/tool
controls, and limitations. A file opened later does not prove startup
discovery; a catalogue entry alone does not prove activation. An unavailable
harness or unsupported observation is **unverified**, not a pass. Use this
evidence to decide whether a separate adapter is needed.

The static contract check verifies paths and structure only. It cannot prove
that a model followed an instruction, that a harness loaded a linked file, or
that permissions and sandboxing are equivalent.

## Cross-Harness Skill Evidence

The following post-adapter smoke-test observations are dated 7 November 2026. Discovery covered `primer-plan`, `primer-audit`, `primer-render-qa`, and `primer-handoff` at the repository root and a nested directory. The precise nested directory, full prompts, commands, and settings were not recorded in this summary, so the observations are not a complete reproduction recipe.

| Harness | Discovery | Explicit activation | Automatic selection |
|---|---|---|---|
| Claude Code 2.1.319 | Pass: all four skills at root and nested directory. | `/primer-plan` reached the skill workflow, but behavioural completion was inconclusive: the run expanded into tools and subagent work and was stopped. | Unverified. |
| Codex 0.166.0 | Pass: all four skills at root and nested directory. | Pass: `primer-plan` activation identified the canonical `.agents/skills/primer-plan/SKILL.md` and two instructions; the exact prompt and instruction excerpts are not recorded here. | Pass: `primer-plan` was selected automatically for a suitable task. |
| Pi 0.99.2 | Pass: all four skills at root and nested directory. | Pass for native loading and explicit activation; the configured `llamacpp-local` model connection failed before a response, so behavioural completion is unverified. | Unverified. |

For manual fallback, open the relevant canonical `.agents/skills/<name>/SKILL.md` and follow it with the project contract. This remains available independently of native discovery and activation; these observations do not establish a separate manual-fallback behavioural test.

## Claude Primer Skill Adapter

Claude Code 2.1.319 failed to discover the four canonical skills under `.agents/skills/` in the reported smoke test; Pi and Codex discovered them. The tracked `.claude/skills/` directory supplies the following relative directory symlinks:

| Claude entry | Relative target |
|---|---|
| `primer-plan` | `../../.agents/skills/primer-plan` |
| `primer-audit` | `../../.agents/skills/primer-audit` |
| `primer-render-qa` | `../../.agents/skills/primer-render-qa` |
| `primer-handoff` | `../../.agents/skills/primer-handoff` |

Edit the canonical `.agents/skills/<name>/SKILL.md`, not a copied adapter. The links require a checkout and filesystem that preserve symlinks; otherwise, open the canonical files manually. Static validation checks the link paths and targets, not Claude's discovery or activation. Test startup discovery, explicit activation, and model-selected activation separately as described above; the earlier failure does not establish that this adapter works in every runtime or configuration.

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
