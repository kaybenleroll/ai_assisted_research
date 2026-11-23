#!/usr/bin/env python3
"""Advisory comparison of Markdown H2/H3 candidates with published HTML.

This does not establish heading quality or release readiness. Review the source
and the rendered page whenever differences or ambiguous conversions are reported.
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from difflib import SequenceMatcher
from html import unescape
from html.parser import HTMLParser
from pathlib import Path
import re
import sys


@dataclass(frozen=True)
class Heading:
    level: int
    text: str
    location: str
    ambiguous: bool = False


def markdown_text(value: str) -> tuple[str, bool]:
    """Normalise common inline constructs; flag constructs needing human review."""
    value = re.sub(r"\s+\{#[A-Za-z][\w:.-]*\}\s*$", "", value)
    value = re.sub(r"\s+#+\s*$", "", value)
    code: list[str] = []
    def save_code(match: re.Match[str]) -> str:
        code.append(" ".join(match.group(2).split()))
        return f"\x00{len(code) - 1}\x00"
    value = re.sub(r"(`+)(.*?)\1", save_code, value)
    ambiguous = bool(re.search(r"!\[|\]\[|<[^>]+>|\{[^}]+\}|~~|\$", value))
    # Nested brackets and nested link destinations require a full Markdown parser.
    if re.search(r"\[[^]]*\[[^]]*\]|\]\([^)]*\([^)]*\)", value):
        ambiguous = True
    value = re.sub(r"\[([^\[\]]+)\]\([^()]*\)", r"\1", value)
    value = re.sub(r"(\*{1,3}|_{1,3})(?=\S)(.*?\S)\1", r"\2", value)
    value = re.sub(r"\\([!\"#$%&'()*+,\-./:;<=>?@\[\\\]^_`{|}~])", r"\1", value)
    for index, content in enumerate(code):
        value = value.replace(f"\x00{index}\x00", content)
    return " ".join(unescape(value).split()), ambiguous


def source_headings(text: str) -> tuple[list[Heading], list[str]]:
    headings: list[Heading] = []
    warnings: list[str] = []
    fence: tuple[str, int] | None = None
    nested_fence: tuple[str, int] | None = None
    previous = ""
    for number, line in enumerate(text.splitlines(), 1):
        if nested_fence is not None:
            close = re.match(r"^\s*(`{3,}|~{3,})\s*$", line)
            if close and close.group(1)[0] == nested_fence[0] and len(close.group(1)) >= nested_fence[1]:
                nested_fence = None
            continue
        nested = re.match(r"^(?: {4,}|\s*(?:[-+*]|\d+[.)])\s+)(`{3,}|~{3,})", line)
        if fence is None and nested:
            token = nested.group(1)
            nested_fence = (token[0], len(token))
            warnings.append(f"source:{number}: nested or indented fence is not fully supported; inspect its contents")
            continue
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
        if re.fullmatch(r" {0,3}(?:=+|-+)[ \t]*", line) and previous.strip():
            warnings.append(f"source:{number}: possible Setext heading is outside ATX H2/H3 candidate scope")
        previous = line
        match = re.match(r"^ {0,3}(#{2,3})[ \t]+(.+?)\s*$", line)
        if match:
            title, ambiguous = markdown_text(match.group(2))
            headings.append(Heading(len(match.group(1)), title, f"source:{number}", ambiguous))
        elif not re.match(r"^ {0,3}#{1,6}(?:[ \t]|$)", line) and re.search(r"\S[ \t]*#{2,3}[ \t]+\S", line):
            warnings.append(f"source:{number}: possible heading marker embedded in text; inspect rendered output")
    if fence is not None:
        warnings.append("source: unclosed fenced code block; later headings cannot be assessed")
    return headings, warnings


class HTMLHeadings(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.headings: list[Heading] = []
        self.level: int | None = None
        self.parts: list[str] = []
        self.start_line = 0
        self.ambiguous = False
        self.excluded: list[str] = []
        self.number_depth = 0

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attributes = dict(attrs)
        if self.excluded:
            if tag == self.excluded[-1]:
                self.excluded.append(tag)
            return
        if tag in ("nav", "header") or attributes.get("id") in ("TOC", "document-title"):
            self.excluded.append(tag)
            return
        if self.level is not None and self.number_depth:
            if tag == "span":
                self.number_depth += 1
            return
        if self.level is not None and tag == "span" and "header-section-number" in (attributes.get("class") or "").split():
            self.number_depth = 1
            return
        if tag in ("h1", "h2", "h3", "h4"):
            if self.level is not None:
                self.ambiguous = True
            else:
                self.level = int(tag[1])
                self.start_line = self.getpos()[0]
                self.parts = []
                self.ambiguous = False
        elif self.level is not None and tag in ("img", "br", "script", "style"):
            self.ambiguous = True

    def handle_data(self, data: str) -> None:
        if self.level is not None and not self.excluded and not self.number_depth:
            self.parts.append(data)

    def handle_endtag(self, tag: str) -> None:
        if self.excluded:
            if tag == self.excluded[-1]:
                self.excluded.pop()
            return
        if self.number_depth:
            if tag == "span":
                self.number_depth -= 1
            return
        if self.level is not None and tag == f"h{self.level}":
            self.headings.append(Heading(self.level, " ".join("".join(self.parts).split()),
                                         f"html:{self.start_line}", self.ambiguous))
            self.level = None


def analyse(source: str, html: str, level_offset: int | None = None) -> tuple[list[str], int | None]:
    candidates, warnings = source_headings(source)
    parser = HTMLHeadings()
    parser.feed(html)
    parser.close()
    if parser.level is not None:
        warnings.append(f"html:{parser.start_line}: unclosed heading; inspect rendered output")
    if level_offset is None:
        # Compare identical text at each plausible level mapping. Never silently
        # choose an offset when the available evidence gives a tied best score.
        scores = {}
        for offset in (-1, 0, 1):
            expected = [(h.level + offset, h.text) for h in candidates if not h.ambiguous]
            actual = [(h.level, h.text) for h in parser.headings if h.level in (2 + offset, 3 + offset) and not h.ambiguous]
            scores[offset] = sum(block.size for block in SequenceMatcher(a=expected, b=actual, autojunk=False).get_matching_blocks())
        best = max(scores.values())
        winners = [offset for offset, score in scores.items() if score == best]
        if len(winners) != 1 or not best:
            return warnings + ["ambiguous heading level offset; specify --level-offset and review the result"], None
        level_offset = winners[0]
    actual_headings = [h for h in parser.headings if h.level in (2 + level_offset, 3 + level_offset)]
    for heading in candidates + actual_headings:
        if heading.ambiguous:
            warnings.append(f"{heading.location}: ambiguous heading conversion: {heading.text!r}")
    expected = [(h.level + level_offset, h.text) for h in candidates]
    actual = [(h.level, h.text) for h in actual_headings]
    matcher = SequenceMatcher(a=expected, b=actual, autojunk=False)
    for operation, i1, i2, j1, j2 in matcher.get_opcodes():
        if operation == "equal":
            continue
        for heading in candidates[i1:i2]:
            warnings.append(f"{heading.location}: source heading differs or is absent from HTML: H{heading.level} {heading.text}")
        for heading in actual_headings[j1:j2]:
            warnings.append(f"{heading.location}: HTML heading differs or is absent from source: H{heading.level} {heading.text}")
    return warnings, level_offset


def compare(source: str, html: str, level_offset: int | None = None) -> list[str]:
    return analyse(source, html, level_offset)[0]


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source", type=Path)
    parser.add_argument("html", type=Path)
    parser.add_argument("--level-offset", type=int, choices=(-1, 0, 1), help="HTML heading level minus source level; infer when omitted")
    args = parser.parse_args(argv)
    try:
        findings, offset = analyse(args.source.read_text(encoding="utf-8"), args.html.read_text(encoding="utf-8"), args.level_offset)
    except (OSError, UnicodeError) as exc:
        print(f"outline comparison failed: {exc}", file=sys.stderr)
        return 2
    print("Advisory ATX H2/H3 candidate comparison; human review of hierarchy and other heading forms is required.")
    if offset is not None:
        method = "explicit" if args.level_offset is not None else "inferred"
        print(f"Heading level offset: {offset:+d} ({method}; HTML level minus source level).")
    else:
        print("Heading level offset: undetermined.")
    if findings:
        print("\n".join(f"- {finding}" for finding in findings))
        return 1
    print("No ATX H2/H3 candidate differences or ambiguous conversions detected.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
