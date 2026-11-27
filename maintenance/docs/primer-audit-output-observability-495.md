# Primer Audit Tool-Output Observability Probe

This record supports [#495](https://github.com/kaybenleroll/ai_assisted_research/issues/495) and the wider calibration in [#490](https://github.com/kaybenleroll/ai_assisted_research/issues/490). It supplements the [earlier calibration record](primer-audit-calibration-490.md). On 27 November 2026, a synthetic probe compared a Codex CLI event stream, a hook input and the model's report. It was an instrumentation check, not an audit or an autonomous recovery trial.

## Procedure

The host ran Codex CLI `0.172.0`; the hook identified the model as `gpt-6.1-terra`. Reasoning effort was not independently recorded. The session was ephemeral, used a read-only tool sandbox, and ran outside the repository in `/tmp/codex-490-trial`. No primer or skill was supplied. The operator used the following capture script, which writes hook standard input to a local file and emits no hook decision:

```python
import sys
with open('/tmp/codex-490-trial/hook.jsonl', 'a', encoding='utf-8') as f:
    f.write(sys.stdin.read().strip() + '\n')
```

After creating the directory and saving this script as `capture.py`, the successful invocation was:

```sh
codex -a never -s read-only \
  -c 'hooks.PostToolUse=[{matcher="Bash",hooks=[{type="command",command="/usr/bin/python3 /tmp/codex-490-trial/capture.py"}]}]' \
  exec --ephemeral --json --skip-git-repo-check \
  --dangerously-bypass-hook-trust -C /tmp/codex-490-trial \
  'Use exactly one shell tool call to run seq 1 20000 with a small max output token limit if available. Report whether output was truncated and quote its truncation indicator. Do not call any other tools.' \
  </dev/null > /tmp/codex-490-trial/events2.jsonl \
  2>/tmp/codex-490-trial/stderr2
```

The bypass applied only to this invocation; the operator supplied and inspected the local hook. It is not a recommendation to bypass hook trust generally. The CLI warned that untrusted project-local configuration was disabled; the hook configured on the command line nevertheless ran. The exact tool-call token-limit argument was not retained in the event record, so the chosen limit cannot be independently reconstructed from it. The hook input recorded `Bash` and command `seq 1 20000`.

## Observations and retention

The completed command event's `aggregated_output` contained 108,894 characters, beginning at `1` and ending at `20000`. The hook's `tool_response` contained 507 characters and included:

```text
Warning: truncated output (original token count: 27224)
Total output lines: 20000

1
2
...
…27124 tokens truncated…
...
19999
20000
```

The ellipses on separate lines above denote excerpts omitted from this record; the truncation marker itself was in the hook response. The model reported: “Yes, the output was truncated. The indicator was: ‘Warning: truncated output (original token count: 27224)’.” That report is consistent with the hook but is not an independent capture of the complete payload delivered to the model.

The operator reviewed the prompt, script, hook fields and relevant event output for retention. This record retains only the synthetic command, findings and short excerpts; session identifiers, paths to any transcript, unrelated context and raw event records are omitted. At the time of the probe the disposable local files had these SHA-256 hashes; their `/tmp` locations are not durable archives:

| File | SHA-256 |
|---|---|
| `capture.py` | `4913f5174a3bb443b6022c36b6e68d30ce20c1a3e71438e993e5f4ca9384a04b` |
| `events2.jsonl` | `a0be31fc08b92133cb90153c917c9907269934e4b75cb980507eef824edf5616` |
| `hook.jsonl` | `fe62f119899e4d9be10a7e86dd5540ffa35702eaea8e2a3b2a730528424dd101` |

Hashes identify the observed local files but cannot reconstruct them. Repeating the command produces a new session and may produce different event metadata or model behaviour. Raw hooks and event streams can contain prompts, tool outputs, paths and other sensitive context; inspect and minimise them before retention or publication. Never publish credentials or hidden reasoning.

## Interpretation and limits

The event stream and hook captured different representations of the same synthetic command output. The hook exposed a truncation indicator, and the model reported the same indicator. The event's complete output must not be treated as the model's delivered payload.

The [version-matched implementation](https://github.com/openai/codex/blob/rust-v0.172.0/codex-rs/core/src/tools/context.rs) supplies the hook with output rendered under the model output policy, while `response_text()` adds a header and can further reduce the budget. Consequently the hook is evidence of its own input, not proof of the exact final bytes sent to the model. The [hook documentation](https://developers.openai.com/codex/hooks/) describes supported paths and their exceptions. This probe did not independently capture the final request, test all tools or establish comprehension.

The first synthetic attempt used literal `\\x27` sequences in a Python command, which caused a syntax error; its project-local hook was also disabled as untrusted. It produced no truncation evidence. A separate minimal `Reply only with OK.` CLI session completed but exercised neither a tool nor a skill. An initial sandboxed attempt failed during CLI initialisation because the home filesystem was read-only; the successful sessions ran with the authorised narrow sandbox escalation. These failures do not establish a CLI product limitation.

This prompt explicitly requested a truncation report. It did not ask for a primer review, attempt recovery, test an unavailable range, or exercise native skill activation. Those questions remain open under #490. A future recovery trial needs an independently observable final model-facing payload and a fresh, unnamed audit task; otherwise record the delivery boundary as unobservable and do not claim a pass. A separate controlled omission may still test recovery behaviour, labelled as simulated.
