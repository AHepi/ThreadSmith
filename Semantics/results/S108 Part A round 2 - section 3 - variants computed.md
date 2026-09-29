# S108 Part A round 2 - section 3 - variants computed

*Computing agent for section 3 (rule 5 of `S108 Part A round 2 - how the replies will be read, written before sending.md`; Opus 5.5 per `S108 Part A round 2 - who computes, recorded before any reply is opened.md`), 28–29 September 2026. Fresh. Works only in `S108 Part A round 2 - computation/section 3 model/` (a copy of round 1's `S108 Part A - computation/section 3 model/`, 36 files md5-identical at the copy; round 1's copy never written). Runs in `S108 Part A round 2 - computation/section 3 runs/`. Nothing here changes the theory (rule 11). "Candidate" or "explanation" for what the theory judges; "model" only for the program or a small structure it builds (S43). Read with the reply (`s108r2_glm_section3.response.txt`, 34a8e69f…) and the tabulation (§2–§8).*

Status: in progress, filled as it goes; nothing ruled.

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
