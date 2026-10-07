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
| W59.1 | **FIX** (substantive) | "Rivals" is defined by "not one account on \(C\)", which (a) makes the good and bad rescue one account, not rivals, on the record question, against refinement (2); (b) makes compatible candidates rivals, so "a conflict between ideas" is false of kind (ii); (c) turns Derivation 2's sufficient condition into a definition that Derivation 2 refuses; plus the defects in 1.2–1.7. Replacement NEW, DECLARATION and rows below; checked on 02's models and by the program. |
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

**Repair adopted in section 3.** Rivalry is conflict at some admitted pair, in \(C\) or outside it. Redescriptions and compatible candidates never conflict, so neither is a rival. Kind (i) is conflict inside \(C\), and kind (ii) is conflict only outside it. This is refinement (1) and refinement (2) in the theory's own terms, and Derivation 2 is used only for its Consequence, which the repair matches exactly ("some admitted change separates them, and must supply it"). r2b checks it on the pairs 02 built for M1–M3, M5 and M6, and m3d on 02's door (section 5):
- The good and bad rescues on the record question become kind (ii), and on the full question kind (i).
- The myth and its southern variant are kind (ii) on both writings.
- A label swap is not a rival: grief against "sorrow", Persephone against Freyr, dog against turtle, the god renamed.
- The mechanism and the rule are not rivals unless the change that sets the variety effect directly is admitted; then they are kind (ii).
- The idle god, the route god and the unfaithful god are not rivals of Tomas's account.
- The spring and the slack cable (02 M3(d)) are not rivals while only pushes are admitted, since both could be faithful at once. They are kind (ii) once holding the spring slack is admitted (m3d). The cable is still refuted inside \(C\) by its own failure, as the kind-(ii) sentence says.
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

Each fix is given as the exact text to put in place of the drafted text in `01 entries.md`, or as a stated deletion. Every field not named is UPHELD as drafted. The fixed NEW texts were spliced into a scratch copy of the list (`attack3a/cl_fixed.md`) together with the W36.1 companion edit (3.6), and the program ran clean on it (section 5).

### 3.1 W34.1 — FIX

- **CHECK, add at the end:** "03a (25 September): UPHELD in substance; GAIN, one REASON sentence and the N4 row corrected. W34.1 as edited, W33.1 as edited, W59.1 and W60.1 stand or fall together under plan 1.5's cap (the group-H unit); if the unit is dropped, W34.1 and W33.1 revert to their text of 24 September."
- **REASON, "Reach goes with the lemma", last sentence, replace with:** "Its one clause that a verdict used, that standing is fixed by the candidate and the world and not by what anyone has checked (N4), is kept in W59.1, stated for questions: whether a candidate is an account of a question is fixed by the candidate, the question and the world, not by when anyone first asks the question or by whether anyone has checked the candidate against it."
- **REASON, "The two gaps found earlier", second sub-bullet, replace "closed in substance" with:** "narrowed, not closed".
- **CASES AT RISK, N4 (O56), second sentence, replace with:** "It stays toward through W59.1's sentence: whether a candidate is an account of a question is fixed by the candidate, the question and the world, not by when anyone first asks the question or by whether anyone has checked the candidate against it."
- **GAIN, replace with:** "Part VI no longer carries a count over a family nobody declares, on jobs nobody defines. 'Job' leaves the theory. The family \(\mathcal V\) stays only as the domain of (D), where no verdict turns on it, and it is still not among Part XIV's declared inputs."

### 3.2 W33.1 — FIX

- **CHECK, add at the end:** "03a (25 September): UPHELD in substance. O2's 'This derives L275 s2's rule.' is struck, as check 2 had ruled; the sentence on W36.1 is corrected. One unit with W34.1 as edited, W59.1 and W60.1 (see W34.1)."
- **CASES AT RISK, the O2 row: delete its last sentence** "This derives L275 s2's rule." (Check 2 struck it as circular, and the block of 23–24 September carries the same slip.)
- **REASON, 25 September bullet, replace the sentence** "W36.1's 'how hard an account is to vary is a separate matter (Part VI)' still lands, on W59.1's 'easy to vary'." **with:** "W36.1's pointer to Part VI now lands on W59.1's 'easy to vary'. Its words 'how hard an account is to vary' ask for a degree that Part VI no longer states, so they become 'whether an account is easy to vary' (the companion edit to W36.1)."

### 3.3 W59.1 — FIX

**NEW** (replaces the drafted NEW; the anchor, the rule and the Part VII heading are unchanged):

````text
**Rivals.** Two explanatory candidates for one question \(p\) are **rivals** when one is offered as an answer to \(p\) in place of the other and they conflict at some admitted edit–boundary pair of the target, in \(C\) or outside it. Two candidates **conflict** at such a pair \((a,b)\) when their answers there differ, or when each of them could meet (F1), (F2) and (A) there under some relations of the target there and no relations of the target there let both, as when two of their active components with one anchor have different relations there. Each rival is offered for the whole of \(p\), and so claims (F1), (F2) and (A) at every pair of \(C\), tested or not, and the rest of (E) on \(C\); outside \(C\) it claims nothing on \(p\), but what its organization and transport give there can conflict with what another's give. Two candidates that differ only in how they are written, one carried onto the other by a structure-preserving bijection, conflict at no pair (Derivation 8), and nor do two candidates, however differently they are cut, that some relations of the target would let both meet (F1), (F2) and (A) at each admitted pair; neither pair is a pair of rivals. A result is **established** for an assessor who holds a usable receipt for it (Part IX); by (K3), a result that tells against a candidate tells against it only together with the background and instruments of the test that yields it. A candidate **fits** what is established for an assessor when no result established for that assessor shows it failing a condition of (E). No list of all rivals is supposed: the rivals of a candidate are those someone has offered in its place, and a candidate that nobody has offered is no one's rival. Nor are rivals a selection population: whether a selected transport is underdetermined at an unseen pair is fixed by its population (Derivation 3), whatever rivals anyone offers.

**Problems.** Two rivals that both fit what is established for an assessor pose, for that assessor, a **problem for \(p\)**: a conflict between ideas that what the assessor has established has not settled. It is of one of two kinds. (i) The rivals conflict at some \((a,b)\in C\). Establishing what the target does there, its relations as well as its answer where their answers there agree, is then a **test** that solves the problem whatever it shows, since afterwards at most one of them fits; an answer it refutes stays refuted on \(p\) (Part VIII). (ii) They conflict at no pair of \(C\), only at admitted pairs outside it: the contract does not contain their conflict. Their answers then agree at every pair of \(C\), so no established answer holds one of them to account without the other; a test inside \(C\) can refute one of them without the other only for a failure of its own; and where both meet (E) on \(C\) both are accounts of \(p\). A candidate is **easy to vary**, in the sense used here, when it and a rival pose a problem of the second kind; the rival is then easy to vary too, and the term says nothing about which of them is right. A criticism that a candidate is easy to vary must supply such a rival (Part IX). Two rivals that are both accounts on \(C\) conflict only outside it, and a claim that one is right and the other wrong is a claim that some admitted change outside \(C\) separates them, and must supply it, as a claim that one assignment of anchors is "really" right must (Derivation 2, Consequence). The remedy is a finer contract that contains such a change, which is a new question (Part III), and on it the problem is of the first kind; whether a candidate is an account of a question is fixed by the candidate, the question and the world, not by when anyone first asks the question or by whether anyone has checked the candidate against it (Parts I and V). Nothing here counts rivals, grades a candidate or ranks candidates. A problem that a system represents can be a recognized difficulty (Part X), as when choosing one of two rivals meets a claimed obligation only by dropping the other, which fits as well, where the protected obligations include keeping every rival that fits (Part XI).

---

# Part VII — Exact constructions
````

**DECLARATION** (replaces the drafted one): Part VI now defines rivals for a question: two candidates, one offered as an answer in place of the other, that conflict at some admitted pair, in the contract or outside it. Two candidates conflict at a pair when their answers there differ, or when each could meet (F1), (F2) and (A) there and no relations of the target there let both. Two candidates that differ only in how they are written, or that some relations of the target would let both meet those conditions at each admitted pair, are not rivals. It defines when a result is established for an assessor (a usable receipt, with (K3)'s caveat) and when a candidate fits what is established. It says that no list of all rivals is supposed, that a candidate nobody has offered is no one's rival, and that rivals are not a selection population, whose underdetermination Derivation 3 fixes. It says that two rivals that both fit pose, for that assessor, a problem for the question. Where they conflict at a pair of the contract, establishing what the target does there, its relations as well as its answer, is a test that solves the problem whatever it shows. Where they conflict only outside the contract, their answers agree on it, no established answer holds one to account without the other, a test inside it refutes one without the other only for a failure of its own, and both are accounts where both meet (E). A candidate is easy to vary when it and a rival pose a problem of that second kind; the rival is then easy to vary too, and the term says nothing about which is right. A criticism that a candidate is easy to vary must supply such a rival. Two rivals that are both accounts conflict only outside the contract, and a claim that one is right must supply an admitted change outside it that separates them; the remedy is a finer contract, a new question on which the problem is of the first kind. Whether a candidate is an account of a question is fixed by the candidate, the question and the world, not by when the question is first asked or whether anyone has checked. Nothing here counts, grades or ranks, and a represented problem can be a recognized difficulty where the protected obligations include keeping every rival that fits.

**CHECK, add at the end:** "03a (25 September): FIX. Rivalry is now conflict at some admitted pair, in the contract or outside it, not 'not one account on C'. The old test was too narrow (02 M1(8), M2), too wide (02 M3(b), M6), and it read Derivation 2's sufficient condition as a definition. Conflict now excludes a candidate that cannot meet the conditions whatever the target does. The kind-(i) test names relations, the kind-(ii) claims are made exact, the assessor is named, the Derivation 3 sentence is added, the 'asked' clause is corrected for non-vacuity, and the obligation in the last sentence is declared. Every pair 02 built was re-run under the new wording ('03a' runs r2b and m2b). The whole list applies with the program. One unit with W34.1 and W33.1 as edited and W60.1."

**REASON, replace the bullets "Why it is stated this way", "What each sentence rests on" and "The owner's example", and the phrase "(Derivation 2)" in "Labels do not make rivals", with:**
- **Why it is stated this way.**
  - *Rivals by conflict.* The owner's "a variation is a competitor", and Deutsch's problem as a conflict between ideas (p.17), both need a conflict. "They differ in what they claim, not only in wording" (refinement (1)) is conflict at some admitted change, in \(C\) or outside it. The drafted test "not one account on \(C\) in the sense of Derivation 2" had three faults:
    - it was too narrow: same-cut candidates that differ only outside \(C\) came out as one account (02 M1(8), M2);
    - it was too wide: compatible cuts and idle additions came out as kind-(ii) rivals (02 M3(b), M6);
    - it read as a definition Derivation 2's sufficient condition, which Derivation 2 refuses ("Without the premise of (ii) nothing more follows", D3:L560; W19.2, LOSS).
  - *Redescriptions.* A structure-preserving bijection preserves (F1), (F2) and (A) pair by pair (Derivation 8). So a candidate and its rewriting conflict nowhere. Two candidates that some relations of the target let both meet the conditions at each admitted pair conflict nowhere either, however they are cut.
  - *Conflict.* The two routes are these. Answers that differ cannot both meet (A), since \(\operatorname{Ans}_p(a,b)\) is one value by (Q). Or each could meet the three conditions and no relations let both, as with two components on one anchor with different relations, which cannot both meet (F1). A candidate that could not meet the conditions at a pair whatever the target does is excluded from the second route: its failure is its own, and it would otherwise conflict with its own relabelling (r2).
  - *Outside \(C\).* A candidate for \(p\) claims nothing outside \(C\) (D3:L43, L159), but its organization and transport give something there. Derivation 2's Consequence already speaks of "some admitted change" that separates candidates the contract does not.
  - *Established and fits* are as drafted, with the assessor named, since a usable receipt is indexed to one (D3:L384).
  - *Not a population.* A differing survivor (Derivation 3) is a member of \(\mathcal T\) whether or not anyone has conjectured it. A rival is offered whether or not \(\mathcal T\) contains it. The sentence keeps O48 and D3-T from being read through rivals.
- **What each sentence rests on.**
  - *Kind (i).* At a pair of \(C\) where they conflict, once the target's relations there (or, where the answers differ, its answer) are established, not both meet (F1), (F2) and (A) there, so at most one fits. "An answer it refutes stays refuted on \(p\)": W60.1.
  - *Kind (ii).* At each pair of \(C\) there is no conflict, so the answers agree. Equal answers stand or fall together under (A). A relation test there refutes one of them without the other only for a failure of its own: either that one could not meet the conditions there whatever the target does, or the actual relations do not satisfy it while other relations would have satisfied both. Where both meet (E) on \(C\) both are accounts: (E) itself.
  - *Both accounts.* If both are accounts on \(C\), both meet the three conditions at every pair of \(C\) under the actual relations, so they conflict at no pair of \(C\). Their rivalry lies outside \(C\), and a claim that one is right must supply that change (Derivation 2, Consequence). A finer contract containing it makes the conflict one inside the new contract, which is kind (i).
  - *Not by when the question is asked.* (E) uses neither \(O_p\) nor \(\rho_p\), and nothing in it is dated. Non-vacuity's stated scope belongs to the question whenever the question is asked (03a §1.5). This is W34.1's reach clause, kept and stated for questions.
  - *The recognized difficulty.* The last sentence is an instance of W35.3's second clause, with the obligation declared (D3:L435, L516).
- **The owner's example.** "Demeter grieves" and "Persephone is underground" (as the cause, with no grief) give one answer at every pair of the Greek question.
  - Where a change that sets the mediating state on its own is admitted, they conflict there: one sets her grief, and the other has nothing to set. So they are rivals of kind (ii) (03a, m2b: 12 conflicting pairs, none in the Greek contract).
  - Where no such change is admitted, they conflict nowhere and are not rivals. Their difference is then idle, as is the difference between Persephone and Freyr (Deutsch p.21).
  - Tied to nothing in the target, a god's component can meet (F1) nowhere, and its story fails by its own construction.
- **Labels do not make rivals**: replace "are one account in Derivation 2's sense, not rivals" with "conflict at no admitted change (Derivation 8), so they are not rivals".

**CASES AT RISK** (replaces the drafted list):
- **O24 (the unused joint setting): toward.** The two arrangements conflict at the joint setting.
  - The setting is reachable by hand, so it is physically admitted. By non-vacuity it is in \(C\) unless a stated scope excludes it. Then the problem is kind (i), and "One reachable setting is enough" is the test that solves it.
  - If a stated scope excludes the setting, the problem is kind (ii), and the finer question makes it kind (i).
  - Read as selection, the case rests on Derivation 3 (W19.2, W17.3), which the new sentence keeps apart.
- **O36: toward on the reason; no mark moves.** "A candidate that nobody has offered is no one's rival" is O36's "a fact about a candidate nobody has written". P's criticality rests on (B) and D3:L299.
- **O45: holds.** No candidate is offered in place of the two-spring account. A one-spring candidate offered in its place would conflict with it where the first spring is deleted: a test there if that deletion is in \(C\).
- **O46: holds.** The cable account anchors a different subnetwork. Offered in the spring account's place, it is a rival, not the spring account continued. Its success is its own (D3:L307).
- **O48: holds; the watch is lifted.** A conjectured arrangement with the forbidden wire is at most a rival. It is not a member of the population, and the text now says that rivals do not make a population (Derivation 3). If the devices are established to lack the wire, the arrangement does not fit.
- **D3-T (O76): holds.** The discarded design failed a tried setting, so it does not fit. "No such pair exists" is Derivation 3's fact about the population, which the new sentence keeps a conjectured design from overturning.
- **N1 (O53): holds; toward on the reason.** An idle sun god conflicts with Tomas's account at no admitted pair, so it is not a rival even if someone offers the struck version in its place (03a r2b). The same holds on the route reading. On the unfaithful reading it is not a rival either: the answers are the same, and its failure is its own, which is W33.1's interference.
- **N2 (O54): holds (No); toward on the reason, on either writing of the myth.** Before the sailor's report, the southern variant conflicts with the myth only at the southern pairs, which lie outside the Greek question: kind (ii) (r2b; 02 M2's writing-dependence is gone). The report is a pair of the world question, where the two conflict: kind (i) there. The "No" rests on (E).
- **N3 (O55): holds on both questions.** "Its details … could be swapped" is kind (ii) only for swaps that change what the myth gives at some admitted change, as the southern variant does. Swapping which gods, or what bargain, conflicts nowhere, so it gives no rival (r2b: grief against "sorrow", Persephone against Freyr). Watched: a reader may take "no rival" for name swaps as calling the myth hard to vary. The "No" rests on non-circular dependence and the "only in form" on W36.1.
- **N4 (O56): Q1 toward** through the corrected sentence (not by when the question is first asked). Q2 unchanged.
- **N5 (O57): toward.** The two readings conflict at the southern change, outside the home question: kind (ii) at home. The finer question makes it kind (i), and a trial in the south solves it. This agrees with W17.2's Derivation-3 reading, in which both readings are population members that survive the home history, because the two are kept apart.
- **N7 (O59): holds; the watch is narrowed.** Compatible accounts are not rivals, even if offered in place of each other. Watched only if Maya's candidate gives something outside her range that conflicts with Bea's there.
- **N17 (O67):** no pull. Answers A and B conflict nowhere.
- **N24 (O74): holds.** Different queries make different questions.
- **N25 (O75): Q1 holds; Q2 toward.** Dog and turtle conflict at no admitted change, on either anchoring (r2b). "The difference between them is idle".
- **Others.** O1: its second half stays SILENT; for its first half see W60.1. O27: holds; "the one test that would separate them" is a kind-(i) test, and the robot's move is (K3)'s caveat. O2, O8 and O47 hold.

**GAIN** (replaces): The theory says what hard-to-vary comes to without a count, a family or a grade.
- Two candidates are rivals when they conflict somewhere.
- An easily varied candidate has a rival that fits as well and conflicts with it only where the question does not reach.
- The remedy is a finer question, on which a test solves the problem, and the criticism is the rival.
- Kind (i) states the crucial test, O24's case, directly.
- Redescriptions, compatible accounts and idle additions are not rivals.

**LOSS** (replaces):
- Two paragraphs, about 740 words, and six defined terms.
- "Easy to vary" is symmetric and relative to what an assessor has established. It gives no ground for preferring either rival, and on the Greeks' question it applies to the tilt as much as to the myth.
- A candidate nobody has challenged with a rival is not called easy to vary, however loose it is (refinement (3)).
- Variants that conflict at no admitted change, such as two myths that differ only in their gods, are not rivals at all, though Deutsch calls them incompatible (p.21).
- A candidate with a kind-(ii) rival is still an account of its question if it meets (E). Deutsch would say it explains nothing (sources note).
- Whether two candidates conflict outside \(C\) depends on what their transports translate there. A candidate whose transport translates nothing outside \(C\) has no kind-(ii) rival.

### 3.4 W60.1 — FIX

**NEW** (replaces the drafted NEW; the anchor sentence is unchanged):

````text
A new index is a new claim.

**A failed answer stays failed.** Fix a question \(p\), a pair \((a,b)\in C\) and a value \(y\neq\operatorname{Ans}_p(a,b)\). By (A), a candidate for \(p\) whose answer at \((a,b)\) is \(y\), \(\operatorname{Ans}_E(\tau(a),\sigma(b))=y\), is not an account of \(p\), whether it is the candidate that gave \(y\) there and failed, that candidate offered again, a rival, or a changed candidate that keeps \(y\) there; and the same holds on every question with the same target and query whose contract contains \((a,b)\). Once it is established for an assessor that the target's answer at \((a,b)\) is not \(y\), this is established for that assessor of every such candidate alike, from the candidate's own answer there, with no record of which candidates failed before or of how any was changed. Here "established" is meant as in Part VI: the assessor holds a usable receipt for the target's answer at \((a,b)\) (Part IX), and by (K3) the test that yields it tells against a candidate only together with the background and instruments it relies on. If a premise about them ceases to be live, the receipt is not usable and the exclusion ceases to be established, for every such candidate alike; no candidate is thereby shown to be an account (K2). A contract that omits \((a,b)\) makes a different question (Part III): an account on it does not answer \(p\), and the failure on \(p\) stands (Historical index).
````

**DECLARATION** (replaces): Part VIII now states that on a question, a candidate whose answer at a pair of the contract differs from the target's is not an account of it, nor of any question with the same target and query whose contract contains that pair, whatever candidate it is. Once the target's answer there is established for an assessor, by a usable receipt, this is established for that assessor of every such candidate alike, from its own answer there, with no record of earlier failures or changes. By (K3) the exclusion is established only together with the background and instruments of the test; if a premise about them ceases to be live, it ceases to be established for every such candidate alike, without any candidate being shown to be an account. A contract omitting the pair makes a different question, an account on which does not answer the original, whose failure stands.

**CHECK, add at the end:** "03a (25 September): true under its hypotheses, including (K3)'s caveat. Three phrases made exact: the assessor is named; 'alike' is 'from the candidate's own answer there'; what lapses under (K3) is the establishing, not the fact (K2). The D3-T row is corrected. One unit with W34.1 and W33.1 as edited and W59.1: its 'established' is Part VI's."

**REASON:**
- **"The hypotheses, stated in the text", add two sub-bullets:** "'Established' is for one assessor. 'Alike' means from each candidate's own answer, derived from its organization, over the same leaf." and "What lapses under (K3) is the establishing, not the fact: 'Withdrawing a premise removes a license; it does not make the conclusion false' (D3:L387); 'The binding is by the world's answer, not by the recorded observation' (correction-sticks analysis, Appendix A (b))."
- **"The place", replace its last sentence with:** "Part XV's list is left unchanged. The first sentence follows from (A) and (Q) by definition, and the rest from Part IX's receipts, (K2) and (K3), so the paragraph adds no result open to a counterexample of its own."

**CASES AT RISK, replace the D3-T row with:** "**D3-T (O76): holds; not moved.** The discarded design fails at a tried setting, which the case already says. Its reason, 'No such pair exists', is about the population (Derivation 3), which this entry does not reach."

**GAIN** (replaces): "The theory says in one paragraph why a correction sticks on its question with no record of which candidates failed or how any was changed. It needs only a usable receipt of the target's answer at the pair, which is a record of the world, not of the candidates. It says what 'established' requires, and why blaming the test exempts no candidate."

### 3.5 W38.1 — FIX

**NEW: the four lines below replace the drafted *Explanation*, *Idle parts*, *Hard to vary* and *Reach* lines.** *Surprise and problems* stays as drafted, and is now exact ("narrower"). The *Explanation* line takes the new phrase only with the W36.1 companion edit (3.6); without that edit it keeps "how hard an account is to vary". The block "W38.1: the lines of NEW that change" in 01 is regenerated from these.

````text
- *Explanation.* Deutsch counts a false myth as an explanation (chapter 1, p.19). Here that is an explanatory candidate (Part V). Part I's fallibility commitment uses "explanation" for an account on a contract, and whether an account is easy to vary is a separate matter (Part VI).
- *Idle parts.* Deutsch counts superfluous features as a defect of an explanation (chapter 1, p.25). Here (E) has no condition that each commitment do work: a commitment that does no work by itself is critical in no support, and nothing in the semantics grades a candidate for carrying one (Parts 0, VI and XIV).
- *Hard to vary.* Deutsch calls an explanation good or bad as it is hard or easy to vary while still accounting for what it purports to account for (chapter 1, p.31), and a myth easy to vary because its details could be changed without changing its predictions, and so changed to make other predictions when they were needed (pp.20–22). Here hard-to-vary is stated through rivals and problems, with no measure or count of variants (Part VI). Two rivals that both fit what is established pose a problem, a conflict between ideas in his sense (p.17); a pair of the question's contract at which they conflict is a test that solves it, as an experiment decides between two viable theories whose predictions conflict (p.16); and a candidate is easy to vary when it has a rival that fits as well and conflicts with it only outside what the question covers, as his variant of the myth in which Demeter sends the warmth south agrees with the myth on every season the Greeks knew (p.21). Four departures remain. He judges ease of variation before any variant is offered, and would reject a bad explanation without any experiment (p.25); here it is shown only by offering the rival, which is the criticism. He holds that an explanation able to fit anything in its field explains nothing (p.22); here a candidate with such a rival is an account of its question when it meets (E), and the remedy is a finer question. Here being easy to vary is symmetric between two rivals and prefers neither: offered in place of each other on the question of the seasons the Greeks knew, the tilt of the Earth's axis, which he calls hard to vary (p.24), and the myth are rivals of this kind, each easy to vary relative to the other. And variants that conflict at no admitted change, such as the Persephone and Freyr myths, which he finds radically incompatible yet reducible to one core explanation (p.21), are here not rivals at all (Part VI).
- *Reach.* Deutsch's reach is the power of an explanation to solve problems beyond those it was made for (chapter 1, p.28), and an explanation already applies, when it is first thought of, where its creators never looked (p.29). Here the word is not defined, and nothing is measured by how many questions a candidate answers; whether a candidate is an account of a question is fixed by the candidate, the question and the world, not by when anyone first asks the question or by whether anyone has checked the candidate against it (Parts I and VI).
````

**CHECK, add to the 25 September bullet:** "03a: the *Hard to vary* line follows W59.1's fix and records a fourth departure (symmetry: the tilt against the myth). *Reach* follows the corrected sentence and cites p.29. *Explanation* reads 'whether an account is easy to vary', with W36.1's companion edit. The *Idle parts* pointer is 'Parts 0, VI and XIV'. The fallback table is recut to the group-H unit."

**REASON, "25 September: hard to vary", replace with:** "**25 September: hard to vary.** The owner's position of 24–25 September states hard-to-vary through rivals and problems (W59.1), and this note says so. The pages used are Deutsch:
- p.16, on experiment between two viable theories;
- p.17, on problems as conflicts;
- pp.20–22: on p.21 the southern variant, and the Persephone and Freyr myths, 'radically incompatible' yet with 'the same core explanation'; on p.22 an explanation that could explain anything;
- p.24, the tilt as 'hard to vary';
- p.25, rejection without experiment;
- p.29: an explanation already applies where its creators never looked;
- p.31, the glossary.

Each page was checked by page marker in the extracted text. No book is quoted: the lines paraphrase. Four departures are recorded: judgement before a rival is offered; the name of explanation kept for an account with an easy rival; symmetry, which makes the tilt easy to vary relative to the myth on the Greeks' question; and variants that conflict at no admitted change, which are not rivals. The *Surprise and problems* line changes 'is' to 'can be' for the wider sense, since Part VI now says a represented problem for a question 'can be' a recognized difficulty. 'Is' would contradict it, and 'narrower' is exact because every problem for a question is a conflict."

**LOSS, replace "about 720 words" with** "about 1,150 words" (the note as spliced: 1,120 words to the line before its last sentence).

**FALLBACKS, replace the table with:**

| line | rests on | fallback |
|---|---|---|
| Inexplicit representation (parallels) | C W41.1 | drop the sentence |
| Part I's substrate independence (parallels) | C W45.1 | (as drafted) |
| Explanation | C W36.1, and its companion edit for "whether an account is easy to vary" | (as drafted) if W36.1 is dropped; if only the companion edit is not made, the line keeps "how hard an account is to vary is a separate matter (Part VI)" |
| Idle parts | C W33.1 (the words 'does no work by itself'); the claim itself holds on file 11 and Parts 0 and XIV | (as drafted) |
| Hard to vary, Reach, Surprise and problems (its sentence on a problem for a question), Idle parts | the group-H unit: W34.1 and W33.1 as edited, W59.1, W60.1 | if the unit is dropped: no *Hard to vary* line, and the lines *Idle parts*, *Reach* and *Surprise and problems* revert to their text of 24 September (the "Old lines" above) |
| Stated limits | B1 W57.1 + W32(b).1 | (as drafted) |
| Selection | A W37.1 for 'Parts 0 and'; the claim holds on file 11's Part IV | (as drafted) |
| Surprise and problems | C W35.1–W35.3 | (as drafted) |
| Elimination | C W40.1 | drop the sentence |

The drafted rows "Hard to vary | H W59.1", "Reach | H W59.1", "Reach, if W34.1 as edited is dropped | C W34.1" and "Surprise and problems, if W59.1 is dropped | H W59.1" go. The third was wrong: with W34.1 dropped and W33.1 as edited kept, "reach" does not occur at all.

### 3.6 Companion edits outside the five entries

- **W36.1 (required).** Change NEW and DECLARATION from "how hard an account is to vary is a separate matter (Part VI)" to "whether an account is easy to vary is a separate matter (Part VI)". In its REASON, replace "and W33.1 says that measure grades nothing" with "and Part VI states no degree of variation (W59.1)". In its CHECK, replace "(L313)" with "(W59.1)". KIND stays CLAIM. The counts do not change, and the list applies with the edit (section 5).
- **The dependence order (recommended).** The file-11 sentence "(S), (B), (D) depend on (E)." is still free (W7.5). It would become: "(S), (B), (D) depend on (E); rivals and the problems they pose (Part VI) on (F1), (F2), (A), (E), histories and receipts." 01 §8 proposed "Derivation 2" in place of "(F1), (F2), (A)". Under the fix, Derivation 2 is no longer used.
- **The frame (the orchestrator's).**
  - The "What the checks changed" row for W33.1 still says "a separate matter, shown by Pres".
  - "Findings carried forward" and P2(d) move N4's watch from W34.1 to W59.1's corrected sentence.
  - W35.3's REASON ("The word 'problem' is not defined") is dated.
  - 01 §2 decision 3 and §3's table rows D3:L69 and D3:L335 should follow 1.1, 2.7 and 3.6.

---

## 4. Case movements under the fixed entries

| case | 01's drafted entries | after the 03a fixes |
|---|---|---|
| O1 | first half toward on the reason (W60.1); SILENT kept | same |
| O24 | toward, on the non sequitur "reachable, so in \(C\)" | toward: kind (i) when the setting is in \(C\) (non-vacuity), kind (ii) then (i) on the finer question when it is excluded |
| O27 | holds | holds |
| O36 | toward on the reason | same |
| O45, O46, O47, O2, O8 | hold | hold |
| O48 | holds; watched (rival read as survivor) | holds; the watch is lifted by the Derivation 3 sentence |
| D3-T (O76) | "moves toward on its reason" (W59.1 and W60.1) | holds; not moved; the Derivation 3 sentence guards Ivo's reading |
| N1 (O53) | holds only while nobody offers the struck version; if someone does, kind (ii) and each "easy to vary" (**risk away**, 02 M6) | holds; toward on the reason: no rival on any reading |
| N2 (O54) | toward on one writing, fails on the other (02 M2) | toward on both writings |
| N3 (O55) | row misstates ("its details … is a rival of kind (ii)") | holds; name swaps give no rival; watched, reading only |
| N4 (O56) | Q1 toward, through a clause that collides with non-vacuity | Q1 toward, through the corrected clause |
| N5 (O57) | toward | toward, and consistent with W17.2's Derivation 3 reading |
| N7 (O59) | holds only while nobody offers the two in place of each other; watched | holds; the watch is narrowed to Maya's candidate outside her range |
| N17 (O67) | if the two are offered in place of each other, kind (ii) and each "easy to vary" (no mark) | no pull |
| N24 (O74) | holds | holds |
| N25 (O75) | Q2 toward (one account) | Q2 toward (no conflict anywhere, on either anchoring) |

**Away:** none predicted under the fixed entries. The one reading risk is N3's watch. Under the drafted entries N1 carried a risk away.

---

## 5. Runs and files

All in `rivals/attack3a/`, on Python 3.11 with the standard library. 02's engine and models are imported and left unchanged.

| file | what | md5 |
|---|---|---|
| `r2test.py` → `r2_output.txt` | rivals as conflict at some admitted pair, with the draft's conflict and with degenerate conflicts excluded, on M1–M3, M5 and M6 | 9b06a3e38329b3d8997bf63af7ebc24b → 63a0b1e0d6763782396ad4b847fc3465 |
| (inline) → `r2b_output.txt` | the same with conflict exactly as the fixed text words it (answers differ, or each could and none lets both); it begins with r2's printout | f064b3cc135b63ed22c335a5cec5b1ae |
| `m3d_door.py` → `m3d_output.txt` | 02's door: spring against slack cable, with and without holding the spring slack admitted | 1d318c8dee058b8b952ae17090c5af55 → 4f612e87638f2a4e72e5235c81560074 |
| `m2b_mediator.py` → `m2b_output.txt` | the owner's example with a change that sets the mediating state admitted, and without it | e8b75ad3f4172c78263015be38284a01 → f9c860cf4715fa33d0e1f092b87fd419 |
| `fixed_W59.txt`, `fixed_W60.txt`, `fixed_W38_lines.txt` | the fixed texts, byte for byte as in section 3 | ec603238c3a0a69a467922f4f305b99a, 57dac0bb180f1b935055d4c21aad618d, 46dd641d6091bc0e27b3f76fc41707e8 |
| `splice_fixed.py` → `cl_fixed.md` | a copy of `rivals/cl_spliced.md` with the fixed W59.1, W60.1 and W38.1 lines and the W36.1 companion edit | ab78a04dfbe0dcfc4a9ba7fe0806918a → 703529a768a40f0dd05d6b9c19c5a553 |
| `tool_output.txt`, `fixed_theory.md` | the program on `cl_fixed.md`, with `--self-test` | 9e18cd9501abeb1f7af0e0b3842b84b8, 3cdf924c1a2969a73b922150ca440a21 |

**r2b, the fixed wording, verbatim:**

```text
B-definition, as the fixed W59.1 words it: conflict at x iff answers differ, or (each could meet and none lets both)
####################################################################################################
  M1 E_good vs E_bad, p (C_full)                       rivals; PROBLEM kind (i): 8 pairs of C, 0 outside
  M1 E_good vs E_bad, p_rec                            rivals; PROBLEM kind (ii): 0 pairs of C, 8 outside
  M1 E_bad vs E_windy, p_rec                           rivals; PROBLEM kind (ii): 0 pairs of C, 8 outside
  M1 E_good vs E0, p                                   rivals; NO problem: E0 does not fit
  M3a renamed                                          not rivals: no conflict at any admitted pair
  M3b mechanism vs rule, override not admitted         not rivals: no conflict at any admitted pair
  M3b mechanism vs rule, override admitted             rivals; PROBLEM kind (ii): 0 pairs of C, 8 outside
  M3c same answers, one anchor, different relations    rivals; PROBLEM kind (i): 4 pairs of C, 0 outside
  M2 dem vs und                                        not rivals: no conflict at any admitted pair
  M2 und vs freyr                                      not rivals: no conflict at any admitted pair
  M2 dem vs sorrow                                     not rivals: no conflict at any admitted pair
  M2 tilt vs dem (Greek question)                      rivals; PROBLEM kind (ii): 0 pairs of C, 4 outside
  M2 dem vs south (N2)                                 rivals; PROBLEM kind (ii): 0 pairs of C, 2 outside
  M2 dem_p vs south (N2, other writing)                rivals; PROBLEM kind (ii): 0 pairs of C, 2 outside
  M2 dem[R-none] vs und[R-none]                        not rivals: no conflict at any admitted pair
  M2 tilt vs dem[R-none]                               rivals; PROBLEM kind (ii): 0 pairs of C, 4 outside
  M5 dog vs turtle                                     not rivals: no conflict at any admitted pair
  M5 dog[R-none] vs turtle[R-none]                     not rivals: no conflict at any admitted pair
  M5 dog vs self                                       not rivals: no conflict at any admitted pair
  M6 Tomas vs +god idle                                not rivals: no conflict at any admitted pair
  M6 Tomas vs +god route                               not rivals: no conflict at any admitted pair
  M6 Tomas vs +god unfaithful                          not rivals: no conflict at any admitted pair
  M6 god idle vs zeus idle                             not rivals: no conflict at any admitted pair
```

**m2b, verbatim:**

```text
dem+ Account on Greek C: True | und: True
fits Greek-era answers: dem+ True und True
conflict pairs: 12, of which in the Greek contract: 0; e.g. [{'place': 'N', 'half': 'H1', 'ins': 0}, {'place': 'N', 'half': 'H1', 'ins': -1}, {'place': 'N', 'half': 'H2', 'ins': 1}]
VERDICT: rivals, kind (ii)
without the mediating change admitted: conflict pairs 0 -> not rivals
```

**m3d, verbatim:**

```text
Account: spring True cable False | fit answers: True True
  only pushes admitted                     conflict pairs 0 (in C 0) -> not rivals (compatible: both could be faithful at once)
  also "hold the spring slack" admitted    conflict pairs 1 (in C 0) -> rivals, kind (ii)
```

**The program on the fixed list, verbatim:**

```text
file 11: md5 5e494c1095d920d128b9a79de378f923 (as required)
entries parsed: 65 (applied 60, of which theory 57 and meta 3; record-only 5; held 0)
theory entries by expected ruling: CLAIM 51, ORDER 2, WORDING 4
every OLD, locator and anchor occurs once in file 11; no applied OLDs overlap; no held anchor is touched
note: N = 51 of M = 57 changes; layer 2: K = 42 places
result is file 11 with exactly the listed replacements (walk check); 55 diff hunks, each inside an entry
cut of the three meta blocks gives back the theory text; no withheld word in it; no slot left
self-test: an unlisted edit was refused
self-test: an edit inside a new text was refused
self-test: the clean draft passed
written: <scratch>/attack3a/fixed_full.md
md5: 1217fc2345fbf47f41c9f005cbffd764
words: 29046 (theory text alone: 12471)
lines: 1840
```

`diff` of the fixed theory text against 01's theory text (`rivals/new_theory.md`) shows four changed lines: D3:L69 (the W36.1 companion edit), the "Rivals" and "Problems" paragraphs, and "A failed answer stays failed". Nothing else differs. Greps of the fixed theory text find no "Pres", no "job" and no "Hard-to-vary". It has 12,443 words by `wc -w`.
