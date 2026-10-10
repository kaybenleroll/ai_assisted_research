#!/usr/bin/env bash
set -euo pipefail

repo_root="$(git rev-parse --show-toplevel)"
cd "$repo_root"

if [[ -n "${OCI:-}" ]]; then
  runtime="$OCI"
elif command -v podman >/dev/null 2>&1; then
  runtime=podman
else
  runtime=docker
fi

files=()
if [[ "${1:-}" == --changed ]]; then
  base_ref="${BASE_REF:-origin/main}"
  git rev-parse --verify "${base_ref}^{commit}" >/dev/null
  while IFS= read -r -d '' path; do
    case "$path" in
      README.md|primer_*/*.md|gaming_silo_rpg/*.md)
        if [[ "$path" != primer_building_ai_agents/README.md ]]; then
          files+=("$path")
        fi
        ;;
    esac
  done < <(git diff --name-only -z --diff-filter=AMR "${base_ref}...HEAD" -- '*.md')
elif (( $# )); then
  files=("$@")
else
  while IFS= read -r -d '' path; do
    files+=("$path")
  done < <(git ls-files -z -- 'README.md' 'primer_*/*.md' 'gaming_silo_rpg/*.md')
fi

if [[ "$runtime" == podman ]]; then
  identity=(--userns=keep-id)
  mount_suffix=:z
else
  identity=(--user="$UID")
  mount_suffix=
fi

"$runtime" run --rm "${identity[@]}" -v "$repo_root:/repo$mount_suffix" -w /repo \
  "${LINT_IMAGE:-localhost/primers-lint:1.51.1}" \
  python3 -I scripts/lint_report.py "${files[@]}"
