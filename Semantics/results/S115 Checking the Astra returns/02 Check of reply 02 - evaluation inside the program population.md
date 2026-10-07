# Check of GPT 6 Astra's reply 02: evaluation inside the program population (log S115)

*Written by Claude (Opus 5.5) on 30 September 2026, decisions S66 to S68, by the one agent that does the whole S115 check. Reply checked: `tests/S115 Returns from GPT 6 Astra/02 Return - evaluation inside the program population.md`, answering brief 02 ("Evaluation inside the program population, with stock Avida features"). Source checked: Avida 2.14.0 at commit 47f13dad, in the scratchpad copy. Everything run here was a short test on the stock binary, one Avida process at a time, under `nice -n 19` with a timeout, while S113's runner (PID 2411) was still running. In the owner's Avida terms (S61); all entities are digital programs executing on Avida's virtual CPU.*

## 1. What the reply offers

1. A source inventory of every stock Avida route by which one Avida program can act on another (mating, deme competition, parasites, messages, reputation, donations, attacks and more), saying for each whether the choosing is done by the program's own instructions or by Avida's C++.
2. Its finding: in almost every route the comparison of candidates is written in C++; the one place a program's own instructions can carry a test is when it reads a number from a neighbour, does arithmetic on it, and then gives or withholds something.
3. Two small stock-Avida experiments built on that: a program reads a neighbour's sent number (or its displayed reputation), does five arithmetic instructions, and gives 10 energy units only if the result is zero; only those five instructions can change.
4. A timed encounter test with three arms (as built, recipients swapped after the arithmetic, giving switched off), and a replay of every living instruction sequence from saved program populations at update 1,000 and 5,000.
5. A complete generator (`make_experiments.py`), run locally by Astra in short versions; the 5,000-update runs are not run.

## 2. Its claims that the proposed runs depend on, checked against the source at 47f13dad

Paths under `avida-core/source/`.

| # | Claim | Holds? | File and function |
|---|---|---|---|
| 1 | The extra instructions (`send`, `receive`, `pose`, `get-neighbors-reputation`, `donate-energy-faced10`, `repro`, `one`, `zero`, `if-equ-0`) exist for the heads CPU and can be declared in an instruction-set file without new C++. | holds | `cpu/cHardwareCPU.cc`, instruction table (e.g. line 286 `donate-energy-faced10`); run here: all load and execute. |
| 2 | `pose` raises the program's reputation by one without any donation. | holds | `cpu/cHardwareCPU.cc` `cHardwareCPU::Inst_Pose` (line 10002). |
| 3 | With `ENERGY_SHARING_METHOD 0`, `donate-energy-faced10` gives nothing unless the neighbour has an open energy request (none here), so the "off" arm keeps the arithmetic but removes the giving. | holds | `cpu/cHardwareCPU.cc` `Inst_DonateEnergyFaced10` (5958-5976): gives only if `HasOpenEnergyRequest()` or method 1. Run here: off gives 1000 in every cell. |
| 4 | `NO_MUT_INSTS` keeps the protected instructions from being changed by `repro`'s copy changes. | holds, with a limit | `cpu/cHardwareCPU.cc` `Inst_Repro` (line 3391) reads the list; `main/cAvidaConfig.h` line 593 says the list is "NOT checked for all mutation types". The rig sets every other kind of instruction change to 0, so only the checked kind occurs. |
| 5 | `repro` replicates the program in one instruction; the program has no copy loop of its own. | holds | `cpu/cHardwareCPU.cc` `Inst_Repro` (3363-3425). This matters: program replication here is supplied by the instruction's meaning, not carried by instructions as in S111-S113. |
| 6 | The C++, not the program, compares candidates in mate choice, parasite infection and deme competition. | unchecked in detail | Named functions exist (`cBirthMatingTypeGlobalHandler`, `cPopulation::CompeteDemes`, `TestForParasiteInteraction`); not read line by line here. No proposed run depends on it. |
| 7 | Events need named arguments (`SavePopulation filename=...`, `InjectAll filename=...`). | holds | `actions/SaveLoadActions.cc`, `actions/PopulationActions.cc`; run here. |
| 8 | Cost: six 5,000-update runs about 0.6 CPU-hours. | holds in part | Measured here: a 100-update run took about 9 s wall on a loaded machine with 3,600 programs from update 0, so about 7.5 minutes per 5,000 updates, about 0.75 CPU-hours for six. |

Count: 6 hold (one with a limit), 1 in part, 0 do not hold, 1 unchecked (not needed by any run).

## 3. What it says it ran, and what was reproduced here

Scratch folder: `/tmp/claude-0/-home-user-ThreadSmith/8d9323da-c0ec-57ec-91fd-8f99ca99320a/scratchpad/s115/r02/`. The generator was extracted unchanged into `tools/s115/02/make_experiments.py` and run: `python3 make_experiments.py` (manifest `files.sha256.json`, sha256 `fc37c313…`). Each encounter was run as `nice -n 19 timeout 30 $B -c avida.cfg` in its folder, `$B` the stock binary.

| What | Reply | Here |
|---|---|---|
| Founder encounter, both mechanisms: energies, cells 0-3 | 990, 1010, 1000, 1000; IDs 0 1 2 3 | same, both mechanisms |
| Recipients swapped after the arithmetic | energies the same; IDs 0 3 2 1 (candidate 0 got the gift) | same, both mechanisms |
| Giving switched off | four energies of 1000 | same, both mechanisms |
| Candidate 1 replaced by candidate 2 (refusal) | no transfers | same (edited copy of the events file), both mechanisms |
| Last `dec` changed to `sub` | 1000, 1000, 990, 1010 (cue 0 accepted instead of 1) | same, both mechanisms |
| Two 100-update population runs | 3,600 programs each; 198 and 190 living sequences | same: 198 (received number) and 190 (reputation), 3,600 programs each |
| Replay of every living sequence against cues 0, 1, 2 | five response patterns: reject all, accept only 0, only 1, only 2, all | same five patterns in both banks |
| Swapped and off arms | zero cue contrast | zero (the reply's own checks in `summarize_bank.py` pass) |
| CPU time of a 100-update run | 14.4 and 13.2 s | about 9 s wall each here |

**Differences.** The generated evolution events save the population only every 1,000 updates, so a 100-update run as shipped leaves no snapshot at update 100; Astra's short runs must have used other events. Here one line `u 100 SavePopulation filename=detail` was added before `Exit` in a copy. Nothing else differed.

**One thing seen here that the reply does not report.** After only 100 updates (about 79 generations), the founder's rule ("accept only 1") was carried by 881 of 3,600 programs (received number) and 1,154 (reputation); "reject all" by 1,830 and 1,368. Giving costs the giver 10 energy units and brings it nothing, so the giving rule is likely to be lost. That is one run of each, 100 updates; it is no result, only a warning that the 5,000-update runs may show evaluation disappearing rather than changing.

## 4. Every run or measurement it proposes

Files: `/home/user/ThreadSmith/Semantics/tools/s115/02/make_experiments.py` (writes everything: configurations, instruction set, ancestors, candidates, `prepare_bank.py`, `summarize_bank.py`, `run_suite.py`) and `run_commands.sh`, both copied unchanged below a note.

**R02-a. Encounter tests (founder, refusal, changed arithmetic).**
- *What it tests in the owner's question:* whether a choice about another program can be carried by a program's own instructions, so that changing an instruction changes the choice. It is the "evaluation inside the programs" half of the S63 question, in its smallest form.
- *Stock or patch:* stock (extended heads instruction set, no C++).
- *Files:* `stock_avida_evaluation/<scalar|reputation>/<assay|shuffle|off>/`.
- *Seeds and length:* seed 101; 17 updates.
- *CPU:* under a second each. **Already run here; matched every reported number.**
- *What would count against it:* the gift not following the cue, or a changed arithmetic instruction not changing which cue is accepted.
- *Dependencies:* none. *Problems:* hand-made; shows the mechanism can carry a choice, not that one arises.

**R02-b. Six 5,000-update runs and the bank comparison.**
- *What it tests:* whether the programs' giving rules change under computational selection, and whether the rules at update 5,000 differ from those at 1,000 on the same fixed candidates.
- *Stock or patch:* stock.
- *Files:* `run_suite.py` (made by the generator): `python3 stock_avida_evaluation/run_suite.py --avida <stock binary> --output results_5000`.
- *Seeds and length:* 101, 102, 103 × two mechanisms; 5,000 updates; snapshots every 1,000; 36 bank assays.
- *CPU:* about 0.75 CPU-hours for the runs (measured rate above), plus under 0.1 for the assays; about 0.3 hours of wall time with three at once. Astra's optional 50,000-update extension: about 7.5 CPU-hours.
- *What would count against it, as the reply fixes it:* cue changes not changing decisions; changed arithmetic not changing the cue-to-decision map; support matched to cues not distinguishable from the swapped arm; giving or discrimination disappearing counts against "useful maintenance in this ecology"; a change in how many copies of each sequence alone does not count as learning.
- *Dependencies:* none on S113's results; it needs processors.
- *Problems found:*
  1. **The giving rule has no benefit to the giver.** Nothing pays back a program for choosing well; the likely outcome (already visible at 100 updates) is a drift to "reject all". That would count against useful maintenance, as the reply says, but it makes the run a weak test of the owner's question: it is set up so that evaluation has nothing to gain.
  2. **The swapped-arm contrast is zero by construction.** Each identity panel has a matching swapped panel, and averaging the pair cancels any cue effect. The check guards against bookkeeping errors; it cannot come out otherwise if the bookkeeping is right.
  3. **Very little can change.** Only five arithmetic instructions can change, among `inc`, `dec`, `add`, `sub`, `nand`; sensing, giving and replication are protected. The space of possible rules is small (five patterns were already reached in 100 updates).
  4. **Different from the owner's earlier runs.** Replication by one `repro` instruction, no division insertions or deletions, no task rewards, energy mode on. Nothing carries over to S111-S113 directly.
  5. The 100-update test runs need an extra save line (section 3).

## 5. Strengths and weaknesses

**Strengths.**
- Every reported encounter number and both 100-update counts were reproduced exactly.
- The source inventory is wide and careful, and separates choosing done by a program's instructions from choosing done by Avida's C++; it names controls that do not work as they seem (for example `PRED_PREY_SWITCH -1`).
- No source change; the runs are cheap (about one CPU-hour).
- The reply keeps its claims small: it says the experiments do not show knowledge creation, nor evaluation of a candidate's correctness.

**Weaknesses.**
- The choice made inside the programs is about a number a neighbour sends or displays, not about what the neighbour can compute; it is far from "judging another program's capability".
- Choosing well brings the chooser nothing, so the likely result is loss of the choice; the design does not ask what would make evaluation worth keeping.
- The swapped control is balanced by construction and cannot fail on real data.
- The rig (protected scaffold, `repro`, energy) is far from the owner's earlier Avida execution environments.
