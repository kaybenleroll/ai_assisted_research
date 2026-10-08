#!/usr/bin/env python3
"""Refresh the README's cross-category recently-updated document list."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
import re
import subprocess


ROOT = Path(__file__).resolve().parents[1]
README = ROOT / "README.md"
BEGIN = "<!-- BEGIN RECENTLY UPDATED -->"
END = "<!-- END RECENTLY UPDATED -->"


@dataclass(frozen=True)
class Document:
    title: str
    category: str
    html: str
    pdf: str | None
    source: str


DOCUMENTS = (
    Document("Building Autonomous AI Agents", "AI Agents and Coding Tools", "primer_building_ai_agents/primer_ai_agents_comprehensive.html", "primer_building_ai_agents/primer_ai_agents_comprehensive.pdf", "primer_building_ai_agents/primer_ai_agents_comprehensive.md"),
    Document("Claude Code Alternatives", "AI Agents and Coding Tools", "primer_claude_code_alternative/primer-claude-code-alternatives.html", "primer_claude_code_alternative/primer-claude-code-alternatives.pdf", "primer_claude_code_alternative/primer-claude-code-alternatives.md"),
    Document("Codex for Claude Code Users", "AI Agents and Coding Tools", "primer_codex_for_claude_code_users/primer-codex-for-claude-code-users.html", "primer_codex_for_claude_code_users/primer-codex-for-claude-code-users.pdf", "primer_codex_for_claude_code_users/primer-codex-for-claude-code-users.md"),
    Document("The Evaluation Loop", "AI Agents and Coding Tools", "primer_evaluation_loop/primer_evaluation_loop.html", "primer_evaluation_loop/primer_evaluation_loop.pdf", "primer_evaluation_loop/primer_evaluation_loop.md"),
    Document("Hermes Agent Server", "AI Agents and Coding Tools", "primer_hermes_server/primer_hermes_server.html", "primer_hermes_server/primer_hermes_server.pdf", "primer_hermes_server/primer_hermes_server.md"),
    Document("OpenClaw", "AI Agents and Coding Tools", "primer_openclaw/primer_openclaw.html", "primer_openclaw/primer_openclaw.pdf", "primer_openclaw/primer_openclaw.md"),
    Document("Pi Coding Agent", "AI Agents and Coding Tools", "primer_pi_coding_agent/primer_pi_coding_agent.html", "primer_pi_coding_agent/primer_pi_coding_agent.pdf", "primer_pi_coding_agent/primer_pi_coding_agent.md"),
    Document("Running LLMs Locally", "AI Agents and Coding Tools", "primer_research_local_llms/primer-running-llms-locally.html", "primer_research_local_llms/primer-running-llms-locally.pdf", "primer_research_local_llms/primer-running-llms-locally.md"),
    Document("Containerization", "Developer Tooling", "primer_containerization/primer_containerization.html", "primer_containerization/primer_containerization.pdf", "primer_containerization/primer_containerization.md"),
    Document("Oh My Zsh", "Developer Tooling", "primer_ohmyzsh/primer_ohmyzsh.html", "primer_ohmyzsh/primer_ohmyzsh.pdf", "primer_ohmyzsh/primer_ohmyzsh.md"),
    Document("Python for Expert R Users", "Developer Tooling", "primer_python_for_r_users/primer_python_for_r_users.html", "primer_python_for_r_users/primer_python_for_r_users.pdf", "primer_python_for_r_users/primer_python_for_r_users.md"),
    Document("Catastrophe ELT Workbook", "Quantitative Foundations", "workbook_catmodel_elt_documents/outputs/workbook_elt.html", None, "workbook_catmodel_elt_documents/workbook_elt.qmd"),
    Document("Deep Learning and Generative AI", "Quantitative Foundations", "primer_deep_learning/primer_deep_learning.html", "primer_deep_learning/primer_deep_learning.pdf", "primer_deep_learning/primer_deep_learning.md"),
    Document("Digital Signal Processing", "Quantitative Foundations", "primer_digital_signal_processing/primer_digital_signal_processing.html", "primer_digital_signal_processing/primer_digital_signal_processing.pdf", "primer_digital_signal_processing/primer_digital_signal_processing.md"),
    Document("Information Theory Series", "Quantitative Foundations", "article_info_theory/information_theory_series_combined.html", "article_info_theory/information_theory_series_combined.pdf", "article_info_theory/information_theory_series_combined.md"),
    Document("Complex Analysis", "Quantitative Foundations", "primer_complex_analysis/primer_complex_analysis.html", "primer_complex_analysis/primer_complex_analysis.pdf", "primer_complex_analysis/primer_complex_analysis.md"),
    Document("Numerical Analysis", "Quantitative Foundations", "primer_numerical_analysis/primer_numerical_analysis.html", "primer_numerical_analysis/primer_numerical_analysis.pdf", "primer_numerical_analysis/primer_numerical_analysis.md"),
    Document("Comparative Religion", "Society and Institutions", "primer_comparative_religion/primer-comparative-religion.html", "primer_comparative_religion/primer-comparative-religion.pdf", "primer_comparative_religion/primer-comparative-religion.md"),
    Document("European Electoral Systems", "Society and Institutions", "primer_political_systems/primer-european-electoral-systems.html", "primer_political_systems/primer-european-electoral-systems.pdf", "primer_political_systems/primer-european-electoral-systems.md"),
    Document("Military Organisation, Ranks, and Doctrine", "Society and Institutions", "primer_military_structure/primer_military_structure.html", "primer_military_structure/primer_military_structure.pdf", "primer_military_structure/primer_military_structure.md"),
    Document("Document Index", "Silo RPG Materials", "gaming_silo_rpg/gaming_silo_index.html", "gaming_silo_rpg/gaming_silo_index.pdf", "gaming_silo_rpg/gaming_silo_index.md"),
    Document("Comprehensive World Bible", "Silo RPG Materials", "gaming_silo_rpg/gaming_silo_comprehensive_bible.html", "gaming_silo_rpg/gaming_silo_comprehensive_bible.pdf", "gaming_silo_rpg/gaming_silo_comprehensive_bible.md"),
    Document("Game Master's Secrets", "Silo RPG Materials", "gaming_silo_rpg/gaming_silo_gm_secrets.html", "gaming_silo_rpg/gaming_silo_gm_secrets.pdf", "gaming_silo_rpg/gaming_silo_gm_secrets.md"),
    Document("Player's Survival Guide", "Silo RPG Materials", "gaming_silo_rpg/gaming_silo_player_guide.html", "gaming_silo_rpg/gaming_silo_player_guide.pdf", "gaming_silo_rpg/gaming_silo_player_guide.md"),
    Document("Starter Campaigns", "Silo RPG Materials", "gaming_silo_rpg/gaming_silo_starter_campaign.html", "gaming_silo_rpg/gaming_silo_starter_campaign.pdf", "gaming_silo_rpg/gaming_silo_starter_campaign.md"),
)


def last_commit(document: Document) -> tuple[datetime, str]:
    result = subprocess.run(
        ["git", "-C", str(ROOT), "log", "-1", "--format=%aI%x09%H", "--", document.source],
        check=True,
        capture_output=True,
        text=True,
    )
    value = result.stdout.strip()
    if not value:
        raise RuntimeError(f"No Git history found for {document.source}")
    timestamp, commit = value.split("\t", 1)
    return datetime.fromisoformat(timestamp), commit


def link(document: Document) -> str:
    links = f"[{document.title}]({document.html})"
    if document.pdf:
        links += f" · [PDF]({document.pdf})"
    return links


def render() -> str:
    ranked = sorted(
        ((last_commit(document), document) for document in DOCUMENTS),
        key=lambda item: (-item[0][0].timestamp(), item[1].title.casefold()),
    )[:5]
    rows = [
        BEGIN,
        "## Recently updated",
        "",
        "These are the five most recently edited primary documents across the catalogue. Dates come from Git history for each document's canonical source file.",
        "",
        "| Document | Category | Last updated |",
        "|----------|----------|--------------|",
    ]
    rows.extend(
        f"| {link(document)} | {document.category} | {timestamp.date().isoformat()} |"
        for (timestamp, _commit), document in ranked
    )
    rows.extend(["", END])
    return "\n".join(rows)


def main() -> None:
    text = README.read_text()
    pattern = re.compile(re.escape(BEGIN) + r".*?" + re.escape(END), re.DOTALL)
    if not pattern.search(text):
        raise RuntimeError("README markers for the recent-documents block were not found")
    README.write_text(pattern.sub(render(), text, count=1))


if __name__ == "__main__":
    main()
