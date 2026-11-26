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

## Second Native Trial: Pi Coding Agent

A fresh `codex exec` session with the same CLI, model and effort ran at
`fcd58e9` against `primer_pi_coding_agent/primer_pi_coding_agent.md`
(SHA-256 `1a8edd490e0f3fb58f864a89da5a3d15b5fb3320aa2e20c7dd471a90e0ee0fd0`)
and its HTML. The prompt SHA-256 was
`d3380d4dae817fa33cc95d256f2aaa3758dc26b859ad9959afcf502d43fa1c21`:

> Please review primer_pi_coding_agent/primer_pi_coding_agent.md and its published HTML for structure and explanatory depth. Read the entire source in bounded contiguous batches, check the reader journey and practical examples, and report source coverage, concrete reader consequences, structural and release decisions, and checks not performed. This is a read-only review. Do not read existing audit records, issues, calibration reports or failure ledgers, and do not edit files or delegate.

The prompt did not name the skill. Recorded commands show one read of
`.agents/skills/primer-audit/SKILL.md` and two invocations containing the
outline comparator. The recorder's six source outputs matched the source
exactly for ranges 1–180, 181–360, 361–540, 541–720, 721–900 and 901–1082.
As above, recorded outputs do not independently prove the delivered payload or
comprehension; a structured native-activation event was not established.

The final review characterised the first-session route as sound, but did not
identify that `git diff` cannot show the contents of the newly created untracked
README (source lines 127–151; previously verified issue #473). This is a
concrete missed practical verification step. The reviewer also questioned
whether the Rocker case fulfils its culminating role because several components
are absent. The source explicitly calls it illustrative and states those
components must be created (lines 774–776); without the complete brief, the
reviewer's stronger assertion is an unresolved scope judgement, not a confirmed
defect or false positive. The comparator reported no candidate heading mismatch;
the review did not run examples, verify live claims, inspect the tracked brief
or perform release checks. It reported release not-ready and gave no explicit
structural-gate label, despite an overall structural disposition.

This trial shows one natural skill-file read but a consequential missed action
and an omitted gate label; it does not establish reliable skill behaviour. The
raw event file was not reviewed for publication or committed. Its temporary
SHA-256 is `22182b3dca44789771b2dcd4358e8b2e7591cfd593eeb5e225eaabdbff004a4e`;
the final report SHA-256 is
`5fd9ac505f60b4eb447fe2b89e9d6941a0e68c74054f619156b69c9d8257c564`.

## Third Native Trial: Practical-Verification Guidance Retry

A fresh read-only Codex session used the same Pi prompt and source, with the
new practical-verification guidance at commit `d65b98d` (skill SHA-256
`d9d51ca7fc6802affb27d0c4a091a67693feebe47c52e080651d09e573c49804`).
The prompt prohibited edits and the session used a read-only sandbox, so it was
not given a writable disposable fixture; a failure to execute such a fixture is
not itself a violation. The skill file was read. Eight recorder-captured source
outputs matched the source for lines 1–150, 151–300, 301–450, 451–600,
601–750, 751–900, 901–1050 and 1051–1082. This establishes recorded outputs,
not the exact delivered payload or comprehension.

The reviewer again described the first-session route as making independent
diff review observable and did not identify the untracked README problem in
#473. It also omitted an explicit structural-gate label. The coordinator
independently ran a minimal temporary Git reproduction: `git status --short`
showed `?? README.md`, while `git diff` returned no README contents. The retry
found the separately tracked Rocker comparator-description ambiguity (#474),
but its stronger judgement on the explicitly illustrative project remains
unresolved without the complete brief. This was a fresh session but the same
source and task as the preceding trial, so it is not independent generalisation.
The new instruction did not reliably surface the known practical failure in this
setting. The reviewer was not asked to read existing audit or issue records.

The unreviewed raw event file remains temporary only (SHA-256
`3f1b6fd556a7c1bfba94f6c793d4d7f0c9637b162f3b9ae9394e1feb3e6d186d`);
the returned report SHA-256 was
`599f5da23b90dad4daf3f9e8f871668542e535993ee7501e87601060158961a9`.
Neither hash preserves its file. No genuine tool-layer truncation was tested.

## Fourth Native Trial: State Transitions and Disposable Fixture

A fresh Codex session used guidance commit `2edc135` (skill SHA-256
`86db2891c690bca131541e7cabdf61c4ff525ce350a079ae56870ca492b3cb20`)
and the same Pi source and HTML. Unlike the preceding read-only-sandbox trial,
this run allowed a disposable temporary directory and the reviewer chose to
read the tracked brief and case contract. Their SHA-256 values were respectively
`0a9de70192ca8fb5862337e8a4d6229251335bdbd360e586551a20c625898d56` and
`b88cf7973b9a90e65dbb6d8d123a0ed4fbc69dcdb1bf21f7d89268fa79a86e93`.
The brief promises an independently reviewed first-run change but does not
identify the untracked-file defect. The prompt (SHA-256
`6cced5545cb323220f4fc5909c475b36e1cb99751d09d90d8ed0724174b634c1`) was:

> Please review primer_pi_coding_agent/primer_pi_coding_agent.md and its published HTML for structure and explanatory depth. Read the entire source in bounded contiguous batches, check the reader journey and practical examples, and report source coverage, concrete reader consequences, structural and release decisions, and checks not performed. This is a read-only review of the repository; you may create a disposable temporary directory outside the repository to check commands. Do not read existing audit records, issues, calibration reports or failure ledgers, and do not edit repository files or delegate.

The recorder shows a skill-file read and eleven source-read outputs matching
lines 1–1082 after removing the displayed line numbers. It also records a
successful temporary Git reproduction: status printed `?? README.md` and the
following `git diff -- README.md` printed no content. The final review identified
the first-run verification defect, gave a structural-gate pass for its scoped
review, and reported release not-ready pending correction and release checks.
It treated the Rocker project as illustrative within its disclosed limits,
which differs from the previous reviewer's unresolved scope concern. It did not
execute Pi or check current external claims or rendered visual accessibility.

This is a successful detection and independently observable reproduction of
the known #473 failure, after two unsuccessful Pi trials. It used the same
source and a changed prompt/sandbox, and consulted a brief and contract that the
previous trial did not. Those differences prevent attribution of the result
to the new instruction alone. A success on this known example does not prove
general reliability, native-activation semantics or genuine truncation recovery.
The reviewed minimal observations are retained here; the unreviewed raw event
file is temporary only, SHA-256
`43d8f71dbc576a2653e0f32737b550ac358d407cb0eaac8368755e37cdbb24a0`.
The returned report SHA-256 was
`be9324f4dbcba5ceacd6efde69c2742258e3ca175e6aafdce492f7ada05f4423`.
Hashes alone cannot recover lost files.
