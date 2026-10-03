# S114 Restart audit: results

*Log S114, decisions S64 to S66. Written 30 September 2026 by the one Opus 5.5 agent of log S114 (S56), after the runs, against the plan written and committed before them: `results/S114 Restart audit - how it will be tested, written before running.md` (73ea5de). In the owner's Avida terms (S61). All entities are digital programs executing on Avida's virtual CPU. Data: `S114 Restart audit - results.json` beside this file (every sample, both ways, every seed). Scripts: `tools/s114_restart_audit_run_the_pieces_and_the_continuous_runs.py` (the runs), `tools/s114_restart_audit_reload_the_continuous_populations.py` (the follow-up check, a departure), `tools/s114_restart_audit_compare_the_pieces_with_the_continuous_runs.py` (the measures and thresholds). Raw output in the scratch space (`s114_restart_audit/`, about 60 MB), not in the repository. Observations only; nothing is settled (S28).*

---

## 0. In short

- **The reload keeps the resource levels exactly** (S113's runner carries them; the next piece starts at the printed level to six figures), **but disturbs them for some updates after**: in the first 20 updates after a reload a resource level moves by a median 13% per update, against 3.6% in an unbroken run (section 3).
- **FIXED GRADED: no measure moved consistently.** Common capabilities, the nine tasks' prevalence and generations differed between the two ways in different directions in different seeds; the differences are of the same size as those between seeds.
- **COMMON TASKS PAY LESS: one threshold counts by the plan's letter, generations (15% to 30% fewer in pieces, all three seeds), but a follow-up check shows this is mainly a difference in how generations are counted, not in the process.** Three other measures lean the same way in all three seeds without reaching their thresholds: births 5% to 10% lower, common capabilities lower just after a reload, and common capabilities over the second half lower in two seeds and equal in the third (−2.5, −1.8, 0).
- **Generations in S113 cannot be read from `average.dat` as they stand** (each piece restarts the count at 0), and even summed over pieces they are not comparable with an unbroken run's.
- **Every run and check ran as planned**; two things were added after the first results were seen, and one threshold rested on a wrong assumption (section 6).

## 1. What was run

As planned: FIXED GRADED and COMMON TASKS PAY LESS, seeds 11401, 11402, 11403, each **in pieces** (S113's own `run_one`, imported and called unchanged, 10 pieces of 1,000 updates) and **continuous** (one Avida process of 10,000 updates, same files and seed as the first piece). 12 runs, all exit 0; pieces 702 to 833 s per run in all, continuous 650 to 881 s. S113's runner (process 2411) was alive throughout, so **one Avida process at a time** throughout. Checks C1 (the extra printing), C2 (resources just after a reload) and C3 (Astra's native examples, reported in `S114 Checking GPT 6 Astra's reply.md`) as planned; the follow-up check of section 4 added.

**C1, the extra printing changes nothing**: in all six pairs, the continuous run's first 1,000 updates (task counts, program counts, births and instructions executed at 250, 500, 750 and 1,000) are identical to the first piece's. So the two ways part only at the first reload.

**C2, a piece is repeatable**: rerunning piece 5 of COMMON TASKS PAY LESS seed 11401 from the same saved program population and seed gave task and program counts identical to the original, line for line.

## 2. The thresholds (plan, section 3)

Differences are PIECES minus CONTINUOUS, one per seed (11401, 11402, 11403), over the piece-end samples at 5,000 to 10,000 unless said. "Counts" = all three the same direction and the smallest at least the threshold.

### FIXED GRADED

| Test | Differences by seed | Verdict |
|---|---|---|
| T1, common capabilities (of the 77, ≥10% of programs), mean 5,000-10,000 | +0.17, −0.67, +1.00 | not separated by three seeds |
| T1, at 10,000 | 0, 0, +1 | not separated |
| T2, prevalence points, each of the nine two-input tasks | none same-signed at 5 or more; ORN +5.9, +9.1, +3.5 | none counts; ORN same direction, below the threshold |
| T3, generations at 10,000 (sum of piece ends against continuous) | +17.2%, +20.2%, −21.5% | not separated |
| T5, just after a reload (local update 250): common | +0.56, −0.89, +0.22 | not separated |
| T5, births | +55%, +99%, −7% | not separated |
| T5, prevalence | none same-signed at 5 or more; OR −1.4, −1.1, −4.8 | none counts |

The largest single differences in prevalence are big (NAND −29 points and EQU +48 points in seed 11403; AND −27 and NOR −26 in 11402), but in no task the same way in all three seeds. Births at the piece ends: +81%, +92%, −8% (in seeds 11401 and 11402 the continuous runs' program populations came to replicate about half as often from update 2,000 on, with longer gestation; not in 11403).

### COMMON TASKS PAY LESS

| Test | Differences by seed | Verdict |
|---|---|---|
| T1, common capabilities, mean 5,000-10,000 | −2.50, −1.83, 0.00 | not separated (two fewer, one equal) |
| T1, at 10,000 | −2, −2, 0 | not separated |
| T2, prevalence points | none same-signed; XOR −23.5, −88.4, +27.1; EQU −34.0, −79.3, +22.0 | none counts |
| T3, generations at 10,000 | −20.2%, −30.2%, −15.5% | **counts** by the plan's letter; see section 4 |
| T4, resources reset at a reload: level written for the next piece against the level printed at the piece's end | largest difference 0 (every reload, every seed) | **no reset** |
| T4, second clause: C2's printed level at update 0 against the level written | up to 58% | counts by the letter, but the clause rested on a wrong assumption; see section 3 |
| T5, common | −1.44, −1.33, −0.67 | same direction, below the threshold |
| T5, births | −2.4%, +10.1%, −9.6% | not separated |
| T5, prevalence | none same-signed at 5 or more | none counts |

Births at the piece ends, 5,000 to 10,000: **−5.7%, −9.8%, −4.6%**, the same direction in all three seeds, below the 10% used for births in T5 (no threshold was set for births at piece ends).

## 3. Resources at a reload

- **Carried exactly.** At all 27 reloads (9 per seed), the level S113's runner wrote into the next piece's environment file equals the level Avida printed at the end of the piece, to the six figures Avida prints. Nothing is reset.
- **Then disturbed.** The plan's second T4 clause assumed that Avida's print at update 0 comes before any running. It does not: the continuous run prints 99.49 at update 0 for every resource, which is its starting level 0 plus one update's inflow of 100 less its outflow. So C2's print at update 0 is the level **after the first update** of the reloaded piece, and its difference from the level written (up to 58%, median 18%) is consumption, not a reset. It is still a disturbance: over the first 20 updates after that reload, the levels in use move by a median **13%** per update (99th percentile 48%), against **3.6%** (99th percentile 19%, largest 32%) in the continuous run of the same seed over updates 5,000 to 6,000. The levels swing with a period of about 6 to 8 updates (for example resNOT: 125.7 written; 52.3, 51.9, 94.5, 106.8, 114.4, 112.4, 97.1, 76.3, 68.3, 87.1, 115.1, 136.8, 169.4 over updates 0 to 12). The likely reason, not tested: every loaded program starts its instruction sequence from the top at the same moment, so their task performances, and the resource they draw, come in waves until the programs drift out of step. How long the waves last was not measured (C2 printed every update only to update 20).

## 4. The follow-up check: does the reload itself change replication? (a departure)

Added after the first results were seen, because in seeds 11401 and 11402 of FIXED GRADED the runs in pieces had about twice the births of the continuous runs. It separates "the program populations evolved differently" from "the reload makes the same programs replicate differently": each continuous run's program population saved at update 5,000 was loaded exactly as S113 loads a piece (S113's environment and event text, unchanged; for COMMON TASKS PAY LESS the continuous run's resource levels at 5,000 carried as S113's runner would; seed 1,000 × seed + 5) and run for 1,000 updates, printing births every update.

| Environment, seed | births per update after the reload: updates 1-10, 250-1,000 | continuous, updates 5,250-6,000 (4 samples) | gestation time at the end: reloaded, continuous | generations over the 1,000 updates: piece measure, continuous increase |
|---|---|---|---|---|
| FIXED GRADED 11401 | 121, 136 | 124 | 444, 445 | 124, 267 |
| FIXED GRADED 11402 | 37, 71 | 75 | 958, 944 | 55, 73 |
| FIXED GRADED 11403 | 158, 179 | 172 | 390, 405 | 145, 140 |
| COMMON TASKS PAY LESS 11401 | 229, 212 | 214 | 302, 306 | 225, 381 |
| COMMON TASKS PAY LESS 11402 | 191, 174 | 178 | 380, 384 | 125, 149 |
| COMMON TASKS PAY LESS 11403 | 221, 223 | 247 | 287, 289 | 186, 210 |

- **Births and gestation times after a reload are those of the unbroken run**, within the scatter of the continuous run's own samples (from +10% to −9%), apart from a dip in the first 10 updates in two of the three FIXED GRADED populations (121 and 37 against 124 and 75; the programs restarting their copies). So the doubled births of FIXED GRADED seeds 11401 and 11402 in pieces were **evolution**: their program populations took different courses, not a direct effect of the reload.
- **The generation measure differs between the two ways even when the process does not**: with births unchanged, the piece measure (the average generation at the end of a piece, counted from 0 at the reload) was lower than the continuous run's increase over the same 1,000 updates in 5 of 6 cases, by 16% to 54%, and higher in 1 by 4%. The reason, read from how Avida counts: a program's generation is the number of divisions along its line of descent; in an unbroken run, when a line with a long history of fast replication spreads, the average rises by that history too; a reload erases every history, so the piece measure counts only what happens inside the piece. **So T3's count for COMMON TASKS PAY LESS is mainly, perhaps wholly, a difference in the measure, not a change in the process**; the audit cannot say how much of it, if any, is left. Births, the direct measure of replication, were 5% to 10% lower in pieces in all three seeds; in the follow-up, 1%, 2% and 9% lower. Both below 10%.

## 5. What it means for reading S113 (plan, section 4, applied)

- **FIXED GRADED**: no threshold counts. S113's piece-end numbers for this environment can be read as those of unbroken runs, at the scale of the thresholds (one common capability, five prevalence points). But the two ways differ from each other as much as two seeds do (up to 48 prevalence points in one task, and twice the births in two of three seeds), so any statement about FIXED GRADED in S113 needs the spread across its three seeds, not one run.
- **ONE HARD TASK ONLY, NO TASK REWARDS, FIXED LARGE LIST** (the same pieces, no resources): assumed to behave like FIXED GRADED; **not shown**.
- **COMMON TASKS PAY LESS**: the resource levels are carried exactly, so the environment is the one S113's plan describes; but each reload sets off swings in the resource levels, and the runs in pieces leaned, in all three seeds and below every threshold, towards fewer births (5% to 10%) and fewer common capabilities just after reloads, and in two seeds towards about two fewer common capabilities over the second half (XOR and EQU much less prevalent). The plan's rule does not call this a change; it is not excluded either. **Any S113 comparison that turns on one or two common capabilities between COMMON TASKS PAY LESS and another environment (the plan's E6: at least as many common capabilities as FIXED GRADED) should be read as possibly lowered for COMMON TASKS PAY LESS by the pieces.**
- **GROWING LIST**: its reward changes happen only at the breaks; the break is part of that environment, and this audit does not separate it.
- **Generations, all environments**: S113's `average.dat` generation at a piece's end counts only that piece. Summed over pieces it is still not the same measure as an unbroken run's average generation (section 4), and the bias depends on how strongly lines of descent sweep, which differs between environments. **S113's generations should not be compared with S111's, nor between S113's environments, as generations; births per update (`count.dat`) are the safer measure of replication.**
- **The samples at local update 250**: T5 did not count in either environment; S113's 250-update samples need not be left out on this evidence, but in COMMON TASKS PAY LESS they lean lower (common capabilities −1.4, −1.3, −0.7).
- **Update 0 after a reload**: `count.dat` there counts every loaded program as a birth; S113 does not sample it.

## 6. Departures from the plan

1. **The follow-up check of section 4** was added after the first results were seen (new script `tools/s114_restart_audit_reload_the_continuous_populations.py`; six runs of 1,000 updates, one at a time, all exit 0). It changes no planned verdict; it bears on how T3 is read.
2. **The second clause of T4 rested on a wrong assumption** (that Avida's update-0 print comes before any running). Reported by its letter (counts), with what it actually shows (section 3); the comparison of per-update changes against the continuous run was added to the comparison script to show it.
3. **Births at the piece ends** were compared (not in the plan's thresholds; reported as observations only).
4. Nothing was cut: all three seeds ran in both ways for both environments. Astra's native examples used seeds 11401 and 111401 as planned.

## 7. Astra's cost estimate (claim 39 of the check)

Astra estimated its own restart audit (six runs of 5,000 updates) at about 0.6 CPU-hours. Measured here, a continuous 10,000-update run took 650 to 881 s with three other Avida processes running beside it, so six 5,000-update runs would take about 0.55 to 0.73 CPU-hours: **holds**.

## 8. What was not measured

The other four S113 environments; more seeds or longer runs; how long the resource swings last after a reload; the effect of the new random seed at each reload apart from the reload's other losses (stock Avida saves no random state); lines of descent; S113's own runs, which were not read or touched.
