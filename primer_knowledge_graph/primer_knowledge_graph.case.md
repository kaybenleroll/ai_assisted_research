# Primer teaching-case contract: Northbridge evidence-backed knowledge graph

- Issue and milestone: #398; related #397
- Reader capability: Follow a bounded source set into an evidence-preserving
  claim ledger, answer a dated question, diagnose an incorrect or incomplete
  answer, correct the source-derived input, rebuild the DuckDB representation,
  and explain the changed result and remaining uncertainty.
- Case purpose: Northbridge makes the organising method concrete without
  pretending that a small synthetic fixture is a complete organisation. It
  exposes source authority, temporal conflict, identity ambiguity, privacy,
  and correction in one connected route.
- Case boundary: Synthetic policy register, directory and meeting excerpts;
  dates and source roles declared in the fixture; no real people or retained
  documents; no completeness claim beyond the supplied records; no legal or
  operational authority inferred from the example.

## Trace

| Stage | Description | Evidence or artefact | Status |
|---|---|---|---|
| Source inputs or assumptions | Read the bounded synthetic excerpts, locators, directory rows and explicit refusal cases; declare source roles and temporal assumptions | `examples/source_records.json`, `examples/fixture.json`, opening boundary sections | executable and illustrative |
| Construction, extraction, or transformation decisions | Apply the declared sentence patterns; preserve spans and methods; resolve Alex Kim by abstention; retain curated rows as explicitly curated | `examples/python/construction.py`, `examples/python/knowledge_graph.py` | executable for the declared patterns; curated rows illustrative |
| Intermediate records or representation | Build entities, mentions, claims, temporal fields, polarity, source links and extraction evidence; project positive claims only for topology analysis | DuckDB `claims`, `sources`, `mentions`, `extraction_evidence` tables; R projection | executable in Python; R projection alternative |
| Stored or computed result | Write a file-backed DuckDB database, close it, reopen read-only, and inspect persisted rows | `examples/python/knowledge_graph.py` database assertions | executable |
| Reader-facing query or operation | Run direct, two-hop, provenance, temporal and evidence-conflict queries; separately run R path/component operations | Python SQL queries; `examples/r/knowledge_graph.R` | executable |
| Interpretation of the result | Return supported, refuted or abstain for no evidence, conflict and indeterminate temporal scope; interpret R output only as topology | `answer_rows`, dated cases, R output and explanation | executable and explanatory |
| Failure mode or scope limit | Show extraction refusal, unresolved identity, incomplete source boundary, lossy R projection, and a deliberate correction that changes a downstream answer | Negative/ambiguous fixtures; correction/rebuild assertions; limitations sections | correction path must be executable in #398; other limits illustrative |

## Teaching decisions

- Executable stages: Python source-pattern extraction, evidence-span checks,
  validation, DuckDB write/reopen, direct/two-hop/provenance/temporal queries,
  abstention cases, correction/rebuild/re-evaluation, and the R path/component
  and node-summary operations. Register stable example IDs in the manifest or
  code comments when implementation changes are made.
- Illustrative stages: full-document ingestion, general NLP, production
  identity resolution, RDF/SPARQL/SHACL/PROV-O snippets, Cypher, graph-database
  serving, and real access-control enforcement.
- Measured stages: none beyond the deterministic outputs of the examples;
  do not report performance measurements without a separate workload and
  reproducible benchmark.
- Required alternatives: Python/DuckDB is the primary evidence-preserving
  route; R must use the same declared positive projection or explicitly state
  why its small interchange fixture is equivalent for topology only; RDF and
  property-graph mappings must name which claim qualifiers they preserve or
  discard.
- Expected abstentions or failures: unresolved Alex Kim identity; no evidence
  outside the source boundary; conflict between positive and negative claims;
  indeterminate temporal horizon; unsupported extraction sentence; and any
  correction whose evidence is insufficient to update the answer.
- Evidence and freshness plan: Pin and record Python/DuckDB and R runtime
  versions from repository artifacts; verify current DuckDB, W3C, Cypher,
  igraph and tidygraph claims against official primary sources before release;
  mark all unexecuted snippets and prospective integrations explicitly.

The contract is complete only when the reader can follow the same Northbridge
case from source text to an interpreted result, see a diagnosis and correction
change the result, and identify where the method must abstain.
