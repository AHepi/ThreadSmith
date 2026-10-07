# S116 Routine runs from Astra's replies: how they will be tested, written before running

*Log S116. Written 30 September 2026 by the one Opus 5.5 agent of log S116 (decisions S56 and S68: one agent for the whole job, no subagent or workflow), **before any measuring run**, and committed before the runs start. It carries out the routine part of S115's plan (`results/S115 Checking the Astra returns/00 What the eight replies offer, and a plan of runs.md`, section 3, batches 2 and 3) and one run proposed by the S113 settlement (`results/S113 Which execution environments learn - the GLM cross-examination, settled.md`, section 5). No new owner words since S68. In the owner's Avida terms (S61, `records/Semantics - Avida terms, given by the owner.md`): an **Avida program** is one program of a **program population**; a **distinct instruction sequence** is one exact ordering of instructions, carried by one or more programs; a **computational capability** is one task Avida can check (a logic or arithmetic operation), and a program has it when Avida credits it with **task performance**; the **Avida execution environment** is what is rewarded, by how much and from what resource. All entities are digital programs executing on Avida's virtual CPU; nothing biological is involved and nothing that copies itself runs on the real machine. Observations only; nothing is settled (S28).*

**One mechanics test was made before this file**, to know what to write: a 1,000-update copy of reply 02's run in a 10 x 10 world (about 1 second) showed that reply 02's events already save the program population at the last update (`detail-1000.spop` was written). So the "one added save line" of check 02 (needed there for a 100-update test, whose last update is not a multiple of 1,000) is **not needed** for the 5,000-update runs; none is added. Nothing else was run.

**The owner's question** (S63): "The execution environment is an important clue. Looking inside the machines is the wrong direction. The question is, what kind of execution environment can use these machines to progressively learn how to do new things..."

---

## 0. What carries into every comparison with S113

From the S114 restart audit (`results/S114 Restart audit - results.md`) and the S113 settlement:
- **COMMON TASKS PAY LESS may be lowered by S113's pieces** (fewer births and fewer common capabilities just after a reload, all three seeds, below the audit's thresholds). Any comparison below that turns on one or two capabilities between it and another environment is read with that caution.
- **Generations in S113's data are not used** (a reload resets them). None is used here.
- **Three seeds are read through their spread**: "more" only if every seed of one environment is above every seed of the other (S113's rule); otherwise "not separated by three seeds".
- **FIXED LARGE LIST and GROWING LIST were not audited** against unbroken runs; the extension (section 4) inherits every reload caveat.

Everything S113 saved is read from copies: the 180 saved program populations (18 runs x the saves at 5,000, 10,000, ..., 50,000; S113 kept no save at update 0) are copied into the scratch space before any probe; nothing is written into S113's folder. **Departure from S115's plan already known**: the plan says "11 saves" per run; there are 10 (the starting program at update 0, Avida's default ancestor, is the same in every run and performs no task).

## 1. Batch 2: probing every saved S113 program population (replies 01, 05, 08)

**What is run.** Reply 01's probe battery (`tools/s115/01/probe_task_audit.py`, unchanged), analyze mode only, with the profiles `core` and `logic_high`, on each run's 10 saved program populations: every living distinct instruction sequence is run alone on Avida's test CPU with 8 fixed input triples (the script's own seed 20260930), every checkable task listed at reward 0. Then reply 01's summariser (`summarize_probes.py`, unchanged) with a reward history for each run made from S113's own environment files and the GROWING LIST's recorded additions (never-rewarded tasks marked "never"). The Avida binary is called through a small wrapper that adds `nice -n 19` and a one-hour time limit; nothing in the scripts changes. Estimated cost: about 1 CPU-hour.

**Definitions used (fixed now).** A program **performs** a task on the probe when its sequence is credited with the task on **all 8** input triples and is viable (the summariser's `viable_all`). **Present**: at least one program; **common**: at least 10% of the programs (as S113). **Logic capabilities**: S113's 77 logic tasks. **Never-rewarded arithmetic**: `echo`, `add`, `add3`, `sub` and every `math_*` task (canonical names only, aliases not counted twice); no S113 environment ever rewarded any of them. `fib_*` (a fixed number, not a function of the inputs) and `dontcare` are left out of both counts. **Ever seen** (a run, at a saved update): tasks present at that save or any earlier one. **Kept continuously**: tasks present at every save from a given save to a later one (the summariser's `every_saved_snapshot`). `logic_high` is the same 77 logic tasks on large inputs (above 2^24); it is summarised by an S116 script with the same rule, since the summariser reads `core` only.

**K (reply 05).** For each saved program population, its 100 most common distinct instruction sequences (by the number of programs carrying them; all if fewer) are loaded, recalculated, kept if viable, and Avida's `ANALYZE_KNOCKOUTS` (single instruction ablation: each instruction in turn replaced by Avida's null instruction) is run under one fixed reference environment: S113's FIXED GRADED environment (the nine two-input tasks at their S111 rewards 1 to 5, the other 68 logic tasks listed at 0, no resources). **K of a sequence** = its lethal plus detrimental ablations (instructions whose ablation lowers Avida fitness). Reported per save: the mean weighted by programs, the median and the maximum over the viable sequences, and how many of the 100 were viable. Estimated cost: about 0.3 CPU-hours.

**Readings and what would count for and against each** (from S115's plan table, sharpened):

| reading | measure | counts for | counts against |
|---|---|---|---|
| B2.1 Capabilities accumulate (they are added and kept, not only replaced) | per run: ever seen, present, and kept continuously (logic plus arithmetic), 25,000 to 50,000 | ever seen and present both rise, or present stays within 1 of ever seen | **turnover without accumulation**: ever seen rises by 3 or more over 25,000 to 50,000 while present at 50,000 is below present at 25,000 (the plan's "ever seen rising while the kept set falls"); counted per run, then per environment by three seeds |
| B2.2 Kept, not lost and found again | per run: of the tasks present at 25,000, how many are present at 50,000 (endpoint), how many at every save between (continuous); "present after a sampled gap" (present at both ends, missing between) | continuous at least 80% of endpoint in the paying environments' middle seed | gaps common: in any paying environment's middle seed, more than a fifth of the endpoint-kept tasks were missing at some save between |
| B2.3 The environment brings the never-rewarded capabilities, not replication alone | never-rewarded arithmetic present and common at 50,000, and ever seen, per environment | paying environments above NO TASK REWARDS by the three-seed rule | **NO TASK REWARDS not below** a paying environment by the three-seed rule (then these capabilities come with replication itself, not with what the environment pays) |
| B2.4 Building up of structure (reply 05's K) | weighted mean K at 5,000 and at 50,000, per run | K higher at 50,000 than at 5,000 in all three seeds of a paying environment, and that rise larger than NO TASK REWARDS's in every seed | **no rise in K anywhere** (no paying environment rises in all three seeds); or paying environments' rise not above NO TASK REWARDS's (then K follows replication, not the paid tasks) |
| B2.5 S113's counts do not depend on small inputs | logic capabilities present and common under `core` and under `logic_high`, at 50,000 | the two within 10% of the `core` count in every paying run | a paying run where `logic_high` is more than 10% below `core`: part of S113's "capabilities" hold only for small numbers (a caution on S113's counts, not a verdict on the owner's question) |

The probe's counts are also set beside S113's own test-processor counts (S113 used one set of inputs, the probe 8 and "all 8"); differences are reported, not ruled on. The ordering of environments at 50,000 (common logic capabilities by the probe) is reported by the three-seed rule.

**Not tested in batch 2.** Ancestry and reuse maps (reply 01's M3: S113's pieces break the ancestry record); dynamics and activity statistics (M4, with no neutral comparison); reply 01's other 16 profiles; MODES, shadow runs, historical instruction use (not in stock saves); first appearance finer than 5,000 updates; any input other than the probe's 8 triples.

## 2. Batch 3a: reply 02's evaluation inside the programs

**What is run.** Reply 02's generator (`tools/s115/02/make_experiments.py`, unchanged; its manifest must hash to `fc37c313…`, as in S115) and its `run_suite.py`, unchanged: two mechanisms (a program reads a neighbour's sent number, "scalar", or its displayed reputation, "reputation"; five arithmetic instructions decide; it gives 10 energy units or not) x seeds 101, 102, 103 x 5,000 updates in a 60 x 60 world, three at once; then its 36 bank assays (every living sequence saved at 1,000 and at 5,000, each run against candidates showing cues 0, 1 and 2, in the arms "active", "swapped after the arithmetic" and "giving off") and `summarize_bank.py`. The Avida binary through the same wrapper. Estimated cost: about 0.8 CPU-hours.

**Measures (S116 script, after the suite).** For each sequence at each bank, its response pattern: which of cues 0, 1, 2 it gives to (from the active arm's grants in the three pairs). Weighted by programs: the share that **gives to no cue** ("reject all"), the share that **discriminates** (gives to some cues and not others), the share that **gives to all**, and the most common pattern.

| reading | counts for | counts against |
|---|---|---|
| B3a.1 A choice made by the programs' own instructions changes under computational selection **and lasts** | at 5,000, discriminating programs at least 10% in at least two of three seeds of a mechanism, and the most common pattern at 5,000 different from the founder's ("accept only 1") or from 1,000's | **giving and discrimination disappearing** (S115's expected outcome): at 5,000, reject-all at least 90% and discriminating under 5% in every seed of a mechanism |
| B3a.2 Bookkeeping sound | the swapped and off arms show zero cue contrast (reply's own checks pass) | any nonzero contrast in those arms (S115: zero by construction, so this checks bookkeeping only) |

**Not tested.** Whether evaluation would last if choosing well paid the chooser (nothing in the design pays it); anything about S113's environments (a different rig: replication by one `repro` instruction, protected scaffold, energy, no task rewards); Astra's optional 50,000-update extension.

## 3. Batch 3b: reply 05's rare-kind competition under COMMON TASKS PAY LESS

**The mechanism S113's expectation E6 relies on**: when a task is common its resource runs low and it pays less, so a kind of program doing tasks few others do is paid more and should grow when rare.

**Which two kinds (rule fixed now).** From S113's COMMON TASKS PAY LESS **seed 1** (the seed with the most tasks, 17 common) at update 50,000, using batch 2's probe (`core`, all 8 inputs, viable): **A** = the most common viable distinct instruction sequence; **B** = the most common viable sequence whose set of the nine paid two-input tasks includes at least one that A lacks (if none, the most common with a different set of the nine). Both must be viable in the test CPU (Avida's own check that the program completes a copy of itself); with every instruction change off, any sequence other than A and B appearing in the runs is counted and reported (it would mean a program does not copy itself exactly).

**What is run.** A new S116 script (`tools/s116_compete_a_rare_and_a_common_kind.py`) builds, for each run, S113's COMMON TASKS PAY LESS environment with S113's own function (`environment_text`, imported unchanged), every resource starting at the level S113's seed 1 had at update 50,000 (as S113's runner carries it), S111's `avida.cfg` with **every instruction change off** (copy error 0, one-instruction insertion and deletion 0), and the full 60 x 60 world filled at update 0: A in a share s of the 3,600 cells and B in the rest, cells chosen at random by a placement seed. s = 1%, 10%, 50%, 90%, 99%; placements 1, 2, 3 (Avida seed 116000 + 10 x placement + share index). 15 runs x 2,000 updates, continuous (no reload), three at once. Saved every 500 updates; the share of A counted from the saved populations. Estimated cost: about 1 CPU-hour (above S115's 0.6: late S113 program populations run slower); if the first run shows more than 1.5 CPU-hours in all, the 1% and 99% shares run with one placement only and the rest is recorded as proposed.

| reading | counts for | counts against |
|---|---|---|
| B3b.1 Common tasks paying less favours the rare kind (both kinds grow when rare) | A's share rises from 1% and from 10% **and** falls from 90% and from 99%, in all three placements | **no growth from rare**: A's share falls from 1% in all three placements, or rises from 99% in all three (then one kind wins from every start, and the resources do not hold this pair together) |
| B3b.2 Unclear | anything else (drift at 1% can remove 36 programs by chance) | |

**Not tested.** Other pairs of kinds, other seeds; whether it holds with instruction changes on (the S113 runs); whether the pieces changed it; a mixture of more than two kinds. A positive result would support E6's mechanism for this pair only; it would not explain why E6 was not separated in S113.

## 4. The extension: FIXED LARGE LIST seed 2 from 50,000 to 75,000

**What is run.** S113's own runner functions (`tools/s113_run_the_avida_execution_environments.py`, imported, **unchanged**: `run_one('fixed_large', 2, pieces=75, out=<S116 folder>)`) on a copy of that run's `state.json` and its last piece's folder (with the program population saved at 50,000). So 25 more pieces of 1,000 updates, each a new Avida process loading the last saved program population, Avida seeds 2,050 to 2,074, a 900-second limit per piece, exactly as S113 ran it; the whole runner under `nice -n 19`. Estimated cost: about 0.6 CPU-hours.

**Counted as S113 did**: (i) Avida's world count (`tasks.dat` and `count.dat` at every 250 updates; common = at least 10% of programs) with the counting code of S113's runner; (ii) the test-processor count at every 5,000 (55,000 to 75,000, and 50,000 again as a check that the copy starts where S113 ended: it must give 41 common) with S113's own measuring function (`one_snapshot`, imported unchanged, its working folder pointed into the S116 scratch space).

| reading | counts for | counts against |
|---|---|---|
| E.1 Its count keeps rising (the run S113 found still rising: 28 at 40,000, 37 at 45,000, 41 at 50,000) | test-processor common count at 75,000 at least 44 (3 or more above 50,000) **and** a new high of the world count at or after 65,000 | **levelled off**: test-processor count at 75,000 within 1 of 41 and no new high of either count after 60,000 |
| E.2 In between | anything else, reported as "rising slowly or unclear" | |

**Reload caveats (S114 audit), said plainly**: this run is made in pieces with a reload every 1,000 updates, like S113's; FIXED LARGE LIST was never audited against an unbroken run; the world count can fall after a reload where processor time is very uneven (the fault found in S113's seed 3), so the test-processor count is the one read first; one seed only.

**Not tested.** Whether any other run would rise if continued; longer than 75,000; an unbroken run.

## 5. How it all bears on the owner's question

- Batch 2 asks, of every S113 environment with one fixed yardstick, whether new capabilities were added and kept (accumulation, the "progressively"), whether capabilities nobody paid for came with the environment or with replication alone, and whether programs came to rely on more of their instructions.
- Batch 3a asks whether an environment where the choosing is inside the programs keeps a choice at all.
- Batch 3b tests the one mechanism by which "common tasks pay less" was expected to widen what a program population does.
- The extension asks whether the one S113 run still rising at 50,000 goes on.
None of these settles what knowledge is, which environment to pursue, or which of S115's batches 4 to 9 to run: those stay with the owner.

## 6. Running rules

Every Avida process under `timeout` and `nice -n 19`; at most three at once on 4 processors; raw output only in the scratch space (`s116/`), never in git; kills only by exact process number of processes started here; stock Avida at commit 47f13dad (`avida/cbuild/bin/avida`); no patched build is needed (reply 07's bounded runner is not used; the probe reads Avida's own task credits). The whole job stays under about 4 CPU-hours; anything that would exceed it is recorded as proposed, not run. Every departure is recorded in the results.
