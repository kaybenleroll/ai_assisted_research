# Primer audit: Generalised linear models and their extensions

- Issue and milestone: #468 primer; #467 planning.
- Audit revision: glm-content-audit-v1
- Source revision: e77fa0721fe4a062e7219aa3e068e00adcc6ab66
- Source SHA-256: f6487efe39fa5f66aa97c8a1c401c0b8750b013204ac1af39e0cda72adf29da5
- Tracked path: primer_glm/primer_glm.audit.md
- Starting branch: docs/468-glm-primer
- Reviewer(s): independent content-review agent (Terra/medium); evidence assembled separately by integration agent.
- Date: 2026-11-22
- Reviewed revision: e77fa0721fe4a062e7219aa3e068e00adcc6ab66
- Brief reviewed: primer_glm/primer_glm.brief.md, glm-brief-v3.
- Review boundary: whole-document prose review on prior source; scoped changed-passages and dependent-transition re-review at final hash; figures, numerical execution, links and rendered outputs have the narrower boundaries stated below.
- Teaching-case contract: primer_glm/primer_glm.case.md, glm-case-v3.
- Core-concept depth matrix: primer_glm/primer_glm.brief.md, glm-brief-v3.
- Readiness decision: not-ready

Canonical IDs R01–R11 and C01–C26 retain their exact original meanings. Machine-readable tables use the one-to-one lowercase schema aliases `r01`–`r11` and `c01`–`c26`; each row records its original uppercase IDs alongside them. This is a lexical normalisation for this unpublished v3 evidence artefact, not a scope reduction, reassignment or a claim that the lexical forms never changed. The source and output snapshot is bound to the recorded Git commit.


Explicit canonical-to-schema mapping: R01=r01; R02=r02; R03=r03; R04=r04; R05=r05; R06=r06; R07=r07; R08=r08; R09=r09; R10=r10; R11=r11. C01=c01; C02=c02; C03=c03; C04=c04; C05=c05; C06=c06; C07=c07; C08=c08; C09=c09; C10=c10; C11=c11; C12=c12; C13=c13; C14=c14; C15=c15; C16=c16; C17=c17; C18=c18; C19=c19; C20=c20; C21=c21; C22=c22; C23=c23; C24=c24; C25=c25; C26=c26.

## Whole-document review

| Area | Scope and method | Exact evidence or location | Status | Finding or gap | Disposition |
|---|---|---|---|---|---|
| Brief coverage and scope | Whole-document initial review; changed transitions re-reviewed | primer_glm/primer_glm.md:65 | verified | R01–R11 retained, no demotion | Content gate pass |
| Technical claims, derivations, and calculations | Whole prose read; selected formulas checked analytically | primer_glm/primer_glm.md:186 | verified | Not every numerical output independently executed | Retain scope and complete technical checks |
| Source quality, attribution, and freshness | Path and attribution checked only in part | primer_glm/primer_glm.md:26 | not-checked | Independent rights, source and freshness verification remains | Release gate pending |
| Explanatory depth and prerequisites | Whole-document and changed route review | primer_glm/primer_glm.md:73 | verified | Original gaps repaired | Retain |
| Structure, dependency order, and section fragmentation | Full review; duplicate concurvity consolidated and re-reviewed | primer_glm/primer_glm.md:942 | verified | C18 now retains one explanation | Retain |
| Worked examples and interpretations | Whole-document inventory; scoped review of repairs | primer_glm/primer_glm.md:405 | verified | Targeted author runs reported; reviewer did not rerun | Retain execution distinction |
| Applications, limitations, and failure modes | Whole-document and changed-route review | primer_glm/primer_glm.md:409 | verified | Gamma undercoverage and NB tail discrepancy remain visible | Do not describe them as fixed |
| Figures, tables, equations, and accessibility | Captions reviewed; hurdle image inspected separately | primer_glm/primer_glm.md:1045 | not-checked | Complete visual and accessibility QA not performed by reviewer | Release gate pending |
| HTML, PDF, metadata, and committed outputs | Not assessed | primer_glm/primer_glm.md:3 | not-checked | Rendered assets and Git snapshot pending | Release gate pending |
| Residual uncertainty and follow-up questions | Bounded review | primer_glm/primer_glm.md:1147 | verified | GLMM, MCMC, numerical and observational limits remain | Keep stated limits |

## Teaching-case trace

| Case stage | Source or section | Evidence and result | Execution status | Gap or limitation |
|---|---|---|---|---|
| Input or assumptions | primer_glm/primer_glm.md:405 | 400 independent Gamma observations and declared model | illustrative | Reviewer did not rerun |
| Construction or extraction decision | primer_glm/primer_glm.md:405 | fixed 250 training and 150 test units | illustrative | independent synthetic units, not ecological sampling claim |
| Intermediate representation | primer_glm/primer_glm.md:407 | intercept-only then x-dependent Gamma mean | illustrative | fitted family assumptions apply |
| Stored or computed result | primer_glm/primer_glm.md:407 | held-out residual pattern and revised fit | illustrative | author execution reported separately |
| Reader-facing query or operation | primer_glm/primer_glm.md:409 | compare same-test scores and predictive coverage | illustrative | one split and fitted-parameter assumptions |
| Interpretation | primer_glm/primer_glm.md:411 | mean and future-observation intervals at x=0.8 | illustrative | bootstrap tail and model uncertainty |
| Failure mode or scope limit | primer_glm/primer_glm.md:409 | revised interval covers 89.3% in sample | illustrative | does not establish coverage in a target population |
| Correction and re-evaluation | primer_glm/primer_glm.md:407 | add x, re-evaluate residuals and score | illustrative | remaining uncertainty not declared solved |

## Brief and example traceability

The route transition and concept matrices below map the reader promise to the same source revision. Executed author examples support the numerical evidence but are not substituted for the independent prose judgement; snippets explicitly marked illustrative remain unverified as production code.

## Reader-scale section depth

| Section and route/concept IDs | Teaching job | Reasoning spine or worked thread | Application or interpretation locator | Material limitation or failure-case locator | Disposition and rationale |
|---|---|---|---|---|---|
| Orientation and notation (r01/c01) | Orientation and notation reader action | primer_glm/primer_glm.md:3 to primer_glm/primer_glm.md:3 | primer_glm/primer_glm.md:3 | primer_glm/primer_glm.md:9 | retain: deliberately bounded orientation |
| Regression (r01/c02,c03,c22) | Regression reader action | primer_glm/primer_glm.md:65 to primer_glm/primer_glm.md:101 | primer_glm/primer_glm.md:101 | primer_glm/primer_glm.md:140 | retain: design and fitted intervals |
| GLM components (r02/c04,c05) | GLM components reader action | primer_glm/primer_glm.md:148 to primer_glm/primer_glm.md:166 | primer_glm/primer_glm.md:166 | primer_glm/primer_glm.md:164 | retain: link and moments |
| Fitting (r02/c06,c07; r03/c23) | Fitting reader action | primer_glm/primer_glm.md:182 to primer_glm/primer_glm.md:200 | primer_glm/primer_glm.md:200 | primer_glm/primer_glm.md:246 | retain: derivation and separation repair |
| Probability and counts (r03/c08,c09,c10) | Probability and counts reader action | primer_glm/primer_glm.md:266 to primer_glm/primer_glm.md:284 | primer_glm/primer_glm.md:284 | primer_glm/primer_glm.md:310 | retain: denominators and offset |
| Positive response (r04/c11,c13) | Positive response reader action | primer_glm/primer_glm.md:364 to primer_glm/primer_glm.md:405 | primer_glm/primer_glm.md:405 | primer_glm/primer_glm.md:409 | retain: held-out repair and undercoverage |
| Inference (r04/c12,c14) | Inference reader action | primer_glm/primer_glm.md:431 to primer_glm/primer_glm.md:451 | primer_glm/primer_glm.md:451 | primer_glm/primer_glm.md:507 | retain: tests and diagnostics |
| Categorical (r11/c25,c26) | Categorical reader action | primer_glm/primer_glm.md:581 to primer_glm/primer_glm.md:610 | primer_glm/primer_glm.md:610 | primer_glm/primer_glm.md:654 | retain: probabilities and ordinal repair |
| Dispersion (r05/c15,c16) | Dispersion reader action | primer_glm/primer_glm.md:658 to primer_glm/primer_glm.md:713 | primer_glm/primer_glm.md:713 | primer_glm/primer_glm.md:747 | retain: NB tail failure |
| Dependence (r06/c17) | Dependence reader action | primer_glm/primer_glm.md:757 to primer_glm/primer_glm.md:811 | primer_glm/primer_glm.md:811 | primer_glm/primer_glm.md:858 | retain: group and uncertainty limits |
| Smooths (r10/c18) | Smooths reader action | primer_glm/primer_glm.md:868 to primer_glm/primer_glm.md:909 | primer_glm/primer_glm.md:909 | primer_glm/primer_glm.md:942 | retain: duplicate consolidated and re-reviewed |
| Zeros (r07/c19) | Zeros reader action | primer_glm/primer_glm.md:956 to primer_glm/primer_glm.md:995 | primer_glm/primer_glm.md:995 | primer_glm/primer_glm.md:1073 | retain: corrected symbol and non-identifiability |
| Bayesian (r08/c20,c21) | Bayesian reader action | primer_glm/primer_glm.md:1083 to primer_glm/primer_glm.md:1107 | primer_glm/primer_glm.md:1107 | primer_glm/primer_glm.md:1147 | retain: count and posterior diagnostics |
| Synthesis and boundaries (r09/c24) | Synthesis and boundaries reader action | primer_glm/primer_glm.md:1181 to primer_glm/primer_glm.md:1199 | primer_glm/primer_glm.md:1199 | primer_glm/primer_glm.md:1205 | retain: bounded reference |

## Route transition evidence

These rows reflect the independent review's *illustrative* execution status; author-reported execution is recorded separately. Input, intermediate reasoning, output, interpretation and limitations are explicit and linked in reader order.

| route_id | concept_id(s) | transition (from to) | linked input and reader operation | intermediate reasoning or decision | result | interpretation | material limitation | execution status | gap and reader consequence | original IDs |
|---|---|---|---|---|---|---|---|---|---|---|
| r01 | c01,c02,c03,c22 | input to representation | primer_glm/primer_glm.md:65: Penguin sampling and model matrix | primer_glm/primer_glm.md:73: species fit | primer_glm/primer_glm.md:101: reader calculation | primer_glm/primer_glm.md:126: mean and future intervals | primer_glm/primer_glm.md:140: observational selection and variance | illustrative | none in content review; verification limits remain | R01, C01, C02, C03, C22 |
| r01 | c01,c02,c03,c22 | representation to interpreted boundary | primer_glm/primer_glm.md:101: take prior operation forward | primer_glm/primer_glm.md:73: retain model and design assumptions | primer_glm/primer_glm.md:126: mean and future intervals | primer_glm/primer_glm.md:126: interpret target | primer_glm/primer_glm.md:140: observational selection and variance | illustrative | none in content review; numerical and release QA separate | R01, C01, C02, C03, C22 |
| r02 | c04,c05,c06,c07 | input to representation | primer_glm/primer_glm.md:148: family and link | primer_glm/primer_glm.md:166: moments and score | primer_glm/primer_glm.md:186: reader calculation | primer_glm/primer_glm.md:200: IRLS update | primer_glm/primer_glm.md:234: rank and link assumptions | illustrative | none in content review; verification limits remain | R02, C04, C05, C06, C07 |
| r02 | c04,c05,c06,c07 | representation to interpreted boundary | primer_glm/primer_glm.md:186: take prior operation forward | primer_glm/primer_glm.md:166: retain model and design assumptions | primer_glm/primer_glm.md:200: IRLS update | primer_glm/primer_glm.md:200: interpret target | primer_glm/primer_glm.md:234: rank and link assumptions | illustrative | none in content review; numerical and release QA separate | R02, C04, C05, C06, C07 |
| r03 | c08,c09,c10,c23 | input to representation | primer_glm/primer_glm.md:270: binomial trials and exposure | primer_glm/primer_glm.md:284: logistic and Poisson models | primer_glm/primer_glm.md:334: reader calculation | primer_glm/primer_glm.md:509: offset and interaction | primer_glm/primer_glm.md:246: separation and ridge sensitivity | illustrative | none in content review; verification limits remain | R03, C08, C09, C10, C23 |
| r03 | c08,c09,c10,c23 | representation to interpreted boundary | primer_glm/primer_glm.md:334: take prior operation forward | primer_glm/primer_glm.md:284: retain model and design assumptions | primer_glm/primer_glm.md:509: offset and interaction | primer_glm/primer_glm.md:509: interpret target | primer_glm/primer_glm.md:246: separation and ridge sensitivity | illustrative | none in content review; numerical and release QA separate | R03, C08, C09, C10, C23 |
| r04 | c11,c12,c13,c14 | input to representation | primer_glm/primer_glm.md:364: positive Gamma response | primer_glm/primer_glm.md:405: held-out correction | primer_glm/primer_glm.md:435: reader calculation | primer_glm/primer_glm.md:451: prediction intervals and nested test | primer_glm/primer_glm.md:409: undercoverage and approximation | illustrative | none in content review; verification limits remain | R04, C11, C12, C13, C14 |
| r04 | c11,c12,c13,c14 | representation to interpreted boundary | primer_glm/primer_glm.md:435: take prior operation forward | primer_glm/primer_glm.md:405: retain model and design assumptions | primer_glm/primer_glm.md:451: prediction intervals and nested test | primer_glm/primer_glm.md:451: interpret target | primer_glm/primer_glm.md:409: undercoverage and approximation | illustrative | none in content review; numerical and release QA separate | R04, C11, C12, C13, C14 |
| r05 | c15,c16 | input to representation | primer_glm/primer_glm.md:664: extra count variance | primer_glm/primer_glm.md:676: quasi and NB | primer_glm/primer_glm.md:713: reader calculation | primer_glm/primer_glm.md:741: fitted means and simulated checks | primer_glm/primer_glm.md:747: NB upper-tail mismatch | illustrative | none in content review; verification limits remain | R05, C15, C16 |
| r05 | c15,c16 | representation to interpreted boundary | primer_glm/primer_glm.md:713: take prior operation forward | primer_glm/primer_glm.md:676: retain model and design assumptions | primer_glm/primer_glm.md:741: fitted means and simulated checks | primer_glm/primer_glm.md:741: interpret target | primer_glm/primer_glm.md:747: NB upper-tail mismatch | illustrative | none in content review; numerical and release QA separate | R05, C15, C16 |
| r06 | c17 | input to representation | primer_glm/primer_glm.md:761: clustered visits | primer_glm/primer_glm.md:783: integrated site effects | primer_glm/primer_glm.md:811: reader calculation | primer_glm/primer_glm.md:856: known/new-site prediction and group score | primer_glm/primer_glm.md:862: small groups and parameter uncertainty | illustrative | none in content review; verification limits remain | R06, C17 |
| r06 | c17 | representation to interpreted boundary | primer_glm/primer_glm.md:811: take prior operation forward | primer_glm/primer_glm.md:783: retain model and design assumptions | primer_glm/primer_glm.md:856: known/new-site prediction and group score | primer_glm/primer_glm.md:856: interpret target | primer_glm/primer_glm.md:862: small groups and parameter uncertainty | illustrative | none in content review; numerical and release QA separate | R06, C17 |
| r10 | c18 | input to representation | primer_glm/primer_glm.md:872: nonlinear gradient | primer_glm/primer_glm.md:891: basis and penalty | primer_glm/primer_glm.md:909: reader calculation | primer_glm/primer_glm.md:942: smooth fit and concurvity repair | primer_glm/primer_glm.md:948: support and grouped validation | illustrative | none in content review; verification limits remain | R10, C18 |
| r10 | c18 | representation to interpreted boundary | primer_glm/primer_glm.md:909: take prior operation forward | primer_glm/primer_glm.md:891: retain model and design assumptions | primer_glm/primer_glm.md:942: smooth fit and concurvity repair | primer_glm/primer_glm.md:942: interpret target | primer_glm/primer_glm.md:948: support and grouped validation | illustrative | none in content review; numerical and release QA separate | R10, C18 |
| r11 | c25,c26 | input to representation | primer_glm/primer_glm.md:585: category observations | primer_glm/primer_glm.md:622: softmax and ordered thresholds | primer_glm/primer_glm.md:639: reader calculation | primer_glm/primer_glm.md:654: probability and held-out comparison | primer_glm/primer_glm.md:616: sparse categories and assumptions | illustrative | none in content review; verification limits remain | R11, C25, C26 |
| r11 | c25,c26 | representation to interpreted boundary | primer_glm/primer_glm.md:639: take prior operation forward | primer_glm/primer_glm.md:622: retain model and design assumptions | primer_glm/primer_glm.md:654: probability and held-out comparison | primer_glm/primer_glm.md:654: interpret target | primer_glm/primer_glm.md:616: sparse categories and assumptions | illustrative | none in content review; numerical and release QA separate | R11, C25, C26 |
| r07 | c19 | input to representation | primer_glm/primer_glm.md:960: zero counts | primer_glm/primer_glm.md:978: hurdle and mixture masses | primer_glm/primer_glm.md:995: reader calculation | primer_glm/primer_glm.md:1039: held-out predictions | primer_glm/primer_glm.md:1073: detection and unidentified mechanisms | illustrative | none in content review; verification limits remain | R07, C19 |
| r07 | c19 | representation to interpreted boundary | primer_glm/primer_glm.md:995: take prior operation forward | primer_glm/primer_glm.md:978: retain model and design assumptions | primer_glm/primer_glm.md:1039: held-out predictions | primer_glm/primer_glm.md:1039: interpret target | primer_glm/primer_glm.md:1073: detection and unidentified mechanisms | illustrative | none in content review; numerical and release QA separate | R07, C19 |
| r08 | c20,c21 | input to representation | primer_glm/primer_glm.md:1087: prior and likelihood | primer_glm/primer_glm.md:1107: posterior and predictive check | primer_glm/primer_glm.md:1113: reader calculation | primer_glm/primer_glm.md:1139: count interval and sampling | primer_glm/primer_glm.md:1147: prior and diagnostics limits | illustrative | none in content review; verification limits remain | R08, C20, C21 |
| r08 | c20,c21 | representation to interpreted boundary | primer_glm/primer_glm.md:1113: take prior operation forward | primer_glm/primer_glm.md:1107: retain model and design assumptions | primer_glm/primer_glm.md:1139: count interval and sampling | primer_glm/primer_glm.md:1139: interpret target | primer_glm/primer_glm.md:1147: prior and diagnostics limits | illustrative | none in content review; numerical and release QA separate | R08, C20, C21 |
| r09 | c24 | input to representation | primer_glm/primer_glm.md:1195: boundary recognition | primer_glm/primer_glm.md:1199: specialist structures | primer_glm/primer_glm.md:1199: reader calculation | primer_glm/primer_glm.md:1199: next reading | primer_glm/primer_glm.md:1205: not taught as fitted route | illustrative | none in content review; verification limits remain | R09, C24 |
| r09 | c24 | representation to interpreted boundary | primer_glm/primer_glm.md:1199: take prior operation forward | primer_glm/primer_glm.md:1199: retain model and design assumptions | primer_glm/primer_glm.md:1199: next reading | primer_glm/primer_glm.md:1199: interpret target | primer_glm/primer_glm.md:1205: not taught as fitted route | illustrative | none in content review; numerical and release QA separate | R09, C24 |

## Adversarial depth gate

The independent reviewer recorded `verified` for every concept at the reviewed prose scope. Original E/A/I/L locator groups are retained in `.scratch/glm-repairs-2026-11-22/re-audit.md`; the table selects an exact source line for each field and preserves the reviewer’s final R07 correction. The final reviewer did not independently rerun the suite.

| route_id | route tier | concept_id | explanation locator | example/action locator | interpretation locator | limitation locator | evidence revision | reviewer | status | finding | scope decision | original IDs |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| r01 | primary | c01 | primer_glm/primer_glm.md:65 | primer_glm/primer_glm.md:69 | primer_glm/primer_glm.md:65 | primer_glm/primer_glm.md:69 | e77fa0721fe4a062e7219aa3e068e00adcc6ab66 | independent content-review agent | verified | Study design and estimand reader path and limit reviewed | retain; no scope reduction | R01, C01 |
| r01 | primary | c02 | primer_glm/primer_glm.md:73 | primer_glm/primer_glm.md:91 | primer_glm/primer_glm.md:83 | primer_glm/primer_glm.md:89 | e77fa0721fe4a062e7219aa3e068e00adcc6ab66 | independent content-review agent | verified | Ordinary regression reader path and limit reviewed | retain; no scope reduction | R01, C02 |
| r01 | primary | c03 | primer_glm/primer_glm.md:89 | primer_glm/primer_glm.md:126 | primer_glm/primer_glm.md:126 | primer_glm/primer_glm.md:140 | e77fa0721fe4a062e7219aa3e068e00adcc6ab66 | independent content-review agent | verified | Gaussian error and prediction reader path and limit reviewed | retain; no scope reduction | R01, C03 |
| r02 | primary | c04 | primer_glm/primer_glm.md:148 | primer_glm/primer_glm.md:154 | primer_glm/primer_glm.md:154 | primer_glm/primer_glm.md:164 | e77fa0721fe4a062e7219aa3e068e00adcc6ab66 | independent content-review agent | verified | GLM components reader path and limit reviewed | retain; no scope reduction | R02, C04 |
| r02 | primary | c05 | primer_glm/primer_glm.md:166 | primer_glm/primer_glm.md:174 | primer_glm/primer_glm.md:174 | primer_glm/primer_glm.md:174 | e77fa0721fe4a062e7219aa3e068e00adcc6ab66 | independent content-review agent | verified | Exponential family reader path and limit reviewed | retain; no scope reduction | R02, C05 |
| r02 | primary | c06 | primer_glm/primer_glm.md:186 | primer_glm/primer_glm.md:334 | primer_glm/primer_glm.md:186 | primer_glm/primer_glm.md:186 | e77fa0721fe4a062e7219aa3e068e00adcc6ab66 | independent content-review agent | verified | Likelihood and scores reader path and limit reviewed | retain; no scope reduction | R02, C06 |
| r02 | primary | c07 | primer_glm/primer_glm.md:200 | primer_glm/primer_glm.md:200 | primer_glm/primer_glm.md:213 | primer_glm/primer_glm.md:213 | e77fa0721fe4a062e7219aa3e068e00adcc6ab66 | independent content-review agent | verified | IRLS reader path and limit reviewed | retain; no scope reduction | R02, C07 |
| r03 | primary | c08 | primer_glm/primer_glm.md:270 | primer_glm/primer_glm.md:334 | primer_glm/primer_glm.md:272 | primer_glm/primer_glm.md:274 | e77fa0721fe4a062e7219aa3e068e00adcc6ab66 | independent content-review agent | verified | Binomial outcomes reader path and limit reviewed | retain; no scope reduction | R03, C08 |
| r03 | primary | c09 | primer_glm/primer_glm.md:278 | primer_glm/primer_glm.md:284 | primer_glm/primer_glm.md:286 | primer_glm/primer_glm.md:286 | e77fa0721fe4a062e7219aa3e068e00adcc6ab66 | independent content-review agent | verified | Poisson counts and offsets reader path and limit reviewed | retain; no scope reduction | R03, C09 |
| r03 | primary | c10 | primer_glm/primer_glm.md:509 | primer_glm/primer_glm.md:509 | primer_glm/primer_glm.md:511 | primer_glm/primer_glm.md:509 | e77fa0721fe4a062e7219aa3e068e00adcc6ab66 | independent content-review agent | verified | Interactions and contrasts reader path and limit reviewed | retain; no scope reduction | R03, C10 |
| r04 | primary | c11 | primer_glm/primer_glm.md:364 | primer_glm/primer_glm.md:405 | primer_glm/primer_glm.md:407 | primer_glm/primer_glm.md:409 | e77fa0721fe4a062e7219aa3e068e00adcc6ab66 | independent content-review agent | verified | Gamma response reader path and limit reviewed | retain; no scope reduction | R04, C11 |
| r04 | primary | c12 | primer_glm/primer_glm.md:435 | primer_glm/primer_glm.md:451 | primer_glm/primer_glm.md:451 | primer_glm/primer_glm.md:459 | e77fa0721fe4a062e7219aa3e068e00adcc6ab66 | independent content-review agent | verified | Inference and comparison reader path and limit reviewed | retain; no scope reduction | R04, C12 |
| r04 | primary | c13 | primer_glm/primer_glm.md:435 | primer_glm/primer_glm.md:411 | primer_glm/primer_glm.md:411 | primer_glm/primer_glm.md:409 | e77fa0721fe4a062e7219aa3e068e00adcc6ab66 | independent content-review agent | verified | Prediction and validation reader path and limit reviewed | retain; no scope reduction | R04, C13 |
| r04 | primary | c14 | primer_glm/primer_glm.md:473 | primer_glm/primer_glm.md:532 | primer_glm/primer_glm.md:542 | primer_glm/primer_glm.md:475 | e77fa0721fe4a062e7219aa3e068e00adcc6ab66 | independent content-review agent | verified | Diagnostics reader path and limit reviewed | retain; no scope reduction | R04, C14 |
| r05 | alternative | c15 | primer_glm/primer_glm.md:676 | primer_glm/primer_glm.md:713 | primer_glm/primer_glm.md:739 | primer_glm/primer_glm.md:684 | e77fa0721fe4a062e7219aa3e068e00adcc6ab66 | independent content-review agent | verified | Quasi-likelihood reader path and limit reviewed | retain; no scope reduction | R05, C15 |
| r05 | alternative | c16 | primer_glm/primer_glm.md:690 | primer_glm/primer_glm.md:713 | primer_glm/primer_glm.md:739 | primer_glm/primer_glm.md:707 | e77fa0721fe4a062e7219aa3e068e00adcc6ab66 | independent content-review agent | verified | Negative binomial reader path and limit reviewed | retain; no scope reduction | R05, C16 |
| r06 | alternative | c17 | primer_glm/primer_glm.md:761 | primer_glm/primer_glm.md:811 | primer_glm/primer_glm.md:856 | primer_glm/primer_glm.md:805 | e77fa0721fe4a062e7219aa3e068e00adcc6ab66 | independent content-review agent | verified | GLMM dependence reader path and limit reviewed | retain; no scope reduction | R06, C17 |
| r10 | alternative | c18 | primer_glm/primer_glm.md:872 | primer_glm/primer_glm.md:909 | primer_glm/primer_glm.md:938 | primer_glm/primer_glm.md:940 | e77fa0721fe4a062e7219aa3e068e00adcc6ab66 | independent content-review agent | verified | GAM smooths reader path and limit reviewed | retain; no scope reduction | R10, C18 |
| r07 | alternative | c19 | primer_glm/primer_glm.md:960 | primer_glm/primer_glm.md:995 | primer_glm/primer_glm.md:995 | primer_glm/primer_glm.md:1019 | e77fa0721fe4a062e7219aa3e068e00adcc6ab66 | independent content-review agent | verified | Hurdle and zero inflation reader path and limit reviewed | retain; no scope reduction | R07, C19 |
| r08 | alternative | c20 | primer_glm/primer_glm.md:1087 | primer_glm/primer_glm.md:1107 | primer_glm/primer_glm.md:1107 | primer_glm/primer_glm.md:1111 | e77fa0721fe4a062e7219aa3e068e00adcc6ab66 | independent content-review agent | verified | Bayesian estimation reader path and limit reviewed | retain; no scope reduction | R08, C20 |
| r08 | alternative | c21 | primer_glm/primer_glm.md:1111 | primer_glm/primer_glm.md:1111 | primer_glm/primer_glm.md:1113 | primer_glm/primer_glm.md:1113 | e77fa0721fe4a062e7219aa3e068e00adcc6ab66 | independent content-review agent | verified | Bayesian workflow reader path and limit reviewed | retain; no scope reduction | R08, C21 |
| r01 | primary | c22 | primer_glm/primer_glm.md:65 | primer_glm/primer_glm.md:101 | primer_glm/primer_glm.md:101 | primer_glm/primer_glm.md:65 | e77fa0721fe4a062e7219aa3e068e00adcc6ab66 | independent content-review agent | verified | Missingness, measurement and selection reader path and limit reviewed | retain; no scope reduction | R01, C22 |
| r03 | primary | c23 | primer_glm/primer_glm.md:240 | primer_glm/primer_glm.md:246 | primer_glm/primer_glm.md:246 | primer_glm/primer_glm.md:246 | e77fa0721fe4a062e7219aa3e068e00adcc6ab66 | independent content-review agent | verified | Regularisation and separation reader path and limit reviewed | retain; no scope reduction | R03, C23 |
| r09 | reference-only | c24 | primer_glm/primer_glm.md:1195 | primer_glm/primer_glm.md:1199 | primer_glm/primer_glm.md:1199 | primer_glm/primer_glm.md:1199 | e77fa0721fe4a062e7219aa3e068e00adcc6ab66 | independent content-review agent | verified | Other response and dependence structures reader path and limit reviewed | retain; no scope reduction | R09, C24 |
| r11 | alternative | c25 | primer_glm/primer_glm.md:585 | primer_glm/primer_glm.md:610 | primer_glm/primer_glm.md:610 | primer_glm/primer_glm.md:616 | e77fa0721fe4a062e7219aa3e068e00adcc6ab66 | independent content-review agent | verified | Multinomial response reader path and limit reviewed | retain; no scope reduction | R11, C25 |
| r11 | alternative | c26 | primer_glm/primer_glm.md:622 | primer_glm/primer_glm.md:639 | primer_glm/primer_glm.md:639 | primer_glm/primer_glm.md:654 | e77fa0721fe4a062e7219aa3e068e00adcc6ab66 | independent content-review agent | verified | Ordinal response reader path and limit reviewed | retain; no scope reduction | R11, C26 |

## Published snippets and calculations

| Published snippet or calculation | Test/manifest ID or illustrative status | Fixture and expected result checked | Gap |
|---|---|---|---|
| Core, dispersion, grouped and predictive repair | core-repairs-r; extensions-bayes-repairs-r, author reported | Fixed synthetic inputs and frozen penguins; targeted run reported by integration agent | Independent content reviewer did not rerun; whole final suite pending |
| glmmTMB zero-model package snippet | illustrative | Model intent explained at primer_glm/primer_glm.md:1047 | Package snippet not verified in chosen runtime |
| MCMC random-walk teaching code | bayes-r, author reported | Small posterior/grid comparison; batch-means estimate | Not a vetted general-purpose sampler or full R-hat/ESS implementation |

## Representative sampling

| Sample/page/object | Risk represented | Evidence and result | Status | Follow-up |
|---|---|---|---|---|
| Opening motivation | Reader scope | primer_glm/primer_glm.md:3 | verified | preserve boundaries |
| IRLS derivation | Mathematical transition | primer_glm/primer_glm.md:200 | verified | independent run not claimed |
| Gamma held-out repair | Prediction and remaining failure | primer_glm/primer_glm.md:405 | verified | undercoverage remains |
| Penguins and Salamanders | Design and provenance | primer_glm/primer_glm.md:101 | verified | full rights/source verification pending |
| Figure 07 | Hurdle notation | primer_glm/primer_glm.md:1045; image hash recorded below | verified | HTML/PDF visual placement pending |

## Revision-triggered second audit

| Previous and current revisions | Changed artefacts and exact passages | Affected route/concept rows, transitions, claims, examples and outputs | Review scope, reviewer, method and result | Remaining gaps and readiness consequence |
|---|---|---|---|---|
| Source SHA c1e147a4beddad3309f521ea13e3f5c07f961a1385aaa8fc410609500c7cad27 to 05f5a389c68a7854dbb2430ba0064b1018a5b0e7f41b236b27122e3de9775694 | Core, extension, Bayesian and figures; primer_glm/primer_glm.md:126, primer_glm/primer_glm.md:747, primer_glm/primer_glm.md:856, primer_glm/primer_glm.md:942, primer_glm/primer_glm.md:1045, primer_glm/primer_glm.md:1107 | Original route gaps repaired, figure q defect found | Independent reviewer scoped re-review, content initially fail | Figure notation correction then re-review required |
| Source SHA 05f5a389c68a7854dbb2430ba0064b1018a5b0e7f41b236b27122e3de9775694 to 634e7a79d25fe4646ac049eab957f61991e2376105e8c8643515334505229df5 | Figure 07 generator and PNG, concurvity consolidation, separated-example wording, documentation links; primer_glm/primer_glm.md:56, primer_glm/primer_glm.md:246, primer_glm/primer_glm.md:942, primer_glm/primer_glm.md:1045 | R07/C19, R10/C18, R03/C23 and dependent figure semantics | Independent reviewer inspected changed prose and actual image; final content pass | Other independent execution, rendered placement and release checks pending |

| Evidence and affected rows | Retained or newly reviewed/executed | Revision, method, result and reason for retention | Limits or outstanding checks |
|---|---|---|---|
| Unchanged whole-document prose, all unaffected concepts | retained | Earlier independent whole-document review; scoped re-review preserves prior evidence | Not a new full read or full execution |
| R07/C19 figure and adjacent semantics | newly reviewed | Final source SHA 634e7a79d25fe4646ac049eab957f61991e2376105e8c8643515334505229df5; image SHA 5d3b3d334327ed95bd8f0d19d7805fc3282a8b841da19982eec7ae848a2b5c83, generator SHA 3f2ac25f2e113dda670152a2def0b69d26525bcb0e3eea0b15875b587d0d960c; reviewer opened image | HTML/PDF placement and accessibility remain pending |
| Targeted R repairs | author-reported execution | `just examples glm core-repairs-r extensions-bayes-repairs-r` passed per integration report | Independent reviewer did not rerun; final full suite pending |

## Reconcile earlier evidence

| Earlier finding or audit | Location and revision reported | Current status | Evidence |
|---|---|---|---|
| Whole-document initial gaps | `.scratch/glm-draft-2026-11-21/whole-audit.md`, SHA c1e147a4beddad3309f521ea13e3f5c07f961a1385aaa8fc410609500c7cad27 | resolved | independent re-review at final source SHA, route evidence above |
| Hurdle figure q mismatch | provisional re-audit, source SHA 05f5a389c68a7854dbb2430ba0064b1018a5b0e7f41b236b27122e3de9775694 | resolved | final scoped image and caption check at primer_glm/primer_glm.md:1045 |
| Duplicate concurvity and separation wording | provisional re-audit | resolved | final scoped review at primer_glm/primer_glm.md:942 and primer_glm/primer_glm.md:246 |

## Release readiness checklist

| Gate | Decision | Required evidence or limitation |
|---|---|---|
| Brief and audit binding | not-ready | Source snapshot is committed; final evidence binding remains to be checked |
| Route/concept gate | pass | Independent content pass; all taught routes verified at stated review scope |
| Locator validity | not-ready | Git-backed source and line verification to be run against committed snapshot |
| Examples | not-ready | targeted author runs exist; final full suite not established by this reviewer |
| Rendered outputs | not-ready | pinned HTML/PDF and render QA pending |
| Accessibility | not-ready | visual and interactive checks pending |
| Sources | not-ready | independent source, rights and freshness verification pending |
| Links | not-ready | offline and online checks pending |
| Revision review | not-ready | re-review after any further source or figure changes |
| Handoff | not-ready | bind commit and complete current repository release checks |

- Content gate: pass
- Release readiness: not-ready

## Execution and render evidence

- Transition checks: independent review uses `illustrative` for reader transitions; targeted author execution recorded above, not independently repeated.
- Reader-scale section review: exact source locators and dispositions above, bound to final source SHA and retained prior review.
- Commands actually run: no new commands by the content reviewer for the full example suite; image 07 was visually inspected. Figure generation and targeted runs are author-reported evidence.
- Examples executed: no independent re-run by reviewer; author reports `core-repairs-r`, `extensions-bayes-repairs-r` and prior examples.
- Examples parsed but not executed: illustrative glmmTMB snippet remains unverified in its required runtime.
- Visual QA pages: final HTML/PDF not inspected by content reviewer.
- Offline or unavailable checks: external source, links, accessibility and publication artefacts.
- Reviewer effort: not recorded by independent reviewer.
- Stopping rule: content-depth and scoped repairs only; release gates and full suite delegated separately.

## Pilot learning

- False positives: none recorded.
- Missed issues: initial whole-document review preceded later figure q mismatch; scoped re-review found and verified the correction.
- Procedure changes proposed: none recorded.
- Remaining work: bind source commit, finish #468 build, examples, sources, links, accessibility and render QA.
- Readiness decision: not-ready
- Readiness rationale: content gate passes; release evidence is incomplete.

## Layout-only revision and visual review addendum

The independent reviewer re-reviewed source SHA-256 `634e7a79d25fe4646ac049eab957f61991e2376105e8c8643515334505229df5` to `f6487efe39fa5f66aa97c8a1c401c0b8750b013204ac1af39e0cda72adf29da5` after line-wrapping the NB2 display and two R examples. The source and outputs are committed as `e77fa0721fe4a062e7219aa3e068e00adcc6ab66`. R parse trees for the two affected blocks were compared in pinned R 4.5.3 and were identical; the mathematical terms, captions and figure IDs were unchanged. The earlier whole-document and scoped-review findings are retained at their original hashes, with the affected R05/C16, R06/C17 and R07/C19 paths re-reviewed for these layout changes. This is not a fresh full-source review or an independent re-execution of every example.

The preceding review's historic `634e7a...` hash remains the corrected-figure content snapshot; this addendum binds the current source and supersedes any statement that it is the latest source. The repaired PDF SHA-256 is `8f77bb909dcfc2612607351278ecb956b42308058c2aeb42a23d94497ef5d641`. The independent visual reviewer checked pages 46–47, 53–55 and 64–66 after the repair: the previously clipped equation and code fit on those sampled pages, with no observed overlap. Other earlier sampled pages are evidence at the earlier PDF revision only; this is not a whole-PDF visual pass. The PDF is untagged and no reading-order or tag-tree conformance is claimed.

The actual primary HTML, MathML and MathJax HTML were opened via an isolated headless Chrome DevTools session. A sampled zero-process mathematical viewport was legible in all three; the primary and MathJax variants logged a local `file:///sre/speech-worker.js` worker import error. Speech functionality and HTTP deployment are unverified. The scripted scroll is not ordinary fragment-navigation verification; keyboard navigation, assistive technology, accessibility-tree and screen-reader behaviour remain untested. The visual sample does not verify all maths or all pages. See `.scratch/glm-repairs-2026-11-22/visual-review.md` for exact artifact hashes, prior failed render and screenshot attempts, commands and the review boundary.

## Additional language coverage

The author ran `just examples glm real-cases-python real-cases-julia bayes-count-python bayes-count-julia` in the pinned offline Python and Julia containers; all four added entries passed, as recorded in `.scratch/glm-repairs-2026-11-22/language-coverage-report.md`. The matched real cases reproduce R reference penguin Gaussian/Gamma species means, contrasts and design ranks and the Salamanders GP Poisson predictions. The matched Poisson–Gamma case reproduces a posterior mean, mean-rate credible interval and future-count interval. The independent content reviewer did not rerun these four entries. Synthetic four-family core, fixed-shape NB2 and fixed-penalty spline examples also have R/Python/Julia versions. Estimated-dispersion NB, GLMM, REML GAM, hurdle/zero inflation, multinomial/ordinal and logistic MCMC/hierarchical demonstrations remain R-only; there is no claim of universal feature parity or generic production safety. The final full current manifest has not been verified by this audit record.

Content gate remains **pass** at the scoped independent-review boundary. Release readiness remains **not-ready** until the final repository audit, current example suite, links, source and provenance checks, accessibility limitations, visual evidence and CI are assessed. A passing mechanical check cannot establish the prose judgement.
