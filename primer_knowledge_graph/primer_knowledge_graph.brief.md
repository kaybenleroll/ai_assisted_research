# Primer brief: Building Knowledge Graphs: From Sources to Verifiable Queries

- Issue and milestone: #398; related #397
- Brief revision: `kg-398-brief-r5`
- Source revision: `85d0535`
- Revision state: Editorial source and outputs committed at the source revision
  above. Audit and release readiness are recorded separately.
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
  hand-worked construction, queries, diagnosis, and correction;
  validation and evaluation; an R `igraph`/`tidygraph` projection; RDF,
  SPARQL, SHACL and PROV-O; property graphs, Cypher, and graph-database
  storage trade-offs; release and governance. Python/DuckDB provides optional
  companion verification of bounded construction, queries, and correction.
- Exclusions: General-purpose NLP, ontology engineering in depth, legal advice,
  vendor benchmarking, production deployment, a complete Neo4j integration,
  and claims that a synthetic fixture represents a real organisation.
- Proposed dependency-led route: Explain what a knowledge graph is and when it
  helps; establish the Northbridge boundary and competency questions; preserve
  source mentions and distinguish them from entities; model qualified claims
  with time, polarity, provenance and uncertainty; work one source sentence
  through construction to a query result; extract conservatively and abstain
  on identity; use direct, path, temporal and provenance questions; diagnose a
  failed extraction and work the revised ledger by hand; define authorised
  disclosure and release products; evaluate those permitted outputs; then
  check the final release regression. Transfer the reasoning to research
  literature and software dependencies, comparing their modelling decisions.
  Use the alternative R projection and storage reference for topology and
  representation questions.
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
    organising model of evidence-backed claims. Work the standalone case by
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
- Teaching devices: Two native Pandoc text-flow diagrams show the
  source → mention/entity → qualified claim → evidenced answer chain and the
  baseline → diagnosis → revised ledger → release regression cycle. Labelled
  stages and operations remain selectable text in HTML/PDF; their meaning
  does not depend on colour or arrow glyphs alone. Line blocks keep this
  source-only revision free of code fences and build changes.
  Retained-excerpt, mention-decision, span-to-assertion, and ledger tables
  supply the detailed hand replay beneath the opening flow. Three worked
  failures develop symptom, diagnosis, test, and change; a compact table
  retains the other diagnostic cases. The three-pass experiment distinguishes
  extraction repair from source correction. Evaluation follows the disclosure
  contract, with Pass A's inputs, arithmetic, and interpretation grouped in a
  worked note. One final release regression table gathers changed values,
  classifications, paths, and citations. H4 landmarks divide each long
  transfer case at source/model, query, correction, and audit transitions;
  a cross-case comparison covers entity grain, qualifiers, admissible joins,
  completeness, and correction dependencies. The optional storage reference
  uses mapping tables and an acceptance handoff to the worked answer records.
- Languages and executable examples: Python 3.12 with pinned DuckDB remains
  companion verification for the primary route; R with pinned `igraph`,
  `tidygraph`, `dplyr`, and `tibble` remains companion verification for the
  alternative projection. Optional Python verification builds, closes,
  reopens, and queries a temporary database and exercises the bounded
  correction, rebuild, and re-evaluation. The published explanation supplies
  the worked reasoning and states each interchange boundary and the semantics
  discarded.
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
  - The primary lab works source-version replay by hand. The optional Python
    companion rebuilds a changed retained excerpt in a fresh temporary
    database. Durable release publication is a production extension.

## Route-keyed worked-case trace

The trace binds the case to its stable route and concept IDs. Every primary
stage is hand-worked in the primer. Companion verification is optional and
covers the bounded operations stated below.

| route_id | route tier | stage | concept_id(s) | Input and decision | Output handed to the next stage | Evidence mode and scope decision |
|---|---|---|---|---|---|---|
| route-python-duckdb | primary | Boundary and questions | kg-boundary | Declare Northbridge sources, authority, dates, and Q1–Q5 contracts | Bounded questions and refusal rules | Hand-worked, including the two-part Q2 and Q4 contracts |
| route-python-duckdb | primary | Mentions and qualified claims | kg-mentions, kg-claims | Preserve source spans, distinguish mentions from entities, and retain source, interval and polarity | Candidate claims and evidence-bearing rows | Hand-worked from excerpts. The optional companion verifies construction for declared patterns |
| route-python-duckdb | primary | Temporal and conservative construction | kg-temporal, kg-extraction | Classify bounded, unbounded and unknown horizons, refuse unsupported dates, and abstain on Alex identity | Source-derived `c1`, `c4`, `c5` plus refusal decisions | Hand-worked classifications and refusals. Companion extraction covers fixture patterns |
| route-python-duckdb | primary | Ledger and evidence queries | kg-duckdb, kg-queries | Bind identifiers, select rows, join path hops, and classify dates in the printed ledger | Evidence rows and supported, refuted, or abstention results | Hand-worked queries. The storage reference describes the optional DuckDB mapping and reopen check |
| route-python-duckdb | primary | Diagnosis and correction | kg-correction | Diagnose the first evidence loss, compare omitted-negative, repaired, and changed-source runs, and replay R2 derivations | Revised evidence links, source comparison, and policy result | Hand-worked failures and three-pass lab. The optional companion verifies a bounded rebuild |
| route-python-duckdb | primary | Privacy and release boundary | kg-privacy | Compare ordinary citations, answers, and counts across paired releases | Approved evidence and the same ordinary outputs in both states | Hand-worked disclosure test and governance assumptions |
| route-python-duckdb | primary | Evaluate permitted outputs and release regression | kg-evaluation, kg-correction, kg-privacy | Score the synthetic items against the audience contract, then compare original and revised answers, paths, and citations | Interpreted measures and release acceptance expectations | Worked arithmetic, answer items, and final regression table; no deployment accuracy claim |
| route-r-projection | alternative | Positive projection | kg-r-projection | Read the declared positive interchange fixture and analyse paths/components | Topology results without claim qualifiers | executable alternative; deliberately not synchronised with changed Python input |
| route-r-projection | alternative | Interpret topology and return to evidence | kg-r-projection | Explain unit path cost, components, and discarded dates, polarity, provenance and claim IDs | A topology interpretation and a return path to the evidence ledger | Hand-worked interpretation with optional R verification. Evidence questions require the ledger |
| route-graph-storage | reference-only | RDF, property graphs and storage choice | kg-rdf, kg-property, kg-storage | Compare qualified mappings and workload boundaries | A future storage decision and prospective test | reference-only; no continuous teaching spine or executed service migration promised |

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
