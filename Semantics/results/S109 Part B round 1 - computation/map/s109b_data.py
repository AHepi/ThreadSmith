# S109 Part B round 1: what the one Opus agent records by hand for each variant (rules 5 and 6): how it is implemented,
# the inventions with their other choices, its meaning (old → new of each part of the explanation definition that moves),
# and its edges with their standing. The builder (s109b_map_build.py) joins this with the computed scope (section runs)
# and the whole-suite results. Standing: "computed" (a run shows it), "contradicted" (a run shows the opposite), "claimed
# only" (no run decides it; a reading of the text).
PARTS = ("(E)", "Dec", "Expl", "(Suff)", "(Nec)")

V = {}


def v(id_, **kw):
    kw["id"] = id_
    V[id_] = kw


# ---------------------------------------------------------------- B1
v("PB1.1", section="B1", free=["D3.5"], kind="replace", carry="V1.7 (a)", impl="yes", switch="S109B_VARIANT=PB1.1 (core.nonvacuous)",
  readings=["PB1.1"], suite=["B1 PB1.1"],
  inventions=["none new: drops I27 (Excl a primitive); other choice: I27 kept"],
  meaning=[("(E): NonVacuous", "Sol_D(1,b0) ≠ ∅ ∧ (A×B)∖C ⊆ Excl(Σ), Excl(Σ) a declared input (I27)", "Sol_D(1,b0) ≠ ∅ (Excl(Σ) := (A×B)∖C, so Stated holds of every question)")],
  scope_note="On every question the program builds Excl(Σ) already equals (A×B)∖C (I85), so no worked, owner's or generated case moves; the hand case with Excl(Σ) = ∅ (the pole's forward candidate on C1) enters: Acc F → T (small cases).",
  edges=[("moves", "X:NonVacuous, X:(E)", "computed", "e1.51", "the hand case: NonVacuous F → T, Acc F → T"),
         ("constrains", "D6.6", "computed", "e1.49", "NonVacuous's second conjunct holds of every candidate under PB1.1"),
         ("blocks", "L43.s4, L159.s1 (FROZEN)", "claimed only", "e1.48", "the requirement that the exclusion be stated has nothing to read"),
         ("changes with", "D0.2 (FROZEN; I27)", "claimed only", None, "Excl leaves the primitives")])
v("PB1.2", section="B1", free=["D3.1"], kind="strengthen", carry="R2V1.9 (b)", impl="nearest reading", switch="S109B_VARIANT=PB1.2, S109B_THETA=all or strict (core.is_question)",
  readings=["PB1.2 Θ all", "PB1.2 Θ strict"], suite=["B1 PB1.2-strict"],
  inventions=["S109-B1-I1: Θ_admits of a bare edit, which the program never computes: 'all' (Θ admits every edit: the program's worlds) or 'strict' (Θ admits the identity only: the reading on which no edit of a mathematical target is admitted); others: Θ_admits of an edit of an attributed organization at a grain (the text's words at L159.s3); of the pair (a,b)"],
  meaning=[("domain of (E), Expl, (Suff), (Nec)", "p a question: C ⊆ A×B, (1,b0) ∈ C", "… ∧ ∀(a,b) ∈ C: Θ_admits(a); a contract holding an edit Θ does not admit names no question")],
  scope_note="Θ 'all': nothing moves (the code path is the default's). Θ 'strict': every contract holding an edit other than 1 names no question: 36 of 49 cases leave (0 enter), among them the owner's two-part sign and weathervane with the change read as an edit or mixed; with the change read as a boundary both stay (their contracts hold the identity edit only); 813 of 999 generated accounts leave; 18 claims move.",
  edges=[("blocks", "L159.s3, L49.s4 (FROZEN)", "claimed only", None, "admitting a change is not a claim that it can be carried out"),
         ("constrains", "Θ (D0.1)", "claimed only", None, "Θ_admits must be read of a bare edit"),
         ("moves", "X:(E) (its domain), X:Expl", "computed", None, "Θ strict: 36 cases, 813 generated leave")])
v("PB1.3", section="B1", free=["D3.2"], kind="replace", carry="R2V1.8 (b)", impl="yes", switch="S109B_VARIANT=PB1.3 (core.is_question)",
  readings=["PB1.3"], suite=["B1 PB1.3"],
  inventions=["S109-B1-I2: Y_p ⊆ X_δD checked at the pairs of C (others: at every pair of A×B); a designation that is not one port (the fibre query's (H,T,L)) names no question"],
  meaning=[("domain of (E); what (A) and Contrast compare", "Q(O,a,b;δ) ∈ Y_p ∪ {⊥}, Y_p free (I21)", "Y_p := X_δD: a query with an answer outside X_δD ∪ {⊥} names no question")],
  scope_note="The pole's identification question C_id (fibre query) leaves (Acc T → F); nothing else, no generated case (every generated query reads a port), no claim.",
  edges=[("constrains", "D3.3 (FROZEN)", "claimed only", None, "Ident and Obst have no question"),
         ("moves", "X:(E) (its domain)", "computed", None, "C_id leaves"),
         ("changes with", "E2, E4, E9 (FROZEN)", "claimed only", None, "their non-port queries name no question")])
v("PB1.4", section="B1", free=["D4.2"], kind="replace", carry="R2V1.7 (b)", impl="yes", switch="S109B_VARIANT=PB1.4 (core.footprint_bijections)",
  readings=["PB1.4"], suite=["B1 PB1.4"], inventions=["none new: drops I10 (β); other choices: β as now; β keeping an order"],
  meaning=[("none of the five parts", "j ~_C j′ :⟺ ∃β …", "j ~_C j′ :⟺ V_j = V_j′ (ordered) ∧ sig_C(j) = sig_C(j′)")],
  scope_note="No case moves (no conjunct reads a kind). FC05 (ii) and FC103.new1 (b) (Argument 2's 'one kind' for E9's exchanged pair) move.",
  edges=[("changes with", "D4.3", "computed", "r2e1.34", "FC103.new1 (b): k1 and k2 no longer of one kind"),
         ("moves", "nothing in the definition; Arguments 1-2's claims", "computed", None, "FC05, FC103.new1")])
v("PB1.5", section="B1", free=["L155.s6"], kind="replace", carry="R2V1.4 (b)", impl="yes (read by no claim)", switch="core.found()",
  readings=["PB1.5"], suite=[], inventions=["which values count as found (other: all three, which makes Found vacuous)"],
  meaning=[("none of the five parts", "Found(p) requires ρ_p = constructed", "Found(p) :⟺ ρ_p ∈ {selected, constructed}")],
  scope_note="Nothing moves: no conjunct of (E), Dec or the defeat sets reads Found (FC30), and no claim calls it; the whole suite was not run (its code path is the default's).",
  edges=[("changes with", "D3.4 (FROZEN)", "claimed only", "r2e1.30", "Found's clause"),
         ("constrains", "(QF) (L544)", "claimed only", None, "Found is (QF)'s subject")])
v("PB1.6", section="B1", free=["L103.s1", "D1.3"], kind="replace", carry="–", impl="yes", switch="S109B_VARIANT=PB1.6 (core.Org.L)",
  readings=["PB1.6"], suite=["B1 PB1.6"],
  inventions=["the empty-relation deletion; the absent-port clause not implemented (the program adds no absent port); others: the full relation (as now); removal from J (needs I03 moved)"],
  meaning=[("(E): Dependence (NC2's Lost, through D6.1's E−G)", "E−G: every component of G imposes the full relation", "E−G: every component of G imposes the empty relation; so Sol_{E−G} = ∅ and Ans_{E−G} = ⊥ wherever G's footprints are nonempty")],
  scope_note="61 generated candidates enter (Dep F → T; all E_enc-family with a commitment empty somewhere), the reply's idle-commitment case enters (Acc F → T); no worked or owner's case moves; FC-E's restriction line changes (E|{k} gives ⊥); FC01 (a) (deletion keeps solutions) fails.",
  edges=[("moves", "X:Dependence, X:(E)", "computed", None, "61 generated enter"),
         ("changes with", "D6.1, D7.1 (restriction)", "computed", None, "FC-E1's restriction to {k} answers ⊥"),
         ("constrains", "D3.6 (FROZEN)", "claimed only", None, "an absent port")])
v("PB1.7", section="B1", free=["L141.s2", "D3.1"], kind="strengthen", carry="–", impl="yes", switch="S109B_VARIANT=PB1.7 (core.is_question)",
  readings=["PB1.7"], suite=["B1 PB1.7"], inventions=["'some edit other than 1' (others: some edit no relabeling; two pairs with different answers)"],
  meaning=[("domain of (E)", "(1,b0) ∈ C", "(1,b0) ∈ C ∧ ∃(a,b) ∈ C: a ≠ 1")],
  scope_note="8 cases leave: C_id and every encoding of the owner's sign and vane with the change read as a boundary (contracts {1}×B); with the change as an edit or mixed both stay; 186 generated leave; FC25.new2 (a) fails. Its drops are a subset of Part A's C5's: equal on every worked and owner's case, C5 drops 80 generated more (comparisons with Part A).",
  edges=[("moves", "X:(E) (its domain)", "computed", None, "8 cases, 186 generated leave"),
         ("constrains", "L257, D6.9 (FROZEN)", "claimed only", None, "the relabeling exclusion vacuous on baseline-only contracts")])
v("PB1.8", section="B1", free=["L115.s1", "D4.1"], kind="strengthen", carry="– (lifts e1.00)", impl="yes", switch="S109B_VARIANT=PB1.8 (core.sig_fn, one_kind)",
  readings=["PB1.8"], suite=["B1 PB1.8"], inventions=["Sol_D(a,b)↾V_j as the fourth component (others: Sol of {j} alone; the baseline only)"],
  meaning=[("none of the five parts", "sig_C(j) = {(a,b,L_j(a,b))}", "sig⁺_C(j) = {(a,b,L_j(a,b),Sol_D(a,b)↾V_j)}")],
  scope_note="No case moves; FC05 fails ((i) signatures use relations only; (ii) reading (i)); FC17, FC18 hold (the reply's 'FC18 at risk' does not happen).",
  edges=[("changes with", "D4.4", "computed", "e1.00", "FC17, FC18 unchanged"),
         ("blocks", "L119 (FROZEN): kinds 'not from the values its ports take in a solution'", "computed", None, "FC05 (i)"),
         ("changes with", "FC18 (Argument 1: a same-kind condition adds nothing), the reply's 'at risk'", "contradicted", None, "FC18 holds under PB1.8")])
v("PB1.9", section="B1", free=["L113.s1", "D4.1", "D4.2", "D4.3", "D4.4"], kind="replace", carry="–", impl="yes", switch="S109B_VARIANT=PB1.9 (core.one_kind)",
  readings=["PB1.9"], suite=["B1 PB1.9"], inventions=["S109-B1-I3: A×B read as every pair both readings reach (others: C, as now; C ⊆ C′ ⊆ A×B)"],
  meaning=[("none of the five parts", "kinds: classes of ~_C", "kinds: classes of ~_{A×B}")],
  scope_note="No case moves; FC04 (b) (a finer contract can separate) finds no witness, FC05 and FC16 fail.",
  edges=[("blocks", "L119 (FROZEN): kinds relative to the contract", "computed", None, "FC04 (b), FC16"),
         ("constrains", "L11.s2 (FROZEN)", "claimed only", None, "reads more nearly this way")])
# ---------------------------------------------------------------- B2
v("PB2.1", section="B2", free=["L189.s2"], kind="replace", carry="R2V2.7 (a)", impl="yes", switch="S109B_VARIANT=PB2.1 (core.faithful; claims_b.faithful_on, viol_at)",
  readings=["PB2.1"], suite=["B2 PB2.1"], inventions=["none new: I49's wide extent (others: narrow; wide at L220 only)"],
  meaning=[("Dec (Sel's Faithful_H, Held, Rep, T′) and Expl", "Faithful_C := F1 ∧ F2; Faithful_H without (A); Viol narrow", "Faithful_C := F1 ∧ F2 ∧ A; Faithful_H with (A) at H; Viol := Viol⁺")],
  scope_note="No worked, owner's or generated case moves on the hand-set histories (their selection pair is answered right); FC104.new1 (b)'s selected transport, wrong in its answer at its own H, is no longer selected (Sel F): declared, so no explanation there; FC67 (invertible recodings keep fidelity) fails. The bridge's chain reads Held by hand: stays.",
  edges=[("changes with", "D5.7, D12.7 (FROZEN)", "computed", "r2e2.14", "FC104.new1 (b)"),
         ("blocks", "L221.n1, L223.s3 (FROZEN)", "computed", "r2e2.14", "FC104.new1 (b): no Sel with Viol⁺ inside H"),
         ("moves", "X:Dec, X:Expl", "computed", None, "FC104.new1 (b)"),
         ("blocks", "invariance of fidelity under recoding (FC67)", "computed", None, "FC67")])
v("PB2.2", section="B2", free=["D5.5", "L241.s1"], kind="weaken", carry="–", impl="yes", switch="S109B_VARIANT=PB2.2 (core.F2; faithful_on)",
  readings=["PB2.2"], suite=["B2 PB2.2"], inventions=["none new: I18's dropped choice"],
  meaning=[("(E): (F2); Dec through Faithful_H", "F2_C := F2eq_C ∧ Hom(τ)", "F2_C := F2eq_C")],
  scope_note="The reversed calculation under τ′ on C1 enters (Acc F → T: identification presented as production); the relabeling candidate (τ(1) ≠ 1) moves on the Sel history only (Faithful_H loses Hom); 11 generated enter; FC27.new1 (c) and FC77 move.",
  edges=[("moves", "X:(F2), X:(E)", "computed", None, "1 worked, 11 generated enter"),
         ("blocks", "L271.s1 (FROZEN): the reversed calculation fails (F2) on the production contract", "computed", None, "FC27.new1 (c)"),
         ("blocks", "L257.n3 (FROZEN)", "claimed only", None, "not run as the reply's FC21 (d)")])
v("PB2.3", section="B2", free=["D5.4"], kind="strengthen", carry="–", impl="nearest reading", switch="S109B_VARIANT=PB2.3 (core.F1_at)",
  readings=["PB2.3"], suite=["B2 PB2.3"], inventions=["S109-B2-I1: a component of E with no counterpart in λ fails (F1) (others: exempt; (F1) over J_E minus input assigners)"],
  meaning=[("(E): (F1)", "∀k ∈ Γ: proj^λ Sol_λ(k) = L_k", "∀k ∈ J_E: …")],
  scope_note="214 generated leave (mostly E_enc candidates whose background component has no counterpart: I1 decides it); no worked or owner's case moves; the reply's small case (an added k1 with no counterpart) leaves.",
  edges=[("moves", "X:(F1), X:(E)", "computed", None, "214 generated leave"),
         ("constrains", "L231.s2, L245.s4 (FROZEN)", "claimed only", None, "background as named background")])
v("PB2.4", section="B2", free=["D5.6", "L249.s1"], kind="weaken", carry="–", impl="yes", switch="S109B_VARIANT=PB2.4 (core.A_at)",
  readings=["PB2.4"], suite=["B2 PB2.4"], inventions=["S109-B2-I2 (the reply's PB2-In2): (A) over Det_C (others: C, as now; Det_C ∪ both ⊥)"],
  meaning=[("(E): (A)", "∀(a,b) ∈ C: Ans_E = Ans_p (⊥ = ⊥)", "∀(a,b) ∈ Det_C: Ans_E = Ans_p")],
  scope_note="Meaning moves, scope unchanged on every case computed (49 cases, 17,280 generated, FC-E, CT); the reply's small cases fail (F1) and (F2) on and off; FC21 (a2), FC96 (i) and FC109 fail (two candidates both meeting (A) with different answers at ⊥ pairs).",
  edges=[("blocks", "L369.s2 (B2)", "claimed only", None, "not computed"),
         ("changes with", "D6.4, D8.2 (FROZEN)", "computed", None, "FC96 (i): (A) for both no longer gives equal answers"),
         ("moves", "X:(A)", "computed", None, "meaning only: no candidate enters"),
         ("moves", "X:(E): 'enter: candidates that determine an answer where the target gives ⊥' (the reply)", "contradicted", None, "none enters on any case computed; the reply's own case fails (F1), (F2)")])
v("PB2.5", section="B2", free=["D6.2"], kind="strengthen", carry="–", impl="nearest reading", switch="S109B_VARIANT=PB2.5, S109B_NC0=bg or bg-input (core.NC0, dep)",
  readings=["PB2.5 bg", "PB2.5 bg-input"], suite=["B2 PB2.5-bg", "B2 PB2.5-bg-input"],
  inventions=["S109-B2-I3: 'carries Ans_p' read as Pin (D6.3's clause at one pair) by a background component (k ∉ Γ): 'bg' any, 'bg-input' one that assigns an input port of E (Roles(E)); other: I23's gloss (NC0 always true)"],
  meaning=[("(E): Dependence", "NC0 (true) ∧ NC2", "NC0′ ∧ NC2, NC0′ :⟺ no background component pins δ_E to Ans_p at a pair of C")],
  scope_note="'bg': E5's eliminative candidate (FC62's encoding) leaves, 149 generated leave, FC23.new1 and FC62 fail; 'bg-input': 12 generated leave, no claim moves. The owner's four cases stay. The reply's small case fails (F2) and (A) with and without the variant.",
  edges=[("moves", "X:Dependence, X:(E)", "computed", None, "149 / 12 generated leave"),
         ("constrains", "D6.5 (FROZEN)", "claimed only", None, "NC0 stays a conjunct")])
v("PB2.6", section="B2", free=["D6.6"], kind="weaken", carry="–", impl="yes", switch="S109B_VARIANT=PB2.6 (core.nonvacuous)",
  readings=["PB2.6"], suite=["B2 PB2.6"], inventions=["I27 'no conjunct' (others: as now; V1.7)"],
  meaning=[("(E): NonVacuous", "Sol_D(1,b0) ≠ ∅ ∧ Stated(C,Σ)", "Sol_D(1,b0) ≠ ∅")],
  scope_note="As PB1.1 on every case computed: nothing moves on the program's questions; the hand case with Excl(Σ) = ∅ enters (the same code path's value).",
  edges=[("moves", "X:NonVacuous", "computed", "e1.51", "as PB1.1"),
         ("changes with", "PB1.1 (V1.7)", "computed", None, "the same (E) on every case")])
v("PB2.7", section="B2", free=["D5.6"], kind="re-order a dependence", carry="–", impl="yes", switch="S109B_VARIANT=PB2.7, S105_SLOT_QUANTIFIER (core.A)",
  readings=["PB2.7 every", "PB2.7 some", "PB2.7 some-exempt", "PB2.7 some-exempt-set"], suite=["B2 PB2.7"],
  inventions=["none new: D6.3's quantifier (I136) computed under each reading"],
  meaning=[("(E): (A)", "A_C(ℰ)", "A_C(ℰ) ∧ NC1(ℰ) (no answer slot, D6.3)")],
  scope_note="'every': 20 cases leave (the one-part sign in every encoding, E_enc on every question, the lookups), the two-part sign and the vane stay; 'some', 'some-exempt', 'some-exempt-set': the two-part sign leaves too (every encoding); 935 / 946 / 855 / 858 generated leave. Equal to Part A's C6 (V2.4) on all 17,329 cases under each quantifier (comparisons with Part A).",
  edges=[("changes with", "D6.3 (FROZEN)", "computed", None, "the quantifier readings move (E) again"),
         ("blocks", "L269.s2 (FROZEN) with S45", "computed", None, "FC25.new2"),
         ("moves", "X:(A), X:(E)", "computed", None, "as C6")])
v("PB2.8", section="B2", free=["L311.s2", "D7.3"], kind="weaken", carry="–", impl="no code change", switch="none (every block of a finite Γ is finite)",
  readings=["PB2.8"], suite=[], inventions=["PB2-In3: B finite (other: unrestricted)"],
  meaning=[("none of the five parts", "CB(B;W) :⟺ ∅ ≠ B ⊆ W ∧ W ∈ S ∧ W∖B ∉ S", "… ∧ B finite")],
  scope_note="No part reads (S), (B), (D); on finite Γ nothing can move. On L311's infinitary example FC40 found no finite critical block in 20,000 samples, so under PB2.8 that example has no critical block at all (by argument from FC40's computed result); FC40's check is unchanged and holds.",
  edges=[("blocks", "L313.n3 (FROZEN)", "claimed only", None, "by argument from FC40")])
v("PB2.9", section="B2", free=["D5.1"], kind="replace", carry="–", impl="no code change", switch="none (π is total in the program, I81)",
  readings=["PB2.9"], suite=[], inventions=["none: I16 (partial on solutions) was never the program's; I81 builds π total"],
  meaning=[("(E): what (F1), (F2) read (the transport)", "π: X_D ⇀ X_E on Sol_D (I16)", "π: X_D → X_E total")],
  scope_note="Meaning moves, scope unchanged on every case computed: the program's π is total already.",
  edges=[("changes with", "D8.2, D8.3, D12.5", "claimed only", None, "not computed")])
# ---------------------------------------------------------------- B3
v("PB3.1", section="B3", free=["D12.4"], kind="replace", carry="R2V2.4 (b)", impl="nearest reading", switch="S109B_VARIANT=PB3.1 (claims_s41 FC30.new1 (d), (f): rec_of)",
  readings=["PB3.1"], suite=["B3 PB3.1"], inventions=["S109-B3-I1: only holdings a case names as whole-content copies inherit (the student's); the program's other chains name none"],
  meaning=[("Dec (inheritance, D12.4)", "provenance per part; a binding newly built by the copier gets its own value", "a holding reached by a copy of a carrier's whole content inherits prov(t,o) whole")],
  scope_note="The student's copy enters: Dec at o2 T → F under both H, Expl F → T; nothing else (worked cases, generated, chains, bridge, CT); FC30.new1 (d), (f) fail.",
  edges=[("moves", "X:Dec, X:Expl", "computed", None, "the student's copy"),
         ("blocks", "L405 (FROZEN): 'the rest of the content keeps its inherited provenance'", "claimed only", None, "")])
v("PB3.2", section="B3", free=["D12.5", "L207.s1"], kind="weaken", carry="–", impl="yes", switch="S109B_VARIANT=PB3.2 (claims_b._prov_step)",
  readings=["PB3.2"], suite=["B3 PB3.2"], inventions=["none new: the reading T in Sel's exclusion (I162's other choice)"],
  meaning=[("Dec (Sel's exclusion)", "Rep_ℓ(o,c) :⟺ ∃t [Faithful ∧ (Sel ∨ Con)]; Sel's exclusion reads Rep at o′ ≺ o (T′)", "Rep := Held; Sel's exclusion reads Held at o′ ≺ o (T)")],
  scope_note="10 chain outputs of 584 become declared (18 chains differ), no hand-set case, no generated case; the student's copy and the bridge stay; FC98 (e) fails (the earlier declared holder now blocks the selection).",
  edges=[("moves", "X:Dec, X:Expl", "computed", None, "10 chains"),
         ("blocks", "L211.s3, L211.s1 (FROZEN)", "computed", None, "FC98 (e)")])
v("PB3.3", section="B3", free=["L195.s1", "L195.s5"], kind="strengthen", carry="–", impl="yes", switch="S109B_VARIANT=PB3.3 (claims_b.sel)",
  readings=["PB3.3"], suite=["B3 PB3.3"], inventions=["occurrence read on h's occurs set (the hand-set Sel history lets every pair of C occur, I90) (others: up to o_t; up to e)"],
  meaning=[("Dec (Sel)", "Sel(t;𝒯,μ,H) as D12.1", "… ∧ C ∩ Occ(h) ⊆ H")],
  scope_note="On the hand-set selection history (every pair of C occurred, H = {(1,b0)}) no candidate is selected: 44 of 49 cases lose Expl on that history, the owner's sign and vane among them (every encoding), 999 of 999 generated; Acc unchanged; chains unchanged; FC102.new1, FC12.new2, FC30.new1 (e) move.",
  edges=[("changes with", "D12.1 (FROZEN)", "computed", None, "the hand-set Sel history"),
         ("moves", "X:Dec, X:Expl", "computed", None, "44 cases, 999 generated on a Sel history"),
         ("constrains", "L223.s3 (FROZEN)", "claimed only", None, "")])
v("PB3.4", section="B3", free=["L199.s1", "L199.s3"], kind="re-order a dependence", carry="–", impl="nearest reading", switch="S109B_VARIANT=PB3.4 (claims_b._prov_step)",
  readings=["PB3.4"], suite=["B3 PB3.4"], inventions=["S109-B3-I2: every held holding of a chain holds the one transport t; Sel and Con on h∪ read as 'some holding has it' (others: the last holding's, as now; the earliest's); no precedence rule (Sel and Con may both hold)"],
  meaning=[("Dec (the history)", "Dec(t,o_t) read on h(t,o_t)", "read on h∪(t) = ∪{h(t,o): t held at o}")],
  scope_note="The student's copy enters (Dec F); 82 chain outputs of 584 enter (198 differ; 16 change their number of fixed points); the bridge stays; FC12.new1, FC12.new2, FC30.new1, FC83, FC98, FC98.new1 fail; FC84.new1 (d) finds a chain with more than one fixed point (printed as an error: the claim's own message formats a tuple with %).",
  edges=[("moves", "X:Dec, X:Expl", "computed", None, "student's copy; 82 chains"),
         ("blocks", "L193.s1 (FROZEN): exactly one of three", "computed", None, "FC12.new1: Sel ∧ Con at a fixed point")])
v("PB3.5", section="B3", free=["D11.5", "L217.s2"], kind="weaken", carry="–", impl="yes", switch="S109B_VARIANT=PB3.5 (claims_b.sel)",
  readings=["PB3.5"], suite=["B3 PB3.5"], inventions=["S109-B3-I3: every boundary of H actual (others: Θ by hand, as now; the edit enacted)"],
  meaning=[("Dec (Sel's H-clause)", "H ⊆ Occ(h) (Occurs a primitive through Θ)", "H admitted (Occurs := admitted ∧ actual)")],
  scope_note="Meaning moves, scope unchanged on every case computed: every hand-set history of the program lets every pair of C occur, and FC30.new1 (e)'s link has H = ∅.",
  edges=[("changes with", "D12.1 (FROZEN)", "computed", None, "no case moves")])
v("PB3.6", section="B3", free=["D11.1", "L169.s1"], kind="strengthen", carry="–", impl="nearest reading (a case reading)", switch="S109B_VARIANT=PB3.6 (claims_s41 FC30.new1 (d))",
  readings=["PB3.6"], suite=["B3 PB3.6"], inventions=["the textbook's carrier outside the student's declared boundary (the reading); others: anywhere (as now); β plus carriers relayed in"],
  meaning=[("Dec (what histories are built from)", "Occ: physically located carriers", "Occ: those inside the declared boundary β")],
  scope_note="On that reading the student's copy with one pair tried enters (Dec F: Sel at its own holding); with H = ∅ it stays declared; FC30.new1 (d) fails; nothing else (no other case names β).",
  edges=[("moves", "X:Dec, X:Expl", "computed", None, "student's copy, on that reading"),
         ("constrains", "D16.3 (FROZEN)", "claimed only", None, "")])
v("PB3.7", section="B3", free=["D13.4", "L169.s3"], kind="replace", carry="–", impl="yes", switch="S109B_VARIANT=PB3.7 (claims_b FC85 equiv)",
  readings=["PB3.7"], suite=["B3 PB3.7"], inventions=["output equality of the port query on the first port at the pairs of C_c (others: on C_d; on C_c ∪ C_d)"],
  meaning=[("none of the five parts (New, Origin)", "d ≡_ℓ c :⟺ faithful transports both ways", "d ≡_ℓ c :⟺ Ans_d = Ans_c on C_c")],
  scope_note="No case moves; FC85 holds (its witness of a one-way match survives output equality).",
  edges=[("blocks", "L413.s1, L413.s2 (FROZEN)", "claimed only", None, "")])
v("PB3.8", section="B3", free=["L225.s4"], kind="drop", carry="–", impl="flagged out (no formal statement)", switch="none", readings=[], suite=[],
  inventions=[], meaning=[("none", "—", "—")], scope_note="Not implemented (tabulation §6).", edges=[])
# ---------------------------------------------------------------- B4
v("PB4.1", section="B4", free=["L315.s7"], kind="replace", carry="V2.8's part (a)", impl="nearest reading", switch="S109B_VARIANT=PB4.1 (args.X)",
  readings=["PB4.1"], suite=["B4 PB4.1"],
  inventions=["S109-B4-I1: 'uses its meeting (E)' read as every atom of φ among α's leaves' atoms; the defeat sets' φ (Expl_ atoms) keep D16.XV's reading (others: the instance reading everywhere; RO asking φ among α's symbols)"],
  meaning=[("none of the five parts (Out_j)", "ℰ ruled out for j :⟺ X_j('Acc(ℰ)') ≠ ∅", "… ∃α ∈ X_j with Acc(ℰ) ∈ Uses(α)")],
  scope_note="No case of (E) or Expl moves; a premise alone (¬PM) no longer rules out the design (FC72 (d), FC72.new1 (c)); FC56 (c′) moves.",
  edges=[("changes with", "D9.8 (FROZEN)", "computed", "e2.20", "FC72 (d), FC72.new1 (c)"),
         ("moves", "X:(Suff)", "claimed only", "e2.21", "under S109-B4-I1 the defeat sets do not move; the other choice not computed")])
v("PB4.2", section="B4", free=["D9.5"], kind="weaken", carry="–", impl="yes", switch="S109B_VARIANT=PB4.2 (args.Assessor.scope_ok)",
  readings=["PB4.2"], suite=["B4 PB4.2"], inventions=["which indices j declares (I42)"],
  meaning=[("(Suff), (Nec): X_j through Usable", "Scope_j(u) :⟺ C_u ⊆ C_j(u) ∧ ℓ_u = ℓ_j(u) ∧ β_u = β_j(u)", "Scope_j(u) :⟺ C_u ⊆ C_j(u)")],
  scope_note="No case of (E) or Expl moves; FC56 (a″): the coarse-grain assessor's argument becomes usable.",
  edges=[("changes with", "D9.6 (FROZEN)", "computed", None, "FC56 (a″)")])
v("PB4.3", section="B4", free=["D9.3"], kind="weaken", carry="–", impl="no code change", switch="none (every form's pattern uses all its children)",
  readings=["PB4.3"], suite=[], inventions=["what a form uses (I89's other side)"],
  meaning=[("(Suff), (Nec): X_j through Prem", "Prem(u) := children(u)", "Prem(u) := the premises Form(u) uses")],
  scope_note="Meaning moves, scope unchanged: form_ok's patterns use every child.", edges=[("changes with", "D9.6 (FROZEN)", "claimed only", None, "")])
v("PB4.4", section="B4", free=["L397.s13"], kind="strengthen", carry="–", impl="flagged out as written; computed as PB4.4′ on D9.8", switch="S109B_VARIANT=PB4.4', S109B_HELD=all or no-records (args.X)",
  readings=["PB4.4' all", "PB4.4' no-records"], suite=["B4 PB4.4p-all", "B4 PB4.4p-no-records"],
  inventions=["S109-B4-I2: the variant restated on D9.8 (the tabulation's flag); no one in the program holds a represented explanation of a premise; 'all' every accepted leaf, 'no-records' record leaves exempt (the two give the same)"],
  meaning=[("(Suff), (Nec): X_j", "X_j(φ) := {α: Usable_j(α) ∧ RO(α,φ)}", "… ∧ every premise of α taken as given has a held explanation")],
  scope_note="No case of (E) or Expl moves; every argument of the program has a premise taken as given, so X_j is empty everywhere: nothing is ruled out and the defeat sets are empty; FC23.new2 (f), FC30.new1 (a), (d), (e), (g), (h), FC47.new1, FC56, FC72, FC72.new1, FC72.new2 move.",
  edges=[("blocks", "L397.s10 (FROZEN)", "computed", None, "X_j empty"),
         ("moves", "X:(Suff), X:(Nec)", "computed", None, "the defeat sets empty")])
v("PB4.5", section="B4", free=["L383.s1"], kind="strengthen", carry="–", impl="yes", switch="S109B_VARIANT=PB4.5 (claims_b FC74, FC76)",
  readings=["PB4.5"], suite=["B4 PB4.5"], inventions=["occurrence typed with its allegation (other: retyped, not excluded)"],
  meaning=[("none of the five parts", "a criticism occurrence may lack Bearing", "Occ_criticism(c) ⇒ Bearing(c,z,p)")],
  scope_note="No case of (E) or Expl moves; FC74 (a criticism without bearing) finds no witness; FC76 fails.",
  edges=[("changes with", "D9.10 (FROZEN)", "computed", None, "FC74, FC76")])
v("PB4.6", section="B4", free=["L385.s1", "D9.11"], kind="weaken", carry="–", impl="yes", switch="S109B_VARIANT=PB4.6 (claims_b FC76)",
  readings=["PB4.6"], suite=["B4 PB4.6"], inventions=["route readings as Part A's e3.34b"],
  meaning=[("none of the five parts", "UsesReason asks an image port on an active route", "that clause dropped")],
  scope_note="Nothing moves (FC76's route is active anyway); Part A's e3.34b computed the neighbouring reading.",
  edges=[("changes with", "D11.4 (FROZEN)", "computed", "e3.34b", "no claim moves")])
v("PB4.7", section="B4", free=["L546.s1"], kind="strengthen", carry="–", impl="yes", switch="S109B_VARIANT=PB4.7 (claims_b FC109)",
  readings=["PB4.7"], suite=["B4 PB4.7"], inventions=[],
  meaning=[("none of the five parts", "list with Arguments 1-3", "list with Arguments 1-10")],
  scope_note="Nothing moves; FC109 holds with FC81, FC95, FC97-FC103 added.", edges=[("changes with", "FC109", "computed", None, "holds")])
v("PB4.8", section="B4", free=["D10.1", "L317.s1"], kind="weaken", carry="–", impl="yes", switch="S109B_VARIANT=PB4.8 (claims_r3a2 FC47.new1, claims_r4a3 FC72.new2)",
  readings=["PB4.8"], suite=["B4 PB4.8"], inventions=["whether Prob keeps ξ (other: an assessor-free core beside per-assessor problems)"],
  meaning=[("none of the five parts", "Prob_j :⟺ Riv ∧ NotOut_j ∧ NotOut_j", "Prob :⟺ Riv")],
  scope_note="No case of (E) or Expl moves; FC47.new1 (solved, posed again) and FC72.new2 (c) (no problem for j1) fail.",
  edges=[("blocks", "D10.6 (FROZEN) as written", "computed", None, "FC47.new1")])
