#!/usr/bin/env bash
set -euo pipefail

repo_root="$(git rev-parse --show-toplevel)"
cd "$repo_root"

mode=all
case "${1:-}" in
  --md) mode=md; shift ;;
  --spell) mode=spell; shift ;;
  --prose) mode=prose; shift ;;
  --prose-test) mode=prose-test; shift ;;
esac

if [[ -n "${OCI:-}" ]]; then
  runtime="$OCI"
elif command -v podman >/dev/null 2>&1; then
  runtime=podman
else
  runtime=docker
fi

files=()
if [[ "$mode" == prose-test ]]; then
  files=(lint/fixtures/vale/*.md)
elif [[ "${1:-}" == --changed ]]; then
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

run_prose() {
  local report_mode=$1 vale_status=0 report_status=0
  shift
  local prose_files=() path vale_output
  for path in "$@"; do
    if [[ "$path" != primer_political_systems/complete_prompt.md ]]; then
      prose_files+=("$path")
    fi
  done
  if (( ${#prose_files[@]} == 0 )); then
    printf 'SUMMARY Vale files=0 enforced=0 advisory=0\n'
    return 0
  fi
  vale_output=$("$runtime" run --rm "${identity[@]}" -v "$repo_root:/repo$mount_suffix" -w /repo \
    "${VALE_IMAGE:-docker.io/jdkato/vale:v3.24.0}" --output=JSON "${prose_files[@]}") || vale_status=$?
  if (( vale_status > 1 )) || [[ -z "$vale_output" ]]; then
    printf 'Vale failed with status %s\n' "$vale_status" >&2
    return 2
  fi
  printf '%s' "$vale_output" | "$runtime" run --rm -i "${identity[@]}" \
    -v "$repo_root:/repo$mount_suffix" -w /repo \
    "${LINT_IMAGE:-localhost/primers-lint:1.51.1}" \
    python3 -I scripts/lint_prose_report.py "$report_mode" "${prose_files[@]}" || report_status=$?
  if [[ "$report_mode" == --report ]]; then
    "$runtime" run --rm "${identity[@]}" -v "$repo_root:/repo$mount_suffix" -w /repo \
      "${LINT_IMAGE:-localhost/primers-lint:1.51.1}" \
      python3 -I scripts/filler_density.py "${prose_files[@]}" || return $?
  fi
  return "$report_status"
}

if [[ "$runtime" == podman ]]; then
  identity=(--userns=keep-id)
  mount_suffix=:z
else
  identity=(--user="$UID")
  mount_suffix=
fi

if [[ "$mode" == prose || "$mode" == prose-test ]]; then
  if [[ "$mode" == prose-test ]]; then
    run_prose --fixtures "${files[@]}"
  else
    run_prose --report "${files[@]}"
  fi
  exit $?
fi

spell_status=0
if [[ "$mode" != md ]]; then
  "$runtime" run --rm "${identity[@]}" -v "$repo_root:/repo$mount_suffix" -w /repo \
    "${LINT_IMAGE:-localhost/primers-lint:1.51.1}" \
    python3 -I scripts/lint_report.py "${files[@]}" || spell_status=$?
  if [[ "$mode" == spell ]]; then
    exit "$spell_status"
  fi
fi

md_files=()
for path in "${files[@]}"; do
  if [[ "$path" != primer_political_systems/complete_prompt.md ]]; then
    case "$path" in
      README.md|primer_*/*.md|gaming_silo_rpg/*.md) ;;
      *) printf 'lint configuration error: out-of-scope path: %s\n' "$path" >&2; exit 2 ;;
    esac
    if [[ "$path" == */*/* || ! -f "$path" ]]; then
      printf 'lint configuration error: missing or out-of-scope path: %s\n' "$path" >&2
      exit 2
    fi
    md_files+=("$path")
  fi
done

declare -A enforced_paths=() file_counts=() rule_counts=()
while IFS= read -r entry || [[ -n "$entry" ]]; do
  [[ -z "$entry" || "$entry" == \#* ]] && continue
  case "$entry" in
    primer_*/*.md) ;;
    *) printf 'lint configuration error: out-of-scope manifest path: %s\n' "$entry" >&2; exit 2 ;;
  esac
  if [[ "$entry" == */*/* || "$entry" == primer_political_systems/complete_prompt.md || ! -f "$entry" ]]; then
    printf 'lint configuration error: stale or out-of-scope manifest path: %s\n' "$entry" >&2
    exit 2
  fi
  if [[ -v enforced_paths["$entry"] ]]; then
    printf 'lint configuration error: duplicate manifest path: %s\n' "$entry" >&2
    exit 2
  fi
  enforced_paths["$entry"]=1
done < lint/enforced-structure.txt

md_status=0
md_output=
if (( ${#md_files[@]} )); then
  md_output=$("$runtime" run --rm "${identity[@]}" -v "$repo_root:/repo$mount_suffix" -w /repo \
    "${MDLINT_IMAGE:-docker.io/davidanson/markdownlint-cli2:v0.23.3}" \
    -- "${md_files[@]}" 2>&1) || md_status=$?
fi

enforced_count=0
advisory_count=0
parsed_count=0
while IFS= read -r line; do
  if [[ "$line" =~ ^(.+\.md):([0-9]+)(:[0-9]+)?\ error\ (MD[0-9]{3})/ ]]; then
    path="${BASH_REMATCH[1]}"
    rule="${BASH_REMATCH[4]}"
    category=ADVISORY
    if [[ "$rule" == MD040 || "$rule" == MD045 ]] || \
       { [[ "$rule" == MD001 || "$rule" == MD025 || "$rule" == MD034 ]] && [[ -v enforced_paths["$path"] ]]; }; then
      category=ENFORCED
      (( enforced_count += 1 ))
    else
      (( advisory_count += 1 ))
    fi
    (( parsed_count += 1 ))
    (( file_counts["$path"] += 1 ))
    (( rule_counts["$rule"] += 1 ))
    printf '%s %s\n' "$category" "$line"
  elif [[ -n "$line" ]]; then
    printf '%s\n' "$line"
  fi
done <<< "$md_output"

if (( md_status > 1 || (md_status == 1 && parsed_count == 0) )); then
  printf 'markdownlint failed with status %s\n' "$md_status" >&2
  exit "${md_status:-2}"
fi
for path in "${md_files[@]}"; do
  printf 'BASELINE %s: %s\n' "$path" "${file_counts[$path]:-0}"
done
for rule in MD001 MD003 MD004 MD025 MD034 MD036 MD040 MD045 MD046 MD048 MD049 MD050 MD051 MD059; do
  printf 'BASELINE %s: %s\n' "$rule" "${rule_counts[$rule]:-0}"
done
printf 'SUMMARY markdownlint files=%s enforced=%s advisory=%s\n' \
  "${#md_files[@]}" "$enforced_count" "$advisory_count"

prose_status=0
if [[ "$mode" == all ]]; then
  run_prose --report "${files[@]}" || prose_status=$?
fi

if (( enforced_count || spell_status || prose_status )); then
  exit 1
fi
