# PDF Transition Candidate Calibration

On 26 November 2026, a single reviewer tried a deliberately narrow screen:
extract layout text and select a page when its first non-empty extracted line
is a numbered figure caption. The previous page and that page are candidates
for visual inspection. This is a convenience for selecting a sample, not a
visual verdict or an exhaustive figure detector. Text extraction may place
image text before a caption, omit or reorder text, or fail altogether; figures
without matching captions and interruptions elsewhere on a page are missed.
Headers, captions with other formats, and scanned or untagged images can also
prevent selection. Zero candidates does not establish that a PDF is clear.

The GLM PDF at output revision `117083d` has SHA-256
`29f4ea649855957255c84f3ffcff68e9020ccd36b589a425120830270b74400b`.
Its 105 pages produced five candidates: 16–17, 58–59, 66–67, 82–83 and
91–92. The first four include all four previously recorded interruptions: an
introduction to an equation, two sentences and a code listing respectively;
see [the failure ledger](primer-audit-failure-ledger-471.md#pagination-changes-and-visual-sampling).
The reviewer visually inspected 91–92: Figure 9 occupies its own page after a
completed sentence, so this candidate is not an interruption. Thus one of
five candidates was a false positive for this narrow question. These known
cases informed the screen; they are not an independent validation set. Other
transitions were not exhaustively inspected, so unknown misses are unmeasured.

An independent input was the 108-page fluid-mechanics PDF at repository
revision `7575a008b027bba0bcb9808e3848bec7c9851722`, PDF last changed at
`b498fe28b5d4f55c01967635d3cf628228758fa6`, SHA-256
`8174023f76780b630d5c13cec872b9af8f5a40464a2317495b469769c6a9252c`.
The screen selected 13–14, 23–24, 27–28, 37–38, 39–40, 48–49, 62–63,
63–64, 93–94 and 95–96. Text triage identified three interruptions, which the
reviewer confirmed visually on pages 62–64 and 95–96: Figure 14 separates an
introduction from its equation, Figure 15 splits a sentence, and Figure 22
splits another sentence. These observations are specific to that output and
should be tracked for correction separately. The remaining seven candidates
were text-triaged only and are not counted as visually confirmed false
positives. The other transitions were not inspected and missed cases are
unknown. Candidate selection processed all extracted pages; it did not inspect
all page images. The reviewer opened five fluid pages and one GLM candidate
page, plus their surrounding extracted text. No elapsed review time was
recorded; this count is the available effort measure. The reviewer knew the
GLM cases and was not blinded. This small trial does not estimate general
recall or precision.

To reproduce the selection on an extracted UTF-8 text file, run:

```bash
pdftotext -layout path/to/document.pdf /tmp/document-layout.txt
python3 maintenance/scripts/pdf_transition_candidates.py /tmp/document-layout.txt
```

Use the configured container's Poppler for extraction where appropriate. Open
both sides of selected transitions and record the inspected scope. The screen is
optional and does not replace the existing representative visual review or
judgement about other high-risk transitions.
