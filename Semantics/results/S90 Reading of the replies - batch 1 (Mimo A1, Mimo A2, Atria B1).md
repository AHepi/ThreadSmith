# S90: reading of the replies, batch 1 (Mimo A1, Mimo A2, Atria B1)

*Written on 23 September 2026 by a Claude subagent for the orchestrator, from 23:20 UTC. It records the rulings of fresh Claude checkers on the changes that these three replies contest. The recorder wrote no ruling and did not draft, assemble or check the change list. It read the three replies named here and their receipts, and no other S90 return. It opened no reasoning file. The change list was not edited. Its edits are listed at the end, to be made in one pass together with the later batches. Nothing was written into `authority/`.*

## The rule followed

- The rule is `results/S90 How the cross-examination of the revision 2 draft will be read - written before sending.md`, as extended by `results/S90 Parts - how they will be read, written before sending.md`.
- **Each reply is read on its own** (Parts rule 1).
- **What counts as contested** (Parts rule 2). A change is contested when the reply says it FALLS, or when the reply names an undeclared change of claim or a moved verdict on it. This holds whatever closing line the reply gives the change.
- **Who rules** (Parts rule 3). Each contested change went to a fresh Claude checker. The checker stated the entry and its checkers' verdict, then the reply's argument, then ruled keep, fix (with exact new wording) or drop.
- **How edits are recorded** (Parts rule 4). Edits are recorded as made after the cross-examination.
- **A failed call supports nothing** (Parts rule 5). All three calls here were accepted.
- **Ids.** R01–R55 map to entry ids through the table in the Parts note.
- **Sources**, the same for every ruling:
  - the change list `tests/Revision 2 - change list, draft of 23 September.md` as of 587eebf (md5 a5c92adc9f1e3806c0f9c6394cffde1e, unchanged at HEAD);
  - the revised text `tests/Revision 2 - file 13 draft 2, theory text, as sent for cross-examination.md` (md5 9aecf2f30ce0b4523606b2b8409fdf37);
  - file 11, `authority/11 … revision 1.md` (md5 5e494c1095d920d128b9a79de378f923).
- **The rulings** are copied byte for byte into `results/S90 reading rulings/`, one file per ruling. Each file's md5 is given below. One ruling has no file (R51, task (d)); see that entry.

## Summary

| call | accepted | OVERALL line | closing lines | contested, and why | rulings |
|---|---|---|---|---|---|
| s90_xexam_mimo_A1 (part A1) | yes | OVERALL: NEEDS REPAIR | R08 FALLS; R01, R15, R17 STANDS | R08 (FALLS); R15 (a moved verdict on O45, on one reading); R01 (an undeclared change of claim, on one reading) | R08 FIX; R15 FIX; R01 FIX |
| s90_xexam_mimo_A2 (part A2) | yes | OVERALL: NEEDS REPAIR | R28 FALLS; R26, R27, R29, R41, R43, R51, R54, R55 STANDS | R28 (FALLS); R51 (an undeclared change of claim, task (a)); R51 (moved verdicts on O24, O46, N17 and N25, task (d)); R26 (an undeclared change of claim, on one reading) | R28 FIX; R51 KEEP; R51 KEEP; R26 FIX |
| s90_xexam_atria_B1 (part B1) | yes | OVERALL: NEEDS REPAIR | R39 FALLS; R02, R03, R04, R10, R18, R38, R44, R45, R46, R47, R48, R49, R50, R53 STANDS | R39 (FALLS) | R39 FIX |

**Totals.** There are eight rulings on seven entries: KEEP 2 (both on R51), FIX 6, DROP 0.

**The six FIX rulings:**
- Five change NEW: R08, R15, R01, R28 and R26.
- R15 and R28 also change the DECLARATION.
- R01 also changes the REASON WORD and the fallback declaration line.
- R39 changes only KIND and DECLARATION. Its OLD and NEW stay byte for byte.

**Changes a reply says FALLS, not upheld as argued.**
- **R08:** the move to Part V the reply proposes is refused. The defect is repaired in place instead.
- **R28:** the reply's fifth part for every criticism is refused. The defect is repaired by tying \(\mathcal E_c\) to the connection the criticism already lists.
- **R39:** upheld on KIND. The reply's two repairs are refused: "fold into R38", and "R38's declaration", which does not fit R39's NEW.

## Mimo, part A1 (s90_xexam_mimo_A1)

**The call is accepted.**
- The receipt shows one attempt, status 200, finish "stop", accepted true.
- The response's sha256, bc4c7014…, matches the receipt.
- The last line is END OF REPORT.
- The reply is 1,098 words by `wc -w`.

**Closing lines:**
- `R01: STANDS`
- `R08: FALLS — seven terms used before defined in Part II; the cross-organization kind definition cannot be read at line 119`
- `R15: STANDS`
- `R17: STANDS`
- `OVERALL: NEEDS REPAIR`

**Not contested.** Point 4, on R17 (task (c)), finds that the letter \(G\) of R17's block \(G\subseteq\Gamma\) is also the equation tag (G) of Part X and the variable \(G\subseteq K\times F\) of Part XI. It proposes a new symbol. The reply's line is STANDS. It names no undeclared change of claim and no moved verdict, so under Parts rule 2 the point is noted and not ruled. It is passed to the orchestrator as a notation point.

### R08 (W19.1), point 1: FIX

- **Why contested.** The reply says FALLS (task (c)).
- **The entry.** W19.1, "The sentence after (K): kinds across two candidates". Part II, file-11 L121, revised L119. KIND CLAIM. REASON WORD clarification.
  - The two sentences are the settled S88 wording (F1, block 2), copied byte for byte.
  - CHECK: the entry was checked by its drafter only, and has no FIX or SOUND history.
  - The drafter had already recorded this very defect and left it for this cross-examination.
- **The reply.** The two new sentences at L119 use \(E\), \(E'\), \(\tau\), \(\tau'\), \(\lambda\), "hidden ports projected away" and "the port translation". None of these is defined before Parts IV and V, and unlike Part II's forward reference to \(C\) they carry no inline type. The reply grants that the content is accurate and calls the defect one of placement. Its repair: move the sentences to Part V after \(t=(\pi,\tau,\sigma,\lambda)\) is defined, or gloss the terms inline.
- **The checker.** The premise is true. L119 is the only line in Parts 0–III that uses this notation, and it has no pointer, unlike every other forward use there. The content is sound.
  - **The move is refused**, for three reasons:
    1. The place right after \(t\) is defined is where W20.1 (R15) inserts its sentence, so the two OLDs would overlap.
    2. The move would take the cross-candidate definition away from (K) and from the reserved anchor.
    3. It would leave "Kinds are edit-signatures" without the sense of "one kind" that Derivation 2 uses.
  - **The fix** inserts one typing sentence, in Part IV's and Part V's own words, before the two settled sentences. The settled sentences stay byte for byte, and NEW grows from 84 to 131 words.
- **OLD:** unchanged, `A kind is an equivalence class of components under this relation.`
- **NEW (exact):**

````text
A kind is an equivalence class of components under this relation. For two explanatory candidates (Part V), let \(E\) and \(E'\) be their organizations and \(t=(\pi,\tau,\sigma,\lambda)\) and \(t'=(\pi',\tau',\sigma',\lambda')\) their transports from \(D\), where \(\tau\) translates edits, \(\sigma\) translates boundaries, and \(\lambda\) assigns each component of \(E\) a subnetwork of \(D\), its anchor, with a port translation (Part IV). A component of \(E\) and a component of \(E'\) are of one kind on \(C\) when their signatures, read on \(C\) through \(\tau\) and \(\tau'\), coincide under a footprint bijection; Derivation 2 uses kinds in this sense. Derivation 1 makes the like comparison between a component \(k\) of \(E\), read on \(C\) through \(\tau\), and its anchor \(\lambda(k)\), read on \(C\) directly with its hidden ports projected away, up to the port translation.
````

- **KIND:** CLAIM, unchanged.
- **DECLARATION:** unchanged. The added sentence restates definitions from Parts IV and V and makes no claim.
- **Cases.** The reply names none. O9, O10 and O22 compare components within one organization and hold. N25's second question is exactly as before.
- **Conflicts:** none.
  - W30.1 shares L121, but its OLD is disjoint from W19.1's. The paragraph order becomes:
    1. the definition;
    2. the class;
    3. the typing sentence;
    4. the two settled sentences;
    5. "Kinds are therefore relative to the contract …";
    6. W30.1's sentences.
  - W20.1 is not touched.
- **Ruling file:** `ruling s90_xexam_mimo_A1 R08.md` (md5 96500cef6c7087b60c4770f1ea14d008).

### R15 (W20.1), point 2: FIX

- **Why contested.** The reply's line is STANDS (tasks (a) and (c)). Its point 2 names a moved verdict on O45, conditional on one reading of the new phrase.
- **The entry.** W20.1, "Γ typed: the components the candidate offers as doing the work; the rest is named background". Part V, file-11 L233, revised L231. KIND CLAIM. REASON WORD clarification.
  - The wording is the settled S88 wording (F3, block 2).
  - CHECK: the entry was checked by its drafter only.
  - Its CASES AT RISK reads "O45: watched, with a risk away", and asks X1 to test the row.
- **The reply.** "Those the candidate offers as doing the work" has two readings:
  - (i) the components the candidate identifies as part of the mechanism, whether or not their work has been described;
  - (ii) the components it explicitly describes as contributing.

  On (ii), O45's second spring ("never described as doing anything until the first is deleted") falls outside Γ, and the verdict moves away from "in the account from the start". The reply says Part VI (L307, L299) settles the phrase toward (i), but R15 and its declaration do not. Its repair: "those the candidate identifies as active, whether or not their work has been described".
- **The checker.** The reply is right that the phrase is ambiguous. It does not show that the verdict moves once the whole text is read, and it grants this itself.
  - Read in place, reading (ii) is natural. It is the reading that split file 10 on O45 (S87 P3).
  - The Part VI lines the reply relies on speak of routes and supports, which are already inside Γ. They reach an undescribed component only by inference (the 04c residual).
  - The fix therefore closes the gap in the definition itself.
  - The reply's "identifies as active" is declined. "Active" is undefined and was declined when S88 was settled, and it would make Γ circular.
  - Only the reply's second half is taken, in the words of L307 s3 (file-11 L309 s3).
- **OLD:** unchanged, `and an identified set \(\Gamma\) of active commitments in \(E\).`
- **NEW (exact):**

````text
and an identified set \(\Gamma\) of active commitments in \(E\). The commitments \(\Gamma\) are components of \(E\), those the candidate offers as doing the work, whether or not anyone has described their work; the boundary values of \(E\) and the components of \(E\) outside \(\Gamma\), including any that assigns an input, belong to the named background of Part VI.
````

- **KIND:** CLAIM, unchanged. **REASON WORD:** clarification, unchanged.
- **DECLARATION (exact):**

````text
Part V now types a candidate's commitments: they are components of its organization, those the candidate offers as doing the work, whether or not anyone has described their work, and the organization's boundary values and its other components, including any that assigns an input, belong to the named background of Part VI.
````

- **Cases.**
  - O45 moves from "watched, with a risk away" to "holds AGREE, on firmer text".
  - N1, O2, O7, O36, O46, O47, Part VII's production case, the skew-symmetric case and the S89 N-cases are unaffected.
  - The entry's LOSS stands.
- **Conflicts:** none. W28.1, W3.5, W58(i).1, W20.2, W20.3 and L2-05 agree with the new clause, which adds no term and no symbol.
  - If another reply's checker rules on R15 with other wording at L231, the two rulings must be reconciled.
- **Ruling file:** `ruling s90_xexam_mimo_A1 R15.md` (md5 16f0d68796b43058b528de5caf1c57a1).

### R01 (W37.1), point 3: FIX

- **Why contested.** The reply's line is STANDS (task (b)). Its point 3 names an undeclared change of claim, conditional on a strict reading of "blind".
- **The entry.** W37.1, "Restore 'blind' in Part 0's account of selection". Part 0, file-11 L15, revised L13. KIND ORDER. REASON WORD erratum. DECLARATION none, with a fallback line ready.
  - CHECK: check 1, FIX (kind only), which changed CLAIM to ORDER.
  - The S81 record (03, M2) calls the same word the closest call: all four readers ruled it CLAIM, and ruler R1 raised the gradient case himself.
- **The reply.** R01 is declared ORDER but inserts "blind" before "variation", and the word appears nowhere in Parts I–XVI. Part IV rules out only variation guided by representation or criticism. On a strict reading, "blind" also rules out variation steered by an environmental cue, and then ORDER is wrong. The reply leans to the loose reading and lets the change stand. It proposes deleting "blind".
- **The checker.** The point is sound.
  - Parts IV, X and XII (L195, L201, L405, L475) constrain only the history: it has no represented target and no criticism. They set no condition on how variation is produced.
  - The clause "with no represented target in that history" attaches to the history, so it does not fix the sense of "blind".
  - On the strict sense, Part 0 would state a narrower class than Part IV, and ORDER fails.
  - The clause alone gives the gain the entry wants. O11, N9 and N11 hold on either reading. O11 was AGREE under file 11, which has no "blind".
  - Declaring CLAIM would not help: the prepared line says the content is only Part IV's. Dropping the entry would lose the clarification.
  - So the fix deletes the one word.
- **OLD:** unchanged.
- **NEW (exact):**

````text
A correspondence can be *selected*, produced by variation and survival on a history of encountered changes, with no represented target in that history;
````

- **KIND:** ORDER, unchanged.
- **DECLARATION:** none, unchanged. The fallback line, for use if a checker rules CLAIM, becomes: "Part 0 now says that a selection history holds no represented target, as Part IV states."
- **REASON WORD:** erratum → clarification.
- **Title (optional):** "W37.1 — Part 0's account of selection: no represented target in the history". The id is kept.
- **What is lost:**
  - Part 0 no longer uses file 10's word.
  - The GAIN's "in the same word as file 10" goes.
  - Nothing is lost in the theory's claims.
- **Conflicts:** none.
  - W38.1's pointer "(Parts 0 and IV)" still lands.
  - W17.1 is untouched.
  - The note's row R2-01 changes its reason column by program. The counts are unchanged.
- **Ruling file:** `ruling s90_xexam_mimo_A1 R01.md` (md5 7eb829599cde0a94543c750394d23e00).

## Mimo, part A2 (s90_xexam_mimo_A2)

**The call is accepted.**
- The receipt shows one attempt, status 200, finish "stop", accepted true.
- The response's sha256, 6dde4faf…, matches the receipt. Its md5 is 4ba1fdf27d0d4e2e0a3060707ddae40f, as the R28 ruling records.
- The last line is END OF REPORT.
- The reply is 946 words by `wc -w`.

**Closing lines:**
- `R26: STANDS`
- `R27: STANDS`
- `R28: FALLS — \(\mathcal E_c\) relies on an undefined "offers" relation; declaration's "defines its terms" is inaccurate`
- `R29: STANDS`
- `R41: STANDS`
- `R43: STANDS`
- `R51: STANDS`
- `R54: STANDS`
- `R55: STANDS`
- `OVERALL: NEEDS REPAIR`

**Not contested.** Point 2, on R55 read with R51 (task (c)), finds that L624 cites Derivation 2 without exhibiting the bijection that meets the premise of 2(ii). It grants that the cross-pairing meets the premise and that "the conclusion is true", and it proposes an inserted clause. The reply's line is STANDS. It names no undeclared change of claim and no moved verdict, so under Parts rule 2 the point is noted and not ruled. The R51 checker read it and left it to R55's own checker. If a later reply contests R55, this point goes to that checker. Otherwise it is passed to the orchestrator.

### R28 (W22.1), point 1: FIX

- **Why contested.** The reply says FALLS (task (c)).
- **The entry.** W22.1, "Define \(p_\delta\) and \(\mathcal E_c\) in (K1)". Part IX, "Bearing", file-11 L373, revised L371. KIND CLAIM. REASON WORD erratum.
  - CHECK: check 1, FIX. Check 1 changed file 00's "account" to "the explanatory candidate (Part V) that the criticism offers for \(p_\delta\)".
- **The reply.** At L371, \(\mathcal E_c\) is "the explanatory candidate (Part V) that the criticism offers for \(p_\delta\)". The criticism just defined has only a target \(z\), a defect \(\delta\), grounds \(g\) and a connection, and "offers" is defined nowhere as a relation from a criticism to a Part V structure. So:
  - \(\mathcal E_c\) has no fixed referent;
  - (K1) cannot be evaluated;
  - Bearing is not well defined.

  The reply adds that R29 makes this worse. It says the declaration's "defines its terms" over-claims, while granting that R28 improves on the old text. Its repair makes \(\mathcal E_c\) a fifth part of the criticism.
- **The checker.** The argument is too strong on "offers". Part V's own definition uses the verb (L231), and so do L69, L127 and L335. (EK) at L443 also reads a content directly as a candidate.
  - **It is right on two points.** The clause does not say which of the criticism's four listed parts gives \(\mathcal E_c\), and "defines" over-claims.
  - **The fix** ties \(\mathcal E_c\) to the listed connection, as file 00 does at L607 and L620.
  - **On R29.** Every criticism has a connection. A bare connection gives a candidate with no nonempty block \(G\subseteq\Gamma\), so it fails (E) at L255 and the criticism does not bear, which L377 already allows.
  - **The reply's own repair is refused.** It would add a fifth part to every criticism, and it would use \(p\) before \(p\) is bound. It would also conflict with W22.2 (R29), which the same reply says STANDS.
- **OLD:** unchanged, `Let \(p_\delta\) be the question about the defect. Then`
- **NEW (exact):**

````text
Let \(p_\delta\) be the question whether \(z\) has \(\delta\) in respect of \(p\), and \(\mathcal E_c\) the criticism's connection from \(g\) to \(\delta\), interpreted as an explanatory candidate (Part V) for \(p_\delta\). Then
````

- **KIND:** CLAIM, unchanged. **REASON WORD:** erratum, unchanged.
- **DECLARATION (exact):**

````text
(K1) now says what its terms are: \(p_\delta\) is the question whether the target has the alleged defect in respect of \(p\), and \(\mathcal E_c\) is the criticism's connection from its grounds to the alleged defect, interpreted as an explanatory candidate for that question.
````

- **Cases.** N11, O27, O40 and O50 hold. None turns on how \(\mathcal E_c\) is typed.
- **What is lost:** the verb "offers" in this clause, and nothing else.
- **Conflicts:** none.
  - W22.2 (R29) now agrees with this sentence.
  - W36.1 is untouched.
  - No other entry has an OLD in L373 sentence 1 or in (K1).
- **Ruling file:** `ruling s90_xexam_mimo_A2 R28.md` (md5 c36fa775835af83ea5c7c98302905112).

### R51 (W19.2), point 3, task (a): KEEP

- **Why contested.** The reply's line is STANDS. Its point 3 names an undeclared change of claim.
- **The entry.** W19.2, "Derivation 2: 'Same anchors, one account'". Part XVI, file-11 L552–558, revised L554–562. KIND CLAIM. REASON WORD change of claim.
  - The wording is the settled S88 wording (F1, block 1).
  - CHECK: "as W19.1", so it was checked by its drafter only.
- **The reply.** The declaration says "without that premise nothing more follows", but L560 adds that candidates that anchor different subnetworks, or cut \(D\) at different places, "are different candidates with one answer profile". The new Consequence also narrows the old general principle (a claim that two such candidates "really" differ must supply an admitted change) to candidates that "differ only in which component carries which anchor". The reply says the declaration understates both the added claim and the lost principle.
- **The checker.** Both halves fail.
  1. **The "added claim" is not new.** File 11's Claim already spoke of "Two candidates". "One answer profile" is clause (i), which the declaration states. The paragraph's pointers are to unchanged text: L23, L307, and Derivations 8 and 9.
  2. **The narrowing is declared.** The declaration's last sentence says so ("Its Consequence now covers only candidates that differ in which component carries which anchor"), and so does LOSS. The reply never engaged that sentence.

  The quotations are all found, but the line numbers are off: the paragraph is at L560 and the Consequence at L562.
- **Cases.** O24, O46 and N17 hold AGREE or move toward, through the declared withdrawal of "one account". N25's second question still rests on unchanged text (Part 0 L39; (K) with W30.1 at L119), so the away move the drafters watched for does not happen.
- **Text:** none changes. OLD, NEW, KIND and DECLARATION stay as drafted.
- **To record** in W19.2's CHECK field (the checker's suggested line, exact):

````text
After the cross-examination (S90, Mimo A2, point 3, R51 STANDS): the reply's claim that the declaration understates an added claim ('different candidates with one answer profile') and the loss of the old Consequence's general principle was re-examined and ruled KEEP. 'Different candidates' is file 11's own premise, 'one answer profile' is (i), the paragraph's pointers restate unchanged L23, L307 and Derivations 8–9, and the narrowing of the Consequence is stated in the declaration's last sentence and in LOSS.
````

- **Not ruled, and outside the argument.** The declaration could echo the text's "differ only in". The one-word change would be "Its Consequence now covers only candidates that differ in nothing but which component carries which anchor". The declaration is true as written. This is the orchestrator's option.
- **Conflicts:** none. R55's use of Derivation 2(ii) is left to its own checker.
- **Ruling file:** `ruling s90_xexam_mimo_A2 R51.md` (md5 a586279ae712f1ae74022bfffb82f688).

### R51 (W19.2), task (d): KEEP

- **Why contested.** The reply's line is STANDS. Its task (d) paragraph names moved verdicts on O24, O46, N17 and N25. It says they move toward the fixed verdicts, and that the omitted "different candidates" characterization is what carries them.
- **No ruling file.** This ruling has no file of its own in the scratch folder. Both R51 checkers were given the same file name, and the one file there is the task (a) ruling. That file says it read point 3 and the task (d) paragraph, but it rules on point 3.
  - The task (d) ruling is recorded here from the orchestrator's summary of it, quoted as passed. The summary is cut off at its end.
  - The summary gives the ruling as KEEP, with no text change. It also says that "the exact text" of the CHECK-field note "is in the ruling file", and that file is not in hand.
  - **Before the pass**, the orchestrator either recovers that line or has it written again from the summary below.

  The summary, as passed:

> R51 (W19.2): KEEP. OLD, NEW, KIND and DECLARATION stay as drafted; no text changes.
>
> - **The reply's premise holds.** It names O24, O46, N17 and N25. None of them moves away, and the entry's CASES AT RISK already records O24 ("toward if anything"), O46 ("firmer text") and N17 ("toward on Q1–2", naming the added paragraph) in the reply's direction.
> - **The reply's conclusion fails.** The omitted phrase "different candidates with one answer profile" makes no claim of its own:
>   - "Different candidates" is true by definition, since a candidate includes its transport, λ and all (Part V).
>   - "One answer profile" is clause (i), which the declaration already states.
>   - "Nothing more follows" is also already in the declaration, in the same words.
> - **The verdicts rest on text W19.2 leaves unchanged,** which its added paragraph cites: file 11 L25, Part VI's redundant routes (L309 s3), Derivation 9, and Derivation 3 for O24. W19.2 only removes the slogan that pulled against them, and the declaration's first sentence says so.
> - **O24 cannot rest on the phrase at all.** On any contract containing the reachable setting, the two arrangements answer differently, so they do not share an answer profile.
> - **N25 Q2 holds on either reading.** The entry's "watched" stays, and the reply's "toward" reading should be recorded beside it.
>
> To record: append a KEEP note to W19.2's CHECK; the exact text is in the ruling file.
>
> Conflicts: none. Point 3 (task a) is a separate contested claim on this en[…]

- **The two R51 rulings agree.** Both are KEEP, and neither changes any text.

### R26 (W24.1), point 4: FIX (wording only)

- **Why contested.** The reply's line is STANDS (task (b)). Its point 4 names an undeclared change of claim, conditional on one reading.
- **The entry.** W24.1, "Type \(S_a\), \(T_a\) and the generators in functional transport". Part VIII, file-11 L351, revised L349. KIND WORDING. REASON WORD erratum. DECLARATION none, with a fallback line ready.
  - CHECK: check 1, SOUND. There is no FIX history.
- **The reply.** The typing sentence quantifies over "admitted generator \(a\)", and the commuting condition right after it quantifies over "generator \(a\)". If "admitted generator" is the narrower term, \(S_a\) and \(T_a\) are defined for only some of the generators, and the theorem is silently restricted. The reply proposes making the two quantifiers match.
- **The checker.**
  - **The scope-change claim fails.** "Generator" appears nowhere else in the revised text or in file 11. The only generated structure is Part II's set of admitted edits, \(A\) (L91). The source, 00:518–524, says "for every admitted generator". So the two terms are coextensive, and the scope does not change.
  - **The mismatch is real.** W24.1 put two quantifiers, worded differently, in consecutive sentences. That leaves half undone the entry's own job, which is to restore 00:518 and anchor "generator" to \(A\).
  - **Direction.** "Admitted" is added to the condition rather than dropped from the typing sentence. It is 00:518's exact phrase, and it ties the generators to \(A\).
- **OLD:** unchanged, `**Functional transport.** If \(\pi\circ S_a=T_a\circ\pi\) for every generator \(a\),`
- **NEW (exact):**

````text
**Functional transport.** Let \(S_a\) be a target process and \(T_a\) a represented process for each admitted generator \(a\). If \(\pi\circ S_a=T_a\circ\pi\) for every admitted generator \(a\),
````

- **KIND:** WORDING, unchanged. **DECLARATION:** none, unchanged. The CLAIM fallback line is unchanged.
- **REASON, to add:** "The condition carries 00:518's 'admitted generator' as well, so the two quantifiers match (S90, Mimo A2, R26)."
- **What is lost:** nothing.
- **Conflicts:** none.
  - W31.1 (L361) is unaffected.
  - The revision note's "expected WORDING" and its row R2-26 still hold.
  - No case is at risk. N20 is read on (T2).
- **Ruling file:** `ruling s90_xexam_mimo_A2 R26.md` (md5 a071d566df2858d110ab72f904f64b37).

## Atria, part B1 (s90_xexam_atria_B1)

**The call is accepted.**
- The receipt shows three attempts. Attempts 1 and 2 have status 0 and no finish. Attempt 3 has status 200, finish "stop", accepted true.
- The response's sha256, c2c02bda…, matches the receipt.
- The last line is END OF REPORT.
- The reply is 1,404 words by `wc -w`.

**Closing lines:**
- `R39: FALLS — declared WORDING, but it removes the normative relation's description as "declared," the very claim change R38 declares.`
- `R02, R03, R04, R10, R18, R38, R44, R45, R46, R47, R48, R49, R50, R53: STANDS`, one line each.
- `OVERALL: NEEDS REPAIR`

**Not contested.** Points 2–9 test R04, R02, R38, R45, R49, R03, R44, R47, R53, R46, R48, R10, R18 and R50, and find each standing.
- Point 7 names the weakening of R18 and R50, which is declared.
- No point names an undeclared change of claim or a moved verdict on these changes.
- They are not contested, and under S90 rule 5 they are not thereby confirmed.

### R39 (W6.3), point 1: FIX (kind and declaration; OLD and NEW unchanged)

- **Why contested.** The reply says FALLS (task (b)).
- **The entry.** W6.3, "L447 s3: 'declared as' becomes 'taken as'". Part XI, file-11 L447 s3, revised L449. Group B1. KIND WORDING. REASON WORD erratum. DECLARATION none.
  - CHECK: check 1, SOUND.
  - Its KIND AS DRAFTED keeps a fallback CLAIM line ready.
  - Its REASON says it "can be dropped without harm to any other entry".
- **The reply.** "Declared input" is a technical category in the text, and the old s3 put \(\mathcal N\) in it. R38 is declared CLAIM precisely to remove that description from s2, and R39 removes the second occurrence. So R39 is a change of claim declared as WORDING. The reply's repair: re-declare R39 with R38's declaration, or fold R39 into R38.
- **The checker.** The argument holds.
  - "Declared input" is a technical category (file-11 L514, revised L518). The old s3 put \(\mathcal N\) in that category, and the new s3 does not.
  - This is the same loss that R38 declares as CLAIM for s2. One removal cannot be a claim change in s2 and a paraphrase in s3.
  - W6.4's clause gives the same missing-input consequence, but that does not make the category claim the same claim.
  - The REASON's "can be dropped without harm" is false. Without W6.3, W6.2's declaration would be false of Part XI.
  - **"Fold into R38" is refused.** It would renumber R2-39 onward and merge two disjoint OLDs into one.
  - **R38's declaration cannot be reused**: it says "primitive 2", and R39's NEW does not.
  - One quotation carries a wrong line number: "taken as an input and never derived" is at revised L512, not L514. The point stands.
- **OLD:** unchanged, `declared as a substantive input when aesthetic value is claimed.`
- **NEW:** unchanged, `taken as a substantive input when aesthetic value is claimed.`
- **KIND:** WORDING → CLAIM. **REASON WORD:** erratum, unchanged.
- **DECLARATION (exact):**

````text
Part XI no longer calls the aesthetic normative relation a declared input: it is taken as a substantive input when aesthetic value is claimed.
````

- **REASON, last clause, replace** "and it can be dropped without harm to any other entry." **with** the sentence below. The sentence before it then ends "… for the same reason."

````text
It cannot be dropped: without it, s3 would still call \(\mathcal N\) declared one sentence after W6.2, W6.2's declaration would be false of Part XI, and the paragraph would pull against L510 and L514. After the cross-examination (s90_xexam_atria_B1, point 1) it is ruled CLAIM, with the declaration drafted above as its fallback.
````

- **CHECK (exact):**

````text
check 1, SOUND. After the cross-examination (s90_xexam_atria_B1, R39 FALLS): FIX. KIND WORDING → CLAIM, declaration added; OLD and NEW unchanged.
````

- **Cases.** None. The S81 and S89 books contain no aesthetic case, and CASES AT RISK "None" stands.
- **Conflicts:** none.
  - W6.2 (R38): its declaration overlaps this one and agrees with it, and its OLD is disjoint.
  - W6.1, W6.4 + W14.1, W15.1, W7.2 and W7.3 send \(\mathcal N\) to "an input" outside the declared-input category, as this declaration does.
  - The note already has two lines for other file-11 lines, so two lines for L447 are within its form.
- **Loose end, not ruled.** Revised L51 (file-11 L53, which no entry touches) still says of aesthetics "In Part XI, as a declared normative relation." It does not say "declared input", so the declarations stay true. It is the one remaining place that calls \(\mathcal N\) "declared", and it is passed to the orchestrator.
- **Ruling file:** `ruling s90_xexam_atria_B1 R39.md` (md5 71e79d6308a363a77e014f82b206af47).

## Pending edits to the change list

**None of these is made now.** They are to be applied in one pass together with the later batches, to `tests/Revision 2 - change list, draft of 23 September.md`.

- **Reconcile first.** Parts A1, A2 and B1 also go to the other model. If a later reply contests one of these seven entries, its ruling is reconciled with the one here before the pass. The R15 ruling asks for this at L231.
- **Mark every edit.** Each edit is marked in its entry as made after the cross-examination, with the call and point that raised it.
- **After the pass.** The draft is rebuilt by program, and then the following are checked:
  - the counts;
  - the note's N and M;
  - the revision note (generated from the list);
  - the layer-1 record.

1. **W37.1 (R01; Mimo A1, point 3), FIX.**
   - NEW: "blind" deleted, as given above. OLD unchanged.
   - REASON WORD: erratum → clarification.
   - DECLARATION: the fallback line becomes "If a checker rules CLAIM: 'Part 0 now says that a selection history holds no represented target, as Part IV states.'"
   - GAIN: drop "in the same word as file 10".
   - LOSS: add that Part 0 no longer uses file 10's word.
   - REASON: add the record sentence. After the cross-examination (Mimo, part A1, point 3), "blind" is deleted. Its ordinary strict sense (variation not directed in any way, for example by a cue or a gradient) says more than Parts I–XVI state (S81 03 M2, R1's close call), and the clause alone states the body's sense.
   - CHECK: add the ruling.
   - Title (optional): "W37.1 — Part 0's account of selection: no represented target in the history".
   - By program: the note's row R2-01 reason column becomes "clarification". The counts are unchanged.
   - Optional, outside the ruling: W38.1's "Here selection is blind: …" could read "Here selection has no represented target in its history (Parts 0 and IV)".
2. **W19.1 (R08; Mimo A1, point 1), FIX.**
   - NEW: the typing sentence is inserted after sentence 2. OLD, KIND and DECLARATION unchanged.
   - WHERE: "Two sentences are inserted" → "Three sentences are inserted".
   - REASON: the bullets "Notation, read in place" and "Placed at the reserved anchor" record the typing sentence, added after the cross-examination (s90_xexam_mimo_A1, point 1).
   - LOSS → "Part II grows by three sentences, and it uses the notation of Parts IV and V before those Parts, typed inline with pointers to them."
   - CHECK: add the ruling.
   - "Findings carried forward": the item "Part II uses the notation of Parts IV and V before they introduce it" (list L187) is closed by this edit.
3. **W20.1 (R15; Mimo A1, point 2), FIX.**
   - NEW: add ", whether or not anyone has described their work" after "those the candidate offers as doing the work".
   - DECLARATION: as given above.
   - CHECK and REASON: add "settled wording (F3, block 2) with one clause added after the cross-examination (S90, Mimo A1, point 2): 'whether or not anyone has described their work', from L309 s3; the reply's 'identifies as active' is not taken ('active' is undefined)".
   - CASES AT RISK, O45: "watched, with a risk away" → "holds AGREE, on firmer text (W20.1 now states that membership does not wait on a description; L309 s3, W28.1 and W58(i).1 agree)".
   - Follow-on: the drafter's check line "Watched, with a risk away: O45 under W20.1 …" (list L168).
   - Follow-on: the carried-forward finding "O45 against W20.1's …" (list L190).
4. **W24.1 (R26; Mimo A2, point 4), FIX.**
   - NEW: the condition reads "for every admitted generator \(a\)". KIND WORDING and DECLARATION none unchanged.
   - REASON: add "The condition carries 00:518's 'admitted generator' as well, so the two quantifiers match (S90, Mimo A2, R26)."
   - CHECK: add the ruling.
   - The edit lands in the draft at revised L349.
5. **W22.1 (R28; Mimo A2, point 1), FIX.**
   - NEW and DECLARATION: as given above. KIND and REASON WORD unchanged.
   - CHECK and the list of what the checks changed: add "S90, Mimo part A2, R28 FALLS; fresh checker FIX after the cross-examination: \(\mathcal E_c\) is 'the criticism's connection from \(g\) to \(\delta\), interpreted as an explanatory candidate (Part V) for \(p_\delta\)', not the candidate 'the criticism offers'; the declaration says 'says what its terms are', not 'defines its terms'."
   - The check-1 row for W22.1 in "What the checks changed" stays as history.
6. **W6.3 (R39; Atria B1, point 1), FIX.**
   - KIND: WORDING → CLAIM.
   - DECLARATION: as given above.
   - REASON: the last clause is replaced as given above.
   - CHECK: as given above.
   - OLD and NEW unchanged.
   - "Counts": CLAIM 48 → 49 and WORDING 5 → 4; group B1 13 → 14 of 15.
   - By program: the note reads "49 of the 55 changes" and gains a second line for file-11 L447, after W6.2's. W6.3 leaves the note's list "Entries not declared, whose ruling a checker may raise to CLAIM". Record row R2-39 becomes CLAIM, declared.
7. **W19.2 (R51; Mimo A2, point 3 and task (d)), KEEP twice.**
   - No text changes.
   - CHECK: append the task (a) KEEP line given above.
   - CHECK: append the task (d) KEEP line. Its exact text is in the missing ruling file, to be recovered or written again first.
   - CASES AT RISK, N25: record the reply's "toward" reading beside "watched" (task (d) ruling).
   - Optional, not ruled: the declaration's "differ in which component" → "differ in nothing but which component".
8. **"What the checks changed".** Add a part headed as after the cross-examination (S90), with one row for each FIX above: W37.1, W19.1, W20.1, W24.1, W22.1 and W6.3. Give each row's call and point. The Counts bullet "The checks" gains the S90 totals once every batch is read.

**Passed to the orchestrator, not edits.**
- R17's letter \(G\) (Mimo A1, point 4).
- R55's unexhibited bijection (Mimo A2, point 2).
- Revised L51, "as a declared normative relation" (from the R39 ruling).

Dated 23 September 2026.
