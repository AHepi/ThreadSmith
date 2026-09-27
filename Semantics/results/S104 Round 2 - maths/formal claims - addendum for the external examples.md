# S104 Round 2 — formal claims, addendum for the external examples

*Log S104, review round 2 (the maths round), 27 September 2026. Written by a Claude subagent while the round's runs were going and before any round-2 reply was opened (see `results/S104 Round 2 - addendum to the reading rule, the external cross-examination, written before any reply was opened.md`). The committed `formal claims.md` (FC01–FC110) is not written to; these entries stand beside it. The text under review is `tests/103 The semantics, standing alone, after round 1.md`, md5 f31ebb1f050783f1a84f6136cec20fcd (compared by the program before every run; not written to). Every quotation of the text below was compared by program with the line it names.*

**What this is.** The formal examples of the external cross-examination the owner supplied (`results/S104 Round 2 - external cross-examination supplied by the owner.txt`, "the external reader"), written as claims of the S104 formal core and computed on the S104 model: its 2.1, its 2.3 in two halves, its 3.1, and its count of route families in section 5. Each entry gives the sentences of the text the example bears on, the external reader's own sentence, the formal statement, the inventions it uses, the program's printout, and a status. The program is `s104_external.py` in this folder; it imports the committed package `model/` (the definitions `account`, `restrict`, `routes`, `critical_block`, `indispensable`, `contributory`, `no_work`, `Roles` and the rest, unchanged) and adds only the encodings, whose choices are I103–I108 in `inventions register - addendum for the external examples.md`.

**Statuses.** *CONFIRMED* (the orchestrator's label): the program, run as given, computes what the external reader reports, on a model that reads the text under review and in which every choice the text leaves open is a registered invention, named with the entry. *NOT CONFIRMED*: the computation comes out otherwise than the external reader reports. A status says nothing beyond the model computed; whether a result tells against the text or only against an invention is for the checker of the external item it belongs to (reading rule, rules 5 and 6), and nothing here is settled (S28).

**Counts.** 5 claims, FC-E1 to FC-E5: 5 CONFIRMED, 0 NOT CONFIRMED. The whole run takes under a second.

**Reproducing.** `cd "/home/user/ThreadSmith/Semantics/results/S104 Round 2 - maths" && python3 s104_external.py` (every claim), or with the claim's id (for example `python3 s104_external.py FC-E1`). The printouts below are the program's own lines, trimmed only where marked.

## Index

| id | claim | the external reader | lines | inventions | status |
| --- | --- | --- | --- | --- | --- |
| FC-E1 | An unrelated commitment is critical and globally indispensable | 2.1 | L231, L287, L296, L305, L313 | I103 (I104 for a variant) | CONFIRMED |
| FC-E2 | Both ports of {(0,0),(1,1)} are outputs; only the assigning component tells the two directions apart | 2.3, first half | L103, L109, L119 | I105 (I106 for the other readings) | CONFIRMED |
| FC-E3 | A response and a reading of one port share their families | 2.3, second half | L109, L123, L124, L127 | I107 | CONFIRMED |
| FC-E4 | A readout offered as a cause meets (E) on the cue changes and fails once the contract holds do(N = 0) | 3.1 | L37, L151, L606 | I108 | CONFIRMED |
| FC-E5 | 193 route families, and the finite monotone claim on each | 5 | L305 | none new (I30, I77) | CONFIRMED |

### FC-E1 · An unrelated commitment is critical and globally indispensable

> L287 | Fix \(\mathcal E\) and a declared restriction operation. For \(W\subseteq\Gamma\), let \(E|W\) retain the commitments in \(W\) with the named background fixed; the commitments of \(E|W\) are \(W\).

> L231 | for \(E|W\), \(t'\) is \(t\) with \(\lambda\) restricted to the components of \(E|W\), and \(\Gamma'\) is \(W\).

> L296 | \operatorname{CriticalBlock}(B;W,p)\iff W\in\mathsf S_{E,p}\land W\setminus B\notin\mathsf S_{E,p}. \tag{B}

> L305 | and \(d\) is **globally indispensable**, \(\Gamma\setminus\{d\}\notin\mathsf S_{E,p}\), exactly when \(d\in\bigcap\min\mathsf S\)

> L313 | A commitment \(d\) of a candidate that has a route does no work by itself in it when every route stays a route after \(d\) is added to it and after \(d\) is removed from it

**The external reader (2.1).** "Consequently, CriticalBlock({d}; {k,d}, p) holds. Indeed, d is globally indispensable under the stated definition—even though deleting it never changes or undermines the answer about Y."

**Formal.** With I103 (target D_E1: X, Y, U, V two-valued; background c_X: X = 0, c_U: U = 0; commitments k: Y = X, d: V = U; C = the nine partial settings of X and U at b0; the query reads Y; the copy candidate ℰ with Γ = {k, d}): (a) Acc(ℰ); (b) under I29, E|{k} meets (F1) and (A) at every pair of C and fails the valuation equation of (F2), so {k} ∉ S_{E,p}; (c) CB({d}; {k,d}), Indisp(d) and Contrib(d) hold and NoWork(d) (L313) fails; (d) the answer of E|{k} about Y is the target's at every pair of C. Two variants show what the result rests on: (a′) d in the named background (Γ = {k}); (b′) the restriction of I104 in place of I29.

**Type.** External example: a computation on a model the external reader gives by hand.

**Uses.** Inventions: I03, I04, I14, I15, I18, I20, I21, I22, I24, I25, I27, I29, I77, I78, I79, I81, I82, I83, I84, I85, I103; variant (b′) also I104.

**Result.** CONFIRMED on the text under review. Reproduce: `cd "/home/user/ThreadSmith/Semantics/results/S104 Round 2 - maths" && python3 s104_external.py FC-E1`.

```
Full candidate, Γ = {k,d}: F1 yes, F2eq yes, Hom yes, F2 yes, A yes, NC1 yes, NC2 yes, NonVacuous yes => (E) yes
  NC2 witness (pair, block): (('set(U=0,X=1)', 'b0'), ['k'])
E|{k} (I29, deletion): F1 yes, F2eq no, Hom yes, F2 no, A yes, NC1 yes, NC2 yes, NonVacuous yes => (E) no
  answers about Y across the contract: [every one of the nine pairs: target Y = E|{k} Y; trimmed]
  at the baseline, π[Sol_D] = [(0, 0, 0, 0)] (ports X,Y,U,V); Sol of E|{k} = [(0, 0, 0, 0), (0, 0, 0, 1)]
Routes S_{E,p} = {{d,k}}; min S = {{d,k}}
CriticalBlock({d}; {k,d}) yes; d globally indispensable yes; d contributory yes; d does no work by itself (L313) no
Variant (a), d in the named background (Γ = {k}): (E) yes; routes {{k}}
Variant (b), the restriction of I104 (ports no component left constrains removed, π projected): E|{k}: F1 yes, F2eq yes, Hom yes, F2 yes, A yes, NC1 yes, NC2 yes, NonVacuous yes => (E) yes
  routes {{k}, {d,k}}; CriticalBlock({d}; {k,d}) no; d globally indispensable no; d does no work by itself yes
```

**What it bears on.** (B), "contributory" and "globally indispensable" (L305) and "does no work by itself" (L313) are all read through Account, and Account's (F2) is fidelity of the whole assembled organization. Deleting d frees V, so (F2) fails, and d comes out critical, contributory and globally indispensable, and not a commitment that does no work, while the answer about Y is the same at every pair. The result rests on I29. The text fixes π unchanged under restriction (L231: "t′ is t with λ restricted"); the one alternative found that removes the example (I104, which also removes the port V) changes π. Placing d in the named background removes the question (variant (a′)); L231 lets a candidate name what it offers as doing the work, and the external reader's point is that the test of L313 is meant to find a commitment that does none. The finite monotone claim (L305, FC37) is untouched: here S is upward closed with min S = {{k,d}}, and both k and d lie in ∩min S. Whether this tells against L287–L313, or against a reading of "work" and "critical" the text does not intend, is for the checker of external item E02; no S104 claim asks whether a critical commitment is one the question needs (FC37's second part drew route families from random candidates to test the finite monotone claim; FC41 tested NoWork on set systems, I30).

### FC-E2 · Both ports of {(0,0),(1,1)} are outputs; only the assigning component tells the two directions apart

> L109 | A port is an **output** of component \(j\) when its value is determined by \(L_j\) given the other ports of \(V_j\) across \(B\).

> L109 | No role assignment is supplied. … The direction of an organization is a consequence of which edits it admits, not a stipulation about which way an equation is read.

> L103 | An edit that sets a port replaces the component assigning that port; it does not add an equation beside an incompatible one.

> L119 | An edit that sets a port replaces only the component that assigns the port (above), not the relations of the components that read it

**The external reader (2.3).** "Thus the literal criterion classes both ports as outputs. It does not distinguish the assignment Y := X from X := Y. A finite check confirms that directly."

**Formal.** With I105 (D_fwd: k on (X, Y) with home port Y, background c_X: X = 0; D_rev: the same k with home port X, background c_Y: Y = 0; every partial setting of X and Y admitted): (a) in D_fwd and in D_rev, Out(X, k) and Out(Y, k) (D2.3, I05); (b) asg(Y) = k and asg(X) = c_X in D_fwd, asg(X) = k and asg(Y) = c_Y in D_rev (D2.1, I04), with or without I80; (c) with L_k read at every edit that leaves it as it is (I106 (a)), as (a); with L_k read at every edit, those that alter k included (I106 (b)), only k's home port is an output.

**Type.** External example.

**Uses.** Inventions: I04, I05, I78, I79, I80, I105; the other readings also I106.

**Result.** CONFIRMED on the text under review. Reproduce: `cd "/home/user/ThreadSmith/Semantics/results/S104 Round 2 - maths" && python3 s104_external.py FC-E2`.

```
D_fwd: L_k(1,b0) = [(0, 0), (1, 1)]; edits 1, set(X=0), set(X=1), set(Y=0), set(Y=1), set(X=0,Y=0), set(X=0,Y=1), set(X=1,Y=0), set(X=1,Y=1)
  L109 output of k, relation read at the identity edit (I05): X yes, Y yes
  L109 output of k, relation read at every edit that leaves L_k as it is (I106 (a)): X yes, Y yes
  L109 output of k, relation read at every edit, those that alter k included (I106 (b)): X no, Y yes
  asg (I04, I80): {'X': 'c_X', 'Y': 'k'}; inputs: ['X', 'Y']
  asg (I04, identity excluded (I80 other choice)): {'X': 'c_X', 'Y': 'k'}; inputs: ['X', 'Y']
D_rev: L_k(1,b0) = [(0, 0), (1, 1)]; edits [as D_fwd; trimmed]
  L109 output of k, relation read at the identity edit (I05): X yes, Y yes
  L109 output of k, relation read at every edit that leaves L_k as it is (I106 (a)): X yes, Y yes
  L109 output of k, relation read at every edit, those that alter k included (I106 (b)): X yes, Y no
  asg (I04, I80): {'X': 'k', 'Y': 'c_Y'}; inputs: ['X', 'Y']
  asg (I04, identity excluded (I80 other choice)): {'X': 'k', 'Y': 'c_Y'}; inputs: ['X', 'Y']
```

**What it bears on.** L109's output clause does not tell Y := X from X := Y; what does is which component the setting edits replace, the assigning component that L103 and L119 name and that I04 reads off the edits. This is the Boolean form of FC02 (c) (on the pole, H and θ are outputs of c_L as well as L, and the direction is carried by asg, not by output status), of the formal core's §2 **Vague** note, of I04's other choice (b) ("fails for relational components"), and of the check's H04 (direction defined as (Input_A, asg), with no invention number). Under I106 (b) output status does follow the direction, but only through the setting edits that replace k, which is I04's information again. The external reader's repair asks the text to choose: "either an independent definition from the edit structure or explicit inclusion in the supplied data".

### FC-E3 · A response and a reading of one port share their families

> L123 | - a **causal assignment** has a signature that changes under intervention on its output port and is invariant under observation edits;

> L124 | - a **measurement** has a signature invariant under interventions on the measured port and variable under edits to the measuring relation;

> L127 | In particular, a part that reads or reports another part has a measurement's signature

> L109 | A port is an **observation** when \(A\) contains an edit that alters the relation reporting it without altering what it reports

**The external reader (2.3).** "For a component Y := X, intervening upstream on X changes the solution but normally leaves the relation Y = X unchanged. A measuring component N := X has the same property. Their distinction cannot come merely from whether their own relation changes under that upstream intervention."

**Formal.** With I107 (D_ro: c_X: X = 0; the response c_Y: Y = X; the reading c_N: N = X; every partial setting of X, N and Y): (a) on C_single and on C_all, under R-i and under R-ii (I06), c_N and c_Y are both invariant under every setting of X and belong to the same families (D4.6: causal; measurement, and of which port; rule), with or without I80; (b) with recal(c_N) admitted and in the contract, they belong to different families under both readings.

**Type.** External example.

**Uses.** Inventions: I01, I04, I06, I07, I08, I09, I78, I79, I80, I102, I107.

**Result.** CONFIRMED on the text under review. Reproduce: `cd "/home/user/ThreadSmith/Semantics/results/S104 Round 2 - maths" && python3 s104_external.py FC-E3`.

```
D_ro, C_single (baseline and every single setting), R-i: c_N causal no, measurement of ['X'], rule no | c_Y causal no, measurement of ['X'], rule no | both invariant under the settings of X: yes
D_ro, C_single (baseline and every single setting), R-ii: c_N causal yes, measurement of none, rule no | c_Y causal yes, measurement of none, rule no | both invariant under the settings of X: yes
D_ro, C_all (every edit), R-i: c_N causal no, measurement of ['X'], rule yes | c_Y causal no, measurement of ['X'], rule yes | both invariant under the settings of X: yes
D_ro, C_all (every edit), R-ii: c_N causal no, measurement of ['X'], rule yes | c_Y causal no, measurement of ['X'], rule yes | both invariant under the settings of X: yes
D_ro+recal, C_single plus recal(c_N), R-i: c_N causal no, measurement of ['X'], rule yes | c_Y causal no, measurement of ['X'], rule no | both invariant under the settings of X: yes
D_ro+recal, C_single plus recal(c_N), R-ii: c_N causal no, measurement of ['X'], rule yes | c_Y causal yes, measurement of none, rule no | both invariant under the settings of X: yes
Under I80's other choice (identity excluded) the families on D_ro are the same as under I80: yes
On D_ro, under both readings and on both contracts, c_N and c_Y share every family and are both invariant under the settings of X: yes
With recal(c_N) admitted and in the contract they no longer share their families: under R-i yes, under R-ii yes
```

**What it bears on.** Under R-i the reading and the response are both measurements of X and neither is a causal assignment, as FC07 (a) found (under R-i, a setting of a component's own output is an observation edit whenever the component reads another port); under R-ii both are causal assignments and neither is a measurement. What separates them in the text is L109's observation clause: an edit that alters the reporting relation without altering what it reports, admitted for the reading and not for the response. With such an edit the two part (under R-ii the response is causal and the reading a measurement of X and also a rule application; under R-i the reading alone is a rule application). L127's gloss names reading and reporting together, and the response Y = X reads X as the reading N = X does. On C_all both are rule applications, because a composite of two settings is no setting edit (the check's H01 and R13). The external reader's conclusion is that "the listed patterns do not automatically provide the sharp semantic classification the surrounding prose suggests"; whether L121–L127 claim more than the patterns give is for the checker of external item E05.

### FC-E4 · A readout offered as a cause meets (E) on the cue changes and fails once the contract holds do(N = 0)

> L151 | A measure that identifies an outcome, together with a prediction of the outcome from it through a transport faithful on the contract, answers the identification question; whether the measured part also produces the outcome is the production question, and the first answer is not the second.

> L37 | A correlation has no component that responds to an intervention on its supposed input; a cause does.

> L606 | and \(\mathcal E\) can meet (E) on \(C\) and fail it on \(C'\).

**The external reader (3.1).** "In the finite implementation, this intervention breaks F1, F2, and answer fidelity."

**Formal.** With I108 (target D_mem: c_X: X = 0, c_M: M = X, c_N: N = M, c_Y: Y = M; candidate E_readout with c_Yp: Y = N in place of c_Y and λ(c_Yp) = {c_N, c_Y}, M hidden; C1 = the baseline and the settings of X; C2 = C1 and the setting X = 1, N = 0): (a) for Γ = {c_M, c_N, c_Yp} and for Γ = {c_Yp}, Acc on C1; (b) on C2, (F1), (F2) and (A) fail, and NC1, NC2 and non-vacuity hold; (c) at the setting X = 1, N = 0 the target's solution (X, M, N, Y) is (1, 1, 0, 1) and the candidate's is (1, 1, 0, 0).

**Type.** External example.

**Uses.** Inventions: I03, I04, I14, I15, I18, I20, I21, I22, I24, I25, I27, I77, I78, I79, I81, I82, I83, I84, I85, I108.

**Result.** CONFIRMED on the text under review. Reproduce: `cd "/home/user/ThreadSmith/Semantics/results/S104 Round 2 - maths" && python3 s104_external.py FC-E4`.

```
Γ = {c_M, c_N, c_Yp}, C1 (cue changes): F1 yes, F2eq yes, Hom yes, F2 yes, A yes, NC1 yes, NC2 yes, NonVacuous yes => (E) yes
Γ = {c_M, c_N, c_Yp}, C2 (C1 and set(N=0,X=1)): F1 no, F2eq no, Hom yes, F2 no, A no, NC1 yes, NC2 yes, NonVacuous yes => (E) no
Γ = {c_Yp}, C1 (cue changes): F1 yes, F2eq yes, Hom yes, F2 yes, A yes, NC1 yes, NC2 yes, NonVacuous yes => (E) yes
Γ = {c_Yp}, C2 (C1 and set(N=0,X=1)): F1 no, F2eq no, Hom yes, F2 no, A no, NC1 yes, NC2 yes, NonVacuous yes => (E) no
At set(N=0,X=1): target solutions (X,M,N,Y) [(1, 1, 0, 1)]; candidate's [(1, 1, 0, 0)]
  (F1) for c_Yp there: proj of Sol_{c_N,c_Y} on (N,Y) = [(0, 0), (0, 1)]; L_c_Yp = [(0, 0), (1, 1)]
```

**What it bears on.** An instance of Argument 7 (FC99: an account on C can fail on C′) and of L151's split between identification and production: on the cue contract the relation between N and Y is the projection of the target's subnetwork {c_N, c_Y} and the readout candidate meets (E); on the contract that holds the edit separating the readout from the memory, it fails (F1), (F2) and (A). The external reader counts this a success of the text and adds, as a finding about scope, that the formalism does not say which intervention isolates the readout or whether a manipulation also changes the memory (external item E07). The narrowing of L159 applies: meeting (E) on C1 leaves open why the claim is made on C1 and not on a wider contract.

### FC-E5 · 193 route families, and the finite monotone claim on each

> L305 | **Finite monotone claim.** If \(\Gamma\) is finite, \(\mathsf S\) is upward closed, and \(\Gamma\in\mathsf S\), then \(d\in\Gamma\) is critical for some route (**contributory**) exactly when \(d\in\bigcup\min\mathsf S\)

**The external reader (5).** "I checked every upward-closed route family containing the full commitment set for one through four commitments: 193 families, with no counterexample."

**Formal.** For |Γ| = 1, 2, 3, 4, the upward-closed families S ⊆ P(Γ) with Γ ∈ S number 2, 5, 19 and 167, 193 in all; on each, Contrib(d) ⟺ d ∈ ∪min S and Indisp(d) ⟺ d ∈ ∩min S for every d ∈ Γ.

**Type.** External example.

**Uses.** Inventions: I30, I77.

**Result.** CONFIRMED on the text under review. Reproduce: `cd "/home/user/ThreadSmith/Semantics/results/S104 Round 2 - maths" && python3 s104_external.py FC-E5`.

```
|Γ| = 1: 2 upward-closed families containing Γ
|Γ| = 2: 5 upward-closed families containing Γ
|Γ| = 3: 19 upward-closed families containing Γ
|Γ| = 4: 167 upward-closed families containing Γ
total 193; the finite monotone claim fails on 0 of them
```

**What it bears on.** The same space as FC37's first part, which went on to the 7,581 up-closures of antichains on five commitments, with the same result. The count is one less than each Dedekind number (3, 6, 20, 168), the empty family being the one up-set without Γ. The external reader adds that the problem of its 2.1 "survives precisely because the theorem can be correct while its criticality predicate is interpreted too strongly" (FC-E1).
