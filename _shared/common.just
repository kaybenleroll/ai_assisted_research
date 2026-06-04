# common.just — shared build recipes for all primers/subprojects
# Each importing Justfile must define these variables before the import line:
#   SOURCE_MD   — source markdown filename (e.g. "primer.md")
#   PROJECT_DIR — project directory name   (e.g. "numerical_analysis_primer")
#   TITLE       — document title
#   AUTHOR      — author/date string
#   HTML_EXTRA  — per-project extra HTML pandoc flags (may be empty string "")
#   PDF_EXTRA   — per-project extra PDF  pandoc flags (may be empty string "")

# OCI runtime detection (podman preferred, fall back to docker)
OCI := `command -v podman >/dev/null 2>&1 && echo podman || echo docker`
OCI_FLAGS := if OCI == "podman" { "--userns=keep-id" } else { "" }
MOUNT_SUFFIX := if OCI == "podman" { ":z" } else { "" }

# Shared image and container-internal paths
IMAGE         := "localhost/primers-pandoc:latest"
TEMPLATE      := "/repo/doc_template.html"
COMPACT_LATEX := "/repo/_shared/pandoc-compact-code.latex"

# Repo root: justfile_directory() is the calling project dir (one level below repo root)
REPO_ROOT := justfile_directory() / ".."

# Derived stem (strips .md extension)
SOURCE_MD_STEM := file_stem(SOURCE_MD)

# Pandoc flag sets
HTML_FLAGS_BASE := "--standalone --embed-resources --toc --toc-depth=3 --syntax-highlighting=breezedark"
PDF_FLAGS_BASE  := "--pdf-engine=xelatex --toc --toc-depth=3 -V geometry:margin=1.2in -V fontsize=11pt -V linestretch=1.25 -V colorlinks=true -V linkcolor=NavyBlue -V urlcolor=NavyBlue -V toc-title='Table of Contents'"

default:
  @just --list

html:
  {{OCI}} run --rm {{OCI_FLAGS}} \
    -v "{{REPO_ROOT}}:/repo{{MOUNT_SUFFIX}}" \
    -w "/repo/{{PROJECT_DIR}}" \
    {{IMAGE}} \
    {{SOURCE_MD}} -o {{SOURCE_MD_STEM}}.html \
    {{HTML_FLAGS_BASE}} {{HTML_EXTRA}} \
    --template="{{TEMPLATE}}" \
    --metadata title="{{TITLE}}" \
    --metadata author="{{AUTHOR}}"

pdf:
  {{OCI}} run --rm {{OCI_FLAGS}} \
    -v "{{REPO_ROOT}}:/repo{{MOUNT_SUFFIX}}" \
    -w "/repo/{{PROJECT_DIR}}" \
    {{IMAGE}} \
    {{SOURCE_MD}} -o {{SOURCE_MD_STEM}}.pdf \
    {{PDF_FLAGS_BASE}} {{PDF_EXTRA}} \
    --include-in-header="{{COMPACT_LATEX}}" \
    --metadata title="{{TITLE}}" \
    --metadata author="{{AUTHOR}}"

all: html pdf

clean:
  @echo "No intermediate build files to clean in {{PROJECT_DIR}}"

clobber:
  rm -fv {{SOURCE_MD_STEM}}.html {{SOURCE_MD_STEM}}.pdf

build-image:
  {{OCI}} build -t {{IMAGE}} -f {{REPO_ROOT}}/_shared/Dockerfile {{REPO_ROOT}}/_shared/
