# L71 Test plan - consequences on a fault-free ledger and on the longest

Written before any query is run. Not edited afterwards. The two follow-ups L65 parked: a ledger where the checker found nothing, so consequences are the only output; and the longest ledger, for a second point on size.

Rig 1 patched, s(CASP) 1.1.4 on this machine; `tools/consequences.py` as it stands (the parser fix of Lesson L4 in place). Ledgers as they stand: **C** (henhouse; 9 lines, 5 said, one BECAUSE claim; the recorded run at log 07 found nothing and needed no patch) and **H** (the owner's Mondays paragraph; 27 lines, 25 said, seven claims about lines, the seven-step chain; the recorded run found a contradiction and five steps that do not connect).

## What I expect
| | Expectation | Would count against |
| --- | --- | --- |
| E1 C, derived | Between 3 and 8 derived facts; the henhouse's general line produces its effect for the thing it names, and that produced fact is also said, so at most one derived `holds` that no line states. On a clean ledger the consequences are few and none surprises | More than 12, or none |
| E2 C, deltas | Under 20 delta lines over nine removals; removing the writer's stated effect changes nothing (the general line produces it), as on the tomato | Over 30 |
| E3 H, derived | Between 8 and 25 derived facts. The seven SINCE claims are claims about lines and yield no `holds`; what is derived comes from the ALWAYS lines applied to Monday and to the things the paragraph names. The contradiction ("there is a Monday") appears as a derived fact | Over 40: size bites earlier than the L65 result suggested |
| E4 H, deltas | Between 40 and 120 delta lines over 27 removals; the largest single removal changes at most 12 facts | Over 150, or a single removal over 20 |
| E5 what the mode misses | On H, none of the seven chain steps shows up in the consequences at all, because the driver tests SINCE and the consequences program asks only what holds. So a consequences report on an argument shows what the writer is committed to and says nothing about whether the argument connects. The two modes need each other; neither replaces the other | A SINCE step visible in the derived list |
| E6 time | Each ledger under 3 minutes | H over 10 minutes |

## Not tested
WITHDRAW and MAKE NOT SO; rig 2; any reader.

## Traps
- Editing this file after the runs.
- Reading H's derived count as "more consequences means more useful". What matters is whether a reader would want them, which this plan does not test.
