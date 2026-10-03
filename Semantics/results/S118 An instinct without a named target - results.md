# S118 An instinct without a named target: results

*Log S118, decisions S71 and S72. Written 1 October 2026 by the second Opus 5.5 agent of log S118 (one agent per job, S56, S68; no subagent or workflow), which continued the first S118 agent's work after the owner's correction. Read with the plan written before running (`results/S118 An instinct without a named target - how it will be tested, written before running.md`, d1ecec9) and the addendum written before the pilots were read (`results/S118 An instinct without a named target - addendum after the owner's correction (S72), written before the pilots were read.md`, 2ca6c1a). Numbers: `results/S118 An instinct without a named target - results.json` (524deaa). In the owner's Avida terms (S61): an **Avida execution environment** is the simulated computational environment in which programs execute (what it pays, what it requires before a copy, how it copies); a **program population** is its programs; a **computational capability** (a task) is one of Avida's 77 logic tasks; **present** means performed by at least one program, **common** by at least 10 in 100. No GLM check (S70's latest word on GLM). Nothing in the theory, Part A, Part B, the S110 to S117 files, the plan, the decisions, the terms file or `authority/` was touched. S117's open reading stays open.*

---

## 1. The direct answer, in the S72 sense

**The question (S72, with S71 and S63).** Can an Avida execution environment, the selector, have an instinct to solve problems: a way of selecting under which the program population comes to solve problems, without the execution environment being given exact target goals?

**Answer: only in part.**

- **Yes, at grade 2 ("named one level up"), and only in part by the plan's own test.** The execution environment P1 was told no function. It was told only "any function of the three numbers counts the same, and a function many programs already compute counts less". Under it the program population came to compute 17, 12 and 21 functions commonly by update 20,000 (three seeds, by the test processor). Among them were 11, 6 and 14 three-input functions, none of which the execution environment singled out. But its checking code still writes down the class: the 251 functions of Avida's 77 logic tasks. By the plan's test the result is **mixed**, not "for". It did more than the execution environments that name a short list (7 in their middle seed) in all three seeds. It did less than the execution environment that names all 77 with graded pay (24 in its middle seed) in all three seeds, though seed by seed the spreads overlap (P1 21 against that environment's 12 in seed 3). It kept adding new common functions after update 10,000 in two seeds (8 in seed 1, 1 in seed 2) and added none in the third, which had 22 by then.
- **An execution environment that keeps only solvers makes solving a condition of lasting, but it gives a floor, not a drive.** The execution environment P2 named no function either. From update 5,000 it let a program finish a copy only if that program had solved something during the copy. In every seed the program population survived. It fell to between 1,221 and 2,339 programs 250 updates later and was back at 3,488 or more by 5,500. The share of programs that solve something went from under 1 in 100 to 70 to 77 in 100. Among the programs that can copy themselves at all, the share went to 93 to 96 in 100 (a check made after reading). But the population settled on the two easiest functions (NOT and NAND, one nand step each): 2 common functions in every seed.
- **"Truly unnamed" (grade 3) was not reached and could not be.** As the plan said, these pilots cannot reach it. An execution environment whose criterion comes from outside its own checking code needs either other evolving programs as judges (parasites, stock Avida, not run) or new C++ (paying for predicting what the world does next, not built).

So, in the owner's picture: a stock Avida execution environment can act like an agent that keeps whatever works, without being told what "working" looks like function by function. But it must still be told what kind of thing counts as working (a function of the numbers), and the 20,000 updates here show no sign that it keeps finding harder things on its own. The functions it found stay easy: the hardest common one needs 5 nand steps, against 7 to 10 in S113's GROWING LIST.

## 2. What was run

Two execution environments (the plan's section 3), each three seeds of 20,000 updates in one continuous Avida process. Both used stock Avida at commit 47f13dad, S111's settings and instruction set, the default ancestor (which performs no task), a 60 x 60 world and copy error 0.0075. The driver started at 10:13 and ended at 11:00:13 UTC on 1 October 2026, exit 0, every run exit 0.

- **Set-up check (plan, departure 3).** P2 up to update 1,000 matches S113's NO TASK REWARDS first piece of the same seed exactly (task rows and count rows at 250, 500, 750, 1,000 identical in all three seeds). **Passed.**
- **How P1's pay actually fell (seed 1 at 20,000, Avida's resource levels).** The resource of the most common function (ORN, 2,952 of 3,596 programs) was at 168, so it paid 0.42 of a doubling. Functions computed by no program had full resources (9,950), paying the cap of 1.0. So "rare pays more" works as "common pays less": rarity beyond the cap earns nothing extra.

## 3. The mechanisms (from the plan's table, read in the S72 sense)

| # | Mechanism (plan's row) | Stock? | How named | An instinct of the execution environment? (addendum, section 3) | Tested here |
|---|---|---|---|---|---|
| 1 | Pay for any function of the numbers | stock | one level up | candidate, grade 2 | yes (P1) |
| 2 | Pay for any output | stock | unnamed, but no problem posed | no: selects for no problem | no |
| 3 | Pay for output that depends on the input | bitwise stock; general C++ | one level up | candidate, grade 2 | bitwise part only (= row 1) |
| 4 | Rare pays more | within a listed class stock; open-ended C++ | one level up | candidate, grade 2; preferences follow the population by a fixed rule | yes (P1) |
| 5 | Prediction of the world's next numbers | C++ | grade 3 for the function | candidate, grade 3 | no (not built) |
| 6 | Copy only after solving something | stock | one level up | candidate, grade 2: a copying rule, not a payment | yes (P2) |
| 7 | Energy model | stock (other instruction set) | as its reactions | candidate | no |
| 8 | Foraging | stock (heavier) | resource named, method not | poses no problem of computing | no |
| 9 | Parasites; programs judging programs | stock | grade 3 for which function, grade 2 for the class | parasites: yes, the execution environment using part of its material as judge; a judging rule carried by programs: no | no |
| 10 | Deme competition | stock | as the measure | candidate (selects groups) | no |
| 11 | Stock tasks with a stated target | stock | named exactly | no | no |
| 12 | Limits on tasks | stock | one level up at best | weak | no |

Source lines for every row are in the plan's section 2 and are not repeated here.

## 4. P1, ANY FUNCTION, RARE PAYS MORE: against the plan and the addendum

Common functions (performed by at least 10 in 100 programs), by the test processor, seeds 1 / 2 / 3:

| update | P1 | FIXED LARGE LIST (all 77, graded pay) | COMMON TASKS PAY LESS (9, depleting) | FIXED LIST, GRADED (9) | GROWING LIST | NO TASK REWARDS |
|---|---|---|---|---|---|---|
| 5,000 | 7 / 6 / 5 | 10 / 8 / 15 | 7 / 6 / 5 | 5 / 6 / 5 | 7 / 9 / 9 | 0 / 0 / 0 |
| 10,000 | 8 / 11 / 22 | 23 / 21 / 13 | 13 / 7 / 7 | 6 / 7 / 7 | 43 / 24 / 56 | 0 / 0 / 0 |
| 15,000 | 14 / 10 / 21 | 24 / 28 / 12 | 14 / 7 / 7 | 6 / 7 / 7 | 54 / 29 / 52 | 0 / 0 / 0 |
| 20,000 | **17 / 12 / 21** | 24 / 26 / 12 | 16 / 7 / 7 | 6 / 7 / 7 | 54 / 34 / 54 | 0 / 0 / 0 |

S113's numbers are S113's test-processor summary. S113 ran 50 pieces of 1,000 updates with reloads, while P1 ran unbroken; S114's restart audit found the two alike in FIXED LIST, GRADED and found COMMON TASKS PAY LESS possibly lowered by the pieces. Avida's own count in the world gives P1 17 / 12 / 21 at 20,000 as well.

Further measures at 20,000, seeds 1 / 2 / 3:

- **Present** (any program): 25 / 19 / 26. FIXED LARGE LIST: 48 / 50 / 33.
- **Of the common functions, three-input:** 11 / 6 / 14.
- **Share of programs performing at least one function:** 80 / 79 / 79 in 100 (FIXED LARGE LIST 80 / 84 / 83). Among programs that can copy themselves: 99.9 / 98.9 / 93.4 in 100 (after reading).
- **Distinct functions per program:** middle 7 / 6 / 20, largest 13 / 8 / 21. Programs compute many functions each rather than dividing them up: in seed 3 the typical program computes 20 of the 21 common ones.
- **Hardness of the common functions** (fewest nand steps): largest 5 / 5 / 5, middle 3 / 3 / 3. FIXED LARGE LIST: 7 / 7 / 5 and 4 / 4 / 3. GROWING LIST: 8 / 7 / 10 and 5 / 4 / 5.
- **New common functions after 10,000.** By the test processor (common at 15,000 or 20,000, not at 5,000 or 10,000): 8 / 1 / 0. By Avida's count (first common after 10,000): 5 / 1 / 0.

**The plan's test (section 5).**

- "For" needed at least FIXED LARGE LIST's middle seed (24) in two of three seeds, and new functions still becoming common between 10,000 and 20,000. **Not met**: 17, 12 and 21 are all below 24.
- "Against" needed fewer common functions than COMMON TASKS PAY LESS or FIXED LIST, GRADED in their middle seed (7) in two of three seeds, or no new common function after 10,000. **Not met** on the first: 17, 12 and 21 are all above 7. On the second it is met in one seed (seed 3) of three.
- **So P1 is mixed, as the plan defines it.**

**Read in the S72 sense (addendum, section 4).** P1 is an execution environment that selects by "anything that computes some function of the numbers counts; whatever is common counts less". Told no function, it made the program population compute two to three times as many functions as the execution environments told a short list. It did not do as well as the one told all 77 with graded pay, which is told more: which functions are harder. Its push kept acting in seeds 1 and 2 and stopped in seed 3. Condition (b) of the addendum's definition holds in all three seeds; condition (c) holds in two.

## 5. P2, SOLVE SOMETHING TO REPLICATE, NOTHING PAID: against the plan and the addendum

**Around the switch** (every 250 updates; programs, then births in that update):

| seed | 5,000 | 5,250 | 5,500 | 6,000 |
|---|---|---|---|---|
| 1 | 3,596 (203 births) | 1,221 (46) | 3,488 (159) | 3,592 (179) |
| 2 | 3,598 (190) | 2,236 (82) | 3,585 (158) | 3,594 (170) |
| 3 | 3,598 (239) | 2,339 (150) | 3,597 (200) | 3,598 (242) |

**Which functions carried it through** (Avida's count at 5,250): NOT in every seed (1,215, 1,250 and 2,321 programs). In seed 2 also NAND (485) and ANDN (490). At 20,000: NOT and NAND in every seed, with a few ORN and one or two of a three-input function. **None of the three seeds died out.**

**The share of programs performing at least one function**, by the test processor over every program: 0.2 / 0.5 / 0.4 in 100 at 5,000, then 77 / 70 / 74 in 100 at 20,000. Among programs that can copy themselves (after reading): 0.3 / 0.6 / 0.5 at 5,000, then 95.6 / 93.1 / 94.1 at 20,000. S113's NO TASK REWARDS at 20,000: 0.07 / 0.5 / 0 in 100 of those that can copy.

**Common functions at 20,000:** 2 / 2 / 2 (NOT and NAND; one nand step each). Present: 3 / 3 / 4. Distinct functions per program: middle 1, largest 3 / 2 / 2.

**The plan's tests.**

- *Lasting depends on solving.* "For" needed at least 90 in 100 by 20,000 in every surviving seed. **Not met as written**: 77, 70 and 74, counted over every program. "Against" needed the population to die out in every seed, or the share to stay under 50 in the survivors. **Not met.** So the result lies between the two. The reason, seen only after reading: in every execution environment, the control included, about a quarter of the programs in a saved population are broken copies that cannot copy themselves at all (programs that can copy: 71 to 76 in 100 here, 74 to 82 in 100 in NO TASK REWARDS). Counted over the programs that can copy, the share is 93 to 96 in 100. The plan's threshold did not allow for this. Since this is a reading after the fact, it is reported beside the test, not in place of it.
- *A drive beyond the minimum.* "For" needed at least FIXED LIST, GRADED's middle seed at 20,000 (7). "Against": settles on one or two of the easiest functions. **Against met**: 2 / 2 / 2, the two easiest. Claude's written expectation ("a requirement makes a floor, not a drive") held.

**Read in the S72 sense.** P2 is an execution environment that selects by "nothing is kept unless it solves something", with no preference among solutions. Such a selector makes solving universal among the programs that last, almost at once (within about 500 updates the world's own count of performances had caught up with the number of programs), and then asks for nothing more. Condition (b) holds only for the two easiest functions. Condition (c) holds as a floor: the push keeps acting, but it is met once and does not push further.

## 6. How it bears on S117's breaks 4, 5 and 6

- **B4, "In Avida, lasting does not require doing the task."** P2 shows that one stock setting changes this: in P2's execution environment no program finishes a copy without solving something, and all three program populations survived the change. But what lasting requires there is solving *something* during each copy, not staying faithful to a particular task. A lineage that loses NOT and gains NAND lasts. So B4 is **closed in part**: lasting can be made to require solving, but not the fidelity to one task that D12.1's survival condition speaks of. Whether D12.1's condition is a fact about the world or a stipulation stays as S117 left it.
- **B5, "Explanation as an activity has nothing in Avida."** **Unchanged.** Neither execution environment lets programs offer rivals or criticize each other. P1's selector values things differently as the population changes, which comes nearest to a problem situation that changes, but it does so by a fixed rule and criticizes nothing.
- **B6, "Avida's learning new things is selection, not creation."** **Unchanged in kind, narrowed in one respect.** P1's new common functions arose as S113's did: copy errors, then selection. What changed is that the selector no longer needs each function named. It needs only the class. Construction (the semantics' Build) still fails. If the execution environment is read as the agent (S72), then its selecting, together with the copy errors it introduces, is the nearest thing in Avida to conjecture and criticism. Whether that counts is close to S117's open reading, and it is recorded for the owner, not decided.

## 7. Departures and failures

1. **The original gathering script summed CPU time wrongly.** Three runs went at once, so each run's figure held the other runs that finished inside its time, and the sum counted them two or three times (16,362 s). A fixed copy (`tools/s118_gather_the_results_fixed.py`; the original kept unchanged) takes each run's time from a record of the Avida processes read from the system every 20 seconds. A first try at recovering the times from the runner's figures alone gave a negative time for one run and was dropped. The fixed copy also writes its full output to the scratch space and adds three counts (first common update per function, new common functions after 10,000, a share every 1,000 updates) without changing any measure.
2. **A check made after reading**: the share of solvers among programs that can copy (`tools/s118_after_reading_count_solvers_among_programs_that_copy.py`). It is reported beside the plan's test for P2, not in its place.
3. **The addendum was written after the runs had started and before any result was read.** The agent writing it had seen only the driver log's "started" line and the run folders' names.
4. **The test processor judges whether a program can copy itself without the copying requirement.** So for P2 "can copy" means "can copy if it were not required to solve". Every program that can copy and also performs a function meets the requirement; one that cannot perform a function would be stopped in the world.
5. **Cost below the plan's estimate**: about 0.25 to 0.43 CPU-hours per run, not 0.5 to 0.7.
6. **The comparison with S113** uses S113's test-processor summary at the same updates, as the plan says. S113's Avida counts at piece ends are in the `.json` for completeness but are not used, because of S113's counting fault after a reload.

## 8. What is unsure

- **Three seeds do not separate P1 from FIXED LARGE LIST.** Seed by seed: 17 against 24, 12 against 26, 21 against 12. P1 is above the short named lists' middle seed (7) in all three seeds, but not seed by seed against every seed: COMMON TASKS PAY LESS seed 1 (16) is above P1 seed 2 (12).
- **20,000 updates is short.** S113's environments kept adding until 30,000 to 48,000. Whether P1 levels off at about 20 or keeps going is not known.
- **What P1 rewards.** It pays any function, but with the cap ("rare" earns no more than the full pay), so what it rewards is "not common". An execution environment that paid more and more for rarer and rarer functions was not tried.
- **Seed 3's spread is not P1's alone.** Most programs compute 20 of 21 functions at once, so a single lineage's success can carry the count. The test processor counts programs, not lineages.
- **Whether the owner's "instinct" is met by a fixed rule.** The addendum's question 1: an execution environment with a fixed way of selecting, or one whose way of selecting itself changes ("progressively learn how to do new things", S63)? Not decided.

## 9. Proposed, not run (each above this job's budget or needing the owner's word)

| proposal | why | cost |
|---|---|---|
| P1 to 50,000 updates, seeds 1 to 3 | set beside S113 at 50,000; does the push keep acting? | about 3 to 4 CPU-hours (about 1.2 to 1.6 hours of wall time at three at once) |
| P1, seeds 4 to 10, 20,000 updates | separate P1 from FIXED LARGE LIST | about 2.5 to 3 CPU-hours |
| P1 and P2 together (pay any function, common pays less, and copy only after solving) | does a floor plus novelty do more than either? | about 2 CPU-hours for three seeds |
| Grade 3 by parasites (plan, row 9; stock) | the execution environment uses evolving programs as its judge | set-up with a parasite instruction set and ancestors, then perhaps 2 to 4 CPU-hours; untried |
| Grade 3 by prediction (plan, row 5; new C++) | the execution environment pays for anticipating its own hidden regularity, which its checking code never computes | a new task of perhaps 100 to 200 lines of C++, a rebuild (about 10 CPU-minutes), then about 2 to 3 CPU-hours |

None is started. S115's batches 4 to 9 are not affected and still await the owner's word.

## 10. Recorded for the owner, not applied

S117's open reading (whether a task list and its checking code, written by people, count in the history of the programs they selected). Whether a fixed way of selecting counts as the execution environment's instinct (addendum, section 5). Whether the execution environment's own copy errors make it a conjecturer as well as a selector (section 6, B6). What knowledge is. How "causes itself" is read. Whether a capability tied to the world's input order counts as learned. Which of S115's batches 4 to 9 to run. Part B. Which of section 9's proposals, if any, to run.

## 11. CPU time

The six runs took 6,763 CPU-seconds by the record (about 1.9 CPU-hours; each run's figure at most about 20 seconds short). The two passes of the fixed gathering script and the check after reading took about 2.2 CPU-minutes. The first S118 agent's mechanics tests before the plan took about 70 CPU-seconds. No other Avida run was made.
