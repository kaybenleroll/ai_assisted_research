# Publication accessibility

The shared primer route publishes HTML and PDF together for different uses.
The HTML template provides a document-title heading, named landmarks, a skip
link, section heading levels, and progressive contents controls. Contents
links remain ordinary fragment links when JavaScript is disabled, and the
controls are added as a progressive enhancement. These features and the
structural checks do not establish accessibility conformance.

The PDF route is a print-oriented companion. The pinned build currently uses
XeLaTeX and the committed output reports `Tagged: no` in `pdfinfo`. The
repository does not claim that this route produces tagged PDFs, PDF/UA
conformance, accessible reading order, or tagged tables and links. Record the
untagged limitation in release evidence for each affected publication.

Run `just render-qa <primer-directory>` after rendering. Its ignored report in
`.scratch/render-qa/<primer-directory>/report.md` records HTML structural
checks, PDF metadata and text extraction, container provenance, and candidate
pages for human inspection. The required baseline also includes the build,
link, metadata and freshness checks and visual inspection described in
[Contributing](../../CONTRIBUTING.md). Inspect PDF raster candidates for the
opening, table, code, and figure or equation pages, selecting another page when
a candidate does not contain the intended material.

## Interactive checks

The reviewer decides which human checks apply by examining the changes and
their effects; a successful render-QA run does not make that decision.
Changes to navigation mechanisms, interactive controls, or the rendering rules
that assign heading levels and ARIA semantics require interactive checks
scoped to the affected behaviour. This applies wherever the implementation
lives, including interactive HTML authored within a primer.

Ordinary content changes include adding or reorganising prose headings and
maintaining legacy fragment targets when material moves, using the existing
rendering components. These changes can alter the outline, contents entries
and destination elements without changing the interaction implementation.
Check structure, target IDs and the relevance of each destination. Interactive
checks are advisory for these revisions; preserved IDs alone do not establish
browser scrolling, focus or screen-reader behaviour.

When interactive checks are required, use keyboard navigation, no-JavaScript
navigation, the browser accessibility tree, and a representative screen reader
as applicable to the affected behaviour. Record the tools and versions, tested
controls or destinations, results, and any defects. Resolve known regressions
before release. Advisory status does not make a known broken interaction or
fragment link acceptable.

The containerised `just browser-qa` recipe supplies a repeatable Chromium sample
of keyboard, no-JavaScript and landmark behaviour; see [Contributing](../../CONTRIBUTING.md).
It does not run a screen reader. Record that review independently.

Record checks not performed as not performed, including advisory checks; do
not treat them as passed. Historical evidence retains its original result and
scope.

A change to PDF tagging or reading-order behaviour, or a claim that the PDF
supports either, requires a specialist tag-tree or accessibility-checker test
of that behaviour. The ordinary PDF metadata, text and visual checks remain
required regardless. These checks complement content and claims review; they
do not replace it.
