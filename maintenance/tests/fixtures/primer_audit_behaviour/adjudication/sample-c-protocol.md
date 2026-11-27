# Sample C independent review protocol

This is an unexecuted protocol, not evidence that isolation, catalogue discovery,
activation, event capture, or recovery works. It supports #496. Use two fresh
Codex CLI sessions, no delegation, one unnamed-guidance review and one manually
directed review. This is a small behavioural probe, not a reliability estimate
or a comparison powered to detect a difference. If restricted egress cannot be
established, the explicitly non-blind fallback below may be run; do not call it
blind or claim that filesystem isolation prevents access through the network.

## Pin and isolate

Record the full fixture commit, clean status, CLI version, selected model and
effort, effective configuration and hashes below before either run. The fixture
files are `sample-c/PROMPT.md`, `sample-c/brief.md`, and `sample-c/primer.md`.
The adjudication key is a separate file and must remain outside both reviewer
environments. At preparation their SHA-256 hashes are:

| Input | SHA-256 |
|---|---|
| `PROMPT.md` | `a1ef339f7e8e0023dcfe48c35c6347e762f034026ed0c69b356e1295c9901b4b` |
| `brief.md` | `11777ae8eba71d90278f36e81386aeff90b04f6f6cd42445c3d0ba638e650b27` |
| `primer.md` | `1c4175ed83cc7189e76c9f7acbaed9b51e2d8dbc36235f4c9eb8d7e707d061f6` |
| `adjudication/sample-c-key.md` | `a9b94c77d5a51a6240f3ba8c89b27bf40f7e3ccd7e79bc765775ecd96194f0c7` |
| `.agents/skills/primer-audit/SKILL.md` at base `655fda2631a1875b5ea6ed72e0b2f3fc2a271082` | `8b0744aff0d49efead38f6bac7b3f93b0e660988cec95db28ae361d07f32d3f5` |

Build two separate disposable environments from an explicit allowlist: the
three fixture files and the guidance and skill files needed for the intended
catalogue, with the same paths and bytes in both. Include all resources those
files actually reference if needed; inspect them first for answer leakage.
Do not mount the repository, key, other review output, prior transcripts, or
operator scratch directory. Use an OS/container boundary that denies reads
outside the allowlist; a read-only working tree or an instruction to avoid the
key does not suffice. Provide only the minimum runtime and authentication needed
for the CLI, without copying session history. Restrict network access to what
the review runtime requires and prevent access to repository hosts or local
services that could expose the key. Do not store credentials in evidence.

If restricted egress is unavailable, retain the filesystem boundary and its
canaries, and record the shared network and the key's public availability as
uncontrolled access paths. The fallback is a non-blind trial even if no key
access appears in the observable events. Record the failed or unimplemented
network control and do not infer key exclusion from a lack of observed reads.
Use the same fallback for both reviewers. This does not establish the isolated
trial originally designed here.

Before running the model, from each actual reviewer boundary, attempt to read
the key's host path and a known host-only sentinel and confirm both fail; also
list the environment's mounted paths and confirm the three inputs are readable
with matching hashes. Record the commands, exit status and non-sensitive output.
Confirm that the intended native skill catalogue exposes `primer-audit` in
both environments, using an observed catalogue or session event; merely copying
`SKILL.md` is not catalogue evidence. If the environment cannot support this
control, catalogue availability is unverified; still distinguish observed file
reads from native activation. Do not disclose the
key or its contents to a reviewer, including in a prompt or accessible file.

## Execute and record

Use the same pinned model, effort, guidance, sandbox and starting files for both
runs. Invoke each as a new CLI process, with JSON event output captured to a
private operator-only file and a separate final-message file. For example,
where `REVIEW_ROOT`, `PROMPT_FILE`, `EVENTS` and `FINAL` refer to paths in the
isolated runtime and its private output channel:

```sh
codex exec --ephemeral --skip-git-repo-check --sandbox read-only \
  --model "$REVIEW_MODEL" -c "model_reasoning_effort=\"$REVIEW_EFFORT\"" \
  --cd "$REVIEW_ROOT" --json --output-last-message "$FINAL" - < "$PROMPT_FILE" > "$EVENTS"
```

Check the CLI exit status directly, retain stderr separately, and record the
actual command and effective values without credentials. The operator must
verify that the output paths are writable but are not readable by the other
reviewer. Test that JSONL is parseable and record event types and relevant
observed instruction/skill and file-read events, where exposed. This command is
an example, not a claim that its sandbox enforces the isolation above, that the
catalogue is available, or that JSONL exposes model payloads or native activation.
Do not infer unobserved events from a final response.

Give each reviewer the same task: `Complete PROMPT.md in the current directory.
Inspect any relevant guidance you independently select. Report files and
guidance consulted, actual actions and limitations. Do not delegate.` For the
second run append: `Read and apply .agents/skills/primer-audit/SKILL.md within
the fixture scope.` Adjust paths only to match the controlled layout and record
the exact delivered prompts. This second run is manual application, not native
selection. Fix both final reports before the operator opens the key. An operator
who prepared the key should not conduct or influence either review; if separate
roles are unavailable, record the limitation.

## Adjudicate

Compare each fixed report against the key independently, recording locators,
reported reader consequences, seeded hits and misses, treatment of the short
reference control, route-tier and readiness decisions, and evidence for any
additional finding. Preserve uncertainty about unseeded editorial findings and
avoid treating absence from the key as proof of a false positive. Distinguish
reported file reads from observed events and catalogue availability from native
activation. Record unobservable payloads and unperformed tests explicitly.
Privacy-review retained events and summaries; do not commit raw transcripts,
credentials or private reasoning. Report the hashes, exact prompts and
configuration, isolation checks, actual observations, adjudication and limits.
