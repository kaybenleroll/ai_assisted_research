# Style Guide — `ai_assisted_research` Primers

This guide captures the house style for this collection. Use it when generating a new document or editing an existing one.

## 0 Scope and Precedence

Rule IDs are stable: L covers Language, V Voice, S Structure, E Exposition and Examples, M Markup Mechanics, R Evidence and Sources, and C Contested Subjects. Keep existing IDs when moving or revising rules; do not reuse retired IDs. N is reserved for the maths guide, `docs/math-notation.md`, in issue #146; that file is planned, not yet a link target. Build, date-maintenance, and naming processes belong in CONTRIBUTING.md (issue #143), rather than here.

The table defines which rule groups apply to each document class; a subset names the applicable rule IDs.

| Class | L Language | V Voice | S Structure | E Exposition and Examples | M Markup Mechanics | R Evidence and Sources | C Contested Subjects |
|-------|------------|---------|-------------|---------------------------|--------------------|------------------------|----------------------|
| Primers | All | All | All | All | All | All factual claims | Selected primers (see below) |
| Article | Same as primers once repository-authored | Same as primers | Same as primers | Same as primers | Same as primers | All factual claims | — |
| Silo | All | — | S1 heading case only | — | All, with the class exceptions below | All factual claims | — |
| Workbook | All | — | — | — | M1 and M2 code rules only | All factual claims | — |
| README.md | All | — | S1 heading case only | — | — | All factual claims | — |

Silo uses `*` bullets, permits manual heading numbers, and does not use `--number-sections`. These class exceptions take precedence over the corresponding general mechanics. Workbook heading case and structure remain governed by its separate Quarto system. The Article row describes the replacement repository-authored article; preserve the wording of third-party republications until that replacement.

The C rules apply only to `primer_comparative_religion`, `primer_political_systems`, and `primer_military_structure`. R applies wherever a document makes factual claims.

Apply editorial authority in this order:

1. Subject authority for exact proper names, standards, APIs, identifiers, and quotations; see L2 for spelling boundaries.
2. This guide, including its explicit class exceptions.
3. A declared document-local exception for a genuine subject or audience reason, such as the digital signal processing primer's use of `j` for the imaginary unit.

A local preference does not silently override the guide. Declare a necessary departure, record its reason in the document, and apply it consistently within that limited scope. Subject authority preserves exact names and quoted text; it does not impose the source's spelling or editorial style on repository-authored explanations.

## Language

**L1.** Use UK English for all repository-authored prose and headings: `optimisation`, `behaviour`, `modelling`, `organisation`, `organise`, `analyse`, `recognise`, `centre`, `colour`, `catalogue`, `licence`, and `towards`. Mixed historical US/UK usage does not establish an exception to this policy. Use `program` and `programming` for software; use `licence` as the noun and `license` as the verb. [check: review]

**L2.** Preserve exact proper names (including product, project, and package names), standards, APIs, paper titles, identifiers (including commands, configuration keys, file names, and directory names), copied output, and quotations. A technical concept alone is not an exception: concepts and repository-authored document titles take UK spelling, including domain colouring, quantisation, and neighbourhood. The machine allowlist belongs in `_typos.toml` (issue #155), not in a prose list of fixed technical terms. [check: review]

**L3.** Write prose dates as `7 October 2026`. For an "as of" claim where a day would imply false precision, write `as of October 2026`. Use ISO dates such as `2026-10-07` only in README tables and machine-read fields; retain month-only precision as `2026-10` where that is all the evidence supports. [check: review]

## Voice

**V1.** Address the reader as "you" by default when giving guidance, without turning every paragraph into an instruction. Use "we" in derivations and worked reasoning; do not use "I" in repository-authored exposition. Write as a knowledgeable colleague: conversational, respectful, direct, and technically serious. Prefer active voice and avoid slogans, unexplained idioms, and promotional language. [check: review]

**V2.** Treat the empty hedge patterns in [House.Hedging](.vale/styles/House/Hedging.yml) as errors. Remove verbal padding while preserving the genuine uncertainty described in V3. [check: Vale]

**V3.** State when evidence is limited, a claim is conditional, interpretations differ, or behaviour depends on an implementation. Precision is more useful than false certainty. Prefer one main idea per sentence where that improves comprehension, and vary sentence length to suit the argument. [check: review]

**V4.** Treat filler vocabulary as an editing suggestion, not a ban; its lists live only in Vale configuration (issue #159). More than two filler terms in a paragraph, or a document rate above 1.0 per 1,000 words, triggers review. Fix the cause, for example by replacing a significance claim with a concrete fact or source; do not merely swap synonyms. These thresholds may be tuned after the first sweep. [check: review]

## Structure

**S1.** Use descriptive Title Case headings consistently within each document. The 20 minor words are `a`, `an`, `the`, `and`, `but`, `or`, `nor`, `for`, `so`, `yet`, `as`, `at`, `by`, `in`, `of`, `on`, `per`, `to`, `via`, and `vs`; lowercase them except at the start or end of a heading or immediately after a colon or dash. Capitalise all other words, including `Off` and `Up` (for example "Setting Up a Server"). Capitalise each part of a hyphenated compound unless it is a minor word; leave code spans, identifiers, and proper nouns as written. [check: review]

**S2.** Use one H1 as the canonical title, equal to the Justfile `TITLE`, with no refresh stamps in either. Sections start at `##`; do not skip heading levels or select levels for visual appearance. Normally stop at H4; use H5 only for exercise solutions or where a documented heading demotion requires it. For numbered Pandoc builds with a leading H1 and `##` sections, pass `--shift-heading-level-by=-1` with `--number-sections`, as specified in [CLAUDE.md](CLAUDE.md#primer-build-and-render-notes). [check: review]

**S3.** Open with one coherent orientation block: state what the document covers and which problem or gap it addresses, what it is not, the assumed background, and how to read it. Do not create a separate top-level heading for each item in this triad; use one opening section or integrated introductory prose, with short child headings only when they materially improve navigation. Include an annotated Further Reading section; maths primers also require a Notation section, with details assigned to issue #146. Exercises are optional; a glossary is optional and particularly useful above about 15 specialist terms. Learning objectives are not mandatory. New primers follow these requirements from their first draft; existing primers adopt them through their content-audit row in issue #138, and a maths primer's temporary Notation exemption ends when its row is finished. [check: review]

**S4.** Give long documents a contents or another clear navigation aid, and make individual sections useful to readers consulting them out of order. Where readers have materially different goals or a substantial optional path, provide concise task-based routes and identify reference material separately from the main narrative. Use headings to aid navigation without fragmenting continuous reasoning. [check: review]

**S5.** Write explanatory prose in paragraphs. Use lists for genuinely parallel items, sequences, options, or checklists, and tables for comparisons or mappings. A reference list can complement an explanation; it should not replace the reasoning that teaches the reader. [check: review]

**S6.** When a section contains subsections, introduce them with a brief framing paragraph that explains the section's scope, organising question, or relationship between its parts. Do not merely repeat the heading or list the subsection titles. A navigation-only section is exempt when it contains no substantive exposition. Avoid one-paragraph subsections when they divide a continuous explanation without adding a distinct concept, task, comparison, decision, or useful navigation point; consolidate such material under a broader heading. [check: review]

**S7.** Order the main route so that each stage establishes concepts needed by the next. Introduce the organising model before enumerating components, products, or options. Keep optional catalogues, advanced branches, extended scenarios, and operational reference material behind clear routes or headings; after a broad survey, provide a comparison, synthesis, or decision framework. [check: review]

## Exposition and Examples

**E1.** Keep real technical depth: precise terminology, hypotheses, exceptions, proofs, competing interpretations, and failure modes. Assume general technical literacy rather than domain expertise; explain what a condition number is, why it matters, and what goes wrong when it is ignored. Adapt the method to the subject: mathematical reasoning needs hypotheses, and humanities explanations distinguish evidence, attribution, and interpretation. [check: review]

**E2.** Define unavoidable specialist terms and expand acronyms at first meaningful use, then use the chosen terminology consistently. Give a concept from another field a short grounding; explain a general concept before introducing a vendor's exact term. Where definitions compete, state which one the document uses. [check: review]

**E3.** Prefer worked examples for technical concepts, including small examples within a section, when they let the reader apply or test the idea. Use a proof, historical case, comparison, counterexample, or failure case when it teaches the subject better. Pair abstract explanation with the appropriate teaching device rather than replacing explanation with an example alone. [check: review]

**E4.** Close the example loop. After an example, explain what it demonstrates, which assumptions or decisions it exposes, and where it stops applying. Prefer a small number of coherent running examples when they let concepts build across sections; state whether an example is synthetic, illustrative, executable, or measured. [check: review]

For example, introduce Newton's method in prose, then show its iteration and error:

```python
x = 2.0
for step in range(10):
    fx = x**2 - 2
    fpx = 2 * x
    x = x - fx / fpx
    print(f"step {step}: x={x:.10f}, error={abs(x - 2**0.5):.2e}")
```

**E5.** Keep conceptual grounding inline so a new reader can follow without outside reference; primers are long-form by design. Prefer accurate version-agnostic explanations, and link volatile product and version facts to maintained authoritative sources rather than duplicating them across primers. Link important or contestable claims to the strongest available source, preferring primary documentation, standards, and official data; identify the relevant version or date for claims that can change. Do not pad or compress away necessary reasoning, and do not impose one academic citation system on every subject. [check: review]

The following current passages illustrate clear problem framing and scope boundaries:

> Most introductions to numerical analysis land in one of two camps: short and hand-wavey, easy to read but hard to use, or rigorous and dense to the point where they become difficult to apply in real work.

Source: [primer_numerical_analysis/primer_numerical_analysis.md](primer_numerical_analysis/primer_numerical_analysis.md).

> This is not a full proof-based textbook, and it makes no attempt to be one.

Source: [primer_numerical_analysis/primer_numerical_analysis.md](primer_numerical_analysis/primer_numerical_analysis.md).

## Markup Mechanics

**M1.** Use backtick code fences with a language tag: `bash` for shell commands, `python` or `r` for code, `toml` or `yaml` for configuration, `json` for structured output, and `text` for pseudocode or output when no more specific tag fits. Keep code lines about 90 characters or fewer where practical, and omit the `$` prompt from shell command blocks. [check: review]

**M2.** Present each language implementation in its own idiomatic style; do not port Python to R line by line. [check: review]

**M3.** Write each prose paragraph on one source line, with blank lines between paragraphs and around headings, lists, tables, and code fences. Use `-` for unordered bullets (Silo uses `*`) and `*italic*` for emphasis. [check: review]

**M4.** Use straight double quotes as the primary quotation marks, single quotes only for nested quotations, and straight apostrophes in new and edited source text. Apply logical punctuation: full stops and commas go outside closing quotes unless a complete quoted sentence ends the sentence. For example, the label is "ready". A complete quotation is: "The agent calls the tool." Review punctuation in context. Existing curly quotes render identically under `+smart` and are not swept; legacy inside-quote punctuation is corrected per primer through issue #138. Preserve exact source quotations under L2. [check: review]

**M5.** Use a spaced em dash (` — `) for a prose break and an unspaced en dash for ranges; either `10--20` or `10–20` is accepted in source. Always use the serial comma. Write `e.g.` and `i.e.` with dots and no following comma; use forms such as `5%`, `1,234`, `8 GB`, and `vs`. [check: review]

**M6.** Use meaningful link text rather than bare URLs or "click here". Give each image descriptive alt text and a surrounding text statement explaining its point; explain figures and tables sufficiently, and do not rely on colour alone to convey meaning. [check: review]

**M7.** Put a lead-in sentence before every table. Omit captions by default; use a Pandoc `Table:` caption only when referring to the table elsewhere. The four Silo reference sheets (`gaming_silo_rpg/gaming_silo_player_guide.md`, `gaming_silo_rpg/gaming_silo_gm_secrets.md`, `gaming_silo_rpg/gaming_silo_comprehensive_bible.md`, and `gaming_silo_rpg/gaming_silo_starter_campaign.md`) may place a table directly under its heading as a D16 layout exception, but the caption and accessibility rules still apply. [check: review]

**M8.** Use `> **Note:**` and `> **Warning:**` blockquotes for callouts, sparingly; reserve warnings for material risk or an action the reader must not take. The only allowed fenced-div classes are `.broad-table`, `.compact-table`, and `.code-group`, defined in [doc_template.html](doc_template.html). Use the existing template without adding CSS or filters for callouts. [check: review]

**M9.** For multi-language examples, put consecutive fenced code blocks one after another; the HTML template turns them into tabs, and print and PDF show them in sequence. Label each block with a bold paragraph on its own line that ends in a colon, such as `**Python:**`, `**R:**`, or `**Python (SciPy):**`. The trailing colon also satisfies markdownlint MD036, which otherwise treats a bold-only line as a pseudo-heading. Never add Pandoc attributes to bold text: `**Python**{.code-label}` renders the literal text `{.code-label}` and breaks the tabs. A `::: {.code-group}` fenced div may bound a group. [check: review]

## Evidence and Sources

**R1.** Cite the strongest available source for an important factual claim; prefer primary documentation, standards, and official data, and use a paper when it is the strongest evidence. [check: review]

**R2.** Link to the specific source page that supports the claim, not a site homepage; identify papers with a DOI or arXiv identifier. [check: review]

**R3.** Date claims that can change with `as of Month YYYY`, and avoid relative-time wording such as "currently" or "recently". [check: review]

**R4.** State evidence strength separately from likelihood: never combine a confidence term and a likelihood term in one sentence, and do not impose a fixed scale. [check: review]

**R5.** Apply E5's duplicate-versus-self-contained tie-break: link volatile product and version facts, but keep conceptual grounding inline. [check: review]

**R6.** A primer needs a one-line verification note when it contains time-sensitive claims, including named products or versions, prices, limits, benchmark figures, current office-holders, or statements about the current state of a field; decide and record this per primer during its sources pass, without naming a fixed set of primers. Write the note only after checking the sources, leave it undated, and place it directly after the orientation block: *Verified against primary sources for sections X–Y; unverified claims are flagged inline.* Replace X–Y with the verified section range or "all sections". Mechanical passes do not add or edit this note. [check: review]

## Contested Subjects

**C1.** Attribute opinions, distinguish facts from interpretations, give views weight in proportion to their evidential support and acceptance, and label fringe views as such rather than giving every position equal weight. [check: review]

**C2.** Use contentious labels only when attributed to a source or group that uses them, and explain relevant terminology without adopting a party's framing as neutral description. [check: review]

**C3.** Keep descriptive accounts distinct from analytical claims: describe what a community holds as a descriptive statement, and attribute scholarly interpretations as analysis. [check: review]

**C4.** Include a terminology and transliteration note that identifies the conventions used and explains significant alternatives. Where national terminology differs for equivalent institutions, roles, or equipment, give a comparison table; military structure coverage compares NATO, UK, and US terms. [check: review]

**C5.** Date claims about office-holders and doctrine when they can change; use ICD 203 tradecraft (alternatives, indicators, and linchpin assumptions) only within forecasting passages. [check: review]
