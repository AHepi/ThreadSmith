# The maths against the words, part 12 of 17: Arguments, criticism and reason use

## 1. What you are asked to do

**The text** is a theory of explanation: a formal semantics of what an explanation is and of explanatory creativity, 632 lines, which calls itself "the semantics". Its owner took the decisions in section 2, and asked for "exploring the math a bit more" since "words are vague", adding: "if implementation forces invention, that needs to be recorded" (S36).

**The maths.** The text's definitions were written as mathematics beside the sentences they formalize (D0.1–D18.2; its worked cases encoded as E1–E9). The claims these let one state (FC01–FC110) were each put to a program that searched small finite models for a counterexample. Every choice the maths or the program made that the text does not fix was recorded as an **invention** (I01–I102), with the other choices that were possible. Two checks followed: one re-ran every counterexample and worked it by hand; the other read the maths against the text. They found further choices no entry records (U1–U6 and H01–H20). **Nothing invented is the text's own content.** A counterexample that rests on an invention tells against that way of writing the text, and against the text only where the text fixes what the invention fills in.

**This part** covers Part IX of the text on criticism, bearing, reason use, usable arguments and what a test rules out (L377–L399), with the failed answer of Part VIII (L369): the definitions in section 3; 9 claims (FC56, FC68, FC69, FC70, FC71, FC72, FC73, FC74, FC76) with their results in section 4; the inventions they rest on in section 5 (7 in full); the unrecorded choices in section 6; sentences the maths could not write in section 7; round-1 matters and changes in section 8. The whole is put to readers in 17 parts, each read on its own.

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

### §9 Arguments, usability, ruling out, bearing, reason use

> L397 | **Arguments.** A record leaf is a reference to an event with an interpreted claim. An argument is an argument tree: argument steps whose leaves are premises, which are record leaves or stated assumptions and definitions.

**D9.1 Claims.** Claims are sentences of a first-order language with ¬ and ∧; Incons(φ, ψ) is classical inconsistency of {φ, ψ} **[I38]**. The claims used here include 'Acc(ℰ)', 'Ans_p(a,b) = y', records of a test, and conditionals.

**D9.2 Argument.** A finite tree α. Each internal node is a step u with an inference form Form(u) and a conclusion concl(u); its children are its premises. Leaves are record leaves (each referring to an event, D11.1, with an interpreted claim) or stated assumptions and definitions. MadeFrom(leaf, ψ) is a primitive: the record leaf was made from the claim ψ **[I39]**.

> L387 | **Usability.** For argument step \(u\) with essential premises \(\operatorname{Prem}(u)\), the premises its inference form uses:

> L393 | \(\operatorname{Form}_j(u)\): the inference form of \(u\) is one \(j\) admits. \(\operatorname{Scope}_j(u)\): \(u\) is applied within the contract, grain and boundary \(j\) has declared for it; \(\operatorname{Live}_j(d;u)\): \(d\) is the conclusion of a step of the same argument as \(u\) that is usable by \(j\), or a premise \(j\) tentatively accepts, having taken it up, for whatever reason, and not withdrawn it, whether or not \(j\) holds an explanation of \(d\); a claim \(j\) has never taken up is not live for \(j\).

**D9.3 Essential premises.** Prem(u) ⊆ children(u): the premises Form(u) uses **[I40]**.

**D9.4 Live.** Accepted_j(ξ) is the set of claims j has taken up before ξ and not withdrawn before ξ (a declared input) **[I41]**. Live_j(d; u) :⟺ [d = concl(u') for a step u' in the subtree below u with Usable_j(u')] **[I40]** ∨ d ∈ Accepted_j(ξ).

**D9.5 Form and scope.** Form_j(u) :⟺ Form(u) ∈ Forms_j (declared). Scope_j(u) :⟺ C_u ⊆ C_j(u), ℓ_u = ℓ_j(u), β_u = β_j(u), where (C_u, ℓ_u, β_u) is the index u is applied at and (C_j(u), ℓ_j(u), β_j(u)) what j has declared for it **[I42]**.

> L390 | \operatorname{Usable}_j(u)\iff\operatorname{Form}_j(u)\land\operatorname{Scope}_j(u)\land\forall d\in\operatorname{Prem}(u),\operatorname{Live}_j(d;u). \tag{K2}

**D9.6 Usability (K2).** Usable_j(u) :⟺ Form_j(u) ∧ Scope_j(u) ∧ ∀d ∈ Prem(u) Live_j(d; u), defined by recursion on the height of u, which D9.4 makes well founded **[I40]**. Usable_j(α) :⟺ every step of α is usable by j.

> L397 | Each step of an argument rules out the case in which the step's premises are met and its conclusion fails, for someone who admits its inference form (\(\operatorname{Form}_j\)), while that form stays admitted. An argument is usable by \(j\) when each of its steps is (K2), and it rules out a claim when the claim is inconsistent with its conclusion and the claim's denial is not among its premises (below). For \(\psi\), \(X_j(\psi)\) is the set of arguments usable by \(j\) that rule out \(\psi\).

> L397 | An argument does not rule out a claim when the claim's denial is among its premises, alone or joined to other claims by "and", read structurally as non-circular dependence reads identity (Part V) and not by logical equivalence alone; nor does an argument whose record leaf was made from a claim rule out that claim's denial.

**D9.7 Rules out.** A step u, for j with Form_j(u), rules out the case Prem(u) ∧ ¬concl(u); forms need not be classically sound **[I38]**. RO(α, φ) :⟺ Incons(φ, concl(root of α)); no leaf of α has ¬φ as a conjunct (flattened, up to renaming and the order of conjuncts) **[I39]**; and no record leaf of α is made from a claim whose denial is φ.

> L315 | A claim is **ruled out** for an assessor \(j\) when an argument usable by \(j\) (Part IX) rules it out, and a candidate is ruled out for \(j\) when the claim that it meets (E) is;

> L315 | A candidate is **not ruled out** for \(j\) when no argument usable by \(j\) rules it out.

**D9.8 Ruled out; not ruled out.** X_j(φ) := {α : Usable_j(α) ∧ RO(α, φ)}. Out_j(φ) :⟺ X_j(φ) ≠ ∅; NotOut_j(φ) :⟺ X_j(φ) = ∅. A candidate ℰ is ruled out for j :⟺ Out_j('Acc(ℰ)').

> L397 | Where such an argument uses a claim taken as given, the ruling out is a choice the person using it made, not something the claim does by itself (Part 0).

Formally: Out_j depends on Accepted_j and Forms_j, which are declared inputs that no definition sets (FC56). The choice shows as the input; nothing here makes it.

> L395 | **What a test rules out.** For \(T\land B\land I\Rightarrow O\), an argument usable by \(j\) that rules out \(O\) rules out \(T\land B\land I\) together for \(j\), and nothing narrower. (K3)

**D9.9 (K3).** **[I43]** (i) If α ∈ X_j(O), the conditional T∧B∧I ⇒ O is live for j and j admits modus tollens, then α extended by one step is in X_j(T∧B∧I). (ii) From those premises alone, X_j(T), X_j(B) and X_j(I) gain no member (¬O, T∧B∧I ⇒ O and T have a common model).

> L377 | **Bearing.** A criticism has target \(z\), alleged defect \(\delta\), premise \(g\), and a connection. Let \(p_\delta\) be the question whether \(z\) has \(\delta\) in respect of \(p\), and \(\mathcal E_c\) the explanatory candidate (Part V) for \(p_\delta\) whose organization is the criticism's connection from \(g\) to \(\delta\), with its transport and its identified commitments. Then

> L380 | \operatorname{Bearing}(c,z,p)\iff\operatorname{Account}(\mathcal E_c). \tag{K1}

**D9.10 Criticism and bearing (K1).** A criticism c = (z, δ, g, Conn, occ): a target, an alleged defect, a premise, a connection (an organization from g to δ) and an occurrence in a history. p_δ, the question whether z has δ in respect of p, is supplied with c **[I76]**; ℰ_c := (Conn, p_δ, t_c, Γ_c, δ_c). Bearing(c, z, p) :⟺ Acc(ℰ_c).

> L383 | An adverse signal is not a criticism until an organization represents it as the premise of a criticism alleging a defect in a target.

A criticism's premise g is represented (D12.5) by an organization of the system.

> L385 | **Reason use.** A response uses a reason when a structural map from the represented objection into the response suborganization preserves role bindings, sends content-preserving recodings to the same transition, sends content changes to the changes specified by the operative deliberative rule, and lands on an active route.

**D9.11 Reason use** **[I47]**. The represented objection ob is a content with role bindings (a map from role names to its ports); R is the response suborganization; Rec and Chg are declared sets of content-preserving recodings and content changes of ob; Rule: Chg → changes of R is declared. UsesReason(R, ob) :⟺ there is a map m from ob's ports to R's ports preserving role names, with trans(m(ρ·ob)) = trans(m(ob)) for every ρ ∈ Rec, m(γ·ob) = Rule(γ)(m(ob)) for every γ ∈ Chg, and some image port of m on an active route (D11.4). No clause uses Acc or Usable (FC76).

**Vague.** 'Structural map', 'role bindings', 'the same transition' and 'operative deliberative rule' (L385) are defined nowhere [I47]. 'Among its premises … read structurally' is given by pointing at NC1, which is itself not defined [I39, I24]. Whether the step making a premise live lies below the step (L393) is not said; with any step of the argument, (K2) can have two fixed points (FC69) [I40].

## 4. The claims, with their search results

Each claim: its type, the inventions it uses, its sentences quoted, its formal statement, and its result, part by part; for a counterexample, what it shows and, where short, the model; then the second check's note, and every invention the result rests on (the claim's own and the program's).

### FC56 · Ruling out grows with what is accepted; withdrawal rules nothing out; absence rules out nothing

*a sentence that stood unchanged through every revision; follows from the definitions as written.* Inventions it uses: I38, I40, I41.

> L393 | Withdrawing a premise makes the step unusable; it does not rule the conclusion out.

> L397 | Where no argument usable by \(j\) rules out \(\phi\), that absence rules out nothing, neither \(\phi\) nor \(\neg\phi\).

**Formal.** (a) Usable_j and X_j(φ) are monotone in Accepted_j, in Forms_j and in the contracts j declares (grain and boundary held fixed): enlarging any of them never makes an argument unusable; RO does not depend on j. So withdrawing a premise adds no member to any X_j(φ): it rules out nothing not already ruled out. (b) There are j and φ with X_j(φ) = ∅ = X_j(¬φ).

**Result: HOLDS ON ALL MODELS TRIED.**

- *(a) monotone in what is accepted and admitted* (for all): **holds on all models tried** (1,162 models).
- *(b) absence rules out nothing* (computation): **computed: as claimed**.

**Rests on:** I38, I40, I41, I87, I88, I89.

### FC68 · A failed answer stays failed

*a result the text states.* Inventions it uses: I20, I38, I40, I41.

> L369 | Fix a question \(p\), a pair \((a,b)\in C\) and a value \(y\neq\operatorname{Ans}_p(a,b)\).

> L369 | and so on every question with the same target and query whose contract contains \((a,b)\).

> L369 | no candidate becomes an account by that (E).

**Formal.** (a) Ans_E(τa,σb) = y ≠ Ans_p(a,b) ⇒ ¬A_ab ⇒ ¬Acc on p, and on every p' with the same D, Q and δ whose contract holds (a,b). (b) If j has a usable argument ruling out 'Ans_p(a,b) = y', the premise 'Ans_E(τa,σb) = y' is live and the forms are admitted, then X_j(Acc(ℰ)) ≠ ∅ for every such ℰ alike. (c) If a premise of that argument stops being live, the ruling out lapses for all alike, and Acc(ℰ) is unchanged.

**Result: HOLDS ON ALL MODELS TRIED.**

- *(a) a failed answer stays failed* (for all): **holds on all models tried** (17,280 models).
- *(b), (c) every such candidate alike* (computation): **computed: as claimed**.

**Rests on:** I20, I38, I40, I41, I77, I78, I81, I87, I89.

### FC69 · (K2) is well founded; the loop an earlier study read closes below the step

*a sentence that stood unchanged through every revision; follows from the definitions as written.* Inventions it uses: I40.

*(L390, quoted above.)*

> L393 | \(d\) is the conclusion of a step of the same argument as \(u\) that is usable by \(j\)

**Formal.** Under I40, Usable_j(u) is defined by recursion on height; the loop K2 → Live → a step's usability → K2 (an earlier study) closes on steps strictly below u. Under I40's alternative (any step of the argument), there are arguments where the definition has two fixed points: a root u' concluding d with premise e, and a step u below it concluding e with premise d — both usable or both not.

**Result: HOLDS ON ALL MODELS TRIED.**

- *I40: recursion below the step is well founded* (computation): **computed: as claimed**.
- *I40's alternative: two fixed points* (computation): **computed: as claimed**.

**Rests on:** I40, I87, I89.

### FC70 · Withdrawing a premise that is live twice over leaves the step usable

*a sentence that stood unchanged through every revision; follows from the definitions as written.* Inventions it uses: I40, I41. Bears on round-1 matter 9 (section 8): a premise that stays live twice over (L393).

*(L393, quoted above.)*

**Formal.** There is an argument with a step u and d ∈ Prem(u) such that d is also the conclusion of a usable step below u and d ∈ Accepted_j; after j withdraws d, Live_j(d;u) still holds through the first disjunct, and Usable_j(u) is unchanged. So the first clause holds of a premise live by acceptance only.

**Result: HOLDS ON ALL MODELS TRIED.**

- *a premise live twice over* (computation): **computed: as claimed**.

**Rests on:** I40, I41, I87, I89.

### FC71 · (K3): a failed prediction rules out the conjunction, and nothing narrower

*a result the text states.* Inventions it uses: I38, I43.

> L395 | For \(T\land B\land I\Rightarrow O\), an argument usable by \(j\) that rules out \(O\) rules out \(T\land B\land I\) together for \(j\), and nothing narrower. (K3)

**Formal.** (i) A usable argument concluding ¬O, a live conditional T∧B∧I ⇒ O and an admitted modus tollens give a usable argument ruling out T∧B∧I. (ii) From those premises alone no argument rules out T, B or I by itself: ¬O, (T∧B∧I ⇒ O) and T have a common model.

**Result: HOLDS ON ALL MODELS TRIED.**

- *(i) the conjunction is ruled out* (computation): **computed: as claimed**.
- *(ii) nothing narrower* (computation): **computed: as claimed**.

**Rests on:** I38, I43, I87, I88, I89.

### FC72 · The block on a premise that is the denial, and a premise taken as given

*follows from the definitions as written.* Inventions it uses: I38, I39.

> L397 | An argument does not rule out a claim when the claim's denial is among its premises, alone or joined to other claims by "and", read structurally as non-circular dependence reads identity (Part V) and not by logical equivalence alone;

> L397 | a premise from which a step leads to the denial, as one does from \(r\) and "if \(r\), this candidate fails (E)", is a premise taken as given, and using it is the gamble above, not a circular argument.

**Formal.** (a) If ¬φ is a conjunct of a leaf (I39), then ¬RO(α,φ). (b) If a record leaf is MadeFrom ψ, then ¬RO(α,¬ψ). (c) The argument with leaves r and (r → ¬Acc(ℰ)) and one modus ponens step rules out Acc(ℰ): neither leaf has ¬Acc(ℰ) as a conjunct.

**Result: HOLDS ON ALL MODELS TRIED.**

- *(a), (b), (c)* (computation): **computed: as claimed**.

**Rests on:** I38, I39, I87, I89.

### FC73 · Inconsistent accepted premises rule out a claim and its denial alike

*a result the text states.* Inventions it uses: I38.

> L397 | Where the premises \(j\) tentatively accepts are inconsistent, arguments from them can rule out, for \(j\), a claim and its denial alike;

**Formal.** There are j and φ with X_j(φ) ≠ ∅ and X_j(¬φ) ≠ ∅ (for example Accepted_j ⊇ {q, q → ¬φ, s, s → φ}, modus ponens admitted).

**Result: HOLDS ON ALL MODELS TRIED.**

- *inconsistent premises* (computation): **computed: as claimed**.

**Rests on:** I38, I87, I89.

### FC74 · A criticism occurrence can exist without bearing

*a sentence that stood unchanged through every revision; follows from the definitions as written.* Inventions it uses: I45.

> L383 | A criticism occurrence can exist when (K1) fails.

**Formal.** The data of a criticism (target z, alleged defect δ, premise g, connection, an occurrence in a history) are defined without Acc; so there are models with a criticism occurrence c and ¬Acc(ℰ_c), that is ¬Bearing(c,z,p).

**Result: HOLDS ON ALL MODELS TRIED.**

- *a criticism without bearing* (there is): **witness found** (1 models).
  Searched: a criticism whose connection candidate has ¬Acc
  the connection's candidate fails (E): Bearing fails while the criticism occurrence (its data) exists

**Rests on:** I45, I77, I78, I81.

### FC76 · Reason use gives neither bearing nor usability

*a sentence that stood unchanged through every revision; follows from the definitions as written.* Inventions it uses: I47. Bears on round-1 matter 11 (section 8): the undefined phrases at L375 and L385.

> L385 | Using an objection does not give it bearing (K1) or make any argument from it usable (K2).

**Formal.** Under I47, UsesReason is defined without Acc and without Usable_j; there are models with UsesReason and ¬Bearing, and with UsesReason and no usable argument from the objection.

**Result: HOLDS ON ALL MODELS TRIED.**

- *reason use without bearing* (computation): **computed: as claimed**.

**Rests on:** I47, I90, I95.

## 5. The inventions these rest on

In full: each invention this part is the first of the parts to use. Then, for an invention given in full in another part that a counterexample here rests on, what was invented. Then the rest by title. I77 and I78, the bounds and families of the search, are described in section 1 and given in full in another part.

### I38 · Claims, their denials, and 'inconsistent with its conclusion'

Fills in for:

> L397 | An argument is usable by \(j\) when each of its steps is (K2), and it rules out a claim when the claim is inconsistent with its conclusion and the claim's denial is not among its premises (below).

**Invented.** Claims are sentences of a first-order language with classical ¬ and ∧; 'inconsistent with' is classical inconsistency of {φ, conclusion}. Inference forms themselves are arbitrary (an admitted form need not be classically sound); only the ruling-out relation uses classical consistency.

**Other choices.** (a) inconsistency relative to j's own admitted forms. (b) claims as sets of situations, inconsistency as disjointness.

**Used by:** claims of this part: FC56, FC68, FC71, FC72, FC73; 2 other claims.

### I39 · 'Among its premises', read structurally; records made from a claim

Fills in for:

*(L397, quoted above.)*

**Invented.** ¬φ is among the premises when some leaf, flattened as a conjunction, has ¬φ as a conjunct, up to renaming of bound variables and the order of conjuncts. 'Made from a claim' is a primitive relation MadeFrom(leaf, ψ) on record leaves.

**Other choices.** (a) up to a declared set of structural rewrites. (b) logical equivalence (the text excludes it).

**Used by:** claims of this part: FC72; 2 other claims.

### I40 · Live through a step: a step below, and essential premises

Fills in for:

*(L387, quoted above.)*

*(L393, quoted above.)*

**Invented.** An argument is a finite tree; Prem(u) is the set of u's children that its form uses. The step whose conclusion makes d live lies in the subtree below u, so Usable is defined by recursion on height and is well founded.

**Other choices.** (a) any step of the argument, the definition read as a least fixed point. (b) arguments as finite acyclic graphs, one node shared by several steps.

**Used by:** claims of this part: FC56, FC68, FC69, FC70; 2 other claims.

### I41 · Tentative acceptance over time; withdrawal

Fills in for:

> L393 | or a premise \(j\) tentatively accepts, having taken it up, for whatever reason, and not withdrawn it

**Invented.** Accepted_j(ξ) is the set of claims j has taken up before ξ and not withdrawn before ξ; Live, Usable and ruled out are evaluated at a time ξ. Accepted_j is a declared input (L522).

**Other choices.** (a) untimed sets (one assessor state).

**Used by:** claims of this part: FC56, FC68, FC70.

### I42 · Scope_j: within the declared contract, grain and boundary

Fills in for:

> L393 | \(\operatorname{Scope}_j(u)\): \(u\) is applied within the contract, grain and boundary \(j\) has declared for it

**Invented.** Each step u carries an index (C_u, ℓ_u, β_u); j declares (C_j(u), ℓ_j(u), β_j(u)); Scope_j(u) holds when C_u ⊆ C_j(u), ℓ_u = ℓ_j(u) and β_u = β_j(u).

**Other choices.** (a) equality of contracts. (b) steps without an index, Scope_j vacuous for them.

**Used by:** 1 other claim.

### I43 · (K3): what it adds and what 'nothing narrower' says

Fills in for:

*(L395, quoted above.)*

**Invented.** (i) If j has a usable argument concluding ¬O, the conditional T∧B∧I ⇒ O is live for j and j admits modus tollens, the argument extended by one step rules out T∧B∧I for j. (ii) 'Nothing narrower': from those premises alone no argument rules out T, B or I by itself, since classically ¬O, T∧B∧I ⇒ O and T have a common model.

**Other choices.** (a) (K3) as a restriction on j's admitted forms (j admits no form that concludes ¬T from them). (b) (K3) as a definition of what a test rules out, not a consequence of (K2).

**Used by:** claims of this part: FC71; 1 other claim.

### I47 · Reason use: 'structural map', 'role bindings', 'the same transition', 'operative deliberative rule'

Fills in for:

*(L385, quoted above.)*

**Invented.** The represented objection ob is a content with role bindings (a map from role names to its ports); a structural map m sends ob's ports to ports of the response suborganization R, preserving role names; Rec is a declared set of content-preserving recodings and Chg a declared set of content changes of ob; m(ρ·ob) induces the same state change of R as m(ob) for ρ in Rec; m(γ·ob) = Rule(γ)(m(ob)) for γ in Chg, with Rule a declared map ('the operative deliberative rule'); some image port of m lies on an active route (I46).

**Other choices.** (a) the deliberative rule as a component of the system's organization, picked out by its signature. (b) the structural map as a transport (π,τ,σ,λ), making reason use a fidelity condition.

**Used by:** claims of this part: FC76; 1 other claim.

Named by title only (given in full in another part): I20, How the fixed query is applied to a candidate's organization; I24, NC1: the target's answer as an unanalysed boundary input or component, read structurally; I45, 'Event' is a set of occurrences; I76, The three defects of a question, formally; I77, Finite models and the bounds of the search; I78, Two families of generated organizations: surgical edits with override, and free edits; I81, Transports as port translations; computed ports; generated candidates; the transport space searched for ≡; I87, Claims as propositional formulas, read structurally; I88, X_j ranges over a finite set of arguments; an argument has a step; I89, The inference forms: MP, MT, AND-introduction, AND-elimination and a free form; I90, The physical module supplied by hand: histories and provenance as free predicates; I95, Toy histories for active routes.

## 6. Choices no register entry records

Found by the two checks. U-entries come from the check that re-ran the program; H-entries from the check that read the maths against the text, in its wording.

### H12 · Bearing: p_δ and ℰ_c supplied with the criticism; the tag names an entry for another sentence (D9.10)

> L377 | Let \(p_\delta\) be the question whether \(z\) has \(\delta\) in respect of \(p\), and \(\mathcal E_c\) the explanatory candidate (Part V) for \(p_\delta\) whose organization is the criticism's connection from \(g\) to \(\delta\), with its transport and its identified commitments.

- **Added.** In D9.10:
  - "p_δ, the question whether z has δ in respect of p, is supplied with c" (tagged [I76]);
  - the connection "an organization from g to δ";
  - t_c, Γ_c and δ_c supplied.
- **Recorded, and not.** I76 fills in for L161 only (a question's three defects). D9.10's choices are in no entry.
- **Depends on it.** FC74, FC76 (the ¬Bearing half) and FC107.

## 7. Sentences of this group the maths could not write

**NF13** (L8). Why it was not formalized: No notion of a claim 'getting' something exists in the semantics; formally, only the absence of any predicate triggered by NotOut (a syntactic property).

> L8 | A claim that no argument rules out is only not ruled out, and gets nothing from that

**NF14** (L397). Why it was not formalized: No measure of cost; the text says so ('puts no measure on it').

> L397 | That a person can use a claim so, without containing its explanation, is a costly gamble for all creative agents

## 8. Round 1: matters noted and changes made

In the first review round, readers tried to vary sentences that had stood unchanged; the rulings changed four lines and recorded fourteen matters outside the sentences examined, left for later rounds.

**Round-1 matter 9.** A premise live twice over (a leaf that is also a usable step's conclusion): withdrawing it leaves the step usable by the first disjunct of Live, so L393's "Withdrawing a premise makes the step unusable", read without restriction, says more than (K2) gives in that narrow configuration.

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
