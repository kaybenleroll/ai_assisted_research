# Primer teaching-case contract: Generalised linear models and their extensions

- Issue and milestone: #468 primer; #467 planning.
- Case revision: glm-case-v5
- Source revision: 8417dba1d9183041213115f6361d84107ae40109
- Source SHA-256: 27d68fb0fdb9686588bf349404a88764702ae405e1d96cfc99f05d85f19cef07
- Reader capability: construct and assess a model from observed units to prediction, diagnosis, revision and limits.
- Case purpose: link sampling and estimand to distribution, design, fit, uncertainty and revision.
- Case boundary: the cumulative simulated count case, Gamma companion, other synthetic cases and real penguin and package-derived Salamanders studies are distinct datasets.

The independent complete content reading covered source SHA-256 `84eba056acb9ed85f3f0586b36555887bb4729de0178c62e1d27d91c92bb7e95` at commit `858f4ef29e6e85ef50acbc3231ccc639a27a1b99`. The only subsequent source changes, verified in the Git diff to `8417dba1d9183041213115f6361d84107ae40109`, add inline style attributes to two existing compatibility spans; prose and line positions are unchanged. The independent reviewer did not reread the full source at the new hash. The recorded current revision and concept-row evidence revisions bind the preserved content judgement and this delta inspection to the current source; they do not claim a new independent full read.


## Combined count trace

The author ran the combined R fit and fixed-input R/Python/Julia prediction checks in pinned isolated containers, including training diagnostics; the independent reviewer read the complete preceding source and independently integrated the fixed prediction fixture. The reviewer did not refit the model. The current full 23-entry manifest subsequently passed in the pinned runtimes; that execution is separate from the independent reviewer’s checks.

| Stage | Input, operation and result | Mode and evidence | Limit |
|---|---|---|---|
| Input and split | primer_glm/primer_glm.md:1088: seed 4682026, 72 sites, four visits, known effort and nonlinear NB2 truth; 54 training and 18 test sites | executable; author ran | simulated truth is not empirical evidence |
| Model and diagnostic | primer_glm/primer_glm.md:1096: Poisson, NB, site and smooth fits; training residual bins, zero, tail and site-total checks | executable; author ran; independent prose review | site-total result does not identify site dependence; checks are plug-in and finite simulation |
| Repair and re-evaluation | primer_glm/primer_glm.md:1110: inspect patterns, compare candidates and scores for the same held-out new sites | executable; author ran | one split; test reuse and model-selection limits |
| Prediction | primer_glm/primer_glm.md:1132: integrate one shared site effect; compare means, [0,6] predictive interval and joint score | executable fixed-input R/Python/Julia; independent fixed-fixture integration | fitted-parameter and smoothing uncertainty omitted; no Python/Julia refit |
| Boundary | primer_glm/primer_glm.md:1138: evaluate remaining discrepancy and observation process | illustrative review | detection, causation and biological zero states not identified |

## Gamma companion trace

| Stage | Input, operation and result | Mode and evidence | Limit |
|---|---|---|---|
| Input and construction | primer_glm/primer_glm.md:565: 400 synthetic Gamma observations, seed 222468; 250 train and 150 test | executable; author reported | separate simulation |
| Fit and discrepancy | primer_glm/primer_glm.md:567: intercept-only then gradient mean | executable; author reported | simulated truth is known |
| Compare and interpret | primer_glm/primer_glm.md:573: held-out scores and intervals | executable; author reported | same-target comparison, one split |
| Correction and boundary | primer_glm/primer_glm.md:579: remaining undercoverage despite mean repair | illustrative independent review | no claim of general calibration |

## Teaching decisions

Author executions and independent content reading are distinct. Mathematical explanations are illustrative review evidence even where companion scripts ran. Specialised GLMM, GAM, zero, categorical and posterior algorithms are R-first; the combined three-language check compares predictions at fixed fitted inputs. Real studies are observational and do not identify detection or causation. Source and outputs are bound to the recorded commit; final release checks remain pending.
