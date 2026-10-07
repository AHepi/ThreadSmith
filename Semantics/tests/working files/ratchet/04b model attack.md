# 04b Model attack: counterexamples to the correction lemma (03), and a check of the 02 models

*Working file, 24 September 2026. Nothing in the repository was changed. The Pinker folder was not opened. Scripts and outputs: `ratchet/attack/` (Python 3.11, standard library, all eight run in under 10 seconds). `fe.py` is a new finite implementation of Account (E) with Part II's solution semantics: organizations as ports and component relations, Sol as the intersection (O), deletion as the full relation, the transport map π, and (A), (F1), (F2) and NonCircular. `pl.py` is an independent pair-level engine (Account = (A)), written without importing `ratchet/models`. Re-read for this: 03 in full; 02 in full; `models/*.py` and their outputs; D3 Part II (L81–105), Part V (L229–283), Part VI (L285–313), L159, L363, L510–532; F00 L162, L270–300, L352–386; EC section 2 and option (b).*

**Tags.** [COMPUTED] exact output of a script on a stated finite model. [PROVED] a short general argument. [F] follows from quoted lines. [T] a line says it. [I] my inference.

**How the attack was run.** Each claim was taken at its word. I then looked for a finite model where the stated hypotheses hold and the conclusion fails. Where the models of 02/03 read a term one way (a job is one pair; Account is (A) alone; a deleted part is switched off), I also ran the theory's own reading of that term (a job is a question whose contract holds the baseline; Account is (E); a deleted component imposes the full relation, D3:L101). Where 03 says "one interpretation" (03:L64), each member of a family keeps the later explanation's transport, as file 00 requires: "Each pair retains its edited components, background, and interpretation" (F00:L294).

---

## 0. Bottom line

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

## 1. Verdicts, claim by claim

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

## 2. The counterexamples

### CE1. The witness is lost under (E) with one interpretation (A1). Attacks rows 1–3, 27, 32, 33.

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

### CE2. One correction, two embeddings, opposite answers (A1). Attacks rows 1, 14, 18.

Emb-1 and Emb-2 hold the same final candidate. It has the same answers at all 16 pairs and is an account on the open question in both. On F = {j_seen, j_eshade} under full (E):
- Emb-1: 1 → 1, not strict;
- Emb-2: 2 → 1, strict.

Whether "the failed job excluded the old explanation" is therefore a fact about how the correction is written down. Blocking: as CE1.

### CE3. The narrowing clause without the identity edit (A2). Attacks rows 7, 8, 23.

**Hypotheses hold.** E0 is an account on j_seen and not on j_fail.

**Conclusion fails** under both readings:

```text
  V1 = the other three sun maps (every edit changes something) full (E)  |Pres(F)|=0  |Pres(F+f*)|=0  strictly larger after the narrowing? False
  V2 = edits that add the variety part, any sun map          full (E)  |Pres(F)|=1  |Pres(F+f*)|=1  strictly larger after the narrowing? False
  V1 + identity                                              full (E)  |Pres(F)|=1  |Pres(F+f*)|=0  strictly larger after the narrowing? True
```

D3:L301 says only "a declared family V of organization edits". Nothing puts the identity in it.

**Blocking:** "the identity edit is a member of V".

### CE4. An added block cannot rescue a mistake (A3(a)). Attacks row 5.

[PROVED] By (O), Sol is an intersection over components. So Sol(E0 + B) ⊆ Sol(E0) at every pair, and Ans(E0 + B) ⊆ Ans(E0) for the query "which bed first". If E0's answer at f\* is determined and wrong, E0 + B answers the same or answers nothing.

[COMPUTED] E0 + B answered north at f\* for 0 of 256 relations on (V, Sun, first), 0 of 65,536 on (V, Sun, ovr, first), and 0 of 3,000 random relations on all six ports. The subset property held at all 16 pairs for the 256.

So every rescue of a *mistake* changes a component, and "Where E1 only adds a block B, E0 = E1|(Γ1\B)" covers only failures by silence. A3(c) gives one: E0′ leaves the answer open for a changed planting, and there var is critical at f\*, with E1′|(Γ1\B) equal to E0′ exactly.

**Blocking:** add "and E0's answer at f\* is undetermined", or declare the restriction operation.

### CE5. Criticality depends on the restriction operation (A3(b)). Attacks row 6.

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

### CE6. Limit (iii): the separating job need not be (A) (A5(1)). Attacks row 11.

The two members var = [V = early] and var = [V = early ∧ Sun = S] answer identically at all 16 pairs, and both are right at all 16. j_eshade separates them: the second fails (F2) and (F1) at the shaded early-variety year, since its mechanism claims "no variety effect" there. (A) holds for both.

**Blocking:** "that is (E) on that job".

### CE7. "Never harder to vary on the old jobs" turns on the declared families (A4(i)). Attacks rows 21, 26, 34.

```text
  pair A  E0: sun reads Sun (4 maps)             |Pres(J_before)|=  1   E1: sun reads Sun x var[V]     |Pres(J_before)|=  2  -> E1 EASIER to vary
  pair B  E0: sun reads Sun, W (16 maps)         |Pres(J_before)|=  4   E1: sun reads Sun x var[V]     |Pres(J_before)|=  2  -> E1 HARDER to vary
  pair C  E0: sun reads Sun, W, Wi (256 maps)    |Pres(J_before)|= 64   E1: sun fixed (id) x var[V]    |Pres(J_before)|=  2  -> E1 HARDER to vary
  every one of the six families holds a member answering exactly as E0 at all 16 pairs: True
```

"Every extension is at least as easy to vary" holds exactly when E0's own family is placed inside E1's (pair A). That is Vers(E0) ⊆ Vers(E1), a fact about the embedding, not about the correction. So 03 §4's argument that "a correction must be harder to vary" refuses the good rescue depends on the families. Under pairs B and C, the good rescue passes it.

**Blocking:** limit (ii)'s own condition, written into the sentence.

### CE8. "No choice of menus flips it" / "always met, by the lemma" (A4(iv), A1). Attacks rows 14, 27.

```text
  sun[4] x var[V]  (holds v0 = var off)                                  |Pres(J_before)|=2  |Pres(J_after)|=1  strict? True
  rule "north first if the variety is P", P in {early, late} (no v0)     |Pres(J_before)|=1  |Pres(J_after)|=1  strict? False
```

Both families hold the corrected candidate. Together with CE1, strictness flips with the menu under (A) and with the port structure under (E). As a condition of (E), "adding the failed job must shrink Pres" would refuse the neighbour's rescue in one listing and pass it in another.

**Blocking:** hypothesis (iv) plus CE1's hypothesis. Under both, the claim is true and does nothing, which is 03's point.

### CE9. A bad rescue registers as harder to vary, under file 00's own premise (A4(ii)). Against the owner's (2); supports 03.

In E0's own family with sun reading Sun and W (fixed organization, interpretation and family), the wet-spring rescue *is a member*:
- sun maps dry/sunS→S, dry/shadeS→N, wet/sunS→N, and wet/shadeS either way.
- Adding the failed summer takes Pres from 4 to 2.

By the measure, the bad rescue shows as a shrink, the same as any job added under (H). No organization change is needed, so no embedding question arises.

### CE10. "Disjoint … never nested" is a menu artifact (A4(iii)). Attacks row 25.

Take U_B = sun[Sun, W] × var[V], with Vers(E0) = var off. Then |Pres_E0(J_before)| = 4 and |Pres_E1(J_after)| = 6, with an overlap of 2. With 02's menu the overlap is 0.

**Blocking:** "E0's own family has no member that does f\*".

### CE11. m3's check (1) tests the encoding (A6c). Row 38.

"okmask of v0 (sun=id, all added parts off) == pairs E0 gets right: True". Every instance was therefore guaranteed. The lemma's content is that equality, and CE1 is where it fails.

### CE12. "A job nothing fails" (A6a, A6f). Attacks rows 17, 35.

```text
  m3 as run: F = J_after     E0 does F? False E0 does the added job? True  |Pres| 1 -> 1  strict? False
  clean: F = J_before        E0 does F? True  E0 does the added job? True  |Pres| 2 -> 2  strict? False
  E1 family sun' x var[V], jobs {j_seen, j_fail} + {B0, wet spring}  (no pair contrasts with the baseline) full (E)  |Pres|=0
  E1 family sun' x var[V], jobs {j_seen, j_fail} + {B0, shade, wet spring}                                 full (E)  |Pres|=1
```

NonCircular needs a pair whose answer differs from the baseline's (D3:L255). A question whose contract has no such pair is one no candidate can account on.

**Blocking:** a job must hold a contrast.

### CE13. More jobs separate the rescues than 03 says (A6e). Attacks row 20.

Any of the following, added to J_after, keeps the good rescue and drops the wet-spring rescue:
- dry/calm/early/sunS;
- dry/windy/early/sunS;
- wet/calm/late/sunS;
- wet/windy/late/sunS.

The windy twin of the seed trial also drops the patch.

### CE14. Symmetry rows that compare a family with itself (A6b). Attacks row 22.

"good reads V+W, bad reads W+V: same set of override predicates? True". The same holds for V+W+Wi against W+V+Wi. The "good" family var[V+W+Wi] contains the rain rescue, so CX3's "good:V+W+Wi 64:1 good easier" (02:L600) sets a family holding both rescues against one holding only the bad one.

### CE15. Option (b)'s marks depend on reading "deleted" as "switched off" (A6g). Attacks row 36.

```text
  E_good   on J_after  consequences (off): 0  -> MARKED             consequences (Part II): 1  -> not marked
  E_bad    on J_after  consequences (off): 0  -> MARKED             consequences (Part II): 1  -> not marked
  E_patch  on C_full   consequences (off): 0  -> MARKED             consequences (Part II): 7  -> not marked
```

(b)'s draft says "its answer there is not kept when that component is deleted" (EC, option (b)). With Part II deletion, the answer is "not kept" (it becomes undetermined) at every pair where the part could fire, so the do-nothing patch has 7 consequences.

**Blocking:** (b) must say "set to the earlier value" instead of "deleted". This is the same repair CE5 needs. It also bears on 02 §7's comparison of (b) with Pres.

---

## 3. Errors found in the 02 models

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

## 4. What the proposal needs if it goes ahead [I]

- **(H\*)**: take the witness hypothesis as "v0 ∈ V is an account on every job of F, under the family's interpretation, and not on f\*". Add, as the sufficient condition, "v0 removes B together with the ports only B assigns, and the transport is restricted accordingly". Drop "It holds for every declared V that has the member v0". The conclusion is then (H) with a named witness, which is true and short.
- **§1(3)**: "Met, not relaxed" becomes "met when the earlier candidate, with its transport restricted, is a member". For a correction that posits a new variable, that takes a family of candidate edits. The owner's worry about file 00 returns at exactly that point.
- **Narrowing clause and pointer (c)**: add "when the identity edit is in V".
- **Companion**: either restrict it to failures by silence, or name the restriction operation (switch-off). Either way, drop 03:L25's "a rescuing addition is critical at the failed job" as a mark of rescue.
- **Limit (iii)**: "(E) on that job".
- **§4**: bullet 1 needs limit (ii)'s condition. Bullet 2 is false as stated (CE8). Bullet 3 stands, with the symmetric pairs 1:1, 4:4 and 6:6.
- **§2 point 4**: delete "no choice of menus flips it".
- **The hypothesis list**: replace the third control with the clean one, using a job that holds a contrast.

The overall verdicts of 03 (point (1) PARTLY, (2) NO, (3) PARTLY; no case verdict moves) stand. The ground for (3) gets narrower.

## 5. What stays uncertain

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

## Appendix: script outputs, verbatim

### `a0_crosscheck.py`

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

### `a1_witness_under_full_E.py`

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

### `a2_narrowing_without_identity.py`

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

### `a3_companion.py`

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

### `a4_family_choice.py`

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

### `a5_limit_iii_and_symmetry.py`

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

### `a6_model_checks.py`

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

### `a7_mistake_back.py`

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
