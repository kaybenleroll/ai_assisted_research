# Cross-harness skill behaviour evidence — issue #380

## Objective and boundary

This record tests the four portable primer skills from the repository root and
the nested `primer_fluid_mechanics/` directory:

- `primer-plan`
- `primer-audit`
- `primer-render-qa`
- `primer-handoff`

It distinguishes startup discovery, explicit activation, model-selected
activation, and manual fallback. It tests behaviour, not harness equivalence,
content quality, provider quality, or static link validity. No skill, adapter,
CI, provider, or primer content was changed.

The evidence was collected on 10 November 2026 from branch
`infra/380-cross-harness-skill-evidence`, based on `cf58e5d3daca01818f79f0a43eb1a200a433c640`
(`origin/main`). The worktree was clean before testing and remained clean until
this record was added.

## Harness and environment

| Harness | Version probe | Controls | Current result |
|---|---|---|---|
| Codex | `codex --version` → `codex-cli 0.167.0` | `-a never -s read-only exec --ephemeral --json`; root and nested working directories | Executed successfully; results below |
| Claude Code | `claude --version` → `2.1.322 (Claude Code)` | Installation/version probe only | Behaviour unverified: invoking the provider would transmit prompts and repository context, and the runtime rejected that call without a more specific authorisation |
| Pi | `pi --version` → `1.5.0` | Installation/version probe only | Behaviour unverified: no provider invocation was attempted |

The command probes establish installation and version only. They do not prove
discovery or activation. Earlier repository observations for Claude Code 2.1.319
and Pi 0.99.2 are retained as historical evidence, not substituted for this
current-version run.

## Codex results

The startup, explicit-activation, and model-selection probes covered all four
skills in both the repository root and `primer_fluid_mechanics/`. Manual
fallback was separately executed only for `primer-plan`:

| Skill | Startup discovery | Explicit activation | Model-selected activation | Manual fallback |
|---|---|---|---|---|
| `primer-plan` | pass | pass | pass | pass |
| `primer-audit` | pass | pass | pass | unverified |
| `primer-render-qa` | pass | pass | pass | unverified |
| `primer-handoff` | pass | pass | pass | unverified |

### Startup discovery

Command pattern:

```text
codex -a never -s read-only exec --ephemeral --json -C <directory> <bounded prompt>
```

Before opening a repository file, the Codex startup context exposed `AGENTS.md`
and all four skill names in both working directories. The nested test therefore
supports discovery from `primer_fluid_mechanics/`, while the root test supports
discovery from the repository root. A catalogue entry was counted only as
discovery; it was not counted as activation by itself.

### Explicit activation

Each skill was named explicitly using its `$primer-*` name in a fresh,
read-only, ephemeral Codex invocation in both directories. The response
identified the canonical file under `.agents/skills/<name>/SKILL.md` and
reported a skill-specific stopping rule. Representative observed rules were:

- `primer-plan`: stop at the agreed plan unless drafting is authorised.
- `primer-audit`: a failed check does not authorise repair.
- `primer-render-qa`: stop and report if a build could overwrite outputs outside
  the permitted scope.
- `primer-handoff`: a handoff does not itself authorise repair or release.

The explicit runs did not create or edit files, delegate, use network tools, or
perform the underlying primer tasks. One nested `primer-audit` run emitted a
transient model-refresh timeout before completing the bounded file-read probe;
the activation result still completed and is recorded with that limitation.

### Model-selected activation

For each skill, a suitable task was presented without naming a skill or path:
planning a new primer, auditing an existing primer, verifying rendered outputs,
or preparing a bounded handoff. Codex selected the corresponding skill and
reported its canonical path in both directories. These were selection probes,
not full task executions, and therefore do not prove that a longer task would
complete correctly.

### Manual fallback

The fallback probe instructed Codex not to invoke a native skill and to open
`.agents/skills/primer-plan/SKILL.md` directly. It confirmed the skill name and
stopping rule from the repository root. From the nested directory, the first
relative path was correctly absent; locating the repository-root canonical path
and opening it then succeeded. This demonstrates the documented manual route
for `primer-plan`, including the important requirement to resolve
repository-owned files from the repository root. Manual fallback for the other
three skills was not separately executed and remains unverified; the result is
not generalised from one skill to all four. It does not demonstrate native
discovery failure.

## Claude Code and Pi

The local binaries are present and version probes succeeded. No current-version
behavioural status is claimed for either harness:

| Harness | Discovery | Explicit activation | Model-selected activation | Manual fallback |
|---|---|---|---|---|
| Claude Code 2.1.322 | unverified | unverified | unverified | unverified |
| Pi 1.5.0 | unverified | unverified | unverified | unverified |

This is an environmental boundary, not a pass. The runtime rejected a Claude
Code provider invocation because it could transmit repository context to an
external provider without a more specific authorisation. Pi was not invoked
because no provider call had been authorised. To resolve these rows, run the
same bounded probes in a session where the user has explicitly authorised the
target provider and where the required provider/model is available. Do not
copy private transcripts, credentials, or hidden reasoning into this record.

## Static checks and limitations

Static contract checks can confirm paths, symlinks, and structure but cannot
prove runtime discovery, activation, model selection, or equivalent permissions.
The existing repository guidance correctly treats those as separate claims.
This record also does not test workbook or Silo tasks, benchmark harnesses, or
live third-party providers in ordinary CI; those are outside issue #380's
skill-specific evidence boundary.

The evidence supports the following conclusion:

1. Codex 0.167.0 has current, reproducible evidence for all four behavioural
   dimensions at repository root and nested-primer scope.
2. Claude Code 2.1.322 and Pi 1.5.0 are installed, but their current behaviour
   remains unverified and must not be represented as equivalent to Codex.
3. The repository's static checks and existing historical observations remain
   useful context, but neither substitutes for nor upgrades the unverified
   Claude/Pi rows.

## Reproduction and next action

Re-run the bounded commands from a disposable checkout with the exact harness
version, working directory, settings, permissions, and prompt recorded. The
next owner is the maintainer with authority to permit Claude Code and Pi
provider calls. Until then, the Claude/Pi rows remain unverified rather than
blocking the Codex evidence record with an unsupported claim.
