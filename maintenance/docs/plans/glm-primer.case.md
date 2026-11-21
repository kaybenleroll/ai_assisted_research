# Teaching-case contract: Generalised linear models and their extensions

- Issue and milestone: #467, planning; primer drafting is a subsequent milestone.
- Case revision: `glm-case-v2`.
- Baseline revision: `e03baa554ff96cad286efb9caf32c9d82c9d6f4d`.
- Reader capability: construct, fit, interpret, check and revise a statistical
  model, explaining what each component contributes and what the data cannot
  establish.
- Case purpose: connect the conditional distribution, mean, link, predictor,
  estimation and uncertainty through visible modelling decisions. Extensions
  arise from problems encountered in that process.
- Case boundary: an explicitly simulated ecological monitoring programme is
  the continuous teaching spine. Separate real studies provide external
  applications; they are not represented as observations from that programme.
  A simulated mechanism is known by construction, not established empirically.
- State at 21 November 2026 snapshot: feasibility inputs are frozen and selected
  probes and analyses have run. No primer examples manifest, finished teaching
  prose, complete route suite, publication output or independent audit exists.
  Detailed identities, hashes, commands and outputs are in
  [the feasibility record](glm-primer.feasibility.md) and its linked scratch
  reports.

## Trace

| Stage | Description | Evidence or artefact | Status |
|---|---|---|---|
| Source inputs or assumptions | Declare survey units, sites, repeat visits, environmental covariates, survey effort, response support and the observation process. Distinguish detection from occupancy and recorded counts from abundance. | Simulation specification remains to be drafted. Frozen penguin CSV and pinned package-derived Salamanders CSV with upstream source metadata and hashes are recorded in the evidence file. | Two real feasibility inputs selected and frozen; original Dryad byte identity is not established or required. BBS is not selected and its archive was not downloaded. |
| Construction and transformation | Build an auditable analysis table, describe exclusions and missingness, encode categorical predictors and interactions, and preserve denominators, effort, grouping and time. | Penguins: 344 rows, 2 missing body masses and 11 missing sexes; 342-row mass fit and 333-row complete-sex subset. Salamanders: 644 package rows and explicit R-to-CSV conversion; one GP subset has 92 rows across 23 sites and four visits. | Feasibility preparation and assertions passed; final reader-facing transformation ledger and frozen tracked inputs remain to be produced. |
| Intermediate representation | Show the design matrix, offsets, linear predictor, inverse-link mean and conditional variance for named observations. | Fixed-design R/Python/Julia comparisons cover Gaussian, Bernoulli, Poisson with offset and Gamma; fixed-theta NB2 compared across R/Python/Julia and task-local statsmodels. | Preliminary agreement on benign, full-rank fixed designs. Python and Julia core translations are explicit algorithms, not independent production packages. |
| Computed result | Build likelihood, score and curvature; show a fitting iteration; fit the complete model and inspect convergence and identifiability. | Existing base runtime probes pass. Limited R extension spikes and pinned baseline fits on penguins and Salamanders are recorded with scripts and outputs. | Preliminary feasibility only; no full example suite, advanced package verification, full diagnostics or independent analysis audit. |
| Reader-facing operation | Produce predictions and contrasts on meaningful scales, with separate treatment of uncertainty in the mean and variation in new observations. | Baseline fitted means and a single exploratory row/site split for Salamanders are recorded; penguin model predictions and design-rank checks are recorded. | Illustrative outputs only. No plots or reader-facing uncertainty displays have been audited. |
| Interpretation | Explain coefficients, probability changes, rate ratios and positive-response effects; compare substantive conclusions rather than only fit statistics. | Worked interpretation with units, reference levels and estimand stated. | Planned; observational associations do not establish causation. |
| Failure or boundary | Introduce overdispersion, separation, dependence, nonlinear structure, extra zeros, missingness or observation bias in separate controlled examples. | Diagnostic plots, deliberately misspecified fits, and a record of what each diagnostic can establish. | Planned; do not combine all failure mechanisms into one opaque dataset. |
| Correction and re-evaluation | Change the relevant mean, variability, dependence or observation assumption; refit and recheck predictions and uncertainty using an appropriate validation split. | Before/after modelling ledger, held-out results and remaining-limit statement. | Planned; improved fit does not prove a biological mechanism. |

## Feasibility snapshot and limits

The 21 November evidence snapshot is a planning input, not a release gate
report. Palmer penguins is the positive-response/categorical case. The pinned
CSV is the authors' curated package data at commit
`8957207b78d6ccd1b4654a9dd9c9041b657478ab`, SHA-256
`f204db2c753b0937caac3cb35258562c14f073e4bbc76be24b4c51ce22767a93`; authors
declare CC0 and request contact about analysis/collaboration, recorded without
claiming contact or treating the request as a CC0 condition. Salamanders uses
the glmmTMB package object at commit
`c311085c19a50af9a8e930352885313897333b7f`, SHA-256
`cca69c7eb8488d7932217ccc623a815105eb3e522f4debcb1841342c31bfc389`, converted
to CSV with SHA-256
`1dadca43a8c917da58cd341fb04f15c0ad22384a8487a33dc3f6b77516bf8874`. Carry
both requested citations, Dryad CC0 metadata and the package's AGPL-3 declaration
with explicit derived-data provenance. The original Dryad file API returned
401 and a further landing-page stream request returned 403; the package copy is
usable as such, with no byte-identity claim.

The repository images' existing offline probes pass: Python 3.12.15 with
NumPy 2.3.3/SciPy 1.16.2/Matplotlib 3.10.6; R 4.5.3 with base `stats`, MASS,
mgcv and torch; Julia 1.12.7 with ForwardDiff 0.10.39 and Zygote 0.7.10. The
R/Python/Julia fixed-design fits agree closely on four core families. A separate
fixed-theta NB2 check also agrees within 5.93e-7, including a separately built
task-local statsmodels image whose dependencies are pinned but not hash-locked.
No shared runtime was modified. Existing R extension spikes demonstrate limited
execution support, not production adequacy. Advanced package-layer results
remain pending final integration by the main/model worker.

Penguin feasibility compared Gaussian/identity and Gamma/log models on the
same 342 mass records and a 333-row sex-complete subset. Salamander feasibility
compared Poisson and MASS NB2 fits for prespecified GP counts; its independent
row and held-site single splits are illustrative only. Site visits are
dependent; these fits do not estimate occupancy, abundance or causal effects.
Neither model comparison establishes adequacy or selects a final model.

## Teaching decisions

- Small examples are hand-worked first where that makes the mechanism clear.
  Explain the input, calculation, output, interpretation and limitation.
- The simulation spine has distinct branches: binary detection, counts with
  effort, positive continuous measurements, site-level heterogeneity, smooth
  environmental effects, and explicit mixture or hurdle processes. These are
  labelled constructions, not an asserted single biological law.
- Real examples revisit the same modelling stages with actual measurement,
  sampling and missingness constraints. Do not invent an effort variable or
  a trial denominator that the source did not record.
- R is the primary teaching implementation. Main examples also have Python and
  Julia implementations. Software differences are teaching material; package
  feature gaps must be resolved through a verified alternative implementation
  or a scope decision agreed before the affected chapter is drafted.
- Freeze shared input tables for cross-language checks. Compare design
  matrices, parameter definitions, fitted means, predictions and compatible
  likelihoods before comparing printed coefficients or significance values.
  Account for contrast coding, dispersion, likelihood constants, integration
  approximations, priors and interval definitions.
- Simulations carry random-seed and generation specifications. Stochastic
  inference requires convergence and Monte Carlo uncertainty checks; a fixed
  seed alone does not establish a correct result.
- Quasi-likelihood specifies a mean–variance relationship rather than a full
  sampling distribution. Generate its motivating data from an explicit
  distribution and do not pretend to simulate from a quasi-family alone.
- Every substantial extension has a full teaching spine: problem, mechanism,
  worked application, interpretation and material limit. More examples must
  add understanding rather than repeat an unexplained command sequence.
- Exercises include outline solutions and span calculation, model choice,
  interpretation, debugging and critique.

## Evidence and acceptance

Assign executable example IDs during implementation and map them to the
brief's stable route and concept IDs. Record exact commands, pinned runtime
and dependency versions, input provenance, expected outcomes and tolerances.
Label examples as planned, illustrative, parsed or executed according to the
evidence actually available.

Review the full input-to-conclusion trace for each taught route. Confirm that
the text explains how intermediate results feed the next stage; passing code
does not establish that the prose teaches the connection. Include correction
and re-evaluation when a diagnosed failure can be addressed, and state when a
different data design or model class is required.

Real-data acceptance requires a source citation, version or retrieval date,
documented reuse terms, units, sampling design, identifiers, missing-value
definitions and transformation history. A software package's code licence
does not by itself settle the rights for every bundled dataset.

The content gate and publication gate remain separate. After drafting, bind
the brief and audit to the actual source revision, render HTML/PDF using the
repository's pinned containers, execute the agreed examples and inspect
representative figures, equations, tables and code layouts. No such checks
have been performed at this planning stage.
