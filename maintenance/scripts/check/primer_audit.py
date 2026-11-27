#!/usr/bin/env python3
"""Validate and report revision-bound primer audit evidence.

This complements ``primer_evidence.py``: the existing checker validates the
audit schema, while this checker resolves source locators and Git revisions.
It does not judge whether a cited passage teaches the claimed material.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
# Historical snapshots fixed in policy; removing a registry entry is allowed.
LEGACY_BASELINE = {
    "primer_codex_for_claude_code_users/primer_codex_for_claude_code_users.audit.md":
        "a7e6ab742d9ce9b9a0c40cda5808317e9b8cc5b23570cba4b403a43436938ad9",
    "primer_knowledge_graph/primer_knowledge_graph.audit.md":
        "f1365a210f14ab06c8e688009dbb0b37fe586c4cf5eb5f662381faf997226fd6",
    "primer_pi_coding_agent/primer_pi_coding_agent.audit.md":
        "334eba0c311f2633530fc71f3bc5306e056007e5cc8db66110099d254a27983b",
}
REVISION_RE = re.compile(r"^[A-Za-z0-9._/-]+@[0-9a-f]{7,64}$|^[0-9a-f]{7,64}$")
METADATA_RE = re.compile(r"^\s*-\s*([^:]+):\s*(.*?)\s*$")
LOCATOR_RE = re.compile(
    r"(?<![A-Za-z0-9_/.-])(?P<path>[A-Za-z0-9_.-]+(?:/[A-Za-z0-9_.-]+)*\.(?:md|py|R|json|toml|txt|html|pdf)):(?P<line>[1-9][0-9]*)"
)
HUNK_RE = re.compile(r"^@@ -\d+(?:,\d+)? \+(?P<start>\d+)(?:,(?P<count>\d+))? @@")


def metadata(text: str) -> dict[str, str]:
    found = {}
    for line in text.splitlines():
        match = METADATA_RE.match(line)
        if match:
            found[match.group(1).strip()] = match.group(2).strip().strip("`")
    return found


def git(root: Path, *args: str, check: bool = True) -> str:
    result = subprocess.run(["git", *args], cwd=root, text=True, capture_output=True)
    if check and result.returncode:
        raise RuntimeError(result.stderr.strip() or f"git {' '.join(args)} failed")
    return result.stdout.strip()


def resolve_revision(root: Path, revision: str) -> str:
    if not REVISION_RE.fullmatch(revision):
        raise ValueError(f"invalid commit-like revision: {revision}")
    return git(root, "rev-parse", "--verify", f"{revision}^{{commit}}")


def source_hash(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def source_path(root: Path, source: Path) -> Path:
    path = source if source.is_absolute() else root / source
    path = path.resolve()
    try:
        path.relative_to(root.resolve())
    except ValueError as exc:
        raise ValueError(f"source is outside repository: {source}") from exc
    if not path.is_file():
        raise ValueError(f"source does not exist: {path.relative_to(root)}")
    return path


def structured_locator_text(audit_text: str) -> list[tuple[int, str]]:
    lines = audit_text.splitlines()
    start = next((i for i, line in enumerate(lines) if line.strip() == "## Adversarial depth gate"), None)
    if start is None:
        return []
    selected = []
    for number, line in enumerate(lines[start + 1:], start + 2):
        if line.startswith("## "):
            break
        selected.append((number, line))
    return selected


def locator_findings(root: Path, audit: Path) -> list[str]:
    errors = []
    for number, text in structured_locator_text(audit.read_text(encoding="utf-8")):
        for match in LOCATOR_RE.finditer(text):
            relative = Path(match.group("path"))
            target = root / relative
            line = int(match.group("line"))
            if not target.is_file():
                errors.append(f"audit:{number}: locator file does not exist: {relative}")
                continue
            with target.open(encoding="utf-8") as handle:
                line_count = sum(1 for _ in handle)
            if line > line_count:
                errors.append(f"audit:{number}: locator line {line} exceeds {relative} ({line_count} lines)")
    return errors


def case_findings(root: Path, source: Path, case: Path) -> list[str]:
    """Validate an explicitly bound case; unbound legacy cases are unchanged."""
    if not case.is_file():
        return []
    text = case.read_text(encoding="utf-8")
    fields = {}
    for name in ("Current source revision", "Current source SHA-256"):
        fields[name] = [m.group(1).strip().strip("`") for m in re.finditer(
            rf"^- {re.escape(name)}:\s*(.*?)\s*$", text, re.M)]
    start, end = "<!-- current locators: start -->", "<!-- current locators: end -->"
    if not any(fields.values()) and start not in text and end not in text:
        return []
    errors = []
    if any(len(values) != 1 for values in fields.values()):
        errors.append("case: exactly one current source revision and SHA-256 are required")
    else:
        revision, digest = fields["Current source revision"][0], fields["Current source SHA-256"][0]
        if not re.fullmatch(r"[0-9a-f]{64}", digest) or digest != source_hash(source):
            errors.append("case: current source SHA-256 is invalid or differs from working source")
        try:
            resolved = resolve_revision(root, revision)
            relative = source.relative_to(root).as_posix()
            result = subprocess.run(["git", "show", f"{resolved}:{relative}"], cwd=root, capture_output=True)
            if result.returncode or result.stdout != source.read_bytes():
                errors.append("case: source is absent at current revision or differs from working source")
        except (RuntimeError, ValueError) as exc:
            errors.append(f"case: current revision: {exc}")
    active = False
    regions = 0
    locators = 0
    range_re = re.compile(r"(?<![A-Za-z0-9_/.-])(?P<path>[A-Za-z0-9_.-]+(?:/[A-Za-z0-9_.-]+)*\.(?:md|py|R|json|toml|txt|html|pdf)):(?P<line>[0-9]+)(?:[-–](?P<end>[0-9]+))?")
    for number, line in enumerate(text.splitlines(), 1):
        if line.strip() == start:
            if active:
                errors.append(f"case:{number}: nested current locator marker")
            active = True
            regions += 1
        elif line.strip() == end:
            if not active:
                errors.append(f"case:{number}: unmatched current locator end")
            active = False
        elif active:
            for match in range_re.finditer(line):
                locators += 1
                relative = Path(match.group("path"))
                target = (root / relative).resolve()
                try:
                    target.relative_to(root.resolve())
                    if not target.is_file():
                        raise ValueError("file does not exist")
                    count = len(target.read_text(encoding="utf-8").splitlines())
                    first = int(match.group("line"))
                    last = int(match.group("end") or first)
                    if first < 1 or last < first or last > count:
                        raise ValueError(f"line range is outside file ({count} lines)")
                except (ValueError, OSError, UnicodeError) as exc:
                    errors.append(f"case:{number}: invalid current locator {match.group(0)}: {exc}")
    if active:
        errors.append("case: unclosed current locator marker")
    if not regions or not locators:
        errors.append("case: bound case requires marked current locators")
    return errors


def revision_findings(root: Path, source: Path, brief: Path, audit: Path) -> tuple[list[str], str, str]:
    errors = []
    brief_meta = metadata(brief.read_text(encoding="utf-8"))
    audit_meta = metadata(audit.read_text(encoding="utf-8"))
    source_revision = audit_meta.get("Source revision", "")
    reviewed_revision = audit_meta.get("Reviewed revision", "")
    brief_revision = brief_meta.get("Source revision", "")
    if not source_revision or not reviewed_revision:
        return ["audit: Source revision and Reviewed revision are required"], "", ""
    try:
        resolved_source = resolve_revision(root, source_revision)
        resolved_reviewed = resolve_revision(root, reviewed_revision)
    except (RuntimeError, ValueError) as exc:
        return [f"revision: {exc}"], "", ""
    if resolved_source != resolved_reviewed:
        errors.append("audit: Source revision and Reviewed revision resolve to different commits")
    if brief_revision and REVISION_RE.fullmatch(brief_revision):
        try:
            if resolve_revision(root, brief_revision) != resolved_source:
                errors.append("brief and audit: Source revision resolves to different commits")
        except (RuntimeError, ValueError) as exc:
            errors.append(f"brief: {exc}")
    relative = source.relative_to(root).as_posix()
    committed_result = subprocess.run(
        ["git", "show", f"{resolved_source}:{relative}"], cwd=root, capture_output=True
    )
    committed = committed_result.stdout
    if committed_result.returncode:
        errors.append(f"revision: source is absent at {source_revision}: {relative}")
    elif committed != source.read_bytes():
        errors.append(f"revision: working source differs from reviewed commit {source_revision}: {relative}")
    return errors, resolved_source, source_hash(source)


def changed_ranges(root: Path, revision: str, source: Path) -> list[tuple[int, int]]:
    relative = source.relative_to(root).as_posix()
    diff = git(root, "diff", "--unified=0", revision, "--", relative)
    ranges = []
    for line in diff.splitlines():
        match = HUNK_RE.match(line)
        if not match:
            continue
        start = int(match.group("start"))
        count = int(match.group("count") or "1")
        ranges.append((start, max(start, start + count - 1)))
    return ranges


def impacted_locators(root: Path, audit: Path, ranges: list[tuple[int, int]]) -> list[str]:
    impacts = []
    source_rel = None
    for line_number, text in enumerate(audit.read_text(encoding="utf-8").splitlines(), 1):
        for match in LOCATOR_RE.finditer(text):
            line = int(match.group("line"))
            if any(start <= line <= end for start, end in ranges):
                impacts.append(f"audit:{line_number}: {match.group('path')}:{line}")
    return impacts


def project_paths(root: Path, project: str) -> tuple[Path, Path, Path]:
    directory = (root / project).resolve()
    if not directory.is_dir():
        raise ValueError(f"project directory does not exist: {project}")
    justfile = directory / "Justfile"
    match = re.search(r'^SOURCE_MD\s*:=\s*"([^"]+)"', justfile.read_text(encoding="utf-8"), re.M)
    if not match:
        raise ValueError(f"{justfile.relative_to(root)}: SOURCE_MD is missing")
    source = directory / match.group(1)
    brief = directory / f"{directory.name}.brief.md"
    audit = directory / f"{directory.name}.audit.md"
    return source, brief, audit


def checklist_findings(text: str) -> list[str]:
    """Validate decisions in the single current checklist section."""
    sections: list[list[str]] = []
    outlines: list[list[str]] = []
    current: list[str] | None = None
    fence: tuple[str, int] | None = None
    for line in text.splitlines():
        marker = re.match(r"^ {0,3}(`{3,}|~{3,})", line)
        if marker:
            token = marker.group(1)
            if fence is None:
                if current is not None:
                    current.append("")  # A fence interrupts a Markdown table.
                fence = (token[0], len(token))
            elif token[0] == fence[0] and len(token) >= fence[1] and not line[marker.end():].strip():
                fence = None
            continue
        if fence is not None:
            continue
        heading = re.match(r"^ {0,3}(#{1,6})[ \t]+(.*?)[ \t]*#*[ \t]*$", line)
        if heading:
            current = None
            if heading.group(1) == "##" and heading.group(2) == "Outline and hierarchy review":
                current = []
                outlines.append(current)
            if heading.group(1) == "##" and heading.group(2) == "Release readiness checklist":
                current = []
                sections.append(current)
            continue
        if current is not None:
            current.append(line)

    if len(sections) != 1:
        return [f"audit: expected exactly one current 'Release readiness checklist' section; found {len(sections)}"]

    errors = []
    decisions = {}
    for name, allowed, required in (("Content gate", "pass|fail", True),
                                    ("Structural gate", "pass|fail|not-checked", bool(outlines)),
                                    ("Release readiness", "ready|not-ready", True)):
        # Count malformed fields too, so a valid entry cannot hide a duplicate.
        candidates = [line for line in sections[0]
                      if re.match(rf"^\s*(?:(?:[-+*]|\d+[.)])\s+)?{re.escape(name)}\b", line, re.I)]
        if not candidates and not required:
            continue
        if len(candidates) != 1:
            errors.append(f"audit: checklist must contain exactly one {name} entry; found {len(candidates)}")
            continue
        match = re.fullmatch(
            rf"- {re.escape(name)}:\s+\*\*({allowed})\*\*(?:[,. ;:]\s*\S.*|\s+\S.*)?\s*",
            candidates[0],
        )
        if not match:
            errors.append(f"audit: malformed {name} entry in checklist")
        else:
            decisions[name] = match.group(1)
    if decisions.get("Content gate") == "fail" and decisions.get("Release readiness") == "ready":
        errors.append("audit: Release readiness cannot be ready when Content gate is fail")
    if decisions.get("Structural gate") in ("fail", "not-checked") and decisions.get("Release readiness") == "ready":
        errors.append("audit: Release readiness cannot be ready when Structural gate is fail or not-checked")
    if decisions.get("Structural gate") == "pass":
        if len(outlines) != 1:
            errors.append(f"audit: Structural gate pass requires exactly one Outline and hierarchy review; found {len(outlines)}")
        else:
            outline = outlines[0]
            rendered = [line for line in outline if re.match(
                r"^\s*(?:(?:[-+*]|\d+[.)])\s+)?Rendered contents\b", line, re.I)]
            if len(rendered) != 1 or not re.fullmatch(
                r"- Rendered contents:\s+\*\*checked\*\*(?:[,. ;:]\s*\S.*|\s+\S.*)?\s*", rendered[0]
            ):
                errors.append("audit: Structural gate pass requires exactly one Rendered contents: **checked** entry")
            header = ("Actual section and hierarchy at reviewed revision", "Purpose and parent/child relationship",
                      "Adjacent sibling boundary and rationale", "Finding and disposition")
            def cells(line: str) -> list[str]:
                line = line.strip()
                if not (line.startswith("|") and line.endswith("|")):
                    return []
                return [cell.strip() for cell in re.split(r"(?<!\\)\|", line[1:-1])]
            def evidence(cell: str) -> bool:
                return bool(cell and not re.fullmatch(r"(?i)(?:[-–—]+|n/?a|tbd|todo|pending|not[- ]checked|<[^>]*>|\[[^]]*\])", cell))
            found = False
            incomplete = False
            for index, line in enumerate(outline[:-2]):
                if tuple(cells(line)) != header:
                    continue
                separator = cells(outline[index + 1])
                if len(separator) != 4 or not all(re.fullmatch(r":?-{3,}:?", cell) for cell in separator):
                    continue
                for row in outline[index + 2:]:
                    values = cells(row)
                    if not values:
                        if row.strip().startswith("|"):
                            incomplete = True
                        break
                    if len(values) != 4 or not all(evidence(value) for value in values):
                        incomplete = True
                    else:
                        found = True
            if not found or incomplete:
                errors.append("audit: Structural gate pass requires complete outline evidence table rows")
    return errors


def coverage_findings(text: str, source_bytes: bytes, *, legacy: bool = False) -> list[str]:
    """Check required self-reported inclusive line ranges in the current outline.

    The ranges record a claim; they cannot establish that anyone read the source.
    Revision validation separately binds these bytes to the reviewed commit.
    """
    outline: list[str] = []
    checklist: list[str] = []
    metadata_lines: list[str] = []
    all_coverage: list[str] = []
    all_schemas: list[str] = []
    in_metadata = True
    current: list[str] | None = None
    fence: tuple[str, int] | None = None
    for line in text.splitlines():
        marker = re.match(r"^ {0,3}(`{3,}|~{3,})", line)
        if marker:
            token = marker.group(1)
            if fence is None:
                fence = (token[0], len(token))
            elif token[0] == fence[0] and len(token) >= fence[1] and not line[marker.end():].strip():
                fence = None
            continue
        if fence is not None:
            continue
        heading = re.match(r"^ {0,3}(#{1,6})[ \t]+(.*?)[ \t]*#*[ \t]*$", line)
        if heading:
            # A document title may precede its metadata.
            if heading.group(1) != "#":
                in_metadata = False
            current = None
            if heading.group(1) == "##" and heading.group(2) == "Outline and hierarchy review":
                current = outline
            elif heading.group(1) == "##" and heading.group(2) == "Release readiness checklist":
                current = checklist
            continue
        if in_metadata:
            metadata_lines.append(line)
        if re.match(r"^\s*(?:(?:[-+*]|\d+[.)])\s+)?Audit schema\b", line, re.I):
            all_schemas.append(line)
        if re.match(r"^\s*(?:(?:[-+*]|\d+[.)])\s+)?Source read coverage\b", line, re.I):
            all_coverage.append(line)
        if current is not None:
            current.append(line)

    schemas = [line for line in metadata_lines if re.match(
        r"^\s*(?:(?:[-+*]|\d+[.)])\s+)?Audit schema\b", line, re.I)]
    if all_schemas and (len(all_schemas) != 1 or len(schemas) != 1
                        or not re.fullmatch(r"- Audit schema: 2\s*", schemas[0])):
        return ["audit: expected one supported Audit schema entry: - Audit schema: 2"]
    entries = [line for line in outline if re.match(
        r"^\s*(?:(?:[-+*]|\d+[.)])\s+)?Source read coverage\b", line, re.I)]
    if schemas and (len(entries) != 1 or len(all_coverage) != 1):
        return ["audit: Audit schema 2 requires exactly one Source read coverage entry in the current outline review"]
    if not schemas and not legacy:
        return ["audit: Audit schema 2 is required for unregistered or changed audits"]
    if not entries:
        return []  # Only an exact registered historical record is exempt.
    if len(entries) != 1:
        return ["audit: expected exactly one Source read coverage entry in outline review"]
    match = re.fullmatch(r"- Source read coverage: (none|[0-9]+-[0-9]+(?:,\s*[0-9]+-[0-9]+)*)\s*", entries[0])
    if not match:
        return ["audit: malformed Source read coverage; use none or inclusive ranges such as 1-20, 21-40"]
    gate = [re.fullmatch(r"- Structural gate:\s+\*\*(pass|fail|not-checked)\*\*(?:[,. ;:]\s*\S.*|\s+\S.*)?\s*", line)
            for line in checklist if re.match(r"^\s*(?:(?:[-+*]|\d+[.)])\s+)?Structural gate\b", line, re.I)]
    if len(gate) != 1 or gate[0] is None:
        return ["audit: Source read coverage requires one valid Structural gate entry"]
    line_count = source_bytes.count(b"\n") + bool(source_bytes and not source_bytes.endswith(b"\n"))
    ranges = [] if match.group(1) == "none" else [tuple(map(int, item.split("-"))) for item in match.group(1).split(",")]
    errors = []
    previous = 0
    complete = True
    for start, end in sorted(ranges):
        if start < 1 or end < start or end > line_count:
            errors.append(f"audit: Source read coverage range {start}-{end} is invalid for {line_count} source lines")
            continue
        if start <= previous:
            errors.append(f"audit: Source read coverage range {start}-{end} overlaps a previous range")
        if start > previous + 1:
            complete = False
        previous = max(previous, end)
    complete = complete and previous == line_count
    if gate[0].group(1) == "pass" and line_count == 0:
        errors.append("audit: Structural gate pass requires a nonempty source")
    if gate[0].group(1) == "pass" and not complete:
        errors.append(f"audit: Structural gate pass requires complete Source read coverage of lines 1-{line_count}")
    return errors


def legacy_audit_registry(root: Path) -> dict[str, str]:
    """Load the reviewed snapshot exemptions; malformed or absent registries fail closed."""
    registry = root / "maintenance/docs/primer-audit-legacy.json"
    try:
        data = json.loads(registry.read_text(encoding="utf-8"), object_pairs_hook=_unique_object)
    except (OSError, ValueError) as exc:
        raise ValueError(f"invalid legacy audit registry {registry}: {exc}") from exc
    if not isinstance(data, dict) or set(data) != {"version", "legacy"} or type(data["version"]) is not int or data["version"] != 1 or not isinstance(data["legacy"], list):
        raise ValueError("invalid legacy audit registry: expected version 1 and legacy list")
    entries = {}
    for item in data["legacy"]:
        if not isinstance(item, dict) or set(item) != {"path", "sha256"}:
            raise ValueError("invalid legacy audit registry entry")
        path, digest = item["path"], item["sha256"]
        if (not isinstance(path, str) or not re.fullmatch(r"[A-Za-z0-9_.-]+(?:/[A-Za-z0-9_.-]+)*\.md", path)
                or any(part in (".", "..") for part in path.split("/"))
                or not isinstance(digest, str) or not re.fullmatch(r"[0-9a-f]{64}", digest)):
            raise ValueError("invalid legacy audit registry path or SHA-256")
        if path in entries:
            raise ValueError(f"duplicate legacy audit registry path: {path}")
        if LEGACY_BASELINE.get(path) != digest:
            raise ValueError(f"legacy audit registry entry is not in the fixed historical baseline: {path}")
        entries[path] = digest
    return entries


def _unique_object(pairs: list[tuple[str, object]]) -> dict[str, object]:
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError(f"duplicate registry field: {key}")
        result[key] = value
    return result


def validate(root: Path, source: Path, brief: Path, audit: Path) -> list[str]:
    errors = []
    registry = legacy_audit_registry(root)
    try:
        relative_audit = audit.resolve().relative_to(root.resolve()).as_posix()
    except ValueError as exc:
        raise ValueError("audit is outside repository") from exc
    if not brief.is_file():
        errors.append(f"brief does not exist: {brief.relative_to(root)}")
    if not audit.is_file():
        errors.append(f"audit does not exist: {audit.relative_to(root)}")
    if errors:
        return errors
    errors.extend(locator_findings(root, audit))
    errors.extend(case_findings(root, source_path(root, source), source.with_suffix(".case.md")))
    revision_errors, reviewed_source, digest = revision_findings(root, source_path(root, source), brief, audit)
    errors.extend(revision_errors)
    audit_text = audit.read_text(encoding="utf-8")
    errors.extend(checklist_findings(audit_text))
    if reviewed_source:
        committed = subprocess.run(
            ["git", "show", f"{reviewed_source}:{source.relative_to(root).as_posix()}"],
            cwd=root, capture_output=True,
        )
        if committed.returncode == 0:
            errors.extend(coverage_findings(audit_text, committed.stdout, legacy=(
                registry.get(relative_audit) == hashlib.sha256(audit.read_bytes()).hexdigest()
            )))
    print(f"source: {source.relative_to(root)}")
    print(f"source sha256: {digest}")
    return errors


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-root", type=Path, default=ROOT)
    parser.add_argument("--project", type=str)
    parser.add_argument("--source", type=Path)
    parser.add_argument("--brief", type=Path)
    parser.add_argument("--audit", type=Path)
    parser.add_argument("--impact-from", type=str, help="report audit locators in source lines changed since this revision")
    args = parser.parse_args(argv)
    root = args.repo_root.resolve()
    try:
        if args.project:
            source, brief, audit = project_paths(root, args.project)
        elif args.source and args.brief and args.audit:
            source, brief, audit = args.source, args.brief, args.audit
        else:
            parser.error("provide --project or all of --source, --brief, and --audit")
        source = source_path(root, source)
        brief = (brief if brief.is_absolute() else root / brief).resolve()
        audit = (audit if audit.is_absolute() else root / audit).resolve()
        errors = validate(root, source, brief, audit)
        if args.impact_from:
            ranges = changed_ranges(root, args.impact_from, source)
            print(f"changed source ranges since {args.impact_from}: {ranges or 'none'}")
            impacts = impacted_locators(root, audit, ranges)
            print("affected audit locators:")
            print("\n".join(f"- {item}" for item in impacts) if impacts else "- none")
    except (OSError, RuntimeError, ValueError) as exc:
        errors = [str(exc)]
    if errors:
        print("primer audit check failed:", file=sys.stderr)
        print("\n".join(f"- {error}" for error in errors), file=sys.stderr)
        return 1
    print("primer audit check passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
