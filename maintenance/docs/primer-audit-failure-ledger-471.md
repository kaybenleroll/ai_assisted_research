# Primer audit failure ledger for #471

This ledger records observed failures and bounded remedies, not a finding that
any primer is ready. The companion [calibration report](primer-outline-calibration-471.md)
records the trials and revisions. Scratch reports cited below were local working
evidence on 23 November 2026 and may not be retained; commit IDs and the
examples reproduced here identify the relevant observations.

## Notation hierarchy

**Classification: conflicting instruction.** The former N1 required a literal
`## Notation`, conflicting with the user's requested introductory subsection.
The GLM structural proposal reviewed source `8417dba1d9183041213115f6361d84107ae40109`
and records this conflict. Guidance commit `6a4000f` permits notation inside the
introduction or at top level, before first mathematical use. The later
[maths notation guide](math-notation.md) retains the first-use requirement.

**Measurable remedy:** check the actual heading hierarchy and first mathematical
use for each affected primer, and record the user's placement requirement and
its disposition. Test both permitted hierarchies against N1. The rule change is
not approval of an individual outline, and this ledger does not claim such a
test has been run.

## Closing-section purpose mistaken for sufficient depth

**Classification: application and evidence-design failure.** The GLM audit at
`d929bea` retained its synthesis, specialist boundaries and exercises using
labels such as “bounded” and “distinct purpose”, without showing that the
closing journey gave readers enough developed reasoning or practice. A
separate challenge repeated the conclusion. The content and structural passes
were subsequently withdrawn at `808c5ba`. Distinct jobs are real but do not
establish sufficient depth.

**Bounded remedy:** cite the reader tasks and passages on both sides of a
boundary, compare a meaningful alternative where relevant, and test the
reader's next action against an actual opportunity and feedback or explain why
these are not promised. Record unsupported transfer and its consequence. The
two scoped trials and their limits are in the calibration report. They do not
establish reliable whole-document behaviour.

## Truncated or fragmentary structural review

**Classification: application failure; prior instruction sufficiency is
uncertain.** The first blinded GLM manual trial provisionally passed structure
after a truncated read and missed known issues. A later independent trial
identified notation placement, a lone child and missing case landmarks; it
initially marked the incomplete review `not-checked`, then read the full source
and contents. Its editorial judgement did not override the user's explicit
requirement. The calibration report documents both trials and their limits.

**Measurable remedy:** record the reviewed revision, contiguous source ranges,
each top-level boundary and rendered contents inspected. If required coverage
is incomplete, report the structural gate `fail` when a structural defect has
already been confirmed; otherwise report it `not-checked`. In either case,
report release readiness as `not-ready` and identify the unreviewed scope.
The [audit skill](../../.agents/skills/primer-audit/SKILL.md) now states these
gates. A complete read does not itself prove sound editorial or technical
judgement. The later spectral review's recorded contiguous ranges 1–2251 are an
example of coverage evidence, not proof of a full technical audit.

## False locators and disconnected cases

**Classification: missing explicit semantic-remapping instruction followed by
application failure.** For GLM source `0245c0356ecd5fb33d94f46ae8eac3ebf133ba58`,
brief `glm-brief-v6` and audit `glm-content-audit-v4` passed mechanical shape and
locator-existence checks, although subsequent review found real passages that
did not support their labelled claims. The local `glm-locator-recheck.md`
records, for example, c16's action at line 697 as merely `n <- 400`, with the
simulation and fit spanning lines 693–716. Guidance commit `ab7bcd9` requires
semantic checks of retained or moved locators. A subsequent correction at
`e25c409` still joined separate cases: the resumed handover identifies r03's
binomial, Poisson and interaction passages as distinct, and r08's conjugate
count and logistic cases as distinct. A set of individually relevant passages
does not establish a continuous case. These are historical findings, not a
claim about the current GLM audit.

**Measurable remedy:** inspect every retained and changed explanation, action,
interpretation and limitation cell against its named role at the bound source
revision. For each route trace the actual case identity and input-to-result
transitions; split distinct cases, or mark an unsupported transition `gap` or
`not-checked`. Record reviewer, revision, locators and outcome, then run the
mechanical checks separately. Independent review of corrections must include
case continuity, not just locator existence. No checker pass establishes
semantic accuracy, and the observations do not establish an exhaustive content
or technical review.

## Pending work and claims of exhaustive verification

**Classification: uncertain as a general instruction failure; reporting and
verification risk demonstrated.** The shutdown handover recorded content fail
pending technical review, and distinguished a historical full review from a
targeted review of changed prose. It also reported eight inaccessible DOI links;
the later local `glm-source-followup.md` checked only those eight and explicitly
did not claim a complete source or full-text audit. The resumed handover says
new-head CI might still be pending and that the correction required independent
review. These scoped records do not establish that every pending claim elsewhere
was vague, or that the remaining work was completed.

**Measurable remedy:** replace an unqualified `pending` or `verified` with the
specific artefact and revision, scope, method, observed result, unresolved
items and next check. For an exhaustive claim, enumerate the population and
account for each item, including inaccessible and not-checked items; otherwise
state the sample and its limits. Distinguish old successful checks from checks
on the current head. No amount of reporting converts an unavailable source or
unperformed check into a pass.

## Workflow activation

**Classification: application behaviour; cause of incomplete outputs is
uncertain.** The calibration report distinguishes a manual skill read from
native selection. In fresh unnamed-task synthetic trials, the first selected the
skill but gave an incorrect release decision, the second omitted the explicit
structural-gate label, and a third selected the workflow and reported both
required labels after clarification. The third was a retry on the same fixture,
not an independent demonstration of general reliability.

**Measurable remedy:** preserve separate evidence for catalogue discovery,
native selection and skill read, and substantive application. In a fresh,
unnamed-task probe record the event log, exact skill revision, fixture and both
gate labels, including failure or omitted labels. Repeat on an independent
fixture before making a broader reliability claim. Manual application and a
single successful retry do not establish reliable native activation.

## Pagination changes and visual sampling

**Classification: visual sampling gap; broader reliability unproven.** In the
GLM draft PR #470, the PDF at output revision `117083d` passed render QA and a
sampled visual review, but a later independent wider sample found Figure 7
between two parts of an R listing on pages 66–67. The sampled pass did not
establish that other page boundaries were sound. Output revision `72b5b19`
flushes deferred figures before code; a reviewer inspected the affected pages
and a wider sample, with a figure-only page and whitespace still recorded.

**Remedy:** after changes that can repaginate a document, widen the sample and
inspect both sides of affected code and figure page breaks. Record the output
revision, pages, result and remaining scope. This directly addresses the
observed blind spot; the additional prose and equation cases below refine the
sampling guidance but do not establish exhaustive visual coverage.

### Calibrated visual-sampling trial, 26 November 2026

A fresh reviewer was manually instructed to apply the then-current render-QA
guidance to the GLM PDF at SHA-256
`29f4ea649855957255c84f3ffcff68e9020ccd36b589a425120830270b74400b`. The
sample covered pages 1, 6, 16–20, 47–49, 58–60, 71–73, and 82–83. The reviewer
detected a figure splitting the introduction and equation on pages 16–17, and
sentence interruptions on pages 58–59 and 82–83, but missed the known code
listing interruption on pages 66–67. Those target pages were not in the
sample. The trial therefore supports adding prose and equation floats to the
boundary checks, while showing that the sampled review still missed a known
defect.

The reviewer was manually instructed; native skill selection was not tested.
No raw event logs were retained, and the shared filesystem did not enforce
blinding. This is one bounded observation, not evidence that the guidance
caused the detections or miss, nor a reliability or exhaustive-coverage claim.
The trial does not assess or establish the outcome of any pagination fix.
Pages outside the listed sample remain uninspected.

The manually supplied skill was the render-QA skill at `c763201`, SHA-256
`49a5e63e10956c3bd84763d4dd3cc9fa0459b10aaa6d2d8d62b105d7bfb22af1`.
The reviewer was a fresh `gpt-6.1-terra` medium subagent. Its prompt asked it
to apply that skill and the review checklist to the supplied PDF after a
whole-document pagination change, choose representative pages and transitions,
report pages, SHA, material defects and limits, and avoid other repository
files, history, audits, PRs, conversation and memory. No source, brief or HTML
was supplied. This is the recorded task description, not a retained tool-event
transcript; the shared environment could not enforce those exclusions.
