# 35 Test plan - the third pile

Written before building. Not edited afterwards.
Authority document: "Claude Fable Semantics - standalone theory" (file 10). Design drawn on: the other model's repaired rulebook V3 (unrun).

## What gets built, and the case for each
| Feature | Forcing case | I expect |
| --- | --- | --- |
| Named what-if cases: supposed lines belong to a named case and stay out of the actual ledger | F06: the door is said to be open and not open; a what-if supposes the bell rings | The door contradiction is reported once, as already there. Under "the bell rings": no new contradiction |
| Two rival cases | F09: one case supposes the door open, another supposes it not open | No contradiction in either, and none between them |
| The Mondays paragraph, with "Monday is gone" as a named case | ledger H | The contradiction moves out of the main report and appears under the supposition, as the supposition undoing itself. The chain verdict stays the same |
| Results set aside when their cause is changed | F22: push, box moved, "moved BECAUSE pushed"; what-if withdraws the push | "Without the push the box would not have moved" HOLDS. Before the change it would wrongly fail, because the line "the box moved" stays |
| MAKE NOT SO on a fact other lines produce | my hostile case KX (balcony plants) | The rig declines to run it and names the lines that still produce the fact |
| NOT on part of a line: a denied BECAUSE | F08: the jar broke, NOT because it was dropped | Fine when no line makes dropping produce breaking. Flagged when the ledger's own MAKES line supplies exactly that |
| The same fact at different stages | F17: door open in the morning, not open in the evening | With the stage in the fact's name: no contradiction. With it left out: a false contradiction. So this one is a rule for the translator, and needs no rig change |
| Joining the two rigs (rule 11) | the ball paragraph with two BECAUSE lines | "Sally was thrown backwards BECAUSE she threw the ball": jump, since the laws of pressing will not produce it. "The ball moved toward the wall BECAUSE she threw it": follows, and the cause does work |

## What would count as failure
Any forcing case coming out otherwise; any earlier ledger's report changing, apart from ledger H in the way stated above; any question over 20 seconds.

## Likely ways these patches will fail later
Named cases: a case inside a case. Set-aside results: a result with two causes, only one of them changed. Denied BECAUSE: a denial of a SINCE. Joined rigs: a BECAUSE whose effect is a change of state, since the laws only know movement.

## Traps
- Editing this file after the runs.
