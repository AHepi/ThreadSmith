# L77 Table for the owner - what each check computes and what its report claims

Drafted 22 September by the orchestrator from the driver's code (`rigs/rig 1 - arguments/patched/run_check.py`, the line numbers given), at the request of review A2 (L76): before any check is patched, say for each which question it computes, which its report claims, and whether it is asked inside a told world and inside a supposed case. The owner strikes and adds; the struck version is the contract term that L64's next version carries beside section 4. Nothing is built until then.

| Check (code) | Question the code computes | Question the report's words claim | Asked in the actual ledger | Asked inside a told world | Asked inside a supposed case | Gap, if any |
| --- | --- | --- | --- | --- | --- | --- |
| 1 contradictions (:79) | is any fact both held and denied among the non-case lines, and which smallest line set gives it | "these lines cannot all hold" | yes | no (patch 12 asks it there, separately) | no (patch 12, separately) | none |
| 2 BECAUSE claims (:95) | does some general line make the cause produce the effect, with the claim line and directly stated effect removed; circle and idle tests | FOLLOWS / JUMP / CIRCLE / IDLE CAUSE, as claims about the writer's reasoning | yes | **no** | **no** | finding 1: a reported argument is never tested; the report says nothing, and the header then reads NO FAULT FOUND |
| 2b SINCE claims (:140) | does the ledger connect the reason to what is expected | "reason to expect ... NO CONNECTION" | yes | **no** | **no** | same as check 2 |
| the chain (:165) | which SINCE/BECAUSE steps hold and whether the last conclusion stands | "the final conclusion stands / does not stand" | yes | no | no | same |
| 3 plans (:190) | does doing the action change something the aim depends on | "cannot work / kind mistake / cannot tell" | yes | no | no | as above; and CANNOT TELL prints no lines to trace |
| 4 exceptions (:217) | an exception to a USUALLY line with no reason | "departure from the usual, no reason given" | yes | no | no | |
| 5 likeness (:233) | shared slots between two events; fitted to paragraph F | "these two events are alike in ..." | yes | no | no | patch 5 has no give-up entry in the record |
| patch 8 two USUALLY (:249) | two usual-case lines give and deny one fact | "pull opposite ways; settles nothing" | yes | no | no | |
| patch 9 exemption (:259) | an exemption aimed at an ALWAYS line | "exemption from an ALWAYS line" | yes | no | no | |
| patch 10 added lines (:265) | does the conclusion follow with every said line removed | "added lines alone give the conclusion" | yes | no | no | |
| patches 11, 13 what-ifs (:274) | with the change made and every effect *tied to it by a BECAUSE claim* set aside, does the asked fact hold | "your what-if HOLDS / FAILS", the tie stated as "your ledger says they came from what was changed" | yes | no | no | finding 2: the tie is taken from a BECAUSE whatever check 2 said of it, and the report does not say so; the filled-in note 38 line 113 promises is never printed here; F09 runs through the same function |
| patch 14 denied BECAUSE (:300) | does the ledger produce the effect from the denied cause | "you deny a cause your own lines supply / fine" | yes | no | no | F15: the matching positive claim is never looked for |
| patch 12 named cases (:310) | inside each world, looked at alone, is any fact both held and denied | "inside a told world: no contradiction / under the supposition: contradiction" | - | contradiction only | contradiction only | finding 1 from the other side; and the contradiction branch prints supposition wording for a told world |
| the header (:334) | does the report text contain any of a fixed list of finding words | "NO FAULT FOUND in the lines that were checked" | - | - | - | finding 5 (A2): it cannot tell checked-and-passed from never-asked; RAN OUT OF TIME and CANNOT TELL are not in its list |
| the gauge (:329) | count of marks; `len(leftover)` over `len(sentences)` | "N of M sentences went to the leftover bin (not checked)" | - | - | - | the numerator is bin entries, not sentences; a sentence with no line and no entry reads as checked (T10-B) |
| consequences.py | every binding of ten queries over all lines pooled, minus clause heads whose body is exactly `line(N)`; one line removed at a time | "derived (not stated by any line)"; "nothing changes" | pooled | pooled | pooled | finding 4; stated facts by regex miss general lines and second notations; "nothing changes" means "no change in the reported fact set" |

## Three questions the owner answers by striking
1. Inside a told world and inside a supposed case, which of the checks above are asked? The reviewers' recommendation: all of them, looked at alone, with a finding that would need a line from outside the world counted in the gauge rather than reported.
2. What does a what-if answer: the world, or the ledger with the writer's stated causes taken at their word? The reviewers' recommendation: the second, printed as such, with the tie, its verdict and any filled-in line named.
3. What replaces NO FAULT FOUND: named outcomes per check (asked and clean; not asked, because the ledger has no such line; ran out of time), or the header with the list of kinds never asked appended?

## Traps
- Reading "no" in the told-world column as a fault of the code. 38 line 105 promises only a contradiction inside a told world; the code keeps 38. The fault is between 38 and L64's tables, and this table is where it is settled.
