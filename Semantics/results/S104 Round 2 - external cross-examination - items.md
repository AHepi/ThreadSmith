# S104 Round 2 — the external cross-examination: items

*Log S104, review round 2 (the maths round), 27 September 2026. Written by a Claude subagent while the round's runs were going and before any round-2 reply was opened, under `results/S104 Round 2 - addendum to the reading rule, the external cross-examination, written before any reply was opened.md`. Built by `results/S104 Round 2 - external cross-examination - items, build script.py`, which compared the md5 of the text under review (`tests/103 The semantics, standing alone, after round 1.md`, f31ebb1f050783f1a84f6136cec20fcd) and of the saved document (3aeed4029848cc8ad375f314123eaf66), every quotation of the text with the line it names, and every quotation of the document with the document and with the lines the item names. No theory text was written. This file obeys decision S23 except where it quotes the text or the document.*

**What this is.** The findings of the external cross-examination the owner supplied (`results/S104 Round 2 - external cross-examination supplied by the owner.txt`; "the external reader"), as items E01 to E22 in the document's order. For each: the lines of the document it comes from; the place in the text it bears on, quoted; whether its description of the text matches file 103; the finding in one or two sentences and its evidence (Claude's words); its proposed repair and its other key sentences in its own words; whether it challenges the text; and the S104 formal claims, counterexamples, inventions, entries of the check of the formalization and claims not formalized that touch the same place. The extraction is Claude's; where it and the document differ, the document's words govern (addendum, point 2). The same items are in the `.json` file beside this one.

**Challenges the text.** *yes*: it names a sentence of the text and a defect in it, and goes to a checker (addendum, point 4). *in doubt*: it may challenge a sentence, and goes to a checker (rule 5). *a finding about scope (section 3)*: recorded as a finding about scope, not as a defect (addendum, point 7). *no*: it names no line to change. An item that goes to no checker is still given as context to the checker of any group whose lines it names (addendum, point 4). Nothing here rules on an item.

**Counts.** 22 items: 7 *yes*, 6 *in doubt*, 5 *a finding about scope (section 3)*, 4 *no*. Five examples reproduced on the S104 model as FC-E1 to FC-E5 (`results/S104 Round 2 - maths/formal claims - addendum for the external examples.md`), every one CONFIRMED on the text under review; their inventions are I103 to I108 (`results/S104 Round 2 - maths/inventions register - addendum for the external examples.md`).

**Which copy the external reader examined** is not stated. Every description of the text it gives was compared with file 103 (below, item by item), and each matched; the four lines round 1 changed (L123, L443, L471, L520) are not quoted by it.

## Index

| id | its section | finding | lines of the text | challenges | S104 on the same place | reproduced |
| --- | --- | --- | --- | --- | --- | --- |
| E01 | 1 | What it finds stands | L159, L211, L245, L367, L407, L409 | no | FC19, FC95, FC99, FC68 | — |
| E02 | 2.1 | The contribution test can make irrelevant material “indispensable” | L103, L231, L287, L296, L299, L305, L313 | yes | FC37, FC41, FC38, FC39, FC40, FC42, FC101 | FC-E1 |
| E03 | 2.2 | Representation and construction appear to depend on each other | L197, L208, L405, L520, L526 | yes | FC98, FC78, FC81, FC82, FC83 | — |
| E04 | 2.3, first half | Functional determination does not uniquely identify outputs | L103, L109, L119, L325 | yes | FC02, FC11, FC06 | FC-E2 |
| E05 | 2.3, second half | The families of signatures do not give a sharp classification; kinds beyond the signatures | L11, L121, L123, L124, L125, L127, L558 | in doubt | FC07, FC08, FC09, FC10, FC12, FC13, FC14, … | FC-E3 |
| E06 | 2.4 | The proposed falsification tests are narrower than some of the claims | L17, L61, L277, L536, L538 | yes | FC30, FC31 | — |
| E07 | 3.1 | Neural readout against causal mechanism: a successful test | L37, L127, L151, L159, L606 | a finding about scope | FC99, FC26, FC27, FC28, FC34, FC36, FC35, … | FC-E4 |
| E08 | 3.2 | Surprise: the clearest cognitive mismatch | L25, L221, L223, L584 | a finding about scope | FC81, FC82, FC20, FC102 | — |
| E09 | 3.3, first part | Infant exploration: representable, but not yet classified | L405, L407, L409, L429, L632 | a finding about scope | FC90, FC83, FC84 | — |
| E10 | 3.3, second part | “Predicts from occupancy” does not fix a memoryless predictor | L620, L622, L624, L626 | yes | FC102 | — |
| E11 | 3.4 | Model-based learning: no ready-made psychological distinction | L13, L225, L584 | a finding about scope | FC82, FC83, FC84 | — |
| E12 | 3.5 | Finding questions: recording the event is not explaining its occurrence | L15, L544, L588, L592 | a finding about scope | FC97 | — |
| E13 | 4.1 | Declared indices: objective, or merely conditional | L31, L43, L159, L473, L522, L608 | in doubt | FC30, FC99, FC32, FC50 | — |
| E14 | 4.2 | Selection and construction: separate mechanisms, or separate labels on histories | L47, L77, L201, L411, L542 | in doubt | FC78, FC80, FC84 | — |
| E15 | 4.3 | Exact fidelity and explanatory idealization | L242, L250, L277, L363, L538 | in doubt | FC66, FC104, FC19 | — |
| E16 | 4.4 | Does the argument machinery explain reasoning? | L8, L393, L397, L429 | no | FC56, FC69, FC70, FC72, FC73 | — |
| E17 | 4.5 | The capability conditions and ordinary fallible performance | L466, L479, L495, L509 | yes | FC91, FC92, FC93, FC94, FC110 | — |
| E18 | 5 | Tables (set aside by the external reader) | L269, L536 | no | FC25 | — |
| E19 | 5 | The transport could hide the answer (set aside as open) | L255, L273 | yes | FC23, FC24, FC108, FC20 | — |
| E20 | 5 | Fixed port sets (set aside as repairable) | L105, L425, L590 | in doubt | FC97, FC62 | — |
| E21 | 5 | The finite monotone claim (set aside: no counterexample) | L305 | no | FC37 | FC-E5 |
| E22 | opening, 5 (last paragraph), 6 and 7 | The overall verdict, the revision priorities and the proposed benchmark | L3, L17, L27, L546 | in doubt | FC110, FC109 | — |

## Items

### E01 · 1 · What it finds stands

**In the document.** Lines 13–21 of the saved file.

**The place in the text.**

> L245 | (F1) prevents an assembled match from hiding a decomposition in error. (F2) prevents a set of pieces each faithful locally from hiding a lost shared constraint.

> L211 | A system can represent a theory in error: the transport from carrier to content is faithful while the transport from the content's target to the content fails.

> L407 | An inexplicit representation is not an absent one.

> L409 | A system's realization can use a partial, distributed, or temporally extended representation.

> L159 | a narrowing adopted after a failure is a new claim at a new index (Part VIII)

> L367 | A proposition indexed to a contract remains that proposition when a later theory changes the current contract. A new index is a new claim.

**Its description of the text.** Its descriptions (the three fidelities together; a representation of a theory in error against an erroneous representation; inexplicit, distributed and temporally extended representation; a narrower claim as a new index) match these lines of file 103.

**The finding.** Requiring component, global and question fidelity together keeps an answer that matches the target's from vindicating a proposed mechanism; the text keeps a representation of a theory in error apart from a representation in error, admits inexplicit, distributed and temporally extended representation, and treats a narrowing after a failure as a new claim at a new index. These are strengths; they do not show that the class captures everything called explanatory creativity.

**Its evidence.** Its reading of the text's wording; no example.

**Its repair, in its own words.** None offered.

**Its other words.**

> The strongest part is the combination of component fidelity, global fidelity, and question fidelity. Requiring all three prevents a correct answer from automatically vindicating the proposed internal mechanism.

> These are substantive strengths. But they do not establish that the resulting class captures everything that deserves to be called explanatory creativity.

**Challenges the text.** no: no line challenged. What it says stands counts for nothing either way (addendum, point 5). Its closing sentence bears on L17 through E22.

**S104 on the same place.**

- Formal claims: FC19 ((F1) and (F2) do different work): holds on all models tried; FC95 (a system can represent a theory in error): holds on all models tried; FC99 (Argument 7: an account on C can fail on C'): holds on all models tried; FC68 (a failed answer stays failed): holds on all models tried.
- Counterexamples (`search results.md`): none.
- Inventions (`inventions register.md`): I48, I52, I65.
- Claims of the text not formalized: NF09 (L407).

**Reproduced.** None.

### E02 · 2.1 · The contribution test can make irrelevant material “indispensable”

**In the document.** Lines 25–85 of the saved file.

**The place in the text.**

> L287 | Fix \(\mathcal E\) and a declared restriction operation. For \(W\subseteq\Gamma\), let \(E|W\) retain the commitments in \(W\) with the named background fixed; the commitments of \(E|W\) are \(W\).

> L231 | those the candidate offers as doing the work, whether or not anyone has described their work

> L231 | for \(E|W\), \(t'\) is \(t\) with \(\lambda\) restricted to the components of \(E|W\), and \(\Gamma'\) is \(W\).

> L103 | A deleted component imposes the full relation on its ports.

> L296 | \operatorname{CriticalBlock}(B;W,p)\iff W\in\mathsf S_{E,p}\land W\setminus B\notin\mathsf S_{E,p}. \tag{B}

> L299 | Criticality is relative to the route \(W\) it is assessed in

> L305 | and \(d\) is **globally indispensable**, \(\Gamma\setminus\{d\}\notin\mathsf S_{E,p}\), exactly when \(d\in\bigcap\min\mathsf S\)

> L313 | **Commitments that do no work.** (E) has no condition that each commitment do work. … A commitment \(d\) of a candidate that has a route does no work by itself in it when every route stays a route after \(d\) is added to it and after \(d\) is removed from it

**Its description of the text.** Its descriptions (a route as a subset of commitments that still meets Account; a critical block as one whose deletion destroys that status; deletion keeping the ports; commitments that do no work) match L287–L313 and L103 of file 103.

**The finding.** A critical block (B), and with it “contributory”, “globally indispensable” and “does no work by itself”, is failure of Account after deletion, and Account's (F2) can fail for a reason the question does not turn on; so a commitment that plays no part in the answer can come out critical and globally indispensable. The definitions run together indispensability to the fidelity of the whole organization and contribution to explaining the question.

**Its evidence.** Its Boolean example: k: Y = X and d: V = U, identity transports, Γ = {k, d}, the baseline and every partial setting of X and U (nine edits), unset inputs zero. The full candidate meets the conditions; with d deleted, V is unconstrained, (F2) fails, and the answer about Y is unchanged at every pair, so CriticalBlock({d}; {k,d}, p) holds and d is globally indispensable. It weighs two defences: that d should not have been among the commitments (answered: L313's test is meant to find commitments that do no work, and asking for the relevance judgment first defeats it), and a restriction that removes the disconnected ports (answered: it needs a different restriction operation from the one with an unchanged identity projection).

**Its repair, in its own words.**

> Distinguish structural-fidelity criticality from question-relative explanatory contribution. The latter needs a relevance condition or an explicit question-preserving reduction, not merely failure of Account after deletion.

**Its other words.**

> The definition conflates indispensability to the fidelity of the whole represented organization with contribution to explaining this question.

> A demonstrated classification problem in the interpretation of explanatory contribution. It is not, by itself, a refutation of Account sufficiency: the full candidate still explains Y through k.

**Challenges the text.** yes. It bears on L287–L313 (and, through “the work”, on L231); its own verdict is that it does not rule out sufficiency (L536).

**S104 on the same place.**

- Formal claims: FC37 (the finite monotone claim): holds on all models tried; the example leaves it as it is (FC-E1); FC41 (commitments that do no work): holds on all models tried, on set systems (I30), not on routes computed from a candidate; FC38, FC39, FC40, FC42 (the route examples read as set systems, I30): hold on all models tried; FC101 (Argument 9; uses I29): holds on all models tried.
- Counterexamples (`search results.md`): none of the twelve falls on these lines.
- Inventions (`inventions register.md`): I29 (the restriction operation: deletion, ports and π kept; its first other choice, removal, is made exact as I104 in the addendum), I30, I15.
- The check of the formalization, and the formal core: §2b, I29's row: L231's wording and the register's choice (deletion keeps J_E whole, so λ 'restricted to the components of E|W' restricts nothing).

**Reproduced.** FC-E1: CONFIRMED on the text under review (resting on I29 and I103; variant (a′), d in the named background, meets (E) with Γ = {k}; variant (b′), the restriction of I104, removes the example and changes π, which L231's wording does not).

### E03 · 2.2 · Representation and construction appear to depend on each other

**In the document.** Lines 87–121 of the saved file.

**The place in the text.**

> L208 | \operatorname{Rep}_\ell(o,c)\iff\exists t\,[\operatorname{Faithful}_C(t:\operatorname{Org}_\ell(o)\to c)\land(\operatorname{Sel}(t)\lor\operatorname{Con}(t))]. \tag{R}

> L197 | **Constructed.** There is an episode (Part X) whose construction trace prepares \(t\), and in which \(t\), or the organization it carries to, is available as a represented target.

> L405 | \(\operatorname{Build}_{\beta,\ell}(s,c,h,e)\) is met when an actual subhistory owned by \(s\) and delimited at \(e\) prepares a represented organization for explanatory use of \(c\)

> L405 | A construction trace identifies the controlled processes, the incoming carriers, the bindings constructed, and the resulting representation.

> L526 | (R) depends on (F1)–(F2) and physical provenance. … Build depends on histories, Ownership and (E). … The order has no cycle and no endless descent. A representation defined only by its own construction, or an ownership and a capability each defined only by the other, has not supplied its place in the order

> L520 | Representation, from fidelity and provenance (R). Provenance, from physical history (Parts IV, XII).

**Its description of the text.** Its schematic 'Rep ⇔ Faithful ∧ (Sel ∨ Con)' is (R) at L208; 'construction is described as preparing a represented organization, and its trace includes the resulting representation' matches L405; 'its stated dependency order omits the apparent dependence of Build on representation and then asserts that there is no cycle' matches L526, which lists Build under histories, Ownership and (E); the warning it credits is L526's last sentence.

**The finding.** Read literally, (R) needs Sel or Con, Con needs a construction trace, and Build's trace prepares “a represented organization” and names “the resulting representation”, so Rep → Con → Build → Rep; L526's order lists Build without (R) and says the order has no cycle. L526's warning names the risk and does not supply the missing construction.

**Its evidence.** The dependencies read from the wording of the definitions; a stripped-down instance ('This occurrence represents because it was constructed; it was constructed because the relevant physical process produced this representation'); no model.

**Its repair, in its own words.**

> Define a raw physical construction relation first. Its premises may refer to representations at strictly earlier stages; its output should initially be a carrier with specified structural properties. Then derive representation of that output. A ranked inductive definition would make the intended grounding explicit.

**Its other words.**

> Rep → Con → Build → Rep.

> “Construction trace” is intended to be independently recognizable from physical processes, role bindings, and transformations, without applying Rep to its output.

> That could work. But it needs to be the actual definition.

> An unresolved foundational dependency, not a proof that no coherent version of the framework exists.

**Challenges the text.** yes. It bears on L197, L405 and L526 (and on Argument 6 at L596, which rests on L526's order).

**S104 on the same place.**

- Formal claims: FC98 (Argument 6 and the dependence order): not tested (a property of the definitions' graph); its Look names the same loop, build → prov → rep; FC78, FC81 (d), FC82, FC83: counterexamples on the same definitions (Con, Build), each resting on I56 with Prepares set by hand (I90); they bear on the exclusivity of the provenances, not on the loop.
- Counterexamples (`search results.md`): FC78, FC81 (d), FC82, FC83 (above); none on the loop itself.
- Inventions (`inventions register.md`): I56 (Prepares, BindingConstruction and TransferComposite as primitives: the formal core's way of keeping the loop open, D18.1), I52, I53, I48, I90.
- The check of the formalization, and the formal core: formal core D18.1: 'with “represented” read through (R), Build, Con and Rep are defined together, as one fixed point, unless Con's trace is read without (R)'; H05, T15 (Sel limited by L195; L201 and L411 left out).

**Reproduced.** none: a matter of the order of the definitions, not of a model (FC98 was not tested for the same reason).

### E04 · 2.3, first half · Functional determination does not uniquely identify outputs

**In the document.** Lines 123–145 of the saved file.

**The place in the text.**

> L109 | No role assignment is supplied.

> L109 | A port is an **output** of component \(j\) when its value is determined by \(L_j\) given the other ports of \(V_j\) across \(B\).

> L109 | The direction of an organization is a consequence of which edits it admits, not a stipulation about which way an equation is read.

> L103 | An edit that sets a port replaces the component assigning that port; it does not add an equation beside an incompatible one.

> L119 | An edit that sets a port replaces only the component that assigns the port (above), not the relations of the components that read it

> L325 | Under \(A\) containing interventions on \(H\) and \(\theta\), these ports are inputs and \(L\) is an output, by Part II.

**Its description of the text.** Its paraphrase of the output clause and of 'replacing the component that “assigns” the port' matches L109 and L103.

**The finding.** L109's output criterion makes both ports of the relation {(0,0),(1,1)} outputs, so it does not tell Y := X from X := Y; the edits tell them apart only once it is said which component an intervention replaces, and “the component assigning that port” is neither defined from the edits nor supplied with the data.

**Its evidence.** The relation {(0,0),(1,1)} on two two-valued ports, and 'A finite check'.

**Its repair, in its own words.**

> That assignment relation needs either an independent definition from the edit structure or explicit inclusion in the supplied data.

**Its other words.**

> Thus the literal criterion classes both ports as outputs. It does not distinguish the assignment Y := X from X := Y. A finite check confirms that directly.

> Repairable under-specification.

**Challenges the text.** yes. It bears on L103, L109 and L119 (and on L325's 'by Part II').

**S104 on the same place.**

- Formal claims: FC02 (c): on the pole, H and θ are outputs of c_L as well as L, and the direction is carried by asg, not by output status: holds; FC11 (roles relative to A, families relative to C; round-1 matter 5): holds; FC06: holds.
- Counterexamples (`search results.md`): none of the twelve falls on these lines.
- Inventions (`inventions register.md`): I04 (the assigning component read off the setting edits; its other choice (b), the unique component of which v is an output, 'fails for relational components'), I05, I80, I102.
- The check of the formalization, and the formal core: H03, H04 (direction defined as (Input_A, asg), with no invention number); T13, R14 (the identity edit as a setting edit); R21 (output read at the identity edit); formal core §2, the Vague note.

**Reproduced.** FC-E2: CONFIRMED on the text under review (resting on I05 and I105; the same under I106 (a); only under I106 (b) does output status follow the direction, and then through the setting edits that replace k).

### E05 · 2.3, second half · The families of signatures do not give a sharp classification; kinds beyond the signatures

**In the document.** Lines 140–145 of the saved file.

**The place in the text.**

> L121 | What ordinary language calls a cause, a measurement, a rule or a constitutive status are families of signatures:

> L123 | - a **causal assignment** has a signature that changes under intervention on its output port and is invariant under observation edits;

> L124 | - a **measurement** has a signature invariant under interventions on the measured port and variable under edits to the measuring relation;

> L125 | - a **rule application** has a signature invariant under interventions on the world and variable under edits to the rule.

> L127 | These are descriptions of patterns in (K), not additional data. … In particular, a part that reads or reports another part has a measurement's signature … Which of the two an account offers as producing an outcome is fixed by that signature, not by the account's wording.

> L11 | at any level of detail, a *kind* is nothing over and above how a component responds to the changes that level admits.

> L558 | The word "kind" is therefore eliminable from the definition of an account, and its elimination loses no case.

**Its description of the text.** Its 'proposed signatures of causal assignments, measurements, and rule applications' are L123–L125 of file 103 (L123 as changed in round 1); 'the sharp semantic classification the surrounding prose suggests' points to L121 and L127.

**The finding.** A causal assignment Y := X and a measuring component N := X both keep their relation under an upstream intervention on X, so the families of L123–L125 cannot tell them apart by that; the patterns do not give the sharp classification the prose around them suggests. Argument 1 keeps the text's own signatures under (F1); it does not show that those signatures exhaust every important sense of kind.

**Its evidence.** Y := X against N := X under an intervention on X.

**Its repair, in its own words.** None offered.

**Its other words.**

> For a component Y := X, intervening upstream on X changes the solution but normally leaves the relation Y = X unchanged. A measuring component N := X has the same property. Their distinction cannot come merely from whether their own relation changes under that upstream intervention.

> This is not an argument that measurements cannot be causal processes; they can be. It is an argument that the listed patterns do not automatically provide the sharp semantic classification the surrounding prose suggests.

> Argument 1 establishes preservation of the document’s defined signatures. It does not independently establish that those signatures exhaust every scientifically important sense of kind.

**Challenges the text.** in doubt: goes to a checker (reading rule, rule 5). For L121–L127: whether they say more than the patterns give. For L11 and L558: a question of scope, which bears on (Elim) at L540.

**S104 on the same place.**

- Formal claims: FC07 (under R-i a component that reads a port other than its output is a measurement and not causal on a contract that sets its output; the families differ between the readings on the pole's contract; round-1 change L123): holds; FC08 (L127's gloss has a clause about solutions), FC09 (four names, three families; round-1 matter 4), FC10 (L57 against L123), FC12, FC13, FC14, FC17: hold; FC18 (Argument 1's Consequence): counterexample under I94, a reading the text excludes (the check's T03).
- Counterexamples (`search results.md`): FC18 (above).
- Inventions (`inventions register.md`): I06 (the two readings of observation edits), I07, I08, I09, I102.
- The check of the formalization, and the formal core: H01 and R13 (a composite of settings is no setting edit); H02; R01 (R-i against R-ii).
- Claims of the text not formalized: NF04 (L540, (Elim)).

**Reproduced.** FC-E3: CONFIRMED on the text under review (resting on I06 under both readings and I107; an edit that alters the reading's relation alone separates them).

### E06 · 2.4 · The proposed falsification tests are narrower than some of the claims

**In the document.** Lines 147–173 of the saved file.

**The place in the text.**

> L17 | A candidate would conflict with the conjecture if an argument not using these four ruled out the claim that it is a non-explanation of its question while these four cannot represent it; so would a candidate that meets (E) on its question and contract (Part V) when such an argument rules out the claim that it is an explanation there.

> L61 | (Suff) sufficiency of the four conditions of Account; (Nec) their necessity

> L536 | A candidate meeting all four conditions of (E) on a contract of its question, with a transport whose provenance is not declared (Part IV), such that an argument not using (E) rules out the claim that it is an explanation of what its question asks.

> L538 | A candidate such that an argument not using (E) rules out the claim that it is a non-explanation, whose organization no transport can preserve under any contract on its target.

> L277 | (E) has no condition on how a mechanism came to be guessed

**Its description of the text.** Its 'Part XV asks for a candidate whose organization cannot be preserved by any transport under any contract on its target' matches L538; 'the sufficiency challenge adds a non-declared-provenance requirement' matches L536; 'explicitly does not depend on how the mechanism was guessed' matches L277.

**The finding.** The denial of necessity on a question p is a candidate that explains p and fails Account on p's contract; L538 asks instead for a candidate whose organization no transport preserves under any contract on its target, a much stronger demand. L536 adds to sufficiency a transport whose provenance is not declared, though (E) takes no provenance. A critic can then defeat one claim while the text answers with a weaker one.

**Its evidence.** The two forms it writes out: 'Explains(E,p) ⇒ Account(E,p)' on a specified question, against representability somewhere under some contract.

**Its repair, in its own words.**

> The statements of the central claims and their admissible refutations need to be aligned. Otherwise, a critic can defeat one claim while the document answers by defending a weaker one.

**Its other words.**

> But Part XV asks for a candidate whose organization cannot be preserved by any transport under any contract on its target. That is a much stronger demand on the critic.

> Likewise, the sufficiency challenge adds a non-declared-provenance requirement, although Account itself does not require that provenance and explicitly does not depend on how the mechanism was guessed.

**Challenges the text.** yes. It bears on L17, L536 and L538 (and on L61's summary).

**S104 on the same place.**

- Formal claims: FC30 ((E) takes no assessor, history, provenance or wording): holds; FC31 ('the four conditions', five conjuncts, L536): not tested.
- Counterexamples (`search results.md`): none of the twelve falls on these lines.
- Inventions (`inventions register.md`): I20, I27, I28, I49.
- Claims of the text not formalized: NF01 (L17), NF02 (L536), NF03 (L538).

**Reproduced.** none: it concerns how the claims and their refutations are stated.

### E07 · 3.1 · Neural readout against causal mechanism: a successful test

**In the document.** Lines 187–223 of the saved file.

**The place in the text.**

> L151 | A measure that identifies an outcome, together with a prediction of the outcome from it through a transport faithful on the contract, answers the identification question; whether the measured part also produces the outcome is the production question, and the first answer is not the second.

> L37 | A correlation has no component that responds to an intervention on its supposed input; a cause does.

> L127 | Which of the two an account offers as producing an outcome is fixed by that signature, not by the account's wording.

> L159 | Why the question asked is answered on this restriction and not on a wider one is a substantive, criticizable part of the claim; the semantics records the restriction and supplies no rule that decides it.

> L606 | and \(\mathcal E\) can meet (E) on \(C\) and fail it on \(C'\).

**Its description of the text.** No sentence of the text is described; the example is its own, worked with the text's conditions.

**The finding.** On the memory system M := X, N := M, Y := M, the proposal Y := N meets the matching conditions on cue changes and fails (F1), (F2) and answer fidelity once the contract holds X = 1, do(N = 0); the text forces the distinction between a scoped dependence and a causal attribution. The formalism does not find which intervention isolates the readout, or whether a manipulation also changes the memory.

**Its evidence.** The memory example, with its values at X = 1, do(N = 0): target M = 1, N = 0, Y = 1; proposal Y = 0.

**Its repair, in its own words.** None offered.

**Its other words.**

> In the finite implementation, this intervention breaks F1, F2, and answer fidelity.

> This is a real success for the framework. It forces the distinction between an adequate scoped dependency and a stronger causal attribution.

> The formalism does not discover which neural intervention isolates the readout, or whether an experimental manipulation also changes memory. Those are substantive empirical assumptions.

**Challenges the text.** a finding about scope (section 3): no line challenged. What it credits counts for nothing either way (addendum, point 5).

**S104 on the same place.**

- Formal claims: FC99 (Argument 7): holds; FC26, FC27, FC28 (the pole on the production and identification contracts): hold; FC34, FC36: hold; FC35 (L151's 'prediction' is outside L219's definition; round-1 matter 6): not tested; FC101 (Argument 9): holds.
- Counterexamples (`search results.md`): none of the twelve falls on these lines.
- Inventions (`inventions register.md`): I51, I65.
- The check of the formalization, and the formal core: R09 (the identification contract's edits as boundary variations); R10.
- Claims of the text not formalized: NF08 (L151).

**Reproduced.** FC-E4: CONFIRMED on the text under review (resting on I108).

### E08 · 3.2 · Surprise: the clearest cognitive mismatch

**In the document.** Lines 225–273 of the saved file.

**The place in the text.**

> L221 | - **surprise** is a violation of a selected transport at \((a,b)\notin H\).

> L223 | a constructed one that fails at an actually occurring pair of its contract is violated, and the failure is not surprise

> L584 | Surprise is not a feeling added to the semantics; it is the signature of a selected transport meeting a change outside its history.

> L25 | a probability on claims

**Its description of the text.** Its 'surprise as a fidelity violation by a selected transport at an encountered pair outside its selection history' and 'a constructed transport can be violated, but its violation is explicitly not surprise' match L221 and L223.

**The finding.** (A) A probabilistic model can be faithful and still meet an unexpected outcome (P(B) = 0.01, about 6.64 bits): unexpectedness does not need an unfaithful representation, so identifying surprise with fidelity failure leaves part of the phenomenon out. (B) Two agents with the same expectation and the same response differ only in how the expectation was acquired; the text calls one violation surprise and the other not, and a cognitive application needs an argument that this difference of history marks a difference in the process studied. It grants that the definition is consistent and that Argument 4 follows from it.

**Its evidence.** The probability example (−log2 0.01 = log2 100 ≈ 6.644, arithmetic outside the S104 model, which has no probabilities; the text supplies none on claims, L25, L522); the two agents.

**Its repair, in its own words.**

> Distinguish statistical unexpectedness, subjective prediction discrepancy, recognized model inadequacy, and the provenance of the expectation. Those can interact without being defined as the same thing.

**Its other words.**

> Unexpectedness does not require an objectively unfaithful representation.

> That distinction may be useful for classifying histories. But a cognitive application needs an argument that this historical distinction identifies a relevant difference in the psychological process being studied.

> A strong coverage objection to a general cognitive application, not a counterexample to the definitional theorem.

**Challenges the text.** a finding about scope (section 3): no line challenged. Its point (B) meets FC81 (d): on the formal core, without L201 and L411 (H05), one transport can be selected and constructed on one history and be surprised.

**S104 on the same place.**

- Formal claims: FC81 (Argument 4): counterexample in part (d), resting on I52, I53, I56, I90; FC82: counterexample (a transport the result of both responses); FC20 (violation in either extent): counterexample with non-injective value maps; FC102 (a) (surprise in the worked case): not tested.
- Counterexamples (`search results.md`): FC81 (d); FC82.
- Inventions (`inventions register.md`): I50, I51, I52, I53, I56, I90.
- The check of the formalization, and the formal core: H05, R11 (Sel limited by L195); H07 (surprise with the selection parameters bound by 'for some'); H08.

**Reproduced.** none in the S104 model (the probability example is arithmetic, checked by hand).

### E09 · 3.3, first part · Infant exploration: representable, but not yet classified

**In the document.** Lines 275–300 of the saved file.

**The place in the text.**

> L632 | This episode is a relative-consistency instance for the class. It is not a claim that any actual infant, animal, or program instantiates it.

> L405 | Reconstruction by a learner is construction; relay is not.

> L407 | None of (R), Deploy and Build asks whether the relevant distinctions and transformations are written in a particular format

> L409 | A construction trace may therefore identify a binding constructed in the subhistory by its use rather than by a statement of it

> L429 | A **recognized difficulty** is a failure of a claimed aim, or a conflict in which what the system holds meets a claimed aim only by failing a protected one (Part XI), when the system represents it.

**Its description of the text.** Its 'It explicitly says this is not an attribution to an actual infant, animal, or program' matches L632; 'The document allows tacit representations' matches L407–L409.

**The finding.** Behaviour after an expectation-violating event is compatible with the framework, but does not show that the learner represented a defect in its own account, or built a new binding rather than recruiting an existing capacity; allowing tacit representation does not show that the representations Build or a critical episode need were present. Representability succeeds while the empirical classification stays underdetermined.

**Its evidence.** Its two cross-examination questions; no example worked.

**Its repair, in its own words.** None offered.

**Its other words.**

> What evidence determines that the infant represented a defect in its own account, rather than changing attention or exploratory behavior after an unexpected event?

> The document allows tacit representations, so demanding verbal reports would be an unfair test. But allowing tacit representations does not establish that the particular representations required by Build or a critical episode were present.

> The empirical behavior is compatible with the framework. It does not identify the framework’s proposed internal provenance or establish CreateEx.

**Challenges the text.** a finding about scope (section 3): no line challenged.

**S104 on the same place.**

- Formal claims: FC90 (the worked case's '(EX) is met' against (EX)'s conjuncts): not tested; FC83, FC84 (only construction is originative; every creative attribution requires construction): FC83 a counterexample, FC84 holds.
- Counterexamples (`search results.md`): FC83.
- Inventions (`inventions register.md`): I55, I56, I60, I68.
- The check of the formalization, and the formal core: H15 (the four parts of a critical episode).
- Claims of the text not formalized: NF09 (L407), NF10 (L429).

**Reproduced.** none.

### E10 · 3.3, second part · “Predicts from occupancy” does not fix a memoryless predictor

**In the document.** Line 295 of the saved file.

**The place in the text.**

> L620 | The sensory field is the occupancy of cells, which cells are filled, without which thing fills them.

> L622 | \(S_0\) predicts occupancy from recent occupancy. It is faithful on \(H_0\).

> L624 | \(S_0\), predicting from occupancy, predicts nothing there and is violated when the thing re-emerges at a cell consistent with its velocity.

> L626 | If the population's transports can only predict from occupancy, no member survives the extended history: the fidelity failure is structural, not parametric.

**Its description of the text.** Its 'the document's final example describes a selected occupancy predictor failing under occlusion' matches L620–L626.

**The finding.** A predictor from occupancy histories can carry information through an occlusion, so “predicts from occupancy” does not by itself give a memoryless predictor; for no member of a selected population to survive the extended history, the population's state and memory restrictions have to be stated, not only its sensory input.

**Its evidence.** The remark; no model worked.

**Its repair, in its own words.**

> To establish the claimed impossibility for a selected population, one must specify its state and memory restrictions, not just describe its sensory input.

**Its other words.**

> There is also a technical caution about the occupancy example. “Predicts from occupancy” does not, by itself, establish a memoryless architecture. A predictor using occupancy histories may preserve information through occlusion.

**Challenges the text.** yes (a finding of section 3 that bears on sentences of the text, L622 and L626; addendum, point 7). The same point as the S104 counterexample to FC102 (b), which the reading rule already sends to a checker (rule 5, the twelve).

**S104 on the same place.**

- Formal claims: FC102 (b), second half: counterexample (computed: not as claimed): on I68's encoding with I100's occlusion, a window longer than the occlusion lets an occupancy predictor extrapolate, so the failure is not structural; with two things a window predictor can fail with no occlusion at all; FC102 (b), first half (an occlusion that outlasts the window): computed as claimed; (a), (c): not tested.
- Counterexamples (`search results.md`): FC102 (b), second half.
- Inventions (`inventions register.md`): I68, I100, I52.
- The check of the formalization, and the formal core: H17 (two things that may share a cell and pass through each other); R22.

**Reproduced.** none new: FC102 (b) is the S104 computation of the same point.

### E11 · 3.4 · Model-based learning: no ready-made psychological distinction

**In the document.** Lines 302–328 of the saved file.

**The place in the text.**

> L13 | Creativity lives in construction. Selection produces the raw material construction works on.

> L225 | A **selection response** extends the history \(H\) of a selected transport and lets \(\mu\) act: the transport is re-tuned within the population. A **construction response** introduces a new organization or a new transport with a construction trace.

> L584 | The two responses, extend \(H\) and re-tune, or construct a new transport, are the difference between learning and creating

**Its description of the text.** No sentence of the text is described; it warns against a mapping the text does not make.

**The finding.** Selection is not model-free learning and construction is not model-based learning: planning can use a learned model through a retained procedure with no new binding, and criticism can revise a simple value-based policy. The two distinctions concern different things, and trial-by-trial predictions come from supplied mechanisms, not from Account or provenance.

**Its evidence.** Reinforcement-learning research, named and not cited.

**Its repair, in its own words.**

> A cognitive application must measure both rather than substituting one for the other.

**Its other words.**

> In the present semantics, however, model-based planning need not automatically be construction. A system can use a learned transition model through a retained procedure without newly constructing a binding or criticizing a represented target during the relevant episode.

> Potentially useful descriptive structure, but not yet a psychological process theory.

**Challenges the text.** a finding about scope (section 3): no line challenged.

**S104 on the same place.**

- Formal claims: FC82, FC83 (the two responses; only construction originative): counterexamples resting on I52, I56, I90; FC84: holds.
- Counterexamples (`search results.md`): FC82; FC83.
- Inventions (`inventions register.md`): I52, I53, I56, I90.
- The check of the formalization, and the formal core: H05, H08, R11.

**Reproduced.** none.

### E12 · 3.5 · Finding questions: recording the event is not explaining its occurrence

**In the document.** Lines 330–347 of the saved file.

**The place in the text.**

> L15 | A question, meaning its target, its scope of admitted changes and what it asks, can be found as well as answered, and the semantics represents both (Part III, Argument 5).

> L588 | Hence an episode whose originative contribution is a new contract meets (G) and, where the other conjuncts are met, (EX).

> L592 | Finding a new question, by an owned construction (G), is a creative act, as answering one is.

> L544 | A case of finding a new question that treating a contract as a content, something that can be constructed, be new, and be the originative contribution of an episode, fails to capture

**Its description of the text.** Its 'Treating questions as constructible contents' matches L15 and L588–L592.

**The finding.** The semantics can record that an agent changed a target, its admitted changes or its query, and supplies no mechanism that selects which change occurs; Argument 5 gives an encoding, not a theory of why particular questions are found. That is a problem only where representability is treated as the explanatory achievement itself.

**Its evidence.** Two questions a cognitive account would face.

**Its repair, in its own words.** None offered.

**Its other words.**

> The semantics can record changes in aims, hypotheses, and questions. What it does not yet supply is the mechanism selecting one of those changes.

> Argument 5 establishes an encoding possibility, not a theory of why particular questions are found.

**Challenges the text.** a finding about scope (section 3): no line challenged.

**S104 on the same place.**

- Formal claims: FC97 (Argument 5: a contract can be an organization and a content): holds.
- Counterexamples (`search results.md`): none.
- Inventions (`inventions register.md`): I01, I48, I67.
- Claims of the text not formalized: NF06 (L544).

**Reproduced.** none.

### E13 · 4.1 · Declared indices: objective, or merely conditional

**In the document.** Lines 351–369 of the saved file.

**The place in the text.**

> L31 | Grain, boundary, continuity and the contract of admitted changes are **declared indices**: every claim is relative to them

> L43 | What is independent of the modeller lies in the target and in fidelity; what the modeller chose to leave out lies in the stated scope, and so in the record.

> L159 | the semantics records the restriction and supplies no rule that decides it

> L473 | Both are declared before the attribution, not chosen after it.

> L522 | where the input is missing, the assessment is left open and the semantics says so rather than choosing the input from the assessment wanted.

> L608 | Goalpost-moving is the act of passing off a claim at one index as a claim at another

**Its description of the text.** Its 'The document explicitly leaves the justification of a restricted scope as a substantive, criticizable input' matches L159.

**The finding.** A fact can be objective relative to a contract, but the assessment turns on the target, grain, decomposition, counterparts, admitted changes and scope; recording them makes adjustment after the result visible and does not show that the question is the one a theory needed to answer. Without a procedure the framework risks becoming a precise language for whatever interpretation the investigator already favours.

**Its evidence.** Its argument; no example.

**Its repair, in its own words.**

> For cognitive-science applications, the protection should be procedural: specify the relevant grain, contrasts, component mappings, and admissible revisions before testing the decisive cases.

**Its other words.**

> How much of the desired classification can be obtained by choosing those inputs after seeing the result?

> Recording those choices makes retrospective adjustment visible. It does not establish that the resulting question is the one a scientific theory needed to answer.

**Challenges the text.** in doubt: goes to a checker (reading rule, rule 5). The text asks for declaration before attribution for boundary and continuity (L473) and records scope (L159, L522); whether grain, counterparts and contrasts call for the same is the question. Its decisive question (section 7, E22) is the same point.

**S104 on the same place.**

- Formal claims: FC30, FC99: hold; FC32 (L520 against L526's order): not tested; FC50 (a narrowed contract leaves the problem on p): holds.
- Counterexamples (`search results.md`): none.
- Inventions (`inventions register.md`): I27, I28, I85.

**Reproduced.** none.

### E14 · 4.2 · Selection and construction: separate mechanisms, or separate labels on histories

**In the document.** Lines 371–384 of the saved file.

**The place in the text.**

> L201 | Neither provenance is reducible to the other: a selected transport has no represented target and no criticism in its history; a constructed one has both.

> L47 | Nothing about construction is reduced to selection; Part IV keeps the two apart by what their histories contain

> L77 | Neither is reduced to the other.

> L411 | Construction is not selection. A selected transport has no represented target in its history; a constructed one does.

> L542 | a method that rewrites every construction trace as a selection history without loss (against Part IV, collapsing the two provenances and removing creativity from the semantics)

**Its description of the text.** Its 'The prohibition on represented targets in selected histories' matches L195, L201 and L411; 'The qualified underdetermination result in Argument 3' is L572–L576.

**The finding.** Argument 3's qualified underdetermination stands, with the population restriction doing the work, but it gives no general discontinuity between selection and construction: an evolutionary search with represented candidates, counterexamples and content-sensitive revision would count as construction, so “selection” here is narrower than variation and selection in general, and the ban on represented targets in selected histories gives a difference of classification, not of mechanism.

**Its evidence.** An evolutionary search procedure with represented candidates and revision.

**Its repair, in its own words.**

> Identify what a construction mechanism does that is not already captured by the independently specified physical processes, representations, memory, and feedback in its history.

**Its other words.**

> The qualified underdetermination result in Argument 3 is sound: if two transports survive the same history and differ elsewhere, survival on that history does not distinguish them there. The population restriction is doing important work.

> The prohibition on represented targets in selected histories guarantees a classificatory difference. It does not, by itself, establish a mechanistic irreducibility result.

**Challenges the text.** in doubt: goes to a checker (reading rule, rule 5). Whether L47, L77, L201 and L542 claim more than a difference of classification.

**S104 on the same place.**

- Formal claims: FC78 (exactly one of three provenances): counterexample under D12.1, resting on H05 (L201 and L411 left out of Sel); FC80 (Argument 3): holds; FC84: holds.
- Counterexamples (`search results.md`): FC78.
- Inventions (`inventions register.md`): I52, I53, I54, I90.
- The check of the formalization, and the formal core: H05, T15, R11.
- Claims of the text not formalized: NF05 (L542), NF07 (L201).

**Reproduced.** none.

### E15 · 4.3 · Exact fidelity and explanatory idealization

**In the document.** Lines 386–399 of the saved file.

**The place in the text.**

> L250 | \operatorname{Ans}_E(\tau(a),\sigma(b))=\operatorname{Ans}_p(a,b). \tag{A}

> L242 | \pi[\operatorname{Sol}_D(a,b)]=\operatorname{Sol}_E(\tau(a),\sigma(b))

> L277 | It does not exclude a coarse dependence for omitting finer workings or an instrument: an account at a coarse grain is an account of the coarse question

> L363 | An exact question is not silently replaced by an approximate one.

> L538 | whose organization no transport can preserve under any contract on its target

**Its description of the text.** Its 'F1, F2, and answer fidelity are exact equalities' and 'an approximate transport bound' match L236–L250 and L363.

**The finding.** (F1), (F2) and (A) are exact equalities, and the approximate transport bound does not replace Account with an approximate account; a working model may capture a dependence while simplifying its realization, and the two answers the text has (an exact coarse-grained dependence, or a question about the approximation) do not show that every useful idealization is handled without changing what it was offered to explain.

**Its evidence.** Its argument; no worked idealization.

**Its repair, in its own words.**

> A substantive necessity question, not an immediate contradiction. A worked cognitive idealization is needed, with the coarse-graining and preserved dependence written out.

**Its other words.**

> The burden is to show that its exactness requirement tracks the intended scientific distinction rather than classifying most working explanations as merely candidates.

**Challenges the text.** in doubt: goes to a checker (reading rule, rule 5). It bears on (Nec) at L538 and on L277 and L363.

**S104 on the same place.**

- Formal claims: FC66 ((T2)): holds; FC104 (the two extents of 'fidelity'; round-1 matter 12): not tested; FC19: holds.
- Counterexamples (`search results.md`): none.
- Inventions (`inventions register.md`): I28, I49.
- Claims of the text not formalized: NF03 (L538).

**Reproduced.** none.

### E16 · 4.4 · Does the argument machinery explain reasoning?

**In the document.** Lines 401–412 of the saved file.

**The place in the text.**

> L393 | or a premise \(j\) tentatively accepts, having taken it up, for whatever reason, and not withdrawn it, whether or not \(j\) holds an explanation of \(d\)

> L397 | A premise may be a claim taken as given: tentatively accepted, for whatever reason, even with no thought given to it, by someone who holds no explanation of it.

> L429 | Closing an episode is a choice

> L8 | An argument is never a reason *for* a claim: what it does is rule out a claim's denial, or a rival, for someone who can use it, and only while it stays usable (K2).

**Its description of the text.** Its 'Usable records whether an agent admits the inference form, respects its scope, and retains its premises. It explicitly permits premises accepted without their explanations' matches L393 and L397.

**The finding.** Usability records what an agent admits and retains and can model the consequences of its commitments, but does not explain why the agent adopts a premise, notices a conflict, drops an assumption or stops; the text calls these choices, which it says is no logical error, but in cognitive science they are among the phenomena to explain. Redescribing an argument for a conclusion as one against its denial does not by itself explain the operation or settle its status.

**Its evidence.** Its argument.

**Its repair, in its own words.** None offered.

**Its other words.**

> The document calls these choices. That is not a logical error. But in cognitive science, those choices are among the principal phenomena requiring explanation.

> Similarly, redescribing an argument for a conclusion as an argument against its denial does not by itself explain the psychological operation or settle its epistemic status.

> Useful bookkeeping for reasoning episodes; incomplete as a theory of reasoning dynamics.

**Challenges the text.** no: no line challenged. Its remark on L8 bears on the owner's decision S23 (argument as reasons why this and not that); a point against that reading is a question for the owner, and no ruling may change it (addendum, point 8).

**S104 on the same place.**

- Formal claims: FC56, FC69, FC70, FC72, FC73 (ruling out, (K2), premises taken as given): hold.
- Counterexamples (`search results.md`): none.
- Inventions (`inventions register.md`): I38, I40, I41.
- The check of the formalization, and the formal core: R15.
- Claims of the text not formalized: NF13 (L8), NF14 (L397).

**Reproduced.** none.

### E17 · 4.5 · The capability conditions and ordinary fallible performance

**In the document.** Lines 414–424 of the saved file.

**The place in the text.**

> L466 | \operatorname{RetReal}(\pi,T,C;\chi)\iff\forall z\in C\ \forall i\in\operatorname{dom}T\ \forall\eta\in\operatorname{Exec}(\pi,z,i;\chi),\ \eta\text{ completes with }o\in T[i]\text{ and }z'\in C. \tag{CT1}

> L479 | \(q\in Q_\Theta\) is a tolerance of performance and \(r\in Q_\Theta\) a tolerance of retention

> L495 | An explanatory barrier is an independently characterized domain for which every admitted, non-question-begging enabling condition leaves the relevant capability unavailable.

> L509 | a finite performance record does not suffice for it.

**Its description of the text.** Its 'RetReal quantifies over every admitted execution: all must complete successfully and return to the retained constructor attribute' matches L466.

**The finding.** (CT1) asks every admitted execution to complete and return, so a task with a small nonzero chance of failure, the failures in the execution family, fails it where ordinary usage would call the ability retained; the text has tolerances, but has to show whether a tolerance ranges over a distribution of executions or only over each output. “Non-question-begging” enabling conditions must exclude supplying the explanation being attributed while allowing teaching and scaffolding.

**Its evidence.** Its argument; no model.

**Its repair, in its own words.**

> But it needs to show explicitly how reliability is represented—particularly whether tolerance applies to a distribution of executions rather than only to the quality of each output.

**Its other words.**

> Suppose a modeled cognitive task has a small but nonzero probability of failure, and those failures belong to the execution family. Then this condition fails, even when performance would ordinarily count as a retained ability.

> At the universal level, the existential enabling conditions need equally careful treatment. “Non-question-begging” must exclude supplying the very explanation or discovery being attributed, while still permitting genuine teaching and scaffolding.

**Challenges the text.** yes. It bears on L466 and L479 (how reliability is represented) and on 'non-question-begging' at L495.

**S104 on the same place.**

- Formal claims: FC91 ((CT1) as C ⊆ F(C); round-1 matter 10), FC92 ((CT2); round-1 change L471), FC93 ((CT3), (CT4)): hold; FC94 (recursion does not entail universality), FC110: not tested.
- Counterexamples (`search results.md`): none.
- Inventions (`inventions register.md`): I61, I62, I74, I97, I98.
- The check of the formalization, and the formal core: T14.
- Claims of the text not formalized: NF11 (L495), NF12 (L497).

**Reproduced.** none.

### E18 · 5 · Tables (set aside by the external reader)

**In the document.** Lines 430–431 of the saved file.

**The place in the text.**

> L269 | A table that encodes an organization's response to every admitted change is not a table in that sense: it meets (F1) as a decomposition does, and it is an account when it meets the other conjuncts of (E).

> L536 | A table that encodes the response to every admitted change does not fail (F1)

**Its description of the text.** Its 'The document explicitly allows such a table when it preserves the required component structure' matches L269 and L536.

**The finding.** “A complete counterfactual lookup table cannot explain” is no argument by itself: the text allows such a table when it keeps the required component structure and meets the other conditions, and repackaging a mechanism as a table gave no sufficiency counterexample.

**Its evidence.** None given.

**Its repair, in its own words.** None offered.

**Its other words.**

> The document explicitly allows such a table when it preserves the required component structure and meets the other conditions. Calling it a table is not an independent argument against explanation. I did not find a decisive sufficiency counterexample merely by repackaging a mechanism this way.

**Challenges the text.** no: no line challenged. The S104 search found what the external reader did not: FC25 (b), below, a case against L269's 'it meets (F1)'.

**S104 on the same place.**

- Formal claims: FC25 (tables): counterexample in part (b): an encoding table fails (F1) when a port of the target lies in no footprint, under I14 and I32; with λ(k) read in the context of the whole target it meets (F1) (the check's R19).
- Counterexamples (`search results.md`): FC25 (b).
- Inventions (`inventions register.md`): I14, I32.
- The check of the formalization, and the formal core: R19.

**Reproduced.** none.

### E19 · 5 · The transport could hide the answer (set aside as open)

**In the document.** Lines 433–434 of the saved file.

**The place in the text.**

> L255 | The target's answer does not appear, at the declared grain, as an unanalysed boundary input or as a component; moving an assertion from an input slot into a component named "law" does not discharge this. Identity of that assertion with the target's answer is structural at the declared grain, not the indiscriminate identification of all logically equivalent mathematical statements.

> L273 | "\(p\) because \(p\)" fails non-circular dependence.

**Its description of the text.** Its 'the non-circularity clause' and 'structural answer-identity at the declared grain' match L255.

**The finding.** The flexible translations make hiding the answer in the transport a serious line of attack; the non-circularity clause may exclude plain versions, but encoded variants need an exact account of structural answer-identity at the declared grain before they can be decided. An open obligation of formalization, not an exhibited counterexample.

**Its evidence.** None worked.

**Its repair, in its own words.**

> Encoded variants require a more exact account of structural answer-identity at the declared grain before they can be adjudicated.

**Its other words.**

> This is a serious attack surface because the translations are flexible. But the non-circularity clause may exclude straightforward versions.

**Challenges the text.** yes. It names an obligation L255 leaves open (addendum, point 5).

**S104 on the same place.**

- Formal claims: FC23 ('p because p'): counterexample: it meets NC2 and fails non-circular dependence only through NC1, whose 'unanalysed', 'at the declared grain' and 'structural' are defined nowhere; FC24, FC108: hold; FC20: counterexample with non-injective value maps (I14, I81).
- Counterexamples (`search results.md`): FC23; FC20.
- Inventions (`inventions register.md`): I23, I24, I25, I79, I81, I82, I83.
- The check of the formalization, and the formal core: R07, R08, R24; formal core §18, 'Where the text was vaguest', 2.

**Reproduced.** none.

### E20 · 5 · Fixed port sets (set aside as repairable)

**In the document.** Lines 436–437 of the saved file.

**The place in the text.**

> L425 | A dimension of variation mentioned in passing is not thereby a port of the account; it becomes one when the account admits changes to it, and adding it is construction.

> L590 | and admitted edits (add or remove a change; alter \(\mathcal Q\)).

> L105 | Values of ports may be paths, functions, fields, mathematical structures or histories.

**Its description of the text.** No sentence is quoted; its 'the organizations have fixed port sets' is (O) at L87–L100.

**The finding.** Organizations have fixed port sets, so adding structure (a new question, a new component) needs dormant slots, structure-valued ports or a meta-organization; the value domains look broad enough that this is an encoding to make clear, not an impossibility.

**Its evidence.** None worked.

**Its repair, in its own words.**

> Some of the exact constructions need clearer encoding: adding structure requires dormant slots, structure-valued ports, or a meta-organization.

**Its other words.**

> But the allowed value domains are broad enough that this looks repairable. It is not a demonstrated expressive impossibility.

**Challenges the text.** in doubt: goes to a checker (reading rule, rule 5). L425 and L590 speak of adding a port and adding a change; (O) fixes the port set and does not say how either is added.

**S104 on the same place.**

- Formal claims: FC97 (Argument 5): holds; FC62 (the absent structure as a deleted counterpart): holds.
- Counterexamples (`search results.md`): none.
- Inventions (`inventions register.md`): I01, I03 (ports and components the same under every edit; absence as the full relation), I67.

**Reproduced.** none.

### E21 · 5 · The finite monotone claim (set aside: no counterexample)

**In the document.** Lines 439–440 of the saved file.

**The place in the text.**

> L305 | **Finite monotone claim.** If \(\Gamma\) is finite, \(\mathsf S\) is upward closed, and \(\Gamma\in\mathsf S\), then \(d\in\Gamma\) is critical for some route (**contributory**) exactly when \(d\in\bigcup\min\mathsf S\)

**Its description of the text.** Matches L305.

**The finding.** Every upward-closed route family containing the whole commitment set, for one to four commitments (193 families), gives no counterexample; the problem of 2.1 survives because the theorem can hold while its criticality predicate is read too strongly.

**Its evidence.** Its exhaustive check of 193 families.

**Its repair, in its own words.** None offered.

**Its other words.**

> I checked every upward-closed route family containing the full commitment set for one through four commitments: 193 families, with no counterexample.

**Challenges the text.** no: no line challenged.

**S104 on the same place.**

- Formal claims: FC37: holds on every family on |Γ| ≤ 4 and on the 7,581 up-closures of antichains on five commitments.
- Counterexamples (`search results.md`): none.
- Inventions (`inventions register.md`): I30, I77.

**Reproduced.** FC-E5: CONFIRMED on the text under review (2, 5, 19 and 167 families for one to four commitments).

### E22 · opening, 5 (last paragraph), 6 and 7 · The overall verdict, the revision priorities and the proposed benchmark

**In the document.** Lines 5–494 of the saved file.

**The place in the text.**

> L3 | ## A structural class of explanatory creativity, with selected and constructed correspondence

> L17 | The **constitutive conjecture** is this: explanatory creativity is fully characterized by

> L27 | It does not decide whether any human, machine, institution or lineage belongs to the classes defined. It defines the classes.

> L546 | **A mathematical error.** A counterexample to the finite monotone claim, (I2), (O1), (T2), (CT2), or Arguments 1–3 under their stated assumptions.

**Its description of the text.** Its 'its strongest advertised achievement is a full characterization of explanatory creativity' points to L3 and L17; the text states the characterization as a conjecture (L17) and names what would rule it out (Part XV).

**The finding.** The text's strongest shown achievement is an audit language for scoped explanatory structure, and its strongest advertised one a full characterization of explanatory creativity; the small mathematical results do much less than the conjecture, and their holding is no argument for it. Its priorities: explanatory relevance apart from whole-model fidelity (E02), construction grounded without its resulting representation (E03), surprise apart from fidelity failure (E08); then an operational account of component mappings, construction traces and scope choices (E13). Its benchmark: a known mechanism with hidden state, an editable measurement channel, an unrelated subsystem, and classifications fixed before the critical interventions are revealed.

**Its evidence.** Sections 1 to 5.

**Its repair, in its own words.**

> The highest-priority revisions are to separate explanatory relevance from whole-model fidelity, ground construction without presupposing its resulting representation, and separate surprise from objective fidelity failure.

**Its other words.**

> It is promising as a framework for auditing explanatory claims, but it has not established its stronger claim to fully characterize explanatory creativity.

> However, I did not find a decisive counterexample satisfying the document’s full requirements for refuting the sufficiency of Account.

> The small mathematical results generally do much less than the central philosophical claim. Their correctness should not be mistaken for proof of the constitutive conjecture.

> Then fix the candidate classifications before revealing the critical interventions.

> What does the framework force us to conclude about a difficult case before we adjust its grain, contract, counterparts, and provenance description to fit the outcome?

**Challenges the text.** in doubt: goes to a checker (reading rule, rule 5). Whether L3 and L17 say more than the text's results; the text calls the characterization a conjecture. Its benchmark is a proposal for a test outside the text, and its priorities are proposals (addendum, point 6). The findings about scope (E07, E08, E09, E11, E12) and E16 bear on L17 through this item.

**S104 on the same place.**

- Formal claims: FC110 (the classes are defined; no membership is asserted): not tested; FC109 ('A mathematical error': the named claims): holds.
- Counterexamples (`search results.md`): none.
- Inventions (`inventions register.md`): I74, I75.
- Claims of the text not formalized: NF01 (L17).

**Reproduced.** none.
