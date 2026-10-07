# Grading — Set 1 vs Set 2 (grader: Opus 5.5)

Marked against `marking.md` **as amended**. M = MUST items, N = case-specific MUST-NOT bullets, X1–X4 = common MUST-NOT, EC = extra credit. F = found, P = partly, M = missed (in tallies).

Rule I applied on borderline overstatements: if a fact the case does not give is stated in passing inside a hypothetical, I note it under "errors" and don't count it. I count it as a violation when the answer relies on it, either as the stated basis for a test or in its bottom line.

---

## case_n1 — KelpMax

### Set 1
| Item | Verdict | Evidence |
|---|---|---|
| M1 row position | **F** | "spray is perfectly confounded with south-end microclimate (light, airflow, irrigation zone…) … no randomization, no interspersed sprayed/unsprayed rows" |
| M2 (amended) unblinded / proponent-compiled / untallied BER | **P** | Has the BER point ("not tallied … a recalled impression, not a measurement"; "record … BER counts directly"). Never mentions grader blinding or that the proposing manager compiled the logs. |
| M3 generalization | **F** | "would only show the spray works at this site, cultivar, and season … nor that the effect generalizes to other blocks or years" |
| M4 (amended) economics: application labour, contract prices | **P** | "economic case ($9,000/ha benefit) is borrowed from 2024 contract prices and this season's weather". Spray labour and equipment cost are missing. |
| EC | 0 | No repeated-measures point, no registration/residue point. Contract prices are already credited under M4. |

MUST-NOT: N1 no, N2 no, N3 no, X1 no, X2 no, X3 no, X4 no.
Errors: none material. "no bloom date or fruit-set count was measured" is a fair reading: the case says only "observed".
Padding: 2 ("Patches/catch-alls: None yet"; the "Flip" counterfactual about blaming shade).

### Set 2
| Item | Verdict | Evidence |
|---|---|---|
| M1 | **F** | F1 "A repeat split with rows 21-40 … sprayed instead"; "spray confounded with greenhouse position" |
| M2 (amended) | **F** | F3 "Blossom-end-rot culls, tallied separately by row"; F5 "the only record is self-compiled by the trial's proponent"; next test "logs kept independently of the trial's proponent". Grading bias is raised in F3. |
| M3 | **F** | Q1 "one block, one cultivar, one season" (thin, but it is the point) |
| M4 (amended) | **M** | Nothing on application cost or contract prices. Q12 "commits cost" is only a vague cousin. |
| EC | 1 | EC1: F2 "weekly totals are repeated measures on 40 rows, not 16 independent trials … recomputed on 20 vs 20 row-season totals" |

MUST-NOT: none counted. Borderline X2: F3 says "the crews who knew the assignment", but the case never says the crews knew. The amendment exists because of exactly this. It sits inside a falsifier, so I noted it and didn't count it.
Errors: the X2 borderline above. Q2 "nothing was supplied as input beyond spray" is meaningless here.
Padding: 4 (Q2, Q4, Q8 "does not apply"; Q7-C1 "covered" adds nothing).

**Better: Set 2.** It catches the proponent-compiled logs, grading bias and the repeated-measures problem. Set 1 never raises blinding or who compiled the logs.

---

## case_n2 — MathQuest (amended: M1 co-intervention, M2 outcome validity, M3 selection/baseline/exclusions. Time horizon moved to EC.)

### Set 1
| Item | Verdict | Evidence |
|---|---|---|
| M1 co-intervention | **F** | "co-interventions present only in the treatment group … compare app-only adopting classrooms against classrooms that got the orientation and added quizzes but not the app" |
| M2 outcome validity | **M** | The interim assessment and its alignment with the app are never questioned. |
| M3 selection / baseline / exclusions by arm | **P** | Has "no report of whether exclusion was balanced across arms" and "classrooms weren't randomized". There is no request for baseline equivalence (prior or fall scores) or for bounds on the excluded students. |
| EC | 2 | Dose–response is self-selected ("self-selected dosage … produces the identical gradient"). Fade-out: "after the novelty of a new tool fades" (partial). No clustering point, no opportunity-cost point. |

MUST-NOT: none violated. Minor overstatement: "they self-selected into adopting". The amendment notes the case does not say how classrooms came to adopt. It is phrased as a fact, but it is not used as a finding, so I didn't count it.
Errors: the overstatement above.
Padding: 2 ("Reverse … direction is untested"; the "Flip" paragraph).

### Set 2
| Item | Verdict | Evidence |
|---|---|---|
| M1 | **P** | F3 "the added quizzes mix a second intervention into the app's credit". But the falsifier itself ("Comparison scores, before any quizzes were added …, already track the eventual gap") doesn't test the co-intervention, and the orientation is never mentioned. |
| M2 | **P** | F5 "End-of-year state scores, not just the spring interim" gives an independent measure. There is no question about how far the assessment overlaps the app's content or format. |
| M3 | **F** | F1 "prior-year scores … already differ by 0.2 SD"; F4 "Of the ~300 excluded students, those from adopting classrooms … differential attrition" |
| EC | 1 | Dose–response: F2 "engaged students may use any daily app more". |

MUST-NOT: none violated. A placebo app (F2) is a feasible test, not an X4.
Errors: F3 is incoherent as a test of the co-intervention. "whose teachers also added written quizzes" over-generalizes, since the case says "several". The thresholds ("by over 1 scaled point") are arbitrary.
Padding: 5 (Q2, Q4, Q8 "does not apply"; F6 author/funding check, which is generic; Q10–Q12 restate F6).

**Better: Set 2, narrowly.** Its coverage is broader (baseline equivalence, exclusions by arm, an independent outcome). Set 1 handles the central co-intervention point better but misses outcome validity entirely.

---

## case_n3 — Sentinel-4 (the well-tested case)

### Set 1
| Item | Verdict | Evidence |
|---|---|---|
| M1 confirm decisive controls | **F** | Randomization "held", pre-registration "held … what makes the 23% figure hard to explain away", label maturation "held, with a scope caveat" |
| M2 false-decline side covered | **F** | "Subgroup checks … held — rules out the rival 'it only works for one region/customer type'". The 0.04 pp rise against the margin is in its framing. |
| M3 operational evidence | **P** | Covers blind review and the rollback trigger ("rollback trigger … its gauge … is named"). Latency is only listed as a part and never confirmed. |
| M4 (amended) scope limits as limits | **P** | Adversarial adaptation is well covered ("will erode once fraudsters see it at 100% scale"). The holiday or seasonal fraud mix is never named. |
| EC | 1 | Late chargebacks: "later-maturing disputes are outside the test". |

MUST-NOT: N1 no (it frames the main gap as phasing the rollout, not a rerun), N2 no, N3 no, X1–X4 no.
Errors: "the one change list item" is garbled. It also refers to "pre/post designs in other cases here", which is outside this case.
Padding: 2 ("Poke" check; "Reverse" paragraph).

### Set 2
| Item | Verdict | Evidence |
|---|---|---|
| M1 | **P** | Marks the randomization and pre-registration rows as covered (Q6, Q10). But it never credits the 60-day maturation and adjudication, and it treats disputes as an open hole (F4). Its bottom line makes the claim conditional: "held if F1, F2, F6". |
| M2 | **F** | Q5 "covered … 'no subgroup breached the margin,' checked per region" |
| M3 | **P** | Rollback (Q12) and blind analysts (Q6) are there. Latency is absent. |
| M4 | **F** | F1 "excludes the high-fraud holiday season"; F3 "fraud is adversarial; the trial attacker never saw Sentinel-4 live" |
| EC | 1 | Holiday re-check: next test "pull November-December losses against the same margins". |

MUST-NOT:
- **X2 violated**: F6 "every number is self-reported by Sentinel-4's own team". The case doesn't say this. The answer uses it as the basis for a test and repeats it in its bottom line ("as reported by Meridian's own team").
- **N2 violated**: F4 "Disputes unresolved at freeze time … leaves their count unstated" contradicts the case, which says pending disputes "had been adjudicated".
- **N1 violated (moderate)**: the claim is "held if F1, F2, F6", which makes acceptance depend on a holiday-period rerun of the same two arms, an architecture ablation (F2, which isn't needed for a Sentinel-4-vs-incumbent claim) and an independent re-tally. That treats a well-tested result as unproven. The amended N1 clarification protects questions framed as points to confirm. These are framed as conditions for acceptance.
- X1, X3, X4: no.

Errors: the F4 misreading; the F6 invented fact; F2 tests a claim (credit to the sequence architecture) that the case does not make.
Padding: 4 (Q2-C2, Q3-C2, Q4, Q8-C2 "does not apply").

**Better: Set 1.** It recognizes the case as strong and attaches its caveats as scope limits. Set 2 invents a self-reporting problem, misreads the adjudication, and makes acceptance conditional.

---

## case_n4 — LEZ NO2

### Set 1
| Item | Verdict | Evidence |
|---|---|---|
| M1 sensor validity / calibration | **F** | "cross-sensitive to temperature and humidity … pending a calibration check against a reference monitor"; "a reference-grade cross-check on a sample of sensors" |
| M2 meteorology / control site | **F** | "no control ward outside the LEZ and no comparison to the same Dec–Feb→Mar–May change in a prior, pre-LEZ year" |
| M3 traffic data | **F** | "no traffic count or vehicle-mix data is cited to connect the LEZ's actual mechanism to the reading" |
| M4 displacement to boundary or outer roads | **M** | It mentions outer wards only for transferability ("different traffic/heating mix"), not for diverted traffic. |
| EC | 1 | Volunteer placement bias: "volunteers in every ward happen to live somewhere less exposed". |

MUST-NOT: X3 has one generic point ("no p-value or CI is given"), well under a third, so not violated. The case-specific N (don't assert weather explains it as fact) is borderline: "Seasonal meteorology … would produce the same percentage drop". It is framed as an unexcluded rival, so not counted. X1, X2, X4: no.
Padding: 2 ("Flip" paragraph; the p-value point).

### Set 2
| Item | Verdict | Evidence |
|---|---|---|
| M1 | **F** | F2 "temperature/humidity cross-sensitivity"; F6 "co-located reference-grade monitor, run alongside a sample of the sensors" |
| M2 | **F** | F1 "outside the four wards, or the same four wards in a prior non-LEZ year"; F3, F5 |
| M3 | **M** | No request for measured traffic volumes. Q6 "differ in weather and traffic" is only a vague cousin. |
| M4 | **M** | F3 uses an outside area only as a control, not to look for displacement. |
| EC | 2 | Placement bias (F4, volunteers "may sit away from the roads the zone targets"); background or regional reference monitor as a control (F3). |

MUST-NOT: none counted. Minor overstatements: Q7 "uncalibrated sensors" and F6 "no reference-grade check has been run". The case only fails to report one. Noted, not counted.
Errors: those overstatements. F1, F3 and F5 largely duplicate each other.
Padding: 4 (Q2, Q4, Q10 "does not apply"; Q8 "sensor correction is fitted in the lab").

**Better: Set 1.** It gets the missing traffic data. Both miss displacement.

---

## case_n5 — Reflow profile (amended: M5 baseline / regression to the mean added)

### Set 1
| Item | Verdict | Evidence |
|---|---|---|
| M1 concurrent changes | **F** | "a coincident change (e.g., a paste or component lot rotating out around 12 August) would produce the identical before/after pattern"; "materials/humidity log check" |
| M2 Lines 1–2 as control | **M** | Lines 1–2 appear only as transfer targets. |
| M3 AOI measurement validity | **F** | "depends on AOI calibration and classification being stable across the change date; this is asserted, not checked, and the group compiling the numbers is the one proposing the fix" (no ICT cross-check named) |
| M4 latent defects | **M** | Nothing on ICT, functional test or field returns. |
| M5 baseline / regression to the mean | **P** | "The Q2 root cause … resolved on its own around the same time" is the rival, but it asks for material records, not the longer pre-change defect series. |
| EC | 0.5 | Transferability: "Lines 1 and 2, which may run different products, equipment" (no pilot required). |

MUST-NOT: none violated.
Padding: 2 ("Flip"; "Remove, in parts" repeats the part-by-part section).

### Set 2
| Item | Verdict | Evidence |
|---|---|---|
| M1 | **F** | F1 "A paste-lot, stencil or operator log entry around 12 Aug shows another change" |
| M2 | **M** | F6 pilots the profile on Line 1 or 2. It doesn't use their trend as a control. |
| M3 | **P** | F4 "An AOI count from another station … no outside recount". It is framed as self-compilation, not as program or threshold drift at the station. |
| M4 | **F** | F5 "Field failure rate tied to solder joints … AOI catches visible defects only" |
| M5 | **F** | F3 "Pre-change weekly rates from the prior quarter vary by more than 1.4 points"; next test "pull the prior quarter's weekly AOI rate" |
| EC | 1.5 | Transferability pilot (F6). Independent recount (F4, partial). |

MUST-NOT:
- **X2 violated**: F6 says as fact that "the other lines carry different paste or component mixes than Line 3". The case doesn't say this, and the answer uses it as the rationale for F6.
- Others: no.

Errors: Q13 "a full count, not a sample" isn't given in the case. The F2 single-factor revert is useful.
Padding: 4 (Q2, Q4 "does not apply"; Q5 "worst single week"; Q10).

**Better: Set 2.** It gets latent defects and the baseline series. Set 1 misses both and has no control line.

---

## case_n6 — Meeting-free Wednesday (amended: M4 is self-selection only; clustering and fidelity moved to EC)

### Set 1
| Item | Verdict | Evidence |
|---|---|---|
| M1 no control | **F** | "A concurrent, non-pilot comparison team … tracked on the same PSS-10 over the same eight weeks" |
| M2 attrition | **F** | "if the 27 non-responders were disproportionately still-stressed or still-busy staff, the remaining sample overstates the improvement" |
| M3 concurrent hiring wave | **F** | "the brief itself states a competing cause (hiring relief after a stretched Q2) … never separates out" |
| M4 self-selection | **F** | "self-selection likely means more receptive teams and leads are already represented"; "already-less-stressed teams were the ones whose leads volunteered" |
| EC | 0.5 | Durability: "once the hiring-wave relief fades" (partial). |

MUST-NOT: none violated. X2 is hedged ("if", "likely"). X4: no blinding demand.
Padding: 3 ("Flip"; "Reverse"; "Patches").

### Set 2
| Item | Verdict | Evidence |
|---|---|---|
| M1 | **F** | F1 "A non-pilot team, measured on PSS-10 over the same eight weeks" |
| M2 | **F** | F2 "The 27 non-completers' baseline scores … average 2 points or more above" |
| M3 | **F** | F1 effect: "names 'settling in after its summer hiring wave' as a live rival cause" |
| M4 | **F** | F3 "voluntary sign-up by team leads is a selection, not a random assignment" |
| EC | 2.5 | Demand characteristics and objective measures (F4 "self-report, unblinded to a watched intervention … sick-leave hours, turnover"); beyond 8 weeks (F6); team-level check (F5, partial cousin of the clustering point). |

MUST-NOT: none counted. Minor errors: Q12 says check-ins are "mandatory", but the case says only weekly. Q2 mentions "attendance records", which the case doesn't give. The next test's conclusion ("a survivor average, not a treatment effect") is stated a bit too strongly, though it is conditional.
Padding: 5 (Q2, Q4, Q8 "does not apply"; Q10; Q11).

**Better: Set 2, narrowly.** Both find all four MUST items. Set 2 earns more extra credit, though it has minor factual slips.

---

## Summary table

| Case | Set 1 MUST F/P/M | Set 1 MUST-NOT violated | Set 2 MUST F/P/M | Set 2 MUST-NOT violated | Better |
|---|---|---|---|---|---|
| n1 | 2/2/0 | 0 | 3/0/1 | 0 | Set 2 |
| n2 | 1/1/1 | 0 | 1/2/0 | 0 | Set 2 (narrow) |
| n3 | 2/2/0 | 0 | 2/2/0 | 3 (N1, N2, X2) | Set 1 |
| n4 | 3/0/1 | 0 | 2/0/2 | 0 | Set 1 |
| n5 | 2/1/2 | 0 | 3/1/1 | 1 (X2) | Set 2 |
| n6 | 4/0/0 | 0 | 4/0/0 | 0 | Set 2 (narrow) |

## Totals (24 MUST items)

| | Found | Partly | Missed | MUST-NOT violations | Extra credit (approx.) | Padding points | Cases won |
|---|---|---|---|---|---|---|---|
| Set 1 | 14 | 6 | 4 | 0 | ~5 | 13 | 2 |
| Set 2 | 15 | 5 | 4 | 4 | ~9 | 26 | 4 |

Neither set breaches X3 in any case. Set 2's tables come closest, because the Q rows that are "does not apply" or restate an F point are boilerplate.

## Three main weaknesses

**Set 1**
1. It misses measurement and data-source points, especially downstream outcomes: blinding and the proponent-compiled logs (n1), outcome validity of the interim test (n2), latent defects and the Lines 1–2 control (n5).
2. It uses the same reasoning template every time ("Flip", "Reverse", "Patches", "Poke"), and those sections often add nothing for the case (n1, n3, n5, n6).
3. It earns little extra credit, and it names a problem without giving the concrete check that would settle it: no ICT cross-check (n5), no baseline-equivalence ask (n2), no spray labour cost (n1), no holiday window (n3).

**Set 2**
1. It states facts the case doesn't give: Sentinel-4 numbers "self-reported by Sentinel-4's own team" (n3), other lines "carry different paste or component mixes" (n5). Smaller slips: crews "who knew the assignment" (n1), "uncalibrated sensors" (n4), "mandatory check-ins" (n6).
2. It doesn't recognize a well-tested result (n3). It misreads the adjudicated disputes as unresolved and makes acceptance depend on reruns and ablations.
3. Its Q-table is boilerplate and the falsifier wording is mechanical: rows marked "does not apply", arbitrary numeric thresholds, and some incoherent tests (n2 F3). It also misses case-specific points that don't fit the template: economics (n1), traffic counts (n4), displacement (n4).

## Overall judgement

The two sets cover the MUST items about equally (14/6/4 vs 15/5/4). Set 2 wins more cases, mainly on breadth and extra credit. Set 1 is more reliable: no MUST-NOT violations, and it judged the well-tested case (n3) correctly, which is where Set 2 invented facts and moved the burden of proof. Under strict grading I give Set 1 a slight overall edge for reliability, though Set 2 is the more thorough finder of tests. My confidence is low to moderate: the MUST counts are nearly tied, and the verdict depends mainly on how heavily one weights n3 and Set 2's factual slips.
