# S90: reading of the replies, batch 2 (Atria A2, Mimo B1)

*Written on 23–24 September 2026 by a Claude subagent for the orchestrator, from about 23:55 UTC on 23 September. It records the rulings of fresh Claude checkers on the changes that these two replies contest. The recorder wrote no ruling and did not draft, assemble or check the change list. It read the two replies named here and their receipts, and no other S90 return. It opened no reasoning file and no attempt file. It read batch 1's reading and the ruling files of both batches. The change list was not edited. Its edits are listed at the end, together with batch 1's, to be made in one pass with the later batches. Nothing was written into `authority/`.*

## The container restart

- **The container restarted at about 23:30 UTC on 23 September 2026.** The rerun note (`results/S90 and S87 - seven calls rerun after the container restart - written before sending.md`) records it.
- **Both replies read here came back before the restart**, and so did the S87 retry O17, which is read in `determination/09`:
  - Atria A2 at 23:19:21;
  - O17 at 23:26:18;
  - Mimo B1 at 23:26:46.

  The times are each receipt's `asked_at_unix` plus `total_seconds`.
- **They were committed after it**, at c137e86 (23:32:35), together with their receipts, requests and attempt files.
- **No data was lost.** The file of each reply has the sha256 its receipt records, and each request file has the receipt's `request_sha256`. The working tree and the scratch folders came through the restart, including batch 1's `s90r/`, whose files date from 23:05 to 23:25.
- **Batch 1 was committed at fbcef8c (23:25:34), before the restart.**
- **The four rulings here were written after the restart**, between 23:39 and 23:51, in the scratch folder `s90r2/`.
- **The seven calls in flight at the restart failed on the dead proxy.** They are being sent again as pass 2 under the rerun note (57482a5, faf91f6). None of them is read here.
- **The restart did not cause batch 1's missing task-(d) ruling file for R51.** Batch 1 recorded the file as missing when it was written, from 23:20, before the restart.

## The rule followed

- **The rule** is the one batch 1 followed: `results/S90 How the cross-examination of the revision 2 draft will be read - written before sending.md`, as extended by `results/S90 Parts - how they will be read, written before sending.md`.
  - **Each reply is read on its own** (Parts rule 1).
  - **What counts as contested** (Parts rule 2). A change is contested when the reply says it FALLS, or when the reply names an undeclared change of claim or a moved verdict on it, whatever closing line it gives the change.
  - **Who rules** (Parts rule 3). Each contested change goes to a fresh Claude checker, one that did not draft, assemble or check the change list and did not write the part briefs. None of this batch's checkers wrote a batch-1 ruling. Each checker states the entry and its checkers' verdict, then the reply's argument, and then rules keep, fix (with exact new wording) or drop.
  - **Edits are recorded as made after the cross-examination** (Parts rule 4).
  - **A failed call supports nothing** (Parts rule 5). Both calls here were accepted.
  - **Silence is not support** (S90 rule 5).
- **Reconciliation.** Where a change was already ruled in batch 1, the ruling here is reconciled with batch 1's. Parts A2 and B1 have now been read for both models: A2 is Mimo's in batch 1 and Atria's here, and B1 is Atria's in batch 1 and Mimo's here.
- **Ids.** R01–R55 map to entry ids through the table in the Parts note.
- **Sources**, the same for every ruling, and the same as batch 1's:
  - the change list `tests/Revision 2 - change list, draft of 23 September.md` as of 587eebf (md5 a5c92adc9f1e3806c0f9c6394cffde1e, unchanged at HEAD);
  - the revised text `tests/Revision 2 - file 13 draft 2, theory text, as sent for cross-examination.md` (md5 9aecf2f30ce0b4523606b2b8409fdf37);
  - file 11, `authority/11 … revision 1.md` (md5 5e494c1095d920d128b9a79de378f923);
  - the S81 case book (md5 4f488d149e44669240d5db546c8e946a) and the S89 case book (md5 b2e535777976a511935430bd089ba500);
  - batch 1's reading (md5 56219a1d3bf20e22ea241cb18ff8a426).
- **The briefs.** The part A2 brief has md5 234bf749788fc3ab3ddcb1e06e249f98 and the B1 brief 130a5eace514ebb02b736d12a311ade2. The sha256 of each is its receipt's `user_sha256`.
- **The rulings** are copied byte for byte into `results/S90 reading rulings/`, one file per ruling, under their scratch names. Each file's md5 is given below.

## Summary

| call | accepted | OVERALL line | closing lines | contested, and why | rulings |
|---|---|---|---|---|---|
| s90_xexam_atria_A2 (part A2) | yes, attempt 4 of 4 | OVERALL: SOUND | R26, R27, R28, R29, R41, R43, R51, R54, R55 STANDS | R51 (moved verdicts on O24, O36 and O46, point 2, task (d)) | R51 KEEP |
| s90_xexam_mimo_B1 (part B1) | yes, attempt 2 of 2 | OVERALL: NEEDS REPAIR | R04 FALLS; R39 FALLS; R03, R10, R48 STANDS; no line for the other 10 | R04 (FALLS); R39 (FALLS); R48 (point 3: on one reading, an undeclared change of claim) | R04 KEEP; R39 FIX; R48 FIX |

**Totals, this batch.** There are four rulings on four entries: KEEP 2 (R51, R04), FIX 2 (R39, R48) and DROP 0.

**Totals, batches 1 and 2 together.** There are twelve rulings on nine entries: KEEP 4 (R51 three times, R04 once), FIX 8 and DROP 0.
- **Entries fixed (7):** W37.1 (R01), W19.1 (R08), W20.1 (R15), W24.1 (R26), W22.1 (R28), W6.3 (R39) and W7.5 (R48).
- **Entries kept (2):** W19.2 (R51) and W58(ii).1 (R04).
- **Entries dropped:** none.
- **Two entries were ruled more than once**, and each set of rulings was reconciled into one:
  - **R39.** Batch 1's FIX, on Atria B1, and this batch's FIX, on Mimo B1, are one ruling. Its edit is made once.
  - **R51.** Batch 1's two KEEPs, on Mimo A2 tasks (a) and (d), and this batch's KEEP, on Atria A2, agree. The task-(d) CHECK line batch 1 could not supply is now written, and it covers both replies.

**The two FIX rulings in this batch:**
- **R39** changes KIND (WORDING → CLAIM) and DECLARATION, as batch 1 already ruled. OLD and NEW stay byte for byte. REASON, CHECK and the "What the checks changed" row now name both calls.
- **R48** changes NEW (one clause added: "(EK) also on (P), ") and DECLARATION. OLD and KIND stay as they are.

**Changes a reply says FALLS, not upheld as argued:**
- **R04:** KEEP. Both repairs the reply offers are refused.
- **R39:** upheld on KIND, as in batch 1. The reply's declaration is refused in favour of batch 1's, and so is "merge into R38".

## Atria, part A2 (s90_xexam_atria_A2)

**The call is accepted.**
- The receipt shows four attempts. Attempts 1–3 have status 0 and no finish, after 1,802.5, 1,802.3 and 1,802.2 s, and left no attempt files. Attempt 4 has status 200, finish "stop", 0 bad chunks and accepted true, after 788.9 s.
- The response's sha256, ae41c8df…, matches the receipt. The request's sha256, 0bdb26b0…, matches the receipt's `request_sha256`.
- The last line is END OF REPORT.
- The reply is 1,376 words by `wc -w`. It used 43,892 reasoning tokens (46,052 completion tokens) of the 65,536 allowed.

**Closing lines:**
- `R26: STANDS`, `R27: STANDS`, `R28: STANDS`, `R29: STANDS`, `R41: STANDS`, `R43: STANDS`, `R51: STANDS`, `R54: STANDS`, `R55: STANDS`, one line each
- `OVERALL: SOUND`

No change FALLS, and the reply names no undeclared change of claim. The only moved verdicts it names are in point 2, on R51 (below).

**Not contested, but bearing on batch 1.** None of these points names an undeclared change of claim or a moved verdict, so under Parts rule 2 none of them is ruled. Each is set beside batch 1's ruling or item.
- **Point 1, R55 with R51 (tasks (a)–(c)).** Atria exhibits the bijection that meets the premise of Derivation 2(ii) for R55 (W19.3 + W10(b).1): \(\varphi\) is the exchange of the two things, so \(\lambda(1)\) and \(\lambda'(2)\) are the same subnetwork, and likewise \(\lambda(2)\) and \(\lambda'(1)\). It calls R55's restriction ("that admits each edit for both things alike", revised L624) a repair of an old claim that was too strong.
  - Batch 1 passed exactly this point to the orchestrator, from Mimo A2 point 2, as a bijection L624 cites without exhibiting. Mimo granted the premise was met.
  - So both replies to part A2 find the premise met. The item stays with the orchestrator, with Atria's exhibition beside it. No reply contests R55.
- **Point 8, R26 (W24.1) (task (b)).** Atria finds that the typing sentence binds notation that was free and restricts nothing.
  - This agrees with the batch-1 R26 checker, who found no change of scope because "admitted generator" and "generator" are coextensive.
  - The condition Atria quotes, "If π∘S_a=T_a∘π for every generator a", is OLD's, and OLD is unchanged by batch 1's FIX, which adds "admitted" only to NEW's condition. Nothing needs reconciling.
- **Point 7, R28 and R29 (W22.1, W22.2).** Atria reads R28 as sent, with "the explanatory candidate (Part V) that the criticism offers for \(p_\delta\)" at L371, and finds it standing. It does not take up "offers", on which batch 1 ruled FIX (Mimo A2 point 1).
  - Under rule 1 this STANDS is evidence, not support for the wording as sent.
  - The clause Atria relies on, "\(p_\delta\) be the question whether \(z\) has \(\delta\) in respect of \(p\)", is kept word for word in batch 1's new NEW. Batch 1's FIX stands, and nothing needs reconciling.
- **Points 3–6** find that R27 does not move N20 and that R54 moves no verdict (O48 rests on the unchanged Derivation 3 and Part XV(D)). They find no case that turns on R41, R43, R28 or R29.

### R51 (W19.2), point 2, task (d): KEEP

- **Why contested.** The reply's line is `R51: STANDS` and its OVERALL line is SOUND. Its point 2 names moved verdicts on O24, O36 and O46, all toward the fixed verdict, and calls the move declared. Under Parts rule 2 a named moved verdict contests the change, as batch 1 counted Mimo A2's task-(d) moves toward the fixed verdict on the same entry.
- **The entry.** W19.2, "Derivation 2: 'Same anchors, one account'". It is in Part XVI: file-11 L552–558, revised L554–562. KIND CLAIM. REASON WORD change of claim.
  - The wording is the settled S88 wording (F1, block 1).
  - CHECK reads "as W19.1", so the entry was checked by its drafter only.
  - CASES AT RISK: O46 "holds AGREE, on firmer text"; O36 "holds AGREE"; O24 "holds AGREE, toward if anything"; N17 toward on its first two questions; N25's second question watched.
  - Batch 1 ruled KEEP twice (Mimo A2, task (a) and task (d)). At HEAD neither KEEP line has yet been appended.
- **The reply.** File 11's "are one account at grain C", with components "pairwise of one kind", misfires on three cases, because in each the two candidates anchor different subnetworks and the old claim would make them one account against the fixed verdict:
  - O24, two wirings;
  - O36, two proof routes;
  - O46, the spring and the reassigned cable.

  The revised (i)/(ii), L560's "nothing more follows", and the unchanged Part VI clauses now give the fixed verdicts. The declaration states the weakening and the narrowed Consequence. No listed case moves away. The reply proposes no repair.
- **The checker.**
  - **The quotations are found.** "One account at grain C" and "pairwise of one kind" are at file-11 L554. L560 is verbatim, and so is the declaration's "covers only candidates that differ in which component carries which anchor". L307's reassigned-component clause is unchanged from file-11 L309 s3.
  - **One description is wrong, and it does not bear on R51.** The reply calls L299 ("the supports assessed are subsets of the written Γ …") unchanged. It is R21's new wording (W58(i).1). File-11 L301 read "the supports assessed are the ones actually written". Both wordings exclude the unwritten support, and R21's own record already gives O36 as AGREE on firmer text. The reply makes no point on R21, so nothing goes to R21's checker.
  - **R51 reaches these cases only through L554–562.** "Derivation 2" is cited only at L119 and L624, and "one account" occurs only at L554–556 and L624.
  - **No mark moves.** S81 (04; 01) already marked file 11 AGREE on O24 (on f11 L558, L259 s2), on O36 (L301) and on O46 (L309 s3). What goes is the pull of "one account … pairwise of one kind" against those verdicts. The declaration's first sentence and its "without that premise nothing more follows" state that withdrawal. So the moves are declared, and the reply says so itself.
    - **O36** is the one case this reply adds to batch 1. It holds AGREE, on firmer text. The rewrite needs a premise outside Γ, so the premise of (ii) fails and the two are "different candidates", as the fixed verdict's "a candidate nobody has written" has it. L299 keeps the assessment to subsets of the written Γ.
    - **O24** holds AGREE, toward if anything. It now rests on unchanged text: L23, Derivation 3 (L566, W17.3) and L257 s2. On a contract that contains the setting, the two arrangements answer differently, so by (i) Derivation 2 cannot make them one account. The narrowing of the old Consequence that O24 once rested on is declared, and batch 1 ruled on it (task (a), KEEP).
    - **O46** holds AGREE, on firmer text. (ii) does not apply, and L307's clause carries the verdict.
  - **Not contested.** The reply says O10, O11, O18, O45, N15, N17 and N25 do not turn on Derivation 2. On N17 and N25 this differs from the entry and from Mimo A2, but on either reading neither case moves away, and the entry's records stand as batch 1 left them.
- **Text:** none changes. OLD, NEW, KIND (CLAIM), REASON WORD and DECLARATION stay as drafted.
- **Reconciled with batch 1.** One KEEP covers batch 1's two KEEPs and this reply.
  - It agrees with the task (a) ruling: the narrowed Consequence is declared, and O24 does not need the lost general principle.
  - It is the same kind of contest as the task (d) ruling: moves toward the fixed verdict that the declaration accounts for.
  - **The missing task-(d) CHECK line cannot be recovered.** The checker searched `results/S90 reading rulings/` and the scratch folder `s90r/`. The only R51 file in either is the task (a) ruling, and the two copies have the same md5 (a586279a…). So the ruling writes the line again, from batch 1's summary together with this ruling, to cover both Mimo A2 (task (d)) and Atria A2 (point 2).
  - Batch 1's optional "differ in nothing but" stays the orchestrator's option. This reply reads the declaration's last sentence as accurate and gives no reason to take the change.
- **To record** (Parts rule 4: a keep goes in the CHECK field):
  1. CHECK: append batch 1's task (a) line, exactly as batch 1 gives it.
  2. CHECK: append this task (d) line (exact). It replaces the missing batch-1 line.

````text
After the cross-examination (S90, task (d): Mimo A2 on O24, O46, N17 and N25, and Atria A2, point 2, on O24, O36 and O46; both R51 STANDS): the moved verdicts both replies name were re-examined and ruled KEEP. Every move named is toward the fixed verdict, and both replies grant that the declaration accounts for it. On the S81 reading file 11 was already AGREE on O24, O36 and O46, so no mark moves; what goes is file 11's "one account … pairwise of one kind", which pulled against them, and the declaration's first sentence and its "without that premise nothing more follows" state that withdrawal. The verdicts rest on text W19.2 leaves unchanged: L23, Derivation 9 and L307's reassigned-component clause (O46), L299 as W58(i).1 words it (O36), and Derivation 3 (W17.3) with L257 s2 (O24), whose old support in file 11's general Consequence is narrowed as the declaration's last sentence says. "Different candidates" in L560 holds by Part V's definition of a candidate, and "one answer profile" is (i). No case moves away: N17 moves toward on its first two questions or not at all, and N25's second question holds on either reading.
````

  3. CASES AT RISK: append to the O36 bullet (exact):

````text
Atria (S90, part A2) reads this as a move toward: file 11's "one account … pairwise of one kind" could have merged the written candidate with the unwritten one. The move is the declared withdrawal, and no mark moves (S81 read file 11 AGREE, on L301).
````

  4. CASES AT RISK, N25: batch 1's edit stands. Mimo's "toward" reading is recorded beside "watched", and nothing is added for Atria.
- **Conflicts:** none. A keep changes no text. R55 is found consistent with R51 in the reply's point 1 and is not contested.
- **Ruling file:** `ruling s90_xexam_atria_A2 item 1 R51.md` (md5 6e1af65fedc5f743d1eeba9121978bea).

## Mimo, part B1 (s90_xexam_mimo_B1)

**The call is accepted.**
- The receipt shows two attempts.
  - **Attempt 1** was rejected ("finish length"): status 200, finish "length", 0 content characters, after 2,170.3 s, following a wait of 2,650.2 s for a slot. Its files, `s90_xexam_mimo_B1.pass1.a1.reasoning.txt` and the 0-byte `s90_xexam_mimo_B1.pass1.a1.truncated.txt`, were committed at c137e86 and not read.
  - **Attempt 2** was accepted: status 200, finish "stop" and 0 bad chunks, after 1,960.4 s.
- The response's sha256, b67c7207…, matches the receipt. The request's sha256, c797ecb2…, matches the receipt's `request_sha256`.
- The last line is END OF REPORT.
- The reply is 1,364 words by `wc -w`. It used 115,383 reasoning tokens (117,510 completion tokens) of the 131,072 allowed.

**Closing lines:**
- `R03: STANDS`
- `R04: FALLS — weaker claim in WORDING guise ("not primitive, not depended on" ≠ "appears nowhere")`
- `R10: STANDS`
- `R39: FALLS — reclassifies 𝒩 ("declared" → "taken") while typed WORDING`
- `R48: STANDS`
- `OVERALL: NEEDS REPAIR`

**Ten of the part's 15 changes have no line:** R02, R18, R38, R44, R45, R46, R47, R49, R50 and R53. The reply makes no point on any of them. Silence is not support (S90 rule 5), so none of the ten counts as examined and upheld by this reply. The five lines it does give are not counted as confirmation either (rule 1).

**Not contested.** These are points for the orchestrator on presentation, not rulings.
- **Point 4, R10 (W57.1 + W32(b).1) (task (c)).** The reply finds three faults in "the ground of its restriction" (L159):
  - it is not defined;
  - it collides with Part IX's "grounds \(g\)";
  - its pointer to Part XIV and Part XIV's pointer back to Part III never state that the two expressions are the same.

  It offers a gloss. It says expressly that no verdict moves and that the declaration is satisfied.
- **Point 5, R03 (W7.1) (task (c)).** Bolded "declared inputs" at L31 comes before any gloss of it, now that R02 has removed the earlier mention at L25. The reply calls R03's claim correctly declared and the defect one of load order only. It offers a gloss.
- **Quotations.** The recorder spot-checked the reply's quotations against the revised text and found them at L31, L159, L449, L520 and L594. The checkers' own checks of quotations are given under each ruling.

### R04 (W58(ii).1), point 1: KEEP

- **Why contested.** The reply says FALLS (task (b)).
- **The entry.** W58(ii).1, "L33 s4: no such predicate is primitive or depended on". Part 0, file-11 L33 s4, revised L31. GROUP B1. REASON WORD clarification.
  - OLD: `No predicate meaning "really explains", "is a cause" or "is knowledge" appears anywhere (Derivation 6).`
  - NEW: `No predicate meaning "really explains", "is a cause" or "is knowledge" is taken as primitive, and no definition depends on one (Derivation 6).`
  - KIND: WORDING. DECLARATION: none, with a CLAIM fallback line ready.
  - CHECK: "check 1, FIX (kind only)", CLAIM → WORDING. 03 ruled L33 s2–s4 ORDER (M6, upheld) and read "appears anywhere" as L590's "no residual predicate" (03 §8 item 11).
  - The REASON records why the skeleton's "is defined or presupposed" was not used: "defined" would contradict L586, (EK) and Part II's causal assignment.
  - Batch 1 made no ruling on this entry. Atria (B1, point 2) tested R04 and found it standing. There is nothing to reconcile.
- **The reply.** The old wording rules out every such predicate, derived or not. The new one rules out only a primitive one and one that a definition uses. So a derived "explains" predicate that is defined but used by no other definition satisfies the new wording and not the old, and a WORDING entry weakens a claim. The pointer makes it worse. On the natural reading of "residual", Derivation 6's Consequence (L594) supports the old wording, and the new second half is supported by Part XIV (L520), which R04 does not cite. The reply offers two repairs:
  - retype R04 as CLAIM, with a declaration that Part 0 now claims only that no such predicate is primitive or depended on;
  - or keep WORDING and write "exists in the theory (Derivation 6)".
- **The checker.**
  - **The quotations are found.** The Consequence is at revised L594 and file-11 L590. The reply's "594–595" is one line off, because L595 is blank. "Nothing depends on a predicate meaning …" is at revised L520 and file-11 L518.
  - **On the reply's reading, OLD is already false in file 11.** File 11 defines explanation (L13), a proof's explaining (L51), the causal assignment (L125–129), and knowledge and representation (L512). Its (RC) depends on (EK) and (E). So read the reply's way, both OLD and L518 are false in file 11 itself.
  - **"Residual" means "left undefined".** Derivation 6's Claim is that every predicate is defined. Its Consequence lists "represents", which Part XIV derives. So "no residual predicate" means none is taken as primitive, which is NEW's first half.
  - **The second half copies L518**, in L518's sense: the quotation marks and "really" mark the *unanalyzed* predicate. On that reading OLD and NEW say the same thing.
  - **The reply's "orphan derived predicate" is already in file 11.** The causal assignment of L125 is defined, and no other definition uses it. NEW is true of it, and OLD, read literally, was false of it.
  - **The pointer is sound.** Derivation 6's proof (revised L592) runs "By the dependence order of Part XIV", and L31 s3 says "in the order Part XIV states".
  - **Both repairs are refused.**
    - "Exists in the theory" is false against revised L11, L49, L121–127 and L514.
    - The CLAIM declaration would declare that Part 0 withdraws a claim the text never made on any reading it bears. It would also reverse 03's upheld M6 ORDER ruling without new ground.
  - **Batch 1's R39 precedent does not carry over.** There the old words let a reader conclude something the text uses as a working category. Here the old conclusion is one the text refutes in four places.
- **Text:** none changes. OLD, NEW, KIND WORDING, DECLARATION none and the prepared CLAIM fallback line all stay byte for byte.
- **Cases.** The reply names none, and CASES AT RISK is "None". A search of the S81 and S89 case books for "is a cause", "primitive", "predicate", "residual" and "really explain" finds nothing. No verdict moves.
- **To record** (CHECK, append). The ruling file sets out the same sentences as a list, and here they are joined in order:

````text
After the cross-examination (s90_xexam_mimo_B1, point 1, R04 FALLS: 'weaker claim in WORDING guise'): KEEP. The reply reads 'a predicate meaning …' and L590's 'residual' as covering derived predicates. On that reading, both OLD and L518 are false in file 11 itself, which defines explanation (L13), a proof's explaining (L51), the causal assignment (L125–129) and knowledge and representation (L512), and whose (RC) depends on (EK) and (E). On the only reading the text bears, the unanalyzed predicate, OLD and NEW say the same thing. The second half copies L518. Derivation 6's proof reaches L518/L520. Atria (s90_xexam_atria_B1, point 2) found the entry standing.
````

- **By program:** nothing changes. The counts, the note's N and M, and record row R2-04 stay as they are. The entry stays in the note's list "Entries not declared, whose ruling a checker may raise to CLAIM".
- **Conflicts:** none. W7.1 (R03) is untouched, and its "in the order Part XIV states" supports the pointer. W7.6 (R53) agrees.
- **Ruling file:** `ruling s90_xexam_mimo_B1 item 1 R04.md` (md5 78fa498408bfe4366d5fa1f7964f4b2d).

### R39 (W6.3), point 2: FIX (kind and declaration; OLD and NEW unchanged), one ruling with batch 1's

- **Why contested.** The reply says FALLS (task (b)).
- **The entry.** W6.3, "L447 s3: 'declared as' becomes 'taken as'". Part XI, file-11 L447 s3, revised L449. GROUP B1. KIND WORDING. REASON WORD erratum. DECLARATION none. CHECK "check 1, SOUND".
  - OLD: `declared as a substantive input when aesthetic value is claimed.`
  - NEW: `taken as a substantive input when aesthetic value is claimed.`
- **Batch 1's ruling on this entry** (Atria B1, point 1) is FIX:
  - KIND WORDING → CLAIM;
  - the declaration given below;
  - the REASON's "can be dropped without harm" replaced;
  - Atria's repairs "fold into R38" and "R38's declaration" refused;
  - revised L51 passed to the orchestrator.
- **The reply.** "Declared" is a term of art. Part XIV has a "Declared inputs" section, and there are "declared indices" and, the reply says, a "Declared" provenance type in Part IV. The old s3 placed \(\mathcal N\) in the declared-input category. The new s3 matches primitive 2 ("taken as an input and never derived"). R38 is typed CLAIM for the same reclassification in s2, and R39 repeats it one sentence later as WORDING. The reply offers two repairs:
  - merge R39 into R38;
  - or retype it CLAIM with the declaration "𝒩 is now 'taken as' rather than 'declared as' a substantive input in the aesthetic case, consistent with its status as primitive 2."
- **The checker.** The point on KIND agrees with batch 1's FIX.
  - **By the list's own test (change list L2184) the change is CLAIM.** From old s3 a reader concludes that the aesthetic \(\mathcal N\) is a declared input. From the revised text no reader can.
  - W6.4's clause gives the same missing-input consequence by another route, but that is not the same assertion.
  - **Merge into R38: refused, as in batch 1.** It would renumber R2-39 onward and merge two disjoint OLDs.
  - **Mimo's declaration: refused, in favour of batch 1's.**
    - It quotes the two verbs and does not say which conclusion is lost.
    - Its "consistent with its status as primitive 2" gives R39 a content its NEW does not carry. Primitive 2 is named in W6.2 (s2), not in R39's NEW.
  - **One quotation is not found as stated.** The provenance value "declared" belongs to a contract, at revised L155 in Part III ("A **declared** contract is stipulated by the modeller"). Part IV has only "A declared transport" (L211). The point does not rest on it.
- **OLD:** unchanged. **NEW:** unchanged.
- **KIND:** CLAIM (was WORDING). **REASON WORD:** erratum, unchanged.
- **DECLARATION (exact, as batch 1):**

````text
Part XI no longer calls the aesthetic normative relation a declared input: it is taken as a substantive input when aesthetic value is claimed.
````

- **REASON, last clause.** "and it can be dropped without harm to any other entry." is replaced with the sentence below. The sentence before it then ends "… for the same reason." This is batch 1's sentence with the second call added:

````text
It cannot be dropped: without it, s3 would still call \(\mathcal N\) declared one sentence after W6.2, W6.2's declaration would be false of Part XI, and the paragraph would pull against L510 and L514. After the cross-examination (s90_xexam_atria_B1, point 1; s90_xexam_mimo_B1, point 2) it is ruled CLAIM, with the declaration drafted above as its fallback.
````

- **CHECK (exact).** It replaces batch 1's CHECK line:

````text
check 1, SOUND. After the cross-examination (s90_xexam_atria_B1, point 1, and s90_xexam_mimo_B1, point 2; both R39 FALLS): FIX. KIND WORDING → CLAIM, declaration added; OLD and NEW unchanged. Both replies' repairs refused: folding into W6.2 (R38) would renumber the record and merge disjoint OLDs; W6.2's declaration, and Mimo's "consistent with its status as primitive 2", give R39 a content its NEW does not carry.
````

- **"What the checks changed":** the W6.3 row names both calls and points, s90_xexam_atria_B1 point 1 and s90_xexam_mimo_B1 point 2.
- **By program, once, not twice** (batch 1's pending edit 6):
  - CLAIM 48 → 49, WORDING 5 → 4, and group B1 13 → 14 of 15;
  - the note reads "49 of the 55 changes", and it gains a second line for file-11 L447, after W6.2's;
  - W6.3 leaves the note's list "Entries not declared, whose ruling a checker may raise to CLAIM";
  - record row R2-39 becomes CLAIM, declared.
- **Cases.** The reply names none. The S81 and S89 books have no "aesthet", "beaut" or "artist". O12 is a claim of worth, not of aesthetic value. It falls under s2 (W6.2) and L516 (W6.4) and stays SILENT. CASES AT RISK "None" stands.
- **Conflicts:** none. W6.2 (R38) has a disjoint OLD, and its declaration agrees with this one. W6.1, W6.4 + W14.1, W15.1, W7.2 and W7.3 all send \(\mathcal N\) to "an input" outside the declared-input category.
- **Loose end, unchanged:** revised L51, "In Part XI, as a declared normative relation". It is batch 1's item and stays with the orchestrator.
- **Ruling file:** `ruling s90_xexam_mimo_B1 item 2 R39.md` (md5 503df60170a2e307a0f1aa6db1bf0685).

### R48 (W7.5), point 3: FIX (NEW and DECLARATION; OLD and KIND unchanged)

- **Why contested.** The reply's line is `R48: STANDS` (tasks (a) and (c)). Its point 3 argues that the declaration omits a part of the changed sentence, the unchanged clause "(P), (EK) depend on (G), (E), Deploy". It says that in the combined sentence this clause now reads as the baseline for (P)'s "also" dependencies, "giving the error a form it did not have before". On one reading that names an undeclared change of claim. The same point adds that (EK)'s dependence on (P) is never stated.
- **The entry.** W7.5, "L518 s9–s11: Ownership, owned capability, ProducedBy and the obligations". Part XIV, "Dependence order", file-11 L518, revised L520. GROUP B1. KIND CLAIM. REASON WORD erratum.
  - CHECK: "check 1, SOUND. The order still omits Result, ProducesVia, Cap and Enable (B1 finding 9)".
  - The REASON's "Not corrected" keeps "(P), (EK) depend on (G), (E), Deploy" as a harmless over-statement.
  - Finding 9 records the same over-statement. It does not record the missing (EK)→(P).
  - Batch 1 made no ruling on this entry, and Atria (B1) found it standing. There is nothing to reconcile.
- **The reply.**
  - **Its first claim.** (P)'s definiens uses only the obligations and ProducedBy, so "(P) depends on (G), (E), Deploy" contradicts it, and "(P) also on …" presupposes that the first list is right for (P).
  - **Its second claim.** (EK) uses Repair, so (EK) depends on (P), and the order never says so.
  - The reply calls both partly pre-existing. Its repair: "(EK) depends on (G), (E), Deploy and (P). (P) depends on ProducedBy and on the declared obligations with their occasions, and ProducedBy on histories and their active routes."
- **The checker.**
  - **Quotations.** They are found on their content. Three of the reply's line numbers are wrong: (P) is at L432, not 438; (G) at L416, not 371; and (EK)'s "Repair_{O,P}" at L441, not 443.
  - **The first claim names no undeclared change of claim.** The clause is word for word the same in both texts, and the reply grants this. What "(P) also on …" adds is exactly what the declaration names.
  - **Deleting the over-statement would trade it for an under-statement.**
    - (G) is plainly idle for (P).
    - (E) and Deploy carry (P)'s only route in the order to (R). ProducedBy rests on active routes, which L369 defines through a *represented* input and distinction, and an obligation in O may be epistemic (L437).
    - The reply's rewording for (P) is therefore not taken.
  - **The second claim is a real gap, and R48 opens it.**
    - (EK) uses Repair_{O,P} and O_ep ⊆ O (L440–443).
    - In file 11, (P) and (EK) had the same stated bases, so nothing was lost.
    - R48 gives (P) new bases and does not give them to (EK), so for the first time (EK)'s stated bases do not reach the declared obligations.
    - Yet R53's proof now says the order lists the declared inputs "with the definitions that rest on them".
    - The one true clause "(EK) also on (P)" closes the gap. It is read off (EK)'s definition and adds a base, so it cannot under-state. It makes no circle, and it touches neither W20's two free sentences nor L520's last sentence (M49).
- **OLD** (unchanged):

````text
Build depends on histories and (E). (N), (G) depend on Deploy and Build. (P), (EK) depend on (G), (E), Deploy.
````

- **NEW (exact).** The only change to the drafted NEW is the clause "(EK) also on (P), ", inserted after "with their occasions," and before "and ProducedBy".

````text
Ownership depends on histories and a declared boundary, and owned capability on Ownership, (CT1) and a declared continuity (Part XII). Build depends on histories, Ownership and (E). (N), (G) depend on Deploy and Build. (P), (EK) depend on (G), (E), Deploy; (P) also on ProducedBy and on the declared obligations with their occasions, (EK) also on (P), and ProducedBy on histories and their active routes.
````

- **KIND:** CLAIM, unchanged. **REASON WORD:** erratum, unchanged.
- **DECLARATION (exact):**

````text
Part XIV's dependence order now places Ownership on histories and a declared boundary, owned capability on Ownership, (CT1) and a declared continuity, Build on Ownership, (P) on ProducedBy and the declared obligations with their occasions, (EK) on (P), and ProducedBy on histories and their active routes.
````

- **REASON, to add**, marked as after the cross-examination (exact):

````text
(EK) uses Repair_{O,P} and the obligations O_ep ⊆ O (L440–443). As drafted, the order gave (P) its bases in ProducedBy and the declared obligations and left (EK), in the same sentence, with no route to them. Derivation 6's proof as W7.6 words it follows each definition to the declared inputs through this order. The clause states a dependence (EK)'s definition already has. It moves no case, touches neither W20's two free sentences nor the last sentence, and creates no circle (Mimo, s90_xexam_mimo_B1, point 3).
````

- **REASON, "Not corrected":** add one sentence (exact):

````text
Kept after the cross-examination: only (G) is plainly idle for (P), and (E) and Deploy carry (P)'s route to (R) through active routes and epistemic obligations.
````

- **CHECK:** add (exact):

````text
After the cross-examination (Mimo B1, point 3): FIX, '(EK) also on (P)' added; the over-statement for (P) kept.
````

- **GAIN:** add "(EK) reaches the declared obligations through (P)." **LOSS:** none. **CASES AT RISK:** no change.
- **Finding 9** stays as it is in substance. It may add that (EK)→(P) is now stated.
- **Cases.**
  - The reply names none.
  - O35 and O38 turn on how a condition covers its occasions (L435, L514). O37 turns on L520's last sentence. O49 turns on Ownership before owned capability.
  - A search of both case books finds no case that cites the dependence order.
  - No mark moves.
- **By program.** Row R2-48 stays CLAIM, and N, M and K are unchanged. The note's line for R2-48 follows the new declaration when the draft is rebuilt. The new NEW occurs once in the rebuilt draft and overlaps no other entry.
- **Carried forward, not ruled:** what an active route depends on. L369 defines it "under the declared contrasts", the order does not place active routes, and L514 does not list declared contrasts. No reply raised this.
- **Conflicts:** none. W7.4 (s1), W3.2 (the last sentence) and W20's two free sentences are untouched.
- **Ruling file:** `ruling s90_xexam_mimo_B1 item 3 R48.md` (md5 532245a0c17f0db620d245b3438313b0).

## Pending edits to the change list, batches 1 and 2

**None of these is made now.** They are to be applied in one pass together with the later batches, to `tests/Revision 2 - change list, draft of 23 September.md`. Items 1–5 and 8 are batch 1's, unchanged. Items 6 and 7 are batch 1's, amended here. Items 9 and 10 are new.

- **Reconcile first.** Parts A1, B2 and C are still to be read for one or both models. If a later reply contests one of these nine entries, its ruling is reconciled with the ones here before the pass. The R15 ruling asks for this at L231.
- **Mark every edit.** Each edit is marked in its entry as made after the cross-examination, with the call and point that raised it.
- **After the pass.** The draft is rebuilt by program, and then the following are checked:
  - the counts;
  - the note's N and M;
  - the revision note (generated from the list);
  - the layer-1 record.

1. **W37.1 (R01; Mimo A1, point 3), FIX.** As batch 1, item 1.
   - NEW: "blind" deleted. REASON WORD erratum → clarification.
   - The fallback declaration line, GAIN, LOSS, REASON and CHECK are changed as batch 1 gives them.
   - Title (optional). Row R2-01's reason column is set by program.
2. **W19.1 (R08; Mimo A1, point 1), FIX.** As batch 1, item 2.
   - NEW: the typing sentence is inserted after sentence 2.
   - WHERE, REASON, LOSS and CHECK are changed as batch 1 gives them.
   - The carried-forward finding "Part II uses the notation of Parts IV and V before they introduce it" is closed.
3. **W20.1 (R15; Mimo A1, point 2), FIX.** As batch 1, item 3.
   - NEW: ", whether or not anyone has described their work" is added.
   - DECLARATION, CHECK and REASON are changed as batch 1 gives them.
   - CASES AT RISK, O45 → "holds AGREE, on firmer text …", with the two follow-ons at list L168 and L190.
4. **W24.1 (R26; Mimo A2, point 4), FIX.** As batch 1, item 4.
   - NEW: the condition reads "for every admitted generator \(a\)".
   - REASON and CHECK are changed as batch 1 gives them.
   - Atria A2, point 8, finds R26 standing and restricting nothing, which agrees. Nothing needs reconciling.
5. **W22.1 (R28; Mimo A2, point 1), FIX.** As batch 1, item 5.
   - NEW and DECLARATION are changed as batch 1 gives them. The CHECK line and the "What the checks changed" line are added.
   - Atria A2, point 7, finds R28 standing on the wording as sent and does not take up "offers". Its \(p_\delta\) clause is kept in the new NEW. Nothing needs reconciling.
6. **W6.3 (R39; Atria B1, point 1, and Mimo B1, point 2), FIX. Batch 1's item 6, amended.**
   - KIND: WORDING → CLAIM. OLD and NEW unchanged.
   - DECLARATION: as batch 1.
   - REASON: the last clause is replaced with the sentence given above, which names both calls.
   - CHECK: the line given above, which names both calls, in place of batch 1's.
   - "Counts", made once: CLAIM 48 → 49, WORDING 5 → 4, and group B1 13 → 14 of 15.
   - By program: the note reads "49 of the 55 changes" and gains a second L447 line. W6.3 leaves the list of entries not declared. Row R2-39 becomes CLAIM, declared.
7. **W19.2 (R51; Mimo A2, point 3 and task (d); Atria A2, point 2), KEEP three times. Batch 1's item 7, amended.**
   - No text changes.
   - CHECK: append batch 1's task (a) line, exact, as batch 1 gives it.
   - CHECK: append the task (d) line given above, exact. It covers Mimo A2 (d) and Atria A2 point 2, and it replaces batch 1's missing line, which cannot be recovered.
   - CASES AT RISK, O36: append the sentence given above, exact.
   - CASES AT RISK, N25: record Mimo's "toward" reading beside "watched" (batch 1).
   - Optional, not ruled: the declaration's "differ in which component" → "differ in nothing but which component".
8. **"What the checks changed".** Add a part headed as after the cross-examination (S90), with one row for each FIX: W37.1, W19.1, W20.1, W24.1, W22.1, W6.3 and W7.5. Give each row's call and point, and name both calls in the W6.3 row. The Counts bullet "The checks" gains the S90 totals once every batch is read.
9. **W58(ii).1 (R04; Mimo B1, point 1), KEEP. New.**
   - No text changes. KIND WORDING, DECLARATION none and the CLAIM fallback line all stay byte for byte.
   - CHECK: append the line given above, exact.
   - By program: nothing changes.
10. **W7.5 (R48; Mimo B1, point 3), FIX. New.**
    - NEW: the clause "(EK) also on (P), " is inserted, as given above.
    - DECLARATION: as given above.
    - REASON: add the reason paragraph, and add the one sentence under "Not corrected", both given above.
    - CHECK: add the line given above.
    - GAIN: add "(EK) reaches the declared obligations through (P)."
    - OLD, KIND, REASON WORD, CASES AT RISK and LOSS are unchanged.
    - Optional: finding 9 notes that (EK)→(P) is now stated.
    - By program: the note's line for R2-48 follows the new declaration. The counts and N, M and K are unchanged.

**Passed to the orchestrator, not edits** (batches 1 and 2):
- R17's letter \(G\) (Mimo A1, point 4).
- R55's bijection (Mimo A2, point 2: cited at L624 without being exhibited). Atria A2, point 1, now exhibits it: \(\varphi\) is the exchange of the two things. Neither reply contests R55.
- Revised L51, "as a declared normative relation" (from batch 1's R39 ruling, left there by this batch's).
- R10's "the ground of its restriction" at L159 (Mimo B1, point 4). It is undefined beside Part IX's "grounds \(g\)", and the reply offers a gloss.
- R03's bolded "declared inputs" at L31, before any gloss (Mimo B1, point 5). The reply offers a gloss.
- What an active route depends on (from the R48 ruling). L369 is "under the declared contrasts", the order does not place active routes, and L514 does not list declared contrasts. It is a candidate for "Findings carried forward".

## What is still to come

- **Read so far.**
  - Batch 1: Mimo A1, Mimo A2 and Atria B1.
  - Batch 2 (this file): Atria A2 and Mimo B1.
  - So parts A2 and B1 have now been read for both models.
- **Not yet read.** Atria A1, B2 and C, and Mimo B2 and C. Their pass 1 was cut by the container restart, and they were sent again as pass 2 at 23:45:32 under the rerun note. Each will be read on its own under the same rules. A pass-2 failure supports nothing, and that part's changes are then reported as not examined by that model.
- **The pass on the change list** is made once, after every batch is read and reconciled.

Dated 23–24 September 2026.
