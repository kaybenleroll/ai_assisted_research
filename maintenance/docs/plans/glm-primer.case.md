# Teaching-case contract: Generalised linear models and their extensions

- Issue and milestone: #467, planning; primer drafting is a subsequent milestone.
- Case revision: `glm-case-v1`.
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
- State: planned only. No dataset has been frozen, example executed or result
  validated for this new primer.

## Trace

| Stage | Description | Evidence or artefact | Status |
|---|---|---|---|
| Source inputs or assumptions | Declare survey units, sites, repeat visits, environmental covariates, survey effort, response support and the observation process. Distinguish detection from occupancy and recorded counts from abundance. | Simulation specification with named parameters; separately, source records and data dictionaries for each real study. | Planned; real-data selections require provenance and reuse checks. |
| Construction and transformation | Build an auditable analysis table, describe exclusions and missingness, encode categorical predictors and interactions, and preserve denominators, effort, grouping and time. | Shared input files and transformation ledger; hand-worked rows beside code. | Planned; no data processing performed. |
| Intermediate representation | Show the design matrix, offsets, linear predictor, inverse-link mean and conditional variance for named observations. | Small numerical tables and diagrams; matched R, Python and Julia core examples. | Planned; definitions must be harmonised before comparisons. |
| Computed result | Build likelihood, score and curvature; show a fitting iteration; fit the complete model and inspect convergence and identifiability. | Hand calculation checked against an explicit algorithm and package output. | Planned; no numerical equivalence or runtime claim. |
| Reader-facing operation | Produce predictions and contrasts on meaningful scales, with separate treatment of uncertainty in the mean and variation in new observations. | Prediction tables, curves and uncertainty displays for explicit covariate scenarios. | Planned; conditional and marginal targets must be labelled. |
| Interpretation | Explain coefficients, probability changes, rate ratios and positive-response effects; compare substantive conclusions rather than only fit statistics. | Worked interpretation with units, reference levels and estimand stated. | Planned; observational associations do not establish causation. |
| Failure or boundary | Introduce overdispersion, separation, dependence, nonlinear structure, extra zeros, missingness or observation bias in separate controlled examples. | Diagnostic plots, deliberately misspecified fits, and a record of what each diagnostic can establish. | Planned; do not combine all failure mechanisms into one opaque dataset. |
| Correction and re-evaluation | Change the relevant mean, variability, dependence or observation assumption; refit and recheck predictions and uncertainty using an appropriate validation split. | Before/after modelling ledger, held-out results and remaining-limit statement. | Planned; improved fit does not prove a biological mechanism. |

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
