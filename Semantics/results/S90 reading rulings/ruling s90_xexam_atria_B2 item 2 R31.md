# Ruling: s90_xexam_atria_B2, item 2, R31 (W21.1)

*A fresh Claude checker, 24 September 2026. It follows the S90 rule (rules 1, 2, 5, 7 and 8), "S90 Parts - how they will be read, written before sending.md" (rules 1 and 3) and "S90 and S87 - seven calls rerun after the container restart - written before sending.md" (section 2 item 4: the pass-2 reply stands where the pass-1 reply would have stood). This checker did not draft, assemble or check the change list, and did not write the part briefs.*

*The file name.* The name asked for, "ruling s90_xexam_atria_B2 (part B2, Atria). Pass 2, accepted on attempt 4 of 4: … 1,375 words. item 2 R31.md", is 304 bytes. That is over the file system's 255-byte limit, so this file uses the short form of its sibling `ruling s90_xexam_atria_B2 item 1 R42.md`.

*The call.*
- *The reply read is `parts/s90_xexam_atria_B2.response.txt` (1,375 words by `wc -w`). The name the orchestrator gave for it is a label, and no file has that name.*
- *Its sha256 f965836a9b2f… matches the receipt. The receipt shows pass 2 with four attempts: 1 to 3 had status 0 and finish none, and 4 had status 200, finish "stop" and 0 bad chunks. No pass-2 attempt file exists. The last line is END OF REPORT. It is accepted.*
- *Its reasoning file was not opened.*

*Sources.*
- *The change list, md5 a5c92adc9f1e3806c0f9c6394cffde1e.*
- *The revised text, "Revision 2 - file 13 draft 2 …", md5 9aecf2f30ce0b4523606b2b8409fdf37.*
- *File 11, md5 5e494c1095d920d128b9a79de378f923, read only.*
- *The part B2 brief, md5 d214f495e0b9fcac4f423d522bee0d37, section R31.*
- *The S81 case book, md5 4f488d14…; the S89 candidate book, md5 b2e53577…; D3-T `final.md`.*
- *The S81 determination 01 and 04, for the file-11 marks; the plan's row W21 and its test-round predictions; the worklist's W21.*

## 1. The entry, its history and earlier rulings

W21.1, "L405: ≡_ℓ is defined, and 00:746's first sentence is restored".
- **Place:** Part X, **Newness**, file-11 L405, revised L407.
- **Group:** B2. **Reason word:** clarification.
- **Record row:** R2-31 (C26 in the S90 brief).
- **OLD:** `**Newness.** With \(R_{<e}(s,h)=\bigcup_{\xi\text{ before }e}R_{\beta,\ell}(s,\xi)\),`
- **NEW:** `**Newness.** Write \(d\equiv_\ell c\) when there are transports from \(d\) to \(c\) and from \(c\) to \(d\), both faithful on \(c\)'s contract at grain \(\ell\). The equivalence is structural at the stated grain, not string equality or similarity. With \(R_{<e}(s,h)=\bigcup_{\xi\text{ before }e}R_{\beta,\ell}(s,\xi)\),`
- **KIND:** CLAIM.
- **DECLARATION:** "Part X now defines the equivalence in (N): d ≡_ℓ c when there are transports from d to c and from c to d, both faithful on c's contract at grain ℓ. The equivalence is structural at that grain, not string equality or similarity."

**Its checkers' history.**
- **CHECK:** "check 1, SOUND."
- **W19.2's recheck of skeleton conflict 12** (change list L2027): "W21.1 … stands as drafted. O11, O18 and N15 keep W21.1's readings."
- **The plan's row W21** took c's contract on purpose. Its guards are O3, O11, O15, O18, O27, O31, N4, N15 and N21.
- **CASES AT RISK** gives no move away on any case:
  - O11 "stays AGREE, and more securely", since Wednesday has no Build in any case;
  - O3, O18, O31 and N21 "stay AGREE";
  - O27 stays SILENT;
  - N15: AGREE "is secured";
  - N10 is unchanged;
  - N4 is watched, "not away".

**Earlier rulings.**
- **Batch 1 and batch 2** made no ruling on R31 or W21.1.
- **A sibling ruling in this reading** (`ruling s90_xexam_mimo_B2 item 1 R31.md`) ruled Mimo B2's "R31: FALLS — definition of ≡_ℓ ill-typed and non-symmetric" **KEEP**.
  - It held that the transport from d to c is judged on c's contract as (R) judges a transport into c, and that the transport from c to d is typed as in Part V.
  - It held that nothing uses symmetry, since (N) is the relation's only use.
  - It held that Mimo's repair ("each faithful on the contract of its source") would change the claim and could reopen N4.

  This ruling is reconciled with it in section 4.

## 2. The reply's argument

The closing line is "R31: STANDS". Point 3, "R31 (a, d) — a repair of an undefined symbol, and it settles the newness cases", argues as follows.

**The symbol was undefined, and the definition is well formed.**

> "The current text's (N) used \(d\equiv_\ell c\) without defining it; line 407 now defines it … The definition is well formed for both directions (a transport to a content is assessed on the content's contract, as in (R); a transport from a content is assessed on its domain's contract, as in Part V)."

**The claimed move.**

> "This moves the newness cases from unsettled to settled, all toward the fixed verdicts: **O11** Wednesday (the chosen key is mutually faithful with Tuesday's, so not new — "she is reusing what Tuesday gave her"); **O18** and **O31** (the small binding is not equivalent to anything in the received repertoire, and the rest keeps its inherited provenance); **N15** and **N21** (newness is indexed to the system's prior repertoire, so "not new to the world" and "her own construction" are both respected). The declaration states the definition, so the moves are accounted for."

**Why it is re-examined.** The reply names moved verdicts on R31, so R31 is re-examined whatever line the reply gives it (S90 rule 2; Parts rule 2). The reply is also the counter-reading to Mimo B2's FALLS.

## 3. The texts

**Quotations (S90 rule 8).** All are found.
- The line 407 wording is found at revised L407. OLD is found once in file 11, at L405, and nowhere else.
- "she is reusing what Tuesday gave her" is found in O11's verdict.
- "not new to the world" is in N15's verdict: "What she ended up with was not new to the world".
- "her own construction" is in N21's verdict: "the grasp of the rule is her own construction".
- The (R) and Part V typing it paraphrases is found at revised L205–208 and L233–236.

**The typing: correct.**
- (R) judges a transport *into* c on c's contract: \(t:\operatorname{Org}_\ell(o)\to c\), faithful on c's contract (L205, L208).
- Part V judges a transport from D to E on a contract whose edits are D's: (F1) uses \(\operatorname{Sol}_{\lambda(k)}(a,b)\) with \(\lambda(k)\subseteq D\).
- NEW's d→c transport is (R)'s pattern, and its c→d transport is Part V's. This is the entry's own REASON, and the sibling ruling holds the same.
- **Symbol use.** \(\equiv_\ell\) occurs only at L407 and in (N) at L410 of the revised text, and only at L408 in file 11, where it is undefined. So the reply's "undefined symbol" is right.

**"From unsettled to settled": the same marks, reached more firmly. Nothing moves.**
- **O11, O18 and O31** have a ruled file-11 baseline.
  - S81's two readers and determination 04 give AGREE on each, with the passage the same (01 §O11; 04 rows O18 and O31, "f11 L401 s5").
  - The plan's P1 predicts that none of O1–O52 moves.
  - So the current text was not SILENT on them. The marks rested on Build and on L401 s5 ("A small binding newly prepared inside received content is construction of that binding, and the rest of the content keeps its inherited provenance"), not on a reading of ≡_ℓ.
  - What NEW adds is a checkable New. The mark is the same. The entry records exactly this: "stays AGREE, and more securely".
- **O11: the reply's route is not what settles it.**
  - The situation gives only that she picks a key "saying it looks like Tuesday's". That is similarity, which NEW says is not the criterion.
  - So "the chosen key is mutually faithful with Tuesday's" is a fact the case does not supply. The entry's LOSS says a case "must supply that or leave it open".
  - "Wednesday is neither" holds on either reading of New, because Wednesday has no Build (she picks and files nothing), and (G) needs Build.
  - The reply's route points the same way as the fixed verdict. It is not needed, and it is not a move.
- **O18 and O31.**
  - The corrected content differs from the received one at the new catch or tooth, and at this plant's valve.
  - So no transport from the received content to the corrected one is faithful on the corrected content's contract, and the corrected content is New.
  - L401 s5 credits only the binding. This matches CASES AT RISK.
- **N15 and N21** have no file-11 baseline. The plan rules O53–O76 in the test round.
  - **N15.** Salma's repertoire before the correction held only the "less" copy, which is not equivalent to the "more" content on that content's contract. So it is New to her, while it is the teacher's idea (not new to the world).
  - **N21.** Heard phrases give no transport faithful on the rule's contract, which covers unheard phrases. So her grasp is New to her.
  - Both readings agree with the fixed verdicts and with CASES AT RISK.
  - **If the test round rules file 11 SILENT on either**, because ≡_ℓ was undefined, the move is toward the fixed verdict. It traces to this declared CLAIM, as the plan's P2(b) requires, and it is not an undeclared change of claim.
- **Other cases.** The reply names no case away. It names neither N4 nor D3-T, and D3-T concerns neither newness nor equivalence.

**What follows.** No verdict moves away, and no undeclared change of claim is shown. The reply's "moves" are, on the ruled baseline, the entry's own "more securely" and "secured". The typing the reply gives is the one that answers Mimo B2's FALLS.

## 4. Ruling: KEEP (reconciled with the Mimo B2 ruling on R31: KEEP)

**The entry stands as drafted, byte for byte:** OLD, NEW, KIND CLAIM and DECLARATION.

**One reconciled append to CHECK**, replacing the separate appends of the two R31 rulings:

"After the cross-examination:
- s90_xexam_mimo_B2 (point 1, R31 FALLS: 'ill-typed and non-symmetric'): KEEP.
  - The transport from d to c is judged on c's contract as (R) judges a transport into c (L205–208, file-11 text unchanged, on which Deploy and so (N)'s repertoire rest). The transport from c to d is typed as in Part V. Both are checked on the changes c commits to.
  - The relation is taken on the contract of the content whose newness is in question. (N) is its only use, and nothing uses symmetry. 'Equivalence' is the file's two-direction sense (L357).
  - The declaration states the definition word for word.
  - The proposed 'each faithful on the contract of its source' would make c new whenever an earlier content commits beyond c. That is a change of claim, against plan row W21, and it could reopen N4.
- s90_xexam_atria_B2 (point 3, R31 STANDS; names moves 'from unsettled to settled, all toward the fixed verdicts' on O11, O18, O31, N15 and N21): KEEP.
  - It gives the same typing.
  - On O11, O18 and O31, file 11's ruled marks are already AGREE, through Build and L401 s5, so no mark moves. NEW makes New checkable, which is the 'more securely' recorded here.
  - O11's 'Wednesday is neither' rests on the absence of Build. The case says only that the key 'looks like' Tuesday's, which NEW excludes as a criterion.
  - N15 and N21 have no file-11 baseline yet. A move toward on either, if the test round finds one, traces to this declared definition."

**Nothing else changes.**
- No other field changes, and nothing follows by program: the counts, the note's N and M, and record row R2-31 are unchanged.
- W19.2's recheck of skeleton conflict 12 stands.
- **Noted for the owner, not ruled** (it comes from the sibling ruling): a sentence at Part IV (L189) or (R) (L205–208) could say that a transport into c is faithful on c's contract when it is faithful on the pairs it carries into that contract. That would state in words the reading the file already needs. It concerns file-11 text outside the 55 changes.
