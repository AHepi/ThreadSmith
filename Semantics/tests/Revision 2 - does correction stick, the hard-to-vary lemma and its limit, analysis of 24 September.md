# Revision 2 - does correction stick, the hard-to-vary lemma and its limit, analysis of 24 September

**DRAFT — analysis for the owner; not frozen; made by Claude subagents**

*What this is.* The owner's position: a record of rescues is redundant. Once an explanation is rescued, the mistake should not be able to creep back in, and good explanations make bad ones harder to fit by definition. Concretely: (1) a correction adds the failed case to the explanation's jobs, so any version that brings the mistake back fails; (2) a bad rescue (a do-nothing patch, or a narrowed question) registers as making the explanation easier to vary, by the same measure that defines a good explanation; (3) file 00 limited the hard-to-vary comparison to a fixed organization, interpretation and variation family, and said the containment may be non-strict, so can that limit be relaxed for comparing an explanation with its own correction, without ranking different people's explanations? This note checks the position against file 11, draft 3 of file 13, file 00 and the error-correction analysis of 24 September, with a gardener's north bed as the running example, and proposes a lemma for draft 3, Part VI.

The body is the checked result: a proposal (Appendix C), attacked against the texts (Appendix D) and by counterexample models (Appendix E), with every correction applied and listed in the body's section 0. Appendix A is the reading of the texts and Appendix B the first models, with their scripts inlined. The appendices are the working files copied unchanged, except that one book quotation in Appendix A is shortened (marked), and on 25 September the quotations chained with it were paraphrased (dated line beside them). References to "01" to "04b" are to Appendices A to E. The scripts of every round are also in the folder `Revision 2 - does correction stick - model scripts/` beside this note: `models/` (Appendices B and C), `attack/` (Appendix E) and `check/` (the body). References to `ratchet/models/`, `ratchet/attack/` and `ratchet/check/` are to those subfolders; each script runs with Python 3.11 and the standard library from its own folder, and every saved output was reproduced byte for byte on 24 September 2026. Nothing here changes the theory text. Draft 3 of file 13 is not frozen, and its line numbers are those of the file as read on 24 September 2026. Every case movement is a reading, not a test result.

---

## 05 Checked result: does a correction stick? The hard-to-vary lemma and its limit

*Working file, 24 September 2026. This is `03 proposal.md` after the text attack (`04a`) and the model attack (`04b`), with every correction applied. Read for this: 01, 02, 03, 04a and 04b in full; draft 3 (D3) at L13, L25, L43, L55, L69, L91, L103, L151, L159, L161, L189, L195, L231, L247, L255, L265, L273, L277, L285–313, L363, L421, L447, L516, L518, L528–540, L556–570, L602 and L606; file 00 (F00) at L283, L294, L356–383 and L1298–1302; file 11 (F11) at L15, L301 and L315; the change list (CL) at L1138; the error-correction analysis (EC), section 2 and option (b); the cases O1, O36, O45–O48, N1, N2, N7 and D3-T `final.md`; Deutsch ch. 1 at pp.25, 28, 29 and 31, by page marker. All twelve earlier scripts were re-run, and every output is byte-identical to the saved one. One new script, `ratchet/check/r1_repaired_wording.py` (output `r1_output.txt`; Python 3.11, standard library, under 2 seconds), runs the repaired wording against the counterexamples of 04b. The Pinker folder was not opened. Nothing in the theory text is changed by this note. Draft 3 is not frozen; its line numbers are those of the file as read today.*

**Tags.** [T] a line says it. [F] follows from quoted lines with no added premise. [PROVED] a short general argument, given here. [COMPUTED] exact output of a script on a stated finite model. [I] my inference; it could be wrong.
- "(A) only" marks a number from the models that read Account as answer agreement at single pairs (02, 03).
- "full (E)" marks a number from `fe.py` (04b). It also checks (F1), (F2) and non-circular dependence, with Part II's solution semantics, and a job is a question whose contract holds the baseline summer.

**The example.**
- **E0.** "The south wall gets the most sun, so the south bed ripens first." It held for the summers seen. One year the north bed ripened first.
- **Good rescue.** The neighbour planted an early-ripening variety along the north side. It can be checked. It predicts north-first in a dry spring too, and it predicts that the effect goes if the seed changes.
- **Bad rescue.** "In a wet spring the north bed ripens first." It fits only the failure, and "windy spring" would fit as well.
- **Narrowing.** "My explanation only covered the five summers seen." The failed summer is one of the five, so taken literally this rescues E0 only together with a patch: that is EC's Situation 3, the wet-spring rescue confined to the record. Read as "the summers before the failure", it rescues E0 alone (02's E_narrow).
- **Jobs in the full-(E) models.**
  - j_seen = {a recorded summer, the shading test}.
  - j_eshade = {baseline, a shaded year with the early variety}. E0 answers north, which is right.
  - j_fail = {baseline, the failed summer}.
  - The open question holds all 16 settings of rain, wind, variety and shade.
- **Two ways to write the good rescue.** Both give the same answer at all 16 settings, and both are accounts on the open question (04b A1).
  - **Emb-2, a changed rule.** "North first if the neighbour planted early, otherwise the sunnier bed." It reads the planting, which each summer sets.
  - **Emb-1, a mechanism.** "An early variety switches on a variety effect, and the effect makes the north bed first." The effect is a new variable, which the transport reads from the garden itself.

---

### 0. What changed after the attacks

Every verdict of 04a and 04b is applied. "Repaired" means a minimal hypothesis was added and the counterexample was re-run against it (R-numbers are sections of `r1_output.txt`). "Withdrawn" means the claim is dropped.

| # | 03 claim | Attack | What 05 does | Check |
|---|---|---|---|---|
| 1 | (H\*)'s witness is "E₁,v₀ = E₀", an organization | CE1: under full (E) with one interpretation, the switched-off and the deleted versions fail j_eshade, which E0 does. Result 1 → 1. Read literally, the hypothesis cannot be met, since an organization edit cannot delete a port | **Repaired.** The witness hypothesis is stated at the level of Account for one member v₀. A new bridge clause says when v₀ carries E0's verdicts | R1: 0 failures in 5,880 instances (10 families, 2 readings, 294 pairs (F, f\*) each). CE1: the hypothesis is false and the result is 1 → 1. Emb-2 and the candidate-edit family: the hypothesis is true and the result is 2 → 1. R2: the bridge holds for Emb-2 on all 32,768 contracts and fails for Emb-1 |
| 2 | "Where E₁ only adds a block B, E₀ = E₁\|(Γ₁∖B)" | 04a 6′; CE4: an added block cannot rescue a determined wrong answer (0 of 256, 0 of 65,536, 0 of 3,000) | **Withdrawn** | a3 re-run |
| 3 | Companion: a rescuing block is critical at f\*; "all three rescues are" | CE5: under Part II deletion the block is critical at every job; the verdict depends on the restriction operation | **Withdrawn.** Its true form is (B) together with D3:L313's idle-part sentence, and it applies only where E0 said nothing at f\* | a3 re-run, part (c) |
| 4 | Narrowing clause | CE3: fails without the identity edit in 𝒱 | **Repaired:** "if 𝒱 contains the identity edit" | R3: with the identity, 32 of 32 instances strict (full (E)) and 45 of 45 ((A) only). Without it, 4 of 32 and 12 of 32 |
| 5 | Pointer (c) | Contradicts itself; "the index records" is wrong; needs the identity | **Repaired** as in 04a 13, with the identity | R3 |
| 6 | Limit (i), "may … whenever" | 04a: needs Derivation 3's qualification. 04b: the numbers stand | **Reworded:** a member is excluded only through pairs the jobs hold, and what survives elsewhere is fixed by 𝒱 | R6: on the same jobs, 56 of 64 in the rich family and 0 of 1 in the poor one |
| 7 | Limit (ii), "the later organization is never the harder to vary" | REFUTED (04a 8; CE7) | **Replaced:** (H\*) does not compare E with E0 | A4(i): 1 → 2, 4 → 2, 64 → 2 |
| 8 | Limit (iii), "that is (A) on that job" | CE6, CE13 | **Corrected:** "(E) on that job" | a5, a6(e) re-run |
| 9 | Limit (iv), and "no choice of menus flips it" | (iv) UPHELD; the rest REFUTED (CE8, CE2) | **Reworded:** whether a witness exists is a fact about 𝒱 and about how E is written | A4(iv); R1 |
| 10 | Edit (a) parenthesis, "a job is a question" | A new definition | **Dropped.** The iff is kept | R1: 0 cases where strictness and the witness come apart |
| 11 | Closing: "one interpretation … orders no candidates … who wrote E₁" | UPHELD for (H\*); REFUTED for the paragraph while (ii) stood | **Kept,** without "one interpretation". "Earlier", "later" and "written" are replaced by structural hypotheses | — |
| 12 | §1(1): "274,000 instances, no failure" | No evidential weight (CE11) | **Dropped as evidence** | a6(c) |
| 13 | §1(1): "a legitimate new claim" | CORRECTED | "A new claim at a new index; recorded, not forbidden, not certified" | D3:L159, L602 |
| 14 | §1(1): "the member excluded" | Wording | "a member excluded" | — |
| 15 | §1(2): "[T] No measure defines a good explanation" | Tag | [F] | — |
| 16 | §1(2): "only the seed trial or the open question separates them, and that is (A)" | CE13; 04a 2b | Four single summers separate them, and they do it through (E) | a6(e), a5 |
| 17 | §1(2): "an extension never has the smaller Pres" | True only inside an embedding (CE7) | Kept as a fact of the embedding and kept out of the theory text | A4(i) |
| 18 | §1(2): symmetric pairs "1:1, 4:4, 6:6, 64:64" | CE14: 64:64 (and V+W/W+V) compare a family with itself | 1:1, 4:4, 6:6 only | a6(b) |
| 19 | §1(2): the narrowed Pres "equals, exactly, Pres of the claim made before the failure" | 04a 2e | "Equals Pres of the record before the failure, and contains Pres of the earlier claim on the open question" | — |
| 20 | §1(3): "Met, not relaxed"; PARTLY | 04a 3b; CE1 | **NO.** The limit is not relaxed, the lemma does not compare the two, and the witness depends on the writing | R1, R2 |
| 21 | §1(3): "before and after are disjoint" | A menu artifact (CE10) | Dropped | A4(iii) |
| 22 | §3 rows: N2, O1, N7, N1, O36, O48, Saint, Situation 3 | CORRECTED (04a 5) | Applied in section 3 | — |
| 23 | §4: "it cannot flip any case, since it changes no definition" | True only without (a)'s parenthesis | Now true: the parenthesis is dropped | — |
| 24 | §4: "a measure on 𝒱 … is a merit function" | Overstated | "An order of candidates by a measure on 𝒱 would be" | — |
| 25 | §4: "'Adding the failed job must shrink Pres' is always met" | REFUTED (CE8, CE1) | As a condition it would turn on the writing and the menus | R1 |
| 26 | §4: "Part VI gets its link to correction" | (D) already records it | "States a link that (D) records" | — |
| 27 | §2, third control ("a job nothing fails") | CE12: it dropped two hypotheses at once | The clean control is used | R5: 2 → 2 |
| 28 | §5.1: "(F1) could shrink the sets without touching strictness" | False if (F1) empties Pres(F) | Handled by the Account-level hypothesis | — |
| 29 | 02: deletion read as switch-off; (A) at single pairs; label errors | 04b §3 | Carried into the answers. 02 stands as written in its appendix | a0 (25 of 25 re-derived) |
| 30 | EC option (b)'s marks | CE15: they depend on "deleted" meaning "switched off" | Reported (sections 4 and 5), not changed here | a6(g) |

---

### 1. Answers to the owner's three points

#### (1) "A correction adds the failed case to the jobs, so any version that brings the mistake back fails." PARTLY.

- **At the failed summer, yes, and no record is needed.** [T, F] (A) holds "For every (a,b) ∈ C" (D3:L247). So any candidate that answers "south first" at the failed summer is no account on any job whose contract holds that summer: a rival, a rescue, or E0 offered again. This holds while the job is kept.
- **Whether the failed job is what excludes the old explanation depends on how the correction is written.** [COMPUTED, full (E)] Adding the failed job strictly shrinks the fitting versions exactly when some version does the old jobs and fails the new one: the witness.
  - Written as a changed rule (Emb-2), the old rule is such a version. On F = {j_seen, j_eshade}, adding the failed summer gives 2 → 1 (R1). Its Account verdict equals E0's on all 32,768 contracts that hold the baseline (R2).
  - Written as a mechanism (Emb-1), with the variety effect read from the garden under the correction's own interpretation, no version carries E0's verdicts. Once the old jobs include the shaded early-variety year, a job E0 did, no version is a witness either, and the result is 1 → 1 (CE1, R1). With only the recorded summers and the shading test, the switched-off version still happens to be a witness (2 → 1, A1).
    - With the part switched off, the version asserts "no variety effect". It then fails the shaded early-variety year, which E0 passed.
    - Its verdicts differ from E0's on 1,920 of the 32,768 contracts. With the part deleted, they differ on 2,040 (R2).
    - So in Emb-1, what keeps the mistake out at the failed summer can be an old job, not the failure.
- **Beyond the failed summer, no.** [COMPUTED]
  - Take the rich family sun′ × var[V, W, Wi] (1,024 versions, the correction's transport). Under full (E), 56 of the 64 versions that do the recorded summers and the failed one repeat E0's error at another early-variety sunny summer. With the seed trial added, 24 of 32 still do. On the open question, 0 of 1 (R6, A7).
  - In the poor rule family, 0 of 1 on the same jobs.
  - Under (A) only, the counts are 18 of 52, 71 of 208 and 56 of 64 (02, re-derived in 04b A0).
  - What the jobs leave open is fixed by the family, as what a history leaves open is fixed by a population (D3:L566–570).
- **On the open question the failure added nothing.** [T] Reach "is fixed by E and the world, not by which jobs anyone has checked" (D3:L313). E0 was never an account there: the failure showed that and created no job. So the mistake cannot re-enter an *account* of the unchanged open question. But nobody can see this before a separating test: "blocked as a fact, unmarked in the record" (EC, Situation 2).
- **It is not a ratchet.**
  - [T] "a narrowing adopted after a failure is a new claim at a new index" (D3:L159). It is recorded, not forbidden: only the unrecorded change is goalpost-moving (D3:L602). It is not certified either: "the semantics records the restriction and supplies no rule that certifies it" (D3:L159).
  - [COMPUTED] Narrowing the corrected rule back to the summers seen readmits the version that answers as E0: 1 → 2 (A7).

#### (2) "A bad rescue registers as easier to vary — more versions fit — by the same measure that defines a good explanation." NO.

- **No measure defines a good explanation in the theory.** [F] Draft 3 does not use the phrase. Pres "grades nothing" (D3:L313). The semantics supplies "no merit function" (D3:L25, L516). "By definition" is Deutsch's glossary, "hard/easy to vary while still accounting for what it purports to account for" (D p.31), and draft 3 does not adopt it.
- **On the record plus the failed summer, one family holds all three rescues.** [COMPUTED]
  - The good, wet-spring and one-summer rescues are all among the 52 fitting versions of U1 ((A) only). Under full (E), the good and wet-spring rescues are both among the 4 of sun′ × var[V, W] (a5).
  - What separates them is a job holding a pair where they differ. Four single summers do it: the seed trial, its windy twin, and a wet spring with the usual planting, calm or windy (a6(e)).
  - A job can also separate two versions with identical answers, through (F1) or (F2) (a5(1)). Either way it is (E) on that job, not a count.
- **Inside E0's own family, the bad rescue registers as a shrink.** [COMPUTED] Let E0's sun part read shade and rain. That is one organization, one interpretation and one family, which is file 00's premise. The wet-spring rescue is then a member, and adding the failed summer takes the fitting set from 4 to 2 (A4(ii)). By the measure, it is harder to vary, not easier.
- **Between separately declared families, the direction is a menu fact.** [COMPUTED]
  - The correction comes out easier to vary (1 → 2) or harder (4 → 2, 64 → 2) according to the menus (A4(i)).
  - Where the record cannot tell rain from the variety, families built alike give equal Pres: 1:1, 4:4, 6:6.
  - Otherwise the order flips with the menus: 1:96 against 64:1, and the "good" family of the 64:1 row also holds the rain rescue (CE14).
  - The one-summer patch has Pres 1 in its single-exception family, the same as the good rescue. In an any-predicate family it has 24,576.
- **A do-nothing patch cannot rescue at all.** [T] A commitment that does no work leaves a candidate that "meets (E) exactly when it meets (E) without d" (D3:L313). The one-summer exception does work at the failed summer. [I] Under full (E) it may already fail non-circular dependence there, since an account "whose only substantive component restates the answer it was asked for" fails it (D3:L273). That turns on the grain reading EC left open.
- **The narrowing is the one place where "more versions fit" is a theorem, and then only with the identity edit in the family.** [PROVED, COMPUTED]
  - Taken literally ("the five summers seen", the failed one included), it rescues only a patched explanation: Situation 3. The wet-spring rescue confined to the record has a strictly larger Pres than on the open question (U1, (A) only: 52 against 13).
  - Read as "the summers before the failure", it rescues E0 alone. Its Pres is strictly larger than with the failed summer (R3: 32 of 32 instances under full (E); without the identity, 4 of 32 and 12 of 32). It equals Pres of the record before the failure, and it contains Pres of the earlier claim on the open question.
  - Either way, a claim honestly narrow from the start sits in the same inclusion. Only the record of indexed claims tells a retreat (D3:L55, L161, L602).

#### (3) "Can the file-00 limit be relaxed for comparing an explanation with its own correction, without ranking different people's explanations?" NO.

- **File 00's reasons are structural.** [T, F] There is no common set; "It says nothing by itself about two different theories using different interpretations or different variation families" (F00:L379). Counts change with redescription: "splitting one feature into ten cannot create knowledge" (F00:L381). The interpretation is held fixed (F00:L358, L1300). None of these mentions authorship, so each applies to one's own correction.
- **The checked lemma does not relax the limit and does not make the comparison.** [F] It compares two sets of jobs inside one declared family, in which one member may carry E0's verdicts. That meets file 00's premise. It is not a comparison of E0 with the correction (04a 3b).
- **The witness itself depends on the writing, which is file 00's redescription worry coming back.** [COMPUTED] The same correction has a witness when written as a changed rule (2 → 1). Written as a mechanism under one interpretation, it has none (1 → 1) (CE1, CE2; R1, R2). One way to restore the witness there is a family that holds E0 with its own transport (R4: 2 → 1). Whether a family of "organization edits" may do that is open (section 5).
- **Between separately declared families there is no comparison to be had.** [COMPUTED] Easier or harder flips with the menus (A4(i)).
- **"Own" does no formal work.** [F] The hypotheses are structural, so a rival's correction written the same way gets the same result. What makes a correction someone's own is history: provenance is told "by their histories, not their outputs" (D3:L13; F11:L15). A comparison confined to one's own corrections therefore presupposes the record the owner wants to drop.

---

### 2. The checked wording

**Where it goes.**
- Draft 3, Part VI: a one-clause edit inside **Hard-to-vary** (D3:L313), and a new paragraph directly after it, before Part VII.
- Optionally, a pointer at the end of **Historical index** (D3:L363).

It is a lemma. It adds no condition to (E), no measure and no declared input.

**(a) Edit in D3:L313.** Replace "the containment need not be strict;" with:

> the containment need not be strict, and it is strict exactly when some member of \(\operatorname{Pres}(F)\) is not an account on some job of \(F'\) (Witness in a common family);

**(b) New paragraph after D3:L313.**

> **Witness in a common family.** Let \(\mathcal V\) be a declared family of organization edits of \(E\), \(F\) a set of jobs and \(f^*\) a job. If some \(v_0\in\mathcal V\) satisfies \(\operatorname{Account}(E_{v_0},f)\) for every \(f\in F\) and \(\neg\operatorname{Account}(E_{v_0},f^*)\), then
> \[
> v_0\in\operatorname{Pres}(F)\setminus\operatorname{Pres}(F\cup\{f^*\}),\qquad\text{so}\qquad\operatorname{Pres}(F\cup\{f^*\})\subsetneq\operatorname{Pres}(F).\tag{H\(^*\)}
> \]
> By (A), every job whose contract holds a pair at which \(E_{v_0}\) answers otherwise than the target is such an \(f^*\). *Proof.* (H) gives the containment, and the hypotheses put \(v_0\) in the first set and not in the second. ∎
>
> *Another candidate as witness.* Let \(\mathcal E_0=(E_0,p,t_0,\Gamma_0)\) be a candidate for \(p\). Suppose the organization, transport and commitments with which \(E_{v_0}\) is assessed in \(\mathcal V\) are those of \(\mathcal E_0\), except for ports that every pair of every contract sets through \(\tau\) or \(\sigma\), on which no relation of \(E_{v_0}\) depends, and to which \(\pi\) and the port translations of \(t_0\)'s anchors are extended by the identity. Then \(\operatorname{Account}(E_{v_0},f)\iff\operatorname{Account}(\mathcal E_0,f)\) for every job \(f\). *Proof.* At each pair, and with any block of \(\Gamma_0\) deleted, the solutions of \(E_{v_0}\), their images under \(\pi\) and the projections of the anchors are those of \(\mathcal E_0\) with the added ports at the pair's values. So the answers, and the comparisons of (F1), (F2) and non-circular dependence, coincide. ∎ The condition fails when \(E\) adds a port that its transport reads from the target's state and not from the pair, as when a change posits a mechanism with its own variable. A member with that part deleted leaves the port free, and one with it set to a constant asserts a value. (F2) compares either with the target, where \(\mathcal E_0\) asserted nothing. Then no member that keeps \(E\)'s transport need have \(\mathcal E_0\)'s verdicts, and (H\(^*\)) may have no witness.
>
> If \(\mathcal V\) contains the identity edit, and \(E\) is an account on every job of \(F\) and not on \(f^*\), the identity is a witness: \(\operatorname{Pres}(F)\supsetneq\operatorname{Pres}(F\cup\{f^*\})\). This is so whether \(f^*\) was claimed at an earlier index and later omitted, or never claimed. Which of the two it was is read from the record of indexed claims (Part III, Scope; Part VIII, Historical index; Derivation 7), not from \(\operatorname{Pres}\).
>
> (H\(^*\)) says what \(f^*\) excludes and nothing more.
> (i) \(\operatorname{Pres}(F\cup\{f^*\})\) excludes no member for what it does at a pair that no job of \(F\cup\{f^*\}\) holds in its contract. Whether \(\mathcal V\) has a member that answers there as the witness does is fixed by \(\mathcal V\), as what a history leaves open is fixed by a population (Derivation 3).
> (ii) (H\(^*\)) compares \(\operatorname{Pres}(F)\) with \(\operatorname{Pres}(F\cup\{f^*\})\) in one family. It does not compare \(E\) with \(\mathcal E_0\). They are different organizations with different families, and it gives no ground for calling either harder to vary than the other.
> (iii) Two members that are both accounts on every job of \(F\cup\{f^*\}\) both belong to \(\operatorname{Pres}(F\cup\{f^*\})\). Only a job on which one meets (E) and the other does not separates them.
> (iv) Whether a witness exists is a fact about the declared \(\mathcal V\) and about how \(E\) is written. One change may have a witness when written as a changed rule over ports the pairs set, and none when written as a mechanism with its own variable. A family whose menus lack the earlier setting has none. Without a witness the containment may be non-strict.
>
> (H\(^*\)) relates two subsets of one declared family, which is the premise of (H). It orders no candidates, counts nothing, and uses no fact about who wrote any candidate or when.

**(c) Optional pointer, at the end of D3:L363.**

> A set of jobs that omits one its candidate fails has, when \(\mathcal V\) contains the identity edit, a strictly larger \(\operatorname{Pres}\) than the same set with that job (Part VI), whether the job was dropped after a failure or never claimed; which of the two it was is shown by the record of indexed claims, not by \(\operatorname{Pres}\).

**Hypotheses: what each one blocks, and the re-run.** [COMPUTED unless marked]

| Hypothesis | Counterexample it blocks | Without it | With it |
|---|---|---|---|
| v₀ is an account on every job of F, under the interpretation 𝒱 gives it (replaces "E₁,v₀ = E₀") | CE1 (Emb-1, one interpretation); 03 §5.1 ((F1) empties Pres(F)) | 1 → 1 with the switched-off or deleted version named as v₀ (A1) | R1: in Emb-1 the hypothesis is false for every member, and the lemma claims nothing. Across all families, 0 failures in 5,880 instances |
| v₀ is not an account on f\* | The clean control | 2 → 2 at pair level, and 2 → 2 under full (E) for {baseline, shade, wet spring} (A6(a), R5) | — |
| A witness exists in 𝒱 (limit (iv)) | CE8 (a menu without "off"); CE2 (Emb-1) | 1 → 1 (A4(iv), A1) | Stated as a limit, not assumed away |
| Bridge: the added ports are set by the pair, and no relation depends on them | CE1 | Emb-1's switched-off version differs from E0 on 1,920 of 32,768 contracts, its deleted version on 2,040 (R2) | Emb-2's version differs on 0 of 32,768 (R2). [PROVED] above |
| Narrowing clause: the identity edit is in 𝒱 | CE3 | 4 of 32 and 12 of 32 instances strict (full (E)); 6 of 45 ((A) only) (R3) | 32 of 32 and 45 of 45 (R3) |
| (a) iff: F ⊆ F′ | — | — | R1: strict exactly when a witness exists, in every instance |

**Withdrawn, and why.**
- **"Where E₁ only adds a block B, E₀ = E₁|(Γ₁∖B)."** [PROVED, COMPUTED] Under (O), a block added beside a component that fixes a wrong answer can only shrink the solutions. So it can never turn a determined wrong answer right (CE4: 0 of 256, 0 of 65,536 and 0 of 3,000 relations). A rescue of a mistake changes a component.
- **The companion clause** ("a rescuing block is critical at the failed job"). As a conditional it is true, since it is (S) and (B). It is withdrawn for three reasons:
  - Under Part II deletion, its hypothesis holds only where E0 said nothing at the failed pair, not where E0 was wrong (a3(c)). The gardener's failure is a wrong answer, so the clause never applies to her.
  - Under deletion, the rescuing block is critical at every job, old ones included, so criticality marks no rescue work. Under switch-off, it is still critical at a job E0 already did (CE5).
  - What it was meant to add, that an idle part cannot rescue, is already in D3:L313.

  The minimal repairs ("E0 undetermined at f\*", or a declared switch-off restriction) leave a clause with nothing to say about the cases.
- **"No choice of menus flips it"** (CE8, CE2).
- **Old limit (ii)**, where a set identity was used to compare E₁ with E₀.

**Why it does not rank different people's explanations.**
1. Its conclusion is an inclusion between two subsets of one declared family, not a relation between two candidates. Limit (ii) says so, and limit (iii) says that two members that both survive are not separated by it.
2. Its hypotheses are Account facts about one member and structural facts about ports and anchors, not facts about authorship or time. A rival's version of the same correction, written the same way, gets the same result.
3. It supplies no rule for building a common family. Where no declared family holds both explanations (tilt against myth), it says nothing, and building one would be the comparison F00:L1300 refused. If someone declares a family wide enough to hold both, its conclusion is still about job sets.
4. It asserts that a witness exists and counts nothing, so "counting jobs is not a warrant" (D3:L313) and F00:L1302 stand. Whether the witness exists does depend on the menus and the writing (limit (iv)), which is one more reason it cannot serve as a grade.

**What kind of text.**
- **A lemma.** It follows from (H), (A) and the definition of Pres with no new premise. The bridge follows from Part II's solution semantics and Part V's conditions. With (a)'s parenthesis dropped it changes no definition, so it cannot flip a case.
- **Not a Part VI measure.** An order of candidates by a measure on 𝒱 would be a merit function (D3:L25, L516). The counts flip with the menus (1:96 against 64:1; the patch 1 against 24,576; the amended myth 2 against 18). They also flip with redescription: one rain part written as one, two or five parts gives 2 → 1, 4 → 3 and 32 → 31.
- **Not a condition of (E).**
  - "A correction must be harder to vary than what it corrects" turns on the families. With 1 → 2 it refuses the good rescue; with 4 → 2 and 64 → 2 it passes it (CE7).
  - "Adding the failed job must shrink Pres" refuses the neighbour's-variety rescue written as a mechanism and passes it written as a rule (CE1, CE2). It also refuses it under a menu without "off" (CE8).
  - "Pres must separate good from bad rescues" fails on the symmetric record (1:1, 4:4, 6:6).
  - Each of these would put an undeclared input, 𝒱, inside (E).

---

### 3. The three test situations and the named cases

It is a lemma, so **no verdict moves**. What changes is which reasons are available and which misreadings are blocked.

| Case | What the checked wording says | Direction |
|---|---|---|
| **Saint** (EC Situation 1) | The patched saint is no account on any contract that holds the failed Saturday: (F1) fails if the mood is tied to nothing, and non-circular dependence fails if it is read off the sales (EC). In a family of the baker's explanation that contains the identity, adding the failed Saturday shrinks Pres strictly, with the original as the witness, provided it did the earlier Saturdays. That the idle saint could not rescue is D3:L313, not the lemma. Precision (04a): (F1) binds every active component, and giving the saint work makes its relation no longer full, so (F1) can fail | None. Still blocked by (E) |
| **North bed, open** (Situation 2) | Written as a changed rule, the version carrying E0's verdicts is the witness, and the failed summer shrinks Pres strictly (2 → 1, full (E)). Written as a mechanism, no version carries E0's verdicts. With the shaded early-variety year among the old jobs, the failed summer then excludes nothing new (1 → 1): an old job already excludes the mistake. On the record plus the failed summer, the good, wet-spring and one-summer rescues all stay in Pres (52 of 1,088 in U1, (A) only; good and wet-spring among 4 in sun′ × var[V, W], full (E)). Limit (iii): only a job where they differ decides, through (E) | None. Still "blocked as a fact, unmarked in the record". No pre-test mark |
| **Narrowed question** (Situation 3) | The narrowing clause, with the identity: the wet-spring rescue confined to the five recorded summers, the failed one included, has a strictly larger Pres than on the open question (U1, (A) only: 52 against 13). The good rescue confined to the same record, and a claim never made wider, sit in the same inclusion. A retreat is read only from the record of indexed claims | The description moves toward; the verdict does not. It passes (E) only on EC's qualified reading: "Yes, in draft 3, on the reading of (F1) that Grievance 1 gives", with non-circular dependence's second sentence unsettled. Its appropriateness is unsettled (D3:L159, L516) |
| **N2** (myth amended) | Under (E) there is no instance. The original myth is no account on its Greek jobs, since (F1), (F2) and (A) fail (EC, Appendix A), so it cannot be a witness. "6 → 2, strict" is a fact of the (A)-only model. Limit (ii) blocks reading that shrink as merit | None. The No rests on (E) (EC, Part C) |
| **O1** (Bruno) | The narrowing clause applies to a restated rule only if that rule is an account on its narrower contract. A forecasting rule may answer an identification question, not why the stream floods (D3:L151). The lemma has no notion of a series | None. "The series is a retreat" stays SILENT; only a record of runs (EC option (b)) could move it |
| **N7** (two bakers) | The narrowing clause holds whether Maya's limits followed failures or were never widened, so it marks her on neither reading. Bea's "fuller" account is reach by D3:L313's definition: her reach contains "why only in that range" and Maya's does not. It is not (H) | None. "Both explain" stands |
| **N1** (sun god) | Nothing failed, so there is no instance. "The god is idle" is one reading. The case is also watched as a redundant route or an unfaithful component (CL:L1138) | Unaffected |
| **O36** | Nothing failed. The checked text makes no criticality claim, since the companion is withdrawn, and (H\*) says nothing about whether P is critical in the routes as written (D3:L299) | Unaffected |
| **O45** | Deleting the first spring is an organization edit, not a failure at a pair. The second spring was in Γ from the start (D3:L231, L307) | Unaffected |
| **O47** | The new commitment breaks a support. No job failed for the earlier collection, so there is no instance. The replaced limit (ii) no longer ascribes variability to the extended collection, which is no account | Unaffected |
| **O48** | It concerns Derivation 3's population, not 𝒱. It is the guard for limit (i): a response imaginable at an unseen setting need not be available | Unaffected. It supports limit (i)'s wording |
| **D3-T** | Selection, not edits, so the lemma does not apply directly. The analogue is Derivation 3 (D3:L566–568). The discarded design fails a tried setting, as E0 fails f\*, so it is no survivor, and its behaviour at the untried setting says nothing about survivors. With one passing design, "the population fixes it". Limit (i) now carries the same qualification | Holds |

---

### 4. Gains and losses

**Gains.**
- The true part of the owner's point (1) is stated exactly. At the failed job, given a witness, the shrink is strict: this supplies the witness whose absence file 00 allowed for ("need not be strict").
- The bridge says when E0 itself is the witness, and so where the owner's picture holds: a correction written as a changed rule over what each case sets. It is the one piece with content beyond (H).
- It shows where file 00's redescription worry comes back. One correction, written two ways, has a witness or has none (CE2). That bears on the owner's question (3), not only on the lemma.
- The limits block four misreadings:
  - that a bad rescue registers as easier to vary;
  - that a correction is harder, or easier, to vary than the original;
  - that two surviving rescues are ranked;
  - that strictness is merit.
- Situation 3 gets an exact Part VI description, tied to the record of indexed claims.
- There is no new declared input, no merit function and no change to (E). No verdict moves.

**Losses.**
- Several hundred words of theory text for (H) with a named witness (a one-line proof), a bridge, a narrowing clause and four limits.
- With the companion withdrawn, the text gets no statement that a rescuing part must be critical at the failed job. The idle-part point stays where it was (D3:L313).
- It does not make the record redundant. Its own narrowing clause shows that Pres cannot tell a dropped job from one never claimed.
- It gives no pre-test rejection in Situation 2. It does not read runs (O1), blaming the background or the test (K3), or grain saves.
- 𝒱 is still neither a declared input nor an index (D3:L516, L518). Limit (iv) and the bridge make plain that what the lemma delivers depends on how 𝒱 and E are written.
- A reader may still take strictness as merit. Limit (ii) is the guard.
- **Side finding on the record option.** [COMPUTED] EC option (b) defines a consequence as a pair where the answer "is not kept when that component is deleted". Under Part II deletion, every added override has such a pair at every sunny-south pair of its contract, so (b) marks none of the good rescue, the bad rescue or the patch. The models that showed (b) marking them switched the part off (CE15). (b) needs "set to the earlier value" in place of "deleted", or a declared restriction operation (D3:L287). This note does not change it.

---

### 5. What remains uncertain

1. **Whether a family of organization edits may give some members a restricted transport.**
   - D3:L299 says only "a declared family 𝒱 of organization edits". File 00 held the interpretation fixed, and there "Each pair retains its edited components, background, and interpretation" (F00:L294).
   - If a family may hold E0 with its own transport, a correction that posits a mechanism has its original as witness (R4: 2 → 1).
   - If it may not, (H\*) with the original as witness is limited to corrections that add no variable the transport reads from the world.
2. **How far the bridge's proof reaches.** It uses Part II's solution semantics and Part V as modelled in `fe.py`. `fe.py` does not model non-circular dependence's first two sentences (the target's answer "as a component"), grain, or non-vacuity, which it takes as met. It reads (F1) at the boundary values each pair fixes, which is EC's reading of Grievance 1. The general proof is short, but it has not been checked against those unmodelled clauses.
3. **What a job is.** The texts do not define "explanatory job" (01 (a)), and the checked wording does not define it either. (H\*) holds on either reading. The counts depend on the reading, and so does whether a job with no contrast is one no candidate can do (R5: 2 → 0).
4. **Part VI's declared restriction operation** (D3:L287): switch-off, or Part II deletion. It decided the withdrawn companion, and it decides EC option (b)'s marks.
5. **The one-summer patch.** Whether it already fails non-circular dependence at the failed summer ("restates the answer it was asked for", D3:L273). If it does, (E) separates it from the good rescue on the record plus the failed summer.
6. **What the owner wanted.** The owner may have wanted a mark rather than a truth. The lemma cannot give point (2). A mark of retreat needs a record (EC option (b), with the repair noted in section 4), which is a separate decision.
7. **Evidence and line numbers.** The models are toy models: they give counterexamples, not frequencies. Draft 3 is not frozen, and its line numbers may move.

---

### 6. Plain words

**The garden.** A gardener says the south bed ripens first because the south wall gets the most sun. One year the north bed ripens first. She can rescue her explanation in three ways.
- **Good:** the neighbour planted an early variety along the north side. It can be checked, and it predicts what a dry spring or new seed does.
- **Bad:** "in a wet spring the north bed ripens first". It fits only the failure, and "windy spring" would fit as well.
- **Retreat:** "my explanation only covered the summers I had seen".

**Does the mistake stay out?** At the failed summer, yes. Any version that says "south first" there is wrong, and the basic test rejects it for any question that still includes that summer, with no record needed. Three things limit this.
- **Other summers.** Versions that fit every recorded summer and the failed one can still say "south first" in early-variety summers nobody has seen: 56 of the 64 that fit in one family, and 24 of 32 after a seed trial. Only the question "every kind of spring" shuts them all out. On that question her old explanation was always wrong; the failure showed this but did not create it.
- **How the correction is written.** Written as a changed rule ("north first if the neighbour planted early, otherwise the sunnier bed"), her old explanation is one of the versions, and the failed summer throws it out. Written as a mechanism with its own hidden "variety effect", her old explanation is not among the versions, and the failed summer may throw out nothing new. Same answers, different bookkeeping.
- **The retreat.** She can drop the failed summer from her question at any time. That is a new claim, recorded, not forbidden, and it readmits the old version.

**Does a bad rescue look "easier to vary"?** No.
- The theory does not define a good explanation by variation. That definition is Deutsch's, and the theory's count of fitting versions "grades nothing".
- On the recorded summers plus the failed one, the good rescue, the wet-spring rescue and a one-summer exception all fit the same family. Only a new test tells them apart, such as the seed trial or a wet spring with the usual planting.
- Inside her old explanation's own family, the wet-spring rescue even comes out harder to vary: from 4 fitting versions to 2.
- Whether a correction looks easier or harder than the original depends on how the versions are listed: 1, 4 or 64 for the original against 2 for the correction.
- Only the retreat reliably shows "more versions fit", and a claim honestly narrow from the start shows the same.

**Can the comparison be allowed for one's own correction?** No.
- File 00's reasons (no common set, counts that change when a feature is split, a fixed interpretation) say nothing about who wrote what.
- What can be had is smaller. Inside the correction's family, if some version keeps the old explanation's verdicts, adding the failed summer strictly shrinks the versions that fit. That compares two sets of jobs, not the explanation with its correction.
- Whether such a version exists depends on how the correction is written, which is file 00's redescription worry coming back.
- "Own" does no work: a rival's correction written the same way gets the same result. What makes a correction someone's own is its history, which is the record.

**What changed after the attacks.** The witness is now "a version that does the old jobs and fails the new one", because the earlier wording failed for a hidden variable. The retreat clause needs the unchanged version in the family. Two claims were withdrawn: "a rescuing part must be critical at the failed job" and "a correction is never harder to vary".

**Bottom line.** A record of rescues is not redundant. The theory keeps a corrected mistake out of every account of an unchanged question, as a fact. But it cannot see this before a test, and it cannot tell a retreat from an honest limit. Whether the failed case even excludes the old explanation depends on how the correction is written.

---

### 7. Output of `check/r1_repaired_wording.py`, verbatim

```text
====================================================================================================
R1  THE REPAIRED WORDING AGAINST THE COUNTEREXAMPLES
====================================================================================================

----------------------------------------------------------------------------------------------------
R1  repaired (H*) and the (a) iff: every F (up to 3 of the 7 jobs) and every f* outside F
    counts of (witness hypothesis, strict containment); only (T,T) and (F,F) may occur
----------------------------------------------------------------------------------------------------
    jobs: j_seen={dry/calm/late/sunS, dry/calm/late/shadeS}, j_eshade={dry/calm/late/sunS, dry/calm/early/shadeS}, j_fail={dry/calm/late/sunS, wet/windy/early/sunS}, j_seed={dry/calm/late/sunS, dry/calm/early/sunS}, j_rain={dry/calm/late/sunS, dry/calm/late/shadeS, wet/calm/late/sunS}, j_rain_nc={dry/calm/late/sunS, wet/calm/late/sunS}, j_open=all 16 pairs
  Emb-1 (16, E1's transport)               (A) only  (T,T)=  89 (F,F)= 205  hypothesis true but not strict=0  strict without hypothesis=0
  Emb-1 (16, E1's transport)               full (E)  (T,T)=  72 (F,F)= 222  hypothesis true but not strict=0  strict without hypothesis=0
  Emb-1 + alpha (17)                       (A) only  (T,T)=  89 (F,F)= 205  hypothesis true but not strict=0  strict without hypothesis=0
  Emb-1 + alpha (17)                       full (E)  (T,T)=  72 (F,F)= 222  hypothesis true but not strict=0  strict without hypothesis=0
  Emb-1 + E0 with its own transport (17)   (A) only  (T,T)=  89 (F,F)= 205  hypothesis true but not strict=0  strict without hypothesis=0
  Emb-1 + E0 with its own transport (17)   full (E)  (T,T)=  84 (F,F)= 210  hypothesis true but not strict=0  strict without hypothesis=0
  Emb-2 (16)                               (A) only  (T,T)=  89 (F,F)= 205  hypothesis true but not strict=0  strict without hypothesis=0
  Emb-2 (16)                               full (E)  (T,T)=  89 (F,F)= 205  hypothesis true but not strict=0  strict without hypothesis=0
  Emb-2 without the "off" setting (12)     (A) only  (T,T)=  49 (F,F)= 245  hypothesis true but not strict=0  strict without hypothesis=0
  Emb-2 without the "off" setting (12)     full (E)  (T,T)=  69 (F,F)= 225  hypothesis true but not strict=0  strict without hypothesis=0
  A2 V1 (3)                                (A) only  (T,T)=  13 (F,F)= 281  hypothesis true but not strict=0  strict without hypothesis=0
  A2 V1 (3)                                full (E)  (T,T)=   7 (F,F)= 287  hypothesis true but not strict=0  strict without hypothesis=0
  A2 V1 + identity (4)                     (A) only  (T,T)=  52 (F,F)= 242  hypothesis true but not strict=0  strict without hypothesis=0
  A2 V1 + identity (4)                     full (E)  (T,T)=  35 (F,F)= 259  hypothesis true but not strict=0  strict without hypothesis=0
  A2 V2 (4)                                (A) only  (T,T)=  49 (F,F)= 245  hypothesis true but not strict=0  strict without hypothesis=0
  A2 V2 (4)                                full (E)  (T,T)=  69 (F,F)= 225  hypothesis true but not strict=0  strict without hypothesis=0
  A2 V2 + identity (5)                     (A) only  (T,T)=  88 (F,F)= 206  hypothesis true but not strict=0  strict without hypothesis=0
  A2 V2 + identity (5)                     full (E)  (T,T)=  89 (F,F)= 205  hypothesis true but not strict=0  strict without hypothesis=0
  A7 rich sun' x var[V,W,Wi] (1024)        (A) only  (T,T)= 150 (F,F)= 144  hypothesis true but not strict=0  strict without hypothesis=0
  A7 rich sun' x var[V,W,Wi] (1024)        full (E)  (T,T)= 120 (F,F)= 174  hypothesis true but not strict=0  strict without hypothesis=0
  failures of the repaired (H*) or of the iff, all families: 0

  The counterexamples of 04b under the repaired hypothesis (full (E)):
   CE1 Emb-1, v0 = beta (switched off)        F={j_seen, j_eshade}, f*=j_fail: hypothesis for the named v0? False for some member? False  |Pres| 1 -> 1  strict? False
   CE1 Emb-1 + alpha, v0 = alpha (deleted)    F={j_seen, j_eshade}, f*=j_fail: hypothesis for the named v0? False for some member? False  |Pres| 1 -> 1  strict? False
   CE2 Emb-2, v0 = rule ignoring V            F={j_seen, j_eshade}, f*=j_fail: hypothesis for the named v0? True  for some member? True   |Pres| 2 -> 1  strict? True
   R4  Emb-1 + E0 with its own transport      F={j_seen, j_eshade}, f*=j_fail: hypothesis for the named v0? True  for some member? True   |Pres| 2 -> 1  strict? True
   -> CE1: the repaired hypothesis is false, so the lemma makes no claim, and indeed 1 -> 1.
      CE2 and R4: it is true, and the containment is strict (2 -> 1).

----------------------------------------------------------------------------------------------------
R2  the bridge: does v0 have E0's Account verdict on every contract holding the baseline? (full (E))
----------------------------------------------------------------------------------------------------
  Emb-2 v0: rule ignoring V (added port V is an input the pair sets)       contracts=32768  E0 an account on 2040  verdicts differ on 0
  Emb-1 beta: var switched off (added port ovr read from the target)       contracts=32768  E0 an account on 2040  verdicts differ on 1920  smallest: {dry/calm/late/sunS, dry/calm/early/shadeS}
  Emb-1 alpha: sun restored, var deleted (ovr left free)                   contracts=32768  E0 an account on 2040  verdicts differ on 2040  smallest: {dry/calm/late/sunS, dry/calm/late/shadeS}
  E0 itself, with its own transport                                        contracts=32768  E0 an account on 2040  verdicts differ on 0
  sanity: per-pair decomposition equals fe Account on 300 random contracts x 4 candidates: True

----------------------------------------------------------------------------------------------------
R3  narrowing clause: E = E0 (the identity edit), accounts on F, not on f*; is Pres(F) strictly larger?
----------------------------------------------------------------------------------------------------
  A2 V1 (3)                    (A) only  identity in V? False  instances= 45  strict=  6  not strict= 39
  A2 V1 (3)                    full (E)  identity in V? False  instances= 32  strict=  4  not strict= 28
  A2 V1 + identity (4)         (A) only  identity in V? True   instances= 45  strict= 45  not strict=  0
  A2 V1 + identity (4)         full (E)  identity in V? True   instances= 32  strict= 32  not strict=  0
  A2 V2 (4)                    (A) only  identity in V? False  instances= 45  strict=  6  not strict= 39
  A2 V2 (4)                    full (E)  identity in V? False  instances= 32  strict= 12  not strict= 20
  A2 V2 + identity (5)         (A) only  identity in V? True   instances= 45  strict= 45  not strict=  0
  A2 V2 + identity (5)         full (E)  identity in V? True   instances= 32  strict= 32  not strict=  0

----------------------------------------------------------------------------------------------------
R5  the clean control for "v0 fails f*" (a job the witness also does)
----------------------------------------------------------------------------------------------------
  Emb-2, F={j_seen}, f*=j_rain    (A) only  v0 does f*? True   |Pres| 2 -> 2  strict? False
  Emb-2, F={j_seen}, f*=j_rain_nc (A) only  v0 does f*? True   |Pres| 2 -> 2  strict? False
  Emb-2, F={j_seen}, f*=j_rain    full (E)  v0 does f*? True   |Pres| 2 -> 2  strict? False
  Emb-2, F={j_seen}, f*=j_rain_nc full (E)  v0 does f*? False  |Pres| 2 -> 0  strict? True
  pair level, sun x var[V], F=J_before, f*=another wet spring (usual planting): |Pres| 2 -> 2  strict? False
  -> with jobs as questions, {B0, wet spring} has no contrast, so NO member does it (strict for a
     reason unrelated to the witness); with a contrast held ({B0, shade, wet spring}), E0 does it and
     the shrink is not strict. The hypothesis "v0 fails f*" is needed.

----------------------------------------------------------------------------------------------------
R6  limit (i): members of Pres(F + f*) repeating E0's wrong answer at pairs no job holds (full (E))
----------------------------------------------------------------------------------------------------
  Emb-2 (16)                           F={j_seen, j_fail}                 |Pres|=  1  repeating E0 at an unreached pair:   0
  Emb-2 (16)                           F={j_seen, j_fail, j_seed}         |Pres|=  1  repeating E0 at an unreached pair:   0
  Emb-2 (16)                           F={j_open}                         |Pres|=  1  repeating E0 at an unreached pair:   0
  A7 rich sun' x var[V,W,Wi] (1024)    F={j_seen, j_fail}                 |Pres|= 64  repeating E0 at an unreached pair:  56
  A7 rich sun' x var[V,W,Wi] (1024)    F={j_seen, j_fail, j_seed}         |Pres|= 32  repeating E0 at an unreached pair:  24
  A7 rich sun' x var[V,W,Wi] (1024)    F={j_open}                         |Pres|=  1  repeating E0 at an unreached pair:   0
  -> the same jobs leave the mistake open in the rich family and closed in the poor one: fixed by V.
```

---

## Appendix A — The text reading (working file 01, copied unchanged except as noted)

### 01 Text: does a rescued explanation keep its mistake out without a record?

*Working file, 24 September 2026. Read-only on the repository. Read in full: file 11; draft 3 (the revision-2 theory text, file 13 draft 3); the error-correction analysis of 24 September (EC). Read at the cited passages: file 10; file 00 (L110–400, 580–600, 780–860, 1270–1330, 1356–1396, plus greps); the change list entries W33.1 and W34.1; the S81 case book (O1, O27, O45, O46); the N-case book (N2, N3, N6, N7); D3-T `final.md`; project story entries 28–29; Deutsch chapter 1 pp.21–29 and p.306 in the book text. The Pinker folder was not opened. Draft 3 is not frozen: its line numbers are those of the file as read today.*

**Conventions.** F11:L, F10:L, F00:L, F12:L = file line; D3:L = draft 3 line; EC:L = the error-correction analysis; CL:L = the change list. **[T]** = what a line says. **[F]** = follows from quoted lines with no added premise. **[I]** = my inference; it could be wrong.

**The example, in the theory's terms.** E0 = "the south wall gets the most sun" (held four summers, failed in the fifth: the north bed ripened first). E_good = E0 + "the neighbour planted an early variety along the north side". E_bad = E0 + "in a wet spring the north bed ripens first". Two contracts: C_open, every physically admitted change, including weather and planting (what an unstated scope amounts to on EC's first reading, EC:L121); and C_5, "the five summers seen, as they came". p_open and p_5 are the questions on those contracts.

---

#### (a) Jobs, F, Pres, the variation family, the lemma, reach

**The lemma.**
- [T] F11:L315 (identical at F10:L330; F12:L317 has "causal jobs"): "**Hard-to-vary.** For explanatory jobs \(F\subseteq F'\), \(\operatorname{Pres}(F')\subseteq\operatorname{Pres}(F)\), where \(\operatorname{Pres}(F)=\{v\in\mathcal V:\forall f\in F,\operatorname{Account}(E_v,f)\}\). More reach constrains variation; the containment need not be strict; counting jobs is not a warrant."
- [T] D3:L313 has the same statement plus W34.1's sentence: "The **reach** of \(E\) is the set of jobs \(f\) with \(\operatorname{Account}(E,f)\); it is fixed by \(E\) and the world, not by which jobs anyone has checked." It also has W33.1's sentences: "(E) has no condition that each commitment do work. A commitment \(d\) does no work by itself in the candidate when every support stays a support after \(d\) is added to it and after \(d\) is removed from it: a candidate carrying \(d\) then meets (E) exactly when it meets (E) without \(d\), and \(\{d\}\) is critical in no support (B). When \(\Gamma\) is infinite, a block of such commitments can still be critical (Infinitary support). How hard an account is to vary is a separate matter, shown by \(\operatorname{Pres}\), and it grades nothing."
- [T] File 00 states it with its premises (F00:L356–377): "Fix an organization, interpretation, variation family \(\mathcal V\), and a family \(F\) of explanatory jobs." Then (H): \(F\subseteq F'\Rightarrow\operatorname{Pres}(F')\subseteq\operatorname{Pres}(F)\). "**Proof.** Preserving every job in the larger family includes preserving every job in the smaller family. ∎"

**What an "explanatory job" is.**
- [T] No text defines it. File 11 and draft 3 use the word only in the lemma (grep: F11:L315, D3:L313, F10:L330). File 00 uses it at L358 and L379, and at L381: "'Hard to vary' is therefore an articulated pattern of constrained changes, relative to an explanatory job."
- [F] By type, a job is a **question**. It fills the second slot of Account, where every other use puts a question: \(\operatorname{Account}(E|W,p)\) (F11:L292), \(\operatorname{Account}(E_v,p)\) (F11:L304). Account is defined for \(\mathcal E=(E,p,t,\Gamma)\) (F11:L233). So a job is a whole \(p=(D,C,b_0,\mathcal Q,O_p,\rho_p)\) (F11:L140), with its whole contract. The two lineage texts agree. File 00's reach is participation "in an account of another question" (F00:L383), and CL:L1110 (W34.1) says "reach concerns the questions a written content answers".
- **F** is any family of jobs. In file 11 the lemma is universally quantified over \(F\subseteq F'\), so nobody fixes F. File 00 says "Fix … a family \(F\)" (L358) and names no one who fixes it.

**Pres(F).** [T] It is the set of variants \(v\in\mathcal V\) for which the varied organization \(E_v\) is an account on every job in F. [F] It is a subset of one fixed \(\mathcal V\), taken relative to one fixed E. File 11 never defines \(E_v\) beyond "For a declared family \(\mathcal V\) of organization edits" (F11:L301; D3:L299). File 00 adds, for the same family in (D): "Each pair retains its edited components, background, and interpretation." (F00:L294).

**The variation family, and who fixes it.**
- [T] It is "a declared family \(\mathcal V\) of organization edits" (F11:L301; D3:L299; F10:L316).
- [F] Nobody is named as declaring it. \(\mathcal V\) is **not** in Part XIV's list of declared inputs (F11:L514; D3:L516), which lists O and P, a contract's scope and appropriateness, boundary and continuity, and (in draft 3) the weighting of credit. Nor is it among the indices (F11:L516; D3:L518). So the rule "rather than choosing the input from the verdict wanted" (F11:L514) is not stated for \(\mathcal V\). EC:L237 flags the risk.

**What "reach" means now.**
- [T] In file 11 it is undefined, used once in the lemma. File 10 dropped file 00's definition (CL:L1106). That definition was: "Reach occurs when an unchanged organizational core participates in an account of another question through a stated anchor and additional background. The new bridge is itself content and can be a creative contribution." (F00:L383)
- [T] In draft 3, reach(E) is the set of jobs f with Account(E,f), "fixed by \(E\) and the world, not by which jobs anyone has checked" (D3:L313).
- [F] With the identity edit in \(\mathcal V\), E itself is in Pres(F) exactly when \(F\subseteq\) reach(E).
- [I] Inside one E, "more reach constrains variation" can only mean a larger job family held against the same \(\mathcal V\). Reach compared between two different E's is the comparison file 00 rejects (section c).

---

#### (b) Jobs, the contract C, and (A)

**Is a pair of C a job?**
- [F] No. A job is a question with a whole contract (a). A pair \((a,b)\in C\) is one member of a job's contract.
- [F] A pair can become a job only by writing a new question whose contract holds it, for example \(\{(1,b_0),(a,b)\}\). By [T] F11:L153 ("Two questions with the same \(D\) and different \((C,\mathcal Q)\) are different questions, and an answer to one is not an answer to the other") that is a different question.
- [F] Account is not monotone in the contract, in either direction. (F1), (F2) and (A) are universal over C, so they survive shrinking C and can fail when C grows. Non-circular dependence is existential over C: it needs a witnessing pair (F11:L257; D3:L255), so it survives growing C and can fail when C shrinks. So an account on C need not be an account on a sub-contract, and conversely.

**Does a failed pair inside C bind every later candidate on that contract?**
- [T] (A): "For every \((a,b)\in C\), \(\operatorname{Ans}_E(\tau(a),\sigma(b))=\operatorname{Ans}_p(a,b)\)" (F11:L249–253). "The query \(\mathcal Q\) is held fixed; an account of a different query is not an account of this one." (F11:L255) "Every conjunct is a condition on how supplied relations behave under the changes in \(C\)." (F11:L267) Realism: "Whether a transport is faithful on a contract is independent of whether anyone accepts it." (F11:L69) File 00: "The contract ranges over the declared class of changes, including unperformed changes, not merely over the trials on which the candidate succeeded." (F00:L208)
- [F] **Yes, as a fact, with no record needed.** \(\operatorname{Ans}_p(a,b)\) is fixed by D. Any candidate for p that answers that pair differently fails (A), whether it is a rival, a rescue or E0 offered again. It never "becomes" bound: the pair was in C before anyone tested it.
- [F] Two limits.
  1. The binding is by the world's answer, not by the recorded observation. A test refutes "\(\neg(T\land B\land I)\) and nothing narrower" (F11:L391; F12:L411: "which conjunct fails is a further question"). A rescuer who blames B or I changes no job, and the account's standing stays whatever the world makes it.
  2. The binding holds only while the question keeps that contract.

**What if the rescue narrows the contract to exclude the failed pair?**
- [T] F11:L161: "An account at a stated scope answers the question asked at that scope; it does not answer a broader question that failed, and a narrowing adopted after a failure is a new claim at a new index (Part VIII). What makes a restriction appropriate to the question asked is a substantive, criticizable part of the claim; the semantics records the restriction and supplies no rule that certifies it."
- [T] D3:L159 adds: "Meeting the conditions of an account (Part V) on the restricted contract does not certify the restriction as appropriate. Where the claim states the ground of its restriction, a verdict on the restriction is given with that ground; where it states none and a verdict turns on one, the ground is a missing declared input (Part XIV)."
- [T] F11:L163: "What is prohibited is changing \(C\) or \(\mathcal Q\) during an assessment without recording that the claim has changed. Supplying a meaning for a replacement query can make a coherent new question; it does not answer the original one."
- [T] Historical index: "A proposition indexed to a contract remains that proposition when a later theory changes the current contract. A new index is a new claim." (F11:L365; F10:L378; D3:L363)
- [T] Derivation 7: "The claim '\(\mathcal E\) is an account on \(C\)' and the claim '\(\mathcal E\) is not an account on \(C'\)' are claims at different indices and may both be true." "Goalpost-moving is the act of changing the index without recording the change, and it is a failure of the record, not a licensed operation of the semantics." (F11:L596–598)
- [F] On the narrowed contract the failed pair binds nothing. The old claim stays failed at its old index. The new claim gets whatever (E) gives it on its own contract.
- [F] Applied to the example:
  - "The four summers before, as they came": this retreat of E0 **fails (E) itself**. File 11's non-circular dependence needs a pair "that removes or replaces a nonempty block of Γ … under which the answer profile changes" (F11:L257). Draft 3's needs a pair whose answer "differs from its value at \((1,b_0)\)" (D3:L255). Four natural summers, all "south first", supply neither. Non-vacuity also excludes a contract "excluding every change under which the active commitments could matter to \(\mathcal Q\)" (F11:L259).
  - "The five summers seen" does not rescue E0 alone, since the failure is one of the five. It rescues only the patched E_bad. On EC's reading of (F1), E_bad passes on C_5 in draft 3 and is unsettled in file 11 (EC:L140–145). And a contract with no interventions is not a production question (F11:L153; D3:L151).

**Is anything tying a rescue's contract to the old one?**
- [T] Only the following, and none requires the new contract to contain the old one or the failed pair.
  1. **Question identity.** "The same question" means the same \((D,C,\mathcal Q)\) (F11:L153; F10:L168). A rescue that claims the same question is held to C. One that narrows is answering another question.
  2. **The record of index changes** (F11:L163, L365, L596–598).
  3. **(EK)'s index.** "The scope of \(\operatorname{Account}(c,p_c)\) is the contract fixed at \(e_c\). A later narrowing of that contract to rescue adequacy is a new claim at a new index, and does not retroactively satisfy (EK)." (F11:L445; F10:L456; D3:L447) This is the only sentence in the theory that names a "rescue".
  4. **(P)'s obligations**, "fixed for the comparison" (F11:L427). If the epistemic obligation was declared at the broad question, the narrowed claim does not meet it (EC:L149).
  5. **Non-vacuity.** Exclusions must be stated, "not silently" (F11:L259). Grievance 4: a quiet exclusion "is caught by the requirement that the exclusion be stated … and then by any criticism that supplies the excluded change" (F11:L45).
  6. **Draft 3's missing-input mark and Part XV preamble** (D3:L159, L516, L528).
- [T] Against a tie: Derivation 5's proof lists "add or remove a change; alter \(\mathcal Q\)" as admitted edits of a contract (F11:L580; D3:L584). A contract can be the originative content of (G): "When it is a contract, the originative act is the finding of a question." (F11:L417)
- [T] File 00 had stronger ties, not carried into files 10, 11, 12 or draft 3 (grep, none found):
  - "A newly discovered problem may supply a new obligation, but its connection to the original difficulty must be accounted for rather than assumed from a shared label." (F00:L785)
  - "A transport supplies the interpretation of \(o\) and \(r\) across changed representations; without one they are not silently compared." (F00:L800)
  - "A later model may show that the earlier application was always mistaken … Alternatively, a later model may preserve an accurate approximation while explaining its limits. These are different cases. A transport must say which it is." (F00:L593)
  - "It must not be dismissed by inventing a favorable new grain after the fact." (F00:L1380)

---

#### (c) The limit: wording, reason, motivating example

**Wording.**
- [T] F00:L358: "Fix an organization, interpretation, variation family \(\mathcal V\), and a family \(F\) of explanatory jobs."
- [T] F00:L379: "That is the valid structural connection between additional reach and restrictions on variation. The containment need not be strict. It says nothing by itself about two different theories using different interpretations or different variation families. Counting jobs is not a replacement for the missing comparison."
- [T] F00:L381: "'Hard to vary' is therefore an articulated pattern of constrained changes, relative to an explanatory job. It is not the requirement that every detail of a complete theory be individually indispensable. Nor is it a numerical warrant. Two descriptions can divide the same work into different numbers of features; splitting one feature into ten cannot create knowledge."
- [T] F00:L1300 (under "More reach is not a count-based warrant", L1298): "The FW3 statement that an explanation reaching more is thereby harder to vary is not a valid comparison between arbitrary contents. The valid containment result holds when the organization, interpretation, and variation family stay fixed while preservation requirements are added. It may be non-strict. The structurally extended source already states this correction. [S5: T12; S6: Part III.3]"
- [T] F00:L1302: "FW5 also withdraws the special permission for a count of conjecturally independent features to order explanations for preference. A numerical division into features can change without any increase in explanatory content. Particular newly met constraints can supply reasons; their count alone does not supply those reasons."
- [T] The same limit elsewhere in file 00:
  - on maps: "All maps have declared domains. Their meanings are held fixed across the comparison." (F00:L170)
  - on supports: "A new map or a changed role assignment is a different route, which must be identified as such." (F00:L265)
  - on transports: "The proof is about a fixed map and compatible scopes. It does not establish that two different theories share an interpretation merely because their outputs sometimes agree." (F00:L534)
  - on counts: "no special count of 'independent reach' is licensed to choose explanations by itself" (F00:L851)
  - FW4 is credited with "the correct fixed-family reach lemma" (F00:L1286).
- [T] Files 10, 11 and draft 3 keep only "the containment need not be strict; counting jobs is not a warrant". They drop the "Fix …" premise, leaving it implicit in the one \(E\) and one \(\mathcal V\) of Pres.

**The stated reason.** File 00 gives three reasons and no others.
1. [F] **Mathematical.** The proof (L377) is an inclusion between two subsets of one \(\mathcal V\). With two organizations or two families there is no common set in which one Pres could contain the other ("It says nothing by itself about two different theories…", L379).
2. [T] **Invariance under redescription.** Any comparison across contents would need counts, and counts change with how the work is cut into features: "Two descriptions can divide the same work into different numbers of features; splitting one feature into ten cannot create knowledge" (L381). See also L1302.
3. [T] **Interpretation held fixed.** Map meanings are "held fixed across the comparison" (L170), and a changed map or role is "a different route" (L265).
- [T] **And "thereby" fails even inside one fixed family**, because the containment "may be non-strict" (L1300).

**The motivating example.**
- [T] The only concrete example in file 00 is the redescription one: "splitting one feature into ten" (L381). FW3's own statement, and the FW3 and FW4 passages cited (S5 T12, S6 Part III.3), are not in the repository. NOT-IN-BUNDLE.md says of file 00: "Its links point to files outside this repository." **Not checkable here:** whether FW3 gave a specific counterexample.

**Does the reason apply to an explanation and its own correction?**
- [F] **Yes.** None of the three reasons mentions unrelatedness, authorship or target. They are structural. "Arbitrary" means contents with no shared organization, interpretation and \(\mathcal V\). Same target, same question and shared parts do not remove the reasons.
- [I] What matters is how the correction is represented.
  - **As its own organization with its own family.** E_bad or E_good taken with its own \(\mathcal V_1\): reason 1 applies, since \(\mathcal V_1\) has a slot (the north-bed clause) that E0's family lacks. Reason 2 applies, since "in a wet spring" can be written as one feature or as ten (rainfall in April, in May, …), which changes any count. Reason 3 applies in part: the shared core can keep its anchors, but the new component brings a new anchor (rain, or the variety).
  - **As an edit of E0.** Declare \(\mathcal V_0\) to contain E0's organization edits "add a north-bed component anchored to X", for X among rain, wind, frost, the neighbour's variety and so on. File 00's (D) family already allows this: "Replacement contrasts need not be deletion contrasts" (F00:L283), and each pair "retains its edited components, background, and interpretation" (L294). Then E0 and \(\mathcal V_0\) are fixed, every rescue is some \(E0_v\), and the lemma applies **with no relaxation**. The limit is met, not lifted. This works equally for a rival gardener's rescue written as an edit of the same E0. The family does not single out "its own" correction, and it needs no ranking of people.

---

#### (d) How a rescue relates to the old candidate

**New candidate.**
- [T] F11:L309 (D3:L307; absent from F10:L324): "a component reassigned to a new target after a deletion belongs to a new candidate with its own assessment, and the new candidate's success is not the old one's."
- [T] "A changed rule is a changed component." (F11:L105) A candidate is \((E,p,t,\Gamma)\) (F11:L233).
- [F] Any patch makes a new candidate. EC:L25 corrects "[TEXT]" to "[FOLLOWS]" for this. O46: "What survived is a new account with a cable in it … the replacement's success is its own." Interference: "\(b\) is not made 'not a commitment' to repair this" (F11:L311).

**New index.** See (b): F11:L161, L365, L445, L596–598.

**Repair's protected obligations: the one place that says a correction keeps what was right.**
- [T] (P): "\(\exists o\in O[\neg o(\xi)\land o(\xi')]\land\forall r\in P[r(\xi)\Rightarrow r(\xi')]\land\operatorname{ProducedBy}\)" (F11:L427–430).
- [T] "The obligations are declared inputs … a protected condition is lost exactly when it fails on an occasion it covers. … (P) does not rank alternatives. Losses outside \(P\) must be exposed." (F11:L433)
- [T] Draft 3: \(r(\xi')\) "held on every occasion it covers from \(\xi\) to \(\xi'\), not only at \(\xi'\)" (D3:L435).
- [T] File 00: "Their definitions need not predate the discovery historically; they must not shift inside its assessment." (F00:L787) "Adding a member to a set of accounts does not establish (P) for a comparison that protects the lost achievement." (F00:L808)
- [F] **"Keep what was right" exists, but only as a declared input.** Nothing makes the old successes protected by default.
- [F] In the example, E_bad is a trade-off fix in the world. E0 was right about wet springs with the usual planting (south first). E_bad says north there. With P = "the right bed for every spring with the usual planting", E_bad loses P, but (P) sees the loss only once such a spring has occurred by \(\xi'\) (D3:L435). E_good keeps P.
- [T] Derivation 10 is the text's own model correction. The new \(S_1\) is faithful "on the extended contract", and (P) holds "If it repairs the obligation … while protecting 'predict displacements correctly'" (F11:L616–618). The contract is extended and the old success protected, but by stipulation in the example, not by a rule.

**Criticism (Part IX).**
- [T] Bearing: "\(\operatorname{Bearing}(c,z,p)\iff\operatorname{Account}(\mathcal E_c,p_\delta)\)" (F11:L373–376). K3 (F11:L391).
- [T] "(E) does not exclude a true mechanism guessed for bad reasons; the reasons for adopting it are assessed elsewhere (Part IX)." (F11:L279)
- [F] "It was the variety" bears only on a question whose contract holds a pair that separates rain from the variety. On C_5 it bears only on the restriction, which is criticizable (F11:L161, L45), and in draft 3 that verdict is unsettled if no ground is stated (EC:L147).

**Derivation 3 and selection: the text's one built-in ratchet is a history.**
- [T] A selected transport survives on "a finite history \(H\subseteq C\) of edit–boundary pairs actually encountered, and a survival condition requiring fidelity on \(H\)" (F11:L197). "A **selection response** extends \(H\) and lets \(\mu\) act" (F11:L227). Draft 3 adds that "fidelity on \(H\) without membership in \(\mathcal T\) is not survival" (D3:L195).
- [F] Once a failure joins H, every later survivor is faithful at it. The mistake cannot return among survivors while H is kept. That guarantee is carried by a **record of encountered pairs**, not by the content. D3-T shows it: the discarded design "failed the test at a setting the tester does try", so it is not a survivor.
- [F] Constructed candidates have no H in (E). Their counterpart is keeping the pair in the contract, which (b) shows the text does not require. File 10's unqualified Derivation 3 ("always underdetermined", F10:L38) does not change this.

**(EK) and newness.**
- [T] (EK) cannot be backdated by a narrowing (F11:L445).
- [T] Newness: \(\operatorname{New}(s,c,h,e)\iff\neg\exists d\in R_{<e}(s,h),\ d\equiv_\ell c\) (F11:L405–409). Draft 3: \(d\equiv_\ell c\) "when there are transports from \(d\) to \(c\) and from \(c\) to \(d\), both faithful on \(c\)'s contract at grain \(\ell\)" (D3:L407). "A system may understand a false theory." (F11:L399)
- [F] E0 offered again, or a narrowing that keeps E0's organization, is equivalent to repertoire content on the new contract. It is not New, so it gets no Origin and no (EK) credit.
- [I] The narrowed contract itself may still count as question-finding (Derivation 5; EC:L150). Newness withholds credit; it does not stop the mistake from returning.

**Does anything say a correction must keep what the old explanation got right?**
- [T] Only (P)'s protected obligations, when declared, with "Losses outside \(P\) must be exposed" (F11:L433), and Derivation 10 as an example.
- [T] EC's summary stands on the texts: the revision "is *not* constrained by any requirement that the new content keep the old parts, be minimal or principled, or be hard to vary" (EC:L475).
- [T] File 00's "unchanged organizational core" (F00:L383) described reach, not correction, and was dropped (CL:L1106).

---

#### (e) Answer to the owner's three points

**(1) "A correction adds the failed case to the explanation's jobs, so any version that brings the mistake back fails."**
- [F] **Right about the fact, wrong about the mechanism.**
  - The failed case is a pair, not a job. On p_open it was always in C.
  - Reach is "fixed by \(E\) and the world, not by which jobs anyone has checked" (D3:L313). So p_open was never in reach(E0), before or after the failure. The failure is evidence of that fact. It adds no job.
  - On p_open, (A), (F1) and (F2) bind every candidate at every pair (F11:L249–267). E0 offered again fails at the failed summer. E_bad fails at pairs that separate rain from the variety: a wet spring with the usual planting, or the variety in a dry spring (EC:L122). So on a fixed question the mistake cannot re-enter an **account**, with no record needed.
- [F] **It is not a ratchet.**
  1. The job can be dropped. Narrowing is a legitimate new claim (F11:L161, L163, L580, L596–598), and on it the pair binds nothing.
  2. The mistake can re-enter a **claim**. Nothing stops someone from claiming E0 or E_bad for p_open. The claim is false as a fact but "unmarked in the record" until a separating pair is tested (EC:L131, L159).
  3. K3 lets the rescuer blame B or I, and no job changes (F11:L391).
  4. The text's one real ratchet, selection's H, is itself a record (d).

**(2) "A bad rescue registers as making the explanation easier to vary, since more versions fit, by the same measure that defines a good explanation."**
- [T] The theory has no measure that defines a good explanation. (E) defines an account. Pres "grades nothing" (D3:L313). The semantics supplies no merit function, and "a claim that needs one is unsettled" (D3:L516; D3:L25). File 11 has no merit function; where a claim needs one it takes it as a declared input (F11:L27).
- [F] **The narrowing: true, in the lemma's own direction, with no relaxation.** Take E0 and \(\mathcal V_0\) fixed (c). Narrowing replaces the jobs \(\{p_5, p_{open}\}\) by \(\{p_5\}\). By the lemma, \(\operatorname{Pres}(\{p_5,p_{open}\})\subseteq\operatorname{Pres}(\{p_5\})\): dropping jobs can only enlarge Pres. Every X true only of the failed summer (rain, wind, frost, the variety) is in \(\operatorname{Pres}(\{p_5\})\). Only the variety edit is in \(\operatorname{Pres}(\{p_{open}\})\). Three caveats:
  1. "the containment need not be strict".
  2. It is an inclusion, not a count: "counting jobs is not a warrant", and no measure on \(\mathcal V\) is supplied.
  3. It registers the same enlargement for an honest limit (Iras, N6; Maya, N7) as for a retreat (Bruno, O1). It records that jobs were removed, not that they were removed after a failure. The earlier swap clause A-prime failed on exactly this: "a swap that works shows a limit is loose, not that it was fitted to failures; and the clause would refuse honest limits" (project story entry 29).
- [F] **The do-nothing patch on an open question: false.**
  - \(\operatorname{Pres}_{E0}(F)\) is fixed by E0, \(\mathcal V_0\), F and the world. Adopting a patch changes none of them. E_bad just picks a member of \(\mathcal V_0\) that is not in \(\operatorname{Pres}(\{p_{open}\})\). It registers as **not an account**, not as "easier to vary". EC:L244: "The patched account is not an account, as a fact, so it has no grade to lower."
  - E_good and E_bad differ only in X, so they have the same neighbours in \(\mathcal V_0\). No count of fitting neighbours separates them on either contract. On C_open the fitting set is {variety} for both. On C_5 it is the same large set for both.
  - On C_5, if both meet (F1), (F2) and (A), file 11 makes them "one account at grain \(C\)" (F11:L554). Draft 3 makes them different candidates "with one answer profile" (D3:L560). Either way: "the contract does not contain the distinction … The remedy is a finer contract, which is a new question" (F11:L558; D3:L562).
  - What separates good from bad is reach: E_good is in Pres for the extra jobs (a dry spring with the variety; a change of seed), and E_bad is not. That is a fact about the world, not visible from the five summers.
- [F] Also, "do-nothing" is not the theory's "does no work". A commitment that does no work "meets (E) exactly when it meets (E) without \(d\)" (D3:L313), so it cannot rescue anything. The wet-spring clause does work at the failed summer. Its fault is unfaithfulness on C_open, or confounding with rivals on C_5.

**(3) Can the file-00 limit be relaxed for an explanation and its own correction without becoming a ranking of different people's explanations?**
- [F] **No relaxation is needed for what can be had.** Written as edits of the old explanation, rescues are variants in one declared family, and the lemma applies as it stands (c). This compares contents in one family, not thinkers. It is not specific to "own" corrections, since a rival's edit of the same E0 sits in the same family.
- [F] **What cannot be had is "the correction is easier or harder to vary than the original"** with each taken as its own organization and family. File 00's reasons (no common set, counts that change under redescription, fixed interpretation) apply to one's own correction as fully as to strangers'. An ordering of members inside one family would need a measure on \(\mathcal V\). That is a merit function: "unsettled" in draft 3 (D3:L25, L516), withdrawn in file 00 (L1302).
- [I] **The owner's own framing assumes a record.** The comparison is meant for "its own" correction only, and what makes a content some explanation's own correction is history: which content was changed, after which failure. The theory tells provenance "by their histories, not their outputs" (F11:L15). So restricting the comparison to one's own corrections assumes the record that point (3) was meant to make unnecessary.

**Bottom line.**
- [F] The owner is right about the world-fixed facts. On a question that keeps its contract, (E) and reach keep a corrected mistake out of every account, with no record.
- [I] The owner is wrong that this makes a record of rescues redundant. The record does its work where those facts do not reach:
  1. claims made before any separating test (Situation 2: blocked as a fact, unmarked);
  2. changes of question, above all a narrowing to what was seen, bundled with a fitted patch (Situation 3, which passes (E)); Pres enlarges there by the lemma, but it grades nothing and registers honest limits in the same way;
  3. runs of rescues (O1, SILENT).
- [T] The texts already keep part of such a record: the historical index, the ban on unrecorded changes, the ban on backdated (EK), declared protected obligations, and in draft 3 the missing-input mark. [F] None of these says that a new question was shaped around a failure, or that a run of rescues is a retreat.

**Source check (Deutsch, for context).** [T] The harder an explanation is to vary, the harder it is to build a variant of it with a different reach (D p.29, paraphrased). **[CHANGED for the repository: quotation shortened to 25 words or fewer.]** Its predictions cannot be confined to a region one picks (D p.28, paraphrased). The confined variant "is no longer an explanation of seasons, just a (purported) rule of thumb" (D p.28). Had the good explanation been refuted, its defenders would have had no way out (D p.25, paraphrased). [F] The theory matches the first two in fact: reach is fixed by E and the world, and a narrowing changes the job claimed, not E's reach. It matches the third only in part: no interventions means no production question (D3:L151), and uniform seen cases fail non-circular dependence. It lets a confined narrowing bundled with a fitted patch pass (E).

*25 September: chained quotes shortened to keep within the 25-word rule (decision S19); meanings and page references kept.*

---

## Appendix B — The first models, with the scripts inlined (working file 02, copied unchanged except as noted)

### 02 Models — does a rescue ratchet? Pres before and after a correction, computed

*Working file, 24 September 2026. Not frozen. Nothing in the repository was changed. Scripts: `ratchet/models/m1_gardener.py`, `m2_seasons.py`, `cx_counterexamples.py` (Python 3.11, standard library only, run in a few seconds). Their full outputs are inlined in the appendix, verbatim. Read for this: file 11 Parts II, III, V, VI (F11:L95–315); file 00 "Support families" to "Hard-to-vary and reach" (F00:L248–385) and L1300; draft 3 Part VI (D3:L295–313); the error-correction analysis of 24 September (sections 0–4, Appendix A10–A11, Part C); N1, N2 of the N-case book; D3-T; Deutsch ch. 1, pp.21–28, by page marker. The Pinker folder was not opened.*

**Tags.** [COMPUTED] = an exact output of the scripts on the stated finite model. [PROVED] = a short general argument, given in section 6. [INFERENCE] = a reading, which could be wrong.

---

#### 0. The owner's position, checked

The position: a record of rescues is redundant, because a correction makes the mistake impossible to refit, and a bad rescue shows up as easier to vary by the measure that defines a good explanation.

1. **"A correction adds the failed case to the jobs, so any version that brings the mistake back fails."**
   - **True only at the failed pair itself.** [COMPUTED, PROVED] No version of any family that does the failed case repeats the old answer there. Once the old explanation is embedded, Pres also shrinks strictly: the old explanation is the witness. This holds in every family and model tried.
   - **False for the mistake as a whole.** [COMPUTED] E0's mistake covers four pairs (every sunny year with the early variety), not one. In a family rich enough to contain the "hybrid" version, Pres(J_after) holds versions that are right on every job and wrong exactly where E0 was wrong. Example: *sun = id, the early variety wins only in a wet windy spring*. Under a variety component that reads V, W and Wi, 56 of the 64 surviving versions do this. Adding the seed trial still leaves 24. Only when all four pairs are jobs does the count reach 0.
   - **The mistake is kept out only on the world's contract.** [COMPUTED] There it is kept out as a fact that nobody can see before a separating test. This is the analysis's "blocked as a fact, unmarked in the record", reached again.
2. **"A bad rescue registers as easier to vary."**
   - **False in general.** [COMPUTED, PROVED] On the recorded summers, wet, windy and early occur together. Swapping W and V maps the record onto itself, so any family that treats the two rescues alike gives the bad rescue exactly the Pres of the good one: 1:1, 4:4, 6:6, 64:64.
   - Under the port-swap family, "windy would fit as well" is true of the **good** rescue too: Pres = {wet, windy, early}.
   - The do-nothing patch has Pres = 1 in its natural single-exception family, the same as the good rescue.
   - The amended myth *shrinks* Pres, from 6 to 2. This is the same shape as the tilt's own honest correction (4 to 2), and after the amendment the myth is as small as the tilt (2 against 2).
   - The bad rescue registers as easier only when its part is given more ports than the good part. That is a choice of family, and the grid in CX3 flips both ways.
   - **The narrowing** registers only against the wider contract it left: 0 → 1. Its Pres equals the pre-failure Pres exactly, so without the recorded earlier index it looks like an honest narrow claim made from the start.
3. **The file-00 limit.** The embedding makes one comparison valid: the *later* explanation's family with more jobs, (H). There strictness is guaranteed. It does not yield the owner's comparisons:
   - Pres before and Pres after are **disjoint** in every rescue that added a part (all of M1's, and the myth's). They are never nested.
   - On fixed jobs, every added component makes Pres **weakly larger**, whether the rescue is good or bad.
   - It cannot separate a good from a bad rescue on the same record.
   - Nothing in it uses the fact that the correction is the author's *own*. It works for any extension. Organizations that are not extensions (tilt against myth) have no embedding unless an assembly rule is invented.

So, on these models, the Pres measure does not do the work that a record of rescues does. What separates the good rescue from the bad one is (A) on pairs that separate them: the world's contract, or a background job such as the seed trial that exercises the added part independently. That is a fact about answers, not a count of versions. [INFERENCE: whether this makes a record *necessary* is section 7.]

---

#### 1. What was modelled

**The theory's terms, made finite.**

| Term | In the models |
|---|---|
| Target D | M1: a garden with 16 settings (edit–boundary pairs): W wet/dry, Wi windy/calm, V the neighbour's variety late/early, Sun: the south wall sunny or shaded (an admitted intervention). M2: 6 pairs, place N/E/S × half-year H1/H2. |
| Truth | M1: north first iff the variety is early; otherwise the sunnier bed first. M2: the season is sign(latitude) × sign(half); the equator has none. |
| Candidate (organization) | A list of components, each a function on stated ports. M1: `sun` (the sunnier bed ripens first) plus *override* parts (if any fires, north first). M2 tilt: tilt t, latitude factor g, heating law h. M2 myth: schedule, grief u, and in the amended myth a destination d for the banished warmth. |
| Contract C / jobs | A job is one pair. "Account(E_v, job)" is read as **(A) at that pair**. (F1) is not modelled. Non-circular dependence (draft-3 S3 reading) is checked in M1 (i). |
| Variation family | The product of the stated menus of the organization's components. Each menu is written out in the script, and each result names its family. |
| Pres(F) | The versions in the family that answer every job in F as the target does. |

**M1 jobs.** Five good summers (dry, calm, late variety, sunny wall; one pair) plus one shading test make J_before. The sixth summer f* (wet, windy, early variety) failed. J_after = J_before + f*. C_full = all 16 settings. BG_seed is a seed trial (early variety in a dry calm spring gives north first). BG_rain is another wet spring with the late variety (south first). The narrowing is read as "my explanation only covered the summers seen before the failure", so C_narrow = J_before. A bare variant drops the shading test.

**M1 candidates.**
- E0: the sunnier bed first.
- E_good: E0 + variety override "early → north".
- E_bad: E0 + rain override "wet → north".
- E_patch: E0 + an exception that fires at f* only.
- E_narrow: E0 on C_narrow.

**M2 jobs.**
- J_greek: N in both halves.
- J_sailor: J_greek + the sailor's two southern pairs.
- J_world: all six pairs.
- The tilt also takes two component jobs outside the seasons question: BG_heat (a plate facing a lamp warms) and BG_elev (the Greek noon sun is high in H1). The myth takes none, since nothing but the seasons bears on Demeter.
- A hypothetical "in-phase" report tests Deutsch's "nowhere to go".

**M2 candidates.**
- T*: tilt, sphere, direct heating.
- The escape-clause tilt ("elsewhere the same", Deutsch pp.27–28), which is flat geometry on these places.
- M0: the original myth.
- M1: the amended myth, "she sends the warmth south and calls it home".
- The myth narrowed to Greece.

---

#### 2. M1, the gardener: results per rescue

Base stated family: `sun` = all 4 maps; the added part = all predicates on its own ports (variety reads V; rain reads W, the owner's "wet"; a second run lets rain read W and Wi); the exception = fires at one setting, or off. Embedding U = sun × var[V] × rain[W] × exc[single], |U| = 1088. Vers(E) = the points of U whose parts absent from E are off. [COMPUTED]

| Rescue | (i) (A) on its contract; (A) on C_full | (ii) \|Pres\| before (E0, J_before) → after (own family, J_after) | E0 in Pres after? | Surviving versions repeating E0's error elsewhere | (iii) (H) in U: Pres_E1(J_after) vs Pres_E1(J_before) | Pres_E0(J_before) vs Pres_E1(J_before) | Pres_E1(J_after) vs Pres_E0(J_before) | (iv) enlarges? |
|---|---|---|---|---|---|---|---|---|
| E_good (early → N), stated on C_full | yes; yes | 1 of 4 → 1 of 16 | no | 0 (but 56 of 64 when var reads V,W,Wi: CX1) | 2 → 1, strict | strictly inside (1 ⊊ 2) | disjoint | no (1 = 1) |
| E_bad (wet → N), rain reads W | yes on J_after; **no** on C_full (4 pairs) | 1 → 1 of 16 | no | 1 (itself) | 2 → 1, strict | strictly inside | disjoint | **no** (equal to E_good) |
| E_bad, rain reads W and Wi | yes on J_after; no | 1 → 4 of 64 | no | 4 | 8 → 4, strict | strictly inside | disjoint | yes (+3), only by the wider menu |
| E_patch, single-exception family | yes on J_after; no (3 pairs) | 1 → 1 of 68 | no | 1 (itself) | 17 → 1, strict | strictly inside | disjoint | **no** |
| E_patch, any-predicate family (4 ports) | yes on J_after; no | 1 → 24576 of 262144 | — | — | — | — | — | yes, only by the menu |
| E_narrow = E0 on C_narrow | yes, and non-circular (the shading test is the witness); **bare** records only: (A) yes, non-circular **no** | Pres(C_narrow) = Pres(J_before) = 1; Pres_E0(J_after) = 0 | is E0 | all 4 of E0's errors lie outside C_narrow | — | — | — | vs the failed contract yes (0 → 1); vs the pre-failure claim **equal** |

In the fully common family (every part of U free), Pres depends on the jobs alone:
- |Pres(J_before)| = 68, |Pres(J_after)| = 52, |Pres(J_after + BG_seed)| = 35, |Pres(C_full)| = 13.
- E_good, E_bad and E_patch are all members of Pres(J_after).
- Only E_good survives BG_seed or C_full.
- The 13 on C_full have one answer profile, inflated by idle exceptions (CX4).

For comparison, option (b) of the 24 September analysis. [COMPUTED]
- **Marked** (no consequence beyond the failed pair): E_patch (on any contract), E_narrow, and E_good and E_bad when their contract is confined to the record J_after.
- **Not marked:** E_good and E_bad on C_full (3 consequences each).

#### 3. M2, the seasons: results per rescue

| Candidate / rescue | (i) (A): J_greek / J_sailor / J_world | (ii) \|Pres\| before → after | Old version in Pres after? | Surviving versions keeping the old error | (iii) (H) | (iv) enlarges? |
|---|---|---|---|---|---|---|
| Myth amended, law family (d ∈ {none, S, E}) | yes / yes / **no** (equator) | own family 2 of 36 → 2 of 108. Embedded: Pres_M1(J_greek) = 6 → Pres_M1(J_sailor) = 2 | no (d = none excluded) | 2 of 2 keep M0's error at the equator | 6 → 2, strict. Pres_M1(J_sailor) vs Pres_M0(J_greek): disjoint | **no**: after = before (2 = 2), and it shrinks by 4 inside its family, as a correction does |
| Myth amended, table family (grief reads state and place) | same | 2 → 18 of 2916 | — | — | — | yes (+16), only by the menu |
| Myth narrowed to Greece (after the report) | yes on J_greek | Pres = 2, **equal** to before the report; vs J_sailor 0 → 2 | — | — | — | only against the wider contract |
| Tilt's own correction, escape → sphere (same organization: file 00 met), law menus | T*: yes / yes / yes; escape version fails the S pairs | 4 → 2 (T1); 2 → 1 (with BG) | no | 0 (law menus); 2 of 6 (table menus) | strict | no |

What Pres(J_greek) leaves open at the unseen southern pair S,H1, *before* the report. [COMPUTED]

| Family | Answers at S,H1 across Pres | In-phase report: \|Pres\| |
|---|---|---|
| Tilt, law menus (sphere or flat/escape) | summer, winter | 2 |
| Tilt, law menus + BG_heat, BG_elev | summer, winter | 1 |
| Tilt, one law everywhere (sphere only) + BG | winter only (right) | **0: nowhere to go** |
| Tilt, table menus + BG | all three | 6 |
| Myth, own organization (d = none) | summer only (wrong) | 2 |
| Myth, embedded (d free) | summer, winter | 4 |

On the sailor's jobs, the amended myth and the tilt are the same size (2 and 2 under law menus). Each Pres is one relabelling pair: myth (Persephone away in H1, her absence brings summer); tilt (t−1, inverse heating). BG_heat removes the tilt's relabelling. Nothing removes the myth's.

---

#### 4. The embedding (file 00's limit)

**What goes wrong naively.** [COMPUTED] The families before and after have different organizations:
- **Subset tests are ill-typed.** A version before is (sun); after it is (sun, override). As sets, Pres after ∩ Pres before is empty for every rescue, so a naive program says "not inside" for the good rescue too.
- **Answer profiles** are the only common currency. Every rescue changes the answer at f*, so "profiles after ⊆ profiles before" is False for all of them. On the old jobs, every surviving profile is the truth, so the sets are trivially equal.
- **Counts** say good = bad = patch = narrow = before (all 1).
- **Fractions** make the do-nothing patch the hardest to vary (1/68 against 1/16). They also make the amended myth *harder* to vary than the original (2/108 against 2/36).

**The embedding.** Take the later organization and put "off" (or a constant) in the added part's menu. The old explanation is then the new one with the part switched off. Redoing (ii)–(iv) inside it gives the following. [COMPUTED; PROVED in section 6]

- **Valid and useful.** (H) compares the later family on J_before and on J_after. The shrink is always **strict**: the embedded old explanation did J_before and fails f*. It is the witness file 00 said might be missing. This is the owner's point (1), exactly at the failed pair.
- **Not the owner's (iii).** On fixed jobs, Pres_E0(F) ⊆ Pres_E1(F) for every F, because Vers(E0) ⊆ Vers(E1). Adding a part never makes the explanation harder to vary on the old jobs. It was strictly easier in every rescue here (1 → 2 for good and bad alike; 1 → 17 for the patch; 2 → 6 for the myth).
- **Not a before/after order.** Pres_E1(J_after) and Pres_E0(J_before) were **disjoint** in every rescue that added a part (all of M1's, and the myth's). The only comparison left is counts, and counts depend on menus (CX3).
- **Not good against bad.** In the fully common family, Pres depends on the jobs alone. Good, bad and patch rescues are all members of Pres(J_after). The only thing that tells them apart is membership of Pres on a job set that separates them, and that is (A).
- **Not specific to one's own correction.** The construction needs only that the later organization *extends* the earlier one. E_good and E_bad are handled identically, and so would be a rival's extension. Relaxing the limit "for one's own correction" therefore does no formal work. What makes a correction one's own is its history. [INFERENCE] For organizations that are not extensions (tilt against myth), there is no embedding unless an assembly rule is invented, which would be the cross-theory ranking file 00 refused.
- **The added part's menu is a free choice**, and it decides (ii)–(iv): see CX1 and CX3.

**Verdict.** The embedding makes (H) meaningful between an explanation and its extension, with guaranteed strictness. That delivers the owner's point (1) at the failed pair and nothing more. It does not turn hard-to-vary into a ranking of people. It also does not rank the correction above the original, or the good rescue above the bad one.

---

#### 5. Counterexamples found

**CX1: a good correction that leaves the old mistake refittable.** [COMPUTED]
- E_good passes (A) on J_after (which holds f*) and on C_full.
- Let the variety part read V, W and Wi. That is natural: "does the early variety win in every spring?" is exactly what is unknown.
- Pres(J_after) then has 64 versions, and **56** of them give E0's wrong answer at some other early-variety sunny pair. Example: (sun=id, var = early∧wet∧windy) is wrong as E0 at 3 pairs.
- With the seed trial it is still 24. With every pair of M(E0) as a job it is 0, and on C_full it is 0.
- With V+W it is 2 of 4, e.g. "the early variety wins only in a wet spring".
- The owner's claim holds only under the poorest menu (var reads V: 0). There the family itself does the work.
- Two more instances:
  - M2: both surviving amended myths keep the original myth's error at the equator.
  - The tilt under table menus: 2 of 6 survivors repeat the escape version's error.

**CX2: bad rescues that do not enlarge Pres.** [COMPUTED, PROVED]
- (a) **The symmetry of the record.** Swapping W and V maps J_after onto itself and keeps its answers. For every family pair built alike, Pres_bad is the swap of Pres_good:
  - var[V] vs rain[W]: 1:1;
  - V+Wi vs W+Wi: 4:4;
  - V+Sun vs W+Sun: 6:6;
  - V+W+Wi vs W+V+Wi: 64:64.
  - The port-swap family gives Pres(J_after) = {wet, windy, early}: "windy would fit as well" is equally true of the good rescue.
  - The world breaks the symmetry (on C_full, Pres_bad = 0), and so does BG_seed (only "early" survives). Both do it through (A).
- (b) **The do-nothing patch**, single-exception family: |Pres| = 1, equal to the good rescue and to E0 before.
- (c) **The amended myth**, law family: Pres 6 → 2 in its family. After the amendment it equals the original's pre-report 2 and the tilt's 2. By the measure, the bad rescue looks like a correction.
- (d) **The narrowing**: Pres(C_narrow) = Pres(J_before). There is no enlargement relative to the claim before the failure.

**CX3: results that flip with the family.** [COMPUTED]
- **Grid of |Pres(J_after)|, good : bad.** The three swap-symmetric pairs are equal (1:1, 4:4, 6:6). Otherwise either direction appears: "bad easier" (e.g. 1:96) and "good easier" (e.g. 64:1).
- **Patch:** 1 (single exception) against 24576 (any predicate).
- **Amended myth:** 2 (law) against 18 (table).
- **Original myth before the report:** unanimous at the south in its own family ("hard to vary", and wrong), spread in the embedded family.
  - Deutsch's "slight variants … it has to go elsewhere – into the southern hemisphere" (D p.21) is a verdict in the *embedded* family.
- **Tilt:** unanimous at the south, with "nowhere to go" (D p.25), **only** in the family that admits one law everywhere.
  - With the escape clause admitted, the tilt with every background job still fits an in-phase report.
  - Deutsch excludes that variant because it is "no longer an explanation of seasons, just a (purported) rule of thumb" (D p.28). That is a restriction of the family, not a Pres count.
- **Leave-the-report-out:** it flags the tilt exactly as it flags the myth, unless the family is sphere-only.
- This matches Derivation 3: "what H leaves open about t is what T leaves open" (F11:L197). The family plays the part of the population.

**CX4: (H) non-strict, and idle parts in the count.** [COMPUTED]
- Adding a genuinely new job (BG_rain) to E_good's jobs excludes nothing (1 = 1).
- In the fully common family, Pres(C_full) has 13 members and one answer profile. Twelve of them carry an idle exception that fires where the answer is north anyway.

**CX5: history-free detection fails.** [COMPUTED]
- A leave-one-out test ("is the answer at x fixed by the other jobs?") does **not** flag the amended myth: each southern pair pins d for the other.
- Leaving out the sailor's report as a block does flag it, but that needs to know which jobs arrived together, which is history.
- In the gardener, leave-one-out flags good and bad alike on J_after (both open at f*). With BG_seed it separates them only because E_bad already fails (A).

---

#### 6. Four small facts behind the numbers [PROVED]

1. **Failed pair.** If f* ∈ F and E0 answered f* wrongly, no v ∈ Pres(F) repeats E0's answer at f*. If E0 ∈ V and E0 does F_old, then Pres(F_old ∪ {f*}) ⊊ Pres(F_old). *Proof:* Pres requires the right answer at f*, and E0 is in the second set but not the first. ∎
2. **Extension.** If Vers(E0) ⊆ Vers(E1) inside a common U, then Pres_E0(F) = Pres_U(F) ∩ Vers(E0) ⊆ Pres_U(F) ∩ Vers(E1) = Pres_E1(F) for every F. ∎ So on fixed jobs, adding a part can only enlarge Pres.
3. **Hybrid.** Suppose V contains h, which answers as E1 on F and as E0 on M(E0) \ F. Then h ∈ Pres(F), and h repeats E0's mistake on M(E0) \ F. Hence "the mistake cannot come back" holds for every family rich enough to hold hybrids iff M(E0) ⊆ F. ∎
4. **Symmetry.** Let σ be a permutation of the settings that maps F onto F and keeps the truth on F. Let σ map the good family onto the bad family, part by part. Then Pres_bad(F) = σ(Pres_good(F)), so every quantity computed from (V, F, Pres) is the same for both. ∎ On the gardener's record, σ is the W↔V swap.

#### 7. Bearing on the record of rescues [INFERENCE]

**What the models support.**
- (E) with (A) blocks the general bad rescue on an open question, as a fact. Neither Pres nor option (b) catches it before a separating test. Pres cannot catch it, by fact 4.
- What Pres can register depends on a remembered earlier job set:
  - the narrowing registers as an enlargement only against the recorded wider index;
  - the fitted myth registers only when the report is left out as a block.
- Both need the history of which jobs a change was fitted to. That is the content of a record of rescues. The theory already keeps part of it in the historical index.

**Where option (b) marks what Pres misses, and the reverse.**
- (b) marks the single-exception patch and the law-family myth; Pres does not.
- Pres "registers" the W+Wi bad rescue only through its wider menu; (b) does not mark it on C_full.
- So on these models the two are not redundant with each other, and the owner's ground for calling the record redundant ("by definition") does not hold.

**The owner's intuition holds under two conditions,** and then as (A) rather than as looseness:
- the family is law-like (one law everywhere), and
- background jobs exercise the added part independently (the seed trial; the lamp and the card).

Under those conditions a bad rescue is not "easier to vary": it fails outright (BG_seed; the in-phase report under the sphere-only family). That is Deutsch's "the best explanations are the ones that are most constrained by existing knowledge" (D p.26), read as more jobs.

#### 8. What I am unsure of

1. **Jobs are single pairs** and Account is read as (A) only. (F1) might exclude some versions counted here (for example rain anchored to rain). If so, it would shrink the bad rescue's Pres, not enlarge it. The direction of CX2 would stand.
2. **The menus are my statements.** The results are exact given them, and CX3 shows that they are what decides. A reader may hold that one menu is *the* right one. The theory supplies no rule that picks it, and the analysis's option (c) cost already says V becomes an assessor's input (D3:L516).
3. **The narrowing is read as "the summers seen before the failure".** If "the five recorded summers" includes the failure, E0 fails (A) on it. The analysis's Situation 3 (the bad rescue on the confined record) is covered as E_bad on J_after.
4. **The embedding uses a product family with "off" in the menu.** An embedding by a constant other than "off" gives the same containment facts (facts 1 and 2 need only Vers(E0) ⊆ Vers(E1)). Neighbourhood families (single edits of the candidate) were not run.
5. **Toy models.** A property shown in a finite model is a counterexample to a general claim. It is not evidence about how often real rescues behave so.

---

#### Appendix — script outputs, verbatim

##### `m1_gardener.py`

```text
==============================================================================
M1  THE GARDENER
==============================================================================
Settings: 16 = W{dry,wet} x Wi{calm,windy} x V{late,early} x Sun{sunS,shadeS}
Truth: N first iff V=early; otherwise the sunnier bed first.
E0 = (sun=id): the sunnier bed ripens first.
M(E0) = pairs where E0 is wrong = {dry/calm/early/sunS, dry/windy/early/sunS, wet/calm/early/sunS, wet/windy/early/sunS}
J_before (records + shading test) = {dry/calm/late/sunS, dry/calm/late/shadeS}
f* (the failed sixth summer)      = wet/windy/early/sunS
J_after = J_before + f*
C_full = all 16 settings (every admitted change of the named variables)
BG_seed = {dry/calm/early/sunS}  BG_rain = {wet/calm/late/sunS}

------------------------------------------------------------------------------
(i) THE (A) TEST AND NON-CIRCULAR DEPENDENCE, each candidate on its stated contract
------------------------------------------------------------------------------
E0 (before)                 on J_before                           (A)=True  NonCirc=True   x=dry/calm/late/shadeS, G=sun
E0 (after the failure)      on J_after                            (A)=False NonCirc=True   fails at {wet/windy/early/sunS}
E_good                      on C_full                             (A)=True  NonCirc=True   x=dry/calm/late/shadeS, G=sun
E_good                      on J_after                            (A)=True  NonCirc=True   x=dry/calm/late/shadeS, G=sun
E_bad (wet->N)              on C_full                             (A)=False NonCirc=True   fails at {dry/calm/early/sunS, dry/windy/early/sunS, wet/calm/late/sunS, wet/windy/late/sunS}
E_bad (wet->N)              on J_after (analysis Sit.3)           (A)=True  NonCirc=True   x=dry/calm/late/shadeS, G=sun
E_patch (exception at f*)   on C_full                             (A)=False NonCirc=True   fails at {dry/calm/early/sunS, dry/windy/early/sunS, wet/calm/early/sunS}
E_patch (exception at f*)   on J_after                            (A)=True  NonCirc=True   x=dry/calm/late/shadeS, G=sun
E_narrow = E0               on C_narrow (summers seen + shading)  (A)=True  NonCirc=True   x=dry/calm/late/shadeS, G=sun
E_narrow_bare = E0          on C_narrow_bare (summers seen only)  (A)=True  NonCirc=False  no pair of C changes the answer

------------------------------------------------------------------------------
(ii)-(iv) NAIVE: each candidate in its OWN family (different organizations)
------------------------------------------------------------------------------
Stated menus: sun = all 4 maps {S,N}->{S,N}; an override reading ports P = all
predicates on P (off included); the exception = fires at exactly one setting (or off).
E0 before                    |V|=     4  |Pres|=    1  fraction=0.2500
E0 after the failure         |V|=     4  |Pres|=    0  fraction=0.0000
E_good  [var reads V]        |V|=    16  |Pres|=    1  fraction=0.0625
E_bad   [rain reads W]       |V|=    16  |Pres|=    1  fraction=0.0625
E_bad   [rain reads W,Wi]    |V|=    64  |Pres|=    4  fraction=0.0625
E_patch [single exception]   |V|=    68  |Pres|=    1  fraction=0.0147
E_narrow (E0 on C_narrow)    |V|=     4  |Pres|=    1  fraction=0.2500
E_patch [any predicate, 4 ports] |V|=262144  |Pres|=24576  fraction=0.0938

Naive subset test Pres_after <= Pres_before: the elements are tuples of different
length (sun) vs (sun, override); as Python sets they are always disjoint:
   E_good  [var reads V]        Pres_after & Pres_before = empty  -> "after is not inside before" for every rescue
   E_bad   [rain reads W]       Pres_after & Pres_before = empty  -> "after is not inside before" for every rescue
   E_bad   [rain reads W,Wi]    Pres_after & Pres_before = empty  -> "after is not inside before" for every rescue
   E_patch [single exception]   Pres_after & Pres_before = empty  -> "after is not inside before" for every rescue
Answer profiles as the only common currency (profile on C_full):
   E_good  [var reads V]        profiles(after) inside profiles(before)? False
   E_bad   [rain reads W]       profiles(after) inside profiles(before)? False
   E_bad   [rain reads W,Wi]    profiles(after) inside profiles(before)? False
   E_patch [single exception]   profiles(after) inside profiles(before)? False
   (any rescue changes the answer at f*, so this is False for every rescue; restricted
    to J_before every surviving profile equals the truth, so it is trivially "equal".)

------------------------------------------------------------------------------
(v) EMBEDDING  U = sun x var[V] x rain[W] x exc[single]   |U| = 1088
    Vers(E) = points of U whose components absent from E are off.
------------------------------------------------------------------------------
E0: |Vers|=4  |Pres(J_before)|=1  |Pres(J_after)|=0  |Pres(C_narrow)|=1  |Pres(C_full)|=0

E_good = (sun=id, var=early, rain=off, exc=off)   |Vers|=16
  (ii)  |Pres(J_before)|=2  |Pres(J_after)|=1  |Pres(C_full)|=1
        E0 (added component off) in Pres(J_before)? True   in Pres(J_after)? False
        versions in Pres(J_after) that give E0's wrong answer at f*: 0
        versions in Pres(J_after) that give E0's wrong answer somewhere in M(E0): 0
  (iii) Pres(J_after) vs Pres(J_before) [same family, more jobs, (H)]: first STRICTLY INSIDE second
        Pres_E0(J_before) vs Pres_E_good(J_before) [old jobs, before vs after family]: first STRICTLY INSIDE second
        Pres_E_good(J_after) vs Pres_E0(J_before) [after on new jobs vs before on old]: disjoint
  (iv)  |Pres_E_good(J_after)| - |Pres_E0(J_before)| = +0 ;  vs E_good on J_after: +0
        does the candidate itself pass (A) on C_full? True

E_bad = (sun=id, var=off, rain=wet, exc=off)   |Vers|=16
  (ii)  |Pres(J_before)|=2  |Pres(J_after)|=1  |Pres(C_full)|=0
        E0 (added component off) in Pres(J_before)? True   in Pres(J_after)? False
        versions in Pres(J_after) that give E0's wrong answer at f*: 0
        versions in Pres(J_after) that give E0's wrong answer somewhere in M(E0): 1
           e.g. (sun=id, var=off, rain=wet, exc=off)  wrong as E0 at {dry/calm/early/sunS, dry/windy/early/sunS}
  (iii) Pres(J_after) vs Pres(J_before) [same family, more jobs, (H)]: first STRICTLY INSIDE second
        Pres_E0(J_before) vs Pres_E_bad(J_before) [old jobs, before vs after family]: first STRICTLY INSIDE second
        Pres_E_bad(J_after) vs Pres_E0(J_before) [after on new jobs vs before on old]: disjoint
  (iv)  |Pres_E_bad(J_after)| - |Pres_E0(J_before)| = +0 ;  vs E_good on J_after: +0
        does the candidate itself pass (A) on C_full? False

E_patch = (sun=id, var=off, rain=off, exc=only@wet/windy/early/sunS)   |Vers|=68
  (ii)  |Pres(J_before)|=17  |Pres(J_after)|=1  |Pres(C_full)|=0
        E0 (added component off) in Pres(J_before)? True   in Pres(J_after)? False
        versions in Pres(J_after) that give E0's wrong answer at f*: 0
        versions in Pres(J_after) that give E0's wrong answer somewhere in M(E0): 1
           e.g. (sun=id, var=off, rain=off, exc=only@wet/windy/early/sunS)  wrong as E0 at {dry/calm/early/sunS, dry/windy/early/sunS, wet/calm/early/sunS}
  (iii) Pres(J_after) vs Pres(J_before) [same family, more jobs, (H)]: first STRICTLY INSIDE second
        Pres_E0(J_before) vs Pres_E_patch(J_before) [old jobs, before vs after family]: first STRICTLY INSIDE second
        Pres_E_patch(J_after) vs Pres_E0(J_before) [after on new jobs vs before on old]: disjoint
  (iv)  |Pres_E_patch(J_after)| - |Pres_E0(J_before)| = +0 ;  vs E_good on J_after: +0
        does the candidate itself pass (A) on C_full? False

Narrowing in U: E_narrow = E0 on C_narrow.  Pres_E0(C_narrow) vs Pres_E0(J_before): equal;
   vs Pres_E0(J_after): first STRICTLY CONTAINS second (1 vs 0)

------------------------------------------------------------------------------
(v) EMBEDDING  U = sun x var[V] x rain[W,Wi] x exc[single]   |U| = 4352
    Vers(E) = points of U whose components absent from E are off.
------------------------------------------------------------------------------
E0: |Vers|=4  |Pres(J_before)|=1  |Pres(J_after)|=0  |Pres(C_narrow)|=1  |Pres(C_full)|=0

E_good = (sun=id, var=early, rain=off, exc=off)   |Vers|=16
  (ii)  |Pres(J_before)|=2  |Pres(J_after)|=1  |Pres(C_full)|=1
        E0 (added component off) in Pres(J_before)? True   in Pres(J_after)? False
        versions in Pres(J_after) that give E0's wrong answer at f*: 0
        versions in Pres(J_after) that give E0's wrong answer somewhere in M(E0): 0
  (iii) Pres(J_after) vs Pres(J_before) [same family, more jobs, (H)]: first STRICTLY INSIDE second
        Pres_E0(J_before) vs Pres_E_good(J_before) [old jobs, before vs after family]: first STRICTLY INSIDE second
        Pres_E_good(J_after) vs Pres_E0(J_before) [after on new jobs vs before on old]: disjoint
  (iv)  |Pres_E_good(J_after)| - |Pres_E0(J_before)| = +0 ;  vs E_good on J_after: +0
        does the candidate itself pass (A) on C_full? True

E_bad = (sun=id, var=off, rain=wet&calm|wet&windy, exc=off)   |Vers|=64
  (ii)  |Pres(J_before)|=8  |Pres(J_after)|=4  |Pres(C_full)|=0
        E0 (added component off) in Pres(J_before)? True   in Pres(J_after)? False
        versions in Pres(J_after) that give E0's wrong answer at f*: 0
        versions in Pres(J_after) that give E0's wrong answer somewhere in M(E0): 4
           e.g. (sun=id, var=off, rain=wet&windy, exc=off)  wrong as E0 at {dry/calm/early/sunS, dry/windy/early/sunS, wet/calm/early/sunS}
           e.g. (sun=id, var=off, rain=wet&calm|wet&windy, exc=off)  wrong as E0 at {dry/calm/early/sunS, dry/windy/early/sunS}
           e.g. (sun=id, var=off, rain=dry&windy|wet&windy, exc=off)  wrong as E0 at {dry/calm/early/sunS, wet/calm/early/sunS}
  (iii) Pres(J_after) vs Pres(J_before) [same family, more jobs, (H)]: first STRICTLY INSIDE second
        Pres_E0(J_before) vs Pres_E_bad(J_before) [old jobs, before vs after family]: first STRICTLY INSIDE second
        Pres_E_bad(J_after) vs Pres_E0(J_before) [after on new jobs vs before on old]: disjoint
  (iv)  |Pres_E_bad(J_after)| - |Pres_E0(J_before)| = +3 ;  vs E_good on J_after: +3
        does the candidate itself pass (A) on C_full? False

E_patch = (sun=id, var=off, rain=off, exc=only@wet/windy/early/sunS)   |Vers|=68
  (ii)  |Pres(J_before)|=17  |Pres(J_after)|=1  |Pres(C_full)|=0
        E0 (added component off) in Pres(J_before)? True   in Pres(J_after)? False
        versions in Pres(J_after) that give E0's wrong answer at f*: 0
        versions in Pres(J_after) that give E0's wrong answer somewhere in M(E0): 1
           e.g. (sun=id, var=off, rain=off, exc=only@wet/windy/early/sunS)  wrong as E0 at {dry/calm/early/sunS, dry/windy/early/sunS, wet/calm/early/sunS}
  (iii) Pres(J_after) vs Pres(J_before) [same family, more jobs, (H)]: first STRICTLY INSIDE second
        Pres_E0(J_before) vs Pres_E_patch(J_before) [old jobs, before vs after family]: first STRICTLY INSIDE second
        Pres_E_patch(J_after) vs Pres_E0(J_before) [after on new jobs vs before on old]: disjoint
  (iv)  |Pres_E_patch(J_after)| - |Pres_E0(J_before)| = +0 ;  vs E_good on J_after: +0
        does the candidate itself pass (A) on C_full? False

Narrowing in U: E_narrow = E0 on C_narrow.  Pres_E0(C_narrow) vs Pres_E0(J_before): equal;
   vs Pres_E0(J_after): first STRICTLY CONTAINS second (1 vs 0)

------------------------------------------------------------------------------
FULLY COMMON FAMILY: all of U free (Pres depends on the jobs only)
------------------------------------------------------------------------------
  |Pres(J_before (= C_narrow) )| =   68   members among named: E0, E_good, E_bad, E_patch
  |Pres(J_after               )| =   52   members among named: E_good, E_bad, E_patch
  |Pres(J_after + BG_seed     )| =   35   members among named: E_good
  |Pres(J_after + BG_rain     )| =   17   members among named: E_good, E_patch
  |Pres(C_full                )| =   13   members among named: E_good
  Pres(J_after) vs Pres(J_before): first STRICTLY INSIDE second  (the narrowing moves back from the first to the second)

------------------------------------------------------------------------------
COMPARISON: what the record of option (b) marks (no consequence beyond the failed pair)
------------------------------------------------------------------------------
  E_good   on C_full   consequences: 3   -> not marked
  E_good   on J_after  consequences: 0   -> MARKED (absorbed)
  E_bad    on C_full   consequences: 3   -> not marked
  E_bad    on J_after  consequences: 0   -> MARKED (absorbed)
  E_patch  on C_full   consequences: 0   -> MARKED (absorbed)
  E_patch  on J_after  consequences: 0   -> MARKED (absorbed)
  E_narrow: the limit follows from no component -> MARKED (absorbed)
```

##### `m2_seasons.py`

```text
==============================================================================
M2  THE SEASONS
==============================================================================
Truth: N,H1=summer, N,H2=winter, E,H1=none, E,H2=none, S,H1=winter, S,H2=summer
J_greek = {N,H1, N,H2}   J_sailor = J_greek + {S,H1, S,H2}   J_world = all 6 pairs

------------------------------------------------------------------------------
(i) THE (A) TEST
------------------------------------------------------------------------------
  Tilt T* (t+1, sphere, direct)    on J_greek  (A)=True  
  Tilt T* (t+1, sphere, direct)    on J_sailor (A)=True  
  Tilt T* (t+1, sphere, direct)    on J_world  (A)=True  
  Tilt with escape clause (flat)   on J_greek  (A)=True  
  Tilt with escape clause (flat)   on J_sailor (A)=False fails at {S,H1, S,H2}
  Tilt with escape clause (flat)   on J_world  (A)=False fails at {E,H1, E,H2, S,H1, S,H2}
  Myth M0 (original)               on J_greek  (A)=True  
  Myth M0 (original)               on J_sailor (A)=False fails at {S,H1, S,H2}
  Myth M0 (original)               on J_world  (A)=False fails at {E,H1, E,H2, S,H1, S,H2}
  Myth M1 (amended, d=S)           on J_greek  (A)=True  
  Myth M1 (amended, d=S)           on J_sailor (A)=True  
  Myth M1 (amended, d=S)           on J_world  (A)=False fails at {E,H1, E,H2}

------------------------------------------------------------------------------
(ii) Pres AND WHAT IT LEAVES OPEN AT UNSEEN PAIRS (spread = answers across Pres)
------------------------------------------------------------------------------
  tilt, law menus, no background jobs            |V|=   12  |Pres(J_greek )|=   4  spread {'S,H1': ['summer', 'winter'], 'E,H1': ['none', 'summer']}
  tilt, law menus, no background jobs            |V|=   12  |Pres(J_sailor)|=   2  spread {'E,H1': ['none']}
  tilt, law menus, no background jobs            |V|=   12  |Pres(J_world )|=   2  spread 
  tilt, law menus + BG_heat, BG_elev             |V|=   12  |Pres(J_greek )|=   2  spread {'S,H1': ['summer', 'winter'], 'E,H1': ['none', 'summer']}
  tilt, law menus + BG_heat, BG_elev             |V|=   12  |Pres(J_sailor)|=   1  spread {'E,H1': ['none']}
  tilt, law menus + BG_heat, BG_elev             |V|=   12  |Pres(J_world )|=   1  spread 
  tilt, sphere only (one law everywhere) + BG    |V|=    6  |Pres(J_greek )|=   1  spread {'S,H1': ['winter'], 'E,H1': ['none']}
  tilt, sphere only (one law everywhere) + BG    |V|=    6  |Pres(J_sailor)|=   1  spread {'E,H1': ['none']}
  tilt, sphere only (one law everywhere) + BG    |V|=    6  |Pres(J_world )|=   1  spread 
  tilt, TABLE menus (all g, all h) + BG          |V|= 2187  |Pres(J_greek )|=  18  spread {'S,H1': ['none', 'summer', 'winter'], 'E,H1': ['none', 'summer', 'winter']}
  tilt, TABLE menus (all g, all h) + BG          |V|= 2187  |Pres(J_sailor)|=   6  spread {'E,H1': ['none', 'summer', 'winter']}
  tilt, TABLE menus (all g, all h) + BG          |V|= 2187  |Pres(J_world )|=   2  spread 
  myth, original organization (d fixed none)     |V|=   36  |Pres(J_greek )|=   2  spread {'S,H1': ['summer'], 'E,H1': ['summer']}
  myth, original organization (d fixed none)     |V|=   36  |Pres(J_sailor)|=   0  spread {'E,H1': []}
  myth, original organization (d fixed none)     |V|=   36  |Pres(J_world )|=   0  spread 
  myth, amended organization (d in none,S,E)     |V|=  108  |Pres(J_greek )|=   6  spread {'S,H1': ['summer', 'winter'], 'E,H1': ['summer', 'winter']}
  myth, amended organization (d in none,S,E)     |V|=  108  |Pres(J_sailor)|=   2  spread {'E,H1': ['summer']}
  myth, amended organization (d in none,S,E)     |V|=  108  |Pres(J_world )|=   0  spread 
  myth amended, TABLE menu (grief reads state and place) |V|= 2916  |Pres(J_sailor)|=  18  spread {'E,H1': ['none', 'summer', 'winter']}

------------------------------------------------------------------------------
(ii)-(iv) THE MYTH'S RESCUE: naive (own families) and embedded (d switched to none)
------------------------------------------------------------------------------
  NAIVE own families: original on J_greek |Pres|=2 of 36 (0.0556); amended on J_sailor |Pres|=2 of 108 (0.0185)
  NAIVE, table menu for the amended grief: amended on J_sailor |Pres|=18 of 2916  (original: 2)
  EMBEDDED in the amended organization; Vers(M0) = d=none (36), Vers(M1) = all d (108):
    |Pres_M0(J_greek)|=2  |Pres_M0(J_sailor)|=0  |Pres_M1(J_greek)|=6  |Pres_M1(J_sailor)|=2
    M0 (d switched off) in Pres_M1(J_sailor)? False
    (iii) Pres_M1(J_sailor) vs Pres_M1(J_greek) [(H)]: first STRICTLY INSIDE second
          Pres_M0(J_greek) vs Pres_M1(J_greek) [old jobs]: first STRICTLY INSIDE second
          Pres_M1(J_sailor) vs Pres_M0(J_greek): disjoint
    (iv) |Pres_M1(J_sailor)| - |Pres_M0(J_greek)| = +0  -> the amendment does NOT enlarge Pres
         |Pres_M1(J_sailor)| - |Pres_M1(J_greek)| = -4  (the same shrink a correction shows)
    M(M0) = {E,H1, E,H2, S,H1, S,H2}
    versions in Pres_M1(J_sailor) that keep M0's wrong answer somewhere in M(M0): 2 of 2 (at E)
    spread of Pres_M1(J_greek) at the sailor's pairs: {'S,H1': ['summer', 'winter'], 'S,H2': ['summer', 'winter']}

------------------------------------------------------------------------------
THE TILT'S OWN CORRECTION (escape clause -> sphere): same organization, file 00 condition met
------------------------------------------------------------------------------
  tilt, law menus, no background jobs      |Pres(J_greek)|=4  |Pres(J_sailor)|=2  (H): first STRICTLY INSIDE second;  escape version in Pres(J_sailor)? False
  tilt, law menus + BG_heat, BG_elev       |Pres(J_greek)|=2  |Pres(J_sailor)|=1  (H): first STRICTLY INSIDE second;  escape version in Pres(J_sailor)? False
  M(escape version) = {E,H1, E,H2, S,H1, S,H2}
  tilt, law menus, no background jobs      versions in Pres(J_sailor) giving the escape version's wrong answer somewhere: 0 of 2
  tilt, law menus + BG_heat, BG_elev       versions in Pres(J_sailor) giving the escape version's wrong answer somewhere: 0 of 1
  tilt, TABLE menus (all g, all h) + BG    versions in Pres(J_sailor) giving the escape version's wrong answer somewhere: 2 of 6

------------------------------------------------------------------------------
"NOWHERE TO GO" (Deutsch p.25): a hypothetical report that the south is IN phase with Greece
------------------------------------------------------------------------------
  tilt, law menus, no background jobs            |Pres(in-phase report)| =   2  e.g. (t+1, flat/escape, direct)
  tilt, law menus + BG_heat, BG_elev             |Pres(in-phase report)| =   1  e.g. (t+1, flat/escape, direct)
  tilt, sphere only (one law everywhere) + BG    |Pres(in-phase report)| =   0  -> nowhere to go
  tilt, TABLE menus (all g, all h) + BG          |Pres(in-phase report)| =   6  e.g. (t+1, g+1+1+1, hs/w/n)
  myth, original organization (d fixed none)     |Pres(in-phase report)| =   2  e.g. (sched:ha, u:home->summer,away->winter, d=none)
  myth, amended organization (d in none,S,E)     |Pres(in-phase report)| =   4  e.g. (sched:ha, u:home->summer,away->winter, d=none)

------------------------------------------------------------------------------
TILT vs AMENDED MYTH on the jobs each now does
------------------------------------------------------------------------------
  tilt, law menus, no background jobs            |Pres(J_sailor)| = 2
  tilt, law menus + BG_heat, BG_elev             |Pres(J_sailor)| = 1
  tilt, sphere only (one law everywhere) + BG    |Pres(J_sailor)| = 1
  myth, amended organization (d in none,S,E)     |Pres(J_sailor)| = 2
      myth version in Pres: (sched:ha, u:home->summer,away->winter, d=S)
      myth version in Pres: (sched:ah, u:home->winter,away->summer, d=S)
      tilt version in Pres (T1): (t+1, sphere, direct)
      tilt version in Pres (T1): (t-1, sphere, inverse)

------------------------------------------------------------------------------
HISTORY-FREE vs HISTORY-USING detection of a fitted part
  LOO(x): is the answer at x fixed by Pres(F - {x})?  BLOCK: is it fixed by Pres(F - block)?
------------------------------------------------------------------------------
  amended myth (embedded family)   LOO at S,H1: answers ['winter']
  amended myth (embedded family)   LOO at S,H2: answers ['summer']
  amended myth (embedded family)   BLOCK (sailor's report left out): answers at S,H1 ['summer', 'winter'], at S,H2 ['summer', 'winter']
  tilt T1 (no background)          LOO at S,H1: answers ['winter']
  tilt T1 (no background)          LOO at S,H2: answers ['summer']
  tilt T1 (no background)          BLOCK (sailor's report left out): answers at S,H1 ['summer', 'winter'], at S,H2 ['summer', 'winter']
  tilt T2 (+BG)                    LOO at S,H1: answers ['winter']
  tilt T2 (+BG)                    LOO at S,H2: answers ['summer']
  tilt T2 (+BG)                    BLOCK (sailor's report left out): answers at S,H1 ['summer', 'winter'], at S,H2 ['summer', 'winter']
  tilt T3 (sphere only, +BG)       LOO at S,H1: answers ['winter']
  tilt T3 (sphere only, +BG)       LOO at S,H2: answers ['summer']
  tilt T3 (sphere only, +BG)       BLOCK (sailor's report left out): answers at S,H1 ['winter'], at S,H2 ['summer']

------------------------------------------------------------------------------
NARROWING: "the myth only covers Greece" (after the report)
------------------------------------------------------------------------------
  Pres_M0(J_greek) after narrowing vs before the report: equal (|2| vs |2|);  vs Pres_M0(J_sailor): first STRICTLY CONTAINS second (0)

------------------------------------------------------------------------------
OPTION (b) consequences (pairs of J_world other than the sailor's where the change matters)
------------------------------------------------------------------------------
  myth amendment d: none -> S        consequences {} -> MARKED (absorbed)
  tilt correction flat -> sphere     consequences {E,H1, E,H2} -> not marked
```

##### `cx_counterexamples.py`

```text
==============================================================================
CX1  A GOOD CORRECTION THAT LEAVES THE OLD MISTAKE REFITTABLE
==============================================================================

Family: sun x var[V]  |V|=16   E_good = (sun=id, var=early)
  E_good passes (A) on J_after (holds f*)? True   on C_full? True
  jobs = J_after + {}                                                         |Pres|=  1  mistake-reinstating=  0
  jobs = J_after + {dry/calm/early/sunS}                                      |Pres|=  1  mistake-reinstating=  0
  jobs = J_after + {dry/windy/early/sunS}                                     |Pres|=  1  mistake-reinstating=  0
  jobs = J_after + {wet/calm/early/sunS}                                      |Pres|=  1  mistake-reinstating=  0
  jobs = J_after + {dry/calm/early/sunS, dry/windy/early/sunS}                |Pres|=  1  mistake-reinstating=  0
  jobs = J_after + {dry/calm/early/sunS, wet/calm/early/sunS}                 |Pres|=  1  mistake-reinstating=  0
  jobs = J_after + {dry/windy/early/sunS, wet/calm/early/sunS}                |Pres|=  1  mistake-reinstating=  0
  jobs = J_after + {dry/calm/early/sunS, dry/windy/early/sunS, wet/calm/early/sunS} |Pres|=  1  mistake-reinstating=  0
  jobs = J_after + BG_seed (the seed trial)                                   |Pres|=  1  mistake-reinstating=  0
  jobs = C_full (the world's contract)                                        |Pres|=  1  mistake-reinstating=  0

Family: sun x var[V+W]  |V|=64   E_good = (sun=id, var=early&dry|early&wet)
  E_good passes (A) on J_after (holds f*)? True   on C_full? True
  jobs = J_after + {}                                                         |Pres|=  4  mistake-reinstating=  2
      e.g. (sun=id, var=early&wet)  gives E0's wrong S at {dry/calm/early/sunS, dry/windy/early/sunS}
  jobs = J_after + {dry/calm/early/sunS}                                      |Pres|=  2  mistake-reinstating=  0
  jobs = J_after + {dry/windy/early/sunS}                                     |Pres|=  2  mistake-reinstating=  0
  jobs = J_after + {wet/calm/early/sunS}                                      |Pres|=  4  mistake-reinstating=  2
  jobs = J_after + {dry/calm/early/sunS, dry/windy/early/sunS}                |Pres|=  2  mistake-reinstating=  0
  jobs = J_after + {dry/calm/early/sunS, wet/calm/early/sunS}                 |Pres|=  2  mistake-reinstating=  0
  jobs = J_after + {dry/windy/early/sunS, wet/calm/early/sunS}                |Pres|=  2  mistake-reinstating=  0
  jobs = J_after + {dry/calm/early/sunS, dry/windy/early/sunS, wet/calm/early/sunS} |Pres|=  2  mistake-reinstating=  0
  jobs = J_after + BG_seed (the seed trial)                                   |Pres|=  2  mistake-reinstating=  0
  jobs = C_full (the world's contract)                                        |Pres|=  1  mistake-reinstating=  0

Family: sun x var[V+W+Wi]  |V|=1024   E_good = (sun=id, var=early&dry&calm|early&dry&windy|early&wet&calm|early&wet&windy)
  E_good passes (A) on J_after (holds f*)? True   on C_full? True
  jobs = J_after + {}                                                         |Pres|= 64  mistake-reinstating= 56
      e.g. (sun=id, var=early&wet&windy)  gives E0's wrong S at {dry/calm/early/sunS, dry/windy/early/sunS, wet/calm/early/sunS}
  jobs = J_after + {dry/calm/early/sunS}                                      |Pres|= 32  mistake-reinstating= 24
  jobs = J_after + {dry/windy/early/sunS}                                     |Pres|= 32  mistake-reinstating= 24
  jobs = J_after + {wet/calm/early/sunS}                                      |Pres|= 32  mistake-reinstating= 24
  jobs = J_after + {dry/calm/early/sunS, dry/windy/early/sunS}                |Pres|= 16  mistake-reinstating=  8
  jobs = J_after + {dry/calm/early/sunS, wet/calm/early/sunS}                 |Pres|= 16  mistake-reinstating=  8
  jobs = J_after + {dry/windy/early/sunS, wet/calm/early/sunS}                |Pres|= 16  mistake-reinstating=  8
  jobs = J_after + {dry/calm/early/sunS, dry/windy/early/sunS, wet/calm/early/sunS} |Pres|=  8  mistake-reinstating=  0
  jobs = J_after + BG_seed (the seed trial)                                   |Pres|= 32  mistake-reinstating= 24
  jobs = C_full (the world's contract)                                        |Pres|=  1  mistake-reinstating=  0

  (check: in every family above no version in Pres(J_after) repeats E0's answer at f* itself)

==============================================================================
CX2  A BAD RESCUE THAT DOES NOT ENLARGE Pres: the record cannot tell wet from early
==============================================================================
swap(J_after) == J_after as a set? True ; truth kept on J_after under the swap? True
swap(C_full truth) == truth? False  (the world is not symmetric)
good reads     bad reads        |Pres_g|   |Pres_b| swap bijection |Pres_g|full |Pres_b|full
V              W                       1          1           True            1            0
V+Wi           W+Wi                    4          4           True            1            0
V+Sun          W+Sun                   6          6           True            5            0
V+W            W+V                     4          4           True            1            1
V+W+Wi         W+V+Wi                 64         64           True            1            1

Port-swap family (override fires on one literal): Pres(J_after) = ['(sun=id, cond=wet)', '(sun=id, cond=windy)', '(sun=id, cond=early)']
  -> "windy would fit as well" and "wet would fit as well" hold of the GOOD rescue too.
  with the seed trial BG_seed added: ['(sun=id, cond=early)']
  with another wet spring BG_rain added: ['(sun=id, cond=windy)', '(sun=id, cond=early)']

Do-nothing patch, single-exception family: |Pres(J_after)| = 1 (E_good with var[V]: 1; E0 before: 1)

==============================================================================
CX3  VERDICTS THAT FLIP WITH THE VARIATION FAMILY
==============================================================================
|Pres(J_after)| for E_good (rows: ports its variety component reads) vs E_bad (columns)
            bad:W           bad:W+Wi        bad:W+Sun       bad:W+Wi+Sun    
good:V      1:1 equal       1:4 bad easier  1:6 bad easier  1:96 bad easier 
good:V+Wi   4:1 good easier 4:4 equal       4:6 bad easier  4:96 bad easier 
good:V+Sun  6:1 good easier 6:4 good easier 6:6 equal       6:96 bad easier 
good:V+W+Wi 64:1 good easier64:4 good easier64:6 good easier64:96 bad easier

Do-nothing patch: single-exception family |Pres(J_after)|=1 ; any-predicate family |Pres(J_after)|=24576

==============================================================================
CX4  (H) NON-STRICT, AND IDLE PARTS IN THE COUNT
==============================================================================
E_good family sun x var[V]: Pres(J_after + BG_rain) vs Pres(J_after): equal (1 vs 1)
  -> a genuinely new job (another wet spring) is added and nothing is excluded.
Fully common family U: |Pres(C_full)| = 13, although only one answer profile survives:
    (sun=id, var=early, rain=off, exc=off)
    (sun=id, var=early, rain=off, exc=only@dry/calm/late/shadeS)
    (sun=id, var=early, rain=off, exc=only@dry/calm/early/sunS)
    (sun=id, var=early, rain=off, exc=only@dry/calm/early/shadeS)
    (sun=id, var=early, rain=off, exc=only@dry/windy/late/shadeS)
    (sun=id, var=early, rain=off, exc=only@dry/windy/early/sunS)
    (sun=id, var=early, rain=off, exc=only@dry/windy/early/shadeS)
    (sun=id, var=early, rain=off, exc=only@wet/calm/late/shadeS)
    (sun=id, var=early, rain=off, exc=only@wet/calm/early/sunS)
    (sun=id, var=early, rain=off, exc=only@wet/calm/early/shadeS)
    (sun=id, var=early, rain=off, exc=only@wet/windy/late/shadeS)
    (sun=id, var=early, rain=off, exc=only@wet/windy/early/sunS)
    (sun=id, var=early, rain=off, exc=only@wet/windy/early/shadeS)
  -> every surviving version gives the true answers; the count is inflated by idle
     exceptions that fire where the answer is N anyway (counting versions is no warrant).

==============================================================================
CX5  LEAVE-ONE-OUT (history-free) vs LEAVE-THE-FAILURE-OUT, gardener
==============================================================================
  jobs J_after            E_good var[V]  passes (A) on the jobs? True   answers at f* fixed by the other jobs: ['N', 'S']
  jobs J_after            E_bad rain[W]  passes (A) on the jobs? True   answers at f* fixed by the other jobs: ['N', 'S']
  jobs J_after + BG_seed  E_good var[V]  passes (A) on the jobs? True   answers at f* fixed by the other jobs: ['N']
  jobs J_after + BG_seed  E_bad rain[W]  passes (A) on the jobs? False  answers at f* fixed by the other jobs: []
```

#### Appendix — the scripts, inlined

*Added for the repository. The three scripts behind this file, and `m3_lemma_check.py`, which 03 added to the same folder, with its output. They are also in `Revision 2 - does correction stick - model scripts/models/`.*

##### `m1_gardener.py`

```python
#!/usr/bin/env python3
"""M1 - the gardener and the north bed.

Everything is finite and enumerated. Vocabulary follows files 00 and 11 and draft 3:

  target D      the garden. A 'setting' is one edit-boundary pair: the values of
                W (wet spring), Wi (windy spring), V (the neighbour's variety on the
                north side), Sun (which bed gets more sun; 'N' means the south wall
                has been shaded, an admitted intervention).
  truth         the neighbour's early variety makes the north bed ripen first,
                whatever the weather; otherwise the sunnier bed ripens first.
  candidate     an organization: a 'sun' component (maps the sunnier bed to the bed
                that ripens first) plus zero or more OVERRIDE components (each a
                predicate on the setting; if any override fires, the answer is N).
  job           one setting of a contract. Account(E_v, job) is read as (A) at that
                pair: the version's answer equals the target's answer.
  variation family
                the product of the stated menus of the organization's components.
  Pres(F)       the versions in the family that do every job in F.

The narrowing is read as: five good summers were recorded (plus one shading test),
the sixth summer failed, and the gardener then says her explanation only covered
the summers seen before it.
"""
from itertools import product, combinations

ORDER = ('W', 'Wi', 'V', 'Sun')
DOM = {'W': (0, 1), 'Wi': (0, 1), 'V': ('late', 'early'), 'Sun': ('S', 'N')}
WORD = {'W': {0: 'dry', 1: 'wet'}, 'Wi': {0: 'calm', 1: 'windy'},
        'V': {'late': 'late', 'early': 'early'}, 'Sun': {'S': 'sunS', 'N': 'shadeS'}}
POS = {k: i for i, k in enumerate(ORDER)}
SETTINGS = [tuple(v) for v in product(*(DOM[k] for k in ORDER))]
SIDX = {s: j for j, s in enumerate(SETTINGS)}
NS = len(SETTINGS)


def get(s, k):
    return s[POS[k]]


def show(s):
    return '/'.join(WORD[k][get(s, k)] for k in ORDER)


def truth(s):
    return 'N' if get(s, 'V') == 'early' else get(s, 'Sun')


TRUTH = tuple(truth(s) for s in SETTINGS)

# ---------------------------------------------------------------- menus
SUN_MENU = [('id', {'S': 'S', 'N': 'N'}), ('allS', {'S': 'S', 'N': 'S'}),
            ('allN', {'S': 'N', 'N': 'N'}), ('swap', {'S': 'N', 'N': 'S'})]


def fn_menu(ports):
    """All predicates on the listed ports (all functions config -> {fire, not})."""
    configs = list(product(*(DOM[p] for p in ports)))
    menu = []
    for outs in product((False, True), repeat=len(configs)):
        fires = frozenset(c for c, o in zip(configs, outs) if o)
        if not fires:
            label = 'off'
        elif len(fires) == len(configs):
            label = 'always'
        else:
            label = '|'.join(sorted('&'.join(WORD[p][v] for p, v in zip(ports, c)) for c in fires))
        bits = tuple(tuple(get(s, p) for p in ports) in fires for s in SETTINGS)
        menu.append((label, bits))
    return menu


def single_menu():
    """An exception that fires at exactly one setting (the 'do-nothing patch' family)."""
    menu = [('off', tuple(False for _ in SETTINGS))]
    for t in SETTINGS:
        menu.append(('only@' + show(t), tuple(s == t for s in SETTINGS)))
    return menu


LITERALS = [('wet', 'W', 1), ('dry', 'W', 0), ('windy', 'Wi', 1), ('calm', 'Wi', 0),
            ('early', 'V', 'early'), ('late', 'V', 'late')]


def literal_menu():
    """Port-swap family: the override fires on one literal ('wet' could be 'windy')."""
    menu = [('off', tuple(False for _ in SETTINGS))]
    for nm, k, v in LITERALS:
        menu.append((nm, tuple(get(s, k) == v for s in SETTINGS)))
    return menu


# ---------------------------------------------------------------- families
class Family:
    """Product of the menus of an organization's components. comps[0] is 'sun'."""

    def __init__(self, name, comps):
        self.name = name
        self.names = [n for n, _ in comps]
        self.menus = [m for _, m in comps]
        assert self.names[0] == 'sun'
        self.sun_out = [tuple(item[1][get(s, 'Sun')] for s in SETTINGS) for item in self.menus[0]]

    def size(self):
        n = 1
        for m in self.menus:
            n *= len(m)
        return n

    def versions(self, fixed=None):
        """fixed: dict comp-name -> menu label (e.g. {'rain': 'off'}) restricting the family."""
        ranges = []
        for n, m in zip(self.names, self.menus):
            if fixed and n in fixed:
                ranges.append([i for i, it in enumerate(m) if it[0] == fixed[n]])
            else:
                ranges.append(range(len(m)))
        return product(*ranges)

    def profile(self, v, deleted=()):
        """Answer at every setting. deleted: comp names removed (sun -> undetermined, override -> off)."""
        if 'sun' in deleted:
            sun = (None,) * NS
        else:
            sun = self.sun_out[v[0]]
        ovs = [self.menus[c][v[c]][1] for c in range(1, len(v)) if self.names[c] not in deleted]
        return tuple('N' if any(o[j] for o in ovs) else sun[j] for j in range(NS))

    def label(self, v):
        return '(' + ', '.join('%s=%s' % (n, self.menus[c][v[c]][0]) for c, n in enumerate(self.names)) + ')'

    def find(self, **labels):
        v = []
        for n, m in zip(self.names, self.menus):
            want = labels.get(n, 'off')
            v.append([i for i, it in enumerate(m) if it[0] == want][0])
        return tuple(v)


def does_jobs(prof, jobs):
    return all(prof[j] == TRUTH[j] for j in jobs)


def pres(fam, jobs, fixed=None):
    return [v for v in fam.versions(fixed) if does_jobs(fam.profile(v), jobs)]


def pres_count(fam, jobs, fixed=None):
    return sum(1 for v in fam.versions(fixed) if does_jobs(fam.profile(v), jobs))


# ---------------------------------------------------------------- jobs and contracts
def S(W, Wi, V, Sun):
    return SIDX[(W, Wi, V, Sun)]


B0 = S(0, 0, 'late', 'S')           # baseline: the five recorded summers (all alike)
SHADE = S(0, 0, 'late', 'N')        # her shading test
FSTAR = S(1, 1, 'early', 'S')       # the sixth summer: wet, windy, neighbour planted early
J_BEFORE = [B0, SHADE]
J_AFTER = J_BEFORE + [FSTAR]
C_FULL = list(range(NS))
C_NARROW = list(J_BEFORE)           # "only the summers seen" (with the shading test kept)
C_NARROW_BARE = [B0]                # "only the summers seen", shading test dropped
BG_SEED = [S(0, 0, 'early', 'S')]   # seed trial: early variety, dry calm spring -> N first
BG_RAIN = [S(1, 0, 'late', 'S')]    # another wet spring, late variety -> S first


def jl(jobs):
    return '{' + ', '.join(show(SETTINGS[j]) for j in jobs) + '}'


# ---------------------------------------------------------------- theory checks on one candidate
def a_test(fam, v, contract):
    prof = fam.profile(v)
    bad = [j for j in contract if prof[j] != TRUTH[j]]
    return (not bad), bad


def noncircular(fam, v, contract):
    """Draft-3 S3 reading: some pair x of C and block G of active components such that
    the answer at x differs from the answer at the baseline, and the contrast is lost
    (equal, or undetermined) when G is deleted."""
    if B0 not in contract:
        return False, 'baseline not in contract'
    active = ['sun'] + [n for c, n in enumerate(fam.names) if c > 0 and fam.menus[c][v[c]][0] != 'off']
    prof = fam.profile(v)
    for r in range(1, len(active) + 1):
        for G in combinations(active, r):
            dp = fam.profile(v, deleted=G)
            for x in contract:
                if prof[x] != prof[B0]:
                    if dp[x] is None or dp[B0] is None or dp[x] == dp[B0]:
                        return True, 'x=%s, G=%s' % (show(SETTINGS[x]), '+'.join(G))
    return False, 'no pair of C changes the answer'


def consequences(fam, v, comp, contract, failed):
    """Option (b) of the 24 September analysis: pairs of the later claim's own contract,
    other than the failed pairs, where deleting the added component changes the answer."""
    prof = fam.profile(v)
    dp = fam.profile(v, deleted=(comp,))
    return [j for j in contract if j not in failed and prof[j] != dp[j]]


def rel(A, B):
    A, B = set(A), set(B)
    if A == B:
        return 'equal'
    if A < B:
        return 'first STRICTLY INSIDE second'
    if A > B:
        return 'first STRICTLY CONTAINS second'
    if not (A & B):
        return 'disjoint'
    return 'incomparable (overlap %d)' % len(A & B)


def main():
    print('=' * 78)
    print('M1  THE GARDENER')
    print('=' * 78)
    print('Settings: %d = W{dry,wet} x Wi{calm,windy} x V{late,early} x Sun{sunS,shadeS}' % NS)
    print('Truth: N first iff V=early; otherwise the sunnier bed first.')
    fam0 = Family('E0 own', [('sun', SUN_MENU)])
    e0 = fam0.find(sun='id')
    p0 = fam0.profile(e0)
    MIST = [j for j in range(NS) if p0[j] != TRUTH[j]]
    print('E0 = (sun=id): the sunnier bed ripens first.')
    print('M(E0) = pairs where E0 is wrong =', jl(MIST))
    print('J_before (records + shading test) =', jl(J_BEFORE))
    print('f* (the failed sixth summer)      =', show(SETTINGS[FSTAR]))
    print('J_after = J_before + f*')
    print('C_full = all 16 settings (every admitted change of the named variables)')
    print('BG_seed =', jl(BG_SEED), ' BG_rain =', jl(BG_RAIN))

    # ------------------------------------------------------------ own families
    MV, MW, MWWi, MVWWi = fn_menu(('V',)), fn_menu(('W',)), fn_menu(('W', 'Wi')), fn_menu(('V', 'W', 'Wi'))
    MSING = single_menu()
    fam_good = Family('E_good own [var reads V]', [('sun', SUN_MENU), ('var', MV)])
    fam_bad = Family('E_bad own [rain reads W]', [('sun', SUN_MENU), ('rain', MW)])
    fam_bad2 = Family('E_bad own [rain reads W,Wi]', [('sun', SUN_MENU), ('rain', MWWi)])
    fam_patch = Family('E_patch own [exception at one setting]', [('sun', SUN_MENU), ('exc', MSING)])
    good = fam_good.find(sun='id', var='early')
    bad = fam_bad.find(sun='id', rain='wet')
    bad2 = fam_bad2.find(sun='id', rain='wet&calm|wet&windy')
    patch = fam_patch.find(sun='id', exc='only@' + show(SETTINGS[FSTAR]))

    print()
    print('-' * 78)
    print('(i) THE (A) TEST AND NON-CIRCULAR DEPENDENCE, each candidate on its stated contract')
    print('-' * 78)
    rows = [
        ('E0 (before)', fam0, e0, J_BEFORE, 'J_before'),
        ('E0 (after the failure)', fam0, e0, J_AFTER, 'J_after'),
        ('E_good', fam_good, good, C_FULL, 'C_full'),
        ('E_good', fam_good, good, J_AFTER, 'J_after'),
        ('E_bad (wet->N)', fam_bad, bad, C_FULL, 'C_full'),
        ('E_bad (wet->N)', fam_bad, bad, J_AFTER, 'J_after (analysis Sit.3)'),
        ('E_patch (exception at f*)', fam_patch, patch, C_FULL, 'C_full'),
        ('E_patch (exception at f*)', fam_patch, patch, J_AFTER, 'J_after'),
        ('E_narrow = E0', fam0, e0, C_NARROW, 'C_narrow (summers seen + shading)'),
        ('E_narrow_bare = E0', fam0, e0, C_NARROW_BARE, 'C_narrow_bare (summers seen only)'),
    ]
    for nm, fam, v, C, cn in rows:
        ok, badp = a_test(fam, v, C)
        nc, why = noncircular(fam, v, C)
        print('%-27s on %-34s (A)=%-5s NonCirc=%-5s  %s' % (nm, cn, ok, nc,
              ('fails at ' + jl(badp)) if badp else why))

    print()
    print('-' * 78)
    print('(ii)-(iv) NAIVE: each candidate in its OWN family (different organizations)')
    print('-' * 78)
    print('Stated menus: sun = all 4 maps {S,N}->{S,N}; an override reading ports P = all')
    print('predicates on P (off included); the exception = fires at exactly one setting (or off).')
    naive = [
        ('E0 before', fam0, J_BEFORE),
        ('E0 after the failure', fam0, J_AFTER),
        ('E_good  [var reads V]', fam_good, J_AFTER),
        ('E_bad   [rain reads W]', fam_bad, J_AFTER),
        ('E_bad   [rain reads W,Wi]', fam_bad2, J_AFTER),
        ('E_patch [single exception]', fam_patch, J_AFTER),
        ('E_narrow (E0 on C_narrow)', fam0, C_NARROW),
    ]
    for nm, fam, J in naive:
        n = pres_count(fam, J)
        print('%-28s |V|=%6d  |Pres|=%5d  fraction=%.4f' % (nm, fam.size(), n, n / fam.size()))
    # the all-functions exception family: 4 x 65536 versions
    MALL = fn_menu(('W', 'Wi', 'V', 'Sun'))
    fam_patch_all = Family('E_patch own [exception = any predicate on all 4 ports]', [('sun', SUN_MENU), ('exc', MALL)])
    n = pres_count(fam_patch_all, J_AFTER)
    print('%-28s |V|=%6d  |Pres|=%5d  fraction=%.4f' % ('E_patch [any predicate, 4 ports]', fam_patch_all.size(), n, n / fam_patch_all.size()))
    print()
    print('Naive subset test Pres_after <= Pres_before: the elements are tuples of different')
    print('length (sun) vs (sun, override); as Python sets they are always disjoint:')
    for nm, fam, J in naive[2:6]:
        A = set(pres(fam, J))
        B = set(pres(fam0, J_BEFORE))
        print('   %-28s Pres_after & Pres_before = %s  -> "after is not inside before" for every rescue' % (nm, A & B or 'empty'))
    print('Answer profiles as the only common currency (profile on C_full):')
    B = {fam0.profile(v) for v in pres(fam0, J_BEFORE)}
    for nm, fam, J in naive[2:6]:
        A = {fam.profile(v) for v in pres(fam, J)}
        print('   %-28s profiles(after) inside profiles(before)? %s' % (nm, A <= B))
    print('   (any rescue changes the answer at f*, so this is False for every rescue; restricted')
    print('    to J_before every surviving profile equals the truth, so it is trivially "equal".)')

    # ------------------------------------------------------------ embedding
    for tag, rain_menu in (('rain reads W', MW), ('rain reads W,Wi', MWWi)):
        U = Family('U', [('sun', SUN_MENU), ('var', MV), ('rain', rain_menu), ('exc', MSING)])
        print()
        print('-' * 78)
        print('(v) EMBEDDING  U = sun x var[V] x rain[%s] x exc[single]   |U| = %d' % (tag.split(' reads ')[1], U.size()))
        print('    Vers(E) = points of U whose components absent from E are off.')
        print('-' * 78)
        e0u = U.find(sun='id')
        rain_lab = 'wet' if rain_menu is MW else 'wet&calm|wet&windy'
        cands = {
            'E_good': (U.find(sun='id', var='early'), 'var'),
            'E_bad': (U.find(sun='id', rain=rain_lab), 'rain'),
            'E_patch': (U.find(sun='id', exc='only@' + show(SETTINGS[FSTAR])), 'exc'),
        }
        vers = {
            'E0': {'var': 'off', 'rain': 'off', 'exc': 'off'},
            'E_good': {'rain': 'off', 'exc': 'off'},
            'E_bad': {'var': 'off', 'exc': 'off'},
            'E_patch': {'var': 'off', 'rain': 'off'},
        }
        P0b = pres(U, J_BEFORE, vers['E0'])
        P0a = pres(U, J_AFTER, vers['E0'])
        print('E0: |Vers|=%d  |Pres(J_before)|=%d  |Pres(J_after)|=%d  |Pres(C_narrow)|=%d  |Pres(C_full)|=%d' % (
            len(list(U.versions(vers['E0']))), len(P0b), len(P0a), len(pres(U, C_NARROW, vers['E0'])),
            len(pres(U, C_FULL, vers['E0']))))
        goodPa = None
        for nm in ('E_good', 'E_bad', 'E_patch'):
            v1, comp = cands[nm]
            fx = vers[nm]
            nV = len(list(U.versions(fx)))
            Pb = pres(U, J_BEFORE, fx)
            Pa = pres(U, J_AFTER, fx)
            Pf = pres(U, C_FULL, fx)
            if nm == 'E_good':
                goodPa = Pa
            reinst_f = [v for v in Pa if U.profile(v)[FSTAR] == p0[FSTAR]]
            reinst_any = [v for v in Pa if any(U.profile(v)[j] == p0[j] for j in MIST)]
            print()
            print('%s = %s   |Vers|=%d' % (nm, U.label(v1), nV))
            print('  (ii)  |Pres(J_before)|=%d  |Pres(J_after)|=%d  |Pres(C_full)|=%d' % (len(Pb), len(Pa), len(Pf)))
            print('        E0 (added component off) in Pres(J_before)? %s   in Pres(J_after)? %s' % (e0u in Pb, e0u in Pa))
            print('        versions in Pres(J_after) that give E0\'s wrong answer at f*: %d' % len(reinst_f))
            print('        versions in Pres(J_after) that give E0\'s wrong answer somewhere in M(E0): %d' % len(reinst_any))
            for v in reinst_any[:3]:
                prof = U.profile(v)
                print('           e.g. %s  wrong as E0 at %s' % (U.label(v), jl([j for j in MIST if prof[j] == p0[j]])))
            print('  (iii) Pres(J_after) vs Pres(J_before) [same family, more jobs, (H)]: %s' % rel(Pa, Pb))
            print('        Pres_E0(J_before) vs Pres_%s(J_before) [old jobs, before vs after family]: %s' % (nm, rel(P0b, Pb)))
            print('        Pres_%s(J_after) vs Pres_E0(J_before) [after on new jobs vs before on old]: %s' % (nm, rel(Pa, P0b)))
            print('  (iv)  |Pres_%s(J_after)| - |Pres_E0(J_before)| = %+d ;  vs E_good on J_after: %+d' % (
                nm, len(Pa) - len(P0b), len(Pa) - len(goodPa)))
            print('        does the candidate itself pass (A) on C_full? %s' % (U.profile(v1) == TRUTH))
        print()
        print('Narrowing in U: E_narrow = E0 on C_narrow.  Pres_E0(C_narrow) vs Pres_E0(J_before): %s;'
              % rel(pres(U, C_NARROW, vers['E0']), P0b))
        print('   vs Pres_E0(J_after): %s (%d vs %d)' % (rel(pres(U, C_NARROW, vers['E0']), P0a),
                                                       len(pres(U, C_NARROW, vers['E0'])), len(P0a)))

    # ------------------------------------------------------------ fully common family
    U = Family('U', [('sun', SUN_MENU), ('var', MV), ('rain', MW), ('exc', MSING)])
    print()
    print('-' * 78)
    print('FULLY COMMON FAMILY: all of U free (Pres depends on the jobs only)')
    print('-' * 78)
    named = {'E0': U.find(sun='id'), 'E_good': U.find(sun='id', var='early'),
             'E_bad': U.find(sun='id', rain='wet'),
             'E_patch': U.find(sun='id', exc='only@' + show(SETTINGS[FSTAR]))}
    for jn, J in (('J_before (= C_narrow)', J_BEFORE), ('J_after', J_AFTER), ('J_after + BG_seed', J_AFTER + BG_SEED),
                  ('J_after + BG_rain', J_AFTER + BG_RAIN), ('C_full', C_FULL)):
        P = pres(U, J)
        members = [k for k, v in named.items() if v in P]
        print('  |Pres(%-22s)| = %4d   members among named: %s' % (jn, len(P), ', '.join(members) or '-'))
    print('  Pres(J_after) vs Pres(J_before): %s  (the narrowing moves back from the first to the second)' %
          rel(pres(U, J_AFTER), pres(U, J_BEFORE)))

    # ------------------------------------------------------------ option (b)
    print()
    print('-' * 78)
    print('COMPARISON: what the record of option (b) marks (no consequence beyond the failed pair)')
    print('-' * 78)
    for nm, fam, v, comp in (('E_good', fam_good, good, 'var'), ('E_bad', fam_bad, bad, 'rain'),
                             ('E_patch', fam_patch, patch, 'exc')):
        for cn, C in (('C_full', C_FULL), ('J_after', J_AFTER)):
            cons = consequences(fam, v, comp, C, [FSTAR])
            print('  %-8s on %-8s consequences: %-3d -> %s' % (nm, cn, len(cons),
                  'not marked' if cons else 'MARKED (absorbed)'))
    print('  E_narrow: the limit follows from no component -> MARKED (absorbed)')


if __name__ == '__main__':
    main()
```

##### `m2_seasons.py`

```python
#!/usr/bin/env python3
"""M2 - the seasons: the tilt explanation, the myth, and the myth amended.

Target D: three places N (Greece), E (the equator), S (far south) and two halves of
the year H1 (Greek summer months) and H2. Answer at a pair (place, half):
summer / winter / none. Truth (the tilt): season = sign(latitude) x sign(half),
with 0 meaning no seasons.

Tilt organization: tilt t in {+1, 0, -1}; latitude factor g (place -> {+1,0,-1});
heating law h (exposure in {+1,0,-1} -> season). season(p, half) = h[t * g(p) * s(half)].
The tilt also takes two component jobs outside the seasons question (Deutsch p.24:
"we know - and can test independently of our experience of seasons"):
  BG_heat : a plate facing a lamp warms, one turned away cools, one edge-on neither
            (pins h);
  BG_elev : the noon sun at N is high in H1 and low in H2 (pins t * g(N)).
The myth takes no such job: nothing but the seasons bears on Demeter's grief.

Myth organization: schedule (half -> Persephone away/home); grief u (away/home ->
season, the same everywhere); in the AMENDED organization also a destination d in
{none, S, E}: the place d gets the opposite of the rest of the world ("she sends the
warmth south, and calls it home"). The original myth is the amended organization
with d = none.
"""
from itertools import product

PLACES = ('N', 'E', 'S')
LAT = {'N': 1, 'E': 0, 'S': -1}
HALVES = ('H1', 'H2')
SG = {'H1': 1, 'H2': -1}
SEAS = {1: 'summer', -1: 'winter', 0: 'none'}
SEASONS = ('summer', 'winter', 'none')
OPP = {'summer': 'winter', 'winter': 'summer', 'none': 'none'}
PAIRS = [(p, h) for p in PLACES for h in HALVES]
TRUTH = {x: SEAS[LAT[x[0]] * SG[x[1]]] for x in PAIRS}

J_GREEK = [('N', 'H1'), ('N', 'H2')]
J_SAILOR = J_GREEK + [('S', 'H1'), ('S', 'H2')]
J_WORLD = list(PAIRS)
SAILOR_BLOCK = [('S', 'H1'), ('S', 'H2')]


def pl(xs):
    return '{' + ', '.join('%s,%s' % x for x in xs) + '}'


# ---------------------------------------------------------------- tilt
G_LAW = [('sphere', {'N': 1, 'E': 0, 'S': -1}), ('flat/escape', {'N': 1, 'E': 1, 'S': 1})]
G_SPHERE = G_LAW[:1]
G_TABLE = [('g' + ''.join('%+d' % v for v in vals), dict(zip(PLACES, vals))) for vals in product((1, 0, -1), repeat=3)]
H_LAW = [('direct', {1: 'summer', -1: 'winter', 0: 'none'}), ('inverse', {1: 'winter', -1: 'summer', 0: 'none'})]
H_TABLE = [('h' + '/'.join(v[0] for v in vals), dict(zip((1, -1, 0), vals))) for vals in product(SEASONS, repeat=3)]
T_MENU = [('t+1', 1), ('t0', 0), ('t-1', -1)]


class Tilt:
    kind = 'tilt'

    def __init__(self, name, gmenu, hmenu, background):
        self.name, self.gmenu, self.hmenu, self.bg = name, gmenu, hmenu, background

    def versions(self):
        return list(product(range(3), range(len(self.gmenu)), range(len(self.hmenu))))

    def ans(self, v, x):
        t = T_MENU[v[0]][1]
        g = self.gmenu[v[1]][1]
        h = self.hmenu[v[2]][1]
        return h[t * g[x[0]] * SG[x[1]]]

    def bg_ok(self, v):
        if not self.bg:
            return True
        t = T_MENU[v[0]][1]
        g = self.gmenu[v[1]][1]
        h = self.hmenu[v[2]][1]
        heat = h[1] == 'summer' and h[-1] == 'winter' and h[0] == 'none'
        elev = t * g['N'] * SG['H1'] == 1 and t * g['N'] * SG['H2'] == -1
        return heat and elev

    def label(self, v):
        return '(%s, %s, %s)' % (T_MENU[v[0]][0], self.gmenu[v[1]][0], self.hmenu[v[2]][0])

    def find(self, t, g, h):
        return ([i for i, m in enumerate(T_MENU) if m[0] == t][0], [i for i, m in enumerate(self.gmenu) if m[0] == g][0],
                [i for i, m in enumerate(self.hmenu) if m[0] == h][0])


# ---------------------------------------------------------------- myth
SCHED = [('sched:' + ''.join(a[0] for a in vals), dict(zip(HALVES, vals))) for vals in product(('home', 'away'), repeat=2)]
U_MENU = [('u:home->%s,away->%s' % vals, {'home': vals[0], 'away': vals[1]}) for vals in product(SEASONS, repeat=2)]


class Myth:
    """Law-like myth family: schedule x uniform grief x destination (menu stated per run)."""
    kind = 'myth'

    def __init__(self, name, dmenu):
        self.name, self.dmenu, self.bg = name, dmenu, False

    def versions(self):
        return list(product(range(len(SCHED)), range(len(U_MENU)), range(len(self.dmenu))))

    def ans(self, v, x):
        st = SCHED[v[0]][1][x[1]]
        s = U_MENU[v[1]][1][st]
        return OPP[s] if x[0] == self.dmenu[v[2]] else s

    def bg_ok(self, v):
        return True

    def label(self, v):
        return '(%s, %s, d=%s)' % (SCHED[v[0]][0], U_MENU[v[1]][0], self.dmenu[v[2]])

    def find(self, d):
        return ([i for i, m in enumerate(SCHED) if m[1] == {'H1': 'home', 'H2': 'away'}][0],
                [i for i, m in enumerate(U_MENU) if m[1] == {'home': 'summer', 'away': 'winter'}][0],
                self.dmenu.index(d))


class MythTable:
    """Table-like amended myth: grief reads (state, place); every table is a version."""
    kind = 'myth-table'

    def __init__(self, name):
        self.name, self.bg = name, False
        self.keys = [(st, p) for st in ('home', 'away') for p in PLACES]

    def versions(self):
        return list(product(range(len(SCHED)), product(SEASONS, repeat=len(self.keys))))

    def ans(self, v, x):
        st = SCHED[v[0]][1][x[1]]
        return dict(zip(self.keys, v[1]))[(st, x[0])]

    def bg_ok(self, v):
        return True


def pres(fam, jobs, only=None):
    vs = only if only is not None else fam.versions()
    return [v for v in vs if fam.bg_ok(v) and all(fam.ans(v, x) == TRUTH[x] for x in jobs)]


def spread(fam, P, xs):
    return {('%s,%s' % x): sorted({fam.ans(v, x) for v in P}) for x in xs}


def rel(A, B):
    A, B = set(A), set(B)
    if A == B:
        return 'equal'
    if A < B:
        return 'first STRICTLY INSIDE second'
    if A > B:
        return 'first STRICTLY CONTAINS second'
    if not (A & B):
        return 'disjoint'
    return 'incomparable (overlap %d)' % len(A & B)


def a_test(fam, v, jobs):
    bad = [x for x in jobs if fam.ans(v, x) != TRUTH[x]]
    return (not bad), bad


def main():
    print('=' * 78)
    print('M2  THE SEASONS')
    print('=' * 78)
    print('Truth:', ', '.join('%s,%s=%s' % (x[0], x[1], TRUTH[x]) for x in PAIRS))
    print('J_greek =', pl(J_GREEK), '  J_sailor = J_greek +', pl(SAILOR_BLOCK), '  J_world = all 6 pairs')

    T1 = Tilt('tilt, law menus, no background jobs', G_LAW, H_LAW, False)
    T2 = Tilt('tilt, law menus + BG_heat, BG_elev', G_LAW, H_LAW, True)
    T3 = Tilt('tilt, sphere only (one law everywhere) + BG', G_SPHERE, H_LAW, True)
    T4 = Tilt('tilt, TABLE menus (all g, all h) + BG', G_TABLE, H_TABLE, True)
    Mo = Myth('myth, original organization (d fixed none)', ['none'])
    Me = Myth('myth, amended organization (d in none,S,E)', ['none', 'S', 'E'])
    Mt = MythTable('myth amended, TABLE menu (grief reads state and place)')

    tstar = T1.find('t+1', 'sphere', 'direct')
    tesc = T1.find('t+1', 'flat/escape', 'direct')
    m0 = Me.find('none')
    m1 = Me.find('S')
    m0o = Mo.find('none')

    print()
    print('-' * 78)
    print('(i) THE (A) TEST')
    print('-' * 78)
    for nm, fam, v in (('Tilt T* (t+1, sphere, direct)', T1, tstar), ('Tilt with escape clause (flat)', T1, tesc),
                       ('Myth M0 (original)', Me, m0), ('Myth M1 (amended, d=S)', Me, m1)):
        for jn, J in (('J_greek', J_GREEK), ('J_sailor', J_SAILOR), ('J_world', J_WORLD)):
            ok, bad = a_test(fam, v, J)
            print('  %-32s on %-8s (A)=%-5s %s' % (nm, jn, ok, ('fails at ' + pl(bad)) if bad else ''))

    print()
    print('-' * 78)
    print('(ii) Pres AND WHAT IT LEAVES OPEN AT UNSEEN PAIRS (spread = answers across Pres)')
    print('-' * 78)
    unseen_g = [('S', 'H1'), ('E', 'H1')]
    for fam in (T1, T2, T3, T4, Mo, Me):
        for jn, J, look in (('J_greek', J_GREEK, unseen_g), ('J_sailor', J_SAILOR, [('E', 'H1')]),
                            ('J_world', J_WORLD, [])):
            P = pres(fam, J)
            print('  %-46s |V|=%5d  |Pres(%-8s)|=%4d  spread %s' % (fam.name, len(fam.versions()), jn, len(P),
                                                                   spread(fam, P, look) if look else ''))
    P = pres(Mt, J_SAILOR)
    print('  %-46s |V|=%5d  |Pres(J_sailor)|=%4d  spread %s' % (Mt.name, len(Mt.versions()), len(P),
                                                               spread(Mt, P, [('E', 'H1')])))

    print()
    print('-' * 78)
    print('(ii)-(iv) THE MYTH\'S RESCUE: naive (own families) and embedded (d switched to none)')
    print('-' * 78)
    Pb_own = pres(Mo, J_GREEK)
    Pa_own = pres(Me, J_SAILOR)
    print('  NAIVE own families: original on J_greek |Pres|=%d of %d (%.4f); amended on J_sailor |Pres|=%d of %d (%.4f)'
          % (len(Pb_own), len(Mo.versions()), len(Pb_own) / len(Mo.versions()), len(Pa_own), len(Me.versions()),
             len(Pa_own) / len(Me.versions())))
    Pa_tab = pres(Mt, J_SAILOR)
    print('  NAIVE, table menu for the amended grief: amended on J_sailor |Pres|=%d of %d  (original: %d)' % (
        len(Pa_tab), len(Mt.versions()), len(Pb_own)))
    vers0 = [v for v in Me.versions() if Me.dmenu[v[2]] == 'none']
    P0b = pres(Me, J_GREEK, vers0)
    P0a = pres(Me, J_SAILOR, vers0)
    P1b = pres(Me, J_GREEK)
    P1a = pres(Me, J_SAILOR)
    print('  EMBEDDED in the amended organization; Vers(M0) = d=none (%d), Vers(M1) = all d (%d):' % (len(vers0), len(Me.versions())))
    print('    |Pres_M0(J_greek)|=%d  |Pres_M0(J_sailor)|=%d  |Pres_M1(J_greek)|=%d  |Pres_M1(J_sailor)|=%d' % (
        len(P0b), len(P0a), len(P1b), len(P1a)))
    print('    M0 (d switched off) in Pres_M1(J_sailor)? %s' % (m0 in P1a))
    print('    (iii) Pres_M1(J_sailor) vs Pres_M1(J_greek) [(H)]: %s' % rel(P1a, P1b))
    print('          Pres_M0(J_greek) vs Pres_M1(J_greek) [old jobs]: %s' % rel(P0b, P1b))
    print('          Pres_M1(J_sailor) vs Pres_M0(J_greek): %s' % rel(P1a, P0b))
    print('    (iv) |Pres_M1(J_sailor)| - |Pres_M0(J_greek)| = %+d  -> the amendment does %s enlarge Pres' % (
        len(P1a) - len(P0b), 'NOT' if len(P1a) <= len(P0b) else ''))
    print('         |Pres_M1(J_sailor)| - |Pres_M1(J_greek)| = %+d  (the same shrink a correction shows)' % (len(P1a) - len(P1b)))
    old_mist = [x for x in PAIRS if Me.ans(m0, x) != TRUTH[x]]
    print('    M(M0) =', pl(old_mist))
    keep = [v for v in P1a if any(Me.ans(v, x) == Me.ans(m0, x) for x in old_mist)]
    print('    versions in Pres_M1(J_sailor) that keep M0\'s wrong answer somewhere in M(M0): %d of %d (at E)' % (len(keep), len(P1a)))
    print('    spread of Pres_M1(J_greek) at the sailor\'s pairs:', spread(Me, P1b, SAILOR_BLOCK))

    print()
    print('-' * 78)
    print('THE TILT\'S OWN CORRECTION (escape clause -> sphere): same organization, file 00 condition met')
    print('-' * 78)
    for fam in (T1, T2):
        Pg = pres(fam, J_GREEK)
        Ps = pres(fam, J_SAILOR)
        print('  %-40s |Pres(J_greek)|=%d  |Pres(J_sailor)|=%d  (H): %s;  escape version in Pres(J_sailor)? %s' % (
            fam.name, len(Pg), len(Ps), rel(Ps, Pg), tesc in Ps))
    esc_mist = [x for x in PAIRS if T1.ans(tesc, x) != TRUTH[x]]
    print('  M(escape version) =', pl(esc_mist))
    for fam in (T1, T2, T4):
        Ps = pres(fam, J_SAILOR)
        # the escape version's answers, computed directly (it is (t+1, flat, direct))
        esc_ans = {x: T1.ans(tesc, x) for x in PAIRS}
        keep = [v for v in Ps if any(fam.ans(v, x) == esc_ans[x] for x in esc_mist)]
        print('  %-40s versions in Pres(J_sailor) giving the escape version\'s wrong answer somewhere: %d of %d' % (
            fam.name, len(keep), len(Ps)))

    print()
    print('-' * 78)
    print('"NOWHERE TO GO" (Deutsch p.25): a hypothetical report that the south is IN phase with Greece')
    print('-' * 78)
    inphase = {('N', 'H1'): 'summer', ('N', 'H2'): 'winter', ('S', 'H1'): 'summer', ('S', 'H2'): 'winter'}
    for fam in (T1, T2, T3, T4, Mo, Me):
        P = [v for v in fam.versions() if fam.bg_ok(v) and all(fam.ans(v, x) == a for x, a in inphase.items())]
        ex = fam.label(P[0]) if P and hasattr(fam, 'label') else ''
        print('  %-46s |Pres(in-phase report)| = %3d  %s' % (fam.name, len(P), ('e.g. ' + ex) if ex else '-> nowhere to go'))

    print()
    print('-' * 78)
    print('TILT vs AMENDED MYTH on the jobs each now does')
    print('-' * 78)
    for fam in (T1, T2, T3):
        print('  %-46s |Pres(J_sailor)| = %d' % (fam.name, len(pres(fam, J_SAILOR))))
    print('  %-46s |Pres(J_sailor)| = %d' % (Me.name, len(P1a)))
    for v in P1a:
        print('      myth version in Pres:', Me.label(v))
    for v in pres(T1, J_SAILOR):
        print('      tilt version in Pres (T1):', T1.label(v))

    print()
    print('-' * 78)
    print('HISTORY-FREE vs HISTORY-USING detection of a fitted part')
    print('  LOO(x): is the answer at x fixed by Pres(F - {x})?  BLOCK: is it fixed by Pres(F - block)?')
    print('-' * 78)
    for nm, fam in (('amended myth (embedded family)', Me), ('tilt T1 (no background)', T1), ('tilt T2 (+BG)', T2),
                    ('tilt T3 (sphere only, +BG)', T3)):
        for x in SAILOR_BLOCK:
            P = pres(fam, [y for y in J_SAILOR if y != x])
            print('  %-32s LOO at %s,%s: answers %s' % (nm, x[0], x[1], sorted({fam.ans(v, x) for v in P})))
        P = pres(fam, J_GREEK)
        print('  %-32s BLOCK (sailor\'s report left out): answers at S,H1 %s, at S,H2 %s' % (
            nm, sorted({fam.ans(v, ('S', 'H1')) for v in P}), sorted({fam.ans(v, ('S', 'H2')) for v in P})))

    print()
    print('-' * 78)
    print('NARROWING: "the myth only covers Greece" (after the report)')
    print('-' * 78)
    Pn = pres(Mo, J_GREEK)
    print('  Pres_M0(J_greek) after narrowing vs before the report: %s (|%d| vs |%d|);  vs Pres_M0(J_sailor): %s (%d)' % (
        rel(Pn, Pb_own), len(Pn), len(Pb_own), rel(Pn, pres(Mo, J_SAILOR)), len(pres(Mo, J_SAILOR))))

    print()
    print('-' * 78)
    print('OPTION (b) consequences (pairs of J_world other than the sailor\'s where the change matters)')
    print('-' * 78)
    cons_m = [x for x in J_WORLD if x not in SAILOR_BLOCK and Me.ans(m1, x) != Me.ans(m0, x)]
    cons_t = [x for x in J_WORLD if x not in SAILOR_BLOCK and T1.ans(tstar, x) != T1.ans(tesc, x)]
    print('  myth amendment d: none -> S        consequences %s -> %s' % (pl(cons_m), 'not marked' if cons_m else 'MARKED (absorbed)'))
    print('  tilt correction flat -> sphere     consequences %s -> %s' % (pl(cons_t), 'not marked' if cons_t else 'MARKED (absorbed)'))


if __name__ == '__main__':
    main()
```

##### `cx_counterexamples.py`

```python
#!/usr/bin/env python3
"""Counterexample hunt on the gardener model (M1). Uses the machinery of m1_gardener.py.

CX1  a good correction (passes (A) on a contract holding the failed case) that leaves
     the old mistake refittable;
CX2  a bad rescue that does not enlarge Pres under any family treating the two
     rescues alike (a symmetry of the record);
CX3  verdicts that flip with the variation family;
CX4  the containment (H) holding non-strictly (file 00's caveat), and what idle
     parts do to the counts;
CX5  a history-free test (leave-one-out) against the history-using test (leave the
     failure out) on the gardener.
"""
from itertools import combinations, product
from m1_gardener import (Family, SUN_MENU, fn_menu, single_menu, literal_menu, SETTINGS, NS, TRUTH, show, jl, get,
                         pres, pres_count, J_BEFORE, J_AFTER, C_FULL, FSTAR, BG_SEED, BG_RAIN, B0, SIDX, rel)

fam0 = Family('E0', [('sun', SUN_MENU)])
P0 = fam0.profile(fam0.find(sun='id'))
MIST = [j for j in range(NS) if P0[j] != TRUTH[j]]


def reinstating(fam, P):
    return [v for v in P if any(fam.profile(v)[j] == P0[j] for j in MIST)]


def cx1():
    print('=' * 78)
    print('CX1  A GOOD CORRECTION THAT LEAVES THE OLD MISTAKE REFITTABLE')
    print('=' * 78)
    for ports in (('V',), ('V', 'W'), ('V', 'W', 'Wi')):
        fam = Family('E_good, var reads %s' % '+'.join(ports), [('sun', SUN_MENU), ('var', fn_menu(ports))])
        # the correct variety component: fires exactly when V=early (the unique version with the true profile
        # and sun=id; it is also the unique one whose override fires on every early config and no late one)
        good = [v for v in fam.versions() if fam.profile(v) == TRUTH and fam.label(v).startswith('(sun=id')
                and all(fam.menus[1][v[1]][1][j] == (get(SETTINGS[j], 'V') == 'early') for j in range(NS))][0]
        print('\nFamily: sun x var[%s]  |V|=%d   E_good = %s' % ('+'.join(ports), fam.size(), fam.label(good)))
        print('  E_good passes (A) on J_after (holds f*)? %s   on C_full? %s' % (
            all(fam.profile(good)[j] == TRUTH[j] for j in J_AFTER), fam.profile(good) == TRUTH))
        rest = [j for j in MIST if j != FSTAR]
        for r in range(len(rest) + 1):
            for T in combinations(rest, r):
                J = J_AFTER + list(T)
                P = pres(fam, J)
                R = reinstating(fam, P)
                tag = 'jobs = J_after + ' + (jl(T) if T else '{}')
                line = '  %-75s |Pres|=%3d  mistake-reinstating=%3d' % (tag, len(P), len(R))
                if R and r == 0:
                    ex = R[0]
                    line += '\n      e.g. %s  gives E0\'s wrong S at %s' % (fam.label(ex), jl([j for j in MIST if fam.profile(ex)[j] == P0[j]]))
                print(line)
        P = pres(fam, J_AFTER + BG_SEED)
        print('  %-75s |Pres|=%3d  mistake-reinstating=%3d' % ('jobs = J_after + BG_seed (the seed trial)', len(P), len(reinstating(fam, P))))
        P = pres(fam, C_FULL)
        print('  %-75s |Pres|=%3d  mistake-reinstating=%3d' % ('jobs = C_full (the world\'s contract)', len(P), len(reinstating(fam, P))))
        # sanity: nothing in Pres(J_after) repeats the mistake AT f*
        assert not [v for v in pres(fam, J_AFTER) if fam.profile(v)[FSTAR] == P0[FSTAR]]
    print('\n  (check: in every family above no version in Pres(J_after) repeats E0\'s answer at f* itself)')


def swap_setting(s):
    """Exchange the roles of W and V: W=0<->late, W=1<->early."""
    W, Wi, V, Sun = s
    return ({'late': 0, 'early': 1}[V], Wi, {0: 'late', 1: 'early'}[W], Sun)


def cx2():
    print()
    print('=' * 78)
    print('CX2  A BAD RESCUE THAT DOES NOT ENLARGE Pres: the record cannot tell wet from early')
    print('=' * 78)
    sw = {SIDX[s]: SIDX[swap_setting(s)] for s in SETTINGS}
    print('swap(J_after) == J_after as a set? %s ; truth kept on J_after under the swap? %s' % (
        set(sw[j] for j in J_AFTER) == set(J_AFTER), all(TRUTH[sw[j]] == TRUTH[j] for j in J_AFTER)))
    print('swap(C_full truth) == truth? %s  (the world is not symmetric)' % all(TRUTH[sw[j]] == TRUTH[j] for j in C_FULL))
    pairs = [(('V',), ('W',)), (('V', 'Wi'), ('W', 'Wi')), (('V', 'Sun'), ('W', 'Sun')), (('V', 'W'), ('W', 'V')),
             (('V', 'W', 'Wi'), ('W', 'V', 'Wi'))]
    print('%-14s %-14s %10s %10s %14s %12s %12s' % ('good reads', 'bad reads', '|Pres_g|', '|Pres_b|', 'swap bijection',
                                                 '|Pres_g|full', '|Pres_b|full'))
    for pg, pb in pairs:
        fg = Family('g', [('sun', SUN_MENU), ('var', fn_menu(pg))])
        fb = Family('b', [('sun', SUN_MENU), ('rain', fn_menu(pb))])
        Pg = pres(fg, J_AFTER)
        Pb = pres(fb, J_AFTER)
        # map each good-version profile through the swap and compare the profile multisets on C_full
        prof_g = sorted(tuple(fg.profile(v)[sw[j]] for j in range(NS)) for v in Pg)
        prof_b = sorted(fb.profile(v) for v in Pb)
        print('%-14s %-14s %10d %10d %14s %12d %12d' % ('+'.join(pg), '+'.join(pb), len(Pg), len(Pb), prof_g == prof_b,
                                                     pres_count(fg, C_FULL), pres_count(fb, C_FULL)))
    fl = Family('lit', [('sun', SUN_MENU), ('cond', literal_menu())])
    P = pres(fl, J_AFTER)
    print('\nPort-swap family (override fires on one literal): Pres(J_after) =', [fl.label(v) for v in P])
    print('  -> "windy would fit as well" and "wet would fit as well" hold of the GOOD rescue too.')
    P = pres(fl, J_AFTER + BG_SEED)
    print('  with the seed trial BG_seed added:', [fl.label(v) for v in P])
    P = pres(fl, J_AFTER + BG_RAIN)
    print('  with another wet spring BG_rain added:', [fl.label(v) for v in P])
    fp = Family('patch', [('sun', SUN_MENU), ('exc', single_menu())])
    print('\nDo-nothing patch, single-exception family: |Pres(J_after)| = %d (E_good with var[V]: %d; E0 before: %d)' % (
        pres_count(fp, J_AFTER), pres_count(Family('g', [('sun', SUN_MENU), ('var', fn_menu(('V',)))]), J_AFTER),
        pres_count(fam0, J_BEFORE)))


def cx3():
    print()
    print('=' * 78)
    print('CX3  VERDICTS THAT FLIP WITH THE VARIATION FAMILY')
    print('=' * 78)
    gp = [('V',), ('V', 'Wi'), ('V', 'Sun'), ('V', 'W', 'Wi')]
    bp = [('W',), ('W', 'Wi'), ('W', 'Sun'), ('W', 'Wi', 'Sun')]
    print('|Pres(J_after)| for E_good (rows: ports its variety component reads) vs E_bad (columns)')
    print('%-12s' % '' + ''.join('%-16s' % ('bad:' + '+'.join(b)) for b in bp))
    cache_b = {b: pres_count(Family('b', [('sun', SUN_MENU), ('rain', fn_menu(b))]), J_AFTER) for b in bp}
    for g in gp:
        ng = pres_count(Family('g', [('sun', SUN_MENU), ('var', fn_menu(g))]), J_AFTER)
        cells = []
        for b in bp:
            nb = cache_b[b]
            verdict = 'bad easier' if nb > ng else ('good easier' if ng > nb else 'equal')
            cells.append('%d:%d %-10s' % (ng, nb, verdict))
        print('%-12s' % ('good:' + '+'.join(g)) + ''.join('%-16s' % c for c in cells))
    fpa = Family('patch-all', [('sun', SUN_MENU), ('exc', fn_menu(('W', 'Wi', 'V', 'Sun')))])
    fps = Family('patch-single', [('sun', SUN_MENU), ('exc', single_menu())])
    print('\nDo-nothing patch: single-exception family |Pres(J_after)|=%d ; any-predicate family |Pres(J_after)|=%d'
          % (pres_count(fps, J_AFTER), pres_count(fpa, J_AFTER)))


def cx4():
    print()
    print('=' * 78)
    print('CX4  (H) NON-STRICT, AND IDLE PARTS IN THE COUNT')
    print('=' * 78)
    fg = Family('g', [('sun', SUN_MENU), ('var', fn_menu(('V',)))])
    A = pres(fg, J_AFTER)
    B = pres(fg, J_AFTER + BG_RAIN)
    print('E_good family sun x var[V]: Pres(J_after + BG_rain) vs Pres(J_after): %s (%d vs %d)'
          % (rel(B, A), len(B), len(A)))
    print('  -> a genuinely new job (another wet spring) is added and nothing is excluded.')
    U = Family('U', [('sun', SUN_MENU), ('var', fn_menu(('V',))), ('rain', fn_menu(('W',))), ('exc', single_menu())])
    P = pres(U, C_FULL)
    print('Fully common family U: |Pres(C_full)| = %d, although only one answer profile survives:' % len(P))
    for v in P:
        print('   ', U.label(v))
    print('  -> every surviving version gives the true answers; the count is inflated by idle')
    print('     exceptions that fire where the answer is N anyway (counting versions is no warrant).')


def cx5():
    print()
    print('=' * 78)
    print('CX5  LEAVE-ONE-OUT (history-free) vs LEAVE-THE-FAILURE-OUT, gardener')
    print('=' * 78)
    fams = [('E_good var[V]', Family('g', [('sun', SUN_MENU), ('var', fn_menu(('V',)))])),
            ('E_bad rain[W]', Family('b', [('sun', SUN_MENU), ('rain', fn_menu(('W',)))]))]
    for jn, J in (('J_after', J_AFTER), ('J_after + BG_seed', J_AFTER + BG_SEED)):
        for nm, fam in fams:
            P = pres(fam, [j for j in J if j != FSTAR])
            ans = sorted({fam.profile(v)[FSTAR] for v in P})
            Pfull = pres(fam, J)
            print('  jobs %-18s %-14s passes (A) on the jobs? %-5s  answers at f* fixed by the other jobs: %s' % (
                jn, nm, bool(Pfull), ans))


if __name__ == '__main__':
    cx1()
    cx2()
    cx3()
    cx4()
    cx5()
```

##### `m3_lemma_check.py`

```python
#!/usr/bin/env python3
"""M3 - check the proposed lemma "Correction in a common family" (H*) and its stated limits
against the finite models of m1_gardener.py and m2_seasons.py.

The proposed statement (plain form):
  Let V be a declared family of edits of the later organization E1 that contains a member v0
  giving the earlier organization E0. If E0 does every job in F and fails a job f*, then
  v0 is in Pres(F) and not in Pres(F + f*), so Pres(F + f*) is strictly inside Pres(F).
  If E1 does f* and the correction only adds a block B, then B is critical for f* in E1.
  Same argument with the identity edit as witness: a narrowing that omits a job its own
  candidate fails restores a strictly larger Pres.
Limits stated with it:
  (i)   a member of Pres(F + f*) may fail another job g that E0 fails (hybrids);
  (ii)  on the same jobs, the family of E0 inside V has Pres no larger than V's (extension);
  (iii) two extensions that both do F + f* are both in Pres(F + f*); only a job one fails separates them;
  (iv)  without v0 in V the strictness is not guaranteed.
Jobs are sets of pairs (a contract); Account(E_v, job) is read as (A) on every pair of it.
"""
import random
from itertools import combinations, product
from m1_gardener import (Family, SUN_MENU, fn_menu, single_menu, SETTINGS, NS, TRUTH, show, get,
                         J_BEFORE, J_AFTER, C_FULL, C_NARROW, FSTAR, BG_SEED, B0)
import m2_seasons as m2

random.seed(24)
FULL = (1 << NS) - 1


def mask(js):
    m = 0
    for j in js:
        m |= 1 << j
    return m


def okmask(fam, v):
    prof = fam.profile(v)
    return mask(j for j in range(NS) if prof[j] == TRUTH[j])


def build(fam):
    vs = list(fam.versions())
    return vs, [okmask(fam, v) for v in vs]


def pres_idx(masks, F):
    return {i for i, m in enumerate(masks) if m & F == F}


fam0 = Family('E0', [('sun', SUN_MENU)])
E0PROF = fam0.profile(fam0.find(sun='id'))
R0 = [j for j in range(NS) if E0PROF[j] == TRUTH[j]]       # pairs E0 gets right (12)
M0 = [j for j in range(NS) if E0PROF[j] != TRUTH[j]]       # pairs E0 gets wrong (4)
MR0, MM0 = mask(R0), mask(M0)


def v0_index(fam, vs):
    want = fam.find(sun='id')                               # every added part 'off'
    return vs.index(want)


def check_lemma(fam, label, n_contracts=400):
    vs, ms = build(fam)
    i0 = v0_index(fam, vs)
    n_checked = 0
    fails = 0
    min_gap = None
    # (1) every F within the pairs E0 gets right (all 4096 subsets; a sample of 300 for large families),
    #     every single failed pair f*
    allF = [mask(Fs) for r in range(len(R0) + 1) for Fs in combinations(R0, r)]
    if len(vs) > 5000:
        allF = random.sample(allF, 300)
    for F in allF:
        if True:
            cntF = sum(1 for m in ms if m & F == F)
            for fs in M0:
                Fp = F | (1 << fs)
                cntFp = sum(1 for m in ms if m & Fp == Fp)
                n_checked += 1
                in_F = ms[i0] & F == F
                in_Fp = ms[i0] & Fp == Fp
                if not (in_F and not in_Fp and cntFp < cntF):
                    fails += 1
                gap = cntF - cntFp
                min_gap = gap if min_gap is None else min(min_gap, gap)
    # (2) f* as a whole question: random contracts that hold at least one failed pair
    for _ in range(n_contracts):
        F = mask(random.sample(R0, random.randint(0, len(R0))))
        C = mask(random.sample(range(NS), random.randint(1, NS)))
        if not C & MM0:
            C |= 1 << random.choice(M0)
        Fp = F | C
        cntF = sum(1 for m in ms if m & F == F)
        cntFp = sum(1 for m in ms if m & Fp == Fp)
        n_checked += 1
        if not ((ms[i0] & F == F) and not (ms[i0] & Fp == Fp) and cntFp < cntF):
            fails += 1
    print('  %-44s |V|=%6d  instances checked=%6d  failures of (H*)=%d  min strict gap=%d'
          % (label, len(vs), n_checked, fails, min_gap))
    return fails


def hybrids(fam, label, F, fstar_contract):
    vs, ms = build(fam)
    Fp = F | fstar_contract
    P = [i for i, m in enumerate(ms) if m & Fp == Fp]
    rest = MM0 & ~Fp
    H = [i for i in P if (~ms[i]) & rest]
    return len(P), len(H), (fam.label(vs[H[0]]) if H else '')


def extension(fam, label):
    vs, ms = build(fam)
    v0set = {i for i, v in enumerate(vs)
             if all(fam.menus[c][v[c]][0] == 'off' for c in range(1, len(fam.names)))}
    strict = equal = bad = 0
    for F in range(1 << NS):
        P = {i for i, m in enumerate(ms) if m & F == F}
        P0 = P & v0set
        if not P0 <= P:
            bad += 1
        elif P0 < P:
            strict += 1
        else:
            equal += 1
    print('  %-44s all 65536 job sets F: Pres_V0(F) inside Pres_V(F) always? %s   strictly larger for %d, equal for %d'
          % (label, bad == 0, strict, equal))


def main():
    print('=' * 100)
    print('M3  THE PROPOSED LEMMA (H*) AND ITS LIMITS, CHECKED ON THE MODELS')
    print('=' * 100)
    print('E0 right at %d pairs, wrong at %d: %s' % (len(R0), len(M0), ', '.join(show(SETTINGS[j]) for j in M0)))

    MV, MW, MWWi = fn_menu(('V',)), fn_menu(('W',)), fn_menu(('W', 'Wi'))
    families = [
        ('U1 = sun x var[V] x rain[W] x exc[single]', Family('U1', [('sun', SUN_MENU), ('var', MV), ('rain', MW), ('exc', single_menu())])),
        ('U2 = sun x var[V] x rain[W,Wi] x exc[single]', Family('U2', [('sun', SUN_MENU), ('var', MV), ('rain', MWWi), ('exc', single_menu())])),
        ('E_good rich = sun x var[V,W,Wi]', Family('g3', [('sun', SUN_MENU), ('var', fn_menu(('V', 'W', 'Wi')))])),
        ('redescribed: sun x rainA[W] x rainB[W]', Family('split', [('sun', SUN_MENU), ('rainA', MW), ('rainB', MW)])),
        ('redescribed x10: sun x rain1..rain5[W]', Family('split5', [('sun', SUN_MENU)] + [('rain%d' % k, MW) for k in range(1, 6)])),
    ]
    grid_ports = [('V',), ('V', 'Wi'), ('V', 'Sun'), ('V', 'W', 'Wi')]
    grid_bad = [('W',), ('W', 'Wi'), ('W', 'Sun'), ('W', 'Wi', 'Sun')]
    for gp in grid_ports:
        for bp in grid_bad:
            f = Family('grid', [('sun', SUN_MENU), ('var', fn_menu(gp)), ('rain', fn_menu(bp))])
            if f.size() <= 70000:
                families.append(('grid sun x var[%s] x rain[%s]' % ('+'.join(gp), '+'.join(bp)), f))

    print('\n' + '-' * 100)
    print('(1) (H*): every F that E0 does, every f* that E0 fails (single failed pairs, and random whole contracts')
    print('    holding a failed pair). Strict containment with the embedded E0 as witness?')
    print('-' * 100)
    total = 0
    for label, fam in families:
        total += check_lemma(fam, label, n_contracts=200 if fam.size() > 5000 else 400)
    print('  TOTAL failures of (H*) across all families: %d' % total)

    print('\n' + '-' * 100)
    print('(1b) Counts on the gardener\'s own jobs (F = J_before, f* = the failed summer): strict in every family,')
    print('     while the SIZE of the gap depends on the menus')
    print('-' * 100)
    for label, fam in families[:5]:
        vs, ms = build(fam)
        F, Fp = mask(J_BEFORE), mask(J_AFTER)
        a = sum(1 for m in ms if m & F == F)
        b = sum(1 for m in ms if m & Fp == Fp)
        print('  %-44s |Pres(J_before)|=%5d  |Pres(J_after)|=%5d' % (label, a, b))

    print('\n' + '-' * 100)
    print('(iv) NEGATIVE CONTROLS: drop a hypothesis and strictness is no longer guaranteed')
    print('-' * 100)
    MV_noff = [it for it in MV if it[0] != 'off']
    famN = Family('noV0', [('sun', SUN_MENU), ('var', MV_noff)])
    vs, ms = build(famN)
    F, Fp = mask(J_BEFORE), mask(J_AFTER)
    a = {i for i, m in enumerate(ms) if m & F == F}
    b = {i for i, m in enumerate(ms) if m & Fp == Fp}
    print('  no v0 (var menu without "off"): Pres(J_before)=%s  Pres(J_after)=%s  strict? %s'
          % ([famN.label(vs[i]) for i in a], [famN.label(vs[i]) for i in b], b < a))
    famG = Family('gv', [('sun', SUN_MENU), ('var', MV)])
    vs, ms = build(famG)
    i0 = v0_index(famG, vs)
    # hypothesis "E0 does F" dropped: F already holds a failed pair (a job added after an earlier correction)
    F = mask(J_BEFORE + [M0[0]])
    Fp = F | (1 << M0[1])
    a = {i for i, m in enumerate(ms) if m & F == F}
    b = {i for i, m in enumerate(ms) if m & Fp == Fp}
    print('  E0 does not do F (sun x var[V]; F = J_before + %s; f* = %s): E0 in Pres(F)? %s  |Pres(F)|=%d  |Pres(F+f*)|=%d  strict? %s'
          % (show(SETTINGS[M0[0]]), show(SETTINGS[M0[1]]), ms[i0] & F == F, len(a), len(b), b < a))
    b2 = {i for i, m in enumerate(ms) if m & (mask(J_AFTER) | mask([s for s in range(NS) if get(SETTINGS[s], 'V') == 'late' and get(SETTINGS[s], 'W') == 1])) == (mask(J_AFTER) | mask([s for s in range(NS) if get(SETTINGS[s], 'V') == 'late' and get(SETTINGS[s], 'W') == 1]))}
    a2 = {i for i, m in enumerate(ms) if m & mask(J_AFTER) == mask(J_AFTER)}
    print('  a new job no member fails (sun x var[V]; wet springs with the late variety added to J_after): |Pres| %d -> %d, strict? %s  (file 00\'s non-strict case)'
          % (len(a2), len(b2), b2 < a2))
    fam = families[0][1]
    vs, ms = build(fam)
    i0 = v0_index(fam, vs)
    # a job E0 already does: (H) only, and non-strict (file 00's caveat)
    F = mask(J_AFTER)
    Fp = F | mask([s for s in range(NS) if get(SETTINGS[s], 'V') == 'late' and get(SETTINGS[s], 'W') == 1])
    a = {i for i, m in enumerate(ms) if m & F == F}
    b = {i for i, m in enumerate(ms) if m & Fp == Fp}
    print('  added job that E0 does (wet springs, late variety) on F = J_after: |Pres|=%d -> %d, strict? %s'
          % (len(a), len(b), b < a))

    print('\n' + '-' * 100)
    print('(i) HYBRIDS: members of Pres(F + f*) that fail another job E0 fails')
    print('-' * 100)
    for label, fam in families[:3]:
        n, h, ex = hybrids(fam, label, mask(J_BEFORE), 1 << FSTAR)
        n2, h2, _ = hybrids(fam, label, mask(J_BEFORE), mask(C_FULL))
        print('  %-44s f* = the failed summer: %4d in Pres, %4d hybrids %s' % (label, n, h, ('e.g. ' + ex) if ex else ''))
        print('  %-44s f* = the open question (all 16 pairs): %4d in Pres, %4d hybrids' % ('', n2, h2))

    print('\n' + '-' * 100)
    print('(ii) EXTENSION: on the same jobs, the embedded family of E0 never has the larger Pres')
    print('-' * 100)
    for label, fam in families[:3]:
        extension(fam, label)

    print('\n' + '-' * 100)
    print('(iii) GOOD AGAINST BAD in one family (U1): same witness, both kept; only a job one fails separates them')
    print('-' * 100)
    fam = families[0][1]
    vs, ms = build(fam)
    good = vs.index(fam.find(sun='id', var='early'))
    bad = vs.index(fam.find(sun='id', rain='wet'))
    patch = vs.index(fam.find(sun='id', exc='only@' + show(SETTINGS[FSTAR])))
    for nm, J in (('J_after', J_AFTER), ('J_after + seed trial', J_AFTER + BG_SEED), ('C_full', C_FULL)):
        P = pres_idx(ms, mask(J))
        print('  Pres(%-22s) |%4d|  E_good in? %-5s  E_bad in? %-5s  E_patch in? %s'
              % (nm, len(P), good in P, bad in P, patch in P))

    print('\n' + '-' * 100)
    print('NARROWING instance (identity edit as witness)')
    print('-' * 100)
    vs0, ms0 = build(fam0)
    e0 = vs0.index(fam0.find(sun='id'))
    a = pres_idx(ms0, mask(C_NARROW))
    b = pres_idx(ms0, mask(C_NARROW) | (1 << FSTAR))
    print('  E0 narrowed to the summers seen: |Pres(C_narrow)|=%d  |Pres(C_narrow + f*)|=%d  witness E0? %s'
          % (len(a), len(b), e0 in a and e0 not in b))
    print('  same set as the claim BEFORE the failure (Pres(J_before))? %s  -> the inclusion does not say whether the'
          % (a == pres_idx(ms0, mask(J_BEFORE))))
    print('     omitted job was dropped after a failure or never claimed; only the historical index says which')
    a = pres_idx(ms, mask(J_AFTER))
    b = pres_idx(ms, mask(C_FULL))
    print('  Situation 3 (E_bad confined to the recorded summers, open question dropped), U1: |Pres(J_after)|=%d'
          ' |Pres(J_after + open question)|=%d  witness E_bad? %s' % (len(a), len(b), bad in a and bad not in b))
    print('     the same inclusion has E_good\'s honest confinement to J_after inside it: E_good in both? %s'
          % (good in a and good in b))

    print('\n' + '-' * 100)
    print('COMPANION: the added block is critical for f* (B), and not critical for the old jobs')
    print('-' * 100)
    for nm, lab in (('E_good', dict(sun='id', var='early')), ('E_bad', dict(sun='id', rain='wet')),
                    ('E_patch', dict(sun='id', exc='only@' + show(SETTINGS[FSTAR])))):
        v = fam.find(**lab)
        added = [n for n in fam.names[1:] if lab.get(n, 'off') != 'off']
        full = fam.profile(v)
        rest = fam.profile(v, deleted=tuple(added))              # E1|Gamma0 = E0
        acc_full_f = full[FSTAR] == TRUTH[FSTAR]
        acc_rest_f = rest[FSTAR] == TRUTH[FSTAR]
        acc_rest_F = all(rest[j] == TRUTH[j] for j in J_BEFORE)
        acc_full_F = all(full[j] == TRUTH[j] for j in J_BEFORE)
        print('  %-8s Gamma1 support for f*? %-5s Gamma0 support for f*? %-5s -> block critical for f*: %-5s |'
              ' for J_before: Gamma1 %s, Gamma0 %s -> critical: %s'
              % (nm, acc_full_f, acc_rest_f, acc_full_f and not acc_rest_f, acc_full_F, acc_rest_F,
                 acc_full_F and not acc_rest_F))

    print('\n' + '-' * 100)
    print('M2  SEASONS: the myth amended and the tilt\'s own correction')
    print('-' * 100)
    myth = m2.Myth('amended', ['none', 'S', 'E'])
    MV2 = myth.versions()
    v0s = [v for v in MV2 if myth.dmenu[v[2]] == 'none']
    m0 = myth.find('none')
    truth_ok = lambda fam, v, xs: all(fam.ans(v, x) == m2.TRUTH[x] for x in xs)
    R = [x for x in m2.PAIRS if myth.ans(m0, x) == m2.TRUTH[x]]
    W = [x for x in m2.PAIRS if myth.ans(m0, x) != m2.TRUTH[x]]
    fails = n = 0
    for r in range(len(R) + 1):
        for Fs in combinations(R, r):
            for k in range(1, len(W) + 1):
                for Ws in combinations(W, k):
                    P = [v for v in MV2 if truth_ok(myth, v, Fs)]
                    Pp = [v for v in MV2 if truth_ok(myth, v, Fs + Ws)]
                    n += 1
                    if not (m0 in P and m0 not in Pp and len(Pp) < len(P)):
                        fails += 1
    print('  myth, law family (d in none,S,E): instances %d, failures of (H*) %d' % (n, fails))
    P = [v for v in MV2 if truth_ok(myth, v, m2.J_GREEK)]
    Pp = [v for v in MV2 if truth_ok(myth, v, m2.J_SAILOR)]
    hyb = [v for v in Pp if any(myth.ans(v, x) == myth.ans(m0, x) for x in W if x not in m2.J_SAILOR)]
    print('  J_greek -> J_sailor: |Pres| %d -> %d, witness M0 excluded? %s; hybrids keeping M0\'s error at the equator: %d of %d'
          % (len(P), len(Pp), m0 in P and m0 not in Pp, len(hyb), len(Pp)))
    tilt = m2.Tilt('law', m2.G_LAW, m2.H_LAW, False)
    esc = tilt.find('t+1', 'flat/escape', 'direct')
    TV = tilt.versions()
    Rt = [x for x in m2.PAIRS if tilt.ans(esc, x) == m2.TRUTH[x]]
    Wt = [x for x in m2.PAIRS if tilt.ans(esc, x) != m2.TRUTH[x]]
    fails = n = 0
    for r in range(len(Rt) + 1):
        for Fs in combinations(Rt, r):
            for k in range(1, len(Wt) + 1):
                for Ws in combinations(Wt, k):
                    P = [v for v in TV if truth_ok(tilt, v, Fs)]
                    Pp = [v for v in TV if truth_ok(tilt, v, Fs + Ws)]
                    n += 1
                    if not (esc in P and esc not in Pp and len(Pp) < len(P)):
                        fails += 1
    P = [v for v in TV if truth_ok(tilt, v, m2.J_GREEK)]
    Pp = [v for v in TV if truth_ok(tilt, v, m2.J_SAILOR)]
    print('  tilt, law family, escape version as v0: instances %d, failures %d; J_greek -> J_sailor |Pres| %d -> %d'
          % (n, fails, len(P), len(Pp)))
    print('  myth against tilt: no member of either family gives the other organization -> (H*) has no instance')


if __name__ == '__main__':
    main()
```

##### `m3_lemma_check.py` output

```text
====================================================================================================
M3  THE PROPOSED LEMMA (H*) AND ITS LIMITS, CHECKED ON THE MODELS
====================================================================================================
E0 right at 12 pairs, wrong at 4: dry/calm/early/sunS, dry/windy/early/sunS, wet/calm/early/sunS, wet/windy/early/sunS

----------------------------------------------------------------------------------------------------
(1) (H*): every F that E0 does, every f* that E0 fails (single failed pairs, and random whole contracts
    holding a failed pair). Strict containment with the embedded E0 as witness?
----------------------------------------------------------------------------------------------------
  U1 = sun x var[V] x rain[W] x exc[single]    |V|=  1088  instances checked= 16784  failures of (H*)=0  min strict gap=12
  U2 = sun x var[V] x rain[W,Wi] x exc[single] |V|=  4352  instances checked= 16784  failures of (H*)=0  min strict gap=12
  E_good rich = sun x var[V,W,Wi]              |V|=  1024  instances checked= 16784  failures of (H*)=0  min strict gap=8
  redescribed: sun x rainA[W] x rainB[W]       |V|=    64  instances checked= 16784  failures of (H*)=0  min strict gap=1
  redescribed x10: sun x rain1..rain5[W]       |V|=  4096  instances checked= 16784  failures of (H*)=0  min strict gap=1
  grid sun x var[V] x rain[W]                  |V|=    64  instances checked= 16784  failures of (H*)=0  min strict gap=1
  grid sun x var[V] x rain[W+Wi]               |V|=   256  instances checked= 16784  failures of (H*)=0  min strict gap=1
  grid sun x var[V] x rain[W+Sun]              |V|=   256  instances checked= 16784  failures of (H*)=0  min strict gap=5
  grid sun x var[V] x rain[W+Wi+Sun]           |V|=  4096  instances checked= 16784  failures of (H*)=0  min strict gap=17
  grid sun x var[V+Wi] x rain[W]               |V|=   256  instances checked= 16784  failures of (H*)=0  min strict gap=2
  grid sun x var[V+Wi] x rain[W+Wi]            |V|=  1024  instances checked= 16784  failures of (H*)=0  min strict gap=2
  grid sun x var[V+Wi] x rain[W+Sun]           |V|=  1024  instances checked= 16784  failures of (H*)=0  min strict gap=10
  grid sun x var[V+Wi] x rain[W+Wi+Sun]        |V|= 16384  instances checked=  1400  failures of (H*)=0  min strict gap=34
  grid sun x var[V+Sun] x rain[W]              |V|=   256  instances checked= 16784  failures of (H*)=0  min strict gap=5
  grid sun x var[V+Sun] x rain[W+Wi]           |V|=  1024  instances checked= 16784  failures of (H*)=0  min strict gap=5
  grid sun x var[V+Sun] x rain[W+Sun]          |V|=  1024  instances checked= 16784  failures of (H*)=0  min strict gap=23
  grid sun x var[V+Sun] x rain[W+Wi+Sun]       |V|= 16384  instances checked=  1400  failures of (H*)=0  min strict gap=84
  grid sun x var[V+W+Wi] x rain[W]             |V|=  4096  instances checked= 16784  failures of (H*)=0  min strict gap=8
  grid sun x var[V+W+Wi] x rain[W+Wi]          |V|= 16384  instances checked=  1400  failures of (H*)=0  min strict gap=8
  grid sun x var[V+W+Wi] x rain[W+Sun]         |V|= 16384  instances checked=  1400  failures of (H*)=0  min strict gap=40
  TOTAL failures of (H*) across all families: 0

----------------------------------------------------------------------------------------------------
(1b) Counts on the gardener's own jobs (F = J_before, f* = the failed summer): strict in every family,
     while the SIZE of the gap depends on the menus
----------------------------------------------------------------------------------------------------
  U1 = sun x var[V] x rain[W] x exc[single]    |Pres(J_before)|=   68  |Pres(J_after)|=   52
  U2 = sun x var[V] x rain[W,Wi] x exc[single] |Pres(J_before)|=  272  |Pres(J_after)|=  208
  E_good rich = sun x var[V,W,Wi]              |Pres(J_before)|=  128  |Pres(J_after)|=   64
  redescribed: sun x rainA[W] x rainB[W]       |Pres(J_before)|=    4  |Pres(J_after)|=    3
  redescribed x10: sun x rain1..rain5[W]       |Pres(J_before)|=   32  |Pres(J_after)|=   31

----------------------------------------------------------------------------------------------------
(iv) NEGATIVE CONTROLS: drop a hypothesis and strictness is no longer guaranteed
----------------------------------------------------------------------------------------------------
  no v0 (var menu without "off"): Pres(J_before)=['(sun=id, var=early)']  Pres(J_after)=['(sun=id, var=early)']  strict? False
  E0 does not do F (sun x var[V]; F = J_before + dry/calm/early/sunS; f* = dry/windy/early/sunS): E0 in Pres(F)? False  |Pres(F)|=1  |Pres(F+f*)|=1  strict? False
  a new job no member fails (sun x var[V]; wet springs with the late variety added to J_after): |Pres| 1 -> 1, strict? False  (file 00's non-strict case)
  added job that E0 does (wet springs, late variety) on F = J_after: |Pres|=52 -> 15, strict? True

----------------------------------------------------------------------------------------------------
(i) HYBRIDS: members of Pres(F + f*) that fail another job E0 fails
----------------------------------------------------------------------------------------------------
  U1 = sun x var[V] x rain[W] x exc[single]    f* = the failed summer:   52 in Pres,   18 hybrids e.g. (sun=id, var=off, rain=off, exc=only@wet/windy/early/sunS)
                                               f* = the open question (all 16 pairs):   13 in Pres,    0 hybrids
  U2 = sun x var[V] x rain[W,Wi] x exc[single] f* = the failed summer:  208 in Pres,   71 hybrids e.g. (sun=id, var=off, rain=off, exc=only@wet/windy/early/sunS)
                                               f* = the open question (all 16 pairs):   13 in Pres,    0 hybrids
  E_good rich = sun x var[V,W,Wi]              f* = the failed summer:   64 in Pres,   56 hybrids e.g. (sun=id, var=early&wet&windy)
                                               f* = the open question (all 16 pairs):    1 in Pres,    0 hybrids

----------------------------------------------------------------------------------------------------
(ii) EXTENSION: on the same jobs, the embedded family of E0 never has the larger Pres
----------------------------------------------------------------------------------------------------
  U1 = sun x var[V] x rain[W] x exc[single]    all 65536 job sets F: Pres_V0(F) inside Pres_V(F) always? True   strictly larger for 65536, equal for 0
  U2 = sun x var[V] x rain[W,Wi] x exc[single] all 65536 job sets F: Pres_V0(F) inside Pres_V(F) always? True   strictly larger for 65536, equal for 0
  E_good rich = sun x var[V,W,Wi]              all 65536 job sets F: Pres_V0(F) inside Pres_V(F) always? True   strictly larger for 65536, equal for 0

----------------------------------------------------------------------------------------------------
(iii) GOOD AGAINST BAD in one family (U1): same witness, both kept; only a job one fails separates them
----------------------------------------------------------------------------------------------------
  Pres(J_after               ) |  52|  E_good in? True   E_bad in? True   E_patch in? True
  Pres(J_after + seed trial  ) |  35|  E_good in? True   E_bad in? False  E_patch in? False
  Pres(C_full                ) |  13|  E_good in? True   E_bad in? False  E_patch in? False

----------------------------------------------------------------------------------------------------
NARROWING instance (identity edit as witness)
----------------------------------------------------------------------------------------------------
  E0 narrowed to the summers seen: |Pres(C_narrow)|=1  |Pres(C_narrow + f*)|=0  witness E0? True
  same set as the claim BEFORE the failure (Pres(J_before))? True  -> the inclusion does not say whether the
     omitted job was dropped after a failure or never claimed; only the historical index says which
  Situation 3 (E_bad confined to the recorded summers, open question dropped), U1: |Pres(J_after)|=52 |Pres(J_after + open question)|=13  witness E_bad? True
     the same inclusion has E_good's honest confinement to J_after inside it: E_good in both? True

----------------------------------------------------------------------------------------------------
COMPANION: the added block is critical for f* (B), and not critical for the old jobs
----------------------------------------------------------------------------------------------------
  E_good   Gamma1 support for f*? True  Gamma0 support for f*? False -> block critical for f*: True  | for J_before: Gamma1 True, Gamma0 True -> critical: False
  E_bad    Gamma1 support for f*? True  Gamma0 support for f*? False -> block critical for f*: True  | for J_before: Gamma1 True, Gamma0 True -> critical: False
  E_patch  Gamma1 support for f*? True  Gamma0 support for f*? False -> block critical for f*: True  | for J_before: Gamma1 True, Gamma0 True -> critical: False

----------------------------------------------------------------------------------------------------
M2  SEASONS: the myth amended and the tilt's own correction
----------------------------------------------------------------------------------------------------
  myth, law family (d in none,S,E): instances 60, failures of (H*) 0
  J_greek -> J_sailor: |Pres| 6 -> 2, witness M0 excluded? True; hybrids keeping M0's error at the equator: 2 of 2
  tilt, law family, escape version as v0: instances 60, failures 0; J_greek -> J_sailor |Pres| 4 -> 2
  myth against tilt: no member of either family gives the other organization -> (H*) has no instance
```

---

## Appendix C — The proposal (working file 03, copied unchanged except as noted)

### 03 Proposal: a correction lemma inside a common family, and why it does not make the record redundant

*Working file, 24 September 2026. Nothing in the repository was changed. Built on `01 text.md` and `02 models.md`. Re-read for this: draft 3 Parts V–VI and D3:L25, L151, L159, L255, L363, L516, L528, L562, L566, L602; file 00 L276–300 and L352–386, L1296–1304; the error-correction analysis (EC) section 2 and option (b); cases O1, O36, O45–O48 (S81 book), N1, N2, N7 (N-case book), D3-T `final.md`; Deutsch ch. 1 at pp.22, 25, 29. The Pinker folder was not opened. New script: `ratchet/models/m3_lemma_check.py`, output `m3_output.txt` (Python 3.11, standard library, about 35 seconds).*

**Tags.** [T] a line says it. [F] follows from quoted lines. [PROVED] a short general argument. [COMPUTED] exact output of a script on a stated finite model. [I] my inference.

---

#### 1. Answers to the owner's three points

##### (1) "A correction adds the failed case to the jobs, so any version that brings the mistake back fails." PARTLY.

- **Yes, at the failed case.** [F] (A) is universal over the contract (D3:L247–251), so any job whose contract holds the failed summer is one on which the old explanation is not an account. [PROVED, COMPUTED] Inside the later explanation's family, with the old one present as a member, adding that job shrinks Pres **strictly**, and the old explanation is the member that is excluded. Checked on 20 gardener families (every job set the old explanation does, every failed pair, plus random whole contracts): about 274,000 instances, no failure. Also the myth (60 instances) and the tilt (60 instances), no failure (M3 (1)).
- **No, beyond the failed case, when the jobs are the record.** [COMPUTED] Versions that do every recorded job and the failed one but repeat the old mistake at *another* early-variety summer survive: 18 of 52 (family U1), 71 of 208 (U2), 56 of 64 (a variety part that reads variety, rain and wind). Both amended myths that survive keep the original's error at the equator (2 of 2). The count reaches 0 only when the job added is the whole open question (13 survivors, 0 of them repeating the mistake) (M3 (i)).
- **And on the open question the failure added nothing.** [T] Reach "is fixed by \(E\) and the world, not by which jobs anyone has checked" (D3:L313). The old explanation was never an account on the open question. The failure showed that fact; it did not create a job. So the owner is right that a mistake cannot come back into an *account* of an unchanged question. But that holds as a fact nobody can see before a separating test (EC Situation 2: "blocked as a fact, unmarked in the record").
- **It is not a ratchet.** [T] A narrowing adopted after a failure is a legitimate new claim (D3:L159, L363, L602). [PROVED] By the same lemma, with the narrowed claim itself as the excluded member, dropping the failed job gives back the larger Pres (section 2, narrowing clause).

##### (2) "A bad rescue registers as easier to vary, by the measure that defines a good explanation." NO.

- [T] No measure defines a good explanation. Draft 3 supplies no merit function (D3:L25), and Pres "grades nothing" (D3:L313).
- [COMPUTED] In one family holding all three rescues, the good rescue, the wet-spring rescue and the do-nothing patch are all members of Pres of the record plus the failed summer (52). Only the seed trial (35 left, good only) or the open question (13 left, good only) separates them, and that is (A), not variation (M3 (iii)).
- [PROVED, COMPUTED] On the same jobs, a family that extends the old explanation never has the smaller Pres. It was strictly larger for all 65,536 job sets in three families (M3 (ii)). That holds for the good rescue too.
- [COMPUTED] The record is symmetric under swapping rain and variety, so families that treat the two rescues alike give equal Pres: 1:1, 4:4, 6:6, 64:64. Otherwise the order flips with the menus: 1:96 against 64:1 (02, CX2–CX3). The do-nothing patch has Pres 1, the same as the good rescue.
- **The narrowing is the one place where "more versions fit" is a theorem.** [COMPUTED] E0 narrowed to the summers seen: Pres 1 against 0 with the failed summer. Situation 3 (the wet-spring rescue confined to the record): 52 against 13 with the open question. But Pres of the narrowed claim equals, exactly, Pres of the claim made before the failure. The good rescue confined to the same record sits in the same inclusion (M3, narrowing). The inclusion cannot tell a job dropped after a failure from one never claimed. Only the historical index (D3:L363) can, and the historical index is a record.
- [F] "Do-nothing" in the theory's sense cannot rescue at all. A commitment that does no work "meets (E) exactly when it meets (E) without \(d\)" (D3:L313). The companion clause below makes this exact: [COMPUTED] a rescuing addition is critical at the failed job, and all three rescues (good, wet spring, one-summer exception) are (M3, companion). The wet-spring clause is therefore not idle. Its fault is unfaithfulness on the open question.

##### (3) "Can the file-00 limit be relaxed for an explanation and its own correction?" PARTLY: it cannot be relaxed, but it can be met.

- [T] File 00's reasons are structural (F00:L379, L381, L1300): there is no common set, counts change under redescription, and interpretation is held fixed. [F] None mentions authorship, so they apply to one's own correction as fully as to anyone's (01 (c)). [COMPUTED] Taken each with its own family, before and after are disjoint, and every count depends on the menus (02 §4).
- [PROVED] **Met, not relaxed.** Take the later explanation's declared family and require that one member restore the earlier organization. Then there is one organization, one interpretation and one family, which is file 00's premise (F00:L358), and (H) applies. What is new is that the earlier organization is a guaranteed witness, so the containment is strict. That answers file 00's "need not be strict" for exactly this case.
- [F] "Own" does no formal work. The hypothesis is structural: the family contains the earlier organization. A rival's extension of the same explanation meets it equally and gets the same result. What makes a correction someone's *own* is history (F11:L15). So a comparison restricted to one's own corrections would assume the record the owner wants to do without.

---

#### 2. The proposal: wording, hypotheses, check

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

#### 3. What it does in the test situations and cases

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

#### 4. Gains, losses, and what kind of text it should be

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

#### 5. What stays uncertain

1. **What a job is.** "Explanatory job" is undefined in the texts (01 (a)). The proposal makes it a question. The models read jobs as single pairs, with Account as (A) alone. (H\(^*\)) holds on either reading. The hybrid counts and the Pres sizes depend on it, and (F1) could shrink the sets (the amended myth may have an empty Pres under full (E)) without touching strictness.
2. **Whether the witness member always exists.** A transport is part of a candidate, not of an organization (D3 Part V). A correction that re-anchors a kept component may not be undone by an *organization* edit. File 11 never defines \(E_v\) beyond "organization edits" (F11:L301). If so, the family must be one of candidate edits.
3. **Background in the companion clause.** Whether \(E_1|(\Gamma_1\setminus B)=E_0\) holds when removing \(B\) alters the named background.
4. **Whether the owner wanted a mark, not a truth.** The lemma cannot give point (2). A mark of retreat needs a record (EC option (b)), which is a separate decision this proposal neither needs nor replaces.
5. **The evidence behind the limits.** The limits are shown by finite toy models: counterexamples, not frequencies. Draft 3 is not frozen, and its line numbers may move.

---

## Appendix D — The text attack (working file 04a, copied unchanged except as noted)

### 04a Text attack on `03 proposal.md`

*Working file, 24 September 2026. Read-only on the repository. Read for this:*
- *03 in full.*
- *Draft 3 (D3) in full.*
- *File 11 (F11) at L13–29, L161, L299–303, L313–315 and L365.*
- *File 00 (F00) at L260–386 and L1285–1310.*
- *The change list (CL): W33.1 and W34.1 (L1087–1141).*
- *The error-correction analysis (EC) in full to L285, plus its Appendix A rows at L525–531 and L560–561.*
- *Cases: S81 O1, O36, O45–O48; N-case book N1, N2, N7; D3-T `final.md` and `why.md`; the S81 results rows for O1.*
- *`models/m3_output.txt`, the head of `m3_lemma_check.py`, and 02 §4.*
- *Deutsch ch. 1 at pp.25, 28 and 31 in the extracted text.*

*The Pinker folder was not opened. Line numbers are those of the files as read today. Draft 3 is not frozen.*

**Tags.** [T] a line says it. [F] follows from quoted lines. [I] inference. 03:Lnn is a line of the proposal.

---

#### 0. Verdicts, one line each

##### Section 1 of 03 (the owner's three points)

| # | 03 claim | Verdict | Line(s) |
|---|---|---|---|
| 1a | At the failed job, (A) makes the old explanation fail any job holding the failed summer, and with the old organization in the family the shrink is strict (03:L13) | UPHELD. One wording fix: "the member excluded" should be "a member excluded". | D3:L247–251 |
| 1b | Beyond the failed case, versions that repeat the old error at an unrecorded pair survive (03:L14) | UPHELD, as computed on (A)-only models. In the text it is Derivation 3's shape, so it needs Derivation 3's qualification (see 7). | D3:L195, L566–570 |
| 1c | Reach "is fixed by E and the world, not by which jobs anyone has checked"; the failure showed a fact and created no job (03:L15) | UPHELD. The quote is exact. | D3:L313 (W34.1) |
| 1d | "A narrowing adopted after a failure is a legitimate new claim" [T] (03:L16) | CORRECTED | D3:L159, L602 |
| 2a | "[T] No measure defines a good explanation" (03:L20) | CORRECTED (the tag). The quotes from L25 and L313 are exact. | D3:L25, L69, L313 |
| 2b | The three rescues are all in Pres on the record plus the failed summer. Only the seed trial or the open question separates them, "and that is (A), not variation" (03:L21) | CORRECTED | D3:L255, L273, L556 |
| 2c | On the same jobs, an extension never has the smaller Pres (03:L22) | UPHELD as a fact about the models. It is a cross-family comparison and must stay out of the theory text (see 12). | F00:L379, L1300 |
| 2d | Where the record is symmetric, Pres is equal; otherwise the counts flip with the menus (03:L23) | UPHELD | F00:L381, L1302 |
| 2e | The narrowed claim's Pres "equals, exactly, Pres of the claim made before the failure", and "the historical index is a record" (03:L24) | CORRECTED | D3:L313, L363, L55, L161, L602 |
| 2f | Idle in the theory's sense cannot rescue; the wet-spring clause is not idle; its fault is unfaithfulness (03:L25) | UPHELD. The L313 quote is exact. | D3:L313; EC L131 |
| 3a | File 00's reasons are structural and none mentions authorship (03:L29) | UPHELD. The quotes check. | F00:L379, L381, L1300 |
| 3b | "Met, not relaxed" (03:L30) | CORRECTED. (H\*) meets file 00's premise, but it is not the owner's comparison, and limit (ii) makes the relaxation that 03 says cannot be made. | F00:L358, L379, L1300 |
| 3c | "Own" does no formal work; own-ness is history (03:L31) | UPHELD in substance. CORRECTED citation. | D3:L13 (=F11:L15), L421 |

##### Section 2 of 03 (the wording)

| # | 03 claim | Verdict | Line(s) |
|---|---|---|---|
| 4 | (a) "(a job is a question, Part III)" (03:L44) | CORRECTED. It is a new definition. | D3:L138–147, L313 |
| 5 | (a) "strict exactly when some member of Pres(F) is not an account on some job of F′" (03:L46) | UPHELD. The iff is correct. | D3:L313 |
| 6 | (b) (H\*) and its proof (03:L50–54) | UPHELD as mathematics. CORRECTED in how v₀ is specified. | D3:L189, L231 |
| 6′ | (b) "Where E₁ only adds a block B, E₀=E₁\|(Γ₁∖B)" (03:L50) | CORRECTED. This is a hypothesis, not a fact. | D3:L103, L287 |
| 6″ | (b) The companion clause (03:L54) | UPHELD. It is (S) and (B), and it is already recorded by (D). | D3:L290–302 |
| 7 | (b) Limit (i), "may … whenever" (03:L59) | CORRECTED. It needs Derivation 3's qualification. | D3:L195, L568–570; O48; D3-T |
| 8 | (b) Limit (ii), "the later organization is never the harder to vary" (03:L60) | REFUTED as worded | F00:L379, L1300; D3:L313; EC L235; O47 |
| 9 | (b) Limit (iii), "that is (A) on that job" (03:L61) | CORRECTED: it should read (E) | D3:L556–560, L562 |
| 10 | (b) Limit (iv) (03:L62) | UPHELD | — |
| 11 | (b) The narrowing clause (03:L56) | CORRECTED. It needs the identity edit in 𝒱. | D3:L91, L299 |
| 12 | (b) "It orders no candidates. It uses no fact about who wrote E₁ or when" (03:L64) | UPHELD for (H\*). REFUTED for the paragraph while (ii) stands. The words "earlier", "later" and "written" should be made structural. | F00:L379 |
| 13 | (c) Pointer at L363 (03:L66) | CORRECTED | D3:L55, L161, L363, L602 |
| 14 | "Hypotheses, and why each is needed" (03:L68–72) | UPHELD. The m3 output matches every number. | m3 (iv), (1b) |
| 15 | Why it does not rank, items 1, 2 and 4 (03:L75–78) | UPHELD | — |
| 15′ | Why it does not rank, item 3: "no witness member, so it says nothing" (03:L77) | CORRECTED | D3:L103, L299 |

##### Section 3 of 03 (the cases)

| # | Case | Verdict |
|---|---|---|
| 16 | Saint | UPHELD, with two precisions (see 5.1) |
| 17 | North bed, open | UPHELD |
| 18 | Narrowed question | UPHELD. "Still passes (E)" is CORRECTED to EC's qualified pass. |
| 19 | N2 | CORRECTED. Under (E) there is no instance. |
| 20 | O1 | CORRECTED. There is an instance only if the restated rules are accounts. Nothing moves. |
| 21 | N7 | UPHELD for Maya. CORRECTED on Bea's "fuller". |
| 22 | N1 | CORRECTED. "The god is idle" is one reading. |
| 23 | O36 | CORRECTED. "The witness is always a written earlier organization" is false for the (a) iff. O36 is still unaffected. |
| 24 | O45 | UPHELD |
| 25 | O47 | UPHELD. The case shows why (ii) must go. |
| 26 | O48 | CORRECTED (minor). It rests on the population, not on 𝒱, and bears on limit (i). |
| 27 | D3-T | UPHELD, once limit (i) carries Derivation 3's qualification |

##### Sections 4 and 5 of 03

| # | 03 claim | Verdict | Line(s) |
|---|---|---|---|
| 28 | Gain: "Part VI gets its link to correction" (03:L107) | CORRECTED. (D) already records the link; the lemma only states it. | D3:L302; F00:L294 |
| 29 | "It cannot flip any case, since it changes no definition" (03:L121) | CORRECTED. This is true only without (a)'s parenthesis. | — |
| 30 | "A Part VI measure … needs a measure on 𝒱, which is a merit function" (03:L122) | CORRECTED. An order of candidates by such a measure is one; counting itself is not. | D3:L25, L516; F00:L1302 |
| 31 | "'Adding the failed job must shrink Pres' is always met, by the lemma" (03:L125) | CORRECTED. It holds only when 𝒱 contains v₀. | D3:L516 |
| 32 | Other §4 bullets (03:L124, L126–127) | UPHELD | — |
| 33 | §5 uncertainties (03:L133–137) | UPHELD | — |
| 34 | Bottom line: a record of rescues is not redundant | UPHELD, and the text says so directly | D3:L43, L55, L159, L602 |

**Answers to the brief's questions.**
- **Conflict with draft 3?** Limit (ii) conflicts with file 00's scope (F00:L379, L1300) and with "how hard an *account* is to vary" (D3:L313). Limit (iii) is misaligned with Derivation 2. Limit (i) misses Derivation 3's qualification. The narrowing clause omits a hypothesis. (a) adds a definition. Nothing conflicts with the (E) conditions, with "grades nothing" (except through (ii)), with "counting jobs is not a warrant", with W33.1 or with W34.
- **Ranking or merit function?** Not in (H\*). Limit (ii) brings back EC option (c)'s inclusion order between two candidates, in one direction. It must be rewritten.
- **History?** Nothing puts history into (E). The narrowing clause sends "dropped or never claimed" to the record, which the text licenses. Only wording is at fault.

---

#### 1. Section 1 claims

##### 1a. The failed job: UPHELD

[T] (A) holds "For every (a,b)∈C" (D3:L247). So a job whose contract holds a pair where E₀ answers otherwise is one on which E₀ is no account. [F] If E₀'s candidate is a member of Pres(F), it is not a member of Pres(F∪{f\*}). The m3 output shows 0 failures in about 274,000 instances (16,784 × 16 + 1,400 × 4).

"The old explanation is *the* member that is excluded" (03:L13) is loose. The output shows gaps of 8 to 84 members, and v₀ is one of them. Write "a member".

##### 1b. Beyond the failed case: UPHELD, with a qualifier

The figures are exact against m3 (i): 18 of 52, 71 of 208 and 56 of 64; on the open question, 13, 13 and 1 left, with 0 hybrids. One correction: "13 survivors" (03:L14) is U1 and U2 only; E_good rich leaves 1.

In the text this is Derivation 3's shape. What a set of jobs leaves open is what the family leaves open: "what H leaves open about t is what 𝒯 leaves open" (D3:L195). "Where 𝒯 contains no such transport … the population fixes it" (D3:L568). So "survive" is a fact about the menus chosen, not about correction. See 7.

##### 1c. Reach: UPHELD

The quote is exact: "it is fixed by E and the world, not by which jobs anyone has checked" (D3:L313). The inference is sound: a failure adds no job to reach.

##### 1d. "A legitimate new claim": CORRECTED

The text never says "legitimate".
- D3:L159: "a narrowing adopted after a failure is a new claim at a new index (Part VIII)". The same line goes on: "the semantics records the restriction and supplies no rule that certifies it".
- D3:L602 forbids only the unrecorded change: "Goalpost-moving is the act of changing the index without recording the change".

**Replace with:** "A narrowing adopted after a failure is a new claim at a new index, recorded, not forbidden, and not certified as appropriate (D3:L159, L602)."

The conclusion "not a ratchet" stands.

##### 2a. "No measure defines a good explanation": CORRECTED (tag)

This is [F], not [T]. Draft 3 never uses "good explanation". What it says:
- "how hard an account is to vary is a separate matter (Part VI)" (D3:L69);
- "it grades nothing" (D3:L313);
- "no merit function" (D3:L25, L516).

The owner's "by definition" is Deutsch's glossary: "Good/bad explanation An explanation that is hard/easy to vary while still accounting for what it purports to account for" (D p.31). Draft 3 does not adopt it. On point numbering: the merit-function sentence is D3:L25 (F11:L27). D3:L27 is the "does not prove membership" line.

##### 2b. "Only the seed trial or the open question separates them, and that is (A)": CORRECTED

This is true in the models, where "Account(E_v, job) is read as (A) on every pair of it" (m3 header). Under draft 3's (E), two things change.

1. **The one-summer patch may not be an account even on the failed job.** Non-circular dependence requires that "the target's answer does not appear, at the declared grain, … as a component" (D3:L255). L273 adds: "So does an account whose only substantive component restates the answer it was asked for". A component that yields "north first" only at the failed summer's settings writes that answer in. [I] It fails at f\*, on the same grain reading that EC leaves unsettled for N2 and Situation 3 (EC L143, L560). If so, the patch is separated from the good rescue already on the record plus the failed summer, by (E), before any seed trial.
2. **The separating job works through (E), not only through (A).** Derivation 2(i) gives candidates that meet (F1), (F2) and (A) the same answer profile (D3:L556). Two rescues can then differ only in their anchors, and what separates them is (F1) on a finer contract (D3:L562). EC's "one way it passes", with "wet" anchored to the variety (EC L124), is exactly such a case.

**Replace "that is (A), not variation" with "that is (E) on that job, not variation".** Add that under full (E) the patch may already fail non-circular dependence at the failed job.

##### 2c. Extensions never have the smaller Pres: UPHELD as a model fact

The m3 figures are right: 65,536 job sets in each of 3 families, strictly larger in every one. The claim concedes the owner's literal point (2) for every rescue alike: on the old jobs, good and bad rescues both "register as easier to vary". That supports 03's "NO" as a *distinguishing* mark. But the comparison sets E₀'s own family inside E₁'s. That is the cross-family comparison file 00 withholds (see 8), so it belongs in the analysis, not in the theory text.

##### 2d. Symmetric record: UPHELD

This is consistent with F00:L381 ("splitting one feature into ten cannot create knowledge") and F00:L1302.

##### 2e. "Equals, exactly, Pres of the claim made before the failure"; "the historical index is a record": CORRECTED

**The equality.** m3 computes "same set as the claim BEFORE the failure (Pres(J_before))". So "the claim before the failure" is taken to be the jobs *checked* before it. On W34's reading, the gardener's earlier claim was on the open question: reach is "not by which jobs anyone has checked" (D3:L313). On that reading, Pres of the narrowed claim is ⊇ Pres of the earlier claim, and strictly so when a member fails the open question (in U1, 1 against 0).

**Replace with:** "equals Pres of the record as it stood before the failure; against the earlier claim on the open question, it is at least as large."

**"The historical index is a record."** L363 is a principle, not a record: "A proposition indexed to a contract remains that proposition when a later theory changes the current contract. A new index is a new claim." A narrowed claim and a claim never made wider have the same kind of index, the narrow contract. What tells them apart is the existence of the earlier claim at its own index. L363 keeps that claim as a proposition, and the record shows that it was made:
- "every change carries a provenance record" (D3:L55);
- "without recording that the claim has changed" (D3:L161);
- "a failure of the record" (D3:L602).

**Replace with:** "Only the record of indexed claims can (Part VIII, historical index; D3:L55, L161, L602)."

##### 2f. Idle parts cannot rescue: UPHELD

The quote is exact: "a candidate carrying d then meets (E) exactly when it meets (E) without d" (D3:L313). EC's caveat (EC L39, L158) is that every part is vacuously idle in a candidate with no support. It does not reach a rescue, because a rescued E₁ is an account on f\*, so Γ₁ is a support. The same caveat bites in N2 (see 19).

##### 3a. File 00's reasons: UPHELD

- F00:L379: "It says nothing by itself about two different theories using different interpretations or different variation families."
- F00:L1300: "The valid containment result holds when the organization, interpretation, and variation family stay fixed … It may be non-strict."
- F00:L381.

None mentions authorship.

##### 3b. "Met, not relaxed": CORRECTED

(H\*) takes one organization E₁, one interpretation and one family 𝒱, which is file 00's premise (F00:L358). What it compares is **two job sets inside E₁'s family**, of which E₀ is one member. It does not compare E₀ with E₁. The owner's question was whether hard-to-vary can compare an explanation with its correction. The answer is **no**: the limit is not relaxed, and that comparison is not made.

Limit (ii) as drafted does make it (see 8), so 03 contradicts its own answer.

**Replace with:** "NO. The limit cannot be relaxed, and (H\*) does not compare the explanation with its correction. It compares two sets of jobs inside the correction's family, of which the original is a member."

##### 3c. "Own": CORRECTED citation

F11:L15 (= D3:L13) concerns the provenance of correspondences. Ownership of a process is D3:L421: "owned by s when its processes run inside the system boundary". That rests on a declared boundary (D3:L467, L516). The substance stands. Note also that the owner's "its own correction" means "the correction *of* this explanation", and 03's structural reading (the family contains E₀) is the right one for that.

---

#### 2. The wording against draft 3

##### 4. "(a job is a question, Part III)": CORRECTED

- **It is well typed.** Account takes a question (D3:L231, L302), and a question is a whole 6-tuple, "p=(D, C, b₀, 𝒬, O_p, ρ_p)" (D3:L138). So "job is a question" also makes the obligations and the contract's **provenance** ρ_p part of a job's identity. (E) never reads either, and 03 does not say so.
- **It is not needed.** 03 says (H\*) "holds on either reading" (03:L133).
- **It breaks a claim in 03.** It is a definition, which falsifies 03:L121 ("it changes no definition").
- **It needs a declaration.** In the change list's terms it is a KIND: CLAIM, which needs cases at risk: N4 Q1 and N5, which rest on reach (CL W34.1).

**Fix:** drop the parenthesis. Or keep it with "(a job is a question, Part III; Account on it reads only D, C, b₀ and 𝒬)" and declare it.

##### 5. The (a) iff: UPHELD

Members of Pres(F) are accounts on F, so failing some job of F′ means failing F′∖F. It sits beside "counting jobs is not a warrant" without touching it.

##### 6. (H\*): UPHELD as mathematics, CORRECTED in how v₀ is specified

The proof is (H) plus two hypotheses. But the paragraph says "E_{1,v₀}=E₀ … each component it keeps with its earlier anchor". Anchors belong to the transport: "λ assigns each component of E a subnetwork of D" (D3:L189). And a candidate is (E,p,t,Γ) (D3:L231). Pres writes Account(E_v, f) and leaves t and Γ implicit. 03's uncertainty 2 notes this.

**Fix:** "a member v₀ whose candidate is E₀'s: organization E₀, its transport t₀ and its commitments Γ₀, with the named background fixed."

##### 6′. "Where E₁ only adds a block B, E₀=E₁|(Γ₁∖B)": CORRECTED

This is not automatic, for two reasons.
- Restriction deletes B's components. "A deleted component imposes the full relation on its ports" (D3:L103), and E|W is taken under "a declared restriction operation" (D3:L287). If B brought new ports, or if a component of E₁∖B reads B's ports, then E₁|(Γ₁∖B) is not E₀.
- An added dependence onto an output E₀ already fixed is usually a *changed* component: "it does not add an equation beside an incompatible one" (D3:L103).

**Fix:** delete the sentence and keep the equation only as the companion's hypothesis, which already reads "If also … and E₀=E₁|(Γ₁∖B)".

##### 6″. The companion clause: UPHELD, and already recorded by (D)

It follows from (S) and (B) as stated. Where the identity edit is in 𝒱, it is also the statement that (1, v₀) ∈ Boundary_{E₁,f\*} (D3:L302). File 00 says of the boundary that it "records where an account survives or fails" (F00:L294). So the "link to correction" (03:L107) exists already; the lemma makes it explicit (see 28). It fits W33.1: a singleton {d} that is critical fails the removal half of the idle test.

##### 7. Limit (i): CORRECTED

"A member of Pres(F∪{f\*}) **may** answer as E₀ does … **whenever** no job … holds that pair" reads as though such a member always exists. Derivation 3 was restated for exactly this reading:
- "The presence of an unseen pair alone does not establish that such a t′ exists" (D3:L566);
- "What the qualification gives up is the guarantee of a differing survivor at every unseen pair" (D3:L570).

O48 and D3-T are the guards.

**Replace with:** "(i) Pres(F∪{f\*}) excludes no member for its answer at a pair that no job of F∪{f\*} holds in its contract. Whether 𝒱 has a member that answers there as E₀ does is fixed by 𝒱, as what a history leaves open is fixed by a population (Derivation 3)."

##### 8. Limit (ii): REFUTED as worded

"So where the earlier organization's own family sits inside 𝒱, the later organization is never the harder to vary on the same jobs" (03:L60). Four problems:

1. **It compares two organizations with different families.** E₀'s family is edits of E₀. To "sit inside 𝒱" (edits of E₁), each edit of E₀ must be identified with an edit of E₁, via v₀. That identification is exactly the "common family" that F00:L379 and L1300 do not supply. The identity Pres_{𝒱₀}(F)=Pres_𝒱(F)∩𝒱₀ holds for a subfamily of *one* organization. The "So" moves from it to a claim about *two*.
2. **It is EC's option (c) order.** "For candidates that share V, order them by inclusion of Pres(F) … smaller means harder to vary" (EC L235). (ii) asserts that order between E₁ and E₀, in one direction. That is a comparison of two candidates by variability, which 03:L64 says the paragraph never makes and 1(3) says cannot be made.
3. **It ascribes variability to non-accounts.** L313 is scoped to accounts: "How hard an account is to vary". In O47, E₁ (with the locked room) is no account, yet (ii) says it is "never the harder to vary". 03's O47 row has to add a warning; the defect is in the sentence.
4. **The theory text does not need it.** Its job, blocking "a correction is harder to vary", is done by saying that (H\*) makes no such comparison.

**Replace with:** "(ii) (H\*) compares Pres(F) with Pres(F∪{f\*}) in one family. It does not compare E₁ with E₀. They are different organizations with different families (F00:L379), and it gives no ground for calling either harder to vary than the other."

##### 9. Limit (iii): CORRECTED

"Only a job on which one is an account and the other is not separates them, and that is (A) on that job" should read "**(E)** on that job". By Derivation 2(i), candidates that meet (F1), (F2) and (A) have one answer profile (D3:L556). Where they cut D differently, the separating change is a finer contract (D3:L562), where (F1) can separate candidates that (A) cannot. Derivation 9 says the same for outputs (D3:L610).

##### 10. Limit (iv): UPHELD

m3 (iv) matches: with no "off" setting, Pres is 1 → 1.

##### 11. The narrowing clause: CORRECTED

"With the identity edit as the witness" needs the identity in 𝒱. D3 gives an identity to the admitted edits A ("closed under a partial associative composition with identity 1", D3:L91). 𝒱 is only "a declared family of organization edits" (D3:L299), and nothing puts 1 in it. A counterexample: 𝒱 = {w}, with E_w an account on neither F nor f\*. Then Pres(F) = Pres(F∪{f\*}) = ∅.

**Fix:** "If 𝒱 contains the identity edit, E is an account on every job of F, and E is not an account on f\*, then …". Also replace "read from the historical index (Part VIII)" with "read from the record of indexed claims (Part III, Scope; Part VIII, Historical index; Derivation 7)", as in 2e.

##### 12. The closing sentence: UPHELD for (H\*), REFUTED for the paragraph while (ii) stands

(H\*) itself relates two subsets of one family, orders nothing, counts nothing and uses no history. Two wording points:
- The paragraph's words "later organization", "earlier candidate" and (in 03's O36 row) "written" import time and authorship into a lemma that claims to use neither. Call them E₁ and E₀ and state only the structural hypotheses.
- Once (ii) is replaced as in 8, "It orders no candidates" is true of the whole paragraph.

##### 13. Pointer (c): CORRECTED

- "A narrowing that omits a job … whether or not that job was ever claimed" contradicts itself: a job never claimed was not narrowed away.
- "the index, not Pres, records that it was": an index is "what a claim is relative to" (D3:L518), not a record.
- It needs the identity in 𝒱 (see 11).

**Replace with:** "A set of jobs that omits one its candidate fails has, when 𝒱 contains the identity edit, a strictly larger Pres than the same set with that job (Part VI), whether the job was dropped after a failure or never claimed. Which of the two it was is shown by the record of indexed claims, not by Pres."

##### 15′. "No witness member, so it says nothing" (tilt against myth): CORRECTED

𝒱 is any declared family (D3:L299), and "A changed rule is a changed component" (D3:L103). A family wide enough to change every component can hold both organizations, and then (H\*) applies. Nothing is lost, because its conclusion is still an inclusion of job sets, not an order of the tilt and the myth. **Replace with:** "unless someone declares a family holding both; even then its conclusion is about job sets, and it supplies no rule for building such a family (F00:L1300)."

##### The rest of the checklist

- **(E).** No conflict. Every hypothesis is an Account fact, and nothing is added to (E) (D3:L261–265).
- **Derivation 1.** No conflict.
- **Derivation 6.** 𝒱 is neither a declared index (D3:L518) nor a declared input (D3:L516), and Pres is absent from the dependence order (D3:L520). This gap predates the proposal and 03 reports it (03:L118). The lemma's hypothesis (iv) is about which members 𝒱 has, so it leans on that gap harder, but it yields no verdict, so it cannot be "choosing the input from the verdict wanted" (D3:L516).
- **Derivation 7.** Consistent, with the wording in 11 and 13.
- **Derivation 8.** Redescription is a refinement, not a recoding ("does not apply to coarsenings", D3:L606). 03 claims only that strictness survives it, which m3 (1) and (1b) confirm (4 → 3, 32 → 31).
- **Derivation 10.** No conflict.
- **Part XV.** (H\*) is a new mathematical claim. Like (H), it is not on the "mathematical error" list (D3:L540). No conflict. Listing it is optional.
- **"Grades nothing" and "counting jobs is not a warrant."** No conflict, except through (ii).
- **W33.1.** The companion clause agrees with the idle test (see 6″ and 2f).
- **W34.** 03 keeps reach apart from checked jobs (1c). Only 2e's equality slips back to the checked-jobs reading.

---

#### 3. Ranking and merit function

- **(H\*) and the companion clause.** Neither. They give an inclusion between two job sets of one family, and a block critical in one written support. Neither is a relation between candidates or a value.
- **Limit (ii).** Yes, in the weak form of EC option (c): an inclusion order of E₁ over E₀ by Pres, across families. It is not a merit function (it assigns no values) and not a ranking of thinkers (D3:L25, L516). But it is the comparison of different theories that F00:L379 and L1300 withhold, and it contradicts 03:L64. **Rewrite as in 8.**
- **§4's "a measure on 𝒱, which is a merit function" (03:L122).** Overstated. F00:L1302: "This does not prohibit mathematics about counts". What would be a merit function is **an order of candidates** by such a measure. **Fix:** "an order of candidates by a measure on 𝒱 would be a merit function (D3:L25, L516)."

#### 4. History

- **(E).** The theory keeps history out of (E): "None inspects a label" (D3:L265); "the reasons for adopting it are assessed elsewhere" (D3:L277). Nothing in 03 puts history into (E). **UPHELD.**
- **The record.** The theory places narrowings in the record: "scope-honesty lives in the record" (D3:L43); see also L55, L159, L161 and L602. 03 sends "dropped after a failure or never claimed" there. That is licensed. Only the wording "historical index is a record" or "the index records" is wrong (2e, 13).
- **The words.** "Earlier", "later" and "written" should be structural (12). "It is not a fact about authorship or time" (03:L76) is true of the hypotheses once they are.

---

#### 5. Cases

##### 5.1 The three test situations

**Saint: UPHELD.** Two precisions:
1. The companion clause's antecedent is false here. The changed saint fails (F1) or non-circular dependence "on any contract that contains the failed Saturday" (EC L110). So the lemma adds a conditional reason only: *had* it rescued, it would be critical.
2. "Must do work, and then (F1) … binds it" misplaces the binding. (F1) binds "every active component" (D3:L233), idle or not. What changes when the saint is given work is that its relation is no longer full, so (F1) can fail.

A literal point: the companion's E₁|(Γ₁∖B) *removes* the changed saint and does not restore the idle one. By L313 the two meet (E) alike, so nothing turns on it.

**North bed, open: UPHELD.** "Blocked as a fact, unmarked in the record" is EC L131 verbatim. The "52" is from the (A)-only model.

**Narrowed question: UPHELD on the description.** "Still passes (E)" is CORRECTED to EC's qualified pass: "Yes, in draft 3, on the reading of (F1) that Grievance 1 gives", with non-circular dependence's second sentence "unsettled" (EC L140–143).

##### 5.2 The cases in the brief

**N2: CORRECTED (no instance under (E)).** (H\*) needs Account(E₀, f) for every f ∈ F, with E₀ the original myth. But "The myth's components have no anchors that track, for example, the tilt or other latitudes, so (F1), (F2) and (A) fail" (EC L525). The original myth is no account on its Greek jobs either. So the witness hypothesis fails, and "6 → 2, strict" is a fact of the (A)-only model (m3 M2). The companion clause does not apply either: the amended myth is no account on the southern jobs, and its "warmth sent south" is vacuously idle (EC L158). The verdict "No" is untouched and rests on (E) (EC L220, L525). The "risk away if strictness is read as merit" arises only in the (A)-only reading. It is smaller than 03 says, but still worth guarding.

**O1: CORRECTED.** The narrowing clause applies to a restated rule only if that rule is an account on its restricted contract. The fixed verdict is "Bruno has no explanation of the floods". EC flags that "a forecasting rule answers an identification question, not why the stream floods" (D3:L151; EC L262). So either there is no instance, or each restated rule is an account of a narrower, different question (D3:L151). On both readings, **no verdict moves**, and "the series as a whole is a retreat" stays SILENT (S81 results row O1: "SILENT … the same point"). The lemma has no notion of a series: **UPHELD.**

**N7: UPHELD for Maya.**
- The narrowing clause holds "whether … dropped after a failure, or was never claimed", so it marks her on neither reading. That avoids option (b)'s risk (EC L221).
- CORRECTED: "Bea's 'fuller' account is reach, by (H) in her family". (H) is about Pres in one family and says nothing about Maya. "Fuller" is reach by W34's definition: Bea's reach contains the job "why only in that range", on which Bea is an account and Maya is not (D3:L313). EC L246 says the same ("that is reach, not variation"). **Fix:** cite the reach definition, not (H).

**O36: CORRECTED.** "The witness is always a written earlier organization, never an unwritten variant" is false for the (a) iff, "strict exactly when some member of Pres(F) is not an account", because Pres's members are "unwritten by definition" (EC L67). It is also not needed for (H\*), whose hypothesis is structural. O36 is still unaffected, for a different reason. O36 concerns criticality in supports of the *written* Γ ("the supports assessed are subsets of the written Γ", D3:L299). The only criticality claim in the proposal, the companion clause, assesses subsets of the written Γ₁. **Replace with:** "Nothing failed. The companion clause assesses only subsets of the written Γ₁ (D3:L299), and (H\*) says nothing about whether P is critical."

**O45: UPHELD.** "whether or not anyone has described their work" (D3:L231); "A route already present in the candidate is a route" (D3:L307). No job fails. The lemma has no notion of when a part was added, which matches "does not make it a later addition".

**O47: UPHELD** as unaffected: nothing failed for E₀. But the row's own warning, "(ii) must not be read as 'the extension is an account'", shows that (ii) ascribes "never the harder to vary" to an organization that fails (E). That is the reason in 8 to replace (ii).

**O48: CORRECTED (minor).** O48 concerns the *population* 𝒯 of Derivation 3: "a transport that would need a part every member of the population is built without is not in it" (D3:L475). It does not concern 𝒱. It is an analogue of hypothesis (iv), not support for it. Its sharper use is as the guard for limit (i) (see 7).

**D3-T: UPHELD.** The row applies Derivation 3 correctly (D3:L566–568). The discarded design fails a tried setting, as E₀ fails f\*, so it is not a survivor, and its behaviour elsewhere shows nothing about survivors. "With no second passing design nothing is left open" is "the population fixes it" (D3:L568). The analogy with limit (i) holds only once (i) carries the same qualification. As worded ("may … whenever"), (i) makes the claim that D3-T is built to catch.

**N1 (in 03's table, not in the brief): CORRECTED.** "The god is idle (D3:L313)" is one reading. On the case's words ("keeps the tilt steady") it is watched as a redundant route or an unfaithful component (CL:L1138). The row's conclusion (unaffected) stands.

---

#### 6. Corrected wording (for 03 §2)

**(a)** Keep only: replace "the containment need not be strict;" with "the containment need not be strict, and it is strict exactly when some member of Pres(F) is not an account on some job of F′ (Correction in a common family);". Drop "(a job is a question, Part III)", or declare it as a CLAIM (see 4).

**(b)**

> **Correction in a common family.** Let \(\mathcal V\) be a declared family of organization edits of \(E_1\), with a member \(v_0\) whose candidate is \(\mathcal E_0\): its organization \(E_0\), transport \(t_0\) and commitments \(\Gamma_0\), with the named background fixed. Let \(\operatorname{Account}(E_0,f)\) for every \(f\in F\), and \(\neg\operatorname{Account}(E_0,f^*)\). By (A), every job whose contract holds a pair at which \(E_0\) answers otherwise than the target is such an \(f^*\). Then
> \[ v_0\in\operatorname{Pres}(F)\setminus\operatorname{Pres}(F\cup\{f^*\}),\quad\text{so}\quad \operatorname{Pres}(F\cup\{f^*\})\subsetneq\operatorname{Pres}(F).\tag{H\(^*\)}\]
> If also \(\operatorname{Account}(E_1,f^*)\), and \(E_1|(\Gamma_1\setminus B)\) is \(\mathcal E_0\) under the declared restriction for a nonempty \(B\subseteq\Gamma_1\), then \(\operatorname{CriticalBlock}(B;\Gamma_1,f^*)\). Where the identity edit is in \(\mathcal V\), \((1,v_0)\in\operatorname{Boundary}_{E_1,f^*}\) (D). *Proof.* (H) gives the containment, and the hypotheses place \(v_0\) on either side. For the block, \(\Gamma_1\in\mathsf S_{E_1,f^*}\) and \(\Gamma_1\setminus B\notin\mathsf S_{E_1,f^*}\). ∎
>
> If \(\mathcal V\) contains the identity edit, the same argument covers a narrowing. If \(E\) is an account on every job of \(F\) and not on \(f^*\), then \(\operatorname{Pres}(F)\supsetneq\operatorname{Pres}(F\cup\{f^*\})\). This is so whether \(f^*\) was claimed at an earlier index and later omitted, or never claimed. Which of the two it was is read from the record of indexed claims (Part III, Scope; Part VIII, Historical index; Derivation 7), not from \(\operatorname{Pres}\).
>
> (H\*) says what \(f^*\) excludes and nothing more.
> (i) \(\operatorname{Pres}(F\cup\{f^*\})\) excludes no member for its answer at a pair that no job of \(F\cup\{f^*\}\) holds. Whether \(\mathcal V\) has a member that answers there as \(E_0\) does is fixed by \(\mathcal V\), as what a history leaves open is fixed by a population (Derivation 3).
> (ii) (H\*) compares \(\operatorname{Pres}(F)\) with \(\operatorname{Pres}(F\cup\{f^*\})\) in one family. It does not compare \(E_1\) with \(E_0\). They are different organizations with different families, and it gives no ground for calling either harder to vary than the other.
> (iii) Two members of \(\mathcal V\) that are both accounts on every job of \(F\cup\{f^*\}\) both belong to \(\operatorname{Pres}(F\cup\{f^*\})\). Only a job on which one meets (E) and the other does not separates them.
> (iv) If no member of \(\mathcal V\) has \(\mathcal E_0\) as its candidate, (H\*) does not apply, and the containment may be non-strict.
>
> (H\*) relates two subsets of one family of one organization under one interpretation, which is the premise of (H). It orders no candidates and uses no fact about who wrote any candidate or when.

**(c)** "A set of jobs that omits one its candidate fails has, when \(\mathcal V\) contains the identity edit, a strictly larger \(\operatorname{Pres}\) than the same set with that job (Part VI), whether the job was dropped after a failure or never claimed. Which of the two it was is shown by the record of indexed claims, not by \(\operatorname{Pres}\)."

##### Section 1 answers, corrected

- **(1) PARTLY.** Unchanged, except that "legitimate" becomes "a new claim at a new index, recorded, not certified (D3:L159)".
- **(2) NO.** Unchanged in substance. The first bullet is [F]. "(A), not variation" becomes "(E), not variation", with the note that under full (E) the one-summer patch may already fail non-circular dependence at the failed job. 2e is fixed as above.
- **(3) NO.** File 00's limit is not relaxed, and (H\*) makes no comparison of the explanation with its correction.

##### Section 4, corrected

- "It cannot flip any case, since it changes no definition" holds only without (a)'s parenthesis.
- "A Part VI measure … needs a measure on 𝒱, which is a merit function" becomes "an order of candidates by a measure on 𝒱 would be a merit function".
- "'Adding the failed job must shrink Pres' is always met" becomes "is met exactly when 𝒱 contains a witness, so as a condition it would turn on how 𝒱 is declared, an input no one declares (D3:L516)".
- The gain "Part VI gets its link to correction" becomes "(D) already records it; the lemma states it".

#### 7. What survives unchanged

- (H\*) as mathematics.
- The companion clause.
- Limit (iv).
- The hypotheses section.
- Items 1, 2 and 4 of "Why it does not rank".
- Every "no verdict moves".
- The Saint, north-bed, O45, O47 and D3-T rows.
- The bottom line.

On the bottom line, the text states it outright: "Objectivity lives in the physics and the fidelity facts; scope-honesty lives in the record" (D3:L43). A lemma about Pres cannot tell a dropped job from one never claimed, so the record is not redundant.

---

## Appendix E — The model attack (working file 04b, copied unchanged except as noted)

### 04b Model attack: counterexamples to the correction lemma (03), and a check of the 02 models

*Working file, 24 September 2026. Nothing in the repository was changed. The Pinker folder was not opened. Scripts and outputs: `ratchet/attack/` (Python 3.11, standard library, all eight run in under 10 seconds). `fe.py` is a new finite implementation of Account (E) with Part II's solution semantics: organizations as ports and component relations, Sol as the intersection (O), deletion as the full relation, the transport map π, and (A), (F1), (F2) and NonCircular. `pl.py` is an independent pair-level engine (Account = (A)), written without importing `ratchet/models`. Re-read for this: 03 in full; 02 in full; `models/*.py` and their outputs; D3 Part II (L81–105), Part V (L229–283), Part VI (L285–313), L159, L363, L510–532; F00 L162, L270–300, L352–386; EC section 2 and option (b).*

**Tags.** [COMPUTED] exact output of a script on a stated finite model. [PROVED] a short general argument. [F] follows from quoted lines. [T] a line says it. [I] my inference.

**How the attack was run.** Each claim was taken at its word. I then looked for a finite model where the stated hypotheses hold and the conclusion fails. Where the models of 02/03 read a term one way (a job is one pair; Account is (A) alone; a deleted part is switched off), I also ran the theory's own reading of that term (a job is a question whose contract holds the baseline; Account is (E); a deleted component imposes the full relation, D3:L101). Where 03 says "one interpretation" (03:L64), each member of a family keeps the later explanation's transport, as file 00 requires: "Each pair retains its edited components, background, and interpretation" (F00:L294).

---

#### 0. Bottom line

1. **All the numbers stand.** 02 and 03 report 25 numbers, and every one was re-derived independently (A0, 25 of 25). The four model scripts re-run byte-identical to their saved outputs, and 02's appendix matches them verbatim. What fails is the readings and labels, not the arithmetic.
2. **Under the models' reading, (H\*) cannot fail.** The witness is built to answer as the earlier explanation, so the "about 274,000 instances" test the encoding, not the lemma (A6c).
3. **Under Account (E) with one interpretation, (H\*) fails for the owner's own good rescue.** This happens when the rescue posits a mechanism with its own variable. The "switched-off" or "deleted" earlier version is then not the earlier candidate. It *denies* the new mechanism where the earlier explanation said nothing about it, and so it fails a job the earlier explanation did. Take the jobs {summers seen, a shaded year with the early variety}. Adding the failed summer then excludes nothing: 1 → 1. The same correction written as a changed rule with no new port gives 2 → 1. So two embeddings of one correction give opposite answers (A1).
4. **Four more clauses are false or need an unstated hypothesis:**
   - the narrowing clause needs the identity edit in the family (A2);
   - a block that only adds cannot rescue a determined wrong answer, and the companion's computed support depends on reading "deleted" as "switched off" (A3);
   - limit (iii) should say (E), not (A) (A5);
   - two of 03 §4's arguments are family-dependent or false (A4, A1).
5. **The owner's position is refuted on the same three points as in 03, now also under full (E).**
   - (1) The mistake comes back where no job reaches it: 56 of 64 members (A7).
   - (2) On the record, a bad rescue is an account exactly when the good one is. Inside the old explanation's own family it registers as *harder* to vary (4 → 2) (A4(ii), A5(2)).
   - (3) The embedding meets file 00's premise only if the earlier *candidate*, with its transport, is a member. An organization edit under one interpretation does not give that whenever the correction adds a variable (A1).

---

#### 1. Verdicts, claim by claim

"03:Ln" is a line of `03 proposal.md`, and "02:Ln" a line of `02 models.md`.

| # | Claim | Verdict | Counterexample or evidence | Minimal hypothesis that would block the counterexample |
|---|---|---|---|---|
| 1 | (H\*): v0 ∈ Pres(F) \ Pres(F∪{f\*}), so Pres(F∪{f\*}) ⊊ Pres(F) (03:L50–53) | **CORRECTED** | CE1, CE2. Under (A) alone it is a tautology. Under (E) with E1's interpretation, a v0 meeting "E1,v0 = E0" up to the added port fails (F2)/(F1) on a job E0 does. Result: 1 → 1. Read literally, no organization edit deletes a port, so the hypothesis cannot be met and the lemma is vacuous. | Replace "Account(E0, f) for f ∈ F" with "Account(E1,v0, f) for f ∈ F under the family's interpretation". Structurally: v0 removes B together with the ports only B assigns and restricts the transport to the rest (a candidate edit), or E1 adds no port its transport reads from the target. |
| 2 | "(H\*) relates two subsets of one family of one organization under one interpretation … holds for every declared V that has the member v0" (03:L64) | **CORRECTED** | CE1. "Has the member v0" (an organization) is not enough under one interpretation. | As row 1. |
| 3 | 03 §1(3) "Met, not relaxed": one organization, one interpretation, one family, so (H) applies with a guaranteed witness (03:L30) | **CORRECTED** | CE1, CE2. It is met only when the earlier candidate, with its own transport, is a member. For a correction that adds a variable, that takes members with different transports (candidate edits). A strict "one interpretation" loses the witness. | As row 1. |
| 4 | "By (A), every job whose contract holds a pair at which E0 answers otherwise than the target is such an f\*" (03:L50) | **UPHELD** | Account ⇒ (A) (D3:L261). | — |
| 5 | "Where E1 only adds a block B, E0 = E1\|(Γ1\B)" (03:L50) | **CORRECTED** | CE4, CE5. Under (O), adding a block only shrinks Sol, so an added block can never turn a determined wrong answer right: 0 of 256, 0 of 65,536 and 0 of 3,000 relations. A rescue of a *mistake* changes a component. Under Part II deletion, E1\|(Γ1\B) is then not E0: it leaves the answer undetermined. | Add "and E0's answer at f\* is undetermined" (a failure by silence, A3(c)); or declare the Part VI restriction operation as "set B's ports to E0's values" and state it. |
| 6 | Companion: CriticalBlock(B; Γ1, f\*) (03:L53); "all three rescues are" critical at the failed job (03:L25) | **CORRECTED** | CE5. Under Part II deletion, B is critical at the failed job *and at every old job*, so criticality marks no rescue work. The "not critical for J_before" in m3 comes from `profile(deleted=…)` switching an override off (m1:L121). Under full (E), even switch-off leaves B critical at the shaded early-variety job. | Declare the restriction operation (D3:L287 already requires one) as switch-off, and restrict the clause to (A)-level jobs; or drop "critical at f\*" as a mark of rescue. |
| 7 | Narrowing clause: E accounts on F and not on f\* ⇒ Pres(F) ⊋ Pres(F∪{f\*}) (03:L56) | **CORRECTED** | CE3. With a family that lacks the identity edit, the hypotheses hold and the result is 0 → 0 or 1 → 1, under both (A) and (E). | "the identity edit is a member of V". |
| 8 | Pointer (c): a narrowing that omits a failed job "enlarges Pres whether or not that job was ever claimed" (03:L66) | **CORRECTED** | CE3. | As row 7. |
| 9 | Limit (i): a member of Pres(F∪{f\*}) may repeat E0's answer where no job reaches (03:L59) | **UPHELD** | Also under full (E): 56 of 64, 24 of 32 with the seed trial, and 0 of 1 on the open question (A7). | — |
| 10 | Limit (ii): Pres_V0(F) = Pres_V(F) ∩ V0, so where E0's own family sits inside V the later organization is never the harder to vary (03:L60) | **UPHELD** as a conditional set identity under one interpretation | Its use without the condition (rows 21, 26) is CORRECTED by CE7. | — |
| 11 | Limit (iii): only a job on which one member is an account and the other is not separates them, "and that is (A) on that job, not variation" (03:L61) | **CORRECTED** | CE6. Two members give identical answers at all 16 pairs, yet the shaded early-variety job separates them through (F2)/(F1), with (A) holding for both. | Read "(E) on that job". |
| 12 | Limit (iv): without v0 the containment may be non-strict (03:L62) | **UPHELD** | A4(iv), A2, and m3's control. | — |
| 13 | "It orders no candidates. It uses no fact about who wrote E1 or when." A rival's extension gets the same result (03:L64, L77) | **UPHELD** | Nothing in `fe.py` or `pl.py` refers to authorship. | — |
| 14 | "It is a statement that a witness exists, not a count … no choice of menus flips it" (03:L78) | **CORRECTED** | CE8. The same correction with a menu lacking "off" gives 1 → 1 against 2 → 1 (A4(iv)). Under (E), the same correction with a mechanism port gives 1 → 1 against 2 → 1 (A1). The witness's existence *is* a menu fact. | Add "among families holding a member that is an account on F and not on f\*". |
| 15 | Edit (a): strict exactly when some member of Pres(F) is not an account on some job of F′ (03:L46) | **UPHELD** | A tautology given F ⊆ F′. | — |
| 16 | Hypotheses needed: without v0, 1 → 1; without "E0 does F", 1 → 1 (03:L69–70) | **UPHELD** | Reproduced. | — |
| 17 | Hypotheses needed: "add a job nothing fails (another wet spring with the usual planting) … 1 → 1" (03:L71) | **CORRECTED** | CE12. As run in m3 the control drops two hypotheses at once, since its F = J_after already holds f\*. The clean control gives 2 → 2. Read as a question (03's edit (a)), the job {baseline, wet spring} has no contrast, so *every* member fails NonCircular: 1 → 0, strict. | A job must hold a pair whose answer differs from the baseline's; use {baseline, shade, wet spring} (1 → 1 under (E)). |
| 18 | Redescription keeps the witness and the strictness, which meets file 00's "splitting one feature into ten" (03:L72) | **CORRECTED** | The splits checked do keep both (4 → 3, 32 → 31, re-derived). But a redescription that drops "off" loses both (A4(iv)), and so does one that adds a mechanism port, under (E) (A1). | As rows 1 and 14. |
| 19 | 03 §1(1): not a ratchet; dropping the failed job gives back the larger Pres (03:L16) | **UPHELD** | Also under full (E): narrowing the corrected rule back to the summers seen readmits the version that answers as E0 (A7). | (Needs the identity or a v0 in V, row 7.) |
| 20 | 03 §1(2): all three rescues are in Pres(record + f\*) = 52; "Only the seed trial … or the open question … separates them" (03:L21) | **CORRECTED** (the second half) | CE13. Four single summers separate good from wet-spring: the seed trial, its windy twin, and a wet spring with the usual planting, calm or windy. | Rephrase: "only a job holding a pair where they answer differently". |
| 21 | 03 §1(2): "a family that extends the old explanation never has the smaller Pres" (03:L22) | **UPHELD** inside an embedding (A0: 65,536 of 65,536); **CORRECTED** as a claim about the correction | CE7. With separately declared own families, the correction is harder to vary on the old jobs: 4 against 2, and 64 against 2. | Limit (ii)'s condition: E0's own declared family is contained in V. |
| 22 | 03 §1(2): symmetric families give equal Pres "1:1, 4:4, 6:6, 64:64" (03:L23, L126) | **CORRECTED** | CE14 (a label error). 64:64 (and the V+W/W+V 4:4 of 02:L158) compare one family with itself: the predicate sets are identical. The genuine symmetric pairs are 1:1, 4:4 (V+Wi/W+Wi) and 6:6. The symmetry also holds under full (E) (A5(2)). | Drop the identity rows. |
| 23 | 03 §1(2): the narrowing is "the one place where 'more versions fit' is a theorem" (03:L24) | **CORRECTED** | CE3. | Row 7's hypothesis. |
| 24 | 03 §1(3): "'Own' does no formal work" (03:L31) | **UPHELD** | — | — |
| 25 | 03 §1(3): "Taken each with its own family, before and after are disjoint" (03:L29), from 02 (02:L25, L131: "disjoint … never nested") | **CORRECTED** | CE10. In own families the "disjointness" is tuple length (02 §4 says so itself), not a finding. In an embedded family whose old sun component reads rain, Pres_E0(J_before) and Pres_E1(J_after) overlap in 2 members. | "E0's own family has no member that does f\*." |
| 26 | 03 §4: "A correction must be harder to vary" would refuse the neighbour's rescue, since on the old jobs every extension is at least as easy to vary (03:L124) | **CORRECTED** | CE7. Pair A: 1 → 2, easier. Pair B: 4 → 2, harder. Pair C: 64 → 2, harder. Every family holds a member answering as E0. | Limit (ii)'s condition, stated in the sentence. |
| 27 | 03 §4: "'Adding the failed job must shrink Pres' is always met, by the lemma, so it would do nothing" (03:L125) | **REFUTED** | CE8, CE1. It is not always met: 1 → 1 with a menu lacking "off" (under (A)), and 1 → 1 for the good rescue with a mechanism port (under (E)). As a condition of (E), it would refuse the neighbour's-variety rescue under one description and pass it under another. | Rows 1 and 14 together; then it is met, and does nothing. |
| 28 | 03 §4: any Pres test separating good from bad fails on the symmetric record (03:L126) | **UPHELD** | A0, and A5(2) under full (E): both in Pres on the record; only a separating job decides. | — |
| 29 | 03 §5.1: (F1) "could shrink the sets … without touching strictness" (03:L133) | **CORRECTED** | [F] If (F1) empties Pres(F), then Pres(F∪{f\*}) = Pres(F) = ∅: not strict. CE1 shows that (F1)/(F2) can also remove the witness while Pres(F) stays non-empty. | The lemma's own hypothesis (E0, or v0, an account on F), not the (A) shadow of it. |
| 30 | 03 §3: "no verdict moves" | **UPHELD** | A lemma adds no condition. Detail: the Saint row's companion reason depends on the restriction operation (row 6), and the N2 row's "6 → 2, strict" is an (A)-level fact. Under (E), N2 has an instance only if the unamended myth is an account on the Greek jobs. | — |
| 31 | 02 numbers (M1, M2, CX1–CX5, M3) | **UPHELD** | A0: 25 of 25 re-derived. The four scripts re-run byte-identical. 02's appendix matches its outputs. | — |
| 32 | 02 §4 "The shrink is always strict"; 02 §6 fact 1 (02:L129, L190) | **CORRECTED** | CE1: under (E), "E0 ∈ V" is exactly what the embedding fails to give. | Row 1. |
| 33 | 02 §8.4: an embedding by a constant other than "off" gives the same containment facts (02:L220) | **CORRECTED** | CE1. Under (E), the constant is an *assertion* about the new port, and (F2) checks it. | Row 1. |
| 34 | 02 §0.3 and fact 2: on fixed jobs every added component makes Pres weakly larger (02:L26, L191) | **CORRECTED** | CE7. True inside an embedding with Vers(E0) ⊆ Vers(E1), false between declared own families. | Limit (ii)'s condition. |
| 35 | 02 CX4: a genuinely new job (BG_rain) excludes nothing (02:L178) | **UPHELD** for a job read as a pair; **CORRECTED** for a job read as a question | CE12. | Row 17. |
| 36 | 02 §2/§7 option (b) comparison (m1 "consequences") | **CORRECTED** | CE15. m1 deletes by switching off. With "deleted" read as Part II deletion, every added override has a consequence at every sunny-south pair of its contract, and (b) marks none of good, bad or patch (02 has it marking all three on J_after, and the patch on C_full). | Option (b) must declare that "deleted" means "set to the earlier value". |
| 37 | m1 (i) NonCircular column | **UPHELD** | Re-run with Part II deletion: 0 of 9 verdicts change (A6d). | — |
| 38 | m3 check (1), "about 274,000 instances, no failure" | **UPHELD** as arithmetic; **no evidential weight** | CE11. v0's okmask equals E0's right-pairs by construction, so no failure was possible (A6c). | — |

---

#### 2. The counterexamples

##### CE1. The witness is lost under (E) with one interpretation (A1). Attacks rows 1–3, 27, 32, 33.

**Model.** [COMPUTED]
- **Target D.** Ports W, Wi, V, Sun, a hidden variety effect ovrD, and first. dvar: ovrD = [V = early]. dfirst: first = N if ovrD, else the sunnier bed.
- **E0**, with its own transport. Ports W, Wi, Sun, first. One component: sun, first = Sun. π0 forgets V.
- **E1, Emb-1: the owner's good rescue as a mechanism.**
  - var: ovr = [V = early]. sun′: first = N if ovr, else g(Sun).
  - E1's transport reads ovr from ovrD, "the variety effect is on".
  - The family: sun′ ∈ 4 maps × var ∈ {off, always, early, late}. All members keep E1's interpretation (F00:L294, 03:L64).
  - Two readings of v0:
    - (β) var switched off: the models' reading.
    - (α) sun restored and var deleted: 03's "v0 restores it".
- **E1, Emb-2: the same correction as a changed rule, no new port.** rule: first = N if P(V), else g(Sun). v0 = rule ignoring V, which is E0 plus an unread input.
- **Jobs**, each a contract holding the baseline, per 03's edit (a):
  - j_seen = {recorded summers, shading test};
  - j_eshade = {baseline, a shaded year when the neighbour planted early}. E0 answers north, which is right.
  - j_fail = {baseline, failed summer}.

**Hypotheses hold.**
- E0 is an account on j_seen and j_eshade under full (E), and not on j_fail.
- Up to the added port, v0 is "the earlier candidate's organization, each component it keeps with its earlier anchor, and the named background fixed".
- The corrected candidate is an account on the open question in both embeddings, with identical answers at all 16 pairs.

**Conclusion fails.**

```text
Account read as FULL (E): (A), (F1), (F2), NonCircular
F = {j_seen, j_eshade}   [E0 own, full (E): does F? True  does f*? False]
   Emb-1, v0 = var switched off (beta)            |Pres(F)|=1 |Pres(F+f*)|=1  strict? False  v0 in Pres(F)? False  Pres(F+f*)={(sun'=id, var=early)}
      v0 fails: F2@dry/calm/early/shadeS F1@dry/calm/early/shadeS
   Emb-1 + v0 = sun restored, var deleted (alpha) |Pres(F)|=1 |Pres(F+f*)|=1  strict? False  v0 in Pres(F)? False  Pres(F+f*)={(sun'=id, var=early)}
      v0 fails: F2@dry/calm/late/sunS F2@dry/calm/late/shadeS; F2@dry/calm/late/sunS F2@dry/calm/early/shadeS
   Emb-2, v0 = rule ignoring V                    |Pres(F)|=2 |Pres(F+f*)|=1  strict? True   v0 in Pres(F)? True   Pres(F+f*)={(rule: N if early else id(Sun))}
```

Under (A) alone, all three rows are strict (2 → 1, 3 → 1, 2 → 1). So the failure comes from the interpretation, not the answers.

**Why.** [PROVED] E1's transport assigns the new port a value read from the target. Then any member with the new part switched off asserts that value is "off" everywhere. Any member with it deleted leaves the value free. (F2), π[Sol_D] = Sol_E, sees either one at a pair where the target has the effect on. The earlier explanation had no such port, so it asserted nothing there, and it passes wherever its answers are right. So Account(E1,v0, f) ≠ Account(E0, f) exactly on jobs that hold such a pair and that E0 does. The shaded early-variety year is one. Read literally, "E1,v0 = E0" cannot be met in Emb-1 at all ("any Emb-1 member with E0's port set? False"), because an organization edit cannot delete a port (D3:L101). So the lemma is vacuous there.

**What it means for the owner.** In Emb-1, the versions that repeat the mistake at f\* are already excluded by j_eshade, a job the old explanation *passed*. The failure adds no exclusion. "The failed case is what keeps the mistake out" is then false even at the failed pair.

**Minimal blocking hypothesis.** State the witness at the level where the proof uses it: *v0 is an account on every job of F under the family's interpretation* (the proof needs nothing else). Two structural sufficient conditions:
- (a) V is a family of candidate edits, and v0 removes B together with the ports only B assigns, with the transport restricted to the remaining ports. v0's candidate is then E0's.
- (b) E1 adds no port that its transport reads from the target.

Either way, 03 §1(3)'s "one organization, one interpretation" must become "one interpretation, restricted for v0".

##### CE2. One correction, two embeddings, opposite answers (A1). Attacks rows 1, 14, 18.

Emb-1 and Emb-2 hold the same final candidate. It has the same answers at all 16 pairs and is an account on the open question in both. On F = {j_seen, j_eshade} under full (E):
- Emb-1: 1 → 1, not strict;
- Emb-2: 2 → 1, strict.

Whether "the failed job excluded the old explanation" is therefore a fact about how the correction is written down. Blocking: as CE1.

##### CE3. The narrowing clause without the identity edit (A2). Attacks rows 7, 8, 23.

**Hypotheses hold.** E0 is an account on j_seen and not on j_fail.

**Conclusion fails** under both readings:

```text
  V1 = the other three sun maps (every edit changes something) full (E)  |Pres(F)|=0  |Pres(F+f*)|=0  strictly larger after the narrowing? False
  V2 = edits that add the variety part, any sun map          full (E)  |Pres(F)|=1  |Pres(F+f*)|=1  strictly larger after the narrowing? False
  V1 + identity                                              full (E)  |Pres(F)|=1  |Pres(F+f*)|=0  strictly larger after the narrowing? True
```

D3:L301 says only "a declared family V of organization edits". Nothing puts the identity in it.

**Blocking:** "the identity edit is a member of V".

##### CE4. An added block cannot rescue a mistake (A3(a)). Attacks row 5.

[PROVED] By (O), Sol is an intersection over components. So Sol(E0 + B) ⊆ Sol(E0) at every pair, and Ans(E0 + B) ⊆ Ans(E0) for the query "which bed first". If E0's answer at f\* is determined and wrong, E0 + B answers the same or answers nothing.

[COMPUTED] E0 + B answered north at f\* for 0 of 256 relations on (V, Sun, first), 0 of 65,536 on (V, Sun, ovr, first), and 0 of 3,000 random relations on all six ports. The subset property held at all 16 pairs for the 256.

So every rescue of a *mistake* changes a component, and "Where E1 only adds a block B, E0 = E1|(Γ1\B)" covers only failures by silence. A3(c) gives one: E0′ leaves the answer open for a changed planting, and there var is critical at f\*, with E1′|(Γ1\B) equal to E0′ exactly.

**Blocking:** add "and E0's answer at f\* is undetermined", or declare the restriction operation.

##### CE5. Criticality depends on the restriction operation (A3(b)). Attacks row 6.

```text
  (A)+NonCircular              restriction by deletion    B=var is  j_seen: CRITICAL;  j_eshade: CRITICAL;  j_fail: CRITICAL
  (A)+NonCircular              restriction by switch-off  B=var is  j_seen: not critical;  j_eshade: not critical;  j_fail: CRITICAL
  full (E), E1's transport     restriction by deletion    B=var is  j_seen: CRITICAL;  j_eshade: CRITICAL;  j_fail: CRITICAL
  full (E), E1's transport     restriction by switch-off  B=var is  j_seen: not critical;  j_eshade: CRITICAL;  j_fail: CRITICAL
```

Part VI takes E|W under "a declared restriction operation" (D3:L287). Part II deletes by imposing the full relation (D3:L101). m1 and m3 switch an override off (`profile`, m1:L121). Consequences:
- Under deletion, the rescuing part is critical everywhere the answer reads it, so "critical at the failed job" says nothing about rescue.
- Under switch-off with (E), it is critical at a job E0 already did.
- "E0 = E1|(Γ1\B)" holds, up to ports, only under switch-off.

**Blocking:** declare the restriction as "set B's ports to E0's values". Keep the companion's claim to f\*, and do not read non-criticality at old jobs from it.

##### CE6. Limit (iii): the separating job need not be (A) (A5(1)). Attacks row 11.

The two members var = [V = early] and var = [V = early ∧ Sun = S] answer identically at all 16 pairs, and both are right at all 16. j_eshade separates them: the second fails (F2) and (F1) at the shaded early-variety year, since its mechanism claims "no variety effect" there. (A) holds for both.

**Blocking:** "that is (E) on that job".

##### CE7. "Never harder to vary on the old jobs" turns on the declared families (A4(i)). Attacks rows 21, 26, 34.

```text
  pair A  E0: sun reads Sun (4 maps)             |Pres(J_before)|=  1   E1: sun reads Sun x var[V]     |Pres(J_before)|=  2  -> E1 EASIER to vary
  pair B  E0: sun reads Sun, W (16 maps)         |Pres(J_before)|=  4   E1: sun reads Sun x var[V]     |Pres(J_before)|=  2  -> E1 HARDER to vary
  pair C  E0: sun reads Sun, W, Wi (256 maps)    |Pres(J_before)|= 64   E1: sun fixed (id) x var[V]    |Pres(J_before)|=  2  -> E1 HARDER to vary
  every one of the six families holds a member answering exactly as E0 at all 16 pairs: True
```

"Every extension is at least as easy to vary" holds exactly when E0's own family is placed inside E1's (pair A). That is Vers(E0) ⊆ Vers(E1), a fact about the embedding, not about the correction. So 03 §4's argument that "a correction must be harder to vary" refuses the good rescue depends on the families. Under pairs B and C, the good rescue passes it.

**Blocking:** limit (ii)'s own condition, written into the sentence.

##### CE8. "No choice of menus flips it" / "always met, by the lemma" (A4(iv), A1). Attacks rows 14, 27.

```text
  sun[4] x var[V]  (holds v0 = var off)                                  |Pres(J_before)|=2  |Pres(J_after)|=1  strict? True
  rule "north first if the variety is P", P in {early, late} (no v0)     |Pres(J_before)|=1  |Pres(J_after)|=1  strict? False
```

Both families hold the corrected candidate. Together with CE1, strictness flips with the menu under (A) and with the port structure under (E). As a condition of (E), "adding the failed job must shrink Pres" would refuse the neighbour's rescue in one listing and pass it in another.

**Blocking:** hypothesis (iv) plus CE1's hypothesis. Under both, the claim is true and does nothing, which is 03's point.

##### CE9. A bad rescue registers as harder to vary, under file 00's own premise (A4(ii)). Against the owner's (2); supports 03.

In E0's own family with sun reading Sun and W (fixed organization, interpretation and family), the wet-spring rescue *is a member*:
- sun maps dry/sunS→S, dry/shadeS→N, wet/sunS→N, and wet/shadeS either way.
- Adding the failed summer takes Pres from 4 to 2.

By the measure, the bad rescue shows as a shrink, the same as any job added under (H). No organization change is needed, so no embedding question arises.

##### CE10. "Disjoint … never nested" is a menu artifact (A4(iii)). Attacks row 25.

Take U_B = sun[Sun, W] × var[V], with Vers(E0) = var off. Then |Pres_E0(J_before)| = 4 and |Pres_E1(J_after)| = 6, with an overlap of 2. With 02's menu the overlap is 0.

**Blocking:** "E0's own family has no member that does f\*".

##### CE11. m3's check (1) tests the encoding (A6c). Row 38.

"okmask of v0 (sun=id, all added parts off) == pairs E0 gets right: True". Every instance was therefore guaranteed. The lemma's content is that equality, and CE1 is where it fails.

##### CE12. "A job nothing fails" (A6a, A6f). Attacks rows 17, 35.

```text
  m3 as run: F = J_after     E0 does F? False E0 does the added job? True  |Pres| 1 -> 1  strict? False
  clean: F = J_before        E0 does F? True  E0 does the added job? True  |Pres| 2 -> 2  strict? False
  E1 family sun' x var[V], jobs {j_seen, j_fail} + {B0, wet spring}  (no pair contrasts with the baseline) full (E)  |Pres|=0
  E1 family sun' x var[V], jobs {j_seen, j_fail} + {B0, shade, wet spring}                                 full (E)  |Pres|=1
```

NonCircular needs a pair whose answer differs from the baseline's (D3:L255). A question whose contract has no such pair is one no candidate can account on.

**Blocking:** a job must hold a contrast.

##### CE13. More jobs separate the rescues than 03 says (A6e). Attacks row 20.

Any of the following, added to J_after, keeps the good rescue and drops the wet-spring rescue:
- dry/calm/early/sunS;
- dry/windy/early/sunS;
- wet/calm/late/sunS;
- wet/windy/late/sunS.

The windy twin of the seed trial also drops the patch.

##### CE14. Symmetry rows that compare a family with itself (A6b). Attacks row 22.

"good reads V+W, bad reads W+V: same set of override predicates? True". The same holds for V+W+Wi against W+V+Wi. The "good" family var[V+W+Wi] contains the rain rescue, so CX3's "good:V+W+Wi 64:1 good easier" (02:L600) sets a family holding both rescues against one holding only the bad one.

##### CE15. Option (b)'s marks depend on reading "deleted" as "switched off" (A6g). Attacks row 36.

```text
  E_good   on J_after  consequences (off): 0  -> MARKED             consequences (Part II): 1  -> not marked
  E_bad    on J_after  consequences (off): 0  -> MARKED             consequences (Part II): 1  -> not marked
  E_patch  on C_full   consequences (off): 0  -> MARKED             consequences (Part II): 7  -> not marked
```

(b)'s draft says "its answer there is not kept when that component is deleted" (EC, option (b)). With Part II deletion, the answer is "not kept" (it becomes undetermined) at every pair where the part could fire, so the do-nothing patch has 7 consequences.

**Blocking:** (b) must say "set to the earlier value" instead of "deleted". This is the same repair CE5 needs. It also bears on 02 §7's comparison of (b) with Pres.

---

#### 3. Errors found in the 02 models

The arithmetic has no errors (A0, 25 of 25; re-runs byte-identical). What needs fixing:

1. **Deletion.** `Family.profile(v, deleted=…)` switches a deleted override off (m1:L121). Part II frees its port.
   - No effect on m1 (i) (A6d, 0 of 9 changes).
   - It decides m3's companion column (CE5) and 02's option (b) marks (CE15).
2. **Account = (A) at single pairs** hides three things:
   - the transport (CE1);
   - the contrast a job needs (CE12);
   - (F1)/(F2) separations (CE6).

   02 §8.1 declares this reading, but 02 §4, §6 fact 1 and §8.4 draw conclusions ("always strict", "the same containment facts" for any constant) that do not survive it.
3. **Menu artifacts stated as findings:**
   - "disjoint … never nested" (CE10);
   - "every added component makes Pres weakly larger" (CE7).

   Both are true of 02's menus and embedding, not of corrections.
4. **Labels.** CX2's 64:64 and V+W/W+V rows compare a family with itself, and CX3's "good" row with V+W+Wi holds the bad rescue (CE14).
5. **m3's control** for "E0 fails the added job" drops two hypotheses at once (CE12).
6. **m3's "274,000 instances"** carries no evidential weight beyond the two-line proof (CE11).

Nothing else was found. The M2 numbers were checked by re-run only, not re-derived.

---

#### 4. What the proposal needs if it goes ahead [I]

- **(H\*)**: take the witness hypothesis as "v0 ∈ V is an account on every job of F, under the family's interpretation, and not on f\*". Add, as the sufficient condition, "v0 removes B together with the ports only B assigns, and the transport is restricted accordingly". Drop "It holds for every declared V that has the member v0". The conclusion is then (H) with a named witness, which is true and short.
- **§1(3)**: "Met, not relaxed" becomes "met when the earlier candidate, with its transport restricted, is a member". For a correction that posits a new variable, that takes a family of candidate edits. The owner's worry about file 00 returns at exactly that point.
- **Narrowing clause and pointer (c)**: add "when the identity edit is in V".
- **Companion**: either restrict it to failures by silence, or name the restriction operation (switch-off). Either way, drop 03:L25's "a rescuing addition is critical at the failed job" as a mark of rescue.
- **Limit (iii)**: "(E) on that job".
- **§4**: bullet 1 needs limit (ii)'s condition. Bullet 2 is false as stated (CE8). Bullet 3 stands, with the symmetric pairs 1:1, 4:4 and 6:6.
- **§2 point 4**: delete "no choice of menus flips it".
- **The hypothesis list**: replace the third control with the clean one, using a job that holds a contrast.

The overall verdicts of 03 (point (1) PARTLY, (2) NO, (3) PARTLY; no case verdict moves) stand. The ground for (3) gets narrower.

#### 5. What stays uncertain

1. **The finite (E) is my implementation.**
   - Edits set input ports.
   - (F1) compares a component's relation with the inputs the pair fixes against the anchor subnetwork's projection.
   - Anchors: sun′ to dfirst; var to dvar; E0's sun to both.
   - NonVacuous is taken as met.

   CE1 needs only (F2), with π reading the new port from the target. That follows from any transport that interprets the added mechanism as a real variable. A transport that interprets it as nothing would make (F1) unanchored (EC Situation 1).
2. **The restriction operation of Part VI is "declared"** (D3:L287), so switch-off is a legitimate declaration. CE5 shows only that the companion's verdict depends on which one is declared.
3. **Whether a family may hold members with different (restricted) transports and still count as "one interpretation"** in file 00's sense (F00:L162, L294). If it may, CE1's repair (a) costs nothing. If it may not, (H\*) is limited to corrections without new variables.
4. **Toy models.** A finite model is a counterexample, not a frequency.

---

#### Appendix: script outputs, verbatim

##### `a0_crosscheck.py`

```text
====================================================================================================
A0  INDEPENDENT RE-DERIVATION OF 02/03 NUMBERS
====================================================================================================
  |U1|                                                                   got 1088         02/03 says 1088         OK
  U1 |Pres(J_before)|                                                    got 68           02/03 says 68           OK
  U1 |Pres(J_after)|                                                     got 52           02/03 says 52           OK
  U1 |Pres(J_after + seed)|                                              got 35           02/03 says 35           OK
  U1 |Pres(J_after + BG_rain)|                                           got 17           02/03 says 17           OK
  U1 |Pres(C_full)|                                                      got 13           02/03 says 13           OK
  U2 |Pres(J_before)|, |Pres(J_after)|                                   got (272, 208)   02/03 says (272, 208)   OK
  rich sun x var[V,W,Wi] |Pres(J_before)|, |Pres(J_after)|               got (128, 64)    02/03 says (128, 64)    OK
  hybrids U1 (in Pres, repeating E0 elsewhere)                           got (52, 18)     02/03 says (52, 18)     OK
  hybrids U2                                                             got (208, 71)    02/03 says (208, 71)    OK
  hybrids rich                                                           got (64, 56)     02/03 says (64, 56)     OK
  hybrids rich, seed trial added                                         got (32, 24)     02/03 says (32, 24)     OK
  open question: U1, U2, rich |Pres|                                     got (13, 13, 1)  02/03 says (13, 13, 1)  OK
  CX2 good[V] : bad[W]                                                   got (1, 1)       02/03 says (1, 1)       OK
  CX2 good[V+Wi] : bad[W+Wi]                                             got (4, 4)       02/03 says (4, 4)       OK
  CX2 good[V+Sun] : bad[W+Sun]                                           got (6, 6)       02/03 says (6, 6)       OK
  CX2 good[V+W] : bad[W+V]                                               got (4, 4)       02/03 says (4, 4)       OK
  CX2 good[V+W+Wi] : bad[W+V+Wi]                                         got (64, 64)     02/03 says (64, 64)     OK
  CX3 good[V] : bad[W+Wi+Sun]                                            got (1, 96)      02/03 says (1, 96)      OK
  CX3 good[V+W+Wi] : bad[W]                                              got (64, 1)      02/03 says (64, 1)      OK
  patch, single-exception family |Pres(J_after)|                         got 1            02/03 says 1            OK
  patch, any-predicate family (4 ports) |Pres(J_after)|                  got 24576        02/03 says 24576        OK
  rain split in two: |Pres(J_before)| -> |Pres(J_after)|                 got (4, 3)       02/03 says (4, 3)       OK
  rain split in five                                                     got (32, 31)     02/03 says (32, 31)     OK
  U1: Pres_V0(F) strictly inside Pres_V(F), number of the 65536 F        got 65536        02/03 says 65536        OK

  all checks agree: True (25 of 25)
```

##### `a1_witness_under_full_E.py`

```text
====================================================================================================
A1  THE WITNESS UNDER FULL (E), ONE INTERPRETATION PER FAMILY
====================================================================================================
E0 (own transport) on each job, full (E):
   j_seen    Account=True  
   j_eshade  Account=True  
   j_fail    Account=False A@wet/windy/early/sunS F2@wet/windy/early/sunS F1@wet/windy/early/sunS
   j_open    Account=False A@dry/calm/early/sunS F2@dry/calm/early/sunS F1@dry/calm/early/sunS

Sanity: the corrected candidate is an account on the open question (all 16 pairs), full (E):
   Emb-1 (sun'=id, var=early)         True
   Emb-2 (rule: N if early else id(Sun)) True
   answers of the two corrected candidates agree at every pair? True

Literal hypothesis "E1_v0 = E0": port sets
   E0 ports           : ['Sun', 'W', 'Wi', 'first']
   every Emb-1 member : ['Sun', 'V', 'W', 'Wi', 'first', 'ovr'] (an organization edit cannot delete a port)
   Emb-2 v0 ports     : ['Sun', 'V', 'W', 'Wi', 'first'] (E0 plus the input V, read by nothing)
   any Emb-1 member with E0's port set? False

----------------------------------------------------------------------------------------------------
Account read as (A) ONLY, as in ratchet/models
----------------------------------------------------------------------------------------------------
F = {j_seen}   [E0 own, full (E): does F? True  does f*? False]
   Emb-1, v0 = var switched off (beta)            |Pres(F)|=2 |Pres(F+f*)|=1  strict? True   v0 in Pres(F)? True   Pres(F+f*)={(sun'=id, var=early)}
   Emb-1 + v0 = sun restored, var deleted (alpha) |Pres(F)|=3 |Pres(F+f*)|=1  strict? True   v0 in Pres(F)? True   Pres(F+f*)={(sun'=id, var=early)}
   Emb-2, v0 = rule ignoring V                    |Pres(F)|=2 |Pres(F+f*)|=1  strict? True   v0 in Pres(F)? True   Pres(F+f*)={(rule: N if early else id(Sun))}
F = {j_seen, j_eshade}   [E0 own, full (E): does F? True  does f*? False]
   Emb-1, v0 = var switched off (beta)            |Pres(F)|=2 |Pres(F+f*)|=1  strict? True   v0 in Pres(F)? True   Pres(F+f*)={(sun'=id, var=early)}
   Emb-1 + v0 = sun restored, var deleted (alpha) |Pres(F)|=3 |Pres(F+f*)|=1  strict? True   v0 in Pres(F)? True   Pres(F+f*)={(sun'=id, var=early)}
   Emb-2, v0 = rule ignoring V                    |Pres(F)|=2 |Pres(F+f*)|=1  strict? True   v0 in Pres(F)? True   Pres(F+f*)={(rule: N if early else id(Sun))}

----------------------------------------------------------------------------------------------------
Account read as FULL (E): (A), (F1), (F2), NonCircular
----------------------------------------------------------------------------------------------------
F = {j_seen}   [E0 own, full (E): does F? True  does f*? False]
   Emb-1, v0 = var switched off (beta)            |Pres(F)|=2 |Pres(F+f*)|=1  strict? True   v0 in Pres(F)? True   Pres(F+f*)={(sun'=id, var=early)}
   Emb-1 + v0 = sun restored, var deleted (alpha) |Pres(F)|=2 |Pres(F+f*)|=1  strict? True   v0 in Pres(F)? False  Pres(F+f*)={(sun'=id, var=early)}
      v0 fails: F2@dry/calm/late/sunS F2@dry/calm/late/shadeS
   Emb-2, v0 = rule ignoring V                    |Pres(F)|=2 |Pres(F+f*)|=1  strict? True   v0 in Pres(F)? True   Pres(F+f*)={(rule: N if early else id(Sun))}
F = {j_seen, j_eshade}   [E0 own, full (E): does F? True  does f*? False]
   Emb-1, v0 = var switched off (beta)            |Pres(F)|=1 |Pres(F+f*)|=1  strict? False  v0 in Pres(F)? False  Pres(F+f*)={(sun'=id, var=early)}
      v0 fails: F2@dry/calm/early/shadeS F1@dry/calm/early/shadeS
   Emb-1 + v0 = sun restored, var deleted (alpha) |Pres(F)|=1 |Pres(F+f*)|=1  strict? False  v0 in Pres(F)? False  Pres(F+f*)={(sun'=id, var=early)}
      v0 fails: F2@dry/calm/late/sunS F2@dry/calm/late/shadeS; F2@dry/calm/late/sunS F2@dry/calm/early/shadeS
   Emb-2, v0 = rule ignoring V                    |Pres(F)|=2 |Pres(F+f*)|=1  strict? True   v0 in Pres(F)? True   Pres(F+f*)={(rule: N if early else id(Sun))}

----------------------------------------------------------------------------------------------------
What v0 (beta) asserts that E0 did not: its ovr port against the target's variety effect
----------------------------------------------------------------------------------------------------
   dry/calm/late/sunS         E0 answer ['S'] v0 answer ['S'] v0 ovr [0]  target ovrD 0
   dry/calm/late/shadeS       E0 answer ['N'] v0 answer ['N'] v0 ovr [0]  target ovrD 0
   dry/calm/early/shadeS      E0 answer ['N'] v0 answer ['N'] v0 ovr [0]  target ovrD 1
   wet/windy/early/sunS       E0 answer ['S'] v0 answer ['S'] v0 ovr [0]  target ovrD 1
```

##### `a2_narrowing_without_identity.py`

```text
====================================================================================================
A2  NARROWING CLAUSE: E = E0 narrowed to the summers seen (F = {j_seen}), f* = the failed summer
====================================================================================================
Hypotheses: E0 accounts on j_seen? True   E0 accounts on j_fail? False

  V1 = the other three sun maps (every edit changes something) (A) only  |Pres(F)|=0  |Pres(F+f*)|=0  strictly larger after the narrowing? False
  V1 = the other three sun maps (every edit changes something) full (E)  |Pres(F)|=0  |Pres(F+f*)|=0  strictly larger after the narrowing? False
  V2 = edits that add the variety part, any sun map          (A) only  |Pres(F)|=1  |Pres(F+f*)|=1  strictly larger after the narrowing? False
  V2 = edits that add the variety part, any sun map          full (E)  |Pres(F)|=1  |Pres(F+f*)|=1  strictly larger after the narrowing? False
  V1 + identity                                              (A) only  |Pres(F)|=1  |Pres(F+f*)|=0  strictly larger after the narrowing? True
  V1 + identity                                              full (E)  |Pres(F)|=1  |Pres(F+f*)|=0  strictly larger after the narrowing? True
  V2 + identity                                              (A) only  |Pres(F)|=2  |Pres(F+f*)|=1  strictly larger after the narrowing? True
  V2 + identity                                              full (E)  |Pres(F)|=2  |Pres(F+f*)|=1  strictly larger after the narrowing? True

  V2 members in Pres(F) and in Pres(F+f*): ['(rule: N if early else id(Sun))'] ['(rule: N if early else id(Sun))']
```

##### `a3_companion.py`

```text
====================================================================================================
A3  THE COMPANION CLAUSE UNDER PART II DELETION
====================================================================================================
----------------------------------------------------------------------------------------------------
(a) PURE ADDITION: E1 = E0 + B, E0 = "the sunnier bed first" kept unchanged
----------------------------------------------------------------------------------------------------
  B any relation on (V, Sun, first)                          relations tried=   256  E0+B answers north at f*: 0  Ans(E0+B) inside Ans(E0) everywhere: True
  B any relation on (V, Sun, ovr, first), ovr a new port     relations tried= 65536  E0+B answers north at f*: 0  Ans(E0+B) inside Ans(E0) everywhere: not run (f* checked)
  B reads W, Wi, V, Sun, ovr, first                          random relations= 3000  E0+B answers north at f*: 0
  So a block added beside a component that already fixes a WRONG answer cannot rescue: the rescue
  must change a component, and then E0 = E1|(Gamma1 - B) is false and the companion is silent.

----------------------------------------------------------------------------------------------------
(b) THE GARDENER'S RESCUE (a1, Emb-1): E1 = {sun': N if ovr else Sun, var: ovr = [V=early]}, B = {var}
----------------------------------------------------------------------------------------------------
  E1|(Gamma1 - B) answers equal E0's at every pair?  deletion: False   switch-off: True
  e.g. at dry/calm/late/sunS: E0 ['S'], deletion ['N', 'S'], switch-off ['S']
  (A)+NonCircular              restriction by deletion    B=var is  j_seen: CRITICAL;  j_eshade: CRITICAL;  j_fail: CRITICAL
  (A)+NonCircular              restriction by switch-off  B=var is  j_seen: not critical;  j_eshade: not critical;  j_fail: CRITICAL
  full (E), E1's transport     restriction by deletion    B=var is  j_seen: CRITICAL;  j_eshade: CRITICAL;  j_fail: CRITICAL
  full (E), E1's transport     restriction by switch-off  B=var is  j_seen: not critical;  j_eshade: CRITICAL;  j_fail: CRITICAL

----------------------------------------------------------------------------------------------------
(c) WHERE THE COMPANION APPLIES: an E0 that was SILENT at f* (undetermined), not wrong
----------------------------------------------------------------------------------------------------
  E0' answers at f*: ['N', 'S'] (target ['N'])   E1' answers at f*: ['N']
  E0' does j_seen: True  j_eshade: True  j_fail: False ;  E1' does j_fail: True
  E1'|(Gamma - var) = E0' exactly (same ports, same components)? True
  -> CriticalBlock(var; Gamma1, j_fail): True. The companion holds here, where E0 said nothing at f*.
```

##### `a4_family_choice.py`

```text
====================================================================================================
A4  RESULTS THAT TURN ON THE DECLARED FAMILY
====================================================================================================
----------------------------------------------------------------------------------------------------
(i) Is the correction harder to vary than E0 on the OLD jobs (J_before)?  Each own family declared separately.
----------------------------------------------------------------------------------------------------
  pair A  E0: sun reads Sun (4 maps)             |Pres(J_before)|=  1   E1: sun reads Sun x var[V]     |Pres(J_before)|=  2  -> E1 EASIER to vary
  pair B  E0: sun reads Sun, W (16 maps)         |Pres(J_before)|=  4   E1: sun reads Sun x var[V]     |Pres(J_before)|=  2  -> E1 HARDER to vary
  pair C  E0: sun reads Sun, W, Wi (256 maps)    |Pres(J_before)|= 64   E1: sun fixed (id) x var[V]    |Pres(J_before)|=  2  -> E1 HARDER to vary
  every one of the six families holds a member answering exactly as E0 at all 16 pairs: True
  -> "every extension is at least as easy to vary on the old jobs" holds in pair A only; it is the
     embedding (E0's own family placed inside E1's) that makes it true, not the correction.

----------------------------------------------------------------------------------------------------
(ii) The bad rescue as a member of E0's OWN family (sun reads Sun and W): no organization change at all
----------------------------------------------------------------------------------------------------
  |Pres(J_before)| = 4   |Pres(J_after)| = 2   (the rescue registers as a SHRINK: harder to vary)
    member of Pres(J_after): sun map dry/sunS->S, dry/shadeS->N, wet/sunS->N, wet/shadeS->S
    member of Pres(J_after): sun map dry/sunS->S, dry/shadeS->N, wet/sunS->N, wet/shadeS->N
  -> "in a wet spring the north bed ripens first" is a member of the old family; by (H) adding the
     failed summer shrinks Pres. Owner's (2) ("more versions fit") is reversed under file 00's own premise.

----------------------------------------------------------------------------------------------------
(iii) "Pres before and Pres after are disjoint in every rescue that added a part": embedded family
      U_B = sun[Sun,W] x var[V]; Vers(E0) = var off
----------------------------------------------------------------------------------------------------
  |Pres_E0(J_before)| = 4  |Pres_E1(J_after)| = 6  overlap = 2  -> NOT disjoint
  (02's menu, sun[Sun] x var[V]: overlap = 0 -> disjoint)

----------------------------------------------------------------------------------------------------
(iv) Strictness of (H*) for ONE correction, two menus ("no choice of menus flips it")
----------------------------------------------------------------------------------------------------
  sun[4] x var[V]  (holds v0 = var off)                                  |Pres(J_before)|=2  |Pres(J_after)|=1  strict? True
  rule "north first if the variety is P", P in {early, late} (no v0)     |Pres(J_before)|=1  |Pres(J_after)|=1  strict? False
  Both families hold the corrected candidate; they differ only in whether the menu lists "off".
```

##### `a5_limit_iii_and_symmetry.py`

```text
====================================================================================================
A5  LIMIT (iii) AND THE SYMMETRY UNDER FULL (E)
====================================================================================================
(1) two members of sun' x var[V,Sun]:  (sun'=id, var=[V=early])  and  (sun'=id, var=[V=early and Sun=S])
    same answer as each other at all 16 pairs? True ; both right at all 16 pairs? True
    j_fail = {B0, f*}                first: True  second: True   second fails: -
    j_eshade = {B0, early/shadeS}    first: True  second: False  second fails: F2@dry/calm/early/shadeS F1@dry/calm/early/shadeS
    open question (16 pairs)         first: True  second: False  second fails: F2@dry/calm/early/shadeS F1@dry/calm/early/shadeS F2@dry/windy/early/shadeS
    -> a job separates them, and (A) holds for both at every pair: the separating conjunct is (F1)/(F2).

(2) good (var reads V) against bad (var reads W) in ONE family sun' x var[V,W], E1's transport
    the record + f*            |Pres|= 4   good in? True  bad in? True 
    + seed trial               |Pres|= 2   good in? True  bad in? False
    + wet spring (with shade)  |Pres|= 2   good in? True  bad in? False
    + wet spring, no contrast  |Pres|= 0   good in? False bad in? False
    open question              |Pres|= 1   good in? True  bad in? False
    -> on the record both are accounts under full (E) as well; only a separating job decides.
    The job {B0, wet spring} has no pair whose answer differs from the baseline (both south), so
    NonCircular fails for EVERY member: good fails it for that reason alone: ['NonCircular']
```

##### `a6_model_checks.py`

```text
====================================================================================================
A6  CHECKS OF ratchet/models
====================================================================================================
----------------------------------------------------------------------------------------------------
(a) m3 control "a new job no member fails" (sun x var[V]; wet springs with the usual planting)
----------------------------------------------------------------------------------------------------
  m3 as run: F = J_after     E0 does F? False E0 does the added job? True  |Pres| 1 -> 1  strict? False
  clean: F = J_before        E0 does F? True  E0 does the added job? True  |Pres| 2 -> 2  strict? False
  -> as run, two hypotheses are dropped at once (E0 already fails f* in F); the clean control
     drops one and still gives the non-strict case.

----------------------------------------------------------------------------------------------------
(b) 02 CX2 and CX3: are the "good" and "bad" families different families?
----------------------------------------------------------------------------------------------------
  good reads V+W      bad reads W+V      same set of override predicates? True
  good reads V+W+Wi   bad reads W+V+Wi   same set of override predicates? True
  good reads V        bad reads W        same set of override predicates? False
  good reads V+Wi     bad reads W+Wi     same set of override predicates? False
  "good" family var[V+W+Wi] contains the rain rescue (fires iff wet)? True ; the variety rescue? True
  "good" family var[V+W] contains the rain rescue (fires iff wet)? True ; the variety rescue? True
  -> CX2's 4:4 (V+W vs W+V) and 64:64 rows compare a family with itself; CX3's "good:V+W+Wi" row
     is a family holding BOTH rescues, set against one holding only the bad one.

----------------------------------------------------------------------------------------------------
(c) m3 check (1): is a failure possible under its encoding?
----------------------------------------------------------------------------------------------------
  okmask of v0 (sun=id, all added parts off) == pairs E0 gets right: True
  so for every F inside R0 and every f* in M(E0): v0 in Pres(F) and not in Pres(F+f*), by construction.
  The ~274,000 instances test the encoding, not the lemma; the lemma's content is the equality above,
  which a1 shows fails under full (E) with one interpretation.

----------------------------------------------------------------------------------------------------
(d) m1 (i) NonCircular with Part II deletion (override deleted -> its port free) instead of "off"
----------------------------------------------------------------------------------------------------
  E0             |C|= 2  NonCirc (m1, off)=True   NonCirc (Part II)=True 
  E0             |C|= 3  NonCirc (m1, off)=True   NonCirc (Part II)=True 
  E_good         |C|=16  NonCirc (m1, off)=True   NonCirc (Part II)=True 
  E_good         |C|= 3  NonCirc (m1, off)=True   NonCirc (Part II)=True 
  E_bad          |C|=16  NonCirc (m1, off)=True   NonCirc (Part II)=True 
  E_bad          |C|= 3  NonCirc (m1, off)=True   NonCirc (Part II)=True 
  E_patch        |C|= 3  NonCirc (m1, off)=True   NonCirc (Part II)=True 
  E_narrow       |C|= 2  NonCirc (m1, off)=True   NonCirc (Part II)=True 
  E_narrow_bare  |C|= 1  NonCirc (m1, off)=False  NonCirc (Part II)=False
  verdicts changed: 0

----------------------------------------------------------------------------------------------------
(e) which added jobs separate the good rescue from the wet-spring rescue on the record (U1)?
----------------------------------------------------------------------------------------------------
  J_after + dry/calm/early/sunS      good in? True  bad in? False
  J_after + dry/windy/early/sunS     good in? True  bad in? False
  J_after + wet/calm/late/sunS       good in? True  bad in? False
  J_after + wet/windy/late/sunS      good in? True  bad in? False
  -> four single summers separate them: the early variety in a dry spring (the seed trial and its windy
     twin) and a wet spring with the usual planting (calm or windy); "only the seed trial or the open
     question" is too narrow.

----------------------------------------------------------------------------------------------------
(f) 02 CX4 / 03 s2 third control, with a job read as a QUESTION (03 edit (a)): baseline + pairs
----------------------------------------------------------------------------------------------------
  E1 family sun' x var[V], jobs {j_seen, j_fail} + none                                                    (A) only  |Pres|=1
  E1 family sun' x var[V], jobs {j_seen, j_fail} + none                                                    full (E)  |Pres|=1
  E1 family sun' x var[V], jobs {j_seen, j_fail} + {B0, wet spring}  (no pair contrasts with the baseline) (A) only  |Pres|=1
  E1 family sun' x var[V], jobs {j_seen, j_fail} + {B0, wet spring}  (no pair contrasts with the baseline) full (E)  |Pres|=0
  E1 family sun' x var[V], jobs {j_seen, j_fail} + {B0, shade, wet spring}                                 (A) only  |Pres|=1
  E1 family sun' x var[V], jobs {j_seen, j_fail} + {B0, shade, wet spring}                                 full (E)  |Pres|=1
  -> read as a question, "another wet spring" alone is a job NO member can do (NonCircular needs a
     contrast with the baseline), so adding it is strict (1 -> 0), not file 00's non-strict case.

----------------------------------------------------------------------------------------------------
(g) 02 s2/s7 option (b) marks, with "deleted" read as Part II deletion (port freed) instead of "off"
----------------------------------------------------------------------------------------------------
  E_good   on C_full   consequences (off): 3  -> not marked         consequences (Part II): 7  -> not marked
  E_good   on J_after  consequences (off): 0  -> MARKED             consequences (Part II): 1  -> not marked
  E_bad    on C_full   consequences (off): 3  -> not marked         consequences (Part II): 7  -> not marked
  E_bad    on J_after  consequences (off): 0  -> MARKED             consequences (Part II): 1  -> not marked
  E_patch  on C_full   consequences (off): 0  -> MARKED             consequences (Part II): 7  -> not marked
  E_patch  on J_after  consequences (off): 0  -> MARKED             consequences (Part II): 1  -> not marked
  -> with Part II deletion every added override has a "consequence" at every sunny-south pair of its
     contract (its deletion leaves the answer undetermined there), so (b) marks none of the three.
```

##### `a7_mistake_back.py`

```text
====================================================================================================
A7  THE MISTAKE COMING BACK AFTER A GOOD CORRECTION, FULL (E)
====================================================================================================
family sun' x var[V,W,Wi] with E1's transport: 1024 members
  {j_seen, j_fail}   |Pres|= 64  repeating E0's wrong answer at an unreached pair:  56  e.g. (sun'=id, var=00000001) repeats E0 at dry/calm/early/sunS, dry/windy/early/sunS, wet/calm/early/sunS
  + seed trial       |Pres|= 32  repeating E0's wrong answer at an unreached pair:  24  e.g. (sun'=id, var=00001001) repeats E0 at dry/windy/early/sunS, wet/calm/early/sunS
  open question      |Pres|=  1  repeating E0's wrong answer at an unreached pair:   0  

Not a ratchet: the corrected candidate narrowed back to the summers seen (Emb-2, rule family)
  jobs {j_seen, j_fail}    |Pres|=1  members: (rule: N if early else id(Sun))
  narrowed to {j_seen}     |Pres|=2  members: (rule: N if off else id(Sun)), (rule: N if early else id(Sun))
  -> the version that answers as E0 (rule: N if off ...) is back in Pres once the failed job is dropped.
```
