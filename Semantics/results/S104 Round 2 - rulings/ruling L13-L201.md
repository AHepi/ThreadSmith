# S104 Round 2 — ruling L13-L201

*Written on 28 September 2026 by a fresh Opus 5.5 checker that built nothing of this round and rules on no other group. Created at once and filled as it went (lesson S28). No theory text, reading rule, addendum, grouping record, tabulation, brief, reply or committed maths file was written, and nothing in `authority/`. The only computations: the program's four claims of this group rerun (`python3 -m model.run --claim FCnn --scale 4 --time-cap 45`, FC77, FC78, FC81, FC82: every status as recorded, and every result sentence as in `search results.json` except that FC82's names the pair ('set(H=1)', 'b1_45') under some hash seeds in place of ('set(H=2)', 'b1_45'), as the program check's §4.1 records, with the same verdict); `s104_creative_transport.py` rerun (output md5 62cac6e63f0cdc6cffac236080eed38a, the card's); and one small script in the scratchpad that reuses the second check's computation B (its Appendix) with the wording ruled below. This file obeys decision S23 except where it quotes the text, a reply, a brief, the external document, the case card, the case files, a program's printout or the owner.*

## Header

- **Group:** L13-L201 (`results/S104 Round 2 - the grouping of the checkers, recorded before any ruling.json`).
- **Lines:** L13, L193, L195, L197, L199, L201 of `tests/103 The semantics, standing alone, after round 1.md` (md5 checked: f31ebb1f050783f1a84f6136cec20fcd).
- **Primary items:** D12.1, D12.2, D12.3, FC77, FC78, FC81, FC82, I52, I53, H05, H13, NF07, E03, C01, C02, C04, C11.
- **Shared items (lines here):** E14 (L201), C03 (L195), C07 (L197).
- **Context items:** E11 (L13), C13 (L195).
- **Read whole:** the reading rule and its two addenda; the grouping record; the tabulation's rows for every item above (parts 13, 14, 15, 17; sections 3, 4, 7, 8); the replies `s104_maths_mimo_13`, `s104_maths_glm_13`, `s104_maths_mimo_14`, `s104_maths_glm_14` (`.response.txt` only), and every other passage of the 34 replies that names an item or a line of this group (by reply line: Mimo part 15, lines 37 and 71; GLM part 15, lines 27 and 81; GLM part 17, line 70; Mimo part 4, line 23); the briefs of parts 13 and 14 whole, and the passages of parts 15 and 17 on NF07 and I52; `formal core.md` §12 and D15.8, D18.1; `formal claims.md` FC77, FC78, FC81, FC82, NF07; the register's I52, I53 and both addenda; `search results.md` for the four claims; `check - program and counterexamples.md` §2, §3, §4.4; `check - formalization against the text.md` whole in its sections 1 to 3 and 6 and the Appendix (H05–H09, H13, T10, T15, R11, R12, R16); the external document's passages 2.2 (doc L87–L121), 3.4 (doc L302–L328) and 4.2 (doc L371–L384) whole, with the items file's entries E03, E11, E14; the case card whole, the case files (README, script, note) and the creative transport inventions addendum (I109–I121); decisions S20–S39 in `records/Semantics - Decisions.md`. The round-1 critical review holds no matter or change on these lines.

**The rulings in one line each.** L13 KEEP. L193 KEEP. L195 FIX (its fourth sentence; settles I52 in one part, I53, H05). L197 KEEP. L199 FIX (its second sentence; settles nothing: the text's own L13 words). L201 KEEP.

## 1. Line by line

### L13

> L13 | A correspondence can be *selected*, produced by variation and survival on a history of encountered changes, with no represented target in that history; or *constructed*, produced by an episode of conjecture and criticism; or merely *declared* by whoever writes the model down.

> L13 | Creativity lives in construction. Selection produces the raw material construction works on. Declaration is used only as a modelling convenience, and a claim about creativity cannot depend on it.

**What challenges it.** C01 (the case card; primary here). E11 (the external reader; context, a finding about scope). No point of Mimo or GLM names L13.

**C01's side.** On the readings where neither Sel nor Con holds (the card's CT8, R2, and R4 with L201 and L411), the case's transport is declared by exclusion, while its pair "was computed, not written"; L13's "merely *declared* by whoever writes the model down" then describes a history this is not.

**The text's side.** L13 does not say how a declared correspondence was produced physically; it says what it counts as: something that stands only because whoever writes the model down enters it. L211 says what that amounts to: "A declared transport does not make an occurrence represent anything; it makes a modeller assert that it does." On the card's "neither" readings the run computed a pair, and its history gives the correspondence neither selected nor constructed provenance; in the semantics its standing as a correspondence is then exactly the modeller's entry, which is what L13 says. The card's "neither" rows rest on I114, I115 and I116 (and the provenance question itself on I111); what a routine's output inherits from the routine's writer is L427's question, not L13's. So C01's argument meets L199's pronoun (ruled below) and not L13, whose "whoever writes the model down" already names the modeller.

**E11.** The external reader warns against reading selection as model-free and construction as model-based learning. L13 makes no such mapping; "Selection produces the raw material construction works on" is read with L201's "that is one arrangement, not a requirement". A finding about scope; nothing in it bears against L13's words.

**Noted, not ruled here.** L13's "produced by an episode of conjecture and criticism" says, as L201's "a constructed one has both" does, that a constructed correspondence's history holds criticism. L197 asks of Con a represented target and not criticism, unless its "episode (Part X)" is a critical episode, which turns on the reading of "episode" (H06, ruled with L55 by group L47-L77). See L201 and the shared notes.

**Ruling: KEEP.**

### L193

> L193 | A transport \(t\) whose domain is an organization of a physical system has exactly one of three provenances, determined by its history in the physical module:

**What challenges it.** FC78 (GLM part 13; the second check), with FC81 (d) and FC82 (one finding); D12.1; I53; H05; C01; C11. One proposal: GLM's `G13-B8`.

````
A transport \(t\) whose domain is an organization of a physical system has exactly one of three provenances, determined by its history in the physical module and carried by each of its parts separately:
````

**GLM's argument for G13-B8.** L201's "Construction may operate on selected material. Selection may continue to operate beneath construction." lets one transport be both selected and constructed in one history, so "exactly one of three" needs I54's rule per part.

**Mimo's argument against it** (part 13, FC78): those two sentences "must be read of the material and the process, not of one transport's own provenance, since the same line denies a selected transport any represented target. That reading keeps both sentences; a precedence rule would override one of them."

**Ruling between them.** Mimo's reading stands. The material a construction operates on is held by other transports, each with its own history and provenance (L405: "the rest of the content keeps its inherited provenance"; L211: "A carrier keeps its provenance"). The transport a construction prepares has, on its one history (L193's "determined by its history", singular; the second check's T10), a construction trace with a represented target; with L195 as fixed below, that history rules Sel out for it, so exactly one provenance holds of it and nothing in L201 needs parts. G13-B8's added clause would have L193 say that a transport with "exactly one" provenance carries it "by each of its parts separately": either one value repeated on every part, which adds nothing, or a value per part, under which a transport has as many provenances as its parts have, against "exactly one". Either way it writes I54 into L193, and whether the text should settle I54 is for the checker that holds I54 (group L405-L429). Rejected.

**FC78, FC81 (d), FC82.** Their counterexample tells against L195's wording, not against L193's claim (see L195 and the items). With L195 fixed, "exactly one" holds on FC78's history (computed below).

**C01 on L193.** "the case's transport has exactly one provenance only because Dec is defined by exclusion" (card line 409). That is how L199 defines it ("Neither of the above"); L193's "exactly one" says that the two provenances with content exclude each other and that the third is the rest. No defect.

**C11.** L193 gives provenance to a transport "whose domain is an organization of a physical system"; (R) asks provenance only of a transport from \(\operatorname{Org}_\ell(o)\) (L205, L213). The provenance question the case raises is about the transports the running computer holds, whose domain is the organization a physical occurrence instantiates. A candidate's transport from a target given only in code (L159's "a mathematical structure") is a transport of Part V, and (E) asks it no provenance. L193 states the scope as meant; I111 is the card's reading, made so that its questions could be asked. No change.

**Ruling: KEEP.**

### L195

> L195 | **Selected.** There is a population \(\mathcal T\) of candidate transports, a variation operator \(\mu\) on \(\mathcal T\), a finite history \(H\subseteq C\) of edit–boundary pairs actually encountered, and a survival condition requiring fidelity on \(H\).

> L195 | A transport **survives on \(H\)** when it is a member of \(\mathcal T\) that meets the survival condition on \(H\); fidelity on \(H\) without membership in \(\mathcal T\) is not survival. No member of the history represents \(t\), \(H\), or the survival condition.

> L195 | The population \(\mathcal T\) is part of the claim: what \(H\) leaves open about \(t\) is what \(\mathcal T\) leaves open (Argument 3).

**What challenges it.** Primary: D12.1, FC77, FC78, FC81, FC82, I52, I53, H05, H13, C02, C04. Shared: C03. Context: C13. Five proposals, copied from the tabulation:

- Mimo `M13-B1` (part 13), the line whole:

````
> L195 | **Selected.** There is a population \(\mathcal T\) of candidate transports, a variation operator \(\mu\) on \(\mathcal T\), a finite history \(H\subseteq C\) of edit–boundary pairs actually encountered in the physical module, at least one pair being so encountered, and a survival condition requiring fidelity on \(H\) and nothing beyond it. A transport **survives on \(H\)** when it is a member of \(\mathcal T\) that meets the survival condition on \(H\); fidelity on \(H\) without membership in \(\mathcal T\) is not survival. No occurrence of the history stands for \(t\), \(H\), or the survival condition, standing for being read in the physical module and not as the representation of (R).
````

- GLM `G13-B2` (part 13), the fourth sentence:

````
No occurrence in the selection history represents \(t\), \(H\), the survival condition, \(t\)'s target, or a criticism: a selected transport has no represented target in its history.
````

- GLM `G13-B6` (part 13), the first sentence:

````
There is a population \(\mathcal T\) of candidate transports — the set of transports the physics and the stated construction admit — a variation operator \(\mu\) on \(\mathcal T\) under which \(t\) has a competitor in \(\mathcal T\), a finite history \(H\subseteq C\) of edit–boundary pairs actually encountered in a physical selection history, and a survival condition requiring fidelity on \(H\).
````

- Mimo `M14-B2` (part 14), the fourth sentence:

````
> L195 | No occurrence of the history represents \(t\), \(H\), the survival condition, or the organization \(t\) carries to.
````

- GLM `G14-B2` (part 14), the third and fourth sentences:

````
> L195 | A transport **survives on \(H\)** when it is a member of \(\mathcal T\) that meets the survival condition on \(H\); fidelity on \(H\) without membership in \(\mathcal T\) is not survival. No member of the history represents \(t\), \(H\), the survival condition, or an organization \(t\) carries to.
````

The points, one by one.

**(a) "No member of the history": a pair cannot represent.** Both readers: the members of \(H\) are edit–boundary pairs, and a pair represents nothing; the maths had to read "occurrences of a physical history" (I52). Mimo and GLM in part 13 say the words must change; GLM in part 14 calls the occurrence reading "forced" and "harmless" and keeps "member" in G14-B2. *Ruling:* the words change. The only history L195 names is "a finite history \(H\subseteq C\) of edit–boundary pairs", so the sentence, read as written, forbids nothing, and the maths had to read it otherwise to give it any content. "Occurrence" is the text's word for what represents (L169: "An **occurrence** is a physically located carrier"; L205), and L481 already makes Sel "a claim about a physical history". GLM's "harmless" does not meet the point that the sentence, read as written, does no work.

**(b) What the history may not represent: H05.** Mimo (part 14) and GLM (part 14): L195 must also forbid a representation of the organization \(t\) carries to, which L197 counts as a represented target; otherwise L195 and L197 let one history give both Sel and Con, and L193's "exactly one" and L223's "the failure is not surprise" fail. Mimo (part 13) and GLM (part 13): the text carries that exclusion at L201 and L411, so FC78 is a counterexample to D12.1 (H05), and the maths must take L201 and L411 in; Mimo there proposes no change for this, GLM gives `G13-B2`. *Ruling:* L195 carries it. The text says three times that a selected transport's history holds no represented target (L13: "with no represented target in that history"; L201: "a selected transport has no represented target and no criticism in its history"; L411: "A selected transport has no represented target in its history"), and L197 names what a represented target is: "\(t\), or the organization it carries to". L195 is the sentence headed "**Selected.**", the one a reader takes as the definition, and it forbids representations of \(t\), \(H\) and the survival condition only. So the text says two things about what a selection history may hold: its definition leaves a represented codomain open, three other sentences rule it out. Read with L195 alone, Sel and Con hold together on one history (FC78, FC81 (d), FC82: the program; the second check by hand); read with L201 and L411, they do not (the second check's computation B). This is a defect of wording that rests on no invention: it is visible by reading L195 beside L197, L201 and L411, and the part-13 side's own argument (the text carries the exclusion) is the reason to state it where the definition stands. The text settles H05's other choice already (L201, L411; the check's T15); the FIX says it at L195 too.

*Which wording.* Mimo's `M14-B2` says "of the history", which leaves open whether the history is \(H\) (pairs) or \(t\)'s physical history. GLM's `G14-B2` keeps the category slip of (a) and says "an organization", where a transport carries to one organization, its codomain, which L197 calls "the organization it carries to". GLM's `G13-B2` says "in the selection history": if the forbidden representations range only over the part of \(t\)'s history in which selection ran, a construction episode in another part of the same history could give Con while Sel holds, which is I53's rejected choice (a) and brings FC78 back; its "\(t\)'s target" can be read as the target of Part V (a transport's domain) as well as the organization it carries to; "represents … a criticism" does not say what L201 says ("no criticism in its history"); and its closing clause repeats L201. The FIX below writes "in the history of \(t\)", which is L193's "its history" and L201's and L411's "in its history" (one history: T10, I53), and "the organization \(t\) carries to", which is L197's phrase.

*Why not "and no criticism".* A criticism alleging a defect in \(t\) or in the organization it carries to has that target available as represented (L383: "an organization represents it as the premise of a criticism alleging a defect in a target"; L429: "a target available before its criticism"), so the FIX already rules such a criticism out, and L201's "no criticism" for a selected transport then follows from the definition.

**(c) "represents" or "stands for" (Mimo's `M13-B1`).** Mimo: "represents" is (R)'s word and (R) needs the provenance D12.1 is defining, so the loop sits in the text; read the forbidden relation in the physical module instead. *Ruling:* keep "represents" in (R)'s sense. Exclusivity rests on Sel forbidding exactly what Con asks for ("available as a represented target", L197, in (R)'s sense). If Sel forbade only a "standing for" read in the physical module, a history could hold an (R)-representation of the codomain (Con) and no "standing for" (Sel), and FC78 would return. "Stands for" is also a term the text nowhere defines. The dependence of Sel on (R) is on representations held by occurrences through their own transports, that is, on the provenance of other transports in the history; whether the text's order places that dependence is E03's matter at L526 (see E03).

**(d) \(H\) nonempty (Mimo's "at least one pair being so encountered"; I52's other choice (b)).** Mimo: L193's "determined by its history in the physical module" and L195's "actually encountered" want an encounter; otherwise Sel can hold with none (FC77's residue). GLM: the text says only "a finite history"; I52 (b) should stay rejected; it cites L41. *Ruling:* no change; I52 (b) stays open. With \(H=\emptyset\), L195's own last sentence and Argument 3 already say what follows: "what \(H\) leaves open about \(t\) is what \(\mathcal T\) leaves open", and where the population holds no differing survivor "the population fixes it" (L574). A selection on an empty history is one whose every value its population fixes; nothing in the text is at odds with that. Mimo's worry, that "selected" keeps no content from an encounter, is not met by nonemptiness either: a history of one pair (the baseline, say) constrains almost as little, so the requirement would change the letter and leave the matter, which is how much \(H\) constrains and is Argument 3's own subject. GLM's L41 does not bear on emptiness; the ruling rests on the reason given here.

**(e) The survival condition: Mimo's "and nothing beyond it" against GLM's "a lower bound".** Mimo: without the narrowing to exactly \(\mathrm{Faithful}_H\), Sel "has no definite content". GLM (part 14): "requiring fidelity on \(H\)" states a lower bound (GLM's appeal to S20's "Good explanations make bad ones harder to fit" is parked, S33, S34, and not weighed). *Ruling:* keep "requiring fidelity on \(H\)". The words ask that survival require fidelity on \(H\); L481 has the survival condition "enacted by the environment", which may require more (L517's Θ carries resources and tolerances). Argument 3 needs only that survivors be faithful on \(H\), and L41 holds whatever else survival requires. Mimo's reason is met by L481: the content of a survival condition is a fact of the physical history, which the semantics takes from Θ and does not write into the definition. The narrow \(\mathrm{Faithful}_H\) of I52 stays a choice of the search. C04's point on the same clause: see the item; it asks for no change.

**(f) GLM's `G13-B6`.** Its three additions. *The population as "the set of transports the physics and the stated construction admit":* L481 already says it, in the sentence that says how Sel is read ("A selected provenance \(\operatorname{Sel}(t;\mathcal T,\mu,H)\) is a claim about a physical history"); whether D12.1 should take L481's equality is H09's, ruled with L481. *"Under which \(t\) has a competitor in \(\mathcal T\)":* GLM rests it on S20's "A variation is a competitor". In S20 the owner speaks of variations of an explanation that compete with it ("If two discovered variations fit, that constitutes a problem"), not of what a variation operator produces in a population of transports; the owner's words do not ask that a selected transport have a competitor, and the clause would be a new condition on selection (a competitor when: before survival, or among the survivors?) that nothing else in the text uses. Insofar as the appeal bears on what hard to vary covers, it is parked. *"In a physical selection history":* L193, in the same paragraph ("determined by its history in the physical module"), and L481 already say it. Rejected.

**(g) H13 ("actually encountered", Mimo's "in the physical module").** Redundant with L193 in the same paragraph and with L481; see H13 under the items. No change at L195.

**(h) C03 (shared; primary with group L205-L211).** With the FIX the non-representation clause keeps (R)'s sense, so, as C03 says, whether it holds of a machine search that codes its own task and scoring turns on the provenance of the code's writing: if that writing is declared, the code represents nothing (L211) and the clause holds; if it is constructed, the case table represents \(H\) and the scoring the survival condition, and the clause fails (as it already does under the present wording, which names \(H\) and the survival condition). Whether such a search can have selected provenance at all is recorded as a question for the owner (below); the present wording, and the FIX, state the matter through (R), as the owner's words leave it: they say nothing on it.

**(i) C02 on L195** (primary here): "The novelty archive beneath it retains by novelty, with no fidelity condition. Neither profile, and not L195's survival condition, describes these." L195 says when a transport is selected; a retention by novelty with no fidelity condition is not a selection in L195's sense, and L201 says only that selection "may" operate beneath construction. Nothing to change.

**(j) C13 (context).** The no-history population holds no pair meeting (E), as L481's second clause says, and Argument 3 works as written on the noninverted history: this bears on L195's last sentence working as written.

**The computation.** The second check's computation B, rerun in the scratchpad with Sel forbidding representations of \(t\), \(H\), the survival condition and the codomain (the FIX): on FC78's history (`prov_counterexample()`, whose one representation is `('o1', 'cod')`), D12.1 as written gives Sel, Con, Sel on \(H\cup\{x\}\): `True True True`; with the FIX: `False True False`. So "exactly one" holds there (Con only), FC81 (d)'s transport is not surprised (Surp needs Sel), and FC82's selection response on the same history fails. On the case (CT8, rerun), R3 under D12.1 gives both provenances and with L201 and L411 read in gives constructed only; the FIX gives the second.

**Ruling: FIX.**

- **old** (the fourth sentence): `No member of the history represents \(t\), \(H\), or the survival condition.`
- **new:** `No occurrence in the history of \(t\) represents \(t\), \(H\), the survival condition, or the organization \(t\) carries to.`
- **Why this wording and not the text's:** the text's sentence forbids nothing (its "members" are pairs) and, read as meant, leaves a represented codomain open in a selection history while L13, L201 and L411 rule it out and L197 makes it Con's represented target; so L195 and L197 let one history give both provenances, against L193. **Why not a reader's:** see (b): `M14-B2` leaves the history unnamed; `G14-B2` keeps the slip; `G13-B2` narrows to "the selection history", which reopens FC78, and says less exactly what it adds; `M13-B1`'s "stands for" parts Sel from Con's (R) and adds (d) and (e), rejected above; `G13-B6` is rejected under (f).
- **Settles** (rule 6), each stated in so many words: the text should now settle **I52** in one part only, the reading of "member of the history" as an occurrence of \(t\)'s physical history, since the sentence cannot do its work otherwise and L481 already makes Sel a claim about a physical history (the type of μ, the narrow survival condition, and I52's choice (b) stay open; I52's choice (a) is excluded by L481); the text should now settle **I53** at L195 as it already does at L193 (one history, T10); the text should now settle **H05** at L195 as it already does at L201 and L411: no represented target, neither \(t\) nor the organization it carries to, in a selection history.
- **Other sentences of L195:** KEEP (points (c) to (j)).

### L197

> L197 | **Constructed.** There is an episode (Part X) whose construction trace prepares \(t\), and in which \(t\), or the organization it carries to, is available as a represented target. Write \(\operatorname{Con}(t;h,e)\).

**What challenges it.** D12.2 (through E03 and C07; no reader challenges D12.2); E03 (primary here); C07 (shared; primary with group L47-L77). No wording is proposed for L197.

**The readers.** Mimo (part 13): "the organization it carries to" read as the codomain stands; "Part X" is a placeholder the maths resolves to D13.3, D13.8. GLM (part 13): says what the sentence says. GLM (part 14): the availability clause "is what lets Sel and Con co-hold" — a point about L195, met there.

**E03's argument** (doc L87–L121, whole): (R) needs Sel or Con; Con needs "an episode with a construction trace and a represented target"; Build (L405) prepares "a represented organization" and its trace names "the resulting representation"; so "Rep → Con → Build → Rep", while L526 lists Build without (R) and says the order has no cycle. Its strongest defence, in its words: "“Construction trace” is intended to be independently recognizable from physical processes, role bindings, and transformations, without applying Rep to its output." And: "That could work. But it needs to be the actual definition." Its repair has no exact wording.

**Ruling on E03 for L197.** L197 says what Con asks for; it states no order. Its "available as a represented target" uses (R)'s word, and that dependence is one edge of E03's loop; the other is L405's "prepares a represented organization". Where the dependence belongs is the order (L526), which lists "Build depends on histories, Ownership and (E)" and "(R) depends on (F1)–(F2) and physical provenance", and says "The order has no cycle and no endless descent". What would place L197's use of (R) is a statement, in the order, that the representations Con and Build ask for are held by occurrences through transports whose provenance comes from an earlier part of the history; that is what "no endless descent" needs and the text does not state. That wording belongs to L526 and L405, which other checkers hold. Rewriting L197 to read "represented" through the physical module alone would part Con from (R), and Sel (L195 as fixed) and Con would no longer name the same relation (L195, point (c)).

**C07** (card: "Con asks for "an episode" (L197). Under L55's sentence the run is none … The text's body does not define "episode" by itself."). What "episode" means is H06's (primary, group L47-L77, which rules L55). L197 points to Part X for it. Nothing in L197 changes until that ruling is made; see the shared notes.

**Ruling: KEEP.**

### L199

> L199 | **Declared.** Neither of the above. The transport is entered into the model by its author. Write \(\operatorname{Dec}(t)\).

**What challenges it.** D12.3 (GLM part 13); C01 (the case card). Mimo (part 13): "as a note on how a declared transport comes into a model it needs no clause, and Dec as neither Sel nor Con is what "Neither of the above" says."

**GLM's argument.** \(\operatorname{Dec}:=\neg\operatorname{Sel}\land\neg\operatorname{Con}\) matches "Neither of the above" only once Sel carries L201's exclusion; "the defect is in D12.1, not here". Met by the L195 FIX and by D12.1 taking it in; nothing in L199.

**C01's argument.** "L199's "The transport is entered into the model by its author" … describe[s] a history this is not: the pair was computed, not written."

**Weighing.** The pronoun "its" reads most naturally as the transport's ("The transport is entered … by its author"). On that reading the sentence says something it should not, in two ways that do not rest on the case's inventions: a transport a deterministic routine computed, whose history gives neither provenance, was not entered by whoever made it (C01); and a transport a programmer writes into a system, whose content "remains its writer's contribution" (L427) and which keeps its inherited provenance (L409: "received content used as it was received keeps its inherited provenance"), would be "entered into the model by its author" and so be read as declared. L13 gives the reading meant: "merely *declared* by whoever writes the model down"; and L211 says what it comes to: "it makes a modeller assert that it does". On that reading C01's objection falls (see L13). Mimo is right that the sentence describes and adds no condition, and D12.3 is right to leave it out as a condition; the FIX keeps it a description and makes clear whose entry it describes.

**Ruling: FIX.**

- **old:** `The transport is entered into the model by its author.`
- **new:** `The transport is entered into the model by whoever writes the model down.`
- **Why this wording and not the text's:** the text's pronoun admits the reading that makes a written or computed transport declared by its maker, against L409 and L427; L13's own words close it. **Why not a reader's:** no reader and no item proposed wording for L199. "Whoever writes the model down" is L13's phrase; "a modeller" (L211) would bring a second name for the same person.
- **Settles:** nothing; the text settles the reading at L13.

### L201

> L201 | A physical system may hold selected transports at the object layer and constructed transports at the simulation layer; that is one arrangement, not a requirement. Construction may operate on selected material. Selection may continue to operate beneath construction. Neither provenance is reducible to the other: a selected transport has no represented target and no criticism in its history; a constructed one has both.

**What challenges it.** FC78, FC81, FC82 (their lines include L201), H05, NF07, C02 (primary here); E14 (shared; primary with group L47-L77). No reader, item or finding proposes wording for L201.

**FC78 and H05.** L201's last clause is the text's own statement of the exclusion that D12.1 left out. With L195 fixed, it is what the definition gives. Its second and third sentences are read of material and process (see L193), and stand.

**E14's argument** (doc L371–L384, whole): Argument 3's qualified underdetermination "is sound"; it gives no general discontinuity between selection and construction; an evolutionary search with represented candidates, counterexamples and content-sensitive revision "might qualify as construction rather than pure selection. That is not a contradiction. It shows that “selection” here is narrower than a generic variation-and-selection algorithm." And: "The prohibition on represented targets in selected histories guarantees a classificatory difference. It does not, by itself, establish a mechanistic irreducibility result." **The text's side.** L201's "Neither provenance is reducible to the other" is explained after its colon by what the two histories contain; L13: "The three are told apart by their histories, not their outputs"; L47: "Part IV keeps the two apart by what their histories contain"; and L542 names what would rule it out: "a method that rewrites every construction trace as a selection history without loss". None of these claims a mechanism that construction has and selection lacks beyond what the history contains; the external reader's "classificatory difference" is what the text claims, and its demand asks for more than the text claims without naming a sentence that claims it. No change for E14.

**C02's argument** (card line 410): "L201 tells the two provenances apart by two profiles: no represented target and no criticism, or both. The run's history, on the ordinary sense of "represents", has a represented target (its coded task and the codomain it builds) and no criticism (L383)." **Weighing.** L201 does not claim that its two profiles exhaust histories: a history that holds neither profile is, by L195, L197 and L199, neither selected nor constructed. The finding that the run holds a represented target rests on "the ordinary sense" (I114), and whether the run is constructed on Build (I115) and on the episode (I116). One residue does not rest on the case: "a constructed one has both" says that a constructed transport's history holds criticism, and L197 does not ask criticism of Con unless its "episode (Part X)" is a critical episode (Part X's L429), which turns on the reading of "episode" (H06, primary with group L47-L77). Under rule 6 that residue rests on a reading the text leaves open and ruled elsewhere; so KEEP here, and the matter goes to the shared notes. The archive: see L195, point (i).

**NF07.** See the item: the words stand.

**Ruling: KEEP.**

## 2. Item by item (primary items: what each comes to)

### D12.1 · Selected (L193, L195)

The formal core's D12.1 parts from the words in four places; which should stand, each:
- *"No occurrence represents" for "No member of the history represents".* The maths (I52's reading) stands, and the words now say it (L195 FIX).
- *The non-representation clause limited to \(t\), \(H\) and the survival condition (H05).* The words stand (L13, L201, L411), now written at L195 as well; the maths should change: D12.1's clause should forbid, over occurrences of the history of \(t\), representations of \(t\), \(H\), the survival condition and the organization \(t\) carries to.
- *The survival condition as exactly \(\mathrm{Faithful}_H\).* The words stand ("requiring fidelity on \(H\)", a necessary condition, the rest enacted by the environment, L481); the narrow reading stays a choice of the search (I52).
- *The population by inclusion (H09) and \(H\) possibly empty.* The first is H09's, ruled with L481; the second stays open (L195, point (d)).

Mimo's point that "represents" makes a loop: the words stand; the dependence is placed, or not, by the order at L526 (E03).

### D12.2 · Constructed (L197)

The maths says what the sentence says: a construction trace that prepares \(t\), and \(t\) or its codomain available as a represented target. Two things it takes over: "episode" as any subhistory (D13.8; H06, ruled with L55 by group L47-L77), and "represented" read through (R), which with Build's trace makes the fixed point the formal core itself names (D18.1) and E03 names. The words stand and the maths stands, with H06 recorded; E03's matter belongs to the order (L526).

### D12.3 · Declared (L199)

\(\operatorname{Dec}:=\neg\operatorname{Sel}\land\neg\operatorname{Con}\) is what "Neither of the above" says, and the maths is right to leave the second sentence out as a description (the second check's §4). GLM's point that the formal core is at odds with itself (I53's gloss "Sel has none" against D12.1) is met when D12.1 takes H05's choice in. The words stand, with the pronoun of the second sentence fixed (L199 FIX); the maths stands.

### FC77 · Without a physical witness, selection is met by every transport

A counterexample to the claim's own wording, not to the text: "fidelity on \(\emptyset\) is vacuous" fails because (F2)'s homomorphism clause is a condition on τ as a whole (I18; the second check worked it by hand; rerun here, 494 models, as recorded). Its held part (the trivial witness exactly when τ is a homomorphism, 8,640 models) bears on I52's rejected choice (a), which L481 excludes ("A selected provenance … is a claim about a physical history"), and on the population of one, which L481's equality excludes wherever the physics admits more (H09). Both readers agree it tells against the claim's wording (Mimo: the claim should read "every transport whose \(\tau\) is a homomorphism"; GLM: "the claim's wording was wrong"). The residue Mimo keeps (Sel with \(H=\emptyset\)) is ruled under L195, point (d): the text is coherent on it, and it stays open. No text change comes from FC77. GLM's hand attack on the held part (a pointwise homomorphism clause) was not a model; the second check's hand work and the rerun agree with I18.

### FC78 · Exactly one of three provenances

The counterexample (the program's; reproduced and worked by hand by the second check; rerun here) tells against the text's wording at L195, not against L193's claim and not only against an invention. The two readers' sides: in part 13 both say it is a counterexample to D12.1 (H05) and not to the text, since L201 and L411 state the exclusion; in part 14 both say, of FC81 (d), which is one finding with it, that it tells against the text through L195's gap. The two sides agree on the facts; what they differ on is whether a definition that says less than three other sentences of the same text is a defect of the text. It is (L195, point (b)): L195 and L197, read as the definitions they are, let one history give both provenances, which L193, L201 and L411 deny. The FIX at L195 removes it (computation B rerun: Sel `False`, Con `True`). What it rested on besides: I53 (one history: the text's, T10), I54 (not used by the finding once L195 is fixed; L193, point on G13-B8), I56 and I90 (Prepares and the history set by hand), I92 (the pole). GLM's per-part L193 is rejected (L193).

### FC81 · Argument 4, and who can be surprised

- *(a)–(c), held by construction.* Two hand attacks, each checked by hand here (the program holds these parts by construction and cannot represent the readings used).
  - GLM's (\(H\not\subseteq C\)) dies on L195's "a finite history \(H\subseteq C\)", as GLM says.
  - Mimo's (part 14 reply line 52: \(t\)'s own history \(H=C\), and a second population in which \(t\) survives on \(H'=\{(a_1,b_0)\}\) and fails at \((a_2,b_0)\notin H'\)) cannot be built under the maths' reading, in which survival on \(H\) is (F1) and the (F2) equation at every pair of \(H\): \(t\) would have to be faithful at \((a_2,b_0)\in C=H\) and fail there. It can be built under GLM's historical reading of H07 (survival on \(H\) a fact about the encounters when they occurred), and then it tells against D12.7's "for some" binding, which lets another history witness surprise while \(t\)'s own history exhausts \(C\), against L223's "A system whose history exhausts its contract cannot be surprised". The words give \(t\) one history (L217: "where \(t\) is selected, history \(H\)"; L193). So it tells against the maths' binding (H07, ruled with L217–L225), not against the text.
- *(d).* One finding with FC78 (the second check). It tells against L195's wording through the same gap, and goes with the FIX: on its history Sel fails, so Surp fails, and "Con(t) ∧ Viol ⇒ ¬Surp" holds there. L223's "a constructed one that fails at an actually occurring pair of its contract is violated, and the failure is not surprise" then follows from the definitions, as Mimo says; L223 is in no checker's group and nothing is proposed for it. The narrow violation (I50) on which (d) is stated is ruled with L220.

### FC82 · The two responses to a violation have no common result

One finding with FC78 for what it shows about provenance. The recorded model computes no response (\(t'=t\), no violation, no μ step: H08), so as recorded it tells against the model's reading of "response" and, through L195's gap, against the text. The FIX removes both the recorded case (computed: Sel on \(H\cup\{x\}\) `False`) and the second check's stronger case (\(\mathcal T=\{t,t'\}\), \(\mu(t)=\{t'\}\), the same history giving Con(t′) through the represented codomain, which is the organization \(t\) carries to as well: Sel(t) fails there, so SelResp fails; reasoned by hand, the stronger case not being in the program). What remains is for L225 (group L217–L225: D12.8, H08, FC83): D12.8 does not ask that the result of a selection response be selected, so a history in which μ yields \(t'\) while a separate trace prepares \(t'\) and represents the organization \(t'\) carries to (a different organization from \(t\)'s, since members of \(\mathcal T\) differ in relations, I71) is not excluded by the definitions; whether that is a selection response at all is L225's question. GLM's `G14-B3` (L225) is that group's to rule.

### I52 · Selection: the parameters witnessed in a physical history

- *Settled by the text:* the physical witness (L481: "A selected provenance … is a claim about a physical history: a population of candidate transports, a physically admitted variation operator, and a survival condition enacted by the environment"; L193), so I52's other choice (a) is excluded; the population as the whole admitted set (L481; H09, ruled there).
- *Should now be settled:* "member of the history" read as an occurrence of \(t\)'s physical history. The FIX at L195 writes it (settles I52 in this part).
- *Should stay open:* the type of μ (Mimo: "a variation operator on \(\mathcal T\)" fixes no type, and nothing turns on it); the survival condition as exactly \(\mathrm{Faithful}_H\) (the words ask only that it require fidelity on \(H\); L195, point (e)); \(H\) required to be nonempty, I52's choice (b) (L195, point (d)).
- GLM's appeal to S20's "A variation is a competitor" to require a competitor: rejected on its argument (L195, point (f)). GLM's part-14 appeal to S20 on the strength of survival conditions: parked.
- C04's point on the extent of "fidelity": see C04.

### I53 · 'Exactly one of three provenances': one whole history

The text settles it: L193's "determined by its history", singular (the second check's T10), and L201's and L411's "in its history". What the register calls its mechanism, "Con then excludes Sel (Con puts a represented target in that history; Sel has none)", was a hope while L195 forbade less than L201 (GLM, part 14); with the FIX it follows from the definitions. Its other choice (a) (different parts of the history, with a rule of precedence) is not needed: L201's "Construction may operate on selected material. Selection may continue to operate beneath construction." is read of material and process (L193). The FIX writes "the history of \(t\)" at L195, the same one history (settles I53 at L195 as the text already does at L193). One reading this leaves to be recorded: new inventions, 1.

### H05 · Selection limited by L195 alone; L201 and L411 left out (D12.1)

The text settles its other choice: L13 ("with no represented target in that history"), L201 and L411, as the second check found (T15). Both readers agree the text carries it; they part on whether L195 should say it. It should (L195, point (b)); the FIX writes it at L195 (settles H05 at L195), and D12.1 should take it in. With it, FC78, FC81 (d) and FC82 go on their models (computed by the second check and here), FC83's recorded counterexample goes as far as it rests on H05 (its other part rests on H08 and I56, ruled with L225), and FC84's second sentence ("Sel's history holds no represented target (L195)") says what L195 now says.

### H13 · "actually occurring" as a primitive with no entry (D11.5)

The text settles where "actually encountered" and "actually occurring" are read: in the physical module (L193: "determined by its history in the physical module"; L481: "a claim about a physical history"; L31: Θ "says what organization a physical occurrence instantiates at a grain"). What H13 records is that the maths' primitive Occurs has no invention number: a matter of the register, which the second check's entry already records; it is no move. L195 needs no words for it (Mimo's "in the physical module" would repeat L193 in the same paragraph). GLM's `G13-B13` on L217 is for the checker of L217 (group L217–L225), where H13 is shared.

### NF07 · L201, "Neither provenance is reducible to the other"

Not formalized, since "reducible" is defined nowhere. The words stand. The colon clause says what the irreducibility consists in, a difference in what the histories contain, and L542's "(Prov) Genesis" says what would rule it out: "a method that rewrites every construction trace as a selection history without loss". The formal part is exclusivity (FC78, after H05) together with that difference. E14's "a classificatory difference … not … a mechanistic irreducibility result" describes what the text claims, not a defect (L201). C02's point is ruled under L201. The maths may formalize L542's "rewrites … without loss" when "without loss" is given a reading; nothing asks for it now.

### E03 · Representation and construction appear to depend on each other

It tells against the text, at L526, and not against L197's sentence. The dependence it names is on the text's words: Con asks for a represented target (L197), Build prepares "a represented organization" and its trace names "the resulting representation" (L405), and (R) asks for Sel or Con (L208). L526 lists "Build depends on histories, Ownership and (E)" and "(R) depends on (F1)–(F2) and physical provenance", and says "The order has no cycle and no endless descent". That last clause holds only if the representations Con and Build ask for are held through transports whose provenance comes from an earlier part of the history (an ordering by stages of the history), which the text does not state. L526's closing warning ("A representation defined only by its own construction … has not supplied its place in the order") names the case that ordering would exclude; it does not supply the ordering, as the external reader says. The result rests on no invention: the formal core's D18.1 reads it off the same words, and I56 (Build's primitives read through Θ) is how the maths kept the loop open, not what made it. The repair (the external reader's has no exact wording) belongs to L526 and L405, which other checkers hold (E03 is shared there). L197: KEEP. What the external reader calls its strongest defence (a construction trace recognizable from physical processes without applying Rep to its output) and an ordering by stages of the history are two ways of placing it; which the text should take is for those lines. The case card's C03 meets the same loop concretely (the run's provenance turns on the provenance of its code's writing).

### C01 · Declared by exclusion; L199's and L13's descriptions

Its first half (exactly one provenance "only because Dec is defined by exclusion") describes how L199 defines Declared and is no defect (L193). Its second half tells against L199's wording, not against L13: L199's "its author" admits the reading under which a computed or written transport is declared by its maker, which L409 and L427 rule out; L13 gives the reading meant, and the FIX at L199 writes it there. On L13 the finding rests on the card's "neither" rows (I114, I115, I116; I111), and L13's "by whoever writes the model down" already describes what such a correspondence counts as (L211). Its last sentence ("Whether a deterministic routine's output is its writer's content (L427) is not said") is L427's (group L427).

### C02 · Neither of L201's two profiles

On the text's words, a history that holds neither profile is neither selected nor constructed; L201 does not claim the profiles exhaust histories. The card's classification of the run (a represented target, no criticism) rests on I114 ("the ordinary sense of "represents""), and whether the run is constructed on I115 and I116; under rule 6 the finding is recorded against those readings, and it changes no line by itself. The residue that does not rest on the case (L201's and L13's "criticism" in every constructed history, against L197, which asks only a represented target) turns on the reading of "episode" (H06), ruled with L55 (shared notes). The archive's retention by novelty is not a selection in L195's sense, and L201's "may" asks nothing of it. Whether a machine search that codes its own task can be selected at all is recorded as a question for the owner. No change to L195 or L201 from C02.

### C04 · The extent of "fidelity" in L195's survival condition

The text settles the extent at the level of L195's words: survival must require fidelity on \(H\), and fidelity is Part V's component and global conditions (L189: "A transport is **faithful on \(C\)** when it meets the component and global fidelity conditions of Part V"), not the answers alone (L23: "Fidelity is over **component structure under change**, not over outputs"). So an answer-only survival condition, the experiment's own, is not one L195 names, except that on the eight cases both pick the same two pairs (CT2). On the four noninverted cases they part (CT5), and that divergence rests on I110 (λ of the receiver ranging over both polarities; I110's other choice, with the polarity's own component in λ, removes the constraint that makes fidelity keep two pairs) and I113. Which conditions "fidelity" includes (narrow or wide, I49) is ruled with the group that holds I49. Argument 3 holds for an answer-only survival condition a fortiori (it constrains less), so nothing in the text needs it to be fidelity for Argument 3's sake; the text asks fidelity because it is the correspondence, not its outputs, that selection shapes (L21: "history says how that organization came to track another"). No change; the card's finding is recorded against I110 and I113.

### C11 · Provenance only for a transport whose domain is a physical system's organization

The text settles the scope, and the scope is meant: provenance is asked of the transports a physical system holds, whose domain is the organization a physical occurrence instantiates (L193, L205, L213); a candidate's transport from a target given only in code is Part V's, and (E) asks no provenance of it. The case's provenance questions are about the running computer's transports, which L193 covers; I111 is the card's reading so that they could be asked. No change.

## 3. Shared items (only as they bear on the lines here)

- **E14 (here L201; primary with group L47-L77).** Weighed under L201: the colon clause, L13 and L47 place the difference in what the histories contain, which is what the external reader grants ("a classificatory difference"); no sentence here claims more. L201: KEEP.
- **C03 (here L195; primary with group L205-L211).** Weighed under L195, point (h): the FIX keeps (R)'s sense, so the run's classification turns on the provenance of the code's writing, as C03 says. L195: FIX (for other reasons); nothing in C03 asks a different wording.
- **C07 (here L197; primary with group L47-L77).** Weighed under L197: "episode" is H06's. L197: KEEP.

## 4. Shared notes (for other checkers and the critical review; no ruling on their lines)

1. **Group L47-L77 (H06, C07, E14 primary; L55, L47, L77).** If "episode" is ruled a delimited subhistory (D13.8; Mimo's reading) or L55's history of contract changes (GLM's), neither asks criticism, and then L201's "a constructed one has both" and L13's "produced by an episode of conjecture and criticism" say more than L197 gives: L197, L405 and L411 ask a represented target of construction, not criticism. Then either L197 would need criticism, or L201 and L13 would need to name the represented target alone. I keep L13 and L201 because the matter turns on that reading. Also: FC84's second sentence (L47) rests on H05, and with the L195 FIX L195 says what it says. If the ruling on L55 gives "episode" a definition, L197's pointer "(Part X)" should point to where the definition stands.
2. **Group L520-L526 (FC98; E03 shared, here L526).** E03 tells against L526's listing (my item's finding): Con (L197) and Build (L405) use "represented", the order lists neither dependence, and "no cycle and no endless descent" holds only under an ordering by stages of the history that the text does not state. I keep L197; the placing belongs to L526.
3. **Group L405-L429 (D12.4, I54, H14, C06; E03 shared, here L405; H05 and C02 via L411).** With the L195 FIX, L411 says what L195 says. GLM's per-part rule (`G13-B4`, I54) is not needed for L193's exclusivity (Mimo's reading of L201's second and third sentences, adopted here); whether the text should settle I54 for L405's "the rest of the content keeps its inherited provenance" is that group's. L405's "prepares a represented organization" is E03's other edge. C01's residual question, whether a deterministic routine's output is its writer's content, is L427's. The L199 FIX relies on L409 and L427 as they stand.
4. **Group L217-L225 (D12.7, D12.8, H07, H08, FC83; H13 shared, here L217).** Mimo's hand model under FC81 (part 14 reply line 52) tells against D12.7's "for some" binding under GLM's historical reading of H07; checked by hand here. FC82's residue (D12.8 does not ask that the result of a selection response be selected) is recorded as a new invention below. H13: the text places occurrence in the physical module (L193, L481, L31); whether L217 should say so (`G13-B13`) is that group's.
5. **Group L481 (H09, D15.8).** FC77's population-of-one witness goes once D12.1 takes L481's equality; `G13-B6`'s population clause was not written into L195 because L481 says it.
6. **L223** is in no checker's group. With the L195 FIX, its "a constructed one that fails at an actually occurring pair of its contract is violated, and the failure is not surprise" follows from the definitions.

## 5. New inventions (choices no register entry records)

1. **"The history of \(t\)" as the history by which \(t\) came to be.** L193 ("its history"), L195 as fixed ("the history of \(t\)"), L201 and L411 ("in its history") are read as the history that produced \(t\), including any episode whose trace prepares it and the selection that produced it, and not later events in the same system. I53 says "the whole physical history of t up to the attribution", which would count a later occurrence representing the organization \(t\) carries to (for example a simulation layer built over \(P\) that represents \(P\)): a selected object-layer transport would then become neither selected nor constructed, against L201's "A physical system may hold selected transports at the object layer and constructed transports at the simulation layer" and L211's "A carrier keeps its provenance". Not written into the text by this ruling (the FIX uses the text's own "history of \(t\)"); recorded for the orchestrator.
2. **D12.8 does not ask that the result of a selection response be selected.** SelResp(t → t′) asks Sel(t), \(t'\in\mu^*(t)\) and survival of \(t'\) on \(H\cup\{(a,b)\}\), not \(\operatorname{Sel}(t';\mathcal T,\mu,H\cup\{(a,b)\})\); FC82's formal statement assumes it ("Sel(t') excludes Con(t')"). H08 records μ* and "new" and not this.

## 6. Owner questions

1. **Whether a machine search that writes its own task and scoring in code can have selected provenance at all** (the creative transport addendum's example, point 5; C02, C03; GLM part 14 on FC81: "a transport selected by trial and error whose target organization is itself held in a carrier (S26's first example) would then not be selected on that history. Whether that is a misclassification or the truth is FC78's question"). *One side:* L13, L201, L411, and L195 as fixed, say a selected transport's history holds no represented target; if the code's case table, scoring or trees represent \(H\), the survival condition or the organization \(t\) carries to under (R), the run is not selected, and is constructed if L197's episode and trace are met, declared otherwise; this keeps selection blind to its target, which is what lets Argument 3 and surprise turn on the population and the history, and what L542's second disjunct protects. *The other side:* the README's own description ("Training only on the noninverted channel selects an unmodified direct protocol"), and variation-and-selection with a coded fitness in computing generally, call such a search selection; under the text, its class then turns on the provenance of the programmer's writing (C03), a history outside the run. *Ruling on the wording only:* the present wording, and L195 as fixed, state the matter through (R), leaving the answer to the provenance of the code's carriers; the owner's words say nothing on it, and the FIX chooses nothing beyond what L201 and L411 already state.

## 7. Parked points

1. **I52 (GLM, part 14):** the strength of survival conditions as "a live question" under S20's "Good explanations make bad ones harder to fit". Parked (S33, S34); not applied, not weighed.
2. **FC77 and I52 (GLM, part 13):** the appeal to S20's "A variation is a competitor" for the selection population's variation operator. Ruled on its argument as a reading of the owner's words (L195, point (f)); insofar as it bears on what hard to vary covers, parked and not applied.

## 8. Formal claims and definitions to formalize again

- **D12.1** (L195's fourth sentence changed): Sel's non-representation clause over occurrences of the history of \(t\), forbidding representations of \(t\), \(H\), the survival condition and the organization \(t\) carries to (H05's other choice); then rerun **FC77** (quotes L195), **FC78**, **FC81 (d)**, **FC82**, **FC83**, **FC84** (second sentence), **FC95** (uses I52), and the case's **CT8**.
- **D12.3** (L199's second sentence changed): recheck that it stays a description, with no clause.
- Register entries: **I52** (the occurrence reading now the text's), **I53**, and the check's **H05** (now the text's at L195) and **H13** (Occurs to be numbered).

## 9. Quotations compared (rule 11)

Every block quotation `> Lnnn | …` above, and every inline quotation of the text with a line number, was compared by program with the text under review after this file was written; the result is recorded at the end of this file. The readers' quotations relied on were compared by the tabulation (every one used here is recorded there as found at the line named, or, for the brief's own wording, found in the brief). The external document's and the case card's passages quoted here were compared with those files. The one model a reader gave by hand for an item of this group (Mimo's under FC81) was checked by hand; FC77, FC78, FC81 and FC82 were rerun by the program, and FC78's history with the FIX by the scratchpad script.

**Result of the comparison.** Twelve lines of this file begin `> Lnnn | `. Nine are quotations of the text, and each was found at the line it names (" … " joining fragments of one line). The other three are readers' proposals printed in their fence blocks (`M13-B1`, `M14-B2`, `G14-B2`), not quotations; each of the six proposals printed here was compared with the tabulation's copy and found there, byte for byte. Fifty-seven inline quotations of the text with a line number were listed and found at the line named, one of them after its markup was restored (L23's "**component structure under change**"); a second scan, by pattern, of every quoted phrase standing next to a line number found no quotation of the text away from the line it names (its other hits were quotations of the card, the replies, or this ruling's own wording). The quotations of the external document, the case card, the README and the replies (GLM part 14 on FC81; Mimo part 13 on FC78 and D12.3; GLM part 13 on D12.3) were each found in their files. No quotation relied on was left unfound.

END OF RULING
