# S126 The closing knock-out test: how it will be tested, written before running

*Log S126, decisions S76, S80 and S81. Written 2 October 2026 by the one Opus 5.5 agent of log S126 (S56, S68), **before any arm is run**, and committed before the runs start. Before this plan only these were done: the saved program populations' task counts and resource levels at the save were read (they are not intervention results; they are what the selection rule below reads), and one rig check in Avida's analysis mode showed that a do-nothing instruction (nop-X) can be added to the instruction set with mutation weight 0 and that a program with it at its first site is read and run (it fails replication there, as expected). No arm has been prepared or run. In the owner's Avida terms (S61). Observations only; nothing is settled (S28).*

## 1. The question, and the reading of "Avida itself" assumed

The owner (S76): "The definition of knowledge says it must has a causal affect on its surroundings. Not just other little programs, but Avida itself. Has that been demonstrated yet?" After S80 and S81 this is the one cheap closing run of the Avida line; no new execution environment is designed.

**The test.** Does a learned computational capability's effect on Avida's own state **disappear** when that capability is removed from the program population (copying kept), and **return** when it is restored?

**Assumed, and left to the owner.** "Avida itself" is read here as **Avida's state** (here, the execution environment's resource stores), not its rules. The route by which task performance draws a store down is one Avida's designers wrote (`cEnvironment.cc`, finite resources consumed by reactions; checked in S125, check of reply 03, claim 1). So a positive result shows a capability-specific effect on the execution environment's state through a designed route; it does not show a program changing Avida's rules, and it is not the strict E3 of S123 (no designed route at all), which reply 03 argued cannot occur in a closed simulation.

## 2. The material and the selection rule (S125's rule, adopted unchanged)

S125 (`05 The refined hypothesis.md`, 7.2) fixed the rule before any intervention: **S113's COMMON TASKS PAY LESS, seeds 1 and 2, the saved program population at 50,000 updates (piece 49's save), with its resource levels; q = the task performed by the most programs at that save (Avida's `tasks.dat` at that update), ties to the higher reward value.** It is applied separately to each population, so each has its own q. Read from the save:

| Population | Programs | Distinct instruction sequences | q by the rule | Programs credited with q | q's store at the save | Full store (no use) |
|---|---|---|---|---|---|---|
| seed 1 | 3,549 | 2,441 | **ORN** (or-not, reward level 2) | 3,382 | 250.9 | 10,000 |
| seed 2 | 3,551 | 3,016 | **NOT** (reward level 1) | 3,237 | 319.1 | 10,000 |

"Clearly drawn down" is taken as below 10% of the full store (1,000): both qualify (2.5% and 3.2%). In this execution environment every one of the nine two-input tasks draws on its own store: inflow 100 per update, 1% outflow, so an unused store fills toward 10,000 with a time constant of about 100 updates; each performance takes 0.25% of what is left (at most 1.0), and pay is 2 to the power of (level × amount taken).

## 3. The cuts, and how they are validated

**The removal.** A cut site's instruction is replaced by **nop-X**, an instruction that does nothing and is no label (as in S111 and S112), added as a 27th instruction with **mutation weight 0** (`redundancy=0`), so that copying errors never create it and the draw of random instructions is the same as with the 26 of S113. The same 27-instruction set is used in every arm. **Rig check** (before any arm): the unchanged population continued for 200 updates with the 26- and the 27-instruction set, same seed, must give identical data files; if not, this is a departure, reported, and all arms still use the 27-set.

**The probe.** Avida's analysis mode (its test processor: each program alone, no variation), with a probe execution environment that lists the nine tasks at **pay 0** (so pay cannot stand in for a capability). A **finite panel of four input triples**: Avida's fixed test inputs and three more drawn with a fixed seed in Avida's input form (top byte 0x0f, 0x33, 0x55; low 24 bits random). Read for each program and each input: copies (Avida's `viable`), which of the nine tasks are done, gestation time.

**Mapping.** Every living distinct instruction sequence in the save is probed. **A q-sequence** is one that does q on at least one panel input. Every q-sequence is cut, however rare.

**The cut of a q-sequence.** The smallest set of nop-X replacements such that, on **every** panel input: q is not done; the program still copies; every other task is done exactly as before. Search: all single sites; if none, all pairs of sites whose single replacement keeps copying. If no set of size 1 or 2 meets all three, then the smallest set of size 1 or 2 that stops q and keeps copying while losing the fewest other task-and-input instances is taken, and its collateral losses are recorded (organisms affected, tasks lost). If none of size 1 or 2 stops q while copying, the sequence is left uncut, and the organisms so left are reported (a preparation shortfall; residual q in the arm will show it). Among several equally small cuts, the one changing gestation time least is taken, then the lowest sites.

**The sham of a q-sequence.** The same number of nop-X replacements at sites that **change nothing** on the panel: copying, all nine tasks on every input, and gestation time all identical to the original. Drawn with a fixed seed among single sites that change nothing (cut sites excluded); a draw of two is kept only if the pair together also changes nothing (up to 50 draws). A q-sequence with no such set gets no sham, reported.

**Programs that are not q-sequences** are left exactly as saved in every arm.

## 4. The arms

Every arm starts from **the same reload**: Avida loads the saved program population (S113's runner did the same at every piece; it restores each program's cell, merit and place in its current copy) into the execution environment with **the stores set to their levels at the save** (`initial=`, as S113's runner carried them). **S114 found that a reload loses working state** (registers, partly done copies' processor state, task counters), so every arm is a continuation *after reconstruction*, all arms treated alike. Settings are S113's runner's (S111's `avida.cfg`, `COPY_MUT_PROB 0.0075`, the nine tasks at levels 1 to 5 with their stores, the other 68 tasks listed at pay 0, `requisite:max_count=1`), except the 27th instruction and the finer recording below; a continuation is one unbroken Avida process (no 1,000-update pieces).

| Arm | Program population at the reload | Length |
|---|---|---|
| **L0** original | the save, passed through the same editing script with no replacement | 3,000 updates |
| **Lq** cut | every q-sequence cut | 3,000 updates; its program population also saved at 1,000 updates |
| **Ls** sham | every q-sequence given its sham | 3,000 updates |
| **Lr** restored as handled | Lq's file with every removed instruction put back by the same script (must be byte-identical to L0's file) | 1,000 updates |
| **Lq-then-restored** | Lq's program population saved at 1,000 updates, with every nop-X put back to the instruction it replaced (below), reloaded with Lq's store levels at that update | 2,000 updates |
| **Lq-then-reloaded** | the same save of Lq, reloaded unchanged, the same handling | 2,000 updates |

**Seeds.** Two per arm and population: 50 and 150 added to 1,000 × the S113 seed (1050 and 1150; 2050 and 2150); 1050 and 2050 are the seeds S113's runner would have given the next piece. All arms of a population use the same two seeds.

**Why restoration is done twice.** Lr as specified (the removed instructions put back, handled the same way) gives a file identical to L0's and, Avida being deterministic, the same continuation: it checks the handling, not the capability. The restoration that can fail is **Lq-then-restored**: after the store has recovered under the cut, the removed instructions are put back into the programs that carry them. Since nop-X is never made by copying errors, every nop-X in Lq's later population descends from a cut site; each is put back to the instruction that the cut site with the best-matching surrounding (ten instructions on each side) had held; ambiguous matches are counted and reported. The restored sequences are then probed (share that do q on the panel). Its control is **Lq-then-reloaded**, because a reload itself disturbs (S114).

**Replay arms (R0, Rq of reply 03) are not run**: they separate the feedback route from the direct effect, which the owner's question does not need, and exact clamping of stores needs new code (reply 03, L115). Not tested.

**Budget.** About 3,000 × 6 × 2 + 1,000 × 4 + 2,000 × 8 = 56,000 updates; at the rate of S113's last pieces of these two runs (about 90 to 120 seconds per 1,000 updates, three at once), about 1.6 to 1.9 CPU-hours, plus the probes (estimated under 0.3). Never over 3 CPU-hours; at most 3 Avida processes at once, each under `timeout` and `nice -n 19`. If the measured rate would pass 2.6 CPU-hours, the second seed of Lq-then-restored and Lq-then-reloaded is dropped first, and this is recorded.

## 5. What is recorded

Every update: every store (`PrintResourceData`) and the number of times each task was **executed that update** (`PrintTasksExeData`: new executions only, so the carry-over of task counters and merit from before the reload does not count). Every 10 updates: `PrintTasksData` (programs credited with each task in their last copy) and `PrintCountData` (programs, copying). Every 100: `PrintAverageData`. Saves at 1,000 and at the end.

**Carry-over.** Loaded programs keep their saved merit (the same in every arm, since merit fields are not edited) until their next copy; Avida's per-program task records start empty after a load. So the store responds to new executions from the first update; merit effects of the cut appear over about one copy.

## 6. The measures and what counts, fixed now

**Window.** Updates 201 to 1,000 after a reload (after about two time constants of the store). **The main number**: q's store, mean over the window, per arm and seed. The whole trajectory is reported.

**The L0 band.** For each population, from L0's two seeds: lowest and highest window mean, widened by T = the larger of twice their difference and 25% of their average. "Matches L0" means within the band. The same band is computed for each of the other eight stores.

**For the hypothesis (the effect is the capability's, it disappears and returns), in each population:**
1. **Cut works**: in Lq, q executions in updates 1 to 100 are under 5% of L0's (mean of seeds); copying goes on (programs at update 1,000 at least 90% of L0's).
2. **Disappears**: Lq's q store, both seeds, window mean at least 5,000 (half full) and above the L0 band.
3. **Specific**: Lq's other eight stores match L0 (allowance: at most one of the eight outside the band in a seed, reported).
4. **Not generic damage**: Ls's q store matches L0, both seeds.
5. **Handled alike**: Lr's file is byte-identical to L0's and its 1,000 updates give the same numbers as L0's, same seed.
6. **Returns**: Lq-then-restored's q store, window mean (its updates 201 to 1,000) below 1,000 (back to "clearly drawn down") in both seeds, while Lq-then-reloaded's stays at least 5,000 (unless q has re-evolved in that population, which is then reported and read from the execution counts).

**Against:** q still executed in Lq at more than 5% of L0's after validated cuts (the dependence fails, or the panel missed sequences); Lq's q store within the sham's or L0's range (no capability-specific effect); Ls's q store out of L0's band (the effect is generic damage, not the capability); Lq-then-restored not drawing the store back down while its restored programs do q on the panel.

**Neither (a preparation failure, not a result):** no cut that keeps copying for sequences carrying more than 5% of q's programs; the population collapsing in Lq or Ls.

**A verdict per population** (for, against, mixed, or neither), and one overall: **for** only if both populations meet 1 to 6.

**Re-evolution.** If q reappears in Lq (executions rising again), its timing is reported, and its store's fall after that is not counted against criterion 2 if it comes after the window.

## 7. What is not tested

- Whether programs change Avida's **rules** (its C++ or the execution environment's settings): they cannot in this set-up, and this test does not try.
- The replay controls (feedback route against direct effect); exact clamping of stores.
- Where the knowledge sits (H1' against H2' of S125): an outward effect does not split them (reply 03, L119).
- Learning from outside data; construction; explanation.
- Uninterrupted state: every arm is a continuation after a reload.
- Inputs outside the four-input panel (residual q in Lq would show what the panel missed).
- Any population other than the two chosen, and any task other than the q chosen in each.

## 8. Files

Scripts in `tools/s126_*.py`, each with a plain note at the top. Raw output in the scratch space (`s126/`), never in git; S113's scratch folder is only read (the two saves and their resource files are copied). Results: `results/S126 The closing knock-out test - results.md` and `.json`; the plain file `plain words/126 Does the programs' knowledge change Avida itself, in plain words.md`.
