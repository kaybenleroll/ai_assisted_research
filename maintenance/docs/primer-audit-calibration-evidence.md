# Primer Audit Calibration Evidence

This record inventories evidence for the draft outline and audit workflow in
[#471](https://github.com/kaybenleroll/ai_assisted_research/issues/471) and
sets a format for future calibration under
[#484](https://github.com/kaybenleroll/ai_assisted_research/issues/484). It
is not a primer audit or a claim that the workflow reliably detects all defects.
The inventory was made on 26 November 2026 against draft PR
[#472](https://github.com/kaybenleroll/ai_assisted_research/pull/472), branch
`docs/471-primer-outline-review`, commit
`4aa4d3d9f90689e47c65876db446ee30a2dd6a1d`. Paths describe this environment
at that time; absence here does not prove that no copy exists elsewhere.

## Inventory and Evidence Boundaries

| Evidence | Observed state | What it establishes and what remains unavailable |
|---|---|---|
| Draft branch `maintenance/docs/primer-outline-calibration-471.md` and `maintenance/docs/primer-audit-failure-ledger-471.md` | Present in Git at `4aa4d3d` | Durable summaries of reported trials, failures, revisions and limits. They are not the underlying event logs. |
| Draft branch `maintenance/tests/fixtures/primer_audit_behaviour/` | Present in Git at `4aa4d3d`: prompts, samples A and B, references, contents extracts and answer key | Recoverable fixture inputs and adjudication key. Presence alone does not establish what a session received or produced. |
| `/tmp/outline-skill-activation-471.jsonl` | Absent | The report describes a manual skill read; the raw event record could not be inspected. It does not claim native activation. |
| `/tmp/outline-fixture-471/` | Absent | The earlier request-error-rate fixture and review are summarised in the report; the named raw inputs and output were not recovered. This is distinct from the tracked A/B fixtures. |
| `/tmp/outline-natural-probe-471.jsonl`, `/tmp/outline-natural-retry-471.jsonl`, `/tmp/outline-natural-final-471.jsonl` | All absent | The report records two partial attempts and a same-fixture retry. The raw records cannot independently verify their prompts or outcomes here. |
| `/tmp/primer-audit-trials-471/` | Absent, including all named files beneath it | The report preserves summaries of A/B selection probes, long-primer and comparator trials, controlled-reader prompts, readers and logs, and spectral and semantic trials. None of those temporary raw files was recovered in this inventory. |
| `.scratch/outline-audit-471/glm-locator-recheck.md` and `glm-source-followup.md` in the main workspace | Both present as ignored local files | These are related local notes about locator and source checks, not substitutes for missing trial prompts or event logs. Their contents were not audited or copied here. They remain ephemeral and may require privacy review. |

The missing trial-directory files named in the report include `native-probe.jsonl`,
`native-probe-b.jsonl`, `native-long.jsonl`, `native-long-same-tree.jsonl`,
`prompt-real-bound.txt`, `primer-reader-bound.py`, `session-real-single-batch.jsonl`,
`prompt-real-complete.txt`, `session-real-complete.jsonl`, `prompt-real-single.txt`,
`session-real-single.jsonl`, `prompt-native-complete.txt`,
`session-native-complete.jsonl`, `prompt-spectral-independent.txt`,
`session-spectral-independent.jsonl`, `prompt-semantic-independent.txt` and
`session-semantic-independent.jsonl`. The report also describes controlled
fixtures and other prompts in that directory without naming every file. The
inventory checks the named directory as a whole; it does not claim a search of
all backups, sessions or machines. These records are missing from the inspected
locations; whether they are irretrievable is unknown.

The report distinguishes observable selection and reading of the skill from a
separately recorded native activation event. A command that opens `SKILL.md`
shows a file read. The prompt and event record determine whether the read was
manually instructed or autonomously selected; applying the guidance substantively
requires further evidence. Catalogue discovery, selection, activation, file
reading and successful application are separate observations.
In particular, the reported native-truncation session said its first response
was truncated, but the described event log retained the complete command output.
The delivered payload was not independently observable. Subsequent range reads
and the report do not prove the initial delivered content or comprehension.
Simulated omissions and a real tool-layer truncation are different conditions.

## Durable Trial Record

Store a small reviewed Markdown record with the fixture and any safe,
reproducible reader or harness needed to repeat it. Bind each referenced tracked
artefact to a reachable commit and, where useful, a content hash. Record an
uncommitted input by hash and preserve its reviewed content before relying on it;
a hash alone cannot reconstruct a lost file. Link each record from the relevant
issue or PR. Preserve failed and inconclusive trials alongside successful ones.

Before retaining an event excerpt, inspect it for private data, credentials,
hidden reasoning and unrelated conversation. Retain only the minimum safe
prompt, tool requests and observable outputs needed to support the claim; use
redacted excerpts or a purpose-built event summary where raw material cannot be
published. State who reviewed the redaction, what was omitted and where any
permitted raw record is retained. Never commit hidden reasoning, credentials or
unreviewed transcripts. If evidence cannot be safely retained, mark it
unavailable and limit the claim; do not invent a substitute observation.

Use this template for each trial:

```text
Trial ID and date:
Question and success/failure criteria:
Fixture or task: tracked path and commit/hash; exact safe prompt or path:
Source, rendered output, brief and guidance revisions/hashes:
Harness, model/effort and relevant tool configuration:
Selection evidence: catalogue discovery / native activation event / skill read /
  manual instruction, each observed, self-reported, not observed or unavailable:
Actions: ordered tool requests and safe output references; source ranges and
  whether each response was complete, truncated, unavailable or unknown:
Results: findings and gate decisions; observed output versus reviewer report:
Adjudication: expected findings, misses, false positives and disagreements;
  evidence and reviewer for each decision:
Truncation: simulated or tool-layer; trigger, independent evidence of delivered
  payload if available, retries and ranges recovered or still missing:
Retention: safe artefact paths and hashes; redaction reviewer and omissions;
  raw evidence location or reason unavailable:
Limitations and next action: scope, uncertainty, owner and issue/PR link:
```

An event record can show a request, a response captured by the recorder, or an
explicit activation event only if the instrumentation exposes it. Distinguish
that observation from the model's own account and from an adjudicator's
inference. Received line ranges are self-reported or recorder-observed coverage,
not proof of comprehension. A sample fixture, a passing checker or a successful
retry does not establish performance on every document.

## Targeted Follow-up Trials

1. **Recovery with independently observable tool truncation.** In a fresh
   single-reviewer session, use a revision-bound long source and an unnamed
   complete-audit task that does not instruct recovery. First establish whether
   the harness exposes the exact payload delivered to the reviewer and an
   independently observable truncation indicator. If it does, provoke actual
   tool-layer truncation and retain safe evidence of the initial payload,
   autonomous retries, recovered and missing intervals, and final gate decisions.
   If it does not, record the test as unobservable, not passed; do not substitute
   a full recorder output or the reviewer's statement for delivery evidence.
2. **Controlled recovery and unavailable control.** Separately rerun a
   deterministic simulated omission using a preserved reader and fixture, with
   a complete-audit request but no recovery instruction in the prompt. Include a
   control where omitted ranges cannot be obtained. Record whether recovery was
   attempted without a follow-up prompt, whether every range was obtained and
   whether an incomplete review remains not ready. Label the omission simulated.
3. **Editorial calibration and activation.** Repeat a blinded real-primer
   outline and reader-journey review, plus a contrasting fixture with a valid
   short reference section. Record the exact brief, sources, rendered contents
   and skill revision, seeded or independently adjudicated findings, misses and
   false positives. Run an unnamed-task selection probe separately from a manual
   skill application; capture only activation events the harness exposes. These
   tests address specific failure modes and do not certify a full audit.

The trial owner should publish or link the reviewed records to #471 and #484,
then decide whether the remaining uncertainty changes the draft workflow's
stopping boundary. Do not delay recording a failed or unobservable trial until a
successful one is available. The schema bypass in #483 is a separate
implementation question; coverage records cannot prove that a reviewer read or
understood a source.
