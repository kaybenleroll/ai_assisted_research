set shell := ["bash", "-c"]

default:
  @just --list

# Build the shared pandoc image used by all primer projects
build-image:
  cd primer_building_ai_agents && just build-image

# Per-project render targets
building-ai-html:
  cd primer_building_ai_agents && just html

building-ai-docs:
  cd primer_building_ai_agents && just docs

political-html:
  cd primer_political_systems && just html

political-all:
  cd primer_political_systems && just all-docs

numerical-html:
  cd primer_numerical_analysis && just html

numerical-all:
  cd primer_numerical_analysis && just full

openclaw-html:
  cd primer_openclaw && just html

hermes-server-html:
  cd primer_hermes_server && just html

hermes-server-pdf:
  cd primer_hermes_server && just pdf

hermes-server-all:
  cd primer_hermes_server && just all

claude-alt-html:
  cd primer_claude_code_alternative && just html

claude-alt-pdf:
  cd primer_claude_code_alternative && just pdf

claude-alt-docs:
  cd primer_claude_code_alternative && just all

codex-claude-html:
  cd primer_codex_for_claude_code_users && just html

codex-claude-pdf:
  cd primer_codex_for_claude_code_users && just pdf

codex-claude-docs:
  cd primer_codex_for_claude_code_users && just all

research-html:
  cd primer_research_local_llms && just html

catmodel-html-dev:
  cd workbook_catmodel_elt_documents && just render-dev-container

catmodel-html-full:
  cd workbook_catmodel_elt_documents && just render-full-container

silo-html:
  cd gaming_silo_rpg && just silo-html

silo-all:
  cd gaming_silo_rpg && just silo-all

info-theory-html:
  cd article_info_theory && just html

info-theory-all:
  cd article_info_theory && just all-docs

deep-learning-html:
  cd primer_deep_learning && just html

deep-learning-pdf:
  cd primer_deep_learning && just pdf

deep-learning-all:
  cd primer_deep_learning && just html-variants
  cd primer_deep_learning && just all

digital-signal-processing-html:
  cd primer_digital_signal_processing && just html

digital-signal-processing-pdf:
  cd primer_digital_signal_processing && just pdf

digital-signal-processing-all:
  cd primer_digital_signal_processing && just full

eval-loop-html:
  cd primer_evaluation_loop && just html

eval-loop-pdf:
  cd primer_evaluation_loop && just pdf

eval-loop-all:
  cd primer_evaluation_loop && just all-docs

python-r-html:
  cd primer_python_for_r_users && just html

python-r-pdf:
  cd primer_python_for_r_users && just pdf

python-r-all:
  cd primer_python_for_r_users && just all

military-html:
  cd primer_military_structure && just html

military-pdf:
  cd primer_military_structure && just pdf

military-all:
  cd primer_military_structure && just all

ohmyzsh-html:
  cd primer_ohmyzsh && just html

ohmyzsh-pdf:
  cd primer_ohmyzsh && just pdf

ohmyzsh-all:
  cd primer_ohmyzsh && just all

comparative-religion-html:
  cd primer_comparative_religion && just html

comparative-religion-pdf:
  cd primer_comparative_religion && just pdf

comparative-religion-all:
  cd primer_comparative_religion && just all

containerization-html:
  cd primer_containerization && just html

containerization-pdf:
  cd primer_containerization && just pdf

containerization-all:
  cd primer_containerization && just all

# Common daily build across active document projects
html-dev: building-ai-html building-ai-docs political-html numerical-html openclaw-html hermes-server-html research-html catmodel-html-dev claude-alt-html codex-claude-html silo-html info-theory-html deep-learning-html digital-signal-processing-html eval-loop-html python-r-html military-html ohmyzsh-html comparative-religion-html containerization-html
  @echo "✓ Dev HTML render complete across projects"

# Full render where supported
html-full: building-ai-html building-ai-docs political-html numerical-html openclaw-html hermes-server-all research-html catmodel-html-full claude-alt-docs codex-claude-docs silo-all info-theory-all deep-learning-all digital-signal-processing-all eval-loop-all python-r-all military-all ohmyzsh-all comparative-religion-all containerization-all
  @echo "✓ Full HTML render complete across projects"

clean-generated:
  cd primer_building_ai_agents && just clobber
  cd primer_political_systems && just clobber
  cd primer_numerical_analysis && just clobber
  cd primer_openclaw && just clobber
  cd primer_hermes_server && just clobber
  cd primer_research_local_llms && just clobber
  cd primer_claude_code_alternative && just clobber
  cd primer_codex_for_claude_code_users && just clobber
  cd gaming_silo_rpg && just silo-clobber
  cd article_info_theory && just clobber
  cd primer_deep_learning && just clobber
  cd primer_digital_signal_processing && just clobber
  cd primer_evaluation_loop && just clobber
  cd primer_military_structure && just clobber
  cd primer_ohmyzsh && just clobber
  cd primer_containerization && just clobber
  @echo "✓ Generated artifacts cleaned"
