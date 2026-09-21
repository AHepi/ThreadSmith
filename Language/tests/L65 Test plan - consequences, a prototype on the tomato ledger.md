# L65 Test plan - consequences, a prototype on the tomato ledger

Written before any query is run. Not edited afterwards.
Authority document: file 10. Language: file 38. Scope: L64 (accepted by the owner without strikes, decision L7). Rig: rig 1 as it stands, patched, s(CASP) 1.1.4 on this machine. Ledger: A, the tomato paragraph, as it stands (13 lines: 11 said, 1 filled in, 1 usual case; four sentences; the recorded report finds a contradiction about the door plant, a BECAUSE that follows, and a plan that cannot work).

## The question, frozen
Step two of the approved five (log L63): before designing a consequences mode, find out cheaply whether the pull between *many consequences* and *exact read-back* (L64, section 7) is real, by asking the checker for everything that follows from the tomato ledger and under each admitted change, and counting.

Two things are asked:
1. **What follows.** Every fact the rules derive from the ledger that no said line states directly: `holds`, `produced`, `denied`, `contradiction`, `depends_on`, `achieves`, `kind`.
2. **What changes.** The same, with each line taken out one at a time (thirteen runs), reported as the difference from the full ledger: what appears, what disappears.

The change list is the contract's first admitted change only (take out one line). WITHDRAW, MAKE NOT SO and slot changes are not run here.

## How it is run
A program, `tools/consequences.py`, new, using the driver's own `run_query` so that the rules, the s(CASP) flags and the time limit are the rig's. It asks each predicate with a variable, collects the bindings, and subtracts the facts a said line states directly (read from the ledger's own clause heads). Nothing is written to the ledger; nothing in the rig is changed. The raw s(CASP) output of every query is kept.

## What I expect
| | Expectation | What would show the pull |
| --- | --- | --- |
| E1 | On the full ledger, the derived facts number between 6 and 12: `produced(dies(...))` for both plants, `holds(dies(door_plant))` (derived, never said), `depends`/`depends_on` for both plants and for the thermometer's reading, `contradiction(dies(door_plant))`. No `achieves`: nothing depends on the reading | More than three times the said lines (over 33) |
| E2 | Exactly one derived fact catches the writer out, `holds(dies(door_plant))`, and it is the same fact the fault mode already reports as a contradiction. On a ledger with a fault, consequences mostly restate the finding | If several derived facts the fault mode never mentions appear, consequences add something on faulty ledgers too |
| E3 | Under each single removal, the difference from the full ledger is small: at most 4 facts appear or disappear. Removing line 5 (the ALWAYS) removes every `produced` and the contradiction. Removing line 9 (the denial) removes the contradiction but `holds(dies(door_plant))` stays: the ledger still commits the writer to the door plant dying. That is the one deduction here a reader would want and the fault mode does not print | A removal that changes more than 8 facts |
| E4 | The thirteen removals together yield 20 to 60 delta lines. Shown whole, that is too much for a four-sentence paragraph; shown as "under change X: these appear, these disappear", it is readable | Over 100 |
| E5 | s(CASP)'s `#pred` wording gives a read-back of every derived fact for free, but the wording "it follows or was said that" cannot tell derived from said; the program has to subtract said lines itself. So the read-back of consequences needs one new fixed sentence: "this was never said; it follows from lines N, M" | If the justification tree names the lines used, the sentence can be built from it; if not, a rule change is needed |
| E6 | Each query answers in under 2 seconds; the whole prototype under 3 minutes | A time-out on any `holds(X)` query means enumeration needs ground queries and the design changes |

## What would count as failure
- Of the idea: no derived fact beyond what is said (E1 = 0), so deductions add nothing on this ledger.
- Of the design: E1 or E4 over their limits, so the filter is the first thing to build, not the last.
- Of the rig: a time-out or an enumeration that s(CASP) refuses.

## Not tested
- WITHDRAW, MAKE NOT SO, slot changes, and told worlds.
- Any ledger but A. A fault-free ledger (A2, or C) is the next one, where consequences are the only output.
- Reading by anyone but Claude.
- How the count grows with ledger size (one point is not a curve).

## Traps
- Editing this file after the run.
- Counting the delta lines as evidence of anything but size.
- Reading "it follows that" as "the writer said". The subtraction is the whole point.
