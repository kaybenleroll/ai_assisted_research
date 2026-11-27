# Primer brief: Pi Coding Agent

- Issue and milestone: #442, current-documentation refresh, after Codex #441.
- Brief revision: pi-current-docs-v1
- Source revision: db93a99128b8424698f73c321d24e624d578b7ac
- Tracked path: primer_pi_coding_agent/primer_pi_coding_agent.brief.md
- Reader: experienced Claude Code user evaluating, configuring and supervising Pi for a bounded repository task.
- Prerequisites: terminal, Git, repository instructions and basic Claude Code concepts; TypeScript reading helpful for extension route.
- Problem and motivation: similar coding agents have different model, tool, extension and authority boundaries; readers must establish what Pi actually loads and can do before assembling a workflow.
- Intended outcome: explain the harness, choose authentication and models, run and verify a supervised task, select integrations deliberately, manage sessions, and identify containment and reproducibility boundaries.
- Scope: retain substantive current primer coverage, examples, headings and link targets; correct supported stale claims and make verification limitations explicit. Follow the migration and data-project routes without claiming they were executed in this refresh.
- Exclusions: exhaustive feature catalogue, benchmarking, actual provider billing verification, live model/tool execution, third-party security audit, production deployment, completed Rocker project or measurement of model quality.
- Proposed dependency-led route: harness and controlled first run → model/authentication → automation or customisation as needed → research and session continuity → security boundaries → Rocker integration → comparative lookup. Each taught route exposes input, decision, result, interpretation and limit.
- Approximate depth: retain the existing practical explanation and code, including meaningful limitations and examples. Depth follows the decisions; no quota.
- Worked examples: disposable read-only first session, authentication and local model setup, bounded RPC/SDK illustrations, extension and MCP snippets, search and session handoff, restricted Podman Rocker fixture.
- Real-world cases: a synthetic daily-temperature analysis demonstrates agent versus analysis-container responsibility; do not imply a real dataset or model outcome.
- Teaching-case contract: primer_pi_coding_agent/primer_pi_coding_agent.case.md
- Worked-case trace: route-keyed table below; coherent smaller examples teach routes that precede or do not fit the case.
- Core-concept depth matrix: this brief, stable IDs below.
- Route classification and teaching spines: first-run, models, automation, customisation, research, sessions, containment and rocker are primary; comparison is reference-only. Each has its own motivating problem, operation, interpretation and boundary in the trace.
- Figures, tables, equations: retain existing control flow, comparison and workflow tables; no new figure needed.
- Languages and executable examples: Markdown, shell, JSON, Python, TypeScript, Dockerfile, Just. Published snippets illustrative unless a precise separate test is recorded; fake RPC event tests validate a prototype only, not Pi or provider operation.
- Evidence plan: primary Pi docs and changelogs, product and package source, registry evidence, separately labelled historical checks. Source map `.scratch/2026-11-19-pi-current-audit.md` and `pi-rpc-prototype-evidence.md`; verify claim-specific links. Image index and npm retrieval are verified by main's read-only registry check, not image execution or package review. Build and render in pinned repository containers.
- Open decisions: No blocking planning decisions. Include the tested single-prompt RPC prototype with explicit fake-stream versus live-runtime boundaries. Align the publication date to primary-document checks. Exact web-access source security review and Pi/provider runtime remain unperformed.

## Review plan

- Whole-document checks: current claims, preserved substantive coverage, examples and cross-references; record exact findings and output revisions.
- Representative samples: authentication warnings, early RPC events and error paths, extension return result, browser security, trust/telemetry, fixture and Rocker build, dense tables and rendered pages.
- Planned independent reviewers: validate current source claims and route-depth separately; render reviewer checks HTML/PDF and visual samples.
- Content gate: each primary route has its intended input, decision, operation, intermediate result, interpretation and limit; trace case without substituting unrun code for evidence.
- Depth gate: reject tool/feature catalogues where the reader cannot make and justify the promised decision.
- Post-draft checkpoint: compare each route to its trace and record exact source locators and decisions in the tracked brief before audit.
- Case acceptance: match fixture, expected result, acceptance logic and host/container boundary; distinguish illustrated snippets, historical test and current tests; identify unprovided artefacts and correction path.
- Scope acceptance: retain original explanatory and case coverage; optional comparisons remain lookup and cannot displace primary routes. No unsupported claim of execution or uniform availability.

## Worked-Case Trace

| route_id | stage | case input or prior result | decision, operation, or observed result | output handed onwards | stage mode | planned evidence or check |
|---|---|---|---|---|---|---|
| first-run | input through interpretation and boundary | Disposable repo and a tool-capable model | Select `--no-mcp` and read-only tools, inspect loaded context, then supervise one edit and compare Git diff | Independently reviewed change or diagnostic of failed layer | illustrative | Current CLI/security docs; no live session implied |
| models | input through interpretation and boundary | First run needs hosted or local model | Choose provider/auth, inspect readiness then test tool support; prevent stale credentials overriding intended key | Selected model and qualified provider configuration | illustrative | Current providers, models, llama.cpp docs; account-specific billing unverified |
| automation | input through interpretation and boundary | Same bounded review prompt | Choose print, JSON, RPC or SDK; consume message and settlement status, handle handled/queued/error | Result or explicit unresolved failure for independent review | illustrative | CLI integration/RPC/SDK docs; prototype tested only with fake subprocess streams |
| customisation | input through interpretation and boundary | Recurring task or missing integration | Select instruction, skill, template, extension, package or MCP based on execution and authority; review source | Narrowly enabled capability | illustrative | Current skill, extensions, package and MCP docs; illustrative URL and package placeholders |
| research | input through interpretation and boundary | Need current package documentation for Rocker case | Direct source for known URL, reviewed search skill or enabled Radius for discovery, then inspect primary source | Dated source handoff with uncertainty | illustrative | pi-skills source, Radius docs and explicit data paths; no live search run |
| sessions | input through interpretation and boundary | Research session and resulting URLs | Name, branch, compact or hand off; inspect summary and sharing destination | Reviewed handoff note, not an assumed full context | illustrative | Session and compaction docs; no transcript uploaded |
| containment | input through interpretation and boundary | Agent/task runs with host access and analysis code needs isolation | Distinguish trust, callable tools and OS controls; compare host Pi with constrained analysis container | Reviewable boundary and access decision | illustrative | Current security/containerisation/settings docs; no security guarantee |
| rocker | input through interpretation and boundary | Fictional CSV, expected rows and analysis contract | Agent edits code; digest-pinned image and tests would compare R/Python outputs; inspect independent check and configuration diff | Conditional acceptance or rejection and correction | illustrative | the tracked case contract; fixture arithmetic by inspection, image index identity confirmed, runtime not run in this refresh |

## Optional Branches and Unresolved Concepts

| route_id | optional branch | reader need | worked evidence added | material displaced or shortened | scope decision and reason |
|---|---|---|---|---|---|
| comparison | Agent comparisons | Locate migration differences | Current source-linked capability table | No expansion into feature catalogue | Retain reference-only; product and account behaviour changes |
| models | Local models and llama.cpp | Avoid confusing model with endpoint | Router setup and layered diagnosis | No exhaustive provider catalogue | Retain bounded alternative within model route |
| research | Browser and hosted web search | Select appropriate access and exposure | CDP trust and Radius enablement | Avoid duplicating general search instructions | Retain, qualify macOS launcher and source review |

| route_id | concept_id | unresolved gap | decision and reason | effect on reader outcome |
|---|---|---|---|---|
| automation | rpc-completion | Existing sample mishandles early completion and handled prompt | Expand illustration around disposition, final status, timeout and explicit single-prompt limitation | Reader can distinguish acceptance, completion and error |
| customisation | tool-errors | Returned `isError: true` works as well as throwing | Correct with official extension reference | Reader can report tool failure correctly |
| research | third-party-pin | Registry existence does not establish reviewed package source | Narrow claim to version identity, cite no security review | Reader understands install requires own review |
| rocker | case-runtime | Full project inputs and current execution missing | Narrow to illustrative fixture and historical test; list missing assets explicitly | Reader understands what must be supplied to reproduce |

## Post-draft teaching-depth checkpoint

- Draft source revision: c193c88ce7f16a2145c4be27dd53f7feb6668422
- Brief revision reviewed: pi-current-docs-v1

The coordinator followed all eight primary routes against their planned traces after drafting and before final audit. Source locators below refer to `primer_pi_coding_agent/primer_pi_coding_agent.md`. All planned concept IDs/tiers are retained. The RPC block exactly matches the tested scratch prototype; synthetic protocol tests do not execute Pi. The complete Rocker workflow remains illustrative, with missing implementation assets made explicit in the reader-facing source.

| route_id | brief trace or teaching device | draft locators and transition findings | decision and rationale | scope reduction and effect on reader promise |
|---|---|---|---|---|
| first-run | Disposable supervised task | Lines 127–159 restrict tools, inspect discovery, authorise one edit, inspect actual Git diff and diagnose the failing layer. | Retain coherent first-loop example. | None. |
| models | Provider/readiness decision and local endpoint | Lines 165–233 explain credential precedence, account metering uncertainty, endpoint selection and layered tool-call checks. | Retain documented connection choices; no account result promised. | None. |
| automation | Single-prompt event lifecycle | Lines 263–380 distinguish acceptance/handled/settlement and final failure; RPC code retains early events and imposes deadline; SDK completion caveat explicit. | Expand actual lifecycle example and limits; prototype identity checked with synthetic failures. | No live-provider promise; no arbitrary concurrent-run correlation. |
| customisation | Minimal layer plus word-count tool | Lines 382–537 compare instructions versus code, show tool mechanism and error result, and explain in-process gates versus selective MCP. | Correct error/schema facts while retaining concrete code and authority explanation. | None. |
| research | Source lookup, search and handoff | Lines 539–636 use pinned source URL, reviewed-skill workflow and browser/RPC/service choice; macOS paths and package review limits explicit. | Retain worked selection and source-handoff spine. | No package security review or live search claimed. |
| sessions | Branch, compact, share or hand off | Lines 642–688 explain on-disk versus active context, branch effects, summaries and sensitive sharing destinations. | Retain decisions and factual note for continuation. | None. |
| containment | Host process versus analysis runtime | Lines 690–746 distinguish trust, tools and OS isolation; lines 920–972 instantiate mounts/network/output policy and protected-host review. | Retain mechanism and concrete boundary failure. | None. |
| rocker | Fixture through conditional acceptance | Lines 774–973 declare missing files, compute expected values, prewrite contract/comparator, assign Pi tasks, pin environment, restrict mounts and reject unsupported acceptance. | Expand arithmetic and protected comparator review, retain all recipes. | Case remains illustrative; no complete supplied application or fresh runtime pass. |

## Core-concept depth matrix

| route_id | route tier | concept_id | concept | reader action | mechanism or reasoning | significance | teaching device | worked evidence | interpretation | limitations | downstream use | Evidence/source plan |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| first-run | primary | harness-control | Harness and loop | Orient then supervise one edit | Model requests tools; harness executes under process authority | Diagnose the right layer | Disposable first session | Restricted tool command and Git diff | Tool selection affects available calls | Not OS isolation | Safe model and workflow selection | Pi CLI and security docs |
| models | primary | provider-auth | Provider and model | Select credentials and check model readiness | Provider protocol, credential precedence and tool-call compatibility differ | Avoid false readiness and unexpected billing | Hosted/local decision | API key, login, local endpoint and small tool probe | Readiness is not tool quality | Provider and account limits vary | First run and automation | Providers, models, llama.cpp, Anthropic primary docs |
| automation | primary | rpc-completion | Programmatic lifecycle | Choose mode and classify completion | Response accepts prompt; events report settlement and final stop reason | Prevent silent failures | Single-prompt RPC sequence and SDK comparison | Fake streams for normal, early, handled and failure | Settled is not success | Example is illustrative, events lack command ID | Reliable integration | RPC, JSON, SDK references and prototype evidence |
| customisation | primary | extension-boundary | Resource and extension choices | Choose minimal customisation | Instructions guide; extensions execute and tools return results | Review executable authority | Skill, tool and MCP example | `isError` or throw; selective server exposure | Capability comes with process access | In-process gate is not sandbox | Safe research and custom workflow | Skills, extensions, MCP and package docs |
| research | primary | source-discovery | Current evidence | Retrieve and verify primary information | Search finds leads; direct sources support claims | Avoid stale or invented answers | Search skill and dated handoff | Known raw URL, Brave or Radius option | Source and observed capability are distinct | Third-party code and query exposure need review | Rocker research | pi-skills source, Radius docs, pin identity |
| sessions | primary | session-continuity | Branches and compaction | Preserve decisions across runs | Active context is a branch and summaries replace older prompt context | Avoid losing essential constraints | Branch and handoff example | `/tree`, `/compact`, reviewed note | Original on disk does not mean model sees it | Summaries and uploads may expose or omit data | Implement and hand off | Sessions and compaction docs |
| containment | primary | trust-isolation | Authority and isolation | Choose process and container boundary | Trust gates resources; OS controls actual access | Prevent confusing prompts with enforcement | Host Pi versus restricted analysis container | `--no-mcp` and rootless mounts | Analysis isolation does not restrict host agent | Mounts, network and credentials define exposure | Supervised and unattended runs | Security, settings, containerisation docs |
| rocker | primary | reproducible-case | Analysis acceptance | Apply fixture and validate both implementations | Contract, locked environment and independent comparison separate expectations from model output | Make results reviewable | Synthetic temperature project | Two A readings mean 5.70; B 3.40; missing-only group excluded | Expected rows are conditional on unprovided cleaners/tests | No current full case run; bootstrap and host agent remain risks | Adapt project with supplied code and locks | Rocker digest and reproducibility sources; case contract |
| comparison | reference-only | agent-comparison | Agent lookup | Find a starting migration comparison | Products differ in bundled defaults and controls | Avoid assumed feature parity | Dated comparison table | Pi, Claude Code, Codex, OpenCode and Aider | Verify actual version and permissions | Not a benchmark or exhaustive catalogue | Select targeted official documentation | Current primary product docs |

## Issue #473: first-run baseline amendment

For source SHA-256 `aa9d213fd1787ea29e248c28998095dae9db76ea1ab8fee3f4f81b4dfb2b1340`, retain the `first-run` / `harness-control` route and its illustrative Pi boundary. The disposable repository now starts with a committed README using a command-local identity; the reader verifies the initial commit and compares both staged and unstaged tracked changes against it, then inspects untracked files separately. The baseline and diff commands can be tested without running Pi or a provider. Earlier revision and locator references remain historical.
