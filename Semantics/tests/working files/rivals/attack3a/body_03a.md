# Rivals and problems: the drafted entries attacked from the text

**Working file, 25 September 2026. Not frozen.** It attacks the five entries drafted in `rivals/01 entries.md` (W34.1, W33.1, W59.1, W60.1, W38.1) from the text of draft 3 and file 11, using the model results in `rivals/02 models.md`, and gives a verdict and, where needed, the exact correction for each.

*Written by a subagent for the orchestrator.*
- **Read:** `01 entries.md` and `02 models.md` in full; draft 3's theory text in full; file 11 at L7–L9, L25–L27, L151–L163, L313–L319, L363–L367 and L516–L520; the change list's frame and the entries W36.1, W35.3, W19.2 and W17.2 (N5 row); the S81 case book (O1, O2, O8, O24, O27, O36, O45–O48); the N-case book (N1–N7, N24, N25); D3-T `final.md`; both analyses of 24 September at the passages the entries quote; Deutsch chapter 1 in the extracted text, pp.16–31 by page marker.
- **Run:** three short scripts in `rivals/attack3a/` on 02's engine and models (section 5), and the apply program on a scratch copy of the list with the fixes spliced in.
- **Not done:** the repository was read only (`git status` clean). Nothing was written into `authority/`, and the Pinker folder was not opened.
- **References.** "L" alone is file 11; "D3:L" is draft 3's theory text; "01:L" and "02" are the two working files; "r2", "r2b" and "m2b" are this file's runs (section 5).

---

## 0. Verdicts

| entry | verdict | in one line |
|---|---|---|
| W34.1 | **FIX** (small) | Sound; its GAIN overclaims (\(\mathcal V\) stays, unlisted, in (D)); its N4 row must follow W59.1's corrected sentence; it must be declared one unit with W33.1, W59.1 and W60.1. |
| W33.1 | **FIX** (small) | Sound NEW and DECLARATION; strike O2's "This derives L275 s2's rule." (its own CHECK struck it); W36.1's "how hard an account is to vary" does not "still land" and needs a companion edit. |
| W59.1 | **FIX** (substantive) | "Rivals" is defined by "not one account on \(C\)", which (a) makes the good and bad rescue one account, not rivals, on the record question, against refinement (2); (b) makes compatible candidates rivals, so "a conflict between ideas" is false of kind (ii); (c) turns Derivation 2's sufficient condition into a definition that Derivation 2 refuses; plus five smaller defects. Replacement NEW, DECLARATION and rows below; checked on 02's models and by the program. |
| W60.1 | **FIX** (small) | True under its hypotheses, including (K3)'s caveat, once three phrases are made exact (an assessor; the candidate's own answer; the exclusion ceases to be *established*, it is not refuted, K2); its D3-T row overclaims. |
| W38.1 | **FIX** | The *Hard to vary* line must follow W59.1's fix and record a fourth departure (the relation is symmetric: on the Greeks' question the tilt is easy to vary relative to the myth); *Reach* follows the corrected sentence; *Explanation* keeps a dangling "how hard"; two fallback rows are wrong; the word count is stale. |

No entry is dropped. Section 3 gives each fix in full, section 4 the case movements, section 5 the runs.

---

## 1. W59.1: what is wrong with "Rivals" and "Problems", point by point

### 1.1 Derivation 2 (revised): the rival test borrows a relation Derivation 2 refuses to define

- The draft says rivals "are not one account on \(C\) in the sense of Derivation 2 (paired active components with one anchor and one kind on \(C\), and one answer profile)".
- Derivation 2 (D3:L556) gives only a **sufficient** condition, and only for candidates that "both satisfy (F1), (F2) and (A) on \(C\)". It then says: "Without the premise of (ii) nothing more follows" (D3:L560). W19.2's LOSS says: "Whether two differently decomposed candidates are one account is left undefined."
- W59.1 turns the premise of (ii) into an *if and only if*, applies it to candidates outside its premise (rivals need only *fit what is established*), and concludes "not one account" wherever the premise fails. That is a new claim in Derivation 2's territory, undeclared, and against its own "nothing more follows".
- The borrowed relation also gives wrong verdicts, both ways:
  - **Too narrow.** Kinds are judged on \(C\) (K), so two candidates cut alike that differ only outside \(C\) are "one account on \(C\)" and so not rivals. 02 proves this in general (02 §3, mismatch 1, a lemma) and computes it: on the record-only question the good rescue ("early variety") and the bad one ("wet spring") are one account (02 M1(8); r2 prints "draft: one account on C_rec? True"). That is the central example of the correction-sticks analysis, and refinement (2)'s paradigm of kind (ii). The draft's N2 row then holds on one writing of the myth and fails on the other (02 M2).
  - **Too wide.** Any two candidates cut differently are "not one account", however compatible. A mechanism and a rule that are both faithful at every admitted change (02 M3(b)), a fuller and a leaner account, and Tomas with and without an idle sun god (02 M6) become rivals the moment one is offered in the other's place, pose a "problem" of kind (ii), and are each "easy to vary". Yet they conflict nowhere, so the text's own glosses, "a conflict between ideas" and "the contract does not contain their conflict", are false of them. The owner's "a variation is a competitor", and Deutsch's problem as conflicting ideas (p.17), both need a conflict.
- It also sits badly with Part 0 (D3:L11: "Two components no admitted change can separate are one kind at that level") and Part XV (C) (D3:L534). Two candidates that anchor different but indistinguishable subnetworks, or cut one mechanism differently, and are never separated by any admitted change, would pose a "problem": a distinction no admitted change supports, doing work.

**Repair adopted in section 3.** Rivalry is conflict at some admitted pair, in \(C\) or outside it. Redescriptions and compatible candidates never conflict, so neither is a rival. Kind (i) is conflict inside \(C\), and kind (ii) is conflict only outside it. This is refinement (1) and refinement (2) in the theory's own terms, and Derivation 2 is used only for its Consequence, which the repair matches exactly ("some admitted change separates them, and must supply it"). r2b checks it on every pair 02 built (section 5):
- The good and bad rescues on the record question become kind (ii), and on the full question kind (i).
- The myth and its southern variant are kind (ii) on both writings.
- A label swap is not a rival: grief against "sorrow", Persephone against Freyr, dog against turtle, the god renamed.
- The mechanism and the rule are not rivals unless the change that sets the variety effect directly is admitted; then they are kind (ii).
- The idle god, the route god and the unfaithful god are not rivals of Tomas's account.
- The tilt against the myth is kind (ii) on the Greek question.
- The owner's example is kind (ii) exactly when a change that sets the mediating state on its own is admitted. That is the REASON's own gloss ("A change that set the mediating state on its own would lie outside that contract"; m2b: 12 conflicting pairs, none in the Greek contract). With no such change admitted, the two stories conflict nowhere, and their difference is idle, as Persephone's and Freyr's is (Deutsch p.21).

### 1.2 "Conflict": a candidate that can never be faithful conflicts with its own copy

- The draft's definition: two candidates conflict at \((a,b)\) "when, whatever the target's relations there, not both meet (F1), (F2) and (A) there". A candidate with a component anchored to no part of the target fails (F1) at every pair, whatever the target, so it "conflicts" with every candidate everywhere, including with its own relabelling (r2: dog[R-none] against turtle[R-none], "degenerate allowed", kind (i)).
- Under the draft's rival test this was masked, since such pairs were "one account". Under any rival test that uses conflict it is fatal.
- The corrected definition keeps the draft's two named routes and drops the degenerate case. Two candidates conflict when their answers there differ, or when each could meet (F1), (F2) and (A) there and no relations of the target let both. This is 02's option (b), now run (r2b).
- With it every claim about the kinds is true (proofs in 3.3's REASON). The one claim that fails, "no test the question admits is sure to solve the problem", is false where one rival cannot meet the conditions at a pair of \(C\) whatever the target does. It is replaced by what is true: a test inside \(C\) refutes one rival without the other only for a failure of its own.

### 1.3 The kind-(i) test must establish relations, not only answers

"Establishing what the target does there" solves the problem "whatever it shows" only if the target's **relations** there are established where the two answers agree. With the answer alone, 11 of 64 outcomes leave both rescues fitting at the shaded-wall pairs (02 M1(4); M3(c)). Fixed: "its relations as well as its answer where their answers there agree".

### 1.4 Derivation 3, D3-T and O48: a rival is not a differing survivor

- Derivation 3's "differing survivor" is a member of a selection population, "a transport the physics and the stated construction admit" (D3:L566, L475), whether or not anyone has conjectured it. A rival is a candidate someone has offered, whether or not the population contains it. Kind (i) and the differing survivor have the same shape (both fit what the history or the record holds, and both differ at an unseen pair), so a reader can take the one for the other.
- **O48**: a conjectured arrangement with the forbidden wire would then "keep the unseen setting open", against "there is no alternative in that population".
- **D3-T**: Ivo's conjectured design would do the same. And the reverse error sits in 01's own D3-T row: "none exists", said of a kind-(i) problem, is a fact about offers, whereas the case's "No such pair exists" is a fact about the population.
- **N5** is carried by both routes. W17.2 reads the rule's two readings as population members that both survive the home history, and W59.1 reads them as rivals once someone puts them forward. The two agree only because they are kept apart.
- Fixed: one sentence in "Rivals": "Nor are rivals a selection population: whether a selected transport is underdetermined at an unseen pair is fixed by its population (Derivation 3), whatever rivals anyone offers."

### 1.5 Non-vacuity, and N4: "whether or not anyone has asked the question"

- Non-vacuity requires that every excluded physically admitted edit be "excluded by a stated scope, not silently" (D3:L257; D3:L159: "a stated scope is what makes it one"). A scope is stated when a question is posed. So "whether a candidate is an account of a question is fixed by the candidate and the world, whether or not anyone has asked the question", read literally, contradicts (E) for every question with a proper contract that nobody asks.
- W34.1's clause, which this replaces, said "not by which jobs anyone has checked". N4 needs no more than this: the question is asked later, and the idea already accounted for it (Deutsch p.29: "when its creators first thought of it, it already applied in our planet's other hemisphere").
- Fixed: "fixed by the candidate, the question and the world, not by when anyone first asks the question or by whether anyone has checked the candidate against it (Parts I and V)".

### 1.6 Declared inputs and Repair: "keeping such a rival is protected"

The draft asserts that keeping a rival that fits "is protected (Part XI)". The obligations \(O\) and \(P\) are declared inputs (D3:L435, L516), which the semantics records and does not supply. Fixed: "where the protected obligations include keeping every rival that fits (Part XI)". The sentence stays an instance of W35.3's second clause, and "can be" stays.

### 1.7 Smaller defects

- **"Claims the conditions of (E) at every pair of \(C\)".** Non-circular dependence and non-vacuity are not conditions at a pair. Fixed: "claims (F1), (F2) and (A) at every pair of \(C\), tested or not, and the rest of (E) on \(C\)".
- **"Offered" and "conjectured".** The rival test says "each is offered … in place of the other", and the last sentence says "those someone has conjectured". The two words disagree, and "each … in place of the other" asks the first-offered candidate to have been offered in place of one not yet made. Fixed: "one is offered … in place of the other", and "those someone has offered in its place".
- **"Established" names no assessor.** A usable receipt is indexed to one (\(\operatorname{Usable}_j\), D3:L384), but "fits what is established" and "problem for \(p\)" name none. Fixed: "established for an assessor", "fits … for an assessor", "pose, for that assessor, a problem for \(p\)".
- **Symmetry is only in the REASON.** A reader of the text alone can take "easy to vary" as a defect of one side. That is the draft's own risk on N7, and it arises on the tilt as well (below). Fixed in the text: "the rival is then easy to vary too, and the term says nothing about which of them is right".
- **"A criticism … supplies such a rival".** As a statement of fact it is false of criticisms that fail to. Fixed: "must supply such a rival (Part IX)", in parallel with Derivation 2's "must supply it".
- **"The remedy is a finer contract".** It follows "Where both rivals are accounts on \(C\)", and 02 M3(d) shows that it can be misread as the remedy for kind (ii) in general. Under the fix, two rivals that are both accounts on \(C\) conflict only outside it, so the scope is exact. The sentence now also says what the finer contract does: on it, the problem is of the first kind.

### 1.8 The REASON of W59.1: three invalid steps

1. "On the Greek question they give one answer at every pair, so they conflict at no pair of \(C\)" (01:L216). The converse holds; 02 M3(c) is a counterexample (one answer everywhere, conflict through (F1) at four pairs). Under the fix, the owner's example is kind (ii) because the stories conflict at the mediating change outside the Greek contract and at no pair inside it (m2b).
2. The O24 row: "reachable by hand and so a pair of \(C\)". Reachability makes the setting physically admitted, not a member of \(C\). By non-vacuity it is in \(C\) unless a stated scope excludes it.
3. "(E) uses neither \(O_p\) nor \(\rho_p\) … whether or not anyone has asked": non-vacuity uses a stated scope (1.5).

### 1.9 What the draft got right, and the fix keeps

It keeps:
- no list of rivals, and no count or grade;
- the two kinds, and kind (ii)'s "the contract does not contain their conflict", now true;
- "where both meet (E) on \(C\) both are accounts";
- the link to Derivation 2's Consequence and to the recognized difficulty;
- the definitions of "established" and "fits" through receipts and (K3);
- the anchor (L317–L319), the id, the KIND and the REASON WORD.

---

## 2. The other checks

### 2.1 Derivation 7 (question identity), Derivations 8–10, Part V

- **Derivation 7.**
  - No collision. "Problem for \(p\)" is indexed to \(p\) and to what an assessor has established, not an assessment verdict.
  - W60.1's narrowing clause is D3:L151 and L159. It holds whether or not the narrowing is recorded, since identity is by \((C,\mathcal Q)\). An unrecorded one is Derivation 7's goalpost-moving, a failure of the record.
- **Derivation 8.** It is the right warrant that a redescription conflicts nowhere: a structure-preserving bijection preserves (F1), (F2) and (A) pair by pair. Derivation 2 is not, since its "one account" can still conflict outside \(C\) (the rescues).
- **Derivation 9.** Kind (ii)'s "no established answer holds one of them to account without the other" is Derivation 9's point, and a relation test inside \(C\) can still refute one of them. The fixed wording says exactly this.
- **Derivation 10.** \(t_1\) and its swap conflict at no admitted pair on a contract that treats both things alike. They are not rivals, under the draft and under the fix.
- **Part V.** (E) is untouched. See 1.5 for non-vacuity, and 1.7 for "the conditions of (E) at every pair".

### 2.2 Part VI: supports, critical blocks, W33.1's idleness test

- W33.1's three kept sentences are exact and independent of Pres, as its REASON says. The addition half and the removal half follow from the stated test.
- Under the draft, an idle commitment makes a rival (02 M6). Under the fix it does not: the idle god conflicts nowhere (r2b), so 02's proposed repair (setting idle commitments aside before comparing) is not needed.
- A commitment idle on \(C\) that says something different outside \(C\) does make a rival, of kind (ii). That is correct, since it then claims something different.
- A candidate with a critical block deleted conflicts with the full one where the contrast is lost. It is a rival of kind (i), which a test settles. That is sensible.

### 2.3 W34's reach

- W34.1 as edited removes reach, correctly. The noun "reach" occurs nowhere in the new text; D3:L151, L245, L331, L397, L556 and L624 were checked, and all are verbs or "reachability".
- N4's clause now lives in W59.1, corrected (1.5).

### 2.4 The recognized difficulty (W35), Repair, criticism (Part IX)

- W59.1's last sentence is an instance of W35.3's second clause once the obligation is declared (1.6).
- The sources note's change from "is" to "can be" is right. A problem in Deutsch's sense (conflicting ideas) need not involve claimed and protected obligations. Check 2's fix (c) is not undone, since the line still gives Deutsch's p.17 definition.
- W35.3's REASON ("The word 'problem' is not defined in the theory") is dated, as 01 §8 says. Its text and declaration are unaffected.
- Part IX: "must supply" (1.7). (K1) bears on an easy-to-vary criticism exactly when its connection is an account of \(p_\delta\), whose answer turns on the supplied rival.

### 2.5 Part XIV's declared inputs; "no merit function / grades nothing" (D3:L25, F11:L27, D3:L516)

- The new terms rest on four things:
  - histories ("offered");
  - receipts ("established", Part IX);
  - (F1), (F2) and (A) ("conflict");
  - a quantifier over the target's relations at one pair ("under some relations of the target there").
- The last is the same kind of quantifier as Derivation 3's proof ("another admitted relation") and is equally undeclared. No verdict in 02's models or in r2 and r2b turns on "all" against "functional" (02 M1(3)). Carried forward; no text change.
- The obligations in the recognized-difficulty example are now marked as declared (1.6).
- (D)'s "declared family \(\mathcal V\)" is still not in Part XIV's list, so W34.1's GAIN must not say it left.
- "Easy to vary" is a relation to one offered rival. It is symmetric (now said in the text), counts nothing, and ranks nothing. None of D3:L25, F11:L27 or D3:L516 is touched.

### 2.6 Part XV

- No entry needs Part XV changed. W60.1 adds no result open to a counterexample: its first sentence is (A) and (Q) by definition. The REASON's phrase "a counterexample to (A)" is odd, since (A) is a condition and not a result, and is reworded.
- Under the draft, W59.1 edged toward Part XV (C) (1.1). Under the fix, every rival pair is separated by an admitted change.
- The Derivation 3 sentence keeps rivals out of attack (D)'s first limb.

### 2.7 Dangling pointers to Pres, "job", or a degree of variation

- **Theory text after the fix:** no Pres, no "job", no "Hard-to-vary" (grep of `attack3a/fixed_theory.md`).
- **D3:L69 (W36.1):** "how hard an account is to vary is a separate matter (Part VI)". Part VI no longer states a degree, so "how hard" dangles. Companion edit to W36.1: "whether an account is easy to vary". W36.1's REASON ("W33.1 says that measure grades nothing") and its CHECK ("(L313) … exact") are dated with it.
- **W38.1's *Explanation* line:** the same phrase; fixed with it.
- **W38.1's fallback row "Reach, if W34.1 as edited is dropped":** it says "used once, for the jobs an account is held to". If W34.1 is dropped and W33.1 as edited stays, the word "reach" does not occur at all. If both are dropped, it occurs once, in a comment on the containment. Replaced by a unit rule (3.5).
- **The frame's "What the checks changed" table** still says W33.1 reads "a separate matter, shown by Pres". **"Findings carried forward"** and **P2(d)** still name W34.1 for reach. These are the orchestrator's.
- **Part VII (D3:L335), "a rival account would need"** is counterfactual and reads as "an account that, offered, would be a rival". 01's table says it "uses 'rival' in the new sense", which is not quite so, but it needs no change.

### 2.8 Is "correction sticks" true under its stated hypotheses?

**Yes**, with three phrases made exact.
- **The fact.** Fix \(p\), \((a,b)\in C\) and \(y\neq\operatorname{Ans}_p(a,b)\). Any candidate whose answer there is \(y\) fails (A) on \(p\). For \(p'\) with the same \(D\) and \(\mathcal Q\) and \((a,b)\in C'\), \(\operatorname{Ans}_{p'}(a,b)=\mathcal Q(D,a,b)=\operatorname{Ans}_p(a,b)\) by (Q), since the baseline does not enter. So it fails there too. No history enters.
- **Its being established.** The receipt is for a claim about the target, not about any candidate. Against a given candidate, the receipt is that receipt plus the derivation of the candidate's own answer from its organization, the same leaf for all. So it is established "alike", *from each candidate's own answer*. The draft omits this, and without it "established of every such candidate" overstates what an assessor holds about a candidate whose answer nobody has derived.
- **(K3)'s caveat.** What lapses when the background or the instruments are doubted is the *establishing*, through (K2)'s liveness of premises. The fact does not lapse: "withdrawing a premise … does not make the conclusion false" (D3:L387), and "the binding is by the world's answer, not by the recorded observation" (correction-sticks analysis, Appendix A (b)). The draft's "the exclusion does too [come into question]" blurs the two. Fixed.
- **The narrowing clause.** It is D3:L151, L159 and L363.
- **Limits, all respected.** Other pairs, runs of saves, grain changes, and the claim, as distinct from the account, of the old answer (analysis §1(1), "It is not a ratchet" (2)).
- **"Without any record".** It means no record of candidates' failures or changes. The receipt of the target's answer is itself a record of the world, which the text requires, and the REASON and GAIN should say so.

### 2.9 KINDs and DECLARATIONs

| entry | KIND | REASON WORD | DECLARATION |
|---|---|---|---|
| W34.1 | CLAIM, right | change of claim, right | right as drafted |
| W33.1 | CLAIM, right | change of claim, right (a file-11 sentence is withdrawn) | right as drafted |
| W59.1 | CLAIM, right | change of claim, right | must follow the fixed NEW (3.3) |
| W60.1 | CLAIM, right | clarification, right: derivable from (A), (Q), (K2), (K3) and D3:L151/L159, as with W35.3 | must follow the fixed NEW (3.4) |
| W38.1 | META, right | meta | "made by the note", right |

---

## 3. The fixes in full
