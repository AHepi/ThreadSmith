# 03 Proposal: a correction lemma inside a common family, and why it does not make the record redundant

*Working file, 24 September 2026. Nothing in the repository was changed. Built on `01 text.md` and `02 models.md`. Re-read for this: draft 3 Parts V–VI and D3:L25, L151, L159, L255, L363, L516, L528, L562, L566, L602; file 00 L276–300 and L352–386, L1296–1304; the error-correction analysis (EC) section 2 and option (b); cases O1, O36, O45–O48 (S81 book), N1, N2, N7 (N-case book), D3-T `final.md`; Deutsch ch. 1 at pp.22, 25, 29. The Pinker folder was not opened. New script: `ratchet/models/m3_lemma_check.py`, output `m3_output.txt` (Python 3.11, standard library, about 35 seconds).*

**Tags.** [T] a line says it. [F] follows from quoted lines. [PROVED] a short general argument. [COMPUTED] exact output of a script on a stated finite model. [I] my inference.

---

## 1. Answers to the owner's three points

### (1) "A correction adds the failed case to the jobs, so any version that brings the mistake back fails." PARTLY.

- **Yes, at the failed case.** [F] (A) is universal over the contract (D3:L247–251), so any job whose contract holds the failed summer is one on which the old explanation is not an account. [PROVED, COMPUTED] Inside the later explanation's family, with the old one present as a member, adding that job shrinks Pres **strictly**, and the old explanation is the member that is excluded. Checked on 20 gardener families (every job set the old explanation does, every failed pair, plus random whole contracts): about 274,000 instances, no failure. Also the myth (60 instances) and the tilt (60 instances), no failure (M3 (1)).
- **No, beyond the failed case, when the jobs are the record.** [COMPUTED] Versions that do every recorded job and the failed one but repeat the old mistake at *another* early-variety summer survive: 18 of 52 (family U1), 71 of 208 (U2), 56 of 64 (a variety part that reads variety, rain and wind). Both amended myths that survive keep the original's error at the equator (2 of 2). The count reaches 0 only when the job added is the whole open question (13 survivors, 0 of them repeating the mistake) (M3 (i)).
- **And on the open question the failure added nothing.** [T] Reach "is fixed by \(E\) and the world, not by which jobs anyone has checked" (D3:L313). The old explanation was never an account on the open question. The failure showed that fact; it did not create a job. So the owner is right that a mistake cannot come back into an *account* of an unchanged question. But that holds as a fact nobody can see before a separating test (EC Situation 2: "blocked as a fact, unmarked in the record").
- **It is not a ratchet.** [T] A narrowing adopted after a failure is a legitimate new claim (D3:L159, L363, L602). [PROVED] By the same lemma, with the narrowed claim itself as the excluded member, dropping the failed job gives back the larger Pres (section 2, narrowing clause).

### (2) "A bad rescue registers as easier to vary, by the measure that defines a good explanation." NO.

- [T] No measure defines a good explanation. Draft 3 supplies no merit function (D3:L25), and Pres "grades nothing" (D3:L313).
- [COMPUTED] In one family holding all three rescues, the good rescue, the wet-spring rescue and the do-nothing patch are all members of Pres of the record plus the failed summer (52). Only the seed trial (35 left, good only) or the open question (13 left, good only) separates them, and that is (A), not variation (M3 (iii)).
- [PROVED, COMPUTED] On the same jobs, a family that extends the old explanation never has the smaller Pres. It was strictly larger for all 65,536 job sets in three families (M3 (ii)). That holds for the good rescue too.
- [COMPUTED] The record is symmetric under swapping rain and variety, so families that treat the two rescues alike give equal Pres: 1:1, 4:4, 6:6, 64:64. Otherwise the order flips with the menus: 1:96 against 64:1 (02, CX2–CX3). The do-nothing patch has Pres 1, the same as the good rescue.
- **The narrowing is the one place where "more versions fit" is a theorem.** [COMPUTED] E0 narrowed to the summers seen: Pres 1 against 0 with the failed summer. Situation 3 (the wet-spring rescue confined to the record): 52 against 13 with the open question. But Pres of the narrowed claim equals, exactly, Pres of the claim made before the failure. The good rescue confined to the same record sits in the same inclusion (M3, narrowing). The inclusion cannot tell a job dropped after a failure from one never claimed. Only the historical index (D3:L363) can, and the historical index is a record.
- [F] "Do-nothing" in the theory's sense cannot rescue at all. A commitment that does no work "meets (E) exactly when it meets (E) without \(d\)" (D3:L313). The companion clause below makes this exact: [COMPUTED] a rescuing addition is critical at the failed job, and all three rescues (good, wet spring, one-summer exception) are (M3, companion). The wet-spring clause is therefore not idle. Its fault is unfaithfulness on the open question.

### (3) "Can the file-00 limit be relaxed for an explanation and its own correction?" PARTLY: it cannot be relaxed, but it can be met.

- [T] File 00's reasons are structural (F00:L379, L381, L1300): there is no common set, counts change under redescription, and interpretation is held fixed. [F] None mentions authorship, so they apply to one's own correction as fully as to anyone's (01 (c)). [COMPUTED] Taken each with its own family, before and after are disjoint, and every count depends on the menus (02 §4).
- [PROVED] **Met, not relaxed.** Take the later explanation's declared family and require that one member restore the earlier organization. Then there is one organization, one interpretation and one family, which is file 00's premise (F00:L358), and (H) applies. What is new is that the earlier organization is a guaranteed witness, so the containment is strict. That answers file 00's "need not be strict" for exactly this case.
- [F] "Own" does no formal work. The hypothesis is structural: the family contains the earlier organization. A rival's extension of the same explanation meets it equally and gets the same result. What makes a correction someone's *own* is history (F11:L15). So a comparison restricted to one's own corrections would assume the record the owner wants to do without.

---

## 2. The proposal: wording, hypotheses, check

**Where.** Draft 3, Part VI.
- (a) A one-clause edit inside **Hard-to-vary** (D3:L313).
- (b) A new paragraph, **Correction in a common family**, placed directly after it and before Part VII.
- (c) Optional: a pointer sentence at the end of **Historical index** (D3:L363).

It is a lemma. It adds no condition and no measure.

**(a) Edit in D3:L313.** Replace "For explanatory jobs \(F\subseteq F'\)," with "For explanatory jobs \(F\subseteq F'\) (a job is a question, Part III),". Replace "the containment need not be strict;" with:

> the containment need not be strict, and it is strict exactly when some member of \(\operatorname{Pres}(F)\) is not an account on some job of \(F'\) (Correction in a common family);

**(b) New paragraph after D3:L313.**

> **Correction in a common family.** Let a later organization \(E_1\), with commitments \(\Gamma_1\), be declared with a family \(\mathcal V\) of organization edits that has a member \(v_0\) with \(E_{1,v_0}=E_0\): the earlier candidate's organization, each component it keeps with its earlier anchor, and the named background fixed. Where \(E_1\) only adds a block \(B\), \(E_0=E_1|(\Gamma_1\setminus B)\). Where it changes a component, \(v_0\) restores it. Let \(\operatorname{Account}(E_0,f)\) for every \(f\in F\), and \(\neg\operatorname{Account}(E_0,f^*)\). By (A), every job whose contract holds a pair at which \(E_0\) answers otherwise than the target is such an \(f^*\). Then
> \[
> v_0\in\operatorname{Pres}(F)\setminus\operatorname{Pres}(F\cup\{f^*\}),\qquad\text{so}\qquad\operatorname{Pres}(F\cup\{f^*\})\subsetneq\operatorname{Pres}(F).\tag{H\(^*\)}
> \]
> If also \(\operatorname{Account}(E_1,f^*)\) and \(E_0=E_1|(\Gamma_1\setminus B)\), then \(\operatorname{CriticalBlock}(B;\Gamma_1,f^*)\). *Proof.* (H) gives the containment. \(v_0\) is in \(\operatorname{Pres}(F)\) by the first hypothesis and not in \(\operatorname{Pres}(F\cup\{f^*\})\) by the second. For the block, \(\Gamma_1\in\mathsf S_{E_1,f^*}\) and \(\Gamma_1\setminus B\notin\mathsf S_{E_1,f^*}\) (B). ∎
>
> The same argument, with the identity edit as the witness, covers a narrowing. If \(E\) is an account on every job of \(F\) and not on \(f^*\), then \(\operatorname{Pres}(F)\supsetneq\operatorname{Pres}(F\cup\{f^*\})\). This holds whether \(f^*\) was held at an earlier index and dropped after a failure, or was never claimed. Which of the two it was is read from the historical index (Part VIII), not from \(\operatorname{Pres}\).
>
> (H\(^*\)) says what \(f^*\) excludes and nothing more.
> (i) A member of \(\operatorname{Pres}(F\cup\{f^*\})\) may answer as \(E_0\) does at a pair where \(E_0\) answers otherwise than the target, whenever no job of \(F\cup\{f^*\}\) holds that pair in its contract.
> (ii) For any \(\mathcal V_0\subseteq\mathcal V\), \(\operatorname{Pres}_{\mathcal V_0}(F)=\operatorname{Pres}_{\mathcal V}(F)\cap\mathcal V_0\). So where the earlier organization's own family sits inside \(\mathcal V\), the later organization is never the harder to vary on the same jobs.
> (iii) Two members of \(\mathcal V\) that are both accounts on \(F\cup\{f^*\}\) both belong to \(\operatorname{Pres}(F\cup\{f^*\})\). Only a job on which one is an account and the other is not separates them, and that is (A) on that job, not variation.
> (iv) If no member of \(\mathcal V\) gives \(E_0\), (H\(^*\)) does not apply, and the containment may be non-strict.
>
> (H\(^*\)) relates two subsets of one family of one organization under one interpretation, which is the premise of (H). It orders no candidates. It uses no fact about who wrote \(E_1\) or when. It holds for every declared \(\mathcal V\) that has the member \(v_0\).

**(c) Optional pointer, end of D3:L363.** "A narrowing that omits a job its candidate fails enlarges \(\operatorname{Pres}\) whether or not that job was ever claimed (Part VI); the index, not \(\operatorname{Pres}\), records that it was."

**Hypotheses, and why each is needed.** [COMPUTED, M3 (iv)]
- **The earlier organization is a member of the family.** Without it: a variety part with no "off" setting gives Pres 1 → 1, non-strict.
- **The earlier explanation does the old jobs.** Without it: take the old jobs to include one failed pair already. The job set then holds a pair where the earlier explanation is wrong, and adding a second failed pair gives 1 → 1, non-strict.
- **The earlier explanation fails the added job.** Without it: add a job nothing fails (another wet spring with the usual planting). This is file 00's own non-strict case: 1 → 1.
- **Redescription.** Splitting the rain part into two parts, or into five, changes the counts: 4 → 3 and 32 → 31, against 2 → 1 unsplit (02, E_bad in U1). It keeps the witness and the strictness (M3 (1), (1b)). That meets file 00's "splitting one feature into ten" (F00:L381).

**Why it does not rank different people's explanations (file 00's worry).**
1. Its conclusion is an inclusion between two subsets of **one** family. It is not a relation between two candidates. Limit (iii) says outright that two rescues in the same family are not separated by it.
2. Its hypothesis is a structural fact about content: the family contains the earlier organization. It is not a fact about authorship or time. A rival's extension of the same explanation gets the identical result, and the lemma never sets the two rescues against each other.
3. Where neither organization is an edit of the other (tilt against myth), there is no witness member, so it says nothing. It supplies no rule for building a common family. Building one is the cross-theory comparison F00:L1300 refused.
4. It is a statement that a witness exists, not a count. So "counting jobs is not a warrant" and F00:L1302 stand, and no choice of menus flips it. The strict inclusion held in all 20 families checked, 15 of them from the CX3 grid, where the counts flip both ways.

---

## 3. What it does in the test situations and cases

It is a lemma, so **no verdict moves**. What changes is which reasons are available, and which misreadings are blocked.

| Case | What (H\(^*\)) says | Direction |
|---|---|---|
| **Saint** (EC Sit. 1) | The idle-saint organization is the witness. The shrink at the failed Saturday is strict. The companion clause: to rescue, the changed saint must be critical at that Saturday, so it must do work, and then (F1) or non-circular dependence binds it (EC:Sit. 1). This ties draft 3's idle-part sentence (D3:L313) to correction. | None. Still blocked by (E). One reason added. |
| **North bed, open** (Sit. 2) | Strict with E0 excluded. Good, wet-spring and patch rescues are all kept on the record plus the failed summer (52). Limit (iii) says only a separating job decides. | None. Still "blocked as a fact, unmarked". No pre-test mark. |
| **Narrowed question** (Sit. 3) | The narrowing clause, with the rescue as witness: 52 against 13. This is the owner's "more versions fit", now proved. But it is identical to the good rescue honestly confined, and to a claim never made wider. It is read as a retreat only through the historical index. | Description moves toward; the verdict does not. Still passes (E), and its appropriateness is still unsettled (D3:L159, L516). |
| **N2** myth amended | Taking "sends the warmth nowhere" as the witness: 6 → 2, strict. That is the same shape as the tilt's own correction (4 → 2). Limit (i): both survivors keep the equator error. The lemma cannot give N2's No, which stays on (F1) and non-circular dependence (EC, Part C). | None. **Risk away** if strictness is read as merit. Limit (iii) and "orders no candidates" guard against that. |
| **O1** Bruno | Each restatement is a narrowing, and each is strict against the job it dropped, which is consistent with "each limit is honest taken alone". The lemma has no notion of a series, and it treats an honest limit the same way. | None. "The series is a retreat" stays SILENT. Only a record of runs (EC option (b)) moves it. |
| **N7** Maya | The narrowing clause holds for her limits whether or not they followed failures ("never claimed" is written in). So on the failure reading it does not mark her either, unlike option (b)'s risk. Bea's "fuller" account is reach, by (H) in her family. | None. It holds on both readings. |
| **N1** sun god | Nothing failed, so there is no instance. The god is idle (D3:L313). Had he been added to fix a failure, the companion clause says he would have to be critical at the failed job. | Unaffected. |
| **O36** | Nothing failed. The witness is always a *written* earlier organization, never an unwritten variant, so the lemma adds nothing about "a candidate nobody has written". | Unaffected. |
| **O45** | Deleting the first spring is not a failure at a pair, and the second spring was in \(\Gamma\) from the start (D3:L307). There is no added block and no failed job. | Unaffected. |
| **O47** | This is the reverse of a correction: the addition breaks a support. There is no failed job for E0, so there is no instance. Limit (ii) is about the *family*. The earlier organization stays in Pres while the extended candidate is no account, which is consistent with "the conclusion no longer follows". | Unaffected. Note: (ii) must not be read as "the extension is an account". |
| **O48** | Limit (iv): a version the declared family does not contain cannot be a witness. That matches "imaginable and not available". | Unaffected. It supports hypothesis (iv). |
| **D3-T** | This is selection, not edits, so the lemma does not apply directly. The analogue is Derivation 3 (D3:L566): the discarded design excludes itself at a tried setting and, as in limit (i), says nothing about survivors elsewhere. With no second passing design nothing is left open. | Holds. The same shape of reason. |

---

## 4. Gains, losses, and what kind of text it should be

**Gains.**
- Owner's point (1), at the failed job, becomes a theorem, with strictness guaranteed where file 00 left it open.
- Part VI gets its link to correction (the companion clause ties draft 3's idle-part sentence to rescue).
- Situation 3 gets an exact Part VI description, tied to Part VIII.
- The limits written into the text block three misreadings: that a bad rescue is easier to vary, that a correction is harder to vary than the original, and that one's own correction can be ranked.
- No new declared input, no merit function, no change to (E).

**Losses.**
- A paragraph for a fact whose proof is two lines.
- A reader may take strictness as merit. N2 shows the amended myth "shrinks like a correction".
- It does not make the record redundant. Its own narrowing clause shows that Pres cannot tell a dropped failure from a limit never claimed.
- No pre-test rejection of Situation 2.
- It does not reach runs (O1), blaming the background or the test (K3), or grain saves.
- \(\mathcal V\) is still not among the declared inputs (D3:L516; EC:L237). The lemma is safe because it holds for every \(\mathcal V\), but whoever declares \(\mathcal V\) can leave the witness out (hypothesis (iv)).

**Lemma, not a Part VI measure, not a condition of (E).**
- **A lemma** is a truth that follows from (H), (A) and (B) with no new premise, for every declared family. It cannot flip any case, since it changes no definition. It only states consequences already true.
- **A Part VI measure** (a size of Pres, or an order by it) needs a measure on \(\mathcal V\), which is a merit function (D3:L25, L516). Its outputs flip with the menus (1:96 against 64:1; patch 1 against 24,576; myth 2 against 18) and with redescription (2 → 1, 4 → 3, 32 → 31 for one rain part written as one, two or five).
- **A condition of (E)** would flip cases.
  - "A correction must be harder to vary than what it corrects" refuses the neighbour's-variety rescue: on the old jobs every extension is at least as easy to vary (limit (ii); 1 → 2 in 02 §4).
  - "Adding the failed job must shrink Pres" is always met, by the lemma, so it would do nothing.
  - Any Pres test separating good from bad rescues fails on the symmetric record (1:1, 4:4, 6:6, 64:64).
  - Any such condition would place an undeclared input inside (E).

---

## 5. What stays uncertain

1. **What a job is.** "Explanatory job" is undefined in the texts (01 (a)). The proposal makes it a question. The models read jobs as single pairs, with Account as (A) alone. (H\(^*\)) holds on either reading. The hybrid counts and the Pres sizes depend on it, and (F1) could shrink the sets (the amended myth may have an empty Pres under full (E)) without touching strictness.
2. **Whether the witness member always exists.** A transport is part of a candidate, not of an organization (D3 Part V). A correction that re-anchors a kept component may not be undone by an *organization* edit. File 11 never defines \(E_v\) beyond "organization edits" (F11:L301). If so, the family must be one of candidate edits.
3. **Background in the companion clause.** Whether \(E_1|(\Gamma_1\setminus B)=E_0\) holds when removing \(B\) alters the named background.
4. **Whether the owner wanted a mark, not a truth.** The lemma cannot give point (2). A mark of retreat needs a record (EC option (b)), which is a separate decision this proposal neither needs nor replaces.
5. **The evidence behind the limits.** The limits are shown by finite toy models: counterexamples, not frequencies. Draft 3 is not frozen, and its line numbers may move.
