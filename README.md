# AI-Assisted Research

AI-assisted research and writing projects — long-form technical primers, articles, and documents rendered to HTML and PDF via pandoc.

Browse the documents below or visit the [GitHub Pages site](https://kaybenleroll.github.io/ai_assisted_research/).

---

## Technical Primers

| Document | Description |
|----------|-------------|
| [Deep Learning and Generative AI](primer_deep_learning/primer_deep_learning.html) | Neural networks, transformers, LLMs, and generative AI — architecture, training, and practical use |
| [Numerical Analysis Primer](primer_numerical_analysis/primer_numerical_analysis.html) | Floating-point arithmetic, linear algebra, root finding, ODEs, optimisation, eigenvalues, AD, and regularisation |
| [Building Autonomous AI Agents](primer_building_ai_agents/primer_ai_agents_comprehensive.html) | Comprehensive guide to designing and implementing agentic AI systems |
| [Agent Implementation Quick Reference](primer_building_ai_agents/primer_agent_quick_reference.html) | Condensed reference card for common agent patterns |
| [OpenClaw Primer](primer_openclaw/primer_openclaw.html) | Podman-first guide to the OpenClaw framework |
| [Hermes Server Primer](primer_hermes_server/primer_hermes_server.html) | Guide to the Hermes Server framework |
| [Running LLMs Locally](primer_research_local_llms/primer-running-llms-locally.html) | Landscape of options for running language models on local hardware |
| [Claude Code Alternatives](primer_claude_code_alternative/primer-claude-code-alternatives.html) | Survey of AI coding agents, mid-2026 refresh |
| [Codex for Claude Code Users](primer_codex_for_claude_code_users/primer-codex-for-claude-code-users.html) | Practical guide to running Codex alongside Claude Code in one repository |
| [The Evaluation Loop](primer_evaluation_loop/primer_evaluation_loop.html) | Turning subjective AI task quality into numeric evals: the four moves, verifiable rewards, RLHF/DSPy, Goodhart failure modes, agent evaluation |
| [Python for Expert R Users](primer_python_for_r_users/primer_python_for_r_users.html) | Comprehensive migration guide for experienced tidyverse, purrr, and furrr users, with deep ggplot2 replacement strategy |
| [Military Organisation, Ranks, and Doctrine](primer_military_structure/primer_military_structure.html) | How armies are structured from fire team to army group, how ranks map to command levels, the Napoleonic inheritance, 20th-century adaptations, and naval/air force equivalents |
| [Oh My Zsh: A Practical Guide](primer_ohmyzsh/primer_ohmyzsh.html) | ZSH fundamentals, Oh My Zsh architecture, deep plugin coverage, themes, advanced features, and a personalised setup audit |

## Articles

| Document | Description |
|----------|-------------|
| [Information Theory Series](article_info_theory/information_theory_series_combined.html) | Entropy, mutual information, channel capacity, and their applications |

## Politics

| Document | Description |
|----------|-------------|
| [European Electoral Systems](primer_political_systems/primer-european-electoral-systems.html) | Practical primer on electoral systems across European democracies |

## Religion

| Document | Description |
|----------|-------------|
| [Comparative Religion](primer_comparative_religion/primer-comparative-religion.html) | Scripture, doctrine, community structure, liturgy, and internal diversity across Judaism, Christianity, Islam, Hinduism, Sikhism, Buddhism, and Shinto |

## Silo RPG Materials

| Document | Description |
|----------|-------------|
| [Document Index](gaming_silo_rpg/gaming_silo_index.html) | Navigation map for all Silo RPG source documents |
| [Player's Survival Guide](gaming_silo_rpg/gaming_silo_player_guide.html) | Player-facing rules, setting knowledge, and character options |
| [Game Master's Secrets](gaming_silo_rpg/gaming_silo_gm_secrets.html) | GM-only lore, hidden mechanics, and macro-level world state |
| [Comprehensive World Bible](gaming_silo_rpg/gaming_silo_comprehensive_bible.html) | Full world reference — history, factions, technology, and geography |
| [Starter Campaigns](gaming_silo_rpg/gaming_silo_starter_campaign.html) | Introductory campaign scenarios and player archetypes |

---

## Build

Shared build infrastructure lives in `_shared/`. Each primer has a thin `Justfile` that sets variables and imports `../_shared/common.just`.

```
# Render a specific primer
cd primer_numerical_analysis && just all

# Generate figures then render (primers with plots)
cd primer_numerical_analysis && just full
```

The `workbook_catmodel_elt_documents/` directory uses a separate Quarto + R + Python pipeline and does not use the pandoc infrastructure.
