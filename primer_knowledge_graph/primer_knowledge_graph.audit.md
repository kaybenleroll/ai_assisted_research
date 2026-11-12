# Primer audit: Building Knowledge Graphs: From Sources to Verifiable Queries

- Issue and milestone: #398; related #397; accessibility follow-up #421
- Audit revision: `kg-398-depth-audit-r16`
- Source revision: `5924434`
- Reviewed revision: `5924434`
- Brief reviewed: `primer_knowledge_graph/primer_knowledge_graph.brief.md`, `kg-398-brief-r13`
- Tracked path: `primer_knowledge_graph/primer_knowledge_graph.audit.md`
- Starting branch: `docs/398-revise-knowledge-graph-primer`
- Reviewer(s): Codex, applying `primer-audit`
- Review boundary: source structure and depth at `5924434`, with historical execution and release evidence retained separately
- Core-concept depth matrix: brief r13, all 14 stable IDs and three route tiers
- Date: 2026-11-12
- Teaching-case contract: `primer_knowledge_graph/primer_knowledge_graph.case.md`, historical reconciliation `2d47558`
- Readiness decision: not-ready

## Current content review

Compared source `9ceb2d2` to `5924434`, brief r12 to r13 and audit r15 to
r16. Reviewed the structural changes, adjacent reasoning, primary and
alternative paths, the 14 concept passages, and the new property-graph
example against the current source. Locators below refer to Markdown at
`5924434`, not rendered pages. Source SHA-256 is
`74e0d4fb5a7add90685da8fc7f94461eeb67ce4c4d976658c0da8383144332f7`.

**Content gate: pass** for the bounded illustrative primary and alternative
routes and reference-only storage. The four-part introduction grounds terms,
ledger and graph choices before the case. Northbridge remains an orientation,
and the shortened design retains the source boundary, answer contracts and
Orion completeness counterexample. The merged evidence and question chapter
connects temporal classification to selections. Literature and dependency
chapters each retain a complete source, query, correction and limit. The
property-graph addition shows both dated outcomes and why collapsing edges
loses evidence. No blocking primary or alternative depth gap was found.
This is a content judgement, not a release or accessibility approval.

## Reader-scale section depth

| Section and IDs | Teaching job and reasoning | Application or interpretation | Limit | Disposition |
|---|---|---|---|---|
| Introduction 3–43; kg-boundary, kg-claims | Four H3s establish graph terms, evidence ledgers, modelling choices and routes. | 7–33 compares graph and ledger and motivates a modelling decision. | 35–43 defines background and scope. | retain; expanded orientation gives the first case a usable vocabulary. |
| Northbridge 45–115; primary | Orient the complete source-to-release chain. | 87–115 covers answer, failure, disclosure and release. | 47–49 and 113–115 bound the synthetic case. | retain as orientation; detailed replay follows. |
| Design 117–155; kg-boundary | Consolidated boundary and answer contracts lead to the Orion counterexample. | 121–155 | 151–155 distinguishes absence from completeness. | retain; shortened reasoning still supports the design decision. |
| Evidence Ledger 157–257; kg-mentions, kg-claims, kg-extraction, kg-duckdb | Mention decisions, qualified assertions, extraction and source trace. | 180–257 | 229–235, 253–257 | retain; construction leads to inspectable evidence. |
| Interpret Evidence and Answer Questions 259–357; kg-temporal, kg-queries | One H2 links temporal classification and conflict policy to the query operations. | 263–291, 293–355 | 269–273, 350–355 | retain; continuous reasoning avoids an artificial chapter break. |
| Diagnose and Correct 358–431; kg-correction | Locate the first failure and compare three controlled passes. | 371–429 | 429–431 | retain; correction and changed sources have distinct consequences. |
| Govern Disclosure and Release 432–555; kg-privacy, kg-evaluation | Audience selection precedes scoring and regression. | 451–466, 498–552 | 530, 554 | retain; interpretation remains bounded to synthetic outputs. |
| Literature 558–646; primary transfer | Source/version/study joins, filtered results and correction. | 598–645 | 645 | retain as an independent H2; the case exposes overlapping evidence. |
| Installed Dependencies 647–754; primary transfer | Build-scoped traversal, advisory applicability, correction and comparison. | 684–753 | 696, 727–735 | retain as a separate H2; the case needs its own build and version assumptions. |
| Positive Projection 755–807; kg-r-projection | Derive a lossy view and analyse paths and components. | 761–806 | 803–806 | retain; topology does not settle the source evidence. |
| Practice 808–833; primary and alternative | Apply earlier decisions with worked answers. | 812–833 | 810, 833 | retain; exercises deliberately reuse bounded assumptions. |
| Storage 834–886; kg-rdf, kg-property, kg-storage, kg-duckdb | Four H3s cover schema, RDF, property graphs and companion implementation. | 838–877, 879–885 | 846, 863, 873, 883 | retain; the expanded property-graph example distinguishes evidence, interpretation and access. |
| Further Reading 887–893 | Signpost sources for further study. | 889–893 | References do not independently validate an implementation. | retain as a deliberately brief reference. |

## Route transition evidence

The primary and alternative paths were revisited at `5924434`. Operations
are illustrative; historical companion execution does not change their status.
Numbers in the table are current source Markdown lines.

| route_id | concept_id(s) | transition (from to) | linked input and reader operation | intermediate reasoning or decision | result | interpretation | material limitation | execution status | gap and reader consequence |
|---|---|---|---|---|---|---|---|---|---|
| route-python-duckdb | kg-boundary | source boundary to question contract | 53–55, 129–149: admit R1/M1/D1 and fix Q4 endpoints, day and sources | 123–137, 151: separate designated source role from comparison policy | Q4 contract selects the two-source proposition; passed to mention matching | 151–155: one-source applicability differs from two-source agreement | 55, 137, 153: no completeness or operational authorisation | illustrative | No gap; reader can justify admissible evidence before construction. |
| route-python-duckdb | kg-mentions | question and excerpts to shared identities | 57–59, 180–193: match version/project occurrences under M1 topic, inspect directory IDs | 180–195: issuer/context support links; Alex has no discriminator | Policy/Atlas IDs link the Q4 participants; unresolved `m-alex` feeds authorised Q5 | 195–197: identifier consistency does not prove identity; abstention preserves reviewability | 59, 182, 195: absent topic or missed candidate can defeat a link | illustrative | No gap; no forced Alex merge is required by the next assertion step. |
| route-python-duckdb | kg-claims, kg-extraction | identities and spans to qualified assertions | 61–69, 207–227: read R1 affirmation and M1 denial using accepted endpoint IDs | 215, 219–233: check meaning, negation, dates and conditions; refuse unsupported candidates | Separate `c1`/`c5`, plus `c4`, enter seven-row ledger 235–245 | 247: same proposition permits comparison without fusing source assertions | 77, 203, 229–235: completeness, independence and four curated rows | illustrative | No gap; reader can explain what was extracted, curated or refused. |
| route-python-duckdb | kg-duckdb, kg-claims | admitted rows to evidence-preserving ledger lookup | 237–257: select `c5`, follow source and locator to M1 sentence 2 and its mention | 251–257, 322: source is required; mention is optional, so `c7` survives lookup | Rows with inspectable evidence feed classification and queries | 255–257: origin, authority and evidence integrity differ; persistence is optional (881) | 253, 881–883: offsets can drift; database schema does not enforce the whole contract | illustrative | No gap within hand route; companion persistence is verified separately, not a prerequisite. |
| route-python-duckdb | kg-temporal | qualified ledger to dated evidence | 265–271: classify each row at requested day; retain polarity | 269, 283–291: same proposition/scope first, conflict before indeterminacy | `c1`/`c5` applicable on 15 March; `c5` indeterminate on 16 March (328–338) | 269, 340: applicable evidence may deny applicability; changed abstention has a changed reason | 267, 273, 279: unknown is not continuation or knowledge history | illustrative | No gap; temporal state is handed explicitly to policy, not erased by aggregation. |
| route-python-duckdb | kg-queries, kg-temporal, kg-duckdb | selection and dates to Q1/Q2/Q3/Q5 answers | 299–324: bind roles/sources; Q1 retains register rows; Q2 binds owner object; Q3 keeps both polarities; Q5 inspects `r2` | 303–314, 320–324: classify dates, preserve identity and evidence joins | Q1 date table; Morgan at snapshot with later continuity unknown; both minutes rows; unresolved Alex | 310–316, 320–324: name, time support, assertion set and review decision have different answer shapes | 308, 314–316, 322–324: no inferred continuity, cardinality or attendance edge | illustrative | No gap; the owner result does not smuggle a later valid date into evaluation. |
| route-python-duckdb | kg-queries, kg-temporal | classified Q4 rows to comparison and applicability answer | 89–95, 328–338: bind version 1/Atlas, select both sources, classify `c1`/`c5` | 91, 289, 328: opposing applicable polarities trigger disagreement then withholding | 93, 342: two-sentence citations and justified abstention; 340 explains next-day change | Comparison and applicability are separate determinations, including where one source alone is applicable | 93–95, 340–342: no true governing-policy conclusion; a different rule needs authority | illustrative | No gap; these answer records become the correction baseline at 354–356. |
| route-python-duckdb | kg-queries, kg-temporal, kg-correction | ledger joins to bounded path and impact dependency | 346: match `c1` object to `c3` subject on Atlas; reject `c7` | 348–350: keep types, source, polarity and each hop's time support | 350: path supported on 1 January, indeterminate on 1 March, outside on 1 April; dependency recorded at 356 | 348–352: node path differs from evidence-pair count and applicability propagation | 352: shared organisation does not extend version 1 to Orion | illustrative | No gap; correction can revisit the dated path as well as Q4. |
| route-python-duckdb | kg-correction | bad answer and retained span to repaired construction | 99–101, 373–391: inspect first divergence in source/candidate/admission/selection/policy/presentation | 381–387, 410–412: hold sources/date/policy fixed and restore only `c5`; boundary-test classifier separately | A supported becomes B disagreement/abstention with both rows and citations | 369, 383, 412: repair restores evidence rather than settles the dispute | 375, 387, 391: validation alone, indefinite extension or re-extraction cannot cure every later-stage defect | illustrative | No gap; repaired G-B supplies the controlled baseline for source revision. |
| route-python-duckdb | kg-correction, kg-temporal, kg-queries | repaired baseline to R2 derivations and changed answers | 408–422: replace register sentence 1, retain sentences 2/3 and snapshot context, rebuild register derivations | 414–428: preserve R1; reverify unchanged spans and classify all dependent hops | 420–428: `c1` exclusive end 1 March; `c2`/`c6` values retained with R2 provenance; Q4 refuted; 1 March path outside | 424–426: no applicable disagreement is not agreement; unchanged values still need revised evidence | 103, 430: hypothetical correction; do not overwrite old history or claim authority | illustrative | No gap; revised derivations feed release impact set at 474–478. |
| route-python-duckdb | kg-privacy | answer records and restricted identity to permitted evidence views | 107–109, 438–460: fix paired releases, approved sentences and ordinary/authorised purpose | 451–466: filter before traversal/count/citation; compare identical ordinary inputs | 457–462: same Q4, sentence lookup, fixed Q5 and zero visible links; authorised views differ | 449, 462–466: two candidate paths are not two attendees; masking labels leaks counts | 466, 488: combinations, caches and provenance still require a threat model | illustrative | No gap; audience-authorised outputs, not internal answers, become evaluation inputs. |
| route-python-duckdb | kg-evaluation, kg-privacy | permitted outputs to defined items and interpreted measures | 494–508: define assertion/answer units and audience; Pass A returns only `c1` | 498–512: distinguish retrieval from full answer and score C against its own R2 reference | 506–524: A precision 1/1, recall 1/2; B 2/2 each; coverage 2/5, policy agreement 5/5 | 508, 524: relevant returns can omit decisive evidence; definitions explain different success measures | 528–530: zero denominators, deduplication and tiny synthetic items; no empirical accuracy | illustrative | No gap; evaluation definitions specify the release regression expectations. |
| route-python-duckdb | kg-correction, kg-evaluation, kg-privacy | evaluated G-B/G-C to release acceptance record | 474–490, 534–548: compute impact from three register derivations and compare answer records | 540–552: compare boundary dates, same-value citations, changed abstention causes, dated path and paired disclosure | 540–548: Q1 gap at 1 March, Q2/c6 new evidence, Q4 refutation, changed path, unchanged undated edge | 550–552: values alone cannot establish a correct release | 490, 554, 883: named approval and live enforcement/publication need separate implementation | illustrative | No gap within agreed teaching route; no deployed release is claimed. |
| route-r-projection | kg-r-projection | ledger and entity set to positive edge view | 757–771: select six positive rows, group ordered triples, retain all eight entity IDs | 761–775: `c4`/`c6` collapse; declared vertices preserve two isolates | Five edges/eight vertices become topology input; companion independently reads fixture (806, 883) | 773–775: edge count differs from assertion count and selection does not describe activity | 761, 773, 883: polarity/time/provenance/claim IDs lost; no Python correction synchronisation | illustrative | No gap; executed R construction does not execute this ledger-to-view derivation. |
| route-r-projection | kg-r-projection | edge view to paths, components and node measures | 779–798: expand outgoing neighbours, ignore direction for weak connectivity, count in/out edges | 779–783: unit costs, no reverse route, six connected nodes and two isolates | Two-hop path, three weak components, eight strong singletons; directional degree sums five, Atlas total three | 781, 798: measures describe chosen costs and edges, not confidence or influence | 781, 798: weighted search or parallel edges can change measures | illustrative | No gap; prose supplies derivation and interpretation independently of passing R assertions. |
| route-r-projection | kg-r-projection | topology result to dated evidence interpretation | 802–804: compare same positive triple under R1/R2, then select/date-filter a new view | Unchanged undated edge versus revised `c1` outside; cross-source policy precedes decision-view projection | Original dated register edge present; corrected absent; return to Q4 ledger for cause | 802–804: unchanged topology is expected, absence can encode several causes | 804, 883: a dated label alone does not qualify each hop; companion is not synchronised | illustrative | No gap under retained alternative scope; dated analysis needs a newly constructed scoped input. |

## Adversarial depth gate

All 14 concept rows were reviewed at `5924434`; verified means sufficient
explanation, action, interpretation and limitation within the stated route.

| route_id | route tier | concept_id | explanation locator | example/action locator | interpretation locator | limitation locator | evidence revision | reviewer | status | finding | scope decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| route-python-duckdb | primary | kg-boundary | `primer_knowledge_graph/primer_knowledge_graph.md:123` | `primer_knowledge_graph/primer_knowledge_graph.md:143` | `primer_knowledge_graph/primer_knowledge_graph.md:151` | `primer_knowledge_graph/primer_knowledge_graph.md:153` | 5924434 | Codex | verified | Source roles and Q1–Q5 make evidence selection and refusal reproducible. | Retain synthetic bounded primary promise; no world-completeness claim. |
| route-python-duckdb | primary | kg-mentions | `primer_knowledge_graph/primer_knowledge_graph.md:163` | `primer_knowledge_graph/primer_knowledge_graph.md:186` | `primer_knowledge_graph/primer_knowledge_graph.md:195` | `primer_knowledge_graph/primer_knowledge_graph.md:197` | 5924434 | Codex | verified | Context/issuer support links; Alex abstention preserves the unresolved occurrence and repair evidence. | Retain; production resolution calibration is excluded in brief and source 39–43. |
| route-python-duckdb | primary | kg-claims | `primer_knowledge_graph/primer_knowledge_graph.md:201` | `primer_knowledge_graph/primer_knowledge_graph.md:237` | `primer_knowledge_graph/primer_knowledge_graph.md:247` | `primer_knowledge_graph/primer_knowledge_graph.md:215` | 5924434 | Codex | verified | Qualified source assertions preserve polarity, time, roles and comparison grain; 71–73 and 838–844 explain visual/formal distinctions. | Retain; curated rows and assumed context remain explicit (182, 235). |
| route-python-duckdb | primary | kg-temporal | `primer_knowledge_graph/primer_knowledge_graph.md:265` | `primer_knowledge_graph/primer_knowledge_graph.md:271` | `primer_knowledge_graph/primer_knowledge_graph.md:340` | `primer_knowledge_graph/primer_knowledge_graph.md:267` | 5924434 | Codex | verified | Classification, polarity, comparison and conflict-first policy remain distinct; 291 works a policy alternative. | Retain case day/exclusive-end convention; no invented continuity. |
| route-python-duckdb | primary | kg-extraction | `primer_knowledge_graph/primer_knowledge_graph.md:219` | `primer_knowledge_graph/primer_knowledge_graph.md:223` | `primer_knowledge_graph/primer_knowledge_graph.md:233` | `primer_knowledge_graph/primer_knowledge_graph.md:229` | 5924434 | Codex | verified | Worked spans lead to accepted rows; refusals distinguish uncertainty from malformed records. | Retain declared patterns and four curated rows; general NLP excluded. |
| route-python-duckdb | primary | kg-duckdb | `primer_knowledge_graph/primer_knowledge_graph.md:251` | `primer_knowledge_graph/primer_knowledge_graph.md:322` | `primer_knowledge_graph/primer_knowledge_graph.md:881` | `primer_knowledge_graph/primer_knowledge_graph.md:883` | 5924434 | Codex | verified | Required source and optional mention support hand replay including c7; optional reopen/query companion passed separately. | Retain narrowed standalone ledger promise agreed in brief r10 and contract; persistence is optional and does not enforce full semantics. |
| route-python-duckdb | primary | kg-queries | `primer_knowledge_graph/primer_knowledge_graph.md:297` | `primer_knowledge_graph/primer_knowledge_graph.md:328` | `primer_knowledge_graph/primer_knowledge_graph.md:342` | `primer_knowledge_graph/primer_knowledge_graph.md:352` | 5924434 | Codex | verified | Q1–Q5 selections and typed c1/c3 join preserve classifications, evidence and scope. | Retain illustrative operation; later ownership and Orion applicability are not inferred. |
| route-python-duckdb | primary | kg-correction | `primer_knowledge_graph/primer_knowledge_graph.md:360` | `primer_knowledge_graph/primer_knowledge_graph.md:408` | `primer_knowledge_graph/primer_knowledge_graph.md:424` | `primer_knowledge_graph/primer_knowledge_graph.md:430` | 5924434 | Codex | verified | First-loss diagnosis, A/B/C, R2 carry-forwards and 538–552 regression teach changed results and changed evidence. | Retain hand replay plus bounded optional rebuild; durable publication excluded (883). |
| route-python-duckdb | primary | kg-evaluation | `primer_knowledge_graph/primer_knowledge_graph.md:494` | `primer_knowledge_graph/primer_knowledge_graph.md:504` | `primer_knowledge_graph/primer_knowledge_graph.md:508` | `primer_knowledge_graph/primer_knowledge_graph.md:530` | 5924434 | Codex | verified | Fixed evidence/answer units explain arithmetic, missing-denial consequences and 2/5 versus 5/5 denominators. | Retain illustrative tiny gold set; no independent accuracy study promised. |
| route-python-duckdb | primary | kg-privacy | `primer_knowledge_graph/primer_knowledge_graph.md:438` | `primer_knowledge_graph/primer_knowledge_graph.md:451` | `primer_knowledge_graph/primer_knowledge_graph.md:462` | `primer_knowledge_graph/primer_knowledge_graph.md:466` | 5924434 | Codex | verified | Paired releases resolve approved citations and derive identical ordinary responses and visible counts. | Retain synthetic view reasoning; live enforcement/threat-model validation excluded (554, 883). |
| route-r-projection | alternative | kg-r-projection | `primer_knowledge_graph/primer_knowledge_graph.md:757` | `primer_knowledge_graph/primer_knowledge_graph.md:761` | `primer_knowledge_graph/primer_knowledge_graph.md:798` | `primer_knowledge_graph/primer_knowledge_graph.md:804` | 5924434 | Codex | verified | Deduplication, neighbour expansion, weak/strong components and degree are derived, then returned to evidence. | Retain lossy independent fixture and no correction synchronisation (883); alternative tier unchanged. |
| route-graph-storage | reference-only | kg-rdf | `primer_knowledge_graph/primer_knowledge_graph.md:852` | `primer_knowledge_graph/primer_knowledge_graph.md:856` | `primer_knowledge_graph/primer_knowledge_graph.md:861` | `primer_knowledge_graph/primer_knowledge_graph.md:863` | 5924434 | Codex | verified | Qualified resources retain evidence; 840–846 distinguish classification, validation and source assertion. | Retain bounded worked mapping and bridge; no executed reasoner/SHACL/SPARQL integration. |
| route-graph-storage | reference-only | kg-property | `primer_knowledge_graph/primer_knowledge_graph.md:869` | `primer_knowledge_graph/primer_knowledge_graph.md:871` | `primer_knowledge_graph/primer_knowledge_graph.md:873` | `primer_knowledge_graph/primer_knowledge_graph.md:873` | 5924434 | Codex | verified | Parallel assertions preserve source and time; the worked dates expose conflict and indeterminacy. | Retain short reference comparison, not a taught service route or executed Cypher. |
| route-graph-storage | reference-only | kg-storage | `primer_knowledge_graph/primer_knowledge_graph.md:875` | `primer_knowledge_graph/primer_knowledge_graph.md:877` | `primer_knowledge_graph/primer_knowledge_graph.md:885` | `primer_knowledge_graph/primer_knowledge_graph.md:883` | 5924434 | Codex | verified | Workload choice and prospective exchange test use the worked evidence and answer records as acceptance criteria. | Retain reference-only serving guidance; no benchmark, migration or Neo4j service promise. |


## Evidence provenance and revision review

| Evidence | Revision and method | Current consequence |
|---|---|---|
| Structural and teaching review | New manual review of the `9ceb2d2` to `5924434` source diff, moved chapter boundaries, adjacent route transitions, 14 concept locators and the new property-graph example; brief r12 to r13 and audit r15 to r16. | Content pass above; no new execution or external source check is implied. |
| Earlier full review and standards | Audit r15 and its predecessors record complete reading at `3f3d384`, targeted review at `9ceb2d2`, and scoped W3C checks on 12 November; other source/API checks date to 11 November at `1ee9f80`. | Retained as historical evidence for unchanged claims; not every citation or dependency was independently rechecked. |
| Python and R | `just examples` rerun against source `5924434`; both pinned companion manifests pass. | Execution remains bounded to the companions; the primary prose, projection derivation, disclosure and release are illustrative. |
| Rendering and visual checks | `just all` and `just render-qa primer_knowledge_graph` rerun from source `5924434`; representative pages 1, 54, 9 and 41 inspected. | HTML/PDF freshness and sampled visual quality pass; PDF remains untagged. |
| Accessibility | Prior review and #421 identify outstanding human checks. | Keyboard, no-JavaScript, browser accessibility tree, screen-reader and PDF tag/reading-order checks remain outstanding. |

The earlier scoped standards review checked [RDF 1.1](https://www.w3.org/TR/rdf11-concepts/), [SPARQL 1.1](https://www.w3.org/TR/sparql11-query/), [PROV-O](https://www.w3.org/TR/prov-o/), [Neo4j 5 MATCH](https://neo4j.com/docs/cypher-manual/5/clauses/match/) and the declared companion APIs at `1ee9f80` on 11 November. The subsequent bridge review checked [RDF Schema domain](https://www.w3.org/TR/rdf-schema/#ch_domain), [range](https://www.w3.org/TR/rdf-schema/#ch_range) and [SHACL cardinality](https://www.w3.org/TR/shacl/#MinCountConstraintComponent) on 12 November. These are retained source checks, not renewed checks or executed reasoner and validator results.

The current companion run used `just examples`, with the Python/DuckDB and R manifests both passing in pinned containers. Its Python assertions cover bounded construction, persistence and queries; R checks a precomputed fixture's path and weak components. The hand-worked release and disclosure case, ledger-to-projection transformation and service migration were not executed by those passes. The current publication report records representative opening, figure, table and prose-page visual checks, and a PDF reported as `Tagged: no`; those samples do not establish full accessibility.

The earlier audit contains further commands, hashes, samples and standards
links in Git history. They remain associated with their original revisions.
No source, output, case contract, figure or example was changed by this audit.

## Release readiness checklist

- Content gate: **pass** for the agreed teaching scope.
- Release readiness: **not-ready**. Human accessibility checks remain open;
  current output build and sampled visual QA pass, but do not clear #421.
- The structural evidence checker tests IDs, revisions and required fields; it
  cannot establish pedagogy, rendered quality or accessibility.

## Mechanical checks

- `python3 -I scripts/check/primer_evidence.py primer_knowledge_graph/primer_knowledge_graph.brief.md primer_knowledge_graph/primer_knowledge_graph.audit.md`: passed.
- `python3 -I scripts/check/primer_audit.py --repo-root . --project primer_knowledge_graph`: passed; verifies source revision and explicit concept locators, not their teaching quality.
- Explicit anchor comparison of `9ceb2d2` and `5924434`: all 32 earlier explicit anchors remain; 36 are present now.
- `git diff --check`: passed.

`just all`, `just examples`, and `just render-qa primer_knowledge_graph`
passed. The mechanical checks do not validate every free-text line reference
or the semantics of a cited passage; locators are revision-specific.
