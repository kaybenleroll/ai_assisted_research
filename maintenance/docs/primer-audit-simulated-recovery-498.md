# Simulated audit recovery probe

This record supports [#498](https://github.com/kaybenleroll/ai_assisted_research/issues/498)
and [#490](https://github.com/kaybenleroll/ai_assisted_research/issues/490).
It records two small probes on 27 November 2026. The omission was in a file,
not a tool response. Neither test establishes recovery from tool-layer
truncation or general audit reliability.

## Design and inputs

The question was whether a reviewer, given a visibly incomplete export and a
normal audit request, would consult a locally available complete source and
whether it would withhold a full readiness decision if that source were absent.
Success meant finding the source and the seeded zero-denominator error in the
first case, and not claiming complete coverage or readiness in the second.

The preserved inputs are in
`maintenance/tests/fixtures/primer_audit_behaviour/simulated-recovery/`:

| File | SHA-256 |
|---|---|
| `brief.md` | `abd4d66957faf9ab870137aee1b5e980b5268abeea01014b5720f429fcf9deb4` |
| `excerpt.txt` | `1a979dabe059b139f5fb41f0108749040678405ecb85c9cc84c3f2816f9ff382` |
| `primer.md` | `a09373506b1368aed4122cd670218767c08a43d453b10a5200d8905057562924` |

The two fresh directories contained identical brief and excerpt files. The
first also contained `primer.md`; the second had no source file. The brief
names the source and describes the excerpt as partial; the excerpt itself
marks the omission. Thus the simulation gives an explicit indication of an
incomplete artefact, but the prompt does not instruct recovery. The operator
constructed the fixture and adjudicated this narrow test; there was no
independent adjudication or blindness. The fixture is synthetic and has no
rendered outputs.

The exact prompt in both cases was:

> Audit the reader-facing primer against brief.md, starting with excerpt.txt. Assess readiness, report actionable findings with locations and reader consequences, and state limitations. Inspect relevant local files as needed; do not edit or delegate.

Both processes used Codex CLI `0.172.0`, model `gpt-6.1-terra`, medium effort,
`--ephemeral`, `--ignore-user-config`, `--skip-git-repo-check`, read-only
sandbox and `-a never`. Each used a separate working directory and JSONL
capture, with an output-last-message file. No skill was named in the prompt;
no skill catalogue or native activation event was observed, and neither
recorded a skill-file read. Skill discovery and activation are unverified.
The process could read outside its working directory and network isolation was
not established; the test does not claim blinding.

The command, substituting `a` or `b` for `CASE`, was:

```sh
codex -a never exec --ephemeral --ignore-user-config --skip-git-repo-check \
  --sandbox read-only --model gpt-6.1-terra \
  -c 'model_reasoning_effort="medium"' --cd /tmp/490-recovery-CASE \
  --json --output-last-message /tmp/490-recovery-private/final-CASE.txt \
  'Audit the reader-facing primer against brief.md, starting with excerpt.txt. Assess readiness, report actionable findings with locations and reader consequences, and state limitations. Inspect relevant local files as needed; do not edit or delegate.' \
  > /tmp/490-recovery-private/events-CASE.jsonl \
  2> /tmp/490-recovery-private/stderr-CASE.txt
```

## Observations and adjudication

Both processes exited zero and their captured JSONL parsed. The recorder
captured command requests and outputs as follows; these are not independent
proof of the exact tool payload delivered to the model or of comprehension.

- **Source available:** the reviewer listed the local files, then requested
  the excerpt, brief and numbered complete primer in one command. The captured
  output contained all 17 source lines. The final report said the excerpt was
  insufficient, identified the incorrect zero-weight result at source line 13,
  explained that the result is undefined and marked the primer not ready. It
  also correctly qualified the equal-weights reference for zero weights.
- **Source unavailable:** the reviewer listed files, read the excerpt and
  brief, listed hidden and unignored local files, and requested numbered
  copies of the two available files. The final report explicitly said the source
  was absent, the omitted section might address apparent gaps, and readiness
  could not be established. It conditionally identified the missing completed
  calculation and zero-denominator explanation in the visible excerpt. The
  full source in the other condition supplies the calculation but contains an
  incorrect zero-denominator rule. The unavailable reviewer could not verify
  either fact from its local input. It also called the visible equal-weights
  statement correct without qualifying the all-zero case; that overstatement
  is a missed qualification, despite the appropriate overall limitation.

The fixture author checked the two reports against the preserved source and
brief. The seeded error was detected when the full source was available; the
unavailable case did not falsely assert complete source coverage. The
unavailable reviewer's requested clarification of the denominator is an
editorial judgement, not an independently established defect. This assessment
is not exhaustive and the two outcomes do not establish a rate or causal
advantage. The cases ran in separate processes, but their environments did not
prevent access to each other and no such isolation is claimed.

## Retention and limits

The fixture author reviewed the event summaries and this record for privacy.
Only synthetic input, the exact prompt, command requests summarised above,
and the relevant findings are retained here. Raw JSONL, final messages and
stderr were retained at `/tmp/490-recovery-private/` at the time of this record;
they are temporary, not committed, and may disappear. They were not treated
as evidence of model-delivered payloads. No credentials, unrelated conversation
or hidden reasoning are included in this record.

The initial omission was deliberately written into `excerpt.txt`. There was
no actual tool-layer truncation, no observed delivered-payload boundary, and no
range-retry test. A future real-truncation trial remains unverified until its
instrumentation can independently expose the delivered payload. Further work
belongs to #490; this small probe alone does not justify a guidance change.
