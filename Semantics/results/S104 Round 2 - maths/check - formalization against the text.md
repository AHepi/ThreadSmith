# S104 Round 2 — check: the formalization against the text

*Log S104, review round 2 (the maths round), 27 September 2026, under decision S36 ("if implementation forces invention, that needs to be recorded"). A fresh reader (Opus 5.5) compared every definition of `formal core.md` (D0.1–D18.2, E1–E9) and every claim of `formal claims.md` (FC01–FC110) with the sentences they quote from `tests/103 The semantics, standing alone, after round 1.md` (md5 f31ebb1f050783f1a84f6136cec20fcd, not written to), and read `inventions register.md` (I01–I102), `search results.md` and the parts of `model/` a result turned on. No other file was edited. Nothing is committed. Every block quotation of the text is written `> Lnnn | …` and was compared by program with the line it names; " … " joins fragments of one line, in order. Inline quotations of the text were compared with the text in the same way. Quoted words of the formal core, the register, the search results or the code are said to be theirs where they appear.*

**The question asked.** For every formal definition and claim: does it say what the quoted sentence says, no more and no less? Three lists follow from it: (1) content the maths adds that the register does not record (hidden inventions, H01–H20); (2) registered inventions that the text itself fixes, so that they are not inventions (T01–T15, with four more where the text's own wording points to the other choice); (3) reading choices where the other reading changes a search result (R01–R25). §4 and §5 give a verdict for each definition and each claim; §6 says what each of the twelve counterexamples is a counterexample to.

**Three computations of this check.** Where a claim below says that another reading changes a result, it is either read off `search results.md`, or reasoned in the entry, or computed by one of three small scripts run from the scratchpad against `model/` unchanged (no byte code written). Their code is in the Appendix, so each can be rerun. They are marked [computed here].

## Summary

- **Hidden inventions: 20 entries (H01–H20).** Among them:
  - **H05.** D12.1 takes L195's sentence ("No member of the history represents \(t\), \(H\), or the survival condition") as the only limit on what a selection history may represent. It leaves out L201 and L411, which say that a selected transport has no represented target in its history. L411 is quoted nowhere in this round's files; L201's clause is quoted only in the register, under I53. Four of the twelve counterexamples rest on this omission: FC78, FC81 (d), FC82 and FC83. With L201 and L411 read into Sel, none of the four arises on the same models [computed here]. The register's own entry I53 says "Sel has none", which D12.1 does not encode.
  - **H01.** D2.1 does not count a composite of two setting edits as setting either port. By I08 it then counts as an edit to the rule of each component it alters. The result "Composites collapse the families", as the implementer's summary of this round puts it, rests on this reading. When a composite of settings counts as setting each port it sets, no component on the pole's C2* has the rule signature under either reading of observation. Under R-ii, the families on C2* are then the same as on C2 [computed here].
  - **H10.** The word "differ" is read two ways. In conflict (D8.2, L315) an undetermined answer differs from a determined one; in non-circular dependence (D6.4, L255, I22) it does not. FC48, and with it L317's "Their answers then agree at every pair of \(C\)", holds only under the first reading. Under the second there is a model with no conflict at a pair of C and different answers there [computed here].
  - **H11.** D11.4 drops L375's clause on a route "already at rest when the result occurred". The FC75 Look found that D11.4 counts such a route as active. That is a property of D11.4, not of L375.
  - **H06.** D13.8 makes an episode any subhistory. L55 says "An episode is a history in which contracts change, and every change carries a provenance record."
  - **H12.** D9.10 is tagged [I76], but I76 covers only L161's defects of a question. What D9.10 invents (p_δ and ℰ_c supplied with the criticism) is not in the register.
  - **H17.** In the encoding of Argument 10 the two things may share a cell and pass through each other. FC102's two-thing result rests on this, and it is not in I68 or I100.
- **Inventions the text fixes: 15 entries (T01–T15).** The counterexamples to FC05 and FC18 rest on readings that the text's own words exclude: I93 (ii) is excluded by "stay equal" (L119), and I94 by the formula at L556. I15, I35, I36 and I37 are given by the text's own wording at L231, L315, L562 and L317. I80's literal reading, that the identity edit is a setting edit, sits against L103, L141 and L325. For I27, I40, I65 and I29 the text's words point to the alternative the register lists.
- **Reading choices that change a result: 25 entries (R01–R25).** Eleven are reported both ways in `search results.md`. The rest are reported only in part, only as a Look, or not at all; among them are R06 (FC48), R09 (FC28), R11 (FC78, FC81 (d), FC82, FC83), R13 (C2*) and R20 (FC21 (a)).
- **The twelve counterexamples (§6).**
  - Five are counterexamples to a formal claim's own statement or to a formalizer's gloss, not to a sentence of the text: FC20, FC23 (b), FC25 (b), FC77 and FC102 (b).
  - Two rest on readings the text excludes: FC05 and FC18.
  - Four rest on the omission of L201 and L411: FC78, FC81 (d), FC82 and FC83.
  - One is a model in which a sentence of the text fails under a reading the text leaves open: FC63 (c-i), for L343's "meets (F1)" when the sum component relates every tuple of term values.
  - Several results reported as holding bear on the text's sentences more directly than the counterexamples do: FC21 (b), FC25 (a), FC70, FC08, FC07, FC23 and FC34 (§6).

## 1. Hidden inventions

Each entry gives where the maths makes the choice, the sentence it fills in for, what was added, the other choices, and what depends on it. None of these is in `inventions register.md` in the form given here.

### H01 · A composite of settings is no setting edit, so it is an edit to the rule (D2.1 with D4.6 and I08)

> L103 | An edit that sets a port replaces the component assigning that port; it does not add an equation beside an incompatible one.

> L119 | An edit that sets a port replaces only the component that assigns the port (above), not the relations of the components that read it

> L125 | - a **rule application** has a signature invariant under interventions on the world and variable under edits to the rule.

- **Added.** D2.1 asks a setting edit to leave every other component as it was. A composite such as set(H=1, L=1) replaces c_H and c_L, so it sets neither H nor L. D4.6 and I08 then class every edit that alters j and is not in Set_{o_j} as an edit to j's rule. So a composite that sets c_H's own output, together with another port, counts as an edit to c_H's rule.
- **Recorded, and not.** I04 records the surgical form of D2.1. It does not record this consequence, and neither I04 nor I08 lists the other choice.
- **Other choices.**
  - A composite of settings sets each port it sets. L119's "only" then reads as said of one setting. L91's "closed under a partial associative composition" puts such composites into A whenever they are defined.
  - Or: a composite that sets j's output is no edit to j's rule, even though it is no setting edit either.
- **Depends on it.**
  - The FC07 part "pole C2 with composites" (C2*): no component is causal, and every component has the rule signature under both readings. This is the result the implementer's summary calls "Composites collapse the families".
  - Under the first other choice [computed here], C2* gives no family at all under R-i, and c_H, c_L, c_θ causal under R-ii. No component has the rule signature under either reading.
  - C2's own families are the same under both choices.
  - FC06 also rests on D2.1 as written: a composite in Set_H would alter c_L, a reader of H.

### H02 · "its output port" read as the port the component assigns (D4.6)

> L123 | - a **causal assignment** has a signature that changes under intervention on its output port and is invariant under observation edits;

> L109 | A port is an **output** of component \(j\) when its value is determined by \(L_j\) given the other ports of \(V_j\) across \(B\).

- **Added.** D4.6 reads "its output port" as o_j, the port j assigns (asg, read off the setting edits). It does not use the output that L109 defines (D2.3). FC02 (c) shows the two come apart on the pole: by D2.3, H and θ are outputs of c_L as well as L.
- **Other choice.** Use D2.3's outputs. A component with several outputs then needs a rule of union, as I102 gives for asg.
- **Depends on it.** The Causal predicate in FC06, FC07 and FC10–FC13. On the pole's C1 and C2 the families come out the same under both choices (reasoned), because setting H or θ never alters c_L. Random families were not searched under the other choice.

### H03 · A setting edit sets its port at every boundary (D2.1)

> L109 | A port \(v\) is an **input** under \(A\) when \(A\) contains an edit that sets \(v\) directly.

- **Added.** "Set_v := the edits of A that, at every b, set v through some component". I04 speaks of setting "at boundary b". The quantifier over boundaries is not recorded.
- **Other choice.** At some b, or at the boundaries of the contract in use.
- **Depends on it.** Input, asg, and every family predicate. No result was computed under the other choice.

### H04 · Direction defined as (Input_A, asg) (D2.5)

> L109 | The direction of an organization is a consequence of which edits it admits, not a stipulation about which way an equation is read.

- **Added.** The text says what direction is a consequence of, not what it is. D2.5 makes it the pair (which ports A sets, which component each setting edit replaces). It has no invention number.
- **Depends on it.** FC02 (a) and (c) ("the direction H,θ → L is carried by asg, not by output status").

### H05 · Selection limited by L195 alone; L201 and L411 left out (D12.1)

> L193 | A transport \(t\) whose domain is an organization of a physical system has exactly one of three provenances, determined by its history in the physical module:

> L195 | No member of the history represents \(t\), \(H\), or the survival condition.

> L197 | in which \(t\), or the organization it carries to, is available as a represented target.

> L201 | Neither provenance is reducible to the other: a selected transport has no represented target and no criticism in its history; a constructed one has both.

> L411 | Construction is not selection. A selected transport has no represented target in its history; a constructed one does.

- **Added.** D12.1 forbids only occurrences that represent t, H or the survival condition.
  - By L197, a represented target is "\(t\), or the organization it carries to". So a represented codomain is left open in Sel's history, and so is a criticism.
  - L411 is quoted nowhere in `formal core.md`, `formal claims.md` or the register. L201's clause is quoted in the register under I53 and nowhere in the formal core or the claims; FC78 quotes another sentence of L201, and NF07 sets L201 aside for the word "reducible".
  - The register's own I53 says "Con then excludes Sel (Con puts a represented target in that history; Sel has none)". D12.1 does not encode "Sel has none".
- **Recorded, and not.** `search results.md` names L201 under FC78, but the register has no entry for the choice. I52 lists as other choices only "no physical witness" and "H required to be nonempty"; I53 lists only Sel and Con "evaluated on different parts of the history".
- **Other choice.** Sel's history contains no represented target (neither t nor the organization it carries to) and no criticism, as L201 and L411 state of every selected transport.
- **Depends on it.** FC78, FC81 (d), FC82 and FC83 all use the history of `prov_counterexample()`, in which occurrence o1 represents the codomain.
  - With L201 and L411 read into Sel [computed here], Sel on that history is False and Con is True. FC78's "exactly one" then holds, the surprise of FC81 (d) does not arise, and the selection response of FC82 and FC83 is False.
  - FC84's second sentence also rests on this entry; see §5.

### H06 · An episode is any subhistory (D13.8), against L55's sentence

> L55 | An episode is a history in which contracts change, and every change carries a provenance record.

> L197 | **Constructed.** There is an episode (Part X) whose construction trace prepares \(t\)

- **Added.** "An episode is a subhistory" (D13.8), with no invention number. This makes the "episode" of L197, L405 ("delimited at \(e\)") and (G) as wide as any subhistory. L55's sentence sits in the front matter. L35 says of the front matter that it "states nothing the body does not state more exactly", and the body never defines "episode" by itself.
- **Other choice.** L55's reading: a history in which contracts change, each change with a provenance record.
- **Depends on it.** Con (D12.2) and so FC78–FC84 and FC95. The model's `con(h)` takes no episode at all: it holds when a trace in h prepares t and t or its codomain is a represented target in h. Under L55's reading, Con in the FC78 family of models would also need a contract change with its record, and the hand-set histories state none. This was not computed. I90 covers setting Θ by hand; it does not cover what an episode is.

### H07 · Surprise with the selection parameters bound by "for some" (D12.7)

> L217 | Let \(t\) be a transport to the simulation layer \(S\), with contract \(C\) and, where \(t\) is selected, history \(H\).

> L221 | - **surprise** is a violation of a selected transport at \((a,b)\notin H\).

- **Added.** "Surp(t; a,b) :⟺ Sel(t; 𝒯, μ, H) for some 𝒯, μ, H with (a,b) ∉ H, and Viol(t; a,b)". L217 gives t one history H, and L193 says provenance is "determined by its history".
- **A consequence the formal core does not note.** Sel asks for (F1) and the (F2) equation at every pair of H, and Viol is their failure at (a,b). So Viol(t; a,b) already puts (a,b) outside every H on which t survives, and the clause "(a,b) ∉ H" does no work in D12.7.
- **Other choice.** H is the one history of t's selection, fixed by the physical history.
- **Depends on it.** No computed result: FC81 (d) uses a fixed H.

### H08 · The two responses (D12.8), and the model's responses

> L225 | A **selection response** extends the history \(H\) of a selected transport and lets \(\mu\) act: the transport is re-tuned within the population. A **construction response** introduces a new organization or a new transport with a construction trace.

- **Added in D12.8.** SelResp uses μ*, any number of μ-steps including none, so t' = t is allowed. ConResp reads "new" as New (N) relative to a repertoire. Neither choice has a number.
- **Added in the model.** FC82 and FC83 compute the selection response as `sel(c, H + [x], h)` alone: no violation at x, no μ step, and t' = t. The responses to a violation that L225 distinguishes are not modelled; what is computed is Sel on an extended history.
- **Depends on it.** FC82 and FC83. Their counterexamples show only what FC78 shows (Sel and Con on one history). They say nothing further about responses.

### H09 · The population: D12.1's "the members of 𝒯 are admitted by the physics" against L481's "The population is the set" (D12.1, D15.8, model)

> L481 | The population is the set of transports the physics and the stated construction admit; a transport that would need a part every member of the population is built without is not in it.

- **Added.**
  - D15.8 writes 𝒯 := {t : Θ admits t ∧ parts(t) ⊆ …}, an equality. D12.1 asks only that "the members of 𝒯 are admitted by the physics", an inclusion.
  - The model's witnesses use 𝒯 = {t} and μ the identity: a population of one, with no variation.
  - "parts(t)" is not defined or registered.
- **Other choices.**
  - 𝒯 is the whole admitted set, as L481 has it.
  - Or a population with a variation operator that moves something (L155: "the surviving member of a population under a variation-and-survival history").
- **Depends on it.** The witnesses of FC77, FC78, FC81 (d), FC82 and FC83. No status changes on these models, since Θ is set by hand (I90) and could admit {t} alone. The remark under FC77 in `search results.md`, "(R) keeps content from 'selected' only through Θ's admission of t, through Hom, or through a requirement of a nonempty history" leaves out L481's equality.

### H10 · "differ" read two ways (D8.2 against D6.4)

> L315 | Two candidates **conflict** at such a pair \((a,b)\) when their answers there differ

> L255 | the answer of \(E\) at \((\tau(a),\sigma(b))\) differs from its answer at \((1,\sigma(b_0))\)

- **Added.**
  - In D8.2 (and `conflict()` in `model/core.py`), an undetermined answer ⊥ differs from a determined one.
  - In D6.4 (I22), "differs" holds only between two determined answers.
  - I21 records only that ⊥ = ⊥. Neither entry records the choice for L315, or that the same word gets two readings.
- **Depends on it.** FC48 holds because a pair with answers 0 and ⊥ is a conflict pair by the first disjunct. Under L255's reading carried into L315 [computed here]:
  - Candidate E1 answers 0 and can meet (F1), (F2) and (A) under the target's relations.
  - Candidate E2 has the answer ⊥, because a background component empties Sol_E. It can meet under no relations.
  - At (1, b0) ∈ C there is then no conflict, and the answers differ.
  - So L317 (ii)'s "Their answers then agree at every pair of \(C\)" holds under D8.2's reading and fails under D6.4's.

### H11 · The "already at rest" clause dropped from active routes (D11.4)

> L375 | A route that started and did no work, or that was already at rest when the result occurred, is not active for that result; whether a route is active is read from the history, not from the result.

- **Added.** D11.4 (I46) has no clause for a route at rest when the result occurred, so it says less than L375. I46's entry does not record the omission. I95's other choice ("occurrences with time stamps and persistence made explicit") names what would be needed.
- **Depends on it.** The FC75 Look ("D11.4 counts it active", in `search results.md`) and the line on the L375 "already at rest" route in the implementer's summary. L375 excludes such a route in so many words. What stays open in the text is only whether a finished route whose product persists is "at rest".

### H12 · Bearing: p_δ and ℰ_c supplied with the criticism; the tag names an entry for another sentence (D9.10)

> L377 | Let \(p_\delta\) be the question whether \(z\) has \(\delta\) in respect of \(p\), and \(\mathcal E_c\) the explanatory candidate (Part V) for \(p_\delta\) whose organization is the criticism's connection from \(g\) to \(\delta\), with its transport and its identified commitments.

- **Added.** In D9.10:
  - "p_δ, the question whether z has δ in respect of p, is supplied with c" (tagged [I76]);
  - the connection "an organization from g to δ";
  - t_c, Γ_c and δ_c supplied.
- **Recorded, and not.** I76 fills in for L161 only (a question's three defects). D9.10's choices are in no entry.
- **Depends on it.** FC74, FC76 (the ¬Bearing half) and FC107.

### H13 · "actually occurring" as a primitive with no entry (D11.5)

> L217 | For an edit–boundary pair \((a,b)\in C\) actually occurring:

- **Added.** Occurs(a, b, ξ), "a primitive read through Θ". D0.2 lists it, the only listed primitive with no invention number.
- **Depends on it.** Sel (D12.1: "its pairs having occurred"), Surp (FC81) and FC102 (a), which was not tested.

### H14 · Contribution of content as a primitive (D13.7)

> L427 | Contribution of content and ownership of a process are different attributions

- **Added.** "Contrib(h', w) records who supplied a content". It is not in D0.2 and not in the register.
- **Depends on it.** No claim.

### H15 · The four parts of a critical episode, and "connected to its inquiry" (D13.8)

> L429 | **Episodes.** A complete critical episode contains a recognized difficulty, a target available before its criticism, a conjectural objection, and a content-sensitive response. … A creative critical episode contains an instance of (G) connected to its inquiry.

- **Added.**
  - The word "available" is read as "represented".
  - The phrase "a conjectural objection" is read as "a criticism (D9.10)".
  - The phrase "a content-sensitive response" is read as "a response that uses the criticism as a reason (D9.11)".
  - The phrase "connected to its inquiry" is read as "the (G) instance's Attempt addresses the question the episode's difficulty poses". The formal core marks this last one "not fixed by the text" but gives it no number. The §13 Vague note points to [I55, I56], which are Deploy and Build.
  - How s and Δ enter CreativeCriticalEpisode(s, Δ, h, e) is not said.
- **Depends on it.** (EX) and so FC89 and FC90, both not tested.

### H16 · "can affect its operative use" read as "on an active route" (D16.1)

> L487 | the result can affect its operative use.

- **Added.** D16.1 reads it as "a result on an active route to d's operative use". I74, which quotes L487's own wording, keeps "can change its operative use".
- **Depends on it.** (RC); FC94, not tested.

### H17 · Two things that may share a cell and pass through each other (E9, I68, I100; FC102)

> L620 | Stipulate an object layer \(P\): a line of cells; two things, each with a position and a velocity; continuity components; admitted edits: displace a thing, set its velocity, occlude a cell, swap the two identities.

- **Added.** In `fc102` each thing moves as pos + vel with reflection, independently of the other. Two things may be in one cell, which reads as one occupied cell, and may cross. I68 and I100 record the cells, velocities, reflection, occlusion run and window. They do not record that the things do not interact.
- **Other choice.** Things that exclude one another (they cannot share a cell, and they bounce or stop).
- **Depends on it.** FC102 (b), second half, for two things: "a window-w predictor can fail with no occlusion at all". This finding also touches L622's stipulation "It is faithful on \(H_0\)": on this encoding it limits which histories H0 a window-w occupancy predictor can be faithful on.

### H18 · FC101's "edits deleting internal components" encoded as knock-outs (the model)

> L103 | A deleted component imposes the full relation on its ports.

- **Added.** FC101 (b) speaks of "a question whose contract holds edits deleting internal components". In `fc101` the edits del_r1 and del_r2 set m1 := 0 or m2 := 0; they do not impose the full relation. The register entries FC101 rests on (I29, I46, I78) do not cover this.
- **Depends on it.** FC101 (b). Reasoned through with the full relation, the parallel-route candidate still fails (F1) for M1's question at every pair, because the output components differ. So the status would not change.

### H19 · Org_ℓ extended from occurrences to histories; "subhistory" (D11.3)

> L375 | A history \(h\) is a set of occurrences with an acyclic causal precedence \(\prec_h\) (write \(\preceq_h\) for its reflexive closure) and a physical interpretation supplying process occurrences, their ports, and the connections actually instantiated.

- **Added.**
  - "Org_ℓ(h) is the organization Θ gives h at grain ℓ": L213 gives Org_ℓ for an occurrence.
  - "A subhistory is a subset closed under the interpretation, with ≺ restricted." Neither has a number.
- **Depends on it.** D11.4 (active routes), and through it FC75, FC76, FC87 and FC101.

### H20 · Smaller unregistered choices

- **D3.4.** A contract's selected and constructed provenance is read "as for transports (D12.1, D12.2)". L155 gives contracts their own wording ("the surviving member of a population under a variation-and-survival history").
- **D13.6.** Attempt is "a claim read through Θ". D0.2 does not list it; I90 names it only for the program.
- **D10.3.** The shape of the argument from a test ("R* at (a,b); Meets_ab(ℰ, R*) fails; Acc(ℰ) requires it") is written without a number. FC47 (b) uses it.
- **D15.5.** "owned (D13.7) at ξ" is applied to a protocol and a constructor attribute. D13.7 defines ownership for subhistories.
- **D16.5.** "M has an instance of (G) in a critical episode" stands for L528's "connected to a critical episode".

## 2. Inventions the text fixes

Each entry gives the registered invention, the sentence that fixes it, which way, and the results it touches. "Fixes" here means the text's own words give the choice, open to another reading like anything else (S28).

### T01 · I15 ('active component' is a member of Γ)

> L231 | an identified set \(\Gamma\) of active commitments in \(E\). The commitments \(\Gamma\) are components of \(E\), those the candidate offers as doing the work

The active components are the commitments. I15's other choices ("every component of E", or every component λ covers) are excluded by L231. No result changes.

### T02 · I93 reading (i) ('stay equal' under the bijection that witnesses the kind)

> L119 | an edit under which the two relations stay equal does not separate the components.

"Stay" presupposes the equality that already holds, under the bijection that makes j and j' one kind. Reading (ii), "equal under some footprint bijection" at the new pair, is not staying equal. FC05's counterexample exists only under (ii); under (i) FC05 holds on every model tried (`search results.md`). The counterexample is to a reading, not to L119.

### T03 · I94 (the counterpart read untranslated) excluded

> L556 | By (K), \(\operatorname{sig}_C(\lambda(k))=\{(a,b,\operatorname{proj}^{\lambda}_{V_k}\operatorname{Sol}_{\lambda(k)}(a,b))\}\)

> L233 | projecting away its hidden ports and carrying what remains to \(V_k\) by the port translation of \(\lambda\) (write \(\operatorname{proj}^{\lambda}_{V_k}\) for this projection)

The text writes the counterpart's signature with proj^λ_{V_k}, which by L233 carries the relation to V_k by the port translation. That is D4.4's reading. FC18's counterexample needs both I94 (untranslated) and I14's value maps κ (the text has "a port translation" and no value maps). Under D4.4's reading FC18 holds on every model tried.

### T04 · I12, in part (σ on boundaries; τ[C] as a set of pairs)

> L556 | \(\operatorname{sig}_{\tau[C]}(k)=\{(\tau(a),\sigma(b),L_k(\tau(a),\sigma(b)))\}\)

The text translates boundaries by σ and indexes τ[C] by pairs, as I12 does. What I12 still chooses is comparing the two signatures as functions on C.

### T05 · I13 ((K) extended to subnetworks)

The same line (L556, quoted under T03) writes the counterpart's signature out in full. The extension is the text's; only its "By (K)" is loose.

### T06 · I35 (conflict given χ)

> L315 | Two candidates that some relations of the target's components would let both meet (F1), (F2) and (A) at a pair, when \(\chi\) excludes every such relation, conflict there given \(\chi\)

D8.6 is this sentence written in symbols. I35's other choice (the second disjunct of plain conflict restricted to Allow_χ) is another definition, not another reading of these words.

### T07 · I36 ('one counterpart')

> L562 | one counterpart, the same subnetwork of \(D\) with port translations that are bijections onto the same ports of \(D\)

The text says what "one counterpart" means, and I36 follows it. The other reading tested in FC44 ("the same subnetwork, whatever the port translations") is excluded by these words, so FC44's witness under it bears on no sentence of the text. I36's added "matching value maps" comes from I14, not from the text.

### T08 · I37 ('easy to vary' relative to an assessor)

> L317 | Two rivals, neither of them ruled out for an assessor, pose, for that assessor, a **problem for \(p\)**

In the text, "easy to vary" is defined by posing a problem (L317), and a problem is posed "for that assessor". The assessor-free alternative is excluded.

### T09 · I33, the symmetry of rivals

> L315 | Two explanatory candidates for one question \(p\) are **rivals** when one of them has been offered as an answer to \(p\) in place of the other

The words "one of them … the other" are symmetric. That Offered is a primitive stays an invention.

### T10 · I53 (one history)

L193 (quoted under H05) says "determined by its history", in the singular.

### T11 · I63 (a tag names the sentence before it)

> L395 | For \(T\land B\land I\Rightarrow O\), an argument usable by \(j\) that rules out \(O\) rules out \(T\land B\land I\) together for \(j\), and nothing narrower. (K3)

> L471 | the greatest fixed point is the union of the sets \(D\) with \(D\subseteq F(D)\). (CT2)

> L363 | whenever \(z,Sz,\dots,S^{n-1}z\) lie in that scope. (T2) Without a modulus, no accumulated bound follows.

The text's tags follow the sentence they name wherever the placement is unambiguous, and so do all the display \tag{}s. I63 is the text's own convention.

### T12 · I31 (the routes of the infinitary example)

> L311 | no minimal route, and no route of one commitment, exists.

With I31's other question, "is |x| ≤ 1/N for a stated N?", {d_N} would be a route of one commitment. The text's stated conclusion fixes the route family as I31 has it.

### T13 · I80, against its literal reading

> L141 | it contains the baseline \((1,b_0)\).

> L325 | Under \(A\) containing interventions on \(H\) and \(\theta\), these ports are inputs and \(L\) is an output, by Part II.

- **The text's words.**
  - The identity edit is the baseline, not an intervention.
  - A setting edit "replaces the component assigning that port" (L103), and the identity replaces nothing.
  - L325 ties input status to interventions.
  - I80's own other choice ("exclude 1 from Set_v") is the reading these lines give.
- **Results.** No status changes. FC02 (c) prints "The identity edit is a setting edit of H and of θ (I80): True", and the line "Identity edit counts as a setting edit" in the implementer's summary rests wholly on the literal reading. FC25 (a)'s reported witness is a relative of this case: a setting edit that sets p0 to the value it already has, changing no relation (see R14).

### T14 · I62, in part

> L479 | \(\mathsf{Admit}^{q,r}_\Theta\) is the set of tasks physically achievable at tolerances \((q,r)\);

A task with a realization at (q, r) is achievable at (q, r), so "Admit contains every realized task" is the text's. Antitonicity follows from "\(q\) precedes \(q'\) when \(q'\) admits no performance \(q\) excludes" (L479).

### T15 · Exclusivity of the two provenances (what D12.1 leaves open)

L193, L201 and L411 (quoted under H05) state three times that a selected transport is not a constructed one and why: it has no represented target in its history. The formal core registers the question as I53 ("one history") but leaves the text's answer out of D12.1. See H05 and R11.

### 2b. Registered choices where the text's own wording points to the other choice

| Invention | The text's words | The register's choice | Result changed? |
|---|---|---|---|
| I27 | > L257 \| every edit the target admits that is excluded from \(C\) is excluded by a stated scope, not silently. | pairs, not edits | No: I85 names every excluded pair, so both readings hold trivially in the searches |
| I40 | > L393 \| \(d\) is the conclusion of a step of the same argument as \(u\) that is usable by \(j\) | a step below u only | FC69 reports both; the words give "any step", under which (K2) has two fixed points (R15) |
| I65 | > L151 \| An identification question has a \(\mathcal Q\) that computes a fibre and a \(C\) containing edits to the observed value. | boundary variations of u_H, not edits | Yes: FC28 (R09) |
| I29 | > L231 \| for \(E\|W\), \(t'\) is \(t\) with \(\lambda\) restricted to the components of \(E\|W\), and \(\Gamma'\) is \(W\). | deletion keeps J_E whole, so λ "restricted to the components of \(E\|W\)" restricts nothing | No for port-reading queries (deletion and removal give the same Sol) |

(In the table, "\|" stands for the text's "|".)

## 3. Reading choices where the other reading changes a search result

"Said?" means whether `search results.md` reports the result under both readings.

| # | Choice (where) | Registered? | Result under the formalization | Under the other reading | Said? |
|---|---|---|---|---|---|
| R01 | Observation edits R-i against R-ii (D2.4) | I06 | FC07: on C2, c_L is a measurement and not causal (R-i) | c_L causal, no measurement (R-ii) | yes |
| R02 | "stay equal" under which bijection (L119) | I93 | FC05 counterexample under (ii) | holds under (i), which the text fixes (T02) | yes |
| R03 | The counterpart read untranslated (L119, L556) | I94 | FC18 counterexample | holds under D4.4 (T03) | yes |
| R04 | Value maps κ in port translations (D5.1) | I14 | FC18 and FC20 counterexamples need κ ≠ id; FC96 (ii) has a caveat | FC18, FC20 hold with κ the identity | yes |
| R05 | Kinds between equal domains only (D4.2) | I10 | FC18 fails under I94 | FC18's Look: holds with value bijections | in the claim's Look only; not computed |
| R06 | "differ" in conflict (D8.2 against D6.4) | no (H10) | FC48 holds | fails [computed here]; L317 (ii)'s "Their answers then agree" fails with it | no |
| R07 | Non-circular dependence as the conjunction, NC1 included (L255) | I24, I25 | FC23: the lookup fails through NC1 | under NC2 alone the lookup meets non-circular dependence, and L273 ("\(p\) because \(p\)" fails non-circular dependence) fails | yes |
| R08 | A slot at every pair of C, the baseline included (D6.3) | I24 (the quantifier is in the entry; no other choice listed) | FC26 Look: the forward pole meets (E) on C3 (settings of L only) | a slot at the pairs that set L makes c_L a slot, and NC1 fails there | partly |
| R09 | The identification contract's "edits" as boundary variations (E1) | I65 | FC28 holds | with edits that set L, (F1), (F2) and (A) all fail for E_rev (computed in FC28's Look). (F2) would fail with real values too: the target keeps H = u_H while E_rev's H follows the set L | as a Look; the status line does not say it |
| R10 | "an answer to one is not an answer to the other" (L151) | I73 | narrow: holds | wide: a candidate meets (E) on two questions (FC34 witness) | yes |
| R11 | Sel limited by L195 alone (D12.1) | no (H05) | FC78, FC81 (d), FC82, FC83 counterexamples | none of the four arises on the same models [computed here] | FC78 names L201; not registered |
| R12 | Episode as any subhistory (D13.8) | no (H06) | Con holds in the FC78 family of models | with L55's reading, Con needs a contract change with a record, which those histories do not state | no (not computed) |
| R13 | A composite of settings is no setting edit (D2.1, I08) | no (H01) | C2*: no causal component; every component has the rule signature | R-i: no family; R-ii: c_H, c_L, c_θ causal; no rule signature under either [computed here] | no |
| R14 | The identity (and a no-op setting) as a setting edit (D2.1) | I80 | FC02 (c) remark; FC25 (a)'s reported witness is a no-op setting | the reported witness goes (the status need not). A non-degenerate witness remains (reasoned): C sets a port the table's ports do not depend on, and E_tab still meets (F1). So the finding against L269's "under any contract containing one" stands | no |
| R15 | Live through a step below u only (D9.4) | I40 | FC69: well founded | two fixed points (FC69's other part) | yes |
| R16 | The range of the homomorphism clause (D5.5) | I18 | FC77: Sel(t;{t},id,∅) exactly when τ is a homomorphism | with the clause only for edits occurring in the contract (I18's first other choice), H = ∅ gives the trivial witness for every t with τ(1) = 1: the formalizer's first statement of FC77. I52's "no physical witness" alone does not do this, since Hom stays | partly |
| R17 | Which relation the Leibniz sum component carries (E6) | I99 | FC63 (c-i) fails (F1) | (c-ii) meets (E) | yes |
| R18 | Derived ports for the Leibniz terms (E6) | I81 | the candidate can be written | under I14 alone it cannot be written | yes |
| R19 | Sol of a subnetwork over its own footprints (D1.4) | I14, I32 | FC25 (b) fails with a port in no footprint | with λ(k) read in the context of the whole of D (I14's first other choice), E_enc meets (F1) | yes |
| R20 | "relabelings" as edits that leave the answer as at the baseline (D6.9) | I26 | FC21 (a) holds, close to by definition | with I26's first other choice (an automorphism, which may rename the answer's values), a candidate meeting (A) can meet NC2 on a contract of relabelings, and FC21 (a) fails. Reasoned, not computed | no |
| R21 | Output read at the identity edit (D2.3) | I05 | FC02 (b): output does not depend on A (true by construction of I05) | at every edit that does not replace j (I05's first other choice), output can depend on A | no |
| R22 | Two-layer encoding: window, occlusion run, things that pass through each other (E9) | I68, I100; not the passing through (H17) | FC102 (b) second half: fails for one and two things | with things that exclude one another, the two-thing part ("can fail with no occlusion at all") may not arise. Not computed | partly |
| R23 | No "at rest" clause (D11.4) | no (H11) | FC75 Look: the route counts as active | L375 excludes it | Look only |
| R24 | Contrast when the baseline answer is ⊥ (D6.4) | I22 | a determined answer at x against ⊥ at the baseline is no contrast | under L315's reading of "differ" it is one, and NC2 (so Acc) can change for such candidates. Which random results would move was not computed | no |
| R25 | "one counterpart" (L315) | I36 | FC44 holds | the other reading gives a witness; the text excludes it (T07) | yes |

## 4. The definitions, one by one

Verdicts:
- **as the text**: the definition says what the quoted lines say.
- **+Inn**: as the text with the registered inventions named.
- **adds (Hnn)** or **less (Hnn)**: see §1.
- **fixed (Tnn)**: a registered invention the text fixes; see §2.

| Def | Lines | Verdict | Note |
|---|---|---|---|
| D0.1 | L31, L522 | as the text | |
| D0.2 | — | +I20, I21, I27, I29, I33, I34, I39, I46, I47, I55, I56, I58, I59; adds (H13) | Occurs has no number; Contrib (H14), Attempt and Org_ℓ(h) (H19, H20) are not listed |
| D1.1 | L88, L91, L94 | +I01, I02, I03 | |
| D1.2 | L100 | as the text | |
| D1.3 | L103, L339 | +I03 | "deleted" defined as having the full relation; the text gives only one direction |
| D1.4 | L189, L233 | +I14 | |
| D2.1 | L103, L119 | +I04, I80; adds (H01, H03) | the identity case: T13 |
| D2.2 | L109 | as the text, given D2.1 | |
| D2.3 | L109 | +I05 | "across \(B\)" names no edit, which leans to I05 |
| D2.4 | L109, L127 | +I06 | both readings carried |
| D2.5 | L109 | adds (H04) | |
| D3.1 | L138, L141, L147 | +I20 | δ_D added to the tuple |
| D3.2 | L141, L144, L253 | +I20, I21 | |
| D3.3 | L151 | +I72 | |
| D3.4 | L155 | adds (H20) | "as for transports" |
| D3.5 | L159, L257 | +I27 | the text's word is "edit" (§2b) |
| D3.6 | L161, L367 | +I76 | |
| D3.7 | L151 | +I73 | |
| D4.1 | L116 | as the text | |
| D4.2 | L119 | +I10, I11 | |
| D4.3 | L119 | +I12 | σ and τ[C] fixed by L556 (T04) |
| D4.4 | L119, L556 | +I13 | fixed (T05) |
| D4.5 | L123–L125 | +I09 | |
| D4.6 | L123–L125, L347 | +I04, I06, I07, I08, I102; adds (H02, H01) | |
| D5.1 | L186, L189 | +I14, I16, I17 | κ is content the text does not have (R04) |
| D5.2 | L233 | +I14 | |
| D5.3 | L231 | +I15, I20 | I15 fixed (T01) |
| D5.4 | L236 | as the text | |
| D5.5 | L242 | +I18 | |
| D5.6 | L250 | +I21 | |
| D5.7 | L189, L245, L247 | +I49, I18 | "faithful" is narrow by L189 |
| D6.1 | L255 | as the text | |
| D6.2 | L255 | +I23 | |
| D6.3 | L255 | +I24, I28 (the program adds I79, I82, I83) | |
| D6.4 | L255 | +I21, I22; see H10 | |
| D6.5 | L255 | +I25 | L273 ("fails non-circular dependence") leans to the conjunction (R07) |
| D6.6 | L257 | +I27 | |
| D6.7 | L262 | as the text | |
| D6.8 | L231 | as the text | F2 sits under the heading "Component fidelity" (L233–L243) |
| D6.9 | L257 | +I26 | |
| D6.10 | L269 | +I32 | |
| D7.1 | L287, L231 | +I29 | §2b |
| D7.2, D7.3 | L290, L296 | as the text | |
| D7.4 | L302 | as the text | E_v's transport and commitments left open: no choice is made, so (D) cannot be evaluated as written |
| D7.5 | L305 | as the text | criticality of one commitment read as that of the singleton, which L299 gives ("no singleton in it is") |
| D7.6 | L313 | as the text | |
| D8.1 | L315 | +I19 | R over every relation on the footprints is the text's ("it does not turn on what any physics admits") |
| D8.2 | L315 | as the text; see H10 | |
| D8.3 | L315 | +I33 | symmetry fixed (T09) |
| D8.4, D8.5 | L315 | +I34 | the second disjunct of D8.5 is the text's words |
| D8.6 | L315 | +I35 | fixed (T06) |
| D9.1, D9.2 | L397 | +I38, I39 | |
| D9.3 | L387 | +I40 | |
| D9.4 | L393 | +I40, I41 | I40 against the words (§2b) |
| D9.5 | L393 | +I42 | |
| D9.6 | L390, L397 | as the text (with I40) | |
| D9.7 | L397 | +I38, I39 | |
| D9.8 | L315, L397 | as the text | |
| D9.9 | L395 | +I43 | less: (K3) is stated without conditions; D9.9 (i) adds "the conditional … is live for j and j admits modus tollens" |
| D9.10 | L377, L380 | adds (H12) | tagged [I76], which fills in for L161 only |
| D9.11 | L385 | +I47 | |
| D10.1, D10.2 | L317 | as the text | |
| D10.3 | L317 | adds (H20) | the argument's shape |
| D10.4 | L317 | +I37 | fixed (T08) |
| D10.5, D10.6 | L315, L317 | as the text | |
| D11.1 | L169 | +I45 | |
| D11.2 | L169 | +I48 | |
| D11.3 | L375 | +I44; adds (H19) | |
| D11.4 | L375 | +I46; less (H11) | |
| D11.5 | L217 | adds (H13) | |
| D12.1 | L193, L195 | +I52; less (H05); adds (H09) | |
| D12.2 | L197 | as the text, with "episode" per D13.8 (H06) | |
| D12.3 | L199 | +I53 | fixed (T10); drops "The transport is entered into the model by its author", read as description |
| D12.4 | L211, L405 | +I54 | |
| D12.5 | L205, L208 | +I48 | |
| D12.6 | L175, L177 | as the text | typing only |
| D12.7 | L219–L221 | +I50, I51; adds (H07) | |
| D12.8 | L225 | adds (H08) | |
| D12.9 | L572 | +I71 | |
| D13.1, D13.2 | L403, L415 | +I55 | |
| D13.3 | L405 | +I56 | |
| D13.4 | L413 | +I48 | |
| D13.5 | L416 | as the text | |
| D13.6 | L419, L422 | adds (H20) | Attempt read through Θ |
| D13.7 | L427 | adds (H14) | |
| D13.8 | L429 | adds (H06, H15) | |
| D14.1 | L441 | +I57 | the right side r(ξ') is the text's; the left side r(ξ) is I57's |
| D14.2 | L438 | as the text | |
| D14.3 | L441 | +I57 | |
| D14.4 | L441 | +I58 | |
| D14.5 | L443 | +I59 | |
| D14.6 | L453 | +I60 | |
| D14.7 | L447–L449 | as the text (+I44) | |
| D14.8 | L455 | as the text | typed only; 𝒩 used by no definition |
| D15.1–D15.3 | L461, L466, L469, L471 | +I61 | |
| D15.4 | L473 | as the text | |
| D15.5 | L475 | as the text; adds (H20) | ownership of a protocol |
| D15.6 | L477 | as the text | |
| D15.7 | L479 | +I62 | largely fixed (T14) |
| D15.8 | L481 | as L481; adds (H09) | D12.1 does not use the equality; "parts(t)" is undefined |
| D16.1 | L487 | adds (H16) | |
| D16.2 | L492 | +I74 | |
| D16.3 | L495 | as the text | "non-question-begging" left undefined (NF11) |
| D16.4 | L497–L506 | +I75 | |
| D16.5 | L528 | as the text; adds (H20) | |
| D18.1 | L526 | as the text's order, plus D0.2's sinks | |
| D18.2 | L612 | +I70 | |
| E1 | L325 | +I65, I92 | the identification contract: R09 and §2b |
| E2 | L329 | +I63, I64 | I63 fixed (T11) |
| E3, E4 | L331, L335 | as the text | |
| E5 | L339 | +I03 | |
| E6 | L343 | +I66, I99 | GF(3) for "real" is registered |
| E7 | L353, L358, L363 | as the text | |
| E8 | L590 | +I67 | |
| E9 | L620 | +I68, I69, I100; adds (H17) | |

## 5. The claims, one by one

Verdicts:
- **as quoted**: the formal claim says what the quoted sentence says, or is a consequence of the formal core that it names as such.
- **more** or **less**: than the quoted sentence.
- **rests on**: a reading or invention the other reading of which changes the result (§3).

| Claim | Verdict | Note |
|---|---|---|
| FC01 | as quoted | its Look is I21's merging of "none" and "several" into ⊥ |
| FC02 | as quoted; rests on H04, I05 (R21), I80 (T13) | (c) is a finding on L325: H and θ are outputs of c_L too |
| FC03, FC04 | as quoted | |
| FC05 | as quoted; the counterexample rests on I93 (ii), which "stay" excludes (T02) | |
| FC06 | as quoted; rests on H01 | under composites-as-settings, a composite setting m alters a reader |
| FC07 | as quoted (R01) | the C2* part rests on H01 (R13) |
| FC08 | as quoted | a finding on L127: its second clause is about solutions |
| FC09–FC14 | as quoted | FC09 also found the rule and measurement families overlapping |
| FC15, FC16 | as quoted | |
| FC17 | as quoted (+I12) | |
| FC18 | as quoted; the counterexample rests on I94 (T03) and κ (R04) | |
| FC19 | less | "prevents" is formalized as independence of (F1) and (F2) |
| FC20 | a claim of the formalizer's (no sentence of the text claims it) | the counterexample adds a condition the claim lacks (κ injective) |
| FC21 | less | (a) adds the hypothesis (A), which L257 does not have; (b) is a witness that L257's "admits no candidate that meets non-circular dependence" fails as written for candidates failing (A); (a) rests on I26 (R20) |
| FC22 | as quoted | |
| FC23 | as quoted; (b) as stated had a hole (a background that empties Sol_E) | the finding (NC2 does not exclude the lookup) stands with a satisfiable background; rests on I24, I25 (R07) |
| FC24 | as quoted | |
| FC25 | as quoted | (a)'s reported witness is a no-op setting (R14); a non-degenerate witness exists, so L269's "under any contract containing one" still fails as written; (b)'s counterexample is an edge case of I14's Sol_N (R19) |
| FC26 | as quoted | the Look rests on I24's quantifier (R08) |
| FC27 | as quoted | |
| FC28 | rests on I65 (R09) | the status "HOLDS" is under the reading against the text's word "edits" |
| FC29, FC30 | as quoted | |
| FC31, FC32 | not tested | |
| FC33 | as quoted | |
| FC34 | as quoted (both readings, R10) | |
| FC35 | not tested | |
| FC36–FC43 | as quoted | FC40 (c) and FC41 (c) are derived steps the text leaves unsaid, as the claims say |
| FC44 | as quoted; the other reading is excluded by L562 (T07) | |
| FC45–FC47 | as quoted | FC47 (b) uses D10.3's argument shape (H20) |
| FC48 | rests on H10 (R06) | |
| FC49, FC50 | as quoted | |
| FC51 | more | (a) lists "τ' fails the homomorphism clause on edits new in C'", which cannot occur: under D5.5 and I18, Hom is a condition on τ as a whole and does not depend on C |
| FC52–FC62 | as quoted | FC53 (b) and FC60 are findings on L315 and L331 |
| FC63 | less, and rests on I81, I99 (R17, R18) | (c) lists NC2 but not NC1, while L343 says "Non-circular dependence is met" (the model computed NC1 true in (c-ii)); the one model where a sentence of the text fails under a reading it leaves open (§6) |
| FC64–FC69 | as quoted | FC69 rests on I40 (R15) |
| FC70 | as quoted | the finding holds under I40 and under its other choice: with "any step", a premise live through another step still stays live when withdrawn |
| FC71–FC74 | as quoted | FC74 rests on H12 |
| FC75 | as quoted for (a)–(c) | the Look rests on H11 |
| FC76 | as quoted; the ¬Bearing half rests on H12 | |
| FC77 | the formalizer's own statement ("every transport") | refined by I18 (R16); rests on H09 |
| FC78 | as quoted; rests on H05, H06, H09 | |
| FC79 | as quoted | |
| FC80 | less | (a) says that two survivors differing at an unseen pair are not separated by survival, which is true by definition. L574's step "that transport survives on \(H\)" is not tested. Under I71 it holds only when (τ(a), σ(b)) is not also the image of a pair of H: altering E's relation there alters fidelity at that pair of H. Neither the claim nor I71 records this condition |
| FC81 | as quoted; (d) rests on H05 | (a)–(c) by construction; see H07 on "∉ H" |
| FC82, FC83 | as quoted; rest on H05 and H08 | the selection response modelled has no violation and no μ step |
| FC84 | more | the first sentence (Origin ⇒ Build) is by construction. The second, "Sel's history holds no represented target (L195)", says what L195 does not say and D12.1 does not encode. FC78's model is a Sel history with a represented codomain. The sentence is L201's and L411's content (H05) |
| FC85–FC88 | as quoted | FC86's Look holds whatever I57 does with r(ξ) on the left |
| FC89, FC90 | not tested | |
| FC91–FC93 | as quoted | |
| FC94 | not tested | |
| FC95–FC97 | as quoted | FC96 (ii) keeps I14's caveat |
| FC98 | not tested | |
| FC99 | as quoted | the witness is trivial: τ sends an edit of C' to an edit of E that does not match it |
| FC100 | as quoted for (E) | |
| FC101 | as quoted; rests on H18 | the status would not change with full-relation deletions (reasoned) |
| FC102 | more | (b) reads "recent" as a window w (I68) and adds a parametric escape the text does not claim; the counterexample is to that gloss. For two things it fits L626's "structural, not parametric"; the no-occlusion failure rests on H17 (R22) |
| FC103 | as quoted for (d) | |
| FC104–FC110 | as quoted (not tested or syntactic) | |

## 6. What the twelve counterexamples are counterexamples to

| Counterexample | To what | What it rests on |
|---|---|---|
| FC05 | L119 under reading (ii) | I93 (ii), which the text's "stay equal" excludes (T02) |
| FC18 | L558 under I94 with value maps | I94, excluded by L556 (T03); κ (R04) |
| FC20 | the formal claim's own statement | κ may merge values: the text lets π: X_D → X_E merge values (L189) |
| FC23 (b) | the claim's wording (a background that empties Sol_E) | the finding about NC2 and the lookup stands |
| FC25 (b) | the claim's E_enc, when a port lies in no footprint | I14's Sol_N over footprints (R19) |
| FC63 (c-i) | L343, "The full Leibniz expansion with skewness substituted meets (F1) and (F2)" | I81, I99: which relation the sum component carries, which the text leaves open (R17) |
| FC77 | the formalizer's "every transport" | I18 (R16), I52, H09 |
| FC78 | L193's "exactly one", through D12.1 | H05 (with H06, H09); gone with L201 and L411 [computed here] |
| FC81 (d) | L223's "the failure is not surprise", through D12.1 | as FC78 |
| FC82 | L225's two responses, through D12.1 | as FC78, and H08 |
| FC83 | L225's "Only the second can be originative", through D12.1 | as FC78, and H08 |
| FC102 (b) | the formalizer's gloss that a long enough window extrapolates | I68, I100, H17; for two things it fits L626 |

**Results reported as holding that bear on the text's sentences** (each under the inventions it names):
- **FC21 (b)** (L257, "admits no candidate"): a candidate meeting NC2 on a contract of relabelings exists when it does not meet (A).
- **FC25 (a)** (L269, "under any contract containing one"): a setting edit of a port the table's ports do not depend on leaves the table faithful.
- **FC70** (L393): withdrawing a premise that is also the conclusion of a usable step leaves the step usable.
- **FC08** (L127): the gloss says more than L124's signature.
- **FC07** (L123, L127): on the pole contract that sets L, the forward shadow component is a measurement of H and θ under R-i.
- **FC23** (L273): NC2 alone does not exclude a lookup.
- **FC34** (L151, wide reading): a candidate can meet (E) on two different questions about one target.
- **FC60** (L331): the circularity named there is not one (E) can register.

## Appendix · The three computations of this check

Each was run from a scratchpad folder with `PYTHONDONTWRITEBYTECODE=1 python3 <file>`. None writes a file, and `model/` was not changed.

**A. FC48 under L255's reading of "differ" (R06, H10).**

```python
import sys; sys.dont_write_bytecode = True
sys.path.insert(0, "/home/user/ThreadSmith/Semantics/results/S104 Round 2 - maths")
from model.core import Org, Question, PortQuery, Candidate, Translation, ONE, BOT, conflict, meet_table
D = Org("D", ["p0"], {"p0": (0, 1)}, ["c0"], {"c0": ("p0",)}, ["b0"], [ONE], lambda a2, a1: None, lambda j, a, b: {(0,)})
p = Question(D, [(ONE, "b0")], "b0", PortQuery(), "p0")
E1 = Org("E1", ["p0"], {"p0": (0, 1)}, ["k"], {"k": ("p0",)}, ["b0"], [ONE], lambda a2, a1: None, lambda j, a, b: {(0,)})
E2 = Org("E2", ["p0", "p1"], {"p0": (0, 1), "p1": (0, 1)}, ["k", "bg"], {"k": ("p0",), "bg": ("p1",)}, ["b0"], [ONE],
         lambda a2, a1: None, lambda j, a, b: {(0,)} if j == "k" else set())
def cand(E):
    lam = {"k": (frozenset(["c0"]), {"p0": Translation(("p0",))})}
    if "bg" in E.comps: lam["bg"] = (frozenset(["c0"]), {"p1": Translation(("p0",))})
    return Candidate(E, p, {v: Translation(("p0",)) for v in E.ports}, {ONE: ONE}, {"b0": "b0"}, lam, ["k"], "p0")
c1, c2 = cand(E1), cand(E2)
y1, y2 = c1.ans_E(ONE, "b0"), c2.ans_E(ONE, "b0")
rows = meet_table(c1, c2, ONE, "b0")
m1, m2, both = any(r[0] for r in rows), any(r[1] for r in rows), any(r[0] and r[1] for r in rows)
print(y1, y2, conflict(c1, c2, ONE, "b0"), (y1 is not BOT and y2 is not BOT and y1 != y2) or (m1 and m2 and not both))
```

Output: `0 ⊥ True False`. Under D8.2 the pair (1, b0) ∈ C is a conflict pair. Under L255's reading it is not, and the answers there differ.

**B. The provenance counterexamples with L201 and L411 read into Sel (R11, H05).**

```python
import sys; sys.dont_write_bytecode = True
sys.path.insert(0, "/home/user/ThreadSmith/Semantics/results/S104 Round 2 - maths")
import model.claims_b as cb
def sel_l201(c, H, h): return cb.sel(c, H, h) and not any(x in ("t", "cod") for (_, x) in h.rep)
p, c, H, h = cb.prov_counterexample()
x = [a for a in p.C if a != (cb.ONE, "b1_45")][0]
print(cb.sel(c, H, h), cb.con(h), cb.sel(c, H + [x], h))   # D12.1 as written
print(sel_l201(c, H, h), cb.con(h), sel_l201(c, H + [x], h))  # with L201 and L411
```

Output: `True True True`, then `False True False`. Sel and Con no longer hold together on FC78's history, the selection response of FC82 and FC83 no longer holds, and FC81 (d)'s transport is no longer surprised.

**C. The pole's families on C2* when a composite of settings sets each port it sets (R13, H01).**

`sets_through` of `model/core.py` is replaced in memory for this run (the file is not changed) by the following rule. j's relation is a slice on v; j is altered at some boundary (which also puts I80's identity case aside); and every other component the edit alters is itself replaced by a slice. The families are then computed with `Roles` on `pole()` and `pole_contracts()` from `model/claims_a.py`.

| Contract | D2.1 as written | Composites set each port |
|---|---|---|
| C2, R-i | causal c_H, c_θ; measurement (c_L, H), (c_L, θ) | the same |
| C2, R-ii | causal c_H, c_L, c_θ | the same |
| C2*, R-i | no causal component; measurement (c_L, H), (c_L, θ); rule c_H, c_L, c_θ | no family |
| C2*, R-ii | no causal component; measurement (c_L, H), (c_L, θ); rule c_H, c_L, c_θ | causal c_H, c_L, c_θ |

*Written 27 September 2026. Not committed. The text under review still has md5 f31ebb1f050783f1a84f6136cec20fcd.*
