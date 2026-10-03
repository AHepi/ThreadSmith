# Ruling: s90_xexam_atria_C, item 2, R06 (W36.1)

*By a fresh Claude checker, 24 September 2026. The checker works under the S90 rule, as extended by "S90 Parts - how they will be read, written before sending.md" (rules 1–3 and 5), and under the rerun note "S90 and S87 - seven calls rerun after the container restart - written before sending.md" (ruling 4: the pass-2 reply stands where the pass-1 reply would have stood). It did not draft, assemble or check the change list, and it did not write the part briefs.*

*File name.* The task asked for "ruling s90_xexam_atria_C (part C, Atria). Pass 2, accepted on attempt 6 of 6: … 1,227 words. item 2 R06.md". That name is 287 bytes, and the filesystem refused it (ENAMETOOLONG; the limit is 255). This file follows the short form of the other Atria rulings in this folder, such as "ruling s90_xexam_atria_B2 item 1 R42.md".

*The call.* The reply is `parts/s90_xexam_atria_C.response.txt`. The file name in the task puts the call description where the tag belongs, and no file of that name exists. This is the only reply of this tag.
- Pass 2 was accepted on attempt 6 of 6. The receipt's attempt history shows attempts 1–5 at status 0 with nothing back (1,802.4, 1,590.3, 497.8, 119.6 and 929.0 s).
- Attempt 6 returned status 200 and finished "stop", with 0 bad chunks and 7,638 characters. END OF REPORT is on the last line.
- The reply's sha256 is bd51b78593b3ac9e7d194d7f0b62e43e223f8c487d6e611a6118999d50d7a72f, which matches the receipt. It is 1,227 words by `wc -w`.
- The receipt's `user_sha256` is a94c8ef9ead3…, the part C brief. Pass 1 ended on the dead proxy with no reply (rerun note §1), and none of it was read.
- No reasoning file was opened.

*Why R06 is here.* The reply's closing line is "R06: STANDS". Its point 3, under (d), names a move of the theory's verdict on N3 that R06 causes. The reply says the move is toward the fixed verdict and is declared. Under S90 Parts rule 2, a change is contested when a reply names a moved verdict on it, "whatever line it gives the change". So R06 goes to a checker.

*Sources:*
- *the change list, md5 a5c92adc9f1e3806c0f9c6394cffde1e (587eebf; no later commit touches it);*
- *the revised text, `tests/Revision 2 - file 13 draft 2, theory text, as sent for cross-examination.md`, md5 9aecf2f30ce0b4523606b2b8409fdf37;*
- *file 11, md5 5e494c1095d920d128b9a79de378f923, read only;*
- *the part C brief, md5 2183faa5005b112347f484b6c8ace196 (its R06 block and tasks (a)–(d));*
- *the S81 book, md5 4f488d149e44669240d5db546c8e946a;*
- *the S89 candidate book, md5 b2e535777976a511935430bd089ba500;*
- *D3-T's `final.md`;*
- *the revision note draft (row R2-06), and the worklist rows for W36, N1, N2 and N3.*

*The S87 rules (05, 05b and 05c) govern S87 rows, not S90 parts, so they are not applied here.*

*Map (part-rule table): "R06 | W36.1 | C06 | C | 71 | 69 | CLAIM | O8, O15, N1, N2, N3, N22".*

## 1. The entry and its checkers' history

W36.1, "Part I: which sense of "explanation" the fallibility commitment uses".
- **Group** C. **Item** W36.
- **Place.** Part I, "Fallibility without falsehood-as-work", file-11 L71, revised L69. One sentence is added after s2. s1 and s2, the commitment, are unchanged.
- **REASON WORD** clarification. **KIND** CLAIM.
- **OLD:** `What cannot count as explanation is an error in the very dependence alleged to do the work.`
- **NEW:** `What cannot count as explanation is an error in the very dependence alleged to do the work. "Explanation" in this commitment means an account, an explanatory candidate satisfying \(\operatorname{Account}\) on its contract (Part V); a false theory offered as an answer is an explanatory candidate, which ordinary usage may still call an explanation, and how hard an account is to vary is a separate matter (Part VI).`
- **DECLARATION:** "Part I now says that "explanation" in its fallibility commitment means an account in Part V's sense, that a false theory offered as an answer is an explanatory candidate which ordinary usage may still call an explanation, and that how hard an account is to vary is a separate matter (Part VI)."
- **CHECK (the checkers' verdict):** "check 2, FIX. "A separate measure" meets L27's "a measure of worth" and B1's "no merit function"; NEW reads "a separate matter". Cases: as drafted, plus N1 watched (the Γ question, as C's C7) and N4 Q2 watched (with W34.1)."
- **CASES AT RISK (drafters' expectation, not sent):**
  - "N3: toward on both questions. "It does not explain … it is an explanation only in form, an attempt, a false one" describes a candidate that fails Account and that ordinary usage calls an explanation."
  - "N2 holds, or moves toward (the patched myth is a candidate that fails)."
  - "N1, N7, N8, N16, N22 and N25 hold."
  - O15 and O8 are watched.
- **Record.** Revision note row R2-06: "W36.1 | C06 | 71 | clarification | CLAIM | yes". Worklist, N3: "W36, W29, W39, W20 | an explanation "only in form"; the answer is written into the bargain".
- **Earlier rulings.**
  - Batch 1 and batch 2 make no ruling on R06, W36.1 or C06. Batch 1's reading of R28 (W22.1) says only "W36.1 is untouched", and the R28 ruling finds W22.1 consistent with L69.
  - Mimo's reply to part C gives "R06: STANDS" and raises no point on R06.
  - The single S90 call (C06) failed and supports nothing.
  - There is nothing to reconcile.

## 2. The reply's argument

The closing line is "R06: STANDS". Point 3 is headed "R06, R21, R24, R25, R30, R34 · (d) — declared moves toward the fixed verdicts; none away." Its R06 bullet:

> "R06 (line 69) on N3: the verdict's pairing — "No, the myth does not explain why winter comes every year" with "Yes, it is an explanation of winter, but only in form" — is R06's candidate/account distinction: the myth is "an explanatory candidate, which ordinary usage may still call an explanation," but not an account, since the yearly return is written into the bargain (non-circular dependence, Part V). The current text's "What cannot count as explanation is an error in the very dependence alleged to do the work" read as denying even the "in form" yes. Same mechanism serves N1 (the sun-god sentence rides along) and N2 (the amended myth is a candidate, not an account, of the southern seasons)."

The reply finds no defect in R06. It names a move toward on N3, which it counts as declared, and says the same mechanism serves N1 and N2.

**Quotations checked (S90 rule 8).**
- "an explanatory candidate, which ordinary usage may still call an explanation" is in NEW, at revised L69, byte for byte.
- "What cannot count as explanation is an error in the very dependence alleged to do the work" is OLD. It stands unchanged at revised L69 and file-11 L71. "(line 69)" is correct.
- "No, the myth does not explain why winter comes every year" and "Yes, it is an explanation of winter, but only in form" are N3's verdict, word for word.
- The reply does not quote "the yearly return is written into the bargain". It paraphrases N3's "The yearly return is simply written into the terms of the bargain." "Rides along" paraphrases N1's "riding along".

All the quotations are found.

## 3. Reading

**N3.** Questions: "Does the myth explain why winter comes every year? Is it an explanation of winter?" Fixed verdict: "No … Yes, … but only in form: it is an attempt at one, and a false one."
- **The current text.** The myth alleges that winter depends on Demeter's grief under the bargain, and that dependence is itself false. So under the old s2 the myth "cannot count as explanation". That gives "No" to the first question. Read literally, it also gives "No" to the second, the "in form" yes. The old text had no other word for what the myth is, apart from Part V's technical "explanatory candidate". The sense of "explanation" was open, and N3's open notes record that all four authors found the two questions using "explain" in two senses without saying which. So a careful reader of the old text disagrees with the verdict on the second question, or is split on it.
- **The revised text.**
  - *First question: No, as before.* The myth is not an account, so it does not explain. It fails (E) twice over:
    - (F1) fails, because Demeter's grief has no anchor in the world whose relation matches it;
    - non-circular dependence fails. Revised L255 says "The target's answer does not appear, at the declared grain, as an unanalysed boundary input or as a component", and L273 says "So does an account whose only substantive component restates the answer it was asked for." The yearly return written into the bargain is such a component.

    So the reply's "(non-circular dependence, Part V)" names a real ground. That ground is file 11's (L257 and L275), strengthened by W39.1 and the W20 entries. It is not R06's.
  - *Second question: Yes, in form.*
    - The myth is an explanatory candidate. By L231 a candidate is an organization, a transport from D to it, and an identified Γ. By L185 a transport is not faithful by definition ("A transport is faithful on C when …"), so a false theory can be a candidate.
    - The new clause says such a candidate is one "which ordinary usage may still call an explanation". That is the verdict's "an explanation … only in form … an attempt at one, and a false one".
- **So the second question moves toward** the fixed verdict, from disagree or split to agree. The first holds agree, or moves toward from split if the two senses are read as the old text leaving both questions open. That is how the entry's "toward on both questions" is meant. Nothing moves away.
- **The move is declared.** It follows from the declaration's first two clauses and needs nothing else:
  - "explanation" in the commitment means an account in Part V's sense;
  - "a false theory offered as an answer is an explanatory candidate which ordinary usage may still call an explanation".

  The drafters predicted it in CASES AT RISK, and the reply reads it the same way. It is not an undeclared change of claim under task (d).

**N1.** Fixed verdict: Tomas explains; the sun-god sentence is not part of what explains; "Strike it out and the account works exactly as before."
- R06 alone moves nothing here. The verdict is carried by unchanged s1 ("A theory may contain an accurate scoped dependence together with errors elsewhere"), by L231's split between Γ and the named background, and by R24's no-work test at L313. The reply's own R24 bullet puts N1 there.
- Whether the god clause sits inside Γ is the Γ question that check 2 marked as watched (W20 and W33.1). R06 neither raises it nor settles it.
- The reply's "same mechanism serves N1" does not claim a move. N1 holds agree, as the entry says.

**N2.** Fixed verdict: "No."
- Old text: the warmth-sent-south dependence is false, so the changed myth cannot count as explanation. That gives "No".
- New text: the changed myth is a candidate and not an account. Its southern part is "the sailor's report retold in the myth's terms", which L273 excludes, and (F1) fails as for N3. That gives "No".
- The new clause also gives a place to the alternative in N2's confidence note, "an explanation, just a false and patched one", as ordinary usage for a candidate.
- N2 holds agree, or moves toward. That is the entry's expectation, and it is declared by the same two clauses.

**Cases given for R06 that the reply does not raise.**
- **O8.** "a good explanation with an honest scope." The new "how hard an account is to vary is a separate matter (Part VI)" does not make "good" wait on Pres. L313 adds that Pres "grades nothing". Petra's candidate is an account on her scoped contract. It holds agree.
- **O15.** "Sam's account of his own work is complete." That is the ordinary "account". The new sentence is scoped "in this commitment". It holds agree.
- **N22.** Yuri's false or incomplete theory is a candidate by the declared clause. That fits "Whether it is good or true is another matter". The question asks whether a reason is given, not whether one is explained. It holds, and R25 (W40.1) carries the verdict.
- **D3-T** (selection and an untried setting) has no false theory and no question about the sense of "explanation". It is not touched.

**Coherence (task (c)). No defect is found.**
- "(Part V)" points to L231 and (E), which say what the sentence says. A forward pointer from Part I is the Part's usual form.
- "(Part VI)" points to revised L313, "How hard an account is to vary is a separate matter, shown by \(\operatorname{Pres}\), and it grades nothing". The wording matches.
- The sentence agrees with L211 ("A system can represent a false theory") and L397 ("A system may understand a false theory"), with Part 0's L11, and with W22.1's typing of the criticism's connection as an explanatory candidate (L371; the R28 ruling).
- No unchanged sentence that uses "explanation" (L11, L23, L47, L335, L532, L536, L594, L602) becomes false. The sentence scopes itself to "this commitment".

## 4. Ruling

**KEEP.** W36.1 stands as drafted. OLD, NEW, KIND (CLAIM) and DECLARATION are unchanged.

**Reason.**
- The reply finds no defect. The move it names on N3 is real and is toward the fixed verdict:
  - the "in form" yes, which the old s2 read literally denied, is now the declared "explanatory candidate, which ordinary usage may still call an explanation";
  - the "No" stays, because the myth fails (E): (F1), and non-circular dependence at L255 and L273.
- The move follows from the declaration's own clauses, and the entry's CASES AT RISK predicted it. So it is not an undeclared change of claim.
- N1 holds (it is carried by s1, L231 and R24), N2 holds or moves toward, and O8, O15, N22 and D3-T hold.
- Every quotation checks.
- The pointers are exact, and no coherence defect was found.

**For the CHECK field (S90 rule 3):** "Cross-examination of revision 2 (S90 part C): Atria gave STANDS and named, under (d), a move toward the fixed verdict on N3: the candidate/account distinction gives "No, it does not explain" with "Yes, an explanation … only in form", which the old s2 read literally denied. Mimo gave STANDS with no point. Ruled KEEP after the cross-examination: the move is toward, and it follows from the declaration's two clauses ("explanation" means an account; a false theory offered as an answer is a candidate that ordinary usage may call an explanation). The "No" rests on (F1) and non-circular dependence (L255, L273). N1 holds (s1, L231, R24), N2 holds or moves toward, and O8, O15 and N22 hold. The pointers to Part V and to Part VI (L313) are exact."
