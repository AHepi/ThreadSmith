# S93 ruling: X11, proposed (Part VII, "Production and direction", draft 4 L325)

*Written by a fresh Claude checker on 25 September 2026, under rules 4, 5, 9, 11 and 12 of `results/S93 How the cross-examination of draft 4 will be read - written before sending.md`. The checker did not draft, assemble or check the change list and did not write the briefs. It read the reading rule; in the tabulation only section 2.2's entry for X11, section 3.7 and X11's entry in section 7; the two replies section 7 names (`s93_xexam_atria_I.response.txt`, `s93_xexam_mimo_I.response.txt`, response files only); brief part I (md5 2be35c1ec040d791e348acacaae6a79c); the draft-4 theory text (md5 fc55b470c63cd4b3c27d6aa64d8d8c17); the change list (md5 b6b2ea95ea9e21ebea3316d8e9fa4b40); and file 11 (md5 5e494c1095d920d128b9a79de378f923). For the kind and the cases it also consulted plan 1.1 of `tests/Revision 2 - plan and test round, draft of 23 September.md`, the definitions of S81 determination file 03, the S81 case readings of O4 and O6, and case N23 of the S89 book. It read no other ruling, no other item's part of the tabulation, and no other S93 reply. It wrote only this file and committed nothing.*

## The proposed entry

As the reading rule states it ("What is cross-examined", third bullet) and brief part I §4 prints it:

- **Place.** Part VII, "Production and direction": draft 4 L325, file 11 L323. OLD is one sentence of that line.
- **KIND:** WORDING. **REASON WORD:** erratum. **DECLARATION:** none.
- **CHECK:** none yet. The entry is proposed and has not been entered in the change list or applied to the theory text. Log S92 recorded the slip.
- **Situations named:** O6, O4.
- **OLD:**
````text
The reversed calculation \(H=L\tan\theta\) is not: intervening on \(H\) changes the target's \(L\) but not the calculation's \(H\).
````
- **NEW:**
````text
The reversed calculation \(H=L\tan\theta\) is not: intervening on \(H\) changes the target's \(L\) but not the calculation's \(L\).
````

**Checked here.** The proposal can be entered.
- OLD occurs exactly once in file 11 (L323) and exactly once in draft 4 (L325).
- It also stands in file 10 (L338), so it is not a difference between file 10 and file 11, and no layer-2 row is affected.
- No entry in the change list touches file-11 L323. In file-11 order, the entry belongs between W59.1 (FILE-11 LINE 317–319) and W40.1 (FILE-11 LINE 337).

## Atria's argument

Atria's reply for part I makes three points on X11, and its closing line is `X11: UPHELD — the symbol must be *L*: …`.

- **Point 6 (T1).** Atria tried to argue that the old symbol was right, because the calculation's computed \(H\) stays at \(L\tan\theta\). It reports that this attack fails. An edit that sets a port replaces the component that assigns the port. So under the reversed calculation, the intervention on \(H\) sets the calculation's \(H\), and the calculation's \(L\) does not follow while the target's \(L\) moves. (F2) therefore fails in \(L\). The new symbol is the one L271 requires, and the old one contradicted L271.
- **Point 7 (T2, T3, T4).** WORDING is the right kind. The claim that governs the sentence, that the reversed calculation is not faithful under this contract, is unchanged. Only the description of how it fails is corrected: "the erratum removes a false sub-claim rather than adding one". With the change, L325 agrees with L271. O6 and O4 do not move. The one-symbol change is the right repair.
- **(a).** "No bearing on rivals, variation, criticism or error correction; the rule is not engaged."

**Quotation check (rule 9).**
- "An edit that sets a port replaces the component assigning that port" is FOUND at L103.
- "intervening on the upstream port changes the target's downstream value but not the calculation's" is FOUND at L271.
- "not the calculation's *H*" is FOUND at L325.
- "the reversed calculation *H* = *L* tan θ is not [faithful] under this contract" is FOUND only in pieces, with an inserted word. L325 reads "The forward organization is faithful under this contract. The reversed calculation \(H=L\tan\theta\) is not: …". The bracket fills the ellipsis correctly.
- Atria's solution sets, which leave the calculation's \(L\) "arbitrary", are its own formalization. Whether the calculation's \(L\) is unconstrained or held at a boundary value, it does not follow \(h\cot\theta_0\), so the conclusion does not depend on that choice.

**Assessment.**
- **Points 6 and 7 on T1, T3 and T4 hold** on the texts (Rulings, 1 and 3).
- **Point 7 on T2 does not hold.** It narrows the test to "what the theory says a candidate must satisfy", and it answers only the first half of the CLAIM test: whether anything new can be concluded. Its own words, "removes a false sub-claim", concede the second half: a reader can no longer conclude something the current text stated (Rulings, 2).

## Mimo's argument

Mimo's reply for part I makes three points on X11, and its closing line is `X11: CHALLENGED — the wordings name different ports, so WORDING is the wrong kind; should be CLAIM.`

- **Point 1 (T2).** WORDING requires that the new wording say what the old said. The two wordings name different ports and so make different claims. A reader of the current text can conclude that the calculation's \(H\) is unchanged by the intervention on \(H\), and the new wording withdraws that conclusion. Mimo proposes KIND CLAIM with this declaration: "The revision corrects the port named in the last clause of the reversed-calculation sentence. The current text's sentence named \(H\) as the port unchanged by the intervention on \(H\); the revision names \(L\). The claim now stated in Part VII is the same one line 271 states of the same reversed calculation: intervening on the upstream port changes the target's downstream value but not the calculation's."
- **Point 2 (T1, T3, T4).** The change of symbol is correct. The translated edit sets \(H\) in \(E\) and leaves the calculation's \(L\) untouched, while the target's \(L\) changes, so the mismatch that breaks (F2) is in \(L\). L325 and L271 now agree, no verdict moves, and naming \(L\) is the minimal repair.
- **Point 7 ((a)).** "X11 raises no new (a) issue: the reversed calculation remains a rival assessed the same way; only the symbol naming the mismatch is corrected."

**Quotation check (rule 9).**
- "the new wording says what the old wording said, in other words" is FOUND in brief I §1, line 10 (the definition of WORDING).
- "fails (F2) under the production contract: intervening on the upstream port changes the target's downstream value but not the calculation's" is FOUND at L271.
- "the calculation's \(H\) is unchanged by the intervention on \(H\)" is NOT FOUND as a quotation. It is Mimo's own statement of what a reader can conclude. L325 reads "… changes the target's \(L\) but not the calculation's \(H\)", which says the same, so the point is ruled on the text.

**Assessment.**
- **Point 1's argument on the kind holds** (Rulings, 2).
- **Mimo's declaration is true, but it cannot be entered as written.** It cites a line number and speaks of "the current text" and "the revision". It describes the act of correcting rather than saying what Part VII now says. No declaration in the change list does any of these, because declarations go into file 13's note and say what the theory claims. A third wording is given below (Rulings, 4).
- **Point 2 holds.**

## Rulings

**1. The change of symbol is right (T1). Both readers agree, and the texts confirm it.**
- By Part II, \(H\) and \(\theta\) are inputs and \(L\) an output under the production contract (L109, applied at L325).
- In the reversed calculation, \(H\) is the port its one component assigns. An edit that sets \(H\) "replaces the component assigning that port" (L103). So the intervention sets the calculation's \(H\), and the calculation's \(H\) changes with it.
- The calculation's \(L\) was tied to \(H\) only through the component that has been replaced, so the edit does not reach it. The target's \(L = H\cot\theta\) moves. Read under (F2) (L242), the mismatch is in \(L\).
- **OLD is therefore false in the theory's own terms.** It could be true only if the translated edit left the component that assigns the calculation's \(H\) in place, and L103 excludes that for an edit that sets a port. OLD also does not state what L271 states of every reversed calculation. NEW states it: the upstream port is \(H\), the downstream value is \(L\).
- **The repair is minimal and right.** No better repair was proposed or found.

**2. The kind is CLAIM, not WORDING. Mimo's challenge is upheld.**
- **By the definitions.** The brief defines WORDING (§1) as "the new wording says what the old wording said, in other words". S81 file 03, whose definitions the change list's KIND field applies, requires for WORDING that "every conclusion drawn from one can be drawn from the other". Under OLD, the intervention leaves the calculation's \(H\) unchanged; that is false under L103. Under NEW, it leaves the calculation's \(L\) unchanged; that is true. Two sentences with different truth values in the theory's own terms do not say the same thing in other words.
- **It is not ORDER either.** L271 already states NEW's positive content, at wider scope. But the entry also removes OLD's assertion, and nothing stated elsewhere does that work.
- **By the CLAIM test.** From OLD a reader can conclude, on the sentence's own words, that intervening on \(H\) leaves the calculation's \(H\) unchanged. From NEW that can no longer be concluded, which is the second half of the CLAIM test (brief §1). A careful reader who sets L325 against L103 finds an open, contradictory reading at this place. Plan 1.1 rules that a change which closes an open reading is CLAIM. Either way the kind is CLAIM.
- **By the change list's own precedents.** Where an erratum corrects or drops a sentence that says something false which the rest of the text contradicts, the list rules CLAIM and declares it:
  - W6.1: L27 s2 was contradicted by the body. "LOSS: … That reading is withdrawn."
  - W7.1: "Everything else is derived" was contradicted by L514.
  - W10a.1: Derivation 10's gloss misdescribed Derivation 3. Its REASON notes that "Derivation 10's conclusions do not rest on the clause", and it is still CLAIM.
- **The WORDING errata are different.** Each removed or added nothing asserted in the theory's terms:
  - W9.1 dropped a parenthesis with no referent in the document. 03 ruled that "The rule in the sentence stands without the parenthesis".
  - W24.1 adds typing that binds free notation and restricts nothing.
  - X11 removes an asserted and false statement about a named port, so it belongs with W6.1, W7.1 and W10a.1.
- **Unchanged claims do not make a change WORDING.** Atria is right that the verdict the sentence carries, that the reversed calculation is not faithful under this contract, is unchanged. But the kind is decided by what can be concluded, not by whether a verdict moves: W7.1 and W7.6 are CLAIM with no case at risk.
- **The REASON WORD stays erratum.** Plan 1.1 defines an erratum as a change that "corrects or restores a pointer, a label, a symbol or a hypothesis". This change corrects a symbol, and W6.1, W7.1 and W10a.1 pair erratum with CLAIM.

**3. No fixed verdict moves, in either direction (T4).**
- **O6 and O4 (the named situations).** Both S81 readings rest these cases on the passages about signatures and identification, and on the restated-answer rule: file 11 L129, L153 and L275, which are draft 4 L127, L151 and L273. Neither reading cites file 11 L323 or file 10 L338. The sentence's verdict, "is not" faithful under the production contract, stands under both wordings: if the calculation's \(H\) really stayed put, (F2) would still fail. So neither O6 nor O4 could have rested on the wrong symbol.
- **N23 (the planets; direction), a case of my own choosing.** No S93 brief carries it. It is the one case with the pole's structure, a reversed calculation offered as production. W20.2's CASES AT RISK reads it through L323: the backward account "fails (F2), as L323's reversed calculation does". It cites the failure, not the port, and both wordings give the failure. Under NEW, the backward account fails exactly as L271 says. N23's verdict holds.
- **No pole or shadow case exists.** The S81 book and the S89 book were searched for "shadow", "pole", "height", "direction" and "reversed". Only N23 concerns direction.
- **The rest of the paragraph and the text that reads it are untouched.** The sentences "It is faithful under the identification contract …" and "Direction is derived from the admitted edits; the nouns "pole" and "shadow" fix nothing" are unchanged, and so are L271 and Part XV's L536, which rests on Part V. No line of draft 4 other than L271 and L325 speaks of "the calculation's" port.

**4. Between the two declarations.** Atria gives none, since it holds the entry to be WORDING. Mimo's is true of NEW but is not in the change list's form (point 1 above). The change list's form is "Part … no longer says that …; it now says …" (W6.1, W11.1, W13.1, W34.1), with no line numbers. The declaration below claims no more than NEW says:
- NEW does not say that the calculation's \(H\) changes, although L103 entails it, and the declaration does not say so either.
- It names Part V as the place that already says the new clause, as W13.1 ("which matches Part XII") and W17.2 ("as Part IV does") name theirs.

**5. The entry as fixed.** OLD and NEW are entered exactly as proposed, byte for byte. Its fields:
- **STATUS:** applied.
- **FILE-11 LINE:** 323.
- **WHERE:** Part VII, "Production and direction" (L323), sentence 5.
- **REASON WORD:** erratum.
- **KIND:** CLAIM.
- **DECLARATION:**

  ````text
  Part VII no longer says that intervening on \(H\) leaves the reversed calculation's \(H\) unchanged; it now says that the intervention leaves the calculation's \(L\) unchanged while the target's \(L\) changes, as Part V says of a reversed calculation.
  ````
- **CASES AT RISK:** none moves. O6 and O4 rest on draft 4 L127, L151 and L273, and N23 on the failure of (F2), which both wordings state.
- **CHECK line** (rule 12), suggested: "S93 cross-examination: s93_xexam_mimo_I, point 1 (X11 CHALLENGED, WORDING should be CLAIM); s93_xexam_atria_I, points 6–7 (X11 UPHELD) — FIX, kind and declaration: KIND WORDING → CLAIM, declaration added; OLD, NEW and REASON WORD erratum as proposed."

**6. Noted for the orchestrator, not ruled.**
- **The count changes.** Entering X11 as CLAIM makes the list's count of entries that change the theory text 58, with CLAIM 52, WORDING 4 and ORDER 2. The note's "51 of the 57 changes" would read "52 of the 58 changes".
- **Rule 12.** Its "X11, if not dropped, is entered as a new WORDING entry" describes the proposal. Under rule 4, this FIX sets the kind.
- **File 12 has the same slip.** File 12 (`authority/12 … causality, standalone theory.md`, L325) carries the same sentence. It is under no round, and nothing was written into `authority/`.

**7. Question (a).** Both replies say X11 has no bearing on rivals, variation, criticism or error correction, and the checker agrees. The entry names no rival set, count, grade or record, and it changes only which port the mismatch is stated in.

X11: FIX
