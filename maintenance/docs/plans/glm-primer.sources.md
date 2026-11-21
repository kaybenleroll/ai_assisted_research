# GLM primer: source and implementation feasibility record

Updated 21 November 2026. Historical proposals below are distinguished from executed feasibility. Current frozen-data, runtime, model commands, hashes and results are summarised in [the feasibility record](glm-primer.feasibility.md) and full scratch reports. No primer-level audit or release claim is made.

## Initial candidates (superseded as defaults by the reuse follow-up)

This section preserves the original 20 November shortlist as planning history.
Evidence gathered on 21 November supersedes its unresolved salamander
provenance and default-case status; see the data and software feasibility update.

1. **Stream salamanders**, Price et al.: the [Dryad record](https://datadryad.org/dataset/doi%3A10.5061/dryad.5m8f6) offers a 5.39 KB count-data CSV, identifies the study and paper, and the [glmmTMB manual](https://cran.r-project.org/web/packages/glmmTMB/refman/glmmTMB.html) describes 644 rows, 23 sites sampled four times, species, site mining status and sampling covariates. Real repeated ecological counts support Poisson/NB, grouping, and exploratory zero-inflation. `count > 0` is detection in a visit, not demonstrated true site occupancy; repeated visits do not alone identify occupancy without an explicit observation model and assumptions. Different species/site/visit rows are dependent; choose and document the observational unit. Do not invent effort or exposure variables. Cite both original paper and Dryad as the package requests. Dryad landing page accessible without login, but exact file licence and permitted redistribution not established; pin the version and verify licence and source/package transformations before vendoring.
2. **Owl nestling begging**, [glmmTMB Owls documentation](https://cran.r-project.org/web/packages/glmmTMB/refman/glmmTMB.html): 599 records with nest, treatment, parent sex, brood size and negotiation counts, with Roulin and Bersier 2007 cited; package credits Alain Zuur for data access. Package example fits NB, nest random intercept and log brood-size offset; [DHARMa's case](https://cran.r-project.org/web/packages/DHARMa/vignettes/DHARMa.html) demonstrates Poisson, grouped and NB diagnostic progression. This is a separate study, not a salamander follow-up. Offset imposes proportionality to brood size; compare the estimated coefficient and discuss whether biologically plausible. Original data licence/redistribution permission and detailed sampling design not established; use installed package for development pending verification. Neither excess zeros nor fit improvement proves a separate structural-zero mechanism.
3. **Black cherry trees**, [R datasets manual](https://stat.ethz.ch/R-manual/R-patched/RHOME/library/datasets/html/trees.html): 31 felled trees with positive timber volume, height and diameter, labelled `Girth` in error. Sources given are Meyer (1953) and Ryan et al. (1976). Useful separate forestry example of positive response, Gamma/log mean versus log-transformed Gaussian response, back-transformation and influential observations; size and limited study provenance prohibit ecological generalisation. Available with base R; original data rights and independent redistribution terms remain unverified. Treat suitability of Gamma as a model assumption requiring diagnostics, not fact.

Use an ecology-themed simulated case as the continuous spine so latent truth, exposure, nonlinearity, sampling process and known failure mechanisms are explicit; keep real cases separate and identify actual source boundaries. Simulations should include Bernoulli/Poisson, changing effort, group heterogeneity, overdispersion, smooth response, distinguishable structural zeros and Bayesian prior sensitivity; do not assert that all are identifiable from one finite realised dataset. A running real case can revisit salamanders for binary *detection* and counts; Owls provides a real offset and grouped example; trees supplies a distinct positive outcome. An R/Python/Julia core should share frozen input and checks for design matrix, mean predictions, log likelihood conventions and named tolerances; full extension parity is not promised.

## Software feasibility and limits

- R `glm` and family interfaces provide the core (see [glm](https://stat.ethz.ch/R-manual/R-devel/library/stats/html/glm.html) and [family](https://stat.ethz.ch/R-manual/R-devel/library/stats/html/family.html)). [glmmTMB](https://cran.r-project.org/web/packages/glmmTMB/refman/glmmTMB.html) documents NB, random effects and zero-inflation; [mgcv](https://cran.r-project.org/web/packages/mgcv/refman/mgcv.html) documents penalised GAMs, NB, and restricted zero-inflated families. [brms](https://paulbuerkner.com/brms/reference/brm.html) documents Bayesian multilevel inference; [its family parameterisation](https://paulbuerkner.com/brms/articles/brms_families.html) spells out zero-inflated and hurdle likelihoods. Quasi-likelihood is not a full probability distribution: do not promise ordinary likelihood/AIC or direct simulation from it.
- [statsmodels API](https://www.statsmodels.org/stable/api.html) lists GLM, GLMGam, zero-inflated count models, and Bayesian Poisson/binomial mixed models; mixed-model support is limited compared with general-purpose GLMM software. Its [GAM implementation source](https://www.statsmodels.org/stable/_modules/statsmodels/gam/generalized_additive_model.html) labels it experimental; test chosen smooth features and version. [PyMC's example](https://www.pymc.io/projects/examples/en/latest/generalized_linear_models/GLM-poisson-regression.html) demonstrates Bayesian Poisson regression; selected mixture and random-effect specifications need implementation verification.
- [GLM.jl](https://juliastats.org/GLM.jl/dev/api/) supports formula/matrix GLMs. [MixedModels.jl](https://juliastats.org/MixedModels.jl/v5.2/limitations/) explicitly warns its GLMM results for families with dispersion parameters are incorrect and says GAMMs are unsupported; use only a documented suitable Bernoulli/Poisson mixed model if tested. [TuringGLM.jl](https://turinglang.org/TuringGLM.jl/stable/tutorials/poisson_regression/) documents Bayesian Poisson sampling; bespoke mixture/GAM implementations are unverified. Julia GLM documentation notes [different default Wald reference distributions from R](https://juliastats.org/GLM.jl/dev/examples/) for estimated dispersion. Do not assume identical numerical estimates or inference: contrast coding, offsets, exposure, weights, dispersion, priors, optimisation and likelihood constants must be harmonised.

## Data and software feasibility update (21 November 2026)

The selected cases are now frozen for planning feasibility: Palmer penguins for
positive measurements and categorical contrasts, and the explicitly
package-derived glmmTMB Salamanders object for repeated counts. The exact URLs,
source commits, file hashes, row structure, reuse statements, transformations
and bounded interpretations are recorded in `glm-primer.case.md` and
`glm-primer.feasibility.md`. Dryad's original CSV could not be downloaded, but
the pinned package-derived case is acceptable with its provenance and
attribution; original-file identity is not a gate. BBS is not the selected
default and its archive was not downloaded. The prior BBS release metadata
uncertainty is retained only as a note about an unselected option.

The base Python, R, Julia and Pandoc images are present locally; existing
offline probes pass. Fixed-design core fits agree for Gaussian, Bernoulli,
Poisson with offset and Gamma, and fixed-theta NB2 predictions agree across
R/Python/Julia plus a task-local statsmodels image. These Python and Julia core
translations include short explicit algorithms, not production packages. R
extension feasibility includes limited simulations and fit spikes. The
advanced package-image layer results remain subject to final integration and
review; these checks do not establish final dependency locks, complete feature
coverage, full diagnostics or a correct inferential conclusion.

## Reuse follow-up: stronger candidates (20 November 2026)

**Palmer penguins — recommend as the reusable positive-response/categorical example in place of trees.** The [package authors' README](https://github.com/allisonhorst/palmerpenguins/blob/main/README.md) says its data are CC0 under Palmer LTER and LTER Type I policy. Its [vignette](https://github.com/allisonhorst/palmerpenguins/blob/main/vignettes/intro.Rmd) says the data came from the EDI portal and were collected by Kristen Gorman and Palmer LTER in 2007–09. Cite the package and the original [Gorman et al. paper](https://doi.org/10.1371/journal.pone.0090081), plus the EDI species records listed by the README: [Adélie](https://doi.org/10.6073/pasta/98b16d7d563f265cb52372c8ca99e60f), [Gentoo](https://doi.org/10.6073/pasta/7fca67fb28d56ee2ffa3d9370ebda689), [Chinstrap](https://doi.org/10.6073/pasta/c14dfcfada8ea13a17536e73eb6fbe9e). The README additionally asks those publishing the data to contact Gorman about analysis and possible collaboration, and refers to LTER data-use policy; record that request faithfully alongside CC0 rather than treating it as a verified licence condition or asserting contact occurred. The [dataset documentation](https://allisonhorst.github.io/palmerpenguins/reference/penguins.html) describes 344 observations with species, island, body mass, size measurements, sex and year; [CSV documentation](https://allisonhorst.github.io/palmerpenguins/reference/path_to_file.html) confirms bundled small CSV files and shows missing values. Model adult body mass with species as categorical covariate; demonstrate missing-data selection, uneven species/island design, observational scope and no implied causality. A Gamma model is a teaching choice requiring diagnostics, not implied by positivity. Use binary sex classification only with explicit missingness and scientific limitations; it is not an ecological occupancy example.

**USGS North American Breeding Bird Survey — researched alternative, not the selected default.** The [USGS release page for dataset 1966–2019, version 2019.0](https://www.usgs.gov/data/north-american-breeding-bird-survey-dataset-1966-2019-version-20190), DOI [10.5066/P9J6QUF6](https://doi.org/10.5066/P9J6QUF6), explicitly marks this release CC0 1.0. It describes annual roadside routes, nominally 50 stops per route, three minutes per stop, counts of birds seen/heard, route and observer IDs, date, weather and quality indicator. Routes recur across years, though stop positions can change; USGS [documents spatial uncertainty](https://www.usgs.gov/data/location-and-land-cover-uncertainty-associated-stop-level-data-north-american-breeding-bird). USGS [protocol](https://www.pwrc.usgs.gov/bbS/participate/BBSInstructions.pdf) explicitly says counts are not exhaustive censuses. A compact extracted route-year/species subset could teach count outcomes, repeated routes and observer effects, with sight/hearing detection and roadside selection limitations. Do not equate a zero count with verified absence or presume every unreported species/route is a surveyed zero: verify raw tables, run quality, joining and missing-versus-zero semantics before extraction. A fixed three-minute protocol alone does not demonstrate variable exposure; use synthetic variable effort or another verified source instead of inventing a BBS offset.

The USGS page has an unresolved inconsistency: its title states 1966–2019 while its abstract says 1966–2018. Check release metadata and actual year fields before specifying the coverage. The DOI target's ScienceBase page was blocked by robots, so exact file layout, download sizes, subset reproducibility and release-level terms beyond the USGS landing page were not independently inspected. No download performed. Earlier owl/salamander/tree sources remain optional candidates with dataset-level terms unresolved; replace as default real cases, not as claims that their use is prohibited.


## Mathematical source plan

The foundational source is [Nelder and Wedderburn (1972), Generalized Linear Models](https://doi.org/10.2307/2344614). Its publisher abstract supports the historical connection between exponential-family observations, iterative weighted regression and likelihood-based analysis; this planning pass does not claim to have audited every derivation in the article.

For penalised smooths and smoothing-parameter estimation, [Wood (2011)](https://doi.org/10.1111/j.1467-9868.2010.00749.x) is a primary-method source, also listed in the [mgcv citation record](https://cran.r-project.org/web/packages/mgcv/citation.html). The research phase must inspect the actual mathematical claims used, distinguish smoothing-parameter estimation from coefficient estimation, and check each explanatory example.

Before each remaining route is drafted, extend this map with primary or authoritative sources for quasi-likelihood, negative-binomial parameterisations, multilevel integration and marginalisation, categorical response models, mixture and hurdle identifiability, Bayesian computation, predictive assessment and observation-process limits. A topic label or package manual alone is insufficient support for a general mathematical or ecological claim. Map the selected sources to the brief's stable concept IDs.

## Planning acceptance and next evidence

Begin mathematical drafting against the selected synthetic spine, penguin
measurements and package-derived Salamanders counts. Do not wait on the
unselected BBS archive or an original-file byte comparison. Keep the following
as explicit gates for final executable examples and release:

- select and lock a supported implementation for each advanced route and
  record immutable image/dependency identities; the current statsmodels layer
  has exact version pins but lacks wheel hashes, and advanced package layers
  still need final review;
- validate route-specific fits, parameterisations, diagnostics, failure and
  repair examples, and uncertainty claims, including Bayesian computation and
  grouped validation where promised;
- freeze and register final inputs and executable examples, then run every
  selected example offline in its pinned runtime with recorded tolerances;
- complete the content checkpoint, independent audit, source locators, figures,
  pinned HTML/PDF builds and visual QA before release.

The base image probes and preliminary core/NB comparisons are feasibility
evidence, not publication reproducibility. Scope remains R01–R11 and C01–C26;
software decisions must resolve the promised reader outcomes, not silently
remove a route.
