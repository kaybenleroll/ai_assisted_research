# Primer audit: Pi Coding Agent

- Issue and milestone: #442; current-documentation refresh after Codex #441.
- Audit revision: pi-first-run-473-v1.
- Audit schema: 2
- Source revision: 629d566
- Reviewed revision: 629d566
- Source SHA256: 2da79108a2f215417efac09acdb315d2f0460efb96885aa8b218d44984c448c2.
- Tracked path: primer_pi_coding_agent/primer_pi_coding_agent.audit.md
- Starting branch: docs/442-pi-current-refresh.
- Reviewer(s): Codex independent content reviewer, gpt-6.1-sol/high; separate documentation researcher and publication coordinator.
- Date: 2026-11-19.
- Brief reviewed: primer_pi_coding_agent/primer_pi_coding_agent.brief.md, pi-current-docs-v1.
- Core-concept depth matrix: brief pi-current-docs-v1; all nine stable IDs and unchanged tiers (eight primary, one reference-only).
- Teaching-case contract: primer_pi_coding_agent/primer_pi_coding_agent.case.md.
- Review boundary: complete 1022-line baseline source and complete brief/case/research evidence read; complete refreshed diff, changed passages and dependent routes reviewed at 340fc52, then final three source corrections reread at c193c88. Current primary-documentation and synthetic RPC evidence supplied by separate researcher/main. No live Pi/provider, package-security or complete Rocker execution.
- Readiness decision: not-ready

**Historical #442 decision: content gate passed and release readiness was ready**, following the coordinator’s verification recorded below. The current #473 structural review remains outstanding and supersedes that historical readiness decision. Earlier pending statements describe the independent reviewer’s draft checkpoint and are superseded by that verification. All eight primary routes supply actual reasoning, action, interpreted result and material limit. Source line ranges below refer to `primer_pi_coding_agent/primer_pi_coding_agent.md` at the reviewed commit. Current output checks and synthetic protocol tests do not certify live provider behaviour or execute the illustrative Rocker case.

## Whole-document review

| Area | Scope and method | Exact evidence or location | Status | Finding or gap | Disposition |
|---|---|---|---|---|---|
| Brief coverage/scope | Complete baseline reading, current diff and nine-ID comparison | 5–21;127–233;235–380;382–746;774–973 | verified | Existing explanation, examples, recipes and reference routes retained; no route demoted to clear a finding. | Retain nine IDs/tiers and declared illustrative scope. |
| Technical claims | Full inventory plus separate primary-documentation comparison | 178–180;263–380;466;517;661–663;784–840 | verified | Credential/schema/error/lifecycle/compaction claims corrected within supported scope; fixture arithmetic checked by inspection. | No exhaustive implementation/billing/runtime guarantee. |
| Sources/freshness | Researcher's source map and actual edited-claim reconciliation | 3/11; documentation map below | verified | Pi 1.5.2 documentation baseline and latest-doc redirects explicit; exact historical version examples remain dated. | Preserve package, registry and provider limits separately. |
| Explanatory depth/prerequisites | Continuous reading, all primary paths and concept gate | Section and transition tables below | verified | Baseline RPC and case construction/acceptance gaps resolved in actual prose/code. | Retain complete worked paths and boundary explanations. |
| Structure/dependency order | Full outline and section-boundary review | 23–101;161–233;382–688;690–973 | verified | Harness model precedes tools/provider choices; minimal customisation synthesis follows examples; safety prepares concrete case. | No broad consolidation needed; reference branches intentionally concise. |
| Examples/interpretation | Automation state machine and fixture-to-acceptance trace | 265–380;820–840;844–869;923–973 | verified | Reader sees early/handled/error decisions, group arithmetic, independent expected result and conditional acceptance. | Fake-stream results are not actual Pi wire/provider tests; case missing assets explicit. |
| Applications/limits | Whole-source and dependent-path review | 141/153;207–233;267/361/380;702–746;776/917–973 | verified | Tool selection, process access, provider readiness, transcript sharing and host/analysis boundaries are distinct. | No claimed containment/security equivalence. |
| Tables/code/accessibility meaning | Source structure and current reported render evidence | 239–245;527–533;712–717;784–840;925–956 | verified | Tables support decisions; code fenced; no source figures/equations. | Output/visual evidence recorded separately; no interactive accessibility claim. |
| HTML/PDF/metadata | Main's current pinned build/render reports | Publication evidence below | verified | Required outputs regenerated; IDs retained and deterministic semantics pass as reported. | Final suite and final page observations remain coordinator-owned. |
| Residual uncertainty | Explicit scope reconciliation | 3/11,267/361/380,592/600–603,776/873/923/971–973 | verified | No live accounts, credentials, endpoint, extensions, sandbox, third-party source audit or full case run claimed. | Preserve limitations in release note. |

## Teaching-case trace

| Case stage | Source or section | Evidence and result | Execution status | Gap or limitation |
|---|---|---|---|---|
| Input/assumptions | 776,782–787,823–829 | Fictional five-row CSV, validation/grouping/sort/tolerance contract; host Pi versus analysis container. | illustrative | Missing cleaners/tests/comparator/locks listed before use. |
| Construction decision | 784–787,832,840 | Reject malformed/unknown/empty/nonnumeric required input; discard missing, group date/station; prewrite expected result and comparator. | illustrative | Not a supplied runnable implementation. |
| Intermediate representation | 832 | A's two valid readings total11.4, mean5.70, min5.10/max6.30; B one value gives3.40. | illustrative | Arithmetic hand-checked; no container calculation implied. |
| Stored/computed result | 833–837,840 | Independent expected CSV; hypothetical R/Python output paths consumed by comparator. | illustrative | Expected values are not observed generated files. |
| Reader operation | 844–869,873–918,925–969 | Assign bounded implementation, pin runtime/locks, run tests/pipeline under declared mounts, compare each output to independent expected file, inspect actual host diff. | illustrative | Reader supplies implementations/locks; image retrieval is not image execution. |
| Interpretation | 964–971 | Accept only after actual independent tests/comparison and protected-file review pass; disagreement or weakened gate cannot establish acceptance. | illustrative | One fixture and agent-authored tests do not prove universal correctness. |
| Failure/scope limit | 917–918,958–973 | Moving renv bootstrap, mounts/network/user and host agent authority constrain reproducibility/containment. | illustrative | No full current run; historical toy QA explicitly separate at923. |

## Brief and example traceability

| Promise | Actual teaching device | Interpretation and scope |
|---|---|---|
| first-run/models | Disposable controlled loop127–159; hosted/local/readiness path165–233 | Actual diff/tool evidence required, readiness not model/tool quality or billing proof. |
| automation | Mode comparison239–265; explicit single-prompt state machine267–359; SDK363–380 | Handled/started/queued, settlement and final stop separate; SDK prints text without claiming application success. |
| customisation/research | Minimal mechanism382–537; pinned source/search/browser choices539–636 | Guidance versus process code and data paths explained; package identity not source security review. |
| sessions/containment | Branch/summary/handoff642–688; trust/tool/OS and container choices690–746 | Disk history not model context, conversation branch not filesystem rollback, trust not sandbox. |
| rocker | Independent contract/input/expectation782–840 → bounded implementation844–869 → environment873–956 → actual acceptance964–973 | Supplies teaching design, not complete copy-and-run project or fresh execution. |
| comparison | Lookup748–772 | Bounded descriptions, no empirical ranking or uniform feature parity. |

## Reader-scale section depth

The complete baseline was read continuously, then changed passages and their dependent teaching paths were reread at the current revisions. Each section advances a distinct task or is retained for a deliberate orientation/reference/synthesis purpose. No word/heading quota was used.

| Major section / route hosts | Teaching job and reasoning spine | Application/interpretation | Material limit | Disposition |
|---|---|---|---|---|
| Short Version5–21 | Expert-reader orientation, scope and navigation | 13 | 15–21 | retain; retain clear illustrative/missing-assets scope and current verification boundary without adding headings. |
| How Pi Works23–101 | Model/harness/tools/environment → loop → minimalism rationale → migration mapping | 38–50,80–101 | 68–76,93–101 | retain; organising model precedes feature choices and historical design remains separate from current capability. |
| Installation103–159 | Install alternatives/platforms → controlled first loop → terminal steering | 129–153 | 123–125,141,159 | retain; action, expected evidence and layer-specific failure recovery are already substantial. |
| Models161–233 | Authentication precedence → hosted/local decision → protocol config/router → staged readiness | 178–188,207–233 | 180,207–209 | retain; local troubleshooting is dependency-led, not endpoint catalogue. |
| Non-interactive235–380 | Choose interface → command acceptance versus settlement → separate SDK embedding | 263–380 | 261,361,380 | retain; actual RPC state machine now teaches disposition, early settlement, final stop and failure/deadline; SDK remains explicitly minimal lifecycle illustration. |
| Customisation382–537 | Guidance→template→skill→code→package/MCP → minimal-mechanism decision | 386,466–537 | 487,503,517–523 | retain; error-result/schema correction preserves the concrete tool; examples and final synthesis prevent catalogue-only treatment. |
| Research539–636 | Known source before discovery → reviewed skill → hosted/browser alternatives → primary-source interpretation | 545–590,626–636 | 592–603 | retain; corrected source-review/browser claims, keep clear data paths and narrow-account limitations. |
| Sessions638–688 | Persistent tree → branch actions → compacted model context → private handoff → workflow | 659–688 | 661–667 | retain; concise commands and note complement actual explanation. |
| Safety690–746 | Trust versus tool exposure versus OS reach → choose boundary → credential/network/telemetry limits | 702–740 | 704–706,717,746 | retain; explains meaningful asymmetries, including host extensions outside Gondolin. |
| Comparison748–772 | Bounded migration lookup and implementation relationships | 762–772 | 766,772 | retain reference-only; no feature-rank expansion. |
| Rocker774–973 | Contract/input→independent expected result→bounded agent phases→pinned runtime→mounts→acceptance | 821–869,925–973 | 917–919,971–973 | retain; numeric contract, worked arithmetic, protected comparator/diff and historical/missing-assets scope now explicit. Recipe and environment depth preserved. |
| Reference975–1074 | Troubleshooting order, configuration map, glossary and annotated sources | 981–1018 | 984–997 | retain; intentionally bounded lookup route supported by preceding teaching. |
| Closing1076–1082 | Synthesis and sensible trial sequence | 1080–1082 | 1080 | retain; closing 1082 now explicitly requires supplying missing files before applying checks. |

## Route transition evidence

All reader-facing transitions remain illustrative: no Pi/provider or full case operation ran. Exact published RPC code was exercised only against synthetic subprocess streams, separately recorded under execution evidence.

| route_id | concept_id(s) | transition (from to) | linked input and reader operation | intermediate reasoning or decision | result | interpretation | material limitation | execution status | gap and reader consequence |
|---|---|---|---|---|---|---|---|---|---|---|
| first-run | harness-control | New installation→supervised change | Disposable Git repo129–136, chosen model140, restricted orientation141 | Inspect loaded context/trust142 before restarting for named edit143 | Independent status/diff/check144 supplies accept/reject evidence151 | Tool support, loaded instructions and file contract are separate151 | Extensions retain host authority141; steering cannot undo started command159 | illustrative | Complete; setup failures diagnosed by layer153. |
| models | provider-auth | Model need→qualified connection | Hosted login/key165–180 or compatible endpoint194–205/router218–231 | Stored credential can beat exported key178; choose supported protocol188 | Check auth/health/chat/stream/tool roundtrip207/233 | Endpoint availability and chat response do not establish tool quality207 | Actual billing180, context/protocol207, external data paths209 | illustrative | Complete bounded choice; no account/provider result asserted. |
| automation | rpc-completion | Mode choice→prompt disposition | Select mode239–265; subscribe/drain before write285–300 | Correlate responseID, distinguish started/queued/handled311–318 | Handled returns no model answer325–326; other dispositions feed settlement test327 | Acceptance/handling is not model completion265/267 | Fresh single-prompt/no independent runs assumption267; events lack promptID | illustrative | Baseline handled hang/early-event race repaired in actual state machine. |
| automation | rpc-completion | Started run→classified result | Remember assistant message/early settlement319–324, then check327–339 | Reject abort/missing message/non-stop reason328–338 | Completed result or explicit exception; deadline/EOF/stream/UI errors300–310 | Final stop means protocol completion, not factual/task correctness361 | No arbitrary shared-run correlation267; production backpressure/UI/lifecycle limits361 | illustrative | Complete within declared example scope; fake stream tests separate. |
| automation | rpc-completion | Integration choice→SDK lifecycle | Choose RPC separate process or SDK in-process363/380; explicit cwd/in-memory session369–377 | Await prompt then print text; dispose in finally372–377 | Text/lifecycle illustration, not success assertion | Prose363 requires final-message stopReason before using as success test | Host trust/credentials and opt-in extensions/MCP binding380 | illustrative | Sufficient minimal SDK comparison; RPC supplies detailed outcome teaching. |
| customisation | extension-boundary | Repeated need→narrow capability | Compare guidance/template/skill/code386–423, concrete count tool438–463 | Use executable tool/gate only when required466–487; source-review package503 | Registered tool/controlled call or selectively exposed MCP507–519 | Minimal mechanism decision523–537; process authority remains | Error/schema correction466; regex gate not sandbox487; MCP not containment517 | illustrative | Complete, no package/extension execution claimed. |
| research | source-discovery | Current question→evidence handoff | Retrieve known versioned raw source545–554 or search skill558–590 | Review selected source/helper/dependencies, choose Brave/Radius/browser data path567–613 | Source table/request572–578 and repository/source check626–636 | Search results are leads626; read primary current source636 | Exact third-party audit592, browser trust600–603, hosted terms594 | illustrative | Complete; immutable placeholder is a planning instruction, not an audited pin. |
| sessions | session-continuity | Research output→continuation | Name/branch session644–661; compact preserve instructions663 | Distinguish current branch/model summary from original on-disk history659/663 | Reviewed note670–678 feeds implementation685/861 | Summary is not original evidence678; branch does not undo files659 | Sensitive sharing destination667; summaries may omit detail663 | illustrative | Complete, no transcript upload or lossless-memory promise. |
| containment | trust-isolation | Host access→chosen boundary | Classify trust/tools/OS694–706, choose process boundary710–740 | Tools/MCP exposure and resource loading do not enforce filesystem/network | Restricted analysis runtime930–959 has RO inputs and writable outputs | Host Pi remains outside this boundary776/971 | Credentials740, instruction trust exception704, offline not firewall746 | illustrative | Complete; comparator and boundary-file review969 protect acceptance from host edits. |
| rocker | reproducible-case | Input→independent expected output | Contract784–787 and fixture823–829 | Discard missing/group; work A/B statistics832 | Expected rows834–837 feed independent comparator840 | Expected file precedes candidate implementation844 | Nonnumeric/date/flag failures784/840; missing-only group785 | illustrative | P1/P2 resolved; arithmetic hand-checked, not runtime output. |
| rocker | reproducible-case | Expected contract→candidate analysis | Committed gate844, bounded read/research/implement845–869 | Independent R/Python code from contract; digest873 and locks907–918 | Restricted QA/pipeline942–955 would create R/Python outputs | Mounts and independent expectations make returned result reviewable958 | Missing files776/923, renv bootstrap917, host Pi971 | illustrative | Complete design; no copy-and-run/full-project execution promise. |
| rocker | reproducible-case | Candidate→conditional acceptance | Actual tests/comparison964–968 and actual Git status/diff969 | Verify protected comparator/config/fixtures unchanged; reject unsupported completion971 | Accept fixture only if checks actually pass971 | Agreement means declared fixture checks, not universal correctness869/973 | Host can weaken container/gate971; private data not made safe by analysis container973 | illustrative | P3/P4 resolved; input/gate preservation and historical-run boundary explicit816–817/923/1082. |

## Adversarial depth gate

The historical #442 depth review remains in Git history. These current-revision rows are explicitly not checked: their semantic locators and independent depth decisions require a fresh pass. IDs and tiers remain unchanged.

| route_id | route tier | concept_id | explanation locator | example/action locator | interpretation locator | limitation locator | evidence revision | reviewer | status | finding | scope decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| first-run | primary | harness-control | primer_pi_coding_agent/primer_pi_coding_agent.md:29 | primer_pi_coding_agent/primer_pi_coding_agent.md:141 | primer_pi_coding_agent/primer_pi_coding_agent.md:151 | primer_pi_coding_agent/primer_pi_coding_agent.md:159 | 629d566 | Codex scoped reviewer | not-checked | Current semantic locator and independent depth review outstanding; prior decision is historical. | Retain route/tier and explicit verification boundary. |
| models | primary | provider-auth | primer_pi_coding_agent/primer_pi_coding_agent.md:178 | primer_pi_coding_agent/primer_pi_coding_agent.md:194 | primer_pi_coding_agent/primer_pi_coding_agent.md:207 | primer_pi_coding_agent/primer_pi_coding_agent.md:180 | 629d566 | Codex scoped reviewer | not-checked | Current semantic locator and independent depth review outstanding; prior decision is historical. | Retain route/tier and explicit verification boundary. |
| automation | primary | rpc-completion | primer_pi_coding_agent/primer_pi_coding_agent.md:265 | primer_pi_coding_agent/primer_pi_coding_agent.md:267 | primer_pi_coding_agent/primer_pi_coding_agent.md:361 | primer_pi_coding_agent/primer_pi_coding_agent.md:380 | 629d566 | Codex scoped reviewer | not-checked | Current semantic locator and independent depth review outstanding; prior decision is historical. | Retain route/tier and explicit verification boundary. |
| customisation | primary | extension-boundary | primer_pi_coding_agent/primer_pi_coding_agent.md:386 | primer_pi_coding_agent/primer_pi_coding_agent.md:438 | primer_pi_coding_agent/primer_pi_coding_agent.md:535 | primer_pi_coding_agent/primer_pi_coding_agent.md:487 | 629d566 | Codex scoped reviewer | not-checked | Current semantic locator and independent depth review outstanding; prior decision is historical. | Retain route/tier and explicit verification boundary. |
| research | primary | source-discovery | primer_pi_coding_agent/primer_pi_coding_agent.md:545 | primer_pi_coding_agent/primer_pi_coding_agent.md:560 | primer_pi_coding_agent/primer_pi_coding_agent.md:626 | primer_pi_coding_agent/primer_pi_coding_agent.md:592 | 629d566 | Codex scoped reviewer | not-checked | Current semantic locator and independent depth review outstanding; prior decision is historical. | Retain route/tier and explicit verification boundary. |
| sessions | primary | session-continuity | primer_pi_coding_agent/primer_pi_coding_agent.md:644 | primer_pi_coding_agent/primer_pi_coding_agent.md:647 | primer_pi_coding_agent/primer_pi_coding_agent.md:663 | primer_pi_coding_agent/primer_pi_coding_agent.md:667 | 629d566 | Codex scoped reviewer | not-checked | Current semantic locator and independent depth review outstanding; prior decision is historical. | Retain route/tier and explicit verification boundary. |
| containment | primary | trust-isolation | primer_pi_coding_agent/primer_pi_coding_agent.md:692 | primer_pi_coding_agent/primer_pi_coding_agent.md:733 | primer_pi_coding_agent/primer_pi_coding_agent.md:740 | primer_pi_coding_agent/primer_pi_coding_agent.md:704 | 629d566 | Codex scoped reviewer | not-checked | Current semantic locator and independent depth review outstanding; prior decision is historical. | Retain route/tier and explicit verification boundary. |
| rocker | primary | reproducible-case | primer_pi_coding_agent/primer_pi_coding_agent.md:782 | primer_pi_coding_agent/primer_pi_coding_agent.md:823 | primer_pi_coding_agent/primer_pi_coding_agent.md:832 | primer_pi_coding_agent/primer_pi_coding_agent.md:776 | 629d566 | Codex scoped reviewer | not-checked | Current semantic locator and independent depth review outstanding; prior decision is historical. | Retain route/tier and explicit verification boundary. |
| comparison | reference-only | agent-comparison | primer_pi_coding_agent/primer_pi_coding_agent.md:750 | primer_pi_coding_agent/primer_pi_coding_agent.md:752 | primer_pi_coding_agent/primer_pi_coding_agent.md:762 | primer_pi_coding_agent/primer_pi_coding_agent.md:772 | 629d566 | Codex scoped reviewer | not-checked | Current semantic locator and independent depth review outstanding; prior decision is historical. | Retain route/tier and explicit verification boundary. |

## Sources, freshness and residual limits

The researcher read the complete baseline source/companions and checked named volatile topics against primary documentation. This reviewer reconciled that source map with actual edits, rather than independently reopening every URL. Detailed notes are `.scratch/2026-11-19-pi-current-audit.md` and `.scratch/refresh-2026-11-19/pi-rpc-prototype-evidence.md`; essential durable scope is recorded here.

| Topic | Primary sources and supported result | Verification boundary |
|---|---|---|
| Release/install/platforms | [Pi 1.5.2](https://pi.dev/changelog/releases/1.5.2), [quickstart](https://docs.pi.dev/latest/quickstart), [CLI](https://docs.pi.dev/latest/cli): baseline, installer/npm trade-off and terminal auth | Documentation only; no Pi install/login/platform execution. |
| Provider/models | [Providers](https://docs.pi.dev/latest/providers), [models](https://docs.pi.dev/latest/models), [llama.cpp](https://docs.pi.dev/latest/llama-cpp), [Anthropic plan statement](https://support.claude.com/en/articles/15036540-use-the-claude-agent-sdk-with-your-claude-plan): hosted/local and subscription uncertainty | No billing/provider/model/endpoint/tool-quality test. |
| Automation | [CLI integration](https://docs.pi.dev/latest/cli-integration), [RPC](https://docs.pi.dev/latest/rpc), [commands](https://docs.pi.dev/latest/rpc-commands), [JSON](https://docs.pi.dev/latest/json), [SDK](https://docs.pi.dev/latest/sdk): dispositions/settlement/final status, print limit error, SDK retry/completion and extension binding | Exact prototype fake tests/AST separate; no actual wire/provider or TypeScript compilation/execution. |
| Extensions/resources | [Extensions](https://docs.pi.dev/latest/extensions), [1.5.0](https://pi.dev/changelog/releases/1.5.0), [skills](https://docs.pi.dev/latest/skills), [packages](https://docs.pi.dev/latest/packages), [MCP](https://docs.pi.dev/latest/mcp): structured error flag, schema coercion, resource/exposure controls | No extension/tool/gate/server run or third-party security audit. |
| Research/browser | pi-skills [Brave source](https://github.com/badlogic/pi-skills/tree/main/brave-search), [browser source](https://github.com/badlogic/pi-skills/tree/main/browser-tools), [Radius](https://radius.earendil.com/docs/extensions): source helper options, macOS launcher, default-off hosted search, dependency≠activation | Main-branch source inspected, no immutable audited commit claimed. No live search/browser/cookie/Radius-account operation; terms/retention unverified. |
| Sessions/compaction/security | [Sessions](https://docs.pi.dev/latest/sessions), [compaction](https://docs.pi.dev/latest/compaction), [security](https://docs.pi.dev/latest/security), [settings](https://docs.pi.dev/latest/settings), [environment](https://docs.pi.dev/latest/environment-variables), [containers](https://docs.pi.dev/latest/containerization): branch/sharing, summary trigger/output and trust/telemetry/offline scope | No uploaded session, network capture, enforced allowed/blocked probe or guarantee for every deployment. |
| Rocker/registries | [Rocker reproducibility](https://rocker-project.org/use/reproducibility.html), [Podman](https://docs.podman.io/en/stable/markdown/podman-run.1.html), [renv/Docker](https://rstudio.github.io/renv/articles/docker.html), [pip hashes](https://pip.pypa.io/en/stable/topics/secure-installs/); main read GHCR/npm registries | Pinned index body hash and Linux amd64/arm64 entries confirmed; npm 0.40.0 identity exists. No image pull/build/run, complete project or exact-package security audit. |
| Comparisons/history | Current source-linked product descriptions and earlier dated anecdotes | Bounded reference inventory, not live cross-agent comparison, adoption audit or performance ranking. Historical pinned v1.3.0 sources and October toy QA stay historical. |

The npm existence check does not establish reviewed code. The registry digest verifies the referenced index, not the moving tag's present identity or successful runtime. The renv bootstrap remains a moving dependency despite the lockfile. Local models do not make tool/extension traffic local. These limits are substantive conditions for using the methods.

## Snippet and execution provenance

| Snippet/calculation | Current evidence | What it establishes | Unperformed |
|---|---|---|---|
| Published RPC Python269–359 | Main compared exact code to `pi_rpc_example.py`, parsed AST and reran `python3 -W error::ResourceWarning -m unittest discover -s .scratch/refresh-2026-11-19 -p 'test_pi_rpc_example.py' -v` | Four test methods/12 synthetic scenarios pass without ResourceWarning: normal,early,queued,handled,rejected,provider-error,abort,missing-message,malformed-JSON,EOF,UI,timeout | No Pi/provider wire behaviour; production/shared-run correlation, stream-size/backpressure/UI remain out of scope. |
| Other shell/JSON/TypeScript/Dockerfile/Just snippets | Illustrative source review | Intended choices, sequence and caveats | No compilation/native activation/server/credential/container workflow execution. |
| Temperature fixture832–837 | Hand inspection of2 valid A values and1 B value | Sum11.4/count2→mean5.70; B3.40; declared missing-only exclusion | No actual R/Python generated results. |
| Rocker toy QA923 | Historical October edition report | Earlier report retained explicitly as historical | Not rerun or substituted for current case execution. |

Reader-facing route transitions stay `illustrative` because their input is an actual Pi/provider/project operation. The fake-stream test is separately `executed` on a prototype with synthetic subprocess inputs; it cannot change a live route's execution status.

## Revision-triggered second audit

This is the first tracked audit for Pi. The baseline scratch review preceded source revision and found concrete automation/case gaps; the current tracked judgement includes a genuine second pass after those repairs.

| Previous and current revisions | Changed artefacts/passages | Affected concepts/transitions | Review and result | Remaining consequence |
|---|---|---|---|---|
| Baseline f18f0dd→340fc52 | Source/Justfile/output refresh; verification3/11, auth178/180, RPC263–380, error/schema466, MCP517, search592–603, sessions661–663, case776/784/832/840/873/968–970, current links | All nine IDs inventoried; automation/customisation/research/sessions/containment/Rocker changes and dependent first-run/model paths | Complete baseline1022-line read, complete 458-line diff read in nontruncated follow-ups, changed passages and dependent routes reread. Event-state and P1/P2 repairs support content pass; P3/P4 final wording follow-up below. | No actual Pi/provider or full case run inferred. |
| 340fc52→c193c88 | Source816–817 protects comparator in agent instructions;923 labels toy QA historical/no current run/missing files;1082 requires supplying missing files. Outputs regenerated. | containment/trust-isolation, rocker/reproducible-case and opening/closing promise | Actual three-hunk diff plus existing gate840/844, actual diff969, host-authority971 and source776 scope re-reviewed. Independent gate, historical evidence and runnable-scope claims now agree. | No unresolved primary content gap; final checks/visual evidence pending coordinator. |

## Retained evidence and reconciled findings

| Evidence/finding | Current disposition | Reason/current locator |
|---|---|---|
| Baseline organising model, credential ordering, tool/OS boundaries and session reasoning | Retained and reread through dependencies | Unchanged teaching remains applicable at current locators; not promoted to execution. |
| RPC early/handled/provider/deadline gaps | Resolved | 267–361 subscribes/drains first, remembers settlement, separates handled, rejects final failures and applies deadline; constraints explicit. |
| P1 numeric validation | Resolved within promised scope | 784 explicitly rejects nonnumeric required values. A finite/NaN/Inf specification was a stronger recommendation, not a prior promise; no guarantee beyond the stated contract is inferred. |
| P2 unworked expected fixture | Resolved | 832 supplies A/B intermediate arithmetic before independently written expected rows. |
| P3 host edits/diff/protected comparator | Resolved | 816–817 and969 protect comparator; actual status/diff separates intended host source edits from unexpected changes;971 explains unenforced host authority. |
| P4 missing assets/historical run/closing implication | Resolved | 776 lists missing implementation assets and no refresh run;923 historical report;1082 instructs supplying missing files. |
| Old TypeScript tool-error/browser/package-review claims | Corrected with primary evidence | 466 structured errors/schema;592 historical pin/registry versus security;600/603 launcher/dependency scope. |
| Synthetic RPC and registry checks | Newly supplied evidence | Exact code/AST/fake streams and registry retrieval are distinct, precisely bounded evidence. |
| Prior publication/historical toy execution | Historical only | No older render/test/report used as current content/runtime proof. |

## Publication and representative sampling

Main reports the pinned target `all` build and `just render-qa primer_pi_coding_agent` pass and regenerated required HTML/PDF. The current known report uses Pandoc 3.11 and image 61d7d31cd74fba20b6ac708c108fa8879f3a7106b9f0226f30debe2be130771a; Poppler 25.12.0 supplies PDF extraction/rasterisation. Main reports 413 current HTML IDs, all baseline IDs retained, and no duplicates by exact JSON comparison. This reviewer inspected available build/render evidence; final c193c88 page observations are recorded below; the complete check suite remains pending main. Build/rendering this publication does not run Pi or Rocker examples.

| Sample | Risk and method | Current result/limit |
|---|---|---|
| Opening5–21 | Scope, old/current versions and illustrative boundaries | Source pass; missing-assets statement776 qualifies later case. |
| Difficult automation263–380 | Follow disposition/event/outcome and SDK comparison | Source pass; fake tests support prototype branches only. |
| Extension466/487 and browser592–613 | Error handling, executable authority and review provenance | Source pass; no activation/security audit. |
| Case782–840/964–973 | Follow actual input→arithmetic→expected output→independent gate→conditional acceptance | Source pass; missing implementations and fresh runtime explicit. |
| Final PDF p1,p39,p14,p34,p36,p37 | Main inspected opening, actual glossary table, RPC start, protected comparator/fixture arithmetic, historical QA/recipe and acceptance diff | Pass; no observed clipping or overflow. Unchanged RPC continuation p15/16 and contract p33 were also inspected. Figures/equations absent; fallback p21 is a starter table. |

The shared template/navigation/rendering components are unchanged ordinary content corrections. Interactive checks are advisory under `maintenance/docs/publication-accessibility.md`; keyboard, no-JavaScript, browser accessibility-tree and screen-reader traversal were **not performed**. Preserved IDs and extractable text do not prove interaction or assistive behaviour. PDF remains an **untagged print companion**, with no PDF/UA or tagged reading-order claim.

## Release readiness checklist

| Gate | Decision | Evidence/limit |
|---|---|---|
| Brief/audit binding | pass final check | Audit, brief and case bind c193c88; committed locator validation passed. |
| Route/concept gate | pass | Nine stable concept rows, eight primary routes and reference scope substantively reviewed; no unresolved primary gap. |
| Locator validity | pass final check | Human-selected exact current passages nonblank; structural/Git-backed checks passed. |
| Examples | pass stated scope | Exact RPC fake tests/AST separate; all reader-facing scenarios illustrative; no full executable manifest promise. |
| Rendered outputs | pass reported scoped build | Required output build/render pass reported; listed final visual samples pass; final complete suite passed as recorded in Coordinator final verification. |
| Accessibility | pass applicable scoped evidence | Deterministic semantics and listed final visual samples pass; interactive unperformed/advisory; PDF untagged. |
| Sources | pass scoped documentation evidence | Research map reconciled with current edits; live/third-party/historical limits explicit. |
| Links/lint/freshness | pass final suite | Main reports lint-changed pass in permitted container context; final pipeline/check passed; exact results are recorded in Coordinator final verification. |
| Revision review | pass | Baseline full reading, substantive committed diff and final three repairs genuinely reread. |
| Handoff | ready for review | Main owns final mechanical/visual evidence and release decision. |

- Content gate: **fail**; current depth rows are not checked.
- Structural gate: **not-checked**; a current whole-document structural review remains outstanding.
- Release readiness: **not-ready**

## Execution and render evidence

- Content reviewer: complete baseline source/brief/case/evidence reading, changed diff/current passage and dependent-transition review, Git/status/SHA256 and exact nonblank locator inspection. No teaching operation independently executed.
- Main/researcher: current primary-documentation checks, read-only registry identity checks, exact RPC prototype comparison/AST and four fake test methods covering 12 scenarios. No live Pi/provider/model test.
- Publication coordinator: pinned all/render QA reported pass; final listed visual samples and lint-changed pass reported; pipeline/freshness/binding/check suite passed as recorded in Coordinator final verification. Older toy QA and old source checks retain their original date.
- Deliberately unperformed: Pi install/login/provider/billing/endpoint, extension/MCP/browser activation, package security audit, OS-boundary probes, complete Rocker build/run and interactive accessibility.
- Stop: tracked audit draft and content judgement returned to main. A new source, example or output change triggers affected-scope review; metadata rebinding alone is insufficient.

## Pilot learning

Most baseline sections already teach real decisions. The weaknesses were operational links: an RPC sample could hang or misclassify success, expected rows lacked intermediate arithmetic, and host/gate verification needed clearer protection. Repair the actual decision path and state the test/scope boundary; do not replace it with catalogue detail or a false runtime pass. No word/heading quota or new validator policy was needed.

## Coordinator final verification

19 November 2026; source and all nine concept evidence rows remain bound to c193c88ce7f16a2145c4be27dd53f7feb6668422, SHA256 1a8edd490e0f3fb58f864a89da5a3d15b5fb3320aa2e20c7dd471a90e0ee0fd0. The brief and teaching-case contract were rebound to that exact commit; no route, concept, tier or reader promise changed. Corrected the intermediate-arithmetic textual locators from the preceding blank line to line 832 after inspecting the actual passage; judgement unchanged.

- `just --justfile primer_pi_coding_agent/Justfile all`: pass, pinned Pandoc/XeLaTeX container.
- `just render-qa primer_pi_coding_agent`: pass; HTML semantics, assets, PDF metadata/text and raster generation. Main inspected opening p1, glossary table p39, RPC p14–16, contract p33, final protected comparator/fixture p34, historical-runtime paragraph/recipe p36 and acceptance p37. No clipping or overflow observed. No figures/equations; fallback p21 is a starter table.
- `just primer-audit primer_pi_coding_agent`: pass after the tracked audit was present; structural evidence, Git-backed source/locator bindings, full pinned rebuild, render QA, freshness, scoped Markdown and offline links. No executable-example manifest: no opt-in full project operation ran.
- `just check`: pass with the tracked audit present; agent contract, renderer/evidence/audit tests, changed evidence bindings, metadata (31 documents), variants (31), Mermaid (51 HTML files), freshness (31 source/output pairs), generated README consistency.
- `just lint-changed`: pass; changed Markdown/prose and full offline link baseline (59 files, zero link findings). `just lint-spell` on Pi source/brief/case: pass. Final evidence prose is separately checked before commit.
- Exact published Python block: AST parse and byte equality to synthetic-tested prototype pass. Four unittest methods covering 12 synthetic scenarios pass with ResourceWarning treated as error; this does not invoke Pi or a provider.
- All baseline HTML IDs retained; 413 current IDs unique. Publication filenames and all 57 fence-aware headings retained. Required HTML/PDF outputs accompany the source commits.

Logs and raster files are in ignored `.scratch/refresh-2026-11-19/` and `.scratch/render-qa/primer_pi_coding_agent/`; this tracked record retains the results and limitations. An initial restricted-context lint attempt could not access Podman state; the identical recipe passed in the permitted container context. An early `just check` correctly stopped because the in-progress audit did not yet exist; the completed-audit rerun passed. Neither initial failure was treated as a pass.

Content gate **pass** and release readiness **ready for PR review**, without a live-provider, package-security, complete Rocker execution or interactive-accessibility claim. The independent content review remains distinct from the coordinator’s checks. Source changes require affected-route review again. Preserve source history when merging because Git-backed evidence pins depend on it.

The pipeline rebuild changed PDF binary bytes; pinned Poppler extraction compared byte-for-byte identical to the visually reviewed final PDF text (`cmp pi-final-pdf.txt pi-pipeline-pdf.txt`: pass). Source and HTML were unchanged. This is text-equivalence evidence, not a claim of binary or pixel identity. Final brief/audit schema, Git-backed binding/locator validation and `git diff --check` passed again after the audit results were recorded.

Pre-merge editorial review, 19 November 2026: source unchanged from c193c88; independent reviewer confirmed no substantive blocker or execution overclaim. Reconciled stale pending-check wording with completed coordinator verification; no concept, route, tier, source claim or output changed.

## Outline and hierarchy review

- Source read coverage: 1-150, 151-300, 301-450, 451-600, 601-750, 751-900, 901-1050, 1051-1086
- Rendered contents: **not-checked**; opening and selected PDF pages were inspected, but the whole outline and each boundary have not yet been independently assessed. `python3 -I maintenance/scripts/check/primer_outline_compare.py primer_pi_coding_agent/primer_pi_coding_agent.md primer_pi_coding_agent/primer_pi_coding_agent.html` reported no H2/H3 candidate differences; this is advisory.

## Issue #473: first-run revision review

The affected source is bound by SHA-256 `2da79108a2f215417efac09acdb315d2f0460efb96885aa8b218d44984c448c2`; the earlier commit-bound whole-document audit and its locators remain historical. The changed `first-run` / `harness-control` route at source lines 127–154 now creates a unique disposable repository, commits the README with a command-local identity, asks Pi not to commit, checks that the baseline remains HEAD, compares the tracked file with HEAD, and calls out separate inspection of untracked files. This repairs the claimed independent evidence without changing the route's illustrative status or asserting a Pi/provider run.

A disposable Git fixture executed the documented initialisation and commit, appended the example sentence, and added an untracked file. `git status --short` showed both; `git diff HEAD -- README.md` showed the added sentence both before and after staging it. No Pi or provider was run. The review is limited to this changed route and its dependent interpretation; the previous audit is not a fresh whole-document audit.

## Issues #473 and #474: comparator clarification

Source `629d566` specifies the expected header, row count, uniqueness, byte-wise order, encoding and numeric formatting, exact keys, counts and extrema, and the numerical mean tolerance. A small independent Python `Decimal` check accepted the expected A row and rejected a row with only its minimum changed from `5.10` to `5.20`. This checks that negative example, not a complete comparator or the illustrative Rocker project. Earlier row-level audit decisions are historical; the current rows are marked not-checked pending semantic locator and depth review.

## Current reader-route observations

At source `629d566`, the first-run path (127–157) gives a baseline, supervised action and independently inspectable result; the fixture exercised the Git portion only. The case (780–975) names missing assets, supplies input and independently prepared values, specifies a comparator and returns to host/container boundaries; the negative minimum check exercised one field decision only. The intermediate routes distinguish authentication (169–237), RPC outcome versus correctness (239–384), executable customisation authority (386–541), research evidence (543–640), session state versus filesystem state (642–692), and containment (694–750). The comparison (752–776) and reference (979–1078) offer lookup rather than a replacement for the practical route. These are reader observations from the complete source read, not independent verification of every claim, a row-by-row semantic locator review, or a full structural boundary verdict. The comparison placement question is separately tracked as #475.
