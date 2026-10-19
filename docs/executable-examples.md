# Executable Primer Examples

This document defines the policy and build contract for running selected code
examples from the technical primers. The shared Python, R, and Julia runtimes
are available; the executable-example runner is separate work. This policy does
not make existing examples executable.

## Purpose and Boundary

Primer code has two legitimate roles. Some snippets are intended to be copied
and adapted as explanations. Others are complete, deterministic examples that
should be executed to catch syntax errors, stale APIs, incorrect imports, and
claims about numerical results. The repository must distinguish those roles
explicitly rather than treating every fenced code block as a test.

The executable-example system covers selected Python, R, and Julia examples in
Pandoc primers. It is separate from document rendering: the Pandoc image
continues to render primers, the executable-example R runtime uses
`localhost/primers-r-runtime:4.5.3`, the existing Rocker image continues to
generate R figures, the executable-example Julia runtime uses
`localhost/primers-julia-runtime:1.12.7`, and the workbook retains its
independent Quarto image and render workflow. This system does not replace or
broaden those images.

## What Is Executable

An example is executable only when all of the following are true:

- it is complete enough to run without hidden notebook state or private data;
- its dependencies are declared by the selected language runtime or by the
  primer's explicit example configuration;
- it has a deterministic or bounded result suitable for an assertion, an
  exit-status check, or a documented output check;
- it does not require credentials, network access, a GPU, an interactive
  terminal, or an external service; and
- it is listed in that primer's execution manifest.

The manifest is the allowlist. A fenced block is not executable merely because
it has a recognised language label, appears in a published primer, or happens
to be syntactically valid.

The following remain illustrative unless a later audit converts them into
complete manifest entries:

- pseudocode and abbreviated fragments;
- snippets containing placeholders such as `...`, `<your-value>`, or
  `YOUR_API_KEY`;
- API sketches whose imports or surrounding application are omitted;
- examples that depend on private data, credentials, network services, a GPU,
  a long-running job, or interactive state; and
- intentionally language-neutral or comparative snippets that explain an idea
  without claiming to be a runnable program.

When an example is executable, the source should make its contract visible:
use a self-contained script or a delimited block, state important
assumptions, and assert the meaningful result rather than merely printing a
value.

## Repository Layout

The shared implementation will use these conventions:

```text
_shared/
  runtime/
    python/          # Python Containerfile and dependency lock
    r/               # R Containerfile and package lock
    julia/           # Julia Containerfile, Project.toml, Manifest.toml
  examples.just     # language dispatch and common execution recipes

primer_<name>/
  examples/
    manifest.toml    # explicit executable-example allowlist
    ...              # scripts or extracted runnable examples
```

The exact manifest schema is part of #313, but it must identify at least the
language, script or source block, expected execution mode, and any output or
assertion policy needed by the runner. A primer may keep a runnable example in
its Markdown when that is the clearest presentation; extracting a script is
preferred when the same example needs substantial setup or repeated execution.

The runner must use repository-relative paths and reject manifest entries that
escape the primer directory. It must report the primer, example identifier,
language, command, and captured failure so that a contributor can
repair the example without reproducing the whole build locally.

## Runtime Responsibilities

Each language image is a reproducible execution environment, not a general
development image. It is responsible for:

- a digest-pinned base image and explicitly recorded language version;
- the smallest justified shared package set for examples migrated into the
  common runtime;
- a lockfile or equivalent package-resolution record;
- a non-interactive probe that verifies the interpreter and shared packages;
- a documented update process for base images and dependencies; and
- a stable working-directory and input/output contract for the runner.

Primer-specific packages should not be added to a shared image merely because
one primer uses them. If a dependency is needed by only one primer,
the manifest and follow-up implementation should make that exception explicit
or provide a separately justified image layer. Image size and cold-build time
must be measured before adding a package set to CI.

The Python, R, and Julia images are independent. A failure in one language
must identify that language and must not silently fall back to the Pandoc,
R-figure, lint, or workbook images.

### Python Runtime Profiles

Issue #310 provides two deliberately separate Python profiles. The base image
uses Python 3.12.15 on the digest-pinned `python:3.12.15-slim-bookworm` image
and installs the exact versions in
`_shared/runtime/python/requirements.lock`: NumPy, SciPy, and Matplotlib.
The CPU PyTorch profile is built on that image and adds the exact versions in
`requirements-pytorch.lock` plus PyTorch 2.14.1 from the official CPU wheel
index recorded in `torch-cpu.lock`. PyTorch is not part of
the base image because it is large and only a subset of numerical examples
needs automatic differentiation.

The image entrypoints run `probe.py`. The probe asserts the Python minor
version, imports every shared package, performs a small NumPy/SciPy operation,
and, for the PyTorch profile, differentiates a scalar square. Run
`just build-python-runtimes` followed by `just probe-python-runtime` and
`just probe-python-torch` after changing a pin. Both probes must pass with
network access disabled. The profile is intended for the host
architectures for which the selected upstream wheels are published; adding
another architecture requires a separate build and probe review.

The lock inputs are updated as a reviewed set. A runtime update must record
the new base digest or package pins, rebuild both images from a clean local
cache, rerun the probes, and measure image size and cold-build time before CI
adoption. The repository-check `PYTHON_IMAGE` remains independent and must
not be used as an executable-example runtime.

### R Runtime

Issue #311 provides a separate executable-example R runtime tagged
`localhost/primers-r-runtime:4.5.3` by default. Build and run its offline probe
from the repository root with `just build-r-runtime probe-r-runtime`. Set
`R_RUNTIME_IMAGE` to override the tag. The existing `ROCKER` image and its
figure recipes remain unchanged; they continue to serve plot generation. The
digest-pinned `rocker/r-ver` base supplies the dated P3M CRAN snapshot for
direct and transitive CRAN packages. The MLverse CPU `torch` package and its
LibTorch/Lantern payload are explicit exceptions recorded under
`_shared/runtime/r/`. The probe checks the installed R, direct package, and
native torch versions with networking disabled. The last clean local build took
66 seconds and produced 2,099,951,961 bytes on x86_64.

### Julia Runtime

Issue #312 provides a separate executable-example Julia runtime tagged
`localhost/primers-julia-runtime:1.12.7` by default. Build and run its offline
probe from the repository root with `just build-julia-runtime probe-julia-runtime`.
Set `JULIA_RUNTIME_IMAGE` to override the tag. The image
uses the amd64 digest-pinned official `julia:1.12.7-bookworm` base. Its
committed `Project.toml` and generated `Manifest.toml` provide the shared
ForwardDiff and Zygote environment used by the automatic-differentiation
examples. The Containerfile instantiates and precompiles that environment
during the network-enabled build; the probe checks Julia, package versions, and
deterministic derivative values with networking disabled.

The manifest pins Julia package source trees and versions, but it does not make
binary artifacts identical across architectures. The initial runtime therefore
records amd64 as its supported build target. Update the Julia base and the
project/manifest together, rebuild from a clean cache, rerun the offline probe,
and record cold-build time and image size before adopting a new version. The
initial clean local build took 75 seconds and produced an image of
1,315,152,893 bytes on x86_64; this is a planning measurement, not a CI
guarantee.

## Runner Contract

The common runner will be exposed through shared `just` recipes and thin
per-primer wrappers. Its container invocation must:

- use the repository's existing Podman/Docker detection and user/mount flags;
- mount source material read-only wherever the example does not need to edit
  it;
- provide a fresh temporary writable output directory for generated files;
- disable network access by default, with no credential passthrough;
- run from a stable container path with a predictable locale and environment;
- clean up the container and temporary output on success or failure; and
- leave the Git working tree unchanged.

Examples that intentionally write files must write only below the temporary
output directory and must assert or enumerate the expected artefacts. The
runner must not infer executable examples from Markdown fences and must fail
closed when a manifest entry is malformed or names an unsupported language.

## Reproducibility and Updates

Base image references are pinned by digest. Language package versions are
recorded in the image build context: Python uses a locked requirements input,
R uses a dated Rocker/P3M CRAN snapshot plus a direct-package expectation file,
and Julia uses both `Project.toml` and `Manifest.toml`. The selected mechanism
may vary by ecosystem, but an unbounded install such as `pip install package`
or `install.packages("package")` is not an acceptable runtime contract.

Each image issue must record the versions and digests it adopts, provide a
clean-build probe, and state how updates are reviewed. Updating a runtime must
be allowed to surface example failures; it must not silently change the
meaning of an example or overwrite generated primer outputs.

## CI Adoption

Example execution is initially opt-in and limited to migrated manifest
entries. The first CI integration should measure cold-build duration and image
size, use a bounded timeout, and run only examples that meet the contract
above. It must not make every existing code fence a mandatory test. A failed
example should identify the manifest entry and preserve enough logs to
diagnose it.

The migration issue will begin with representative examples from the ML
optimisation, numerical analysis, and digital signal processing primers, then
expand only when the manifest and runtime contracts have proved stable.

## Work Decomposition

The issues below are deliberately separated so that architecture, images,
execution policy, and content migration can be reviewed independently:

| Issue | Responsibility | Prerequisites | Not included |
| --- | --- | --- | --- |
| #309 | This policy, directory contract, and dependency boundaries | None | Runtime images or migrated examples |
| #310 | Pinned Python runtime, lock input, probe, and documentation | #309 | Generic runner and broad example migration |
| #311 | Pinned R runtime, lock input, probe, and documentation | #309 | Replacing the Rocker figure workflow |
| #312 | Pinned Julia runtime, project/manifest, probe, and documentation | #309 | Generic runner and broad example migration |
| #313 | Shared runner, manifest schema, language dispatch, temporary I/O, and per-primer wrappers | #309, #310, #311, #312 | Auditing or migrating every existing code fence |
| #314 | Example audit, selected migrations, assertions, and affordable opt-in CI | #309, #310, #311, #312, #313 | Making all snippets mandatory on the first pass |

Changes to the catastrophe workbook remain outside this sequence. Its Quarto
and combined R/Python image are a separate build system with its own recipes
and dependency policy.
