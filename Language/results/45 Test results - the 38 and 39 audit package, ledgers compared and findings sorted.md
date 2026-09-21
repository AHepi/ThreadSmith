# 45 Test results - the 38 and 39 audit package: ledgers compared, findings sorted

Plan: file 45, frozen 21 September 2026, unchanged. Run by a worker, OpenAI Codex, from the handoff L60; its return is kept whole at "L62 Return - plan 45 run by OpenAI Codex" (1,145 files, every hash in its manifest checked here). Checked by the orchestrator: the manifest; the source identity (the 194 files it was given, byte for byte the handoff); its s(CASP) 1.1.4 on SWI-Prolog 9.0.4, the same as here; and eight of its Part B runs repeated on this machine's rig, reports the same to the word once timings are set aside ("45 Reruns by the orchestrator"). What is marked **seen** below was seen here or in its preserved raw logs; **read** is from the files; **worked out** follows from those.

Translator for Part A: OpenAI Codex, not Claude. Standing convention: the fixture as the actual ledger, TOLD only for a story or report inside the text (the choice of file 46; the owner has not yet decided).

## Part A - six ledgers, line by line

| Text | The plan expected | What happened | Prediction |
| --- | --- | --- | --- |
| All six | Same facts, different standing, on every held line | **Seen.** Every shared line differs in standing (TOLD in a fixture world against CLAIMED or GIVEN). But not every line is shared: T02-B has one line only the other model wrote. So the prediction holds for shared lines and fails as a whole | Partly wrong |
| T02-B | Four both; "Mara's description" only theirs; none only new | **Seen.** Four both (kingfisher, feathers, belong, unharmed); only theirs: "feathers were the subject of Mara's description of their colour"; none only new. The worker binned the description as who-describes-what, as the plan said Claude would | Right |
| T02-D | One line differs in kind: a filled-in Result "as a result of happening p" on the new side | **Seen.** All seven lines match as content; no Result was written; "when" was read as time, not production, and both burnings kept as Facts | Wrong |
| L09 | Both empty | **Seen.** Both empty; the line in both bins | Right |
| N03-A | Identical: two said, one filled in | **Seen.** Three both (pear; yellow skin; red colouring filled in); no only-lines | Right |
| N03-B | Same happening and things; one only theirs if it kept the meta-sentence | **Seen.** Five both, none only; both sides binned "The text states the contact". The conditional did not arise (the plan wrote it without looking; Lesson 51) | Right on the core |
| N05-A | Both empty | **Seen.** Both empty; both bins keep the denied belief whole | Right |

The comparison was made with tools/sameness.py, which compares wording and says so; the worker's hand decisions on the "only" and "near" lists are in its `part_a/sameness/HAND_DECISIONS.md` and were read here: every "near" was one fact in two wordings; the one "only" line in T02-B is a real extra commitment. Bin-entry counts differ only by bookkeeping (one entry per sentence against one prose entry).

**Failure of the language:** none. The two easy cases, N03-A and L09, gave the same content on both sides. **Failure of the comparison:** none; the standing difference did not swamp the test, because the program lists standing separately.

**What Part A shows, and no more:** on six texts both translators had already seen, two translators working from 38 and 39 wrote the same content in five of six, and the sixth differed by one line. It is not blind (the worker read the other model's six once before translating, as the brief required, and says so), so it is not evidence that 38 and 39 fix a ledger for an unseen translator. That test needs unseen texts and a translator who has read no ledger.

## Part B - the fifteen findings sorted after the runs

All 48 prepared texts were translated or given a written disposition; 50 driver runs and 149 direct queries were made, on the frozen and the patched copies. Sorting is by the patched rig's output; the frozen copy is history. The rows the orchestrator ran again here are marked "rerun".

| Finding | What the rig said | Pile | The plan's prediction |
| --- | --- | --- | --- |
| F01 exception against ALWAYS | No run: translation stops at rule 12. **Read**: 38 line 51 promises the exemption report; rule 12 and 39 forbid the line | 1, wording | Right |
| F02 embedded content as TOLD | **Seen**: N05-A empty on both sides; N06 kept desire and disbelief in the bin | 1, a guard on 39 line 30 | Right |
| F03 a chosen reading | No run: readings kept in "Readings I chose" and the bin | 1, wording | Right |
| F04 a Result needs a producer | **Seen, rerun**: N14-A, "the box moved away from the wall", written as a Fact; NO FAULT FOUND; the movement never reaches the laws. N15-A/B keep the causal relation but no Result either | 2, held if 38's promise to check stated movement covers movement with no producer; else a declared scope | Right on the translation; the control is weaker than predicted |
| F05 enabling is not achieving | **Seen**: N17-A is HELPS (the text says "assisted"), no tendency stated; rig 2 reports the word rests on something nobody stated; the gate stays shut; nothing false | 3 | Pile right; the mechanism (LETS against a stated tendency) wrong, as Lesson 51 said before the run |
| F06 MAKES with a prior tendency | **Seen**: N16-A on rig 2: THE WORD DOES NOT FIT THE SLOTS for MAKES with the tendency stated; rig 1 stores the ordinary-production sentence as a Fact and does not assess it | 3, with the owner's decision on R06 | Pile right; wording of the report wrong |
| F07 the offered route and the endpoint | **Seen, rerun**: N19-A: the press route holds, the flag-to-bell reason is NO CONNECTION and "doing no work", the conclusion STANDS by the other route. The rig already keeps them apart. N20-A: the conclusion stated first is printed as the final conclusion, because the case has only one SINCE step; it did not reproduce patch 7's give-up | N19: no pile. N20: 3, only because patch 7's give-up is logged | N19 wrong (predicted a circle and a wording fix); N20 not forced by this case |
| F08 the added-lines test is silent | **Seen, rerun**: silent on N23-A and on N23-B. B has no claimed conclusion for patch 10 to test; the writer of N23-B claims nothing, so nothing is taken out and asked again | 3, a logged give-up | A right; B wrong: the case as written cannot fire patch 10 |
| F09 an actual observation in a what-if | **Seen, rerun**: N25-A: "MAKE NOT SO: pushed(box)"; the box "still moved" because the actual line "the box moved after the push" is not tied to the push; the what-if HOLDS. The right answer under 38 is "cannot tell". N25-B, with the source's own no-push account, FAILS and a contradiction is reported between the actual movement and the supposed one | 2 | Right; the layer (the what-if rule, or the translator writing "after" as a Fact) is open |
| F10 only-ways | **Seen**: T27-B, both gates open, no contradiction, no alternative picked | 1, say SHOWS | Right; T26 not run |
| F11 one event, several mentions | Translation only: one happening, repetition in the bin; N29-B two happenings | 3, a translator note | Right |
| F12 a mentioned goal | **Seen**: N22 has no SO THAT in the text, so no plan claim was written and "cannot tell" was never asked. Direct queries: achieves(turn(dial), kept_cool(pear)) answers in both A and B, because the rig's achieves means only "changes a slot the goal depends on" | 1, write the MENTION form and say what achieves means | Pile right; "cannot tell" wrong, as Lesson 51 said before the run |
| F13 a clean report is not coverage | No run. **Read**: 38 lines 17, 44 and 113 already say a clean report means the lines fit and name what is unchecked | 3, already declared | Wrong (predicted wording, pile 1) |
| F14 a verb with no object | **Seen**: N30-A "the bell rang" as a Fact, nothing found; N30-B on rig 2: "Verbs with no shape: ring" | 3 | Right |
| F15 a BECAUSE and its exact denial | **Seen, rerun**: N18-A: the BECAUSE is a JUMP (nothing makes fleaming produce opening); the NOT [BECAUSE] is "Fine"; **no contradiction between them** though they share effect and cause. N18-B (denial only): nothing, correctly | 2 | Right |

**The sort.** Pile 1, wording: F01, F02, F03, F10, F12 (five; the plan said seven). Pile 2, a change indicated: F04 (held-if), F09, F15 (three; as predicted). Pile 3, declared or already logged: F05, F06, F08, F11, F13, F14, and F07's N20 branch (seven; the plan said five). No pile: F07's N19 branch. Fourteen of fifteen piles as the run gave them; twelve of fifteen as the plan predicted; four mechanisms wrong where the pile was right.

**Failure of the audit:** none. No finding dissolved on a run. **Failure of the language:** F15 and F09, both confirmed by runs and both repeated here. A ledger of legal lines can hold a stated cause and its exact denial and the checker reports no clash; an actual fact written as a Fact rides into a what-if untouched, so the what-if holds when the ledger cannot say.

## What the worker found that the plan did not ask
- Every historical run and every new one carries s(CASP) "predicate does not exist" errors for the questions the driver asks of every ledger (BECAUSE claims, plans, likenesses, exemptions) when the ledger has no lines of that kind: 8 of 12 sections in the recorded T05-B run, 640 of 2,085 sections in the whole historical log (**seen** here). The driver counts them as "no such claims", by design since log 07, and prints NO FAULT FOUND; the report does not say which questions were answered and which were never asked because nothing was there to ask. The worker declined to read any such report as a clean answer, which is stricter than the rig's convention and right about what the report shows. Recorded as Lesson L2.
- The rig has no two-ledger entry point (Lesson 52); the worker used tools/sameness.py and judged the rest by hand, as the brief asked.
- Rig 1's what-if on N25-A takes "the box moved after the push" as invariant because nothing ties it to the push; the language has no form for "after" that the what-if can see.

## Not tested
- A blind translation: both translators had seen the other's six, or the texts.
- Any translator that has not read a ledger; any unseen text.
- The 324 receipts; T21, T26, T39, T61, T76 and the F13 cases were not run (documentary by the worker's pre-registered matrix).
- R06 and R12, the owner's choices; the candidate 39.
- Any pile-2 change. None was built; the round ends at the sort.

## Traps
- Reading NO FAULT FOUND without the raw log. The report cannot tell "checked and fine" from "nothing of that kind to check".
- Reading Part A as agreement between independent translators. It is reconstruction after reading.
- Fixing F09 in the what-if rule before deciding whether "after" is a translator's problem. The layer is open.
- Counting the piles. They are a sort, not a score.

## PARKED, for the owner
- The fixture: actual ledger or TOLD world. Both sides differ on every shared line for this reason alone.
- R06: the narrow force-dynamic MAKES against ordinary production.
- F04's scope: does 38 promise to check a stated movement that names no producer?
- The first pile-2 change: F15 is the cleanest forcing case (N18-A; control N18-B must stay silent). Built only on the owner's word, with what it gives up.
- The driver's report should name the questions it could not ask.
