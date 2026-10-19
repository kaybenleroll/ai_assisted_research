# Executable-example migration inventory

This inventory records the first evidence-based migration for issue #314.
The manifest is an allowlist: an existing fenced block remains illustrative
unless it is represented by one of the scripts below. The selected scripts are
small, deterministic, self-contained, and assert a numerical property rather
than relying on printed output or a plot.

## Included

| Primer | Manifest entry | Source material | Reason for inclusion |
| --- | --- | --- | --- |
| ML optimisation | `regularised-logistic` | Recurring Example: Regularised Logistic Regression | Standard-library Python check of stable loss, gradient finite difference, row-order invariance, and descent. |
| ML optimisation | `logistic-ad` | Automatic Differentiation for Optimisation — Worked Derivative Products | Julia ForwardDiff/Zygote check of forward and reverse gradients, a JVP, an HVP, and independent finite differences. |
| Numerical analysis | `linear-solve-python`, `linear-solve-r`, `linear-solve-julia` | Shared Example A: Solve a System and Compute Residual | The same well-conditioned two-by-two solve is short, deterministic, and teaches language parity with residual assertions. |
| Digital signal processing | `fft-parseval-python` | Conjugate Symmetry and One-Sided Spectra; Parseval's theorem | NumPy check of the unnormalised FFT energy identity and real-input conjugate symmetry without plots or external state. |

The scripts live below each primer's `examples/` directory and are listed in
that directory's `manifest.toml`. The runner executes them in manifest order.

## Excluded from the first wave

- R and Julia parity for the DSP FFT check: the first pass establishes the
  property with the shared Python scientific runtime before adding more image
  build time and another pair of normalisation conventions.
- The ML PyTorch derivative fence: the PyTorch profile is intentionally large,
  and the first CI job does not need it to establish the runner contract.
- Existing R plot generators: they already have dedicated `plots` and `full`
  recipes, write tracked figures, and are not manifest-style examples.
- Examples whose result depends on a plot, a stochastic trace, hidden state
  from an earlier fence, or a specialised solver package.

## Deferred candidates

The next candidates are the numerical-analysis root, derivative, quadrature,
and least-squares examples; the ML simplex projection and deterministic
curvature checks; and DSP aliasing, STFT reconstruction, and causal filter
properties. Each needs its own assertion and tolerance review before being
added. Package-heavy ODE, adaptive optimisation, and broad DSP pipeline
examples remain deferred until their runtime dependencies and side effects are
measured.

## CI boundary and measurements

The first CI job is opt-in by path: it runs on changes to the migrated
manifests/scripts, the shared runner and runtime definitions, the Justfiles,
or this workflow. It builds only the Python base, R, and Julia profiles used by
the selected entries, probes them offline, and runs all three opted-in
manifests. It does not make every primer snippet mandatory.

The existing local planning measurements are 66 seconds and about 2.10 GB for
the R runtime, and 75 seconds and about 1.32 GB for the Julia runtime on
x86_64. These are planning observations rather than CI guarantees; the
workflow has a 30-minute job limit and should be tightened after observing
several clean GitHub-hosted runs.
