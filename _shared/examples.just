# Shared executable-example entry point. Callers supply the repository root
# and primer directory so this also works from imported per-primer Justfiles.
run-examples repo primer *ids:
  python3 -I "{{repo}}/_shared/examples/run.py" --repo-root "{{repo}}" "{{primer}}" {{ids}}
