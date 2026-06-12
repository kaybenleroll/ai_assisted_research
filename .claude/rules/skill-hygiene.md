# Skill Hygiene

Promoted from session captures. Review with `/reflect`.

---

- Run a comparison pass before planning any content migration, to establish actual scope
- For multi-point edits in a markdown file, write a single atomic script — sequential Edit calls cascade line-number shifts and break subsequent reads
- When grepping for H1 headings in markdown, exclude `#` lines inside fenced code blocks — they match the pattern but are bash comments, not headings
- When scoping coordinated changes to a project, check for companion documents beyond the primary source file
- When adding Mermaid diagrams to a primer, render a small subset covering all new syntactic features through the container before committing to a full build — the filter leaves raw fences in HTML output while pandoc exits 0 on failure
- After building a primer with Mermaid diagrams, grep the HTML output for raw fence patterns (graph LR, graph TB, subgraph, stroke-dasharray, literal {.mermaid}) — any hit means mmdc failed silently; also confirm each diagram has a rendered figure or img tag, as the build exits 0 regardless of mmdc failure
