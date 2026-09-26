# Difference reader 2: file 10 against file 11

Written by Claude (difference reader 2 of two, working independently).

## What I read, and blindness

- Read in full: file 10 (`Semantics/authority/10 Claude Fable Semantics - standalone theory.md`, 629 lines) and file 11 (`Semantics/authority/11 Claude Fable Semantics - standalone theory, revision 1.md`, 622 lines), side by side. I also ran a mechanical sentence-level diff (every sentence of each file checked for an exact match in the other) so that no changed sentence was missed. Every sentence the diff flagged appears below.
- Read: the case book (`Semantics/tests/S81 Case book - the 52 cases, situations and fixed verdicts, as the tested agent sees them.md`), after the sweep, to name the cases each CLAIM could touch.
- Read: lines 1–75 of brief `s81_1C_A.txt` (the instructions: the marks AGREE / DISAGREE / SPLIT / SILENT / CASE DISPUTED and "Same finding"), plus the first 20 lines and the heading list of `s81_1K_A.txt` (the same instructions). A grep of 1C for the word "mark" also printed one line of the embedded theory text (1C line 100), which is file 11's Part 0 line 27 word for word. I saw no returns.
- Seen by accident, names only: running `ls` on `Semantics/tests/` to find the case book printed the file names of the S81 plans (three), the case-book provenance file, "S81 Stage 1 testing - file 11 against every case.md" and "S81 Stage 2 audit - check the Stage 1 return.md". I did not open any of them. Listing `Semantics/authority/` also showed files 00 and 12 and NOT-IN-BUNDLE.md, none of them opened. Nothing under `Semantics/results/` was listed or opened except the two named briefs, which I opened by their exact paths.
- File 11's own header names "Semantics results S75". I did not open it.
- Seen by accident while writing, names only: after writing step 1, a check of my output file ran `ls -la` on the shared `s81_det/` folder. It listed other files there: f10.md, f11.md, reader1_O1-O26.md, reader1_O27-O52.md, reader2_O1-O26.md, reader2_O27-O52.md, wdiff.txt. I did not open, read or grep any of them. My step 1 list had already been written when I saw the names, and nothing in it or after it depends on them. My output file was also rewritten on disk between my writes, apparently by a process that restates prose in plain wording. I checked that the content (rulings, lines, quotes) is intact and made one fix: the S/X tally of D8.

Ruling key. **CLAIM**: file 11 asserts something file 10 does not, or stops asserting something file 10 does, or changes scope, conditions, quantifiers, definitions, or what follows from what. **WORDING**: the same claim in different words. **ORDER**: the same claim, moved. Within CLAIM I add a grade:
- **S** (substantive): new content that file 10 does not contain and does not entail, or content that contradicts or weakens file 10.
- **X** (explicit): a new sentence that file 10 does not state but that follows from file 10's definitions or restates something file 10 says in another place. It can still move a verdict, for example from SILENT or SPLIT to AGREE, by settling a point a reader of file 10 would have to derive.
- **meta**: a claim about the document, not about the theory.

Line numbers are the files' own line numbers. File 11 writes each paragraph on a single line, so one line often holds several places. "s2" means the second sentence on that line.

---

# STEP 1: the sweep (written before step 3)

## Part 0: front matter

**D1: revision note (new header)**
- F10: absent (nothing between the subtitle at line 3 and the rule at line 5). F11: line 5, "*Revision 1 (file 11), 22 September 2026. A rewrite of file 10 for coherence: ... One claim changes: Derivation 3 ... The three sentences that restated it (the answer to grievance 3, attack point (D), the Part XV entry) change with it. Nothing else changes in what is claimed.*"
- Ruling: **CLAIM (meta)**. These are new assertions about the document. "Nothing else changes in what is claimed" is false by this sweep: at least 40 other places below are CLAIMs. The list of places that restate Derivation 3 is also incomplete: see D30, D32, D60 and D67.
- Verdict effect: none through the theory. It names case O48, which could steer a reader who sees the header.

**D2: What this document claims, ¶1**
- F10 11: "Nothing in the definition of an explanation asks whether ..."; F11 13: "The definition never asks whether ..." and adds "(Part II, Derivation 1)".
- Ruling: **WORDING**. The same claim, with a pointer added.

**D3: What this document claims, ¶2 (the provenances)**
- F10 13: "*selected* — produced by blind variation and survival on a history of predictions —"; F11 15: "*selected*, produced by variation and survival on a history of encountered changes;". Also "distinguished by" becomes "told apart by", and "(Part IV)" is added.
- Ruling: **WORDING**, borderline. The front matter drops "blind" and "predictions". The body definition is the same in both files (F10 210 = F11 197: "a finite history H⊆C of edit–boundary pairs actually encountered"; "No member of the history represents t, H, or the survival condition", which is the blindness). File 11's front matter now matches that body text. What the theory commits to is unchanged.

**D4: What this document claims, ¶3 (questions)**
- F10 15 / F11 17. Dashes become commas; "distinguishes" becomes "separates"; "(Part III, Derivation 5)" is added.
- Ruling: **WORDING**.

**D5: What this document claims, ¶4 (constitutive conjecture)**
- F10 17 / F11 19. Identical, plus the new sentence "Part XV lists what would count."
- Ruling: **WORDING**. A pointer only.

**D6: What this document does not claim, ¶2**
- F10 23: "Fidelity in this semantics is over ..."; F11 25: "Fidelity is over ..." with "(Derivation 9)" added.
- Ruling: **WORDING**.

**D7: What this document does not claim, ¶3 (declared input where file 10 had an empty place)**
- F10 25: "It does not supply an objective aesthetics, a probability of truth, a merit function, or a ranking of thinkers. It supplies places where such things would go if anyone had them, and marks those places as empty."
- F11 27 s1–s2: "... a merit function, a measure of worth, or a ranking of thinkers. Where a claim needs one of these, the semantics takes it as a **declared input** and marks the place (Parts XI, XIV)."
- Ruling: **CLAIM (S)**. There are three changes. (a) "a measure of worth" joins the list. (b) File 10's position is an empty place. File 11 instead takes the missing item as a declared input, so a verdict is given relative to that input, and by Part XIV "Declared inputs" (D62) the verdict is unsettled when the input is absent. (c) The body of file 11 makes only the normative relation (worth and aesthetics) an input. It never says a probability of truth, a merit function or a ranking of thinkers is taken as a declared input, so this front-matter sentence says more than the body does.
- Verdict effect: possible on points about merit or worth. The result is SILENT when no input is stated and a conditional verdict when one is. Cases: O12 ("its merit is real"), O35 ("held in every way that mattered"), O38 ("Whether four seconds mattered to anyone is a different question").

**D8: What this document does not claim, ¶3 (division of credit, new sentence)**
- F10: absent. F11 27 s3: "It does not supply a division of credit among contributors beyond what a history establishes (Part XI)."
- Ruling: **CLAIM (S)**. This is the front-matter copy of the new credit rule in Part XI (D55). File 10 has no rule about credit anywhere.
- Verdict effect: yes. Cases: O20, O21, O26, O27, O32, O39, O40, O50 (see D55).

**D9: new section "What is primitive, what is an index, and what is derived"**
- F10: absent from Part 0. The content is at Part XIV 516–525 (Primitives; Indices, not primitives; Dependence order) and Derivation 6 (591–597). F11 31–33.
- Ruling: **ORDER**. This is Part XIV and Derivation 6 copied forward. Two notes. (a) "the normative relation N, taken as an input wherever a question invokes worth" carries the change from aesthetics to worth, which is counted once at D61. (b) "Everything else is derived" leaves out file 11's own fourth category, the declared inputs of Part XIV (D62). That is a tension inside file 11, not a claim about the theory.

**D10: Grievances, new opening sentence**
- F10: absent. F11 37: "Each answer points at the part of the document that carries it; the front matter states nothing the body does not state more exactly."
- Ruling: **CLAIM (meta)**. It is false at least at D7(c), where the body does not carry probability of truth, merit or ranking as declared inputs.
- Verdict effect: none.

**D11: Grievance 1** (F10 31–32 / F11 39). "which is exactly what" becomes "which is what"; "Declared kind-labels added" becomes "A declared label adds"; "edit-fidelity already finds it" becomes "fidelity finds it"; a Part II pointer is added. **WORDING**.

**D12: Grievance 2** (F10 34–35 / F11 41). "The semantics indexes every kind-claim to its level" becomes "Every kind-claim is indexed to its level." **WORDING**.

**D13: Grievance 3 (Derivation 3 restated)**
- F10 38: "There is a theorem below (Derivation 3) that selected transports are *always* underdetermined on unseen changes."
- F11 43: "Derivation 3 says that a selected transport is underdetermined by its history on an unseen change wherever its population admits a differing survivor there." "entirely independent" also becomes "independent".
- Ruling: **CLAIM (S)**. The quantifier changes from "always" to "wherever its population admits a differing survivor there". File 10's theorem says underdetermination holds at every unseen change. File 11 makes it conditional on the population.
- Verdict effect: yes. O48 (under file 10 there is always a differing survivor, against the fixed verdict "there is no alternative in that population"; under file 11 the premise is not met, as the fixed verdict says). O24 (a reachable alternative exists; AGREE under both files). O3 is touched only through surprise.

**D14: Grievance 4** (F10 40–41 / F11 45). "(non-vacuity, Part V)" is added and "and in the fidelity facts" becomes "and the fidelity facts". **WORDING**.

**D15: Grievance 5** (F10 43–44 / F11 47). "/" becomes a comma list, and "not about whether it is right" is dropped. **WORDING**.

**D16: Grievance 6** (F10 46–47 / F11 49). The quoted grievance loses "That is deflationary."; "things-with-persistence" becomes "persistent things"; "the semantics forbids that reduction in Part IV" becomes "Part IV forbids the reduction and Part XV names its refutation". **WORDING**, with a pointer added.

**D17: Grievance 7** (F10 49–50 / F11 51). The quoted grievance loses "This cannot handle mathematical explanation."; "This is worked in Part VII." becomes "(Part VII)". **WORDING**.

**D18: Grievance 8** (F10 52–53 / F11 53). "three distinct mathematical carriers and refuses to define any as another" becomes "get three distinct carriers, and none is defined as another". **WORDING**.

**D19: Grievance 9** (F10 55–56 / F11 55). The quoted grievance loses "Who says the selection happened?"; "(Parts IV, XII)" is added; "it is a label. The difference is the difference between a hypothesis and a stipulation." is dropped. **WORDING**: "A kind-label is not a claim about anything" is kept.

**D20: Grievance 10** (F10 58–59 / F11 57). "It is having it both ways deliberately" becomes "It is, deliberately"; "contracts can change" becomes "contracts change". **WORDING**.

**D21: Grievance 11** (F10 61–62 / F11 59). "(Part II)" is added; "What the semantics denies" becomes "What it denies"; the italics on *before* are dropped. **WORDING**.

**D22: "Where to attack this" moved into Part XV; Part XV rebuilt**
- F10: Part 0 lines 64–78 list (A)–(E) in full, and Part XV lines 531–545 is a separate, unlabelled list with no question-finding entry, ending "None of these is protected by notation ...".
- F11: Part 0 lines 61–63 keep a one-line summary of (A)–(E) and point to Part XV. Part XV lines 524–538 now carries labelled (A)–(E) plus "A mathematical error", with "in the order of how much falls" and "None ... is protected by notation ..." moved to its top (526).
- Ruling: **ORDER**, for everything except (A)'s table sentence (D24) and (D) (D23). Small wording inside the move: (B) keeps file 10's Part XV phrasing ("no transport can preserve") and drops Part 0's "satisfying component fidelity" and "it may be inadequate", which Part VII keeps as "as a place where it may not be". (C) keeps file 10's Part XV "This refutes Derivation 1 and reinstates correspondence as primitive" and drops Part 0's softer "would reopen the question". (E) gains "(against Derivation 5)". "This refutes sufficiency / necessity" becomes the labels. Both files already contained each of these claims.

**D23: attack point (D) and the Part XV entry (Derivation 3 restated)**
- F10 74: "Show either that a selected transport can be non-underdetermined on unseen changes (against Derivation 3), or ..."; F10 539: "**A non-fallible selected transport.** A selection history H⊊C whose survivor is determined on C∖H. This refutes Derivation 3."
- F11 534: "**(D) Genesis.** Any of three: a selected transport whose value at an unseen change is determined by its history although its population admits a differing survivor there (against Derivation 3; a population with no such survivor is the theorem's own qualification, not a refutation); ...". The Part 0 summary (F11 63) is neutral: "(D) the two provenances and the underdetermination of selected transports".
- Ruling: **CLAIM (S)**. Two changes. (a) What refutes the theorem is now conditioned on the population. A survivor determined off-history where the population has no alternative is expressly not a refutation. (b) The refuter is now pointwise ("at an unseen change"), where file 10 had "determined on C∖H". In file 11 the attack point and the Part XV entry are one passage, where file 10 had them in two places.
- Verdict effect: O48 (directly), O24.

**D24: attack (A), sufficiency: the table sentence**
- F10 68: "The classic attempts — lookup tables, reversed calculations, conclusion-as-premise — all fail one of the four; a new one must fail none." F10 533 has no table sentence.
- F11 528: "... a table of observed answers fails (F1); ... A table that encodes the response to every admitted change fails none and is an account, so it is not a counterexample; a new attempt must fail none and still explain nothing."
- Ruling: **CLAIM (S)**. This is the attack-list copy of D35. File 10 says lookup tables all fail. File 11 separates two kinds of table and says the encoding kind "fails none and is an account".
- Verdict effect: O33 (the table is faithful) and O2 (the almanac). Low.

## Part I: Commitments

Only punctuation changes: F10 84 / F11 69 and F10 90 / F11 75. See D68. There is no other difference.

## Part II: Organizations and their changes

**D25: Kinds are edit-signatures, finer contract**
- F10 136: "a coarser contract identifies more components."; F11 121 adds ", and two components of one kind on C may separate on a finer contract."
- Ruling: **WORDING**. This follows from the definition, and file 10 says it at grievance 2 (line 35: "At a finer level with more admitted changes they may separate").

**D26: Kinds are edit-signatures, a reading part has a measurement's signature (new)**
- F10: absent (paragraph ends at line 144, "It asks what its signature is."). F11 129: "In particular, a part that reads or reports another part has a measurement's signature: change only the reading and the part it reports stays as it was; change the part and the reading follows. Which of the two an account offers as producing an outcome is settled by that signature, not by the account's wording."
- Ruling: **CLAIM (X)**. It applies file 10's measurement signature (line 141) and the direction result of Part VII to reporting parts. The rule that the signature, not the account's wording, settles which part produces the outcome is new text.
- Verdict effect: can move a SPLIT to an AGREE. Cases: O9 (float against dial), O6 (the thermometer "is what is making the child shiver"), O4 (the index read by an instrument).

## Part III: Questions

**D27: The respect is the query, measure against production (new sentence)**
- F10 168: absent. F11 153, last sentence: "A measure that identifies an outcome, with a reliable prediction from it, answers the identification question; whether the measured part also produces the outcome is the production question, and the first answer is not the second."
- Ruling: **CLAIM (X)**. It applies "Two questions with the same D and different (C,Q) are different questions" to a measure. The claim that a reliable measure with a prediction answers the identification question is new text.
- Verdict effect: O4 ("a useful measure and a reliable prediction ... said almost nothing about why") and O6 (the first statement is a good reason; the second mistakes the instrument). Both come close to word for word.

**D28: "Scope, and a question that can be wrong", new paragraph**
- F10 174: heading "A question can be wrong", with no scope paragraph. F11 159 (new heading) and 161: "A contract is a declared subset of the physically admitted changes, and a stated scope is what makes it one. An account at a stated scope answers the question asked at that scope; it does not answer a broader question that failed, and a narrowing adopted after a failure is a new claim at a new index (Part VIII). What makes a restriction appropriate to the question asked is a substantive, criticizable part of the claim; the semantics records the restriction and supplies no rule that certifies it."
- Ruling: **CLAIM**. The first sentence is X: it restates non-vacuity (F10 272). The second is X: it generalizes F10 456 (Part XI, a narrowing to rescue EK is a new claim at a new index) and the Part VIII historical index to every account. The third is S: an explicit abstention. The theory states that it does not certify whether a restriction is appropriate, and D62 lists that appropriateness as a declared input.
- Verdict effect: yes. O1 (a retreat), O5 ("a legitimate narrowing. The limit follows from a part of her account"), O8 ("honest scope"). Where the case does not state what makes the restriction appropriate, the third sentence together with D62 can yield SILENT. O8 is supported by the second sentence.

**D29: A question that can be wrong, replacement query (new sentence)**
- F10 176: absent. F11 163, last sentence: "Supplying a meaning for a replacement query can make a coherent new question; it does not answer the original one."
- Ruling: **CLAIM (X)**. It follows from "The query Q is held fixed" (F10 268) and "changing C or Q ... without recording", but file 10 does not say it.
- Verdict effect: O34 (directly: "A meaning has been supplied ... It is not what Lea asked").

## Part IV: Layers, transports, and provenance

**D30: Three provenances, Selected: the population is part of the claim (new)**
- F10 210: ends "Write Sel(t;T,μ,H)." F11 197 adds: "The population T is part of the claim: what H leaves open about t is what T leaves open (Derivation 3)."
- Ruling: **CLAIM (S)**. It is tied to the Derivation 3 change but sits outside the three sentences the revision note names. The population, not the history alone, now fixes what is open.
- Verdict effect: O48, O24.

**D31: Representation is derived, provenance survives loss of access (new)**
- F10 226: absent. F11 213, last sentence: "A carrier keeps its provenance when present access to it is lost, and a later record derived from the carrier is not a second, independent witness to its history."
- Ruling: **CLAIM (S)**.
- Verdict effect: O28 ("The provenance is intact; the access is not"), O16 ("the diary is a second copy of the first"), O29 (a quotation inside the circle).

**D32: Expectation, surprise, violation (new sentence tied to Derivation 3)**
- F10 238: "Surprise requires an incomplete selection history, which is to say it requires that the world admit changes ... This is derived, not assumed (Derivation 4)." F11 225: "Surprise requires an incomplete selection history: the world must admit changes ... (Derivation 4). Whether the correspondence could have been otherwise at such a change is a fact about its population (Derivation 3)."
- Ruling: **CLAIM (S)** for the added last sentence, which ties to Derivation 3 and is not named in the revision note. The rest is WORDING.
- Verdict effect: O48, O24, and O3 (surprise) weakly.

## Part V: Account

**D33** (F10 260 / F11 247). "(Derivation 1)" is added after "no further condition about kinds to state". **WORDING**.

**D34** (F10 282 and 292, the headings "What (E) excludes" and "What (E) does not exclude" / F11 269, "What (E) excludes, and what it does not"). The two sections are merged. **ORDER**.

**D35: Table of observed answers, the encoding table "is an account"**
- F10 284: "A table that genuinely encodes an organization's response to every admitted change is not a table in that sense and is not excluded." F11 271: "... is not a table in that sense: it satisfies (F1) as a decomposition does, and it is an account. The word "table" settles nothing; the response under the admitted changes does."
- Ruling: **CLAIM (S)**. File 10 says only that (E)'s table clause does not exclude it. File 11 asserts that it is an Account, which needs all four conditions, including non-circular dependence and non-vacuity. This is stronger than file 10.
- Verdict effect: low. O33 ("The table is faithful"). O2 (the almanac is a table of observed answers under both files).

**D36: Reversed calculation, "may be faithful under the identification contract"**
- F10 286: absent at this place. F11 273 adds: "It may be faithful under the identification contract, which is a different question (Part III)."
- Ruling: **WORDING**. File 10 says this at Part VII line 338 ("It is faithful under the identification contract") for the same construction. File 11 repeats it here with "may".

**D37: Non-circularity, a component that restates the answer, packaged beside a real dependence (new)**
- F10 288: ""p because p" fails non-circular dependence." F11 275 adds: "So does an account whose only substantive component restates the answer it was asked for; packaging a genuine dependence that answers a different question beside it does not repair this (the bell does not explain the tide)."
- Ruling: **CLAIM (S)**. File 10's non-circular condition (line 270) has two clauses that pull apart on such a case. "The target's answer does not appear ... as a component" excludes it. "There exists (a,b) ... that removes ... a nonempty block of Γ ... under which the answer profile changes" can be met by the packaged block. File 11 settles the case and names it: the bell and the tide.
- Verdict effect: O2 (directly: its situation stresses that removing the bell "does change" what the account establishes). Under file 10 this reads as SPLIT or AGREE; under file 11, AGREE.

**D38: What (E) does not exclude, reworded**
- F10 294: "A true mechanism guessed for bad reasons satisfies (E); ... A less elegant account satisfies (E) as fully as a more elegant one with the same fidelity." F11 279: "(E) does not exclude a true mechanism guessed for bad reasons; ... It does not prefer an elegant account to a less elegant one with the same fidelity." The proof sentence is identical.
- Ruling: **WORDING**. "Satisfies" becomes "does not exclude", which is marginally weaker, but the point (reasons and elegance are not conditions) is the same.

**D39: What (E) does not exclude, coarse dependence (new)**
- F10: absent. F11 279 s3: "It does not reject a coarse dependence for omitting finer workings or an instrument: an account at a coarse grain is an account of the coarse question, and its strength is fixed by its contract, not by what a finer contract would add."
- Ruling: **CLAIM (S)**.
- Verdict effect: O7 (directly: "a genuine explanation, a coarse one ... no instrument is involved"). Under file 10 the likely mark is AGREE by way of "depth is question-relative". Under file 11 it is AGREE, stated outright.

## Part VI: Work, support, and interference

**D40: criticality is relative to the support written (new)**
- F10 316: "A block may be critical while no singleton in it is." F11 301 adds: "Criticality is relative to the support W it is assessed in: a commitment critical in one successful support need not be critical in the full candidate, and the supports assessed are the ones actually written, not a support someone could write in their place."
- Ruling: **CLAIM**. The first clause is X, from (B)'s index W. The second, "the ones actually written, not a support someone could write", is S.
- Verdict effect: O36 (directly: "P is critical in each route as written ... a candidate nobody has written").

**D41: the finite monotone theorem's reach (new)**
- F10 322: ends "∎". F11 307 adds: "The theorem applies only where its assumptions hold; an addition to Γ that destroys a support is the interference case below, and there upward closure fails."
- Ruling: **CLAIM (X)**. It follows from the theorem's hypotheses and the interference example.
- Verdict effect: O47 (directly: "additions could not always be made without loss").

**D42: Redundant routes, a route present from the start, and reassignment (new)**
- F10 324: "... the semantics represents the difference." F11 309: "... (Derivation 9). A route already present in the candidate is a route whether or not anyone has described its work; a component reassigned to a new target after a deletion belongs to a new candidate with its own assessment, and the new candidate's success is not the old one's."
- Ruling: **CLAIM (S)**. The pointer is WORDING.
- Verdict effect: O45 (the spring nobody mentioned) and O46 (the cable), both directly.

## Part VII: Exact constructions

**D43** (F10 352 / F11 337). "listed under attack (B)" becomes "listed under attack (B) in Part XV". **WORDING**: the pointer is retargeted because the attack list moved (D22).

No other difference in Part VII.

## Part VIII: Transport results

**D44: new paragraph "Recoding", sentence 1**
- F10: absent (Part VIII lines 364–378). F11 363 s1: "A declared, invertible recoding of a carrier preserves the content when a reader who applies the declared convention recovers every pairing (Derivation 8)."
- Ruling: **CLAIM (S)**. Derivation 8 (the same in both files) says only that structure-preserving bijections preserve (E), (G), (P) and (EK). The criterion of a reader applying a declared convention is new.
- Verdict effect: O43 (directly: "anyone reading with it recovers every pairing").

**D45: "Recoding", sentence 2**
- F10: absent. F11 363 s2: "A section of a carrier filled from another source keeps that other source's history, whatever it happens to match."
- Ruling: **CLAIM (S)**.
- Verdict effect: O44 (directly: "The patched section does not [depend on the source], and its matching is luck").

## Part IX: Criticism, use, and standing

**D46: Histories, a started route that did no work (new)**
- F10 384: ends "... under the declared contrasts." F11 371 adds: "A route that started and did no work, or that was already at rest when the result occurred, is not active for that result; whether a route is active is read from the history, not from the result."
- Ruling: **CLAIM (S)**. The first clause is close to file 10's "nonconstant dependence ... joining a represented input to an operative result". The "at rest" case and "read from the history, not from the result" are new.
- Verdict effect: O52 (directly), O25 (Ben's valve closed when nothing was left to stop), O19 (the diagram did no work), O13.

**D47: Receipts, a record reconstructed from the claim (new)**
- F10 406: ends "missing evidence stays missing." F11 393 adds: "A record reconstructed from the claim it is meant to support is not a receipt for that claim."
- Ruling: **CLAIM (X)**. It is close to entailed by "A receipt is a derivation tree over leaves", where a leaf refers to an event.
- Verdict effect: O16 (the diary), O29 (the quoted margin note), O37 (a circle).

## Part X: Understanding, construction, and origin

**D48: Deployment, narrow retained use (new)**
- F10 412 (the dashes are punctuation, D68). F11 399 adds: "A narrow retained use is what it is: it establishes neither the wider understanding it falls short of nor a permanent inability to reach it."
- Ruling: **CLAIM (S)**.
- Verdict effect: O14 (directly: "kept a narrow skill ... has yet to understand").

**D49: Construction, a first representation without prior observation (new)**
- F10 414. F11 401 adds: "A first representation may be constructed from an available problem without prior observation of what it represents."
- Ruling: **CLAIM (S)**.
- Verdict effect: O3 (directly: a part "that stands for cards she has never observed").

**D50: Construction, a small binding inside received content (new)**
- F10 414. F11 401 adds: "A small binding newly prepared inside received content is construction of that binding, and the rest of the content keeps its inherited provenance."
- Ruling: **CLAIM (S)**.
- Verdict effect: O18 (the one tooth), O31 (the wrong valve), O11 (Wednesday, reuse) weakly.

**D51: Origin, a dimension mentioned in passing (new)**
- F10 430. F11 417 adds: "A dimension of variation mentioned in passing is not thereby a port of the account; it becomes one when the account admits changes to it, and adding it is construction."
- Ruling: **CLAIM (S)**.
- Verdict effect: O23 (directly: "The seal was tight"), O33 (the columns "could have carried single-knob rows") weakly.

**D52: new paragraph "Ownership"**
- F10: absent. "owned by s" in Build (line 414) is used there but never defined. F11 419: "The subhistory in Build is owned by s when its processes run inside the system boundary and resource contract declared for s (Part XII). Work supplied from outside that boundary, a diagnosis, a decisive question, an instruction about what to read, remains an outside contribution however it is executed inside; a process that runs inside the boundary is the system's own today whoever wrote it; and where the boundary is drawn decides, not where the process sits in the casing. Ownership is not defined by the capability it is meant to ground (Part XII)."
- Ruling: **CLAIM (S)**. A new definition, of a term file 10 leaves undefined.
- Verdict effect: large. O17, O21 (a decisive question from outside), O27, O30 (the routine uploaded that morning), O40, O41 (an instruction about what to read), O49, O50, O51 (the casing).

## Part XI: Progress, knowledge, and the normative

**D53: Repair, obligations as declared inputs over stated occasions, and the loss criterion (new)**
- F10 438–444: "For claimed obligations O and protected obligations P, fixed for the comparison, [(P)] ... (P) does not rank alternatives. Losses outside P must be exposed." The (P) formula tests "∀r∈P[r(ξ)⇒r(ξ')]", only at the two compared states ξ and ξ'.
- F11 433 s1: "The obligations are declared inputs: O says what is to be repaired and P what is to be protected, each as a stated condition over stated occasions, and a protected condition is lost exactly when it fails on an occasion it covers."
- Ruling: **CLAIM (S)**. "Fixed for the comparison" becomes "declared inputs" (close to WORDING). Two further changes are not wording. (a) Obligations are now conditions over occasions. (b) Loss is defined as failure on any covered occasion ("exactly when"). In file 10's (P), loss is read at the end state ξ' only, provided the condition held at ξ, and occasions have no role. An interruption between ξ and ξ' after which the condition holds again is no loss under file 10's formula as written. It is a loss under file 11 if the occasions cover it, and outside file 11's loss if they do not. The formula (P) itself is unchanged, so the sentence also sits uneasily with the formula it glosses.
- Verdict effect: yes. O38 (condition stated as "at all times during the work", broken for four seconds). File 11 reaches "it was broken", so AGREE. File 10's end-state reading gives "held", a DISAGREE, unless r is read as ranging over the interval. O35 (the condition's occasions are not stated; nobody drew). File 11 gives AGREE if the occasions are draws, DISAGREE if all times, and SILENT under D62 if unstated. File 10 gives no loss (end state), so AGREE on "not a loss".

**D54: Repair, declaring an obligation makes no claim about worth (new)**
- F11 433 s2: "Their declaration makes no claim that the aims are worth pursuing, and (P) does not rank alternatives." File 10 has only the second clause.
- Ruling: **CLAIM (X)**.
- Verdict effect: O12, O35, O38 (the "mattered" points).

**D55: Repair, ProducedBy defined, and credit (new)**
- F10: ProducedBy appears only inside (P) (line 441) and is never defined. There is no credit rule. F11 433 s4: "ProducedBy holds when an active route (Part IX) runs from Δ to the repair; it credits each contribution the history establishes, and where two sufficient contributions both ran, both are credited and the history supplies no division of credit that it does not contain."
- Ruling: **CLAIM (S)**. A new definition and a new credit rule.
- Verdict effect: large. O13, O20 ("Neither can claim it alone"), O25, O26 ("the record divides it"), O32 (the minutes establish the division), O39, O52. It bears on O21, O27, O40 and O50 wherever the fixed verdict divides credit as "mostly". The rule that "no division of credit that it does not contain" is supplied can make "mostly" unsupported (DISAGREE or SILENT) unless the history establishes it.

**D56: Repair, three attributions (new)**
- F11 433 s5: "A correct account that produced nothing, an act that repaired without an account, and a repair produced through use of an account are three different attributions."
- Ruling: **CLAIM (X)**. It is implicit in (EK)'s separate conjuncts, Account and ProducesVia.
- Verdict effect: O13 (directly).

**D57: "Artistic effect, purpose, and aesthetic reason" becomes "Worth, and the normative relation"**
- F10 458: the normative relation N is "declared as a substantive input when aesthetic value is claimed ... The semantics does not derive N." F11 447: "Repairing an obligation establishes that it was repaired; it establishes nothing about whether the obligation, or the question that led to it, was worth having. Where a claim invokes worth, the semantics takes a normative relation N as a declared input and marks the place (Part XIV). The aesthetic case is one such invocation: ... The semantics does not derive N, and no aesthetics follows from achieving a stated effect."
- Ruling: **CLAIM (S)**. N's scope widens from aesthetic value to any invocation of worth, and a new separation of repair from worth is stated.
- Verdict effect: O12 ("its merit is real": under file 11 merit needs N, which the case does not supply, so SILENT; file 10 also left merit empty, D7), O35, O38.

## Part XII: The physical module

**D58: new paragraph "System boundary and continuity"**
- F10: absent. β and Ω are named only as indices, at line 523. F11 465: "A capability is attributed to a system under a declared boundary ... and a declared continuity Ω ... A replaced part that preserves the declared continuity leaves the same system; a process run inside the boundary is the system's whoever wrote it; a process run outside it is not the system's however close it sits. Both are declared before the attribution, not chosen after it."
- Ruling: **CLAIM (S)**.
- Verdict effect: O42 (directly: the new board), O30, O41, O51.

**D59: Owned capability, the ground of ownership (new sentence)**
- F10 476: ends "A theorist's description of a protocol is not the system's possession of it." F11 467 adds: "Ownership is grounded in the processes and resources the boundary includes, never in the capability being attributed: "owned because it can, and can because owned" grounds neither."
- Ruling: **CLAIM (S)**.
- Verdict effect: O49 (directly), O17.

**D60: Selection in the physical module, the population defined (new, tied to Derivation 3)**
- F10 482: ends "It is fallible and checkable as any physical claim is." F11 473 adds: "The population is the set of transports the physics and the stated construction admit; a transport that would need a part every member of the population is built without is not in it."
- Ruling: **CLAIM (S)**. It supplies the premise that makes Derivation 3's qualification bite. It is not among the three places the revision note names.
- Verdict effect: O48 (directly: the forbidden wire).

## Part XIV: The class collected

**D61: Primitives, item 2 (N invoked by worth)**
- F10 519: "The normative relation N, when a question invokes one." F11 510: "... when a question invokes worth. It is taken as an input and never derived; the aesthetic relation of Part XI is one instance."
- Ruling: **CLAIM (S)**. The same widening as D57. Counted here as the Part XIV place.
- Verdict effect: O12.

**D62: new paragraph "Declared inputs"**
- F10: absent. Between line 521 ("Everything else is derived ...") and line 523 ("Indices, not primitives") there is nothing. F11 514: "Besides the two primitives, some claims take stated inputs that the semantics records and does not supply: the obligations O and P of a repair, with the occasions each covers (Part XI); the scope of a contract and what makes a restriction appropriate (Part III); the system boundary and continuity of an attribution (Part XII). A verdict that depends on one of these is a verdict given the input; where the input is missing, the verdict is unsettled and the semantics says so rather than choosing the input from the verdict wanted."
- Ruling: **CLAIM (S)**. This adds a new category to the class, beside the primitives, the indices and the derived. It also adds a verdict rule: when the input is missing, the verdict is "unsettled". That rule reads directly as the SILENT mark ("it takes the deciding matter as an input the case leaves unstated"). There is a tension: boundary and continuity also remain "declared indices" at 516. The Part 0 taxonomy (D9) and "Everything else is derived" leave this category out.
- Verdict effect: large, and it pulls toward SILENT. The cases where an input it names is unstated: O35 (occasions), O1 and O5 (what makes a restriction appropriate), and O17, O21, O27, O30, O40 and O50 (no boundary is stated, yet ownership or credit is at issue). Where the input is stated, it pulls toward AGREE: O38, O41, O42, O51.

**D63: Dependence order, well-foundedness (new sentence)**
- F10 525: ends "... or "is knowledge."" F11 518 adds: "The order is well founded: a representation justified only by its own construction, or an ownership and a capability justified only by each other, has not supplied its place in it, and a separate proof that would supply it counts only when the account uses it."
- Ruling: **CLAIM (S)**.
- Verdict effect: O37 (directly: "The textbook proof would break the circle, and the account has not used it"), O49, O17.

Membership and "Indices, not primitives" are unchanged. The only other Part XIV change is the punctuation at 512 (D68).

## Part XV: What defeats this class

The rebuild is covered by D22 (ORDER), D23 (CLAIM, (D)) and D24 (CLAIM, (A) table). "A mathematical error" is identical (F10 543 / F11 538).

## Part XVI: Derivations

**D64: Derivation 3, title, claim, proof and consequence**
- F10 567–573. Title: "Selected transports are underdetermined on unseen changes". Claim: "For every (a,b)∈C∖H there exists a transport t′, also surviving on H, with a different value at (a,b)." Proof: "Alter L_j(a,b) for one (a,b)∉H to any other admitted relation; the result survives on H and differs at (a,b)." Consequence: "faithful where it was tested and unconstrained where it was not."
- F11 560–566. Title: "... on unseen changes their population leaves open". Claim: "Let t be selected from a population T ... For every (a,b)∈C∖H at which some t′∈T, also surviving on H, has a different value from t, the value of t at (a,b) is underdetermined by H ... The presence of an unseen pair alone does not establish that such a t′ exists; it must be admitted, realizable, a member of T, and a survivor of H." Proof: "Where T contains a transport with L_j(a,b) altered ... Where T contains no such transport, H is silent on the value at (a,b) and the population fixes it." Consequence: "... and, wherever its population admits an alternative, unconstrained where it was not ... What the qualification gives up is the guarantee of a differing survivor at every unseen pair ... a population restriction, a physical relation, or another stated constraint may already fix a value that the history never tested."
- Ruling: **CLAIM (S)**. A universal existence theorem becomes a conditional one that is close to definitional. New conditions: "admitted, realizable, a member of T". A new case is added: the population fixes the value.
- Verdict effect: O48 (moves from DISAGREE under file 10 to AGREE under file 11), O24 (AGREE under both), O3 (surprise) weakly.

**D65: Derivation 5, consequence (new sentence)**
- F10 589. F11 582 adds: "That a question was found says nothing about its worth (Part XI)."
- Ruling: **CLAIM (X)**. It follows from D57, and it is new against file 10, where N covered aesthetics only.
- Verdict effect: O12 (directly: "Noor found a better question, and its merit is real". The first half is supported; the second is unsettled without N).

**D66: Derivation 6, claim widened**
- F10 593: "... together with declared indices." F11 586: "... together with declared indices and declared inputs."
- Ruling: **CLAIM (S)**. The theorem's claim changes to cover D62's new category. The proof is unchanged ("By the dependence order of Part XIV"), and the dependence order does not list the declared inputs.
- Verdict effect: none directly. It carries D62.

**D67: Derivation 10, the selection response glossed through Derivation 3 (new clause)**
- F10 623: "the fidelity failure is structural, not parametric." F11 616: "... not parametric, and this is Derivation 3's qualification seen from the other side, a population that admits no survivor at the new change."
- Ruling: **CLAIM (X)**. A new interpretive assertion, tied to Derivation 3 and not in the revision note. It is inexact. Derivation 3's qualification concerns the absence of a differing survivor of H at an unseen pair. Derivation 10's case is the absence of any member faithful on the extended history. The two coincide only if all H0-survivors agree at the occlusion. See cross-reference X5.
- Verdict effect: none. Derivation 10's conclusions ((G), (P), (EK)) are unchanged.

Derivations 1, 2, 4 (apart from punctuation), 7, 8 and 9 are identical.

## D68: punctuation and markup only (WORDING, 17 places)

Dashes become commas, a serial comma is dropped, bold is added, or a Part pointer is pluralized. The claim is the same in each:
F10 27/F11 29; F10 84/F11 69; F10 90/F11 75; F10 122/F11 107; F10 138/F11 123; F10 158/F11 143; F10 168/F11 153 (s1: "rule-status, purpose-achievement" becomes "rule-status or purpose-achievement"); F10 190/F11 177; F10 284/F11 271 (bold "table of observed answers"); F10 286/F11 273 (dashes, bold "reversed calculation"); F10 298/F11 283; F10 412/F11 399; F10 521/F11 512 ("(Part IV, XII)" becomes "(Parts IV, XII)", "— from those" becomes ", from those"); F10 581/F11 574; F10 617/F11 610; F10 623/F11 616 (dashes around "a persistence component"); F10 625/F11 618.

## Step 1 counts

- **CLAIM: 44 places.** D1, D7, D8, D10, D13, D23, D24, D26, D27, D28, D29, D30, D31, D32, D35, D37, D39, D40, D41, D42, D44, D45, D46, D47, D48, D49, D50, D51, D52, D53, D54, D55, D56, D57, D58, D59, D60, D61, D62, D63, D64, D65, D66, D67.
  - meta, about the document and not the theory: 2 (D1, D10).
  - S: 33, including D8, which copies the S-rule D55 into the front matter and is new against file 10. X: 9 (D26, D27, D29, D41, D47, D54, D56, D65, D67). D28 and D40 are mixed and counted as S.
  - Tied to Derivation 3: 7 (D13, D23, D64, the three the revision note names in its own terms; and D30, D32, D60, D67, which it does not name).
- **WORDING: 21 ids, which is 37 places** (D2, D3, D4, D5, D6, D11, D12, D14, D15, D16, D17, D18, D19, D20, D21, D25, D33, D36, D38, D43; and D68, which covers 17 places).
- **ORDER: 3** (D9, D22, D34).

---

# STEP 2: cross-references in file 11

I listed every internal pointer in file 11: a Part, a section, a derivation, a definition or condition, or a bracketed label such as (O), (O1), (E) or (K1). I checked where each one points.

## Pointers that are CORRECT

Pointers carried over unchanged from file 10 are all still correct: (O), (Q), (K), (F1), (F2), (A), (E), (S), (B), (D), (R), (T1), (T2), (I1), (I2), (I4), (O1), (K1), (K2), (K3), (P), (EK), (AR), (G), (N), (CT1)–(CT4), (CA), (RC), (U1)–(U3), "by Part II" (323), "Part V" (191), "Part IV" (157), "(Part X)" (199, 227), "(Part IX)" (279), "(Part XII)" (399), "(Part VIII, historical index)" and "(Derivation 5)" in Derivation 7, "(Derivation 4)" and "(Derivation 1)" in Derivation 10, "(Derivation 2)" (620), "Parts II–XIII" and "Derivation 1" in Derivations 2 and 6. "(O1)" at 333 and 538 is the Part VII obstruction label. Its target is correct in both files, but the label has the same name as case O1. That collision is present in file 10 as well and is not a change.

New or changed pointers in file 11 that I checked and rule CORRECT:
- 13 "(Part II, Derivation 1)". 15 "(Part IV)". 17 "(Part III, Derivation 5)". 19 "Part XV lists what would count" ((A), (B)). 25 "(Derivation 9)". 27 "(Part XI)" for the division of credit (Repair, 433). 33 "in the order Part XIV states" and "(Derivation 6)".
- 39 "(Part II, "Kinds are edit-signatures")". 43 "Derivation 3" (the paraphrase matches the revised claim at 562). 45 "(non-vacuity, Part V)" (259: "excluded by a stated scope, not silently"). 49 "Part IV forbids the reduction and Part XV names its refutation" ((D), second disjunct). 51 "(Part VII)". 53 "In Part XI" (the aesthetic case is now inside "Worth, and the normative relation"). 55 "(Parts IV, XII)". 57 "Derivation 7". 59 "(Part II)". 63 "(A)–(E)" and "Part XV".
- 161 "(Part VIII)" (Historical index: "A new index is a new claim"). 197 "(Derivation 3)". 225 "(Derivation 4)" and "(Derivation 3)". 247 "(Derivation 1)". 273 "(Part III)" (The respect is the query). 309 "(Derivation 9)". 337 "attack (B) in Part XV" (retargeted; Part XV (B) names eliminative explanation).
- 363 "(Derivation 8)". The target is right: invertible recoding is a bijection. The reader-convention criterion in the sentence is new and not in Derivation 8 (see D44). The pointer supports the sentence's core.
- 419 "(Part XII)" twice (System boundary and continuity; Owned capability). 433 "(Part IX)" (active route). 510 "the aesthetic relation of Part XI". 512 "(Parts IV, XII)". 514 "(Part XI)", "(Part III)", "(Part XII)".
- Part XV: 528 "Part V says which of the four each classic attempt fails" (table fails (F1) at 271; reversed calculation fails (F2) at 273; "p because p" fails non-circular dependence at 275). 530 "(Part VII)". 532 "Derivation 1". 534 "Derivation 3" and "Part IV" twice. 536 "(against Derivation 5)". 538 "Derivations 1–3 under their stated assumptions".
- 582 "(Part XI)" (worth, 447).

## Pointers that are not CORRECT

**X1. Revision note, line 5: "The three sentences that restated it (the answer to grievance 3, attack point (D), the Part XV entry)". Ruled SLIP.** The enumeration follows file 10's layout, where attack point (D) (Part 0, line 74) and the Part XV entry (line 539) are two sentences. In file 11 the attack list has moved into Part XV, so "attack point (D)" and "the Part XV entry" are one passage (534). The Part 0 residue at 63 is a neutral summary that does not restate Derivation 3. The pointers land, but on two places, not three. What the note claims is unaffected. Separately, and not as a pointer fault, the note's completeness claims are false. File 11 restates or depends on the new Derivation 3 in four further places the note does not name (197, 225, 473, 616: D30, D32, D60, D67). "Nothing else changes in what is claimed" is contradicted by the other CLAIMs of step 1.

**X2. Line 27 (Part 0, "does not claim"): "Where a claim needs one of these, the semantics takes it as a declared input and marks the place (Parts XI, XIV)." Ruled SLIP.** The targets carry this only for worth and aesthetics: Part XI "Worth, and the normative relation" (447), and Part XIV Primitives item 2 (510). Nothing in the body makes a probability of truth, a merit function or a ranking of thinkers a declared input. There is also a clash of terms: Part XIV's "Declared inputs" paragraph (514) opens "Besides the two primitives", so under Part XIV's own terms N is a primitive and not a declared input. The pointer covers only part of the sentence. What the sentence claims is set by its own words (see D7), so I rule SLIP.

**X3. Line 447 (Part XI): "the semantics takes a normative relation N as a declared input and marks the place (Part XIV)." Ruled SLIP.** The same clash of terms as X2. Part XIV calls N a primitive "taken as an input" (510) and keeps "declared inputs" (514) as a separate category that excludes the primitives. The substance, that N is an input and is never derived, is carried.

**X4. Line 588 (Derivation 6 proof): "By the dependence order of Part XIV, following each definition to its base." Ruled SLIP.** The claim at 586 now adds "and declared inputs". The dependence order at 518 does not list the declared inputs (O and P with their occasions, the appropriateness of a restriction, boundary and continuity). It also does not list the new definitions that rest on them: Ownership (419), System boundary and continuity (465), and ProducedBy (433). The pointer still lands on the right paragraph, but that paragraph no longer covers the widened claim. The claim itself is set by its words.

**X5. Line 616 (Derivation 10): "this is Derivation 3's qualification seen from the other side, a population that admits no survivor at the new change". Ruled SLIP.** Derivation 3's qualification (562–564) is the case where T holds no survivor of H that differs from t at the unseen pair. There, "H is silent ... and the population fixes it". Derivation 10's case is that no member of the population survives the extended history, meaning none is faithful at the occlusion. These are different conditions. Occupancy-only predictors could differ among themselves at the occlusion, so Derivation 3's unqualified clause would apply, and still none would survive. They coincide only if every H0-survivor agrees there. The pointer lands on the right derivation with an inexact gloss. Derivation 10's conclusions are unchanged, so it does not change what Derivation 10 claims.

**No pointer is CLAIM-CHANGING.** In none of the cases above does the misdirection change what the sentence asserts. In X1–X4 the fault is that the target covers less than the sentence says. That is a coverage gap, recorded under D7, D10, D62 and D66.

Also noted, not a pointer fault. Line 33 ("What is primitive ...") divides the theory into primitives, indices and "Everything else is derived, in the order Part XIV states". Part XIV itself (514) adds a fourth category, declared inputs, that is neither derived nor in the dependence order. Boundary and continuity are both "declared indices" (33, 516) and "declared inputs" (514).

## Pointers in file 10 that file 11 dropped or retargeted

- **Retargeted**: F10 352 "listed under attack (B)" (target: Part 0, "Where to attack this" (B), line 70) becomes F11 337 "listed under attack (B) in Part XV" (target 530). CORRECT.
- **Carried into Part XV with the move**: F10 68 "(Part V)" becomes F11 528 "Part V says ...". F10 70 "Part VII gives the semantics' treatment" becomes 530 "(Part VII)". F10 72 "Derivation 1 says this is impossible" becomes 532 "This refutes Derivation 1". F10 74 "(against Derivation 3)", "(against Part IV)" and "the primitive layer described in Part IV" become 534 with the same pointers. F10 539 "This refutes Derivation 3" becomes 534 "against Derivation 3". F10 533/535 "This refutes sufficiency / necessity" become the labels (A) and (B). All CORRECT.
- **Reworded but kept**: F10 38 "There is a theorem below (Derivation 3)" becomes 43 "Derivation 3 says". F10 47 "in Part IV" becomes 49 "Part IV ... and Part XV". F10 50 "This is worked in Part VII" becomes 51 "(Part VII)". F10 238 "This is derived, not assumed (Derivation 4)" becomes 225 "(Derivation 4)". F10 521 "(Part IV, XII)" becomes 512 "(Parts IV, XII)".
- **Dropped**: none. F10 76, attack (E), had no pointer; file 11 adds "(against Derivation 5)" at 536.

---

# STEP 3: the named places (written after steps 1 and 2)

Disclosure: the task text named these three places before I began, so I knew of them during the sweep. The sweep did not depend on that knowledge. It rested on a mechanical sentence-by-sentence diff of the two files, which flags every changed sentence whether or not anyone has named it, and each of the three places appears in that output. I then read and ruled every flagged sentence Part by Part. None of the three needed special handling to be caught.

**(i) Derivation 3 and the three sentences restated with it.**
- Caught: yes. Derivation 3 is **D64, CLAIM (S)**. A universal existence theorem ("For every (a,b)∈C∖H there exists a transport t′ ... with a different value") becomes a conditional one ("at which some t′∈T, also surviving on H, has a different value"). It adds the requirement "admitted, realizable, a member of T, and a survivor of H", a new proof branch ("the population fixes it"), and a new consequence that gives up "the blanket claim that every untested value is unconstrained".
- The answer to grievance 3 is **D13, CLAIM (S)**: "*always* underdetermined" becomes "wherever its population admits a differing survivor there".
- Attack point (D) and the Part XV entry are **D23, CLAIM (S)**. In file 11 they are one passage (534), not two. It changes both the condition (population-relative) and the quantifier (file 10's "determined on C∖H" becomes a single "unseen change"). The Part 0 residue (63) is a neutral summary.
- Beyond the three named sentences, the sweep found four more CLAIMs tied to Derivation 3 that the revision note does not name. These are D30 (Part IV Selected, 197), D32 (Expectation, 225), D60 (Part XII, 473: the population defined, and a part missing from every member keeps a transport out), and D67 (Derivation 10, 616, an inexact gloss). D60 supplies the premise that decides O48.
- Case effect: O48 moves from DISAGREE under file 10 to AGREE under file 11. O24 is AGREE under both.

**(ii) Part XI Repair: "each as a stated condition over stated occasions, and a protected condition is lost exactly when it fails on an occasion it covers" (F11 433; F10 438–444).**
- Caught: yes. This is **D53, CLAIM (S)**.
- File 10's Repair paragraph has "fixed for the comparison" and the (P) formula, whose protection clause "∀r∈P[r(ξ)⇒r(ξ')]" is tested only at the two compared states. File 10 has no occasions and no loss criterion beyond that formula. File 11 adds occasions to every obligation and defines loss as failure on any covered occasion. It leaves (P) itself unchanged, so the formula and the new sentence now read differently: endpoint states against covered occasions. That difference is itself a possible SPLIT.
- Case effect. O38 (condition stated as "at all times during the work", four-second stop): file 10's endpoint reading finds no loss, which is DISAGREE with "it was broken". File 11 finds a loss on a covered occasion, which is AGREE. O35 (condition not stated, nobody drew): file 10 finds no loss at ξ′, which is AGREE with "not a loss". Under file 11 it turns on the occasions: SILENT under D62 when they are unstated, AGREE if the occasions are draws, DISAGREE if all times. The sweep caught it because the sentence did not exist in file 10.

**(iii) Part XIV "Declared inputs" (F11 514).**
- Caught: yes. This is **D62, CLAIM (S)**. It is a whole new paragraph with no counterpart in file 10 (nothing between F10 521 and 523).
- It adds a class category beside the primitives, the indices and the derived. It also adds a verdict rule: "where the input is missing, the verdict is unsettled and the semantics says so". That rule corresponds to the SILENT mark as the briefs define it ("it takes the deciding matter as an input the case leaves unstated").
- It is carried into Derivation 6's claim (D66, "and declared inputs") and echoed in Part 0 (D7).
- It is in tension with Part 0's "Everything else is derived" (D9) and with "Indices, not primitives", which still lists boundary and continuity as indices. The Derivation 6 proof pointer no longer covers it (X4).
- Case effect: it pulls toward SILENT wherever a case leaves the named input unstated. For occasions that is O35. For what makes a restriction appropriate, O1 and O5. For the system boundary where ownership or credit is at issue, O17, O21, O27, O30, O40 and O50. It pulls toward AGREE where the input is stated: O38, O41, O42 and O51.
