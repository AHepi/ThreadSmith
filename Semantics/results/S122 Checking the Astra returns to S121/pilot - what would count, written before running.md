# The S122 pilot: what it is and what would count against, written before running

*Log S122, decision S75. Written by Claude (Opus 5.5) on 1 October 2026, before the pilot was started, and committed before any of its output was read. In the owner's Avida terms (S61); the **execution environment** is the whole simulated world and is the selector under test (S72). This is a pilot: two seeds, 20,000 updates, far below the experiment reply 01 proposes (eleven arms, 50,000 updates, 3 or 40 seed blocks). It is reported as a pilot, not as the experiment.*

## What runs

Reply 01's own code (`tools/s122/01/temporal_selector/runner.py`, `assay.py`, `selector.py`, unchanged; their SHA-256 match the reply's own list), stock Avida at 47f13dad (the clone in the scratch space, read only; the runner's own check that the checkout is the pinned commit and unmodified passes), the stock `avida.cfg` with the runner's changes only (seed, world size, verbosity), the stock heads instructions and the stock task-free ancestor, a 60 x 60 world (the reply's default), the fixed input triple 0x0F13149F, 0x3308E53E, 0x556241EB set in the world, 77 task detectors (66 paid, 11 withheld at zero pay), pieces of 1,000 updates with a save and reload between pieces, the reply's six-order assay after each piece, **20 pieces (20,000 updates)**.

| Arm | Runner `--arm` | Master seeds | What the execution environment does |
|---|---|---|---|
| Temporal selector | `full` | 2201, 2202 | the reply's seven units with their state kept from piece to piece |
| Memory wiped | `memoryless` | 2201, 2202 | the same equations, the state set back to zero before every step |

The same master seed is used in both arms of a pair, so the two arms of a pair run the same Avida seeds piece by piece, and their first two pieces are identical (both selectors start from zero state; they first differ in the pay set for piece 3). Each Avida process runs under `nice -n 19` and a 900-second timeout (a small wrapper around the binary); each runner under `nice -n 19` and a 3-hour timeout; at most three at once. Raw output in the scratch space (`s122/pilot/`), never in git.

## What Claude expects, from reading the code before running

- **Pay never vanishes and never explodes.** The pay for the 66 paid detectors always sums to 18 doublings (a doubling multiplies a program's share of processor time by 2). With nothing common, each gets 18/66 = 0.27 of a doubling (a 21% gain), about three times the 0.1 that made nothing common in S120's pilot of reply 02, and about a quarter of the up-to-one doubling of S118's P1 (12 to 21 common functions at 20,000). So Claude expects **a few common capabilities (0 to 6) at 20,000 in each arm**, mostly the easy ones (NOT, NAND, ORN).
- **Adaptation cuts the pay of the first capability.** Once NOT is common in all orders (say half the programs), its trace rises and its pay falls from 0.27 towards about 0.08 doublings. Claude expects NOT to stay common anyway (it costs little), or, if it is lost, a loss latch to set and raise its pay again.
- **Latches.** A latch sets when a capability is common in the world's order but fails in other orders, or when a common one is lost. S117 found most NOT programs pass in all six orders, so Claude expects few order latches; loss latches only if a capability rises and falls. Claude expects **few or no latches to be cleared** by the program population in 20 pieces, because the world never shows the other orders and so never pays for passing them.
- **The two arms are alike in what becomes common.** The memory-wiped arm differs from the full arm in more than memory: with zero state its trace is 0.22 of the current share, its surprise unit pays the current share (the forecast is always 0), its loss latch and sequence unit never fire. Claude expects these differences to move pay by a few hundredths of a doubling per task, too little to change what becomes common in 20,000 updates.

## What would count against these expectations

- Against "the two arms are alike": in at least one seed, the common counts (world order or all orders) of the two arms differ by 3 or more at piece 20, or the set of common capabilities differs by 3 or more. (With two seeds, a difference would be a lead to follow, not a result.)
- Against "pay never vanishes or explodes": any piece where a paid detector's pay is below 0.01 or above 6 doublings, or the paid total differs from 18.
- Against "few or no latches cleared": two or more latches set and later cleared in one run.
- Against "a few common capabilities": no common capability in either arm of either seed (then the pay is too weak for 20,000 updates, as in S120's pilot), or more than 12.

## Measures

From the runner's own records (`piece_NNN/complete.json`, `assay/observation.json`; read by `tools/s122_read_the_temporal_selector_pilot.py`): per piece, capabilities common in the world's order and in all six orders, common withheld ones, latches set and released, the pay vector (least, most, the share of the 18 going to latched detectors), the ten most common capabilities; the CPU time of each Avida piece and of each assay (reply 04 says the assay "may dominate" the cost; reply 01 says the assays are expected to dominate). Also the reply's own `summarize.py` on each finished run.

## Cost expected

About 70 to 90 CPU-seconds per piece (S113's one CPU-hour per 50,000 updates), plus a few seconds of assay: about 0.45 CPU-hours per run, **about 1.8 CPU-hours for the four**, within the job's 4. If the first pieces run much slower, the runs are cut to fewer pieces and the cut is reported.
