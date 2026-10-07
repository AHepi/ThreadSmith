# The maths against the words, part 16 of 17: The physical module, recursion, universality and the class collected

## 1. What you are asked to do

**The text** is a theory of explanation: a formal semantics of what an explanation is and of explanatory creativity, 632 lines, which calls itself "the semantics". Its owner took the decisions in section 2, and asked for "exploring the math a bit more" since "words are vague", adding: "if implementation forces invention, that needs to be recorded" (S36).

**The maths.** The text's definitions were written as mathematics beside the sentences they formalize (D0.1–D18.2; its worked cases encoded as E1–E9). The claims these let one state (FC01–FC110) were each put to a program that searched small finite models for a counterexample. Every choice the maths or the program made that the text does not fix was recorded as an **invention** (I01–I102), with the other choices that were possible. Two checks followed: one re-ran every counterexample and worked it by hand; the other read the maths against the text. They found further choices no entry records (U1–U6 and H01–H20). **Nothing invented is the text's own content.** A counterexample that rests on an invention tells against that way of writing the text, and against the text only where the text fixes what the invention fills in.

**This part** covers Part XII of the text (L459–L483), Part XIII (L485–L511) and Part XIV (L513–L530): the definitions in section 3; 5 claims (FC91, FC92, FC93, FC94, FC110) with their results in section 4; the inventions they rest on in section 5 (6 in full); the unrecorded choices in section 6; sentences the maths could not write in section 7; round-1 matters and changes in section 8. The whole is put to readers in 17 parts, each read on its own.

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

### §15 The physical module

> L461 | **Tasks.** A substrate is a physical system; an attribute a set of its states; a task a specified input-to-output attribute transformation with explicit resources and side effects. Possibility is the absence of a law-imposed limit, short of exact, on the tolerance to which a task can be performed and retained; it is not one trajectory that performed the task.

**D15.1 Tasks.** A substrate has a state space Z_s; an attribute is a subset of Z_s; a task T is a relation between input and output attributes, with dom T and T[i], and with its resources and side effects stated **[I61]**. Here physical possibility enters as the carrying out of a transformation.

> L466 | \operatorname{RetReal}(\pi,T,C;\chi)\iff\forall z\in C\ \forall i\in\operatorname{dom}T\ \forall\eta\in\operatorname{Exec}(\pi,z,i;\chi),\ \eta\text{ completes with }o\in T[i]\text{ and }z'\in C. \tag{CT1}

> L469 | Execution families are nonempty on admitted inputs; deadlock is not a vacuous performance of the task.

**D15.2 Retained realization (CT1).** Exec(π, z, i; χ) is a set of executions, each with a completion flag, an output o and a final constructor state z'. RetReal(π, T, C; χ) :⟺ for every z ∈ C, i ∈ dom T and η ∈ Exec(π, z, i; χ): η completes with o ∈ T[i] and z' ∈ C. Standing assumption: Exec(π, z, i; χ) ≠ ∅ for z ∈ C and i ∈ dom T **[I61]**. (Here C is a constructor attribute and π a protocol: the letters of Part XII are local.)

> L471 | **Retention fixed point.** \(F(C)\) = states whose executions all complete and return into \(C\). \(F\) is monotone; \(C\subseteq F(C)\) is the invariant form; the greatest fixed point is the union of the sets \(D\) with \(D\subseteq F(D)\). (CT2)

**D15.3 Retention operator; (CT2).** F(X) := {z ∈ Z : for every i ∈ dom T and every η ∈ Exec(π, z, i; χ), η completes with o ∈ T[i] and z' ∈ X}, with 'complete' read as (CT1)'s completion **[I61]**. (CT2): F is monotone on P(Z); RetReal(π, T, C; χ) ⟺ C ⊆ F(C); gfp(F) = ∪{D ⊆ Z : D ⊆ F(D)}, with D a bound letter (FC91, FC92).

> L473 | **System boundary and continuity.** A capability is attributed to a system under a declared boundary (which processes and resources are the system's) and a declared continuity \(\Omega\) (what makes it the same system through change).

**D15.4 Boundary and continuity.** β: the processes and resources that are the system's (declared); Ω: a relation on system states saying which are the same system (declared). Both are fixed before the attribution (L473).

> L475 | **Owned capability.** \(\operatorname{Can}_{\Omega,\beta}(\xi,T;\chi)\) requires an owned retained realization or an owned, physically admitted, finite construction of one under the same continuity and resource contract.

**D15.5 Owned capability.** Can_{Ω,β}(ξ, T; χ) :⟺ there is a protocol π and constructor attribute C, owned (D13.7) at ξ, with RetReal(π, T, C; χ); or an owned, physically admitted, finite construction of such, under Ω and the same resource contract.

> L477 | **Achievement.** \(\operatorname{CanAdv}(\xi,p;\chi,J_p,C_I)\): for each starting configuration in the independently specified \(J_p\), every maximal execution completes with a history meeting the achievement predicate and a continuing organization in \(C_I\).

**D15.6 Advancing capability (CA).** CanAdv(ξ, p; χ, J_p, C_I) :⟺ for every z ∈ J_p, every maximal execution from z completes with a history meeting the achievement predicate for p and ends with an organization in C_I.

> L479 | **Tolerances.** The tolerances of the physical module (Part XIV) form a directed preorder \(Q_\Theta\), in which \(q\) precedes \(q'\) when \(q'\) admits no performance \(q\) excludes, and none of them is exact;

**D15.7 Tolerances; Admit, Cap, Poss.** (Q_Θ, ≤) a directed preorder, q ≤ q' when q' excludes at least what q excludes; no member exact. Admit^{q,r} := the tasks with a realization (owned or not) at performance tolerance q and retention tolerance r, antitone in (q, r) **[I62]**; Cap^{q,r}_Ω(ξ) := the tasks with an owned realization, or an owned construction of one, at (q, r); Poss_Θ := ∩_{q,r} Admit^{q,r}; Cap^∞ := ∩_{q,r} Cap^{q,r}. (CT3): Cap^{q,r} ⊆ Admit^{q,r}; (CT4): Cap^∞ ⊆ Poss_Θ (FC93).

> L481 | The population is the set of transports the physics and the stated construction admit; a transport that would need a part every member of the population is built without is not in it.

**D15.8 Selection's population.** 𝒯 := {t : Θ admits t ∧ parts(t) ⊆ the parts of the stated construction}; μ is physically admitted; the survival condition is enacted by the environment (L481). This is where D12.1's witness is read.

### §16 Recursion, universality, classes

> L487 | **Scrutinizability.** An aspect \(d\) of a system's practice is scrutinizable at \(\xi\) when there is an owned, admitted continuation in which a description of \(d\) becomes a represented target, criticism can be directed at it, and the result can affect its operative use.

**D16.1 Scrutinizable.** Scr(d, ξ) :⟺ some owned, physically admitted continuation from ξ has a description of d as a represented target, a criticism (D9.10) of it, and a result on an active route to d's operative use.

> L492 | \forall n<\omega\ \forall\text{ admitted target chains of length }n,\ \exists\text{ an owned enabling continuation}. \tag{RC}

**D16.2 Recursive capacity (RC).** RC :⟺ for every n < ω and every admitted target chain d1, …, dn (each d(i+1) a description of di made a represented target), there is an owned continuation meeting Scr(dn) **[I74]**.

> L495 | \(\operatorname{Enable}(s,T,\chi)\) is met when \(\chi\) is an admitted, non-question-begging enabling condition for \(s\) and the task \(T\), in the sense of (CT1).

**D16.3 Enable.** Enable(s, T, χ) :⟺ χ is physically admitted, 'non-question-begging' (not defined; NF11), and an enabling condition in (CT1)'s sense.

> L500 | \operatorname{UU}\iff\forall c\in\mathfrak E_\Theta\ \exists\chi,\ \operatorname{Enable}(s,U_c,\chi)\land\operatorname{Can}(\xi_0,U_c;\chi), \tag{U1}

> L503 | \operatorname{UC}\iff\forall p\in\mathfrak P^{\mathrm{adv}}_\Theta\ \exists\chi,\ \operatorname{Enable}(s,A_p,\chi)\land\operatorname{CanAdv}(\xi_0,p;\chi,J_p,C_I), \tag{U2}

> L506 | \mathsf{UECS}=\{(M,s,\xi_0,\Omega,\beta):M\models\operatorname{RC}\land\operatorname{UU}\land\operatorname{UC}\}. \tag{U3}

**D16.4 Universality.** 𝔈_Θ := {c : Acc(c, p, t, Γ) for some p, t, Γ, and Θ admits a carrier instantiating c} **[I75]**; 𝔓^adv_Θ is not defined beyond its name (NF12). UU, UC, UECS as displayed.

> L528 | **Membership.** The base class: interpretations supplying these data with typing as declared, meeting physical realization wherever a physical attribution is made. The creative-episode class: base interpretations with an instance of (G) connected to a critical episode. The explanation-creation class: an instance of (EX). The recursive class: (RC). The universal class: (U3).

**D16.5 Classes.** Base := the interpretations M of the data of §§1–15 with the typing above and Θ-realization of every physical attribution; CreativeEp := {M ∈ Base : M has an instance of (G) in a critical episode}; ExplCreation := {M : M ⊨ CreateEx for some s, Δ, h, e}; Recursive := {M : M ⊨ RC}; Universal := UECS. Each is the extension of a formula; no axiom here puts any system in any class (FC110).

## 4. The claims, with their search results

Each claim: its type, the inventions it uses, its sentences quoted, its formal statement, and its result, part by part; for a counterexample, what it shows and, where short, the model; then the second check's note, and every invention the result rests on (the claim's own and the program's).

### FC91 · (CT1) is C ⊆ F(C) only with (CT1)'s completion read into F

*follows from the definitions as written.* Inventions it uses: I61. Bears on round-1 matter 10 (section 8): 'complete' in L471's first sentence.

*(L466, quoted above.)*

> L471 | \(F\) is monotone; \(C\subseteq F(C)\) is the invariant form

**Formal.** Under I61: RetReal(π,T,C;χ) ⟺ C ⊆ F(C). With 'complete' read without the output condition, C ⊆ F(C) follows from RetReal and is weaker than it.

**Result: HOLDS ON ALL MODELS TRIED.**

- *(CT1) ⟺ C ⊆ F(C) under I61* (for all): **holds on all models tried** (12,000 models).
- *the other reading is weaker* (there is): **witness found** (2 models).
  Searched: with 'complete' read without the output condition, C ⊆ F(C) does not give RetReal
  C = [0, 1, 2]: C ⊆ F'(C) (complete without the output condition) and ¬RetReal; T = {0: {1, 2}, 1: {0, 1}}; executions {(0, 0): [(yes, 0, 1), (yes, 1, 0)], (0, 1): [(yes, 1, 1), (yes, 2, 2)], (1, 0): [(yes, 2, 1)], (1, 1): [(yes, 1, 2)], (2, 0): [(yes, 1, 2)], (2, 1): [(yes, 0, 1)]}

**Rests on:** I61, I97.

### FC92 · (CT2): monotone F and its greatest fixed point

*a sentence that stood unchanged through every revision; a result the text states.* Inventions it uses: I61. Bears on the round-1 change at L471 (section 8); what the round-1 change at L471 may have disturbed: the locally bound D and how L546 names (CT2).

> L471 | the greatest fixed point is the union of the sets \(D\) with \(D\subseteq F(D)\). (CT2)

> L546 | **A mathematical error.** A counterexample to the finite monotone claim, (I2), (O1), (T2), (CT2), or Arguments 1–3 under their stated assumptions.

**Formal.** (a) X ⊆ Y ⇒ F(X) ⊆ F(Y). (b) U := ∪{D ⊆ Z : D ⊆ F(D)} has F(U) = U and contains every fixed point (the Knaster–Tarski construction on P(Z)). (c) The D of (b) is bound in the clause and is not a question's target. (d) (CT2) has no counterexample under either reading of 'complete', since monotonicity does not use the output condition.

**Result: HOLDS ON ALL MODELS TRIED.**

- *(CT2)* (for all): **holds on all models tried** (12,000 models).

**Rests on:** I61, I97.

### FC93 · (CT3), (CT4), and capability at one tolerance

*a result the text states.* Inventions it uses: I62.

> L479 | Then \(\mathsf{Cap}^{q,r}_\Omega(\xi)\subseteq\mathsf{Admit}^{q,r}_\Theta\); \(\mathsf{Cap}^\infty=\bigcap_{q,r}\mathsf{Cap}^{q,r}\subseteq\mathsf{Poss}_\Theta\). (CT3, CT4) Capability at a given tolerance does not imply possibility at every tolerance.

**Formal.** (a) Under I62, Cap^{q,r} ⊆ Admit^{q,r}. (b) Intersecting over (q,r): Cap^∞ ⊆ Poss. (c) There are models with T ∈ Cap^{q,r} and T ∉ Poss.

**Result: HOLDS ON ALL MODELS TRIED.**

- *(a) CT3, (b) CT4* (for all): **holds on all models tried** (12,000 models).
- *(c) capability at one tolerance* (there is): **witness found** (2 models).
  Searched: T ∈ Cap^{q,r} and T ∉ Poss
  T ∈ Cap^(0, 0) and T ∉ Poss: [3]

**Rests on:** I62, I98.

### FC94 · Recursion does not entail universality

*a result the text states.* Inventions it uses: I74, I75.

> L509 | Recursion does not entail universality; a historical extension leaves it open; a finite performance record does not suffice for it.

**Formal.** (a) There is a model of RC with ¬UU. (b) With 𝔈_Θ infinite (I75), no finite set of performed tasks decides UU.

**Result: NOT TESTED.**

- *recursion and universality* (not tested): **not tested**.
  Why not: RC, UU, Enable, target chains and 𝔈_Θ have no finite semantics without Θ; a model would be an assignment of free predicates, which shows only that no axiom links them (as FC110)

**Rests on:** I74, I75.

### FC110 · The classes are defined; no membership is asserted

*a sentence that stood unchanged through every revision; follows from the definitions as written.* Inventions it uses: I74, I75.

> L27 | It does not decide whether any human, machine, institution or lineage belongs to the classes defined. It defines the classes.

> L528 | **Membership.** The base class: interpretations supplying these data with typing as declared, meeting physical realization wherever a physical attribution is made.

**Formal.** Syntactic: each class of L528 (base, creative-episode, explanation-creation, recursive, universal) is the extension of a formula of the formal core; no axiom of the formal core places any particular system in a class.

**Result: NOT TESTED.**

- *the classes* (not tested): **not tested**.
  Why not: syntactic, about the formal core's definitions

**Rests on:** I74, I75.

## 5. The inventions these rest on

In full: each invention this part is the first of the parts to use. Then, for an invention given in full in another part that a counterexample here rests on, what was invented. Then the rest by title. I77 and I78, the bounds and families of the search, are described in section 1 and given in full in another part.

### I61 · Tasks and executions; 'complete' in F read as (CT1)'s completion

Fills in for:

> L461 | a task a specified input-to-output attribute transformation with explicit resources and side effects.

*(L469, quoted above.)*

> L471 | \(F(C)\) = states whose executions all complete and return into \(C\).

**Invented.** A task T is a relation between inputs and outputs, with dom T and T[i]. Exec(π,z,i;χ) is a set of executions, each with a completion flag, an output o and a final constructor state z'. F(X) := {z : for every i in dom T and every η in Exec(π,z,i;χ), η completes with o in T[i] and z' in X}: 'complete' is read as (CT1)'s 'completes with o ∈ T[i]'. Nonemptiness of Exec (L469) is a standing assumption for z in C and i in dom T, not part of F.

**Other choices.** (a) 'complete' without the output condition (then C ⊆ F(C) is weaker than (CT1)). (b) nonemptiness inside F (F(X) then leaves out states with no executions).

**Used by:** claims of this part: FC91, FC92; 1 other claim.

### I62 · Tolerances: stricter tolerances admit fewer tasks; Admit contains every realized task

Fills in for:

> L479 | form a directed preorder \(Q_\Theta\), in which \(q\) precedes \(q'\) when \(q'\) admits no performance \(q\) excludes, and none of them is exact;

> L479 | \(\mathsf{Admit}^{q,r}_\Theta\) is the set of tasks physically achievable at tolerances \((q,r)\);

**Invented.** q precedes q' when q' excludes at least what q excludes (q' is at least as strict). Admit^{q,r} is antitone in (q,r). A task with a realization, owned or not, at (q,r) is in Admit^{q,r} (so (CT3) follows from the definitions).

**Other choices.** (a) Admit given by the physical module with no stated link to realizations (then (CT3) is an assumption).

**Used by:** claims of this part: FC93.

### I74 · Recursive capacity: target chains and enabling continuations

Fills in for:

> L492 | \forall n<\omega\ \forall\text{ admitted target chains of length }n,\ \exists\text{ an owned enabling continuation}.

**Invented.** A target chain of length n is a sequence d1, …, dn of aspects of the system's practice, each d(i+1) a description of di made a represented target, each step admitted by the physical module; an owned enabling continuation is an owned continuation in which dn becomes a represented target, criticism is directed at it and the result can change its operative use (L487).

**Other choices.** (a) chains of scrutiny of one aspect repeated n times.

**Used by:** claims of this part: FC94, FC110.

### I75 · The explanatory contents 𝔈_Θ

Fills in for:

> L497 | With \(\mathfrak E_\Theta\) the explanatory contents that some carrier can hold under the physical module

**Invented.** 𝔈_Θ := {c : for some p, t, Γ, Account((c,p,t,Γ)), and the physical module admits some carrier instantiating c}. It is taken to be infinite where FC94 needs it.

**Other choices.** (a) contents that some carrier holds at present.

**Used by:** claims of this part: FC94, FC110.

### I97 · Tasks and executions on finite state sets

Fills in for:

*(L466, quoted above.)*

**Invented.** At most 4 constructor states, 2 inputs, 3 outputs; each (state, input) has one or two executions, each a triple (completes, output, final state) drawn at random; Exec is nonempty everywhere (L469's standing assumption).

**Other choices.** (a) executions as infinite traces (with 'completes' a property of the trace).

**Used by:** claims of this part: FC91, FC92.

### I98 · Tolerances as a 3 × 3 grid of performance and retention

Fills in for:

> L479 | The tolerances of the physical module (Part XIV) form a directed preorder \(Q_\Theta\)

**Invented.** Performance and retention tolerances are each 0 < 1 < 2 (stricter is larger); Admit and the realized tasks are random antitone families of four tasks; Cap is a random subset of the realized tasks.

**Other choices.** (a) a preorder that is not a product of chains. (b) tolerances with no exact member, approached as a limit.

**Used by:** claims of this part: FC93.

## 6. Choices no register entry records

Found by the two checks. U-entries come from the check that re-ran the program; H-entries from the check that read the maths against the text, in its wording.

### H16 · "can affect its operative use" read as "on an active route" (D16.1)

> L487 | the result can affect its operative use.

- **Added.** D16.1 reads it as "a result on an active route to d's operative use". I74, which quotes L487's own wording, keeps "can change its operative use".
- **Depends on it.** (RC); FC94, not tested.

## 7. Sentences of this group the maths could not write

**NF11** (L495). Why it was not formalized: 'Independently characterized' and 'non-question-begging' are not defined.

> L495 | An explanatory barrier is an independently characterized domain for which every admitted, non-question-begging enabling condition leaves the relevant capability unavailable.

**NF12** (L497). Why it was not formalized: 'Coherently posed' and 'advanceable' are not defined, so (U2)'s domain is open.

> L497 | the coherently posed advanceable challenges

**NF16** (L51). Why it was not formalized: Strong candidate L51.s1: a pointer; formal content only the typing of 𝒩 ⊆ Act × Occ × Rsn × V_A as an input.

> L51 | **8. "Where is aesthetics?"** In Part XI, as a declared appraisal relation.

**NF17** (L517). Why it was not formalized: Strong candidate L517.s1: a signature of types for the import, not a claim.

> L517 | 1. The **physical module** \(\Theta\): substrate state spaces, attributes, admitted processes, controlled-action interpretation, resources, tolerances, and \(\operatorname{Org}_\ell\), the organization a physical occurrence instantiates at a grain.

## 8. Round 1: matters noted and changes made

In the first review round, readers tried to vary sentences that had stood unchanged; the rulings changed four lines and recorded fourteen matters outside the sentences examined, left for later rounds.

**The round-1 change at L471.** Before:

> L471 (before round 1) | **Retention fixed point.** \(F(C)\) = states whose executions all complete and return into \(C\). \(F\) is monotone; \(C\subseteq F(C)\) is the invariant form; the union of post-fixed sets is the greatest fixed point. (CT2)

After, as the text now stands:

> L471 | **Retention fixed point.** \(F(C)\) = states whose executions all complete and return into \(C\). \(F\) is monotone; \(C\subseteq F(C)\) is the invariant form; the greatest fixed point is the union of the sets \(D\) with \(D\subseteq F(D)\). (CT2)

**Round-1 matter 10.** "complete" in L471's first sentence must be read as (CT1)'s "completes with o∈T[i]" for clause 2 of (CT2) to be (CT1).

**Round-1 matter 14.** L27 gives no pointer to Part XIV where L23 and L25 give theirs.

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
