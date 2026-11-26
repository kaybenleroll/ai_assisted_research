# Primer outline calibration for #471

This report records behavioural probes of revised structural-audit guidance. It
does not establish a full primer audit, release readiness, or native skill
activation.

## GLM

The first blinded manual trial provisionally passed the structure despite a
truncated read and missed known issues. That result is a calibration failure,
not evidence that the primer met the user's requirements.

After the instructions were revised, a second independent trial identified the
placement of notation, a duplicated lone child heading, and missing subheadings
in the combined case. It initially marked the incomplete review as
`not-checked`; after reading the full source and rendered contents, it judged
the findings editorial improvements. The user has expressly said the primer is
not ready. Unmet user requirements block readiness regardless of that editorial
judgement.

The reviewed source was `primer_glm/primer_glm.md`, at source commit
`8417dba1d9183041213115f6361d84107ae40109`, SHA-256
`27d68fb0fdb9686588bf349404a88764702ae405e1d96cfc99f05d85f19cef07`.
The trials do not prove that every structural issue was found.

### Locator remapping failure

Following the GLM revision at source commit `0245c0356ecd5fb33d94f46ae8eac3ebf133ba58`,
the revision-bound checks for the brief `glm-brief-v6` and audit
`glm-content-audit-v4` passed their schema and locator-existence checks. A
subsequent semantic review found many route and concept cells bound to real but
incorrect passages, including headings, unrelated statements and a reference-only
route presented as a complete teaching transition. Thus the mechanical passes did
not establish that the cited passages supported the claims. Further locator
corrections and independent verification are in progress; this record does not
claim that those corrections have been validated.

Guidance commit `ab7bcd9` strengthens `.agents/skills/primer-audit/SKILL.md`
and `maintenance/docs/primer-production-procedure.md` to require semantic
checking of every retained or moved explanation, action, interpretation and
limitation locator after revision. This addresses the identified guidance gap;
it does not itself validate the GLM evidence or establish a complete technical
audit.

## Knowledge graph

A manual trial inspected the current outline and representative passages of
`primer_knowledge_graph/primer_knowledge_graph.md`, at source commit
`5924434d90d25eba7360d78172d74b21365462c6`, SHA-256
`74e0d4fb5a7add90685da8fc7f94461eeb67ce4c4d976658c0da8383144332f7`.
The brief was revision `kg-398-brief-r13`, SHA-256
`29bc428f153f9e7f4e3b0640b9f1bf76c26d6b85a467a96cd5fd01b43d6f18d5`.
The reviewer had already seen the earlier audit; this trial was not blind.

The short further-reading section was retained as navigation, and the
literature and installed-dependencies cases as distinct applications. The
introduction's repeated graph, storage, and ledger comparisons were a possible
non-blocking editorial improvement. The trial was partial: it did not review
every child relationship or complete the full audit. It cannot support a
structural-gate pass.

## Activation and evidence limits

A fresh Codex 0.171 prompt read the updated skill through a command. No
independent native activation event was established; this is manual application,
not evidence of native activation. The temporary raw log is
`/tmp/outline-skill-activation-471.jsonl`.

For the knowledge-graph trial, the uncommitted audit skill had SHA-256
`ca83cda52fe2af0e69f97af8b708640f944e63bba20ccad07f0541cea8d238e5`
and the uncommitted shared procedure had SHA-256
`de5f5e57d6d4d441b4095528357abe16f56d78649f77197a0fad0eec0955a568`.
The worktree HEAD was `e03baa554ff96cad286efb9caf32c9d82c9d6f4d`.
A later refinement to the wording about user requirements was not separately
behaviour-tested. No synthetic test result is claimed.

## Independent synthetic trial

A separate reviewer manually applied the revised workflow to a synthetic
request-error-rate primer without reading the fixture author's audit. The
reviewer identified a calculation fragmented across headings, a redundant
single-child orientation, and missing landmarks in a long worked case. A short
reference section was retained. The reviewer proposed incorporating a short
transition that the fixture author had retained; this disagreement requires
editorial adjudication and is not automatically a false positive. The fixture
had no rendered output, so the reviewer correctly recorded the structural gate
as not checked and release as not ready. This is a controlled fixture, not
real-primer validation or native skill activation. The temporary inputs and
review are under `/tmp/outline-fixture-471/`; their availability is not assumed
for a future audit.

A fresh, unnamed-task Codex 0.171 session selected `primer-audit`, read its
canonical skill file, and identified the fixture's fragmented calculation and
missing case landmarks while retaining the short reference. It stated that
rendered contents were unchecked but reported release readiness as unchecked,
rather than the required `not-ready`. After the skill was clarified, a second
fresh session selected and read the skill, found those same candidate issues,
and reported release readiness as `not-ready`. It did not explicitly label the
structural-gate decision despite the instruction to state both decisions. These
are partial behaviour observations on one synthetic fixture, not proof of
reliable activation or editorial judgement in other tasks. Raw temporary event
logs are `/tmp/outline-natural-probe-471.jsonl` and
`/tmp/outline-natural-retry-471.jsonl`.

After the instruction was refined to require both labels, a third fresh
unnamed-task session selected and read the audit workflow, identified the
fragmented calculation and missing case landmarks, retained the short
reference, and explicitly reported `Structural gate: not-checked` and
`Release readiness: not-ready` because rendered contents were not inspected.
This is one successful retry on the same fixture, following two partial or
failed trials, not evidence that the workflow will always be selected or
applied correctly. The temporary event log is
`/tmp/outline-natural-final-471.jsonl`.

The readiness checker now validates the shape and consistency of adopted
structural evidence, including the rendered-contents status. Historical audits
without either new marker remain exempt; an evidence row does not prove that
all boundaries were reviewed or that the editorial judgement is sound.

## Notation hierarchy conflict

The GLM structural review found that notation rule N1 required a literal `##`
heading, although the user requested notation within the introduction and
several established primers use a `### Notation` subsection. The rule now
permits either location while retaining the requirement to introduce notation
before mathematical use. This resolves a conflict in guidance; it does not
itself approve any specific primer outline.

## Readiness-decision and independent fixture trials

On 23 November 2026, guidance revision `bb8dd577934fc41cc04c8bb9f52f501355cc99f8` added an integrated reader judgement and a requirement to state each open item's risk, evidence needed, owner and blocking or advisory disposition. The [failure ledger](primer-audit-failure-ledger-471.md) separates instruction conflicts, missing guidance and application failures. Two independent reviewers received only one fixture each and the revised skill; the author-defined answer key was withheld. Inputs and key are preserved under `maintenance/tests/fixtures/primer_audit_behaviour/`. These short controlled fixtures are not full-size primers or proof of general reliability.

- **Sample A:** the reviewer identified the reachable but semantically wrong citation, unsupported ready statement, fragmented definitions and late notation; retained the short reference and correctly found no omitted contents entry. They reported content and structural failure and release not-ready. They noted that a contents extract does not establish complete output or visual QA.
- **Sample B:** the reviewer identified the wrong citation target, omitted rendered heading and contradictory release claim, and differentiated a pending check from a failed measurement. They identified the fragmented definitions and notation order, and retained the short checklist. They reported content and structural failure and release not-ready. They also suggested a numerical residual example or narrower reader promise; that is an editorial judgement beyond the objective answer key.

A fresh `codex exec` session received an unnamed read-only audit request for sample A at the same guidance revision. Its event log shows it announced use of primer-audit and read `.agents/skills/primer-audit/SKILL.md`; it identified the wrong citation, fragmented teaching and unsupported readiness, correctly found the contents extract consistent, and reported content and structural failure and release not-ready. This is observed selection and skill reading for one session, not a separately recorded native activation event or proof of reliable selection. The temporary event log is `/tmp/primer-audit-trials-471/native-probe.jsonl`; the manual independent reviewer and this fresh session both used sample A, so they are not independent fixtures.

Real-primer calibration at `bb8dd57` produced useful findings but both reviewers stopped short of a complete source reading after output truncation. Each correctly reported incomplete scope and did not claim a complete review; neither resumed using smaller batches. The GLM reviewer initially raised a potential multinomial fitted-comparison gap, then retracted it after checking the brief: the requirement that both examples share a fitted dataset had been invented by the reviewer. The deep-learning reviewer identified the malformed rendered CNN parent and proposed several technical checks; these are review findings, not independently adjudicated conclusions. The initial brief did not communicate the user's preference for introductory notation, so its back-matter recommendation cannot test compliance with that preference. Subsequent instructions ask reviewers to continue in bounded batches and include that preference. Guidance was amended to instruct recovery from truncated reads; the amendment requires its own behavioural test. Neither real-primer trial authorises source changes or constitutes a release decision.

### Follow-up on truncated real-primer trials

After explicit follow-up instructions to read contiguous batches, the deep-learning reviewer reported reading source lines 1–1401 and the full HTML contents. With the user's introductory-notation preference supplied, they recommended moving the existing notation table into the introduction. They retained the structural failure for the malformed CNN heading and reported additional potential technical defects, including an asserted derivative claim. These claims require independent technical adjudication; the trial did not run examples, build or source-verification checks.

The GLM reviewer retracted the initially asserted multinomial blocker after comparing it with the brief. On resumption, they reported a structural pass while also admitting that source lines 1307–1308 had not been read. This contradicted the incomplete-reading rule and is a failed verdict-consistency observation. After a further explicit prompt, they read those lines, confirmed the earlier conclusion, and maintained release not-ready because semantic trace-cell and technical checks remained incomplete. Neither recovery demonstrates that the revised skill will autonomously resume after truncation: both reviewers were specifically prompted to do so. The revised skill now calls for bounded recovery and prohibits inventing a shared-dataset requirement; fresh independent tests of those refinements remain outstanding.

A second fresh unnamed-task `codex exec` session on sample B used guidance revision `6901c02`. Its event log shows it announced and read the primer-audit skill. It found the wrong citation target, omitted contents entry and contradictory release statement; it also proposed developing the residual-check example, treated the checklist as an action aid, and reported content and structural failure and release not-ready. This is a second observed skill selection on a different short fixture, not evidence that the truncation or shared-case refinements work on long documents. The temporary event log is `/tmp/primer-audit-trials-471/native-probe-b.jsonl`.

A fresh independent real-primer trial of revision `6901c02` identified the deep-learning contents defect and the user-specified notation placement, but stopped after truncated source/output inspection without attempting recovery. It correctly marked the structural gate not-checked and release not-ready, yet failed the required complete audit. This demonstrates that the earlier recovery instruction was insufficient in this trial. The workflow now calls for planning bounded contiguous reads before reading a long source and verifying range coverage; a further fresh trial is required.

### Recorded coverage and its limits

A further independent trial read the batching instruction but stopped after truncated output, explicitly attributing that decision to execution error rather than tool failure. Guidance alone has not proved sufficient. Audit schema 2 therefore records inclusive, revision-bound source-read ranges and the checker rejects missing, malformed, overlapping, out-of-bounds or incomplete coverage on a structural pass. Partial coverage can support a structural fail for an observed defect, or `not-checked`, but not release readiness. A Git-backed test checks complete coverage, a missing final two-line range, and revision mismatch.

The record is self-reported: a checker cannot prove the reviewer received, read or understood those lines. Legacy unversioned audits remain exempt, so omitting both the schema and coverage markers also bypasses enforcement for a new audit. The skill and template direct new audits to use schema 2, but the checker cannot distinguish an unversioned new audit from a historical one. A controlled behavioural trial that forces truncation and tests autonomous recovery remains outstanding; the unit tests validate recorded ranges, not the behaviour. Do not treat the workflow as fully reliable on long documents on this evidence.

A fresh unnamed-task long-primer session at guidance revision `8381326` selected and read the skill and issued seven contiguous source reads covering lines 1–1401; the event log recorded no truncation for those individual outputs. Its final answer nevertheless characterised its review as targeted and did not identify the known CNN heading missing from both published contents lists. It did identify the requested notation issue and other technical concerns, which remain unadjudicated. Complete source-output reads did not establish a correct source-versus-rendered outline comparison. The temporary event log is `/tmp/primer-audit-trials-471/native-long.jsonl`. This was an unforced-output trial, not the controlled truncation-recovery experiment still required.

### Advisory source-to-HTML comparison

The first comparator prototype treated Pandoc's shifted levels and numbered spans as differences, producing many false positives on real primers. After adaptation to the repository's HTML, `python3 -I maintenance/scripts/check/primer_outline_compare.py` reports the single missing CNN candidate at deep-learning source line 337 and no ATX H2/H3 candidate differences for the current GLM source and HTML. Independent review found a code-span false mismatch and an undisclosed inferred-offset limitation; code-span handling was corrected and the CLI now states its mapping and scope. Tests cover the observed rendering pattern and selected ambiguity cases. The comparator is advisory: inferred uniform level shifts can still hide a globally wrong hierarchy, deeper headings and complex Markdown are outside its complete coverage, and only human inspection of the actual contents and source establishes an editorial judgement. A fresh workflow trial after this addition remains to be assessed.

A fresh long-primer trial at `089851d` switched to the separate main checkout containing the input primer, where the draft comparator was unavailable; its attempted comparator invocation failed. The session nevertheless found the rendered CNN defect by direct inspection. The trial was interrupted after that observation and cannot establish end-to-end tool use. A subsequent trial must place the primer and draft workflow in the same checkout; this is a test-environment mismatch, not evidence that the comparator itself failed.

The corrected same-checkout fresh trial at `089851d` selected and read the skill, ran the comparator successfully, inspected the flagged source and all HTML variants plus PDF contents, and reported the CNN hierarchy defect and `Structural gate: fail`. Its final report also stated that its full source read was truncated and that it had not completed the whole-document review. It did not autonomously recover the missing coverage. This establishes successful comparator use and a justified observed structural failure for this one run, while repeating the unresolved long-read execution failure. The trial did not force a controlled truncation, did not edit the primer, and does not establish complete technical or content verification. The temporary event log is `/tmp/primer-audit-trials-471/native-long-same-tree.jsonl`.

### Controlled truncation tests

A tool-mechanics test used a deterministic 1,000-line fixture (SHA-256 `7db9d8875e61b219b456eb66a5466d7123f5c80dc59342c516366c968cc94530`). A deliberately constrained command response was truncated even though its first and last markers survived. Ten bounded reads reconstructed all 1,000 lines exactly. Checking only response boundaries would therefore have missed the omitted middle. This test demonstrates that recovery is possible in that environment; it does not test an auditor's judgement.

Three fresh Codex 0.171 sessions using `gpt-6.1-terra` at medium effort then audited a synthetic record through a controlled reader. Its first response deliberately omitted lines 31–970 and reported truncation; the initial prompt required that first broad read and explicitly instructed recovery. In the recovery case the session requested contiguous ranges, found the seeded test-set leakage at line 537, and reported full coverage. In the unavailable case every retry failed; the session attempted smaller ranges, reported lines 31–970 unchecked, and said the review was incomplete. A 20-line untruncated control was reviewed without unnecessary recovery. No follow-up prompt was given in these sessions.

These are narrow behavioural observations: the truncation was produced by a synthetic reader, the recovery instruction was in the task prompt, and neither the skill nor a real primer was tested.

A further fresh session selected and read the skill without being asked and was given a scoped audit of the real 1,401-line deep-learning source. Its prompt required use of a controlled reader, whose first response signalled and omitted lines 41–1361, but did not instruct recovery. The session detected the omission and requested ranges covering the source. It then reported that combined recovery outputs were truncated, gave only partial reviewed ranges and correctly reported the structural gate not-checked and release not-ready. It did not retry the remaining gaps even though the reader supported further requests. The event log records individual bounded outputs with the requested final lines and no literal truncation marker, but does not establish what combined output the model saw; it cannot confirm or disprove the reported combined-output truncation. The source was read from the main workspace while the skill was in the draft worktree, so the input was not bound to that worktree's revision. This is another failure to complete recovery, not a full primer audit. The skill was subsequently amended to request and inspect one batch per tool call and to retry missing intervals after interrupted recovery; this amendment needs a fresh test.

The controlled prompts, readers, fixtures and event logs were saved under `/tmp/primer-audit-trials-471/`; that temporary location is not durable evidence. Neither the earlier real-primer failure nor the latest simulated-omission failure is resolved by the successful synthetic sessions. A successful test of the amended workflow and independent evidence of real tool-output handling are needed before claiming this failure mode is reliably handled.

On 24 November, a fresh session tested the amended skill against the same source through a reader bound to the guidance checkout. The prompt asked for a scoped audit, required the initial broad read, and did not instruct recovery. The session read the skill, recognised the forced omission, and inspected selected ranges; it reported an attempted combined read as truncated and explicitly limited its assessment, with structural gate not-checked and release not-ready. It did not attempt full recovery. Because the request expressly allowed a scoped audit, this is inconclusive as a test of the required complete-audit recovery behaviour, rather than a demonstrated violation of the whole-document gate. The source SHA-256 was `bf7e2f2e512791eb602ff316837869fe45ce34e2e3a5a480927397616e9dff94`; guidance checkout HEAD was `eead11bf9eb37539a5beb9f2ccd902d0645e3cb6` with the amended skill uncommitted. The temporary prompt, reader and event log are `prompt-real-bound.txt`, `primer-reader-bound.py` and `session-real-single-batch.jsonl` under `/tmp/primer-audit-trials-471/`. A fresh trial should request a complete audit while leaving the recovery instruction to the skill.

Two further fresh sessions received that complete-audit request without a recovery instruction. The first reported complete coverage through delegated readers, but the parent event log did not expose their individual reads; this does not independently establish their coverage. The second was instructed to work alone, selected and read the amended skill, recognised the reader's simulated omission and requested ten individual contiguous ranges covering lines 1–1401. The event log records every requested line in the corresponding output, with no truncation indication. It found the known CNN contents defect and reported outstanding release checks. This is one successful controlled recovery using the actual source, not a full release audit or proof of general reliability: the initial truncation was simulated, a received range does not prove comprehension, and the task did not supply the user's introductory-notation preference. The prompts and event logs are `prompt-real-complete.txt`, `session-real-complete.jsonl`, `prompt-real-single.txt` and `session-real-single.jsonl` in the same temporary directory. Independent evidence for recovery from genuine tool-layer truncation remains outstanding.

Another fresh single-reviewer session was asked to begin with `cat` of the actual source and then perform a complete read-only audit, without a recovery instruction in the prompt. It reported that the initial tool response was truncated, selected the skill, and issued seven separate contiguous `sed` reads covering lines 1–1401; the event log contains the complete outputs of those reads. It ran the heading comparator, identified the CNN defect and reported unperformed release checks. The event log also retains the full initial command output, so it cannot independently establish exactly what portion was delivered to the model; the observation of truncation is the session's report. This is encouraging evidence of recovery from a reported native tool truncation, not independent proof of the tool's delivered payload or a guarantee of reliable behaviour. The temporary prompt and log are `prompt-native-complete.txt` and `session-native-complete.jsonl`. The task again omitted the user's notation preference and did not constitute a release audit.

### Independent spectral graph theory trial

On 24 November a fresh, single-reviewer session received a complete read-only structural and explanatory audit request for the spectral graph theory primer. The prompt stated that notation belongs within the introduction before first use and that major sections need substantive explanation; it did not identify the known malformed heading. Guidance checkout HEAD was `799aab9fa1ae9afbb015707590b5ec0476cd8ba4`; the source's last commit was `8190dd96003c11d6ed91a419c0aa50f3ff54591d`, and its SHA-256 was `37a27a61a40eeb81bb3c35253de5be4483a92c1529ff5f8b01db9c017ed4cf7c`.

The session selected and read the audit skill and requested the source in nine contiguous batches covering lines 1–2251; the event log contains all numbered lines in those outputs, without a recorded truncation marker. It ran the advisory heading comparison, recognised the missing rendered portfolio heading at line 1122 and the unmet introductory-notation requirement, and reported structural fail and release not-ready. It correctly distinguished placement from a symbol-before-definition defect, which it did not establish. Its section-by-section assessment described teaching threads and retained several deliberately short reference branches; it suggested case landmarks as editorial improvements, not automatic blockers.

The reviewer also identified a possible promise-to-evidence gap at lines 1015–1021: the perturbation ledger says it records a parameter experiment but describes what such a ledger should record without presenting the promised values. Inspection of those passages confirms that mismatch; its formal content-gate consequence remains undecided without a tracked brief and full route audit. This independent trial supports the observed structural and reader-scale behaviour in one additional real primer. It does not prove that every section or technical claim was understood or checked, and it did not conduct full technical, source, visual or release verification. It did not establish notation behaviour without an explicit user requirement. Its prompt and event log are `prompt-spectral-independent.txt` and `session-spectral-independent.jsonl` under `/tmp/primer-audit-trials-471/`; these temporary files are not durable evidence. No primer changes are authorised by the trial.

### Revision-bound semantic evidence trial

A fresh single-reviewer session independently assessed three primary concept rows (`kg-boundary`, `kg-mentions` and `kg-extraction`) and three Q4 transition rows in the knowledge-graph audit. The prompt named the rows and requested comparison with the brief, source and case inputs, decisions, outputs and limitations; it did not identify the anticipated source-role ambiguity or table-header locators. The source revision was `5924434d90d25eba7360d78172d74b21365462c6`, the brief `kg-398-brief-r13` and the audit `kg-398-depth-audit-r18`. The reviewer selected and read the audit skill and limited its conclusion to this sample.

The reviewer traced the two-source Q4 comparison through the answer and the controlled bad-answer repair without inventing a case break. It qualified the audit's phrase “admit R1/M1/D1”: D1 supplies identity and affiliation context, not a third Q4 applicability assertion. It identified three example locators that point to table headers rather than the worked rows immediately following them, and supplied the relevant row ranges. The significance of a header locator depends on the repository's locator convention; a header is not itself the worked action. It also distinguished the prose's illustrative semantic refusals from what the companion's narrow pattern implementation demonstrates, and did not claim that it had executed the companion. The source-role qualification and header positions were independently checked during calibration. These observations support the semantic and continuity review of this small real sample; they do not establish that other rows, the whole primer, or the companion execution have been verified. The temporary prompt and event log are `prompt-semantic-independent.txt` and `session-semantic-independent.jsonl` under `/tmp/primer-audit-trials-471/`.

### Closing-journey depth trials

On 24 November, user feedback challenged the GLM audit's retention of the
closing sections at source `46bcfa4`. The existing reasoning asserted that
the sections were bounded without demonstrating whether their development was
adequate. A first independent scoped trial of an uncommitted guidance revision
inspected source lines 1325–1440 and the heading inventory. It cited passages
and compared boundaries, but retained the exercises without examining whether
they practise the synthesis as a complete decision. This was a behavioural
failure, not a validation of the revision.

After further instruction to test a concrete reader action, a fresh reviewer
examined source lines 1280–1440 and the outline. The revised skill SHA-256 was
`5868a36eb830a03f5a3b1463c681992f262af36d47aecb5d5c23502dc814fcce`.
The reviewer identified that the combined exercise supplies no new diagnostic
or score evidence for a model-selection decision, while treating this as an
advisory opportunity because the brief and whole source were outside the
trial. It retained the section boundaries and reported the structural gate
not-checked. This is useful partial detection, not a validated whole-document
audit or evidence that all closing-section depth issues were found. Neither
trial inspected rendered contents, checked the brief or executed examples;
both were explicitly scoped and manually directed to the revised skill. They
do not establish native activation or reliable generalisation to other primers.

### Whole-source GLM and contrasting Pi editorial trials

Two independent reviewers were manually directed to the revised skill at
`3f43392` and asked to examine complete sources and their reader promises,
without seeing the current audit. The GLM reviewer received an inadvertent
truncated tail of the brief's evidence section, describing build, link and
accessibility status but no visible editorial finding or content verdict. The
trial is therefore non-blind. The reviewer reported receiving GLM source lines
1–1440 in twelve contiguous batches without truncation, and inspected the
committed HTML contents as text. The source was last changed at `46bcfa4`;
its SHA-256 was `29e0923b94c1e824412b6d51541d1b6d8de419b43f4aae8d86f5dbcb7a6cd5d3`.

The GLM reviewer identified that exercises 1423–1425 repeat the numerical
inputs and answers at 1188, 1211 and 1251/1261, weakening independent transfer,
and that the practice does not require choosing and justifying an end-to-end
revision on new evidence. The coordinator checked these three repetitions in
the source. The reviewer retained the synthesis and reference boundaries as
substantive for their stated jobs, with possible synthesis expansion; that does
not resolve the user's concern about the depth and organisation of the ending.
A separate closing assessment also proposed more explicit boundary-recognition
and solution steps. The trial detected a specific important weakness, but did
not establish that all the provisional closing assessment's concerns were
found or that an absence of further gaps is verified.

The second reviewer reported reading Pi coding-agent source lines 1–1082 in
six contiguous batches and its brief, without reading its audit or rendered
contents. The source was last changed at `c193c88` and its SHA-256 was
`1a8edd490e0f3fb58f864a89da5a3d15b5fb3320aa2e20c7dd471a90e0fd0`.
The reviewer found that the first-run example creates an untracked README at
131–135, then asks for `git diff` at 143–151; the coordinator confirmed the
instructions, and Git does not show an untracked file's contents in a normal
diff. The reviewer also identified an ambiguity: the contract at 784–787
requires exact extrema, but the comparator description at 840 names only keys,
counts and mean in its parenthetical. It also says to compare each row with the
expected file, so this is not proof that an actual comparator omits extrema;
the example does not supply that implementation. The reviewer retained the
short glossary and closing perspective as useful references and proposed moving
the comparison section; that placement is an editorial judgement, not a
verified defect.

Both trials were editorial, not full technical, source, execution, visual or
release audits. Historical reconciliation was intentionally excluded; neither
proves native skill activation or behaviour on every primer. The Pi findings
are review candidates, not changes or a fresh readiness decision for that
primer. These observations support further use of the guidance with human
adjudication, but do not establish reliable detection of all depth or
structural issues. Retain the distinction between a useful finding, an
unresolved interpretation and a demonstrated repair.

### Reader-outcome trial on historical GLM source, 26 November

A fresh single reviewer was manually directed to the amended audit skill at
`94acd9d` (skill SHA-256
`29d6db7c0ee95b558f415809c762a546fe9659a3c6bb9253477e7c7b723510df`).
The prompt requested a complete read-only editorial audit of a supplied primer
and brief, required bounded source reads and reported ranges, and excluded the
existing audit, calibration and failure ledger. It did not name the closing
findings or proposed fixes. The reviewer was `gpt-6.1-terra` at medium effort.
The source was taken from commit `46bcfa4` (SHA-256
`29e0923b94c1e824412b6d51541d1b6d8de419b43f4aae8d86f5dbcb7a6cd5d3`);
the supplied brief from that commit had SHA-256
`a37fb3f6925209f6259499856c6e2c35831a97fdb91eb6f421d534b490b11f1b`.
The reviewer correctly observed that the brief records a different source hash.
Its historical gate statements were also visible. Consequently this is blind
to the specific closing findings, not to the earlier overall verdict, and its
source/brief revision binding is not valid evidence of a release audit.

The reviewer reported untruncated contiguous source coverage 1–1440 in twelve
120-line batches. The coordinator received the reviewer result but did not
retain a raw event log, so the ranges are reviewer-reported, not independent
proof of delivery or comprehension. Manual direction to read the skill does
not establish native activation. The reviewer identified the absence of a
fresh staged diagnostic-to-revision exercise, repeated values and limited
intermediate feedback (source lines 1361–1379, 1400–1408 and 1423–1440),
explained the consequence for independent transfer, and recommended expansion.
It distinguished this gap from the substantive worked case. It gave content
fail, structural not-checked because rendered contents were unavailable, and
release not-ready. These observations are consistent with the earlier closing
assessment; the test was not scored as having found every proposed improvement.

The reviewer retained specialist boundaries as reference material and did not
identify the separate opportunity to practise recognising which boundary fits a
new observation. It did not independently check calculations, render outputs,
links, source identity, examples or every concept row. The trial demonstrates
one useful detection under partial blindness, not reliability across primers or
proof that the new boundary-recognition instruction was effective. A second
trial should use a revision-matched brief without prior verdicts and preserve
safe observable output under the durable evidence format in #484.

A second fresh manual-skill trial used the same historical source and an
explicitly prepared reader-and-scope excerpt of `glm-brief-v11` with the correct
source identity and no historical gate verdict. The full brief and case contract
were not supplied. The safe prompt, exact excerpt and input hashes are retained
in [the trial record](primer-audit-trial-2026-11-26.md). The reviewer reported
coverage of lines 1–1440 in twelve batches, found the repeated inputs and lack
of unfamiliar staged decision practice, and correctly declined a full content
gate because the complete brief and route matrix were unavailable. It retained
the specialist section as a reference and did not identify the separate
boundary-recognition practice opportunity. Structural gate was not-checked
because outputs were not supplied; release remained not-ready. The excerpt was
derived for the trial rather than a complete revision-bound brief, and received
ranges remain reviewer-reported. This independent run supports detection of the
practice problem under a verdict-free prompt, but repeats the boundary-detection
miss and does not establish general reliability or native skill activation.

### Revised boundary instruction and independent spectral trial

Two more fresh manually directed reviews used skill commit `9c56ea6` (skill
SHA-256 `a141d8d65c1ed06e3f410cc6f45fd23272bbf57efb33984e386d7f9c6c250eb9`).
On the historical GLM source and the same incomplete, verdict-free excerpt,
the reviewer again found repeated values and missing staged practice. This
reviewer also tried a concrete count-versus-continuous-cover recognition task,
cited source passages and judged the distinction supported; it mentioned little
applied unfamiliar-case feedback. That observation shows use of the new
instruction, but does not independently settle the earlier assessment that
boundary recognition needed more development. The reviewer did not propose the
same boundary exercise and did not have the complete brief. Record this as a
partial detection and editorial disagreement, not a clear pass or false positive.

A second reviewer examined the 2,251-line spectral graph theory primer (source
SHA-256 `37a27a61a40eeb81bb3c35253de5be4483a92c1529ff5f8b01db9c017ed4cf7c`)
and its HTML contents, with an explicit introductory-notation requirement. It
reported contiguous source coverage, found the missing rendered portfolio
heading at line 1122 and the unmet notation requirement, and identified weak
exercise feedback as a scoped editorial concern. It also reported two advisory
comparator false positives caused by smart apostrophe typography, at source lines
432 and 1944; both headings appeared in the HTML contents. The tracked brief was
not available and examples, technical claims and release checks were not run.
The reviewer reported structural fail and release not-ready. This real-primer
trial is an additional observed use, not proof of general reliability. Reviewer
coverage is self-reported; raw tool-event logs were not retained. Prompts and
adjudication limits are recorded in the accompanying trial record.

At comparator commit `e742854`, prose apostrophes are matched across straight
and typographic forms. The spectral comparison then reports only the missing
portfolio heading. Apostrophes inside code spans are flagged as ambiguous for
human review rather than silently treated as equivalent. Regression tests use
both affected spectral headings, an omitted-heading control and literal-code
cases. This corrects the observed false positives; it does not establish that
other typographic or Markdown forms are handled exhaustively. The independently
identified spectral practice-feedback issue is recorded as #486.

### Fresh Codex selection trial

A fresh unnamed-task Codex session at `2688081` announced use of the audit
skill, read its file and ran the outline comparator. The recorder retained nine
contiguous source-read outputs matching all 2,251 spectral-primer lines, and
the final review found the missing rendered heading, stated notation problem,
practice-feedback gap and perturbation-ledger gap. This is one encouraging
natural-selection observation on a previously used primer, not a general
reliability or genuine-truncation test. The exact prompt, hashes, observable
actions and evidence boundaries are in the [native trial record](primer-audit-native-trial-2026-11-26.md).
The raw event file was not retained as a reviewed tracked artefact; recorded
outputs do not prove comprehension or the exact payload delivered to the model.

A second unnamed-task Codex trial at `fcd58e9` read the audit skill and all
1,082 Pi source lines in six recorder-verified output batches, but described its
first-session control loop as sound without identifying the untracked README
and ineffective `git diff` inspection already recorded in #473. It reported a
separate possible gap in the illustrative Rocker project, whose significance
requires the unavailable brief; it also omitted an explicit structural-gate
label. This is a substantive miss and gate-reporting miss, not a reliable
pass. The exact prompt, observed actions, result hashes and limits are retained
in [the native trial record](primer-audit-native-trial-2026-11-26.md).
