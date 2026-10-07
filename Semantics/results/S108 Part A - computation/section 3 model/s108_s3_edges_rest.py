# S108 Part A, section 3: the edges of V3.5–V3.8 (read by s108_s3_edges.py). Same fields and standings.


def add_rest(e):
    # ---- V3.5 D13.8 Episode(h') :⟺ h' ⊆ h a subhistory ------------------------------------------------------------------
    e("V3.5", "changes with", "L55.n3", "S1", "'An episode is a history in which every change C→C′ carries a provenance record (D13.8)' points at D13.8 and would be false of it",
      "computed", "under V3.5 FC84.new1 (c)'s chain with an unrecorded change C → C′ is an episode (S41 reading F → T); FC84.new1 (a4)'s iv-u chain: Episode F → T (cases §C); L55.n3's words no longer describe D13.8")
    e("V3.5", "moves", "Dec(t) via Episode → CT (D12.2)", "S2", "more episodes → more Con → fewer Dec → more explanations",
      "contradicted under D12.2's cut (T′, and T) for every candidate meeting (E); computed in the tag encoding and under the rejected cuts K, U",
      "worlds.chains (115,400 chains, n ≤ 4): under T′ and T, Con moves only at holdings whose t is not held there (11,240), none where it is: Acc ⇒ Faithful ⇒ held at o_t, and {o_t} alone is an episode, so the record clause never decides Con there; worked cases: 'Con-chg (chain, T′)' Dec moves 5, all Acc F; worlds.cands: 0 Account ∧ ¬Dec(t) moves on the chain histories (61,900). In the tag encoding ('Con-chg (tags)': the target labelled represented at o1 only, before the unrecorded change) every candidate meeting (E) moves in: 22 of 27 worked cases, 1,013 / 881 / 232 / 1,670 generated. Under K: 5,118 chains with a held output move (Dec T → F)",
      settle="whether D12.2's 'available as a represented target' may be read at o_t itself (Held(o_t), T′, D12.2 as written) or only at an earlier occurrence of the episode (the tag encoding; K): a reading of L197 and D12.2 against D18.1's cut")
    e("V3.5", "changes with", "D12.2's Held(o′, x) for some o′ ⪯ o_t (I162, the cut T′)", "S2", None, "added",
      "what keeps D13.8's record clause from ¬Dec(t) for a candidate meeting (E) is D12.2's o′ ⪯ o_t with Held at o_t (the chain model, T′): with o′ ≺ o_t only (K) the clause reaches 5,118 held chains; computed (worlds.chains)", named=False)
    e("V3.5", "changes with", "FC84.new1 (a3), (c), (a4); FC84.new2", "–", None, "added",
      "suite.V3.5: FC84.new1 (c) as claimed → not as claimed (the unrecorded change C → C′ is an episode under both readings; Con at o2 [T] both under the S41 reading, [F] → [T] under L55's); (a3) as claimed → not as claimed (under L55's reading iv-u's unrecorded change now moves Con, where only a recorded one did); (a4) look: Episode (base, iv-u) (T, F) → (T, T); FC84.new2 (b) witness found → none (with no record clause, P4's unordered form and the covering form cannot differ; the claim's status kept); FC32.new1 (c), FC98 (b): text only (the sinks q(o), Rec_h′, ImmAfter leave D18.1's graph)", named=False)

    # ---- V3.6 D15.8 𝒯 := {t : Θ admits t} --------------------------------------------------------------------------------
    e("V3.6", "blocks", "none found (no frozen sentence states the parts bound; L481.s3 is S3, varied with it)", "–", "–",
      "computed (search)", "grep of the template's FROZEN sentences: L195.s1 ('There is a population 𝒯 of candidate transports, a variation operator μ on 𝒯, … a survival condition requiring fidelity on H') names 𝒯 and says nothing of parts; no other FROZEN sentence names the population or the stated construction; the suite under V3.6 moves no claim's status (text only: FC32.new1 (c), FC98 (b), the sinks 'parts' and 'stated construction' leave D18.1's graph)")
    e("V3.6", "constrains", "D12.1 writes 𝒯 = D15.8's population", "S2", "the variant must still define a set 𝒯; it does",
      "computed", "under V3.6 D12.1 reads t ∈ 𝒯 through s108s3.in_population (Θ's admission alone); Sel computed on every history of §3, §6.1")
    e("V3.6", "moves", "Sel (D12.1), hence Dec and Expl; Argument 3's extent (FC80)", "S2; S4", "wider population: more Sel, fewer Dec, wider underdetermination",
      "computed (on S108-3-I4); not settled for FC80 as built",
      "worked cases 'Sel-parts': Account ∧ ¬Dec(t) F → T on the 22 with Acc T; worlds.cands: 1,013 / 881 / 232 / 1,670 in ('Sel-parts'; t′ + an idle part the same); pairs newly underdetermined (t′ deviating): 1,141 / 859 / 469 / 2,577 candidates; the pole: t′ faithful on H, Sel F → T, each of the 6 pairs of C1∖H underdetermined 0 → 1. FC80 (suite) does not move: its populations state no construction (S108-3-I3)",
      settle="for FC80 itself: a population with a stated construction built into FC80's generator")
    e("V3.6", "changes with", "L481.s3", "S3", None, "added",
      "L481.s3's second clause ('a transport that would need a part every member of the population is built without is not in it') is false of D15.8 under V3.6: t′ with a part none of 𝒯 has is in 𝒯 (cases §C)", named=False)
    e("V3.6", "moves", "the student's declared copy (FC30.new1 (d))", "–", None, "added",
      "unmoved, as the reply says: Dec(t) at o2 T under V3.6 (the copy's defect is the absent trace and D12.3's inheritance, not the population)", named=False)

    # ---- V3.7 D11.4 without the dependence conjunct -------------------------------------------------------------------------
    e("V3.7", "blocks", "L375.s2", "FROZEN", "'nonconstant dependence on the represented distinction under the declared contrasts' is part of the frozen definition the varied D11.4 must read",
      "computed", "FC75 (a) (did no work) and (a′) (dependence only outside R) as claimed → not as claimed (suite.V3.7; (a″), (b) text only: the reason printed); worlds.routes: 1,436 of 5,724 routes active under V3.7 with constant dependence, smallest n = 2: n1 := c0(i)")
    e("V3.7", "moves", "(P) via ProducedBy (D14.3), (EX) via ProducesVia (D14.6), reason use (D9.11)", "FROZEN", "idle routes become active; no part of (E) moves",
      "computed for ProducedBy and ProducesVia on generated circuits; not settled for UsesReason; (E) computed",
      "worlds.routes: ProducedBy F → T on 685 of 1,460 circuits, ProducesVia on 952 of 2,860 (circuit, occurrence); Acc 0 moves anywhere. The program supplies ProducedBy, ProducesVia and UsesReason by hand in its claims (I90, I47): FC76 (UsesReason) unmoved",
      settle="UsesReason computed over circuits with a represented objection and role maps (D9.11's m, Rec, Chg), which the program does not build")

    # ---- V3.8 D14.7 without CreativeCriticalEpisode ------------------------------------------------------------------------
    e("V3.8", "blocks", "none (L443.s3 constrains only O_ex ⊆ O; L445.s1, L429.s1–s3 are S3)", "FROZEN; S3", "–",
      "computed, in part", "no frozen sentence about (EX) is false under V3.8 (L443.s3 names O_ex only); but see the added edge on L528.s2–s3 (FROZEN)")
    e("V3.8", "constrains", "L443.n1 ('an explanatory aim requires a deployable account')", "S3", "Deploy conjunct kept",
      "computed", "Deploy is kept in s108s3.create_ex's rest; CreateEx under V3.8 never holds with Deploy F (worlds.createx)")
    e("V3.8", "changes with", "L628 and D18.1's DEP", "S4", "FC90: CCE 'left unstated by L628', so no sentence change is forced; DEP's (EX) node loses its Crit edge (FC32.new1 (f))",
      "computed for DEP; the quotation does not match the text now; the owner's part not settled by computation",
      "DEP: (EX) no longer reaches Crit: FC32.new1 (f) as claimed → not as claimed ((EX) ⇝ Crit F under U, K, T, T′; Con, CT, Episode ⇝ Crit F as before); FC84.new1 (a4) look: I192 (d)'s CreateEx [F] → [F, T]. L628: FC90 unmoved (its (EX) list is fixed); the words 'left unstated by L628' are FC90's result about text 103 (its first part); the text now, L628.n2, states 'with CreativeCriticalEpisode(s,Δ,h,e)' among its hypotheses, which under V3.8 becomes a surplus hypothesis (the conditional still holds), so no sentence is made false (rule 14)",
      settle="whether the owner wants (EX) to keep its critical episode (S47 with S41 Q6): the owner's yes or no")
    e("V3.8", "moves", "the class of created explanations; not (E), not Expl, not (Suff)/(Nec)", "–", "(EX) is a defined relation of an episode (L31.s4)",
      "computed", "worlds.createx: CreateEx F → T on 7,086 of 1,929,216 valuations (1,884 chains), T → F on 0; the bridge (a1), no criticism: 0 → 16 of 1,024; FC84.new1 (a4) I192 (d): [F] → [F, T]; Acc, Dec, Account ∧ ¬Dec(t) and the defeat sets: 0 moves (§3, §6.1)")
    e("V3.8", "changes with", "L528.s2, L528.s3 (the creative-episode class; the explanation-creation class)", "FROZEN", None, "added",
      "under 'none' every instance of (EX) has a critical episode connected to (G), so the explanation-creation class (L528.s3) lies inside the creative-episode class (L528.s2); under V3.8 not: the bridge (a1) with no criticism meets (EX) on 16 valuations and CCE on none (worlds.createx: 21 such chains); DEP's 'Classes' still reads CCE", named=False)
