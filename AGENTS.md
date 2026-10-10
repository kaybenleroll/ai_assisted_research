# Repository Instructions

Read this file, then [CLAUDE.md](CLAUDE.md), then the task-specific document it routes you to. In particular, use [CONTRIBUTING.md](CONTRIBUTING.md) for process and build work and [STYLE_GUIDE.md](STYLE_GUIDE.md) for authored prose.

Codex does not run Claude-specific hooks or load Claude skills or memory from this repository. The repository Git hooks in `.githooks/` block commits and pushes directly to `main`; they apply when configured with `just setup`. Run the relevant commands in the `CLAUDE.md` Definition of Done before opening a PR, and report their results.
