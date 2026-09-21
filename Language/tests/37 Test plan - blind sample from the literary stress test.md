# 37 Test plan - blind sample from the literary stress test

Written before translating or running anything, and before opening any of the package's annotations. Not edited afterwards.
Authority document: "Claude Fable Semantics - standalone theory" (file 10). Language under test: file 36.

## What the package is
Made by the other model. 324 short inputs: 20 public-domain literary excerpts, 80 case families of three texts each, 16 late challenges, 48 probes. Inputs and answer keys are in separate files. It says it never had file 36, used its own rewritten rulebook as a stand-in, and ran nothing. Its two scripts were not run by me.

## The sample, and how it was chosen
Four case families, the base text and its contrasting text from each: T05, T07, T10, T11. Chosen from the first twelve families by reading texts and questions only, because they sit inside what file 36 claims to cover: mention against fact, a told story against the room, achieved against caused, a reason to conclude against a producer. Eight texts. These are someone else's cases; the translating is still mine.

## What I expect
| Text | I expect from the checker |
| --- | --- |
| T05-B note says "Open the gate"; gate stayed shut | Nothing found, and nowhere is the gate said to have opened. The command itself goes to the bin |
| T05-D same note; Ada opened the gate | Nothing found; the opening is a plain fact |
| T07-B Nora's story has the door open; in the room it stayed shut | A FALSE ALARM. I will write the story as a named case, and named cases sit on top of the actual ledger, so the checker will report a contradiction under "Nora's story". A story should not inherit the room |
| T07-D same door, same moment, open and not open | Contradiction, correctly |
| T10-B opened the window to keep the letter dry; it stayed dry; no reason given | No causal finding at all, since the writer makes no causal claim. The plan check may complain that nothing links window to dryness |
| T10-D the account says opening the window caused the dryness | "Jump": a BECAUSE with no line that MAKES. Arguably too harsh for a bare statement of cause |
| T11-B the lamp was the inspector's reason for concluding; it was not what made the visitor return | The denied BECAUSE comes out fine. The SINCE comes out "no connection", since no general line is given. That the reasoning is the inspector's goes to the bin |
| T11-D the lamp drew the visitor back | "Jump", as T10-D |

## What would count as failure of the language or the rig
The gate counted as opened in T05-B. No contradiction in T07-D. A cause asserted by the checker in T10-B. The lamp accepted as producer in T11-B.

## Traps
- Editing this file after the run, or reading the annotations before it.
