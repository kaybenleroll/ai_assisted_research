# Executable Primer Examples

This document defines the policy and build contract for running selected code
examples from the technical primers. The shared Python, R, and Julia runtimes
are available, together with the opt-in executable-example runner. This policy
does not make existing examples executable.

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

Each manifest is `examples/manifest.toml`, with a top-level integer
`schema_version` (currently `1`) and one `[[examples]]` table per executable
entry. Entries use this schema:

```toml
schema_version = 1

[[examples]]
id = "gradient-check"
language = "python"
script = "examples/gradient_check.py"
profile = "python-base"
working_dir = "."
timeout_seconds = 30
```

`id` is unique within the primer and is the selector accepted by `just
examples`. `language` is one of `python`, `r`, or `julia`. Each entry uses
exactly one of `script` or `markdown` plus `fence`; these are paths contained
by the primer directory. `profile` must be `python-base`, `python-torch`, `r`,
or `julia`, and must match the language. `timeout_seconds` is an optional
integer from 1 to 600. Unknown keys, duplicate IDs, unsupported
language/profile pairs, invalid timeouts, and paths that escape the primer
directory fail closed. `working_dir` is an optional directory within the primer
and controls the container working directory. Example scripts must assert
meaningful results themselves; a zero exit status is the success condition, and
stdout/stderr are retained in the runner report. The runner processes entries
in manifest order and stops on the first failure.

Keep an example in its script when possible. A script may read its own
read-only primer tree and may write only below the runner-provided temporary
output directory. Do not place generated files in the primer checkout.

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

The runner is exposed through repository-root and shared per-primer `just`
recipes:

```sh
# From the repository root: run every entry in one primer
just examples numerical_analysis

# From the repository root: run selected IDs in manifest order
just examples numerical_analysis gradient-check matrix-solve

# From a primer directory: run every entry or selected IDs for this primer
just examples
just examples gradient-check
```

The root recipe takes a primer directory name without `primer_` (for example,
`numerical_analysis`); the per-primer recipe needs no primer argument. The
runner is invoked with host `python3 -I` and uses the repository's existing
Podman-first/Docker-fallback selection, Podman keep-ID user namespace, and
SELinux mount suffix conventions for runtime containers. It exposes no host
credentials and disables networking. Its container invocation must:

- use the repository's existing Podman/Docker detection and user/mount flags;
- mount source material read-only wherever the example does not need to edit
  it;
- provide a fresh temporary writable output directory for generated files;
- disable network access by default, with no credential passthrough;
- run from a stable container path with a predictable locale and environment;
- clean up the container and temporary output on success or failure; and
- leave the Git working tree unchanged.

Build the needed language image before running examples: `just
build-python-runtimes`, `just build-r-runtime`, or `just build-julia-runtime`
from the repository root. The runner does not build images implicitly. Use
`just --list` in a primer directory or at the repository root to inspect the
available recipes.

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

Issue #314 records the first migration in
[the executable-example inventory](executable-example-migration.md). It begins
with representative examples from the ML optimisation, numerical analysis,
and digital signal processing primers, then expands only when the manifest and
runtime contracts have proved stable.

The corresponding GitHub Actions job is path-scoped and opt-in. It builds only
the runtime profiles used by the migrated entries, probes them with networking
disabled, and runs the three selected manifests. It is deliberately separate
from the general repository checks so image-build time and example failures do
not obscure rendering, lint, or workbook failures.

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
