# Primer audit: Generalised linear models and their extensions

- Issue and milestone: #468 primer; #467 planning.
- Audit revision: glm-content-audit-v3
- Source revision: 8417dba1d9183041213115f6361d84107ae40109
- Source SHA-256: 27d68fb0fdb9686588bf349404a88764702ae405e1d96cfc99f05d85f19cef07
- Tracked path: primer_glm/primer_glm.audit.md
- Starting branch: docs/468-glm-primer
- Reviewer(s): independent editorial/content reviewer; evidence assembled separately by implementation agent.
- Date: 2026-11-22
- Reviewed revision: 8417dba1d9183041213115f6361d84107ae40109
- Brief reviewed: primer_glm/primer_glm.brief.md, glm-brief-v5.
- Review boundary: independent complete preceding source reading, scoped repair review and subsequent span-only delta inspection; independent fixed-input numerical integration only, not model refit or full execution; visual sampling completed; release checks pending.
- Teaching-case contract: primer_glm/primer_glm.case.md, glm-case-v5.
- Core-concept depth matrix: primer_glm/primer_glm.brief.md, glm-brief-v5.
- Readiness decision: not-ready

The independent complete content reading covered source SHA-256 `84eba056acb9ed85f3f0586b36555887bb4729de0178c62e1d27d91c92bb7e95` at commit `858f4ef29e6e85ef50acbc3231ccc639a27a1b99`. The only subsequent source changes, verified in the Git diff to `8417dba1d9183041213115f6361d84107ae40109`, add inline style attributes to two existing compatibility spans; prose and line positions are unchanged. The independent reviewer did not reread the full source at the new hash. The recorded current revision and concept-row evidence revisions bind the preserved content judgement and this delta inspection to the current source; they do not claim a new independent full read.


Original R01–R11 and C01–C26 retain their exact identities and meanings. Schema aliases are one-to-one r01–r11 and c01–c26, with original IDs included in each row; no reassignment or scope reduction is implied.

## Whole-document review

| Area | Scope and method | Exact evidence or location | Status | Finding or gap | Disposition |
|---|---|---|---|---|---|
| Brief coverage and scope | Independent preceding prose reading and span-only delta inspection; narrower execution as stated | primer_glm/primer_glm.md:69 | verified | All 11 routes and 26 concepts retained | retain stated boundary |
| Technical claims, derivations, and calculations | Independent preceding prose reading and span-only delta inspection; narrower execution as stated | primer_glm/primer_glm.md:337 | verified | Selected algebra and fixed-input integration checked, not all calculations independently executed | retain stated boundary |
| Source quality, attribution, and freshness | Independent preceding prose reading and span-only delta inspection; narrower execution as stated | primer_glm/primer_glm.md:18 | not-checked | Earlier bounded primary-source verification retained; current full source freshness not independently rechecked | retain stated boundary |
| Explanatory depth and prerequisites | Independent preceding prose reading and span-only delta inspection; narrower execution as stated | primer_glm/primer_glm.md:151 | verified | Full preceding source read and transition gaps re-reviewed | retain stated boundary |
| Structure, dependency order, and section fragmentation | Independent preceding prose reading and span-only delta inspection; narrower execution as stated | primer_glm/primer_glm.md:301 | verified | Concrete responses motivate fitting and later extensions | retain stated boundary |
| Worked examples and interpretations | Independent preceding prose reading and span-only delta inspection; narrower execution as stated | primer_glm/primer_glm.md:1066 | verified | Combined diagnostic and repair now explicitly followed | retain stated boundary |
| Applications, limitations, and failure modes | Independent preceding prose reading and span-only delta inspection; narrower execution as stated | primer_glm/primer_glm.md:563 | verified | Gamma undercoverage and NB tail mismatch retained | retain stated boundary |
| Figures, tables, equations, and accessibility | Independent preceding prose reading and span-only delta inspection; narrower execution as stated | primer_glm/primer_glm.md:939 | not-checked | Nine figures inventoried; sampled visual checks passed; assistive-technology accessibility remains unverified | retain stated boundary |
| HTML, PDF, metadata, and committed outputs | Independent preceding prose reading and span-only delta inspection; narrower execution as stated | primer_glm/primer_glm.md:3 | not-checked | Current rebuilt PDF and HTML browser samples passed; render QA passed | retain stated boundary |
| Residual uncertainty and follow-up questions | Independent preceding prose reading and span-only delta inspection; narrower execution as stated | primer_glm/primer_glm.md:1363 | verified | Parameter uncertainty, detection and observational limits remain | retain stated boundary |

## Teaching-case trace

| Case stage | Source or section | Evidence and result | Execution status | Gap or limitation |
|---|---|---|---|---|
| Input or assumptions | primer_glm/primer_glm.md:1088 | 72 sites, known effort and NB2 truth | illustrative | synthetic design; author execution separate |
| Construction or extraction decision | primer_glm/primer_glm.md:1094 | 54 training and 18 held-out sites | illustrative | one fixed split; author execution separate |
| Intermediate representation | primer_glm/primer_glm.md:1096 | five fixed candidate models | illustrative | shared distribution and prediction target; author execution separate |
| Stored or computed result | primer_glm/primer_glm.md:1102 | training discrepancy table | illustrative | simulation summaries include Monte Carlo error; author execution separate |
| Reader-facing query or operation | primer_glm/primer_glm.md:1116 | compare joint site log scores | illustrative | outcomes held out from fitting; author execution separate |
| Interpretation | primer_glm/primer_glm.md:1132 | integrated mean, count interval and joint score | illustrative | fixed model parameters; author execution separate |
| Failure mode or scope limit | primer_glm/primer_glm.md:1138 | reconsider observations and unresolved checks | illustrative | does not establish adequacy or causation; author execution separate |
| Correction and re-evaluation | primer_glm/primer_glm.md:1110 | smooth reduces a gradient pattern; inspect sensitivity | illustrative | site total is not an identification test; author execution separate |

## Brief and example traceability

All route and concept rows below are independently read against the preceding source, with the span-only delta inspected as stated above; executable author evidence is not used as a substitute for reader-path judgement.

## Reader-scale section depth

| Section and route/concept IDs | Teaching job | Reasoning spine or worked thread | Application or interpretation locator | Material limitation or failure-case locator | Disposition and rationale |
|---|---|---|---|---|---|
| Orientation and notation (r01/c01) | bounded orientation | primer_glm/primer_glm.md:3 | primer_glm/primer_glm.md:39 | primer_glm/primer_glm.md:34 | retain: bounded orientation |
| Regression (r01/c02,c03,c22) | design and interval thread | primer_glm/primer_glm.md:69 | primer_glm/primer_glm.md:111 | primer_glm/primer_glm.md:145 | retain: design and interval thread |
| Components, probabilities and positive outcomes (r02/c04; r03/c08,c09; r04/c11) | families before abstraction | primer_glm/primer_glm.md:151 | primer_glm/primer_glm.md:221 | primer_glm/primer_glm.md:273 | retain: families before abstraction |
| Fitting (r02/c05,c06,c07; r03/c23) | score to IRLS and failure | primer_glm/primer_glm.md:301 | primer_glm/primer_glm.md:337 | primer_glm/primer_glm.md:389 | retain: score to IRLS and failure |
| Inference (r04/c12,c13) | contrasts and targets | primer_glm/primer_glm.md:407 | primer_glm/primer_glm.md:449 | primer_glm/primer_glm.md:483 | retain: contrasts and targets |
| Diagnostics (r04/c14) | repair with remaining undercoverage | primer_glm/primer_glm.md:500 | primer_glm/primer_glm.md:565 | primer_glm/primer_glm.md:579 | retain: repair with remaining undercoverage |
| Dispersion (r05/c15,c16) | quasi versus full predictive model | primer_glm/primer_glm.md:601 | primer_glm/primer_glm.md:688 | primer_glm/primer_glm.md:722 | retain: quasi versus full predictive model |
| GLMM (r06/c17) | shared-effect prediction | primer_glm/primer_glm.md:732 | primer_glm/primer_glm.md:790 | primer_glm/primer_glm.md:833 | retain: shared-effect prediction |
| GAM (r10/c18) | penalty and concurvity repair | primer_glm/primer_glm.md:845 | primer_glm/primer_glm.md:892 | primer_glm/primer_glm.md:925 | retain: penalty and concurvity repair |
| Zero processes (r07/c19) | identifiability and detection | primer_glm/primer_glm.md:939 | primer_glm/primer_glm.md:978 | primer_glm/primer_glm.md:1056 | retain: identifiability and detection |
| Combined count case (r05/c16; r06/c17; r10/c18) | actual discrepancy and model revision | primer_glm/primer_glm.md:1066 | primer_glm/primer_glm.md:1102 | primer_glm/primer_glm.md:1138 | retain: actual discrepancy and model revision |
| Categories (r11/c25,c26) | probabilities and ordinal repair | primer_glm/primer_glm.md:1142 | primer_glm/primer_glm.md:1183 | primer_glm/primer_glm.md:1219 | retain: probabilities and ordinal repair |
| Bayesian (r08/c20,c21) | updating, diagnostics and prediction | primer_glm/primer_glm.md:1223 | primer_glm/primer_glm.md:1267 | primer_glm/primer_glm.md:1337 | retain: updating, diagnostics and prediction |
| Synthesis (r01,c01; r05,c16; r06,c17; r10,c18) | carry checks through combined modelling | primer_glm/primer_glm.md:1343 | primer_glm/primer_glm.md:1347 | primer_glm/primer_glm.md:1357 | retain: carry checks through combined modelling |
| Boundaries and exercises (r09/c24) | intentionally bounded reference and exercises | primer_glm/primer_glm.md:1363 | primer_glm/primer_glm.md:1375 | primer_glm/primer_glm.md:1371 | retain: intentionally bounded reference and exercises |

## Route transition evidence

Each transition was independently read, with example execution illustrative to the reviewer. Additional fixed-input numerical execution is reported separately.

| route_id | concept_id(s) | transition (from to) | linked input and reader operation | intermediate reasoning or decision | result | interpretation | material limitation | execution status | gap and reader consequence | original IDs |
|---|---|---|---|---|---|---|---|---|---|---|
| r01 | c01,c02,c03,c22 | input to interpreted result | primer_glm/primer_glm.md:71: Penguin design and species matrix | primer_glm/primer_glm.md:113: fitted means and observation intervals | primer_glm/primer_glm.md:137: worked result | primer_glm/primer_glm.md:137: interpret target | primer_glm/primer_glm.md:145: selection and missingness | illustrative | none found in independent content read | R01, C01,C02,C03,C22 |
| r02 | c04,c05,c06,c07 | input to interpreted result | primer_glm/primer_glm.md:155: family/link and predictor | primer_glm/primer_glm.md:305: score, information and hand IRLS | primer_glm/primer_glm.md:348: worked result | primer_glm/primer_glm.md:348: interpret target | primer_glm/primer_glm.md:371: rank and link constraints | illustrative | none found in independent content read | R02, C04,C05,C06,C07 |
| r03 | c08,c09,c10,c23 | input to interpreted result | primer_glm/primer_glm.md:177: trials, offsets and interactions | primer_glm/primer_glm.md:221: likelihood and probability contrast | primer_glm/primer_glm.md:481: worked result | primer_glm/primer_glm.md:481: interpret target | primer_glm/primer_glm.md:389: separation and penalty assumptions | illustrative | none found in independent content read | R03, C08,C09,C10,C23 |
| r04 | c11,c12,c13,c14 | input to interpreted result | primer_glm/primer_glm.md:253: positive Gamma outcome | primer_glm/primer_glm.md:567: held-out repair and predictive coverage | primer_glm/primer_glm.md:575: worked result | primer_glm/primer_glm.md:575: interpret target | primer_glm/primer_glm.md:579: remaining interval undercoverage | illustrative | none found in independent content read | R04, C11,C12,C13,C14 |
| r05 | c15,c16 | input to interpreted result | primer_glm/primer_glm.md:603: count dispersion | primer_glm/primer_glm.md:647: quasi versus NB and fitted checks | primer_glm/primer_glm.md:712: worked result | primer_glm/primer_glm.md:712: interpret target | primer_glm/primer_glm.md:722: NB tail remains discrepant | illustrative | none found in independent content read | R05, C15,C16 |
| r06 | c17 | input to interpreted result | primer_glm/primer_glm.md:738: repeated sites | primer_glm/primer_glm.md:772: integration and group prediction | primer_glm/primer_glm.md:831: worked result | primer_glm/primer_glm.md:831: interpret target | primer_glm/primer_glm.md:833: few groups and parameter uncertainty | illustrative | none found in independent content read | R06, C17 |
| r10 | c18 | input to interpreted result | primer_glm/primer_glm.md:851: nonlinear gradient | primer_glm/primer_glm.md:870: basis, penalty and smooth repair | primer_glm/primer_glm.md:917: worked result | primer_glm/primer_glm.md:917: interpret target | primer_glm/primer_glm.md:925: concurvity and support | illustrative | none found in independent content read | R10, C18 |
| r07 | c19 | input to interpreted result | primer_glm/primer_glm.md:945: zero observations | primer_glm/primer_glm.md:978: hurdle and mixture mass calculations | primer_glm/primer_glm.md:1020: worked result | primer_glm/primer_glm.md:1020: interpret target | primer_glm/primer_glm.md:1056: detection and non-identifiability | illustrative | none found in independent content read | R07, C19 |
| r11 | c25,c26 | input to interpreted result | primer_glm/primer_glm.md:1148: unordered and ordered categories | primer_glm/primer_glm.md:1187: softmax and cumulative thresholds | primer_glm/primer_glm.md:1219: worked result | primer_glm/primer_glm.md:1219: interpret target | primer_glm/primer_glm.md:1221: proportional-odds and sparse categories | illustrative | none found in independent content read | R11, C25,C26 |
| r08 | c20,c21 | input to interpreted result | primer_glm/primer_glm.md:1227: prior and count likelihood | primer_glm/primer_glm.md:1267: posterior, predictive checking and sampling | primer_glm/primer_glm.md:1311: worked result | primer_glm/primer_glm.md:1311: interpret target | primer_glm/primer_glm.md:1337: prior sensitivity and finite-chain limits | illustrative | none found in independent content read | R08, C20,C21 |
| r05 | c15,c16 | combined diagnostic to revised model | primer_glm/primer_glm.md:1096: fit prespecified candidates | primer_glm/primer_glm.md:1102: inspect residual, zero, tail and site-total discrepancies | primer_glm/primer_glm.md:1110: interpret candidate changes | primer_glm/primer_glm.md:1116: compare joint held-site scores | primer_glm/primer_glm.md:1138: one split, site effect not identified and parameter uncertainty | illustrative | no unresolved content gap; numerical and release gates remain separate | R05, C15,C16 |
| r06 | c17 | combined diagnostic to revised model | primer_glm/primer_glm.md:1096: fit prespecified candidates | primer_glm/primer_glm.md:1102: inspect residual, zero, tail and site-total discrepancies | primer_glm/primer_glm.md:1110: interpret candidate changes | primer_glm/primer_glm.md:1116: compare joint held-site scores | primer_glm/primer_glm.md:1138: one split, site effect not identified and parameter uncertainty | illustrative | no unresolved content gap; numerical and release gates remain separate | R06, C17 |
| r10 | c18 | combined diagnostic to revised model | primer_glm/primer_glm.md:1096: fit prespecified candidates | primer_glm/primer_glm.md:1102: inspect residual, zero, tail and site-total discrepancies | primer_glm/primer_glm.md:1110: interpret candidate changes | primer_glm/primer_glm.md:1116: compare joint held-site scores | primer_glm/primer_glm.md:1138: one split, site effect not identified and parameter uncertainty | illustrative | no unresolved content gap; numerical and release gates remain separate | R10, C18 |

## Adversarial depth gate

| route_id | route tier | concept_id | explanation locator | example/action locator | interpretation locator | limitation locator | evidence revision | reviewer | status | finding | scope decision | original IDs |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| r01 | primary | c01 | primer_glm/primer_glm.md:71 | primer_glm/primer_glm.md:113 | primer_glm/primer_glm.md:113 | primer_glm/primer_glm.md:145 | 8417dba1d9183041213115f6361d84107ae40109 | independent content reviewer | verified | mechanism, action, interpretation and boundary independently read | retain; no scope reduction | R01, C01 |
| r01 | primary | c02 | primer_glm/primer_glm.md:83 | primer_glm/primer_glm.md:101 | primer_glm/primer_glm.md:109 | primer_glm/primer_glm.md:115 | 8417dba1d9183041213115f6361d84107ae40109 | independent content reviewer | verified | mechanism, action, interpretation and boundary independently read | retain; no scope reduction | R01, C02 |
| r01 | primary | c03 | primer_glm/primer_glm.md:95 | primer_glm/primer_glm.md:137 | primer_glm/primer_glm.md:145 | primer_glm/primer_glm.md:145 | 8417dba1d9183041213115f6361d84107ae40109 | independent content reviewer | verified | mechanism, action, interpretation and boundary independently read | retain; no scope reduction | R01, C03 |
| r02 | primary | c04 | primer_glm/primer_glm.md:155 | primer_glm/primer_glm.md:163 | primer_glm/primer_glm.md:167 | primer_glm/primer_glm.md:171 | 8417dba1d9183041213115f6361d84107ae40109 | independent content reviewer | verified | mechanism, action, interpretation and boundary independently read | retain; no scope reduction | R02, C04 |
| r02 | primary | c05 | primer_glm/primer_glm.md:305 | primer_glm/primer_glm.md:319 | primer_glm/primer_glm.md:319 | primer_glm/primer_glm.md:313 | 8417dba1d9183041213115f6361d84107ae40109 | independent content reviewer | verified | mechanism, action, interpretation and boundary independently read | retain; no scope reduction | R02, C05 |
| r02 | primary | c06 | primer_glm/primer_glm.md:223 | primer_glm/primer_glm.md:325 | primer_glm/primer_glm.md:335 | primer_glm/primer_glm.md:325 | 8417dba1d9183041213115f6361d84107ae40109 | independent content reviewer | verified | mechanism, action, interpretation and boundary independently read | retain; no scope reduction | R02, C06 |
| r02 | primary | c07 | primer_glm/primer_glm.md:339 | primer_glm/primer_glm.md:348 | primer_glm/primer_glm.md:350 | primer_glm/primer_glm.md:371 | 8417dba1d9183041213115f6361d84107ae40109 | independent content reviewer | verified | mechanism, action, interpretation and boundary independently read | retain; no scope reduction | R02, C07 |
| r03 | primary | c08 | primer_glm/primer_glm.md:179 | primer_glm/primer_glm.md:223 | primer_glm/primer_glm.md:241 | primer_glm/primer_glm.md:183 | 8417dba1d9183041213115f6361d84107ae40109 | independent content reviewer | verified | mechanism, action, interpretation and boundary independently read | retain; no scope reduction | R03, C08 |
| r03 | primary | c09 | primer_glm/primer_glm.md:191 | primer_glm/primer_glm.md:199 | primer_glm/primer_glm.md:217 | primer_glm/primer_glm.md:199 | 8417dba1d9183041213115f6361d84107ae40109 | independent content reviewer | verified | mechanism, action, interpretation and boundary independently read | retain; no scope reduction | R03, C09 |
| r03 | primary | c10 | primer_glm/primer_glm.md:479 | primer_glm/primer_glm.md:481 | primer_glm/primer_glm.md:483 | primer_glm/primer_glm.md:479 | 8417dba1d9183041213115f6361d84107ae40109 | independent content reviewer | verified | mechanism, action, interpretation and boundary independently read | retain; no scope reduction | R03, C10 |
| r04 | primary | c11 | primer_glm/primer_glm.md:253 | primer_glm/primer_glm.md:277 | primer_glm/primer_glm.md:285 | primer_glm/primer_glm.md:273 | 8417dba1d9183041213115f6361d84107ae40109 | independent content reviewer | verified | mechanism, action, interpretation and boundary independently read | retain; no scope reduction | R04, C11 |
| r04 | primary | c12 | primer_glm/primer_glm.md:413 | primer_glm/primer_glm.md:427 | primer_glm/primer_glm.md:435 | primer_glm/primer_glm.md:445 | 8417dba1d9183041213115f6361d84107ae40109 | independent content reviewer | verified | mechanism, action, interpretation and boundary independently read | retain; no scope reduction | R04, C12 |
| r04 | primary | c13 | primer_glm/primer_glm.md:565 | primer_glm/primer_glm.md:571 | primer_glm/primer_glm.md:575 | primer_glm/primer_glm.md:579 | 8417dba1d9183041213115f6361d84107ae40109 | independent content reviewer | verified | mechanism, action, interpretation and boundary independently read | retain; no scope reduction | R04, C13 |
| r04 | primary | c14 | primer_glm/primer_glm.md:504 | primer_glm/primer_glm.md:526 | primer_glm/primer_glm.md:545 | primer_glm/primer_glm.md:547 | 8417dba1d9183041213115f6361d84107ae40109 | independent content reviewer | verified | mechanism, action, interpretation and boundary independently read | retain; no scope reduction | R04, C14 |
| r05 | alternative | c15 | primer_glm/primer_glm.md:637 | primer_glm/primer_glm.md:649 | primer_glm/primer_glm.md:657 | primer_glm/primer_glm.md:659 | 8417dba1d9183041213115f6361d84107ae40109 | independent content reviewer | verified | mechanism, action, interpretation and boundary independently read | retain; no scope reduction | R05, C15 |
| r05 | alternative | c16 | primer_glm/primer_glm.md:663 | primer_glm/primer_glm.md:688 | primer_glm/primer_glm.md:712 | primer_glm/primer_glm.md:722 | 8417dba1d9183041213115f6361d84107ae40109 | independent content reviewer | verified | mechanism, action, interpretation and boundary independently read | retain; no scope reduction | R05, C16 |
| r06 | alternative | c17 | primer_glm/primer_glm.md:738 | primer_glm/primer_glm.md:802 | primer_glm/primer_glm.md:831 | primer_glm/primer_glm.md:835 | 8417dba1d9183041213115f6361d84107ae40109 | independent content reviewer | verified | mechanism, action, interpretation and boundary independently read | retain; no scope reduction | R06, C17 |
| r10 | alternative | c18 | primer_glm/primer_glm.md:851 | primer_glm/primer_glm.md:899 | primer_glm/primer_glm.md:917 | primer_glm/primer_glm.md:925 | 8417dba1d9183041213115f6361d84107ae40109 | independent content reviewer | verified | mechanism, action, interpretation and boundary independently read | retain; no scope reduction | R10, C18 |
| r07 | alternative | c19 | primer_glm/primer_glm.md:945 | primer_glm/primer_glm.md:978 | primer_glm/primer_glm.md:1020 | primer_glm/primer_glm.md:1056 | 8417dba1d9183041213115f6361d84107ae40109 | independent content reviewer | verified | mechanism, action, interpretation and boundary independently read | retain; no scope reduction | R07, C19 |
| r08 | alternative | c20 | primer_glm/primer_glm.md:1229 | primer_glm/primer_glm.md:1235 | primer_glm/primer_glm.md:1237 | primer_glm/primer_glm.md:1241 | 8417dba1d9183041213115f6361d84107ae40109 | independent content reviewer | verified | mechanism, action, interpretation and boundary independently read | retain; no scope reduction | R08, C20 |
| r08 | alternative | c21 | primer_glm/primer_glm.md:1267 | primer_glm/primer_glm.md:1311 | primer_glm/primer_glm.md:1325 | primer_glm/primer_glm.md:1337 | 8417dba1d9183041213115f6361d84107ae40109 | independent content reviewer | verified | mechanism, action, interpretation and boundary independently read | retain; no scope reduction | R08, C21 |
| r01 | primary | c22 | primer_glm/primer_glm.md:71 | primer_glm/primer_glm.md:111 | primer_glm/primer_glm.md:145 | primer_glm/primer_glm.md:557 | 8417dba1d9183041213115f6361d84107ae40109 | independent content reviewer | verified | mechanism, action, interpretation and boundary independently read | retain; no scope reduction | R01, C22 |
| r03 | primary | c23 | primer_glm/primer_glm.md:381 | primer_glm/primer_glm.md:387 | primer_glm/primer_glm.md:389 | primer_glm/primer_glm.md:405 | 8417dba1d9183041213115f6361d84107ae40109 | independent content reviewer | verified | mechanism, action, interpretation and boundary independently read | retain; no scope reduction | R03, C23 |
| r09 | reference-only | c24 | primer_glm/primer_glm.md:1363 | primer_glm/primer_glm.md:1367 | primer_glm/primer_glm.md:1371 | primer_glm/primer_glm.md:1373 | 8417dba1d9183041213115f6361d84107ae40109 | independent content reviewer | verified | mechanism, action, interpretation and boundary independently read | retain; no scope reduction | R09, C24 |
| r11 | alternative | c25 | primer_glm/primer_glm.md:1148 | primer_glm/primer_glm.md:1177 | primer_glm/primer_glm.md:1173 | primer_glm/primer_glm.md:1181 | 8417dba1d9183041213115f6361d84107ae40109 | independent content reviewer | verified | mechanism, action, interpretation and boundary independently read | retain; no scope reduction | R11, C25 |
| r11 | alternative | c26 | primer_glm/primer_glm.md:1187 | primer_glm/primer_glm.md:1198 | primer_glm/primer_glm.md:1219 | primer_glm/primer_glm.md:1221 | 8417dba1d9183041213115f6361d84107ae40109 | independent content reviewer | verified | mechanism, action, interpretation and boundary independently read | retain; no scope reduction | R11, C26 |

## Execution and independent verification

The independent reviewer read the complete source at the preceding SHA stated above after the prior combined-case finding. Earlier whole review at SHA `167c5d654cd62e7dd463bb45dd141e3636300fdeb84c84ad1d794432bd6cd011` failed the expanded combined route, then the reviewer scoped the diagnostic repair and read the whole frozen source again. The prior source was not saved for an exact textual diff; the final full read establishes current prose judgement without assuming no other changes. The initial independent reviewer also checked selected algebra and independently evaluated the fixed combined fixture using Simpson quadrature: joint log density −5.200793738832468 and F(0), F(5), F(6) 0.4090556883, 0.9692510412, 0.9825167897. This is not independent model fitting or validation.

The example author reports pinned offline `just examples glm combined-r combined-python combined-julia` passed on the isolated implementation commits, including the diagnostic addendum; the reviewer did not rerun those fits. The final 23-entry manifest passed in pinned runtimes; the independent content reviewer did not rerun it. The earlier 20-entry manifest and build checks belong to the fa462de9 predecessor. A code pass does not approve prose, identify ecological mechanisms, or establish production-grade numerical robustness. glmmTMB snippet remains illustrative and is not verified in its runtime.

## Reconcile earlier evidence

The earlier original content-depth gaps, hurdle q-notation defect, duplicate concurvity, and separated-example wording were repaired in the historical fa462de9 audit. The 167c5d65 review found a new combined diagnostic-to-repair gap and an invalid site-total correlation phrase; current independent re-review finds both repaired. The prior primary-source checks cover documented dataset licences/provenance, methods and software at their recorded scope; original Dryad bytes, some publisher landing pages and exhaustive external claims were not verified. Current combined mgcv references use documented `nb`, random-effect smooths, REML and new-level prediction semantics; the author checked implementation against the installed package, not all possible versions. See the source-verification, combined-case and independent reports in the editorial scratch evidence.

## Release readiness checklist

| Gate | Decision | Evidence or limitation |
|---|---|---|
| Current independent content | pass | Full preceding source read; repaired combined transition verified; span-only delta inspected; no independent full reread at current hash |
| Source and locator binding | pass | Source and outputs committed at the recorded revision; Git-backed source and locator recheck passed |
| Examples | pass | Current 23-entry manifest passed in pinned runtimes; independent reviewer did not rerun it |
| Build, render and visual | pass | Current render QA and independent PDF visual sampling passed on pages 1, 11, 12, 50, 51, 66 and 68–70. Browser checks passed in primary and MathML HTML: both preserved fragments and an ordinary heading appeared below the header; MathML display and MathJax inline maths were visible |
| Links and sources | pending | Offline HTML links passed. Online wrapper exited 0 but underlying Lychee exited 2: 68 total, 56 successes, 4 redirects, 8 unsupported, 8 errors (7 DOI 403, 1 DOI redirect limit); no clean online pass |
| Accessibility | advisory | Current PDF untagged and assistive technology, keyboard and navigation not verified; no conformance claim |
| Repository, PR and CI | pending | `just check` and scoped lint passed; draft PR update and current-head CI pending |

- Content gate: **pass**
- Release readiness: **not-ready**

## Pilot learning

The original whole-current review caught an important catalogue-like diagnostic gap despite scores and executable predictions. Repair now carries the observed training pattern through candidate revision and retains the non-diagnostic site-total finding. Independent fixed-fixture checks do not replace fitting verification; runtime, output and release review remain separate.
