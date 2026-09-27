# S104 Round 2 — search results

*Log S104, review round 2 (the maths round), 27 September 2026, under decision S36 ("maybe exploring the math a bit more might help instead of words. Since words are vague"; "if implementation forces invention, that needs to be recorded"). The text under review is `tests/103 The semantics, standing alone, after round 1.md`, md5 f31ebb1f050783f1a84f6136cec20fcd (checked before every run; not written to). The claims are those of `formal claims.md` (FC01–FC110); the program is the package `model/` in this folder, standard library only. Written by `model/report.py` from one run of `python3 -m model.run --scale 4 --time-cap 45` (326 s of computing).*

**What this is.** For each formal claim, the program built small finite models of the formal core and looked for a counterexample: through every model of a small space where the space is small, otherwise through seeded random draws in ascending order of size, so that the first counterexample found is the smallest found. Existence claims were searched for a witness. Claims about the text's worked cases were computed on the encodings of `formal core.md` §17. Every choice the program made that the formal core leaves open is an invention, recorded in `inventions register.md` as I77–I102 and tagged in the code; every result names the inventions it rests on, the claim's own and the program's. A result that rests on an invention is a result about this formalization, not about the text. Nothing is settled (S28): 'holds on all models tried' reports a search that found nothing within its bounds (I77), and a counterexample is one model, open to being read another way.

**Statuses.** A claim is *COUNTEREXAMPLE FOUND* when some part found one (or a computation on a worked case came out otherwise than the claim says); *HOLDS ON ALL MODELS TRIED* when no part did and at least one part was put to models; *NOT TESTED* when no part could be, with the reason. Parts are: *for all* (searched for a counterexample), *there is* (searched for a witness), *computation* (a worked case computed), *by construction* (true of the program as written, reported, not searched), *look* (a claim's Look, a first reading of where a counterexample might lie, computed; its outcome never makes the claim's status), and *not tested*.

**Counts.** 110 claims: 87 HOLDS ON ALL MODELS TRIED; 12 COUNTEREXAMPLE FOUND; 11 NOT TESTED. Parts: 62 holds on all models tried; 18 witness found; 51 computed: as claimed; 6 counterexample found; 20 not tested; 16 holds by construction; 2 look: not as expected; 3 look: as expected; 6 computed: not as claimed; 1 no witness found.

**Reproducing.** Every result, counterexamples included, is reproduced by one command, given with it: `cd "/home/user/ThreadSmith/Semantics/results/S104 Round 2 - maths" && python3 -m model.run --claim FCnn --scale 4 --time-cap 45`. The whole run: the same command without `--claim`.

## Counterexamples

### FC05 · Kinds are fixed by relations, not by solution values

**The claim.** sig_C(j) is a function of (L_j(a,b))_{(a,b)∈C} alone. If β_*L_j(a,b) = L_j'(a,b) for every (a,b) in C, then j ~_C j', whatever the projections of Sol_D(a,b) on V_j and V_j' are; adding to C a pair at which β_*L_j = L_j' leaves the relation between j and j' as it was.

**What it rests on.** Rests on I93 reading (ii) ('stay equal' under any footprint bijection) with I10's bijection of equal domains; under reading (i) the sentence holds on every model tried. Every invention the counterexample depends on: I10, I77, I78, I93.

**Reproduce.** `cd "/home/user/ThreadSmith/Semantics/results/S104 Round 2 - maths" && python3 -m model.run --claim FC05 --scale 4 --time-cap 45`

**Part: (ii) reading (ii): any bijection** (counterexample found). if j ~_C j' and β_*L_j = L_j' at a new pair x for some footprint bijection β, then j ~_{C∪{x}} j'

Searched: sizes ports=1 dom≤1 comps=1 |B|=1 edits=0 … ports=3 dom≤2 comps=3 |B|=2 edits=2 (108 sizes, 800 draws each); families: G-free (equal domains); seed 104052; 10729 models tried; 4392 of them meeting the claim's hypothesis; first found at size ports=2 dom≤2 comps=2 |B|=1 edits=1.

```
L119: 'an edit under which the two relations stay equal does not separate the components'. Here c1 ~_C c0 (witness (1, 0)), the relations agree at the new pair ('e1', 'b0') under the bijection (0, 1), and yet c1 and c0 are not of one kind on C ∪ {('e1', 'b0')}: the pair separates them because they agree there only under a bijection that does not witness ~_C.
organization D
  ports: p0 ∈ {0,1}; p1 ∈ {0,1}
  components: c0 on (p0,p1); c1 on (p0,p1)
  boundaries B = {b0}; edits A = {1,e1}
  composition (other than with 1): e1·e1=undef
  L_c1(1,b0) = {(0,0) (0,1)}
  L_c1(e1,b0) = {(0,1) (1,1)}
  L_c0(1,b0) = {(0,0) (1,0)}
  L_c0(e1,b0) = {(0,1) (1,1)}
C = {(1,b0)}
```

### FC18 · Argument 1's Consequence: a same-kind condition adds nothing; no third case

**The claim.** SameKind_C(ℰ) := for every k in Γ, the signature of k read through t and sig_C(λ(k),θ_k) coincide under a footprint bijection (I10). Claim: F1_C(ℰ) ⇒ SameKind_C(ℰ), so Acc(ℰ) ⟺ Acc(ℰ) ∧ SameKind_C(ℰ) for every ℰ and C.

**What it rests on.** Rests on I94 (the counterpart read untranslated, on D's ports and domains) with I10 (bijections between equal domains) and I14 (value maps). Under D4.4's reading FC18 holds on every model tried. Every invention the counterexample depends on: I10, I13, I14, I77, I78, I81, I94.

**Reproduce.** `cd "/home/user/ThreadSmith/Semantics/results/S104 Round 2 - maths" && python3 -m model.run --claim FC18 --scale 4 --time-cap 45`

**Part: untranslated reading (I94)** (counterexample found). F1_C ⇒ SameKind_C, the counterpart read on its own D ports with D's domains

Searched: sizes ports=1 dom≤1 comps=1 |B|=1 edits=0 … ports=3 dom≤2 comps=3 |B|=2 edits=2 (108 sizes, 240 draws each); families: G-surg, G-free; seed 104182; 972 models tried; 660 of them meeting the claim's hypothesis; first found at size ports=1 dom≤2 comps=1 |B|=1 edits=0.

```
Under the untranslated reading of 'read on C directly … up to the port translation' (I94), (F1) holds and commitment k0 is of no kind with its counterpart: its port domains are the images of value maps, so no footprint bijection between equal domains exists (I10). Argument 1's Consequence then needs I10's value-bijection alternative.
question p: target D, b0 = b0, query Q_w (reads the designated port) designating p0, C = {(1,b0)}
candidate ℰ for p: Γ = {k0}, δ_E = p0
  π: p0 := κ{0: 1, 1: 1}(p0)
  τ: 1↦1; σ: b0↦b0
  λ(k0) = ({c0}, p0:=κ{0: 1, 1: 1}(p0))
organization E_ℰ
  ports: p0 ∈ {1}
  components: k0 on (p0)
  boundaries B = {b0}; edits A = {1}
  L_k0(1,b0) = {(1)}
```

### FC20 · When (F2) at a pair gives (A) at that pair (violation in either extent)

**The claim.** If Q reads a port w of the target, δ_E designates a port w' of E, and π(z)_{w'} = κ(z_w) for every z (π acts on the designated port as a value map κ), then the valuation equation of (F2) at (a,b) gives Ans_E(τ(a),σ(b)) = κ(Ans_p(a,b)); with κ the identity this is (A) at (a,b). Without that condition on π, (F2) at a pair does not give (A) there. Violation and Violation⁺ (I50) coincide exactly where it does.

**What it rests on.** Rests on I14 and I81 (value maps that need not be injective) and I21 (⊥ for several values). With κ the identity the claim holds on every model tried. Every invention the counterexample depends on: I14, I16, I20, I21, I49, I50, I77, I78, I81.

**Reproduce.** `cd "/home/user/ThreadSmith/Semantics/results/S104 Round 2 - maths" && python3 -m model.run --claim FC20 --scale 4 --time-cap 45`

**Part: any value map κ** (counterexample found). F2eq at (a,b) ∧ π acts on the designated port as κ ⇒ Ans_E(τa,σb) = κ(Ans_p(a,b)) (κ(⊥) = ⊥)

Searched: sizes ports=1 dom≤1 comps=1 |B|=1 edits=0 … ports=3 dom≤2 comps=3 |B|=2 edits=2 (108 sizes, 600 draws each); families: G-surg, G-free; seed 104201; 2404 models tried; 1849 of them meeting the claim's hypothesis; first found at size ports=1 dom≤2 comps=1 |B|=1 edits=0.

```
At (1,b0) the valuation equation of (F2) holds and π acts on the designated port as the value map κ{0: 0, 1: 0}(p0), yet Ans_E = 0 while κ(Ans_p) = ⊥: the target's port takes the values [0, 1], so Ans_p = ⊥, and κ sends them to one value, so E's answer is determined. FC20's conclusion needs κ injective on the values Sol_D takes.
question p: target D, b0 = b0, query Q_w (reads the designated port) designating p0, C = {(1,b0)}
organization D
  ports: p0 ∈ {0,1}
  components: c0 on (p0)
  boundaries B = {b0}; edits A = {1}
  L_c0(1,b0) = full
candidate ℰ for p: Γ = {k0}, δ_E = p0
  π: p0 := κ{0: 0, 1: 0}(p0)
  τ: 1↦1; σ: b0↦b0
  λ(k0) = ({c0}, p0:=κ{0: 0, 1: 0}(p0))
organization E_ℰ
  ports: p0 ∈ {0}
  components: k0 on (p0)
  boundaries B = {b0}; edits A = {1}
  L_k0(1,b0) = {(0)}
```

### FC23 · 'p because p' fails non-circular dependence through NC1 only

**The claim.** Let E_lk have Γ = {k}, L_k(τ(a),σ(b)) the answer slot for Ans_p(a,b) (I24), and no other component constraining the answer ports. (a) NC1 fails for E_lk. (b) If Ans_p is not constant on C, NC2 holds for E_lk with G = {k}: after deleting k the answer is ⊥ at both points, so an answer E_lk determined is no longer determined. So E_lk fails non-circular dependence through NC1 only; under I24's alternative (a), NC2 alone, E_lk meets non-circular dependence.

**What it rests on.** Rests on I24 (the lookup's slot) and on the claim's own wording, which allows background components that make Sol_E empty; with a satisfiable background (b) holds on every model tried. Every invention the counterexample depends on: I21, I22, I24, I25, I77, I78, I79, I81, I82, I83.

**Reproduce.** `cd "/home/user/ThreadSmith/Semantics/results/S104 Round 2 - maths" && python3 -m model.run --claim FC23 --scale 4 --time-cap 45`

**Part: (b) as stated** (counterexample found). Ans_p not constant on C ⇒ NC2(E_lk) with G = {k}

Searched: sizes ports=1 dom≤1 comps=1 |B|=1 edits=0 … ports=3 dom≤2 comps=3 |B|=2 edits=2 (108 sizes, 320 draws each); families: G-surg, G-free; seed 104232; 6308 models tried; 105 of them meeting the claim's hypothesis; first found at size ports=2 dom≤2 comps=1 |B|=1 edits=1.

```
Ans_p is not constant on C (values [0, 1]), and the lookup E_lk fails NC2: its background component makes Sol_E empty at {(1,b0), (e1,b0)}, so E_lk's answer is ⊥ there and no contrast of the kind NC2 names appears. FC23 (b) needs a lookup whose other components are satisfiable.
question p: target D, b0 = b0, query Q_w (reads the designated port) designating p0, C = {(1,b0), (e1,b0)}
organization D
  ports: p0 ∈ {0,1}; p1 ∈ {0,1}
  components: c0 on (p0)
  boundaries B = {b0}; edits A = {1,e1}
  composition (other than with 1): e1·e1=undef
  L_c0(1,b0) = {(0)}
  L_c0(e1,b0) = {(1)}
candidate ℰ_lk for p: Γ = {k}, δ_E = p0
  π: p0 := id(p0); p1 := id(p1)
  τ: 1↦1, e1↦e1; σ: b0↦b0
  λ(k) = ({c0}, p0:=id(p0))
organization E_lk
  ports: p0 ∈ {0,1}; p1 ∈ {0,1}
  components: k on (p0); bg on (p1)
  boundaries B = {b0}; edits A = {1,e1}
  composition (other than with 1): e1·e1=undef
  L_k(1,b0) = {(0)}
  L_k(e1,b0) = {(1)}
  L_bg(1,b0) = {}
  L_bg(e1,b0) = {}
```

### FC25 · Tables: a fixed table fails (F1) where the projection moves; an encoding table meets it

**The claim.** (a) E_tab (I32): F1 at (a,b) ⟺ the projection of Sol_D(a,b) on the table's ports equals that of Sol_D(1,b0). So E_tab fails (F1) under C exactly when C holds a pair at which that projection moves; a setting edit that leaves it unchanged (a port set to its baseline value, or a port the table's ports do not depend on) does not make it fail. (b) E_enc, with L_k(τ(a),σ(b)) := that projection at (a,b), meets (F1) on every C.

**What it rests on.** Rests on I14 and D1.4 (a subnetwork's ports are its components' footprints) with I32 (λ(k) = the whole target). Where every port of D lies in some footprint, (a) and (b) hold on every model tried. Every invention the counterexample depends on: I03, I04, I14, I32, I77, I78.

**Reproduce.** `cd "/home/user/ThreadSmith/Semantics/results/S104 Round 2 - maths" && python3 -m model.run --claim FC25 --scale 4 --time-cap 45`

**Part: (b) with a port of D in no footprint** (counterexample found). E_enc meets (F1) on every C, D having a port in no footprint

Searched: sizes ports=1 dom≤1 comps=1 |B|=1 edits=0 … ports=3 dom≤2 comps=3 |B|=2 edits=2 (108 sizes, 160 draws each); families: G-surg; seed 104254; 1 models tried; first found at size ports=2 dom≤1 comps=1 |B|=1 edits=0.

```
E_enc (I32: λ(k) = the whole target, projected on k's ports) fails (F1): its ports include ['p1'], which lies in no footprint of D, so it is not a port of the subnetwork J_D (D1.4 and I14 build V_N from footprints) and no port translation can reach it; the value of such a port is free in Sol_D and the table records it, but proj^λ cannot. FC25 (b) holds only where every port of D lies in some footprint.
question p: target D, b0 = b0, query Q_w (reads the designated port) designating p1, C = {(1,b0)}
organization D
  ports: p0 ∈ {0}; p1 ∈ {0}
  components: h_p0 on (p0)
  boundaries B = {b0}; edits A = {1}
  L_h_p0(1,b0) = {(0)}
candidate E_enc for p: Γ = {tab}, δ_E = p1
  π: p1 := id(p1)
  τ: 1↦1; σ: b0↦b0
  λ(tab) = ({h_p0}, p1:=id(p1))
organization E_enc
  ports: p1 ∈ {0}
  components: tab on (p1)
  boundaries B = {b0}; edits A = {1}
  L_tab(1,b0) = {(0)}
```

### FC63 · Odd-order skew-symmetric matrices

**The claim.** (a) For every odd n and every n×n M over ℝ (or GF(p), p odd) with Mᵀ = −M: det M = 0. (b) det I3 = 1; det [[0,1],[−1,0]] = 1. (c) With I66, the Leibniz candidate meets (F1), (F2), (A), NC2 and non-vacuity (the scope statement naming the edits to field arithmetic and to the determinant–invertibility link).

**What it rests on.** Rests on I66 and I99 (which relation the sum component carries) and I81 (derived ports, without which the candidate cannot be written under I14). With the sum restricted to realizable term tuples the candidate meets (E). Every invention the counterexample depends on: I03, I27, I66, I81, I82, I99.

**Reproduce.** `cd "/home/user/ThreadSmith/Semantics/results/S104 Round 2 - maths" && python3 -m model.run --claim FC63 --scale 4 --time-cap 45`

**Part: (c-i) the Leibniz candidate, sum over every tuple of term values** (computed: not as claimed). the Leibniz candidate meets (F1), (F2), (A), NC2 and non-vacuity

```
Target: n ∈ {1,2,3}, entries in GF(3), M one port, components order, skew, odd, det, inv; edits remove skew (rs), remove oddness (ro), both (rb); the edits to field arithmetic and to det–invertibility are not edits of this encoding, so the scope clause is met trivially (I99). Answers {'1': False, 'rs': True, 'ro': True, 'rb': True}. The Leibniz candidate needs ports for the terms, which D lacks: under I14 (each E port translated to one D port) it cannot be written; with derived ports (a term port read as a function of M, I81) it can. Variant 'sum over every tuple of term values': F1 False (failing: ['sum']); Account False {'F1': False, 'F2eq': True, 'A': True}. Variant 'sum restricted to realizable term tuples': F1 True (failing: none); Account True {'translates C': True, 'F1': True, 'F2eq': True, 'Hom': True, 'F2': True, 'A': True, 'NC1': True, 'NC2': True, 'NonVacuous': True}, NC2 witness (('rb', 'b0'), ['order']).
```

*the sum component, relating every tuple of term values to their sum, differs from its counterpart's projection, which holds only the term tuples some matrix gives: (F1) fails for it*

### FC77 · Without a physical witness, selection is met by every transport

**The claim.** Read with no physical witness: for every t, Sel(t; {t}, id, ∅) holds (fidelity on ∅ is vacuous, and an empty history holds nothing that represents). Then (R) reduces to 'some faithful transport exists'. With I52, Sel needs a physical selection history; test which of I52's requirements block the trivial witness.

**What it rests on.** Rests on I18 (Hom is a condition on τ as a whole, not at a pair) and I52 (Sel with 𝒯 = {t}, μ the identity). The trivial witness exists exactly for the transports whose τ is a homomorphism. Every invention the counterexample depends on: I18, I48, I52, I77, I78, I81, I90.

**Reproduce.** `cd "/home/user/ThreadSmith/Semantics/results/S104 Round 2 - maths" && python3 -m model.run --claim FC77 --scale 4 --time-cap 45`

**Part: with H = ∅ and an empty selection history** (counterexample found). every transport t has Sel(t; {t}, id, ∅) when Θ admits t (fidelity on ∅ vacuous)

Searched: sizes ports=1 dom≤1 comps=1 |B|=1 edits=0 … ports=3 dom≤2 comps=3 |B|=2 edits=2 (108 sizes, 80 draws each); families: G-surg, G-free; seed 104771; 494 models tried; first found at size ports=1 dom≤1 comps=1 |B|=1 edits=2.

```
Sel(t; {t}, id, ∅) fails for this transport although H = ∅ and the selection history is empty: fidelity on ∅ is not vacuous, because (F2)'s homomorphism clause is a condition on τ as a whole (I18), and here Hom(τ) fails. Every transport whose τ is a homomorphism is 'selected' by these parameters; one whose τ is not, is not.
question p: target D, b0 = b0, query Q_w (reads the designated port) designating p0, C = {(1,b0), ([alt:h_p0],b0), ([p0=0,alt:h_p0],b0), ([p0=0],b0)}
organization D
  ports: p0 ∈ {0}
  components: h_p0 on (p0)
  boundaries B = {b0}; edits A = {1,[p0=0],[alt:h_p0],[p0=0,alt:h_p0]}
  composition (other than with 1): [p0=0]·[p0=0]=[p0=0], [p0=0]·[alt:h_p0]=[p0=0,alt:h_p0], [p0=0]·[p0=0,alt:h_p0]=[p0=0,alt:h_p0], [alt:h_p0]·[p0=0]=[p0=0,alt:h_p0], [alt:h_p0]·[alt:h_p0]=[alt:h_p0], [alt:h_p0]·[p0=0,alt:h_p0]=[p0=0,alt:h_p0], [p0=0,alt:h_p0]·[p0=0]=[p0=0,alt:h_p0], [p0=0,alt:h_p0]·[alt:h_p0]=[p0=0,alt:h_p0], [p0=0,alt:h_p0]·[p0=0,alt:h_p0]=[p0=0,alt:h_p0]
  L_h_p0(1,b0) = {(0)}
  L_h_p0([p0=0],b0) = {(0)}
  L_h_p0([alt:h_p0],b0) = {}
  L_h_p0([p0=0,alt:h_p0],b0) = {(0)}
candidate ℰ for p: Γ = {c0}, δ_E = p0
  π: p0 := id(p0)
  τ: 1↦1, [p0=0]↦1, [alt:h_p0]↦[alt:h_p0], [p0=0,alt:h_p0]↦[p0=0]; σ: b0↦b0
  λ(c0) = ({h_p0}, p0:=id(p0))
organization E_r
  ports: p0 ∈ {0}
  components: c0 on (p0)
  boundaries B = {b0}; edits A = {1,[p0=0],[alt:h_p0],[p0=0,alt:h_p0]}
  composition (other than with 1): [p0=0]·[p0=0]=[p0=0], [p0=0]·[alt:h_p0]=[p0=0,alt:h_p0], [p0=0]·[p0=0,alt:h_p0]=[p0=0,alt:h_p0], [alt:h_p0]·[p0=0]=[p0=0,alt:h_p0], [alt:h_p0]·[alt:h_p0]=[alt:h_p0], [alt:h_p0]·[p0=0,alt:h_p0]=[p0=0,alt:h_p0], [p0=0,alt:h_p0]·[p0=0]=[p0=0,alt:h_p0], [p0=0,alt:h_p0]·[alt:h_p0]=[p0=0,alt:h_p0], [p0=0,alt:h_p0]·[p0=0,alt:h_p0]=[p0=0,alt:h_p0]
  L_c0(1,b0) = {(0)}
  L_c0([alt:h_p0],b0) = {(0)}
  L_c0([p0=0],b0) = {(0)}
```

### FC78 · Exactly one of three provenances

**The claim.** Under I53, Sel(t) ∧ Con(t) is impossible and Dec(t) := ¬Sel ∧ ¬Con, so exactly one holds. Under I53's alternative there are histories with Sel on one part and Con on another. Per part (I54), exactly one holds of each part.

**What it rests on.** Rests on D12.1's reading of L195 (I52: no occurrence represents t, H or the survival condition), I53 (one history), I56 (Prepares a primitive) and I90 (Θ by hand). L201's stronger sentence would exclude it; the formal core does not use L201. Every invention the counterexample depends on: I52, I53, I54, I56, I90, I92.

**Reproduce.** `cd "/home/user/ThreadSmith/Semantics/results/S104 Round 2 - maths" && python3 -m model.run --claim FC78 --scale 4 --time-cap 45`

**Part: exactly one provenance under I53** (computed: not as claimed). Sel(t) ∧ Con(t) is impossible on one history

```
One history h: o1 represents the organization t carries to (its codomain), a construction trace in h prepares t (Prepares, I56), no occurrence represents t, H or the survival condition, and t (the pole's forward transport) is faithful on H = {(1,b1_45)}, whose pair occurs. Sel(t; {t}, id, H): True. Con(t; h, e): True. D12.1 follows L195 ('No member of the history represents t, H, or the survival condition'), which does not forbid a represented codomain; L197 lets Con hold through 'the organization it carries to'. L201's stronger sentence ('a selected transport has no represented target … in its history') would exclude it, and the formal core does not use it. Θ is supplied by hand here (I90).
candidate ℰ_fwd for p: Γ = {c_H,c_T,c_L}, δ_E = L
  π: H := id(H); T := id(T); L := id(L)
  τ: 1↦1, set(H=1)↦set(H=1), set(H=2)↦set(H=2), set(L=1)↦set(L=1), set(L=2)↦set(L=2), set(T=45)↦set(T=45), set(H=1,L=1)↦set(H=1,L=1), set(H=1,L=2)↦set(H=1,L=2), set(H=1,T=45)↦set(H=1,T=45), set(H=2,L=1)↦set(H=2,L=1), set(H=2,L=2)↦set(H=2,L=2), set(H=2,T=45)↦set(H=2,T=45), set(L=1,T=45)↦set(L=1,T=45), set(L=2,T=45)↦set(L=2,T=45), set(H=1,L=1,T=45)↦set(H=1,L=1,T=45), set(H=1,L=2,T=45)↦set(H=1,L=2,T=45), set(H=2,L=1,T=45)↦set(H=2,L=1,T=45), set(H=2,L=2,T=45)↦set(H=2,L=2,T=45); σ: b1_45↦b1_45
  λ(c_H) = ({c_H}, H:=id(H))
  λ(c_T) = ({c_T}, T:=id(T))
  λ(c_L) = ({c_L}, H:=id(H); T:=id(T); L:=id(L))
organization D_pole
  ports: H ∈ {1,2}; T ∈ {45}; L ∈ {1,2}
  components: c_H on (H); c_T on (T); c_L on (H,T,L)
  boundaries B = {b1_45}; edits A = {1,set(H=1),set(H=2),set(L=1),set(L=2),set(T=45),set(H=1,L=1),set(H=1,L=2),set(H=1,T=45),set(H=2,L=1),set(H=2,L=2),set(H=2,T=45),set(L=1,T=45),set(L=2,T=45),set(H=1,L=1,T=45),set(H=1,L=2,T=45),set(H=2,L=1,T=45),set(H=2,L=2,T=45)}
  composition (other than with 1): set(H=1)·set(H=1)=set(H=1), set(H=1)·set(H=2)=set(H=1), set(H=1)·set(L=1)=set(H=1,L=1), set(H=1)·set(L=2)=set(H=1,L=2), set(H=1)·set(T=45)=set(H=1,T=45), set(H=1)·set(H=1,L=1)=set(H=1,L=1), set(H=1)·set(H=1,L=2)=set(H=1,L=2), set(H=1)·set(H=1,T=45)=set(H=1,T=45), set(H=1)·set(H=2,L=1)=set(H=1,L=1), set(H=1)·set(H=2,L=2)=set(H=1,L=2), set(H=1)·set(H=2,T=45)=set(H=1,T=45), set(H=1)·set(L=1,T=45)=set(H=1,L=1,T=45), set(H=1)·set(L=2,T=45)=set(H=1,L=2,T=45), set(H=1)·set(H=1,L=1,T=45)=set(H=1,L=1,T=45), set(H=1)·set(H=1,L=2,T=45)=set(H=1,L=2,T=45), set(H=1)·set(H=2,L=1,T=45)=set(H=1,L=1,T=45), set(H=1)·set(H=2,L=2,T=45)=set(H=1,L=2,T=45), set(H=2)·set(H=1)=set(H=2), set(H=2)·set(H=2)=set(H=2), set(H=2)·set(L=1)=set(H=2,L=1), set(H=2)·set(L=2)=set(H=2,L=2), set(H=2)·set(T=45)=set(H=2,T=45), set(H=2)·set(H=1,L=1)=set(H=2,L=1), set(H=2)·set(H=1,L=2)=set(H=2,L=2), set(H=2)·set(H=1,T=45)=set(H=2,T=45), set(H=2)·set(H=2,L=1)=set(H=2,L=1), set(H=2)·set(H=2,L=2)=set(H=2,L=2), set(H=2)·set(H=2,T=45)=set(H=2,T=45), set(H=2)·set(L=1,T=45)=set(H=2,L=1,T=45), set(H=2)·set(L=2,T=45)=set(H=2,L=2,T=45), set(H=2)·set(H=1,L=1,T=45)=set(H=2,L=1,T=45), set(H=2)·set(H=1,L=2,T=45)=set(H=2,L=2,T=45), set(H=2)·set(H=2,L=1,T=45)=set(H=2,L=1,T=45), set(H=2)·set(H=2,L=2,T=45)=set(H=2,L=2,T=45), set(L=1)·set(H=1)=set(H=1,L=1), set(L=1)·set(H=2)=set(H=2,L=1), set(L=1)·set(L=1)=set(L=1), set(L=1)·set(L=2)=set(L=1), set(L=1)·set(T=45)=set(L=1,T=45), set(L=1)·set(H=1,L=1)=set(H=1,L=1), set(L=1)·set(H=1,L=2)=set(H=1,L=1), set(L=1)·set(H=1,T=45)=set(H=1,L=1,T=45), set(L=1)·set(H=2,L=1)=set(H=2,L=1), set(L=1)·set(H=2,L=2)=set(H=2,L=1), set(L=1)·set(H=2,T=45)=set(H=2,L=1,T=45), set(L=1)·set(L=1,T=45)=set(L=1,T=45), set(L=1)·set(L=2,T=45)=set(L=1,T=45), set(L=1)·set(H=1,L=1,T=45)=set(H=1,L=1,T=45), set(L=1)·set(H=1,L=2,T=45)=set(H=1,L=1,T=45), set(L=1)·set(H=2,L=1,T=45)=set(H=2,L=1,T=45), set(L=1)·set(H=2,L=2,T=45)=set(H=2,L=1,T=45), set(L=2)·set(H=1)=set(H=1,L=2), set(L=2)·set(H=2)=set(H=2,L=2), set(L=2)·set(L=1)=set(L=2), set(L=2)·set(L=2)=set(L=2), set(L=2)·set(T=45)=set(L=2,T=45), set(L=2)·set(H=1,L=1)=set(H=1,L=2), set(L=2)·set(H=1,L=2)=set(H=1,L=2), set(L=2)·set(H=1,T=45)=set(H=1,L=2,T=45), set(L=2)·set(H=2,L=1)=set(H=2,L=2), set(L=2)·set(H=2,L=2)=set(H=2,L=2), set(L=2)·set(H=2,T=45)=set(H=2,L=2,T=45), set(L=2)·set(L=1,T=45)=set(L=2,T=45), set(L=2)·set(L=2,T=45)=set(L=2,T=45), set(L=2)·set(H=1,L=1,T=45)=set(H=1,L=2,T=45), set(L=2)·set(H=1,L=2,T=45)=set(H=1,L=2,T=45), set(L=2)·set(H=2,L=1,T=45)=set(H=2,L=2,T=45), set(L=2)·set(H=2,L=2,T=45)=set(H=2,L=2,T=45), set(T=45)·set(H=1)=set(H=1,T=45), set(T=45)·set(H=2)=set(H=2,T=45), set(T=45)·set(L=1)=set(L=1,T=45), set(T=45)·set(L=2)=set(L=2,T=45), set(T=45)·set(T=45)=set(T=45), set(T=45)·set(H=1,L=1)=set(H=1,L=1,T=45), set(T=45)·set(H=1,L=2)=set(H=1,L=2,T=45), set(T=45)·set(H=1,T=45)=set(H=1,T=45), set(T=45)·set(H=2,L=1)=set(H=2,L=1,T=45), set(T=45)·set(H=2,L=2)=set(H=2,L=2,T=45), set(T=45)·set(H=2,T=45)=set(H=2,T=45), set(T=45)·set(L=1,T=45)=set(L=1,T=45), set(T=45)·set(L=2,T=45)=set(L=2,T=45), set(T=45)·set(H=1,L=1,T=45)=set(H=1,L=1,T=45), set(T=45)·set(H=1,L=2,T=45)=set(H=1,L=2,T=45), set(T=45)·set(H=2,L=1,T=45)=set(H=2,L=1,T=45), set(T=45)·set(H=2,L=2,T=45)=set(H=2,L=2,T=45), set(H=1,L=1)·set(H=1)=set(H=1,L=1), set(H=1,L=1)·set(H=2)=set(H=1,L=1), set(H=1,L=1)·set(L=1)=set(H=1,L=1), set(H=1,L=1)·set(L=2)=set(H=1,L=1), set(H=1,L=1)·set(T=45)=set(H=1,L=1,T=45), set(H=1,L=1)·set(H=1,L=1)=set(H=1,L=1), set(H=1,L=1)·set(H=1,L=2)=set(H=1,L=1), set(H=1,L=1)·set(H=1,T=45)=set(H=1,L=1,T=45), set(H=1,L=1)·set(H=2,L=1)=set(H=1,L=1), set(H=1,L=1)·set(H=2,L=2)=set(H=1,L=1), set(H=1,L=1)·set(H=2,T=45)=set(H=1,L=1,T=45), set(H=1,L=1)·set(L=1,T=45)=set(H=1,L=1,T=45), set(H=1,L=1)·set(L=2,T=45)=set(H=1,L=1,T=45), set(H=1,L=1)·set(H=1,L=1,T=45)=set(H=1,L=1,T=45), set(H=1,L=1)·set(H=1,L=2,T=45)=set(H=1,L=1,T=45), set(H=1,L=1)·set(H=2,L=1,T=45)=set(H=1,L=1,T=45), set(H=1,L=1)·set(H=2,L=2,T=45)=set(H=1,L=1,T=45), set(H=1,L=2)·set(H=1)=set(H=1,L=2), set(H=1,L=2)·set(H=2)=set(H=1,L=2), set(H=1,L=2)·set(L=1)=set(H=1,L=2), set(H=1,L=2)·set(L=2)=set(H=1,L=2), set(H=1,L=2)·set(T=45)=set(H=1,L=2,T=45), set(H=1,L=2)·set(H=1,L=1)=set(H=1,L=2), set(H=1,L=2)·set(H=1,L=2)=set(H=1,L=2), set(H=1,L=2)·set(H=1,T=45)=set(H=1,L=2,T=45), set(H=1,L=2)·set(H=2,L=1)=set(H=1,L=2), set(H=1,L=2)·set(H=2,L=2)=set(H=1,L=2), set(H=1,L=2)·set(H=2,T=45)=set(H=1,L=2,T=45), set(H=1,L=2)·set(L=1,T=45)=set(H=1,L=2,T=45), set(H=1,L=2)·set(L=2,T=45)=set(H=1,L=2,T=45), set(H=1,L=2)·set(H=1,L=1,T=45)=set(H=1,L=2,T=45), set(H=1,L=2)·set(H=1,L=2,T=45)=set(H=1,L=2,T=45), set(H=1,L=2)·set(H=2,L=1,T=45)=set(H=1,L=2,T=45), set(H=1,L=2)·set(H=2,L=2,T=45)=set(H=1,L=2,T=45), set(H=1,T=45)·set(H=1)=set(H=1,T=45), set(H=1,T=45)·set(H=2)=set(H=1,T=45), set(H=1,T=45)·set(L=1)=set(H=1,L=1,T=45), set(H=1,T=45)·set(L=2)=set(H=1,L=2,T=45), set(H=1,T=45)·set(T=45)=set(H=1,T=45), set(H=1,T=45)·set(H=1,L=1)=set(H=1,L=1,T=45), set(H=1,T=45)·set(H=1,L=2)=set(H=1,L=2,T=45), set(H=1,T=45)·set(H=1,T=45)=set(H=1,T=45), set(H=1,T=45)·set(H=2,L=1)=set(H=1,L=1,T=45), set(H=1,T=45)·set(H=2,L=2)=set(H=1,L=2,T=45), set(H=1,T=45)·set(H=2,T=45)=set(H=1,T=45), set(H=1,T=45)·set(L=1,T=45)=set(H=1,L=1,T=45), set(H=1,T=45)·set(L=2,T=45)=set(H=1,L=2,T=45), set(H=1,T=45)·set(H=1,L=1,T=45)=set(H=1,L=1,T=45), set(H=1,T=45)·set(H=1,L=2,T=45)=set(H=1,L=2,T=45), set(H=1,T=45)·set(H=2,L=1,T=45)=set(H=1,L=1,T=45), set(H=1,T=45)·set(H=2,L=2,T=45)=set(H=1,L=2,T=45), set(H=2,L=1)·set(H=1)=set(H=2,L=1), set(H=2,L=1)·set(H=2)=set(H=2,L=1), set(H=2,L=1)·set(L=1)=set(H=2,L=1), set(H=2,L=1)·set(L=2)=set(H=2,L=1), set(H=2,L=1)·set(T=45)=set(H=2,L=1,T=45), set(H=2,L=1)·set(H=1,L=1)=set(H=2,L=1), set(H=2,L=1)·set(H=1,L=2)=set(H=2,L=1), set(H=2,L=1)·set(H=1,T=45)=set(H=2,L=1,T=45), set(H=2,L=1)·set(H=2,L=1)=set(H=2,L=1), set(H=2,L=1)·set(H=2,L=2)=set(H=2,L=1), set(H=2,L=1)·set(H=2,T=45)=set(H=2,L=1,T=45), set(H=2,L=1)·set(L=1,T=45)=set(H=2,L=1,T=45), set(H=2,L=1)·set(L=2,T=45)=set(H=2,L=1,T=45), set(H=2,L=1)·set(H=1,L=1,T=45)=set(H=2,L=1,T=45), set(H=2,L=1)·set(H=1,L=2,T=45)=set(H=2,L=1,T=45), set(H=2,L=1)·set(H=2,L=1,T=45)=set(H=2,L=1,T=45), set(H=2,L=1)·set(H=2,L=2,T=45)=set(H=2,L=1,T=45), set(H=2,L=2)·set(H=1)=set(H=2,L=2), set(H=2,L=2)·set(H=2)=set(H=2,L=2), set(H=2,L=2)·set(L=1)=set(H=2,L=2), set(H=2,L=2)·set(L=2)=set(H=2,L=2), set(H=2,L=2)·set(T=45)=set(H=2,L=2,T=45), set(H=2,L=2)·set(H=1,L=1)=set(H=2,L=2), set(H=2,L=2)·set(H=1,L=2)=set(H=2,L=2), set(H=2,L=2)·set(H=1,T=45)=set(H=2,L=2,T=45), set(H=2,L=2)·set(H=2,L=1)=set(H=2,L=2), set(H=2,L=2)·set(H=2,L=2)=set(H=2,L=2), set(H=2,L=2)·set(H=2,T=45)=set(H=2,L=2,T=45), set(H=2,L=2)·set(L=1,T=45)=set(H=2,L=2,T=45), set(H=2,L=2)·set(L=2,T=45)=set(H=2,L=2,T=45), set(H=2,L=2)·set(H=1,L=1,T=45)=set(H=2,L=2,T=45), set(H=2,L=2)·set(H=1,L=2,T=45)=set(H=2,L=2,T=45), set(H=2,L=2)·set(H=2,L=1,T=45)=set(H=2,L=2,T=45), set(H=2,L=2)·set(H=2,L=2,T=45)=set(H=2,L=2,T=45), set(H=2,T=45)·set(H=1)=set(H=2,T=45), set(H=2,T=45)·set(H=2)=set(H=2,T=45), set(H=2,T=45)·set(L=1)=set(H=2,L=1,T=45), set(H=2,T=45)·set(L=2)=set(H=2,L=2,T=45), set(H=2,T=45)·set(T=45)=set(H=2,T=45), set(H=2,T=45)·set(H=1,L=1)=set(H=2,L=1,T=45), set(H=2,T=45)·set(H=1,L=2)=set(H=2,L=2,T=45), set(H=2,T=45)·set(H=1,T=45)=set(H=2,T=45), set(H=2,T=45)·set(H=2,L=1)=set(H=2,L=1,T=45), set(H=2,T=45)·set(H=2,L=2)=set(H=2,L=2,T=45), set(H=2,T=45)·set(H=2,T=45)=set(H=2,T=45), set(H=2,T=45)·set(L=1,T=45)=set(H=2,L=1,T=45), set(H=2,T=45)·set(L=2,T=45)=set(H=2,L=2,T=45), set(H=2,T=45)·set(H=1,L=1,T=45)=set(H=2,L=1,T=45), set(H=2,T=45)·set(H=1,L=2,T=45)=set(H=2,L=2,T=45), set(H=2,T=45)·set(H=2,L=1,T=45)=set(H=2,L=1,T=45), set(H=2,T=45)·set(H=2,L=2,T=45)=set(H=2,L=2,T=45), set(L=1,T=45)·set(H=1)=set(H=1,L=1,T=45), set(L=1,T=45)·set(H=2)=set(H=2,L=1,T=45), set(L=1,T=45)·set(L=1)=set(L=1,T=45), set(L=1,T=45)·set(L=2)=set(L=1,T=45), set(L=1,T=45)·set(T=45)=set(L=1,T=45), set(L=1,T=45)·set(H=1,L=1)=set(H=1,L=1,T=45), set(L=1,T=45)·set(H=1,L=2)=set(H=1,L=1,T=45), set(L=1,T=45)·set(H=1,T=45)=set(H=1,L=1,T=45), set(L=1,T=45)·set(H=2,L=1)=set(H=2,L=1,T=45), set(L=1,T=45)·set(H=2,L=2)=set(H=2,L=1,T=45), set(L=1,T=45)·set(H=2,T=45)=set(H=2,L=1,T=45), set(L=1,T=45)·set(L=1,T=45)=set(L=1,T=45), set(L=1,T=45)·set(L=2,T=45)=set(L=1,T=45), set(L=1,T=45)·set(H=1,L=1,T=45)=set(H=1,L=1,T=45), set(L=1,T=45)·set(H=1,L=2,T=45)=set(H=1,L=1,T=45), set(L=1,T=45)·set(H=2,L=1,T=45)=set(H=2,L=1,T=45), set(L=1,T=45)·set(H=2,L=2,T=45)=set(H=2,L=1,T=45), set(L=2,T=45)·set(H=1)=set(H=1,L=2,T=45), set(L=2,T=45)·set(H=2)=set(H=2,L=2,T=45), set(L=2,T=45)·set(L=1)=set(L=2,T=45), set(L=2,T=45)·set(L=2)=set(L=2,T=45), set(L=2,T=45)·set(T=45)=set(L=2,T=45), set(L=2,T=45)·set(H=1,L=1)=set(H=1,L=2,T=45), set(L=2,T=45)·set(H=1,L=2)=set(H=1,L=2,T=45), set(L=2,T=45)·set(H=1,T=45)=set(H=1,L=2,T=45), set(L=2,T=45)·set(H=2,L=1)=set(H=2,L=2,T=45), set(L=2,T=45)·set(H=2,L=2)=set(H=2,L=2,T=45), set(L=2,T=45)·set(H=2,T=45)=set(H=2,L=2,T=45), set(L=2,T=45)·set(L=1,T=45)=set(L=2,T=45), set(L=2,T=45)·set(L=2,T=45)=set(L=2,T=45), set(L=2,T=45)·set(H=1,L=1,T=45)=set(H=1,L=2,T=45), set(L=2,T=45)·set(H=1,L=2,T=45)=set(H=1,L=2,T=45), set(L=2,T=45)·set(H=2,L=1,T=45)=set(H=2,L=2,T=45), set(L=2,T=45)·set(H=2,L=2,T=45)=set(H=2,L=2,T=45), set(H=1,L=1,T=45)·set(H=1)=set(H=1,L=1,T=45), set(H=1,L=1,T=45)·set(H=2)=set(H=1,L=1,T=45), set(H=1,L=1,T=45)·set(L=1)=set(H=1,L=1,T=45), set(H=1,L=1,T=45)·set(L=2)=set(H=1,L=1,T=45), set(H=1,L=1,T=45)·set(T=45)=set(H=1,L=1,T=45), set(H=1,L=1,T=45)·set(H=1,L=1)=set(H=1,L=1,T=45), set(H=1,L=1,T=45)·set(H=1,L=2)=set(H=1,L=1,T=45), set(H=1,L=1,T=45)·set(H=1,T=45)=set(H=1,L=1,T=45), set(H=1,L=1,T=45)·set(H=2,L=1)=set(H=1,L=1,T=45), set(H=1,L=1,T=45)·set(H=2,L=2)=set(H=1,L=1,T=45), set(H=1,L=1,T=45)·set(H=2,T=45)=set(H=1,L=1,T=45), set(H=1,L=1,T=45)·set(L=1,T=45)=set(H=1,L=1,T=45), set(H=1,L=1,T=45)·set(L=2,T=45)=set(H=1,L=1,T=45), set(H=1,L=1,T=45)·set(H=1,L=1,T=45)=set(H=1,L=1,T=45), set(H=1,L=1,T=45)·set(H=1,L=2,T=45)=set(H=1,L=1,T=45), set(H=1,L=1,T=45)·set(H=2,L=1,T=45)=set(H=1,L=1,T=45), set(H=1,L=1,T=45)·set(H=2,L=2,T=45)=set(H=1,L=1,T=45), set(H=1,L=2,T=45)·set(H=1)=set(H=1,L=2,T=45), set(H=1,L=2,T=45)·set(H=2)=set(H=1,L=2,T=45), set(H=1,L=2,T=45)·set(L=1)=set(H=1,L=2,T=45), set(H=1,L=2,T=45)·set(L=2)=set(H=1,L=2,T=45), set(H=1,L=2,T=45)·set(T=45)=set(H=1,L=2,T=45), set(H=1,L=2,T=45)·set(H=1,L=1)=set(H=1,L=2,T=45), set(H=1,L=2,T=45)·set(H=1,L=2)=set(H=1,L=2,T=45), set(H=1,L=2,T=45)·set(H=1,T=45)=set(H=1,L=2,T=45), set(H=1,L=2,T=45)·set(H=2,L=1)=set(H=1,L=2,T=45), set(H=1,L=2,T=45)·set(H=2,L=2)=set(H=1,L=2,T=45), set(H=1,L=2,T=45)·set(H=2,T=45)=set(H=1,L=2,T=45), set(H=1,L=2,T=45)·set(L=1,T=45)=set(H=1,L=2,T=45), set(H=1,L=2,T=45)·set(L=2,T=45)=set(H=1,L=2,T=45), set(H=1,L=2,T=45)·set(H=1,L=1,T=45)=set(H=1,L=2,T=45), set(H=1,L=2,T=45)·set(H=1,L=2,T=45)=set(H=1,L=2,T=45), set(H=1,L=2,T=45)·set(H=2,L=1,T=45)=set(H=1,L=2,T=45), set(H=1,L=2,T=45)·set(H=2,L=2,T=45)=set(H=1,L=2,T=45), set(H=2,L=1,T=45)·set(H=1)=set(H=2,L=1,T=45), set(H=2,L=1,T=45)·set(H=2)=set(H=2,L=1,T=45), set(H=2,L=1,T=45)·set(L=1)=set(H=2,L=1,T=45), set(H=2,L=1,T=45)·set(L=2)=set(H=2,L=1,T=45), set(H=2,L=1,T=45)·set(T=45)=set(H=2,L=1,T=45), set(H=2,L=1,T=45)·set(H=1,L=1)=set(H=2,L=1,T=45), set(H=2,L=1,T=45)·set(H=1,L=2)=set(H=2,L=1,T=45), set(H=2,L=1,T=45)·set(H=1,T=45)=set(H=2,L=1,T=45), set(H=2,L=1,T=45)·set(H=2,L=1)=set(H=2,L=1,T=45), set(H=2,L=1,T=45)·set(H=2,L=2)=set(H=2,L=1,T=45), set(H=2,L=1,T=45)·set(H=2,T=45)=set(H=2,L=1,T=45), set(H=2,L=1,T=45)·set(L=1,T=45)=set(H=2,L=1,T=45), set(H=2,L=1,T=45)·set(L=2,T=45)=set(H=2,L=1,T=45), set(H=2,L=1,T=45)·set(H=1,L=1,T=45)=set(H=2,L=1,T=45), set(H=2,L=1,T=45)·set(H=1,L=2,T=45)=set(H=2,L=1,T=45), set(H=2,L=1,T=45)·set(H=2,L=1,T=45)=set(H=2,L=1,T=45), set(H=2,L=1,T=45)·set(H=2,L=2,T=45)=set(H=2,L=1,T=45), set(H=2,L=2,T=45)·set(H=1)=set(H=2,L=2,T=45), set(H=2,L=2,T=45)·set(H=2)=set(H=2,L=2,T=45), set(H=2,L=2,T=45)·set(L=1)=set(H=2,L=2,T=45), set(H=2,L=2,T=45)·set(L=2)=set(H=2,L=2,T=45), set(H=2,L=2,T=45)·set(T=45)=set(H=2,L=2,T=45), set(H=2,L=2,T=45)·set(H=1,L=1)=set(H=2,L=2,T=45), set(H=2,L=2,T=45)·set(H=1,L=2)=set(H=2,L=2,T=45), set(H=2,L=2,T=45)·set(H=1,T=45)=set(H=2,L=2,T=45), set(H=2,L=2,T=45)·set(H=2,L=1)=set(H=2,L=2,T=45), set(H=2,L=2,T=45)·set(H=2,L=2)=set(H=2,L=2,T=45), set(H=2,L=2,T=45)·set(H=2,T=45)=set(H=2,L=2,T=45), set(H=2,L=2,T=45)·set(L=1,T=45)=set(H=2,L=2,T=45), set(H=2,L=2,T=45)·set(L=2,T=45)=set(H=2,L=2,T=45), set(H=2,L=2,T=45)·set(H=1,L=1,T=45)=set(H=2,L=2,T=45), set(H=2,L=2,T=45)·set(H=1,L=2,T=45)=set(H=2,L=2,T=45), set(H=2,L=2,T=45)·set(H=2,L=1,T=45)=set(H=2,L=2,T=45), set(H=2,L=2,T=45)·set(H=2,L=2,T=45)=set(H=2,L=2,T=45)
  L_c_H(1,b1_45) = {(1)}
  L_c_H(set(H=1),b1_45) = {(1)}
  L_c_H(set(H=1,L=1),b1_45) = {(1)}
  L_c_H(set(H=1,L=1,T=45),b1_45) = {(1)}
  L_c_H(set(H=1,L=2),b1_45) = {(1)}
  L_c_H(set(H=1,L=2,T=45),b1_45) = {(1)}
  L_c_H(set(H=1,T=45),b1_45) = {(1)}
  L_c_H(set(H=2),b1_45) = {(2)}
  L_c_H(set(H=2,L=1),b1_45) = {(2)}
  L_c_H(set(H=2,L=1,T=45),b1_45) = {(2)}
  L_c_H(set(H=2,L=2),b1_45) = {(2)}
  L_c_H(set(H=2,L=2,T=45),b1_45) = {(2)}
  L_c_H(set(H=2,T=45),b1_45) = {(2)}
  L_c_H(set(L=1),b1_45) = {(1)}
  L_c_H(set(L=1,T=45),b1_45) = {(1)}
  L_c_H(set(L=2),b1_45) = {(1)}
  L_c_H(set(L=2,T=45),b1_45) = {(1)}
  L_c_H(set(T=45),b1_45) = {(1)}
  L_c_T(1,b1_45) = {(45)}
  L_c_T(set(H=1),b1_45) = {(45)}
  L_c_T(set(H=1,L=1),b1_45) = {(45)}
  L_c_T(set(H=1,L=1,T=45),b1_45) = {(45)}
  L_c_T(set(H=1,L=2),b1_45) = {(45)}
  L_c_T(set(H=1,L=2,T=45),b1_45) = {(45)}
  L_c_T(set(H=1,T=45),b1_45) = {(45)}
  L_c_T(set(H=2),b1_45) = {(45)}
  L_c_T(set(H=2,L=1),b1_45) = {(45)}
  L_c_T(set(H=2,L=1,T=45),b1_45) = {(45)}
  L_c_T(set(H=2,L=2),b1_45) = {(45)}
  L_c_T(set(H=2,L=2,T=45),b1_45) = {(45)}
  L_c_T(set(H=2,T=45),b1_45) = {(45)}
  L_c_T(set(L=1),b1_45) = {(45)}
  L_c_T(set(L=1,T=45),b1_45) = {(45)}
  L_c_T(set(L=2),b1_45) = {(45)}
  L_c_T(set(L=2,T=45),b1_45) = {(45)}
  L_c_T(set(T=45),b1_45) = {(45)}
  L_c_L(1,b1_45) = {(1,45,1) (2,45,2)}
  L_c_L(set(H=1),b1_45) = {(1,45,1) (2,45,2)}
  L_c_L(set(H=1,L=1),b1_45) = {(1,45,1) (2,45,1)}
  L_c_L(set(H=1,L=1,T=45),b1_45) = {(1,45,1) (2,45,1)}
  L_c_L(set(H=1,L=2),b1_45) = {(1,45,2) (2,45,2)}
  L_c_L(set(H=1,L=2,T=45),b1_45) = {(1,45,2) (2,45,2)}
  L_c_L(set(H=1,T=45),b1_45) = {(1,45,1) (2,45,2)}
  L_c_L(set(H=2),b1_45) = {(1,45,1) (2,45,2)}
  L_c_L(set(H=2,L=1),b1_45) = {(1,45,1) (2,45,1)}
  L_c_L(set(H=2,L=1,T=45),b1_45) = {(1,45,1) (2,45,1)}
  L_c_L(set(H=2,L=2),b1_45) = {(1,45,2) (2,45,2)}
  L_c_L(set(H=2,L=2,T=45),b1_45) = {(1,45,2) (2,45,2)}
  L_c_L(set(H=2,T=45),b1_45) = {(1,45,1) (2,45,2)}
  L_c_L(set(L=1),b1_45) = {(1,45,1) (2,45,1)}
  L_c_L(set(L=1,T=45),b1_45) = {(1,45,1) (2,45,1)}
  L_c_L(set(L=2),b1_45) = {(1,45,2) (2,45,2)}
  L_c_L(set(L=2,T=45),b1_45) = {(1,45,2) (2,45,2)}
  L_c_L(set(T=45),b1_45) = {(1,45,1) (2,45,2)}
```

### FC81 · Argument 4, and who can be surprised

**The claim.** Surp(t;a,b) := Sel(t) ∧ Viol(t;a,b) ∧ (a,b) ∈ C∖H ∧ Occurs(a,b). (a) Surp ⇒ H ⊊ C. (b) No transport ⇒ no Surp. (c) H = C ⇒ no Surp. (d) Con(t) ∧ Viol ⇒ ¬Surp (I53).

**What it rests on.** (d) rests on the same history as FC78 (I52, I53, I56, I90). Every invention the counterexample depends on: I50, I52, I53, I56, I90, I92.

**Reproduce.** `cd "/home/user/ThreadSmith/Semantics/results/S104 Round 2 - maths" && python3 -m model.run --claim FC81 --scale 4 --time-cap 45`

**Part: (d) Con(t) ∧ Viol ⇒ ¬Surp (under I53)** (computed: not as claimed). a constructed transport violated at an occurring pair is not surprised

```
In a history like FC78's (the codomain represented, Prepares, no representation of t, H or the survival condition), t (the pole's forward transport into an organization whose c_L gives L = 1 under set H=2) is faithful on H = {(1,b1_45)} (Hom included) and violated at (set(H=2), b1_45) ∉ H, which occurs. Con: True; Sel: True; Viol: True; Surp: True. The clause rests on FC78's claim that Sel excludes Con, which fails under D12.1.
```

### FC82 · The two responses to a violation have no common result

**The claim.** SelResp(t → t'): t' ∈ 𝒯, reached from t by μ, surviving on H ∪ {(a,b)}; ConResp(→ t''): t'' or its codomain new, with Con(t''). Under I53 no transport is the result of both (Sel(t') excludes Con(t')).

**What it rests on.** Rests on the same history as FC78 (I52, I53, I56, I90). Every invention the counterexample depends on: I52, I53, I56, I90, I92.

**Reproduce.** `cd "/home/user/ThreadSmith/Semantics/results/S104 Round 2 - maths" && python3 -m model.run --claim FC82 --scale 4 --time-cap 45`

**Part: no common result** (computed: not as claimed). no transport is the result of both a selection response and a construction response

```
t' = the pole's forward transport, new relative to an empty repertoire, survives on H ∪ {('set(H=2)', 'b1_45')} (SelResp) and has Con in the same history (ConResp): True and True. As in FC78, D12.1 does not exclude a represented codomain.
```

### FC83 · Only the construction response can be originative

**The claim.** Claim to test: SelResp(t → t') ⇒ ¬Origin(s,c',p,h,e) for the content c' that t' carries to. (G) needs Build, and Build needs a subhistory that prepares a represented organization for explanatory use of c' (I56). Sel(t') forbids occurrences that represent t', H or the survival condition (L195), not the organization t' carries to (which Con names, L197).

**What it rests on.** Rests on I56 (Build's three primitives) and I90 (Θ by hand); it is the case FC83's own Look names. Every invention the counterexample depends on: I52, I56, I90, I92.

**Reproduce.** `cd "/home/user/ThreadSmith/Semantics/results/S104 Round 2 - maths" && python3 -m model.run --claim FC83 --scale 4 --time-cap 45`

**Part: only construction is originative** (computed: not as claimed). SelResp(t → t') ⇒ ¬Origin(s, c', …)

```
A history in which t' survives on H ∪ {('set(H=2)', 'b1_45')} (SelResp: True) and an owned subhistory prepares a represented organization for c' with a binding construction and is no transfer composite (Build's three primitives, I56, set true), c' used to address p (Attempt) and no earlier content matches it (New): Origin True. Nothing in D12.1 or D13.3 ties Build's subhistory to the selection history; the claim follows only on one of the two conditions its Look names.
```

### FC102 · Argument 10: surprise, the structural failure of selection, and the constructed layer

**The claim.** With I68: (a) t0 (window w) survives on H0 and is violated at the re-emergence pair, which lies in C0∖H0: Surp. (b) If the occlusion hides the thing for longer than w steps, every window-w occupancy predictor fails on the extended history (two histories with equal last-w occupancy and different re-emergence cells); if w is at least that long, an occupancy predictor can extrapolate and the failure is not structural. (c) t1 meets (F1) and (F2) on the extended contract, and each persistence component's signature read through t1 equals its thing's continuity subnetwork's (Argument 1).

**What it rests on.** Rests on I68 and I100 (six cells, occlusion of a run of interior cells, occupancy without identity as L620 has it, reflection at the ends); I52, the claim's own, plays no part in this computation. Every invention the counterexample depends on: I52, I68, I100.

**Reproduce.** `cd "/home/user/ThreadSmith/Semantics/results/S104 Round 2 - maths" && python3 -m model.run --claim FC102 --scale 4 --time-cap 45`

**Part: (b) second half: a window longer than the occlusion** (computed: not as claimed). w > L ⇒ an occupancy predictor can extrapolate (the failure is not structural)

```
one thing, failing (w, L) with L < w: [(1, 0), (2, 1), (3, 2)]; two things: [(1, 0), (2, 0), (2, 1), (3, 1), (3, 2)]. With two things the occupancy readings carry no identity: two things that cross and two that stay give the same readings, so a window-w predictor can fail with no occlusion at all (things, w, L and two starts: ((2, 1, 0), (((0, -1), (1, -1)), ((0, -1), (1, 0))))). With one thing the window needs two visible frames (w ≥ L + 2) for the velocity. FC102 (b)'s second half holds under neither count as stated, on I68's encoding with this program's occlusion (I100).
```

## Every claim

| claim | status | parts | rests on |
| --- | --- | --- | --- |
| FC01 | HOLDS ON ALL MODELS TRIED | 1 holds on all models tried; 1 witness found | I03, I77, I78 |
| FC02 | HOLDS ON ALL MODELS TRIED | 1 witness found; 1 holds on all models tried; 1 computed: as claimed | I04, I05, I65, I77, I78, I80, I92 |
| FC03 | HOLDS ON ALL MODELS TRIED | 1 holds on all models tried | I10, I77, I78 |
| FC04 | HOLDS ON ALL MODELS TRIED | 1 holds on all models tried; 1 witness found | I10, I11, I77, I78 |
| FC05 | COUNTEREXAMPLE FOUND | 2 holds on all models tried; 1 counterexample found | I10, I77, I78, I93 |
| FC06 | HOLDS ON ALL MODELS TRIED | 1 holds on all models tried | I04, I07, I09, I77, I78, I80, I102 |
| FC07 | HOLDS ON ALL MODELS TRIED | 5 computed: as claimed | I04, I06, I07, I09, I65, I80, I92, I102 |
| FC08 | HOLDS ON ALL MODELS TRIED | 1 witness found | I04, I06, I07, I77, I78 |
| FC09 | HOLDS ON ALL MODELS TRIED | 1 computed: as claimed | I08, I78 |
| FC10 | HOLDS ON ALL MODELS TRIED | 1 holds on all models tried; 1 not tested | I08, I09, I77, I78 |
| FC11 | HOLDS ON ALL MODELS TRIED | 1 computed: as claimed; 1 holds by construction | I04, I09, I80, I92 |
| FC12 | HOLDS ON ALL MODELS TRIED | 1 holds on all models tried | I09, I77, I78, I80 |
| FC13 | HOLDS ON ALL MODELS TRIED | 1 holds on all models tried; 1 holds by construction | I04, I06, I08, I09, I70, I77, I78 |
| FC14 | HOLDS ON ALL MODELS TRIED | 1 computed: as claimed | — |
| FC15 | HOLDS ON ALL MODELS TRIED | 1 holds on all models tried | I12, I18, I77, I78, I81 |
| FC16 | HOLDS ON ALL MODELS TRIED | 1 holds on all models tried | I10, I12, I77, I78, I81 |
| FC17 | HOLDS ON ALL MODELS TRIED | 1 holds on all models tried | I12, I13, I14, I15, I77, I78, I81 |
| FC18 | COUNTEREXAMPLE FOUND | 1 holds on all models tried; 1 counterexample found | I10, I13, I14, I77, I78, I81, I94 |
| FC19 | HOLDS ON ALL MODELS TRIED | 2 witness found | I14, I15, I77, I78, I81, I101 |
| FC20 | COUNTEREXAMPLE FOUND | 1 counterexample found; 2 holds on all models tried | I14, I16, I20, I21, I49, I50, I77, I78, I81 |
| FC21 | HOLDS ON ALL MODELS TRIED | 1 holds on all models tried; 1 witness found; 1 holds by construction | I21, I22, I26, I77, I78, I81, I85, I101 |
| FC22 | HOLDS ON ALL MODELS TRIED | 1 holds on all models tried | I21, I22, I77, I78, I81 |
| FC23 | COUNTEREXAMPLE FOUND | 2 holds on all models tried; 1 counterexample found | I21, I22, I24, I25, I77, I78, I79, I81, I82, I83 |
| FC24 | HOLDS ON ALL MODELS TRIED | 1 holds on all models tried; 1 not tested | I24, I77, I78, I79, I81, I83 |
| FC25 | COUNTEREXAMPLE FOUND | 2 holds on all models tried; 1 witness found; 1 counterexample found | I03, I04, I14, I32, I77, I78, I80, I101 |
| FC26 | HOLDS ON ALL MODELS TRIED | 2 computed: as claimed; 1 look: not as expected | I04, I20, I21, I24, I27, I65, I79, I85, I92 |
| FC27 | HOLDS ON ALL MODELS TRIED | 1 computed: as claimed | I04, I65, I92 |
| FC28 | HOLDS ON ALL MODELS TRIED | 1 computed: as claimed; 1 look: not as expected | I20, I65, I92 |
| FC29 | HOLDS ON ALL MODELS TRIED | 1 holds on all models tried | I12, I77, I78, I81 |
| FC30 | HOLDS ON ALL MODELS TRIED | 1 holds by construction | I20, I27, I28 |
| FC31 | NOT TESTED | 1 not tested | I49 |
| FC32 | NOT TESTED | 1 not tested | I20, I27, I28 |
| FC33 | HOLDS ON ALL MODELS TRIED | 1 holds on all models tried; 1 not tested | I24, I27, I28, I70, I77, I78, I81 |
| FC34 | HOLDS ON ALL MODELS TRIED | 5 witness found | I24, I27, I73, I77, I78, I79, I81, I85, I101 |
| FC35 | NOT TESTED | 1 not tested | I51 |
| FC36 | HOLDS ON ALL MODELS TRIED | 1 computed: as claimed; 1 holds by construction | I72 |
| FC37 | HOLDS ON ALL MODELS TRIED | 2 holds on all models tried | I77, I78, I81 |
| FC38 | HOLDS ON ALL MODELS TRIED | 1 computed: as claimed | I30 |
| FC39 | HOLDS ON ALL MODELS TRIED | 1 computed: as claimed | I30 |
| FC40 | HOLDS ON ALL MODELS TRIED | 1 holds on all models tried | I30, I31, I91 |
| FC41 | HOLDS ON ALL MODELS TRIED | 1 holds on all models tried | I29, I77 |
| FC42 | HOLDS ON ALL MODELS TRIED | 1 computed: as claimed | I30 |
| FC43 | HOLDS ON ALL MODELS TRIED | 1 holds on all models tried | I33, I37, I77, I78, I81, I86 |
| FC44 | HOLDS ON ALL MODELS TRIED | 1 holds on all models tried; 1 witness found | I14, I19, I36, I77, I78, I81, I101 |
| FC45 | HOLDS ON ALL MODELS TRIED | 1 holds on all models tried; 1 holds by construction | I17, I19, I20, I70, I77, I78, I81 |
| FC46 | HOLDS ON ALL MODELS TRIED | 1 holds on all models tried | I19, I21, I77, I78, I81, I85 |
| FC47 | HOLDS ON ALL MODELS TRIED | 1 holds on all models tried; 1 computed: as claimed | I19, I38, I40, I42, I43, I77, I78, I81, I87, I88, I89 |
| FC48 | HOLDS ON ALL MODELS TRIED | 1 holds on all models tried | I21, I77, I78, I81 |
| FC49 | HOLDS ON ALL MODELS TRIED | 1 holds on all models tried | I16, I17, I33, I77, I78, I81, I86 |
| FC50 | HOLDS ON ALL MODELS TRIED | 1 holds on all models tried; 1 holds by construction | I11, I33, I77, I78, I81, I86 |
| FC51 | HOLDS ON ALL MODELS TRIED | 2 holds on all models tried | I18, I24, I27, I77, I78, I81, I85 |
| FC52 | HOLDS ON ALL MODELS TRIED | 1 holds on all models tried | I19, I34, I77, I78, I81 |
| FC53 | HOLDS ON ALL MODELS TRIED | 2 computed: as claimed | I34, I38, I40, I87, I88, I89, I90 |
| FC54 | HOLDS ON ALL MODELS TRIED | 1 holds on all models tried | I19, I33, I34, I35, I77, I78, I81 |
| FC55 | HOLDS ON ALL MODELS TRIED | 1 computed: as claimed | — |
| FC56 | HOLDS ON ALL MODELS TRIED | 1 holds on all models tried; 1 computed: as claimed | I38, I40, I41, I87, I88, I89 |
| FC57 | HOLDS ON ALL MODELS TRIED | 1 holds on all models tried | I63, I64, I77 |
| FC58 | HOLDS ON ALL MODELS TRIED | 2 holds on all models tried; 1 look: as expected | I63, I64, I77 |
| FC59 | HOLDS ON ALL MODELS TRIED | 1 computed: as claimed | I64 |
| FC60 | HOLDS ON ALL MODELS TRIED | 1 holds by construction; 1 computed: as claimed | I24, I39, I87, I89 |
| FC61 | HOLDS ON ALL MODELS TRIED | 1 holds on all models tried; 1 computed: as claimed | I63, I77 |
| FC62 | HOLDS ON ALL MODELS TRIED | 1 computed: as claimed | I03, I14, I78, I79 |
| FC63 | COUNTEREXAMPLE FOUND | 3 computed: as claimed; 1 computed: not as claimed | I03, I27, I66, I81, I82, I99 |
| FC64 | HOLDS ON ALL MODELS TRIED | 1 holds on all models tried | I77 |
| FC65 | HOLDS ON ALL MODELS TRIED | 1 holds on all models tried | I77 |
| FC66 | HOLDS ON ALL MODELS TRIED | 1 holds on all models tried; 1 computed: as claimed | I77 |
| FC67 | HOLDS ON ALL MODELS TRIED | 1 holds on all models tried; 1 holds by construction | I54, I70, I77, I78, I81 |
| FC68 | HOLDS ON ALL MODELS TRIED | 1 holds on all models tried; 1 computed: as claimed | I20, I38, I40, I41, I77, I78, I81, I87, I89 |
| FC69 | HOLDS ON ALL MODELS TRIED | 2 computed: as claimed | I40, I87, I89 |
| FC70 | HOLDS ON ALL MODELS TRIED | 1 computed: as claimed | I40, I41, I87, I89 |
| FC71 | HOLDS ON ALL MODELS TRIED | 2 computed: as claimed | I38, I43, I87, I88, I89 |
| FC72 | HOLDS ON ALL MODELS TRIED | 1 computed: as claimed | I38, I39, I87, I89 |
| FC73 | HOLDS ON ALL MODELS TRIED | 1 computed: as claimed | I38, I87, I89 |
| FC74 | HOLDS ON ALL MODELS TRIED | 1 witness found | I45, I77, I78, I81 |
| FC75 | HOLDS ON ALL MODELS TRIED | 2 computed: as claimed; 1 holds by construction; 1 look: as expected | I44, I46, I95 |
| FC76 | HOLDS ON ALL MODELS TRIED | 1 computed: as claimed | I47, I90, I95 |
| FC77 | COUNTEREXAMPLE FOUND | 1 counterexample found; 1 holds on all models tried; 1 computed: as claimed | I18, I48, I52, I77, I78, I81, I90 |
| FC78 | COUNTEREXAMPLE FOUND | 1 computed: not as claimed | I52, I53, I54, I56, I90, I92 |
| FC79 | HOLDS ON ALL MODELS TRIED | 1 holds by construction | I49, I52 |
| FC80 | HOLDS ON ALL MODELS TRIED | 1 holds on all models tried; 1 witness found; 1 not tested | I02, I52, I71, I77, I78, I81 |
| FC81 | COUNTEREXAMPLE FOUND | 1 holds by construction; 1 computed: not as claimed | I50, I52, I53, I56, I90, I92 |
| FC82 | COUNTEREXAMPLE FOUND | 1 computed: not as claimed | I52, I53, I56, I90, I92 |
| FC83 | COUNTEREXAMPLE FOUND | 1 computed: not as claimed | I52, I56, I90, I92 |
| FC84 | HOLDS ON ALL MODELS TRIED | 1 holds by construction | I53, I56 |
| FC85 | HOLDS ON ALL MODELS TRIED | 1 holds on all models tried; 1 no witness found; 1 computed: as claimed | I48, I77, I78, I81 |
| FC86 | HOLDS ON ALL MODELS TRIED | 1 holds on all models tried; 1 look: as expected | I57, I96 |
| FC87 | HOLDS ON ALL MODELS TRIED | 1 holds by construction | I46, I57 |
| FC88 | HOLDS ON ALL MODELS TRIED | 1 computed: as claimed | I57, I58, I96 |
| FC89 | NOT TESTED | 1 not tested | I59, I60 |
| FC90 | NOT TESTED | 1 not tested | I44, I57, I59, I60, I68 |
| FC91 | HOLDS ON ALL MODELS TRIED | 1 holds on all models tried; 1 witness found | I61, I97 |
| FC92 | HOLDS ON ALL MODELS TRIED | 1 holds on all models tried | I61, I97 |
| FC93 | HOLDS ON ALL MODELS TRIED | 1 holds on all models tried; 1 witness found | I62, I98 |
| FC94 | NOT TESTED | 1 not tested | I74, I75 |
| FC95 | HOLDS ON ALL MODELS TRIED | 1 computed: as claimed | I48, I52, I90, I92 |
| FC96 | HOLDS ON ALL MODELS TRIED | 2 holds on all models tried | I10, I12, I14, I77, I78, I81 |
| FC97 | HOLDS ON ALL MODELS TRIED | 1 computed: as claimed; 1 not tested | I01, I48, I67 |
| FC98 | NOT TESTED | 1 not tested | I20, I29, I33, I34, I39, I46, I47, I55, I56, I58, I59 |
| FC99 | HOLDS ON ALL MODELS TRIED | 1 computed: as claimed | I65, I92 |
| FC100 | HOLDS ON ALL MODELS TRIED | 1 holds on all models tried; 1 not tested | I45, I70, I77, I78, I81 |
| FC101 | HOLDS ON ALL MODELS TRIED | 1 holds by construction; 1 computed: as claimed | I29, I46, I78 |
| FC102 | COUNTEREXAMPLE FOUND | 1 computed: as claimed; 1 computed: not as claimed; 1 not tested | I52, I68, I100 |
| FC103 | HOLDS ON ALL MODELS TRIED | 1 computed: as claimed; 1 not tested | I10, I14, I68, I69, I100 |
| FC104 | NOT TESTED | 1 not tested | I49, I50 |
| FC105 | NOT TESTED | 1 not tested | I45 |
| FC106 | HOLDS ON ALL MODELS TRIED | 1 holds on all models tried; 1 not tested | I76, I77, I78, I81 |
| FC107 | NOT TESTED | 1 not tested | I76 |
| FC108 | HOLDS ON ALL MODELS TRIED | 1 holds by construction | I23 |
| FC109 | HOLDS ON ALL MODELS TRIED | 1 computed: as claimed | I10, I12, I13, I14, I61, I63, I64, I71 |
| FC110 | NOT TESTED | 1 not tested | I74, I75 |

## Details, claim by claim

### FC01 · Solutions shrink as relations shrink; deletion never removes a solution — HOLDS ON ALL MODELS TRIED

**The claim.** If L_j(a,b) ⊆ L'_j(a,b) for every j, then Sol_D(a,b) ⊆ Sol_D'(a,b). In particular Sol_{D−G}(a,b) ⊇ Sol_D(a,b), where D−G deletes the components of G (full relations).

**Rests on.** Claim's inventions: I03. Program's: I77, I78. **Reproduce.** `cd "/home/user/ThreadSmith/Semantics/results/S104 Round 2 - maths" && python3 -m model.run --claim FC01 --scale 4 --time-cap 45`

- **(a) monotone; deletion keeps solutions** [for all] — *holds on all models tried*. L_j ⊆ L'_j for every j ⇒ Sol_D ⊆ Sol_D'; Sol_{D−G} ⊇ Sol_D
  - Searched: sizes ports=1 dom≤1 comps=1 |B|=1 edits=0 … ports=3 dom≤2 comps=3 |B|=2 edits=2 (108 sizes, 240 draws each); families: G-surg, G-free; seed 104011; 25920 models tried.

- **(look) deletion can make an undetermined answer determined** [there is] — *witness found*. there are D, (a,b), G with Ans_p(a,b) = ⊥ (Sol empty) and Ans on D−G determined
  - Searched: sizes ports=1 dom≤1 comps=1 |B|=1 edits=0 … ports=3 dom≤2 comps=3 |B|=2 edits=2 (108 sizes, 160 draws each); families: G-surg, G-free; seed 104012; 4 models tried; first found at size ports=1 dom≤1 comps=1 |B|=1 edits=0.

  ```
  As the Look expects: at (1,b0) Sol_D is empty, so the port query answers ⊥; deleting {c0} gives the determined answer 0.
  question p: target D, b0 = b0, query Q_w (reads the designated port) designating p0, C = {(1,b0)}
  organization D
    ports: p0 ∈ {0}
    components: c0 on (p0)
    boundaries B = {b0}; edits A = {1}
    L_c0(1,b0) = {}
  ```

### FC02 · Direction is read from the admitted edits; output status is not — HOLDS ON ALL MODELS TRIED

**The claim.** (a) Input(v) and asg(v) are functions of the setting edits in A (I04); two organizations with the same L and different A can differ in both. (b) Output(v,j) (I05) is a function of L_j(1,·) alone and does not depend on A. (c) In the pole encoding, c_L's relation L = H cot θ (θ in (0°,90°)) determines each of H, θ, L given the other two, so H and θ are outputs of c_L as well as L; the direction H,θ → L is carried by asg, not by output status.

**Rests on.** Claim's inventions: I04, I05, I65. Program's: I77, I78, I80, I92. **Reproduce.** `cd "/home/user/ThreadSmith/Semantics/results/S104 Round 2 - maths" && python3 -m model.run --claim FC02 --scale 4 --time-cap 45`

- **(a) Input and asg depend on A** [there is] — *witness found*. two organizations with the same L and different A differ in Input or asg
  - Searched: sizes ports=1 dom≤1 comps=1 |B|=1 edits=0 … ports=3 dom≤2 comps=3 |B|=2 edits=2 (108 sizes, 160 draws each); families: G-surg; seed 104021; 2 models tried; first found at size ports=1 dom≤1 comps=1 |B|=1 edits=1.

  ```
  D and D' have the same relations and differ only in A (D' lacks the setting edits of p0 other than 1).
  Input(p0): True in D, False in D'; asg(p0): h_p0 in D, None in D'.
  organization D
    ports: p0 ∈ {0}
    components: h_p0 on (p0)
    boundaries B = {b0}; edits A = {1,[p0=0]}
    composition (other than with 1): [p0=0]·[p0=0]=[p0=0]
    L_h_p0(1,b0) = {}
    L_h_p0([p0=0],b0) = {(0)}
  A of D' = {1}
  ```

- **(b) Output does not depend on A** [for all] — *holds on all models tried*. Out(v, j) is the same for D and D' (same L_j(1,·), different A)
  - Searched: sizes ports=1 dom≤1 comps=1 |B|=1 edits=0 … ports=3 dom≤2 comps=3 |B|=2 edits=2 (108 sizes, 160 draws each); families: G-surg; seed 104022; 10239 models tried.

- **(c) pole: c_L determines each of its ports** [computation] — *computed: as claimed*. Out(H,c_L), Out(θ,c_L), Out(L,c_L) all hold on the grid (I65)

  ```
  Out(v, c_L) for v = H, θ, L: {'H': True, 'T': True, 'L': True}. asg (read off the setting edits, I04): {'H': 'c_H', 'T': 'c_T', 'L': 'c_L'}. The identity edit is a setting edit of H and of θ (I80): True.
  ```

### FC03 · 'Of one kind on C' is an equivalence relation — HOLDS ON ALL MODELS TRIED

**The claim.** j ~_C j' (I10) is reflexive, symmetric and transitive on J.

**Rests on.** Claim's inventions: I10. Program's: I77, I78. **Reproduce.** `cd "/home/user/ThreadSmith/Semantics/results/S104 Round 2 - maths" && python3 -m model.run --claim FC03 --scale 4 --time-cap 45`

- **equivalence** [for all] — *holds on all models tried*. ~_C is reflexive, symmetric and transitive
  - Searched: sizes ports=1 dom≤1 comps=1 |B|=1 edits=0 … ports=3 dom≤2 comps=4 |B|=2 edits=2 (144 sizes, 160 draws each); families: G-free (equal domains); seed 104031; 23040 models tried.

### FC04 · A coarser contract identifies more components; a finer one can separate them — HOLDS ON ALL MODELS TRIED

**The claim.** C' ⊆ C ⇒ (j ~_C j' ⇒ j ~_C' j'), since one footprint bijection serving every pair of C serves every pair of C'. And there are D, C' ⊊ C, j, j' with j ~_C' j' and not j ~_C j'.

**Rests on.** Claim's inventions: I10, I11. Program's: I77, I78. **Reproduce.** `cd "/home/user/ThreadSmith/Semantics/results/S104 Round 2 - maths" && python3 -m model.run --claim FC04 --scale 4 --time-cap 45`

- **(a) coarser identifies more** [for all] — *holds on all models tried*. C' ⊆ C ∧ j ~_C j' ⇒ j ~_C' j'
  - Searched: sizes ports=1 dom≤1 comps=1 |B|=1 edits=0 … ports=3 dom≤2 comps=4 |B|=2 edits=2 (144 sizes, 160 draws each); families: G-free (equal domains); seed 104041; 23040 models tried.

- **(b) a finer contract can separate** [there is] — *witness found*. there are D, C' ⊊ C, j, j' with j ~_C' j' and not j ~_C j'
  - Searched: sizes ports=1 dom≤1 comps=1 |B|=1 edits=0 … ports=3 dom≤2 comps=4 |B|=2 edits=2 (144 sizes, 160 draws each); families: G-free (equal domains); seed 104042; 1309 models tried; first found at size ports=1 dom≤1 comps=2 |B|=1 edits=1.

  ```
  c0 ~_C' c1 and not on C ⊋ C'
  organization D
    ports: p0 ∈ {0}
    components: c0 on (p0); c1 on (p0)
    boundaries B = {b0}; edits A = {1,e1}
    composition (other than with 1): e1·e1=undef
    L_c0(1,b0) = {(0)}
    L_c0(e1,b0) = {(0)}
    L_c1(1,b0) = {(0)}
    L_c1(e1,b0) = {}
  C = {(1,b0), (e1,b0)}
  C' = {(1,b0)}
  ```

### FC05 · Kinds are fixed by relations, not by solution values — COUNTEREXAMPLE FOUND

**The claim.** sig_C(j) is a function of (L_j(a,b))_{(a,b)∈C} alone. If β_*L_j(a,b) = L_j'(a,b) for every (a,b) in C, then j ~_C j', whatever the projections of Sol_D(a,b) on V_j and V_j' are; adding to C a pair at which β_*L_j = L_j' leaves the relation between j and j' as it was.

**Rests on.** Claim's inventions: I10. Program's: I77, I78, I93. **Reproduce.** `cd "/home/user/ThreadSmith/Semantics/results/S104 Round 2 - maths" && python3 -m model.run --claim FC05 --scale 4 --time-cap 45`

- **(ii) reading (i): β a witness of ~_C** [for all] — *holds on all models tried*. if β witnesses j ~_C j' and β_*L_j = L_j' at a new pair x, then j ~_{C∪{x}} j'
  - Searched: sizes ports=1 dom≤1 comps=1 |B|=1 edits=0 … ports=3 dom≤2 comps=3 |B|=2 edits=2 (108 sizes, 240 draws each); families: G-free (equal domains); seed 104051; 10372 models tried; 2951 of them meeting the claim's hypothesis.

- **(ii) reading (ii): any bijection** [for all] — *counterexample found*. if j ~_C j' and β_*L_j = L_j' at a new pair x for some footprint bijection β, then j ~_{C∪{x}} j'
  - Searched: sizes ports=1 dom≤1 comps=1 |B|=1 edits=0 … ports=3 dom≤2 comps=3 |B|=2 edits=2 (108 sizes, 800 draws each); families: G-free (equal domains); seed 104052; 10729 models tried; 4392 of them meeting the claim's hypothesis; first found at size ports=2 dom≤2 comps=2 |B|=1 edits=1.
  - The counterexample is written out above, under Counterexamples.

- **(i) signatures use relations only** [for all] — *holds on all models tried*. adding a component that changes Sol leaves ~_C among the other components unchanged
  - Searched: sizes ports=1 dom≤1 comps=1 |B|=1 edits=0 … ports=3 dom≤2 comps=3 |B|=2 edits=2 (108 sizes, 120 draws each); families: G-free (equal domains); seed 104053; 12960 models tried.

### FC06 · A setting edit leaves every reader's relation as it was — HOLDS ON ALL MODELS TRIED

**The claim.** Under I04, for every port m, every setting edit a of m and every component j ≠ asg(m): L_j(a,b) = L_j(1,b). Hence every component that reads m and does not assign it is invariant under interventions on m on every contract (I09): the first clause of the measurement bullet holds of every reader of m.

**Rests on.** Claim's inventions: I04, I07, I09. Program's: I77, I78, I80, I102. **Reproduce.** `cd "/home/user/ThreadSmith/Semantics/results/S104 Round 2 - maths" && python3 -m model.run --claim FC06 --scale 4 --time-cap 45`

- **setting edits leave readers as they were** [for all] — *holds on all models tried*. ∀m with asg(m) defined, ∀a ∈ Set_m, ∀j ≠ asg(m): L_j(a,b) = L_j(1,b); every reader of m is invariant under Set_m on every contract
  - Searched: sizes ports=1 dom≤1 comps=1 |B|=1 edits=0 … ports=3 dom≤3 comps=3 |B|=2 edits=2 (162 sizes, 160 draws each); families: G-surg, G-free; seed 104061; 25920 models tried.

### FC07 · The three families on the pole's contracts, under both readings of 'observation edit' — HOLDS ON ALL MODELS TRIED

**The claim.** Causal_C(j): C holds a setting edit of j's output port that changes L_j, and j is invariant under Obs on C. (a) Under R-i, if j reads a port m other than its output o and C sets o, that setting edit alters asg(o) = j and leaves asg(m): it is in Obs, and j changes under it, so ¬Causal_C(j); and j is a measurement of m (FC06 and that edit). On a contract that sets every port, Causal_C is the set of components that read no port besides their own output. (b) Under R-ii, Obs holds only non-setting edits of a reporting component. Pole (I65), contract C1 = settings of H and θ: under both readings c_H, c_θ ∈ Causal and c_L is in no family (C1 sets no output of c_L and holds no edit of it). Contract C2 = settings of H, θ and L: under R-i c_H, c_θ ∈ Causal, c_L ∈ Meas(·,H) ∩ Meas(·,θ), c_L ∉ Causal; under R-ii c_H, c_θ, c_L ∈ Causal and no component is a measurement.

**Rests on.** Claim's inventions: I04, I06, I07, I09, I65. Program's: I80, I92, I102. **Reproduce.** `cd "/home/user/ThreadSmith/Semantics/results/S104 Round 2 - maths" && python3 -m model.run --claim FC07 --scale 4 --time-cap 45`

- **pole C1 under R-i** [computation] — *computed: as claimed*. the families FC07 states for C1 under R-i: {'causal': ['c_H', 'c_T'], 'meas': [], 'rule': []}

  ```
  computed: {'causal': ['c_H', 'c_T'], 'meas': [], 'rule': []}; Obs(R-i) = {set(H=1,L=1), set(H=1,L=1/3√3), set(H=1,L=2), set(H=1,L=2/3√3), set(H=1,L=2√3), set(H=1,L=3), set(H=1,L=3√3), set(H=1,L=√3), set(H=2,L=1), set(H=2,L=1/3√3), set(H=2,L=2), set(H=2,L=2/3√3), set(H=2,L=2√3), set(H=2,L=3), set(H=2,L=3√3), set(H=2,L=√3), set(H=3,L=1), set(H=3,L=1/3√3), set(H=3,L=2), set(H=3,L=2/3√3), set(H=3,L=2√3), set(H=3,L=3), set(H=3,L=3√3), set(H=3,L=√3), set(L=1), set(L=1,T=30), set(L=1,T=45), set(L=1,T=60), set(L=1/3√3), set(L=1/3√3,T=30), set(L=1/3√3,T=45), set(L=1/3√3,T=60), set(L=2), set(L=2,T=30), set(L=2,T=45), set(L=2,T=60), set(L=2/3√3), set(L=2/3√3,T=30), set(L=2/3√3,T=45), set(L=2/3√3,T=60), set(L=2√3), set(L=2√3,T=30), set(L=2√3,T=45), set(L=2√3,T=60), set(L=3), set(L=3,T=30), set(L=3,T=45), set(L=3,T=60), set(L=3√3), set(L=3√3,T=30), set(L=3√3,T=45), set(L=3√3,T=60), set(L=√3), set(L=√3,T=30), set(L=√3,T=45), set(L=√3,T=60)}
  ```

- **pole C1 under R-ii** [computation] — *computed: as claimed*. the families FC07 states for C1 under R-ii: {'causal': ['c_H', 'c_T'], 'meas': [], 'rule': []}

  ```
  computed: {'causal': ['c_H', 'c_T'], 'meas': [], 'rule': []}; Obs(R-ii) = {set(H=1,L=1), set(H=1,L=1/3√3), set(H=1,L=2), set(H=1,L=2/3√3), set(H=1,L=2√3), set(H=1,L=3), set(H=1,L=3√3), set(H=1,L=√3), set(H=2,L=1), set(H=2,L=1/3√3), set(H=2,L=2), set(H=2,L=2/3√3), set(H=2,L=2√3), set(H=2,L=3), set(H=2,L=3√3), set(H=2,L=√3), set(H=3,L=1), set(H=3,L=1/3√3), set(H=3,L=2), set(H=3,L=2/3√3), set(H=3,L=2√3), set(H=3,L=3), set(H=3,L=3√3), set(H=3,L=√3), set(L=1,T=30), set(L=1,T=45), set(L=1,T=60), set(L=1/3√3,T=30), set(L=1/3√3,T=45), set(L=1/3√3,T=60), set(L=2,T=30), set(L=2,T=45), set(L=2,T=60), set(L=2/3√3,T=30), set(L=2/3√3,T=45), set(L=2/3√3,T=60), set(L=2√3,T=30), set(L=2√3,T=45), set(L=2√3,T=60), set(L=3,T=30), set(L=3,T=45), set(L=3,T=60), set(L=3√3,T=30), set(L=3√3,T=45), set(L=3√3,T=60), set(L=√3,T=30), set(L=√3,T=45), set(L=√3,T=60)}
  ```

- **pole C2 under R-i** [computation] — *computed: as claimed*. the families FC07 states for C2 under R-i: {'causal': ['c_H', 'c_T'], 'meas': [('c_L', 'H'), ('c_L', 'T')], 'rule': []}

  ```
  computed: {'causal': ['c_H', 'c_T'], 'meas': [('c_L', 'H'), ('c_L', 'T')], 'rule': []}; Obs(R-i) = {set(H=1,L=1), set(H=1,L=1/3√3), set(H=1,L=2), set(H=1,L=2/3√3), set(H=1,L=2√3), set(H=1,L=3), set(H=1,L=3√3), set(H=1,L=√3), set(H=2,L=1), set(H=2,L=1/3√3), set(H=2,L=2), set(H=2,L=2/3√3), set(H=2,L=2√3), set(H=2,L=3), set(H=2,L=3√3), set(H=2,L=√3), set(H=3,L=1), set(H=3,L=1/3√3), set(H=3,L=2), set(H=3,L=2/3√3), set(H=3,L=2√3), set(H=3,L=3), set(H=3,L=3√3), set(H=3,L=√3), set(L=1), set(L=1,T=30), set(L=1,T=45), set(L=1,T=60), set(L=1/3√3), set(L=1/3√3,T=30), set(L=1/3√3,T=45), set(L=1/3√3,T=60), set(L=2), set(L=2,T=30), set(L=2,T=45), set(L=2,T=60), set(L=2/3√3), set(L=2/3√3,T=30), set(L=2/3√3,T=45), set(L=2/3√3,T=60), set(L=2√3), set(L=2√3,T=30), set(L=2√3,T=45), set(L=2√3,T=60), set(L=3), set(L=3,T=30), set(L=3,T=45), set(L=3,T=60), set(L=3√3), set(L=3√3,T=30), set(L=3√3,T=45), set(L=3√3,T=60), set(L=√3), set(L=√3,T=30), set(L=√3,T=45), set(L=√3,T=60)}
  ```

- **pole C2 under R-ii** [computation] — *computed: as claimed*. the families FC07 states for C2 under R-ii: {'causal': ['c_H', 'c_L', 'c_T'], 'meas': [], 'rule': []}

  ```
  computed: {'causal': ['c_H', 'c_L', 'c_T'], 'meas': [], 'rule': []}; Obs(R-ii) = {set(H=1,L=1), set(H=1,L=1/3√3), set(H=1,L=2), set(H=1,L=2/3√3), set(H=1,L=2√3), set(H=1,L=3), set(H=1,L=3√3), set(H=1,L=√3), set(H=2,L=1), set(H=2,L=1/3√3), set(H=2,L=2), set(H=2,L=2/3√3), set(H=2,L=2√3), set(H=2,L=3), set(H=2,L=3√3), set(H=2,L=√3), set(H=3,L=1), set(H=3,L=1/3√3), set(H=3,L=2), set(H=3,L=2/3√3), set(H=3,L=2√3), set(H=3,L=3), set(H=3,L=3√3), set(H=3,L=√3), set(L=1,T=30), set(L=1,T=45), set(L=1,T=60), set(L=1/3√3,T=30), set(L=1/3√3,T=45), set(L=1/3√3,T=60), set(L=2,T=30), set(L=2,T=45), set(L=2,T=60), set(L=2/3√3,T=30), set(L=2/3√3,T=45), set(L=2/3√3,T=60), set(L=2√3,T=30), set(L=2√3,T=45), set(L=2√3,T=60), set(L=3,T=30), set(L=3,T=45), set(L=3,T=60), set(L=3√3,T=30), set(L=3√3,T=45), set(L=3√3,T=60), set(L=√3,T=30), set(L=√3,T=45), set(L=√3,T=60)}
  ```

- **pole C2 with composites (outside FC07's statement)** [computation] — *computed: as claimed*. C2* = C2 plus the composite settings that set L together with H or θ: families under both readings

  ```
  R-i: {'causal': [], 'meas': [('c_L', 'H'), ('c_L', 'T')], 'rule': ['c_H', 'c_L', 'c_T']}; R-ii: {'causal': [], 'meas': [('c_L', 'H'), ('c_L', 'T')], 'rule': ['c_H', 'c_L', 'c_T']}. Under D2.1 a composite of two settings is no setting edit (it changes two components), so it counts as an edit to the rule of each component it alters (I08) and, where it leaves the component assigning the reported port, as an observation edit (both readings). On C2* no component is causal and every component has the rule signature: FC07's results hold only on contracts without composites.
  ```

### FC08 · L127's gloss of a measurement's signature has a clause about solutions — HOLDS ON ALL MODELS TRIED

**The claim.** 'Change only the reading and the part it reports stays as it was' is a condition on relations (FC06). 'Change the part and the reading follows' is a condition on solutions: under a setting edit of m, the projection of Sol_D on the reading o changes. There are D and j reading m whose relation is constant in m (the projection on o does not follow m) and j still meets both clauses of L124.

**Rests on.** Claim's inventions: I04, I06, I07. Program's: I77, I78. **Reproduce.** `cd "/home/user/ThreadSmith/Semantics/results/S104 Round 2 - maths" && python3 -m model.run --claim FC08 --scale 4 --time-cap 45`

- **a measurement whose reading does not follow** [there is] — *witness found*. there are D and j reading m with Meas_C(j,m) (both clauses) whose reading's projection does not follow a setting of m
  - Searched: sizes ports=1 dom≤1 comps=1 |B|=1 edits=0 … ports=3 dom≤2 comps=3 |B|=2 edits=2 (108 sizes, 240 draws each); families: G-surg; seed 104081; 18019 models tried; first found at size ports=2 dom≤2 comps=2 |B|=1 edits=2.

  ```
  Under R-i, h_p0 is a measurement of p1 on the contract of every pair (both clauses of L124 hold), and no setting edit of p1 changes the projection of Sol on the reading p0: 'change the part and the reading follows' fails.
  organization D
    ports: p0 ∈ {0,1}; p1 ∈ {0,1}
    components: h_p0 on (p0,p1); h_p1 on (p0,p1)
    boundaries B = {b0}; edits A = {1,[p1=1],[alt:h_p0],[p1=1,alt:h_p0]}
    composition (other than with 1): [p1=1]·[p1=1]=[p1=1], [p1=1]·[alt:h_p0]=[p1=1,alt:h_p0], [p1=1]·[p1=1,alt:h_p0]=[p1=1,alt:h_p0], [alt:h_p0]·[p1=1]=[p1=1,alt:h_p0], [alt:h_p0]·[alt:h_p0]=[alt:h_p0], [alt:h_p0]·[p1=1,alt:h_p0]=[p1=1,alt:h_p0], [p1=1,alt:h_p0]·[p1=1]=[p1=1,alt:h_p0], [p1=1,alt:h_p0]·[alt:h_p0]=[p1=1,alt:h_p0], [p1=1,alt:h_p0]·[p1=1,alt:h_p0]=[p1=1,alt:h_p0]
    L_h_p0(1,b0) = {(1,0) (1,1)}
    L_h_p0([p1=1],b0) = {(1,0) (1,1)}
    L_h_p0([alt:h_p0],b0) = full
    L_h_p0([p1=1,alt:h_p0],b0) = full
    L_h_p1(1,b0) = {(0,1) (1,0)}
    L_h_p1([p1=1],b0) = {(0,1) (1,1)}
    L_h_p1([alt:h_p0],b0) = {(0,1) (1,0)}
    L_h_p1([p1=1,alt:h_p0],b0) = {(0,1) (1,1)}
  ```

### FC09 · Four names, three families: a constitutive status is a rule application — HOLDS ON ALL MODELS TRIED

**The claim.** The bullets define three predicates Causal_C, Meas_C, Rule_C. L347 gives a constitutive rule the signature of Rule_C (Z read as the world's ports, C_r as the rule, I08). So 'a rule' and 'a constitutive status' both map to Rule_C.

**Rests on.** Claim's inventions: I08. Program's: I78. **Reproduce.** `cd "/home/user/ThreadSmith/Semantics/results/S104 Round 2 - maths" && python3 -m model.run --claim FC09 --scale 4 --time-cap 45`

- **L347's rule relation has Rule_C's signature** [computation] — *computed: as claimed*. Rule_C(c_r) on the contract of every pair (I08)

  ```
  families: {'R-i': {'causal': ['h_z'], 'meas': [('c_r', 'z')], 'rule': ['c_r']}, 'R-ii': {'causal': ['h_z'], 'meas': [('c_r', 'z')], 'rule': ['c_r']}}. So 'a constitutive status' (L347) and 'a rule' (L125) both map to Rule_C. Under both readings c_r also has the signature of a measurement of z (the edits setting s and the rule edit alter c_r and leave h_z): the families overlap.
  ```

### FC10 · L57 against the new L123 — HOLDS ON ALL MODELS TRIED

**The claim.** Rule_C(j) ⇒ (variable under rule edits ∧ invariant under world interventions), which is L57's rule sentence; Causal_C(j) ⇒ changes under intervention on its output, which is L57's cause sentence. L57 names no condition on observation edits; the bullet's second clause adds to L57 and does not conflict with it. The clause round 1 removed ('and under replacement of the component') has no counterpart in L57.

**Rests on.** Claim's inventions: I08, I09. Program's: I77, I78. **Reproduce.** `cd "/home/user/ThreadSmith/Semantics/results/S104 Round 2 - maths" && python3 -m model.run --claim FC10 --scale 4 --time-cap 45`

- **families imply L57's clauses** [for all] — *holds on all models tried*. Rule_C ⇒ variable under rule edits ∧ invariant under world interventions; Causal_C ⇒ changes under intervention on its output
  - Searched: sizes ports=1 dom≤1 comps=1 |B|=1 edits=0 … ports=3 dom≤2 comps=3 |B|=2 edits=2 (108 sizes, 160 draws each); families: G-surg, G-free; seed 104101; 17280 models tried.

- **L57 names no condition on observation edits; the removed clause** [not tested] — *not tested*. textual comparison of L57 with L123
  - Why not: a reading of two sentences' wording, not a property of models

### FC11 · Roles are relative to A; families are relative to C — HOLDS ON ALL MODELS TRIED

**The claim.** Input(v) quantifies over A; Causal_C(asg(v)) over C ⊆ A × B. There are D, C, v with Input(v) and ¬Causal_C(asg(v)) (C holds no setting edit of v). Conversely every family predicate uses edits of A only, so no family membership needs an edit A lacks.

**Rests on.** Claim's inventions: I04, I09. Program's: I80, I92. **Reproduce.** `cd "/home/user/ThreadSmith/Semantics/results/S104 Round 2 - maths" && python3 -m model.run --claim FC11 --scale 4 --time-cap 45`

- **Input(v) without Causal_C(asg(v))** [computation] — *computed: as claimed*. there are D, C, v with Input(v) and ¬Causal_C(asg(v))

  ```
  pole, C = {(1,b1_45)}: Input(H) = True, Causal_C(c_H) = False (R-i), False (R-ii)
  ```

- **families use edits of A only** [by construction] — *holds by construction*. no family predicate needs an edit A lacks

  ```
  Roles quantifies over org.A and over the pairs of C only.
  ```

### FC12 · Invariance clauses can be vacuous; change clauses cannot — HOLDS ON ALL MODELS TRIED

**The claim.** On C = {(1,b0)} no component is in any family (each family needs a 'changes' or 'variable' clause witnessed by a pair of C, I09). On a C with no Obs edit, Causal's second clause holds vacuously; with no world intervention, Rule's first clause does; with no intervention on m, Meas's first clause does.

**Rests on.** Claim's inventions: I09. Program's: I77, I78, I80. **Reproduce.** `cd "/home/user/ThreadSmith/Semantics/results/S104 Round 2 - maths" && python3 -m model.run --claim FC12 --scale 4 --time-cap 45`

- **the baseline contract puts no component in any family** [for all] — *holds on all models tried*. C = {(1,b0)} ⇒ no component in any family, both readings
  - Searched: sizes ports=1 dom≤1 comps=1 |B|=1 edits=0 … ports=3 dom≤3 comps=3 |B|=2 edits=2 (162 sizes, 160 draws each); families: G-surg, G-free; seed 104121; 25920 models tried.

### FC13 · The families are patterns in (K), not additional data — HOLDS ON ALL MODELS TRIED

**The claim.** Causal_C(j), Meas_C(j,m) and Rule_C(j) are functions of D and C alone: of sig_C(j) and of how each edit of C is classed (a setting edit of a port, an observation edit, a rule edit, or none), a classification I04, I06 and I08 read off (A, L). Under I04's alternative (a), a declared asg, the classification needs data beyond D and C.

**Rests on.** Claim's inventions: I04, I06, I08, I09. Program's: I70, I77, I78. **Reproduce.** `cd "/home/user/ThreadSmith/Semantics/results/S104 Round 2 - maths" && python3 -m model.run --claim FC13 --scale 4 --time-cap 45`

- **families are carried by renamings** [for all] — *holds on all models tried*. the family predicates, computed from (D, C) alone, are carried along by every renaming of ports, components, edits and boundaries
  - Searched: sizes ports=1 dom≤1 comps=1 |B|=1 edits=0 … ports=3 dom≤2 comps=3 |B|=2 edits=2 (108 sizes, 160 draws each); families: G-surg, G-free; seed 104131; 17280 models tried.

- **no further data** [by construction] — *holds by construction*. Causal_C, Meas_C, Rule_C take (D, C) and a reading of observation edits, nothing else

  ```
  Roles(org) and families(C, reading): no declared asg, no declared measured port.
  ```

### FC14 · No definition asks whether a component 'is' a cause — HOLDS ON ALL MODELS TRIED

**The claim.** Syntactic: no definition of the formal core takes a predicate 'is a cause' as an argument; the component-level predicates are sig_C, ~_C and the family predicates, each a function of D and C (FC13).

**Rests on.** Claim's inventions: none. Program's: none. **Reproduce.** `cd "/home/user/ThreadSmith/Semantics/results/S104 Round 2 - maths" && python3 -m model.run --claim FC14 --scale 4 --time-cap 45`

- **syntactic scan** [computation] — *computed: as claimed*. no definition of the formal core takes a predicate 'is a cause'

  ```
  definition lines of formal core.md matching 'is a cause' / 'IsCause' / 'Cause(': 0
  ```

### FC15 · τ[C] is a contract of the candidate's organization — HOLDS ON ALL MODELS TRIED

**The claim.** If τ(1) = 1 and τ, σ map into A_E, B_E, then τ[C] ⊆ A_E × B_E and (1, σ(b0)) ∈ τ[C]: τ[C] is a contract of E with baseline σ(b0), as far as a contract is a set of pairs holding the baseline.

**Rests on.** Claim's inventions: I12, I18. Program's: I77, I78, I81. **Reproduce.** `cd "/home/user/ThreadSmith/Semantics/results/S104 Round 2 - maths" && python3 -m model.run --claim FC15 --scale 4 --time-cap 45`

- **τ[C] holds (1, σ(b0))** [for all] — *holds on all models tried*. τ(1) = 1 ⇒ τ[C] ⊆ A_E × B_E and (1, σ(b0)) ∈ τ[C]
  - Searched: sizes ports=1 dom≤1 comps=1 |B|=1 edits=0 … ports=3 dom≤2 comps=3 |B|=2 edits=2 (108 sizes, 160 draws each); families: G-surg, G-free; seed 104151; 17280 models tried.

### FC16 · Reading a candidate's components through the transport agrees with (K) on τ[C] — HOLDS ON ALL MODELS TRIED

**The claim.** For k, k' in one candidate E and a footprint bijection β: the signatures of k and k' read on C through t coincide under β ⟺ k ~_{τ[C]} k' under β by (K), since (a,b) ↦ (τ(a),σ(b)) maps C onto τ[C].

**Rests on.** Claim's inventions: I10, I12. Program's: I77, I78, I81. **Reproduce.** `cd "/home/user/ThreadSmith/Semantics/results/S104 Round 2 - maths" && python3 -m model.run --claim FC16 --scale 4 --time-cap 45`

- **reading through t agrees with (K) on τ[C]** [for all] — *holds on all models tried*. k, k' coincide on C through t ⟺ k ~_{τ[C]} k'
  - Searched: sizes ports=1 dom≤1 comps=1 |B|=1 edits=0 … ports=3 dom≤2 comps=3 |B|=2 edits=2 (108 sizes, 160 draws each); families: G-surg, G-free; seed 104161; 17280 models tried.

### FC17 · Argument 1: (F1) makes each commitment's signature its counterpart's — HOLDS ON ALL MODELS TRIED

**The claim.** F1_C(ℰ) ⇒ ∀k∈Γ ∀(a,b)∈C: L_k(τ(a),σ(b)) = proj^λ_{V_k} Sol_{λ(k)}(a,b); that is, the signature of k read on C through t equals sig_C(λ(k),θ_k) (I13) as functions on C.

**Rests on.** Claim's inventions: I12, I13, I14, I15. Program's: I77, I78, I81. **Reproduce.** `cd "/home/user/ThreadSmith/Semantics/results/S104 Round 2 - maths" && python3 -m model.run --claim FC17 --scale 4 --time-cap 45`

- **(F1) makes each commitment's signature its counterpart's** [for all] — *holds on all models tried*. F1_C ⇒ sig of k through t = sig_C(λ(k)) on C
  - Searched: sizes ports=1 dom≤1 comps=1 |B|=1 edits=0 … ports=3 dom≤2 comps=3 |B|=2 edits=2 (108 sizes, 160 draws each); families: G-surg, G-free; seed 104171; 17280 models tried; 10682 of them meeting the claim's hypothesis.

### FC18 · Argument 1's Consequence: a same-kind condition adds nothing; no third case — COUNTEREXAMPLE FOUND

**The claim.** SameKind_C(ℰ) := for every k in Γ, the signature of k read through t and sig_C(λ(k),θ_k) coincide under a footprint bijection (I10). Claim: F1_C(ℰ) ⇒ SameKind_C(ℰ), so Acc(ℰ) ⟺ Acc(ℰ) ∧ SameKind_C(ℰ) for every ℰ and C.

**Rests on.** Claim's inventions: I10, I13, I14. Program's: I77, I78, I81, I94. **Reproduce.** `cd "/home/user/ThreadSmith/Semantics/results/S104 Round 2 - maths" && python3 -m model.run --claim FC18 --scale 4 --time-cap 45`

- **D4.4's reading (counterpart carried to V_k)** [for all] — *holds on all models tried*. F1_C ⇒ SameKind_C, the counterpart's signature read on V_k (D4.4)
  - Searched: sizes ports=1 dom≤1 comps=1 |B|=1 edits=0 … ports=3 dom≤2 comps=3 |B|=2 edits=2 (108 sizes, 160 draws each); families: G-surg, G-free; seed 104181; 17280 models tried; 10513 of them meeting the claim's hypothesis.

- **untranslated reading (I94)** [for all] — *counterexample found*. F1_C ⇒ SameKind_C, the counterpart read on its own D ports with D's domains
  - Searched: sizes ports=1 dom≤1 comps=1 |B|=1 edits=0 … ports=3 dom≤2 comps=3 |B|=2 edits=2 (108 sizes, 240 draws each); families: G-surg, G-free; seed 104182; 972 models tried; 660 of them meeting the claim's hypothesis; first found at size ports=1 dom≤2 comps=1 |B|=1 edits=0.
  - The counterexample is written out above, under Counterexamples.

### FC19 · (F1) and (F2) do different work — HOLDS ON ALL MODELS TRIED

**The claim.** (a) There is ℰ with F2_C ∧ A_C ∧ ¬F1_C. (b) There is ℰ with F1_C ∧ ¬F2_C: two commitments each matching its counterpart, whose counterparts share a port of D that E's two components do not share.

**Rests on.** Claim's inventions: I14, I15. Program's: I77, I78, I81, I101. **Reproduce.** `cd "/home/user/ThreadSmith/Semantics/results/S104 Round 2 - maths" && python3 -m model.run --claim FC19 --scale 4 --time-cap 45`

- **(a) F2 ∧ A ∧ ¬F1** [there is] — *witness found*. there is ℰ with F2_C ∧ A_C ∧ ¬F1_C
  - Searched: sizes ports=1 dom≤1 comps=1 |B|=1 edits=0 … ports=3 dom≤2 comps=3 |B|=2 edits=2 (108 sizes, 800 draws each); families: G-surg, G-free; proper models only: domains ≥ 2, every port in a footprint, Sol_D(1,b) ≠ ∅, Γ ≠ ∅; seed 104191; 70 models tried; first found at size ports=1 dom≤2 comps=1 |B|=1 edits=0.

  ```
  F2 ∧ A ∧ ¬F1
  question p: target D, b0 = b0, query Q_w (reads the designated port) designating p0, C = {(1,b0)}
  organization D
    ports: p0 ∈ {0,1}
    components: h_p0 on (p0)
    boundaries B = {b0}; edits A = {1}
    L_h_p0(1,b0) = {(1)}
  candidate ℰ for p: Γ = {k0}, δ_E = p0
    π: p0 := id(p0)
    τ: 1↦1; σ: b0↦b0
    λ(k0) = ({h_p0}, p0:=id(p0))
  organization E_ℰ
    ports: p0 ∈ {0,1}
    components: k0 on (p0); bg on (p0)
    boundaries B = {b0}; edits A = {1}
    L_k0(1,b0) = full
    L_bg(1,b0) = {(1)}
  ```

- **(b) F1 ∧ ¬F2** [there is] — *witness found*. there is ℰ with two or more commitments, no background component, and F1_C ∧ ¬F2_C
  - Searched: sizes ports=1 dom≤1 comps=1 |B|=1 edits=0 … ports=3 dom≤2 comps=3 |B|=2 edits=2 (108 sizes, 1200 draws each); families: G-surg, G-free; proper models only: domains ≥ 2, every port in a footprint, Sol_D(1,b) ≠ ∅, |Γ| ≥ 2; seed 104192; 3799 models tried; first found at size ports=1 dom≤2 comps=3 |B|=1 edits=0.

  ```
  F1 ∧ ¬F2 (F2eq False, Hom True)
  question p: target D, b0 = b0, query Q_w (reads the designated port) designating p0, C = {(1,b0)}
  organization D
    ports: p0 ∈ {0,1}
    components: h_p0 on (p0); k0 on (p0); k1 on (p0)
    boundaries B = {b0}; edits A = {1}
    L_h_p0(1,b0) = {(1)}
    L_k0(1,b0) = full
    L_k1(1,b0) = full
  candidate ℰ for p: Γ = {k0,k1}, δ_E = p0
    π: p0 := id(p0)
    τ: 1↦1; σ: b0↦b0
    λ(k0) = ({k1}, p0:=id(p0))
    λ(k1) = ({k0}, p0:=id(p0))
  organization E_ℰ
    ports: p0 ∈ {0,1}
    components: k0 on (p0); k1 on (p0)
    boundaries B = {b0}; edits A = {1}
    L_k0(1,b0) = full
    L_k1(1,b0) = full
  ```

### FC20 · When (F2) at a pair gives (A) at that pair (violation in either extent) — COUNTEREXAMPLE FOUND

**The claim.** If Q reads a port w of the target, δ_E designates a port w' of E, and π(z)_{w'} = κ(z_w) for every z (π acts on the designated port as a value map κ), then the valuation equation of (F2) at (a,b) gives Ans_E(τ(a),σ(b)) = κ(Ans_p(a,b)); with κ the identity this is (A) at (a,b). Without that condition on π, (F2) at a pair does not give (A) there. Violation and Violation⁺ (I50) coincide exactly where it does.

**Rests on.** Claim's inventions: I16, I20, I21, I49, I50. Program's: I77, I78, I81. **Reproduce.** `cd "/home/user/ThreadSmith/Semantics/results/S104 Round 2 - maths" && python3 -m model.run --claim FC20 --scale 4 --time-cap 45`

- **any value map κ** [for all] — *counterexample found*. F2eq at (a,b) ∧ π acts on the designated port as κ ⇒ Ans_E(τa,σb) = κ(Ans_p(a,b)) (κ(⊥) = ⊥)
  - Searched: sizes ports=1 dom≤1 comps=1 |B|=1 edits=0 … ports=3 dom≤2 comps=3 |B|=2 edits=2 (108 sizes, 600 draws each); families: G-surg, G-free; seed 104201; 2404 models tried; 1849 of them meeting the claim's hypothesis; first found at size ports=1 dom≤2 comps=1 |B|=1 edits=0.
  - The counterexample is written out above, under Counterexamples.

- **κ the identity** [for all] — *holds on all models tried*. F2eq at (a,b) ∧ π the identity on the designated port ⇒ (A) at (a,b)
  - Searched: sizes ports=1 dom≤1 comps=1 |B|=1 edits=0 … ports=3 dom≤2 comps=3 |B|=2 edits=2 (108 sizes, 400 draws each); families: G-surg, G-free; seed 104202; 43200 models tried; 30991 of them meeting the claim's hypothesis.

- **Violation and Violation⁺ coincide where κ = id** [for all] — *holds on all models tried*. κ the identity ⇒ Viol(t;a,b) ⟺ Viol⁺(t;a,b)
  - Searched: sizes ports=1 dom≤1 comps=1 |B|=1 edits=0 … ports=3 dom≤2 comps=3 |B|=2 edits=2 (108 sizes, 240 draws each); families: G-surg, G-free; seed 104203; 25920 models tried; 24253 of them meeting the claim's hypothesis.

### FC21 · A contract of relabelings admits no candidate meeting (A) and non-circular dependence — HOLDS ON ALL MODELS TRIED

**The claim.** (a) If every edit of C is a relabeling for p (I26), then for every ℰ with A_C(ℰ) and τ(1) = 1: ¬NC2(ℰ). (b) Without (A) the implication can fail: a candidate whose own answers vary over τ[C] can meet NC2 on a contract of relabelings. (c) 'Excluding every change under which the active commitments could matter to Q' is ¬NC2 for every candidate, by NC2's definition.

**Rests on.** Claim's inventions: I21, I22, I26. Program's: I77, I78, I81, I85, I101. **Reproduce.** `cd "/home/user/ThreadSmith/Semantics/results/S104 Round 2 - maths" && python3 -m model.run --claim FC21 --scale 4 --time-cap 45`

- **(a) relabelings and (A) exclude NC2** [for all] — *holds on all models tried*. every edit of C a relabeling ∧ A_C ∧ τ(1) = 1 ⇒ ¬NC2
  - Searched: sizes ports=1 dom≤1 comps=1 |B|=1 edits=0 … ports=3 dom≤2 comps=3 |B|=2 edits=2 (108 sizes, 240 draws each); families: G-surg, G-free; seed 104211; 14807 models tried; 10239 of them meeting the claim's hypothesis.

- **(b) without (A)** [there is] — *witness found*. a candidate whose answers vary over τ[C] meets NC2 on a contract of relabelings
  - Searched: sizes ports=1 dom≤1 comps=1 |B|=1 edits=0 … ports=3 dom≤2 comps=3 |B|=2 edits=2 (108 sizes, 800 draws each); families: G-surg, G-free; proper models only; seed 104212; 241 models tried; first found at size ports=1 dom≤2 comps=1 |B|=1 edits=1.

  ```
  On a contract of relabelings (every pair of C has the baseline answer 1), a candidate without (A) meets NC2 (witness (('[p0=1]', 'b0'), ['k0'])).
  question p: target D, b0 = b0, query Q_w (reads the designated port) designating p0, C = {(1,b0), ([p0=1],b0)}
  organization D
    ports: p0 ∈ {0,1}
    components: h_p0 on (p0)
    boundaries B = {b0}; edits A = {1,[p0=1]}
    composition (other than with 1): [p0=1]·[p0=1]=[p0=1]
    L_h_p0(1,b0) = {(1)}
    L_h_p0([p0=1],b0) = {(1)}
  candidate ℰ for p: Γ = {k0}, δ_E = p0
    π: p0 := id(p0)
    τ: 1↦1, [p0=1]↦[p0=1]; σ: b0↦b0
    λ(k0) = ({h_p0}, p0:=id(p0))
  organization E_ℰ
    ports: p0 ∈ {0,1}
    components: k0 on (p0)
    boundaries B = {b0}; edits A = {1,[p0=1]}
    composition (other than with 1): [p0=1]·[p0=1]=[p0=1]
    L_k0(1,b0) = {(1)}
    L_k0([p0=1],b0) = {}
  ```

- **(c) 'excluding every change under which the commitments could matter'** [by construction] — *holds by construction*. is ¬NC2 for every candidate

  ```
  read as the definition of NC2 negated; nothing to search
  ```

### FC22 · The baseline alone gives no contrast — HOLDS ON ALL MODELS TRIED

**The claim.** If C = {(1,b0)} and τ(1) = 1 then ¬NC2(ℰ) for every ℰ: the only pair compares the baseline with itself, and neither disjunct of the contrast holds.

**Rests on.** Claim's inventions: I21, I22. Program's: I77, I78, I81. **Reproduce.** `cd "/home/user/ThreadSmith/Semantics/results/S104 Round 2 - maths" && python3 -m model.run --claim FC22 --scale 4 --time-cap 45`

- **the baseline alone gives no contrast** [for all] — *holds on all models tried*. C = {(1,b0)} ∧ τ(1) = 1 ⇒ ¬NC2
  - Searched: sizes ports=1 dom≤1 comps=1 |B|=1 edits=0 … ports=3 dom≤2 comps=3 |B|=2 edits=2 (108 sizes, 240 draws each); families: G-surg, G-free; seed 104221; 25920 models tried.

### FC23 · 'p because p' fails non-circular dependence through NC1 only — COUNTEREXAMPLE FOUND

**The claim.** Let E_lk have Γ = {k}, L_k(τ(a),σ(b)) the answer slot for Ans_p(a,b) (I24), and no other component constraining the answer ports. (a) NC1 fails for E_lk. (b) If Ans_p is not constant on C, NC2 holds for E_lk with G = {k}: after deleting k the answer is ⊥ at both points, so an answer E_lk determined is no longer determined. So E_lk fails non-circular dependence through NC1 only; under I24's alternative (a), NC2 alone, E_lk meets non-circular dependence.

**Rests on.** Claim's inventions: I21, I22, I24, I25. Program's: I77, I78, I79, I81, I82, I83. **Reproduce.** `cd "/home/user/ThreadSmith/Semantics/results/S104 Round 2 - maths" && python3 -m model.run --claim FC23 --scale 4 --time-cap 45`

- **(a) NC1 fails for the lookup** [for all] — *holds on all models tried*. Ans_p determined on C ⇒ some component of E_lk is an answer slot
  - Searched: sizes ports=1 dom≤1 comps=1 |B|=1 edits=0 … ports=3 dom≤2 comps=3 |B|=2 edits=2 (108 sizes, 240 draws each); families: G-surg, G-free; seed 104231; 11748 models tried.

- **(b) as stated** [for all] — *counterexample found*. Ans_p not constant on C ⇒ NC2(E_lk) with G = {k}
  - Searched: sizes ports=1 dom≤1 comps=1 |B|=1 edits=0 … ports=3 dom≤2 comps=3 |B|=2 edits=2 (108 sizes, 320 draws each); families: G-surg, G-free; seed 104232; 6308 models tried; 105 of them meeting the claim's hypothesis; first found at size ports=2 dom≤2 comps=1 |B|=1 edits=1.
  - The counterexample is written out above, under Counterexamples.

- **(b) with satisfiable background** [for all] — *holds on all models tried*. Ans_p not constant on C ∧ Sol_E(τa,σb) ≠ ∅ on C ⇒ NC2(E_lk)
  - Searched: sizes ports=1 dom≤1 comps=1 |B|=1 edits=0 … ports=3 dom≤2 comps=3 |B|=2 edits=2 (108 sizes, 320 draws each); families: G-surg, G-free; seed 104233; 15666 models tried; 431 of them meeting the claim's hypothesis.

### FC24 · L273's second sentence uses 'account' for a candidate — HOLDS ON ALL MODELS TRIED

**The claim.** No ℰ has Acc(ℰ) ∧ ¬NonCircular(ℰ), by (E); so 'an account' in this sentence is a candidate offered as an account (L69's 'a theory in error offered as an answer is an explanatory candidate'). Adding to Γ a component answering another question leaves the answer slot in place, so NC1 still fails (I24); FC23's remark on NC2 applies unchanged.

**Rests on.** Claim's inventions: I24. Program's: I77, I78, I79, I81, I83. **Reproduce.** `cd "/home/user/ThreadSmith/Semantics/results/S104 Round 2 - maths" && python3 -m model.run --claim FC24 --scale 4 --time-cap 45`

- **packaging another dependence leaves the slot** [for all] — *holds on all models tried*. E_lk with an added commitment still fails NC1
  - Searched: sizes ports=1 dom≤1 comps=1 |B|=1 edits=0 … ports=3 dom≤2 comps=3 |B|=2 edits=2 (108 sizes, 240 draws each); families: G-surg, G-free; seed 104241; 3714 models tried.

- **L273's 'an account' names a candidate** [not tested] — *not tested*. reading of the word 'account' at L273
  - Why not: a reading of wording

### FC25 · Tables: a fixed table fails (F1) where the projection moves; an encoding table meets it — COUNTEREXAMPLE FOUND

**The claim.** (a) E_tab (I32): F1 at (a,b) ⟺ the projection of Sol_D(a,b) on the table's ports equals that of Sol_D(1,b0). So E_tab fails (F1) under C exactly when C holds a pair at which that projection moves; a setting edit that leaves it unchanged (a port set to its baseline value, or a port the table's ports do not depend on) does not make it fail. (b) E_enc, with L_k(τ(a),σ(b)) := that projection at (a,b), meets (F1) on every C.

**Rests on.** Claim's inventions: I03, I04, I14, I32. Program's: I77, I78, I80, I101. **Reproduce.** `cd "/home/user/ThreadSmith/Semantics/results/S104 Round 2 - maths" && python3 -m model.run --claim FC25 --scale 4 --time-cap 45`

- **(a) E_tab's F1** [for all] — *holds on all models tried*. F1 at (a,b) for E_tab ⟺ the projection of Sol_D on its ports is that at (1,b0)
  - Searched: sizes ports=1 dom≤1 comps=1 |B|=1 edits=0 … ports=3 dom≤2 comps=3 |B|=2 edits=2 (108 sizes, 160 draws each); families: G-surg; targets whose every port lies in a footprint; seed 104251; 14845 models tried.

- **(a) a setting edit that leaves the table faithful** [there is] — *witness found*. there is a contract holding a setting edit (of a port with two values or more) on which E_tab meets (F1)
  - Searched: sizes ports=1 dom≤1 comps=1 |B|=1 edits=0 … ports=3 dom≤2 comps=3 |B|=2 edits=2 (108 sizes, 800 draws each); families: G-surg; proper models only; seed 104252; 8520 models tried; first found at size ports=1 dom≤2 comps=1 |B|=1 edits=1.

  ```
  L269 says a table of observed answers 'fails (F1) under any contract containing' an intervention. Here C contains the setting edits {([p0=0],b0)} and E_tab meets (F1) on C: none of them moves the projection of Sol_D on the table's ports.
  question p: target D, b0 = b0, query Q_w (reads the designated port) designating p0, C = {(1,b0), ([p0=0],b0)}
  organization D
    ports: p0 ∈ {0,1}
    components: h_p0 on (p0)
    boundaries B = {b0}; edits A = {1,[p0=0]}
    composition (other than with 1): [p0=0]·[p0=0]=[p0=0]
    L_h_p0(1,b0) = {(0)}
    L_h_p0([p0=0],b0) = {(0)}
  candidate E_tab for p: Γ = {tab}, δ_E = p0
    π: p0 := id(p0)
    τ: 1↦1, [p0=0]↦[p0=0]; σ: b0↦b0
    λ(tab) = ({h_p0}, p0:=id(p0))
  organization E_tab
    ports: p0 ∈ {0,1}
    components: tab on (p0)
    boundaries B = {b0}; edits A = {1,[p0=0]}
    composition (other than with 1): [p0=0]·[p0=0]=[p0=0]
    L_tab(1,b0) = {(0)}
    L_tab([p0=0],b0) = {(0)}
  ```

- **(b) E_enc meets F1** [for all] — *holds on all models tried*. E_enc meets (F1) on every C
  - Searched: sizes ports=1 dom≤1 comps=1 |B|=1 edits=0 … ports=3 dom≤2 comps=3 |B|=2 edits=2 (108 sizes, 160 draws each); families: G-surg; targets whose every port lies in a footprint; seed 104253; 14855 models tried.

- **(b) with a port of D in no footprint** [for all] — *counterexample found*. E_enc meets (F1) on every C, D having a port in no footprint
  - Searched: sizes ports=1 dom≤1 comps=1 |B|=1 edits=0 … ports=3 dom≤2 comps=3 |B|=2 edits=2 (108 sizes, 160 draws each); families: G-surg; seed 104254; 1 models tried; first found at size ports=2 dom≤1 comps=1 |B|=1 edits=0.
  - The counterexample is written out above, under Counterexamples.

### FC26 · The pole: the forward organization meets (E) on the production contract — HOLDS ON ALL MODELS TRIED

**The claim.** With I65: E_fwd = D_pole with the identity transport and Γ = {c_H, c_θ, c_L} meets (F1), (F2), (A), NC1, NC2 and non-vacuity (with a scope statement) on C1 = settings of H and θ, and on C2 = C1 plus settings of L; Q reads L.

**Rests on.** Claim's inventions: I04, I20, I21, I24, I27, I65. Program's: I79, I85, I92. **Reproduce.** `cd "/home/user/ThreadSmith/Semantics/results/S104 Round 2 - maths" && python3 -m model.run --claim FC26 --scale 4 --time-cap 45`

- **forward organization on C1** [computation] — *computed: as claimed*. E_fwd meets (F1), (F2), (A), NC1, NC2 and non-vacuity on C1

  ```
  conjuncts: {'translates C': True, 'F1': True, 'F2eq': True, 'Hom': True, 'F2': True, 'A': True, 'NC1': True, 'NC2': True, 'NonVacuous': True}
  ```

- **forward organization on C2** [computation] — *computed: as claimed*. E_fwd meets (F1), (F2), (A), NC1, NC2 and non-vacuity on C2

  ```
  conjuncts: {'translates C': True, 'F1': True, 'F2eq': True, 'Hom': True, 'F2': True, 'A': True, 'NC1': True, 'NC2': True, 'NonVacuous': True}
  ```

- **a contract whose only non-baseline edits set L** [look] — *look: not as expected*. the look: on it c_L is an answer slot and NC1 fails for the forward organization

  ```
  conjuncts on C3 = the baseline plus the settings of L: {'translates C': True, 'F1': True, 'F2eq': True, 'Hom': True, 'F2': True, 'A': True, 'NC1': True, 'NC2': True, 'NonVacuous': True}. NC1 holds: c_L is no answer slot at the baseline pair, and D6.3 asks for a slot at every pair of C. NC2 holds too (witness (('set(L=1/3√3)', 'b1_45'), ['c_H'])): deleting c_L frees L at a setting pair as well, since a deleted component imposes the full relation under every edit (D1.3), so the answer determined there is lost. The forward organization meets (E) on C3.
  ```

### FC27 · The pole: the reversed calculation fails (F2) on the production contract — HOLDS ON ALL MODELS TRIED

**The claim.** E_rev: components c'_L (L = the observed value, from the boundary), c'_θ, c'_H (H = L tan θ); τ(set H := h) = set H := h. At (set H := h, b) with h ≠ u_H: π[Sol_D] has L = h cot θ, Sol_E_rev has L = u_H cot θ. (F2) fails there.

**Rests on.** Claim's inventions: I04, I65. Program's: I92. **Reproduce.** `cd "/home/user/ThreadSmith/Semantics/results/S104 Round 2 - maths" && python3 -m model.run --claim FC27 --scale 4 --time-cap 45`

- **the reversed calculation fails (F2) at setH := h ≠ u_H** [computation] — *computed: as claimed*. F2eq fails for E_rev at (set H := h, b0) with h ≠ u_H

  ```
  set(H=2): F2eq False, L in π[Sol_D] [2], L in Sol_E [1]; set(H=3): F2eq False, L in π[Sol_D] [3], L in Sol_E [1]. Account on C1: {'translates C': True, 'F1': False, 'F2eq': False, 'Hom': True, 'F2': False, 'A': False, 'NC1': True, 'NC2': True, 'NonVacuous': True}.
  ```

### FC28 · The pole: the reversed calculation meets (F1), (F2), (A) on the identification contract — HOLDS ON ALL MODELS TRIED

**The claim.** On I65's identification contract (boundaries varying u_H; Q the fibre {H : H cot θ = observed L}), E_rev with τ the identity and σ(b) the observed L meets (F1), (F2) and (A).

**Rests on.** Claim's inventions: I20, I65. Program's: I92. **Reproduce.** `cd "/home/user/ThreadSmith/Semantics/results/S104 Round 2 - maths" && python3 -m model.run --claim FC28 --scale 4 --time-cap 45`

- **identification contract: boundaries varying u_H** [computation] — *computed: as claimed*. E_rev with τ, σ the identity meets (F1), (F2), (A)

  ```
  {'F1': True, 'F2': True, 'A': True}; answers (target, E_rev): {'b1_45': ([1], [1]), 'b2_45': ([2], [2]), 'b3_45': ([3], [3])}
  ```

- **with edits that set L (replacing c_L)** [look] — *look: not as expected*. the look: D's fibre over the set value is every H, and (A) fails for E_rev

  ```
  {'F1': False, 'F2': False, 'A': False}. Rows: set(L=1): target fibre [1], E_rev [1], F1 False, F2eq True; set(L=1/3√3): target fibre [], E_rev ⊥, F1 False, F2eq False; set(L=2): target fibre [2], E_rev [2], F1 False, F2eq False; set(L=2/3√3): target fibre [], E_rev ⊥, F1 False, F2eq False; set(L=2√3): target fibre [], E_rev ⊥, F1 False, F2eq False; set(L=3): target fibre [3], E_rev [3], F1 False, F2eq False; set(L=3√3): target fibre [], E_rev ⊥, F1 False, F2eq False; set(L=√3): target fibre [], E_rev ⊥, F1 False, F2eq False. With this program's fibre query (the fibre over the single value of (θ, L) in Sol, I92) the target's fibre at a setting of L is {l·tan θ} ∩ X_H, not every H. (A) fails where that set is empty: E_rev, whose own c'_H still imposes H = L tan θ, then has no solution and answers ⊥, while the target answers the empty fibre. (F1) and (F2) fail at every setting of L: E_rev's c'_H is not replaced by the setting, D's c_L is.
  ```

### FC29 · A contrast no admitted edit realizes witnesses nothing — HOLDS ON ALL MODELS TRIED

**The claim.** NC2 quantifies over pairs of C ⊆ A_D × B_D; a contrast of E at a pair of E that is the image of no pair of C witnesses nothing. If every contrast of E lies off τ[C], then ¬NC2.

**Rests on.** Claim's inventions: I12. Program's: I77, I78, I81. **Reproduce.** `cd "/home/user/ThreadSmith/Semantics/results/S104 Round 2 - maths" && python3 -m model.run --claim FC29 --scale 4 --time-cap 45`

- **NC2's contrast lies on τ[C]** [for all] — *holds on all models tried*. NC2 ⇒ a contrast at some (τa,σb) with (a,b) ∈ C
  - Searched: sizes ports=1 dom≤1 comps=1 |B|=1 edits=0 … ports=3 dom≤2 comps=3 |B|=2 edits=2 (108 sizes, 160 draws each); families: G-surg, G-free; seed 104291; 17280 models tried; 1722 of them meeting the claim's hypothesis.

### FC30 · (E) takes no assessor, history, provenance or wording — HOLDS ON ALL MODELS TRIED

**The claim.** Acc(ℰ) is a function of (D, C, b0, Q, δ, E, t, Γ, Σ, ℓ) only (Σ the stated scope, I27; ℓ the grain, I28); it takes no assessor, no Accepted_j, no history and no provenance. Faithful_C(t) is a function of (D, E, t, C). Candidates alike in these arguments have the same Acc value, whatever else differs.

**Rests on.** Claim's inventions: I20, I27, I28. Program's: none. **Reproduce.** `cd "/home/user/ThreadSmith/Semantics/results/S104 Round 2 - maths" && python3 -m model.run --claim FC30 --scale 4 --time-cap 45`

- **Acc takes no assessor, history or provenance** [by construction] — *holds by construction*. Acc is a function of (D, C, b0, Q, δ, E, t, Γ, Σ, ℓ)

  ```
  core.account(cand) reads cand.E, cand.p (D, C, b0, Q, δ_D, Σ), cand.pi/tau/sigma/lam, cand.Gamma, cand.deltaE only; the model has one grain.
  ```

### FC31 · 'The four conditions', five conjuncts, and L520's three sources — NOT TESTED

**The claim.** (E) has five conjuncts; Part V has four headed conditions: Component fidelity = (F1) ∧ (F2), Question fidelity = (A), Non-circular dependence, Non-vacuity. 'The four conditions' at L61, L231 and L536 are the four headings. L520's three sources cover the four headings exactly when 'fidelity under change' has the wide extent Fid⁺ (I49); with the narrow extent L189 defines, L520 names no source for (A).

**Rests on.** Claim's inventions: I49. Program's: none. **Reproduce.** `cd "/home/user/ThreadSmith/Semantics/results/S104 Round 2 - maths" && python3 -m model.run --claim FC31 --scale 4 --time-cap 45`

- **five conjuncts, four headings, L520's sources** [not tested] — *not tested*. counting and reading of L61, L231, L520, L536
  - Why not: a reading of wording, not a model property

### FC32 · L520 (after round 1) against L526's dependence order — NOT TESTED

**The claim.** In the formal core Acc uses (O), (Q), (K) (through F1), t, Γ, the stated scope Σ (a declared input), the grain ℓ (an index, in NC1) and the designation δ (I20). L526 gives (E) the ancestors (F1), (F2), (A) and 'those'; it names neither non-circular dependence nor non-vacuity, nor any index or declared input, among them. Test: is every argument of Acc an ancestor of (E) in L526's order?

**Rests on.** Claim's inventions: I20, I27, I28. Program's: none. **Reproduce.** `cd "/home/user/ThreadSmith/Semantics/results/S104 Round 2 - maths" && python3 -m model.run --claim FC32 --scale 4 --time-cap 45`

- **Acc's arguments against L526's order** [not tested] — *not tested*. is every argument of Acc an ancestor of (E) in L526's order?
  - Why not: a property of the dependence graph read from the text (S101, D18.1), not of models; the model can only list Acc's arguments (FC30)

### FC33 · 'Every conjunct is a condition on supplied relations; none inspects a label' — HOLDS ON ALL MODELS TRIED

**The claim.** (a) If E' is E with its components and ports renamed by bijections, with t, δ and Γ carried along, then Acc(ℰ') = Acc(ℰ). (b) Non-vacuity's scope clause (I27) is a condition on a declared statement, and Sol_D(1,b0) ≠ ∅ on the baseline only; NC1 is read at a grain (I28). So the first sentence holds, as written, of (F1), (F2), (A) and NC2.

**Rests on.** Claim's inventions: I24, I27, I28, I70. Program's: I70, I77, I78, I81. **Reproduce.** `cd "/home/user/ThreadSmith/Semantics/results/S104 Round 2 - maths" && python3 -m model.run --claim FC33 --scale 4 --time-cap 45`

- **(a) Acc is kept by renaming E's components and ports** [for all] — *holds on all models tried*. Acc(ℰ') = Acc(ℰ) for a renamed copy with t, δ, Γ carried along
  - Searched: sizes ports=1 dom≤1 comps=1 |B|=1 edits=0 … ports=3 dom≤2 comps=3 |B|=2 edits=2 (108 sizes, 160 draws each); families: G-surg, G-free; seed 104331; 17280 models tried.

- **(b) which conjuncts inspect a declared statement or a grain** [not tested] — *not tested*. non-vacuity's scope clause and NC1's grain
  - Why not: a reading of the conjuncts' arguments; see FC30

### FC34 · Two questions, one target: what 'an answer to one is not an answer to the other' allows — HOLDS ON ALL MODELS TRIED

**The claim.** Narrow reading (I73): there are p, p' with the same D, (C,Q) ≠ (C',Q'), and ℰ with Acc on p and not on p'. Wide reading: no ℰ has Acc on both. Test the wide reading with C' ⊊ C and the same Q: if NC2's witness pair lies in C', NC1 holds on C' and Σ' states the scope of C', a candidate meeting (E) on C meets it on C'. (NC1 can fail on C' while holding on C: a component can coincide with the answer slot on the fewer pairs of C'.) Also: Acc is neither monotone nor antitone in C.

**Rests on.** Claim's inventions: I24, I27, I73. Program's: I77, I78, I79, I81, I85, I101. **Reproduce.** `cd "/home/user/ThreadSmith/Semantics/results/S104 Round 2 - maths" && python3 -m model.run --claim FC34 --scale 4 --time-cap 45`

- **narrow reading: Acc on one question and not the other** [there is] — *witness found*. there are p, p' (same D) and ℰ with Acc on exactly one
  - Searched: sizes ports=1 dom≤1 comps=1 |B|=1 edits=0 … ports=3 dom≤2 comps=3 |B|=2 edits=2 (108 sizes, 800 draws each); families: G-surg, G-free; proper models only; seed 104341; 416 models tried; first found at size ports=1 dom≤2 comps=1 |B|=1 edits=1.

  ```
  Acc on C: True; on C' ⊆ C: False
  question p: target D, b0 = b0, query Q_w (reads the designated port) designating p0, C = {(1,b0), ([alt:h_p0],b0)}
  question p': target D, b0 = b0, query Q_w (reads the designated port) designating p0, C = {(1,b0)}
  organization D
    ports: p0 ∈ {0,1}
    components: h_p0 on (p0)
    boundaries B = {b0}; edits A = {1,[alt:h_p0]}
    composition (other than with 1): [alt:h_p0]·[alt:h_p0]=[alt:h_p0]
    L_h_p0(1,b0) = {(0)}
    L_h_p0([alt:h_p0],b0) = full
  candidate ℰ for p: Γ = {k0}, δ_E = p0
    π: p0 := id(p0)
    τ: 1↦1, [alt:h_p0]↦[alt:h_p0]; σ: b0↦b0
    λ(k0) = ({h_p0}, p0:=id(p0))
  organization E_ℰ
    ports: p0 ∈ {0,1}
    components: k0 on (p0)
    boundaries B = {b0}; edits A = {1,[alt:h_p0]}
    composition (other than with 1): [alt:h_p0]·[alt:h_p0]=[alt:h_p0]
    L_k0(1,b0) = {(0)}
    L_k0([alt:h_p0],b0) = full
  ```

- **wide reading: a candidate meeting (E) on both** [there is] — *witness found*. there are p ≠ p' with one D and ℰ with Acc on both (against the wide reading)
  - Searched: sizes ports=1 dom≤1 comps=1 |B|=1 edits=0 … ports=3 dom≤2 comps=3 |B|=2 edits=2 (108 sizes, 1200 draws each); families: G-surg, G-free; proper models only; seed 104342; 2482 models tried; first found at size ports=1 dom≤2 comps=1 |B|=1 edits=2.

  ```
  A candidate meeting (E) on two different questions with one target (C' ⊊ C): an instance against the wide reading (I73's alternative).
  question p: target D, b0 = b0, query Q_w (reads the designated port) designating p0, C = {(1,b0), ([alt:h_p0],b0), ([p0=1],b0)}
  question p': target D, b0 = b0, query Q_w (reads the designated port) designating p0, C = {(1,b0), ([alt:h_p0],b0)}
  organization D
    ports: p0 ∈ {0,1}
    components: h_p0 on (p0)
    boundaries B = {b0}; edits A = {1,[p0=1],[alt:h_p0],[p0=1,alt:h_p0]}
    composition (other than with 1): [p0=1]·[p0=1]=[p0=1], [p0=1]·[alt:h_p0]=[p0=1,alt:h_p0], [p0=1]·[p0=1,alt:h_p0]=[p0=1,alt:h_p0], [alt:h_p0]·[p0=1]=[p0=1,alt:h_p0], [alt:h_p0]·[alt:h_p0]=[alt:h_p0], [alt:h_p0]·[p0=1,alt:h_p0]=[p0=1,alt:h_p0], [p0=1,alt:h_p0]·[p0=1]=[p0=1,alt:h_p0], [p0=1,alt:h_p0]·[alt:h_p0]=[p0=1,alt:h_p0], [p0=1,alt:h_p0]·[p0=1,alt:h_p0]=[p0=1,alt:h_p0]
    L_h_p0(1,b0) = {(0)}
    L_h_p0([p0=1],b0) = {(1)}
    L_h_p0([alt:h_p0],b0) = {}
    L_h_p0([p0=1,alt:h_p0],b0) = {(1)}
  candidate ℰ for p: Γ = {k0}, δ_E = p0
    π: p0 := id(p0)
    τ: 1↦1, [p0=1]↦[p0=1], [alt:h_p0]↦[alt:h_p0], [p0=1,alt:h_p0]↦[p0=1,alt:h_p0]; σ: b0↦b0
    λ(k0) = ({h_p0}, p0:=id(p0))
  organization E_ℰ
    ports: p0 ∈ {0,1}
    components: k0 on (p0)
    boundaries B = {b0}; edits A = {1,[p0=1],[alt:h_p0],[p0=1,alt:h_p0]}
    composition (other than with 1): [p0=1]·[p0=1]=[p0=1], [p0=1]·[alt:h_p0]=[p0=1,alt:h_p0], [p0=1]·[p0=1,alt:h_p0]=[p0=1,alt:h_p0], [alt:h_p0]·[p0=1]=[p0=1,alt:h_p0], [alt:h_p0]·[alt:h
  … (the full text is in search results.json and is printed by the reproduce command)
  ```

- **Acc not antitone in C** [there is] — *witness found*. there are C' ⊆ C with Acc on C and not on C'
  - Searched: sizes ports=1 dom≤1 comps=1 |B|=1 edits=0 … ports=3 dom≤2 comps=3 |B|=2 edits=2 (108 sizes, 1200 draws each); families: G-surg, G-free; proper models only; seed 104343; 701 models tried; first found at size ports=1 dom≤2 comps=1 |B|=1 edits=1.

  ```
  Acc on C, not on C' ⊆ C
  question p: target D, b0 = b0, query Q_w (reads the designated port) designating p0, C = {(1,b0), ([alt:h_p0],b0)}
  question p': target D, b0 = b0, query Q_w (reads the designated port) designating p0, C = {(1,b0)}
  organization D
    ports: p0 ∈ {0,1}
    components: h_p0 on (p0)
    boundaries B = {b0}; edits A = {1,[alt:h_p0]}
    composition (other than with 1): [alt:h_p0]·[alt:h_p0]=[alt:h_p0]
    L_h_p0(1,b0) = {(1)}
    L_h_p0([alt:h_p0],b0) = {}
  candidate ℰ for p: Γ = {k0}, δ_E = p0
    π: p0 := id(p0)
    τ: 1↦1, [alt:h_p0]↦[alt:h_p0]; σ: b0↦b0
    λ(k0) = ({h_p0}, p0:=id(p0))
  organization E_ℰ
    ports: p0 ∈ {0,1}
    components: k0 on (p0)
    boundaries B = {b0}; edits A = {1,[alt:h_p0]}
    composition (other than with 1): [alt:h_p0]·[alt:h_p0]=[alt:h_p0]
    L_k0(1,b0) = {(1)}
    L_k0([alt:h_p0],b0) = {}
  ```

- **Acc not monotone in C** [there is] — *witness found*. there are C' ⊆ C with Acc on C' and not on C
  - Searched: sizes ports=1 dom≤1 comps=1 |B|=1 edits=0 … ports=3 dom≤2 comps=3 |B|=2 edits=2 (108 sizes, 1200 draws each); families: G-surg, G-free; proper models only; seed 104344; 2549 models tried; first found at size ports=1 dom≤2 comps=1 |B|=1 edits=2.

  ```
  Acc on C' ⊆ C, not on C
  question p: target D, b0 = b0, query Q_w (reads the designated port) designating p0, C = {(1,b0), ([alt:h_p0],b0), ([p0=0],b0)}
  question p': target D, b0 = b0, query Q_w (reads the designated port) designating p0, C = {(1,b0), ([alt:h_p0],b0)}
  organization D
    ports: p0 ∈ {0,1}
    components: h_p0 on (p0)
    boundaries B = {b0}; edits A = {1,[p0=0],[alt:h_p0],[p0=0,alt:h_p0]}
    composition (other than with 1): [p0=0]·[p0=0]=[p0=0], [p0=0]·[alt:h_p0]=[p0=0,alt:h_p0], [p0=0]·[p0=0,alt:h_p0]=[p0=0,alt:h_p0], [alt:h_p0]·[p0=0]=[p0=0,alt:h_p0], [alt:h_p0]·[alt:h_p0]=[alt:h_p0], [alt:h_p0]·[p0=0,alt:h_p0]=[p0=0,alt:h_p0], [p0=0,alt:h_p0]·[p0=0]=[p0=0,alt:h_p0], [p0=0,alt:h_p0]·[alt:h_p0]=[p0=0,alt:h_p0], [p0=0,alt:h_p0]·[p0=0,alt:h_p0]=[p0=0,alt:h_p0]
    L_h_p0(1,b0) = {(1)}
    L_h_p0([p0=0],b0) = {(0)}
    L_h_p0([alt:h_p0],b0) = full
    L_h_p0([p0=0,alt:h_p0],b0) = {(0)}
  candidate ℰ for p: Γ = {k0}, δ_E = p0
    π: p0 := id(p0)
    τ: 1↦1, [p0=0]↦[p0=0], [alt:h_p0]↦[alt:h_p0], [p0=0,alt:h_p0]↦[p0=0,alt:h_p0]; σ: b0↦b0
    λ(k0) = ({h_p0}, p0:=id(p0))
  organization E_ℰ
    ports: p0 ∈ {0,1}
    components: k0 on (p0)
    boundaries B = {b0}; edits A = {1,[p0=0],[alt:h_p0],[p0=0,alt:h_p0]}
    composition (other than with 1): [p0=0]·[p0=0]=[p0=0], [p0=0]·[alt:h_p0]=[p0=0,alt:h_p0], [p0=0]·[p0=0,alt:h_p0]=[p0=0,alt:h_p0], [alt:h_p0]·[p0=0]=[p0=0,alt:h_p0], [alt:h_p0]·[alt:h_p0]=[alt:h_p0], [alt:h_p0]·[p0=0,alt:h_p0]=[p0=0,alt:h_p0], [p0=0,alt:h_p0]·[p0=0]=[p0=0,alt:h_p0], [p0=0,al
  … (the full text is in search results.json and is printed by the reproduce command)
  ```

- **NC1 can fail on C' while holding on C** [there is] — *witness found*. there are C' ⊆ C with NC1 on C and not on C'
  - Searched: sizes ports=1 dom≤1 comps=1 |B|=1 edits=0 … ports=3 dom≤2 comps=3 |B|=2 edits=2 (108 sizes, 1600 draws each); families: G-surg, G-free; proper models only; seed 104345; 742 models tried; first found at size ports=1 dom≤2 comps=1 |B|=1 edits=1.

  ```
  NC1 holds on C and fails on C' ⊆ C
  question p: target D, b0 = b0, query Q_w (reads the designated port) designating p0, C = {(1,b0), ([alt:h_p0],b0)}
  question p': target D, b0 = b0, query Q_w (reads the designated port) designating p0, C = {(1,b0)}
  organization D
    ports: p0 ∈ {0,1}
    components: h_p0 on (p0)
    boundaries B = {b0}; edits A = {1,[alt:h_p0]}
    composition (other than with 1): [alt:h_p0]·[alt:h_p0]=[alt:h_p0]
    L_h_p0(1,b0) = {(1)}
    L_h_p0([alt:h_p0],b0) = full
  candidate ℰ for p: Γ = {k0}, δ_E = p0
    π: p0 := id(p0)
    τ: 1↦1, [alt:h_p0]↦[alt:h_p0]; σ: b0↦b0
    λ(k0) = ({h_p0}, p0:=id(p0))
  organization E_ℰ
    ports: p0 ∈ {0,1}
    components: k0 on (p0)
    boundaries B = {b0}; edits A = {1,[alt:h_p0]}
    composition (other than with 1): [alt:h_p0]·[alt:h_p0]=[alt:h_p0]
    L_k0(1,b0) = {(1)}
    L_k0([alt:h_p0],b0) = full
  ```

### FC35 · 'Prediction' at L151 is outside L219's definition — NOT TESTED

**The claim.** L219 defines Pred for transports whose codomain is S (L217). L151 applies 'prediction' to a transport faithful on the contract with no codomain named. Under I51, Pred_t(a,b) := Ans_E(τ(a),σ(b)) for every t, and L151's use is covered; without it, L151's use lies outside the definition.

**Rests on.** Claim's inventions: I51. Program's: none. **Reproduce.** `cd "/home/user/ThreadSmith/Semantics/results/S104 Round 2 - maths" && python3 -m model.run --claim FC35 --scale 4 --time-cap 45`

- **L151's 'prediction'** [not tested] — *not tested*. whether L151's use lies inside L219's definition
  - Why not: a question of which lines a definition covers (I51)

### FC36 · What a question asks is fixed by the query and the contract, not by a label — HOLDS ON ALL MODELS TRIED

**The claim.** Under I72, Prod(p), Ident(p), Obst(p) are functions of (D, Q, δ, C) and are unchanged by renaming ports and components (δ carried along). They need not exclude one another (a query can read an output port and also compute a fibre) and do not cover rule-status and purpose-achievement.

**Rests on.** Claim's inventions: I72. Program's: I72. **Reproduce.** `cd "/home/user/ThreadSmith/Semantics/results/S104 Round 2 - maths" && python3 -m model.run --claim FC36 --scale 4 --time-cap 45`

- **production and obstruction at once** [computation] — *computed: as claimed*. a query can meet two respects' sufficient conditions (I72)

  ```
  Q reads w, an output of h_w, C holds settings of v upstream of w (Prod: True), and Y_p = {reachable, unreachable} (Obst: True).
  ```

- **respects are carried by renamings** [by construction] — *holds by construction*. Prod, Obst are functions of (D, Q, δ, C)

  ```
  they read only D's relations, A, the designated port's domain and C
  ```

### FC37 · The finite monotone claim — HOLDS ON ALL MODELS TRIED

**The claim.** For every finite Γ and every upward-closed S ⊆ P(Γ) with Γ ∈ S: (∃W∈S: CB({d};W)) ⟺ d ∈ ∪min S, and Γ∖{d} ∉ S ⟺ d ∈ ∩min S. Testable on every upward-closed family over |Γ| ≤ 5.

**Rests on.** Claim's inventions: none. Program's: I77. **Reproduce.** `cd "/home/user/ThreadSmith/Semantics/results/S104 Round 2 - maths" && python3 -m model.run --claim FC37 --scale 4 --time-cap 45`

- **every upward-closed family, |Γ| ≤ 5** [for all] — *holds on all models tried*. for finite Γ, upward-closed S with Γ ∈ S: contributory ⟺ ∈ ∪min S; indispensable ⟺ ∈ ∩min S
  - Searched: exhaustive: all families on |Γ| ≤ 4 (filtered to upward closed with Γ ∈ S) and all 7581 up-closures of antichains on |Γ| = 5; 73393 models tried; 7773 of them meeting the claim's hypothesis.

- **S_{E,p} of random candidates** [for all] — *holds on all models tried*. the finite monotone claim on route families computed from candidates (where its hypotheses hold)
  - Searched: sizes ports=1 dom≤1 comps=1 |B|=1 edits=0 … ports=3 dom≤2 comps=3 |B|=2 edits=2 (108 sizes, 120 draws each); families: G-surg, G-free; seed 104372; 12960 models tried; 1325 of them meeting the claim's hypothesis.

### FC38 · Redundant routes — HOLDS ON ALL MODELS TRIED

**The claim.** S = {{a},{b},{a,b}} is upward closed with min S = {{a},{b}}: a and b are contributory, neither is globally indispensable.

**Rests on.** Claim's inventions: I30. Program's: none. **Reproduce.** `cd "/home/user/ThreadSmith/Semantics/results/S104 Round 2 - maths" && python3 -m model.run --claim FC38 --scale 4 --time-cap 45`

- **redundant routes** [computation] — *computed: as claimed*. S = {{a},{b},{a,b}}: each contributory, neither indispensable

  ```
  {'upward': True, 'mins': [['b'], ['a']], 'contrib': {'a': True, 'b': True}, 'indisp': {'a': False, 'b': False}}
  ```

### FC39 · Interference — HOLDS ON ALL MODELS TRIED

**The claim.** S = {{a}}: Γ ∉ S, {a} ∈ S, S is not upward closed, so the finite monotone claim's hypotheses fail; {a} is critical in {a}.

**Rests on.** Claim's inventions: I30. Program's: none. **Reproduce.** `cd "/home/user/ThreadSmith/Semantics/results/S104 Round 2 - maths" && python3 -m model.run --claim FC39 --scale 4 --time-cap 45`

- **interference** [computation] — *computed: as claimed*. S = {{a}}: Γ ∉ S, not upward closed, {a} critical in {a}

  ```
  Γ ∈ S: False; CB({a};{a}): True
  ```

### FC40 · Infinitary routes: collective criticality, and the step the first sentence leaves unsaid — HOLDS ON ALL MODELS TRIED

**The claim.** With I31: (a) S is upward closed, Γ ∈ S, min S = ∅, no member of S has one element. (b) For W ∈ S and nonempty B ⊆ W: CB(B;W) ⟺ the index set of W∖B is bounded; every critical block is infinite, and critical blocks exist (B = W). (c) Each d_n does no work by itself (L313): for W ∈ S, W ∪ {d_n} ∈ S and W ∖ {d_n} ∈ S. (d) So L313's last sentence has an instance here. Step (c) is the one L311's first sentence does not say in words.

**Rests on.** Claim's inventions: I30, I31. Program's: I91. **Reproduce.** `cd "/home/user/ThreadSmith/Semantics/results/S104 Round 2 - maths" && python3 -m model.run --claim FC40 --scale 4 --time-cap 45`

- **(a)-(c) on eventually periodic sets** [for all] — *holds on all models tried*. routes = unbounded index sets: upward closed, no minimal member, no one-commitment route, every critical block infinite, each d_n does no work by itself
  - Searched: sizes ports=1 dom≤1 comps=1 |B|=1 edits=0 … ports=1 dom≤1 comps=1 |B|=1 edits=0 (1 sizes, 80000 draws each); families: eventually periodic subsets of ℕ; subsets of ℕ of the form F ∪ {n ≥ N : n mod m ∈ R}, N ≤ 6, m ≤ 4; seed 104401; 80000 models tried.

### FC41 · Commitments that do no work, and why 'when Γ is infinite' — HOLDS ON ALL MODELS TRIED

**The claim.** NoWork(d) := S ≠ ∅ ∧ ∀W∈S (W∪{d} ∈ S ∧ W∖{d} ∈ S). Then (a) for every W ⊆ Γ: W∪{d} ∈ S ⟺ W∖{d} ∈ S; (b) {d} is critical in no route; (c) a finite block every member of which does no work by itself is critical in no route, so the 'when Γ is infinite' of L313's last sentence cannot be dropped.

**Rests on.** Claim's inventions: I29. Program's: I77. **Reproduce.** `cd "/home/user/ThreadSmith/Semantics/results/S104 Round 2 - maths" && python3 -m model.run --claim FC41 --scale 4 --time-cap 45`

- **every family on |Γ| ≤ 4** [for all] — *holds on all models tried*. NoWork(d): (a) W∪{d} ∈ S ⟺ W∖{d} ∈ S; (b) {d} critical in no route; (c) a finite block of such commitments is critical in no route
  - Searched: exhaustive: all 2^(2^n) families S ⊆ P(Γ), n ≤ 4 (65,536 at n = 4); 65812 models tried.

### FC42 · Criticality is relative to the route — HOLDS ON ALL MODELS TRIED

**The claim.** (a) In Redundant routes, B = W = {a,b} is critical (W∖B = ∅ ∉ S) and neither singleton is. (b) There, a is critical in {a} and not in {a,b}.

**Rests on.** Claim's inventions: I30. Program's: none. **Reproduce.** `cd "/home/user/ThreadSmith/Semantics/results/S104 Round 2 - maths" && python3 -m model.run --claim FC42 --scale 4 --time-cap 45`

- **criticality relative to the route** [computation] — *computed: as claimed*. (a) {a,b} critical in {a,b}, no singleton is; (b) a critical in {a}, not in {a,b}

  ```
  CB({a,b};{a,b}) = True (needs ∅ ∉ S: True); singletons critical in {a,b}: False; CB({a};{a}) = True
  ```

### FC43 · Conflict, rivals, problems and 'easy to vary' are symmetric — HOLDS ON ALL MODELS TRIED

**The claim.** Conf(ℰ,ℰ';a,b) ⟺ Conf(ℰ',ℰ;a,b); Riv is symmetric (either offered in place of the other, I33); so Prob_j and its kind are symmetric, and ETV_j(ℰ) through ℰ' gives ETV_j(ℰ').

**Rests on.** Claim's inventions: I33, I37. Program's: I77, I78, I81, I86. **Reproduce.** `cd "/home/user/ThreadSmith/Semantics/results/S104 Round 2 - maths" && python3 -m model.run --claim FC43 --scale 4 --time-cap 45`

- **symmetry** [for all] — *holds on all models tried*. Conf(ℰ,ℰ';a,b) ⟺ Conf(ℰ',ℰ;a,b); the kind of problem is symmetric
  - Searched: sizes ports=1 dom≤1 comps=1 |B|=1 edits=0 … ports=3 dom≤2 comps=2 |B|=2 edits=1 (48 sizes, 80 draws each); families: G-surg, G-free; seed 104431; 3837 models tried.

### FC44 · Two commitments with one counterpart and different relations cannot both meet (F1) — HOLDS ON ALL MODELS TRIED

**The claim.** Under I36: if k ∈ Γ and k' ∈ Γ' have one counterpart and different relations at (a,b), then no R gives F1_ab(ℰ,R) ∧ F1_ab(ℰ',R). Under the reading 'one counterpart = the same subnetwork', there are ℰ, ℰ', R meeting both with different relations.

**Rests on.** Claim's inventions: I14, I19, I36. Program's: I77, I78, I81, I101. **Reproduce.** `cd "/home/user/ThreadSmith/Semantics/results/S104 Round 2 - maths" && python3 -m model.run --claim FC44 --scale 4 --time-cap 45`

- **under I36** [for all] — *holds on all models tried*. one counterpart (same subnetwork, translations, value maps) and different relations at (a,b) ⇒ no R gives F1 at (a,b) to both
  - Searched: sizes ports=1 dom≤1 comps=1 |B|=1 edits=0 … ports=3 dom≤2 comps=2 |B|=2 edits=1 (48 sizes, 80 draws each); families: G-surg, G-free; seed 104441; 3641 models tried.

- **the reading 'one counterpart = the same subnetwork'** [there is] — *witness found*. there are ℰ, ℰ', R with one subnetwork as counterpart, different relations, both meeting (F1)
  - Searched: sizes ports=1 dom≤1 comps=1 |B|=1 edits=0 … ports=3 dom≤2 comps=3 |B|=2 edits=2 (108 sizes, 240 draws each); families: G-surg, G-free; proper models only; seed 104442; 9 models tried; first found at size ports=2 dom≤2 comps=1 |B|=1 edits=0.

  ```
  One subnetwork {h_p0} is the counterpart of k in both candidates, through different port translations (v := p0 and v := p1). At (1,b0) the two relations differ and both meet (F1) under the target's own relations: the clause of L315 ('none do when two of their active components with one counterpart have different relations there') needs I36's reading of 'one counterpart'.
  question p: target D, b0 = b0, query Q_w (reads the designated port) designating p1, C = {(1,b0)}
  organization D
    ports: p0 ∈ {0,1}; p1 ∈ {0,1}
    components: h_p0 on (p0,p1)
    boundaries B = {b0}; edits A = {1}
    L_h_p0(1,b0) = {(0,0) (0,1)}
  candidate ℰ_p0 for p: Γ = {k}, δ_E = v
    π: v := id(p0)
    τ: 1↦1; σ: b0↦b0
    λ(k) = ({h_p0}, v:=id(p0))
  organization E_p0
    ports: v ∈ {0,1}
    components: k on (v)
    boundaries B = {b0}; edits A = {1}
    L_k(1,b0) = {(0)}
  candidate ℰ_p1 for p: Γ = {k}, δ_E = v
    π: v := id(p1)
    τ: 1↦1; σ: b0↦b0
    λ(k) = ({h_p0}, v:=id(p1))
  organization E_p1
    ports: v ∈ {0,1}
    components: k on (v)
    boundaries B = {b0}; edits A = {1}
    L_k(1,b0) = full
  ```

### FC45 · Recoded candidates, and candidates some relations let both meet, conflict nowhere — HOLDS ON ALL MODELS TRIED

**The claim.** (a) If φ: E ≅ E' with t' = φ∘t, Γ' = φ[Γ] and Ans_E'(φa',φb') = Ans_E(a',b'), then ¬Conf(ℰ,ℰ';a,b) at every pair both translate. (b) If at every such pair some R lets both meet, they conflict nowhere.

**Rests on.** Claim's inventions: I17, I19, I20, I70. Program's: I70, I77, I78, I81. **Reproduce.** `cd "/home/user/ThreadSmith/Semantics/results/S104 Round 2 - maths" && python3 -m model.run --claim FC45 --scale 4 --time-cap 45`

- **(a) recoded candidates** [for all] — *holds on all models tried*. a structure-preserving recoding of ℰ conflicts with ℰ at no pair
  - Searched: sizes ports=1 dom≤1 comps=1 |B|=1 edits=0 … ports=3 dom≤2 comps=2 |B|=2 edits=1 (48 sizes, 60 draws each); families: G-surg, G-free; seed 104451; 2879 models tried.

- **(b) some R lets both meet at every pair ⇒ no conflict** [by construction] — *holds by construction*. by D8.2's second disjunct

  ```
  Conf's second disjunct needs ¬∃R BothMeet; the first needs different answers, which BothMeet excludes (both equal Ans^R_p)
  ```

### FC46 · A conflict inside the contract: at most one account — HOLDS ON ALL MODELS TRIED

**The claim.** ∀ℰ,ℰ' ∀(a,b)∈C: Conf(ℰ,ℰ';a,b) ⇒ ¬(Acc(ℰ) ∧ Acc(ℰ')). (If both met (E), both would meet (F1), the (F2) equation and (A) at (a,b) under the target's own relations R*: equal answers, and R* lets both.) So two accounts on C conflict at no pair of C.

**Rests on.** Claim's inventions: I19, I21. Program's: I77, I78, I81, I85. **Reproduce.** `cd "/home/user/ThreadSmith/Semantics/results/S104 Round 2 - maths" && python3 -m model.run --claim FC46 --scale 4 --time-cap 45`

- **two accounts do not conflict in C** [for all] — *holds on all models tried*. Acc(ℰ) ∧ Acc(ℰ') ⇒ no conflict at any pair of C
  - Searched: sizes ports=1 dom≤1 comps=1 |B|=1 edits=0 … ports=3 dom≤2 comps=2 |B|=2 edits=1 (48 sizes, 240 draws each); families: G-surg, G-free; only pairs of candidates that both meet (E) are counted; seed 104461; 722 models tried.

### FC47 · A test at a conflict pair rules out at least one, for an assessor who can use it — HOLDS ON ALL MODELS TRIED

**The claim.** (a) Conf(ℰ,ℰ';a,b) ⇒ ∀R ¬(Meets_ab(ℰ,R) ∧ Meets_ab(ℰ',R)); so for the recorded R*, Meets_ab fails for at least one. (b) For j who admits the forms used, whose scope holds (a,b), and for whom the record's premises about background and instruments are live, the argument 'R* at (a,b); Meets_ab(·,R*) fails; Acc requires it' puts a member in X_j(Acc(ℰ)) or in X_j(Acc(ℰ')).

**Rests on.** Claim's inventions: I19, I38, I40, I42, I43. Program's: I77, I78, I81, I87, I88, I89. **Reproduce.** `cd "/home/user/ThreadSmith/Semantics/results/S104 Round 2 - maths" && python3 -m model.run --claim FC47 --scale 4 --time-cap 45`

- **(a) conflict excludes joint meeting** [for all] — *holds on all models tried*. Conf(ℰ,ℰ';a,b) ⇒ ∀R ¬(Meets_ab(ℰ,R) ∧ Meets_ab(ℰ',R))
  - Searched: sizes ports=1 dom≤1 comps=1 |B|=1 edits=0 … ports=3 dom≤2 comps=2 |B|=2 edits=1 (48 sizes, 60 draws each); families: G-surg, G-free; seed 104471; 2879 models tried; 1644 of them meeting the claim's hypothesis.

- **(b) the argument from a test's record** [computation] — *computed: as claimed*. for j who admits MP and MT and for whom the record and its premises are live, the argument is in X_j(Acc(ℰ))

  ```
  argument:
    step [MT] ⊢ ¬acc1
      step [MP] ⊢ ¬meets1
        record leaf: rec
        assumption leaf: (rec → ¬meets1)
      assumption leaf: (acc1 → meets1)
  usable by j: True; rules out Acc(ℰ): True; usable once the record is withdrawn: False
  ```

### FC48 · No conflict inside the contract: answers agree there — HOLDS ON ALL MODELS TRIED

**The claim.** If ¬Conf(ℰ,ℰ';a,b) at every (a,b) ∈ C, then Ans_E(τa,σb) = Ans_E'(τ'a,σ'b) at every (a,b) ∈ C (⊥ = ⊥, I21); so for any recorded answer at (a,b), (A) there holds for both or for neither.

**Rests on.** Claim's inventions: I21. Program's: I77, I78, I81. **Reproduce.** `cd "/home/user/ThreadSmith/Semantics/results/S104 Round 2 - maths" && python3 -m model.run --claim FC48 --scale 4 --time-cap 45`

- **no conflict in C ⇒ answers agree** [for all] — *holds on all models tried*. ¬Conf at every pair of C ⇒ equal answers on C
  - Searched: sizes ports=1 dom≤1 comps=1 |B|=1 edits=0 … ports=3 dom≤2 comps=2 |B|=2 edits=1 (48 sizes, 60 draws each); families: G-surg, G-free; seed 104481; 2879 models tried; 1363 of them meeting the claim's hypothesis.

### FC49 · The two kinds of problem exclude each other and cover every pair of rivals — HOLDS ON ALL MODELS TRIED

**The claim.** Riv(ℰ,ℰ';p) ⇒ exactly one of: some pair of C is a conflict pair; no pair of C is, and some translated pair outside C is.

**Rests on.** Claim's inventions: I16, I17, I33. Program's: I77, I78, I81, I86. **Reproduce.** `cd "/home/user/ThreadSmith/Semantics/results/S104 Round 2 - maths" && python3 -m model.run --claim FC49 --scale 4 --time-cap 45`

- **exactly one kind** [for all] — *holds on all models tried*. Riv ⇒ exactly one of kind (i), kind (ii)
  - Searched: sizes ports=1 dom≤1 comps=1 |B|=1 edits=0 … ports=3 dom≤2 comps=2 |B|=2 edits=1 (48 sizes, 60 draws each); families: G-surg, G-free; seed 104491; 2879 models tried; 1588 of them meeting the claim's hypothesis.

### FC50 · A finer contract makes a problem of the first kind; a narrowed one leaves the problem on p — HOLDS ON ALL MODELS TRIED

**The claim.** (a) If Conf(ℰ,ℰ';a,b) with (a,b) ∉ C, p' is p with C' ⊇ C ∪ {(a,b)}, and ℰ, ℰ' are offered for p' with neither ruled out for j, then Prob_j(ℰ,ℰ';p') is of the first kind. (b) For C'' ⊆ C leaving out every conflict pair, p'' ≠ p, and Prob_j(ℰ,ℰ';p) is a function of p's data and j alone, unchanged by anything about p''.

**Rests on.** Claim's inventions: I11, I33. Program's: I77, I78, I81, I86. **Reproduce.** `cd "/home/user/ThreadSmith/Semantics/results/S104 Round 2 - maths" && python3 -m model.run --claim FC50 --scale 4 --time-cap 45`

- **(a) a finer contract makes kind (i)** [for all] — *holds on all models tried*. Conf at (a,b) ∉ C, C' ⊇ C ∪ {(a,b)} ⇒ the problem on p' is of kind (i)
  - Searched: sizes ports=1 dom≤1 comps=1 |B|=1 edits=0 … ports=3 dom≤2 comps=2 |B|=2 edits=1 (48 sizes, 60 draws each); families: G-surg, G-free; seed 104501; 2880 models tried; 563 of them meeting the claim's hypothesis.

- **(b) a narrowed contract leaves the problem on p** [by construction] — *holds by construction*. Prob_j on p is a function of p's data and j

  ```
  problem_kind(ℰ,ℰ') reads only the candidates, their question and its contract
  ```

### FC51 · A change that separates two accounts lies outside their shared contract — HOLDS ON ALL MODELS TRIED

**The claim.** (a) If Acc(ℰ) and Acc(ℰ') on C, C' ⊋ C, Acc(ℰ) on C' and ¬Acc(ℰ') on C', then some (a,b) ∈ C'∖C has ¬(F1 ∧ (F2) equation ∧ A)_ab(ℰ'), or τ' fails the homomorphism clause on edits new in C', or the scope statements differ (NC1 and NC2 carry over from C to C'; Sol_D(1,b0) is unchanged). (b) If ℰ' is ℰ with λ' = λ∘ψ for a permutation ψ of Γ and both meet (F1) on C, then for every k and (a,b) ∈ C the projected relations of λ(k) and λ(ψk) agree under the port translations: no pair of C separates the two pairings.

**Rests on.** Claim's inventions: I18, I24, I27. Program's: I77, I78, I81, I85. **Reproduce.** `cd "/home/user/ThreadSmith/Semantics/results/S104 Round 2 - maths" && python3 -m model.run --claim FC51 --scale 4 --time-cap 45`

- **(a) separation lies in C'∖C** [for all] — *holds on all models tried*. Acc of both on C, Acc(ℰ) and ¬Acc(ℰ') on C' ⊋ C ⇒ a pair of C'∖C where ℰ' fails F1, the F2 equation or A
  - Searched: sizes ports=1 dom≤1 comps=1 |B|=1 edits=0 … ports=3 dom≤2 comps=3 |B|=2 edits=2 (108 sizes, 320 draws each); families: G-surg, G-free; each question's scope statement states every pair outside its contract (I85); seed 104511; 20665 models tried; 202 of them meeting the claim's hypothesis.

- **(b) two pairings** [for all] — *holds on all models tried*. λ' = λ∘ψ (ψ keeping footprints), both F1 on C ⇒ the projected relations of λ(k) and λ(ψk) agree on C
  - Searched: sizes ports=1 dom≤1 comps=1 |B|=1 edits=0 … ports=3 dom≤2 comps=3 |B|=2 edits=2 (108 sizes, 320 draws each); families: G-surg, G-free; ψ restricted to permutations of Γ that keep footprints; seed 104512; 8884 models tried; 5693 of them meeting the claim's hypothesis.

### FC52 · Conflict with a claim: the first disjunct implies the second — HOLDS ON ALL MODELS TRIED

**The claim.** Under I34: if χ excludes ℰ's answer at (a,b), then χ excludes every R with Meets_ab(ℰ,R) (Meets includes (A) at the pair, so the answer under such R is ℰ's answer). The definition reduces to its second disjunct.

**Rests on.** Claim's inventions: I19, I34. Program's: I77, I78, I81. **Reproduce.** `cd "/home/user/ThreadSmith/Semantics/results/S104 Round 2 - maths" && python3 -m model.run --claim FC52 --scale 4 --time-cap 45`

- **first disjunct implies the second** [for all] — *holds on all models tried*. χ excludes ℰ's answer at (a,b) ⇒ χ excludes every R with Meets_ab(ℰ,R)
  - Searched: sizes ports=1 dom≤1 comps=1 |B|=1 edits=0 … ports=3 dom≤2 comps=2 |B|=2 edits=1 (48 sizes, 40 draws each); families: G-surg, G-free; seed 104521; 1919 models tried; 747 of them meeting the claim's hypothesis.

### FC53 · Conflict with a claim rules a candidate out only with the premise that the claim speaks of the target — HOLDS ON ALL MODELS TRIED

**The claim.** (a) If ConfCl(ℰ,χ;a,b), (a,b) ∈ C, Applies(χ,a,b), χ and Applies live for j, forms admitted: X_j(Acc(ℰ)) ≠ ∅. (b) There is a model (the text's pendulum, its friction component deleted by the edit) with ConfCl(ℰ,χ;a,b), ¬Applies(χ,a,b), and no argument from χ in X_j(Acc(ℰ)).

**Rests on.** Claim's inventions: I34, I38, I40. Program's: I87, I88, I89, I90. **Reproduce.** `cd "/home/user/ThreadSmith/Semantics/results/S104 Round 2 - maths" && python3 -m model.run --claim FC53 --scale 4 --time-cap 45`

- **(a) with Applies** [computation] — *computed: as claimed*. ConfCl at (a,b) ∈ C, Applies, χ and Applies live, forms admitted ⇒ X_j(Acc(ℰ)) ≠ ∅

  ```
  argument:
    step [MP] ⊢ ¬acc
      step [AndI] ⊢ (applies ∧ chi)
        assumption leaf: applies
        assumption leaf: chi
      assumption leaf: ((chi ∧ applies) → ¬acc)
  usable: True, rules out Acc: True
  ```

- **(b) the pendulum without Applies** [computation] — *computed: as claimed*. ConfCl(ℰ,χ;a,b) and ¬Applies(χ,a,b), and no argument from χ in X_j(Acc(ℰ))

  ```
  D: friction stops the motion at the baseline; the edit del_f deletes friction. χ allows only relations of friction that stop the motion. ConfCl at (del_f,b0): True. For j who accepts χ and 'χ ∧ Applies ⇒ ¬Acc' but not Applies, the arguments of height ≤ 2 from these premises (19) that j can use and that rule out Acc: 0.
  ```

### FC54 · Rivals given χ conflict nowhere without χ at that pair — HOLDS ON ALL MODELS TRIED

**The claim.** Riv_χ(ℰ,ℰ';p) := Offered ∧ ∃(a,b) ConfG_χ(ℰ,ℰ';a,b); Prob_{χ,j} := Riv_χ ∧ χ ∈ Accepted_j ∧ neither ruled out for j. Claim: ConfG_χ(a,b) ⇒ ¬Conf(a,b) (some R lets both meet, so their answers agree and the second disjunct of Conf fails). So a pair of rivals given χ that conflicts at no other pair is not a pair of rivals.

**Rests on.** Claim's inventions: I19, I33, I34, I35. Program's: I77, I78, I81. **Reproduce.** `cd "/home/user/ThreadSmith/Semantics/results/S104 Round 2 - maths" && python3 -m model.run --claim FC54 --scale 4 --time-cap 45`

- **conflict given χ excludes conflict** [for all] — *holds on all models tried*. ConfG_χ(ℰ,ℰ';a,b) ⇒ ¬Conf(ℰ,ℰ';a,b)
  - Searched: sizes ports=1 dom≤1 comps=1 |B|=1 edits=0 … ports=3 dom≤2 comps=2 |B|=2 edits=1 (48 sizes, 40 draws each); families: G-surg, G-free; seed 104541; 1919 models tried; 578 of them meeting the claim's hypothesis.

### FC55 · Nothing in Part VI counts rivals or orders candidates — HOLDS ON ALL MODELS TRIED

**The claim.** Syntactic: every predicate of §§8–10 takes at most two candidates, or one candidate and one claim; none takes a set of candidates, a cardinality or an order on candidates.

**Rests on.** Claim's inventions: none. Program's: none. **Reproduce.** `cd "/home/user/ThreadSmith/Semantics/results/S104 Round 2 - maths" && python3 -m model.run --claim FC55 --scale 4 --time-cap 45`

- **syntactic: no predicate of Part VI takes more than two candidates** [computation] — *computed: as claimed*. every predicate over candidates in the model takes at most two

  ```
  functions checked: ['conflict', 'conf_given', 'conf_claim', 'rivals', 'problem_kind', 'conflict_pairs', 'meets_ab', 'meet_table']; taking more than two candidates: none
  ```

### FC56 · Ruling out grows with what is accepted; withdrawal rules nothing out; absence rules out nothing — HOLDS ON ALL MODELS TRIED

**The claim.** (a) Usable_j and X_j(φ) are monotone in Accepted_j, in Forms_j and in the contracts j declares (grain and boundary held fixed): enlarging any of them never makes an argument unusable; RO does not depend on j. So withdrawing a premise adds no member to any X_j(φ): it rules out nothing not already ruled out. (b) There are j and φ with X_j(φ) = ∅ = X_j(¬φ).

**Rests on.** Claim's inventions: I38, I40, I41. Program's: I87, I88, I89. **Reproduce.** `cd "/home/user/ThreadSmith/Semantics/results/S104 Round 2 - maths" && python3 -m model.run --claim FC56 --scale 4 --time-cap 45`

- **(a) monotone in what is accepted and admitted** [for all] — *holds on all models tried*. Accepted_j ⊆ Accepted_j', Forms_j ⊆ Forms_j' ⇒ Usable_j ⊆ Usable_j' and X_j(φ) ⊆ X_j'(φ)
  - Searched: sizes ports=3 dom≤2 comps=1 |B|=1 edits=0 … ports=3 dom≤2 comps=1 |B|=1 edits=0 (1 sizes, 1600 draws each); families: random propositional premises over p, q, r; all arguments of height ≤ 2; seed 104561; 1162 models tried; time cap 45 s reached at size ports=3 dom≤2 comps=1 |B|=1 edits=0.

- **(b) absence rules out nothing** [computation] — *computed: as claimed*. there are j, φ with X_j(φ) = ∅ = X_j(¬φ)

  ```
  j accepts p; φ = q: |X_j(q)| = 0, |X_j(¬q)| = 0 over 6 arguments
  ```

### FC57 · (I2): identified at every attainable value exactly when the feature factors through the measurement — HOLDS ON ALL MODELS TRIED

**The claim.** (∀y ∈ g[Z]: |f[Z_y]| = 1) ⟺ ∃f̄: Y → F with f = f̄∘g on Z.

**Rests on.** Claim's inventions: I63, I64. Program's: I77. **Reproduce.** `cd "/home/user/ThreadSmith/Semantics/results/S104 Round 2 - maths" && python3 -m model.run --claim FC57 --scale 4 --time-cap 45`

- **(I2) on finite sets** [for all] — *holds on all models tried*. (∀y ∈ g[Z]: |f[Z_y]| = 1) ⟺ f = f̄∘g for some f̄
  - Searched: exhaustive: every g: Z → Y and f: Z → F with |Z| ≤ 4, |Y| ≤ 3, |F| ≤ 3; 11132 models tried.

### FC58 · (I3): the kernel criterion; repeated rows; an independent calibration — HOLDS ON ALL MODELS TRIED

**The claim.** Z = ℝ^n, g = G ∈ ℝ^{m×n}, feature c ∈ ℝ^n: (∀y ∈ G[ℝ^n]: |cᵀ[G⁻¹(y)]| = 1) ⟺ ker G ⊆ ker cᵀ. A row in the row space of G leaves ker G unchanged; a row outside it lowers dim ker G by one.

**Rests on.** Claim's inventions: I63, I64. Program's: I77. **Reproduce.** `cd "/home/user/ThreadSmith/Semantics/results/S104 Round 2 - maths" && python3 -m model.run --claim FC58 --scale 4 --time-cap 45`

- **the kernel criterion** [for all] — *holds on all models tried*. c constant on every fibre of G over ℚ^n ⟺ ker G ⊆ ker c (rank test against a search for z ∈ ker G with c·z ≠ 0 in [-8,8]^n)
  - Searched: sizes ports=3 dom≤1 comps=1 |B|=1 edits=0 … ports=3 dom≤1 comps=1 |B|=1 edits=0 (1 sizes, 2400 draws each); families: integer matrices, entries in [-2,2], n, m ≤ 3; seed 104581; 2400 models tried.

- **rows** [for all] — *holds on all models tried*. a row in the row space leaves ker G; a row outside it lowers dim ker by one
  - Searched: sizes ports=3 dom≤1 comps=1 |B|=1 edits=0 … ports=3 dom≤1 comps=1 |B|=1 edits=0 (1 sizes, 2400 draws each); families: integer matrices; seed 104582; 2400 models tried.

- **Z a proper subset** [look] — *look: as expected*. the look: with Z a proper subset (I64's alternative), the criterion can fail

  ```
  Z = {0,1}², g = x+y, f = x: kernel criterion False; identified at every attainable y on Z: False (y = 1 has the fibre {(0,1),(1,0)}). Taking y ∈ {0, 2} alone, f is identified though ker g ⊄ ker f: on a box the criterion is sufficient, not necessary, at a given y.
  ```

### FC59 · The two balances — HOLDS ON ALL MODELS TRIED

**The claim.** G = [[1,1,0],[1,0,1]] on (x, b_A, b_B): ker G = span{(1,−1,−1)}; c = (0,−1,1) gives c·(1,−1,−1) = 0 (identified); c = (1,0,0) gives 1 (not identified).

**Rests on.** Claim's inventions: I64. Program's: none. **Reproduce.** `cd "/home/user/ThreadSmith/Semantics/results/S104 Round 2 - maths" && python3 -m model.run --claim FC59 --scale 4 --time-cap 45`

- **the two balances** [computation] — *computed: as claimed*. ker G = span{(1,−1,−1)}; b_B − b_A identified; x not

  ```
  rank G = 2; c=(0,−1,1): c·k = 0; c=(1,0,0): c·k = 1
  ```

### FC60 · Setting a bias from the favoured mass: where the circularity can be registered — HOLDS ON ALL MODELS TRIED

**The claim.** (a) Two candidates with the boundary value b_B = 0, one set 'because it gives the mass I favour' and one set by an independent calibration, have the same (D, C, E, t, Γ, Σ), so the same Acc value (FC30): (E) does not register the circularity, and NC1 does not either, since the value 0 is not the answer (I24). (b) Where it can be registered is Part IX's block: an argument concluding x = m* whose premise b_B = 0 is a record MadeFrom the claim x = m* (I39) does not rule out x ≠ m* (D9.7). (c) Its value can equal the target's b_B, so (F1), (F2), (A) can hold at the baseline.

**Rests on.** Claim's inventions: I24, I39. Program's: I87, I89. **Reproduce.** `cd "/home/user/ThreadSmith/Semantics/results/S104 Round 2 - maths" && python3 -m model.run --claim FC60 --scale 4 --time-cap 45`

- **(a) (E) does not register how an input was chosen** [by construction] — *holds by construction*. two candidates alike in (D, C, E, t, Γ, Σ) have one Acc value

  ```
  core.account takes no record of why b_B was set (FC30); NC1 compares relations with the answer, and b_B = 0 is not the answer (I24)
  ```

- **(b) the record made from x = m* does not rule out x ≠ m*** [computation] — *computed: as claimed*. RO fails for an argument whose record leaf is MadeFrom the favoured claim

  ```
  argument:
    step [MP] ⊢ x_is_m
      record leaf: bB_is_0 (made from x_is_m)
      assumption leaf: (bB_is_0 → x_is_m)
  usable: True; rules out ¬x_is_m: False
  ```

### FC61 · (O1): an invariant blocks paths; equal values do not give paths; twenty-three tokens — HOLDS ON ALL MODELS TRIED

**The claim.** (a) If zRz' ⇒ I(z) = I(z'), then R* ⊆ {(z,z') : I(z) = I(z')}. (b) There are R, I, z, z' with I(z) = I(z') and not zR*z'. (c) Distributions (n1,n2,n3) of 23 whole tokens: an equal split needs 3n = 23, which has no whole solution.

**Rests on.** Claim's inventions: I63. Program's: I77. **Reproduce.** `cd "/home/user/ThreadSmith/Semantics/results/S104 Round 2 - maths" && python3 -m model.run --claim FC61 --scale 4 --time-cap 45`

- **(a) an invariant blocks paths** [for all] — *holds on all models tried*. zRz' ⇒ I(z)=I(z') gives R* ⊆ {I(z)=I(z')}
  - Searched: exhaustive: 2000 random step relations on ≤ 5 states (seed 10461); 2000 models tried; 892 of them meeting the claim's hypothesis.

- **(b) equal values do not give paths; (c) twenty-three tokens** [computation] — *computed: as claimed*. (b) a witness; (c) no equal split of 23

  ```
  R = ∅ on {0,1}, I constant: I(0) = I(1) and 0 does not reach 1; distributions of 23 whole tokens in three piles: 300, equal splits: 0
  ```

### FC62 · Eliminative explanation: the rival's structure as a deleted counterpart — HOLDS ON ALL MODELS TRIED

**The claim.** D with a component x whose baseline relation is full (I03) and an edit a_x giving it a relation; E with k, λ(k) = {x}, baseline relation full, τ(a_x) giving k the projected relation. F1 at (1,b0): full = full; at (a_x,b0): holds when τ(a_x) gives k that relation. On C = {(1,b0), (a_x,b0)}, E can meet (E) (NC2 with G = {k}) when the answer depends on x.

**Rests on.** Claim's inventions: I03, I14. Program's: I78, I79. **Reproduce.** `cd "/home/user/ThreadSmith/Semantics/results/S104 Round 2 - maths" && python3 -m model.run --claim FC62 --scale 4 --time-cap 45`

- **eliminative explanation** [computation] — *computed: as claimed*. E with k, λ(k) = {x} (deleted at the baseline) meets (E) on {(1,b0),(a_x,b0)} when the answer depends on x

  ```
  answers: baseline 0, a_x 1; conjuncts {'translates C': True, 'F1': True, 'F2eq': True, 'Hom': True, 'F2': True, 'A': True, 'NC1': True, 'NC2': True, 'NonVacuous': True}; NC2 witness (('a_x', 'b0'), ['k'])
  organization D_elim
    ports: u ∈ {0,1}; e ∈ {0,1}
    components: h_u on (u); x on (u,e); rest on (e)
    boundaries B = {b0}; edits A = {1,a_x}
    composition (other than with 1): a_x·a_x=undef
    L_h_u(1,b0) = {(1)}
    L_h_u(a_x,b0) = {(1)}
    L_x(1,b0) = full
    L_x(a_x,b0) = {(0,0) (1,1)}
    L_rest(1,b0) = {(0)}
    L_rest(a_x,b0) = full
  candidate ℰ_elim for p_noX: Γ = {k}, δ_E = e
    π: u := id(u); e := id(e)
    τ: 1↦1, a_x↦a_x; σ: b0↦b0
    λ(k) = ({x}, u:=id(u); e:=id(e))
    λ(k_u) = ({h_u}, u:=id(u))
    λ(k_rest) = ({rest}, e:=id(e))
  organization E_elim
    ports: u ∈ {0,1}; e ∈ {0,1}
    components: k_u on (u); k on (u,e); k_rest on (e)
    boundaries B = {b0}; edits A = {1,a_x}
    composition (other than with 1): a_x·a_x=undef
    L_k_u(1,b0) = {(1)}
    L_k_u(a_x,b0) = {(1)}
    L_k(1,b0) = full
    L_k(a_x,b0) = {(0,0) (1,1)}
    L_k_rest(1,b0) = {(0)}
    L_k_rest(a_x,b0) = full
  ```

### FC63 · Odd-order skew-symmetric matrices — COUNTEREXAMPLE FOUND

**The claim.** (a) For every odd n and every n×n M over ℝ (or GF(p), p odd) with Mᵀ = −M: det M = 0. (b) det I3 = 1; det [[0,1],[−1,0]] = 1. (c) With I66, the Leibniz candidate meets (F1), (F2), (A), NC2 and non-vacuity (the scope statement naming the edits to field arithmetic and to the determinant–invertibility link).

**Rests on.** Claim's inventions: I03, I27, I66. Program's: I81, I82, I99. **Reproduce.** `cd "/home/user/ThreadSmith/Semantics/results/S104 Round 2 - maths" && python3 -m model.run --claim FC63 --scale 4 --time-cap 45`

- **(a) odd skew-symmetric matrices are singular over GF(p), p odd** [computation] — *computed: as claimed*. det M = 0 for odd n, Mᵀ = −M

  ```
  matrices checked: 99547 (n ∈ {1,3,5}, p ∈ {3,5,7}; exhaustive where p^(n(n−1)/2) ≤ 60000, else 20000 drawn with seed 10463); nonsingular: 0
  ```

- **(b)** [computation] — *computed: as claimed*. det I3 = 1; det [[0,1],[−1,0]] = 1

  ```
  computed
  ```

- **(c-i) the Leibniz candidate, sum over every tuple of term values** [computation] — *computed: not as claimed*. the Leibniz candidate meets (F1), (F2), (A), NC2 and non-vacuity
  - Note: the sum component, relating every tuple of term values to their sum, differs from its counterpart's projection, which holds only the term tuples some matrix gives: (F1) fails for it
  - The counterexample is written out above, under Counterexamples.

- **(c-ii) the Leibniz candidate, sum restricted to realizable term tuples** [computation] — *computed: as claimed*. the Leibniz candidate meets (F1), (F2), (A), NC2 and non-vacuity

  ```
  Variant 'sum restricted to realizable term tuples': Account True {'translates C': True, 'F1': True, 'F2eq': True, 'Hom': True, 'F2': True, 'A': True, 'NC1': True, 'NC2': True, 'NonVacuous': True}, NC2 witness (('rb', 'b0'), ['order']).
  ```

### FC64 · Functional transport — HOLDS ON ALL MODELS TRIED

**The claim.** If π∘S_a = T_a∘π for each generator a, then π∘S_{an}⋯S_{a1} = T_{an}⋯T_{a1}∘π for every finite word whose intermediate scopes match.

**Rests on.** Claim's inventions: none. Program's: I77. **Reproduce.** `cd "/home/user/ThreadSmith/Semantics/results/S104 Round 2 - maths" && python3 -m model.run --claim FC64 --scale 4 --time-cap 45`

- **functional transport** [for all] — *holds on all models tried*. π∘S_a = T_a∘π for generators ⇒ for every word of length ≤ 4
  - Searched: sizes ports=3 dom≤3 comps=1 |B|=1 edits=0 … ports=3 dom≤3 comps=1 |B|=1 edits=0 (1 sizes, 80000 draws each); families: random maps on ≤ 3 states; seed 104641; 80000 models tried; 32532 of them meeting the claim's hypothesis.

### FC65 · Relational transport: simulations compose — HOLDS ON ALL MODELS TRIED

**The claim.** If R ⊆ Z_D × Z_E is a forward simulation for τ and R' ⊆ Z_E × Z_F one for τ', then R;R' is a forward simulation for τ'∘τ; likewise backward; where the codomain of R lies in the domain of R'.

**Rests on.** Claim's inventions: none. Program's: I77. **Reproduce.** `cd "/home/user/ThreadSmith/Semantics/results/S104 Round 2 - maths" && python3 -m model.run --claim FC65 --scale 4 --time-cap 45`

- **simulations compose** [for all] — *holds on all models tried*. forward (backward) simulations R, R' give a forward (backward) simulation R;R'
  - Searched: sizes ports=3 dom≤3 comps=1 |B|=1 edits=0 … ports=3 dom≤3 comps=1 |B|=1 edits=0 (1 sizes, 80000 draws each); families: random step relations on ≤ 3 states, one generator; seed 104651; 80000 models tried; 34479 of them meeting the claim's hypothesis.

### FC66 · (T2): the accumulated bound, and none without a modulus — HOLDS ON ALL MODELS TRIED

**The claim.** (a) e_{k+1} ≤ ε + L·e_k for k < n, so e_n ≤ ε Σ_{k<n} L^k. (b) There are S, T, π, d with one-step discrepancy ≤ ε everywhere, T not Lipschitz, and e_2 larger than any given number.

**Rests on.** Claim's inventions: none. Program's: I77. **Reproduce.** `cd "/home/user/ThreadSmith/Semantics/results/S104 Round 2 - maths" && python3 -m model.run --claim FC66 --scale 4 --time-cap 45`

- **(a) the accumulated bound** [for all] — *holds on all models tried*. one-step discrepancy ≤ ε on a scope closed under S, T L-Lipschitz ⇒ e_n ≤ ε Σ_{k<n} L^k (n ≤ 5)
  - Searched: sizes ports=1 dom≤1 comps=1 |B|=1 edits=0 … ports=1 dom≤1 comps=1 |B|=1 edits=0 (1 sizes, 80000 draws each); families: exact rationals; S a map of a finite scope; T(x) = ±Lx + c; seed 104661; 80000 models tried.

- **(b) no bound without a modulus** [computation] — *computed: as claimed*. there are S, T with one-step discrepancy ≤ ε on the scope, T not Lipschitz, and e_2 as large as one likes

  ```
  S(x) = x + 1/10, T(x) = x + 1/10 + K(x−1)², K = 10^6, scope {1}: e_1 = 0, e_2 = 10000
  ```

### FC67 · A declared invertible recoding keeps the content — HOLDS ON ALL MODELS TRIED

**The claim.** For an invertible recoding r of carrier values and a reader applying r⁻¹, the composite transport is faithful wherever the original was, and the carrier's provenance carries over (I54); so Rep is kept.

**Rests on.** Claim's inventions: I54, I70. Program's: I77, I78, I81. **Reproduce.** `cd "/home/user/ThreadSmith/Semantics/results/S104 Round 2 - maths" && python3 -m model.run --claim FC67 --scale 4 --time-cap 45`

- **an invertible recoding keeps fidelity** [for all] — *holds on all models tried*. E recoded by value bijections r, t' = r∘t: Faithful(t') ⟺ Faithful(t)
  - Searched: sizes ports=1 dom≤1 comps=1 |B|=1 edits=0 … ports=3 dom≤2 comps=3 |B|=2 edits=2 (108 sizes, 160 draws each); families: G-surg, G-free; seed 104671; 17280 models tried.

- **provenance carries over (I54)** [by construction] — *holds by construction*. the carrier's provenance carries over

  ```
  I54 is a rule of carrying over; nothing to search
  ```

### FC68 · A failed answer stays failed — HOLDS ON ALL MODELS TRIED

**The claim.** (a) Ans_E(τa,σb) = y ≠ Ans_p(a,b) ⇒ ¬A_ab ⇒ ¬Acc on p, and on every p' with the same D, Q and δ whose contract holds (a,b). (b) If j has a usable argument ruling out 'Ans_p(a,b) = y', the premise 'Ans_E(τa,σb) = y' is live and the forms are admitted, then X_j(Acc(ℰ)) ≠ ∅ for every such ℰ alike. (c) If a premise of that argument stops being live, the ruling out lapses for all alike, and Acc(ℰ) is unchanged.

**Rests on.** Claim's inventions: I20, I38, I40, I41. Program's: I77, I78, I81, I87, I89. **Reproduce.** `cd "/home/user/ThreadSmith/Semantics/results/S104 Round 2 - maths" && python3 -m model.run --claim FC68 --scale 4 --time-cap 45`

- **(a) a failed answer stays failed** [for all] — *holds on all models tried*. Ans_E(τa,σb) ≠ Ans_p(a,b) at (a,b) ∈ C ⇒ ¬Acc on p and on every p' with the same D, Q, δ whose contract holds (a,b)
  - Searched: sizes ports=1 dom≤1 comps=1 |B|=1 edits=0 … ports=3 dom≤2 comps=3 |B|=2 edits=2 (108 sizes, 160 draws each); families: G-surg, G-free; seed 104681; 17280 models tried; 6463 of them meeting the claim's hypothesis.

- **(b), (c) every such candidate alike** [computation] — *computed: as claimed*. a usable argument ruling out 'Ans_p(a,b) = y' rules out Acc for every candidate answering y; withdrawing its record lapses it for all alike

  ```
  (A) and each candidate's own answer y give 'acc_i → ans_is_y'. Usable and ruling out for both: True; after the record is withdrawn, usable for neither: True
  ```

### FC69 · (K2) is well founded; the loop read in S101 closes below the step — HOLDS ON ALL MODELS TRIED

**The claim.** Under I40, Usable_j(u) is defined by recursion on height; the loop K2 → Live → a step's usability → K2 (S101) closes on steps strictly below u. Under I40's alternative (any step of the argument), there are arguments where the definition has two fixed points: a root u' concluding d with premise e, and a step u below it concluding e with premise d — both usable or both not.

**Rests on.** Claim's inventions: I40. Program's: I87, I89. **Reproduce.** `cd "/home/user/ThreadSmith/Semantics/results/S104 Round 2 - maths" && python3 -m model.run --claim FC69 --scale 4 --time-cap 45`

- **I40: recursion below the step is well founded** [computation] — *computed: as claimed*. with Live through a step below, Usable has one value

  ```
  root ⊢ d from e; below it u ⊢ e from the leaf d; j accepts nothing. Usable (I40): False
  ```

- **I40's alternative: two fixed points** [computation] — *computed: as claimed*. with Live through any step of the argument, the usability operator has two fixed points

  ```
  least fixed point: 0 usable steps; greatest: 2
  ```

### FC70 · Withdrawing a premise that is live twice over leaves the step usable — HOLDS ON ALL MODELS TRIED

**The claim.** There is an argument with a step u and d ∈ Prem(u) such that d is also the conclusion of a usable step below u and d ∈ Accepted_j; after j withdraws d, Live_j(d;u) still holds through the first disjunct, and Usable_j(u) is unchanged. So the first clause holds of a premise live by acceptance only.

**Rests on.** Claim's inventions: I40, I41. Program's: I87, I89. **Reproduce.** `cd "/home/user/ThreadSmith/Semantics/results/S104 Round 2 - maths" && python3 -m model.run --claim FC70 --scale 4 --time-cap 45`

- **a premise live twice over** [computation] — *computed: as claimed*. withdrawing d leaves the step usable when d is also the conclusion of a usable step below

  ```
  argument:
    step [AndI] ⊢ (d ∧ q)
      step [MP] ⊢ d
        assumption leaf: q
        assumption leaf: (q → d)
      assumption leaf: q
  usable before j withdraws d: True; after: True. L393's 'Withdrawing a premise makes the step unusable' holds of a premise live by acceptance only.
  ```

### FC71 · (K3): a failed prediction rules out the conjunction, and nothing narrower — HOLDS ON ALL MODELS TRIED

**The claim.** (i) A usable argument concluding ¬O, a live conditional T∧B∧I ⇒ O and an admitted modus tollens give a usable argument ruling out T∧B∧I. (ii) From those premises alone no argument rules out T, B or I by itself: ¬O, (T∧B∧I ⇒ O) and T have a common model.

**Rests on.** Claim's inventions: I38, I43. Program's: I87, I89. **Reproduce.** `cd "/home/user/ThreadSmith/Semantics/results/S104 Round 2 - maths" && python3 -m model.run --claim FC71 --scale 4 --time-cap 45`

- **(i) the conjunction is ruled out** [computation] — *computed: as claimed*. usable ¬O, live conditional, modus tollens ⇒ T ∧ B ∧ I ruled out

  ```
    step [MT] ⊢ ¬(T ∧ B ∧ I)
      step [MP] ⊢ ¬O
        record leaf: rec
        assumption leaf: (rec → ¬O)
      assumption leaf: ((T ∧ B ∧ I) → O)
  ```

- **(ii) nothing narrower** [computation] — *computed: as claimed*. ¬O, (T∧B∧I ⇒ O) and each of T, B, I have a common model; no argument of height ≤ 3 from these premises rules out T, B or I

  ```
  common models: {'T': True, 'B': True, 'I': True}; arguments ruling out T, B, I: {'T': 0, 'B': 0, 'I': 0} (over 6 arguments)
  ```

### FC72 · The block on a premise that is the denial, and a premise taken as given — HOLDS ON ALL MODELS TRIED

**The claim.** (a) If ¬φ is a conjunct of a leaf (I39), then ¬RO(α,φ). (b) If a record leaf is MadeFrom ψ, then ¬RO(α,¬ψ). (c) The argument with leaves r and (r → ¬Acc(ℰ)) and one modus ponens step rules out Acc(ℰ): neither leaf has ¬Acc(ℰ) as a conjunct.

**Rests on.** Claim's inventions: I38, I39. Program's: I87, I89. **Reproduce.** `cd "/home/user/ThreadSmith/Semantics/results/S104 Round 2 - maths" && python3 -m model.run --claim FC72 --scale 4 --time-cap 45`

- **(a), (b), (c)** [computation] — *computed: as claimed*. (a) ¬φ a conjunct of a leaf blocks; (b) a record made from ψ does not rule out ¬ψ; (c) r and r → ¬Acc rule out Acc

  ```
  (a) True; (b) True; (c) True
  ```

### FC73 · Inconsistent accepted premises rule out a claim and its denial alike — HOLDS ON ALL MODELS TRIED

**The claim.** There are j and φ with X_j(φ) ≠ ∅ and X_j(¬φ) ≠ ∅ (for example Accepted_j ⊇ {q, q → ¬φ, s, s → φ}, modus ponens admitted).

**Rests on.** Claim's inventions: I38. Program's: I87, I89. **Reproduce.** `cd "/home/user/ThreadSmith/Semantics/results/S104 Round 2 - maths" && python3 -m model.run --claim FC73 --scale 4 --time-cap 45`

- **inconsistent premises** [computation] — *computed: as claimed*. X_j(φ) ≠ ∅ and X_j(¬φ) ≠ ∅

  ```
  Accepted_j = {q, q→¬φ, s, s→φ}
  ```

### FC74 · A criticism occurrence can exist without bearing — HOLDS ON ALL MODELS TRIED

**The claim.** The data of a criticism (target z, alleged defect δ, premise g, connection, an occurrence in a history) are defined without Acc; so there are models with a criticism occurrence c and ¬Acc(ℰ_c), that is ¬Bearing(c,z,p).

**Rests on.** Claim's inventions: I45. Program's: I77, I78, I81. **Reproduce.** `cd "/home/user/ThreadSmith/Semantics/results/S104 Round 2 - maths" && python3 -m model.run --claim FC74 --scale 4 --time-cap 45`

- **a criticism without bearing** [there is] — *witness found*. a criticism whose connection candidate has ¬Acc
  - Searched: sizes ports=1 dom≤1 comps=1 |B|=1 edits=0 … ports=3 dom≤2 comps=3 |B|=2 edits=2 (108 sizes, 40 draws each); families: G-surg, G-free; seed 104741; 1 models tried; first found at size ports=1 dom≤1 comps=1 |B|=1 edits=0.

  ```
  the connection's candidate fails (E): Bearing fails while the criticism occurrence (its data) exists
  candidate ℰ for p: Γ = {k0}, δ_E = p0
    π: p0 := id(p0)
    τ: 1↦1; σ: b0↦b0
    λ(k0) = ({h_p0}, p0:=id(p0))
  organization E_ℰ
    ports: p0 ∈ {0}
    components: k0 on (p0); bg on (p0)
    boundaries B = {b0}; edits A = {1}
    L_k0(1,b0) = {}
    L_bg(1,b0) = {(0)}
  ```

### FC75 · Active routes: the excluded routes fail the definition's own clauses — HOLDS ON ALL MODELS TRIED

**The claim.** Under I46: (a) a route none of whose occurrences lies on a ≺_h-chain to r inside it fails the join clause; (b) a route whose value at r does not change when i's port is set across the declared contrasts fails the dependence clause; (c) activity is a function of (h, Org_ℓ(h), i, r, K), not of r's value alone.

**Rests on.** Claim's inventions: I44, I46. Program's: I95. **Reproduce.** `cd "/home/user/ThreadSmith/Semantics/results/S104 Round 2 - maths" && python3 -m model.run --claim FC75 --scale 4 --time-cap 45`

- **(a) a member on no chain to r** [computation] — *computed: as claimed*. a route with a member off every chain from i to r fails

  ```
  side is on no chain from i to r inside R
  ```

- **(b) no dependence** [computation] — *computed: as claimed*. a route whose value at r does not change with i's port fails

  ```
  no dependence on the declared contrasts
  ```

- **(c) a function of (h, Org, i, r, K)** [by construction] — *holds by construction*. activity is not read from r's value alone

  ```
  act_route takes the circuit, R, i, r and K
  ```

- **a route at rest before the result** [look] — *look: as expected*. the look: a route that ran early and whose product persists and feeds r is joined to r, and D11.4 counts it active

  ```
  i → m ran at step 1; m's product persists (an edge m → r across time, no process between) and r occurs at step 9 after 'late'. D11.4 (I46): True (dependence on the contrast (0, 1)). L375 says a route 'already at rest when the result occurred, is not active'; D11.4 does not exclude this one.
  ```

### FC76 · Reason use gives neither bearing nor usability — HOLDS ON ALL MODELS TRIED

**The claim.** Under I47, UsesReason is defined without Acc and without Usable_j; there are models with UsesReason and ¬Bearing, and with UsesReason and no usable argument from the objection.

**Rests on.** Claim's inventions: I47. Program's: I47, I90. **Reproduce.** `cd "/home/user/ThreadSmith/Semantics/results/S104 Round 2 - maths" && python3 -m model.run --claim FC76 --scale 4 --time-cap 45`

- **reason use without bearing** [computation] — *computed: as claimed*. UsesReason ∧ ¬Bearing; and no usable argument from the objection is involved

  ```
  response on an active route: True; the criticism's connection meets (E): False. UsesReason takes no Acc and no Usable.
  ```

### FC77 · Without a physical witness, selection is met by every transport — COUNTEREXAMPLE FOUND

**The claim.** Read with no physical witness: for every t, Sel(t; {t}, id, ∅) holds (fidelity on ∅ is vacuous, and an empty history holds nothing that represents). Then (R) reduces to 'some faithful transport exists'. With I52, Sel needs a physical selection history; test which of I52's requirements block the trivial witness.

**Rests on.** Claim's inventions: I48, I52. Program's: I77, I78, I81, I90. **Reproduce.** `cd "/home/user/ThreadSmith/Semantics/results/S104 Round 2 - maths" && python3 -m model.run --claim FC77 --scale 4 --time-cap 45`

- **with H = ∅ and an empty selection history** [for all] — *counterexample found*. every transport t has Sel(t; {t}, id, ∅) when Θ admits t (fidelity on ∅ vacuous)
  - Searched: sizes ports=1 dom≤1 comps=1 |B|=1 edits=0 … ports=3 dom≤2 comps=3 |B|=2 edits=2 (108 sizes, 80 draws each); families: G-surg, G-free; seed 104771; 494 models tried; first found at size ports=1 dom≤1 comps=1 |B|=1 edits=2.
  - The counterexample is written out above, under Counterexamples.

- **the trivial witness exactly when τ is a homomorphism** [for all] — *holds on all models tried*. Sel(t; {t}, id, ∅) ⟺ Hom(τ), when Θ admits t
  - Searched: sizes ports=1 dom≤1 comps=1 |B|=1 edits=0 … ports=3 dom≤2 comps=3 |B|=2 edits=2 (108 sizes, 80 draws each); families: G-surg, G-free; seed 104772; 8640 models tried.

- **which of I52's requirements block the trivial witness** [computation] — *computed: as claimed*. the empty selection history meets every requirement of I52 but Θ's admission of t (and Hom(τ))

  ```
  With H = ∅: 'the pairs of H occur', (F1) and the (F2) equation on H are vacuous; an empty history has no occurrence, so none represents t, H or the survival condition. What remains is Hom(τ) (not pair-relative, I18) and 'the members of 𝒯 are admitted by the physics' (L481), which the formal core leaves to Θ; nothing requires H or h_sel to be nonempty. So (R) keeps content from 'selected' only through Θ's admission of t, through Hom, or through a requirement of a nonempty history, which the text does not state.
  ```

### FC78 · Exactly one of three provenances — COUNTEREXAMPLE FOUND

**The claim.** Under I53, Sel(t) ∧ Con(t) is impossible and Dec(t) := ¬Sel ∧ ¬Con, so exactly one holds. Under I53's alternative there are histories with Sel on one part and Con on another. Per part (I54), exactly one holds of each part.

**Rests on.** Claim's inventions: I52, I53, I54. Program's: I90, I92. **Reproduce.** `cd "/home/user/ThreadSmith/Semantics/results/S104 Round 2 - maths" && python3 -m model.run --claim FC78 --scale 4 --time-cap 45`

- **exactly one provenance under I53** [computation] — *computed: not as claimed*. Sel(t) ∧ Con(t) is impossible on one history
  - The counterexample is written out above, under Counterexamples.

### FC79 · Survival is how the transport got there; fidelity is what it is — HOLDS ON ALL MODELS TRIED

**The claim.** Faithful_C(t) is a function of (D, E, t, C); Sel(t;𝒯,μ,H) of (t, 𝒯, μ, H, the selection history). No clause of Faithful takes 𝒯, μ or H, so two transports alike in (D, E, t) have the same Faithful value on every C.

**Rests on.** Claim's inventions: I49, I52. Program's: none. **Reproduce.** `cd "/home/user/ThreadSmith/Semantics/results/S104 Round 2 - maths" && python3 -m model.run --claim FC79 --scale 4 --time-cap 45`

- **fidelity takes no population** [by construction] — *holds by construction*. Faithful_C(t) is a function of (D, E, t, C)

  ```
  core.faithful(cand) reads cand and its question only
  ```

### FC80 · Argument 3: underdetermination where the population leaves room — HOLDS ON ALL MODELS TRIED

**The claim.** (a) If t, t' ∈ 𝒯 both survive on H and value_t(a,b) ≠ value_t'(a,b) (I71) for (a,b) ∈ C∖H, the survival condition does not separate them. (b) If all survivors on H agree at (a,b), that value is a function of (𝒯, H). (c) The step 'altered at one pair gives another admitted relation' uses I02; under an action law, an alteration at one pair can force others, and (a)'s hypothesis is harder to meet.

**Rests on.** Claim's inventions: I02, I52, I71. Program's: I77, I78, I81. **Reproduce.** `cd "/home/user/ThreadSmith/Semantics/results/S104 Round 2 - maths" && python3 -m model.run --claim FC80 --scale 4 --time-cap 45`

- **(a), (b) the survivors on H fix what they share** [for all] — *holds on all models tried*. all survivors on H agree at (a,b) ⇒ that value is a function of (𝒯, H)
  - Searched: sizes ports=1 dom≤1 comps=1 |B|=1 edits=0 … ports=3 dom≤2 comps=3 |B|=2 edits=2 (108 sizes, 120 draws each); families: G-surg, G-free; seed 104801; 7383 models tried.

- **(a) underdetermination** [there is] — *witness found*. some (a,b) ∈ C∖H at which survivors on H differ
  - Searched: sizes ports=1 dom≤1 comps=1 |B|=1 edits=0 … ports=3 dom≤2 comps=3 |B|=2 edits=2 (108 sizes, 240 draws each); families: G-surg, G-free; seed 104802; 1 models tried; first found at size ports=1 dom≤1 comps=1 |B|=1 edits=1.

  ```
  underdetermined at (e1,b0): 2 survivors on H = {(1,b0)} with different values there
  question p: target D, b0 = b0, query Q_w (reads the designated port) designating p0, C = {(1,b0), (e1,b0)}
  ```

- **(c) under an action law** [not tested] — *not tested*. an alteration at one pair forces others, and (a)'s hypothesis is harder to meet
  - Why not: comparing I02 with an action law needs a population family closed under an action law; not built in this round

### FC81 · Argument 4, and who can be surprised — COUNTEREXAMPLE FOUND

**The claim.** Surp(t;a,b) := Sel(t) ∧ Viol(t;a,b) ∧ (a,b) ∈ C∖H ∧ Occurs(a,b). (a) Surp ⇒ H ⊊ C. (b) No transport ⇒ no Surp. (c) H = C ⇒ no Surp. (d) Con(t) ∧ Viol ⇒ ¬Surp (I53).

**Rests on.** Claim's inventions: I50, I52, I53. Program's: I90, I92. **Reproduce.** `cd "/home/user/ThreadSmith/Semantics/results/S104 Round 2 - maths" && python3 -m model.run --claim FC81 --scale 4 --time-cap 45`

- **(a)-(c)** [by construction] — *holds by construction*. Surp ⇒ H ⊊ C; no transport ⇒ no Surp; H = C ⇒ no Surp

  ```
  Surp needs (a,b) ∈ C∖H with H ⊆ C (Sel), and a transport; each follows from D12.7 as written
  ```

- **(d) Con(t) ∧ Viol ⇒ ¬Surp (under I53)** [computation] — *computed: not as claimed*. a constructed transport violated at an occurring pair is not surprised
  - The counterexample is written out above, under Counterexamples.

### FC82 · The two responses to a violation have no common result — COUNTEREXAMPLE FOUND

**The claim.** SelResp(t → t'): t' ∈ 𝒯, reached from t by μ, surviving on H ∪ {(a,b)}; ConResp(→ t''): t'' or its codomain new, with Con(t''). Under I53 no transport is the result of both (Sel(t') excludes Con(t')).

**Rests on.** Claim's inventions: I52, I53. Program's: I90, I92. **Reproduce.** `cd "/home/user/ThreadSmith/Semantics/results/S104 Round 2 - maths" && python3 -m model.run --claim FC82 --scale 4 --time-cap 45`

- **no common result** [computation] — *computed: not as claimed*. no transport is the result of both a selection response and a construction response
  - The counterexample is written out above, under Counterexamples.

### FC83 · Only the construction response can be originative — COUNTEREXAMPLE FOUND

**The claim.** Claim to test: SelResp(t → t') ⇒ ¬Origin(s,c',p,h,e) for the content c' that t' carries to. (G) needs Build, and Build needs a subhistory that prepares a represented organization for explanatory use of c' (I56). Sel(t') forbids occurrences that represent t', H or the survival condition (L195), not the organization t' carries to (which Con names, L197).

**Rests on.** Claim's inventions: I52, I56. Program's: I90, I92. **Reproduce.** `cd "/home/user/ThreadSmith/Semantics/results/S104 Round 2 - maths" && python3 -m model.run --claim FC83 --scale 4 --time-cap 45`

- **only construction is originative** [computation] — *computed: not as claimed*. SelResp(t → t') ⇒ ¬Origin(s, c', …)
  - The counterexample is written out above, under Counterexamples.

### FC84 · Every creative attribution requires construction — HOLDS ON ALL MODELS TRIED

**The claim.** Origin ⇒ Build; CreateEx ⇒ Origin ⇒ Build; the creative-episode class (L528) needs an instance of (G), hence Build; Build's subhistory is what a construction trace identifies (L405). Separate traces: Sel's history holds no represented target (L195), Con's holds one (L197).

**Rests on.** Claim's inventions: I53, I56. Program's: none. **Reproduce.** `cd "/home/user/ThreadSmith/Semantics/results/S104 Round 2 - maths" && python3 -m model.run --claim FC84 --scale 4 --time-cap 45`

- **every creative attribution requires Build** [by construction] — *holds by construction*. Origin ⇒ Build; CreateEx ⇒ Origin ⇒ Build

  ```
  Build is a conjunct of (G) (D13.6) and (G) is a conjunct of (EX) (D14.7)
  ```

### FC85 · A content matches itself; the matching is read one way — HOLDS ON ALL MODELS TRIED

**The claim.** Under I48: (a) c ≡_ℓ c (the identity transport both ways), so c ∈ R_<e ⇒ ¬New. (b) d ≡_ℓ c (on C_c) can hold while c ≡_ℓ d (on C_d) fails; (N) uses only d ≡_ℓ c with c fixed.

**Rests on.** Claim's inventions: I48. Program's: I48, I77, I78, I81. **Reproduce.** `cd "/home/user/ThreadSmith/Semantics/results/S104 Round 2 - maths" && python3 -m model.run --claim FC85 --scale 4 --time-cap 45`

- **(a) c ≡ c** [for all] — *holds on all models tried*. the identity transport c → c is faithful on C_c
  - Searched: sizes ports=1 dom≤1 comps=1 |B|=1 edits=0 … ports=3 dom≤2 comps=3 |B|=2 edits=2 (108 sizes, 160 draws each); families: G-surg, G-free; seed 104851; 17280 models tried.

- **(b) the matching is read one way (random)** [there is] — *no witness found*. d ≡ c on C_c while c ≡ d on C_d fails
  - Searched: sizes ports=1 dom≤1 comps=1 |B|=1 edits=0 … ports=2 dom≤2 comps=2 |B|=1 edits=2 (24 sizes, 160 draws each); families: G-free; ≡ decided over the transport space π, λ the identity, τ and σ every map (a restriction, I81); seed 104852; 2560 models tried.

- **(b) the matching is read one way (constructed)** [computation] — *computed: as claimed*. d ≡ c on C_c while c ≡ d on C_d fails
  - Note: c ≡ d fails over the transport space searched; that no transport at all exists is not shown

  ```
  d ≡ c holds and c ≡ d fails (over the transport space searched: π, λ the identity, τ, σ every map)
  d's contract: {(1,b0), (e,b0)}
  c's contract: {(1,b0)}
  organization E_d
    ports: x ∈ {0,1}
    components: k on (x)
    boundaries B = {b0}; edits A = {1,e}
    composition (other than with 1): e·e=undef
    L_k(1,b0) = {(0)}
    L_k(e,b0) = {(1)}
  organization E_c
    ports: x ∈ {0,1}
    components: k on (x)
    boundaries B = {b0}; edits A = {1,e}
    composition (other than with 1): e·e=undef
    L_k(1,b0) = {(0)}
    L_k(e,b0) = {(0)}
  ```

### FC86 · Repair: a protected aim failed in between is lost — HOLDS ON ALL MODELS TRIED

**The claim.** Under I57: a protected r met at ξ and at ξ' and failed on a covered occasion between them makes (P) fail; r is lost ⟺ it fails on a covered occasion in [ξ, ξ'].

**Rests on.** Claim's inventions: I57. Program's: I96. **Reproduce.** `cd "/home/user/ThreadSmith/Semantics/results/S104 Round 2 - maths" && python3 -m model.run --claim FC86 --scale 4 --time-cap 45`

- **every condition, occasion set and pair of times on 4 times** [for all] — *holds on all models tried*. a protected r met at ξ and failed on a covered occasion between makes (P) fail; r lost ⟺ it fails on a covered occasion in [ξ, ξ']
  - Searched: exhaustive: all conditions and occasion sets on times 0..3, all ξ ≤ ξ'; 2560 models tried.

- **a protected aim already failing at ξ** [look] — *look: as expected*. (outside FC86) a protected aim that fails at a covered ξ counts as lost by 'fails on an occasion it covers' and is not protected by (P)

  ```
  cond false at ξ = 0 (covered), true after: r(ξ) on the left is false, so (P) asks nothing of r, while 'r fails on a covered occasion in [ξ, ξ']' holds: under I57 'lost' in L441 and (P)'s protection differ for an aim already failing at ξ.
  ```

### FC87 · Two sufficient contributions that both ran are both attributed — HOLDS ON ALL MODELS TRIED

**The claim.** ProducedBy attributes the repair to each Δ_i with an active route to it; with two such, both; no function from the history to shares of attribution is defined (a weighting is a declared input, L522).

**Rests on.** Claim's inventions: I46, I57. Program's: none. **Reproduce.** `cd "/home/user/ThreadSmith/Semantics/results/S104 Round 2 - maths" && python3 -m model.run --claim FC87 --scale 4 --time-cap 45`

- **both contributions attributed** [by construction] — *holds by construction*. ProducedBy attributes the repair to each contribution with an active route to it

  ```
  Attr(o) is a set (D14.3); no share function is defined
  ```

### FC88 · Losses outside P are exposed in the claim, not in (P) — HOLDS ON ALL MODELS TRIED

**The claim.** Under I58: a repair claim with aims O, P, Aims* and exposure record X is well formed ⟺ {r ∈ Aims*∖P : r(ξ) ∧ ¬r(ξ')} ⊆ X. The condition bears on the claim: (P) can hold while the claim is not well formed.

**Rests on.** Claim's inventions: I57, I58. Program's: I96. **Reproduce.** `cd "/home/user/ThreadSmith/Semantics/results/S104 Round 2 - maths" && python3 -m model.run --claim FC88 --scale 4 --time-cap 45`

- **(P) holds, the claim is not well formed** [computation] — *computed: as claimed*. a repair claim can meet (P) and fail WellFormed

  ```
  O repaired between ξ = 0 and ξ' = 1, P kept, and an aim of Aims*∖P met at ξ and lost by ξ' with an empty exposure record: (P) True, WellFormed False
  ```

### FC89 · L443 (after round 1) puts 'deployable' where Deploy's type allows it — NOT TESTED

**The claim.** Deploy takes a content (L403). Under the old wording a correction (a subhistory with changes, L435) was asked to be deployable, a mismatch of type. Under the new wording (I59) both kinds of explanatory aim put Deploy on the account c, which is what (EX) asks for every o ∈ O_ex. (EX) has no condition that tells the two kinds apart; the second kind is carried only by ProducesVia.

**Rests on.** Claim's inventions: I59, I60. Program's: none. **Reproduce.** `cd "/home/user/ThreadSmith/Semantics/results/S104 Round 2 - maths" && python3 -m model.run --claim FC89 --scale 4 --time-cap 45`

- **L443's two kinds of explanatory aim** [not tested] — *not tested*. Deploy's type against L443's wording
  - Why not: a reading of the wording of L443 against Deploy's typing

### FC90 · The worked case's '(EX) is met' against (EX)'s conjuncts — NOT TESTED

**The claim.** (EX) needs: CreativeCriticalEpisode(s,Δ,h,e); Repair; o ∈ O_ex with ¬o(ξ) ∧ o(ξ'); Origin(s,c,p_c,h,e_c) with e_c ⪯_h e; Account; c ∈ Result(Δ); Deploy(s,c,ξ';U_c); ProducesVia(Δ,c,o;ξ,ξ'). L628 states (G)'s Build and New (not Attempt), (P), Account and 'deployable'. Test which of CreativeCriticalEpisode (L429's four parts), Attempt, c ∈ Result(Δ), ProducesVia and e_c ⪯_h e the worked case's description gives, and which it leaves to be read in.

**Rests on.** Claim's inventions: I44, I57, I59, I60, I68. Program's: none. **Reproduce.** `cd "/home/user/ThreadSmith/Semantics/results/S104 Round 2 - maths" && python3 -m model.run --claim FC90 --scale 4 --time-cap 45`

- **the worked case's '(EX) is met'** [not tested] — *not tested*. which conjuncts of (EX) the worked case's description gives
  - Why not: a reading of L620–L628; the model does not encode the worked case's history

### FC91 · (CT1) is C ⊆ F(C) only with (CT1)'s completion read into F — HOLDS ON ALL MODELS TRIED

**The claim.** Under I61: RetReal(π,T,C;χ) ⟺ C ⊆ F(C). With 'complete' read without the output condition, C ⊆ F(C) follows from RetReal and is weaker than it.

**Rests on.** Claim's inventions: I61. Program's: I97. **Reproduce.** `cd "/home/user/ThreadSmith/Semantics/results/S104 Round 2 - maths" && python3 -m model.run --claim FC91 --scale 4 --time-cap 45`

- **(CT1) ⟺ C ⊆ F(C) under I61** [for all] — *holds on all models tried*. RetReal(π,T,C) ⟺ C ⊆ F(C), 'complete' read as (CT1)'s completion
  - Searched: sizes ports=1 dom≤1 comps=1 |B|=1 edits=0 … ports=1 dom≤1 comps=1 |B|=1 edits=0 (1 sizes, 12000 draws each); families: random executions on ≤ 4 states; seed 104911; 12000 models tried.

- **the other reading is weaker** [there is] — *witness found*. with 'complete' read without the output condition, C ⊆ F(C) does not give RetReal
  - Searched: sizes ports=1 dom≤1 comps=1 |B|=1 edits=0 … ports=1 dom≤1 comps=1 |B|=1 edits=0 (1 sizes, 12000 draws each); families: random executions; seed 104912; 2 models tried; first found at size ports=1 dom≤1 comps=1 |B|=1 edits=0.

  ```
  C = [0, 1, 2]: C ⊆ F'(C) (complete without the output condition) and ¬RetReal; T = {0: {1, 2}, 1: {0, 1}}; executions {(0, 0): [(True, 0, 1), (True, 1, 0)], (0, 1): [(True, 1, 1), (True, 2, 2)], (1, 0): [(True, 2, 1)], (1, 1): [(True, 1, 2)], (2, 0): [(True, 1, 2)], (2, 1): [(True, 0, 1)]}
  ```

### FC92 · (CT2): monotone F and its greatest fixed point — HOLDS ON ALL MODELS TRIED

**The claim.** (a) X ⊆ Y ⇒ F(X) ⊆ F(Y). (b) U := ∪{D ⊆ Z : D ⊆ F(D)} has F(U) = U and contains every fixed point (the Knaster–Tarski construction on P(Z)). (c) The D of (b) is bound in the clause and is not a question's target. (d) (CT2) has no counterexample under either reading of 'complete', since monotonicity does not use the output condition.

**Rests on.** Claim's inventions: I61. Program's: I97. **Reproduce.** `cd "/home/user/ThreadSmith/Semantics/results/S104 Round 2 - maths" && python3 -m model.run --claim FC92 --scale 4 --time-cap 45`

- **(CT2)** [for all] — *holds on all models tried*. F monotone; U = ∪{D ⊆ F(D)} is the greatest fixed point; under both readings of 'complete'
  - Searched: sizes ports=1 dom≤1 comps=1 |B|=1 edits=0 … ports=1 dom≤1 comps=1 |B|=1 edits=0 (1 sizes, 12000 draws each); families: random executions on ≤ 4 states; seed 104921; 12000 models tried.

### FC93 · (CT3), (CT4), and capability at one tolerance — HOLDS ON ALL MODELS TRIED

**The claim.** (a) Under I62, Cap^{q,r} ⊆ Admit^{q,r}. (b) Intersecting over (q,r): Cap^∞ ⊆ Poss. (c) There are models with T ∈ Cap^{q,r} and T ∉ Poss.

**Rests on.** Claim's inventions: I62. Program's: I98. **Reproduce.** `cd "/home/user/ThreadSmith/Semantics/results/S104 Round 2 - maths" && python3 -m model.run --claim FC93 --scale 4 --time-cap 45`

- **(a) CT3, (b) CT4** [for all] — *holds on all models tried*. Cap^{q,r} ⊆ Admit^{q,r}; Cap^∞ ⊆ Poss
  - Searched: sizes ports=1 dom≤1 comps=1 |B|=1 edits=0 … ports=1 dom≤1 comps=1 |B|=1 edits=0 (1 sizes, 12000 draws each); families: random antitone task families on a 3×3 tolerance grid; seed 104931; 12000 models tried.

- **(c) capability at one tolerance** [there is] — *witness found*. T ∈ Cap^{q,r} and T ∉ Poss
  - Searched: sizes ports=1 dom≤1 comps=1 |B|=1 edits=0 … ports=1 dom≤1 comps=1 |B|=1 edits=0 (1 sizes, 2000 draws each); families: random antitone task families; seed 104932; 2 models tried; first found at size ports=1 dom≤1 comps=1 |B|=1 edits=0.

  ```
  T ∈ Cap^(0, 0) and T ∉ Poss: [3]
  ```

### FC94 · Recursion does not entail universality — NOT TESTED

**The claim.** (a) There is a model of RC with ¬UU. (b) With 𝔈_Θ infinite (I75), no finite set of performed tasks decides UU.

**Rests on.** Claim's inventions: I74, I75. Program's: none. **Reproduce.** `cd "/home/user/ThreadSmith/Semantics/results/S104 Round 2 - maths" && python3 -m model.run --claim FC94 --scale 4 --time-cap 45`

- **recursion and universality** [not tested] — *not tested*. a model of RC with ¬UU; no finite set of performed tasks decides UU
  - Why not: RC, UU, Enable, target chains and 𝔈_Θ have no finite semantics without Θ; a model would be an assignment of free predicates, which shows only that no axiom links them (as FC110)

### FC95 · A system can represent a theory in error — HOLDS ON ALL MODELS TRIED

**The claim.** There are o, a content c = (E_c, C_c, Γ_c) and its target D_c with Rep_ℓ(o,c) and ¬Faithful for the candidate's transport t_c: D_c → E_c.

**Rests on.** Claim's inventions: I48, I52. Program's: I90, I92. **Reproduce.** `cd "/home/user/ThreadSmith/Semantics/results/S104 Round 2 - maths" && python3 -m model.run --claim FC95 --scale 4 --time-cap 45`

- **a system can represent a theory in error** [computation] — *computed: as claimed*. Rep_ℓ(o, c) and ¬Faithful for the candidate's transport t_c: D_c → E_c

  ```
  o instantiates E_wrong (L = 2H, Θ supplied by hand); the identity transport o → c is faithful on c's contract: True; Con set true by hand (I90); t_c from the pole to E_wrong is faithful: False
  ```

### FC96 · Argument 2: same counterparts, one account — HOLDS ON ALL MODELS TRIED

**The claim.** (i) A_C(ℰ) ∧ A_C(ℰ') ⇒ Ans_E(τa,σb) = Ans_E'(τ'a,σ'b) on C. (ii) If φ: Γ → Γ' is a bijection with λ'(φk) = λ(k), θ_k and θ'_φk with the same image, and F1_C for both, then β_k := θ'_φk⁻¹∘θ_k is a footprint bijection under which the signatures of k and φk read through t, t' coincide on C, when the value maps agree (I14); with different value maps they coincide only up to recoding values (I10's alternative).

**Rests on.** Claim's inventions: I10, I12, I14. Program's: I77, I78, I81. **Reproduce.** `cd "/home/user/ThreadSmith/Semantics/results/S104 Round 2 - maths" && python3 -m model.run --claim FC96 --scale 4 --time-cap 45`

- **(i) (A) for both ⇒ equal answers** [for all] — *holds on all models tried*. A_C(ℰ) ∧ A_C(ℰ') ⇒ equal answers on C
  - Searched: sizes ports=1 dom≤1 comps=1 |B|=1 edits=0 … ports=3 dom≤2 comps=2 |B|=2 edits=1 (48 sizes, 80 draws each); families: G-surg, G-free; seed 104961; 3835 models tried; 1731 of them meeting the claim's hypothesis.

- **(ii) same counterparts give one kind** [for all] — *holds on all models tried*. φ: Γ → Γ' with λ'(φk) = λ(k), same images and value maps, F1 for both ⇒ k and φk of one kind on C through t, t'
  - Searched: sizes ports=1 dom≤1 comps=1 |B|=1 edits=0 … ports=3 dom≤2 comps=3 |B|=2 edits=2 (108 sizes, 160 draws each); families: G-surg, G-free; seed 104962; 17280 models tried.

### FC97 · Argument 5: a contract can be an organization and a content — HOLDS ON ALL MODELS TRIED

**The claim.** Under I67, D_C (membership ports, a query port, closure components, setting edits) is an organization in the sense of (O): nonempty domains, footprints, a partial composition with identity, a relation for every (j,a,b). With a contract on D_C (I48), Deploy, Build, New and (G) take it as a content.

**Rests on.** Claim's inventions: I01, I48, I67. Program's: I67. **Reproduce.** `cd "/home/user/ThreadSmith/Semantics/results/S104 Round 2 - maths" && python3 -m model.run --claim FC97 --scale 4 --time-cap 45`

- **a contract as an organization** [computation] — *computed: as claimed*. D_C (membership ports, a query port, closure components, setting edits) meets (O)'s typing and I01's partial monoid laws

  ```
  nonempty domains True; identity True; associativity (total here) True; relations on footprints True; 27 edits
  ```

- **Deploy, Build, New and (G) take it as a content** [not tested] — *not tested*. a contract as a content
  - Why not: needs Θ (I90); the typing check above is what the model can do

### FC98 · Argument 6 and the dependence order: acyclic, and ending where the text says — NOT TESTED

**The claim.** Graph: nodes the defined symbols of the formal core; an edge from a definition to each symbol it uses. Test (a) acyclicity (S101 read two loops from the wording: build–prov–rep, and K2–arg–livej, which FC69 closes under I40); (b) every sink is Θ (with Org_ℓ), 𝒩, (O), (Q), an index, or a declared input of L522. Symbols the formal core uses that are none of these on their face: Offered (I33), the restriction operation (I29), Integrated and Nontrivial (I55), Prepares, BindingConstruction, TransferComposite (I56), MadeFrom (I39), Applies (I34), Aims* (I58), O_ex (I59), the contrasts K (I46), Rule, Rec, Chg (I47), Occurs (§12), the designation δ (I20). For each: a claim read through Θ, or a primitive the text does not list?

**Rests on.** Claim's inventions: I20, I29, I33, I34, I39, I46, I47, I55, I56, I58, I59. Program's: none. **Reproduce.** `cd "/home/user/ThreadSmith/Semantics/results/S104 Round 2 - maths" && python3 -m model.run --claim FC98 --scale 4 --time-cap 45`

- **the dependence graph** [not tested] — *not tested*. acyclic, ending in Θ, 𝒩, (O), (Q), indices and declared inputs
  - Why not: a property of the definitions' dependence graph (D18.1), not of models

### FC99 · Argument 7: an account on C can fail on C' — HOLDS ON ALL MODELS TRIED

**The claim.** There are D, C, C', Q and ℰ with Acc on (D, C, …) and ¬Acc on (D, C', …); for example the pole's forward candidate with C1 and with C' adding an edit at which its τ gives the wrong edit of E.

**Rests on.** Claim's inventions: I65. Program's: I92. **Reproduce.** `cd "/home/user/ThreadSmith/Semantics/results/S104 Round 2 - maths" && python3 -m model.run --claim FC99 --scale 4 --time-cap 45`

- **an account on C can fail on C'** [computation] — *computed: as claimed*. the forward candidate with τ shifting the settings of L: Acc on C1, ¬Acc on C1 ∪ {(set(L=1),b0)}

  ```
  on C1: {'translates C': True, 'F1': True, 'F2eq': True, 'Hom': True, 'F2': True, 'A': True, 'NC1': True, 'NC2': True, 'NonVacuous': True}; on C1': {'translates C': True, 'F1': False, 'F2eq': False, 'Hom': True, 'F2': False, 'A': False, 'NC1': True, 'NC2': True, 'NonVacuous': True} (τ is a homomorphism: Hom = True)
  ```

### FC100 · Argument 8: structure-preserving bijections keep (E), (G), (P), (EX) — HOLDS ON ALL MODELS TRIED

**The claim.** Under I70: Acc(φ·ℰ) = Acc(ℰ), and (G), (P), (EX) are kept, for every structure-preserving bijection φ of all the data, NC1's answer slot and the stated scope carried along. Testable on random isomorphic copies of finite models.

**Rests on.** Claim's inventions: I45, I70. Program's: I70, I77, I78, I81. **Reproduce.** `cd "/home/user/ThreadSmith/Semantics/results/S104 Round 2 - maths" && python3 -m model.run --claim FC100 --scale 4 --time-cap 45`

- **(E) is kept by structure-preserving bijections** [for all] — *holds on all models tried*. Acc(φ·ℰ) = Acc(ℰ) for random isomorphic copies of D and E (ports, components, edits, boundaries)
  - Searched: sizes ports=1 dom≤1 comps=1 |B|=1 edits=0 … ports=3 dom≤2 comps=3 |B|=2 edits=2 (108 sizes, 120 draws each); families: G-surg, G-free; seed 105001; 12960 models tried.

- **(G), (P), (EX)** [not tested] — *not tested*. kept by every structure-preserving bijection
  - Why not: need histories and Θ; not modelled beyond free predicates

### FC101 · Argument 9: an input–output description does not fix an account — HOLDS ON ALL MODELS TRIED

**The claim.** (a) For any function f of the projection P: P(M0) = P(M1) ⇒ f(M0) = f(M1). (b) Construct M0 (two parallel routes to the output) and M1 (a priority route with a fallback) with equal input–output projections, a question whose contract holds edits deleting internal components, and a candidate that meets (E) for one and not the other.

**Rests on.** Claim's inventions: I29, I46. Program's: I29, I78. **Reproduce.** `cd "/home/user/ThreadSmith/Semantics/results/S104 Round 2 - maths" && python3 -m model.run --claim FC101 --scale 4 --time-cap 45`

- **(a) a function of the projection** [by construction] — *holds by construction*. P(M0) = P(M1) ⇒ f(M0) = f(M1)

  ```
  a function of the projection sees nothing else
  ```

- **(b) equal input-output behaviour, different accounts** [computation] — *computed: as claimed*. M0 and M1 with equal projections under the input settings; a contract with deletions of internal components; a candidate meeting (E) for M0 and not for M1

  ```
  input-output equal: True; the parallel-route candidate meets (E) on M0's question: True; on M1's: (False, {'translates C': True, 'F1': False, 'F2eq': False, 'Hom': True, 'F2': False, 'A': False, 'NC1': True, 'NC2': True, 'NonVacuous': True})
  ```

### FC102 · Argument 10: surprise, the structural failure of selection, and the constructed layer — COUNTEREXAMPLE FOUND

**The claim.** With I68: (a) t0 (window w) survives on H0 and is violated at the re-emergence pair, which lies in C0∖H0: Surp. (b) If the occlusion hides the thing for longer than w steps, every window-w occupancy predictor fails on the extended history (two histories with equal last-w occupancy and different re-emergence cells); if w is at least that long, an occupancy predictor can extrapolate and the failure is not structural. (c) t1 meets (F1) and (F2) on the extended contract, and each persistence component's signature read through t1 equals its thing's continuity subnetwork's (Argument 1).

**Rests on.** Claim's inventions: I52, I68. Program's: I100. **Reproduce.** `cd "/home/user/ThreadSmith/Semantics/results/S104 Round 2 - maths" && python3 -m model.run --claim FC102 --scale 4 --time-cap 45`

- **(b) first half: the occlusion outlasts the window** [computation] — *computed: as claimed*. occlusion of L ≥ w steps ⇒ two histories with equal last-w occupancy and different re-emergence readings

  ```
  N = 6 cells, cells 1..4 hidden from t = 3 for L steps. Failing (things, w, L): [(1, 1, 1), (1, 1, 2), (1, 1, 3), (1, 1, 4), (1, 2, 2), (1, 2, 3), (1, 2, 4), (1, 3, 3), (1, 3, 4), (2, 1, 1), (2, 1, 2), (2, 1, 3), (2, 1, 4), (2, 2, 2), (2, 2, 3), (2, 2, 4), (2, 3, 3), (2, 3, 4)]
  ```

- **(b) second half: a window longer than the occlusion** [computation] — *computed: not as claimed*. w > L ⇒ an occupancy predictor can extrapolate (the failure is not structural)
  - The counterexample is written out above, under Counterexamples.

- **(a), (c)** [not tested] — *not tested*. t0 survives on H0 and is surprised; t1 meets (F1) and (F2) on the extended contract
  - Why not: the two-layer organizations S0, S1 and their transports are not built in this round (E9 encodes only the object layer here)

### FC103 · Argument 10: the swap, two pairings, one account — HOLDS ON ALL MODELS TRIED

**The claim.** With I69: ψ an automorphism of P preserving C and the answers; t1' := t1∘ψ. (a) t1' meets (F1), (F2) and (A) on C exactly when t1 does. (b) The exchange of persistence components meets Argument 2 (ii)'s premise, so each k and its image are of one kind on C. (c) No pair of C separates the two pairings (FC51 (b)). (d) The swap edit leaves every occupancy answer unchanged.

**Rests on.** Claim's inventions: I10, I14, I68, I69. Program's: I100. **Reproduce.** `cd "/home/user/ThreadSmith/Semantics/results/S104 Round 2 - maths" && python3 -m model.run --claim FC103 --scale 4 --time-cap 45`

- **(d) the swap leaves occupancy answers unchanged** [computation] — *computed: as claimed*. exchanging the two things' states leaves every occupancy reading unchanged

  ```
  all placements of two things on 5 cells
  ```

- **(a)-(c) on E9** [not tested] — *not tested*. t1∘ψ meets (F1), (F2), (A) exactly when t1 does; one kind; no pair separates the pairings
  - Why not: E9's simulation layer is not built; the general forms are tested as FC33, FC96 (ii) and FC51 (b)

### FC104 · The two extents of 'fidelity' across the text — NOT TESTED

**The claim.** For each line using 'faithful' or 'fidelity' (L17, L23, L37, L41, L43, L49, L67, L69, L151, L189, L195, L205, L208, L211, L220, L233, L245, L247, L271, L277, L325, L339, L403, L407, L413, L520, L576, L622, L626, L630), assign the extent under which the sentence holds as written: narrow (F1) ∧ (F2), or wide (F1) ∧ (F2) ∧ (A). Claim to test: no single extent serves every line; L189, L245 and L630 need the narrow one, L247's heading and L520 the wide one.

**Rests on.** Claim's inventions: I49, I50. Program's: none. **Reproduce.** `cd "/home/user/ThreadSmith/Semantics/results/S104 Round 2 - maths" && python3 -m model.run --claim FC104 --scale 4 --time-cap 45`

- **two extents of 'fidelity'** [not tested] — *not tested*. which extent each line needs
  - Why not: a reading of thirty lines' wording

### FC105 · 'Event' is used and never defined; 'occurrence' is defined — NOT TESTED

**The claim.** Under I45 every use of 'event' (L53, L55, L161, L397, L604, L612) is read as a set of occurrences. Test whether any use needs more (for example 'lost event identities' at L612, an identity of an event beyond its occurrences). Argument 6 (L596) speaks of predicates; 'event' is a sort, defined nowhere.

**Rests on.** Claim's inventions: I45. Program's: none. **Reproduce.** `cd "/home/user/ThreadSmith/Semantics/results/S104 Round 2 - maths" && python3 -m model.run --claim FC105 --scale 4 --time-cap 45`

- **'event'** [not tested] — *not tested*. whether any use of 'event' needs more than a set of occurrences
  - Why not: a reading of six lines' wording

### FC106 · A question's three defects, as far as they can be written — HOLDS ON ALL MODELS TRIED

**The claim.** Under I76: 'incompatible baseline' is Sol_D(1,b0) = ∅ (then non-vacuity fails and no candidate has Acc) or b0 ∉ B; 'incompatible requirements' is a description whose conditions on (C, Q) have no joint instance; 'fails to pick out its alleged target' is a description met by no organization or by several, and cannot be written with p alone, since D is given in p.

**Rests on.** Claim's inventions: I76. Program's: I77, I78, I81. **Reproduce.** `cd "/home/user/ThreadSmith/Semantics/results/S104 Round 2 - maths" && python3 -m model.run --claim FC106 --scale 4 --time-cap 45`

- **an incompatible baseline admits no account** [for all] — *holds on all models tried*. Sol_D(1,b0) = ∅ ⇒ ¬NonVacuous ⇒ no candidate has Acc
  - Searched: sizes ports=1 dom≤1 comps=1 |B|=1 edits=0 … ports=3 dom≤2 comps=3 |B|=2 edits=2 (108 sizes, 160 draws each); families: G-surg, G-free; seed 105061; 17280 models tried; 5709 of them meeting the claim's hypothesis.

- **the other two defects** [not tested] — *not tested*. failing to pick out a target; incompatible requirements
  - Why not: need a description Desc of the question (I76), which the model does not build

### FC107 · Exposing a question's defect is another question — NOT TESTED

**The claim.** The question p_δ (whether p has defect δ) has a target, contract and query of its own, so p_δ ≠ p; a candidate for it is assessed by (E) on p_δ, as in (K1).

**Rests on.** Claim's inventions: I76. Program's: none. **Reproduce.** `cd "/home/user/ThreadSmith/Semantics/results/S104 Round 2 - maths" && python3 -m model.run --claim FC107 --scale 4 --time-cap 45`

- **p_δ ≠ p** [not tested] — *not tested*. exposing a defect is another question
  - Why not: definitional: p_δ has its own target, contract and query (D9.10)

### FC108 · The first sentence of non-circular dependence adds no condition — HOLDS ON ALL MODELS TRIED

**The claim.** Under I23, NC0 holds of every candidate: every answer is computed by evaluating E at (τ(a),σ(b)), with σ(b) a function of b. A reading on which it adds a condition needs a notion of how an answer is computed (propagation against lookup) that (O) and (Q) do not give.

**Rests on.** Claim's inventions: I23. Program's: none. **Reproduce.** `cd "/home/user/ThreadSmith/Semantics/results/S104 Round 2 - maths" && python3 -m model.run --claim FC108 --scale 4 --time-cap 45`

- **NC0 adds no condition** [by construction] — *holds by construction*. NC0 holds of every candidate

  ```
  core.noncircular is NC1 ∧ NC2; every answer is computed by evaluating E at (τ(a), σ(b))
  ```

### FC109 · 'A mathematical error': the named claims, each under its stated assumptions — HOLDS ON ALL MODELS TRIED

**The claim.** L546 names the finite monotone claim (FC37), (I2) (FC57), (O1) (FC61), (T2) (FC66), (CT2) (FC92) and Arguments 1–3 (FC17, FC96, FC80). Each is stated in the formal core with its assumptions. A counterexample that rests on an invention is a counterexample to the formalization, not to the text, and is reported with the invention it rests on.

**Rests on.** Claim's inventions: I10, I12, I13, I14, I61, I63, I64, I71. Program's: none. **Reproduce.** `cd "/home/user/ThreadSmith/Semantics/results/S104 Round 2 - maths" && python3 -m model.run --claim FC109 --scale 4 --time-cap 45`

- **the named results, each under its assumptions** [computation] — *computed: as claimed*. L546's named claims have no counterexample on the models tried

  ```
  FC37: HOLDS ON ALL MODELS TRIED; FC57: HOLDS ON ALL MODELS TRIED; FC61: HOLDS ON ALL MODELS TRIED; FC66: HOLDS ON ALL MODELS TRIED; FC92: HOLDS ON ALL MODELS TRIED; FC17: HOLDS ON ALL MODELS TRIED; FC96: HOLDS ON ALL MODELS TRIED; FC80: HOLDS ON ALL MODELS TRIED (rerun here at 0.3 of the budget; the full runs are reported under each claim)
  ```

### FC110 · The classes are defined; no membership is asserted — NOT TESTED

**The claim.** Syntactic: each class of L528 (base, creative-episode, explanation-creation, recursive, universal) is the extension of a formula of the formal core; no axiom of the formal core places any particular system in a class.

**Rests on.** Claim's inventions: I74, I75. Program's: none. **Reproduce.** `cd "/home/user/ThreadSmith/Semantics/results/S104 Round 2 - maths" && python3 -m model.run --claim FC110 --scale 4 --time-cap 45`

- **the classes** [not tested] — *not tested*. each class is the extension of a formula; no axiom places a system in a class
  - Why not: syntactic, about the formal core's definitions

## Not tested, and why

- FC10, L57 names no condition on observation edits; the removed clause: a reading of two sentences' wording, not a property of models
- FC24, L273's 'an account' names a candidate: a reading of wording
- FC31, five conjuncts, four headings, L520's sources: a reading of wording, not a model property
- FC32, Acc's arguments against L526's order: a property of the dependence graph read from the text (S101, D18.1), not of models; the model can only list Acc's arguments (FC30)
- FC33, (b) which conjuncts inspect a declared statement or a grain: a reading of the conjuncts' arguments; see FC30
- FC35, L151's 'prediction': a question of which lines a definition covers (I51)
- FC80, (c) under an action law: comparing I02 with an action law needs a population family closed under an action law; not built in this round
- FC89, L443's two kinds of explanatory aim: a reading of the wording of L443 against Deploy's typing
- FC90, the worked case's '(EX) is met': a reading of L620–L628; the model does not encode the worked case's history
- FC94, recursion and universality: RC, UU, Enable, target chains and 𝔈_Θ have no finite semantics without Θ; a model would be an assignment of free predicates, which shows only that no axiom links them (as FC110)
- FC97, Deploy, Build, New and (G) take it as a content: needs Θ (I90); the typing check above is what the model can do
- FC98, the dependence graph: a property of the definitions' dependence graph (D18.1), not of models
- FC100, (G), (P), (EX): need histories and Θ; not modelled beyond free predicates
- FC102, (a), (c): the two-layer organizations S0, S1 and their transports are not built in this round (E9 encodes only the object layer here)
- FC103, (a)-(c) on E9: E9's simulation layer is not built; the general forms are tested as FC33, FC96 (ii) and FC51 (b)
- FC104, two extents of 'fidelity': a reading of thirty lines' wording
- FC105, 'event': a reading of six lines' wording
- FC106, the other two defects: need a description Desc of the question (I76), which the model does not build
- FC107, p_δ ≠ p: definitional: p_δ has its own target, contract and query (D9.10)
- FC110, the classes: syntactic, about the formal core's definitions

## Results by invention

Each invention, with the claims whose results depend on it; a claim with a counterexample names the parts whose counterexample depends on it. The same list is written into each entry of `inventions register.md`.

| invention | results that depend on it |
| --- | --- |
| I01 | FC97 (holds on all models tried) |
| I02 | FC80 (holds on all models tried) |
| I03 | FC01 (holds on all models tried); FC25 (counterexample: (b) with a port of D in no footprint); FC62 (holds on all models tried); FC63 (counterexample: (c-i) the Leibniz candidate, sum over every tuple of term values) |
| I04 | FC02 (holds on all models tried); FC06 (holds on all models tried); FC07 (holds on all models tried); FC08 (holds on all models tried); FC11 (holds on all models tried); FC13 (holds on all models tried); FC25 (counterexample: (b) with a port of D in no footprint); FC26 (holds on all models tried); FC27 (holds on all models tried) |
| I05 | FC02 (holds on all models tried) |
| I06 | FC07 (holds on all models tried); FC08 (holds on all models tried); FC13 (holds on all models tried) |
| I07 | FC06 (holds on all models tried); FC07 (holds on all models tried); FC08 (holds on all models tried) |
| I08 | FC09 (holds on all models tried); FC10 (holds on all models tried); FC13 (holds on all models tried) |
| I09 | FC06 (holds on all models tried); FC07 (holds on all models tried); FC10 (holds on all models tried); FC11 (holds on all models tried); FC12 (holds on all models tried); FC13 (holds on all models tried) |
| I10 | FC03 (holds on all models tried); FC04 (holds on all models tried); FC05 (counterexample: (ii) reading (ii): any bijection); FC16 (holds on all models tried); FC18 (counterexample: untranslated reading (I94)); FC96 (holds on all models tried); FC103 (holds on all models tried); FC109 (holds on all models tried) |
| I11 | FC04 (holds on all models tried); FC50 (holds on all models tried) |
| I12 | FC15 (holds on all models tried); FC16 (holds on all models tried); FC17 (holds on all models tried); FC29 (holds on all models tried); FC96 (holds on all models tried); FC109 (holds on all models tried) |
| I13 | FC17 (holds on all models tried); FC18 (counterexample: untranslated reading (I94)); FC109 (holds on all models tried) |
| I14 | FC17 (holds on all models tried); FC18 (counterexample: untranslated reading (I94)); FC19 (holds on all models tried); FC20 (counterexample: any value map κ); FC25 (counterexample: (b) with a port of D in no footprint); FC44 (holds on all models tried); FC62 (holds on all models tried); FC96 (holds on all models tried); FC103 (holds on all models tried); FC109 (holds on all models tried) |
| I15 | FC17 (holds on all models tried); FC19 (holds on all models tried) |
| I16 | FC20 (counterexample: any value map κ); FC49 (holds on all models tried) |
| I17 | FC45 (holds on all models tried); FC49 (holds on all models tried) |
| I18 | FC15 (holds on all models tried); FC51 (holds on all models tried); FC77 (counterexample: with H = ∅ and an empty selection history) |
| I19 | FC44 (holds on all models tried); FC45 (holds on all models tried); FC46 (holds on all models tried); FC47 (holds on all models tried); FC52 (holds on all models tried); FC54 (holds on all models tried) |
| I20 | FC20 (counterexample: any value map κ); FC26 (holds on all models tried); FC28 (holds on all models tried); FC30 (holds on all models tried); FC32 (not tested); FC45 (holds on all models tried); FC68 (holds on all models tried); FC98 (not tested) |
| I21 | FC20 (counterexample: any value map κ); FC21 (holds on all models tried); FC22 (holds on all models tried); FC23 (counterexample: (b) as stated); FC26 (holds on all models tried); FC46 (holds on all models tried); FC48 (holds on all models tried) |
| I22 | FC21 (holds on all models tried); FC22 (holds on all models tried); FC23 (counterexample: (b) as stated) |
| I23 | FC108 (holds on all models tried) |
| I24 | FC23 (counterexample: (b) as stated); FC24 (holds on all models tried); FC26 (holds on all models tried); FC33 (holds on all models tried); FC34 (holds on all models tried); FC51 (holds on all models tried); FC60 (holds on all models tried) |
| I25 | FC23 (counterexample: (b) as stated) |
| I26 | FC21 (holds on all models tried) |
| I27 | FC26 (holds on all models tried); FC30 (holds on all models tried); FC32 (not tested); FC33 (holds on all models tried); FC34 (holds on all models tried); FC51 (holds on all models tried); FC63 (counterexample: (c-i) the Leibniz candidate, sum over every tuple of term values) |
| I28 | FC30 (holds on all models tried); FC32 (not tested); FC33 (holds on all models tried) |
| I29 | FC41 (holds on all models tried); FC98 (not tested); FC101 (holds on all models tried) |
| I30 | FC38 (holds on all models tried); FC39 (holds on all models tried); FC40 (holds on all models tried); FC42 (holds on all models tried) |
| I31 | FC40 (holds on all models tried) |
| I32 | FC25 (counterexample: (b) with a port of D in no footprint) |
| I33 | FC43 (holds on all models tried); FC49 (holds on all models tried); FC50 (holds on all models tried); FC54 (holds on all models tried); FC98 (not tested) |
| I34 | FC52 (holds on all models tried); FC53 (holds on all models tried); FC54 (holds on all models tried); FC98 (not tested) |
| I35 | FC54 (holds on all models tried) |
| I36 | FC44 (holds on all models tried) |
| I37 | FC43 (holds on all models tried) |
| I38 | FC47 (holds on all models tried); FC53 (holds on all models tried); FC56 (holds on all models tried); FC68 (holds on all models tried); FC71 (holds on all models tried); FC72 (holds on all models tried); FC73 (holds on all models tried) |
| I39 | FC60 (holds on all models tried); FC72 (holds on all models tried); FC98 (not tested) |
| I40 | FC47 (holds on all models tried); FC53 (holds on all models tried); FC56 (holds on all models tried); FC68 (holds on all models tried); FC69 (holds on all models tried); FC70 (holds on all models tried) |
| I41 | FC56 (holds on all models tried); FC68 (holds on all models tried); FC70 (holds on all models tried) |
| I42 | FC47 (holds on all models tried) |
| I43 | FC47 (holds on all models tried); FC71 (holds on all models tried) |
| I44 | FC75 (holds on all models tried); FC90 (not tested) |
| I45 | FC74 (holds on all models tried); FC100 (holds on all models tried); FC105 (not tested) |
| I46 | FC75 (holds on all models tried); FC87 (holds on all models tried); FC98 (not tested); FC101 (holds on all models tried) |
| I47 | FC76 (holds on all models tried); FC98 (not tested) |
| I48 | FC77 (counterexample: with H = ∅ and an empty selection history); FC85 (holds on all models tried); FC95 (holds on all models tried); FC97 (holds on all models tried) |
| I49 | FC20 (counterexample: any value map κ); FC31 (not tested); FC79 (holds on all models tried); FC104 (not tested) |
| I50 | FC20 (counterexample: any value map κ); FC81 (counterexample: (d) Con(t) ∧ Viol ⇒ ¬Surp (under I53)); FC104 (not tested) |
| I51 | FC35 (not tested) |
| I52 | FC77 (counterexample: with H = ∅ and an empty selection history); FC78 (counterexample: exactly one provenance under I53); FC79 (holds on all models tried); FC80 (holds on all models tried); FC81 (counterexample: (d) Con(t) ∧ Viol ⇒ ¬Surp (under I53)); FC82 (counterexample: no common result); FC83 (counterexample: only construction is originative); FC95 (holds on all models tried); FC102 (counterexample: (b) second half: a window longer than the occlusion) |
| I53 | FC78 (counterexample: exactly one provenance under I53); FC81 (counterexample: (d) Con(t) ∧ Viol ⇒ ¬Surp (under I53)); FC82 (counterexample: no common result); FC84 (holds on all models tried) |
| I54 | FC67 (holds on all models tried); FC78 (counterexample: exactly one provenance under I53) |
| I55 | FC98 (not tested) |
| I56 | FC78 (counterexample: exactly one provenance under I53); FC81 (counterexample: (d) Con(t) ∧ Viol ⇒ ¬Surp (under I53)); FC82 (counterexample: no common result); FC83 (counterexample: only construction is originative); FC84 (holds on all models tried); FC98 (not tested) |
| I57 | FC86 (holds on all models tried); FC87 (holds on all models tried); FC88 (holds on all models tried); FC90 (not tested) |
| I58 | FC88 (holds on all models tried); FC98 (not tested) |
| I59 | FC89 (not tested); FC90 (not tested); FC98 (not tested) |
| I60 | FC89 (not tested); FC90 (not tested) |
| I61 | FC91 (holds on all models tried); FC92 (holds on all models tried); FC109 (holds on all models tried) |
| I62 | FC93 (holds on all models tried) |
| I63 | FC57 (holds on all models tried); FC58 (holds on all models tried); FC61 (holds on all models tried); FC109 (holds on all models tried) |
| I64 | FC57 (holds on all models tried); FC58 (holds on all models tried); FC59 (holds on all models tried); FC109 (holds on all models tried) |
| I65 | FC02 (holds on all models tried); FC07 (holds on all models tried); FC26 (holds on all models tried); FC27 (holds on all models tried); FC28 (holds on all models tried); FC99 (holds on all models tried) |
| I66 | FC63 (counterexample: (c-i) the Leibniz candidate, sum over every tuple of term values) |
| I67 | FC97 (holds on all models tried) |
| I68 | FC90 (not tested); FC102 (counterexample: (b) second half: a window longer than the occlusion); FC103 (holds on all models tried) |
| I69 | FC103 (holds on all models tried) |
| I70 | FC13 (holds on all models tried); FC33 (holds on all models tried); FC45 (holds on all models tried); FC67 (holds on all models tried); FC100 (holds on all models tried) |
| I71 | FC80 (holds on all models tried); FC109 (holds on all models tried) |
| I72 | FC36 (holds on all models tried) |
| I73 | FC34 (holds on all models tried) |
| I74 | FC94 (not tested); FC110 (not tested) |
| I75 | FC94 (not tested); FC110 (not tested) |
| I76 | FC106 (holds on all models tried); FC107 (not tested) |
| I77 | FC01 (holds on all models tried); FC02 (holds on all models tried); FC03 (holds on all models tried); FC04 (holds on all models tried); FC05 (counterexample: (ii) reading (ii): any bijection); FC06 (holds on all models tried); FC08 (holds on all models tried); FC10 (holds on all models tried); FC12 (holds on all models tried); FC13 (holds on all models tried); FC15 (holds on all models tried); FC16 (holds on all models tried); FC17 (holds on all models tried); FC18 (counterexample: untranslated reading (I94)); FC19 (holds on all models tried); FC20 (counterexample: any value map κ); FC21 (holds on all models tried); FC22 (holds on all models tried); FC23 (counterexample: (b) as stated); FC24 (holds on all models tried); FC25 (counterexample: (b) with a port of D in no footprint); FC29 (holds on all models tried); FC33 (holds on all models tried); FC34 (holds on all models tried); FC37 (holds on all models tried); FC41 (holds on all models tried); FC43 (holds on all models tried); FC44 (holds on all models tried); FC45 (holds on all models tried); FC46 (holds on all models tried); FC47 (holds on all models tried); FC48 (holds on all models tried); FC49 (holds on all models tried); FC50 (holds on all models tried); FC51 (holds on all models tried); FC52 (holds on all models tried); FC54 (holds on all models tried); FC57 (holds on all models tried); FC58 (holds on all models tried); FC61 (holds on all models tried); FC64 (holds on all models tried); FC65 (holds on all models tried); FC66 (holds on all models tried); FC67 (holds on all models tried); FC68 (holds on all models tried); FC74 (holds on all models tried); FC77 (counterexample: with H = ∅ and an empty selection history); FC80 (holds on all models tried); FC85 (holds on all models tried); FC96 (holds on all models tried); FC100 (holds on all models tried); FC106 (holds on all models tried) |
| I78 | FC01 (holds on all models tried); FC02 (holds on all models tried); FC03 (holds on all models tried); FC04 (holds on all models tried); FC05 (counterexample: (ii) reading (ii): any bijection); FC06 (holds on all models tried); FC08 (holds on all models tried); FC09 (holds on all models tried); FC10 (holds on all models tried); FC12 (holds on all models tried); FC13 (holds on all models tried); FC15 (holds on all models tried); FC16 (holds on all models tried); FC17 (holds on all models tried); FC18 (counterexample: untranslated reading (I94)); FC19 (holds on all models tried); FC20 (counterexample: any value map κ); FC21 (holds on all models tried); FC22 (holds on all models tried); FC23 (counterexample: (b) as stated); FC24 (holds on all models tried); FC25 (counterexample: (b) with a port of D in no footprint); FC29 (holds on all models tried); FC33 (holds on all models tried); FC34 (holds on all models tried); FC37 (holds on all models tried); FC43 (holds on all models tried); FC44 (holds on all models tried); FC45 (holds on all models tried); FC46 (holds on all models tried); FC47 (holds on all models tried); FC48 (holds on all models tried); FC49 (holds on all models tried); FC50 (holds on all models tried); FC51 (holds on all models tried); FC52 (holds on all models tried); FC54 (holds on all models tried); FC62 (holds on all models tried); FC67 (holds on all models tried); FC68 (holds on all models tried); FC74 (holds on all models tried); FC77 (counterexample: with H = ∅ and an empty selection history); FC80 (holds on all models tried); FC85 (holds on all models tried); FC96 (holds on all models tried); FC100 (holds on all models tried); FC101 (holds on all models tried); FC106 (holds on all models tried) |
| I79 | FC23 (counterexample: (b) as stated); FC24 (holds on all models tried); FC26 (holds on all models tried); FC34 (holds on all models tried); FC62 (holds on all models tried) |
| I80 | FC02 (holds on all models tried); FC06 (holds on all models tried); FC07 (holds on all models tried); FC11 (holds on all models tried); FC12 (holds on all models tried); FC25 (counterexample elsewhere) |
| I81 | FC15 (holds on all models tried); FC16 (holds on all models tried); FC17 (holds on all models tried); FC18 (counterexample: untranslated reading (I94)); FC19 (holds on all models tried); FC20 (counterexample: any value map κ); FC21 (holds on all models tried); FC22 (holds on all models tried); FC23 (counterexample: (b) as stated); FC24 (holds on all models tried); FC29 (holds on all models tried); FC33 (holds on all models tried); FC34 (holds on all models tried); FC37 (holds on all models tried); FC43 (holds on all models tried); FC44 (holds on all models tried); FC45 (holds on all models tried); FC46 (holds on all models tried); FC47 (holds on all models tried); FC48 (holds on all models tried); FC49 (holds on all models tried); FC50 (holds on all models tried); FC51 (holds on all models tried); FC52 (holds on all models tried); FC54 (holds on all models tried); FC63 (counterexample: (c-i) the Leibniz candidate, sum over every tuple of term values); FC67 (holds on all models tried); FC68 (holds on all models tried); FC74 (holds on all models tried); FC77 (counterexample: with H = ∅ and an empty selection history); FC80 (holds on all models tried); FC85 (holds on all models tried); FC96 (holds on all models tried); FC100 (holds on all models tried); FC106 (holds on all models tried) |
| I82 | FC23 (counterexample: (b) as stated); FC63 (counterexample: (c-i) the Leibniz candidate, sum over every tuple of term values) |
| I83 | FC23 (counterexample: (b) as stated); FC24 (holds on all models tried) |
| I85 | FC21 (holds on all models tried); FC26 (holds on all models tried); FC34 (holds on all models tried); FC46 (holds on all models tried); FC51 (holds on all models tried) |
| I86 | FC43 (holds on all models tried); FC49 (holds on all models tried); FC50 (holds on all models tried) |
| I87 | FC47 (holds on all models tried); FC53 (holds on all models tried); FC56 (holds on all models tried); FC60 (holds on all models tried); FC68 (holds on all models tried); FC69 (holds on all models tried); FC70 (holds on all models tried); FC71 (holds on all models tried); FC72 (holds on all models tried); FC73 (holds on all models tried) |
| I88 | FC47 (holds on all models tried); FC53 (holds on all models tried); FC56 (holds on all models tried); FC71 (holds on all models tried) |
| I89 | FC47 (holds on all models tried); FC53 (holds on all models tried); FC56 (holds on all models tried); FC60 (holds on all models tried); FC68 (holds on all models tried); FC69 (holds on all models tried); FC70 (holds on all models tried); FC71 (holds on all models tried); FC72 (holds on all models tried); FC73 (holds on all models tried) |
| I90 | FC53 (holds on all models tried); FC76 (holds on all models tried); FC77 (counterexample: with H = ∅ and an empty selection history); FC78 (counterexample: exactly one provenance under I53); FC81 (counterexample: (d) Con(t) ∧ Viol ⇒ ¬Surp (under I53)); FC82 (counterexample: no common result); FC83 (counterexample: only construction is originative); FC95 (holds on all models tried) |
| I91 | FC40 (holds on all models tried) |
| I92 | FC02 (holds on all models tried); FC07 (holds on all models tried); FC11 (holds on all models tried); FC26 (holds on all models tried); FC27 (holds on all models tried); FC28 (holds on all models tried); FC78 (counterexample: exactly one provenance under I53); FC81 (counterexample: (d) Con(t) ∧ Viol ⇒ ¬Surp (under I53)); FC82 (counterexample: no common result); FC83 (counterexample: only construction is originative); FC95 (holds on all models tried); FC99 (holds on all models tried) |
| I93 | FC05 (counterexample: (ii) reading (ii): any bijection) |
| I94 | FC18 (counterexample: untranslated reading (I94)) |
| I95 | FC75 (holds on all models tried); FC76 (holds on all models tried) |
| I96 | FC86 (holds on all models tried); FC88 (holds on all models tried) |
| I97 | FC91 (holds on all models tried); FC92 (holds on all models tried) |
| I98 | FC93 (holds on all models tried) |
| I99 | FC63 (counterexample: (c-i) the Leibniz candidate, sum over every tuple of term values) |
| I100 | FC102 (counterexample: (b) second half: a window longer than the occlusion); FC103 (holds on all models tried) |
| I101 | FC19 (holds on all models tried); FC21 (holds on all models tried); FC25 (counterexample elsewhere); FC34 (holds on all models tried); FC44 (holds on all models tried) |
| I102 | FC06 (holds on all models tried); FC07 (holds on all models tried) |

*Written 27 September 2026. Not committed.*
