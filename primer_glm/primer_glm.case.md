# Primer teaching-case contract: Generalised linear models and their extensions

- Issue and milestone: #468 primer; #467 planning.
- Case revision: glm-case-v6
- Current source revision: 0ff4b2599d01cfd6ddff260f98fbb5bfba954d32
- Current source SHA-256: a9ee8afb265930574bdaa1025396f5023f21fe5dbff0ecc5607a0418e33340a1
- Reader capability: construct and assess a model from observed units to prediction, diagnosis, revision and limits.
- Case purpose: link sampling and estimand to distribution, design, fit, uncertainty and revision.
- Case boundary: the cumulative simulated count case, Gamma companion, other synthetic cases and real penguin and package-derived Salamanders studies are distinct datasets.

The current source binding is the reachable squash-merge commit `0ff4b25`; its source blob and SHA-256 match reviewed branch commit `190d12d`. This does not claim a new review.

The independent complete content reading covered source SHA-256 `84eba056acb9ed85f3f0586b36555887bb4729de0178c62e1d27d91c92bb7e95` at commit `858f4ef29e6e85ef50acbc3231ccc639a27a1b99`. A span-only delta was subsequently inspected at `8417dba1d9183041213115f6361d84107ae40109`. The source changed further after that point. The [audit](primer_glm.audit.md) records the later scoped reviews, including the correction at the source revision above; it does not claim a new independent whole-document technical review at that revision. The trace locators below were reconciled semantically to that source for this case update; this is not a new execution or independent content review.

## Combined count trace

The author ran the combined R fit and fixed-input R/Python/Julia prediction checks in pinned isolated containers, including training diagnostics; the independent reviewer read the complete preceding source and independently integrated the fixed prediction fixture. The reviewer did not refit the model. The current full 23-entry manifest subsequently passed in the pinned runtimes; that execution is separate from the independent reviewer’s checks.

<!-- current locators: start -->

| Stage | Input, operation and result | Mode and evidence | Limit |
|---|---|---|---|
| Input and split | primer_glm/primer_glm.md:1105 and primer_glm/primer_glm.md:1111: seed 4682026, 72 sites, four visits, known effort and nonlinear NB2 truth; 54 training and 18 test sites | executable; author ran | simulated truth is not empirical evidence |
| Model and diagnostic | primer_glm/primer_glm.md:1113 and primer_glm/primer_glm.md:1117: Poisson, NB, site and smooth fits; training residual bins, zero, tail and site-total checks | executable; author ran; independent prose review | site-total result does not identify site dependence; checks are plug-in and finite simulation |
| Repair and re-evaluation | primer_glm/primer_glm.md:1129 and primer_glm/primer_glm.md:1137: inspect patterns, compare candidates and scores for the same held-out new sites | executable; author ran | one split; test reuse and model-selection limits |
| Prediction | primer_glm/primer_glm.md:1155–1159: integrate one shared site effect; compare means, [0,6] predictive interval and joint score | executable fixed-input R/Python/Julia; independent fixed-fixture integration | fitted-parameter and smoothing uncertainty omitted; no Python/Julia refit |
| Boundary | primer_glm/primer_glm.md:1161: evaluate remaining discrepancy and observation process | illustrative review | detection, causation and biological zero states not identified |

<!-- current locators: end -->

## Gamma companion trace

<!-- current locators: start -->

| Stage | Input, operation and result | Mode and evidence | Limit |
|---|---|---|---|
| Input and construction | primer_glm/primer_glm.md:582 and primer_glm/primer_glm.md:599: 400 synthetic Gamma observations, seed 222468; 250 train and 150 test | executable; author reported | separate simulation |
| Fit and discrepancy | primer_glm/primer_glm.md:584–586: intercept-only then gradient mean | executable; author reported | simulated truth is known |
| Compare and interpret | primer_glm/primer_glm.md:588–590: held-out scores and intervals | executable; author reported | same-target comparison, one split |
| Correction and boundary | primer_glm/primer_glm.md:591–592: remaining undercoverage despite mean repair | illustrative independent review | no claim of general calibration |

<!-- current locators: end -->

## Teaching decisions

Author executions and independent content reading are distinct. Mathematical explanations are illustrative review evidence even where companion scripts ran. Specialised GLMM, GAM, zero, categorical and posterior algorithms are R-first; the combined three-language check compares predictions at fixed fitted inputs. Real studies are observational and do not identify detection or causation. The source binding above identifies the version used for these locators; the audit records the separate output, execution and sampled visual evidence. PR #507 merged on 27 November 2026; its release evidence and remaining advisory accessibility and online-link limitations are recorded in the audit. This case update adds no new release assessment.
