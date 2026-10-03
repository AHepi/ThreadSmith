# S93: reading of the replies

*Written by a Claude subagent for the orchestrator on 25 September 2026, after every checker had ruled, under rule 7 of `results/S93 How the cross-examination of draft 4 will be read - written before sending.md` ("the reading rule", md5 f1da3d1941499e0a8e6388a046275a0f; "rule n" is its paragraph n). It records all eighteen items and applies the rulings to the change list (rule 12), which makes draft 5 of revision 2. It read the reading rule; the tabulation, `results/S93 Tabulation of the replies, before any ruling.md` (md5 739d4d6bccc83caa03589bd45d030396: its header, section 1, section 2.1, section 4, sections 6 and 7, and the opening of section 3); the ten ruling files in `results/S93 reading rulings/`, whole; the change list, the revision note and `tools/s89_apply_changes.py`. It opened no S93 reply, receipt, request, reasoning or attempt file, and not the session's key file. It wrote no ruling. Nothing was written into `authority/`. Line numbers are draft 4's (`tests/Revision 2 - file 13 draft 4, theory text.md`) unless marked "file-11".*

## 1. What was sent

Eighteen items, X01 to X18, in the order of the text: the ten entries the S90 checkers fixed (W37.1, W19.1, W35.1, W35.2, W20.1, W40.1, W24.1, W22.1, W6.3, W7.5), the six draft-4 entries (W38.1, W36.1, W34.1, W33.1, and W59.1 as two items, "Rivals" and "Problems"), and one proposed WORDING entry not yet made (X11, the pole sentence at L325). They went in eleven part briefs, A to K, each to Atria (`Atria-Dawn-Preview`) and to Mimo (`mimo-v2.6-pro`), whole, as one user message with no system text: 22 calls, effort medium. The briefs withheld every W-number, every REASON, CHECK, GAIN and LOSS, and the drafters' expected direction on each case (the reading rule, "What is sent").

## 2. Receipts

All 22 calls were accepted on pass 1 (rule 8): every receipt has finish "stop" and pass 1, and every response file ends `END OF REPORT` (the tabulation, section 1). Several calls needed more than one attempt inside pass 1: attempts with no HTTP status (a connection failure, not an answer) came before the accepted one for Atria A (three), C, D, F, I and K (three); Atria E's first attempt ran to the length ceiling with no content and was not read. No item is "not examined" by either model.

## 3. How the items were read

Ten items were challenged under rule 3 and went to one fresh Claude checker each (rules 4 and 5): X03, X04, X05, X06, X09, X10, X11, X14, X17, X18. Eight were challenged by neither reply, and where verdict words were asked the two replies' words agree; they went to no checker and are recorded as **upheld by both readers; not thereby confirmed** (rules 2 and 5): X01, X02, X07, X08, X12, X13, X15, X16. No reply disputes a fixed verdict (the tabulation, section 5; rule 10). A challenge counts as upheld only when its checker rules FIX or DROP (rule 4).

Every ruling file ends with its ruling line, and each was committed once. X09's and X10's files carry "Rivals" and "Problems" in their names, at the orchestrator's instruction, where the tabulation's section 7 gives "ruling S93 X09 W59.1.md" and "ruling S93 X10 W59.1.md".

## 4. The eighteen items

"A" is Atria and "M" Mimo; the closing lines are as the tabulation gives them. The ruling files are in `results/S93 reading rulings/`.

| item | entry | place (draft 4) | kind | part | closing lines A / M | outcome | ruling file (md5) |
|---|---|---|---|---|---|---|---|
| X01 | W37.1 | Part 0, L13 | ORDER | F | UPHELD / UPHELD | upheld by both readers; not thereby confirmed | none |
| X02 | W36.1 | Part I, L69 | CLAIM | D | UPHELD / UPHELD | upheld by both readers; not thereby confirmed | none |
| X03 | W19.1 | Part II, L119 | CLAIM | F | UPHELD / CHALLENGED | **FIX** | `ruling S93 X03 W19.1.md` (ca75c0085d1835cae3a2ca88ba1e9136) |
| X04 | W35.1 | Part IV, L217–221 | CLAIM | G | UPHELD / UPHELD | **KEEP**, with a companion entry W35.5 and a bookkeeping edit to W35.1's REASON | `ruling S93 X04 W35.1.md` (b82f1d1c8dd2ac7c4a363c834d283f07) |
| X05 | W35.2 | Part IV, L223 | CLAIM | G | UPHELD / CHALLENGED | **FIX** | `ruling S93 X05 W35.2.md` (74b825b2d3c40fdbf58442a7402a8e31) |
| X06 | W20.1 | Part V, L231 | CLAIM | H | UPHELD / CHALLENGED | **FIX**, with three record edits | `ruling S93 X06 W20.1.md` (aa9a21e9b55e2138f2b66a840470ca3c) |
| X07 | W34.1 | Part VI, L313 | CLAIM | D | UPHELD / UPHELD | upheld by both readers; not thereby confirmed | none |
| X08 | W33.1 | Part VI, L313 | CLAIM | D | UPHELD / UPHELD | upheld by both readers; not thereby confirmed | none |
| X09 | W59.1, "Rivals" | Part VI, L315 | CLAIM | A | CHALLENGED / CHALLENGED | **FIX** (NEW and DECLARATION) | `ruling S93 X09 W59.1 Rivals.md` (f92389a295496d37c00b530b0b6c61dd) |
| X10 | W59.1, "Problems" | Part VI, L317 | CLAIM | B | UPHELD / UPHELD | **KEEP** | `ruling S93 X10 W59.1 Problems.md` (ae10f9be471c1e1546eab6197c15d088) |
| X11 | proposed | Part VII, L325 | proposed WORDING | I | UPHELD / CHALLENGED | **FIX**: entered as a new entry, W61.1, KIND CLAIM, with a declaration | `ruling S93 X11 proposed.md` (38c477ab95ba986fc16c8719e76c3188) |
| X12 | W40.1 | Part VII, L339 | CLAIM | I | UPHELD / UPHELD | upheld by both readers; not thereby confirmed | none |
| X13 | W24.1 | Part VIII, L353 | WORDING | J | UPHELD / UPHELD | upheld by both readers; not thereby confirmed | none |
| X14 | W60.1 | Part VIII, L369 | CLAIM | C | UPHELD / UPHELD | **KEEP** | `ruling S93 X14 W60.1.md` (7db95a43415b4b09c95ded7a013fd78b) |
| X15 | W22.1 | Part IX, L377 | CLAIM | J | UPHELD / UPHELD | upheld by both readers; not thereby confirmed | none |
| X16 | W6.3 | Part XI, L455 | CLAIM | K | UPHELD / UPHELD | upheld by both readers; not thereby confirmed | none |
| X17 | W7.5 | Part XIV, L526 | CLAIM | K | UPHELD / CHALLENGED | **FIX** | `ruling S93 X17 W7.5.md` (d0dd8a27c934fa5c6255422826ca66d9) |
| X18 | W38.1 | the note of sources and departures | META | E | CHALLENGED / CHALLENGED | **FIX** (one line) | `ruling S93 X18 W38.1.md` (2a440ee25b144a65e12484a3eeacdc36) |

In all: **7 FIX** (X03, X05, X06, X09, X11, X17, X18), **3 KEEP** (X04, X10, X14), **no DROP**, and **8 upheld by both readers** (X01, X02, X07, X08, X12, X13, X15, X16). X04 went to its checker although both closing lines read UPHELD, because Mimo's point 2 showed an unchanged sentence made stale (rule 3); X10 and X14 went for a disagreement on verdict words or for optional wordings (rules 3 and 5).

**OVERALL lines.** Atria: NEEDS REPAIR in parts A and E, SOUND in the other nine. Mimo: NEEDS REPAIR in A, E, F, G, H, I and K, SOUND in B, C, D and J. A count settles nothing (rule 5).

## 5. Verdict words, by model and item (rule 6)

"–" means the question was not asked of the item in its part; in parts G, I and K, (a) was asked only as a point, and the reply's words are given.

| item | (a) A / M | (b) A / M | (c1) A / M | (c2) A / M | (d) A / M |
|---|---|---|---|---|---|
| X01 | – | – | – | – | – |
| X02 | FAITHFUL / FAITHFUL | – | – | – | – |
| X03 | – | – | – | – | RIGHT / RIGHT, WITH A LOSS |
| X04 | point: "faithful to, or merely neutral" / point: "Faithful" | – | – | – | – |
| X05 | as X04 | – | – | – | – |
| X06 | – | – | – | – | RIGHT / RIGHT, WITH A LOSS |
| X07 | FAITHFUL / FAITHFUL | – | – | – | – |
| X08 | FAITHFUL / FAITHFUL | – | – | – | RIGHT / RIGHT |
| X09 | FAITHFUL / FAITHFUL | – | – | UNSETTLED BY THE TEXT / UNSETTLED BY THE TEXT | RIGHT / RIGHT, WITH A LOSS |
| X10 | FAITHFUL / FAITHFUL | – | HARMLESS / HARMLESS | UNSETTLED BY THE TEXT / ESTABLISHED | – |
| X11 | point: no bearing / point: "no new (a) issue" | – | – | – | – |
| X12 | point: "not engaged and is not violated" / point: "consistent" | – | – | – | – |
| X13 | – | – | – | – | – |
| X14 | FAITHFUL / FAITHFUL | HOLDS AS STATED / HOLDS AS STATED | – | UNSETTLED BY THE TEXT / UNSETTLED BY THE TEXT | – |
| X15 | FAITHFUL / FAITHFUL | – | – | – | – |
| X16 | point: "Not applicable" / point: "Faithful" | – | – | – | – |
| X17 | point: "Faithful" / point: "Faithful" | – | – | – | – |
| X18 | FAITHFUL / FAITHFUL | – | HARMLESS / HARMLESS | – | – |

No reply returned NOT FAITHFUL, FAILS, DEFECT or SAY DIFFERENTLY on any item. No reply found a listed set, a count of versions, a grade or a record brought back, and no checker's fix brings one back (each ruling says so).

## 6. The rulings, and the exact wording of every fix

Each FIX is made in its entry of the change list, its ruled texts cut from the ruling file by script, byte for byte (checked again by program after the edit; section 7). Each item's line in its entry's CHECK field begins "S93 cross-examination:", in the checker's words where a checker ruled; for the eight items no reply challenged it reads "S93 cross-examination: upheld by both readers (s93_xexam_atria_<part>, s93_xexam_mimo_<part>); not thereby confirmed.", with the item's part. The full texts are in the rulings and in the entries; the changed words are given here.

**X03 · W19.1 · FIX.** Mimo's challenge 2 upheld: NEW reported Derivation 1 for "a component", where Derivation 1 and (F1) speak of "every active component" (L554, L233). In NEW's last sentence, "Derivation 1 makes the like comparison between a component \(k\) of \(E\)" becomes "Derivation 1 makes the like comparison between an active component \(k\) of \(E\)" (NEW grows from 131 to 132 words). In the declaration, "between a component, read through its transport, and its anchor, read on C directly with its hidden ports projected away." becomes "between an active component, read through its transport, and its anchor, read on C directly with its hidden ports projected away, up to the port translation." KIND CLAIM unchanged. KEEP on the challenges of index and value identification and of classes across candidates. The ruling's own CHECK line is used.

**X04 · W35.1 · KEEP.** OLD, NEW, KIND and DECLARATION stand. Mimo's point 2 is upheld as a finding, not against the item: after W35.1, Derivation 4's proof (L582, file-11 L572) still reports the old third bullet, "Surprise is defined as a violation at \((a,b)\notin H\).", and reaches its Claim's "selected" only through the typing of \(H\). The repair is a companion entry, **W35.5**, entered as the ruling gives it, whole, after W35.4: OLD "Surprise is defined as a violation at \((a,b)\notin H\).", NEW "Surprise is defined as a violation of a selected transport at \((a,b)\notin H\).", FILE-11 LINE 572, GROUP C, REASON WORD clarification, KIND WORDING, no declaration (a fallback line is given if a checker rules CLAIM). W35.1's REASON sentence on Derivations 4 and 10 is replaced by the ruling's words: "Derivation 4's Claim and Derivation 10 are unchanged and stay true word for word. Derivation 4 reads "A system can be surprised only if it holds a transport selected on a history H …". Its proof read "Surprise is defined as a violation at (a,b)∉H", which reports the old third bullet; after the S93 cross-examination the companion entry W35.5 brings it to the new one."

**X05 · W35.2 · FIX.** Mimo's challenge upheld: the definitions are scoped to pairs "actually occurring" (L217), while fidelity is stated at every pair of the contract. In NEW and in the declaration, "a constructed one that fails at a pair of its contract" and "a constructed transport to the simulation layer that fails at a pair of its contract" become "… fails at an actually occurring pair of its contract". KIND CLAIM and REASON WORD unchanged. KEEP on the third clause under "restating its definitions". The ruling offers one LOSS sentence "optional, to keep the record whole"; it is added as written: "After the S93 cross-examination, a constructed transport whose fidelity fails only at pairs of its contract that never occur is not called violated by this sentence; the definitions at L217–220 never called it so."

**X06 · W20.1 · FIX.** In NEW and the declaration: "including any that assigns an input" becomes "including any of them that assigns an input", so the candidate's offer decides membership for every component, as S88 settled; and "boundary values" becomes "boundary conditions", the term of L91. NEW now ends "the boundary conditions of \(E\) and the components of \(E\) outside \(\Gamma\), including any of them that assigns an input, belong to the named background of Part VI." KIND CLAIM unchanged. Mimo's exception ("never one of them"), its declaration and its repairs at L245, L299 and L558 are not taken; Atria's optional phrase is not taken. The record edits the ruling lists are made: the finding carried forward on the two readings of "including any that assigns an input" is closed, and so is REASON's matching bullet; in the finding on "active", "puts the components that assign inputs in the named background" becomes "puts the components outside Γ, including any that assign inputs, in the named background"; and in O7's CASES AT RISK, after "assigns an input and is named background", the words "where the candidate does not offer it as doing the work; offered, it is a commitment, and O7 holds on both identifications (W20.2)" are added.

**X09 · W59.1, "Rivals" · FIX.** Two small wordings.
- Ruling 2 (Mimo point 2): the illustration of conflict guaranteed only the second conjunct and could make a candidate that never meets (F1) conflict with its own rewriting. In NEW, "and no such relations let both, as when two of their active components with one anchor have different relations there." becomes "and no such relations let both, as none do when two of their active components with one anchor have different relations there." Mimo's separate disjunct is not taken.
- Ruling 4 (Mimo point 3(ii)): the declaration's third sentence becomes "Two candidates that differ only in how they are written, one carried onto the other by a structure-preserving bijection that takes its transport with it and leaves its answers as they are, or that some such relations would let both meet those conditions at each admitted pair, are not rivals."
- KEEP on the parse of "and nor do" (ruling 1), on the declaration's silence about "offered for the whole of p" (ruling 3), on "both translate" (ruling 4), on "established" and failures found by examining a candidate (ruling 5; the owner's choice, section 9), on the dependence order (ruling 6; placed by X17's fix) and on Mimo's whole replacement (ruling 7). KIND CLAIM unchanged. The declaration is shared with X10, whose ruling is KEEP, so only X09's change applies.

**X10 · W59.1, "Problems" · KEEP.** No change. Mimo's optional "For that assessor" is not needed; on (c2) Atria's "unsettled by the text" is the more exact account of what the text states, and L317 is true on either answer; the dependence order's silence is L526's (X17); Mimo F's loss is declared in the entry's LOSS.

**X11 · proposed · FIX: entered as W61.1, KIND CLAIM.** Both readers hold the change of symbol right; Mimo's challenge on the kind is upheld: OLD asserts a statement about a named port that is false in the theory's own terms, and NEW withdraws it. Under rule 4 the checker's ruling sets the kind, so the entry is CLAIM, not the WORDING of rule 12's wording. Entered between W59.1 and W40.1 (file-11 order), as the ruling gives it: FILE-11 LINE 323; WHERE Part VII, "Production and direction" (L323), sentence 5; REASON WORD erratum; KIND CLAIM.
- OLD: "The reversed calculation \(H=L\tan\theta\) is not: intervening on \(H\) changes the target's \(L\) but not the calculation's \(H\)."
- NEW: "The reversed calculation \(H=L\tan\theta\) is not: intervening on \(H\) changes the target's \(L\) but not the calculation's \(L\)."
- DECLARATION: "Part VII no longer says that intervening on \(H\) leaves the reversed calculation's \(H\) unchanged; it now says that the intervention leaves the calculation's \(L\) unchanged while the target's \(L\) changes, as Part V says of a reversed calculation."
- The id W61.1, its title, GROUP "S93", ITEM, REASON and GAIN / LOSS are this subagent's bookkeeping, taken from the reading rule and the ruling; the ruling gives no id.

**X14 · W60.1 · KEEP.** No change. The closing clause ("an account on it does not answer \(p\)") is true in the idiom of L151, L159, L161 and L253; "the exclusion" is fixed by its antecedent. The result holds as stated (ruling, "Does the result hold").

**X17 · W7.5 · FIX.** Both readers say the order stays true but places none of Part VI's new terms; the checker rules that this matters now, because L31 and Derivation 6's proof (L598) rest on the order. OLD is extended by the unchanged sentence "(RC), (U1)–(U3) depend on all of the above.", and NEW ends with it followed by one new sentence:

> In Part VI, conflict depends on (F1), (F2), (A) and the relations the adopted physics admits, rivals on conflict and on the offer of one in place of the other, what is established on usable receipts (Part IX), fits on what is established and (E), a problem for \(p\) on rivals and fits, and easy to vary on a problem for \(p\).

The declaration gains "; and it places Part VI's conflict on (F1), (F2), (A) and the relations the adopted physics admits, rivals on conflict and on the offer of one in place of the other, what is established on usable receipts (Part IX), fits on what is established and (E), a problem for \(p\) on rivals and fits, and easy to vary on a problem for \(p\)." after "ProducedBy on histories and their active routes". KIND CLAIM and REASON WORD erratum unchanged. The heading becomes "W7.5 — L518 s9–s12: Ownership, owned capability, ProducedBy and the obligations; Part VI's terms", and WHERE names the (RC) sentence. The REASON bullet, CASES AT RISK line, and GAIN and LOSS sentences the ruling suggests are added, and the first bullet of "Found in draft 4" now says the placement is made. KEEP on Mimo's (EK) omissions (\(O_{\mathrm{ep}}\), ProducesVia), on Build and (E), and on "resource contract".

**X18 · W38.1 · FIX.** In the sources note's *Surprise and problems* line, "a conflict in which meeting a claimed obligation fails a protected one" becomes "a conflict in which what the system holds meets a claimed obligation only by failing a protected one", L429's words (Mimo points 1–2). KIND META; DECLARATION and OLD unchanged. KEEP on the *Reach* pointer "(Parts I and VI)", which both readers asked to change (the note's clause stands in Part VI), and on the *Hard to vary* application (Atria point 2). The note changes; the theory text does not.

## 7. The change list, draft 5, and the build

The change list keeps its file name (`tests/Revision 2 - change list, draft of 23 September.md`); its frame now says it is draft 5. Besides the fixes above, the frame is brought up to date (the header, the italic record, What this is, Counts, a section "After the cross-examination (S93)" in "What the checks changed", the held items, and a new section "Carried forward after S93"). The revision note is regenerated as the draft-4 pass did it: section 1 from the program's NOTE block, section 2's last column from the program's layer-2 table, section 5's map rebuilt in file-11 order with a column for S93, the other sections edited in place.

**Bookkeeping, 25 September 2026.** W34.1's and W59.1's CASES AT RISK wrote "N7 (O59)"; under D8 N7 is O58 and O59 is N8 (the reading rule noted the slip). Both now read "N7 (O58)", each with a dated note. The draft-4 pass record (`tests/Revision 2 - hard to vary restated through rivals and problems, 25 September.md`, its table row "N7 (O59, two bakers)") is left as the record of that pass.

**Counts, draft 4 → draft 5.**

| | draft 4 | draft 5 |
|---|---|---|
| entries parsed | 65 | 67 |
| applied (theory + meta) | 60 (57 + 3) | 62 (59 + 3) |
| record-only / held | 5 / 0 | 5 / 0 |
| CLAIM / WORDING / ORDER | 51 / 4 / 2 | 52 / 5 / 2 |
| the note: N of M; K | 51 of 57; 42 | 52 of 59; 42 |
| by group | A 14/18, B1 14/15, B2 11/11, C 10/11, H 2/2 | A 14/18, B1 14/15, B2 11/11, C 10/12, H 2/2, S93 1/1 |
| diff hunks against file 11 | 55 | 57 |
| theory text md5; words (runner / `wc -w`) | fc55b470c63cd4b3c27d6aa64d8d8c17; 12,577 / 12,549 | 7f1d8ad02adf96e27622593bd263252e; 12,650 / 12,622 |
| full draft md5; words (runner / `wc -w`) | 57c94ab5f0bada4e9443904253dc2db3; 29,864 / 29,820 | 40cefd9b586f43762e0a58c54e843cb0; 30,426 / 30,382 |

The program's numbering (layer 1) places W61.1 at R2-26 and W35.5 at R2-56: W40.1 to W17.3 move up one (R2-27 to R2-55), and W7.6, W10a.1 and W19.3 + W10(b).1 two (R2-57 to R2-59). No layer-2 place moves between "changed", "kept with text beside it" and "kept".

**The build.** `python3 Semantics/tools/s89_apply_changes.py <scratch>/d5_full.md --theory-output "Semantics/tests/Revision 2 - file 13 draft 5, theory text.md" --date "draft of 25 September 2026, not frozen" --self-test` ran with no refusal: every OLD, locator and anchor occurs once in file 11, no applied OLDs overlap, the result is file 11 with exactly the listed replacements, every diff hunk lies inside an entry, the cut of the three meta blocks gives back the theory text, no withheld word, no slot left, and both planted edits were refused. The theory text of draft 5 is committed as `tests/Revision 2 - file 13 draft 5, theory text.md`; draft 4's file is unchanged. Two cross-checks agree with the checkers' own in-memory builds: W35.5 alone on draft 4 gives theory md5 5f7888dba8be366f5caed39672bdd096 (the X04 ruling), and the X17 fix alone gives f7fb94d3ad26c089c6abbf60b83baf67 (the X17 ruling).

**Draft 4 → draft 5, the theory text, by program.** Seven lines differ and nothing else; each hunk lies inside exactly one entry a ruling changed (checked against the entries' positions in the built text):

| draft-4 line | entry | ruling | words |
|---|---|---|---|
| 119 | W19.1 | X03 | "a component \(k\)" → "an active component \(k\)" |
| 223 | W35.2 | X05 | "fails at a pair" → "fails at an actually occurring pair" |
| 231 | W20.1 | X06 | "boundary values" → "boundary conditions"; "including any that" → "including any of them that" |
| 315 | W59.1 | X09 | "as when two of their active components" → "as none do when two of their active components" |
| 325 | W61.1 | X11 | "but not the calculation's \(H\)." → "but not the calculation's \(L\)." |
| 526 | W7.5 | X17 | one sentence inserted after "(RC), (U1)–(U3) depend on all of the above." (62 words) |
| 582 | W35.5 | X04 (companion entry) | "a violation at" → "a violation of a selected transport at" |

X18 changes only the note of sources and departures, which is a meta block and not part of the theory text. In the full draft the three meta blocks differ as they must: the NOTE block (the count sentence, five changed declarations and W61.1's new line), the SOURCES block (the one line of X18) and the RECORD (layer 1 renumbered, with W61.1 and W35.5, and the changed texts; layer 2's last column renumbered). The program also confirms that the change list's entries differ from draft 4's only in W19.1, W35.2, W20.1, W59.1, W7.5 and W38.1, with W61.1 and W35.5 added, and that each ruled text stands byte for byte as its ruling gives it. The scripts are in `tests/Revision 2 - S93 rulings applied - scripts/`.

## 8. X17's sentence, re-read against the X09 and X10 rulings

The X17 checker had not read the X09 and X10 rulings and asked that its sentence be re-read against the fixed L315 and L317 before the edit (its finding 5). Re-read:
- X10's ruling is KEEP: L317 is unchanged, so "a problem for \(p\) on rivals and fits" and "easy to vary on a problem for \(p\)" rest where they did.
- X09's fix changes two things. In L315 the illustration "as when" becomes "as none do when"; it now illustrates only the second conjunct of conflict ("no such relations let both") and adds no condition and no base. Conflict still rests on answers (under (A)), on (F1), (F2) and (A), and on the relations the adopted physics admits; the illustration's "active components with one anchor" are Part V's commitments and Part IV's anchors, which (F1) already uses. The declaration's third sentence gains the bijection clause for candidates that are not rivals, a consequence the text already stated (Derivation 8), not a base of any defined term.
- Neither ruling touches "offered", the physics' quantifier, the receipt clause, (K3)'s caveat or "fits".

So X09's fix does not change what L315's and L317's terms rest on, and X17's sentence stands as ruled.

## 9. For the owner

Rule 6: a finding that is a choice for the owner is recorded with both replies' reasons; the checker says only whether the present wording states the matter truly. Each checker that met these says it does.

**(c1) The symmetry on the Greeks' question: whether "easy to vary" should point at one side.** All four answers are HARMLESS (Atria B, Mimo B on X10; Atria E, Mimo E on X18), and none proposes words.
- *What the text says* (the X10 and X18 rulings). On the Greeks' question the tilt and the myth, offered in place of each other and both fitting what an assessor has established, conflict only outside the contract, so they pose a problem of the second kind and each is easy to vary relative to the other, for that assessor. A finer contract with a pair where they conflict is a new question, on which they pose a problem of the first kind. On the Greeks' question itself the problem stands until what is established leaves at most one of them fitting; southern results lie outside that contract. So there the tilt stays easy to vary relative to the myth until something established shows the myth failing (E) on the Greeks' own contract, for instance its non-circular failure, if such a finding counts as established: that is (c2). The X10 ruling adds one reading note: L317's "a conflict between ideas that what the assessor has established has not settled" must then be read as "not settled on \(p\)".
- *Atria.* The term is question- and assessor-relative and says nothing about which candidate is right; the tilt remains an account throughout; it is a declared departure from Deutsch's grading use, coherent with the theory's abstention from merit functions (L25). To call the tilt hard to vary on the Greeks' question would need a count of its variations, which the owner's rule forbids.
- *Mimo.* The label is a statement about the dispute, not about the tilt's own variability; the asymmetry the fixed verdicts need is carried by (E) (the myth fails non-circular dependence, N3; the tilt does not, N1) and by the first-kind problem a wider question makes (N2, N4). Words marking the tilt hard and the myth easy on the restricted question would be the grade the owner's rule forbids.

**(c2) Whether a failure found by examining a candidate counts as established.** Atria A, Mimo A (X09), Atria B (X10), Atria C and Mimo C (X14): UNSETTLED BY THE TEXT; Mimo B (X10): ESTABLISHED. No reply argues that such failures should not count; five say the text should settle it so that they do.
- *What the text says* (the X09, X10 and X14 rulings). L315 defines a result as established for an assessor who holds a usable receipt for it (Part IX), and a candidate as fitting when no established result shows it failing a condition of (E). Part IX neither includes nor excludes an examination of the candidate as the event a leaf refers to (L397). The present wording is true on either answer and does not claim the matter settled; L315's (K3) clause, "the test that yields it", leans toward tests.
- *What turns on it.* If such failures do not count, a candidate whose circularity, empty anchor or internal clash has been found still fits, can share a problem with a sound account and make it "easy to vary" relative to it, and a second-kind problem with it could close only by a test that cannot catch the failure. If they count, "easy to vary" is charged only against rivals that survive examination.
- *The six proposals* (none applied): Atria A, a verification the assessor holds is a receipt, its premises the definitions and the adopted physics, usable under (K2) and qualified by (K3); Mimo A, an inspection failure is such a result once the assessor holds a usable receipt for the inspection; Atria B, a failure decidable from the candidate, the question and the contract alone is established for one who has examined it, without a test, and (K3) does not qualify it; Mimo B, optional words that a result may show this from the candidate's own content, by analysis; Atria C, candidate-side facts read by inspection, receipts kept for target-side and world-side claims; Mimo C, a leaf may reference the candidate's own content, with (K3) taking the definitions, declared indices and reading convention as background. They differ on whether the examination is a receipt, whether (K3) qualifies it, and where the words go (after L315's "fits" sentence, or in Part IX).
- *For the owner to have in view* (the X09 and X14 rulings). Any settlement changes what the theory claims and needs a declaration. The (K3) clause must agree with it. X14's third sentence stands on either settlement the replies propose; it would lose its support only on a settlement neither proposes (a candidate's content could enter no receipt and could not be read without one).

**(d) Losses, and "offered … in place of the other".** Asked whether requiring rivals to conflict at an admitted pair loses anything: RIGHT from Atria A, D, F, H and Mimo D; RIGHT, WITH A LOSS from Mimo A, F and H. Each ruling finds that the wording states each loss truly (most are recorded in W59.1's LOSS).
1. A conflict at a pair only one transport translates is not counted (Mimo A, Mimo H). Where a transport does not translate a pair, its candidate gives nothing there to conflict with.
2. "Easy to vary" is never said of N25's dog and turtle, a swappable pick (Mimo F); both of N25's fixed verdicts stand, "only the name is missing" (the X03 and X10 rulings).
3. Variations that differ only where no admitted change reaches are never rivals, such as a sun god who approves and one who is indifferent (Mimo H).
4. **"Offered as an answer to \(p\) in place of the other" may be narrower than the owner's "discovered"** (Mimo H; Mimo A under (a), "two sibling variations of one original could then escape rivalry"; Atria A, "slightly tighter than the owner's", a narrowness and not a fault). Atria F holds that the gloss "a candidate's rivals are among the candidates someone has offered" fixes the broad reading. The X09 ruling: the clause alone admits the narrow reading, the gloss states the broad one, and no reply names a verdict that turns on it; a variation someone has thought of but not offered is no one's rival under the text. Whether "offered … in place of" renders "discovered" is the owner's call. The X06 ruling adds a second question for the owner: whether "A variation is a competitor" should reach variations that no admitted change separates.

## 10. Findings for later entries, from every ruling

None is an edit in draft 5; each is carried forward in the change list's "Carried forward after S93".
- **L245 and L558: "every component" against "every active component".** L245 says "every component of \(E\)" has the signature of its anchor and L558 "each component", where (F1) and Derivation 1 say "every active component" (L233, L554); after X03's fix, L245 is the one place that says "every component". Candidates: "every active component of \(E\)" at L245 (a CLAIM, narrowing), "each active component" at L558, or a definition of "active component"; whether an anchoring condition on named-background components would then add to (F1) and (F2) needs its own check (X03, finding 1; X06, finding 1).
- **(K2)'s \(\mathrm{Lic}_j\), \(\mathrm{Scope}_j\) and \(\mathrm{Live}_j\) are undefined** (L390 only), so Derivation 6's claim cannot be followed through receipts to the primitives; X17's sentence makes it more visible (X17, finding 1).
- **L598 over-states the order.** Derivation 6's proof says the order "lists the declared indices and the declared inputs with the definitions that rest on them", which is still unmet for the finding-9 omissions; either the order grows or W7.6 says the proof follows unplaced definitions through their own text (X17, finding 3). Receipts, (K2) and (K3) are still unplaced; if placed, (K3) goes after "what is established" (X17, finding 2; X10, ruling 4).
- **"Conflict" is used in two senses:** the defined sense at L315, and the ordinary sense of L429 and of L317's gloss "a conflict between ideas" (X17, finding 6).
- **File 12's L325 carries the same pole-sentence slip** that W61.1 corrects in file 11. File 12 is under no round; nothing was written into `authority/` (X11, point 6).
- **The Part IV question of value maps in port translations.** Whether a port translation may carry a map of values also governs "footprint bijection" in both sentences of L119 and at L564; if it may, Part IV should say so once for all three (X03, finding 2; already carried forward from draft 4).
- **Classes across candidates.** None is formed; if wanted, the relation's domain and transitivity must be stated, as a CLAIM (X03, finding 3).
- **"(RC), (U1)–(U3) depend on all of the above" over-states;** harmless to well-foundedness (X17, finding 4).
- **\(O_{\mathrm{ep}}\) and "resource contract".** \(O_{\mathrm{ep}}\) is read off \(O\) (L443); "resource contract" (L427, L475) has no place of its own among the declared inputs (L522), a candidate clause for L522 (X17, finding 7). "Test" (L317) and "does no work" (L313) stay unplaced; their bases are placed (X17, finding 8).
- **L325's "\(L\) is an output, by Part II"** stands beside "An intervention on \(L\) replaces its component"; by L109 \(L\) is also an input if \(A\) contains that intervention. Noted only (X06, finding 2).
- **The sources note.** Its FALLBACKS table sends *Surprise and problems* back to draft 3's text, which has the words X18's fix replaces; if that fallback is used, the same replacement applies. The *Elimination* line leaves out "its own target" (Mimo E point 4, not a challenge). "(Parts I, V and VI)" would also be true for *Reach*, not required (X18).
- **Derivation 10's obligation.** Atria G point 2 names "predict displacements correctly" (L628), which is the protected obligation; the repaired one is "possess a deployable account of re-emergence after occlusion" (X05).
- **A failed answer stays failed: the limit.** The same mistake at another pair of \(C\) that has not been tested can come back unnoticed; X14 claims nothing there, and the route is Part VI's rivals, problems and tests. W60.1's CASES AT RISK reads O1 as moved toward on its first half; both readers find no move, since L159 already gives it (X14).
- **Flagged in the tabulation, section 4, not items.** L524's definition of a declared input still admits \(\mathcal N\); Mimo K point 7 offers "and which is not one of the two primitives". \(\mathcal V\) survives in (D) (L299, L302) and is not among Part XIV's declared inputs. A search of draft 4 finds "Pres" and "job" 0 times, and "reach" only in "reachability" and as a verb.

*End of the reading.*
