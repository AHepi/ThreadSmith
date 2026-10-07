# The maths against the words, part 10 of 17: Conflict and rivals

## 1. What you are asked to do

**The text** is a theory of explanation: a formal semantics of what an explanation is and of explanatory creativity, 632 lines, which calls itself "the semantics". Its owner took the decisions in section 2, and asked for "exploring the math a bit more" since "words are vague", adding: "if implementation forces invention, that needs to be recorded" (S36).

**The maths.** The text's definitions were written as mathematics beside the sentences they formalize (D0.1–D18.2; its worked cases encoded as E1–E9). The claims these let one state (FC01–FC110) were each put to a program that searched small finite models for a counterexample. Every choice the maths or the program made that the text does not fix was recorded as an **invention** (I01–I102), with the other choices that were possible. Two checks followed: one re-ran every counterexample and worked it by hand; the other read the maths against the text. They found further choices no entry records (U1–U6 and H01–H20). **Nothing invented is the text's own content.** A counterexample that rests on an invention tells against that way of writing the text, and against the text only where the text fixes what the invention fills in.

**This part** covers conflict, rivals and conflict with a claim in Part VI of the text (L315): the definitions in section 3; 6 claims (FC43, FC44, FC45, FC52, FC53, FC54) with their results in section 4; the inventions they rest on in section 5 (7 in full); the unrecorded choices in section 6; sentences the maths could not write in section 7; round-1 matters and changes in section 8. The whole is put to readers in 17 parts, each read on its own.

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

### §8 Conflict, rivals, conflict with a claim

> L315 | Two candidates **conflict** at such a pair \((a,b)\) when their answers there differ, or when each of them could meet (F1), (F2) and (A) there under some relations of the target's components at that pair, each a relation on the component's footprint (Part II), and no such relations let both

**D8.1 Meeting at a pair under hypothetical relations.** For a pair (a,b) and R = (R_j)_{j∈J_D} with R_j ⊆ ∏_{v∈V_j} X_v: D^R is D with L_j(a,b) replaced by R_j; Ans^R_p(a,b) := Q(D^R, a, b; δ_D). Meets_ab(ℰ, R) :⟺ for every k ∈ Γ, proj^λ_{V_k}[Sol^R_{N_k}(a,b)] = L^E_k(τ(a),σ(b)); π[Sol_{D^R}(a,b)] = Sol_E(τ(a),σ(b)); and Ans_E(τ(a),σ(b)) = Ans^R_p(a,b) **[I19]**. BothMeet_ab(R) :⟺ Meets_ab(ℰ,R) ∧ Meets_ab(ℰ',R).

**D8.2 Conflict.** For a pair (a,b) of the target that both transports translate, in C or outside it: Conf(ℰ, ℰ'; a,b) :⟺ Ans_E(τ(a),σ(b)) ≠ Ans_E'(τ'(a),σ'(b)) ∨ [∃R Meets_ab(ℰ,R) ∧ ∃R' Meets_ab(ℰ',R') ∧ ¬∃R'' BothMeet_ab(R'')].

> L315 | Whether two candidates conflict depends on their organizations and transports and on the target's ports and components, not on anyone's view of them; it is found by argument, with no test, and it does not turn on what any physics admits (Part I).

R ranges over every assignment of relations on the footprints; no physical module enters D8.1–D8.2.

> L315 | Two explanatory candidates for one question \(p\) are **rivals** when one of them has been offered as an answer to \(p\) in place of the other and they conflict at some admitted edit–boundary pair of the target that both their transports translate, in \(C\) or outside it.

> L315 | No list of all rivals is supposed: a candidate's rivals are among the candidates someone has offered, and a candidate that nobody has offered is no one's rival.

**D8.3 Offer; rivals.** Offered(ℰ, ℰ', p) is a primitive: a record that ℰ was offered for p in place of ℰ' **[I33]**. Riv(ℰ, ℰ'; p) :⟺ [Offered(ℰ,ℰ',p) ∨ Offered(ℰ',ℰ,p)] ∧ Conf(ℰ,ℰ'; a,b) for some pair both translate. Riv is a two-place relation; nothing here ranges over the rivals of a candidate.

> L315 | A candidate offered for \(p\) is offered for the whole of \(p\): it claims (F1), (F2) and (A) at every pair of \(C\), tested or not, and the rest of (E) on \(C\); outside \(C\) it claims nothing on \(p\)

A candidate offered for p is the claim Acc(ℰ) on p.

> L315 | \(\chi\) need not be an explanation or come with one, and it may be a claim about what is possible or impossible: the bare claim that perpetual motion is impossible is enough for a conflict with a candidate whose organization gives perpetual motion.

**D8.4 A claim at a pair.** A claim χ is given, at each pair, by Allow_χ(a,b), a set of assignments R of relations to the target's components (the behaviours χ allows), and by Applies(χ, a, b) ∈ {yes, no}, the premise that χ speaks of the target under that pair's edit **[I34]**. A claim about what is possible or impossible enters only through Allow_χ: here, and only here in §§1–10, physical possibility is content.

> L315 | A candidate **conflicts with** a claim \(\chi\) at an admitted pair of the target that its transport translates, in \(C\) or outside it, when \(\chi\) excludes what the candidate's organization and transport give there: its answer, or every relation of the target's components under which it could meet (F1), (F2) and (A) there.

**D8.5 Conflict with a claim.** ConfCl(ℰ, χ; a,b) :⟺ [every R with Ans^R_p(a,b) = Ans_E(τ(a),σ(b)) lies outside Allow_χ(a,b)] ∨ [every R with Meets_ab(ℰ,R) lies outside Allow_χ(a,b)].

> L315 | Two candidates that some relations of the target's components would let both meet (F1), (F2) and (A) at a pair, when \(\chi\) excludes every such relation, conflict there given \(\chi\)

**D8.6 Conflict given χ; rivals given χ.** ConfG_χ(ℰ, ℰ'; a,b) :⟺ some R has BothMeet_ab(R), and every such R lies outside Allow_χ(a,b) **[I35]**. Riv_χ(ℰ, ℰ'; p) :⟺ one offered in place of the other ∧ ConfG_χ at some pair.

**Vague.** 'One counterpart' is not fixed [I36]. What a claim is, and how it 'excludes', are not given beyond the example [I34]. 'Offered' has no definition and is not a declared input [I33].

## 4. The claims, with their search results

Each claim: its type, the inventions it uses, its sentences quoted, its formal statement, and its result, part by part; for a counterexample, what it shows and, where short, the model; then the second check's note, and every invention the result rests on (the claim's own and the program's).

### FC43 · Conflict, rivals, problems and 'easy to vary' are symmetric

*a result the text states.* Inventions it uses: I33, I37.

> L317 | the rival is then easy to vary too

**Formal.** Conf(ℰ,ℰ';a,b) ⟺ Conf(ℰ',ℰ;a,b); Riv is symmetric (either offered in place of the other, I33); so Prob_j and its kind are symmetric, and ETV_j(ℰ) through ℰ' gives ETV_j(ℰ').

**Result: HOLDS ON ALL MODELS TRIED.**

- *symmetry* (for all): **holds on all models tried** (3,837 models).

**Rests on:** I33, I37, I77, I78, I81, I86.

### FC44 · Two commitments with one counterpart and different relations cannot both meet (F1)

*a result the text states.* Inventions it uses: I14, I19, I36.

> L315 | as none do when two of their active components with one counterpart have different relations there.

**Formal.** Under I36: if k ∈ Γ and k' ∈ Γ' have one counterpart and different relations at (a,b), then no R gives F1_ab(ℰ,R) ∧ F1_ab(ℰ',R). Under the reading 'one counterpart = the same subnetwork', there are ℰ, ℰ', R meeting both with different relations.

**Result: HOLDS ON ALL MODELS TRIED.**

- *under I36* (for all): **holds on all models tried** (3,641 models).
- *the reading 'one counterpart = the same subnetwork'* (there is): **witness found** (9 models).
  Searched: there are ℰ, ℰ', R with one subnetwork as counterpart, different relations, both meeting (F1)
  One subnetwork {h_p0} is the counterpart of k in both candidates, through different port translations (v := p0 and v := p1). At (1,b0) the two relations differ and both meet (F1) under the target's own relations: the clause of L315 ('none do when two of their active components with one counterpart have different relations there') needs I36's reading of 'one counterpart'.

**Rests on:** I14, I19, I36, I77, I78, I81, I101.

### FC45 · Recoded candidates, and candidates some relations let both meet, conflict nowhere

*a result the text states.* Inventions it uses: I17, I19, I20, I70.

> L315 | Two candidates that differ only in how they are written, one carried onto the other by a structure-preserving bijection that takes its transport with it and leaves its answers as they are, conflict at no pair

**Formal.** (a) If φ: E ≅ E' with t' = φ∘t, Γ' = φ[Γ] and Ans_E'(φa',φb') = Ans_E(a',b'), then ¬Conf(ℰ,ℰ';a,b) at every pair both translate. (b) If at every such pair some R lets both meet, they conflict nowhere.

**Result: HOLDS ON ALL MODELS TRIED.**

- *(a) recoded candidates* (for all): **holds on all models tried** (2,879 models).
- *(b) some R lets both meet at every pair ⇒ no conflict* (by construction): **holds by construction**.

**Rests on:** I17, I19, I20, I70, I77, I78, I81.

### FC52 · Conflict with a claim: the first disjunct implies the second

*follows from the definitions as written.* Inventions it uses: I19, I34.

> L315 | when \(\chi\) excludes what the candidate's organization and transport give there: its answer, or every relation of the target's components under which it could meet (F1), (F2) and (A) there.

**Formal.** Under I34: if χ excludes ℰ's answer at (a,b), then χ excludes every R with Meets_ab(ℰ,R) (Meets includes (A) at the pair, so the answer under such R is ℰ's answer). The definition reduces to its second disjunct.

**Result: HOLDS ON ALL MODELS TRIED.**

- *first disjunct implies the second* (for all): **holds on all models tried** (1,919 models).

**Rests on:** I19, I34, I77, I78, I81.

### FC53 · Conflict with a claim rules a candidate out only with the premise that the claim speaks of the target

*a result the text states.* Inventions it uses: I34, I38, I40.

> L315 | Where the pair is in \(C\), that argument rules out that the candidate meets (E) for any assessor \(j\) who can use it, and so who tentatively accepts \(\chi\) (K2)

> L315 | Either way the argument needs the premise that \(\chi\) speaks of the target under that pair's edit.

> L315 | without that premise the argument rules out no candidate there; the candidate still conflicts with \(\chi\).

**Formal.** (a) If ConfCl(ℰ,χ;a,b), (a,b) ∈ C, Applies(χ,a,b), χ and Applies live for j, forms admitted: X_j(Acc(ℰ)) ≠ ∅. (b) There is a model (the text's pendulum, its friction component deleted by the edit) with ConfCl(ℰ,χ;a,b), ¬Applies(χ,a,b), and no argument from χ in X_j(Acc(ℰ)).

**Result: HOLDS ON ALL MODELS TRIED.**

- *(a) with Applies* (computation): **computed: as claimed**.
- *(b) the pendulum without Applies* (computation): **computed: as claimed**.

**Rests on:** I34, I38, I40, I87, I88, I89, I90.

### FC54 · Rivals given χ conflict nowhere without χ at that pair

*follows from the definitions as written.* Inventions it uses: I19, I33, I34, I35.

> L315 | Two candidates offered one in place of the other that conflict at a pair given \(\chi\) are **rivals given \(\chi\)**: for an assessor who tentatively accepts \(\chi\) they pose a problem for \(p\) as rivals do (Problems, below), and for one who does not, they pose none on that account.

**Formal.** Riv_χ(ℰ,ℰ';p) := Offered ∧ ∃(a,b) ConfG_χ(ℰ,ℰ';a,b); Prob_{χ,j} := Riv_χ ∧ χ ∈ Accepted_j ∧ neither ruled out for j. Claim: ConfG_χ(a,b) ⇒ ¬Conf(a,b) (some R lets both meet, so their answers agree and the second disjunct of Conf fails). So a pair of rivals given χ that conflicts at no other pair is not a pair of rivals.

**Result: HOLDS ON ALL MODELS TRIED.**

- *conflict given χ excludes conflict* (for all): **holds on all models tried** (1,919 models).

**Rests on:** I19, I33, I34, I35, I77, I78, I81.

## 5. The inventions these rest on

In full: each invention this part is the first of the parts to use. Then, for an invention given in full in another part that a counterexample here rests on, what was invented. Then the rest by title. I77 and I78, the bounds and families of the search, are described in section 1 and given in full in another part.

### I19 · Meeting (F1), (F2) and (A) at one pair under hypothetical relations of the target

Fills in for:

> L315 | when their answers there differ, or when each of them could meet (F1), (F2) and (A) there under some relations of the target's components at that pair, each a relation on the component's footprint (Part II), and no such relations let both

**Invented.** For a pair (a,b) and an assignment R = (R_j)_{j in J_D}, R_j ⊆ ∏_{V_j} X_v: D^R is D with its relations at (a,b) replaced by R; Meets_ab(ℰ,R) is (F1) at (a,b) for every k in Γ with Sol_λ(k) computed from R, the valuation equation of (F2) with Sol_D^R, and (A) with the target's answer computed by the query on D^R. The homomorphism clause is left out at a pair (I18). R ranges over every assignment of relations on the footprints.

**Other choices.** (a) include the homomorphism clause. (b) R ranging only over assignments some physics admits (L315 excludes it: 'it does not turn on what any physics admits'). (c) R ranging over the relations the target has at other admitted pairs.

**Used by:** claims of this part: FC44, FC45, FC52, FC54; 2 other claims.

### I33 · The offer of one candidate in place of another: a primitive

Fills in for:

> L315 | Two explanatory candidates for one question \(p\) are **rivals** when one of them has been offered as an answer to \(p\) in place of the other

**Invented.** Offered(ℰ, ℰ', p) is a primitive relation (a record of offers), not defined in the formal core; rivals are symmetric (either one offered in place of the other).

**Other choices.** (a) offers as events in histories, read through the physical module. (b) offers as a declared input (L522 does not list them).

**Used by:** claims of this part: FC43, FC54; 3 other claims.

### I34 · A claim χ as a set of allowed behaviours at a pair, and the premise that it speaks of the target

Fills in for:

*(L315, quoted above.)*

*(L315, quoted above.)*

**Invented.** At each pair, χ is modelled as a set Allow_χ(a,b) of assignments R of relations to the target's components (the behaviours χ allows). 'χ excludes its answer' := every R whose query answer is Ans_E(τ(a),σ(b)) lies outside Allow_χ(a,b). 'χ excludes every relation under which it could meet' := every R with Meets_ab(ℰ,R) lies outside Allow_χ(a,b). The premise that χ speaks of the target under the pair's edit is a separate yes/no input Applies(χ,a,b).

**Other choices.** (a) χ as a sentence of a language with its own semantics, related to behaviours by a declared reading. (b) χ as constraining answers only (then the second disjunct cannot be expressed).

**Used by:** claims of this part: FC52, FC53, FC54; 1 other claim.

### I35 · Conflict given χ: no requirement that each candidate can meet under χ

Fills in for:

*(L315, quoted above.)*

**Invented.** ConflictGiven_χ(ℰ,ℰ';a,b) := some R lets both meet at (a,b), and every such R lies outside Allow_χ(a,b). Nothing is required of what each can meet under χ alone.

**Other choices.** (a) the second disjunct of plain conflict with R restricted to Allow_χ: each can meet under some allowed R, and no allowed R lets both.

**Used by:** claims of this part: FC54.

### I36 · 'Two of their active components with one counterpart'

Fills in for:

*(L315, quoted above.)*

**Invented.** k in Γ and k' in Γ' have one counterpart when λ(k) = λ'(k') as subnetworks, their port translations have the same image, and θ'^-1∘θ is a bijection V_k → V_k' with matching value maps; 'different relations there' means L_k'(τ'(a),σ'(b)) ≠ β_*(L_k(τ(a),σ(b))) under that bijection β.

**Other choices.** (a) one counterpart = the same subnetwork, whatever the port translations (then the clause can fail: the translations can carry one projected relation to two different relations).

**Used by:** claims of this part: FC44.

### I86 · Every pair of candidates examined counts as offered one in place of the other

Fills in for:

*(L315, quoted above.)*

**Invented.** The primitive Offered (I33) is taken to hold, both ways, of every pair of candidates a test examines; rivals are then the pairs that conflict somewhere both translate.

**Other choices.** (a) Offered drawn at random (it would test nothing about conflict). (b) Offered held of no pair (then there are no rivals).

**Used by:** claims of this part: FC43; 2 other claims.

### I88 · X_j ranges over a finite set of arguments; an argument has a step

Fills in for:

> L397 | An argument is an argument tree: argument steps whose leaves are premises, which are record leaves or stated assumptions and definitions.

**Invented.** X_j(ψ) is computed over a finite set of arguments: those a test builds, or every tree of height at most 2 or 3 over the given premises with the admitted forms. An argument with no step (a bare leaf) is no argument. So 'no argument rules it out' is shown only over that set.

**Other choices.** (a) every argument over the premises (infinite; decidable only by a search over deductions). (b) a bare premise counts as an argument.

**Used by:** claims of this part: FC53; 3 other claims.

Named by title only (given in full in another part): I14, Subnetworks, their solutions, and port translations with value maps; I17, Partial τ and σ; which pairs a transport 'translates'; I20, How the fixed query is applied to a candidate's organization; I37, 'Easy to vary' is relative to an assessor; I38, Claims, their denials, and 'inconsistent with its conclusion'; I40, Live through a step: a step below, and essential premises; I70, A structure-preserving bijection of all the data (Argument 8); I77, Finite models and the bounds of the search; I78, Two families of generated organizations: surgical edits with override, and free edits; I81, Transports as port translations; computed ports; generated candidates; the transport space searched for ≡; I87, Claims as propositional formulas, read structurally; I89, The inference forms: MP, MT, AND-introduction, AND-elimination and a free form; I90, The physical module supplied by hand: histories and provenance as free predicates; I101, Which models count as witnesses: the proper-model filter.

## 6. Choices no register entry records

Found by the two checks. U-entries come from the check that re-ran the program; H-entries from the check that read the maths against the text, in its wording.

None bears on this part's claims.

## 7. Sentences of this group the maths could not write

None beyond those named under the claims.

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
