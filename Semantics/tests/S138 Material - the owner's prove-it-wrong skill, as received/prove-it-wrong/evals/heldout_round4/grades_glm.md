# case_g1 — Marsh Street bus priority

## Set 1

| MUST | Verdict | Evidence |
|---|---|---|
| M1 isolation from retiming + fare freeze | **Found** | F1: "A comparable route untouched by the bus lane, over the same 8 weeks, shows a travel-time and boarding change of similar size, since the citywide signal-retiming and the fare freeze ran over the same period" |
| M2 diverted traffic / unanchored 2.4 km/h | **Found** | F6: "Average vehicle delay on parallel side streets or cross-traffic rises by more than 2.4 km/h"; F8: "a 2.4 km/h fall is undefined as pass or fail against the pre-lane mean car speed" |
| M3 baseline seasonality / persistence | **Partly** | F2 covers persistence ("weeks 9-16 ... a novelty or publicity effect fading"); seasonality/weather/daylight of the Feb vs Mar–May baseline never raised |
| M4 what boardings measure (redistribution, not unique riders) | **Partly** | F7 questions the metric ("a counting-boundary change, not new ridership") but via an ungrounded counter-coverage mechanism; no redistribution from other routes/modes, no unique-riders point |
| M5 survey respondents or 71% baseline comparability | **Missed** | Only "the April survey's response rate and wording" under routine checks — neither credited route (onboard selection of existing riders; unknown date/method of the 71% baseline) |
| M6 extrapolation without corridor comparability | **Partly** | "The 15-20% projection ... is untested outside Marsh Street" — flags untestedness but gives no comparability reason (baseline delays, demand, route mix) |

**MUST-NOT:** none violated. (Borderline X4: the "next test" asks for a route "not touched by ... the fare freeze", which if the freeze is citywide may not exist — not counted, since a citywide-trends comparison is feasible and is the substance of the ask.) X3 not violated: the falsifiers are case-specific; the generic Q-template is counted as padding below.
**Wrong about the case:** nothing material.
**Padding:** ≈12 (the "does not apply" Q-rows, e.g. "single arm and measure each, no tied control", "nothing here was fitted, learned or tuned").
**Extra credit:** E1 found (compare changes on an untreated route over the same weeks — DiD in substance); E2 not found.

## Set 2

| MUST | Verdict | Evidence |
|---|---|---|
| M1 | **Found** | F1: "A corridor with the retiming project but no bus lane shows a travel-time gain of 10%+"; F2: "Boardings on routes untouched by the lane but covered by the February fare freeze rise 8%+" |
| M2 | **Found** | F3: "GPS speeds on the parallel street one block over fall more than 2.4 km/h ... diverted traffic would mean the car cost is understated" |
| M3 | **Partly** | F5: "A second 8-week window (weeks 9–16) shows most of the gain gone ... rests on one opening, one draw" — persistence only, no seasonality/weather of the baseline |
| M4 | **Missed** | No redistribution ("riders moving from other routes/modes") or unique-riders point anywhere; F2 tests the fare-freeze rival, not riders shifting between routes |
| M5 | **Missed** | The 71%→79% survey is never mentioned; it is not even in the C-list |
| M6 | **Found** | F6: "Ferndale's and Eastgate's baseline ridership and traffic differ from Marsh Street's by a stated margin ... projected gain elsewhere unsupported" |

**MUST-NOT:** none violated. Minor embellishment: "the parallel street one block over" invents a geography detail; framed as a measurement proposal, not a case fact, so not counted.
**Wrong about the case:** nothing; the survey omission is a coverage gap, not an error.
**Padding:** ≈10 ("does not apply" rows).
**Extra credit:** E1 found (untreated-corridor comparison, "find a corridor touched by retiming but not the lane"); E2 not found.

## Set 3

| MUST | Verdict | Evidence |
|---|---|---|
| M1 | **Found** | "compare ridership on corridor routes vs. other routes that got only the retiming/fare freeze, over the same 8 weeks ... the single most informative missing test" |
| M2 | **Partly** | Only the threshold half: "Held only if 2.4 km/h is the right threshold for 'not material,' which is asserted not fixed" — no diverted-traffic/parallel-street question at all |
| M3 | **Partly** | "a longer pre-period than one month" questions baseline adequacy; no seasonality/weather, no novelty-fade persistence check |
| M4 | **Missed** | No point on what the boardings rise measures |
| M5 | **Missed** | "satisfaction +8pp" listed as a given, never questioned |
| M6 | **Found** | "Ferndale/Eastgate, which likely differ in baseline congestion, bus frequency, and stop spacing? No mechanism is given that would generate a number for those corridors other than 'similar'" |

**MUST-NOT:** none violated. X1 checked: "Result: fails — attribution is currently a story" is a verdict on the causal story, not a declaration that the measured claim is false.
**Wrong about the case:** nothing.
**Padding:** ≈1 ("Check the patches ... N/A").
**Extra credit:** E1 found (pull data for untreated routes "and report the counterfactual gain"); E2 not found.

**Ranking g1: Set 2 > Set 1 > Set 3** — Set 2 fully covers M1/M2/M6; Set 1 also finds M2 and half of M4; Set 3 misses diversion (M2), M4 and M5 entirely.

---

# case_g2 — futures momentum backtest

## Set 1

| MUST | Verdict | Evidence |
|---|---|---|
| M1 execution realism / capacity | **Found** | F6: "Simulating fills at the next intraday price instead of settlement price ... settlement-price fills may not be achievable" (the same-bar fill point); F7: "A capacity test, sizing ~45 contracts per signal against each contract's actual volume ... without a tested capacity limit" |
| M2 survivorship | **Found** | F1: "Rebuilding the universe from each year's own liquidity ranking, not today's list ... survivorship/look-ahead bias" |
| M3 in-sample lookback and filter | **Found** | F2: "A frozen out-of-sample period ... or a second non-overlapping window (e.g. 2003-2013)"; F3: "a filter tuned to the one bad period it fixes may not generalise" |
| M4 robustness evidence | **Found** | F5: "'robust... no sector dependence' rests on an unreported worst case" (per-sector breakdown); F2 supplies the earlier-history element |

**MUST-NOT:** none violated. N4 checked: F8's "a regime with structurally different rates ... than 2013-2023" is conditional test framing, not a macro characterisation stated as fact.
**Wrong about the case:** nothing.
**Padding:** ≈12 ("does not apply" rows).
**Extra credit:** E2 found (F1 point-in-time universe + F7 capacity test); E1 (filter same-day look-ahead), E3 (rolls), E4 not found.

## Set 2

| MUST | Verdict | Evidence |
|---|---|---|
| M1 | **Found** | F6: "At $250M, ~45 contracts/signal, realistic market-impact slippage drops Sharpe below 1.2 ... live-size claim unmeasured" |
| M2 | **Found** | F3: "Universe fixed to contracts liquid in 2013 (incl. delisted since) ... 'currently listed' universe is survivor-selected" |
| M3 | **Found** | F1 walk-forward holdout for the lookback; F2: "a post-hoc filter may just patch 2020" |
| M4 | **Found** | F4: "'no sector dependence' rests on an average, not the losing year"; Q9: "one path, correlated years, not independent draws"; Q11: "'available on request' is an offer, not a run; nobody outside the team ran it" |

**MUST-NOT:** **X2 violated** — F6's receipt: "blocked | team reruns with an impact model; passes at 1.5+" invents a rerun and a result the case does not report (and contradicts its own effect note "live-size claim unmeasured"). **N2 violated** — the same cell states a specific corrected Sharpe ("passes at 1.5+") as fact. N1, N4, X1, X3, X4 not violated.
**Wrong about the case:** the fabricated receipt above.
**Padding:** ≈11 ("does not apply" rows).
**Extra credit:** E2 found (F3 universe + F6's impact ask); E1, E3, E4 not found.

## Set 3

| MUST | Verdict | Evidence |
|---|---|---|
| M1 | **Found** | "Execution model (settlement price + commission only) | Held if — ... held only if $250M/45 contracts avg doesn't move the market, which isn't tested", sharpened to "the less-liquid half of the 56 contracts" |
| M2 | **Found** | "'56 most liquid currently' universe | Unknown — current liquidity, not liquidity-at-each-historical-date, risks survivorship bias" |
| M3 | **Found** | Lookback "picked as the best of 4 in-sample candidates"; filter "a patch with no independent gauge"; poke: "run the system on 2000–2012 or 2024 data ... the most important missing test" |
| M4 | **Found** | "'No dependence on any single sector' is an output check, not a workings check"; "Ten profitable years ... is not ten independent tests"; OOS/earlier history demanded |

**MUST-NOT:** **N4 violated (borderline)** — "one broadly trending decade for trend-following assets" and "a regime change (not seen 2013–2023)" assert facts about the sample period the case does not give, and they drive the critique. N1, N2, X1, X2, X3, X4 not violated.
**Wrong about the case:** the above period characterisation.
**Padding:** ≈1 ("Reverse ... N/A").
**Extra credit:** E2 found (universe re-ranking + "capacity/impact study at $250M on the less-liquid contracts"); E1, E3, E4 not found.

**Ranking g2: Set 1 > Set 3 > Set 2 (near-tie at the top)** — all three find all four MUSTs and E2; Set 1 is fully clean, Set 3 carries one borderline N4, Set 2 fabricates a test result (X2+N2).

---

# case_g3 — macro-synthetic fibre trial

## Set 1

| MUST | Verdict | Evidence |
|---|---|---|
| M1 recognise strong design | **Partly** | Accepts "across three plants and three curing temperatures, fibre raised 28-day compressive strength by about 14%", but randomisation, blinding and the accredited third-party lab are never recognised as strengths (Q11 even says "no 'checked' or 'verified' language") |
| M2 accept 14% within scope, separate from striking | **Found** | "fibre raised 28-day compressive strength by about 14% ... held if the matched water-reducer dose is not itself contributing"; "Whether the early-age (7-day) strength is enough to justify earlier formwork striking ... is not shown by the 28-day figures reported" |
| M3 real scope limits | **Found** | F8: "Chloride ingress, freeze-thaw durability and fatigue loading were not tested; the source states footpaths 'fall outside that exposure here'"; scoped "in this standard C25/30 footpath blend" (dosage/supplier and flexural→crack-control sub-points absent) |
| M4 cost-conditioned proposal sensible | **Partly** | Quotes the conditioning (C4) but treats it as "ignor[ing] a possible finish or safety consequence" rather than noting the narrow conditioning is sensible |
| M5 early-age/striking gap | **Found** | F1: "The 7-day compressive strength by mix, the age that governs formwork striking ... the trial's stated purpose is unaddressed by the 28-day figures actually quoted" |

**MUST-NOT:** none violated (the water-reducer arm F2 is the allowed E3-type question; F7's replication ask is an extra, not a demand that the main tests be redone, since acceptance is granted within scope).
**Wrong about the case:** minor — treats 7 days as "the age that governs formwork striking"; striking typically occurs within hours to days.
**Padding:** ≈12 ("does not apply" rows).
**Extra credit:** E3 found (F2: third arm with "same water-reducer dose as the fibre mix but with no fibre"); E1, E2, E4 not found.

## Set 2

| MUST | Verdict | Evidence |
|---|---|---|
| M1 | **Found** | Q6 covered: "'alternating in randomised order', 'blinded to mix identity'"; Q9 covered: "Three batching plants each produced 20 trial loads and 20 control loads"; Q11 covered: "An accredited third-party laboratory ... blinded" |
| M2 | **Found** | "the 28-day compressive (14%) and flexural (7%) gains hold as reported, *held if* F2 and F3", with the striking claim kept separate: "not yet supported by the early-age data that decision actually needs" |
| M3 | **Found** | Q1 covered (durability exclusions quoted); "those are stated exclusions, outside the claim, not loose parts"; blend/temperature scoping in the claim-as-it-stands |
| M4 | **Partly** | Q12 covered quotes "Cost is EUR 6.80/m³ higher, so we propose using the fibre only where earlier striking is needed", but the conditioning's sensibility is never noted — the focus is the unsupported premise |
| M5 | **Found** | F1: "7-day (early-age) compressive gain, the figure the striking decision needs ... C3's actual premise is unsupported by data quoted here" |

**MUST-NOT:** none violated.
**Wrong about the case:** same minor 7-day-as-striking-age simplification as Set 1.
**Padding:** ≈9 ("does not apply" rows).
**Extra credit:** E3 found (F3: "A mix with fibre omitted but the same water-reducer dose ... the slump-matching admixture, not the fibre, could be the active part"); E1, E2, E4 not found.

## Set 3

| MUST | Verdict | Evidence |
|---|---|---|
| M1 | **Found** | "This design is unusually strong: randomised order, matched slump, blinded third-party testing, three plants, three cure temperatures — ... not to re-litigate what it already controls for" |
| M2 | **Found** | "28-day strength gain | Held — by the randomised, blinded, multi-plant, multi-temperature design", kept separate from the striking row |
| M3 | **Found** | Dosage ("no neighbouring dosage (e.g. 3 or 5 kg/m³) was run"), "the specific fibre product", durability "explicitly out of scope", lab-cylinder vs full-scale limit |
| M4 | **Missed** | Cost appears only as a "given" (+EUR 6.80/m³); the "only where earlier striking is needed" conditioning is never discussed |
| M5 | **Found** (sharpest of the three) | "striking typically happens well before 7 days; no data point in the 1–3 day range where the decision actually lives"; "Add early-age (12–72h) maturity or pull-out strength testing" |

**MUST-NOT:** none counted. Borderline X2 noted: "footpaths are commonly salted directly for pedestrian safety" asserts a general fact against the case's stipulation ("footpaths fall outside that exposure here") — treated as contesting the report's own assertion and framed as a question, so not counted.
**Wrong about the case:** the above assertion is the only questionable case-related claim.
**Padding:** ≈1 ("Check the patches ... N/A").
**Extra credit:** none — E3 missed (accepts "matched slump" without asking what the water-reducer change did to w/c or air); E1, E2, E4 not found.

**Ranking g3: Set 2 > Set 3 > Set 1** — Set 2 covers all five MUST dimensions plus E3; Set 3 misses M4 and all extras but has the sharpest M5; Set 1 never recognises the design (M1 partly).

---

# Summary table

| Case | Set 1 F/P/M | Set 1 MN | Set 2 F/P/M | Set 2 MN | Set 3 F/P/M | Set 3 MN | Ranking |
|---|---|---|---|---|---|---|---|
| g1 | 2/3/1 | 0 | 3/1/2 | 0 | 2/2/2 | 0 | 2 > 1 > 3 |
| g2 | 4/0/0 | 0 | 4/0/0 | 2 (X2, N2) | 4/0/0 | 1 (N4) | 1 > 3 > 2 |
| g3 | 3/2/0 | 0 | 4/1/0 | 0 | 4/0/1 | 0 (1 borderline noted) | 2 > 3 > 1 |

# Totals

| | Found | Partly | Missed | MUST-NOT violations | Extra credit | Padding | Cases ranked first |
|---|---|---|---|---|---|---|---|
| Set 1 | 9 | 5 | 1 | 0 | 3 (E1-g1, E2-g2, E3-g3) | ≈36 | 1 (g2) |
| Set 2 | 11 | 2 | 2 | 2 (X2, N2 — one fabricated passage) | 3 (E1-g1, E2-g2, E3-g3) | ≈30 | 2 (g1, g3) |
| Set 3 | 10 | 2 | 3 | 1 (N4, borderline) | 2 (E1-g1, E2-g2) | ≈3 | 0 |

# Three most important weaknesses per set

**Set 1**
1. Mechanism substitution: raises cousin tests instead of the listed ones — g1 M4 (counter-coverage change instead of redistribution/unique riders), M5 missed (response rate/wording instead of respondent selection or 71% baseline), M6 without corridor comparability.
2. Fails to explicitly recognise strong designs and conditioned proposals: g3 M1 partly — randomisation, blinding and the third-party lab never credited despite the case's emphasis.
3. Template bloat: ≈12 "does not apply" boilerplate rows per case (≈36 total) that add nothing case-specific; misses most extra-credit sharp points beyond its ledger (e.g. g1 E2, g2 E1/E3/E4, g3 E1).

**Set 2**
1. Fabricated evidence: g2 F6's receipt "team reruns with an impact model; passes at 1.5+" — an invented test and result (X2) including a specific corrected Sharpe (N2), contradicting its own "live-size claim unmeasured" note.
2. Whole-claim blind spots when items fall outside its falsifier table: g1 M4 (redistribution) and M5 (the satisfaction survey is not even listed as a claim).
3. Boilerplate burden (≈30 rows across three cases) plus small invented details ("the parallel street one block over", g1).

**Set 3**
1. Weak on measurement-validity threads: g1 misses diversion to parallel streets (M2 partly), boardings-not-new-riders (M4) and survey selection/baseline (M5) — its parts/flip method foregrounds causal attribution over what the metrics measure.
2. Asserts environment facts not in the case to drive critiques: g2 "one broadly trending decade" (N4); g3 "footpaths are commonly salted" (borderline X2).
3. Drops peripheral items: g3 M4 (cost-conditioned proposal) missed and no g3 extra credit (E3 missed); fewer extra credits overall (2 vs 3).

# Overall judgement

Set 2 has the best raw MUST coverage (11 found, first on two of three cases) but commits the only hard MUST-NOT breach of the round — an invented backtest rerun with a passing Sharpe — which under strict grading is a serious integrity failure, not a style flaw. Set 3 is the cleanest and by far the most efficient (near-zero padding, one borderline violation) with coverage only one found-item behind Set 2, and would be the safest choice where fabrication risk matters most. Set 1 is accurate and violation-free but too often settles for cousin tests and buries its real content in generic template rows. Confidence: moderate — the partial/found boundaries (g1 M4 and M6, g3 M1 and M4, the g2 N4 call) are genuinely close and could shift totals by one or two points either way, though the relative picture (Set 2 strongest on coverage, Set 3 cleanest, Set 1 thinnest) is stable across those calls.# case_g4 — Beetroot nitrate time trial

## Set 1

**MUST**
- M1 (fixed order, no counterbalancing, confounded with session): **Found.** "with every rider taking beetroot first and placebo second, a trial-order or learning effect cannot be told apart from nitrate." Correctly keeps to indistinguishability rather than asserting practice explains the gain.
- M2 (broken blinding: taste/colour + coach as designer/administrator/timer): **Found.** "the coach who designed the study, knew the assignment, administered the drinks and ran the visible stopwatch"; F2 also requires "drinks indistinguishable by taste or colour".
- M3 (diet control by self-report diary only): **Found.** "'no protocol violations' rests on the riders' self-report, not an independent check." (Background-nitrate point not made, but the central test is.)
- M4 (sample: one club/one coach non-independence, one trial per condition vs test-retest, CI lower bound 0.6% vs "~2% meaningful"): **Partly.** "one cohort of 14, tested once, is a single draw" — replication only; no non-independence, no test-retest variability, and the 0.6% bound is used only for a different purpose (F6).

**MUST-NOT:** N1 no (bias framed as rival explanation); N2 no; X1 no (hedged "held if"); X2 no; X3 no; X4 no.

**Errors about the case:** none.

**Extra credit:** E1 **found** (counterbalanced repeat + taste/colour-indistinguishable drinks + blinded timekeeper); E2 missed; E3 missed.

**Padding:** 0.

## Set 2

**MUST**
- M1: **Partly.** "a fixed order (beetroot always second) cannot separate nitrate from a practice/familiarity effect" — the confound is raised, but on an inverted order and via the non-credited "practice explains the gain" reasoning.
- M2: **Found.** "the coach knew the assignment and ran the stopwatch himself"; "'unmistakable in taste and colour' means the riders were not blinded either."
- M3: **Missed.** The diary is treated as adequate: Q13 "'diaries showed no protocol violations'" marked "covered"; self-report is never questioned.
- M4: **Missed.** Only generic replication ("one cohort, one week, one order"); no one-club non-independence, no test-retest, no CI-bound point.

**MUST-NOT:** N1 no; N2 no; X1 no; **X2 violated** — the case says beetroot was first; the answer states repeatedly "beetroot always second" (F1, Q10, "Claim as it stands"), a fact the case does not give (it contradicts it); X3 no; X4 no.

**Errors about the case:** the order inversion above; F1's "reversed (placebo second, beetroot first)" is internally muddled.

**Extra credit:** E1 **partly** (randomised counterbalance + blinded timer; no flavour-masked placebo, no washout); E2 missed; E3 missed.

**Padding:** 1 (F4, the free-standing "second independent cohort" replication check).

## Set 3

**MUST**
- M1: **Partly.** "perfectly confounded with any learning/familiarity/pacing effect of a second attempt at the same course" — confound raised, but again on the inverted premise ("beetroot always trial 2") and the discredited learning direction ("A pure learning/pacing-familiarity effect would produce exactly this pattern").
- M2: **Found.** "the one person who knew the allocation also ran the drinks and the stopwatch display riders saw"; "taste/colour gave it away, so expectancy effects on self-paced effort cannot be excluded."
- M3: **Missed.** The diary is accepted: "Diet-diary check | Held, narrowly"; self-report/background nitrate never questioned.
- M4: **Missed.** No sample critique at all (only "for these 14 riders" as framing); no test-retest or CI-bound point.

**MUST-NOT:** N1 no ("unconscious bias", not deliberate); N2 no; X1 no ("unestablished" is about evidential sufficiency, hedged); **X2 violated** — "(beetroot always second)", "beetroot always trial 2", "every rider got beetroot only on trial 2" contradict the case; X3 no; X4 no.

**Errors about the case:** the order inversion, repeated in the table, the reverse check and the flip check.

**Extra credit:** E1 **found** ("Counterbalance or randomise drink order… opaque, flavour-matched drinks; automated timing not visible to the coach"); E2 missed; E3 missed.

**Padding:** 0.

**Ranking (g4): Set 1 > Set 3 > Set 2.** Set 1 is the only set with the order right, the only one to question the diet diary, and violation-free; Set 3 edges Set 2 on extra credit (full E1) despite the same misses and the same inversion.

---

# case_g5 — Personalised pricing pilot

## Set 1

**MUST**
- M1 (early stopping): **Found.** "stopping halfway at first significance is optional stopping, which inflates the apparent effect."
- M2 (contamination / "conservative" unverified): **Found.** "'conservative' is asserted from an unquantified anecdote, not measured in either direction"; F7 asks for redemption logs by control-arm visitors.
- M3 (metric: returns/cancellations unnetted, pre/post-discount ambiguity, cannibalised margin): **Found.** "a revenue-per-visitor rise can coexist with a margin fall once the discount cost is netted out" (margin/discount netting; returns not specifically raised).
- M4 (operating point and actual window: Black Friday run-up, pull-forward, ordinary months): **Partly.** "over the roughly two weeks actually run" (window) and F6's "one atypical week" — but no Black Friday seasonality or pull-forward argument.
- M5 (extrapolation to all EU stores): **Found.** "the 5-6% EU-wide figure is projected from one UK, one-segment test" (plus F4 on the flagged subgroup).

**MUST-NOT:** N1 no; N2 no (falsifiers framed as tests); X1 no; X2 no; X3 no; X4 no.

**Errors about the case:** none material.

**Extra credit:** E1 missed (Q6 dismisses the account-ID split issue); E2 **partly** (fixed-horizon re-run + lift net of discount cost + redemption logging; no single-use code, no returns adjustment); E3 missed.

**Padding:** 0.

## Set 2

**MUST**
- M1: **Found.** "stopping once significant inflates false-positive risk."
- M2: **Found.** "'if anything ... conservative' is asserted, not measured"; F2 tests whether control redeemers spent as much as treatment.
- M3: **Found.** "'checkout totals at order time' may not net out returns"; plus voucher cost at EU scale (Q12).
- M4: **Found.** "over roughly half of a planned 4-week test"; "a demand spike big enough to justify urgency is big enough to be doing some of the work in the numbers too"; F3's seasonal mixing.
- M5: **Found.** "the UK figure may not transfer" (F4, Q1).

**MUST-NOT:** N1 no; N2 no; X1 no; **X2 violated** — F4's receipt invents an event and result the case does not report: "blocked | marketing runs a matched pilot in one EU store; passes within 5–6%"; X3 no; X4 no.

**Errors about the case:** the invented EU pilot above.

**Extra credit:** E1 missed; E2 **partly** (run to planned length; no margin/returns-adjusted re-run, no single-use code); E3 missed.

**Padding:** 0.

## Set 3

**MUST**
- M1: **Found.** "optional stopping on a significance threshold inflates the false-positive rate versus the design-time plan; no correction … is mentioned."
- M2: **Found.** "depends on how much of the control group redeemed the code and how, which isn't measured"; named test: redemption logs by account ID.
- M3: **Found.** "top-line revenue lift could be partly or wholly offset by discount cost … doesn't yet rule out 'revenue up, profit down'" (returns not specifically raised).
- M4: **Found.** "It does not show the effect would hold without Black-Friday-adjacent timing" (the atypicality point; the ~2-week window length itself is not noted).
- M5: **Found.** "EU transferability | Unknown — different markets, currencies, competitive context; no basis given."

**MUST-NOT:** N1 no; N2 no; X1 no; X2 no (the asymmetric-stopping inference is fair); X3 no; X4 no (full-window re-analysis is paired with a feasible sequential correction).

**Errors about the case:** none material.

**Extra credit:** E1 missed; E2 **partly** (full-window re-analysis/sequential correction + margin report; no single-use code); E3 missed.

**Padding:** 0.

**Ranking (g5): Set 3 > Set 2 > Set 1.** Set 3 and Set 2 cover all five MUSTs (Set 2 adds returns and the window length); Set 2 loses second place to a fabricated pilot result; Set 1 is clean but only partly gets the seasonal operating point.

---

# case_g6 — XSS remediation verified

## Set 1

**MUST**
- M1 (scanner validity; zero findings ≠ zero bugs): **Found.** "'zero findings' from a scanner never shown to catch a planted XSS shows nothing" (F1 plants a payload through the same DAST/SAST setup).
- M2 (what was scanned; authenticated pages): **Found.** "The 1,100+ crawled pages, checked against the full inventory, omit over 5% of templates: auth-only, API, PDF, email or admin pages."
- M3 (independence of verification): **Found.** "retrying only the original strings by the fix's authors may not show the sink is closed"; F3 requires "a tester outside the fix's own team".
- M4 (six weeks too short; lagging signals): **Found.** "Given 4 payouts over 6 months … the chance of 0 in a random 6-week window exceeds 20% … close to what the old rate gives by chance."
- M5 (SAST result covers only the new template layer; sinks outside unassessed/displacement): **Missed.** Nothing on the template-layer scope of SAST or non-template sinks; closest points are crawl inventory (F2, F6).
- M6 (manual retest scope: original payloads only; fresh adversarial testing): **Found.** "A fresh set of mutated payloads, different from the original Q2 set."

**MUST-NOT:** N1 no (planting is proposed for calibration, not a claimed bypass); N2 no; N3 no (bias framing); X1 no; X2 no (the 20% figure is arithmetic on the case's numbers); X3 no; X4 no.

**Errors about the case:** none.

**Extra credit:** E1 **partly** (seeded calibration scan + outside reviewer; no authenticated sessions); E2 **found** ("the recommendation is made without testing the library on that codebase", F5).

**Padding:** 0.

## Set 2

**MUST**
- M1: **Found.** "zero findings shows only the scanner's own corpus"; "swap it for a scanner carrying no XSS payloads and it reports the same zero"; F1 plants unseen-corpus payloads on staging.
- M2: **Found.** "1+ page outside the '1,100+' crawl (post-14 June, or behind auth) is found vulnerable."
- M3: **Found.** "the check that built the fix also graded it"; F3 re-runs by "someone outside the sanitiser team".
- M4: **Found.** "zero XSS reports could mean fewer lookers, not fewer holes"; F5 tests all-category bounty volume.
- M5: **Missed.** Nothing on the SAST result being limited to the new template layer or displacement to non-template sinks.
- M6: **Found.** "1 payload novel since 14 June succeeds against the sanitiser — closing assumes no untried bypass exists."

**MUST-NOT:** N1 no ("Not shown: that the sanitiser has a hole"); N2 no; N3 no; X1 no; **X2 violated** — "The hand re-run of the 4 Q2 payloads": the case never states the payload count (four is the bounty-payout figure); X3 no; X4 no.

**Errors about the case:** the conflated payload count above.

**Extra credit:** E1 **partly** (planted payload + outside party; no authenticated sessions); E2 missed (the internal-tools recommendation is quoted but the different-codebase transfer is never questioned).

**Padding:** 0.

## Set 3

**MUST**
- M1: **Found.** "'no reason to doubt coverage' | Unknown — asserted; scanners have known blind spots (DOM XSS, mutation XSS) not addressed" — the coverage claim is an opinion, and a differently-sourced corpus is proposed. (Less sharp than Sets 1–2: the seeded-build check itself is not proposed.)
- M2: **Found.** "uncrawled or authenticated/dynamic surfaces"; "no inventory of excluded surfaces".
- M3: **Found.** "Independent verification — by someone who didn't write the sanitiser — hasn't happened; the same team wrote and verified the fix."
- M4: **Found.** "held only if overall submission volume to the program stayed flat; if attacker attention dropped generally, zero XSS reports is not evidence"; the non-XSS payout comparison is proposed.
- M5: **Missed.** The SAST/template-layer scope and displacement are never raised; DOM/mutation XSS appear only as payload classes, not as unassessed sinks.
- M6: **Found.** "try a payload class the sanitiser was never built against (e.g. mutation XSS, Unicode-normalisation bypass)"; "a fitted part confirmed on its own fitting case".

**MUST-NOT:** N1 no; N2 no (general blind-spot statements, not assertions about this scanner's config); N3 no; X1 no; X2 no; X3 no; X4 no.

**Errors about the case:** none material.

**Extra credit:** E1 **partly** (independent pentest/different corpus; no seeded scan, no authenticated sessions); E2 **found** ("assumes the fix transfers to different sinks/frameworks; untested").

**Padding:** 0.

**Ranking (g6): Set 1 > Set 3 > Set 2.** All three miss M5 (SAST scope/displacement — the hard item); Set 1 is sharpest (explicit seeded-scan calibration, quantitative bounty check, E2) and clean; Set 3 matches on MUSTs with a good attention gauge and E2; Set 2 equals the coverage but has the "4 Q2 payloads" fabrication and misses E2.

---

# Summary table

| Case | Set 1 F/P/M | Set 1 MN viol | Set 2 F/P/M | Set 2 MN viol | Set 3 F/P/M | Set 3 MN viol | Ranking |
|---|---|---|---|---|---|---|---|
| g4 | 3/1/0 | 0 | 1/1/2 | 1 (X2) | 1/1/2 | 1 (X2) | S1 > S3 > S2 |
| g5 | 4/1/0 | 0 | 5/0/0 | 1 (X2) | 5/0/0 | 0 | S3 > S2 > S1 |
| g6 | 5/0/1 | 0 | 5/0/1 | 1 (X2) | 5/0/1 | 0 | S1 > S3 > S2 |

# Totals

| | Set 1 | Set 2 | Set 3 |
|---|---|---|---|
| MUST found | 12 | 11 | 11 |
| MUST partly | 2 | 1 | 1 |
| MUST missed | 1 | 3 | 3 |
| MUST-NOT violations | 0 | 3 (all X2) | 1 (X2) |
| Extra credit | 2 found, 2 partly | 0 found, 3 partly | 2 found, 2 partly |
| Padding | 0 | 1 | 0 |
| Cases ranked first | 2 (g4, g6) | 0 | 1 (g5) |

# Three most important weaknesses per set

**Set 1**
1. Misses the seasonal operating point when a test window is atypical — g5 M4 only partly (window noted, Black Friday/pull-forward never argued).
2. Shares the g6 blind spot: never questions that the SAST result covers only the new template layer (g6 M5).
3. Sample critiques stay at replication level — g4 M4 only partly; one-club non-independence, test-retest variability and the 0.6% CI bound vs "~2% meaningful" are never made.

**Set 2**
1. States facts the case does not give — one X2 per case: the invented EU pilot that "passes within 5–6%" (g5), "the 4 Q2 payloads" (g6), "beetroot always second" (g4).
2. Weak on trial-design reading in g4: misses diet self-report (M3) and sample non-independence (M4), and marks the diary evidence "covered".
3. Direction-of-bias carelessness — g4 M1 leans on practice/familiarity explaining a first-session beetroot gain, the one rival mechanism the amended list discredits.

**Set 3**
1. g4 is its worst case: the same order inversion (X2), M3 missed with the diary actively marked "Held", and M4 missed entirely.
2. The same g6 M5 gap (SAST scope/displacement) as everyone else.
3. Framework verdicts occasionally substitute for the specific test — g6 M1 rests on "asserted; scanners have blind spots" without the seeded/zero-coverage check, and g4's "single fatal gap" is argued through the misdirected learning story.

# Overall judgement

Set 1 is the most reliable: it is the only set with zero MUST-NOT violations, the only one to read the g4 design correctly and question the diet diary, and it wins or ties every case except g5, where it is merely thinner. Set 3 runs it close — full MUST coverage on g5 and g6 and the best extra-credit haul — but shares Set 2's g4 collapse (inverted order, missed M3/M4). Set 2 matches the g5/g6 coverage but is the only set to invent unreported results, and it did so in all three cases, which is disqualifying for trust even when the surrounding analysis is good. Overall: Set 1 ≥ Set 3 > Set 2.

Confidence: reasonably high in the ordering and in Set 2's violations (all three are textually clear); moderate on the fine F/P calls — g4 M1 for Sets 2–3, g5 M4 for Sets 1/3, and g6 M1 for Set 3 could each shift one grade without changing the rankings.# Grading — cases o1, o2, o3

## case_o1 (rgn4 / fin regeneration)

### Set 1
- **M1 Found** — F1: "A second, independent mutant allele (different sgRNA or exon) or an mRNA-rescue of this 7-bp deletion… a single CRISPR line cannot rule out an off-target mutation as the real cause."
- **M2 Found** — F4: "A proliferation assay (EdU/BrdU) in the 3-dpa blastema… 'drives proliferation' is inferred from expression data and domain homology, not a proliferation assay here"; F5 adds rivals (wound epidermis, migration, apoptosis).
- **M3 Found** — F2: "A re-measurement of the same images, by someone blind to genotype… the one measurement was made by the same student who did the amputations and genotyping."
- **M4 Found** — F3: "Length measured at 14 or 30 dpa… 'required for regeneration' needs more than one early timepoint to rule out a closing delay."
- **MUST-NOT**: N1–N3 not violated; X1–X4 not violated (all falsifiers correctly marked "missing").
- **Extra credit**: E1 Found (F6: "all 48 fish come from one pair; one clutch is one draw"); E4 Found (F4 effect column). E2, E3, E5 missed.
- **Errors**: none material (a nit: F7 asserts "morphologically normal was assessed by inspection only" — method not stated in the case; not load-bearing, not counted).
- **Padding**: 1 (F8, "A lab outside this subgroup reproduces the 41% deficit before the write-up is submitted" — generic replication demand).

### Set 2
- **M1 Found** — F1: "A second, independent rgn4 allele (different sgRNA target)… an off-target or linked mutation could be the real cause."
- **M2 Found** — F3: "Proliferation markers (EdU/PH3+) in the 3-dpa blastema… inferred from expression and homology, not measured"; Q3: "cell death or migration defects predict the same result."
- **M3 Found** — F2: "rescored blind to genotype on the same images… the same student amputated, genotyped and measured; nothing is blinded."
- **M4 Missed** — no delay-vs-failure or time-course question anywhere; Q1 treats "7 dpa" as mere scope ("stated for this line, this assay, 7 dpa; no wider promise made").
- **MUST-NOT**: N1–N3 not violated. **X2 violated (minor)**: Q5 says "individual fish values… are not given, only mean and SD" — the case reports no SD. X1, X3, X4 not violated.
- **Extra credit**: E1 Found (F4: "one clutch, one cross is the only genetic draw so far"); E4 Found ("supplied from published data and homology, not tested here"). E2, E3, E5 missed.
- **Errors**: the invented SD.
- **Padding**: 0.

### Set 3
- **M1 Found** — "a second, independent sgRNA/allele reproducing the phenotype would separate rgn4 from an off-target or linked mutation; not run"; plus rescue ("Re-expressing rgn4 in the mutant should restore regenerate length… not attempted").
- **M2 Found** — "Unknown — no proliferation assay was run. Shorter regenerate is consistent with reduced proliferation, increased apoptosis, delayed blastema formation, or impaired outgrowth"; "an EdU/BrdU or pHH3 proliferation assay at 3dpa is the missing test"; Wnt dependence correctly flagged as deferred.
- **M3 Found** — "Unknown — not blinded: the same student who amputated and genotyped also measured length in Fiji, a manual/subjective step."
- **M4 Found** — "Does the mutant catch up at later time points (14/21dpa), i.e. is this delayed regeneration or permanently impaired regeneration? Not tested."
- **MUST-NOT**: N1–N3 not violated; X1–X4 not violated ("fails" is applied to checks of the evidence, not to the claim's truth).
- **Extra credit**: E4 Found ("A correlative expression pattern plus a domain-homology guess is not evidence of mechanism"). E1 missed (clutch independence never questioned), E2, E3, E5 missed.
- **Errors**: none material (nit: "randomised-sibling… design" loosely describes a design the case does not name; charitable reading as Mendelian segregation).
- **Padding**: 0.

**Ranking o1: Set 1 > Set 3 > Set 2** — Sets 1 and 3 cover all four MUSTs; Set 1 adds the single-clutch point (E1); Set 2 misses the time-course item entirely.

---

## case_o2 (Harlan induced seismicity)

### Set 1
- **M1 Found** — F1: "Recomputing both counts using only the station subnetwork that ran continuously through all 48 months, excluding the 8 added in 2024… 'same picker' does not rule this out"; F5: "Restricting both periods to magnitudes safely detectable by the pre-densification network"; next test names "the magnitude of completeness."
- **M2 Found** — F2: "A 10 km or 20 km radius, chosen without reference to the post-injection map… the radius was picked after seeing the cluster."
- **M3 Found** — F4: "A comparable field with similar geology and no injection… nothing rules out a broader regional rise unrelated to Harlan's wells" (control-region ask met; the "same station change" nuance is left to F1).
- **M4 Found** — F3: "Monthly injection volume at the three wells correlates with monthly event count… no check that seismicity tracks the mechanism's own lever"; F6 adds a depth comparison.
- **MUST-NOT**: N1–N3 not violated (picker sentence explicitly rejected); X1–X4 not violated.
- **Extra credit**: E4 Partly (F3's monthly volume-vs-count is the "tracks injection volume" half of the diagnostic; no plot against densification date). E1, E2, E3 missed.
- **Errors**: none.
- **Padding**: 0.

### Set 2
- **M1 Found** — F3: "Magnitude-of-completeness, computed separately pre/post-2024, differs by more than 0.3 units"; F1: "With the 8 new stations removed, the post-injection count within 15 km falls by more than half."
- **M2 Found** — "flagged by the report itself as chosen 'after inspecting the epicentre map,' a free, post-hoc boundary unless shown not tuned to the result it frames" — circularity fully made, though no explicit radius-sensitivity re-run is proposed.
- **M3 Found** — F2: "The same comparison, on a circle with new station coverage but no well, shows a similar fold-increase" — a control region with the same station change; note the rival is framed only as densification, not as a natural swarm.
- **M4 Found** — F4: "Hypocentres lie within 1–2 km of the well bottoms, not scattered… required for the pressure-diffusion mechanism implied, not yet shown."
- **MUST-NOT**: N1–N3 not violated; X1–X4 not violated.
- **Extra credit**: E3 Partly ("regulatory limits follow; the station confound is a live consequence of error"). E1, E2, E4 missed.
- **Errors**: none.
- **Padding**: 0.

### Set 3
- **M1 Found** — "check whether the magnitude of completeness (Mc) dropped after the 2024 station densification… This test is not reported"; table: "A consistent *algorithm* run on a *denser* network still detects more, smaller events."
- **M2 Found** — "Swapping it for a neighbouring radius (10 or 20 km) and checking whether the fold-change survives is the natural robustness check; not shown."
- **M3 Found** — "a non-injection control area with the same new stations"; plus the pre-existing-trend rival: "Could seismicity have already been rising before March 2024… a longer baseline is needed."
- **M4 Found** — "Does the explanation predict the observed depth range from the known injection interval, rather than just reporting it? Not shown."
- **MUST-NOT**: N1–N3 not violated; X1–X4 not violated ("cannot yet separate 'more earthquakes' from 'more earthquakes detected'" is conditional).
- **Extra credit**: none (E1–E4 all missed).
- **Errors**: none.
- **Padding**: 0.

**Ranking o2: Set 1 > Set 3 > Set 2** — all three complete the MUSTs; Set 1 uniquely adds injection-volume tracking and the original-stations recount, Set 3 is close with the sharpest diagnosis; Set 2 never asks for an explicit radius re-run and frames the control only as a densification check.

---

## case_o3 (structured interviews)

### Set 1
- **M1 Found** — F1: "The 11 opt-in teams, scored on their own 2024 ratings and retention before the kit existed, already rate 0.2 points or retain 5 points higher… better teams opting in would produce this gap with no effect from the kit" (+F4 on retention baseline).
- **M2 Found** — F2: "the rater is the same manager who chose the kit and knows the method, unblinded"; F8 asks for "an objective metric (output, sales, peer scores)."
- **M3 Found** — F3: "'still employed at that review' drops 23% of comparison and 16% of structured hires, at different rates" (leavers re-included; differential loss noted).
- **M4 Found** — F5: "the expected 'similar gains' in new role types is untested."
- **MUST-NOT**: N1–N3 not violated (F4 correctly refuses both N1 conclusions); X1–X4 not violated.
- **Extra credit**: E3 Found (F9: "Time-to-hire or candidate drop-out under the kit rises by more than 10%… mandating the kit could cost hiring speed or candidates"). E1, E2, E4 missed.
- **Errors**: none.
- **Padding**: 0 (F6's replication ask is anchored to "one self-selected cohort over one year").

### Set 2
- **M1 Found** — F1: "Teams matched on manager quality, prior retention and size (not just the 11 vs 15 split)… the 11 opt-in teams may differ systematically from the other 15."
- **M2 Found** — F2: "the same managers who chose the kit also rate the hires, unblinded."
- **M3 Found** — F3: "With hires who left before 12 months counted at a below-average rating, the gap falls under 0.2 or reverses… 'still employed at that review' drops exactly the likeliest failures."
- **M4 Found** — Q1: "operations and support are explicitly new territory"; F4 effect: "'similar gains' is unsupported outside engineering/sales."
- **MUST-NOT**: **X2 violated** — F4's receipt: "HR runs one pilot team before Q3 2026; passes near 0.4" invents both a pilot and its result (the case reports neither), with a baseless "blocked" status, and contradicts its own effect column. N1, N2, N3 not violated; X1, X3, X4 not violated.
- **Extra credit**: E4 Partly (Q11: "'made decisions easier and fairer' is the same managers' own account" — used as bias evidence, not as the satisfaction≠quality scope point). E1, E2, E3 missed.
- **Errors**: the fabricated pilot and its result (above).
- **Padding**: 1 (the "Flip" paragraph — "had the comparison teams shown the higher rating, would the write-up have credited their hiring judgment…" — rhetoric that fits any evaluation report).

### Set 3
- **M1 Found** — "Not held — self-selection confound. Teams that chose to adopt may differ in management rigor, function mix, or motivation"; fix: "A within-team before/after comparison (adoption teams' own pre-2025 hires vs. post)."
- **M2 Found** — "Not held — rater is not independent of treatment. The same managers who chose the kit and said it's 'fairer' also supply the quality score"; asks for "an independent outcome (e.g., a cross-manager or objective performance measure)."
- **M3 Found** — "the two rated populations are differently survivor-filtered… were their last-known or exit ratings pulled in, or just dropped?"
- **M4 Found** — "that extending to ops/support (different skills, different interview content) should show similar gains. No change on the list supports this; it's an added, untested generalisation."
- **MUST-NOT**: N1–N3 not violated (the retention-trend aside handled correctly: "held only net of the stated company-wide cooling-market trend"); X1–X4 not violated.
- **Extra credit**: E4 Found ("Idle for the quality-of-hire claim — it's evidence about process satisfaction, a different job, not about hire quality"). E1, E2, E3 missed.
- **Errors**: none.
- **Padding**: 0.

**Ranking o3: Set 1 = Set 3 > Set 2** — both complete all four MUSTs with one extra each (Set 1: rollout costs; Set 3: pulse-survey scope); Set 2 covers the MUSTs but fabricates a pilot result.

---

## Summary table

| Case | Set 1 F/P/M | Set 1 MUST-NOT | Set 2 F/P/M | Set 2 MUST-NOT | Set 3 F/P/M | Set 3 MUST-NOT | Ranking |
|---|---|---|---|---|---|---|---|
| o1 | 4/0/0 | 0 | 3/0/1 | 1 (X2, minor: "mean and SD") | 4/0/0 | 0 | 1 > 3 > 2 |
| o2 | 4/0/0 | 0 | 4/0/0 | 0 | 4/0/0 | 0 | 1 > 3 > 2 |
| o3 | 4/0/0 | 0 | 4/0/0 | 1 (X2: invented pilot + result) | 4/0/0 | 0 | 1 = 3 > 2 |

## Totals

| | Found | Partly | Missed | MUST-NOT violations | Extra credit | Padding | Ranked first |
|---|---|---|---|---|---|---|---|
| Set 1 | 12 | 0 | 0 | 0 | 3.5 (E1+E4 o1; ½E4 o2; E3 o3) | 1 | 3 (2 outright, 1 tie) |
| Set 2 | 11 | 0 | 1 | 2 (both X2) | 3 (E1+E4 o1; ½E3 o2; ½E4 o3) | 1 | 0 |
| Set 3 | 12 | 0 | 0 | 0 | 2 (E4 o1; E4 o3) | 0 | 1 (tie) |

## Three most important weaknesses per set

**Set 1**
1. Occasional filler that would fit any claim — external-lab replication demanded before submission (o1) — plus arbitrary numeric thresholds ("within 5 points of 41%", "coefficient above 0.5") that mimic precision without grounding (o1, o2).
2. Closes off or skips fertile lines beyond the MUSTs: "the Poisson significance is not in question" (o2, forgoing declustering); no team-clustering or pulse-survey scope point (o3).
3. Format bloat: the 13-question grid is mostly "does not apply", burying strong falsifiers in template noise across all three cases.

**Set 2**
1. Fabricates test events/results: the invented HR pilot that "passes near 0.4" under a baseless "blocked" status (o3) — the most serious single defect in the batch.
2. Misses the subtler MUST: no delay-vs-failure time-course question at all (o1, M4); the radius-sensitivity re-run is only implied, never asked (o2).
3. Unforced slips about report contents: "only mean and SD" when no SD is reported (o1); extras thin outside o1 (no declustering, clustering or relocation anywhere).

**Set 3**
1. Narrowest reach beyond the MUSTs: misses single-clutch independence (o1), declustering and relocation (o2), rollout costs and team clustering (o3) — only two extras total.
2. Loose provenance language: "randomised-sibling… design" describes a design the case does not name (o1); "borrowed from regional geology (not named)" is speculative attribution (o2).
3. Verdict-flavoured phrasing ("Result: fails") skates near X1 without crossing it, and some checks stay conceptual — survivorship "inflate or deflate in either direction" without the 16%/23% anchor (o3).

## Overall judgement

On these three cases Set 1 and Set 3 are effectively complete against the marking lists with no MUST-NOT violations: Set 1 edges ahead on extra-credit breadth (clutch independence, injection-volume tracking, rollout costs) at the cost of some formulaic padding, while Set 3 is the most economical and case-anchored. Set 2 matches the core coverage except for the missed o1 time-course item and is clearly third because it twice states things the case does not give, including one wholly invented pilot result. Confidence: high for the MUST and MUST-NOT determinations (explicit lists, unambiguous answers); moderate for extra-credit partials and padding, where judgement enters.# Grading report — cases o4, o5, o6

---

## CASE o4 (CI flakiness agent)

MUST items: M1 three green runs ≠ fix (≈58% chance; many reruns needed); M2 fixes hide rather than remove cause (root-cause analysis); M3 race test moved to nightly, incident must stay open; M4 verification is self-reported (action log; need CI logs/human review). Extras: E1 runtime cost; E2 nightly job monitored; E3 other flaky tests beyond the 9; E4 branch vs main CI environment.

### Set 1
- **M1 found** — "At the prior ~1-in-6 failure rate, 3 consecutive passes occur by chance with probability near 58%; at least 30 runs are needed to tell a fix from luck."
- **M2 found** — "raising a timeout to 10 seconds can outrun a race without removing it"; "a retry that hides a genuine error is a patch, not a fix"; nightly move named in F1.
- **M3 found** — "the one test tied to that bug was explicitly excluded from CI, not shown fixed"; "Closing the refund double-posting incident on this basis does not follow."
- **M4 missed** — the self-reported action log / independence-of-verification point is never articulated. Q11 points to F3/F4, but F3 is about CI load and F4 about retry masking; no request for CI-system logs or independent review.
- **Extras:** E3 found ("'every one of the 9' leaves open whether 9 was the full count"); E4 found ("'on my branch' is not the load the flakiness was observed under"). E1, E2 missed.
- **MUST-NOT:** N1 no; N2 no (race treated as open); N3 no; X1–X4 no (the 58% is derived, not invented).
- **Errors:** none. **Padding:** 0.

### Set 2
- **M1 found** — "'failed roughly 1 in 6 runs' means 3 green runs sit within the old rate's own noise"; 50-run reruns requested (F1, F4).
- **M2 found** — "widened timeouts and retries can hide the fault instead of removing it"; "a retry that swallows a transient error also swallows a real one."
- **M3 found** — "the test tied to the actual incident is not among the passing runs, since it no longer runs on pull requests"; "reinstate the race test on the PR gate before closing the incident ticket."
- **M4 found** — "'I ran' and 'my branch' is the agent's own, unwitnessed run"; falsifier F4 = independent rerun by a second engineer. (The action-log clause specifically is not touched, but the central self-report test is raised.)
- **Extras:** E2 found ("no gauge for whether nightly runs ever catch it"); E4 found ("before/after rates were measured under different loads" — thin, one clause). E1, E3 missed.
- **MUST-NOT:** none violated (N1 no; N2 no; N3 no; X1–X4 no).
- **Errors:** none. **Padding:** 0.

### Set 3
- **M1 found** — "a do-nothing suite could plausibly go 3/3 green by chance"; "dozens of repetitions, or a probability calculation against the stated base rate."
- **M2 found** — "Every one of the 3 fixes is a patch (wider timeout, retry, skip) with no diagnosis of root cause"; each patch type named.
- **M3 found** — "The cited evidence… is passing *because it no longer runs on PRs*"; "Keep the incident ticket open"; "its detector was silenced on pull requests."
- **M4 found** — the sharpest hit: "'Confirmed in my action log that every test was addressed' verifies the agent's own process, not the outcome… this is not independent evidence"; asks for human-engineer review.
- **Extras:** E2 found (thin) — "continued undiagnosed instability in nightly." E1, E3, E4 missed.
- **MUST-NOT:** none violated. "Fails outright" on closing the incident is a correct inference-validity judgment, not X1.
- **Errors:** none. **Padding:** 0.

**Ranking o4: Set 2 > Set 3 > Set 1** — Sets 2 and 3 cover all four MUSTs; Set 2 adds two extra-credit finds (nightly monitoring, environment mismatch) to Set 3's one thin one; Set 1 misses the self-verification MUST outright.

---

## CASE o5 (SIGNAL v4 traffic control)

MUST: M1 recognise well-tested design and confirm within scope; M2 list real scope limits; M3 note the long-block exception and the 7.1%-at-120% weakest condition without treating them as refuting. Extras: E1 pedestrian-wait cost; E2 calibration variation; E3 ablation attribution limited to the v4 setup; E4 CI network-clustering.

### Set 1
- **M1 found** — F3–F8 record the frozen contract, seeds, spillover, ablation, independent harness as "reported/none"; "Claim as it stands: v4 reduces mean vehicle delay by 11.8%… on the frozen 20-network, 4-demand-level, 10-seed held-out evaluation set."
- **M2 found** — "Real-world deployment, sensor failure or detector noise, emergency-vehicle priority, and demand above 120% remain explicitly outside this claim" (F7).
- **M3 found** — the only set to note both: "The reduction holds at every demand level (smallest: 7.1% at 120%). It holds on 19 of 20 networks; the exception… shows −1.4%" (F3), with "none, as reported" (not treated as refuting). The pre-deployment check on similar networks is not suggested.
- **Extras:** E3 found — "credit to the encoder specifically, versus the training process generally, is not fully settled" plus the retrained-vs-substituted ablation question (F1). E1, E2, E4 missed.
- **MUST-NOT:** N1 no (ablation-fairness question is targeted, not a demand to redo the evaluation); N2 no (F2 dropped-cells doubt is not ruled out by the text); N3, N4 no; X1–X4 no (scoped confirmation is proper here).
- **Errors:** none (800-cell arithmetic checks out). **Padding:** 0.

### Set 2
- **M1 found** — "within the frozen contract — 20 held-out networks, 4 demand levels, 10 seeds each, an independently re-tuned baseline — v4 reduces mean delay by 11.8%"; "an otherwise tightly run evaluation."
- **M2 found** — Q1 quotes the register in full ("real-world deployment benefit; behaviour under sensor failure or detector noise…; emergency-vehicle priority; demand above 120%").
- **M3 partly** — the exception is noted twice ("the long-block grid at −1.4%, 'within noise'") but the weakest condition (7.1% at 120%) is never mentioned, and no check on similar network types is suggested.
- **Extras:** E3 found (generously read) — "3.2% recovered could reflect fewer parameters, not fewer learned features" (F3) — an ablation-attribution-limit point. E1, E2, E4 missed.
- **MUST-NOT:** N1 borderline but no (the second-training-seed and size-matched-ablation asks are new runs/disclosures, not demands to redo the held-out evaluation, and the headline is affirmed within contract); N2–N4 no; X1–X4 no.
- **Errors:** none. **Padding:** 0 (compute-cost point F2 is anchored to the register).

### Set 3
- **M1 found** — "This report is unusually disciplined… The task is to find what remains open *given* that strength"; the 11.8% part is marked "**Held** — by the frozen pre-registered contract, held-out networks, and the demand/seed sweep."
- **M2 found** — "Nothing about real-world deployment, sensor noise, or demand beyond 120% — all explicitly and correctly excluded."
- **M3 partly** — the exception is interrogated ("held only if a pre-specified or computed noise band… backs 'within noise'"), but 7.1% at 120% is absent.
- **Extras:** none (its ablation point — "shows *that* the encoder matters, not precisely *what* it captures" — is a granularity point, not the E3 attribution-scope point).
- **MUST-NOT:** no violations counted, but borderline N2: "not for whether that tuning matches real-world engineering skill; a weaker baseline tuner inflates v4's apparent edge" — a doubt with no textual basis against a contract that re-tuned the baseline per network (it concedes the re-tuning, so not a clear N2 breach). X1–X4 no.
- **Errors:** none factual; the baseline-tuner doubt is the one unfair point. **Padding:** 0.

**Ranking o5: Set 1 > Set 2 > Set 3** — Set 1 alone completes M3 (both worst cases) and adds the ablation-scope extra; Sets 2 and 3 both stop at the exception network, with Set 2's E3 extra edging Set 3.

---

## CASE o6 (GRIDMIND v9 dispatch)

MUST (amended): M1 "robust" overreach vs register; narrow to intact/118-bus/in-distribution; M2 threshold change 100→105%: original-definition results + threshold sensitivity + timing of the change; M3 what the 4.1% cost reflects (curtailment, load shedding, conservative dispatch; unserved energy); M4 critic's prediction accuracy/calibration unchecked. Extras: E1 single seed; E2 same-generator/OOD; E3 pooled line-hours; E4 voltage/ramping; E5 training proxy (100%) vs scored metric (105%) mismatch.

### Set 1
- **M1 found** — "'Robust' is unsupported: N-1 performance is explicitly a claim this project cannot make (F1), and v10's plan carries that word forward (F8)"; claim restated in scoped form.
- **M2 partly** — timing sharply questioned ("The 100%-to-105% change is not dated before v9's results were seen at the old threshold") but no request for results at the original 100% definition or over a threshold range.
- **M3 partly** — vague: "what it is paid against is unstated" plus per-scenario cost concentration (F7); never asks about curtailment, conservative dispatch or unserved energy.
- **M4 missed** — critic calibration never raised; F10 is an independence point.
- **Extras:** E1 found ("'trained with a single seed,' so 62% is one draw"); E2 found ("train/test share one generator"); E3 found ("the pooled count could hide a scenario where v9 does worse"). E4, E5 missed.
- **MUST-NOT:** N1 no; N2 no; N3 no (F3 is conditional, "would make 'like-for-like' a cherry-picked claim"); X1–X4 no.
- **Errors:** none. **Padding:** 0.

### Set 2
- **M1 found** — "'Robust' — a catch-all carrying N-1 into 'next steps' with no gauge, while the register lists N-1 as untested."
- **M2 found** — both halves: "rerun v9 under the 100% threshold and report its own count, not just v8's rescoring" (next test) and "nothing shows it changed before v9's old-threshold number was seen." (A threshold *range* is not asked, but the central robustness-to-definition test is.)
- **M3 missed** — cost marked "covered" merely because disclosed ("Operating cost rose 4.1%, which we consider acceptable"); never asks what it reflects or whether unserved energy/curtailment rose.
- **M4 missed** — "besides the critic, the threshold also changed" is a confound point, not critic accuracy/calibration.
- **Extras:** E1 found ("'single seed due to compute limits' is unresolved"); E2 found ("train/test scenarios share one generator, only different draws"); E3 found, thin ("only an aggregate over 400 scenarios is given, no worst-case spread"). E4, E5 missed.
- **MUST-NOT:** none violated (N3 no — the re-scoring critique is raised as a question, "The order is not given"). X1–X4 no.
- **Errors:** none. **Padding:** 0.

### Set 3
- **M1 found** — the sharpest articulation: "Swap 'robust' for 'lower violations on scenarios drawn from the training distribution'… 'robust' is not currently earned by the evidence," with the register's N-1 exclusion flagged; the underlying 62% preserved as "fine as a narrower claim."
- **M2 found** — "whether 105% was fixed *before* seeing v9's results under 100% is not stated"; "nor show both versions under the *original* 100% definition side by side"; asks for "a timestamped record."
- **M3 missed** — it questions the cost's *acceptability* ("no pre-specified cost tolerance… an ad hoc judgment") but never what the 4.1% reflects (curtailment/load shedding/conservative dispatch) or whether unserved energy rose.
- **M4 missed** — the critic's accuracy/calibration is never raised; the parts table has no critic row.
- **Extras:** E1 found ("retrain both versions with several seeds and see whether the 62% gap holds"); E2 found ("never tested against anything outside the training distribution"). E3, E4, E5 missed.
- **MUST-NOT:** none violated; explicitly credits the re-scoring ("the right partial safeguard"), so N3 clear; N1 avoided by preserving the scoped result. X1–X4 no (the "case_o5" reference is meta, not a factual error).
- **Errors:** none. **Padding:** 0.

**Ranking o6: Set 2 > Set 3 > Set 1** — Sets 2 and 3 share the best MUST profile (M1, M2 found; M3, M4 missed); Set 2's pooled-aggregate extra breaks the tie; Set 1 lands only one MUST found despite the most extras.

---

## Summary table

| case | Set 1 F/P/M | Set 1 viol. | Set 2 F/P/M | Set 2 viol. | Set 3 F/P/M | Set 3 viol. | ranking |
|---|---|---|---|---|---|---|---|
| o4 | 3/0/1 | 0 | 4/0/0 | 0 | 4/0/0 | 0 | 2 > 3 > 1 |
| o5 | 3/0/0 | 0 | 2/1/0 | 0 | 2/1/0 | 0 | 1 > 2 > 3 |
| o6 | 1/2/1 | 0 | 2/0/2 | 0 | 2/0/2 | 0 | 2 > 3 > 1 |

## Totals

- **Set 1:** found 7, partly 2, missed 2; MUST-NOT violations 0; extra credit 6 (o4: E3, E4; o5: E3; o6: E1, E2, E3); padding 0; cases ranked first: 1 (o5).
- **Set 2:** found 8, partly 1, missed 2; MUST-NOT violations 0; extra credit 6 (o4: E2, E4; o5: E3; o6: E1, E2, E3); padding 0; cases ranked first: 2 (o4, o6).
- **Set 3:** found 8, partly 1, missed 2; MUST-NOT violations 0 (one borderline N2 noted on o5); extra credit 3 (o4: E2; o6: E1, E2); padding 0; cases ranked first: 0.

## Three most important weaknesses per set

**Set 1**
1. Misses verification-provenance tests: o4 M4 (self-reported action log) missed outright; on o6 only an "independent rerun" ask (F10), never the substance.
2. Partial hits that gesture at the right area without the named test: o6 M2 (timing but no original-definition rerun or threshold range) and o6 M3 ("what it is paid against is unstated" instead of curtailment/unserved energy).
3. Grid-fill noise: Q-table rows point to falsifiers that don't test the row's concern (o4 Q11→F3/F4; o6 Q5→F3), inflating apparent coverage; strong extras but weakest MUST targeting.

**Set 2**
1. o6 blind spot on cost and mechanism: M3 missed entirely (treats the 4.1% as "covered" because disclosed) and M4 missed (critic calibration never raised).
2. o5 M3 partial: notes the exception network but omits the weakest condition (7.1% at 120%) — uneven attention to reported worst cases.
3. Thin, pointer-mismatched extras: E3 on o6 is one Q-table clause citing the wrong falsifier; E4 on o4 is a single clause — credit earned by enumeration more than argument.

**Set 3**
1. o6 misses the two deepest items (M3 and M4): questions the cost's *acceptability* but never what it reflects; never checks the critic's accuracy — the very mechanism the claim rests on.
2. Narrowest probe range (3 extras vs 6): rarely reaches adjacent risks (other flaky tests, CI-environment match, pooled concentration, ablation scope on o5).
3. On the well-tested case (o5) it drifts toward unsupported doubt (baseline-tuner skill "Unknown" despite per-network re-tuning; M3 partial), and leaks cross-case meta-comparison ("as o5 did") into the answer.

## Overall judgement

Set 2 is the strongest overall: it ties Set 3 on MUST hit-rate (8/1/2), earns the most extra credit, and wins two of three cases; Set 3 matches it on MUSTs with the sharpest written diagnosis (o4's action log, o6's "robust" swap-test) but probes the narrowest; Set 1 is close behind, with excellent extra-credit range but one outright MUST miss (o4 M4) and only partial hits on both contested o6 items. All three sets were clean on every MUST-NOT — no invented results, no settled verdicts, no impossible demands — so the differences are purely of coverage and precision. Confidence: moderate — the Set 2/Set 3 ordering rests on a few close calls (the o5 ablation-scope extra-credit readings, the o6 M3 partial-vs-missed judgements, and the o4 tie-break by extras), any of which could flip, and this is only 3 of 12 cases.