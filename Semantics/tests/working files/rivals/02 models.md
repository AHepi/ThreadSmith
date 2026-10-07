# Rivals and problems: the drafted wording tested on finite models

**Working file, 25 September 2026. Not frozen.** It tests the wording drafted in `rivals/01 entries.md`, chiefly W59.1 ("Rivals", "Problems"; 01:L177–L179) and W60.1 ("A failed answer stays failed"; 01:L271), on six finite, fully explicit models.

*Written by a subagent for the orchestrator.*
- **Read:** `01 entries.md` in full; draft 3's theory text at L1–L369 and L380–L625; the correction-sticks analysis, sections 0–6, with its scripts `fe.py`, `pl.py`, `a5`, `m1_gardener.py` and `m2_seasons.py`; the S81 case book at O1, O24, O36, O45–O48; the N-case book at N1–N7 and N25; D3-T `final.md`; Deutsch chapter 1, pp.20–22, in the extracted text.
- **Not done:** the repository was read only. Nothing was written into `authority/`, and the Pinker folder was not opened.
- **Scripts:** `rivals/models/` (Python 3.11, standard library, about 45 seconds in all). Every output is inlined verbatim in the appendix.
- **References.** "01:L" means `01 entries.md`, and "D3:L" means draft 3's theory text. [COMPUTED] marks a script output. [PROVED] marks a short general argument given here. [I] marks my inference.

---

## 0. The result in brief

**The draft's definitions reach every verdict tested without a list of rivals, a count or a grade** (section 4). W60.1 holds exactly as stated. The kind-(i) half of W59.1 holds, with one wording gap. The kind-(ii) half has two defects, and three of the draft's own case rows do not follow from its definitions.

**The mismatches, most important first.** Each is taken up in section 3.
1. **Rivals that differ only outside the question are "one account" on it.** Derivation 2's relation is judged on \(C\), and kinds on \(C\) cannot see a difference that lies outside \(C\). So two candidates cut alike (the same components on the same anchors) that differ only outside \(C\) are one account on \(C\), and so not rivals [PROVED, COMPUTED]. Kind (ii) is left with differently cut rivals only.
   - Examples: "wet spring" against "windy spring" on the record question, and the myth against its southern variant, written with one more port.
   - This contradicts the owner's refinement (2), and the draft's own N2 row on one writing.
   - A tested repair judges "one account" on every admitted change, not on \(C\) alone.
2. **"Conflict" is met where one candidate fails whatever the target does.** Suppose a component is anchored to nothing in the target: a god, or the holder of the universe. Then it fails (F1) at every pair, whatever the target's relations. The definition counts this as a conflict at every pair, so the pair becomes kind (i).
   - This happens to the owner's own example when the gods are anchored to nothing.
   - The REASON's step "they give one answer at every pair, so they conflict at no pair of \(C\)" (01:L216) is invalid. A same-answer pair with one anchor and different relations also conflicts.
3. **The kind-(i) test must establish relations, not only answers.** "Establishing what the target does there … solves the problem whatever it shows" is true only if the target's relations there are established. Where the two rivals give the same answer at the pair and differ through (F1), a test of the answer alone leaves both fitting. This holds at 4 of the 8 pairs that separate the gardener's two rescues.
4. **An idle part makes a rival.** Derivation 2 pairs every active component, so Tomas's account with the idle sun god is never one account with Tomas's account without it. Offered in place of each other, they are kind-(ii) rivals, and each is "easy to vary". A tested repair sets aside any commitment that does no work by itself (W33.1's test) before the comparison.
5. **N25, dog against turtle: the draft says not rivals (one account). The task expected kind (ii).** The case book sides with the draft: "the same empty claim … the difference between them is idle". No admitted change reaches the holder, so no rule consistent with Part 0 and defeat condition (C) can make the two rivals. The expectation, not the draft, is what fails here.
6. **Three case rows in W59.1 go beyond its definitions.**
   - N3: label swaps such as "which gods" or "what bargain" are one account, not kind-(ii) rivals.
   - N2: the row holds on one writing of the myth and fails on the other (mismatch 1).
   - The owner's example is kind (ii) only on the writing that gives grief its own step. Written with the same cut as "Persephone is underground", the two stories are one account, as Persephone and Freyr are.
7. **Consequences the note of sources and departures does not record.**
   - On the Greek question, the tilt and the myth pose a kind-(ii) problem, so the tilt is "easy to vary" there.
   - "The remedy is a finer contract" is too strong where one rival is not an account: a test of relations inside \(C\) can refute it.
   - Whether a failure derivable from the candidate alone (non-circular dependence, or an anchor tied to nothing) is "established" is not said. The N25 stories pose a problem or not according to it.

**Tables, one per model.** "Case book" is the thoughtful person's verdict where a case exists.

**M1, the gardener**

| Question | Draft's verdict | Case book, or the owner's position | Match |
|---|---|---|---|
| E_good ("early variety") against E_bad ("wet spring") on "every kind of spring and planting": rivals? | Rivals. Offered in place of each other, and not one account | Owner: rivals | yes |
| A problem, and of which kind? | Both fit the recorded summers and the failed one. Kind (i): they conflict at 8 pairs, 4 of them the dry spring with the early variety and the wet spring with the usual planting (sunny, calm or windy) | O24: "the record has not chosen between them. One reachable setting is enough" | yes |
| Does a test at the dry spring with the early variety solve it? | Yes, whatever it shows, even when only the answer is observed | O24 | yes |
| Does a test at a separating pair where the answers agree (the south wall shaded) solve it? | Only if the variety effect itself is established. With the answer alone, 11 of 64 outcomes leave both fitting | The draft says it solves | **gap** (mismatch 3) |
| After the test, is the old mistake excluded with no record? | Yes. All 265 of 1,041 harness candidates that repeat "south first" at the failed summer fail to fit, and none is an account on any of 22 contracts that hold it. No candidate answering "north" is excluded by that result | Owner: correction sticks | yes |
| Beyond the failed summer? | Not claimed. 56 of the 66 fitting candidates repeat E0's error at another early-variety summer; 24 of 34 still do after the seed trial | The analysis's limit | consistent |
| The retreat: E0 on the narrowed contract | An account of \(p'\), a different question. Not a rival of E_good on \(p\). E0 offered again for \(p\) does not fit, and \(p\) stays failed | O1: "Bruno has no explanation of the floods" | yes |
| The same rescues on the record-only question | One account on \(C\): **not rivals, no problem** | Owner's refinement (2): kind (ii), easy to vary ("windy spring would fit as well") | **NO** (mismatch 1) |

**M2, the seasons**

| Question | Draft's verdict | Case book, or the owner's position | Match |
|---|---|---|---|
| "Demeter grieves" (grief its own step) against "Persephone is underground", Greek question, gods tied to the parts of the world they stand for | Rivals, kind (ii) | Owner: kind (ii) | yes |
| The same, gods anchored to nothing | Kind (i), degenerate: neither can meet (F1) at any pair whatever the target | Owner: kind (ii) | **NO** (mismatch 2) |
| "Demeter's grief makes the cold", written with the same cut as "underground" | One account, not rivals | Owner's example | **depends on the writing** (mismatch 6) |
| Persephone against Freyr; grief against "sorrow" | One account, not rivals | Deutsch p.21: "the same core explanation"; the draft's departure recorded | yes |
| Tilt against myth, world question | Kind (i). Conflict at the equator and the far south; a test at the far south solves it, answer alone. After the sailor, the myth does not fit | Expected kind (i) in the south; N2 | yes |
| Tilt against myth, Greek question | Kind (ii): the tilt is "easy to vary" there | Deutsch: the tilt is the good explanation; N1, N4 | **not recorded** (mismatch 7) |
| N2: the myth against its southern variant, Greek question | Kind (ii) if the myth's cold part does not read place; **one account** if it does | The draft's N2 row: kind (ii) | **one writing fails** (mismatch 1) |
| N3: "its details … could be swapped" | Label swaps are one account and not rivals; only a change of cut, or of claims outside \(C\), gives a rival | The draft's N3 row: "a rival of kind (ii)" | **partial** (mismatch 6) |
| N2: does the amended myth explain the world's seasons? | No: (F1) fails at the far south | N2: No | yes |

**M3, redescription and cutting**

| Question | Draft's verdict | Case book, or the owner's position | Match |
|---|---|---|---|
| One explanation in two wordings (the variety effect renamed) | One account, not rivals, no problem | Owner's refinement (1) | yes |
| Two cuttings with one answer profile, both accounts: a mechanism (two components) against a rule (one) | Not one account. If nobody offers one in place of the other, no problem. If someone does: rivals, kind (ii), each "easy to vary". The finer question (set the variety effect directly) makes it kind (i): the mechanism is an account there and the rule is not | No case. Nearest is N7: fuller and leaner accounts both explain, and neither is weakened | **partial.** The finer true account is called "easy to vary" because a compatible coarsening was offered in its place; only "offered in place" guards against it (the draft's own N7 watch) |
| One answer at every pair, one anchor, different relations | Kind (i): four conflicts through (F1). The answer alone does not solve it | The REASON's step "one answer at every pair, so no conflict" | **refutes the step** (mismatch 2) |
| Spring against a slack cable: the same answers, different anchors, the cable not an account | Kind (ii). No test is sure to solve it, but the actual relations at push = 1 refute the cable inside \(C\) | The draft's "The remedy is a finer contract" | **scope** (mismatch 7) |

**M4, D3-T**

| Question | Draft's verdict | Case book | Match |
|---|---|---|---|
| Is the discarded design a rival that fits? | Not a problem: it fails at a tried setting | D3-T: No; "a design the tester threw out cannot be one of them" | yes |
| Does passing settle the untried setting? | Yes, once "only two designs exist" is held as a receipt: the kept design's answer there is derived, and every design lit there fails, 8 of 8. Without that receipt, a conjectured third design poses a kind-(i) problem | D3-T: "Passing therefore tells you which design you have" | yes (it needs the population fact counted as established) |

**M5, N25**

| Question | Draft's verdict | Case book, or the task | Match |
|---|---|---|---|
| Dog against turtle | One account, not rivals, no problem. This holds on both anchorings | Task: kind (ii). Case book: "the same empty claim … the difference between them is idle" | **NO against the task** (mismatch 5); yes against the case book |
| Does any of them explain? | No: each fails non-circular dependence | N25: none explains | yes |
| Dog against "the universe holds itself up" (a different cut) | Kind (ii) with real anchors. Kind (i), degenerate, with the dog anchored to nothing. No problem at all if a non-circular-dependence failure counts as established | — | ambiguous (mismatches 2 and 7) |

**M6, N1**

| Question | Draft's verdict | Case book, or the task | Match |
|---|---|---|---|
| Tomas with and without an idle sun god, nobody offering one in place of the other | Not rivals, no problem. The god does no work (both halves of W33.1's test pass) | N1: Tomas explains; the god is not part of it | yes |
| The same, offered in place of each other (the struck version put forward) | **Rivals (4 against 5 components), kind (ii), each "easy to vary"** | Task: "one account plus an idle commitment, not a problem" | **NO** (mismatch 4) |
| The god swapped for another god | One account | The draft's N1 row | yes |
| The god as a second route, or as an unfaithful part | Route: the removal half fails, and offered in place it is kind (ii). Unfaithful: not an account, and a degenerate kind (i) | Watched in W33.1 | as watched |

---

## 1. The machinery

`models/engine.py` adapts the correction-sticks analysis's `attack/fe.py`, its finite implementation of (E).

**Kept from `fe.py`.**
- Organizations, ports and components, and solutions by (O).
- A deleted component imposes the full relation.
- (A), (F2), (F1) with anchors and port translations, the third sentence of non-circular dependence, and non-vacuity.

**Added from Part II.** An edit that sets a port replaces the component that assigns it (D3:L103).

**Not modelled.** The first two sentences of non-circular dependence and grain, as in `fe.py`.

**The drafted terms, as the scripts read them.**
- **One account** is the content of W59.1's parenthesis: a bijection of active components, each pair with one anchor (the same components of \(D\), translated onto the same ports of \(D\)) and one kind on the stated set of pairs, and one answer profile there. The draft judges it on \(C\). The scripts also judge it on every admitted pair, to test a repair.
- **Rivals:** the same question, offered in place of each other, and not one account. "Offered" is a fact of history that each model supplies.
- **Conflict at \(x\)** means: for every assignment of relations to the target's components at \(x\), not both candidates meet (F1), (F2) and (A) there. The relations at \(x\) vary independently of the other pairs, as Derivation 3's proof has it ("supplied independently for each \((a,b)\)", D3:L568).
  - The space is "all" (every relation) in M1, M3 (c), M3 (d) and M4, and "functional" in M2, M3 (b), M5 and M6. M1's output (3) shows that the two spaces give the same conflict sets.
  - The engine also reports whether each candidate alone could meet the three conditions at \(x\). A conflict in which both could is marked PROPER, and one in which either could not is marked DEGENERATE.
- **Established:** a pair's answer (`'ans'`), or a pair's relations (`'full'`), held as a receipt.
- **Fits:** no established result shows a failure. Non-circular dependence is reported separately, and M5 also runs it as part of "fits".
- **Problem:** two rivals that both fit. Kind (i) if they conflict at some pair of \(C\), otherwise kind (ii).
- **"Solves whatever it shows":** for every possible outcome at the pair, at most one of the two still fits. It is checked with the relations established, and with the answer only.

**Nothing in the engine lists, counts or grades rivals.** The model scripts build families of candidates only as test harnesses for universal claims. Examples are W60.1's "every such candidate alike" and D3-T's "no such pair exists".

## 2. Notes on the models

**M1, the gardener** (`garden.py`, `m1_gardener.py`). The target, E0 and the two ways of writing the good rescue are those of the correction-sticks analysis. Emb-1 is the mechanism; Emb-2 is the changed rule.
- **The rescues.** E_good, E_bad, E_windy and E_patch are Emb-1 candidates whose variety component reads rain, wind and variety on one anchor (dvar). They differ only in when it fires.
- **What is established.** Only answers: the recorded summers, the shading test and the failed summer.
- **The separating pairs.** They are exactly the settings where "early" and "wet" disagree. Where the south bed is sunny, the answers differ. Where the south wall is shaded, both answer "north", and the rescues differ only in whether the variety effect is on (output (4)).
- **W60.1.** It is confirmed in the form stated: the result at the failed summer excludes exactly the candidates that give the failed answer there, and every one of them. It excludes nothing else, which is W60.1's own limit (output (6)).
- **The retreat.** It behaves as D3:L151 and D3:L159 say.
- **Section (8)** is the finding behind mismatch 1. On the record-only question every fitting Emb-1 candidate is one account with every other: 2,016 pairs, output (9).

**M2, the seasons** (`seasons.py`, `m2_seasons.py`).
- **The target** is a tilted, steady axis (dexp), the warmth received (dins) and the season (dseason). Every myth component needs an anchor (Part IV), so two readings were run.
  - **R-real:** each god stands for the part of the world whose role it claims. Persephone's absence is the low sun, and Demeter's grief is the warmth received.
  - **R-none:** anchored to nothing.
- **The myths are accounts of the Greek question under R-real.** That turns on the unmodelled first sentences of non-circular dependence, which the draft's N3 row relies on. It does not touch any rival verdict.
- **The tilt against the southern variant.** It conflicts at the far south through a shared component of the target (dexp) reached through different ports. That is neither of the two routes the definition names ("as when …"). The definition's "whatever the target's relations" quantifier catches it, as it should.

**M3, redescription and cutting.**
- (b) repeats the analysis's "same answers, different bookkeeping" as a question about rivals.
- (c) is the analysis's a5 pair ("var fires on early" against "early and the south bed sunny"), rebuilt with one anchor.
- (d) is a new door model.

**M4, D3-T.** "Only two designs exist" enters as a derived receipt for the kept design's answer at the untried setting (D3:L391: "A receipt is a derivation tree over leaves"). With it the draft's verdict matches the case. Without it, a conjectured third design would pose a kind-(i) problem, which is the case's own "Ivo would need two designs that both pass".

**M5, N25.** The holder is a port of the target that no admitted change reaches. The dog and the turtle are the same organization with a different port name.

**M6, N1.** The target makes the steady axis explicit (dspin). W33.1's two-halved test gives the three readings its CASES AT RISK names:
- idle: both halves pass;
- a redundant route: the removal half fails;
- interference: the addition half fails.

## 3. The mismatches, with the evidence and the repairs tested

**1. Same-cut rivals that differ only outside \(C\) are one account on \(C\).**
- *Lemma [PROVED].* Suppose a bijection pairs the active components of two candidates for \(p\) with one anchor each, and the two conflict at no pair of \(C\). Then they are one account on \(C\) in the sense of W59.1's parenthesis.
  - *Proof.* Take \(x\in C\). No conflict at \(x\) means that some relations of the target at \(x\) let both meet (F1) and (A). (F1) makes each paired component's relation under the pair equal to the projection of the one anchor onto the same ports. So the paired relations coincide at \(x\), and (A) makes the answers equal. ∎
  - *Checked [COMPUTED].* On the record question, 2,016 of 2,016 no-conflict pairs among the fitting Emb-1 candidates are one account (M1 (9)).
- *Consequence.* Under the draft, a kind-(ii) problem needs rivals cut differently: another number of active components, or other anchors. "Wet spring" against "windy spring", and "early variety" against "wet spring", on the record-only question are one account, not rivals (M1 (8)).
- *Why this contradicts the owner.* Refinement (2) calls such pairs rivals that differ nowhere the question covers, and "the mark of an easily varied explanation". The owner's own example survives only because grief is written as its own step.
- *It also makes the draft's N2 row depend on the writing.* The southern variant is kind (ii) against "dem", and one account against "dem_p", the same myth whose cold part also reads the place (M2 (2)).
- *Repair tested.* In the rivals sentence, judge "one account" on every admitted change, inside \(C\) or not, and not on \(C\) alone. For example, "…and some admitted change, inside \(C\) or not, separates them, in their answers or in the relations of their paired components: they are not one account in the sense of Derivation 2 on every admitted change."
  - Results: on the record question, E_good against E_bad and E_bad against E_windy become kind (ii) (M1 (8)). N2 becomes kind (ii) on both writings (M2 (5)).
  - Label swaps (Persephone against Freyr, grief against "sorrow") and dog against turtle stay one account, since no admitted change separates them anywhere.
  - This is Derivation 2's Consequence read as the test of a real rival. A claim that one is right "must supply" the separating change, and for kind (ii) that change lies outside \(C\).
  - Cost: kind (ii) then speaks of changes the question does not admit, though the verdicts inside \(p\) do not use them.

**2. "Conflict" counts a pair where one candidate cannot meet the conditions whatever the target does.**
- A component anchored to no component of the target meets (F1) nowhere, because its anchor's projection is the full relation. "Not both meet" is then true at every pair, so the pair of rivals is kind (i) and a "test" anywhere "solves" it.
- This happens to Demeter against Persephone under R-none (M2 (3)), to the dog against the self-holding universe with the dog anchored to nothing (M5), and to the unfaithful sun god (M6).
- The draft's claims about each kind stay true: W59.1's REASON says the definition was built for that. But the owner's example then comes out kind (i) under that anchoring.
- **The REASON's step is invalid.** 01:L216 says "On the Greek question they give one answer at every pair, so they conflict at no pair of \(C\)". The converse is what holds (01:L206). M3 (c) is a counterexample with real anchors: one answer at every pair, and a conflict through (F1) at four.
- *Two ways to fix it.*
  - (a) Keep the definition, and correct the REASON. The owner's example is kind (ii) when each god is tied to the part of the world whose role it claims, and grief is its own step.
  - (b) Define conflict as "their answers there differ, or each could meet (F1), (F2) and (A) there and no relations of the target there let both". Kind (ii)'s "no test the question admits is sure to solve the problem" must then read "no established answer", because a test of relations is sure to refute a candidate that cannot meet the conditions.
  - Option (b) makes the owner's example kind (ii) under both anchorings. I have not run (b) through the scripts [I].

**3. The kind-(i) test must establish the target's relations where the answers agree.**
- M1 (4): at 4 of the 8 separating pairs, the answer alone leaves both rescues fitting in 11 of 64 outcomes. M3 (c): at all 4.
- Suggested wording: "Establishing what the target does there, its relations and not only its answer, is then a test that solves the problem whatever it shows".
- In practice the gardener's decisive test is a sunny-south setting, where the answer suffices.

**4. Idle commitments make rivals.**
- Derivation 2 pairs all active components. So Tomas with an idle god and Tomas without it are never one account, and if one is offered in place of the other, they are kind-(ii) rivals, each "easy to vary" (M6).
- The draft keeps N1 right only through "no candidate is offered in place of Tomas's" (01:L225). A critic who puts the struck version forward ("strike it out and the account works exactly as before") is offering it in place.
- *Repair tested:* before asking whether two candidates are one account, set aside every single commitment that does no work by itself (W33.1's test). Idle god: set aside, one account with Tomas. Route and unfaithful readings: nothing set aside, still rivals (M6, last block).
- An infinite \(\Gamma\) needs care, since a block of idle commitments can be critical (D3:L311). The repair is stated for single commitments.

**5. N25: dog against turtle.**
- The draft gives one account, not rivals, on both anchorings (M5), and repair 1 does not change this.
- The task expected kind (ii). The case book's main verdict is with the draft ("As explanations they make the same empty claim … the difference between them is idle"). Only its gloss "In words, yes … both stories cannot be true" leans the other way.
- Kind (ii) here would need the label to count as a claim, which Part 0 ("whatever labels anyone attaches to them"), Derivation 1 and defeat condition (C) (D3:L534) exclude. It would also clash with the owner's refinement (1): a redescription is one explanation.
- The dog story does have a kind-(ii) rival in a story cut differently: "the universe holds itself up".

**6. Case rows that go beyond the definitions.**
- *N3 (01:L231).* "Its details … could be swapped for others … is a rival of kind (ii)". Swapping which gods or what bargain is a label swap: one account (M2, dem against sorrow, und against freyr). Only swapping "why grief brings cold" for a mechanism with another cut gives a rival. The row should say "some of its details".
- *N2 (01:L229).* This holds only on one writing, until repair 1.
- *The owner's example (01:L216).* Kind (ii) only with grief as its own step. The REASON says so; a reader should know that the verdict rests on the cut.

**7. Consequences to record, or wording to scope.**
- *The tilt is "easy to vary" on the Greek question* (M2 (2): tilt against the myth, kind (ii)). The sources note should record this departure: Deutsch's paradigm of a good explanation is, in the defined sense, easy to vary relative to a myth on a question the myth fits. The draft's LOSS names the symmetry but not this case.
- *"The remedy is a finer contract, which is a new question"* (01:L179). It follows "Where both rivals are accounts on \(C\)", but can be read as the remedy for kind (ii) in general. In M3 (d) one rival is not an account, and establishing the relations at a pair inside \(C\) refutes it. The sentence should be scoped to the case where both are accounts.
- *"Fits" and failures derivable from the candidate alone.* Non-circular dependence, and (F1) for a component anchored to nothing, can be shown without any test. The draft does not say whether such a derivation is an "established result". In N25 the stories pose a problem or not according to this (M5: "with NonCircular counted in 'fits'").

**Also noted, not a mismatch.**
- The conflict routes the draft names are not exhaustive: M2's tilt against the southern variant conflicts through neither. The definition's quantifier is what carries the claims, as the REASON intends.
- A compatible coarsening offered in place of a finer account (M3 (b)) makes each "easy to vary". The draft already watches this under N7 (01:L236–L239 and L473–L476).

## 4. Does any verdict need a list of all rivals, a count or a grade?

**No.** Every verdict above was reached from four things:
- pairwise relations: rival, conflict and fit;
- universal statements over the pairs of \(C\), and over the target's possible relations at one pair;
- a single exhibited rival, for "easy to vary";
- (A), for W60.1's "every such candidate alike".

Where the models enumerate candidates (M1 (6), M1 (9), M4's harness), they only test a universal claim that the draft proves without enumeration.

Three places come near, and none is a violation.
- **"Whatever the target's relations there"** quantifies over a space the theory does not declare: all relations, functional ones, or physically possible ones. It ranges over the target, not over rivals, and no verdict in these models changed with the space (M1 (3); the degenerate failures do not depend on it).
- **"Not easy to vary"** would need the finite set of rivals someone has offered, which is a record of offers. The draft never asserts it, and its LOSS accepts that an unchallenged candidate is not called easy to vary.
- **"Offered" and "conjectured"** are facts of history. This matches the owner's "two DISCOVERED rival explanations". W60.1 needs no record of failures, as the owner asked.

## 5. Files and re-running

`rivals/models/` in the session scratchpad:

| file | md5 |
|---|---|
| engine.py | f9e5d850e1c4866336b52a65f75da738 |
| garden.py | 8e47c50f61deb8c10b44b62d6def813f |
| seasons.py | 5e1545d1c8e391720aba87ed0f58587e |
| m1_gardener.py → m1_output.txt | cc46b73db5a9cbc234b7b8b24a1245a1 → ef1b69f80b8511f1aa28717d271a4ea6 |
| m2_seasons.py → m2_output.txt | 94805f76441065b7bf020c2bff472e42 → 9f8d79ace0f0d73f49b72a6e9e4dedcc |
| m3_redescription.py → m3_output.txt | 779008a38548aa4b830242413d227237 → 50f640715fed170a13d7f47ec517fa4a |
| m4_d3t.py → m4_output.txt | ea3add326335bef3f8b79173a64c8015 → fdc6330ee055f8e01b2bc740c390690b |
| m5_n25.py → m5_output.txt | 6a3c42c477d3beb89f41c80a044c6160 → 2f6f4b3d91ec4dba9efe223d89259322 |
| m6_n1.py → m6_output.txt | c693e0e0561b0d200c0fbba3a9cdba95 → 42f5153611c46d97d27efba424406a03 |

Run each script with `python3 <script>` from the models folder.

---

## Appendix: the outputs, verbatim

### `m1_gardener.py` → `m1_output.txt`

```text
====================================================================================================
M1  THE GARDENER
====================================================================================================
p: contract C_full (16 settings), baseline dry/calm/late/sunS
established (answers only): dry/calm/late/sunS -> ['S'], dry/calm/late/shadeS -> ['N'], wet/windy/early/sunS -> ['N']

----------------------------------------------------------------------------------------------------
(1) each candidate: fits what is established? NonCircular on C_full? Account on p?
----------------------------------------------------------------------------------------------------
  E0       fits=False NC=True  Account(p)=False A+F2+F1[sun]@dry/calm/early/sunS A+F2+F1[sun]@dry/windy/early/sunS A+F2+F1[sun]@wet/calm/early/sunS A+F2+F1[sun]@wet/windy/early/sunS
  E_good   fits=True  NC=True  Account(p)=True  
  E_bad    fits=True  NC=True  Account(p)=False A+F2+F1[var]@dry/calm/early/sunS F2+F1[var]@dry/calm/early/shadeS A+F2+F1[var]@dry/windy/early/sunS F2+F1[var]@dry/windy/early/shadeS
  E_windy  fits=True  NC=True  Account(p)=False A+F2+F1[var]@dry/calm/early/sunS F2+F1[var]@dry/calm/early/shadeS A+F2+F1[var]@dry/windy/late/sunS F2+F1[var]@dry/windy/late/shadeS
  E_patch  fits=True  NC=True  Account(p)=False A+F2+F1[var]@dry/calm/early/sunS F2+F1[var]@dry/calm/early/shadeS A+F2+F1[var]@dry/windy/early/sunS F2+F1[var]@dry/windy/early/shadeS
  E_rule   fits=True  NC=True  Account(p)=True  

----------------------------------------------------------------------------------------------------
(2) the draft's verdict on pairs offered in place of each other, on p (space: all relations)
----------------------------------------------------------------------------------------------------
  E_good vs E_bad
    same question: True
    one account (Derivation 2): False  [answer profiles differ on the pairs compared]
    offered in place of each other: True  -> rivals: True
    fit what is established: (True, True)
      conflict at dry/calm/early/sunS        PROPER     routes: answers differ; one anchor, different relations (var/var)
      conflict at dry/calm/early/shadeS      PROPER     routes: one anchor, different relations (var/var)
      conflict at dry/windy/early/sunS       PROPER     routes: answers differ; one anchor, different relations (var/var)
      conflict at dry/windy/early/shadeS     PROPER     routes: one anchor, different relations (var/var)
      conflict at wet/calm/late/sunS         PROPER     routes: answers differ; one anchor, different relations (var/var)
      conflict at wet/calm/late/shadeS       PROPER     routes: one anchor, different relations (var/var)
      conflict at wet/windy/late/sunS        PROPER     routes: answers differ; one anchor, different relations (var/var)
      conflict at wet/windy/late/shadeS      PROPER     routes: one anchor, different relations (var/var)
    VERDICT: PROBLEM for p, kind (i)
  E_good vs E_windy
    same question: True
    one account (Derivation 2): False  [answer profiles differ on the pairs compared]
    offered in place of each other: True  -> rivals: True
    fit what is established: (True, True)
      conflict at dry/calm/early/sunS        PROPER     routes: answers differ; one anchor, different relations (var/var)
      conflict at dry/calm/early/shadeS      PROPER     routes: one anchor, different relations (var/var)
      conflict at dry/windy/late/sunS        PROPER     routes: answers differ; one anchor, different relations (var/var)
      conflict at dry/windy/late/shadeS      PROPER     routes: one anchor, different relations (var/var)
      conflict at wet/calm/early/sunS        PROPER     routes: answers differ; one anchor, different relations (var/var)
      conflict at wet/calm/early/shadeS      PROPER     routes: one anchor, different relations (var/var)
      conflict at wet/windy/late/sunS        PROPER     routes: answers differ; one anchor, different relations (var/var)
      conflict at wet/windy/late/shadeS      PROPER     routes: one anchor, different relations (var/var)
    VERDICT: PROBLEM for p, kind (i)
  E_bad vs E_windy
    same question: True
    one account (Derivation 2): False  [answer profiles differ on the pairs compared]
    offered in place of each other: True  -> rivals: True
    fit what is established: (True, True)
      conflict at dry/windy/late/sunS        PROPER     routes: answers differ; one anchor, different relations (var/var)
      conflict at dry/windy/late/shadeS      PROPER     routes: one anchor, different relations (var/var)
      conflict at dry/windy/early/sunS       PROPER     routes: answers differ; one anchor, different relations (var/var)
      conflict at dry/windy/early/shadeS     PROPER     routes: one anchor, different relations (var/var)
      conflict at wet/calm/late/sunS         PROPER     routes: answers differ; one anchor, different relations (var/var)
      conflict at wet/calm/late/shadeS       PROPER     routes: one anchor, different relations (var/var)
      conflict at wet/calm/early/sunS        PROPER     routes: answers differ; one anchor, different relations (var/var)
      conflict at wet/calm/early/shadeS      PROPER     routes: one anchor, different relations (var/var)
    VERDICT: PROBLEM for p, kind (i)
  E_good vs E_patch
    same question: True
    one account (Derivation 2): False  [answer profiles differ on the pairs compared]
    offered in place of each other: True  -> rivals: True
    fit what is established: (True, True)
      conflict at dry/calm/early/sunS        PROPER     routes: answers differ; one anchor, different relations (var/var)
      conflict at dry/calm/early/shadeS      PROPER     routes: one anchor, different relations (var/var)
      conflict at dry/windy/early/sunS       PROPER     routes: answers differ; one anchor, different relations (var/var)
      conflict at dry/windy/early/shadeS     PROPER     routes: one anchor, different relations (var/var)
      conflict at wet/calm/early/sunS        PROPER     routes: answers differ; one anchor, different relations (var/var)
      conflict at wet/calm/early/shadeS      PROPER     routes: one anchor, different relations (var/var)
    VERDICT: PROBLEM for p, kind (i)
  E_good vs E0
    same question: True
    one account (Derivation 2): False  [active components 2 vs 1: no bijection]
    offered in place of each other: True  -> rivals: True
    fit what is established: (True, False)
    VERDICT: rivals; NO problem: E0 does not fit what is established
  E_bad vs E0
    same question: True
    one account (Derivation 2): False  [active components 2 vs 1: no bijection]
    offered in place of each other: True  -> rivals: True
    fit what is established: (True, False)
    VERDICT: rivals; NO problem: E0 does not fit what is established

----------------------------------------------------------------------------------------------------
(3) does the space of target relations matter? conflict pairs, all relations vs functional
----------------------------------------------------------------------------------------------------
  E_good   vs E_bad    all:  8  functional:  8  same set: True
  E_good   vs E_windy  all:  8  functional:  8  same set: True
  E_bad    vs E_windy  all:  8  functional:  8  same set: True
  E_good   vs E_patch  all:  6  functional:  6  same set: True

----------------------------------------------------------------------------------------------------
(4) E_good vs E_bad: which pairs of C separate them, and does a test there solve the problem
    "whatever it shows"? (full = the target's relations there are established; ans = only its answer)
----------------------------------------------------------------------------------------------------
  dry/calm/early/sunS      routes: answers differ; one anchor, different relations (var/var)  full: solves=True   ans: solves=True  (outcomes where both still fit: 0 of 64)
  dry/calm/early/shadeS    routes: one anchor, different relations (var/var)                  full: solves=True   ans: solves=False (outcomes where both still fit: 11 of 64)
  dry/windy/early/sunS     routes: answers differ; one anchor, different relations (var/var)  full: solves=True   ans: solves=True  (outcomes where both still fit: 0 of 64)
  dry/windy/early/shadeS   routes: one anchor, different relations (var/var)                  full: solves=True   ans: solves=False (outcomes where both still fit: 11 of 64)
  wet/calm/late/sunS       routes: answers differ; one anchor, different relations (var/var)  full: solves=True   ans: solves=True  (outcomes where both still fit: 0 of 64)
  wet/calm/late/shadeS     routes: one anchor, different relations (var/var)                  full: solves=True   ans: solves=False (outcomes where both still fit: 11 of 64)
  wet/windy/late/sunS      routes: answers differ; one anchor, different relations (var/var)  full: solves=True   ans: solves=True  (outcomes where both still fit: 0 of 64)
  wet/windy/late/shadeS    routes: one anchor, different relations (var/var)                  full: solves=True   ans: solves=False (outcomes where both still fit: 11 of 64)

----------------------------------------------------------------------------------------------------
(5) the seed trial is run: the target's answer at dry/calm/early/sunS is established
----------------------------------------------------------------------------------------------------
  E0       fits=False
  E_good   fits=True
  E_bad    fits=False
  E_windy  fits=False
  E_patch  fits=False
  E_rule   fits=True
  E_good vs E_bad after the test:
    same question: True
    one account (Derivation 2): False  [answer profiles differ on the pairs compared]
    offered in place of each other: True  -> rivals: True
    fit what is established: (True, False)
    VERDICT: rivals; NO problem: E_bad does not fit what is established

----------------------------------------------------------------------------------------------------
(6) W60.1 "a failed answer stays failed": test harness over 1,041 candidates for p
    (Emb-1: 4 sun' maps x all 256 predicates on V,W,Wi; Emb-2: all 16 rules on V,Sun; E0).
    The harness only tests the universal claim; the draft's claim itself lists nothing.
----------------------------------------------------------------------------------------------------
  candidates answering S at the failed summer (repeat the failed answer): 265
    of these, fit what is established: 0   are an account on any of 22 contracts holding it: 0
  candidates answering N there: 776; excluded by the failed-summer result alone: 0
  LIMIT (not claimed by W60.1): candidates that fit and repeat E0's error at another early/sunS setting: 56 of 66
    e.g. E1[id,00000001], wrong as E0 at dry/calm/early/sunS, dry/windy/early/sunS, wet/calm/early/sunS
    offered in place of E_good -> PROBLEM for p, kind (i) ; conflict pairs: 6
  after the seed trial: fit 34; still repeating E0's error somewhere untested: 24; at the seed trial: 0

----------------------------------------------------------------------------------------------------
(7) the retreat: "my explanation only covered the summers seen" (contract C_narrow = {B0, SHADE})
----------------------------------------------------------------------------------------------------
  E0 for p': Account = True
  E0 for p : Account = False  (A+F2+F1[sun]@dry/calm/early/sunS A+F2+F1[sun]@dry/windy/early/sunS A+F2+F1[sun]@wet/calm/early/sunS);  fits what is established = False
  E0-for-p' offered in place of E_good-for-p -> not rivals: candidates for different questions
  E0 offered again for p, in place of E_good -> rivals; NO problem: E0 does not fit what is established
  E0 an account on any of the 22 contracts holding the failed summer? False
  E0 an account on the narrowed contract, where the failed summer is omitted? True  (a different question)

----------------------------------------------------------------------------------------------------
(8) the same pair on the record-only question p_rec (C = {B0, SHADE, FSTAR})
----------------------------------------------------------------------------------------------------
  E_good vs E_bad on p_rec
    same question: True
    one account (Derivation 2): True  [paired: sun1~sun1, var~var]
    offered in place of each other: True  -> rivals: False
    VERDICT: not rivals: one account (paired: sun1~sun1, var~var)
  E_bad vs E_windy on p_rec
    same question: True
    one account (Derivation 2): True  [paired: sun1~sun1, var~var]
    offered in place of each other: True  -> rivals: False
    VERDICT: not rivals: one account (paired: sun1~sun1, var~var)
  accounts of p_rec: E_good True, E_bad True, E_windy True
  REPAIR tested: "one account" judged on every admitted setting (all 16), not on C_rec:
  E_good vs E_bad on p_rec, repaired rule
    same question: True
    one account (Derivation 2): False  [answer profiles differ on the pairs compared]
    offered in place of each other: True  -> rivals: True
    fit what is established: (True, True)
      conflict at no pair of C
    VERDICT: PROBLEM for p, kind (ii)
  E_bad vs E_windy on p_rec, repaired rule
    same question: True
    one account (Derivation 2): False  [answer profiles differ on the pairs compared]
    offered in place of each other: True  -> rivals: True
    fit what is established: (True, True)
      conflict at no pair of C
    VERDICT: PROBLEM for p, kind (ii)

----------------------------------------------------------------------------------------------------
(9) same-cut lemma, checked on the harness: two Emb-1 candidates (paired components, one anchor each)
    that conflict at no pair of a contract are one account on it. Contracts: C_rec and C_full.
----------------------------------------------------------------------------------------------------
  C_rec  pairs of fitting sun'=id candidates with no conflict on the contract: 2016; of these NOT one account: 0
  C_full pairs of fitting sun'=id candidates with no conflict on the contract: 0; of these NOT one account: 0
```

### `m2_seasons.py` → `m2_output.txt`

```text
====================================================================================================
M2  THE SEASONS
====================================================================================================

----------------------------------------------------------------------------------------------------
(1) each candidate: Account on p_greek, on p_world; fits the Greek-era results; fits after the sailor
----------------------------------------------------------------------------------------------------
  tilt         greek=True  world=True  fitsG=True  fitsS=True   world fails: 
  dem          greek=True  world=False fitsG=True  fitsS=False  world fails: A+F2+F1[sched]@E,H1 A+F2+F1[sched]@E,H2 A+F2+F1[sched]@S,H1
  dem_p        greek=True  world=False fitsG=True  fitsS=False  world fails: A+F2+F1[sched]@E,H1 A+F2+F1[sched]@E,H2 A+F2+F1[sched]@S,H1
  sorrow       greek=True  world=False fitsG=True  fitsS=False  world fails: A+F2+F1[sched]@E,H1 A+F2+F1[sched]@E,H2 A+F2+F1[sched]@S,H1
  south        greek=True  world=False fitsG=True  fitsS=True   world fails: A+F2+F1[sched]@E,H1 A+F2+F1[sched]@E,H2 F2+F1[gcold,sched]@S,H1
  und          greek=True  world=False fitsG=True  fitsS=False  world fails: A+F2+F1[sched]@E,H1 A+F2+F1[sched]@E,H2 A+F2+F1[sched]@S,H1
  dem2         greek=True  world=False fitsG=True  fitsS=False  world fails: A+F2+F1[bargain]@E,H1 A+F2+F1[bargain]@E,H2 A+F2+F1[bargain]@S,H1
  freyr        greek=True  world=False fitsG=True  fitsS=False  world fails: A+F2+F1[war]@E,H1 A+F2+F1[war]@E,H2 A+F2+F1[war]@S,H1
  dem[R-none]  greek=False world=False fitsG=True  fitsS=False  world fails: F1[gcold,griefc,sched]@N,H1 F1[gcold,griefc,sched]@N,H2 A+F2+F1[gcold,griefc,sched]@E,H1
  und[R-none]  greek=False world=False fitsG=True  fitsS=False  world fails: F1[cold,sched]@N,H1 F1[cold,sched]@N,H2 A+F2+F1[cold,sched]@E,H1
  R-none myths on p_greek fail: F1[gcold,griefc,sched]@N,H1 F1[gcold,griefc,sched]@N,H2

----------------------------------------------------------------------------------------------------
(2) the draft on p_greek (Greek-era results; "one account" judged on C = the Greek pairs)
----------------------------------------------------------------------------------------------------
  dem vs und
    same question: True
    one account (Derivation 2): False  [active components 3 vs 2: no bijection]
    offered in place of each other: True  -> rivals: True
    fit what is established: (True, True)
      conflict at no pair of C
    VERDICT: PROBLEM for p, kind (ii)
  und vs dem2
    same question: True
    one account (Derivation 2): True  [paired: cold~griefcold, sched~bargain]
    offered in place of each other: True  -> rivals: False
    VERDICT: not rivals: one account (paired: cold~griefcold, sched~bargain)
  und vs freyr
    same question: True
    one account (Derivation 2): True  [paired: cold~warmth, sched~war]
    offered in place of each other: True  -> rivals: False
    VERDICT: not rivals: one account (paired: cold~warmth, sched~war)
  dem vs sorrow
    same question: True
    one account (Derivation 2): True  [paired: gcold~scold, griefc~sorrowc, sched~sched]
    offered in place of each other: True  -> rivals: False
    VERDICT: not rivals: one account (paired: gcold~scold, griefc~sorrowc, sched~sched)
  tilt vs dem
    same question: True
    one account (Derivation 2): False  [no pairing with one anchor]
    offered in place of each other: True  -> rivals: True
    fit what is established: (True, True)
      conflict at no pair of C
    VERDICT: PROBLEM for p, kind (ii)
  tilt vs und
    same question: True
    one account (Derivation 2): False  [active components 3 vs 2: no bijection]
    offered in place of each other: True  -> rivals: True
    fit what is established: (True, True)
      conflict at no pair of C
    VERDICT: PROBLEM for p, kind (ii)
  dem vs south
    same question: True
    one account (Derivation 2): False  [no pairing with one anchor]
    offered in place of each other: True  -> rivals: True
    fit what is established: (True, True)
      conflict at no pair of C
    VERDICT: PROBLEM for p, kind (ii)
  dem_p vs south
    same question: True
    one account (Derivation 2): True  [paired: gcold~gcold, griefc~griefc, sched~sched]
    offered in place of each other: True  -> rivals: False
    VERDICT: not rivals: one account (paired: gcold~gcold, griefc~griefc, sched~sched)

----------------------------------------------------------------------------------------------------
(3) R-none: the gods anchored to nothing (Part IV still requires an anchor)
----------------------------------------------------------------------------------------------------
  dem[R-none] vs und[R-none]
    same question: True
    one account (Derivation 2): False  [active components 3 vs 2: no bijection]
    offered in place of each other: True  -> rivals: True
    fit what is established: (True, True)
      conflict at N,H1                       DEGENERATE routes: NONE of the two named routes
         DEGENERATE (dem[R-none] and und[R-none] cannot meet the three there whatever the target)
      conflict at N,H2                       DEGENERATE routes: NONE of the two named routes
         DEGENERATE (dem[R-none] and und[R-none] cannot meet the three there whatever the target)
    VERDICT: PROBLEM for p, kind (i)
  tilt vs dem[R-none]
    same question: True
    one account (Derivation 2): False  [no pairing with one anchor]
    offered in place of each other: True  -> rivals: True
    fit what is established: (True, True)
      conflict at N,H1                       DEGENERATE routes: NONE of the two named routes
         DEGENERATE (dem[R-none] cannot meet the three there whatever the target)
      conflict at N,H2                       DEGENERATE routes: NONE of the two named routes
         DEGENERATE (dem[R-none] cannot meet the three there whatever the target)
    VERDICT: PROBLEM for p, kind (i)
  test at N,H2 (full) solves dem[R-none] vs und[R-none]? True ; (answer only)? False

----------------------------------------------------------------------------------------------------
(4) the draft on p_world, before the sailor (tilt against the myth), and after
----------------------------------------------------------------------------------------------------
  tilt vs dem
    same question: True
    one account (Derivation 2): False  [answer profiles differ on the pairs compared]
    offered in place of each other: True  -> rivals: True
    fit what is established: (True, True)
      conflict at E,H1                       PROPER     routes: answers differ
      conflict at E,H2                       PROPER     routes: answers differ
      conflict at S,H1                       PROPER     routes: answers differ
      conflict at S,H2                       PROPER     routes: answers differ
    VERDICT: PROBLEM for p, kind (i)
    test at E,H1  full solves=True  ans solves=True
    test at E,H2  full solves=True  ans solves=True
    test at S,H1  full solves=True  ans solves=True
    test at S,H2  full solves=True  ans solves=True
  after the sailor's report:
  tilt vs dem
    VERDICT: rivals; NO problem: dem does not fit what is established
  dem_p vs south
    VERDICT: PROBLEM for p, kind (i)
  tilt vs south
    same question: True
    one account (Derivation 2): False  [answer profiles differ on the pairs compared]
    offered in place of each other: True  -> rivals: True
    fit what is established: (True, True)
      conflict at E,H1                       PROPER     routes: answers differ
      conflict at E,H2                       PROPER     routes: answers differ
      conflict at S,H1                       PROPER     routes: NONE of the two named routes
      conflict at S,H2                       PROPER     routes: NONE of the two named routes
    VERDICT: PROBLEM for p, kind (i)

----------------------------------------------------------------------------------------------------
(5) REPAIR tested: "one account" judged on every admitted pair (all six), for the Greek-question pairs
----------------------------------------------------------------------------------------------------
  dem vs und
    VERDICT: PROBLEM for p, kind (ii)
  und vs dem2
    VERDICT: not rivals: one account (paired: cold~griefcold, sched~bargain)
  und vs freyr
    VERDICT: not rivals: one account (paired: cold~warmth, sched~war)
  dem vs sorrow
    VERDICT: not rivals: one account (paired: gcold~scold, griefc~sorrowc, sched~sched)
  dem vs south
    VERDICT: PROBLEM for p, kind (ii)
  dem_p vs south
    VERDICT: PROBLEM for p, kind (ii)
  tilt vs dem
    VERDICT: PROBLEM for p, kind (ii)
```

### `m3_redescription.py` → `m3_output.txt`

```text
====================================================================================================
M3  REDESCRIPTION AND CUTTING
====================================================================================================

----------------------------------------------------------------------------------------------------
(a) one explanation, two wordings
----------------------------------------------------------------------------------------------------
    same question: True
    one account (Derivation 2): True  [paired: sun1~suncomp, var~boostcomp]
    offered in place of each other: True  -> rivals: False
    VERDICT: not rivals: one account (paired: sun1~suncomp, var~boostcomp)

----------------------------------------------------------------------------------------------------
(b) two cuttings with one answer profile: mechanism (Emb-1) against rule (Emb-2), on p = C_full
----------------------------------------------------------------------------------------------------
  Account on C_full: E_good True, E_rule True; answers agree at every pair: True
  not offered in place of each other:
    same question: True
    one account (Derivation 2): False  [active components 2 vs 1: no bijection]
    offered in place of each other: False  -> rivals: False
    VERDICT: not rivals: not offered in place of each other
  offered in place of each other:
    same question: True
    one account (Derivation 2): False  [active components 2 vs 1: no bijection]
    offered in place of each other: True  -> rivals: True
    fit what is established: (True, True)
      conflict at no pair of C
    VERDICT: PROBLEM for p, kind (ii)
  the finer contract (adds ovrD := 0/1 at every setting, 48 pairs):
    Account: E_good True ; E_rule False  A+F2+F1[rule]@dry/calm/late/sunS/set ovr=1 A+F2+F1[rule]@dry/calm/early/sunS/set ovr=0 A+F2+F1[rule]@dry/windy/late/sunS/set ovr=1
    on p_fine, offered in place of each other:
    VERDICT: PROBLEM for p, kind (i); conflict pairs: 8 (all at edits that set ovrD: True)

----------------------------------------------------------------------------------------------------
(c) one answer at every pair, one anchor, different relations
----------------------------------------------------------------------------------------------------
  answers agree at all 16 pairs: True ; Account on C_full: True / False
    same question: True
    one account (Derivation 2): False  [no pairing with one anchor; one anchor, not one kind on C (var vs var)]
    offered in place of each other: True  -> rivals: True
    fit what is established: (True, True)
      conflict at dry/calm/early/shadeS      PROPER     routes: one anchor, different relations (var/var)
      conflict at dry/windy/early/shadeS     PROPER     routes: one anchor, different relations (var/var)
      conflict at wet/calm/early/shadeS      PROPER     routes: one anchor, different relations (var/var)
      conflict at wet/windy/early/shadeS     PROPER     routes: one anchor, different relations (var/var)
    VERDICT: PROBLEM for p, kind (i)
  test at dry/calm/early/shadeS: full solves=True ; answer-only solves=False

----------------------------------------------------------------------------------------------------
(d) the door: a spring, and a slack cable offered in its place
----------------------------------------------------------------------------------------------------
  Account on the door question: spring True ; cable False  (F2+F1[pull,shut]@push=1)
    same question: True
    one account (Derivation 2): False  [no pairing with one anchor]
    offered in place of each other: True  -> rivals: True
    fit what is established: (True, True)
      conflict at no pair of C
    VERDICT: PROBLEM for p, kind (ii)
  a test at push=1: sure to solve, whatever it shows? relations established: False ; only the answer: False
  with the actual relations at push=1 established: spring fits True, cable fits False
```

### `m4_d3t.py` → `m4_output.txt`

```text
====================================================================================================
M4  D3-T, THE DISCARDED CONTROLLER
====================================================================================================
  design X (kept)                  Account(p)=True  fits tester results=True  fits with the population receipt=True
  design Y (discarded)             Account(p)=False fits tester results=False fits with the population receipt=False
  Z (a conjectured third design)   Account(p)=False fits tester results=True  fits with the population receipt=False

  Ivo: the discarded design Y, against the kept X (tester results):
    same question: True
    one account (Derivation 2): False  [answer profiles differ on the pairs compared]
    offered in place of each other: True  -> rivals: True
    fit what is established: (True, False)
    VERDICT: rivals; NO problem: design Y (discarded) does not fit what is established
  a conjectured Z against X, tester results only (population not established):
    same question: True
    one account (Derivation 2): False  [answer profiles differ on the pairs compared]
    offered in place of each other: True  -> rivals: True
    fit what is established: (True, True)
      conflict at A on, B on                 PROPER     routes: answers differ; one anchor, different relations (ctl/ctl)
    VERDICT: PROBLEM for p, kind (i)
    test at the untried setting: sure to solve (relations)=True (answer)=True
  Z against X, with the population receipt:
    same question: True
    one account (Derivation 2): False  [answer profiles differ on the pairs compared]
    offered in place of each other: True  -> rivals: True
    fit what is established: (True, False)
    VERDICT: rivals; NO problem: Z (a conjectured third design) does not fit what is established

  harness: all 16 lamp tables on (A, B) as candidates for p
    fit the tester results: 4; pairs of these that conflict at the untried setting: 4
    fit with the population receipt: 1 (T0010); such pairs: 0
    every table lit at the untried setting fails once the receipt is held: True (8 tables)
  (K3): if the population premise is put in question the derived result is not usable; then Z fits again: True
```

### `m5_n25.py` → `m5_output.txt`

```text
====================================================================================================
M5  N25, WHAT HOLDS THE UNIVERSE UP
====================================================================================================
  dog              answers [['yes'], ['yes']] ; NonCircular=False Account=False fits (answers)=True  fits (answers + NonCircular)=False
  turtle           answers [['yes'], ['yes']] ; NonCircular=False Account=False fits (answers)=True  fits (answers + NonCircular)=False
  self             answers [['yes'], ['yes']] ; NonCircular=False Account=False fits (answers)=True  fits (answers + NonCircular)=False
  dog[R-none]      answers [['yes'], ['yes']] ; NonCircular=False Account=False fits (answers)=True  fits (answers + NonCircular)=False
  turtle[R-none]   answers [['yes'], ['yes']] ; NonCircular=False Account=False fits (answers)=True  fits (answers + NonCircular)=False

  dog vs turtle (R-real)
    same question: True
    one account (Derivation 2): True  [paired: exists~exists, holds~holds]
    offered in place of each other: True  -> rivals: False
    VERDICT: not rivals: one account (paired: exists~exists, holds~holds)
    with NonCircular counted in "fits": not rivals: one account (paired: exists~exists, holds~holds)
  dog vs turtle (R-none)
    same question: True
    one account (Derivation 2): True  [paired: exists~exists, holds~holds]
    offered in place of each other: True  -> rivals: False
    VERDICT: not rivals: one account (paired: exists~exists, holds~holds)
    with NonCircular counted in "fits": not rivals: one account (paired: exists~exists, holds~holds)
  dog vs self (R-real)
    same question: True
    one account (Derivation 2): False  [active components 2 vs 1: no bijection]
    offered in place of each other: True  -> rivals: True
    fit what is established: (True, True)
      conflict at no pair of C
    VERDICT: PROBLEM for p, kind (ii)
    with NonCircular counted in "fits": rivals; NO problem: dog and self does not fit what is established
  dog vs self (dog R-none)
    same question: True
    one account (Derivation 2): False  [active components 2 vs 1: no bijection]
    offered in place of each other: True  -> rivals: True
    fit what is established: (True, True)
      conflict at push=0                     DEGENERATE routes: NONE of the two named routes
         DEGENERATE (dog[R-none] cannot meet the three there whatever the target)
      conflict at push=1                     DEGENERATE routes: NONE of the two named routes
         DEGENERATE (dog[R-none] cannot meet the three there whatever the target)
    VERDICT: PROBLEM for p, kind (i)
    with NonCircular counted in "fits": rivals; NO problem: dog[R-none] and self does not fit what is established
```

### `m6_n1.py` → `m6_output.txt`

```text
====================================================================================================
M6  N1, TOMAS AND THE SUN GOD
====================================================================================================
  Tomas                  Account=True  fits=True  
  Tomas+god[idle]        Account=True  fits=True  
  Tomas+god[route]       Account=True  fits=True  
  Tomas+god[unfaithful]  Account=False fits=True  F1[god]@N,H1 F1[god]@N,H2
  Tomas+zeus[idle]       Account=True  fits=True  

  W33.1's test: does the god do no work by itself (every support stays one when it is added and when removed)?
    Tomas+god[idle]        addition half=True  removal half=True  supports: {geo,heat,seas,spin}, {geo,god,heat,seas,spin}
    Tomas+god[route]       addition half=True  removal half=False supports: {geo,god,heat,seas}, {geo,heat,seas,spin}, {geo,god,heat,seas,spin}
    Tomas+god[unfaithful]  addition half=False removal half=True  supports: {geo,heat,seas,spin}

  Tomas vs Tomas+god[idle], offered in place of each other: False
    same question: True
    one account (Derivation 2): False  [active components 4 vs 5: no bijection]
    offered in place of each other: False  -> rivals: False
    VERDICT: not rivals: not offered in place of each other
  Tomas vs Tomas+god[idle], offered in place of each other: True
    same question: True
    one account (Derivation 2): False  [active components 4 vs 5: no bijection]
    offered in place of each other: True  -> rivals: True
    fit what is established: (True, True)
      conflict at no pair of C
    VERDICT: PROBLEM for p, kind (ii)
  Tomas vs Tomas+god[route], offered in place of each other: True
    same question: True
    one account (Derivation 2): False  [active components 4 vs 5: no bijection]
    offered in place of each other: True  -> rivals: True
    fit what is established: (True, True)
      conflict at no pair of C
    VERDICT: PROBLEM for p, kind (ii)
  Tomas vs Tomas+god[unfaithful], offered in place of each other: True
    same question: True
    one account (Derivation 2): False  [active components 4 vs 5: no bijection]
    offered in place of each other: True  -> rivals: True
    fit what is established: (True, True)
      conflict at N,H1                       DEGENERATE routes: NONE of the two named routes
         DEGENERATE (Tomas+god[unfaithful] cannot meet the three there whatever the target)
      conflict at N,H2                       DEGENERATE routes: NONE of the two named routes
         DEGENERATE (Tomas+god[unfaithful] cannot meet the three there whatever the target)
      conflict at E,H1                       DEGENERATE routes: NONE of the two named routes
         DEGENERATE (Tomas+god[unfaithful] cannot meet the three there whatever the target)
      conflict at E,H2                       DEGENERATE routes: NONE of the two named routes
         DEGENERATE (Tomas+god[unfaithful] cannot meet the three there whatever the target)
      conflict at S,H1                       DEGENERATE routes: NONE of the two named routes
         DEGENERATE (Tomas+god[unfaithful] cannot meet the three there whatever the target)
      conflict at S,H2                       DEGENERATE routes: NONE of the two named routes
         DEGENERATE (Tomas+god[unfaithful] cannot meet the three there whatever the target)
    VERDICT: PROBLEM for p, kind (i)
  Tomas+god[idle] vs Tomas+zeus[idle], offered in place of each other:
    same question: True
    one account (Derivation 2): True  [paired: geo~geo, god~zeus, heat~heat, seas~seas, spin~spin]
    offered in place of each other: True  -> rivals: False
    VERDICT: not rivals: one account (paired: geo~geo, god~zeus, heat~heat, seas~seas, spin~spin)

  REPAIR tested: set aside every single commitment that does no work by itself (W33.1's test) before
  asking whether the two are one account.
    Tomas+god[idle]        set aside: ['god']  one account with Tomas: (True, 'paired: geo~geo, heat~heat, seas~seas, spin~spin')
    Tomas+god[route]       set aside: -        one account with Tomas: (False, 'active components 4 vs 5: no bijection')
    Tomas+god[unfaithful]  set aside: -        one account with Tomas: (False, 'active components 4 vs 5: no bijection')
```
