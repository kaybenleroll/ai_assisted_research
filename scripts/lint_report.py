"""Run typos in the lint container and classify findings by document."""

import json
from pathlib import Path
import subprocess
import sys


ROOT = Path.cwd()
MANIFEST = Path("lint/enforced-spelling.txt")


def in_scope(path: Path) -> bool:
    parts = path.parts
    if path == Path("README.md"):
        return True
    if len(parts) != 2 or path.suffix != ".md":
        return False
    if parts[0] == "gaming_silo_rpg":
        return True
    return parts[0].startswith("primer_") and path != Path(
        "primer_building_ai_agents/README.md"
    )


def clean_path(raw: str) -> Path:
    path = Path(raw)
    if path.is_absolute() or ".." in path.parts or not in_scope(path):
        raise ValueError(f"out-of-scope path: {raw}")
    if not path.is_file():
        raise ValueError(f"missing path: {raw}")
    return path


def main() -> int:
    try:
        enforced = set()
        for number, line in enumerate(MANIFEST.read_text().splitlines(), 1):
            value = line.strip()
            if not value or value.startswith("#"):
                continue
            path = clean_path(value)
            if path in enforced:
                raise ValueError(f"duplicate manifest path at line {number}: {value}")
            enforced.add(path)
        paths = [clean_path(raw) for raw in sys.argv[1:]]
    except (OSError, ValueError) as exc:
        print(f"lint configuration error: {exc}", file=sys.stderr)
        return 2

    findings = {path: 0 for path in paths}
    marker_count = sum(
        path.read_text(encoding="utf-8").count("<!-- typos: ignore-line -->")
        for path in paths
    )
    enforced_count = advisory_count = 0
    if paths:
        result = subprocess.run(
            ["typos", "--config", "_typos.toml", "--format", "json", "--sort", "--", *map(str, paths)],
            text=True,
            capture_output=True,
            check=False,
        )
        if result.returncode not in (0, 2):
            print(result.stderr or result.stdout, file=sys.stderr)
            return result.returncode
        for line in result.stdout.splitlines():
            try:
                item = json.loads(line)
                path = Path(item["path"])
                number = item["line_num"]
                typo = item["typo"]
            except (ValueError, KeyError, TypeError) as exc:
                print(f"invalid typos output: {exc}: {line}", file=sys.stderr)
                return 2
            if path not in findings:
                print(f"unexpected typos path: {path}", file=sys.stderr)
                return 2
            findings[path] += 1
            category = "ENFORCED" if path in enforced and path.parts[0] != "gaming_silo_rpg" else "ADVISORY"
            if category == "ENFORCED":
                enforced_count += 1
            else:
                advisory_count += 1
            suggestions = ", ".join(item.get("corrections") or [])
            print(f"{category} {path}:{number}: {typo} -> {suggestions}")
        if result.returncode == 2 and not result.stdout:
            print(result.stderr or "typos failed without findings", file=sys.stderr)
            return 2
    for path, count in findings.items():
        print(f"BASELINE {path}: {count}")
    print(
        f"SUMMARY files={len(paths)} enforced={enforced_count} "
        f"advisory={advisory_count} typos: ignore-line={marker_count}"
    )
    return 1 if enforced_count else 0


if __name__ == "__main__":
    sys.exit(main())
