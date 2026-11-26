# GLM primer feasibility evidence

Issue #467; snapshot date: 21 November 2026. This record summarises the
feasibility reports present at integration time. Worker reports can grow after
this snapshot; later evidence must be dated and incorporated explicitly.
Feasibility permits mathematical drafting against selected cases. It is not a
claim that the primer, all examples, advanced package environments, audit or
publication have been completed.

## Selected data and provenance

### Palmer penguins

Use the authors' curated package CSV at commit
[`8957207b78d6ccd1b4654a9dd9c9041b657478ab`](https://github.com/allisonhorst/palmerpenguins/tree/8957207b78d6ccd1b4654a9dd9c9041b657478ab),
downloaded from the pinned public URL:

`https://raw.githubusercontent.com/allisonhorst/palmerpenguins/8957207b78d6ccd1b4654a9dd9c9041b657478ab/inst/extdata/penguins.csv`

SHA-256: `f204db2c753b0937caac3cb35258562c14f073e4bbc76be24b4c51ce22767a93`.
Authors declare CC0 and request publishers contact Kristen Gorman about
analysis/collaboration; record that request, but do not represent it as a CC0
condition or claim contact. Cite the package and Gorman et al. (2014), plus the
EDI species records listed in the source report. The 344-row file has two
missing body masses and eleven missing sex values. The 342-row complete-mass
case supports a matched Gaussian/identity and Gamma/log feasibility comparison;
the complete-sex example has 333 rows. The uneven species/island design limits
separate attribution and the all-cells species-by-island interaction is rank
deficient. It is observational data; no causal or intervention claim follows.

### Salamanders

Use the explicitly package-derived object from
[`glmmTMB` commit `c311085c19a50af9a8e930352885313897333b7f`](https://github.com/glmmTMB/glmmTMB/tree/c311085c19a50af9a8e930352885313897333b7f),
not a claimed original-file copy. Pinned object URL:

`https://github.com/glmmTMB/glmmTMB/blob/c311085c19a50af9a8e930352885313897333b7f/glmmTMB/data/Salamanders.rda`

Object SHA-256: `cca69c7eb8488d7932217ccc623a815105eb3e522f4debcb1841342c31bfc389`.
The offline R-to-CSV transformation script is
`.scratch/glm-feasibility-2026-11-21/data/prepare.R`, SHA-256
`a2d221fce1075a36691d0b4bdcdf2517f95a940fb0d32d0dcf08c7f1a2b81260`;
the converted 644-row CSV hash is
`1dadca43a8c917da58cd341fb04f15c0ad22384a8487a33dc3f6b77516bf8874`.
Carry the package AGPL-3 declaration, Dryad metadata's CC0 declaration, both
requested citations, commit, hashes and transformation with this derived-data
case. Dryad's dataset API gave metadata for version 1 (17 November 2016),
DOI `10.5061/dryad.5m8f6`, 23 reaches and the Price et al. paper; the original
file API returned HTTP 401 and a further landing-page stream returned HTTP 403.
Original-file byte identity and exact original-to-package transformation are
not claimed and are not gates. The object has 23 sites, four sample labels per
site, seven species/stage categories and no missing values in the checked
columns. A prespecified GP subset has 92 rows, 12 reference and 11 mined sites.
Counts are detections/recorded counts, not occupancy or known abundance; visits
within sites are dependent, and no exposure variable was established.

The USGS Breeding Bird Survey is not the selected default and its archive was
not downloaded. The prior title/abstract year inconsistency remains relevant
only if the plan later reopens that candidate. Owl and tree cases are also not
selected defaults.

## Runtime inventory and probes

All four local images were present when inventoried. IDs and local digests:

| Runtime | Image | Image ID | Digest | Version/evidence |
|---|---|---|---|---|
| Python | `localhost/primers-python-runtime:3.12.15` | `43507107691f` | `sha256:b7baff17314e7b9818264c516e467af60036c527ee8174f739c97e129399595b` | Python 3.12.15; NumPy 2.3.3; SciPy 1.16.2; Matplotlib 3.10.6 |
| R | `localhost/primers-r-runtime:4.5.3` | `d6bdf72307c0` | `sha256:bad6c984a14dd3e114d26d136447cf053f5d63cb0faa33dfef1943d00983feda` | R 4.5.3; base stats 4.5.3; MASS 7.3-65; Matrix 1.7-5; numDeriv 2016.8-1.1; mgcv 1.9-4; survival 3.8-6; torch 0.17.0 CPU |
| Julia | `localhost/primers-julia-runtime:1.12.7` | `dec460a73a62` | `sha256:10cca15e36fe64594c8a95d5949437dd948be82a71492e4c35dd065fe015400b` | Julia 1.12.7; ForwardDiff 0.10.39; Zygote 0.7.10 |
| Pandoc | `localhost/primers-pandoc:latest` | `61d7d31cd74f` | `sha256:239428f1d61de725be479c72ada0bbe146a313791ee2d68333114b6c623ad771` | Pandoc 3.11; Lua 5.4 |

Existing offline base probes passed using:

```sh
podman run --rm --pull=never --network=none localhost/primers-python-runtime:3.12.15
podman run --rm --pull=never --network=none localhost/primers-r-runtime:4.5.3
podman run --rm --pull=never --network=none localhost/primers-julia-runtime:1.12.7
podman run --rm --pull=never --network=none --entrypoint pandoc localhost/primers-pandoc:latest --version
```

The base Python image does not include pandas, statsmodels, scikit-learn,
SymPy, JAX or PyTorch. The Julia locked project exposes ForwardDiff and Zygote
as direct dependencies; no high-level GLM package is in that project.

## Model feasibility results

Full commands, script hashes, raw output and caveats are in
`.scratch/glm-feasibility-2026-11-21/models-report.md` and
`.scratch/glm-feasibility-2026-11-21/data-report.md`.

Reproduction scripts and SHA-256 hashes:

| Script | SHA-256 |
|---|---|
| `.scratch/glm-feasibility-2026-11-21/data/prepare.R` | `a2d221fce1075a36691d0b4bdcdf2517f95a940fb0d32d0dcf08c7f1a2b81260` |
| `.scratch/glm-feasibility-2026-11-21/data/real_cases.R` | `a568d723712fd4c90c44b12bdff4ac599ab0bd6675f16833693c720025eed6fe` |
| `models/core.R` | `eb21091beb89e663b272d49815bb0b0fad359ad20ea30ccee303bc49d688ad4d` |
| `models/core.py` | `b03cc3aed2cb5208632e09cc8c8bc371a0cc8789862f93f114a5f9ee8a63b41d` |
| `models/core.jl` | `e4cd135990ffac6d89105c9cbde86ffded049c9803cc997fa9b9bedf4debd499` |
| `models/extensions.R` | `d8df6a4cb06cd84fef0fef07f186adbd73530cdce8c7da3b3cc6c644faeb27f1` |
| `models/nb.R` | `6015221b93986167886d51137f5ef61c8ac43a192a551ba245723864f4563005` |
| `models/nb.py` | `b71ff87ec77fad9bbb9e3fb308f91e40688830a86c77782f157d3f419ffdbfa3` |
| `models/nb.jl` | `83aab86aee1c69a836c7bdf26c8cb2c2ea5a50b3e4b3d1b3f2f052ea263efc48` |
| `models/statsmodels_nb.py` | `cede204f91bf07e10cfe68c78a5deeea75e77459d7d65642d206f1b25005dd24` |

Model scripts are under `.scratch/glm-feasibility-2026-11-21/models/`.
The runtime image references and exact Podman commands are listed in the
model report; all runs were offline after image preparation.

- A common 24-observation benign full-rank design compares Gaussian/identity,
  Bernoulli/logit, Poisson/log with exposure offset, and Gamma/log. R uses
  `glm`; Python and Julia use translations of explicit Fisher-scoring/IRLS
  algorithms, not independent production libraries. For two fixed profiles,
  predictions match to a largest printed difference of `4e-10`.
- A fixed-theta NB2 design (`theta=2`) was compared using R MASS, Python SciPy,
  Julia ForwardDiff and a task-local statsmodels layer. Maximum prediction
  discrepancy was `5.93e-7`. The explicit SciPy and Julia likelihood methods
  omit terms constant in coefficients and do not include production safeguards;
  this does not verify NB dispersion estimation across languages.
- R-only spikes ran quasi-Poisson, NB2, custom random-intercept Poisson
  integration, `mgcv::gam`, simple hurdle and zero-inflated likelihoods,
  conjugate beta-binomial calculations, grid logistic Bayes, multinomial
  (`nnet`) and ordinal (`MASS::polr`). These are narrow feasibility examples,
  not complete route support, robust statistical validation or production
  implementations. Bayesian sampling/MCMC and diagnostics have not been
  established. Advanced package-layer results await final main/model-worker
  integration and review.
- Baseline real-data fits ran offline in the pinned R image. Penguins compares
  Gaussian and Gamma fits on the same 342 mass observations. Salamanders
  compares Poisson and MASS NB2 fits for GP counts, plus one row-level and one
  site-blocked split. The report gives exact coefficients, fitted values,
  dispersion and split scores. These are feasibility, not a full inferential,
  diagnostic or ecological interpretation audit; no best model was selected.

The task-local Python layer `localhost/glm-feasibility-python:20261121` used
statsmodels 0.15.0, pandas 3.1.1, patsy 1.0.3 and pinned dependencies. Its
image ID is
`50597994beed88cc40fa2499a4c575d1f68cf8e42fe387a1e00f29a91594eec4`.
Requirements and Containerfile hashes are respectively
`6e6435a096450a80589818975075515fe0d85d921c4b561b537b24384a95fa53` and
`5bf18a95aee11bb3c2d53b2eff648960f5696901fa198233db60da5c23c95650`.
Versions were pinned but wheel hashes were not; the base tag was mutable at
build time. Keep this image isolated; no shared runtime definitions changed.

## Remaining gates

Drafting may proceed against the selected cases and known algorithmic evidence.
Before final examples and release: choose and lock supported implementations
for each advanced route; resolve dependency/image identities (including hashes
for the task-local Python layer if retained); validate route-specific fits,
parameterisations, uncertainty, diagnostics, failure/repair and grouped
validation; verify advanced package results; register and execute the final
example manifest offline with tolerances; and complete the content checkpoint,
independent audit, figures, pinned HTML/PDF builds and visual QA. Preserve all
R01–R11 and C01–C26 reader outcomes. Reproducibility is an explicit acceptance
criterion for implementation issue #468.
