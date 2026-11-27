# Scoped R projection review trial

This record supports [#490](https://github.com/kaybenleroll/ai_assisted_research/issues/490).
On 27 November 2026 a fresh reviewer examined a real primer's alternative
reader route. This was unblinded: the repository, key material and network
were accessible. It was not a complete audit, a fixture accuracy test, or a
measurement of general reliability.

## Inputs and procedure

The clean input revision was `c231267c066396fb8a47a6645e5e767d54abf7c2`.
SHA-256 hashes were `74e0d4fb5a7add90685da8fc7f94461eeb67ce4c4d976658c0da8383144332f7`
for `primer_knowledge_graph/primer_knowledge_graph.md`,
`29bc428f153f9e7f4e3b0640b9f1bf76c26d6b85a467a96cd5fd01b43d6f18d5`
for its tracked brief, and
`8b0744aff0d49efead38f6bac7b3f93b0e660988cec95db28ae361d07f32d3f5`
for `.agents/skills/primer-audit/SKILL.md`. The exact prompt was:

> Independently review the alternative R topology projection route in primer_knowledge_graph against its tracked brief at the current revision. Assess whether a reader can follow the promised construction, interpret the result and recognise the information lost when returning to evidence. Report specific strengths, actionable defects or uncertainties with precise locators and reader consequences. Inspect relevant guidance you independently select. This is a scoped read-only review, not a full audit; do not modify files, contact GitHub, inspect prior calibration reports or delegate. State files and guidance consulted, actual actions, and limits.

The operator ran `codex -a never exec --ephemeral --ignore-user-config
--sandbox read-only --model gpt-6.1-terra -c
'model_reasoning_effort="medium"' --cd /home/mcooney/workspace/ai_assisted_research
--json` with that prompt. Codex CLI was 0.172.0. JSONL and stderr were
captured outside the checkout; the process exited zero and all 19 JSONL records
parsed. The CLI warned that untrusted project-local configuration was disabled.
The command used the normal CLI sandbox, with no custom authentication mount.

The seven completed command events record requests to inspect the contract and
Git state; inventory primer files and route terms; read the review checklist and
style guide; read selected brief and primer ranges; inspect the R companion,
manifest, fixture and runtime README; reread projection and brief passages; and
search companion references and repository instructions. Their exit statuses
were zero. The recorder contains aggregated command outputs, not proof of the
exact payload delivered to the model. Several requests combined long outputs;
the captured output cannot establish complete model-side receipt or comprehension.
The reviewer reported a scoped source review and no execution of R, external
documentation verification, rendered-output inspection or full audit.

The skill existed at the pinned path, but no captured command read it and no
native activation event was observed. The event stream does not expose the
actual skill catalogue presented to the reviewer, so catalogue availability and
the ability to select it are unverified. The reviewer named the contract,
review checklist and style guide, not the audit skill. No conclusion about
native activation follows from a file's existence or its absence from the log.

## Findings and independent check

The reviewer found the hand-worked graph construction, path and component
reasoning, and return from topology to evidence useful. The record author
checked source lines 761–806: they specify eight vertices, five positive edges,
the path and component interpretation, and the temporal correction's effect on
the evidence answer. This is a sampled check, not verification of every claim.

The reviewer called the absence of a companion path and invocation an
actionable defect. Source line 806 identifies an R companion but supplies no
path or command. The script at `examples/r/knowledge_graph.R:3` specifies its
working directory; the manifest identifies it and `CONTRIBUTING.md:33` gives
the repository runner. The local navigation gap is supported; whether the
primer's reader promise makes it a blocking defect needs a broader judgement.

The reviewer also judged the transition from the hand-worked table to the R
node transformation too compressed. The source describes the operation at
line 806; the companion calculates membership and adds node fields at lines
24–33 and prints a node table at lines 59–64. More explanation could aid the
reader, but whether it is required is an editorial judgement, not an established
technical error. The reviewer supported this concern by asserting a
no-programming prerequisite for the R route. That premise is false: brief lines
14–17 say familiarity with tables and identifiers suffices for the standalone
route and that R applies to optional implementation material. The separate
claim that the node-table explanation needs expansion is not thereby resolved.

The open knowledge-graph issue [#481](https://github.com/kaybenleroll/ai_assisted_research/issues/481)
concerns different sampled evidence bindings; it does not adjudicate these
R-route findings. The trial did not use a pre-existing answer key, so misses
and other false positives cannot be exhaustively identified. No other false
positive is established by this bounded check. The route was not run and its
dependency versions and numerical outputs were not independently verified.

The operator reviewed the relevant event types, commands and report for privacy;
this record retains a minimised summary rather than raw output. The temporary
JSONL had SHA-256 `86ee1a879f2d179bee176955702fc4c79f645fc3a7fe1939f2e1af8cd112b17b`;
its hash cannot reconstruct it and the temporary file is not a durable archive.
One unsupported prerequisite claim warrants checking audience assertions
against the brief when adjudicating future findings; it does not by itself
justify changing the audit guidance or establish a failure rate.

## Captured command requests

These are the seven completed command requests, in order. Outputs remain subject
to the model-delivery limitation above.

```sh
/usr/bin/zsh -lc 'pwd && git status --short && git branch --show-current && git rev-parse HEAD && cat maintenance/docs/project-contract.md'
/usr/bin/zsh -lc "rg --files primer_knowledge_graph | sort && rg -n -i 'topology|projection|alternative|route_id' primer_knowledge_graph --glob '"'!*.html'"' --glob '"'!*.pdf'"' --glob '*brief*'"
/usr/bin/zsh -lc 'cat maintenance/docs/review-checklist.md && cat STYLE_GUIDE.md'
/usr/bin/zsh -lc "nl -ba primer_knowledge_graph/primer_knowledge_graph.brief.md | sed -n '1,180p;230,268p' && nl -ba primer_knowledge_graph/primer_knowledge_graph.md | sed -n '1,240p;700,850p'"
/usr/bin/zsh -lc 'nl -ba primer_knowledge_graph/examples/r/knowledge_graph.R && cat primer_knowledge_graph/examples/manifest.toml && cat primer_knowledge_graph/examples/fixture.json && cat primer_knowledge_graph/runtime/README.txt'
/usr/bin/zsh -lc "nl -ba primer_knowledge_graph/primer_knowledge_graph.md | sed -n '735,812p' && nl -ba primer_knowledge_graph/primer_knowledge_graph.brief.md | sed -n '70,100p;155,180p;250,266p' && rg -n 'c1|c5|c6|projection|r-graph|Rscript|tidygraph' primer_knowledge_graph/primer_knowledge_graph.md | head -65"
/usr/bin/zsh -lc "rg -n 'examples/r|knowledge-graph-r|r-graph|fixture.json|companion' primer_knowledge_graph/primer_knowledge_graph.md | head -35 && nl -ba primer_knowledge_graph/primer_knowledge_graph.md | sed -n '1,65p;180,235p' && rg -n 'r-graph|knowledge-graph-r|Rscript' maintenance primer_knowledge_graph/Justfile CONTRIBUTING.md --glob '"'!*.html'"' --glob '"'!*.pdf'"'"
```
