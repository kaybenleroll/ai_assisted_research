set shell := ["bash", "-c"]

default:
  @just --list

# Build the shared pandoc image used by all primer projects
build-image:
  cd building_ai_agents && just build-image

# Per-project render targets
building-ai-html:
  cd building_ai_agents && just html

building-ai-docs:
  cd building_ai_agents && just docs

political-html:
  cd political_systems && just html

numerical-html:
  cd numerical_analysis_primer && just html

openclaw-html:
  cd openclaw_primer && just html

claude-alt-html:
  cd claude_code_alternative && just html

claude-alt-pdf:
  cd claude_code_alternative && just pdf

claude-alt-docs:
  cd claude_code_alternative && just all

research-html:
  cd research_local_llms && just html

catmodel-html-dev:
  cd catmodel_elt_documents && just render-dev-container

catmodel-html-full:
  cd catmodel_elt_documents && just render-full-container

silo-html:
  cd silo_rpg_primer && just silo-html

silo-all:
  cd silo_rpg_primer && just silo-all

info-theory-html:
  cd info_theory_article && just html

info-theory-all:
  cd info_theory_article && just all

deep-learning-html:
  cd deep_learning_primer && just html

deep-learning-pdf:
  cd deep_learning_primer && just pdf

deep-learning-all:
  cd deep_learning_primer && just all

# Common daily build across active document projects
html-dev: building-ai-html building-ai-docs political-html numerical-html openclaw-html research-html catmodel-html-dev claude-alt-html silo-html info-theory-html deep-learning-html
  @echo "✓ Dev HTML render complete across projects"

# Full render where supported
html-full: building-ai-html building-ai-docs political-html numerical-html openclaw-html research-html catmodel-html-full claude-alt-docs silo-all info-theory-all deep-learning-all
  @echo "✓ Full HTML render complete across projects"

clean-generated:
  cd building_ai_agents && just clobber
  cd political_systems && just clobber
  cd numerical_analysis_primer && just clobber
  cd openclaw_primer && just clobber
  cd research_local_llms && just clobber
  cd claude_code_alternative && just clobber
  cd silo_rpg_primer && just silo-clobber
  cd info_theory_article && just clobber
  cd deep_learning_primer && just clobber
  @echo "✓ Generated artifacts cleaned"
