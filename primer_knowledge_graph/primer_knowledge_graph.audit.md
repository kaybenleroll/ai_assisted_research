# Primer audit: Building Knowledge Graphs: From Sources to Verifiable Queries

- Issue and milestone: #398; related #397
- Audit revision: `kg-398-depth-audit-r7`
- Source revision: `a02e3d9`
- Tracked path: `primer_knowledge_graph/primer_knowledge_graph.audit.md`
- Starting branch: `docs/398-knowledge-graph-finish`
- Reviewer(s): Codex
- Date: 2026-11-11
- Reviewed revision: `a02e3d9`
- Brief reviewed: `primer_knowledge_graph/primer_knowledge_graph.brief.md`, `kg-398-brief-r4`, based on commit `a02e3d9` with the source revision metadata updated in the working tree
- Review boundary: committed source and brief read for teaching and traceability; calculations sampled by hand; source/output render and examples passed; citation-by-citation verification and visual accessibility remain unchecked
- Teaching-case contract: `primer_knowledge_graph/primer_knowledge_graph.case.md`
- Core-concept depth matrix: brief r4, all 14 IDs reviewed below
- Readiness decision: not-ready

The reviewed source is committed at `a02e3d9`. The brief is revision r4 from
that commit, with only its source revision metadata updated to point to the
commit. The source/output render and examples have passed; citation-by-citation
and visual semantic accessibility review remain outstanding.

## Whole-document review

| Area | Scope and method | Evidence | Status | Finding and disposition |
|---|---|---|---|---|
| Brief and case coverage | Whole source against r4 and the case contract | Lines 13–742; route and concept matrices below | verified | Primary and alternative reader paths are substantively taught; reference route is bounded. |
| Claims and calculations | Sampled temporal boundary, Q4, path and retrieval arithmetic | Lines 175–183, 234–260, 315–345, 351–375, 654–673 | verified | Case outcomes and 1/2 versus 2/2 recall follow the stated inputs; this is not verification of every claim. |
| Sources and freshness | Inventory only | Lines 715–750 and inline citations | not-checked | Check each primary source and version before release; the source's verification statement was not independently re-established here. |
| Depth and organisation | Full reading and section-boundary review | Lines 13–709; section dispositions below | verified | The case carries a continuous reasoning spine; comparisons and exercises build on it. |
| Examples and failure | Trace by hand, including correction and disclosure | Lines 127–167, 234–260, 289–345, 385–413 | verified | The synthetic case teaches choices and limitations; execution is separate. |
| Figures, tables and accessibility | Source inventory only | Excerpt/ledger tables at 39–43 and 147–155; projection table at 662–671 | not-checked | Tables replace diagrams as specified in the brief; rendered semantics and visual quality need review. |
| HTML, PDF and metadata | Source/output render passed for the committed revision | Published outputs in `primer_knowledge_graph/` | partial | Render passed; semantic visual accessibility review remains outstanding. |
| Uncertainty and limits | Full source | Lines 377, 413, 628, 679, 742 | verified | Synthetic evaluation, access control, projection and durable release limits are stated. |

## Reader-scale depth review

| Section | Teaching job and reasoning spine | Reader action and interpretation | Limit | Disposition |
|---|---|---|---|---|
| Introduction | Orient the fictional conflict and standalone route | Lines 5–9 | Sources are fictional | retain; orientation |
| Design the Graph Around Questions | Typed paths and bounded questions | Lines 19–29, 49–65 | Absence is scoped | retain |
| Build an Evidence Ledger | Mentions, qualified claims, extraction, provenance | Lines 92–105, 129–167 | Refuse unsupported assertions | retain |
| Interpret Time, Conflict, and Uncertainty | Date classification and comparable propositions | Lines 175–199 | Unknown end is not continuity | retain |
| Answer Questions From the Graph | Bind and select ledger rows, classify and join | Lines 205–260 | Path is not authority or applicability to Orion | retain |
| Diagnose, Correct, and Evaluate the Answer | Isolate failure, replay revisions, score defined items | Lines 289–345, 351–375 | Small synthetic gold set | retain |
| Govern Identity, Disclosure, and Releases | Apply views before operations and trace release impacts | Lines 385–413, 419–453 | Access and release controls are hand-worked | retain |
| Transfer the Method to Literature and Dependencies | Apply typed evidence paths in two domains | Lines 497–509, 618–628 | Neither clinical conclusion nor exploitation follows from a path | retain |
| Analyse a Positive Projection | Select edges, calculate paths, components and degree, then return to evidence | Lines 636–681 | Lossy undated topology cannot answer dated evidence questions | retain |
| Practise the Reasoning | Test and interpret the preceding methods | Lines 687–707 | Exercises reuse synthetic assumptions | retain; practice |
| Storage and Implementation Reference | Compare qualified mappings and operational choices | Lines 715–740 | Mapping and service migration are not executed | retain; bounded reference |
| Further Reading | Signpost deeper sources | Lines 746–750 | Not a replacement for source checking | retain; reference |

## Teaching-case trace

| Case stage | Evidence and result | Execution status | Limitation |
|---|---|---|---|
| Input and assumptions | Lines 35–45: R1, D1, M1 excerpts and date convention | illustrative | Selected fictional evidence |
| Construction | Lines 92–105, 129–141: resolve mentions and extract `c1`, `c4`, `c5`; abstain on Alex | illustrative | Narrow illustrative patterns |
| Intermediate representation | Lines 145–157: seven qualified assertion rows | illustrative | Four rows curated |
| Computed result and query | Lines 234–260: match `c1` and `c5`, classify time and compare; join `c1` and `c3` | illustrative | Policy applies only to selected evidence |
| Interpretation | Lines 241–250: disagreement on 15 March and abstention on applicability | illustrative | Neither source establishes universal truth |
| Failure and correction | Lines 289–345: omitted denial, repaired extraction, R2 rebuild and re-evaluation | illustrative | Production release machinery is not implemented |

## Route transition evidence

All locators below refer to the current source revision and all operations were
reviewed as hand-worked explanations, not independently executed.

| route_id | concept_id(s) | transition (from to) | linked input and reader operation | intermediate reasoning or decision | result | interpretation | material limitation | execution status | gap and reader consequence |
|---|---|---|---|---|---|---|---|---|---|
| route-python-duckdb | kg-boundary, kg-mentions | excerpts → identities | Lines 35–59 select R1/M1 and Q4; lines 92–105 resolve mentions | Shared version and project IDs, but abstain on Alex | Identified participants and unresolved mention | Rows can share a proposition without merging people | No source completeness, lines 63–65 | illustrative | None blocking; companion examples passed. |
| route-python-duckdb | kg-claims, kg-extraction | identities → ledger | Lines 111–141 turn the M1 denial into `c5` | Preserve polarity, span and temporal horizon | `c5` alongside `c1`, lines 145–157 | Opposite evidence remains separable | Refuse conditional or imprecise claims, lines 139–143 | illustrative | None blocking. |
| route-python-duckdb | kg-temporal, kg-queries, kg-duckdb | ledger → Q4 and path | Lines 175–183 and 234–260 select and classify `c1`, `c5`, then join `c1` to `c3` | Compare matching proposition and classify each hop | Disagreement and abstention; path changes with date | Conflict and topology answer different questions | Unknown horizon and absent Orion rule | illustrative | Optional persistence is described at line 740; companion examples passed. |
| route-python-duckdb | kg-correction, kg-evaluation | Q4 failure → repaired and revised answers | Lines 289–345 trace missing `c5`, restore it, then rebuild from R2 | Hold question and policy fixed; classify new interval | Supported in A, abstention in B, refuted in C | Distinguish extraction defect from source correction | Synthetic source and bounded experiment | illustrative | None blocking; companion examples passed. |
| route-python-duckdb | kg-evaluation, kg-privacy | answers → score and permitted release | Lines 351–375 score fixed evidence and answer items; lines 385–413 filter paired audience views | Separate retrieval from answer quality and filter before counting | Recall 1/2 then 2/2; identical ordinary outputs | A correct internal result can leak through counts | Hand-worked views, not enforced access control | illustrative | None blocking. |
| route-r-projection | kg-r-projection | ledger → positive edge view | Lines 636–650 select six positive assertions, deduplicate triples and include eight vertices | Drop qualifiers and retain five directed edges | Five-edge graph with two isolates | Edges count distinct connections, not evidence records | Dates and assertion IDs discarded | illustrative | None blocking; R example passed. |
| route-r-projection | kg-r-projection | edge view → topology → evidence | Lines 654–673 expand neighbours and compute weak components and degrees | Unit edge costs and direction-free weak connectivity | Two-hop path, three weak components, Atlas degree three | Structural analysis of selected view | Lines 675–681 return to dated evidence; projection cannot decide Q4 | illustrative | None blocking; R example passed. |

## Adversarial depth gate

Every row is a content judgement at the source revision above. `verified` denotes
teaching evidence, not execution or release approval. Each locator identifies a
passage in `primer_knowledge_graph/primer_knowledge_graph.md`.

| route_id | route tier | concept_id | explanation locator | example/action locator | interpretation locator | limitation locator | evidence revision | reviewer | status | finding | scope decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| route-python-duckdb | primary | kg-boundary | `primer_knowledge_graph/primer_knowledge_graph.md:33` | `primer_knowledge_graph/primer_knowledge_graph.md:53` | `primer_knowledge_graph/primer_knowledge_graph.md:61` | `primer_knowledge_graph/primer_knowledge_graph.md:63` | a02e3d9 | Codex | verified | Question, source and refusal bound meaning. | Retain brief scope. |
| route-python-duckdb | primary | kg-mentions | `primer_knowledge_graph/primer_knowledge_graph.md:73` | `primer_knowledge_graph/primer_knowledge_graph.md:97` | `primer_knowledge_graph/primer_knowledge_graph.md:105` | `primer_knowledge_graph/primer_knowledge_graph.md:103` | a02e3d9 | Codex | verified | Mention, entity and unresolved identity remain distinct. | Retain brief scope. |
| route-python-duckdb | primary | kg-claims | `primer_knowledge_graph/primer_knowledge_graph.md:111` | `primer_knowledge_graph/primer_knowledge_graph.md:133` | `primer_knowledge_graph/primer_knowledge_graph.md:155` | `primer_knowledge_graph/primer_knowledge_graph.md:125` | a02e3d9 | Codex | verified | Qualified assertions preserve opposing evidence. | Retain brief scope. |
| route-python-duckdb | primary | kg-temporal | `primer_knowledge_graph/primer_knowledge_graph.md:175` | `primer_knowledge_graph/primer_knowledge_graph.md:179` | `primer_knowledge_graph/primer_knowledge_graph.md:245` | `primer_knowledge_graph/primer_knowledge_graph.md:183` | a02e3d9 | Codex | verified | The date classifier distinguishes outside from unknown. | Retain brief scope. |
| route-python-duckdb | primary | kg-extraction | `primer_knowledge_graph/primer_knowledge_graph.md:129` | `primer_knowledge_graph/primer_knowledge_graph.md:133` | `primer_knowledge_graph/primer_knowledge_graph.md:137` | `primer_knowledge_graph/primer_knowledge_graph.md:139` | a02e3d9 | Codex | verified | Source spans yield candidates and explicit refusals. | Retain brief scope. |
| route-python-duckdb | primary | kg-duckdb | `primer_knowledge_graph/primer_knowledge_graph.md:740` | `primer_knowledge_graph/primer_knowledge_graph.md:159` | `primer_knowledge_graph/primer_knowledge_graph.md:165` | `primer_knowledge_graph/primer_knowledge_graph.md:742` | a02e3d9 | Codex | verified | Ledger evidence joins are taught; optional persistence remains unverified. | Retain brief scope. |
| route-python-duckdb | primary | kg-queries | `primer_knowledge_graph/primer_knowledge_graph.md:203` | `primer_knowledge_graph/primer_knowledge_graph.md:234` | `primer_knowledge_graph/primer_knowledge_graph.md:241` | `primer_knowledge_graph/primer_knowledge_graph.md:258` | a02e3d9 | Codex | verified | Bindings and date classification support interpreted answers. | Retain brief scope. |
| route-python-duckdb | primary | kg-correction | `primer_knowledge_graph/primer_knowledge_graph.md:315` | `primer_knowledge_graph/primer_knowledge_graph.md:317` | `primer_knowledge_graph/primer_knowledge_graph.md:325` | `primer_knowledge_graph/primer_knowledge_graph.md:345` | a02e3d9 | Codex | verified | Three passes expose extraction repair and source revision. | Retain brief scope. |
| route-python-duckdb | primary | kg-evaluation | `primer_knowledge_graph/primer_knowledge_graph.md:351` | `primer_knowledge_graph/primer_knowledge_graph.md:357` | `primer_knowledge_graph/primer_knowledge_graph.md:371` | `primer_knowledge_graph/primer_knowledge_graph.md:377` | a02e3d9 | Codex | verified | Fixed item boundaries distinguish recall and answer quality. | Retain brief scope. |
| route-python-duckdb | primary | kg-privacy | `primer_knowledge_graph/primer_knowledge_graph.md:385` | `primer_knowledge_graph/primer_knowledge_graph.md:398` | `primer_knowledge_graph/primer_knowledge_graph.md:409` | `primer_knowledge_graph/primer_knowledge_graph.md:413` | a02e3d9 | Codex | verified | Paired views explain disclosure and count leakage. | Retain brief scope. |
| route-r-projection | alternative | kg-r-projection | `primer_knowledge_graph/primer_knowledge_graph.md:632` | `primer_knowledge_graph/primer_knowledge_graph.md:636` | `primer_knowledge_graph/primer_knowledge_graph.md:654` | `primer_knowledge_graph/primer_knowledge_graph.md:679` | a02e3d9 | Codex | verified | A selected projection supports worked paths and components, not evidence answers. | Retain brief scope. |
| route-graph-storage | reference-only | kg-rdf | `primer_knowledge_graph/primer_knowledge_graph.md:715` | `primer_knowledge_graph/primer_knowledge_graph.md:718` | `primer_knowledge_graph/primer_knowledge_graph.md:724` | `primer_knowledge_graph/primer_knowledge_graph.md:726` | a02e3d9 | Codex | verified | Qualified resources distinguish descriptions from bare assertions. | Retain brief scope. |
| route-graph-storage | reference-only | kg-property | `primer_knowledge_graph/primer_knowledge_graph.md:732` | `primer_knowledge_graph/primer_knowledge_graph.md:732` | `primer_knowledge_graph/primer_knowledge_graph.md:732` | `primer_knowledge_graph/primer_knowledge_graph.md:736` | a02e3d9 | Codex | verified | Parallel relationships or assertion nodes retain evidence; exchange needs testing. | Retain brief scope. |
| route-graph-storage | reference-only | kg-storage | `primer_knowledge_graph/primer_knowledge_graph.md:734` | `primer_knowledge_graph/primer_knowledge_graph.md:736` | `primer_knowledge_graph/primer_knowledge_graph.md:734` | `primer_knowledge_graph/primer_knowledge_graph.md:736` | a02e3d9 | Codex | verified | Workload and exchange tests guide choice without a benchmark claim. | Retain brief scope. |

## Published examples and representative sampling

| Object | Method and result | Limitation |
|---|---|---|
| Northbridge Q4 and correction | Hand-traced source rows, 15/16 March classifications and R2 derivations at lines 234–250 and 315–345 | Illustrative; the companion example passed within its fixture boundary. |
| Retrieval score | Checked Pass A precision 1/1 and recall 1/2, and Pass B precision and recall 2/2 at lines 351–359 | Synthetic example, not empirical performance. |
| R projection | Checked graph construction, breadth-first path, components and degree at lines 636–681 | The R example passed; the projection remains lossy. |
| Literature and dependencies | Read source-version joins, qualifying filters and correction boundaries at lines 459–628 | Fictional cases, hand-worked; no external data verified. |
| RDF, SPARQL, SHACL, PROV-O, Cypher | Read mapping and caveats at lines 715–736 | Illustrative reference; specifications and product-version claims were not rechecked. |
| Rendered page samples | Not sampled | Opening, table, code and figure/equation pages need visual inspection where applicable, including accessibility meaning. |

## Revision-triggered second audit

The source and brief were substantively rewritten after audit r6 at `f730591`.
Codex reread the current source and brief, rebound the locators, and sampled the
hand calculations. The reviewed source is committed at `a02e3d9`; source/output
render and examples have passed for that revision. Earlier visual findings are
historical and are not claimed for this revision. Citation-by-citation and
visual semantic accessibility review remain outstanding.

## Release readiness checklist

- Content gate: **pass**
- Release readiness: **not-ready**

| Gate | Decision | Evidence or remaining work |
|---|---|---|
| Route and concept depth | pass | All 14 rows reviewed; primary and alternative transitions are taught. Reference-only has no service execution promise. |
| Revision binding | pass | Source and reviewed revision point to `a02e3d9`; brief r4 has its source revision updated to the same commit. |
| Examples and implementation | pass | Python/DuckDB and R examples passed for the committed source, within their fixture boundaries. |
| Published outputs | partial | Source/output render passed; representative visual semantic review remains outstanding. |
| Sources and accessibility | pending | Recheck primary citations and versions, links, output structure and accessibility meaning. |
| Mechanical checks | pass | Evidence structure and Git-backed revision and locator checks passed; see commands below. |

## Mechanical check results

Source/output render and examples passed for `a02e3d9` as reported for the
committed revision. The checks below concern the updated evidence metadata.

- `python3 -I scripts/check/primer_evidence.py primer_knowledge_graph/primer_knowledge_graph.brief.md primer_knowledge_graph/primer_knowledge_graph.audit.md`: **passed**, exit 0.
- `python3 -I scripts/check/primer_audit.py --repo-root . --project primer_knowledge_graph`: **passed**, exit 0; source SHA-256 `6bf53d1689870ed0a28193178797480b6796afcdef48cf562ba1540c54f6da2a`.
- `git diff --check -- primer_knowledge_graph/primer_knowledge_graph.brief.md primer_knowledge_graph/primer_knowledge_graph.audit.md`: **passed**, exit 0.

These checks do not establish citation accuracy or visual semantic accessibility.
