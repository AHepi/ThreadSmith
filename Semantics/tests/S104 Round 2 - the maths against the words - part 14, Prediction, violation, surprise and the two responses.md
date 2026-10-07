# The maths against the words, part 14 of 17: Prediction, violation, surprise and the two responses

## 1. What you are asked to do

**The text** is a theory of explanation: a formal semantics of what an explanation is and of explanatory creativity, 632 lines, which calls itself "the semantics". Its owner took the decisions in section 2, and asked for "exploring the math a bit more" since "words are vague", adding: "if implementation forces invention, that needs to be recorded" (S36).

**The maths.** The text's definitions were written as mathematics beside the sentences they formalize (D0.1–D18.2; its worked cases encoded as E1–E9). The claims these let one state (FC01–FC110) were each put to a program that searched small finite models for a counterexample. Every choice the maths or the program made that the text does not fix was recorded as an **invention** (I01–I102), with the other choices that were possible. Two checks followed: one re-ran every counterexample and worked it by hand; the other read the maths against the text. They found further choices no entry records (U1–U6 and H01–H20). **Nothing invented is the text's own content.** A counterexample that rests on an invention tells against that way of writing the text, and against the text only where the text fixes what the invention fills in.

**This part** covers prediction, violation and surprise in Part IV of the text (L215–L225), with Arguments 3 and 4 (L570–L584): the definitions in section 3; 4 claims (FC80, FC81, FC82, FC83) with their results in section 4; the inventions they rest on in section 5 (1 in full); the unrecorded choices in section 6; sentences the maths could not write in section 7; round-1 matters and changes in section 8. The whole is put to readers in 17 parts, each read on its own.

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

### Definitions from other sections that these claims use

> L193 | A transport \(t\) whose domain is an organization of a physical system has exactly one of three provenances, determined by its history in the physical module:

> L195 | **Selected.** There is a population \(\mathcal T\) of candidate transports, a variation operator \(\mu\) on \(\mathcal T\), a finite history \(H\subseteq C\) of edit–boundary pairs actually encountered, and a survival condition requiring fidelity on \(H\).

> L195 | A transport **survives on \(H\)** when it is a member of \(\mathcal T\) that meets the survival condition on \(H\); fidelity on \(H\) without membership in \(\mathcal T\) is not survival. No member of the history represents \(t\), \(H\), or the survival condition.

**D12.1 Selected.** Sel(t; 𝒯, μ, H) :⟺ t ∈ 𝒯; μ: 𝒯 → P(𝒯); H ⊆ C finite, its pairs having occurred (D11.5); Faithful_H(t) (D5.7), i.e. t survives on H; and there is a physical selection history h_sel in which the pairs of H occur, the members of 𝒯 are admitted by the physics (D15.8), and no occurrence represents (D12.5) t, H or the survival condition **[I52]**.

> L197 | **Constructed.** There is an episode (Part X) whose construction trace prepares \(t\), and in which \(t\), or the organization it carries to, is available as a represented target. Write \(\operatorname{Con}(t;h,e)\).

**D12.2 Constructed.** Con(t; h, e) :⟺ some episode of h up to e (D13.8) has a construction trace (D13.3) that prepares t, and t or its codomain is a represented target in it.

> L175 | The **object layer** \(P\) is an organization whose ports are persistent things with boundaries and identity, whose components are their continuity relations, and whose admitted edits include displacement, occlusion and re-identification.

> L177 | The **simulation layer** \(S\) is an organization over \(P\) whose components are dependencies among things and whose queries are predictions: what a port of \(P\) will take under an admitted edit.

**D12.6 Layers.** P and S are organizations typed as L175 and L177 say; nothing assumes either exists in a given system (L179).

> L219 | - the **prediction** is \(\operatorname{Ans}_S(\tau(a),\sigma(b))\);

> L220 | - a **violation** occurs when fidelity fails at \((a,b)\);

> L221 | - **surprise** is a violation of a selected transport at \((a,b)\notin H\).

**D12.7 Prediction, violation, surprise.** For t from P to S with contract C and, if selected, history H, at (a,b) ∈ C with Occurs(a,b,ξ): Pred_t(a,b) := Ans_S(τ(a),σ(b)); Viol(t; a,b) :⟺ ¬(F1 at (a,b) ∧ F2eq at (a,b)), and Viol⁺ adds (A) at (a,b) **[I50]**; Surp(t; a,b) :⟺ Sel(t; 𝒯, μ, H) for some 𝒯, μ, H with (a,b) ∉ H, and Viol(t; a,b). Pred is extended to any transport, Pred_t(a,b) := Ans_E(τ(a),σ(b)), where a line uses it so (L151) **[I51]**.

> L225 | A **selection response** extends the history \(H\) of a selected transport and lets \(\mu\) act: the transport is re-tuned within the population. A **construction response** introduces a new organization or a new transport with a construction trace.

**D12.8 Responses.** SelResp(t → t'; a,b) :⟺ Sel(t; 𝒯, μ, H), t' ∈ μ*(t) ⊆ 𝒯 and t' survives on H ∪ {(a,b)}. ConResp(→ t'') :⟺ t'' or its codomain is new (D13.5) and Con(t''; h, e).

> L405 | **Construction.** \(\operatorname{Build}_{\beta,\ell}(s,c,h,e)\) is met when an actual subhistory owned by \(s\) and delimited at \(e\) prepares a represented organization for explanatory use of \(c\), contains a nontrivial binding construction relevant to that use, and is not a composition of content-preserving transfers.

**D13.3 Build; construction trace.** Build_{β,ℓ}(s, c, h, e) :⟺ some subhistory h' of h ending at e with Owned_β(h', s) (D13.7) has Prepares(h', c), BindingConstruction(h', c) and ¬TransferComposite(h') **[I56]**. A construction trace is (h', the controlled processes, the incoming carriers, the bindings constructed, the resulting representation) (L405). A binding may be identified by its use: by responses meeting D9.11's clauses (L409).

## 4. The claims, with their search results

Each claim: its type, the inventions it uses, its sentences quoted, its formal statement, and its result, part by part; for a counterexample, what it shows and, where short, the model; then the second check's note, and every invention the result rests on (the claim's own and the program's).

### FC80 · Argument 3: underdetermination where the population leaves room

*a result the text states.* Inventions it uses: I02, I52, I71.

> L572 | the value of \(t\) at \((a,b)\) is underdetermined by \(H\): survival on \(H\) does not distinguish \(t\) from \(t'\) there.

> L574 | Where \(\mathcal T\) contains no such transport, \(H\) is silent on the value at \((a,b)\) and the population fixes it.

**Formal.** (a) If t, t' ∈ 𝒯 both survive on H and value_t(a,b) ≠ value_t'(a,b) (I71) for (a,b) ∈ C∖H, the survival condition does not separate them. (b) If all survivors on H agree at (a,b), that value is a function of (𝒯, H). (c) The step 'altered at one pair gives another admitted relation' uses I02; under an action law, an alteration at one pair can force others, and (a)'s hypothesis is harder to meet.

**Result: HOLDS ON ALL MODELS TRIED.**

- *(a), (b) the survivors on H fix what they share* (for all): **holds on all models tried** (7,383 models).
- *(a) underdetermination* (there is): **witness found** (1 models).
  Searched: some (a,b) ∈ C∖H at which survivors on H differ
  underdetermined at (e1,b0): 2 survivors on H = {(1,b0)} with different values there
- *(c) under an action law* (not tested): **not tested**.
  Why not: comparing I02 with an action law needs a population family closed under an action law; not built in this round

**Rests on:** I02, I52, I71, I77, I78, I81.

### FC81 · Argument 4, and who can be surprised

*a result the text states.* Inventions it uses: I50, I52, I53.

> L580 | **Claim.** A system can be surprised only if it holds a transport selected on a history \(H\) strictly smaller than its contract \(C\).

> L223 | A system with no transport cannot be surprised. A system whose history exhausts its contract cannot be surprised.

> L223 | a constructed one that fails at an actually occurring pair of its contract is violated, and the failure is not surprise

**Formal.** Surp(t;a,b) := Sel(t) ∧ Viol(t;a,b) ∧ (a,b) ∈ C∖H ∧ Occurs(a,b). (a) Surp ⇒ H ⊊ C. (b) No transport ⇒ no Surp. (c) H = C ⇒ no Surp. (d) Con(t) ∧ Viol ⇒ ¬Surp (I53).

**Result: COUNTEREXAMPLE FOUND.** (d) rests on the same history as FC78 (I52, I53, I56, I90).

- *(a)-(c)* (by construction): **holds by construction**.
- *(d) Con(t) ∧ Viol ⇒ ¬Surp (under I53)* (computation): **computed: not as claimed**.
  Searched: a constructed transport violated at an occurring pair is not surprised
  In a history like FC78's (the codomain represented, Prepares, no representation of t, H or the survival condition), t (the pole's forward transport into an organization whose c_L gives L = 1 under set H=2) is faithful on H = {(1,b1_45)} (Hom included) and violated at (set(H=2), b1_45) ∉ H, which occurs. Con: yes; Sel: yes; Viol: yes; Surp: yes. The clause rests on FC78's claim that Sel excludes Con, which fails under D12.1.

**The second check.** One finding with FC78 (same history, with t replaced by a transport violated at (set(H=2), b1_45) ∉ H, so Sel, Viol, Surp and Con all hold). See FC78's note and H05.

**Rests on:** I50, I52, I53, I56, I90, I92.

### FC82 · The two responses to a violation have no common result

*a sentence that stood unchanged through every revision; follows from the definitions as written.* Inventions it uses: I52, I53.

*(L225, quoted above.)*

**Formal.** SelResp(t → t'): t' ∈ 𝒯, reached from t by μ, surviving on H ∪ {(a,b)}; ConResp(→ t''): t'' or its codomain new, with Con(t''). Under I53 no transport is the result of both (Sel(t') excludes Con(t')).

**Result: COUNTEREXAMPLE FOUND.** Rests on the same history as FC78 (I52, I53, I56, I90).

- *no common result* (computation): **computed: not as claimed**.
  Searched: no transport is the result of both a selection response and a construction response
  t' = the pole's forward transport, new relative to an empty repertoire, survives on H ∪ {('set(H=2)', 'b1_45')} (SelResp) and has Con in the same history (ConResp): yes and yes. As in FC78, D12.1 does not exclude a represented codomain.

**The second check.** One finding with FC78 (same history, t' = t). The recorded 'response' has t' = t and no violation; the check built a stronger case (population {t, t'}, μ(t) = {t'}, t violated at (set(H=2), b1_45) ∉ H, t' surviving on H with that pair added, the same history giving Con(t')): the two responses still have a common result. See H05 and H08.

**Rests on:** I52, I53, I56, I90, I92.

### FC83 · Only the construction response can be originative

*a sentence that stood unchanged through every revision; a result the text states.* Inventions it uses: I52, I56.

> L225 | Only the second can be originative under Part X.

**Formal.** Claim to test: SelResp(t → t') ⇒ ¬Origin(s,c',p,h,e) for the content c' that t' carries to. (G) needs Build, and Build needs a subhistory that prepares a represented organization for explanatory use of c' (I56). Sel(t') forbids occurrences that represent t', H or the survival condition (L195), not the organization t' carries to (which Con names, L197).

**Result: COUNTEREXAMPLE FOUND.** Rests on I56 (Build's three primitives) and I90 (Θ by hand); it is the case FC83's own Look names.

- *only construction is originative* (computation): **computed: not as claimed**.
  Searched: SelResp(t → t') ⇒ ¬Origin(s, c', …)
  A history in which t' survives on H ∪ {('set(H=2)', 'b1_45')} (SelResp: yes) and an owned subhistory prepares a represented organization for c' with a binding construction and is no transfer composite (Build's three primitives, I56, set to hold), c' used to address p (Attempt) and no earlier content matches it (New): Origin yes. Nothing in D12.1 or D13.3 ties Build's subhistory to the selection history; the claim follows only on one of the two conditions its Look names.

**The second check.** Separate from FC78. Origin's three conjuncts are set to hold by hand (Attempt, New, and Build's primitives, I56); the selection response holds on the same history; nothing in D12.1, D12.8 or D13.3 ties Build's subhistory to the selection history. It shows what the definitions allow, not any physics (I52, I56, I90, I92).

**Rests on:** I52, I56, I90, I92.

## 5. The inventions these rest on

In full: each invention this part is the first of the parts to use. Then, for an invention given in full in another part that a counterexample here rests on, what was invented. Then the rest by title. I77 and I78, the bounds and families of the search, are described in section 1 and given in full in another part.

### I50 · A violation at a pair: which conditions fail

Fills in for:

*(L220, quoted above.)*

**Invented.** Violation(t;a,b) := not [(F1) at (a,b) and the valuation equation of (F2) at (a,b)] (narrow). Violation⁺ adds (A) at (a,b). Both are carried; FC20 asks when they coincide.

**Other choices.** (a) only (A) at (a,b) (a failed prediction). (b) the whole of (F2), homomorphism clause included.

**Used by:** claims of this part: FC81; 2 other claims. Counterexamples resting on it: FC20, FC81.

### I52 · Selection: the parameters witnessed in a physical history

**Invented** (given in full in another part). μ: 𝒯 → P(𝒯); the survival condition is Faithful_H (narrow). Sel(t;𝒯,μ,H) also requires a physical selection history h_sel in which the pairs of H occur and the members of 𝒯 are admitted by the physics (L481), and in which no occurrence represents (R) t, H or the survival condition. 'Member of the history' is read as an occurrence of h_sel, since the members of H are pairs and cannot represent.

### I53 · 'Exactly one of three provenances': one whole history

**Invented** (given in full in another part). Sel and Con are evaluated on one history: the whole physical history of t up to the attribution. Con then excludes Sel (Con puts a represented target in that history; Sel has none).

### I56 · Build: 'prepares', 'nontrivial binding construction', 'content-preserving transfer'

**Invented** (given in full in another part). Build := for some subhistory h' of h ending at e and owned by s, Prepares(h',c), BindingConstruction(h',c) and not TransferComposite(h'), with the three as primitive predicates read through the physical module.

### I90 · The physical module supplied by hand: histories and provenance as free predicates

**Invented** (given in full in another part). Where the formal core reads something through Θ (which occurrences represent what, which pairs occur, whether the physics admits a population, Prepares, BindingConstruction, TransferComposite, Attempt, Integrated), the program sets it by hand as a finite relation. 'The organization it carries to is a represented target' is an occurrence representing t's codomain. Transports and their fidelity are computed; the rest is stipulated. A model built so shows what the definitions allow, not what any physics does.

### I92 · The pole in exact arithmetic, with its grids, baseline, contracts and fibre query

**Invented** (given in full in another part). Values of L are exact numbers r + s√3 (cot 30° = √3, cot 45° = 1, cot 60° = √3/3); X_L is the set of values H cot θ on the grid H ∈ {1,2,3}, θ ∈ {30°,45°,60°}; boundaries are the nine pairs (u_H, u_θ); b0 = (1, 45°); C1 holds the single settings of H and θ at b0, C2 adds the single settings of L, C2* adds the composites that set L with H or θ. The fibre query returns {H ∈ X_H : H cot θ = L} for the single value of (θ, L) in Sol, ⊥ when that value is not single. E_rev's components are c'_L (L = u_H cot u_θ, from the boundary), c'_θ and c'_H (H = L tan θ), with λ as in model/cases.py.

Named by title only (given in full in another part): I02, No law links a composite edit's relations to its parts' relations; I51, 'Prediction' for a transport not said to reach the simulation layer; I71, The 'value' of a transport at a pair (Argument 3); I77, Finite models and the bounds of the search; I78, Two families of generated organizations: surgical edits with override, and free edits; I81, Transports as port translations; computed ports; generated candidates; the transport space searched for ≡.

## 6. Choices no register entry records

Found by the two checks. U-entries come from the check that re-ran the program; H-entries from the check that read the maths against the text, in its wording.

### H07 · Surprise with the selection parameters bound by "for some" (D12.7)

> L217 | Let \(t\) be a transport to the simulation layer \(S\), with contract \(C\) and, where \(t\) is selected, history \(H\).

*(L221, quoted above.)*

- **Added.** "Surp(t; a,b) :⟺ Sel(t; 𝒯, μ, H) for some 𝒯, μ, H with (a,b) ∉ H, and Viol(t; a,b)". L217 gives t one history H, and L193 says provenance is "determined by its history".
- **A consequence the formal core does not note.** Sel asks for (F1) and the (F2) equation at every pair of H, and Viol is their failure at (a,b). So Viol(t; a,b) already puts (a,b) outside every H on which t survives, and the clause "(a,b) ∉ H" does no work in D12.7.
- **Other choice.** H is the one history of t's selection, fixed by the physical history.
- **Depends on it.** No computed result: FC81 (d) uses a fixed H.

### H08 · The two responses (D12.8), and the model's responses

*(L225, quoted above.)*

- **Added in D12.8.** SelResp uses μ*, any number of μ-steps including none, so t' = t is allowed. ConResp reads "new" as New (N) relative to a repertoire. Neither choice has a number.
- **Added in the model.** FC82 and FC83 compute the selection response as `sel(c, H + [x], h)` alone: no violation at x, no μ step, and t' = t. The responses to a violation that L225 distinguishes are not modelled; what is computed is Sel on an extended history.
- **Depends on it.** FC82 and FC83. Their counterexamples show only what FC78 shows (Sel and Con on one history). They say nothing further about responses.

## 7. Sentences of this group the maths could not write

None beyond those named under the claims.

## 8. Round 1: matters noted and changes made

In the first review round, readers tried to vary sentences that had stood unchanged; the rulings changed four lines and recorded fourteen matters outside the sentences examined, left for later rounds.

**Round-1 matter 3.** "signature" in the everyday sense at L584 ("the signature of a selected transport meeting a change outside its history"), beside the defined term.

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
