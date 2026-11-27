# Primer audit: Deep Learning and Generative AI

- Issue and milestone: #482; depends on #476 / PR #516.
- Audit revision: `482-audit-draft-v1`.
- Audit schema: 2
- Source revision: `00ca2852502230a3099fe874d2c255e4e42be18e`
- Tracked path: `primer_deep_learning/issue-482-audit.md`.
- Starting branch: `docs/482-deep-learning-audit`.
- Reviewer(s): Codex.
- Date: 2026-11-27.
- Reviewed revision: `00ca2852502230a3099fe874d2c255e4e42be18e`
- Historical review: the full continuous pre-revision read was at `bda64e7666f2c228de6f12b87c9beeaa36831076`; a subsequent continuous reread covered lines 1–1424 at `538fa40`, with lines 1–184 carried from the identical pre-correction text and lines 185–200 reread after that correction; the changed passages at the current revision have been sampled but have not received a complete audit.
- Brief reviewed: `primer_deep_learning/issue-482-brief.md`, `482-brief-v1`.
- Readiness decision: not-ready
- Review boundary: Full source read and provisional outline decisions at the pre-revision revision; changed passages and numeric arithmetic sampled after revision. Source claims, all route transitions, and post-change outline and depth gates remain incomplete.
- Teaching-case contract: Separate mathematical worked threads and an explicitly illustrative decision case are planned in the brief.
- Core-concept depth matrix: Brief `482-brief-v1`; rows below are deliberately not checked until post-change review is completed.

## Whole-document review

The pre-revision observations, boundary proposals, exact locators, independent counterexamples and sources are in `issue-482-review-proposal.md`. The post-change revision corrects three identified mathematical problems, adds worked explanations and moves notation, but those changes do not establish that all routes meet the brief. VAE sampling and pathwise-gradient claims were qualified in the revisions through `00ca285` using [Kingma and Welling](https://arxiv.org/abs/1312.6114), section 2.2–2.3; WGAN-GP was checked against [Gulrajani et al.](https://arxiv.org/abs/1704.00028), section 4, and recurrent Jacobian bounds against [Pascanu et al.](https://arxiv.org/abs/1211.5063), section 2. These are scoped checks, not complete reviews. The universal approximation activation hypothesis was checked against [Leshno et al.](https://archive.nyu.edu/handle/2451/14329) and corrected with a quadratic counterexample. The BERT corruption probabilities and DDPM final-noise rule were checked against the [BERT paper](https://arxiv.org/abs/1810.04805), section 3.3, and [DDPM](https://arxiv.org/abs/2006.11239), Algorithm 2. LoRA parameter counts were recalculated; the DDPM batch broadcast was executed in the isolated `localhost/primers-python-torch:2.14.1` runtime for a `(3, 2, 4, 4)` tensor and per-image coefficients 0.9, 0.7 and 0.5. SentencePiece and byte-level BPE claims were checked against the [SentencePiece paper](https://arxiv.org/abs/1808.06226), section 3, and [byte-level BPE paper](https://arxiv.org/abs/1909.03341), sections 2–3; the text no longer says all tokenisation is lossy or BPE requires whitespace splitting. WordPiece details, model-choice recommendations, training costs and other time-sensitive claims still require source-backed adjudication. The example scenario contains hypothetical results, not empirical measurements. Code snippets remain illustrative.

## Outline and hierarchy review

- Source read coverage: none
- Rendered contents: **not-checked** for the full post-change outline; the opening PDF contents and notation page were sampled.

The full read recorded in the proposal applies to `bda64e7`, not the changed source. A fresh continuous reader review and explicit boundary/child decisions at `00ca285` are required. Moving notation preserves its `notation` HTML fragment and the parent chapter numbering, but this does not prove interactive navigation.

## Adversarial depth gate

All nine primary concepts below remain not-checked; no route passes until its transitions and limitations have been reviewed.

## Core-concept depth matrix

| route_id | route tier | concept_id | explanation locator | example/action locator | interpretation locator | limitation locator | evidence revision | reviewer | status | finding | scope decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| foundations | primary | network_update | primer_deep_learning.md:202 | primer_deep_learning.md:263 | primer_deep_learning.md:263 | primer_deep_learning.md:263 | 00ca2852502230a3099fe874d2c255e4e42be18e | Codex | gap | Scalar update is checked but no numerical multilayer example carries the stated forward route through the weight update. | retain pending review |
| spatial | primary | cnn_features | primer_deep_learning.md:371 | primer_deep_learning.md:383 | primer_deep_learning.md:408 | primer_deep_learning.md:446 | 00ca2852502230a3099fe874d2c255e4e42be18e | Codex | not-checked | Output size and parameters are worked; broad CNN-versus-ViT claims need source review. | retain pending review |
| recurrent | primary | state_gradients | primer_deep_learning.md:536 | primer_deep_learning.md:566 | primer_deep_learning.md:566 | primer_deep_learning.md:582 | 00ca2852502230a3099fe874d2c255e4e42be18e | Codex | gap | Scalar state trace does not calculate a gated cell path; surrounding long-range claims need review. | retain pending review |
| attention | primary | attention_weights | primer_deep_learning.md:704 | primer_deep_learning.md:716 | primer_deep_learning.md:716 | primer_deep_learning.md:716 | 00ca2852502230a3099fe874d2c255e4e42be18e | Codex | not-checked | Numeric lookup checked; attention scaling assumptions and whole route need review. | retain pending review |
| language | primary | language_training | primer_deep_learning.md:885 | primer_deep_learning.md:922 | primer_deep_learning.md:946 | primer_deep_learning.md:910 | 00ca2852502230a3099fe874d2c255e4e42be18e | Codex | gap | BERT and LoRA fixes checked; WordPiece training description and tokenisation claims need verification. | retain pending review |
| variational | primary | elbo | primer_deep_learning.md:1006 | primer_deep_learning.md:1010 | primer_deep_learning.md:1018 | primer_deep_learning.md:1066 | 00ca2852502230a3099fe874d2c255e4e42be18e | Codex | not-checked | Jensen bridge sampled; the complete route and limits still need independent review. | retain pending review |
| adversarial | primary | wasserstein | primer_deep_learning.md:1098 | primer_deep_learning.md:1106 | primer_deep_learning.md:1104 | primer_deep_learning.md:1110 | 00ca2852502230a3099fe874d2c255e4e42be18e | Codex | not-checked | Constraint corrections sampled; the complete GAN comparison remains to be reviewed. | retain pending review |
| diffusion | primary | score | primer_deep_learning.md:1126 | primer_deep_learning.md:1154 | primer_deep_learning.md:1173 | primer_deep_learning.md:1173 | 00ca2852502230a3099fe874d2c255e4e42be18e | Codex | not-checked | Broadcast executed; score bridge and reverse sampler need full independent review. | retain pending review |
| selection | primary | model_choice | primer_deep_learning.md:1367 | primer_deep_learning.md:1409 | primer_deep_learning.md:1409 | primer_deep_learning.md:1409 | 00ca2852502230a3099fe874d2c255e4e42be18e | Codex | gap | Scenario now supplies numerical illustrative outcomes; categorical recommendations and cost minima still need sources and conditions. | retain pending review |

The listed passages were inspected for the indicated roles; the entries labelled as limitations are provisional where they discuss a concern without establishing every promised boundary. Further semantic review of the full passages and input-to-result transitions is required before changing any status. A primary `not-checked` row blocks content readiness.

## Route transition evidence

The following placeholders mark unreviewed transitions, not verified teaching. Complete each route from input to interpreted result and limit before readiness.

| route_id | concept_id(s) | transition (from to) | linked input and reader operation | intermediate reasoning or decision | result | interpretation | material limitation | execution status | gap and reader consequence |
|---|---|---|---|---|---|---|---|---|---|
| foundations | network_update | scalar input to loss update | x=2, w=0.5, y=3 at line 263 | derive gradients and use learning rate 0.1 | w=0.9, b=0.2, loss 0.5 | loss falls on this example | one scalar layer and one step | executed | No numerical multilayer transition to match the earlier model. |
| spatial | cnn_features | image shape to feature map | 5 by 5 input and 3 by 3 kernel at lines 383–407 | apply output-size rule and shared weights | 3 by 3 output and 1,792-parameter multi-channel example | parameter sharing reduces the kernel parameters | padding and architecture affect spatial output | illustrative | Numerical kernel values and competing-model claims not checked. |
| recurrent | state_gradients | sequence to state | h0=0, inputs 1 and 0 at line 566 | apply tanh recurrence twice | states 0.762 then 0.363 | initial input influence attenuates | one scalar parameter choice | executed | No worked gated-cell update connecting gates to a retained contribution. |
| attention | attention_weights | query and keys to output | q=1, keys 0 and log 3, values 2 and 10 at line 716 | softmax of the two scores | weights 1/4 and 3/4, output 8 | second value dominates; q=0 gives 6 | chosen scalar projections | executed | Full transformer route and scaling assumptions not independently verified. |
| language | language_training | tokens to adaptation | tokenisation and BERT objective at lines 890–929 | corrupt selected positions and predict originals | contextual representations; low-rank adaptation at lines 938–946 | training objective shapes model use | tokenizer and model assumptions differ | illustrative | No end-to-end worked input through objective and adaptation; WordPiece claim unresolved. |
| variational | elbo | marginal to lower bound | joint density and variational posterior at lines 1000–1018 | insert posterior and apply Jensen | ELBO and KL gap | reconstruction and regularisation terms | support and tractability assumptions | illustrative | Independent full derivation and transition review still required. |
| adversarial | wasserstein | distributions to critic | real and generated distributions at lines 1096–1111 | optimise approximate critic with sampled gradient penalty | critic objective and generator signal | distance estimate is approximate | sampled penalty does not establish a global constraint | illustrative | No concrete distribution pair and numeric critic comparison. |
| diffusion | score | clean sample to noise estimate | x0 and noise at lines 1124–1161 | construct xt and predict sampled noise | per-image coefficients and noise estimate | score is conditional expected noise scaled at line 1173 | finite network approximates optimum | executed | Broadcast only executed; score derivation and full training transition not independently reproduced. |
| selection | model_choice | inspection data to model comparison | 2,000 labelled images and explicit thresholds at line 1409 | compare validation recall, false alarms and target-device latency | 75%, 95% and 90% recalls with stated constraints at line 1411 | compressed candidate meets thresholds provisionally | hypothetical results and shift risk; test set remains untouched | illustrative | Cost table and categorical recommendations elsewhere remain unverified. |

## Verification and readiness

At `00ca285`, pinned `just deep-learning-all`, `just render-qa primer_deep_learning`, targeted offline links, spelling, Markdown and prose checks completed on the changed inputs. Prose reports five existing advisories. The scalar update, recurrence and attention arithmetic were independently recalculated; a non-symmetric Jacobian finite-difference counterexample is documented in the proposal. PDF visual samples were taken on an immediately preceding build, including pages 1, 14, 34, 41, 46, 54–56, 69 and 79–80; after the notation move page 5 was rechecked, and after the later changes pages 19–20 and 57–62 were rechecked, including both sides of affected page breaks; the universal approximation correction was checked on preceding-build pages 14–16. At `00ca285`, changed regions and page breaks were inspected on pages 16–18, 44–45, 49–52 and 63–65; after tokenizer changes pages 47–49 were inspected; the subsequent scenario was inspected on pages 78–80. These are targeted samples, not an exhaustive inspection of the final 80-page PDF. Other pagination on the final build must be rechecked against the changed source. PDF metadata reports `Tagged: no`.

The browser service returned no available browser during the parent work; keyboard, no-JavaScript, accessibility-tree and screen-reader checks were not performed. Full claims verification, executable framework examples, whole-document post-change review, semantic locator check and `just primer-audit` are not complete. The preliminary brief also needs its full case trace and post-draft checkpoint reconciled.

- Structural gate: **not-checked**
- Content gate: **fail** (primary routes remain not-checked).
- Release readiness: **not-ready**.
