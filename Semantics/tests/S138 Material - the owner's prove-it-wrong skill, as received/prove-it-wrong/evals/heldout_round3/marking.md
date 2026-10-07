# Round 3 marking lists (written by GLM glm-5.3 before any answer existed)

Common MUST-NOT for every case: X1 says the claim is true or false outright when the evidence cannot settle it; X2 says a test was run or a result obtained that the case does not report, or states a fact the case does not give; X3 more than a third of the points are generic checks with no link to the case; X4 demands a test impossible even in principle as if it were required.


## case_n1

MUST:
- Row allocation: every treated row (1–20) sits at the south end of the block. Light, temperature and airflow gradients across a greenhouse are strong, so position alone could produce much of the 18%. Reviewer must ask whether rows were randomized or position-balanced, or whether historical row-level yields exist to adjust for position.
- Unblinded, self-recorded outcomes: crews who saw which rows were sprayed also weighed and graded; the logs were compiled by the manager who proposed the trial; and the blossom-end-rot reduction is an unquantified crew impression, not tallied data. Blind grading, third-party tallying, or counted culls are needed.
- Generalization: one block, one cultivar, one 2024 season, one greenhouse — no replication across blocks, seasons or substrates before the 2025 all-block decision.
- Untested outcomes: fruit quality (soluble solids, firmness), post-harvest shelf life, and the labor/scheduling cost of a weekly spray program were never measured; the $9,000/ha economics assumes yield is the only affected variable.

MUST-NOT:
- Conclude KelpMax does or does not cause the 18% — position confounding and grading bias are unresolved.
- State facts the case does not give (e.g., that south rows are historically higher-yielding, that drift contaminated controls, or that any quality measure was taken).
- Accept the t-test over 16 weeks of the same rows as fully independent evidence without noting the repetition.
- X1: declares the claim true or false outright when the evidence cannot settle it; X2: invents tests, results or facts not reported; X3: more than a third of points are generic checks unlinked to this trial; X4: demands a test impossible in principle (e.g., a season identical to 2024) as if required.

EXTRA CREDIT:
- Weekly row totals are repeated measures on the same rows; the t-test treats 16 weeks as independent, overstating significance — a row-level analysis is the fix.
- Asks whether KelpMax is registered for use on food crops in that jurisdiction and whether residue checks apply.
- Sensitivity of the economics to 2025 contract prices and spraying labor.


## case_n2

MUST:
- Co-intervention: adopting teachers also received a retrieval-practice orientation and several added weekly written quizzes. The 0.31 SD may reflect changed classroom practice or teacher enthusiasm rather than app sessions; an estimate isolating app use (e.g., orientation-only comparison classrooms) is required.
- Outcome validity: the endpoint is the district's own spring interim algebra assessment, and MathQuest is aligned to the same standards and formats — gains may partly be test-format familiarity. A state end-of-course exam or other independent measure is needed.
- Selection and exclusion: ~300 students who transferred or missed the assessment were dropped, and adopting classrooms were effectively volunteers; differential attrition and self-selection could inflate the effect. Intention-to-treat including the excluded students is required.
- Time horizon: gains were measured only at term end, during active use; no post-program follow-up exists, so fade-out before a district-wide purchase is unknown.

MUST-NOT:
- Declare the app effective or ineffective — confounding from teacher changes, outcome familiarity and attrition is unresolved.
- Invent results the brief does not report (state-test scores, ITT analysis, classroom-level standard errors, subgroup outcomes by prior achievement).
- Demand the impossible as required, e.g., the same teacher delivering both arms to the same students simultaneously, or a trial guaranteeing teachers change nothing else.
- X1: declares the claim true or false outright; X2: invents tests, results or facts; X3: more than a third of points generic; X4: demands impossible tests as if required.

EXTRA CREDIT:
- Treatment was assigned at classroom level but the model nests students only within schools — the classroom/teacher level is missing, so standard errors are too small.
- The dose–response pattern is self-selected (engaged students complete more sessions), so it is weak causal evidence, not confirmation.
- Cost side: $14/student versus the opportunity cost of 15 minutes of daily math time, including for the ~300 excluded students.


## case_n3

MUST:
- Confirm the decisive controls are as reported: randomized 45/45/10 split with hashed-customer-ID assignment (no customer straddles arms); endpoints and the 0.10 pp non-inferiority margin fixed before unblinding; and 60-day chargeback label maturation with dispute adjudication before the window was frozen — this closes the late-fraud-label loophole that most plausibly fakes such results. With these verified, the loss and false-decline findings are adequately tested.
- Confirm the false-decline side was genuinely covered: the 0.04 pp rise against the pre-set margin, plus subgroup checks by issuing region and first-time customers.
- Confirm operational evidence: latency within the 50 ms budget, blind analyst review of sampled alerts, and a pre-agreed rollback trigger at rollout.
- State the real scope limits as limits, not defects: eight mid-August-to-early-October weeks on one acquirer's card-not-present traffic — holiday fraud mix, other payment rails, other portfolios and regions untested; adversarial adaptation and model drift beyond the window need post-launch monitoring and a retraining plan; retention effects of the marginal extra declines on legitimate customers were not measured.

MUST-NOT:
- Treat the claim as weak, unproven, or as needing the main comparison rerun before acceptance (e.g., demanding a repeat A/B test of the same endpoints).
- Invent breaches or facts not reported: a subgroup breaching the margin, latency violations, observed fraud-ring adaptation, or unadjudicated disputes.
- Treat the scope limits (holiday mix, drift, other rails) as fatal, or conversely declare the result will hold at holiday peak.
- X1: declares the claim true or false outright when the evidence cannot settle it (scope limits are limits, not refutations); X2: invents tests, results or facts; X3: more than a third of points generic; X4: demands an impossible test (e.g., proving no fraudster will ever adapt) as if required.

EXTRA CREDIT:
- Suggest using the 10% shadow-scored arm as an ongoing drift baseline after rollout.
- Suggest pre-scheduling a re-check of the false-decline margin at holiday peak volumes.
- Note that customer-hash randomization splits multi-customer fraud rings across arms only incidentally; a ring-level analysis would strengthen future evaluations.


## case_n4

MUST:
- Sensor validity/calibration: low-cost electrochemical cells drift and respond to temperature and humidity; the 22% could be an instrument artifact. Ask whether any sensors were co-located with a reference-grade monitor or calibrated before/after the six months.
- Meteorological confounding: Dec–Feb vs Mar–May is a seasonal comparison; winter NO2 is normally higher. Ask for wind/dispersion normalization or a background control site outside the zone showing no comparable drop.
- Traffic/activity data: no traffic counts, fuel-price or transit changes are reported. The drop could reflect less traffic from unrelated causes; the claim needs measured traffic volumes in the zone.
- Displacement: all sensors are inside the zone. Check boundary and outer-ward roads for NO2 increases from diverted traffic before recommending extension to those very wards.
MUST-NOT:
- X1: declare the zone did or did not cause the improvement outright; the evidence cannot settle it.
- X2: invent reported facts (e.g., claim a wind study or calibration was done, or that traffic fell).
- X3: fill the review with generic checks (sample size, p-values) unlinked to this design.
- X4: demand reference-grade monitors at all 45 sites as the only acceptable test; co-locating a subset is a fair requirement.
- Must not assert as fact that weather or displacement explains the result — those are untested hypotheses here.
EXTRA CREDIT:
- Cross-sensitivity of electrochemical cells to ozone; placement bias (volunteers' windows, distance from roads); any mid-study firmware or recalibration events; use of the city's existing background monitor as a free control series.


## case_n5

MUST:
- Concurrent changes: the maintenance window that changed the profile may also have changed paste lot, stencil, feeders, or the AOI library revision. The report never excludes other simultaneous changes on or around 12 August.
- Missing control line: Lines 1 and 2 ran unchanged through the same weeks; their defect trend is the natural control and was not examined. A shared drop would point to a plant-wide cause, not the profile.
- Measurement validity: the entire before/after series comes from the single Line 3 AOI station; a re-tuned program or drifted threshold would manufacture the drop. Cross-check with ICT/functional test results or an independent manual audit of stored images.
- Time horizon: two weeks of AOI catches visible defects only. Latent joint failures (head-in-pillow, brittle joints) surface at ICT, functional test, or in field returns — none is reported for boards built under the new profile.
MUST-NOT:
- X1: declare the profile does or does not work; attribution is untested.
- X2: state as fact that a paste lot changed or the AOI was updated — the case doesn't say; these are things to check, not findings.
- X3: generic process-improvement advice with no tie to this design.
- X4: demand destructive sectioning of every board; sampled cross-sections suffice.
- Must not assert the improvement will regress or that rollout is safe/unsafe as settled.
EXTRA CREDIT:
- Independent recount of stored AOI images by QA outside this group (the claiming group compiles the numbers); stratify by board type and batch in case the product mix shifted to easier boards; SPC/CUSUM to date precisely when the step occurred; verify same operator shifts pre/post.


## case_n6

MUST:
- No control condition: no comparison with teams that kept their normal schedule (or a waitlist group), so the 3.3-point drop cannot be attributed to the meeting change; a same-period control team trend is the key missing test.
- Attrition/survivorship: only 44 of 71 baseline completers (and 44 of 94 invited) answered at week 8. If the most stressed or busiest staff dropped out, the improvement is inflated; follow-up rates and baseline scores of non-responders must be checked.
- Concurrent cause: the summer hiring wave and lighter workload fall in the same weeks and plausibly reduced stress on its own; the design cannot separate it from the meeting change.
- Clustering/non-independence: outcomes are individual but the intervention was assigned to 5 teams, and volunteers chose to join — "every team improved" rests on 5 non-independent units with self-selected leads; the analysis must treat team as the unit or adjust for clustering, and note the self-selection.
MUST-NOT:
- X1: conclude meetings do or don't reduce stress in general; the evidence cannot settle it.
- X2: assert that dropouts were the most stressed, or that hiring explains the effect — plausible, untested.
- X3: generic survey advice (Cronbach's alpha, Likert formatting) unconnected to this design.
- X4: demand a double-blind version — participants inevitably knew; a waitlist control is the appropriate ask, not blinding.
EXTRA CREDIT:
- Demand characteristics/reactivity of a repeated self-report whose purpose participants knew; objective outcomes (absence, handle times, attrition) as converging measures; effects beyond 8 weeks; randomizing teams rather than taking volunteers.


## Amendments adopted before any answers (6 October 2026, audit by Opus 5.5)

Numbering convention: MUST items are referred to as M1, M2, … in the order they appear in each case's list above; case-specific MUST-NOT bullets as N1, N2, … in order (the common X1–X4 keep their labels). All six cases are usable; none is withdrawn.

### case_n1
- case_n1: reword M2 to: "Unblinded, self-recorded outcomes: nothing says the harvest crews who weighed and graded were blind to treatment; the logs were compiled by the operations manager who proposed the trial; and the blossom-end-rot reduction is an untallied crew impression. Blind grading, third-party tallying, or counted culls are needed." Reason: the case does not state that the crews saw which rows were sprayed; the point is that blinding is not reported.
- case_n1: reword M4 to: "Economics: the $9,000/ha figure counts only product cost (~$340/ha) against yield; the labour, equipment and scheduling cost of a weekly spray program is not included, and the value depends on 2024 contract prices. Credit also, but do not require, fruit-quality or shelf-life checks." Reason: the case text supports the missing application cost directly; specific quality measures (soluble solids, firmness, shelf life) are not derivable from it and are already partly covered by "marketable" grading, so requiring them is unfair.
- case_n1: reword N3 to: "Explicitly endorse the t-test over 16 weekly totals of the same rows as sound, independent evidence." Reason: as written, the bullet penalises an answer that merely leaves out the repeated-measures point, which the list itself gives only as EXTRA CREDIT. Leaving it out loses the extra credit; it is not a violation.

### case_n2
- case_n2: reword M2 to: "Outcome validity: the endpoint is the district's own interim algebra assessment, and the app is aligned to the same state standards. Ask how far the assessment overlaps the app's content or item format (teaching to the test) and whether an independent measure (e.g. a state test) agrees." Reason: the case does not say MathQuest matches the assessment's *formats*; that was stated as fact in the marking.
- case_n2: reword M3 to: "Selection, baseline equivalence and exclusion: assignment was not randomized (adopting vs comparison classrooms in the same schools; how classrooms came to adopt is not reported) and no baseline/prior-achievement comparison or adjustment is reported. About 300 students were excluded, with no split by arm. The answer must ask for baseline equivalence (e.g. fall scores) and for exclusions by arm, with sensitivity analysis or bounds for the excluded students." Reason: the original demanded an 'intention-to-treat including the excluded students', which is not possible as stated, because those students have no spring score (only imputation or bounds are possible). It also left out baseline equivalence, the most basic check for a non-randomized comparison.
- case_n2: move M4 (time horizon / fade-out) from MUST to EXTRA CREDIT. Reason: durability after the term matters for the purchase, but it does not test the claimed 0.31 SD term-end effect. As a MUST it outweighs points the case invites directly, such as the self-selected dose–response.

### case_n3 (the well-tested case)
Audit judgement: the case is well tested on its stated endpoints, and the MUST list's overall stance (strong evidence, with scope limits) is right. Several details in the case text can still be questioned legitimately, and the marking should not penalise them:
- case_n3: add to EXTRA CREDIT: "Notes the timing: the test window closed on 9 October and labels needed 60 days to mature (to about 8 December), yet rollout began on 20 October. The rollout decision therefore came before the final matured results could exist, or the dates need checking. This concerns the decision process, not the validity of the measured effects."
- case_n3: add to EXTRA CREDIT: "Asks whether non-inferiority was judged on the confidence bound rather than the 0.04 pp point estimate (no interval is reported). Also asks how declined transactions were confirmed legitimate, and whether chargebacks arriving after 60 days (network windows can be longer) could matter."
- case_n3: add a clarification to N1: "Raising the timing, confidence-interval, false-decline labelling or late-chargeback questions above, framed as points to confirm, does not count as treating the claim as weak or as demanding a rerun." Reason: these questions are derivable from the text, and without this clarification a careful answer could be penalised.
- case_n3: reword M4's opening to: "State the real scope limits as limits, not defects — at least the short late-summer window (holiday fraud mix untested) and adversarial adaptation/drift needing post-launch monitoring; other rails/portfolios and retention effects of extra declines are further credit." Reason: as written, M4 bundles six sub-points into one MUST. A grader could fail an answer that names the two main limits.

### case_n4
- case_n4: reword M4's first sentence from "all sensors are inside the zone" to "the results are reported only for the four inner (zone) wards, and no sensor outside the zone is reported". Reason: the case does not say where all 45 households are. It says only that the improvement "holds in every ward", in a text about the four inner wards.

### case_n5
- case_n5: reword M1 to: "Concurrent changes: the report does not rule out other changes on or around 12 August — paste lot, stencil, feeders/nozzles, AOI program or library, product mix." Reason: the marking states as fact a 'maintenance window that changed the profile', which the case does not mention. This breaches the list's own X2 standard.
- case_n5: reword M2's first clause to "Lines 1 and 2 have not had the new profile (it is proposed for them), so their defect trend over the same weeks is the natural control and is not reported." Reason: the case does not say they 'ran unchanged'.
- case_n5: add MUST M5: "Baseline and regression to the mean: the profile was changed after a defect spike, and the case does not give the period of the 3.1% 'before' figure, the pre-spike baseline rate, or whether the spike was already subsiding by 12 August. A spike can fall back on its own. The answer must ask for the longer pre-change series (Q1 through early August) to show that the step coincides with the change." Reason: this is the most direct alternative explanation the case invites ("after the Q2 defect spike"), and the list leaves it out.
- case_n5: add to EXTRA CREDIT: "Transferability: a reflow profile is specific to an oven and a board. Ask whether Lines 1 and 2 had the same spike and defect types, and require a profiling and pilot run on each line before transfer. Also ask whether a 245 °C peak is within the component ratings for those lines' products."

### case_n6
- case_n6: reword M4 to: "Self-selection: team leads volunteered their teams, so the five teams may be unrepresentative of the company. This bears directly on the company-wide recommendation." Then move the clustering point (five teams assigned, individual-level paired t-test, 'every team improved' rests on five units) to EXTRA CREDIT. Reason: as written, M4 joins two separate points, so an answer making only one could be marked down. Self-selection follows directly from the text and from the recommendation. The clustering adjustment is a valid but more technical refinement.
- case_n6: add to EXTRA CREDIT: "Fidelity/displacement: whether Wednesday afternoons were actually meeting-free, and whether meetings simply moved to other days. Neither is reported."
