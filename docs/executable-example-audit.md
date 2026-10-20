# Executable-Example Coverage Audit

This audit records which code examples across the primer set should become
explicitly executable, which need a specialised smoke-test harness, and which
should remain illustrative. It was completed for issue #321 on 20 October
2026. The audit follows the allowlist and runtime contract in
[Executable Primer Examples](executable-examples.md): a language-labelled
Markdown fence is not executable merely because it appears complete.

## Method and Decision Rules

Each primer was reviewed for language-labelled fences, standalone scripts,
Justfile recipes, dependencies, side effects, and claims that could be checked
with a bounded assertion. Candidates were then classified as follows:

- **Migrate** means that the example is sufficiently complete, deterministic or
  bounded, offline, and suitable for an entry in an existing Python, R, or
  Julia manifest.
- **Specialised smoke test** means that the example is worth checking but needs
  a separate shell, Git, container, service, or product-specific harness.
- **Illustrative** means that the example is intentionally incomplete,
  provider-dependent, stateful, interactive, networked, credentialed,
  GPU-dependent, or otherwise unsuitable for shared executable-example CI.

The recommended order weighs instructional value, assertion quality, runtime
and dependency cost, maintenance risk, and whether the existing runner can
execute the example without a new runtime profile.

## Coverage Snapshot

Issue #314 established six manifest entries across three primers:

| Primer | Existing entries | Current coverage |
| --- | ---: | --- |
| ML optimisation | 2 | Regularised logistic optimisation in Python and automatic differentiation in Julia. |
| Numerical analysis | 3 | A small linear solve in Python, R, and Julia. |
| Digital signal processing | 1 | A NumPy FFT and Parseval check in Python. |

The remaining primers have no executable-example manifest. Existing plot
generators are build inputs rather than manifest examples, and OpenClaw's
backup and restore scripts are operational utilities rather than safe tests.

## Primer Inventory

The inventory covers every primer directory. “None” means that the audit found
no candidate that should be migrated under the current execution contract; it
does not mean that the primer contains no code or commands.

| Primer | Candidate and source | Class | Proposed contract and runtime | Priority and recommendation |
| --- | --- | --- | --- | --- |
| Building AI agents | Agent execution loop in `primer_building_ai_agents/primer_ai_agents_comprehensive.md`, “The Execution Loop Implementation”. | Migrate | Inject a fixed fake tool/model sequence and assert tool order, retry cap, and terminal result. Python base; no model call. | **High.** Extract the pure control flow before testing it. Keep live-agent examples illustrative. |
| Claude Code alternative | Provider-neutral configuration in `primer_claude_code_alternative/primer-claude-code-alternatives.md`, “The Recommended Default: OpenCode Plus Explicit Model Tiers”. | Specialised smoke test | Parse a selected complete JSON fixture and assert required fields and loopback endpoint shape. Python standard library. This checks the documented shape, not product compatibility. | **Low.** Consider only as a narrow static check; do not start providers or install npm packages. |
| Codex for Claude Code users | Complete TOML configuration block in `primer_codex_for_claude_code_users/primer-codex-for-claude-code-users.md`, “Configuration”. | Specialised smoke test | Parse one self-contained TOML fixture with `tomllib` and assert a documented invariant. Python 3.12. | **Low.** Product semantics and shell setup remain illustrative. |
| Comparative religion | No suitable language-labelled executable candidate identified. | Illustrative | The primer is prose-led and its examples are interpretive rather than deterministic programs. | **None.** Do not add a test harness for this content. |
| Complex analysis | Contour quadrature convergence in `primer_complex_analysis/primer_complex_analysis.md`, “A Numerical Contour Check”. | Migrate | Numerically integrate a simple contour and assert convergence towards the known residue result as resolution increases. Python base, preferably standard library. | **High.** Strong mathematical contract and low runtime cost. `generate_plots.R` remains a rendering input. |
| Containerisation | No suitable current executable fence; diagrams and CLI guidance appear under “Building and Identifying Images” and “Reproducible Development and CI”. | Specialised smoke test | A future test could build a tiny pinned image and assert command output, but requires an isolated container engine harness. | **None for current examples.** Create a separate container-integration issue only if the harness is justified. |
| Deep learning | Fixed-input CPU self-attention or ConvNet block in `primer_deep_learning/primer_deep_learning.md`, “Code: Self-Attention in Three Frameworks” or “Code: A Small ConvNet in Three Frameworks”. | Migrate | Fix the seed and input, run one forward/backward pass, and assert output shape plus finite gradients. CPU PyTorch profile. | **Medium.** Select one compact PyTorch example; exclude TensorFlow, Flax, downloads, and training loops. |
| Digital signal processing | `primer_digital_signal_processing/examples/fft_parseval.py`. | Migrate | Existing Parseval and conjugate-symmetry assertions. Python base. | **Complete in #314.** Use as the pattern for future numerical migrations. |
| Evaluation loop | Elo update in `primer_evaluation_loop/primer_evaluation_loop.md`, “Aggregate”, and deterministic metric calculations in “Automate”. | Migrate | Assert draw invariance, equal-and-opposite rating changes, conserved total rating, and bounded metric outputs. Python base. | **High.** Small, pure, and directly tied to the primer's claims. Exclude live judge/model calls. |
| Hermes server | YAML and shell configuration under “Configuration” and “API Server”. | Illustrative | No stable offline Hermes parser or pinned service contract is available; meaningful checks would require a server and provider configuration. | **None.** Revisit only if Hermes supplies a pinned offline validator. |
| Information theory | Joint-law marginals and mutual information in `primer_information_theory/primer_information_theory.md`, “Base R and Python: Inspect a Joint Law”. | Migrate | Assert the displayed symmetric binary law's marginals and mutual information in bits. Python standard library or base R. | **High.** Best low-cost next candidate; Python and R parity can be separate entries. |
| Linux/Git workflows | Pipeline recovery and reflog recovery in `primer_linux_git_workflows/primer_linux_git_workflows.md`, “Worked Example: Finding and Recovering a Failed Pipeline” and “Recovery Walkthrough”. | Specialised smoke test | In a disposable temporary repository, assert `pipefail` failure propagation and recovery-ref contents. Bash plus Git. | **Medium.** Valuable, but needs a separate shell runner with strict temporary-repository safety. |
| ML optimisation | `primer_ml_optimisation/examples/regularised_logistic.py` and `logistic_ad.jl`. | Migrate | Existing deterministic optimisation and automatic-differentiation assertions. Python and Julia runtimes. | **Complete in #314.** No further migration required before the audit follow-ups. |
| Military structure | No suitable language-labelled executable candidate identified. | Illustrative | Tables, terminology, and organisational comparisons do not expose a deterministic program contract. | **None.** Keep examples explanatory and sourced. |
| Numerical analysis | `primer_numerical_analysis/examples/linear_solve.py`, `linear_solve.R`, and `linear_solve.jl`. | Migrate | Existing solution and residual assertions across three languages. | **Complete in #314.** Extend only with similarly bounded numerical claims. |
| Oh My Zsh | No suitable current executable candidate identified. | Specialised smoke test | Shell configuration could be tested only in an isolated shell with a controlled home directory and installed plugin set. | **None for now.** A shell-harness issue would be separate from the language runner. |
| OpenClaw | `primer_openclaw/scripts/backup_state.sh` and `restore_state.sh`, plus service and Compose configuration. | Specialised smoke test | A refactored archive helper could round-trip a temporary fixture, but current scripts control services and restore state in place. | **None for current scripts.** Never run them against the checkout or real service state in CI. |
| Pi coding agent | Project-trust discussion in `primer_pi_coding_agent/primer_pi_coding_agent.md`, “Project Trust”. | Specialised smoke test | A pure policy model could assert trust decisions for fixed project resources, but this would test the documented model, not Pi itself. Python base if extracted. | **Low.** Consider only after clearly separating policy logic from Pi startup and npm dependencies. |
| Political systems | No suitable language-labelled executable candidate identified. | Illustrative | The primer's comparisons and institutional claims require evidence and interpretation rather than program execution. | **None.** Maintain through content and source review. |
| Python for R users | Standard-library mapping example in `primer_python_for_r_users/primer_python_for_r_users.md`, “Mapping Family Equivalents With Real Patterns”. | Migrate | Assert mapping keys, values, and transformation results on a fixed fixture. Python base. | **Medium-high.** Prefer this before pandas examples; do not enlarge the shared image for a single data-frame example. |
| Researching local LLMs | Offline scoring and threshold decision in `primer_research_local_llms/primer-running-llms-locally.md`, “Minimal Local Eval Loop”. | Migrate | Use fixed expected outputs and assert metric aggregation and the threshold decision. Python base. | **Medium-high.** Test scoring only; exclude model servers, downloads, GPUs, and inference. |
| Retrieval and RAG | Toy lexical/hybrid ranking and metrics in `primer_retrieval_rag/primer_retrieval_rag.md`, “Lexical Retrieval” and “Ranking and Evaluation”. | Migrate | Assert exact ranked IDs, Recall@k, MRR, nDCG, and access-filtered results on a synthetic corpus. Python base. | **High.** Strong offline candidate; do not imply that toy metrics validate production databases or ANN services. |

## Recommended Follow-Up Order

The audit recommends the following implementation sequence:

1. **Issue A — deterministic Python mathematics and evaluation examples:**
   information theory, evaluation loop, and complex-analysis contour
   quadrature. These require no new runtime profile and have clear assertions.
2. **Issue B — offline retrieval and scoring examples:** retrieval/RAG toy
   ranking, local-LLM scoring, and the Python-for-R-users standard-library
   example. Keep the fixtures synthetic and document their limits.
3. **Issue C — bounded control-flow and CPU autodiff:** the building-agents
   execution loop and one fixed-input PyTorch example. Review the CPU image
   cost before adding CI coverage.
4. **Issue D — shell and Git smoke-test harness:** evaluate whether an isolated
   Bash/Git runner is worth maintaining for Linux/Git and selected shell
   primers. This is separate infrastructure, not an extension of the
   Python/R/Julia manifest runner.
5. **Issue E — static configuration checks:** consider narrowly scoped TOML or
   JSON fixture validation for the Codex and Claude-alternative primers only
   if the source examples are complete and the documented invariants are
   stable.

No migration is recommended for the comparative religion, military structure,
or political systems primers, nor for current Hermes server or OpenClaw service
examples. Their claims are better protected by source review, rendering checks,
and carefully bounded manual verification.

## Runtime and CI Boundaries

The existing runner supports Python, R, and Julia manifests only. The audit
does not justify adding shell, JavaScript, YAML, SQL, container-engine, or live
service execution to the shared CI job. Any new runtime must have a pinned
base, explicit dependencies, an offline probe, a bounded timeout, and a clear
cross-primer need.

Rendering a primer does not execute its code fences. Plot recipes such as
`primer_complex_analysis/generate_plots.R` and the numerical and DSP plotting
recipes are exercised only when their project-specific `plots` or `full`
targets are invoked; they are not automatically covered by the executable
example manifests. Operational scripts must remain outside the shared runner
unless they are first refactored to operate on disposable temporary fixtures.

The inventory should be revisited when a primer's code changes materially or a
runtime dependency is updated. Follow-up migration issues should add only the
examples whose assertion and maintenance contracts are explicit.
