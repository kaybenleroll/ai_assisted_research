set shell := ["bash", "-c"]

import '_shared/images.just'

OCI := env_var_or_default("OCI", `command -v podman >/dev/null 2>&1 && echo podman || echo docker`)
PYTHON_OCI_FLAGS := if OCI == "podman" { "--userns=keep-id" } else { "--user=" + `id -u` + ":" + `id -g` }
MOUNT_SUFFIX := if OCI == "podman" { ":z" } else { "" }

default:
  @just --list

# Create a Pandoc primer skeleton; finish the printed registration steps before publishing
new-primer $short $title:
  #!/usr/bin/env bash
  set -euo pipefail
  if [[ ! "$short" =~ ^[a-z0-9_]+$ ]]; then
    printf 'Invalid short name: use lowercase letters, digits and underscores.\n' >&2
    exit 1
  fi
  if [[ -z "$title" || "$title" == *$'\n'* ]]; then
    printf 'Title must be non-empty and contain no newline.\n' >&2
    exit 1
  fi
  project_dir="primer_${short}"
  if [[ -e "$project_dir" || -L "$project_dir" ]]; then
    printf '%s already exists.\n' "$project_dir" >&2
    exit 1
  fi
  escape_sed_replacement() {
    printf '%s' "$1" | sed 's/[\\&|]/\\&/g'
  }
  source_title="$(escape_sed_replacement "$title")"
  just_title="$(printf '%s' "$title" | sed 's/[\\"]/\\&/g')"
  just_title="$(escape_sed_replacement "$just_title")"
  project_value="$(escape_sed_replacement "$project_dir")"
  review_date="$(LC_ALL=C date '+%e %B %Y' | sed 's/^ //')"
  mkdir "$project_dir"
  trap 'rm -f "$project_dir/Justfile" "$project_dir/$project_dir.md"; rmdir "$project_dir"' ERR
  sed -e "s|@@PROJECT_DIR@@|$project_value|g" -e "s|@@JUST_TITLE@@|$just_title|g" \
    -e "s|@@DATE@@|$review_date|g" \
    _shared/templates/primer/Justfile.tmpl > "$project_dir/Justfile"
  sed "s|@@TITLE@@|$source_title|g" \
    _shared/templates/primer/primer.md.tmpl > "$project_dir/$project_dir.md"
  trap - ERR
  printf 'Created %s. Next:\n' "$project_dir"
  printf '%s\n' \
    '  - Set AUTHOR; update DATE after the substantive review.' \
    '  - Draft and verify the primer against STYLE_GUIDE.md.' \
    '  - Add top-level Justfile targets.' \
    '  - Register source and outputs in scripts/update_readme_recent.py; run just readme.' \
    '  - Add and synchronise an area label in .github/labels.json if this is a new class.' \
    '  - Add the directory to the CLAUDE.md document-class list.' \
    '  - Render in containers and commit the source, Justfile, HTML and PDF together.'

# Generate the README document tables from Justfile review dates
readme:
  {{OCI}} run --rm {{PYTHON_OCI_FLAGS}} -v "{{justfile_directory()}}:/repo{{MOUNT_SUFFIX}}" -w /repo {{PYTHON_IMAGE}} python scripts/update_readme_recent.py

# Check README generation without changing files
readme-check:
  {{OCI}} run --rm {{PYTHON_OCI_FLAGS}} -v "{{justfile_directory()}}:/repo{{MOUNT_SUFFIX}}" -w /repo {{PYTHON_IMAGE}} python3 -I scripts/update_readme_recent.py --check

# Check committed metadata, renderer variants, Mermaid, freshness, and README generation
check: check-meta check-variants check-mermaid check-fresh check-readme

check-meta:
  {{OCI}} run --rm {{PYTHON_OCI_FLAGS}} -v "{{justfile_directory()}}:/repo{{MOUNT_SUFFIX}}" -w /repo {{PYTHON_IMAGE}} python3 -I scripts/check/check.py meta

check-variants:
  {{OCI}} run --rm {{PYTHON_OCI_FLAGS}} -v "{{justfile_directory()}}:/repo{{MOUNT_SUFFIX}}" -w /repo {{PYTHON_IMAGE}} python3 -I scripts/check/check.py variants

check-mermaid:
  {{OCI}} run --rm {{PYTHON_OCI_FLAGS}} -v "{{justfile_directory()}}:/repo{{MOUNT_SUFFIX}}" -w /repo {{PYTHON_IMAGE}} python3 -I scripts/check/check.py mermaid

check-fresh:
  {{OCI}} run --rm {{PYTHON_OCI_FLAGS}} -v "{{justfile_directory()}}:/repo{{MOUNT_SUFFIX}}" -w /repo {{PYTHON_IMAGE}} python3 -I scripts/check/check.py fresh

check-readme: readme-check

# Build the pinned spelling checker image
build-lint-image:
  {{OCI}} build --build-arg PYTHON_IMAGE={{PYTHON_IMAGE}} -t {{LINT_IMAGE}} -f _shared/Dockerfile.lint _shared/

# Check every in-scope Markdown source with spelling, structure, and prose rules
lint:
  bash scripts/lint.sh

# Check Markdown structure and accessibility without the spelling checker
lint-md *FILES:
  bash scripts/lint.sh --md {{FILES}}

# Check House prose rules, or only the named Markdown files
lint-prose *FILES:
  bash scripts/lint.sh --prose {{FILES}}

# Assert each House rule's passing and failing fixture
lint-prose-test:
  bash scripts/lint.sh --prose-test

# Check Markdown files changed since BASE_REF (default: origin/main)
lint-changed:
  bash scripts/lint.sh --changed

# Check all in-scope files, or only the named Markdown files
lint-spell *FILES:
  bash scripts/lint.sh --spell {{FILES}}

# Build the shared pandoc image used by all primer projects
build-image:
  {{OCI}} build -t {{IMAGE}} -f _shared/Dockerfile _shared/

# Configure hooks and fetch the two images used by primer builds
setup:
  git config core.hooksPath .githooks
  just build-image
  {{OCI}} pull {{ROCKER}}

# Per-project render targets
building-ai-html:
  cd primer_building_ai_agents && just html

building-ai-docs:
  cd primer_building_ai_agents && just docs

political-html:
  cd primer_political_systems && just html

political-all:
  cd primer_political_systems && just all

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

deep-learning-html:
  cd primer_deep_learning && just html

deep-learning-pdf:
  cd primer_deep_learning && just pdf

deep-learning-all:
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
  cd primer_evaluation_loop && just all

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

pi-agent-html:
  cd primer_pi_coding_agent && just html

pi-agent-pdf:
  cd primer_pi_coding_agent && just pdf

pi-agent-all:
  cd primer_pi_coding_agent && just all

complex-analysis-html:
  cd primer_complex_analysis && just html

complex-analysis-pdf:
  cd primer_complex_analysis && just pdf

complex-analysis-all:
  cd primer_complex_analysis && just full

# Common daily build across active document projects
html-dev: pi-agent-html building-ai-html building-ai-docs political-html numerical-html openclaw-html hermes-server-html research-html catmodel-html-dev claude-alt-html codex-claude-html silo-html deep-learning-html digital-signal-processing-html eval-loop-html python-r-html military-html ohmyzsh-html comparative-religion-html containerization-html complex-analysis-html
  @echo "✓ Dev HTML render complete across projects"

# Full render where supported
html-full: pi-agent-all building-ai-html building-ai-docs political-html numerical-html openclaw-html hermes-server-all research-html catmodel-html-full claude-alt-docs codex-claude-docs silo-all deep-learning-all digital-signal-processing-all eval-loop-all python-r-all military-all ohmyzsh-all comparative-religion-all containerization-all complex-analysis-all
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
  cd primer_deep_learning && just clobber
  cd primer_digital_signal_processing && just clobber
  cd primer_evaluation_loop && just clobber
  cd primer_military_structure && just clobber
  cd primer_ohmyzsh && just clobber
  cd primer_containerization && just clobber
  cd primer_pi_coding_agent && just clobber
  cd primer_complex_analysis && just clobber
  @echo "✓ Generated artifacts cleaned"
