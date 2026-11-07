#!/usr/bin/env python3
"""Check the repository's small, harness-neutral instruction contract."""

from __future__ import annotations

import argparse
import os
import re
import sys
from pathlib import Path

REQUIRED_H2 = [
    "Purpose and Scope",
    "Task Routing",
    "Repository Invariants",
    "Document Classes",
    "Collaboration and Handoffs",
    "Issues and Pull Requests",
    "Silo Context Navigation Mandate",
    "Definition of Done",
    "Adapters and Limits",
]
ADAPTERS = {"AGENTS.md"}
SKILLS = ("primer-plan", "primer-audit", "primer-render-qa", "primer-handoff")


def headings(text: str) -> list[str]:
    result = []
    fenced = False
    for line in text.splitlines():
        if line.startswith("```"):
            fenced = not fenced
        elif not fenced:
            match = re.match(r"^## (.+?)\s*#*$", line)
            if match:
                result.append(match.group(1).strip())
    return result


def check(root: Path) -> list[str]:
    errors: list[str] = []
    contract = root / "docs/project-contract.md"
    if not contract.is_file():
        return ["missing docs/project-contract.md"]
    try:
        contract_text = contract.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        return ["docs/project-contract.md is not UTF-8"]
    actual = headings(contract_text)
    if actual != REQUIRED_H2:
        errors.append(f"contract H2 sequence is {actual!r}, expected {REQUIRED_H2!r}")
    root_claude = root / "CLAUDE.md"
    if root_claude.exists() or root_claude.is_symlink():
        errors.append("root CLAUDE.md must not exist; AGENTS.md is canonical")
    for name in ADAPTERS:
        path = root / name
        if not path.is_file():
            errors.append(f"missing {name}")
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            errors.append(f"{name} is not UTF-8")
            continue
        links = re.findall(r"\[[^]]+\]\(([^)]+)\)", text)
        targets = [link for link in links if link == "docs/project-contract.md"]
        if len(targets) != 1:
            errors.append(f"{name} must contain exactly one link to docs/project-contract.md")
        if "Read" not in text or "project contract" not in text:
            errors.append(f"{name} must explicitly instruct the reader to read the project contract")
    if re.search(r"\]\((?:\.\./)*AGENTS\.md\)|\]\((?:\.\./)*CLAUDE\.md\)", contract_text):
        errors.append("project contract must not link to an adapter")
    claude_skills = root / ".claude/skills"
    if claude_skills.is_symlink() or not claude_skills.is_dir():
        errors.append(".claude/skills must be a real directory")
    for skill in SKILLS:
        adapter = claude_skills / skill
        expected = f"../../.agents/skills/{skill}"
        if not adapter.is_symlink():
            errors.append(f"Claude skill adapter {skill} must be a symlink to {expected}")
        elif os.readlink(adapter) != expected:
            errors.append(f"Claude skill adapter {skill} must point exactly to {expected}")
        elif not adapter.is_dir() or not (adapter / "SKILL.md").is_file():
            errors.append(f"Claude skill adapter {skill} is dangling or missing SKILL.md")
    local_paths = [
        "../CONTRIBUTING.md", "../STYLE_GUIDE.md", "math-notation.md",
        "review-checklist.md", "agent-collaboration.md",
        "../workbook_catmodel_elt_documents/README.md",
        "../gaming_silo_rpg/gaming_silo_index.md",
    ]
    for target in local_paths:
        if not (contract.parent / target).is_file():
            errors.append(f"contract link target is missing: {target}")
    router = root / "docs/primer-workflow-skills.md"
    if not router.is_file():
        errors.append("missing docs/primer-workflow-skills.md")
    else:
        try:
            router_text = router.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            errors.append("docs/primer-workflow-skills.md is not UTF-8")
        else:
            links = re.findall(r"\[`([^`]+)`\]\(([^)]+)\)", router_text)
            for skill in SKILLS:
                target = f"../.agents/skills/{skill}/SKILL.md"
                actual_targets = [link for name, link in links if name == skill]
                if actual_targets != [target]:
                    errors.append(f"skill {skill} must link exactly once to {target}; found {actual_targets!r}")
                if not (router.parent / target).is_file():
                    errors.append(f"skill link target is missing: {target}")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args()
    errors = check(args.root.resolve())
    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1
    print("agent contract: OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
