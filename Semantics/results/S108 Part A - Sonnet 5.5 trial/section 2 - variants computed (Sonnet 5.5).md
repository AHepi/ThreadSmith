# Section 2, variants computed (Sonnet 5.5 trial)

Status: computed. Written by the trial agent (Sonnet 5.5) working alone from the reply `S108 Part A - returns/s108_glm_section2.response.txt`, the round-4 program and the rule text; the other agent's work was not opened. Computation only: nothing here is a change to the theory (S40), and every statement below is a result of running the program, or says that it is not settled by computation and what would settle it. The edges are also in `section 2 - variants computed (Sonnet 5.5).json`. Start and end times are in `timing.txt`.

## 1. What was computed, and how to read it

Scope: the in-scope variants V2.1 to V2.7 of the reply's section 2. V2.8 is flagged out of scope by the tabulation and is not implemented (its two edge rows are listed in section 8 and not computed).

Words used. "Acc" is the candidate meeting (E) after S106: F1, F2, A, Dependence (NC0 and NC2) and NonVacuous. "Off" is the current definition (the default). "On" is one variant switched on alone; two variants are never on together. "Acc and not Dec" is the candidate counting as an explanation (Expl := Acc and not Dec, D12.1 to D12.3). "Holds" and "fails" are the program's T and F. A "witness" is the pair (a,b) of the contract, with the commitments removed, that NC2 uses. "Routes" S are the sets W of commitments for which the restricted candidate still gives the account (D7.2).

The variants, each a switch in the copy of the round-4 program (`section 2 model/`), read from the environment variable `S108_S2`; nothing set means the round-4 program exactly.

| Variant | What it changes, in plain words | Reply's kind | Switch |
|---|---|---|---|
| V2.1 | Dependence (NC2) asks only that the answer differs at some pair of the contract; the test that removing commitments loses the difference, and the removed group, are deleted | weaken | V2.1 |
| V2.2 | the removed group of commitments in Dependence must be a single commitment | strengthen | V2.2 |
| V2.3 | the pair that witnesses Dependence must have an edit other than the identity (a is not 1) | strengthen | V2.3 |
| V2.3b | the same, read through the transport: the pair's translated edit is not 1 (my reading, section 2) | strengthen | V2.3b |
| V2.4 | (E) again has the written-in test NC1 as a conjunct (round 3's reading) | strengthen | V2.4 |
| V2.5 | Sel (D12.1) admits an empty history H | weaken | V2.5 |
| V2.6 | conflict (D8.2) counts only at pairs of the contract C | weaken | V2.6 |
| V2.7 | ConfCl (D8.5) keeps only its first disjunct (the answer route); the route through what the parts must do is cut | weaken | V2.7 |

Where the program lives and how each place was computed:
1. worked cases: the 27 worked cases of the text (the round-4 script `s106_cases.py`) plus the student's declared formula, 28 in all; driver `s108_section2_cases.py`.
2. external examples FC-E1 to FC-E5 and the creative transport case CT1 to CT8: 17 named candidates, driver `s108_section2_external.py`; the two round-4 scripts `s104_external.py`, `s104_creative_transport.py` and `s106_cases.py` were also run with each variant on and compared line by line with off. FC-E2, FC-E3 and FC-E5 build no candidate and call no Acc.
3. small cases the reply gives, and a few I added: driver `s108_section2_small.py` (11 cases, section 4).
4. generated worlds at scale 4: 17280 worlds over 108 sizes (seed 108101, the same worlds for every variant, digest c6cce42db46390653a2761a5a25aade9f51589a90f5e9e1f262dcb0d9a9c7f9a); driver `s108_section2_worlds.py`. V2.6 and V2.7 act on conflict, so they were run on worlds that carry a conflict question (section 5).
5. the whole suite (142 claims, 340 parts) at scale 4, time cap 45, once with nothing on and once with each variant on. The run with nothing on reproduces the round-4 base run exactly (133 hold, 2 counterexample, 7 not tested; 0 of 340 parts moved).

Every run used `env -i ... PYTHONHASHSEED=0 timeout N python3 -B`, standard library only. The printouts are in `printouts/` (section 9).

## 2. Inventions of this trial (S36)

1. The pairs proxy for problems. D10.4's Prob_j and ETV_j are not program functions. A "problem" between two candidates is read here as: both meet Acc, they are rivals (core.rivals), and its kind is core.problem_kind (kind i when a conflict pair lies in C, kind ii when none does). ETV is read as its kind-ii clause. Used only for the "problems" counts in sections 5 and 6.
2. V2.3b. The reply's "a pair of C with a not 1" can be read on the edit of the contract (V2.3) or on the edit after translation, tau(a) not 1 (V2.3b). Both are computed. A third reading in the reply ("pairs other than (1,b0)") was not implemented.
3. V2.2 as a singleton. The reply's other choice "a block critical in some route" was not implemented.
4. The finite cousin of L311 (small case C): a Candidate is finite (I77), so the infinitary candidate of L311 cannot be built; the cousin has three commitments, no route of one commitment, every pair a route.
5. The scenario labels (i) constructed, (ii) declared with no pair tried, (iii) declared with one pair tried, for the three ways provenance_of can present a transport. The choice of these three is mine.
6. V2.5's switch `SEL_H_NONEMPTY` in `claims_b.py`: the condition "H nonempty" in Sel is dropped when V2.5 is on.
7. V2.7's cut: after the existence clauses of area 2, the second disjunct is set to fail.
8. Case G (a candidate with no commitments) and cases I and J, added because V2.1 and V2.3 have edges there that the reply did not name.
9. The V2.6 and V2.7 world sets (worlds with a conflict question, seeds 108106 and 108107), and the pairs runs (seed 108106, sizes of the conflict harness).

## 3. Which variants change the explanation definition

Expl := Acc and not Dec. Computed and checked in the source:

| Variant | Changes Expl? | How |
|---|---|---|
| V2.1 | yes, weaker | Acc: more candidates meet it (59 of 17280 worlds move F to T) |
| V2.2 | yes, stronger | Acc: fewer (16 worlds T to F) |
| V2.3 | yes, stronger | Acc: 264 worlds T to F (V2.3b: 271) |
| V2.4 | yes, stronger | Acc: 952 worlds T to F, 1022 to 70 |
| V2.5 | yes, weaker | Dec: in scenario (ii) Dec falls from 17280 worlds to 408; Acc unchanged, Acc and not Dec goes from 0 to 1022 |
| V2.6 | no | Acc and Dec never call conflict; 0 Acc moves in every run |
| V2.7 | no | the same; it moves ConfCl only |

The source check (a scan of the function bodies in `core.py`, `claims_b.py`, `claims_s41.py`): `account`, `NC2`, `routes`, `sel`, `con` and `provenance_of` do not call `conflict`, `rivals`, `conf_claim`, `conflict_pairs` or `problem_kind` directly. The computed runs agree (V2.6: 0 Acc moves over 19193 pairs).

## 4. Worked cases, small cases, external and creative cases

### 4.1 The 28 worked cases (27 of the text plus the student's declared formula)

23 of the 28 hold Acc when nothing is on.

| Variant | Acc | Other things that move |
|---|---|---|
| V2.1 | no Acc moves | the witness moves in 26 cases: the removed group becomes empty (printed as `[]`); routes unchanged in all 28 |
| V2.2 | no moves | nothing |
| V2.3 | 1 case T to F: E1 reversed calculation on the identification contract C_id | witness moves in 3 more (L257: (1,b0) to (a,b0); E9 with t1 and with t1 after psi: (1,b0m1z) to (disp1_0,b0m1z)) |
| V2.3b | the same 1 case T to F | witness moves in the 2 E9 cases; L257 keeps (1,b0), because tau(1) is not 1 there (the one difference from V2.3) |
| V2.4 | 10 cases T to F: E1 reversed under Mimo's tau' (H only), L269 E_enc on C1 and C2, L273, M1, M2, M3, R3-Q1 (the hand-turned vane), E8 p_delta, the S44 shop sign with one part | routes of the same 10 change; the other 13 Acc cases stay, among them E1 forward (three cases), the shop sign with two parts, M5, M13, E5, E9, the sign with a day port and the student's formula |
| V2.5 | no Acc moves | Acc and not Dec in scenario (ii) goes F to T for all 23 Acc cases; scenarios (i) and (iii) do not move |
| V2.6, V2.7 | no moves | nothing |

E6 skew-symmetric statuses (FC63 c-i, c-ii) do not move under any variant.

### 4.2 Small cases (the reply's, and four added)

| Case | What it is | Off | V2.1 | V2.2 | V2.3 / V2.3b | V2.4 | V2.5 | V2.6 | V2.7 |
|---|---|---|---|---|---|---|---|---|---|
| A (reply, V2.1) | x,y,z, idle commitment dz, identity transport, Gamma = {dz} | Acc fails, S empty | Acc holds; S {} to {{},{dz}}; witness ((e,b0), []) | no move | no move | no move | no move | no move | no move |
| B (reply, V2.2 L307) | two commitments each a route, S = {{ja},{jb},{ja,jb}} | Acc holds | witness block only; S unchanged | Acc fails; S loses {ja,jb} | no move | Acc fails; S empty | scenario (ii) F to T | no move | no move |
| C (reply, V2.2 L311, finite cousin) | Gamma = {d1,d2,d3}, no route of one commitment, every pair a route | Acc holds | witness block only | Acc fails; S loses {d1,d2,d3} | no move | no move | scenario (ii) | no move | no move |
| D (reply's unsettled edge, L309) | interference: the full candidate fails F1, the subset {ka} is a route, S = {{ka}} | Acc fails | witness block only; S = {{ka}} unchanged | no move | no move | no move | no move | no move | no move |
| E (reply, V2.7 wheel) | Gamma = {c}, chi = "perpetual motion is impossible" | ConfCl holds (first disjunct fails, second holds) | no move | no move | no move | no move | no move | no move | ConfCl fails |
| F (reply, V2.6 tilt and myth) | Greeks' contract | tilt and myth are rivals, kind ii | no move | no move | no move | Acc(myth1) T to F | no move | not rivals; the finer contract is unchanged (rivals, kind i) | no move |
| G (added) | no commitments (Gamma = {}), x,y,z target | Acc fails | Acc holds; S {} to {{}} | no move | no move | no move | no move | no move | no move |
| H1, H2 (reply, V2.3) | reversed and forward calculations on C_id = {1} x B | Acc holds | no move | no move | Acc fails; S empty | no move | scenario (ii) | no move | no move |
| I (added) | a contract {1} x B with two boundaries | Acc holds | no move | no move | Acc fails; S empty | no move | scenario (ii) | no move | no move |
| J (added) | a contrast that lies outside C | Acc fails | no move (V2.1 does not read a contrast outside C) | no move | no move | no move | no move | no move | no move |

The reply's unsettled edge (V2.1 and frozen L309.s1) is settled by case D: under V2.1 the full candidate still fails F1, the subset {ka} is still a route, and S is unchanged.

### 4.3 External examples and the creative transport case (17 named candidates)

FC-E1 (full candidate, E restricted to {k}, variants (a) and (b)), FC-E4 (C1 and C2, each with two choices of Gamma), CT1, CT3 (reading R-B), CT5 (the direct pair on the target that cannot invert, and on the full target), CT6 (equality pair and xor pair), CT7, CT8.

Only V2.5 moves any of them. Acc and not Dec in scenario (ii) goes F to T for the 8 that hold Acc: FC-E1 full, FC-E1 variants (a) and (b), FC-E4 C1 (twice), CT1, CT5 on the non-inverting target, CT8. The 9 that fail Acc stay: FC-E1 E restricted to {k}, FC-E4 C2 (twice), CT3 R-B, CT5 full target, CT6 (both), CT7. V2.1, V2.2, V2.3, V2.3b, V2.4, V2.6 and V2.7 move no Acc of the 17. V2.1 and V2.3 change no result of the populations of 256 pairs (CT2, CT4, CT5).

The round-4 scripts run with each variant on differ from off in a few printed lines only: V2.1 in 2 lines of `s104_external` (the NC2 witness block `['k']` becomes `[]`), 0 lines of the creative transport script; V2.3 and V2.3b in 4 lines of `s106_cases` (the E1 identification line C_id). No other variant moves any line.

## 5. Generated worlds at scale 4

17280 worlds over 108 sizes (seed 108101). Acc off holds in 1022 (E_enc 919, lookup 91, random 12). Gamma has 0 commitments in 355 worlds, 1 in 13119, 2 in 3212, 3 in 594. Worlds with C in {1} x B: 8855 (Acc off 181); worlds with tau[C] in {1} x B: 9723 (Acc off 193).

| Variant | Candidates whose result differs, off against on | Smallest witness |
|---|---|---|
| V2.1 | Acc F to T in 59 (Gamma has 1 commitment: 54, 2: 5, none: 0); Acc on 1081; families E_enc 57, random 2. The NC2/Dependence conjunct moves in 346 worlds; the NC2 witness differs in 3558; routes S differ in 71; the empty set enters S in 64; the interference shape (a subset of the commitments is a route, the full set is not) enters S in 12 (45 to 57). C in {1} x B: Acc 181 to 187; tau[C] in {1} x B: 193 to 199 | size ports=1 dom<=1 comps=2 boundaries=1 edits=2, E_enc, Gamma = {k0}, C = {(1,b0),(e1,b0)}. Off: NC2 fails, S empty. On: witness ((e1,b0), []), S = {{k0},{}} |
| V2.2 | Acc T to F in 16 (Gamma 2 commitments: 15, 3: 1), all E_enc; Acc on 1006. Witness differs in 111; routes differ in 16, all entering the interference shape (45 to 61) | size ports=1 dom<=1 comps=2 boundaries=1 edits=2, E_enc, Gamma = {k0,k1}, C = {(1,b0),(e1,b0),(e2,b0)}. Off: witness ((e2,b0),[k0,k1]), S = {{k0,k1},{k0},{k1}}. On: no witness, S = {{k0},{k1}} |
| V2.3 | Acc T to F in 264 (Gamma 1: 199, 2: 63, 3: 2; E_enc 236, lookup 24, random 4); Acc on 758. C in {1} x B: Acc 181 to 0; tau[C] in {1} x B: 193 to 6. Routes differ in 284 (all become empty); witness differs in 1166 | size ports=1 dom<=1 comps=1 boundaries=2 edits=0, E_enc, Gamma = {k0}, C = {(1,b0),(1,b1)}. Off: witness ((1,b0),[k0]), S = {{k0}}. On: no witness, S empty |
| V2.3b | Acc T to F in 271 (Gamma 1: 205, 2: 64, 3: 2); Acc on 751. C in {1} x B: 181 to 0; tau[C] in {1} x B: 193 to 0. Routes differ in 294; witness differs in 1214 | the same world as V2.3's |
| V2.4 | Acc T to F in 952 (Gamma 1: 724, 2: 213, 3: 15; E_enc 850, lookup 91, random 11); Acc on 70. Routes differ in 994. C in {1} x B: 181 to 12; tau[C] in {1} x B: 193 to 14. The NC2/Dependence conjunct itself does not move (the loss is through NC1). No candidate moves F to T | size ports=1 dom<=1 comps=1 boundaries=1 edits=1, E_enc, Gamma = {k0}, C = {(1,b0),([alt:h_p0],b0)}. Witness unchanged, NC2 holds, S {{k0}} to {}, Acc T to F through NC1 |
| V2.5 | Acc unchanged (1022). Scenario (ii): Acc and not Dec 0 to 1022, Dec 17280 to 408, Dec differs in 16872 (1022 of them among Acc worlds). Scenarios (i) and (iii) unchanged (Acc and not Dec 1022 both ways; Dec 0 and 6337 both ways) | the same world as V2.4's |
| V2.6 | 1920 worlds with a conflict question (seed 108106, 48 sizes): Acc moves 0; Riv 1097 to 955; conflict pairs differ in 398 (on: every conflict pair lies in C); kind ii 142 to 0; kind i 955 unchanged; rivalry lost while both candidates hold Acc: 3 | size ports=1 dom<=1 comps=1 boundaries=1 edits=1, C = {(1,b0)}. Off: conflict pair (e1,b0) lies outside C, kind ii. Both candidates fail Acc; a second witness has both holding Acc |
| V2.7 | 1919 worlds, 4318 pairs (seed 108107): ConfCl holds to fails in 393 (1873 to 1480), all with the second disjunct alone holding; first disjunct 1480 off and on; second disjunct 1803 to 0; first disjunct alone (off) 70 | size ports=1 dom<=1 comps=2 boundaries=1 edits=0, pair (1,b0), Gamma = {k0,k1}, first disjunct fails, second holds, the candidate's answer is undetermined |

The reply's V2.3 claim "no candidate on any contract of the form {1} x B" is computed for C in {1} x B (181 to 0). Read through the transport (tau[C] in {1} x B), V2.3 leaves 6 worlds where Acc holds, V2.3b leaves 0; this is the reason V2.3b was added.

Pairs of candidates (the proxy of section 2, invention 1), seed 108106, sizes of the conflict harness:

| Variant, scale | Acc moves | Problems, off to on |
|---|---|---|
| V2.1 x4 (1920 pairs) | 4 F to T | 3 to 3 |
| V2.1 x40 (19193 pairs) | 78 F to T, 0 T to F | 47 to 57 (10 gained, all kind ii; both candidates Acc 329 to 365) |
| V2.2 x4 | 1 T to F | 3 to 3 |
| V2.2 x40 | 15 T to F | 47 to 47 (none lost, none gained; both Acc 329 to 324) |
| V2.3 x4 | 75 T to F | 3 to 1 (2 lost, kind ii; both Acc 34 to 17) |
| V2.3b x4 | 77 T to F | 3 to 1 (both Acc 34 to 16) |
| V2.4 x4 | 149 T to F | 3 to 0 (3 lost, kind ii; both Acc 34 to 1) |
| V2.6 x40 | 0 | 47 to 0 (all 47 lost, all kind ii; both Acc 329 to 329) |

In every pairs run, problems of kind i are 0 off and on: all problems found are kind ii. So the runs say nothing about problems of kind i.

## 6. The whole suite with each variant on

Off reproduces the base exactly. Claim-level statuses (holds / counterexample / not tested), then the claims whose result moves.

| Variant | Statuses | Claims that move |
|---|---|---|
| V2.1 | 133 / 2 / 7 | FC29 count hypothesis_met 3238 to 3577; the printed NC2 witness (block `[]`) moves in FC21, FC22, FC23.new2, FC26, FC29, FC62, FC63 (text only) |
| V2.2 | 133 / 2 / 7 | counts only, in FC29, FC37, FC46, FC51 |
| V2.3 | 132 / 3 / 7 | FC25.new2 (a) goes from holds to counterexample; FC23 (b) with satisfiable background goes from holds to counterexample (FC23's claim status was already counterexample); 12 parts move: FC23 (3), FC23.new1 (1), FC25.new2 (2), FC29, FC34, FC37, FC46, FC51, FC74 |
| V2.3b | 132 / 3 / 7 | the same claims as V2.3; FC29 hypothesis_met 3238 to 2445 (V2.3: 2534); FC21's witness line does not differ; 12 parts move |
| V2.4 | 128 / 7 / 7 | FC23.new2, FC23.new5, FC25.new2, FC27.new1, FC72.new2 go to counterexample; 28 parts move |
| V2.5 | 132 / 3 / 7 | FC77 (the H empty part) goes to counterexample |
| V2.6 | 132 / 3 / 7 | FC72.new2 (b) and (c) go to counterexample; counts move in FC47 (1666 to 1460), FC49 (1611 to 1426), FC50 (572 to 0) |
| V2.7 | 132 / 3 / 7 | FC52 (the restated area 2 part) goes to counterexample; FC53 and FC54 hold |

FC110's one text difference in every comparison is the trailing "total N s" timing line (an artifact). FC107 under V2.4 differs only in a printed generated label. FC54 (ConfG implies not Conf) holds under V2.7: `conf_given` reads the meet table and does not call `conf_claim`.

## 7. The reply's traces, checked against the computation

| Variant | Reply's statement | Result |
|---|---|---|
| V2.1 | the x,y,z candidate meets (E) after V2.1 | computed (case A) |
| V2.1 | "still not an explanation: identity transport declared" | holds only in scenario (ii); in scenarios (i) and (iii) the case A candidate is Acc and not Dec after V2.1 (contradicted there) |
| V2.1 | "newly meeting (E): the written-in candidate" | contradicted: L273's written-in candidate already meets Acc off (after S106), so it does not newly meet it; the idle-commitment candidate does (case A) |
| V2.1 | "which stop: none" | computed: 0 candidates T to F in 17280 worlds, in the pairs runs and in the worked cases |
| V2.2 | L307's redundant candidate stops meeting (E) | computed (case B) |
| V2.2 | L311's infinitary candidate stops meeting (E) | not settled by computation (a Candidate is finite, I77); the finite cousin, case C, does |
| V2.3 | E_rev and E_fwd on C_id stop meeting (E); "M13 unaffected" | computed (cases H1, H2; M13 keeps Acc and its witness) |
| V2.3 | "every candidate on every contract {1} x B" | computed for C in {1} x B (181 to 0); qualified for tau[C] in {1} x B: 6 worlds remain under V2.3, 0 under V2.3b |
| V2.4 | E_enc, one-part shop sign, myth1, M1 to M3, lookup stop; E_fwd, two-part shop sign, myth2 stay | computed (section 4.1; worlds: lookup 91 of 91 stop) |
| V2.4 | "newly counting: none" | computed: 0 F to T in 17280 worlds |
| V2.5 | the student's declared copy becomes Acc and not Dec | computed in scenario (ii); in (iii) it already holds off |
| V2.6 | tilt and myth are not rivals on the Greeks' contract; the finer contract is unaffected | computed (case F) |
| V2.7 | the wheel candidate's ConfCl holds off, fails on | computed (case E) |
| V2.7 | the ruling-out argument of L315.s14 lapses | not settled by computation: the program has no function for an assessor's ruling out; it would need Out_j programmed |

## 8. The edges

Status words: computed (the reply's "why" is what the computation shows); contradicted (the computation shows otherwise); not settled by computation (with what would settle it); mixed (parts carry one of the three). The kind label of a row (blocks, moves, constrains, changes with) is not something a program can compute; only the "why" clause is checked. Rows r13 and r14 are computed as an effect.

| Row | Variant, kind, item | Status | Computed result, or what would settle it |
|---|---|---|---|
| r1 | V2.1 moves Dependence (D6.5) | computed | 59 worlds F to T; cases A and G |
| r2 | V2.1 changes with D7.2 routes (L289) | mixed | computed: the empty set enters S in 64 worlds; L307 and L309 set systems stay unchanged (cases B, D). Not settled by computation: "L293.s1 and L299.s1 still readable" (about reading frozen sentences; a reading by the owner or a text check would settle it) |
| r3 | V2.1 constrains L275.n1 | computed | case J no move; FC29 holds |
| r4 | V2.2 blocks L311.s2 | mixed | computed: the finite cousin (case C) separates the collective block from (E). Not settled by computation: the infinitary L311 candidate (an infinite-Gamma semantics, or the owner's admission of infinite candidates, would settle it) |
| r5 | V2.2 constrains L299.s1 | computed | cases B and C; 16 worlds |
| r6 | V2.2 changes with D10.4, D10.6 ("fewer problems posed, none of the second kind from collective candidates") | contradicted, on the proxy | problems 3 to 3 (x4) and 47 to 47 (x40), none lost, none gained; every problem found is kind ii. A program function for Prob_j would settle it without the proxy |
| r7 | V2.3 blocks L329.s3 (identification) and E2 | computed | cases H1, H2, I; 181 to 0 for C in {1} x B |
| r8 | V2.3 changes with D3.3 (section 1) | not settled by computation | it concerns how D3.3 classifies contracts; programming D3.3's classification would settle it |
| r9 | V2.3 constrains L253.s1 | computed | the query is untouched; witness pairs move in L257 and E9; Acc also moves where no other witness exists |
| r10 | V2.4 blocks (owner decision S45) | not settled by computation | it concerns S45 and the frozen text. Computed result only: 5 claims that encode S44 and S45 go to counterexample |
| r11 | V2.4 moves (E) and Bearing | computed | myth1 Acc T to F; FC72.new2 (c) goes to counterexample |
| r12 | V2.4 changes with D16.XV, (Suff)/(Nec) | mixed | computed: Expl shrinks (952 worlds; 10 worked cases). Not settled by computation: the defeat sets and the (Nec) attack list (need Out and the attack list programmed) |
| r13 | V2.5 constrains L195.s1 | computed as an effect | H empty is admitted; scenario (ii) |
| r14 | V2.5 blocks L211.s3 in effect | computed as an effect | the student's declared copy is Acc and not Dec in scenario (ii); 23 of 23 Acc worked cases |
| r15 | V2.5 moves Dec, Expl, (Suff) | mixed | computed: Dec 17280 to 408, Expl 0 to 1022 (scenario ii). Not settled by computation: (Suff) (needs (Suff)'s defeat set programmed) |
| r16 | V2.6 blocks L315.s1, L317.s6 | computed | kind ii 142 to 0 (worlds); 47 to 0 (pairs) |
| r17 | V2.6 moves nothing in (E) | mixed | computed: Acc moves 0, source check. Not settled by computation: the ETV and (Nec) attack route through easy-to-vary (needs ETV programmed) |
| r18 | V2.7 blocks L315.s12 in effect | computed | case E; FC52 goes to counterexample; 393 of 4318 pairs |
| r19 | V2.7 constrains D8.4 | computed | first disjunct 1480 off and on; second disjunct 1803 to 0 |
| r20 | V2.7 changes with D8.6 | mixed | computed: ConfG unchanged (FC54 holds; `conf_given` does not call `conf_claim`). Not settled by computation: "feeds no ruling out of a single candidate" (needs Out programmed) |
| r21, r22 | V2.8 constrains D16.XV; moves (Suff)'s defeat set | out of scope | V2.8 is flagged out of scope and not implemented |

Tally of the 20 in-scope rows: computed 11, contradicted 1, not settled by computation 2, mixed 6. Counting the parts of the mixed rows (each part one status): computed 17, contradicted 1, not settled by computation 8.

The reply's one unsettled edge (V2.1 and frozen L309.s1): settled by computation, case D (S unchanged, the interference shape persists).

### Edges the computation shows and the reply did not name

V2.1
- the candidate with no commitments meets (E) whenever the answer varies over C (case G; S = {{}}); the reply names the idle commitment only.
- printed NC2 witnesses lose their block in FC21, FC22, FC23.new2, FC26, FC29, FC62, FC63 (text only).
- more problems of kind ii between candidates (47 to 57 at x40, on the proxy).

V2.2
- L307's set system {{a},{b},{a,b}} becomes {{a},{b}}; the interference shape grows from 45 to 61 worlds.

V2.3
- FC23 (b) with satisfiable background and FC25.new2 (a) go to counterexample.
- the reading split: V2.3 leaves L257's witness at the identity, V2.3b does not; 264 against 271 worlds; 6 against 0 worlds on tau[C] in {1} x B.

V2.4
- four more worked candidates stop meeting (E) than the reply lists: E1 reversed with H only, L273, R3-Q1, E8 p_delta.
- L307's S becomes empty.
- 5 claims go to counterexample.
- none of the 17 external and creative named candidates moves (a null result).
- problems 3 to 0 (proxy, x4).

V2.5
- FC77 (H empty part) goes to counterexample.
- every declared candidate with an Acc-holding account becomes Acc and not Dec in scenario (ii), including 8 external and creative candidates.

V2.6
- FC50 (a) hypothesis_met 572 to 0; FC47 and FC49 counts fall; FC72.new2 (b) and (c) go to counterexample.
- every kind-ii problem is lost, and all problems found are kind ii (47 to 0 at x40).

V2.7
- FC52 (the restated area 2 part) goes to counterexample; the loss is 393 of 4318 pairs, the second disjunct alone.

## 9. Things not done, and where everything is

Not done or not settled:
- V2.8: out of scope, not implemented.
- The infinitary L311 candidate: cannot be built (Candidates are finite).
- Prob_j, ETV_j, Out_j and (Suff)'s defeat set are not program functions, so the parts of rows r6 (partly), r12, r15, r17 and r20 that concern them are not settled by computation.
- The third reading of V2.3 (pairs other than (1,b0)) and V2.2's "a block critical in some route" were not implemented.
- The pairs runs at scale 40 cover V2.1, V2.2 and V2.6 only; V2.3, V2.3b and V2.4 at scale 4 only. V2.5's pairs were not run (it does not move Acc; a problem is defined by Acc and rivalry).
- Two variants were never on together.

Files, all inside `S108 Part A - Sonnet 5.5 trial/`:
- `section 2 model/`: the copy of the round-4 program with the switches; drivers `s108_section2_cases.py`, `s108_section2_small.py`, `s108_section2_worlds.py`, `s108_section2_pairs.py`, `s108_section2_external.py`.
- `printouts/cases/` (worked, small, external named), `printouts/each variant, the round-4 scripts/`, `printouts/generated worlds, scale 4/`, `printouts/pairs of candidates/`, `printouts/whole suite, off and each variant/`.
- To rerun from `section 2 model/`: `S108_S2=V2.1 PYTHONHASHSEED=0 python3 -B -m model.run --claim FC29 --scale 4 --time-cap 45 --no-write` (any variant name from section 1; with the variable unset the program is the round-4 program), or a driver, for example `PYTHONHASHSEED=0 python3 -B s108_section2_worlds.py V2.3 4 out.json`.
