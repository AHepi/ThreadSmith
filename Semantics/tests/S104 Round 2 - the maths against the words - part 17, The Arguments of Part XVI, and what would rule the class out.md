# The maths against the words, part 17 of 17: The Arguments of Part XVI, and what would rule the class out

## 1. What you are asked to do

**The text** is a theory of explanation: a formal semantics of what an explanation is and of explanatory creativity, 632 lines, which calls itself "the semantics". Its owner took the decisions in section 2, and asked for "exploring the math a bit more" since "words are vague", adding: "if implementation forces invention, that needs to be recorded" (S36).

**The maths.** The text's definitions were written as mathematics beside the sentences they formalize (D0.1–D18.2; its worked cases encoded as E1–E9). The claims these let one state (FC01–FC110) were each put to a program that searched small finite models for a counterexample. Every choice the maths or the program made that the text does not fix was recorded as an **invention** (I01–I102), with the other choices that were possible. Two checks followed: one re-ran every counterexample and worked it by hand; the other read the maths against the text. They found further choices no entry records (U1–U6 and H01–H20). **Nothing invented is the text's own content.** A counterexample that rests on an invention tells against that way of writing the text, and against the text only where the text fixes what the invention fills in.

**This part** covers the Arguments of Part XVI of the text (L550–L632), Part XV (L532–L548) and the dependence order (L526): the definitions in section 3; 8 claims (FC97, FC98, FC99, FC100, FC101, FC102, FC103, FC109) with their results in section 4; the inventions they rest on in section 5 (4 in full); the unrecorded choices in section 6; sentences the maths could not write in section 7; round-1 matters and changes in section 8. The whole is put to readers in 17 parts, each read on its own.

**Your task, in one line:** say where the maths and the words part company and which should stand; whether each counterexample tells against the text or only against an invention, and what change to the text removes it; whether the text settles each invention, and if not what it should say; and try by hand to break the claims that held (section 9; the report, section 10). Try as hard as you can, against the texts given here alone. The maths is itself a conjecture about how the text can be written; so is the text.

**The search.** Every port had a finite domain; the organizations searched had at most 3 ports of 2 or 3 values, 3 or 4 components, 2 boundaries and about 12 edits, in two generated families (I77, I78), tried smallest first. Statuses: *holds on all models tried* (and nothing beyond them); *counterexample found*; *witness found* or *no witness found* (for a claim that something exists); *computed: as claimed* or *not as claimed* (on an encoding of a worked case); *holds by construction* (so written in the program, not searched); *look* (a first reading, written before the search, of where a counterexample might lie, then computed); *not tested*, with the reason. The physical module was not computed: where a claim needs histories or provenance, they were set by hand (I90).

**Who is who; citing.** "The owner" is the theory's owner; "Claude" is the drafters of the text and of the maths. Line numbers are those of the whole text, title as line 1. `> Lnnn | …` quotes line nnn exactly as it stands, formulas in the text's markup; " … " joins fragments of one line. The maths writes in its own notation. Quote the text exactly, with line numbers; where you rely on a line not given here, say so.

## 2. The owner's words

The theory's owner took the decisions below, in this order; the task in section 9 is set against them. Each is quoted from the project's record of decisions. Words inside quotation marks are the owner's, word for word, typos included, except where the connecting words say that a quoted phrase is Claude's (in S26 and S28). The few connecting words outside the quotation marks are the recorder's; where the record names internal files or logs there, a plain description stands in their place. The record's own reading of each decision is not given: the owner's words decide, and where section 9 is worded differently from them, the owner's words decide there too, and you should say so. Decisions on how the work is run are left out. In these words "Claude" is the drafters of the text and of the maths; "your agents" and "your explanation" in S27 are addressed to them.

**S20** (24 and 25 September 2026). On whether the theory should grade explanations: "Well that depends entirely on how error correction is handled." Then: "A record is redundant. Once the explanation is rescued, the mistake shouldn't be able to creep back in. Good explanations make bad ones harder to fit by definition. So this is the next bit to check. But understand why before sending off workers" Then, on the set of versions: "That assumes that the set even matters or that the creative agent can even list them. As far as I'm aware, that's not possible, even in principle. A variation is a competitor. Whether anyone can list all variations that still fit is beside the point. If two discovered variations fit, that constitutes a problem. Please tell me if I'm misunderstanding something here. Because I think I am." (24 September 2026) And: "Ok. As long as this correct is logged somewhere, I won't have to correct it again" (25 September 2026)

**S21** (25 September 2026). Answering choices the drafters had put to the owner: "In the case of non scientific theories: candidate explanations attempt to solve a problem. Both may appear to solve it. But choosing one, for whatever reason, means that the person doing the choosing sees no option but to choose the one that isn't ruled out by its best argument (note: “sees no option”, not “has no option”). Both may survive, which means no resolution has been reached. Therefore further investigation is required the conflict and potentially solve the problem. The problem may, for whatever reason, be ill posed. Therefore, whatever happens to the candidates is up to the person doing the choosing. Notice I never once claimed what must happen. Resolution is up to the person and the person's choice. If the person decides the problem is a low priority, then this whole process may be abandoned. If the person is told by its parents to “hurry up and clean your room”, this entire episode may never resolve, and fade into recesses of that person's history. Whatever happens is always the choice of the person. Choice is always important because there is no such thing as an infallible creative agent. Creative agents are always constrained in some way: not enough time, the crop needs harvesting, I need to recharge my electronic brain, whatever. They're all valid choices. Whether they're rational may or may not ever be opened and examined by the creative person/agent. The question of “does it need to match the problem”: yes, if resolution is the goal. But “matches the problem” is always tentative and may be wrong. The case for science is reality itself. It must match reality, but not by some fixed infallible metric. Creativity is a process that may or may not lead to a metric." and "I don't really understand the rest of the conflicts. But does the response above add anything?" (25 September 2026)

**S23** (25 September 2026). Next step, in three paragraphs: "Next step. Get rid of all words that imply verificationism and see if the semantics still holds. Forbidden words and phrases." "Fits, supports, supported, verifies, verified, corroborates, corroborated, proves, proved, disproves, disproved, reason to believe, reason to reject. In fact, anything belief related at all must be scrubbed. Better than, worse than, true, not true, more true, established, authority, foundation, foundational, derived, derived from. Anything that could imply some sort of foundational truth or authority. Anything that could be interpreted as needing verification or falsification in any absolute sense. Anything that is accepted is always tentatively, and mean anywhere that "accept" or "accepted" is used." "Also, argument is short hand for: reasons why this and not that. Not reasons for this and not that. An argument is merely something that can be strung together into a coherent structure to decide why this and not another." (25 September 2026)

**S25** (26 September 2026). Answering Claude's report that an earlier draft ties questions and conflict to physically admitted changes: "Oh dear. That's a pretty big hole. "Physically possible or impossible" has to do with instantiation and transformation of information and knowledge. It has nothing to do with explanation." (26 September 2026)

**S26** (26 September 2026). After Claude said that physical possibility had leaked into the core of the theory: "Well not strictly nothing. But" Then, quoting Claude's sentence "Physical possibility comes in only when something is instantiated or transformed": "This is correct. But can you please list 5 examples of how this translates from explanation to physical so I can tell if you understand correctly." (26 September 2026)

*What S27 answers.* Between S26 and S27 the drafters gave the owner the five examples asked for: holding an explanation in a carrier (ink, a brain, a file); copying or teaching it; testing between two rival explanations, where the test changes the thing explained; building from an explanation (a perpetual-motion machine, a bridge); and performing music. The examples are the drafters' words, not the owner's, and are not a decision. S27 is the owner's reply to them.

**S27** (26 September 2026). Answering Claude's five examples (decision S26), headed "Two important footnotes so your agents aren't led astray": "Explanations can contradict each other at the level of explanation without ever having to be tested against reality. For example, if your explanation inadvertently describes something with the exact same properties as a perpetual motion machine, you don't have to compare your explanation directly to the world. If it can be shown that your explanation implies perpetual motion, then that's a conflict. Why perpetual motion is impossible carries its own explanation. But the entirety of that explanation need not do. "perpetual motion is impossible" is enough to trigger a conflict. It is not enough for a creative agent to do anything about it though." "What's more, the creative agent need not contain the entirety of why perpetual motion is impossible. It could just be the agent accepted it as a given, without any thought whatsoever, and then uses it to identify flaws with their own explanations. Creative entities can do creative work without ever containing the entire contents of a explanation it uses to find errors. It need not. But that property alone is a costly gamble for all creative agents. If this weren't possible, then error correction could become impossibly costly to perform. Of course, nothing is stopping one from designing a system that must contain the entire contents of other explanations before they do the work of error correction. It's also a detail that exists outside the process." (26 September 2026)

**S28** (26 September 2026). Answering Claude's question whether the theory may keep that a candidate meets the requirements "settled by the world": "A theory is never settled. That's what "tentatively accepted" means. Unless you mean something else." Then, answering whether ruling out a rival by a claim taken as given is already doing something about it: "Also, yes. That "ruling out" is a choice that was made. Again, unless you mean something else." Then, after Claude explained that the thing explained is however it is and everything anyone accepts about it stays tentative: "1. That is correct." (26 September 2026)

**S33** (27 September 2026). After reading a study of what seven sentences of the text depend on, in three paragraphs: "Hmm. This makes me think that moving "hard to vary" outside the system was a critical error on my part.  Like a car without fuel, something needs to actually drive the changes that do occur." "My silly mistake was confusing "preferred" with "use". The agent need not be aware, at all, that they use a method. Preference never enters the integration of "hard to vary"." "So before doing anything, can you return a summary of all the different ways it has been defined and used historically, including now." (27 September 2026)

**S34** (27 September 2026). After decision S33: "I'm just a lowly human. As it happens, I'm using theories in the same way I stayed previously: taking some for granted to continuously rule available options. Even though I could probably unpack them again with enough work." Then, after reading a summary of every way hard to vary had been defined and used, in two paragraphs: "Hard to vary is not blind. Although variation may be blind, judging hard to vary is not." "I'm now realising hard to vary covers everything from logical contradictions to conflicts. That's hard. Because now I've got to figure out what it actually covers." Then, when Claude offered an agent to list every kind of ruling-out already in the theory: "No. Park it for now. Let's stick with the other mapping that took some time to develop. What would you recommend?" (27 September 2026)

**S36** (27 September 2026). During the reading of the first review round: "So what are all the checks doing? Don't stop. But maybe exploring the math a bit more might help instead of words. Since words are vague" Then, after Claude agreed and proposed a maths round: "Unless you disagree" Then, after Claude said it did not disagree, with three caveats: "Also, if implementation forces invention, that needs to be recorded." (27 September 2026)

## 3. The definitions, beside the sentences they formalize

The maths' own sections are printed whole where this part's claims live in them; single definitions from other sections follow, each with the sentences before it. Under **Vague**, the maths names what the text leaves open there.

Notation (from the maths' conventions). A condition holds or fails; ⊥ is the undetermined answer, not the value of a condition. P(X) is the set of subsets of X; ∏ the cartesian product; z|U restricts a valuation to the ports U; f[S] is the image of S; R* is the reflexive-transitive closure of a relation; ⇀ marks a partial map. D is a target, E a candidate's organization; a subscript or superscript names the organization where needed (A_E, B_E, J_E, L^E_k). A pair (a,b) is an edit a and a boundary b; x := (τ(a),σ(b)) and x0 := (1,σ(b0)). Definitions are numbered D§.n by the maths' sections (§1–§18), encodings of the text's worked cases E1–E9. **[Inn]** marks the place where an invention is used.

### §18 Dependence, invariance, and where the text was vaguest

> L526 | **Dependence order.** (O) and (Q) depend on nothing; nor do the declared indices and the declared inputs, which are stated, not defined.

**D18.1 The dependence graph.** Nodes: the symbols defined in §§1–16 (D-numbered). An edge from a definition to each symbol its right-hand side uses. Sinks allowed by the text (L526, L596): Θ with Org_ℓ, 𝒩, (O), (Q), the indices, the declared inputs of L522. The primitives of D0.2 are sinks the text does not list; FC98 asks of each whether it is a claim read through Θ. Of the two loops an earlier study read from the wording, K2 → Live → K2 closes below the step (D9.4, D9.6). The other, build → prov → rep, stays open here: L405's 'prepares a represented organization' asks for (R), (R) asks for Sel or Con, and Con asks for a construction trace, which is what Build's subhistory is. D13.3 hides the loop only by making Prepares a primitive [I56]; with 'represented' read through (R), Build, Con and Rep are defined together, as one fixed point, unless Con's trace is read without (R). The text names the risk at L526 ('A representation defined only by its own construction … has not supplied its place in the order'). FC98 tests both loops.

**D18.2 Structure-preserving bijections** **[I70]**. A bijection φ of ports, values, components, edits (a partial-monoid isomorphism), boundaries and occurrences (preserving ≺_h and Θ's interpretation), with Q, δ, Σ and every declared input carried along. Argument 8 (FC100) is the claim that (E), (G), (P) and (EX) are kept by every such φ.

**Where the text was vaguest, for this formalization.** Three places needed the most inventions, and each carries weight elsewhere:

1. **Roles and families in Part II (L103, L109, L119, L123–L127).** The text speaks of 'the component assigning' a port and of 'observation edits', and supplies neither an assignment nor a way to read one off relational components; the two readings of L109's observation give different families on the pole's own contract (FC07), and L127's gloss adds a condition on solutions that (K) does not record (FC08). Inventions I04–I13.
2. **Non-circular dependence (L255, L257).** Its one fully formal sentence (NC2) does not exclude a lookup of the answer ('p because p' meets NC2 when the answer varies, FC23); the exclusion rests on NC1, whose 'unanalysed', 'at the declared grain' and 'structural' are defined nowhere, and on 'in the claimed way'. Inventions I21–I28.
3. **How one query and one contract apply across organizations (L141, L253, L250; L205, L413).** (A) applies the target's query to the candidate's organization, whose ports differ; (R) and ≡ ask a transport into a content to be faithful 'on c's contract', a contract on the codomain, which a transport's conditions quantify over on the domain. Every (A), (R), New, Origin and (EX) rests on the choice. Inventions I20, I48.

Next after these: the undefined primitives of Parts IX–XI (L375, L385, L403, L405, L453; I46, I47, I55, I56, I60), each read as a plain word by the round-1 checkers and each needing a primitive predicate here.

### Definitions from other sections that these claims use

**D0.1 The frame.** Every definition below is relative to a frame Φ: the imports, the declared indices and the declared inputs.

**D0.2 Primitives this formalization adds.** Beyond Φ, the formal core uses these symbols, which the text names or needs but neither defines nor lists among its imports, indices or declared inputs. Each is an invention, and FC98 asks of each whether it is a claim read through Θ or a primitive the text does not list: the designation δ of a query [I20]; the undetermined answer ⊥ [I21]; Excl(Σ) [I27]; the restriction operation [I29] (the text calls it declared, L287; L522 does not list it); Offered [I33]; Allow_χ and Applies [I34]; MadeFrom [I39]; the contrast set K of an active route [I46]; Rule, Rec, Chg of reason use [I47]; Integrated and Nontrivial [I55]; Prepares, BindingConstruction, TransferComposite [I56]; Aims* and the exposure record [I58]; O_ex's marking [I59]; Occurs (D11.5).

**E8 A contract as an organization** **[I67]**.

**E9 The two-layer episode** **[I68, I69]**.

## 4. The claims, with their search results

Each claim: its type, the inventions it uses, its sentences quoted, its formal statement, and its result, part by part; for a counterexample, what it shows and, where short, the model; then the second check's note, and every invention the result rests on (the claim's own and the program's).

### FC97 · Argument 5: a contract can be an organization and a content

*a result the text states.* Inventions it uses: I01, I48, I67.

> L588 | **Claim.** A contract \(C\), taken with its edits and its query, can be given the structure of an organization in the sense of (O), and can be the content \(c\) in (G).

> L590 | Give it ports (the edits and their boundaries), components (the closure conditions, each with the relation it imposes on its ports, as (O) requires), and admitted edits (add or remove a change; alter \(\mathcal Q\)).

**Formal.** Under I67, D_C (membership ports, a query port, closure components, setting edits) is an organization in the sense of (O): nonempty domains, footprints, a partial composition with identity, a relation for every (j,a,b). With a contract on D_C (I48), Deploy, Build, New and (G) take it as a content.

**Result: HOLDS ON ALL MODELS TRIED.**

- *a contract as an organization* (computation): **computed: as claimed**.
- *Deploy, Build, New and (G) take it as a content* (not tested): **not tested**.
  Why not: needs Θ (I90); the typing check above is what the model can do

**Rests on:** I01, I48, I67.

### FC98 · Argument 6 and the dependence order: acyclic, and ending where the text says

*a result the text states.* Inventions it uses: I20, I29, I33, I34, I39, I46, I47, I55, I56, I58, I59.

> L596 | **Claim.** Every predicate in Parts II–XIII is defined in terms of \(\Theta\) (including \(\operatorname{Org}_\ell\)) and, where invoked, \(\mathcal N\), together with the structural vocabulary of (O) and (Q), declared indices and declared inputs.

> L526 | The order has no cycle and no endless descent.

**Formal.** Graph: nodes the defined symbols of the formal core; an edge from a definition to each symbol it uses. Test (a) acyclicity (an earlier study read two loops from the wording: build–prov–rep, and K2–arg–livej, which FC69 closes under I40); (b) every sink is Θ (with Org_ℓ), 𝒩, (O), (Q), an index, or a declared input of L522. Symbols the formal core uses that are none of these on their face: Offered (I33), the restriction operation (I29), Integrated and Nontrivial (I55), Prepares, BindingConstruction, TransferComposite (I56), MadeFrom (I39), Applies (I34), Aims* (I58), O_ex (I59), the contrasts K (I46), Rule, Rec, Chg (I47), Occurs (§12), the designation δ (I20). For each: a claim read through Θ, or a primitive the text does not list?

**Result: NOT TESTED.**

- *the dependence graph* (not tested): **not tested**.
  Why not: a property of the definitions' dependence graph (D18.1), not of models

**Rests on:** I20, I29, I33, I34, I39, I46, I47, I55, I56, I58, I59.

### FC99 · Argument 7: an account on C can fail on C'

*a result the text states.* Inventions it uses: I65.

> L606 | and \(\mathcal E\) can meet (E) on \(C\) and fail it on \(C'\).

**Formal.** There are D, C, C', Q and ℰ with Acc on (D, C, …) and ¬Acc on (D, C', …); for example the pole's forward candidate with C1 and with C' adding an edit at which its τ gives an edit other than the one required of E.

**Result: HOLDS ON ALL MODELS TRIED.**

- *an account on C can fail on C'* (computation): **computed: as claimed**.

**Rests on:** I65, I92.

### FC100 · Argument 8: structure-preserving bijections keep (E), (G), (P), (EX)

*a result the text states.* Inventions it uses: I45, I70.

> L612 | Transporting all carriers, relations, transports, histories, contracts and declared inputs along structure-preserving bijections preserves (E), (G), (P), (EX).

> L612 | The result does not apply to coarsenings, changed boundaries, or lost event identities.

**Formal.** Under I70: Acc(φ·ℰ) = Acc(ℰ), and (G), (P), (EX) are kept, for every structure-preserving bijection φ of all the data, NC1's answer slot and the stated scope carried along. Testable on random isomorphic copies of finite models.

**Result: HOLDS ON ALL MODELS TRIED.**

- *(E) is kept by structure-preserving bijections* (for all): **holds on all models tried** (12,960 models).
- *(G), (P), (EX)* (not tested): **not tested**.
  Why not: need histories and Θ; not modelled beyond free predicates

**Rests on:** I45, I70, I77, I78, I81.

### FC101 · Argument 9: an input–output description does not fix an account

*a result the text states.* Inventions it uses: I29, I46.

> L616 | **Claim.** If \(M_0,M_1\) have the same input–output projection and differ on an account claim, no function of the projection agrees with the claim on both.

> L616 | Parallel and priority wiring are an instance.

**Formal.** (a) For any function f of the projection P: P(M0) = P(M1) ⇒ f(M0) = f(M1). (b) Construct M0 (two parallel routes to the output) and M1 (a priority route with a fallback) with equal input–output projections, a question whose contract holds edits deleting internal components, and a candidate that meets (E) for one and not the other.

**Result: HOLDS ON ALL MODELS TRIED.**

- *(a) a function of the projection* (by construction): **holds by construction**.
- *(b) equal input-output behaviour, different accounts* (computation): **computed: as claimed**.

**Rests on:** I29, I46, I78.

### FC102 · Argument 10: surprise, the structural failure of selection, and the constructed layer

*a result the text states.* Inventions it uses: I52, I68.

> L624 | \(S_0\), predicting from occupancy, predicts nothing there and is violated when the thing re-emerges at a cell consistent with its velocity. This is surprise (Argument 4).

> L626 | If the population's transports can only predict from occupancy, no member survives the extended history: the fidelity failure is structural, not parametric.

> L626 | Under (F1), \(t_1\) is faithful on the extended contract.

**Formal.** With I68: (a) t0 (window w) survives on H0 and is violated at the re-emergence pair, which lies in C0∖H0: Surp. (b) If the occlusion hides the thing for longer than w steps, every window-w occupancy predictor fails on the extended history (two histories with equal last-w occupancy and different re-emergence cells); if w is at least that long, an occupancy predictor can extrapolate and the failure is not structural. (c) t1 meets (F1) and (F2) on the extended contract, and each persistence component's signature read through t1 equals its thing's continuity subnetwork's (Argument 1).

**Result: COUNTEREXAMPLE FOUND.** Rests on I68 and I100 (six cells, occlusion of a run of interior cells, occupancy without identity as L620 has it, reflection at the ends); I52, the claim's own, plays no part in this computation.

- *(b) first half: the occlusion outlasts the window* (computation): **computed: as claimed**.
- *(b) second half: a window longer than the occlusion* (computation): **computed: not as claimed**.
  Searched: w > L ⇒ an occupancy predictor can extrapolate (the failure is not structural)
  one thing, failing (w, L) with L < w: [(1, 0), (2, 1), (3, 2)]; two things: [(1, 0), (2, 0), (2, 1), (3, 1), (3, 2)]. With two things the occupancy readings carry no identity: two things that cross and two that stay give the same readings, so a window-w predictor can fail with no occlusion at all (things, w, L and two starts: ((2, 1, 0), (((0, -1), (1, -1)), ((0, -1), (1, 0))))). With one thing the window needs two visible frames (w ≥ L + 2) for the velocity. FC102 (b)'s second half holds under neither count as stated, on I68's encoding with this program's occlusion (I100).
- *(a), (c)* (not tested): **not tested**.
  Why not: the two-layer organizations S0, S1 and their transports are not built in this round (E9 encodes only the object layer here)

**The second check.** Re-implemented from the register's description (six cells, reflection at the ends, cells 1..4 hidden for L steps, a window of w frames ending just before re-emergence): the same tables. One thing fails at (w, L) = (1,0), (2,1), (3,2), that is, at w = L + 1, and never once w ≥ L + 2: one visible frame gives position but not velocity. The printed two-thing example (w, L) = (1,0) fails for one thing too; (2,0) shows the missing identity (things at 0 and 1 standing still against things at 1 and 2 moving −1 give equal readings for two frames). See H17.

**Rests on:** I52, I68, I100.

### FC103 · Argument 10: the swap, two pairings, one account

*a result the text states.* Inventions it uses: I10, I14, I68, I69.

> L630 | On any contract containing it that admits each edit for both things alike, composing \(t_1\) with the exchange of the two things gives a second transport, which sends each persistence component to the other thing's continuity subnetwork.

> L630 | A claim that "component 1 is thing 1 and not thing 2" is a claim that some admitted change separates the two pairings of persistence components to things, and on this contract none does.

**Formal.** With I69: ψ an automorphism of P preserving C and the answers; t1' := t1∘ψ. (a) t1' meets (F1), (F2) and (A) on C exactly when t1 does. (b) The exchange of persistence components meets Argument 2 (ii)'s premise, so each k and its image are of one kind on C. (c) No pair of C separates the two pairings (FC51 (b)). (d) The swap edit leaves every occupancy answer unchanged.

**Result: HOLDS ON ALL MODELS TRIED.**

- *(d) the swap leaves occupancy answers unchanged* (computation): **computed: as claimed**.
- *(a)-(c) on E9* (not tested): **not tested**.
  Why not: E9's simulation layer is not built; the general forms are tested as FC33, FC96 (ii) and FC51 (b)

**Rests on:** I10, I14, I68, I69, I100.

### FC109 · 'A mathematical error': the named claims, each under its stated assumptions

*a sentence that stood unchanged through every revision; a result the text states.* Inventions it uses: I10, I12, I13, I14, I61, I63, I64, I71.

> L546 | **A mathematical error.** A counterexample to the finite monotone claim, (I2), (O1), (T2), (CT2), or Arguments 1–3 under their stated assumptions.

**Formal.** L546 names the finite monotone claim (FC37), (I2) (FC57), (O1) (FC61), (T2) (FC66), (CT2) (FC92) and Arguments 1–3 (FC17, FC96, FC80). Each is stated in the formal core with its assumptions. A counterexample that rests on an invention is a counterexample to the formalization, not to the text, and is reported with the invention it rests on.

**Result: HOLDS ON ALL MODELS TRIED.**

- *the named results, each under its assumptions* (computation): **computed: as claimed**.

**Rests on:** I10, I12, I13, I14, I61, I63, I64, I71.

## 5. The inventions these rest on

In full: each invention this part is the first of the parts to use. Then, for an invention given in full in another part that a counterexample here rests on, what was invented. Then the rest by title. I77 and I78, the bounds and families of the search, are described in section 1 and given in full in another part.

### I67 · A contract as an organization (Argument 5), encoded

Fills in for:

*(L590, quoted above.)*

**Invented.** One port m_(a,b) with domain {0,1} for each (a,b) in A × B (membership in C) and one port q whose domain is a declared set of queries; components: the baseline condition (m_(1,b0) = 1) and whatever closure conditions the question declares (for example m_(a1,b) ∧ m_(a2,b) → m_(a2·a1,b)); edits: set a membership port, set q, and composites.

**Other choices.** (a) ports for edits only, boundaries fixed. (b) no closure conditions beyond the baseline (the text names 'the closure conditions' without saying which).

**Used by:** claims of this part: FC97.

### I69 · 'Built alike': the exchange is an automorphism

Fills in for:

> L630 | The two things are built alike in \(P\), and their persistence components alike in \(S_1\)

**Invented.** The exchange ψ of the two things is a bijection of P's ports, components, edits and boundaries that preserves L, maps C onto C and leaves the query's answers unchanged; the same holds in S1 for the exchange of the persistence components.

**Other choices.** (a) an isomorphism between the two things' subnetworks only.

**Used by:** claims of this part: FC103.

### I70 · A structure-preserving bijection of all the data (Argument 8)

Fills in for:

*(L612, quoted above.)*

**Invented.** Bijections of ports, values, components, edits (a partial-monoid isomorphism), boundaries and occurrences (preserving ≺_h and the physical module's interpretation), with the query, its designation and every declared input carried along (Q^φ(φ·O, φa, φb) = Q(O,a,b)).

**Other choices.** (a) the physical module not transported (then (G) and (EX) need it to commute with the bijection).

**Used by:** claims of this part: FC100; 3 other claims.

### I100 · The two-layer episode's object layer: cells, occlusion and windows

Fills in for:

> L620 | Stipulate an object layer \(P\): a line of cells; two things, each with a position and a velocity; continuity components; admitted edits: displace a thing, set its velocity, occlude a cell, swap the two identities.

> L622 | \(S_0\) predicts occupancy from recent occupancy.

**Invented.** Six cells, velocities −1, 0, 1, reflection at the ends, ten steps; the occlusion hides the interior cells 1..4 from step 3 for L steps (a run of occluded cells, not one cell); readings are occupancy without identity (L620's sensory field); a window-w predictor is any function of the last w readings; one thing and two things are both tried.

**Other choices.** (a) a single occluded cell (the Look of FC102). (b) stopping at the ends. (c) readings that carry identity.

**Used by:** claims of this part: FC102, FC103. Counterexamples resting on it: FC102.

### I52 · Selection: the parameters witnessed in a physical history

**Invented** (given in full in another part). μ: 𝒯 → P(𝒯); the survival condition is Faithful_H (narrow). Sel(t;𝒯,μ,H) also requires a physical selection history h_sel in which the pairs of H occur and the members of 𝒯 are admitted by the physics (L481), and in which no occurrence represents (R) t, H or the survival condition. 'Member of the history' is read as an occurrence of h_sel, since the members of H are pairs and cannot represent.

### I68 · Argument 10's two-layer episode, encoded; 'recent occupancy'

**Invented** (given in full in another part). A line of N cells (N = 6 for tests), two things with position in {0..N−1} and velocity in {−1,0,1}, time steps 0..K; continuity: pos(t+1) = pos(t) + vel(t), with a stated rule at the ends (reflection); occluding cell c makes the occupancy reading of c empty; swap exchanges the two things' positions and velocities. S0 predicts occupancy at t+1 from the occupancy of the last w steps, with the window w shorter than the occlusion.

Named by title only (given in full in another part): I01, Composition of edits: a partial monoid with Kleene associativity; I04, Setting a port: a surgical edit, and the assigning component read off the edits; I10, Kinds: a footprint bijection between equal value domains, relations compared as sets; I12, Reading a candidate's component on C through the transport; τ[C]; I13, (K) extended from components to subnetworks; I14, Subnetworks, their solutions, and port translations with value maps; I20, How the fixed query is applied to a candidate's organization; I21, Undetermined answers: a value ⊥; I27, The stated scope: a declared statement over pairs; I28, The grain as a label on the organizations compared; I29, The restriction operation (E restricted to W): deletion; I33, The offer of one candidate in place of another: a primitive; I34, A claim χ as a set of allowed behaviours at a pair, and the premise that it speaks of the target; I39, 'Among its premises', read structurally; records made from a claim; I45, 'Event' is a set of occurrences; I46, Active route: 'represented input', 'operative result', 'applicable relations', 'declared contrasts'; I47, Reason use: 'structural map', 'role bindings', 'the same transition', 'operative deliberative rule'; I48, Contents, 'c's contract', and transports into a content; I55, Deploy: 'integrated into problem-directed activity', 'nontrivial use respect'; I56, Build: 'prepares', 'nontrivial binding construction', 'content-preserving transfer'; I58, 'Losses outside P': the aims considered, and 'exposed'; I59, Explanatory aims: L443 read as a characterization of O_ex; I60, ProducesVia: 'the relevant binding of c'; I61, Tasks and executions; 'complete' in F read as (CT1)'s completion; I63, A tag such as (I2) names the sentence before it; I64, Identification: 'attainable', and the admitted states in the linear case; I65, The pole and its shadow, encoded; I71, The 'value' of a transport at a pair (Argument 3); I77, Finite models and the bounds of the search; I78, Two families of generated organizations: surgical edits with override, and free edits; I81, Transports as port translations; computed ports; generated candidates; the transport space searched for ≡; I92, The pole in exact arithmetic, with its grids, baseline, contracts and fibre query.

## 6. Choices no register entry records

Found by the two checks. U-entries come from the check that re-ran the program; H-entries from the check that read the maths against the text, in its wording.

### H17 · Two things that may share a cell and pass through each other (E9, I68, I100; FC102)

*(L620, quoted above.)*

- **Added.** In `fc102` each thing moves as pos + vel with reflection, independently of the other. Two things may be in one cell, which reads as one occupied cell, and may cross. I68 and I100 record the cells, velocities, reflection, occlusion run and window. They do not record that the things do not interact.
- **Other choice.** Things that exclude one another (they cannot share a cell, and they bounce or stop).
- **Depends on it.** FC102 (b), second half, for two things: "a window-w predictor can fail with no occlusion at all". This finding also touches L622's stipulation "It is faithful on \(H_0\)": on this encoding it limits which histories H0 a window-w occupancy predictor can be faithful on.

### H18 · FC101's "edits deleting internal components" encoded as knock-outs (the model)

> L103 | A deleted component imposes the full relation on its ports.

- **Added.** FC101 (b) speaks of "a question whose contract holds edits deleting internal components". In `fc101` the edits del_r1 and del_r2 set m1 := 0 or m2 := 0; they do not impose the full relation. The register entries FC101 rests on (I29, I46, I78) do not cover this.
- **Depends on it.** FC101 (b). Reasoned through with the full relation, the parallel-route candidate still fails (F1) for M1's question at every pair, because the output components differ. So the status would not change.

### H20 · Smaller unregistered choices



- **D3.4.** A contract's selected and constructed provenance is read "as for transports (D12.1, D12.2)". L155 gives contracts their own wording ("the surviving member of a population under a variation-and-survival history").
- **D13.6.** Attempt is "a claim read through Θ". D0.2 does not list it; I90 names it only for the program.
- **D10.3.** The shape of the argument from a test ("R* at (a,b); Meets_ab(ℰ, R*) fails; Acc(ℰ) requires it") is written without a number. FC47 (b) uses it.
- **D15.5.** "owned (D13.7) at ξ" is applied to a protocol and a constructor attribute. D13.7 defines ownership for subhistories.
- **D16.5.** "M has an instance of (G) in a critical episode" stands for L528's "connected to a critical episode".

## 7. Sentences of this group the maths could not write

**NF01** (L17). Why it was not formalized: 'Is a non-explanation of its question' is not a predicate of the semantics, and 'these four cannot represent it' has no definition; only the logical shape can be written.

> L17 | A candidate would conflict with the conjecture if an argument not using these four ruled out the claim that it is a non-explanation of its question while these four cannot represent it

**NF02** (L536). Why it was not formalized: (Suff) relates Account to 'is an explanation of what its question asks', which the semantics leaves outside itself; formal shape only: ¬∃ℰ [Acc(ℰ) ∧ ¬Dec(t) ∧ some argument not using (E) is in X_j('ℰ is an explanation')].

> L536 | such that an argument not using (E) rules out the claim that it is an explanation of what its question asks.

**NF03** (L538). Why it was not formalized: The preservation clause is formal (∀C ∀t ¬Faithful_C(t)); 'rules out the claim that it is a non-explanation' is not.

> L538 | whose organization no transport can preserve under any contract on its target.

**NF04** (L540). Why it was not formalized: 'Explanatory work' is not defined; the formal part of (Elim) is FC18 and FC96.

> L540 | and the distinction does explanatory work.

**NF05** (L542). Why it was not formalized: 'Without loss' is not defined; nor is 'explanation operates on the object layer' in the third item.

> L542 | a method that rewrites every construction trace as a selection history without loss

**NF06** (L544). Why it was not formalized: 'Fails to capture' is not defined; the formal part of (QF) is Argument 5 (FC97).

> L544 | A case of finding a new question that treating a contract as a content, something that can be constructed, be new, and be the originative contribution of an episode, fails to capture

**NF15** (L45). Why it was not formalized: About other theories, not a claim of the semantics.

> L45 | Whether the combination is new is a question about the literature.

## 8. Round 1: matters noted and changes made

In the first review round, readers tried to vary sentences that had stood unchanged; the rulings changed four lines and recorded fourteen matters outside the sentences examined, left for later rounds.

None falls in this part.

## 9. The task

For the definitions, claims, counterexamples and inventions of this part:

**(a) Does each formal statement say what the sentence says?** For each definition in section 3 and each claim in section 4, compare the maths with the sentence or sentences it formalizes. Where they part company, say how, and which should stand, the maths or the words, with reasons why this and not that. Where the words should change, give the new wording.

**(b) Each counterexample** (a part marked *counterexample found* or *computed: not as claimed*, and a *look* that came out *not as expected*). Is it a counterexample to the text, or only to an invention or to the claim's own wording? If it tells against the text, give the exact change to the text that removes it; or say that it shows the text saying something it should not, and what.

**(c) Each invention given in full in section 5, and each unrecorded choice in section 6.** Does the text in fact settle it? If it does, quote the words that do. If not, give the exact wording the text should carry, or say why it should stay open. A proposal that writes an invention into the text says so, naming it.

**(d) Attack the claims that held.** A claim that held on every model tried held only on those small models, under the inventions named. Try by hand to find a counterexample, to the claim or to the sentence it formalizes: under another reading, without an invention, or beyond the bounds searched. Give the model in full and say what it rests on.

**(e) The round-1 matters and changes in section 8.** For each, does the text need a change? Give the exact wording, or the reasons why none.

**Rules.**

- Give the exact wording for every proposal: the whole sentence as it would stand, between fence lines, with the line it replaces.
- Do not list, count, grade or rank rivals, and do not argue from how many there are (decision S20).
- Say nothing about what must happen to a candidate (decision S21).
- An argument here means reasons why this and not that (decision S23). A wording you propose obeys decision S23 and keeps to what the owner's words in section 2 say.
- Physical possibility enters only where information or knowledge is instantiated or transformed, and as the content of a claim a candidate can conflict with (decisions S25–S27).
- Nothing is settled, and a ruling out by a claim taken as given is a choice the person made (decision S28); nothing you find settles anything.
- Do not propose anything about what hard to vary covers: the owner has parked that question (decisions S33, S34). The text's own 'easy to vary' (L317) is not that question.
- Where values are placed is the owner's question; do not propose to move them.
- Keep apart what the text forces and what a reader might take it to mean.

## 10. The report

- Five sections, (a) to (e), in that order. In each, one entry per item you have something to say about, headed by its id and line (for example `FC05 · L119`, `I93 · L119`, `H05`, `U4`, `matter 5 · L109`), with the exact wording of each proposal between fence lines. Items on which you have nothing to add are named together in one line at the end of the section.
- Keep the whole report under about 3,000 words. Depth where an item needs it counts for more than equal space for all.
- End the report with a line that reads exactly END OF REPORT.
