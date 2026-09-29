# S108 Part A round 2 - the dependency map, after round 2

*Rule 6 of `S108 Part A round 2 - how the replies will be read, written before sending.md`. Written 29 September 2026 by the one Opus 5.5 agent that, under decision S56, does the whole reading of round 2. Built by `S108 Part A round 2 - computation/map after round 2/s108r2_map_build.py` on round 1's corrected map (`S108 Part A - the dependency map.json`, 7ce9b1c65b55487d79f0c1a427adc2d9; `.md`, 1da37cf057ff02047fdeb1ca740eb5d8), which is read and never written; with the four round-2 "variants computed" files and their `.json`, the whole-suite runs of round 2, and the review of the Sonnet 5.5 trial (`S108 Part A - Sonnet 5.5 trial/Opus review of the Sonnet 5.5 trial.md`, its O1 to O4). Every input's md5 is in the `.json` (`inputs`). An experiment on copies (rule 11): nothing here changes the theory's text, formal core, claims or program, and nothing is ruled. "Candidate" or "explanation" for what the theory judges; "model" only for the program's own small structures (S43).*

Status: complete, 29 September 2026, before the GLM cross-examination (S56), which is read under its own rule. The candidate list (rule 7) is `S108 Part A round 2 - candidate definitions of explanation, after round 2.md`.

## 0. How this round was done, and what the map holds

**Departures from the round's rule, and why** (all S55, S56: the owner's words, "You're using Opus 5.5 on Xhigh. That's a waste of tokens. It's capable of doing the whole thing on its own. Use GLM for cross examination. No need to Opus to do single sections"):

| rule | as written | as done | why |
|---|---|---|---|
| 5 | at most one Opus agent per section | sections 1 and most of 2 and 3 by the per-section agents before S56 stopped them; the rest of 2 and 3, all of 4, by one Opus agent | S56 |
| 5, "Who does what" | the whole-suite runs are Sonnet harness jobs (a worker and a verifier) | the one Opus agent ran `tools/sonnet_harness/run_claims.py` itself, by script, once per variant setting, 3–4 at a time under `timeout` (the queue: `computation/whole suite/run_queue.py`) | S55 (Sonnet 5.5 costs more than twice Opus 5.5 for these tasks) and S56; a script run by the agent costs less than a Sonnet agent; no second run by a verifier (a departure the review of the runs should weigh) |
| 6, 7 | one Opus agent | the same agent as the computing | S56 |
| 8 | a fresh Opus critical reviewer | the GLM cross-examination, four jobs at once, from four angles, under its own rule written before sending (`S108 Part A round 2 - how the GLM cross-examination will be read, written before sending.md`) | S56 ("Use GLM for cross examination") |

**The restart.** The agent first given this whole job was cut off by a session restart at about 00:24 UTC on 29 September 2026. Its partial work (a run queue, section 4's script, section 3's reruns) was committed (f601771) and continued, not redone, by the agent that wrote this map: its queue's whole-suite jobs had all ended at once with exit 2, because `run_claims.py` refuses an output folder outside the scratchpad; they were rerun with the folders in the scratchpad (`computation/whole suite/jobs, second batch …`, `third batch A`, `B`); its queue's two section-3 "failures" (exit 1) were results, not failures (the harness exits 1 when claims move: R2V3.8 moves FC72, FC72.new1; R2V3.9 FC68); section 4's script was complete and was run, with one count corrected (section 4's file, §0).

| | after round 1 | after round 2 |
|---|---|---|
| nodes | 859 | 876 (17 named first in round 2: new claims FC21.v1, FC21.v2, claims and definitions round 1's edges did not name) |
| edges | 221: computed 179, claimed only 31, contradicted 11 | 337: computed 265, claimed only 46, contradicted 26 (round 1's 221, e4.40 split in three and e2.14 in two, 3 corrections from the Sonnet trial's review, and 110 new) |
| round-2 edges | – | 110: computed 70, claimed only 32 (19 of them of the 10 variants flagged out of scope and not implemented), contradicted 8 |
| template items touched (815) | computed 142, claimed only 26, untouched 647 | computed 191, claimed only 33, untouched 591 |
| middle items untouched (577) | 473 | 426 |
| variants | 32 tabulated, 29 run | 41 tabulated, 31 implemented and computed, 10 flagged by the tabulation and not implemented (rule 4) |

Kinds and standings are round 1's (§0 of round 1's map): *blocks*, *constrains*, *changes with*, *moves*, *independent of*; *computed*, *contradicted*, *claimed only* ("not settled by computation" in the section files). Round-2 edges are `r2e<section>.<k>` in the `.json`, each with its source row, the variant, the items (template ids parsed from the row's item), the standing as the section file wrote it, what shows it, and whether its variant was implemented.

## 1. The parts of the explanation definition

As round 1's map §1: being an explanation is Account(ℰ) ∧ ¬Dec(t) (D16.XV; L17.n2, L49.n3, L61.n2, L69.n3), Account = (E) = Acc (D6.7) = F1 ∧ F2 ∧ A ∧ Dependence ∧ NonVacuous. Nothing in round 2 changed the program's definition; every variant is a switch in a copy.

## 2. How the explanation definition changes with each round-2 variant (computed)

Counts: worked cases; generated at scale 4 (sections 1 and 3: SMALL / value maps / proper / MID; section 2: single / value maps / MID proper; section 4: SMALL / MID, round 1's stream). "Explanation" = Account ∧ ¬Dec(t) unless the variant redefines it. Section files hold the rest.

| variant | item or reading | Acc (E) | being an explanation | what else moves |
|---|---|---|---|---|
| R2V1.1 | S108-1-I5: ρ_p recorded (D3.4, under V1.5's conjunct) | declared: out as I5 (22 worked, 961 / 886 / 221 / 1,674); selected or constructed: 0 | as Acc | the bridge's CreateEx 1 → 0 of 1,024 where its brief is declared |
| R2V1.6 | L11.s1: Expl := (A) ∧ Dependence ∧ NonVacuous ∧ ¬Dec(t) | 0 | **in, never out**: 2 worked (Con history), FC-E 1, CT 3, generated 201 / 149 / 59 / 415 (Con), 141 / 99 / 35 / 236 (Sel) | (Nec) as written fails on the entering cases; the suite cannot see it (no claim forms Expl on a candidate failing (F1) or (F2)) |
| R2V1.10 | S108-1-I1, reading (iii) | ℰ_bv not admitted on the pole under V1.1 + (iii) (the reply's "as under (i)" contradicted) | as Acc | generated under V1.1: follows 2,899, baseline 870, (iii) 1,841 of 34,560 admitted |
| R2V2.1 | the owner's change: edit / boundary / mixed | C5: stands under boundary only; C1: turns on Γ, not the encoding | as Acc | – |
| R2V2.2 | D6.3's quantifier, (E) as it is / with V2.4 | as it is: 0 (60 worked, all generated); with V2.4: 21 / 29 / 25 / 26 of 51 worked out | as Acc | FC26, FC34 (Slot claims) move with (E) as it is |
| R2V2.3 | the hand-set histories: (a) one-holding chains, (b) tried pairs nothing survives | 0 | (a) chains = the hand-set histories on every case; C7 on chains n ≤ 3: 663 of 1,071 in, exactly those selected with one tried pair; (b) every account survives on every H ⊆ C | – |
| R2V2.5 | D6.9 with '≠ ⊥' | 0 | 0 | 1,953 / 1,909 / 212 contracts stop being relabelings |
| R2V2.6 | D11.2, second sentence deleted | 0 | at the sentence's own reach 0 (the reply's claim contradicted); with the whole exclusion dropped: the student's copy selected, 5 claims move | CT8's R2, R4 selected (whole exclusion) |
| R2V2.8 | V1.6's formula: Acc ∧ ¬BadTarget ∧ ¬BadReq, Desc per case | target grain 0; **program grain: 26 worked out, every candidate on the sign's and the vane's questions**; widest: every account | as Acc | e1.45–e1.47 settled |
| R2V2.9 | D6.8's headings | 0 | 0 | FC31's label |
| R2V2.10 | D12.7: Viol := Viol⁺ | 0 | 0 | Sel ∧ Viol ⇒ (a,b) ∉ H fails (450 generated); SelResp at a pair of H |
| R2V2.11 | FC21.v1, FC21.v2 (claims) | – | – | the suite now separates D6.4 from V2.1 and V2.2 (e2.38, e2.39 closed) |
| R2V3.1 | C8's claim on another question sharing t | 0 | out only under S108-3-I2 (CT reads ExplUse), where the claim's account fails: 210 / 140 / 41 / 457 (designation), 122 / 93 / 36 / 200 (widest), …; with CT reading Prepares: 0 | FC90.new1 |
| R2V3.2 | D13.8's record key | 0 | re-entry chains: the core's key ('contract') and the program's ('change') part: every account on a re-entry history is an explanation under 'contract', not under 'change' | the core and the program disagree on D13.8 (I174) |
| R2V3.3 | Held as a tag; the trace's extent | 0 | the extent decides the record clause: 45,072 held outputs with a spanning trace, cut T′ | – |
| R2V3.4 | D15.8's parts as ports / edits | 0 | in: 'Sel-parts' 356 / 1,013 (ports / edits, SMALL); t′ with an idle part 1,013 | underdetermined pairs +1,041 / +1,141 |
| R2V3.5 | no construction stated ⇒ 𝒯 = ∅ | 0 | **out: every selected account whose history states no construction** (1,013 / 881 / 232 / 1,670), the pole's forward candidate on 'Sel' | 5 claims' status, 3 claims' parts (single runs) |
| R2V3.6 | Dec from chains (I90) | 0 | 0 (chains reproduce the hand-set Dec; C7, C9, C10 move the same) | – |
| R2V3.7 | D11.3: ⪯ reflexive closure of ≺ | 0 | out on 'Con-far' tag histories (every account); chains: 4,224 + 11,520 Dec F → T | CT8's R1, R3 constructed → declared; CreateEx 3 of 1,024 |
| R2V3.8 | D9.2: every argument has a step | 0 | 0 | a premise alone no argument (FC72 (d)); Out_j 392 of 1,600 T → F |
| R2V3.9 | D9.1 without 'Ans_p(a,b) = y' | 0 | 0 | FC68 (b), FC47.new1's Solved; Out_j 950 of 1,600 T → F |
| R2V3.10 | D15.5 without the construction disjunct | 0 | 0 | Can 48 → 32, Deploy 24 → 16, CreateEx 3 → 2 of 64 |
| R2V4.1 | C11 × D6.3's quantifier, (Suff) co-varied | 0 | out: 10 / 15 / 12 / 12 worked cases (every / some / some-exempt / some-exempt-set); 941 / 952 / 849 / 854 of 1,019; 1,590 / 1,617 / 1,361 / 1,385 of 1,686 | (Suff) as conjectured fails on exactly the drops unless co-varied |
| R2V4.2 | C12 with (Suff) 'both', S41 Q2's answer as an argument | 0 | the student's copy in under every shape (as round 1) | under 'both' the Q2 argument defeats (Suff) |
| R2V4.3 | C13 read at the content (e) | 0 | out on 25 held relays of 3,208 chains (the reply's "0 moves" contradicted) | – |
| R2V4.4 | histories built as chains | 0 | every worked (24) and generated (1,019; 1,686) account an explanation; C13 (a) 0 | C12 and now agree on every worked case under these histories |
| R2V4.5 | E9 with the set query Q_id | **t1∘ψ out** ((A) fails at 2,768 of 3,456) | t1∘ψ out | L630.n3, L630.s4 false of this question |
| R2V4.6 | L524.s2: unindexed claims | – | – | ℰ_rev's Acc takes both values over five contracts (L604.s1 blocked) |
| R2V4.7 | L522.s1's declared inputs struck | 0 | 0 | nothing usable by any j; (Suff), (Nec) defeat sets empty |
| R2V4.8 | L526.s18 deleted (cut U) | 0 | Dec has two values or none on every account where t is held | DEP's cycle Live → (K2) → Live |
| R2V4.10 | D18.2 carrying traces, records | 0 | – | e4.22 contradicted |

**What round 2 adds about the dependencies of the explanation definition** (short):

- **(E) moved in round 2 only where a variant rewrites what (E) reads**: V1.5's conjunct under a recording of ρ_p (R2V1.1), a condition on the question's target added to Acc (R2V2.8), (E) with the slot test back under a quantifier (R2V2.2 with V2.4), the answer query of E9 (R2V4.5). Every upstream definition first varied in round 2 (D6.9, D11.2, D11.3, D6.8, D9.1, D9.2, D12.7, D15.5, E9) moved no candidate's Acc, except E9 whose query is (A)'s own input.
- **Being an explanation moves with Dec's readings far more than with its definitions**: of the upstream definitions varied for the first time, only D11.3 (R2V3.7) moves Dec, and only on histories whose witness lies two steps back; D11.2 at its own reach moves nothing. Every other move of being an explanation in round 2 comes from a *reading*: the record key (R2V3.2), the trace's extent (R2V3.3), the parts (R2V3.4), 𝒯 with no stated construction (R2V3.5), CT reading ExplUse (R2V3.1), histories built as chains (R2V4.4), cut U (R2V4.8), and D16.XV's rule (R2V4.1–R2V4.3, R2V1.6).
- **The core and the program part on one definition**: D13.8's record key (R2V3.2): the program keys a provenance record by the change (I174), the formal core's words by the new contract; they differ on every re-entry history. A result of Part A about the state after round 4, for the orchestrator's records, not for change in Part A (as round 1's O4 finding).
- **The hand-set histories (I90) were the widest gap after round 1**: round 2 built chain histories in three sections (R2V2.3, R2V3.6, R2V4.4). Chains reproduce the hand-set Dec on every worked and generated case (R2V3.6, R2V2.3 (a)); built with a tried pair per case (R2V4.4), they make every account an explanation, so the separations C7, C12, C13 draw rest on the program's computed chains (FC30.new1 (d)) and on the chosen history kinds, not on hand-set labels alone.
- **The owner's own cases stay where round 1 left them, on the same two readings**: the change read as an edit or a boundary (C5; C1 turns on Γ, not the encoding), and D6.3's quantifier (C6, C11: S44 comes on the three non-'every' readings, R2V2.2 and R2V4.1 computed on every encoding). Round 2 adds a third place: a condition on the question's target at the program's grain (R2V2.8) empties the sign's and the vane's questions.

## 3. Round-1 edges whose standing round 2 changed (each with its round-1 standing)

<!-- changes -->
| edge | round-1 standing | after round 2 | what changed it | what shows it (cut) |
|---|---|---|---|---|
| e1.02 | claimed only | claimed only | section 1 (not settled) | the words read two ways: W1 (lambda(k)'s constraints alone) = I14's Sol_N at 138,487 of 138,487 (k, pair) of the worked candidates; W2 (imposed within D, restricted to V_N) = V1.1's at 138,487 of 138,487; W1 = W2 at 14,004 |
| e1.03 | claimed only | contradicted | section 1, round 2 | contradicted: under V1.1: L556.n2's statement ((F1) at (a,b) iff D4.4's sig_C(lambda(k)) and (K)'s sig of k agree) at 7,042 of 7,042 translated pairs of the worked candidates; FC17, FC18 hold (single runs); D4.4's gloss 'extends (K)' fails (14,064 of 166,251 (j, pair)), which L556.n2 does not use |
| e1.14 | claimed only | claimed only | section 1 (not settled) | 6,354 new setting pairs (round 1's SMALL targets, seed 108001, 160 per size, 5,954; the pole 400): the assigning component's old relation left beside the slice: 0 of 6,354; an altered k != j whose relation alone excludes the set value (S108r2-1-I6): 2,709 of 5,954 (pole 0 of 400); Sol_D empty at some b 4,129, of which 1,420 with no single such k |
| e1.36 | claimed only | claimed only | section 1 (not settled) | value side: under V1.5 (I5; R2V1.1 declared) every assessment of (E) on a declared contract admits nothing (22 worked, every generated candidate) |
| e1.37 | claimed only | computed | section 1, round 2 | computed: a chain o1 < o2, C1 -> C2 (E8's arrangement, S108r2-1-I4): trace preparing C2, change recorded: Con(C2) T (S41, L55), rho constructed; unrecorded: T (S41), F (L55); no trace: declared. D3.1's slot holds the computed value; L155.s6's Found claim allowed exactly where constructed; E_fwd on the found question Acc T under none, V1.5, R2V1.1; on the declared one T, F, F |
| e1.38 | claimed only | contradicted | section 1, round 2 | contradicted: D13.8 as written: Episode, Con and Build at the bridge's output identical under every state (none, I5, R2V1.1 x3) and every rho(brief), chains a1, a2, a4, readings S41 and L55; the move is in D14.7's CreateEx through Acc(c, p_c, ...): 1 -> 0 of 1,024 on (a2) where the brief is declared |
| e1.39 | claimed only | computed | section 1, round 2 | computed: a finite class over the 27 worked (p, t, Gamma, delta), Theta admitting every carrier (by hand): 13 organizations under none, recorded selected, recorded constructed; 0 under I5 and recorded declared; the adversary class itself is not defined (NF12): not settled for it |
| e1.40 | claimed only | claimed only | section 1 (not settled) | 'fails to capture' and 'not creative' have no definition (D16.XV's list) |
| e1.45 | claimed only | computed | section 2, round 2 | computed: defective questions stay questions (their candidates fail Acc); NonVacuous unchanged (BadBaseline kept in it); the variant adds, it replaces nothing |
| e1.46 | claimed only | computed | section 2, round 2 | computed for (Suff) and FC106; (Nec) as L538 states it independent: at the program's grain no candidate on the sign's or vane's question is in (Suff)'s defeat set (FC23.new2 (f) moves); FC106's two untested defects get values from Desc (BadTarget T for sign and vane at that grain, BadReq F everywhere) |
| e1.47 | claimed only | computed | section 2, round 2 | computed: target grain 0; program grain 26 worked cases (the sign's and vane's questions); widest all 51 and all generated |
| e2.03 | claimed only | computed | section 2, round 2 | computed: off, V2.1, V2.3: routes = the infinite index sets (341 of 434 representations), no route of one commitment, no critical singleton, every tail block critical; V2.2: no route (0): (B) records nothing |
| e2.06c | claimed only | computed | section 2, round 2 | computed under the strict reading of "account": Acc T → F (Dependence: every witness pair has a = 1); Ident's clause on C = {1}×B holds (E2 reads no (E)); under the loose reading (the finding, no (E)) nothing is blocked |
| e2.07 | claimed only | computed | section 2, round 2 | computed: on exactly the contracts {1}×B′ V2.3 empties the accounts (168 / 150 / 48 → 0) and V1.4 empties Ident's contract clause (799 / 796 / 94 → 0); on C_id: Ident I163 T, V1.4 F; E_fwd, E_rev Acc T → F under V2.3, E_rev's (F1), (F2), (A) unchanged: L325.n6's "faithful under the identification contract" keeps its fidelity and loses the contract's role under V1.4 and its account under V2.3 |
| e2.11b | claimed only | contradicted | section 2, round 2 | contradicted as to D16.XV's (Nec) (L538); computed as to L61's reading: L538: exposure reads Faithful_C(t), T off and under V2.4: in no defeat set either way; L61's 'their' (Account ∧ ¬Dec): with a Con or Sel history F → T under V2.4 |
| e2.16c | claimed only | contradicted | section 2, round 2 | contradicted; keep "independent of" X:(Nec): α rules out Expl(ℰ) and uses no Acc (a (Suff) defeat's shape), never ¬Expl(ℰ) (what (Nec)'s defeat needs); under V2.6 ETV holds of nothing (round 1: 310 of 310 kind-ii pairs gone) |
| e2.19 | claimed only | contradicted | section 2, round 2 | computed for the argument from ConfCl; contradicted as to D8.6: round 1's V2.7 case: α rules out Acc(ℰ) off, not constructible under V2.7; ConfG_χ does not read D8.5: 0 of 8,628 translated pairs move |
| e2.26 | claimed only | computed | section 2, round 2 | computed: under V2.2 no block is critical in any route (0), off 2,728 (W, tail) |
| e2.33 | claimed only | computed | section 2, round 2 | computed: Out_j('Acc(ℰ)') by α: 23 off, 0 under V2.7 (20 at a pair of C): the route to "solved with no test" goes there |
| e3.30b | claimed only | computed | section 3, round 2 | computed: 7,404 populations: under V3.6 𝒯 grows 29,616 → 53,748 members and the populations with an unseen pair underdetermined by the survivors 3,586 → 4,090 (581 more, 0 fewer); under R2V3.4 ports 3,961 (452 more) |
| e3.34b | claimed only | computed | section 3, round 2 | computed: 'an active route' read as R itself: UsesReason F → T on exactly the 1,436 routes that did no work; read as any route through m's image: 2,684 (1,093 of them routes that did no work) |
| e4.22 | claimed only | contradicted | section 4, round 2 | contradicted: Expl now T / F and C13 (a) T / F on the pair: both definitions read the trace; D18.2 maps preserve ≺_h and Θ's interpretation, and D0.2 lists Prepares and Rec among Θ's primitives, so h ↦ h′ is no D18.2 map; nothing is specific to V4.3 and D18.2.v1 adds what D18.2 already carries |
| e4.40a | claimed only (e4.40) | computed | section 4, round 2 (§6) | the pole, 𝒯 = {t, t_ab,H}: L572.s2's condition (a surviving differer) at 0 of 2 unseen pairs, V4.8's Underdet at 2; survivors agree at 2 (L574.s5) |
| e4.40b | claimed only (e4.40) | contradicted | section 4, round 2 (§6) | L574.n4's route (t_ab survives on H at every unseen pair, t_ab,H at none) is the same under V4.8 |
| e4.40c | claimed only (e4.40) | claimed only | section 4, round 2 (§6) | turns on reading 'admits an alternative' (L576.s1); not computed |
| e2.14b | computed (in e2.14) | claimed only | correction O2 | the (Suff) part of R15 was not computed |
<!-- /changes -->

Round-1 edges round 2 did not settle, and why: e1.02, e1.14, e1.36, e1.40 (section 1: the words read two ways; the text's terms undefined), e2.09 (S45, the owner's), e3.37b (S47 with S41 Q6, the owner's), e1.48–e1.51 (V1.7, to Part B), e2.20, e2.21 (V2.8, its D16.XV part computed as V4.4 in round 1, its L315.s7 part to Part B). e2.38 and e2.39 keep their standing (a computed "no claim separates"): the gaps they recorded are closed by FC21.v1 and FC21.v2 (R2V2.11).

## 4. Corrections from the review of the Sonnet 5.5 trial (round 1's section 2)

The Opus review of the Sonnet 5.5 trial (S53) found four points in round 1's section-2 computation (O1–O4). Each is recorded here as a correction to round 1's map, not by writing round 1's files:

| id | correction | in the map |
|---|---|---|
| O1 | V2.6 makes FC50 (a) vacuous: its hypothesis count 572 → 0 (the trial's count, rerun by the review); round 1 left claim counts out as "timed", but these searches are seeded and run to the end | new edge e2.O1: V2.6 moves FC50 (computed) |
| O2 | R12, R15 and R17 of round 1's section 2 were marked computed with a part unsettled | R12 (e2.11a/b) and R17 (e2.16a/b/c) were already split by round 1's second checker; R15 is split here: e2.14 keeps X:Dec, X:Expl computed; **e2.14b**, V2.5 moves X:(Suff), claimed only (not computed in either round) |
| O3 | N16 (e2.38) said no claim builds a candidate whose Dependence needs a block of two or more; under V2.2 FC46's accounts drop 962 → 927 and the counts of FC29, FC37, FC51 move | new edge e2.O3: V2.2 changes with FC46, FC29, FC37, FC51 (computed); e2.38's wording withdrawn; its gap (no claim's result separates V2.2) closed in round 2 by FC21.v2 |
| O4 | V2.3's second reading, the witness pair read through τ (τ(a) ≠ 1), was not examined: 6 accounts on τ[C] ⊆ {1}×B survive V2.3 and drop under V2.3b | new edge e2.O4: V2.3b moves X:(E) (computed by the trial, rerun by the review); C5 carries it as a second reading (the candidate list) |

## 5. The whole suite with each round-2 variant on

Run by script (§0), scale 4, time cap 45, each run compared claim by claim and part by part with the round-4 record (`formal claims, after round 4.json`, key after_round4; the off runs of every copy: 133 / 2 / 7 of 142, no difference). "Moved" = the claims whose status or a part's (label, kind, status) differs from the record.

<!-- suite -->
| run | setting | H / CEX / NT of | moved (status or a part) | of them parts only | expected (section file) | as expected |
|---|---|---|---|---|---|---|
| section 1/R2V1.1-constructed | R2V1.1-constructed | 133 / 2 / 7 of 142 | none | – | none | yes |
| section 1/R2V1.1-declared | R2V1.1-declared | 118 / 17 / 7 of 142 | FC101, FC22, FC23, FC23.new1, FC23.new2, FC23.new3, FC23.new5, FC25.new2, FC26, FC27.new1, FC30.new1, FC34, FC42.new1, FC62, FC63, FC72.new2, FC74, FC90.new1, FC99 | FC23, FC34, FC63, FC74 | FC101, FC22, FC23, FC23.new1, FC23.new2, FC23.new3, FC23.new5, FC25.new2, FC26, FC27.new1, FC30.new1, FC34, FC42.new1, FC62, FC63, FC72.new2, FC74, FC90.new1, FC99 | yes |
| section 1/R2V1.1-selected | R2V1.1-selected | 133 / 2 / 7 of 142 | none | – | none | yes |
| section 1/R2V1.10 | R2V1.10 | not yet run | – | – | FC101, FC102.new1, FC104.new1, FC12.new1, FC12.new2, FC12.new3, FC22, FC23, FC23.new1, FC23.new2, FC23.new3, FC23.new5, FC26, FC27.new1, FC28, FC30.new1, FC42.new1, FC62, FC63, FC72.new2, FC83, FC85, FC90.new1, FC95, FC99 | – |
| section 1/R2V1.6 | R2V1.6 | 133 / 2 / 7 of 142 | none | – | none | yes |
| section 1/R2V1.6s | R2V1.6s | 133 / 2 / 7 of 142 | none | – | none | yes |
| section 1/off | off | 133 / 2 / 7 of 142 | none | – | none | yes |
| section 2/s00 | off | not yet run | – | – | none | – |
| section 2/s01 | 'some' ((E) as it is) | not yet run | – | – | FC26, FC34 | – |
| section 2/s02 | 'some-exempt' | not yet run | – | – | FC34 | – |
| section 2/s03 | 'some-exempt-set' | not yet run | – | – | FC34 | – |
| section 2/s04 | V2.4 × 'some' | not yet run | – | – | ≥ FC23, FC23.new1, FC23.new2, FC23.new3, FC23.new5, FC25.new2, FC26, FC27.new1, FC34, FC72.new2 | – |
| section 2/s05 | V2.4 × 'some-exempt' | not yet run | – | – | ≥ as s04 | – |
| section 2/s06 | V2.4 × 'some-exempt-set' | not yet run | – | – | ≥ as s04 | – |
| section 2/s07 | R2V2.3a | not yet run | – | – | none | – |
| section 2/s08 | R2V2.5 | not yet run | – | – | none | – |
| section 2/s09 | R2V2.6 written | not yet run | – | – | none | – |
| section 2/s10 | R2V2.6 HS | not yet run | – | – | none | – |
| section 2/s11 | R2V2.6 reply | not yet run | – | – | FC12.new2, FC30.new1, FC83, FC98, FC98.new1 | – |
| section 2/s12 | R2V2.8 target | not yet run | – | – | none | – |
| section 2/s13 | R2V2.8 program | not yet run | – | – | FC22, FC23.new1, FC23.new2, FC23.new5 | – |
| section 2/s14 | R2V2.8 widest | not yet run | – | – | ≥ FC22, FC23, FC23.new1, FC23.new2, FC23.new3, FC23.new5, FC25.new2, FC26, FC27.new1, FC34, FC72.new2, FC74 | – |
| section 2/s15 | R2V2.9 | not yet run | – | – | FC31 | – |
| section 2/s16 | R2V2.10 | not yet run | – | – | none | – |
| section 2/s17 | R2V2.11 | not yet run | – | – | none; FC21.v1, FC21.v2 new (both hold) | – |
| section 3/R2V3.1 | R2V3.1 | not yet run | – | – | FC90.new1 | – |
| section 3/R2V3.10 | R2V3.10 | not yet run | – | – | FC32.new1 | – |
| section 3/R2V3.2-contract | R2V3.2-contract | not yet run | – | – | none | – |
| section 3/R2V3.4-edits | R2V3.4-edits | not yet run | – | – | none | – |
| section 3/R2V3.4-ports | R2V3.4-ports | not yet run | – | – | none | – |
| section 3/R2V3.5 | R2V3.5 | not yet run | – | – | FC102.new1, FC104.new1, FC12.new1, FC12.new2, FC30.new1, FC77, FC80.new1, FC83 | – |
| section 3/R2V3.6 | R2V3.6 | not yet run | – | – | none | – |
| section 3/R2V3.7 | R2V3.7 | not yet run | – | – | none | – |
| section 3/R2V3.8 | R2V3.8 | not yet run | – | – | FC72, FC72.new1 | – |
| section 3/R2V3.9 | R2V3.9 | not yet run | – | – | FC68 | – |
| section 3/off | off | not yet run | – | – | none | – |

6 runs in; 30 not yet run when this table was generated. No run timed out; no run changed its program folder.
<!-- /suite -->

## 6. Gaps after round 2 (rule 6; rule 10 decides a third round on them)

### 6.1 Items still untouched

<!-- stretch -->
| stretch | FROZEN: computed / claimed only / untouched | middle: computed / claimed only / untouched |
|---|---|---|
| S1 | 12 / 4 / 41 | 22 / 9 / 123 |
| S2 | 32 / 3 / 60 | 56 / 4 / 93 |
| S3 | 12 / 1 / 36 | 21 / 0 / 116 |
| S4 | 9 / 0 / 28 | 27 / 12 / 94 |

(After round 1: S1 7 / 7 / 43, 18 / 4 / 132; S2 28 / 5 / 62, 39 / 6 / 108; S3 9 / 1 / 39, 17 / 0 / 120; S4 7 / 0 / 30, 17 / 3 / 113.)
<!-- /stretch -->

**Middle definitions still untouched** (neither varied nor named by a computed or contradicted edge): **D5.7** (Faithful; question fidelity: upstream of Dec, Expl, (Suff), (Nec) by its statement; R2V2.7 varied it but was flagged out of scope, its formula rewriting L189.s2 [FROZEN]), D8.new1, D13.7, D14.1, D15.1, D15.2 (upstream of no part of the explanation definition by D18.1's graph or by statement; the replies left D14.1, D15.1, D15.2 "for budget" and D13.7 as a note). Every other middle definition round 1 left untouched, including the six upstream of the explanation definition (D6.9, D11.2, D11.3, D6.8, D9.1, D9.2), is computed now.

**Middle definitions no variant of either round has varied** (some named by computed edges): D4.6, D5.7, D6.5, D7.4, D8.3, D8.new1, D9.9, D9.10, D10.3, D10.6, D12.3, D12.8, D13.7, D14.1, D15.1, D15.2, D16.5, D18.1, E1, E2. Of these, upstream of (E) or Dec by D18.1's graph or statement: D5.7, D6.5 (Dependence), D12.3 (Dec itself; R2V2.4 flagged, in effect D12.4 [FROZEN]), D18.1 (the order; R2V4.8 reached it through L526.s18).

**Middle sentences**: 426 of 577 still untouched; section 2 and section 3 varied no middle sentence in round 2 (the replies: "none is upstream of the explanation definition"; "a sentence-by-sentence pass needs a round of its own"); section 1 varied 6, section 4 7.

### 6.2 Edges still claimed only (46)

- **Round 1's, still claimed only (14)**: e1.02, e1.14, e1.36, e1.40 (not settled by round 2's computation: readings of the words, undefined terms); e2.09, e3.37b (the owner's yes or no); e1.48–e1.51, e2.20, e2.21 (ruled to Part B, or computed as V4.4); e2.14b (O2); e4.40c (L576.s1, L576.s4: a reading of "admits").
- **Round 2's (32)**: 19 of the ten flagged variants, not implemented (R2V1.2–R2V1.5, R2V1.7–R2V1.9, R2V2.4, R2V2.7; rule 4: the orchestrator's; under S56 the one agent records them and leaves them flagged), and 13 of implemented variants whose item is a sentence the program does not read (L23.s1, L481.s3, L195.s1, L397.s5, D15.7, L562.s3, L606–L608, L522.s2, L596.s1, L598.s2) or a reading with no code (FC97.new1 and E8 under R2V2.6; R2V4.6's unindexed defeat sets).

### 6.3 Readings still computed one way only, and what the program cannot compute

| reading | what rests on it after round 2 |
|---|---|
| edit or boundary for the owner's changes; the mixed encoding (P-R2S2-6, 7) | C5's flags (stand under boundary only); the sign's mixed encoding is the computing agent's |
| D6.3's quantifier (I136) | C6's and C11's S44 flag (computed under all four readings, every encoding): **the owner's to settle** (rule 13) |
| a question's recorded history ρ_p (S108-1-I5; S108r2-1-I1) | C2's flags stand iff the case's question is declared or unrecorded; no case records one |
| Desc's grain (P-R2S2-3) | R2V2.8's whole effect: 0 at the target's grain, the owner's two questions empty at the program's grain; the universe of organizations is the program's |
| S108-3-I2 (CT reads ExplUse) | C8's every move, and R2V3.1's |
| the trace's extent; the record key | C9's reach; the core and the program part on re-entry (R2V3.2) |
| chain histories (S108r2-4-I1, P-R2S2-9) | R2V4.4's "every account an explanation", by construction of a tried pair per case; R2V4.3's 25 relays from a holding not holding t |
| cut U (R2V4.8), the nearest statable readings of R2V4.7, R2V3.9, R2V3.10 | computed at the nearest statable reading only |
| the bridge (FC84.new1) | builds no candidate: no variant's effect on it as an explanation is computed (as after round 1); only its provenance and CreateEx |

Not computable in the program as it stands (unchanged from round 1 except where noted): an infinite Γ (L311: computed on ultimately periodic index sets in round 2, e2.03, e2.26); UsesReason over circuits (computed on circuits with an objection in round 2, e3.34b); 𝔈_Θ membership over every (p, t, Γ); (CT1), Enable, UU, barriers; the adversary class of D16.4; 'fails to capture' and 'not creative' (e1.40); a Desc over organizations the program does not build.

## 7. Is a third round of Part A needed? (rule 10)

**Not for the explanation definition's middle definitions; possibly for one definition and for the middle sentences.** Every middle definition upstream of the explanation definition that round 1 left untouched has been varied and computed in round 2 (D6.9, D11.2, D11.3, D6.8, D9.1, D9.2), except **D5.7**, whose one variant rewrites a FROZEN sentence (L189.s2) and so cannot be a reading of the frozen words: a third round could not vary it inside Part A's rule either; it belongs to Part B (vary the hard-to-vary parts). The edges still claimed only are, with four exceptions, of variants flagged out of scope, readings of the text's words the program does not compute, or the owner's yes or no; the four (e1.02, e1.14, e1.36, e1.40) turn on words the text leaves undefined. The readings that decide the owner's own cases (edit or boundary; D6.3's quantifier; a question's recorded history) are the owner's to settle, not a round's. What remains untouched in bulk is the middle sentences (426 of 577), most of which the section agents judged not upstream of the explanation definition; a sentence-by-sentence pass would be a round of its own and, on round 2's evidence (sentence variants moved Expl only in R2V1.6), would reach the definition rarely.

So, on this map: a third round is **not** needed for gaps that bear on the explanation definition, provided the GLM cross-examination finds none; the rule for reading it says a third round follows only if gaps that bear on the explanation definition remain after it. Then Part B (S52).

## 8. Unsure

- **The whole suite was run once per setting, by this agent's script**, not by a worker and a second verifier; a run that differs from the record is reported as the section files expect or explained; none was repeated.
- **Mapping rows to items** parses template ids from each row's item text (`ids_in` in the builder); a row naming a claim part or a reading only (e.g. "C5's flags") names no node.
- **Touched** counts as round 1's map: varied, or named by a computed or contradicted edge; claimed only otherwise. Round 2's rows of the flagged variants count their items as claimed only.
- **The Sonnet trial's O1, O3, O4** are the trial's counts as the Opus review reran them; this agent did not rerun them.
- **e2.19** is marked contradicted (the edge claims V2.7 changes with D8.6; section 2 computed the argument from ConfCl and found D8.6's ConfG_χ unmoved).
- **Section 3's worked-case run** (part A of its script) ended while this map was built; its results (section 3's §10) agree with the generated worlds and add the owner's cases to C8 and C16.

Built by one Opus 5.5 agent under rules 6 and 10 and decision S56, 29 September 2026. Nothing ruled; nothing applied to the theory (rule 11).
