# Primer brief: Building Knowledge Graphs: From Sources to Verifiable Queries

- Issue and milestone: #398; related #397
- Brief revision: `kg-398-brief-r3`
- Source revision: `f730591`
- Tracked path: `primer_knowledge_graph/primer_knowledge_graph.brief.md`
- Reader: Software or data practitioners who understand tables, JSON, basic
  Python or SQL, and reproducible data work, but do not yet understand graph
  modelling, evidence qualification, or graph-database trade-offs.
- Prerequisites: Basic relational data and Python/SQL; no prior RDF, ontology,
  graph database, R, or formal provenance experience is assumed.
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
  Python/DuckDB construction and query; executable diagnosis/correction;
  validation and evaluation; an R `igraph`/`tidygraph` projection; RDF,
  SPARQL, SHACL and PROV-O; property graphs, Cypher, and graph-database
  storage trade-offs; release and governance.
- Exclusions: General-purpose NLP, ontology engineering in depth, legal advice,
  vendor benchmarking, production deployment, a complete Neo4j integration,
  and claims that a synthetic fixture represents a real organisation.
- Proposed dependency-led route: Explain what a knowledge graph is and when it
  helps; establish the Northbridge boundary and competency questions; preserve
  source mentions and distinguish them from entities; model qualified claims
  with time, polarity, provenance and uncertainty; work one source sentence
  through construction to a query result; extract conservatively and abstain
  on identity; use direct, path, temporal and provenance questions; diagnose a
  failed extraction, rebuild after a source correction, and re-evaluate the
  answer; then compare RDF, property-graph, tabular, and R projection choices
  before closing with governance and release.
- Approximate depth: Substantial, explanatory treatment. The document should
  grow where the dependency, worked case, or limitation requires it; word count
  is an outcome rather than a cap.
- Worked examples: Northbridge competency questions; a small graph and its
  qualified evidence table; comparative policy, research-literature, and
  software-dependency graphs; source sentence to mention, entity decision,
  claim, query, result and limitation; two Alex Kim identity abstention;
  direct, path, provenance, temporal and conflict questions; a deliberately
  broken extraction followed by correction and re-evaluation; R shortest-path
  and component analysis; and storage-neutral comparisons of RDF and property
  graphs. Executable implementations remain companion evidence rather than the
  reader's primary route.
- Real-world cases: Northbridge is a synthetic organisational-policy case used
  because it exposes source authority, temporal conflict, identity ambiguity,
  privacy, and correction without implying access to real personal data. Brief
  contrast cases should be used only to explain why workload, provenance,
  update, and access requirements affect storage choice.
- Teaching-case contract: `primer_knowledge_graph/primer_knowledge_graph.case.md`
- Core-concept depth matrix: the matrix below; retain all IDs in the later audit.
- Route classification and teaching spines: The route classifications and teaching spines are specified below.
  - `route-python-duckdb` — `primary`: Northbridge questions motivate the
    organising model of evidence-backed claims; the standalone case constructs,
    queries, diagnoses, corrects, rebuilds, re-evaluates, and states where the
    method abstains. Python/DuckDB remains companion verification evidence.
  - `route-r-projection` — `alternative`: the same bounded positive projection
    is used to demonstrate `igraph` paths/components and `tidygraph` node
    transformations; the result is interpreted as topology analysis, with the
    discarded claim semantics made explicit as its material limit.
  - `route-graph-storage` — `reference-only`: RDF/property graphs and graph
    databases are compared as representation and serving options, with one
    worked mapping and a workload-based choice guide, not a product survey or
    executed Neo4j route.
- Figures, tables, and equations: Preserve the useful source-to-ledger pipeline,
  make the standalone graph and source-to-answer walkthrough central, add a
  correction-loop diagram, retain the source/claim and storage comparison
  tables, add before/after answer tables, and use equations only where they
  clarify evaluation measures or temporal classification. Do not make code or
  repository file targets necessary to understand a worked example.
- Languages and executable examples: Python 3.12 with pinned DuckDB remains
  companion verification for the primary route; R with pinned `igraph`,
  `tidygraph`, `dplyr`, and `tibble` remains companion verification for the
  alternative projection. Python must execute the correction/rebuild/
  re-evaluation path. The published explanation must remain readable without
  opening or running either implementation, and must state each interchange
  boundary and discarded semantic.
- Evidence plan: Verify current DuckDB 1.4.3 behaviour against official
  documentation; verify RDF 1.1, SPARQL 1.1, SHACL and PROV-O statements against
  W3C specifications; verify the narrow Cypher claims against the named
  official manual; verify the R APIs and reported output against pinned package
  documentation and the executable example; reconcile every source-sensitive
  claim with its citation, version and access date.
- Open decisions:
  - Retain the R script's self-contained positive projection for this milestone.
    It is explicitly an alternative topology teaching route, not a synchronised
    view of a changed Python source. A generated projection would be a separate
    content change because it would alter the interchange boundary.
  - Which exact Neo4j/Cypher version to name in the reference branch. Evidence
    needed: current official documentation; do not add an integration until a
    separate issue authorises a service test.
  - Keep the correction demonstration as a changed retained excerpt rebuilt in
    a fresh temporary database. A durable source version is described as a
    production extension, not promised by this milestone.

## Route-keyed worked-case trace

The following trace binds the continuous case to the existing stable route and
concept IDs. It is a planning and post-draft comparison spine, not a claim that
every stage is executable. `Illustrative` means the reader can follow the
reasoning in the prose but the example does not independently run that whole
question; `executable` is reserved for the bounded Python or R operations
asserted by the examples.

| route_id | route tier | stage | concept_id(s) | Input and decision | Output handed to the next stage | Evidence mode and scope decision |
|---|---|---|---|---|---|---|
| route-python-duckdb | primary | Boundary and questions | kg-boundary | Declare Northbridge sources, authority, dates, and Q1–Q5 contracts | Bounded questions and refusal rules | illustrative; Q2 owner continuation remains an explicitly illustrative answer |
| route-python-duckdb | primary | Mentions and qualified claims | kg-mentions, kg-claims | Preserve source spans, distinguish mentions from entities, and retain source, interval and polarity | Candidate claims and evidence-bearing rows | executable for declared patterns; curated rows remain illustrative |
| route-python-duckdb | primary | Temporal and conservative construction | kg-temporal, kg-extraction | Classify bounded, unbounded and unknown horizons; refuse unsupported dates and abstain on Alex identity | Validated source-derived `c1`, `c4`, `c5` plus refusal decisions | executable for the declared fixture patterns; not a general extractor |
| route-python-duckdb | primary | DuckDB representation and queries | kg-duckdb, kg-queries | Store, reopen, and query direct, two-hop, provenance and dated evidence | Evidence rows and supported, refuted, or abstention results | executable for the bounded fixture; no production schema claim |
| route-python-duckdb | primary | Diagnosis, correction and re-evaluation | kg-correction, kg-evaluation | Compare omitted-negative, repaired, and changed-source constructions; explain the Q1–Q5 score as synthetic | Changed answer plus an explicit evaluation limitation | correction path executable; Q1–Q5 score illustrative and not independently adjudicated |
| route-python-duckdb | primary | Privacy and release boundary | kg-privacy | Apply audience-specific disclosure and state source, coverage and governance limits | A bounded answer or abstention with a release limitation | illustrative governance; no enforced access-control implementation |
| route-r-projection | alternative | Positive projection | kg-r-projection | Read the declared positive interchange fixture and analyse paths/components | Topology results without claim qualifiers | executable alternative; deliberately not synchronised with changed Python input |
| route-r-projection | alternative | Interpret topology and return to evidence | kg-r-projection | Explain unit path cost, components, and discarded dates, polarity, provenance and claim IDs | A topology interpretation and a return path to DuckDB evidence | illustrative interpretation around an executable projection; cannot answer evidence questions |
| route-graph-storage | reference-only | RDF, property graphs and storage choice | kg-rdf, kg-property, kg-storage | Compare qualified mappings and workload boundaries | A future storage decision and prospective test | reference-only; no continuous teaching spine or executed service migration promised |

## Review plan

- Whole-document checks: Inventory the complete source against every route and
  concept ID; inspect dependency order, compressed transitions, claims,
  examples, limitations, citations, accessibility, and committed HTML/PDF.
- Representative samples: Opening orientation; the source-to-claim transition;
  the DuckDB schema and temporal query; the diagnosis/correction loop; the R
  projection; the RDF/property-graph storage boundary; evaluation; privacy;
  and representative rendered pages containing code, tables, figures, and
  equations.
- Planned independent reviewers: One reviewer for pedagogical depth and route
  classification; one for the executable case and data semantics; one for
  current primary-source claims and storage contrasts. Reviewers report
  findings, not generic approval, and do not edit overlapping files.
- Content gate: Trace Northbridge from source input through construction,
  intermediate claim representation, stored DuckDB result, reader-facing
  operation, interpretation, diagnosis, correction, rebuild, re-evaluation,
  and failure boundary. A fixture or passing script alone is insufficient.
- Depth gate: For every route and concept below, require exact explanation,
  reader action or worked example, interpretation, and material limitation.
  A definition, list, citation, heading, or code output alone is not teaching
  evidence. Any primary or alternative row without those locators blocks
  readiness; reference-only rows need an explicit scope rationale.

## Core-concept depth matrix

| route_id | route tier | concept_id | concept | reader action | mechanism or reasoning | significance | teaching device | worked evidence | interpretation | limitations | downstream use | Evidence/source plan |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| route-python-duckdb | primary | kg-boundary | Boundary and competency questions | Define what a graph may answer and what it must refuse | Scope, source authority, population and completeness govern query meaning | Prevents bounded absence becoming a universal negative | Northbridge question table and boundary decision | Three questions with source and date constraints | State what each answer does and does not establish | Synthetic sources are incomplete | Drives schema and query tests | Cite source-boundary and completeness guidance |
| route-python-duckdb | primary | kg-mentions | Mentions, entities and identifiers | Preserve a mention before linking it to an entity | A string occurrence, real-world entity and stable identifier are different objects | Prevents premature identity collapse | Two Alex Kim records and mention ledger | Unresolved meeting mention | Abstain when candidates remain indistinguishable | IDs are local to the case | Enables review and later reconciliation | Cite identifier and entity-modelling sources |
| route-python-duckdb | primary | kg-claims | Qualified claims | Represent who/what/where/when/source/polarity for a claim | A graph edge needs qualifiers and evidence to support interpretation | Makes answers auditable and conflicting | Claim ledger mapped from source sentences | `c1`, `c4`, `c5` with locators | Explain support, refutation and conflict | Curated rows are not extraction proof | Supports DuckDB, RDF and property mappings | Verify vocabulary and provenance claims |
| route-python-duckdb | primary | kg-temporal | Temporal scope and polarity | Query a claim for a date without inventing continuity | bounded, unbounded and unknown intervals behave differently; negative claims are evidence | Avoids false current answers | Date classifier and conflict cases | 1 March, 15 March, 16 March and 1 April | Interpret applicable, outside and indeterminate | Encoded dates are case assumptions | Powers release and re-evaluation | Verify date semantics in source and code |
| route-python-duckdb | primary | kg-extraction | Conservative extraction and abstention | Extract only declared patterns and record refusals | Narrow patterns, offsets and methods make construction inspectable | Makes failure diagnosable instead of silently broad | Source sentence table and refusal cases | Rejected unsupported sentence and accepted candidates | Identify extraction uncertainty | Not a general NLP extractor | Supports tests and human review | Verify implementation claims against code |
| route-python-duckdb | primary | kg-duckdb | File-backed DuckDB representation | Build, close, reopen and query the ledger | Tables preserve claims, sources, mentions and evidence spans; parameters constrain queries | Gives a reproducible working baseline | Schema and file-backed runtime | Reopened database assertions | Distinguish storage from graph semantics | Entities/relations projection is bounded | Provides durable local analysis | Verify pinned DuckDB 1.4.3 behaviour |
| route-python-duckdb | primary | kg-queries | Direct, two-hop and provenance queries | Answer a competency question with source context | Joins and bounded paths expose topology without discarding qualifiers | Shows why graph questions still need evidence | SQL query walkthrough | Direct, two-hop and provenance results | Interpret rows as evidence, not truth | Query scope follows fixture boundary | Feeds R projection and storage comparison | Verify SQL/runtime claims |
| route-python-duckdb | primary | kg-correction | Diagnosis, correction and re-evaluation | Locate a bad answer, change the source-derived input, rebuild and compare | A correction is useful only when its downstream answer changes as expected | Before/after correction loop | Deliberate extraction failure and changed end date | Failing answer, repaired claim, changed answer | Explain which stage changed and why | Synthetic mutation is not production governance | Establishes release regression behaviour | Verify executable assertions and case limits |
| route-python-duckdb | primary | kg-evaluation | Gold sets and useful measures | Adjudicate an answer against supporting/opposing evidence | Precision/recall depend on item definitions and adjudication, not arithmetic alone | Northbridge evidence-backed gold items | Q1–Q5 remapped to actual claims | Label and measure one answer set | Interpret false positives and abstentions | Small gold set is illustrative | Guides monitoring and review | Source evaluation definitions and case labels |
| route-python-duckdb | primary | kg-privacy | Proportionate identity and access | Decide what to expose and to whom | Identity resolution and provenance can increase inference risk | Prevents a useful graph becoming an unsafe disclosure | Alex Kim access scenario | Reviewer versus ordinary-user query | Explain allow, redact or abstain | Synthetic access rules are not policy | Informs governance and release | Verify privacy claims and state assumptions |
| route-r-projection | alternative | kg-r-projection | Positive topology projection | Analyse selected relations in R | Projection drops polarity, dates, provenance and claim identity | Demonstrates graph analysis without pretending it preserves evidence | `igraph` path/components plus `tidygraph` node table | Same five positive relations and expected path | Interpret topology only | Lossy projection cannot answer evidence questions | Useful for exploratory structural analysis | Verify pinned R APIs and output |
| route-graph-storage | reference-only | kg-rdf | RDF and qualified claims | Map a claim ledger to triples and provenance | URI identity and reification/qualified patterns preserve semantics differently | Offers interoperability vocabulary | One Northbridge claim in Turtle/SPARQL | Illustrative mapping and query | State what the mapping retains | Snippets are unexecuted | Supports standards-aware exchange | Verify W3C RDF/SPARQL/PROV-O claims |
| route-graph-storage | reference-only | kg-property | Property graphs and Cypher | Compare a qualified claim mapping with a property graph | Node/relationship properties and query patterns make different trade-offs | Clarifies representation versus truth | Cypher-shaped mapping beside RDF | Illustrative direct/path query | Interpret convenience and loss | Product/version semantics vary | Informs serving choice | Verify named Cypher manual |
| route-graph-storage | reference-only | kg-storage | Graph-database storage choice | Choose DuckDB, a graph database, or another store for a workload | Workload, updates, traversal, provenance and operations determine the boundary | Avoids “graph database” as automatic solution | Decision table and prospective smoke test | Same questions mapped to storage needs | Explain why no universal winner follows | No benchmark or Neo4j run in scope | Provides a future integration brief | Verify only current official claims |
