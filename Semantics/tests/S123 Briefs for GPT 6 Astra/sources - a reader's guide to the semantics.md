# A reader's guide to the semantics, for the S123 briefs

*Written by Claude on 2 October 2026 (log S123) for GPT 6 Astra. The attached text, `sources - the semantics, standing alone, after round 4.md`, is cited "L" + line. Its formal core (not attached) is cited by definition id (D) with the core file's line, and its formal claims by id (FC). For each term: where it is defined, what it means in a few lines, and how a test in Avida would or would not touch it. The Avida notes summarise the project's mapping of the Avida work onto the semantics (log S117) and a later assessment (S123); they are readings to test, not settled. The text never uses the word "knowledge".*

## How to use it

Read Part 0 (L7-61) and Part IV (L165-225) of the text first. A brief that asks what a test "tests and does not test" means: which of the terms below the test's outcome could bear on, and which it could not.

## 1. Organizations, roles, kinds (Part II)

- **Organization** (L83-105; D1.1, core L50): ports with value domains, components with footprints, boundary conditions, admitted edits; the solutions are the valuations every component allows (O). A **deleted component** imposes the full relation on its ports (L103; D1.3, core L64). *In Avida*: a program is an organization; instruction ablation (an instruction swapped for a do-nothing) is **not** deletion: the do-nothing still acts (an unused read shifts later reads), so it is an admitted edit that replaces a component (L103: "A changed rule is a changed component").
- **Roles** (L107-109; D2.2-D2.6): input, output, observation are read off which edits are admitted, not stipulated.
- **Kinds** (L111-127; D4.1-D4.2, core L142-146): two components are one kind on a contract when their responses to its changes coincide; a finer contract can separate them. *In Avida*: programs alike in the world's input order come apart under other orders.

## 2. Questions and contracts (Part III)

- **Question** p = (D, C, b0, 𝒬, O_p, ρ_p) (L131-147; D3.1, core L104): a target, a **contract** C (the admitted changes the claim ranges over), a baseline, a query, aims, and the contract's provenance. The **respect** is fixed by the query and the contract's shape (L149-151).
- **Provenance of a contract** (L153-155; D3.4, core L118): declared, selected or constructed; a claim that an episode **found** a question needs a constructed contract. *In Avida*: every task is a declared question (written in C++ beforehand); no Avida process has found a question.
- **Scope** (L157-161; D3.5, core L122): a contract is a stated subset of the changes its target admits; the exclusion must be stated.

## 3. Occurrences, layers, transports (Part IV)

- **Occurrence** and **content** (L167-169; D11.1-D11.2, core L428-430): a physically located carrier; an organization with its commitments.
- **Object layer P** and **simulation layer S** (L171-179; D12.6, core L480): P's ports are persistent things (boundaries, identity; edits include displacement, occlusion, re-identification); S is over P and its queries are predictions. Nothing assumes either exists. *In Avida*: neither exists; programs read numbers. A state grid (positions, movement) is the nearest stock feature.
- **Transport** t = (π, τ, σ, λ) from D to E (L181-189; D5.1, core L186): π carries valuations, τ edits, σ boundaries, λ assigns each component of E a subnetwork of D with a port translation. **Faithful on C** when (F1) and (F2) hold (below; D5.7, core L214).
- **Functional transport** (L353; FC64): if π∘S_a = T_a∘π for each admitted generator, the same holds for every finite composition: the represented process tracks the target process step by step. **Relational transport** (L355-361; FC65): a relation preserving transitions forward (T1), backward too for equivalence; relations **compose** when intermediate scopes agree. **Approximate transport** (L363, (T2)): a one-step error bound accumulates at a stated rate. **Recoding** (L365): an invertible declared recoding preserves content; a section filled from another source keeps that source's history. *In Avida*: a data stream read by a program is the domain side of a data transport; what it is about depends on where the stream comes from (Avida's own generator, in every run so far).

## 4. The three histories (Part IV, L191-201)

A transport whose domain is physical has **exactly one** provenance, fixed by its history, not its outputs (L13, L193).

- **Selected** (L195; D12.1, core L454): a population 𝒯 of candidate transports, a variation operator μ, a finite nonempty history H of changes that actually occurred, survival requiring fidelity on H (plus whatever the environment enacts, L481); **and** no earlier occurrence in its history represents the transport, H, the survival condition or its codomain; **and** no construction trace prepares it. "What H leaves open about t is what 𝒯 leaves open" (L195; Argument 3).
- **Constructed** (L197; D12.2, core L458): prepared by a construction trace (Build, below) in an episode in which the transport, or what it carries to, is held as a represented target.
- **Declared** (L199; D12.3, core L462): neither. A relay or record keeps its source's provenance (L211; D12.3).
- **Per part** (D12.4, core L468): each part of a transport carries its own provenance; "A small binding newly prepared inside received content is construction of that binding" (L405).
- Arrangement (L201): selected transports at the object layer, constructed ones at the simulation layer, is one possibility; "Construction may operate on selected material."

*In Avida*: whether an evolved program's correspondence with its task is selected or declared turns on an **open reading** (S117): **Reading A**, the C++ that checks the task is part of the world's rules, so the program's history holds no represented target and its correspondence is **selected**; **Reading B**, that code is an earlier occurrence that represents the task (people wrote it, it computes the task), so the correspondence is **declared**. The project's owner has not chosen; give results under both. Nothing in any Avida history has met **constructed**.

## 5. Representation, prediction, surprise (Part IV)

- **Representation** (R) (L203-213; D12.5, core L474): an occurrence represents a content at a grain when a transport from the organization it instantiates to the content is faithful on the content's contract **and** selected or constructed. "A declared transport does not make an occurrence represent anything" (L211). A system can represent a theory in error (L211). The one import is Org_ℓ, what organization an occurrence instantiates (L213). *Keep apart*: a correspondence that merely holds (faithful, but declared) is not representation.
- **Prediction, violation, surprise** (L215-223; D12.7, core L488): for a transport to the simulation layer, the prediction is its answer at an occurring change; a **violation** is a fidelity failure there; **surprise** is a violation of a **selected** transport at a change outside its history. A constructed transport can be violated, never surprised. **Argument 4** (L578-584): surprise needs a history strictly smaller than the contract.
- **Two responses** (L225; D12.8, core L492): a **selection response** extends H and re-tunes within the population; a **construction response** builds a new organization or transport with a construction trace; only the second can be originative. *In Avida*: programs fail at input orders the world never gives, which has the shape of surprise, but no program predicts and the world never changes its order, so nothing is surprised (S117, B7). A stream whose rule switches (S120's ready run) gives a violation for a forecasting program; whether it is surprise in this strict sense turns on the missing object layer.

## 6. Account, and being an explanation (Part V)

- **Candidate** ℰ = (E, p, t, Γ) (L231; D5.3): an organization, a transport from the target, and the commitments offered as doing the work.
- **(F1)** component fidelity (L233-237; D5.4, core L198), **(F2)** the assembled organization agrees (L239-243; D5.5, core L202), **(A)** question fidelity (L247-251; D5.6, core L206), **Dependence** (L255; D6.4-D6.5, core L234-239: some contrast is lost when a block of commitments is deleted), **Non-vacuity** (L257; D6.6, core L243).
- **Account (E)** = F1 ∧ F2 ∧ A ∧ Dependence ∧ NonVacuous (L259-265; D6.7, core L247). **Being an explanation** = Account ∧ ¬Dec(t) (L17, L49, L69; D16.XV, core L638): a declared transport meeting (E) is no explanation.
- **What (E) excludes** (L267-277): a table of observed answers fails (F1); a reversed calculation fails (F2) on the production contract. *In Avida*: a whole program, as one block, meets (E) for its task on the numbers the world hands in; cut into instructions it fails (F1); so under Reading A it is an explanation of its task (of Avida's rule), under Reading B not (S117, B1). S112's circuits fail (A) at most single ablations (B3).

## 7. Routes, rivals, problems (Part VI)

- **Routes, critical blocks, boundaries** (L285-313; D7.1-D7.6): which subsets of commitments meet (E); a block can be critical when no single member is. *In Avida*: a task done in two places is stopped only by a pair of ablations.
- **Rivals, conflict, conflict with a claim** (L315; D8.2, core L301; D8.3, core L313; D8.5, core L325): two candidates offered one in place of the other that give different answers at some admitted change. **Rivals are not a selection population** (L315).
- **Problem, test, easy to vary** (L317; D10.1, core L400; D10.3, core L410; D10.4, core L414): two rivals neither ruled out for an assessor; a test records what the target does where they conflict; "easy to vary" is a problem of the kind whose conflict lies outside the contract. *In Avida*: programs competing for cells are not rivals in this sense; nothing in Avida offers or rules out candidates.
- **A failed answer stays failed; historical index** (L367-369).

## 8. Histories, criticism, use (Part IX)

- **History, active route** (L375; D11.3, core L434; D11.4, core L438; occurring pairs, D11.5, core L442): a set of occurrences with an acyclic precedence; an active route joins a represented input to an operative result.
- **Criticism and bearing (K1)** (L377-383; D9.10, core L384): a criticism has a target, an alleged defect, a premise and a connection; it bears when its connection is an account. "An adverse signal is not a criticism until an organization represents it as the premise of a criticism alleging a defect in a target." (L383). *In Avida*: withheld pay is a signal, not a criticism.
- **Reason use, usability (K2), what a test rules out (K3), arguments** (L385-397; D9.6, core L353; D9.9; D9.11).

## 9. Construction and origin (Part X)

- **Deploy, repertoire** (L403; D13.1, core L504; D13.2, core L506): holding a representation integrated into problem-directed activity as a retained capability.
- **Build** (construction) (L405-411; D13.3, core L510): an actual subhistory owned by the system prepares a held content for explanatory use, contains a nontrivial binding construction, and is not a composition of content-preserving transfers. "Reconstruction by a learner is construction; relay is not." (L405). An inexplicit representation is not an absent one (L407). Use alone does not construct (L409). "Construction is not selection" (L411). *In Avida*: copying a program is relay; nothing in a program's run builds a binding against a target (processors reset at division). Learning within a life (as in a modified Avida, see the Pinker note) is the first place Build could be asked.
- **Newness (N)** (L413-417; D13.4-D13.5, core L514-518), **Origin (G)** (L419-425; D13.6, core L522), **Ownership** (L427; D13.7, core L526: processes inside a declared boundary are the system's, whoever wrote them), **Episodes, recognized difficulty** (L429; D13.8, core L530).

## 10. Repair and created explanation (Part XI)

- **Repair (P)** (L435-441; D14.2, core L544) and **created explanation (EX)** (L443-453; D14.7, core L568): an episode that repairs an explanatory aim by an originative, deployable account whose binding lies on the active route of the repair. *In Avida*: nothing; (EX) needs (G), which needs Build.

## 11. The physical module (Part XII)

- **Tasks; retained realization (CT1); retention (CT2)** (L461-471; D15.1-D15.3, core L580-590): constructor theory's tasks and catalysts, stated for the semantics.
- **System boundary and continuity** (L473; D15.4, core L594): declared before an attribution; a process run inside the boundary is the system's whoever wrote it. **Owned capability** (L475; D15.5, core L598). **Achievement** (L477). **Tolerances** (L479).
- **Selection in the physical module** (L481; D15.8, core L610): a selected provenance is a claim about a physical history, with "a survival condition enacted by the environment". *In Avida*: the execution environment enacts it; whether the programs, the execution environment or both are the system is a declared boundary, not a finding.

## 12. Recursion, the class, what would rule it out (Parts XIII to XV)

- **Scrutinizability, recursive capacity, barriers, universality** (L485-509; D16.1-D16.4, core L616-632): "Recursion does not entail universality" (L509).
- **The class collected; dependence order** (L513-528); **what would rule it out** (L532-546), among it **(Prov)**: a selected transport fixed at an unseen change though its population held a differing survivor, or a method that rewrites every construction trace as selection (L542).

## 13. Arguments to know (Part XVI)

- **Argument 3** (L570-576): selected transports are underdetermined on unseen changes their population leaves open. *In Avida*: computed on 16 of 18 saved populations for input order (S117).
- **Argument 4** (L578-584): surprise requires an incomplete history.
- **Argument 9** (L614-616): output descriptions do not determine accounts.
- **Argument 10** (L618-632): a two-layer episode: a selected occupancy predictor is surprised at re-emergence after occlusion; selection cannot repair it (structural failure); a constructed layer with a persistence component can. It is a worked example of the selected and constructed responses, and of what an object layer is; "It is not a claim that any actual infant, animal, or program instantiates it." (L632).

## 14. What an Avida test can and cannot touch, in one table

| Term | Can a test in stock Avida bear on it? |
|---|---|
| organization, kinds, contracts, transports, fidelity | yes, computed (S117) |
| selected provenance, Argument 3 | yes, under Reading A; declared under Reading B |
| representation | only as the reading allows; about Avida's own rules |
| prediction, surprise | not in the strict sense (no object or simulation layer) |
| construction, origin, (EX) | nothing found; asking needs learning within a life or another environment |
| criticism, problems, rivals | nothing in Avida offers or rules out candidates |
| boundary, ownership | yes, but the boundary is declared, not found |
