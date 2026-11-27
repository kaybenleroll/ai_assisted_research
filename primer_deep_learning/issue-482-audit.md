# Primer audit: Deep Learning and Generative AI

- Issue and milestone: #482; depends on #476 / PR #516.
- Audit revision: `482-audit-draft-v1`.
- Audit schema: 2
- Source revision: `69dfd2b661df7b78eb74eabae6171a79cc460e11`
- Tracked path: `primer_deep_learning/issue-482-audit.md`.
- Starting branch: `docs/482-deep-learning-audit`.
- Reviewer(s): Codex.
- Date: 2026-11-27.
- Reviewed revision: `69dfd2b661df7b78eb74eabae6171a79cc460e11`
- Historical review: the full continuous pre-revision read was at `bda64e7666f2c228de6f12b87c9beeaa36831076`; a subsequent continuous reread covered lines 1–1424 at `538fa40`, with lines 1–184 carried from the identical pre-correction text and lines 185–200 reread after that correction; the changed passages at the current revision have been sampled but have not received a complete audit.
- Brief reviewed: `primer_deep_learning/issue-482-brief.md`, `482-brief-v1`.
- Readiness decision: not-ready
- Review boundary: Full source read and provisional outline decisions at the pre-revision revision; changed passages and numeric arithmetic sampled after revision. Source claims, all route transitions, and post-change outline and depth gates remain incomplete.
- Teaching-case contract: Separate mathematical worked threads and an explicitly illustrative decision case are planned in the brief.
- Core-concept depth matrix: Brief `482-brief-v1`; rows below are deliberately not checked until post-change review is completed.

## Whole-document review

The pre-revision observations, boundary proposals, exact locators, independent counterexamples and sources are in `issue-482-review-proposal.md`. The post-change revision corrects three identified mathematical problems, adds worked explanations and moves notation, but those changes do not establish that all routes meet the brief. VAE sampling and pathwise-gradient claims were qualified in the revisions through `69dfd2b` using [Kingma and Welling](https://arxiv.org/abs/1312.6114), section 2.2–2.3; WGAN-GP was checked against [Gulrajani et al.](https://arxiv.org/abs/1704.00028), section 4, and recurrent Jacobian bounds against [Pascanu et al.](https://arxiv.org/abs/1211.5063), section 2. These are scoped checks, not complete reviews. The universal approximation activation hypothesis was checked against [Leshno et al.](https://archive.nyu.edu/handle/2451/14329) and corrected with a quadratic counterexample. The BERT corruption probabilities and DDPM final-noise rule were checked against the [BERT paper](https://arxiv.org/abs/1810.04805), section 3.3, and [DDPM](https://arxiv.org/abs/2006.11239), Algorithm 2. LoRA parameter counts were recalculated; the DDPM batch broadcast was executed in the isolated `localhost/primers-python-torch:2.14.1` runtime for a `(3, 2, 4, 4)` tensor and per-image coefficients 0.9, 0.7 and 0.5. Tokenisation, model choice, training costs and other time-sensitive claims still require source-backed adjudication. The example scenario contains hypothetical results, not empirical measurements. Code snippets remain illustrative.

## Outline and hierarchy review

- Source read coverage: none
- Rendered contents: **not-checked** for the full post-change outline; the opening PDF contents and notation page were sampled.

The full read recorded in the proposal applies to `bda64e7`, not the changed source. A fresh continuous reader review and explicit boundary/child decisions at `69dfd2b` are required. Moving notation preserves its `notation` HTML fragment and the parent chapter numbering, but this does not prove interactive navigation.

## Adversarial depth gate

All nine primary concepts below remain not-checked; no route passes until its transitions and limitations have been reviewed.

## Core-concept depth matrix

| route_id | route tier | concept_id | explanation locator | example/action locator | interpretation locator | limitation locator | evidence revision | reviewer | status | finding | scope decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| foundations | primary | network_update | primer_deep_learning.md:202 | primer_deep_learning.md:261 | primer_deep_learning.md:261 | primer_deep_learning.md:261 | 69dfd2b661df7b78eb74eabae6171a79cc460e11 | Codex | not-checked | Full route and dependent transitions not re-audited | retain pending review |
| spatial | primary | cnn_features | primer_deep_learning.md:361 | primer_deep_learning.md:385 | primer_deep_learning.md:405 | primer_deep_learning.md:442 | 69dfd2b661df7b78eb74eabae6171a79cc460e11 | Codex | not-checked | Locators and route not semantically rechecked | retain pending review |
| recurrent | primary | state_gradients | primer_deep_learning.md:526 | primer_deep_learning.md:564 | primer_deep_learning.md:576 | primer_deep_learning.md:580 | 69dfd2b661df7b78eb74eabae6171a79cc460e11 | Codex | not-checked | Changed Jacobian and state path need full review | retain pending review |
| attention | primary | attention_weights | primer_deep_learning.md:700 | primer_deep_learning.md:714 | primer_deep_learning.md:714 | primer_deep_learning.md:714 | 69dfd2b661df7b78eb74eabae6171a79cc460e11 | Codex | not-checked | Worked arithmetic sampled; route not fully audited | retain pending review |
| language | primary | language_training | primer_deep_learning.md:881 | primer_deep_learning.md:900 | primer_deep_learning.md:920 | primer_deep_learning.md:960 | 69dfd2b661df7b78eb74eabae6171a79cc460e11 | Codex | not-checked | Claims and locators need verification | retain pending review |
| variational | primary | elbo | primer_deep_learning.md:1008 | primer_deep_learning.md:1010 | primer_deep_learning.md:1016 | primer_deep_learning.md:1058 | 69dfd2b661df7b78eb74eabae6171a79cc460e11 | Codex | not-checked | Derivation sampled; full transition needs review | retain pending review |
| adversarial | primary | wasserstein | primer_deep_learning.md:1098 | primer_deep_learning.md:1104 | primer_deep_learning.md:1110 | primer_deep_learning.md:1110 | 69dfd2b661df7b78eb74eabae6171a79cc460e11 | Codex | not-checked | Constraint correction needs independent review | retain pending review |
| diffusion | primary | score | primer_deep_learning.md:1168 | primer_deep_learning.md:1168 | primer_deep_learning.md:1168 | primer_deep_learning.md:1168 | 69dfd2b661df7b78eb74eabae6171a79cc460e11 | Codex | not-checked | Conditional expectation derivation needs independent source review | retain pending review |
| selection | primary | model_choice | primer_deep_learning.md:1360 | primer_deep_learning.md:1404 | primer_deep_learning.md:1404 | primer_deep_learning.md:1404 | 69dfd2b661df7b78eb74eabae6171a79cc460e11 | Codex | not-checked | Illustrative scenario and strong surrounding recommendations need review | retain pending review |

These line references are candidates, not verified semantic mappings; review every locator and the input-to-result, interpretation and limit transitions before changing any status. A primary `not-checked` row blocks content readiness.

## Route transition evidence

The following placeholders mark unreviewed transitions, not verified teaching. Complete each route from input to interpreted result and limit before readiness.

| route_id | concept_id(s) | transition (from to) | linked input and reader operation | intermediate reasoning or decision | result | interpretation | material limitation | execution status | gap and reader consequence |
|---|---|---|---|---|---|---|---|---|---|
| foundations | network_update | input to interpretation | Not yet reviewed | Not yet reviewed | Not yet reviewed | Not yet reviewed | Not yet reviewed | not-checked | Reader path remains unverified |
| spatial | cnn_features | input to interpretation | Not yet reviewed | Not yet reviewed | Not yet reviewed | Not yet reviewed | Not yet reviewed | not-checked | Reader path remains unverified |
| recurrent | state_gradients | input to interpretation | Not yet reviewed | Not yet reviewed | Not yet reviewed | Not yet reviewed | Not yet reviewed | not-checked | Reader path remains unverified |
| attention | attention_weights | input to interpretation | Not yet reviewed | Not yet reviewed | Not yet reviewed | Not yet reviewed | Not yet reviewed | not-checked | Reader path remains unverified |
| language | language_training | input to interpretation | Not yet reviewed | Not yet reviewed | Not yet reviewed | Not yet reviewed | Not yet reviewed | not-checked | Reader path remains unverified |
| variational | elbo | input to interpretation | Not yet reviewed | Not yet reviewed | Not yet reviewed | Not yet reviewed | Not yet reviewed | not-checked | Reader path remains unverified |
| adversarial | wasserstein | input to interpretation | Not yet reviewed | Not yet reviewed | Not yet reviewed | Not yet reviewed | Not yet reviewed | not-checked | Reader path remains unverified |
| diffusion | score | input to interpretation | Not yet reviewed | Not yet reviewed | Not yet reviewed | Not yet reviewed | Not yet reviewed | not-checked | Reader path remains unverified |
| selection | model_choice | input to interpretation | Not yet reviewed | Not yet reviewed | Not yet reviewed | Not yet reviewed | Not yet reviewed | not-checked | Reader path remains unverified |

## Verification and readiness

At `69dfd2b`, pinned `just deep-learning-all`, `just render-qa primer_deep_learning`, targeted offline links, spelling, Markdown and prose checks completed on the changed inputs. Prose reports five existing advisories. The scalar update, recurrence and attention arithmetic were independently recalculated; a non-symmetric Jacobian finite-difference counterexample is documented in the proposal. PDF visual samples were taken on an immediately preceding build, including pages 1, 14, 34, 41, 46, 54–56, 69 and 79–80; after the notation move page 5 was rechecked, and after the later changes pages 19–20 and 57–62 were rechecked, including both sides of affected page breaks; the universal approximation correction was checked on preceding-build pages 14–16. At `69dfd2b`, changed regions and page breaks were inspected on pages 16–18, 44–45, 49–52 and 63–65. These are targeted samples, not an exhaustive inspection of the final 80-page PDF. Other pagination on the final build must be rechecked against the changed source. PDF metadata reports `Tagged: no`.

The browser service returned no available browser during the parent work; keyboard, no-JavaScript, accessibility-tree and screen-reader checks were not performed. Full claims verification, executable framework examples, whole-document post-change review, semantic locator check and `just primer-audit` are not complete. The preliminary brief also needs its full case trace and post-draft checkpoint reconciled.

- Structural gate: **not-checked**
- Content gate: **fail** (primary routes remain not-checked).
- Release readiness: **not-ready**.
