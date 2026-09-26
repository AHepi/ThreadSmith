# Ruling: s90_xexam_atria_A2, item 1, R51 (W19.2)

*A fresh Claude checker, 23 September 2026, working under the S90 rule as extended by "S90 Parts - how they will be read, written before sending.md". Under rule 2 of that note, a moved verdict that a reply names is re-examined whatever closing line the reply gives the change. This checker did not draft, assemble or check the change list, and did not write the part briefs. It wrote none of batch 1's rulings.*

*What it read of the reply: points 1 and 2 (the only points that name R51) and the closing lines. It also read the receipt: accepted on attempt 4, finish "stop", response md5 d9fc7c6c25ee25332047571e7293cd80, with END OF REPORT as the last line. It opened no reasoning file and no other S90 return.*

*Sources:*
- *the change list, md5 a5c92adc9f1e3806c0f9c6394cffde1e (587eebf, unchanged at HEAD);*
- *the revised text, md5 9aecf2f30ce0b4523606b2b8409fdf37;*
- *file 11, md5 5e494c1095d920d128b9a79de378f923;*
- *the A2 brief, md5 234bf749788fc3ab3ddcb1e06e249f98;*
- *the S81 case book, md5 4f488d149e44669240d5db546c8e946a, and the S89 case book, md5 b2e535777976a511935430bd089ba500;*
- *the S81 determination, files 01 and 04.*

## 1. The entry, its checkers' history, and batch 1's rulings on it

W19.2, "Derivation 2: 'Same anchors, one account'", is R51 (= R2-51). It sits in Part XVI, Derivation 2: file-11 L552–558, revised L554–562. KIND: CLAIM. REASON WORD: change of claim.

- **OLD:**

````text
## 2. Indistinguishable is identical

**Claim.** Two candidates \(\mathcal E,\mathcal E'\) for the same \(p\) that both satisfy (F1), (F2), and (A) on \(C\) are one account at grain \(C\): their components are pairwise of one kind on \(C\) and their answer profiles coincide.

*Proof.* Immediate from Derivation 1 and (A). ∎

**Consequence.** Underdetermination of an account by a contract is not a failure of the semantics to decide; it is the semantics reporting that the contract does not contain the distinction. The remedy is a finer contract, which is a new question. A claim that two such candidates "really" differ is a claim that some admitted change separates them, and must supply it.
````

- **NEW:**

````text
## 2. Same anchors, one account

**Claim.** Let \(\mathcal E,\mathcal E'\) be candidates for the same \(p\) that both satisfy (F1), (F2) and (A) on \(C\). (i) Their answer profiles coincide on \(C\). (ii) If a bijection \(\varphi\) of their active components gives each \(k\) and \(\varphi(k)\) one anchor, the same subnetwork of \(D\) with port translations onto the same ports of \(D\), then \(k\) and \(\varphi(k)\) are of one kind on \(C\) for every \(k\); so far as (F1), (F2) and (A) reach, the two are one account on \(C\): \(\varphi\) pairs their active components, each pair of one kind on \(C\), and by (i) their answer profiles coincide.

*Proof.* (i) By (A), \(\operatorname{Ans}_E(\tau(a),\sigma(b))=\operatorname{Ans}_p(a,b)=\operatorname{Ans}_{E'}(\tau'(a),\sigma'(b))\) for every \((a,b)\in C\). (ii) By Derivation 1, \(k\) has the signature of its anchor on the ports its translation names, and \(\varphi(k)\) the signature of the same anchor on the same ports; composing the one translation with the inverse of the other gives a footprint bijection under which the two signatures, read on \(C\), coincide. ∎

Without the premise of (ii) nothing more follows: candidates that anchor different subnetworks, or cut \(D\) at different places, are different candidates with one answer profile (Derivation 9; Part VI, redundant routes). A coarsening is not a recoding (Derivation 8).

**Consequence.** Where two candidates that satisfy (F1), (F2) and (A) differ only in which component carries which anchor, the contract does not contain the distinction; a claim that one assignment is "really" right is a claim that some admitted change separates them, and must supply it. The remedy is a finer contract, which is a new question.
````

- **DECLARATION:** "Derivation 2 no longer says that two candidates for one question that satisfy (F1), (F2) and (A) on C are one account whose components are pairwise of one kind. It now says that their answer profiles coincide on C; that where a bijection of their active components gives each pair one anchor, the same subnetwork of D with port translations onto the same ports of D, each pair is of one kind on C and, so far as (F1), (F2) and (A) reach, the two are one account; and that without that premise nothing more follows. Its Consequence now covers only candidates that differ in which component carries which anchor."

- **Checkers' history (CHECK).** The field reads: "as W19.1. The text is the settled wording (F1, block 1), copied byte for byte."
  - W19.1's CHECK says it was not put to check 1 or check 2, which ran before S88 was settled. Only its drafter checked it: the program applied it with no refusal and no overlap, and the drafter read it in place and worked the guard rows.
  - The entry has no FIX or SOUND history.
  - At HEAD, neither of batch 1's KEEP lines has been appended yet.

- **CASES AT RISK, on the cases this reply names:**
  - O46 "holds AGREE, on firmer text".
  - O36 "holds AGREE. The unwritten route with another premise cuts \(D\) at a different place, so it is a different candidate, and P stays critical in each route as written."
  - O24 "holds AGREE, toward if anything".
  - N17 is toward on its first two questions.
  - N25's second question is watched.

- **Batch 1 ruled on this entry twice, both times on Mimo A2, and both rulings are KEEP.**
  - **Point 3, task (a).** The ruling file is `ruling s90_xexam_mimo_A2 R51.md`, md5 a586279ae712f1ae74022bfffb82f688. It is KEEP with no text change, and its CHECK line is given exact in the batch 1 reading.
  - **Task (d), moved verdicts on O24, O46, N17 and N25.** This ruling is also KEEP with no text change. Its CHECK line is missing.
    - This checker searched `results/S90 reading rulings/` and the scratch folder `s90r/`. The only R51 file in either place is the task (a) ruling, and the two copies have the same md5.
    - So the line cannot be recovered. Batch 1 allows it to be written again from the orchestrator's summary, and section 4 below writes it again, reconciled with this ruling.

## 2. The reply's argument

**Why contested.** The reply's line is `R51: STANDS`, and its OVERALL line is `OVERALL: SOUND`. Its point 2 names moved verdicts on O24, O36 and O46 under task (d). Parts rule 2 counts that as contesting the change, as batch 1 counted Mimo A2's parallel moves toward the fixed verdict.

Point 2, whole:

> "**2. R51 — (d): it moves O24, O36 and O46 toward the fixed verdict, and the declaration accounts for the move.**
>
> Under the current text, two candidates for one p satisfying (F1), (F2) and (A) on C "are one account at grain C," with components "pairwise of one kind." That misfires on O24 (two wirings differing at one reachable but unused setting), O36 (two proof routes both using P) and O46 (the spring account vs. the reassigned cable account): in each the two candidates anchor different subnetworks, so the old claim would collapse them into one account against the fixed verdict. The revised Derivation 2 says only (i) answer profiles coincide, and (ii) the one-account conclusion needs the shared-anchor premise; and it adds "Without the premise of (ii) nothing more follows: candidates that anchor different subnetworks, or cut D at different places, are different candidates with one answer profile." That, with the unchanged Part VI clause ("the supports assessed are subsets of the written Γ … not a support someone could write with commitments outside Γ" and "a component reassigned to a new target after a deletion belongs to a new candidate with its own assessment"), now gives the fixed verdicts. The declaration states the weakening and the narrowed Consequence ("covers only candidates that differ in which component carries which anchor"), so the move is declared. No listed case moves away from its verdict: O10, O11, O18, O45, N15, N17, N25 turn on (K), Build/relay and (E), not on Derivation 2."

Point 1 ends: "R51's declaration and R55's declaration both describe their wordings exactly, and neither overstates." Under rules 1 and 5 this is evidence, not support. The reply proposes no repair for R51.

## 3. The texts and the cases

**Quotations (S90 rule 8).**
- "are one account at grain C" and "pairwise of one kind": found in file 11 at L554, as "the current text".
- The L560 sentence: found verbatim, apart from how \(D\) is typeset.
- The declaration's "covers only candidates that differ in which component carries which anchor": found verbatim.
- "a component reassigned to a new target after a deletion belongs to a new candidate with its own assessment": found at revised L307. It is unchanged from file 11 L309 s3, second clause.
- "the supports assessed are subsets of the written Γ … not a support someone could write with commitments outside Γ": found at revised L299, with the ellipsis standing for "whether or not anyone has set them out,". **It is not unchanged**, as the reply says.
  - It is R21 (W58(i).1, part C, CLAIM).
  - File 11 L301 reads: "the supports assessed are the ones actually written, not a support someone could write in their place."
  - The misdescription does not bear on R51. Both wordings exclude the unwritten support, and R21's own record says "O36 holds AGREE, on firmer text". The reply makes no point on R21, so nothing is passed to R21's checker.

**Searches.**
- In file 11, "Derivation 2" is cited only at L620, and "one account" occurs only at L554.
- In the revised text, "Derivation 2" is cited only at L119 (W19.1) and L624 (W19.3). "One account" occurs only at L554–556 and L624.
- So R51 can touch O24, O36 and O46 only through L554–562. No other line of either text carries the old slogan.

**The file-11 baseline.** The S81 determination (04, step 3; 01 for the rows it did not reselect) marks file 11 **AGREE** on all three cases:
- O24 rests on "f11 L558, L259 s2", the old Consequence and Non-vacuity.
- O36 rests on f11 L301.
- O46 rests on "f11 L309 s3, second clause".

So no mark moves. What changes is the text a reading can rest on. The reply's "misfires … against the fixed verdict" overstates file 11, as the cases below show.

**O36** (fixed verdict: "P is critical in each route as written. That another route could be written without it is a fact about a candidate nobody has written.")
- **File 11.** Suppose the written candidate and the unwritten rewrite both reach the fixed answer. Read on them, the old Claim offered a real pull: "one account … pairwise of one kind" would give the account a support without P. But L301 answered that pull directly, and S81 rests the AGREE there.
- **Revised text.** The rewrite needs a premise outside Γ, so it anchors another subnetwork or cuts \(D\) elsewhere. The premise of (ii) fails, and L560 says "nothing more follows". The two are "different candidates", which matches the fixed verdict's own "a candidate nobody has written". L299 keeps the assessment to subsets of the written Γ.
- **Result:** O36 holds AGREE, on firmer text. The reply's "toward" is the same fact counted as a move.
- **Nothing moves it away.** The old Consequence's general principle, which R51 narrows, was never what O36 rested on.
- **O36 is the one case this reply adds to batch 1's rulings, and it holds.**

**O24** (fixed verdict: "They are two arrangements, and the record has not chosen between them. One reachable setting is enough.")
- **File 11.** On the tested grain, the old Claim pulled toward "one account". The old Consequence carried the verdict: the reachable setting is the admitted change that "must" be supplied. S81 rests O24's AGREE on that sentence (L558).
- **Revised text.** The narrowed Consequence no longer reaches O24. The verdict now rests on unchanged text:
  - L23: different internal routes make "different organizations".
  - Derivation 3 at L566 (W17.3): both arrangements are members of \(\mathcal T\), both survive on \(H\), and they differ at a setting the physics admits.
  - L257 s2: an admitted edit is left out of \(C\) only by a stated scope.
  - On a contract that contains the setting, their answers differ. So by (i) they cannot both satisfy (A) there, and Derivation 2 cannot make them one account.
- **Result:** O24 holds AGREE, "toward if anything", as the entry and batch 1 say.
- **The narrowing of the Consequence is declared.** It is in the declaration's last sentence, and batch 1 already ruled on it (task (a), KEEP). Batch 1's task (d) summary adds: "O24 cannot rest on the phrase at all."

**O46** (fixed verdict: "What survived is a new account with a cable in it. The spring account did not survive …")
- The spring and the cable anchor different subnetworks, so (ii) does not apply.
- L307's reassigned-component clause is unchanged and carries the verdict.
- The only pull toward "the spring account survived" was the slogan's "one account", and the declaration's first sentence withdraws it.
- **Result:** O46 holds AGREE, on firmer text, as the entry and batch 1 say.

**Is the move declared?** Yes. The moves that the reply names on O24, O36 and O46 are all toward the fixed verdict. Each is the removal of a pull, and that removal is what the declaration's first sentence states, together with "without that premise nothing more follows". The narrowed Consequence is its last sentence. So under task (d) there is no undeclared change of claim, and the reply says so itself.

**Not contested.** The reply also says that O10, O11, O18, O45, N15, N17 and N25 do not turn on Derivation 2. That names no move.
- On N17 and N25 it differs from the entry and from Mimo A2. N17 is toward on its first two questions, through L560, which its "different candidates" touches. N25's second question is watched.
- On either reading, neither case moves away.
- The entry's records of N17 and N25 stand as batch 1 left them. The reply's reason is incomplete on N17, but its conclusion agrees.

**Reconciled with batch 1.**
- This is the same entry and the same kind of contest as batch 1's task (d) ruling: moves toward the fixed verdict that the declaration accounts for.
- It is compatible with batch 1's task (a) ruling. The narrowed Consequence is declared, and O24 does not need the lost general principle.
- Its one new case, O36, holds.
- Batch 1's optional one-word change, "differ in nothing but", stays the orchestrator's option. This reply reads the declaration's last sentence as accurate and gives no reason to take the change.

## 4. Ruling: KEEP, one ruling reconciled with batch 1's two KEEPs

OLD, NEW, KIND (CLAIM), REASON WORD and DECLARATION all stay as drafted, and no text changes. Under rule 3, the keep is recorded in the entry's CHECK field. The recording, to be made in the one pass with batch 1's edits:

1. **CHECK: append the task (a) line exactly as batch 1 gives it**, unchanged.
2. **CHECK: append one task (d) line** covering Mimo A2 (task (d)) and Atria A2 (point 2). It replaces the missing batch 1 line, which cannot be recovered, and is written again here from the batch 1 summary together with this ruling. Exact text:

````text
After the cross-examination (S90, task (d): Mimo A2 on O24, O46, N17 and N25, and Atria A2, point 2, on O24, O36 and O46; both R51 STANDS): the moved verdicts both replies name were re-examined and ruled KEEP. Every move named is toward the fixed verdict, and both replies grant that the declaration accounts for it. On the S81 reading file 11 was already AGREE on O24, O36 and O46, so no mark moves; what goes is file 11's "one account … pairwise of one kind", which pulled against them, and the declaration's first sentence and its "without that premise nothing more follows" state that withdrawal. The verdicts rest on text W19.2 leaves unchanged: L23, Derivation 9 and L307's reassigned-component clause (O46), L299 as W58(i).1 words it (O36), and Derivation 3 (W17.3) with L257 s2 (O24), whose old support in file 11's general Consequence is narrowed as the declaration's last sentence says. "Different candidates" in L560 holds by Part V's definition of a candidate, and "one answer profile" is (i). No case moves away: N17 moves toward on its first two questions or not at all, and N25's second question holds on either reading.
````

3. **CASES AT RISK, O36:** append to the O36 bullet, exact:

````text
Atria (S90, part A2) reads this as a move toward: file 11's "one account … pairwise of one kind" could have merged the written candidate with the unwritten one. The move is the declared withdrawal, and no mark moves (S81 read file 11 AGREE, on L301).
````

4. **CASES AT RISK, N25:** batch 1's edit stands (record Mimo's "toward" reading beside "watched"). Nothing is added for Atria.
5. **Batch 1 reading, edits, item 7:** "CHECK: append the task (d) KEEP line. Its exact text is in the missing ruling file …" is met by line 2 above.

**Conflicts: none.** A keep changes no text. R21 (W58(i).1) is misdescribed by the reply as unchanged, but the reply raises no point on it, and R21's record of O36 agrees with this ruling. R55 is found consistent with R51 in the reply's point 1, and it is not contested there.
