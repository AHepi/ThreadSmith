# S111 Avida - the GLM cross-examination, settled

*Written 29 September 2026 by one Opus 5.5 agent (decision S56), under rules 3 to 6 of `results/S111 Avida - how the GLM cross-examination will be read, written before sending.md` (committed 566eb03, amended b862f8c, before sending). This agent did not do the work cross-examined; it weighs arguments, not their source. Filled as the settling went; finished. It obeys decision S23 in Claude's own sentences; "candidate" or "explanation" for what the theory judges, never "model" (S43). Nothing here changes the theory's text, formal core, claims or program, any Part A, Part B or S110 file, the decisions record or `authority/`; the S111 files as sent are kept unchanged.*

## 0. The condition for opening, and what came back

The run log (`S111 Avida - GLM cross-examination returns/run log.txt`) ends "s111x_glm_loop: every pass ended; accepted 4 of 4 jobs" and "loop ended 2026-09-29T12:39:19Z"; the process had exited. Receipts: key_found_in_output_and_replaced = 0 and sandbox_unchanged = true for all four; model glm-5.3; each reply ends END OF REPORT (a 2,122 words, b 1,044, c 1,696, d 1,313). Returns at commit b679daa.

| job | angle | objections | stand | stand in part | do not stand |
|---|---|---|---|---|---|
| a | whether the measures measure the three properties as the owner stated them | 12 (Xa1–Xa12) | 6 | 6 | 0 |
| b | the scripts and the numbers | 4 (Xb1–Xb4) | 2 | 1 | 1 |
| c | what the program causes and what the simulated world does | 7 (Xc1–Xc7) | 2 | 5 | 0 |
| d | the plain-words file against the results | 7 (Xd1–Xd7) | 5 | 2 | 0 |
| all | | **30** | **15** | **14** | **1** |

GLM's own ids (X1.1 … X4.7) are renamed Xa1 … Xd7 in the order each reply gives them. What each job checked without objection, and what it did not reach, is in its reply; nothing there is taken as agreement. Several jobs raising the same point (Xa7, Xb2, Xc5; Xa8, Xc3; Xa11, Xb4; Xa6, Xc4) decided nothing by their number; each was settled on its own argument.

**What was used to settle**: the plan, the results and their `.json`, the four summary tables, the seven S111 scripts, the configuration, Avida's source and the raw run output in the scratch space. **Reruns and new checks**, all in the scratch space (`<scratchpad>/s111x_settle/`), Avida's analysis mode only (the test processor; nothing self-copying ran on the real machine), each under a timeout, three at once at most on 4 processors; the two scripts are committed as `tools/s111x_settling_checks.py` and `tools/s111x_settling_check_ancestor_lethal.py`, and their numbers are in `results/S111 Avida - the three properties measured, after the cross-examination.json`:

- **R-inputs-scan** (for Xa6, Xc4): the one-change scan of the nine most common genotypes at update 50,000, run again with the test processor's fixed inputs (it reproduced the sent numbers exactly) and with two other input triples (Avida's own pattern: the top eight bits fixed, the rest drawn with seed 1110).
- **R-inputs-tasks** (for Xa6): the genotypes covering 90% of each run's organisms at 50,000, each run in the test processor with the fixed inputs and the two other triples; the share performing each task.
- **R-evolved-map** (for Xc1): each run's most common genotype at 50,000, every site knocked out in turn with `nop-X`; its own essential sites; every organism aligned to that genotype (the same alignment as R3); the share still carrying its instruction, at its essential and at its other sites.
- **R-ancestor-lethal** (for Xa10): the ancestor's 2,500 one-change programs, counted by site.
- **Read, not rerun**: Avida's `Inject` action (`source/actions/PopulationActions.cc`, `cActionInject`) for Xb1; the header lines Avida wrote into `count.dat`, `time.dat` and `tasks.dat` of the runs, for Xb3; the test processor's inputs (`source/cpu/cTestCPU.cc` 233-251, `source/main/cEnvironment.cc` 1284-1288) for Xa6 and Xc4; `RECALCULATE`'s arguments (`source/analyze/cAnalyze.cc` 10261-10290); the Marletto summary table's JSON, split afresh, for Xa5.

## 1. Job a: whether the measures measure the three properties as the owner stated them

**Xa1. No measure measures the information itself causing its resistance to change; §8's second bullet lacks the world's part.** *Stands in part.* The factual half stands: §3's "Program or world" and §6 give the arrangement as "shaped by the world's weeding", and §8's second bullet does not say so; the corrected copy adds that clause (as §8's third bullet already does for sense (b)). The other half, that "in neither sense does the information itself cause the resistance", is a reading of the owner's "cause itself"; the S111 files leave that to the owner ("Whether 'cause itself' asks for more than this is the owner's to say"). **Recorded, not applied** (rule 5; S28, S21); it is listed in section 5 below.

**Xa2. §4's "Shown" misstates the plan's line ("present in most organisms at every save").** *Stands.* The plan's line and its measures (M2: the exact copy loop, the head, the essential-site conservation of R3, the whole ancestor) are as GLM quotes them. The exact-letter measures are not in most organisms; R3 is an average over sites, not a count of organisms; it is above one half at 52 of the 54 saves and below it at two (high seed 2: 0.38 at 40,000 and 0.495 at 50,000). The only per-organism measure is the added share whose genotype still copies itself exactly: 49% to 89% over all 54 saves, below one half only at update 1,000 in two high-rate runs (0.492, 0.498). **Changes**: §4's "Shown" says the line is met only in part, with these numbers; plain file §5 says so in everyday words.

**Xa3. The plain file's headline "The three properties were each found" says more than the results.** *Stands in part.* The results hedge by the plan's lines; the plain headline does not. GLM's replacement ("measured … each showed a program's half and a world's half") is close to right; the added clause on what stayed the same is already in the plain file's "Remains" bullet. **Changes**: the headline becomes "Each of the three properties was found in the sense the plan set out before anything was run, and each has two halves", and the note under the second property says the test was met for copying, not for speed (Xa4).

**Xa4. §3's "Shown" drops the plan's fitness clause.** *Stands.* The plan's line: "a large share of single changes leave copying and fitness unchanged". Fitness unchanged (one part in a million) in 14% to 36% of single changes, within 1% in 20% to 49% (per run at 50,000): not "a large share". **Changes**: §3's "Shown" quotes the line and says it was met in its copying clause, not in its fitness clause; plain file §4 likewise.

**Xa5. "Eliminating in every copy does" is overstated: 10% of organisms are untouched, and genotypes with no task-only site are left as they are and counted as performing.** *Stands*, and the split made for it sharpens it. The script (`s111_marletto_test_on_the_logic_tasks.py`, the `only_none` branch) counts a performing genotype with no task-only site (every site whose knockout stops the task also stops copying) as still performing, untouched. Split afresh from the summary JSON (uncapped): for **EQU, XOR and NOR the whole residue is these untouched genotypes** (EQU: 2.4% on average, 1.1% to 4.4%, all of it untouched); in every covered genotype that had task-only sites, knocking them out stopped the task. For OR all but 0.1 point is untouched; for NOT, of the 21%, about 6 points are untouched genotypes and about 15 points genotypes that still do NOT with their task-only sites knocked out (the "more than one route" of §5 applies to those); NAND 5 and 2, AND 3 and 5, ORN 4 and 4, ANDN 4 and 5. **Changes**: the headline becomes "Eliminating in every covered copy does"; §5 states both residues and the split; §8 and plain file §6 read the 1% to 4% as the untouched programs. No number in the table moves; what the EQU column's residue is changes.

**Xa6. "Reliably" is probed on one fixed pair of inputs.** *Stands in part.* The test processor does give fixed inputs (`cTestCPU.cc` 233-251; the triple is built so that every combination of bits is present, `cEnvironment.cc` 1284-1288). **Rerun (R-inputs-tasks)**: with two other input triples, the share of covered organisms performing each task moved by at most 1.8 points in any run (EQU by at most 0.6); 1.2% to 6.8% of organisms have a genotype whose set of tasks changes with the inputs. So "performs the task" holds across these inputs within two points. **Changes**: §5 states the fixed inputs and the check.

**Xa7. "0.2 to 1.4 points" should be "0.1 to 1.4".** *Stands in part.* The lower end is wrong, but the exact figure is 0.15 (high seed 2: 0.2992 to 0.2977, JSON); GLM's 0.1 comes from the two-decimal table. See Xb2.

**Xa8. The plan's "for comparison, the ancestor alone in the test processor" (C4) was left out unrecorded.** *Stands.* **Changes**: C4 gives the comparison by arithmetic from C1 (one copy per 389 instructions; at Avida's average of 30 instructions per organism per update, `AVE_TIME_SLICE 30`, about 0.077 births per organism per update in a world of ancestors), against the worlds' 0.075, 0.060 and 0.036; recorded as departure 12.

**Xa9. M1's "no world held fewer than 3,481 organisms" is from sampled updates.** *Stands.* The main worlds printed their counts every 1,000 updates (`MAIN_EVENTS`, `u 0:1000:end PrintCountData`). **Changes**: M1 says "at each of the 50 sampled updates"; plain file §5 likewise.

**Xa10. "Essential" is the `nop-X` knockout's; lethal changes also fall at non-essential sites (about 120 of 470), so R3's contrast is a lower bound.** *Stands in part.* **Rerun (R-ancestor-lethal)**: of the ancestor's 470 one-changes that stop copying, **373 fall at the 15 essential sites** (373 of the 375 changes there; every change is lethal at 14 of them, all but site 3) and **97 at the other 85 sites** (1 to 3 of 25 at each, 4.6% of their changes), not about 120. The knockout's split and the split by any change agree closely; the point that a few changes at "non-essential" sites also stop copying stands and is now stated. "Lower bound" is not applied: the per-site conservation was not recomputed by lethal share, so no bound is shown. **Changes**: a sentence in §3(b).

**Xa11. The C3 note's "for genomes that were no longer 100 long" describes a filter the script does not apply.** *Stands.* The world figure is the plain ratio of Avida's summed counts over every birth at the sampled updates. **Changes**: the clause is replaced (with Xb4 and Xc2).

**Xa12. The rewritten copy loops also align in more than one way, so the essential-site shares share the alignment's roughness.** *Stands in part.* Plausible and not measured; bounded by R-evolved-map (Xc1), where every organism is aligned to its own run's most common genotype and the essential-above-rest contrast holds in all nine runs. **Changes**: §7 "Unsure" extended.

## 2. Job b: the scripts and the numbers

**Xb1. K1 was not run as stated: `Inject random_%03d.org %d` with `i * 36` injects genotype i in i·36 copies.** *Does not stand.* The second argument of Avida's `Inject` is the cell, not a count (`cActionInject`: `m_cell_id`, then `Inject(*genome, …, m_cell_id, …)`). The runs' own `count.dat` for K1 shows, at update 0, 100 organisms of 100 genotypes, one in each of cells 0, 36, …, 3,564. The plan's "one per cell" is what ran. **Changes**: none.

**Xb2. The smallest EQU drop is 0.15 points, not 0.2.** *Stands.* Per run (uncapped): low 2: 1.36; low 3: 0.86; default 1: 0.38; default 2: 0.28; high 1: 0.16; high 2: 0.15. **Changes**: "0.15 to 1.4 points" in §5, the §6 table and §8 of the results, and in plain file §6.

**Xb3. The data-file column indices lean on layouts recorded nowhere in the folder.** *Stands in part.* The indices are right, checked against the header lines Avida wrote into the runs' files: in `count.dat` column 3 is the number of organisms, column 9 the births in the update, column 11 "number of breed true" (the script's `r[2]`, `r[8]`, `r[10]`, counted from 0); in `time.dat` column 3 is the average generation (`r[2]`); in `tasks.dat` columns 2 to 10 are the nine tasks in the script's order. No number moves. **Changes**: the columns are recorded in the corrected copy's §7. The `tasks.dat` header also says it counts organisms that "have the particular task as a component of their merit", which agrees with the inherited-merit reading of the world-versus-test gap in §5; noted there as the header's words, still not checked.

**Xb4. The C3 note's last clause misstates the measure; length is the difference.** *Stands.* With Xa11 and Xc2.

## 3. Job c: what the program causes and what the simulated world does

**Xc1. R3's split is the ancestor's knockout map, carried over to genomes whose copy machinery was rewritten; whether those sites are still essential was not tested.** *Stands in part.* The gap was real. **Rerun (R-evolved-map)**: in each run's most common genotype at 50,000, 13 to 22 sites stop copying when knocked out; with every organism aligned to that genotype, those sites still hold its instruction in **0.88 (low), 0.90 (default), 0.80 (high)** of cases on average (0.76 to 0.95 across runs), against **0.64, 0.56, 0.45** (0.39 to 0.70) at its other sites; **above in all nine runs**. The contrast does not rest on the ancestor's map. (Measured against the most common genotype, both kinds of site read higher than against the ancestor, since its relatives are near it; the comparison is between the two kinds.) **Changes**: §3(b) and the §6 row report the check.

**Xc2. The C3 row's three columns are not one measure: "expected" and "sampled" are the ancestor's; the world column counts the evolved populations' births.** *Stands in part.* The C3 note did say the world's genomes were "no longer 100 long", but not what follows. With the mean lengths of the saves (about 104, 109 and 101 over the six saves; 105, 109 and 88 at the last), the expected share is about 0.69 to 0.70, 0.40 to 0.41 and 0.12 to 0.16; each world figure (0.693, 0.400, 0.131) lies in that range. **Changes**: the C3 note says so; plain file §3 says the rates and the changed lengths, with the added and removed instructions (Xd1).

**Xc3. C4's ancestor comparison was dropped unrecorded.** *Stands.* As Xa8.

**Xc4. R1's "neutral" rests on test-processor fitness on fixed inputs.** *Stands in part.* **Rerun (R-inputs-scan)**: under two other input triples, the nine scans' neutral share moved by at most 0.009 and the viable share by at most 0.025 (default seed 3, 0.786 to 0.811); each most common genotype's fitness and task set were the same under all three; the low-beside-high verdicts at 50,000 (neutral and viable both higher at the high rate) are unchanged under both. **Changes**: §3(a) states the fixed inputs and the check.

**Xc5. "0.2 to 1.4" should be "0.1 to 1.4".** *Stands in part.* As Xa7: 0.15.

**Xc6. K3's "remains as well as one that can" overdraws the control.** *Stands.* K3 holds no copier. **Changes**: "remains too" (the plan's word).

**Xc7. The expected upper bound uses a 26-instruction draw; the sampled offspring were made with `nop-X` as a 27th.** *Stands in part.* The helper's folder appends `nop-X` for every analysis run, `SAMPLE_OFFSPRING` included, so the sampled column's errors were drawn from 27 instructions. The expected column describes the world (26), so line 55 is right for what it states; the difference to the sampled condition is below 0.001. **Changes**: a sentence in §7 item 8 and in the C3 note; the script is not changed.

## 4. Job d: the plain-words file against the results

**Xd1. The plain file never mentions the added and removed instructions (each one time in twenty per split), and without them the fidelity sentence is wrong.** *Stands.* From the copy errors alone, the low rate gives about 78 in 100. **Changes**: §2 adds the sentence; §3's sentence names both and the changed lengths.

**Xd2. The no-change control switched off all three kinds of change, not only copying mistakes.** *Stands* (`the exact commands.txt`, K5). **Changes**: §4's sentence.

**Xd3. "For as long as you like" is longer than the 2,000 time steps run.** *Stands.* **Changes**: §1.

**Xd4. The departures sentence on the control runs is wrong: three failed at once, the fourth ran without `nop-X`, and all five were rerun.** *Stands.* **Changes**: §7.

**Xd5. "The program runs, makes room, and never fills it" was not measured.** *Stands in part.* It is how Avida's rules read (`h-alloc` makes room, `h-copy` fills it), but no run looked at it. **Changes**: the example says only that no copy is made.

**Xd6. "The world writes a random instruction instead" hides that the draw can give the same one.** *Stands.* **Changes**: §2.

**Xd7. Two roundings of 15,940 (16,000 and 15,900); "the simplest sum, NOT" is not in the results.** *Stands in part.* The rounding stands; "simplest" is not wrong by Avida's own table (NOT is one of the two tasks with the smallest reward, `environment.cfg`), but the results do not say it. **Changes**: "15,900" in both places; "the sum NOT".

**Not reached by job d, settled here**: the "44 of the 3,600" in plain file §6: the most common genotype of low seed 2 holds 44 organisms (the JSON's `dominant.abundance`), and its knockout lowers the covered share by 44 of 3,240 organisms (1.36 points). As stated.

## 5. Recorded for the owner, not applied (rule 5)

- **Xa1, its second half**: that in neither sense measured does "the information itself" cause its resistance to change ((a) is an arrangement the world's weeding produced, (b) is the world's removal), so that the second property, as the owner stated it, is not shown. The S111 files give the observations (both are in §3 and §6) and leave "whether 'cause itself' asks for more" to the owner; applying the objection would settle how the three properties should be read.

## 6. What changed

- **Corrected copies**: `results/S111 Avida - the three properties measured, after the cross-examination.md` and `.json` (every amendment marked with its objection id; the new checks' numbers in the `.json`); the files as sent are unchanged. No summary table and no S111 script changed; the two settling scripts are new files.
- **Headline numbers**: the smallest drop in EQU from one genotype's knockout, 0.2 becomes 0.15 points. Every other number stands. Three verdicts are restated: §3's (a) is met for copying, not for speed; §4's "present in most organisms at every save" is met only in part; §5's "eliminating in every copy" becomes "in every covered copy", and the EQU residue is read as the untouched genotypes.
- **New checks that left the results where they were**: other inputs (neutral and viable shares, the low-beside-high verdicts, task shares), the evolved genomes' own essential sites, the ancestor's lethal changes by site.
- **Plain file 111** updated to match; its note says it now follows the check; a section says what the check changed; one next step.

Settled by Claude under decisions S56 and S59 and the reading rule. 29 September 2026.
