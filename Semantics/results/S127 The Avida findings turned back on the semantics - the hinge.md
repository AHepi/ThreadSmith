# S127 The Avida findings turned back on the semantics: the hinge

*Log S127, 2 October 2026 (decisions S80, S81). One Opus 5.5 agent doing the whole job (S56, S68; no subagent or workflow), beside the S126 agent (the closing knock-out run), none of whose files was touched. Writing only: no Avida run, no outside model, no GLM check (S70's latest word). Avida is described in the owner's terms (S61). The semantics is cited from `tests/107 The semantics, standing alone, after round 4.md` by line ("L195"), and from `results/S107 Round 4 - maths after the reading/formal core, after round 4.md` by definition id with its line in that file ("D12.1, core line 454"); inventions by their register number (I52 in `results/S104 Round 2 - maths/inventions register.md`; I167 to I177 in `results/S105 Round 3 - maths after the reading/inventions register - addendum after round 3.md`). **Nothing in the theory's text, formal core, claims or program is changed**: every wording below is a proposal for the owner. Part B (S109) stays held (S57); the review rounds stay on hold (S52); this is not a round.*

**The owner's words.** S80: "This is the think outside the box part. Is it actually worth persuing this line? What can we really tell right now?" S81, after Claude's answer: "Agree. Let's do that". Claude's answer, as recorded with S80: Avida has shown the adaptive kind of knowledge and nothing of the explanatory kind; every execution environment tried names its target at least one level up; the one result of lasting value is about the semantics, not Avida: the hinge of S117. S81's reading: turn what Avida found back on the semantics; set out the hinge for the owner to decide.

## 0. In short

- **The hinge.** Whether an evolved Avida program's match with its task is *selected* (and so, by the semantics' own rules, a representation of the task and, taken as one block, an explanation of it in the semantics' narrow sense) or *declared* (it represents nothing and explains nothing). The text leaves this open at one place: the clause of D12.1 that no earlier occurrence in the history may represent the transport, the history, the survival condition or the codomain (L195; core line 454), read through two inventions, I52 ("member of the history" read as an occurrence of the selection history) and I167 (the history is that of one holding, "its preparing episode included"). Whether Avida's task-checking code, written by people, is such an occurrence is what the text does not say.
- **Three readings.** **A**: the checking code is part of the simulated world's rules (its physics), not an occurrence; the programs' matches can be selected. **B**: the checking code is an earlier occurrence that represents the task (it carries the provenance of the people who wrote it, by the text's own rule for records); the programs' matches are declared. **C** (new here): the history is read inside a declared boundary; inside the boundary the owner drew in S72 (the whole execution environment, from the start of a run), the checking code's match with the task arrived whole from outside, has no selected or constructed history there, and so, by L211, represents nothing; the programs' matches can be selected. With a wider boundary that takes in the people who wrote Avida, C gives B's verdict.
- **A second open point moves the same verdicts, and no reading of the hinge settles it.** D12.1 asks for "a survival condition requiring fidelity on H"; in Avida, programs last without doing any task (S117 B4; S125 correction 15). If "requiring" means a strict requirement, the programs of almost every run in the record are declared under *every* reading of the hinge, and so is every adaptation of a living species, whose advantage is graded too. If a graded advantage counts, A and C make Avida's programs selected. The semantics has no word for a graded advantage (the companion file, item 4, where it is judged NEEDED).
- **What no reading of the hinge decides.** The text already says that a selected correspondence that meets (E) is an explanation (L17, L49, D16.XV), and that only construction creates one (L13, L411, (EX)). So adaptations in nature, where nobody wrote a checker, are explanations in the narrow sense under all three readings (given the graded reading of survival). The hinge decides only whether Avida is a fair model of that case.
- **Recommendation, for the owner to decide:** Reading C with the S72 boundary (it gives A's verdicts for the programs), read together with "the explanation kind" (S59) as the semantics' *created* explanation. Reasons in section 6. If the owner means by "the explanation kind" anything the semantics calls an explanation, no reading of the hinge gives "knowledge without the explanation kind" for living species; that would need a change to (Suff) itself, set out in section 7 as a further proposal, against the owner's answer S41 Q2 as S108 read it.

## 1. Where exactly the text leaves it open

**The definition.** Selected (L195): a population 𝒯 of candidate transports, a variation operator μ, a finite history H ⊆ C of edit-boundary pairs actually met, a survival condition requiring fidelity on H; t is a member that survived; and

> ¬[∃o ≺_{h(t)} o_t, x ∈ {t, H, survival condition, cod t}: Rep(o, x)] ∧ ¬[∃h' ⊆ h(t): CT(h', t)] (D12.1)

In the round-2 text the first clause was the sentence "No member of the history represents t, H, or the survival condition", which the inventions register quotes (I52). The formal core (D12.1, core line 454) writes it as: no occurrence o earlier than o_t in h(t) represents any of t, H, surv or cod t, "where Sel, Con and Dec are of a holding (t, o_t), o_t an occurrence at which t is held, and h(t) := h(t, o_t) is the history that produced that holding, its preparing episode included".

**What is invented, and so open.**

1. **I52.** The text's "member of the history" is said of H, a set of pairs, which cannot represent; the formal core reads it as an occurrence of the physical selection history. Without that reading, Sel is met by every transport (FC77). The invention fixes that *occurrences* are what must not represent; it does not say which things in a simulated world are occurrences and which are the world's rules.
2. **I167.** h(t) is the history that produced the holding, "its preparing episode included". It does not say where that history starts. Avida's checking code was written years before any run and is executed at every task check during the run; both its writing and its running are causally upstream of every program's holding.
3. **D0.1 and Part XII.** For Avida the physical module Θ is itself a program written by people (S117 B8; D0.1): the semantics' physics is a fallible theory of matter, Avida's is exact and written. Whether a rule of Avida's program counts as physics or as an occurrence is not a question the text was written to answer.
4. **The rule for records (L211; D12.3, core line 462; FC12.new2 (a)).** "A later record made from the carrier carries that provenance": a record made from a represented content represents what its source represented. Code written by people who understood the task is, on one reading, such a record. On another, it is a rule put into a world, which L211's other sentence covers: "A declared transport does not make an occurrence represent anything".
5. **The survival condition (L195, L481; D12.1's surv with Env, I177; D15.8, core line 610).** The text says the condition requires fidelity on H and is "enacted by the environment" (L481); the formal core reads surv as fidelity on H and an environmental condition Env that is given as "⊤" (none). S117 left open whether "requiring" is a fact about the environment or the semantics' stipulation (S117 results, section 11). This is the second open point (section 5).

**The computed case** (S117, MC1, a copy of the model, one bit, exact for bitwise NOT): the most common NOT program of run low seed 2 (S112; 110 instructions; 44 copies), which hands back nand(x, x). Taken as one block on the numbers the world hands in, it meets every conjunct of (E): (F1), (F2), (A), Dependence, NonVacuous. Under Reading A the model's `sel` holds, `con` fails, Dec is false; under Reading B `sel` fails, because the history holds an occurrence representing `surv` and `cod`, and Dec is true. Cut into its instructions, it fails (F1), because the task has no parts for them to match (S117 B3; MC1); S112's circuit, offered as the program's account of itself, gets every single-ablation answer right in only 8.8 in 100 program-task pairs (C1).

## 2. The three readings, each with what changes

### Reading A: the checking code belongs to the world's rules

**Statement.** Avida's task list and checking code, fixed before a run, are part of the physical module for Avida (its laws), not occurrences of any history. Nothing in h(t) then represents surv or the task, and an evolved program's correspondence with its task is selected wherever the other conditions of D12.1 hold.

**In the semantics' own worked cases.** Part VII's exact constructions (pole and shadow, the two balances, the 23 tokens, explanations that remove structure, odd skew-symmetric matrices, constitutive rules) state no provenance and are claims about Account, which takes none (FC30): nothing changes. Argument 10's two-layer episode stipulates t₀ selected: nothing changes, and the episode could be built in a simulated world with a scorer people wrote and still be selection, so its surprise could be exhibited there. The owner's cases in the formal claims: the student's copied pendulum formula stays declared, not an explanation (FC30.new1 (a); S41 Q2); the shop sign and the weathervane, which S108 computed on a selection history, stay explanations on such a history whoever wrote its scorer; the bridge built to a fixed brief stays constructed (FC84.new1; the brief is the represented target D12.2 asks for).

**In S117's map** (the eight units S117 marked as turning on the reading: D11.4, D12.1, D12.3, D12.5, D16.XV, FC30.new1, FC75, T10; counts recomputed in section 4): D12.3, D12.5, D16.XV, FC30.new1, T10, D11.4 and FC75 go from LINES UP IN PART to LINES UP EXACTLY: the programs represent their tasks on the world's order of inputs; an evolved circuit is the inexplicit representation T10 speaks of; the routes in Avida's traces are active routes from a represented input. D12.1 stays IN PART for the second open point (section 5), unless the run requires solving (S118's "copy only after solving something", Avida's required tasks) or the graded wording of item 4 of the companion file is adopted. D16.XV and FC30.new1 line up in a way that bites: the NOT program, taken whole, is then an explanation of NOT in the semantics' sense, so an assessor who takes as given that it is not one holds an argument, not using (E), that rules out (Suff) (MC1). The owner, if the owner holds that premise in the narrow sense, is that assessor.

**In what the theory says about evolved adaptations in nature.** No change: nobody wrote a checker, so A and B do not differ there. A makes Avida a fair model of that case.

**What A commits the theory to.**
- Every evolved program, and every adapted trait of a living species, whose selected correspondence meets (E) on some question is an explanation of that question in the narrow sense, never a created one. The text already commits to this for nature (L13, L17, L49, L69, D16.XV); A extends it to selection by rules that people wrote. Since one block meets (E) easily (MC1) while the same program cut into its parts fails (B3, C1), in practice most adapted traits, taken whole, would be explanations, and bad ones by the owner's own standard (S44, S45: a written-in answer makes a bad explanation, not none).
- A line between "a rule of the world" and "an occurrence". A fixed checker is a rule; a breeder choosing each generation, a person scoring by hand, Claude's growing-list runner (S113, adding tasks between pieces on counts it reads) and the temporal driver of S122 are occurrences that act during the history. A must say which side each is on; the text gives no criterion, and S125 already lists "the driver's boundary" among the owner's open points. A people-written rule fixed before the run is on one side; a person choosing live, by the very same criterion, is on the other: the same selected trait would be selected under the first and declared under the second.
- Treating a written program as physics, although the semantics' physics is a fallible theory with no exact tolerance (D15.7; S117 B8).

### Reading B: the people-written checker is an earlier occurrence representing the task

**Statement.** The checking code is an occurrence of h(t), earlier than every holding it shaped. It computes the task, and it was written by people who represented the task; by the rule for records (L211; D12.3; FC12.new2 (a)) it carries their provenance, so it represents the task (cod t) and the survival condition. D12.1's first clause then fails. No construction trace prepares the program's correspondence (I168: a transport assembled later from a trace's outputs is not prepared by it). So the correspondence is declared: it holds faithfully and represents nothing (L211).

**In the semantics' own worked cases.** Part VII: nothing changes (no provenance). Argument 10: unchanged as stipulated; but built in any simulation with a scorer people wrote, t₀ would be declared, so its failure under occlusion would be a violation and not surprise (surprise needs a selected transport, D12.7, Argument 4). The owner's cases: the pendulum copy unchanged; the shop sign and the weathervane, reached by a selection history whose scorer someone wrote, become declared and so not explanations (S41 Q2); the bridge stays constructed; and a design for the same brief found by a computer search scored against the brief would be declared, while the engineer's own design is constructed.

**In S117's map.** D12.3, D16.XV and FC30.new1 go to LINES UP EXACTLY: the programs are declared accounts and, by S41's rule, not explanations, which agrees with the owner's reading of Avida (S59, S60) and with S111's observation that nothing in the programs refers to where the numbers come from. D12.1, D12.5, D11.4 and FC75 go to DOES NOT LINE UP (selection's clause fails; nothing is represented; no input is represented, so no active route); T10 goes to DOES NOT LINE UP (nothing is represented, explicitly or not). Units S117 did not mark also move: FC80 (Argument 3, whose premise is a selected t) goes from EXACT to IN PART, since the computed underdetermination stands (C3: 16 of 18 populations) but the argument no longer speaks of these programs; T07 and T08 ("selection produces the raw material") lose their Avida counterpart for task capabilities; D12.7 and D12.8 fail for one more reason (no selected transport).

**In what the theory says about evolved adaptations in nature.** No change where nothing in the history represents the survival condition. But B, applied by the clause's own words with no restriction to people (the semantics never names people; Part I, substrate independence), also reaches any selection carried out by a chooser that itself represents the criterion: a female choosing mates by a display she perceives, a predator whose eye represents the prey's look, the child of S124's Reading 1 who represents the meaning side of a grammar. Read so, a trait shaped by mate choice would be declared (Claude's argument; not computed).

**What B commits the theory to.**
- Anything bred or found by search against a criterion that people represent is declared: dog breeds and crop varieties chosen by breeders, enzymes from directed evolution, a program or antenna found by a genetic algorithm against a scoring function people wrote, and every Avida run in the record (all name their target at least one level up: S80's answer; S118 grade 2). None represents what it was selected for; none is an explanation.
- The semantics' selection-side claims (representation by selection, surprise, the selection response, Argument 3 about a selected transport) can then never be exhibited in a simulation people build with a scorer, only in nature. Avida, chosen in S59 as a working case to build from, would be a case of constructor theory's knowledge (the three properties, S111) but not of the semantics' selected representation at all.
- A verdict that turns on who wrote the selector, which S60 asked to set aside ("Ignore the fact that they were evolved to solve a problem"), and which, for the case the owner's distinction is about (inherited traits of living species, Deutsch's non-explanatory knowledge), gives no help: they stay explanations in the narrow sense under B.

### Reading C: the code apart from its writers, tied to the declared boundary

**Statement.** The history h(t) of a holding is read inside the system boundary declared for the claim, as the semantics already does for ownership and capability (Part XII, L473; D13.7; D15.4). The text separates the two attributions this needs: "a process that runs inside the boundary is the system's own whoever wrote it", and "a routine written outside the boundary and run inside it is the system's own process, and its content remains its writer's contribution" (L427). Inside the boundary of S72 (the whole Avida execution environment, which "does selecting ... Just as an autonomous agent does selection", from the start of a run), the checking code is a process whose match with the task arrived whole from outside; inside the boundary it has neither a selected nor a constructed history; so, by L211's sentence on declared transports, it represents nothing there, and what it carries is its writers' contribution, recorded as such. Nothing in h(t) inside the boundary then represents surv or the task, and the program's correspondence can be selected. With a boundary drawn wider, taking in the people who wrote Avida, the code is a record of their representation (L211's other sentence), represents the task, and C gives B's verdict.

This is a third reading and not A under another name: A says the code is not an occurrence at all; C says it is an occurrence, inside the boundary, whose correspondence is declared there. It is not B either: B counts the writers' provenance in whatever boundary is drawn.

**In the semantics' own worked cases.** As A with the S72 boundary, as B with the wide one. Argument 10, the bridge and the pendulum copy are unchanged under both. The shop sign and the weathervane on a selection history depend on the boundary declared for the claim.

**In S117's map.** With the S72 boundary, as A (section 4). With the wide boundary, as B. S117's D13.7 (ownership; EXACT) is the place the reading leans on, and is unchanged.

**In what the theory says about evolved adaptations in nature.** No change; the boundary of a lineage's claim ordinarily contains no one who wrote its selector. For a bred animal, the verdict follows the boundary: around the farm with its breeder, declared; around the lineage, with the breeder's choices recorded as a contribution from outside, selected.

**What C commits the theory to.**
- **Provenance becomes relative to a declared boundary**, as capability already is (Part XII). L193's "exactly one of three provenances, determined by its history in the physical module" would hold per boundary; one transport can be selected relative to one boundary and declared relative to another, and both claims are true at their indices (Historical index, Part VIII; Argument 7 keeps claims at different indices apart).
- Every provenance claim, and so every claim of representation and of explanation, must state its boundary; Part XIV's list of declared inputs gains "the boundary of a provenance claim". Where it is missing, the assessment is left open (Part XIV), as now.
- A gamble the text already names elsewhere: a boundary can be drawn to get the verdict wanted. Part XII forbids it for capability ("Both are declared before the attribution, not chosen after it"); the same rule would have to bind provenance.

## 3. A table of the three

| | A: world's rules | B: earlier representing occurrence | C: boundary-relative (S72 boundary) | C (wide boundary) |
|---|---|---|---|---|
| Is Avida's checking code an occurrence of h(t)? | no | yes | yes | yes |
| Does it represent the task? | – | yes (its writers' provenance, L211) | no: declared inside the boundary (L211) | yes |
| The NOT program of low seed 2 | selected *if* survival condition met (section 5); represents NOT; taken whole, an explanation of NOT, never created | declared; represents nothing; not an explanation (S41) | as A | as B |
| Adaptations of living species | selected (graded reading); narrow explanations where (E) holds | the same, except where a chooser represents the criterion (mate choice), then declared | the same as A | the same as B |
| Bred or search-found things | selected if the scorer is a fixed rule; declared if a person chooses live | declared | follows the boundary | declared |
| Selection-side claims shown in a people-built simulation | yes | never | yes | never |
| Owner's "Avida programs are not explanations", held in the narrow sense | rules out (Suff) for the owner | agrees | rules out (Suff) for the owner | agrees |
| What it asks of the text | a line between rule and occurrence | nothing new; the clause read at full width | provenance indexed to a declared boundary | as C |

## 4. S117's counts under each reading

Recomputed by hand from `results/S117 The Avida work against the semantics - results.json` (284 units), moving only the units named in section 2; the S117 scripts were not rerun. S117 as published: 114 LINES UP EXACTLY, 36 IN PART, 18 DOES NOT LINE UP, 116 NOTHING IN AVIDA.

| | exact | in part | does not | nothing | units moved |
|---|---|---|---|---|---|
| S117 as published (the eight units counted IN PART) | 114 | 36 | 18 | 116 | – |
| A, or C with the S72 boundary, survival as the text stands | 121 | 29 | 18 | 116 | D11.4, D12.3, D12.5, D16.XV, FC30.new1, FC75, T10 to exact; D12.1 stays in part |
| the same, with a graded advantage counted (companion file, item 4) | 122 | 28 | 18 | 116 | and D12.1 to exact |
| B, or C with the wide boundary | 116 | 29 | 23 | 116 | D12.3, D16.XV, FC30.new1 to exact; D12.1, D12.5, D11.4, FC75, T10 to does not; FC80 from exact to in part |

Under A the strict reading of survival would itself undo most of A's gains for the graded-pay runs (section 5); the second row counts the units as S117 computed them, with the formal core's survival condition. Under B, T07 and T08 (already IN PART) would lose their Avida counterpart for task capabilities and might move further; they are not moved in the count.

## 5. The second open point: does a graded advantage count as surviving?

**What the text says.** "A survival condition requiring fidelity on H" (L195); "a survival condition enacted by the environment" (L481); the formal core: surv(t, H) :⟺ Faithful_H(t) ∧ Env, Env read through Θ, "none given: Env ≡ ⊤" (I177).

**What Avida shows.** In Avida a program lasts by being copied faster than the world removes programs (S111, section 4: with death by age switched off, K3, a program that cannot copy remains; beside an intact one, K4, a knocked-out one is gone by update 500). Doing a task pays (more running time); it is not required. In the environment that pays for nothing, run 1: 3,600 programs at update 50,000, 11 doing NOT; in the fixed list run 1: 3,595 programs, 2,290 doing NOT (S117 B4, C3). Only S118's "copy only after solving something" and Avida's required tasks make doing a task a condition of copying.

**What follows, by Claude's argument.**
- On the formal core's reading (Env ≡ ⊤), every member of the population that is faithful on H counts as surviving on H. Then the 11 programs doing NOT in the run that paid for nothing would be selected for NOT under Reading A, though nothing in their history made NOT matter. That cannot be what "selected" means.
- On the strict reading ("requiring" as a fact the environment enacts), the programs of every graded-pay run in the record (S111, S112, S113's paying environments, S116) are not selected under any reading of the hinge; with Con failing too, they are declared by default (D12.3: "neither of the above"). The hinge would then matter only for required-task runs. And every adaptation of a living species, whose advantage is graded, would be declared as well, which contradicts the text's own picture of selection producing the object layer (Part IV; grievance 6).
- So the survival condition has to count a graded advantage (fidelity on H changes which members are copied or persist), and must not count mere fidelity among survivors. The semantics has no word for this; the companion file (item 4) judges it NEEDED and proposes a wording. The change keeps L25's refusal to order explanations or thinkers: the ordering is a physical fact about copying, in the physical module, not an appraisal the semantics makes. Argument 3's step still holds, since it holds for any condition on values at H (FC80.new1 (b)).

S125's correction 15 says the same from the other side: "Reading A does not make an evolved program's correspondence 'selected' on its own."

## 6. Which reading best fits the owner's stated views (a recommendation only)

**The owner's words that bear on it.**
- S57: "defining explanation is not the point either. We have a definition of information and knowledge, and they are in constructor theory. I suspect the next move is how do we know when this indefinite amorphous thing in a creative agent constitutes knowledge."
- S59: "What kind of information has the following properties: - Can cause itself to be copied. - Can cause itself to resist change. - Can cause itself to remain." and "The explanation kind comes next. I know I defined knowledge."
- S60: "Ok. So we have a machine that can evolve to instantiate knowledge. But it still doesn't answer what knowledge actually is." and "Ignore the fact that they were evolved to solve a problem, I want to know what that evolved information actually is, given the environment it was instantiated in."
- S63 and S72: "The execution environment is an important clue." "The environment is the thing that does selecting. Just as an autonomous agent does selection."
- S71: "I don't know yet. Avida can exhibit a type of autonomy. But can you give it an instinct to solve a problem without specifying exact target goals?"
- S41 Q2, to Claude's question setting a link "simply declared" against one "found by trial or worked out": "No, not if just declared". S108 (candidate C16) read this as the owner accepting that a link found by trial is not declared.
- S44 and S45: a candidate with the answer written in is "an explanation. Just not a good one"; "Yes, take the test out".
- "Knowledge without the explanation kind" is Claude's phrase for S59's reading (Avida as a working case of knowledge without explanation).

**Recommendation: Reading C with the boundary of S72, which gives Reading A's verdicts for the programs; and "the explanation kind" of S59 read as the semantics' created explanation (Build, (G), (EX)), not as its narrow "explanation" (Account and not declared).** Why:

1. **S72 draws the boundary.** The owner put the whole execution environment, checker included, inside the system under test, as the selector. C with that boundary is that framing written into the semantics, and it uses a separation the text already makes (L427: process ownership against content contribution).
2. **S60 asks to set aside how the programs came to be paid.** B makes the verdict turn on exactly that: who wrote the payer. C and A read the program's correspondence from the history inside the world it lives in.
3. **S41 Q2 separates declared from "found by trial".** B turns every link found by trial into a declared one whenever the trial's judge was written by someone, the direction S108 flagged as going against S41 Q2 (C16).
4. **S59 chose Avida as a case to build from.** Under B, Avida could never show the semantics' selected representation, surprise or selection response, in any set-up people could build; under C (and A) it can.
5. **"Knowledge without the explanation kind" survives, in the sense the sources give it.** Under every reading the semantics calls an adapted trait of a living species, taken whole, an explanation in its narrow sense where (E) holds; B cannot change that, so B gets the owner's verdict for Avida by a reason that does not carry over to the case the distinction is about (Deutsch's genes against explanations). What the semantics does say of both, under every reading, is that nothing there is constructed, so nothing there is a created explanation (L13, L411; S117 B5, B6; S125 clause 5). That is the line between the adaptive and the explanatory kind, and it does not depend on the hinge.
6. **It matches S44 and S45.** Under C, the NOT program taken whole is an explanation of NOT, and a bad one: cut into its parts it fails (F1) (B3), and the further questions it leaves open (why NOT, why these numbers) are the ones the owner said make an explanation bad, not absent.

**What could count against the recommendation.**
- S71 and S72 ask for an execution environment "without specifying exact target goals", which shows the owner treats a people-named target as a real limit of what Avida shows. B puts that limit into provenance. C puts it into content: the programs' correspondence is with the relation that people named (S125 clause 3), which is a limit on what they are *about*, not on whether they were selected.
- If the owner holds "Avida's programs are no explanations" in the narrow sense, as a premise, C and A make that premise an argument against (Suff) for the owner (MC1). The owner would then have to drop the premise, or (Suff), or read "explanation kind" as created explanation.
- C makes provenance relative to a boundary, a new index on a relation the text says is fixed by the physical history (L193).
- The second open point (section 5) must be settled with it, or C and A give the programs of the graded runs no selected provenance after all.

## 7. Wording each reading would need (proposed, not applied)

Each is written as a change to the text at the line named and a matching change to the formal core; S40 asks that fixes be maths and code rather than prose, so the text change is the least that says it, and the formal change is the main one.

**For A.**
- Text, L195, after the formula: *"A rule of the physical module is no member of a history; in a simulated world, the world's program and settings as fixed before a run belong to the physical module (Part XII), whoever wrote them."*
- Text, L481, at the end: *"The environment that enacts a survival condition may be a rule of the physical module, and a rule represents nothing."*
- Formal core, D12.1: the quantifier "∃o ≺_{h(t)} o_t" ranges over Occ (D11.1) and not over Θ's rules; I52 settled as "occurrences of h(t), the rules of Θ excluded"; D0.1 notes that for a simulated world Θ is its program as fixed at the run's start.
- What it leaves to say: where a person or driver who chooses during the run falls (an occurrence, under this wording).

**For B.**
- Text, L195, after the formula: *"An occurrence that computes the survival condition, or a record made from one that represents it (Representation, below), represents the survival condition, whatever made it; a correspondence selected through it is declared unless a construction trace prepares it."*
- Formal core, D12.1: I52 and I167 settled as written, with h(t, o_t) including every occurrence causally upstream of o_t, the writing of a world's rules included; D12.3's record clause applied to code (FC12.new2 (a)).
- What it leaves to say: whether the clause is restricted to people (the text has no ground for it) or reaches every chooser that represents the criterion.

**For C.**
- Text, L195, after the formula: *"The history of a holding is read inside the system boundary declared for the claim (Part XII). A process inside the boundary whose correspondence entered it whole from outside has, there, neither a selected nor a constructed history, and represents nothing there; what it carries is a contribution from outside the boundary (Part X, Ownership). A provenance is relative to the boundary declared, as a capability is, and the boundary is declared before the attribution, not chosen after it."*
- Text, L193: "exactly one of three provenances, determined by its history in the physical module" becomes "... determined by its history in the physical module inside the declared boundary".
- Text, L522 (declared inputs): add *"the boundary of a provenance claim"*.
- Formal core, D12.1, D12.3: h(t) := h(t, o_t) restricted to the occurrences inside β (D15.4, core line 594); I167 extended so; D12.3's record clause applies to transfers inside β; a holding whose correspondence enters β whole gets Dec inside β.

**The survival condition (needed with A or C; companion file, item 4).** Text, L195: "a survival condition requiring fidelity on H" becomes *"a survival condition under which fidelity on H changes which members persist or are copied (a requirement is one such condition; a higher rate of copying for members faithful on H is another)"*; formal core, D12.1's surv: Env is no longer ⊤ but the requirement that, in h(t), members of 𝒯 faithful on H are copied or persist at a higher rate than members that are not, other things in the population being equal (read through Θ).

**A further proposal, if the owner wants "explanation" itself to exclude what selection makes.** Not a reading of the hinge. D16.XV and (Suff): explanation as Account ∧ Con(t) in place of Account ∧ ¬Dec(t); L13, L17, L49, L69 and L536 changed with it, and Grievance 6's "Construction is a separate provenance with a separate trace, and every creative attribution requires it" would then cover explanation, not only creativity. Against it: the owner's S41 Q2 as S108 read it (C16 was the computed version of this change and was flagged for that reason: it took the owner's sign and weathervane out wherever they were reached by trial); the text's own claim that the object layer, made by selection, is what explanation operates on (Part IV; (Prov) (iii)) would need restating; and S44 and S45's generous use of "explanation".

## 8. What is unsure

- Every verdict on the readings is Claude's argument from the text and the formal core; only MC1 (S117) was computed, and only for A and B on one program. C was not computed; under the S72 boundary it gives A's model values by construction of the reading, not by a run.
- The counts of section 4 were moved by hand, not by S117's scripts.
- Whether the clause of D12.1 reaches mate choice and the child's grammar (B's wider commitments) is Claude's reading; S124 made the grammar point first (its Reading 1).
- Whether Avida's own divide checks (minimum size, copied fraction) are a people-written computation of part of the survival condition for the copy machinery, which would carry B's verdict to the copying correspondence too, was not looked into; Avida's source was not opened for this job.
- The owner's "the explanation kind" may mean something narrower or wider than the semantics' created explanation; the recommendation rests on reading it as the sources do (Deutsch's adaptive against explanatory knowledge; S110, S123), which the owner has not confirmed.
- S126's knock-out run was not read; nothing here depends on it.
