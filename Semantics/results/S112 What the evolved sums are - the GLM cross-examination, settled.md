# S112 What the evolved sums are - the GLM cross-examination, settled

*Written 30 September 2026 by one Opus 5.5 agent (decision S56), under rules 3 to 6 of `results/S112 What the evolved sums are - how the GLM cross-examination will be read, written before sending.md` (committed bb63fb2 before sending). This agent did not do the work cross-examined; it weighs arguments, not their source. In the owner's Avida terms (decision S61). Created at once and filled as the settling went; finished. Nothing here changes the theory's text, formal core, claims or program, any Part A, Part B, S110 or S111 file, the decisions record, the S61 terms file or `authority/`; the S112 files as sent are kept unchanged.*

## 0. The condition for opening, and what came back

The run log (`S112 What the evolved sums are - GLM cross-examination returns/run log.txt`) ends "s112x_glm_loop: every pass ended; accepted 4 of 4 jobs" and "loop ended 2026-09-30T03:51:20Z"; the process had exited. Receipts: key_found_in_output_and_replaced = 0 and sandbox_unchanged = true for all four; model glm-5.3; each reply ends END OF REPORT (a 2,232 words, b 1,512, c 1,424, d 1,193). Returns at commit b212c6f.

| job | angle | objections | stand | stand in part | do not stand |
|---|---|---|---|---|---|
| a | whether the answer answers the owner's two questions exactly | 10 (Xa1–Xa10) | 9 | 1 | 0 |
| b | the minimal-removal search (instruction ablation) and its limits | 6 (Xb1–Xb6) | 4 | 2 | 0 |
| c | the circuits and their canonical forms against the traces | 6 (Xc1–Xc6) | 5 | 1 | 0 |
| d | the plain-words file against the results | 10 (Xd1–Xd10) | 8 | 2 | 0 |
| all | | **32** | **26** | **6** | **0** |

GLM's own ids (X1.1 … X4.10) are renamed Xa1 … Xd10 in the order each reply gives them. What each job checked without objection, and what it did not reach, is in its reply; nothing there is taken as agreement. Points raised by several jobs (Xb5 and Xc1; Xa9 and Xc2; Xa10, Xb6 and Xd2; Xb1 and Xd3) decided nothing by their number; each was settled on its own argument.

**What was used to settle**: the plan, the results and their `.json`, the five S112 scripts, the raw output in the scratch space, Avida in analysis mode. **Reruns and new checks**, all in the scratch space (`<scratchpad>/s112x_settle/`), Avida's analysis mode only (the test processor and `TRACE`; nothing self-copying ran on the real machine), each under a timeout, at most three workers at once on 4 processors:

- **R-NOT-15-17** (for Xa2): the NOT worked example with site 15, then site 17, ablated; the test processor and Avida's trace, read by the trace reader (`tools/s112x_settling_checks.py`).
- **R-pairs-with-replication-sites** (for Xb1, Xb2): for the 91 sequence-task pairs the sent search left at 3 or more or not stopped (48 distinct instruction sequences), the sent search's two start sets run again, and every pair of sites holding at least one site whose single ablation stops replication ablated (112,396 Avida programs run; same script).
- **R-reread** (for Xc6, Xc3): the 1,399 distinct instruction sequences with a `nand(ONES,ONES)` part in any route or a constant folded as OTHER in a credited route, traced by Avida again and read by the corrected copy of the trace reader (`tools/s112_read_what_the_programs_compute_from_avidas_traces_after_the_cross_examination.py`); every field of their records other than the reduced forms came out the same as sent (1,399 of 1,399; 0 steps where the replay differs from the trace); 1,462 routes' reduced forms changed, all of them routes that held `nand(ONES,ONES)`.
- **R-summary** (for Xa7, Xb1, Xb3, Xb4, Xc3, Xc6): the corrected copy of the summariser (`tools/s112_summarise_what_had_to_be_removed_and_what_it_is_after_the_cross_examination.py`) wrote `results/S112 What the evolved sums are - what had to be removed and what it is, after the cross-examination.json`; every number it shares with the sent `.json` came out the same except those the reduced-form correction changes (listed under Xc6).
- **Read, not rerun**: the `.json` as sent (`ablation_against_routes`, role tables, `single_site_stops_it_vs_number_of_routes`, environment denominators); the summariser's code (units, denominators); the trace records of the OR and XOR worked examples (Xc4); Avida's accept lists as the reader holds them (`cTaskLib.cc` 513-575, for Xd8); decision S23's wording (Xd9); the plan's section 5 (Xa1).

## 1. Job a: whether the answer answers the owner's two questions exactly

**Xa1. The plan's "removal against route" check is computed but not reported, and it counts against conclusion (1).** *Stands.* The plan (section 3) asks "whether each minimal removal set cuts every route of the sum" and (section 5) names its failure as counting against (1). The `.json` holds it; the `.md` did not report it or list the omission. Numbers (from the `.json`): of the required single sites, 748,700 of 904,433 (82.8%) lie in every route of the task, from 77.6% (NOT) to 88.1% (NAND); 155,733 (17.2%) stop the task with some route not containing them; of the minimal pairs, 233,060 of 876,577 (26.6%; NOT 47.8%) do not hold a site of every route. **Changes**: a paragraph in section 2 of the corrected copy, saying that in this share what had to be removed is not the route's instructions, as the plan said; a sixth departure item. The headline (98.0% stopped by one site) does not move; its reading as "the route's instructions" is limited by it.

**Xa2. Site 15 in the NOT example is glossed as a register choice of the instruction before it, which reads as the `pop`'s; it is the `dec`'s, outside the route.** *Stands.* **Rerun (R-NOT-15-17)**: site 15 (`nop-C`) follows `dec` at 14; in the program as it is, the `dec` takes one from CX, which the `pop` at 16 then overwrites. With 15 ablated, the `dec` takes one from BX, where B sits; the `nand` at 20 combines B − 1 with B; no output of the run is NOT; the program replicates and keeps its other seven tasks. Site 17 (the `pop`'s own register choice) ablated: the `pop` puts B into BX, CX keeps the all-ones the `dec` made from zero, and the `nand` at 20 computes nand(B, all ones) = NOT B, credited at the same output, 26. GLM's own account of 17 (a later hand-out at 34 carries it) is not what the trace shows; GLM asked for the rerun if unsure. **Changes**: section 2.1 of the corrected copy; plain file section 3.

**Xa3. "Only given Avida's meanings" claims more than was tried.** *Stands.* Two other meanings of the `nand` letter, `IO` as nothing and three shufflings were tried; no other. **Changes**: section 4's conclusion and section 0 say "under none of the other meanings tried; other single changes of meaning were not tried"; plain file section 5 likewise.

**Xa4. The `IO`-off row cannot come out otherwise; it shows the credit's dependence, not the computation's.** *Stands in part.* The outcome is fixed by Avida's rules, as the plan predicted, and the file presented it as a finding: that stands. But the computation's dependence is shown too, by argument: numbers enter the registers only through `IO`, so with it doing nothing no input reaches any circuit. **Changes**: section 4 says both, and that the row's other content is that 83% to 89% still replicate; plain file section 5 likewise.

**Xa5. The unit of "80% of cases (1,081,852 of 1,359,165)" is unstated.** *Stands.* In the summariser the count is per site and task (each replication-required site once per task the program performs). **Changes**: section 5 names the unit.

**Xa6. The role list leaves out constant-making.** *Stands*, with the range corrected: 0.1% (NAND) to 6.3% (NOT) of required sites weighted by Avida programs (GLM's "2% to 6%" is not the range). **Changes**: section 2's role paragraph.

**Xa7. "The same kinds and roles, in every run" rests on pooled tables.** *Stands*, and the split made for it changes the sentence. **R-summary**, run by run: the same kinds are required in every run, but their shares differ widely: for NOT, `IO` 14% to 49% of a run's required sites and `nand` 0% to 42% (one run's NOT programs make NOT by arithmetic, `sub(ONES, x)`); for XOR, `IO` 15% to 32%; the most frequent role is the gate in some runs, the register choice, the mover or arithmetic in others. **Changes**: section 2 ("What the programs share across runs"); the run-by-run shares in the `.json`; plain file section 7.

**Xa8. "A route's required instructions execute in one order" is not checked across programs.** *Stands*, and more: even the worked examples interleave reads and gates (XOR reads at 47 and 48 after the `nand` at 43; NOR and EQU read B at 66 after four arithmetic steps). What holds is what the data flow requires: a gate runs after the reads of the numbers it combines, the output write last. **Changes**: section 2 says so, and that the order of the required instructions outside the route was not checked.

**Xa9. The prediction denominators (82,347; 79,266; 76,805) are not explained.** *Stands.* They are the sequence-task pairs whose program still replicates under the change (`x['viable']` in the summariser). **Changes**: section 4, three places.

**Xa10. Plain file: "because the program did it in two places" drops "almost always".** *Stands* (18 of the 1,664 have one route in the trace). **Changes**: plain file section 3 ("almost always") and section 1.

## 2. Job b: the minimal-removal search and its limits

**Xb1. The pair, triple and irreducible searches try only sites whose single ablation leaves replication; a second ablation can let replication go on again, so the "none found" and the minimum can be wrong.** *Stands*, and a number in the results moves. **Rerun (R-pairs-with-replication-sites)**: of the 89 sequence-task pairs counted as not stopped, **85** (NOT 41, ORN 44; 91 Avida programs) are stopped by a pair holding one site whose single ablation stops replication and one other site: ablated together, the program replicates and the task is gone (for example the `IO` at 18 and the `nand` at 81 of a high-seed-3 sequence; 671 of the 112,396 pairs tried left replication). **4** (NOT, 4 Avida programs) remain stopped by no set of one or two sites; the 2 stopped by three are stopped by no such pair. For every other sequence-task pair the smallest size cannot change (one site already stops it, or a pair does and no single site can). **Changes**: section 0 (the 2.0% split: 1,573 + 85 pairs, 2 of three, 4 none), section 2's table (NOT 671 + 41 and 4; ORN 265 + 44 and 0), section 5, section 7 (not tested: such sets elsewhere); the `.json` gives the smallest set after the rerun; plain file sections 1, 3, 6, 7. The headline, 98.0% (98.6% by program) stopped by one site, does not move.

**Xb2. The reason given for the 89 ("every instruction of their task is also an instruction of their replication") is not what the search shows.** *Stands.* **Rerun**: in all 89, the search's second start set (every copying-safe site ablated at once) stopped replication, so "not stopped" came from that set; the route start set left the task performed. From the data: in 80 of the 89, every route of the task holds a site whose single ablation stops replication (in 87, an `IO`, a `nand` and a `swap` of the route are such sites); 62% of their route sites are such. And 85 of them are stopped by a pair (Xb1). **Changes**: section 5 rewritten with these counts; plain file section 3.

**Xb3. "Minimal pairs total 876,577" and the irreducible set sizes (3; 5, 6) have no source in the `.json`.** *Stands in part.* 876,577 is in the sent `.json` as the sum of each task's `pair cuts every route` and `pair does not cut every route` (643,517 + 233,060), unnamed; the sizes were only in the raw output. **Changes**: the corrected `.json` writes `minimal_pairs_total` per task (NOT 276,926 … XOR 8,435) and the irreducible sets' sizes (five orders each: 3, 3, 3, 3, 3 and 3, 3, 3, 5, 6); section 2 and 5 cite them.

**Xb4. "Because the program no longer splits" is a reading; the splitting was recorded but not reported.** *Stands in part.* The splitting was recorded only for the 159 traced sites of the nine most common sequences: of the 116 credited with no task, 113 did not split in the trace; 43 split and were credited with some task; 3 split and were credited with none. So in that sample the reading holds for 113 of 116; over the 1,359,165 cases it is not counted. **Changes**: section 5 reports these counts and says "in keeping with"; the `.json` holds them per run.

**Xb5. "Program-task pairs" are counted by distinct instruction sequence.** *Stands* (83,725 is the sum of the sequences column). **Changes**: "sequence-task pairs" throughout the corrected copy; the plain file says "pairs of an instruction sequence and one of its sums".

**Xb6. Plain file drops "almost always".** *Stands*; as Xa10.

## 3. Job c: the circuits and their canonical forms against the traces

**Xc1.** As Xb5. *Stands.* Same change.

**Xc2.** As Xa9. *Stands.* Same change.

**Xc3. Constants folded as OTHER are written OTHER whatever their value, so circuits that differ only in such a constant count as one.** *Stands.* **Rerun (R-reread, R-summary)**: with each such constant written with its value, the distinct reduced circuits of credited routes become NOT 415 (347 without values), NAND 247 (243), AND 119 (100), ORN 223 (207), OR 417 (404), ANDN 180 (175), NOR 190 (174), XOR 40 (35), EQU 68 (59). **Changes**: section 0 and 3 give both counts; section 7 says the forms without values are lower bounds in that respect; plain file sections 4 and 6.

**Xc4. The OR and XOR examples leave out executed `IO` between the gates and the output, on which the logic ids depend.** *Stands in part.* The examples list the route's steps and the required rotation `IO`s; 67 (and, for XOR, 78) are executed, not required, and outside the route (trace record read: site 67 `IO`, executed). The list did not claim to hold every executed `IO`, but without them a reader cannot recompute the ids 252 and 90. **Changes**: section 3.1 names them.

**Xc5. "0 differing steps" checks the replay's numbers, not the provenance it carries.** *Stands.* **Changes**: section 7 (Unsure) says so, and names what bears on the provenance too (the first accepted output equals Avida's own credit in 83,725 of 83,725; the predictions under changed meanings match for 99%).

**Xc6. In the reduced form, `nand(ONES,ONES)` is kept as a part though it is the constant ZERO.** *Stands*, and it occurs: 170 credited routes and 1,292 other routes held it (as the first part of chains such as NOT's `nand(ONES,ONES); nand(g1,x0); nand(g2,x1)`, which reduces to one `nand` of an input with itself). **Rerun (R-reread, R-summary)** with the fold added: distinct reduced circuits NOT 350 → 347, NAND 248 → 243, AND 102 → 100, ORN 211 → 207, OR 409 → 404 (ANDN, NOR, XOR, EQU unchanged); over all routes NOT 1,190 → 1,182, NAND 3,296 → 3,280, AND 151 → 149, ORN 17,870 → 17,790, OR 899 → 892; accepted on all eight combinations NOT 250 → 247, NAND 230 → 225, AND 69 → 67, ORN 174 → 170, OR 383 → 378; function groups NAND 170 → 165, ORN 121 → 118, OR 283 → 278; the top NOT circuit 13,520 → 13,557 Avida programs, 7,925 → 7,959 sequences, 347 → 352 route strings (still 63%); AND's two-gate row 1,015 → 1,016 sequences, 110 → 111 strings; ORN's second row 2,322 → 2,346 sequences. No share in the most-common table moves; the smallest circuits do not move; "save one" does not move. **Changes**: the corrected reader and summariser; section 0, 3, 5 of the corrected copy; plain file sections 4 and 7.

## 4. Job d: the plain-words file against the results

**Xd1. "Most of these are extra reads" is not what the data show.** *Stands.* Among required sites outside the route, `IO` outside the routes is the largest group for AND, ORN and EQU (40% to 57% of them), and not for the other six, where register or head choices of instructions outside the routes lead (42% to 60%), with control instructions next. **Changes**: plain file section 3.

**Xd2. Section 1's direct answer misdescribes the residual 2%.** *Stands.* **Changes**: plain file section 1, now with the rerun's numbers (almost always two places; a few needed three; 4 not stopped).

**Xd3. "Every pair of instructions" claims more testing than was done.** *Stands* (Xb1). **Changes**: plain file sections 3 and 6.

**Xd4. "One from each place" is stated as universal; the results allow a rotation read and one route site.** *Stands in part.* The results' own qualifier is added; the new pairs of Xb1 (one site needed for copying and one other) are told in the next bullet. **Changes**: plain file section 3.

**Xd5. Reading in and handing out are one instruction, listed as two kinds.** *Stands.* **Changes**: plain file sections 1 and 2.

**Xd6. "Five kinds of step" is in neither results file.** *Stands.* **Changes**: "a few kinds of step".

**Xd7. The reshuffled meanings: a few letters kept theirs by chance.** *Stands.* **Changes**: plain file section 5.

**Xd8. "A different sum": logic id 139 is not one of the nine.** *Stands* (139 is in no accept list). **Changes**: "no longer EQU, nor any of the nine sums".

**Xd9. The note says none of the removed words is used, but §6 says Avida "would not accept".** *Stands in part.* "Accept" is not among the words S23 removes, so the note's claim holds; but S23 gives "accept" one meaning wherever it is used (tentatively accepted), and §6 used it in a machine's sense. **Changes**: "would not take".

**Xd10. "In its population": the owner's terms give "program population".** *Stands.* **Changes**: plain file section 3.

## 5. Recorded for the owner, not applied

- **Where the environment is** (job a, not reached): whether the owner's "the environment it was instantiated in" (S60) means the Avida world, with neighbours and changing inputs, rather than the test processor where each program runs alone. The S112 files measure the test processor and say so; the world's counts are higher and the reason is unchecked. Which the owner means is the owner's to say (S28, S21).
- **Whether what was removed is "the evolved information"** (from Xa1): 17% of the required single sites stop the task without cutting every route, through the input rotation, the control flow or other state. Whether those count as part of what the owner asks "that evolved information actually is" is a reading of S60 beyond what the files set out; recorded, not applied.
- Nothing here settles what knowledge is, how "causes itself" is read, or log S111's open question on whether the program itself resists change.

## 6. What changed

- `results/S112 What the evolved sums are - what had to be removed and what it is, after the cross-examination.md` and `.json` (every amendment marked with its id).
- `tools/s112_read_what_the_programs_compute_from_avidas_traces_after_the_cross_examination.py` (Xc6, Xc3), `tools/s112_summarise_what_had_to_be_removed_and_what_it_is_after_the_cross_examination.py` (Xa7, Xb1, Xb3, Xb4, Xc3, Xc6), `tools/s112x_settling_checks.py` (the reruns); the scripts as sent are unchanged.
- Plain file 112, updated to follow the check, with a section on what the check changed and one next step.
- **Headline numbers and the direct answers**: unchanged (98.0% of sequence-task pairs, 98.6% of Avida programs, stopped by one instruction; the kinds of required instruction; the most common circuits and their shares; the environment tests). What moved: the 2% remainder (89 not stopped → 4; 85 stopped by pairs holding an instruction needed for copying), the distinct-circuit counts (Xc6, Xc3), the wording of what was tried (Xa3, Xa4), and what the required instructions are against every route (Xa1) and run by run (Xa7).

## 7. Unsure

- The rerun of Xb1 tried pairs holding a replication-required site only for the 91 left over; triples of that kind were not tried anywhere, so the 4 and the 2 may still have smaller sets.
- The corrected reduced form folds `nand(ONES,ONES)`; other constant parts built from input-bearing parts (for example `inc` of a part that reduces to ZERO) are not folded; none was raised or looked for.
- The run-by-run shares (Xa7) are counted over required sites; a run with few performers of a task (XOR in three runs, EQU in six) gives shares from few programs.

Settled by Claude under decisions S17, S20, S21, S23, S28, S43, S56, S60 and S61. 30 September 2026.
