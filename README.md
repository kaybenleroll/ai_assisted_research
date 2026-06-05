# AI-Assisted Research

AI-assisted research and writing projects — long-form technical primers, articles, and documents rendered to HTML and PDF via pandoc.

Browse the documents below or visit the [GitHub Pages site](https://kaybenleroll.github.io/ai_assisted_research/).

---

## Technical Primers

| Document | Description |
|----------|-------------|
| [Deep Learning and Generative AI](deep_learning_primer/deep_learning_primer.html) | Neural networks, transformers, LLMs, and generative AI — architecture, training, and practical use |
| [Numerical Analysis Primer](numerical_analysis_primer/numerical_analysis_primer.html) | Floating-point arithmetic, linear algebra, root finding, ODEs, optimisation, eigenvalues, AD, and regularisation |
| [Building Autonomous AI Agents](building_ai_agents/ai_agents_comprehensive_primer.html) | Comprehensive guide to designing and implementing agentic AI systems |
| [Agent Implementation Quick Reference](building_ai_agents/agent_quick_reference.html) | Condensed reference card for common agent patterns |
| [OpenClaw Primer](openclaw_primer/openclaw_primer.html) | Podman-first guide to the OpenClaw framework |
| [Running LLMs Locally](research_local_llms/running-llms-locally.html) | Landscape of options for running language models on local hardware |
| [Claude Code Alternatives](claude_code_alternative/claude-code-alternatives.html) | Survey of AI coding agents as of 2026 |
| [The Evaluation Loop](evaluation_loop_primer/evaluation_loop_primer.html) | Turning subjective AI task quality into numeric evals: the four moves, verifiable rewards, RLHF/DSPy, Goodhart failure modes, agent evaluation |

## Articles

| Document | Description |
|----------|-------------|
| [Information Theory Series](info_theory_article/information_theory_series_combined.html) | Entropy, mutual information, channel capacity, and their applications |

## Politics

| Document | Description |
|----------|-------------|
| [European Electoral Systems](political_systems/european-electoral-systems-primer.html) | Practical primer on electoral systems across European democracies |

## Silo RPG Materials

| Document | Description |
|----------|-------------|
| [Document Index](silo_rpg_primer/silo_index.html) | Navigation map for all Silo RPG source documents |
| [Player's Survival Guide](silo_rpg_primer/silo_player_guide.html) | Player-facing rules, setting knowledge, and character options |
| [Game Master's Secrets](silo_rpg_primer/silo_gm_secrets.html) | GM-only lore, hidden mechanics, and macro-level world state |
| [Comprehensive World Bible](silo_rpg_primer/silo_comprehensive_bible.html) | Full world reference — history, factions, technology, and geography |
| [Starter Campaigns](silo_rpg_primer/silo_starter_campaign.html) | Introductory campaign scenarios and player archetypes |

---

## Build

Shared build infrastructure lives in `_shared/`. Each primer has a thin `Justfile` that sets variables and imports `../_shared/common.just`.

```
# Render a specific primer
cd numerical_analysis_primer && just all

# Generate figures then render (primers with plots)
cd numerical_analysis_primer && just full
```

The `catmodel_elt_documents/` directory uses a separate Quarto + R + Python pipeline and does not use the pandoc infrastructure.
