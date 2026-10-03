# S113 Which execution environments learn: how it will be tested, written before running

*Log S113, decisions S62, S63 and S64. Written 30 September 2026 by the one Opus 5.5 agent of log S113 (S56), **before any measuring run**, and committed by that agent before the runs start. In the owner's Avida terms (S61, `records/Semantics - Avida terms, given by the owner.md`): an **Avida program** is one program in a **program population**; a **distinct instruction sequence** is what Avida calls a genotype; a **computational capability** here is one of Avida's logic tasks, and a program has it when Avida credits it with **task performance**; the **Avida execution environment** is the list of rewarded tasks, their rewards and any resources; **Avida fitness** decides how much processor time a program gets; **computational selection** is the resulting differential program replication. All entities are digital programs executing on Avida's virtual CPU; nothing biological is involved. Before this plan, only these runs were made: one run of the task ranking (below), two 2- and 3-piece test runs of the runner (seed 99, in `s113/test_runs/`, not used for any result) and one 1,000-update check that listing unrewarded tasks changes nothing (below). Observations only; nothing is settled (S28).*

---

## 0. The question

The owner, S62: "No no. We now know what minimum functions static knowledge must have. The next step is figuring out how to create new knowledge with these basic building blocks. I'm stumped. I need to think for a bit." S63: "The execution environment is an important clue. Looking inside the machines is the wrong direction. The question is, what kind of execution environment can use these machines to progressively learn how to do new things..." S64, after Claude proposed this test: "Thinking." then "Do it".

So the test: **start every run from the same Avida program, change only the Avida execution environment, and count how many new computational capabilities appear in the program population over time.** Each environment below is a different answer to "what kind of execution environment": reward one hard task; reward a fixed list; reward nothing; make the list grow as the program population becomes able to do more; make common tasks pay less.

## 1. What Avida offers, as found in its source (Avida 2.14.0, commit 47f13dad, built in S111)

The documentation folder was not fetched in S111; everything below is read from the source and from the example configuration files that come with it.

**Task library** (`source/main/cTaskLib.cc`, 214 task names). For the default instruction set (the one of S111 and S112, which reads and writes numbers only through `IO`):
- the nine **two-input logic tasks** of S111 (NOT, NAND, AND, ORN, OR, ANDN, NOR, XOR, EQU);
- **68 three-input logic tasks**, `logic_3AA` to `logic_3CP` (lines 121-188). Together with the nine, they are every logic function of up to three input numbers, taken bit by bit, except the two constants and copying one input unchanged, counting as one task the functions that differ only by which input is which (read from the tasks' accepted "logic ids"; 5 of the 256 ids are accepted by no task: 0, 255 and the three inputs). Avida ships an environment rewarding all 77 (`support/config/misc/environment-all-logic.cfg`);
- **56 arithmetic tasks** (`math_1AA` ... on one input, `math_2AA` ... on two, `math_3AA` ... on three), `echo`, `add`, `sub`, `mult`, `sqrt`, Fibonacci and sorting tasks;
- many tasks that need other instruction sets or world features (movement, messages, groups of cells), not usable here.

**Resources that run down as programs use them** (`cEnvironment.cc`, `DoProcesses`, 1610 on; example `support/config/misc/environment-9resource.cfg`): a `RESOURCE` line gives an amount with an inflow per update and an outflow share per update; a reaction may draw on it (`process:resource=...:frac=...:max=...`); the amount a program gets is the smaller of `max` and `frac` times what is left, and what it gets is taken out of the resource. With `type=pow` the program's merit is multiplied by 2 to the power of (value times the amount got) (`PROCTYPE_POW`). So when many programs perform a task, its resource runs low and each performance pays less. A second example, `environment-cascade.cfg`, makes performing easier tasks produce the resource that harder tasks draw on.

**Changing the environment during a run** (`source/actions/EnvironmentActions.cc`, `SaveLoadActions.cc`): events at chosen updates can change a reaction's value (`SetReactionValue`, `SetReactionValueMult`), its task (`SetReactionTask`), its limits (`SetReactionMinTaskCount`, `SetReactionMaxTaskCount`), resource inflow and outflow (`SetResourceInflow`, `SetResourceOutflow`), or add any environment line (`ChangeEnvironment`). **No event is triggered by the state of the program population**: every event fires at an update (or generation) fixed before the run. The program population can be saved (`SavePopulation`: every distinct instruction sequence, the cells its programs sit in, their average merit and how far each is into its current copy) and loaded into a new Avida process with a new environment (`LoadPopulation`, `cPopulation.cc` 6820 on; it restores each program's cell and merit, the merit scaled for the part of the copy still to do). **Requisites** (`requisite:reaction=`, `noreaction=`, `min_count`, `max_count`) make a reward depend on what the same program has already done in its life.

**How the growing list is made, then.** Because no event can respond to the program population, every run is cut into **50 pieces of 1,000 updates**; at the end of each piece Avida saves the program population and the next piece is a new Avida process that loads it. Between pieces, for the growing list only, the runner reads how many programs performed each task and, by the rule in section 4, may reward more tasks. **All six environments are run in the same pieces**, so the breaks are the same for every environment; S111's unbroken runs serve as the check on what the breaks do (section 7).

## 2. How hard each task is

The only logic instruction in the default instruction set is `nand`. For every one of the 77 tasks, `tools/s113_rank_the_tasks_by_the_fewest_nand_steps_they_need.py` finds the fewest `nand` steps a circuit needs to compute it from the three inputs, by trying every circuit of 1 step, then 2, up to 9 (`results/S113 Which execution environments learn - the runs/the 77 tasks ranked by the fewest nand steps.json`). For the nine two-input tasks it gives 1, 1, 2, 2, 3, 3, 4, 4, 5: exactly S111's reward values. The step count is each task's **level**:

| level | tasks | how many |
|---|---|---|
| 1 | NOT, NAND | 2 |
| 2 | AND, ORN, 3BO | 3 |
| 3 | OR, ANDN, 3AG, 3BA, 3BS, 3BZ, 3CI | 7 |
| 4 | NOR, XOR, 3AH, 3AQ, 3AT, 3AX, 3BY, 3CH, 3CJ, 3CN, 3CP | 11 |
| 5 | EQU, 3AR, 3BG, 3BL, 3BN, 3BR, 3BU, 3CB, 3CC, 3CE, 3CK, 3CM | 12 |
| 6 | 3AL, 3AN, 3AO, 3AV, 3AY, 3BB, 3BC, 3BE, 3BH, 3BJ, 3BV, 3BW, 3CA, 3CF, 3CG, 3CO | 16 |
| 7 | 3AA, 3AC, 3AF, 3AP, 3AU, 3AW, 3BD, 3BI, 3BP, 3BX, 3CD, 3CL | 12 |
| 8 | 3AD, 3AI, 3AJ, 3AK, 3AS, 3BF, 3BK, 3BM, 3BQ, 3BT | 10 |
| 9 | 3AE, 3AM, 3AZ | 3 |
| 10 or more | 3AB ("exactly one input bit is 1") | 1 |

3AB was not found with 9 steps; the search stopped there, so its 10 is a lower bound, used as its level.

## 3. What every run shares

- **The same starting program**: Avida's default ancestor, `default-heads.org` (100 instructions; it performs no task), injected once at update 0.
- **The same instruction set** (`instset-heads.cfg`, 26 instructions), **world** (60 x 60 cells, wrapping at the edges), **instruction-change rate** (copy error 0.0075 per copied instruction, S111's default; one inserted and one deleted instruction each with probability 0.05 per copy), **program replication and death rules**: S111's `avida.cfg` unchanged, S111's copy used (`results/S111 Avida - the runs/configuration/`).
- **The same 77 tasks listed** in every environment, so that Avida counts the programs performing each. A task that is not rewarded is listed with value 0: its reward multiplies merit by 2^0 = 1. **Check made before running**: one 1,000-update piece with seed 1000, once with S111's nine-task environment and once with the 77-task FIXED GRADED environment: the nine tasks' counts every 250 updates and every line of `count.dat` are identical, and the saved program populations differ only in the date line (in `s113/neutral_check/`). Only NOT had appeared by then, so this checks the listing, not a population doing many tasks.
- **Rewards**: `type=pow`, value = the task's level (section 2), at most one reward per task per copy (`requisite:max_count=1`), as in S111.
- **50 pieces of 1,000 updates** = 50,000 updates, as S111. Piece k of seed s runs with Avida seed 1000 s + k.
- Every Avida process runs under a 900-second timeout.

## 4. The execution environments

| name | what is rewarded | the answer it gives to "what kind of environment" |
|---|---|---|
| **FIXED LIST, GRADED** (`fixed_graded`) | the nine two-input tasks, values 1 to 5 by level (S111's environment) | a fixed list of problems with easier stepping stones |
| **ONE HARD TASK ONLY** (`equ_only`) | EQU only, value 5 | one hard problem, no stepping stones |
| **NO TASK REWARDS** (`no_rewards`) | nothing | program replication only (control) |
| **GROWING LIST** (`growing`) | at first NOT and NAND (level 1); then level by level up to all 77, by the rule below | the supply of new problems grows with what the program population can do |
| **COMMON TASKS PAY LESS** (`common_pays_less`) | the nine two-input tasks, values 1 to 5, each drawing on its own resource that runs down | a task pays less the more programs perform it |
| **FIXED LARGE LIST** (`fixed_large`) | all 77 tasks from the start, value = level | many problems from the start, none added |

**The growing list's rule.** After each piece, if at least one task of the highest level now rewarded is performed by at least 10% of the program population (Avida's `tasks.dat` count at the piece's end, divided by the number of programs in `count.dat`), the next level is added to the rewarded list (all its tasks, value = level). At most one level is added per piece. Once added, a level stays rewarded. So the list can grow from 2 tasks to 77 in no fewer than 9 pieces, and only as fast as the program population makes each level's tasks common.

**The resources of COMMON TASKS PAY LESS.** One global resource per two-input task: inflow 100 per update, outflow 1% per update (so it settles at 10,000 when unused), `frac=0.0025`, `max=1.0` (Avida's `environment-9resource.cfg` values for inflow, outflow and frac; its `max=25` with `type=add` changed to `max=1.0` with `type=pow`, so that a program performing a task when the resource is full gets exactly FIXED GRADED's reward, 2 to the level; when more programs perform it than the inflow feeds, each gets less). The amount left at the end of a piece is carried into the next piece as its starting amount (`initial=`); the first piece starts at Avida's default, 0.

The seven files are in `results/S113 Which execution environments learn - the runs/configuration/` (each environment's first piece, and the growing list with all ten levels rewarded), with the events of the first and of every later piece.

**Why no other environments.** Arithmetic tasks, cascades (the `environment-cascade.cfg` way of growing the supply) and environments that change on a fixed schedule are left out, to stay within the budget; the growing list is made responsive to the program population, which is the owner's "as it learns". A growing list with depletable resources is not run (budget).

## 5. The measures

For each run, from `tasks.dat` and `count.dat` every 250 updates (the counts at the first 250 updates of a piece are taken as Avida gives them; since a loaded program's record of its tasks is empty until it completes one copy, these counts may be a little low; this is measured by comparing the 250 and 1,000 counts within pieces and reported):

- **M1, the number of distinct computational capabilities present**, out of the 77: (a) performed by at least one program ("by any program"); (b) performed by at least 10% of the program population ("common"; the same share as the growing list's rule); both over time, with the nine two-input and the 68 three-input tasks also counted apart. None of the 77 is performed by the starting program, so every one present is new.
- **M2, first appearance** of each task: the first sample at which it is performed by any program, and the first at which it is common.
- **M3, keeping**: of the tasks that were ever common, how many are common at update 50,000, and how many are performed by no program at 50,000; the number of times a task went from common to performed by no program.
- **M4, rising or levelling off**: the last update at which the count of common tasks reached a new highest value ("last new high"); the count is said to **level off** if its last new high is at or before update 40,000 (10,000 updates or more with no new high); also the rise over the last 10,000 updates.
- **M5, spread across seeds**: every number per seed, with the smallest, middle and largest of the three seeds.
- **M6, reuse**, if the time allows: at update 50,000, the most common distinct instruction sequence of each run is run alone in Avida's test processor (analysis mode, the 77 tasks listed, `nop-X` added as a do-nothing instruction as in S111 and S112); every single instruction is ablated (replaced by `nop-X`), and the **required instructions** for each task are those whose ablation stops that task while program replication continues (S112's definition). For each pair of tasks the program performs, the earlier (by M2 in that run, "by any program") and the later, the share of the later task's required instructions that are also required for the earlier is compared with the share expected if the later task's required instructions were placed at random among the program's instructions not required for replication. More sharing than that expectation is read as the later task's circuit **reusing** parts of the earlier's. S112's trace reader is not used: it reads only the nine two-input tasks.

Written by `tools/s113_count_new_capabilities_over_time.py` (M1 to M5) and `tools/s113_measure_reuse_of_task_circuits.py` (M6), to be written after this plan and committed before their results.

## 6. Expectations, and what would count against each

Claude's expectations, written before running. With three seeds per environment, "more" between two environments means: every seed of one above every seed of the other (smallest of one above largest of the other); "fewer" the reverse; otherwise **"not separated by three seeds"**.

- **E1, one hard task against graded.** The owner's remembered result (Lenski, Ofria, Pennock and Adami, 2003, from Claude's memory, not cited as a fact here) is that EQU arose only when simpler tasks were also rewarded. Expectation: EQU becomes common in fewer seeds of ONE HARD TASK ONLY than of FIXED GRADED, and later where it does. **Against**: EQU common in as many ONE HARD TASK ONLY seeds as FIXED GRADED seeds, at a middle first-common update no later.
- **E2, no rewards.** Expectation: NO TASK REWARDS ends with the fewest common capabilities of the six (at most 2 at update 50,000 in every seed). **Against**: any seed with 3 or more common at 50,000, or NO TASK REWARDS not fewer than FIXED GRADED.
- **E3, growing list against fixed graded.** Expectation: GROWING LIST ends with more common capabilities than FIXED GRADED (it rewards up to 77 tasks, FIXED GRADED nine). **Against**: not more.
- **E4, "a growing list learns more new capabilities than a fixed list"**, the proposition the owner's question points at, set against the FIXED LARGE LIST (the same 77 tasks, all rewarded from the start). Claude does **not** expect it: Claude expects the two to be not separated by three seeds at 50,000, the fixed large list reaching its counts earlier. **Against the proposition**: GROWING LIST not more than FIXED LARGE LIST in common capabilities at 50,000. **Against Claude's expectation**: either one more than the other.
- **E5, rising or levelling off.** Expectation: in FIXED GRADED and ONE HARD TASK ONLY the count of common capabilities levels off (last new high at or before 40,000) in every seed; in GROWING LIST and FIXED LARGE LIST it is still rising after 40,000 in at least two seeds. **Against**: the reverse in either pair.
- **E6, common tasks pay less.** Expectation: COMMON TASKS PAY LESS ends with at least as many common capabilities as FIXED GRADED, and more of the nine present at the end by any program; its programs spread over tasks rather than all performing all of them. **Against**: fewer common capabilities than FIXED GRADED.
- **E7, keeping.** Expectation: in the rewarding environments at least 90% of the tasks ever common are common at 50,000; in NO TASK REWARDS, tasks that were ever common are not kept. **Against**: under 90% kept in any rewarding environment's middle seed.
- **E8, reuse.** Expectation: the later task's required instructions share more with the earlier task's than the random expectation, in most pairs. **Against**: the average share no larger than the random expectation.

## 7. Seeds, length, compute budget and order

- **Seeds 1, 2 and 3** in each environment: 18 runs of 50,000 updates.
- **Budget**: 4 CPUs, at most 3 runs at once. A test piece with a full program population took 59 seconds; 50 pieces about 50 minutes; 18 runs, three at a time, about 5 to 6 hours. The runner (`tools/s113_run_the_avida_execution_environments.py`) takes the runs in the order seed 1 of all six environments, then seed 2, then seed 3, so that every environment has a run early; it is started detached, under an overall timeout of 10 hours. If the runs go slower than 8 hours in all, the third seeds of the slowest environments are cut short at a whole piece and this is recorded.
- **S111's three default-rate runs** (the same settings, nine tasks listed, run unbroken) are **not** used as FIXED GRADED seeds: the new runs list 77 tasks and are run in pieces, so they do not match S111's settings exactly. They are used as a check on the pieces: the FIXED GRADED runs' nine-task counts and EQU first appearance against S111's three unbroken runs (the same seeds 1 to 3, a different random sequence).
- Raw output stays in `s113/runs/` in the scratch space; the saved program population is kept every 5,000 updates. Into the repository go only configuration files, the exact commands, compact summaries and the scripts.

## 8. What will not be measured

- Tasks beyond the 77 logic tasks (arithmetic and others); other instruction sets, world sizes or instruction-change rates; a growing list made with Avida's cascades or on a fixed schedule; longer runs.
- Whether a capability is new to the program ancestry of a given program (only whether it is present in the program population).
- What the circuits compute beyond the ablation overlap (S112's trace reader is not extended).
- Any statement about biological evolution: these are digital programs on Avida's virtual CPU.

## 9. Departures

Every departure from this plan is recorded in `results/S113 Which execution environments learn - the runs/the exact commands.txt` and in the results file.
