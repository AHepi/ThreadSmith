# The maths against the words, part 15 of 17: Construction, newness, origin, repair and created explanation

## 1. What you are asked to do

**The text** is a theory of explanation: a formal semantics of what an explanation is and of explanatory creativity, 632 lines, which calls itself "the semantics". Its owner took the decisions in section 2, and asked for "exploring the math a bit more" since "words are vague", adding: "if implementation forces invention, that needs to be recorded" (S36).

**The maths.** The text's definitions were written as mathematics beside the sentences they formalize (D0.1–D18.2; its worked cases encoded as E1–E9). The claims these let one state (FC01–FC110) were each put to a program that searched small finite models for a counterexample. Every choice the maths or the program made that the text does not fix was recorded as an **invention** (I01–I102), with the other choices that were possible. Two checks followed: one re-ran every counterexample and worked it by hand; the other read the maths against the text. They found further choices no entry records (U1–U6 and H01–H20). **Nothing invented is the text's own content.** A counterexample that rests on an invention tells against that way of writing the text, and against the text only where the text fixes what the invention fills in.

**This part** covers Part X of the text on understanding, construction, newness and origin (L401–L431) and Part XI on repair, created explanation and appraisal (L433–L457): the definitions in section 3; 7 claims (FC84, FC85, FC86, FC87, FC88, FC89, FC90) with their results in section 4; the inventions they rest on in section 5 (7 in full); the unrecorded choices in section 6; sentences the maths could not write in section 7; round-1 matters and changes in section 8. The whole is put to readers in 17 parts, each read on its own.

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

### §13 Deploy, Build, New, Origin, ownership, episodes

> L403 | \(\operatorname{Deploy}_{\beta,\ell}(s,c,\xi;U)\) is met when \(s\) at \(\xi\) holds a representation of \(c\), by (R) a faithful transport with selected or constructed provenance, integrated into problem-directed activity and serving the declared use task \(U\) as a retained capability (Part XII). The repertoire \(R_{\beta,\ell}(s,\xi)\) is the set of contents deployable in some nontrivial use respect.

**D13.1 Deploy.** Deploy_{β,ℓ}(s, c, ξ; U) :⟺ some occurrence o of s at ξ has Rep_ℓ(o, c), Integrated(o, s, ξ), and Can_{Ω,β}(ξ, U; χ) holds for some χ with a realization that uses o **[I55]**.

**D13.2 Repertoire.** R_{β,ℓ}(s, ξ) := {c : Deploy_{β,ℓ}(s, c, ξ; U) for some U with Nontrivial(U)} **[I55]**; R_{<e}(s,h) := ∪_{ξ before e} R_{β,ℓ}(s, ξ) (L415).

> L405 | **Construction.** \(\operatorname{Build}_{\beta,\ell}(s,c,h,e)\) is met when an actual subhistory owned by \(s\) and delimited at \(e\) prepares a represented organization for explanatory use of \(c\), contains a nontrivial binding construction relevant to that use, and is not a composition of content-preserving transfers.

**D13.3 Build; construction trace.** Build_{β,ℓ}(s, c, h, e) :⟺ some subhistory h' of h ending at e with Owned_β(h', s) (D13.7) has Prepares(h', c), BindingConstruction(h', c) and ¬TransferComposite(h') **[I56]**. A construction trace is (h', the controlled processes, the incoming carriers, the bindings constructed, the resulting representation) (L405). A binding may be identified by its use: by responses meeting D9.11's clauses (L409).

> L413 | **Newness.** Write \(d\equiv_\ell c\) when there are transports from \(d\) to \(c\) and from \(c\) to \(d\), both faithful on \(c\)'s contract at grain \(\ell\).

**D13.4 Matching.** d ≡_ℓ c :⟺ there are t: E_d → E_c faithful on the preimage of C_c, and t': E_c → E_d faithful on C_c, at grain ℓ **[I48]**. It is read with c fixed (L413) and is not claimed symmetric (FC85).

> L416 | \operatorname{New}(s,c,h,e)\iff\neg\exists d\in R_{<e}(s,h),\ d\equiv_\ell c. \tag{N}

**D13.5 New (N).** New(s, c, h, e) :⟺ no d ∈ R_{<e}(s, h) has d ≡_ℓ c.

> L422 | \operatorname{Origin}_{\beta,\ell}(s,c,p,h,e)\iff\operatorname{Attempt}(s,c,p,h,e)\land\operatorname{New}(s,c,h,e)\land\operatorname{Build}_{\beta,\ell}(s,c,h,e). \tag{G}

**D13.6 Attempt; Origin (G).** Attempt(s, c, p, h, e): c is used in h, up to e, to address p (L419; a claim read through Θ). Origin :⟺ Attempt ∧ New ∧ Build. c may be an organization, a transport or a contract (L425; E8).

> L427 | **Ownership.** The subhistory in Build is owned by \(s\) when its processes run inside the system boundary and resource contract declared for \(s\) (Part XII).

**D13.7 Ownership.** Owned_β(h', s) :⟺ every process of h' runs inside the boundary β and resource contract declared for s. Contribution of content is a separate attribution (L427): Contrib(h', w) records who supplied a content, and does not enter Owned.

> L429 | **Episodes.** A complete critical episode contains a recognized difficulty, a target available before its criticism, a conjectural objection, and a content-sensitive response. A **recognized difficulty** is a failure of a claimed aim, or a conflict in which what the system holds meets a claimed aim only by failing a protected one (Part XI), when the system represents it. A creative critical episode contains an instance of (G) connected to its inquiry.

**D13.8 Episodes.** An episode is a subhistory. CompleteCritical(h') :⟺ h' contains a recognized difficulty (a represented failure of a claimed aim, or a represented conflict in which meeting a claimed aim fails a protected one), a target represented before its criticism, a criticism (D9.10) of it, and a response that uses the criticism as a reason (D9.11). CreativeCriticalEpisode(s, Δ, h, e) :⟺ a complete critical episode of h up to e that contains an instance of (G) 'connected to its inquiry' (read: the (G) instance's Attempt addresses the question the episode's difficulty poses; not fixed by the text).

**Vague.** 'Integrated into problem-directed activity', 'nontrivial use respect' (L403), 'prepares', 'nontrivial binding construction', 'content-preserving transfers' (L405) and 'connected to its inquiry' (L429) are defined nowhere [I55, I56]. 'Faithful on c's contract' for a transport into c needs c's contract on c's own organization [I48].

### §14 Repair, created explanation, appraisal

> L435 | **Repair.** The contribution \(\Delta\) of a repair is a subhistory together with the changes of content it makes.

> L441 | The aims are declared inputs: \(O\) says what is to be repaired and \(P\) what is to be protected, each as a stated condition over stated occasions, and a protected condition is lost exactly when it fails on an occasion it covers. In (P), accordingly, \(r(\xi')\) says of a protected condition \(r\) that it was met on every occasion it covers from \(\xi\) to \(\xi'\), not only at \(\xi'\).

**D14.1 Aims.** An aim is (cond, Occ) with Occ a set of times (declared). For o ∈ O: o(ξ) :⟺ cond met at ξ. For r ∈ P, on the left of (P): r(ξ) :⟺ cond met at ξ if ξ ∈ Occ_r, and holds otherwise; on the right: r(ξ') :⟺ cond met at every ω ∈ Occ_r with ξ ≤ ω ≤ ξ' **[I57]**.

> L438 | \operatorname{Repair}_{O,P}(\xi,\xi';\Delta)\iff\exists o\in O[\neg o(\xi)\land o(\xi')]\land\forall r\in P[r(\xi)\Rightarrow r(\xi')]\land\operatorname{ProducedBy}(\Delta,\xi,\xi';O). \tag{P}

**D14.2 Repair (P).** Repair_{O,P}(ξ, ξ'; Δ) :⟺ ∃o ∈ O [¬o(ξ) ∧ o(ξ')] ∧ ∀r ∈ P [r(ξ) ⇒ r(ξ')] ∧ ProducedBy(Δ, ξ, ξ'; O). Δ = (h_Δ, the content changes it makes).

> L441 | \(\operatorname{ProducedBy}\) is met when an active route (Part IX) runs from \(\Delta\) to the repair; it attributes the repair to each contribution whose active route ran to it in the history, and where two sufficient contributions both ran, the repair is attributed to both and the history supplies no division of the attribution that it does not contain.

**D14.3 ProducedBy.** ProducedBy(Δ, ξ, ξ'; O) :⟺ some o ∈ O with ¬o(ξ) ∧ o(ξ') has an active route (D11.4) from an occurrence of h_Δ to the occurrence at which o's condition comes to be met **[I57]**. Attr(o) := {Δ_i : ProducedBy(Δ_i, …) for o}; no share function is defined (a weighting is a declared input, L522).

> L441 | Losses outside \(P\) must be exposed.

**D14.4 Losses outside P.** A repair claim carries Aims* ⊇ O ∪ P and an exposure record X; WellFormed :⟺ {r ∈ Aims* ∖ P : r(ξ) ∧ ¬r(ξ')} ⊆ X **[I58]**.

> L443 | **Created explanation.** An explanatory aim requires a deployable account, or the correction of a use through one. With \(O_{\mathrm{ex}}\subseteq O\) the explanatory aims,

**D14.5 Explanatory aims.** O_ex ⊆ O, a declared marking; o ∈ O_ex when o's condition is that s possesses a deployable account of a stated question, or is L443's 'the correction of a use through' a deployable account **[I59]**.

> L453 | \(\operatorname{Result}(\Delta)\) is the set of contents at \(\xi'\) that \(\Delta\) prepared. \(\operatorname{ProducesVia}(\Delta,c,o;\xi,\xi')\) is met when an active route that runs from \(\Delta\) to the repair of \(o\) contains the relevant binding of \(c\).

**D14.6 Result; ProducesVia.** Result(Δ) := the contents at ξ' that h_Δ prepared (Prepares, D13.3). ProducesVia(Δ, c, o; ξ, ξ') :⟺ some active route from an occurrence of h_Δ to the occurrence at which o comes to be met contains an occurrence instantiating the binding named in c's construction trace **[I60]**.

> L447 | \operatorname{CreateEx}(s,\Delta,h,e)\iff{}&\operatorname{CreativeCriticalEpisode}(s,\Delta,h,e)\land\exists\xi,\xi'\,\bigl[\operatorname{Repair}_{O,P}(\xi,\xi';\Delta)\\

> L448 | &\land\exists o\in O_{\mathrm{ex}}\,\exists c,p_c,e_c,t_c,\Gamma_c\,[e_c\preceq_h e\land\neg o(\xi)\land o(\xi')\land\operatorname{Origin}_{\beta,\ell}(s,c,p_c,h,e_c)\\

> L449 | &\quad\land\operatorname{Account}\big((c,p_c,t_c,\Gamma_c)\big)\land c\in\operatorname{Result}(\Delta)\land\operatorname{Deploy}_{\beta,\ell}(s,c,\xi';U_c)\land\operatorname{ProducesVia}(\Delta,c,o;\xi,\xi')]\bigr].

**D14.7 Created explanation (EX).** As displayed, with e_c ⪯_h e read in the partial order of D11.3 **[I44]**, and with Account((c, p_c, t_c, Γ_c)) evaluated on the contract of p_c fixed at e_c (L453): CreateEx(s, Δ, h, e) :⟺ CreativeCriticalEpisode(s, Δ, h, e) ∧ ∃ξ, ξ' [Repair_{O,P}(ξ, ξ'; Δ) ∧ ∃o ∈ O_ex ∃c, p_c, e_c, t_c, Γ_c (e_c ⪯_h e ∧ ¬o(ξ) ∧ o(ξ') ∧ Origin(s, c, p_c, h, e_c) ∧ Acc(c, p_c, t_c, Γ_c) ∧ c ∈ Result(Δ) ∧ Deploy(s, c, ξ'; U_c) ∧ ProducesVia(Δ, c, o; ξ, ξ'))].

> L455 | achievement \(\mathcal R[a,k]\neq\varnothing\land\mathcal R[a,k]\subseteq G[k]\) (AR); and \(\mathcal N\subseteq \mathit{Act}\times\mathit{Occ}\times\mathsf{Rsn}\times\mathcal V_A\) taken as a substantive input when aesthetic value is claimed

**D14.8 Appraisal, typed only.** 𝓡 ⊆ Act × Occ × Eff, G ⊆ Occ × Eff, (AR): 𝓡[a,k] ≠ ∅ ∧ 𝓡[a,k] ⊆ G[k]; 𝒩 ⊆ Act × Occ × Rsn × V_A, an input with Rsn and V_A unspecified. No definition of this file uses 𝒩; where values are placed is the owner's question.

**Vague.** Which aim ProducedBy's route runs to is not tied to (P)'s first conjunct [I57]. The universe of 'losses outside P' is not given [I58]. L443 names two kinds of explanatory aim; (EX) treats them alike and the second is carried only by ProducesVia (FC89) [I59]. 'The relevant binding' (L453) [I60].

## 4. The claims, with their search results

Each claim: its type, the inventions it uses, its sentences quoted, its formal statement, and its result, part by part; for a counterexample, what it shows and, where short, the model; then the second check's note, and every invention the result rests on (the claim's own and the program's).

### FC84 · Every creative attribution requires construction

*a sentence that stood unchanged through every revision; follows from the definitions as written.* Inventions it uses: I53, I56.

> L47 | Construction is a separate provenance with a separate trace, and every creative attribution requires it.

**Formal.** Origin ⇒ Build; CreateEx ⇒ Origin ⇒ Build; the creative-episode class (L528) needs an instance of (G), hence Build; Build's subhistory is what a construction trace identifies (L405). Separate traces: Sel's history holds no represented target (L195), Con's holds one (L197).

**Result: HOLDS ON ALL MODELS TRIED.**

- *every creative attribution requires Build* (by construction): **holds by construction**.

**Rests on:** I53, I56.

### FC85 · A content matches itself; the matching is read one way

*follows from the definitions as written.* Inventions it uses: I48.

> L413 | Write \(d\equiv_\ell c\) when there are transports from \(d\) to \(c\) and from \(c\) to \(d\), both faithful on \(c\)'s contract at grain \(\ell\).

*(L416, quoted above.)*

**Formal.** Under I48: (a) c ≡_ℓ c (the identity transport both ways), so c ∈ R_<e ⇒ ¬New. (b) d ≡_ℓ c (on C_c) can hold while c ≡_ℓ d (on C_d) fails; (N) uses only d ≡_ℓ c with c fixed.

**Result: HOLDS ON ALL MODELS TRIED.**

- *(a) c ≡ c* (for all): **holds on all models tried** (17,280 models).
- *(b) the matching is read one way (random)* (there is): **no witness found** (2,560 models).
  Searched: d ≡ c on C_c while c ≡ d on C_d fails
- *(b) the matching is read one way (constructed)* (computation): **computed: as claimed**.

**Rests on:** I48, I77, I78, I81.

### FC86 · Repair: a protected aim failed in between is lost

*a sentence that stood unchanged through every revision; follows from the definitions as written.* Inventions it uses: I57.

*(L438, quoted above.)*

> L441 | a protected condition is lost exactly when it fails on an occasion it covers.

**Formal.** Under I57: a protected r met at ξ and at ξ' and failed on a covered occasion between them makes (P) fail; r is lost ⟺ it fails on a covered occasion in [ξ, ξ'].

**Result: HOLDS ON ALL MODELS TRIED.**

- *every condition, occasion set and pair of times on 4 times* (for all): **holds on all models tried** (2,560 models).
- *a protected aim already failing at ξ* (look): **look: as expected**.
  Searched: (outside FC86) a protected aim that fails at a covered ξ counts as lost by 'fails on an occasion it covers' and is not protected by (P)
  cond failing at ξ = 0 (covered), holding after: r(ξ) on the left fails, so (P) asks nothing of r, while 'r fails on a covered occasion in [ξ, ξ']' holds: under I57 'lost' in L441 and (P)'s protection differ for an aim already failing at ξ.

**Rests on:** I57, I96.

### FC87 · Two sufficient contributions that both ran are both attributed

*follows from the definitions as written.* Inventions it uses: I46, I57.

> L441 | where two sufficient contributions both ran, the repair is attributed to both and the history supplies no division of the attribution that it does not contain.

**Formal.** ProducedBy attributes the repair to each Δ_i with an active route to it; with two such, both; no function from the history to shares of attribution is defined (a weighting is a declared input, L522).

**Result: HOLDS ON ALL MODELS TRIED.**

- *both contributions attributed* (by construction): **holds by construction**.

**Rests on:** I46, I57.

### FC88 · Losses outside P are exposed in the claim, not in (P)

*a sentence that stood unchanged through every revision; follows from the definitions as written.* Inventions it uses: I57, I58.

*(L441, quoted above.)*

**Formal.** Under I58: a repair claim with aims O, P, Aims* and exposure record X is well formed ⟺ {r ∈ Aims*∖P : r(ξ) ∧ ¬r(ξ')} ⊆ X. The condition bears on the claim: (P) can hold while the claim is not well formed.

**Result: HOLDS ON ALL MODELS TRIED.**

- *(P) holds, the claim is not well formed* (computation): **computed: as claimed**.

**Rests on:** I57, I58, I96.

### FC89 · L443 (after round 1) puts 'deployable' where Deploy's type allows it

*a sentence that stood unchanged through every revision; follows from the definitions as written.* Inventions it uses: I59, I60. Bears on the round-1 change at L443 (section 8); what the round-1 change at L443 may have disturbed: (EX) L447–L449, ProducesVia L453.

> L443 | An explanatory aim requires a deployable account, or the correction of a use through one.

> L449 | \operatorname{Deploy}_{\beta,\ell}(s,c,\xi';U_c)

**Formal.** Deploy takes a content (L403). Under the old wording a correction (a subhistory with changes, L435) was asked to be deployable, a mismatch of type. Under the new wording (I59) both kinds of explanatory aim put Deploy on the account c, which is what (EX) asks for every o ∈ O_ex. (EX) has no condition that tells the two kinds apart; the second kind is carried only by ProducesVia.

**Result: NOT TESTED.**

- *L443's two kinds of explanatory aim* (not tested): **not tested**.
  Why not: a reading of the wording of L443 against Deploy's typing

**Rests on:** I59, I60.

### FC90 · The worked case's '(EX) is met' against (EX)'s conjuncts

*a result the text states.* Inventions it uses: I44, I57, I59, I60, I68. Bears on what the round-1 change at L443 may have disturbed: the worked case at L628.

> L628 | If \(S_1\) was built by an owned subhistory containing a nontrivial binding construction, the binding of a persistence component to a continuity subnetwork, and \(S_1\) is not in the prior repertoire, then (G) is met.

> L628 | and since \(S_1\) is an account on its contract and deployable, (EX) is met.

**Formal.** (EX) needs: CreativeCriticalEpisode(s,Δ,h,e); Repair; o ∈ O_ex with ¬o(ξ) ∧ o(ξ'); Origin(s,c,p_c,h,e_c) with e_c ⪯_h e; Account; c ∈ Result(Δ); Deploy(s,c,ξ';U_c); ProducesVia(Δ,c,o;ξ,ξ'). L628 states (G)'s Build and New (not Attempt), (P), Account and 'deployable'. Test which of CreativeCriticalEpisode (L429's four parts), Attempt, c ∈ Result(Δ), ProducesVia and e_c ⪯_h e the worked case's description gives, and which it leaves to be read in.

**Result: NOT TESTED.**

- *the worked case's '(EX) is met'* (not tested): **not tested**.
  Why not: a reading of L620–L628; the model does not encode the worked case's history

**Rests on:** I44, I57, I59, I60, I68.

## 5. The inventions these rest on

In full: each invention this part is the first of the parts to use. Then, for an invention given in full in another part that a counterexample here rests on, what was invented. Then the rest by title. I77 and I78, the bounds and families of the search, are described in section 1 and given in full in another part.

### I55 · Deploy: 'integrated into problem-directed activity', 'nontrivial use respect'

Fills in for:

> L403 | integrated into problem-directed activity and serving the declared use task \(U\) as a retained capability (Part XII). The repertoire \(R_{\beta,\ell}(s,\xi)\) is the set of contents deployable in some nontrivial use respect.

**Invented.** Deploy_βℓ(s,c,ξ;U) := for some occurrence o of s at ξ, Rep_ℓ(o,c), Integrated(o,s,ξ) and, for some χ, Can_Ωβ(ξ,U;χ) with a realization that uses o. Integrated and Nontrivial(U) are primitive predicates read through the physical module.

**Other choices.** (a) Integrated defined through active routes (o lies on an active route to a problem's result).

**Used by:** 1 other claim.

### I57 · Repair: how the aims are read at ξ and over [ξ, ξ']; which aim ProducedBy runs to

Fills in for:

> L441 | In (P), accordingly, \(r(\xi')\) says of a protected condition \(r\) that it was met on every occasion it covers from \(\xi\) to \(\xi'\), not only at \(\xi'\).

> L441 | \(\operatorname{ProducedBy}\) is met when an active route (Part IX) runs from \(\Delta\) to the repair

**Invented.** An aim is (cond, Occ) with Occ a set of times. o(ξ) for o in O: cond met at ξ. On the left of (P), r(ξ) := cond met at ξ if ξ ∈ Occ_r, and holds otherwise; on the right, r(ξ') := cond met at every ω ∈ Occ_r with ξ ≤ ω ≤ ξ'. ProducedBy(Δ,ξ,ξ';O) := some o in O with ¬o(ξ) ∧ o(ξ') has an active route from an occurrence of Δ to the occurrence at which its cond comes to be met; it need not be the o of (P)'s first conjunct.

**Other choices.** (a) tie ProducedBy to the same o as the first conjunct. (b) r(ξ) on the left also read over an interval.

**Used by:** claims of this part: FC86, FC87, FC88, FC90.

### I58 · 'Losses outside P': the aims considered, and 'exposed'

Fills in for:

*(L441, quoted above.)*

**Invented.** A repair claim carries a declared set Aims* ⊇ O ∪ P of aims under consideration and an exposure record X; the claim is well formed when {r ∈ Aims* \ P : r(ξ) ∧ ¬r(ξ')} ⊆ X. Aims* is a declared input that L522 does not list.

**Other choices.** (a) all aims the system holds, read through the physical module. (b) exposure as a statement in the record, not a set.

**Used by:** claims of this part: FC88; 1 other claim.

### I59 · Explanatory aims: L443 read as a characterization of O_ex

Fills in for:

> L443 | **Created explanation.** An explanatory aim requires a deployable account, or the correction of a use through one.

**Invented.** O_ex ⊆ O is a declared marking of aims; L443 is read as: o is explanatory when its condition is 's possesses a deployable account of a stated question' or is L443's 'the correction of a use through' a deployable account. (EX) imposes the same conditions on both kinds.

**Other choices.** (a) L443 as a necessary condition only. (b) O_ex defined by (EX)'s own conditions.

**Used by:** claims of this part: FC89, FC90; 1 other claim.

### I60 · ProducesVia: 'the relevant binding of c'

Fills in for:

> L453 | \(\operatorname{ProducesVia}(\Delta,c,o;\xi,\xi')\) is met when an active route that runs from \(\Delta\) to the repair of \(o\) contains the relevant binding of \(c\).

**Invented.** The relevant binding of c is the binding named in c's construction trace (Build's binding construction); 'contains' means some occurrence of the route instantiates it.

**Other choices.** (a) any occurrence that carries c.

**Used by:** claims of this part: FC89, FC90.

### I68 · Argument 10's two-layer episode, encoded; 'recent occupancy'

Fills in for:

> L620 | Stipulate an object layer \(P\): a line of cells; two things, each with a position and a velocity; continuity components; admitted edits: displace a thing, set its velocity, occlude a cell, swap the two identities.

> L622 | \(S_0\) predicts occupancy from recent occupancy.

**Invented.** A line of N cells (N = 6 for tests), two things with position in {0..N−1} and velocity in {−1,0,1}, time steps 0..K; continuity: pos(t+1) = pos(t) + vel(t), with a stated rule at the ends (reflection); occluding cell c makes the occupancy reading of c empty; swap exchanges the two things' positions and velocities. S0 predicts occupancy at t+1 from the occupancy of the last w steps, with the window w shorter than the occlusion.

**Other choices.** (a) continuous positions. (b) an unbounded window (then an occupancy predictor could extrapolate through an occlusion, and the 'structural' failure can fail: FC102). (c) stopping at the ends instead of reflecting.

**Used by:** claims of this part: FC90; 2 other claims. Counterexamples resting on it: FC102.

### I96 · Aims on discrete time

Fills in for:

> L441 | each as a stated condition over stated occasions

**Invented.** Times are 0..3; a condition is a sequence of values, each 'holds' or 'fails'; occasions are a set of times; the repair's ξ ≤ ξ'; Aims* and the exposure record (I58) are finite lists.

**Other choices.** (a) continuous time with occasions as intervals.

**Used by:** claims of this part: FC86, FC88.

Named by title only (given in full in another part): I44, Causal precedence in a history is transitive; I46, Active route: 'represented input', 'operative result', 'applicable relations', 'declared contrasts'; I48, Contents, 'c's contract', and transports into a content; I53, 'Exactly one of three provenances': one whole history; I56, Build: 'prepares', 'nontrivial binding construction', 'content-preserving transfer'; I77, Finite models and the bounds of the search; I78, Two families of generated organizations: surgical edits with override, and free edits; I81, Transports as port translations; computed ports; generated candidates; the transport space searched for ≡.

## 6. Choices no register entry records

Found by the two checks. U-entries come from the check that re-ran the program; H-entries from the check that read the maths against the text, in its wording.

### H06 · An episode is any subhistory (D13.8), against L55's sentence

> L55 | An episode is a history in which contracts change, and every change carries a provenance record.

> L197 | **Constructed.** There is an episode (Part X) whose construction trace prepares \(t\)

- **Added.** "An episode is a subhistory" (D13.8), with no invention number. This makes the "episode" of L197, L405 ("delimited at \(e\)") and (G) as wide as any subhistory. L55's sentence sits in the front matter. L35 says of the front matter that it "states nothing the body does not state more exactly", and the body never defines "episode" by itself.
- **Other choice.** L55's reading: a history in which contracts change, each change with a provenance record.
- **Depends on it.** Con (D12.2) and so FC78–FC84 and FC95. The model's `con(h)` takes no episode at all: it holds when a trace in h prepares t and t or its codomain is a represented target in h. Under L55's reading, Con in the FC78 family of models would also need a contract change with its record, and the hand-set histories state none. This was not computed. I90 covers setting Θ by hand; it does not cover what an episode is.

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

## 7. Sentences of this group the maths could not write

**NF07** (L201). Why it was not formalized: 'Reducible' is not defined; the formal part is exclusivity (FC78).

> L201 | Neither provenance is reducible to the other

**NF09** (L407). Why it was not formalized: 'Written in a particular format' has no formal counterpart; formally, (R), Deploy and Build take no format argument (a syntactic property).

> L407 | An inexplicit representation is not an absent one.

**NF10** (L429). Why it was not formalized: No formal content beyond the syntactic fact that no definition outputs a choice (decisions S21, S28).

> L429 | Closing an episode is a choice

**NF19** (L455). Why it was not formalized: The three aesthetic relations are typed inputs; 'none is defined as another' is a syntactic property, and no relation among them is given to test.

> L455 | None is defined as another.

## 8. Round 1: matters noted and changes made

In the first review round, readers tried to vary sentences that had stood unchanged; the rulings changed four lines and recorded fourteen matters outside the sentences examined, left for later rounds.

**The round-1 change at L443.** Before:

> L443 (before round 1) | **Created explanation.** An explanatory aim requires an account, or the correction of a use through one, to be deployable. With \(O_{\mathrm{ex}}\subseteq O\) the explanatory aims,

After, as the text now stands:

> L443 | **Created explanation.** An explanatory aim requires a deployable account, or the correction of a use through one. With \(O_{\mathrm{ex}}\subseteq O\) the explanatory aims,

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
