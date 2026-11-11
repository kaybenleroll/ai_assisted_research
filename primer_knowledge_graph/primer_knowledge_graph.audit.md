# Primer audit: Building Knowledge Graphs: From Sources to Verifiable Queries

- Issue and milestone: #398; related #397
- Audit revision: `kg-398-depth-audit-r6`
- Source revision: `a02df70`
- Tracked path: `primer_knowledge_graph/primer_knowledge_graph.audit.md`
- Starting branch: `docs/398-knowledge-graph-finish`
- Reviewer(s): Codex, with two read-only comparative reviews
- Date: 11 November 2026
- Reviewed revision: `a02df70`
- Brief reviewed: `primer_knowledge_graph/primer_knowledge_graph.brief.md`, `kg-398-brief-r3`
- Review boundary: complete source, brief, case, executable manifest and committed HTML/PDF; human depth review and structural checks performed; full citation and accessibility review remain outstanding
- Teaching-case contract: `primer_knowledge_graph/primer_knowledge_graph.case.md`
- Core-concept depth matrix: 14 stable route/concept rows in the tracked brief
- Readiness decision: not-ready
- Readiness note: content gate passes; release readiness remains not-ready because source, accessibility, and handoff evidence is incomplete.

This audit supersedes `kg-398-depth-audit-r5`. Earlier executable and render
evidence is retained only where the source and implementation remain unchanged;
the new standalone section, consolidated route, and changed locators required a
fresh audit after the revision. That fresh audit is recorded below. The unrelated working-tree change to
`mise.toml` is outside this review.

## Whole-document review

| Area | Scope and method | Evidence | Status | Finding | Disposition |
|---|---|---|---|---|---|
| Brief coverage and scope | Whole-document comparison against the tracked brief | Source lines 3–1040; brief r3 | verified | The brief now promises a standalone conceptual route, with implementations as companion evidence. | Recheck after final prose edits. |
| Explanatory depth | Whole-document reading plus reader-scale section review | New graph section lines 32–144; source-to-answer walkthrough lines 344–390 | verified | The central concept and one complete construction/use/query thread are now explicit. | Continue expanding only where a reader transition remains unsupported. |
| Structure and fragmentation | Heading inventory and adjacent-section reading | 12 H2 sections; consolidated claim, extraction, provenance, and optional projection branches | verified | Fragmentation is materially reduced; reference material remains intentionally denser. | Retain this hierarchy unless a later reader review finds a broken route. |
| Technical claims and calculations | Risk-selected comparison with the existing executable evidence | Temporal policy lines 557–582; path interpretation lines 344–390 and 816–868 | retained | Existing bounded-date, conflict, abstention, and lossy-projection claims remain applicable. | Rerun examples after final source/output changes. |
| Examples and reader action | Hand-worked tables and end-to-end source-to-answer trace | Lines 56–81 and 344–390; Northbridge Q1–Q5 lines 150–167 | verified | The reader can follow a direct assertion, a two-hop path, and an unresolved identity without opening repository files. | Keep the implementation route subordinate to the conceptual route. |
| Sources and freshness | Inventory only; no complete citation-by-citation refresh | Further reading lines 1040–1047; inline source links | not-checked | Primary-source verification is incomplete after the substantive revision. | Required before release. |
| Outputs and accessibility | HTML/PDF regenerated; representative visual pages inspected | Render-QA report for a02df70; opening, source table, code, query, correction and governance pages | verified | No clipping or unreadable layout was found in the inspected pages. Automated accessibility review remains outstanding. | Keep accessibility separate from content approval. |
| Privacy, limitations, and governance | Whole-document reading | Privacy lines 428–468; governance lines 997–1039 | verified | Limits remain explicit: synthetic sources, unresolved identity, no production access enforcement, no universal engine claim. | Preserve these boundaries. |

## Reader-scale depth review

Length is used as a diagnostic signal, not a quota. Each major section was
checked for an opening teaching job, a reasoning spine or worked thread, a
reader operation or interpretation, and a material limit.

| Section | Teaching job and worked spine | Reader-use evidence | Limit | Disposition |
|---|---|---|---|---|
| Introduction | Establish audience, standalone promise, build/use split, and scope | Lines 7–28 | Orientation cannot teach the operation itself | retain |
| What a Knowledge Graph Is—and When It Helps | Explain graph versus edge list, qualified evidence, and when a graph helps | Lines 34–144, especially the hand-worked graph at 56–81 | Storage choice remains workload-dependent | retain as the new conceptual anchor |
| Define the Boundary Before Building the Graph | Turn questions and source roles into bounded contracts | Lines 150–218; Q2 reasoning at 168–200 | Synthetic source set is incomplete | retain |
| Represent Evidence, Entities, and Qualified Claims | Connect mentions, identifiers, claims, assertions, time, and polarity | Lines 231–265 | The local IDs are synthetic and source locators are not complete documents | retain as one consolidated frame |
| Build Conservatively and Resolve Identity with Abstention | Move from candidate evidence to accepted or refused claims | Lines 271–343 | Narrow patterns are not a general extractor | retain |
| Work one claim from source to answer | Make the entire construction and query transition explicit | Lines 344–390 | The answer depends on the stated source boundary and policy | retain as primary worked thread |
| Preserve Provenance, Time, Conflict, and Uncertainty | Explain why source, time, disagreement, and uncertainty travel together | Lines 400–427 | No historical release record in the fixture | retain |
| Privacy and Proportionate Identity | Show that an unresolved identity also changes disclosure | Lines 428–468 | Access rules are illustrative | retain |
| Use the Graph: From Claims to Interpreted Queries | Separate direct, path, temporal, and provenance operations from storage syntax | Lines 469–582 | The tabular implementation remains bounded | retain; recheck after final code removal decision |
| Optional Representations | Compare RDF, property graphs, R projections, and storage boundaries | Lines 583–868 | Reference snippets and Neo4j route are unexecuted; R projection is lossy | retain as reference-only/alternative branch |
| Validate, Evaluate, and Diagnose | Distinguish valid records, supported claims, evaluation, and repair | Lines 869–996 | Synthetic evaluation is not population accuracy | retain |
| Maintain, Evaluate, Release, and Govern | Trace corrections and dependencies into release responsibility | Lines 997–1039 | Durable release and retraction machinery are proposed | retain |

## Teaching-case trace

| Case stage | Evidence | Execution status | Finding or limitation |
|---|---|---|---|
| Input and assumptions | Northbridge sources and Q1–Q5 contracts, lines 150–167 | illustrative | Synthetic records do not establish real-world completeness. |
| Construction decision | Source-to-candidate table and walkthrough, lines 293–390 | illustrative in the prose; executable companion retained | The reader can reproduce the reasoning without running code. |
| Intermediate representation | Qualified claim table, lines 73–76 and 231–265 | illustrative | Source, interval, polarity, and unresolved mentions remain distinct. |
| Stored/computed result | Evidence ledger and result table, lines 515–582 | executed evidence retained from prior audit; prose re-reviewed | Temporary DuckDB files do not constitute a durable release. |
| Reader-facing query | Direct, path, temporal, and provenance operations, lines 538–582 | illustrative in the main route; executable companion retained | A path is not a new claim, and an unknown horizon is not continuity. |
| Interpretation | Walkthrough and limitations, lines 344–390 and 557–582 | illustrative | Results are bounded by source scope and answer policy. |
| Failure and limit | Alex abstention, conflict, absence, and privacy, lines 201–218, 271–292, 428–468 | illustrative | No production access-control or general NLP claim is made. |

## Route transition evidence

| route_id | concept_id(s) | transition (from to) | linked input and reader operation | intermediate reasoning or decision | result | interpretation | material limitation | execution status | gap and reader consequence |
|---|---|---|---|---|---|---|---|---|---|
| route-python-duckdb | kg-boundary, kg-mentions | source boundary → question | Q1–Q5 identify source, date, relation, evidence, and refusal scope, lines 150–167 | The answer contract fixes source selection before traversal | Bounded questions and refusal rules | The answer is limited to the selected source scope | The fixture is synthetic and incomplete | illustrative | No gap; without this boundary the reader cannot interpret absence or authority. |
| route-python-duckdb | kg-claims, kg-temporal | mention → qualified claim | The hand-worked source sentence becomes `c5` with polarity, interval, horizon, source, and locator, lines 344–356 | Mention and assertion are kept distinct; negative evidence survives | A query can return the competing assertion with its evidence | The result remains a source-backed assertion, not universal truth | Temporal meaning is an encoded case assumption | illustrative | No gap; without qualifiers the reader cannot interpret conflict or date. |
| route-python-duckdb | kg-extraction, kg-correction | candidate → accepted/refused construction | Narrow patterns preserve spans and distinguish acceptance, rejection, and abstention, lines 293–343 | A changed or missing candidate points to extraction rather than storage | A source-derived claim or explicit refusal | The decision can be diagnosed and rerun | Not a general NLP pipeline | illustrative | No gap in the bounded case; general extraction remains outside scope. |
| route-python-duckdb | kg-duckdb, kg-queries | claims → direct/path query | Return claim IDs for direct and two-hop operations, lines 538–556 | Join only the declared predicates and retain both hop IDs | Version → Atlas → Northbridge is a path, not a new claim | The path is useful for structure, not authority | Main prose is storage-neutral; implementation is bounded | illustrative | No gap; an undated path cannot support an as-of conclusion. |
| route-python-duckdb | kg-temporal, kg-queries | query → temporal aggregation | Classify each matching assertion as outside, applicable, indeterminate, or invalid, lines 557–582 | Apply the end-kind contract before aggregation | Conflict and uncertainty produce abstention | The result reports the selected policy outcome | The policy is not universal authority logic | illustrative | No gap; omitting this step would permit unsupported certainty. |
| route-python-duckdb | kg-privacy, kg-evaluation | unresolved result → disclosure/evaluation decision | Report the unresolved Alex mention and audience-specific answer contract, lines 271–292 and 428–468 | Do not invent identity or expose restricted candidates | A bounded disclosure or abstention | The answer contract changes with audience and evidence access | Access rules and labels are illustrative | illustrative | No gap; production enforcement is explicitly outside scope. |
| route-r-projection | kg-r-projection | positive edge list → topology result | Analyse the declared positive projection for paths and components, lines 816–868 | Interpret unit cost and weak connectivity as topology | Path and component results | The result is a structural summary of the projection | Dates, polarity, provenance, and claim IDs are lost | illustrative | No gap for the alternative; it cannot answer evidence questions. |
| route-graph-storage | kg-rdf, kg-property, kg-storage | qualified claim → representation choice | Compare RDF and property-graph mappings against the same evidence fields, lines 591–815 | Choose storage from question, workload, provenance, and operations | A future serving decision | The comparison informs a design choice, not a tested winner | No service execution or benchmark | illustrative | No gap for reference-only scope; implementation would require a separate route. |

## Adversarial depth gate

The stable IDs and route tiers are retained from brief r3. The following rows
record the fresh content judgement at source revision `a02df70`; they do not
claim that the implementation examples or every citation have been rerun.

| route_id | route tier | concept_id | explanation locator | example/action locator | interpretation locator | limitation locator | evidence revision | reviewer | status | finding | scope decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| route-python-duckdb | primary | kg-boundary | `primer_knowledge_graph/primer_knowledge_graph.md:146` | `primer_knowledge_graph/primer_knowledge_graph.md:150` | `primer_knowledge_graph/primer_knowledge_graph.md:201` | `primer_knowledge_graph/primer_knowledge_graph.md:214` | a02df70 | Codex | verified | Questions and source roles bound the answer before construction. | Synthetic bounded case retained. |
| route-python-duckdb | primary | kg-mentions | `primer_knowledge_graph/primer_knowledge_graph.md:231` | `primer_knowledge_graph/primer_knowledge_graph.md:236` | `primer_knowledge_graph/primer_knowledge_graph.md:344` | `primer_knowledge_graph/primer_knowledge_graph.md:382` | a02df70 | Codex | verified | Mentions, entities, and unresolved Alex candidates are kept distinct. | Synthetic identifiers only. |
| route-python-duckdb | primary | kg-claims | `primer_knowledge_graph/primer_knowledge_graph.md:244` | `primer_knowledge_graph/primer_knowledge_graph.md:73` | `primer_knowledge_graph/primer_knowledge_graph.md:344` | `primer_knowledge_graph/primer_knowledge_graph.md:382` | a02df70 | Codex | verified | The claim/assertion distinction and qualified evidence are worked through. | No claim of source completeness. |
| route-python-duckdb | primary | kg-temporal | `primer_knowledge_graph/primer_knowledge_graph.md:250` | `primer_knowledge_graph/primer_knowledge_graph.md:557` | `primer_knowledge_graph/primer_knowledge_graph.md:567` | `primer_knowledge_graph/primer_knowledge_graph.md:578` | a02df70 | Codex | verified | Bounded, unbounded, and unknown horizons lead to distinct classifications. | Domain-valid time is a teaching assumption. |
| route-python-duckdb | primary | kg-extraction | `primer_knowledge_graph/primer_knowledge_graph.md:271` | `primer_knowledge_graph/primer_knowledge_graph.md:293` | `primer_knowledge_graph/primer_knowledge_graph.md:344` | `primer_knowledge_graph/primer_knowledge_graph.md:339` | a02df70 | Codex | verified | Source spans, narrow patterns, refusals, and identity abstention are connected. | No general NLP extractor. |
| route-python-duckdb | primary | kg-duckdb | `primer_knowledge_graph/primer_knowledge_graph.md:515` | `primer_knowledge_graph/primer_knowledge_graph.md:519` | `primer_knowledge_graph/primer_knowledge_graph.md:538` | `primer_knowledge_graph/primer_knowledge_graph.md:532` | a02df70 | Codex | verified | The ledger schema and implementation boundary are explained without making them the main route. | Temporary local storage only. |
| route-python-duckdb | primary | kg-queries | `primer_knowledge_graph/primer_knowledge_graph.md:538` | `primer_knowledge_graph/primer_knowledge_graph.md:344` | `primer_knowledge_graph/primer_knowledge_graph.md:557` | `primer_knowledge_graph/primer_knowledge_graph.md:552` | a02df70 | Codex | verified | Direct, path, temporal, and provenance operations return evidence and interpretation. | Undated paths cannot answer as-of questions. |
| route-python-duckdb | primary | kg-correction | `primer_knowledge_graph/primer_knowledge_graph.md:1020` | `primer_knowledge_graph/primer_knowledge_graph.md:913` | `primer_knowledge_graph/primer_knowledge_graph.md:997` | `primer_knowledge_graph/primer_knowledge_graph.md:1039` | a02df70 | Codex | verified | The correction route remains bounded and the Python example passed after the source revision. | Retain bounded correction scope; no durable release claim. |
| route-python-duckdb | primary | kg-evaluation | `primer_knowledge_graph/primer_knowledge_graph.md:913` | `primer_knowledge_graph/primer_knowledge_graph.md:930` | `primer_knowledge_graph/primer_knowledge_graph.md:950` | `primer_knowledge_graph/primer_knowledge_graph.md:996` | a02df70 | Codex | verified | Evaluation prose distinguishes synthetic measures from population accuracy; the Python example passed. | Synthetic measures remain illustrative. |
| route-python-duckdb | primary | kg-privacy | `primer_knowledge_graph/primer_knowledge_graph.md:428` | `primer_knowledge_graph/primer_knowledge_graph.md:441` | `primer_knowledge_graph/primer_knowledge_graph.md:458` | `primer_knowledge_graph/primer_knowledge_graph.md:468` | a02df70 | Codex | verified | Disclosure, minimisation, and false-negative risks are worked through the unresolved identity case. | No enforced production access control. |
| route-r-projection | alternative | kg-r-projection | `primer_knowledge_graph/primer_knowledge_graph.md:816` | `primer_knowledge_graph/primer_knowledge_graph.md:833` | `primer_knowledge_graph/primer_knowledge_graph.md:868` | `primer_knowledge_graph/primer_knowledge_graph.md:868` | a02df70 | Codex | verified | The alternative remains conceptually bounded and its R example passed after the source revision. | Keep lossy projection as alternative. |
| route-graph-storage | reference-only | kg-rdf | `primer_knowledge_graph/primer_knowledge_graph.md:591` | `primer_knowledge_graph/primer_knowledge_graph.md:608` | `primer_knowledge_graph/primer_knowledge_graph.md:650` | `primer_knowledge_graph/primer_knowledge_graph.md:650` | a02df70 | Codex | verified | RDF claim/assertion mapping explains why qualifiers need explicit representation. | Unexecuted reference design. |
| route-graph-storage | reference-only | kg-property | `primer_knowledge_graph/primer_knowledge_graph.md:736` | `primer_knowledge_graph/primer_knowledge_graph.md:753` | `primer_knowledge_graph/primer_knowledge_graph.md:773` | `primer_knowledge_graph/primer_knowledge_graph.md:787` | a02df70 | Codex | verified | Property-graph convenience is contrasted with evidence loss and claim nodes. | No pinned Neo4j execution. |
| route-graph-storage | reference-only | kg-storage | `primer_knowledge_graph/primer_knowledge_graph.md:788` | `primer_knowledge_graph/primer_knowledge_graph.md:805` | `primer_knowledge_graph/primer_knowledge_graph.md:815` | `primer_knowledge_graph/primer_knowledge_graph.md:815` | a02df70 | Codex | verified | Workload, update, provenance, and operations determine storage choice. | No benchmark or universal winner. |

## Release readiness checklist

| Gate | Decision | Evidence or remaining work |
|---|---|---|
| Brief and audit binding | pending | Brief content is r3 and source-bound to a02df70; audit metadata must be committed and mechanically checked. |
| Content gate | pass | The fresh whole-document depth review, route trace, stable-ID matrix, executable examples, and representative visual inspection pass. |
| Stable route/concept IDs | pass | Existing tiers and IDs are preserved in brief r3 and this audit. |
| Examples | pass | Both opted-in Python and R examples pass in their pinned runtimes. |
| HTML/PDF and freshness | pass | Outputs were rebuilt; freshness, render QA, and representative visual inspection pass. |
| Accessibility | not-checked | Run automated checks and inspect tables, text diagrams, headings, and code/optional-branch pages. |
| Sources | not-checked | Complete citation-by-citation primary-source verification. |
| Links | pass | Scoped offline links pass after the heading and anchor changes. |
| Final handoff | pending | Record exact commands, review boundary, limitations, and release decision. |

- Content gate: **pass**
- Release readiness: **not-ready**

## Execution boundary

The source and outputs were changed in commit `a02df70`. The content gate is
now passed on the basis of the fresh whole-document review, both executable
examples, the repeatable audit, and representative visual inspection. Release
readiness remains not-ready until citation-by-citation source verification,
automated accessibility review, and the final handoff are complete.
