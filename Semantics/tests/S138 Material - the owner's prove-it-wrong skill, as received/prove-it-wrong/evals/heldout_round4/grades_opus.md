# Grading of cases g1–g6 (Set 1, Set 2, Set 3)

Grader: Opus 5.5. Graded against the marking lists in `marking.md` Part A, **as amended** (the amended MUST items replace the originals). F = found, P = partly, M = missed. MUST-NOT: N-items are case-specific; X1–X4 are common. Following the general amendment, a MUST item counts as found when the answer raises the central test with a case-specific reason, even if not every sub-point is named.

---

## case_g1: Marsh Street bus priority (6 MUST)

### Set 1
| Item | Mark | Evidence |
|---|---|---|
| M1 isolate the scheme from signal retiming and fare freeze, for both results; comparison corridor | F | F1: "A comparable route untouched by the bus lane, over the same 8 weeks, shows a travel-time and boarding change of similar size, since the citywide signal-retiming and the fare freeze ran over the same period" (C1, C2) |
| M2 diversion vs absorption; only Marsh St measured; no baseline speed | F | F6: "delay on parallel side streets… could be delay displaced nearby"; F8: "a 2.4 km/h fall is undefined… against the pre-lane mean car speed" |
| M3 baseline / seasonality / persistence | P | F2 novelty fading, "weeks 9-16"; seasonality, weather and holidays in Feb vs Mar–May are not raised |
| M4 redistribution, not new riders; not unique riders | P | F7: "a change in which trips or stops the automatic passenger counters covered", which is a counter-coverage point, not redistribution from other routes or modes |
| M5 survey selection or comparability of the 71% baseline | P | "Routine checks: … the April survey's response rate and wording", a vague cousin of the point |
| M6 extrapolation to corridors with unestablished baselines | P | F4: "the 15-20% projection is untested outside Marsh Street", with no reason about differing baselines or demand |

MUST-NOT: none violated. Extra credit: E1 (untreated comparison corridor, F1 / next test). Errors: F6 measures "delay" in km/h (wording). Padding: 3 (F3 segment breakdown, F5 pre-dated plan, the mostly "does not apply" Q-table).

### Set 2
| Item | Mark | Evidence |
|---|---|---|
| M1 | F | F1 retiming rival for C1/C3, F2 fare-freeze rival for C2; "find a corridor touched by retiming but not the lane" |
| M2 | F | F3: "GPS speeds on the parallel street one block over fall more than 2.4 km/h… diverted traffic"; the baseline-speed point is absent |
| M3 | P | F5: "A second 8-week window (weeks 9–16) shows most of the gain gone"; no seasonality |
| M4 | M | Instead marks Q13 "covered … complete counts", the opposite of the point |
| M5 | M | survey not mentioned |
| M6 | F | F6: "Ferndale's and Eastgate's baseline ridership and traffic differ from Marsh Street's" |

MUST-NOT: none violated. Extra credit: E1. Errors: "travel time and boardings rose by the stated amounts" (travel time fell); counters treated as complete and unproblematic (Q7/Q13 "covered"). Padding: 3 (F4, F7, generic Flip/Q-table rows). The "pull" (a lane that cuts bus time 21% yet costs cars little hints that retiming carries both) is a good case-specific point.

### Set 3
| Item | Mark | Evidence |
|---|---|---|
| M1 | F | "A concurrent comparison group — routes exposed to retiming/fare freeze but not bus priority"; next step pulls "ridership and GPS-speed data" for untreated routes |
| M2 | P | "held only if 2.4 km/h is the right threshold for 'not material'"; diversion to other streets is never raised |
| M3 | P | "a longer pre-period than one month"; "anticipatory ridership growth from publicity before 12 March" |
| M4 | M | not raised |
| M5 | M | satisfaction listed only as "Given" |
| M6 | F | "Ferndale/Eastgate, which likely differ in baseline congestion, bus frequency, and stop spacing" |

MUST-NOT: none violated. Extra credit: E1. Errors: "one month" pre-period is right for the travel-time baseline but wrong for boardings (eight weeks before). Padding: 3 (Flip, Reverse, "Check the patches: N/A"). Separating the lane from signal priority is a sensible extra point.

**Ranking g1: Set 1 > Set 2 > Set 3.** Set 1 touches all six items (2F/4P) with no errors. Set 2 has more full hits (3F) but misses two and calls the counters "covered". Set 3 misses diversion, redistribution and the survey.

---

## case_g2: Futures momentum backtest (4 MUST; N4 added)

### Set 1
| Item | Mark | Evidence |
|---|---|---|
| M1 execution realism / capacity / same-bar fill | F | F6: "settlement-price fills may not be achievable for a weekly-rebalanced entry"; F7: "capacity test, sizing ~45 contracts per signal against each contract's actual volume" |
| M2 survivorship of current-listing universe | F | F1: "Rebuilding the universe from each year's own liquidity ranking, not today's list" |
| M3 in-sample lookback and filter | F | F2 frozen OOS / walk-forward for lookback; F3 filter "fit excluding 2020" |
| M4 robustness evidence descriptive, no OOS / per-sector | F | F2 "second non-overlapping window (e.g. 2003-2013)"; F5 worst year "loss concentrated in one sector"; replication of code not raised |

MUST-NOT: none (F8 asks about "a regime with structurally different rates" without characterising 2013–2023 as fact, so N4 is not violated). Extra credit: E2 (historical-liquidity universe + capacity test). Errors: F5 wording ("worst of the '10 of 11' profitable years… shows a loss") is muddled. Padding: 2 (F4 buy-and-hold rival, Q-table).

### Set 2
| Item | Mark | Evidence |
|---|---|---|
| M1 | F | F6: "At $250M, ~45 contracts/signal, realistic market-impact slippage drops Sharpe below 1.2" |
| M2 | F | F3: "Universe fixed to contracts liquid in 2013 (incl. delisted since)" |
| M3 | F | F1 walk-forward lookback; F2 filter post-2020 |
| M4 | F | F4 sector share of losing year; Q11 "'available on request' is an offer, not a run; nobody outside the team ran it"; Q9 "one path, correlated years" |

MUST-NOT: **X2 violated**. F6 has status "blocked" with receipt "team reruns with an impact model; passes at 1.5+", a result the case does not report (close to N2 as well). Extra credit: E2. Errors: F7 asks for "a dated plan… predates 2013", which is not meaningful for a backtest built now; Q11 cites F3 for the replication point (wrong cross-reference); C5 (capital) is not listed as a claim. Padding: 4 (F5, F7, Flip, Q-table rows).

### Set 3
| Item | Mark | Evidence |
|---|---|---|
| M1 | F | "settlement-price fills with commission but no slippage/impact"; "held only if $250M/45 contracts avg doesn't move the market"; capacity study "on the less-liquid contracts" |
| M2 | F | "current liquidity, not liquidity-at-each-historical-date, risks survivorship bias" |
| M3 | F | filter "confirming a fitted part on the case it was fitted to"; lookback "best of 4 in-sample candidates, no sensitivity numbers given" |
| M4 | F | "Ten profitable years… is not ten independent tests"; "'No dependence on any single sector' is an output check"; OOS on 2000–2012 / 2024 |

MUST-NOT: **N4 violated (mild)**: "Ten profitable years in one broadly trending decade for trend-following assets" states the macro character of the sample as fact and uses it to discount the result; the crowding point ("a common trend-following/momentum factor shared across many CTAs over this decade") is also outside fact. Extra credit: E2. Padding: 2 (Reverse N/A, crowding point).

**Ranking g2: Set 1 > Set 3 > Set 2.** All three find all four items. Set 1 is clean and alone has the same-bar fill point. Set 3's breach is a mild N4. Set 2 invents a rerun result.

---

## case_g3: Fibre concrete trial (5 MUST after amendment; the well-tested case)

### Set 1
| Item | Mark | Evidence |
|---|---|---|
| M1 recognise the strong design | M | Never says so. The Q-table marks blinding, randomisation and third-party testing nowhere as covered, and F3/F4/F6/F7 add doubts instead |
| M2 accept 14% within scope, separate from striking | F | "fibre raised 28-day compressive strength by about 14%… Whether the early-age (7-day) strength is enough… is not shown" |
| M3 scope limits | P | F8 durability/fatigue as stated limits; "standard C25/30 footpath blend"; no dosage, supplier or static-only point, and nothing on modest flexural vs crack control |
| M4 cost-conditioned proposal sensible | M | F5 instead attacks the recommendation (trip hazard) |
| M5 aim mismatch: no early-age results | F | F1: "The 7-day compressive strength… the age that governs formwork striking… the trial's stated purpose is unaddressed by the 28-day figures" |

MUST-NOT: **X2 violated**. F4 "Any of the 120 cast cylinders": the case gives 120 loads, not a cylinder count (several ages × temperatures). N1/N2 not violated: F7's demand for a second trial is a replication suggestion, not a demand to redo the blinded, multi-plant design. Extra credit: E3 (F2 "same water-reducer dose… no fibre", a good point). Padding: 3 (F4, F7, Q-table).

### Set 2
| Item | Mark | Evidence |
|---|---|---|
| M1 | F | Q6/Q9/Q10/Q11 "covered": "alternating in randomised order", "blinded to mix identity", "Three batching plants… 60 per arm", "accredited third-party laboratory" |
| M2 | F | "the 28-day compressive (14%) and flexural (7%) gains hold as reported… The recommendation… is not yet supported by the early-age data" |
| M3 | P | Q1 "scoped to this C25/30 footpath blend and the tested 5–35°C range"; durability stated as exclusions; no dosage/supplier |
| M4 | F | Q12 "covered": "Cost is EUR 6.80/m³ higher, so we propose using the fibre only where earlier striking is needed" |
| M5 | F | F1: "7-day (early-age) compressive gain, the figure the striking decision needs"; Q7 "only 28-day and flexural results are given" |

MUST-NOT: none violated. Extra credit: E3 (F3). Padding: 2 (Flip, Q-table rows). The flexural "add a job" point is sound.

### Set 3
| Item | Mark | Evidence |
|---|---|---|
| M1 | F | "This design is unusually strong: randomised order, matched slump, blinded third-party testing, three plants, three cure temperatures" |
| M2 | F | "28-day strength gain: Held"; striking treated separately |
| M3 | F | "4 kg/m³ dosage… no neighbouring dosage"; "the specific fibre product"; lab cylinders vs "full-scale dispersion"; durability out of scope |
| M4 | M | not mentioned |
| M5 | F | "no data point in the 1–3 day range where the decision actually lives"; "Add early-age (12–72h) maturity… testing" |

MUST-NOT: **X2 violated**. "footpaths are commonly salted directly for pedestrian safety" is an outside fact used to contest the report's scope statement (it stops short of N3, since it is framed as a check to make). Errors: "Covered: … 7/28/90-day tests" and "earliest-tested point (7 days)" treat the 7-day results as existing data, when the case does not report them. Extra credit: none. Padding: 1 ("Check the patches: N/A").

**Ranking g3: Set 2 > Set 3 > Set 1.** Set 2 recognises the strong design and the cost conditioning, finds the aim mismatch and the w/c confound, and has no breach. Set 3 is close but misses M4 and adds an outside fact. Set 1 never acknowledges the design's strength and invents a cylinder count.

---

## case_g4: Beetroot nitrate time trial (4 MUST)

Key case fact: **beetroot first, placebo second.**

### Set 1
| Item | Mark | Evidence |
|---|---|---|
| M1 fixed order confounded with session | F | F1: "with every rider taking beetroot first and placebo second, a trial-order or learning effect cannot be told apart from nitrate" (correct order; no wrong-direction claim) |
| M2 broken blinding (taste; coach recorded outcome) | F | F2: "drinks indistinguishable by taste or colour and a timekeeper unaware… the coach who designed the study, knew the assignment, administered the drinks and ran the visible stopwatch" |
| M3 self-report diet diary | F | F4: "'no protocol violations' rests on the riders' self-report, not an independent check" |
| M4 sample / single trial / CI lower bound vs ~2% | P | F3: "one cohort of 14, tested once, is a single draw"; F6 mentions the 0.6% bound but not against the "meaningful ~2%" claim |

MUST-NOT: none violated. Extra credit: E1 (counterbalanced order, indistinguishable drinks, blinded timekeeper). Padding: 2 (F5 individual riders, Q-table).

### Set 2
| Item | Mark | Evidence |
|---|---|---|
| M1 | P | Raises the fixed order, but on the wrong fact and with the reasoning the amendment refuses to credit: "a fixed order (beetroot always second) cannot separate nitrate from a practice/familiarity effect" |
| M2 | F | F2 blind timer; F3: "'unmistakable in taste and colour' means the riders were not blinded either" |
| M3 | M | Q13 "covered: 'diaries showed no protocol violations'", which accepts the diary |
| M4 | P | F4: "one cohort, one week, one order" |

MUST-NOT: **X2 violated**: "beetroot always second" (repeated in the summary and the hard-to-vary section) contradicts the case. Also "ran the stopwatch himself" assumes the coach's gender. Extra credit: none (no masked placebo). Padding: 3 (Q-table, day-of-week Poke, Flip).

### Set 3
| Item | Mark | Evidence |
|---|---|---|
| M1 | P | "fixed order (beetroot always second) … perfectly confounded with any learning/familiarity/pacing effect of a second attempt". The order is wrong, and so is the central "single fatal gap" reasoning |
| M2 | F | administrator/timer "Not held"; participant blinding "Not held — taste/colour gave it away" |
| M3 | M | "Diet-diary check: Held, narrowly — rules out gross dietary protocol violation", which accepts the diary |
| M4 | M | sample size, clustering and the CI vs ~2% are not raised |

MUST-NOT: **X2 violated** (same reversed order). X1 not violated: "treat the ~2% figure as unestablished" is a fair reading of the evidence. Extra credit: E1 ("opaque, flavour-matched drinks; automated timing"). Padding: 1 (Flip).

**Ranking g4: Set 1 > Set 2 > Set 3.** Set 1 has the order right, finds the diary point and has no breach. Sets 2 and 3 both reverse the order and accept the diaries. Set 2 at least notes the single cohort.

---

## case_g5: Personalised voucher A/B test (5 MUST)

### Set 1
| Item | Mark | Evidence |
|---|---|---|
| M1 early stopping | F | F1: "stopping halfway at first significance is optional stopping, which inflates the apparent effect" |
| M2 contamination; "conservative" unverified | F | F2: "'conservative' is asserted from an unquantified anecdote, not measured in either direction"; F7 redemption log |
| M3 metric not netted (discount, returns, cannibalised margin) | F | F8: "Revenue per visitor net of the 10% discount's cost… a revenue-per-visitor rise can coexist with a margin fall" (returns not raised) |
| M4 operating point / data window (~2 weeks, Black Friday run-up, pull-forward) | P | "over the roughly two weeks actually run"; Black Friday seasonality and pull-forward are not raised |
| M5 extrapolation to EU | F | F3: "the 5-6% EU-wide figure is projected from one UK, one-segment test" |

MUST-NOT: none violated. Extra credit: none (the next test has a fixed horizon and discount netting but no leak-proof code). Good extra point: F4, the lift applies only to the flagged subgroup. Padding: 2 (F6 weekly breakdown, Q-table).

### Set 2
| Item | Mark | Evidence |
|---|---|---|
| M1 | F | F1; "almost any test, watched continuously and stopped the moment it crosses p<0.05, crosses it even with no real effect" |
| M2 | F | F2; "'if anything' can absorb any surprising result without being checked" |
| M3 | F | F5: "'checkout totals at order time' may not net out returns"; Q12 "returns or cancellations" |
| M4 | F | "over roughly half of a planned 4-week test"; Pull: "a demand spike big enough to justify urgency is big enough to be doing some of the work in the numbers" |
| M5 | F | F4 "the UK figure may not transfer" |

MUST-NOT: **X2 violated**. F4 status "blocked", receipt "marketing runs a matched pilot in one EU store; passes within 5–6%", a pilot result not in the case. Errors: F3 compares a "week-4 lift" that was never run; Q1 calls it "this 4-week window". Padding: 2 (Flip, Q-table).

### Set 3
| Item | Mark | Evidence |
|---|---|---|
| M1 | F | "optional stopping on a significance threshold inflates the false-positive rate" |
| M2 | F | "could inflate variance, bias toward null, or… bias either way"; "check redemption logs" |
| M3 | F | "top-line revenue lift could be partly or wholly offset by discount cost" |
| M4 | P | "without Black-Friday-adjacent timing", but it believes the full four weeks were run (see below) |
| M5 | F | "EU transferability — different markets, currencies, competitive context" |

MUST-NOT: **X2 violated**: "Recompute significance on the full 4-week data… checkable retroactively from the logged daily data" assumes a control-arm data set the case does not give (the test was stopped halfway and the banner rolled out). Extra credit: none. Padding: 1 (Flip).

**Ranking g5: Set 1 > Set 2 > Set 3.** Set 2 has the most full hits (5F) but invents a pilot result. Set 1 gives a clean 4F/1P. Set 3 builds its main next step on data that probably does not exist.

---

## case_g6: XSS remediation (6 MUST after amendment)

### Set 1
| Item | Mark | Evidence |
|---|---|---|
| M1 scanner never shown to detect seeded XSS | F | F1: "'zero findings' from a scanner never shown to catch a planted XSS shows nothing" |
| M2 authenticated crawl | F | F2: "omit… auth-only, API, PDF, email or admin pages" |
| M3 independence | F | F3 "run by a tester outside the fix's own team"; next test "a reviewer outside the security team" |
| M4 time horizon / lagging signals | F | F4: "Given 4 payouts over 6 months… the chance of 0 in a random 6-week window exceeds 20%… close to what the old rate gives by chance" |
| M5 displacement outside the template layer | P | F2/F6 non-template surfaces and inventory, framed as crawl coverage rather than sinks outside the SAST-checked layer |
| M6 retest only original payloads | F | F3: "A fresh set of mutated payloads, different from the original Q2 set" |

MUST-NOT: none violated. Extra credit: E1 (seeded scan + independent retest, with auth pages in F2), E2 (F5: "the recommendation is made without testing the library on that codebase"). Errors: the summary's "held if… ability to catch a seeded XSS is unshown" inverts the logic. Padding: 1 (Q-table).

### Set 2
| Item | Mark | Evidence |
|---|---|---|
| M1 | F | F1 planted unseen payload; "swap it for a scanner carrying no XSS payloads and it reports the same zero" |
| M2 | F | F2: "page outside the '1,100+' crawl (post-14 June, or behind auth)" |
| M3 | F | F3: "the check that built the fix also graded it" |
| M4 | P | F5 and catch-all: "zero XSS reports could mean fewer lookers"; the six-week window is not called too short |
| M5 | M | sinks outside the template layer not raised |
| M6 | F | F4; "a payload one step different is untested" |

MUST-NOT: **X2 violated**: "The hand re-run of the 4 Q2 payloads": the number of Q2 payloads is not given (the "four" is bounty payouts). Extra credit: E1 (F1 + F3). Padding: 2 (Q-table rows, Flip).

### Set 3
| Item | Mark | Evidence |
|---|---|---|
| M1 | P | "DAST/SAST 'no reason to doubt coverage' — Unknown — asserted; scanners have known blind spots", with no seeded-calibration test |
| M2 | F | "uncrawled or authenticated/dynamic surfaces" |
| M3 | F | "the same team wrote and verified the fix… no independent check is offered" |
| M4 | P | bounty "Held if… overall submission volume… stayed flat"; "a few weeks of scanner silence" |
| M5 | F | "vendor pages, email templates, PDFs, error pages reflecting input"; "DOM-based/mutation XSS" |
| M6 | F | "try a payload class the sanitiser was never built against (e.g. mutation XSS, Unicode-normalisation bypass)" |

MUST-NOT: none violated (the "known blind spots" remark is general, not a claim about this scanner's configuration). Extra credit: E2 ("assumes the fix transfers to different sinks/frameworks"). Errors: "Check the patches: fails", which treats the sanitiser itself as an ungauged catch-all, is muddled reasoning. Padding: 1 (that check).

**Ranking g6: Set 1 > Set 3 > Set 2.** Set 1 finds 5 of 6 plus both extras, with the best bounty-rate reasoning. Set 3 has no breach but no seeded-scanner test. Set 2 misses displacement and invents a payload count.

---

## Summary table

| Case | Set 1 MUST F/P/M | Set 1 MUST-NOT violated | Set 2 MUST F/P/M | Set 2 MUST-NOT violated | Set 3 MUST F/P/M | Set 3 MUST-NOT violated | Ranking |
|---|---|---|---|---|---|---|---|
| g1 | 2/4/0 | 0 | 3/1/2 | 0 | 2/2/2 | 0 | 1 > 2 > 3 |
| g2 | 4/0/0 | 0 | 4/0/0 | 1 (X2) | 4/0/0 | 1 (N4) | 1 > 3 > 2 |
| g3 | 2/1/2 | 1 (X2) | 4/1/0 | 0 | 4/0/1 | 1 (X2) | 2 > 3 > 1 |
| g4 | 3/1/0 | 0 | 1/2/1 | 1 (X2) | 1/1/2 | 1 (X2) | 1 > 2 > 3 |
| g5 | 4/1/0 | 0 | 5/0/0 | 1 (X2) | 4/1/0 | 1 (X2) | 1 > 2 > 3 |
| g6 | 5/1/0 | 0 | 4/1/1 | 1 (X2) | 4/2/0 | 0 | 1 > 3 > 2 |

## Totals (30 MUST items)

| Set | Found | Partly | Missed | MUST-NOT violations | Extra credit | Padding | Cases ranked first |
|---|---|---|---|---|---|---|---|
| Set 1 | 20 | 8 | 2 | 1 | 6 | 13 | 5 (g1, g2, g4, g5, g6) |
| Set 2 | 21 | 5 | 4 | 4 | 4 | 16 | 1 (g3) |
| Set 3 | 19 | 6 | 5 | 4 | 4 | 9 | 0 |

No set triggered X1, X3 or X4. Padding is counted per point; the long "does not apply" Q-tables in Sets 1 and 2 are counted as one padding point per case.

## Three most important weaknesses of each set

**Set 1**
1. On the well-tested case it does not recognise the strength of the design or the sensible cost conditioning. It adds doubts instead (g3: M1 and M4 missed).
2. It often raises the right area only in a weak form. Examples: novelty instead of seasonality, counter coverage instead of redistribution, a "routine" survey check (g1), no Black Friday operating point (g5), displacement framed as crawl coverage (g6).
3. Occasional invented detail and garbled logic: "120 cast cylinders" (g3, X2) and an inverted "held if" summary (g6). There is also long Q-table padding in every case.

**Set 2**
1. It invents results in "blocked" ledger rows ("passes at 1.5+" in g2, "passes within 5–6%" in g5) and invents or misreads facts ("beetroot always second" in g4, "the 4 Q2 payloads" in g6).
2. It marks evidence "covered" too readily, which suppresses real tests: APC counts "complete" (g1), diet diaries "covered" (g4).
3. It has the most generic padding (Flip / catch-all sections and many Q-table rows). It also misses a case-specific item where other sets found it: displacement outside the template layer (g6).

**Set 3**
1. It misreads case facts and builds central conclusions on them: the reversed drink order is its "single fatal gap" (g4), it assumes full four-week data exists (g5), and it treats 7-day results as reported (g3).
2. It brings in outside facts as premises: "footpaths are commonly salted" (g3), "one broadly trending decade" / CTA crowding (g2, N4).
3. It covers less ground on multi-item cases: diversion, redistribution and the survey are missed (g1), and so are the diet diary and sample size (g4) and the seeded-scanner calibration (g6).

## Overall judgement

Set 1 is the strongest. It has the fewest misses (2), only one MUST-NOT violation and the most extra credit, it ranks first on five of six cases, and it gets the case facts right where the other two slip. Its main failure is not crediting a well-designed trial (g3). Sets 2 and 3 are close on MUST coverage (21 vs 19 found), and each has four violations. Set 2 does slightly better on coverage and handled g3 best, but it invents results. Set 3 is the most concise but misreads facts more often. I am fairly confident (about 75%) that Set 1 ranks first. I am much less confident about the order of Sets 2 and 3, which is close to a tie.
# Grading — cases o1 to o6 (Opus 5.5 marking lists with GLM amendments)

Grading is strict against the amended lists in `marking.md`, Part B. F = found, P = partly, M = missed. The common MUST-NOTs (X1–X4) and the case-specific N items are checked for each answer. Any stated fact the case does not give counts as X2. Under the general amendment, a MUST item is awarded when the answer raises its central test with a case-specific reason.

---

## case_o1 — rgn4 and zebrafish fin regeneration

### Set 1
| Item | Grade | Evidence |
|---|---|---|
| M1 single allele / off-target | F | F1: "A second, independent mutant allele (different sgRNA or exon) or an mRNA-rescue … a single CRISPR line cannot rule out an off-target mutation" |
| M2 mechanism step not measured | F | F4: "A proliferation assay (EdU/BrdU) in the 3-dpa blastema"; F5: "Wound-epidermis formation, blastema migration, or apoptosis rate … no rival mechanism … ruled out" |
| M3 measurement not blind | F | F2: "re-measurement … by someone blind to genotype … same student who did the amputations and genotyping" (does not ask for a fixed measurement rule, but the central point is there) |
| M4 single time point | F | F3: "Length measured at 14 or 30 dpa … to rule out a closing delay" |

Extra credit: E1 (F6: "all 48 fish come from one pair; one clutch is one draw"), E4 ("inferred from expression data and domain homology, not a proliferation assay"). **2.**
MUST-NOT: none violated. N1, N2 and N3 are clean; the answer never treats the sibling design as a flaw. On F7, "assessed by inspection only" is a fair reading of "morphologically normal", so it is not counted as X2.
Errors: none material.
Padding: **3**. These are F7 (a systemic-health assay with only a weak link to the claim), F8 (an outside lab reproducing the result before write-up, which is a generic replication demand) and F9 (individual values, a generic "show the raw data" point). That is 3 of 9 falsifiers, exactly a third, so X3 is not exceeded.

### Set 2
| Item | Grade | Evidence |
|---|---|---|
| M1 | F | F1: "A second, independent rgn4 allele (different sgRNA target) … an off-target or linked mutation could be the real cause" |
| M2 | F | F3: "Proliferation markers (EdU/PH3+) in the 3-dpa blastema … rather than death or migration being the cause" |
| M3 | F | F2: "rescored blind to genotype on the same images … nothing is blinded" |
| M4 | M | No time course anywhere. Q1 even says "does not apply … the claim is stated for this line, this assay, 7 dpa; no wider promise made" |

Extra credit: E1 (F4: "one clutch, one cross is the only genetic draw"), E4 ("inferred from expression and homology, not measured"). **2.**
MUST-NOT: **X2 violated.** Q5 says "only mean and SD" are given, but the case reports means and a p-value, not an SD.
Errors: Q1 says the claim makes "no wider promise" beyond 7 dpa. C1 and C4 claim rgn4 is "required for fin regeneration", which is exactly the wider promise.
Padding: **1** (the "Flip" paragraph is speculative and adds no test).

### Set 3
| Item | Grade | Evidence |
|---|---|---|
| M1 | F | "a second, independent sgRNA/allele … would separate rgn4 from an off-target or linked mutation"; "Re-expressing rgn4 in the mutant should restore regenerate length" |
| M2 | F | "an EdU/BrdU or pHH3 proliferation assay at 3dpa is the missing test"; "consistent with reduced proliferation, increased apoptosis, delayed blastema formation" |
| M3 | F | "Blinded remeasurement of the same images by someone not involved in genotyping" |
| M4 | F | "Does the mutant catch up at later time points (14/21dpa), i.e. is this delayed regeneration or permanently impaired" |

Extra credit: E4 ("A correlative expression pattern plus a domain-homology guess is not evidence of mechanism"). **1.**
MUST-NOT: **X2 violated.** The phenotype row says it is "held by the randomised-sibling, blinded-genotype-by-sequencing design". The case states neither randomisation nor blinded genotyping, and the next row of the answer contradicts it.
Errors: the X2 point above. "Single founder line" is also not stated, though it is a plausible inference.
Padding: 0.

**Ranking o1: Set 1 > Set 3 > Set 2.** Sets 1 and 3 both cover all four MUSTs. Set 1 does so without violations and with more extras, while Set 3 asserts a randomised, blinded design that the case does not give. Set 2 misses the time course and adds an SD.

---

## case_o2 — Harlan induced seismicity

### Set 1
| Item | Grade | Evidence |
|---|---|---|
| M1 densification / completeness | F | F1: "using only the station subnetwork that ran continuously … 'same picker' does not rule this out"; F5: restrict to magnitudes detectable pre-densification; next test: "recompute … the magnitude of completeness" |
| M2 post-hoc radius | F | F2: "A 10 km or 20 km radius, chosen without reference to the post-injection map" |
| M3 natural rival / control region | F | F4: "A comparable field … no injection, over the same 48 months … nothing rules out a broader regional rise unrelated to Harlan's wells" |
| M4 physical link | F | F3: "Monthly injection volume at the three wells correlates with monthly event count … no check that seismicity tracks … injection volume" |

Extra credit: none credited. F3 covers only the injection half of E4, which asks for the series against both densification and injection.
MUST-NOT: none violated. N2 is clean ("addresses only the picker algorithm, not the added stations").
Errors: Q9 says "the Poisson significance is not in question". That overlooks event clustering and aftershocks (E1), so the answer actively waves off a valid test.
Padding: **1** (F6, the overlap of hypocentre depths with the excluded Sutter zone, which has a weak link to the claim).

### Set 2
| Item | Grade | Evidence |
|---|---|---|
| M1 | F | F1: "With the 8 new stations removed"; F3: "Magnitude-of-completeness, computed separately pre/post-2024"; "the picker stayed fixed, but what it listens to (station density) did not" |
| M2 | P | It notes the radius is "a free, post-hoc boundary unless shown not tuned to the result it frames", but proposes no sensitivity test. Q10 points to F2, which is a densification control, not a radius test. |
| M3 | P | F2: "a circle with new station coverage but no well" is the right control, but it is framed only as a densification check. No natural swarm or regional rival is named. |
| M4 | F | F4: "Hypocentres lie within 1–2 km of the well bottoms … required for the pressure-diffusion mechanism" |

Extra credit: none. The "Pull" paragraph mentions improved location quality but uses it for detection, not for events moving across the circle (E2).
MUST-NOT: none violated. N2 is clean in the body, although Q11 marks the "one named picker" as "covered".
Errors: Q11 calls the single picker "covered", which is inconsistent with its own F1/F3 critique.
Padding: **1** ("Flip").

### Set 3
| Item | Grade | Evidence |
|---|---|---|
| M1 | F | "check whether the magnitude of completeness (Mc) dropped after the 2024 station densification … restricted to events above the pre-densification Mc"; "Not held — conflates two different things" |
| M2 | F | "this is circular … Swapping it for a neighbouring radius (10 or 20 km) and checking whether the fold-change survives" |
| M3 | F | "a non-injection control area with the same new stations"; "a coincidental trend … a longer baseline is needed" |
| M4 | F | "Does the explanation predict the observed depth range from the known injection interval"; the depth row says it is "not related to injection-interval depth or basement-fault structure" |

Extra credit: none.
MUST-NOT: none violated.
Errors: "wells sited in response to prior activity" is speculative, but it is posed as a question. "the known injection interval" implies data the case does not give, but this is minor and not counted.
Padding: 0.

**Ranking o2: Set 1 = Set 3 > Set 2.** Both cover all four MUSTs. Set 1 is broader (volume correlation, continuous subnetwork) but waves off the Poisson issue. Set 3 is cleaner and adds a longer baseline. Set 2 is only partial on the radius and the natural rival.

---

## case_o3 — Structured interviews and quality of hire

### Set 1
| Item | Grade | Evidence |
|---|---|---|
| M1 self-selection, pre-period baseline | F | F1: "The 11 opt-in teams, scored on their own 2024 ratings and retention before the kit existed" |
| M2 manager-rated outcome | F | F2: "A rating collected by someone other than the hiring manager, or blind … the rater is the same manager who chose the kit"; F8: "An objective metric (output, sales, peer scores)" |
| M3 survivorship of the rated sample | F | F3: "Re-including hires who left before 12 months … drops 23% of comparison and 16% of structured hires" |
| M4 ops/support extrapolation | F | F5: "A pilot in operations or support roles … the expected 'similar gains' in new role types is untested" |

Extra credit: E3 (F9: "Time-to-hire or candidate drop-out under the kit rises"). **1.** F7, a per-team breakdown, is close to clustering (E1) but does not make the effective-sample point, so it is not credited.
MUST-NOT: none violated. N1 is clean ("a cooling labour market does not rule out a pre-existing gap").
Errors: "scored at their last rating" assumes early leavers have a rating, but this is minor.
Padding: **1** (F6, a second cohort year, which is a generic replication point).

### Set 2
| Item | Grade | Evidence |
|---|---|---|
| M1 | F | F1: "Teams matched on manager quality, prior retention and size … the 11 opt-in teams may differ systematically" |
| M2 | P | It names the problem ("the same managers who chose the kit also rate the hires, unblinded"), but its remedy, "re-scored blind to which method produced each hire", is not workable when the rater is the manager. It never asks for an outcome recorded by someone other than the manager. |
| M3 | F | F3: "With hires who left before 12 months counted at a below-average rating … drops exactly the likeliest failures" |
| M4 | F | F4: "'similar gains' is unsupported outside engineering/sales" |

Extra credit: none. Q11 cites the pulse survey only as the managers' own account and does not say that it measures satisfaction rather than hire quality.
MUST-NOT: **X2 violated, and seriously.** F4 has status "blocked" with the receipt "HR runs one pilot team before Q3 2026; passes near 0.4". That is an invented test and an invented result. N3 is not violated.
Errors: Q5 maps the per-team question to F3, which is about leavers. Q10 asserts that "the opt-in window, metric and cutoff appear fixed".
Padding: **1** ("Flip").

### Set 3
| Item | Grade | Evidence |
|---|---|---|
| M1 | F | "Not held — self-selection confound"; "A within-team before/after comparison (adoption teams' own pre-2025 hires vs. post)" |
| M2 | F | "rater is not independent of treatment … an independent outcome (e.g., a cross-manager or objective performance measure) is needed" |
| M3 | F | "were their last-known or exit ratings pulled in, or just dropped?"; "differently survivor-filtered" |
| M4 | F | "extending to ops/support … it's an added, untested generalisation" |

Extra credit: E4 ("Pulse-survey satisfaction … evidence about process satisfaction, a different job, not about hire quality"). **1.**
MUST-NOT: none violated. N1 is handled correctly ("held only net of the stated company-wide cooling-market trend").
Errors: "reverse causation" is a loose label for selection, but this is minor.
Padding: 0.

**Ranking o3: Set 1 = Set 3 > Set 2.** Both cover all four MUSTs with one extra each: costs for Set 1, the pulse survey for Set 3. Set 2 fabricates a pilot result.

---

## case_o4 — CI flakiness agent report

### Set 1
| Item | Grade | Evidence |
|---|---|---|
| M1 3/3 green is weak | F | F2: "3 consecutive passes occur by chance with probability near 58%; at least 30 runs are needed" |
| M2 masking rather than fixing | F | F4: "the retry masks a real, reproducible error … a patch, not a fix"; F5: "raising a timeout … can outrun a race without removing it" |
| M3 refund test moved, incident | F | "Closing the refund double-posting incident on this basis does not follow: the one test tied to that bug was explicitly excluded from CI"; "revert the move" |
| M4 self-reported verification | M | The action log is never identified as the claimant's own record. C3 is tested only through F4 (retry masking) and F6. |

Extra credit: E3 (F6: "a longer window … surfaces at least 1 flaky test outside this set") and E4 (F3: "run on real CI infrastructure, with its usual concurrent jobs"). **2.**
MUST-NOT: N1, N2 and N3 are clean. **X2 violated (minor):** F3 says "'on my branch' is not the load the flakiness was observed under", which states as fact a difference of environment that the case does not give.
Errors: F6 is mapped to C4 rather than C3.
Padding: 0.

### Set 2
| Item | Grade | Evidence |
|---|---|---|
| M1 | F | F1: "'failed roughly 1 in 6 runs' means 3 green runs sit within the old rate's own noise"; 50 runs. It does not compute the 58%. |
| M2 | F | F2: "widened timeouts and retries can hide the fault instead of removing it"; "'fixed' is stated before the mechanism, not the symptom, was checked" |
| M3 | F | F3: "moved to `nightly`, off the PR gate"; "reinstate the race test on the PR gate before closing the incident ticket" |
| M4 | P | F4 and Q11: "'I ran' and 'my branch' is the agent's own, unwitnessed run". This is self-reporting of the runs, but the self-written "addressed" action log, which is the item's core, is not challenged. |

Extra credit: E2 ("with no gauge for whether nightly runs ever catch it"). **1.**
MUST-NOT: **X2 violated (minor).** Q6 says "before/after rates were measured under different loads", which states a fact the case does not give.
Errors: Q13 marks the counting boundary as "covered … 9 tests addressed, 3 full-suite runs, none dropped", which contradicts its own point that the race test was dropped from the gate.
Padding: 0.

### Set 3
| Item | Grade | Evidence |
|---|---|---|
| M1 | F | "three repetitions is not strong evidence … a do-nothing suite could plausibly go 3/3 green by chance"; "dozens of repetitions, or a probability calculation" |
| M2 | F | "Every one of the 3 fixes is a patch (wider timeout, retry, skip) with no diagnosis of root cause" |
| M3 | F | "passing because it no longer runs on PRs"; "Keep the incident ticket open" |
| M4 | F | "Self-reference trap: 'Confirmed in my action log …' verifies the agent's own process, not the outcome … not independent evidence"; "have a human engineer investigate" |

Extra credit: none. "continued undiagnosed instability in nightly" comes close to E2 but does not ask whether nightly runs are monitored.
MUST-NOT: none violated. N2 is borderline: "Investigate and fix the actual race condition … the underlying refund race" presumes the race is real. The answer asks for investigation and keeps the ticket open, so this is not counted.
Errors: none material.
Padding: 0.

**Ranking o4: Set 3 > Set 1 > Set 2.** Only Set 3 catches the self-reported action log, and it does so with no violation. Set 1 is strong on the 58% figure and has two extras, but misses M4. Set 2 gets M4 only partly, has an X2 and has a self-contradicting row.

---

## case_o5 — SIGNAL v4 (well-tested case)

### Set 1
| Item | Grade | Evidence |
|---|---|---|
| M1 recognises it as well tested | F | Six falsifiers marked "reported … none, as reported" (held-out set, spillover, ablation, independent harness, frozen contract) |
| M2 real scope limits | P | Only the register is listed (F7: "these are real limits of scope, stated by the source itself"). There is nothing on the sim-to-real gap, the driver or detector model, incidents, or template-generated networks. |
| M3 exception and weakest condition | P | F3 quotes the 7.1% figure and the −1.4% exception, then says "none, as reported". It does not suggest checking network types like the long-block grid. |

Extra credit: E3 (F1: "credit to the encoder specifically, versus the training process generally, is not fully settled"). **1.**
MUST-NOT: N1–N4 are not violated. It asks open questions (ablation retraining, dropped cells) and does not demand that anything be redone.
Errors: none.
Padding: **1** (F2, an undisclosed dropped cell, which is a generic exclusion check with nothing in the case to prompt it).

### Set 2
| Item | Grade | Evidence |
|---|---|---|
| M1 | F | "the one gap in an otherwise tightly run evaluation"; "not an artifact of leaked data, a changed metric, or a biased harness" |
| M2 | P | Q1 quotes the register only. There is no sim-to-real gap and no template limit. |
| M3 | P | It mentions the long-block grid at −1.4% only as a strength ("names its own worst case"). There is no 7.1% figure and no follow-up check on similar networks. |

Extra credit: none.
MUST-NOT: not violated. The demands for a training seed and a size-matched ablation are new tests, not redos.
Errors: F2 says "unlike the register's other tracked consequences", but the register lists exclusions, not tracked consequences.
Padding: **2** (F2, compute/operating cost, which is generic and outside the claim; and the "Flip" paragraph).

### Set 3
| Item | Grade | Evidence |
|---|---|---|
| M1 | F | "This report is unusually disciplined … The task is to find what remains open given that strength, not to re-litigate it"; the 11.8% result is marked "Held" |
| M2 | P | "Nothing about real-world deployment, sensor noise, or demand beyond 120% — all explicitly and correctly excluded" covers the register only, with no sim-to-real gap and no template limit |
| M3 | P | The exception network is "Held if … a pre-specified or computed noise band … backs 'within noise'". It is not treated as a refutation, but there is no check on similar network types and no 7.1% figure. |

Extra credit: none.
MUST-NOT: N2 is borderline. "Baseline tuning quality — Unknown … a weaker baseline tuner inflates v4's apparent edge" raises a doubt the text largely rules out ("re-tuned by a separate team member for each network"). The answer does not call the baseline untuned and labels the point "owner-fixed", so it is not counted.
Errors: "both arms re-tuned/run independently" is wrong, because only the baseline was re-tuned.
Padding: 0.

**Ranking o5: Set 1 > Set 3 > Set 2.** All three get M1 found and M2 and M3 partly. Set 1 credits the most of the design explicitly and earns E3. Set 3 frames the case well but nearly invents a doubt about the baseline. Set 2 adds generic padding.

---

## case_o6 — GRIDMIND v9

### Set 1
| Item | Grade | Evidence |
|---|---|---|
| M1 "robust" overreaches, N-1 register | F | F1: "'robust' is contradicted by the register's own exclusion of N-1"; F8: "planning on an unestablished premise carries the gap forward" |
| M2 metric change: 100% results, range, timing | P | Timing only: "held if the 105% threshold was fixed before v9's results were seen at the old one". It does not ask for results at 100% or across a range of thresholds. |
| M3 what the 4.1% cost reflects | M | F7 asks about the scenario spread of cost and says "what it is paid against is unstated". That is a vague cousin, with no curtailment, load shedding or conservative dispatch. |
| M4 critic accuracy and calibration | M | Not raised. F4, a non-learned safety margin as a rival, is a different test. |

Extra credit: E1 (F2: "Retraining both versions with 3+ seeds") and E2 (F6: "A batch from a different generator"). **2.** F5 ("pooled count could hide a scenario where v9 does worse") is near E3 but does not raise concentration on particular lines or severity, so it is not credited.
MUST-NOT: N1, N2 and N3 are clean. F3 is conditional ("a late redefinition would make …").
Errors: Q13 says "all 400 scenarios are counted under the same threshold, no stated exclusion", which overlooks that the redefinition itself changes what is counted.
Padding: **3** (F7, a generic cost-distribution point; F9, a trivial "outside the claim" row; F10, a generic independent rerun). That is 3 of 10 falsifiers, so X3 is not exceeded.

### Set 2
| Item | Grade | Evidence |
|---|---|---|
| M1 | F | "'Robust' — a catch-all carrying N-1 into 'next steps' … while the register lists N-1 as untested"; the claim as it stands is narrowed to "400 scenarios from one generator, under the 105% threshold" |
| M2 | F | F1: "Under the 100% threshold, v9's own count …"; "nothing shows it changed before v9's old-threshold number was seen". There is no threshold range, but the central test and the timing are both there. |
| M3 | M | Q12 marks cost as "covered" by quoting "which we consider acceptable" |
| M4 | M | Not raised |

Extra credit: E1 (F2, seeds) and E2 (F3, "Evaluated on a generator with a different distribution"). **2.**
MUST-NOT: none violated.
Errors: Q12 accepts the 4.1% cost judgement as "covered", and Q5 maps the worst-case spread to the generator falsifier.
Padding: **1** (F6, a generic independent rerun).

### Set 3
| Item | Grade | Evidence |
|---|---|---|
| M1 | F | "Swap 'robust' for 'lower violations on scenarios drawn from the training distribution' … sits awkwardly next to the register's own exclusion of N-1"; "the underlying result … is fine as a narrower claim" |
| M2 | F | "whether 105% was fixed before seeing v9's results under 100% is not stated"; "nor show both versions under the original 100% definition side by side" |
| M3 | M | "The 4.1% cost increase is accepted without a stated tolerance" does not ask what the cost buys (curtailment, shedding) |
| M4 | M | Not raised |

Extra credit: E1 ("Multi-seed training runs for both versions") and E2 ("not in the register at all: out-of-distribution scenarios"). **2.**
MUST-NOT: **X2 violated.** The change list says "two thresholds (both reported, v8 re-scored under the new one)", but the case reports results under 105% only, and the answer's own later row contradicts this. N3 is clean ("the right partial safeguard").
Errors: it refers to another case ("Unlike case_o5", "as o5 did with its 5% pedestrian-wait tolerance") and imports that case's tolerance as a benchmark for this one.
Padding: **1** (the cost-tolerance comparison with o5).

**Ranking o6: Set 2 > Set 3 > Set 1.** Sets 2 and 3 both get M1 and M2 in full. Set 2 does so with no violation, while Set 3 misstates what was reported. Set 1 gets M2 only partly and has the most padding. All three miss M3 and M4.

---

## Summary table

| Case | Set 1 MUST F/P/M | Set 1 MUST-NOT violated | Set 2 MUST F/P/M | Set 2 MUST-NOT violated | Set 3 MUST F/P/M | Set 3 MUST-NOT violated | Ranking |
|---|---|---|---|---|---|---|---|
| o1 | 4/0/0 | 0 | 3/0/1 | 1 (X2: SD) | 4/0/0 | 1 (X2: randomised/blinded design) | S1 > S3 > S2 |
| o2 | 4/0/0 | 0 | 2/2/0 | 0 | 4/0/0 | 0 | S1 = S3 > S2 |
| o3 | 4/0/0 | 0 | 3/1/0 | 1 (X2: invented pilot result) | 4/0/0 | 0 | S1 = S3 > S2 |
| o4 | 3/0/1 | 1 (X2: branch load, minor) | 3/1/0 | 1 (X2: different loads, minor) | 4/0/0 | 0 | S3 > S1 > S2 |
| o5 | 1/2/0 | 0 | 1/2/0 | 0 | 1/2/0 | 0 | S1 > S3 > S2 |
| o6 | 1/1/2 | 0 | 2/0/2 | 0 | 2/0/2 | 1 (X2: "both thresholds reported") | S2 > S3 > S1 |

## Totals (23 MUST items per set)

| | Set 1 | Set 2 | Set 3 |
|---|---|---|---|
| Found | 17 | 14 | 19 |
| Partly | 3 | 6 | 2 |
| Missed | 3 | 3 | 2 |
| MUST-NOT violations | 1 (minor) | 3 (1 serious: fabricated result) | 2 |
| Extra credit | 8 | 5 | 4 |
| Padding points | 9 | 6 | 1 |
| Cases ranked first | 4 (o1, o5 alone; o2, o3 tied) | 1 (o6) | 3 (o4 alone; o2, o3 tied) |

## Three most important weaknesses of each set

**Set 1**
1. **Misses the intermediate step and what the trade-off costs.** It does not check the critic's calibration or what the cost rise reflects (o6 M3, M4), and it never questions the self-written action log (o4 M4).
2. **Its scope analysis on the well-tested case covers only the register.** It lists no sim-to-real gap and no check on networks like the exception (o5 M2, M3), and it gives the threshold-timing question without asking for results at 100% (o6 M2).
3. **Most padding.** It includes generic replication and raw-data falsifiers (o1 F7–F9, o6 F7, F9, F10) and long "does not apply" Q-tables. It also waves off a valid test, saying the Poisson significance is "not in question" (o2), and asserts an environment difference the case does not give (o4).

**Set 2**
1. **Invents facts.** It reports a fabricated pilot test and result ("HR runs one pilot team … passes near 0.4", o3), an SD that is not in the case (o1), and "different loads" (o4).
2. **Misses or only partly reaches central tests.** It has no time course and denies that the claim promises anything beyond 7 dpa (o1 M4). The radius-sensitivity and natural-rival points are only partial (o2 M2, M3), and it marks the cost judgement as "covered" (o6 M3).
3. **Its Q-tables contradict its own analysis.** Examples: "none dropped" (o4 Q13), the picker marked "covered" (o2 Q11), and misrouted pointers (o3 Q5, o6 Q5). It also has stock "Flip" paragraphs that add no test (o1, o2, o3, o5).

**Set 3**
1. **States design facts the case does not give.** It says the design was "randomised-sibling, blinded-genotype" (o1) and that "two thresholds (both reported)" (o6), and in both cases its own later text contradicts the claim.
2. **The same depth gaps as the others on the mechanism and the trade-off.** It misses the critic's calibration and what the 4.1% cost reflects (o6 M3, M4), and its scope list for the well-tested case covers only the register (o5 M2, M3).
3. **Fewest extras, and it leaks context from other cases.** It finds nothing on declustering, location shifts or the time series (o2), nothing on nightly monitoring (o4), and gives itself the fewest extra-credit points (4). It imports another case into its answer for o6 ("Unlike case_o5", "as o5 did"), and it nearly invents a doubt the text rules out about baseline tuning (o5).

## Overall judgement

Set 3 is the strongest on the amended lists: 19 of 23 MUSTs found, almost no padding, and the only set to catch the self-reported action log in o4. Set 1 is a close second: 17 found, the fewest violations and the most extra credit, but more generic padding. Set 2 is clearly weakest, with the fewest MUSTs found and three X2 violations, one of them a fabricated test result.

I am fairly confident that Set 2 ranks last. I have only moderate confidence in the order of Sets 3 and 1. It rests on a few judgement calls (o4 M4, o6 M2, and how much weight Set 3's two X2 errors deserve against Set 1's extra credit and padding), and those calls could plausibly reverse it.
