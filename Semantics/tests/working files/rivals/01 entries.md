# Hard-to-vary through rivals and problems: change entries for the revision-2 change list

**DRAFT, 25 September 2026. Not frozen, and not yet in the change list.** This file holds five entries: two new ones (W59.1, W60.1) and three existing ones edited (W34.1, W33.1, W38.1). Each is written in the change list's format, to be spliced into `Semantics/tests/Revision 2 - change list, draft of 23 September.md`.

*Written by a subagent for the orchestrator.*
- **Read:** draft 3's theory text in full; the change list (its frame, and the entries W1.1, W38.1, W36.1, W34.1, W33.1, W35.3, W19.2, W7.4, W7.5 and W3.2); the revision note; `tools/s89_apply_changes.py`; file 11 at L140–L163, L295–L319, L345–L367 and L516–L540; file 00 through the correction-sticks analysis's quotations of it; both analyses of 24 September, with the model scripts folder listed; the S81 case book (O1, O2, O8, O24, O27, O36, O45–O48); the N-case book (N1–N7, N24, N25); D3-T `final.md`; Deutsch chapter 1 in the extracted text, pp.16–31.
- **Not done:** the repository was read only. Nothing was written into `authority/`, and the Pinker folder was not opened.
- **Line numbers:** "L" alone means file 11, as in the change list, and "D3:L" means draft 3's theory text.

**Kinds, and how this file is ordered.**
- Four entries change the theory text, and all four are CLAIM.
- W38.1 is META, and it changes only the note of sources and departures.
- In the change list, W59.1 goes directly after W33.1, and W60.1 directly after W31.1. The program orders the entries by position in file 11 in any case.

## 1. What changes, in brief

- **Part VI.**
  - The counting lemma goes. That is W34.1, whose OLD is widened to take in the label "Hard-to-vary" and the containment \(\operatorname{Pres}(F')\subseteq\operatorname{Pres}(F)\), and W33.1, which drops "More reach constrains variation; …" and "… shown by Pres, and it grades nothing".
  - Its paragraph keeps W33.1's three sentences on commitments that do no work, under the label "Commitments that do no work".
  - Two paragraphs follow it, "Rivals" and "Problems" (W59.1). They state hard-to-vary as the owner put it on 24–25 September:
    - A rival is a competitor that differs in what it claims, not a redescription.
    - Two rivals that both fit what is established pose a problem for the question.
    - Where the rivals conflict at a pair of the contract, a test there solves the problem.
    - Where they conflict at no pair of the contract, the question cannot settle it. Being easy to vary is exactly having such a rival, and the remedy is a finer question.
    - No list of rivals is supposed, and nothing counts, grades or ranks.
- **Part VIII.** After "Historical index", a paragraph "A failed answer stays failed" (W60.1). On a fixed question, every candidate that gives an answer the target is established not to give, at a pair of the contract, fails (A). No record is needed. The exclusion stands or falls with the background and instruments of the test, for every such candidate alike. A narrowing that drops the pair is a different question, and the original failure stands.
- **The sources note (W38.1).** *Idle parts*, *Reach* and *Surprise and problems* are rewritten, and a line *Hard to vary* is added. It maps rivals and problems onto Deutsch pp.16, 17 and 20–22 and records three remaining departures.

## 2. The decisions

1. **The Pres containment is dropped, not kept as a remark under another name.** The five reasons are in W34.1's REASON. In short:
   - It is trivial, and nothing uses it.
   - Its only possible extra content, strictness, depends on how \(E\) and the family are written.
   - Its counts follow the declared family and the wording. They even make a bad rescue look harder to vary.
   - It rests on "explanatory jobs" and a family \(\mathcal V\) that the theory never defines or declares.
   - Under any name it invites reading as a grade.
2. **The definition of reach goes with it.** It existed to define the lemma's one noun use of "reach". Its one clause that a verdict used (N4) is kept in W59.1: whether a candidate is an account of a question is fixed by the candidate and the world, whether or not anyone has asked the question.
3. **Rivals are defined by conflict, and "problem for p" is a relational term.**
   - Rivals are offered in place of each other and are not one account on \(C\) in Derivation 2's sense. The two kinds of problem are split by where they conflict: at a pair of \(C\), or at none.
   - "Conflict" is defined so that each claim made about the two kinds is true. In particular, kind (ii) says "no test … is sure to solve" it, not "no test can", because an (F1) failure of one rival can still refute it on \(C\).
   - The bold term is "problem for \(p\)". The bare word keeps its passing sense at D3:L397 and D3:L399.
4. **(B) goes in Part VIII, after "Historical index".** It is the index result applied to one pair. It is not a Part XVI derivation, because its proof is (A) read once. It says what "established" requires (a usable receipt, Part IX) and applies (K3)'s caveat to every candidate alike.
5. **The mechanics.**
   - W34.1's OLD had to widen to the start of L315: the label and the lemma are file-11 text that no entry touched. Its NEW is replaced, and it keeps its id.
   - W33.1's OLD is unchanged, and its NEW is cut to its three kept sentences.
   - These two OLDs stay disjoint, separated by the one space that was between them.
   - W59.1 is an insertion anchored on the Part VII rule and heading (L317–L319), as W38.1 anchors on L7–L9.
   - W60.1 is an insertion anchored on the last sentence of "Historical index" (L365).
   - No OLD matches text that is itself the NEW of another entry. Where the text to replace was an entry's NEW (W34.1's reach sentence; W33.1's first and last sentences), that entry's NEW is edited instead, as the task asks.
6. **The ids.** W59 (hard-to-vary through rivals and problems) and W60 (a failed answer stays failed) are new items after W58, from the owner's position of 24–25 September. The group is H. The orchestrator may renumber them.

## 3. What depended on Pres in draft 3, and what each becomes

Found by grep of draft 3 for Pres, job, reach, \(\mathcal V\), vary, hard-to-vary, rival and problem, and read in place.

| draft 3 | text | depends on Pres? | becomes |
|---|---|---|---|
| D3:L313 | the lemma, W34.1's reach sentence, W33.1's sentences | yes | W34.1 and W33.1 edited; W59.1 added after |
| D3:L69 | W36.1: "how hard an account is to vary is a separate matter (Part VI)" | pointer only | **kept.** It now lands on W59.1's "easy to vary", and it stays true: a candidate with a kind-(ii) rival can still be an account |
| D3:L299–302 | (D), \(\operatorname{Boundary}_{E,p}\) over "a declared family \(\mathcal V\)" | no | kept; now the only use of \(\mathcal V\) (section 4) |
| D3:L335 | Part VII, "a rival account", "The rival's supposed structure" | no | kept; it uses "rival" in the new sense (a candidate offered against the eliminative account, conflicting where the contract introduces the components) |
| D3:L397, L399 | "problem-directed activity", "an available problem" | no | kept; the defined term is "problem for \(p\)" |
| D3:L423 | the recognized difficulty (W35.3) | no | kept; W59.1 links to it ("can be") |
| D3:L520 | dependence order | no (Pres was never listed) | kept; see findings |
| D3:L526–540 | Part XV | no (neither (H) nor Pres is listed, and "A mathematical error" names only the finite monotone theorem, (I2), (O1), (T2), (CT2) and Derivations 1–3) | kept; W60.1 is not added to its list, since a counterexample to it would be a counterexample to (A) |
| sources note | *Explanation*, *Idle parts*, *Reach*, *Surprise and problems* | *Idle parts* ("grades nothing") and *Reach* (jobs) yes; the other two no | W38.1 edited: *Idle parts*, *Reach* and *Surprise and problems* rewritten, *Hard to vary* added, *Explanation* kept |
| revision note | declarations of W34.1 and W33.1 | yes | regenerated by the program from the edited declarations |

After the change, the theory text has no Pres, no "job" and no "Hard-to-vary". "Reach" survives only as a verb (lines 403, 562 and 630 of the new theory text) or in "reachability". \(\mathcal V\) survives only in (D) (and \(\mathcal V_A\), the aesthetic value set, which is unrelated).

## 4. The two gaps found earlier

- **"The variation family is not a declared input": it dissolves in substance.**
  - After the change, \(\mathcal V\) occurs only as the domain of (D).
  - There, whether \((v,w)\in\operatorname{Boundary}_{E,p}\) is fixed by \(v\) and \(w\) alone, since it holds exactly when \(\operatorname{Account}(E_v,p)\neq\operatorname{Account}(E_w,p)\). No claim about a candidate or a pair of edits turns on which family is declared.
  - No case, definition or derivation uses (D); the dependence order only places it.
  - The earlier worry was that a grade or a count over \(\mathcal V\) could be chosen "from the verdict wanted" (D3:L516). With Pres gone, nothing grades or counts over \(\mathcal V\).
  - If the orchestrator wants the letter covered too, a later revision can add "the family \(\mathcal V\) of (D)" to Part XIV's declared inputs. No entry is drafted for it.
- **"Job is undefined": closed.** After the change "job" occurs nowhere in the theory text (grep, 0 hits). Its two uses, the lemma and W34.1's reach definition, both go. Nothing defines it, and nothing needs it.

## 5. The entries

Each block below is a complete entry in the change list's format. W34.1, W33.1 and W38.1 replace their blocks of 23–24 September; W59.1 and W60.1 are new.

### W34.1 — Part VI: the job-counting lemma and Pres are dropped, and reach with them

- **STATUS:** applied
- **GROUP:** C; edited 25 September (group H)
- **ITEM:** W34; W59
- **FILE-11 LINE:** 315
- **WHERE:** Part VI, "Hard-to-vary" (L315), from the bold label through the end of the first sentence, where Pres is defined. **Edited on 25 September.** Before, this entry's OLD was only the Pres clause (the last part of that sentence) and its NEW added the definition of reach. The OLD is now widened back to the start of the line, taking in the label and the lemma, which are file-11 text that no other entry touches. The NEW is now only the label of the paragraph that W33.1 writes. The single space after this OLD and W33.1's OLD are unchanged.
- **REASON WORD:** change of claim
- **KIND:** CLAIM
- **CHECK:** check 2, SOUND, on the text before 25 September. W34.1 was contested by neither S90 reply. **25 September:** OLD widened and NEW replaced under the owner's position of 24–25 September (see REASON). Checked by the drafter only. OLD occurs once in file 11, starts and ends on L315, and ends where W33.1's OLD begins less one space, so the two do not overlap. The whole list, spliced, applies with `tools/s89_apply_changes.py --self-test`. No outside reader has seen this text.
- **OLD:**
````text
**Hard-to-vary.** For explanatory jobs \(F\subseteq F'\), \(\operatorname{Pres}(F')\subseteq\operatorname{Pres}(F)\), where \(\operatorname{Pres}(F)=\{v\in\mathcal V:\forall f\in F,\operatorname{Account}(E_v,f)\}\).
````
- **NEW:**
````text
**Commitments that do no work.**
````
- **DECLARATION:** Part VI no longer states that, for sets of explanatory jobs \(F\subseteq F'\), \(\operatorname{Pres}(F')\subseteq\operatorname{Pres}(F)\), and no longer defines \(\operatorname{Pres}\); its paragraph on commitments that do no work is headed as such.
- **REASON:**
  - **The owner's position (24–25 September).** Hard-to-vary is not a count over a listed set of versions. No one can list all rivals, even in principle, and the set does not matter. File 11's lemma is exactly such a count: an inclusion between subsets of a family \(\mathcal V\) of variants of \(E\), indexed by sets of "explanatory jobs". It is replaced by rivals and problems (W59.1).
  - **The containment is dropped, not kept under another name.** Five reasons.
    1. It is trivial. Its proof is one line from the definition: "Preserving every job in the larger family includes preserving every job in the smaller family" (F00:L377). No case, derivation or definition uses it: in draft 3, Pres occurs only at D3:L313.
    2. The only content it could add beyond that line is strictness. Strictness needs a witness in the family, and whether one exists turns on the menus and on how \(E\) is written. The same correction has a witness when written as a changed rule (2 → 1) and none when written as a mechanism (1 → 1). (Correction-sticks analysis, §1(3), §2 limit (iv), CE1–CE2.)
    3. Its counts follow the declared family and the wording, not the explanation. They flip with the menus: 1:96 against 64:1. They flip with redescription: one rain part written as one, two or five parts gives 2 → 1, 4 → 3 and 32 → 31 (correction-sticks analysis, §2, "What kind of text"). Inside its own family a bad rescue even registers as harder to vary, 4 → 2 (§1(2), A4(ii)). So it cannot carry the idea its label names.
    4. It rests on two inputs the theory never supplies. "Explanatory job" is defined nowhere (correction-sticks analysis, §5 item 3, and its Appendix A (a)). The family \(\mathcal V\) is neither a declared input nor an index (§4, losses; error-correction analysis, option (c), costs).
    5. Kept under another name, it would still invite reading as a grade. The error-correction analysis finds that "A Pres grade would mostly re-measure how narrow the question is" (option (c)). D3:L25 and D3:L516 refuse a merit function.
  - **What is lost.** Nothing that a verdict, a derivation or another definition uses. Deutsch's comparative usage ("most constrained") gets no home, and it had none that D3:L516 allowed.
  - **Reach goes with the lemma.** W34.1 defined reach so that the lemma's one noun use, "More reach constrains variation", was defined where it was first used. With the lemma gone, the theory has no noun use of "reach": the uses at D3:L151, L245, L331, L397, L556 and L624 are verbs or "reachability". A definition that no text uses would keep "jobs" in the theory. Its one clause that a verdict used, that standing is fixed by the candidate and the world and not by what anyone has checked (N4), is kept in W59.1, stated for questions.
  - **The two gaps found earlier.**
    - "Job is undefined": closed. After the change "job" occurs nowhere in the theory text (grep, 0 hits).
    - "The variation family is not a declared input": closed in substance. \(\mathcal V\) now occurs only as the domain of (D), \(\operatorname{Boundary}_{E,p}\), where whether a pair \((v,w)\) belongs is fixed by \(v\) and \(w\) alone. No claim about a candidate or a pair of edits turns on which family is declared, and no case or other definition uses (D).
  - **The label.** W33.1's sentences on commitments that do no work stay, so the paragraph needs a label in place of "Hard-to-vary". Every paragraph of Part VI after (D) has one. "Commitments that do no work" uses W33.1's own phrase and adds no new word.
- **CASES AT RISK:**
  - **O36: toward.** Pres counted variants nobody wrote, which the error-correction analysis found in tension with O36 (option (c)). Nothing in Part VI now speaks of an unwritten route, and W59.1 says that a candidate nobody has offered is no one's rival.
  - **N4 (O56).** Q1 was "toward" through reach being "fixed by E and the world". It stays toward through W59.1's sentence: whether a candidate is an account of a question is fixed by the candidate and the world, whether or not anyone has asked the question. If W59.1 were dropped, Q1 would hold on realism alone (D3:L67), and the declared move toward would go. Q2 rests on Deploy and Attempt, which are unchanged.
  - **N5 (O57)** was watched under reach. It holds under this entry and moves toward under W59.1.
  - **N7 (O59).** "Bea's account is fuller" was read as reach (correction-sticks analysis, §3, row N7). It now rests on (E): Bea's account is also an account of the further question why the rise works only in that range, and Maya's is not. It holds.
  - **No row rested on the lemma.** N1, N2, N3, N24, N25, O24, O45, O46, O47, O48 and D3-T hold.
- **GAIN:** Part VI no longer carries a count over a family nobody declares, on jobs nobody defines. Both undefined inputs leave with it.
- **LOSS:** The containment (H) inherited from file 00 goes, and with it "the containment need not be strict" (W33.1). Reach is no longer defined, and Deutsch's reach has no named counterpart (sources note).

### W33.1 — Part VI: (E) tolerates a commitment that does no work; (B) marks it

- **STATUS:** applied
- **GROUP:** C; edited 25 September (group H)
- **ITEM:** W33; W59
- **FILE-11 LINE:** 315
- **WHERE:** Part VI, "Hard-to-vary" (L315), the lemma's last sentence ("More reach constrains variation; …"). **Edited on 25 September.** Before, NEW kept that sentence and added four after it. It now drops that sentence and the last of the four, on Pres, and keeps the three on commitments that do no work, byte for byte. W34.1's new label heads the paragraph.
- **REASON WORD:** change of claim
- **KIND:** CLAIM
- **CHECK:** check 2, FIX. Four defects: under the drafted test every commitment of L313's infinitary support "does no work"; "any support" could be read as "some support"; the declaration's "or" let one half of the test suffice; and "measure", as in W36.1. NEW scopes the label ("does no work by itself in the candidate"), states both halves for every support, says what happens when Γ is infinite, and reads "a separate matter, shown by Pres". Cases: O2's "this derives L275 s2's rule" is struck (circular); O19 is added, watched.
  - S90 cross-examination: s90_xexam_atria_C, point 3 (R24 STANDS, naming a move toward on N1) — KEEP, after the cross-examination. Cross-examination of revision 2 (S90 part C): Atria gave STANDS and named, under (d), a declared move toward the fixed verdict on N1 ("Strike it out and the account works exactly as before" read as the no-work test, with \(\{d\}\) critical in no support), and claimed that the test is equivalent to "\(\{d\}\) critical in no support". Mimo gave STANDS with no point. Ruled KEEP after the cross-examination. The move on N1 is toward, on the reading where the sentence constrains nothing, and the declaration accounts for it. The claimed equivalence is false (Interference, L309: \(\{b\}\) is critical in no support but fails the addition half), and NEW does not assert it; NEW's "then" consequences follow from the two-halved test. N1's watch on the redundant-route and unfaithful readings stays as recorded. It comes from (B), L307 and (F1), not from this entry. O45, N2 and O8 hold.
  - **25 September:** NEW and the declaration edited under the owner's position of 24–25 September. Two sentences are removed: file 11's "More reach constrains variation; the containment need not be strict; counting jobs is not a warrant.", which NEW had kept, and NEW's last sentence, "How hard an account is to vary is a separate matter, shown by \(\operatorname{Pres}\), and it grades nothing." The three sentences between them are unchanged, and R24's KEEP was ruled on them. The REASON WORD moves from clarification to change of claim, because a file-11 sentence is now withdrawn. Checked by the drafter only; no outside reader has seen this text.
- **OLD:**
````text
More reach constrains variation; the containment need not be strict; counting jobs is not a warrant.
````
- **NEW:**
````text
(E) has no condition that each commitment do work. A commitment \(d\) does no work by itself in the candidate when every support stays a support after \(d\) is added to it and after \(d\) is removed from it: a candidate carrying \(d\) then meets (E) exactly when it meets (E) without \(d\), and \(\{d\}\) is critical in no support (B). When \(\Gamma\) is infinite, a block of such commitments can still be critical (Infinitary support).
````
- **DECLARATION:** Part VI no longer says that more reach constrains variation, that the containment need not be strict, or that counting jobs is not a warrant; it now says that (E) has no condition that each commitment do work; that a commitment such that every support stays a support when it is added and when it is removed does no work by itself in the candidate, leaves the candidate's standing under (E) unchanged and is critical in no support; and that when the commitments are infinitely many a block of such commitments can still be critical.
- **REASON:** Worklist W33 (source point 2; verify obs 2, PARTLY CONFIRMED; M7). The source counts superfluous features as a defect. (E) accepts a candidate that carries a commitment doing no work, and Part VI reports such a commitment only through (S) and (B). The text never says this (worklist). The plan's wording, "(E) is fidelity: a commitment that does no work passes (E) …", is made exact in two places. (i) (E) is not only fidelity: non-circular dependence and non-vacuity are also conjuncts. So the sentence says instead that (E) has no condition that each commitment do work. That is true, because non-circular dependence asks only for some nonempty block. (ii) "Does no work" is given a test in Part VI's own terms: adding the commitment to any support, or removing it from any support, leaves a support. Both halves of the claim follow from that test: Γ is a support exactly when Γ∖{d} is, and {d} is critical in no support. The addition half excludes an interfering commitment (Part VI, Interference). The removal half excludes a redundant route (Redundant routes; L309), since removing it from the support in which it is the only route leaves no support. The sentence states no condition (plan 1.2; conflict 12). The departure from the source goes in the sources note (W38). It holds under every W20 option, because it is stated through (S) and (B), not through the wording of non-circular dependence (skeleton conflict 11).
  - **25 September.** The owner's position is that hard-to-vary is not a count over a listed set of versions (W34.1, REASON). File 11's sentence "More reach constrains variation; the containment need not be strict; counting jobs is not a warrant." comments on the containment that W34.1 drops, and its words "reach", "containment" and "jobs" have nothing left to refer to. The last sentence named Pres, which W34.1 drops. "It grades nothing" is still true, and it stays said where it belongs: D3:L25 and D3:L516 supply no merit function, and W59.1 says that nothing in rivals and problems counts, grades or ranks. W36.1's "how hard an account is to vary is a separate matter (Part VI)" still lands, on W59.1's "easy to vary". The three kept sentences answer the source's point on superfluous features and do not depend on Pres, as the error-correction analysis confirms (section 2, "What the three situations show": "An idle part cannot make a candidate an account").
- **CASES AT RISK:**
  - O36, O45 and O47 hold. P in O36 is critical, not idle. The second spring in O45 fails the removal test: removing it from the support in which it is the only spring leaves no support. So it is a route, not idle. The locked room in O47 fails the addition test, so it is interference, not idle.
  - O2 holds. The bell part does no work for the tide question. The candidate meets (E) with it exactly when it meets (E) without it, and without it the almanac restates the answer (L275), so it fails either way. This derives L275 s2's rule.
  - N1: toward if the sun-god sentence constrains nothing, or is not among the active commitments. Watched: if it is read as a second component that keeps the tilt steady, it is either a redundant route or an unfaithful component. As a redundant route it fails the removal test, and the verdict "not part of what explains" moves to DISAGREE. As an unfaithful component it fails the addition test; that is interference, and "Tomas explains" is at risk. Which reading applies turns on how Γ is typed (W20, held).
  - N25 does not move: the difference between dog and turtle is a matter of Derivation 2's kinds (W19, held). N2 does not move: the patch was fitted after the fact, which is the historical index. N7 and O8 hold: scope is untouched.
  - **25 September.** No row rested on the two removed sentences. N1 keeps R24's move toward, which came from the three kept sentences. N2 and N25 now also have W59.1's reasons (see there). O36 moves toward under W34.1.
- **GAIN:** The split between (E) and (B) is stated, with a test for idleness that excludes interference and redundant routes. After 25 September the paragraph says only that, and no longer comments on a count.
- **LOSS:** The theory now says openly that it tolerates idle parts, which the source counts as defects. The explicit "it grades nothing" moves out of this paragraph (W59.1; D3:L25; D3:L516).

### W59.1 — Part VI: hard-to-vary stated through rivals and problems

- **STATUS:** applied
- **GROUP:** H
- **ITEM:** W59 (new: the owner's position of 24–25 September on hard-to-vary)
- **FILE-11 LINE:** 317–319
- **WHERE:** Part VI, after its last paragraph (L315, headed "Commitments that do no work" after W34.1) and before the rule at L317 that opens Part VII. Two paragraphs are inserted, "Rivals" and "Problems". The anchor is L317–L319 (the rule, the blank line and the Part VII heading), kept byte for byte, as W38.1 anchors on L7–L9. No other entry touches L316–L319.
- **REASON WORD:** change of claim
- **KIND:** CLAIM
- **CHECK:** drafted 25 September; checked by the drafter only. OLD occurs once in file 11 and overlaps no other OLD. The whole list, spliced, applies with `tools/s89_apply_changes.py --self-test`: one diff hunk, beside this entry. Every sentence was checked against its pointer in draft 3 (see REASON, "What each sentence rests on"). No outside reader has seen this text.
- **OLD:**
````text
---

# Part VII — Exact constructions
````
- **NEW:**
````text
**Rivals.** Two explanatory candidates for one question \(p\) are **rivals** when each is offered as an answer to \(p\) in place of the other and they differ in what they claim on \(C\), not only in how it is written: they are not one account on \(C\) in the sense of Derivation 2 (paired active components with one anchor and one kind on \(C\), and one answer profile). Each is offered for the whole of \(p\), and so claims the conditions of (E) at every pair of \(C\), tested or not. Two candidates **conflict** at a pair \((a,b)\) when, whatever the target's relations there, not both meet (F1), (F2) and (A) there, as when their answers there differ, or two of their active components with one anchor have different relations there. A result is **established** for an assessor who holds a usable receipt for it (Part IX); by (K3), a result that tells against a candidate tells against it only together with the background and instruments of the test that yields it. A candidate **fits** what is established when no established result shows it failing a condition of (E). No list of all rivals is supposed: the rivals of a candidate are those someone has conjectured, and a candidate that nobody has offered is no one's rival.

**Problems.** Two rivals that both fit what is established pose a **problem for \(p\)**: a conflict between ideas that what is established has not settled. It is of one of two kinds. (i) The rivals conflict at some \((a,b)\in C\). Establishing what the target does there is then a **test** that solves the problem whatever it shows, since afterwards at most one of them fits; an answer it refutes stays refuted on \(p\) (Part VIII). (ii) They conflict at no pair of \(C\): the contract does not contain their conflict. Their answers then agree at every pair of \(C\), so no established answer holds one of them to account without the other, no test the question admits is sure to solve the problem, and where both meet (E) on \(C\) both are accounts of \(p\). A candidate is **easy to vary**, in the sense used here, when it and a rival pose a problem of the second kind, and a criticism that it is easy to vary supplies such a rival (Part IX). Where both rivals are accounts on \(C\), a claim that one is right and the other wrong is a claim that some admitted change separates them, and must supply it, as a claim that one assignment of anchors is "really" right must (Derivation 2, Consequence). The remedy is a finer contract, which is a new question (Part III); whether a candidate is an account of a question is fixed by the candidate and the world, whether or not anyone has asked the question (Part I). Nothing here counts rivals, grades a candidate or ranks candidates. A problem that a system represents can be a recognized difficulty (Part X), as when giving one answer to \(p\) meets a claimed obligation only by dropping a rival that fits as well, and keeping such a rival is protected (Part XI).

---

# Part VII — Exact constructions
````
- **DECLARATION:** Part VI now defines rivals for a question (candidates each offered as an answer in place of the other that are not one account on its contract), when two candidates conflict at a pair, when a result is established (a usable receipt, with (K3)'s caveat) and when a candidate fits what is established; it says that no list of all rivals is supposed; that two rivals that both fit pose a problem for the question, which a test at a pair of the contract where they conflict solves whatever it shows; that where they conflict at no pair of the contract their answers agree at every pair and no test the question admits is sure to solve it; that a candidate is easy to vary when it and a rival pose a problem of that second kind, and a criticism that it is easy to vary supplies such a rival; that where both rivals are accounts, a claim that one is right and the other wrong must supply an admitted change that separates them, the remedy being a finer contract, which is a new question; that whether a candidate is an account of a question is fixed by the candidate and the world, whether or not anyone has asked it; that nothing here counts, grades or ranks; and that a represented problem can be a recognized difficulty.
- **REASON:**
  - **The owner's position (agreed in conversation, 24–25 September).** Hard-to-vary is not a count over a listed set of versions: no one can list all rivals, even in principle, and the set does not matter. A variation is a competitor, and two discovered rival explanations that both fit constitute a problem. Three refinements were agreed:
    1. Rivals must differ in what they claim, not only in wording, since a redescription is one explanation (Derivation 2).
    2. "Fit" means fit the whole question, every admitted change, tested or not. This splits problems into two kinds. Rivals that differ at some change the question covers are settled by a test there. Rivals that differ nowhere the question covers cannot be held to account by the question, and that is the mark of an easily varied explanation ("Demeter grieves" against "Persephone is underground").
    3. Deutsch's "easy to vary" judges an explanation before anyone offers a rival. On this view the criticism is the producing of the rival, and no grade or count is needed.
  - **What the theory already half-said.**
    - Revised Derivation 2's Consequence (D3:L562): two candidates with one answer profile; a claim that one is "really" right must supply a separating admitted change; "The remedy is a finer contract, which is a new question".
    - The recognized difficulty (W35; D3:L223, L423).
    - Grievance 4 (D3:L43): an exclusion is caught "by any criticism that supplies the excluded change". This is the model for "a criticism that it is easy to vary supplies such a rival".
    - The error-correction analysis lists what the theory leaves open: "A choice between candidates the contract does not tell apart" (section 1, citing D3:L562). It also finds that a new adjustable part is "caught in the verdict whenever the question is left open … only as a fact that a later test would show" (section 2). That is the first kind of problem, and the test is the later test.
  - **Why it is stated this way.**
    - *Rivals.* "Offered as an answer to \(p\) in place of the other" makes a rival a competitor, as the owner's "a variation is a competitor" asks. So two compatible accounts are not rivals merely because they differ. A fuller account beside a leaner one (N7), and two real springs (O45), are compatible accounts of this kind.
    - *Not one account.* "Not one account on \(C\) in the sense of Derivation 2" is refinement (1), in the theory's own relation. The parenthesis gives that relation's content, as Derivation 2's (ii) states it: paired active components with one anchor and one kind on \(C\), and one answer profile. With "one anchor" in it, the parenthesis keeps O46's spring and cable apart, as W19.2's REASON requires.
    - *The whole of \(p\).* "Each is offered for the whole of \(p\) … at every pair of \(C\), tested or not" is refinement (2). It rests on realism and on (E) quantifying over every pair (D3:L67, L265).
    - *Conflict.* It is defined so that the two kinds are exhaustive and each claim about them is true. The two named ways follow from (Q) and (F1). \(\operatorname{Ans}_p(a,b)\) is one value, so candidates with different answers there cannot both meet (A). An anchor's projected relation is one relation, so two components with one anchor and different relations there cannot both meet (F1).
    - *Established.* The (K3) clause is K3's own caveat (D3:L389). What is established is read through Part IX's usable receipts, so the semantics gains no new input. The same definition serves W60.1.
    - *Problem for \(p\).* The bold term is "problem for \(p\)", not "problem". The bare word keeps the passing sense it has at D3:L397 ("problem-directed activity") and D3:L399 ("an available problem"). There a first representation is built from a problem, and two rivals would make no sense.
  - **What each sentence rests on (checked in draft 3).**
    - Kind (i). "At most one of them fits": at the pair, not both meet the conditions whatever the target does. "An answer it refutes stays refuted on \(p\)": W60.1.
    - Kind (ii).
      - "Their answers then agree at every pair of \(C\)": different answers at a pair would be a conflict there.
      - "No established answer holds one of them to account without the other": equal answers stand or fall together under (A).
      - "No test the question admits is sure to solve the problem": at every pair some relations of the target let both meet the conditions.
      - "Where both meet (E) on \(C\) both are accounts of \(p\)": this is (E) itself.
      - The sentence claims no more than this. A test can still refute one of the two for an error of its own, as when an anchor that only one of them uses fails (F1). That is why the text says "no test … is sure to", not "no test can".
    - "Where both rivals are accounts on \(C\), a claim that one is right and the other wrong … must supply" a separating change. If both meet (E) on \(C\), nothing in \(C\) separates them, so such a claim is about a change outside \(C\), as in Derivation 2's Consequence. The qualifier "where both … are accounts" is needed: without it, an (F1) failure of one rival inside \(C\) would be a counterexample.
    - "Whether a candidate is an account of a question is fixed by the candidate and the world, whether or not anyone has asked the question": (E) uses neither \(O_p\) nor \(\rho_p\) (D3:L231–265), and whether a transport is faithful is independent of acceptance (D3:L67). This is W34.1's reach clause, kept and stated for questions.
    - The recognized-difficulty sentence is an instance of W35.3's second clause (D3:L423): "what the system holds meets a claimed obligation only by failing a protected one". It says "can be", as D3:L223 does for a violation.
  - **The easy-to-vary sentence is a definition, not a grade.** It needs an offered rival, which is refinement (3). It is relative to \(p\) and to what is established. It is symmetric between the two rivals. It counts nothing and ranks nothing.
  - **The correction-sticks analysis supports this form.** It found that no Pres statement can separate a good rescue from a bad one on the symmetric record (1:1, 4:4, 6:6). Only "a job holding a pair where they differ" can, and "it is (E) on that job, not a count" (§1(2); §2, limit (iii)). That job is kind (i)'s test.
  - **The owner's example.** "Demeter grieves" and "Persephone is underground" (as the cause, with no grief) cut the target differently: grief is a mediating component that the other lacks. So they are not one account on \(C\). On the Greek question they give one answer at every pair, so they conflict at no pair of \(C\), which is kind (ii). A change that set the mediating state on its own would lie outside that contract.
  - **Labels do not make rivals.** Two tellings that differ only in labels, a dog or a turtle (N25), are one account in Derivation 2's sense, not rivals. This agrees with Deutsch's own reduction of the Persephone and Freyr myths to one core explanation (p.21). The sources note records it.
- **CASES AT RISK:**
  - **O24 (the unused joint setting): toward.** The two arrangements fit every tested setting and conflict at one untested joint setting, reachable by hand and so a pair of \(C\). That is kind (i). "the record has not chosen between them" is a conflict that what is established has not settled, and "One reachable setting is enough" is the test that solves it whatever it shows. File 11 carried O24 through Derivation 3 and L257 s2 (W19.2, CASES AT RISK). It now has a direct statement.
  - **O36 (a premise both routes use): toward.** "A candidate that nobody has offered is no one's rival", with "no list of all rivals is supposed", is O36's "a fact about a candidate nobody has written". Pres, which counted such candidates, goes (W34.1).
  - **O45 (the spring nobody mentioned): holds.** The account holds both springs as one candidate, and no candidate is offered in its place. Two real springs are compatible, and a fuller candidate is not a rival for being different. The verdict rests on D3:L231 (W20.1) and D3:L307, which are untouched.
  - **O46 (the cable that used to be a spring): holds, on firmer text.** The cable account anchors a different subnetwork, so it is not one account with the spring account. Offered in its place, it would be a rival, not a survivor. Its success is its own (D3:L307).
  - **O48 (the forbidden wire): holds; watched.** A reader might take a conjectured arrangement with the forbidden wire as a rival that keeps the unseen setting open. It poses no problem. A rival must fit what is established, and a candidate whose component needs a wire the devices are established to lack fails (F1) against that result. O48 rests on Derivation 3 and D3:L475, which are untouched. This entry speaks of candidates for a question, not of a selection population.
  - **D3-T (O76): holds, and moves toward on its reason.** The discarded design failed a tried setting, so it does not fit what is established and poses no problem. "Ivo would need two designs that both pass and still differ at the untried setting" describes a problem of kind (i), and none exists. The verdict rests on Derivation 3, which is untouched.
  - **N1 (the sun god): holds.** No candidate is offered in place of Tomas's. The sun-god sentence is W33.1's matter, a commitment that does no work, not a rival. A telling that swaps the god for another god is one account with Tomas's on \(C\), not a rival.
  - **N2 (the myth amended): holds (No), and moves toward on its reason.**
    - The original myth fails the southern reports, so it no longer fits.
    - The amended myth's "No" rests on (E): (F1), and non-circular dependence as W20.2 words it. This entry does not touch that.
    - "Had the sailor reported something different, the storyteller could as easily have changed the story another way" is now statable. Before the report, a variant that sends the warmth south conflicts with the myth at no pair of the Greek question, so the myth was easy to vary in the new sense (kind (ii)). The sailor's report is a pair at which the two conflict.
  - **N3 (a myth about winter): holds on both questions, and moves toward on the reason.**
    - "Its details … could be swapped for others that fit the Greeks' facts just as well" is a rival of kind (ii).
    - Q1's "No" rests on non-circular dependence, since the yearly return is written into the bargain. Q2's "an explanation … only in form" rests on W36.1. Neither moves.
    - Watched: a reader might carry "both are accounts of \(p\)" over to the myth. The text says so only "where both meet (E) on \(C\)", and the myth does not.
  - **N4 (O56).** Q1 stays toward through the sentence on questions nobody has asked (see W34.1). Q2 is unchanged.
  - **N5 (O57): toward.** The rule's two readings, by months and by seasons, are rivals. They conflict at no pair of the home question, and they conflict at the southern change. At home that is a problem of kind (ii). The remedy is a finer question, and a trial in the south is a test that solves it. "The rule itself cannot tell him which reading to trust … he needs what the rule leaves out … or else trial" says the same.
  - **N7 (two bakers): holds; watched.**
    - As written, the bakers do not offer their accounts in place of each other, so they are not rivals, and "both explain" rests on (E).
    - A reader who treats them as rivals finds that they conflict at no pair of Maya's contract. Each is then "easy to vary" relative to the other, in the defined sense. Nothing is graded, both remain accounts, and Bea's is also an account of why the rise works only in that range.
    - Risk: a reader who takes "easy to vary" as a defect pulls against "Leaving them unexplained does not weaken her explanation".
  - **N24 (two sealed sorts of matter): holds.** Asha's weak reading and Bram's claim use different queries, so they answer different questions and are not rivals for one \(p\) (D3:L151). The verdict rests on W45.1 and Part XIII's barrier.
  - **N25 (what holds the universe up).** Q1 holds on non-circular dependence. Q2 moves toward.
    - The dog and turtle stories pair their components with one anchor and one kind, and they have one answer profile. They are one account written two ways, not rivals.
    - Taken as rivals, a claim that one is right must supply an admitted change that separates them, and nothing inside the universe can supply one.
    - "As explanations they make the same empty claim … the difference between them is idle" is this. Q2 was watched under W19.2 and now has a direct statement.
  - **Others.** O1: its second half ("the series … is a retreat") stays SILENT, since nothing here reads a series; for its first half see W60.1. O27: holds. "The one test that would separate them" is a kind (i) test, and the robot's reinterpretation is (K3)'s caveat, which the established clause states. The attribution ("mostly") is not reached. O2, O8 and O47 hold.
- **GAIN:** The theory says what hard-to-vary comes to without a count, a family or a grade. An easily varied candidate is one with a rival that fits as well and that the question cannot separate from it. The remedy is a finer question, and the criticism is the rival. Case (i) states the crucial test, O24's case, directly.
- **LOSS:**
  - Two paragraphs (about 470 words) and five defined terms.
  - "Easy to vary" is symmetric and relative to what is established. It gives no ground for preferring either of two kind-(ii) rivals, which is Deutsch's comparative use.
  - A candidate nobody has challenged with a rival is not called easy to vary, however loose it is. That is refinement (3), and it gives up Deutsch's judgement before any rival is offered.
  - A candidate with a kind-(ii) rival is still an account of its question if it meets (E). Deutsch would say such an explanation explains nothing (sources note).

### W60.1 — Part VIII: a failed answer stays failed

- **STATUS:** applied
- **GROUP:** H
- **ITEM:** W60 (new: the owner's position of 24–25 September, "correction sticks without any record")
- **FILE-11 LINE:** 365
- **WHERE:** Part VIII, "Historical index" (L365). A paragraph is added after it, before the rule that closes Part VIII. The anchor is the paragraph's last sentence, kept byte for byte. No other entry touches L365.
- **REASON WORD:** clarification
- **KIND:** CLAIM
- **CHECK:** drafted 25 September; checked by the drafter only. OLD occurs once in file 11. The whole list, spliced, applies with `tools/s89_apply_changes.py --self-test`. Each claim was checked against (A), D3:L151, D3:L159, D3:L363 and (K3) in draft 3 (see REASON). No outside reader has seen this text.
- **OLD:**
````text
A new index is a new claim.
````
- **NEW:**
````text
A new index is a new claim.

**A failed answer stays failed.** Fix a question \(p\), a pair \((a,b)\in C\) and a value \(y\neq\operatorname{Ans}_p(a,b)\). By (A), a candidate for \(p\) whose answer at \((a,b)\) is \(y\), \(\operatorname{Ans}_E(\tau(a),\sigma(b))=y\), is not an account of \(p\), whether it is the candidate that gave \(y\) there and failed, that candidate offered again, a rival, or a changed candidate that keeps \(y\) there; and the same holds on every question with the same target and query whose contract contains \((a,b)\). Once it is established that the target's answer at \((a,b)\) is not \(y\), this is established of every such candidate alike, with no record of which candidates failed before or of how any was changed. Here "established" is meant as in Part VI: the assessor holds a usable receipt for the target's answer at \((a,b)\) (Part IX), and by (K3) the test that yields it tells against a candidate only together with the background and instruments it relies on; if they come into question, the exclusion does too, for every such candidate alike. A contract that omits \((a,b)\) makes a different question (Part III): an account on it does not answer \(p\), and the failure on \(p\) stands (Historical index).
````
- **DECLARATION:** Part VIII now states that on a question, a candidate whose answer at a pair of the contract differs from the target's is not an account of it, nor of any question with the same target and query whose contract contains that pair, whatever candidate it is; that once the target's answer there is established, by a usable receipt, this is established of every such candidate alike, with no record of earlier failures or changes; that by (K3) the exclusion stands or falls with the background and instruments of the test, for all such candidates alike; and that a contract omitting the pair makes a different question, an account on which does not answer the original, whose failure stands.
- **REASON:**
  - **The owner's position (24–25 September).** Correction sticks without any record. On a fixed question, any explanation that repeats the failed answer fails the basic test. A narrowing of the question after a failure is a different claim that does not answer the original, which stays failed (F11:L161; D3:L159).
  - **The correction-sticks analysis proves the true part and marks its limits.**
    - Its §1(1): "At the failed summer, yes, and no record is needed. (A) holds 'For every (a,b) ∈ C' … any candidate that answers 'south first' at the failed summer is no account on any job whose contract holds that summer: a rival, a rescue, or E0 offered again. This holds while the job is kept."
    - Its limits, all respected here. "Beyond the failed summer, no": the result speaks only of the pair \((a,b)\), and makes no claim about other pairs. "It is not a ratchet": the narrowing clause says a narrowed contract is a different question, not that narrowing is forbidden. "The binding is by the world's answer, not by the recorded observation" (Appendix A (b)): hence the receipt and (K3) clauses.
    - The theory text needs nothing from the analysis's Pres lemma (H\*), which W34.1 drops.
  - **The error-correction analysis** (section 1) lists "The failed claim stays failed" as [TEXT] and "A failed test refutes the conjunction of theory, background and the claim that the test did what was intended" (K3). It also names the save by blaming the background or the test (section 2). The (K3) clause answers it without a record: blaming the background or the instruments reopens the exclusion for every candidate alike, and exempts none.
  - **The hypotheses, stated in the text.**
    - A fixed question \(p\), and a pair of its contract.
    - A value that is not the target's answer there. \(\operatorname{Ans}_p(a,b)\) is one value of \(Y_p\) by (Q).
    - For the second clause, the same target and query, so that \(\operatorname{Ans}_{p'}(a,b)=\mathcal Q(D,a,b)=\operatorname{Ans}_p(a,b)\).
    - For "established", a usable receipt (Part IX), with (K3)'s caveat. The first sentence is a fact of (A) and needs no receipt. Only its being established does.
  - **Each clause, checked in draft 3.**
    - (A), D3:L247–251: the first sentence.
    - D3:L151 ("Two questions with the same \(D\) and different \((C,\mathcal Q)\) are different questions, and an answer to one is not an answer to the other") and D3:L159 ("it does not answer a broader question that failed, and a narrowing adopted after a failure is a new claim at a new index"): the last sentence.
    - D3:L363 (Historical index): "the failure on \(p\) stands".
    - Receipts, D3:L391: a receipt against each such candidate is a derivation over the same leaf, so it needs no record of the candidate.
  - **The place.** Part VIII, directly after "Historical index", whose last sentence it continues, and which W59.1 points to ("an answer it refutes stays refuted on \(p\) (Part VIII)"). It is not a Part XVI derivation, because its proof is (A) read once. Part XV's list of results open to a counterexample is left unchanged: a counterexample to this one would be a counterexample to (A).
- **CASES AT RISK:**
  - **O1 (Bruno): toward on the first half, and the second half stays SILENT.** Each restated rule narrows the contract, so it is a different question that does not answer when the stream floods. The flood question's failures stand, so Bruno has no account of the floods ("Bruno has no explanation of the floods"). Nothing here reads the series, so "the series as a whole is a retreat" is not reached.
  - **D3-T (O76): holds, and moves toward on its reason.** The discarded design's answer at the tried setting (A on, B off) is not the target's, so the design fails there. Any design with that answer fails there too, which is why it "says nothing about controllers that pass".
  - **O27 (the test that fitted neither): holds.** The robot's move puts the instrument in question. The (K3) clause says the exclusion of both diagnoses then reopens alike, which fits the case, and the re-run with the second sensor establishes a new result. The attribution verdict is not reached.
  - **O8 (Petra's own ovens) and N7 (two bakers): hold; N7 is watched.** A scope stated from the start involves no failed answer. N7 is read with Maya's limits "found … by experience". If a reader takes them as narrowings after failures, each narrower claim is a different question. That is D3:L159's point, and "Maya explains" is a verdict on her stated question. The error-correction analysis flagged this reading (option (b), cases).
  - **N2 (the myth amended): holds.** The original myth's answer at the southern pairs stays failed on any question that contains them. The amended myth changes the answer there, so this entry does not bear on it, and its "No" rests on (E).
  - **Untouched: O24, O36, O45, O46, O47, O48, N1, N3, N4, N5, N24 and N25.** None has a failed answer at a pair of a contract. In O46 the deletion is an organization edit, not a failure at a pair (error-correction analysis, option (b), cases).
- **GAIN:** The theory says in one paragraph why a correction sticks on its question with no record of rescues. It says what "established" requires, and why blaming the test exempts no candidate.
- **LOSS:** About 220 words. It does not reach pairs beyond the failed one, runs of saves, or grain changes: the limits the correction-sticks analysis found (§1(1); §4, losses).

**W38.1: the lines of NEW that change.** Every other line of NEW is byte for byte as in draft 3's list. The full entry follows.

Old lines (removed):

````text
- *Idle parts.* Deutsch counts superfluous features as a defect of an explanation (chapter 1, p.25). Here (E) has no condition that each commitment do work: a commitment that does no work by itself is critical in no support, and how hard an account is to vary grades nothing (Part VI).
- *Reach.* Deutsch's reach is the power of an explanation to solve problems beyond those it was made for (chapter 1, p.28). Here the reach of an account is the set of jobs on which it is an account, fixed by the account and the world (Part VI).
- *Surprise and problems.* For Deutsch a problem is a situation in which conflicting ideas are experienced, and a problem can arise without any observation (chapter 1, p.17). Here surprise is kept for selected transports (Part IV). A problem in his sense is a recognized difficulty (Part X): a failure of a claimed obligation, or a conflict in which meeting a claimed obligation fails a protected one (Part XI), when the system represents it.
````

New lines (in their place, in this order):

````text
- *Idle parts.* Deutsch counts superfluous features as a defect of an explanation (chapter 1, p.25). Here (E) has no condition that each commitment do work: a commitment that does no work by itself is critical in no support, and nothing in the semantics grades a candidate for carrying one (Parts 0 and VI).
- *Hard to vary.* Deutsch calls an explanation good or bad as it is hard or easy to vary while still accounting for what it purports to account for (chapter 1, p.31), and a myth easy to vary because its details could be changed without changing its predictions (pp.20–22). Here hard-to-vary is stated through rivals and problems, with no measure or count of variants (Part VI). Two rivals that both fit what is established pose a problem, a conflict between ideas in his sense (p.17); a pair of the question's contract at which they conflict is a test that solves it, as an experiment decides between two viable theories whose predictions conflict (p.16); and a candidate is easy to vary when it has a rival that fits as well and conflicts with it nowhere the question covers, as his variant of the myth in which Demeter sends the warmth south agrees with the myth on every season the Greeks knew (p.21). Three departures remain. He judges ease of variation before any variant is offered, and would reject a bad explanation without any experiment (p.25); here it is shown only by offering the rival, which is the criticism. He holds that an explanation able to fit anything in its field explains nothing (p.22); here a candidate with such a rival is an account of its question when it meets (E), and the remedy is a finer question. And variants whose differing details do no work, which he finds reduce to one core explanation (p.21), are here one account written two ways, not rivals (Derivation 2).
- *Reach.* Deutsch's reach is the power of an explanation to solve problems beyond those it was made for (chapter 1, p.28). Here the word is not defined, and nothing is measured by how many questions a candidate answers; whether a candidate is an account of a question is fixed by the candidate and the world, whether or not anyone has asked the question (Parts I and VI).
- *Surprise and problems.* For Deutsch a problem is a situation in which conflicting ideas are experienced, and a problem can arise without any observation (chapter 1, p.17). Here surprise is kept for selected transports (Part IV). A problem for a question is narrower: two rivals that both fit what is established (Part VI). A problem in his wider sense can be a recognized difficulty (Part X): a failure of a claimed obligation, or a conflict in which meeting a claimed obligation fails a protected one (Part XI), when the system represents it.
````

### W38.1 — The note of sources and departures

- **STATUS:** applied
- **GROUP:** M; edited 25 September (group H)
- **ITEM:** W38
- **FILE-11 LINE:** 7–9
- **WHERE:** front matter, after the note. It is inserted before the rule `---` at L7 that opens Part 0. The anchor is L7–L9 (the rule, the blank line and the Part 0 heading), kept byte for byte. L7–L9 belong to no group.
- **REASON WORD:** meta
- **KIND:** META
- **CHECK:** check 2, FIX. Five statements were inaccurate: what file 00 cites, Marletto's page for interoperability, Deutsch's definition of a problem, the Derivation 6 clause, and the stated-limits line against B1's wording. Three lines follow C's fixes (physical media, a separate matter, does no work by itself). The fallback table's substrate row now cites chapter 3, pp.88 and 95. The assembler also gave the fallback for "Surprise and problems" the corrected account of Deutsch's "problem", which check 2's fix (c) implies but did not write out.
  - **25 September:** four lines of NEW changed for W59.1 and the edits to W34.1 and W33.1, and the fallback table with them. *Idle parts* no longer says that how hard an account is to vary grades nothing, since Pres goes; it says that nothing grades a candidate for carrying a commitment that does no work. A line *Hard to vary* is added after it. *Reach* no longer gives a definition by jobs. *Surprise and problems* now names the problem for a question of Part VI and says that a problem in the wider sense "can be" a recognized difficulty, where it said "is", to agree with Part VI's "can be". Every other line is byte for byte as before. Checked by the drafter only; no outside reader has seen these lines.
- **OLD:**
````text
---

# Part 0 — Read this first
````
- **NEW:**
````text
<!-- META:SOURCES BEGIN -->
*Sources and departures.*

**Sources.** The semantics has two sources, named as such by its owner: Chiara Marletto, *The Science of Can and Can't* (2021), and David Deutsch, *The Beginning of Infinity* (2011). Its predecessor is the FW5 construction of 8 September 2026 (file 00), whose reference list cites articles by the two authors, not these books. The task wording of the physical module (Part XII) is constructor theory's, from Deutsch's paper "Constructor Theory", *Synthese* 190 (2013), which file 00 cites. The definitions, conditions and derivations are this document's own. None is attributed to either book, and this note says nothing about what follows from them.

**Close parallels, named and not claimed as derived.** Derivation 9's last sentence, declared provenance, "relay is not" construction (Part X) and reason use (Part IX) have close parallels in Deutsch, chapter 7, pp.155–161, and chapter 16, p.406. Inexplicit representation (Part X) has one in Deutsch, chapter 16, pp.405 and 412. Part I's substrate independence, held so far as the adopted physics lets contents pass between physical media, matches the interoperability principle as Marletto states it (chapter 3, pp.87–88; its consequence for universal computers, p.95).

**Departures.** The semantics departs from the books on purpose at these places.
- *Explanation.* Deutsch counts a false myth as an explanation (chapter 1, p.19). Here that is an explanatory candidate (Part V). Part I's fallibility commitment uses "explanation" for an account on a contract, and how hard an account is to vary is a separate matter (Part VI).
- *Idle parts.* Deutsch counts superfluous features as a defect of an explanation (chapter 1, p.25). Here (E) has no condition that each commitment do work: a commitment that does no work by itself is critical in no support, and nothing in the semantics grades a candidate for carrying one (Parts 0 and VI).
- *Hard to vary.* Deutsch calls an explanation good or bad as it is hard or easy to vary while still accounting for what it purports to account for (chapter 1, p.31), and a myth easy to vary because its details could be changed without changing its predictions (pp.20–22). Here hard-to-vary is stated through rivals and problems, with no measure or count of variants (Part VI). Two rivals that both fit what is established pose a problem, a conflict between ideas in his sense (p.17); a pair of the question's contract at which they conflict is a test that solves it, as an experiment decides between two viable theories whose predictions conflict (p.16); and a candidate is easy to vary when it has a rival that fits as well and conflicts with it nowhere the question covers, as his variant of the myth in which Demeter sends the warmth south agrees with the myth on every season the Greeks knew (p.21). Three departures remain. He judges ease of variation before any variant is offered, and would reject a bad explanation without any experiment (p.25); here it is shown only by offering the rival, which is the criticism. He holds that an explanation able to fit anything in its field explains nothing (p.22); here a candidate with such a rival is an account of its question when it meets (E), and the remedy is a finer question. And variants whose differing details do no work, which he finds reduce to one core explanation (p.21), are here one account written two ways, not rivals (Derivation 2).
- *Reach.* Deutsch's reach is the power of an explanation to solve problems beyond those it was made for (chapter 1, p.28). Here the word is not defined, and nothing is measured by how many questions a candidate answers; whether a candidate is an account of a question is fixed by the candidate and the world, whether or not anyone has asked the question (Parts I and VI).
- *Stated limits.* Both books hold that a limit of scope needs an explanation (Deutsch, chapter 1, pp.27–28; Marletto, chapter 1, p.24). Here a stated limit is recorded and not certified: meeting the conditions of an account on a restricted contract certifies nothing about the restriction, and a verdict on a restriction whose ground the claim states is given with that ground (Part III).
- *Selection.* Deutsch calls criticism and experiment a selection (chapter 4, p.78). Here selection is blind: its history holds no represented target (Parts 0 and IV).
- *Surprise and problems.* For Deutsch a problem is a situation in which conflicting ideas are experienced, and a problem can arise without any observation (chapter 1, p.17). Here surprise is kept for selected transports (Part IV). A problem for a question is narrower: two rivals that both fit what is established (Part VI). A problem in his wider sense can be a recognized difficulty (Part X): a failure of a claimed obligation, or a conflict in which meeting a claimed obligation fails a protected one (Part XI), when the system represents it.
- *Elimination.* Deutsch asks an eliminative explanation to explain why what it denies seems to exist (chapter 7, p.154). Here why the absent structure appears is a separate question with its own contract, which an account of the absence neither answers nor needs to (Part VII).
- *Acquisition.* Deutsch holds that grasping any idea takes conjecture (chapter 4, p.94; chapter 16, pp.403–406). Here not every acquisition is construction: reconstruction by a learner is, and relay is not (Part X).
- *Knowledge as self-preserving information.* Marletto defines knowledge as information that can keep itself instantiated in physical systems (chapter 5, p.155). The semantics leaves this out: its class is explanatory creativity, and knowledge in that sense would be an attribution of the physical module, outside the class.
- *Universality and aesthetics.* Deutsch holds that people are universal explainers (chapter 6, p.146) and that there are objective truths in aesthetics (chapter 14, p.368). The semantics abstains on both. It defines the universal class and shows no one to belong to it (Parts 0 and XIII), and it takes worth as an input and derives no aesthetics (Part XI).

Page numbers are the printed pages of the editions named. A third book, named by the owner as further reading, is not a source and is not cited.
<!-- META:SOURCES END -->

---

# Part 0 — Read this first
````
- **DECLARATION:** made by the note ("the note of sources and departures after it … not part of the theory and add nothing to it"). Not counted in N or M.
- **REASON:**
  - Worklist W38 (verify obs 1, 3 and 10; decision S19); plan 1.3.6.
  - The content is plan 1.3.6's: the sources; the constructor-theory lineage of Part XII (00:910 and 00:1416, [R2]); the FW5 predecessor; the close parallels (Deutsch, chapters 7 and 16); and the eight departures it lists.
  - Added, because other groups' entries send them here:
    - reach (C's C12 on W34.1);
    - elimination (C's C12 on W40.1);
    - the mapping of "problem" to the recognized difficulty (C's W35.3 reason);
    - interoperability, a term kept out of the theory (C's W45.1 reason);
    - blind selection (A's W37.1 reason).
  - Also added: inexplicit representation as a parallel (D pp.405, 412), since C's W41.1 restores it from file 00.
  - No book is quoted, so plan 1.3.6's 25-word limit is met trivially.
  - **Page numbers.** Each was checked against the extracted text of the named editions, by locating a phrase from the page with `sources/locate.py`: Deutsch pp.17, 19, 25, 27–28, 28, 78, 94, 146, 154, 155, 156, 160–161, 368, 405, 406 and 412, and Marletto pp.24, 95 and 155, each in the chapter named. Deutsch pp.403–406 was read (the passage on how memes are acquired, which runs across those pages). Plan 1.3.6 asks the writer to recheck at freeze.
  - **25 September: hard to vary.** The owner's position of 24–25 September states hard-to-vary through rivals and problems (W59.1), and this note says so. Deutsch p.17 on problems as conflicts, p.16 on experiment between two viable theories, pp.20–22 on ease of variation (p.21, the southern variant and the one core of the Persephone and Freyr myths; p.22, an explanation that could explain anything), p.25 on rejection without experiment, and p.31 (glossary, good and bad explanation). Each page was checked with `sources/locate.py` on a phrase from the page. No book is quoted: the lines paraphrase. The departures recorded are the three that remain after the change: judgement before a rival is offered, the name of explanation kept for an account with an easy rival, and label-only variants read as one account. The *Surprise and problems* line changes "is" to "can be" for the wider sense, since Part VI now says a represented problem for a question "can be" a recognized difficulty, and "is" would contradict it.
  - **Named and not named.** The decision number (S19) is not named, because no meta block names a record file. The third book is mentioned and not named or cited, since plan 1.3.6 says it is not cited.
  - Each line that rests on another group's entry has a fallback, given below, for use if that entry is dropped under plan 1.5's cap.
- **CASES AT RISK:** none. The block is cut from every brief (D6), and "Deutsch" and "Marletto" are on the build's withheld list (plan 2.5). If it reached a tester, the departures would steer readings toward the books' judgements at exactly the guard rows: idle parts (N1, N25), hard to vary (N2, N3, N5, N25, O24), stated limits (O1, O5, O8, N7), selection (O11, N11), surprise (O3, N18, N19) and elimination (N22).
- **GAIN:** Lineage, and honesty about where the semantics departs from its two sources.
- **LOSS:** Readers may hold the theory to the books (worklist W38). The authority file grows by about 720 words.
- **FALLBACKS:** if an entry a line of the sources note rests on is dropped under plan 1.5's cap, the line is replaced by the fallback, or dropped where none is given.

  | line | rests on | fallback |
  |---|---|---|
  | Inexplicit representation (parallels) | C W41.1 | drop the sentence |
  | Part I's substrate independence (parallels) | C W45.1 | Part I's substrate independence is stated without condition; Marletto treats the interoperability of carriers as a law of physics that may fail (chapter 3, pp.88 and 95). |
  | Explanation | C W36.1 | - *Explanation.* Deutsch counts a false myth as an explanation (chapter 1, p.19). Here that is an explanatory candidate (Part V), and Part I's fallibility commitment uses "explanation" for what is not in error in the dependence alleged to do the work. |
  | Idle parts | C W33.1 (the words 'does no work by itself'); H W59.1 ('Nothing here … grades'); the claim itself holds on file 11 | - *Idle parts.* Deutsch counts superfluous features as a defect of an explanation (chapter 1, p.25). Here a commitment that does no work does not stop a candidate from being an account; Part VI reports it. |
  | Hard to vary | H W59.1 | - *Hard to vary.* Deutsch calls an explanation good or bad as it is hard or easy to vary while still accounting for what it purports to account for (chapter 1, p.31). Here no measure of variation is stated and nothing is graded (Parts 0 and XIV). |
  | Reach | H W59.1 (the sentence on questions nobody has asked) | - *Reach.* Deutsch's reach is the power of an explanation to solve problems beyond those it was made for (chapter 1, p.28). Here the word is not used, and whether a transport is faithful on a contract does not depend on anyone's accepting it (Part I). |
  | Reach, if W34.1 as edited is dropped | C W34.1 | - *Reach.* Deutsch's reach is the power of an explanation to solve problems beyond those it was made for (chapter 1, p.28). Here the word is used once, for the jobs an account is held to (Part VI), and is not defined. |
  | Stated limits | B1 W57.1 + W32(b).1 | - *Stated limits.* Both books hold that a limit of scope needs an explanation (Deutsch, chapter 1, pp.27–28; Marletto, chapter 1, p.24). Here a stated limit is recorded, and what makes it appropriate is a criticizable part of the claim that the semantics does not certify (Part III). |
  | Selection | A W37.1 for 'Parts 0 and'; the claim holds on file 11's Part IV | (replace "(Parts 0 and IV)" with "(Part IV)") |
  | Surprise and problems, if W59.1 is dropped | H W59.1 | - *Surprise and problems.* For Deutsch a problem is a situation in which conflicting ideas are experienced, and a problem can arise without any observation (chapter 1, p.17). Here surprise is kept for selected transports (Part IV). A problem in his sense is a recognized difficulty (Part X): a failure of a claimed obligation, or a conflict in which meeting a claimed obligation fails a protected one (Part XI), when the system represents it. |
  | Surprise and problems | C W35.1-W35.3 | - *Surprise and problems.* For Deutsch a problem is a situation in which conflicting ideas are experienced, and a problem can arise without any observation (chapter 1, p.17). Here surprise is kept for selected transports (Part IV), and the recognized difficulty of a critical episode (Part X) is not defined. |
  | Elimination | C W40.1 | drop the sentence |

## 6. Verification

**How the entries were checked.** The five blocks above were spliced into a scratch copy of the change list by `rivals/splice.py`. W59.1 went after W33.1, W60.1 after W31.1, and W34.1, W33.1 and W38.1 replaced their old blocks. The repository copy was not touched. The program was then run on the scratch copy:

```text
python3 Semantics/tools/s89_apply_changes.py <scratch>/new_full.md --change-list <scratch>/cl_spliced.md \
    --theory-output <scratch>/new_theory.md --date "draft of 25 September 2026, not frozen" --self-test
```

**Its output, verbatim:**

```text
file 11: md5 5e494c1095d920d128b9a79de378f923 (as required)
entries parsed: 65 (applied 60, of which theory 57 and meta 3; record-only 5; held 0)
theory entries by expected ruling: CLAIM 51, ORDER 2, WORDING 4
every OLD, locator and anchor occurs once in file 11; no applied OLDs overlap; no held anchor is touched
note: N = 51 of M = 57 changes; layer 2: K = 42 places
result is file 11 with exactly the listed replacements (walk check); 55 diff hunks, each inside an entry
cut of the three meta blocks gives back the theory text; no withheld word in it; no slot left
self-test: an unlisted edit was refused
self-test: an edit inside a new text was refused
self-test: the clean draft passed
written: <scratch>/new_full.md
md5: 0dea7cbd2adef3938f6750b80d587caf
words: 28459 (theory text alone: 12231)
lines: 1840
```

**The baseline.** Run first on the unchanged change list, the program gave back draft 3's theory text exactly: md5 403c4f2fb3e5d57bb48a5647011c9f91, the same as the committed file. The full draft 3, with the date text of 24 September, has md5 e33624e73da8c31e33a8e8df222931af.

**The new theory text against draft 3.** The theory text written with the new entries has md5 3009cc90be8dbd51aad79ce9d9e2be91 and 12,203 words by `wc -w`. `diff` against draft 3's theory text shows exactly two hunks:
- draft 3's L313 is replaced by the three paragraphs "Commitments that do no work", "Rivals" and "Problems";
- one paragraph, "A failed answer stays failed", is added after draft 3's L363.

Nothing else differs.

**Other checks.**
- **Uniqueness.** Every OLD above occurs once in file 11 (md5 5e494c1095d920d128b9a79de378f923), checked by script and again by the program.
- **Greps of the new theory text.** "operatorname{Pres}": 0 hits. "job": 0. "Hard-to-vary": 0. "grades nothing": 0. "reach": verbs only. \(\mathcal V\): only at (D).
- **Quotations.** Every quotation these entries attribute to the two analyses, file 00, draft 3, the case books or D3-T was checked by script against its source. All occur verbatim.
- **Deutsch's pages.** Each page the sources note cites was checked with `sources/locate.py` on a phrase from the page: pp.16, 17, 20, 21, 22, 25 and 31. The new lines paraphrase and quote nothing.

## 7. What else must change in the change list and the note

These are not entries. The frame of the change list is the orchestrator's to update.

- **Counts.**
  - Entries that change the theory text: 57. Expected CLAIM 51, WORDING 4, ORDER 2.
  - By group: A 14 of 18, B1 14 of 15, B2 11 of 11, C 10 of 11 (W34.1 and W33.1 stay in C, edited), H 2 of 2.
  - The note will read "51 of the 57 changes". Meta 3, record-only 5, held 0, and layer 2 K = 42 are unchanged.
- **R2 numbers.**
  - Unchanged: R2-01 to R2-24. W34.1 is still R2-23 and W33.1 still R2-24.
  - New: W59.1 becomes R2-25, and W60.1 becomes R2-29.
  - Shifted by one: W40.1 25→26, W24.1 26→27, W31.1 27→28.
  - Shifted by two: every entry from W22.1 (28→30) to W19.3 + W10(b).1 (55→57).
  - The revision note's section 5 map, which gives each entry's S90 id beside its R2 number, must be regenerated.
- **The build line** in "What the checks changed" would read:
  - 65 entries parsed; 60 applied (57 theory, 3 meta); 5 record-only; none held.
  - CLAIM 51, WORDING 4, ORDER 2. N = 51 of M = 57, K = 42. 55 diff hunks.
  - Theory text md5 3009cc90be8dbd51aad79ce9d9e2be91.
- **"W34.1" in the frame.** "Findings carried forward" and P2(d) name W34.1 as a watch for N1 and N4 under "reach". After the edit, W34.1 carries no reach, and the N4 watch moves to W59.1's sentence on questions nobody has asked.
- **The revision note** (`tests/Revision 2 - revision note, draft of 23 September.md`) is regenerated by the program. The new or changed declaration lines are those of W34.1, W33.1, W59.1 and W60.1 above.
- **Outside reading.** No outside reader has seen W59.1, W60.1, or the edited W34.1, W33.1 and W38.1. They are the least tested texts in the list.

## 8. Findings carried forward (not entries)

- **The dependence order does not place the new terms.** Rivals, conflict, established, fits and problem for \(p\) are defined from (E), Derivation 2's relation, histories ("offered", "conjectured") and receipts. No new primitive or declared input is used, so Derivation 6's claim still holds. The order at D3:L520 does not list them, as it already omits Result, ProducesVia, Cap and Enable (finding 9).
  - A clause is available if wanted. The file-11 sentence "(S), (B), (D) depend on (E)." is still untouched by any entry (W7.5 left it free), so an entry could make it read: "(S), (B), (D) depend on (E); rivals and the problems they pose (Part VI) on (E), Derivation 2, histories and receipts."
- **W35.3's REASON is now dated.** It says "The word 'problem' is not defined in the theory". It is still true of the bare word, but "problem for \(p\)" is now defined. Its text and declaration are unaffected.
- **W38.1's *Surprise and problems* line now says "can be" where it said "is".** This matches W59.1: a problem in Deutsch's wider sense, when represented, can be a recognized difficulty. A fresh checker should confirm that this does not undo check 2's fix (c).
- **The "easy to vary" definition is symmetric.**
  - Two kind-(ii) rivals are each easy to vary relative to the other, and this includes a fuller and a leaner account if someone offers them in place of each other (N7, watched).
  - "In place of the other" keeps compatible accounts that nobody pits against each other out of it.
  - If the owner wants the term to point at one side only, a further condition would be needed. Any such condition risks becoming a grade.
- **A failure blamed on the background or the instruments.** W60.1's (K3) clause answers the save of blaming the test (error-correction analysis, section 2): the exclusion reopens for every candidate alike. It says nothing of runs of saves (O1's second half), or of a change of grain (F00:L1380), which remain open.
- **The declared restriction operation of Part VI** (D3:L287) is still not among the declared inputs. This is unchanged by these entries and was already carried forward.
