# S126 The closing knock-out test: results

*Log S126, decisions S76, S80 and S81. 2 October 2026, by the one Opus 5.5 agent of log S126 (S56, S68). The plan, with its two addenda, is `S126 The closing knock-out test - how it will be tested, written before running.md` (committed 3be0483 before anything was prepared; addendum 1, 40dbce8, after the cut search and before any arm; addendum 2, 8ea186a, after phase 1 and before any restoration arm). All numbers are in `S126 The closing knock-out test - results.json`, made by `tools/s126_read_the_results.py` from Avida's own data files. Scripts: `tools/s126_find_the_cuts_and_the_shams.py`, `tools/s126_run_the_arms.py`, `tools/s126_read_the_results.py`. Raw output in the scratch space (`s126/`), not in git. Stock Avida at 47f13dad. In the owner's Avida terms (S61). Observations only; nothing is settled (S28).*

## 1. The answer, short

**Partly yes, under the reading of "Avida itself" as its state.** In population 2, taking the NOT capability out of most programs (copying kept) let the execution environment's NOT store refill from about 290 to about 4,200 to 4,500 (of 10,000) within 100 to 150 updates; a matched harmless change did nothing; and putting the removed instructions back, at update 100, drew the store down to about 300 within 50 to 100 updates, while the same population reloaded without restoring stayed near 4,000 for those updates. In population 1 the same removal of ORN lifted ORN's store fourfold for only eight updates: the quarter of the programs the cut did not reach took over the processor time and drew the store down again. **The strict criteria written before running are not met in either population**: the cut was never complete, the store never stayed above half full, and the run itself brought the capability back by selection (about 1,000 updates in population 2; about ten in population 1). So the result is **mixed**: a capability-specific effect on the execution environment's state that disappears when the capability is removed and returns when it is restored was seen, for a few hundred updates, in one population; it is not a durable or complete knock-out, and it runs through a route Avida's designers wrote.

## 2. What was run

| Step | What | Avida CPU |
|---|---|---|
| Selection | S113 COMMON TASKS PAY LESS, seeds 1 and 2, saved at 50,000 updates; q by S125's rule (most-credited task): **ORN** in population 1 (3,382 programs credited; store 251), **NOT** in population 2 (3,237; store 319); full store 10,000 | 0 |
| Cut search | every living distinct instruction sequence (2,441 and 3,016) probed in Avida's analysis mode on a four-input panel with pay 0; cuts and shams by nop-X (an instruction that does nothing; mutation weight 0) | 3,801 s |
| Rig check | the save continued 200 updates with 26 and with 27 instructions, same seed | 43 s; every data file identical |
| Phase 1 | L0 (unchanged), Lq (cut), Ls (sham): 2,000 updates, two seeds each, both populations; Lr (the removed instructions put back by the same script): 1,000 updates, first seed | 2,269 s |
| Diagnostics (added, addendum 2) | one program alone in an empty world without variation (cut, original, sham; 12 runs, 300 updates); Lq whole, its cut programs only, its uncut programs only, and the cut programs' originals, without variation (8 runs, 100 updates); Lq's first 40 updates saved every 5; and, outside Avida's runs, the cuts on twelve more inputs in analysis mode | 98 s, plus about 6 s |
| Phase 2 (population 2 only) | Lq rerun to update 100 (identical to phase 1's Lq over 0 to 100, both seeds), then Lq-then-restored and Lq-then-reloaded, 1,000 updates, two seeds; the restored programs probed | 318 s, plus the probe (seconds) |
| **Total** | | **about 6,540 CPU-seconds, 1.82 CPU-hours** (3,801 for the cut search, 2,728 for all Avida runs) (at most 3 Avida processes at once, every one under `timeout` and `nice -n 19`) |

Every arm passes through **a reload** (S114: a reload loses working state), all alike; every arm is a continuation after reconstruction. Every store was recorded at every update.

## 3. The cuts

| Population, q | q-sequences (programs) | Clean cut (programs) | Cut losing other tasks too (programs) | No cut (programs) | Replacements, Lq = Ls |
|---|---|---|---|---|---|
| 1, ORN | 1,556 (2,645) | 309 (352) | 1,127 (2,172) | 120 (121) | 2,677 |
| 2, NOT | 1,810 (2,324) | 980 (1,179) | 746 (1,061) | 84 (84) | 2,855 |

On the panel every cut stops q and keeps copying; every sham changes nothing. On twelve further inputs, 0.1 to 2.4% of population 1's cut programs (weighted) still did ORN. **In the world, alone** (one program filling an empty world for 300 updates, no variation, every store starting full), each cut program left q's store full (9,952 at update 300) while its original and its sham drew it to the same level (for example 4,017 and 4,017), and the sham's numbers were identical to the original's. **What the cuts did not reach:** 904 programs of population 1 and 1,227 of population 2 were not q-sequences on the panel (849 and 1,056 programs of the two populations are in sequences that copy on no panel input), plus the q-sequences with no cut, 121 and 84 programs.

## 4. The stores, arm by arm

**Population 2, NOT's store** (seed 2050; seed 2150 alike):

| Update after the reload | 0 | 10 | 20 | 30 | 50 | 100 | 150 | 200 | 300 | 500 | 750 | 1,000 | 2,000 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| L0 original | 266 | 291 | 243 | 265 | 275 | 279 | 254 | 365 | 295 | 260 | 289 | 286 | 283 |
| Ls sham | 266 | 278 | 235 | 265 | 282 | 289 | 273 | 281 | 281 | 298 | 276 | 251 | 337 |
| **Lq cut** | 413 | 1,233 | 1,868 | 2,410 | 3,194 | **4,288** | **4,504** | 4,445 | 3,816 | 2,105 | 741 | 477 | 316 |
| Lq, seed 2150 | 413 | 1,206 | 1,766 | 2,180 | 2,866 | 3,912 | 4,062 | 3,529 | 2,446 | 390 | 309 | 338 | 319 |

**Population 2, from Lq's state at update 100** (a reload; columns are updates after it):

| | 0 | 10 | 20 | 30 | 50 | 100 | 200 | 300 | 500 | 750 | 1,000 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| **Lq-then-restored**, 2050 | 4,179 | 2,990 | 2,244 | 1,655 | 691 | **275** | 316 | 300 | 332 | 296 | 294 |
| Lq-then-reloaded, 2050 | 4,279 | 4,371 | 4,235 | 4,226 | 4,238 | 4,090 | 3,560 | 2,974 | 1,942 | 393 | 431 |
| **Lq-then-restored**, 2150 | 3,796 | 2,370 | 1,741 | 1,042 | 317 | 355 | 382 | 368 | 250 | 286 | 294 |
| Lq-then-reloaded, 2150 | 3,907 | 4,104 | 4,012 | 3,948 | 3,783 | 3,361 | 2,232 | 1,029 | 413 | 417 | 332 |

Restoring put a removed instruction back at 4,292 and 4,262 program sites (ambiguous: 20 and 44), and raised the share of programs doing NOT on the panel from 13% and 12% to 61% and 60% (the original population: 65%).

**Population 1, ORN's store** (seed 1050):

| Update after the reload | 0 | 8 | 10 | 20 | 30 | 50 | 100 | 200 | 500 | 1,000 | 2,000 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| L0 original | 167 | 351 | 291 | 227 | 219 | 223 | 218 | 239 | 232 | 238 | 222 |
| Ls sham | 167 | 361 | 292 | 224 | 243 | 245 | 239 | 242 | 211 | 218 | 202 |
| **Lq cut** | 347 | **1,016** | 945 | 634 | 342 | 310 | 310 | 331 | 258 | 235 | 231 |

**Performances of q per update, inferred from the store** (inflow 100, outflow 1%, each performance taking the smaller of 1.0 and 0.25% of the store; mean of two seeds):

| | updates 1-8 | 9-30 | 31-100 | 101-250 | 251-500 | 501-1,000 | 1,501-2,000 |
|---|---|---|---|---|---|---|---|
| Pop. 1 L0 | 209 | 177 | 170 | 166 | 167 | 167 | 166 |
| Pop. 1 Lq | **12** | 123 | 136 | 146 | 151 | 156 | 164 |
| Pop. 1 Ls | 206 | 181 | 170 | 169 | 168 | 168 | 167 |
| Pop. 2 L0 | 198 | 148 | 139 | 135 | 134 | 134 | 134 |
| Pop. 2 Lq | **10** | **27** | **41** | 63 | 85 | 107 | 125 |
| Pop. 2 Ls | 196 | 152 | 138 | 135 | 136 | 136 | 135 |

**Why population 1 came back in eight updates** (diagnostics without variation, 100 updates): Lq whole, 147 performances per update in updates 9 to 30; only its cut programs (the rest replaced by inert programs), 7, and its store rose to 5,860 by update 100; only its uncut programs, 24 rising to 89; the cut programs' originals, 236. So ORN's store is drawn down in Lq by programs the cut did not reach, and they do it far faster when they share the world with the cut programs than alone. The likeliest reason (not tested separately): in population 1 most cuts also removed other tasks (section 3), so at their first copy the cut programs' merit falls steeply and Avida gives their processor time to the uncut quarter, whose copies then come several times faster. In population 2 the same diagnostic shows the store rising whether the uncut programs are present or not (6,329 and 5,854 at update 100), so there the return in Lq came through variation and selection over hundreds of updates, not from programs left over.

## 5. Against the plan (section 6), population by population

| Criterion | Population 1 (ORN) | Population 2 (NOT) |
|---|---|---|
| 1. Cut works (q executions in 1-100 under 5% of L0's; programs at 1,000 at least 90%) | **not met** as written; the counter used counts last copies (addendum 2); by the store, 12 of 209 performances in updates 1-8, then 123 of 177 | **not met** as written; by the store, 10 of 198 (5%) in 1-8, 27 of 148 (18%) in 9-30, 41 of 139 (30%) in 31-100; programs kept (3,560 and 3,530 against 3,547) |
| 2. Disappears (window 201-1,000 mean at least 5,000 and above the L0 band) | **not met**: 276 and 237 (band 176 to 296) | **not met** as written: 1,829 and 949 (band 217 to 363); peak 4,532 at update 163 and 4,190 at 132, 15 times L0 |
| 3. Specific (other eight stores in their L0 bands) | met (nothing moved, as q's store did not either) | **not met** in seed 2050 (NAND, ANDN, XOR, EQU above their bands: the cuts' collateral losses); met in seed 2150 |
| 4. Not generic damage (Ls's q store in the L0 band) | met (234, 234) | met (289, 288) |
| 5. Handled alike (Lr file identical to L0's; same numbers) | met (identical file; identical numbers over 1,000 updates) | met |
| 6. Returns (restored arm's window mean under 1,000, the reloaded one's at least 5,000 or q re-evolved) | not run (nothing rose to return from; addendum 2) | **met**: 294 and 292; reloaded 1,499 and 533 as NOT re-spread; in updates 1-200 the restored arm averaged 741 and 596, the reloaded one 4,018 and 3,234 |
| Verdict | **against as written**, diagnosed as a cut that did not reach every ORN program | **mixed**: criteria 4, 5, 6 met; 1, 2, 3 not as written, with a clear transient effect and return |

**Overall: not "for"** (the plan required both populations to meet 1 to 6). The verdict in plain terms is in section 1.

## 6. Departures

1. **Lengths shortened** before any arm (addendum 1): 2,000 updates for L0, Lq, Ls; Lr 1,000 updates with one seed; the cut search cost 1.06 CPU-hours, not under 0.3.
2. **A counter misdescribed** in the plan: `PrintTasksExeData` sums each program's tasks of its last completed copy, so it is not "new executions"; criterion 1 is read as written and also from the store.
3. **Diagnostics added** after phase 1 (addendum 2). In two of them, programs left out are replaced by programs of nop-X only (leaving lines out, or marking them no longer living, made Avida fail at load); these inert programs hold their cells and processor time until they die of age.
4. **Restoration moved** to update 100 and to population 2 only (addendum 2), after phase 1 had been read. The rerun to update 100 repeated phase 1's Lq exactly (its first check said otherwise because of a blank-line artefact in the comparison; rechecked).
5. **The fallback rule for cuts** was applied size-first ("smallest, then fewest losses"); a losses-first reading or a wider search might have given cleaner cuts in population 1; not tried (cost).
6. **Replay arms** (R0, Rq) not run, as planned.

## 7. What is unsure

- Why the uncut programs of population 1 draw ORN's store down so much faster beside the cut programs than alone: the merit explanation fits the timing (the jump comes at the cut programs' first copy, update 9) but was not tested by itself.
- Which of population 1's uncut programs do ORN in the world although the panel did not show it (those in sequences that copy on no panel input are the likeliest; not probed in the world one by one).
- Whether population 2's return in Lq is re-evolution, reversion of the cut sites, or the spread of a few residual NOT programs: the share of programs carrying the cut fell over the run, but lineages were not traced.
- Floating-point store values are from Avida's printed data (six significant figures).
- Two populations, one task each, one execution environment; the effect sizes would differ elsewhere.

## 8. What it means for S76 and the refined hypothesis

**Under the state reading of "Avida itself"**, a learned capability's effect on Avida's own state has now been **measured**: the NOT store's level depends on the instructions that perform NOT (cut: it refills; sham: no change; restored: it is drawn down again), at the population level, over hundreds of updates. That is the outward clause (4) of S125's refined hypothesis observed once, in one population, transiently. It also shows something the plan did not expect: **the run defends the capability**. When the store refills, the pay for doing q rises (for NOT from about 1.65 to 2 times a program's merit; for ORN from about 2.4 to 4 times), and any program still or newly able to do q spreads, so the effect on the store fades by itself. Under the other readings of "Avida itself" (its rules, the settings it reads), nothing here bears: no program changed a rule, and the route (task performance drawing on a finite store) is one Avida's designers wrote. Whether this counts as the causal effect the owner's definition asks for is the owner's to say.

**Not tested:** Avida's rules; the replay controls; where the knowledge sits (H1' against H2'); outside data; construction; explanation; uninterrupted state.
