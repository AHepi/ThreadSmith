# 05 Checked result: does a correction stick? The hard-to-vary lemma and its limit

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

## 0. What changed after the attacks

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

## 1. Answers to the owner's three points

### (1) "A correction adds the failed case to the jobs, so any version that brings the mistake back fails." PARTLY.

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

### (2) "A bad rescue registers as easier to vary — more versions fit — by the same measure that defines a good explanation." NO.

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

### (3) "Can the file-00 limit be relaxed for comparing an explanation with its own correction, without ranking different people's explanations?" NO.

- **File 00's reasons are structural.** [T, F] There is no common set; "It says nothing by itself about two different theories using different interpretations or different variation families" (F00:L379). Counts change with redescription: "splitting one feature into ten cannot create knowledge" (F00:L381). The interpretation is held fixed (F00:L358, L1300). None of these mentions authorship, so each applies to one's own correction.
- **The checked lemma does not relax the limit and does not make the comparison.** [F] It compares two sets of jobs inside one declared family, in which one member may carry E0's verdicts. That meets file 00's premise. It is not a comparison of E0 with the correction (04a 3b).
- **The witness itself depends on the writing, which is file 00's redescription worry coming back.** [COMPUTED] The same correction has a witness when written as a changed rule (2 → 1). Written as a mechanism under one interpretation, it has none (1 → 1) (CE1, CE2; R1, R2). One way to restore the witness there is a family that holds E0 with its own transport (R4: 2 → 1). Whether a family of "organization edits" may do that is open (section 5).
- **Between separately declared families there is no comparison to be had.** [COMPUTED] Easier or harder flips with the menus (A4(i)).
- **"Own" does no formal work.** [F] The hypotheses are structural, so a rival's correction written the same way gets the same result. What makes a correction someone's own is history: provenance is told "by their histories, not their outputs" (D3:L13; F11:L15). A comparison confined to one's own corrections therefore presupposes the record the owner wants to drop.

---

## 2. The checked wording

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

## 3. The three test situations and the named cases

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

## 4. Gains and losses

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

## 5. What remains uncertain

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

## 6. Plain words

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

## 7. Output of `check/r1_repaired_wording.py`, verbatim

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
