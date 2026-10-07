# Ruling: R01 (W37.1), contested in s90_xexam_atria_A1, point 1

*Written on 24 September 2026 by a fresh Claude checker, under the S90 rule as extended by the S90 parts rule (rule 3) and the rerun note (item 4: the pass-2 reply stands where the pass-1 reply would have stood). I did not draft, assemble or check the change list, and I did not write the part briefs. I read one reply, `s90_xexam_atria_A1.response.txt` (pass 2, attempt 5). I opened no reasoning file, and I did not open the rejected attempt files `pass2.a3.*` and `pass2.a4.*`. I did not open the other model's reply to part A1. To reconcile, as the task asks, I read batch 1's ruling on R01 and its ruling file `S90 reading rulings/ruling s90_xexam_mimo_A1 R01.md`, and batch 2's list entry for R01.*

*The name of this file is shortened. The name the task gives, with the whole call description in it, is 427 bytes, and the filesystem's limit is 255.*

**The call is accepted.** The receipt shows pass 2, finish "stop", 0 bad chunks. The response's sha256 is 3a6d34137f789e7d…, which matches the receipt. The last line is END OF REPORT, and the reply is 1,103 words by `wc -w`.

**Why R01 is contested.** The reply's closing line is `R01: FALLS — "blind" adds a claim stated nowhere in Part IV or Part XII, so an ORDER change changes one.` Under parts rule 2, FALLS makes the change contested.

## 1. The entry

- **Id.** R01 = R2-01 = W37.1, "Restore 'blind' in Part 0's account of selection". Group A, item W37. File-11 L15, revised-text L13 (Part 0, "What this document claims", paragraph 2, sentence 3).
- **REASON WORD.** erratum. **KIND.** ORDER.
- **DECLARATION.** "none (ORDER, after check 1; listed in the record). If a checker rules CLAIM: 'Part 0 again calls selection blind, and says what that means: the selection history holds no represented target, as Part IV states.'"
- **OLD** (verified at f11 L15, exactly one occurrence):
  ````text
  A correspondence can be *selected*, produced by variation and survival on a history of encountered changes;
  ````
- **NEW** (verified at revised L13):
  ````text
  A correspondence can be *selected*, produced by blind variation and survival on a history of encountered changes, with no represented target in that history;
  ````
- **CHECK (the checkers' verdict).** "check 1, FIX (kind only). The added words copy what L197 and L203 already state, so the change is ORDER, as 03 ruled the same place (M2, upheld). Declaring it would put a false line in the note." The list's table of what the checks changed has "W37.1 | 15 | 1 | expected ruling CLAIM → ORDER; no declaration". The drafter's REASON records that in S81, 03 ruled the drop of "blind" (M2) WORDING as a borderline call, that all four readers ruled it CLAIM, and that "under the strict rule this entry is CLAIM". In 03's table, M2 reads "WORDING (borderline) | A, B, Atria, Mimo | … | The body (f10 L210, L216, L416 = f11 L197, L203, L403) states 'blind' as no represented target, in both files | UPHELD".
- **CASES AT RISK.** O11 holds AGREE, if anything moving toward. N9 holds. N11 is watched, with no mark moved. Part A1 gave all three.

**Rulings already made on this entry.**
- **Batch 1** (`S90 Reading of the replies - batch 1 (Mimo A1, Mimo A2, Atria B1).md`, section "R01 (W37.1), point 3", and list edit 1) ruled **FIX** on Mimo A1's point 3. It deleted "blind", left OLD unchanged, and kept KIND ORDER and DECLARATION none. It changed the fallback line to "Part 0 now says that a selection history holds no represented target, as Part IV states." It changed the REASON WORD from erratum to clarification. It dropped "in the same word as file 10" from GAIN, added the loss of file 10's word to LOSS, and made the title change optional. Its ruling file has md5 7eb829599cde0a94543c750394d23e00.
- **Batch 2** (item 1) repeats batch 1's ruling on R01 ("As batch 1, item 1") and adds no new reading.

## 2. The reply's argument (point 1, task (b))

> "The added clause "with no represented target in that history" (line 13) is genuine ORDER: Part IV's **Selected** says "No member of the history represents \(t\), \(H\), or the survival condition," and Part X says "A selected transport has no represented target in its history; a constructed one does." But the same new wording also inserts the word **"blind"** ("produced by *blind* variation and survival"), and that word is stated nowhere in the body. Part IV defines selection with only "a population \(\mathcal T\) of candidate transports, a variation operator \(\mu\) on \(\mathcal T\), a finite history \(H\subseteq C\) … and a survival condition requiring fidelity on \(H\)"; Part XII repeats "a physically admitted variation operator." Neither imposes blindness. So a correspondence produced by *directed* variation counts as selected under Part IV but not under the Part 0 gloss, which is a claim the current text did not make. It also breaks the front matter's own rule that "the front matter states nothing the body does not state more exactly" (Part 0, "Grievances, anticipated"). No situation moves over it — O11, N9 and N11 turn on the no-represented-target condition the body already states — but the declared kind ORDER requires the added wording to state only what is stated elsewhere, and "blind" does not. Repair: delete "blind," or add blindness to Part IV's definition of **Selected**."

**How it differs from Mimo's point 3, the ground of batch 1.** Mimo made its point conditional on a strict reading of "blind", leaned to the loose reading, and gave the line STANDS. Atria says FALLS without condition. It adds a ground that Mimo did not give: Part 0's own rule at L35. And it offers a second repair: write blindness into Part IV.

**The quotations, checked under rule 8.** Every quotation is verbatim:
- "No member of the history represents \(t\), \(H\), or the survival condition" is at revised L195 (f11 L197).
- "A selected transport has no represented target in its history; a constructed one does." is at revised L405 (f11 L403).
- The Part IV definition, with the ellipsis, is at revised L195.
- "a physically admitted variation operator" is at revised L475 (f11 L473).
- "the front matter states nothing the body does not state more exactly" is at revised L35 (f11 L37), under the heading "Grievances, anticipated" (L33).
- "blind variation" and "with no represented target in that history" are at L13.

The claim that "blind" is not in the body also holds. In the revised text the word occurs once, at L13, and it never occurs in file 11. Neither text has "directed", "undirected" or "random" about variation. The only "directed" is in L473's "directed preorder", which is not about variation.

## 3. Reading

**The body.** Part IV's Selected (L195), L201 ("a selected transport has no represented target and no criticism in its history"), Part X (L405), Part XII (L475) and the lines on contract provenance (L155) all constrain the **history**: nothing in it represents \(t\), \(H\) or the survival condition, and it holds no criticism. They set no condition on how \(\mu\) produces variants beyond its being a physically admitted operator on \(\mathcal T\). Atria's reading is right.

**A refinement of the reply's example.** Variation that is "directed" by a represented target is already excluded by Part IV, so on that sense of the word no difference arises. The difference is real only for variation steered by something that represents nothing, such as an environmental cue, a gradient, or a mechanism that biases variation towards what tends to survive. Part IV admits such a history as selection. Part 0 with "blind" in its ordinary strict sense does not. That is the undeclared narrowing that both replies name, the one ruler R1 raised in S81 ("might also exclude variation steered without any representation, such as by a gradient").

**The clause does not settle the sense of "blind".** "With no represented target in that history" attaches to "a history of encountered changes". It is a condition on the history, not a gloss on the adjective, so it cannot pin "blind" to the body's sense. The drafter's REASON meant it to do that ("pin 'blind' to the body's sense"), but the syntax does not carry it. So L35's rule is broken on the strict reading, as the reply says: the front matter would state something the body does not state at all.

**Is this consistent with S81's M2?** Yes. M2 ruled that file 11's *drop* of "blind" was WORDING, because the body states blindness only as "no represented target". If the drop lost no claim, then leaving the word out of file 13 loses none either. M2 does not require the word to come back. Restoring it is ORDER only on the loose reading, and M2 itself was a named borderline call on which four of four readers said CLAIM. Deletion is safe under both readings. Restoration is safe under one.

**The cases.**
- **O11, the apprentice.** "Monday is blind fitting": she tries keys from the ring, with no cue and no represented target, so this is selection on either reading. On Wednesday she picks by a represented content ("it looks like Tuesday's"), so she is outside selection on either reading, and "neither" holds. O11 was AGREE under file 11, which has no "blind". The verdict's own word "blind" is the case's, not the theory's, so deleting the word from Part 0 cannot move O11 away.
- **N9, dark moths.** Inherited variation, a survival condition enacted by birds, and "No moth has any idea of the colour of the bark … nobody planned the change". This is selection on either reading, and the verdict ("put there by selection") holds.
- **N11, Jana and Kasia.** The teacher's choice among Jana's drafts is not selection in the theory's sense, because the chooser represents what she wants. The clause does that work, and "blind" adds nothing. On a strict reading, Jana's own purposeful drafting might not be "blind", but the verdict does not turn on that ("Every sentence in each final essay was written by the student"). It holds either way.
- **D3-T, candidate O76, not given and not agreed.** An automatic tester keeps the controller that passes, out of two designs. The verdict (No) turns on the population, because only one design passes (Derivation 3, "what \(H\) leaves open about \(t\) is what \(\mathcal T\) leaves open"). It does not turn on how the designs came to exist. It holds either way.
- **No case in either book, and no fixed verdict, turns on the blindness of \(\mu\).** The only S81 case text with the word is O11's verdict.

**The reply's second repair is refused.** Writing blindness into Part IV's Selected would be a CLAIM change to the body. It would narrow selection by a new condition on \(\mu\), and that condition needs a definition the text lacks: blind to what, and undirected by what? It would also need its own entry, declaration and cases, none of which this cross-examination examined. W37's aim is a clarification of Part 0, and the body's sense is already "no represented target".

## 4. Ruling: FIX (reconciled with batch 1, same text)

Atria's point 1 succeeds, and its first repair is the one batch 1 adopted on Mimo's point 3. The two readings agree, so the ruling is the same. It now rests on two independent replies, one of which says FALLS outright, and on the further ground of Part 0's L35 rule. Nothing in batch 1's ruling needs changing, apart from naming both calls in the record.

- **OLD:** unchanged.
- **NEW (exact, identical to batch 1):**
  ````text
  A correspondence can be *selected*, produced by variation and survival on a history of encountered changes, with no represented target in that history;
  ````
- **KIND:** ORDER, unchanged. Every word NEW adds is stated at L195, L201 and L405 (f11 L197, L203, L403).
- **DECLARATION:** none, unchanged. The fallback line, as in batch 1: "If a checker rules CLAIM: 'Part 0 now says that a selection history holds no represented target, as Part IV states.'"
- **REASON WORD:** erratum → clarification, as in batch 1.
- **REASON, the sentence to record (it replaces batch 1's so that it names both calls):**
  - After the cross-examination (Mimo, part A1, point 3; Atria, part A1, pass 2, point 1), "blind" is deleted.
  - Its ordinary strict sense, variation not directed in any way (for example by a cue or a gradient that represents nothing), says more than Parts I–XVI state (S81 03 M2, R1's close call). That breaks Part 0's rule that "the front matter states nothing the body does not state more exactly".
  - The clause alone states the body's sense.
  - Atria's alternative, adding blindness to Part IV's Selected, is refused as an undeclared CLAIM change to the body.
- **CHECK:** add "S90: FIX (Mimo A1 point 3, batch 1; Atria A1 point 1, reconciled, same text)".
- **GAIN, LOSS and title:** as batch 1.
  - GAIN: drop "in the same word as file 10".
  - LOSS: add that Part 0 no longer uses file 10's word.
  - Title (optional): "W37.1 — Part 0's account of selection: no represented target in the history".
- **By program:** the note's row R2-01 takes the reason "clarification". The counts (N = 48 of M = 55; CLAIM 48, WORDING 5, ORDER 2) are unchanged.
- **The "What the checks changed" row for W37.1** names both calls.

**Conflicts.** None new.
- W38.1's pointer "(Parts 0 and IV)" still lands. Batch 1's optional tidy of W38.1's "Here selection is blind: …" is still optional. It would also keep the strict sense out of the sources note.
- W17.1 (R11) keeps "No member of the history represents …" byte for byte and is untouched.
