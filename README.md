# AI-Assisted Research

AI-assisted research and writing projects — long-form technical primers and reference material.

Browse the documents below or visit the [GitHub Pages site](https://kaybenleroll.github.io/ai_assisted_research/).

---

## AI Agents and Coding Tools

| Document | Description |
|----------|-------------|
| [Building Autonomous AI Agents](primer_building_ai_agents/primer_ai_agents_comprehensive.html) · [PDF](primer_building_ai_agents/primer_ai_agents_comprehensive.pdf) | Comprehensive guide to designing and implementing agentic AI systems. Companion: [Agent Architecture Quick Reference](primer_building_ai_agents/primer_agent_quick_reference.html) |
| [Claude Code Alternatives](primer_claude_code_alternative/primer-claude-code-alternatives.html) · [PDF](primer_claude_code_alternative/primer-claude-code-alternatives.pdf) | Survey of AI coding agents, September 2026 refresh |
| [Codex for Claude Code Users](primer_codex_for_claude_code_users/primer-codex-for-claude-code-users.html) · [PDF](primer_codex_for_claude_code_users/primer-codex-for-claude-code-users.pdf) | Practical guide to running Codex alongside Claude Code in one repository |
| [The Evaluation Loop](primer_evaluation_loop/primer_evaluation_loop.html) · [PDF](primer_evaluation_loop/primer_evaluation_loop.pdf) | Turning subjective AI task quality into numeric evals: verifiable rewards, RLHF/DSPy, and Goodhart failure modes |
| [Hermes Agent Server](primer_hermes_server/primer_hermes_server.html) · [PDF](primer_hermes_server/primer_hermes_server.pdf) | Guide to the Hermes Server framework |
| [OpenClaw](primer_openclaw/primer_openclaw.html) · [PDF](primer_openclaw/primer_openclaw.pdf) | Podman-first guide to the OpenClaw framework |
| [Running LLMs Locally](primer_research_local_llms/primer-running-llms-locally.html) · [PDF](primer_research_local_llms/primer-running-llms-locally.pdf) | Landscape of options for running language models on local hardware |

## Developer Tooling

| Document | Description |
|----------|-------------|
| [Containerization: Docker, Podman, and How Kubernetes Fits In](primer_containerization/primer_containerization.html) · [PDF](primer_containerization/primer_containerization.pdf) | Container fundamentals and the OCI spec, Docker's daemon architecture versus Podman's daemonless model, and how Kubernetes orchestrates it all |
| [Oh My Zsh: A Practical Guide](primer_ohmyzsh/primer_ohmyzsh.html) · [PDF](primer_ohmyzsh/primer_ohmyzsh.pdf) | ZSH fundamentals, Oh My Zsh architecture, deep plugin coverage, themes, advanced features, and a personalised setup audit |
| [Python for Expert R Users](primer_python_for_r_users/primer_python_for_r_users.html) · [PDF](primer_python_for_r_users/primer_python_for_r_users.pdf) | Comprehensive migration guide for experienced tidyverse, purrr, and furrr users, with deep ggplot2 replacement strategy |

## Quantitative Foundations

| Document | Description |
|----------|-------------|
| [Catastrophe ELT Workbook](workbook_catmodel_elt_documents/outputs/workbook_elt.html) | *Quarto workbook, executable.* Catastrophe event-loss-table modelling — building and validating an ELT pipeline in R and Python. Companions: [Quickstart](workbook_catmodel_elt_documents/outputs/workbook_quickstart.html) · [Executable Index](workbook_catmodel_elt_documents/outputs/workbook_executable_index.html) |
| [Deep Learning and Generative AI](primer_deep_learning/primer_deep_learning.html) · [PDF](primer_deep_learning/primer_deep_learning.pdf) | Neural networks, transformers, LLMs, and generative AI — architecture, training, and practical use |
| [Information Theory Series](article_info_theory/information_theory_series_combined.html) · [PDF](article_info_theory/information_theory_series_combined.pdf) | *Article series.* Entropy, mutual information, channel capacity, and their applications |
| [Numerical Analysis](primer_numerical_analysis/primer_numerical_analysis.html) · [PDF](primer_numerical_analysis/primer_numerical_analysis.pdf) | Floating-point arithmetic, linear algebra, root finding, ODEs, optimisation, eigenvalues, AD, and regularisation |

## Society and Institutions

| Document | Description |
|----------|-------------|
| [Comparative Religion](primer_comparative_religion/primer-comparative-religion.html) · [PDF](primer_comparative_religion/primer-comparative-religion.pdf) | Scripture, doctrine, community structure, liturgy, and internal diversity across Judaism, Christianity, Islam, Hinduism, Sikhism, Buddhism, and Shinto |
| [European Electoral Systems](primer_political_systems/primer-european-electoral-systems.html) · [PDF](primer_political_systems/primer-european-electoral-systems.pdf) | Practical primer on electoral systems across European democracies |
| [Military Organisation, Ranks, and Doctrine](primer_military_structure/primer_military_structure.html) · [PDF](primer_military_structure/primer_military_structure.pdf) | How armies are structured from fire team to army group, how ranks map to command levels, and naval/air force equivalents |

## Silo RPG Materials

| Document | Description |
|----------|-------------|
| [Document Index](gaming_silo_rpg/gaming_silo_index.html) · [PDF](gaming_silo_rpg/gaming_silo_index.pdf) | Navigation map for all Silo RPG source documents |
| [Comprehensive World Bible](gaming_silo_rpg/gaming_silo_comprehensive_bible.html) · [PDF](gaming_silo_rpg/gaming_silo_comprehensive_bible.pdf) | Full world reference — history, factions, technology, and geography |
| [Game Master's Secrets](gaming_silo_rpg/gaming_silo_gm_secrets.html) · [PDF](gaming_silo_rpg/gaming_silo_gm_secrets.pdf) | GM-only lore, hidden mechanics, and macro-level world state |
| [Player's Survival Guide](gaming_silo_rpg/gaming_silo_player_guide.html) · [PDF](gaming_silo_rpg/gaming_silo_player_guide.pdf) | Player-facing rules, setting knowledge, and character options |
| [Starter Campaigns](gaming_silo_rpg/gaming_silo_starter_campaign.html) · [PDF](gaming_silo_rpg/gaming_silo_starter_campaign.pdf) | Introductory campaign scenarios and player archetypes |

---

## Build

Shared build infrastructure lives in `_shared/`. Each primer has a thin `Justfile` that sets variables and imports `../_shared/common.just`.

```
# Render a specific primer
cd primer_numerical_analysis && just all

# Generate figures then render (primers with plots)
cd primer_numerical_analysis && just full
```

`workbook_catmodel_elt_documents/` uses its own Quarto + R + Python pipeline (see its `Justfile` and `Dockerfile`), not the pandoc infrastructure; rendered outputs live in `workbook_catmodel_elt_documents/outputs/`.
