# Repository maintenance

This directory contains the machinery and guidance used to maintain the publication collection. Run the documented `just` commands from the repository root or the relevant publication directory.

| Directory | Purpose |
|---|---|
| [docs](docs/project-contract.md) | Project contract, production procedures, review guidance and templates. |
| [build](build/common.just) | Shared recipes, container definitions, filters, document template and executable-example runner. |
| [scripts](scripts) | Repository checks, README generation, lint orchestration and render QA. |
| [tests](tests) | Regression tests and their fixtures. |
| [lint](lint) | Enforcement manifests, advisory baselines and prose-rule fixtures. |

Publications remain in their existing top-level directories. The root [contributor guide](../CONTRIBUTING.md), [style guide](../STYLE_GUIDE.md), [agent entry point](../AGENTS.md) and `Justfile` remain the main entry points. Hidden harness, CI and tool configuration directories stay in their conventional discovery locations.

The `maintenance/` directory is excluded from the published Pages site. Its files remain available in the repository.
