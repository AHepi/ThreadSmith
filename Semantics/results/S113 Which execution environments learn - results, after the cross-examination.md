# S113 Which execution environments learn: results, after the cross-examination

*Corrected copy, 30 September 2026, after the GLM cross-examination was settled (`results/S113 Which execution environments learn - the GLM cross-examination, settled.md`). Written by the one Opus 5.5 agent that settled it (S56, S68), not by the agent that wrote the results. The results as sent (`S113 Which execution environments learn - results.md` and `.json`, e57ddbb) are kept unchanged beside this file. Every change is marked with the objection it answers, in brackets, e.g. **[Xa1]**; unmarked text is as sent. The numbers: `S113 Which execution environments learn - results, after the cross-examination.json`, written by `tools/s113_count_new_capabilities_over_time_after_the_cross_examination.py` (a corrected copy, [Xb6]; its block "after the cross-examination" holds every number the settlement added); the tables are printed from it by the unchanged `tools/s113_print_the_results_tables.py`. **No headline number and no verdict E1 to E8 changed; the statement that every environment's count levelled off did [Xa1].** The note below is the note as sent.*


*Log S113, decisions S62, S63 and S64. Written 30 September 2026 by the one Opus 5.5 agent of log S113 (S56), after the runs, **before the GLM cross-examination**, against the plan written and committed before any measuring run: `results/S113 Which execution environments learn - how it will be tested, written before running.md` (d61006a). In the owner's Avida terms (S61, `records/Semantics - Avida terms, given by the owner.md`): an **Avida program** is one program of a **program population**; a **distinct instruction sequence** is what Avida calls a genotype; a **computational capability** is one of Avida's 77 logic tasks, and a program has it when Avida credits it with **task performance**; **present** means performed by at least one program, **common** by at least 10% of the program population; the **Avida execution environment** is what is rewarded, by how much, and from what resource. All entities are digital programs executing on Avida's virtual CPU; nothing biological is involved. The numbers: `S113 Which execution environments learn - results.json` beside this file, written by `tools/s113_count_new_capabilities_over_time.py`; every table below is copied from it by `tools/s113_print_the_results_tables.py`. The exact commands, with every departure: `results/S113 Which execution environments learn - the runs/the exact commands.txt`. Raw output (345 MB) stays in the scratch space. Observations only; nothing is settled (S28).*

---

## 0. In short

Six Avida execution environments, three seeds each, 50,000 updates each, every run starting from the same Avida program (Avida's default ancestor, which performs no task), with the same instruction set, world, instruction-change rates and replication rules. Only the environment differed. Counted: how many of the 77 logic tasks were present and common in the program population over time.

| environment | common at update 50,000 (seeds 1 / 2 / 3) | present at 50,000 | when the common count stopped rising |
|---|---|---|---|
| **GROWING LIST** (starts with NOT and NAND; adds the next harder level once a task of the top level is common) | **65 / 48 / 55** | **74 / 67 / 72** | most by update 10,000 to 25,000; last new high 37,000 / 42,500 / 31,500 |
| **FIXED LARGE LIST** (all 77 rewarded from the start) | 32 / 41 / 0 (Avida's count; 13 in seed 3 by the test processor, section 2) | 54 / 67 / 32 | 33,000 / 48,250 / 28,000 |
| **COMMON TASKS PAY LESS** (the nine two-input tasks, each paid from a resource that runs down) | 17 / 9 / 8 | 45 / 29 / 26 | 15,750 / 31,750 / 33,000 |
| **FIXED LIST, GRADED** (the nine two-input tasks, S111's rewards) | 7 / 8 / 8 | 20 / 30 / 19 | 17,500 / 43,250 / 21,000 |
| **ONE HARD TASK ONLY** (EQU only) | 0 / 0 / 0 | 3 / 2 / 0 | never rose |
| **NO TASK REWARDS** (control) | 0 / 0 / 0 | 3 / 2 / 0 | never rose |

- **The growing list ended with the most new capabilities in every seed**, more than the fixed large list with the same 77 tasks all rewarded from the start (every seed of the one above every seed of the other: the plan's "more"). Claude had expected the two not to be separated; that expectation is contradicted. By "present" alone they are not separated (67 against 67 in seed 2).
- **With EQU alone rewarded, no program ever performed EQU** in any seed, and so the three runs are, number for number, the same runs as NO TASK REWARDS with the same seeds: the reward never acted. With the easier tasks also rewarded, EQU became common in all three seeds (at 17,500, 5,250 and 21,000).
- **[Xa1, Xb1, Xc1] The count of common capabilities slowed to nearly nothing in all but one paying run, but did not level off everywhere by the plan's rule.** In 11 of the 12 runs that paid for tasks, the count at 50,000 was at most one above its count at 40,000. By the plan's M4 (no new high after 40,000), 3 of the 12 made a new high later: by Avida's count FIXED GRADED seed 2 (43,250), GROWING LIST seed 2 (42,500) and FIXED LARGE LIST seed 2 (48,250); by the test processor FIXED GRADED seeds 1 and 3 (50,000 and 45,000, each by one task) and FIXED LARGE LIST seed 2 (50,000). **FIXED LARGE LIST seed 2 was still rising at the end** (28 common at 40,000, 37 at 45,000, 41 at 50,000). Whether longer runs would have kept rising was not tested. The six runs that never had a common task never rose at all [Xb6].
- **Capabilities once common were mostly kept** to update 50,000: **[Xc2]** by Avida's count 73% to 100% per paying run, except FIXED LARGE LIST seed 3 (0%, the counting fault of section 2); by the test processor 62% (that same run, 13 of 21) to 100%. None of the environments lost capabilities wholesale except by the counting fault.
- **New task circuits share required instructions with earlier ones** more than chance would give, in all 12 runs where it could be measured. **[Xb7]** Each run's measure is of one distinct instruction sequence, the most common, which in some runs is carried by a handful of programs (4 to 776).

## 1. What was run

As planned (plan sections 3 and 4): 6 environments x seeds 1, 2, 3 = 18 runs, each 50 pieces of 1,000 updates, every piece a new Avida process that loads the program population the last piece saved. **900 of 900 pieces exited 0**; the runner ran from 08:26 to 16:10 UTC (7 h 43 min, three runs at once). All 77 tasks were listed in every environment, unrewarded ones at value 0. Runs with the same seed number used the same Avida seeds piece by piece in every environment.

The growing list's steps (a level is rewarded from the update given; `growing list steps` in the `.json`):

- growing seed 1: levels 2 to 9 added at updates 2,000 to 9,000, one per piece; level 10 (the one task 3AB) never added.
- growing seed 2: levels 2 to 5 at 2,000 to 5,000; level 6 at 9,000 (no level-5 task was common before), 7 at 10,000, 8 at 11,000; levels 9 and 10 never added (73 of 77 tasks rewarded at the end).
- growing seed 3: levels 2 to 10 at 2,000 to 10,000: all 77 rewarded from update 10,000.

**[Xa3, Xb4]** The rule reads Avida's world count at the piece end, the count that section 2 shows can be too low after a load. Checked: at all 30 saved updates of the three growing runs, the test processor and the world count agree exactly on which tasks of the top rewarded level were common. The one delay, seed 2's level 6 (rewarded from 9,000, not 6,000), fell in pieces where the count 250 updates after the load was 0.99 to 1.03 of the previous piece's end. Those pieces had 98 to 219 births per update among about 3,590 programs, so the records were full long before the piece end. The growing pieces with a count under half after a load (11,000 and 21,000 in seed 1; 17,000, 21,000 and 23,000 in seed 2) all came after the last addition in their run. So the counting fault delayed no addition that can be checked. Between saved updates after the last additions, the test processor cannot be read (those populations were not kept).

So in all three seeds the growing list reached 73 to 77 rewarded tasks by update 11,000, and from then on differed from the fixed large list only in its history and in the few top-level tasks never added.

## 2. Two readings of "present" and "common", and a counting fault found after the runs

**The plan's reading** is Avida's own count in the world (`tasks.dat`): how many programs have the task in the record of their last completed copy. **A fault in it, found after the runs** (a departure, recorded in the exact commands, step 7): a program loaded at the start of a piece has an empty record until it completes a copy of its own (a newborn copies its parent's record, `cPhenotype.cc` 447; a loaded program starts empty). Where processor time is very uneven, many programs complete no copy within a piece and are counted as performing nothing. In FIXED LARGE LIST seed 3, from update 32,000 on, Avida's count showed **no common task at 10 of the 19 piece ends** (32,000, 35,000, 36,000, 42,000, 43,000, 45,000, 46,000, 47,000, 49,000, 50,000), with about 44 births per update against 3,591 programs (`count.dat` of pieces 33 to 35), while the average merit stayed between 4.7 x 10^20 and 1.4 x 10^21 (`average.dat`, updates 33,000 to 50,000; raw output, not in the `.json`). The S114 check of GPT 6 Astra's reply found the same mechanism independently (claim 3 of reply 06 in `results/S115 Checking the Astra returns/`); the S114 restart audit measured the pieces against unbroken runs for FIXED GRADED and COMMON TASKS PAY LESS only (`results/S114 Restart audit - results.md`).

**A second reading, added after the runs**, does not depend on the pieces: every distinct instruction sequence of the program populations saved every 5,000 updates, run alone in Avida's test processor (the 77 tasks listed at value 0, as in S111 and S112), a task counted as performed by all the programs carrying a sequence that performs it there (`tools/s113_measure_capabilities_in_the_saved_program_populations.py`; 180 saved program populations). The two readings side by side, common tasks:

- they agree exactly at all ten saved updates in FIXED GRADED, ONE HARD TASK ONLY and NO TASK REWARDS (all seeds) and COMMON TASKS PAY LESS seed 2;
- elsewhere they differ by 1 to 6 tasks (growing seed 2 at 25,000: 44 by Avida's count, 50 by the test processor), except **FIXED LARGE LIST seed 3 at 35,000, 45,000 and 50,000: 0 by Avida's count, 13 by the test processor** (present: 18, 32, 32 against 48, 50, 51).

**[Xa8] What a reload keeps and loses** (from Avida's source; `results/S114 Checking GPT 6 Astra's reply.md`, claims 1 to 7 and the findings after them; the last item read again here). A reload keeps each program's cell, lineage label and the processor cycles used in its current copy. It gives the program the merit averaged over its distinct instruction sequence, scaled for the rest of the copy. It resets:
- the processor state (every program starts its instruction sequence from the top);
- the record of tasks performed;
- the generation count (`cPhenotype.cc` 701);
- the executed-instruction count and age (`cPhenotype.cc` 702 to 705). So every loaded program gets a fresh life of 20 × its length in executed instructions (`DEATH_METHOD 2`, `AGE_LIMIT 20`).

It is the same in every environment. The S114 restart audit found births and copy times after a reload equal to those of the unbroken run in FIXED GRADED and COMMON TASKS PAY LESS. **Generation counts in S113's data files are not to be used**: a reload resets them. None is used here.

**[Xb3, Xc4]** A check of the load undercount: performances counted 250 updates after a load, against the previous piece's end. This is a departure (section 10, item 8): the plan said "within pieces". The middle ratio and the pieces under one half:

| environment | pieces | middle ratio | smallest | pieces under 0.5 |
|---|---|---|---|---|
| FIXED LIST, GRADED | 146 | 1.003 | 0.969 | 0 |
| ONE HARD TASK ONLY | 105 | 1.0 | 0.0 | 24 |
| NO TASK REWARDS | 105 | 1.0 | 0.0 | 24 |
| GROWING LIST | 146 | 0.92 | 0.305 | 5 |
| COMMON TASKS PAY LESS | 146 | 0.993 | 0.843 | 0 |
| FIXED LARGE LIST | 146 | 0.898 | 0.085 | 18 |

(In ONE HARD TASK ONLY and NO TASK REWARDS the counts are a few programs, so single programs move the ratio.) **[Xb3]** The check as the plan worded it (update 250 against the same piece's update 1,000) gives middle ratios of 0.998 (FIXED GRADED), 0.983 (COMMON TASKS PAY LESS), 0.883 (GROWING LIST) and 0.845 (FIXED LARGE LIST). It mixes the load with growth inside the piece: FIXED GRADED has 4 pieces under one half, all early, while tasks were still appearing. The numbers are in the corrected `.json`. Below, both readings are given where they differ; the comparisons of section 8 are made on both.

## 3. The number of capabilities over time

Avida's count, common (at least 10% of the programs), seeds 1 / 2 / 3:

| environment | 5k | 10k | 15k | 20k | 25k | 30k | 35k | 40k | 45k | 50k |
|---|---|---|---|---|---|---|---|---|---|---|
| FIXED LIST, GRADED | 5 / 6 / 5 | 6 / 7 / 7 | 6 / 7 / 7 | 6 / 7 / 7 | 6 / 7 / 7 | 6 / 7 / 7 | 6 / 7 / 7 | 6 / 8 / 7 | 6 / 8 / 8 | 7 / 8 / 8 |
| ONE HARD TASK ONLY | 0 / 0 / 0 | 0 / 0 / 0 | 0 / 0 / 0 | 0 / 0 / 0 | 0 / 0 / 0 | 0 / 0 / 0 | 0 / 0 / 0 | 0 / 0 / 0 | 0 / 0 / 0 | 0 / 0 / 0 |
| NO TASK REWARDS | 0 / 0 / 0 | 0 / 0 / 0 | 0 / 0 / 0 | 0 / 0 / 0 | 0 / 0 / 0 | 0 / 0 / 0 | 0 / 0 / 0 | 0 / 0 / 0 | 0 / 0 / 0 | 0 / 0 / 0 |
| GROWING LIST | 7 / 9 / 9 | 43 / 24 / 58 | 53 / 29 / 52 | 53 / 35 / 54 | 62 / 44 / 54 | 64 / 45 / 54 | 65 / 45 / 55 | 65 / 47 / 55 | 65 / 48 / 55 | 65 / 48 / 55 |
| COMMON TASKS PAY LESS | 7 / 6 / 5 | 14 / 7 / 7 | 15 / 7 / 7 | 16 / 7 / 7 | 16 / 7 / 8 | 16 / 7 / 9 | 16 / 9 / 9 | 16 / 9 / 8 | 17 / 9 / 8 | 17 / 9 / 8 |
| FIXED LARGE LIST | 10 / 8 / 16 | 23 / 22 / 14 | 24 / 28 / 13 | 24 / 26 / 14 | 28 / 26 / 16 | 29 / 27 / 13 | 32 / 27 / 0 | 31 / 28 / 14 | 32 / 37 / 0 | 32 / 41 / 0 |

Avida's count, present (at least one program):

| environment | 5k | 10k | 15k | 20k | 25k | 30k | 35k | 40k | 45k | 50k |
|---|---|---|---|---|---|---|---|---|---|---|
| FIXED LIST, GRADED | 20 / 18 / 14 | 23 / 28 / 22 | 21 / 19 / 18 | 19 / 25 / 25 | 19 / 23 / 21 | 19 / 27 / 18 | 18 / 24 / 17 | 17 / 29 / 19 | 18 / 29 / 24 | 20 / 30 / 19 |
| ONE HARD TASK ONLY | 1 / 1 / 2 | 2 / 2 / 0 | 1 / 2 / 0 | 1 / 1 / 0 | 1 / 1 / 0 | 1 / 3 / 0 | 2 / 3 / 0 | 2 / 2 / 0 | 2 / 2 / 0 | 3 / 2 / 0 |
| NO TASK REWARDS | 1 / 1 / 2 | 2 / 2 / 0 | 1 / 2 / 0 | 1 / 1 / 0 | 1 / 1 / 0 | 1 / 3 / 0 | 2 / 3 / 0 | 2 / 2 / 0 | 2 / 2 / 0 | 3 / 2 / 0 |
| GROWING LIST | 14 / 20 / 13 | 68 / 51 / 68 | 72 / 57 / 70 | 71 / 58 / 71 | 73 / 66 / 71 | 74 / 64 / 71 | 74 / 60 / 71 | 74 / 62 / 72 | 73 / 63 / 71 | 74 / 67 / 72 |
| COMMON TASKS PAY LESS | 21 / 17 / 12 | 39 / 20 / 17 | 40 / 18 / 20 | 45 / 14 / 15 | 50 / 18 / 18 | 45 / 15 / 25 | 44 / 22 / 29 | 44 / 29 / 25 | 45 / 31 / 22 | 45 / 29 / 26 |
| FIXED LARGE LIST | 28 / 38 / 34 | 39 / 45 / 33 | 42 / 54 / 32 | 46 / 53 / 33 | 51 / 50 / 36 | 47 / 61 / 49 | 53 / 55 / 18 | 52 / 59 / 50 | 53 / 65 / 32 | 54 / 67 / 32 |

The test processor's reading, common:

| environment | 5k | 10k | 15k | 20k | 25k | 30k | 35k | 40k | 45k | 50k |
|---|---|---|---|---|---|---|---|---|---|---|
| FIXED LIST, GRADED | 5 / 6 / 5 | 6 / 7 / 7 | 6 / 7 / 7 | 6 / 7 / 7 | 6 / 7 / 7 | 6 / 7 / 7 | 6 / 7 / 7 | 6 / 8 / 7 | 6 / 8 / 8 | 7 / 8 / 8 |
| ONE HARD TASK ONLY | 0 / 0 / 0 | 0 / 0 / 0 | 0 / 0 / 0 | 0 / 0 / 0 | 0 / 0 / 0 | 0 / 0 / 0 | 0 / 0 / 0 | 0 / 0 / 0 | 0 / 0 / 0 | 0 / 0 / 0 |
| NO TASK REWARDS | 0 / 0 / 0 | 0 / 0 / 0 | 0 / 0 / 0 | 0 / 0 / 0 | 0 / 0 / 0 | 0 / 0 / 0 | 0 / 0 / 0 | 0 / 0 / 0 | 0 / 0 / 0 | 0 / 0 / 0 |
| GROWING LIST | 7 / 9 / 9 | 43 / 24 / 56 | 54 / 29 / 52 | 54 / 34 / 54 | 65 / 50 / 54 | 65 / 44 / 54 | 65 / 49 / 55 | 65 / 45 / 55 | 65 / 46 / 55 | 65 / 46 / 55 |
| COMMON TASKS PAY LESS | 7 / 6 / 5 | 13 / 7 / 7 | 14 / 7 / 7 | 16 / 7 / 7 | 16 / 7 / 8 | 16 / 7 / 9 | 16 / 9 / 8 | 16 / 9 / 8 | 16 / 9 / 8 | 16 / 9 / 8 |
| FIXED LARGE LIST | 10 / 8 / 15 | 23 / 21 / 13 | 24 / 28 / 12 | 24 / 26 / 12 | 28 / 26 / 13 | 29 / 27 / 13 | 32 / 27 / 13 | 31 / 28 / 14 | 31 / 37 / 13 | 32 / 41 / 13 |

The test processor's reading, present:

| environment | 5k | 10k | 15k | 20k | 25k | 30k | 35k | 40k | 45k | 50k |
|---|---|---|---|---|---|---|---|---|---|---|
| FIXED LIST, GRADED | 21 / 21 / 14 | 19 / 29 / 23 | 18 / 22 / 19 | 22 / 25 / 18 | 19 / 22 / 20 | 19 / 29 / 16 | 18 / 26 / 20 | 18 / 28 / 18 | 20 / 36 / 24 | 22 / 31 / 23 |
| ONE HARD TASK ONLY | 2 / 1 / 2 | 3 / 2 / 0 | 1 / 2 / 0 | 1 / 2 / 0 | 2 / 1 / 0 | 1 / 2 / 0 | 2 / 2 / 0 | 3 / 2 / 0 | 1 / 2 / 0 | 3 / 2 / 0 |
| NO TASK REWARDS | 2 / 1 / 2 | 3 / 2 / 0 | 1 / 2 / 0 | 1 / 2 / 0 | 2 / 1 / 0 | 1 / 2 / 0 | 2 / 2 / 0 | 3 / 2 / 0 | 1 / 2 / 0 | 3 / 2 / 0 |
| GROWING LIST | 14 / 19 / 13 | 69 / 49 / 69 | 72 / 56 / 71 | 72 / 60 / 74 | 73 / 62 / 71 | 75 / 62 / 72 | 75 / 61 / 70 | 74 / 62 / 73 | 73 / 62 / 71 | 74 / 65 / 72 |
| COMMON TASKS PAY LESS | 19 / 18 / 8 | 37 / 17 / 15 | 40 / 19 / 18 | 44 / 18 / 15 | 44 / 15 / 19 | 44 / 16 / 24 | 45 / 25 / 21 | 42 / 25 / 25 | 47 / 29 / 22 | 42 / 27 / 23 |
| FIXED LARGE LIST | 28 / 39 / 36 | 41 / 43 / 34 | 44 / 55 / 33 | 48 / 50 / 33 | 53 / 56 / 34 | 49 / 61 / 53 | 54 / 55 / 48 | 53 / 59 / 51 | 52 / 64 / 50 | 54 / 67 / 51 |

## 4. At update 50,000, and levelling off

Avida's count ("levelled off": the last new high of the common count at or before 40,000, plan M4; the rise is over 40,000 to 50,000):

| environment | common (1/2/3) | two-input common | three-input common | present (1/2/3) | two-input present | three-input present | last new high of common | levelled off | rise of common over last 10,000 |
|---|---|---|---|---|---|---|---|---|---|
| FIXED LIST, GRADED | 7 / 8 / 8 | 7 / 8 / 8 | 0 / 0 / 0 | 20 / 30 / 19 | 8 / 9 / 9 | 12 / 21 / 10 | 17500 / 43250 / 21000 | yes / no / yes | 1 / 0 / 1 |
| ONE HARD TASK ONLY | 0 / 0 / 0 | 0 / 0 / 0 | 0 / 0 / 0 | 3 / 2 / 0 | 3 / 2 / 0 | 0 / 0 / 0 | - / - / - | - / - / - | 0 / 0 / 0 |
| NO TASK REWARDS | 0 / 0 / 0 | 0 / 0 / 0 | 0 / 0 / 0 | 3 / 2 / 0 | 3 / 2 / 0 | 0 / 0 / 0 | - / - / - | - / - / - | 0 / 0 / 0 |
| GROWING LIST | 65 / 48 / 55 | 9 / 8 / 7 | 56 / 40 / 48 | 74 / 67 / 72 | 9 / 9 / 9 | 65 / 58 / 63 | 37000 / 42500 / 31500 | yes / no / yes | 0 / 1 / 0 |
| COMMON TASKS PAY LESS | 17 / 9 / 8 | 9 / 9 / 8 | 8 / 0 / 0 | 45 / 29 / 26 | 9 / 9 / 9 | 36 / 20 / 17 | 15750 / 31750 / 33000 | yes / yes / yes | 1 / 0 / 0 |
| FIXED LARGE LIST | 32 / 41 / 0 | 8 / 7 / 0 | 24 / 34 / 0 | 54 / 67 / 32 | 8 / 9 / 6 | 46 / 58 / 26 | 33000 / 48250 / 28000 | yes / no / yes | 1 / 13 / -14 |

The test processor's reading (at 5,000-update steps, so the last new high is a saved update; "common and replicating" counts only programs whose sequence also makes an exact copy of itself in the test processor):

| environment | common at 50,000 | two-input | three-input | present at 50,000 | common and replicating | last new high | levelled off | ever common | kept common |
|---|---|---|---|---|---|---|---|---|---|
| FIXED LIST, GRADED | 7 / 8 / 8 | 7 / 8 / 8 | 0 / 0 / 0 | 22 / 31 / 23 | 7 / 8 / 8 | 50000 / 40000 / 45000 | no / yes / no | 8 / 9 / 8 | 7 / 8 / 8 |
| ONE HARD TASK ONLY | 0 / 0 / 0 | 0 / 0 / 0 | 0 / 0 / 0 | 3 / 2 / 0 | 0 / 0 / 0 | - / - / - | - / - / - | 0 / 0 / 0 | 0 / 0 / 0 |
| NO TASK REWARDS | 0 / 0 / 0 | 0 / 0 / 0 | 0 / 0 / 0 | 3 / 2 / 0 | 0 / 0 / 0 | - / - / - | - / - / - | 0 / 0 / 0 | 0 / 0 / 0 |
| GROWING LIST | 65 / 46 / 55 | 9 / 7 / 7 | 56 / 39 / 48 | 74 / 65 / 72 | 65 / 46 / 55 | 25000 / 25000 / 10000 | yes / yes / yes | 68 / 54 / 61 | 65 / 46 / 55 |
| COMMON TASKS PAY LESS | 16 / 9 / 8 | 9 / 9 / 8 | 7 / 0 / 0 | 42 / 27 / 23 | 16 / 9 / 8 | 20000 / 35000 / 30000 | yes / yes / yes | 17 / 9 / 10 | 16 / 9 / 8 |
| FIXED LARGE LIST | 32 / 41 / 13 | 8 / 7 / 3 | 24 / 34 / 10 | 54 / 67 / 51 | 32 / 41 / 13 | 35000 / 50000 / 5000 | yes / no / yes | 34 / 45 / 21 | 32 / 41 / 13 |

- **GROWING LIST**: two-input tasks common 9 / 8 / 7 of 9, three-input 56 / 40 / 48 of 68 (Avida's count). The count rose fastest between 5,000 and 10,000 (7 / 9 / 9 to 43 / 24 / 58) and then slowly; after 25,000 it rose by at most 4 in any seed (Avida's count).
- **FIXED LARGE LIST**: two-input tasks common 8 / 7 / 0 (3 in seed 3 by the test processor), three-input 24 / 34 / 0 (10). Seed 2 was still rising (37 at 45,000, 41 at 50,000).
- **COMMON TASKS PAY LESS**: all nine two-input tasks present by some program in every seed at 50,000; three-input tasks common only in seed 1 (8).
- **FIXED GRADED**: no three-input task common in any seed, though 10 to 21 were present by some program at 50,000, never rewarded.
- **[Xb6]** In both tables, "-" in the last-new-high and levelled-off columns means the count of common tasks never rose above 0. As sent, these runs were given the first sample (250, or 5,000) and "levelled off: yes". FIXED LARGE LIST seed 3's "levelled off: yes" by Avida's count (last new high 28,000) is shaped by the counting fault; by the test processor its last new high is 5,000.
- The levelling-off verdict moves with the reading for FIXED GRADED (Avida's count: levelled in seeds 1 and 3; the test processor: a new high at 50,000 and 45,000 in seeds 1 and 3, each by one task crossing the 10% share) and for GROWING LIST seed 2 (42,500 by Avida's count; 25,000 by the test processor).

## 5. First appearances

First update at which each two-input task was common (Avida's count; "-" never):

| environment | NOT | NAND | AND | ORN | OR | ANDN | NOR | XOR | EQU |
|---|---|---|---|---|---|---|---|---|---|
| FIXED LIST, GRADED | 1500 / 1250 / 3000 | 2500 / 1750 / 2750 | 9250 / 2500 / 7750 | 1750 / 1500 / 1750 | 1750 / 2500 / 3750 | 46750 / 2750 / 6750 | 2250 / 4250 / 3750 | - / 43250 / - | 17500 / 5250 / 21000 |
| ONE HARD TASK ONLY | - / - / - | - / - / - | - / - / - | - / - / - | - / - / - | - / - / - | - / - / - | - / - / - | - / - / - |
| NO TASK REWARDS | - / - / - | - / - / - | - / - / - | - / - / - | - / - / - | - / - / - | - / - / - | - / - / - | - / - / - |
| GROWING LIST | 1500 / 1250 / 2000 | 1500 / 1500 / 2500 | 5500 / 13500 / 9750 | 2250 / 2250 / 2250 | 3250 / 3250 / 4750 | 5250 / 4000 / 8000 | 5500 / 10250 / 8500 | 6250 / - / - | 21000 / 17000 / 9750 |
| COMMON TASKS PAY LESS | 1500 / 1250 / 7250 | 1750 / 1750 / 2250 | 3250 / 6500 / 6250 | 1750 / 1500 / 1750 | 1750 / 2000 / 3250 | 2000 / 3000 / 4500 | 1750 / 3250 / 2500 | 15500 / 31250 / 29250 | 8750 / 31750 / 29500 |
| FIXED LARGE LIST | 1500 / 1250 / 4250 | 1750 / 1500 / 3000 | 8250 / 2500 / 4000 | 1750 / 1750 / 1750 | 2500 / 2750 / 3000 | 8000 / 6750 / 3000 | 3000 / 6750 / - | - / - / - | 8500 / - / - |

First update at which each two-input task was performed by any program:

| environment | NOT | NAND | AND | ORN | OR | ANDN | NOR | XOR | EQU |
|---|---|---|---|---|---|---|---|---|---|
| FIXED LIST, GRADED | 750 / 750 / 1500 | 1250 / 750 / 1250 | 1500 / 2250 / 2750 | 1500 / 1250 / 1500 | 1500 / 1750 / 3500 | 2000 / 2500 / 3000 | 2000 / 2750 / 3000 | 18000 / 5250 / 20000 | 10000 / 5250 / 20750 |
| ONE HARD TASK ONLY | 750 / 750 / 750 | 2000 / 1500 / 750 | 21500 / 7750 / - | 1750 / 1750 / 2500 | 15250 / 45250 / - | 6000 / 5250 / 6750 | - / - / - | - / - / - | - / - / - |
| NO TASK REWARDS | 750 / 750 / 750 | 2000 / 1500 / 750 | 21500 / 7750 / - | 1750 / 1750 / 2500 | 15250 / 45250 / - | 6000 / 5250 / 6750 | - / - / - | - / - / - | - / - / - |
| GROWING LIST | 750 / 750 / 1500 | 1250 / 750 / 1250 | 2750 / 2750 / 3250 | 1250 / 1250 / 1500 | 2250 / 2500 / 2250 | 3250 / 2750 / 5750 | 4500 / 2750 / 5500 | 5250 / 9250 / 6250 | 5250 / 8250 / 6000 |
| COMMON TASKS PAY LESS | 750 / 750 / 1500 | 1250 / 750 / 1250 | 1500 / 2250 / 2750 | 1500 / 1250 / 1500 | 1500 / 1750 / 2500 | 1750 / 3000 / 3500 | 1750 / 3000 / 2500 | 11500 / 31000 / 29000 | 6500 / 31250 / 29250 |
| FIXED LARGE LIST | 750 / 750 / 1500 | 1250 / 750 / 1250 | 2750 / 2000 / 2000 | 1500 / 1500 / 1500 | 1750 / 2250 / 2500 | 2750 / 1750 / 2000 | 1750 / 2500 / 2750 | 11000 / 3250 / 7250 | 8250 / 4000 / 15250 |

How many tasks of each level (fewest `nand` steps, plan section 2; **[Xa9]** an order fixed before running, not a minimum instruction count: Avida credits a task by the output, and arithmetic instructions such as `sub` and `inc` can reach some logic functions without `nand`) were ever common, and the earliest update any of them was (Avida's count):

| environment | level 1 | level 2 | level 3 | level 4 | level 5 | level 6 | level 7 | level 8 | level 9 | level 10 |
|---|---|---|---|---|---|---|---|---|---|---|
| FIXED LIST, GRADED | 2 (1500) / 2 (1250) / 2 (2750) | 2 (1750) / 2 (1500) / 2 (1750) | 2 (1750) / 2 (2500) / 2 (3750) | 1 (2250) / 2 (4250) / 1 (3750) | 1 (17500) / 1 (5250) / 1 (21000) | 0 / 0 / 0 | 0 / 0 / 0 | 0 / 0 / 0 | 0 / 0 / 0 | 0 / 0 / 0 |
| ONE HARD TASK ONLY | 0 / 0 / 0 | 0 / 0 / 0 | 0 / 0 / 0 | 0 / 0 / 0 | 0 / 0 / 0 | 0 / 0 / 0 | 0 / 0 / 0 | 0 / 0 / 0 | 0 / 0 / 0 | 0 / 0 / 0 |
| NO TASK REWARDS | 0 / 0 / 0 | 0 / 0 / 0 | 0 / 0 / 0 | 0 / 0 / 0 | 0 / 0 / 0 | 0 / 0 / 0 | 0 / 0 / 0 | 0 / 0 / 0 | 0 / 0 / 0 | 0 / 0 / 0 |
| GROWING LIST | 2 (1500) / 2 (1250) / 2 (2000) | 3 (2250) / 3 (2250) / 3 (2250) | 7 (3250) / 7 (3250) / 7 (3250) | 11 (4250) / 10 (4250) / 9 (4250) | 12 (5250) / 11 (9000) / 11 (6000) | 16 (6250) / 14 (10000) / 13 (7000) | 10 (6250) / 9 (10250) / 11 (8000) | 7 (8500) / 0 / 4 (8000) | 0 / 0 / 1 (9250) | 0 / 0 / 1 (10000) |
| COMMON TASKS PAY LESS | 2 (1500) / 2 (1250) / 2 (2250) | 3 (1750) / 2 (1500) / 2 (1750) | 3 (1750) / 2 (2000) / 3 (3250) | 5 (1750) / 2 (3250) / 3 (2500) | 5 (8750) / 1 (31750) / 1 (29500) | 2 (12000) / 0 / 0 | 1 (40500) / 0 / 0 | 0 / 0 / 0 | 0 / 0 / 0 | 0 / 0 / 0 |
| FIXED LARGE LIST | 2 (1500) / 2 (1250) / 2 (3000) | 3 (1750) / 3 (1750) / 3 (1750) | 7 (1750) / 7 (2250) / 6 (2000) | 6 (1750) / 8 (2250) / 4 (2000) | 6 (1750) / 10 (2250) / 5 (3500) | 4 (3750) / 10 (3000) / 2 (26750) | 3 (9500) / 6 (4000) / 1 (28000) | 4 (25500) / 1 (11250) / 2 (28500) | 0 / 0 / 0 | 0 / 0 / 0 |

- In GROWING LIST, the tasks of a level became common soon after the level was rewarded: e.g. seed 2's level 6, rewarded from 9,000, first common at 10,000. Only 4 tasks, all level 7 in seed 1 (3AP, 3AU, 3BP, 3CL), became common before their level was rewarded (at 6,250, with level 7 rewarded from 7,000). In seed 3 the level-9 and level-10 tasks each had one task common (the level-10 task 3AB at 10,000, the update its level was added).
- In FIXED LARGE LIST, the first tasks of levels 1 to 5 became common between 1,250 and 3,500 in every seed; of levels 6 to 8, between 3,000 and 28,500, and fewer of them.
- In ONE HARD TASK ONLY and NO TASK REWARDS, NOT, NAND, ORN and ANDN were performed by some program in every seed, AND and OR in two, NOR, XOR and EQU in none; none was ever common.

## 6. Keeping

Avida's count:

| environment | ever common (1/2/3) | common at 50,000 of those | performed by none at 50,000 | times a common task fell to none | highest common count |
|---|---|---|---|---|---|
| FIXED LIST, GRADED | 8 / 9 / 8 | 7 / 8 / 8 | 0 / 0 / 0 | 0 / 0 / 0 | 7 / 9 / 8 |
| ONE HARD TASK ONLY | 0 / 0 / 0 | 0 / 0 / 0 | 0 / 0 / 0 | 0 / 0 / 0 | 0 / 0 / 0 |
| NO TASK REWARDS | 0 / 0 / 0 | 0 / 0 / 0 | 0 / 0 / 0 | 0 / 0 / 0 | 0 / 0 / 0 |
| GROWING LIST | 68 / 56 / 62 | 65 / 48 / 55 | 0 / 0 / 0 | 2 / 0 / 0 | 66 / 53 / 59 |
| COMMON TASKS PAY LESS | 21 / 9 / 11 | 17 / 9 / 8 | 0 / 0 / 0 | 0 / 0 / 2 | 17 / 9 / 10 |
| FIXED LARGE LIST | 35 / 47 / 25 | 32 / 41 / 0 | 0 / 0 / 5 | 2 / 5 / 11 | 32 / 41 / 20 |

- Of the tasks ever common, the share common at 50,000: FIXED GRADED 0.875 / 0.889 / 1.0; GROWING LIST 0.956 / 0.857 / 0.887; COMMON TASKS PAY LESS 0.81 / 1.0 / 0.727; FIXED LARGE LIST 0.914 / 0.872 / 0.0 (the counting fault; the test processor gives 0.941 / 0.911 / 0.619, and for the others: FIXED GRADED 0.875 / 0.889 / 1.0, GROWING LIST 0.956 / 0.852 / 0.902, COMMON TASKS PAY LESS 0.941 / 1.0 / 0.8).
- No task ever common was performed by no program at 50,000, except in FIXED LARGE LIST seed 3 (5, by Avida's count).
- **[Xb6]** FIXED LARGE LIST seed 3's "times a common task fell to none" (11) is mainly the counting fault of section 2.

## 7. Reuse (M6)

In the most common distinct instruction sequence of each run at update 50,000, run alone in the test processor with every instruction ablated in turn (replaced by `nop-X`): for each pair of tasks it performs, the earlier (by first appearance in that run) and the later, the share of the later task's required instructions also required for the earlier, against the share expected if they were placed at random among the instructions not required for replication.

| run | programs with this sequence | length | replicates | required for replication | tasks performed | pairs | mean shared | mean expected | pairs above | pairs below | pairs sharing nothing |
|---|---|---|---|---|---|---|---|---|---|---|---|
| fixed_graded_seed1 | 14 | 99 | yes | 14 | 7 | 19 | 0.1634 | 0.0793 | 10 | 9 | 9 |
| fixed_graded_seed2 | 41 | 83 | yes | 13 | 8 | 26 | 0.4113 | 0.2022 | 24 | 2 | 1 |
| fixed_graded_seed3 | 14 | 117 | yes | 19 | 8 | 26 | 0.1966 | 0.0852 | 14 | 12 | 12 |
| equ_only_seed1 | 8 | 97 | yes | 20 | 0 | 0 | - | - | 0 | 0 | 0 |
| equ_only_seed2 | 7 | 104 | yes | 20 | 0 | 0 | - | - | 0 | 0 | 0 |
| equ_only_seed3 | 776 | 22 | yes | 9 | 0 | 0 | - | - | 0 | 0 | 0 |
| no_rewards_seed1 | 8 | 97 | yes | 20 | 0 | 0 | - | - | 0 | 0 | 0 |
| no_rewards_seed2 | 7 | 104 | yes | 20 | 0 | 0 | - | - | 0 | 0 | 0 |
| no_rewards_seed3 | 776 | 22 | yes | 9 | 0 | 0 | - | - | 0 | 0 | 0 |
| growing_seed1 | 8 | 134 | yes | 23 | 64 | 1604 | 0.5988 | 0.1809 | 1604 | 0 | 0 |
| growing_seed2 | 46 | 109 | yes | 63 | 46 | 884 | 0.1258 | 0.0508 | 252 | 202 | 617 |
| growing_seed3 | 17 | 108 | yes | 44 | 55 | 1377 | 0.4119 | 0.1655 | 1116 | 60 | 252 |
| common_pays_less_seed1 | 14 | 93 | yes | 21 | 15 | 99 | 0.4091 | 0.1646 | 81 | 18 | 15 |
| common_pays_less_seed2 | 7 | 155 | yes | 20 | 9 | 34 | 0.4032 | 0.1436 | 28 | 6 | 4 |
| common_pays_less_seed3 | 11 | 97 | yes | 15 | 8 | 26 | 0.2143 | 0.0933 | 17 | 9 | 7 |
| fixed_large_seed1 | 4 | 245 | yes | 62 | 31 | 386 | 0.1981 | 0.0335 | 226 | 64 | 160 |
| fixed_large_seed2 | 5 | 195 | yes | 19 | 41 | 769 | 0.5755 | 0.1837 | 768 | 1 | 1 |
| fixed_large_seed3 | 44 | 95 | yes | 20 | 13 | 76 | 0.3672 | 0.1991 | 65 | 11 | 6 |

- **[Xb2] Pairs left out.** A pair is counted only if its two tasks first appeared at different 250-update samples (first appearance in the program population, resolved to 250 updates) and the later task has at least one required instruction. Of 6,145 possible pairs in the 12 runs, 688 were left out for the first reason and 131 for the second: the later task survives every single ablation, as NOT, NAND and ORN do in growing seeds 2 and 3 and fixed large seed 1. That leaves 5,326 counted (per run in the corrected `.json`).
- **[Xb7]** Each row describes one distinct instruction sequence, the most common at 50,000, carried by 4 (fixed large seed 1) to 776 programs of about 3,600; in some runs that is one program's circuits, not the program population's.
- **All 12 runs with pairs: the mean shared share exceeds the mean expected** (for example GROWING LIST seed 1: 0.599 against 0.181, over 1,604 pairs, every pair above; FIXED GRADED seed 1: 0.163 against 0.079, 10 pairs above and 9 below). Over all pairs: **4,205 above the expectation, 394 below**, 727 equal (5,326 pairs).
- In ONE HARD TASK ONLY and NO TASK REWARDS the most common sequences perform no task (in seed 3 of both, a 22-instruction program carried by 776 programs).
- **Unsure**: the required instructions of every task include the reads that bring the inputs in, which any two tasks need; the random expectation does not allow for that, so part of the sharing may be the shared input reads rather than one circuit built on another. The order "earlier, later" is by first appearance in the run, not in this program's own ancestry.

## 8. The comparisons the plan named (section 6), by the plan's rule

"More" only if every seed of one environment is above every seed of the other; "fewer" the reverse; otherwise "not separated by three seeds". Each is given by Avida's count and by the test processor.

- **E1, one hard task against graded.** EQU common in 0 of 3 ONE HARD TASK ONLY seeds (never performed by any program) and in 3 of 3 FIXED GRADED seeds (17,500, 5,250, 21,000; the test processor: 20,000, 10,000, 25,000). **Not against the expectation.**
- **E2, no rewards.** 0 common at 50,000 in every seed. Fewer than FIXED GRADED, GROWING LIST and COMMON TASKS PAY LESS; not separated from ONE HARD TASK ONLY (the same runs); against FIXED LARGE LIST not separated by Avida's count (because of seed 3's 0), fewer by the test processor. **Not against the expectation.**
- **E3, growing list against fixed graded.** More (48 to 65 against 7 to 8). **Not against.**
- **E4, "a growing list learns more new capabilities than a fixed list"**, growing against fixed large, common at 50,000: 65 / 48 / 55 against 32 / 41 / 0 (Avida's count), 65 / 46 / 55 against 32 / 41 / 13 (test processor): **more**, by both readings. **Not against the proposition; against Claude's expectation** ("not separated"). Present at 50,000: 74 / 67 / 72 against 54 / 67 / 32 (74 / 65 / 72 against 54 / 67 / 51): not separated by three seeds.
- **E5, rising or levelling off.** Expected: FIXED GRADED and ONE HARD TASK ONLY level off in every seed; GROWING LIST and FIXED LARGE LIST still rising after 40,000 in at least two seeds. Found: GROWING LIST levelled off in seeds 1 and 3 by Avida's count and in all three by the test processor; FIXED LARGE LIST in seeds 1 and 3 by both; FIXED GRADED seed 2 made a new high at 43,250 by Avida's count, and seeds 1 and 3 at 50,000 and 45,000 by the test processor. **Against the expectation**, by both readings.
- **E6, common tasks pay less against fixed graded.** Common at 50,000: 17 / 9 / 8 against 7 / 8 / 8 (test processor 16 / 9 / 8 against 7 / 8 / 8): not separated. Two-input tasks present by any program: 9 / 9 / 9 against 8 / 9 / 9: not separated. **Not against** (the "against" was "fewer"), but the expected "more of the nine present" is not shown either. **[Xa5, Xb8, Xc3]** The third part of the expectation, "its programs spread over tasks rather than all performing all of them", was not measured in the results as sent. Measured after the fact (so not a test), as the number of the nine tasks one program performs on average at 50,000 (the sum of the nine shares): COMMON TASKS PAY LESS 7.63 / 7.21 / 6.56 against FIXED GRADED 6.16 / 6.41 / 6.97 by Avida's count, and 5.67 / 4.67 / 4.63 against 4.60 / 4.70 / 4.96 by the test processor. Not separated by three seeds, and no sign of spreading: **not shown**. The S114 restart audit found COMMON TASKS PAY LESS possibly lowered by the pieces (fewer births and fewer common capabilities just after reloads, in all three seeds, below its thresholds). So any comparison here that turns on one or two capabilities is to be read with caution.
- **E7, keeping.** Expected at least 90% kept in the middle seed of every rewarding environment. Middle shares, Avida's count: FIXED GRADED 0.889, GROWING LIST 0.887, COMMON TASKS PAY LESS 0.81, FIXED LARGE LIST 0.872; test processor: 0.889, 0.902, 0.941, 0.911. **Against the expectation** by Avida's count in all four, by the test processor in FIXED GRADED only (0.889: one of 9 tasks not kept in seed 2).
- **E8, reuse.** Mean shared above the random expectation in 12 of 12 runs with pairs; 4,205 pairs above, 394 below. **Not against** (with the doubt in section 7).

## 9. Checks

- **Listing unrewarded tasks changes nothing** (before running, plan section 3; one 1,000-update piece, seed 1000: identical counts). **[Xa6]** That check had a population doing only NOT, and compared `tasks.dat` and `count.dat` (its one line of `average.dat` is identical too). **Rerun after the cross-examination**: FIXED GRADED seed 2's population saved at 50,000 (21 tasks present, three-input ones among them) was run 1,000 updates from the same seed (2049), once with the 77 tasks listed and once with the nine only. `count.dat`, `average.dat` and the nine task columns were identical at all 20 samples, while the 77-task run counted 132 to 146 three-input performances per sample. One population, one seed.
- **ONE HARD TASK ONLY is the same run as NO TASK REWARDS, seed by seed**: every line of `tasks.dat` and `count.dat` in all 50 pieces of each seed is identical (only the date lines differ), because no program ever performed EQU, so the one reward never paid.
- **The pieces against S111's unbroken runs** (S111's nine-task environment, the same settings, run in one piece; a different random sequence): EQU first common at 16,000 / 23,000 / never in S111, at 17,500 / 5,250 / 21,000 in FIXED GRADED here; the nine tasks common at 50,000: 9 / 9 / 7 in S111, 7 / 8 / 8 here. Not separated by three seeds. **[Xa7]** No rule was set for this check, and the random sequences differ. Seed by seed, the EQU times differ up to fourfold both ways (5,250 against 23,000 in seed 2; 21,000 against never in seed 3), so this check catches only gross differences. The proper check is the S114 restart audit (`results/S114 Restart audit - results.md`), run on the same runner with its own seeds. It found FIXED GRADED readable as unbroken within its thresholds, through the spread of three seeds. It found COMMON TASKS PAY LESS possibly lowered by the pieces: births 5% to 10% lower, common capabilities leaning lower just after reloads, below its thresholds. GROWING LIST and FIXED LARGE LIST were not audited, and GROWING LIST cannot be separated from its breaks.
- **[Xa4] The resources of COMMON TASKS PAY LESS ran low**, so a common task did pay less. At the 50 piece ends, the middle levels of the resources of tasks common through most of the run were 235 to 301 in seed 1 (all nine), 304 to 345 in seed 2 (all but XOR and EQU) and 112 to 179 in seed 3 (all but AND, XOR and EQU). Full pay needs 400 (`frac=0.0025`, `max=1.0`), and those levels were under 400 at 70% to 98% of piece ends. So a common task paid about 2^(0.59 to 0.86 × its level) in seeds 1 and 2 and 2^(0.28 to 0.45 × its level) in seed 3. The resources of tasks common only late or never stayed near full for most of the run (middle 7,024 to 9,950).
- **[Xb5] The resource levels were carried exactly** across every reload: at all 49 reloads × 9 resources × 3 seeds (1,323 values), the level written into the next piece equals the level printed at the piece's end. The S114 audit found the same at its 27 reloads, and found the levels swinging for about 20 updates after each reload. The piece-end levels above are read 1,000 updates after the reload.
- **Programs at 50,000**: 3,484 to 3,600 in every run (the world holds 3,600).

## 10. Departures from the plan

1. **The second reading** (section 2): the test processor on the saved program populations, added after the runs because Avida's world count fails after a load where processor time is very uneven. Its first appearances are at 5,000-update steps only.
2. **Each piece ran 1,001 updates, not 1,000** (found by the S115 check of reply 06, `targets/avida/Avida2Driver.cc`: `Exit` at update label 1,000 comes after updates 0 to 1,000). A run is 50,050 updates, not 50,000; every update named here is the label (piece number x 1,000 + the update within the piece).
3. **The run took 7 h 43 min**, within the plan's "about 8 hours"; no run was cut short.
4. **The task ranking's search** was capped at 9 steps after running out of memory at 10 (plan section 2, before running); the one task not found (3AB) got 10, a lower bound.
5. **The reuse measure** was first run on the six seed-1 runs to test it (not used); the numbers above are from the run after all 18 ended.
6. The runner's note and the plan's section 3 give the instruction changes as copy error 0.0075 per copied instruction and one inserted and one deleted instruction each with probability 0.05 per copy (S111's `avida.cfg`, unchanged); the runner's note mentions only the first (found by the S114 check; no number changes).
7. `pkill -f` was used once, before the plan, to stop Claude's own task-ranking search; the pattern also ended Claude's own shell. No other process was touched. Every later stop would have been by exact process number; none was needed.
8. **[Xb3, Xc4] The check of the load undercount** compares the count 250 updates after a load with the previous piece's end, not the 250 and 1,000 counts within one piece as the plan said (section 2 gives both).

## 11. What was not measured

- Tasks other than the 77 logic tasks; other instruction sets, world sizes, instruction-change rates; runs longer than 50,000 updates; more than three seeds.
- A growing list built another way (Avida's cascades, a fixed schedule, a list that also grows beyond the designer's 77, or grows from what the program population produces); the growing list with resources that run down.
- Whether the growing list's lead comes from the order of rewards (easy first) or from something else in its history, such as the smaller rewards in its first 10,000 updates; no run separates these.
- The first appearance of a capability in a program's own ancestry, rather than in the program population; which circuit a new task grew from (S112's trace reader was not extended to three-input tasks).
- Whether the pieces changed the course of the runs (only whether they changed the count; S114's audit covered FIXED GRADED and COMMON TASKS PAY LESS, not the growing or fixed large lists).
- The world's inputs: the test processor uses its own fixed inputs, the world gives each program other numbers.

## 12. What the results say about the owner's question

The owner asked (S63) "what kind of execution environment can use these machines to progressively learn how to do new things". Observations from these 18 runs only, settling nothing (S28):

- **An environment that pays for nothing, or only for one hard thing, taught these programs nothing new that became common** **[Xc6]** (two or three tasks were performed by single programs at 50,000). No task became common. With EQU alone rewarded, EQU never appeared, and the reward never acted: those runs are the same runs as with no reward at all. **[Xa2]** In these runs, then, the reward for a task no program ever performed never changed a run's course. Whether a reward reaches the program population only when some program is already near the task was not measured; it is a guess to test.
- **Every environment that paid for easier tasks as well produced new capabilities, and kept most of them.** The ones that paid for more kinds of task produced more: nine two-input tasks gave 7 to 8 common; 77 tasks all offered at once gave 13 to 41 (by the test processor; Avida's count gave 0 in one seed, the counting fault of section 2; **[Xc5]** by the plan's rule, more than the nine by the test processor, not separated by Avida's count); the same 77 tasks offered as a list that started with the two easiest and grew one level at a time, as soon as the program population had made one task of the top level common, gave 46 to 65, the most in every seed.
- **What differed between the growing list and the fixed large list was the order and the timing, not the final list**: both rewarded (nearly) the same 77 tasks from update 11,000 on. Starting from the easy tasks and adding harder ones only once something at the top was common left the program population with more capabilities than having every task on offer from the start. Why is not shown here (section 11).
- **Making a common task pay less** did not separate from paying a fixed amount for the same nine tasks, in these three seeds; in one seed it went on to seven or eight three-input tasks (by the two readings) that nobody paid for.
- **[Xa1] None of these environments was shown to make learning go on**. In 11 of the 12 paying runs the count of common capabilities rose for a while and then nearly stopped (at 50,000 at most one above its count at 40,000), within the 77 tasks the designer listed, with most of the rise in the first 10,000 to 25,000 updates. One run, FIXED LARGE LIST seed 2, was still rising at the end (37 at 45,000, 41 at 50,000). Longer runs were not tried. Where the list was fixed, the program population filled part of it and stopped; where it grew, it grew to the designer's end and then the program population stopped too. None supplied problems beyond the designer's list, and none was built to.
- **New circuits share instructions with the earlier ones** more than chance, in every run where it could be measured, which is what one would see if later capabilities were built on the parts of earlier ones; the measure cannot yet tell that apart from the shared input reads.
