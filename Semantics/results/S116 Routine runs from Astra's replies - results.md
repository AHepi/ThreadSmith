# S116 Routine runs from Astra's replies: results

*Log S116. Written 30 September 2026 by the one Opus 5.5 agent of log S116 (decisions S56, S68), after the runs, **before the GLM cross-examination**, against the plan committed before any measuring run: `results/S116 Routine runs from Astra's replies - how they will be tested, written before running.md` (732cf7f, 16:58 UTC). It carries out batches 2 and 3 of S115's plan of runs (`results/S115 Checking the Astra returns/00 What the eight replies offer, and a plan of runs.md`) and the continuation the S113 settlement proposed. In the owner's Avida terms (S61): an **Avida program** is one program of a **program population**; a **distinct instruction sequence** is one exact ordering of instructions; a **computational capability** is one task Avida can check, and a program has it when Avida credits it with **task performance**; **instruction ablation** is replacing one instruction by Avida's null instruction and running the program again; the **Avida execution environment** is what is rewarded, by how much and from what resource. All entities are digital programs executing on Avida's virtual CPU; nothing biological is involved; nothing that copies itself ran on the real machine. The numbers: `S116 Routine runs from Astra's replies - results.json` beside this file, written by `tools/s116_gather_the_results.py` from the summaries in the scratch space. The exact commands: `S116 Routine runs from Astra's replies - the runs/the exact commands.txt`. Observations only; nothing is settled (S28).*

---

## 0. In short

- **One yardstick for every S113 program population (batch 2).** Reply 01's probe runs every distinct instruction sequence on 8 fixed sets of three input numbers. Counting a task only when a program performs it **on all 8** (and still copies itself), the probe gives **lower counts than S113 in five of the 12 paying runs**, and in two it gives none common at 50,000 where S113 counted many: GROWING LIST seed 2 (0 against S113's 46) and FIXED LARGE LIST seed 1 (0 against 32). **The reason, found here: in those program populations, whether a program performs its tasks, and even whether it copies itself, depends on the input numbers.** In GROWING LIST seed 2 at 50,000, 2,377 of 3,489 programs copy themselves and perform NOT when the three numbers come in the order Avida's world always gives them; when the same numbers come in another order, only 62 to 370 do. Read on the two probe input sets that keep the world's order, the counts are S113's exactly (65 / 46 / 55, 32 / 41 / 13, 16 / 9 / 8, 7 / 8 / 8 common at 50,000). So S113's counts hold for the inputs the world gives, not for inputs in general, in some runs.
- **Capabilities were kept** (B2.2): of the tasks present at 25,000 and at 50,000, 87% to 99% were present at every save between in the paying environments' middle seeds. **Turnover without accumulation** (B2.1) appeared in one run only, FIXED LARGE LIST seed 1, and there it comes from the input dependence above.
- **Arithmetic nobody paid for came with replication, not with the environment** (B2.3): never-rewarded arithmetic tasks (such as `echo` and `sub`) were present at 50,000 in 7 to 11 per seed under NO TASK REWARDS, and not separated from it in any paying environment. **Against** the reading that the environment brings them.
- **K rose where tasks were paid** (B2.4, reply 05): the number of instructions whose ablation lowers Avida fitness under one fixed nine-task reward rose from 5,000 to 50,000 in all three seeds of FIXED GRADED, GROWING LIST and COMMON TASKS PAY LESS, and fell in all three of NO TASK REWARDS. **For**, with a limit: under a reward that pays for tasks, gaining a task adds instructions whose ablation lowers Avida fitness, so this K follows the task count and says little beyond it.
- **Reply 02's choice inside the programs did not disappear in 5,000 updates** (B3a): 9% to 20% of programs still gave to some cues and not others, "reject all" was the most common rule in every run (77% to 88%), and the founder's rule fell from all programs to 2% to 6%. **For by the letter** of the rule written before running; the rule was too weak to tell a choice kept because it was useful from one kept by instruction changes alone.
- **"Common tasks pay less" did not let a rare kind grow** (B3b): the two kinds taken from S113's COMMON TASKS PAY LESS seed 1 by the written rule were A (all nine paid tasks) and B (eight, without AND; no viable sequence had a task A lacks, so the rule's second choice was used). A took the whole world from every start, 1% to 99%, in all three placements, by update 1,500. **Against** (no growth from rare). The AND resource did run lower when A was common, but never low enough for AND to stop paying more than nothing.
- **FIXED LARGE LIST seed 2, continued from 50,000 to 75,000 in S113's own pieces, stopped rising** (E): 41 common capabilities by the test processor at every save from 50,000 to 75,000, and 41 by Avida's world count at all 100 samples after 50,000. **Levelled off.** With S113's reload caveats.
- **CPU time**: about 3.8 CPU-hours of Avida processes, under the 4 allowed.

## 1. What was run

| part | runs | Avida time | exit |
|---|---|---|---|
| Batch 3a, reply 02 | 2 mechanisms x seeds 101-103 x 5,000 updates; 36 bank assays (at 1,000 and 5,000, three arms each) | 3,003 s (the suite's own timing) | all passed the suite's checks |
| Batch 2, probe | 18 runs x 10 saves, profiles `core` (157 tasks) and `logic_high` (77 logic tasks on large inputs), analyze mode | 4,217 s | 36 of 36 "exit 0 missing 0" |
| Batch 2, K | 18 runs x 10 saves x the 100 most common sequences, analyze mode | at most about 1,040 s | 18 of 18 exit 0 |
| Continuation | 25 pieces of 1,000 updates (S113's runner, unchanged), then S113's test-processor function at 6 saves | 1,966 s + 19 s | 25 of 25 exit 0 |
| Batch 3b, competition | 5 starting shares x 3 placements x 2,000 updates | about 3,570 s | 15 of 15 exit 0 |

In all, about **13,800 s, 3.8 CPU-hours**. Stock Avida at 47f13dad; no patched build. Every Avida process at `nice -n 19` under a time limit, at most three at once. Nothing was written into S113's folder; the saved program populations were copied first.

## 2. Batch 2: the probe of every saved S113 program population

### 2.1 What the probe counts, against S113

Logic tasks common at 50,000 (seeds 1 / 2 / 3), by four readings:

| environment | S113 test processor (one input set, world order) | probe `core` (8 small inputs, all 8) | probe `logic_high` (8 large inputs, all 8) | probe, large inputs in the world's order (2 sets) |
|---|---|---|---|---|
| FIXED LIST, GRADED | 7 / 8 / 8 | 7 / 8 / 8 | 7 / 8 / 8 | 7 / 8 / 8 |
| ONE HARD TASK ONLY | 0 / 0 / 0 | 0 / 0 / 0 | 0 / 0 / 0 | 0 / 0 / 0 |
| NO TASK REWARDS | 0 / 0 / 0 | 0 / 0 / 0 | 0 / 0 / 0 | 0 / 0 / 0 |
| GROWING LIST | 65 / 46 / 55 | 51 / 0 / 55 | 65 / 0 / 55 | 65 / 46 / 55 |
| COMMON TASKS PAY LESS | 16 / 9 / 8 | 16 / 7 / 8 | 16 / 9 / 8 | 16 / 9 / 8 |
| FIXED LARGE LIST | 32 / 41 / 13 | 0 / 24 / 13 | 0 / 27 / 13 | 32 / 41 / 13 |

Present at 50,000 (probe `core` against S113's test processor): FIXED GRADED 20 / 25 / 15 against 22 / 31 / 23; GROWING LIST 73 / 27 / 69 against 74 / 65 / 72; COMMON TASKS PAY LESS 42 / 21 / 23 against 42 / 27 / 23; FIXED LARGE LIST 34 / 59 / 47 against 54 / 67 / 51; the two others equal (3 / 2 / 0).

**Why they differ (found after the first results; the last column and this paragraph are a departure, descriptive only).** The probe's input sets put the three numbers in shuffled orders; Avida's world always gives them in one order (the first number's top byte 15, the second 51, the third 85), and S113's test processor used that order. In some program populations the programs' behaviour depends on it:
- GROWING LIST seed 2 at 50,000 (large inputs): in the world's order, 2,377 and 2,381 of 3,489 programs copy themselves and perform NOT; in the six other orders, 62 to 370.
- FIXED LARGE LIST seed 1 at 50,000: on the small inputs only 26 to 169 of 3,484 programs copy themselves; on the large inputs about 1,900 to 2,160, except one order (137).
So in these runs, part of what S113 counted as capabilities, and even the programs' own copying, holds only for inputs arranged as the world arranges them. By the plan's reading (all 8), the probe's count is the stricter one; S113's is the count for the world the programs lived in. Both are reported; neither is ruled on.

By S113's three-seed rule, common logic tasks at 50,000: on the probe's `core` reading, **GROWING LIST against FIXED LARGE LIST is not separated** (51 / 0 / 55 against 0 / 24 / 13), nor GROWING against FIXED GRADED, nor FIXED LARGE against FIXED GRADED; FIXED GRADED is above NO TASK REWARDS. On the world-order reading, GROWING is above FIXED LARGE and FIXED GRADED, and FIXED LARGE above FIXED GRADED, as S113 found (E4 and Xc5 by the test processor). S113's "the growing list ended with the most" therefore holds for the world's inputs and not on the probe's stricter yardstick, because one growing run (seed 2) keeps its capabilities only for the world's order.

### 2.2 The readings of the plan

**B2.1, accumulation** (logic and never-rewarded arithmetic, probe `core`): turnover without accumulation (ever seen up by 3 or more over 25,000 to 50,000 while present falls) in **1 of 18 runs**: FIXED LARGE LIST seed 1 (ever seen 69 to 72, present 64 to 42), which is the input dependence of section 2.1 (at 50,000 its programs hardly copy themselves on small inputs). Elsewhere, where present fell (FIXED GRADED seed 1, 36 to 33), ever seen rose by fewer than 3; in the other runs present stayed or rose (for example COMMON TASKS PAY LESS 54 to 56, 29 to 35, 30 to 34; FIXED LARGE LIST seeds 2 and 3, 56 to 74 and 42 to 58). **For accumulation** in every environment except FIXED LARGE LIST, where one seed counts against by the rule, for the reason given.

**B2.2, kept at every save** (of the tasks present at 25,000 and 50,000, the share present at every save between; middle seed): FIXED GRADED 0.92, GROWING LIST 0.987, COMMON TASKS PAY LESS 0.875, FIXED LARGE LIST 0.945; all at least 0.8: **for**. "Present after a sampled gap" (present at both ends, missing between): 1 to 5 tasks per run.

**B2.3, never-rewarded arithmetic** (`echo`, `add`, `add3`, `sub`, every `math_*`): present at 50,000, NO TASK REWARDS 11 / 11 / 7; FIXED GRADED 13 / 11 / 14; GROWING LIST 12 / 8 / 12; COMMON TASKS PAY LESS 14 / 14 / 11; FIXED LARGE LIST 8 / 15 / 11. Common: NO TASK REWARDS 6 / 6 / 0, the paying environments 0 to 7. **Not separated from NO TASK REWARDS in any environment, by either count: against** the reading that the environment brings them. They come with programs that copy themselves (for example `echo`, returning an input unchanged).

**B2.4, K** (lethal plus detrimental single instruction ablations under S113's FIXED GRADED reward, weighted by programs, over the 100 most common sequences; 96 to 100 of the 100 viable except NO TASK REWARDS / ONE HARD TASK ONLY seed 3, 60 to 100):

| environment | K at 5,000 | K at 50,000 | rise, seeds 1 / 2 / 3 | rose in all three | rise against NO TASK REWARDS |
|---|---|---|---|---|---|
| FIXED LIST, GRADED | 56.5 / 59.0 / 54.0 | 60.8 / 63.5 / 72.8 | 4.2 / 4.5 / 18.8 | yes | more |
| GROWING LIST | 52.7 / 37.2 / 46.5 | 74.2 / 81.9 / 74.7 | 21.5 / 44.8 / 28.3 | yes | more |
| COMMON TASKS PAY LESS | 59.7 / 72.0 / 55.8 | 66.8 / 89.5 / 68.2 | 7.1 / 17.4 / 12.3 | yes | more |
| FIXED LARGE LIST | 62.6 / 37.0 / 49.4 | 89.7 / 74.5 / 45.4 | 27.1 / 37.5 / -4.0 | no | more |
| NO TASK REWARDS (= ONE HARD TASK ONLY) | 45.5 / 45.9 / 46.8 | 36.2 / 34.5 / 22.9 | -9.3 / -11.3 / -24.0 | no | - |

**For** in FIXED GRADED, GROWING LIST and COMMON TASKS PAY LESS. The limit reply 05 names applies: under a reward that pays for the nine two-input tasks, a program that performs them has instructions whose ablation removes a paid task, and so lowers its Avida fitness; K then rises with the task count by construction. Where nothing was paid, K fell (the programs became shorter or more robust to single ablations; not examined).

**B2.5, small against large inputs** (logic tasks at 50,000, `core` against `logic_high`): common counts equal or higher on large inputs in every paying run (GROWING seed 1: 51 small, 65 large); present counts on large inputs equal, higher, or one lower, except GROWING LIST seed 2 (27 small, 23 large, 15% lower). **Against by the letter** (one run more than 10% lower), a caution on S113's counts; the larger caution is the order of the inputs (section 2.1), which the plan did not foresee.

## 3. Batch 3a: reply 02, a choice inside the programs

Shares of programs by the cues they give energy to (active arm), at 5,000 (seeds 101 / 102 / 103):

| mechanism | reject all | discriminating | accept all | most common rule | founder's rule "accept only 1", at 1,000 then 5,000 |
|---|---|---|---|---|---|
| read a sent number | 0.88 / 0.77 / 0.84 | 0.09 / 0.19 / 0.11 | 0.03 / 0.04 / 0.06 | reject all, every seed | 0.049, 0.031 / 0.050, 0.059 / 0.029, 0.039 |
| read a displayed reputation | 0.83 / 0.76 / 0.86 | 0.16 / 0.20 / 0.09 | 0.01 / 0.04 / 0.05 | reject all, every seed | 0.044, 0.029 / 0.050, 0.052 / 0.061, 0.019 |

At 1,000 the discriminating share was 0.16 to 0.25. 3,600 programs, 401 to 447 distinct sequences in every bank. The swapped and off arms showed zero cue contrast everywhere (B3a.2: bookkeeping sound, as S115 expected by construction).

**B3a.1: for, by the letter** (discriminating at least 10% in two of three seeds of each mechanism; the most common rule differs from the founder's). **Against did not occur** (reject all never reached 90%). But the rule was weaker than it looked: five of the program's instructions can change, so every copy has a few per cent chance of a new rule, and a 9% to 20% share of discriminating programs can be kept by that alone. Nothing here shows the choice kept because it served the chooser; the design gives the chooser nothing for choosing well (S115 check 02).

## 4. Batch 3b: the rare-kind competition

**The two kinds, by the rule written before running** (COMMON TASKS PAY LESS seed 1 at 50,000, probe `core`, all 8 inputs, viable): A, the most common viable sequence (14 programs, 93 instructions), performs all nine paid tasks; no viable sequence performs a paid task A lacks, so B is the most common with a different set: B (8 programs, 93 instructions) performs eight, all but AND (29 viable sequences were ranked before it). In the test CPU without resources, B copies itself slightly faster (545 against 577 instruction executions).

**Share of A at update 2,000** (and at 500): from 1%: 1.0 / 1.0 / 1.0 (0.96, 0.95, 0.92 at 500); from 10%, 50%, 90% and 99%: 1.0 in every placement (0.98 to 1.0 at 500). No other sequence appeared (instruction changes off). **B3b.1: against, no growth from rare**: B, rare or common, was lost in every run.

What happened to the resource: with A at 99%, the AND resource stayed between about 140 and 240 (full pay needs 400), so AND still paid A about 2^(2 x 0.0025 x level) = 1.6 to 2.3 times, against B's 5% faster copying. In this environment a common task pays less but never nothing, so a kind that lacks a task cannot gain from others performing it; it could gain only from a task of its own that the common kind lacks, and no such pair existed in this program population.

## 5. The continuation: FIXED LARGE LIST seed 2 from 50,000 to 75,000

| update | 50,000 (the copy) | 55,000 | 60,000 | 65,000 | 70,000 | 75,000 |
|---|---|---|---|---|---|---|
| test processor, common | 41 | 41 | 41 | 41 | 41 | 41 |
| test processor, present | 67 | 66 | 67 | 66 | 67 | 67 |
| distinct sequences | 3,221 | 3,210 | 3,220 | 3,227 | 3,211 | 3,204 |

The copy at 50,000 gives S113's 41 (the check). Avida's world count: 41 common at all 100 samples from 50,250 to 75,000 (and at 49,250 to 50,000); its last new high stays S113's 48,250. **Levelled off** by the plan's rule (count at 75,000 within 1 of 41, no new high of either count after 60,000). The run that was still rising at 50,000 rose no further in 25,000 updates, while about 3,200 distinct instruction sequences kept being replaced.

**Caveats (S114 audit), said plainly**: the continuation was made in pieces with a reload every 1,000 updates, like S113's run; FIXED LARGE LIST was never audited against an unbroken run; one seed only; the world count can fall after a reload where processor time is uneven (it did not here: 41 at every sample).

## 6. Departures from the plan

1. **No save line was added to reply 02's runs** (the task named one): a test before the plan showed the save at the last update is already made; check 02's added line was for a 100-update test.
2. **Two descriptive readings were added to the probe's summary after the first results** (not in the plan, no verdict drawn from them): logic tasks credited on at least one of the 8 small inputs, and logic tasks on the two `logic_high` input sets that keep the world's order. The second explains the difference from S113 (section 2.1). Both are marked in the `.json` as added.
3. **10 saves per run, not 11** (S113 kept no save at update 0; the starting program is the same everywhere and performs no task).
4. **The competition's B was chosen by the rule's second branch** (no viable sequence had a paid task A lacks); as written before running.
5. **CPU**: the probe took about 1.2 CPU-hours (planned about 1), the competition about 1.0 (planned about 1); the whole job about 3.8, within the 4 allowed. Nothing was cut.

## 7. What was not tested

Ancestry and reuse maps across S113's pieces; reply 01's other 16 profiles; MODES, shadow runs and historical instruction use; first appearance finer than 5,000 updates; K under any other reference reward; other pairs of kinds, other seeds, instruction changes on, or longer competitions; whether reply 02's choice would last if choosing well paid; the continuation beyond 75,000, other runs continued, or an unbroken run; why programs in some runs depend on the order of their input numbers (which instructions do it was not traced).

## 8. What the results say about the owner's question

The owner asked (S63) "what kind of execution environment can use these machines to progressively learn how to do new things". Observations only, settling nothing (S28):

- **What S113's program populations learned was kept**, and at a fixed list of 77 tasks the one run still rising at 50,000 rose no further in 25,000 more updates. In the environments tried, learning filled part of the designer's list and then stopped.
- **Some of what was learned is tied to how the environment presents its problems.** In two runs most programs perform their tasks, or copy themselves, only when the three numbers come as the world always gives them (in its order, GROWING LIST seed 2; of its size, FIXED LARGE LIST seed 1). The environment's regularities became part of what the programs rely on; a program population can look capable in its own world and not beyond it.
- **What the environment pays for is what it adds.** Arithmetic nobody paid for was as common with no reward at all; instructions the programs depend on rose only where tasks were paid.
- **Making a common task pay less did not, in the one pair tested, let a rare kind grow**: a common task still paid something, so the kind lacking it lost. An environment in which a problem stops paying altogether when solved by many, or which pays for problems no program has yet solved, was not tried.
- **A choice made inside the programs, with nothing gained by choosing well, did not vanish in 5,000 updates, but nothing showed it was kept for its use.**

## 9. Unsure

- The probe's 8 input sets are one draw; two of them keep the world's order. The world-order reading rests on those two.
- Why growing seed 2 and fixed large seed 1 depend on input order is not traced to instructions; the explanation offered (programs using the numbers in their control of copying) is a guess.
- K's 100 most common sequences carry a varying share of the programs (not reported per save); K under one reward rule only.
- The competition's CPU time is from the runs' own clocks (about 238 s each); K's is an upper bound from wall time.
- One seed for the continuation; one pair and 2,000 updates for the competition.
