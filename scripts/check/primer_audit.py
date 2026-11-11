#!/usr/bin/env python3
"""Validate and report revision-bound primer audit evidence.

This complements ``primer_evidence.py``: the existing checker validates the
audit schema, while this checker resolves source locators and Git revisions.
It does not judge whether a cited passage teaches the claimed material.
"""

from __future__ import annotations

import argparse
import hashlib
import re
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
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
    """Validate the two decisions in the single current checklist section."""
    sections: list[list[str]] = []
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
            current = None
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
    for name, allowed in (("Content gate", "pass|fail"), ("Release readiness", "ready|not-ready")):
        # Count malformed fields too, so a valid entry cannot hide a duplicate.
        candidates = [line for line in sections[0]
                      if re.match(rf"^\s*(?:(?:[-+*]|\d+[.)])\s+)?{re.escape(name)}\b", line, re.I)]
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
    return errors


def validate(root: Path, source: Path, brief: Path, audit: Path) -> list[str]:
    errors = []
    if not brief.is_file():
        errors.append(f"brief does not exist: {brief.relative_to(root)}")
    if not audit.is_file():
        errors.append(f"audit does not exist: {audit.relative_to(root)}")
    if errors:
        return errors
    errors.extend(locator_findings(root, audit))
    revision_errors, _, digest = revision_findings(root, source_path(root, source), brief, audit)
    errors.extend(revision_errors)
    audit_text = audit.read_text(encoding="utf-8")
    errors.extend(checklist_findings(audit_text))
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
