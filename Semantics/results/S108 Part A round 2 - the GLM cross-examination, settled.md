# S108 Part A round 2 - the GLM cross-examination, settled

*Written 29 September 2026 by one Opus 5.5 agent (decision S56: "It's capable of doing the whole thing on its own. Use GLM for cross examination. No need to Opus to do single sections"), under rules 3 to 7 of `results/S108 Part A round 2 - how the GLM cross-examination will be read, written before sending.md` (committed before sending). This agent did not build the work cross-examined; it weighs arguments, not their source. An objection is a claim until settled; several jobs saying the same thing decides nothing; silence is not agreement. "Candidate" or "explanation" for what the theory judges, never "model" (S43). Nothing here changes the theory's text, formal core, claims or program after round 4, round 1's files or program copies, or the decisions record (rule 11). No owner decision is added.*

## 0. The condition for opening, and what came back

The run log (`S108 Part A round 2 - GLM cross-examination returns/run log.txt`) ends "s108r2x_glm_loop: every pass ended; accepted 4 of 4 jobs" and "loop ended 2026-09-29T02:41:21Z"; the process had exited. Receipts, checked before any reply was read: key_found_in_output_and_replaced = 0 and sandbox_unchanged = true for all four; model glm-5.3; each reply ends END OF REPORT (job a 1,436 words, b 1,195, c 1,577, d 1,298). Returns at commit 937229f.

| job | angle | objections | stand | stand in part | do not stand |
|---|---|---|---|---|---|
| a | sections 1 and 2 | 4 (Xa1–Xa4) | 3 | 0 | 1 |
| b | sections 3 and 4 | 5 (Xb1–Xb5) | 1 | 3 | 1 |
| c | the dependency map | 5 (Xc1–Xc5) | 2 | 3 | 0 |
| d | the candidate list against S20–S56 | 2 (Xd1–Xd2) | 1 | 1 | 0 |
| all | | **16** | **7** | **7** | **2** |

GLM's own ids (X1.1 … X4.2) are renamed Xa1 … Xd2 in the order each reply gives them. Where a reply names an edge id of the map that is off by one row, the edge meant is found by its content and named here.

**Runs made for the settlement** (all in the round-2 program copies, run from the folder holding `model/`, `PYTHONHASHSEED=0`, `python3 -B`, under `timeout`; outputs in `S108 Part A round 2 - computation/cross-examination runs/`):

- **Xa1**: section 2's worked-case script `s108r2_s2_cases.py` rerun section by section (`--sections 2a`, `2c`, `3`, `4`, `5`, and `1,2b`), timeout 3 hours each, 4 CPUs; section 1 also in three shards of the cases after the 23rd (the same code path, `shard.py`), because two of its cases (E9's two-layer episode, L626 and L630) take minutes each.
- **Xb1**: `xb1_e_readings.py` in section 4's copy: R2V4.3's reading (e) on the same 3,208 chains under three readings of "Sel at o".
- **Xb3, Xc4**: `python3 -m model.run --claim FC98 --claim FC32.new1 --no-write` in section 4's copy (off).
- **Xc1**: `xc1_nec_under_r2v38.py` in section 3's copy: R2V3.8's effect on (Nec)'s defeat set, the one part split off that a short run could settle (the mirror of section 3's part D for (Suff)).
- **The map's amendments**: `s108r2x_map_amend.py` (reads the map after round 2, md5-asserted, never written; writes the corrected copy).

## 1. The objections and their settlement

### Job a: the computations of sections 1 and 2

**Xa1. Section 2's worked-case numbers rest on no surviving run** (the script's output stops after 22 of 60 cases; its `.json` is absent; the run log shows two exits 143, the timeout's; so §2's counts, §7.1's C5, C3, C4 rows, all of §7.3, §9's Desc per case, §10's rows and §8's e2.06c, e2.07 values are not shown by any kept output).
*Settlement: **stands** (as to the record); settled by a run.* The record is as the objection says: `section 2 runs/run log.txt` reads "gen exit 0 / cases exit 143 / cases exit 143"; the kept output ends at the 22nd case; section 2's file does not record the two failures. Rerun (above): every section ended with exit 0 (2a, 3, 4, 5 in seconds; 2c in 51 s; 1 and 2b in 12 minutes, the two E9 cases taking most of it), and **every number the objection lists reproduces**: §2: R2V2.8 program 26 cases T → F and 52 (case, history) pairs, widest 51 and 102, V2.4 × every / some / some-exempt / some-exempt-set 21 / 29 / 25 / 26 (42 / 58 / 50 / 52 pairs), V2.5 and V2.5 × R2V2.3a 51 pairs each, every other setting 0; the first 25 lines are byte-identical with the kept partial output. §7.1: C5 T on every edit and mixed case, F on every boundary case (the vane's and the sign's candidates and E_enc), the witness pair (setW1, b_still) under V2.3; C3, C4 all T; C6's and C11's rows as written. §7.2: C6 = C11 on every case under every reading; the drops beyond 'every' as listed. §7.3: chains 1,071; C7 admits 663 under T′ (H = ∅), 408 stay declared, 357 under T, 0 under U (no fixed point, "other change"); (b) 0 of 51 accounts fail surv on any pair; ℰ_bad as written. §9: BadTarget T for the sign (4 targets) and the vane (3), F for the pole, the balances, the hand-turned vane; the bridge not computable; widest T on all 36 worked targets. §10 and §8: ℰ_bal Acc T → F under V2.3 (Dependence), Ident's clause T; C_id I163 T, V1.4 F, E_fwd, E_rev T → F; R2V2.5's case; R2V2.6's reaches (51 of 51 Sel only where o1 represents t, H or surv under 'written'; cod t only at the reply's reach; the student's copy [{'o1': 'Con', 'o2': 'Sel'}] only at the reply's reach); R2V2.10's case (Viol, SelResp F → T; Surp F); e2.11b, e2.16c, e2.19 as written. The kept output's first two runs were cut by a timeout shorter than the run needs; nothing in the file was wrong, only unbacked.
*Changes:* the map's edges r2e2.02 (R2E03), r2e2.05 (R2E06), r2e2.06 (R2E07), e2.06c and e2.07 carry a note that their numbers now rest on the rerun (`cross-examination runs/Xa1 section 2 worked cases, rerun/`, outputs and `.json` per section, with its run log); no standing and no count changes in the map or the list. Section 2's file is kept as it was sent; this entry is its erratum (the two failed runs; the rerun).

**Xa2. Section 1 §3.1, row "R2V1.1, recorded declared": the CreateEx cell reads "0" and drops the qualifier the I5 row carries** (1 of 1,024 where the brief's own ρ is selected or constructed).
*Settlement: **stands**.* `section 1 runs/cases/cases.txt` lines 48–51: under recorded declared, ρ(brief) declared or unrecorded gives 0 of 1,024 on (a2), selected or constructed gives 1. The cell should read "0 (brief unrecorded or declared); 1 (brief selected or constructed)".
*Changes:* none in the map or the list (both already say "where its brief is declared"); recorded here as section 1's erratum.

**Xa3. Section 1's file still says its whole-suite runs are "a harness job … not run here"**, though all seven ran and matched §6's expectations; section 2 got an addendum, section 1 none.
*Settlement: **stands**.* Section 1's status line and §6 say so; `whole suite/section 1/` holds the seven runs; the map's §5 lists them (off, R2V1.1 selected / constructed, R2V1.6, R2V1.6s: none moved; R2V1.1 declared: the 19 claims; R2V1.10: the 25), each as §6 expected.
*Changes:* recorded here as section 1's addendum: the one Opus agent that continued after the restart ran the seven settings by script (`run_claims.py`, scale 4, cap 45, against the round-4 record; S55, S56), and each moved exactly the claims §6 expected. The map's §0 already records the staffing. Section 1's file is kept as it was sent.

**Xa4. S44 is quoted as "In either case, it is an explanation."; the objection says the owner's words are "In either case, it's an explanation."**
*Settlement: **does not stand**.* `records/Semantics - Decisions.md`, S44, the owner's words: "… It's a bad explanation, whether from the perspective of the agent itself, or an external observer. In either case, it is an explanation. Just not a good one …". The quotation is verbatim; the contracted form occurs in no file of the project but the reply and its own reasoning (not in its brief either).
*Changes:* none.

### Job b: the computations of sections 3 and 4

**Xb1. R2V4.3: "contradicted" (the reply's lemma that reading (e) moves nothing) holds only under S108r2-4-I3's reading of "Sel at o"** (Sel's conditions staged at a holding that holds t); read as the fixed point's value, the relay inherits Sel and the lemma may hold.
*Settlement: **stands**; settled by a run.* The reply's (e): "∃o (any holding of the content D11.2 of t): Sel at o or a construction trace prepares t at o". Run (`xb1_e_readings.py`, same 3,208 chains with one fixed point under T′): (e) as computed (S108r2-4-I3: held, Sel's conditions staged there, or a trace) differs from ¬Dec at 210 last holdings, **25** with t held; (e) with t held at o and Sel read as the fixed point's value (inherited) or a trace: 191, **4** with t held; (e) at any holding, Sel as the fixed point's value or a trace (the objection's reading): **0**. So the lemma is contradicted under S108r2-4-I3 and under the second reading, and holds under the third.
*Changes:* map: r2e4.06 (R4E07) keeps "contradicted" qualified "under S108r2-4-I3 (25) and the inherited value at a holding of t (4)"; a new part r2e4.06b, computed, "independent of X:Expl on chains when 'Sel at o' is the fixed point's value at any holding: 0 moves"; r2e4.05 (R4E06, "constrains D12.4") qualified likewise, with r2e4.05b contradicted on the third reading (0 departures). List: C13's (e) entry reads "25 of 3,208 under S108r2-4-I3; 4 with the inherited value at a holding of t; 0 at any holding"; the reading is added to the readings computed more than one way. C13 is unflagged and stays so.

**Xb2. Section 4's settlement of e4.40 names L574.s5, which is not one of e4.40's items, and its `.json` gives the whole settlement the standing "computed"** although of its four items one is computed, one independent, two not settled.
*Settlement: **stands in part**.* Section 4's `.json` row "settles e4.40" has standing "computed" and names L574.s5 among the computed; that summary overstates. But the map did not take the summary: it split e4.40 by item (e4.40a computed: L572.s2, with L574.s5 as the survivors' agreement it shows; e4.40b contradicted: L574.n4; e4.40c claimed only: L576.s1, L576.s4), which job c checked and found right.
*Changes:* none in the map or the list; recorded here as section 4's erratum.

**Xb3. R4E18 cites "§8" and R4E05 "the whole suite §8", but §8 has no R2V4.8 or R2V4.2 run; and R2V4.8 varies a cut the suite's FC32.new1 (b) and FC98 (c) read, so §0's "the variants read no code the suite runs" is inaccurate for it; the missing suite run is neither made nor recorded as a departure.**
*Settlement: **stands in part**.* The pointers are wrong: section 4's §8 lists off, R2V4.1 ×3, R2V4.5, R2V4.7 only. But FC98 (c) and FC32.new1 (b) compute cut U themselves, beside K, T and T′, in every off run (run: FC98 (c) "reading U (as worded): two fixed points for a first construction and none for a selection"; FC32.new1 (b) "U: Live → (K2) → Live"), so R4E18's content ("under U no unique provenance on any account") is shown by the off run of those claims and by section 4's §2 and worlds (U: 2 or 0 fixed points on every account). A whole-suite run with U forced in place of T′ was not made: R2V4.8 is a function parameter (`rd="U"`), not a switch of the copy, and its effect on everything that reads provenance is what N41 already computes (Dec with two values or none wherever t is held). Recorded as a departure.
*Changes:* map: r2e4.17 (R4E18) evidence re-pointed to the claims' own parts and section 4 §2; r2e4.04 (R4E05) re-pointed to round 1's suite under V4.2 and section 4 §2; the departure recorded (§5 of the map after the cross-examination). Standings unchanged.

**Xb4. Two record pointers in section 3 are wrong: `worlds/keys.txt` does not exist (the run is `worlds/recflags.txt`), and `suite - expected moves.json`, listed in §0 as in `section 3 runs/`, is absent.**
*Settlement: **stands in part**.* `worlds/keys.txt` exists in the repository (`section 3 runs/worlds/keys.txt`, first line "keys, cut T', n ≤ 4 …"); the sandbox's manifest copied it under the name `recflags.txt` (`material for the GLM cross-examination/sandbox manifest, job 2.json`), so that part is the build's renaming, not the file's error. `suite - expected moves.json` is named in section 3's §0 and exists only in `section 1 runs/`: that pointer is wrong. Nothing rests on it (the reply re-derived §9's expectations from the single-claim runs and the suite, and they hold).
*Changes:* none in the map or the list; recorded here as section 3's erratum.

**Xb5. Section 3 §10, R2V3.1 row: the glosses are swapped ("out 18 (the claim about another port, δ′), 10 (the claim on the question on another port)"; 18 is the designation claim, 10 the port claim).**
*Settlement: **does not stand**.* S108r2-3-I1 defines the designation claim by δ′ := "the first port of E other than δ_E" (a claim about another port) and the port claim as "the question on the first other port of D". The file's gloss gives 18 to the claim about another port δ′ (the designation claim) and 10 to the claim on the question on another port (the port claim): the reply's own reading, stated in other words. `cases.txt` line 56 agrees.
*Changes:* none.

### Job c: the dependency map

**Xc1. Round-2 edges whose parts differ in standing enter the map under their headline standing, so parts the section files say are not computed, or contradicted, count as computed** (round 1 split such rows; the round-2 builder takes one standing per row).
*Settlement: **stands**.* The builder (`map after round 2/s108r2_map_build.py`) takes one standing per row. Every round-2 edge whose `standing_as_written` names parts of different standing (found by search, not only those the reply lists; its ids are one row off in places): r2e3.18 (D10.1, (Nec) not computed), r2e3.22 (D13.2, D16.1 not computed), r2e3.17 (L397.s16 a sentence), r2e3.03 (L55.n3 a sentence), r2e2.18 (L231.s3 not computed), r2e2.20 (contradicted as to Surp at a pair of H), r2e2.21 (D12.1 unchanged), r2e2.16 ((Nec) independent), r2e4.09 (L630.s5 not computed), r2e2.13 (contradicted at the sentence's reach, computed with the whole exclusion dropped); and the round-1 edge e1.46, settled by R2V2.8 with the same shape ((Nec) independent). r2e4.21 is contradicted in both its parts and needs no split.
Of the parts, one could be settled at once by a run: R2V3.8's effect on (Nec) (`xc1_nec_under_r2v38.py`, section 3's copy, the pole's constructed candidate on the three hand-set histories): (Nec) as L538 states it is defeated on no history, off or under R2V3.8 (t is faithful on C, which L538's defeat excludes); under L61's 'their' reading the declared history with j accepting only r ∧ (r → Expl(ℰ)) and modus ponens goes from in the defeat set to out (the premise-alone argument is no argument), the mirror of the (Suff) case section 3 computed. So "R2V3.8 moves (Nec)" is contradicted as to D16.XV's (Nec) and computed as to L61's reading, as e2.11b was in round 2.
*Changes:* map: eleven rows split into twelve parts, each marked Xc1: six claimed only (r2e3.18c D10.1, r2e3.22b, r2e3.17b, r2e3.03b, r2e2.18b, r2e4.09b), five contradicted (r2e3.18b (Nec) under R2V3.8, r2e2.20b, r2e2.21b, r2e2.16b, e1.46b), one computed (r2e2.13b: R2V2.6 at the reply's reach moves Dec and Expl, C21's ground). Items that lose "computed": L231.s3, L630.s5, D13.2, D16.1 (now claimed only); L55.n3, L397.s16, D10.1, D12.1 and X:(Nec) stay computed through other edges. §6.2's list of edges claimed only gains the six claimed-only parts.

**Xc2. The map's §7 verdict (no third round) does not reckon with the middle definitions upstream of the explanation definition that no variant of either round has varied: D6.5 (Dependence), D12.3 (Dec), D18.1 (the order).** §7 argues about D5.7 only; its sentence that every upstream middle definition is varied or computed holds only under the convention that a definition named by a computed edge counts as touched.
*Settlement: **stands in part**.* True that §7 names only D5.7 and that D6.5, D12.3 and D18.1 are never varied themselves (the map's §6.1 lists them). Not true that this leaves a gap a third round inside Part A's rule could reach and that the computation has not already given:
- **D6.5** is "Dependence(ℰ) :⟺ NC0 ∧ NC2", and NC0 holds of every candidate (D6.2), so D6.5 is NC2 (D6.4). Its content has been varied through D6.4 four ways (V2.1, V2.2, V2.3, V2.3b) and through the conjunct V2.4 restores (the written-in test, D6.5's form before S106, C6). A variant of D6.5 that is not one of these adds or removes a conjunct of (E) itself, which is D6.7's.
- **D12.3**'s first sentence is D12.4's inheritance [FROZEN]; its second is the complement of Sel ∨ Con. Sel and Con were varied by fourteen variants over the two rounds (D11.2, D11.3, D12.1, D12.2, D12.7, D13.3, D13.8, D15.5, D15.8, and the readings of histories). The complement's own form, varied, gives only limits the list already carries: every constructed link declared (the widest case of C8's and C20's direction), every selected link declared (C16's), the rule dropped (C12). Their effect is the count of accounts on the history kind dropped, already computed.
- **D18.1** is the order, not a definition a candidate reads. Round 2 varied it where it binds the explanation definition, through L526.s18 (R2V4.8: cut U, Dec without a value), and FC32.new1 and FC98 compute the graph under every cut.
*Changes:* the map's §7 after the cross-examination names D6.5, D12.3 and D18.1 and gives this argument; the `.json`'s `gaps` gains the note, and `third_round_needed` the verdict (§4 below).

**Xc3. The row that settles e2.38 and e2.39 (R2V2.11) is dropped by the builder because section 2's `.json` has `"round1_edge": "e2.38,"` (a trailing comma), so the two edges carry no round-2 note and no entry in the changes.**
*Settlement: **stands**.* Section 2's `.json` line 463 has `"id": "settles e2.38,"`, variant "e2.39"; the builder's `if rid not in edges: continue` skips it; the map `.json`'s e2.38 and e2.39 have no `round2_note`; the md's §3 states the closure in prose only.
*Changes:* map: e2.38 and e2.39 carry the round-2 note (FC21.v1, FC21.v2 close the suite's blind spots), and two rows are added to the changes table (standing unchanged, computed), marked Xc3. Section 2's `.json` is kept as sent.

**Xc4. r2e4.17 (R2V4.8 constrains FC32.new1 (b), FC98 (c)) is computed on no locatable output: its "§8" has no R2V4.8 run, and the map's §5 has no run under U.**
*Settlement: **stands in part**.* The same as Xb3: the pointer is wrong; the output exists (the two claim parts compute U in every off run; section 4 §2 and worlds).
*Changes:* as Xb3.

**Xc5. §6.3 drops round 1's row "S108-4-I7: V4.7 computed on a toy only", though D16.3 was not varied again; its reach by D18.1 includes the defeat conditions, which the map counts among the explanation definition's parts.**
*Settlement: **stands in part**.* The row belongs in §6.3: the reading is still computed one way only. But the reach the objection gives it is wrong: round 1's map row for V4.7 has "– / – / –" in the reach column (the "yes" the reply quotes is V4.1's row), and e4.35 records that Enable is reached by UU, UC, UECS and Classes only, and that (E), Dec and the defeat conditions do not reach it. So the row does not bear on the explanation definition.
*Changes:* map: §6.3 gains the row, with "does not bear on the explanation definition (e4.35)", marked Xc5.

### Job d: the candidate list against the owner's decisions S20 to S56

**Xd1. C2's flag on S41 Q6 (the bridge) is marked "on that reading" for the question's history only, but the computation reaches it on three further conditions the list never names: the move is on (a2) (a first design criticized), not (a1), where nothing moves; "created" is read as CreateEx (Con and Build do not move); and p_c is the brief (S108r2-1-I3).** The reply also says (a1) is the owner's case as S47 writes it, so that on the owner's case nothing changes.
*Settlement: **stands in part**.* The three conditions hold (section 1 §3.1 note: "(a1) … CreateEx 0 of 1,024 under every choice"; §11: "created" read two ways, Con and Build (no move) or CreateEx (moves); "p_c = the brief (S108r2-1-I3) decides the bridge's CreateEx"), and the list should name them. The further claim, that (a1) is the owner's case and (a2) is not, does not stand: S47 writes the bridge "as an episode in which no question about the brief occurred to the agent, not as one with no criticism", and the program's reading of that (I190; FC32.new1 (f)) is "the bridge, Con with or without criticism of designs": (a1) and (a2) are both that case. Which of the two the owner meant is a question about the case's history, the owner's to settle (rule 6): recorded, not applied.
*Changes:* list: C2's round-2 cell and its S41 Q6 flag name the three conditions, "on that reading"; §0's list of readings and §5's gaps gain "the bridge's history (a1 or a2), 'created' as CreateEx, p_c the brief"; §4's plain sentence for C2 is reworded so that it makes no claim about which history the owner meant.

**Xd2. C16 names S41 Q2 without the owner's words and calls the question "the owner's question"; S41's questions are Claude's (the list's own §6).**
*Settlement: **stands**.* The cell reads "the owner's question set a link 'simply declared' against one 'found by trial or worked out'"; the record: the question was Claude's, the owner's answer "No, not if just declared".
*Changes:* list: C16's decisions cell and §4 quote the owner's answer and name the question as the one the owner answered.

## 2. What was not raised, and what the jobs did not reach

The four jobs checked most counts against the kept outputs and reran claims the guard allowed; every count they checked reproduced, apart from the points above. They did not reach, and this settlement does not add: the md5 checks of the copies; section 4's program code (not in its sandbox); a line-by-line reading of the generators; a second run of the whole suite by a verifier (the runs were made once, by script). This agent reran what the objections needed, not the suite.

## 3. Totals after the cross-examination

**The map** (`S108 Part A round 2 - the dependency map, after the cross-examination.md` / `.json`; the map after round 2 kept as sent):

| | after round 2 (as sent) | after the cross-examination |
|---|---|---|
| nodes | 876 | 876 |
| edges | 337: computed 265, claimed only 46, contradicted 26 | **351: computed 268, claimed only 51, contradicted 32** |
| round-2 edges | 110: 70 / 32 / 8 | 123: 72 / 38 / 13 |
| parts split off | – | 14 (12 from 11 rows [Xc1]; 2 [Xb1]) |
| template items touched (815) | computed 191, claimed only 33, untouched 591 | computed 187, claimed only 37, untouched 591 (L231.s3, L630.s5, D13.2, D16.1 now claimed only) |
| middle items untouched | 426 | 426 |
| middle definitions untouched | D5.7, D8.new1, D13.7, D14.1, D15.1, D15.2 | the same |

One more edge was settled by this agent's own check under rule 5, not by an objection: **e2.14b** (V2.5 moves (Suff)'s defeat set; claimed only since correction O2, "not computed in either round"): run `e2_14b_suff_under_v25.py` in section 2's copy: on the 51 worked accounts with the history 'nothing tried', with an argument not using (E) that rules the explanation out, (Suff)'s defeat set as L536 and as L17 (S41) holds 0 off and 51 under V2.5 (and crossed with R2V2.3a); as L17 as text 104 words it, 51 either way. Standing: computed.

**The list** (`S108 Part A round 2 - candidate definitions of explanation, after the cross-examination.md`; the list after round 2 kept as sent): **21 candidates**, **11 flagged** (the same eleven; no flag added or removed): C1 (S44); C2 (S44, S41 Q15, S41 Q6, each on that reading; for the bridge also its history, "created" and the brief [Xd1]); C5 (S41 Q15, S44, on that reading); C6 (S45; S44 on that reading); C7 (S41 Q2 in part); C8 (S41 Q2, S41 Q15, on that reading); C11 (S45; S44 on that reading); C12 (S41 Q2); C15 (S44, S41 Q15, at that grain); C16 (S41 Q2 with the owner's words [Xd2]; S44, S41 Q15 on a selection history); C21 (S41 Q2, on the reply's reading). C13's reading (e) is qualified [Xb1] and stays unflagged.

## 4. A third round of Part A, or Part B (rule 5)

**Part A ends; Part B follows (S52).** No third round.

Rule 5 asks whether gaps that bear on the explanation definition remain after the settled findings: items still untouched that are upstream of (E), Dec, Expl, (Suff) or (Nec), or edges on them the computation could not settle, that a variant inside Part A's rule could reach. After the settlement:

- **Untouched upstream items.** The middle definitions still untouched are D5.7, D8.new1, D13.7, D14.1, D15.1, D15.2. Of these only D5.7 is upstream, and its one variant rewrites L189.s2 [FROZEN], so it cannot be varied inside Part A's rule; it belongs to Part B. Xc2's three never-varied definitions (D6.5, D12.3, D18.1) leave nothing a variant could reach that the computation has not already given (§1, Xc2). The 426 untouched middle sentences are mostly not upstream (the section agents' reading, not contested by any job); a sentence-by-sentence pass would be a round of its own, and round 2's evidence (only R2V1.6 among sentence variants moved Expl) says it would rarely reach the definition.
- **Unsettled edges on the definition's parts.** After the settlement, the claimed-only edges on (E), Dec, Expl, (Suff), (Nec) are e1.51, e2.20, e2.21 (V1.7, V2.8: ruled to Part B, or computed as V4.4 in round 1), r2e1.28, r2e1.33, r2e1.36, r2e2.07 (variants the tabulation flagged out of scope and did not implement: the orchestrator's, rule 4), and r2e4.13 (R2V4.6's unindexed defeat sets: a reading with no code). e2.14b was settled by a run (§3), and R2V3.8's (Nec) part (r2e3.18b) too. None is an edge a variant inside Part A's rule could reach that has not been reached.
- **The readings the owner's cases turn on** (the change as an edit or a boundary; D6.3's quantifier; a question's recorded history; Desc's grain; now also the bridge's history, Xd1) are the owner's to settle, not a round's (rule 6).

So Part B follows: freeze all but the hard-to-vary parts and vary those (S52), under its own rule written and committed before sending, then the flags for the owner's yes or no.

Settled by one Opus 5.5 agent under rules 3 to 7 of the cross-examination's rule and decision S56, 29 September 2026. Nothing applied to the theory (rule 11); no owner decision added.
