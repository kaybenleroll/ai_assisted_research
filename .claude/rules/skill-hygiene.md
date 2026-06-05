# Skill Hygiene

Promoted from session captures. Review with `/reflect`.

---

- Run a comparison pass before planning any content migration, to establish actual scope
- For multi-point edits in a markdown file, write a single atomic script — sequential Edit calls cascade line-number shifts and break subsequent reads
- When grepping for H1 headings in markdown, exclude `#` lines inside fenced code blocks — they match the pattern but are bash comments, not headings
- When scoping coordinated changes to a project, check for companion documents beyond the primary source file
