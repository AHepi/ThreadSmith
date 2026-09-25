# Rivals and problems: the drafted entries attacked with counterexamples

**Working file, 25 September 2026. Not frozen.** It attacks the five entries drafted in `rivals/01 entries.md` (W34.1, W33.1, W59.1, W60.1, W38.1) with counterexamples run on finite models, and checks `rivals/02 models.md` for errors.

*Written by a subagent for the orchestrator.*
- **Read:** `01 entries.md` and `02 models.md` in full; the new theory text the entries produce (`rivals/new_theory.md`, Parts II–IX and Derivations 1–10); the engine and the six model scripts of `rivals/models/`; draft 3's theory text by grep (Pres); the correction-sticks analysis by grep (the counts W34.1 cites, "windy spring"); the error-correction analysis by grep (the Pres-grade sentence); Deutsch chapter 1 in the extracted text, pp.14–31.
- **Not done:** the repository was read only. Nothing was written into `authority/`, and the Pinker folder was not opened. The S81 and N case books and D3-T were not reread; case verdicts are taken from 01's and 02's rows, which quote them.
- **Scripts:** `rivals/attack/` (Python 3.11, standard library, about four minutes in all). They import 02's `models/engine.py` unchanged, through `attack/ext.py`. Every output is inlined verbatim in the appendix.
- **References.** "01:L" means `01 entries.md`; "02" means `02 models.md`; "A1" to "A12" are the attack scripts below. [COMPUTED] marks a script output, [PROVED] a short general argument given here, [I] an inference of mine.
- **The repair tested throughout** is called "the 03b repair". It changes only the rivals clause (section 2).

---

## 0. The verdicts in brief

The draft's definitions of conflict, the two kinds, "established" and W60.1 hold. **The rivals clause does not.** Its test, "not one account on \(C\) in the sense of Derivation 2", fails in both directions:
- Two candidates can be "one account" by the test and still conflict at every pair of \(C\) (A3 (a)).
- A redescription, a duplicate, a coarsening or an idle addition counts as a rival, and so poses a "problem" that is no conflict at all and that no finer contract can remedy (A3 (b)–(e), A9 M6).

Two claims that rest on the clause fail with it: "a conflict between ideas" and "the remedy is a finer contract". One tested repair fixes every case the models raise but one, and that one is recorded as a limit (section 2). The other defects are wording or scope.

| # | Claim | Verdict | Evidence | Minimal fix (section 4) |
|---|---|---|---|---|
| 1 | W59.1: rivals are candidates that are "not one account on \(C\)" by Derivation 2's relation (01:L177) | **REFUTED** | A3 (a): "one account", yet they conflict at 16 of 16 pairs. A1 (3), A9 (M1, p_rec), A11: same-cut rivals differing outside \(C\) are "one account". A3 (b)–(e), A9 M6: redescriptions, duplicates, coarsenings and an idle god are rivals of kind (ii) | FIX-1: rivals each claim something the other does not, at admitted changes in \(C\) or outside it |
| 2 | "each is offered … in place of the other" (tense), and nothing said of narrowing | **FIX** | A5: if "offered" means currently offered, withdrawing both and narrowing makes the problem for \(p\) vanish with nothing established | FIX-5: "has been offered", plus one sentence on narrowing |
| 3 | "Each is offered for the whole of \(p\) … at every pair of \(C\), tested or not" | UPHELD | A1: the unperformable pairs are claimed and classify the problem | — |
| 4 | Conflict: "whatever the target's relations there" | **FIX** | A8: both rivals meet the conditions at a pair only if a conservation law is broken; the draft says kind (ii), and with the physics it is kind (i) | FIX-2: "whatever relations the adopted physics admits for the target there" |
| 5 | Conflict: "as when their answers there differ, or two … components with one anchor have different relations" | UPHELD | Examples, not a definition (02, "also noted") | — |
| 6 | Established: a usable receipt, with (K3)'s caveat | UPHELD | A1 (2): a receipt derived from a rival itself is barred, and a derivation from an independent law works until the law is withdrawn. A7 | — |
| 7 | Fits; a problem for \(p\) | **FIX** (clarity) | A7: the same pair is a problem for an assessor who has dropped a background premise and not for one who holds it | FIX-6: "for an assessor" in "fits" and "problem" |
| 8 | No list of rivals is supposed; nothing counts, grades or ranks | UPHELD | A4: an infinite family. Every verdict is pairwise, and one exhibited rival suffices | — |
| 9 | A problem for \(p\) is "a conflict between ideas" | **REFUTED** under the draft; holds under FIX-1 but for a recorded residual | A3 (b), (d), (e1): both are accounts, and they are compatible or identical in claim. A3 (f): the residual | FIX-1; record the residual (section 2) |
| 10 | Kind (i): "Establishing what the target does there is then a test that solves the problem whatever it shows" | UPHELD conditionally | A1: true if anyone can establish it. 02's mismatch 3: relations, not only answers | FIX-3: add "at most one of them is an account of \(p\), whether or not anyone can establish it", and "its relations and not only its answer" |
| 11 | Kind (i): "an answer it refutes stays refuted on \(p\)" | UPHELD | A6, A7; 02 M1 (6) | — |
| 12 | Kind (ii): the answers agree; no established answer separates them; no test is sure to solve it; both are accounts where both meet (E) | UPHELD | [PROVED] in 01:L205–L210; A3; A8 (true only by counting outcomes the physics forbids, until FIX-2) | — |
| 13 | "Easy to vary" is defined, and the criticism supplies the rival | UPHELD as a definition; LOSS understated | A11: on any question narrower than the admitted changes, a same-cut patch outside \(C\) (Deutsch's own p.27 variant) makes any candidate easy to vary, the tilt included | FIX-11: LOSS and sources note |
| 14 | "a claim that one is right … must supply" a separating admitted change | UPHELD | A3 (b): none exists, so no such claim can be made | — |
| 15 | "The remedy is a finer contract, which is a new question" | **REFUTED** as stated | A3 (b): no admitted change separates the two, so no finer contract exists. A3 (f): a finer contract refutes both. 02 M3 (d): a test of relations inside \(C\) suffices | FIX-4 |
| 16 | "whether a candidate is an account … is fixed by the candidate and the world" | UPHELD | — | — |
| 17 | The recognized-difficulty sentence | **FIX** (wording) | "keeping such a rival is protected" reads as an assertion, but protected obligations are declared inputs (Part XI) | FIX-7 |
| 18 | REASON, the owner's example (01:L216) | **FIX** | 02's mismatch 2 (the step is invalid). A9: under FIX-1 the pair is a rival pair only through an admitted change to the warmth received | FIX-8 |
| 19 | REASON: label swaps are not rivals, "This agrees with Deutsch's own reduction … (p.21)" (01:L217) | **FIX** | Deutsch p.21 also says the two myths "assert radically incompatible things" | FIX-9 |
| 20 | Case rows N2, N3, N7, N1 | **FIX** (N3); the others hold, better under FIX-1 | A9: under FIX-1, N2 is kind (ii) on both writings, N7's watch dissolves, and the idle god is no rival even if offered | FIX-10 |
| 21 | W60.1, first sentence: every candidate giving the refuted answer at the pair fails, on every question with the same target and query holding the pair | UPHELD | 02 M1 (6); A6 (1)–(3) | — |
| 22 | W60.1: established of every such candidate alike, with no record | UPHELD | A7: 67 of 67 revived alike when the premise is dropped, and no other candidate moves | — |
| 23 | W60.1, the (K3) clause: the exclusion reopens alike | UPHELD | A7 | — |
| 24 | W60.1, last sentence (a narrowed contract is a different question) | **FIX** (minor) | A6 (4): the same holds for a changed query, which W60.1 does not name | FIX-12 |
| 25 | W60.1, LOSS: nothing beyond the failed pair | UPHELD | A6 (1): the same mistake at an untested neighbour stays undetected, as recorded | — |
| 26 | W34.1: Pres is trivial and unused; after the change there is no Pres, no "job" and no "Hard-to-vary"; the cited counts | UPHELD | grep: 0, 0, 0; the counts are at the analysis's L190 and L2623 | — |
| 27 | W33.1: the no-work test | **FIX** (minor) | A3 (a): in a candidate with no support, every commitment "does no work by itself" vacuously (E0's only component) | FIX-13 |
| 28 | W38.1: "a pair of the question's contract at which they conflict is a test" | **FIX** | A pair is not a test | FIX-14a |
| 29 | W38.1: p.22 paraphrase "able to fit anything" | **FIX** | Deutsch: "could easily explain anything" | FIX-14b |
| 30 | W38.1: third departure (variants reduce to one core) | **FIX** | It omits "radically incompatible" (p.21) | FIX-14c |
| 31 | W38.1: the departures recorded | **FIX** (add one, under FIX-1) | A11: the p.27 variant makes the tilt easy to vary on the Greek question; Deutsch says the variant is "no longer an explanation" (p.28) | FIX-14d |
| 32 | W38.1: pages 16, 17, 20–22, 25, 31 | UPHELD | Checked in the extracted text (section 3) | — |
| 33 | 02: the scripts and the appendix | UPHELD | Re-run: all six outputs byte for byte; the appendix is verbatim | — |
| 34 | 02: mismatches 1–7 | UPHELD (confirmed) | Re-run; A9; A12 | — |
| 35 | 02: repair 1 ("one account" judged on every admitted pair) | **INSUFFICIENT** | A3 (a)–(e1) | Use FIX-1 |
| 36 | 02: repair 4 (set aside idle commitments first) | **INSUFFICIENT** | A3 (d): a duplicate is a redundant route by W33.1's test and is not set aside. A3 (a): vacuous where there is no support | Use FIX-1 |
| 37 | 02 §4: "no verdict in these models changed with the space" | UPHELD for its models; does not generalize | A10 (M3 (d) is the same in both spaces); A8 | FIX-2 |
| 38 | 02 M5: "self" glossed as "the universe holds itself up; nothing holds it" | **ERROR** in the model's gloss | Its component is anchored to the holder subnetwork: it is a coarsening of the dog story, and FIX-1 finds it claims nothing the dog story does not (A9) | Re-gloss, or anchor "self" so that it denies the holder |
| 39 | 02 M1 table: "Owner … ('windy spring would fit as well')" | **ERROR** (attribution) | The words are the correction-sticks analysis's (its L22, L264) | Attribute to the analysis |
| 40 | 02 option (b), not run there | Its two claims UPHELD | A12 | — |

---

## 1. The counterexamples

### 1.1 Rivals that conflict only at an admitted change nobody can perform (A1)

**Set-up.** A planet's seasons. Setting the tilt to 0 is physically admitted, but no one can perform it and no history contains it. R1 ("tilt") and R2 ("eccentricity") have the same cut and the same anchors, and differ only at tilt 0.

**On \(p_{dep}\)** (the contract holds tilt 0):
- The draft gives kind (i), and so does the 03b repair [COMPUTED].
- "A test there solves it whatever it shows" is true, but only if what the target does at tilt 0 is established.
- A receipt derived from either rival is barred, as "reconstructed from the claim it is meant to support" (Part IX).
- A derivation from an independent law U (Deutsch p.24: surfaces tilted away from the heat are warmed less, testable apart from the seasons) solves the problem. If U is withdrawn, the problem comes back as kind (i) (K3) [COMPUTED].

**Should it be kind (i)? Yes.**
- Whatever the world does at tilt 0, at most one of R1 and R2 is an account of \(p_{dep}\) [COMPUTED, and PROVED from the definition of conflict].
- That realist fact, not the availability of a test, is what separates kind (i) from kind (ii). The owner's parenthesis "(a test there solves it)" assumes a test can be run.
- The draft never states the fact itself; FIX-3 adds it.

**On \(p_{here}\)** (tilt 1 only):
- The draft finds R1 and R2 "one account", so not rivals.
- The 03b repair finds them rivals of kind (ii) [COMPUTED].
- This is 02's mismatch 1 again: rivals that differ only outside \(C\) are lost when they are cut alike.

### 1.2 Rivals that differ only outside the question (A1 (3), A9 M1 and M2, A11)

The draft loses every same-cut pair that differs only outside \(C\) [COMPUTED]:
- the gardener's wet and windy rescues on the record question;
- the myth written with a place port against its southern variant (N2);
- the tilt against its tilt-1 patch;
- the tilt against Deutsch's own Aristarchus variant, "tilt here, in phase elsewhere" (p.27).

The 03b repair makes each of these a kind-(ii) rival pair.

**The price, which the owner's refinement (2) accepts.** "Easy to vary" is then available against any candidate on any contract that omits an admitted change at which the candidate claims something: patch one component's relation there (Derivation 3's proof). So on the Greek question the tilt is easy to vary once anyone offers the p.27 variant (A11). Deutsch says that variant "is no longer an explanation of seasons, just a (purported) rule of thumb" (p.28). This is a departure, and FIX-14d records it.

### 1.3 Pairs that look different but claim the same, and pairs that look alike but differ (A3)

**(a) Alike, but they differ.** Two candidates have the same active components, anchors, kinds and answers. One background component (outside Γ) differs: soil moisture follows the wet spring, or the dry one.
- The draft calls them one account, so not rivals. 02's repair 1 says the same.
- They conflict at all 16 pairs, through (F2), which reads the whole organization [COMPUTED].
- A test of relations at any pair refutes one of them. A test of answers never can.
- The parenthesis is Derivation 2's conclusion for candidates that both *meet* (F1), (F2) and (A). The draft applies it to candidates that need not, and there it no longer implies "no conflict".

**(b) Different, but the same claim.** "Two steps" against "one step", where the intermediate port is reached by no admitted change.
- Both are accounts. The draft, repair 1 and repair 4 all give kind (ii), so each is "easy to vary".
- No admitted pair is one at which they conflict [COMPUTED]. So no finer contract exists, and "the remedy is a finer contract" is false.
- Once an edit that sets \(y\) is admitted (b′), they conflict there and the remedy exists [COMPUTED].
- The 03b repair: not rivals in (b), since the coarse candidate claims nothing the fine one does not; kind (ii) in (b′).

**(c) A recoding.** The variety effect is written 0 ↔ 1.
- If the port translation carries the value map, the draft finds them not of one kind, so kind (ii) rivals.
- If it only renames ports, the recoded candidate fails (F1) everywhere, and the draft gives kind (i).
- Either way a redescription is treated as a rival, against refinement (1). The 03b repair gives not rivals in both cases.
- **Carried forward (not an entry):** Part IV's "port translation" does not say whether it may carry a map of values. If it may not, a recoding of \(E\) alone is not an account, and Derivation 8 covers only the recoding of everything together.

**(d) A duplicate.** The same component is stated twice.
- W33.1's test makes the copy a redundant route (removal half False), not idle. So 02's repair 4 does not set it aside, and the pair stays kind (ii) under the draft and both of 02's repairs.
- The 03b repair: not rivals.

**(e) The tilt against its own coarsening** ("the season is fixed by place and half"), on the world question.
- The draft gives kind (ii). So Deutsch's paradigm of a hard-to-vary explanation is "easy to vary" on the world question, against itself.
- With only place and half admitted, no remedy exists.
- The 03b repair: not rivals (e1). With shading admitted outside \(C\) it gives kind (ii), where the coarsening is false and a finer contract exists (e2) [COMPUTED].

### 1.4 Infinitely many rivals (A4)

The family is "the effect fires when rainfall exceeds \(t\)", for every rational \(t\).
- Every draft claim is pairwise, or universal over a definable class.
- A test at \(r=4\) solves exactly the pairs that straddle 4. Infinitely many problems remain, and no finite set of tests ends them. No draft claim says otherwise.
- "Easy to vary" needs one exhibited rival.
- W60.1 excludes every member that gives the refuted answer, at once.
- Same-cut members that agree on \(C\) are "one account" under the draft, which is mismatch 1 again.
- **UPHELD.** Nothing needs a count.

### 1.5 A problem "solved" by narrowing (A5)

The gardener's two rescues give kind (i) on \(p\), and nothing is established at their 8 conflict pairs. At \(t_2\) both are withdrawn from \(p\) and offered for \(p_n\), which drops those 8 pairs.
- If "offered" means *currently offered*, the draft reports **no problem for \(p\)** at \(t_2\) [COMPUTED]. The narrowing has "solved" \(p\).
- On \(p_n\) the two are "one account", so the problem vanishes there too.
- If "offered" means *has been offered*, the problem for \(p\) stands.
- W60.1 protects failures against narrowing. Nothing protects problems. FIX-5 closes this.

### 1.6 A correction that sticks on \(p\) while the mistake comes back nearby (A6)

- **(1) An untested neighbour.** E0 is not an account of the neighbouring question \(p_{nb}\), whose contract holds an untested summer where E0 errs as before, yet it fits what is established there. W60.1 is silent, as its LOSS says.
- **(2) A coarser query** ("is the south bed first?"). E0 fails too, by one derivation from the same receipt. W60.1's text claims only "the same target and query".
- **(3) Another target** (the neighbour's garden). E0's failed answer is right there, and W60.1 rightly claims nothing.
- **(4) A changed query** ("I meant which bed gets more sun"). It is a different question, and E0 fails its non-circular dependence anyway. W60.1's last sentence names only a narrowed contract.

**Acceptable?** Yes. On the owner's position the correction is the exclusion of the failed answer at the failed pair, on every question that holds the pair. (1) and (3) are the fallibilist limit and are recorded. (2) and (4) need only FIX-12's two words.

### 1.7 A rival that fits only through a background assumption (A7; A3 (a))

- **The test's background.** The failed summer's receipt rests on "the beds were watered alike".
  - For an assessor who drops that premise silently, E0 fits and poses a kind-(i) problem against E_good. For one who holds it, there is none [COMPUTED].
  - W60.1's clause holds exactly: all 67 candidates that fail only there revive alike, and no candidate answering N changes status.
  - "Problem for \(p\)" is therefore relative to an assessor, through "established", and FIX-6 says so.
- **The candidate's own named background.** The background (A3 (a)) is exactly where two candidates can differ while the parenthesis sees nothing. FIX-1 catches this.

### 1.8 A conflict that only the adopted physics makes (A8)

A current splitter under a conservation law. R1 says channel 1 carries the current; R2 says channel 2 does.
- Over every relation, both can meet the three conditions at \(a=1\), with the law deformed. The draft gives kind (ii): "no test … is sure to solve it", and "the remedy is a finer contract".
- Over what the physics admits, they conflict at \(a=1\). That is kind (i), and a test there is sure to solve it [COMPUTED].
- Part I fixes which organizations a carrier can bear by the adopted physics, so the quantifier must range over what the physics admits (FIX-2).
- 02's own models do not show the difference (A10). That confirms 02's §4 for them and no further.

---

## 2. The repair to the rivals clause, run over 02's models (A9)

**The 03b repair.** Two candidates are rivals when:
- each has been offered as an answer to \(p\) in place of the other; and
- each claims something the other does not. At some admitted change, in \(C\) or outside it, that both translate, the adopted physics admits relations of the target under which one of them meets (F1), (F2) and (A) and the other does not. At some such change the reverse holds.

The kinds are unchanged: (i) a conflict at a pair of \(C\); (ii) otherwise. The repair uses only the draft's own kind of quantifier, "the target's relations there", over admitted changes. It lists, counts and grades nothing.

**Against the draft, across 02's six models and the seasons with shading admitted (A9, 35 pairs).** The two agree on 20 pairs and differ on 15 [COMPUTED]. The repair gives the expected verdict wherever one exists, except on two sets of rows whose expectation rests on something the models leave out (consequences 1 and 2 below):
- It restores rivals the draft loses: M1 on the record question, and N2 on both writings (`dem_p` against the southern variant).
- It removes "rivals" that are not competitors:
  - the idle god, the route god and the duplicate;
  - mechanism against rule when no change sets the variety effect;
  - 02's "self", which claims only part of the dog story.
- It keeps every verdict the draft had right: O24's kind (i), D3-T, E0's failure, the label swaps, and the tilt against the myth.

**Three consequences to record.**
1. **The owner's example needs a separating admitted change.** "Demeter grieves" against "Persephone is underground" is a rival pair only where some admitted change sets the warmth received on its own. With only place and half admitted, "Persephone is underground" claims nothing the grief story does not; with shading admitted, the pair is kind (ii) (A9: M2 against S+). This is the change 01:L216 itself names ("A change that set the mediating state on its own"). FIX-8 makes the REASON say that the verdict rests on it.
2. **An impossible candidate is no one's rival.** A myth anchored to nothing fails (F1) at every pair, whatever the world. Under the repair it claims nothing that could hold, so it poses no problem (A9: R-none rows; the unfaithful god). The draft gave kind (i) (degenerate) here, where the owner expects kind (ii) for his example. This matches Deutsch p.25 (rejected "without any experiment"). It decides 02's mismatch 2 for rivalry, but not 02's mismatch 7 (c) for failures of non-circular dependence.
3. **A residual (A3 (f)).** Two candidates can each be exact about a different link, both true, and compatible. They are rivals under the repair (kind (ii)), and they stand or fall together at every admitted pair. The finer contract's test refutes both on the finer question. Only a third candidate exact about both links ends the contest.
   - Neither the draft nor the repair lets a problem be solved by conjecture. A problem ends only when what is established leaves at most one of the rivals fitting.
   - This is a limit to record in LOSS, not a counterexample to any sentence once FIX-4 is made.

---

## 3. Checks of `02 models.md`

- **Reproduction.** All six scripts were re-run from `models/`. Each output is byte for byte its stored file, and each of 02's appendix blocks is verbatim (md5s in section 5).
- **Mismatches 1–7.** Each was confirmed by the re-run. A9 and A12 add evidence.
  - 02's option (b) for degenerate conflicts, which 02 did not run, behaves as 02 said (A12). It makes the owner's example kind (ii) under both anchorings. Under R-none a test of relations at either Greek pair is then sure to solve it, so kind (ii)'s "no test … is sure to solve" would need rewording.
- **Repair 1 is insufficient.** It is "one account" judged on every admitted pair. It fixes the M1 and N2 cases but not A3 (a) (a look-alike conflict), (b), (c), (d) or (e1).
- **Repair 4 is insufficient.** It sets aside commitments that do no work by W33.1's test.
  - A duplicate is a redundant route by that test, so it is not set aside (A3 (d)).
  - In a candidate with no support, every commitment passes the test vacuously and is set aside (A3 (a), DRYM).
- **§4, the space of relations.** 02 says no verdict changed with the space. That is true of its models: the door (M3 (d)) is kind (ii) in both spaces, and the witness is a door that needs both spring and cable (A10). A8 is a model where the physics changes the kind.
- **M5's "self".** It is glossed "the universe holds itself up; nothing holds it". It is modelled as a single component anchored to the holder subnetwork, which says only that something there holds it: a coarsening of the dog story, not its denial.
- **M1's table.** It attributes "windy spring would fit as well" to the owner. The words are the correction-sticks analysis's (its L22 and L264).
- **Page checks for W38.1** (extracted text; a marker [p.N] opens page N):
  - p.16: two viable theories, conflicting predictions, an experiment.
  - p.17: a problem is conflicting ideas experienced.
  - p.20: Freyr.
  - p.21: easy to vary "without changing its predictions"; the southern variant; "radically incompatible" but "the same core explanation".
  - p.22: "could easily explain anything".
  - p.25: "rejected out of hand without any experiment".
  - pp.27–28: the Aristarchus variant, "no longer an explanation".
  - p.31: the glossary.
  - All are as W38.1 cites them, except the two wording points (FIX-14b, 14c).

---

## 4. The exact fixes

OLD and NEW are in the entries' own text (01's line numbers). Where one fix touches a sentence another also touches, the NEW includes both.

**FIX-1, FIX-2, FIX-5 and FIX-6: W59.1 "Rivals" (01:L177).**

OLD:
````text
Two explanatory candidates for one question \(p\) are **rivals** when each is offered as an answer to \(p\) in place of the other and they differ in what they claim on \(C\), not only in how it is written: they are not one account on \(C\) in the sense of Derivation 2 (paired active components with one anchor and one kind on \(C\), and one answer profile).
````
NEW:
````text
Two explanatory candidates for one question \(p\) are **rivals** when each has been offered as an answer to \(p\) in place of the other and each claims something the other does not: at some admitted change, in \(C\) or outside it, that both translate, the adopted physics admits relations of the target under which one of them meets (F1), (F2) and (A) there and the other does not, and at some such change the reverse. Candidates of which neither claims anything the other does not are one explanation however they are written (Derivation 2), and a candidate that claims only part of what another claims is not its rival.
````
In the same paragraph:
- OLD "whatever the target's relations there, not both meet" → NEW "whatever relations the adopted physics admits for the target there, not both meet" (FIX-2).
- OLD "A candidate **fits** what is established when no established result shows it failing" → NEW "A candidate **fits** what is established for an assessor when no result established for that assessor shows it failing" (FIX-6).

**FIX-6, FIX-3, FIX-4, FIX-5 and FIX-7: W59.1 "Problems" (01:L179).** Five replacements:
- OLD "Two rivals that both fit what is established pose a **problem for \(p\)**" → NEW "Two rivals that both fit what is established for an assessor pose, for that assessor, a **problem for \(p\)**".
- OLD "Establishing what the target does there is then a **test** that solves the problem whatever it shows," → NEW "Whatever the target does there, at most one of them is an account of \(p\), whether or not anyone can establish it; establishing what the target does there, its relations and not only its answer, is a **test** that solves the problem whatever it shows," (FIX-3).
- OLD "the contract does not contain their conflict." → NEW "the contract does not contain what separates them." Then insert after "…both are accounts of \(p\)." the sentence (FIX-5): "A contract narrowed to leave out the pairs at which two rivals conflict makes a different question (Part III); it solves nothing on \(p\), and the problem for \(p\) stands until what is established leaves at most one of them fitting."
- OLD "The remedy is a finer contract, which is a new question (Part III);" → NEW "A finer contract that contains a change at which they conflict, where there is one, is a new question (Part III), on which they pose a problem of the first kind;" (FIX-4).
- OLD "and keeping such a rival is protected (Part XI)." → NEW "where keeping such a rival is among the protected obligations (Part XI)." (FIX-7).

**FIX-8: W59.1 REASON, "The owner's example" (01:L216).**
- OLD "On the Greek question they give one answer at every pair, so they conflict at no pair of \(C\), which is kind (ii). A change that set the mediating state on its own would lie outside that contract."
- NEW "With grief tied to the warmth received, both meet (F1), (F2) and (A) at each pair of the Greek question under the target's actual relations, so they conflict at no pair of \(C\): kind (ii). They are rivals because a change that sets the warmth received on its own, such as a veil of dust, is admitted and lies outside that contract: there the grieving goddess makes the cold, and Persephone's absence alone does not. Anchored to nothing, either myth fails (F1) whatever the world does, claims nothing that could hold, and is no one's rival."

**FIX-9: W59.1 REASON, "Labels do not make rivals" (01:L217).**
- OLD "This agrees with Deutsch's own reduction of the Persephone and Freyr myths to one core explanation (p.21)."
- NEW "Deutsch reduces the Persephone and Freyr myths to one core explanation, though he says they assert incompatible things (p.21); here an incompatibility carried by no anchor and no admitted change is one of labels, and the sources note records the departure."

**FIX-10: W59.1 CASES AT RISK.**
- **N3 (01:L231).** OLD "\"Its details … could be swapped for others that fit the Greeks' facts just as well\" is a rival of kind (ii)." → NEW "Some of its details, those whose swap changes what the story claims at an admitted change (why grief brings cold, not which gods), give rivals of kind (ii); a swap of labels gives one account."
- **N2 (01:L229).** Add "on either writing of the myth".
- **N7 (01:L236–L239).** Replace the watch with: "A leaner account claims only part of what a fuller one claims, so the two are not rivals even if offered in place of each other."
- **N1 (01:L225).** Add: "Offered in place of Tomas's, the telling with the idle god claims nothing Tomas's does not, and is not its rival."
- **The DECLARATION** follows the NEW text.

**FIX-11: W59.1 LOSS (01:L247–L251).** Add:
- "On a contract that omits an admitted change at which a candidate claims something, a variant patched there is a rival of the second kind, so any such candidate, the tilt on the Greek question included, is easy to vary there once the variant is offered."
- "A problem ends only when what is established leaves at most one of its rivals fitting, not when a third candidate claims all that each claims."

**FIX-12: W60.1 (01:L271).**
- OLD "A contract that omits \((a,b)\) makes a different question (Part III)"
- NEW "A contract that omits \((a,b)\), or a changed query, makes a different question (Part III)"

**FIX-13: W33.1 (01:L145); minor, optional.**
- OLD "A commitment \(d\) does no work by itself in the candidate when every support stays a support"
- NEW "A commitment \(d\) of a candidate that has a support does no work by itself in it when every support stays a support"

**FIX-14: W38.1 "Hard to vary" (01:L316 and L350; the two copies alike).** Four changes:
- **(a)** OLD "a pair of the question's contract at which they conflict is a test that solves it" → NEW "establishing what the target does at a pair of the question's contract at which they conflict is a test that solves it".
- **(b)** OLD "an explanation able to fit anything in its field explains nothing (p.22)" → NEW "an explanation that could easily explain anything in its field explains nothing (p.22)".
- **(c)** OLD "which he finds reduce to one core explanation (p.21)" → NEW "which he finds assert incompatible things and yet reduce to one core explanation (p.21)".
- **(d)** OLD "Three departures remain." → NEW "Four departures remain." Append: "And a variant that keeps an explanation's claims inside the question and patches them outside it, as Aristarchus might have patched the axis-tilt theory, is for him no longer an explanation (pp.27–28); here it is a rival of the second kind, so on a question that does not reach the far places even the axis-tilt theory is easy to vary." This needs FIX-1. Without it, the draft calls the patch one account.

---

## 5. Files and re-running

`rivals/attack/` in the session scratchpad. Run each with `python3 <script>` from that folder. A3 and A9 were run with `PYTHONHASHSEED=0`, and A3 was also checked with seeds 1 and 2 (the same output). There is no `a2` script: the "differ only outside the question" attack is A1 (3), A9 (M1, M2) and A11.

| file | md5 | output md5 |
|---|---|---|
| ext.py | e24cb926697ded6578b9d70a7f46040f | — |
| a1_unperformable.py | 0d7e55644f2556756f78bf65762754a5 | cb20d508070ae3a86ce32a913683f982 |
| a3_redescription.py | 13a095925693ded527df835768a52ed6 | eac39ca049eb1d7fc25e0206702634c0 |
| a4_infinite.py | f9ddcfa75641810c7d4f6e1395e7a81f | 59331f9709b910dcd25a4fe0ab16100e |
| a5_narrowing.py | d0cddc7aecb787f5f29a9e21c55e6b35 | f9f61886aa9d7d5baac31e8086a5c202 |
| a6_sticks.py | e01ef3fcdc5cb44dbc4c90fb60088165 | 63755596475c97cfacd0848f33d67bb3 |
| a7_k3.py | 2d03ff68dcf04ff0090efc82d26100cd | fb52120edea41602389098e7183e12a7 |
| a8_physics.py | a51827f4185b30d8dbf8ff649817f7f4 | aef0d44bc0f04176301f76d24fa1d2f0 |
| a9_regression.py | fbbc424c9a903547565745a80db6b20a | 833a42032d3e1ce6b1d3f314e6ded269 |
| a10_space.py | 4aa9181050cd5ca0f5f19e24b56888af | dfd124bd88eb47362aef893efcc9e31d |
| a11_patch.py | db2354cc43c4cae37c77d9c91476a315 | 6a149d05056db1b4a48317797200662b |
| a12_option_b.py | 8eeff9d336d81827d1d04a2fbc3d7a57 | 6694f43f83c7a745f852949a95d62e51 |
| rerun/m1…m6_output.txt (02's scripts re-run) | — | identical to 02's stored outputs (ef1b69f8…, 9f8d79ac…, 50f64071…, fdc6330e…, 2f6f4b3d…, 42f51536…) |

---

## Appendix: the outputs, verbatim

### `a1_unperformable.py` → `a1_output.txt`

```text
====================================================================================================
A1  RIVALS THAT CONFLICT ONLY AT AN ADMITTED CHANGE NOBODY CAN PERFORM
====================================================================================================

----------------------------------------------------------------------------------------------------
(1) p_dep: contract = all four pairs; performable/observable: tilt=1 only
----------------------------------------------------------------------------------------------------
  R1 tilt          Account(p_dep)=True  fits=True
  R2 eccentricity  Account(p_dep)=False fits=True
  conflict pairs: ['tilt=0,H1', 'tilt=0,H2']
  draft verdict:    PROBLEM for p, kind (i)
  repair verdict:   PROBLEM for p, kind (i) a pair outside C where they conflict (a finer contract separates them): NO
  "a test there solves it whatever it shows" at tilt=0,H1: relations=True answer=True  (conditional: IF established)
  whatever the world is at tilt=0, at most one of R1, R2 is an account of p_dep: True
  actual world: R1 account=True, R2 account=False

----------------------------------------------------------------------------------------------------
(2) receipts for the answer at tilt=0 (no event there: every receipt is a derivation)
----------------------------------------------------------------------------------------------------
  live premises: ['R1', 'R2', 'U', 'obs tilt=1']
    derived from R1 itself                                                         usable=False  (reconstructed from the claim it supports)
    derived from R2 itself                                                         usable=False  (reconstructed from the claim it supports)
    derived from U (inclined-plate law, tested apart from seasons) + tilt=1 results usable=True 
    -> R1 fits True, R2 fits False; draft verdict: rivals; NO problem: R2 eccentricity does not fit what is established
  live premises: ['R1', 'R2', 'obs tilt=1']
    derived from R1 itself                                                         usable=False  (reconstructed from the claim it supports)
    derived from R2 itself                                                         usable=False  (reconstructed from the claim it supports)
    derived from U (inclined-plate law, tested apart from seasons) + tilt=1 results usable=False
    -> R1 fits True, R2 fits True; draft verdict: PROBLEM for p, kind (i)

----------------------------------------------------------------------------------------------------
(3) p_here: the contract omits the unperformable pairs
----------------------------------------------------------------------------------------------------
  one account on C_here (draft parenthesis): (True, 'paired: geo~geo, seas~seas')
  draft verdict:    not rivals: one account (paired: geo~geo, seas~seas)
  repair verdict:   PROBLEM for p, kind (ii) a pair outside C where they conflict (a finer contract separates them): yes
```

### `a3_redescription.py` → `a3_output.txt`

```text
====================================================================================================
A3  LOOK ALIKE BUT DIFFER; LOOK DIFFERENT BUT CLAIM THE SAME
====================================================================================================

----------------------------------------------------------------------------------------------------
(a) look alike, differ: the same active components, anchors, kinds and answers; different background
----------------------------------------------------------------------------------------------------
    one account on C by the draft's parenthesis: (True, 'paired: sun1~sun1, var~var')
  WETM vs DRYM on p (C = the 16 settings)
    accounts on C: True / False
    draft:         not rivals: one account (paired: sun1~sun1, var~var)
    02 repair 1:   not rivals: one account (paired: sun1~sun1, var~var)
    02 repair 4:   rivals; NO problem: E_good + moisture follows the dry spring does not fit what is established   [set aside: - | ['sun1', 'var']]
    03b repair:    PROBLEM for p, kind (i)   [a pair outside C where they conflict (a finer contract separates them): NO]
    conflict pairs in C (draft's definition): dry/calm/late/sunS, dry/calm/late/shadeS, dry/calm/early/sunS, dry/calm/early/shadeS, dry/windy/late/sunS, dry/windy/late/shadeS, dry/windy/early/sunS, dry/windy/early/shadeS, wet/calm/late/sunS, wet/calm/late/shadeS, wet/calm/early/sunS, wet/calm/early/shadeS, wet/windy/late/sunS, wet/windy/late/shadeS, wet/windy/early/sunS, wet/windy/early/shadeS
    test at dry/calm/late/sunS: sure to solve with relations established: True ; with the answer only: False
    with the actual relations at dry/calm/late/sunS established: WETM fits True, DRYM fits False
    W33.1's test on a candidate with no support at all: DRYM supports: set(); E0 supports: set(); E0's only component "does no work by itself": True

----------------------------------------------------------------------------------------------------
(b) look different, claim the same: two steps against one, at a place no admitted change reaches
----------------------------------------------------------------------------------------------------
  (b) admitted changes: set x only (C = every admitted change)
    accounts on C: True / True
    draft:         PROBLEM for p, kind (ii)
    02 repair 1:   PROBLEM for p, kind (ii)
    02 repair 4:   PROBLEM for p, kind (ii)   [set aside: - | -]
    03b repair:    not rivals: one step claims nothing two steps does not
    conflict pairs in C (draft's definition): none
    is any admitted pair one at which they conflict (a finer contract to remedy it)? False
  (b') edits that set y are admitted too (outside C)
    accounts on C: True / True
    draft:         PROBLEM for p, kind (ii)
    02 repair 1:   PROBLEM for p, kind (ii)
    03b repair:    PROBLEM for p, kind (ii)   [a pair outside C where they conflict (a finer contract separates them): yes]
    conflict pairs in C (draft's definition): none
    conflict pairs outside C: ['x=0,y=1', 'x=1,y=0']

----------------------------------------------------------------------------------------------------
(c) a recoding: the variety effect written 0 <-> 1
----------------------------------------------------------------------------------------------------
  E_good vs E_good recoded (value-map translation) (admitted: the 48 pairs of the finer contract)
    accounts on C: True / True
    draft:         PROBLEM for p, kind (ii)
    02 repair 1:   PROBLEM for p, kind (ii)
    03b repair:    not rivals: neither claims anything the other does not
    conflict pairs in C (draft's definition): none
  E_good vs E_good recoded (rename-only translation) (admitted: the 48 pairs of the finer contract)
    accounts on C: True / False
    draft:         PROBLEM for p, kind (i)
    02 repair 1:   PROBLEM for p, kind (i)
    03b repair:    not rivals: E_good claims nothing E_good recoded (rename-only translation) does not
    conflict pairs in C (draft's definition): dry/calm/late/sunS, dry/calm/late/shadeS, dry/calm/early/sunS, dry/calm/early/shadeS, dry/windy/late/sunS, dry/windy/late/shadeS, dry/windy/early/sunS, dry/windy/early/shadeS, wet/calm/late/sunS, wet/calm/late/shadeS, wet/calm/early/sunS, wet/calm/early/shadeS, wet/windy/late/sunS, wet/windy/late/shadeS, wet/windy/early/sunS, wet/windy/early/shadeS

----------------------------------------------------------------------------------------------------
(d) a duplicate: the variety component stated twice
----------------------------------------------------------------------------------------------------
    W33.1's test on var2: addition half=True removal half=False  supports: {sun1,var}, {sun1,var2}, {sun1,var,var2}
  E_good vs the duplicate
    accounts on C: True / True
    draft:         PROBLEM for p, kind (ii)
    02 repair 1:   PROBLEM for p, kind (ii)
    02 repair 4:   PROBLEM for p, kind (ii)   [set aside: - | -]
    03b repair:    not rivals: neither claims anything the other does not
    conflict pairs in C (draft's definition): none

----------------------------------------------------------------------------------------------------
(e) the tilt against its own coarsening ("the season is fixed by place and half"), world question
----------------------------------------------------------------------------------------------------
  (e1) admitted: place and half only
    accounts on C: True / True
    draft:         PROBLEM for p, kind (ii)
    02 repair 1:   PROBLEM for p, kind (ii)
    02 repair 4:   PROBLEM for p, kind (ii)   [set aside: - | -]
    03b repair:    not rivals: coarse tilt claims nothing tilt does not
    conflict pairs in C (draft's definition): none
  (e2) shading (sets ins) admitted too, outside C
    accounts on C: True / True
    draft:         PROBLEM for p, kind (ii)
    02 repair 1:   PROBLEM for p, kind (ii)
    03b repair:    PROBLEM for p, kind (ii)   [a pair outside C where they conflict (a finer contract separates them): yes]
    conflict pairs in C (draft's definition): none

----------------------------------------------------------------------------------------------------
(f) residual of the 03b repair: two compatible partial claims, each exact about one link, both true
----------------------------------------------------------------------------------------------------
  P vs Q (admitted: set x, and set w outside C)
    accounts on C: True / True
    draft:         PROBLEM for p, kind (ii)
    02 repair 1:   PROBLEM for p, kind (ii)
    03b repair:    PROBLEM for p, kind (ii)   [a pair outside C where they conflict (a finer contract separates them): yes]
    conflict pairs in C (draft's definition): none
    in the actual world P and Q stand or fall together at every admitted pair: True (both meet the three at: ['x=0', 'x=1', 'w=0,x=0', 'w=0,x=1']; both fail at: ['w=1,x=0', 'w=1,x=1'])
    so the finer contract's test refutes both on the finer question, both stay accounts of p, and only a candidate exact about both links (claiming all that each claims) ends the contest.
```

### `a4_infinite.py` → `a4_output.txt`

```text
====================================================================================================
A4  INFINITELY MANY RIVALS (symbolic)
====================================================================================================
  (1) E_s, E_t conflict exactly at s < r <= t (spot check, 5166 triples): True
  (2) members that fit the dry-climate results: every t >= 2 (sample: min fitting t = 2, all t >= 2 fit: True)
      E_3 vs E_5 on p_dry: conflict inside C_dry: False -> kind (ii) (as repaired); draft as written: same cut, same anchor, same relations on C_dry -> "one account", not rivals
      E_3 vs E_5 on p_all: they conflict at every r in (3, 5] -> kind (i)
  (3) a test at r = 4 solves the problem of E_s vs E_t iff s < 4 <= t (or t < 4 <= s):
      E_2 vs E_5: solved by the test at 4: True
      E_3 vs E_7/2: solved by the test at 4: False
      E_9/2 vs E_6: solved by the test at 4: False
      E_5/2 vs E_4: solved by the test at 4: True
      after it, the fitting members are t in [2, 4) (every one fires at r = 4 iff t < 4, target fires): infinitely many; pairs among them still pose problems of kind (i) on p_all.
      no finite set of tests {r_1..r_n} leaves one member: between two consecutive tested values lie infinitely many t, all agreeing on every tested r.
  (4) E_3 is "easy to vary" on p_dry as soon as ONE rival (say E_5) is offered: kind (ii) as repaired. Nothing counts the members or lists them.
  (5) W60.1 over the family: every E_t with t < 1 answers "fires" at r = 1, the target does not: excluded alike, for all (infinitely many) at once; sample check: True
```

### `a5_narrowing.py` → `a5_output.txt`

```text
====================================================================================================
A5  A PROBLEM "SOLVED" BY NARROWING THE QUESTION
====================================================================================================
  conflict pairs on p: 8 (dry/calm/early/sunS ...); C_n keeps 8 settings

----------------------------------------------------------------------------------------------------
(1) the draft, time by time
----------------------------------------------------------------------------------------------------
  t1, "offered" read as now   p: PROBLEM for p, kind (i)                                    p_n: not rivals: not offered
  t1, "offered" read as ever  p: PROBLEM for p, kind (i)                                    p_n: not rivals: not offered
  t2, "offered" read as now   p: not rivals: not offered in place of each other             p_n: not rivals: one account (paired: sun1~sun1, var~var)
  t2, "offered" read as ever  p: PROBLEM for p, kind (i)                                    p_n: not rivals: one account (paired: sun1~sun1, var~var)
  nothing was established at the 8 conflict pairs between t1 and t2: established pairs are ['dry/calm/late/sunS', 'dry/calm/late/shadeS', 'wet/windy/early/sunS']

----------------------------------------------------------------------------------------------------
(2) p_n under the draft (same cut: one account on C_n?) and under the 03b repair
----------------------------------------------------------------------------------------------------
  one account on C_n: (True, 'paired: sun1~sun1, var~var')
  03b repair on p_n (admitted: all 16): PROBLEM for p, kind (ii) a pair outside C where they conflict (a finer contract separates them): yes
  03b repair on p   (admitted: all 16): PROBLEM for p, kind (i) a pair outside C where they conflict (a finer contract separates them): NO
```

### `a6_sticks.py` → `a6_output.txt`

```text
====================================================================================================
A6  DOES THE MISTAKE COME BACK ON A SLIGHTLY DIFFERENT QUESTION?
====================================================================================================
  on p: E0 answers ['S'] at FSTAR, target ['N']; E0 fits: False; Account(p): False

----------------------------------------------------------------------------------------------------
(1) p_nb: same target and query; the contract omits FSTAR and holds an untested neighbour NB
----------------------------------------------------------------------------------------------------
  E0 at NB: ['S'], target at NB: ['N']  -> E0 Account(p_nb) = False (a fact of (A)); fits what is established on p_nb: True
  W60.1 is silent here (NB is not the failed pair); the failure on p stands: E0 Account(p) = False

----------------------------------------------------------------------------------------------------
(2) p_q2: the coarser query "does the south bed ripen first?"
----------------------------------------------------------------------------------------------------
  E0's answer at FSTAR under Q2: ['yes']; the target's: ['no'] -> E0 fails (A) on p_q2: True
  the receipt for Ans_p(FSTAR) = N yields, by one derivation step, one for Ans_q2(FSTAR) = no; W60.1's text states the exclusion only for "the same target and query".

----------------------------------------------------------------------------------------------------
(3) p_nbr: the neighbour's garden (the early variety has no effect there)
----------------------------------------------------------------------------------------------------
  target's answer at FSTAR: ['S']; E0 Account on the neighbour's question: True
  the failed answer on p is the right answer here: a different target, and W60.1 does not claim it.

----------------------------------------------------------------------------------------------------
(4) p_sun: "I meant which bed gets more sun"
----------------------------------------------------------------------------------------------------
  (A) on p_sun: True; NonCircular: False; Account(p_sun): False
  whatever p_sun's fate, it is a question with a different query; W60.1's last sentence names only a contract that omits the pair, while Part III and D3:L151 cover a changed query.
```

### `a7_k3.py` → `a7_output.txt`

```text
====================================================================================================
A7  A RIVAL THAT FITS ONLY THROUGH A BACKGROUND ASSUMPTION (K3)
====================================================================================================
  j1 (holds B)    established pairs: dry/calm/late/sunS, dry/calm/late/shadeS, wet/windy/early/sunS E0 fits: False  E_good vs E0: rivals; NO problem: E0 does not fit what is established
  j2 (dropped B)  established pairs: dry/calm/late/sunS, dry/calm/late/shadeS                     E0 fits: True   E_good vs E0: PROBLEM for p, kind (i)

----------------------------------------------------------------------------------------------------
W60.1 "if they come into question, the exclusion does too, for every such candidate alike"
----------------------------------------------------------------------------------------------------
  harness: 1041 candidates; 265 answer S at FSTAR; of these 67 fit every result except FSTAR's
  for j1: of those 67, fitting: 0
  for j2: of those 67, fitting: 67  (revived alike: True)
  no candidate answering N at FSTAR changes status between j1 and j2: True
  -> the problem "E_good vs E0" exists for j2 and not for j1: the draft's "problem for p" is relative to an assessor, through "established", but the Problems paragraph does not say so.
```

### `a8_physics.py` → `a8_output.txt`

```text
====================================================================================================
A8  A CONFLICT THAT ONLY THE ADOPTED PHYSICS MAKES
====================================================================================================
  R1 channel 1   Account=True  fits=True   
  R2 channel 2   Account=False fits=True   F2+F1[k]@a=1
  one account (draft parenthesis): (False, 'no pairing with one anchor')
  witness over ALL relations at a=1 (the laws deformed: m1 = m2 = 1, delivered 1): R1 meets True, R2 meets True
  a=0, relations the physics admits: some let both meet: True   some let R1: True  some let R2: True
  a=1, relations the physics admits: some let both meet: False  some let R1: True  some let R2: True
  draft verdict (conflict over all relations):          PROBLEM for p, kind (ii)
  with the quantifier over what the physics admits:     PROBLEM for p, kind (i)  (conflict at a=1)
  a test at a=1 establishing the relations: sure to solve over what the physics admits: True
  so the draft's kind-(ii) sentence "no test the question admits is sure to solve" holds of this pair only by counting outcomes the physics forbids, and "the remedy is a finer contract" is not needed: a test inside C solves it.
```

### `a9_regression.py` → `a9_output.txt`

```text
====================================================================================================
A9  THE 03b REPAIR OVER 02'S MODELS
====================================================================================================

----------------------------------------------------------------------------------------------------
M1 the gardener (admitted: the 16 settings; M3 (b) also the 32 edits that set the variety effect)
----------------------------------------------------------------------------------------------------
  M1   E_good vs E_bad, p
       draft:    PROBLEM for p, kind (i)
       03b:      PROBLEM for p, kind (i)   [a pair outside C where they conflict (a finer contract separates them): NO]
       expected: kind (i) (O24; 02)
  M1   E_good vs E0, p
       draft:    rivals; NO problem: E0 does not fit what is established
       03b:      rivals; NO problem (one does not fit)
       expected: no problem: E0 does not fit
  M1   E_good vs E_bad, p_rec
       draft:    not rivals: one account (paired: sun1~sun1, var~var)
       03b:      PROBLEM for p, kind (ii)   [a pair outside C where they conflict (a finer contract separates them): yes]
       expected: kind (ii) (owner, refinement 2)
  M1   E_bad vs E_windy, p_rec
       draft:    not rivals: one account (paired: sun1~sun1, var~var)
       03b:      PROBLEM for p, kind (ii)   [a pair outside C where they conflict (a finer contract separates them): yes]
       expected: kind (ii) (owner: "windy would fit as well")
  M3b  mechanism vs rule, p (C = 16)
       draft:    PROBLEM for p, kind (ii)
       03b:      not rivals: E_rule claims nothing E_good does not
       expected: N7-like: compatible; 02: kind (ii)
  M3b  mechanism vs rule, p, ovr edits admitted
       draft:    PROBLEM for p, kind (ii)
       03b:      PROBLEM for p, kind (ii)   [a pair outside C where they conflict (a finer contract separates them): yes]
       expected: kind (ii); kind (i) on p_fine (02)
  M3c  one answer profile, one anchor, other relations
       draft:    PROBLEM for p, kind (i)
       03b:      PROBLEM for p, kind (i)   [a pair outside C where they conflict (a finer contract separates them): NO]
       expected: kind (i) (02)
  M3d  spring vs slack cable (door)
       draft:    PROBLEM for p, kind (ii)
       03b:      PROBLEM for p, kind (ii)   [a pair outside C where they conflict (a finer contract separates them): NO]
       expected: kind (ii); a relation test in C refutes the cable (02 7b)
  M3a  E_good vs E_good renamed
       draft:    not rivals: one account (paired: sun1~suncomp, var~boostcomp)
       03b:      not rivals: neither claims anything the other does not
       expected: not rivals (refinement 1)

----------------------------------------------------------------------------------------------------
M2 the seasons: the draft on the six pairs; the 03b repair with and without shading admitted
----------------------------------------------------------------------------------------------------
  M2   dem vs und, Greek q., six pairs
       draft:    PROBLEM for p, kind (ii)
       03b:      not rivals: und claims nothing dem does not
       expected: owner: kind (ii)
  M2   und vs freyr, Greek q., six pairs
       draft:    not rivals: one account (paired: cold~warmth, sched~war)
       03b:      not rivals: neither claims anything the other does not
       expected: not rivals (Deutsch p.21 core; draft)
  M2   dem vs sorrow, Greek q., six pairs
       draft:    not rivals: one account (paired: gcold~scold, griefc~sorrowc, sched~sched)
       03b:      not rivals: neither claims anything the other does not
       expected: not rivals (label)
  M2   dem vs dem2, Greek q., six pairs
       draft:    PROBLEM for p, kind (ii)
       03b:      not rivals: dem2 claims nothing dem does not
       expected: -
  M2   dem vs south, Greek q., six pairs
       draft:    PROBLEM for p, kind (ii)
       03b:      PROBLEM for p, kind (ii)   [a pair outside C where they conflict (a finer contract separates them): yes]
       expected: N2: kind (ii)
  M2   dem_p vs south, Greek q., six pairs
       draft:    not rivals: one account (paired: gcold~gcold, griefc~griefc, sched~sched)
       03b:      PROBLEM for p, kind (ii)   [a pair outside C where they conflict (a finer contract separates them): yes]
       expected: N2: kind (ii)
  M2   tilt vs dem, Greek q., six pairs
       draft:    PROBLEM for p, kind (ii)
       03b:      PROBLEM for p, kind (ii)   [a pair outside C where they conflict (a finer contract separates them): yes]
       expected: kind (ii) on the Greek question (02 7a)
  M2   dem[R-none] vs und[R-none], Greek q., six pairs
       draft:    PROBLEM for p, kind (i)
       03b:      not rivals: neither claims anything the other does not
       expected: owner: kind (ii); 02: kind (i) degenerate
  M2   tilt vs dem[R-none], Greek q., six pairs
       draft:    PROBLEM for p, kind (i)
       03b:      not rivals: tilt claims nothing dem[R-none] does not
       expected: 02: kind (i) degenerate
  S+   dem vs und, Greek q., + shading
       draft:    PROBLEM for p, kind (ii)
       03b:      PROBLEM for p, kind (ii)   [a pair outside C where they conflict (a finer contract separates them): yes]
       expected: owner: kind (ii)
  S+   und vs freyr, Greek q., + shading
       draft:    not rivals: one account (paired: cold~warmth, sched~war)
       03b:      not rivals: neither claims anything the other does not
       expected: not rivals (Deutsch p.21 core; draft)
  S+   dem vs sorrow, Greek q., + shading
       draft:    not rivals: one account (paired: gcold~scold, griefc~sorrowc, sched~sched)
       03b:      not rivals: neither claims anything the other does not
       expected: not rivals (label)
  S+   dem vs dem2, Greek q., + shading
       draft:    PROBLEM for p, kind (ii)
       03b:      PROBLEM for p, kind (ii)   [a pair outside C where they conflict (a finer contract separates them): yes]
       expected: -
  S+   dem vs south, Greek q., + shading
       draft:    PROBLEM for p, kind (ii)
       03b:      PROBLEM for p, kind (ii)   [a pair outside C where they conflict (a finer contract separates them): yes]
       expected: N2: kind (ii)
  S+   dem_p vs south, Greek q., + shading
       draft:    not rivals: one account (paired: gcold~gcold, griefc~griefc, sched~sched)
       03b:      PROBLEM for p, kind (ii)   [a pair outside C where they conflict (a finer contract separates them): yes]
       expected: N2: kind (ii)
  S+   tilt vs dem, Greek q., + shading
       draft:    PROBLEM for p, kind (ii)
       03b:      PROBLEM for p, kind (ii)   [a pair outside C where they conflict (a finer contract separates them): yes]
       expected: kind (ii) on the Greek question (02 7a)
  S+   dem[R-none] vs und[R-none], Greek q., + shading
       draft:    PROBLEM for p, kind (i)
       03b:      not rivals: neither claims anything the other does not
       expected: owner: kind (ii); 02: kind (i) degenerate
  S+   tilt vs dem[R-none], Greek q., + shading
       draft:    PROBLEM for p, kind (i)
       03b:      not rivals: tilt claims nothing dem[R-none] does not
       expected: 02: kind (i) degenerate

----------------------------------------------------------------------------------------------------
M4 D3-T; M5 N25; M6 N1
----------------------------------------------------------------------------------------------------
  M4   X vs Y
       draft:    rivals; NO problem: Y discarded does not fit what is established
       03b:      rivals; NO problem (one does not fit)
       expected: no problem: Y fails (D3-T)
  M4   X vs Z, tester results only
       draft:    PROBLEM for p, kind (i)
       03b:      PROBLEM for p, kind (i)   [a pair outside C where they conflict (a finer contract separates them): NO]
       expected: kind (i) (D3-T "two designs")
  M5   dog vs turtle
       draft:    not rivals: one account (paired: exists~exists, holds~holds)
       03b:      not rivals: neither claims anything the other does not
       expected: not rivals (N25 "idle"; draft)
  M5   dog vs turtle, R-none
       draft:    not rivals: one account (paired: exists~exists, holds~holds)
       03b:      not rivals: neither claims anything the other does not
       expected: not rivals
  M5   dog vs self
       draft:    PROBLEM for p, kind (ii)
       03b:      not rivals: self claims nothing dog does not
       expected: 02: kind (ii)
  M6   Tomas vs +idle god
       draft:    PROBLEM for p, kind (ii)
       03b:      not rivals: neither claims anything the other does not
       expected: not a problem (task; N1)
  M6   Tomas vs +route god
       draft:    PROBLEM for p, kind (ii)
       03b:      not rivals: neither claims anything the other does not
       expected: watched (W33.1)
  M6   Tomas vs +unfaithful god
       draft:    PROBLEM for p, kind (i)
       03b:      not rivals: Tomas claims nothing Tomas+god[unfaithful] does not
       expected: watched (W33.1)

----------------------------------------------------------------------------------------------------
where the 03b repair and the draft differ
----------------------------------------------------------------------------------------------------
  M1   E_good vs E_bad, p_rec                           draft: not rivals  03b: kind (ii)   expected: kind (ii) (owner, refinement 2)
  M1   E_bad vs E_windy, p_rec                          draft: not rivals  03b: kind (ii)   expected: kind (ii) (owner: "windy would fit as well")
  M3b  mechanism vs rule, p (C = 16)                    draft: kind (ii)   03b: not rivals  expected: N7-like: compatible; 02: kind (ii)
  M2   dem vs und, Greek q., six pairs                  draft: kind (ii)   03b: not rivals  expected: owner: kind (ii)
  M2   dem vs dem2, Greek q., six pairs                 draft: kind (ii)   03b: not rivals  expected: -
  M2   dem_p vs south, Greek q., six pairs              draft: not rivals  03b: kind (ii)   expected: N2: kind (ii)
  M2   dem[R-none] vs und[R-none], Greek q., six pairs  draft: kind (i)    03b: not rivals  expected: owner: kind (ii); 02: kind (i) degenerate
  M2   tilt vs dem[R-none], Greek q., six pairs         draft: kind (i)    03b: not rivals  expected: 02: kind (i) degenerate
  S+   dem_p vs south, Greek q., + shading              draft: not rivals  03b: kind (ii)   expected: N2: kind (ii)
  S+   dem[R-none] vs und[R-none], Greek q., + shading  draft: kind (i)    03b: not rivals  expected: owner: kind (ii); 02: kind (i) degenerate
  S+   tilt vs dem[R-none], Greek q., + shading         draft: kind (i)    03b: not rivals  expected: 02: kind (i) degenerate
  M5   dog vs self                                      draft: kind (ii)   03b: not rivals  expected: 02: kind (ii)
  M6   Tomas vs +idle god                               draft: kind (ii)   03b: not rivals  expected: not a problem (task; N1)
  M6   Tomas vs +route god                              draft: kind (ii)   03b: not rivals  expected: watched (W33.1)
  M6   Tomas vs +unfaithful god                         draft: kind (i)    03b: not rivals  expected: watched (W33.1)
```

### `a10_space.py` → `a10_output.txt`

```text
====================================================================================================
A10  THE SPACE OF TARGET RELATIONS: 02's M3 (d) RE-RUN
====================================================================================================
  space all        conflict at push=1: False  draft verdict: PROBLEM for p, kind (ii)   test at push=1 sure to solve (relations): False
  space functional conflict at push=1: False  draft verdict: PROBLEM for p, kind (ii)   test at push=1 sure to solve (relations): False
  target relations at push=1 under which both meet (space all): 4; the first:
    dcable   [(1, 1)]
    ddoor    [(0, 1, 0), (1, 0, 0), (1, 1, 1)]
    dspring  [(1, 1)]
```

### `a11_patch.py` → `a11_output.txt`

```text
====================================================================================================
A11  THE p.27 VARIANT: A SAME-CUT PATCH OUTSIDE THE QUESTION
====================================================================================================
  accounts of p_greek: tilt True, p.27 variant True; of the world question: tilt True, variant False
  one account on C_greek (draft parenthesis): (True, 'paired: geo~geo, heat~heat, seas~seas')
  draft:      not rivals: one account (paired: geo~geo, heat~heat, seas~seas)
  03b repair: PROBLEM for p, kind (ii) a pair outside C where they conflict (a finer contract separates them): yes
  -> under the repair (and under the owner's refinement 2) the tilt is "easy to vary" on p_greek once anyone
     offers the p.27 variant; the same construction works for any candidate that claims anything at an
     admitted change outside the contract (patch one component's relation there: Derivation 3's proof).
```

### `a12_option_b.py` → `a12_output.txt`

```text
====================================================================================================
A12  02's OPTION (b), RUN
====================================================================================================
  dem vs und                 option (b) conflicts in C: none         -> kind (ii); pairs of C where a relations test is sure to solve it: none
  dem[R-none] vs und[R-none] option (b) conflicts in C: none         -> kind (ii); pairs of C where a relations test is sure to solve it: ['N,H1', 'N,H2']
```

### 02's scripts re-run (`rerun/`)

```text
m1_output.txt: re-run identical to 02's stored output: True
m2_output.txt: re-run identical to 02's stored output: True
m3_output.txt: re-run identical to 02's stored output: True
m4_output.txt: re-run identical to 02's stored output: True
m5_output.txt: re-run identical to 02's stored output: True
m6_output.txt: re-run identical to 02's stored output: True
```
