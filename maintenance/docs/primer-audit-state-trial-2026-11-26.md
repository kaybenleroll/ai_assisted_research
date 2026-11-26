# Practical State-Transition Calibration, 26 November 2026

## Design and Inputs

Two small offline examples test whether a reviewer follows a published artefact
through generation and verification. They are not complete primers. Both
promise the same three-sensor CSV and use similar build and verification
commands. In case 17, the published output omits one row while the verifier
checks staging and prints `PASS`. Case 29 was intended as a valid control.
The scripts, reader-facing guides, original and corrected control, and
[answer key](../tests/fixtures/primer_audit_behaviour/state-transitions/ANSWER-KEY.md)
are tracked under `maintenance/tests/fixtures/primer_audit_behaviour/state-transitions/`.

All reviews used fresh Codex CLI `0.172.0` sessions with `gpt-6.1-terra` at
medium effort, manually directed to the audit skill at commit `2a62ddd`
(SHA-256 `86db2891c690bca131541e7cabdf61c4ff525ce350a079ae56870ca492b3cb20`).
The guide hash for all cases is
`ed24434b83dca1b5b95da9cdd4c222e391afd3b069676eeb1edce92354f1de64`.
Case 17's build and verifier hashes are
`2809afc26789f53e4cd509892cf07d5c85496c788235a6cb748f1d1e666697f6` and
`deaa036063a4e700d99716ff2fafd0554433d94ddb18012e27da7dbfdcfc2b19`.
Case 29's build hash is
`84ff225719bddbf7ab68680f61c96dc19d90b7204e5a7d1a1c40beb41d0611ff`;
the original verifier hash is
`aae26c3159428fcca1c793ceac74690f3cc1edc6e585ae270a9d2332440991d0`,
and the corrected verifier hash is
`9da2d61a79d254c5ce79f148695b51a509d1f2146a5c6c4de7ad33b16349ce6d`.

An initial pair of delegated reviews was interrupted because their directory
names revealed which input was faulty. Their results were discarded. The
fresh sessions below received neutral directory names and no answer key. Each
received the following prompt, with only the case directory changed:

> Review the practical teaching material under /tmp/primer-case-17, starting at PROMPT.md, using /tmp/ai-research-outline-review/.agents/skills/primer-audit/SKILL.md as applicable. Assess whether the material fulfils its stated reader promise; inspect and run its supplied offline commands if useful. You may write generated files only inside that fixture directory. Do not inspect sibling directories, answer keys, prior calibration material or audits; do not delegate. Return exact findings, evidence, reader consequences and unperformed checks.

The case-17 prompt SHA-256 was
`bf04bf886ea6c1900e2302922db980a30595b3af75032991a54f4497409ca6a8`;
the otherwise identical case-29 prompt hash was
`63e060a54f3029d127e63f4da7255fb3ce4a6949d6c8eedcc462f79ab47347b2`.
The revised control used the same case-29 prompt in a new session. Temporary
fixture directories were separate from the repository. These were manual-skill
trials, not tests of natural discovery or native activation.

## Observations and Adjudication

The case-17 review read the skill and scripts, ran both commands, compared
staging and published contents, and identified both the omitted row and the
verifier's wrong target. It reported content fail. The returned final report
SHA-256 was `2eefb3a63ccb637640c45321567836c8b12ed54020f62ece353fb40659ac47bd`;
the temporary unreviewed event record hash was
`211ad7aebbd580ccc6986afe313a9d76b6bd75d578fdad953b2712b43ffd90a9`.

The original case-29 reviewer correctly identified a separate defect in our
intended control: `csv.DictReader` accepted duplicate `count` columns and the
verifier returned `PASS` on conflicting values. The coordinator reproduced
this. This is a genuine finding, not a false positive. The event record shows
a search of the local memory registry for general audit terms; the possible
influence of the returned material is unknown, so this run is not treated as
fully blind. Its returned report hash was
`5b9604320998658729e6ec74cea3c6886f0ba28fa33433b5705178eb2b885c21`;
the unreviewed temporary event record hash was
`2705f7132a6ef080013c52ea11783ea51ab7d036ad9e089235be45d7d75162ee`.

The corrected control validates the exact header and rejects extra fields. A
fresh reviewer reported that the fixed-inventory workflow meets its narrow
promise. It also raised two valid practical qualifications: rebuilding
unconditionally overwrites files and staging is an independently written
copy, not a source from which publication is derived. It did not treat those
as failure of the specified fixed-output task. It tested an incorrect published
reading, but did not claim exhaustive malformed-input or filesystem testing.
Its report hash was
`15247c55059d1c6c43ffdd1eb12bcb4b46a6fa30cbb16c77af42a95e5c996149`;
the unreviewed temporary event record hash was
`1b6f5e38fcbccfabec37f05ed701266b23f4661a1e76da3300138d9e3fa219a4`.
The corrected-control reviewer used the same case number in a fresh session and
saw no prior report, but the fixture was revised after an earlier review: it is
not a pre-registered, independently chosen negative control.

`test_primer_state_fixtures.py` reproduces the faulty false pass, the original
control's duplicate-header false pass, and the revised control's success and
header rejection in disposable copies. The coordinator retained this minimal
adjudicated record rather than committing unreviewed raw transcripts; raw files
under `/tmp` may disappear and their hashes cannot reconstruct them. These
small, related fixtures support detection and a qualified control observation,
not proof of accuracy on all practical workflows or of genuine tool-layer
truncation recovery.
