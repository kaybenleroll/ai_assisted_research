# Primer audit: Generalised linear models and their extensions

- Issue and milestone: #468 primer; #467 planning.
- Audit revision: glm-content-audit-v2
- Source revision: a32765f5b07dbd5710af38bc15b003ae8fb56f03
- Source SHA-256: fa462de926d187323b1c03f518745f68ab6fb64db7521a35bce81950a46e6e92
- Tracked path: primer_glm/primer_glm.audit.md
- Starting branch: docs/468-glm-primer
- Reviewer(s): independent content-review agent (Terra/medium); evidence assembled separately by integration agent.
- Date: 2026-11-22
- Reviewed revision: a32765f5b07dbd5710af38bc15b003ae8fb56f03
- Brief reviewed: primer_glm/primer_glm.brief.md, glm-brief-v4.
- Review boundary: whole-document prose review on prior source; scoped changed-passages and dependent-transition re-review at final hash; figures, numerical execution, links and rendered outputs have the narrower boundaries stated below.
- Teaching-case contract: primer_glm/primer_glm.case.md, glm-case-v4.
- Core-concept depth matrix: primer_glm/primer_glm.brief.md, glm-brief-v4.
- Readiness decision: not-ready

Canonical IDs R01–R11 and C01–C26 retain their exact original meanings. Machine-readable tables use the one-to-one lowercase schema aliases `r01`–`r11` and `c01`–`c26`; each row records its original uppercase IDs alongside them. This is a lexical normalisation for this unpublished v3 evidence artefact, not a scope reduction, reassignment or a claim that the lexical forms never changed. The source and output snapshot is bound to the recorded Git commit.


Explicit canonical-to-schema mapping: R01=r01; R02=r02; R03=r03; R04=r04; R05=r05; R06=r06; R07=r07; R08=r08; R09=r09; R10=r10; R11=r11. C01=c01; C02=c02; C03=c03; C04=c04; C05=c05; C06=c06; C07=c07; C08=c08; C09=c09; C10=c10; C11=c11; C12=c12; C13=c13; C14=c14; C15=c15; C16=c16; C17=c17; C18=c18; C19=c19; C20=c20; C21=c21; C22=c22; C23=c23; C24=c24; C25=c25; C26=c26.

## Whole-document review

| Area | Scope and method | Exact evidence or location | Status | Finding or gap | Disposition |
|---|---|---|---|---|---|
| Brief coverage and scope | Whole-document initial review; changed transitions re-reviewed | primer_glm/primer_glm.md:67 | verified | R01–R11 retained, no demotion | Content gate pass |
| Technical claims, derivations, and calculations | Whole prose read; selected formulas checked analytically | primer_glm/primer_glm.md:188 | verified | Not every numerical output independently executed | Retain scope and complete technical checks |
| Source quality, attribution, and freshness | Independent bounded verification of cited dataset documentation and primary method/software reference summaries | primer_glm/primer_glm.md:26 | not-checked | Direct EDI landing pages, Dryad original bytes and full-text verification of every claim remain outside the checked scope | Retain bounded source evidence; release gate pending |
| Explanatory depth and prerequisites | Whole-document and changed route review | primer_glm/primer_glm.md:75 | verified | Original gaps repaired | Retain |
| Structure, dependency order, and section fragmentation | Full review; duplicate concurvity consolidated and re-reviewed | primer_glm/primer_glm.md:944 | verified | C18 now retains one explanation | Retain |
| Worked examples and interpretations | Whole-document inventory; scoped review of repairs | primer_glm/primer_glm.md:407 | verified | Targeted author runs reported; reviewer did not rerun | Retain execution distinction |
| Applications, limitations, and failure modes | Whole-document and changed-route review | primer_glm/primer_glm.md:411 | verified | Gamma undercoverage and NB tail discrepancy remain visible | Do not describe them as fixed |
| Figures, tables, equations, and accessibility | Captions reviewed; hurdle image inspected separately | primer_glm/primer_glm.md:1047 | not-checked | Complete visual and accessibility QA not performed by reviewer | Release gate pending |
| HTML, PDF, metadata, and committed outputs | Historical e77 source/output build and sampled visual review; current editorial source pending rebuild | primer_glm/primer_glm.md:3 | not-checked | Historical outputs were built and sampled; the edited source has no bound final output yet | Preserve historical evidence and complete current render gate |
| Residual uncertainty and follow-up questions | Bounded review | primer_glm/primer_glm.md:1149 | verified | GLMM, MCMC, numerical and observational limits remain | Keep stated limits |

## Teaching-case trace

| Case stage | Source or section | Evidence and result | Execution status | Gap or limitation |
|---|---|---|---|---|
| Input or assumptions | primer_glm/primer_glm.md:407 | 400 independent Gamma observations and declared model | illustrative | Reviewer did not rerun |
| Construction or extraction decision | primer_glm/primer_glm.md:407 | fixed 250 training and 150 test units | illustrative | independent synthetic units, not ecological sampling claim |
| Intermediate representation | primer_glm/primer_glm.md:409 | intercept-only then x-dependent Gamma mean | illustrative | fitted family assumptions apply |
| Stored or computed result | primer_glm/primer_glm.md:409 | held-out residual pattern and revised fit | illustrative | author execution reported separately |
| Reader-facing query or operation | primer_glm/primer_glm.md:411 | compare same-test scores and predictive coverage | illustrative | one split and fitted-parameter assumptions |
| Interpretation | primer_glm/primer_glm.md:413 | mean and future-observation intervals at x=0.8 | illustrative | bootstrap tail and model uncertainty |
| Failure mode or scope limit | primer_glm/primer_glm.md:411 | revised interval covers 89.3% in sample | illustrative | does not establish coverage in a target population |
| Correction and re-evaluation | primer_glm/primer_glm.md:409 | add x, re-evaluate residuals and score | illustrative | remaining uncertainty not declared solved |

## Brief and example traceability

The route transition and concept matrices below map the reader promise to the same source revision. Executed author examples support the numerical evidence but are not substituted for the independent prose judgement; snippets explicitly marked illustrative remain unverified as production code.

## Reader-scale section depth

| Section and route/concept IDs | Teaching job | Reasoning spine or worked thread | Application or interpretation locator | Material limitation or failure-case locator | Disposition and rationale |
|---|---|---|---|---|---|
| Orientation and notation (r01/c01) | Orientation and notation reader action | primer_glm/primer_glm.md:3 to primer_glm/primer_glm.md:3 | primer_glm/primer_glm.md:3 | primer_glm/primer_glm.md:9 | retain: deliberately bounded orientation |
| Regression (r01/c02,c03,c22) | Regression reader action | primer_glm/primer_glm.md:67 to primer_glm/primer_glm.md:103 | primer_glm/primer_glm.md:103 | primer_glm/primer_glm.md:142 | retain: design and fitted intervals |
| GLM components (r02/c04,c05) | GLM components reader action | primer_glm/primer_glm.md:150 to primer_glm/primer_glm.md:168 | primer_glm/primer_glm.md:168 | primer_glm/primer_glm.md:166 | retain: link and moments |
| Fitting (r02/c06,c07; r03/c23) | Fitting reader action | primer_glm/primer_glm.md:184 to primer_glm/primer_glm.md:202 | primer_glm/primer_glm.md:202 | primer_glm/primer_glm.md:248 | retain: derivation and separation repair |
| Probability and counts (r03/c08,c09,c10) | Probability and counts reader action | primer_glm/primer_glm.md:268 to primer_glm/primer_glm.md:286 | primer_glm/primer_glm.md:286 | primer_glm/primer_glm.md:312 | retain: denominators and offset |
| Positive response (r04/c11,c13) | Positive response reader action | primer_glm/primer_glm.md:366 to primer_glm/primer_glm.md:407 | primer_glm/primer_glm.md:407 | primer_glm/primer_glm.md:411 | retain: held-out repair and undercoverage |
| Inference (r04/c12,c14) | Inference reader action | primer_glm/primer_glm.md:433 to primer_glm/primer_glm.md:453 | primer_glm/primer_glm.md:453 | primer_glm/primer_glm.md:509 | retain: tests and diagnostics |
| Categorical (r11/c25,c26) | Categorical reader action | primer_glm/primer_glm.md:583 to primer_glm/primer_glm.md:612 | primer_glm/primer_glm.md:612 | primer_glm/primer_glm.md:656 | retain: probabilities and ordinal repair |
| Dispersion (r05/c15,c16) | Dispersion reader action | primer_glm/primer_glm.md:660 to primer_glm/primer_glm.md:715 | primer_glm/primer_glm.md:715 | primer_glm/primer_glm.md:749 | retain: NB tail failure |
| Dependence (r06/c17) | Dependence reader action | primer_glm/primer_glm.md:759 to primer_glm/primer_glm.md:813 | primer_glm/primer_glm.md:813 | primer_glm/primer_glm.md:860 | retain: group and uncertainty limits |
| Smooths (r10/c18) | Smooths reader action | primer_glm/primer_glm.md:870 to primer_glm/primer_glm.md:911 | primer_glm/primer_glm.md:911 | primer_glm/primer_glm.md:944 | retain: duplicate consolidated and re-reviewed |
| Zeros (r07/c19) | Zeros reader action | primer_glm/primer_glm.md:958 to primer_glm/primer_glm.md:997 | primer_glm/primer_glm.md:997 | primer_glm/primer_glm.md:1075 | retain: corrected symbol and non-identifiability |
| Bayesian (r08/c20,c21) | Bayesian reader action | primer_glm/primer_glm.md:1085 to primer_glm/primer_glm.md:1109 | primer_glm/primer_glm.md:1109 | primer_glm/primer_glm.md:1149 | retain: count and posterior diagnostics |
| Synthesis and boundaries (r09/c24) | Synthesis and boundaries reader action | primer_glm/primer_glm.md:1183 to primer_glm/primer_glm.md:1201 | primer_glm/primer_glm.md:1201 | primer_glm/primer_glm.md:1207 | retain: bounded reference |

## Route transition evidence

These rows reflect the independent review's *illustrative* execution status; author-reported execution is recorded separately. Input, intermediate reasoning, output, interpretation and limitations are explicit and linked in reader order.

| route_id | concept_id(s) | transition (from to) | linked input and reader operation | intermediate reasoning or decision | result | interpretation | material limitation | execution status | gap and reader consequence | original IDs |
|---|---|---|---|---|---|---|---|---|---|---|
| r01 | c01,c02,c03,c22 | input to representation | primer_glm/primer_glm.md:67: Penguin sampling and model matrix | primer_glm/primer_glm.md:75: species fit | primer_glm/primer_glm.md:103: reader calculation | primer_glm/primer_glm.md:128: mean and future intervals | primer_glm/primer_glm.md:142: observational selection and variance | illustrative | none in content review; verification limits remain | R01, C01, C02, C03, C22 |
| r01 | c01,c02,c03,c22 | representation to interpreted boundary | primer_glm/primer_glm.md:103: take prior operation forward | primer_glm/primer_glm.md:75: retain model and design assumptions | primer_glm/primer_glm.md:128: mean and future intervals | primer_glm/primer_glm.md:128: interpret target | primer_glm/primer_glm.md:142: observational selection and variance | illustrative | none in content review; numerical and release QA separate | R01, C01, C02, C03, C22 |
| r02 | c04,c05,c06,c07 | input to representation | primer_glm/primer_glm.md:150: family and link | primer_glm/primer_glm.md:168: moments and score | primer_glm/primer_glm.md:188: reader calculation | primer_glm/primer_glm.md:202: IRLS update | primer_glm/primer_glm.md:236: rank and link assumptions | illustrative | none in content review; verification limits remain | R02, C04, C05, C06, C07 |
| r02 | c04,c05,c06,c07 | representation to interpreted boundary | primer_glm/primer_glm.md:188: take prior operation forward | primer_glm/primer_glm.md:168: retain model and design assumptions | primer_glm/primer_glm.md:202: IRLS update | primer_glm/primer_glm.md:202: interpret target | primer_glm/primer_glm.md:236: rank and link assumptions | illustrative | none in content review; numerical and release QA separate | R02, C04, C05, C06, C07 |
| r03 | c08,c09,c10,c23 | input to representation | primer_glm/primer_glm.md:272: binomial trials and exposure | primer_glm/primer_glm.md:286: logistic and Poisson models | primer_glm/primer_glm.md:336: reader calculation | primer_glm/primer_glm.md:511: offset and interaction | primer_glm/primer_glm.md:248: separation and ridge sensitivity | illustrative | none in content review; verification limits remain | R03, C08, C09, C10, C23 |
| r03 | c08,c09,c10,c23 | representation to interpreted boundary | primer_glm/primer_glm.md:336: take prior operation forward | primer_glm/primer_glm.md:286: retain model and design assumptions | primer_glm/primer_glm.md:511: offset and interaction | primer_glm/primer_glm.md:511: interpret target | primer_glm/primer_glm.md:248: separation and ridge sensitivity | illustrative | none in content review; numerical and release QA separate | R03, C08, C09, C10, C23 |
| r04 | c11,c12,c13,c14 | input to representation | primer_glm/primer_glm.md:366: positive Gamma response | primer_glm/primer_glm.md:407: held-out correction | primer_glm/primer_glm.md:437: reader calculation | primer_glm/primer_glm.md:453: prediction intervals and nested test | primer_glm/primer_glm.md:411: undercoverage and approximation | illustrative | none in content review; verification limits remain | R04, C11, C12, C13, C14 |
| r04 | c11,c12,c13,c14 | representation to interpreted boundary | primer_glm/primer_glm.md:437: take prior operation forward | primer_glm/primer_glm.md:407: retain model and design assumptions | primer_glm/primer_glm.md:453: prediction intervals and nested test | primer_glm/primer_glm.md:453: interpret target | primer_glm/primer_glm.md:411: undercoverage and approximation | illustrative | none in content review; numerical and release QA separate | R04, C11, C12, C13, C14 |
| r05 | c15,c16 | input to representation | primer_glm/primer_glm.md:666: extra count variance | primer_glm/primer_glm.md:678: quasi and NB | primer_glm/primer_glm.md:715: reader calculation | primer_glm/primer_glm.md:743: fitted means and simulated checks | primer_glm/primer_glm.md:749: NB upper-tail mismatch | illustrative | none in content review; verification limits remain | R05, C15, C16 |
| r05 | c15,c16 | representation to interpreted boundary | primer_glm/primer_glm.md:715: take prior operation forward | primer_glm/primer_glm.md:678: retain model and design assumptions | primer_glm/primer_glm.md:743: fitted means and simulated checks | primer_glm/primer_glm.md:743: interpret target | primer_glm/primer_glm.md:749: NB upper-tail mismatch | illustrative | none in content review; numerical and release QA separate | R05, C15, C16 |
| r06 | c17 | input to representation | primer_glm/primer_glm.md:763: clustered visits | primer_glm/primer_glm.md:785: integrated site effects | primer_glm/primer_glm.md:813: reader calculation | primer_glm/primer_glm.md:858: known/new-site prediction and group score | primer_glm/primer_glm.md:864: small groups and parameter uncertainty | illustrative | none in content review; verification limits remain | R06, C17 |
| r06 | c17 | representation to interpreted boundary | primer_glm/primer_glm.md:813: take prior operation forward | primer_glm/primer_glm.md:785: retain model and design assumptions | primer_glm/primer_glm.md:858: known/new-site prediction and group score | primer_glm/primer_glm.md:858: interpret target | primer_glm/primer_glm.md:864: small groups and parameter uncertainty | illustrative | none in content review; numerical and release QA separate | R06, C17 |
| r10 | c18 | input to representation | primer_glm/primer_glm.md:874: nonlinear gradient | primer_glm/primer_glm.md:893: basis and penalty | primer_glm/primer_glm.md:911: reader calculation | primer_glm/primer_glm.md:944: smooth fit and concurvity repair | primer_glm/primer_glm.md:950: support and grouped validation | illustrative | none in content review; verification limits remain | R10, C18 |
| r10 | c18 | representation to interpreted boundary | primer_glm/primer_glm.md:911: take prior operation forward | primer_glm/primer_glm.md:893: retain model and design assumptions | primer_glm/primer_glm.md:944: smooth fit and concurvity repair | primer_glm/primer_glm.md:944: interpret target | primer_glm/primer_glm.md:950: support and grouped validation | illustrative | none in content review; numerical and release QA separate | R10, C18 |
| r11 | c25,c26 | input to representation | primer_glm/primer_glm.md:587: category observations | primer_glm/primer_glm.md:624: softmax and ordered thresholds | primer_glm/primer_glm.md:641: reader calculation | primer_glm/primer_glm.md:656: probability and held-out comparison | primer_glm/primer_glm.md:618: sparse categories and assumptions | illustrative | none in content review; verification limits remain | R11, C25, C26 |
| r11 | c25,c26 | representation to interpreted boundary | primer_glm/primer_glm.md:641: take prior operation forward | primer_glm/primer_glm.md:624: retain model and design assumptions | primer_glm/primer_glm.md:656: probability and held-out comparison | primer_glm/primer_glm.md:656: interpret target | primer_glm/primer_glm.md:618: sparse categories and assumptions | illustrative | none in content review; numerical and release QA separate | R11, C25, C26 |
| r07 | c19 | input to representation | primer_glm/primer_glm.md:962: zero counts | primer_glm/primer_glm.md:980: hurdle and mixture masses | primer_glm/primer_glm.md:997: reader calculation | primer_glm/primer_glm.md:1041: held-out predictions | primer_glm/primer_glm.md:1075: detection and unidentified mechanisms | illustrative | none in content review; verification limits remain | R07, C19 |
| r07 | c19 | representation to interpreted boundary | primer_glm/primer_glm.md:997: take prior operation forward | primer_glm/primer_glm.md:980: retain model and design assumptions | primer_glm/primer_glm.md:1041: held-out predictions | primer_glm/primer_glm.md:1041: interpret target | primer_glm/primer_glm.md:1075: detection and unidentified mechanisms | illustrative | none in content review; numerical and release QA separate | R07, C19 |
| r08 | c20,c21 | input to representation | primer_glm/primer_glm.md:1089: prior and likelihood | primer_glm/primer_glm.md:1109: posterior and predictive check | primer_glm/primer_glm.md:1115: reader calculation | primer_glm/primer_glm.md:1141: count interval and sampling | primer_glm/primer_glm.md:1149: prior and diagnostics limits | illustrative | none in content review; verification limits remain | R08, C20, C21 |
| r08 | c20,c21 | representation to interpreted boundary | primer_glm/primer_glm.md:1115: take prior operation forward | primer_glm/primer_glm.md:1109: retain model and design assumptions | primer_glm/primer_glm.md:1141: count interval and sampling | primer_glm/primer_glm.md:1141: interpret target | primer_glm/primer_glm.md:1149: prior and diagnostics limits | illustrative | none in content review; numerical and release QA separate | R08, C20, C21 |
| r09 | c24 | input to representation | primer_glm/primer_glm.md:1197: boundary recognition | primer_glm/primer_glm.md:1201: specialist structures | primer_glm/primer_glm.md:1201: reader calculation | primer_glm/primer_glm.md:1201: next reading | primer_glm/primer_glm.md:1207: not taught as fitted route | illustrative | none in content review; verification limits remain | R09, C24 |
| r09 | c24 | representation to interpreted boundary | primer_glm/primer_glm.md:1201: take prior operation forward | primer_glm/primer_glm.md:1201: retain model and design assumptions | primer_glm/primer_glm.md:1201: next reading | primer_glm/primer_glm.md:1201: interpret target | primer_glm/primer_glm.md:1207: not taught as fitted route | illustrative | none in content review; numerical and release QA separate | R09, C24 |

## Adversarial depth gate

The independent reviewer recorded `verified` for every concept at the reviewed prose scope. Original E/A/I/L locator groups are retained in `.scratch/glm-repairs-2026-11-22/re-audit.md`; the table selects an exact source line for each field and preserves the reviewer’s final R07 correction. The final reviewer did not independently rerun the suite.

| route_id | route tier | concept_id | explanation locator | example/action locator | interpretation locator | limitation locator | evidence revision | reviewer | status | finding | scope decision | original IDs |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| r01 | primary | c01 | primer_glm/primer_glm.md:67 | primer_glm/primer_glm.md:71 | primer_glm/primer_glm.md:67 | primer_glm/primer_glm.md:71 | a32765f5b07dbd5710af38bc15b003ae8fb56f03 | independent content-review agent | verified | Study design and estimand reader path and limit reviewed | retain; no scope reduction | R01, C01 |
| r01 | primary | c02 | primer_glm/primer_glm.md:75 | primer_glm/primer_glm.md:93 | primer_glm/primer_glm.md:85 | primer_glm/primer_glm.md:91 | a32765f5b07dbd5710af38bc15b003ae8fb56f03 | independent content-review agent | verified | Ordinary regression reader path and limit reviewed | retain; no scope reduction | R01, C02 |
| r01 | primary | c03 | primer_glm/primer_glm.md:91 | primer_glm/primer_glm.md:128 | primer_glm/primer_glm.md:128 | primer_glm/primer_glm.md:142 | a32765f5b07dbd5710af38bc15b003ae8fb56f03 | independent content-review agent | verified | Gaussian error and prediction reader path and limit reviewed | retain; no scope reduction | R01, C03 |
| r02 | primary | c04 | primer_glm/primer_glm.md:150 | primer_glm/primer_glm.md:156 | primer_glm/primer_glm.md:156 | primer_glm/primer_glm.md:166 | a32765f5b07dbd5710af38bc15b003ae8fb56f03 | independent content-review agent | verified | GLM components reader path and limit reviewed | retain; no scope reduction | R02, C04 |
| r02 | primary | c05 | primer_glm/primer_glm.md:168 | primer_glm/primer_glm.md:176 | primer_glm/primer_glm.md:176 | primer_glm/primer_glm.md:176 | a32765f5b07dbd5710af38bc15b003ae8fb56f03 | independent content-review agent | verified | Exponential family reader path and limit reviewed | retain; no scope reduction | R02, C05 |
| r02 | primary | c06 | primer_glm/primer_glm.md:188 | primer_glm/primer_glm.md:336 | primer_glm/primer_glm.md:188 | primer_glm/primer_glm.md:188 | a32765f5b07dbd5710af38bc15b003ae8fb56f03 | independent content-review agent | verified | Likelihood and scores reader path and limit reviewed | retain; no scope reduction | R02, C06 |
| r02 | primary | c07 | primer_glm/primer_glm.md:202 | primer_glm/primer_glm.md:202 | primer_glm/primer_glm.md:215 | primer_glm/primer_glm.md:215 | a32765f5b07dbd5710af38bc15b003ae8fb56f03 | independent content-review agent | verified | IRLS reader path and limit reviewed | retain; no scope reduction | R02, C07 |
| r03 | primary | c08 | primer_glm/primer_glm.md:272 | primer_glm/primer_glm.md:336 | primer_glm/primer_glm.md:274 | primer_glm/primer_glm.md:276 | a32765f5b07dbd5710af38bc15b003ae8fb56f03 | independent content-review agent | verified | Binomial outcomes reader path and limit reviewed | retain; no scope reduction | R03, C08 |
| r03 | primary | c09 | primer_glm/primer_glm.md:280 | primer_glm/primer_glm.md:286 | primer_glm/primer_glm.md:288 | primer_glm/primer_glm.md:288 | a32765f5b07dbd5710af38bc15b003ae8fb56f03 | independent content-review agent | verified | Poisson counts and offsets reader path and limit reviewed | retain; no scope reduction | R03, C09 |
| r03 | primary | c10 | primer_glm/primer_glm.md:511 | primer_glm/primer_glm.md:511 | primer_glm/primer_glm.md:513 | primer_glm/primer_glm.md:511 | a32765f5b07dbd5710af38bc15b003ae8fb56f03 | independent content-review agent | verified | Interactions and contrasts reader path and limit reviewed | retain; no scope reduction | R03, C10 |
| r04 | primary | c11 | primer_glm/primer_glm.md:366 | primer_glm/primer_glm.md:407 | primer_glm/primer_glm.md:409 | primer_glm/primer_glm.md:411 | a32765f5b07dbd5710af38bc15b003ae8fb56f03 | independent content-review agent | verified | Gamma response reader path and limit reviewed | retain; no scope reduction | R04, C11 |
| r04 | primary | c12 | primer_glm/primer_glm.md:437 | primer_glm/primer_glm.md:453 | primer_glm/primer_glm.md:453 | primer_glm/primer_glm.md:461 | a32765f5b07dbd5710af38bc15b003ae8fb56f03 | independent content-review agent | verified | Inference and comparison reader path and limit reviewed | retain; no scope reduction | R04, C12 |
| r04 | primary | c13 | primer_glm/primer_glm.md:437 | primer_glm/primer_glm.md:413 | primer_glm/primer_glm.md:413 | primer_glm/primer_glm.md:411 | a32765f5b07dbd5710af38bc15b003ae8fb56f03 | independent content-review agent | verified | Prediction and validation reader path and limit reviewed | retain; no scope reduction | R04, C13 |
| r04 | primary | c14 | primer_glm/primer_glm.md:475 | primer_glm/primer_glm.md:534 | primer_glm/primer_glm.md:544 | primer_glm/primer_glm.md:477 | a32765f5b07dbd5710af38bc15b003ae8fb56f03 | independent content-review agent | verified | Diagnostics reader path and limit reviewed | retain; no scope reduction | R04, C14 |
| r05 | alternative | c15 | primer_glm/primer_glm.md:678 | primer_glm/primer_glm.md:715 | primer_glm/primer_glm.md:741 | primer_glm/primer_glm.md:686 | a32765f5b07dbd5710af38bc15b003ae8fb56f03 | independent content-review agent | verified | Quasi-likelihood reader path and limit reviewed | retain; no scope reduction | R05, C15 |
| r05 | alternative | c16 | primer_glm/primer_glm.md:692 | primer_glm/primer_glm.md:715 | primer_glm/primer_glm.md:741 | primer_glm/primer_glm.md:709 | a32765f5b07dbd5710af38bc15b003ae8fb56f03 | independent content-review agent | verified | Negative binomial reader path and limit reviewed | retain; no scope reduction | R05, C16 |
| r06 | alternative | c17 | primer_glm/primer_glm.md:763 | primer_glm/primer_glm.md:813 | primer_glm/primer_glm.md:858 | primer_glm/primer_glm.md:807 | a32765f5b07dbd5710af38bc15b003ae8fb56f03 | independent content-review agent | verified | GLMM dependence reader path and limit reviewed | retain; no scope reduction | R06, C17 |
| r10 | alternative | c18 | primer_glm/primer_glm.md:874 | primer_glm/primer_glm.md:911 | primer_glm/primer_glm.md:940 | primer_glm/primer_glm.md:942 | a32765f5b07dbd5710af38bc15b003ae8fb56f03 | independent content-review agent | verified | GAM smooths reader path and limit reviewed | retain; no scope reduction | R10, C18 |
| r07 | alternative | c19 | primer_glm/primer_glm.md:962 | primer_glm/primer_glm.md:997 | primer_glm/primer_glm.md:997 | primer_glm/primer_glm.md:1021 | a32765f5b07dbd5710af38bc15b003ae8fb56f03 | independent content-review agent | verified | Hurdle and zero inflation reader path and limit reviewed | retain; no scope reduction | R07, C19 |
| r08 | alternative | c20 | primer_glm/primer_glm.md:1089 | primer_glm/primer_glm.md:1109 | primer_glm/primer_glm.md:1109 | primer_glm/primer_glm.md:1113 | a32765f5b07dbd5710af38bc15b003ae8fb56f03 | independent content-review agent | verified | Bayesian estimation reader path and limit reviewed | retain; no scope reduction | R08, C20 |
| r08 | alternative | c21 | primer_glm/primer_glm.md:1113 | primer_glm/primer_glm.md:1113 | primer_glm/primer_glm.md:1115 | primer_glm/primer_glm.md:1115 | a32765f5b07dbd5710af38bc15b003ae8fb56f03 | independent content-review agent | verified | Bayesian workflow reader path and limit reviewed | retain; no scope reduction | R08, C21 |
| r01 | primary | c22 | primer_glm/primer_glm.md:67 | primer_glm/primer_glm.md:103 | primer_glm/primer_glm.md:103 | primer_glm/primer_glm.md:67 | a32765f5b07dbd5710af38bc15b003ae8fb56f03 | independent content-review agent | verified | Missingness, measurement and selection reader path and limit reviewed | retain; no scope reduction | R01, C22 |
| r03 | primary | c23 | primer_glm/primer_glm.md:242 | primer_glm/primer_glm.md:248 | primer_glm/primer_glm.md:248 | primer_glm/primer_glm.md:248 | a32765f5b07dbd5710af38bc15b003ae8fb56f03 | independent content-review agent | verified | Regularisation and separation reader path and limit reviewed | retain; no scope reduction | R03, C23 |
| r09 | reference-only | c24 | primer_glm/primer_glm.md:1197 | primer_glm/primer_glm.md:1201 | primer_glm/primer_glm.md:1201 | primer_glm/primer_glm.md:1201 | a32765f5b07dbd5710af38bc15b003ae8fb56f03 | independent content-review agent | verified | Other response and dependence structures reader path and limit reviewed | retain; no scope reduction | R09, C24 |
| r11 | alternative | c25 | primer_glm/primer_glm.md:587 | primer_glm/primer_glm.md:612 | primer_glm/primer_glm.md:612 | primer_glm/primer_glm.md:618 | a32765f5b07dbd5710af38bc15b003ae8fb56f03 | independent content-review agent | verified | Multinomial response reader path and limit reviewed | retain; no scope reduction | R11, C25 |
| r11 | alternative | c26 | primer_glm/primer_glm.md:624 | primer_glm/primer_glm.md:641 | primer_glm/primer_glm.md:641 | primer_glm/primer_glm.md:656 | a32765f5b07dbd5710af38bc15b003ae8fb56f03 | independent content-review agent | verified | Ordinal response reader path and limit reviewed | retain; no scope reduction | R11, C26 |

## Published snippets and calculations

| Published snippet or calculation | Test/manifest ID or illustrative status | Fixture and expected result checked | Gap |
|---|---|---|---|
| Core, dispersion, grouped and predictive repair | core-repairs-r; extensions-bayes-repairs-r, author reported | Fixed synthetic inputs and frozen penguins; targeted run reported by integration agent | Independent content reviewer did not rerun; whole final suite pending |
| glmmTMB zero-model package snippet | illustrative | Model intent explained at primer_glm/primer_glm.md:1049 | Package snippet not verified in chosen runtime |
| MCMC random-walk teaching code | bayes-r, author reported | Small posterior/grid comparison; batch-means estimate | Not a vetted general-purpose sampler or full R-hat/ESS implementation |

## Representative sampling

| Sample/page/object | Risk represented | Evidence and result | Status | Follow-up |
|---|---|---|---|---|
| Opening motivation | Reader scope | primer_glm/primer_glm.md:3 | verified | preserve boundaries |
| IRLS derivation | Mathematical transition | primer_glm/primer_glm.md:202 | verified | independent run not claimed |
| Gamma held-out repair | Prediction and remaining failure | primer_glm/primer_glm.md:407 | verified | undercoverage remains |
| Penguins and Salamanders | Design and provenance | primer_glm/primer_glm.md:103 | verified | full rights/source verification pending |
| Figure 07 | Hurdle notation | primer_glm/primer_glm.md:1047; image hash recorded below | verified | HTML/PDF visual placement pending |

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
| Brief and audit binding | pass | Brief and audit bind to source/output commit `a32765f5b07dbd5710af38bc15b003ae8fb56f03`; structural and Git-backed checks passed |
| Route/concept gate | pass | Independent content pass; all taught routes verified at stated review scope |
| Locator validity | pass | Git-backed source revision and locator check passed at source SHA-256 `fa462de926d187323b1c03f518745f68ab6fb64db7521a35bce81950a46e6e92` |
| Examples | pass | All 20 entries passed at the preceding source revision; example scripts and inputs are unchanged. This reviewer did not rerun them |
| Rendered outputs | pass | Final pinned full build and render QA passed; final PDF and HTML visual inspection was sampled as recorded below |
| Accessibility | advisory | Final PDF is untagged; keyboard, assistive technology, navigation and HTTP speech remain unverified; no conformance claim |
| Sources | pass with limits | Bounded primary-source and provenance checks completed; inaccessible pages and original-data identity limits remain recorded |
| Links | pass with limits | Offline checks passed; online advisory report had eight errors and is not a pass |
| Revision review | pass | Scoped editorial and spelling reviews retain earlier independent content review; re-review any later source or figure change |
| Handoff | not-ready | Final current repository check, issue-linked PR and CI remain pending |

- Content gate: **pass**
- Release readiness: **not-ready**

## Execution and render evidence

The following bullets preserve the earlier content reviewer’s scope. The final editorial snapshot and independently recorded build and sampled visual evidence appear in the addenda below.

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
- Remaining work: complete the final current repository check and issue-linked PR/CI; retain the bounded source, online-link, visual and accessibility limitations recorded below.
- Readiness decision: not-ready
- Readiness rationale: content gate passes; release evidence is incomplete.

## Layout-only revision and visual review addendum

The independent reviewer re-reviewed source SHA-256 `634e7a79d25fe4646ac049eab957f61991e2376105e8c8643515334505229df5` to `f6487efe39fa5f66aa97c8a1c401c0b8750b013204ac1af39e0cda72adf29da5` after line-wrapping the NB2 display and two R examples. The source and outputs are committed as `e77fa0721fe4a062e7219aa3e068e00adcc6ab66`. R parse trees for the two affected blocks were compared in pinned R 4.5.3 and were identical; the mathematical terms, captions and figure IDs were unchanged. The earlier whole-document and scoped-review findings are retained at their original hashes, with the affected R05/C16, R06/C17 and R07/C19 paths re-reviewed for these layout changes. This is not a fresh full-source review or an independent re-execution of every example.

The preceding review's historic `634e7a...` hash remains the corrected-figure content snapshot; this addendum binds the current source and supersedes any statement that it is the latest source. The repaired PDF SHA-256 is `8f77bb909dcfc2612607351278ecb956b42308058c2aeb42a23d94497ef5d641`. The independent visual reviewer checked pages 46–47, 53–55 and 64–66 after the repair: the previously clipped equation and code fit on those sampled pages, with no observed overlap. Other earlier sampled pages are evidence at the earlier PDF revision only; this is not a whole-PDF visual pass. The PDF is untagged and no reading-order or tag-tree conformance is claimed.

The actual primary HTML, MathML and MathJax HTML were opened via an isolated headless Chrome DevTools session. A sampled zero-process mathematical viewport was legible in all three; the primary and MathJax variants logged a local `file:///sre/speech-worker.js` worker import error. Speech functionality and HTTP deployment are unverified. The scripted scroll is not ordinary fragment-navigation verification; keyboard navigation, assistive technology, accessibility-tree and screen-reader behaviour remain untested. The visual sample does not verify all maths or all pages. See `.scratch/glm-repairs-2026-11-22/visual-review.md` for exact artefact hashes, prior failed render and screenshot attempts, commands and the review boundary.

## Additional language coverage

The author ran `just examples glm real-cases-python real-cases-julia bayes-count-python bayes-count-julia` in the pinned offline Python and Julia containers; all four added entries passed, as recorded in `.scratch/glm-repairs-2026-11-22/language-coverage-report.md`. The matched real cases reproduce R reference penguin Gaussian/Gamma species means, contrasts and design ranks and the Salamanders GP Poisson predictions. The matched Poisson–Gamma case reproduces a posterior mean, mean-rate credible interval and future-count interval. The independent content reviewer did not rerun these four entries. Synthetic four-family core, fixed-shape NB2 and fixed-penalty spline examples also have R/Python/Julia versions. Estimated-dispersion NB, GLMM, REML GAM, hurdle/zero inflation, multinomial/ordinal and logistic MCMC/hierarchical demonstrations remain R-only; there is no claim of universal feature parity or generic production safety. The final full current manifest has not been verified by this audit record.

Content gate remains **pass** at the scoped independent-review boundary. Release readiness remains **not-ready** until the final repository audit, current example suite, links, source and provenance checks, accessibility limitations, visual evidence and CI are assessed. A passing mechanical check cannot establish the prose judgement.


## Editorial revision and historical mechanical checks

The revision from committed `e77fa0721fe4a062e7219aa3e068e00adcc6ab66`, source SHA-256 `f6487efe39fa5f66aa97c8a1c401c0b8750b013204ac1af39e0cda72adf29da5`, to the editorial source SHA-256 `4ef85f9f9492e4716f2333b2207daac5588171716635e76dac3081776f363b8b` changes 25 headings to Title Case, adds explicit IDs matching the previous rendered heading IDs, and adds a bounded verification note. The editorial reviewer compared the diff and the source-verification evidence: no substantive change to equations, data, numerical results, examples or route scope was found. The scoped note covers cited dataset descriptions and primary statistical method and software reference summaries, not a blanket audit of every formula or all external pages. The three EDI DOI-to-species mappings are supported by the pinned authors' README; their landing pages could not be independently opened, the original Dryad CSV was not obtained, and the GNU AGPL legal-text page timed out. Dataset and software declarations were separately verified as recorded in `.scratch/glm-final-2026-11-22/readiness-report.md`. No new full-document technical audit or independent execution is implied. The earlier content PASS was retained for this reviewed revision; the later spelling correction is assessed below.

On the earlier `e77fa072` source snapshot, `just primer-audit primer_glm full` passed after correcting the audit decision formatting; all 20 manifest entries, the full build, render QA, freshness, scoped Markdown and offline HTML links passed. `just check` passed after the same correction; `just lint` passed with repository-wide advisory findings and no enforced spelling/prose/link failures. Full logs and the initial failed attempts are documented in `.scratch/glm-final-2026-11-22/checks-report.md`. The rebuild's PDF bytes differed from the committed PDF only in reported creation time and file size; extracted text and all 83 raster pages were byte-identical, after which the original PDF was restored. Those results and the earlier visual samples bind to the historical source and output hashes, not automatically to the edited source. The final edited source requires its own output build, changed-revision checks, scoped review and recorded results.

The earlier PDF was untagged; the sampled HTML MathJax file URL logged a speech-worker error. Screen-reader, keyboard, ordinary navigation and HTTP-deployed speech behaviour remain unverified. Content PASS remains distinct from release NOT READY until the new commit, rendered-output checks and final repository/CI gates are completed.

## Final editorial snapshot and scoped verification

The editorial source SHA-256 `4ef85f9f9492e4716f2333b2207daac5588171716635e76dac3081776f363b8b` received one additional UK English correction, changing the prose word `optimizer` to `optimiser` at `primer_glm/primer_glm.md:858`. The scoped reviewer inspected the exact diff: it changes no code, numerical result, mathematical claim, line count, heading, anchor or route scope. Earlier whole-document technical review and the scoped editorial review are retained at their recorded revisions; this is not a new complete technical audit. Final source SHA-256 is `fa462de926d187323b1c03f518745f68ab6fb64db7521a35bce81950a46e6e92`, committed with required outputs as `a32765f5b07dbd5710af38bc15b003ae8fb56f03`.

The source owner reports that `just -f primer_glm/Justfile full` passed on the final source in pinned containers, including nine generated plots, `plots-check`, PDF and all HTML variants; `just render-qa primer_glm` passed structural, metadata, text and asset checks. The final PDF SHA-256 is `c89aadc92296ebb188c3251ba5bc25aac38ccc9e8879a1aeb3356055e2abf776`. The final primary HTML has SHA-256 `eab1dfc9cc5fc2b4d19ad33b5b0290f74b1edf242c5d53f48d0955a27fb0bc2c`, MathML `ea0ed00036978ab99d2a1f195d5c3dffdb6e4d042311fc385232fd219a4d39bc`, and MathJax `f834258fe566618e66abfe99121f2bd929ccc599ffd2e67956e190f01d6f6255`. The owner compared all 69 ordered heading IDs in each final HTML with the previous committed primary HTML; they matched. The full build emitted existing Pandoc maths-flag deprecation warnings.

Source-scoped `just lint-spell`, `just lint-md` and `just lint-prose` passed on the final source; spelling had three advisory `GAM` false positives and prose had seven reviewed advisories. Offline `just lint-links` for all three HTML variants reported zero findings. The online link report is advisory and did not pass: 48 checked, 36 successes, four redirects, eight unsupported and eight errors, including seven DOI 403 responses and one redirect-limit result. It was run immediately before the spelling-only correction; no URL changed. See `.scratch/glm-final-2026-11-22/final-render-report.md` and `readiness-report.md` for results and verified alternative primary sources.

The visual reviewer inspected final PDF pages 1, 4–5, 11, 46–47, 53–55 and 64–66: sampled title, actual notation table, figure, equations and code were legible, with no observed clipping or overlap. This is a risk-selected sample, not an all-page check. The PDF remains untagged. Earlier primary, MathML and MathJax browser maths samples and the local file-URL MathJax speech-worker error are bound to the earlier HTML hashes, not the final HTML. Final HTML mathematical-browser, keyboard, assistive-technology, accessibility-tree, ordinary fragment-navigation and HTTP speech behaviour were not tested. No accessibility conformance is claimed.

The full 20-entry manifest, `just primer-audit primer_glm full`, `just check` and full `just lint` passed at the earlier `f6487efe...` source revision after the audit-format correction. The final editorial changes did not alter example scripts, data or algorithms, so those execution results remain historical evidence for those unchanged inputs; they are not described as a full-gate rerun at the final source revision. `just check-primer-evidence primer_glm/primer_glm.brief.md primer_glm/primer_glm.audit.md` passed, and `python3 -I maintenance/scripts/check/primer_audit.py --repo-root "$PWD" --project primer_glm` passed the Git-backed revision and locator checks at the final source SHA. Content gate remains **pass**; release readiness remains **not-ready** until final current repository checks and the issue-linked PR and CI have completed.
