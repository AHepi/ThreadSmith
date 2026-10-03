# The maths against the words, part 11 of 17: Problems, tests and easy to vary

## 1. What you are asked to do

**The text** is a theory of explanation: a formal semantics of what an explanation is and of explanatory creativity, 632 lines, which calls itself "the semantics". Its owner took the decisions in section 2, and asked for "exploring the math a bit more" since "words are vague", adding: "if implementation forces invention, that needs to be recorded" (S36).

**The maths.** The text's definitions were written as mathematics beside the sentences they formalize (D0.1–D18.2; its worked cases encoded as E1–E9). The claims these let one state (FC01–FC110) were each put to a program that searched small finite models for a counterexample. Every choice the maths or the program made that the text does not fix was recorded as an **invention** (I01–I102), with the other choices that were possible. Two checks followed: one re-ran every counterexample and worked it by hand; the other read the maths against the text. They found further choices no entry records (U1–U6 and H01–H20). **Nothing invented is the text's own content.** A counterexample that rests on an invention tells against that way of writing the text, and against the text only where the text fixes what the invention fills in.

**This part** covers problems, tests and the text's own 'easy to vary' in Part VI of the text (L317), with Argument 2's consequence (L568): the definitions in section 3; 7 claims (FC46, FC47, FC48, FC49, FC50, FC51, FC55) with their results in section 4; the inventions they rest on in section 5 (1 in full); the unrecorded choices in section 6; sentences the maths could not write in section 7; round-1 matters and changes in section 8. The whole is put to readers in 17 parts, each read on its own.

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

### §10 Problems and easy to vary

> L317 | **Problems.** Two rivals, neither of them ruled out for an assessor, pose, for that assessor, a **problem for \(p\)**: a conflict between ideas that no argument usable by that assessor has decided.

**D10.1 Problem.** Prob_j(ℰ, ℰ'; p) :⟺ Riv(ℰ, ℰ'; p) ∧ NotOut_j('Acc(ℰ)') ∧ NotOut_j('Acc(ℰ')').

> L317 | (i) The rivals conflict at some \((a,b)\in C\).

> L317 | (ii) They conflict at no pair of \(C\), only at admitted pairs outside it: the contract does not contain their conflict.

**D10.2 The two kinds.** Kind i :⟺ Conf at some (a,b) ∈ C. Kind ii :⟺ Conf at no pair of C, and at some pair outside C that both translate.

> L317 | recording it, the target's relations as well as its answer where their answers there agree, is a **test**.

**D10.3 Test.** A record at (a,b) ∈ C: the recorded relations R* of the target's components there and the recorded answer, with its premises about background and instruments (K3). The argument from it: 'R* at (a,b); Meets_ab(ℰ, R*) fails; Acc(ℰ) requires it'.

> L317 | A candidate is **easy to vary**, in the sense used here, when it and a rival pose a problem of the second kind;

**D10.4 Easy to vary.** ETV_j(ℰ; p) :⟺ Prob_j(ℰ, ℰ'; p) of kind ii for some ℰ' **[I37]**. This is the text's 'easy to vary' only; what hard to vary covers is parked (S33–S34), and nothing here extends to it.

> L315 | for an assessor who tentatively accepts \(\chi\) they pose a problem for \(p\) as rivals do (Problems, below), and for one who does not, they pose none on that account.

**D10.5 Problem given χ.** Prob_{χ,j}(ℰ, ℰ'; p) :⟺ Riv_χ(ℰ, ℰ'; p) ∧ χ ∈ Accepted_j(ξ) ∧ neither is ruled out for j.

> L317 | Solving a problem so rules one rival out for that assessor while the argument stays usable for that assessor.

**D10.6 Solved.** A problem for j is solved while Out_j('Acc(ℰ)') or Out_j('Acc(ℰ')') holds. Where the argument uses a claim taken as given, that is j's choice (D9.8).

### Definitions from other sections that these claims use

> L315 | Two candidates **conflict** at such a pair \((a,b)\) when their answers there differ, or when each of them could meet (F1), (F2) and (A) there under some relations of the target's components at that pair, each a relation on the component's footprint (Part II), and no such relations let both

**D8.1 Meeting at a pair under hypothetical relations.** For a pair (a,b) and R = (R_j)_{j∈J_D} with R_j ⊆ ∏_{v∈V_j} X_v: D^R is D with L_j(a,b) replaced by R_j; Ans^R_p(a,b) := Q(D^R, a, b; δ_D). Meets_ab(ℰ, R) :⟺ for every k ∈ Γ, proj^λ_{V_k}[Sol^R_{N_k}(a,b)] = L^E_k(τ(a),σ(b)); π[Sol_{D^R}(a,b)] = Sol_E(τ(a),σ(b)); and Ans_E(τ(a),σ(b)) = Ans^R_p(a,b) **[I19]**. BothMeet_ab(R) :⟺ Meets_ab(ℰ,R) ∧ Meets_ab(ℰ',R).

**D8.2 Conflict.** For a pair (a,b) of the target that both transports translate, in C or outside it: Conf(ℰ, ℰ'; a,b) :⟺ Ans_E(τ(a),σ(b)) ≠ Ans_E'(τ'(a),σ'(b)) ∨ [∃R Meets_ab(ℰ,R) ∧ ∃R' Meets_ab(ℰ',R') ∧ ¬∃R'' BothMeet_ab(R'')].

> L315 | Two explanatory candidates for one question \(p\) are **rivals** when one of them has been offered as an answer to \(p\) in place of the other and they conflict at some admitted edit–boundary pair of the target that both their transports translate, in \(C\) or outside it.

> L315 | No list of all rivals is supposed: a candidate's rivals are among the candidates someone has offered, and a candidate that nobody has offered is no one's rival.

**D8.3 Offer; rivals.** Offered(ℰ, ℰ', p) is a primitive: a record that ℰ was offered for p in place of ℰ' **[I33]**. Riv(ℰ, ℰ'; p) :⟺ [Offered(ℰ,ℰ',p) ∨ Offered(ℰ',ℰ,p)] ∧ Conf(ℰ,ℰ'; a,b) for some pair both translate. Riv is a two-place relation; nothing here ranges over the rivals of a candidate.

> L315 | A claim is **ruled out** for an assessor \(j\) when an argument usable by \(j\) (Part IX) rules it out, and a candidate is ruled out for \(j\) when the claim that it meets (E) is;

> L315 | A candidate is **not ruled out** for \(j\) when no argument usable by \(j\) rules it out.

**D9.8 Ruled out; not ruled out.** X_j(φ) := {α : Usable_j(α) ∧ RO(α, φ)}. Out_j(φ) :⟺ X_j(φ) ≠ ∅; NotOut_j(φ) :⟺ X_j(φ) = ∅. A candidate ℰ is ruled out for j :⟺ Out_j('Acc(ℰ)').

## 4. The claims, with their search results

Each claim: its type, the inventions it uses, its sentences quoted, its formal statement, and its result, part by part; for a counterexample, what it shows and, where short, the model; then the second check's note, and every invention the result rests on (the claim's own and the program's).

### FC46 · A conflict inside the contract: at most one account

*a result the text states.* Inventions it uses: I19, I21.

> L317 | (i) The rivals conflict at some \((a,b)\in C\). Whatever the target does there, at most one of them is an account of \(p\), whether or not anyone records what it does;

> L317 | Two rivals that are both accounts on \(C\) conflict only outside it

**Formal.** ∀ℰ,ℰ' ∀(a,b)∈C: Conf(ℰ,ℰ';a,b) ⇒ ¬(Acc(ℰ) ∧ Acc(ℰ')). (If both met (E), both would meet (F1), the (F2) equation and (A) at (a,b) under the target's own relations R*: equal answers, and R* lets both.) So two accounts on C conflict at no pair of C.

**Result: HOLDS ON ALL MODELS TRIED.**

- *two accounts do not conflict in C* (for all): **holds on all models tried** (722 models).

**Rests on:** I19, I21, I77, I78, I81, I85.

### FC47 · A test at a conflict pair rules out at least one, for an assessor who can use it

*a result the text states.* Inventions it uses: I19, I38, I40, I42, I43.

> L317 | recording it, the target's relations as well as its answer where their answers there agree, is a **test**. Whatever it records, an argument from what it records rules out at least one of them for an assessor who can use it

**Formal.** (a) Conf(ℰ,ℰ';a,b) ⇒ ∀R ¬(Meets_ab(ℰ,R) ∧ Meets_ab(ℰ',R)); so for the recorded R*, Meets_ab fails for at least one. (b) For j who admits the forms used, whose scope holds (a,b), and for whom the record's premises about background and instruments are live, the argument 'R* at (a,b); Meets_ab(·,R*) fails; Acc requires it' puts a member in X_j(Acc(ℰ)) or in X_j(Acc(ℰ')).

**Result: HOLDS ON ALL MODELS TRIED.**

- *(a) conflict excludes joint meeting* (for all): **holds on all models tried** (2,879 models).
- *(b) the argument from a test's record* (computation): **computed: as claimed**.

**Rests on:** I19, I38, I40, I42, I43, I77, I78, I81, I87, I88, I89.

### FC48 · No conflict inside the contract: answers agree there

*a result the text states.* Inventions it uses: I21.

> L317 | (ii) They conflict at no pair of \(C\), only at admitted pairs outside it: the contract does not contain their conflict. Their answers then agree at every pair of \(C\), so no argument from an answer recorded in \(C\) rules out one of them without the other;

**Formal.** If ¬Conf(ℰ,ℰ';a,b) at every (a,b) ∈ C, then Ans_E(τa,σb) = Ans_E'(τ'a,σ'b) at every (a,b) ∈ C (⊥ = ⊥, I21); so for any recorded answer at (a,b), (A) there holds for both or for neither.

**Result: HOLDS ON ALL MODELS TRIED.**

- *no conflict in C ⇒ answers agree* (for all): **holds on all models tried** (2,879 models).

**Rests on:** I21, I77, I78, I81.

### FC49 · The two kinds of problem exclude each other and cover every pair of rivals

*follows from the definitions as written.* Inventions it uses: I16, I17, I33.

> L317 | (ii) They conflict at no pair of \(C\), only at admitted pairs outside it

**Formal.** Riv(ℰ,ℰ';p) ⇒ exactly one of: some pair of C is a conflict pair; no pair of C is, and some translated pair outside C is.

**Result: HOLDS ON ALL MODELS TRIED.**

- *exactly one kind* (for all): **holds on all models tried** (2,879 models).

**Rests on:** I16, I17, I33, I77, I78, I81, I86.

### FC50 · A finer contract makes a problem of the first kind; a narrowed one leaves the problem on p

*a result the text states.* Inventions it uses: I11, I33.

> L317 | A finer contract that contains a change at which two rivals conflict makes a new question (Part III), on which, offered for it, they pose a problem of the first kind while neither is ruled out;

> L317 | A contract narrowed to leave out the pairs at which two rivals conflict also makes a different question; it solves nothing on \(p\), and the problem for \(p\) remains until at least one of them is ruled out for that assessor.

**Formal.** (a) If Conf(ℰ,ℰ';a,b) with (a,b) ∉ C, p' is p with C' ⊇ C ∪ {(a,b)}, and ℰ, ℰ' are offered for p' with neither ruled out for j, then Prob_j(ℰ,ℰ';p') is of the first kind. (b) For C'' ⊆ C leaving out every conflict pair, p'' ≠ p, and Prob_j(ℰ,ℰ';p) is a function of p's data and j alone, unchanged by anything about p''.

**Result: HOLDS ON ALL MODELS TRIED.**

- *(a) a finer contract makes kind (i)* (for all): **holds on all models tried** (2,880 models).
- *(b) a narrowed contract leaves the problem on p* (by construction): **holds by construction**.

**Rests on:** I11, I33, I77, I78, I81, I86.

### FC51 · A change that separates two accounts lies outside their shared contract

*a result the text states.* Inventions it uses: I18, I24, I27.

> L317 | a claim that one of them and not the other meets (E) on a contract with some admitted change outside \(C\) is a claim that such a change separates them, and must supply it

> L568 | Where two candidates that meet (F1), (F2) and (A) differ only in which component has which counterpart, the contract does not contain the distinction

**Formal.** (a) If Acc(ℰ) and Acc(ℰ') on C, C' ⊋ C, Acc(ℰ) on C' and ¬Acc(ℰ') on C', then some (a,b) ∈ C'∖C has ¬(F1 ∧ (F2) equation ∧ A)_ab(ℰ'), or τ' fails the homomorphism clause on edits new in C', or the scope statements differ (NC1 and NC2 carry over from C to C'; Sol_D(1,b0) is unchanged). (b) If ℰ' is ℰ with λ' = λ∘ψ for a permutation ψ of Γ and both meet (F1) on C, then for every k and (a,b) ∈ C the projected relations of λ(k) and λ(ψk) agree under the port translations: no pair of C separates the two pairings.

**Result: HOLDS ON ALL MODELS TRIED.**

- *(a) separation lies in C'∖C* (for all): **holds on all models tried** (20,665 models).
- *(b) two pairings* (for all): **holds on all models tried** (8,884 models).

**Rests on:** I18, I24, I27, I77, I78, I81, I85.

### FC55 · Nothing in Part VI counts rivals or orders candidates

*follows from the definitions as written.* Inventions it uses: none.

> L317 | Nothing here counts rivals or orders candidates: of one candidate, what is said is whether it meets (E) on a contract and whether it is ruled out for an assessor; of two, whether they conflict; of a candidate and a claim, whether they conflict.

**Formal.** Syntactic: every predicate of §§8–10 takes at most two candidates, or one candidate and one claim; none takes a set of candidates, a cardinality or an order on candidates.

**Result: HOLDS ON ALL MODELS TRIED.**

- *syntactic: no predicate of Part VI takes more than two candidates* (computation): **computed: as claimed**.

**Rests on:** no invention.

## 5. The inventions these rest on

In full: each invention this part is the first of the parts to use. Then, for an invention given in full in another part that a counterexample here rests on, what was invented. Then the rest by title. I77 and I78, the bounds and families of the search, are described in section 1 and given in full in another part.

### I37 · 'Easy to vary' is relative to an assessor

Fills in for:

> L317 | A candidate is **easy to vary**, in the sense used here, when it and a rival pose a problem of the second kind

**Invented.** ETV_j(ℰ) := for some ℰ', Problem_j(ℰ,ℰ';p) holds and is of the second kind. It inherits the assessor from 'problem'. (What hard to vary covers is parked by decisions S33–S34; this formalization touches only the text's 'easy to vary' and adds nothing about it.)

**Other choices.** (a) assessor-free: some rival conflicts with it only outside C, ruled out or not. (b) for some assessor.

**Used by:** 1 other claim.

Named by title only (given in full in another part): I11, 'Coarser' and 'finer' contracts: fewer and more pairs; I16, The domain of π: 'on the stated scope'; I17, Partial τ and σ; which pairs a transport 'translates'; I18, The homomorphism clause of (F2): its range, and that it is not pointwise; I19, Meeting (F1), (F2) and (A) at one pair under hypothetical relations of the target; I21, Undetermined answers: a value ⊥; I24, NC1: the target's answer as an unanalysed boundary input or component, read structurally; I27, The stated scope: a declared statement over pairs; I33, The offer of one candidate in place of another: a primitive; I38, Claims, their denials, and 'inconsistent with its conclusion'; I40, Live through a step: a step below, and essential premises; I42, Scope_j: within the declared contract, grain and boundary; I43, (K3): what it adds and what 'nothing narrower' says; I77, Finite models and the bounds of the search; I78, Two families of generated organizations: surgical edits with override, and free edits; I81, Transports as port translations; computed ports; generated candidates; the transport space searched for ≡; I85, The default scope statement states every excluded pair; I86, Every pair of candidates examined counts as offered one in place of the other; I87, Claims as propositional formulas, read structurally; I88, X_j ranges over a finite set of arguments; an argument has a step; I89, The inference forms: MP, MT, AND-introduction, AND-elimination and a free form.

## 6. Choices no register entry records

Found by the two checks. U-entries come from the check that re-ran the program; H-entries from the check that read the maths against the text, in its wording.

### H10 · "differ" read two ways (D8.2 against D6.4)

> L315 | Two candidates **conflict** at such a pair \((a,b)\) when their answers there differ

> L255 | the answer of \(E\) at \((\tau(a),\sigma(b))\) differs from its answer at \((1,\sigma(b_0))\)

- **Added.**
  - In D8.2 (and `conflict()` in the program), an undetermined answer ⊥ differs from a determined one.
  - In D6.4 (I22), "differs" holds only between two determined answers.
  - I21 records only that ⊥ = ⊥. Neither entry records the choice for L315, or that the same word gets two readings.
- **Depends on it.** FC48 holds because a pair with answers 0 and ⊥ is a conflict pair by the first disjunct. Under L255's reading carried into L315 [computed by the check]:
  - Candidate E1 answers 0 and can meet (F1), (F2) and (A) under the target's relations.
  - Candidate E2 has the answer ⊥, because a background component empties Sol_E. It can meet under no relations.
  - At (1, b0) ∈ C there is then no conflict, and the answers differ.
  - So L317 (ii)'s "Their answers then agree at every pair of \(C\)" holds under D8.2's reading and fails under D6.4's.

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
