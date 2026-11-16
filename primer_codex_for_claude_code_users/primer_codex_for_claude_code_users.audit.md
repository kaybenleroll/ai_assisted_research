# Primer audit: Codex for Claude Code Users

- Issue and milestone: #435; coordinated workflows and configuration ownership revision
- Audit revision: codex-operating-model-audit-v4
- Source revision: 48562529f6413d07f3189e75d436984f51ee547c
- Reviewed revision: 48562529f6413d07f3189e75d436984f51ee547c
- Draft SHA256: 5d7780a7e79b3770f2f85103f8c636375706de2bf814b5e74d142bfc3f870619
- Tracked path: primer_codex_for_claude_code_users/primer_codex_for_claude_code_users.audit.md
- Starting branch: docs/435-codex-operating-model
- Reviewer(s): Codex independent content reviewer, gpt-6.1-sol at high effort; publication verification recorded separately
- Date: 2026-11-16
- Brief reviewed: primer_codex_for_claude_code_users/primer_codex_for_claude_code_users.brief.md, codex-operating-model-v4
- Review boundary: whole-source reading and coverage inventory; independent risk-selected primary-source checks of changed configuration and delegation semantics; illustrative case and alternative traced without execution; publication evidence separated below
- Teaching-case contract: primer_codex_for_claude_code_users/primer_codex_for_claude_code_users.case.md
- Core-concept depth matrix: brief codex-operating-model-v4; all 12 stable concept IDs and their unchanged tiers
- Readiness decision: ready

The current metadata and matrix identify source commit `48562529f6413d07f3189e75d436984f51ee547c`.
The original content review at `c8a4b57096bd8faf0659c37df412565be728fa8a` and baseline
`73e224d2bfe7824039edc9c55519520f5ae6ef0e` remain historical evidence.
Revision v3 adds a fresh independent whole-source review and a differential
review after integrating relocated main `8190dd96003c11d6ed91a419c0aa50f3ff54591d`.
Only three repository-path lines and four legacy-anchor spans changed from
the previously reviewed source. The post-maintenance section retains the historical v3 review and gate.
The current decision is recorded in Release Acceptance and Policy Applicability.

**Content gate: pass** for the brief's illustrative primary and alternative
routes. **Release readiness: ready** under the owner-approved policy in #439,
adopted at `58f2194e9dd534dc86e03770e3a043d51b5e1cce`; current-head CI
must pass before release. Revision v4 changes the verification-scope and release evidence only;
source, examples, case and published outputs retain the reviewed v3 bytes.
The owner accepted the served preview and authorised the policy update and
merge. The final release section records the applicability decision and
explicitly unperformed advisory checks. Earlier not-ready decisions below
remain historical; no unperformed check has become a pass.

Source locators use `primer_codex_for_claude_code_users/primer-codex-for-claude-code-users.md`.
Plain line ranges in the explanatory tables refer to that committed source.

## Whole-document review

| Area | Scope and method | Exact evidence or location | Status | Finding or gap | Disposition |
| --- | --- | --- | --- | --- | --- |
| Brief coverage and scope | Complete source and 12-row brief inventory | 7–49; 914–1048; 1836–1881; 2510–2525 | verified | Shared contract, durable preferences, role routing, lifecycle, authority, acceptance, migration and handoff are taught; catalogue is bounded reference. | Retain scope; no performance or deployment promise. |
| Technical claims, derivations, and calculations | Full-source claim inventory; independent targeted documentation check | 954–969, 1006, 1858–1864, 1879; source links in those passages | verified | Main-file precedence, agent-specific resolution, review mechanism and authority are distinguished. No calculations or measured model results are asserted. | Retain; historical catalogue claims were inventoried rather than exhaustively reverified. |
| Source quality, attribution, and freshness | Changed claim checks plus dated retained-source boundary | 5, 47–49, 2574–2599, 2601 onwards | verified | 15 November checks are separated from earlier model/interoperability and remote/data snapshots. | Retain stated dates and runtime limits. |
| Explanatory depth and prerequisites | Continuous reader pass and concept gate | 37–49; 53–125; 924–969; 1010–1034; 2512–2525 | verified | The organising model leads to a configured decision, bounded work, rejected completion and a revised evidence handoff. | Retain; no unresolved primary or alternative depth gap. |
| Structure, dependency order, and section fragmentation | Read outline and section boundaries against original | 511–970, 971–1048, 1050–1325; section-depth table below | verified | Configuration now precedes routing and workflow; its stale-source example remains one coherent teaching unit. Safety repetition points to shared checklists. | Retain distinct landmarks; no heading or word quotas used. |
| Worked examples and interpretations | Trace central case and hook/skill alternative | 1014–1034, 1354–1532, 1860–1864, 2512–2525 | verified | Pseudocode build trace supports a conditional scoped correction. Missing visual QA rejects completion; revised outputs require renewed inspection. | Retain illustrative mode; no runnable build-repair fixture claimed. |
| Applications, limitations, and failure modes | Whole-source inventory plus risk sampling | 965–969, 1022–1034, 1860–1881, 2521–2525 | verified | Wrong effective preference, exhausted open capacity, unavailable runtime, false read-only assumption and missing visual evidence have distinct consequences. | Retain layer-specific diagnosis. |
| Figures, tables, equations, and accessibility | Source table/code/heading inspection; rendered QA separate | Configuration table 958–963; acceptance 1026–1032; migration 1496–1507; no figures or equations | verified | Tables have contextual explanations; code is labelled by language; source uses normal heading hierarchy. This does not establish rendered or assistive-technology behaviour. | Retain source structure; publication checks below. |
| HTML, PDF, metadata, and committed outputs | Publication-agent report reconciled against unchanged draft digest | Final HTML/PDF and `.scratch/435/build-observations.md`; render-QA report | verified | Container build, metadata, static HTML checks and sampled pages pass. Source, HTML and PDF in the content commit match the reviewed artefacts byte for byte; baseline-history freshness and publication checks are retained with their dates. | Retain committed publication evidence and separate interactive limitations. |
| Residual uncertainty and follow-up questions | Explicit verification-boundary review | 2574–2599 | verified | Runtime model choices, native hooks/skills, permissions probes and exhaustive unchanged-source refresh are not claimed. | Retain documented limits; no unrelated expansion. |

| Case stage | Source or section | Evidence and result | Execution status | Gap or limitation |
| --- | --- | --- | --- | --- |
| Input or assumptions | 43–49, 1010 | Existing repository, known start, pinned-container policy, target files and outputs define the request. | illustrative | Synthetic; no runtime or account probe. |
| Construction or extraction decision | 924–967, 1012–1022 | Correct durable source, inspect overriding project intent, reconcile investigations, redirect target invocation only if shared route already supplies both outputs. | illustrative | Actual recipe syntax is intentionally not supplied; trace labels are pseudocode. |
| Intermediate representation | 928–949, 958–963, 1016–1020, 1870–1876 | Ownership comparison, configured-intent ledger, before/documented/proposed dependency trace and bounded delegate contract are the reviewable records. | illustrative | These records do not prove loaded settings or successful execution. |
| Stored or computed result | 2514–2519 | Candidate diff and claimed build outputs enter the evidence ledger. | illustrative | Build report is a claim requiring exact commands/logs; no observed run. |
| Reader-facing query or operation | 1026–1034, 2521 | Compare returned artefacts with acceptance cases and request missing HTML/PDF inspection. | illustrative | A generic reviewer approval cannot supply missing evidence. |
| Interpretation | 2521–2525 | Reject the initial completion claim; after repair, verify regenerated outputs, integrated diff and checks before accepting a candidate. | illustrative | Candidate acceptance does not grant commit or publication authority. |
| Failure mode or scope limit | 1024, 1860–1862, 2521–2523 | Missing runtime remains unverified; open-thread refusal is handled within the cap; clipped table requires regeneration and reinspection. | illustrative | Tool lifecycle and authority must be checked in the actual client. |

## Brief and example traceability

| Brief promise or core concept | Section(s) and explanation | Example, case, or limitation | Evidence status and gap |
| --- | --- | --- | --- |
| Shared behavioural model and canonical instructions | 53–125, 511–913 | Diagnostic model, import/fallback example and read-only discovery smoke test | verified; discovery and behaviour are distinct evidence. |
| Durable ownership and effective settings | 914–970 | Stale managed source, selective correction, trusted-project conflict and configured/observed ledger | verified after repair; no live deployment or model invocation. |
| Role routing and coordinated delivery | 994–1034, 1301–1311, 1836–1881 | Staged investigations, sole writer, reviewer, dependency trace and refusal recovery | verified; recommendation is reasoned policy, not a benchmark. |
| Hook/skill alternative | 1341–1532 | Shared procedure, native invocation/event adapters, runner, matrix and interpretation | verified as illustrative migration; actual discovery and hook delivery unexecuted. |
| Evidence-led continuation and comparison | 1171–1243, 2396–2505, 2510–2525 | Factual handoff, controlled evaluation record, missing-QA rejection and revised inspection | verified; fictional scores and returns remain explicitly illustrative. |
| Dated lookup branch | 981–992, 2572–2601 | Model catalogue and verification snapshot | verified within reference scope; not an entitlement or exhaustive compatibility guarantee. |

## Reader-scale section depth

| Section and route/concept IDs | Teaching job | Reasoning spine or worked thread | Application or interpretation locator | Material limitation or failure-case locator | Disposition and rationale |
| --- | --- | --- | --- | --- | --- |
| Introduction 7–49; all routes | Establish audience, motivating mismatch and reading route | Shared task becomes contract, configuration, coordination and evidence | 43–45 | 29–49 | retain; orientation is deliberately brief and makes execution boundaries explicit. |
| Two Harnesses 51–304; shared-contract/layers | Diagnose failure at its actual layer | Four-layer model, co-use modes and shared-state examples | 150–287, 289–303 | 113–125, 251–260 | retain; examples explain why separate checkouts and evidence matter. |
| First-Session Setup 305–510; shared-contract | Test repository comprehension before larger writes | Inspect, bounded source-only experiment, validation, complete publication continuation and handoff | 360–441, 443–509 | 409–441 | retain; temporary source-only exercise is expressly not a finished published change. |
| Instruction Systems 511–913; instruction-discovery | Choose one contract and test native discovery | Discovery algorithms, explicit import versus prose pointer, bounded smoke test | 682–791, 893–913 | 771–791 | retain; third-party generation is a bounded reference branch, not a prerequisite. |
| Configuration 914–970; config-ownership/effective-settings | Trace durable intent through files to session | Stale upstream source, owned-key correction, trusted project conflict and constraints | 935–969 | 963–969 | retain; one continuous incident explains ownership and why agreement is insufficient. |
| Models 971–1049; role-routing/review-acceptance | Allocate capability by responsibility | Coordinator/worker/reviewer roles, conditional dependency correction and acceptance cases | 996–1034 | 998–1006, 1024–1034 | retain; short catalogue and compact rule are deliberate lookup/synthesis landmarks. |
| Workflow 1050–1326; coordinated-delivery/evidence-handoff | Apply contracts across exploration, implementation, review and continuation | State boundary, produce evidence, resume against current files, reconcile investigations before writer | 1148–1243, 1301–1325 | 1245–1299, 1305–1311 | retain; remote/data discussion is a separate risk branch with its own earlier date. |
| Feature Translation 1327–2013; migration/reference | Translate required behaviour at the correct layer | Purpose/trigger/authority/scope precede a complete hook/skill migration; other feature details support lookup | 1341–1532, 2002–2013 | 1513–1532, 1883–2001 | retain; broad feature inventory is signposted as reference beyond the taught alternative. |
| Subagents 1836–1882; delegation-lifecycle/isolation-authority | Dispatch, preserve capacity and integrate | Concrete three-open refusal, evidence preservation, supported close/reuse and bounded return contract | 1860–1881 | 1846, 1862–1879 | retain; lifecycle is now an actual state transition, not only advice. |
| Permissions 1883–2001; isolation-authority | Separate policy, approval and enforced reach | Delete example, configuration controls, tool-scope comparison and harmless probes | 1885–1977 | 1942–2000 | retain; surrounding examples correct the worktree-as-security mistake. |
| Prompting 2014–2288; coordinated-delivery | Turn open requests into contracts and recover from specific failures | Before/after prompts, delegated question and classified recovery | 2032–2270 | 2097, 2182–2195, 2269–2287 | retain; examples are operational reference applying the earlier organising model. |
| Cookbook 2289–2363; migration/instruction-discovery | Make migration reversible | Inspect ownership, move shared policy, probe native behaviour and retain rollback | 2295–2355 | 2356–2363 | retain; links replace repeated feature mechanics while preserving rollout decisions. |
| Safety 2364–2395; isolation-authority/review-acceptance | Apply task authority to real resources | Container mounts/credentials, stopping budgets and generated-output contract | 2368–2394 | 2370–2392 | retain; consolidated checklist points to one operational record. |
| Measurement 2396–2505; workflow-evaluation | Compare accepted workflows fairly | Same starting state and contract, correctness/safety gates, review burden, fictional record and interpretation | 2400–2492 | 2438–2451, 2479–2492 | retain; rubric is for future empirical work and scores no primer or model here. |
| Conclusion 2506–2600; review-acceptance/durable-handoff | Close the case and provide task lookup | Reject missing output inspection, repair/reinspect and transfer factual evidence | 2512–2525 | 2521–2525, 2574–2599 | retain; quick-reference subsections are deliberately concise lookup aids. |
| References 2601 onwards; reference | Direct further verification | Official sources grouped by retained review dates and purpose | 2603 onwards | Verification scope 2574–2599 | retain as reference; linked material does not prove runtime parity. |

## Route transition evidence

All transitions below were rechecked against historical content commit c8a4b570 and its source SHA256; the same semantic passages were re-reviewed at 48562529. Their operations
remain illustrative. Each result supplies the next row's stated input within
that route; dependencies shared across routes are named explicitly.

| route_id | concept_id(s) | transition (from to) | linked input and reader operation | intermediate reasoning or decision | result | interpretation | material limitation | execution status | gap and reader consequence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| shared-contract | layers | Request to diagnosed execution layer | 53–125, 289–303: inspect why a proposed test cannot run | 109–125: distinguish wrong command, instructions, cwd, missing runtime and denied authority | Layer-specific diagnosis feeds initial repository inspection at 360–407 | 301: repair the failed layer rather than automatically change model | 121–125: approval and sandbox reach are separate | illustrative | No gap; reader can explain why a model upgrade does not supply infrastructure. |
| shared-contract | instruction-discovery | Repository inspection to shared loaded contract | 360–407, 682–791: find canonical policy, choose explicit Claude import or valid Codex fallback and inspect discovery evidence | 751–777: competing AGENTS file defeats fallback; Markdown pointer is not an include | Chosen policy plus recorded root/cwd/trust/byte limit feeds the harmless smoke prompt at 783–789 | 791: correct behaviour supports compatibility without proving exact provenance | 773–791: untrusted config, below-cwd discovery and absent logs can leave provenance unknown | illustrative | No gap; the contract is available for configuration and the bounded build task without pretending to share permissions. |
| configuration | config-ownership | Intended preference to repaired durable chain | 924–935: compare managed source with installed reference, then reference with live file | 926–933: agreeing installed/live pair still conceals stale upstream coordinator | Correct only owned durable keys, preview/apply and recheck both comparisons; resulting intended values are shown at 937–949 | 935: file agreement is the result handed to effective-setting diagnosis, not a model-call result | 935–939: whole-file replacement can destroy desktop-owned settings; dotfile tooling is optional | illustrative | No gap; reader can prevent future synchronisation from undoing the intended coordinator. |
| configuration | effective-settings | Agreeing files to project-specific configured intent | 954–963: extend repaired personal Sol/medium with trusted project Terra/medium | 954–956: bounded CLI/project/profile/user ordering, no higher override and no blocking requirement | 962: configured result is Terra/medium, while 963 records runtime not observed | 965: retain deliberate project policy or resolve ownership before a narrow change; pass known intent and unknown runtime to dispatch | 967–969: requirements constrain choices; agent/review mechanisms and actual observations remain separate | illustrative | No gap after repair; reader can justify the mismatch without changing trust or falsely claiming runtime selection. |
| coordinated-delivery | role-routing | Bounded task and configured intent to role allocation | 996–1012: fix outcome, scope and acceptance cases before dispatch | 1000–1012: coordinator retains ambiguity/integration, worker investigates, sole writer follows reconciled findings, reviewer challenges candidate | Role contracts at 1303–1307 and 1870–1876 feed dependency investigation | 998–1006: recommendations follow responsibility; fresh/different review is not proof of independence | 1004, 1012: tightly coupled tasks may remain local; missing context/runtime is diagnosed before escalation | illustrative | No gap; coordinator responsibility is taught instead of a universal cheap-first rule. |
| coordinated-delivery | delegation-lifecycle | Role contracts to bounded capacity recovery | 1850–1860: three open threads, two Done and one working, then refused fourth spawn | 1858–1860: open count differs from running count; preserve completed findings before supported closure | Freed slots permit later assignment under same cap; if unavailable, 1862 chooses supported reuse or existing-session work | 1860–1862: the refusal is lifecycle evidence, not model failure or an instruction to raise limits | 1846, 1862: actual tools may lack closure/reuse; waiting alone proves no release | illustrative | No gap after repair; reader has a complete failed-spawn/recovery transition. |
| coordinated-delivery | isolation-authority | Bounded no-edit contract to actual authority choice | 1870–1879: reviewer/investigator receives no-edit scope in a potentially writable parent | 1879, 1885–1900: a prompt or worktree separates neither OS authority nor external service access | Choose an enforced restricted session/process when required; inspect external tools separately; pass that boundary to implementation | 1309, 1879: checkout separation prevents collisions but is not read-only enforcement | 1942–1963: shell and network restrictions do not cover every external tool or managed surface | illustrative | No gap; no claimed OS probe, and reviewer scope is not mistaken for sandbox isolation. |
| coordinated-delivery | role-routing,review-acceptance | Investigation to candidate correction | 1014–1022: compare faulty host-PDF path with documented shared pinned-container HTML/PDF route | 1022: redirect only the target if shared recipe already supplies both outputs; retain shared files | Proposed scoped correction leads to candidate diff/build evidence at 2514–2519 | 1022, 2518: trace explains the decision but actual logs/diff are still required | 1022–1024: false premise, shared-file dependency or unavailable runtime blocks unsupported completion | illustrative | No gap; pseudocode is sufficient for the promised coordination decision, not a runnable recipe tutorial. |
| coordinated-delivery | review-acceptance | Candidate to rejected and revised evidence | 2514–2521: compare returned diff/trace/build claim with missing page inspection and acceptance cases 1026–1032 | 2521: missing visual evidence rejects completion; runtime-blocked return stays not ready | 2523: clipped-table finding leads to scoped repair, both outputs regenerated and fresh inspection | 2523: coordinator verifies revised records, integrated diff and required checks before calling it a reviewable candidate | 2521–2525: no actual run or unconditional release; commit authority remains separate | illustrative | No gap; renewed artefacts require renewed review rather than inheriting the first build's approval. |
| migration | integration-translation | Existing hook/skill to shared deterministic procedure | 1354–1429: inspect explicit-only Claude audit and Edit/Write post-tool feedback | 1399–1429: canonical neutral skill plus native adapters preserve explicit selection without copying the procedure | Shared procedure and invocation adapters feed fixed runner and Codex event adapter at 1433–1482 | 1427–1429: native selection must be checked; invocation policy grants no tool authority | 1356, 1397: fixture is hypothetical and event matchers miss shell/external writes | illustrative | No gap; reader sees which procedural content moves and which trigger semantics need an adapter. |
| migration | integration-translation | Adapters to interpreted acceptance matrix | 1433–1507: inspect fixed runner exits, native post-edit matchers and trust, then compare behavioural probes | 1482–1490: post-edit feedback cannot prevent/undo edits; required CI adds its own integration enforcement | Expected discovery, event, nested-cwd, invalid-input, missing-runtime and authority outcomes form the matrix | 1509: direct lint success proves neither native discovery nor event delivery, and catalogue presence proves neither execution nor no-edit compliance | 1494–1507: expected outcomes are not observed passes; trust, runtime and trigger coverage remain client-specific | illustrative | No gap; alternative teaches interpretation and limits without claiming a deployed migration. |
| evidence-handoff | durable-handoff | Accepted or blocked candidate to continuation state | 1214–1243, 2521–2525: inspect current files and record branch/revision, paths, commands, errors, output checks and remaining work | 1219–1235: repository state and factual note carry the task; conversational confidence does not | 2525: next harness can inspect/rerun/complete checks without the original chat | 1233–1243, 2525: keep observed selections separate from configured intent and identify the next permitted action | 1180–1217: history/retention/compaction are surface-specific and do not restore a guaranteed repository state | illustrative | No gap; blocked work has an explicit continuation rather than a false completion claim. |
| evidence-handoff | workflow-evaluation | Continuation record to evidence-based routing decision | 2400–2416, 2453–2479: fix equal starts/contracts and populate a per-run record | 2418–2451: correctness and safety gate success before cost; separate repair/review burden and infrastructure failure | 2480–2489: hypothetical comparison is interpreted narrowly and generated-output omission limits the routing conclusion | 2482–2489: observed future workflow evidence can change policy; fictional case does not rank models | 2449–2451, 2479: pilot uncertainty and placeholder record remain explicit | illustrative | No gap; reader can design an evaluation without mistaking this revision for one. |

## Adversarial depth gate

All 12 stable rows were independently reviewed again against the complete
source, followed by a differential review of the seven changed lines and
their dependent discovery, migration, routing and operational passages.
The source line count and all 48 exact locator line numbers are unchanged;
line 996 adds an empty anchor before identical prose. Matrix revisions below
bind this fresh judgement to the current source commit. Earlier review
history and its original revision bindings remain recorded separately.

| route_id | route tier | concept_id | explanation locator | example/action locator | interpretation locator | limitation locator | evidence revision | reviewer | status | finding | scope decision |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| shared-contract | primary | layers | primer_codex_for_claude_code_users/primer-codex-for-claude-code-users.md:53 | primer_codex_for_claude_code_users/primer-codex-for-claude-code-users.md:109 | primer_codex_for_claude_code_users/primer-codex-for-claude-code-users.md:301 | primer_codex_for_claude_code_users/primer-codex-for-claude-code-users.md:121 | 48562529f6413d07f3189e75d436984f51ee547c | Codex independent migration re-review | verified | Diagnostic comparison explains layer-specific repair and distinguishes approval from reach. | Retain primary diagnosis; no guaranteed client parity. |
| shared-contract | primary | instruction-discovery | primer_codex_for_claude_code_users/primer-codex-for-claude-code-users.md:684 | primer_codex_for_claude_code_users/primer-codex-for-claude-code-users.md:739 | primer_codex_for_claude_code_users/primer-codex-for-claude-code-users.md:791 | primer_codex_for_claude_code_users/primer-codex-for-claude-code-users.md:773 | 48562529f6413d07f3189e75d436984f51ee547c | Codex independent migration re-review | verified | Native import, fallback conflict, diagnostics and behaviour smoke prompt teach shared-text discovery. | Retain; exact provenance and runtime discovery remain unexecuted. |
| configuration | primary | config-ownership | primer_codex_for_claude_code_users/primer-codex-for-claude-code-users.md:924 | primer_codex_for_claude_code_users/primer-codex-for-claude-code-users.md:928 | primer_codex_for_claude_code_users/primer-codex-for-claude-code-users.md:935 | primer_codex_for_claude_code_users/primer-codex-for-claude-code-users.md:939 | 48562529f6413d07f3189e75d436984f51ee547c | Codex independent migration re-review | verified | Two adjacent comparisons catch stale upstream intent and owned-key correction preserves unrelated live settings. | Retain synthetic optional user-tool chain; no particular dotfile product required. |
| configuration | primary | effective-settings | primer_codex_for_claude_code_users/primer-codex-for-claude-code-users.md:954 | primer_codex_for_claude_code_users/primer-codex-for-claude-code-users.md:956 | primer_codex_for_claude_code_users/primer-codex-for-claude-code-users.md:965 | primer_codex_for_claude_code_users/primer-codex-for-claude-code-users.md:967 | 48562529f6413d07f3189e75d436984f51ee547c | Codex independent migration re-review | verified | Sol user intent versus trusted-project Terra is resolved under stated assumptions; runtime is explicitly unknown; agent and review mechanisms stay separate. | Retain bounded local comparison, not an exhaustive configuration manual or account test. |
| coordinated-delivery | primary | role-routing | primer_codex_for_claude_code_users/primer-codex-for-claude-code-users.md:996 | primer_codex_for_claude_code_users/primer-codex-for-claude-code-users.md:1012 | primer_codex_for_claude_code_users/primer-codex-for-claude-code-users.md:1022 | primer_codex_for_claude_code_users/primer-codex-for-claude-code-users.md:1024 | 48562529f6413d07f3189e75d436984f51ee547c | Codex independent migration re-review | verified | Coordinator judgement, bounded worker, designated writer and fresh reviewer are justified through the conditional build correction. | Retain reasoned routing recommendation; no measured model ranking. |
| coordinated-delivery | primary | delegation-lifecycle | primer_codex_for_claude_code_users/primer-codex-for-claude-code-users.md:1858 | primer_codex_for_claude_code_users/primer-codex-for-claude-code-users.md:1860 | primer_codex_for_claude_code_users/primer-codex-for-claude-code-users.md:1862 | primer_codex_for_claude_code_users/primer-codex-for-claude-code-users.md:1846 | 48562529f6413d07f3189e75d436984f51ee547c | Codex independent migration re-review | verified | Concrete open-thread refusal, evidence preservation, supported closure/reuse and existing-session fallback teach recovery within the cap. | Retain local three-open example; active tools own actual lifecycle semantics. |
| coordinated-delivery | primary | isolation-authority | primer_codex_for_claude_code_users/primer-codex-for-claude-code-users.md:1885 | primer_codex_for_claude_code_users/primer-codex-for-claude-code-users.md:1870 | primer_codex_for_claude_code_users/primer-codex-for-claude-code-users.md:1879 | primer_codex_for_claude_code_users/primer-codex-for-claude-code-users.md:1951 | 48562529f6413d07f3189e75d436984f51ee547c | Codex independent migration re-review | verified | A no-edit contract in a writable parent is advisory; enforced session/process restrictions and external-tool controls must be chosen separately. | Retain conceptual counterexample; no security probe claimed. |
| coordinated-delivery | primary | review-acceptance | primer_codex_for_claude_code_users/primer-codex-for-claude-code-users.md:1006 | primer_codex_for_claude_code_users/primer-codex-for-claude-code-users.md:2521 | primer_codex_for_claude_code_users/primer-codex-for-claude-code-users.md:2523 | primer_codex_for_claude_code_users/primer-codex-for-claude-code-users.md:1032 | 48562529f6413d07f3189e75d436984f51ee547c | Codex independent migration re-review | verified | Evidence ledger rejects missing visual QA and requires regeneration/reinspection after repair; review_model is restricted to /review. | Retain illustrative acceptance decision with separate commit authority. |
| migration | alternative | integration-translation | primer_codex_for_claude_code_users/primer-codex-for-claude-code-users.md:1343 | primer_codex_for_claude_code_users/primer-codex-for-claude-code-users.md:1401 | primer_codex_for_claude_code_users/primer-codex-for-claude-code-users.md:1509 | primer_codex_for_claude_code_users/primer-codex-for-claude-code-users.md:1506 | 48562529f6413d07f3189e75d436984f51ee547c | Codex independent migration re-review | verified | Neutral procedure, explicit-only adapters, fixed runner, post-edit coverage and expected probes teach behavioural translation. | Retain taught unexecuted alternative; other feature categories remain reference. |
| evidence-handoff | primary | durable-handoff | primer_codex_for_claude_code_users/primer-codex-for-claude-code-users.md:1219 | primer_codex_for_claude_code_users/primer-codex-for-claude-code-users.md:1225 | primer_codex_for_claude_code_users/primer-codex-for-claude-code-users.md:2525 | primer_codex_for_claude_code_users/primer-codex-for-claude-code-users.md:1214 | 48562529f6413d07f3189e75d436984f51ee547c | Codex independent migration re-review | verified | Current files plus factual note carry accepted or blocked work across harnesses without shared transcripts. | Retain surface-specific history/retention boundary; no transcript migration promised. |
| evidence-handoff | primary | workflow-evaluation | primer_codex_for_claude_code_users/primer-codex-for-claude-code-users.md:2402 | primer_codex_for_claude_code_users/primer-codex-for-claude-code-users.md:2457 | primer_codex_for_claude_code_users/primer-codex-for-claude-code-users.md:2482 | primer_codex_for_claude_code_users/primer-codex-for-claude-code-users.md:2451 | 48562529f6413d07f3189e75d436984f51ee547c | Codex independent migration re-review | verified | Controlled starting state, correctness/safety gates and review burden lead to a bounded interpretation of fictional results. | Retain evaluation method; no empirical advantage claimed. |
| reference | reference-only | catalogue-and-surfaces | primer_codex_for_claude_code_users/primer-codex-for-claude-code-users.md:983 | primer_codex_for_claude_code_users/primer-codex-for-claude-code-users.md:985 | primer_codex_for_claude_code_users/primer-codex-for-claude-code-users.md:992 | primer_codex_for_claude_code_users/primer-codex-for-claude-code-users.md:1038 | 48562529f6413d07f3189e75d436984f51ee547c | Codex independent migration re-review | verified | Dated lookup, official links and explicit client/account boundaries are adequate for reference scope. | Retain dated catalogue; not every unchanged identifier, entitlement or community count refreshed. |

| Published snippet or calculation | Test/manifest ID or illustrative status | Fixture and expected result checked | Gap |
| --- | --- | --- | --- |
| Instruction bridges and smoke prompts, 613–791 | illustrative | Discovery semantics and expected policy response inspected in prose | No two-client runtime probe. |
| Configuration and agent TOML, 941–950 and 1850–1856 | parsed-only syntax; scenario illustrative | Coordinator parsed all eight published TOML fences with Python `tomllib`, zero failures; `.scratch/435/config-parse.txt` records the exact draft digest | No live deployment, provider call, schema validation or observed model selection. |
| Build trace, 1016–1020 | illustrative pseudocode | Faulty host path, shared container route and conditional target correction traced | Deliberately not executable just syntax. |
| Hook/skill migration, 1354–1532 | illustrative | Fixed source, runner exit conditions, native adapters and expected matrix read | No native activation, hook delivery or CI execution. |
| Shell/worktree/MCP examples and prompts | illustrative | Source coverage and authority caveats inventoried | No cleanup, connection, external write or enforcement probe. |
| Evaluation YAML, 2457–2477 | illustrative | Record fields and fictional interpretation inspected | No measured run or model comparison. |

## Representative sampling

| Sample/page/object | Risk represented | Evidence and result | Status | Follow-up |
| --- | --- | --- | --- | --- |
| Opening, 7–49 | Overpromised parity or undocumented runtime claims | Reader, background, main/alternative/reference routes and illustrative boundary are explicit. | verified | No expansion required. |
| Configuration, 924–969 and 1864 | Cross-layer precedence mistaken for observed execution | Stale-source and trusted-project counterexamples have different diagnoses; custom-file effort nuance and review mechanisms are explicit. | verified | Runtime choices remain unknown. |
| Build case, 1010–1034 and 2512–2525 | Checklist substituted for construction; confidence substituted for acceptance | Before/documented/proposed trace leads to scoped decision; missing-QA rejection leads to repair and renewed evidence. | verified | No teaching-case execution inferred from publication checks. |
| Hook/skill migration, 1354–1532 | Native syntax mistaken for equivalent behaviour | Shared runner and procedure, separate triggers and authority, expected outcome matrix and interpretation form a complete alternative. | verified | Native probes remain unexecuted. |
| PDF pages 1, 30, 31, 32, 33, 47, 61, 62 and 88 | Clipping, overflow and misleading table/code structure | Publication reviewer opened the actual page images: opening/contents, ownership table, TOML, precedence table, model table, lifecycle, hook/code/table and final ledger legible without observed clipping. Coordinator independently checked pages 31, 33 and 88. | verified | Sampled visual pass only; no figures/equations in source, no claim about all 94 pages or assistive technology. |

## Revision-triggered second audit

This is the first tracked audit for this milestone. It includes a second
human pass after findings on the first integrated draft; baseline-era source
checks are retained only within their original topic/date boundary.

| Previous and current revisions | Changed artefacts and exact passages | Affected route/concept rows, transitions, claims, examples and outputs | Review scope, reviewer, method and result | Remaining gaps and readiness consequence |
| --- | --- | --- | --- | --- |
| Baseline 73e224d2bfe7824039edc9c55519520f5ae6ef0e to Draft SHA256 858808dc92e322fcb9c23bc1eede9c003bbf74c1ddf66a662f26d65a8614cee7 | Source orientation, promoted configuration, moved/reworked routing, staged workflow, subagent semantics, case ending and reduced checklist repetition | All 12 concepts inventoried; new main-route transitions reviewed alongside retained hook/skill alternative | Codex independent full-source review found effective-settings depth gap, promised lifecycle-case omission and staged-plan inconsistency; dependency trace concern resolved by actual draft | Findings sent to integrator before audit; no readiness carried forward. |
| Draft SHA256 858808dc92e322fcb9c23bc1eede9c003bbf74c1ddf66a662f26d65a8614cee7 to 93e2fb1e57d6e57fbef8f11ce296d2a32976f700fcc4390fb96e82d4ffdebdff | Source 954–969, 1303, 1858–1864 and adjacent configuration, dispatch and handoff passages | effective-settings; delegation-lifecycle; role-routing and dependent case transitions | Codex reread changes against official semantics, followed configured intent into delegation, checked closure fallback and sole-writer sequence; all three findings resolved | Content pass; exact working draft lacks commit binding and publication evidence remains separate. |
| Final Draft SHA256 unchanged; newly regenerated outputs and completed brief checkpoint | Final HTML/PDF, Justfile date metadata, generated README date/order, brief route checkpoint and publication report | Publication/accessibility evidence, all current source locators and retained case interpretation | Codex reconciled actual report against final source digest and checked brief checkpoint; publication reviewer inspected nine page samples. Source meaning and illustrative case status unchanged. | Working-tree publication pass; uncommitted binding, browser interaction and screen-reader checks remain release limits. |
| Reviewed draft SHA256 93e2fb1e57d6e57fbef8f11ce296d2a32976f700fcc4390fb96e82d4ffdebdff to real content commit c8a4b57096bd8faf0659c37df412565be728fa8a | Source/HTML/PDF bytes identical; brief v2 and audit v2 now bind source evidence; interactive attempt recorded | All 12 stable concepts and five taught routes retained; configuration, lifecycle, authority and acceptance groups reread; output identity checked | Independent reviewer used committed blobs, SHA256 equality, exact-locator checks and affected-passage review; content pass retained, structural and Git-backed validators now pass | Revision blocker resolved. Required interactive accessibility checks remain unavailable, so release stays not-ready and main will open a draft PR. |
| c8a4b57096bd8faf0659c37df412565be728fa8a to 48562529f6413d07f3189e75d436984f51ee547c | Source lines 818–819 and 2324 update live maintenance paths; 996, 1000, 1844 and 2394 restore legacy fragments; HTML/PDF regenerated | instruction-discovery, role-routing, integration-translation and the operational handoff; all 12 stable concepts and route tiers retained | Independent whole-source review plus differential reading and exact-locator check; content pass retained; scenarios stay illustrative | Required interactive accessibility checks remain unavailable; release not-ready. |

| Evidence and affected rows | Retained or newly reviewed/executed | Revision, method, result and reason for retention | Limits or outstanding checks |
| --- | --- | --- | --- |
| Complete source, 12 concepts and five taught routes | Newly reviewed | Current Draft SHA256; continuous reading plus exact-row and route trace; content pass | No scenario execution. |
| Configuration/subagent/review authority claims | Newly reviewed | Official configuration basics, reference and subagent pages opened 15 November; agrees with scoped researcher source notes | Documentation-only, without account, installed-client or permission probe. |
| Instruction/import/model/hook/skill and remote/data source checks | Retained historical source evidence plus current editorial review | Stated 7 November and earlier dates remain visible at 2574–2599; unchanged claims and limitations reread | Not every unchanged source/citation or community statistic independently refreshed. |
| Publication outputs and brief checkpoint | Retained publication evidence; newly reviewed commit binding | Build, lint, offline links, HTML/PDF checks and sampled visual pass match artefacts now committed at c8a4b57096bd8faf0659c37df412565be728fa8a; source and output byte identity independently checked | Required interactive accessibility checks remain unavailable; committed-state semantic review is recorded below. |

## Reconcile earlier evidence

| Earlier finding or audit | Location and revision reported | Current status: confirmed, resolved, stale, or unverified | Evidence |
| --- | --- | --- | --- |
| First draft did not teach trusted-project override of agreeing user files | Source 954 at Draft SHA256 858808d | resolved | Current 954–969 gives local ordering, Sol/Terra example, ownership decision and runtime-unknown ledger. |
| Brief's failed-spawn lifecycle promise was generic advice | Source 1290/1843 at Draft SHA256 858808d | resolved | Current 1860–1862 gives three-open refusal, evidence preservation and supported closure/reuse/fallback. |
| Implementation began before investigation in one retelling | Source 1288 at Draft SHA256 858808d | resolved | Current 1303 agrees with 1012 and 1840: reconcile read-only investigations, then sole writer. |
| Custom agents equated with TOML; worktree suggested as access isolation | Starting source in researcher notes | resolved | Current 1838–1844 distinguishes built-ins and definitions; 1309 and 1879 distinguish checkout separation and enforcement. |
| Earlier interoperability and model checks | 7 November snapshot, current 2576–2599 | confirmed | Retained as historical bounded checks, not a fresh runtime or comprehensive citation audit. |
| Native examples and performance | Brief/case exclusions | unverified | Deliberately illustrative; no deployment, benchmark, savings, native activation or account availability asserted. |

## Release readiness checklist

| Gate | Decision | Required evidence or limitation |
| --- | --- | --- |
| Brief and audit binding | pass | Brief v4 and audit v4 bind current source 48562529f6413d07f3189e75d436984f51ee547c; independent full-source and differential review completed. |
| Route/concept gate | pass | Five taught routes and 11 primary/alternative concepts pass; reference row retains bounded lookup scope. |
| Locator validity | pass | All 48 unique source locators checked against the committed source, with no blank or out-of-range lines; Git-backed validator result recorded below. |
| Examples | pass | All teaching snippets/cases are illustrative; no executable manifest or run claimed. |
| Rendered outputs | pass | Final container build, metadata/text checks, deterministic HTML semantics and current samples on pages 1, 31, 33, 47 and 67 pass. The committed source/HTML/PDF match reviewed artefacts; final committed-state freshness is recorded by the coordinator. |
| Accessibility | pass | Required automated structure, metadata and sampled visual checks pass. Interactive keyboard, no-JavaScript, browser-tree and screen-reader checks remain not performed; they are advisory for this content/outline and legacy-fragment revision under #439. No conformance or equivalent fragment focus/scroll behaviour is claimed. PDF remains untagged. |
| Sources | pass | Changed configuration/delegation semantics checked against primary pages; retained topic/date limits explicit. |
| Links | pass | Scoped offline generated-HTML links pass with zero findings; exhaustive online checks not claimed. |
| Revision review | pass | First-draft findings and repairs genuinely reread with dependent transitions. |
| Handoff | pass | Owner accepted the served preview and authorised the revised policy and merge. Content/source/output evidence is retained; current-head CI and policy integration are verified by the coordinator before merging. |

- Content gate: **pass**
- Release readiness: **ready**

## Historical Execution and Render Evidence

- Transition checks: all route operations illustrative; reviewed stated inputs, intermediate decisions, results, interpretation and limits at the Draft SHA256. No model selection, hook trigger, skill activation, sandbox boundary or synthetic build operation was independently executed.
- Reader-scale section review: every H2 and the primary/alternative hosting subunits recorded above; retained sections teach distinct operations or are explicitly bounded orientation/reference/synthesis.
- Commands actually run by content reviewer: source/status/diff/heading inventory, `sha256sum`, `git diff --check`, structural evidence checker and repository audit command as recorded below. Publication commands are separate from teaching-case execution.
- Examples executed: none; illustrative only.
- Examples parsed but not executed: coordinator reports all eight TOML fences accepted by Python `tomllib`, zero failures, at original content commit c8a4b570; the TOML fences remain unchanged. This parses TOML syntax only; no Codex schema, effective settings or model execution is established. Scenario transitions remain illustrative.
- Visual QA pages: publication reviewer inspected 1, 30, 31, 32, 33, 47, 61, 62 and 88; all pass for legibility and no observed clipping. Code samples are on 30, 31 and 62. The automated page-47 code/figure suggestions are prose; no figure/equation sample applies because none exist. Coordinator independently opened pages 31, 33 and 88.
- Offline or unavailable checks: exhaustive online citation/link refresh, native migration, model/account reachability, effective runtime selection, permission probes and assistive-technology traversal not performed.
- Reviewer effort: complete source reading, claim/route inventory, targeted official-source verification, one findings round and affected-scope second review; no quality score assigned.
- Stopping rule: stop after committed-state review, evidence binding and honest accessibility reconciliation. At the original draft checkpoint, main owned the evidence commit, push and draft PR; merge was not authorised then. The continuation now authorises conditional merge after release gates pass.

Working-tree publication evidence was supplied by the publication reviewer and
reconciled by this reviewer against the unchanged Draft SHA256:

- `just --justfile primer_codex_for_claude_code_users/Justfile all`: pass,
  Podman 5.7.0, Pandoc 3.11, image ID
  `61d7d31cd74fba20b6ac708c108fa8879f3a7106b9f0226f30debe2be130771a`.
  Build log contains no reported warning, missing-character, overfull or error
  message. Required HTML and 94-page letter PDF regenerated together.
- `just check-meta`, `just check-variants`, `just check-mermaid`,
  `just check-structure`, scoped `just lint-md`, `just lint-spell` and
  `just lint-prose`: pass. Structure advisories concern other primers.
  Vale's line-952 “currently working” advisory is a false positive: it describes
  a state in the running/open distinction, not an undated product assertion.
- `just lint-links primer_codex_for_claude_code_users/primer-codex-for-claude-code-users.html`:
  pass, zero scoped offline findings. The earlier Markdown-path invocation
  failed scope validation and was corrected; it was not a link result.
- `just render-qa primer_codex_for_claude_code_users`: pass. Report records
  116 HTML headings, 19 structured tables, 73 pre blocks, zero images, no
  duplicate IDs or unresolved fragments, expected PDF title/author and
  extractable text without replacement characters. Deterministic HTML title,
  main/contents landmarks, skip link, heading levels and TOC control targets
  pass. These checks do not establish browser or screen-reader behaviour.
- Coordinator ran `just readme` and `just readme-check`: pass, with README
  changes limited to the document date and recent-list ordering.
- `just check-fresh` initially failed because the linked worktree's Git
  metadata is outside the container mount. Coordinator reran the unchanged
  recipe with read-only mounts of the actual baseline HEAD metadata and real
  object database: `just 'PYTHON_OCI_FLAGS=--userns=keep-id -v /tmp/ai_assisted_research-435/.scratch/435/freshness-git-view:/home/mcooney/workspace/ai_assisted_research/.git/worktrees/ai_assisted_research-435:ro -v /home/mcooney/workspace/ai_assisted_research/.git/objects:/history/objects:ro' check-fresh`:
  pass, 31 source/output pairs. This checks committed history at the actual
  baseline; it does not bind this uncommitted draft to a new commit.

Historical initial checks, before the content commit: the content reviewer ran the structural evidence checker successfully. The
initial direct `just primer-audit primer_codex_for_claude_code_users` could
not create its temporary file in read-only `/run/user/1000/just`; rerunning
with `env XDG_RUNTIME_DIR=/tmp` reached the repository checks. The structural
stage passes. The Git-backed stage rejects the working source because it
differs from the baseline reviewed commit, as required. No checker or policy
was changed to evade this result. Final command output and precise revision
failure are retained in the task record; release remains not-ready.

## Historical Committed-State and Accessibility Follow-Up

The user authorised the remaining checks, commits, push and PR creation after
the initial draft audit. Main committed source, required HTML/PDF, metadata,
README, brief and case together as
`c8a4b57096bd8faf0659c37df412565be728fa8a`. Audit v2 and brief v2 bind the
review to that actual source commit while preserving the original baseline
and draft review history above. Main owns the subsequent evidence commit and
draft PR; merge remains outside the authorised scope.

The independent reviewer used `git show <commit>:<path>` and Python SHA-256
comparison to establish that all three committed artefacts equal the
previously reviewed working files byte for byte:

| Committed artefact | SHA256 | Comparison result |
| --- | --- | --- |
| Source Markdown | 93e2fb1e57d6e57fbef8f11ce296d2a32976f700fcc4390fb96e82d4ffdebdff | Exact match |
| Rendered HTML | a1cb73afba6aa0e8a4c7ea7172261af44c1649eaf502c6322ec976de55fc49bf | Exact match |
| Rendered PDF | 9383c36f4d0422fba557a57d3c46ac0bfff0868c6cc9f39c6c702763839b491f | Exact match |

The reviewer then read committed source 924–969, 996–1034, 1301–1311,
1836–1881 and 2510–2525, revisiting configuration ownership and effective
selection, role allocation, build correction, thread refusal/recovery,
authority and the rejected/revised completion claim. All 48 unique exact
source locators were checked against the committed text; none is blank or
out of range. The other source passages, native migration example and
published outputs are unchanged, so their prior full-reading, illustrative
transition and sampled visual evidence remains applicable at the same
source/output digests. No teaching scenario was executed in this follow-up.

Main attempted the required interactive checks through the supported Browser
skill and documented recovery. Browser target selection returned `No browser
is available`; supported browser inventory was `[]`. No target could be
opened. A loopback server could run in the permitted execution context but
did not provide a browser connection. Keyboard navigation, no-JavaScript
navigation, browser accessibility-tree inspection and representative
screen-reader traversal therefore remain **not checked**, not passed.

Orca 50.3 and AT-SPI2 2.60.4 were confirmed installed in the permitted desktop
context. Initial restricted-shell queries could not reach AT-SPI; permitted
version/help queries worked and list-apps could enumerate desktop applications
with a connection warning. Those observations establish installed tools,
not traversal of this target. No running Orca instance or preferences were
replaced. Static HTML semantics and PDF page inspection remain distinct
evidence. PDF `Tagged: no` is the documented print-companion limitation;
no tagging, PDF/UA or accessible reading-order claim is made.

After binding the brief and all audit matrix rows to the real content commit,
the independent reviewer ran:

- `python3 -I scripts/check/primer_evidence.py primer_codex_for_claude_code_users/primer_codex_for_claude_code_users.brief.md primer_codex_for_claude_code_users/primer_codex_for_claude_code_users.audit.md`: pass.
- `python3 -I scripts/check/primer_audit.py --repo-root . --project primer_codex_for_claude_code_users`: pass; reported source SHA256 exactly matches the reviewed/committed source.
- `git diff --check`: pass.

The full pipeline's final build, render, freshness and link results are owned
and reported by the coordinator; these successful binding checks alone do
not replace them or the unavailable interactive checks.

`docs/publication-accessibility.md` explicitly includes these interactive
checks in release evidence. They remain the release blocker; byte identity,
an accessibility-tree inventory or installed screen-reader tooling cannot
substitute for actual traversal. No rendering infrastructure or PDF-tagging
change is proposed by this issue. Next action: establish the supported browser
connection, then record actual keyboard, no-JavaScript, tree and Orca results
with tool versions. Until then, content passes and release is **not-ready**;
main can open the authorised draft PR with this limitation visible.

## Historical Post-Maintenance Integration Review

- Source and reviewed revision: `48562529f6413d07f3189e75d436984f51ee547c`; SHA256 `5d7780a7e79b3770f2f85103f8c636375706de2bf814b5e74d142bfc3f870619`.
- Brief: `codex-operating-model-v3`; audit: `codex-operating-model-audit-v3`.
- Compared with: original content `c8a4b57096bd8faf0659c37df412565be728fa8a` and relocated main `8190dd96003c11d6ed91a419c0aa50f3ff54591d`.
- Reviewer: Codex independent content reviewer at high effort, with separate publication verification; 15 November 2026.

The whole-source re-audit followed all five taught routes and all 12 stable
concept rows, including the bounded reference row. The prior depth judgement
remains pass: actions, reasoning, interpreted results and material limits are
present. The subsequent differential review inspected the actual path changes
at 818–819 and 2324 and their discovery/migration context. Four empty inline
spans at 996, 1000, 1844 and 2394 preserve published section fragments and
lead to the corresponding role-routing, custom-agent translation and
operational-record passages. Removing those spans leaves only the three path
changes. No teaching prose or scenario changed; all route/concept IDs and
tiers, the case contract and the 48 locator line numbers remain intact.

Current risk-selected primary-source checks reconfirmed [configuration
precedence and project trust](https://learn.chatgpt.com/docs/config-file/config-basic#configuration-precedence),
[`review_model` scope](https://learn.chatgpt.com/docs/config-file/config-reference),
[subagent model resolution, open-thread counting and inherited permissions](https://learn.chatgpt.com/docs/agent-configuration/subagents),
and [worktree separation](https://learn.chatgpt.com/docs/environments/git-worktrees).
These are documentation checks, without deployed settings, hook, model,
migration or permission execution. Earlier catalogue, interoperability and
remote/data checks retain their original dates and scope. The earlier eight
TOML-fence syntax checks are retained because those fences are unchanged;
this continuation does not claim new runtime execution of the teaching case.

The target `all` build and `just render-qa` pass through relocated pinned
infrastructure. The HTML retains every one of the 408 draft IDs and every
published-main heading ID, including the four legacy fragments. Removed
code-block and TOC-control IDs were generated controls for deleted headings,
not published section fragments. The 94-page PDF was visually inspected on
pages 1, 31, 33, 47 and 67, including actual table and code material; no
page-edge clipping was observed. There are no figures or equations. Code-page
raster hashes were identical before and after the anchor repair. PDF metadata
reports `Tagged: no`, the documented print-companion limitation; no PDF/UA,
tagged reading order or accessible-PDF claim is made.

The supported Browser connection was retried in this continuation. Selection
returned `No browser is available`; documented recovery listed `[]`.
Keyboard, no-JavaScript, browser accessibility-tree and representative
screen-reader traversal remain **not checked**. Earlier installed Orca/AT-SPI
observations are historical tool-availability evidence only, not a current
traversal. Static HTML semantics and PDF inspection cannot close this gate.
The governing policy is now `maintenance/docs/publication-accessibility.md`.
The user authorises conditional merge, but the unresolved release gate keeps
PR #436 draft and #435 open. **Content gate: pass. Release readiness: not-ready.**

The current sequential pipeline completed successfully:

- `just primer-audit primer_codex_for_claude_code_users`: exit 0; structural and Git-backed binding, pinned build, render QA, freshness and scoped Markdown/HTML links pass.
- `just lint-changed`: exit 0; no enforced findings, with existing prose advisories; all 59 offline publication/README link baselines are clean.
- `just check`: exit 0; tests, metadata, variants, Mermaid, 31 source/output freshness pairs and README consistency pass.
- `git diff --check`: exit 0.

The pipeline rebuilt PDF differs only in creation-time metadata and a two-byte
size change: extracted text is byte-identical and pages 31/67 have identical
raster hashes. Pages 1/33/47 were inspected again without observed clipping.
The reviewed source, HTML and PDF from 48562529 are retained byte for byte;
the metadata-only rebuilt PDF was not substituted. This is reproducible
content/layout evidence, not byte-for-byte PDF build reproducibility. The
brief/audit wording corrections after the pipeline change no source, example
or output; lightweight validators and scoped Markdown were rerun separately.

## Release Acceptance and Policy Applicability

- Review date: 16 November 2026.
- Reviewed source remains `48562529f6413d07f3189e75d436984f51ee547c` with SHA256 `5d7780a7e79b3770f2f85103f8c636375706de2bf814b5e74d142bfc3f870619`.
- Compared evidence: v3 at `c338d771f09e9dbe892c2bfedd5305c36031e2d4`; v4 changes only the tracked brief/audit and integrates the separately reviewed #439 policy.
- Current policy: `maintenance/docs/publication-accessibility.md`, issue #439 and merged PR #440, adopted at `58f2194e9dd534dc86e03770e3a043d51b5e1cce` and integrated into this branch at `4bd0110`.
- Owner acceptance: the owner inspected the served preview, accepted it, approved the narrower policy, and instructed the coordinator to merge the remaining PRs.

The source, case, examples and required HTML/PDF are byte-identical to the
reviewed content commit. The content gate, 12 stable concept rows, tiers,
route transitions and 48 locator line numbers therefore retain their prior
independent review evidence. This is a fresh release-scope review, not a new
claim of whole-source or illustrative-scenario execution.

Independent applicability review compared #436 with relocated main 8190dd9.
The shared template, heading filter, navigation/control implementation and
HTML/PDF rendering flags are unchanged; only the primer date differs in its
Justfile. The source does change the heading outline and contents entries.
Four old heading fragment IDs now belong to empty spans at the beginnings of
corresponding paragraphs (996, 1000, 1844 and 2394). Their IDs survive and the
replacement material is relevant, but those four locations no longer appear
as headings or contents entries. All draft IDs and published-main heading IDs
remain present. This establishes target existence and relevant content, not
equivalent browser focus, scrolling or screen-reader behaviour.

Under the explicitly scoped #439 policy, this is ordinary content, outline
and legacy-fragment maintenance using existing rendering components.
Interactive checks are advisory for this scope. No known broken interaction
or fragment link was identified by the structural, source, output or owner
preview reviews. Keyboard, no-JavaScript, browser accessibility-tree and
representative screen-reader traversal remain **not performed**, with their
behaviour unverified. The unavailable browser connection and earlier tool
availability findings retain their original dates and limits. Advisory status
does not retroactively turn them into passes. The PDF remains an untagged
print companion; no PDF/UA, tagged reading-order or comprehensive HTML
accessibility claim is made.

Final verification on 16 November 2026 after policy integration at `4bd0110`:
`just primer-audit primer_codex_for_claude_code_users`, `just lint-changed`,
`just check` and `git diff --check` all exited 0. The audit recipe reran
structural and Git-backed evidence checks, the pinned-container HTML/PDF
build, render QA, freshness and scoped Markdown/link checks. The repository
checks covered 31 source/output pairs; offline links across 59 files had zero
enforced or advisory failures. Existing review-only prose advisories remain.
Logs are retained in `.scratch/435/final-*.log` in the integration checkout.
Visual evidence and unchanged-source content reviews retain their stated
scope. The rebuilt PDF differed only in its creation timestamp and file size
according to `pdfinfo`; extracted text and raster SHA256 values for pages 1,
31, 33, 47 and 67 were identical to the reviewed committed PDF. That committed
PDF was restored after comparison, leaving source, HTML, PDF and case
byte-identical to `48562529`. The PDF remains untagged. The owner accepted the preview, and the current policy makes the
remaining unperformed interactive checks non-blocking for this scope.
Content gate: **pass**. Release readiness: **ready**, with policy integration
and current-head CI confirmed before the authorised merge.

## Pilot learning

- False positives: initial concern that the running case only listed acceptance requirements was resolved by inspecting the integrated pseudocode trace and scoped correction; no executable fixture is required by the declared illustrative promise.
- Missed issues: none recorded after the resolved configuration, lifecycle and sequencing findings; publication defects can still trigger another review.
- Procedure changes proposed: none; do not alter validators or policy to make uncommitted source appear bound.
- Remaining work: coordinator confirms current-head CI and completes the authorised merge, then synchronises main. Policy #439 is adopted and integrated. Advisory interactive checks remain explicitly not performed.
- Final decision: ready for the authorised release after policy integration and current-head CI; the illustrative content gate passes with no unresolved primary or alternative teaching gap.
