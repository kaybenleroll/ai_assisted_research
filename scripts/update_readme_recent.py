#!/usr/bin/env python3
"""Generate README document tables from the registry and Justfile review dates."""

from __future__ import annotations

import argparse
import calendar
from dataclasses import dataclass
from datetime import date
import difflib
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
README = ROOT / "README.md"
CATEGORIES = (
    "AI Agents and Coding Tools", "Developer Tooling", "Quantitative Foundations",
    "Society and Institutions", "Silo RPG Materials",
)


@dataclass(frozen=True)
class Document:
    title: str
    category: str
    description: str
    html: str
    pdf: str | None
    justfile: str
    date_variable: str = "DATE"
    catalogue_title: str | None = None


# Edit README table rows here, then run `just readme` and `just readme-check`.
# Registry order is catalogue order. The recent block is sorted by review date.
DOCUMENTS = (
    Document("Building Autonomous AI Agents", CATEGORIES[0], "Comprehensive guide to designing and implementing agentic AI systems. Companion: [Agent Architecture Quick Reference](primer_building_ai_agents/primer_agent_quick_reference.html)", "primer_building_ai_agents/primer_ai_agents_comprehensive.html", "primer_building_ai_agents/primer_ai_agents_comprehensive.pdf", "primer_building_ai_agents/Justfile"),
    Document("Claude Code Alternatives", CATEGORIES[0], "Survey of AI coding agents, October 2026 refresh", "primer_claude_code_alternative/primer-claude-code-alternatives.html", "primer_claude_code_alternative/primer-claude-code-alternatives.pdf", "primer_claude_code_alternative/Justfile"),
    Document("Codex for Claude Code Users", CATEGORIES[0], "Practical guide to running Codex alongside Claude Code in one repository", "primer_codex_for_claude_code_users/primer-codex-for-claude-code-users.html", "primer_codex_for_claude_code_users/primer-codex-for-claude-code-users.pdf", "primer_codex_for_claude_code_users/Justfile"),
    Document("The Evaluation Loop", CATEGORIES[0], "Turning subjective AI task quality into numeric evals: verifiable rewards, RLHF/DSPy, and Goodhart failure modes", "primer_evaluation_loop/primer_evaluation_loop.html", "primer_evaluation_loop/primer_evaluation_loop.pdf", "primer_evaluation_loop/Justfile"),
    Document("Hermes Agent Server", CATEGORIES[0], "Guide to the Hermes Server framework", "primer_hermes_server/primer_hermes_server.html", "primer_hermes_server/primer_hermes_server.pdf", "primer_hermes_server/Justfile"),
    Document("OpenClaw", CATEGORIES[0], "Podman-first guide to the OpenClaw framework", "primer_openclaw/primer_openclaw.html", "primer_openclaw/primer_openclaw.pdf", "primer_openclaw/Justfile"),
    Document("Pi Coding Agent", CATEGORIES[0], "Practical primer on Pi’s architecture, local and hosted models, web research, extensions, and coding-agent comparisons", "primer_pi_coding_agent/primer_pi_coding_agent.html", "primer_pi_coding_agent/primer_pi_coding_agent.pdf", "primer_pi_coding_agent/Justfile"),
    Document("Running LLMs Locally", CATEGORIES[0], "Landscape of options for running language models on local hardware", "primer_research_local_llms/primer-running-llms-locally.html", "primer_research_local_llms/primer-running-llms-locally.pdf", "primer_research_local_llms/Justfile"),
    Document("Containerization", CATEGORIES[1], "Container fundamentals and the OCI spec, Docker's daemon architecture versus Podman's daemonless model, and how Kubernetes orchestrates it all", "primer_containerization/primer_containerization.html", "primer_containerization/primer_containerization.pdf", "primer_containerization/Justfile", catalogue_title="Containerization: Docker, Podman, and How Kubernetes Fits In"),
    Document("Oh My Zsh", CATEGORIES[1], "ZSH fundamentals, Oh My Zsh architecture, deep plugin coverage, themes, advanced features, and a personalised setup audit", "primer_ohmyzsh/primer_ohmyzsh.html", "primer_ohmyzsh/primer_ohmyzsh.pdf", "primer_ohmyzsh/Justfile", catalogue_title="Oh My Zsh: A Practical Guide"),
    Document("Python for Expert R Users", CATEGORIES[1], "Comprehensive migration guide for experienced tidyverse, purrr, and furrr users, with deep ggplot2 replacement strategy", "primer_python_for_r_users/primer_python_for_r_users.html", "primer_python_for_r_users/primer_python_for_r_users.pdf", "primer_python_for_r_users/Justfile"),
    Document("Catastrophe ELT Workbook", CATEGORIES[2], "*Quarto workbook, executable.* Catastrophe event-loss-table modelling — building and validating an ELT pipeline in R and Python. Companions: [Quickstart](workbook_catmodel_elt_documents/outputs/workbook_quickstart.html) · [Executable Index](workbook_catmodel_elt_documents/outputs/workbook_executable_index.html)", "workbook_catmodel_elt_documents/outputs/workbook_elt.html", None, "workbook_catmodel_elt_documents/Justfile"),
    Document("Deep Learning and Generative AI", CATEGORIES[2], "Neural networks, transformers, LLMs, and generative AI — architecture, training, and practical use", "primer_deep_learning/primer_deep_learning.html", "primer_deep_learning/primer_deep_learning.pdf", "primer_deep_learning/Justfile"),
    Document("Digital Signal Processing", CATEGORIES[2], "Sampling, Fourier analysis, filtering, spectral estimation, multirate systems, and practical DSP workflows", "primer_digital_signal_processing/primer_digital_signal_processing.html", "primer_digital_signal_processing/primer_digital_signal_processing.pdf", "primer_digital_signal_processing/Justfile"),
    Document("Complex Analysis", CATEGORIES[2], "Holomorphic functions, contour integration, residues, conformal maps, harmonic functions, applications, and computation", "primer_complex_analysis/primer_complex_analysis.html", "primer_complex_analysis/primer_complex_analysis.pdf", "primer_complex_analysis/Justfile"),
    Document("Numerical Analysis", CATEGORIES[2], "Floating-point arithmetic, linear algebra, root finding, ODEs, optimisation, eigenvalues, AD, and regularisation", "primer_numerical_analysis/primer_numerical_analysis.html", "primer_numerical_analysis/primer_numerical_analysis.pdf", "primer_numerical_analysis/Justfile"),
    Document("Comparative Religion", CATEGORIES[3], "Scripture, doctrine, community structure, liturgy, and internal diversity across Judaism, Christianity, Islam, Hinduism, Sikhism, Buddhism, and Shinto", "primer_comparative_religion/primer-comparative-religion.html", "primer_comparative_religion/primer-comparative-religion.pdf", "primer_comparative_religion/Justfile"),
    Document("European Electoral Systems", CATEGORIES[3], "Practical primer on electoral systems across European democracies", "primer_political_systems/primer-european-electoral-systems.html", "primer_political_systems/primer-european-electoral-systems.pdf", "primer_political_systems/Justfile"),
    Document("Military Organisation, Ranks, and Doctrine", CATEGORIES[3], "How armies are structured from fire team to army group, how ranks map to command levels, and naval/air force equivalents", "primer_military_structure/primer_military_structure.html", "primer_military_structure/primer_military_structure.pdf", "primer_military_structure/Justfile"),
    Document("Document Index", CATEGORIES[4], "Navigation map for all Silo RPG source documents", "gaming_silo_rpg/gaming_silo_index.html", "gaming_silo_rpg/gaming_silo_index.pdf", "gaming_silo_rpg/Justfile"),
    Document("Reference-Sheet Index", CATEGORIES[4], "GM routing map for the four compact Silo reference sheets", "gaming_silo_rpg/gaming_reference_silo_index.html", "gaming_silo_rpg/gaming_reference_silo_index.pdf", "gaming_silo_rpg/Justfile", "REF_INDEX_DATE"),
    Document("Player Reference Sheet", CATEGORIES[4], "Player-safe reminders for sectors, roles, everyday life, and party bonds", "gaming_silo_rpg/gaming_reference_silo_player.html", "gaming_silo_rpg/gaming_reference_silo_player.pdf", "gaming_silo_rpg/Justfile", "REF_PLAYER_DATE"),
    Document("GM Reference Sheet", CATEGORIES[4], "GM travel, security, pressure, faction, and daily-life tools", "gaming_silo_rpg/gaming_reference_silo_gm.html", "gaming_silo_rpg/gaming_reference_silo_gm.pdf", "gaming_silo_rpg/Justfile", "REF_GM_DATE"),
    Document("Campaign Reference Sheet", CATEGORIES[4], "Party bonds and quick kits for all ten starter campaigns", "gaming_silo_rpg/gaming_reference_silo_campaign.html", "gaming_silo_rpg/gaming_reference_silo_campaign.pdf", "gaming_silo_rpg/Justfile", "REF_CAMPAIGN_DATE"),
    Document("Comprehensive World Bible", CATEGORIES[4], "Full world reference — history, factions, technology, and geography", "gaming_silo_rpg/gaming_silo_comprehensive_bible.html", "gaming_silo_rpg/gaming_silo_comprehensive_bible.pdf", "gaming_silo_rpg/Justfile", "BIBLE_DATE"),
    Document("Game Master's Secrets", CATEGORIES[4], "GM-only lore, hidden mechanics, and macro-level world state", "gaming_silo_rpg/gaming_silo_gm_secrets.html", "gaming_silo_rpg/gaming_silo_gm_secrets.pdf", "gaming_silo_rpg/Justfile", "GM_DATE"),
    Document("Player's Survival Guide", CATEGORIES[4], "Player-facing rules, setting knowledge, and character options", "gaming_silo_rpg/gaming_silo_player_guide.html", "gaming_silo_rpg/gaming_silo_player_guide.pdf", "gaming_silo_rpg/Justfile", "PLAYER_DATE"),
    Document("Starter Campaigns", CATEGORIES[4], "Introductory campaign scenarios and player archetypes", "gaming_silo_rpg/gaming_silo_starter_campaign.html", "gaming_silo_rpg/gaming_silo_starter_campaign.pdf", "gaming_silo_rpg/Justfile", "CAMPAIGN_DATE"),
)


def checked_path(path: str) -> Path:
    resolved = ROOT / path
    if not resolved.is_file():
        raise ValueError(f"Registry path does not exist: {path}")
    return resolved


def review_date(document: Document) -> tuple[date, str]:
    justfile = checked_path(document.justfile)
    match = re.search(
        rf'^\s*{re.escape(document.date_variable)}\s*:=\s*"([^"]+)"\s*$',
        justfile.read_text(encoding="utf-8"), re.MULTILINE,
    )
    if not match:
        raise ValueError(f"Missing {document.date_variable} in {document.justfile}")
    value = match.group(1)
    parts = value.split()
    months = {name: index for index, name in enumerate(calendar.month_name) if name}
    try:
        if (len(parts) == 3 and parts[0].isdigit() and parts[1] in months
                and re.fullmatch(r"\d{4}", parts[2])):
            parsed = date(int(parts[2]), months[parts[1]], int(parts[0]))
            return parsed, parsed.isoformat()
        if len(parts) == 2 and parts[0] in months and re.fullmatch(r"\d{4}", parts[1]):
            parsed = date(int(parts[1]), months[parts[0]], 1)
            return parsed, parsed.strftime("%Y-%m")
    except ValueError:
        pass
    raise ValueError(f"Unparsable {document.date_variable} in {document.justfile}: {value!r}")


def link(document: Document, catalogue: bool = False) -> str:
    title = document.catalogue_title if catalogue and document.catalogue_title else document.title
    links = f"[{title}]({document.html})"
    if document.pdf:
        links += f" · [PDF]({document.pdf})"
    return links


def markers(name: str) -> tuple[str, str]:
    key = name.upper()
    return f"<!-- BEGIN {key} -->", f"<!-- END {key} -->"


def generate_recent(dates: dict[Document, tuple[date, str]]) -> str:
    begin, end = markers("RECENTLY UPDATED")
    ranked = sorted(DOCUMENTS, key=lambda doc: (-dates[doc][0].toordinal(), doc.title.casefold()))[:5]
    lines = [
        begin, "## Recently Updated", "",
        "These are the five most recently reviewed primary documents across the catalogue. Dates are each document's last-reviewed `DATE` from its Justfile.",
        "", "| Document | Category | Last reviewed |", "|----------|----------|---------------|",
    ]
    lines.extend(f"| {link(doc)} | {doc.category} | {dates[doc][1]} |" for doc in ranked)
    return "\n".join([*lines, "", end])


def generate_category(category: str, dates: dict[Document, tuple[date, str]]) -> str:
    begin, end = markers(category)
    lines = [begin, "<!-- Edit rows in scripts/update_readme_recent.py, then run just readme. -->",
             "| Document | Last reviewed | Description |", "|----------|---------------|-------------|"]
    lines.extend(
        f"| {link(doc, catalogue=True)} | {dates[doc][1]} | {doc.description} |"
        for doc in DOCUMENTS if doc.category == category
    )
    return "\n".join([*lines, end])


def replace_marked(text: str, name: str, replacement: str) -> str:
    begin, end = markers(name)
    if text.count(begin) != 1 or text.count(end) != 1:
        raise ValueError(f"Expected one pair of README markers for {name}")
    pattern = re.compile(re.escape(begin) + r".*?" + re.escape(end), re.DOTALL)
    return pattern.sub(lambda _match: replacement, text, count=1)


def generate(current: str) -> str:
    dates = {}
    for document in DOCUMENTS:
        checked_path(document.html)
        if document.pdf:
            checked_path(document.pdf)
        if document.category not in CATEGORIES:
            raise ValueError(f"Unknown category for {document.title}: {document.category}")
        dates[document] = review_date(document)

    updated = replace_marked(current, "RECENTLY UPDATED", generate_recent(dates))
    for category in CATEGORIES:
        replacement = generate_category(category, dates)
        begin, end = markers(category)
        if begin in updated or end in updated:
            updated = replace_marked(updated, category, replacement)
            # Restore the blank separator if an earlier generator omitted it.
            updated = updated.replace(end + "\n## ", end + "\n\n## ", 1)
            updated = updated.replace(end + "\n---", end + "\n\n---", 1)
            continue
        heading = rf"(?m)^(## {re.escape(category)}\n\n)(\| Document \|[^\n]*\n\|[-| ]+\n(?:\|[^\n]*\n?)+)"
        matches = list(re.finditer(heading, updated))
        if len(matches) != 1:
            raise ValueError(f"Expected one unmarked README table for {category}")
        match = matches[0]
        updated = updated[:match.start(2)] + replacement + "\n" + updated[match.end(2):]
    return updated


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="exit 1 and show a diff if README is out of date")
    args = parser.parse_args()
    try:
        current = README.read_text(encoding="utf-8")
        updated = generate(current)
    except (OSError, ValueError) as exc:
        print(f"README generation failed: {exc}", file=sys.stderr)
        return 2
    if current == updated:
        print("README is up to date")
        return 0
    if args.check:
        sys.stdout.writelines(difflib.unified_diff(
            current.splitlines(keepends=True), updated.splitlines(keepends=True),
            fromfile="README.md", tofile="generated README.md",
        ))
        return 1
    README.write_text(updated, encoding="utf-8")
    print("Updated README.md")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
