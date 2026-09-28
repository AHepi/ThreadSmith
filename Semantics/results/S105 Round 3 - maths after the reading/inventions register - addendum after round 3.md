# S105 Round 3 — inventions register, addendum after round 3

*Integration, 28 September 2026 (rule 6, rule 7; decisions S36, S40). The checkers' provisional inventions, numbered after I166, the last number in use (register I01–I102, addenda I103–I121, I122–I166). Source rows: `results/S105 Round 3 - area N - verdicts and formal fixes.md` §5 (not edited; the table below is the link). Where used: `formal core, after round 3.md`, `formal claims, after round 3.md`, `model after round 3/`. Recording an invention is not a move (rule 16).*

*The replies' own labels "I167"–"I172" (tabulation §7, note 1) are theirs, not register numbers; e.g. B6's "I168" (the image reading of obs) is the other choice of I172 below.*

**Counts.** 16 inventions, I167–I182, from 17 provisional ids: R3A1-03 and R3A3-01 are one choice (≺_h well founded), one number (I169). Recorded and not chosen: I174 (records keyed two ways), I176 (the exemption's extent, both run). Left to the owner: I136's quantifier (owner question R3-Q1; I176 rides on it). Settled in the text by a change (rule 6): I166 (R3A3-T1), I162 for Build (R3A3-T4), I169 (R3A3-T5), I50's narrow extent at L220 (R3A1-T5, FC104 there).

## Provisional id → I number

| prov. | I | prov. | I | prov. | I |
|---|---|---|---|---|---|
| R3A1-01 | I167 | R3A2-01 | I175 | R3A3-01 | I169 (= R3A1-03) |
| R3A1-02 | I168 | R3A2-02 | I176 | R3A3-02 | not used (area 3) |
| R3A1-03 | I169 | | | R3A3-03 | I177 |
| R3A1-04 | I170 | | | R3A3-04 | not used (area 3) |
| R3A1-05 | I171 | | | R3A3-05 | I178 |
| R3A1-06 | I172 | | | R3A3-06 | I179 |
| R3A1-07 | I173 | | | R3A3-07 | I180 |
| R3A1-08 | I174 | | | R3A3-08 | I181 |
| | | | | R3A3-09 | I182 |

## The inventions

| I | prov. | fills (line; item) | choice | other choices | why this one | used by |
|---|---|---|---|---|---|---|
| I167 | R3A1-01 | "its history" (L193), o_t, h(t) for a transport held more than once | provenance of a holding (t, o_t); h(t, o_t) the history that produced the holding; a relay or record carries its source's (D12.3) | one provenance per transport on its whole history (I53: FC12.new2 (b) gives Con); per transport on the history that first produced it (I128 as registered); B1's precedence (FC12.new2 (b), (c)) | L211, L405, L201 | D12.1, D12.3, D12.7, D12.8; claims_b `prov_fixed_points(rec_of=)`; FC12.new2 |
| I168 | R3A1-02 | "prepares t" in CT (L197; I56) | exact: t held at an output of the trace | transitive through contents built from its outputs (FC12.new3) | L405's last sentence, L201 | D12.2; FC12.new3 |
| I169 | R3A1-03, R3A3-01 | "acyclic causal precedence" (L375) under L195's staged formula | ≺_h well founded | acyclic only (no fixed point on an infinite descending chain: FC98.new1 (a), FC98.new2 (a)); well founded below o_t only | L526 "no endless descent"; L193 "exactly one"; D18.1's own proviso | D11.3, D18.1; R3A3-T5 (L375) |
| I170 | R3A1-04 | "represents … H, or the survival condition" (L195) | H and surv over 𝒯 as contents by L590's construction | the exclusion over t, cod t only (against L195's formula); a record reading (P3) | L590, D13.6 | D11.2; FC97.new1 |
| I171 | R3A1-05 | "a finite history H … actually encountered", "survived" (L195) | H ≠ ∅ | H = ∅ allowed (after round 2; FC77 parts 2, 3) | Q2 as asked and answered (S41); L13; I52's registered other choice | D12.1; claims_b `SEL_H_NONEMPTY`; FC77, FC30.new1 (e) |
| I172 | R3A1-06 | "the observed value" (L151) where g is not single on Sol | one value or ⊥, ≠ as D6.4 | the image g[Sol] (B6's "I168"); one value asked at both pairs | D3.2's ⊥; Q15's convention (S41) | D3.3; FC28.new2 |
| I173 | R3A1-07 | "immediately after" (D13.8, I165) | covering relation of ≺⁺ on h′ | every ordered pair (equal under D13.8's records: FC84.new2 (a)); every unordered pair (FC84.new2 (b)) | L55 "every change … carries"; the program's `episode` | D13.8; FC84.new2 |
| I174 | R3A1-08 | records in D13.8: Rec_h′(ρ_{q(o′)}) | recorded, not chosen: keyed by the new contract (D13.8) or by the change (the program) | — | they differ only where one contract is entered twice with one record | D13.8 note; claims_b `episode` |
| I175 | R3A2-01 | L315 "a candidate that nobody has offered is no one's rival": which offer (D8.3; W4) | Off(ℰ′, p), offered for p | ∃q Off(ℰ′, q); no offer clause (as D8.6 reads) | L317 "offered for it" | D8.3 note; no claim computes Riv |
| I176 | R3A2-02 | the exemption of I136's third choice ("a component the contract's own edit replaces") | not chosen; both run: alters k at σ(b) (some-exempt) / sets δ_E through k (some-exempt-set) | — | they differ only where a setting's value is also the identity's (FC23.new1 (f)) | core `SLOT_QUANTIFIER`; FC23.new1 |
| I177 | R3A3-03 | "a survival condition requiring fidelity on H" (L195), "enacted by the environment" (L481) | surv := Faithful_H ∧ Env on t's values at H, Env through Θ (none given: ⊤) | fidelity alone (after round 2, unregistered: FC80.new1 (a)); any condition on t (L574's step then need not hold) | L195 "requiring", L481, L574 | D12.1, D12.9, D15.8; claims_b `sel(env=)`; FC80.new1 |
| I178 | R3A3-05 | "for explanatory use of c" (L405) | o uses the claim 'Acc(ℰ)', c ℰ's organization, transport or contract; the claim need not hold | primitive (I148: L526's "(E)" unbacked); organization only (P5: no contract built, against L425); the claim must hold (against L403) | L526, L425, L449, L403; FC90.new1 (a), (b) | D13.3, D0.2 (UsesClaim); DEP |
| I179 | R3A3-06 | L526's grouped subjects ("(N), (G) depend on Deploy and Build"; "(P), (EX) depend on (G), (E), Deploy") | read together | each alone (New on Build, (P) on (G), (E), Deploy then fail: FC32.new1 (d)) | the definitions (D13.5, D14.2) | FC32.new1 |
| I180 | R3A3-07 | (EX)'s candidate data (L449) | δ_c quantified with c, p_c, t_c, Γ_c | supplied with c (as D9.10) | (EX) quantifies the rest | D14.7 |
| I181 | R3A3-08 | D18.1's nodes | the folds of D_TO_NODE; D0.2's classes (C_I, J_p, 𝒱, the stated construction, Desc as declared inputs L522 does not list) | a node per paragraph | a record of the graph; L522 not changed (S40) | claims_b DEP, D_TO_NODE, D0_2_R3A3; D0.2 |
| I182 | R3A3-09 | E9's instance (L620–L630) | 4 cells, frames 0..3, two things; occlusion of cells 1–2 at t = 1, 2; edits on the initial frame; S0 window 2; B0 where H0's windows never conflict; t0 keeps the frame where H0 is silent | edits at t = 1; occluded cells a third value (not computed) | L622, L624, L626; the smallest instance with L_occ = w = 2 | model/e9.py; FC102.new1, FC103.new1 |

## Registered inventions fixed, amended, settled or pointed to in round 3 (the register's entries are not edited)

| I | now | by |
|---|---|---|
| I44 | acyclic → well founded (I169) | D11.3 (A1 F1 = A3 F1); R3A3-T5 |
| I48 | H and surv typed as contents (I170) | D11.2 (A1 F6) |
| I50 | narrow extent written at L220 (FC104 settled there) | D5.7 (A1 F11); R3A1-T5 |
| I52 | its registered other choice taken: H ≠ ∅ (I171); survival condition surv (I177) | D12.1 (A1 F5; A3 F2) |
| I53, I128 | per holding (I167); a relay or record carries its source's provenance | D12.1, D12.3 (A1 F2, F3) |
| I56 | "prepares" in CT exact (I168) | D12.2 (A1 F4) |
| I94 | FC18's untranslated reading kept as a look | FC18 (A3 F5) |
| I124 | the union written in D4.6 (O_j) | D4.6 (A1 F10) |
| I136 | open: owner question R3-Q1 | D6.3 note (A2 W3) |
| I148 | replaced: ExplUse defined through UsesClaim (I178) | D13.3, D0.2 (A3 F3) |
| I162 | Held's extent that of D12.5 (Rep ⇒ Held); settled in the text for Build | D18.1 (A1 F7); R3A3-T4 |
| I163 | obs where g is not single on Sol: ⊥ (I172) | D3.3 (A1 F8) |
| I165 | "immediately after" defined (I173) | D13.8 (A1 F9) |
| I166 | settled in the text at L397 | D9.6; R3A3-T1 |
| I20 | δ_c quantified in (EX) (I180) | D14.7 (A3 F4) |
