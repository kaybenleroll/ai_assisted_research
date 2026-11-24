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
each top-level boundary and rendered contents inspected; report the structural
gate `not-checked` and release `not-ready` if required coverage is incomplete.
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
