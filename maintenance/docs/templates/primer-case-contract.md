# Primer teaching-case contract: <title>

Use this contract for a primer that teaches a process, system, or applied
method. Complete it before drafting and review it again after the case is
implemented. A synthetic case is acceptable when its boundary and limitations
are explicit.

- Issue and milestone: <primary issue; related issues>
- Reader capability: <what the case should enable the reader to do>
- Case purpose: <why this case teaches the organising method>
- Case boundary: <population, sources, period, assumptions, and exclusions>

## Trace

| Stage | Description | Evidence or artefact | Status |
|---|---|---|---|
| Source inputs or assumptions | | | |
| Construction, extraction, or transformation decisions | | | |
| Intermediate records or representation | | | |
| Stored or computed result | | | |
| Reader-facing query or operation | | | |
| Interpretation of the result | | | |
| Failure mode or scope limit | | | |

## Teaching decisions

- Executable stages: <what runs, with manifest/test IDs>
- Illustrative stages: <what is shown but not run>
- Measured stages: <what has empirical measurements and how they were obtained>
- Required alternatives: <which representations or tools must use the same case>
- Expected abstentions or failures: <cases where refusing or qualifying an
  answer is part of the lesson>
- Evidence and freshness plan: <sources, versions, dates, and verification>

The contract is complete only when a reader can follow the case from its input
to an interpreted output and can see where the method stops applying.

## Binding current evidence after implementation

When a case records current source evidence, opt into mechanical checks with
exactly one `- Current source revision: <commit>` and one
`- Current source SHA-256: <64 lowercase hexadecimal digits>`. The revision
must resolve to a commit containing the same source bytes as the working tree;
the digest must match those bytes. Surround each group of current trace
locators with standalone `<!-- current locators: start -->` and
`<!-- current locators: end -->` lines. Use repository-relative `path:line`
or `path:first–last` locators; at least one is required. The audit gate checks
file existence and line bounds inside these regions. Historical references
outside them are not checked as current. Existing cases without the fields or
markers remain unbound. These checks establish mechanical consistency, not
whether the evidence supports the teaching claim.
