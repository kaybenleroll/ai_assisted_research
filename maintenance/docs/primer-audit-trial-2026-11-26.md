# Primer Audit Trial: Historical GLM Reader Outcomes

## Trial and Inputs

- Date: 26 November 2026. Question: does the amended audit guidance detect a reader's missing opportunity to practise a promised model-building route?
- Guidance: audit skill at commit `94acd9d`, SHA-256 `29d6db7c0ee95b558f415809c762a546fe9659a3c6bb9253477e7c7b723510df`.
- Source: `primer_glm/primer_glm.md` at commit `46bcfa4`, SHA-256 `29e0923b94c1e824412b6d51541d1b6d8de419b43f4aae8d86f5dbcb7a6cd5d3`.
- Brief: `primer_glm/primer_glm.brief.md` at `46bcfa4`, SHA-256 `a37fb3f6925209f6259499856c6e2c35831a97fdb91eb6f421d534b490b11f1b`. Its declared source hash differs from the supplied source, and it includes historical gate statements. It does not include the specific subsequent closing findings. This is partial, not complete, blindness.
- Harness: a fresh single subagent, `gpt-6.1-terra` at medium effort. The skill was manually specified; native discovery or activation was not tested.

## Task Given to the Reviewer

> Perform a read-only editorial audit of the primer at `/tmp/audit-evaluation-2026-11-26/primer.md` against its brief `/tmp/audit-evaluation-2026-11-26/brief.md`. Apply the audit skill at `/tmp/ai-research-outline-review/.agents/skills/primer-audit/SKILL.md`, consulting its linked guidance in `/tmp/ai-research-outline-review` as needed. Assess the complete source for reader journey, section depth, practical transfer, structure and evidence; use bounded reads and record received line ranges. Do not read any existing primer audit, calibration or failure ledger, and do not change files or delegate. Report concrete findings with source locators, reader consequences, dispositions, explicit content/structural verdicts and unperformed checks. This is a research trial, not authorisation to publish. You are not alone in the workspace; preserve all work.

The paths were temporary copies of the Git-bound inputs above. The exact prompt
is retained here; the temporary copies and the reviewer's tool-event log are
not durable artefacts. The coordinator observed the returned review, not the
individual tool deliveries. No raw transcript or hidden reasoning is retained.

## Observed Result and Adjudication

The returned review reported source lines 1–1440 in twelve contiguous batches
without truncation. This is a reviewer report, not independently observed proof
of delivery or comprehension. The reviewer flagged the mismatched brief hash,
identified missing unfamiliar diagnostic-to-revision practice and feedback at
source lines 1361–1379, 1400–1408 and 1423–1440, and distinguished the gap
from the existing combined worked case. It reported content fail, structural
not-checked because rendered contents were unavailable, and release not-ready.
The coordinator compared those findings with the historical closing assessment;
they detect the central transfer issue and repeated-input concern.

The reviewer treated specialist boundaries as an appropriately bounded reference
and did not identify the distinct boundary-recognition practice opportunity.
This is a miss against the provisional assessment, not proof that every reader
must receive specialist fitting instruction. The reviewer did not independently
verify all calculations, sources, examples, outputs or route/concept cells.
The trial gives evidence of one useful editorial detection under partial
blindness; it does not establish native activation, reliable generalisation,
complete technical accuracy or a publication decision. A second trial needs a
source-matched, verdict-free reader brief and independently retained safe output.

## Second Trial: Verdict-Free Excerpt

A fresh independent `gpt-6.1-terra` medium reviewer received the same source and guidance, with the following explicitly incomplete reader-and-scope excerpt (SHA-256 `026b2a1ca44138309f42941ab6e1e32a7965c53c349667c1d033b72d594712c7`). The excerpt was prepared from the historical brief; it is not a replacement for the tracked complete brief.

```text
# Reader and scope excerpt from glm-brief-v11

This is an excerpt prepared for editorial evaluation, not the full tracked brief. Source under review: commit 46bcfa4, SHA-256 29e0923b94c1e824412b6d51541d1b6d8de419b43f4aae8d86f5dbcb7a6cd5d3.

- Reader: quantitatively literate ecological researcher or analyst who can read basic R.
- Prerequisites: algebra, logarithms, elementary probability, derivatives, vectors and basic regression.
- Problem and motivation: match ecological observations, design, distributions and inference while recognising limits of sampling and prediction.
- Intended outcome: build, interpret, diagnose and revise GLMs and taught extensions, with explicit prediction targets and limits.
- Scope: Gaussian, binomial, Poisson and Gamma GLMs, likelihood, IRLS, inference and diagnostics; quasi, NB, mixed models, smooths, zero models, categorical and Bayesian routes.
- Exclusions: complete causal, spatial, temporal, occupancy/detection and survival modelling; reference-only boundaries identify when to seek specialist methods.
- Proposed dependency-led route: regression and concrete response families, general fitting, inference and diagnostics, count extensions and combined case, categorical and Bayesian models, then synthesis and boundaries.
- Approximate depth: substantial worked explanations; no word-count ceiling.
- Worked examples: penguin and Salamanders studies and explicitly separate simulated core, Gamma, count, grouped, zero, categorical and Bayesian cases.
- Real-world cases: Palmer penguins and package-derived Salamanders; `primer_glm/data/README.txt` records provenance and observational limits.
- Teaching-case contract: primer_glm/primer_glm.case.md, glm-case-v5.
- Worked-case trace: route-keyed table below and combined/Gamma case contract.
- Core-concept depth matrix: this brief, glm-brief-v11.
- Route classification and teaching spines: primary, alternative and reference-only as listed below.

| r05 | Quasi and negative binomial | Inference vs predictive distribution; common overdispersed count simulation | Extra distributions or exhaustive alternative variance forms | Expand both: necessary contrasting mechanisms and real ecological use | R05 |
| r06 | Mixed effects | Repeated sites; known clustered simulation | Exhaustive multilevel computational theory | Expand fitting, group-specific and population-averaged estimands, new-group prediction and repair | R06 |
| r10 | GAM smooths | Nonlinear gradients; known smooth simulation with basis, penalty and REML | Exhaustive spline families | Expand fitting, uncertainty, concurvity and extrapolation; narrow advanced smoothing theory | R10 |
| r11 | Multinomial and ordinal outcomes | Unordered classes and ordered conditions; simulate, fit, compare and check proportional odds | Exhaustive categorical response model families | Expand both into substantive executable alternatives as a scope proposal; validate data and software before adopting | R11 |
| r07 | Hurdle and zero inflation | Separate scientific zero mechanisms; simulated competing processes | Exhaustive mixture taxonomy | Expand both; explicitly limit mechanism claims | R07 |
| r08 | Bayesian GLM | Explicit prior, uncertainty and separation; conjugate and executable regression | Full Bayesian computation theory | Expand practical workflow and diagnostics; restrict advanced hierarchical Bayesian models | R08 |
| r09 | Beta, Tweedie, detection, spatial/temporal and survival | Identify common failures and suitable next analysis; conceptual cases | Detailed fitting exercises for these topics | Reference-only: distinguish binomial proportions from continuous fractions in (0,1), for which beta regression may be suitable; a zero-plus-positive response may call for a Tweedie model or a two-part alternative. Full treatment needs separate likelihoods, diagnostics and case contracts; do not claim fitting competence or imply these are interchangeable one-parameter GLMs | R09 |
| r03 | Regularisation | Separation and high-dimensional instability; penalised binomial demonstration | Exhaustive tuning and penalty families | Expand focused demonstration; cross-validation and uncertainty limits, no general machine-learning course | R03 |
| r01 | Missingness, measurement and selection | Recognise selection/detection and state assumptions; counterexamples | Full multiple-imputation and causal identification tutorials | Expand design and consequences; narrow corrections to brief sensitivity guidance | R01 |
```

Exact prompt:

> Conduct a read-only editorial review of `/tmp/audit-evaluation-2026-11-26/primer.md` using the reader and scope excerpt `/tmp/audit-evaluation-2026-11-26/brief-excerpt.md`. Apply `/tmp/ai-research-outline-review/.agents/skills/primer-audit/SKILL.md` and relevant referenced guidance. Review the whole source in bounded contiguous batches; report covered ranges, concrete findings with locators, reader consequences, and your content/structure decisions and unperformed checks. The excerpt is not a complete tracked brief; scope your verdict accordingly. Do not inspect prior audits, calibration records, failure ledgers or conversation context, do not edit files or delegate. You are not alone; preserve other work.

The returned review reported source lines 1–1440 in twelve contiguous batches and found repeated worked inputs and missing unfamiliar staged diagnosis-to-prediction practice, citing source lines 1402, 1423–1425 and 1430. It made the content-blocking consequence conditional on the unavailable complete brief, retained the specialist section as reference material, and did not identify boundary-recognition practice as a separate issue. It reported structure not-checked and release not-ready because the rendered contents and other checks were not supplied. No raw tool-event log was retained; source coverage is reviewer-reported and manual skill use does not establish native activation. The excerpt matches the supplied source identity but does not provide complete route tiers, concepts or case contract. This trial supports a narrow detection observation, not a full audit or a general reliability claim.
