# Maths and Notation Guide

This guide is the notation contract for repository-authored documents that use mathematics. Share the table below with every parallel drafter before writing formulae. Readers need to know what a symbol means before they encounter it in a derivation.

## Notation Contract

**N1.** Put a reader-facing `## Notation` section before the first mathematical use in every new maths primer. Start it with a table of symbol, meaning, and first use; give each concept one notation and define variables locally when a derivation introduces them. Existing maths primers add the section when their #138 content-audit row is finished. [check: review]

For example, a document using gradient descent could begin its Notation section with this table, then explain the update immediately afterwards.

| Symbol | Meaning | First Use |
|---|---|---|
| $x_k$ | Parameter vector at iteration $k$ | Gradient descent update |
| $\eta$ | Positive learning rate | Gradient descent update |
| $\nabla f(x_k)$ | Gradient of the objective at $x_k$ | Gradient descent update |

The update is $x_{k+1}=x_k-\eta\nabla f(x_k)$, where $k$ counts iterations. The table is a model, not a repository-wide symbol dictionary: adapt it to the document's subject and keep its first-use descriptions navigable.

## Symbols and Typesetting

**N2.** Write the variant epsilon as `\varepsilon`. For example, if $|a_n-a|<\varepsilon$ for every $n\geq N$, say that $a_n$ is within the chosen tolerance $\varepsilon$ of $a$. Do not silently alternate it with `\epsilon` for the same quantity. [check: grep]

In a convergence argument, introduce the tolerance in words: "Given any $\varepsilon>0$, choose $N$ such that $n\geq N$ implies $|a_n-a|<\varepsilon$." The same glyph then carries the same meaning in the definition and the proof.

**N3.** Write standard number sets with blackboard bold, such as `\mathbb{R}`. For example, $f:\mathbb{R}\to\mathbb{R}$ with $f(x)=x^2$ maps every real input to a real output. Use the same form for other conventional sets when needed. [check: grep]

If a vector has two real components, write $\mathbf{x}\in\mathbb{R}^2$; the superscript gives the dimension, while the blackboard-bold letter identifies the number set. Reserve $\mathbf{R}$ for a vector or matrix that has actually been defined with that name.

**N4.** Write transpose as `^{\top}`. For example, if $x=(1,2)^{\top}$, then $x^{\top}x=1^2+2^2=5$. Convert historical `^T` or `^{T}` by hand when auditing a primer so surrounding notation remains coherent. [check: grep]

For a matrix $A$ and a vector $x$ with compatible dimensions, $x^{\top}Ax$ is a scalar quadratic form. The superscript is an operation on $x$; do not treat $T$ as a new variable in the Notation table.

**N5.** Declare the imaginary unit separately in each document, even when its letter seems conventional. For example, the digital signal processing primer keeps $j^2=-1$ so $e^{j\pi}=-1$; a complex analysis document may declare $i^2=-1$. Do not change a subject-specific convention merely to make letters uniform across primers. [check: review]

The declaration belongs near the first complex-valued formula and in the Notation table. In a signal-processing derivation, $j$ distinguishes the imaginary unit from a current often labelled $i$; a reader should never have to infer that choice from an example several sections later.

**N6.** Use semantic commands for named operators, upright labels, and words inside maths: `\operatorname`, `\mathrm`, and `\text`, respectively. For example, $\operatorname{rank}(A)=2$ names an operator, $v_{\mathrm{in}}=3$ uses an upright descriptor, and $P(\text{rain})=0.2$ embeds a word. Do not use `\mathrm{R}` for the real numbers; N3 uses `\mathbb{R}`. [check: review]

Here the operator acts on $A$, the subscript labels an input measurement, and "rain" names an event. If $v_{\mathrm{in}}=3$ and $v_{\mathrm{out}}=2$, then $v_{\mathrm{in}}-v_{\mathrm{out}}=1$; neither subscript is a multiplied variable.

**N7.** Treat variables as italic by default; do not impose ISO upright $\mathrm{d}$, $\mathrm{e}$, or $\mathrm{i}$ throughout the collection. For example, write $\int_0^1 x\,dx=1/2$ and declare whether $i$ denotes the imaginary unit when it occurs. Upright text still has the semantic uses in N6. [check: review]

Likewise, $e^x$ can denote the exponential when the context establishes that meaning; the guide does not require rewriting every occurrence as $\mathrm{e}^x$. A local discipline's established convention can still be declared and justified under the Style Guide's precedence rules.

**N8.** Use established LaTeX macros for ordinary structures: `\frac` for fractions, `\to` for arrows, `aligned` for related display lines, `\mathbf` for vectors and matrices, and `\|x\|` for norms. For example, if $\mathbf{x}=(3,4)^{\top}$, then $\|\mathbf{x}\|=\sqrt{3^2+4^2}=5$; a sequence $x_n\to 0$ tends to zero, and $\frac{1}{2}$ is one half. [check: review]

An aligned derivation can show both steps without inventing a macro:

$$
\begin{aligned}
(a+b)^2 &= (a+b)(a+b) \\
&= a^2+2ab+b^2.
\end{aligned}
$$

**N9.** Use `\cdots` between operators and `\ldots` in comma-separated lists. For example, $1+2+\cdots+n=n(n+1)/2$ has addition signs around its ellipsis, while $x_1,x_2,\ldots,x_n$ is a list of terms. [check: review]

In the sum, the omitted terms continue an arithmetic operation. In the list, the omitted entries are separated by commas. The different ellipsis macros make that distinction visible.

## Writing Mathematics

**N10.** Put words between consecutive formulae and make each display part of a sentence. For example, write "$a=b$. Therefore $a+c=b+c$" rather than placing the two equations together without a stated inference. Do not begin a sentence with a symbol; name the object first. [check: review]

**N11.** Write logical relationships in words in prose. Say "for every $x\in\mathbb{R}$ there exists a $y$" rather than using `∀` and `∃` as prose shorthand; say "therefore" rather than `⇒` between sentences. Symbols remain appropriate inside a formula when their meaning is explained. [check: review]

**N12.** State hypotheses with a theorem or claim and define each variable at first use, even when the Notation table lists it. For example, "If $f$ is differentiable on an open interval containing $a$ and $f'(a)=0$, then $a$ is a stationary point" states the needed domain and condition; it does not claim that $a$ is a minimum. [check: review]

**N13.** Number only equations that the document names or refers to later. For example, refer to "the update equation (3)" only if that equation has a stable visible number; leave a one-off calculation such as $2+2=4$ unnumbered. Keep prose references in step with any later renumbering. [check: review]

If the next section substitutes a new value into the same update rule, a number helps the reader find it. If no later sentence points back to the displayed rule, its position in the derivation supplies enough context.

**N14.** Use "we" for the author and reader working through a derivation together: "We substitute $x=2$ and obtain $f(2)=4$." Use the same term and symbol for a concept throughout a document unless a deliberate change is declared. [check: review]

These writing principles are consistent with Donald E. Knuth, Tracy L. Larrabee, and Paul M. Roberts, [*Mathematical Writing*](https://cs.stanford.edu/~knuth/klr.html) (Mathematical Association of America, 1989). The authorship and publication details are verified from Knuth's page; no rule numbers are attributed to the book here.

## Worked Example: A Norm Bound

The following small example shows how the notation contract and prose rules work together. Its symbols would appear before the derivation in a reader-facing Notation section:

| Symbol | Meaning | First Use |
|---|---|---|
| $\mathbf{x}$ | Vector with two real components | Vector definition |
| $\|\mathbf{x}\|$ | Euclidean length of $\mathbf{x}$ | Norm calculation |
| $\varepsilon$ | Positive tolerance | Final bound |

Let $\mathbf{x}=(3,4)^{\top}\in\mathbb{R}^2$. We first calculate its squared length using the transpose notation:

$$
\mathbf{x}^{\top}\mathbf{x}=3^2+4^2=25.
$$

Taking the non-negative square root gives $\|\mathbf{x}\|=5$. Now suppose $\varepsilon>0$ and $\|\mathbf{y}-\mathbf{x}\|<\varepsilon$ for another vector $\mathbf{y}\in\mathbb{R}^2$. The reverse triangle inequality gives the bound:

$$
\bigl|\|\mathbf{y}\|-5\bigr|
\leq\|\mathbf{y}-\mathbf{x}\|
<\varepsilon.
$$

The prose names the hypothesis and the conclusion; the display shows their mathematical relationship. If a later section uses this bound, that later reference is a reason to give the displayed inequality a number. Otherwise it remains unnumbered.

## Theorems and Proofs

**N15.** Use a bold-label paragraph for a theorem-like statement, with a number only when the surrounding document uses one. For example: **Theorem 3.2 (Uniqueness).** If $a=b$ and $a=c$, then $b=c$. State the hypotheses in the statement, not only in the proof. No new filter or fenced theorem block is required. [check: review]

**N16.** Start a proof with a bold `Proof.` label and close its final paragraph with ∎. For example: **Proof.** Since $a=b$ and $a=c$, symmetry gives $b=a$, and transitivity gives $b=c$. ∎ [check: review]

A proof can span several paragraphs when its steps need explanation. Put the end mark after the last sentence, not after the theorem statement or an intermediate calculation.

## Rendering and Source Markup

**N17.** Use `$...$` for inline maths and `$$` on their own lines for display maths. Keep display maths on separate source lines. Do not put raw LaTeX layout commands in prose or headings; `\hspace{0.25em}` currently leaks into two headings of `primer_military_structure` and belongs in its own later audit. Use DejaVu Sans Mono for Greek characters in code blocks so the PDF font covers them. [check: review]

**N18.** Default HTML maths to MathML in `primer_deep_learning`, `primer_digital_signal_processing`, `primer_evaluation_loop`, `primer_numerical_analysis`, and `primer_political_systems`. `primer_complex_analysis` defaults to MathJax following commit `2ddfb1d`; that commit records no reason for the choice. Record the reason in the commit message whenever a document's default renderer changes in future. [check: Justfile and commit]

**N19.** Provide maths variants and the renderer toggle only for a document whose source contains maths. Use the shared recipes described in [Contributing: Building](../CONTRIBUTING.md#building); that section is the source for variant commands and opt-in details. Do not add variants to a document without mathematical content. [check: source and Justfile]

## Audit Greps

**N20.** Run each search below on every maths source before its #138 audit row; record the baseline hit counts by file. Review matches in context: these searches find candidates, and a hit is not by itself a defect. The fifth search also has a repository-wide form to catch layout commands in other primers. [check: grep]

```bash
grep -nE '\\epsilon\b' "$file"
grep -nE '\\mathbf\{R\}|\\mathrm\{R\}' "$file"
grep -nE '\^T\b|\^\{T\}' "$file"
grep -nE '\\rightarrow' "$file"
grep -nE '\\(hspace|newpage|vspace)' "$file"
grep -nE '\\(hspace|newpage|vspace)' primer_*/*.md
```

The first four searches point to N2, N3, N4, and N8. Inspect layout matches for raw commands outside `{=latex}` blocks. `grep` returns 1 when it finds no matches; that is an empty result, not a command failure.

The six existing maths sources are `primer_complex_analysis/primer_complex_analysis.md`, `primer_deep_learning/primer_deep_learning.md`, `primer_digital_signal_processing/primer_digital_signal_processing.md`, `primer_evaluation_loop/primer_evaluation_loop.md`, `primer_numerical_analysis/primer_numerical_analysis.md`, and `primer_political_systems/primer-european-electoral-systems.md`. Apply the same searches to new maths sources when they are created; the guide does not assume that those documents already exist.
