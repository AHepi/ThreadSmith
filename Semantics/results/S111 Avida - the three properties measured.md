# S111 Avida: the three properties measured

*Log S111, decision S59. Being filled as the runs end; not final until this note is replaced.*

## 1. What was done

The owner (S59) states knowledge as information that "Can cause itself to be copied", "Can cause itself to resist change" and "Can cause itself to remain", and asked for "a type of program with these exact properties". Claude named digital organisms; the owner said to run Avida and measure. The plan was written and committed before any measuring run (e958a0d): `results/S111 Avida - how the three properties will be measured, written before running.md`.

- **Avida** 2.14.0 (commit 47f13dad), built in the scratch space with no patch and no extra compiler flag (build notes: `results/S111 Avida - the runs/build notes and Avida's rules as read from its source.md`).
- **The ancestor**: Avida's default hand-written organism, 100 instructions.
- **Nine main worlds**: copy error rates 0.0025 (low), 0.0075 (default), 0.02 (high) per copied instruction, three seeds each, 50,000 updates, everything else Avida's default (60 × 60 grid; one inserted and one deleted instruction each with probability 0.05 per birth; death after executing 20 times the genome's length; the nine logic tasks rewarded).
- **Five control worlds** (K1 to K5) and the test-processor measures (knockouts, one-change programs, random programs).
- Exact commands: `results/S111 Avida - the runs/the exact commands.txt`. Summary tables, each written by one script in `tools/`: `copying and knockouts`, `the worlds over time`, `mutational robustness`, `Marletto test on the logic tasks` (`.md` and `.json`) in `results/S111 Avida - the runs/`. Raw output stays in the scratch space.

## 2. COPIED
## 3. RESISTS CHANGE
## 4. REMAINS
## 5. Marletto's test on the logic tasks
## 6. What the program causes and what the simulated world does
## 7. Departures from the plan, failures, and what was not measured
## 8. What these organisms have and do not have, beside the explanation kind
