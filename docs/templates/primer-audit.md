# Primer audit: <title>

- Issue and milestone: <primary issue; related issues>
- Starting branch: <branch>
- Reviewer(s): <names or harnesses>
- Date: <YYYY-MM-DD>
- Reviewed revision: <commit, not only a branch>
- Brief reviewed: <path or issue comment>
- Review boundary: <whole-document, sampled, executed, or not checked for each method>

## Whole-document review

| Area | Scope and method | Exact evidence or location | Status | Finding or gap | Disposition |
|---|---|---|---|---|---|
| Brief coverage and scope | | | | | |
| Technical claims, derivations, and calculations | | | | | |
| Source quality, attribution, and freshness | | | | | |
| Explanatory depth and prerequisites | | | | | |
| Structure, dependency order, and section fragmentation | | | | | |
| Worked examples and interpretations | | | | | |
| Applications, limitations, and failure modes | | | | | |
| Figures, tables, equations, and accessibility | | | | | |
| HTML, PDF, metadata, and committed outputs | | | | | |
| Residual uncertainty and follow-up questions | | | | | |

Use status values such as `verified`, `reported by an earlier reviewer`,
`unresolved`, or `not checked`. Record whether evidence is whole-document or
sampled; an inventory or green build is not a correctness claim.

## Brief and example traceability

| Brief promise or core concept | Section(s) and explanation | Example, case, or limitation | Evidence status and gap |
|---|---|---|---|---|
| | | | |

For published code, map the reader-facing snippet to its executable example or
state that it is illustrative only. Check fixture schema, dependencies,
ordering conventions, and expected results; a smoke test that exercises a
different path does not verify the snippet.

| Published snippet or calculation | Test/manifest ID or illustrative status | Fixture and expected result checked | Gap |
|---|---|---|---|
| | | | |

## Representative sampling

Sampling supplements the whole-document pass. Record why each sample was
chosen; do not infer full-document coverage from these rows.

| Sample/page/object | Risk represented | Evidence and result | Status | Follow-up |
|---|---|---|---|
| Opening motivation | | | | |
| Formal or difficult passage | | | | |
| Worked example | | | | |
| Practical or real-world case | | | | |
| Table, code, figure, or equation page | | | | |

Choose samples by risk. Record the page, object, and defect separately for
visual checks; inspect figure meaning and accessibility in addition to file
existence.

## Reconcile earlier evidence

| Earlier finding or audit | Location and revision reported | Current status: confirmed, resolved, stale, or unverified | Evidence |
|---|---|---|---|
| | | | |

## Execution and render evidence

- Commands actually run: <commands and results>
- Examples executed: <IDs and runtime, or “none; illustrative only”>
- Examples parsed but not executed: <IDs and reason>
- Visual QA pages: <page/type/pass or fail>
- Offline or unavailable checks: <what could not be verified>
- Reviewer effort: <rough time and friction, without a quality score>
- Stopping rule: <what was deliberately not checked and why>

## Pilot learning

- False positives: <findings that did not represent a real defect>
- Missed issues: <issues found later or by another reviewer>
- Procedure changes proposed: <specific change or “none”>
- Remaining work: <issue-linked next actions>
