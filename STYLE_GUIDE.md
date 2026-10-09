# Style Guide — ai_assisted_research Primers

This guide captures the house style for this collection. Use it as a system prompt when generating a new primer, or as a checklist when editing existing ones.

---

## Voice and Tone

**Casual and direct. Address the reader as "you."**

The primers in this collection are technically serious but not academically dry. Write as if explaining to a smart colleague who has not worked in this area yet — someone who wants real depth, not hand-waving, but also does not need it wrapped in formal language.

- Active voice over passive. "The agent calls the tool" not "the tool is called by the agent."
- No hedging language: never write "it should be noted," "it is worth mentioning," or "one might argue."
- No throat-clearing. Get to the point.

Remove empty verbal padding, not genuine uncertainty. State when evidence is
limited, a claim is conditional, interpretations differ, or behaviour depends
on an implementation. Precision is more useful than false certainty.

Prefer one main idea per sentence where that improves comprehension. Vary
sentence length when the argument needs it; sentence-length targets are editing
signals, not hard limits.

Use a knowledgeable-colleague tone: conversational, respectful and serious.
Address the reader as "you" when it helps, but do not turn every paragraph into
an instruction. Avoid slogans, clichés, unexplained idioms and promotional
language.

## Language Variant

Use **UK English** for all repository-authored prose, including technical
explanations and headings. Prefer forms such as `optimisation`, `behaviour`,
`modelling`, `organisation`, `organise`, `analyse`, `recognise`, `centre`,
`colour`, `catalogue`, `licence`, and `towards`.

Preserve the spelling required by:

- product, project, package, API, command, and configuration names;
- source-code identifiers, file names, and copied output;
- quotations and titles whose original spelling matters; and
- explicitly listed fixed technical terms whose spelling is part of the name.

A technical concept alone is not an exception: explain it in UK English.

Use `program`, `programming`, and related forms for software terminology. Use
`licence` for the noun in ordinary prose and retain `license` when it is part
of an API, command, product name, or quoted source. New primers should follow
this policy from their first draft.

### Audit baseline — 9 October 2026

The initial word-boundary scan covered committed Markdown outside `.scratch/`.
It found mixed usage rather than a single existing convention. The most
significant pairs were:

| US / UK spelling | US form | UK form |
|------------------|---------:|--------:|
| optimization / optimisation | 34 | 26 |
| behavior / behaviour | 107 | 100 |
| modeling / modelling | 36 | 5 |
| organization / organisation | 12 | 33 |
| center / centre | 26 | 43 |
| color / colour | 19 | 8 |
| catalog / catalogue | 8 | 31 |
| license / licence | 6 | 30 |
| toward / towards | 63 | 2 |

These counts are triage evidence, not a mechanical replacement list: they
include code examples, product terminology, quotations, and domain-specific
usage that require review in context. The remaining prose cleanup is tracked
separately so that it can be reviewed and rendered by document rather than
applied as an opaque repository-wide substitution.

## Plain Language Without Flattening the Subject

Plain language removes needless friction; it does not remove technical depth.
Keep precise terminology, hypotheses, exceptions, proofs and competing
interpretations when they help the reader reason about the subject. Define
unavoidable specialist terms at first meaningful use and use the chosen term
consistently afterwards.

Use examples deliberately. Worked examples are the default for technical
concepts, but a proof, historical case, comparison, counterexample or failure
case may teach another subject better. Pair abstract explanations with the
kind of example that lets the reader apply or test the idea.

Adapt the method to the subject. Code examples should be idiomatic; mathematical
primers should state hypotheses and show reasoning; humanities primers should
separate evidence, attribution and interpretation. Do not impose a single
academic voice or citation system on every primer.

## Structure, Navigation and Accessibility

Use descriptive, sentence-case headings with a logical hierarchy. Choose
heading levels for document structure, not visual appearance. Long primers
should provide a contents or other clear navigation aid and should work for
readers who consult individual sections out of order.

Use meaningful link text rather than bare URLs or phrases such as "click here".
Give tables and figures enough surrounding explanation to make their purpose
clear, and do not rely on colour alone to convey meaning. Use notes, cautions
and warnings sparingly: reserve warnings for material risk or an action the
reader must not take.

## Sources, Terminology and Freshness

Link important or contestable claims to the strongest available source,
preferring primary sources for product behaviour, standards and official data.
Date claims that can change. Use an annotated References or Further Reading
section where it helps the reader continue, but do not require formal
author–date citations in every primer.

Expand an acronym at first meaningful use. When a topic has competing
definitions, state which definition the primer uses and, where useful, keep a
short glossary or terminology note. Explain a general concept before giving a
vendor or product's exact term.

Prefer version-agnostic explanations where they remain accurate. When a claim
is version-specific, name the relevant version or date and link to the primary
documentation. Do not duplicate information across primers when a maintained
shared explanation or authoritative source will do; link to it instead.

## Editorial Authority

Apply guidance in this order:

1. The repository style guide and any primer-specific scope or terminology
   contract.
2. The subject's authoritative source, including exact product names, APIs,
   standards, quotations and source-code identifiers.
3. The principles in this guide: clear UK English, technically accurate
   explanation, useful examples, accessible structure and maintainable sources.

When a document needs to depart from the house style for a genuine subject or
audience reason, make the choice explicit and apply it consistently.

---

## Technical Depth

**Real depth. No soft-soaping.**

Assume a technical reader — comfortable with code, familiar with general computing concepts — but not a specialist in the topic. You do not need to explain what a function is. You do need to explain what a conditioning number is, why it matters, and what goes wrong when you ignore it.

When something can fail or go wrong, say so. Readers need to know the failure modes as much as they need the happy path.

---

## Intro Structure — Set Scope and Expectations Explicitly

Every primer should open with a clear statement of:

1. What problem or gap this primer addresses (and why existing resources fall short)
2. What you will and will not learn
3. What level of background is assumed

The numerical analysis primer does this well:

> "Most introductions to numerical analysis land in one of two camps: short and hand-wavey, easy to read but hard to use, or rigorous and dense to the point where they become difficult to apply in real work. [...] This primer tries to sit in the middle."

And then it has explicit "What This Primer Covers" and "What This Primer Is Not" subsections. Do the same. Make scope explicit; don't leave the reader guessing.

---

## "What This Is / Is Not" Framing

Always include it. Either as a subsection pair or woven into the intro. Examples from the collection:

- The openclaw primer opens with the exact ambiguity it resolves: two different projects share the name; this document is explicitly about one of them.
- The numerical analysis primer names two failure modes in existing resources, then explains how this one differs.
- The AI agents primer opens with the core misconception ("if LLMs generate text, how do they do things?") and answers it in the first paragraph.

Pick the specific confusion or gap your primer resolves and lead with it.

---

## Concrete Examples Over Abstract Descriptions

**Prefer worked examples when they clarify the idea.** Abstract descriptions
alone are rarely enough for a technical primer, but proofs, cases, comparisons
and counterexamples may be the right teaching device for other subjects.

Do this:
```python
# Root finding with Newton's method — explicit iteration trace
x = 2.0
for i in range(10):
    fx = x**2 - 2
    fpx = 2 * x
    x = x - fx / fpx
    print(f"step {i}: x={x:.10f}, error={abs(x - 2**0.5):.2e}")
```

Not this:
> Newton's method iteratively improves an estimate by subtracting the ratio of the function value to its derivative.

The second sentence belongs in the paragraph before the example, as motivation. The example is what makes it stick.

Mini worked examples mid-section are encouraged. The AI agents primer uses this frequently: "Mini example: an IT access agent receives 'Grant dashboard access.' It checks user identity, checks role policy, files an access request, and sends a confirmation." Short, concrete, shows the pattern in action.

---

## Section Structure — Narrative, Not Bullet Dumps

**Write in paragraphs.** Use bullet lists only when the content is genuinely list-shaped (steps in a sequence, a set of independent options, a checklist). Do not turn explanatory prose into bullets.

Do this:

> A practical debugging model is to think in layers: gateway, agent, provider, execution, state. Most troubleshooting becomes easier when you identify the failing layer before changing configuration.
>
> The gateway layer handles ingress, routing, APIs, and session plumbing. The agent layer carries prompt context, model selection logic, and tool-call behaviour...

Not this:

> Layers:
> - Gateway: ingress, routing, APIs
> - Agent: prompt context, model selection
> - Provider: model endpoints
> - Execution: tools
> - State: config, auth, session

The prose version teaches. The bullet list is a reference card. Know which you are writing.

Use headers to let readers navigate, not to fragment continuous reasoning into disconnected chunks.

---

## Code Blocks

Always use a language tag:

````markdown
```python
x = 1 + 1
```
````

Never leave code blocks untagged. This applies to shell commands (`bash`), configuration (`toml`, `yaml`), structured output (`json`), and pseudocode (`text` if nothing else fits).

When showing multiple language implementations of the same idea (as the numerical analysis primer does), present each in its own idiomatic style — do not port Python to R line-by-line.

---

## Do This / Not That

**1. Open with the real confusion, not a definition.**

Not that:
> Numerical analysis is the branch of mathematics concerned with numerical approximations of mathematical analysis.

Do this:
> Most introductions to numerical analysis land in one of two camps: short and hand-wavey, easy to read but hard to use, or rigorous and dense... This primer tries to sit in the middle.

---

**2. Name what the reader will not get, not just what they will.**

Not that:
> This primer covers root finding, linear systems, interpolation, ODEs, and optimisation.

Do this:
> This is not a full proof-based textbook, and it makes no attempt to be one. If you want convergence proofs and spectral theory with all conditions stated precisely, the reading list at the end will point you to the right books.

---

**3. Use a concrete mental model early, before the technical detail.**

Not that:
> An autonomous AI agent perceives its environment, reasons using an LLM, and acts to accomplish goals.

Do this:
> If you're coming from a software engineering background, a useful mental model is this: an agent is just a program with an LLM in the decision loop. If you're coming from product or operations, think of it as a very capable junior operator that can read instructions, use software tools, and report what it did.

---

## Unexplained Jargon

Introduce every term the first time it appears in the context of this document. You can assume general technical literacy; you cannot assume domain familiarity. If you use an acronym, expand it on first use. If you use a concept from another field, give a one-sentence grounding.

---

## Length

Primers in this collection are long-form by design. Do not pad, but do not compress past the point where a new reader can follow without outside reference. The goal is self-contained understanding, not a summary that requires the reader to go look things up. When in doubt, prefer the fuller treatment.
