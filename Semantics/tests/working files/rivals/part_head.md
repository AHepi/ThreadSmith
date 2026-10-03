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

After the change, the theory text has no Pres, no "job" and no "Hard-to-vary". "Reach" survives only as a verb (D3:L403, L562, L630 in the new numbering) or in "reachability". \(\mathcal V\) survives only in (D) (and \(\mathcal V_A\), the aesthetic value set, which is unrelated).

## 4. The two gaps found earlier

- **"The variation family is not a declared input": it dissolves in substance.**
  - After the change, \(\mathcal V\) occurs only as the domain of (D).
  - There, whether \((v,w)\in\operatorname{Boundary}_{E,p}\) is fixed by \(v\) and \(w\) alone, since it holds exactly when \(\operatorname{Account}(E_v,p)\neq\operatorname{Account}(E_w,p)\). No claim about a candidate or a pair of edits turns on which family is declared.
  - No case, definition or derivation uses (D); the dependence order only places it.
  - The earlier worry was that a grade or a count over \(\mathcal V\) could be chosen "from the verdict wanted" (D3:L516). With Pres gone, nothing grades or counts over \(\mathcal V\).
  - If the orchestrator wants the letter covered too, a later revision can add "the family \(\mathcal V\) of (D)" to Part XIV's declared inputs. No entry is drafted for it.
- **"Job is undefined": closed.** After the change "job" occurs nowhere in the theory text (grep, 0 hits). Its two uses, the lemma and W34.1's reach definition, both go. Nothing defines it, and nothing needs it.
