# Primer production procedure

This procedure is the portable, harness-agnostic route for creating or
substantially revising a technical primer. It describes the order of work and
the evidence to retain; it does not replace the [style guide](../STYLE_GUIDE.md),
[contributor guide](../CONTRIBUTING.md), or [review checklist](review-checklist.md).
Those documents remain authoritative for prose, repository mechanics, and
content and render QA respectively.

The procedure is deliberately a route, not a quality scorecard. A primer may
be short or long, use few or many headings, and contain no figures when that is
the right decision for its audience. The brief and audit should make those
decisions visible and explain exceptions.

## Lifecycle at a glance

1. **Brief:** define the reader, problem, boundaries, depth, examples, evidence
   plan, and unresolved decisions.
2. **Research:** establish the dependency-led route, authoritative sources,
   terminology, calculations, examples, and known uncertainty.
3. **Scaffold and register:** create the primer through the repository recipe,
   settle the outline, register the document, and record the build route.
4. **Draft:** write from the dependency structure, integrating examples,
   figures, equations, limitations, and practical use cases.
5. **Independent review:** review the whole document for coverage and claims;
   sample representative passages and outputs for depth, structure, and layout.
6. **Render and verify:** build the committed HTML/PDF outputs in containers and
   run the repository checks and visual checks required by the guides.
7. **Evidence and handoff:** record what was checked, what was sampled, what
   remains uncertain, and the exact next action for the next harness or writer.

For a revision, begin by comparing the existing source, outputs, issue scope,
and companion documents. Do not treat a previous audit or a clean CI result as
evidence that the current content is correct.

## 1. Write the brief

Copy [the brief template](templates/primer-brief.md) into an issue or ignored
`.scratch/` handoff note. The brief should answer:

- Who is the reader, what do they already know, and what should they be able
  to do or explain afterwards?
- What problem does the subject solve, why did the approach arise, and what is
  explicitly outside scope?
- What dependency-led route will make the explanation cumulative rather than a
  catalogue of terms?
- What depth is appropriate, and which examples, languages, figures, tables,
  equations, and real-world cases will carry the explanation?
- For a process, system, or applied method, what central teaching case traces
  source inputs through construction to useful outputs, interpretation, and
  limitations? Which stages are executable, illustrative, or measured? Complete
  the [teaching-case contract](templates/primer-case-contract.md).
- Which core concepts need a mechanism or reasoning explanation, why they
  matter, conditions or limits, and a worked case, comparison, counterexample,
  proof, or failure case? Record this in the brief's depth matrix.
- Which claims require primary or current sources, and which calculations or
  executable examples need independent checking?
- Which decisions remain unresolved, and what evidence would settle them?

The brief is a planning instrument, not a promise to preserve every proposed
section. During review, record deliberate omissions and changes in scope.

## 2. Research and design the route

Research in dependency order. Establish the smallest set of concepts needed to
understand the motivating problem, then add formal machinery, worked examples,
applications, limitations, and adjacent methods. For volatile software or
product claims, verify against current primary documentation before publication.

Create a source map that distinguishes definitions and theorems, historical or
motivational claims, current implementation facts, worked-example inputs, and
illustrative interpretation. Check that examples are mathematically or
operationally reproducible and that a citation supports the claim it follows.

Use bounded independent review during research for difficult or disputed
points. Record the question and result; do not treat agreement between agents
as a source.

## 3. Scaffold, register, and establish the build route

Run `just new-primer <short> "<Full Title>"` from the repository root and
complete every registration step it prints. Before adding substantial prose:

- replace the scaffold metadata and settle the source H1 and `TITLE`;
- add the directory to the document-class list in
  [the project contract](project-contract.md);
- add the source and required outputs to the root registration and generated
  README table through the documented recipe;
- define the top-level build targets and any executable-example manifest;
- decide whether maths variants, figures, or a dedicated runtime are needed;
- record the exact container and recipe used for rendering.

The scaffold should be buildable before drafting begins. Keep source, Justfile,
HTML, and PDF ownership together when the document is later committed.

## 4. Draft for explanation

Draft around the reader's decisions and dependencies. A useful local pattern is
motivation, idea, formal statement, worked example, interpretation, limitations,
and practical use. Combine short sections when they do not establish a real
change of subject; retain a heading when it gives the reader a useful landmark
or separates a materially different argument.

For a process, system, or applied method, keep at least one coherent case moving
through the draft. Show its input or assumptions, the decisions that transform
them, the resulting representation, a useful operation or query, and what the
result does and does not establish. Do not let a pre-curated fixture stand in
for construction unless the brief explicitly makes that a deliberate teaching
choice.

Examples should do explanatory work. For each substantial example, state the
input or assumptions, show the method, interpret the result, and note the
failure mode or limitation. Prefer a small hand-worked example before a larger
real-world case. Keep code examples aligned with the repository's executable
example policy: illustrative snippets are not silently presented as tested
programs.

## 5. Run the post-draft audit

Use [the audit template](templates/primer-audit.md) and review the complete
source, not just a sample. The whole-document pass checks the brief, coverage,
technical claims and calculations, source support, explanatory depth,
structure, examples, figures/tables/equations, limitations, outputs, and
residual uncertainty.

For a process, system, or applied-method primer, the audit must complete the
teaching-case trace from input through construction, representation, useful
operation, interpretation, and limits. If that trace cannot be completed, the
content gate has a substantive finding regardless of build or smoke-test
results.

Sampling is complementary, not a substitute for reading. Choose representative
passages and output pages: an opening motivation, a formal or difficult
derivation, a worked example, a practical application, and pages containing
tables, code, figures, or equations. Record why each sample was chosen. A
sampling pass may reveal layout or local explanation failures that a global
grep cannot; it cannot establish whole-document coverage.

Do not convert the audit into a quality score, a fixed word count, or a heading
quota. Record findings, severity, evidence, disposition, and reviewer effort.
False positives and missed issues discovered during a pilot belong in the
audit notes so the procedure can improve without weakening the review standard.

## 6. Render and verify

Follow the exact build, lint, link, freshness, variant, Mermaid, and visual QA
routes in [CONTRIBUTING.md](../CONTRIBUTING.md) and
[the review checklist](review-checklist.md). At minimum, record:

- the commands and container/runtime versions actually used;
- whether examples were executed, merely parsed, or left illustrative;
- HTML/PDF freshness and metadata results;
- representative visual pages and their pass/fail result;
- link and source checks, including known limitations or offline checks.

Use `just render-qa <primer-directory>` to collect the mechanical HTML/PDF
evidence and raster candidates in one ignored bundle. Treat its page choices as
sampling suggestions, open each generated PNG, and record the human result in
the report and PR; the command does not replace visual inspection.

Generated outputs are part of the deliverable. Never claim a render or example
was checked from the existence of a file alone.

## 7. Handoff and release

Use the [portable handoff template](agent-collaboration.md#portable-handoff-template)
when another harness or writer will continue. Include the issue and milestone,
branch and revision, dirty paths, owned files, decisions and evidence, exact
checks, remaining work, and blockers. Recheck live Git state at handoff; a
conversation is not durable project state.

The PR description should identify one primary issue, list related issues on
separate lines, state what this milestone completes, and name any remaining
work. Merge only after the required checks and review evidence are available.
