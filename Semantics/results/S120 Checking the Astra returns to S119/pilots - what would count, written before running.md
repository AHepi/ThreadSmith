# The two S120 pilots: what they are and what would count against, written before running

*Log S120, decision S74. Written by Claude (Opus 5.5) on 1 October 2026, before either pilot was started, and committed before any of their output was read. In the owner's Avida terms (S61); the **execution environment** is the whole simulated world and is the selector under test (S72). Both are pilots: one seed or two, 20,000 updates, far below the experiments the replies propose. They are reported as pilots, not as the experiments.*

## Pilot 1: reply 02's two selectors with memory, against a fixed control (stock Avida)

**What runs.** Reply 02's own driver (`tools/s120/02/run.py`, unchanged), stock Avida at 47f13dad, 60 x 60 world, the heads instructions, the task-free ancestor, all 77 logic tasks detected, pieces of 1,000 updates with a save and reload between pieces, 20 pieces (20,000 updates), one seed per arm:

| Arm | Driver mode | Seed | What the execution environment does |
|---|---|---|---|
| A, learning progress | `progress` | 1001 | pays each task in proportion to how fast its share of programs rose over the last 5 pieces; flat or falling shares are paid nothing |
| B, rarity against an archive | `archive` | 4001 | shares a fixed total (7.7 doublings) among the 77 tasks, more to tasks with less accumulated exposure |
| Fixed control | `all77` | 7001 | pays every task the same 0.1 of a doubling in every piece (the same total as B, never changing) |

Each Avida process runs under `nice -n 19` and a timeout of one hour (a small wrapper around the binary); at most three at once.

**What Claude expects, from reading the code before running.**
- **A will pay almost nothing.** Its pay for a task is 7.7 times the rise in that task's share per piece, divided by the total rise only when the total exceeds 1. In piece 1 every task gets 0.1. If no task's share has risen by the end of piece 1, every pay is zero from piece 2 on, and stays zero until some share rises by chance. Even then a rise of 1 program in 3,600 pays about 0.002 of a doubling. So A is expected to behave like an execution environment that pays nothing (S113's NO TASK REWARDS: no common task).
- **B and the fixed control are expected to be alike.** Both pay about 0.1 of a doubling per task (a 7% gain each); B moves at most a few hundredths towards unseen tasks. Both pay much less per task than S118's P1 (up to a full doubling) or S113's lists. Claude expects fewer common tasks than P1's 12 to 21 at 20,000.

**What would count against these expectations.**
- Against "A pays almost nothing": A's total offered pay at least 1 doubling in at least 5 of pieces 2 to 20, or A with at least 3 common tasks (at least 10 in 100 programs) at 20,000.
- Against "B is like the fixed control": B with at least 5 more common tasks than the fixed control at 20,000 (one seed each, so even this would be weak).

**Measures.** From the driver's own record (`observations.json`): offered pay per piece, tasks present, tasks common (at least 10 in 100 programs, Avida's own count at each piece's end), first common, lost, reacquired. At the last piece, reply 02's own assay (`measure_orders.py`, six input orders on the test CPU).

## Pilot 2: reply 01's anticipating execution environment, from the stock ancestor (patched copy)

**What runs.** The patched copy of Avida (reply 01's five-file patch, unchanged), 60 x 60 world, the stock heads instructions and default ancestor (which has no `IO`), copy changes 0.0075, one insertion and one deletion each with chance 0.05 per division, the one capped reaction `REACTION ANT anticipate process:value=1:type=pow requisite:max_count=1` (a doubling, at most once per copy cycle), `ANTICIPATE_START -1`, `SPECULATIVE 0`, `MERIT_INC_APPLY_IMMEDIATE 1`, no copying requirement: the settings of reply 01's proposed experiment. 20,000 updates, one continuous process each:

| Arm | Rule | Seeds |
|---|---|---|
| R2 (each next number is the last plus one) | `ANTICIPATE_MODE 2` | 1 and 2 |
| R1 (the same number again and again) | `ANTICIPATE_MODE 1` | 1 |

**What Claude expects.** R1 is met by any program that outputs the number it last read, which `IO` does by itself when it runs twice on the same register; it is expected to spread soon after programs gain an `IO`. R2 needs one `inc` between two `IO`s on the same register; it is expected to be found too, perhaps later. Neither shows more than that the execution environment pays for a short fixed relation.

**What would count against "anticipation is found at all from the stock ancestor".** Under R2, fewer than 1 in 100 programs performing the match (Avida's count in `tasks.dat`) at 20,000 updates in both seeds.

**What would count against reading an R2 match as anticipation rather than a fixed recipe.** Saved R2 programs, rerun on the test CPU with fresh streams, that match as often under R1 as under R2 (then they repeat, they do not add one), or that match under R0 (random numbers) above chance.

**Cost expected.** About 0.3 to 0.5 CPU-hours per run of pilot 1 (77 detectors, reloads) and 0.2 to 0.4 per run of pilot 2: about 2.5 CPU-hours for both, within the job's 4.
