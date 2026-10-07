# Round 4 marking lists: all 12 cases

Part A: cases g1 to g6, written by GLM (glm-5.3), with amendments by Opus 5.5 adopted before any answers were seen.

# Round 4 marking lists, written by GLM (glm-5.3) before any answer existed

Common MUST-NOT for every case: X1 says the claim is true or false outright when the evidence cannot settle it; X2 says a test was run or a result obtained that the case does not report, or states a fact the case does not give; X3 more than a third of the points are generic checks with no link to the case; X4 demands a test impossible even in principle as if it were required.


## case_g1

MUST:
- Ask whether the 15% boarding rise can be separated from the two concurrent changes the report itself names (citywide signal retiming from mid-March; the fare freeze from February). As presented, the corridor lane is not isolated as the cause.
- Ask whether car traffic was displaced onto parallel routes: only Marsh Street's own car speeds were measured, so congestion may have shifted to Ferndale Road or Eastgate rather than been absorbed.
- Question the baseline: February (pre-change) vs mid-March-to-May (post-change) invites seasonality, weather, daylight and holiday effects; an eight-week horizon also cannot show whether gains persist once novelty fades.
- Question the ridership metric: boardings from automatic counters can double-count transfers between the four routes and are not unique riders; whether the counters themselves are validated/calibrated is not stated.
- Question the satisfaction survey's respondents: onboard surveys select existing riders; the survey timing (April, post-change) and question wording are not described.
- Question the extrapolation of a 15–20% boarding gain to other corridors whose baseline delays, demand and route mixes are not established to match Marsh Street's.
MUST-NOT:
- State as fact that parallel-street congestion worsened (not measured in the text).
- Claim the car-speed finding settles impacts on drivers generally.
- Assert ridership "really" came from the fare freeze (unsettled), or invent weather data for March.
- X1: declare the claim true or false outright when the evidence cannot settle it; X2: cite tests or results not in the text; X3: fill the list with generic checks unlinked to this corridor; X4: demand impossible tests (e.g., a counterfactual identical city).
EXTRA CREDIT:
- Suggest a difference-in-differences comparison with a similar untreated corridor.
- Note that GPS bus timing is reliable but says nothing about passengers' whole-journey time.


## case_g2

MUST:
- Question execution realism: fills at the settlement price with commissions only means no slippage, bid-ask spread or market impact is modelled; at ~45 contracts per signal on possibly thin legs, realised fills could materially erode or reverse the edge, and the USD 250m capacity of the strategy is untested.
- Question survivorship: the universe is "the 56 most liquid contracts currently listed", so contracts that were once traded but were delisted or died — exactly where momentum tends to hurt — are excluded, flattering results.
- Question data-driven design: the 120-day lookback was picked as the best of four on the same full sample, and the volatility filter was added after inspecting the 2020 drawdown; both are in-sample choices, and no walk-forward, holdout or paper-trading period supports them.
- Question the regime coverage: 2013–2023 is one macro period (low rates, no sustained inflation); behaviour under conditions outside that range is untested, and "10 of 11 profitable years" is a weak robustness statement within it.
MUST-NOT:
- Assert that the strategy will lose money live, or quote a live track record (none exists in the text).
- State a specific corrected Sharpe or return figure as fact.
- X1: declare the claim true or false outright when the evidence cannot settle it; X2: cite tests or results not in the text; X3: fill the list with generic checks unlinked to this backtest; X4: demand impossible tests (e.g., knowing true future fills).
EXTRA CREDIT:
- Note that a no-look-ahead check on the volatility filter (computed with same-day data) is needed.
- Suggest re-running with the delisted-contract universe restored and a capacity/impact model added.


## case_g3

MUST:
- Recognise this as a well-tested claim: the main falsifiers were run — batch-to-batch and plant-to-plant variation (3 plants × 20 loads, randomised), blinding and independence (accredited third-party lab, blind to mix), curing-temperature dependence (5/20/35 °C), time horizon (7/28/90 days), a check on the companion property (flexural, honestly reported as a smaller 7% gain), and cost of the change stated.
- Confirm the reviewer accepts the ~14% 28-day compressive gain as established within the tested scope.
- List the real scope limits: results cover one blend (C25/30), one fibre dosage and one supplier's materials; only static loading was tested — fatigue and durability (chloride ingress, freeze–thaw) were not, so no conclusion follows for de-iced or structural applications; flexural gain is modest, so claims about crack control or joint spacing would not follow from these data.
- Note the proposal is sensibly conditioned on cost (only where earlier striking is needed) rather than a blanket switch.
MUST-NOT:
- Treat the case as weak evidence, or claim the main tests (blinding, multi-plant replication, curing range) must be redone before acceptance.
- Invent doubts the text rules out: e.g., claiming the lab was not blinded, that plant variation was not sampled, or that cost was omitted.
- Extend the claim beyond its scope (structural concrete, marine exposure) and treat that extension as if the trial were meant to cover it.
- X1: declare the claim true or false outright when the evidence cannot settle it; X2: cite tests or results not in the text; X3: fill the list with generic checks unlinked to this trial; X4: demand impossible tests.
EXTRA CREDIT:
- Note that per-load scatter (SD ~2 MPa) means some individual fibre loads still fall below any striking trigger; ask about per-load acceptance criteria.
- Ask whether earlier striking timing itself was validated in the field, not just strength at fixed ages.


## case_g4

MUST:
- Question the fixed order with no counterbalancing: every rider did beetroot first and placebo second, so familiarisation, pacing practice or fatigue over the week is a rival explanation for the 1.8% gain, and carryover cannot be excluded.
- Question the broken blinding: riders could identify the beetroot shot by taste and colour, and the head coach — who designed the study, knew the condition, administered drinks and operated the timing stopwatch — recorded the outcome. Motivation and recorder bias are unaddressed.
- Question diet control by self-report diary only: background nitrate intake (leafy greens, other vegetables) and caffeine avoidance rest on participants' own unverified records; a nitrate-rich control-day meal could swamp a 6.4 mmol dose, and diary compliance cannot be checked.
- Question the sample: n = 14 from one club, training together under the same coach — not independent units — with a CI that just excludes zero, and only an acute single-session test, so nothing on persistence or adaptation.
MUST-NOT:
- Assert the coach deliberately biased times, or that riders "must" have been demotivated on placebo.
- State as fact that a counterbalanced replication would show no effect.
- X1: declare the claim true or false outright when the evidence cannot settle it; X2: cite tests or results not in the text; X3: fill the list with generic checks unlinked to this trial; X4: demand impossible tests (e.g., true blinding of taste by any means being treated as trivially available, or continuous diet monitoring presented as required).
EXTRA CREDIT:
- Suggest a randomised crossover with washout, flavour-masked placebo and blinded electronic timing.
- Note plasma nitrite, the mechanism's intermediate step, was never measured — so even the positive result does not confirm the nitrate pathway.


## case_g5

MUST:
- Question the early stopping: the test was halted the moment p<0.05 appeared at the midpoint; repeated peeking invalidates the reported significance, and the "+6.4%, p<0.05" cannot be taken at face value.
- Question group contamination: the voucher code spread via a deals forum from week 2, so assignment by account ID no longer isolated the arms; the claim that this makes the estimate "conservative" is an unverified assertion (it also corrupts variance and could reflect pull-forward demand rather than added sales).
- Question the metric: revenue is checkout GMV at order time — returns (whose window is still open) and the margin cost of 10% vouchers plus any shipping promos are unnetted, so the net effect on profit is unknown.
- Question the operating point: a four-week test entirely inside the November/Black Friday run-up measures holiday-season price sensitivity; behaviour in ordinary months is outside the tested range.
- Question the extrapolation: from one store, one month, to "all EU stores, +5–6%" without evidence that flagging, mix and elasticity transfer.
MUST-NOT:
- Assert that returns or margin data were analysed (the text does not report them).
- State that a corrected re-run would show no lift.
- X1: declare the claim true or false outright when the evidence cannot settle it; X2: cite tests or results not in the text; X3: fill the list with generic checks unlinked to this test; X4: demand impossible tests (e.g., a contamination-free internet).
EXTRA CREDIT:
- Note multi-session/cross-device visitors weaken the account-ID split.
- Suggest a fixed-horizon re-run on returns-adjusted margin with a leakage-resistant single-use code.


## case_g6

MUST:
- Question the scanner's validity: nowhere does the report show the DAST tool detecting XSS on a deliberately seeded vulnerable build, so "zero findings" could mean zero coverage rather than zero bugs — "no reason to doubt its coverage" is an opinion, not a check.
- Question what was scanned: it is not stated whether the nightly crawl authenticates into the portal; the Q2 findings were in the customer portal, and login-gated pages could be entirely outside the 1,100 scanned pages.
- Question independence of verification: the internal appsec team that wrote the integration also performed the manual verification, and the original external penetration tester was not re-engaged; all positive evidence is recorded by the claimant's own team.
- Question the time horizon and lagging signals: six weeks of no bounty payouts and no support tickets is far too short — attacker rediscovery, researcher attention and reporting all lag, and a pre/post comparison of a few months' bounty history proves little.
- Question displacement: SAST coverage is limited to "the new template layer"; sinks outside it (file uploads, DOM-side code, third-party widgets, non-template endpoints) were not assessed, so the bug class may simply have moved.
MUST-NOT:
- Claim the portal is certainly still vulnerable, or that a bypass was demonstrated.
- Assert facts about scanner configuration (authenticated crawling, payload sets) beyond what the text states.
- Treat the internal team's manual re-run as fraudulently reported rather than potentially biased.
- X1: declare the claim true or false outright when the evidence cannot settle it; X2: cite tests or results not in the text; X3: fill the list with generic checks unlinked to this remediation; X4: demand impossible tests (e.g., proving absence of all future XSS).
EXTRA CREDIT:
- Suggest a seeded-vulnerability calibration scan and a re-test by the original external pentester with authenticated sessions.
- Note that recommending the library for the internal tools estate rests on evidence from a different codebase.


## Amendments adopted before any answers were seen (6 October 2026, audit by Opus 5.5)

Numbering convention: MUST items are referred to as M1, M2, … and MUST-NOT items as N1, N2, … in the order they appear under each case above; EXTRA CREDIT items as E1, E2, …. Wherever a MUST item below is replaced, the replacement text is the item the grader scores. All six cases are usable; none is judged unrealistic.

### General
- all cases: where a MUST item lists several sub-points, award it when the answer raises the central test named in that item's first clause with a case-specific reason; the illustrative sub-points (examples in parentheses or after "e.g.") are not each required.

### case_g1
- case_g1: replace M1 with: "Ask whether the bus-priority scheme can be isolated as the cause of both headline results, given the two concurrent changes the report itself names: the citywide signal retiming from mid-March could account for part of the 21% travel-time cut as well as the boardings rise, and the fare freeze from February could account for part of the 15% boardings rise. A comparison with untreated corridors or citywide trends over the same weeks is needed." Reason: the original item covered only boardings, but the signal retiming is an equally direct rival explanation for the travel-time result.
- case_g1: replace M2 with: "Ask whether car traffic was diverted rather than absorbed: only Marsh Street's own general-traffic speeds were measured, so neither car volumes on Marsh Street nor conditions on parallel streets are known, and a 2.4 km/h mean drop is given without the baseline speed needed to judge whether it is 'slight'." Reason: the original named Ferndale Road and Eastgate as the likely parallel routes, but the case gives them only as proposed future corridors, not as streets parallel to Marsh Street, so that detail cannot be derived from the text; the unanchored 2.4 km/h figure can be.
- case_g1: replace M4 with: "Question what the boardings rise measures: APC boardings on the four corridor routes may reflect riders moving from other routes or modes in the network (redistribution, not new ridership), and boardings are not unique riders. Credit also counter double-counting of transfers or unvalidated counters as supporting points, but they are not required on their own." Reason: redistribution from elsewhere in the network is the more important test the text supports; counter calibration alone is close to a generic check (X3).
- case_g1: amend M5 so that it is satisfied by questioning either the selection of onboard respondents (current riders only) or the comparability of the 71% baseline survey, whose date and method are not given. Reason: the text gives the timing of the 79% survey (April) but not of the 71% survey, so comparability is the derivable point.
- case_g1: reword E2 to: "Note that the GPS travel-time measure covers in-vehicle corridor time only, and says nothing about waiting time, reliability or variability (only a mean is reported), or whole-journey time." Reason: the original asserted as fact that GPS timing is reliable, which the case does not establish.

### case_g2
- case_g2: replace M1 with: "Question execution realism: fills at the settlement price with commission only means no spread, slippage or market impact is modelled; with weekly rebalancing across 56 contracts the cost drag on the edge needs to be estimated, and capacity at USD 250m (~45 contracts per signal) is untested, especially in the less liquid contracts. Credit equally the point that filling at the same settlement price used to compute the signal is not achievable (look-ahead in execution)." Reason: the original stated as a near-prediction that fills 'could materially erode or reverse the edge'. About 45 contracts is small for most liquid futures, so an answer that reasons the impact is probably small in the main contracts but must be checked in thin ones should get full credit. The same-bar fill problem is the sharpest derivable execution point and was missing.
- case_g2: in M2, delete the clause "— exactly where momentum tends to hurt —". Reason: it is an unsupported empirical assertion that is not in the case. The core point stands: the universe was chosen by present-day listing and liquidity, so it includes contracts that later survived and grew liquid and leaves out those that did not.
- case_g2: replace M4 with: "Question the robustness evidence: everything is from one in-sample 2013–2023 run; '10 of 11 profitable years' and 'no dependence on any single sector' are descriptive statements about the same sample used to choose the lookback and the filter (and the sector claim rests on eyeballing the equity curve rather than a per-sector or leave-one-sector-out breakdown); no out-of-sample period, earlier history, or independent replication of the code and data ('available on request') is reported." Reason: the original M4 stated that 2013–2023 had "low rates, no sustained inflation", which is factually wrong (2021–2023 had high inflation and steep rate rises) and goes against X2. The derivable test is out-of-sample and per-sector robustness, not a particular macro story.
- case_g2: add N4: "Characterise the 2013–2023 macro environment as fact in a way that drives the critique (e.g., 'the sample contains no inflation or rate-hiking regime')." Reason: the original M4 itself made this error, and answers repeating it should not be rewarded.
- case_g2: add E3: "Ask how contract rolls were handled (continuous-series construction, roll timing and roll costs), since none is described for an 11-year futures backtest."
- case_g2: add E4: "Ask whether the 9.2% maximum drawdown and 11.4% return are with or without the volatility filter, which the text leaves ambiguous."

### case_g3
- case_g3: add M5: "Note that the reported result does not match the stated aim: the trial was meant to show higher early-age strength for earlier formwork striking, but only 28-day results are reported. The 7-day results are not given, and the ages that matter for striking (typically hours to a few days, especially at 5 °C) were not tested, so the case for earlier striking, and so for the cost proposal, is not yet shown." Reason: this gap follows directly from the text and is the most important open test. Without it the list rewards accepting a conclusion (earlier striking) that the reported data do not reach.
- case_g3: replace M1 with: "Recognise that the trial design is strong: batch-to-batch and plant-to-plant variation (3 plants × 20 loads each arm, randomised), blinding and independence (accredited third-party lab, blind to mix), curing-temperature dependence (5/20/35 °C), multiple test ages planned (7/28/90 days), a companion property checked (flexural, honestly reported as a smaller 7% gain), and the cost of the change stated." Reason: the original listed the "time horizon" as a falsifier that was run with results. The 7- and 90-day ages were planned, but their results are not reported (see M5).
- case_g3: replace M2 with: "Accept the ~14% 28-day compressive gain as well supported within the tested scope (one blend, one dosage, these plants, lab-cured cylinders), while keeping it separate from the earlier-striking conclusion (M5)." Reason: accepting a narrow, well-tested result is not X1, but the original wording could be read as requiring acceptance of the whole proposal.
- case_g3: clarify N1 and N2: raising M5 (unreported or untested early-age strength) is not "treating the case as weak evidence" or "inventing doubts the text rules out". The same holds for asking whether the water/cement ratio and air content were held constant when the water-reducer dosage was changed to match slump. The text says the water-reducer dosage was adjusted but does not say whether water content or w/c ratio was fixed.
- case_g3: add E3: "Ask whether water content / w/c ratio and air content were held constant between mixes when the water-reducer dosage was adjusted, since a higher water-reducer dosage with reduced water could itself explain a compressive gain."
- case_g3: add E4: "Note that a 14% compressive gain is larger than macro-synthetic fibre at ~4 kg/m³ would usually be expected to give (such fibres mainly affect post-crack behaviour), so the result is worth confirming against mix-proportion records." Reason: domain plausibility check; extra credit only, because it is not derivable from the text alone.

### case_g4
- case_g4: replace M1 with: "Question the fixed order with no randomisation or counterbalancing: beetroot was always first and placebo always second, so the condition is fully confounded with the session. Period effects such as accumulated fatigue or training load over the week, illness, or first-session novelty and motivation are rival explanations for the 1.8% difference. (A familiarisation or learning effect would, if anything, favour the second, placebo trial, so an answer may note that this particular bias runs against the claim; answers asserting that practice explains the beetroot advantage are not credited for that reasoning.)" Reason: the original named familiarisation/pacing practice as a rival explanation for the beetroot gain, but with beetroot first, learning would favour placebo. The direction was wrong; the confounding point stands.
- case_g4: in M3, replace "a nitrate-rich control-day meal could swamp a 6.4 mmol dose" with "background nitrate from diet, recorded only on trial days and only by self-report, could differ between the two sessions by an amount comparable to the dose". Reason: "swamp" states a magnitude as fact; also, the diaries covered only trial days, and that limit is derivable.
- case_g4: in M4, delete "and only an acute single-session test, so nothing on persistence or adaptation", and replace "with a CI that just excludes zero" with "with one trial per condition, so the effect cannot be compared with the day-to-day variability of a 20 km time trial, and the CI lower bound (0.6%) is well below the claimed ~2% 'meaningful' benefit". Reason: the recommendation is acute use in race week, so persistence and adaptation are not a test of this claim. A lower bound of 0.6% does not "just" exclude zero. The derivable points are test-retest variability and the gap between the lower bound and the claimed effect.
- case_g4: in N3 (the X4 line), delete the example "true blinding of taste by any means being treated as trivially available". Reason: taste-matched placebos (e.g., nitrate-depleted beetroot juice) are a standard, feasible control. Asking for one is a fair and possible test, not an impossible one, and must not be penalised.
- case_g4: add E3: "Ask when the shot was taken relative to the 07:00 trial, since the text does not give the ingestion-to-exercise interval on which the nitrate effect depends."

### case_g5
- case_g5: in M3, replace "returns (whose window is still open) and the margin cost of 10% vouchers plus any shipping promos are unnetted" with "returns and cancellations are not netted out, it is not stated whether checkout totals are before or after the voucher discount, and the margin given away on purchases that would have happened anyway is not counted". Reason: whether the returns window is still open, and any shipping promos, are not in the case (X2). The pre/post-discount ambiguity and cannibalised margin are derivable.
- case_g5: replace M4 with: "Question the operating point and the actual data window: the test was stopped 'halfway through', so the 'final numbers' most likely cover only about the first two weeks of November rather than the planned four (the text is ambiguous). That period is the Black Friday run-up, when price sensitivity and purchase timing are atypical, and voucher purchases may be pulled forward from Black Friday itself rather than added. Behaviour in ordinary months is outside the tested range." Reason: the original called it "a four-week test", which contradicts the reported early stop.
- case_g5: add E3: "Note that targeting by cart-abandon history rewards abandonment, so rolling out the voucher may teach customers to abandon carts to trigger it. This long-run behavioural effect is not measured by a short test."

### case_g6
- case_g6: in M3, replace "and the original external penetration tester was not re-engaged" with "and no independent retest (by the Q2 penetration testers or any other party) is reported". Reason: the case does not say the Q2 penetration test was external, nor that its testers were not re-engaged; it only reports no independent retest.
- case_g6: in M5, replace "SAST coverage is limited to 'the new template layer'" with "the reported SAST result covers only 'the new template layer'". Reason: the text reports the result for that layer but does not state the SAST tool's scope.
- case_g6: add M6: "Question the manual retest's scope: re-running only the original Q2 payloads against the originally affected endpoints shows that those specific payloads are now blocked, not that the fix generalises. Fresh adversarial testing is needed with new and context-varied payloads (HTML attribute, JavaScript, URL and DOM contexts, sanitiser-bypass variants) and on endpoints beyond the original findings." Reason: a fix verified only against the payloads it was built to block is the most direct falsification gap in the case, and the original list does not cover it.
- case_g6: amend E1 to read "… and an independent re-test with authenticated sessions (by the original penetration testers or another independent party)". Reason: as above, the case does not state that the Q2 tester was external.


Part B: cases o1 to o6, written by Opus 5.5, with amendments by GLM (glm-5.3) adopted before any answers were seen.

# Round 4 marking lists, written by Opus 5.5 (claude-opus-5-5) before any answer existed

Common MUST-NOT for every case: X1 says the claim is true or false outright when the evidence cannot settle it; X2 says a test was run or a result obtained that the case does not report, or states a fact the case does not give; X3 more than a third of the points are generic checks with no link to the case; X4 demands a test impossible even in principle as if it were required.


## case_o1

MUST:
- M1 Only one mutant allele from one sgRNA: the phenotype could come from an off-target lesion or linked mutation carried with the allele; asks for a second independent allele, a trans-heterozygote, a rescue (e.g. mRNA/transgene), or at least an off-target check.
- M2 The proposed mechanism's intermediate step was never measured: no proliferation marker (e.g. EdU/BrdU, PCNA, pH3) in the blastema and no evidence of Wnt dependence; shorter outgrowth is also consistent with defects in wound epidermis, blastema formation, patterning or cell survival, so "blastemal mitogen" is not supported.
- M3 Measurement was not blind: the person who genotyped and amputated also measured regenerate length; asks for blinded scoring or a second scorer, and a fixed measurement rule (e.g. reference ray, amputation plane).
- M4 Single time point (7 dpa): cannot distinguish a delay from a failure to regenerate; asks for a time course to full regeneration (e.g. 14–30 dpa).
EXTRA CREDIT:
- E1 All 48 fish come from one clutch of one pair and likely shared tanks; tank/housing and clutch effects mean the fish are not fully independent, and the result should be repeated in another clutch/pair.
- E2 Amputation level differences (more proximal cuts regenerate faster) could confound lengths; asks whether amputation plane was standardised or growth normalised.
- E3 Notes that genetic compensation in frameshift mutants could mask or alter phenotypes, so comparing with a knockdown or checking for nonsense-mediated decay/transcript levels is informative.
- E4 Points out the transcript enrichment and domain evidence are correlational/predictive and do not establish function.
MUST-NOT:
- N1 Claims that the mutant was rescued, that a second allele exists, or that proliferation was measured.
- N2 Dismisses the phenotype as artefact outright; a 41% difference at n=24 per group is real evidence that something is wrong with regeneration in this line.
- N3 Treats the sibling design as a flaw in itself (sibling controls are appropriate; the issue is a single clutch, not using siblings).


## case_o2

MUST:
- M1 The network was densified in early 2024, at about the same time injection began; the same picker on a denser network detects many more small events, so the "consistent processing" argument does not rule out a detection artefact. Asks for magnitude of completeness before and after, and a rate comparison above a common completeness magnitude (or using only the original stations).
- M2 The 15 km radius was chosen after seeing the post-injection cluster; the test is circular and the p-value overstated. Asks for a pre-specified or physically motivated region and sensitivity to radius.
- M3 Rival natural explanation: a natural swarm or regional rate change at the same time; asks for comparison with control regions away from injection (with the same station change), and whether the Sutter zone or wider area also changed.
- M4 Physical link not tested: no comparison with injection volumes/pressures over time, migration of events from the wells, injection depth vs the 3–6 km hypocentre depths (basement vs injection horizon), or a pore-pressure/stress model.
EXTRA CREDIT:
- E1 Earthquake catalogues contain aftershock sequences; events are not independent, so a Poisson test on raw counts overstates significance; asks for declustering.
- E2 Location quality improved after densification, so events may have moved into or out of the 15 km circle simply because locations changed, not because seismicity changed.
- E3 Notes that a regulatory recommendation (rate limits) carries costs, so the evidence bar should match the action.
MUST-NOT:
- N1 States outright that the seismicity is natural or that it is induced as settled fact.
- N2 Accepts the "same picker throughout" sentence as ruling out detection changes.
- N3 Claims the authors computed completeness magnitudes or ran a control region.


## case_o3

MUST:
- M1 Teams self-selected into the structured kit; teams that opt in may already have better managers, stronger hiring pipelines or different roles; asks for pre-2025 baseline ratings/retention of both groups (difference-in-differences) or matching on team and role.
- M2 The outcome is rated by the same hiring managers who chose and ran the new process, unblinded; investment in the kit can inflate their ratings. Asks for an outcome not recorded by the interviewer/manager (objective performance, calibrated or second-level ratings, promotion, ramp time).
- M3 Ratings are only for hires still employed at 12 months; the groups lost different shares (16% vs 23%), so survivorship changes who is counted; asks for an analysis that includes leavers (e.g. treat early exits as an outcome, bounds).
- M4 Extending to operations and support roles is outside the tested range (engineering and sales only); the gain cannot be assumed there.
EXTRA CREDIT:
- E1 Hires are clustered within 26 teams (11 vs 15), so the effective sample is closer to the number of teams; a hire-level p-value overstates certainty.
- E2 Rating scales may differ by team/manager (lenient vs strict raters); asks for within-manager or calibrated comparisons.
- E3 Costs and side effects of a mandatory panel of three: interviewer time, time-to-fill, offer-acceptance, candidate experience, and adverse impact on demographic groups were not reported.
- E4 Notes the pulse survey measures manager satisfaction, not quality of hire.
MUST-NOT:
- N1 Treats the company-wide retention rise as fully handled by the comparison group without noting the comparison is non-random (or conversely claims it fully explains the gap).
- N2 States that structured interviews do not work, or cites outside research as settling this company's result.
- N3 Claims the team had pre-period data or ran a matched analysis.


## case_o4

MUST:
- M1 Three green runs cannot show a 1-in-6 failure rate has gone: even with no change, three straight passes happen often (about 58% of the time). Asks for many repeated runs (e.g. tens to hundreds, ideally under load/parallelism) to estimate the new failure rate.
- M2 The fixes stop the check from failing rather than removing the cause: retries hide connection errors, longer timeouts hide slowness, and moving a test to nightly removes it from PR CI; asks for root-cause analysis for each test and confirmation that real bugs are not being hidden.
- M3 `test_refund_race_condition` was moved to nightly, not fixed; it may point to a real race condition in the product, and recommending closing the customer refund double-posting incident because the test is "now passing in CI" is wrong — it no longer runs in PR CI. The incident must stay open pending investigation.
- M4 The verification is self-reported: "addressed" in the agent's own action log is a record written by the claimant, not independent evidence; asks for CI-system logs/run history, or human review of the diff.
EXTRA CREDIT:
- E1 Side effects/costs: timeouts raised 5× and retries ×3 increase suite runtime and can slow feedback; asks for the duration change.
- E2 Asks whether the nightly job runs and is monitored, i.e. whether the flaky failure just moved to the nightly suite.
- E3 Notes the 9 tests were found from 200 runs; other flaky tests with lower rates may exist and were not looked for.
- E4 Asks whether the branch runs used the same CI environment/concurrency as `main`.
MUST-NOT:
- N1 Accepts "3/3 green" as proof of stability.
- N2 Claims the race condition is or is not a real product bug as settled fact.
- N3 Claims the agent ran more runs or root-cause analysis than reported.


## case_o5

MUST:
- M1 Recognises the claim as well tested: pre-registered frozen contract, held-out networks from unseen templates, multiple demand levels, independent seeds, a separately tuned baseline, a spillover check on side streets and boundary intersections, side-effect metrics, an ablation, and an evaluator independent of training. Mostly confirms C4.1 as stated within its scope.
- M2 Lists the real scope limits: simulation only (sim-to-real gap, driver behaviour model, simulated detector model); demand above 120% and incidents/disruptions untested; the networks come from template generators, so real city layouts may differ; and as the register says, sensor failure and emergency priority are excluded.
- M3 Notes the one exception (long-block grid) and the weakest condition (7.1% at 120%) as places where the gain is smaller, suggesting checks on network types like the exception before deployment, without treating them as refuting the claim.
EXTRA CREDIT:
- E1 Notes the 3% rise in pedestrian wait is a real cost to report alongside the headline, even though it is within tolerance.
- E2 Suggests checking how results vary with other plausible simulator calibrations (e.g. driver-behaviour parameters) as a further scope test, framed as an extension, not a flaw.
- E3 Notes that the ablation attributes the gain to the encoder inside the v4 training setup only.
MUST-NOT:
- N1 Treats the claim as weak or unsupported, or demands that held-out evaluation, seeds, spillover check, baseline tuning or ablation be redone.
- N2 Invents doubts the text rules out: e.g. metric chosen after results, baseline untuned, test networks seen in training, displacement of queues unchecked, evaluator is the trainer.
- N3 Faults the report for not proving real-world benefit, which it explicitly does not claim.
- N4 Demands a real-city deployment as required before accepting a simulation-scoped claim.


## case_o6

MUST:
- M1 The headline "robust grid operation" and "v9's robust behaviour" go beyond what was tested and conflict with the register, which excludes N-1 contingencies; the claim must be narrowed to intact-network, 118-bus, in-distribution scenarios.
- M2 The violation metric was changed in this version (100% → 105%); re-scoring v8 makes it like-for-like but does not show the result is robust to the threshold; asks for results at the original 100% definition and over a range of thresholds, and why the change was made now.
- M3 The fall in violations may come from what the fix gives up rather than better dispatch: asks what the 4.1% cost rise reflects — e.g. curtailing renewables, load shedding, or conservative dispatch — and whether unserved energy or curtailment rose.
- M4 The critic's intermediate step was not checked: no report of the critic's prediction accuracy/calibration against actual violations, especially on states the v9 policy reaches; the policy may be exploiting critic errors or simply avoiding states the critic flags.
EXTRA CREDIT:
- E1 Single training seed for each version: the 62% gap could partly be seed variation; asks for multiple seeds or confidence intervals.
- E2 Test scenarios come from the same generator and years as training; no out-of-distribution test (extreme weather days, other years, high renewable shares).
- E3 Line-hours are pooled; asks whether violations are concentrated on a few lines or days, and whether severity (peak overload) also fell.
- E4 Asks whether other constraints (voltage limits, ramping) not penalised by the critic got worse.
MUST-NOT:
- N1 Declares v9 unsafe or worthless; a 62% fall in the chosen metric is real evidence within its scope.
- N2 Claims the team ran N-1 tests, multiple seeds, or a 100%-threshold comparison.
- N3 Treats the re-scoring of v8 as dishonest in itself rather than raising threshold sensitivity.

Amendments adopted before any answers were seen (6 October 2026, audit by GLM glm-5.3)

No case is unusable: all six are realistic, internally consistent, and every existing MUST item is derivable from the case text alone. Arithmetic spot-checks pass (o1: 0.89 vs 1.51 = 41% shorter; o2: 211/38 = 5.5-fold; o3: 3.94 − 3.51 = 0.43; o4: (5/6)³ ≈ 58%; o6: (1130−429)/1130 = 62%). Amendments:

- case_o1: add EXTRA E5: the sex of the fish is never reported; fin regeneration rate differs between male and female zebrafish, so credit answers asking whether sex was balanced or stratified across the mutant and sibling groups.
- case_o2: add EXTRA E4: credit answers asking for a monthly event-count time series plotted against both the station densification (early 2024) and the injection start (March 2024); because the two nearly coincide, whether the rate steps up at deployment or instead tracks injection volume over time is the sharpest available diagnostic between a detection artefact and genuinely induced seismicity.
- case_o3: reword N1 to: "Accepts the report's aside that the structured group 'still came out ahead' as settling the company-wide retention trend, or conversely asserts that the trend fully explains the group gap; the comparison is non-random, so neither conclusion is available from these data." (Same intent as the original, but the double-negative phrasing was unclear for graders.)
- case_o4: no amendment; the four MUSTs, the extras and the MUST-NOTs are complete and fair as written.
- case_o5: add EXTRA E4: credit answers asking whether the 95% CI (9.9–13.6%) reflects network-to-network variation (clustering by the 20 held-out networks) or only simulator-seed noise; with one network at −1.4%, a network-clustered interval could be wider than reported.
- case_o6: extend M2 by adding: "…and whether the 105% threshold was chosen before or after v9's results were seen — a metric changed 'for this version' may be a post-hoc choice even though v8 was re-scored, so the timing of the change must be questioned, not just its sensitivity."
- case_o6: add EXTRA E5: the critic penalises predicted exceedance of the thermal limit (100% of rating) within 15 minutes, while the reported metric now counts line-hours above 105% of rating; after the redefinition the training proxy and the scored metric differ, and answers noting this mismatch deserve credit.
- case_o5 (well-tested check): confirmed as genuinely well tested within its stated scope — frozen contract, unseen templates, per-network baseline re-tuning, seeds, spillover and side-effect metrics, ablation, independent evaluator, and an honest claims register — so M1–M3 and N1–N4 stand without change.