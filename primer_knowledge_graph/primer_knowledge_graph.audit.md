# Primer audit: Building Knowledge Graphs: From Sources to Verifiable Queries

- Issue and milestone: #398; related #397
- Audit revision: `kg-398-depth-audit-r11`
- Source revision: `1ee9f80`
- Tracked path: `primer_knowledge_graph/primer_knowledge_graph.audit.md`
- Starting branch: `docs/398-knowledge-graph-finish`
- Reviewer(s): Codex
- Date: 2026-11-11
- Reviewed revision: `1ee9f80`
- Brief reviewed: `primer_knowledge_graph/primer_knowledge_graph.brief.md`, `kg-398-brief-r8`, working-tree update
- Review boundary: whole-document source and routes at `1ee9f80`; scoped
  primary-source review and changed-passage review; regenerated outputs and
  representative visual pages inspected; semantic accessibility remains
  untested
- Teaching-case contract: `primer_knowledge_graph/primer_knowledge_graph.case.md`
- Core-concept depth matrix: brief r8, all 14 IDs reviewed below
- Readiness decision: not-ready

## Current whole-document review

Codex reviewed source `1ee9f80` against brief r8 and the teaching-case
contract. The earlier whole-document and route review at `56d76da` is retained
for unchanged reasoning, with locators rebound below. Compared with that revision,
the changed passages at 75, 400–409, 641–648, 846, 880, 889, 897 and 905
were reread along with their dependent route, correction, literature and storage
context. The diagnostic sequence retains both correction branches, and the
labelled records preserve the three candidates and evidence paths. The revised
reference wording remains bounded to the checked interfaces. The teaching
judgements remain valid; the worked routes remain illustrative.

The inventory covers the graph and questions (143–195), ledger (197–297),
time (299–331), queries (333–396), repair (398–470), disclosure, evaluation
and release (472–594), transfer cases (596–793), topology (795–846), practice
(848–872), storage reference (874–909) and reading (911–917). The walkthrough
agrees with the detailed Q4 classifications and repair at 366–382 and
446–468; its retrieval arithmetic agrees with 532–570. These are selected
hand checks, not independent verification of all claims or sources. The
literature and dependency cases are synthetic; the reference branch does not
promise a service.

The pinned `just all` route regenerated the HTML/PDF after this source change;
both companion examples passed. `just render-qa primer_knowledge_graph` passed
its mechanical checks. Current PDF pages 3, 9, 12 and 57 were rasterised and
visually inspected: the expanded opening, walkthrough, ordered diagnostic
sequence, and labelled literature records are legible with no clipping or
broken page flow. This is visual evidence only, not semantic accessibility
validation.

**Content gate: pass** for the stated illustrative primary and alternative
routes. **Scoped source gate: pass** for the checks recorded below. **Release
readiness: not-ready** for a full accessibility claim because of the shared
template and PDF blockers below. Source SHA-256 at `1ee9f80`:
`51ccafddb162978237ddcdbd1261cb99e41c17a65f861e36dca8a1e9ec6cae08`.

## Scoped source verification

On 11 November 2026 the source reviewer checked the standards and interface
claims, version baselines, and each distinct cited external source, against
primary sources. The review found no material unsupported claim in that scope.
It did not run the companions, execute a graph service or migration, verify all
synthetic calculations, attest installed transitive dependencies, or establish
accessibility. These links identify the checked sources and their use:

- RDF graph, terms, literals and datasets, source 880–889: [RDF 1.1 Concepts](https://www.w3.org/TR/rdf11-concepts/#section-rdf-graph), [literals](https://www.w3.org/TR/rdf11-concepts/#section-Graph-Literal), [datasets](https://www.w3.org/TR/rdf11-concepts/#section-dataset), and the [n-ary relations note](https://www.w3.org/TR/swbp-n-aryRelations/).
- Pattern matching, constraints and provenance, 891–893: [SPARQL 1.1](https://www.w3.org/TR/sparql11-query/), [SHACL](https://www.w3.org/TR/shacl/) and [PROV-O](https://www.w3.org/TR/prov-o/). These support the illustrative mapping, not execution of that mapping.
- Property graph and fixed joins, 897–905: [Neo4j graph concepts](https://neo4j.com/docs/getting-started/appendix/graphdb-concepts/), [Neo4j 5 MATCH](https://neo4j.com/docs/cypher-manual/5/clauses/match/), [DuckDB 1.4 joins](https://duckdb.org/docs/1.4/sql/query_syntax/from#joins) and [DuckDB 1.4 Python DB API](https://duckdb.org/docs/1.4/clients/python/dbapi). No Neo4j service route was executed.
- R projection, 801–846: [igraph 2.3.0 constructor](https://raw.githubusercontent.com/igraph/rigraph/v2.3.0/man/graph_from_data_frame.Rd), [paths](https://raw.githubusercontent.com/igraph/rigraph/v2.3.0/man/distances.Rd), [components](https://raw.githubusercontent.com/igraph/rigraph/v2.3.0/man/components.Rd), and [tidygraph 1.3.1 activation](https://raw.githubusercontent.com/thomasp85/tidygraph/v1.3.1/man/activate.Rd). Synthetic topology was also checked by hand against the fixture.
- Declared baselines: [Python 3.12.15](https://www.python.org/downloads/release/python-31215/), [DuckDB 1.4.3](https://pypi.org/pypi/duckdb/1.4.3/json), [R 4.5.3 release notes](https://stat.ethz.ch/R-manual/R-patched/doc/html/NEWS.html), and package metadata for [igraph 2.3.0](https://raw.githubusercontent.com/igraph/rigraph/v2.3.0/DESCRIPTION), [tidygraph 1.3.1](https://raw.githubusercontent.com/thomasp85/tidygraph/v1.3.1/DESCRIPTION) and [dplyr 1.2.1](https://raw.githubusercontent.com/tidyverse/dplyr/v1.2.1/DESCRIPTION). Transitive versions were not independently attested.
- Other cited sources, 235 and 913–917: [record-linkage blocking](https://www150.statcan.gc.ca/n1/pub/12-001-x/2021002/article/00002-eng.htm), [PROV-DM](https://www.w3.org/TR/prov-dm/), [SPARQL optional patterns](https://www.w3.org/TR/sparql11-query/#optional), and [NIST SP 800-188](https://csrc.nist.gov/pubs/sp/800/188/final). The fictional identity and disclosure examples are not validated by these references.

## Accessibility and output status

The local source fixes are the ordered diagnostic list at 402–407, which
retains both branches, and the labelled literature candidate records at
644–646, which retain the evidence paths. Their current HTML and PDF
presentation was regenerated and visually checked as described above.

The earlier accessibility review found shared build/template limitations:
the PDF is untagged; HTML contents buttons have duplicate accessible names;
there is no skip-to-main link; and the displayed document title is absent from
heading navigation. Keyboard and screen-reader testing, the browser accessibility
tree, and PDF tag and reading-order semantics remain untested. Earlier static
fragment checks do not establish accessibility for this revision. These shared
issues block a full accessibility release claim; the content pass does not
waive them. They are tracked separately because they affect the common primer
template and PDF build rather than this primer's source alone. Follow-up is
tracked in issue #421.

## Current reader-scale section dispositions

| Section and teaching job | Reasoning and reader application | Limit | Disposition |
|---|---|---|---|
| Introduction, 3–75 | Vocabulary, graph comparison and answer trace, 11–71 | Traceability does not prove truth, 63–67 | retain; orientation |
| Complete Northbridge Question, 77–141 | Q4 from source to evaluated release, 85–139 | Fictional and illustrative, 79, 133, 137 | retain; early worked overview |
| Design the Graph, 143–195 | Paths, source scope and Q1–Q5, 147–191 | Absence is scoped, 193–195 | retain |
| Evidence Ledger, 197–297 | Identity decisions and source-to-row construction, 220–235, 259–287 | Extraction may miss evidence, 235, 273–275 | retain |
| Time and Conflict, 299–331 | Classify evidence before policy, 303–313, 321–331 | Unknown duration is not permanence, 307–313 | retain |
| Answer Questions, 333–396 | Bind Q4 and follow a typed path, 368–390 | No applicability inference to Orion, 392 | retain |
| Diagnose and Correct, 398–470 | Trace failures and compare controlled passes, 413–431, 446–468 | Synthetic correction, 448–454 | retain |
| Govern Disclosure and Release, 472–594 | Audience views, evaluation and regression, 476–506, 532–592 | Synthetic checks do not prove deployment safety, 502–508, 570 | retain |
| Transfer to Literature and Dependencies, 596–793 | Versioned evidence and build-specific joins, 600–793 | Path is neither clinical proof nor exploitation, 791–793 | retain |
| Positive Projection, 795–846 | Select edges and calculate paths and components, 801–838 | Dropped qualifiers prevent Q4 answer, 840–844 | retain |
| Practice, 848–872 | Exercises and worked answers, 850–872 | Reuses assumptions, 850 | retain; bounded practice |
| Storage Reference, 874–909 | Map assertions and compare serving choices, 880–901 | Exchange and migration need tests, 901–907 | retain; reference branch |
| Further Reading, 911–917 | Signpost further sources | Does not establish citation verification | retain; intentionally brief |

## Current teaching-case trace

All stages are illustrative prose at `1ee9f80`; no operations were executed
in this audit. Historical companion runs cover only their declared fixtures.

| Stage | Input, decision and result | Limit |
|---|---|---|
| Source and boundary | R1, M1, context and Q4, 79–87 | Incomplete synthetic sources |
| Construction | Link mentions and preserve opposing `c1`, `c5`, 89–103 | Topic context is assumed |
| Representation | Ledger rows and classifications, 103–111, 281–287 | Admitted evidence can be incomplete |
| Query and interpretation | Bind proposition, classify, compare and abstain, 113–119, 368–382 | Result depends on evidence and policy |
| Failure and correction | Omit and restore denial; revise R1 to R2, 121–127, 446–468 | Not an operational decision |
| Disclosure and release | Audience views, scores and release regression, 129–141, 476–594 | Not a production safety or accuracy test |

## Route transition evidence

All locators refer to `primer_knowledge_graph/primer_knowledge_graph.md` at
`1ee9f80`. Execution status describes the hand-worked source explanation.

| route_id | concept_id(s) | transition (from to) | linked input and reader operation | intermediate reasoning or decision | result | interpretation | material limitation | execution status | gap and reader consequence |
|---|---|---|---|---|---|---|---|---|---|
| route-python-duckdb | kg-boundary, kg-mentions | sources to identities | 85–93, 169–175, 220–233 | Topic and IDs link mentions; Alex unresolved | Shared participants | Compare without forced identity | Context and completeness, 93, 177 | illustrative | No blocking gap. |
| route-python-duckdb | kg-claims, kg-extraction | identities to ledger | 95–111, 259–287 | Preserve polarity, time and source | Separate `c1` and `c5` | Opposing assertions stay comparable | Extraction may omit evidence, 111 | illustrative | No blocking gap. |
| route-python-duckdb | kg-temporal, kg-queries, kg-duckdb | ledger to answers | 103–119, 368–390 | Bind and classify rows and path hops | Conflict and abstention | Conflict differs from reachability | Unknown duration; no Orion inference, 105, 392 | illustrative | No blocking gap. |
| route-python-duckdb | kg-correction | answer to correction | 121–127, 446–468 | Restore denial then revise source | B abstains; C refutes | Repair differs from source revision | No operational authority, 127 | illustrative | No blocking gap. |
| route-python-duckdb | kg-privacy, kg-evaluation | correction to release | 129–141, 476–594 | Filter views, score items and compare provenance | Paired outputs and regression | Internal correctness does not ensure disclosure safety | Synthetic views and scores, 133, 570 | illustrative | No blocking gap. |
| route-r-projection | kg-r-projection | ledger to edge view | 797–815 | Select positives, deduplicate and keep isolates | Five edges, eight vertices | Edge count differs from assertion count | Qualifiers dropped, 801 | illustrative | No blocking gap. |
| route-r-projection | kg-r-projection | edge view to topology to evidence | 817–844 | Trace neighbours and components, restore date scope | Two-hop path and three components | Selected topology only | Cannot settle Q4, 842–844 | illustrative | No blocking gap. |

## Adversarial depth gate

Each row records a current teaching judgement at `1ee9f80`. Verified means
the prose teaches the stated scope, not that it was executed or source-verified.

| route_id | route tier | concept_id | explanation locator | example/action locator | interpretation locator | limitation locator | evidence revision | reviewer | status | finding | scope decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| route-python-duckdb | primary | kg-boundary | `primer_knowledge_graph/primer_knowledge_graph.md:163` | `primer_knowledge_graph/primer_knowledge_graph.md:183` | `primer_knowledge_graph/primer_knowledge_graph.md:191` | `primer_knowledge_graph/primer_knowledge_graph.md:193` | 1ee9f80 | Codex | verified | Questions bound admissible evidence. | Retain. |
| route-python-duckdb | primary | kg-mentions | `primer_knowledge_graph/primer_knowledge_graph.md:203` | `primer_knowledge_graph/primer_knowledge_graph.md:222` | `primer_knowledge_graph/primer_knowledge_graph.md:235` | `primer_knowledge_graph/primer_knowledge_graph.md:237` | 1ee9f80 | Codex | verified | Context supports links and Alex requires abstention. | Retain. |
| route-python-duckdb | primary | kg-claims | `primer_knowledge_graph/primer_knowledge_graph.md:241` | `primer_knowledge_graph/primer_knowledge_graph.md:245` | `primer_knowledge_graph/primer_knowledge_graph.md:287` | `primer_knowledge_graph/primer_knowledge_graph.md:243` | 1ee9f80 | Codex | verified | Source-specific assertions preserve qualifications. | Retain. |
| route-python-duckdb | primary | kg-temporal | `primer_knowledge_graph/primer_knowledge_graph.md:305` | `primer_knowledge_graph/primer_knowledge_graph.md:311` | `primer_knowledge_graph/primer_knowledge_graph.md:331` | `primer_knowledge_graph/primer_knowledge_graph.md:307` | 1ee9f80 | Codex | verified | Classification and policy are distinguished. | Retain. |
| route-python-duckdb | primary | kg-extraction | `primer_knowledge_graph/primer_knowledge_graph.md:259` | `primer_knowledge_graph/primer_knowledge_graph.md:263` | `primer_knowledge_graph/primer_knowledge_graph.md:267` | `primer_knowledge_graph/primer_knowledge_graph.md:271` | 1ee9f80 | Codex | verified | Source spans produce candidates and refusals. | Retain. |
| route-python-duckdb | primary | kg-duckdb | `primer_knowledge_graph/primer_knowledge_graph.md:905` | `primer_knowledge_graph/primer_knowledge_graph.md:289` | `primer_knowledge_graph/primer_knowledge_graph.md:295` | `primer_knowledge_graph/primer_knowledge_graph.md:907` | 1ee9f80 | Codex | verified | Hand ledger and optional persistence are distinguished. | Retain. |
| route-python-duckdb | primary | kg-queries | `primer_knowledge_graph/primer_knowledge_graph.md:335` | `primer_knowledge_graph/primer_knowledge_graph.md:368` | `primer_knowledge_graph/primer_knowledge_graph.md:382` | `primer_knowledge_graph/primer_knowledge_graph.md:392` | 1ee9f80 | Codex | verified | Bindings and classifications support interpreted answers. | Retain. |
| route-python-duckdb | primary | kg-correction | `primer_knowledge_graph/primer_knowledge_graph.md:400` | `primer_knowledge_graph/primer_knowledge_graph.md:421` | `primer_knowledge_graph/primer_knowledge_graph.md:446` | `primer_knowledge_graph/primer_knowledge_graph.md:470` | 1ee9f80 | Codex | verified | Failures and passes distinguish repair from revision. | Retain. |
| route-python-duckdb | primary | kg-evaluation | `primer_knowledge_graph/primer_knowledge_graph.md:534` | `primer_knowledge_graph/primer_knowledge_graph.md:542` | `primer_knowledge_graph/primer_knowledge_graph.md:550` | `primer_knowledge_graph/primer_knowledge_graph.md:570` | 1ee9f80 | Codex | verified | Fixed items distinguish retrieval and answer quality. | Retain. |
| route-python-duckdb | primary | kg-privacy | `primer_knowledge_graph/primer_knowledge_graph.md:476` | `primer_knowledge_graph/primer_knowledge_graph.md:488` | `primer_knowledge_graph/primer_knowledge_graph.md:502` | `primer_knowledge_graph/primer_knowledge_graph.md:508` | 1ee9f80 | Codex | verified | Audience views and paired outputs show leakage risks. | Retain. |
| route-r-projection | alternative | kg-r-projection | `primer_knowledge_graph/primer_knowledge_graph.md:797` | `primer_knowledge_graph/primer_knowledge_graph.md:801` | `primer_knowledge_graph/primer_knowledge_graph.md:819` | `primer_knowledge_graph/primer_knowledge_graph.md:844` | 1ee9f80 | Codex | verified | Worked topology loses evidence qualifiers. | Retain. |
| route-graph-storage | reference-only | kg-rdf | `primer_knowledge_graph/primer_knowledge_graph.md:880` | `primer_knowledge_graph/primer_knowledge_graph.md:882` | `primer_knowledge_graph/primer_knowledge_graph.md:889` | `primer_knowledge_graph/primer_knowledge_graph.md:891` | 1ee9f80 | Codex | verified | Qualified resources distinguish descriptions from assertions. | Retain. |
| route-graph-storage | reference-only | kg-property | `primer_knowledge_graph/primer_knowledge_graph.md:897` | `primer_knowledge_graph/primer_knowledge_graph.md:897` | `primer_knowledge_graph/primer_knowledge_graph.md:897` | `primer_knowledge_graph/primer_knowledge_graph.md:901` | 1ee9f80 | Codex | verified | Representation must preserve evidence. | Retain. |
| route-graph-storage | reference-only | kg-storage | `primer_knowledge_graph/primer_knowledge_graph.md:899` | `primer_knowledge_graph/primer_knowledge_graph.md:901` | `primer_knowledge_graph/primer_knowledge_graph.md:899` | `primer_knowledge_graph/primer_knowledge_graph.md:901` | 1ee9f80 | Codex | verified | Workload and exchange tests guide choice. | Retain. |

## Release readiness checklist

- Content gate: **pass**, for the reviewed illustrative teaching routes.
- Source gate: **pass** for the scoped checks and primary sources above.
- Release readiness: **not-ready** for a full accessibility claim. Source
  verification, local content fixes, regenerated outputs, examples, and visual
  samples pass. Shared template/PDF tagging work and keyboard, screen-reader,
  and tag-inspector testing remain outstanding.
- Evidence checks: `python3 -I scripts/check/primer_evidence.py
  primer_knowledge_graph/primer_knowledge_graph.brief.md
  primer_knowledge_graph/primer_knowledge_graph.audit.md` passed, and
  `python3 -I scripts/check/primer_audit.py --repo-root . --project
  primer_knowledge_graph` passed. `just all` passed both companion examples and
  regenerated HTML/PDF; `just render-qa primer_knowledge_graph` passed. Current
  PDF pages 3, 9, 12 and 57 were visually inspected. These checks establish
  neither semantic accessibility nor a tagged PDF. `git diff --check` passed.

## Historical review at 0152148

The following material preserves earlier findings and checks at their original
revisions. It is not current execution or output evidence.

**Layout review, 11 November 2026:** Source `0152148` replaces the literature
excerpt table with four labelled records. The source versions, work names,
locators and quotations are unchanged. PDF page 45 now presents all four
records at a readable width; page 46 and the generated HTML were also checked.
The content gate remains **pass**. Release readiness remains **not-ready**:
primary-source verification and semantic accessibility are outstanding; the
PDF reports that it is untagged. The earlier page 45 layout finding is resolved.

**Previous revision review, 11 November 2026:** Compared source `85d0535` with the
previously reviewed `a02e3d9`, including the revised brief, changed passages,
dependent transitions and rendered outputs. The source SHA-256 is
`9ba095812fdc826ca6aa0b92e3e3fee0557833a7d482599a3c786d01aaaf3cfd`;
brief revision is `kg-398-brief-r5`. The previous review and its original
locators are retained as historical evidence below.

Integration review found that the
diagnostic failures, revised policy example, disclosure-before-evaluation
order, transfer-case landmarks and cross-case comparison follow the existing
teaching route. The opening and correction flows render as selectable line
blocks in HTML and PDF, rather than one-column tables. Visual inspection of
PDF pages 3, 27–29, 45, 48 and 60 found legible flows, diagnostic prose and
transfer headings; the literature excerpt table on page 45 then had excessive
wrapping and unused space. The latest layout review above resolves that finding.
Citation support and semantic accessibility remain unverified.

The pinned HTML/PDF render, both companion examples, metadata, Mermaid,
freshness, Markdown and offline HTML link checks passed. After the source commit
and rebinding, `just primer-audit primer_knowledge_graph` passed, including
evidence and Git-backed locator checks, examples, render QA and scoped links.
The rerendered PDF had the same 73 pages and extracted text as the committed
PDF, but a different creation time; the committed PDF was restored to avoid
timestamp drift. At that revision the content gate passed and release readiness
was not-ready owing to source verification, semantic accessibility and layout.

## Historical reader-scale review at 85d0535

The previous whole-document reading applies to unchanged passages at
`a02e3d9`. The changed material was reread at `85d0535`: the opening flow
(lines 9–19), supplied identity context (104–119), policy comparison (203–213),
diagnosis and three-pass correction (280–353), disclosure followed by
evaluation and release regression (355–477), transfer cases (479–680), and
implementation handoff (790–796). These line numbers refer to `85d0535`.
The revisions preserve the route and its
failure conditions. Each major section retains a coherent teaching job:
orientation (3–23), questions and boundary (25–77), evidence construction
(79–179), time and policy (181–213), queries (215–278), diagnosis (280–353),
disclosure and evaluation (355–477), transfer (479–680), projection
(682–733), practice (735–759), and bounded reference (761–804). Retain these
sections: the transfer landmarks improve retracing, while the short opening,
practice and reference branches have explicit bounded purposes. The synthetic
cases and hand-worked disclosure are not deployment evidence.

## Historical route transition evidence at 0152148

The following current transitions are illustrative hand-worked reasoning;
the separately executed companions cover only their declared fixtures.

| route_id | concept_id(s) | transition (from to) | linked input and reader operation | intermediate reasoning or decision | result | interpretation | material limitation | execution status | gap and reader consequence |
|---|---|---|---|---|---|---|---|---|---|
| route-python-duckdb | kg-boundary, kg-mentions | excerpts → identities | Lines 45–55 select sources; 104–115 resolve mentions | Supplied topic and IDs support links; Alex remains unresolved | Identified participants and an unresolved mention | Shared identity permits comparison | No corpus completeness, 59–77 | illustrative | None blocking. |
| route-python-duckdb | kg-claims, kg-extraction | identities → ledger | Lines 123–127 and 141–169 transform source wording | Preserve polarity, time and provenance | `c1` and `c5` remain distinct | Opposing evidence can coexist | Refuse unsupported rows, 151–155 | illustrative | None blocking. |
| route-python-duckdb | kg-temporal, kg-queries, kg-duckdb | ledger → answers | Lines 187–193 and 217–274 bind, classify and join | Select sources and classify each row | Q4 disagreement and dated path | Conflict is distinct from reachability | Unknown horizon and no inference to Orion | illustrative | None blocking. |
| route-python-duckdb | kg-correction | answer → correction | Lines 282–353 diagnose and compare three passes | Distinguish extraction repair from changed source | Revised ledger and classifications | An unchanged answer may have changed evidence | Synthetic source and bounded experiment | illustrative | None blocking. |
| route-python-duckdb | kg-privacy, kg-evaluation | corrected evidence → permitted, evaluated release | Lines 359–391 define views; 415–473 score and regress outputs | Filter before counting; score fixed items and compare citations | Paired disclosure and regression outcomes | Internal correctness is not disclosure safety | Synthetic views and gold items, 391 and 453 | illustrative | None blocking. |
| route-r-projection | kg-r-projection | ledger → edge view | Lines 682–700 select and deduplicate positive triples | Include isolates and discard qualifiers | Five edges and eight vertices | Edge count differs from assertion count | Dates and evidence lost | illustrative | None blocking. |
| route-r-projection | kg-r-projection | edge view → topology → evidence | Lines 702–731 compute path, components and degrees | Unit costs and weak connectivity | Two-hop path and three weak components | Structure describes the chosen view | Projection cannot answer dated evidence questions | illustrative | None blocking. |

## Historical adversarial depth gate at 0152148

Locators refer to `primer_knowledge_graph/primer_knowledge_graph.md` at
`0152148`. Verified means the teaching is present, not that citations or
accessibility have been approved.

| route_id | route tier | concept_id | explanation locator | example/action locator | interpretation locator | limitation locator | evidence revision | reviewer | status | finding | scope decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| route-python-duckdb | primary | kg-boundary | `primer_knowledge_graph/primer_knowledge_graph.md:45` | `primer_knowledge_graph/primer_knowledge_graph.md:65` | `primer_knowledge_graph/primer_knowledge_graph.md:73` | `primer_knowledge_graph/primer_knowledge_graph.md:75` | 0152148 | Codex | verified | Questions bound admissible evidence. | Retain. |
| route-python-duckdb | primary | kg-mentions | `primer_knowledge_graph/primer_knowledge_graph.md:85` | `primer_knowledge_graph/primer_knowledge_graph.md:104` | `primer_knowledge_graph/primer_knowledge_graph.md:117` | `primer_knowledge_graph/primer_knowledge_graph.md:119` | 0152148 | Codex | verified | Context supports links and Alex requires abstention. | Retain. |
| route-python-duckdb | primary | kg-claims | `primer_knowledge_graph/primer_knowledge_graph.md:123` | `primer_knowledge_graph/primer_knowledge_graph.md:127` | `primer_knowledge_graph/primer_knowledge_graph.md:169` | `primer_knowledge_graph/primer_knowledge_graph.md:125` | 0152148 | Codex | verified | Source-specific assertions preserve qualifications. | Retain. |
| route-python-duckdb | primary | kg-temporal | `primer_knowledge_graph/primer_knowledge_graph.md:187` | `primer_knowledge_graph/primer_knowledge_graph.md:193` | `primer_knowledge_graph/primer_knowledge_graph.md:213` | `primer_knowledge_graph/primer_knowledge_graph.md:189` | 0152148 | Codex | verified | Classification and policy are distinguished. | Retain. |
| route-python-duckdb | primary | kg-extraction | `primer_knowledge_graph/primer_knowledge_graph.md:141` | `primer_knowledge_graph/primer_knowledge_graph.md:145` | `primer_knowledge_graph/primer_knowledge_graph.md:149` | `primer_knowledge_graph/primer_knowledge_graph.md:153` | 0152148 | Codex | verified | Source spans produce candidates and refusals. | Retain. |
| route-python-duckdb | primary | kg-duckdb | `primer_knowledge_graph/primer_knowledge_graph.md:790` | `primer_knowledge_graph/primer_knowledge_graph.md:171` | `primer_knowledge_graph/primer_knowledge_graph.md:177` | `primer_knowledge_graph/primer_knowledge_graph.md:792` | 0152148 | Codex | verified | Hand ledger and optional persistence are distinguished. | Retain. |
| route-python-duckdb | primary | kg-queries | `primer_knowledge_graph/primer_knowledge_graph.md:217` | `primer_knowledge_graph/primer_knowledge_graph.md:250` | `primer_knowledge_graph/primer_knowledge_graph.md:264` | `primer_knowledge_graph/primer_knowledge_graph.md:274` | 0152148 | Codex | verified | Bindings and classifications support interpreted answers. | Retain. |
| route-python-duckdb | primary | kg-correction | `primer_knowledge_graph/primer_knowledge_graph.md:282` | `primer_knowledge_graph/primer_knowledge_graph.md:304` | `primer_knowledge_graph/primer_knowledge_graph.md:329` | `primer_knowledge_graph/primer_knowledge_graph.md:353` | 0152148 | Codex | verified | Failures and passes distinguish repair from revision. | Retain. |
| route-python-duckdb | primary | kg-evaluation | `primer_knowledge_graph/primer_knowledge_graph.md:417` | `primer_knowledge_graph/primer_knowledge_graph.md:425` | `primer_knowledge_graph/primer_knowledge_graph.md:433` | `primer_knowledge_graph/primer_knowledge_graph.md:453` | 0152148 | Codex | verified | Fixed items distinguish retrieval and answer quality. | Retain. |
| route-python-duckdb | primary | kg-privacy | `primer_knowledge_graph/primer_knowledge_graph.md:359` | `primer_knowledge_graph/primer_knowledge_graph.md:371` | `primer_knowledge_graph/primer_knowledge_graph.md:385` | `primer_knowledge_graph/primer_knowledge_graph.md:391` | 0152148 | Codex | verified | Audience views and paired outputs show leakage risks. | Retain. |
| route-r-projection | alternative | kg-r-projection | `primer_knowledge_graph/primer_knowledge_graph.md:682` | `primer_knowledge_graph/primer_knowledge_graph.md:686` | `primer_knowledge_graph/primer_knowledge_graph.md:704` | `primer_knowledge_graph/primer_knowledge_graph.md:729` | 0152148 | Codex | verified | Worked topology loses evidence qualifiers. | Retain. |
| route-graph-storage | reference-only | kg-rdf | `primer_knowledge_graph/primer_knowledge_graph.md:765` | `primer_knowledge_graph/primer_knowledge_graph.md:767` | `primer_knowledge_graph/primer_knowledge_graph.md:774` | `primer_knowledge_graph/primer_knowledge_graph.md:776` | 0152148 | Codex | verified | Qualified resources distinguish descriptions from assertions. | Retain. |
| route-graph-storage | reference-only | kg-property | `primer_knowledge_graph/primer_knowledge_graph.md:782` | `primer_knowledge_graph/primer_knowledge_graph.md:782` | `primer_knowledge_graph/primer_knowledge_graph.md:782` | `primer_knowledge_graph/primer_knowledge_graph.md:786` | 0152148 | Codex | verified | Representation must preserve evidence. | Retain. |
| route-graph-storage | reference-only | kg-storage | `primer_knowledge_graph/primer_knowledge_graph.md:784` | `primer_knowledge_graph/primer_knowledge_graph.md:786` | `primer_knowledge_graph/primer_knowledge_graph.md:784` | `primer_knowledge_graph/primer_knowledge_graph.md:786` | 0152148 | Codex | verified | Workload and exchange tests guide choice. | Retain. |

## Historical release readiness at 0152148

- Content gate: **pass** for the reviewed teaching routes at `0152148`.
- Release readiness: **not-ready**. Primary-source and version verification
  and semantic accessibility need review.
- Executable examples and pinned outputs passed within their stated scope;
  they do not establish citation accuracy or accessibility.

## Historical review at a02e3d9

Everything below this heading records the earlier review, its original line
numbers and decisions; it does not describe the current revision.

The reviewed source was committed at `a02e3d9`. The brief was revision r4 from
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

## Historical route transition evidence

All locators below refer to the historical source revision and all operations were
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

## Historical adversarial depth gate

Every row is a content judgement at `a02e3d9`. `verified` denotes
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

## Historical release readiness checklist

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
