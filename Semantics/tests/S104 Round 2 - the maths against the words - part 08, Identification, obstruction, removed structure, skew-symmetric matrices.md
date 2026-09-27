# The maths against the words, part 8 of 17: Identification, obstruction, removed structure, skew-symmetric matrices

## 1. What you are asked to do

**The text** is a theory of explanation: a formal semantics of what an explanation is and of explanatory creativity, 632 lines, which calls itself "the semantics". Its owner took the decisions in section 2, and asked for "exploring the math a bit more" since "words are vague", adding: "if implementation forces invention, that needs to be recorded" (S36).

**The maths.** The text's definitions were written as mathematics beside the sentences they formalize (D0.1–D18.2; its worked cases encoded as E1–E9). The claims these let one state (FC01–FC110) were each put to a program that searched small finite models for a counterexample. Every choice the maths or the program made that the text does not fix was recorded as an **invention** (I01–I102), with the other choices that were possible. Two checks followed: one re-ran every counterexample and worked it by hand; the other read the maths against the text. They found further choices no entry records (U1–U6 and H01–H20). **Nothing invented is the text's own content.** A counterexample that rests on an invention tells against that way of writing the text, and against the text only where the text fixes what the invention fills in.

**This part** covers the exact constructions of Part VII of the text (L327–L349): identification, the two balances, obstruction, explanation that removes structure, odd-order skew-symmetric matrices: the definitions in section 3; 7 claims (FC57, FC58, FC59, FC60, FC61, FC62, FC63) with their results in section 4; the inventions they rest on in section 5 (6 in full); the unrecorded choices in section 6; sentences the maths could not write in section 7; round-1 matters and changes in section 8. The whole is put to readers in 17 parts, each read on its own.

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

> L255 | The target's answer does not appear, at the declared grain, as an unanalysed boundary input or as a component; moving an assertion from an input slot into a component named "law" does not discharge this. Identity of that assertion with the target's answer is structural at the declared grain, not the indiscriminate identification of all logically equivalent mathematical statements.

**D6.3 NC1 (no answer slot).** Slot_C(ℰ, k) :⟺ δ_E's answer ports lie in V_k, and for every (a,b) ∈ C, L^E_k(τ(a),σ(b)) = {w ∈ ∏_{V_k} X : w on the answer ports = Ans_p(a,b)} (and constrains nothing else); likewise for a boundary coordinate of E whose value at σ(b) is Ans_p(a,b). NC1(ℰ) :⟺ no k ∈ J_E and no boundary coordinate is a slot, in E as given at grain ℓ **[I24, I28]**.

> L255 | There exist \((a,b)\in C\) and a nonempty block \(G\subseteq\Gamma\) such that the answer of \(E\) at \((\tau(a),\sigma(b))\) differs from its answer at \((1,\sigma(b_0))\), or is not determined at \((\tau(a),\sigma(b))\) in the claimed way, and this contrast is lost when the components of \(G\) are deleted from \(E\)

> L255 | evaluated at \((\tau(a),\sigma(b))\) and at \((1,\sigma(b_0))\), the answers of \(E\) with \(G\) deleted are determined and equal, or an answer that \(E\) determines at one of these points is not determined there once \(G\) is deleted.

**D6.4 NC2 (a contrast lost under deletion).** With x = (τ(a),σ(b)) and x0 = (1,σ(b0)):
- Contrast(E; x) :⟺ [Ans_E(x) ≠ ⊥ ∧ Ans_E(x0) ≠ ⊥ ∧ Ans_E(x) ≠ Ans_E(x0)] ∨ [Ans_E(x) = ⊥ ∧ Ans_E(x0) ≠ ⊥] **[I21, I22]**;
- Lost(E, G; x) :⟺ [Ans_{E−G}(x) ≠ ⊥ ∧ Ans_{E−G}(x0) ≠ ⊥ ∧ Ans_{E−G}(x) = Ans_{E−G}(x0)] ∨ [for some y ∈ {x, x0}: Ans_E(y) ≠ ⊥ ∧ Ans_{E−G}(y) = ⊥];
- NC2(ℰ) :⟺ there are (a,b) ∈ C and G ⊆ Γ, G ≠ ∅, with Contrast(E; x) ∧ Lost(E, G; x).

**E2 Identification** **[I63, I64]**.

**E3 The two balances.** G = [[1,1,0],[1,0,1]] on (x, b_A, b_B) (L331). Claims: FC59, FC60.

**E4 Obstruction.**

**E5 Explanation that removes structure** **[I03]**. D with a component x deleted at the baseline and an edit a_x giving it a relation; E with k, λ(k) = {x}. Claim: FC62.

**E6 Odd-order skew-symmetric matrices** **[I66]**.

## 4. The claims, with their search results

Each claim: its type, the inventions it uses, its sentences quoted, its formal statement, and its result, part by part; for a counterexample, what it shows and, where short, the model; then the second check's note, and every invention the result rests on (the claim's own and the program's).

### FC57 · (I2): identified at every attainable value exactly when the feature factors through the measurement

*a result the text states.* Inventions it uses: I63, I64.

> L329 | It is identified on every attainable \(y\) exactly when \(f=\bar f\circ g\) for some \(\bar f\).

**Formal.** (∀y ∈ g[Z]: |f[Z_y]| = 1) ⟺ ∃f̄: Y → F with f = f̄∘g on Z.

**Result: HOLDS ON ALL MODELS TRIED.**

- *(I2) on finite sets* (for all): **holds on all models tried** (11,132 models).

**Rests on:** I63, I64, I77.

### FC58 · (I3): the kernel criterion; repeated rows; an independent calibration

*a result the text states.* Inventions it uses: I63, I64.

> L329 | For linear \(g\) and linear feature \(c^\top\), identification is \(\ker g\subseteq\ker c^\top\).

> L329 | Repeating rows changes no kernel; an independent calibration can.

**Formal.** Z = ℝ^n, g = G ∈ ℝ^{m×n}, feature c ∈ ℝ^n: (∀y ∈ G[ℝ^n]: |cᵀ[G⁻¹(y)]| = 1) ⟺ ker G ⊆ ker cᵀ. A row in the row space of G leaves ker G unchanged; a row outside it lowers dim ker G by one.

**Look** (a first reading of where a counterexample might lie, written before the search). With Z a proper subset (I64's alternative), the criterion can fail.

**Result: HOLDS ON ALL MODELS TRIED.**

- *the kernel criterion* (for all): **holds on all models tried** (2,400 models).
- *rows* (for all): **holds on all models tried** (2,400 models).
- *Z a proper subset* (look): **look: as expected**.
  Searched: the look: with Z a proper subset (I64's alternative), the criterion can fail
  Z = {0,1}², g = x+y, f = x: kernel criterion no; identified at every attainable y on Z: no (y = 1 has the fibre {(0,1),(1,0)}). Taking y ∈ {0, 2} alone, f is identified though ker g ⊄ ker f: on a box the criterion is sufficient, not necessary, at a given y.

**Rests on:** I63, I64, I77.

### FC59 · The two balances

*a result the text states.* Inventions it uses: I64.

> L331 | the kernel is spanned by \((1,-1,-1)\); the readings identify \(b_B-b_A\) and not \(x\).

**Formal.** G = [[1,1,0],[1,0,1]] on (x, b_A, b_B): ker G = span{(1,−1,−1)}; c = (0,−1,1) gives c·(1,−1,−1) = 0 (identified); c = (1,0,0) gives 1 (not identified).

**Result: HOLDS ON ALL MODELS TRIED.**

- *the two balances* (computation): **computed: as claimed**.

**Rests on:** I64.

### FC60 · Setting a bias from the favoured mass: where the circularity can be registered

*a result the text states.* Inventions it uses: I24, I39.

> L331 | "Set \(b_B=0\) because it gives the mass I favour" is not an inference from the readings; it is circular, though the value it sets might be the target's.

**Formal.** (a) Two candidates with the boundary value b_B = 0, one set 'because it gives the mass I favour' and one set by an independent calibration, have the same (D, C, E, t, Γ, Σ), so the same Acc value (FC30): (E) does not register the circularity, and NC1 does not either, since the value 0 is not the answer (I24). (b) Where it can be registered is Part IX's block: an argument concluding x = m* whose premise b_B = 0 is a record MadeFrom the claim x = m* (I39) does not rule out x ≠ m* (D9.7). (c) Its value can equal the target's b_B, so (F1), (F2), (A) can hold at the baseline.

**Result: HOLDS ON ALL MODELS TRIED.**

- *(a) (E) does not register how an input was chosen* (by construction): **holds by construction**.
- *(b) the record made from x = m* does not rule out x ≠ m** (computation): **computed: as claimed**.

**Rests on:** I24, I39, I87, I89.

### FC61 · (O1): an invariant blocks paths; equal values do not give paths; twenty-three tokens

*a result the text states.* Inventions it uses: I63.

> L335 | For allowed steps \(R\) and an invariant \(I\) with \(zRz'\Rightarrow I(z)=I(z')\), no allowed path joins states of different invariant value. (O1) Equal values do not suffice for reachability. Twenty-three indivisible tokens cannot be split equally three ways;

**Formal.** (a) If zRz' ⇒ I(z) = I(z'), then R* ⊆ {(z,z') : I(z) = I(z')}. (b) There are R, I, z, z' with I(z) = I(z') and not zR*z'. (c) Distributions (n1,n2,n3) of 23 whole tokens: an equal split needs 3n = 23, which has no whole solution.

**Result: HOLDS ON ALL MODELS TRIED.**

- *(a) an invariant blocks paths* (for all): **holds on all models tried** (2,000 models).
- *(b) equal values do not give paths; (c) twenty-three tokens* (computation): **computed: as claimed**.

**Rests on:** I63, I77.

### FC62 · Eliminative explanation: the rival's structure as a deleted counterpart

*a result the text states.* Inventions it uses: I03, I14.

> L339 | An account is faithful when introducing those components changes the answer in \(E\) as it does in \(D\), and their absence leaves both unchanged. The rival's supposed structure has as its counterpart a *deleted* subnetwork, whose relation is full (Part II).

**Formal.** D with a component x whose baseline relation is full (I03) and an edit a_x giving it a relation; E with k, λ(k) = {x}, baseline relation full, τ(a_x) giving k the projected relation. F1 at (1,b0): full = full; at (a_x,b0): holds when τ(a_x) gives k that relation. On C = {(1,b0), (a_x,b0)}, E can meet (E) (NC2 with G = {k}) when the answer depends on x.

**Result: HOLDS ON ALL MODELS TRIED.**

- *eliminative explanation* (computation): **computed: as claimed**.

**Rests on:** I03, I14, I78, I79.

### FC63 · Odd-order skew-symmetric matrices

*a result the text states.* Inventions it uses: I03, I27, I66.

> L343 | Question: why is every odd-order real skew-symmetric matrix singular?

> L343 | Non-circular dependence is met: \(I_3\) is an instance under removal of skewness, and \(\begin{pmatrix}0&1\\-1&0\end{pmatrix}\) under removal of oddness.

> L343 | The expansion is an account.

**Formal.** (a) For every odd n and every n×n M over ℝ (or GF(p), p odd) with Mᵀ = −M: det M = 0. (b) det I3 = 1; det [[0,1],[−1,0]] = 1. (c) With I66, the Leibniz candidate meets (F1), (F2), (A), NC2 and non-vacuity (the scope statement naming the edits to field arithmetic and to the determinant–invertibility link).

**Result: COUNTEREXAMPLE FOUND.** Rests on I66 and I99 (which relation the sum component carries) and I81 (computed ports, without which the candidate cannot be written under I14). With the sum restricted to realizable term tuples the candidate meets (E).

- *(a) odd skew-symmetric matrices are singular over GF(p), p odd* (computation): **computed: as claimed**.
- *(b)* (computation): **computed: as claimed**.
- *(c-i) the Leibniz candidate, sum over every tuple of term values* (computation): **computed: not as claimed**.
  Searched: the Leibniz candidate meets (F1), (F2), (A), NC2 and non-vacuity
  Target: n ∈ {1,2,3}, entries in GF(3), M one port, components order, skew, odd, det, inv; edits remove skew (rs), remove oddness (ro), both (rb); the edits to field arithmetic and to det–invertibility are not edits of this encoding, so the scope clause is met trivially (I99). Answers {'1': no, 'rs': yes, 'ro': yes, 'rb': yes}. The Leibniz candidate needs ports for the terms, which D lacks: under I14 (each E port translated to one D port) it cannot be written; with computed ports (a term port read as a function of M, I81) it can. Variant 'sum over every tuple of term values': F1 no (failing: ['sum']); Account no {'F1': no, 'F2eq': yes, 'A': yes}. Variant 'sum restricted to realizable term tuples': F1 yes (failing: none); Account yes {'translates C': yes, 'F1': yes, 'F2eq': yes, 'Hom': yes, 'F2': yes, 'A': yes, 'NC1': yes, 'NC2': yes, 'NonVacuous': yes}, NC2 witness (('rb', 'b0'), ['order']).
- *(c-ii) the Leibniz candidate, sum restricted to realizable term tuples* (computation): **computed: as claimed**.

**The second check.** Worked by hand for (c-i): the sum component relates all 3⁶ tuples of GF(3) term values to their sum, while its counterpart projects only onto term tuples some matrix gives. The all-ones tuple is not realizable: for a 3×3 M each entry lies in exactly one even and one odd term, so t₀t₃t₄ = −t₁t₂t₅, and all ones would need 1 = −1 in GF(3). So (F1) fails for the sum component at every pair. Variant (c-ii), the sum restricted to term tuples some matrix gives, meets (E). Which of the two is 'the' Leibniz candidate is I99's choice; both need I81's computed ports, which I14 excludes, so under the formal core as written the candidate cannot be written at all.

**Rests on:** I03, I27, I66, I81, I82, I99.

## 5. The inventions these rest on

In full: each invention this part is the first of the parts to use. Then, for an invention given in full in another part that a counterexample here rests on, what was invented. Then the rest by title. I77 and I78, the bounds and families of the search, are described in section 1 and given in full in another part.

### I63 · A tag such as (I2) names the sentence before it

Fills in for:

> L329 | The feature is identified at \(y\) exactly when \(Z_y\neq\varnothing\land|f[Z_y]|=1\). (I1)

> L335 | no allowed path joins states of different invariant value. (O1)

> L471 | the greatest fixed point is the union of the sets \(D\) with \(D\subseteq F(D)\). (CT2)

**Invented.** Each parenthesized tag names the sentence it follows, as it can only do at L395 and L471 (nothing follows the tag there). So (I1) is the definition of identification at y, (I2) the factorization claim, (I3) the kernel criterion, and (O1) the invariance claim.

**Other choices.** (a) a tag names the sentence after it (then (I2) is the kernel criterion and (O1) is 'Equal values do not suffice for reachability').

**Used by:** claims of this part: FC57, FC58, FC61; 1 other claim.

### I64 · Identification: 'attainable', and the admitted states in the linear case

Fills in for:

*(L329, quoted above.)*

*(L329, quoted above.)*

**Invented.** y is attainable when y ∈ g[Z]. In the linear case Z is the whole space ℝ^n and 'identification' is identification at every attainable y.

**Other choices.** (a) Z a proper subset (a cone or box of admitted states; then the kernel criterion can fail). (b) identification at one given y.

**Used by:** claims of this part: FC57, FC58, FC59; 1 other claim.

### I66 · The odd-order skew-symmetric case, encoded

Fills in for:

> L343 | Contract: remove skewness; remove oddness; remove both; field arithmetic and determinant–invertibility held fixed.

**Invented.** Ports: the order n, the matrix entries, det, inv; components: skew (Mᵀ = −M), odd (n odd), determinant (Leibniz sum), invertibility (inv ⟺ det ≠ 0); edits: delete skew, delete odd, delete both; Q: 'does the family contain an invertible matrix?'. For tests: n in {1,2,3}, entries in GF(p) for an odd prime p (the statement also holds there, since 2 is invertible) or small integer ranges with exact determinants. The Leibniz candidate: one component per permutation term and a sum component.

**Other choices.** (a) real entries handled symbolically. (b) entries in GF(2), where the statement fails (a different field arithmetic, which the contract holds fixed).

**Used by:** claims of this part: FC63. Counterexamples resting on it: FC63.

### I87 · Claims as propositional formulas, read structurally

Fills in for:

> L397 | it rules out a claim when the claim is inconsistent with its conclusion and the claim's denial is not among its premises (below).

> L397 | read structurally as non-circular dependence reads identity (Part V) and not by logical equivalence alone

**Invented.** Claims are propositional formulas (atoms, ¬, ∧, →), a restriction of I38's first-order language; 'inconsistent with' is inconsistency under every two-valued assignment; 'among its premises, read structurally' is: after removing double negations and flattening and sorting conjunctions, ¬φ is a conjunct of a leaf; the denial of ψ is ¬ψ with a double negation removed. Facts about the models (that a candidate meets a condition at a pair, that χ speaks of the target) enter the arguments as atoms and conditionals.

**Other choices.** (a) first-order claims (I38) with a structural reading up to renaming of bound variables. (b) the denial of ψ read without removing double negations (then 'made from ¬χ' does not block χ).

**Used by:** claims of this part: FC60; 9 other claims.

### I89 · The inference forms: MP, MT, AND-introduction, AND-elimination and a free form

Fills in for:

> L387 | For argument step \(u\) with essential premises \(\operatorname{Prem}(u)\), the premises its inference form uses:

> L393 | \(\operatorname{Form}_j(u)\): the inference form of \(u\) is one \(j\) admits.

**Invented.** Five forms: modus ponens, modus tollens, ∧-introduction, ∧-elimination, and a 'free' form (any premises, any conclusion; an admitted form need not be sound, I38). A step counts only where it instantiates its form; every premise of a step is essential.

**Other choices.** (a) forms declared by each assessor as arbitrary relations between premise sets and conclusions. (b) essential premises a proper subset of a step's children.

**Used by:** claims of this part: FC60; 9 other claims.

### I99 · The odd-order skew-symmetric case in GF(3), and the Leibniz candidate's sum component

Fills in for:

*(L343, quoted above.)*

> L343 | The full Leibniz expansion with skewness substituted meets (F1) and (F2)

**Invented.** n ∈ {1,2,3}, entries in GF(3), the matrix one port; components order, skew, odd, det, inv; edits remove skew, remove oddness, both; the edits to field arithmetic and to the determinant–invertibility link are not edits of this encoding. The Leibniz candidate has one term port and term component per permutation of three (for order 2 the permutations fixing the third index, for order 1 the identity; other terms 0) and one sum component; two relations of the sum component are tested: every tuple of term values with its sum, and only the tuples some matrix gives. Order-5 and GF(5), GF(7) cases enter only the check that odd skew matrices are singular.

**Other choices.** (a) real entries handled symbolically. (b) D given term ports of its own (then the candidate is D itself). (c) a sum component whose footprint includes the matrix.

**Used by:** claims of this part: FC63. Counterexamples resting on it: FC63.

### I03 · Ports and components are fixed; deletion and absence are the full relation

**Invented** (given in full in another part). An edit never adds or removes a member of V or J. A deleted or absent component is one whose relation under that edit and boundary is the full product of its ports' domains. An 'absent' port is one on which every component that could constrain it imposes the full relation.

### I27 · The stated scope: a declared statement over pairs

**Invented** (given in full in another part). A scope statement Σ is a declared input naming a set Excl(Σ) ⊆ A_D × B_D; the clause holds when (A_D × B_D) \ C ⊆ Excl(Σ). Pairs, not edits, are what C excludes. Every a in A_D counts as an edit the target admits.

### I81 · Transports as port translations; computed ports; generated candidates; the transport space searched for ≡

**Invented** (given in full in another part). π is induced by port translations: each port of E reads a tuple of D's ports through a value map (I14's case is one port and a map κ; several ports, a 'computed port', are used only for the term ports of the Leibniz candidate, FC63); π is then total. τ and σ are finite maps. Generated candidates: E's ports a subset of D's (optionally recoded by value maps), its components the projections of groups of D's components at each pair (an encoding candidate, I32's E_enc), τ and σ the identity or random, with background components and one perturbed relation at random; also random organizations with random τ, σ, λ (λ(k) chosen to cover k's footprint), and lookups (FC23). For ≡ (FC85) the transports searched are π and λ the identity on shared names with τ and σ every map, so 'no transport exists' is shown only over that space.

### I82 · Queries in the program; NC1 only for a query that reads a port

**Invented** (given in full in another part). Random searches use the port-reading query Q_w with the designation δ_E of E's copy of the port (I20's default); the worked cases use queries written as functions of Sol (the fibre query of the pole, the 'contains an invertible matrix' query of E6). NC1's answer slot is defined for a port-reading query only; for any other query no component is a slot.

Named by title only (given in full in another part): I14, Subnetworks, their solutions, and port translations with value maps; I21, Undetermined answers: a value ⊥; I22, 'Not determined … in the claimed way'; I24, NC1: the target's answer as an unanalysed boundary input or component, read structurally; I28, The grain as a label on the organizations compared; I39, 'Among its premises', read structurally; records made from a claim; I77, Finite models and the bounds of the search; I78, Two families of generated organizations: surgical edits with override, and free edits; I79, Boundary inputs and exogenous values are carried by components.

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
