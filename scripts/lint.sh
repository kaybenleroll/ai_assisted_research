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
  --links) mode=links; shift ;;
  --links-online) mode=links-online; shift ;;
esac

if [[ -n "${OCI:-}" ]]; then
  runtime="$OCI"
elif command -v podman >/dev/null 2>&1; then
  runtime=podman
else
  runtime=docker
fi

files=()
if [[ "$mode" == links ]]; then
  if (( $# )); then
    files=("$@")
  else
    while IFS= read -r -d '' path; do
      files+=("$path")
    done < <(git ls-files -z -- 'README.md' 'primer_*/*.html' \
      'gaming_silo_rpg/*.html' 'workbook_catmodel_elt_documents/outputs/*.html')
  fi
elif [[ "$mode" == prose-test ]]; then
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

run_links() {
  local link_mode=$1 lychee_status=0 output line path current_path= report_total=0 report_seen=0
  local enforced_count=0 advisory_count=0
  local link_files=() manifest_path
  local -A enforced_paths=() file_counts=()
  shift

  if [[ "$link_mode" == offline ]]; then
    while IFS= read -r -d '' path; do
      link_files+=("$path")
    done < <(git ls-files -z -- 'README.md' 'primer_*/*.html' \
      'gaming_silo_rpg/*.html' 'workbook_catmodel_elt_documents/outputs/*.html')
    local -A tracked_paths=()
    for path in "${link_files[@]}"; do
      tracked_paths["$path"]=1
    done
    while IFS= read -r manifest_path || [[ -n "$manifest_path" ]]; do
      [[ -z "$manifest_path" || "$manifest_path" == \#* ]] && continue
      if [[ ! -v tracked_paths["$manifest_path"] || ! -f "$manifest_path" ]]; then
        printf 'link configuration error: stale or out-of-scope manifest path: %s\n' "$manifest_path" >&2
        return 2
      fi
      if [[ -v enforced_paths["$manifest_path"] ]]; then
        printf 'link configuration error: duplicate manifest path: %s\n' "$manifest_path" >&2
        return 2
      fi
      enforced_paths["$manifest_path"]=1
    done < lint/enforced-links.txt
    if (( $# )); then
      link_files=("$@")
      for path in "${link_files[@]}"; do
        if [[ ! -v tracked_paths["$path"] ]]; then
          printf 'link configuration error: out-of-scope path: %s\n' "$path" >&2
          return 2
        fi
      done
    fi
  else
    if (( $# == 0 )); then
      while IFS= read -r -d '' path; do
        link_files+=("$path")
      done < <(git ls-files -z -- 'README.md' 'primer_*/*.md' 'gaming_silo_rpg/*.md')
    else
      link_files=("$@")
    fi
    local filtered_files=()
    for path in "${link_files[@]}"; do
      [[ "$path" == primer_political_systems/complete_prompt.md || \
         "$path" == primer_building_ai_agents/README.md ]] && continue
      filtered_files+=("$path")
    done
    link_files=("${filtered_files[@]}")
  fi
  if (( ${#link_files[@]} == 0 )); then
    printf 'SUMMARY lychee mode=%s files=0 enforced=0 advisory=0\n' "$link_mode"
    return 0
  fi

  local flags=(--no-progress --mode plain --format detailed)
  [[ "$link_mode" == offline ]] && flags+=(--offline)
  output=$("$runtime" run --rm "${identity[@]}" -v "$repo_root:/repo$mount_suffix" \
    -w /repo "${LYCHEE_IMAGE:-docker.io/lycheeverse/lychee:0.23.0}" \
    "${flags[@]}" "${link_files[@]}" 2>&1) || lychee_status=$?
  if [[ "$link_mode" == online ]]; then
    printf '%s\n' "$output"
    printf 'SUMMARY lychee mode=online files=%s checker-status=%s (report only)\n' \
      "${#link_files[@]}" "$lychee_status"
    return 0
  fi

  local -A selected_paths=()
  for path in "${link_files[@]}"; do
    selected_paths["$path"]=1
  done
  while IFS= read -r line; do
    if [[ "$line" == 'Errors in '* ]]; then
      current_path=${line#Errors in }
      if [[ ! -v selected_paths["$current_path"] ]]; then
        printf 'link report error: unexpected file: %s\n' "$current_path" >&2
        return 2
      fi
    elif [[ "$line" == '[ERROR] '* ]]; then
      if [[ -z "$current_path" ]]; then
        printf 'link report error: finding without file: %s\n' "$line" >&2
        return 2
      fi
      if [[ -v enforced_paths["$current_path"] ]]; then
        printf 'ENFORCED %s: %s\n' "$current_path" "$line"
        (( enforced_count += 1 ))
      else
        printf 'ADVISORY %s: %s\n' "$current_path" "$line"
        (( advisory_count += 1 ))
      fi
      (( file_counts["$current_path"] += 1 ))
    elif [[ "$line" =~ Errors[.]+([0-9]+)$ ]]; then
      report_total=${BASH_REMATCH[1]}
      report_seen=1
    fi
  done <<< "$output"
  if (( lychee_status != 0 && lychee_status != 2 )); then
    printf 'lychee failed with status %s: %s\n' "$lychee_status" "$output" >&2
    return 2
  fi
  if (( report_seen == 0 || report_total != enforced_count + advisory_count )); then
    printf 'link report error: lychee reported %s errors, parsed %s\n' \
      "$report_total" "$(( enforced_count + advisory_count ))" >&2
    return 2
  fi
  for path in "${link_files[@]}"; do
    printf 'BASELINE %s: %s\n' "$path" "${file_counts[$path]:-0}"
  done
  printf 'SUMMARY lychee mode=offline files=%s enforced=%s advisory=%s\n' \
    "${#link_files[@]}" "$enforced_count" "$advisory_count"
  (( enforced_count == 0 ))
}

if [[ "$mode" == links || "$mode" == links-online ]]; then
  if [[ "$mode" == links ]]; then
    run_links offline "${files[@]}"
  else
    run_links online "${files[@]}"
  fi
  exit $?
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

links_status=0
if [[ "$mode" == all ]]; then
  run_links offline || links_status=$?
fi

if (( enforced_count || spell_status || prose_status || links_status )); then
  exit 1
fi
