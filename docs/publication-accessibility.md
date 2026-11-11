# Publication accessibility

The shared primer route publishes HTML and PDF together for different uses.
HTML is the accessibility-complete format: the shared template provides a
document-title heading, named landmarks, a skip link, section heading levels,
and progressive contents controls. Contents links remain ordinary fragment
links when JavaScript is disabled, and the controls are added only as a
progressive enhancement.

The PDF route is a print-oriented companion. The pinned build currently uses
XeLaTeX and the committed output reports `Tagged: no` in `pdfinfo`. The
repository does not claim that this route produces tagged PDFs, PDF/UA
conformance, accessible reading order, or tagged tables and links. Do not add
PDF tagging claims until the pinned route is changed and validated with a PDF
tag-tree or accessibility checker. The limitation is deliberate and belongs
in release evidence for every affected publication.

Run `just render-qa <primer-directory>` after rendering. The ignored report in
`.scratch/render-qa/<primer-directory>/report.md` records HTML structural
checks, PDF metadata and text extraction, container provenance, and candidate
pages for human inspection. Complete the report or the pull-request evidence
with:

- keyboard navigation, including the skip link, contents toggles, and
  fragment navigation;
- no-JavaScript contents navigation;
- the browser accessibility tree for landmarks, document title, section
  levels, and TOC controls;
- a representative screen-reader traversal, with tool and version;
- PDF raster inspection of the opening, table, code, and figure/equation
  pages, plus an explicit tag-tree/accessibility-checker result.

These human checks complement the deterministic HTML checks. They do not
replace content review, visual inspection, or claims verification.
