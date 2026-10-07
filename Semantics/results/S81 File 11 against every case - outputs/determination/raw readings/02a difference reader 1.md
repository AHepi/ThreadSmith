# S81 difference-reader 1: file 10 (frozen authority) against file 11 (revision 1)

Reader: Claude, difference-reader 1 of two, working independently.
Sources read: file 10 in full (629 lines); file 11 in full (622 lines); the S81 case book (O1–O52); lines 1–75 of briefs s81_1C_A.txt and s81_1K_A.txt (the instructions, including the marks and "Same finding"). The two briefs have identical instructions. Brief 1C carries file 11 and brief 1K carries file 10; I saw that only from heading lines in a grep. I did not read the embedded theory or case text in the briefs beyond those heading lines.
Method: I read both files side by side, Part by Part. To be sure no place was missed, I then made a word-level diff of the two files (`git diff --no-index --word-diff`, run on scratch copies) and ruled every hunk. Steps 1 and 2 below were written before step 3.

Blindness report: I opened nothing under Semantics/results/ except those two briefs, read by exact path (lines 1–75, plus a grep of their heading lines). I did not open the project story, Status, README, INDEX, the S81 plans, the case-book provenance file or the S76/S72 instruction files. Listing `Semantics/tests/ | grep S81` and `Semantics/authority/` showed me file NAMES only: the S81 plan files, the provenance file, and the Stage 1 and Stage 2 instruction files in tests/, and files 00 and 12 in authority/. I opened none of them. A harness reminder also showed me the parent session's task-list titles, with no content from any prohibited file. After finishing, an `ls` of s81_det/ showed me the NAMES of other files there (diffreader2.md, reader1_O1-O26.md, reader1_O27-O52.md, reader2_O1-O26.md, reader2_O27-O52.md). I opened none of them. The only mention of results I met is inside file 11 itself: its revision note cites "Semantics results S75" and "the audit's case O48".

Rulings:
- CLAIM: file 11 asserts something file 10 does not; or it drops, re-scopes or re-conditions something file 10 asserts.
- WORDING: the same claim in different words.
- ORDER: the same claim, moved.

The CLAIM rulings carry a sub-tag. The sub-tag is only there to help the reader; the ruling is CLAIM in every case.
- **-c (changed):** file 10 said something different.
- **-n (new):** new content, such as a new definition, condition or verdict rule, that file 10 does not state and that is not a direct consequence of one of its sentences.
- **-a (application):** a new explicit sentence that follows fairly directly from file 10 sentences, but file 10 left it to inference. It can move a mark from SPLIT or SILENT to AGREE.
- **-meta:** a statement about the document rather than about explanation.

Line numbers: "f10 Lx" is file 10, "f11 Ly" is file 11.

---

## STEP 1: Every place where the two files differ

### Front note

**D1: Revision note.** f10: absent. f11 L5: "*Revision 1 (file 11) … One claim changes: Derivation 3, whose unqualified form gave the wrong verdict on the audit's case O48 … Nothing else changes in what is claimed.*"
- **CLAIM-meta.** The note makes new assertions about the document. It says the revision keeps "the same primitives, definitions, conditions, constructions and derivations". It says only Derivation 3 and "three sentences" change. It says the old proof "already assumed the qualification". The sweep below contradicts the first two: file 11 adds new definitions (Ownership, ProducedBy, System boundary and continuity, Recoding, Declared inputs, the population). There are about 46 further CLAIM places.
- Verdict effect: the note is not a theory sentence. But the theory text now names case O48 and tells the reader that the old Derivation 3 gave the wrong verdict there. That can steer a tester on **O48**.
- On "whose proof already assumed the qualification": the f10 proof asserts that an arbitrary alteration "survives on H". Survival is defined only for members of the population T. So the f10 proof silently needed the altered transport to be in T. This part of the note is a fair reading. I did not verify the S75 claim, which is out of scope.

### Part 0: What this document claims

**D2.** f10 L11 / f11 L13. "Nothing in the definition of an explanation asks" → "The definition never asks". Adds the pointer "(Part II, Derivation 1)". **WORDING.**

**D3.** f10 L13 / f11 L15. "*selected* — produced by blind variation and survival on a history of predictions" → "*selected*, produced by variation and survival on a history of encountered changes". Also "distinguished" → "told apart", "of this semantics" → "here", and a pointer "(Part IV)" is added.
- **WORDING** (borderline). "blind" and "history of predictions" are dropped from the front matter. The body keeps both:
  - blindness, as Part IV "No member of the history represents t, H, or the survival condition" (unchanged);
  - H as "edit–boundary pairs actually encountered" (unchanged).
- So the front matter was brought into line with an unchanged body.

**D4.** f10 L15 / f11 L17. Dashes → "meaning"; "distinguishes" → "separates"; pointer "(Part III, Derivation 5)" added. **WORDING.**

**D5.** f10 L17 / f11 L19. Sentence added: "Part XV lists what would count." **WORDING** (a pointer only).

### Part 0: What this document does not claim

**D6.** f10 L23 / f11 L25. "Fidelity in this semantics is over" → "Fidelity is over". Pointer "(Derivation 9)" added. **WORDING.**

**D7.** f10 L25 / f11 L27, sentences 1–2.
- f10: "It does not supply an objective aesthetics, a probability of truth, a merit function, or a ranking of thinkers. It supplies places where such things would go if anyone had them, and marks those places as empty."
- f11: "…a merit function, a measure of worth, or a ranking of thinkers. Where a claim needs one of these, the semantics takes it as a **declared input** and marks the place (Parts XI, XIV)."
- **CLAIM-c.** f11 adds "a measure of worth" to the list. It also replaces "empty places" with "a declared input". Under Part XIV (D67), a verdict is then given relative to the input, and is unsettled when the input is missing. File 10 simply left the place empty.
- Could change a verdict: possible, on cases that need worth: **O12** ("its merit is real"), **O35/O38** ("in every way that mattered", "whether four seconds mattered"). The mark is likely SILENT under both files; what differs is how the theory itself describes the gap.

**D8.** f10: absent / f11 L27, sentence 3: "It does not supply a division of credit among contributors beyond what a history establishes (Part XI)."
- **CLAIM-n.** File 10 says nothing on division of credit.
- Could change a verdict: YES.
  - It supports the fixed verdicts of **O20, O26, O32, O39** ("no way to say whose water stopped"; "the record divides it") and **O40** ("Neither can say 'mostly'").
  - It bears against the "mostly" findings of **O21, O27, O50**. The history does not establish "mostly".

**D9.** f10 L27 / f11 L29. Oxford comma removed. **WORDING** (also listed in D24).

### Part 0: new section "What is primitive, what is an index, and what is derived"

**D10.** f10 Part XIV L516–525 and Derivation 6 L597 / f11 L31–33: "The semantics has two primitives … Grain, boundary, continuity and the contract of admitted changes are **declared indices** … No predicate meaning "really explains", "is a cause" or "is knowledge" appears anywhere (Derivation 6)."
- **ORDER.** This is a front-matter restatement of Part XIV (Primitives, Indices, Dependence order) and of the Consequence of Derivation 6. The one exception is the phrase "the normative relation N, taken as an input wherever a question invokes worth". f10 L519 has "when a question invokes one", meaning a normative relation. That phrase is a CLAIM and is ruled with its body location, D65.

### Part 0: Grievances

**D11.** f10: absent / f11 L37: "Each answer points at the part of the document that carries it; the front matter states nothing the body does not state more exactly."
- **CLAIM-meta.** This is a new rule for reading: the body governs the front matter. It can change which statement a tester treats as authoritative wherever the two differ.
- The claim is not fully true of file 11 itself:
  - L27 says a probability of truth, a merit function and a ranking are taken as declared inputs, but no body text says so (see X3).
  - L63 restates (D) without the qualification.
- No direct case.

**D12. G1.** f10 L31–32 / f11 L39. "The difference is…exactly what the semantics checks" → "That is…what the semantics checks (Part II, "Kinds are edit-signatures")". "Declared kind-labels added no discriminating power…edit-fidelity already finds it…the label was asserting" → "A declared label adds no discriminating power…fidelity finds it…the label asserts". Question and answer are merged onto one line. **WORDING.**

**D13. G2.** f10 L34–35 / f11 L41. "— and then" → ", and then". "The semantics indexes every kind-claim to its level" → "Every kind-claim is indexed to its level". **WORDING.**

**D14. G3** (named place i). f10 L37–38 / f11 L43.
- f10: "There is a theorem below (Derivation 3) that selected transports are *always* underdetermined on unseen changes."
- f11: "Derivation 3 says that a selected transport is underdetermined by its history on an unseen change wherever its population admits a differing survivor there."
- Also "entirely independent" → "independent" (WORDING).
- **CLAIM-c.** The quantifier changes from "always, at every unseen change" to "only where the population admits a differing survivor".
- Could change a verdict: YES, on **O48** ("no alternative in that population… The premise is not met"). File 10's "always" goes against that verdict; file 11 goes with it. It also touches **O24**, where a differing arrangement is given, so the verdict is likely unchanged.

**D15. G4.** f10 L40–41 / f11 L45. Pointer "(non-vacuity, Part V)" added. "in the physics and in the fidelity facts" → "in the physics and the fidelity facts". **WORDING.**

**D16. G5.** f10 L43–44 / f11 L47. "teleosemantics / structural realism / functionalism" → "teleosemantics, structural realism or functionalism". The closing "…a question about the literature, not about whether it is right" loses the clause "not about whether it is right".
- **WORDING.** The dropped clause is already implied by "a question about the literature".

**D17. G6.** f10 L46–47 / f11 L49.
- The objection loses "That is deflationary."
- "things-with-persistence" → "persistent things".
- "the semantics forbids that reduction in Part IV" → "Part IV forbids the reduction and Part XV names its refutation".
- **WORDING.**

**D18. G7.** f10 L49–50 / f11 L51. The objection loses "This cannot handle mathematical explanation." "well-defined" → "well defined". "This is worked in Part VII." → "(Part VII)". **WORDING.**

**D19. G8.** f10 L52–53 / f11 L53. "gives … three distinct mathematical carriers and refuses to define any as another" → "get three distinct carriers, and none is defined as another". **WORDING.**

**D20. G9.** f10 L55–56 / f11 L55.
- The objection loses "just" and "Who says the selection happened?".
- Pointer "(Parts IV, XII)" added.
- Dropped: "it is a label. The difference is the difference between a hypothesis and a stipulation."
- **WORDING.** The contrast between hypothesis and stipulation stays implicit in the two retained sentences: selection is a checkable claim, and a kind-label is not a claim.

**D21. G10.** f10 L58–59 / f11 L57. "It is having it both ways deliberately" → "It is, deliberately". "contracts can change" → "contracts change". **WORDING.**

**D22. G11.** f10 L61–62 / f11 L59. Pointer "(Part II)" added. "What the semantics denies" → "What it denies". Italics dropped on *before*. **WORDING.**

### Part 0: Where to attack this

**D23.** f10 L64–78 / f11 L61–63.
- File 10 states the five attack points in full here.
- File 11 keeps a one-sentence summary: "…are stated exactly in Part XV… (A) sufficiency…; (B) their necessity; (C) the eliminability of kinds; (D) the two provenances and the underdetermination of selected transports; (E) the representability of question-finding."
- **ORDER.** The full statements move to Part XV (see D69–D75).
- Note: the L63 short form of (D) says "the underdetermination of selected transports" without the population qualification. That goes against the note's promise that "every restatement of a theorem carries the theorem's own qualification". I rule it ORDER because it is a label for the Part XV entry, not a restatement of the theorem.

### Punctuation and format only (grouped)

**D24.** WORDING. Em-dashes become commas, and the Oxford comma is dropped, with nothing else changed. Places:
- f11 L29 (f10 L27);
- Part I L69, L75 (f10 L84, L90);
- Part II L107, L123 (f10 L122, L138);
- Part III L143 and the dashes of L153 (f10 L158, L168);
- Part IV L177 (f10 L190);
- Part V L283 (f10 L298);
- the dashes of Part X L399 (f10 L412);
- Derivation 4, Consequence, L574 (f10 L581);
- Derivation 10 L610, the dashes of L616, and L618 (f10 L617, L623, L625);
- the grievance layout (question and answer merged onto one line).

This is 14 or more locations, counted here as one place.

### Part II: Organizations and their changes

**D25.** f10 L136 / f11 L121. Added: "…and two components of one kind on C may separate on a finer contract."
- **WORDING.** This restates f10 G2 ("At a finer level with more admitted changes they may separate") and follows from "a coarser contract identifies more components".

**D26.** f10: absent after L144 / f11 L129. Added: "In particular, a part that reads or reports another part has a measurement's signature: change only the reading and the part it reports stays as it was; change the part and the reading follows. Which of the two an account offers as producing an outcome is settled by that signature, not by the account's wording."
- **CLAIM-a.** This applies f10's measurement signature and Part VII's rule that direction is derived from edits. The rule is now explicit.
- Could change a verdict: YES, from SPLIT to AGREE, on **O4** (the recalibration test), **O6** (warming the thermometer) and **O9** (bending the needle).

### Part III: Questions

**D27.** f10: absent / f11 L153. Added: "A measure that identifies an outcome, with a reliable prediction from it, answers the identification question; whether the measured part also produces the outcome is the production question, and the first answer is not the second."
- **CLAIM-a.** This applies "an answer to one is not an answer to the other". Its wording tracks the fixed verdict of O4 closely ("a useful measure and a reliable prediction").
- Could change a verdict: YES, on **O4** and **O6**.

**D28.** f10 L174 heading "A question can be wrong" → f11 L159 "Scope, and a question that can be wrong". **WORDING.**

**D29.** f10 L272 (non-vacuity) and L41 (G4) / f11 L161, sentence 1: "A contract is a declared subset of the physically admitted changes, and a stated scope is what makes it one." **ORDER** (restates Part V non-vacuity).

**D30.** f10 L456 (Part XI: "A later narrowing of that contract to rescue adequacy is a new claim at a new index"), L378 (historical index) and L41 / f11 L161, sentence 2: "An account at a stated scope answers the question asked at that scope; it does not answer a broader question that failed, and a narrowing adopted after a failure is a new claim at a new index (Part VIII)."
- **ORDER.** The sentence moves the (EK) narrowing sentence and Part VIII's general rule ("A new index is a new claim") to Part III. The generalisation beyond (EK) was already in Part VIII.
- It bears on **O1, O5, O8**, but with no change of claim.

**D31.** f10: absent / f11 L161, sentence 3: "What makes a restriction appropriate to the question asked is a substantive, criticizable part of the claim; the semantics records the restriction and supplies no rule that certifies it."
- **CLAIM-n.** File 10 has no statement about whether a restriction is appropriate. File 11 now states that the semantics certifies none. With D67, "what makes a restriction appropriate" becomes a declared input, so a missing input leaves the verdict unsettled.
- Could change a verdict: YES, towards SILENT.
  - **O5**: "This is a legitimate narrowing." A tester using file 10 could derive this from the limit being tied to a component of Greta's account.
  - **O1**: "the series as a whole is a retreat."
  - **O8**: "an honest scope".

**D32.** f10: absent / f11 L163. Added: "Supplying a meaning for a replacement query can make a coherent new question; it does not answer the original one."
- **CLAIM-a.** Applies "Two questions with the same D and different (C,Q) are different questions".
- Could change a verdict: YES, from SPLIT to AGREE, on **O34**.

### Part IV: Layers, transports, and provenance

**D33.** f10 L210 / f11 L197. Added to *Selected*: "The population T is part of the claim: what H leaves open about t is what T leaves open (Derivation 3)."
- **CLAIM-c** (part of the Derivation 3 cluster, not among the "three sentences" the note names). It adds a constraint to the meaning of Sel.
- Could change a verdict: YES, on **O48**; also touches **O24**.

**D34.** f10: absent after L226 / f11 L213. Added: "A carrier keeps its provenance when present access to it is lost, and a later record derived from the carrier is not a second, independent witness to its history."
- **CLAIM-n.**
- Could change a verdict: YES, on **O28** ("provenance is intact; the access is not") and **O16** ("the diary is a second copy"). It also touches **O29**.

**D35.** f10 L238 / f11 L225. "…which is to say it requires that the world admit changes… This is derived, not assumed (Derivation 4)." → "…: the world must admit changes… (Derivation 4)." **WORDING.**

**D36.** f10: absent / f11 L225. Added: "Whether the correspondence could have been otherwise at such a change is a fact about its population (Derivation 3)."
- **CLAIM-c** (Derivation 3 cluster; not named in the note).
- Could change a verdict: YES, on **O48**; touches **O24**.

### Part V: Account

**D37.** f10 L260 / f11 L247. Pointer "(Derivation 1)" added. **WORDING.**

**D38.** f10 L282 and L292, two headings ("What (E) excludes", "What (E) does not exclude") → f11 L269, one heading ("What (E) excludes, and what it does not"). **ORDER.**

**D39.** f10 L284 / f11 L271.
- f10: "A table that genuinely encodes an organization's response to every admitted change is not a table in that sense and is not excluded."
- f11: "…is not a table in that sense: it satisfies (F1) as a decomposition does, and it is an account. The word "table" settles nothing; the response under the admitted changes does."
- **CLAIM-c.** "Not excluded" by the argument from (F1) becomes "it is an account". That asserts all of (E), including (A), non-circular dependence and non-vacuity, which the sentence never checks.
- Could change a verdict: possible, but low. It touches **O33** ("The table is faithful") and **O2** (the almanac). The almanac encodes no response to intervention, so O2 is probably unaffected.

**D40.** f10 L286 (and Part VII L338) / f11 L273. Added: "It may be faithful under the identification contract, which is a different question (Part III)."
- **ORDER.** This restates f10 Part VII ("It is faithful under the identification contract"), hedged to "may be" for the general case.

**D41.** f10: absent after L288 / f11 L275. Added: "So does an account whose only substantive component restates the answer it was asked for; packaging a genuine dependence that answers a different question beside it does not repair this (the bell does not explain the tide)."
- **CLAIM-n.** The first half follows from f10's "does not appear … as a component".
- The second half closes a loophole in f10's existential clause: "There exists (a,b)∈C that removes … a nonempty block of Γ … under which the answer profile changes". Under file 10, deleting the bell block could be read as satisfying that clause. The sentence is also tailored to a case: it quotes the content of O2.
- Could change a verdict: YES, from SPLIT to AGREE, on **O2**.

**D42.** f10 L294 / f11 L279.
- "A true mechanism guessed for bad reasons satisfies (E)" → "(E) does not exclude a true mechanism guessed for bad reasons".
- "A less elegant account satisfies (E) as fully as a more elegant one" → "It does not prefer an elegant account to a less elegant one".
- **WORDING.** Taken alone, "does not exclude" is weaker than "satisfies". In context the claim is the same.

**D43.** f10: absent / f11 L279. Added: "It does not reject a coarse dependence for omitting finer workings or an instrument: an account at a coarse grain is an account of the coarse question, and its strength is fixed by its contract, not by what a finer contract would add."
- **CLAIM-a.** It follows from grain-indexing and "depth is question-relative". The words "or an instrument" track O7 ("no instrument is involved anywhere").
- Could change a verdict: YES, from SPLIT to AGREE, on **O7**.

### Part VI: Work, support, and interference

**D44.** f10: absent after L316 / f11 L301. Added: "Criticality is relative to the support W it is assessed in: a commitment critical in one successful support need not be critical in the full candidate, and the supports assessed are the ones actually written, not a support someone could write in their place."
- **CLAIM-n.** The first clause follows from (B). The second clause, "the ones actually written", is new.
- Could change a verdict: YES, on **O36**.

**D45.** f10 L322 / f11 L307. Added: "The theorem applies only where its assumptions hold; an addition to Γ that destroys a support is the interference case below, and there upward closure fails."
- **CLAIM-a.** It follows from the definitions and the interference example.
- Could change a verdict: YES, from SPLIT to AGREE, on **O47**.

**D46.** f10 L324 / f11 L309.
- Pointer "(Derivation 9)" added (WORDING).
- Added: "A route already present in the candidate is a route whether or not anyone has described its work; a component reassigned to a new target after a deletion belongs to a new candidate with its own assessment, and the new candidate's success is not the old one's."
- **CLAIM-n.**
- Could change a verdict: YES, on **O45** and **O46**.

### Part VII: Exact constructions

**D47.** f10 L352 / f11 L337. "listed under attack (B)" → "listed under attack (B) in Part XV". **WORDING** (pointer retargeted to follow D23 and D69).

### Part VIII: Transport results

**D48.** f10: absent / f11 L363. New paragraph: "**Recoding.** A declared, invertible recoding of a carrier preserves the content when a reader who applies the declared convention recovers every pairing (Derivation 8). A section of a carrier filled from another source keeps that other source's history, whatever it happens to match."
- **CLAIM-n.** Derivation 8 covers bijective transport of *all* data. The reader condition and the rule for a patched section are new.
- Could change a verdict: YES, on **O43** and **O44**.

### Part IX: Criticism, use, and standing

**D49.** f10 L384 / f11 L371. Added: "A route that started and did no work, or that was already at rest when the result occurred, is not active for that result; whether a route is active is read from the history, not from the result."
- **CLAIM-a.** Mostly derivable from f10's "nonconstant dependence" and "actual occurrences". "Read from the history, not from the result" is new emphasis.
- Could change a verdict: YES, on **O52** and **O25**; touches **O19**.

**D50.** f10 L406 / f11 L393. Added: "A record reconstructed from the claim it is meant to support is not a receipt for that claim."
- **CLAIM-n.**
- Could change a verdict: YES, on **O16** and **O29**.

### Part X: Understanding, construction, and origin

**D51.** f10 L412 / f11 L399. Dashes → commas (WORDING). Added: "A narrow retained use is what it is: it establishes neither the wider understanding it falls short of nor a permanent inability to reach it."
- **CLAIM-n.**
- Could change a verdict: YES, on **O14** ("has yet to understand").

**D52.** f10 L414 / f11 L401. Added: "A first representation may be constructed from an available problem without prior observation of what it represents."
- **CLAIM-n.**
- Could change a verdict: YES, on **O3** (cards never seen).

**D53.** f10 L414 / f11 L401. Added: "A small binding newly prepared inside received content is construction of that binding, and the rest of the content keeps its inherited provenance."
- **CLAIM-n.** File 10 requires a "nontrivial binding construction"; here a *small* binding is construction of that binding.
- Could change a verdict: YES, on **O18** and **O31**; touches **O15**.

**D54.** f10 L430 / f11 L417. Added: "A dimension of variation mentioned in passing is not thereby a port of the account; it becomes one when the account admits changes to it, and adding it is construction."
- **CLAIM-n.**
- Could change a verdict: YES, on **O23**; touches **O33**.

**D55.** f10: absent / f11 L419. New paragraph "**Ownership.**" It defines "owned by s" as "its processes run inside the system boundary and resource contract declared for s". It adds:
- "Work supplied from outside that boundary, a diagnosis, a decisive question, an instruction about what to read, remains an outside contribution however it is executed inside";
- "a process that runs inside the boundary is the system's own today whoever wrote it";
- "where the boundary is drawn decides, not where the process sits in the casing";
- "Ownership is not defined by the capability it is meant to ground".

**CLAIM-n.** File 10 uses "owned" in Build and Can without defining it. The examples track particular cases:
- "decisive question" tracks O21;
- "instruction about what to read" tracks O41;
- "whoever wrote it" tracks O30;
- "casing" tracks O51.

Could change a verdict: YES, on **O17, O21, O27, O30, O40, O41, O49, O50, O51**.

### Part XI: Progress, knowledge, and the normative

**D56.** Named place ii.
- f10 L438: "For claimed obligations O and protected obligations P, fixed for the comparison," then (P), then "(P) does not rank alternatives."
- f11 L433 adds: "The obligations are declared inputs: O says what is to be repaired and P what is to be protected, each as a stated condition over stated occasions, and a protected condition is lost exactly when it fails on an occasion it covers."
- **CLAIM-c.** Two things change.
  1. O and P become *declared inputs*. With D67, a missing input means an unsettled verdict.
  2. The truth condition for loss of protection changes. f10's (P) checks each protected r only at the two states ξ and ξ′, through r(ξ)⇒r(ξ′). f11 makes a protected condition quantify over its stated occasions, and makes loss a biconditional ("exactly when") on failure at any covered occasion. A failure between ξ and ξ′ therefore counts.
- The formula (P) is unchanged, so the prose and the formula now pull apart unless r is re-read as a predicate over the history.
- Could change a verdict: YES.
  - **O38** ("it was broken, for four seconds") moves toward AGREE.
  - **O35** ("The interruption is … not a loss") moves from AGREE under f10's endpoint reading to SILENT, because no occasions are stated, or to DISAGREE, if the tap's protection is read as covering the four seconds.

**D57.** f10: absent / f11 L433. Added: "Their declaration makes no claim that the aims are worth pursuing".
- **CLAIM-n** (part of the worth cluster).
- Could change a verdict: possible, on **O12**, and on the "mattered" wording in **O35/O38**.

**D58.** f10: absent (ProducedBy is undefined) / f11 L433. Added: "ProducedBy holds when an active route (Part IX) runs from Δ to the repair; it credits each contribution the history establishes, and where two sufficient contributions both ran, both are credited and the history supplies no division of credit that it does not contain."
- **CLAIM-n** (a new definition).
- Could change a verdict: YES, on **O13, O20, O25, O26, O32, O39, O52**.

**D59.** f10: absent / f11 L433. Added: "A correct account that produced nothing, an act that repaired without an account, and a repair produced through use of an account are three different attributions."
- **CLAIM-n.** It is close to the ProducesVia conjunct of (EK) but is new as a statement.
- Could change a verdict: YES, from SPLIT or SILENT to AGREE, on **O13**.

**D60.** f10 L458 heading "Artistic effect, purpose, and aesthetic reason" / f11 L447 heading "Worth, and the normative relation". The new text: "Repairing an obligation establishes that it was repaired; it establishes nothing about whether the obligation, or the question that led to it, was worth having. Where a claim invokes worth, the semantics takes a normative relation N as a declared input and marks the place (Part XIV). The aesthetic case is one such invocation…"
- **CLAIM-c.** File 10 introduces N only for aesthetic value. File 11 generalises N to any claim of worth, and adds that repair establishes no worth.
- Could change a verdict: YES, on **O12** ("its merit is real"), which moves toward SILENT when no N is given.

**D61.** f10 L458 / f11 L447. Added: "…and no aesthetics follows from achieving a stated effect."
- **CLAIM-a.** It follows from "None is defined as another".
- No case.

### Part XII: The physical module

**D62.** f10: absent / f11 L465. New paragraph "**System boundary and continuity.**" Its content:
- a declared boundary and a declared continuity Ω;
- "A replaced part that preserves the declared continuity leaves the same system";
- "a process run inside the boundary is the system's whoever wrote it; a process run outside it is not the system's however close it sits";
- "Both are declared before the attribution, not chosen after it."

**CLAIM-n.** File 10 has β and Ω only as indices.

Could change a verdict: YES, on **O42, O30, O51, O41**.

**D63.** f10 L476 / f11 L467. Added: "Ownership is grounded in the processes and resources the boundary includes, never in the capability being attributed: "owned because it can, and can because owned" grounds neither."
- **CLAIM-n.**
- Could change a verdict: YES, on **O49** and **O17**.

**D64.** f10 L482 / f11 L473. Added: "The population is the set of transports the physics and the stated construction admit; a transport that would need a part every member of the population is built without is not in it."
- **CLAIM-n** (Derivation 3 cluster, not named in the note). It gives a new definition of the population that is found nowhere in Derivation 3. It decides O48 almost word for word: "every device in the stated population is built without that wire".
- Could change a verdict: YES, on **O48**.

### Part XIV: The class collected

**D65.** f10 L519 / f11 L510 (and f11 L33).
- f10: "The **normative relation** N, when a question invokes one."
- f11: "…when a question invokes worth. It is taken as an input and never derived; the aesthetic relation of Part XI is one instance."
- **CLAIM-c.** The scope of N changes from "when a question invokes a normative relation" to "when it invokes worth". Aesthetics becomes one instance. "Never derived" restates f10 L458.
- Could change a verdict: possible, on **O12**.

**D66.** f10 L521 / f11 L512. "Part IV, XII" → "Parts IV, XII"; "— from those" → ", from those". **WORDING.**

**D67.** Named place iii. f10: absent / f11 L514: "**Declared inputs.** Besides the two primitives, some claims take stated inputs that the semantics records and does not supply: the obligations O and P of a repair, with the occasions each covers (Part XI); the scope of a contract and what makes a restriction appropriate (Part III); the system boundary and continuity of an attribution (Part XII). A verdict that depends on one of these is a verdict given the input; where the input is missing, the verdict is unsettled and the semantics says so rather than choosing the input from the verdict wanted."
- **CLAIM-n.** It adds a new category between the primitives and the indices, and a new rule for verdicts: a missing input gives an unsettled verdict.
- It overlaps the indices. Boundary β, continuity Ω and the contract C are still called "declared indices" at L516, and are now also declared inputs.
- Could change a verdict: YES, towards SILENT, on every case where the input is not stated:
  - **O35** (occasions not stated);
  - **O1, O5, O8** (appropriateness of a restriction);
  - **O17, O21, O27, O30, O40, O50** (no boundary stated).
- It decides **O41, O42, O51**, where the boundary or continuity is stated.

**D68.** f10 L525 / f11 L518. Added: "The order is well founded: a representation justified only by its own construction, or an ownership and a capability justified only by each other, has not supplied its place in it, and a separate proof that would supply it counts only when the account uses it."
- **CLAIM-n.**
- Could change a verdict: YES, on **O37** (the uncited textbook) and **O49**.

### Part XV: What defeats this class

**D69.** f10 L531–545 / f11 L524–526.
- A preamble is added: "The load-bearing claims, in the order of how much falls if they fail, each with what would refute it." This comes from f10 L66.
- "None of these is protected by notation…" moves from the end (f10 L545) to the start.
- The entry headings become (A)–(E).
- **ORDER.**

**D70.** f10 L68 and L533 / f11 L528, Part XV (A).
- The attack point and the old entry "A faithful transport that does not explain" are merged.
- "lookup tables" → "a table of observed answers".
- It restates Part V's list of which condition each classic attempt fails.
- "This would show change-fidelity is not enough" and "This refutes sufficiency" are dropped; the heading "Sufficiency" carries them.
- **ORDER.**

**D71.** f10: absent / f11 L528, last sentence: "A table that encodes the response to every admitted change fails none and is an account, so it is not a counterexample; a new attempt must fail none and still explain nothing."
- **CLAIM-c.** It repeats the D39 change ("fails none", "is an account").
- Could change a verdict: low; touches **O33** and **O2**.

**D72.** f10 L70 and L535 / f11 L530, (B). This is f10's Part XV text. The attack's "it may be inadequate" is dropped here but survives in Part VII (L337). **ORDER.**

**D73.** f10 L72 and L537 / f11 L532, (C).
- File 11 keeps the f10 Part XV text: "refutes Derivation 1 and reinstates correspondence as primitive".
- It drops the attack's weaker wording: "Derivation 1 says this is impossible; a counterexample would reopen the question whether correspondence must be primitive after all".
- **ORDER.** Both wordings were in file 10, and the stronger one is kept.

**D74.** f10 L74 and L539–541 / f11 L534, (D). Named place i.
- f10 attack: "Show either that a selected transport can be non-underdetermined on unseen changes (against Derivation 3)…"
- f10 XV: "**A non-fallible selected transport.** A selection history H⊊C whose survivor is determined on C∖H. This refutes Derivation 3."
- f11: "Any of three: a selected transport whose value at an unseen change is determined by its history although its population admits a differing survivor there (against Derivation 3; a population with no such survivor is the theorem's own qualification, not a refutation); …"
- **CLAIM-c** for the first limb. The other two limbs (the construction-reduction entry, f10 L541, and the primitive-layer limb) are ORDER.
- The refutation condition changes. The new first limb cannot be met: by f11's own definition, if the population admits a differing survivor there, survival on H does not determine the value. The limb therefore describes a contradiction, and under (D) Derivation 3 can now fail only as a "mathematical error".
- Could change a verdict: YES, on **O48**.

**D75.** f10 L76 / f11 L536, (E). The entry moves from the attack list into Part XV and gains "(against Derivation 5)". **ORDER.** File 10's Part XV had no question-finding entry, but its attack list did.

### Part XVI: Derivations

**D76.** f10 L567 / f11 L560. The title of Derivation 3 gains "…their population leaves open". **CLAIM-c** (named place i).

**D77.** f10 L569 / f11 L562. The Claim of Derivation 3.
- f10: "For every (a,b)∈C∖H there exists a transport t′, also surviving on H, with a different value at (a,b)."
- f11: "Let t be selected from a population T … For every (a,b)∈C∖H at which some t′∈T, also surviving on H, has a different value from t, the value of t at (a,b) is underdetermined by H … The presence of an unseen pair alone does not establish that such a t′ exists; it must be admitted, realizable, a member of T, and a survivor of H."
- **CLAIM-c.** An unconditional existence claim becomes a conditional. The new theorem is close to analytic: "underdetermined" is glossed as "survival on H does not distinguish t from t′".
- Could change a verdict: YES, on **O48**; touches **O24**.

**D78.** f10 L571 / f11 L564. The Proof of Derivation 3.
- f10: "Alter L_j(a,b) … to any other admitted relation; the result survives on H…"
- f11: "Where T contains a transport with L_j(a,b) altered … that transport survives … Where T contains no such transport, H is silent on the value at (a,b) and the population fixes it."
- **CLAIM-c.**

**D79.** f10 L573 / f11 L566. The Consequence of Derivation 3.
- "faithful where it was tested and unconstrained where it was not" → "…and, wherever its population admits an alternative, unconstrained where it was not".
- New sentence: "What the qualification gives up is the guarantee of a differing survivor at every unseen pair, and with it the blanket claim that every untested value is unconstrained; a population restriction, a physical relation, or another stated constraint may already fix a value that the history never tested."
- **CLAIM-c.** Minor tension left: "This is why the primitive layer is fallible" is still unqualified.

**D80.** f10 L589 / f11 L582. The Consequence of Derivation 5 adds: "That a question was found says nothing about its worth (Part XI)."
- **CLAIM-n** (worth cluster).
- Could change a verdict: YES, on **O12** ("its merit is real"), which moves toward SILENT or DISAGREE.

**D81.** f10 L593 / f11 L586. The Claim of Derivation 6: "together with declared indices" → "together with declared indices and declared inputs".
- **CLAIM-c.** The base of every definition grows. The proof still cites only "the dependence order of Part XIV", which does not mention declared inputs.
- Verdict effect: only through D67.

**D82.** f10 L623 / f11 L616. Derivation 10 adds: "…and this is Derivation 3's qualification seen from the other side, a population that admits no survivor at the new change."
- **CLAIM-c** (Derivation 3 cluster; not named in the note). It is a gloss.
- No case directly.

### Totals for step 1

There are 82 places, D1–D82.

- **CLAIM: 47.**
  - 2 are meta: D1, D11.
  - 16 are -c: D7, D14, D33, D36, D39, D56, D60, D65, D71, D74, D76, D77, D78, D79, D81, D82.
  - 22 are -n: D8, D31, D34, D41, D44, D46, D48, D50, D51, D52, D53, D54, D55, D57, D58, D59, D62, D63, D64, D67, D68, D80.
  - 7 are -a: D26, D27, D32, D43, D45, D49, D61.
  - That leaves 45 CLAIM places inside the theory.
- **WORDING: 24.** D2, D3, D4, D5, D6, D9, D12, D13, D15, D16, D17, D18, D19, D20, D21, D22, D24 (a group of 14 or more punctuation spots), D25, D28, D35, D37, D42, D47, D66.
- **ORDER: 11.** D10, D23, D29, D30, D38, D40, D69, D70, D72, D73, D75.

D10 is a moved section, ruled ORDER. Its one changed phrase, "invokes worth", is ruled CLAIM at its body location, D65.

**The Derivation 3 cluster** has 10 CLAIM places: D14, D33, D36, D64, D74, D76, D77, D78, D79, D82. The note names Derivation 3 itself (D76–D79) and "three sentences". In file 11 those sentences are only two places: D14 (grievance 3), and D74, which is both "attack point (D)" and "the Part XV entry" because the two were merged. The note does not name D33, D36, D64 or D82. **D64 is a new definition of the population**, and it alone decides O48.

**The worth cluster** has 6 places: D7, D57, D60, D65, D80, and the phrase in D10.

**Case index.** This lists which CLAIM places touch each case. Every case except O10, O11 and O22 has at least one new or changed CLAIM sentence aimed at it:
- O1: D31, D67
- O2: D41 (D39/D71 low)
- O3: D52
- O4: D26, D27
- O5: D31, D67
- O6: D26, D27
- O7: D43
- O8: D31, D67
- O9: D26
- O12: D7, D57, D60, D65, D80
- O13: D58, D59
- O14: D51
- O15: D53
- O16: D34, D50
- O17: D55, D63, D67
- O18: D53
- O19: D49
- O20: D8, D58
- O21: D8, D55, D67
- O23: D54
- O24: the D3 cluster
- O25: D49, D58
- O26: D8, D58
- O27: D8, D55, D67
- O28: D34
- O29: D34, D50
- O30: D55, D62, D67
- O31: D53
- O32: D8, D58
- O33: D39, D54, D71
- O34: D32
- O35: D56, D67 (D7)
- O36: D44
- O37: D68
- O38: D56 (D7)
- O39: D8, D58
- O40: D8, D55
- O41: D55, D62, D67
- O42: D62, D67
- O43: D48
- O44: D48
- O45: D46
- O46: D46
- O47: D45
- O48: D1, D14, D33, D36, D64, D74, D76–D79
- O49: D55, D63, D68
- O50: D8, D55, D67
- O51: D55, D62, D67
- O52: D49, D58

Many of the new sentences reuse the vocabulary of particular cases: "bell…tide", "or an instrument", "decisive question", "instruction about what to read", "whoever wrote it", "casing", "a part every member of the population is built without", "started and did no work", "mentioned in passing".

---

## STEP 2: Cross-references in file 11

Rulings: CORRECT; SLIP (points wrong, but does not change what the sentence claims); CLAIM-CHANGING (points wrong in a way that changes the claim). "unch." means the pointer is unchanged from file 10 and its target is unchanged.

### 2a. Every internal pointer in file 11

| f11 line | Pointer | Target checked | Ruling |
|---|---|---|---|
| L5 | "Derivation 3" | Part XVI §3 | CORRECT |
| L5 | "the answer to grievance 3" | L43 | CORRECT |
| L5 | "attack point (D), the Part XV entry" (as two of "three sentences") | In file 11 these are one place: attack (D) was merged into Part XV (D) at L534. The only other (D) is the L63 summary, which carries no qualification. | **SLIP** (X1) |
| L5 | "the audit's case O48", "(Semantics results S75)" | Outside the document: a case identifier and a results file | **not internal**; flagged (X2) |
| L13 | (Part II, Derivation 1) | Kinds are edit-signatures; D1 | CORRECT |
| L15 | (Part IV) | Three provenances | CORRECT |
| L17 | (Part III, Derivation 5) | Contracts have provenance; D5 | CORRECT |
| L19 | "Part XV lists what would count" | Part XV | CORRECT |
| L25 | (Derivation 9) | Output descriptions do not determine accounts | CORRECT |
| L27 | (Parts XI, XIV) for "Where a claim needs one of these [objective aesthetics, probability of truth, merit function, measure of worth, ranking of thinkers], the semantics takes it as a declared input" | Part XI takes N as a declared input for worth and aesthetics only. Part XIV names N as a primitive and lists declared inputs (O, P and occasions; scope and appropriateness; boundary and continuity). Neither Part takes a probability of truth, a merit function or a ranking of thinkers as a declared input. | **SLIP** (X3): the target covers 2 of the 5 items |
| L27 | (Part XI) for division of credit | ProducedBy, L433 | CORRECT |
| L33 | "in the order Part XIV states"; (Derivation 6) | Dependence order; D6 | CORRECT |
| L39 | (Part II, "Kinds are edit-signatures") | L113 | CORRECT |
| L43 | Derivation 3 | The restatement matches the new D3 Claim, qualification included | CORRECT |
| L45 | (non-vacuity, Part V) | L259 | CORRECT |
| L49 | Part IV; Part XV | "Neither provenance is reducible"; XV (D) second limb | CORRECT |
| L51 | (Part VII) | Exact constructions | CORRECT |
| L53 | Part XI | Worth and the normative relation, the aesthetic case | CORRECT |
| L55 | (Parts IV, XII) | Selected; Selection in the physical module | CORRECT |
| L57 | Derivation 7 | §7 | CORRECT |
| L59 | (Part II) | Kinds | CORRECT |
| L63 | "stated exactly in Part XV"; (A)–(E) | Part XV (A)–(E) | CORRECT. The (D) summary lacks the D3 qualification; see D23. |
| L115 | (Part III) | unch. | CORRECT |
| L157, L191, L199, L227 | Part IV; Part V; (Part X); Part X | unch. | CORRECT |
| L161 | (Part VIII) | Historical index, "A new index is a new claim" | CORRECT |
| L197 | (Derivation 3) | New D3 | CORRECT |
| L225 | (Derivation 4); (Derivation 3) | §4; §3 | CORRECT |
| L247 | (Derivation 1) | §1 | CORRECT |
| L273 | (Part III) | The respect is the query (identification question) | CORRECT |
| L275 | "(the bell does not explain the tide)" | No bell and no tide appear anywhere in the document. This is the content of case O2. | **SLIP** (X4): dangling, points outside the document. The rule in the sentence stands without it. |
| L279 | (Part IX) | unch. | CORRECT |
| L283 | Derivation 1 | unch. | CORRECT |
| L309 | (Derivation 9) | "Parallel and priority wiring are an instance" | CORRECT |
| L313, L323 | (B); Part II | unch. | CORRECT |
| L337 | "attack (B) in Part XV"; (O) | XV (B), L530, names eliminative explanation as "the exposed case"; (O) L102 | CORRECT. Retargeted from f10's Part 0 attack list. |
| L363 | (Derivation 8) | D8 is transport of ALL carriers and data along bijections. It supports the invertibility half, not the condition about a reader applying the convention or the rule for a patched section. | CORRECT (loose) |
| L399 | (R); (Part XII) | unch. | CORRECT |
| L419 | (Part XII) ×2 | System boundary and continuity, L465; Owned capability, L467 | CORRECT |
| L433 | (Part IX); (P) | Active route, L371; L430 | CORRECT |
| L447 | (Part XIV); (AR) | Primitives item 2 and Declared inputs | CORRECT. Terminology crosses: N is a *primitive* in Part XIV ("Besides the two primitives…" excludes it from declared inputs), but Part XI and Part 0 L27 call it "a declared input". |
| L510 | "the aesthetic relation of Part XI" | L447 | CORRECT |
| L512 | (Part II), (Part III), (Parts IV, XII), (K), (R), (E) | as named | CORRECT |
| L514 | (Part XI); (Part III); (Part XII) | Repair L433; Scope L161; System boundary L465 | CORRECT |
| L518 | all tags in the dependence order | unch. | CORRECT |
| L528 | (E), (F1), (F2), "Part V says which of the four each classic attempt fails" | Part V "What (E) excludes": table fails (F1), reversed calculation fails (F2), p-because-p fails non-circularity | CORRECT. Two notes: (E) has five conjuncts, while "four conditions" is Part V's count. And (E) here is the Account tag, sitting next to the Part XV heading "(E) Question-finding" at L536. The collision is resolvable from context but new to the body; in file 10 the attack labels lived in Part 0. |
| L530 | (Part VII) | Eliminative | CORRECT |
| L532 | Derivation 1 | §1 | CORRECT |
| L534 | Derivation 3; Part IV ×2 | §3; Three provenances; primitive layer | CORRECT |
| L536 | Derivation 5 | §5 | CORRECT |
| L538 | (I2), (O1), (T2), (CT2), Derivations 1–3 | unch. | CORRECT. D3's "stated assumptions" now include the population. |
| L582 | (Part XI) | Worth, L447 | CORRECT |
| L586–588 | Parts II–XIII; Part XIV | unch. | CORRECT. Gap: the Claim now includes "declared inputs", but the dependence order that the proof cites does not mention them. |
| L596 | (Derivation 5); (Part VIII, historical index) | unch. | CORRECT |
| L614 | (Derivation 4) | unch. | CORRECT |
| L616 | "Derivation 3's qualification seen from the other side"; Derivation 1 | D3's qualification is that the population has no differing survivor of H at the unseen pair, so the population fixes the value. In D10 every member predicts from occupancy, so none differs, and none survives the extended history. | CORRECT (loose) |
| L620 | (Derivation 2) | unch. | CORRECT |

Pre-existing issue, the same in both files: Part VII tags (I1), (I2), (I4) have no (I3). This is a numbering gap, not a pointer.

### 2b. Pointers that are not CORRECT

- **X1 (SLIP), L5.** "The three sentences that restated it (the answer to grievance 3, attack point (D), the Part XV entry)". This describes file 10's layout, where the three were separate: f10 L38, L74, L539. In file 11, attack (D) and the Part XV entry are one entry, L534. The Part 0 short form at L63 is a fourth place and is left unqualified. Separately from the pointer, the note's list is incomplete: D33, D36, D64 and D82 also restate or extend Derivation 3.
- **X2 (flag, not internal), L5.** "the audit's case O48" and "(Semantics results S75)" point outside the document. A case identifier appears inside the tested theory.
- **X3 (SLIP), L27.** "(Parts XI, XIV)" does not carry the claim for a probability of truth, a merit function or a ranking of thinkers. This makes the front matter state more than the body, against L37.
- **X4 (SLIP), L275.** "(the bell does not explain the tide)" refers to an example the document never gives; it is the content of case O2.
- **CLAIM-CHANGING: none found.**

### 2c. Pointers in file 10 that file 11 dropped or retargeted

| f10 | f11 | Ruling |
|---|---|---|
| L38 "There is a theorem below (Derivation 3)" | L43 "Derivation 3 says…" | kept; the content changed (D14) |
| L47 "the semantics forbids that reduction in Part IV" | L49 "Part IV forbids… and Part XV names its refutation" | kept, plus a new pointer; CORRECT |
| L50 "This is worked in Part VII." | L51 "(Part VII)" | kept |
| L68 "all four conditions of Account (Part V)" | L528 "all four conditions of (E)" and "Part V says…" | retargeted from Part V to the tag (E), which is in Part V; CORRECT |
| L70 "Part VII gives the semantics' treatment, and it may be inadequate" | L530 "(Part VII) is the exposed case" | kept; the hedge survives at Part VII L337 |
| L72 "Derivation 1 says this is impossible" | dropped | L532 keeps "This refutes Derivation 1"; no loss |
| L74 "(against Derivation 3)", "(against Part IV)", "Part IV" | L534 | kept; the Derivation 3 limb changed (D74) |
| L238 "This is derived, not assumed (Derivation 4)" | L225 "(Derivation 4)" | kept |
| L352 "attack (B)" | L337 "attack (B) in Part XV" | retargeted, because the full (B) moved from Part 0 to Part XV; CORRECT |
| L521 "(Part IV, XII)" | L512 "(Parts IV, XII)" | wording |
| L533 "This refutes sufficiency." / L535 "This refutes necessity." / L539 "This refutes Derivation 3." | headings "(A) Sufficiency", "(B) Necessity"; "(against Derivation 3; …)" | kept in changed form |
| L541 "Construction reduced to selection" (no pointer) | L534 "(against Part IV, …)" | pointer added from f10 L74; CORRECT |
| f10 attack (E), L76 (no pointer) | L536 "(against Derivation 5)" | pointer added; CORRECT |

The only file-10 pointer whose sentence was dropped outright is f10 L72 ("Derivation 1 says this is impossible"). No file-10 pointer was retargeted to a wrong place.

---

## STEP 3: The three named places (written after steps 1 and 2)

A disclosure first. The task text names these three places, so I knew of them before I began the sweep. The sweep did not depend on that. It was a full, mechanical word-level diff of the two files, and every differing hunk was ruled by the same criteria. None of the three was ruled differently because it was named.

**(i) Derivation 3 and the three sentences restated with it.** Caught. Ruled **CLAIM** at every location.
- Derivation 3: title D76, Claim D77, Proof D78, Consequence D79, all CLAIM-c. The existence claim "for every unseen pair there exists a differing survivor" becomes a conditional that holds only where the population contains one.
- The answer to grievance 3: D14, CLAIM-c ("*always* underdetermined" → "wherever its population admits a differing survivor").
- Attack point (D) and the Part XV entry: D74, CLAIM-c for the first limb. In file 11 these two are one entry (L534). The new refutation condition cannot be met on file 11's own definitions, so Derivation 3 is no longer refutable under (D). The Part 0 short form (L63, part of D23, ruled ORDER) still states the underdetermination without the qualification.
- My sweep also found four more places tied to Derivation 3 that the revision note does not mention. All are ruled CLAIM:
  - D33, Part IV Selected: "The population T is part of the claim…"
  - D36, Part IV Surprise: "…a fact about its population (Derivation 3)"
  - **D64, Part XII Selection: a new definition of the population**, "a transport that would need a part every member of the population is built without is not in it". This settles O48 by itself.
  - D82, Derivation 10: "Derivation 3's qualification seen from the other side…"
- So the note's statement that "one claim changes" understates even the Derivation 3 change.

**(ii) Part XI Repair: "each as a stated condition over stated occasions, and a protected condition is lost exactly when it fails on an occasion it covers."** Caught as **D56**. Ruled **CLAIM** (-c).
- File 10 L438 has only "For claimed obligations O and protected obligations P, fixed for the comparison" and the formula (P). There, protection is checked by r(ξ)⇒r(ξ′), before and after.
- File 11 makes O and P declared inputs, which ties them to the Part XIV rule that a missing input leaves the verdict unsettled.
- File 11 also re-defines loss of a protected condition as failure on any covered occasion, as a biconditional. A failure in the middle of a repair now counts even when the condition holds at ξ and ξ′. The formula (P) is unchanged, so prose and formula diverge.
- It could change the verdicts on **O35** (from AGREE toward SILENT or DISAGREE) and **O38** (toward AGREE).
- The rest of that paragraph is also CLAIM: D57 (worth), D58 (a definition of ProducedBy) and D59 (three attributions).

**(iii) Part XIV "Declared inputs".** Caught as **D67**. Ruled **CLAIM** (-n).
- It is a new category between the primitives and the indices: O, P and their occasions; the scope of a contract and what makes a restriction appropriate; boundary and continuity.
- It carries a new rule for verdicts: where the input is missing, the verdict is unsettled.
- It overlaps the declared indices (β, Ω, C), and it widens Derivation 6 (D81).
- It could change verdicts towards SILENT wherever a case leaves the input unstated: O35, O1, O5, O8, O17, O21, O27, O30, O40, O50. It decides O41, O42 and O51.

The sweep caught all three. There was no place the sweep missed and the naming revealed.

---

## Paths

- This file: /tmp/claude-0/-home-user-ThreadSmith/8d9323da-c0ec-57ec-91fd-8f99ca99320a/scratchpad/s81_det/diffreader1.md
- The word diff used for the sweep: /tmp/claude-0/-home-user-ThreadSmith/8d9323da-c0ec-57ec-91fd-8f99ca99320a/scratchpad/s81_det/wdiff.txt
