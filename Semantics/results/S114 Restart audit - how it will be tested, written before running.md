# S114 Restart audit: how it will be tested, written before running

*Log S114, decisions S64 to S66. Written 30 September 2026 by the one Opus 5.5 agent of log S114 (S56), **before any run of the audit**, and committed by that agent before the runs start. In the owner's Avida terms (S61): an **Avida program** is one program in a **program population**; a **distinct instruction sequence** is what Avida calls a genotype; a **computational capability** is one of Avida's logic tasks, and a program has it when Avida credits it with **task performance**; the **Avida execution environment** is the list of rewarded tasks, their rewards and any resources. All entities are digital programs executing on Avida's virtual CPU. Observations only; nothing is settled (S28).*

---

## 0. Why

GPT 6 Astra's reply to the S114 brief (`tests/S114 Return from GPT 6 Astra - execution environments report.md`) says, as its first point: Avida's saved program population is not a complete record of the running world, so S113's procedure (50 pieces of 1,000 updates, the program population saved at the end of each piece and loaded into a new Avida process) may itself change what happens; it proposes a restart audit before S113's learning curves are read. What the source says the save and reload keep and lose is checked line by line in `results/S114 Checking GPT 6 Astra's reply.md`. In short (Avida 2.14.0 at commit 47f13dad): the save keeps each distinct instruction sequence, the cells its programs sit in, how many processor cycles each has used in its current copy, and the sequence's *average* merit; the reload makes every program new, with empty processor registers, stacks and instruction pointers (every loaded program starts executing its instruction sequence from the top), gives every program of a sequence that sequence's average merit, scaled up by the share of the copy it still had to do, sets every program's **generation count to 0** and its record of tasks performed to empty; the random-number state is not saved (S113 gives each piece a new seed); resource levels are not in the saved file (S113's runner carries them over itself, by writing each resource's last printed level into the next piece's environment file). This audit measures whether these differences change the process.

## 1. What is compared

For each of two of S113's Avida execution environments, and each of three seeds:

- **PIECES**: 10 pieces of 1,000 updates, run by **S113's own runner** (`tools/s113_run_the_avida_execution_environments.py`, its function `run_one`, imported and called unchanged with `pieces=10` and an output folder in the scratch space): the same environment files, events, save and reload steps, seeds (Avida seed = 1,000 × seed + piece number), resource carry-over and 900-second timeout per piece as S113.
- **CONTINUOUS**: one Avida process of 10,000 updates, with the same `avida.cfg` (S111's, copy error 0.0075 per copied instruction, and at each division a 0.05 chance of one inserted and a 0.05 chance of one deleted instruction), instruction set, starting program (`default-heads.org`, injected once), environment file (S113's `environment_text`, first piece) and Avida seed as the first piece (1,000 × seed). It prints task counts and program counts every 250 updates, as S113's pieces do, the average data, the most common sequence and the saved program population every 1,000 updates, as the pieces do at their ends, and the resource levels **every update**.

The environments: **FIXED GRADED** (`fixed_graded`: the nine two-input tasks rewarded, values 1 to 5 by level; all 77 logic tasks listed, 68 with value 0) and **COMMON TASKS PAY LESS** (`common_pays_less`: the nine rewarded through nine resources that run down, inflow 100, outflow 1% per update, frac 0.0025, max 1; the 68 listed with value 0). Seeds **11401, 11402, 11403** (Astra's seeds; not S113's 1 to 3, so no S113 run is repeated or read). 12 runs in all, 120,000 updates.

**Extra checks**, run in the same queue:
- **C1, the extra printing.** The continuous run's first 1,000 updates use the same seed and environment as piece 0; if printing more often changes nothing, their task and program counts at updates 250, 500, 750 and 1,000 are identical. If they differ, the continuous runs are still compared, but the difference is recorded.
- **C2, resources just after a reload.** Piece 5 (updates 5,000 to 6,000) of COMMON TASKS PAY LESS seed 11401 is run again from the same saved program population, seed and environment file, with the resource levels printed at every update from 0 to 20 besides the original printing; its task and program counts should repeat the original piece's exactly (a check that a piece is repeatable), and its levels at update 0 and 1 are the levels just after the reload.
- **C3, Astra's native examples** (for the claim check, not for the audit): Astra's restart-audit event files (first segment, then one reloaded segment of 1,000 updates, its nine-task environment, seeds 11401 and 111401), its native analysis commands on the reloaded segment's saved program population, and its B1 event file with its proposed `S114...` actions on stock Avida (Astra says stock Avida must refuse it).

Everything is run by `tools/s114_restart_audit_run_the_pieces_and_the_continuous_runs.py`; raw output in the scratch space (`s114_restart_audit/`). While S113's runner (process 2411) is alive, **one Avida process at a time**; after it has ended, at most three. Every Avida process under a timeout (900 s per piece, 5,400 s per continuous run, 120 to 900 s for the checks). Order: the C3 checks, then seed 11401 (FIXED GRADED pieces, continuous; COMMON TASKS PAY LESS pieces, continuous, C2), then 11402, then 11403. If time runs short, seeds are cut whole (a seed is either run in both ways for both environments, or not counted), and this is recorded.

## 2. The measures

At the same cumulative updates in both ways (every 250 updates; piece k's local update u is cumulative update 1,000 k + u):

- **M1, capabilities present.** From `tasks.dat` and `count.dat`: the number of the 77 tasks performed by at least one program, and by at least 10% of the program population ("common", S113's share); the nine two-input tasks' prevalence (share of programs performing each, in points out of 100).
- **M2, generations.** `average.dat`'s average generation. Because the reload sets every program's generation to 0, the PIECES figure at cumulative update 1,000 (k+1) is the sum, over pieces 0 to k, of each piece's average generation at its end; CONTINUOUS is read directly. (This sum is an estimate: it adds the generations the programs alive at each piece's end went through in that piece.)
- **M3, births.** `count.dat`'s births in the sampled update, and its instructions executed in that update; and the program count.
- **M4, resources** (COMMON TASKS PAY LESS). For each reload: the level of each of the nine resources printed at the end of piece k (update 1,000) — "just before" — and the level at which piece k+1 starts: the `initial=` value S113's runner wrote into piece k+1's environment file, and, for the one reload of C2, the levels Avida prints at updates 0 and 1 — "just after". For CONTINUOUS, the levels at the same cumulative updates, every update.
- **M5, the samples just after a reload.** The PIECES values at local update 250 (the first sample of each piece after the first), against CONTINUOUS at the same cumulative updates, for M1 and M3: the S113 plan already expects task counts there "a little low", since a loaded program's record of tasks is empty until it completes a copy.

## 3. What will count as the piece procedure changing the process (fixed now)

The comparison is PIECES minus CONTINUOUS, per seed, using the piece-end samples at cumulative updates 5,000, 6,000, ..., 10,000 (six samples, averaged) unless said otherwise. A difference **counts** when **all three seeds differ in the same direction and the smallest of the three differences is at least the threshold**:

- **T1**: at least **1 common capability** (M1, the number of the 77 performed by at least 10%), averaged over the six samples; or at update 10,000 alone.
- **T2**: at least **5 prevalence points** in any one of the nine two-input tasks (M1), averaged over the six samples.
- **T3**: at least **10% in generations** (M2) at update 10,000, relative to CONTINUOUS.
- **T4, resources reset**: at any reload of any seed, a resource's "just after" level differing from its "just before" level by more than 1% of the "just before" level (the levels are printed to six significant figures, so rounding alone stays far below 1%). Also counted if C2's printed level at update 0 differs by more than 1% from the `initial=` value written.
- **T5, just after a reload** (M5), reported apart: a difference at local update 250 of at least 1 common capability, 5 prevalence points or 10% in births, in all three seeds the same way. This concerns S113's samples inside pieces, not the course of the run.

If a difference is in the same direction in all three seeds but below its threshold in at least one, it is reported as **"same direction, below the threshold"**, not as a change. Differences that go different ways in different seeds are **"not separated by three seeds"**: with three seeds, and with the random stream of the two ways parting after update 1,000 (the pieces reseed at every reload), this audit can detect only large, consistent effects; small ones are not excluded. Passing all thresholds does **not** make the saved file an exact checkpoint (the source says it is not); it would mean only that, at this size, these measures did not move.

## 4. What it will be taken to mean for reading S113 (fixed now)

- **If none of T1 to T4 counts**: S113's piece-end numbers for FIXED GRADED and COMMON TASKS PAY LESS can be read as those of unbroken runs, at the scale of these thresholds; the same is then assumed, not shown, for ONE HARD TASK ONLY, NO TASK REWARDS and FIXED LARGE LIST, which use the same pieces without resources. GROWING LIST's reward changes happen only at the breaks, so there the break is part of the environment and is not separable by this audit.
- **If T1, T2 or T3 counts**: the environments' comparisons in S113 stand only as comparisons between runs that all went through the same pieces; statements about how fast or how far a program population gets in an environment are qualified by the direction and size found.
- **If T4 counts**: COMMON TASKS PAY LESS in S113 is not the environment described in its plan (depletion would be undone at every break), and its results are read as such.
- **M2 in any case**: S113's `average.dat` generation at a piece's end counts only the generations since that piece's start; any S113 statement about generations must use the sum over pieces.
- **T5**: S113's samples at local update 250 (and possibly 500) are corrected or left out in the S113 reading if T5 counts.

## 5. What will not be measured

The other four S113 environments; more than three seeds or more than 10,000 updates; which program ancestries differ; the effect of the new random seed at each reload apart from the effect of the reload itself (Avida's saved file has no random state, so the two cannot be separated with stock Avida); anything about S113's own runs, which are not read or touched by this audit.

## 6. Departures

Any departure from this plan is recorded in `results/S114 Restart audit - results.md`.
