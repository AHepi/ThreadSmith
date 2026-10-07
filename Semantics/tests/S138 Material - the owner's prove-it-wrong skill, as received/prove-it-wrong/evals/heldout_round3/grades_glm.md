# Case-by-case grading

## case_n1 (KelpMax greenhouse trial)

### Set 1
**MUST**
- **M1 (row allocation/position confound) — Found.** "spray is perfectly confounded with south-end microclimate (light, airflow, irrigation zone, pollinator entry, edge effects)"; fix proposed: "interleave sprayed/unsprayed plots across both ends of the block."
- **M2 (unblinded/self-recorded outcomes) — Partly.** Only the BER element: "BER culls: idle as evidence — not tallied... a recalled impression" (with the counted-culls remedy). Crew blinding and the manager-compiled logs are never mentioned.
- **M3 (generalization) — Found.** "would only show the spray works at this site, cultivar, and season... would not... generalize to other blocks or years."
- **M4 (economics) — Partly.** "borrowed from 2024 contract prices... fitted to one year" (price dependency found); the missing labour/equipment/scheduling cost of the weekly spray program is never raised.

**MUST-NOT:** N1 not violated; N2 not violated (rival confounders framed as possibilities); N3 not violated (t-test not endorsed — it is simply not mentioned); X1–X4 not violated.

**Extra credit:** repeated-measures/t-test — missed; registration/residue — missed; economics sensitivity — partly (2024 prices only, no labour).

**Wrong:** nothing material.
**Padding: 1** ("Patches/catch-alls: None yet — this is a first report, so no rescue has been attempted").

### Set 2
**MUST**
- **M1 — Found.** F1: "position (south end, rows 1-20), not spray, would explain the gain"; swap falsifier; next test "spray assignment swapped to rows 21-40."
- **M2 — Found.** F3 (grading bias, tallied culls); F5/Q11 "the manager who proposed spraying also compiled the yield logs"; Q13 quotes "culls 'were not tallied separately'"; asks for logs "kept independently of the trial's proponent."
- **M3 — Found.** Q1: "one block, one cultivar, one season."
- **M4 — Missed.** No mention of $9,000/ha, $340/ha, spray labour, or contract prices anywhere.

**MUST-NOT:** **X2/N2 — violated (mildly):** F3 presupposes "the crews who knew the assignment" — the case never states crews knew which rows were sprayed (exactly the trap the amendment flags). N1, N3 not violated (F2 attacks the t-test's independence, the correct direction); X1, X3, X4 not violated.

**Extra credit:** repeated measures — **Found**: "The 16 weekly row totals are not independent draws; recomputed on 20 vs 20 row-season totals... the p-value no longer clears 0.05." Registration and economics sensitivity — missed.

**Wrong:** the crew-knowledge assertion above; minor nitpick: "raw per-row daily scale tickets" presumes a record form the case does not describe.
**Padding: 0.**

**Better: Set 2** — it fully covers the measurement-provenance MUST and earns the repeated-measures credit; Set 1's cleaner answer never asks who measured, and only half-catches economics.

---

## case_n2 (MathQuest app)

### Set 1
**MUST**
- **M1 (co-intervention) — Found.** "Orientation + teacher quizzing... co-interventions present only in the treatment group"; fix: "compare app-only adopting classrooms against classrooms that got the orientation and added quizzes but not the app."
- **M2 (outcome validity) — Missed.** No mention of the district interim assessment overlapping app content/format, teaching-to-the-test, or an independent measure.
- **M3 (selection/baseline/exclusion) — Partly.** "classrooms weren't randomized" and "no report of whether exclusion was balanced across arms" (selection + exclusions by arm), but no request for baseline/prior-achievement comparison or sensitivity/bounds.

**MUST-NOT:** N1, N2, N3 not violated (the orientation-only comparison is the marking's own feasible ask). **X2 — borderline violated (mildly):** "they self-selected into adopting" / "Teachers who volunteer for new tools" — the brief never reports how classrooms came to adopt. X1, X3, X4 not violated.

**Extra credit:** dose–response — **Found**: "self-selected dosage... produces the identical gradient with no causal app effect." Classroom nesting — missed; cost — marginal ($14 mentioned, not the 15-minute opportunity cost); fade-out — partly ("after the novelty of a new tool fades").

**Wrong:** the self-selection assertion above.
**Padding: 1** (the "Reverse" paragraph — a generic one-way-causal-claim check).

### Set 2
**MUST**
- **M1 — Partly.** Quizzes covered: "the added quizzes mix a second intervention into the app's credit" (F3); the retrieval-practice **orientation** is never mentioned and no isolating design is proposed.
- **M2 — Partly.** Independent measure found: F5 "End-of-year state scores, not just the spring interim, show no gain"; but no question about assessment/app content or item-format overlap.
- **M3 — Found.** F1 prior-year scores ("Adopting and comparison classrooms' prior-year scores... already differ by 0.2 SD or more"); F4/Q13 exclusions by arm ("those from adopting classrooms score lower on record than those excluded elsewhere"); non-randomized assignment noted.

**MUST-NOT:** N1, N2, N3 not violated (F2's placebo app is offered as a falsifier, not demanded). **X2 — borderline violated (mildly):** "schools or teachers chose to adopt" — not reported. X1, X3, X4 not violated.

**Extra credit:** dose–response — **Found**: "engaged students may use any daily app more, reversing the causal story." Nesting, cost, fade-out — missed.

**Wrong:** the "chose to adopt" assertion.
**Padding: 1** (F6 author/funding conflict check — fits any claim).

**Better: Set 2** — all three MUSTs covered at least partly, including baseline equivalence (the most basic check per the amendment) and an independent outcome measure; Set 1 misses outcome validity entirely.

---

## case_n3 (Sentinel-4 — the well-tested case)

### Set 1
**MUST**
- **M1 (decisive controls) — Found.** "Randomization by customer ID... held — by design"; "Pre-registration... held"; "Label maturation... holds the fraud-loss number against lag bias."
- **M2 (false-decline side) — Found.** The 0.04 rise vs margin is in the frozen question; "Subgroup checks... held — rules out the rival 'it only works for one region/customer type.'"
- **M3 (operational evidence) — Found.** Blind review and rollback confirmed ("the rollback trigger is a patch-in-waiting, and its gauge... named"; "Keep the pre-agreed rollback trigger active through a staged scale-up"); latency budget is listed (part 6) but never explicitly confirmed — minor gap.
- **M4 (scope limits) — Partly.** Adversarial drift strongly present ("will erode once fraudsters see it at 100% scale"; staged scale-up as monitoring); but the **late-summer window / holiday-mix limit is never named** — one of the two limits the amendment requires.

**MUST-NOT:** N1 not violated (staged rollout is monitoring, not a demanded rerun; the controls are accepted as reported); N2, N3 not violated; X1–X4 not violated.

**Extra credit:** late-chargeback point — **Found**: "only for disputes resolved inside 60 days; later-maturing disputes are outside the test." Shadow arm, holiday re-check, ring analysis, timing anomaly, CI point — missed.

**Wrong:** nothing material (the "other cases here" cross-reference is odd but harmless).
**Padding: 1** (the "Poke" paragraph).

### Set 2
**MUST**
- **M1 — Found.** Q6: "covered — report, 'hashed customer ID'; analysts 'blind to arm'"; Q10: "covered — report, 'endpoints, fixed before unblinding'"; F4 questions the pending-dispute count — a confirm-point protected by the amendment.
- **M2 — Found.** C1 quotes the 0.04 vs 0.10 margin; Q5: "covered — report, 'no subgroup breached the margin,' checked per region."
- **M3 — Partly.** Rollback "covered — report, 'rollback trigger tied to either endpoint'" and blind analysts (Q6); **latency (38 ms vs 50 ms) never mentioned**.
- **M4 — Found.** F1: "14 Aug-9 Oct excludes the high-fraud holiday season"; F3: adversarial adaptation with a feasible monitoring check ("fraud-ops could pull post-rollout monthly losses; passes if the rate stays below").

**MUST-NOT:** N1 not violated, but borderline noted: F1/F3 are monitoring-style checks matching the amendment's extra credit; however "held if F1, F2, F6" conditions the claim on an architecture ablation (F2) that cannot refute the 23% result — misplaced over-skepticism, not a rerun demand. N2, N3 not violated; X1–X4 not violated.

**Extra credit:** holiday re-check — **Found**: "Next test: pull November-December losses against the same margins." Shadow arm, ring analysis, timing anomaly, CI point — missed.

**Wrong:** "every number is self-reported by Sentinel-4's own team" — the case never says who authored the review, and this phrasing implies the model's vendor (contradicted by its own summary, "Meridian's own team"); F2's inclusion among the claim's hold-conditions is logically wrong.
**Padding: 2** (F2 architecture ablation; F6 conflict/re-tally check).

**Better: Set 2, narrowly** — it names both required scope limits and earns the holiday-recheck credit; Set 1 covers drift but omits the seasonal limit, which partly offsets Set 2's latency omission and factual sloppiness.

---

# Summary table

| Case | Set 1 MUST (found/partly/missed) | Set 1 MUST-NOT violated | Set 2 MUST (found/partly/missed) | Set 2 MUST-NOT violated | Better |
|---|---|---|---|---|---|
| n1 | 2 / 2 / 0 | none | 3 / 0 / 1 | X2 mild ("crews who knew the assignment") | Set 2 |
| n2 | 1 / 1 / 1 | X2 mild ("self-selected into adopting") | 1 / 2 / 0 | X2 mild ("chose to adopt") | Set 2 |
| n3 | 3 / 1 / 0 | none | 3 / 1 / 0 | none (N1 borderline noted) | Set 2, narrowly |

# Totals (11 MUST items each)

- **Set 1:** 6 found, 4 partly, 1 missed; 1 mild X2 violation; extra credit 2 found (n2 dose–response, n3 late-chargebacks) plus partials; padding ≈ 3.
- **Set 2:** 7 found, 3 partly, 1 missed; 2 mild X2 violations; extra credit 3 found (n1 repeated measures, n2 dose–response, n3 holiday re-check); padding ≈ 3.

# Three most important weaknesses

**Set 1**
1. **Blind spot on measurement provenance and instrument validity** — never asks who recorded the data or whether the outcome measure is aligned: crew blinding and manager-compiled logs absent (n1 M2); assessment-overlap/independent-measure absent (n2 M2).
2. **Drops case-specific quantitative and scope detail** — spray labour cost missed (n1 M4); latency listed but unconfirmed and, decisively, the holiday-window limit missed (n3 M4).
3. **Statistical-structure points left on the table while template checks fill space** — repeated-measures t-test (n1 EC) and classroom-level nesting (n2 EC) both missed; the generic Flip/Reverse/Poke paragraphs recur as padding in every case.

**Set 2**
1. **Asserts unreported facts as premises** — "crews who knew the assignment" (n1), "schools or teachers chose to adopt" (n2), "self-reported by Sentinel-4's own team" (n3).
2. **One-component drops inside bundled MUSTs** — orientation omitted (n2 M1), teaching-to-the-test overlap omitted (n2 M2), latency omitted (n3 M3), and the economics MUST missed outright (n1 M4: $9,000/ha never engaged).
3. **Generic provenance falsifiers and misapplied hold-conditions** — conflict-of-interest/re-tally checks recycled across n2 and n3 (padding), and n3's F2 ablation listed as a condition for a claim it cannot refute.

# Overall judgement

Set 2 handles all three cases better: its falsifier-first format forces engagement with the case-decisive tests (grading provenance, baseline equivalence, holiday window), giving it fuller MUST coverage (7 vs 6 full, equal misses) and more extra credit, at the cost of mild fact-inventions and some generic padding. Set 1's mechanism-centred template produces elegant rival analysis and cleaner factual hygiene, but it repeatedly omits the case-specific measurement, validity and scope points the marking lists treat as essential. Confidence: moderate-to-high on n1 and n2; the n3 call is close enough that a stricter reading of Set 2's N1/F2 over-skepticism could make it a tie, so overall confidence is moderate.# case_n4 — LEZ / NO₂

## Set 1

**MUST**
- **M1 sensor validity/calibration — FOUND.** "electrochemical NO2 sensors are known to be cross-sensitive to temperature and humidity… pending a calibration check against a reference monitor across the same seasonal swing"; next step asks for "a reference-grade cross-check on a sample of sensors" (subset-level, so X4-safe).
- **M2 meteorological confounding — FOUND.** "winter-to-spring NO2 drops (less home heating, less temperature-inversion trapping, different wind/dispersion) occur every year regardless of policy", plus a control ward or prior-year same-season comparison requested.
- **M3 traffic/activity data — FOUND.** "no traffic count or vehicle-mix data is cited to connect the LEZ's actual mechanism (reduced vehicle NO2 emissions in the zone) to the reading." (Framed as mechanism-linking rather than "less traffic from unrelated causes", but the missing-data point itself is explicit.)
- **M4 displacement / outside-zone readings (amended) — MISSED.** Outer wards appear only as a generalization caveat ("nor that outer wards (different traffic/heating mix) would see the same change"); no check for NO₂ *increases* on boundary/outer roads from diverted traffic before extension.

**MUST-NOT**
- X1: not violated ("Not settled", "untested against the obvious rival").
- X2: **minor violation** — "Not settled — no such ward was monitored" (and "there is no control ward outside the LEZ") states as fact what the case does not report; the amendment explicitly notes the case does not say where the sensors are. All other rival framing is hypothetical.
- X3: not violated (one quasi-generic significance point among many case-linked ones).
- X4: not violated (sample-level co-location).
- Case-specific (weather/displacement as fact): not violated — rivals kept as hypotheses.

**Wrong about the case:** the "no such ward was monitored" overstatement above; nothing else.

**Extra credit: 1/4** — placement bias ("self-selected households are not representative of exposure across a ward"). No ozone, no firmware/recalibration, no use of the existing background monitor.

**Padding: 1** — the generic "Flip" template ("Had NO2 risen in spring, would the report have blamed something else…").

## Set 2

**MUST**
- **M1 — FOUND.** F6: "A co-located reference-grade monitor, run alongside a sample of the sensors for the same months"; F2 covers temperature/humidity cross-sensitivity.
- **M2 — FOUND.** F1: "NO2 is seasonally higher in winter from heating and inversions, regardless of any zone"; F3 adds a same-period non-LEZ comparator.
- **M3 traffic/activity data — MISSED.** No request anywhere for traffic counts, fuel-price or transit data; the nearest touch is Q6's passing "differ in weather and traffic", which belongs to the seasonal point, not a data request.
- **M4 displacement — MISSED.** Outside areas are framed only as controls that "shows no comparable drop" (F1/F3), never as candidate sites of NO₂ increases from diverted traffic before the outer-ward extension.

**MUST-NOT**
- X1: not violated ("held if F1, F2 and F3 hold").
- X2: not violated — statuses are "missing/blocked" with proposed receipts; "no comparison area **in this update**" is carefully scoped.
- X3: not violated (F rows all case-linked; Q rows anchored to F items).
- X4: not violated ("one reference monitor per ward" is subset-level).
- Case-specific: not violated.

**Wrong about the case:** nothing material.

**Extra credit: 2/4** — placement/site bias (F4: volunteers "may sit away from the roads the zone targets"); reuse of existing reference-monitor data as a free control (F3 receipt: "could pull regional reference-monitor data").

**Padding: 1** — Q10 pre-registration row.

**n4 line:** **Set 1**, on one more MUST (traffic data), despite Set 2's cleaner record and extra credits.

---

# case_n5 — Line 3 reflow profile

## Set 1

**MUST**
- **M1 concurrent changes (amended) — FOUND.** "the note never says what caused the spike (paste lot, stencil wear, component moisture, humidity)… a coincident change (e.g., a paste or component lot rotating out around 12 August) would produce the identical before/after pattern".
- **M2 Lines 1/2 as natural control (amended) — MISSED.** Lines 1/2 appear only as transfer destinations ("What this does not show. That the same profile transfers to Lines 1 and 2"); their untreated same-weeks defect trend is never requested.
- **M3 measurement validity — FOUND.** "the before/after comparison depends on AOI calibration and classification being stable across the change date; this is asserted, not checked, and the group compiling the numbers is the one proposing the fix." (No ICT/functional or stored-image cross-check named — narrower remedy than the MUST, but the point itself is there.)
- **M4 latent defects / time horizon — MISSED.** Nothing on AOI catching visible defects only, or ICT/functional/field returns for new-profile boards.
- **M5 baseline / regression to mean (added) — PARTLY.** The self-resolving rival is stated ("the Q2 root cause… resolved on its own around the same time is a genuine rival"; "a fit to the calendar, not to a mechanism"), but the longer pre-change weekly series, the period of the 3.1% figure, and whether the spike was subsiding are never asked for.

**MUST-NOT:** X1 not violated ("candidate explanation, not a tested one"); X2 not violated (paste/humidity only as hypotheses); X3 not violated; X4 not violated; no settled claim that the improvement will regress or that rollout is safe/unsafe.

**Wrong about the case:** nothing material ("asserted, not checked" slightly overstates — the case asserts the numbers, not AOI stability; trivial).

**Extra credit:** ≈1 in partial form — interested-compiler point (within the QA-recount item) and partial transferability ("Lines 1 and 2, which may run different products, equipment, or baseline defect causes"; no 245 °C ratings question).

**Padding: 1** — the "Flip" template again.

## Set 2

**MUST**
- **M1 — FOUND.** F1: "A paste-lot, stencil or operator log entry around 12 Aug shows another change on Line 3 in the same window… the revised profile is not the only thing that changed then."
- **M2 — MISSED.** F6 uses Lines 1/2 only as pilot/transfer targets; their untreated trend over the same weeks is never requested.
- **M3 — FOUND.** F4: "An AOI count from another station, same boards, differs from 1.7% by more than 0.3 points", plus "figures 'compiled by this group'… no outside recount". (Doesn't name the re-tuned-AOI-program mechanism, but the external cross-check is the operative test.)
- **M4 — FOUND.** F5: "AOI catches visible defects only; it is a proxy for the reliability the fix should deliver", with field-failure tracking over the next quarter.
- **M5 — FOUND.** F3: "Pre-change weekly rates from the prior quarter vary by more than 1.4 points week to week on their own"; next test: "pull the prior quarter's weekly AOI rate on Line 3". (Doesn't say "regression to the mean", but the pre-change-series request is the required test.)

**MUST-NOT:** X1, X2, X3, X4 all not violated (log check is a proposed test, status "missing"; no findings asserted; pilot of one shift is not destructive sectioning); no settled safety/rollback claim.

**Wrong about the case:** nothing material; "prior quarter" is slightly loose vs "Q1 through early August".

**Extra credit: ≈2** — independent/outside recount (F4/Q11); per-line pilot before transfer (F6; no component-ratings sub-question).

**Padding: 1** — Q10 pre-registration row.

**n5 line:** **Set 2** — 4 MUST found vs 2 found + 1 partly; both missed the Lines-1/2 control.

---

# case_n6 — Meeting-Free Wednesday

## Set 1

**MUST**
- **M1 no control condition — FOUND.** "A concurrent, non-pilot comparison team (or teams) tracked on the same PSS-10 over the same eight weeks — ideally one that also benefited from the hiring wave but kept its normal meeting schedule."
- **M2 attrition/survivorship — FOUND.** "if the 27 non-responders were disproportionately still-stressed or still-busy staff, the remaining sample overstates the improvement; direction of bias isn't knowable from what's given."
- **M3 concurrent cause — FOUND.** "a rival the brief names itself but never separates out"; "'Stress fell because Q2's crunch ended and new hires absorbed workload' is at least as strong given what's in the case."
- **M4 self-selection (amended) — FOUND.** "self-selection likely means more receptive teams and leads are already represented… says nothing about compliance culture elsewhere"; "already-less-stressed teams were the ones whose leads volunteered first (selection, not production)."

**MUST-NOT:** X1 not violated; X2 not violated (conditionals; "direction of bias isn't knowable"); X3 not violated (no generic survey advice); X4 not violated (asks for a comparison group, not blinding).

**Wrong about the case:** nothing (27 non-responders, 62% both used correctly).

**Extra credit: 0** clean — no clustering/units point, no objective outcomes, no durability ask, no fidelity/displacement check.

**Padding: 0** (the "Flip" here is case-linked; the free-text-quote point is case-specific).

## Set 2

**MUST**
- **M1 — FOUND.** F1: "A non-pilot team, measured on PSS-10 over the same eight weeks, shows a drop of 2 points or more with no meeting-free afternoon."
- **M2 — FOUND.** F2: "The 27 non-completers' baseline scores, pulled from week-0 records, average 2 points or more above the 44 completers' baseline."
- **M3 — FOUND.** "the report names 'settling in after its summer hiring wave' as a live rival cause" (F1; Q3).
- **M4 — FOUND.** F3: "voluntary sign-up by team leads is a selection, not a random assignment."

**MUST-NOT:** X1, X2 not violated ("leaves room for the most-stressed staff to have dropped" — conditional); X3 not violated; X4 not violated (F4 notes unblinded self-report but asks for behavioral measures, not blinding).

**Wrong about the case:** nothing.

**Extra credit:** 3 full + 2 partial — objective outcomes (F4 sick-leave/turnover), demand characteristics ("unblinded to a watched intervention"), durability beyond 8 weeks (F6); partial for team-level recomputation (F5, not the five-non-independent-units point) and randomization (Q6). Fidelity (were Wednesdays actually meeting-free) not raised.

**Padding: 1** — Q10.

**n6 line:** **Set 2, slightly** — identical 4/4 MUSTs and clean MUST-NOTs, but Set 2 adds objective outcomes, reactivity and durability; Set 1's control-design specification is the sharpest single idea in either answer.

---

# Summary table

| Case | Set 1 MUST (F/P/M) | Set 1 MUST-NOT | Set 2 MUST (F/P/M) | Set 2 MUST-NOT | Better |
|---|---|---|---|---|---|
| n4 | 3 / 0 / 1 | X2 (minor) | 2 / 0 / 2 | none | Set 1 |
| n5 | 2 / 1 / 2 | none | 4 / 0 / 1 | none | Set 2 |
| n6 | 4 / 0 / 0 | none | 4 / 0 / 0 | none | Set 2 (slight) |
| **Total** | **9 / 1 / 3 of 13** | 1 minor violation | **10 / 0 / 3 of 13** | none | — |

Extra credit: Set 1 ≈ 1 full + 2 partial; Set 2 ≈ 7 full + 2 partial. Padding: Set 1 = 2; Set 2 = 3.

# Three most important weaknesses

**Set 1**
1. **Time-dimension MUSTs dropped (n5).** Latent joint failures after two weeks of visible-only AOI (M4) missed entirely; the pre-change series / spike-subsiding check (M5) only partly — the answer spends its space on which profile parameter did what.
2. **No untreated-companion comparisons (n4, n5).** Lines 1/2 are treated purely as transfer targets, never as the natural control trend (n5 M2); boundary/outer-road displacement never checked (n4 M4) — a repeated failure to use neighboring units as controls.
3. **Narrow sweep beyond one chief rival (all three).** Near-zero extra-credit pickup (none in n6), a boilerplate "Flip" check that pads (n4, n5), and one minor unreported-fact assertion ("no such ward was monitored", n4).

**Set 2**
1. **Mechanism-side confound missed in n4 (M3).** Never asks for traffic counts, fuel-price or transit data — whether the LEZ's actual lever (traffic) moved is unexamined.
2. **Same outside-the-zone blind spot (n4 M4).** Comparators are framed only as "should not also drop", never as sites of NO₂ increases from diverted traffic — directly relevant to the outer-ward extension being recommended.
3. **Same-line blind spot in n5 (M2).** Lines 1/2 appear only as pilot targets, never as the same-period control trend; plus a recurring generic rubric row (Q10) and arbitrary pass thresholds (15%, 2 points, 1.4 points) presented as if meaningful.

# Overall judgement

Set 2 is the stronger set: one more MUST item found, no MUST-NOT breaches (Set 1 has a minor X2 overstatement), and far broader secondary coverage (objective outcomes, durability, recounts, reference-monitor reuse). Set 1 writes more coherent single-rival narratives — its n6 control design is the best single passage in either set — but it drops more MUST items, especially time-horizon and companion-control checks. Confidence: moderately high — the item-level calls are quote-backed and the n5 verdict is clear — but the n4 verdict (Set 1's extra MUST vs Set 2's cleaner record and extra credits) and the n6 edge are close calls that could reasonably go the other way.