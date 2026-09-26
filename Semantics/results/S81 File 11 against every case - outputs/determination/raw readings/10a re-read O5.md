# O5, Greta's dough: re-read after Mimo's retry says RULING FALLS

*Written by a fresh Claude determiner on 24 September 2026, under rules 05, 05b and 05c in `results/S81 File 11 against every case - outputs/determination/`, as the S90 and S87 rerun note (section 2, item 4) directs for the O5 row. This determiner did not draft, assemble or verify the determination, and did not write any earlier reading of a cross-examination reply.*

**What was opened.**
- Mimo's O5 retry reply and its receipt: `results/S87 Cross-examination - the S81 determination - returns/Mimo retry one row per call/s87_xexam_mimo_O5.response.txt` and `.receipt.json`.
- The brief it answered: `tests/S87 Cross-examination - retry, O5 alone.md`. Its sha256 97297d856d51… equals the receipt's `user_sha256`.
- The rules: 05, 05b and 05c in full; the S90 rule, the S90 Parts rule and the S90 and S87 rerun note.
- The determination: 04, sections 1–7; 04b (O1 group), its header, summary table and the O5 row; 04c and 04d, at their O5 entries; the 04e packet `O5.md`, in full.
- File 11 at L5, L25–L29, L37, L41–L45, L73, L125, L155–L163, L253–L261, L277, L355–L367, L423–L447, L501–L530 and L586. File 10 at L23, L25, L38, L40–L41, L136–L140, L176, L268–L274, L290 and L512–L525. Both files were searched whole for "appropriat", "legitima" and "certif".
- The case book, at O1 and O5 (md5 4f488d149e44669240d5db546c8e946a).
- For the reconciliation, the two S90 batch readings, searched for O5, R10, L161, W57 and W32(b), and read at batch 2's R10 lines. Also the change-list entry W57.1 + W32(b).1 (R10) in `tests/Revision 2 - change list, draft of 23 September.md`.

**What was not opened:** Atria's S87 reply, 06, 07, 08 or 09; the O30 and O17 retry replies or their readings; raw readings 07a and 09a; part P2's reply; any attempt or reasoning file.

**Disclosed.** The R10 entry's REASON field contains one sentence that reports Atria's position on O5 as 06 records it. This determiner read that sentence while reading the entry for the reconciliation. Nothing below relies on it, and the ruling in section 4 rests on the texts alone.

---

## 0. The receipt

- **The call was accepted.** `s87_xexam_mimo_O5` was accepted in pass 2, at attempt 4 of 6: status 200, finish "stop", 0 bad chunks, 2,537.6 s.
  - The earlier attempts of pass 2 all failed. Attempt 1 ended "length" with no content. Attempts 2 and 3 ended with status 0.
  - The rerun note allows pass 2: the network cut of pass 1 did not use up the call.
- **Checks.**
  - The response's sha256, 074802f4…, matches the receipt.
  - The last line is END OF REPORT.
  - The reply is 1,237 words by `wc -w`. It used 106,892 reasoning tokens of the 131,072 allowed.
- **Closing line:** "O5: RULING FALLS — file 11 SILENT". Under 05 rule 2 and 05c item 4, the row therefore goes to a fresh determiner.

## 1. The determination's ruling

**04, table (section 3):**

| case | file-10 mark | file-11 mark | verdict | passage | direction | kind | check |
|---|---|---|---|---|---|---|---|
| O5 | AGREE (base) | AGREE | SAME | CHANGED (additive): f11 L161 s3, L514 | — | no change | T, R: UPHELD (medium) |

**04, section 5, test (b):** "O5, "Greta's dough": 4 of 5 file-11 readings SILENT, on f11 L161 s3 ("the semantics records the restriction and supplies no rule that certifies it"). Ruled AGREE: Greta's account states the ground of her limit, and f11 L514 makes "what makes a restriction appropriate" a stated input on which the verdict is "a verdict given the input". Upheld at medium confidence."

**04b, O1 group, its reasons for the file-11 AGREE:**
- f11 L161 s3 makes appropriateness "part of the claim", and L514 makes it a "stated input" on which the verdict is "a verdict given the input".
- "Greta's claim states it … The input is present. The verdict given it is that the restriction is appropriate, because the limit follows from a part of her account. That is the fixed verdict's finding, qualified as given the stated ground and open to criticism. A qualification is the same finding (brief, "Same finding")."
- "'Supplies no rule that certifies it' says the semantics adds no rule of its own. It does not withhold the verdict given the stated ground, which L514 grants in terms."
- "If O5 were SILENT, L514's "a verdict given the input" would never yield a verdict on appropriateness, and its contrast "where the input is missing" would do no work for Part III."
- "O1 is the contrast: its input is missing, and it is SILENT."

**The other parts of the ruling.**
- **File 10:** AGREE, the baseline. Both 1K returns agree with it. "The limit is stated (f10 L272), and the yeast is a component of her account whose relation changes with temperature (f10 L140, the signature under intervention)."
- **Passage:** "File 11's AGREE rests on L161 s3 and L514, which are new (M17, M48). File 10's rests on stated scope alone."
- **The verifications.**
  - 04c (text lens) upheld the ruling at medium confidence: "The ruling is upheld because L514 is the more specific sentence and speaks to this configuration."
  - 04d (rule lens) upheld it too, and recorded "the row's substance is exposed, not its rule application."
- **The hazard.** 04 section 7 records a "reading hazard in f11 L161 s3" for a later revision.

**Why the row matters.** A file-11 SILENT or SPLIT would make O5 AGREE→SILENT, a change away that traces to the new sentences M17 and M48. That would be a theory change away, and test (b) would fail.

## 2. Mimo's argument

The reply makes eight points. It rules file 11 SILENT on the first point of the fixed verdict, "This is a legitimate narrowing".

1. **SILENT on "legitimate".** "File 11 speaks to such evaluations twice, and each time withholds them." It quotes f11 L161 s3 and L514 ("stated inputs that the semantics records and does not supply: … what makes a restriction appropriate (Part III) …"). "On this point they record the claim's ground and abstain. SILENT precedes AGREE in the rules' order, so if it fits, AGREE is not reached." The reply says the second point, "The limit follows from a part of her account", "is at best *recorded*". It relies on the first point alone.
2. **The bridge step has no source.** "f11 L514 *classifies* verdicts … it does not manufacture one." The reply's analogy is Part XI: of the obligations O and P, "Their declaration makes no claim that the aims are worth pursuing, and (P) does not rank alternatives." The theory gives repair verdicts given O and P, "never a verdict on their merits", and "Restriction-appropriateness is the same kind of item." On this reading L514 governs verdicts like f11 L161 s2's "An account at a stated scope answers the question asked at that scope". The reply adds: "On the ruling's reading the same clause would have to yield *worth* verdicts on O and P, which Part XI forbids in terms."
3. **The criterion reading contradicts the text.** If the first clause of L161 s3 were a criterion, "then the semantics would be supplying exactly "a rule that certifies it"". So the clause must be read as "placement (appropriateness lives in the claim's criticizable content)". "With no decision rule, there is no verdict for "given the input" to qualify."
4. **"Same finding" is applied without its first condition.** "A verdict … that *reaches* the fixed verdict's finding *and adds* a qualification …". The reply says "recorded, uncertified, criticizable" "is a statement that no finding is established."
5. **Non-vacuity cannot tell the limits apart.** f11 L259 needs only that exclusions be "excluded by a stated scope, not silently". A stated Tuesday limit meets that too. The reply accepts that the route through non-circular dependence (f11 L257) fails, for the ruling's reason. It adds that "the theory's scope verdicts are about *honesty* (statedness), not legitimacy" (f11 L45).
6. **"Given the input" abstains both ways.** On the Tuesday variant, "the same pairing yields "the verdict is unsettled," not *illegitimate*". "A machinery that can never find a narrowing illegitimate is not finding "legitimate" here."
7. **The consequences.** With the file-11 mark SILENT, the verdict is CHANGED, the direction away and the kind a theory change, through M17 and M48. The reply considered SPLIT and rejected it: L514's "does not supply" and L161's "supplies no rule that certifies it" "agree and resolve the reading".
8. **The file-10 mark stands.** The reply records, without relying on it, that f10's texts "are no stronger" on this point.

**Quotations checked.**
- Every quotation the reply relies on was found word for word:
  - file 11: L161 s2 and s3, L514, L259, L45 and L433;
  - file 10: L41;
  - the case;
  - the mark rules and "Same finding", from section 2 of the brief;
  - the determination's words, from section 5 of the brief.
- The L433 sentence is placed as in "the paragraph opening at L427". That paragraph opens with **Repair.** at L427, and the sentence is at L433.
- The L45 wording ("in the physics and the fidelity facts") is file 11's. File 10's L41 reads "and in the fidelity facts", as the brief notes.

## 3. The texts

**The case (case book O5).** "Greta's rule says her bread dough doubles in two hours. It fails in January. She restates it for rooms warmer than twenty degrees, and her account says why: the yeast that makes the gas works slowly in the cold. Replace her limit with "on days other than Tuesdays" and her account has nothing to say about why Tuesdays would matter."

The fixed verdict has two points:
- (i) "This is a legitimate narrowing."
- (ii) "The limit follows from a part of her account."

**File 11.**
- **L161 s1–s2.** "A contract is a declared subset of the physically admitted changes, and a stated scope is what makes it one. An account at a stated scope answers the question asked at that scope; it does not answer a broader question that failed, and a narrowing adopted after a failure is a new claim at a new index (Part VIII)."
- **L161 s3 (M17, no file-10 counterpart).** "What makes a restriction appropriate to the question asked is a substantive, criticizable part of the claim; the semantics records the restriction and supplies no rule that certifies it."
- **L514 (M48, no file-10 counterpart).** "Besides the two primitives, some claims take stated inputs that the semantics records and does not supply: the obligations \(O\) and \(P\) of a repair, with the occasions each covers (Part XI); the scope of a contract and what makes a restriction appropriate (Part III); the system boundary and continuity of an attribution (Part XII). A verdict that depends on one of these is a verdict given the input; where the input is missing, the verdict is unsettled and the semantics says so rather than choosing the input from the verdict wanted."
- **L125, the same as f10 L140 word for word.** "a **causal assignment** has a signature that changes under intervention on its output port and under replacement of the component, and is invariant under observation edits".
- **L257 and L259, the same as f10 L270 and L272 word for word.** Non-circular dependence and non-vacuity.
- **L45.** "… it is caught by the requirement that the exclusion be stated (non-vacuity, Part V), and then by any criticism that supplies the excluded change. Objectivity lives in the physics and the fidelity facts; scope-honesty lives in the record."
- **L433 s1–s2.** "The obligations are declared inputs: … Their declaration makes no claim that the aims are worth pursuing, and (P) does not rank alternatives."
- **L27 and L447.** Where a claim needs worth, "the semantics takes it as a **declared input** and marks the place". "Where a claim invokes worth, the semantics takes a **normative relation** \(\mathcal N\) as a declared input".
- **Searches of the whole file.**
  - "appropriat" occurs only at L161 and L514.
  - "certif" occurs at L73 ("act on an appraisal without certifying it"), L161 and L501 (a historical extension "does not certify" universality). Only L161 bears on restrictions.
  - "legitima" occurs only at L461 ("legitimate inputs" of execution families), which is unrelated.

**File 10.**
- **L41.** "An account is scoped to its contract and says so. … it is caught by the requirement that the exclusion be stated, and then by any criticism that supplies the excluded change."
- **L140 and L272.** As above.
- **Nothing on appropriateness.** File 10 has no "appropriat" and no counterpart of f11 L161 s3 or L514. Its Part XIV (L516–L523) has primitives, derivation and indices, but no declared inputs.
- **L176.** This is the nearest paragraph, and it is shared with f11 L163 apart from one added sentence.

**The packet (04e, O5).**
- **The readings.**
  - 1K A and 1K B mark AGREE.
  - 1C A and 1C B mark SILENT. Both quote L161 s3, and 1C B also quotes L514.
  - Among the auditors' final marks, Atria on A is SILENT, Atria on B is AGREE (through f11 L257) and Mimo on B is SILENT.
- **The WHYs of the SILENT readings all rest on "supplies no rule that certifies it".**
  - 1C A rejected its own AGREE reading "because the same sentence says the semantics "supplies no rule that certifies it", so the endorsement is the reader's, not the theory's."
  - 1C B rejected the non-vacuity route because "Tuesdays" would satisfy it too.
- **None of them engages L514's contrast** between "a verdict given the input" and "where the input is missing, the verdict is unsettled". 1C B quotes that sentence and reads it only as listing appropriateness "among its declared inputs".

## 4. The ruling, in the plan's words

The words ruled with are the plan's (second version) and the Stage 1 mark rules, quoted in section 2 of the brief.

### File-10 mark: AGREE (baseline). Stands.

Both 1K returns mark AGREE, which is the baseline, so the plan's correction rule cannot arise. The reply does not contest this (point 8). Its aside, that f10's texts "are no stronger" on "legitimate", is recorded and not ruled. The plan's rule fixes the file-10 mark at the baseline here whatever a fresh reading of file 10 would give. On that aside, file 10 could only be SILENT, and then any file-11 AGREE would be a move toward the thoughtful person, never away.

### File-11 mark: AGREE. Stands.

**Point (i), "This is a legitimate narrowing".** The mark rules name two routes to SILENT. Neither fits.

1. **SILENT "because it takes the deciding matter as an input the case leaves unstated".**
   - The theory does take the deciding matter as an input. L514 names "what makes a restriction appropriate (Part III)" among its stated inputs.
   - But the case states it. "Her account says why: the yeast that makes the gas works slowly in the cold." That is the part of her claim that L161 s3 calls "a substantive, criticizable part of the claim", and the semantics "records" it.
   - This route to SILENT fits O1, where Bruno's limits carry no ground, and the determination rules O1 SILENT. It does not fit O5.
   - The mark rules' own wording makes the case's statement of the input decisive. Here the input is stated.
2. **SILENT "because its sentences stop short of deciding it".**
   - L514 speaks to exactly this configuration: "A verdict that depends on one of these is a verdict given the input; where the input is missing, the verdict is unsettled".
   - Whether a narrowing is legitimate is a verdict that depends on "what makes a restriction appropriate". It is the verdict that depends on that input most directly. O1's SILENT is ruled on the same dependence.
   - The sentence contrasts a present input with a missing one. Where the input is missing, the verdict is "unsettled". Where it is present, the verdict is "given the input", which the sentence sets against "unsettled".
   - So a reading on which the verdict stays unsettled when the input is present denies L514's contrast in its own terms. That is the reading of the reply's point 6: "an abstention in both directions".
   - The sentences therefore do not stop short. With the input present, the theory's verdict on the narrowing is given with Greta's stated ground: the restriction is appropriate on the ground her account supplies, and that ground stays open to criticism.

**Point (ii), "The limit follows from a part of her account".** This is reached. The yeast is a component of her account, and its relation to the gas changes under the temperature edit. That is the causal-assignment signature of f11 L125 (= f10 L140). Her stated ground is that part. The reply does not rule this point SILENT, and relies on point (i) alone.

**"Same finding".** The theory's verdict on point (i) reaches the finding "legitimate". It adds two limits: given the stated ground, and open to criticism.
- The fixed verdict states its own legitimacy on the same ground: "The limit follows from a part of her account." The thoughtful person also does not check the yeast's biology. So the theory's "given the ground" is the fixed verdict's own reason, made explicit.
- A verdict "that reaches the fixed verdict's finding and adds a qualification, a limit or a more exact wording reaches the same finding."
- The same rule was applied to O40 ("absent a ranking"), and its converse to O35 and O1, where the input is missing.

**SPLIT considered, and not ruled.** SPLIT needs two supported readings "and the text leaves the choice between them open". It does not leave it open. L514's second sentence settles the choice, because the SILENT reading takes away its contrast for one of its three named inputs. The reply itself rejects SPLIT.

### The reply's points answered

- **Point 1, "each time withholds them".**
  - What the two sentences withhold is the semantics' own supply of the ground: "records and does not supply", and "supplies no rule that certifies it".
  - They do not withhold the verdict given a ground the claim supplies. L514 grants that verdict in the next sentence.
  - The order of the marks does not help the reply. SILENT comes before AGREE only if SILENT fits, and it does not fit (above).
- **Point 2, "classifies, does not manufacture", and the Part XI analogy.** The analogy runs the other way.
  - In Part XI, the inputs O and P are recorded and not judged: "Their declaration makes no claim that the aims are worth pursuing". The verdict that depends on them, Repair, is given with them.
  - Here, the input is the ground: what makes the restriction appropriate. It is recorded and not judged, so whether the yeast story is right stays "criticizable". The verdict that depends on it, whether the narrowing is appropriate, is given with it.
  - The worth of O and P is a different verdict. It depends on another input, \(\mathcal N\), which L27 and L447 take where "a claim invokes worth", and which L514's list does not include.
  - So the ruling's reading does not make L514 "yield *worth* verdicts on O and P". It makes L514 yield what it says: verdicts that depend on the listed inputs, given those inputs.
  - L161 s2's "An account at a stated scope answers the question asked at that scope" depends on the first half of the pair, "the scope of a contract". The reply's reading leaves the second half, "what makes a restriction appropriate", with no verdict that is ever "given the input".
  - No separate rule is needed to "manufacture" the verdict's content. The input is by its description what makes the restriction appropriate, so the verdict given it is that the restriction is appropriate on that ground.
- **Point 3, placement against criterion.**
  - The ruling does not read L161 s3's first clause as a rule of the semantics that certifies restrictions. It reads the clause as the reply does, as placement: appropriateness lives in the claim's criticizable content.
  - The verdict comes from L514, and L514 relativizes it to the claim's own ground. It does not certify: the semantics issues no verdict of its own on whether the ground is good.
  - On that reading the two clauses of L161 s3, and L514, cohere. The claim supplies the ground, the semantics records it and adds no certifying rule, and verdicts that turn on it are given with it.
  - The contradiction the reply finds is a contradiction of a reading the ruling does not adopt.
- **Point 4, the first condition of "Same finding".** This point holds only if the theory's verdict is "recorded, uncertified" and nothing more. L514 says the verdict is "given the input", so the finding is reached, and the limits are qualifications.
- **Point 5, non-vacuity.** The point is true and does not bear on the ruling.
  - The ruling does not rest on non-vacuity or non-circular dependence. It rejects the route through L257 for the reason the reply repeats.
  - What tells Greta's limit from the Tuesday limit in file 11 is L514's contrast: a ground stated against a ground missing. Greta's verdict is given, and the Tuesday limit's is unsettled.
  - So "No definition or condition of the theory separates Greta's limit from the Tuesday limit" is false of file 11.
  - L45's "scope-honesty lives in the record" is shared with file 10 (f10 L41). It does not bear on the two new sentences.
- **Point 6, "can never find a narrowing illegitimate".** The fixed verdict has no point on the Tuesday limit. The Tuesday limit is a contrast in the situation, and the marks compare findings on the fixed verdict's points.
  - That the theory leaves a groundless limit "unsettled", rather than illegitimate, is a limit of the theory. It is not a failure to reach "legitimate" where a ground is stated.
  - Recorded as a residual hazard, not a ground for the mark. On this reading the theory would also give a verdict "given the input" to a stated but poor ground. The only check on such a ground is criticism, which is L161 s3's "criticizable".
- **Points 7 and 8** follow from point 1 and from the file-10 mark, and are answered above.

### The rest of the row

- **Verdict: SAME.** AGREE in both files.
- **Passage: CHANGED (additive).** File 11's AGREE rests on f11 L161 s3 and L514, which have no counterpart in file 10 (M17 and M48, both CLAIM). File 11 keeps file 10's grounds (L125, L259, L45) and adds these two sentences. It does not alter the sentences file 10 relied on.
- **Direction:** none.
- **Kind:** no change.
- **Confidence: medium.**
  - The mark turns on reading two new sentences together. The wording of L161 s3 on its own invites the SILENT reading. Four of five earlier file-11 readings and this reply took it.
  - The ruling stands because L514's contrast and the mark rules' own SILENT criterion, "an input the case leaves unstated", both point the same way, and the SILENT reading answers neither.
  - A count of readers settles nothing (brief, section 7).

## 5. Change or not; away or not

- **Change of ruling: no.** Before and after: file 10 AGREE (baseline), file 11 AGREE, verdict SAME, passage CHANGED (additive) on f11 L161 s3 and L514, no direction, kind no change.
- **Away: no.** O5 is not a theory change away from the thoughtful person, so test (b) is not failed on this row. 05 rule 4 is not engaged, and the standing verdict is not applied again on account of O5.
- **To record** (05 rule 3; the fact that it came after the cross-examination):

````text
After the cross-examination (s87_xexam_mimo_O5, pass 2, attempt 4, accepted; "O5: RULING FALLS — file 11 SILENT"): re-read by a fresh determiner; RULING STANDS. File 10 AGREE (baseline, both 1K AGREE); file 11 AGREE; verdict SAME; passage CHANGED (additive), f11 L161 s3 and L514; no change; not away; test (b) unaffected. The reply reads L161 s3 and L514 as withholding a verdict on appropriateness even where the claim states its ground. L514 contrasts "a verdict given the input" with "where the input is missing, the verdict is unsettled", and the mark rules make SILENT on an input turn on an input "the case leaves unstated"; Greta's case states it ("her account says why"). The reply's Part XI analogy fits the ruling: inputs are recorded and not judged, and verdicts that depend on them are given with them. Worth is a different input (N; L27, L447). Confidence medium; the L161 s3 reading hazard stands as recorded.
````

## 6. Reconciliation with the earlier rulings

- **No earlier ruling has re-read O5 after a cross-examination reply.** No re-ruling of O5 exists in `results/` or in this folder.
- **S90 batch 1 and batch 2 rule nothing on O5.** The only entry that touches it is R10 (W57.1 + W32(b).1, f11 L161). Both S90 replies that examined R10 give it STANDS, and neither contests it:
  - Atria B1, batch 1, "Not contested";
  - Mimo B1, batch 2, point 4, which concerns the undefined phrase "the ground of its restriction" and "says expressly that no verdict moves".
- **R10's CASES AT RISK reads "O5 stays AGREE, and the hazard is closed."** That is the file-11 mark this re-reading upholds, so nothing needs reconciling.
  - R10 is typed CLAIM, with REASON WORD "clarification". The new sentences say in words what this ruling reads from L514 with L161 s3.
  - The KIND is not a finding that file 11 was SILENT on O5. The entry itself expects O5 to "stay" AGREE.
  - Had O5 fallen here, that line of R10 would have needed correcting. It does not.
- **Independence (05c item 7).** This reading was written without 06, 08, 09 or the O30 and O17 retry readings. It is to be set beside them only now that it is written. The disclosure in the header records the one sentence of R10's REASON that reports 06.
