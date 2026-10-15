# Review Checklist

Use this checklist for primer reviews. Select a profile, complete its passes, and record findings in the pull request.

## Pass 0: Choose a Profile

| Profile | Required passes |
|---|---|
| Mechanical sweep | Pass 2 for the scoped edits; Pass 3 when rendered output changes. Pass 1 only when claims or sources change. |
| Content edit | Passes 1 and 2; Pass 3 when rendered output changes. |
| New document | Passes 1–3. |

## Pass 1: Facts and Sources

Apply the R and C rules in the Style Guide. Until #142 adds those rule IDs, use the current source and quotation requirements in [STYLE_GUIDE.md](../STYLE_GUIDE.md), especially L2; the guide has no Sources heading yet, so update this reference when #142 lands. For contested subjects, apply D13 by attributing interpretations and distinguishing them from established facts.

- Open every AI-supplied reference. Confirm its title and author; resolve each DOI and check that it identifies the same work.
- Check quotations against the source. Preserve exact wording and context.
- Date volatile claims with “as of” wording. Attribute contested claims and separate evidence from interpretation.
- Record sources checked, corrections made, and any remaining uncertainty in the PR.

## Pass 2: Prose and Structure

- Check that one coherent opening orientation block delivers the stated promise, explains scope and exclusions, states prerequisites, and gives the reader a route through the document. Do not accept separate top-level headings for each orientation item unless a documented navigation need justifies them.
- For each section with child headings, check for a brief framing paragraph that explains its scope or internal relationship. Review one-paragraph subsections: consolidate those that merely split continuous reasoning, while retaining short subsections with a distinct conceptual, practical, comparative, or navigational purpose.
- Check that the main route is dependency-led: introduce the organising model before enumerating components, keep optional or reference-heavy branches clearly marked, and provide a comparison, synthesis, or decision framework after a broad survey where readers need one.
- Give every core concept an example: worked code, proof, case, comparison, counterexample, or failure case. Prefer explanatory prose to a dump of bullets.
- Apply D10: banned hedges are errors; filler is a suggestion. Review density above two filler terms in a paragraph or above 1.0 per 1,000 words, then fix the cause rather than swapping words.
- Check terminology consistency by searching for the main alternative term. Expand acronyms at first meaningful use; use the first-use helper below and review its candidates by hand.
- Apply D8: address the reader as “you”; use “we” in derivations. Apply D14 by keeping evidence strength and likelihood in separate uncertainty sentences. Apply D16 by giving each table a lead-in sentence.
- Check that examples are interpreted after they appear: state what each demonstrates, its assumptions or decisions, and its limits. For a long primer, record whether a running example or a set of local examples best serves the subject.

From the repository root, set `md` to the Markdown source under review. Until #159 supplies the automated hedge check, this command must return no matches:

```bash
grep -niE 'it should be noted|it is worth (mentioning|noting)|one might argue|needless to say|it is important to note' "$md"
```

Run the first-use acronym helper on the Markdown source; inspect false positives and record unresolved first-use expansions:

```bash
awk '/^[ \t]*(```|~~~)/{fence=!fence; next} !fence && !/^#/{print NR ":" $0}' "$md" | sed -E 's/`[^`]*`//g; s/\]\([^)]*\)/]/g; s#https?://[^ )>]+##g' | awk -F: '{ln=$1; $1=""; line=$0; while (match(line,/[A-Z][A-Z0-9]{2,}/)) {t=substr(line,RSTART,RLENGTH); ctx=substr(line,(RSTART>40?RSTART-40:1),RLENGTH+80); if(!(t in seen)){seen[t]=1; print ln ": " t " | " ctx} line=substr(line,RSTART+RLENGTH)} }' | grep -vE ': (HTTP|HTTPS|GPU|CPU|API|APIs|URL|JSON|README|CLI|PDF|HTML|SQL|CSS|YAML|TOML|UK|USA|LLM|LLMs|AI)\b'
```

Every opening code fence needs a language tag; empty output is required:

```bash
awk '/^[ \t]*```/{if(!fence){if($0 ~ /^[ \t]*```[ \t]*$/) print FILENAME ":" NR; fence=1} else fence=0}' "$md"
```

## Pass 3: Render QA and Visual QA

Follow [CONTRIBUTING.md — Render QA](../CONTRIBUTING.md#render-qa) for builds and render checks; this checklist does not repeat those steps.

**Visual QA** means rasterising and inspecting four PDF page types: the first page, a page with a table, a page with code, and a page with a figure or equation. Record each page number and pass or fail in the PR. This runnable example uses the pinned Pandoc base image and installs Poppler only inside the disposable container. The sample page numbers target `primer_evaluation_loop`; change them for the document under review. Run from the repository root; output stays under `.scratch`:

```bash
podman run --rm --entrypoint sh -v "$PWD":/work:Z -w /work docker.io/pandoc/latex@sha256:bd7641edf35bb8fad1316bacdac15fcc15f4d8d4f89051da2edcace15a6366d8 -c 'apk add --no-cache poppler-utils >/dev/null && mkdir -p .scratch/review-pages && for page in 1 17 13 3; do pdftoppm -f "$page" -l "$page" -png -r 120 primer_evaluation_loop/primer_evaluation_loop.pdf ".scratch/review-pages/page-$page"; done'
```

For another document, replace the PDF path and page numbers 17, 13, and 3 with pages containing a table, code, and a figure or equation. Open all four PNGs and record the result.

## PR Description Template

```markdown
Closes #N

Profile:
- Passes and commands run, with results:
- Facts and sources checked:
- Prose or structure changes and examples:
- Visual QA pages (type, page number, pass/fail), or reason not applicable:
- Exceptions and justification:
```

## Eight-Check Mapping

Use this table to report the eight content checks consistently.

| Check | Checklist item | Evidence in PR |
|---|---|---|
| 1 | Hedge grep in Pass 2 | Matches fixed or justified; record result. |
| 2 | First-use acronyms in Pass 2 | Helper candidates reviewed; list remaining issues. |
| 3 | Tagged fences in Pass 2 | Untagged-opening scan is empty or exceptions are listed. |
| 4 | Examples in Pass 2 | Name 3–5 core concepts and their example types. |
| 5 | Uncertainty in Passes 1–2 | List claims checked and changes made. |
| 6 | Subject-specific exposition in Pass 2 | Record one fix or “none needed” with sections checked. |
| 7 | Terminology in Pass 2 | State the chosen term and alternative searched. |
| 8 | Sources in Pass 1 | Name sources checked or added. |
