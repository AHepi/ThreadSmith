# S104 Round 2 — inventions register, addendum for the external examples

*Log S104, review round 2 (the maths round), 27 September 2026. Decision S36: "Also, if implementation forces invention, that needs to be recorded." Written by a Claude subagent while the round's runs were going and before any round-2 reply was opened (see `results/S104 Round 2 - addendum to the reading rule, the external cross-examination, written before any reply was opened.md`). It continues the numbering of the committed `inventions register.md` (I01–I102), which is not written to. The text under review is `tests/103 The semantics, standing alone, after round 1.md`, md5 f31ebb1f050783f1a84f6136cec20fcd (compared by `s104_external.py` before every run; not written to). Every quotation below was compared by program with the line it names.*

**What this is.** The choices that reproducing the formal examples of the external cross-examination the owner supplied (`results/S104 Round 2 - external cross-examination supplied by the owner.txt`) forced on top of the model's own: the encoding of each example where the document leaves something open, and two readings used only to show what a result rests on. As in the register, nothing invented is the text's own content, and no entry is offered as what the text means. The claims are FC-E1 to FC-E5 in `formal claims - addendum for the external examples.md`; the program is `s104_external.py`, which imports the committed `model/` and changes none of it.

**Counts.** 6 inventions, I103–I108. Each of FC-E1 to FC-E4 uses one encoding entry; I104 and I106 are used only by the variants that show what FC-E1 and FC-E2 rest on. FC-E5 uses none of them (it rests on I30 and I77).

## Index

| id | invention | lines | claims that use it |
| --- | --- | --- | --- |
| I103 | The external 2.1 example encoded: two unrelated dependencies, a zero background, nine settings | L231, L287, L313 | FC-E1 |
| I104 | A restriction that removes the ports no remaining component constrains, and projects π | L231, L287 | FC-E1 (variant (b) only) |
| I105 | The external 2.3 example encoded: one relation {(0,0),(1,1)}, read forward and reversed | L103, L109 | FC-E2 |
| I106 | 'Output' read at edits other than the identity | L109 | FC-E2 (the other readings only) |
| I107 | The external 2.3 second example encoded: a response and a reading of one port, and a recalibration | L109, L123, L124, L127 | FC-E3 |
| I108 | The external 3.1 example encoded: memory, readout and response; a readout offered as a cause | L37, L151 | FC-E4 |

### I103 · The external 2.1 example encoded: two unrelated dependencies, a zero background, nine settings

**The sentence it fills in for.**

> L231 | the boundary conditions of \(E\) and the components of \(E\) outside \(\Gamma\), including any of them that assigns an input, belong to the named background of Part VI.

> L287 | For \(W\subseteq\Gamma\), let \(E|W\) retain the commitments in \(W\) with the named background fixed; the commitments of \(E|W\) are \(W\).

> L313 | A commitment \(d\) of a candidate that has a route does no work by itself in it when every route stays a route after \(d\) is added to it and after \(d\) is removed from it

**What was invented.** The external reader fixes four two-valued variables, k: Y = X and d: V = U, identity transports, Γ = {k, d}, a contract of the baseline and every partial setting of X and U (nine edits, the identity among them), and "Background assignments set unset inputs to zero". The encoding adds: one boundary b0; the zero background carried by two components c_X: X = 0 and c_U: U = 0 of the named background (I79's way), each replaced by the settings of its port; composition of settings by override (I78's surgical family); k's footprint (X, Y) and d's (U, V), each with the relation {(0,0),(1,1)} at every edit (neither is set, so neither is replaced); the question's query reads Y (Q_w with δ = Y, I20); the candidate's organization a copy of the target, with π, τ and σ the identity and λ(j) = {j} with identity port translations for every component (I14, I81).

**Other choices that were possible.**

- the zero background carried by the boundary, as values of designated boundary ports (I79's other choice)
- a contract that also sets Y or V (then the target's answer can be set directly, and NC1 and the stated scope need checking again)
- d placed in the named background rather than among the commitments (computed as FC-E1's variant (a): the candidate meets (E) with Γ = {k}, and d is no commitment, so the question of its criticality does not arise)

**Used by.** Code: `s104_external.py` (e1_org, fc_e1). Claims: FC-E1.

**Results that depend on it.** FC-E1 — CONFIRMED (reproduced on the text under review).

### I104 · A restriction that removes the ports no remaining component constrains, and projects π

**The sentence it fills in for.**

> L287 | Fix \(\mathcal E\) and a declared restriction operation.

> L231 | for \(E|W\), \(t'\) is \(t\) with \(\lambda\) restricted to the components of \(E|W\), and \(\Gamma'\) is \(W\).

**What was invented.** E|W removes the components of Γ ∖ W together with every port that lies in no footprint of a component left, except the designated answer port, which is kept (free where nothing constrains it); π is t's π followed by the projection onto the ports left; λ is restricted to the components left; the commitments are W. This makes exact the first other choice the register lists under I29 ("remove Γ \ W from J_E (their ports then free, or removed)"), in its second form. It changes π, which L231's "t′ is t with λ restricted" does not. Used only to show what FC-E1 rests on; the model's default stays I29.

**Other choices that were possible.**

- I29: deletion, every port and component kept, π unchanged (the model's default, and FC-E1's reading)
- removal of components with their ports kept and left free (the register's I29, first form; for a query that reads a port it gives the same solutions as deletion, as the check of the formalization notes in its §2b)
- removal of the designated answer port as well, where nothing left constrains it (the answer is then undefined, and (A) fails at every pair)

**Used by.** Code: `s104_external.py` (restrict_removing). Claims: FC-E1, variant (b) only.

**Results that depend on it.** FC-E1, variant (b): under I104 the full candidate's routes are {{k}, {k,d}}, {d} is critical in no route, d is not globally indispensable, and d does no work by itself (L313). FC-E1's own result does not use it.

### I105 · The external 2.3 example encoded: one relation {(0,0),(1,1)}, read forward and reversed

**The sentence it fills in for.**

> L109 | A port is an **output** of component \(j\) when its value is determined by \(L_j\) given the other ports of \(V_j\) across \(B\).

> L103 | An edit that sets a port replaces the component assigning that port

**What was invented.** The external reader fixes the relation L = {(0,0),(1,1)} on two two-valued ports and the two assignments Y := X and X := Y. The encoding adds two organizations with one boundary b0 and every partial setting of X and Y as edits (override composition, I78), a setting replacing the component whose home port it sets (I04): D_fwd, where k on (X, Y) has home port Y and a background component c_X: X = 0 has home port X; and D_rev, where the same k has home port X and a background component c_Y: Y = 0 has home port Y. Away from the settings of its home port, k's relation is {(0,0),(1,1)}.

**Other choices that were possible.**

- only the settings of the upstream port admitted (then the downstream port has no setting edit, and I04 leaves its assigning component undefined)
- no background component (the upstream port free at the baseline; output status is unchanged, since it reads k alone)

**Used by.** Code: `s104_external.py` (fc_e2). Claims: FC-E2.

**Results that depend on it.** FC-E2 — CONFIRMED (reproduced on the text under review).

### I106 · 'Output' read at edits other than the identity

**The sentence it fills in for.**

> L109 | A port is an **output** of component \(j\) when its value is determined by \(L_j\) given the other ports of \(V_j\) across \(B\).

**What was invented.** Two readings of which edit L_j is read at, besides I05's identity edit: (a) at every edit at which L_j is as at the identity edit, the reading given here to I05's first other choice ("at every edit of A that does not replace j"), since under D2.1 a composite of two settings is no setting edit (the check of the formalization, H01), so that "replace" is read as "alter"; (b) at every edit of A, those that alter j included. Used only to show what FC-E2 rests on.

**Other choices that were possible.**

- I05: the identity edit alone (the model's default, and FC-E2's reading)
- (a) with "replace" read through D2.1's surgical form: then a composite setting of k's home port and another port is not left out, and in D_fwd X is no output of k while Y is (the first run of `s104_external.py` used this reading; it gives what (b) gives)

**Used by.** Code: `s104_external.py` (out_at). Claims: FC-E2, the other readings only.

**Results that depend on it.** FC-E2: under (a), as under I05, both ports are outputs of k in D_fwd and in D_rev; under (b), only k's home port is (Y in D_fwd, X in D_rev), because at a setting of the home port k's relation becomes a slice that leaves the other port free. Under (b), output status follows the direction only through the setting edits that replace k, which is what I04 reads the assigning component from.

### I107 · The external 2.3 second example encoded: a response and a reading of one port, and a recalibration

**The sentence it fills in for.**

> L123 | - a **causal assignment** has a signature that changes under intervention on its output port and is invariant under observation edits;

> L124 | - a **measurement** has a signature invariant under interventions on the measured port and variable under edits to the measuring relation;

> L127 | In particular, a part that reads or reports another part has a measurement's signature

> L109 | A port is an **observation** when \(A\) contains an edit that alters the relation reporting it without altering what it reports

**What was invented.** The external reader fixes a component Y := X, a measuring component N := X, and an upstream intervention on X. The encoding: D_ro with ports X, N, Y, each two-valued, and one boundary b0; c_X: X = 0 (background); c_Y on (X, Y): Y = X (the response); c_N on (X, N): N = X (the reading); edits every partial setting of X, N and Y (27, override composition, I78), a setting replacing its port's home component (I04). Contracts: C_single, the baseline and the six single settings; C_all, every edit. Then D_ro+recal: D_ro with one more edit recal(c_N), which replaces c_N's relation by N = 1 − X and alters no other component; its composites with other edits are undefined (a partial composition, I01); contract C_single with (recal(c_N), b0) added. The families are D4.6's, under both readings of observation edits (I06).

**Other choices that were possible.**

- a recalibration that makes N constant, or one for c_Y as well (the latter makes the two components alike again)
- the recalibration composed with the settings (an action law, I78's surgical family extended)
- the example written through a memory port, as in FC-E4's target (c_N: N = M and c_Y: Y = M); the families are then read on the same pattern

**Used by.** Code: `s104_external.py` (fc_e3). Claims: FC-E3.

**Results that depend on it.** FC-E3 — CONFIRMED (reproduced on the text under review). On C_all, both components are in the rule family under both readings because a composite of two settings is no setting edit (the check's H01 and R13); the two still coincide there.

### I108 · The external 3.1 example encoded: memory, readout and response; a readout offered as a cause

**The sentence it fills in for.**

> L151 | A measure that identifies an outcome, together with a prediction of the outcome from it through a transport faithful on the contract, answers the identification question; whether the measured part also produces the outcome is the production question, and the first answer is not the second.

> L37 | A correlation has no component that responds to an intervention on its supposed input; a cause does.

**What was invented.** The external reader fixes the target M := X, N := M, Y := M, the proposal Y := N, "ordinary cue changes", and the added intervention X = 1, do(N = 0). The encoding: the target D_mem with ports X, M, N, Y, each two-valued, one boundary b0, components c_X: X = 0 (background), c_M on (X, M): M = X, c_N on (M, N): N = M, c_Y on (M, Y): Y = M; edits every partial setting of the four ports (81, override composition, I78), a setting replacing its port's home component (I04); the query reads Y (I20). Contracts: C1, the baseline and the settings of X (the cue changes); C2, C1 and the composite setting X = 1, N = 0. The candidate E_readout: the same ports, edits and components with c_Yp on (N, Y): Y = N in place of c_Y; π, τ and σ the identity; λ(c_Yp) = {c_N, c_Y} of the target with identity translations of N and Y (M hidden), and λ(j) = {j} for the other components; Γ = {c_M, c_N, c_Yp}, and separately Γ = {c_Yp}; c_X in the named background.

**Other choices that were possible.**

- C2 with the setting N = 0 alone as well, or in place of the composite
- λ(c_Yp) = {c_M, c_N, c_Y} (a larger counterpart with more hidden ports)
- a candidate organization with no port M (then π drops M, and λ must still give each component a counterpart)

**Used by.** Code: `s104_external.py` (mem_orgs, fc_e4). Claims: FC-E4.

**Results that depend on it.** FC-E4 — CONFIRMED (reproduced on the text under review).
