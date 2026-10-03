# S111 Avida: the three properties measured, after the cross-examination

*Log S111, decision S59. Written 29 September 2026 by the one Opus 5.5 agent of log S111 (S56), after every run had ended, and before the GLM cross-examination. The plan was committed before any measuring run (e958a0d); every number below is in one of the four summary tables in `results/S111 Avida - the runs/` and is gathered in the `.json` beside this file (by `tools/s111_summarise_the_three_properties.py`). Spread over seeds is given as the mean with the smallest and largest in brackets. Nothing in the theory's text, formal core, claims or program was touched. Obeys decision S23 in Claude's own sentences; "fitness" is Avida's word for the speed at which a program makes copies of itself.*

*After the cross-examination (29 September 2026): this is the corrected copy. GLM cross-examined the file as sent (`results/S111 Avida - the three properties measured.md`, kept unchanged); one Opus 5.5 agent that did not do the work settled its 30 objections (`results/S111 Avida - the GLM cross-examination, settled.md`: 15 stand, 14 stand in part, 1 does not) and made four new checks in the scratch space, in Avida's analysis mode only (`tools/s111x_settling_checks.py`, `tools/s111x_settling_check_ancestor_lethal.py`). Each amendment is marked with its objection id in square brackets. The one number that moved: the smallest drop in EQU from one genotype's knockout, 0.2 to 0.15 points. The new checks' numbers are in the `.json` beside this file. One objection (Xa1, its second half) is recorded for the owner, not applied.*

## 1. What was done

The owner (S59) states knowledge as information that "Can cause itself to be copied", "Can cause itself to resist change" and "Can cause itself to remain", and asked for "a type of program with these exact properties". Claude named digital organisms and proposed to run Avida and measure the three properties on its organisms; the owner: "Yup do the next step please."

- **Avida** 2.14.0 (commit 47f13dad), built in the scratch space with **no patch and no extra compiler flag** (only `AVIDA_DISABLE_BACKTRACE=1`, Avida's own fallback); build notes and the Avida rules the measures lean on, with source lines: `results/S111 Avida - the runs/build notes and Avida's rules as read from its source.md`.
- **The ancestor**: Avida's default hand-written organism, 100 instructions: a 5-instruction head (`wzcag`), 86 filler instructions that do nothing (`nop-C`), and a 9-instruction copy loop (`zvfcaxgab`).
- **Nine main worlds**: copy error rates 0.0025 (low), 0.0075 (default, Avida's own), 0.02 (high) per copied instruction; three seeds each; 50,000 updates; everything else Avida's default (60 × 60 grid, 3,600 cells; one inserted and one deleted instruction each with probability 0.05 per birth; death after executing 20 times the genome's length; the nine logic tasks rewarded). Each ran 32 to 40 minutes; all nine ended at update 50,000 with exit code 0.
- **Five control worlds** (K1 to K5) and the test-processor measures (knockouts; every one-change program of 27 evolved genotypes and the ancestor; 10,000 random programs).
- Exact commands: `results/S111 Avida - the runs/the exact commands.txt`. Summary tables, each written by one script in `tools/`: `copying and knockouts`, `the worlds over time`, `mutational robustness`, `Marletto test on the logic tasks` (`.md` and `.json`). Raw output (about 3,600 organisms' genomes at six moments per run, Avida's data files) stays in the scratch space.

## 2. COPIED

**C1. The ancestor**, run alone in Avida's test processor (no mutations, no neighbours), makes an exact copy of itself, executing 389 instructions per copy and copying all 100.

**C2. The knockout test.** Each of the 100 instructions in turn was replaced by `nop-X`, an instruction that does nothing and is no label. **15 of the 100 knockouts stop exact self-copying**: sites 1 to 6 (`h-alloc`, `h-search`, `nop-C`, `nop-A`, `mov-head`, `nop-C`) and 92 to 100 (`h-search`, `h-copy`, `if-label`, `nop-C`, `nop-A`, `h-divide`, `mov-head`, `nop-A`, `nop-B`). The other 85 leave self-copying and fitness exactly as they were (fitness ratio 1.0 in all 85). So the copying rests on the instructions that ask for room, find the ends, copy one instruction, check for the end and split, and on the labels that steer them; the filler plays no part. Site 6, the first filler instruction, is in the set: `mov-head` reads it as a label.

**C3. Copy fidelity** (share of offspring identical to the parent):

| condition | copy error rate | expected from the rates | 1,000 offspring made in the test processor: identical | of those 1,000, able to copy themselves exactly | in the worlds: births with an identical offspring |
|---|---|---|---|---|---|
| low | 0.0025 | 0.703 to 0.710 | 723 | 950 | 0.693 (0.684 to 0.704) |
| default | 0.0075 | 0.425 to 0.438 | 436 | 876 | 0.400 (0.356 to 0.445) |
| high | 0.02 | 0.120 to 0.130 | 124 | 664 | 0.131 (0.090 to 0.154) |

"Expected" is (1 − rate)^100 × 0.95 × 0.95, the lower end if every error changes the instruction, the upper if an error can redraw the same one (it can: `source/cpu/cInstSet.cc` 83-88). The world's figure is Avida's own count at the 50 sampled updates (1,000 to 50,000), over every birth of the evolved populations, whatever the parent's length (no length filter) [Xa11, Xb4]. So the columns are not one measure: "expected" and the test-processor columns are the ancestor's (100 sites, no selection), the world's is the evolved populations'. With the populations' mean lengths (about 104, 109 and 101 sites over the six saves; 105, 109 and 88 at the last), the expected share is about 0.69 to 0.70, 0.40 to 0.41 and 0.12 to 0.16; each world figure lies in that range [Xc2]. The test-processor columns were made with `nop-X` in the instruction set, so their copy errors were drawn from 27 instructions, not the world's 26; the expected share differs by less than 0.001 [Xc7].

**C4. Offspring per organism**: births per organism per update, low 0.0751 (0.0707 to 0.0815), default 0.0603 (0.0438 to 0.0749), high 0.0363 (0.0234 to 0.0429); every organism counts, including those that cannot copy. Average generation reached at update 50,000: low 7,474 (7,220 to 7,859), default 9,208 (7,735 to 10,201), high 11,521 (6,310 to 15,940). For comparison, as the plan asked [Xa8, Xc3]: the ancestor alone copies itself once per 389 instructions executed (C1); at Avida's average of 30 instructions per organism per update (`AVE_TIME_SLICE 30`), a world full of ancestors would make about 30 / 389 = 0.077 births per organism per update (arithmetic, not a run).

**C5. From one to thousands**: each world began with one injected ancestor; by update 1,000 every world held 3,566 to 3,600 organisms.

**Controls.** K1: **0 of 10,000** random programs of length 100 make an exact copy of themselves; 100 of them injected into a world made no offspring, and the last was gone after update 66 (they die of age). K2: the ancestor with `h-copy` knocked out does not copy itself; alone in a world it made no offspring and was gone after update 65.

**Shown, by the plan's lines**: the ancestor is viable; a population grows from one; the knockouts split 15 / 85, and the 15 are the copying instructions and their labels; random programs never copy. **Against**: nothing of the plan's list was found.

**Program or world.** The knockout test separates the parts: with those 15 instructions the simulated processor copies; without any one of them it copies nothing exactly. The processor carries out each step, and the world supplies the time and the cell. The fidelity is set by the world: the table's three columns follow the rate the world applies, and no instruction of the set checks or repairs a copy.

## 3. RESISTS CHANGE

Two senses, as planned: (a) **what the program does** stays the same when its instructions change; (b) **the instructions themselves** stay the same in the population.

**(a) R1, R2. One-change programs.** For the ancestor and for the most common genotype of each run at updates 10,000, 30,000 and 50,000: every program differing in exactly one instruction (25 per site), run alone in the test processor.

- The ancestor: of 2,500, 81.2% still copy themselves exactly ("viable"), 17.6% also with fitness unchanged to one part in a million ("neutral"), 75.0% viable with fitness within 1%, 18.8% no longer copy themselves.
- Fitness here is the test processor's, on the fixed inputs it supplies (built so that every combination of bits is present: `source/main/cEnvironment.cc` 1284-1288). Checked after the cross-examination [Xa6, Xc4]: the nine scans at 50,000 run again with two other input triples moved the neutral share by at most 0.009 and the viable share by at most 0.025; each most common genotype's fitness and tasks were the same under all three; the low-beside-high verdicts below are unchanged under both.
- Evolved, at update 50,000:

| condition | viable | neutral | viable, fitness within 1% (added) | length |
|---|---|---|---|---|
| low | 0.698 (0.688 to 0.714) | 0.169 (0.139 to 0.188) | 0.235 (0.198 to 0.272) | 106 (100 to 110) |
| default | 0.754 (0.719 to 0.786) | 0.214 (0.173 to 0.257) | 0.285 (0.246 to 0.336) | 107 (89 to 128) |
| high | 0.758 (0.740 to 0.779) | 0.312 (0.272 to 0.361) | 0.410 (0.311 to 0.490) | 89 (75 to 99) |

- **Low beside high**, by the plan's rule (a difference only if every seed of one lies beyond every seed of the other): the **neutral share is higher at the high rate at all three moments** (10,000, 30,000, 50,000); the viable share is higher at the high rate at 50,000 only (no clear difference at 10,000 and 30,000). Per seed at 50,000, neutral: low 0.188, 0.139, 0.181; high 0.272, 0.301, 0.361.
- So in these runs the genomes that evolved under more copy errors lose less to a single change. This is the direction the "survival of the flattest" result (Wilke and colleagues, 2001, from memory) describes; here it rests only on these runs, and they do not test its mechanism (no competition was run). The high-rate genomes are also shorter (89 against 106), a difference the comparison does not separate.
- The evolved genomes are less robust than the ancestor in the viable share (0.70 to 0.76 against 0.81): the ancestor's 86 filler instructions buffer most changes, and evolution filled them with task code.

**(b) R3, R4. Conservation.** Every living genotype aligned to the ancestor; for each ancestral site, the share of organisms still carrying the ancestor's instruction there, averaged over the 15 essential and the 85 non-essential sites. "Essential" is the knockout's (C2); in the ancestor's one-change scan, 373 of the 470 changes that stop copying fall at the 15 essential sites (373 of the 375 changes there; every change stops copying at 14 of them, all but site 3), and 97 at the other 85 sites (1 to 3 of 25 at each, 4.6% of their changes) [Xa10]. At update 50,000:

| condition | essential sites still the ancestor's | non-essential sites still the ancestor's |
|---|---|---|
| low | 0.836 (0.682 to 0.930) | 0.178 (0.150 to 0.205) |
| default | 0.682 (0.567 to 0.788) | 0.094 (0.056 to 0.123) |
| high | 0.582 (0.495 to 0.724) | 0.051 (0.034 to 0.059) |
| K5, no mutation, update 5,000 | 1.000 | 1.000 |

**Essential sites are above non-essential ones at every save of every run** (54 of 54). Checked after the cross-examination on the evolved genomes' own maps [Xc1]: in each run's most common genotype at 50,000, 13 to 22 sites stop copying when knocked out; with every organism aligned to that genotype, those sites still hold its instruction in 0.88 (low), 0.90 (default) and 0.80 (high) of cases on average (0.76 to 0.95 across runs), against 0.64, 0.56 and 0.45 (0.39 to 0.70) at its other sites: above in all nine runs. So the contrast does not rest on the ancestor's map alone. (Against the most common genotype both kinds of site read higher than against the ancestor, since its relatives are near it; the comparison is between the two kinds.) With no mutation (K5) nothing changes at all: 3,600 organisms, one genotype, the ancestor.

Yet the essential information did change: **the ancestor's exact copy loop `zvfcaxgab` was gone from every organism by update 20,000 in all six low and default runs**; in its place the most common genotypes copy two or three instructions per pass of the loop (low seed 1: `...zvvfcaxvvgab`; low seed 2: `...zvvvfcaxgab`). What it does was kept and sped up; its letters changed.

**Shown, by the plan's lines**: (a) the plan's line was "a large share of single changes leave copying and fitness unchanged": met in its copying clause (69% to 79% of single changes leave copying in place across the nine runs), not in its fitness clause (fitness unchanged to one part in a million in 14% to 36% of them, within 1% in 20% to 49%) [Xa4]; the neutral share moves with the error rate; (b) essential sites change far less than non-essential ones at the same error rate. **Against**: 21% to 31% of single changes stop copying; and the essential sites do change (by update 50,000, 16% to 42% of their places no longer hold the ancestor's instruction, by condition means; 7% to 51% across runs; and the copy loop itself was rewritten).

**Program or world.** Nothing in the program repairs anything. In (a), what buffers change is the arrangement of the program's instructions; the comparison across rates shows the world's error rate shaping that arrangement. In (b), what keeps essential sites unchanged is the world's removal: a change there often leaves an organism that cannot copy (21% to 31% of all single changes stop copying, from (a)); it makes no offspring and dies of age or is overwritten. K5 shows the other side: when the world applies no change, nothing changes.

## 4. REMAINS

- **M1. The populations remained**: at each of the 50 sampled updates from 1,000 to 50,000 (the counts were printed every 1,000 updates; between them nothing was counted), no world held fewer than 3,481 organisms [Xa9] (low 3,597 (3,597 to 3,598); default 3,577 (3,558 to 3,588); high 3,497 (3,481 to 3,518)).
- **M3. The lineage remained**: every organism descends from the one injected ancestor (one injection, no other source), over 6,310 to 15,940 generations.
- **M2. What of the ancestor remained**, at update 50,000:

| condition | identical to the ancestor | the ancestor's copy loop exactly | its head exactly | whose genotype still copies itself exactly (added) |
|---|---|---|---|---|
| low | 0 | 0 | 0.373 (0 to 0.743) | 0.857 (0.829 to 0.872) |
| default | 0 | 0 | 0 | 0.710 (0.659 to 0.768) |
| high | 0 | 0.163 (0 to 0.487) | 0 | 0.650 (0.623 to 0.686) |

Not one organism identical to the ancestor remained in any run; the exact letters of its copy loop or head remained only in some runs; the essential sites, by alignment, remained in 58% to 84% of their places (condition means; section 3); the ability to copy itself exactly remained in 65% to 86% of the organisms (condition means). At the high rate about a third of the organisms cannot copy themselves exactly: they are the world's fresh copying errors, and the population lasts through the others.

**Controls.** K1 and K2 (section 2) were gone by update 67 and 66. **K3**: the same knocked-out ancestor, alone, in a world where **nothing dies of age**, remained for the whole 2,000 updates, making nothing. **K4**: the knocked-out ancestor beside the intact one, nothing dying of age: the knocked-out one was gone by update 500 (the first save), its cell taken by the intact one's offspring; by update 1,000 the grid was full of them.

**Shown, by the plan's lines**: all nine populations lasted to update 50,000; K1 and K2 vanish in the default world. The plan's line "the essential information is present in most organisms at every save" is met only in part [Xa2]: by the plan's own measures (M2), the exact copy loop, head and whole ancestor are not in most organisms; the essential-site conservation of R3, an average over sites and not a count of organisms, is above one half at 52 of the 54 saves and below it at two (high seed 2: 0.38 at 40,000, 0.495 at 50,000); the one per-organism measure, the added share whose genotype still copies itself exactly, is 49% to 89% over all 54 saves, below one half only at update 1,000 in two high-rate runs. **Against**: the ancestor's exact genome, and in most runs the exact copy loop, did not remain; "the essential information" remains only in a sense that allows its letters to change.

**Program or world.** The world removes (old age in K1 and K2; overwriting in K4). K3 shows that when the world removes nothing, a program that cannot copy remains too [Xc6]; so, in Avida, what makes remaining depend on copying is the world's removal rule. The program's part is to be copied faster than it is removed.

## 5. Marletto's test on the logic tasks

The test, as log S110 quotes it: knowledge "is exactly the thing one would ultimately have to eliminate in order to prevent a particular transformation from being performed reliably." (Marletto, ch. 5)

**Tasks evolved in every run.** By update 50,000, NOT, NAND, ORN, OR, ANDN and NOR were performed in all nine runs, AND in nine, XOR in three and EQU (the hardest, equality of two numbers bit by bit) in **six** (Avida's world counts; first seen between updates 13,000 and 44,000). Each task performed by at least 10% of the organisms at update 50,000 was tested (69 run-task pairs).

For each task: (T1) in the most common genotype, each instruction knocked out in turn; the sites whose knockout stops the task are split into those whose knockout also stops copying and the **task-only** sites, whose knockout stops the task but leaves copying; (T2) across the most common genotypes (taken in order of abundance until they held 90% of the organisms; see section 7 on the planned cap), the share of organisms whose genotype performs the task in the test processor, as found, after knocking out the dominant genotype's task sites in that genotype only, and after knocking out **every genotype's own task-only sites in every genotype**:

| task | runs | task-only sites in the dominant | performing, as found | after the dominant only | after every genotype's task-only sites | of former performers, still copying themselves |
|---|---|---|---|---|---|---|
| NOT | 9 | 4.2 (1 to 9) | 0.718 (0.521 to 0.896) | 0.713 (0.520 to 0.887) | 0.209 (0.059 to 0.459) | 0.985 (0.932 to 1.000) |
| NAND | 9 | 5.4 (0 to 12) | 0.697 (0.365 to 0.898) | 0.692 (0.363 to 0.890) | 0.072 (0.022 to 0.125) | 0.936 (0.487 to 1.000) |
| AND | 6 | 13.8 (7 to 27) | 0.593 (0.346 to 0.882) | 0.589 (0.344 to 0.874) | 0.084 (0.009 to 0.366) | 0.984 (0.960 to 1.000) |
| ORN | 9 | 7.4 (3 to 17) | 0.701 (0.519 to 0.888) | 0.696 (0.517 to 0.880) | 0.084 (0.030 to 0.134) | 0.991 (0.964 to 1.000) |
| OR | 9 | 14.2 (6 to 21) | 0.645 (0.443 to 0.857) | 0.640 (0.441 to 0.849) | 0.028 (0.006 to 0.050) | 0.974 (0.920 to 0.999) |
| ANDN | 9 | 11.0 (6 to 29) | 0.670 (0.467 to 0.885) | 0.665 (0.465 to 0.876) | 0.091 (0.010 to 0.433) | 0.988 (0.963 to 0.999) |
| NOR | 9 | 16.2 (8 to 27) | 0.613 (0.391 to 0.845) | 0.608 (0.390 to 0.836) | 0.028 (0.006 to 0.051) | 0.972 (0.921 to 0.999) |
| XOR | 3 | 27.7 (25 to 32) | 0.591 (0.499 to 0.750) | 0.585 (0.497 to 0.736) | 0.021 (0.011 to 0.033) | 0.957 (0.932 to 0.970) |
| EQU | 6 | 22.7 (19 to 26) | 0.551 (0.299 to 0.819) | 0.546 (0.298 to 0.810) | 0.024 (0.011 to 0.044) | 0.979 (0.932 to 1.000) |

(Rows count run-task pairs where the task passed 10%; AND passed in six runs.)

- **Eliminating in one copy does not stop the transformation**: knocking out EQU's sites in the most common genotype lowers the population's share performing EQU by 0.15 to 1.4 points [Xa7, Xb2, Xc5] (the most common genotype holds 5 to 44 of about 3,600 organisms in those runs; a diverse population).
- **Eliminating in every covered copy does** [Xa5]: with every genotype's own task-only sites knocked out, EQU is performed by 1.1% to 4.4% of the covered organisms, and 93% to 100% of the former performers still copy themselves. Two residues are in the making of this column [Xa5]: the 10% of organisms beyond the covered genotypes were not touched; and a performing genotype with no task-only site (every site whose knockout stops the task also stops copying) was left as it is and counted as still performing. For EQU, XOR and NOR the whole residue is these untouched genotypes: in every covered genotype that had task-only sites, knocking them out stopped the task (for OR, all but 0.1 point). So, for EQU, the test picks out about 19 to 26 instructions per genotype (in the dominant of low seed 2, for instance, `IO`, `nand`, `swap`, `push`, `pop`, `sub` and their labels), distinct from the copying machinery, spread over thousands of copies.
- **Not fully**: the joint knockout of single-knockout sites leaves some performers, most for NOT (21% on average, up to 46%; of the 21%, about 6 points are untouched genotypes and about 15 points genotypes that still do NOT with their task-only sites knocked out [Xa5]): a task that can be done by more than one route in the same genome is not stopped by removing what single knockouts find. The test's "ultimately" then needs more than this map.
- The planned version, knocking out *all* the sites whose single knockout stops the task, drops every task to 0.000 in every run, but it also removes copying (those sites include the copy machinery, and a program that does not finish a copy registers no task in the test processor); so it does not separate the task from copying, and the task-only version was added (section 7).
- Avida's world counts give higher shares than the test processor (for EQU at high seed 1: 2,079 of 3,532 organisms, 59%, in the world; 32% in the test processor). Not checked; a likely part: a newborn carries its parent's task credit (`INHERIT_MERIT 1`) until it finishes its own first copy (Avida's task file counts the organisms that "have the particular task as a component of their merit", in its own header [Xb3]), and the test processor gives fixed inputs.
- Each genotype is tried on the test processor's fixed inputs. Checked after the cross-examination [Xa6]: with two other input triples, the share of covered organisms performing each task moved by at most 1.8 points in any run (EQU by at most 0.6), and 1.2% to 6.8% of the organisms have a genotype whose set of tasks changes with the inputs.

**Program or world.** The instructions compute the function (`IO` reads a number the world supplies and writes one back; `nand` and the others transform it). The world supplies the inputs, checks the output, and pays for it in processor time. The test finds the task in the program's instructions, and the task's reliability in the population in their copies.

## 6. What the program causes and what the simulated world does

| property | the program's instructions | the simulated world | the contrast that shows it |
|---|---|---|---|
| copied | ask for room, copy one instruction at a time, find the end, split (15 essential sites) | carries out each step; hands out processor time by merit; puts the offspring in a cell; makes the copy errors (fidelity 0.69, 0.40, 0.13 at the three rates) | knockouts (15 stop it, 85 do not); K1, K2 |
| resists change (a), what it does | the arrangement of instructions decides which changes are harmless | chose that arrangement by which variants lasted: more neutral changes at the high rate | one-change programs; low beside high |
| resists change (b), its instructions | its essential sites are those whose change stops copying | removes the organisms that cannot copy (age, overwriting); makes every change in the first place | essential above non-essential at 54 of 54 saves; on the evolved genotypes' own maps too, 9 of 9 runs [Xc1]; K5 (no change without the world's errors) |
| remains | is copied faster than it is removed | removes by age and by overwriting | K1, K2 gone; K3 remains when nothing dies of age; K4 overwritten |
| a task (Marletto's test) | computes the function (19 to 26 instructions for EQU) | supplies inputs, checks, rewards | one genotype's knockout: 0.15 to 1.4 points less [Xb2]; every covered genotype's: to 1% to 4%, all of it genotypes left untouched [Xa5] |

No instruction of Avida's default set checks a copied instruction against its original or puts one back (`if-label` compares, only to find the end; build notes). So every "resisting" found here is either the program's structure, shaped by the world's weeding, or the world's weeding itself.

## 7. Departures from the plan, failures, and what was not measured

**Departures and additions** (each marked in its script's note):
1. The plan described the ancestor as a 5-instruction head, 85 filler and a 10-instruction copy loop; it is 5, 86 and 9 (100 in all). The knockout test then found 15 essential sites, one of them the first filler instruction (site 6).
2. Robustness: the plan's "neutral" (fitness within one part in a million) counts a one-cycle change in copying time as a change; for the ancestor, 57% of one-change programs copy one cycle faster (388 instead of 389 instructions). A second share, **viable with fitness within 1%**, was added. Both are reported; the plan's rule gives "high above low" for both.
3. Remains: the share of organisms **whose genotype still copies itself exactly** (every living genotype run in the test processor) was added, because the planned exact-letter measures (copy loop, head, whole ancestor) came to 0 in most runs while the populations lasted.
4. Marletto's test: (a) the planned cap of 300 genotypes covered only 15% to 57% of the organisms, not the planned 90%; every measure was also run **without the cap** (90% covered), and the table above uses that; the capped numbers are in the summary table. (b) The **task-only** sites were added, because the planned joint knockout also removes copying (section 5).
5. Controls: the first attempt of K2, K3 and K4 failed at once ("Unknown instruction 'nop-X'": the added line ran onto the last line of the instruction file, which has no final newline), and K1 ran without `nop-X` defined; nothing from that attempt is used. Fixed in the scripts, and all five controls rerun. The controls then printed their counts every update instead of every 100.
6. K1 and K2 stop before 2,000 updates: Avida ends a run when no organism is left (last organisms at update 66 and 65).
7. K4's first count took any genome holding `nop-X` for the knocked-out organism; in that world copy errors can write `nop-X` into the intact ancestor's offspring, so the count ran into the thousands. Corrected to count only the exact knocked-out genome, which was gone by update 500.
8. The control worlds K1 to K4 and every test-processor run use the instruction set with `nop-X` added as a 27th instruction; the nine main worlds and K5 do not. So the 1,000 offspring of C3 had their copy errors drawn from 27 instructions, not 26; the expected share differs by less than 0.001 [Xc7].
9. `numpy` was installed with `pip` for the alignment; `tools/s111_summarise_the_three_properties.py` was added to gather the numbers.
10. The analysis scripts were run on the low runs while the other runs were going (to test them); the reported numbers are from the final run of every script after all runs ended.
11. A snapshot commit (566eb03), made while this agent worked, holds early copies of this file, the plain file, the reading rule and the GLM build; nothing was sent then.
12. C4's comparison with the ancestor alone, in the plan, was left out of the file as sent; given now by arithmetic from C1 (section 2) [Xa8, Xc3].
13. The data files' columns the scripts read, checked against the header lines Avida wrote into them [Xb3]: `count.dat` column 3 the organisms, 9 the births in the update, 11 "number of breed true"; `time.dat` column 3 the average generation; `tasks.dat` columns 2 to 10 the nine tasks, in the scripts' order.

**Not measured**: insertion and deletion mutants in the robustness scan (point changes only); competition between evolved genotypes (the design of Wilke and colleagues); the line of descent step by step; what knocking out two or more task sites at once does beyond the joint knockout; longer runs, other environments, other instruction sets; why Avida's world task counts exceed the test processor's (section 5). The world's own fidelity is Avida's count at 50 sampled updates, not every birth.

**Unsure**: the alignment of repetitive stretches (the ancestor's filler) to evolved genomes is not unique, so per-site conservation of the non-essential sites is rough; the rewritten copy loops (`zvvfcaxvvgab` against `zvfcaxgab`) likewise align in more than one way, so the essential-site shares carry some of the same roughness (not measured; the check on the evolved genotypes' own maps, section 3, aligns to a different genome and gives the same contrast) [Xa12]; three seeds per condition is few; the high-rate genomes are shorter, which the robustness comparison does not separate from the error rate.

## 8. What these organisms have and do not have, beside the explanation kind

Observations only; they settle nothing (S28).

**They have**, in the senses measured:
- A sequence that, run by the world's processor, brings about its own copying: 15 of its instructions are needed for it, and random sequences of the same length never copy.
- Structure that keeps what it does through most single changes (69% to 79% still copy themselves), and loses less to them when the world makes more errors; an arrangement the world's weeding shaped, not anything the instructions do to a change [Xa1].
- Parts that stay the same while the rest changes (essential sites above non-essential at every save), because the world removes the copies whose change stopped the copying.
- A line that lasted 50,000 updates and thousands of generations, although not one organism identical to the first remained and its copy loop was rewritten.
- Instructions that compute a logic function the world rewards; by Marletto's test, eliminating them in one genotype leaves the transformation performed almost as before (0.15 to 1.4 points less for EQU) [Xb2], and eliminating them in every covered genotype that has them stops it in every one; the 1% to 4% of organisms still performing EQU are genotypes left untouched [Xa5].

**They do not have**:
- **No problem.** Nothing in an organism states or holds a problem; the tasks are set, checked and paid for by the world, and an organism does a task or does not.
- **No criticism.** No organism compares variants or finds a flaw in one; variants are removed by the world's rules (age, overwriting, less processor time), not by anything in the organisms.
- **Nothing standing for something outside them.** The EQU code turns two numbers into a third; nothing in the genome refers to the numbers' source, to the reward or to the world. That the code is there *because* the world rewards EQU is a fact about the population's history, not about anything the genome says.
- **No correction of their own errors.** No instruction repairs a copy; every "resisting change" found is structure or the world's weeding (section 6).

Beside the owner's three properties: in each, the organism's instructions are a necessary part (the knockouts; K1, K2 against the ancestor), and the world's rules are the other part (the errors, the removal, the rewards; K3 shows remaining without copying once the world stops removing). Whether "cause itself" asks for more than this is the owner's to say.
