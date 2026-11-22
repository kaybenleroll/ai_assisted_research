# Primer teaching-case contract: Generalised linear models and their extensions

- Issue and milestone: #468 draft; #467 planning.
- Case revision: glm-case-v3
- Source revision: e77fa0721fe4a062e7219aa3e068e00adcc6ab66
- Source SHA-256: f6487efe39fa5f66aa97c8a1c401c0b8750b013204ac1af39e0cda72adf29da5
- Reader capability: construct and assess a model from observed units to interpreted prediction, diagnosis, revision and explicit limitations.
- Case purpose: link sampling and estimand to distribution, design, fit, uncertainty and revision.
- Case boundary: the continuous teaching spine is a simulated Gamma/log positive response; distinct synthetic count, grouping, zero and categorical mechanisms and real penguin and package-derived Salamanders studies are explicitly separate. Known simulation truth is not empirical truth.

## Trace

| Stage | Description | Evidence or artefact | Status |
|---|---|---|---|
| Source inputs or assumptions | 400 independent Gamma observations, mean exp(1+1.1x), shape 4, seed 222468 | primer_glm/primer_glm.md:405; examples/core-repairs.R | Executed by author in pinned R; independent reviewer inspected prose, did not rerun |
| Construction or transformation | First 250 train, 150 held out | primer_glm/primer_glm.md:405 | Executed by author; fixed split applies only to this independent simulation |
| Intermediate representation | Gamma/log intercept-only versus x predictor | primer_glm/primer_glm.md:407 | Executed by author; same outcome and target for both fits |
| Stored or computed result | Baseline residual pattern and revised fit | primer_glm/primer_glm.md:407 | Executed by author; simulated truth known |
| Reader-facing operation | Predict held-out observations and compare scores and coverage | primer_glm/primer_glm.md:409 | Executed by author; 89.3% coverage remains a warning |
| Interpretation | Parametric bootstrap mean and future observation at x=0.8 | primer_glm/primer_glm.md:411 | Executed by author; 500 refits and model assumptions limit tail precision |
| Failure mode or scope limit | Remaining undercoverage, fitted-distribution assumptions, independent simulation | primer_glm/primer_glm.md:409 | Illustrative independent prose review; no real-data validity claim |
| Correction and re-evaluation | Add x and check the same held-out target; identify incomplete interval repair | primer_glm/primer_glm.md:407 | Author executed; independent content re-review retained scientific limitation |

## Teaching decisions

- Executable stages: `core-repairs-r`; the targeted runner was reported passed, and this independent reviewer did not rerun it. The case has no claim of validated real-data prediction.
- Illustrative stages: independent content-review interpretation and mathematical explanation, despite prior author execution.
- Measured stages: synthetic held-out log score, coverage and bootstrap intervals are simulation results at the stated seed, not ecological measurements.
- Required alternatives: matched R/Python/Julia core, NB and fixed-penalty spline; extension examples are currently R-first and the agreed three-language main-example promise remains subject to release verification. Bounded methods are explicitly labelled.
- Expected abstentions: do not infer occupancy from non-detection, causation from association, model truth from a predictive check, or universal calibration from one split.
- Evidence and freshness: penguin and package-derived Salamanders source/rights in `primer_glm/data/README.txt`; historical independent review and scoped final re-review; final revision, link checks and outputs pending.

## Related case traces

The brief maps each route to input, decision, result, interpretation and limit. The Gamma spine does not claim the separately seeded count, hierarchical, zero-inflation and category examples are one ecological dataset. The observed-site/new-site GLMM example conditions on fitted parameters, and the real salamander mixed model remains a proposal. The ordinal and Bayesian simulation cases supply their own repair and sensitivity comparisons. See the audit for route-level locators and review provenance.

## Committed snapshot and language checks

The committed source/output snapshot is `e77fa0721fe4a062e7219aa3e068e00adcc6ab66`, source SHA-256 `f6487efe39fa5f66aa97c8a1c401c0b8750b013204ac1af39e0cda72adf29da5`. An independent reviewer retained the case judgement after layout-only repairs, without repeating the whole-source review or all executions. The author reports four passed targeted Python/Julia entries for the real penguin and Salamanders Poisson cases and conjugate count posterior; other specialised demonstrations remain R-only. These checks add concrete comparable operations and do not establish complete ecological, production or language parity. Release checks remain pending.
