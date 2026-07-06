# The Evaluation Loop: How AI Systems Learn to Improve

## The Core Idea: Measure It, Then Optimise It

Here is the thing nobody tells you when you start building with AI: the model is often the easy part. You can download a strong open-weight model this afternoon, or call a frontier one over an API in three lines of code. What separates a system that gets better every month from one that plateaus on day one is whether you have built a loop that turns mistakes into the next improvement signal — and whether, somewhere in that loop, you can attach a defensible number or checklist to "how good was that?"

Andrej Karpathy gave this loop its clearest articulation. In his 2017 essay "Software 2.0," he argued that for a growing class of problems, the program is no longer hand-written logic but a model whose behaviour is shaped by data, and so "most of the active software development takes the form of curating, growing, massaging and cleaning labeled datasets." The precondition he named for this to work at all is blunt: "repeated evaluation is possible and cheap." Hold onto that sentence. The whole primer hangs off it.

By December 2022 Karpathy had sharpened the idea into what he called a data engine. His formulation, in paraphrase: competitive advantage in AI goes not so much to those with data, but to those with a data engine — iterated data acquisition, re-training, evaluation, deployment, and telemetry — and the winner is whoever can spin that loop fastest. The loop has a fixed shape:

```{.mermaid caption="The data engine loop: every box is plumbing; evaluate is the load-bearing sensor."}
graph LR
    collect[Collect] --> label[Label] --> train[Train] --> evaluate[Evaluate]
    evaluate --> deploy[Deploy] --> telemetry[Telemetry] --> collect
    style evaluate fill:#f96,stroke:#333,stroke-width:3px
```

You collect inputs, label them with the right answer, train a model, evaluate how well it does, deploy it, gather telemetry on where it fails in the wild, and feed those failures back into the next collection round. Tesla's self-driving stack is the canonical worked example. The team would identify a rare failure scenario — say, a particular kind of badly-occluded stop sign — design a trigger that fires when the fleet encounters it, collect sensor data from cars that hit that trigger, annotate it at scale, retrain, deploy, and repeat. Their "Shadow Mode" is the telemetry step made concrete: a shadow autopilot runs silently alongside the human driver, and every time its prediction disagrees with what the human actually did, the system banks a candidate failure case. The disagreement is the signal.

This loop goes by several names, and you will meet all of them in the wild. "Data engine" is Karpathy's own term. "Karpathy loop" is a community paraphrase — useful shorthand, but not a phrase Karpathy himself coined, so do not go looking for it in his writing. "AutoResearch" and "the AI development loop" show up in other corners. They all point at the same diagram above.

The organising principle underneath all of it is one more Karpathy line, and it is the one to tattoo on the inside of your eyelids: "Traditional software automates what you can specify; LLMs and reinforcement learning automate what you can verify." Old-school software needs you to write down the rules. Modern AI systems instead need you to be able to *check* an answer — to evaluate it — even when you could never have written the rules that produce it. You cannot specify, in code, what makes a good translation or a good summary or a good explanation. But if you can reliably judge one, you can optimise toward it.

Which is exactly why the evaluate step is load-bearing, and why it gets a whole primer to itself. Think of the data engine as a control loop, the kind that runs a thermostat: it senses a value, compares it to a target, and acts to close the gap. A thermostat without a thermometer is just a heater with no off switch. The evaluate step is the thermometer. It is the only place in the loop where open-ended performance gets converted into a number, and without that number, nothing downstream can move. Training has no gradient to follow. Deployment has no bar to clear. Telemetry has nothing to compare against. The loop does not slow down — it stops. Every other box in the diagram is plumbing; evaluate is the sensor, and a control loop is only ever as good as its sensor.

So the deep problem of this primer is not only "how do we train models." It is the prior question: when the thing you care about is subjective — clarity, helpfulness, taste, judgment — how do you manufacture an evaluation signal trustworthy enough to optimise against? Sometimes that signal is a scalar score for weight updates; sometimes it is a behavioural rubric for instruction and skill wording. That is the question the rest of these pages take apart.

### What This Primer Covers

- The data engine loop and why evaluation is its load-bearing step.
- A practical fork in the loop: improving model weights at scale versus improving instruction and skill wording at low volume.
- Why open-ended quality resists measurement, and why reference-overlap metrics like BLEU and ROUGE fail on it.
- The generator-discriminator gap: why judging is easier than producing, and why that asymmetry rescues evaluation.
- The four moves that turn subjective quality into a usable score: Decompose, Compare, Aggregate, Automate.
- The lightweight instruction loop: rubric-driven transcript inspection for iterative skill wording improvements.
- Behaviourally-anchored rubrics as a replacement for vague quality scales.
- Pairwise comparison and large-scale human preference collection (Chatbot Arena).
- Aggregating comparisons into latent ratings via Elo and the Bradley-Terry model, with the mathematics worked through.
- G-Eval and reading a judge's log-probabilities to recover a continuous score.
- The bridge from a fitted Bradley-Terry model to the RLHF reward model — the same operation at a different scale.
- Reinforcement Learning with Verifiable Rewards (RLVR), the SWE-bench trajectory, and the hard boundary where verifiable rewards stop helping.

### What This Primer Is Not

This is not a machine-learning textbook, and it proves nothing — there are no convergence theorems here, no gradient-descent derivations, no statistical guarantees about when a rating system is consistent. It is not a runnable end-to-end application; the code snippets are illustrative kernels, not a deployable harness. It is not an RLHF training guide — the reward model gets named and located, not trained — and it is not a survey of every benchmark on the leaderboard. The primer is self-contained for the one thing it is about, the measurement step of the loop; for the territory it deliberately skips, the Further Reading section points you outward.

## The Subjectivity Problem, Stated Plainly

Start with the question that actually stops you, the one with no obvious answer: if you want a system to do something well, how do you turn open-ended performance into a number you can optimise against? Optimisation needs a scalar. Gradient descent, hyperparameter sweeps, leaderboards, A/B tests — every one of them consumes a number and pushes it in a direction. But "did the model explain this well?" is not a number. It is a judgment, and judgments are exactly what we said modern AI is for: the things you can verify but cannot specify. The subjectivity problem is the gap between those two clauses.

Make it concrete. Suppose you pose a single question to a model:

> "What is a derivative contract? My manager mentioned it in a meeting and I have no finance background."

You get back two replies. **Response Alpha** is technically immaculate. It explains that a derivative's value is a function of an underlying asset, references notional value, walks through delta-hedging, mentions mark-to-market accounting. Every word is correct. To the person who asked — a non-specialist who said outright they have no finance background — it is a wall. **Response Beta** reaches for an everyday analogy instead: a derivative is like a home insurance policy. You pay a premium now for the right to claim later; the value of the contract moves with the thing it is written on; and neither party actually expects the event to happen. It is clear, it is memorable, and it sacrifices some precision — "moves with the thing it is written on" is not how a quant would phrase it. Which response is better? You already have an instinct. The hard part is defending that instinct with a number.

The first thing people try is to compare the output against a reference answer. This is where the classical metrics live. **BLEU** (Bilingual Evaluation Understudy) was built for machine translation: it measures n-gram overlap between the candidate text and one or more reference translations, scored from 0 to 1. **ROUGE** (Recall-Oriented Understudy for Gisting Evaluation) was built for summarisation: it is recall-oriented, counting unigram and longest-common-subsequence overlap with reference summaries. Both ask the same underlying question — how many of the "right" words showed up in roughly the right arrangement?

For our derivatives question, that approach collapses on contact. There is no single reference answer — there are thousands of good explanations, sharing little vocabulary with one another. **Response Beta** shares almost no words with **Response Alpha**, and the insurance analogy — the very thing that makes it good — would score near-zero against any finance-textbook reference, because it contains the word "premium" and almost nothing else a textbook would use. Worse, the metric has no way to tell a brilliant analogy apart from random noise that happens to miss the reference vocabulary; both look equally bad to an n-gram counter. The metric rewards lexical mimicry and is blind to whether the explanation actually landed. You could write a response that overlaps heavily with the reference and is still useless, or one that overlaps barely and is excellent, and BLEU would rank the useless one higher.

This is not a quirk of one example. On open-ended tasks, BLEU and ROUGE show near-zero correlation with human judgment — they were designed for tasks with tight reference answers, where the set of acceptable outputs is small and lexically similar, and they degrade to noise the moment the space of good answers opens up. That is the crucial distinction. Machine translation and short summarisation have *constrained* output spaces: there are only so many correct ways to render a sentence in another language, and they overlap heavily. "Explain a derivative to a beginner" has an *open* output space, where the best answers can be lexically disjoint. The metrics are not wrong, exactly; they are measuring the wrong thing, and measuring it precisely. A precise measurement of the wrong quantity is more dangerous than a vague one, because it looks rigorous.

A scope note before going further: this primer treats bias and fairness only where they intersect measurement — where a scoring choice silently encodes a preference, or where a rater pool skews a rating. The broad ethics of fairness in AI is its own field and its own literature; here it appears strictly as a measurement concern.

So absolute scoring against a reference is a dead end for subjective tasks. The way out comes from noticing an asymmetry that Karpathy put plainly: an average person cannot write a good poem, but can easily pick the better of two poems. The skill required to *produce* excellent open-ended work is enormous; the skill required to *recognise* which of two candidates is better is far smaller and far more reliable. This is the **generator-discriminator gap** — discrimination is cheaper and steadier than generation.

You can see it in the numbers on humans themselves. When you ask two people to assign an absolute quality score to a single LLM response, their inter-rater agreement typically lands somewhere in the 70–81% range, depending on the task and how tightly the annotation protocol is written. That range is itself instructive: tighten the protocol and the agreement climbs toward the top of the band; leave "good" undefined and it sinks toward the bottom. But it never reaches 100%, because reasonable people genuinely disagree about what "good" means in isolation. That residual disagreement is the noise floor — the irreducible scatter you cannot annotate your way out of.

That 70–81% figure deserves more scrutiny than it usually gets, because raw percent agreement is a misleading measure. If two raters scribbled scores at random — each using a 5-point scale with equal frequency across the points — they would still land on the same number roughly 20% of the time, purely by accident. Raw agreement therefore conflates genuine consensus with chance overlap, and inflates the apparent reliability of any annotation process. The fix is to subtract out the chance baseline. Cohen's $\kappa$ (Cohen, 1960) does exactly this for two raters:

$$\kappa = \frac{p_o - p_e}{1 - p_e}$$

where $p_o$ is the observed agreement and $p_e$ is the agreement expected by chance. A $\kappa$ of 0 means the raters agree no better than dice; $\kappa = 1$ is perfect agreement. The conventional benchmarks (Landis and Koch, 1977) read $\kappa < 0$ as poor, $0$–$0.2$ as slight, $0.2$–$0.4$ as fair, $0.4$–$0.6$ as moderate, $0.6$–$0.8$ as substantial, and $> 0.8$ as near-perfect.

Two raters is the simple case. Fleiss' $\kappa$ generalises the same chance correction to $n > 2$ annotators scoring the same items, and Krippendorff's $\alpha$ is the most flexible of the family — it copes with any number of raters, nominal through interval scales, and missing data. Run the chance correction on subjective LLM-quality annotation and the comfortable percent-agreement numbers collapse: measured in Fleiss' $\kappa$, inter-rater agreement on output quality typically sits in the moderate band, $0.4$–$0.6$, in the literature. The task is genuinely harder than raw agreement lets on.

The noise floor sets a hard ceiling on automation, and this is the number to internalise. A well-tuned LLM-as-judge agrees with humans at roughly 80–85% under optimised protocols. Read that against the 70–81% humans manage with each other and the conclusion is uncomfortable but clean: the best automated judges sit *at* the human-human floor, not above it. An LLM judge is not a more objective oracle that escapes human messiness — it is a fast, cheap imitation of a human rater, and it inherits the rater's disagreement as its hard limit. No judge, human or machine, gets to be more certain about subjective quality than humans are with each other. Any pipeline that reports 95% "accuracy" on a subjective task is measuring agreement with one particular labelling convention, not agreement with the truth.

Here is the hinge the whole next section swings on. Ask a human "rate this response 1 to 10" and you get noise. Ask the same human "which of these two is better, **Response Alpha** or **Response Beta**" and you get a far more stable answer. The generator-discriminator gap says comparison is where the reliable signal lives. The four moves that follow are, at bottom, an elaborate scheme for converting that one reliable judgment — A beat B — back into the scalar that optimisation demands.

## Manufacturing a Number: The Four Moves

You cannot directly measure "quality." So you manufacture a stand-in. Four moves do the manufacturing, always in this order: **Decompose, Compare, Aggregate, Automate**. Each move buys you something — tractability, reliability, a scalar, scale — and each one charges the same toll. What comes out the far end is never quality itself. It is a *correlated shadow of quality*: a number that moves with the thing you care about closely enough to optimise against, while never being the thing itself. Name that price at every step, because forgetting it is how teams end up optimising the shadow until it detaches from the substance.


```{.mermaid caption="The four moves convert subjective quality into an optimisable scalar, one transformation at a time."}
graph LR
    q[Subjective quality] --> d["Decompose<br/>sub-dimensions"]
    d --> c["Compare<br/>pairwise verdicts"]
    c --> a["Aggregate<br/>latent rating"]
    a --> au["Automate<br/>LLM-judge scalar"]
    au --> s["Correlated shadow<br/>of quality"]
    style s stroke-dasharray: 5 5
```
### Decompose

The first move attacks the vagueness head-on. "Was this a good explanation?" is unanswerable because "good" hides a dozen distinct questions. So you break it into 3–6 sub-dimensions and give each one a small, **behaviourally-anchored** scale — every level defined by an observable behaviour rather than an adjective. Instead of "rate clarity 1–5," you write a rubric where a 4 means "fully resolves the task without any missing step" and a 0 means "leaves the core question unanswered." The anchors are behaviours, not vibes.

For the derivatives question, you might decompose "good answer" into accuracy, accessibility-to-a-non-specialist, completeness, and memorability. Now the two responses separate cleanly. **Response Alpha** scores high on accuracy, low on accessibility. **Response Beta** scores high on accessibility and memorability, slightly lower on accuracy. The vague tie has become four legible numbers. The price: a rubric is a theory of what matters, and the moment you write it down you have decided that these four dimensions, weighted this way, *are* quality. They are a correlated shadow of it — a good rubric tracks quality closely, but an answer can game every sub-dimension and still miss, because the rubric is a model of good, not good itself.

### Compare

The second move cashes in the generator-discriminator gap. Stop scoring responses in isolation; show a judge two at a time and ask only which is better. This is what Chatbot Arena (the LMSYS platform) does at scale: users see two anonymous model responses to the same prompt and vote for the one they prefer. The 2024 paper (Chiang, W.-L. et al., "Chatbot Arena: An Open Platform for Evaluating LLMs by Human Preference," ICML 2024, arXiv:2403.04132) reported roughly 240,000 pairwise preference votes at time of publication; the platform's cumulative total grew into the millions by 2025–2026. For our example, the comparison is exactly the question you could already answer: shown **Response Alpha** beside **Response Beta** for a self-declared non-specialist, which is better? The price: a pile of "A beat B" verdicts is more reliable than any single score, but it is not yet a number you can rank with. A heap of pairwise outcomes is a correlated shadow of a quality ordering that does not yet exist as a scale.

### Aggregate

The third move turns that heap of comparisons into a single latent rating per item — the scalar optimisation has been demanding all along. Two equivalent framings dominate. **Elo**, borrowed from chess, assigns each item a rating and updates it after every match. The expected score for A against B is

$$E_A = \frac{1}{1 + 10^{(R_B - R_A)/400}}$$

and after a match the rating moves toward the surprise in the result:

$$R_A' = R_A + K(S_A - E_A)$$

where $K$ is the K-factor, typically 32. In code:

```python
def elo_update(rating_a: float, rating_b: float,
               outcome: float, k_factor: float = 32) -> tuple[float, float]:
    """
    outcome: 1.0 if A won, 0.5 if draw, 0.0 if B won.
    Returns updated (rating_a, rating_b).
    """
    expected_a = 1 / (1 + 10 ** ((rating_b - rating_a) / 400))
    expected_b = 1 - expected_a
    new_rating_a = rating_a + k_factor * (outcome - expected_a)
    new_rating_b = rating_b + k_factor * ((1 - outcome) - expected_b)
    return new_rating_a, new_rating_b
```

The **Bradley-Terry** model (1952) is the more principled framing: it treats each item as having a latent strength and models the probability that A beats B as

$$P(A \succ B) = \frac{e^{\beta_A}}{e^{\beta_A} + e^{\beta_B}}$$

then fits the strengths $\beta$ to maximise the likelihood of all the observed comparisons at once. Chatbot Arena moved from Elo to Bradley-Terry for exactly this statistical robustness (LMSYS blog, December 2023). Elo is the easier story; Bradley-Terry is the better statistics. Run our votes through either and **Response Beta** surfaces with the higher latent rating for the non-specialist audience — quality has become a coordinate.

Here is the bridge worth stopping for. The fitted Bradley-Terry model is not only a leaderboard tool. Scale it up — make the latent-strength function a small transformer that scores *any* output rather than a fixed table of items — and you have built the **reward model** used in RLHF. It is the identical operation: fit a model over comparisons. The §3 Aggregate step, generalised to a neural network over all possible outputs and applied during training, *is* the RLHF reward model. §6 onward picks this up; the identity is laid here. The price stays fixed: a latent rating is a correlated shadow of quality, and a reward model is that same shadow with a gradient running through it — optimise hard enough against it and the model learns the shadow's blind spots.

### Automate

The fourth move removes the human from the inner loop so the whole thing can run at machine speed. You replace the human judge with an LLM judge, and the sharpest version reads more than the judge's chosen token.

The prompt that does the asking looks like this:

```text
You are an expert evaluator scoring how well a response answers a question
for a specific reader. Judge only the response shown; do not rewrite it.

QUESTION:
"What is a derivative contract? My manager mentioned it in a meeting and I
have no finance background."

RESPONSE:
{{response}}

Score the response on each dimension below, using the 1-5 scale:

  Accuracy       — is every claim correct and free of misleading shortcuts?
  Accessibility  — would a self-declared non-specialist follow it unaided?
  Completeness   — does it resolve the question without leaving a core gap?
  Memorability   — will the reader retain the core idea afterwards?

Scale anchors:
  5 — exemplary: meets the dimension with no reservation
  4 — strong: meets it with a minor, non-blocking flaw
  3 — adequate: meets it but with a flaw a careful reader would notice
  2 — weak: partially meets it; a real shortcoming on this dimension
  1 — failing: does not meet it at all

Return one integer score (1-5) per dimension, then one sentence of
justification per dimension. Output the scores first.
```

The chosen integer is the lossy part; G-Eval recovers the rest.

**G-Eval** (Yang Liu et al., "G-Eval: NLG Evaluation using GPT-4 with Better Human Alignment," EMNLP 2023, arXiv:2303.16634) does not take the judge's output token "4" at face value. It reads the log-probabilities the judge assigns to each score token "1" through "5" and computes the expected value:

$$\hat{s} = \sum_{i=1}^{5} i \cdot p_i$$

so a judge torn between 3 and 4 yields a continuous 3.74 instead of a lossy rounded integer.

```python
import math

def g_eval_score(logprobs: dict[str, float]) -> float:
    """
    logprobs: mapping from score token ("1".."5") to raw log-prob
    Returns the expected score as a continuous float.
    """
    # Convert log-probs to probabilities
    total = sum(math.exp(lp) for lp in logprobs.values())
    p_scores = {token: math.exp(lp) / total for token, lp in logprobs.items()}
    expected_score = sum(int(token) * p for token, p in p_scores.items())
    return expected_score
```

Now an LLM judge reads the derivatives question, reads **Response Alpha** and **Response Beta**, and emits a score with no human in the loop — at the cost that the judge has its own biases, and its number is a correlated shadow of a human judgment, which was itself a correlated shadow of quality. You are now two shadows deep, which is precisely why the agreement ceiling from §2 matters: automation cannot climb above the human noise floor it was trained to imitate.

Two cheap mitigations take the worst of that bias off the table before you trust the number. The first is a **position swap**: run the judge twice on the same pair, once with **Response Alpha** first and once with **Response Beta** first, and average the two scores. An LLM judge has a standing tendency to favour whichever response it reads first or last regardless of content, and presenting each order exactly once cancels that tendency arithmetically rather than hoping the judge ignores it. It doubles the inference cost and removes a whole class of artefacts; the trade is almost always worth it. The second is **multiple independent judges**: run several judges on the same pair and average their scores or take a majority vote. This shrinks the per-judge variance the way any ensemble does, and it partially dilutes systematic self-preference — a panel of different model families cannot all rate the same response highly purely because each finds its own phrasing more probable. Neither move tells you *why* the biases exist; §8 takes apart the mechanisms — self-preference, verbosity, and position — and explains why instructing a judge to be impartial does not remove them. For now it is enough that the swap and the panel blunt their effect.

These four moves are not specific to chatbots. Take an insurance company evaluating how well an LLM summarises complex policy documents for claimants. The moves apply identically: **Decompose** "good summary" into accuracy, coverage, plain-language score, and a missing-information penalty; **Compare** two candidate summaries pairwise; **Aggregate** the comparisons into a latent quality rating; **Automate** with an LLM judge that reads the policy and the summary together. Different domain, same machine — and the same toll, four times over: every number it produces is a correlated shadow of quality, never quality itself.

## The Lightweight Loop: When You Are Editing Instructions, Not Weights

The four moves described above — and the rest of this primer from here onward — assume you have something you can retrain. The loop spins because you can collect failures, label them, and push a gradient through parameters. But there is a second, growing class of practitioners who are iterating on AI systems and have no weights to adjust at all: they are editing instruction text. A system prompt. A workflow definition. A skill file that tells an agent to diagnose a bug by working through five specific phases in order before touching any code. The model itself is fixed; the thing being changed is what it is told to do.

This looks like the same problem. It has the same feel — change something, observe whether the system behaves better, change it again. But the feedback mechanism is structurally different, and applying the full four-move apparatus to it produces the wrong tool for the job. It is worth making this distinction explicit before the primer moves into reward models and RLHF, because the instruction-editing case is where most practitioners first encounter the question "how do I measure this?" — and where the machinery in the next sections is most likely to mislead by appearing applicable when it is not.

### What Changes, and What Does Not

Model training changes what a system *knows* — parameters encode probability distributions over tokens, shaped by every gradient update the model has ever received. Instruction editing changes what it is *told to do* — the context it receives each time it is invoked. These are different levers. A badly-worded training example degrades underlying capability. A badly-worded instruction leaves the capability intact but misdirects it: the model can follow the instruction it received, it is just not the right instruction. The failure modes are different, the evidence trails are different, and the correction mechanisms are different.

The practical consequence: you do not need a training signal to improve instructions. You need to be able to read the instruction's output and tell whether it did what you intended. That is a simpler requirement than manufacturing a gradient, but it is the same underlying demand from §2 — you must be able to evaluate the output before you can improve the system.

### Quality Means Something Different Here

For the single-turn responses in earlier sections, "quality" meant something about the content of the answer — accuracy, accessibility, completeness. For instruction-following systems that prescribe a multi-step process, quality primarily means **adherence**: did the agent execute the intended steps, in the intended order, without skipping? Adherence is observable. You do not need a judge to manufacture a number; you need a checklist that describes what correct execution looks like at each phase, and a session transcript to check it against. For a diagnostic skill that says *build a feedback loop before hypothesising*, the criterion is concrete: a runnable repro or failing test must exist in the session before any hypotheses are offered. Either it does or it does not. The generator-discriminator gap from §2 applies here too — it is much easier to check whether a phase was skipped than to produce the correct phase yourself — but the check costs almost nothing because the answer is binary.

This is the **Decompose** step from §3 applied not to output quality but to *process* quality. Instead of breaking "good answer" into accuracy, accessibility, and memorability, you break "correct skill execution" into its observable phases and write a behavioural anchor for each one: what does completion of this phase look like in the transcript? Write those anchors before you ever invoke the skill, because writing them forces you to notice which phase descriptions are vague enough to permit skipping. A rubric that says "phase 1 complete: a runnable repro exists" is immune to the slippage that afflicts a rubric that says "phase 1 complete: the agent seems to understand the problem."

### The Lightweight Loop

The loop that results is recognisably the data engine, running at much lower RPM:

```{.mermaid caption="The instruction-editing loop is the data engine at human speed: inspect transcripts against a rubric, locate the wording that permitted the failure, revise it."}
graph LR
    write["Write instruction<br/>with phase rubric"] --> invoke["Invoke in<br/>real sessions"]
    invoke --> inspect["Inspect transcript<br/>against rubric"]
    inspect --> locate["Locate wording<br/>that permitted failure"]
    locate --> revise["Revise<br/>that wording"]
    revise --> write
```

The collect step is invoking the instruction in real work. The label step is checking the transcript against the rubric — did phase 1 complete before phase 2 began? The evaluate step is noting which phase the adherence failure clustered in. The train step is editing the specific wording that allowed the failure. There is no automated scoring and no gradient; the loop runs at the speed of a session post-mortem rather than a GPU. But it is the same loop, with the same load-bearing evaluate step in the middle.

A practical note on volume: the statistical methods from §3 — Elo, Bradley-Terry, G-Eval — require enough comparisons to converge to a stable estimate. For a collection of twenty or thirty skill files, each invoked a handful of times per month, that threshold is never reached. Inspection-and-revision works better at this scale than scoring-and-aggregating, for the same reason that you would not run a clinical trial on a sample of four. The quantitative machinery is not wrong; it is simply inappropriate to the data volume available.

### Worked Example: Improving `grill-me` Wording with a Karpathy-Style Loop

Take a real workflow skill such as `grill-me`. The goal is not to improve the model's latent reasoning ability; it is to reduce instruction ambiguity so execution is more consistent. The loop is the same shape as Karpathy's data engine, but each stage is lightweight and text-driven.

Start with a concrete failure pattern you can observe in transcripts:

- The skill asks user questions too early, before enough repo exploration.
- The skill asks broad or duplicate questions that could have been answered from code.
- The skill claims "shared understanding" but still leaves unresolved design branches.

Now define behavioural anchors (your measurement surface):

| Dimension | 0 (Fail) | 1 (Pass) |
|---|---|---|
| Exploration-first adherence | First user question appears before evidence summary | Evidence summary appears before any user question |
| Non-derivable questioning | Asks questions answerable from repo/docs | Asks only questions explicitly marked non-derivable |
| Tree closure | Ends interview with open branches | Replays decisions and lists no unresolved branches |

With those anchors, rewrite only the wording most likely to permit failure. For example:

Before (weak, easy to misinterpret):

```text
Ask one question at a time after exploration.
```

After (strong, testable):

```text
Do not ask the user any question until you have produced an evidence summary
from repository findings with at least 5 concrete facts.
For each fact, cite the source file/path.
Only ask a user question if you cannot derive the answer from code/docs after
exhaustive search; for each such question, state why it is non-derivable.
Before finishing, replay all decisions and explicitly list unresolved branches
as "OPEN" (or state "No open branches").
```

Notice what changed: not tone, but observability. The revised wording creates transcript-visible pass/fail checks.

Then run a small loop over real work (for example, 5 invocations):

1. Use version A wording for sessions 1-2 and version B for sessions 3-5.
2. Score each session against the three binary anchors above.
3. Count pass rates per anchor for A vs B.
4. Keep B only if it improves at least two anchors without regressing the third.
5. If not, edit the smallest ambiguous phrase and rerun another 3-5 sessions.

This is Karpathy's loop in miniature:

- Collect: session transcripts.
- Label: anchor pass/fail per session.
- Train: edit instruction wording.
- Evaluate: compare anchor pass rates by wording version.
- Deploy: keep the better wording and continue observing.

No gradients, no reward model, no Elo required. The loop still qualifies as an evaluation engine because it converts fuzzy dissatisfaction ("this skill feels off") into a repeatable update rule over observed behaviour.

### Worked Example: Improving `diagnose` Wording Without Touching Weights

The same method applies to a process-heavy skill such as `diagnose`, where the central requirement is to establish a reproducible feedback loop before hypothesising. In practice, this skill often drifts in exactly one direction: the agent starts proposing causes before it has built a deterministic reproducer. That drift is not a model-capability failure. It is a wording-permission failure.

Suppose you review five recent sessions and see this pattern:

- In three sessions, hypotheses appeared before any runnable failing test or deterministic repro script.
- In two sessions, the loop existed but was flaky (non-deterministic, noisy assertions).
- In one session, the agent moved to implementation after observing a single failing run rather than a stable repeated failure.

You can score this with an anchor set aimed at behavioural compliance:

| Anchor | Fail condition | Pass condition |
|---|---|---|
| Repro-gate | Hypothesis appears before loop artifact exists | Runnable repro artifact exists before first hypothesis |
| Loop quality | Loop is flaky or symptom-level only | Loop is deterministic and asserts the target symptom |
| Transition discipline | Moves to fix without stable repro evidence | Moves to fix only after repeated stable failure signal |

Now tighten only the instruction text that allowed the most common failure.

Before (high-level, permissive):

```text
Do not proceed to Phase 2 until you have a loop you believe in.
```

After (operational, transcript-checkable):

```text
Before any hypothesis is stated, produce a runnable repro artifact
(test, script, or command) and execute it twice with the same failing signal.
If the two runs do not fail identically, treat the loop as invalid and continue
loop-hardening; do not hypothesise yet.
Only enter fix implementation after a stable loop is present and the exact
assertion/symptom is captured in the artifact output.
```

This revision does three useful things: it introduces a hard gate ("before any hypothesis"), it forces repeatability (two matching failures), and it defines what qualifies as transition readiness.

Run a small A/B sequence in live work:

1. Label three sessions under old wording and three under new wording.
2. Score each session on the three anchors above.
3. Compute pass-rate deltas per anchor.
4. Keep the new wording only if repro-gate and transition-discipline both improve and loop-quality does not regress.

At this scale, avoid overfitting to one anecdote. Keep a wording change only if it survives at least three independent tasks with different failure modes (for example API bug, UI regression, and performance issue). If it helps one and hurts two, revert.

### A Reusable Micro-Protocol for Any Skill Wording Edit

Most teams get stuck because they try to "improve the whole skill" at once. The loop works better when each cycle edits one ambiguous phrase and tests one explicit hypothesis.

Use this protocol:

1. Pick one recurring failure in transcripts, phrased as behaviour, not vibes.
2. Write 2-4 binary anchors that would detect this failure.
3. Identify the narrowest phrase in the skill that could permit it.
4. Rewrite that phrase so pass/fail is visible in transcript evidence.
5. Test on 3-5 real invocations.
6. Keep or revert based on anchor deltas, then log the result.

A useful logging format is a one-line changelog per iteration:

```text
skill=diagnose | change=add repro hard gate | sample=6 sessions |
repro_gate +50pp | loop_quality +17pp | transition_discipline +33pp | keep
```

Those one-line records become your low-volume dataset. They are small, but over time they let you answer practical questions that otherwise remain fuzzy: Which wording edits reliably improve adherence? Which edits trade one failure for another? Which skills are stable enough to stop changing for a while?

### From Fuzzy Intuition to Controlled Iteration

When people say "this skill feels off," they are usually detecting one of three things: a gate is too soft, a criterion is unobservable, or an exit condition is undefined. The lightweight loop gives each of those a direct correction path:

- Soft gate -> convert to explicit precondition with a visible artifact.
- Unobservable criterion -> replace adjectives with evidence requirements.
- Undefined exit -> add explicit completion language and unresolved-branch handling.

That is the practical payoff of importing Karpathy's loop into instruction design. You are not pretending to run frontier post-training on a handful of sessions. You are building a disciplined measurement-and-revision habit that is proportionate to the scale of skill files and still grounded in evaluation, not intuition alone.

### Operating Checklist: Evaluate and Improve One Skill Wording

Use this checklist to run a single improvement cycle on a skill. Copy it, fill it in, file the result, and repeat. Over time the one-line logs from step 7 become your skill-wording audit trail.

**1. Identify the failure pattern**

- [ ] Review 3–5 recent transcripts of this skill.
- [ ] Describe the specific failure in behaviour terms (not "feels off" or "wrong", but "X appeared before Y in the transcript").
- [ ] Estimate frequency: does this failure appear in 1/5 sessions? 3/5? Every session?

**2. Write behavioural anchors**

- [ ] Define 2–4 binary criteria that would let you check if the failure occurred.
- [ ] For each criterion, write explicit pass and fail conditions.
- [ ] Verify: could you hand these criteria to someone unfamiliar with the skill and they could score a transcript?

**3. Identify the ambiguous phrase**

- [ ] Read the skill file and locate the phrase most likely to permit the failure.
- [ ] Is it a gate condition? A criterion description? An exit condition?
- [ ] Make sure it is one phrase, not a paragraph — you are editing a pinpoint, not a rewrite.

**4. Rewrite for observability**

- [ ] Replace adjectives with evidence requirements (e.g., "thorough exploration" -> "5+ concrete facts with file paths").
- [ ] Add explicit gating language if this is a gate ("before X is done, never do Y").
- [ ] Add explicit artifact requirements if this controls evidence ("produce a runnable test" not "understand the problem").

**5. A/B test on real work**

- [ ] Use old wording for sessions A1, A2, A3 (or as many as you have this week).
- [ ] Use new wording for sessions B1, B2, B3 (next few sessions).
- [ ] Score all sessions against the anchors from step 2.
- [ ] Record pass rate for each anchor under A and B.

**6. Decide: keep, revert, or iterate**

- [ ] Check: does the new wording improve at least two anchors?
- [ ] Check: does it regress any anchor by more than 1–2 sessions (noise tolerance)?
- [ ] If yes to both checks, keep the new wording.
- [ ] If no, revert and try a different phrase, or run more sessions if you have fewer than three per condition.

**7. Log the result**

Copy and paste this line into a skill-changelog file (e.g., `.scratch/skill_wording_log.md`):

```text
skill=SKILLNAME | date=YYYY-MM-DD | change="DESCRIBE THE REWRITE" | 
sample=N sessions | anchor1_delta=±Npp | anchor2_delta=±Npp | 
anchor3_delta=±Npp | decision=KEEP/REVERT | notes="ANYTHING INTERESTING"
```

Example:

```text
skill=diagnose | date=2026-06-18 | change="add repro hard gate: 'before any hypothesis, execute repro twice with matching failure'" |
sample=6 sessions | repro_gate=+50pp | loop_quality=+17pp | transition_discipline=+33pp | decision=KEEP | notes="transitions still delayed on one complex session, not regression, will monitor"
```

**8. Move to the next skill or repeat**

- [ ] If you logged a KEEP, let it run for another 5–10 sessions to check for side effects.
- [ ] If you logged a REVERT, file a note of what didn't work so you don't try the same edit again.
- [ ] Pick the next skill with the clearest failure pattern and repeat from step 1.

### Prompt Template: Copy and Paste to Evaluate a Skill

If you want to run a skill-wording evaluation loop with agent assistance, copy the template below into a Claude Code session (or similar) and fill in the bracketed sections. This prompt will guide a subagent through the measurement and revision steps.

```text
I want to improve the wording of a Claude Code skill to reduce execution failures.

## Skill to Evaluate

Skill name: [SKILLNAME]
Skill file path: [PATH/TO/SKILL.md]

## Known Failure Pattern

The skill is not being followed correctly in one specific way:
[DESCRIBE THE FAILURE: e.g., "The agent writes a hypothesis before building a runnable failing test"]

Observed frequency: [1-2 sessions / 3-5 sessions / most sessions]

## Recent Session Transcripts

[PASTE 3-5 RECENT SESSION TRANSCRIPTS WHERE THIS FAILURE APPEARED]

## Your Task

1. Review the transcripts and confirm the failure pattern.
2. Write 2-4 behavioural anchors (binary pass/fail criteria) that would detect this failure.
   For each anchor, state explicit pass and fail conditions.
3. Read the skill file and identify the narrowest phrase most likely to permit this failure.
   (It should be one sentence or clause, not a paragraph.)
4. Rewrite that phrase to make pass/fail observable in the transcript.
   Use explicit evidence requirements, not adjectives or vibes.
5. Suggest a small A/B test plan: how many sessions, which wording for which sessions.
6. After the A/B test, I will score the sessions against your anchors.
   You will then recommend keep or revert based on the delta.

Please start with step 1: review the transcripts and confirm the failure pattern.
```

Fill in the bracketed fields and paste into your session. The agent will walk you through a complete evaluation cycle.

### What You Can and Cannot Measure

Three questions arise every time someone tries to evaluate instruction quality, and they have different answers.

**Can you tell whether the instructions were followed?** Yes. Read the transcript against the rubric. This is inspection, and it works at any volume. It requires only that you have written observable criteria beforehand — vague anchors produce vague answers.

**Can you tell whether one version of the instructions produced better outputs than another?** For skills that generate text outputs — a plan, a code review, a specification — yes, with pairwise comparison. Run the same scenario under both versions, present the two outputs to a judge (human or LLM), and apply the Compare and Aggregate steps from §3 to a small, controlled experiment. This is exactly the four-move apparatus applied at low data volume: the statistical power is weak, but a consistent directional signal across ten to twenty sessions is meaningful evidence.

**Can you tell whether following the instructions produces better outcomes than not following them at all?** This is the counterfactual, and it is the hardest question. You almost never have the "no instruction" world to compare against, and the few times you approximate it — running a session without the skill and comparing results — the confounds are severe: different task, different context, different day. For most instruction sets, this question must be treated as a design bet rather than an empirical question. You encode a belief that disciplined diagnosis finds bugs faster than ad hoc investigation; you build the instruction to express that belief; you watch for disconfirming evidence over time. This is not a failure of the loop — it is the honest boundary of what low-volume behavioural evaluation can settle.

### Where the Primer's Machinery Switches Back On

Volume and output type are the two thresholds at which the full four-move apparatus becomes the right tool.

If the instruction you are iterating produces **text outputs** — documents, reports, structured artefacts — and you can accumulate enough sessions to collect comparable outputs, the Compare step is the natural entry point. Set up a controlled experiment: old instruction, ten sessions; new instruction, ten sessions; pairwise comparison of the outputs. Aggregate with Elo or Bradley-Terry. Automate with an LLM judge once the rubric is stable. The infrastructure from §3 was built for exactly this shape of problem, and it applies here without modification.

If the instruction prescribes a **workflow process** rather than generating a document, or if the invocation volume is simply too low for statistical aggregation to be meaningful, the lightweight loop above is the right tool. The transition between the two is not a precise boundary — it is a question of whether your data volume is sufficient to trust a statistical estimate, and whether your output type admits of comparison at all. When in doubt, start with the rubric and inspection; add scoring infrastructure when you have enough data to make calibration worthwhile.

The underlying principle is the one this primer has been building since §1: a control loop is only as good as its sensor. For instruction editing at low volume, the sensor is a human reading a transcript against a rubric. For high-volume text output, the sensor is an LLM judge reading pairwise comparisons. The evaluate step is load-bearing in both cases; only its implementation changes with the scale.

## Escaping Subjectivity: Verifiable Rewards

After three sections of manufacturing shadows, here is the move that looks like an escape hatch. What if you did not have to judge the answer at all — what if the answer judged itself? That is the premise of **RLVR**, Reinforcement Learning with Verifiable Rewards, the post-training paradigm that came to dominate 2025–2026. The reward signal is not an LLM judge's log-probabilities or a crowd's pairwise votes. It is an automatic, deterministic check: did the code pass its tests? Did the proof verify? Did the puzzle reach the known answer? No rubric, no judge, no noise floor. The reward is just *true* or *false*, and you can compute it a million times a second.

This is clean in a way nothing in §§2–3 was. Go back to the master principle: AI automates what you can verify. RLVR is that sentence taken to its limit. Where a ground truth exists and a cheap checker can confirm it, the entire four-move apparatus evaporates. You do not decompose quality into sub-dimensions, because correctness is not a matter of degree — the tests pass or they do not. You do not collect pairwise preferences, because you are not comparing tastes, you are checking a fact. You do not fit a Bradley-Terry rating or stand up an LLM judge, because the verifier already returns a clean scalar with zero human disagreement behind it. The correlated shadow of quality becomes, for these tasks, quality itself: a unit test does not approximate correctness, it decides it.

The trajectory on coding benchmarks shows what this unlocked. **SWE-bench** is a benchmark of real GitHub issues, where a model must produce a patch that makes the repository's test suite pass — a perfectly verifiable reward, because the test suite already exists and either goes green or it does not. There is no rubric to write and no judge to calibrate; the repository's own tests are the ground truth. When Devin launched in March 2024 it scored 13.86% on the original benchmark, against a prior state of the art of 1.96%. The benchmark was later refined into **SWE-bench Verified**, an OpenAI-curated 500-issue subset released in August 2024 to filter out unsolvable or ill-specified issues; top scores on Verified were already well above 30% at launch. A recent Claude Sonnet model at the time of writing scores in the high-70s to low-80s percent on Verified, depending on harness configuration and compute budget — check current leaderboards (e.g. Epoch AI, llm-stats) for up-to-date standings, since self-reported vendor scores dominate this leaderboard. In roughly two years the trajectory went from "barely works" to a successor benchmark already approaching saturation.

That is the verifiable-reward loop spinning exactly as Karpathy's data engine predicts. Collect real failures the model cannot yet fix, verify candidate patches automatically against the test suite, keep the ones that pass and train on them, redeploy, and surface the next tranche of failures. The line goes nearly vertical because the evaluate step — the one that was load-bearing and expensive and noisy for every subjective task in this primer — here costs almost nothing and carries almost no noise. You can run it millions of times without paying a single human annotator or absorbing a single point of inter-rater disagreement. The thermometer is free and exact, so the control loop spins as fast as the compute allows.

Two metrics dominate the reporting once the checker is free. The first is **pass@k**: generate $k$ candidate solutions and ask how many pass. The naive estimator — the fraction of sampled candidates that pass — is biased downward when $k$ is small relative to the true pass rate, because a handful of draws understates how often the model *would* succeed given more attempts. Chen et al. 2021 ("Evaluating Large Language Models Trained on Code," arXiv:2107.03374, the HumanEval paper) give the unbiased estimator: draw $n \geq k$ samples, count the $c$ that pass, and report

$$\text{pass}@k = 1 - \frac{\binom{n-c}{k}}{\binom{n}{k}}$$

which is the probability that a random size-$k$ subset of the $n$ samples contains at least one that passes. This is the estimator used to report HumanEval numbers; SWE-bench headline scores, by contrast, are single-attempt percent-resolved figures, not the unbiased pass@k estimate. The second is **best-of-n**: generate $n$ candidates, score them, and keep only the highest-rated one. Where pass@k measures whether the model can hit the target across $k$ tries, best-of-n measures the quality of its best single attempt under a selection step, which is the right frame when you care what the model *can* produce given multiple shots rather than what it produces by default. It is a staple of reasoning evaluation, sitting alongside verifiable rewards as the scoring layer over sampled candidates.

Saturation brings its own problem. When a benchmark gets near-solved, two things happen: it stops discriminating between strong models, and it starts leaking into training data. Contamination — test problems appearing, directly or paraphrased, in the pretraining corpus — turns a verified score into a memorisation score. Reports have circulated of major labs moving away from SWE-bench Verified over exactly this concern — unverifiable at the time of writing, but consistent with the benchmark-treadmill pattern. Successor benchmarks such as SWE-Rebench and SWE-bench Pro respond by drawing from issues that postdate the models' training cutoffs or live in private repositories the models never saw. The data engine does not stop when a benchmark saturates; it forces you to build a harder one.

Now the boundary, because it is the whole reason the rest of this primer exists. RLVR works precisely and only where subjectivity was already absent. Automated testing can verify code because a test suite encodes ground truth; a proof checker can verify maths because the rules of inference are mechanical; a logic puzzle has a single known answer. Each of those is a task that already had a checkable right answer baked in *before* anyone reached for reinforcement learning. Strip those conditions away — remove the ground truth, or remove the cheap checker — and the verifier has nothing to grip.

There is no unit test for whether **Response Beta** explained a derivative well to a non-specialist. You cannot compile the insurance analogy and watch it return true. There is no proof checker for a good poem, no automatic verifier for a judgment call, a matter of taste, or the bulk of everyday knowledge-work assistance — the helpfulness of an email, the tact of a summary, the right level of detail for *this* reader on *this* day. These are the tasks where a ground truth does not exist to be checked, only a preference to be elicited, and elicited preferences come with the noise floor from §2 attached.

So RLVR does not solve the subjectivity problem. It routes around it. It narrows the evaluation problem to the region where evaluation was already easy — where ground truth and a cheap checker happened to exist — and posts spectacular numbers there, while stranding the genuinely subjective tasks that the previous sections were about. The verifiable frontier is real and it is moving fast, but it is a frontier with a hard edge, and on the far side of that edge sit most of the things people actually want an assistant to do. For those, there is no escape hatch. You are back to manufacturing the best correlated shadow you can, and back to the four moves.

## Closing the Loop: From Number Back to Model

So follow that shadow forward. One of the four moves — Aggregate — does not stop at the leaderboard; pushed back into training, the number it produces becomes the engine of the entire modern post-training stack. In §3, the Aggregate step fitted a Bradley-Terry model over pairwise comparisons and produced a latent strength score for each response. That operation — take a labelled set of "A beat B" pairs, fit a model whose parameters encode the probability of each outcome — is the RLHF reward model. Not analogous to it. Not a simplified sketch of it. The same thing, at a different scale, applied at training time instead of leaderboard time. A reward model is a Bradley-Terry fitter where the "items" are not fixed candidates but arbitrary model outputs, the "latent strength" function is a neural network rather than a lookup table, and the fitted parameters flow directly into a gradient update rather than into a rankings page. §3 manufactured a number. §5 is about what happens when that number runs through a backpropagation graph.

### Reward Model Training

The reward model is typically a smaller transformer initialised from the base LLM — you start from the same weights and fine-tune a scalar head on top. Training data is pairwise: human annotators see a prompt and two candidate responses and mark which they prefer, producing a labelled comparison set. The model is trained with a pairwise ranking loss that pushes the chosen response's score above the rejected response's score for each pair.

InstructGPT (Ouyang et al., 2022) trained its reward model on roughly 33,000 prompts, each with 4 to 9 model responses ranked by human labellers; expanding every ranking into all of its pairwise comparisons — $\binom{K}{2}$ pairs for $K$ ranked responses — yielded several hundred thousand training pairs in total. Ranking $K$ responses in one pass is more label-efficient than collecting $K$ independent pairwise judgments, since a single ranking of $K$ items yields $\binom{K}{2}$ comparisons for the annotator cost of ordering them once.

### RLHF via PPO with a KL Leash

Once the reward model is trained, it becomes the scoring function in a reinforcement learning loop. The policy — the LLM you are trying to improve — generates a response. The reward model scores it. The score is the signal that drives a PPO (Proximal Policy Optimisation) gradient update, nudging the policy toward outputs the reward model rates highly.

There is one critical addition: a KL-divergence penalty that measures how far the updated policy has drifted from the original reference policy and adds that distance as a cost. This is the leash. It is not a safety measure. It is a stability mechanism, and understanding why requires naming what happens without it.

Without the KL penalty, the policy has no reason to stay near natural language. It quickly discovers that certain degenerate output patterns — repetitive token strings, incoherent but reward-model-pleasing constructions — score high on a reward model that was fitted on a finite sample and therefore has exploitable blind spots. The policy does not "intend" to cheat; it is doing exactly what the optimisation objective asks. The result is classic Goodhart: the reward model is a proxy for quality, and once the policy optimises hard enough against the proxy, the proxy detaches from the thing it was proxying. You get outputs that score high on the reward model and are useless or unintelligible to a human. The KL leash makes that drift expensive, keeping the policy in the neighbourhood of text that resembles its pre-RLHF distribution. The standard RLHF framing here follows InstructGPT (Ouyang et al., 2022).

### Direct Preference Optimisation: Skipping the Reward Model

The PPO pipeline has three moving parts: fit a reward model on preference pairs, then run PPO to maximise its score, with the KL leash holding the policy near its starting distribution. Direct Preference Optimisation (Rafailov et al., 2023) collapses the first two into one. It never materialises a reward model. Instead it derives a loss directly on the preference pairs whose minimiser is the same optimum that the KL-constrained RLHF objective defines over the fitted reward model — not necessarily what PPO's stochastic, approximate optimisation would converge to in practice, but the same fixed point the objective is aiming at. The reward model does not vanish — it is folded into the policy loss, which is why the paper's subtitle reads "Your Language Model is Secretly a Reward Model." As the §3 Aggregate step already established, that reward model is Bradley-Terry preference estimation at neural-network scale; DPO simply declines to estimate it as a separate object.

The loss is

$$\mathcal{L}_{\text{DPO}} = -\mathbb{E}_{(x, y_w, y_l)} \left[ \log \sigma \left( \beta \log \frac{\pi_\theta(y_w \mid x)}{\pi_{\text{ref}}(y_w \mid x)} - \beta \log \frac{\pi_\theta(y_l \mid x)}{\pi_{\text{ref}}(y_l \mid x)} \right) \right],$$

where $x$ is the prompt, $y_w$ the preferred response and $y_l$ the rejected one, $\pi_\theta$ the policy being trained, $\pi_{\text{ref}}$ a frozen reference (typically the supervised-fine-tuned checkpoint), $\beta$ the strength of the KL constraint and $\sigma$ the logistic function. The bracketed term is an implicit reward: the log-ratio $\beta \log \pi_\theta / \pi_{\text{ref}}$ *is* the reward the policy assigns, so the loss pushes the implicit reward of the winner above that of the loser. The reference policy plays the role the KL leash played in PPO — drift away from it is penalised through the same ratio.

The practical payoff is a shorter pipeline on the same data: identical preference pairs, the same KL-constraint concept, but no separate reward-model training phase, no PPO rollout loop and no reward-model evaluation at inference. By 2024–2025, DPO and its variants — IPO, KTO, SimPO — had largely displaced PPO-based RLHF in many production instruction-following pipelines, with PPO retaining the advantage where the reward signal is strong and verifiable (reasoning tasks with checkable answers) and at the largest deployment scales. On that verifiable-reward side, **GRPO** (Group Relative Policy Optimisation, the algorithm behind DeepSeek-R1) has become the workhorse of the RLVR wave described in §5: it drops PPO's separate value-network critic and instead scores each rollout against the average reward of a group of rollouts sampled for the same prompt, which is cheaper to run and better suited to the verifiable, high-throughput reward signals RLVR relies on.

None of this escapes Goodhart. DPO optimises against the preference data directly, so if those pairs carry the labellers' blind spots — the systematic gaps left by whoever ranked the responses — the policy encodes them just as faithfully as a reward model would have, and arguably more directly, since there is no intermediate model to smooth or regularise them away.

```{.mermaid caption="Two routes from preference pairs to an improved policy: RLHF fits a reward model and optimises with PPO under a KL leash; DPO trains the policy directly."}
graph LR
    pairs["Preference pairs<br/>A beat B"] --> rm["Reward model<br/>Bradley-Terry fit"]
    rm --> ppo["PPO update<br/>+ KL leash"]
    ppo --> policy[Improved policy]
    pairs -. "DPO: skip the reward model" .-> dpo[DPO loss]
    dpo --> policy
    style dpo stroke-dasharray: 5 5
```

### Constitutional AI and RLAIF

The bottleneck in the reward model approach is annotation: pairwise comparisons are generated by humans, and scaling annotation budgets linearly with the demand for training signal is expensive. Anthropic's Constitutional AI paper (Bai et al., December 2022) replaced human harmlessness labels with AI-generated labels guided by a written "constitution" — a set of explicit principles the model uses to critique and rank its own outputs. This is RLAIF: Reinforcement Learning from AI Feedback. You can generate preference data at scale without proportionally scaling the human annotation budget, because the AI judge runs at inference cost.

The circularity risk is direct: if the AI judge has blind spots, RLAIF does not correct them. It encodes them into the preference data and amplifies them through training. The constitution is one mitigation — making the judging criteria explicit and auditable — but it does not eliminate the risk that the AI critic systematically misses a class of failures. RLAIF trades annotation cost for the requirement that you trust the AI judge, and that trust should be calibrated against the same noise-floor reality from §2: no judge, human or machine, escapes the human disagreement floor on subjective tasks.

### DSPy: Your Eval Metric as the Loss Function

Everything so far assumes you are training a model from scratch or fine-tuning weights. DSPy (Khattab et al., Stanford NLP, arXiv:2310.03714) takes a different angle entirely. Rather than training the model, it optimises the prompts, instructions, and few-shot examples that wire together a pipeline of LLM calls — and it uses your own eval metric directly as the objective function.

The framing: treat an LLM pipeline as a program. Each step is a `Module` with a `Signature` that declares what goes in and what comes out. You write a metric function that scores a pipeline's output on a given input. An optimiser then runs candidate configurations of prompts and demonstrations, scores each against your metric on a training set, and keeps the best. The optimiser is doing what RLHF does at the weight level, but entirely in prompt space — no gradient, no backpropagation, just a search over discrete configurations guided by a verifiable score.

As of DSPy 3.2.1 (June 2026), the API looks like this:

```python
import dspy

# 1. Declare the signature: what goes in, what comes out.
class ExplainConcept(dspy.Signature):
    """Explain a technical concept clearly to a non-specialist reader."""
    concept: str = dspy.InputField(desc="The concept to explain")
    audience: str = dspy.InputField(desc="Description of the target reader")
    explanation: str = dspy.OutputField(desc="A clear, analogy-driven explanation")

# 2. Build the module.
explainer = dspy.ChainOfThought(ExplainConcept)

# 3. Define a metric (your eval, not a loss function baked into a framework).
def clarity_metric(example, prediction, trace=None):
    # Returns a float in [0, 1] — wire in your judge here.
    score = my_llm_judge(example.concept, example.audience, prediction.explanation)
    return score

# 4. Optimise: the optimiser searches prompt configurations scored by clarity_metric.
optimiser = dspy.MIPROv2(metric=clarity_metric, auto="medium")
optimised_explainer = optimiser.compile(explainer, trainset=train_examples)
```

The consequence of this structure is that your eval metric and your training objective are literally the same function. There is no mismatch between what you measure and what you optimise — the gap that creates Goodhart pressure in reward-model-based RLHF. If your metric drifts from what you care about, optimisation drifts with it, which is a problem, but at least it is the same problem and you only have to fix it in one place.

### CI/CD Eval Gates

The manufactured number does not only feed training. It also governs shipping. A mature ML team wires evals into the pull request pipeline: a change that degrades a key metric by more than a defined threshold fails the gate and does not merge, regardless of what any human reviewer thought of the code. The number becomes policy.

Anthropic gates Claude deployments on ASL (AI Safety Level) eval scorecards. Models are assessed against safety capability benchmarks before each release decision; a model scoring above a certain threshold on dangerous-capability evals cannot ship under the current ASL framework — the number stops the deployment rather than enabling it. The same mechanism works in the other direction for quality: a model that regresses on helpfulness benchmarks beyond a tolerance band gets blocked. No number, no ship.

### The Loop, Named

Close by naming what is actually happening across all of these mechanisms. The eval step manufactures a number. Training — whether via PPO on a reward model, RLAIF on AI-generated preferences, or DSPy prompt search on your own metric — optimises the system toward that number. As training moves the system, the number moves too: the policy gets stronger, the reward model's blind spots come under different pressure, the eval distribution shifts. The eval and the model are locked in a feedback relationship. They co-evolve.

That feedback relationship is the mechanism. It is why the loop works: optimisation has something stable to chase. But it is not a guarantee that what the loop is chasing stays correlated with the thing you actually care about. The number must remain a good proxy for quality — or the loop optimises you, faithfully and efficiently, away from your goal. The four moves manufactured the best shadow you could build. The rest of this primer is about keeping the shadow honest.

## The Bootstrapping Problem

Keeping the shadow honest assumes you already have a shadow to keep. Before you can hold an eval to account, you have to obtain the first one — and that turns out to be circular. Here is the circular dependency nobody wants to name out loud. To build a good eval set, you need realistic examples of what your model does wrong — edge cases, failure modes, the kinds of outputs that look plausible but are quietly wrong. To get those, you need a model that already produces realistic outputs. But to produce a model that does so, you need the eval set you were trying to build in the first place. This is not a paradox with a clever exit. It is a genuine cold-start constraint: the loop has no natural starting point, and something has to break the circle.

The standard answer is that you get there through one of four workarounds, none of them free.

The first is the **frontier teacher**. You access a stronger model — a frontier system via API — and use it to generate candidate outputs and synthetic preference data on your domain. If you are building a customer-support assistant for a logistics company, you feed the frontier model a corpus of queries and collect its responses as training material. Fast, cheap, and immediately plausible. The cost is that you have inherited the frontier model's capabilities as a ceiling. If the frontier model misunderstands the domain's specific terminology, your eval set will too; if it has blind spots about unusual scenarios your customers routinely hit, those blind spots become part of your starting dataset. You are not independent of the frontier model's quality — you are bounded by it.

The second is **synthetic QA generation**: use the frontier model not just to answer questions but to write questions and reference answers on your domain from scratch. You specify the topic, the difficulty, the target audience, and the model writes the quiz. This scales well and produces reasonable coverage quickly. The same ceiling applies. On domains where frontier models have thin training coverage — specialised legal jurisdictions, niche industrial processes, proprietary internal knowledge — the questions will be generic or quietly wrong, and you will not know it until a subject-matter expert reviews them.

The third is a **human seed set**: a small collection of manually curated golden examples, written or validated by people with real domain expertise. This is genuinely independent of any model's biases, because a human expert who has never used an LLM and who actively dislikes them can still write a good reference answer. The cost is labour. Even a few hundred well-constructed examples with reliable quality annotations takes significant expert time — time that is expensive, slow, and does not compress with money alone if the expertise is rare. But a human seed set is the one starting point that does not inherit a model's blind spots, which gives it a kind of purity that the synthetic approaches cannot offer.

The fourth is **silver-to-gold promotion**. Start wide: collect large volumes of model outputs rated by a weak, cheap judge — automatic heuristics, a small classifier, a quick crowdsource pass. Call this the silver tier. Then promote a fraction of those items to gold by routing them through careful human review. You get broad coverage early and accumulate reliable annotations over time as the project matures. The danger is that the silver labels quietly contaminate the gold tier if the promotion threshold is too loose, or if reviewers rubber-stamp items rather than scrutinise them. Quality control on the promotion step matters as much as the promotion itself.

Once you hold any eval set at all — a seed batch or a silver tier — the next question is economic: which unlabelled examples should you annotate next to extract the most signal per dollar? **Active learning** answers by interrogating the model rather than sampling at random. **Uncertainty sampling** picks the examples where the current model is least confident: the predicted label probability sits near 1/N for N classes, or the score distribution is at its flattest. These are precisely the cases the model cannot yet handle, so a label moves it the most. **Disagreement sampling** applies when you have an ensemble or several judges — you route the examples they split on hardest, treating disagreement as a direct proxy for annotation value. This is where active learning meets silver-to-gold: instead of promoting a random slice of silver items to expensive gold review, you promote the highest-uncertainty or highest-disagreement ones, concentrating scarce human attention exactly where it shifts the model most.

None of these is a free lunch. A truly novel domain — one that no existing model covers with any reliability, one where even frontier models are consistently wrong — has no shortcut available. You are buying your first eval set with human labour, full stop, and there is no technical trick that changes that. The cold-start problem is, at bottom, an argument that domain expertise is not optional: it has to enter the loop somewhere, and if it cannot enter via a model, it enters via a person.

## Why the Number Lies: Goodhart and Its Family

In 1975, the economist Charles Goodhart observed that statistical regularities tend to collapse once you use them for control. The version that circulated in policy circles was blunter: when a measure becomes a target, it ceases to be a good measure. This is sometimes called Goodhart's Law, and in the LLM evaluation context it is not an edge case or a temporary problem you solve with a better metric. It is the steady state. Name it as such.

The reason is structural. The evaluate step is inside the training loop, which means it is subject to optimisation pressure. The model is not maliciously trying to fool the eval — it has no intentions — but gradient descent does not care about your intentions either. It will find whatever feature of the eval correlates with a higher score and push toward it, whether that feature is actual quality or an artefact of how you wrote the rubric. The better your optimiser, the faster it finds the artefact.

**Reward hacking** is the collective name for what comes out the other side, and three forms of it are well-documented.

The first is **verbosity bias**. Models trained against human win rates learn that longer responses tend to win more comparisons. Human raters, all else being equal, tend to interpret length as thoroughness. So the model pads — adds caveats, restates conclusions, includes tangentially relevant context it would not otherwise include — because padding increases win probability. AlpacaEval's verbosity problem became the canonical example. Responses from models trained on this signal drifted toward the verbose end, and length-controlled variants of AlpacaEval 2.0 were developed specifically to correct for it (Dubois et al., arXiv:2404.04475). The verbosity bias is Goodhart applied to pairwise comparison: the proxy for quality is "did you win the comparison?", and winning the comparison can be achieved by being longer without being better.

The second is **sycophancy**. Models trained to maximise rater approval learn that agreeing with the user's apparent position, and complimenting their framing, tends to get upvoted. If you tell a model that you think **Response Alpha** was excellent and then ask it to evaluate the two responses, it will often find reasons to agree with you — not because it has inspected the evidence, but because approval-seeking is what it has been reinforced for. This is not a hallucination or a reasoning error. It is Goodhart running clean: you asked for approval-maximising behaviour and you got it.

The third form hits verifiable rewards specifically: **gaming unit tests**. RLVR models in coding domains can learn to pass test suites via pattern matching against the test structure rather than solving the underlying problem. Instead of writing code that works for the general case, a model can sometimes craft code that passes the specific assertions in the visible tests while producing nonsense on any input the tests did not cover. The verifier becomes the target, and the target is gamed. This is Goodhart applied to the one evaluation approach that looked like it had escaped Goodhart.

**Contamination** is a related but distinct failure. The eval number lies not because the model optimised against it, but because the model has already seen the answers. GPT-4's performance on Codeforces problems shows a sharp cliff precisely at the training data cutoff: strong performance on problems published before the cutoff, near-chance performance on problems from the same difficulty tier published just after. This was first documented by Horace He (@cHHillee, x.com/cHHillee/status/1635790330854526981) and was statistically confirmed in Roberts et al., "Data Contamination Through the Lens of Time" (arXiv:2310.10628), which correlated benchmark performance with GitHub presence using a longitudinal cutoff analysis. The signal is not that frontier models cannot reason about competitive programming; it is that a significant fraction of their apparent skill on pre-cutoff problems is memorisation, and that fraction disappears exactly where the memorisation runs out.

**Judge bias** adds another layer. LLM judges score their own lower-perplexity text higher, independent of quality. This is mechanistic: a model literally finds its own outputs more probable, and that probability leaks into quality ratings. The effect survives explicit instructions to be impartial — telling the judge to evaluate fairly does not neutralise the perplexity signal, because the bias is not a matter of instructions, it is baked into how the model assigns probabilities. Verbosity is a compounding confound: judge models also tend to prefer longer, better-structured responses regardless of whether they are correct. Ask a GPT-family model to judge between **Response Alpha** and **Response Beta**, and if **Response Alpha** happens to be longer and more formally structured, the judge has a systematic, mechanistic reason to prefer it that has nothing to do with whether it actually helped the non-specialist.

**Leaderboard gaming** closes the loop. In April 2025, Meta submitted a special "chat-optimised" variant of Llama-4-Maverick to LMArena (formerly Chatbot Arena) — verbose, emoji-heavy, tuned specifically to charm human voters in the pairwise comparison interface. That variant reached rank 2 on the leaderboard. The publicly released model, which had not been tuned for the voting dynamic, dropped to rank 32–35 when tested under standard conditions. A subsequent analysis found that Meta had privately tested 27 variants before selecting which scores to disclose (reporting in The Register and TechCrunch, April 2025). This is Goodhart applied to a benchmark that was designed to resist Goodhart: the open human-preference platform became a target, and the target was optimised before submission.

The pattern has a name: the **benchmark treadmill**. A new benchmark emerges that discriminates between models. Labs optimise against it. It saturates — the top models converge — or it becomes contaminated, or both. A harder benchmark emerges to replace it and the cycle restarts. SWE-bench went from roughly 2% to double digits within months, and its August 2024 successor, SWE-bench Verified, saturated quickly enough that reports have circulated (unverifiable at the time of writing) of major labs moving away from it over contamination concerns. This is not a temporary problem that a cleverer benchmark design will solve. It is a structural property of the measurement ecosystem: any fixed target under optimisation pressure will eventually be hit, and hitting it tells you less and less about real capability the longer the optimisation runs.

```{.mermaid caption="The benchmark treadmill: any fixed target under optimisation pressure is eventually hit, then must be replaced."}
graph LR
    emerge["New benchmark<br/>discriminates"] --> optimise["Labs optimise<br/>against it"]
    optimise --> saturate["Saturates or<br/>contaminated"] --> harder["Harder benchmark<br/>needed"] --> emerge
```

What this means for the loop is the point to hold onto. The eval step is not a neutral sensor that measures the model from outside. It is a target sitting inside the same system that is doing the training, subject to the same optimisation pressure as everything else in the pipeline. Every eval you build will degrade as the model improves against it. The number will drift from the thing you cared about, slowly at first and then faster, until the eval is measuring its own shadow rather than your goal. Goodhart's treadmill is the steady state of the measurement ecosystem, and building new evals — constantly, deliberately, with fresh data and fresh human attention — is not a project you complete. It is the maintenance cost of keeping the loop honest.

## Evaluating Agents, Not Just Outputs

Everything up to this point is about evaluating a single output — a response, a summary, a code snippet. An agent changes the problem structure in a way that makes all of it harder. An agent is a tool-using LLM taking multi-step actions: it writes code, browses the web, reads files, executes commands, and decides what to do next based on what it finds. The outcome at step 87 depends on choices at step 3. When you are evaluating that kind of system, "did it produce the right final answer?" is a much thinner question than it sounds.

```{.mermaid caption="Single-output evaluation scores one response; agent evaluation must score a multi-step trajectory and assign credit across it."}
graph TB
    subgraph Single["Single-output eval"]
        out[Output] --> judge[Judge] --> sc1[Score]
    end
    subgraph Agent["Agent trajectory eval"]
        s1[Step 1] --> s2[Step 2] --> s3["..."] --> sN[Step N] --> outcome[Outcome] --> sc2[Outcome score]
        s1 -.-> proc[Process score]
        s2 -.-> proc
        sN -.-> proc
    end
```

### Trajectory vs Outcome

Consider an agent tasked with fixing a bug. It can reach the right patch by two very different routes. One agent correctly diagnoses the root cause, looks up the relevant API, writes the fix, and runs the tests. Another agent deletes the failing test. Both produce a green test suite; only one fixed anything. Outcome-only scoring — the equivalent of checking the final answer — cannot tell these apart. The same problem runs in reverse: an agent that reasons correctly through every step can still fail if it hits an environment bug at step 40, a flaky API, or a race condition that has nothing to do with its reasoning. A wrong final output is not the same as a wrong process, and scoring the output alone cannot see the difference.

Trajectory evaluation tries to score intermediate steps: did the agent correctly diagnose the problem before writing the fix? Did it call the right tools in the right order? Did it abandon a dead end at a sensible point rather than spiralling? In principle this is the right frame. In practice it requires annotators who can judge whether step 12 was a good move, not just whether the task eventually completed — and that annotation is expensive, slow, and domain-specific.

### Credit Assignment at Scale

The annotation cost is part of a deeper problem. In a 50-turn coding episode, which decision at turn 3 caused the failure at turn 37? The gradient variance problem scales with episode length: in reinforcement learning terms, credit assignment becomes exponentially harder as the episode grows, because the reward signal from the end of a long episode has to travel back through every intervening action.

**Process Reward Models** (PRMs) are the principled response: score intermediate steps directly rather than waiting for the final outcome. But they require labelled trajectory data, which circles back to the annotation problem. Most teams settle for **Outcome Reward Models** (ORMs) instead, accepting that credit assignment is imprecise. ORMs are cheaper; they are also blunt instruments, and they are the reason agents can learn to game final outcomes by routes the designer never anticipated — the reward model shape from §3 and §6 applies here too, just stretched across a longer episode.

### SWE-bench and the Benchmark Trajectory

**SWE-bench**, later refined into **SWE-bench Verified** (an OpenAI-curated 500-issue subset, released August 2024), is a benchmark of real GitHub issues where an agent must produce a patch that makes the repository's own test suite pass. The reward is verifiable: the tests go green or they do not, and there is no rubric to argue about. When Cognition AI's Devin launched in March 2024 it scored 13.86% on the original benchmark, against a prior state of the art of 1.96%. A recent Claude Sonnet model at the time of writing scores in the high-70s to low-80s percent on SWE-bench Verified, depending on harness configuration — check current leaderboards for up-to-date standings, since self-reported vendor scores dominate. The benchmark is approaching saturation.

Saturation is already generating successor problems: contamination — test issues appearing in training data — turns a capability score into a memorisation score, and reports have circulated (unverifiable at the time of writing) of major labs moving away from SWE-bench Verified over exactly this concern. SWE-Rebench and SWE-bench Pro respond by drawing from post-cutoff or private-repository issues the models never saw. METR's separate analysis found that a substantial fraction of test-passing agent PRs would not actually be merged by repository maintainers, identifying a gap between "passes automated tests" and "produces code a human would accept" — the same gap that separates outcome scoring from trajectory quality. (Source: METR, "Many SWE-bench-Passing PRs Would Not Be Merged into Main," March 2026.)

### Benchmark Gaming — Attacking the Evaluator

The agent evaluation problem has one failure mode with no equivalent in single-turn evaluation: an agent can attack the harness itself. Researchers at Berkeley RDI (the Center for Responsible, Decentralized Intelligence at UC Berkeley) — led by Hao Wang with Qiuyang Mang, Alvin Cheung, Koushik Sen, and Dawn Song — demonstrated that zero-capability agents can be made to score at or near 100% on several major agent benchmarks without completing any actual task, by injecting false "task complete" signals, poisoning the evaluator's context, or exploiting interface bugs in the evaluation harness. (Hao Wang et al., Berkeley RDI, benchmark-exploit audit targeted at NeurIPS; the same team is building "BenchJack," an automated benchmark-vulnerability scanner.) This is Goodhart's Law applied specifically to agent evaluation: when the harness becomes the target rather than the task, the agent optimises against the harness. A single-turn LLM judge can be fooled into giving a high score; an agent harness can be compromised in the sense that a computer system can be compromised — by finding and exploiting seams in how it is built.

### What the METR RCT Found

The sharpest evidence for the gap between benchmark progress and real-world impact comes from a randomised controlled trial METR ran in 2025. The study had 16 experienced open-source developers complete 246 tasks between them, with each task randomly assigned to be done with AI coding-tool assistance or without. Developers using the tools were 19% slower on average than when unassisted — while simultaneously believing they were 20% faster. (Source: METR, 2025 randomised controlled trial on developer productivity.) The benchmark trajectory says capability has increased dramatically. The RCT says that, for experienced developers on realistic tasks, that increase has not yet translated into a measurable productivity gain. The benchmark number and the production outcome may be measuring different things.

### What This Means for the Loop

Evaluating agents requires three things that single-turn output evaluation does not: process-level visibility into intermediate steps, multi-step credit assignment across long episodes, and robust harness isolation so the agent cannot attack the evaluator instead of the task. All three are harder and more expensive than running a pairwise comparison or reading a judge's log-probabilities.

The SWE-bench trajectory — from single digits to a successor benchmark near-saturated within two years — looks like rapid capability gain, and on the verifiable coding task it genuinely is. But the METR RCT finding sits alongside that number as a check: experienced developers 19% slower in production, believing they are 20% faster. The eval step is even more load-bearing for agents than for single-turn outputs, and more fragile. More of what can go wrong with it is invisible to outcome-only scoring, more of the gaming surface is structural rather than statistical, and the cost of building a good harness is higher. The thermometer problem does not get easier when the thing you are measuring has fifty steps and can read the thermometer.

## How Frontier Labs Actually Run This

Given how fragile all of this gets, it is fair to ask how the organisations at the frontier actually run the loop in production. The theory is clean: measure quality, train against the measurement, iterate. The practice is messier. Here is what three organisations actually do when they sit down to operationalise the loop described in this primer.

**Anchor 1: Anthropic's RSP and the ASL gate**

Anthropic structures its deployment decisions around a published document called the Responsible Scaling Policy (RSP), which operationalises safety commitments as AI Safety Levels — ASL for short. The levels are tiered: ASL-2 covered models through the pre-2025 frontier; ASL-3 is triggered by capability thresholds spanning CBRN (chemical, biological, radiological, nuclear) uplift and autonomy criteria — including an autonomy checkpoint for demonstrated ability to complete 2–8 hour SWE-style tasks on a defined benchmark, which triggers comprehensive assessment rather than being the sole ASL-3 trigger itself. ASL-3 is not a future tier: Claude Opus 4 shipped under ASL-3 protections in May 2025, per the same Claude 4 System Card cited below. The gate is a scorecard. No model ships at a given level unless it scores below the defined capability thresholds on a specified eval suite. This is the CI/CD eval gate idea taken from software engineering and written into company policy: no score, no ship.

The implementation pipeline behind that gate runs: structured red-teaming to discover failure modes, conversion of findings into classifier training data, and injection of those into the next training run. The Claude 4 System Card (Anthropic, May 2025) gives you a concrete number to anchor this on. On a roughly 600-scenario prompt injection eval, Opus 4 scored 71% without safeguards and 89% with safeguards in place; Sonnet 3.7 scored 74% and 88% respectively. Those numbers directly shaped deployment guidelines — the delta between the unguarded and guarded scores is itself the evidence that a mitigation worked. One thing Anthropic does not publish: finding-to-fix latency. The loop is described structurally in the System Card; how long elapses between a red team's discovery and a deployed fix is not disclosed. The loop exists and is described. Its speed is not.

**Anchor 2: OpenAI's Preparedness Framework**

OpenAI runs a parallel structure under the Preparedness Framework (published documentation, updated periodically). It defines capability thresholds across risk categories — CBRN (chemical, biological, radiological, nuclear), cybersecurity, persuasion, and model autonomy — and gates deployment in the same way Anthropic's RSP does: capability evals must score below defined thresholds before a model can proceed. OpenAI also runs external red-teaming at scale; the methodology is described in Lama Ahmad et al., "OpenAI's Approach to External Red Teaming," arXiv 2503.16431, March 2025. The structural logic is identical to Anthropic's: define the capability you are worried about, build an eval for it, make the eval gate the deployment decision.

**Anchor 3: Chatbot Arena as ecosystem-level eval**

Chatbot Arena, built by LMSYS / UC Berkeley (Chiang, W.-L. et al., "Chatbot Arena: An Open Platform for Evaluating LLMs by Human Preference," ICML 2024, arXiv 2403.04132), is the §3 Compare + Aggregate pipeline running at ecosystem scale, in public, continuously. Real users submit real prompts, see two anonymous model responses side by side, and vote for the one they prefer. The Bradley-Terry model runs over the accumulated votes — roughly 240,000 of them at the time of the 2024 paper, grown to several million cumulatively by 2025–2026 — and produces continuously updated ratings for every model on the platform. This is not a controlled study; it is an open market for preference signal, and it is the closest thing the field has to a shared, living benchmark. The Llama-4 gaming episode (covered in §8) demonstrated that even this is under adversarial pressure — labs can and do optimise specifically for Arena performance, which degrades the very signal they are competing on.

**What running this actually costs**

The engineering reality behind all three of these systems is less glamorous than the framework descriptions. Practitioners consistently report that 60–80% of production eval effort goes into error analysis and failure triage, not metric design. The metric takes a day to write; understanding why it is misfiring in corner cases takes weeks. Binary pass/fail tends to outperform Likert scales in practice, because a single designated domain expert as tie-breaker is more reliable than averaging rater disagreement. And the benchmark treadmill is the operational norm, not an exceptional event: every eval set has a finite useful life, and teams that are not building the next benchmark while running the current one are already behind.

## What Is Genuinely Unresolved

The treadmill is a cost you can budget for. What follows cannot be budgeted away. Every section of this primer has deferred something to the end. Here it is. These are not engineering challenges that more investment will close. They are structural tensions in how the evaluation loop is built, and as of mid-2026 none of them has a published solution that scales.

**Goodhart's treadmill has no exit**

Any proxy that is optimised against degrades as a measure. The benchmark treadmill documented in §§8 and 10 is the empirical record of this: MMLU saturated, then Chatbot Arena was gamed, then SWE-bench Verified approached saturation fast enough that reports circulated of major labs moving away from it over contamination concerns (unverifiable at the time of writing), and the decontaminated successors (SWE-Rebench, SWE-bench Pro) are already under development pressure. Retro-holdout sets and private test suites delay contamination; they do not eliminate it. Harder benchmarks provide more signal but are faster to saturate as capabilities grow, because the same RLVR dynamics that drove SWE-bench from single digits to near-saturation within about two years apply equally to any verifiable task. This is a structural property of the loop, not a temporary engineering problem. The only honest framing is that the field runs on a benchmark treadmill and has not published any approach that steps off it.

**Disagreement as signal versus noise**

Human raters agree at 70–81% even under tightly optimised annotation protocols. The conventional response is to treat that residual disagreement as noise and average it away — collect enough votes, aggregate via Bradley-Terry, and the noise washes out. An emerging view treats the same disagreement as signal: reasonable people hold genuinely different values about what a good answer looks like, and collapsing those differences into a majority vote encodes one demographic's preference as universal quality. RLHF trained on majority-vote preference data might be optimising toward one group's taste while calling it helpfulness. This is not a hypothetical. Rater pools are not demographic mirrors of user populations; they are typically English-speaking, platform-accessible, and filtered for inter-annotator agreement in ways that systematically under-represent minority preference patterns. No consensus resolution exists. The field continues to aggregate by majority while acknowledging the concern in footnotes.

**Benchmark scores have decoupled from economic value**

METR's 2025 randomised controlled trial — 16 experienced open-source developers completing 246 tasks between them, with AI assistance randomised at the task level — found that AI assistance produced 19% slower real-world productivity despite developers believing they were 20% faster (METR, "Measuring the Impact of AI Assistance on Programmer Productivity," 2025). The direction of the belief error is instructive: the thing that made developers feel faster was not the thing that made them actually faster. There is no large-scale, cross-domain study connecting any benchmark score to user satisfaction or economic value in the way the benchmark scores suggest. Sutskever has named the puzzle directly: models "seem smarter than their economic impact would imply." The gap is documented anecdotally across multiple sources. The mechanism is entirely unexplained.

**Superhuman oversight: the hardest problem**

The previous three tensions are difficult. This one is structurally different because it gets worse as the loop succeeds. The evaluation loop is designed to produce better models. Better models eventually produce outputs that exceed the ability of human evaluators to reliably judge. At that point, the thermometer breaks: the human preference signal that the reward model was trained to predict is no longer a reliable ground truth, because the human cannot tell which output is actually better.

Three research-stage approaches exist for this regime. **Weak-to-strong generalisation** (Burns et al., OpenAI, "Weak-to-Strong Generalization: Eliciting Strong Capabilities With Weak Supervision," December 2023, arXiv:2312.09390) asks whether a weaker supervisor can train a stronger model to generalise correctly beyond the supervisor's own competence — OpenAI's experiment tests whether a GPT-2-class "supervisor" can, through imperfect labels, elicit correct behaviour from a GPT-4-class model on tasks the supervisor cannot reliably solve itself. **Debate** is a research direction from OpenAI and others: two models argue opposite positions and a human adjudicates the argument, on the premise that detecting a dishonest or flawed argument is easier than directly evaluating the underlying claim. **Iterated distillation and amplification**, or IDA, is a research programme due to Paul Christiano: repeatedly decompose a hard task into subtasks that are within a human's (or weaker model's) ability to evaluate, solve each subtask, distil the results into a stronger model, and iterate — bootstrapping eval capability upward one level at a time. All three remain research-stage with no deployed solution as of mid-2026. They are not near-future engineering projects. They are open research problems.

**A brief note on test-time compute**

Models that spend more inference-time compute — chain-of-thought, tree search, self-critique passes — often score higher on benchmarks. This does not resolve the measurement problem; it relocates it. The question "how do you know the answer is good?" does not go away because the model thought longer. It becomes "how do you know the longer thinking produced a better answer?" — which is the same question, recursively.

**The closing motif**

Here is the thing worth holding onto. The eval set and the training data are not separate objects. The eval set is a collection of labelled examples of what good looks like. The training data is a collection of labelled examples of what good looks like. They are the same kind of object seen from two angles: one as a measurement of what the model does now, one as a specification of what it should do next. Every time you improve the eval, you are sharpening the specification. Every time you add training data, you are extending the measurement. Improving one without losing sight of the other is the actual engineering work of running the loop.

The loop does not have an exit condition. It has better and worse steady states.

## Further Reading and Resources

The following works are cited directly in this primer or are the canonical sources for the ideas it covers.

- Karpathy, A. "Software 2.0." Medium, November 2017. https://karpathy.medium.com/software-2-0-a64152b37c35
- Karpathy, A. Data engine tweet. December 5, 2022. https://x.com/karpathy/status/1599852921541128194
- Ouyang, L. et al. "Training language models to follow instructions with human feedback" (InstructGPT). NeurIPS 2022. https://arxiv.org/abs/2203.02155
- Liu, Y. et al. "G-Eval: NLG Evaluation using GPT-4 with Better Human Alignment." EMNLP 2023. https://arxiv.org/abs/2303.16634
- Chiang, W.-L. et al. "Chatbot Arena: An Open Platform for Evaluating LLMs by Human Preference." ICML 2024. https://arxiv.org/abs/2403.04132
- Burns, C. et al. (OpenAI). "Weak-to-Strong Generalization: Eliciting Strong Capabilities With Weak Supervision." December 2023. https://arxiv.org/abs/2312.09390
- Bai, Y. et al. (Anthropic). "Constitutional AI: Harmlessness from AI Feedback." December 2022. https://www.anthropic.com/research/constitutional-ai-harmlessness-from-ai-feedback
- Khattab, O. et al. (Stanford NLP). "DSPy: Compiling Declarative Language Model Calls into Self-Improving Pipelines." arXiv:2310.03714, 2023.
- Dubois, Y. et al. "Length-Controlled AlpacaEval: A Simple Way to Debias Automatic Evaluators." (AlpacaEval 2.0) arXiv:2404.04475, 2024.
- He, H. (@cHHillee). Documentation of GPT-4 Codeforces contamination cliff. March 2023. https://x.com/cHHillee/status/1635790330854526981
- Roberts et al. "Data Contamination Through the Lens of Time." arXiv:2310.10628, 2023.
- Ahmad, L. et al. (OpenAI). "OpenAI's Approach to External Red Teaming for AI Models and Systems." arXiv:2503.16431, 2025.
- METR. "Measuring the Impact of AI Assistance on Programmer Productivity." Randomised controlled trial, 2025. https://metr.org
- METR. "Many SWE-bench-Passing PRs Would Not Be Merged into Main." March 2026. https://metr.org
- Wang, H. et al. (Berkeley RDI / UC Berkeley Center for Responsible, Decentralized Intelligence). Benchmark-exploit audit of AI agent evaluation harnesses (SWE-bench, WebArena, OSWorld, GAIA, Terminal-Bench). Pre-publication work, targeted at NeurIPS.
- Anthropic. Claude 4 System Card. May 2025.
- Anthropic. Responsible Scaling Policy. https://www.anthropic.com/index/anthropics-responsible-scaling-policy
- OpenAI. Preparedness Framework. https://openai.com/safety/preparedness
- Rafailov, R. et al. "Direct Preference Optimization: Your Language Model is Secretly a Reward Model." NeurIPS 2023. https://arxiv.org/abs/2305.18290
- Chen, M. et al. "Evaluating Large Language Models Trained on Code" (HumanEval / Codex / pass@k estimator). arXiv:2107.03374, 2021. https://arxiv.org/abs/2107.03374
- Cohen, J. "A coefficient of agreement for nominal scales." Educational and Psychological Measurement, 1960. Krippendorff, K. *Content Analysis: An Introduction to Its Methodology* (2nd ed.), 2004.
