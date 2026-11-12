# Primer teaching-case contract: Northbridge evidence-backed knowledge graph

- Issue and milestone: #398; related #397
- Brief revision: `kg-398-brief-r9`
- Reader capability: Follow a bounded source set into an evidence-preserving
  claim ledger, answer a dated question, diagnose an incorrect or incomplete
  answer, replay a documented correction by hand, and explain the changed
  result and remaining uncertainty. The primary route is standalone
  illustrative prose; running software is optional.
- Case purpose: Northbridge makes the organising method concrete without
  pretending that a small synthetic fixture is a complete organisation. It
  exposes source authority, temporal conflict, identity ambiguity, privacy,
  and correction in one connected route.
- Case boundary: Synthetic policy register, directory and meeting excerpts;
  dates and source roles declared in the fixture; no real people or retained
  documents; no completeness claim beyond the supplied records; no legal or
  operational authority inferred from the example.

## Trace

The primary route (`route-python-duckdb`) is hand-worked and illustrative at
every stage. Optional companion checks supply bounded executable evidence.

| Stage | Reader-facing work and evidence | Mode and companion boundary |
|---|---|---|
| Source inputs or assumptions | Read the synthetic excerpts, locators, directory rows and refusal cases; declare source roles and temporal assumptions | Illustrative; companion uses `examples/source_records.json` and `examples/fixture.json` |
| Construction, extraction, or transformation decisions | Follow mentions, spans, qualified claims, temporal decisions and abstention on Alex Kim | Illustrative; optional `examples/python/construction.py` checks declared sentence patterns and spans, while curated rows remain curated |
| Intermediate records or representation | Follow the printed assertion ledger, source and mention links, temporal fields and polarity | Illustrative; optional Python checks build corresponding tables and evidence for the fixture |
| Stored or computed result | Inspect the worked ledger and selected rows | Illustrative; optional DuckDB check writes a temporary database, closes and reopens it read-only; persistence does not enforce the full ledger contract |
| Reader-facing query or operation | Follow direct, two-hop, provenance, temporal and conflict selections by hand | Illustrative; optional Python runs bounded queries against the fixture |
| Interpretation of the result | Explain supported, refuted or abstain outcomes, including conflict and indeterminate temporal scope | Illustrative; companion assertions check bounded cases, not general accuracy |
| Failure mode or scope limit | Diagnose omitted evidence, restore it, compare the changed-source R2 result, and replay affected derivations | Illustrative; optional companion checks a changed retained excerpt in a fresh temporary database, not durable release publication |
| Alternative projection (`route-r-projection`) | Construct the positive projection and interpret paths and components against the ledger | R construction and operations executable; interpretation illustrative. The self-contained projection discards dates, polarity, provenance and claim IDs and is not synchronised with the correction |
| Storage comparison (`route-graph-storage`) | Compare RDF, property-graph and storage mappings and their retained qualifiers | Reference-only; no service migration is executed |

## Teaching decisions

- Primary acceptance: The published explanation must let a reader trace the
  case from source excerpts through mention decisions, qualified ledger rows,
  selections, interpretation, diagnosis, correction and re-evaluation without
  executing a companion. It must expose source and extraction limits, refusal,
  privacy, and the reason for each material abstention. Compare the original
  and revised answers, classifications and evidence, including unchanged
  results with changed citations.
- Optional executable companion: From the repository root, run
  `just build-python-duckdb-runtime`, `just probe-python-duckdb-runtime`, and
  `just examples knowledge_graph knowledge-graph-python`. The example checks
  declared extraction patterns, evidence spans, validation, temporary
  DuckDB persistence and queries, abstention, extraction repair, and a bounded
  source correction and re-evaluation. The build needs network access or a
  populated cache; the probe and example run offline. The checks cover the
  synthetic fixture and declared patterns, not general extraction, production
  identity resolution, durable publication, or access-control enforcement.
- Alternative executable check: With the pinned R runtime available, run
  `just examples knowledge_graph knowledge-graph-r` from the repository root
  and inspect the expected path and component results. The independent
  positive fixture supports topology only; it does not track revised Python
  sources. Interpretation and information loss must also be explained in prose.
- Illustrative or reference-only material: Full-document ingestion, general
  NLP, production identity resolution, RDF/SPARQL/SHACL/PROV-O snippets,
  Cypher, graph-database serving, and real access-control enforcement. RDF and
  property-graph mappings must name which claim qualifiers they preserve or
  discard.
- Measured stages: None beyond deterministic example outputs; do not report
  performance measurements without a separate workload and reproducible
  benchmark.
- Expected abstentions or failures: Unresolved Alex Kim identity; no evidence
  outside the source boundary; conflict between positive and negative claims;
  indeterminate temporal horizon; unsupported extraction sentence; and any
  correction whose evidence is insufficient to update the answer.
- Evidence and freshness plan: Pin and record Python/DuckDB and R runtime
  versions from repository artifacts; verify current DuckDB, W3C, Cypher,
  igraph and tidygraph claims against official primary sources before release;
  mark all unexecuted snippets and prospective integrations explicitly. Record
  companion execution separately from the illustrative content assessment.
