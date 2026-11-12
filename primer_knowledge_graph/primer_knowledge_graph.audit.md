# Primer audit: Building Knowledge Graphs: From Sources to Verifiable Queries

- Issue and milestone: #398; related #397; shared accessibility follow-up #421
- Audit revision: `kg-398-depth-audit-r15`
- Source revision: `9ceb2d2`
- Tracked path: `primer_knowledge_graph/primer_knowledge_graph.audit.md`
- Starting branch: `docs/398-revise-knowledge-graph-primer`
- Reviewer(s): Codex, applying the native `primer-audit` skill
- Date: 2026-11-12
- Reviewed revision: `9ceb2d2`
- Brief reviewed: `primer_knowledge_graph/primer_knowledge_graph.brief.md`, `kg-398-brief-r12`, working tree pending its rebinding commit
- Review boundary: rebind the targeted schema/storage structural audit to the working tree and brief r12; retain the complete prior content evidence and release evidence, without new assistive-technology testing
- Teaching-case contract: `primer_knowledge_graph/primer_knowledge_graph.case.md`, reconciled at `2d47558`, unchanged since then
- Core-concept depth matrix: brief r12, all 14 stable IDs and all three route tiers retained below
- Readiness decision: not-ready

## Whole-document review

The complete 879-line source at `9ceb2d2` was reread against brief r12 and
the case contract. That was a fresh content judgement, not a rebinding of audit
r11. Source bytes at that revision had SHA-256:
`8544f38a837a79d6230e87b4c2eb6470c28c5449188449800d8ccea8f552f900`.
The targeted second audit below rechecks the only source change at `22aec31`
and brief r12. Unless explicitly marked historical, source locators below identify
`primer_knowledge_graph/primer_knowledge_graph.md` at `9ceb2d2`; line ranges
refer to Markdown, not published page numbers.

**Content gate: pass** within the agreed standalone illustrative primary
route, bounded alternative topology route, and reference scope. There is no
unresolved primary/alternative depth gap. The opening now reaches the problem
before the detailed vocabulary; the continuous Q4 chain preserves identity,
qualifiers, source comparison, interpretation, correction, disclosure, scoring,
and release dependencies. The schema bridge works an inference and a
validation counterexample with different premises and consequences, rather
than merely defining terms. The source-located teaching judgement remains
separate from the companion runs and published-output checks.

The whole-document findings record both the extent and limits of verification.

| Area | Scope and method | Exact evidence or location | Status | Finding or gap | Disposition |
|---|---|---|---|---|---|
| Brief coverage and scope | Complete source versus brief r12 and contract | Source 5–17, 23–91, 113–145, 865–871; contract Trace and Teaching decisions | verified | All three route tiers and 14 concept IDs remain covered. Contract metadata still names r9, its reconciliation baseline; its operative scope agrees with the current brief. | Retain contract history; this audit binds the current brief explicitly. |
| Technical claims, derivations, and calculations | Full inventory; selected independent hand checks and new standards check | 255–281, 318–342, 398–418, 494–514, 590–625, 676–725, 751–794, 828–836 | verified | Checked exclusive dates, conflict priority, R2 carry-forwards, retrieval denominators, transfer-case filters, degrees and components; the RDFS/SHACL contrast remains supported as recorded below. Not every claim independently reverified. | Retain; distinguish sample checks from whole-source inventory. |
| Source quality, attribution, and freshness | Citation inventory; new W3C checks; retain scoped historical source review | 19, 185, 796, 830–832, 842–879 | verified | New bridge checked on 12 November; earlier version/API and other cited-source checks retain their 11 November provenance. No claim to have reopened every citation today. | Retain historical review only for unchanged claims; no latest-version assertion. |
| Explanatory depth and prerequisites | Continuous reading and adversarial matrix | 5–17; source-to-answer chain 29–91; detailed route 93–544 | verified | Familiarity with tables and IDs suffices for the primary case. Printed inputs, choices, intermediate rows and limits carry the reasoning without software. | Retain; optional companions are not hidden prerequisites. |
| Structure, dependency order, and section fragmentation | All major sections and section boundaries | 3–21, 27–91, 93–147, 348–422, 546–745, 798–824, 824–879 | verified | Opening and Northbridge consolidation remove the glossary-first detour. Four walkthrough stages are meaningful decisions; detailed sections deepen them. The former standalone schema bridge is now a subsection of the storage reference, so the remaining top-level sections have a clear teaching or reference role. | Retain the consolidated structure; no stable route or concept ID changed. |
| Worked examples and interpretations | Hand trace of Northbridge, both transfers, R derivation and practice; companion inspection and runs | 119–247, 289–344, 398–418, 441–544, 558–743, 751–822 | verified | Q2 snapshot ownership is distinct from later continuity. Q4 comparison differs from applicability. The R companion consumes a precomputed view, not the ledger filtering described in prose. | Retain explicit illustrative/executed boundaries. |
| Applications, limitations, and failure modes | Whole source, especially dependent repairs | 143–145, 219–223, 363–420, 456, 520, 544, 635, 687, 717–725, 792–794 | verified | Omissions, scope, unknown dates, false joins, count leakage and changed citations have concrete consequences and discriminating checks. | Retain; production guarantees are excluded, not missing promised implementation. |
| Figures, tables, equations, and accessibility | Source inspection and publication render report | 45–61; SVG title/description and labels; tables 227–235, 445–450, 528–538; PDF pages 7 and 53 | not-checked | SVG alt text and figure/table visual samples pass; interactive and assistive-technology semantics remain untested. No formal derivation or code-page render is claimed. | Source teaching is adequate; human accessibility acceptance remains open. |
| HTML, PDF, metadata, and committed outputs | Publication render report and Git baseline | HTML/PDF regenerated from source `9ceb2d2`; details below | verified | Build and representative output checks passed for the structural revision; PDF is untagged. | Human accessibility checks remain a separate release blocker. |
| Residual uncertainty and follow-up questions | Review limits and first-use terminology | 828 expands `RDFS`; 830 links RDF Schema; output/source evidence below | verified | First use now names RDF Schema. No unreviewed primary/alternative teaching transition remains. | Retain output and accessibility limitations below. |

The case contract's r9 label is historical metadata, not evidence of an
unagreed route change. Its acceptance is standalone reasoning; execution is
optional. Brief r10 records the post-draft checkpoint after `e60c339` and
`3f3d384`. Its statements that the audit is stale describe the state before
this update and are superseded by this audit's current binding. Its output
warning is superseded by publication commit `240d09e`. No brief or contract edit was made.

For the central case, every reader-facing stage has the following provenance.

| Case stage | Source or section | Evidence and result | Execution status | Gap or limitation |
|---|---|---|---|---|
| Input or assumptions | 23–31, 113–145 | R1/M1/D1, snapshot dates, exclusive end, source roles and Q1–Q5 define admissible evidence. | illustrative | Synthetic, incomplete beyond the declared boundary. |
| Construction or extraction decision | 33–43, 170–223 | Shared topic/version links; Alex unresolved; negation retained; conditional and imprecise wording refused. | illustrative | Three source-derived rows, four curated rows; supplied topic is an assumption. |
| Intermediate representation | 45–61, 225–247 | Seven assertion rows, required source/locator, optional mention, and `c5` backtrace to M1. | illustrative | Admission does not prove extraction or corpus completeness. |
| Stored or computed result | 65–71, 255–281, 318–330 | Bind `c1`/`c5`, classify each date, compare polarities, apply conflict-first policy. | illustrative | Hand ledger is sufficient; optional database persistence is separate. |
| Reader-facing query or operation | 289–344 | Q1/Q2 direct lookup, Q3/Q5 evidence and identity, Q4 comparison, `c1`/`c3` typed join. | illustrative | Binding, source, audience and per-hop time must stay explicit. |
| Interpretation | 67–71, 300–342 | Disagreement plus withholding on 15 March; temporal withholding on 16 March; no Orion applicability. | illustrative | Neither source truth nor operational authority follows. |
| Failure mode or scope limit | 75–79, 363–420 | A omits denial, B restores it, C changes R1 to R2; same policy yields supported, conflict abstention, then refuted. | illustrative | C is hypothetical; durable release publication is not implemented. |
| Disclosure, evaluation and release | 83–91, 441–544 | Paired ordinary outputs, item definitions, precision/recall and G-B/G-C provenance regression complete the case. | illustrative | No executed access control, independent accuracy study or deployed release. |

## Brief and example traceability

The matrix below provides one exact four-part locator set for each concept.
The transition table checks that those local pieces form complete reader paths.
These are the retained scope reductions, rather than unresolved gaps:

- `route-python-duckdb` stays `primary`: the standalone hand route is the
  promise. Python/DuckDB is optional verification, not production ingestion,
  enforced disclosure, or durable publication. Brief Scope, Exclusions and
  Optional branches agree with source 11–17 and 867–871 and contract Teaching
  decisions. The reader can replay the reasoning without executing it.
- `route-r-projection` stays `alternative`: source 751–765 teaches the
  lossy derivation, while 796 and 869 disclose that the R companion starts
  from an independent precomputed fixture. A synchronised projection of
  corrected Python data is excluded in brief Open decisions and Optional
  branches. The reader must construct a scoped dated view before using R
  after a correction; topology alone cannot settle Q4 (792–794).
- `route-graph-storage` stays `reference-only`: brief Optional branches and
  source 834, 859–863 and 869 promise mappings and a prospective exchange
  test. A reasoner, SHACL processor, Neo4j integration, migration, ontology
  engineering course and benchmark are not promised. The new bridge extends
  `kg-claims`/`kg-rdf`, without adding IDs or upgrading the route tier.

## Reader-scale section depth

Every major section and every section carrying primary/alternative reasoning
was read in sequence at `3f3d384`. All dispositions are fresh judgements.

| Section and route/concept IDs | Teaching job | Reasoning spine or worked thread | Application or interpretation locator | Material limitation or failure-case locator | Disposition and rationale |
|---|---|---|---|---|---|
| Introduction, 3–19; primary `kg-boundary`, `kg-claims` | Orient a reader new to modelling | Conflicting records motivate reusable typed connections and evidence | 7–15 compare document/table/graph and state the route | 13, 17: traceability is not truth; exclusions | retain; brief orientation supplies only vocabulary needed for the first question. |
| Complete Northbridge Question, 21–91; primary `kg-boundary`, `kg-mentions`, `kg-claims`, `kg-temporal`, `kg-queries`, `kg-correction`, `kg-privacy`, `kg-evaluation` | Establish a complete organising case | Source → identity → qualified rows → selection → policy → repair → disclosure → evaluation/release | 65–91 interpreted answer and controlled changes; 47–49 graph supplements trace | 31, 35, 53, 69, 85, 87 | retain; four child stages separate real decisions, while retained inline anchors preserve access. Detailed replay follows. |
| Design the Graph, 93–145; primary `kg-boundary` | Choose typed paths and answer contracts | Reuse shared IDs, specify source roles, distinguish missing evidence and completeness | 101, 119–143: Q1–Q5 and Orion counterexample | 109, 127, 143–145 | retain; develops decisions the overview cannot settle for every question. |
| Evidence Ledger, 147–247; primary `kg-mentions`, `kg-claims`, `kg-extraction`, `kg-duckdb` | Construct reviewable records | Mention decisions, relation meaning, spans/refusals, ledger and provenance chain | 176–219, 227–247: reproduce `c5` and find its source | 185–187, 205, 219–225, 243 | retain; construction and evidence lookup form one sustained dependency. |
| Time and Conflict, 249–281; primary `kg-temporal` | Separate per-row support from policy | Bounded/unknown/unbounded, valid/recorded time, comparable scope, policy counterexample | 259–263, 279–281: dates and alternative rule | 257, 269, 273–277 | retain; each subsection explains a distinct source of wrong conclusions. |
| Answer Questions, 283–346; primary `kg-queries`, `kg-duckdb` | Reproduce selections and typed joins | Q1/Q2 → assertions and evidence → Q4 comparison → qualified path | 289–344: all Q1–Q5, each hop and answer record | 298–306, 330, 338–342 | retain; intermediate bindings prevent output tables becoming unexplained answers. |
| Diagnose and Correct, 348–420; primary `kg-correction` | Locate the first loss and distinguish two interventions | Ordered branches; three failures; A/B/C and R2 carry-forwards | 371–381, 398–418: discriminator, change and changed evidence | 365, 377, 402, 420 | retain; diagnostic examples develop the reference table; repair and source revision remain distinct. |
| Govern Disclosure and Release, 422–544; primary `kg-privacy`, `kg-evaluation`, `kg-correction` | Evaluate what an audience may receive and propagate correction | Fix audience → paired evidence views → manifests → defined items → release regression | 441–456, 488–514, 528–542 | 456, 478–480, 520, 544 | retain; ordering explains why audience policy precedes scoring, and regression tests evidence as well as values. |
| Literature transfer, 546–635; primary transfer of `kg-claims`, `kg-queries`, `kg-correction`, `kg-evaluation` | Preserve unit and version when querying research | Work/version/study/cohort → filtered result → C@2 replay → reverse evidence audit | 590–625, 629–633 | 548, 600, 621, 631–635 | retain; source/model/query/correction/audit landmarks carry an independent transfer thread. |
| Dependency transfer and comparison, 637–743; primary transfer of `kg-boundary`, `kg-queries`, `kg-correction` | Preserve build context and interpret empty results | Selected instances → scoped traversal → advisory bound → I41@2 → cross-case synthesis | 676–707, 715–725, 733–741 | 643, 687, 717–725, 743 | retain; comparison explains what carries across domains and what must be redefined. |
| Positive Projection, 745–796; alternative `kg-r-projection` | Deliberately lose semantics to analyse topology | Deduplicate positives, preserve vertices, expand neighbours, count components/degrees, return to dated evidence | 751–788, 792–796 | 763, 771, 792–794 | retain; full worked derivation and information-loss interpretation justify the alternative route. |
| Practice, 798–822; primary/alternative concepts | Apply earlier decisions | Eight tasks require intermediate bindings and compare worked reasoning | 804–822 | 800, 816–822 | retain; bounded practice deliberately reuses the synthetic assumptions. |
| Storage and Implementation Reference, 824–879; `kg-claims`, reference `kg-rdf`, `kg-property`, `kg-storage`; optional primary `kg-duckdb` | Bridge local meaning to formal consequences, then compare representations against the case's acceptance criteria | Schema/validation/inference subsection: vocabulary → schema → explicitly asserted affiliation → inferred classes → missing-source validation; RDF and property-graph mappings then preserve opposing assertions, optional fields/provenance, qualified relationships and workload/exchange tests | 828–873 | 830, 832–834: qualified record is not direct assertion and conformance is not evidence truth; 851, 853, 861, 863–871 | retain as one reference section with a meaningful schema bridge subsection; no padding or catalogue split. First-use RDF Schema remains expanded at 828. |
| Further Reading, 873–879; reference | Signpost deeper evidence | Annotated primary standards, linkage and disclosure sources | 875–879 | An annotation is not independent source verification | retain; intentionally brief reference list follows, rather than substitutes for, explanation. |

## Route transition evidence

All rows trace reader-facing prose at `3f3d384`. `Illustrative` is deliberate:
manual review and a passing companion do not turn these passages into executed
operations. Result-to-next-input links are stated explicitly. Companion runs
are recorded separately under execution evidence. No required transition is
`proposed` or `not-checked`.

| route_id | concept_id(s) | transition (from to) | linked input and reader operation | intermediate reasoning or decision | result | interpretation | material limitation | execution status | gap and reader consequence |
|---|---|---|---|---|---|---|---|---|---|
| route-python-duckdb | kg-boundary | source boundary to question contract | 29–31, 119–139: admit R1/M1/D1 and fix Q4 endpoints, day and sources | 113–127, 141: separate designated source role from comparison policy | Q4 contract selects the two-source proposition; passed to mention matching | 141–145: one-source applicability differs from two-source agreement | 31, 127, 143: no completeness or operational authorisation | illustrative | No gap; reader can justify admissible evidence before construction. |
| route-python-duckdb | kg-mentions | question and excerpts to shared identities | 33–35, 170–183: match version/project occurrences under M1 topic, inspect directory IDs | 170–185: issuer/context support links; Alex has no discriminator | Policy/Atlas IDs link the Q4 participants; unresolved `m-alex` feeds authorised Q5 | 185–187: identifier consistency does not prove identity; abstention preserves reviewability | 35, 172, 185: absent topic or missed candidate can defeat a link | illustrative | No gap; no forced Alex merge is required by the next assertion step. |
| route-python-duckdb | kg-claims, kg-extraction | identities and spans to qualified assertions | 37–45, 197–217: read R1 affirmation and M1 denial using accepted endpoint IDs | 205, 209–223: check meaning, negation, dates and conditions; refuse unsupported candidates | Separate `c1`/`c5`, plus `c4`, enter seven-row ledger 225–235 | 237: same proposition permits comparison without fusing source assertions | 53, 193, 219–225: completeness, independence and four curated rows | illustrative | No gap; reader can explain what was extracted, curated or refused. |
| route-python-duckdb | kg-duckdb, kg-claims | admitted rows to evidence-preserving ledger lookup | 227–247: select `c5`, follow source and locator to M1 sentence 2 and its mention | 241–247, 312: source is required; mention is optional, so `c7` survives lookup | Rows with inspectable evidence feed classification and queries | 245–247: origin, authority and evidence integrity differ; persistence is optional (867) | 243, 867–869: offsets can drift; database schema does not enforce the whole contract | illustrative | No gap within hand route; companion persistence is verified separately, not a prerequisite. |
| route-python-duckdb | kg-temporal | qualified ledger to dated evidence | 255–261: classify each row at requested day; retain polarity | 259, 273–281: same proposition/scope first, conflict before indeterminacy | `c1`/`c5` applicable on 15 March; `c5` indeterminate on 16 March (318–328) | 259, 330: applicable evidence may deny applicability; changed abstention has a changed reason | 257, 263, 269: unknown is not continuation or knowledge history | illustrative | No gap; temporal state is handed explicitly to policy, not erased by aggregation. |
| route-python-duckdb | kg-queries, kg-temporal, kg-duckdb | selection and dates to Q1/Q2/Q3/Q5 answers | 289–314: bind roles/sources; Q1 retains register rows; Q2 binds owner object; Q3 keeps both polarities; Q5 inspects `r2` | 293–304, 310–314: classify dates, preserve identity and evidence joins | Q1 date table; Morgan at snapshot with later continuity unknown; both minutes rows; unresolved Alex | 300–306, 310–314: name, time support, assertion set and review decision have different answer shapes | 298, 304–306, 312–314: no inferred continuity, cardinality or attendance edge | illustrative | No gap; the owner result does not smuggle a later valid date into evaluation. |
| route-python-duckdb | kg-queries, kg-temporal | classified Q4 rows to comparison and applicability answer | 65–71, 318–328: bind version 1/Atlas, select both sources, classify `c1`/`c5` | 67, 279, 318: opposing applicable polarities trigger disagreement then withholding | 69, 332: two-sentence citations and justified abstention; 330 explains next-day change | Comparison and applicability are separate determinations, including where one source alone is applicable | 69–71, 330–332: no true governing-policy conclusion; a different rule needs authority | illustrative | No gap; these answer records become the correction baseline at 344–346. |
| route-python-duckdb | kg-queries, kg-temporal, kg-correction | ledger joins to bounded path and impact dependency | 336: match `c1` object to `c3` subject on Atlas; reject `c7` | 338–340: keep types, source, polarity and each hop's time support | 340: path supported on 1 January, indeterminate on 1 March, outside on 1 April; dependency recorded at 346 | 338–342: node path differs from evidence-pair count and applicability propagation | 342: shared organisation does not extend version 1 to Orion | illustrative | No gap; correction can revisit the dated path as well as Q4. |
| route-python-duckdb | kg-correction | bad answer and retained span to repaired construction | 75–77, 363–381: inspect first divergence in source/candidate/admission/selection/policy/presentation | 371–377, 400–402: hold sources/date/policy fixed and restore only `c5`; boundary-test classifier separately | A supported becomes B disagreement/abstention with both rows and citations | 359, 373, 402: repair restores evidence rather than settles the dispute | 365, 377, 381: validation alone, indefinite extension or re-extraction cannot cure every later-stage defect | illustrative | No gap; repaired G-B supplies the controlled baseline for source revision. |
| route-python-duckdb | kg-correction, kg-temporal, kg-queries | repaired baseline to R2 derivations and changed answers | 398–412: replace register sentence 1, retain sentences 2/3 and snapshot context, rebuild register derivations | 404–418: preserve R1; reverify unchanged spans and classify all dependent hops | 410–418: `c1` exclusive end 1 March; `c2`/`c6` values retained with R2 provenance; Q4 refuted; 1 March path outside | 414–416: no applicable disagreement is not agreement; unchanged values still need revised evidence | 79, 420: hypothetical correction; do not overwrite old history or claim authority | illustrative | No gap; revised derivations feed release impact set at 464–468. |
| route-python-duckdb | kg-privacy | answer records and restricted identity to permitted evidence views | 83–85, 428–450: fix paired releases, approved sentences and ordinary/authorised purpose | 441–456: filter before traversal/count/citation; compare identical ordinary inputs | 447–452: same Q4, sentence lookup, fixed Q5 and zero visible links; authorised views differ | 439, 452–456: two candidate paths are not two attendees; masking labels leaks counts | 456, 478: combinations, caches and provenance still require a threat model | illustrative | No gap; audience-authorised outputs, not internal answers, become evaluation inputs. |
| route-python-duckdb | kg-evaluation, kg-privacy | permitted outputs to defined items and interpreted measures | 484–498: define assertion/answer units and audience; Pass A returns only `c1` | 488–502: distinguish retrieval from full answer and score C against its own R2 reference | 496–514: A precision 1/1, recall 1/2; B 2/2 each; coverage 2/5, policy agreement 5/5 | 498, 514: relevant returns can omit decisive evidence; definitions explain different success measures | 518–520: zero denominators, deduplication and tiny synthetic items; no empirical accuracy | illustrative | No gap; evaluation definitions specify the release regression expectations. |
| route-python-duckdb | kg-correction, kg-evaluation, kg-privacy | evaluated G-B/G-C to release acceptance record | 464–480, 524–538: compute impact from three register derivations and compare answer records | 530–542: compare boundary dates, same-value citations, changed abstention causes, dated path and paired disclosure | 530–538: Q1 gap at 1 March, Q2/c6 new evidence, Q4 refutation, changed path, unchanged undated edge | 540–542: values alone cannot establish a correct release | 480, 544, 869: named approval and live enforcement/publication need separate implementation | illustrative | No gap within agreed teaching route; no deployed release is claimed. |
| route-r-projection | kg-r-projection | ledger and entity set to positive edge view | 747–761: select six positive rows, group ordered triples, retain all eight entity IDs | 751–765: `c4`/`c6` collapse; declared vertices preserve two isolates | Five edges/eight vertices become topology input; companion independently reads fixture (796, 869) | 763–765: edge count differs from assertion count and selection does not describe activity | 751, 763, 869: polarity/time/provenance/claim IDs lost; no Python correction synchronisation | illustrative | No gap; executed R construction does not execute this ledger-to-view derivation. |
| route-r-projection | kg-r-projection | edge view to paths, components and node measures | 769–788: expand outgoing neighbours, ignore direction for weak connectivity, count in/out edges | 769–773: unit costs, no reverse route, six connected nodes and two isolates | Two-hop path, three weak components, eight strong singletons; directional degree sums five, Atlas total three | 771, 788: measures describe chosen costs and edges, not confidence or influence | 771, 788: weighted search or parallel edges can change measures | illustrative | No gap; prose supplies derivation and interpretation independently of passing R assertions. |
| route-r-projection | kg-r-projection | topology result to dated evidence interpretation | 792–794: compare same positive triple under R1/R2, then select/date-filter a new view | Unchanged undated edge versus revised `c1` outside; cross-source policy precedes decision-view projection | Original dated register edge present; corrected absent; return to Q4 ledger for cause | 792–794: unchanged topology is expected, absence can encode several causes | 794, 869: a dated label alone does not qualify each hop; companion is not synchronised | illustrative | No gap under retained alternative scope; dated analysis needs a newly constructed scoped input. |

The bridge at 828–836 is a bounded explained comparison, not another promised
service route. Its premises, classification result, validation counterexample,
and limits are covered by `kg-claims` and `kg-rdf` below. The reference route
has no mandatory continuous transition trace; source 863's exchange test is
prospective and has not been executed.

## Adversarial depth gate

All 14 rows retain the teaching judgements at `3f3d384`, rebound to `22aec31`
after the targeted second audit, with the brief's
unchanged IDs and tiers. `Verified` means sufficient explanation, action,
interpretation and limitation for the agreed scope. It does not mean every
operation is executed or every external claim has been rechecked today.

| route_id | route tier | concept_id | explanation locator | example/action locator | interpretation locator | limitation locator | evidence revision | reviewer | status | finding | scope decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| route-python-duckdb | primary | kg-boundary | `primer_knowledge_graph/primer_knowledge_graph.md:113` | `primer_knowledge_graph/primer_knowledge_graph.md:133` | `primer_knowledge_graph/primer_knowledge_graph.md:141` | `primer_knowledge_graph/primer_knowledge_graph.md:143` | 22aec31 | Codex | verified | Source roles and Q1–Q5 make evidence selection and refusal reproducible. | Retain synthetic bounded primary promise; no world-completeness claim. |
| route-python-duckdb | primary | kg-mentions | `primer_knowledge_graph/primer_knowledge_graph.md:153` | `primer_knowledge_graph/primer_knowledge_graph.md:176` | `primer_knowledge_graph/primer_knowledge_graph.md:185` | `primer_knowledge_graph/primer_knowledge_graph.md:187` | 22aec31 | Codex | verified | Context/issuer support links; Alex abstention preserves the unresolved occurrence and repair evidence. | Retain; production resolution calibration is excluded in brief and source 17. |
| route-python-duckdb | primary | kg-claims | `primer_knowledge_graph/primer_knowledge_graph.md:191` | `primer_knowledge_graph/primer_knowledge_graph.md:227` | `primer_knowledge_graph/primer_knowledge_graph.md:237` | `primer_knowledge_graph/primer_knowledge_graph.md:205` | 22aec31 | Codex | verified | Qualified source assertions preserve polarity, time, roles and comparison grain; 47–49 and 826–832 explain visual/formal distinctions. | Retain; curated rows and assumed context remain explicit (172, 225). |
| route-python-duckdb | primary | kg-temporal | `primer_knowledge_graph/primer_knowledge_graph.md:255` | `primer_knowledge_graph/primer_knowledge_graph.md:261` | `primer_knowledge_graph/primer_knowledge_graph.md:330` | `primer_knowledge_graph/primer_knowledge_graph.md:257` | 22aec31 | Codex | verified | Classification, polarity, comparison and conflict-first policy remain distinct; 281 works a policy alternative. | Retain case day/exclusive-end convention; no invented continuity. |
| route-python-duckdb | primary | kg-extraction | `primer_knowledge_graph/primer_knowledge_graph.md:209` | `primer_knowledge_graph/primer_knowledge_graph.md:213` | `primer_knowledge_graph/primer_knowledge_graph.md:223` | `primer_knowledge_graph/primer_knowledge_graph.md:219` | 22aec31 | Codex | verified | Worked spans lead to accepted rows; refusals distinguish uncertainty from malformed records. | Retain declared patterns and four curated rows; general NLP excluded. |
| route-python-duckdb | primary | kg-duckdb | `primer_knowledge_graph/primer_knowledge_graph.md:241` | `primer_knowledge_graph/primer_knowledge_graph.md:312` | `primer_knowledge_graph/primer_knowledge_graph.md:867` | `primer_knowledge_graph/primer_knowledge_graph.md:869` | 22aec31 | Codex | verified | Required source and optional mention support hand replay including c7; optional reopen/query companion passed separately. | Retain narrowed standalone ledger promise agreed in brief r10 and contract; persistence is optional and does not enforce full semantics. |
| route-python-duckdb | primary | kg-queries | `primer_knowledge_graph/primer_knowledge_graph.md:285` | `primer_knowledge_graph/primer_knowledge_graph.md:318` | `primer_knowledge_graph/primer_knowledge_graph.md:332` | `primer_knowledge_graph/primer_knowledge_graph.md:342` | 22aec31 | Codex | verified | Q1–Q5 selections and typed c1/c3 join preserve classifications, evidence and scope. | Retain illustrative operation; later ownership and Orion applicability are not inferred. |
| route-python-duckdb | primary | kg-correction | `primer_knowledge_graph/primer_knowledge_graph.md:350` | `primer_knowledge_graph/primer_knowledge_graph.md:398` | `primer_knowledge_graph/primer_knowledge_graph.md:414` | `primer_knowledge_graph/primer_knowledge_graph.md:420` | 22aec31 | Codex | verified | First-loss diagnosis, A/B/C, R2 carry-forwards and 528–542 regression teach changed results and changed evidence. | Retain hand replay plus bounded optional rebuild; durable publication excluded (869). |
| route-python-duckdb | primary | kg-evaluation | `primer_knowledge_graph/primer_knowledge_graph.md:484` | `primer_knowledge_graph/primer_knowledge_graph.md:494` | `primer_knowledge_graph/primer_knowledge_graph.md:498` | `primer_knowledge_graph/primer_knowledge_graph.md:520` | 22aec31 | Codex | verified | Fixed evidence/answer units explain arithmetic, missing-denial consequences and 2/5 versus 5/5 denominators. | Retain illustrative tiny gold set; no independent accuracy study promised. |
| route-python-duckdb | primary | kg-privacy | `primer_knowledge_graph/primer_knowledge_graph.md:428` | `primer_knowledge_graph/primer_knowledge_graph.md:441` | `primer_knowledge_graph/primer_knowledge_graph.md:452` | `primer_knowledge_graph/primer_knowledge_graph.md:456` | 22aec31 | Codex | verified | Paired releases resolve approved citations and derive identical ordinary responses and visible counts. | Retain synthetic view reasoning; live enforcement/threat-model validation excluded (544, 869). |
| route-r-projection | alternative | kg-r-projection | `primer_knowledge_graph/primer_knowledge_graph.md:747` | `primer_knowledge_graph/primer_knowledge_graph.md:751` | `primer_knowledge_graph/primer_knowledge_graph.md:788` | `primer_knowledge_graph/primer_knowledge_graph.md:794` | 22aec31 | Codex | verified | Deduplication, neighbour expansion, weak/strong components and degree are derived, then returned to evidence. | Retain lossy independent fixture and no correction synchronisation (869); alternative tier unchanged. |
| route-graph-storage | reference-only | kg-rdf | `primer_knowledge_graph/primer_knowledge_graph.md:842` | `primer_knowledge_graph/primer_knowledge_graph.md:846` | `primer_knowledge_graph/primer_knowledge_graph.md:851` | `primer_knowledge_graph/primer_knowledge_graph.md:853` | working tree | Codex | verified | Qualified resources retain evidence; 830–836 distinguish classification, validation and source assertion. | Retain bounded worked mapping and bridge; no executed reasoner/SHACL/SPARQL integration. |
| route-graph-storage | reference-only | kg-property | `primer_knowledge_graph/primer_knowledge_graph.md:859` | `primer_knowledge_graph/primer_knowledge_graph.md:859` | `primer_knowledge_graph/primer_knowledge_graph.md:859` | `primer_knowledge_graph/primer_knowledge_graph.md:863` | working tree | Codex | verified | Parallel qualified relationships versus assertion nodes are tested conceptually against independent c1/c5 correction. | Retain short reference comparison, not a taught service route or executed Cypher. |
| route-graph-storage | reference-only | kg-storage | `primer_knowledge_graph/primer_knowledge_graph.md:861` | `primer_knowledge_graph/primer_knowledge_graph.md:863` | `primer_knowledge_graph/primer_knowledge_graph.md:871` | `primer_knowledge_graph/primer_knowledge_graph.md:869` | working tree | Codex | verified | Workload choice and prospective exchange test use the worked evidence and answer records as acceptance criteria. | Retain reference-only serving guidance; no benchmark, migration or Neo4j service promise. |

The published source has no fenced executable snippets. Its worked passages
map to companions or remain illustrative as follows.

| Published snippet or calculation | Test/manifest ID or illustrative status | Fixture and expected result checked | Gap |
|---|---|---|---|
| Source spans, ledger, dates, Q4 and repair (209–281, 318–332, 398–418); optional persistence (867–869) | `knowledge-graph-python`, executed companion; prose illustrative | `examples/source_records.json`, `examples/fixture.json`, `construction.py`, `knowledge_graph.py`: runtime assertions pass for declared extraction, validation, reopen, temporal queries, provenance and bounded A/B/C rebuild. | Does not execute complete Q2, approved evidence views, full R2 carry-forward/release acceptance, or general extraction. |
| Q2, disclosure, scoring, regression, both transfers and practice | illustrative | Hand-checked Q2 horizon, paired outputs, 1/1 and 1/2 versus 2/2, 2/5 versus 5/5, C@2 filtering, I41@2 upper bound and selected worked answers. | No empirical evaluation or deployed disclosure/release test; not a missing implementation promise. |
| Positive projection derivation (751–765) | illustrative | Seven rows → six positive assertions → five triples; all eight vertices; c4/c6 collapse. | R reads precomputed relations rather than executing this transformation. |
| Topology operations (769–796) | `knowledge-graph-r`, executed companion; prose derivation illustrative | Fixture has eight vertices/five edges; R asserts path version 1 → Atlas → Northbridge and three weak components. Prose degree sums/strong components checked by hand. | Degree assertion in R is only non-negativity; not every printed table value has an exact runtime assertion. No synchronised correction input. |
| Schema, RDF/SPARQL/SHACL/PROV-O, property graphs and exchange test (826–863) | illustrative; exchange test prospective | Standards comparison checked as below; assertion-resource mappings read by hand. | No formal syntax payload, reasoner, validator, query service or migration was run. |

## Representative sampling

These risk-selected checks supplement the complete source reading. Rendered
page samples are recorded separately in the publication report.

| Sample/page/object | Risk represented | Evidence and result | Status | Follow-up |
|---|---|---|---|---|
| Opening 5–19 and walkthrough 23–91 | Glossary-first compression or lost transition | Vocabulary is motivated inline; graph/table comparison, exclusions and software-free route precede detailed construction. Consolidation retains source, policy and audience distinctions. | verified | None blocking. |
| Bridge 826–834 | Confusing inference with rejection or evidence truth | Explicitly asserted c3 affiliation plus domain/range yields types; missing c1 source fails assumed cardinality. New W3C checks below support the contrast. | verified | First-use expansion verified at 828; no remaining editorial finding. |
| Q4 dates/correction 318–342, 398–418, 528–540 | Same answer hiding changed premises | Checked 15/16 March, R2 exclusive end, owner/c6 carry-forwards and c1/c3 path. Source comparison and applicability remain distinct. | verified | Companion coverage is narrower than full printed regression. |
| Literature/dependency cases 590–635, 676–725 | False independence or cross-build joins | Two studies/one cohort becomes one qualifying study after C@2; affected production path disappears on corrected 1.9.0 boundary for stated synthetic inputs. | verified | No clinical or real package/advisory validation claimed. |
| Projection 751–794 | Fixture success masking information loss | Checked triples, isolates, neighbour expansion, three weak components, eight strong singletons, in/out sums five and Atlas degree three. | verified | Current R pass does not make dated evidence available. |
| SVG at 47 and evidence tables | Accessibility and visual quality | SVG XML parses; title/desc and labels agree with c1/c5 and source alt/prose. Render report records figure page 7 and table page 53 as visually passed. | not-checked | Complete human accessibility semantics checks. |

## Revision-triggered second audit

This table identifies evidence changes rather than applying one uniform line
offset to r11. The r12-to-r13 row records the targeted second audit.

| Previous and current revisions | Changed artefacts and exact passages | Affected route/concept rows, transitions, claims, examples and outputs | Review scope, reviewer, method and result | Remaining gaps and readiness consequence |
|---|---|---|---|---|
| Audit r11 at `c7b5a91`, source `1ee9f80` → source `e60c339`/`3f3d384` | Opening old 3–75 → current 3–19; Northbridge old 77–141 → current 21–91; inline anchors retain former vocabulary/stage access | Primary boundary, mentions, claims, time, queries, correction, privacy/evaluation; all early transitions | Codex reread complete source, compared diff and retraced inputs through release. Definitions now occur at their use; no lost case decision found. | Old render pages and heading locations cannot validate current layout. |
| `1ee9f80` → `3f3d384` | Primary anchor 143→93, ledger 197→147, time 299→249, query 333→283, correction 398→348, governance 472→422, transfer 596→546, R 795→745 | Every primary/alternative concept/transition locator; adjacent detailed evidence and transfer threads | Codex reread each passage and dependent boundary. New current tables use exact locators for mechanism/action/interpretation/limit. | Locator validity is mechanical support, not the depth judgement. |
| `e60c339` → `3f3d384` | New source 47–49 and `figures/northbridge-evidence-graph.svg` | Primary kg-claims/kg-queries and figure/accessibility evidence | Codex inspected text, XML labels, title/description and correspondence to ledger and policy. | At that review, rendered figure, PDF flow and accessibility meaning were not checked; current render evidence is below. |
| `e60c339` → `3f3d384` | New schema bridge 824–834; storage anchor old 874→current 836 | kg-claims/kg-rdf; relation types, directly asserted graph versus qualified record, validation and inference | Codex traced c3 premises and c1 counterexample; verified new RDFS/SHACL claims against W3C on 12 November. | No formal engine run promised; first-use expansion subsequently resolved at `22aec31`. |
| Brief r8 → r9/r10 at `bddf2cf`/`f014f1b`; contract reconciliation at `2d47558` | Brief source binding, route-keyed trace, scope, post-draft checkpoint; contract Trace and Teaching decisions | All three route tiers/14 IDs, optional execution versus standalone route | Codex compared live committed artefacts, not checkpoint conclusions alone. Contract's r9 baseline agrees with r10 scope. | r10's historical stale-audit and published-output warnings are superseded by later evidence. |
| Audit r12 at `c56a182`, source `3f3d384` → `22aec31`; brief r10 at `f014f1b` → r11 at `dee0ecb` | Source 828 expands RDF Schema (RDFS) at first use; brief updates the source binding and checkpoint wording. No other source line changed. | Schema bridge 826–834; `route-python-duckdb`/`kg-claims` and `route-graph-storage`/`kg-rdf`; inference and validation examples, retained outputs | Codex compared both Git diffs and reread 826–834: 828 names the acronym, 830 retains its explicit assertion and inferred classes, and 832 retains the validation contrast and limits. The change is editorial-only and does not alter route transitions, concept evidence, tiers, or locators. | Acronym finding resolved. At r13, examples and standards checks had not been rerun and output checks remained outstanding. |
| Outputs at `c7b5a91` → `240d09e` | HTML/PDF regenerated for source `22aec31` | Current publication and accessibility evidence | Publication build and render report record successful checks and visual inspection. | Human accessibility checks remain outstanding; PDF is untagged. |

Retained evidence is not relabelled as a current run.

| Evidence and affected rows | Retained or newly reviewed/executed | Revision, method, result and reason for retention | Limits or outstanding checks |
|---|---|---|---|
| Whole source, section dispositions, all concepts and required transitions | retained from audit r12 | `3f3d384`, Codex complete reading, source diff and manual tracing; content pass | Selected hand checks do not independently verify every external or numerical claim. |
| Python and R companions | retained from audit r12 | Source `3f3d384`, brief `f014f1b`; `just examples knowledge_graph`, both manifest IDs pass in existing pinned containers | Synthetic fixtures only; provenance and precise boundary below. |
| RDFS/SHACL bridge | retained from audit r12, with targeted passage rechecked | `3f3d384`, W3C normative passages opened on 12 November; explained consequences supported | No reasoner/validator execution. |
| Other cited standards, version/API baselines and linkage/disclosure sources | retained historical source review | r11 recorded checks on 11 November for `1ee9f80`; unchanged reference/projection text verified by source diff and rereading | Not reopened citation by citation in this audit; no current transitive dependency attestation. |
| Historical builds, examples and visual samples | retained historical reports only | r11 at `c7b5a91` reports `just all`, examples, render QA and pages 3/9/12/57 for source `1ee9f80`; earlier `0152148` page 45/46 checks and `a02e3d9` checks stay in Git history | Superseded for current content/output acceptance; no copied current pass. |
| Accessibility findings | historical findings with r12 metadata confirmation | Prior review and #421 report untagged PDF and shared HTML limitations; r12 `pdfinfo` confirmed baseline PDF `Tagged: no` | Keyboard, no-JavaScript, browser accessibility tree, screen reader and tag/reading-order semantics not checked now. |

## Reconcile earlier evidence

Earlier findings are dispositioned against the current promise and artefacts.

| Earlier finding or audit | Location and revision reported | Current status: confirmed, resolved, stale, or unverified | Evidence |
|---|---|---|---|
| Audit and brief binding mismatch | r11 source `1ee9f80`/brief r8 versus r10 source `3f3d384`; r10 checkpoint reported two schema mismatches | resolved | Current metadata and all 14 evidence rows bind `22aec31`; structural/Git-backed checks below. |
| Opening overhead and fragmented early case | `1ee9f80` opening 3–75 and walkthrough 77–141 | resolved | Fresh reader-scale review of 3–91 and detailed dependent route; compact orientation and continuous case retain substantive distinctions. |
| New graph and schema bridge verification | Brief r10 checkpoint at `f014f1b` | resolved for source meaning and rendered presentation | Source 47–49 and 826–834 read; XML parsed and new W3C claims checked; current output and figure inspection recorded below. |
| Q2 source/date explanation or empirical score ambiguity | Earlier audits through r11 | confirmed as taught and illustrative | Current 302–304 and 509 distinguish snapshot identity from continuity; 494–520 explicitly define synthetic arithmetic and limits. No old teaching gap carried forward. |
| Optional persistence, standalone scope and unsynchronised R | Contract `2d47558`; brief r9/r10 | confirmed scope reductions | Source 867–871 and alternative return-to-evidence at 792–794 agree with contract. Not missing promised production implementation. |
| Ordered diagnostic semantics and literature records | r11 source 402–407 and 644–646 | confirmed in source, output evidence historical | Current 352–357 is an ordered branch sequence; 594–596 preserves three labelled candidate/evidence paths. Prior visual acceptance is not a current render check. |
| Shared accessibility defects | Historical review at `6cf3203`, retained in r11/`c7b5a91`, follow-up #421 | human accessibility evidence remains unresolved | Current deterministic HTML checks pass for control names, skip link and title heading; browser and assistive-technology checks remain outstanding. PDF remains untagged. |
| Builds, output freshness and local visual passes | r11 and older audits | superseded for `22aec31` | Publication report records current build, freshness and visual samples for outputs committed at `240d09e`. |

### Retained primary-source review at 1ee9f80

On 11 November 2026, r11 recorded a scoped primary-source review with no
material unsupported claim found in that scope. The exact sources below are
retained as historical evidence, not reopened checks today. Original line
numbers are explicitly historical; their unchanged current counterparts were
reread. Fictional examples are not validated as real-world facts by these
citations.

- RDF terms, literals, datasets and qualified resources: old 880–889,
  current 842–851; [RDF 1.1 graph](https://www.w3.org/TR/rdf11-concepts/#section-rdf-graph),
  [literals](https://www.w3.org/TR/rdf11-concepts/#section-Graph-Literal),
  [datasets](https://www.w3.org/TR/rdf11-concepts/#section-dataset), and
  [n-ary relations](https://www.w3.org/TR/swbp-n-aryRelations/).
- Pattern matching, constraints and provenance: old 891–893, current 853–855;
  [SPARQL 1.1](https://www.w3.org/TR/sparql11-query/),
  [SHACL](https://www.w3.org/TR/shacl/) and [PROV-O](https://www.w3.org/TR/prov-o/).
  The mapping was not executed.
- Property graph and fixed joins: old 897–905, current 859–867;
  [Neo4j graph concepts](https://neo4j.com/docs/getting-started/appendix/graphdb-concepts/),
  [Neo4j 5 MATCH](https://neo4j.com/docs/cypher-manual/5/clauses/match/),
  [DuckDB 1.4 joins](https://duckdb.org/docs/1.4/sql/query_syntax/from#joins), and
  [Python DB API](https://duckdb.org/docs/1.4/clients/python/dbapi).
  No Neo4j service route was run.
- R projection: old 801–846, current 751–796;
  [igraph 2.3.0 constructor](https://raw.githubusercontent.com/igraph/rigraph/v2.3.0/man/graph_from_data_frame.Rd),
  [paths](https://raw.githubusercontent.com/igraph/rigraph/v2.3.0/man/distances.Rd),
  [components](https://raw.githubusercontent.com/igraph/rigraph/v2.3.0/man/components.Rd), and
  [tidygraph 1.3.1 activation](https://raw.githubusercontent.com/thomasp85/tidygraph/v1.3.1/man/activate.Rd).
- Declared baselines: [Python 3.12.15](https://www.python.org/downloads/release/python-31215/),
  [DuckDB 1.4.3](https://pypi.org/pypi/duckdb/1.4.3/json),
  [R 4.5.3 release notes](https://stat.ethz.ch/R-manual/R-patched/doc/html/NEWS.html),
  [igraph 2.3.0](https://raw.githubusercontent.com/igraph/rigraph/v2.3.0/DESCRIPTION),
  [tidygraph 1.3.1](https://raw.githubusercontent.com/thomasp85/tidygraph/v1.3.1/DESCRIPTION), and
  [dplyr 1.2.1](https://raw.githubusercontent.com/tidyverse/dplyr/v1.2.1/DESCRIPTION).
  Transitive dependencies were not independently attested.
- Other cited sources: old 235 and 913–917, current 185 and 875–879;
  [record-linkage blocking](https://www150.statcan.gc.ca/n1/pub/12-001-x/2021002/article/00002-eng.htm),
  [PROV-DM](https://www.w3.org/TR/prov-dm/),
  [SPARQL optional patterns](https://www.w3.org/TR/sparql11-query/#optional), and
  [NIST SP 800-188](https://csrc.nist.gov/pubs/sp/800/188/final).

### New bridge source checks on 12 November 2026

Source 828–830: W3C [RDF Schema 1.1, domain](https://www.w3.org/TR/rdf-schema/#ch_domain)
and [range](https://www.w3.org/TR/rdf-schema/#ch_range) support the illustrated
subject/object classifications under the assumed relation and schema. The
qualified ledger record is kept distinct from that directly asserted relation.
These are formal consequences of premises, not source corroboration or
participant-rejection constraints. No reasoner was run.

Source 832: SHACL [minimum](https://www.w3.org/TR/shacl/#MinCountConstraintComponent)
and [maximum cardinality](https://www.w3.org/TR/shacl/#MaxCountConstraintComponent)
(sections 4.2.1–4.2.2) support the missing-source
counterexample for an assumed exactly-one requirement.
[SHACL and RDFS inferencing](https://www.w3.org/TR/shacl/#shacl-rdfs), section 1.5,
explains why the selected entailment regime matters. The passage's distinction
between conformance and source truth is appropriate. No executable shape or
validation report is claimed.

## Release readiness checklist

The decisions apply to source `9ceb2d2`, brief r12, the regenerated HTML/PDF outputs, and this audit r15.

| Gate | Decision | Required evidence or limitation |
|---|---|---|
| Brief and audit binding | pass | Source/Reviewed `9ceb2d2`, brief r12; contract `2d47558` r9 baseline reconciled explicitly. |
| Route/concept gate | pass | All 14 IDs and three tiers retained; every primary/alternative transition and section reviewed; no blocking depth row. |
| Locator validity | pass | Structural evidence checker and Git-backed locator/revision checker below; human review supplied teaching judgement. |
| Examples | pass within bounds | Publication report records `just examples` passing both `knowledge-graph-python` and `knowledge-graph-r` offline. Prose operations remain illustrative; full release/disclosure not executed. |
| Rendered outputs | pass | `just all`, render QA, metadata, freshness, variants, Mermaid, structure and README checks passed; visual pages 1, 53 and 7 passed; code page not applicable. |
| Accessibility | blocked | HTML deterministic semantics and SVG alt text pass; PDF reports `Tagged: no`. Keyboard, no-JS, browser accessibility tree, screen reader and PDF tag-tree/reading-order checks remain outstanding under #421. |
| Sources | scoped pass | New RDFS/SHACL claims verified on 12 November; unchanged source checks retain original 11 November provenance. No full renewed citation or dependency attestation. |
| Links | scoped pass | Publication report records offline `just lint-links primer_knowledge_graph/primer_knowledge_graph.html` passing; no full online link check claimed. |
| Revision review | pass | Consolidation, SVG, bridge, brief and contract reviewed with dependent and adjacent routes; all current locators replaced from reading. |
| Handoff | bounded audit complete | Human accessibility checks remain before release; this update owns only the audit. No push/merge authorised here. |

- Content gate: **pass**, for the agreed illustrative primary and alternative teaching routes; no new scope reduction used to excuse a gap.
- Release readiness: **not-ready**, pending the outstanding human accessibility checks.

### Published-output baseline and exact limitation

The publication report `.scratch/render-qa/primer_knowledge_graph/report.md`
was generated at `088a2ba` with modified output files before their final commit;
the HTML and PDF committed at `240d09e` are the checked output bytes. Current
SHA-256 values:

- HTML: `c7fbfb34296d3948fc474de737a8d51eeed7b0a99de92563a357579efb560f22`.
- PDF: `f1b29e83293cfa3172d73e343dcecf920400848da1c1627a42423f4c5eadf105`.

The report records 80 PDF pages and `Tagged: no`; text extraction found no
replacement characters. Visual inspection passed opening page 1, table page 53
and figure page 7. Code page 40 is prose and the source has no code blocks, so
the code-page check is not applicable. Deterministic HTML semantics and the
embedded SVG's alt text passed. These checks do not establish interactive or
assistive-technology accessibility, or resolve #421.

The publication report records `just all` and both examples passing, alongside
`just check-meta`, `just check-fresh` (after commit), `just check-variants`,
`just check-mermaid`, `just check-structure` and `just readme-check`. Scoped
Markdown, spelling and prose lint and the offline HTML link check passed;
structure and prose advisories are documented in the report.

## Execution and render evidence

- **Transition checks:** Codex read and hand-traced every row of the transition
  table at `3f3d384`, including all Q1–Q5, c1/c3 dated joins, A/B/C,
  authorised/ordinary views, scoring, carry-forward citations and topology's
  return to evidence. All reader-facing transitions remain `illustrative`.
- **Examples executed:** `just examples knowledge_graph` from the repository
  root. Initial restricted invocation exited 1 before Python ran:
  `Failed to obtain podman configuration: set sticky bit on: chmod /run/user/1000/libpod: read-only file system`.
  The same command through the permitted elevated path exited 0:
  `PASS knowledge-graph-python` and `PASS knowledge-graph-r`.
- **Runtime and inputs:** manifest `examples/manifest.toml`, profile
  `python-duckdb` using `localhost/knowledge-graph-python:1.4.3`, declared
  Python 3.12.15/DuckDB 1.4.3; profile `r-graph` using
  `localhost/primers-r-graph-runtime:4.5.3`, declared R 4.5.3/igraph 2.3.0/
  tidygraph 1.3.1/dplyr 1.2.1. Runner uses `--pull=never --network=none`,
  read-only repository mount and disposable temporary output directories.
  Neither runtime was rebuilt; declared versions/transitive dependencies were
  not independently re-attested in this run. Scripts and fixtures are unchanged
  since `c7b5a91`; that run is retained evidence from source `3f3d384` and
  was not repeated during r13. The publication report records a later pass.
- **Observed companion results:** Python's assertions pass for the source
  patterns, refusal/abstention, evidence spans, validation, persisted/reopened
  rows, direct/path/provenance/temporal queries and bounded negative repair and
  source correction (script 117–355). R's assertions pass for fixture graph,
  directed path and weak-component result (script 14–52); exact prose degree
  table and strong components were hand-checked separately. The runner
  suppresses successful stdout; the observed output was each PASS line, not
  a saved full result transcript.
- **Examples parsed but not executed:** none claimed. SVG XML was parsed with
  Python standard-library `xml.etree.ElementTree`; its `role="img"`,
  `aria-labelledby="title desc"`, title, description and labels were inspected.
  This is source/static evidence, not visual or assistive-technology testing.
- **Historical revision and baseline checks:** At r12, Git history/diffs for source, brief,
  contract, figures, outputs and examples; byte comparisons against
  `git show 3f3d384:<path>` and `sha256sum` of source/HTML/PDF. Source,
  contract, figure and outputs match that commit; brief r10 is the later
  `f014f1b` checkpoint. Output history then showed last-touch `c7b5a91`;
  publication commit `240d09e` supersedes that output baseline.
- **Mechanical commands:** final structural/Git-backed/diff results are
  recorded immediately below after checking this audit update.
- **Render route in this audit update:** `just primer-audit primer_knowledge_graph`
  invokes examples, a complete build, render QA, freshness and lint/link checks.
  Its build would regenerate forbidden outputs, so the user's audit-only
  instruction takes precedence over the skill's aggregate recipe. In r12, its
  non-mutating structural/revision components and separate companions were run;
  this update repeats only the structural/revision components and records the
  independent publication report.
- **Visual and accessibility checks:** publication report records the visual
  passes above. Browser accessibility tree, keyboard/no-JavaScript, screen-reader,
  PDF tag-tree and reading-order checks remain outstanding.
- **Reviewer effort and stopping rule:** elapsed time was not instrumented; one complete source reading plus
  route/concept/section and targeted verification passes. No suitable bounded
  subagent interface was available in this session. Stop at current audit
  evidence; output regeneration, source/brief/case/figure/example/configuration
  changes, production integrations and release approval are outside ownership.

## Mechanical check results

Results are recorded after the final audit edit; these checks validate evidence
shape, Git binding and whitespace, not content truth or release readiness.

- `just check-primer-evidence primer_knowledge_graph/primer_knowledge_graph.brief.md primer_knowledge_graph/primer_knowledge_graph.audit.md`: **passed**, exit 0; invokes `python3 -I scripts/check/primer_evidence.py` with those paths.
- `python3 -I scripts/check/primer_audit.py --repo-root . --project primer_knowledge_graph`: **passed**, exit 0; source hash is `df978ccf84d9f83947f48a0c4bf2e27ad473181188441be56c7f0de3ea2b7933` and Git binding/locators pass.
- Historical audit r12: `just lint-md primer_knowledge_graph/primer_knowledge_graph.audit.md`: **passed**, exit 0, zero enforced/advisory findings, markdownlint-cli2 0.23.3 / markdownlint 0.41.1. Initial restricted invocation failed on Podman's read-only runtime directory; the identical permitted elevated retry passed.
- `git -C /home/mcooney/workspace/ai_assisted_research diff --check`: **passed**, exit 0; final changed-path review limits this commit to the audit, preserving unrelated `mise.toml`.

## Pilot learning

- False positives: the R fixture's independence and the absence of a deployed
  release/access-control system are agreed scope boundaries, not newly
  discovered primary/alternative teaching gaps. The same Q4 abstention on two
  dates is explained, not evidence that classification was omitted.
- Missed issues: r11's current locators and binding no longer cover this
  source; the r10 checkpoint correctly exposed that mismatch. The r12 review
  recorded the first-use acronym issue, now resolved, and the narrower
  assertion scope of the R runtime test.
- Procedure changes proposed: none. Keep complete source reading, section
  dispositions, transition provenance and the two gate decisions separate.
- Remaining work: the accessibility owner must perform the documented human
  semantic tests and resolve or explicitly disposition #421. No such repair is
  authorised by a passing content gate.
- Final disposition: content passes; release is not-ready. This audit update
  completes the assigned evidence milestone without changing those boundaries.
