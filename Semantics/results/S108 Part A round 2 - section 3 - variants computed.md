# S108 Part A round 2 - section 3 - variants computed

*Computing agent for section 3 (rule 5 of `S108 Part A round 2 - how the replies will be read, written before sending.md`; Opus 5.5 per `S108 Part A round 2 - who computes, recorded before any reply is opened.md`), 28–29 September 2026. Fresh. Works only in `S108 Part A round 2 - computation/section 3 model/` (a copy of round 1's `S108 Part A - computation/section 3 model/`, 36 files md5-identical at the copy; round 1's copy never written). Runs in `S108 Part A round 2 - computation/section 3 runs/`. Nothing here changes the theory (rule 11). "Candidate" or "explanation" for what the theory judges; "model" only for the program or a small structure it builds (S43). Read with the reply (`s108r2_glm_section3.response.txt`, 34a8e69f…) and the tabulation (§2–§8).*

Status: complete, 29 September 2026. **Continued after two stops**: the section agent that set this copy up and wrote §0–§2 was stopped under decision S56 (its runs of the scripts, the chains, the record keys, the arguments and the generated worlds had finished and are used here as they stand); the one Opus 5.5 agent that took over the whole reading under S56 was itself cut off by a session restart at about 00:24 UTC on 29 September, while the worked-case script and three single-claim runs were going. This file is finished by the agent that continued after the restart (S56: one Opus agent for the whole job, a departure from rule 5's "at most one per section"), from those runs and from the reruns named below. Nothing ruled.

## 0. Setup

| item | state |
|---|---|
| copy | round 1's section 3 copy, 36 files identical (md5 list compared) |
| round 1's switches kept | `S108_S3_VARIANT` (V3.1–V3.8), `S108_S3_CT` |
| round 2's switches (`model/s108r2s3.py`) | `S108R2_S3_VARIANT` ∈ {none, R2V3.1, R2V3.2, R2V3.4, R2V3.5, R2V3.6, R2V3.7, R2V3.8, R2V3.9, R2V3.10}; `S108R2_S3_RECKEY` ∈ {change (default), contract}; `S108R2_S3_PARTS` ∈ {components (default), ports, edits}; `S108R2_S3_I8` ∈ {kept, dropped}. Hooks: `claims_b.episode` (key), `claims_b.sel` (parts reading; 𝒯 = ∅), `claims_b.con` and `_con_at` (⪯), `claims_b.DEP` (Can), `claims_r3a1._dag_fixed_points` (⪯), `claims_s41.provenance_of` (chains), `args.usable`, `usable_step`, `rules_out`, `enumerate_args` (D9.2, D9.1) |
| default unchanged | every switch off: `s104_external.py`, `s104_creative_transport.py`, `s106_cases.py` print the committed md5s (86a67664…, d473944e…, 043aeb36…); round 1's `s108_s3_cases.py` prints round 1's `cases.txt` byte for byte (adfcf39c…) |
| scripts (in the copy) | `s108r2_s3_common.py` (histories, claim choices, the chain evaluator), `s108r2_s3_cases.py` (§3–§5), `s108r2_s3_worlds.py` (§6), `s108r2_s3_run_scripts.sh` (§5), `s108r2_s3_run_worlds.sh`, `s108r2_s3_suite_check.py` (the harness's check step), `s108r2_owner_cases.py` (the second checker's owner cases, copied unchanged); in `section 3 runs/`: `s108r2_s3_single.sh` (single claims, §7), `s108r2_s3_specs.py` (writes the specs), `suite - expected moves.json` |
| the chain evaluator | `s108r2_s3_common.chain_out` stages T′, T, K along the chain with the program's own `episode` and ⪯; checked equal to `claims_b.prov_fixed_points` on every chain n ≤ 3 (records anywhere) × 3 cuts × 6 switch states: 50,736 pairs each, 0 mismatches (`worlds/crosscheck.txt`); U uses the fixed points |
| runs | PYTHONHASHSEED=0, `timeout` on every run; the whole suite is the harness's (§7), not run here |

## 1. Which variants are implemented (tabulation §2, §7: no section-3 variant flagged)

| id | item or reading | implemented | how |
|---|---|---|---|
| R2V3.1 | S108-3-I2 and I5's other choices (C8) | yes | round 1's V3.4 with CT reading ExplUse; the claim's ℰ′ per case: own, widest (round 1's), designation (R2-3-I1), gamma, port |
| R2V3.2 | D13.8's record key | yes | the program already keys by the change (a flag per change; I174, "recorded, not chosen"), the variant's new form; `S108R2_S3_RECKEY=contract` gives the formal core's words (any record of the new contract in h′), the variant's old form |
| R2V3.3 | (a) Held as a tag, (b) the trace's extent | yes, in the scripts | no program function reads either (Prepares a one-occurrence label, I56; Held at an output set by each claim, I90): (a) the chain with Held at the output read from the tag; (b) the output's trace from o_s (the second checker's model) |
| R2V3.4 | D15.8's parts | yes | `parts_read`: ports of E in footprints with π(v) (R2-3-I4); edits (the reply's other choice) |
| R2V3.5 | S108-3-I3's other choice | yes | no construction stated ⇒ 𝒯 = ∅ in `sel` (not under round 1's V3.6, which deletes the clause) |
| R2V3.6 | I90's other choice | yes | `provenance_of` builds chains, Rep computed (T′, least fixed point) |
| R2V3.7 | D11.3's ⪯ | yes | Con's witness at o_t or an immediate predecessor (chain, tag model, partial orders) |
| R2V3.8 | D9.2 | yes | `args.ARG_READING` "I88" through `_arg_reading` |
| R2V3.9 | D9.1 | yes, nearest statable | answer atoms (ans…, Ans…, E_ans…) no claims; see §2 |
| R2V3.10 | D15.5 | yes, nearest statable | the program computes no Can: D18.1's Can loses Ω; Deploy and CreateEx over Θ's values (§4) |

## 2. The inventions this computation forced (S36); the reply's R2-3-I1–I8 used as it states them

| id | where | choice | other choices |
|---|---|---|---|
| S108r2-3-I1 | R2V3.1 | claims beyond the reply's: designation δ′ := the first port of E other than δ_E (R2-3-I1's δ′ = H for the pole); gamma Γ′ := all of E's components where Γ is not all, else Γ without its last; port: the question on the first other port of D, E designating that port | every δ′, Γ′, port |
| S108r2-3-I2 | R2V3.2 | a record flag per occurrence: a record made there of the contract operative there. 'change' reads the flag at the change's own occurrence (the program); 'contract' reads any such record of the new contract in h′ | records carrying their change; records made outside h′ |
| S108r2-3-I3 | R2V3.3 | (a) = the chain with Held at the output set by the tag (0) for a candidate meeting (E); (b) h′ ⊇ the trace o_s … o_t (the second checker's) | h′ = the trace exactly (the same Dec wherever the output is held) |
| S108r2-3-I4 | R2V3.4 | ports: {(v, π(v)) : v a port of E in some component's footprint}; edits: {(τ(a), a)} | bindings as λ's |
| S108r2-3-I5 | R2V3.5 | read on the histories that carry a stated construction or none (`Hist`); the chain model's Sel's conditions stay Θ's bit, read as including t ∈ 𝒯 | Sel's conditions 0 on every chain (no chain states a construction) |
| S108r2-3-I6 | R2V3.6 | 'Dec' one occurrence, nothing admitted; 'Con' o1 ≺ o2, a trace at o2; 'Sel' one occurrence; Held at the output from Faithful; T′ (unique fixed point) | R2-3-I6's others (H = ∅; all pairs) |
| S108r2-3-I7 | e3.34b | ob with one role bound to i, Rec = {id}, Chg = ∅; "an active route" read as any route through m's image (the words) and as R itself | other role maps |
| S108r2-3-I8 | e3.30b | FC80's populations with the stated construction := the base member's parts, each member with a twin carrying one more part deviating at one pair of C∖H | other twins |
| S108r2-3-I9 | R2V3.7 | ≺_h of a chain := its covering steps; D12.1's exclusion (≺) kept as the program reads it (every earlier occurrence); under K (Con's witness strictly before) the immediate predecessor; in the tag model a tag counts at the last occurrence or its predecessor | ≺_h read as the order (then ⪯ = ≺* and nothing moves) |
| S108r2-3-I10 | R2V3.9 | an answer atom is one named ans…, Ans…, E_ans… (FC68's; FC47.new1's record 'rec' is not so named, so the suite's R2V3.9 run does not type it); a formula with one is no claim; a tree with such a node is no argument; RO of a non-claim false | D9.1's "include" read as an open list: deleting an item then changes nothing |
| S108r2-3-I11 | R2V3.10 | D18.1's Can loses Ω; Deploy := Rep ∧ Integrated ∧ Can over Θ's values | – |
| S108r2-3-I12 | the suite | R2V3.2's run uses the formal core's key (the variant's old form), since its new form is the program's ('off') | – |

## 3. Findings in brief

| variant (reply) | (E) (Acc) | being an explanation (Account ∧ ¬Dec(t)) | what the computation adds or corrects |
|---|---|---|---|
| R2V3.1 C8 under the other choices: the claim on another question sharing t (R2-3-I1) | 0 | the pole's forward candidate: out only where the claim's δ′ = H (Acc(ℰ′) F: ExplUse F, Build F, Con F, Dec T); own, widest, Γ′ and port claims keep it; generated (claim designation / Γ′ / port / widest) out 210 / 73 / 146 / 122 (SMALL), 140 / 76 / 118 / 93 (value maps), 41 / 10 / 14 / 36 (proper), 457 / 112 / 288 / 200 (MID); with CT reading Prepares (D12.2 as written): 0 | **C8's flag S41 Q2 rests wholly on S108-3-I2** (CT reads ExplUse): on the candidate's own question and on the widest contract nothing moves on the worked case; with the claim on another question sharing t it moves (the reply's claim, computed). FC90.new1 moves in the suite (its (a) case) |
| R2V3.2 D13.8's record key (contract → change) | 0 | on the reply's re-entry chain q = [C′, C, C] (one record, of ρ_C): key 'change' (the program): Episode F, tag Con F, Dec T; key 'contract' (the core's words): Episode T, Dec F; generated: every account on a re-entry history (tags, and chain T′ with the trace spanning) 1,013 / 881 / 232 / 1,670 in under 'contract' against 'change' | **the program already keys by the change** (I174), so the variant's new form is the program's and its old form the core's words: the core and the program part on re-entry chains (2,147,344 chains n ≤ 4, cut T′: Dec F → T on 14,592 + 44,288 held outputs, 'contract' → 'change'). C9 gains re-entry chains under 'change' (the reply's claim computed); no flag |
| R2V3.3 (a) Held read as a tag before an unrecorded change, (b) the trace's extent = the whole subhistory | 0 | (a): the tag at o1, trace at o2: Dec T (off), Dec F under V3.5; as a chain not held at o2: Dec T under T′ and T; (b) the trace spanning o1…o_t across an unrecorded change: Dec F → T on 45,072 held outputs (341,184 chains n ≤ 4, cut T′) | round 1's tag rows were an artefact of the deletion, as the reply says (tag at o1, clause kept: every Acc-T candidate declared, T′ and T); (b) reproduces the second checker's e3.25c (45,072) with the clause kept: the extent decides whether the record clause bites. "C9′" (C9 read with the whole-subhistory extent) = C9 on spanning traces |
| R2V3.4 D15.8's parts as ports (and edits) | 0 | the pole, t′ = t + an idle part, stated construction t's own: components (off) t′ Dec T; ports and edits: t′ in 𝒯, Dec F, an explanation; t on 'Sel-parts' (stated lacks c_L): Dec T under ports, F under edits. Generated (ports / edits): 'Sel-parts' in 356 / 1,013 (SMALL), t′ idle in 1,013 / 1,013, t′ deviating in 576 / 638, newly underdetermined pairs 1,041 / 1,141 | C10's reach **does not need the deletion** (the reply's claim computed): parts as ports or edits admit a t′ with an extra component; ports equals round 1's V3.6 (the clause deleted) on 'Sel-parts' only in part (356 of 1,013), edits equals it everywhere |
| R2V3.5 no construction stated ⇒ 𝒯 = ∅ | 0 | the pole's forward candidate on the 'Sel' history: Sel T → F, Dec F → T, Account ∧ ¬Dec(t) T → F; generated: every account on a Sel history out (1,013 / 881 / 232 / 1,670); CT8 unchanged (its histories are constructions) | the reply's "C10′", the opposite of C10: **every selected candidate whose history states no construction stops being an explanation**: the owner's cases (the vane, the signs) and the pole among them, on that history; the suite moves 5 claims (FC12.new2, FC30.new1, FC77, FC102.new1, FC104.new1) and parts of 3. Flag: **S41 Q2** in reverse (the reply: "it declares more, which Q2 permits"); see the candidate list |
| R2V3.6 I90: Dec from chains | 0 | 0 on every generated candidate (chain T′ reproduces the hand-set Dec, 0 moves); C7's, C9's and C10's moves are the same against R2V3.6 as against the hand-set histories (§6) | the reply's "C9's tag counts do not reproduce" **contradicted** (C9 with R2V3.6: the same four histories in, 1,013 / 881 / 232 / 1,670); the chain evaluator equals the program's fixed points on 50,736 (chain, cut) pairs × 6 switch states (0 mismatches) |
| R2V3.7 D11.3: ⪯ the reflexive closure of ≺ | 0 | tag model: a witness two steps before the output no longer counts: Con T → F; generated: every account on the 'Con-far' tag history out (1,013 / 881 / 232 / 1,670); chains n ≤ 4, cut T′: Dec F → T on 4,224 (trace at o_t, output not held) and 11,520 (trace spanning); CT8's R1, R3: constructed → declared (D12.1 and with L201 and L411; T′ unchanged) | (EX): CreateEx T → F on 3 of 1,024 valuations (e_c two or more steps before e); UsesReason F → T on the 1,436 routes that did no work (e3.34b) |
| R2V3.8 D9.2: every argument has a step | 0 | 0 | a premise alone is no argument: X_j(design ∧ PM) 1 → 0 (FC72 (d)); (Suff) by a premise alone: with forms MP only, the pole's constructed candidate leaves Def(L536); generated 392 of 1,600 Out_j T → F. **Departs from S41 Q23** ("Yes, it's an argument"); FC72 and FC72.new1 move in the suite |
| R2V3.9 D9.1 without 'Ans_p(a,b) = y' | 0 | 0 | X_j('Ans_p(a,b) = y') 1 → 0; FC68 (b) T → F; FC47.new1's case: Solved T → F, Prob_j F → T; generated 950 of 1,600 Out_j T → F; FC68 moves in the suite |
| R2V3.10 D15.5 without the construction disjunct | 0 | 0 | of 64 valuations Can 48 → 32, Deploy 24 → 16, CreateEx 3 → 2; D18.1's Can loses Ω; FC32.new1 moves in the suite |

Discovered changes to which candidates meet (E): none. To which count as explanations with (E) unchanged: R2V3.1 (on S108-3-I2), R2V3.2 (re-entry chains; the core and the program part), R2V3.3 (b) (spanning traces), R2V3.4, R2V3.5, R2V3.7 (on the histories each names). Neither: R2V3.6, R2V3.8, R2V3.9, R2V3.10.

## 4. The worked cases and the owner's cases (rule 5.1)

`s108r2_s3_cases.py` A (the 27 cases of the written-in step's script and the owner's 8: the vane and the signs, edit and boundary) under each state of §0 against its baseline; B, C, D, E: `section 3 runs/cases/cases B-E.txt` (this agent's rerun of parts B to E, unbuffered, while part A ran in the queue: `cases/cases.txt`). Part A is in §10; parts B to E:

| part | what | result |
|---|---|---|
| B | the student's declared copy (FC30.new1 (d)) and the bridge (FC84.new1 (a1), (a2)) under all 26 states | **nothing moves**: the copy stays Dec (H = {(1,b1_45)} and H = ∅), the bridge's output stays Con with Build T in every state |
| C | the reply's small cases R2V3.1–R2V3.7 | as §3's rows (each "after" the reply marked not run is run here) |
| D | arguments: FC72 (d), (Suff) by a premise alone, 'p because p', a test's record, FC68 (b), FC47.new1's case | as §3's R2V3.8 and R2V3.9 rows; R2V3.9 with I8 kept and dropped: the same |
| E | Can, Deploy, CreateEx over Θ's 64 valuations | as §3's R2V3.10 row; no definition of (E), Dec or being an explanation reads Can |

FC-E1–E5 and CT1–CT8 (rule 5.2, 5.3): `s104_external.py` prints the same under every state; `s104_creative_transport.py` moves only under R2V3.7 (CT8's R1, R3: constructed → declared by exclusion under D12.1 as the case reads it; T′ unchanged). `s106_cases.py`: no move under any state (`section 3 runs/scripts/`).

## 5. The generated worlds at scale 4 (rule 5.4)

`s108r2_s3_worlds.py cands` on four populations (SMALL 17,280, seed 108301, 1,013 accounts; SMALL with value maps, 108302, 881; proper targets 1,420, 108303, 232; MID 25,920, 108304, 1,670): the counts are in §3; the smallest witness of every move is ports 1–2, dom ≤ 2, comps 1–2, |B| 1–2 (`worlds/cands.*.txt`). Chains (`worlds/chains.txt`, n ≤ 4, cuts T′, T, K, U), record keys (`worlds/keys.txt`, 2,147,344 chains n ≤ 4 with a record flag at every occurrence), arguments (`worlds/args.txt`, FC56's generator, 1,600), routes (`worlds/routes.txt`, 1,460 circuits), FC80's populations with a stated construction (`worlds/fc80x.txt`), ExplUse per occurrence (`worlds/explu.txt`), CreateEx (`worlds/createx.txt`).

## 6. The readings round 1's candidates rest on, under each choice (rule 5 (1))

| candidate | reading | under each choice (generated: SMALL / value maps / proper / MID) | flags |
|---|---|---|---|
| C8 (V3.4) | S108-3-I2 (CT reads Prepares, or ExplUse) × S108-3-I5 (the claim: own question, widest contract, another question) | Prepares: 0 moves under every claim. ExplUse: own 0 on the worked case; widest 122 / 93 / 36 / 200; designation 210 / 140 / 41 / 457; Γ′ 73 / 76 / 10 / 112; port 146 / 118 / 14 / 288 (out, never in) | S41 Q2 comes only under ExplUse with a claim on a contract or question where Acc(ℰ′) fails; goes under Prepares (D12.2 as written) |
| C9 (V3.5) | the key (change / contract), the trace's extent (at o_t / spanning), the tag encoding, cut K, with R2V3.6 and R2V3.7 | every account in on 'Con-chg' tags, spanning chains and re-entry histories (1,013 / 881 / 232 / 1,670 each) under the key 'change'; under 'contract' re-entry is in already, so C9 adds only 'Con-chg' and spanning; with R2V3.7 or R2V3.6 the same; chains n ≤ 4 (T′): trace at o_t 11,240 (all not held at the output), spanning 45,072 held + 39,304 + 3,392; cut K moves held outputs with the trace at o_t (5,118) | none under any choice (S41 Q6 kept: an episode need hold no change) |
| C10 (V3.6) | S108-3-I4 (parts: components / ports / edits), S108-3-I3 (stated construction; none stated: Θ's 𝒯 or ∅), with R2V3.6 | components: 'Sel-parts' in 1,013 / 881 / 232 / 1,670, t′ idle in the same, t′ deviating 638 / 627 / 22 / 889, underdetermined pairs +1,141 / 859 / 469 / 2,577; ports against R2V3.4 ports: 657 / 545 / 178 / 1,070 more; edits: 0 more (R2V3.4 with edits already admits them); against R2V3.5 (𝒯 = ∅): C10 restores every Sel candidate | none |
| C7 (V2.5) | the hand-set histories (R2V3.6) | Sel (H = ∅) in 1,013 / 881 / 232 / 1,670, with R2V3.6 the same | S41 Q2 (in part) stands |

## 7. Round 1's claimed-only edges of the share (rule 5 (2))

| edge | settlement computed | standing | what shows it |
|---|---|---|---|
| e3.30b V3.6 → Sel → Dec → FC80 | FC80's populations with a stated construction (the base member's parts) and deviating twins (S108r2-3-I8), SMALL 120 per size | **computed** | 7,404 populations: under V3.6 𝒯 grows 29,616 → 53,748 members and the populations with an unseen pair underdetermined by the survivors 3,586 → 4,090 (581 more, 0 fewer); under R2V3.4 ports 3,961 (452 more) |
| e3.34b V3.7 → UsesReason (D9.11) | circuits of ≤ 4 occurrences with an objection bound to i (S108r2-3-I7) | **computed** | 'an active route' read as R itself: UsesReason F → T on exactly the 1,436 routes that did no work; read as any route through m's image: 2,684 (1,093 of them routes that did no work) |
| e3.37b V3.8 changes with L628.n2 | – | noted only | the owner's yes or no (S47 with S41 Q6) |

## 8. The edges (the reply's rows, each marked; then added)

| id | variant | kind | item [mark] | standing | what shows it / what would settle it |
|---|---|---|---|---|---|
| R3E01 | R2V3.1 | blocks | L403.s3 [FROZEN] | computed (round 1, e3.19; again here) | Build F where the claim's account fails (E) |
| R3E02 | R2V3.1 | changes with | D12.2 [S2], D13.3 [S3] | computed | CT reading ExplUse: the moves of §3; reading Prepares: 0 |
| R3E03 | R2V3.1 | moves | X:Dec, X:Expl | computed (on S108-3-I2 only) | §3, §6 |
| R3E04 | R2V3.2 | changes with | L55.n3 [S1], FC84.new2 | computed for FC84.new2's re-entry case (Episode per key); L55.n3 a sentence | §3 |
| R3E05 | R2V3.2 | moves | X:Dec, X:Expl | computed | re-entry chains: Dec per key (§3) |
| R3E06 | R2V3.3 | changes with | D12.2 [S2] (Held's reading), D13.3's tuple [S3] | computed | (a), (b) of §3 |
| R3E07 | R2V3.3 | moves | X:Dec, X:Expl | computed | 45,072 held outputs with a spanning trace |
| R3E08 | R2V3.4 | constrains | D12.1 [S2] | computed | Sel's population clause read through parts (ports, edits) |
| R3E09 | R2V3.4 | changes with | L481.s3 [S3] | not settled by computation | a sentence; the parts it names read as ports is the variant |
| R3E10 | R2V3.4 | moves | X:Dec, X:Expl, D12.9 [S4] (Underdet) | computed | §3; underdetermined pairs +1,041 (ports) |
| R3E11 | R2V3.5 | constrains | L195.s1 [FROZEN] | not settled by computation | L195.s1 names 𝒯 and a variation operator; whether 𝒯 = ∅ is a reading of it is the text's |
| R3E12 | R2V3.5 | changes with | L481.s3 [S3] | not settled by computation | a sentence |
| N31 (added) | R2V3.5 | moves | X:Dec, X:Expl | computed | every Sel candidate with no stated construction out (§3); 5 claims move in the suite |
| R3E13 | R2V3.6 | constrains | FC30 | computed | Acc reads no history (FC30): 0 Acc moves |
| R3E14 | R2V3.6 | changes with | I90; C7, C9, C10's counts | **contradicted** | C7, C9 and C10 move the same against R2V3.6 as against the hand-set histories (§6) |
| R3E15 | R2V3.7 | changes with | D14.7 [S3], D12.2 [S2] | computed | CreateEx 3 of 1,024 T → F; Con at a witness two steps back F |
| R3E16 | R2V3.7 | moves | X:Dec, X:Expl | computed | §3 |
| R3E17 | R2V3.8 | changes with | D9.6, D9.7, L397.s16 [S3] | computed for D9.6 (usable), D9.7 (Out_j); L397.s16 a sentence | §3 |
| R3E18 | R2V3.8 | moves | X:(Suff), X:(Nec), D10.1 [FROZEN] | computed for (Suff) (the pole's candidate leaves Def(L536) with MP only); D10.1 and (Nec) not computed | §4 D |
| R3E19 | R2V3.9 | constrains | L397.s5 [FROZEN] | not settled by computation | a sentence listing the claims |
| R3E20 | R2V3.9 | changes with | D9.8, D10.3 [S2] | computed (FC47.new1's case: Solved T → F, Prob_j F → T) | §4 D |
| R3E21 | R2V3.10 | constrains | D15.7 [FROZEN] | not settled by computation | – |
| R3E22 | R2V3.10 | changes with | D13.1, D13.2 [FROZEN], D14.7 [S3], D16.1 [FROZEN] | computed for D13.1 (Deploy 24 → 16), D14.7 (CreateEx 3 → 2); D13.2, D16.1 not computed | §4 E |
| N32 (added) | R2V3.1–R2V3.10 | independent of | X:(E) | computed | 0 Acc moves in every population, case and state |
| N33 (added) | R2V3.2 | changes with | D13.8 as the core states it against the program (I174) | computed | the program's key is the change; the core's words key by the new contract; they part on re-entry chains |

## 9. The whole suite (a script, S56)

Run by the agent that continued after the restart with `tools/sonnet_harness/run_claims.py` (not a Sonnet worker and verifier: a departure from the rule's harness clause, recorded in the map's §0; S55, S56), scale 4, time cap 45, against the round-4 record: off and each state of §0 (`whole suite/section 3/`). The single-claim runs made before (`section 3 runs/single/`, the claims whose code reaches each switch) expected: R2V3.1 FC90.new1; R2V3.5 FC12.new2, FC30.new1, FC77, FC102.new1, FC104.new1 (status) and FC12.new1, FC80.new1, FC83 (parts); R2V3.8 FC72, FC72.new1; R2V3.9 FC68; R2V3.10 FC32.new1; the others none. Results: off 133 / 2 / 7, no difference; every state moved exactly the claims the single runs expected (R2V3.1 FC90.new1; R2V3.5 the eight; R2V3.8 FC72, FC72.new1; R2V3.9 FC68; R2V3.10 FC32.new1; the others none). The map's §5.

## 10. Addendum: part A (the worked cases)

`cases/cases.txt` (the queue's run, 2,194 s, exit 0; the reruns of parts B to E agree with its B to E). 35 cases, 30 meeting (E) (27 of the written-in step's script, 8 of the owner's: the vane as an edit and as a boundary, the signs as edits and as boundaries). (E) moves under no state (0 of 35 × 26). Account ∧ ¬Dec(t), (case, history) moving against each state's baseline:

| state | moves | the owner's cases among them |
|---|---|---|
| R2V3.1 (C8 with CT reading ExplUse) | out 18 (the claim about another port, δ′), 10 (the claim on the question on another port), 2 (the widest contract) | **the weathervane** (M13; as an edit and as a boundary, Γ = {cP}, {cW,cP}) on the δ′ and port claims; the day-port sign; not the two-part or one-part sign |
| C8 with CT reading Prepares | 0 | – |
| R2V3.2 key 'contract' against 'change' | in 30 (re-entry, tags and spanning chains) | all 8 |
| R2V3.4 ports / edits | in 7 / 30 ('Sel-parts') | edits: all 8 |
| R2V3.5 | **out 30: every candidate meeting (E) on the 'Sel' history** | **all 8: the vane and both signs, in every encoding** |
| R2V3.6 | 0 (5 Dec moves, all on candidates failing (E)) | – |
| R2V3.7 | out 30 ('Con-far' tags) | all 8 |
| R2V3.8, R2V3.9, R2V3.10 | 0 | – |
| C9: V3.5 (key change / contract / with R2V3.7 / with R2V3.6) | in 30 on each history it reaches (four / two / three / four histories) | all 8 |
| C10: V3.6 components / ports / edits / with R2V3.6 / against R2V3.5 | in 30 / 23 / 0 / 30 / 30 + 30 | all 8 where 30 |
| C7: V2.5, and with R2V3.6 | in 30 ('Sel (H = ∅)') | all 8 |

The worked cases give the same pattern as the generated worlds (§3, §6): each reading bites on every candidate meeting (E) on the history it names, except R2V3.1, which bites only where the claim the construction used fails (E), and R2V3.4 with ports (7 of 30). On the owner's cases, **C8 under S108-3-I2 drops the weathervane** (on the claims about another port), and **R2V3.5 drops the vane and both signs on a selection history** (the candidate list's C8 and C16).
