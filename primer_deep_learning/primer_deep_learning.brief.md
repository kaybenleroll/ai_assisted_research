# Primer brief: Deep Learning and Generative AI revision

- Issue and milestone: #482; depends on #476 and its draft PR #516.
- Brief revision: `482-brief-v1`.
- Source revision: `26ae9ed25c29d09280b26efc9ebb3925439ce796`
- Historical baseline: `bda64e7666f2c228de6f12b87c9beeaa36831076`
- Reviewed revision: `26ae9ed25c29d09280b26efc9ebb3925439ce796`
- Tracked path: `primer_deep_learning/primer_deep_learning.brief.md`.
- Reader: A practitioner familiar with classical ML but new to neural networks.
- Prerequisites: Classical ML, basic matrix multiplication and derivatives.
- Problem and motivation: Connect architectural mechanisms to training, generation and practical model choice without treating them as black boxes.
- Intended outcome: Explain core computations and failure modes, follow worked calculations, and make a conditional baseline decision.
- Scope: Neural networks, optimisation, CNNs, RNNs, attention, LLMs, VAEs, GANs, diffusion, framework and model selection. Retain existing cases, code, figures, equations and links.
- Exclusions: An exhaustive formal proof of every result, a production lab notebook, frontier-model reproduction, distributed infrastructure and serving engineering.
- Proposed dependency-led route: Orientation and notation; network prediction and learning; spatial, sequential and attention architectures; LLMs; three generative families; frameworks and applied model selection.
- Approximate depth: Mathematically explicit worked foundations; advanced results are explained to their practical boundary and linked to primary sources.
- Worked examples: Existing convolution-size calculation, new forward–loss–gradient–update calculation, recurrent state trace, attention calculation, ELBO derivation, critic constraint counterexample and decision scenario.
- Real-world case: Image classification with restricted labels and deployment budget; compare a classical or simple baseline and pretrained vision models using held-out outcomes and practical constraints.
- Teaching-case contract: Conceptual and mathematical explanations use separate worked derivations appropriate to each operation; the decision scenario uses an illustrative declared dataset and metrics rather than implying measured results.
- Worked-case trace: See matrix and review proposal. Each conceptual route uses a worked calculation or explicit comparison; the decision route follows input, baseline, evaluation, model choice and failure response.
- Core-concept depth matrix: Below. Stable identifiers remain unchanged after edits.
- Route classification and teaching spines: Each route below is primary; no architecture is silently demoted.
- Figures, tables, and equations: Preserve existing figures and tables; add only equations or tables necessary for the worked calculations and decision case.
- Languages and executable examples: Existing PyTorch, TensorFlow and JAX snippets remain illustrative unless separately executed; independently check small arithmetic with disposable scripts.
- Evidence plan: Primary architecture papers, official framework documentation, analytical derivations and independently checked arithmetic. Review time-sensitive claims and qualify uncertainty.
- Open decisions: Exact consolidation of child headings requires boundary review and preserved fragment IDs; no word or heading quota applies.

## Review plan

- Whole-document checks: Source, headings, route transitions, sources, claims, outputs and accessibility; compare with `issue-482-review-proposal.md`.
- Representative samples: Backpropagation, recurrent Jacobians, ELBO, WGAN penalty, diffusion score and model-choice scenario.
- Content gate: Each primary route must enable its reader action through an explanation, application, interpretation and boundary.
- Depth gate: Follow each row's teaching spine; naming or listing is insufficient. Unresolved gaps block readiness.
- Post-draft checkpoint: Re-review changed passages, dependent transitions and exact locators, then record results in a revision-bound audit; no mechanical check replaces that judgement.
- Case acceptance: Trace declared inputs, computations or decisions, results, interpretations and failure conditions.
- Scope acceptance: Preserve all existing major families and substantive cases; optional details may not displace the primary route.

## Core-concept depth matrix

| route_id | route tier | concept_id | concept | reader action | mechanism or reasoning | significance | teaching device | worked evidence | interpretation | limitations | downstream use | Evidence/source plan |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| foundations | primary | network_update | Prediction and training | Follow a parameter update | Forward graph, loss and chain rule | Connects prediction to learning | Worked arithmetic | Small input through update | Explain sign and changed loss | One step and architecture only | Diagnose training | Check arithmetic independently; standard backprop sources |
| spatial | primary | cnn_features | Convolution and transfer | Calculate spatial output and choose a baseline | Shared local kernels and transferred representations | Relates image structure to compute | Shape calculation and comparison | Existing kernel and parameter example | Explain feature map and parameter savings | Boundaries, stride, dataset shift | Vision choice | Original CNN and transfer papers |
| recurrent | primary | state_gradients | Recurrent state and gradients | Trace state and gradient | Shared recurrence, Jacobian chain and gates | Explains memory and training limits | Numeric state trace and chain rule | Short scalar sequence | Compare persistence and decay | Gate path is not a global guarantee | Compare sequence models | RNN and LSTM primary papers; finite differences |
| attention | primary | attention_weights | Attention and transformers | Calculate an attention output | Scores, softmax and weighted values | Explains contextual mixing | Small numeric example | Query, keys and values | Explain the mixture | Scaling and masks depend on setup | Interpret transformer mechanism | Transformer paper and arithmetic check |
| language | primary | language_training | Language model training and adaptation | Explain token-to-model workflow | Tokenisation, objective and adaptation | Relates training to behaviour | Pipeline and objective comparison | Existing BERT/GPT and LoRA discussion | Compare prediction and adaptation | Tokenisation and model capabilities vary | Select pretrained models | Original papers and official model documentation |
| variational | primary | elbo | Variational autoencoders | Derive and interpret the ELBO | Jensen bound, posterior approximation and reparameterisation | Connects likelihood to trainable objective | Derivation and failure case | Marginal-to-bound steps and Gaussian KL | Interpret reconstruction, KL and gap | Approximate expectation and posterior collapse | Understand latent diffusion | Kingma and Welling primary paper |
| adversarial | primary | wasserstein | GANs and Wasserstein critic | Explain critic constraint and trade-offs | Minimax objective, Lipschitz bound and sampled penalty | Distinguishes theory from training | Counterexample and constrained objective | Existing GAN examples plus constant critic | Interpret approximate distance | Penalty does not prove global constraint | Compare generative models | WGAN and WGAN-GP papers |
| diffusion | primary | score | Diffusion and score estimation | Relate noise prediction to score | Gaussian corruption, conditional score and expectation | Explains reverse denoising | Derivation and sampler comparison | Existing forward process and added score bridge | Interpret noise and reverse movement | Model and sampler approximation | Choose conditioning and sampler | DDPM and score-matching primary papers |
| selection | primary | model_choice | Applied model selection | Choose and evaluate a baseline | Data, constraints, split, metric and model comparison | Makes architecture advice actionable | End-to-end scenario | Declared image task and hypothetical outcomes | Justify choice and next test | Domain shift, costs and uncertainty | Real project design | Document assumptions and source claims |
