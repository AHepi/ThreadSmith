# L71 Test results - consequences on the henhouse and on the longest ledger

Plan: "L71 Test plan - consequences on a fault-free ledger and on the longest.md", frozen at commit 936ce21 before any query was run; not edited since. Program: `tools/consequences.py` as it stood at that commit. Rig 1 patched, s(CASP) 1.1.4. Ledgers C and H as they stand in `rigs/rig 1 - arguments/`. Outputs, raw logs and timings in "L71 Consequences - C and H/".

## The plan's premise on C was wrong
The plan called C "a ledger where the checker found nothing". It was written from my memory of log 07's phrase "C right with no change". That phrase meant the checker was **right** on the henhouse with no patch: it found the contradiction the paragraph is built on (a fox took the hens, yet there was no gap, no climbing and no opened gate, so the fox never got inside). I re-ran the checker on C after the consequences runs; its report (`checker_report_C.txt`) prints CONTRADICTION about got_inside(fox), leaning on six lines. So this test has no fault-free ledger in it. The question the plan wanted answered for a clean ledger, whether consequences are the only output and none surprises, is still open, and is a new plan, not a re-reading of this one. Lesson L6.

## What the runs printed
| | C henhouse | H abolish Mondays |
| --- | --- | --- |
| lines | 9 | 27 |
| facts stated directly | 6 | 18 |
| facts found | 9 | 19 |
| derived, not stated by any line | 4 | 8 |
| delta lines over all removals | 18 | 28 |
| removals that change nothing | 2 | 12 |
| largest single removal | 4 facts (line 5) | 5 facts (line 17) |
| time | 5 s | 14 s |

C, derived: `contradiction(got_inside(fox))`, `denied(got_inside(fox))`, `holds(got_inside(fox))`, `produced(gone(hens))`. Taking out line 1 ("the hens are gone") changes nothing, because usual-case line u3 produces it from line 5; taking out the BECAUSE line 6 changes nothing either, since a BECAUSE claim states no fact.

H, derived: the contradiction `exists(monday)` with `holds(exists(monday))` and its denial from lines 17, 18, 19; `holds(arbitrary(monday))` from lines 1 and 2; `holds(optional(monday))` from 12 and 14; `holds(is_leisure(time))` from 22 and 24; `holds(basis_of_culture(time))` from 22, 24, 25; `becomes(tuesday, monday)` as holds and as produced from 17 and 18.

## The expectations, marked
| | Expected | Found | Mark |
| --- | --- | --- | --- |
| E1 C, derived | 3 to 8; at most one unstated `holds`; none surprises | 4; one unstated `holds` (got_inside); but two of the four are the contradiction and its denial | met on the count; the wording rested on the false premise above, so "none surprises" is not a fair test of anything |
| E2 C, deltas | under 20; removing the stated effect changes nothing | 18; line 1 removal changes nothing | met |
| E3 H, derived | 8 to 25; the SINCE claims yield no `holds`; the contradiction appears as a derived fact | 8; no SINCE claim yields anything; `contradiction(exists(monday))` derived | met, at the bottom of the range |
| E4 H, deltas | 40 to 120; largest removal at most 12 | 28; largest 5 | **not met, on the low side**; not in the "would count against" column (over 150), so the plan's range was simply too high. I overestimated how much H's lines lean on each other |
| E5 what the mode misses | no SINCE step visible in the consequences | none visible; the seven SINCE lines (5, 9, 13, 16, 21, 23, 27) are seven of the twelve removals that change nothing | met |
| E6 time | each under 3 minutes | 5 s and 14 s | met |

Five of six met; E4 missed low.

## What I did not expect
1. **Stated facts hide derived ones.** Taking out ALWAYS lines 3, 6 and 10 of H changes nothing, though the chain leans on them. The reason: the facts they would derive (Monday lacks authority; no duty to obey; Monday is a suggestion) are also stated outright by lines 4, 8 and 12, and the program subtracts what a line states. So a consequences report is blind to a general line whose only work is to derive something the writer also asserts. On C the same thing hides u3's work on line 1 until line 1 is removed. Whether this is a fault depends on the reader: the checker's SINCE test already covers those steps, and E5 says the two modes need each other. It is a limit of the mode to put in the read-back brief, not a rule change.
2. **On H the derived list is the argument's skeleton.** Four of the eight derived facts are exactly the intermediate facts the paragraph's SINCE lines claim to reach (arbitrary, optional, leisure, basis of culture), each with the ALWAYS line and the particular line it rests on. A reader who wanted the argument's steps made explicit gets them here without asking, but only for the steps the writer did not also state as facts (point 1). The checker says whether each SINCE step connects; the consequences program says which intermediate facts follow at all. The overlap is larger than the plan's E5 wording suggested, and the difference is still real.
3. **Size.** H has three times C's lines and took three times as long; its delta count grew by only ten. Consequences on an argument ledger do not multiply with length, because most lines in an argument are claims about lines and derive nothing. L65's worry about a pull between many consequences and exact read-back is not visible at 27 lines either.

## Not tested
A fault-free ledger (the plan's stated aim, missed for the reason above). WITHDRAW and MAKE NOT SO. Rig 2. Any reader.

## Next
A short plan on two ledgers the checker reports clean (candidates: T05-D, one line; D or E from the five paragraphs, if their recorded reports are re-run and printed first, per Lesson L6). Then the read-back brief gets point 1 above.

## Traps
- Reading "C right with no change" as "nothing found". It means the opposite.
- Counting E4's miss as evidence that H is a weak argument. The count measures how many facts lean on each line, not whether the argument holds.

Note, added after the rebase onto main: the plan was frozen as commit 936ce21 on the working branch; rebasing onto main (which had moved by one Semantics commit) renumbered that commit 2b39096. Its content is unchanged; `git show 2b39096` is the frozen plan.
