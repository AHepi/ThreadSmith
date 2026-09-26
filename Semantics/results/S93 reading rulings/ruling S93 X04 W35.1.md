# Ruling S93 X04 · W35.1: expectation and violation (Part IV, draft 4 L217–221)

*A fresh Claude checker, 25 September 2026. It did not draft, assemble or check the change list, did not write the S93 briefs, and has read no S93 reply other than the two it was given. It works under "S93 How the cross-examination of draft 4 will be read - written before sending.md", rules 4, 5, 6, 9, 10, 11 and 12. It did not read any other checker's ruling or any other item's section of the tabulation.*

*What it read, in order:*
- *the reading rule;*
- *in "S93 Tabulation of the replies, before any ruling.md": §2.2's entry for X04, §3.2 (X04.1–X04.11) and §7 item 2;*
- *`s93_xexam_atria_G.response.txt` and `s93_xexam_mimo_G.response.txt`, the response files only;*
- *the part G brief (md5 116b65985d098eb606855954fa34bc71, as the rule states);*
- *the change list (md5 b6b2ea95ea9e21ebea3316d8e9fa4b40): W35.1, and for comparison W35.2 and W35.4;*
- *the draft-4 theory text (md5 fc55b470c63cd4b3c27d6aa64d8d8c17), L173–229, L556–600 and L614–632;*
- *file 11 (md5 5e494c1095d920d128b9a79de378f923), read only: L219 and L572;*
- *for background, S90's ruling on R12 (`ruling s90_xexam_mimo_C item 1 R12.md`) and "S90 Verification of draft 3.md";*
- *`tools/s89_apply_changes.py`, to see what form an entry can take.*

*Line numbers are draft 4's unless marked "file-11". Draft-4 L582 is file-11 L572; draft-4 L217–221 is file-11 L219–223.*

## The entry

**W35.1 — Part IV: expectation and violation for every transport; surprise kept for selected ones.**
- Place: X04, Part IV, "Expectation, surprise, violation", draft 4 L217–221 (file-11 L219–223).
- Group C, item W35 (b′). STATUS applied.
- **KIND:** CLAIM. **REASON WORD:** clarification.

**OLD:**
````text
Let \(t\) be selected on history \(H\) with contract \(C\). For an edit–boundary pair \((a,b)\in C\) actually occurring:

- the **expectation** is \(\operatorname{Ans}_S(\tau(a),\sigma(b))\);
- a **violation** occurs when fidelity fails at \((a,b)\);
- **surprise** is a violation at \((a,b)\notin H\).
````

**NEW:**
````text
Let \(t\) be a transport to the simulation layer \(S\), with contract \(C\) and, where \(t\) is selected, history \(H\). For an edit–boundary pair \((a,b)\in C\) actually occurring:

- the **expectation** is \(\operatorname{Ans}_S(\tau(a),\sigma(b))\);
- a **violation** occurs when fidelity fails at \((a,b)\);
- **surprise** is a violation of a selected transport at \((a,b)\notin H\).
````

**DECLARATION:** "Part IV now defines expectation and violation for every transport to the simulation layer, whatever its provenance, and keeps surprise for a violation of a selected one at a pair outside its history."

**CHECK field:**
- "check 2, SOUND. Widening violation leaves L227's selection response speaking of an H that a constructed transport lacks; the companion entry W35.4 fixes that. The diff shows two hunks for this one entry (L219 and L223)."
- The S90 line: Mimo part C, R12 FALLS; fresh checker FIX. The preamble was narrowed to "a transport to the simulation layer \(S\), with contract \(C\)" and the declaration to "for every transport to the simulation layer, whatever its provenance".

**The REASON on Derivation 4.** This part of the entry was withheld from the readers. It bears on the point at issue:

> Derivations 4 and 10 are unchanged and stay true word for word. Derivation 4 reads "A system can be surprised only if it holds a transport selected on a history H …" and its proof reads "Surprise is defined as a violation at (a,b)∉H".

**CASES AT RISK:**
- O3 holds AGREE.
- N18 moves toward the fixed verdict on Q2.
- O5, O11, O24 and O48 are untouched.
- Derivation 10 is unchanged.

**What the replies closed with.** Atria `X04: UPHELD`; Mimo `X04: UPHELD`. The item comes to this checker because:
- Mimo's point 2 shows an unchanged sentence (L582) made stale by the item, and gives words for it. Rule 3 counts that as a challenge.
- Atria's point 7 examines the same sentence and finds nothing stale. Rule 5 makes that a disagreement.

## Atria's argument

Atria's points on X04 are 1, 3, 5, 7 and 9. Point 6 is on X05 and mentions X04 only in passing: it is X05's checker's, and it is not ruled here.

**Point 1 (T1), reported as failing.**
- *Attack.* Giving a declared transport an "expectation" is false, since "A declared transport does not make an occurrence represent anything; it makes a modeller assert that it does" (L211), and "\(S\) is where expectation lives." (L177).
- *Why Atria says it fails:*
  - expectation is an answer-profile value (L219), and "Surprise is not a feeling added to the semantics" (L584);
  - Part V evaluates fidelity without a provenance test: "Every conjunct is a condition on how supplied relations behave under the changes in \(C\)" (L265);
  - the provenance taxonomy (L193, "exactly one of three provenances") governs representation (R) at L205–209;
  - the declaration's "whatever its provenance" makes the reading explicit.
- *Quotations.* Found: L217 ("Let \(t\) be a transport to the simulation layer \(S\)"), L211, L177, L584, L265, L193, and "whatever its provenance" (brief G §4 l.524).
- *Ruling on the texts.* Agreed. The block defines values and events on transports. (R) at L205–208 says what represents; it does not restrict L217–221.

**Point 3 (T2), reported as failing.**
- *Attack.* The item is ORDER or WORDING, since L225 already spoke of "Two responses to a violation", one of them "A construction response".
- *Why Atria says it fails.* The old block scoped all three definitions to a selected \(t\), so the new wording lets a reader conclude something new. The declaration matches L217–221.
- *Quotations.* Found: the old wording "Let \(t\) be selected on history \(H\) with contract \(C\)" (brief G §4 l.529); "Two responses to a violation" and "A construction response" at L225; the declaration's phrases at brief G §4 l.524; "surprise is a violation of a selected transport at \((a,b)\notin H\)" at L221 (without the bold).
- *Ruling on the texts.* Agreed:
  - a response *to* a violation does not define violation for a constructed transport;
  - in file 11, "violation" is defined only inside the selected-scoped block;
  - CLAIM is the right kind, and the declaration is exact.

**Point 5 (T4, N18), reported as a move toward the fixed verdict.**
- *Argument.* Under the old text the theory was silent on whether the swaying went against what Rhea expected; under L217–220 both designers' expectations are violated. That moves toward "Yes, the swaying went against what both expected", and the declaration accounts for it.
- *Quotations.* Found: "survival on \(H\) does not distinguish \(t\) from \(t'\) there" (L572) and "the blanket claim that every untested value is unconstrained" (L576).
- *One slip.* Atria gives "Rhea's violation is violation-but-not-surprise (L223)" as "unchanged text". That clause of L223 is X05's new sentence, not unchanged text. It does not bear on X04, whose move on N18 is Q2 only, as its CASES AT RISK says.
- *Ruling on the texts.* Agreed. The move on Q2 is toward the fixed verdict and is declared.

**Point 7 (T3), reported as "no stale sentence".** This is the point in dispute.
- *Argument.* Derivation 4's claim and proof "remain correct under the narrower new definition of surprise; the proof's omission of "selected" is a simplification inside a claim already about a selected transport, not a contradiction."
- *Two further observations.* Terms are defined before use (\(S\) at L177, transports at L183–189, provenances at L193–199). The revision from the earlier reading's "Let \(t\) be a transport with contract \(C\)" repairs "a genuine forward-reference".
- *Quotations.* Found: the Claim's words at L580; "Surprise is defined as a violation at \((a,b)\notin H\)" at L582; the earlier wording at brief G §4 l.553.
- *Ruling on the texts:*
  - "Not a contradiction" is right (see Rulings).
  - "A claim already about a selected transport" is the wrong ground. "Selected" is what the Claim at L580 concludes. It is not a premise the proof may assume.
  - "No stale sentence" is wrong (see Rulings).
  - On the forward reference: \(S\) was already defined at L177 before the earlier wording. What S90 repaired was a typing gap: \(\operatorname{Ans}_S(\tau(a),\sigma(b))\) is typed only for a transport whose target is \(S\). The misdescription does not affect X04.

**Point 9 ((a), X04 and X05).**
- *Argument.* Neither item touches hard to vary, rivals, counts, grades or records. Both are "faithful to, or merely neutral with respect to, the owner's words and the rule".
- *Quotations.* Found: "with no record of which candidates failed before or of how any was changed" (L369).
- *Ruling on the texts.* Agreed for X04: it defines three terms by provenance and has nothing to do with a list, a count, a grade or a record.

## Mimo's argument

Mimo's points on X04 are 2, 3, 4, 5, 6 and 8. Point 1 (the "actually occurring" scoping) and point 7 are on X05: they are X05's checker's, and they are not ruled here.

**Point 2 (T3): the challenge.**
- *Argument, part 1.* After X04 the definition is "a violation **of a selected transport** at \((a,b)\notin H\)" (L221; the bold is Mimo's), but L582 still reads "*Proof.* Surprise is defined as a violation at \((a,b)\notin H\)." So L582 "reports a broader definition than the text has".
- *Argument, part 2.* "on that report the Claim at L580 … would be false, since a constructed transport failing at an unseen pair would then be surprise."
- *Argument, part 3.* The Claim and the Consequence (L584, "the signature of a selected transport meeting a change outside its history") match the revised definition, so "what lags is one proof sentence"; "X04 is not the place to fix this, so it does not overturn the item."
- *Words proposed for L582:* "Surprise is defined as a violation of a selected transport at \((a,b)\notin H\); a transport that is not selected is not subject to surprise at all."
- *Quotations.* Found: L582 (the proof sentence), L221 (bold aside), L580, L584.

**Point 3 (T1), reported as failing.**
- *Attack.* "whatever its provenance" against (R): L211 and L13's "a modelling convenience".
- *Why Mimo says it fails:*
  - the block defines values and events on transports as such, and (R) governs representation;
  - surprise stays with selected transports;
  - X05's clause needs "a violation the system represents" (L223), which (R) withholds from declared transports.
- *Quotations.* Found: L211, L13, L223, and brief G §4 l.524.
- *Ruling on the texts.* Agreed, as for Atria's point 1.

**Point 4 (T3), reported as failing.**
- *Attack.* The preamble binds \(H\) only "where \(t\) is selected" (L217), so the \(H\) in the third bullet is unbound when \(t\) is not selected.
- *Why Mimo says it fails.* The bullet speaks of "a selected transport", and the declaration's "at a pair outside its history" settles the reading. "A tightening would be welcome but is not required."
- *Quotations.* Found: L217, L221, and the declaration (brief G §4 l.524).
- *Ruling on the texts:*
  - Agreed that this is no defect of X04. The bullet's "of a selected transport" gives \(H\) its referent.
  - The same fact, that \(H\) exists only for a selected \(t\), is what keeps L582 from being false. See Rulings.

**Point 5 (T4, N18), reported as a declared move toward the fixed verdict.**
- *Quotations:*
  - Found: "Let \(t\) be selected" (brief G §4 l.529); L219's expectation; "Yes, the swaying went against what both expected", "contradicted what Rhea had reason to expect" and "nothing Dov had reason to expect" (brief G §7 l.628); L223's sentence on the population (Derivation 3).
  - **Not found:** "did the swaying go against what she expected". N18's question reads "Did the swaying go against what each designer expected?" (brief G §7 l.626).
- *Ruling on the texts.* Taken on N18's actual question, Mimo's substance stands. For Rhea, file 11 was silent on Q2 and the revised text agrees with the fixed verdict. The move is toward the fixed verdict, and the declaration states it.

**Point 6 (T3, T4), reported as failing.**
- *Argument.* O3, O48, O11 and O5 do not move:
  - selection was already required for surprise;
  - Nadia's transport is selected (L195);
  - O48 turns on Derivation 3;
  - O5 turns on L159.
- *Quotations.* Found: "is often surprised" (brief G §7 l.662); L195's "No member of the history represents \(t\), \(H\), or the survival condition"; both L159 sentences; "days other than Tuesdays" (brief G §7 l.674).
- *Ruling on the texts.* Agreed. None of these verdicts turns on the provenance scope of expectation or violation.

**Point 8 ((a), X04 and X05).**
- *Argument.* No listed set, enumeration, count, grade or record: faithful.
- *Quotations.* Found: L315 ("No list of all rivals is supposed"), L369 (both phrases), L429 ("Closing an episode is a decision, not a proof").
- *Ruling on the texts.* Agreed for X04.

## Rulings

### 1. The challenge: Derivation 4's proof sentence, L582 (Mimo point 2 against Atria point 7)

**Each side.**
- *Mimo:* after X04, L582 reports a broader definition of surprise than L221 gives. On that report the Claim at L580 would be false. The words need changing, but not in X04.
- *Atria:* the proof stays correct. The omission of "selected" is a simplification inside a claim already about a selected transport, and nothing is stale.

**What the proof has to show.** The Claim (L580): a surprised system holds (i) a transport, (ii) selected, (iii) on a history \(H\) strictly smaller than \(C\). The proof (L582) has three sentences:
- s1: "Surprise is defined as a violation at \((a,b)\notin H\)."
- s2: "If there is no transport there is no expectation and hence no violation."
- s3: "If \(H=C\), every occurring \((a,b)\) is in \(H\), so no violation at \((a,b)\notin H\) exists."

**In file 11,** the section opens "Let \(t\) be selected on history \(H\) with contract \(C\)" (file-11 L219):
- s1 repeats the third bullet word for word.
- All three definitions have a selected \(t\) as their subject. So s2 carries (i) and (ii): without a selected transport there is no expectation, hence no violation.
- s3 carries (iii).

**After X04:**
- Expectation and violation are defined for every transport to \(S\), whatever its provenance (L217–220). A constructed transport to \(S\) now has an expectation and can be violated (L223). s2 therefore carries only (i). It no longer carries (ii).
- The selection condition now lives in one place, the third bullet: "a violation of a selected transport at \((a,b)\notin H\)" (L221). The sentence of the proof that reports that bullet, s1, leaves out exactly those words.

**Is L582 false?** No.
- L217 introduces \(H\) only "where \(t\) is selected". A transport has exactly one provenance (L193), so a constructed or declared transport has no \(H\) in this section.
- "A violation at \((a,b)\notin H\)" can therefore be had only by a selected transport. s1 picks out the same events as L221.
- Mimo's "a constructed transport failing at an unseen pair would then be surprise" does not go through on the text. For a constructed transport there is no \(H\) for the pair to lie outside.
- "History" in L193 and L201 is the transport's history in the physical module. It is not the \(H\subseteq C\) of L195 and L217.
- The Claim at L580 is untouched, and the proof is still valid.

**Is L582 merely compressed?** Not on Atria's ground.
- The proof may not take "selected" from the Claim, because (ii) is what the Claim concludes. Atria's sentence treats it as a premise.
- In file 11, (ii) came from the section's scope, through s2. After X04 it can come only from an inference the proof does not state: \(H\) presupposes selection (L217).
- A compression that leaves one of three conclusions to an unstated typing step, after the step that used to carry it has been taken away, is more than a simplification.

**Is L582 stale?** Yes. This is the brief's T3 defect, "an unchanged sentence that the item makes … stale":
- s1 was a verbatim report of the third bullet, and X04 rewrote that bullet.
- The words X04 added, "of a selected transport", are the words the proof now needs.
- The entry's REASON checked the Claim and the proof for truth, and it is right that both stay true. It did not notice that s1 had stopped quoting the definition, or that s2 had stopped carrying (ii).
- Check 2 found the same kind of knock-on at file-11 L227, and entered W35.4 for it. It missed this one.

**Where the repair belongs.** In a separate companion entry, not in X04's OLD or NEW.
- *The form of an entry.* An applied entry has one OLD and one NEW. Its OLD must occur once in file 11 as one contiguous span, and no two applied OLDs may overlap (`s89_apply_changes.py`, `check_entries`).
  - W35.1's OLD is file-11 L219–223. The proof is file-11 L572.
  - An OLD spanning both would take in every applied entry between them and be refused.
- *Precedent.* The change list's own answer to this situation is a companion entry: W35.4 ("Check 2's companion to its W35.2 fix. After W35.1, violation is defined for every transport, …"), KIND WORDING against file 11.
- *X04's own fields.* None of them is wrong:
  - OLD and NEW are the block as it should read;
  - the KIND is CLAIM, rightly;
  - the DECLARATION is exact (both replies agree, and this checker agrees on the texts).
- *X04's own wording creates the need.* So the companion should be entered in the same S93 edit step (rule 12) and not left to a later revision. Otherwise draft 5 would carry a proof whose first sentence misreports the definition it cites.

**Mimo's words.**
- The first clause is adopted. It is the third bullet's own wording, and it is the smallest change that puts (ii) back into the proof: s1 then gives (ii) directly, s2 still gives (i), and s3 gives (iii).
- The second clause, "a transport that is not selected is not subject to surprise at all", is not adopted:
  - it repeats what L223 already says ("surprise only for a selected one");
  - it introduces a phrase the text uses nowhere else;
  - the proof does not need it.

**Cases at risk.** The companion changes the proof's report of a definition and nothing else.
- The Claim, the definition and every other sentence stay as they are.
- O3: Nadia's transport is selected, so her "often surprised" is still surprise.
- N18: Rhea's violation and Dov's surprise are read off Part IV, not off this proof.
- Derivation 10 (L622–624): \(t_0\) is selected on \(H_0\), and "This is surprise (Derivation 4)" stands.
- O5, O11, O24 and O48 do not reach Derivation 4.
- No fixed verdict moves.

**Declaration.**
- X04's declaration does not change.
- The companion is WORDING against file 11, where every \(t\) of the section is selected, so it carries no declaration, as W35.4 carries none.
- What the theory claims does not change.

**Ruling on the challenge.**
- As a challenge to X04 (that the item should not stand as it is), it is **not upheld**: X04 is **KEPT**. Mimo reaches the same conclusion ("it does not overturn the item").
- The finding under it, that L582 is stale after X04, **is upheld**. Atria's point 7 is overruled on that finding.
- The repair is the companion entry given below.
- This KEEP does not mean that L582 is fine.

### 2. The other points on X04

None of these is a challenge.
- Atria's points 1, 3, 5 and 9 and Mimo's points 3, 4, 5, 6 and 8 each report an attack as failing, and this checker agrees on the texts. The slips noted are:
  - Atria 5's "unchanged text" for X05's clause;
  - Atria 7's "forward-reference";
  - Mimo 5's unquoted "what she expected".
  None of them affects the item.
- No point disputes a fixed verdict (rule 10).
- No point on X04 was raised outside part G (rule 11).
- On (a), both replies judge X04 faithful (Atria "faithful to, or merely neutral with respect to"; Mimo "Faithful"). Neither asks for a change of the text, so there is no rule-6 choice for the owner. The present wording states the matter truly: X04 states no rival, list, count, grade or record.

### 3. For W35.1's CHECK field (rule 12)

Words ready to paste:

````text
  - S93 cross-examination: KEEP (ruling S93 X04 W35.1). Both readers upheld X04. Mimo part G point 2 showed that Derivation 4's proof sentence (file-11 L572) still reports the old third bullet, so that after this entry the proof reaches its Claim's "selected" only through the typing of H at L219; Atria part G point 7 called the omission a simplification. L572 is not false but stale. OLD, NEW, KIND and DECLARATION stand; the repair is the companion entry W35.5, as W35.4 is for L227.
````

## Findings for later entries

**1. A companion entry for Derivation 4's proof (to be entered with the S93 edits).**
- The id W35.5 is free (W35.1–W35.4 exist).
- Place it after W35.4. The tool applies entries in file-11 order wherever they stand in the list.
- Text ready to paste:

`````text
### W35.5 — Part XVI, Derivation 4: the proof reports surprise as a violation of a selected transport

- **STATUS:** applied
- **GROUP:** C
- **ITEM:** W35 (b′), companion entry
- **FILE-11 LINE:** 572
- **WHERE:** Part XVI, Derivation 4, "Surprise requires an incomplete history", the first sentence of the proof (file-11 L572; draft 4 L582).
- **REASON WORD:** clarification
- **KIND:** WORDING
- **CHECK:** S93 cross-examination: new companion entry, proposed by the X04 checker (ruling S93 X04 W35.1) on Mimo part G point 2, against Atria part G point 7. WORDING against file 11, where every t of Part IV's section is selected.
- **OLD:**
````text
Surprise is defined as a violation at \((a,b)\notin H\).
````
- **NEW:**
````text
Surprise is defined as a violation of a selected transport at \((a,b)\notin H\).
````
- **DECLARATION:** none (WORDING against file 11; listed in the record). If a checker rules CLAIM: "Derivation 4's proof now reports surprise as a violation of a selected transport."
- **REASON:** Companion to W35.1. In file 11 the proof's first sentence repeats Part IV's third bullet word for word, and every t of that section is selected, so the proof gets its Claim's "selected" from the section's opening: without a selected transport there is no expectation (its second sentence). W35.1 defines expectation and violation for every transport to the simulation layer and moves selection into the third bullet ("a violation of a selected transport"), which the proof's first sentence leaves out; the proof then reaches "selected" only because H is introduced only where t is selected (L219), a step it does not state. The sentence is brought back to the bullet's words. In file 11 every t of the section is selected, so against file 11 the change is one of wording.
- **CASES AT RISK:** None moves. The Claim is unchanged; only the proof's report of the definition is. O3 (Nadia's transport is selected, so her "often surprised" is surprise, as before), N18 (Rhea's violation and Dov's surprise are read off Part IV, not off this proof) and Derivation 10 (t_0 is selected on H_0; "This is surprise (Derivation 4)" stands) were checked.
- **GAIN:** Derivation 4's proof reports Part IV's definition as it now stands, and states the step that gives its Claim's "selected".
- **LOSS:** None.
`````

(The five-backtick outer fence above is only for this ruling. The inner fences are the change list's own four-backtick fences, and they go into the change list as they stand.)

*Checked in memory, with no file written.* `s89_apply_changes.build` was run on the change list as it stands and on a copy held in memory with this entry inserted before W20.1. Nothing was written to disk, and Python ran with bytecode writing off.
- *Baseline:*
  - 65 entries parsed; 60 applied, 57 of them theory;
  - CLAIM 51, WORDING 4, ORDER 2; N = 51, M = 57, K = 42; 55 hunks;
  - theory md5 fc55b470c63cd4b3c27d6aa64d8d8c17, which is draft 4, reproduced.
- *With the entry:*
  - 66 parsed; 61 applied, 58 theory;
  - WORDING 5; N = 51, M = 58, K = 42; 56 hunks, each inside an entry;
  - the self-test refuses both planted edits;
  - theory md5 5f7888dba8be366f5caed39672bdd096.
  - The only difference from draft 4 is one line, L582, whose first sentence becomes the NEW above.
  - The OLD occurs once in file 11, on line 572.

*Consequences for whoever enters it:*
- The record numbers entries by file-11 order, so the new entry takes R2-55. The three entries after it (W7.6, W10a.1, and W19.3 + W10(b).1) move up by one number.
- The frame counts (What this is, Counts) change: M goes from 57 to 58 and WORDING from 4 to 5.

**2. Bookkeeping in W35.1's REASON, if W35.5 is entered.** Once W35.5 is applied, W35.1's REASON sentence "Derivations 4 and 10 are unchanged and stay true word for word." is no longer true of Derivation 4's proof. This is not a FIX of X04's claim-bearing fields; it keeps the entry's own account accurate. Words ready to paste:
- OLD (inside W35.1's REASON): `Derivations 4 and 10 are unchanged and stay true word for word. Derivation 4 reads "A system can be surprised only if it holds a transport selected on a history H …" and its proof reads "Surprise is defined as a violation at (a,b)∉H".`
- NEW: `Derivation 4's Claim and Derivation 10 are unchanged and stay true word for word. Derivation 4 reads "A system can be surprised only if it holds a transport selected on a history H …". Its proof read "Surprise is defined as a violation at (a,b)∉H", which reports the old third bullet; after the S93 cross-examination the companion entry W35.5 brings it to the new one.`

**3. The search for other stale reports.** Every sentence of draft 4 that uses "violation", "expectation" or "surprise" was read: L177, L215–225, L576, L580–584 and L624. L582 is the only one that reports the words of the old third bullet. Two others were checked:
- L223's unchanged "A system with no transport cannot be surprised" and "Surprise requires an incomplete selection history" stay true.
- L624 ("This is surprise (Derivation 4)") is about \(t_0\), which is selected on \(H_0\).

**4. Not ruled here.** Mimo's point 1 (the "actually occurring" scoping) and Atria's point 6 are on X05 and belong to X05's checker. Nothing in this ruling bears on them.

X04: KEEP
