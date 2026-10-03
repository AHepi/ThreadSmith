# Ruling: s90_xexam_atria_C, item 3, R21 (W58(i).1)

*By a fresh Claude checker, 24 September 2026. The checker works under the S90 rule, as extended by "S90 Parts - how they will be read, written before sending.md" (rules 1–3 and 5), and under the rerun note "S90 and S87 - seven calls rerun after the container restart - written before sending.md" (ruling 4: the pass-2 reply stands where the pass-1 reply would have stood). It did not draft, assemble or check the change list, and it did not write the part briefs.*

*File name.* The task asked for "ruling s90_xexam_atria_C (part C, Atria). Pass 2, accepted on attempt 6 of 6: … 1,227 words. item 3 R21.md". That name is 287 bytes, over the filesystem's limit of 255. This file uses the short form of its siblings, "ruling s90_xexam_atria_C item 1 R13.md" and "… item 2 R06.md".

*The call.* The reply is `parts/s90_xexam_atria_C.response.txt`. The file name in the task puts the call description where the tag belongs, and no file of that name exists. This is the only reply of this tag.
- Pass 2 was accepted on attempt 6 of 6. The receipt's attempt history shows attempts 1–5 at status 0 with nothing back.
- Attempt 6 returned status 200 and finished "stop", with 0 bad chunks and 7,638 characters. END OF REPORT is on the last line.
- The reply's sha256 is bd51b78593b3ac9e7d194d7f0b62e43e223f8c487d6e611a6118999d50d7a72f, which matches the receipt. It is 1,227 words by `wc -w`.
- The receipt's `user_sha256` is a94c8ef9ead3…, the part C brief.
- No reasoning file was opened.

*Why R21 is here.* The reply's closing line is "R21: STANDS". Its point 3, under (d), names a move of the theory's verdict on O45 that R21 causes. The reply calls the move toward the fixed verdict and declared. Under S90 Parts rule 2, a change is contested when a reply names a moved verdict on it, "whatever line it gives the change". So R21 goes to a checker.

*Sources:*
- *the change list, md5 a5c92adc9f1e3806c0f9c6394cffde1e (587eebf; no later commit touches it);*
- *the revised text, `tests/Revision 2 - file 13 draft 2, theory text, as sent for cross-examination.md`, md5 9aecf2f30ce0b4523606b2b8409fdf37;*
- *file 11, md5 5e494c1095d920d128b9a79de378f923, read only;*
- *the part C brief, md5 2183faa5005b112347f484b6c8ace196 (its R21 block and task (d));*
- *the S81 book, md5 4f488d149e44669240d5db546c8e946a (O36, O45, O46, O47);*
- *the S89 candidate book, md5 b2e535777976a511935430bd089ba500 (N1);*
- *D3-T's `final.md`, md5 6b211dea40d735abf50426e56344f161;*
- *the S81 determination's 01 (O36, O45) and 03 (§8 item 10), and 06 (O45);*
- *the revision note draft (rows R2-21 and L2-16).*

*The S87 rules (05, 05b and 05c) govern S87 rows, not S90 parts, so they are not applied here.*

*Map (part-rule table): "R21 | W58(i).1 | C17 | C | 301 | 299 | CLAIM | O45, N1".*

## 1. The entry and its checkers' history

W58(i).1, "Part VI: the supports assessed are the subsets of the written Γ".
- **Group** C. **Item** W58(i).
- **Place.** Part VI, the paragraph after (B), s2, last clause: file-11 L301, revised L299.
- **REASON WORD** clarification. **KIND** CLAIM.
- **OLD:** `and the supports assessed are the ones actually written, not a support someone could write in their place.`
- **NEW:** `and the supports assessed are subsets of the written \(\Gamma\), whether or not anyone has set them out, not a support someone could write with commitments outside \(\Gamma\).`
- **DECLARATION:** "Part VI now says that the supports assessed are the subsets of the written commitments, whether or not anyone has set them out, and not supports that need commitments outside them."
- **Both found.** OLD is at file-11 L301 byte for byte, and NEW at revised L299 byte for byte. The brief's R21 block carries the same OLD, NEW, KIND and DECLARATION, with "Situations: O45, N1".
- **CHECK (the checkers' verdict):** "check 2, SOUND. O36 is watched, not held on firmer text: a reader who takes the rewritten route's premise to be one Γ already carries would have it assessed."
- **REASON (not sent), in short.** It comes from the S81 determination's 03 §8 item 10: "'the supports actually written' at L301 has two readings, one of which narrows (S)" (M26). (S) ranges over every W ⊆ Γ. NEW keeps the intended reading, which is 01's at O36: "(S) and (B) … range only over subsets of the written Γ". It closes the other reading. KIND: "The plan offered 'WORDING or CLAIM'; ruled strictly, it is CLAIM."
- **CASES AT RISK (drafters' expectation, not sent):**
  - "O36 holds AGREE, on firmer text."
  - "O45 holds, or moves toward. 'Whether or not anyone has set them out' says that a support nobody described is still assessed, as L309 s3 says of a route."
  - "O46 holds: the cable is a commitment outside Γ … O47 holds."
  - "No N-case turns on which supports are assessed. N1's support without the sun-god sentence is a subset of the written Γ on either reading."
- **Record.** Revision note row R2-21: "W58(i).1 | C17 | 301 | clarification | CLAIM | yes". Layer-2 row L2-16 (M26) quotes the old clause and is marked "changed by R2-21".
- **Earlier rulings.**
  - **Batch 1** makes no ruling on R21. Its ruling on R15 (W20.1; Mimo A1, point 2; FIX) names W58(i).1 twice, as agreeing with the clause it adds to L231 ("whether or not anyone has described their work"). The second time is in O45's new CASES AT RISK line for W20.1: "L309 s3, W28.1 and W58(i).1 agree".
  - **Batch 2** makes no ruling on R21. Its ruling on R51 (W19.2; KEEP) finds that Atria A2 called L299 unchanged. It says "The reply makes no point on R21, so nothing goes to R21's checker". It relies on "L299 as W58(i).1 words it (O36)" and on R21's line "O36 holds AGREE, on firmer text".
  - **Mimo's reply to part C** gives "R21: STANDS" and makes no point on it. Mimo A1's point 2 on R15 quotes NEW at L299 as resolving an ambiguity in R15's reading. That point is about R15 and makes no claim against R21.
  - **The single S90 call** (C17) failed and supports nothing.
  - **Nothing on R21 is to be reconciled.** This ruling has to agree with the R15 FIX and the R51 KEEP, and section 3 checks that it does.

## 2. The reply's argument

The closing line is "R21: STANDS". Point 3 is headed "R06, R21, R24, R25, R30, R34 · (d) — declared moves toward the fixed verdicts; none away." Its R21 bullet:

> "R21 (line 299) on O45: the second spring "was already a route" though nobody described it as working. "Subsets of the written \(\Gamma\), whether or not anyone has set them out" makes \(\{\text{spring 2}\}\in\mathsf S\) assessable and brings the prose into line with (S), which is defined over *all* subsets of \(\Gamma\); the old "the ones actually written" contradicted (S) and the verdict."

The reply finds no defect in R21. It names a move toward on O45, which it counts as declared. It adds that the old wording contradicted both (S) and the verdict.

**Quotations checked (S90 rule 8).**
- "was already a route" is in O45's verdict ("It was already a route."), word for word.
- "Subsets of the written \(\Gamma\), whether or not anyone has set them out" is in NEW at revised L299. The only difference is the capital S.
- "the ones actually written" is in OLD at file-11 L301.
- "(line 299)" is correct.
- "(S), which is defined over *all* subsets of \(\Gamma\)" paraphrases (S) correctly: revised L290, file-11 L292, "\(\mathsf S_{E,p}=\{W\subseteq\Gamma:\operatorname{Account}(E|W,p)\}\)".
- "though nobody described it as working" paraphrases the situation's "never described as doing anything".

All the quotations are found.

**One claim is overstated.** Old L301 did not contradict (S) or the O45 verdict. Only one of its two readings did.
- On the intended reading, "actually written" means built from the commitments the candidate carries, as against "a support someone could write in their place". That is the S81 determination's reading at O36 ("(S) and (B) … range only over subsets of the written Γ"), and on it L301 is entailed by (S).
- The narrow reading, "only the supports someone has set out", is the one that pulls against (S) and against L309 s3.
- The S81 determination gives file 11 AGREE on O45 through L309 s3 (01, O45; 06, "O45: RULING STANDS"). So file 11 did not contradict the verdict as the determination read it.
- The overstatement does not bear on the ruling. It is the ambiguity the entry's REASON gives, stated too strongly.

## 3. Reading

**O45, "The spring nobody mentioned".** The account contains two springs, both connected and both sufficient. The second is never described as doing anything until the first is deleted. The fixed verdict: "It was already a route. That nobody said it did work does not make it a later addition."
- **The revised text.**
  - Both springs are in Γ. L231 types the commitments as "components of \(E\), those the candidate offers as doing the work". With batch 1's R15 fix, it adds "whether or not anyone has described their work". The account contains the second spring, connected. The change list reads that as offering it (W20.1, the O45 bullet).
  - By (S) (L290), \(\{s_2\}\in\mathsf S\), since \(s_2\) alone is sufficient with the named background fixed. The same holds for \(\{s_1\}\) and \(\{s_1,s_2\}\). This is the pattern of "Redundant routes" (L307).
  - L307 (W28.1): "a route is a support of the candidate, a member of \(\mathsf S\), and is a route whether or not any history runs it". L307 s3, unchanged: "A route already present in the candidate is a route whether or not anyone has described its work".
  - NEW at L299 says \(\{s_2\}\) is assessed "whether or not anyone has set them out". So nothing in Part VI makes it wait on the author's later statement.
  - Deleting \(s_1\) keeps a support, since a minimal support (\(\{s_2\}\)) omits it (L305). No component is reassigned, so L307 s3's second clause (a new candidate) does not apply.
  - The theory's verdict is AGREE: the second spring was a route from the start.
- **The current text.** The S81 determination reads file 11 as AGREE on O45, through L309 s3 (M28), a move toward from file 10's SPLIT. Old L301 on its narrow reading would assess \(\{s_2\}\) only once someone set it out, and that pulls against L309 s3. A reader who takes that reading is split. The reader the determination follows is not.
- **So O45 holds AGREE on firmer text, or moves toward** from split for a reader of the narrow reading. Either way the move is toward the fixed verdict, which is the entry's "holds, or moves toward". Nothing moves away.
- **The move is declared.** It is the declaration's own clause, "whether or not anyone has set them out". So it is not an undeclared change of claim under task (d).

**N1, "The seasons and the sun god"** (given with R21). The fixed verdict: Tomas explains, and the sun-god sentence is not part of what explains. "Strike it out and the account works exactly as before."
- Say the god sentence \(g\) is in Γ. Then \(\Gamma\setminus\{g\}\) is a subset of the written Γ. NEW has it assessed although nobody set that support out, and (S) makes it a support. R24's test at L313 then gives \(\{g\}\) "critical in no support".
- Say \(g\) is outside Γ. That is the Γ question that R06's check 2 marked as watched, under W20 and W33.1. Then it belongs to the named background (L231) or is no component of \(E\) at all. Either way it is not a commitment for (S) to assess.
- Either way N1 holds AGREE. R21 is compatible with the verdict and adds a firmer ground on the first reading. No move away.

**O36, "A premise both routes use"** (not given in part C, and not raised by the reply). It is checked because R21's CHECK names it as watched, and because the R51 ruling relied on it.
- The fixed verdict: "P is critical in each route as written. That another route could be written without it is a fact about a candidate nobody has written."
- **On the case's natural reading**, the premise that would replace P in the unwritten version is not among the written commitments. Then the rewritten route needs "commitments outside \(\Gamma\)", and NEW's last clause excludes it by name. That is firmer than OLD's "in their place". AGREE holds, on firmer text.
- **On the reading the CHECK names**, the replacement premise is already in Γ. Then the rewritten route is a subset of Γ. (S) made it a support in file 11 as well (file-11 L292), so R21 adds nothing (S) did not already say; it only stops the prose seeming to deny it.
  - The verdict's mark still holds. Criticality is relative to the support it is assessed in (L299 s2, unchanged), so P stays critical in each route as written.
  - Only the verdict's gloss, "a candidate nobody has written", reads less naturally on this reading. That is a fact about (S), and it holds in file 11 too.
- **So the CHECK's "watched" and CASES AT RISK's "holds AGREE, on firmer text" are both right.** The first gives the caution, and the second the case's natural reading. The R51 ruling's reliance on the latter stands.

**O46 and O47** (named in CASES AT RISK and not given in part C).
- O46: the cable is a commitment outside Γ, so NEW's last clause puts the cable account outside the candidate's supports. With L307 s3's reassignment clause, it is a new candidate. AGREE holds.
- O47 turns on interference (L305, L309). R21 does not touch it.

**D3-T** (the discarded lamp controller). It turns on selection populations and an untried setting (Derivation 3), not on which supports of a candidate are assessed. R21 does not touch it.

**Coherence (task (c)). No defect is found.**
- NEW restates what (S) (L290) and the restriction \(E|W\) for \(W\subseteq\Gamma\) (L287) already fix, and it removes the reading that narrowed (S).
- It fits "Infinitary support" (L311), where the supports are unbounded index sets that nobody could set out one by one. Old L301's narrow reading would have left that paragraph without assessed supports.
- It agrees with W28.1 at L307 ("whether or not any history runs it") and L307 s3 ("whether or not anyone has described its work"). It agrees with R15's L231 clause as fixed in batch 1, and with R24's "every support" at L313.
- "The written \(\Gamma\)" is the only use of "written Γ" in either text. It keeps OLD's word "written" and reads as the candidate's identified Γ (L231). It does not clash with L401's "written in a particular format", which concerns (R), Deploy and Build, not Part VI's supports.
- **The DECLARATION matches NEW.** "The written commitments" is "the written \(\Gamma\)". "Supports that need commitments outside them" is "a support someone could write with commitments outside \(\Gamma\)".
- **KIND CLAIM is right.** NEW closes a reading of OLD, and the reply names a move toward on O45. Had the entry been WORDING, that move would be undeclared. As CLAIM it is declared.

## 4. Ruling

**KEEP.** W58(i).1 stands as drafted. OLD, NEW, KIND (CLAIM) and DECLARATION are unchanged.

**Reason.**
- The reply finds no defect. The move it names on O45 is toward the fixed verdict.
  - On the S81 reading, file 11 was already AGREE through L309 s3, so the mark holds on firmer text.
  - For a reader of old L301's narrow reading, the case moves from split to agree.
  - Either way, the move follows from the declaration's clause "whether or not anyone has set them out", and CASES AT RISK predicted it ("holds, or moves toward"). So it is not an undeclared change of claim.
- The reply's "the old … contradicted (S) and the verdict" overstates the old wording's ambiguity: only its narrow reading did. That does not bear on the entry.
- N1 holds. O36 holds AGREE on the case's natural reading, and stays watched as the CHECK says. That agrees with the R51 ruling. O46, O47 and D3-T hold.
- Every quotation checks, and no coherence defect was found.

**For the CHECK field (S90 rule 3):** "Cross-examination of revision 2 (S90 part C): Atria gave STANDS and named, under (d), a declared move toward the fixed verdict on O45: 'whether or not anyone has set them out' has the second spring's support assessed from the start, in line with (S). Mimo gave STANDS with no point. Ruled KEEP after the cross-examination. The move is toward and follows from the declaration's own clause. On the S81 reading file 11 was already AGREE on O45 through L309 s3, so the mark holds on firmer text; only old L301's narrow reading ('only the supports someone has set out') pulled against it, and the reply's 'contradicted (S) and the verdict' overstates that ambiguity. N1 holds. O36 holds AGREE on the case's natural reading (the replacement premise is outside Γ, which NEW's last clause excludes), and stays watched as check 2 says: on the other reading, (S) already assessed the rewritten route in file 11, and P stays critical in each route as written. O46 and O47 hold."
