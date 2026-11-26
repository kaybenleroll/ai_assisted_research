# Native Audit-Skill Selection Trial: Spectral Primer

## Question and Inputs

On 26 November 2026, a fresh Codex CLI `0.172.0` session using
`gpt-6.1-terra` at medium effort received a read-only editorial task without
being told which skill to use. It ran in the clean guidance checkout at commit
`2688081`; the audit skill SHA-256 was
`a141d8d65c1ed06e3f410cc6f45fd23272bbf57efb33984e386d7f9c6c250eb9`.
The source was `primer_spectral_graph_theory/primer_spectral_graph_theory.md`
(SHA-256 `37a27a61a40eeb81bb3c35253de5be4483a92c1529ff5f8b01db9c017ed4cf7c`)
and its published HTML. The source and skill revisions are also recorded in the companion calibration report.

The exact prompt, SHA-256
`e9a6f7c4d02ee005a2cef1b0e992f9ac568cf78d65354c00abccc75cec264c11`, was:

> Please review primer_spectral_graph_theory/primer_spectral_graph_theory.md and its published HTML for structure and explanatory depth. Notation should appear within the introduction before first use. Read the whole source in bounded contiguous batches and report coverage, concrete reader consequences, the structural and release decisions, and checks not performed. Treat this as a read-only review. Do not read prior audit records, issues, calibration reports or failure ledgers, and do not edit files or delegate.

The stated notation requirement was supplied to the session, so identifying it
is not evidence of discovering an unstated preference. The spectral primer had
already been used in prior trials; the session was fresh, but the source was not
an independent unseen fixture for the overall calibration programme.

## Observations

The returned session announced that it was using `primer-audit`. Its recorded
command events include `cat .agents/skills/primer-audit/SKILL.md` and a run of
`primer_outline_compare.py` on the source and HTML. The task did not name the
skill. This is observed autonomous selection and file reading; a separate
structured native-activation event was not established. It does not by itself
prove substantive skill use.

Nine recorded `sed` command outputs cover source ranges 1–250, 251–500,
501–750, 751–1000, 1001–1250, 1251–1500, 1501–1750, 1751–2000 and
2001–2251. The coordinator compared each recorder-captured output with the
corresponding source lines: all were exact. This supports recorded output
coverage, but does not independently establish what the model received or
understood. No genuine tool-output truncation was induced or verified.

The final review identified the requested notation placement, the missing
rendered portfolio heading at source line 1122, inadequate multi-step exercise
feedback at lines 1560–1593, and the perturbation-ledger promise-to-evidence
mismatch at line 1016. It reported structural fail and release not-ready and
explicitly excluded independent numerical verification, example execution,
links, PDF and visual QA, source freshness and full route reconciliation. The
reported comparator found the missing heading without the two apostrophe false
positives seen in the earlier trial. These findings agree with source-checked
issues #479, #480, #486 and #478 within their stated scopes; they do not prove
that every section or technical claim was assessed correctly.

## Retention and Limits

The coordinator reviewed this minimal record for task-relevant, non-sensitive
content. The raw JSONL event file was not reviewed for safe publication and is
not committed; it was temporarily stored under `/tmp/native-audit-471-events.jsonl`
with SHA-256 `4ec9de9c4541c0b458f2ac16e0c010a4ca373e5a4000b7729fd0ab68694d217e`.
Its persistence is not guaranteed. The returned final report's SHA-256 was
`a4078599ff4c435e29acb7357e92d0f041c023b85d2a5b61ae310d4c1d478751`;
a hash alone cannot reconstruct a lost report. Only the observations above are
retained. This is one natural-selection trial on a previously used primer, not
proof of reliable activation, genuine truncation recovery, general audit
quality, or release readiness.
