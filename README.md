# ai_assisted_research

AI-assisted research and writing projects — pandoc-based primers, articles, and documents.

## Projects

- `building_ai_agents/` — AI agents primer
- `political_systems/` — European electoral systems primer
- `numerical_analysis_primer/` — Numerical analysis primer
- `claude_code_alternative/` — AI coding agents survey
- `openclaw_primer/` — OpenClaw primer
- `research_local_llms/` — Local LLM research notes
- `silo_rpg_primer/` — Silo RPG primer
- `info_theory_article/` — Information theory article
- `catmodel_elt_documents/` — Catastrophe model ELT documents

## Build

Shared build infrastructure in `_shared/`. Each project has a `Justfile` importing `../_shared/common.just`.

Build all: `just all`
