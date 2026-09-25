# Ruling: S93 X05 (W35.2)

*A fresh Claude checker, 25 September 2026, under "S93 How the cross-examination of draft 4 will be read - written before sending.md" (md5 f1da3d1941499e0a8e6388a046275a0f), rules 4, 5, 6, 9, 10, 11 and 12. This checker did not draft, assemble or check the change list, did not write the part briefs, and has read no S93 reply other than the two below. It read, of the tabulation (md5 739d4d6bccc83caa03589bd45d030396), only §2.2's X05 entry, §3.3 and X05's entry in §7. It opened no reasoning, request or attempt file, and no other ruling in this folder.*

*The replies.* Both are part G, pass 1, attempt 1, status 200, finish "stop", 0 bad chunks, accepted, with END OF REPORT on the last line; each response sha256 matches its receipt.
- `s93_xexam_atria_G.response.txt`, sha256 1fd09ff31ccc82f66576bfd709988ca41c0153cc39ea67c8b702880b7ef59cff, 1,484 words by `wc -w`.
- `s93_xexam_mimo_G.response.txt`, sha256 720203266a809093a19d4faa916809599ab477259aaaf6928dc242ad1993880a, 1,451 words by `wc -w`.

*Sources.*
- Change list, `tests/Revision 2 - change list, draft of 23 September.md`, md5 b6b2ea95ea9e21ebea3316d8e9fa4b40 (the draft-4 md5 the reading rule names).
- Draft-4 theory text, `tests/Revision 2 - file 13 draft 4, theory text.md`, md5 fc55b470c63cd4b3c27d6aa64d8d8c17. Line numbers below are its own (L).
- Part G brief, md5 116b65985d098eb606855954fa34bc71.
- For background: `results/S90 reading rulings/ruling s90_xexam_mimo_C item 4 R13.md`, `ruling s90_xexam_atria_C item 1 R13.md`, and `results/S90 Verification of draft 3.md` (its W35.2 row).

## The entry

W35.2, "Part IV: a constructed transport is violated, not surprised". Group C, item W35 (b′). Part IV, "Expectation, surprise, violation", draft-4 L223 (file-11 L225). One sentence is added after s4.

- **KIND:** CLAIM. **REASON WORD:** clarification.
- **OLD:**

````text
Whether the correspondence could have been otherwise at such a change is a fact about its population (Derivation 3).
````

- **NEW:**

````text
Whether the correspondence could have been otherwise at such a change is a fact about its population (Derivation 3). Expectation and violation are defined for every transport to the simulation layer, surprise only for a selected one: a constructed one that fails at a pair of its contract is violated, and the failure is not surprise; a violation the system represents can be a recognized difficulty (Part X).
````

- **DECLARATION:** "Part IV now says, restating its definitions, that expectation and violation are defined for every transport to the simulation layer and surprise only for a selected one; that a constructed transport to the simulation layer that fails at a pair of its contract is violated, and the failure is not surprise; and that a violation the system represents can be a recognized difficulty."
- **CHECK:** "check 2, FIX. File 11 says a system is surprised and a transport is violated, never surprised; NEW reads "is violated, and the failure is not surprise". N18 Q3's Dov half stays watched (his transport need not be read as selected). Companion entry W35.4 added." Its S90 line records the FIX of R13 (Mimo C point 4; Atria C point 1), reconciled by the batch-3 recorder to Mimo C's text: the opening clause scoped "to the simulation layer", the instance written "a constructed one" "so that 'violated' stays inside that scope", and the restated clause added to the declaration.
- **REASON (the parts that bear here):** plan 1.2 asks for surprise to be kept for selected transports "and said so", and "This sentence says it"; the sentence joins a represented violation to Part X's recognized difficulty, which is "how the refutation of a constructed theory gets a place in the semantics without being called surprise"; "can be" because a violation is a recognized difficulty only when fidelity at that pair is a claimed obligation whose failure the system represents. The S90 paragraph narrows "every transport" to transports to the simulation layer and says no case moves.
- **CASES AT RISK:** N18, toward on Q3 ("Rhea's bridge fails at a pair her contract covers, so her grounds are contradicted"; the Dov half, read as selected, is surprise and is watched); O3 holds; O13 and O23 checked. The part G brief lists N18, O23, O3, O13.
- **LOSS:** none beyond W35.1's; after S90, a constructed transport with another target is not called violated by this section.

The definitions the sentence restates (W35.1, as draft 4 has them) are at L217–221: "Let \(t\) be a transport to the simulation layer \(S\), with contract \(C\) and, where \(t\) is selected, history \(H\). For an edit–boundary pair \((a,b)\in C\) actually occurring:", then expectation (L219), "a **violation** occurs when fidelity fails at \((a,b)\)" (L220), and surprise (L221).

## Atria's argument

Closing line: `X05: UPHELD`. Atria makes five points on X05. None of them raises the occurrence condition.

1. **Point 2 (T1).** Attack: the clause "a violation the system represents can be a recognized difficulty (Part X)" is unsupported, since no text makes a transport's fidelity a claimed obligation. Atria reports it failing: "can be" is existential; Derivation 10 gives a model; L201 gives the shape; L317 uses the same device.
   - Quotation check. "a violation the system represents can be a recognized difficulty (Part X)": found at L223. The L429 definition ("a failure of a claimed obligation, or a conflict … when the system represents it"): found at L429. "predict displacements correctly": found at L628. "a represented target and criticism in its history": **not found**; L201 reads "a selected transport has no represented target and no criticism in its history; a constructed one has both", which says the same of a constructed transport. "A problem that a system represents can be a recognized difficulty (Part X)": found at L317.
   - What the texts say. The conclusion holds: L429 makes a represented failure of a claimed obligation a recognized difficulty, so a violation that is such a failure and is represented is one, and "can be" claims no more. But Atria misreads Derivation 10. At L628 "predict displacements correctly" is the obligation *protected*; the obligation repaired, which is the one the occlusion failure bears on, is "possess a deployable account of re-emergence after occlusion". The model still exists; it is not the obligation Atria names.
2. **Point 4 (T2).** Attack: the item is ORDER with one clause appended. Atria reports it failing: the sentence carries claims beyond the restatement (the constructed transport "is violated, and the failure is not surprise"; the link to recognized difficulty, stated nowhere in the current text); CLAIM is right; "the declaration enumerates all three parts accurately". Quotation check: "restating its definitions" found in the brief at l.566 (the declaration); "is violated, and the failure is not surprise" and "can be a recognized difficulty (Part X)" found at L223.
3. **Point 6 (T3).** X04 and X05 interlock: X05's link needs "a violation *the system represents*" (L223, emphasis Atria's), and L211 withholds representation from declared transports; L225 and L429 stay consistent; L223's unchanged sentences stay true. Quotation check: "does not make an occurrence represent anything" found at L211; "A system with no transport cannot be surprised" and "A system whose history exhausts its contract cannot be surprised" found at L223.
4. **Point 8 (T4).** O23, O13, O3, O24, O11, O48 and O5 do not move away. Quotation check: "A dimension of variation mentioned in passing is not thereby a port of the account" found at L425. The line citations without quotation check out: ProducedBy at L307, (K3) at L395, "keeps its inherited provenance" at L409, selection in the physical module at L481, the narrowing sentence at L159, Historical index at L367.
5. **Point 9 ((a)).** Neither item touches hard to vary, rivals, counts, grades or records. Quotation check: "with no record of which candidates failed before or of how any was changed" found at L369.

## Mimo's argument

Closing line: `X05: CHALLENGED — the restatement omits the block's "actually occurring" scoping and its declaration repeats the omission`.

1. **Point 1 (T1, T2): the challenge.**
   - (i) The definitions are scoped to occurring pairs (L217, "actually occurring"; L220, a violation "occurs").
   - (ii) L223 restates them as "a constructed one that fails at a pair of its contract is violated", with no occurrence condition. Read as written, a fidelity failure at a pair of \(C\) that never occurs is a violation, which the definitions do not support.
   - (iii) The theory keeps fidelity at a pair apart from occurrence elsewhere: a candidate claims (F1), (F2) and (A) "at every pair of \(C\), tested or not" (L315); Part VIII speaks of "a pair \((a,b)\in C\)" with no occurrence (L369). And violation is event language: surprise is "the signature of a selected transport meeting a change outside its history" (L584).
   - (iv) O24: on the loose reading an arrangement mismatching at the unused setting "is violated", "converting a fit-and-rivals fact into an event".
   - (v) The declaration repeats the unscoped phrase.
   - (vi) The third clause "sits ill" under "restating its definitions": it is a link to L429, not one of Part IV's definitions, and new against the current text, "which is why the item is rightly CLAIM".
   - It proposes a NEW that reads "a constructed one whose fidelity fails at a pair of its contract that actually occurs is violated", and a declaration with the same change whose third clause reads "and, a link to Part X rather than one of those definitions, that a violation the system represents can be a recognized difficulty" (both given whole in the reply, lines 11–19).
   - Quotation check. L217 (with the ellipsis): found. "a **violation** occurs when fidelity fails at \((a,b)\)": found at L220. "a constructed one that fails at **a pair of its contract** is violated": found at L223. "claims (F1), (F2) and (A) at every pair of \(C\), tested or not": found at L315. "a pair \((a,b)\in C\)": found at L369. "the signature of a selected transport **meeting a change** outside its history": found at L584. "the record has not chosen between them": found in the brief at l.646 (O24's verdict). "restating its definitions": found in the brief at l.566. The L429 definition: found at L429. The bold is Mimo's throughout.
2. **Point 7 (T3).** The present "every transport to the simulation layer" removes the earlier form's clash with L219 and L177; clause three points correctly at L429 and parallels L317; O13 and O23 are untouched. Quotation check: "defined for every transport" found in the brief at l.587 (the earlier wording); "\(S\) is where expectation lives" found at L177; "A problem that a system represents can be a recognized difficulty (Part X)" found at L317; "the contributions whose active routes ran to it" found at **L307**, not L308 as Mimo cites; L425 found. Nothing turns on the line number.
3. **Point 8 ((a)).** No listed set, enumeration, count, grade or record: faithful.

## Rulings

Rule 5: this is a disagreement. Atria upholds X05; Mimo challenges it. Atria's reply does not take up the occurrence condition at all, and by rule 2 its silence is no support. Its points (the link to Part X, the kind, the interlock with X04, the cases) are answered below where they bear on the challenge. Neither reply disputes a fixed verdict (rule 10), and no point on X05 comes from outside part G (rule 11). Part G asks the standard tests only, and its (a) paragraphs agree, so rule 6 gives the checker nothing to record for the owner. The fix below touches no rival, count, grade or record, and (a) stands as both replies give it.

### 1. The dropped occurrence condition in NEW: upheld (FIX)

**What the texts say.**
- **The definitions are scoped to pairs that occur.** "For an edit–boundary pair \((a,b)\in C\) actually occurring:" (L217) introduces the bullet list. Expectation (L219) and violation (L220) are defined only at such a pair.
- **Fidelity at a pair is stated whether or not the pair occurs.** (F1) and (A) are quantified "for every \((a,b)\in C\)" (L233, L247). "Every conjunct is a condition on how supplied relations behave under the changes in \(C\)" (L265). The component relations "are supplied independently for each \((a,b)\)" (L574). A candidate claims fidelity "at every pair of \(C\), tested or not" (L315). So a transport's fidelity can fail at a pair of its contract that never occurs.
- **L223's sentence is a free-standing universal.** It is a separate paragraph, outside the "For … actually occurring:" frame of the bullets. It speaks of "a constructed one", not of \(t\). And it gives a sufficient condition in words of its own: fails at a pair of its contract, therefore violated.
- **A counterexample on the literal reading.** Take a constructed transport to \(S\) with contract \(C=\{(a_1,b),(a_2,b)\}\). Only \((a_1,b)\) ever occurs, fidelity holds there, and fidelity fails at \((a_2,b)\). L217–220 give no violation, because the only pair in their scope is one where fidelity holds. L223, as written, says the transport "is violated", because it fails at a pair of its contract.
- **The theory's "violated" is an event tied to an expectation.** Derivation 4's proof reads "If there is no transport there is no expectation and hence no violation" and "every occurring \((a,b)\) is in \(H\)" (L582). Derivation 10 reads "is violated when the thing re-emerges" (L624). L584 reads "meeting a change", and L225 "Two responses to a violation". Expectation exists only at an occurring pair (L217–219). So a violation at a pair that never occurs would be a violation with no expectation, which L582's "no expectation and hence no violation" treats as impossible.

**Atria's side, at its strongest.** The sentence announces itself as a restatement: "Expectation and violation are defined for …:". "Is violated" can only mean what L220 defines, so the reader imports the occurrence condition. And "fails" in the present tense can be read as an event, failing when the pair comes. That reading is available, and the text does not force the false one. But it does not save the entry, for two reasons.
- A sentence that presents itself as restating definitions has to match them on its plain reading. This one is wider on its plain reading, and the repair costs two words.
- The declaration stands alone in the record, with no L217 frame around it. It says that "a constructed transport to the simulation layer that fails at a pair of its contract is violated", and nothing there supplies the occurrence condition. As a statement of what Part IV claims, the declaration is wider than the definitions it says it restates. That is a T2 defect whatever reading L223 gets.

**Was the drop intended, and is it declared?** It was not intended, and it is not declared.
- The phrase "fails at a pair of its contract" was in the drafted NEW before S90, as quoted in both S90 R13 rulings. Neither S90 ruling examined occurrence. Both scoped the sentence by the transport's *target* ("to the simulation layer"). The Mimo C ruling wrote the instance "a constructed one" "so that 'violated' stays inside that scope", that is, so that the instance should not reach beyond what the definitions define.
- The REASON's example is "the refutation of a constructed theory", which is an event. The N18 note in CASES AT RISK is an occurring pair: opening day, "a pair her contract covers". W35.1's GAIN reads "A constructed theory that fails is violated in the text's own terms", and the text's own terms (L217–220) require occurrence.
- The declaration calls the sentence "restating its definitions", which is true only with the condition.
- Had the wider reading been meant, it would change W35.1's definitions, which say nothing of the kind. It would clash with L582. And it would need a declaration of its own. None exists.

**Mimo's O24 argument does not show a verdict move.** O24's two wiring arrangements are rival candidate arrangements, whose transports run to the target, not to the simulation layer. W35.2's LOSS says such a transport is not called violated by this section, so the clause does not reach them. Even if one were called "violated" at the unused setting, the fixed verdict concerns what the record has chosen, and an unrepresented violation at a setting nobody used chooses nothing. O24 does not move on either reading. The challenge is upheld on T1, T2 and T3, not T4.

**Mimo's "whose fidelity fails" is not adopted.** Mimo gives no argument for it. A transport that "fails at a pair" already reads as its fidelity failing there, since faithfulness is defined by the fidelity conditions (L189). The smallest change keeps "that fails".

**Choice of words.** "an actually occurring pair of its contract" repeats L217's own words, "actually occurring", and inserts two words. Mimo's "a pair of its contract that actually occurs" says the same, but adds a second relative clause to a clause that already has one. The shorter insertion is used in both NEW and DECLARATION.

### 2. The declaration repeats the omission: upheld (FIX, with ruling 1)

The declaration's second clause copies the NEW's unscoped phrase. With the two words added, the clause is an instance of L220–221, and with L193's "exactly one of three provenances" a constructed transport's violation is not surprise. So "restating its definitions" becomes true of it. The declaration must change, and it changes only in that clause.

### 3. The third clause under "restating its definitions": not upheld (KEEP)

The two replies differ here. Mimo says the link "sits ill" under the participial phrase; Atria says the declaration "enumerates all three parts accurately". Atria is right.
- "Its definitions" are Part IV's. The recognized difficulty is Part X's term (L429), and nothing in the declaration presents it as a Part IV definition.
- The link is listed as something Part IV "now says". That is what declares it as a change of claim, and with the KIND, CLAIM, it is declared.
- Both replies agree the link is new against the current text and that the kind is CLAIM, and the present declaration says nothing contrary.

Mimo's rephrasing ("and, a link to Part X rather than one of those definitions, that …") is clearer on a strict parse. It is not needed to state the matter truly, and it is not the smallest change, so it is not adopted.

### 4. Atria's own attacks, and the kind

- The link to Part X is true as "can be" (ruling on Atria's point 2 above, with its misreading of L628 noted).
- The KIND stays CLAIM: both replies agree, and the link and the violation of a constructed transport are both new against file 11.
- The interlock with X04 (Atria point 6; Mimo point 7) is unaffected, because the fix brings L223 into line with X04's L217.

### 5. Verdicts under the fix (CASES AT RISK and the brief's cases)

- **N18.** Opening day's crowd actually occurs, and on Rhea's bridge it is "no larger than the crowds she had calculated for", a pair in her contract.
  - Rhea's constructed transport fails at an actually occurring pair of its contract, so it is violated and the failure is not surprise. Her grounds are contradicted: Q2 and Q3 hold as CHECK and CASES AT RISK state.
  - Dov's half (a selected transport, surprise) is untouched and stays watched.
  - Q1 runs through the recognized-difficulty clause, which is unchanged.
- **O23.** No expectation, violation or surprise is at issue, and L425 governs. Not reached.
- **O3.** Nadia's transport is selected, and her surprise is surprise. The verdict turns on construction. The constructed-transport clause does not reach it.
- **O13.** Nothing is credited by the clause, and ProducedBy (L307) governs. Not reached.
- **O24, O11, O48, O5** (the brief's cases for X04). None turns on a constructed transport's violation. O24 is treated in ruling 1.
- **D3-T** (named in the REASON). Not reached, as S90 found.

No fixed verdict moves.

### The FIX, ready to paste

- **OLD:** unchanged.
- **NEW:**

````text
Whether the correspondence could have been otherwise at such a change is a fact about its population (Derivation 3). Expectation and violation are defined for every transport to the simulation layer, surprise only for a selected one: a constructed one that fails at an actually occurring pair of its contract is violated, and the failure is not surprise; a violation the system represents can be a recognized difficulty (Part X).
````

- **DECLARATION:**

````text
Part IV now says, restating its definitions, that expectation and violation are defined for every transport to the simulation layer and surprise only for a selected one; that a constructed transport to the simulation layer that fails at an actually occurring pair of its contract is violated, and the failure is not surprise; and that a violation the system represents can be a recognized difficulty.
````

- **KIND:** CLAIM (unchanged). **REASON WORD:** clarification (unchanged).
- **Does the fix change what the theory claims?**
  - Against the draft-4 wording on its literal reading, yes: it withdraws "violated" from a constructed transport whose fidelity fails only at pairs that never occur.
  - Against the definitions at L217–220 and against file 11, no: those never called such a transport violated.
  - The entry now claims what its REASON and CASES AT RISK describe. The declaration must change with the NEW, and the text above does that.
- **For the CHECK field (rule 12):**

````text
S93 cross-examination: s93_xexam_mimo_G point 1 (X05 CHALLENGED: the restatement omits "actually occurring", and the declaration repeats it); s93_xexam_atria_G points 2, 4, 6, 8 and 9 (X05 UPHELD; the occurrence condition not raised) — FIX, after the S93 cross-examination. The instance reads "fails at an actually occurring pair of its contract", in L217's words, since the definitions are scoped to pairs actually occurring while fidelity is stated at every pair of the contract, occurring or not; the declaration carries the same words, so that "restating its definitions" is true of it. Mimo's "whose fidelity fails" and its rephrased third clause of the declaration are not adopted. No case moves.
````

- **For the LOSS field (optional, to keep the record whole):**

````text
After the S93 cross-examination, a constructed transport whose fidelity fails only at pairs of its contract that never occur is not called violated by this sentence; the definitions at L217–220 never called it so.
````

## Findings for later entries

- **Nothing else repeats the clause.** In the live texts (the change list and the draft-4 theory text), the phrase "fails at a pair of its contract" occurs only in W35.2's NEW and DECLARATION and at L223. It also occurs in records that are not edited: the eleven S93 briefs' excerpts, draft 3's theory text, and working files under `tests/working files/`. The summary table row at change-list l.126 quotes only "is violated, and the failure is not surprise" and needs no change. The note of sources' *Surprise and problems* bullet (W38.1) does not restate the clause.
- **W35.1 (X04) needs nothing from this ruling.** Its L217 already carries "actually occurring", and the fix aligns L223 with it. L582, which relies on "every occurring \((a,b)\)" and on "no expectation and hence no violation", supports the fix. This checker does not rule on Mimo's point 2 about L582's wording, which is X04's.
- **Atria point 2 misnames Derivation 10's obligation.** "predict displacements correctly" (L628) is the protected obligation. The repaired one is "possess a deployable account of re-emergence after occlusion". Any later reading that relies on Atria's point 2 should use the latter.
- **Two quotations in the replies are off.** Atria's "a represented target and criticism in its history" is not in the text; L201 reads "a constructed one has both". Mimo's L308 is L307.
- **Rebuild check.** `tools/s89_apply_changes.py --self-test` should find the fixed NEW once in the rebuilt draft and the old NEW nowhere, after all rulings are applied (rule 12).

X05: FIX
