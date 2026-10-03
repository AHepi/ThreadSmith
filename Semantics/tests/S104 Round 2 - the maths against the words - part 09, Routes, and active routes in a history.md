# The maths against the words, part 9 of 17: Routes, and active routes in a history

## 1. What you are asked to do

**The text** is a theory of explanation: a formal semantics of what an explanation is and of explanatory creativity, 632 lines, which calls itself "the semantics". Its owner took the decisions in section 2, and asked for "exploring the math a bit more" since "words are vague", adding: "if implementation forces invention, that needs to be recorded" (S36).

**The maths.** The text's definitions were written as mathematics beside the sentences they formalize (D0.1–D18.2; its worked cases encoded as E1–E9). The claims these let one state (FC01–FC110) were each put to a program that searched small finite models for a counterexample. Every choice the maths or the program made that the text does not fix was recorded as an **invention** (I01–I102), with the other choices that were possible. Two checks followed: one re-ran every counterexample and worked it by hand; the other read the maths against the text. They found further choices no entry records (U1–U6 and H01–H20). **Nothing invented is the text's own content.** A counterexample that rests on an invention tells against that way of writing the text, and against the text only where the text fixes what the invention fills in.

**This part** covers routes, critical blocks and boundaries in Part VI of the text (L285–L313), and occurrences, histories and active routes (L167–L169, L375): the definitions in section 3; 8 claims (FC37, FC38, FC39, FC40, FC41, FC42, FC75, FC105) with their results in section 4; the inventions they rest on in section 5 (8 in full); the unrecorded choices in section 6; sentences the maths could not write in section 7; round-1 matters and changes in section 8. The whole is put to readers in 17 parts, each read on its own.

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

### §7 Routes: (S), (B), (D)

> L287 | Fix \(\mathcal E\) and a declared restriction operation. For \(W\subseteq\Gamma\), let \(E|W\) retain the commitments in \(W\) with the named background fixed; the commitments of \(E|W\) are \(W\).

> L231 | for \(E|W\), \(t'\) is \(t\) with \(\lambda\) restricted to the components of \(E|W\), and \(\Gamma'\) is \(W\).

**D7.1 Restriction.** E|W := E − (Γ ∖ W), with t restricted to W and commitments W **[I29]**; Acc(E|W, p) := Acc((E|W, p, t|W, W, δ_E)).

> L290 | \mathsf S_{E,p}=\{W\subseteq\Gamma:\operatorname{Account}(E|W,p)\}. \tag{S}

> L293 | No upward closure and no minimal member are assumed. For nonempty \(B\subseteq W\),

**D7.2 Routes (S).** S_{E,p} := {W ⊆ Γ : Acc(E|W, p)}. A route is a member of S_{E,p}.

> L296 | \operatorname{CriticalBlock}(B;W,p)\iff W\in\mathsf S_{E,p}\land W\setminus B\notin\mathsf S_{E,p}. \tag{B}

**D7.3 Critical block (B).** CB(B; W) :⟺ ∅ ≠ B ⊆ W ∧ W ∈ S ∧ W ∖ B ∉ S.

> L302 | \operatorname{Boundary}_{E,p}=\{(v,w)\in\mathcal V^2:\operatorname{Account}(E_v,p)\neq\operatorname{Account}(E_w,p)\}. \tag{D}

**D7.4 Boundary (D).** For a declared family 𝒱 of organization edits: Boundary := {(v,w) ∈ 𝒱² : Acc(E_v, p) ≠ Acc(E_w, p)}, with E_v's transport and commitments those the edit carries t and Γ to (L231; the text does not fix them further).

> L305 | then \(d\in\Gamma\) is critical for some route (**contributory**) exactly when \(d\in\bigcup\min\mathsf S\), and \(d\) is **globally indispensable**, \(\Gamma\setminus\{d\}\notin\mathsf S_{E,p}\)

**D7.5 Contributory; globally indispensable.** Contrib(d) :⟺ CB({d}; W) for some W ∈ S. Indisp(d) :⟺ Γ ∖ {d} ∉ S.

> L313 | A commitment \(d\) of a candidate that has a route does no work by itself in it when every route stays a route after \(d\) is added to it and after \(d\) is removed from it

**D7.6 No work by itself.** NoWork(d) :⟺ S ≠ ∅ and, for every W ∈ S, W ∪ {d} ∈ S and W ∖ {d} ∈ S.

The worked examples of L307–L311 are read as set systems S ⊆ P(Γ) **[I30]**; the infinitary example's routes are the sets with unbounded index sets **[I31]**.

### §11 Occurrences, events, contents, histories, active routes

> L169 | An **occurrence** is a physically located carrier. A **content** is an organization together with its contract-relative commitments. Occurrences are not identified by carrying the same words; contents are not identified by having the same outputs.

**D11.1 Occurrence; event.** Occ is a set of physically located carriers, interpreted by Θ. An event is a nonempty set of occurrences of a history **[I45]** (the text uses 'event' at L53, L55, L161, L397, L604 and L612 and defines it nowhere; FC105).

**D11.2 Content.** c = (E_c, C_c, Γ_c): an organization, a contract on it, and its commitments **[I48]**. Contents are compared by transports (D13.4), not by outputs.

> L375 | **Histories.** A history \(h\) is a set of occurrences with an acyclic causal precedence \(\prec_h\) (write \(\preceq_h\) for its reflexive closure) and a physical interpretation supplying process occurrences, their ports, and the connections actually instantiated.

**D11.3 History.** h = (O_h, ≺_h, I_h): O_h ⊆ Occ; ≺_h a strict partial order **[I44]**; I_h, supplied by Θ, gives process occurrences, their ports and the connections instantiated. Org_ℓ(h) is the organization Θ gives h at grain ℓ. A subhistory is a subset closed under the interpretation, with ≺ restricted.

> L375 | An **active route** is a connected subnetwork of actual occurrences joining a represented input to an operative result, whose components meet the applicable relations and which has nonconstant dependence on the represented distinction under the declared contrasts.

**D11.4 Active route** **[I46]**. For a result occurrence r: ActRoute_h(R; i, r, K) :⟺ R ⊆ O_h is connected by instantiated connections; i ∈ R is an input occurrence whose port carries a represented distinction; r ∈ R; every occurrence of R lies on a ≺_h-chain from i to r inside R; each occurrence of R meets the relation Org_ℓ(h) gives it; and for some pair (x, x') in the declared contrast set K of values of i's port, setting i's port to x and to x' in Org_ℓ(h) gives different values at r.

> L217 | For an edit–boundary pair \((a,b)\in C\) actually occurring:

**D11.5 Occurring pairs.** Occurs(a, b, ξ) is a primitive read through Θ: the pair occurs at ξ in the system's history.

**Vague.** 'Represented input', 'operative result', 'applicable relations' and 'the declared contrasts' (L375) are defined nowhere [I46]; whether a route that ran to completion and whose product persists is 'already at rest when the result occurred' is not fixed (FC75). 'Event' is used and not defined [I45]. 'c's contract' presupposes contents with contracts of their own [I48].

## 4. The claims, with their search results

Each claim: its type, the inventions it uses, its sentences quoted, its formal statement, and its result, part by part; for a counterexample, what it shows and, where short, the model; then the second check's note, and every invention the result rests on (the claim's own and the program's).

### FC37 · The finite monotone claim

*a result the text states.* Inventions it uses: none.

> L305 | **Finite monotone claim.** If \(\Gamma\) is finite, \(\mathsf S\) is upward closed, and \(\Gamma\in\mathsf S\), then \(d\in\Gamma\) is critical for some route (**contributory**) exactly when \(d\in\bigcup\min\mathsf S\), and \(d\) is **globally indispensable**, \(\Gamma\setminus\{d\}\notin\mathsf S_{E,p}\), exactly when \(d\in\bigcap\min\mathsf S\).

**Formal.** For every finite Γ and every upward-closed S ⊆ P(Γ) with Γ ∈ S: (∃W∈S: CB({d};W)) ⟺ d ∈ ∪min S, and Γ∖{d} ∉ S ⟺ d ∈ ∩min S. Testable on every upward-closed family over |Γ| ≤ 5.

**Result: HOLDS ON ALL MODELS TRIED.**

- *every upward-closed family, |Γ| ≤ 5* (for all): **holds on all models tried** (73,393 models).
- *S_{E,p} of random candidates* (for all): **holds on all models tried** (12,960 models).

**Rests on:** I77, I78, I81.

### FC38 · Redundant routes

*a result the text states.* Inventions it uses: I30.

> L307 | **Redundant routes.** \(\Gamma=\{a,b\}\), \(\mathsf S=\{\{a\},\{b\},\{a,b\}\}\): each is contributory, neither indispensable.

**Formal.** S = {{a},{b},{a,b}} is upward closed with min S = {{a},{b}}: a and b are contributory, neither is globally indispensable.

**Result: HOLDS ON ALL MODELS TRIED.**

- *redundant routes* (computation): **computed: as claimed**.

**Rests on:** I30.

### FC39 · Interference

*follows from the definitions as written.* Inventions it uses: I30.

> L309 | **Interference.** \(\Gamma=\{a,b\}\), \(\mathsf S=\{\{a\}\}\): the full candidate fails (E) although a subset meets it.

> L305 | an addition to \(\Gamma\) that stops a route being one is the interference case below, and there upward closure fails.

**Formal.** S = {{a}}: Γ ∉ S, {a} ∈ S, S is not upward closed, so the finite monotone claim's hypotheses fail; {a} is critical in {a}.

**Result: HOLDS ON ALL MODELS TRIED.**

- *interference* (computation): **computed: as claimed**.

**Rests on:** I30.

### FC40 · Infinitary routes: collective criticality, and the step the first sentence leaves unsaid

*a sentence that stood unchanged through every revision; a result the text states.* Inventions it uses: I30, I31. Bears on round-1 matter 8 (section 8): L311's first sentence; the second sentences of L311 and L273.

> L311 | every set of indices unbounded in \(\mathbb N\) determines \(x=0\); no minimal route, and no route of one commitment, exists.

> L311 | (B) records the collective contribution.

> L313 | When \(\Gamma\) is infinite, a block of such commitments can still be critical (Infinitary routes).

**Formal.** With I31: (a) S is upward closed, Γ ∈ S, min S = ∅, no member of S has one element. (b) For W ∈ S and nonempty B ⊆ W: CB(B;W) ⟺ the index set of W∖B is bounded; every critical block is infinite, and critical blocks exist (B = W). (c) Each d_n does no work by itself (L313): for W ∈ S, W ∪ {d_n} ∈ S and W ∖ {d_n} ∈ S. (d) So L313's last sentence has an instance here. Step (c) is the one L311's first sentence does not say in words.

**Result: HOLDS ON ALL MODELS TRIED.**

- *(a)-(c) on eventually periodic sets* (for all): **holds on all models tried** (80,000 models).

**Rests on:** I30, I31, I91.

### FC41 · Commitments that do no work, and why 'when Γ is infinite'

*a result the text states.* Inventions it uses: I29.

> L313 | A commitment \(d\) of a candidate that has a route does no work by itself in it when every route stays a route after \(d\) is added to it and after \(d\) is removed from it: a candidate carrying \(d\) then meets (E) exactly when it meets (E) without \(d\), and \(\{d\}\) is critical in no route (B).

**Formal.** NoWork(d) := S ≠ ∅ ∧ ∀W∈S (W∪{d} ∈ S ∧ W∖{d} ∈ S). Then (a) for every W ⊆ Γ: W∪{d} ∈ S ⟺ W∖{d} ∈ S; (b) {d} is critical in no route; (c) a finite block every member of which does no work by itself is critical in no route, so the 'when Γ is infinite' of L313's last sentence cannot be dropped.

**Result: HOLDS ON ALL MODELS TRIED.**

- *every family on |Γ| ≤ 4* (for all): **holds on all models tried** (65,812 models).

**Rests on:** I29, I77.

### FC42 · Criticality is relative to the route

*follows from the definitions as written.* Inventions it uses: I30.

> L299 | A block may be critical while no singleton in it is. Criticality is relative to the route \(W\) it is assessed in

> L299 | a commitment critical in one route need not be critical in the full candidate

**Formal.** (a) In Redundant routes, B = W = {a,b} is critical (W∖B = ∅ ∉ S) and neither singleton is. (b) There, a is critical in {a} and not in {a,b}.

**Result: HOLDS ON ALL MODELS TRIED.**

- *criticality relative to the route* (computation): **computed: as claimed**.

**Rests on:** I30.

### FC75 · Active routes: the excluded routes fail the definition's own clauses

*a sentence that stood unchanged through every revision; follows from the definitions as written.* Inventions it uses: I44, I46. Bears on round-1 matter 11 (section 8): the undefined phrases at L375 and L385.

> L375 | A route that started and did no work, or that was already at rest when the result occurred, is not active for that result; whether a route is active is read from the history, not from the result.

**Formal.** Under I46: (a) a route none of whose occurrences lies on a ≺_h-chain to r inside it fails the join clause; (b) a route whose value at r does not change when i's port is set across the declared contrasts fails the dependence clause; (c) activity is a function of (h, Org_ℓ(h), i, r, K), not of r's value alone.

**Look** (a first reading of where a counterexample might lie, written before the search). A route that ran to completion early, whose product persists and feeds r, is joined to r; whether it is 'already at rest when the result occurred' is not fixed by the definition.

**Result: HOLDS ON ALL MODELS TRIED.**

- *(a) a member on no chain to r* (computation): **computed: as claimed**.
- *(b) no dependence* (computation): **computed: as claimed**.
- *(c) a function of (h, Org, i, r, K)* (by construction): **holds by construction**.
- *a route at rest before the result* (look): **look: as expected**.
  Searched: the look: a route that ran early and whose product persists and feeds r is joined to r, and D11.4 counts it active
  i → m ran at step 1; m's product persists (an edge m → r across time, no process between) and r occurs at step 9 after 'late'. D11.4 (I46): yes (dependence on the contrast (0, 1)). L375 says a route 'already at rest when the result occurred, is not active'; D11.4 does not exclude this one.

**Rests on:** I44, I46, I95.

### FC105 · 'Event' is used and never defined; 'occurrence' is defined

*follows from the definitions as written.* Inventions it uses: I45. Bears on round-1 matter 2 (section 8): 'event', never defined, beside 'occurrence' (L169).

> L169 | An **occurrence** is a physically located carrier.

> L161 | Its formulation is still an event.

> L604 | **Claim.** An assessment event with contract \(C\) and an episode in which \(C\) is replaced by \(C'\) with a construction trace are both representable without contradiction.

**Formal.** Under I45 every use of 'event' (L53, L55, L161, L397, L604, L612) is read as a set of occurrences. Test whether any use needs more (for example 'lost event identities' at L612, an identity of an event beyond its occurrences). Argument 6 (L596) speaks of predicates; 'event' is a sort, defined nowhere.

**Result: NOT TESTED.**

- *'event'* (not tested): **not tested**.
  Why not: a reading of six lines' wording

**Rests on:** I45.

## 5. The inventions these rest on

In full: each invention this part is the first of the parts to use. Then, for an invention given in full in another part that a counterexample here rests on, what was invented. Then the rest by title. I77 and I78, the bounds and families of the search, are described in section 1 and given in full in another part.

### I29 · The restriction operation (E restricted to W): deletion

Fills in for:

*(L287, quoted above.)*

**Invented.** E|W is E with every component of Γ \ W deleted (full relation at every edit and boundary, as L103 gives for deletion), the background untouched, J_E and V_E unchanged; the transport is t with λ restricted to W; the commitments are W.

**Other choices.** (a) remove Γ \ W from J_E (their ports then free, or removed). (b) some other declared operation: the text names the operation as declared, and it is not among the declared inputs of L522.

**Used by:** claims of this part: FC41; 2 other claims.

### I30 · The worked examples of routes are set systems

Fills in for:

> L307 | **Redundant routes.** \(\Gamma=\{a,b\}\), \(\mathsf S=\{\{a\},\{b\},\{a,b\}\}\)

**Invented.** The examples of L305–L313 are read as statements about families S ⊆ P(Γ), not about a particular question and candidate; where a test needs a candidate that realizes one, the realization is a further invention, recorded with the test.

**Other choices.** (a) realize each example by a concrete target, question and candidate before reading it.

**Used by:** claims of this part: FC38, FC39, FC40, FC42.

### I31 · The routes of the infinitary example

Fills in for:

*(L311, quoted above.)*

**Invented.** The routes are exactly the sets W whose index set {n : d_n ∈ W} is unbounded; a bounded set leaves x anywhere in [-1/max, 1/max] and is not a route; the empty set is not a route. (The question is read as 'is x determined to be 0?'.)

**Other choices.** (a) the text does not say that bounded sets are not routes; another question (for example 'is |x| ≤ 1/N for a stated N?') gives another route family.

**Used by:** claims of this part: FC40.

### I44 · Causal precedence in a history is transitive

Fills in for:

> L375 | A history \(h\) is a set of occurrences with an acyclic causal precedence \(\prec_h\) (write \(\preceq_h\) for its reflexive closure)

**Invented.** ≺_h is a strict partial order (irreflexive and transitive), so ⪯_h is a partial order.

**Other choices.** (a) ≺_h any acyclic relation and ⪯_h its reflexive closure only (then ⪯_h need not be transitive). (b) ⪯_h the reflexive-transitive closure of an acyclic ≺_h.

**Used by:** claims of this part: FC75; 1 other claim.

### I45 · 'Event' is a set of occurrences

Fills in for:

*(L169, quoted above.)*

*(L161, quoted above.)*

> L397 | A record leaf is a reference to an event with an interpreted claim.

**Invented.** An event is a nonempty set of occurrences of a history; a record leaf refers to one; an assessment and a formulation are events. 'Event' adds no sort beyond occurrences.

**Other choices.** (a) events as a separate primitive sort. (b) events as occurrences of edit–boundary pairs only.

**Used by:** claims of this part: FC105; 2 other claims.

### I46 · Active route: 'represented input', 'operative result', 'applicable relations', 'declared contrasts'

Fills in for:

*(L375, quoted above.)*

**Invented.** Given the organization Org_ℓ(h) that the physical module assigns to the history h: an active route for a result occurrence r is a set R of occurrences of h, connected by the instantiated connections, containing an input occurrence i whose port carries a represented distinction and the result occurrence r (the 'operative result' is a designated result occurrence); every occurrence of R lies on a ≺_h-chain from i to r inside R; each occurrence of R meets the relation Org_ℓ(h) gives it ('the applicable relations'); and for a declared set K of pairs of values of i's port, setting i's port to the two values of some pair in K gives different values at r in Org_ℓ(h).

**Other choices.** (a) 'operative result' = a result that later changes how the system proceeds (L73's operative return). (b) dependence read on the actual history only, without setting i's port. (c) 'connected' read without direction.

**Used by:** claims of this part: FC75; 3 other claims.

### I91 · The infinitary routes on eventually periodic index sets

Fills in for:

> L311 | \(\Gamma=\{d_n:n\in\mathbb N\}\), \(d_n\) the constraint \(|x|\le 1/n\): every set of indices unbounded in \(\mathbb N\) determines \(x=0\)

**Invented.** Sets of commitments are represented by eventually periodic subsets of ℕ, F ∪ {n ≥ N : n mod m ∈ R}; unbounded exactly when R is nonempty. The clauses of FC40 are tested on these sets only.

**Other choices.** (a) arbitrary subsets of ℕ (not finitely representable). (b) a finite truncation of Γ (which changes the claim: every finite family has minimal routes).

**Used by:** claims of this part: FC40.

### I95 · Toy histories for active routes

Fills in for:

> L375 | An **active route** is a connected subnetwork of actual occurrences joining a represented input to an operative result

**Invented.** A history is a finite directed acyclic circuit of occurrences, each with its value computed from its parents; ≺ is reachability; the instantiated connections are the edges; 'connected' is weak connectivity by edges inside R; 'setting i's port' is an intervention on i's value with every later value recomputed; the declared contrasts are a given list of value pairs.

**Other choices.** (a) occurrences with time stamps and persistence made explicit (then 'at rest when the result occurred' could be written). (b) connectivity along directed chains only.

**Used by:** claims of this part: FC75; 1 other claim.

Named by title only (given in full in another part): I48, Contents, 'c's contract', and transports into a content; I77, Finite models and the bounds of the search; I78, Two families of generated organizations: surgical edits with override, and free edits; I81, Transports as port translations; computed ports; generated candidates; the transport space searched for ≡.

## 6. Choices no register entry records

Found by the two checks. U-entries come from the check that re-ran the program; H-entries from the check that read the maths against the text, in its wording.

### H11 · The "already at rest" clause dropped from active routes (D11.4)

*(L375, quoted above.)*

- **Added.** D11.4 (I46) has no clause for a route at rest when the result occurred, so it says less than L375. I46's entry does not record the omission. I95's other choice ("occurrences with time stamps and persistence made explicit") names what would be needed.
- **Depends on it.** The FC75 Look ("D11.4 counts it active", in the search-results file) and the line on the L375 "already at rest" route in the search's summary. L375 excludes such a route in so many words. What stays open in the text is only whether a finished route whose product persists is "at rest".

### H19 · Org_ℓ extended from occurrences to histories; "subhistory" (D11.3)

> L375 | A history \(h\) is a set of occurrences with an acyclic causal precedence \(\prec_h\) (write \(\preceq_h\) for its reflexive closure) and a physical interpretation supplying process occurrences, their ports, and the connections actually instantiated.

- **Added.**
  - "Org_ℓ(h) is the organization Θ gives h at grain ℓ": L213 gives Org_ℓ for an occurrence.
  - "A subhistory is a subset closed under the interpretation, with ≺ restricted." Neither has a number.
- **Depends on it.** D11.4 (active routes), and through it FC75, FC76, FC87 and FC101.

## 7. Sentences of this group the maths could not write

**NF18** (L161). Why it was not formalized: Strong candidate L161.s2: 'event' is defined nowhere (FC105); under I45 it types the formulation as a set of occurrences and says nothing further.

*(L161, quoted above.)*

## 8. Round 1: matters noted and changes made

In the first review round, readers tried to vary sentences that had stood unchanged; the rulings changed four lines and recorded fourteen matters outside the sentences examined, left for later rounds.

**Round-1 matter 2.** "event" is used at L53, L55, L161, L397, L604 and L612 and defined nowhere; "occurrence" is defined at L169; the text does not say how they are related (to be read with L596's claim).

**Round-1 matter 8.** L311's first sentence does not say in words that each d_n does no work by itself, which L313's "such commitments" needs; one step shows it.

**Round-1 matter 11.** "operative result", "applicable relations" (L375), "deliberative", "structural map" (L385) occur only there and are defined nowhere; round 1 read them as plain words.

**Round-1 matter 13.** "contribution" in Part VI and Part XI (L305; L435, L441), each sense fixed where it stands.

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
