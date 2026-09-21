# L65 Test results - consequences, a prototype on the tomato ledger

Plan: L65, frozen at commit 7f12100 before any query. Run 21 September 2026 on this machine, rig 1 patched, s(CASP) 1.1.4. Program: `tools/consequences.py` (new; its first run had a parser fault that listed one stated fact as derived; the fault was found by reading the output against the ledger, fixed, and both runs are kept in the results folder, Lesson L4). Raw s(CASP) output of every query: `results/L65 Consequences prototype - the tomato ledger/raw_log_consequences_A.txt`, 140 queries, no time-out. Everything below is **seen** unless marked.

## What happened, against what was expected

| | Expected | Seen | |
| --- | --- | --- | --- |
| E1 | 6 to 12 derived facts; no `achieves` | **10** derived facts on the full ledger: `produced(dies(...))` for both plants; `holds(dies(door_plant))`, never said; `depends` and `depends_on` for both plants and for the reading; `changes(move(thermometer), reading(thermometer))` from the usual-case line; the contradiction. No `achieves`. 19 facts found in all against 11 stated directly | Right |
| E2 | One derived fact catches the writer out, and the fault mode already reports it | `holds(dies(door_plant))` (and `produced(dies(door_plant))`, the same fact in its producing form) from lines 2, 5, 7: the ledger commits the writer to the door plant dying. The fault mode reports it as the contradiction with line 9. Nothing else derived is news to the fault mode | Right |
| E3 | At most 4 facts change per removal; line 5 removes every `produced`; line 9 removes the contradiction but `holds(dies(door_plant))` stays | Line 5: **8** change; line 2: **6**; line 7: 4; the rest 0 to 4. Line 9: as predicted, the contradiction goes and `holds(dies(door_plant))` stays. Lines 8, 10 and 12 (the writer's own "died", the BECAUSE claim, the plan) change nothing when removed: claims about lines have no consequences in this predicate set, and "the balcony plants died" is produced by lines 1, 5 and 6 without being said | Wrong on the bound (two removals exceed 4; none exceeds 8); right on the shape |
| E4 | 20 to 60 delta lines over thirteen removals | **32** | Right |
| E5 | The `#pred` wording cannot tell derived from said; the program must subtract; the justification tree may name the lines | The tree names them ("line 5 is in the ledger, and balcony_plants is a tomato_plant, because line 1 is in the ledger"), and the program prints "<- lines 2, 5, 7" from it. The sentence "this was never said; it follows from lines N, M" can be built with no rule change | Right; no rule change needed |
| E6 | Under 2 s a query, under 3 min in all | 0.05 to 0.2 s a query; **7 s** in all | Right |

**Failure of the idea:** no. Ten derived facts, one of which is the deduction a reader would want.
**Failure of the design:** no. E1 and E4 inside their limits; the filter is not the first thing to build.
**Failure of the rig:** no.

## What this shows, and what it does not
- The pull between many consequences and exact read-back is **not real at this size**: 10 derived facts and 32 delta lines for a four-sentence paragraph, read in a minute. It may become real with size; one ledger is one point, not a curve (not tested).
- Of the ten derived facts, four are what a reader would call consequences (`holds`, `produced`, `contradiction`); six are the checker's bookkeeping (`depends`, `depends_on`, `changes`). A consequences report should show the first kind and keep the second behind it. **Worked out** from the list; not a rule yet.
- The single deduction that matters, "the door plant died, though you say it did not, because you say cold always kills a tomato plant it reaches and the cold reached it", is exactly the fault mode's contradiction seen from the other side. On a faulty ledger, consequences restate findings. On a fault-free ledger they would be the only output, which is why the next ledger to run is a fault-free one (A2, or C).
- "Take out line 8: nothing changes" is a consequence the fault mode does not print: the writer's own statement that the balcony plants died is doing no work, since the general line and the two facts produce it. That is the "idle" mark of the hard-to-vary skill, found by the checker on the writer's line.
- The read-back of a derived fact needs one new fixed sentence and the line numbers from the tree, both available. Untested on any reader (the read-back test, step three, still owed).

## Not tested
WITHDRAW, MAKE NOT SO, slot changes, told worlds; any ledger but A; growth with size; any reader but Claude.

## Traps
- Reading "nothing changes" as "the line is wrong". It means the line is idle for what follows; it may still be what the writer wanted to say.
- Reading the six bookkeeping facts as deductions about the world.
- Taking 7 seconds as a bound. Thirteen lines; the queries grow with lines times general lines.

## PARKED
- A consequences report: derived `holds`/`produced`/`denied`/`contradiction` first, with "never said; follows from lines N, M"; bookkeeping predicates behind a line.
- Run on a fault-free ledger next (A2 or C), and on the longest (H, 27 lines) for the size point.
- WITHDRAW and MAKE NOT SO as changes, using the driver's what-if code.
