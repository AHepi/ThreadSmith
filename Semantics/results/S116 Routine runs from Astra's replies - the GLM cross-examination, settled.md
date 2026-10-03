# S116 Routine runs from Astra's replies: the GLM cross-examination, settled

*Written 30 September 2026 by the one Opus 5.5 agent settling log S116's GLM cross-examination (decisions S56, S68; no subagent or workflow), created at once after the returns were opened (1502ce9) and filled as the work went. It follows the reading rule committed before sending: `results/S116 Routine runs from Astra's replies - how the GLM cross-examination will be read, written before sending.md` (1f41d20). Its opening condition was met before anything was opened: the run log ends "s116x_glm_loop: every pass ended; accepted 4 of 4 jobs" and "loop ended 2026-09-30T18:48:47Z", and the process had exited; the receipts are clean (glm-5.3; no key in any output; every sandbox unchanged; the guard refused every command not allowed; each reply ends END OF REPORT). Returns: `results/S116 Routine runs from Astra's replies - GLM cross-examination returns/` (ef35af4). In the owner's Avida terms (S61, `records/Semantics - Avida terms, given by the owner.md`): all entities are digital programs executing on Avida's virtual CPU; nothing biological is involved; nothing that copies itself ran on the real machine. Observations only; nothing is settled for the owner (S28).*

**Ids.** GLM numbered its objections X1.1 to X4.10 by job; here job 1 is (a), job 2 (b), job 3 (c), job 4 (d), so X1.1 is **Xa1**, X2.3 is **Xb3**, and so on. An objection raised by two jobs is settled once and counted once in the totals (below).

---

## 0. In short

- **28 objections from 4 jobs: 21 stand, 7 stand in part, none does not stand.** Five are repeats of another job's (Xb4 = Xa6, Xc1 = Xa4, Xd5 = Xc4, Xd1 (i) = Xb1, Xb3 (i) = Xa2); counted once, **23 distinct: 17 stand, 6 stand in part.**
- **The input-order finding stands, and the check made it sharper** (Xa2, Xb3, settled by Avida's source and by a rerun). Avida's world does give a program's three input numbers in one fixed order (source cited below). Given the **same three numbers in all six orders**, and four fresh sets in the world's order, every S113 program population at update 50,000 was run again on the test CPU. The world's order gives S113's counts exactly in every run and every fresh set. But the results said more than the probe had shown: **one other order also works in GROWING LIST seed 2** (47 common, against 46 in the world's order; 0 to 3 in the other four), and **in FIXED LARGE LIST seed 1, four of the six orders work and two do not** (32 common, or 0 with about 110 to 200 of 3,484 programs still copying themselves). A **third run, FIXED LARGE LIST seed 2**, depends in part: 41 common in the world's order, 30 to 36 in the other five, 26 to 27 on the same numbers made small. The other 15 runs do not depend on the order. So: task performance, and in two runs program replication itself, depend on the order and size of the input numbers in three of the 18 runs; not "only in the world's order", but on it and on some orders and not others.
- **Headline numbers that moved**: "77% to 88%" reject all becomes **76% to 88%** (Xc4); the AND resource with A common becomes **about 120 to 295** (pay 1.5 to 2.8 times), not 140 to 240 (1.6 to 2.3) (Xb2); "2,377 and 2,381 copy themselves and perform NOT" becomes 2,377 and 2,381 copy themselves, 2,373 and 2,377 also perform NOT (Xb2). No verdict of the plan changes except **B2.1, which weakens**: by the plan's whole rule, only COMMON TASKS PAY LESS counts for accumulation in all three seeds, not "every environment except FIXED LARGE LIST" (Xa4, Xc1).
- **The bearing on S63 is unchanged in direction and softer in two places**: the rare-kind competition says nothing for or against the mechanism "common tasks pay less", because the one pair had no kind with a task of its own (Xa1); and "learning filled part of the list and then stopped" becomes "stopped rising within the updates run" (Xc5).
- **Reruns**: about 8 CPU-minutes of Avida in analysis mode (the order check, 18 runs); readings of S116's raw output (per-input counts, the AND resource, arithmetic ever seen). No run over the limit; nothing proposed and not run.
- **Amended in corrected copies**: `results/S116 Routine runs from Astra's replies - results, after the cross-examination.md` and `.json`; `tools/s116_gather_the_results_after_the_cross_examination.py`; `tools/s116_probe_the_saved_program_populations_after_the_cross_examination.py` (not run); the settlement's readings `tools/s116x_settle_*.py`. The files as sent are unchanged. Plain file 116 follows the check.

## 1. The reruns and readings

All in `<scratchpad>/s116x_settle/`, every Avida process under `nice -n 19` and a one-hour `timeout` (S116's wrapper), at most three at once; nothing read from or written into S113's folder (the copies S116 made were used).

1. **Avida's source on the inputs** (Xa2, Xb3 (i)). `avida-core/source/main/cEnvironment.cc`, `cEnvironment::SetupInputs` (from line 1252): in the world (`random = true`, no specific inputs set) input 0 is `(15 << 24)` plus 24 random bits, input 1 `(51 << 24)` plus random, input 2 `(85 << 24)` plus random; on the test CPU without random inputs (S113's test processor) the fixed `0x0f13149f`, `0x3308e53e`, `0x556241eb`, the same top bytes in the same order. A cell's inputs are set when a program is placed in it (`cPopulation.cc` line 1365). A program reads them in turn, wrapping round (`cPopulationCell.h` lines 214 to 218, `GetInputAt`; the `IO` instruction, `cHardwareCPU.cc` lines 4188 to 4200). Specific inputs are set only by an event (`EnvironmentActions.cc` line 1033); S113's runner uses none. So the claim holds; the source was not cited.
2. **The order check** (`tools/s116x_settle_order_check.py`; 18 runs x 22 input sets, analyze mode, about 8 CPU-minutes, every run exit 0). Common logic tasks at 50,000 (at least 10% of programs, credited and viable):

| run | world order (S113's numbers; probe set 0; 4 fresh sets) | same numbers, the other five orders (15,85,51 / 51,15,85 / 51,85,15 / 85,15,51 / 85,51,15) | same numbers made small |
|---|---|---|---|
| GROWING LIST seed 2 | 46 in all six sets | 0 / 0 / 3 / **47** / 0 | 0 and 28 |
| FIXED LARGE LIST seed 1 | 32 in all six | 32 / **0** / 32 / **0** / 32 | 0 and 0 |
| FIXED LARGE LIST seed 2 | 41 in all six | 30 to 31 / 30 / 36 / 32 to 33 / 33 to 34 | 26 and 27 |
| FIXED LARGE LIST seed 3 | 13 (S113's numbers), 14 (the others) | 13 or 14 | 13 and 14 |
| the other 14 runs | S113's count | the same count, or within 1 | the same (GROWING LIST seed 1: 65 and 60) |

   Programs that copy themselves, GROWING LIST seed 2: about 2,375 of 3,489 in the world's order, 2,250 in 85,15,51, 61 to 369 in the other four, 227 and 497 small. FIXED LARGE LIST seed 1: about 2,150 of 3,484 in the world's order, 1,930 to 2,060 in three others, 111 to 204 in 51,15,85 and 85,15,51, 33 to 73 small. Four more sets with other top bytes (40, 90, 120 and others) were run; they are not read as capability counts, because without the top bytes 15, 51, 85 one output can match several logic tasks at once (which is why Avida uses those bytes), and some runs gain counts there by that alone.
3. **Per-input counts from the probe's raw files** (`tools/s116x_settle_per_input.py`): reproduce every per-order number of results section 2.1 (2,377 and 2,381 viable; 62 to 370; 26 to 169 on small inputs; 1,921 to 2,164 and 137 on large), with one correction: of the 2,377 and 2,381 that copy themselves, 2,373 and 2,377 perform NOT.
4. **The AND resource** (`tools/s116x_settle_resource_levels.py`): updates 500 to 2,000, the lowest 107 to 136 and the highest 206 to 295 across the 15 runs; with A at 99%, 122 to 295.
5. **A's and B's copying time**: from the one analyze call made when the kinds were chosen (scratch `s116/competition_check/`, never committed as a script): A 577, B 545 instruction executions. Confirmed; now carried into the corrected `.json`.
6. **K's knockout file** (Xb3 (ii)): `analyze/cAnalyze.cc`, `AnalyzeKnockouts` (from line 4483) writes, in order, the sequence's id, lethal, detrimental, neutral and beneficial single ablations (lines 4610 to 4614). Checked on all 17,726 rows S116 read: lethal plus detrimental plus neutral plus beneficial equals the sequence's length in every row.
7. **Never-rewarded arithmetic ever seen by 50,000** (`tools/s116x_settle_arith_ever_seen.py`): NO TASK REWARDS 17 / 19 / 13; paying environments 12 to 21; not separated from NO TASK REWARDS in any environment.

## 2. Job 1 (a): do the runs answer what the plan says, and are the S113 comparisons fair

| id | objection, in short | settled | reason, and what it changes |
|---|---|---|---|
| Xa1 | "'Common tasks pay less' did not let a rare kind grow" is false as written: A grew from 1% | **stands** | A was rare at 1% and took the whole world. What the run shows is that the kind with one more paid task (AND) won from every start, and the kind with no task of its own lost; the case the mechanism needs (each kind with a task the other lacks) did not exist in this program population. The plan's label ("against: no growth from rare", fired by A rising from 99% in all three placements) stays as the plan's label; the headline, section 4 and section 8 are reworded: the result says nothing for or against the mechanism. |
| Xa2 | the world's fixed input order is stated as fact with no source | **stands in part** | The claim holds (section 1, item 1: source cited). But the rerun (item 2) shows the text went further than the probe's eight sets showed: one other order works in GROWING LIST seed 2, four of six in FIXED LARGE LIST seed 1, and FIXED LARGE LIST seed 2 depends in part. Section 2.1, section 8 and the headline are reworded; the world-order counts equal S113's in every run and in four fresh sets. |
| Xa3 | the S114 caution on COMMON TASKS PAY LESS is missing from section 2.1's comparison | **stands** | The plan carries it into any comparison turning on one or two capabilities; COMMON TASKS PAY LESS against FIXED GRADED (16 / 9 / 8 against 7 / 8 / 8) is one. One sentence added. |
| Xa4 | B2.1's environment verdict is not the plan's rule | **stands** (with Xc1) | See Xc1. |
| Xa5 | B3a.1's second clause was met before 1,000, so the verdict rests on the 10% clause alone, and the discriminating share fell from 1,000 to 5,000 "in 5 of 6 runs" | **stands in part** | The clause was met by 1,000 in every run (reject all most common at 1,000 and 5,000), so it did no work here; it could have failed (the founder's rule could have stayed most common), so "could not have failed" goes too far. The discriminating share fell from 1,000 to 5,000 in **4** of 6 runs (0.184 to 0.089, 0.247 to 0.106, 0.232 to 0.162, 0.161 to 0.092) and rose in 2 (0.174 to 0.191, 0.162 to 0.199). One sentence added; "lasts" was tested only to 5,000. |
| Xa6 | "support" (S23's list) in the plan's own sentence | **stands** | The plan (committed before running, 732cf7f) is kept unchanged as the record of what was fixed before running. The word is noted here; the sentence should have read "A positive result would be what E6's mechanism predicts, for this pair only". No S23 word is in the corrected results or plain file. |

**Job 1: 4 stand, 2 stand in part, 0 do not.**

## 3. Job 2 (b): the measures and the scripts

| id | objection, in short | settled | reason, and what it changes |
|---|---|---|---|
| Xb1 | "middle seed" 0.987 is the median, not seed 2 (0.933); the plain file attributes it to the wrong run | **stands in part** | The median of three is the value of the run in the middle by that share: for the growing list, seed 3 (0.933 / 0.987 / 0.988); for FIXED GRADED, seed 3 (0.871 / 0.966 / 0.92). So the number is the middle run's, not a wrong run's; but "middle seed" reads as seed 2. The key is renamed "median of the three seeds (the middle run by this share)" in the corrected `.json`, and the corrected results and plain file say so. |
| Xb2 | per-order counts, A's and B's copying time and the AND resource come from no committed script and are not recorded as departures | **stands** | All three were one-off readings of the raw output. Now read by committed scripts (section 1, items 3 to 5) and carried into the corrected `.json`; recorded as departure 6. Two numbers change: "copy themselves and perform NOT" 2,373 and 2,377 (not 2,377 and 2,381, which is the count that copy themselves); the AND resource with A at 99% 122 to 295, not 140 to 240, so AND paid A about 1.5 to 2.8 times, not 1.6 to 2.3. The conclusion (AND always paid A more than B's 6% faster copying) stands. |
| Xb3 | (i) the world's input order and (ii) the knockout file's columns are not in the build notes | **stands in part** | (i) as Xa2 (counted once); (ii) confirmed from source and on every row (section 1, item 6); nothing changes. The build notes are an S111 file and are not written; the source lines are recorded here and in the corrected results. |
| Xb4 | "support" in the plan | **stands** | Repeat of Xa6, counted once. |
| Xb5 | the growing list's reward history records a task one save early | **stands** | A task rewarded during piece k is first rewarded after update k x 1000, and the save at k x 1000 ends piece k - 1. Fixed in `tools/s116_probe_the_saved_program_populations_after_the_cross_examination.py` (marked [Xb5]); not run, because the summariser's reward label feeds no number or verdict in the results. |
| Xb6 | the bank reader counts a sequence as giving when its grants to a cue differ between pairs (mean exactly 5) | **stands in part** | The threshold would hide that case; but no bank has any such sequence (0 in all 12), so no number changes and no corrected copy of the reader is made (its output would not change). The count is now reported. |
| Xb7 | K's weighting and coverage not stated | **stands** | K is weighted by programs over the viable sequences of the 100 tested; the 100 carry 239 to 2,756 of about 3,500 programs at 50,000 (7% to 77%) and 300 to 677 at 5,000. Added to the caption and the corrected `.json`. |

**Job 2: 4 stand, 3 stand in part, 0 do not** (Xb4 and Xb3 (i) are repeats).

## 4. Job 3 (c): the results against the plan

| id | objection, in short | settled | reason, and what it changes |
|---|---|---|---|
| Xc1 | B2.1 "for accumulation in every environment except FIXED LARGE LIST" is not the plan's rule | **stands** | Applied in full, per run: **for** in 10 runs, **neither** in 7 (FIXED GRADED seeds 1 and 3, GROWING LIST seeds 2 and 3, and seed 3 of both non-paying environments), **against** in 1 (FIXED LARGE LIST seed 1). By three seeds, only COMMON TASKS PAY LESS is for in all three; no environment is against in all three; the two non-paying environments are for in two of three seeds, so this rule does not separate paying from not paying. The corrected results say so. B2.2 (kept) is untouched. |
| Xc2 | K's median and maximum, and never-rewarded arithmetic ever seen, planned and not reported | **stands** | Both now in the corrected `.json` and results (section 1, item 7): K medians move with the weighted means (for example GROWING LIST 53 / 37 / 46 to 74 / 82 / 75); arithmetic ever seen is not separated from NO TASK REWARDS, so B2.3's "against" holds by all three measures. Recorded as departure 7. |
| Xc3 | numbers in the `.md` without a counterpart in the `.json` | **stands** | Distinct sequences, viable counts at every save, per-input counts, copying times and resource levels are now in the corrected `.json`. No number changes except those of Xb2. |
| Xc4 | "77% to 88%" should be 76% | **stands** | 0.7642 (reputation, seed 102). Corrected. |
| Xc5 | "learning filled part of the designer's list and then stopped" generalises from one continued run | **stands in part** | Every S113 count stopped rising within the updates run (last new highs 15,750 to 48,250 by Avida's world count; GLM's "28,000 to 48,500" is not S113's), and the one run still rising at 50,000 rose no further; nothing was run past 75,000. Reworded to "stopped rising within the updates run". |

**Job 3: 4 stand, 1 stands in part, 0 do not** (Xc1 repeats Xa4).

## 5. Job 4 (d): the plain-words file against the results

| id | objection, in short | settled | reason, and what it changes |
|---|---|---|---|
| Xd1 | "middle run 98.7" is not seed 2; and the count is of logic and arithmetic tasks, not of the 77 "sums" the file defines | **stands in part** | (i) as Xb1 (counted once). (ii) stands: the plain file now says "of the sums and arithmetic sums". |
| Xd2 | "Programs came to rely on more of their instructions where sums were paid" hides FIXED LARGE LIST seed 3's fall | **stands** | Reworded: in three of the four paying environments. |
| Xd3 | "in every environment tried so far, the programs learned part of the list" is untrue where nothing was paid | **stands** | Reworded: in every environment that paid for easy sums. |
| Xd4 | "every run gives page 113's numbers exactly" holds for common counts only | **stands** | Reworded, and the order check's finer result put in. |
| Xd5 | 77 should be 76 | **stands** | Repeat of Xc4, counted once. |
| Xd6 | no next step of the work | **stands** | One next step added, leaving the choice to the owner (section 7). |
| Xd7 | "energy" not explained | **stands** | One plain sentence added. |
| Xd8 | NOT used before its explanation; AND never explained | **stands** | Both explained at first use. |
| Xd9 | the instruction count was made under the fixed list's pay in every environment; not said | **stands** | Said. |
| Xd10 | "different programs" and "kinds of program" for one thing | **stands** | One word kept: "kinds of program". |

**Job 4: 9 stand, 1 stands in part, 0 do not** (Xd5 and Xd1 (i) are repeats).

## 6. What the check changed, and what it did not

- **Changed**: the input-order finding is sharper and wider (section 0); B2.1's verdict is weaker; the rare-kind competition no longer reads as evidence against "common tasks pay less"; four numbers (76%, 2,373 / 2,377, 120 to 295, 1.5 to 2.8); "stopped" is limited to the updates run; eight reporting gaps are filled (K median and maximum, coverage, arithmetic ever seen, distinct sequences, per-input counts, copying times, resource levels, inconsistent grants); two departures added (6: readings of the raw output made after the results, now by committed scripts; 7: measures the plan named and the results left out).
- **Not changed**: every other verdict of the plan (B2.2 for; B2.3 against; B2.4 for with its limit; B2.5 against by the letter; B3a.1 for by the letter, B3a.2 sound; B3b.1 against by the plan's label; E levelled off); the headline counts of section 2.1's table; CPU time (3.8 hours for S116; the settlement's reruns about 8 CPU-minutes more).
- **The bearing on S63** keeps its direction: what was learned was kept; part of it is tied to how the world presents its numbers; what the world pays for is what it adds. It is softer in two places (Xa1, Xc5) and sharper in one (the order check).

## 7. Recorded for the owner, not applied

- Whether a capability that works only in the world's order of numbers (or in some orders and not others) counts as learned: the results report both counts and rule on neither; the check adds that some other orders also work. This is the owner's (S28), as are what knowledge is and how "causes itself" is read.
- Whether "common tasks pay less" should be tried again with a pair in which each kind has a task the other lacks, or in an environment where a common task stops paying altogether: a question of which environment to pursue, left to the owner (S21), with S111's and S112's open questions and the choice among S115's batches 4 to 9.
- Why three runs depend on the order of their numbers (which instructions do it) was not traced; the owner has said looking inside the machines is the wrong direction (S63), so it is not proposed.

## 8. Unsure

- The order check used one draw of fresh world-order numbers (four sets) and two sets of numbers in every order; a different draw could move the counts in other orders by a little (FIXED LARGE LIST seed 2 moved by one or two between the two sets).
- GLM saw no raw output; the settlement read it. What both missed can still pass.
- A's and B's copying times come from one analyze call made in the run and never committed as a script; they are now carried into the `.json` from that call's saved output, not recomputed.

Decided by Claude under decisions S28, S56, S61 and S68, following the reading rule (1f41d20). 30 September 2026.
