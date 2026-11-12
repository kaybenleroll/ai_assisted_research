# Primer brief: Building Knowledge Graphs: From Sources to Verifiable Queries

- Issue and milestone: #398; related #397
- Brief revision: `kg-398-brief-r10`
- Source revision: `3f3d384`
- Revision state: Post-draft teaching-depth checkpoint on 12 November 2026,
  after the opening/Northbridge consolidation at `e60c339` and the
  schema/semantics bridge and central evidence graph at `3f3d384`. Exact
  current source locators and remaining verification boundaries are recorded
  below. Route tiers and all route and concept IDs are retained.
- Output baseline: The latest tracked published-output and
  accessibility-review baseline remains `c7b5a91`, for source `1ee9f80`.
  HTML/PDF outputs are stale pending regeneration at source revision
  `3f3d384`. The tracked audit still reviews `1ee9f80` against brief r8;
  neither its old locators nor its content, execution, and output checks
  establish verification of this revision. Re-audit and output regeneration
  remain separate from this checkpoint.
- Tracked path: `primer_knowledge_graph/primer_knowledge_graph.brief.md`
- Reader: Software or data practitioners new to graph modelling, evidence
  qualification, or graph-database trade-offs.
- Prerequisites: Familiarity with tables and identifiers for the standalone
  route. Python, SQL, and R apply to the optional implementation material.
- Problem and motivation: A graph-shaped answer is not automatically a true or
  complete answer. The reader needs a practical method for turning bounded
  source material into qualified claims, preserving evidence and uncertainty,
  querying the result, and knowing when to abstain, correct, or re-evaluate it.
- Intended outcome: The reader can explain what a knowledge graph adds beyond
  an ordinary table or graph drawing; design a bounded case; work from source
  mention to qualified claim to interpreted query result; recognise positive,
  negative, conflicting, and indeterminate evidence; diagnose a failed answer;
  make a documented correction; and choose whether a tabular, RDF, property-
  graph, or other serving representation is appropriate.
- Scope: Source boundaries and competency questions; mentions, entities and
  identifiers; qualified claims; temporal scope, polarity, provenance and
  uncertainty; conservative extraction and identity resolution; privacy;
  hand-worked construction, queries, diagnosis, and correction; validation
  and evaluation; the distinction between vocabulary, instance assertions,
  schema, ontology semantics, validation, and inference; an R
  `igraph`/`tidygraph` projection; RDF, SPARQL, SHACL and PROV-O; property
  graphs, Cypher, and graph-database storage trade-offs; release and
  governance. Python/DuckDB provides optional companion verification of
  bounded construction, queries, and correction.
- Exclusions: General-purpose NLP, production entity-resolution calibration or
  reconciliation, ontology engineering in depth, legal advice, vendor
  benchmarking, production deployment or access enforcement, a complete Neo4j
  integration, ranked semantic retrieval or GraphRAG, and claims that a
  synthetic fixture represents a real organisation.
- Proposed dependency-led route: Open with the problem, reader promise,
  essential vocabulary, and one compact preview of the Northbridge question;
  consolidate the early orientation so the reader reaches the worked problem
  before absorbing the full glossary. Develop the Northbridge case as one
  continuous source-to-answer-and-repair narrative, with source boundary,
  mentions and identity, qualified claims, temporal policy, queries,
  correction, disclosure, evaluation, and release regression as linked stages.
  Follow that case with the detailed evidence ledger and query mechanics, then
  transfer the reasoning to literature and dependency graphs. Add a focused
  bridge from local relations to vocabulary, schema, ontology semantics,
  validation, and inference using the existing Northbridge claims. Use the
  alternative R projection to show deliberate information loss, and keep RDF,
  property-graph, and storage material as bounded reference guidance. End
  with practice, limitations, and further reading.
- Approximate depth: Substantial, explanatory treatment. The document should
  grow where the dependency, worked case, or limitation requires it; word count
  is an outcome rather than a cap.
- Worked examples: Northbridge competency questions; a small labelled graph
  linked to its qualified evidence table; source sentence to mention, entity
  decision, claim, query, result and limitation; two Alex Kim identity
  abstention; direct, path, provenance, temporal and conflict questions; a
  deliberately broken extraction followed by correction and re-evaluation; a
  small schema/validation/inference contrast; research-literature and
  software-dependency transfer graphs; R shortest-path and component analysis;
  and storage-neutral comparisons of RDF and property graphs. Executable
  implementations remain companion evidence rather than the reader's primary
  route.
- Real-world cases: Northbridge is a synthetic organisational-policy case used
  because it exposes source authority, temporal conflict, identity ambiguity,
  privacy, and correction without implying access to real personal data. Brief
  contrast cases should be used only to explain why workload, provenance,
  update, and access requirements affect storage choice.
- Teaching-case contract: `primer_knowledge_graph/primer_knowledge_graph.case.md`
- Core-concept depth matrix: the matrix below; retain all IDs in the later audit.
- Route classification and teaching spines: The route classifications and teaching spines are specified below.
  - `route-python-duckdb` — `primary`: Northbridge questions motivate the
    organising model of evidence-backed claims. The opening walkthrough makes
    Q4's complete source-to-release spine prominent. Work the standalone case by
    hand from source excerpts through ledger construction, query, diagnosis,
    correction, authorised disclosure, evaluation, and release regression.
    Python/DuckDB is optional companion verification.
  - `route-r-projection` — `alternative`: the same bounded positive projection
    is used to demonstrate `igraph` paths/components and `tidygraph` node
    transformations; the result is interpreted as topology analysis, with the
    discarded claim semantics made explicit as its material limit.
  - `route-graph-storage` — `reference-only`: RDF/property graphs and graph
    databases are compared as representation and serving options, with one
    worked mapping and a workload-based choice guide, not a product survey or
    executed Neo4j route.
- Teaching devices: One opening orientation block introduces only the terms
  needed for the first Northbridge question. A compact labelled graph and its
  evidence table establish the relationship between topology, qualifiers,
  provenance, and an answer. The consolidated walkthrough follows the source
  → mention/entity → qualified claim → query → interpretation → correction →
  release chain; an ordered list shows the baseline → diagnosis → revised
  ledger → release regression cycle. A focused relation/schema/validation/
  inference comparison uses the same claims rather than introducing a second
  miniature system. Labels and alt text convey the stages without depending on
  colour. Current HTML/PDF presentation needs review after drafting.
  Retained-excerpt, mention-decision, span-to-assertion, and ledger tables
  supply the detailed hand replay beneath the opening flow. Three worked
  failures develop symptom, diagnosis, test, and change; a compact table
  retains the other diagnostic cases. The three-pass experiment distinguishes
  extraction repair from source correction. Evaluation follows the disclosure
  contract, with Pass A's inputs, arithmetic, and interpretation grouped in a
  worked note. One final release regression table gathers changed values,
  classifications, paths, and citations. H4 landmarks divide each long
  transfer case at source/model, query, correction, and audit transitions;
  labelled candidate records keep the literature bindings and evidence paths
  readable. A cross-case comparison covers entity grain, qualifiers, admissible joins,
  completeness, and correction dependencies. The optional storage reference
  uses mapping tables and an acceptance handoff to the worked answer records.
- Languages and executable examples: Python 3.12.15 with pinned DuckDB 1.4.3
  remains companion verification for the primary route; R 4.5.3 with directly
  checked `igraph` 2.3.0, `tidygraph` 1.3.1, and `dplyr` 1.2.1 remains
  companion verification for the alternative projection. Transitive
  dependencies, including `tibble`, are resolved from the dated package
  snapshot. Optional Python verification builds, closes,
  reopens, and queries a temporary database and exercises the bounded
  correction, rebuild, and re-evaluation. The published explanation supplies
  the worked reasoning and states each interchange boundary and the semantics
  discarded.
- Evidence plan: The scoped source review verified the DuckDB 1.4.3 interface,
  RDF 1.1, SPARQL 1.1, SHACL, PROV-O, Neo4j 5 MATCH, and the pinned R API
  claims against authoritative documentation on 11 November 2026 at source
  `1ee9f80`, as recorded in the tracked audit. This historical review does not
  cover the new RDFS bridge. Retain the exact sources and access boundary in
  the next audit; do not generalise this to a service integration or a
  latest-version claim.
- Open decisions:
  - Opening and Northbridge consolidation is implemented at `e60c339`.
    The checkpoint below follows the retained source, identity, temporal,
    policy, disclosure, evaluation, and correction records through the new
    headings.
  - The bounded schema/semantics bridge and labelled central evidence graph
    are implemented at `3f3d384`. The bridge distinguishes validation from
    inference using Northbridge assertions; ontology engineering remains
    excluded. The visual has descriptive alt text and a prose explanation;
    rendered presentation and semantic accessibility still need review.
  - Retain the R script's self-contained positive projection for this milestone.
    It is explicitly an alternative topology teaching route, not a synchronised
    view of a changed Python source. A generated projection would be a separate
    content change because it would alter the interchange boundary.
  - No Neo4j service integration is in scope. The reference comparison uses the
    Neo4j 5 MATCH manual, checked on 11 November 2026; a service test would be
    a separate issue.
  - The case contract was reconciled at `2d47558`: the reader-facing primary
    route is illustrative and standalone, while optional companion checks
    cover bounded operations. Execution evidence remains separate from the
    source-located teaching checkpoint.
  - The primary lab works source-version replay by hand. The optional Python
    companion rebuilds a changed retained excerpt in a fresh temporary
    database. Durable release publication is a production extension.

## Route-keyed worked-case trace

The trace binds the case to its stable route and concept IDs. Reader-facing
primary stages are illustrative hand-worked prose; optional companion checks
are listed separately as evidence. The alternative route has an executable
companion that constructs a graph from a precomputed positive fixture; the
ledger-to-projection derivation and interpretation are illustrative prose.
Executable denotes the companion's supported mode, not a run at `3f3d384`.
Reference-only material does not carry a continuous teaching spine.

| route_id | route tier | stage | concept_id(s) | Input and decision | Output handed to the next stage | Evidence mode and scope decision |
|---|---|---|---|---|---|---|
| route-python-duckdb | primary | Boundary and questions | kg-boundary | Declare Northbridge sources, authority, dates, and Q1–Q5 contracts | Bounded questions and refusal rules | `illustrative`; verify contracts against retained excerpts |
| route-python-duckdb | primary | Mentions and qualified claims | kg-mentions, kg-claims | Preserve source spans, distinguish mentions from entities, and retain source, interval and polarity | Candidate claims and evidence-bearing rows | `illustrative`; optional companion check `construction.py` covers declared patterns |
| route-python-duckdb | primary | Temporal and conservative construction | kg-temporal, kg-extraction | Classify bounded, unbounded and unknown horizons, refuse unsupported dates, and abstain on Alex identity | Source-derived `c1`, `c4`, `c5` plus refusal decisions | `illustrative`; optional companion extraction check covers fixture patterns |
| route-python-duckdb | primary | Ledger and evidence queries | kg-duckdb, kg-queries | Bind identifiers, select rows, join path hops, and classify dates in the printed ledger | Evidence rows and supported, refuted, or abstention results | `illustrative`; optional DuckDB reopen/query check is companion evidence |
| route-python-duckdb | primary | Diagnosis and correction | kg-correction | Diagnose the first evidence loss, compare omitted-negative, repaired, and changed-source runs, and replay R2 derivations | Revised evidence links, source comparison, and policy result | `illustrative`; optional companion verifies a bounded rebuild |
| route-python-duckdb | primary | Privacy and release boundary | kg-privacy | Compare ordinary citations, answers, and counts across paired releases | Approved evidence and the same ordinary outputs in both states | `illustrative`; synthetic disclosure test, not deployment evidence |
| route-python-duckdb | primary | Evaluate permitted outputs and release regression | kg-evaluation, kg-correction, kg-privacy | Score the synthetic items against the audience contract, then compare original and revised answers, paths, and citations | Interpreted measures and release acceptance expectations | `illustrative`; worked arithmetic and regression table, no deployment accuracy claim |
| route-r-projection | alternative | Positive projection construction | kg-r-projection | Read the declared positive interchange fixture and construct the projected vertices and relations | Five positive relations and eight vertices for path/component analysis | `executable` companion; earlier audit records a pass at `1ee9f80`, not a run at `3f3d384`; the prose derivation does not execute ledger filtering |
| route-r-projection | alternative | Interpret topology and return to evidence | kg-r-projection | Explain unit path cost, components, and discarded dates, polarity, provenance and claim IDs | A topology interpretation and a return path to the evidence ledger | `illustrative`; interpretation is checked against the fixture and ledger |
| route-graph-storage | reference-only | RDF, property graphs and storage choice | kg-rdf, kg-property, kg-storage | Compare qualified mappings and workload boundaries | A future storage decision and prospective test | `reference-only`; no continuous teaching spine or executed service migration |

## Review plan

- Whole-document checks: Inventory the complete source against every route and
  concept ID; inspect dependency order, compressed transitions, claims,
  examples, limitations, citations, accessibility, and committed HTML/PDF.
- Representative samples: Opening orientation; the source-to-claim tables;
  the ledger and temporal query; the three-pass correction lab; the R
  projection; the RDF/property-graph storage boundary; evaluation; privacy;
  and representative rendered pages containing code, tables, figures, and
  equations.
- Planned independent reviewers: One reviewer for pedagogical depth and route
  classification; one for the executable case and data semantics; one for
  current primary-source claims and storage contrasts. Reviewers report
  findings, not generic approval, and do not edit overlapping files.
- Content gate: Trace Northbridge by hand from the source excerpts through
  mention decisions, the assertion ledger, row selection, interpretation,
  diagnosis, correction, and re-evaluation. Check the optional DuckDB
  persistence and execution claims against the companion.
- Depth gate: For every route and concept below, require exact explanation,
  reader action or worked example, interpretation, and material limitation.
  A definition, list, citation, heading, or code output alone is not teaching
  evidence. Any primary or alternative row without those locators blocks
  readiness; reference-only rows need an explicit scope rationale.
- Release-readiness gate: Keep this separate from the content gate. Rebuild
  HTML/PDF after source changes; rebind the audit to the new source, brief, and
  output revisions; run current render QA and the documented keyboard,
  browser-accessibility-tree, screen-reader, and PDF tag-tree checks; record
  HTML accessibility as the target and the pinned PDF's `Tagged: no` status as
  an explicit limitation. Do not call a content pass release-ready.
- Case reconciliation: The contract at `2d47558` identifies the standalone
  illustrative route, optional companion commands, and their bounded checks.
  This checkpoint compares that promise with source `3f3d384`; the next audit
  must review the changed source and rebind its evidence.

## Optional branches and unresolved concepts

| route_id | optional branch | reader need | worked evidence added | material displaced or shortened | scope decision and reason |
|---|---|---|---|---|---|
| route-python-duckdb | Optional Python/DuckDB companion | Reproduce bounded construction, persistence, and correction checks | Temporary database build, reopen, parameterised queries, and bounded rebuild | No reader-facing prose; companion remains outside the main narrative | Retain as optional executable evidence; reconcile the case contract so it does not become a hidden prerequisite |
| route-r-projection | R topology projection | See how a lossy positive view supports path and component analysis | Pinned `igraph`/`tidygraph` projection and expected results | No synchronised projection of later corrected Python data | Retain as an alternative route because its information-loss boundary is a teaching result |
| route-graph-storage | RDF/property-graph reference | Compare representation and serving choices | One Northbridge mapping and workload comparison | No full service implementation or vendor survey | Retain as reference-only; it cannot carry a continuous teaching spine |
| route-graph-storage | Schema/validation/inference bridge | Transfer local relation reasoning into standards-aware semantics | One worked contrast using an existing Northbridge relation | Shorten the storage catalogue and remove repeated format definitions | Expand selectively; keep ontology engineering out of scope |

No missing reader-facing transition was identified in this scoped checkpoint.
The schema, validation, and inference bridge expands the existing
`kg-rdf`/`kg-claims` boundary; it adds no route or replacement concept ID.
The independent audit and outputs remain stale, and the new standards claims
and rendered visual remain unchecked at this revision. Those verification
gaps block current readiness, as detailed below.

## Post-draft teaching-depth checkpoint

Compared source `3f3d384` with brief r9's route-keyed trace and the case
contract reconciled at `2d47558`, on 12 November 2026. The locators below
identify inputs, operations, intermediate reasoning, results, interpretations,
and limits in the current source. This qualitative checkpoint supports the
next independent audit; it does not replace that audit or certify release
readiness. Recheck these locators after any further source or heading move.

- Draft source revision: `3f3d384`
- Brief revision reviewed: `kg-398-brief-r10`, checkpoint against the r9 plan
- Evidence modes: All reader-facing primary stages are `illustrative`.
  The R derivation and interpretation are also `illustrative`; only the
  companion's graph construction and topology operations are `executable`.
  The existing audit records earlier companion passes at `1ee9f80`; neither
  companion was run for this checkpoint. Prose, a manifest entry, or code
  inspection does not establish execution at `3f3d384`.

The route findings retain all existing tiers and concept IDs.

| route_id | brief trace or teaching device | draft locators and transition findings | decision and rationale | scope reduction and effect on reader promise |
|---|---|---|---|---|
| route-python-duckdb | Opening and consolidated Northbridge chain (`kg-boundary`, `kg-mentions`, `kg-claims`, `kg-temporal`, `kg-queries`) | `primer_knowledge_graph/primer_knowledge_graph.md:5` motivates the conflict; `:11` states the synthetic, software-free reading boundary. Full source locators below use this same file. `primer_knowledge_graph/primer_knowledge_graph.md:29` supplies R1/M1 inputs; `:33`–`:45` preserves identity, polarity, time, and ledger reasoning; `:65` selects `c1`/`c5`; `:67`–`:71` interprets disagreement, abstention, citations, and the changed reason on 16 March. | Retain primary. The two sources feed distinct qualified assertions, then selection and policy; the answer is bounded to the records rather than operational authority (`:23`, `:69`). | No new reduction. Standalone illustrative reasoning remains the reader promise. |
| route-python-duckdb | Central evidence graph (`kg-claims`, `kg-queries`) | `primer_knowledge_graph/primer_knowledge_graph.md:45` supplies the ledger context; `primer_knowledge_graph/primer_knowledge_graph.md:47` embeds the labelled graph with descriptive alt text; `primer_knowledge_graph/primer_knowledge_graph.md:49` explains source → assertion → proposition → Q4, and limits the answer arrow to comparison and policy. | Retain as an illustrative teaching device. Text carries polarity, intervals, disagreement, and withholding alongside the evidence tables; the figure does not replace the selection trace. | No new reduction. Source-level text inspected; regenerated HTML/PDF and semantic accessibility are not checked here. |
| route-python-duckdb | Detailed construction and ledger (`kg-boundary`, `kg-mentions`, `kg-claims`, `kg-extraction`, `kg-duckdb`) | `primer_knowledge_graph/primer_knowledge_graph.md:119` retains the excerpts; `:133` gives Q1–Q5 contracts; `:170`–`:187` reasons through identity and Alex abstention; `:197` defines relations; `:209`–`:223` works span decisions and refusals; `:227`–`:235` supplies the ledger; `:241` traces `c5` back to M1. | Retain primary. Each construction decision hands reviewable records to selection. Corpus and extraction completeness remain distinct at `:143`–`:145`; curated rows and optional mentions are explicit at `:225`. | No new reduction. The ledger is hand-worked; optional persistence is described at `primer_knowledge_graph/primer_knowledge_graph.md:867`–`:869`, without execution evidence from this checkpoint. |
| route-python-duckdb | Temporal classification and evidence queries (`kg-temporal`, `kg-queries`) | `primer_knowledge_graph/primer_knowledge_graph.md:255`–`:261` defines and applies horizons; `:318` binds Q4 and classifies both rows; `:322`–`:332` gives date results and explains changed abstention reasons. `primer_knowledge_graph/primer_knowledge_graph.md:336` joins `c1` to `c3`; `:340` dates each hop; `:342` rejects propagation to Orion. | Retain primary. Binding, per-row classification, comparison, and policy remain separate; the two-hop result retains its evidence and intersection of supported periods. | No new reduction. Unknown duration is not continuation; reachability is not an applicability inference. |
| route-python-duckdb | Diagnosis, repair, and source correction (`kg-correction`) | `primer_knowledge_graph/primer_knowledge_graph.md:75`–`:79` connects omission, repair, and R2 to changed answers. `primer_knowledge_graph/primer_knowledge_graph.md:363`–`:381` diagnoses the first loss; `:398`–`:412` works passes A/B/C and R2 derivations; `:414`–`:420` interprets refutation, revised citations, affected paths, and the need to preserve old evidence. | Retain primary. Restoring M1 denial repairs construction; changing R1 to R2 changes source evidence. The same question and policy expose the different causes. | No new reduction. Hypothetical correction and bounded companion rebuild do not establish durable release publication. |
| route-python-duckdb | Disclosure, evaluation, and release (`kg-privacy`, `kg-evaluation`, `kg-correction`) | `primer_knowledge_graph/primer_knowledge_graph.md:83`–`:91` completes the opening chain. `primer_knowledge_graph/primer_knowledge_graph.md:441` fixes paired inputs and approved excerpts; `:445`–`:456` derives equal ordinary answers, citations, and counts, with disclosure limits. `:488`–`:500` supplies Q4 evidence items, Pass A arithmetic, interpretation, and Pass B. `:528`–`:542` compares release results, classifications, paths, carry-forward citations, and audience views. | Retain primary. Audience selection precedes evaluation; corrected derivations reach a final release regression even where displayed values remain equal (`:540`). | No new reduction. Synthetic evaluation and disclosure expectations provide no deployment accuracy or access-enforcement evidence (`:520`, `:544`). |
| route-python-duckdb | Schema/semantics bridge shared with `route-graph-storage` (`kg-claims`, `kg-rdf`) | `primer_knowledge_graph/primer_knowledge_graph.md:197` supplies local relation definitions; `primer_knowledge_graph/primer_knowledge_graph.md:826`–`:828` distinguishes vocabulary, instance assertion, schema, and ontology; `:830` works the deliberately asserted `c3` affiliation and inferred participant classes; `:832` contrasts missing-source validation on `c1`; `:834` bounds the transfer to storage mappings. | Retain bounded illustrative expansion. Formal classification, validation failure, and source evidence have distinct premises and consequences; qualified `c3` alone does not assert an unqualified affiliation (`:830`). | No route or concept change. Ontology engineering remains excluded. No reasoner or SHACL execution is claimed; new RDFS claims need the next source-verification pass. |
| route-r-projection | Input, projection derivation, and companion construction (`kg-r-projection`) | `primer_knowledge_graph/primer_knowledge_graph.md:747` motivates a structural question; `:751` selects positives and deduplicates triples; `:755`–`:765` hands five edges and eight vertices to analysis, explaining six positive assertions, isolates, and information loss. `primer_knowledge_graph/primer_knowledge_graph.md:796` describes the companion. | Retain alternative. Prose derives the view; `primer_knowledge_graph/examples/r/knowledge_graph.R:14`–`:22` reads the precomputed fixture and constructs the graph, rather than executing the ledger-to-projection derivation. | Existing scope reduction retained: independent positive fixture, with no synchronised projection of corrected Python data (`primer_knowledge_graph/primer_knowledge_graph.md:869`). Execution at `3f3d384` is not checked. |
| route-r-projection | Topology operation, result, interpretation, and limit (`kg-r-projection`) | `primer_knowledge_graph/primer_knowledge_graph.md:769` works the two-hop path; `:771` limits unit costs; `:773` derives three weak components; `:777`–`:788` derives and interprets degrees. `primer_knowledge_graph/primer_knowledge_graph.md:792`–`:794` returns unchanged topology to changed dated evidence and explains why missing edges do not settle Q4. | Retain alternative. Intermediate neighbour expansion, weak connectivity, and degree counts support the results. R operations and assertions are inspectable at `primer_knowledge_graph/examples/r/knowledge_graph.R:27`–`:52`; that inspection is not execution. | Existing information-loss boundary retained: dates, polarity, provenance, and assertion identity are discarded. The reader can analyse topology, but must return to the evidence ledger for applicability. |
| route-graph-storage | Reference mappings and workload choice (`kg-rdf`, `kg-property`, `kg-storage`) | `primer_knowledge_graph/primer_knowledge_graph.md:840`–`:855` develops RDF mapping, query, constraint, and provenance reasoning; `:859` maps qualified property-graph relationships; `:861`–`:863` compares workloads and proposes an exchange test; `:871` uses worked answer records as acceptance criteria. | Retain reference-only. The bridge prepares interpretation of the mappings; the exchange test is prospective. | Existing scope reduction retained: no executed service migration, Neo4j integration, or benchmark; no continuous storage teaching spine promised. |

Locator changes are substantive evidence changes for the next audit. The old
opening at source `1ee9f80` lines 3–75 is now lines 3–19; the old Northbridge
overview at 77–141 is now the continuous chain at 21–91. The primary route
anchor moved from 143 to 93, the ledger from 197 to 147, correction from 398
to 348, and disclosure/release from 472 to 422. The R route moved from 795
to 745; its construction, calculations, and return-to-evidence passages now
begin at 749, 767, and 790. The central visual at 47–49 and bridge at
824–834 are new. The storage route anchor moved from 874 to 836. These are
locators in `primer_knowledge_graph/primer_knowledge_graph.md`, not rendered
page numbers; the independent audit must recheck its concept and transition
locators rather than apply a uniform line offset.

No route was demoted and no concept ID was retired. The retained scope
reductions allow standalone primary reasoning, bounded alternative topology,
and storage reference guidance. No additional teaching-depth gap was found
in these transitions. Independent whole-document review, verification of the
new bridge's standards claims, and regenerated visual/accessibility review
remain unresolved. Earlier template/PDF accessibility findings remain open
in the tracked audit; this source checkpoint does not clear them.

Checks on 12 November 2026: `git diff --check` passed. The evidence/schema
command was:

```bash
just check-primer-evidence primer_knowledge_graph/primer_knowledge_graph.brief.md primer_knowledge_graph/primer_knowledge_graph.audit.md
```

It returned exit 1 with exactly two findings: "brief and audit:
Source/Reviewed revision does not match" and "brief and audit: Source revision
does not match". No other schema finding was reported. The brief now binds
`3f3d384`, while the unchanged audit's Source/Reviewed revision remains
`1ee9f80`; that mismatch blocks a current paired evidence pass. Re-audit and
regenerate outputs at the new source revision before a release decision.

## Core-concept depth matrix

| route_id | route tier | concept_id | concept | reader action | mechanism or reasoning | significance | teaching device | worked evidence | interpretation | limitations | downstream use | Evidence/source plan |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| route-python-duckdb | primary | kg-boundary | Boundary and competency questions | Define what a graph may answer and what it must refuse | Scope, source authority, population and completeness govern query meaning | Prevents bounded absence becoming a universal negative | Northbridge question table and boundary decision | Q1–Q5 with source, date, or audience constraints | State the evidence and scope for each answer | Synthetic sources are incomplete | Drives ledger selection and query tests | Check the contracts against the retained excerpts |
| route-python-duckdb | primary | kg-mentions | Mentions, entities and identifiers | Preserve a mention before linking it to an entity | A string occurrence, real-world entity and stable identifier are different objects | Prevents premature identity collapse | Two Alex Kim records and mention ledger | Unresolved meeting mention | Abstain when candidates remain indistinguishable | IDs are local to the case | Enables review and later reconciliation | Cite identifier and entity-modelling sources |
| route-python-duckdb | primary | kg-claims | Qualified claims | Represent who/what/where/when/source/polarity for a claim | A graph edge needs qualifiers and evidence to support interpretation | Makes answers auditable and conflicting | Claim ledger mapped from source sentences | `c1`, `c4`, `c5` with locators | Explain support, refutation and conflict | Curated rows are not extraction proof | Supports DuckDB, RDF and property mappings | Verify vocabulary and provenance claims |
| route-python-duckdb | primary | kg-temporal | Temporal scope and polarity | Query a claim for a date without inventing continuity | bounded, unbounded and unknown intervals behave differently; negative claims are evidence | Avoids false current answers | Date classifier and conflict cases | 1 March, 15 March, 16 March and 1 April | Interpret applicable, outside and indeterminate | Encoded dates are case assumptions | Powers release and re-evaluation | Verify date semantics in source and code |
| route-python-duckdb | primary | kg-extraction | Conservative extraction and abstention | Extract only declared patterns and record refusals | Narrow patterns, offsets and methods make construction inspectable | Makes failure diagnosable instead of silently broad | Source sentence table and refusal cases | Rejected unsupported sentence and accepted candidates | Identify extraction uncertainty | Not a general NLP extractor | Supports tests and human review | Verify implementation claims against code |
| route-python-duckdb | primary | kg-duckdb | Tabular ledger and optional DuckDB representation | Follow a ledger row to its source and mention evidence by hand. Optionally build, reopen, and query the temporary database | Assertion keys connect the ledger to source and optional mention records. The companion uses parameters for query values | Makes persistence and evidence links inspectable | Worked ledger and optional companion notes | Source lookup for `c5` and `c7`. Reopened queries in the companion | Distinguish persistence from the full ledger contract | Companion validation is bounded to the fixture | Supports local verification and storage comparison | Verify pinned DuckDB 1.4.3 behaviour |
| route-python-duckdb | primary | kg-queries | Direct, two-hop and provenance queries | Answer a competency question from the printed ledger | Bind IDs and predicates, match the shared Atlas ID, and retain the scope and evidence for each row | Makes path and answer dependencies inspectable | Hand-worked lookups, Q4 classifications, and bounded path | Owner, version, provenance, and dated two-hop results | Explain which rows support the answer and which are excluded | Query scope follows fixture boundary | Feeds R projection and storage comparison | Check the results against the ledger and excerpts |
| route-python-duckdb | primary | kg-correction | Diagnosis, correction and re-evaluation | Locate a bad answer and replay the corrected ledger by hand | Source-version links and temporal classifications determine which answers and citations need updating | Makes changed conclusions and unchanged values with revised evidence auditable | Worked failures, correction flow, three-pass lab, R2 derivations, and final release regression | Omitted denial, restored denial, revised interval, and R2 carry-forwards | Explain the source comparison and applicability outcome separately | Optional companion verifies a bounded rebuild. Durable release publication needs further work | Establishes release regression behaviour | Check R1/R2 replay and the companion's stated limits |
| route-python-duckdb | primary | kg-evaluation | Gold sets and useful measures | Adjudicate an answer against supporting/opposing evidence | Precision/recall depend on item definitions and adjudication, not arithmetic alone | Northbridge evidence-backed gold items | Q1–Q5 mapped to actual claims and audience contracts | Score Pass A with explicit inputs, arithmetic, and interpretation | Interpret false positives and abstentions | Small gold set is illustrative | Guides monitoring and review | Source evaluation definitions and case labels |
| route-python-duckdb | primary | kg-privacy | Proportionate identity and access | Resolve the approved sentence locator and compare outputs across paired releases | Select the audience view before evaluating citations, paths, and counts | Prevents citation and candidate-count disclosure | Paired Alex Kim release test | Same Q4 answer and citation, Q5 response, and visible count in both ordinary views | Explain why the ordinary result stays fixed while the authorised view differs | The worked test models disclosure behaviour in a synthetic fixture | Informs governance and release regression checks | Check the paired outputs against the view rules |
| route-r-projection | alternative | kg-r-projection | Positive topology projection | Analyse selected relations in R | Projection drops polarity, dates, provenance and claim identity | Demonstrates graph analysis without pretending it preserves evidence | `igraph` path/components plus `tidygraph` node table | Same five positive relations and expected path | Interpret topology only | Lossy projection cannot answer evidence questions | Useful for exploratory structural analysis | Verify pinned R APIs and output |
| route-graph-storage | reference-only | kg-rdf | RDF and qualified claims | Map a claim ledger to triples and provenance | URI identity and reification/qualified patterns preserve semantics differently | Offers interoperability vocabulary | Northbridge assertion-resource mapping and explained SPARQL patterns | Hand-worked representation and query reasoning | State what the mapping retains | Mapping is illustrative; no code snippets | Supports standards-aware exchange | Verify W3C RDF/SPARQL/PROV-O claims |
| route-graph-storage | reference-only | kg-property | Property graphs and Cypher | Compare a qualified claim mapping with a property graph | Node/relationship properties and query patterns make different trade-offs | Clarifies representation versus truth | Qualified relationship mapping beside RDF | Explained pattern matching | Interpret convenience and loss | Product/version semantics vary | Informs serving choice | Verify named Cypher manual |
| route-graph-storage | reference-only | kg-storage | Graph-database storage choice | Choose DuckDB, a graph database, or another store for a workload | Workload, updates, traversal, provenance and operations determine the boundary | Avoids “graph database” as automatic solution | Workload comparison and prospective exchange test | Same questions mapped to storage needs | Explain why no universal winner follows | No benchmark or Neo4j run in scope | Provides a future integration brief | Verify only current official claims |
