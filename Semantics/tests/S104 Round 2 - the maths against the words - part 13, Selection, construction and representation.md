# The maths against the words, part 13 of 17: Selection, construction and representation

## 1. What you are asked to do

**The text** is a theory of explanation: a formal semantics of what an explanation is and of explanatory creativity, 632 lines, which calls itself "the semantics". Its owner took the decisions in section 2, and asked for "exploring the math a bit more" since "words are vague", adding: "if implementation forces invention, that needs to be recorded" (S36).

**The maths.** The text's definitions were written as mathematics beside the sentences they formalize (D0.1–D18.2; its worked cases encoded as E1–E9). The claims these let one state (FC01–FC110) were each put to a program that searched small finite models for a counterexample. Every choice the maths or the program made that the text does not fix was recorded as an **invention** (I01–I102), with the other choices that were possible. Two checks followed: one re-ran every counterexample and worked it by hand; the other read the maths against the text. They found further choices no entry records (U1–U6 and H01–H20). **Nothing invented is the text's own content.** A counterexample that rests on an invention tells against that way of writing the text, and against the text only where the text fixes what the invention fills in.

**This part** covers the three provenances and representation in Part IV of the text (L191–L213): the definitions in section 3; 4 claims (FC77, FC78, FC79, FC95) with their results in section 4; the inventions they rest on in section 5 (7 in full); the unrecorded choices in section 6; sentences the maths could not write in section 7; round-1 matters and changes in section 8. The whole is put to readers in 17 parts, each read on its own.

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

### §12 Provenance, representation, prediction

> L193 | A transport \(t\) whose domain is an organization of a physical system has exactly one of three provenances, determined by its history in the physical module:

> L195 | **Selected.** There is a population \(\mathcal T\) of candidate transports, a variation operator \(\mu\) on \(\mathcal T\), a finite history \(H\subseteq C\) of edit–boundary pairs actually encountered, and a survival condition requiring fidelity on \(H\).

> L195 | A transport **survives on \(H\)** when it is a member of \(\mathcal T\) that meets the survival condition on \(H\); fidelity on \(H\) without membership in \(\mathcal T\) is not survival. No member of the history represents \(t\), \(H\), or the survival condition.

**D12.1 Selected.** Sel(t; 𝒯, μ, H) :⟺ t ∈ 𝒯; μ: 𝒯 → P(𝒯); H ⊆ C finite, its pairs having occurred (D11.5); Faithful_H(t) (D5.7), i.e. t survives on H; and there is a physical selection history h_sel in which the pairs of H occur, the members of 𝒯 are admitted by the physics (D15.8), and no occurrence represents (D12.5) t, H or the survival condition **[I52]**.

> L197 | **Constructed.** There is an episode (Part X) whose construction trace prepares \(t\), and in which \(t\), or the organization it carries to, is available as a represented target. Write \(\operatorname{Con}(t;h,e)\).

**D12.2 Constructed.** Con(t; h, e) :⟺ some episode of h up to e (D13.8) has a construction trace (D13.3) that prepares t, and t or its codomain is a represented target in it.

> L199 | **Declared.** Neither of the above. The transport is entered into the model by its author. Write \(\operatorname{Dec}(t)\).

**D12.3 Declared.** Dec(t) :⟺ no parameters give Sel(t; ·) and none give Con(t; ·). Sel and Con are read on the whole history of t **[I53]**.

> L211 | A carrier keeps its provenance when present access to it is lost, and a later record made from the carrier carries that provenance, not a second, independent one.

> L405 | A small binding newly prepared inside received content is construction of that binding, and the rest of the content keeps its inherited provenance.

**D12.4 Provenance per part; inherited provenance.** prov assigns Sel, Con or Dec to each part of a transport (each component with its counterpart binding). A content-preserving transfer (relay or record) from carrier o to o' gives each part at o' the value it had at o; a binding newly built gets Con. 'Inherited' is this rule, not a fourth value **[I54]**.

> L205 | An occurrence \(o\) **represents** content \(c\) at grain \(\ell\) when there is a transport from the organization that \(o\) instantiates under the physical module, at grain \(\ell\), to \(c\), faithful on \(c\)'s contract, whose provenance is selected or constructed;

> L208 | \operatorname{Rep}_\ell(o,c)\iff\exists t\,[\operatorname{Faithful}_C(t:\operatorname{Org}_\ell(o)\to c)\land(\operatorname{Sel}(t)\lor\operatorname{Con}(t))]. \tag{R}

**D12.5 Representation (R).** Rep_ℓ(o, c) :⟺ there is t: Org_ℓ(o) → E_c, faithful (D5.7) on the preimage {(a,b) : (τ(a),σ(b)) ∈ C_c} with Γ_c as its active components **[I48]**, and some parameters give Sel(t; ·) or Con(t; ·). Org_ℓ is the one thing (R) takes from Θ (L213).

> L175 | The **object layer** \(P\) is an organization whose ports are persistent things with boundaries and identity, whose components are their continuity relations, and whose admitted edits include displacement, occlusion and re-identification.

> L177 | The **simulation layer** \(S\) is an organization over \(P\) whose components are dependencies among things and whose queries are predictions: what a port of \(P\) will take under an admitted edit.

**D12.6 Layers.** P and S are organizations typed as L175 and L177 say; nothing assumes either exists in a given system (L179).

> L219 | - the **prediction** is \(\operatorname{Ans}_S(\tau(a),\sigma(b))\);

> L220 | - a **violation** occurs when fidelity fails at \((a,b)\);

> L221 | - **surprise** is a violation of a selected transport at \((a,b)\notin H\).

**D12.7 Prediction, violation, surprise.** For t from P to S with contract C and, if selected, history H, at (a,b) ∈ C with Occurs(a,b,ξ): Pred_t(a,b) := Ans_S(τ(a),σ(b)); Viol(t; a,b) :⟺ ¬(F1 at (a,b) ∧ F2eq at (a,b)), and Viol⁺ adds (A) at (a,b) **[I50]**; Surp(t; a,b) :⟺ Sel(t; 𝒯, μ, H) for some 𝒯, μ, H with (a,b) ∉ H, and Viol(t; a,b). Pred is extended to any transport, Pred_t(a,b) := Ans_E(τ(a),σ(b)), where a line uses it so (L151) **[I51]**.

> L225 | A **selection response** extends the history \(H\) of a selected transport and lets \(\mu\) act: the transport is re-tuned within the population. A **construction response** introduces a new organization or a new transport with a construction trace.

**D12.8 Responses.** SelResp(t → t'; a,b) :⟺ Sel(t; 𝒯, μ, H), t' ∈ μ*(t) ⊆ 𝒯 and t' survives on H ∪ {(a,b)}. ConResp(→ t'') :⟺ t'' or its codomain is new (D13.5) and Con(t''; h, e).

> L572 | For every \((a,b)\in C\setminus H\) at which some \(t'\in\mathcal T\), also surviving on \(H\), has a different value from \(t\), the value of \(t\) at \((a,b)\) is underdetermined by \(H\)

**D12.9 Value at a pair; underdetermination.** value_t(a,b) := (τ(a), σ(b), (L^E_k(τ(a),σ(b)))_{k∈J_E}); members of 𝒯 share the codomain's ports and components **[I71]**. Underdet(t; a,b; 𝒯, H) :⟺ some t' ∈ 𝒯 surviving on H has value_t'(a,b) ≠ value_t(a,b) (FC80).

**Vague.** 'No member of the history represents' (L195) is said of a set of pairs, which cannot represent; the reading as occurrences of a physical history is invented, and without it Sel is met by every transport (FC77) [I52]. 'Exactly one of three' needs Sel and Con read on one history [I53]. 'Inherited provenance' (L405, L409) is used and not defined [I54].

## 4. The claims, with their search results

Each claim: its type, the inventions it uses, its sentences quoted, its formal statement, and its result, part by part; for a counterexample, what it shows and, where short, the model; then the second check's note, and every invention the result rests on (the claim's own and the program's).

### FC77 · Without a physical witness, selection is met by every transport

*follows from the definitions as written.* Inventions it uses: I48, I52.

> L195 | The transport \(t\) is a member of \(\mathcal T\) that survived.

> L205 | in (R), \(\operatorname{Sel}(t)\) and \(\operatorname{Con}(t)\) abbreviate \(\operatorname{Sel}(t;\mathcal T,\mu,H)\) and \(\operatorname{Con}(t;h,e)\) for some such parameters

**Formal.** Read with no physical witness: for every t, Sel(t; {t}, id, ∅) holds (fidelity on ∅ is vacuous, and an empty history holds nothing that represents). Then (R) reduces to 'some faithful transport exists'. With I52, Sel needs a physical selection history; test which of I52's requirements block the trivial witness.

**Result: COUNTEREXAMPLE FOUND.** Rests on I18 (Hom is a condition on τ as a whole, not at a pair) and I52 (Sel with 𝒯 = {t}, μ the identity). The trivial witness exists exactly for the transports whose τ is a homomorphism.

- *with H = ∅ and an empty selection history* (for all): **counterexample found** (494 models).
  Searched: every transport t has Sel(t; {t}, id, ∅) when Θ admits t (fidelity on ∅ vacuous)
  Sel(t; {t}, id, ∅) fails for this transport although H = ∅ and the selection history is empty: fidelity on ∅ is not vacuous, because (F2)'s homomorphism clause is a condition on τ as a whole (I18), and here Hom(τ) fails. Every transport whose τ is a homomorphism is 'selected' by these parameters; one whose τ is not, is not.
  [The program's printout of the model, 131 words, is not given here; the sentence above states what it shows.]
- *the trivial witness exactly when τ is a homomorphism* (for all): **holds on all models tried** (8,640 models).
- *which of I52's requirements block the trivial witness* (computation): **computed: as claimed**.

**The second check.** Worked by hand: with τ([p0=0]) = 1, τ([alt]) = [alt] and τ([p0=0,alt]) = [p0=0], τ([p0=0])·τ([alt]) = [alt] ≠ τ([p0=0,alt]), so the homomorphism clause fails, and it is not relative to pairs (D5.7, I18); so Sel(t; {t}, id, ∅) fails, against 'fidelity on ∅ is vacuous'. FC77's point survives: (R) itself asks Faithful_C(t), which includes the homomorphism clause, so every t that can figure in (R) has the trivial witness Sel(t; {t}, id, ∅). Only its 'for every t' is too wide.

**Rests on:** I18, I48, I52, I77, I78, I81, I90.

### FC78 · Exactly one of three provenances

*a result the text states.* Inventions it uses: I52, I53, I54.

> L193 | has exactly one of three provenances, determined by its history in the physical module:

> L201 | Construction may operate on selected material. Selection may continue to operate beneath construction.

**Formal.** Under I53, Sel(t) ∧ Con(t) is impossible and Dec(t) := ¬Sel ∧ ¬Con, so exactly one holds. Under I53's alternative there are histories with Sel on one part and Con on another. Per part (I54), exactly one holds of each part.

**Result: COUNTEREXAMPLE FOUND.** Rests on D12.1's reading of L195 (I52: no occurrence represents t, H or the survival condition), I53 (one history), I56 (Prepares a primitive) and I90 (Θ by hand). L201's stronger sentence would exclude it; the formal core does not use L201.

- *exactly one provenance under I53* (computation): **computed: not as claimed**.
  Searched: Sel(t) ∧ Con(t) is impossible on one history
  One history h: o1 represents the organization t carries to (its codomain), a construction trace in h prepares t (Prepares, I56), no occurrence represents t, H or the survival condition, and t (the pole's forward transport) is faithful on H = {(1,b1_45)}, whose pair occurs. Sel(t; {t}, id, H): yes. Con(t; h, e): yes. D12.1 follows L195 ('No member of the history represents t, H, or the survival condition'), which does not forbid a represented codomain; L197 lets Con hold through 'the organization it carries to'. L201's stronger sentence ('a selected transport has no represented target … in its history') would exclude it, and the formal core does not use it. Θ is supplied by hand here (I90).
  [The program's printout of the model, 559 words, is not given here; the sentence above states what it shows.]

**The second check.** Worked by hand: the history is set by hand (I90); one occurrence represents t's codomain, Prepares holds, every pair of C occurs, and nothing represents t, H or the survival condition. D12.1 forbids only representations of t, H or the survival condition (L195), so Sel holds; D12.2 lets Con hold through 'the organization it carries to' (L197), so Con holds too. I53's own gloss ('Sel has none') imports L201's clause, which D12.1 does not contain: the formal core is at odds with itself here. If the represented item is t itself rather than its codomain, Sel fails; everything turns on the codomain. FC81 (d) and FC82 use the same history and are one finding with FC78, not three. See H05.

**Rests on:** I52, I53, I54, I56, I90, I92.

### FC79 · Survival is how the transport got there; fidelity is what it is

*a sentence that stood unchanged through every revision; follows from the definitions as written.* Inventions it uses: I49, I52.

> L41 | Whether that transport is faithful on changes it was never selected against turns on the transport and the target alone, not on whether it survived.

> L41 | Survival is how the transport got there; fidelity is what it is.

**Formal.** Faithful_C(t) is a function of (D, E, t, C); Sel(t;𝒯,μ,H) of (t, 𝒯, μ, H, the selection history). No clause of Faithful takes 𝒯, μ or H, so two transports alike in (D, E, t) have the same Faithful value on every C.

**Result: HOLDS ON ALL MODELS TRIED.**

- *fidelity takes no population* (by construction): **holds by construction**.

**Rests on:** I49, I52.

### FC95 · A system can represent a theory in error

*a result the text states.* Inventions it uses: I48, I52.

> L211 | A system can represent a theory in error: the transport from carrier to content is faithful while the transport from the content's target to the content fails.

**Formal.** There are o, a content c = (E_c, C_c, Γ_c) and its target D_c with Rep_ℓ(o,c) and ¬Faithful for the candidate's transport t_c: D_c → E_c.

**Result: HOLDS ON ALL MODELS TRIED.**

- *a system can represent a theory in error* (computation): **computed: as claimed**.

**Rests on:** I48, I52, I90, I92.

## 5. The inventions these rest on

In full: each invention this part is the first of the parts to use. Then, for an invention given in full in another part that a counterexample here rests on, what was invented. Then the rest by title. I77 and I78, the bounds and families of the search, are described in section 1 and given in full in another part.

### I48 · Contents, 'c's contract', and transports into a content

Fills in for:

> L169 | A **content** is an organization together with its contract-relative commitments.

> L205 | faithful on \(c\)'s contract, whose provenance is selected or constructed

> L413 | both faithful on \(c\)'s contract at grain \(\ell\).

**Invented.** A content is c = (E_c, C_c, Γ_c) with C_c ⊆ A_Ec × B_Ec a contract on c's own organization (for the organization of a candidate for p: C_c := τ[C_p]). A transport t: X → E_c is faithful on c's contract when it meets (F1) and (F2) on the preimage {(a,b) ∈ A_X × B_X : (τ(a),σ(b)) ∈ C_c}, with Γ_c as the active components; a transport from c is faithful on C_c directly.

**Other choices.** (a) a separately declared contract on the carrier's organization. (b) faithfulness on C_c read through a declared inverse of τ.

**Used by:** claims of this part: FC77, FC95; 2 other claims. Counterexamples resting on it: FC77.

### I52 · Selection: the parameters witnessed in a physical history

Fills in for:

> L195 | There is a population \(\mathcal T\) of candidate transports, a variation operator \(\mu\) on \(\mathcal T\), a finite history \(H\subseteq C\) of edit–boundary pairs actually encountered, and a survival condition requiring fidelity on \(H\).

> L195 | No member of the history represents \(t\), \(H\), or the survival condition.

**Invented.** μ: 𝒯 → P(𝒯); the survival condition is Faithful_H (narrow). Sel(t;𝒯,μ,H) also requires a physical selection history h_sel in which the pairs of H occur and the members of 𝒯 are admitted by the physics (L481), and in which no occurrence represents (R) t, H or the survival condition. 'Member of the history' is read as an occurrence of h_sel, since the members of H are pairs and cannot represent.

**Other choices.** (a) a purely formal Sel with no physical witness (then 𝒯 = {t}, μ the identity and H = ∅ make every transport 'selected': FC77). (b) H required to be nonempty.

**Used by:** claims of this part: FC77, FC78, FC79, FC95; 5 other claims. Counterexamples resting on it: FC77, FC78, FC81, FC82, FC83, FC102.

### I53 · 'Exactly one of three provenances': one whole history

Fills in for:

*(L193, quoted above.)*

> L201 | Neither provenance is reducible to the other: a selected transport has no represented target and no criticism in its history; a constructed one has both.

**Invented.** Sel and Con are evaluated on one history: the whole physical history of t up to the attribution. Con then excludes Sel (Con puts a represented target in that history; Sel has none).

**Other choices.** (a) Sel and Con evaluated on different parts of the history (then both can hold, as L201's 'Construction may operate on selected material' allows, and 'exactly one' needs a rule of precedence).

**Used by:** claims of this part: FC78; 3 other claims. Counterexamples resting on it: FC78, FC81, FC82.

### I54 · Inherited provenance: a rule of carrying over, per part

Fills in for:

*(L211, quoted above.)*

*(L405, quoted above.)*

> L409 | Use does not by itself construct: received content used as it was received keeps its inherited provenance.

**Invented.** Provenance is assigned to each part of a transport (each component with its counterpart binding). A content-preserving transfer (relay, record) from carrier o to carrier o' gives each part at o' the provenance it had at o; a binding newly built gets Con; 'inherited' is not a fourth value but the rule by which Sel, Con and Dec carry over.

**Other choices.** (a) 'inherited' as a fourth provenance value. (b) provenance per whole transport only (then L405's 'the rest of the content keeps' cannot be written).

**Used by:** claims of this part: FC78; 1 other claim. Counterexamples resting on it: FC78.

### I56 · Build: 'prepares', 'nontrivial binding construction', 'content-preserving transfer'

Fills in for:

> L405 | **Construction.** \(\operatorname{Build}_{\beta,\ell}(s,c,h,e)\) is met when an actual subhistory owned by \(s\) and delimited at \(e\) prepares a represented organization for explanatory use of \(c\), contains a nontrivial binding construction relevant to that use, and is not a composition of content-preserving transfers.

**Invented.** Build := for some subhistory h' of h ending at e and owned by s, Prepares(h',c), BindingConstruction(h',c) and not TransferComposite(h'), with the three as primitive predicates read through the physical module.

**Other choices.** (a) Build defined through Con (a construction trace). (b) BindingConstruction defined through reason use (L409).

**Used by:** 3 other claims. Counterexamples resting on it: FC78, FC81, FC82, FC83.

### I71 · The 'value' of a transport at a pair (Argument 3)

Fills in for:

> L572 | at which some \(t'\in\mathcal T\), also surviving on \(H\), has a different value from \(t\)

**Invented.** value_t(a,b) := (τ(a), σ(b), (L^E_k(τ(a),σ(b)))_{k in J_E}): the translated pair and the relations the transport's organization has there. Members of 𝒯 share the codomain's ports and components and differ in relations; Argument 3's 'L_j(a,b) altered' is read as L^E_j(τ(a),σ(b)) altered.

**Other choices.** (a) the prediction Ans_E(τ(a),σ(b)) only. (b) the π-image of Sol_D(a,b).

**Used by:** 2 other claims.

### I90 · The physical module supplied by hand: histories and provenance as free predicates

Fills in for:

> L31 | the **physical module** \(\Theta\), which says what organization a physical occurrence instantiates at a grain

*(L195, quoted above.)*

> L197 | There is an episode (Part X) whose construction trace prepares \(t\), and in which \(t\), or the organization it carries to, is available as a represented target.

> L405 | prepares a represented organization for explanatory use of \(c\)

**Invented.** Where the formal core reads something through Θ (which occurrences represent what, which pairs occur, whether the physics admits a population, Prepares, BindingConstruction, TransferComposite, Attempt, Integrated), the program sets it by hand as a finite relation. 'The organization it carries to is a represented target' is an occurrence representing t's codomain. Transports and their fidelity are computed; the rest is stipulated. A model built so shows what the definitions allow, not what any physics does.

**Other choices.** (a) a toy physics from which these relations are computed (e.g. occurrences as small organizations with Rep computed by (R)), which meets the build → prov → rep loop of FC98. (b) leaving every claim that needs Θ untested.

**Used by:** claims of this part: FC77, FC78, FC95; 5 other claims. Counterexamples resting on it: FC77, FC78, FC81, FC82, FC83.

### I18 · The homomorphism clause of (F2): its range, and that it is not pointwise

**Invented** (given in full in another part). τ(1) = 1, and for all a1, a2 in dom τ with a2·a1 defined in A_D, τ(a2)·τ(a1) is defined in A_E and equals τ(a2·a1). The clause is a condition on τ as a whole, not at a pair; '(F2) at a pair' means only the valuation equation there.

### I81 · Transports as port translations; computed ports; generated candidates; the transport space searched for ≡

**Invented** (given in full in another part). π is induced by port translations: each port of E reads a tuple of D's ports through a value map (I14's case is one port and a map κ; several ports, a 'computed port', are used only for the term ports of the Leibniz candidate, FC63); π is then total. τ and σ are finite maps. Generated candidates: E's ports a subset of D's (optionally recoded by value maps), its components the projections of groups of D's components at each pair (an encoding candidate, I32's E_enc), τ and σ the identity or random, with background components and one perturbed relation at random; also random organizations with random τ, σ, λ (λ(k) chosen to cover k's footprint), and lookups (FC23). For ≡ (FC85) the transports searched are π and λ the identity on shared names with τ and σ every map, so 'no transport exists' is shown only over that space.

### I92 · The pole in exact arithmetic, with its grids, baseline, contracts and fibre query

**Invented** (given in full in another part). Values of L are exact numbers r + s√3 (cot 30° = √3, cot 45° = 1, cot 60° = √3/3); X_L is the set of values H cot θ on the grid H ∈ {1,2,3}, θ ∈ {30°,45°,60°}; boundaries are the nine pairs (u_H, u_θ); b0 = (1, 45°); C1 holds the single settings of H and θ at b0, C2 adds the single settings of L, C2* adds the composites that set L with H or θ. The fibre query returns {H ∈ X_H : H cot θ = L} for the single value of (θ, L) in Sol, ⊥ when that value is not single. E_rev's components are c'_L (L = u_H cot u_θ, from the boundary), c'_θ and c'_H (H = L tan θ), with λ as in model/cases.py.

Named by title only (given in full in another part): I49, 'Faithful' and 'fidelity': the narrow extent by default, the wide one where a line asks for it; I50, A violation at a pair: which conditions fail; I51, 'Prediction' for a transport not said to reach the simulation layer; I77, Finite models and the bounds of the search; I78, Two families of generated organizations: surgical edits with override, and free edits.

## 6. Choices no register entry records

Found by the two checks. U-entries come from the check that re-ran the program; H-entries from the check that read the maths against the text, in its wording.

### H05 · Selection limited by L195 alone; L201 and L411 left out (D12.1)

*(L193, quoted above.)*

*(L195, quoted above.)*

> L197 | in which \(t\), or the organization it carries to, is available as a represented target.

*(L201, quoted above.)*

> L411 | Construction is not selection. A selected transport has no represented target in its history; a constructed one does.

- **Added.** D12.1 forbids only occurrences that represent t, H or the survival condition.
  - By L197, a represented target is "\(t\), or the organization it carries to". So a represented codomain is left open in Sel's history, and so is a criticism.
  - L411 is quoted nowhere in the formal core, the formal claims or the register. L201's clause is quoted in the register under I53 and nowhere in the formal core or the claims; FC78 quotes another sentence of L201, and NF07 sets L201 aside for the word "reducible".
  - The register's own I53 says "Con then excludes Sel (Con puts a represented target in that history; Sel has none)". D12.1 does not encode "Sel has none".
- **Recorded, and not.** the search-results file names L201 under FC78, but the register has no entry for the choice. I52 lists as other choices only "no physical witness" and "H required to be nonempty"; I53 lists only Sel and Con "evaluated on different parts of the history".
- **Other choice.** Sel's history contains no represented target (neither t nor the organization it carries to) and no criticism, as L201 and L411 state of every selected transport.
- **Depends on it.** FC78, FC81 (d), FC82 and FC83 all use the history of `prov_counterexample()`, in which occurrence o1 represents the codomain.
  - With L201 and L411 read into Sel [computed by the check], Sel on that history fails and Con holds. FC78's "exactly one" then holds, the surprise of FC81 (d) does not arise, and the selection response of FC82 and FC83 fails.
  - FC84's second sentence also rests on this entry.

### H09 · The population: D12.1's "the members of 𝒯 are admitted by the physics" against L481's "The population is the set" (D12.1, D15.8, model)

> L481 | The population is the set of transports the physics and the stated construction admit; a transport that would need a part every member of the population is built without is not in it.

- **Added.**
  - D15.8 writes 𝒯 := {t : Θ admits t ∧ parts(t) ⊆ …}, an equality. D12.1 asks only that "the members of 𝒯 are admitted by the physics", an inclusion.
  - The model's witnesses use 𝒯 = {t} and μ the identity: a population of one, with no variation.
  - "parts(t)" is not defined or registered.
- **Other choices.**
  - 𝒯 is the whole admitted set, as L481 has it.
  - Or a population with a variation operator that moves something (L155: "the surviving member of a population under a variation-and-survival history").
- **Depends on it.** The witnesses of FC77, FC78, FC81 (d), FC82 and FC83. No status changes on these models, since Θ is set by hand (I90) and could admit {t} alone. The remark under FC77 in the search-results file, "(R) keeps content from 'selected' only through Θ's admission of t, through Hom, or through a requirement of a nonempty history" leaves out L481's equality.

### H13 · "actually occurring" as a primitive with no entry (D11.5)

> L217 | For an edit–boundary pair \((a,b)\in C\) actually occurring:

- **Added.** Occurs(a, b, ξ), "a primitive read through Θ". D0.2 lists it, the only listed primitive with no invention number.
- **Depends on it.** Sel (D12.1: "its pairs having occurred"), Surp (FC81) and FC102 (a), which was not tested.

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
