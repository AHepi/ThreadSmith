# S108 Part A round 1 — what the variations found

*Written on 28 September 2026 by a Claude subagent (Opus 5.5), the records step of Part A's round 1 (rule 15 of `S108 Part A - how the replies will be read, written before sending.md`), from the files named below; it ruled on nothing. It read the four receipts' timing, key and sandbox fields, not the replies, reasoning or request files, and did not open `S108 Part A - Sonnet 5.5 trial/`. Nothing in the theory is changed: Part A is an experiment on copies (rule 11); the text (`tests/107`, md5 c7af964c329ab7959243405d394e6574), the formal core after round 4, its claims and the program after round 4 are as round 4 left them. Terse by decision S40. Obeys decision S23 except where it quotes the owner; "candidate" or "explanation" for what the theory judges, never "model" (S43). Where the corrected map and list differ from earlier files, the second checker's versions govern. Nothing here is settled (S28).*

## In brief

- **Asked (S52).** Freeze the parts that are hard to vary, vary the middle, see how the definition of explanation changes; map the dependencies; four GLM agents, one section each, one frozen template; Opus for the review.
- **Frozen set** (Claude's reading of "the parts that are hard to vary"; the owner has not answered on it): **238 frozen, 577 middle, of 815** items (169 of 688 sentences, 69 of 127 definitions and encodings frozen).
- **Run.** Four GLM 5.3 calls through Claude Code, medium effort, in round 3's sandbox, unchanged; sent 18:10:29 UTC; 4 of 4 accepted on attempt 1 by 18:19:20 (380 to 531 s); no key in any output; every sandbox unchanged (50 files).
- **Tabulated.** **32 variants, 8 per section**; 3 flagged and not run (V1.6, V1.7, V2.8); **29 run**. Every "after" in every reply was marked not run by the reply.
- **Computed** by four Opus 5.5 agents, each in its own copy of the program: worked cases, FC-E1–E5, CT1–CT8, generated candidates at scale 4, and the whole suite under each variant.
- **Effect on explanation** (computed): **6** variants change which candidates meet (E); **7** change which count as explanations while (E) stays; **16** move neither.
- **The largest move: V1.1** (D1.4, what (F1), "each part matches", reads): **15 of 27** worked cases stop meeting (E), among them the owner's two-part shop sign (S44's case) and the weathervane's mechanism (M13, S41 Q15's case); it blocks the FROZEN D4.4, and the claim FC85 (a), "a content matches itself", fails.
- **Roles and kinds.** V1.2, V1.3, V1.4, V1.8 (D2.1, D2.4, D3.3, D2.6) move families, Prod and Ident, and (E) on **0 of 61,914** generated candidates.
- **One way.** Varying ruling out, conflict, creation, routes, the defeat sets and universality moved neither (E) nor being an explanation anywhere: they sit downstream of it or aside (map §2).
- **The map (corrected): 859 nodes, 221 edges** (computed 179, claimed only 31, contradicted 11). **647 of 815** items untouched (473 of 577 middle).
- **Candidates: 13** (C1–C13); **8 flagged** against the owner's decisions (C1, C2, C5, C6, C7, C8, C11, C12), several only under a reading. Nothing applied; the owner's yes or no comes after Part B (S52).
- **Review.** O1–O4 matter, O5–O13 minor; all 13 to one second checker (the orchestrator's decision 1): the review's fix on 12, a third fix on O3.
- **A finding about the theory after round 4.** L538.s2 ("Eliminative explanation (Part VII) is the exposed case") is not met by E5's encodings, with no variant on. Recorded for later; the series is on hold (S52).
- **Moves: none.** Part A changes nothing in the theory.
- **Round 2 of Part A follows** (the orchestrator's decision 4), under its own rule, written and committed before sending.

## 1. The frozen set (bbe1040)

- `tools/s108_frozen_set.py`; `S108 Part A - the frozen set.md` (367c4b1f…) and `.json` (30ca39e3…); plain file 108 for the owner.
- Criterion: FROZEN when (a) put to the readers or checkers at least once and (b) no round or step changed it since; otherwise the middle; where the record cannot tell, the middle.

| | frozen | middle | all |
|---|---|---|---|
| sentences | 169 | 519 | 688 |
| definitions and encodings | 69 | 58 | 127 |
| all items | **238** | **577** | **815** |

- Of S100's 36 strong candidates, 27 frozen, 9 changed later.
- The seven definitions round 4 changed (D0.2, D6.3, D7.4, D9.10, D16.XV, E1, D18.1) were all in the middle.

## 2. The build and the run

- **Printouts** (cb74c40): the program after round 4, whole suite 133 / 2 / 7 of 142; the three case scripts at round 4's md5s.
- **Build** (00adfab, 18:09 UTC; one Opus 5.5 agent): `tools/s108_build.py` (e5b5b5d5…); the frozen template (0c5ad262…); four sections, contiguous Parts, balanced by middle items: **S1** Parts 0–III (154), **S2** IV–VII (153), **S3** VIII–XII (137), **S4** XIII–XVI (133); four briefs (4,916 to 4,928 words by `wc`); the job list; the runner `tools/s108_glm_loop.py` (round 4's, names changed); the reading rule (15 rules; 0909c53d…); the sandbox manifest (49 files and the brief). The helper, guard and imports byte-identical to round 3's; decoy tests not rerun; a dummy-key check of this round's sandbox passed.
- **Run.** Sent 18:10:29 UTC (468466e); every attempt 1; ended 18:16:49 to 18:19:20 (380, 434.8, 490, 531.2 s; 13 to 31 turns); replies 2,390 to 2,636 words, each ending END OF REPORT. Receipts: key replaced 0 times in each; every sandbox unchanged. Returns committed before any was opened (687812c).

## 3. The tabulation (dd73829; one fresh Opus 5.5 agent)

| | S1 | S2 | S3 | S4 | all |
|---|---|---|---|---|---|
| variants | 8 | 8 | 8 | 8 | **32** |
| delete / weaken / strengthen / swap / other | 2 / 2 / 1 / 2 / 1 | 0 / 4 / 3 / 1 / 0 | 7 / 0 / 1 / 0 / 0 | 3 / 2 / 1 / 2 / 0 | 12 / 8 / 6 / 5 / 1 |
| edge rows named | 29 | 22 | 22 | 20 | 93 |
| flagged out of scope (rule 4) | V1.6, V1.7 (in effect) | V2.8 (as written) | – | – | 3 |
| flagged: adds prose (S40) | V1.6 | – | – | – | 1 |

- The replies' own traces: 8 variants move (E), 7 move being an explanation only, 17 neither. Computed: 6, 7, 16 (§5).
- V1.6: a condition on Acc (D6.7, S2) and a new sentence. V1.7: defines Excl(Σ), which the FROZEN D3.5 makes a declared input. V2.8: names the FROZEN L315.s7; its D16.XV part is V4.4's reading.
- No variant moves where values are placed.

## 4. The computation (rule 5)

| section | copy | run | not run | edges (the section's `.json`) |
|---|---|---|---|---|
| 1 (b77bab2) | switch `S108_S1_VARIANT` | V1.1–V1.5, V1.8 | V1.6, V1.7 (flagged; V1.7's baseline side run) | 58 rows |
| 2 (6e17160) | switch `S108_S2_VARIANT` | V2.1–V2.7 | V2.8 (flagged) | 40 rows |
| 3 (feaeed7) | switch `S108_S3_VARIANT` | V3.1–V3.8 | – | 40 rows |
| 4 (5325454) | switch `S108_S4_VARIANT` | V4.1–V4.8 | – | 44 rows |

- Each copy under its default reproduced the committed printouts byte for byte.
- Over: the 27 candidate cases of the written-in step's script (29 in section 4, with E6 and the student's copy); FC-E1–E5; CT1–CT8; generated candidates at scale 4 (section 1: SMALL 17,280, SMALL with value maps 17,280, proper targets 1,434, MID 25,920 = 61,914); the whole suite at scale 4, cap 45, under each variant; capped parts re-run at cap 300 (none hid a result).
- Dec(t) on worked and generated candidates reads histories set by hand (Θ by hand, I90), as the program's own claims do.
- Nearest statable readings, recorded as inventions (§10): V1.5, V3.6, V4.3, V4.5, V4.6; V4.7 on a toy only.

## 5. What moves the explanation definition (computed; the corrected map §2)

Being an explanation now: Account(ℰ) ∧ ¬Dec(t) (D16.XV), Account = (E) = F1 ∧ F2 ∧ A ∧ Dependence ∧ NonVacuous (D6.7).

| moves | variants |
|---|---|
| which candidates meet (E): **6** | V1.1 (D1.4, what (F1) reads); V1.5 (D3.4, ρ_p; under S108-1-I5 only); V2.1, V2.2, V2.3 (D6.4, Dependence's witness); V2.4 (D6.7, NC1 back in (E)) |
| being an explanation, (E) unchanged: **7** | V2.5 (D12.1, H = ∅); V3.4 (D13.3, under S108-3-I2 only); V3.5 (D13.8, for a trace spanning an unrecorded change of contract, in the tag encoding, or under cut K; not for a trace at o_t); V3.6 (D15.8, on S108-3-I4); V4.1, V4.2, V4.3 (D16.XV) |
| neither: **16** | V1.2, V1.3, V1.4, V1.8 (families, Prod, Ident); V2.6, V2.7 (conflict); V3.1, V3.2, V3.3 (ruling out); V3.7 (active routes); V3.8 ((EX)); V4.4, V4.5 (the (Suff), (Nec) defeat sets); V4.6, V4.7, V4.8 (𝔈_Θ, UU on a toy, (Prov)(i)) |
| not run: 3 | V1.6, V1.7, V2.8 |

**V1.1** (D1.4: Sol_N := the projection of Sol_D on V_N):
- Worked cases, Acc T → F on **15 of 27** (conjunct F1): E1 forward on C1–C3; E_rev on C_id; E_rev τ′ on C_H; M2; M5; **M13, the weathervane's mechanism**; E5 ×2; E8; E9 ×2; **the owner's two-part sign (ℰ_two, S44)**; the day-port sign. The same 15 leave Account ∧ ¬Dec(t).
- Stay: every candidate whose counterparts are J_D (E_enc, the lookups, "p because p", the one-part sign), where V1.1 and I14 agree. Every case that moves has a commitment whose counterpart is a proper subnetwork whose own relation is wider than the projection of Sol_D.
- The second checker: the vane and the two-part sign drop under V1.1 with the change read as an edit or as a boundary; E_enc on each question stays.
- Generated: in 16 / 13 / 1 / 19, out 199 / 203 / 30 / 358; most at pairs where Sol_D = ∅.
- FC-E1, FC-E4, CT1, CT2, CT5 move; suite: 21 claims move (112 / 23 / 7).
- FROZEN: blocks D4.4 (computed: sig_C({j}) ≠ sig_C(j) on 7,552 of 17,280 generated); the claim FC85 (a) fails (the identity transport c → c not faithful); D13.4, D13.5 change with it and stay readable (O5).

**Roles and kinds.** V1.2 (D2.1), V1.3 (D2.4), V1.4 (D3.3), V1.8 (D2.6): Acc and Account ∧ ¬Dec(t) move on **0** worked cases, **0** script rows, **0 of 61,914** generated candidates. They move Set_v, asg, Input, Slc, Obs, the families of signatures, Prod and Ident's contract clause; V1.2 and V1.8 block the FROZEN L347.s2 (FC09).

**One way.** Ruling out (V3.1–V3.3, V4.4), conflict (V2.6, V2.7), creation (V3.8), routes (V3.7), the class and universality (V4.5–V4.8): 0 moves of Acc and of Account ∧ ¬Dec(t) on worked cases, scripts and generated candidates. They move who has ruled what out (V3.1: Out_j 1,677 of 9,600 F → T), problems, rivalry (V2.6: 310 of 310 kind-ii pairs), conflict with a claim (V2.7: 410 of 1,822), (P) attribution, (EX) (V3.8: 7,086 of 1,929,216 valuations), 𝔈_Θ, UU (toy) and (Prov)(i). In D18.1's graph none is upstream of (E) or Dec; V3.1–V3.3, V4.4, V4.5 and V4.8 are upstream only of D16.XV's defeat conditions, (Suff) and (Nec). The map: "(E) moves only when its own reads move"; "Being an explanation moves with Dec and with D16.XV's rule, not with (E)".

## 6. The dependency map (dc3c193; corrected by the second checker, 2548f9f)

| | count |
|---|---|
| nodes | **859**: 815 template items + 10 parts of the explanation definition + 32 claims + 2 cases |
| edges | **221** (21 summary): computed 179, claimed only 31, contradicted 11; blocks 21, constrains 33, changes with 79, moves 50, independent of 38 |
| template items touched | computed 142, claimed only 26, **untouched 647** (middle untouched 473 of 577) |
| FROZEN items named by an edge | 60 of 238; blocks computed: D4.4, L307.s1, L315.s1, L317.s6, L347.s2, L375.s2, L403.s3, L495.s1 (toy only) |

- The first build had 858 nodes and 219 edges (646 untouched); the second checker's corrections give the figures above (among them e3.25c added, e1.08 and e4.19 split, e4.25 moved to the rows with no edge).
- **Gaps** (map §6): 17 middle definitions neither varied nor named; 7 of them upstream of the explanation definition: D6.9, D11.2, D11.3, D6.8, D9.1, D9.2, D5.7. 31 edges claimed only. Not computable in the program: an infinite Γ; UsesReason over circuits; 𝔈_Θ membership; (CT1), Can, Enable, UU; an argument whose premise is a computed ConfCl; an attack on (Nec) through easy to vary; Desc, BadTarget, BadReq; a recorded ρ_p. No suite claim separates D6.4 from V2.1 or V2.2. The bridge, E2, E3, E4, E7 carry no candidate.

## 7. The candidate definitions (the corrected list)

| # | variant | moves | flagged against (the owner's words in the list) | on what reading |
|---|---|---|---|---|
| C1 | V1.1 (D1.4) | (E) | **S44** | any |
| C2 | V1.5 (D3.4) | (E) | **S44; S41 Q15**; S41 Q6 not computed | S108-1-I5 only |
| C3 | V2.1 (D6.4) | (E): in only | – | – |
| C4 | V2.2 (D6.4) | (E): out only | – | – |
| C5 | V2.3 (D6.4) | (E): out only | **S41 Q15; S44** | the owner's change (wind, day) read as a boundary; as an edit nothing moves |
| C6 | V2.4 (D6.7) | (E): out only | **S45**; S44 | S45 any; S44 only with D6.3's quantifier other than 'every' |
| C7 | V2.5 (D12.1) | explanation: in | **S41 Q2**, in part | the hand-set history 'nothing tried' |
| C8 | V3.4 (D13.3) | explanation | **S41 Q2** | S108-3-I2 only |
| C9 | V3.5 (D13.8) | explanation: in | – | the trace's extent; tag encoding; cut K |
| C10 | V3.6 (D15.8) | explanation: in | – | S108-3-I4 |
| C11 | V4.1 (D16.XV) | explanation: out | **S45**; S44 | as C6 |
| C12 | V4.2 (D16.XV) | explanation: in | **S41 Q2** | any |
| C13 | V4.3 (D16.XV) | explanation: out, at transferred holdings only | – | S108-4-I3 |

- S44's case is the two-part sign (a red part for Mondays, a blue part for Tuesdays); the one-part sign is the program's companion case (O2).
- Five non-candidate variants sit against a decision, recorded for the orchestrator: V2.6 (S20), V2.7 (S27), V3.1 (S23), V3.3 (S28, S27, S41 Q23), V3.8 (S47 with S41 Q6).
- The owner's cases, as the second checker ran them (Acc; for V4.1 being an explanation with Dec F):

| case | none | V1.1 | V1.5 | V2.3 | V2.4 'every' | V4.1 'every' | V4.1 other three |
|---|---|---|---|---|---|---|---|
| vane as edit (M13) | T | F | F | T | T | T | T |
| vane as boundary | T | F | F | **F** | T | T | T |
| two-part sign as edit | T | F | F | T | T | T | **F** |
| two-part sign as boundary | T | F | F | **F** | T | T | **F** |
| one-part sign | T | T | F | T as edit, F as boundary | F | F | F |

## 8. The critical review, the orchestrator's decisions, the second checker

- **Critical review** (551007c; a fresh Opus 5.5 agent): eight reruns in the section copies agree with the files. O1 (matters): C5 drops the owner's vane and two-part sign where the change is a boundary; flag it. O2 (matters): C6, C11 named the one-part sign as S44's case. O3 (matters): e3.25a "contradicted" holds only for a trace at o_t. O4 (matters): e4.29 shows no move; L538.s2 not met by E5. O5–O13 minor (edge kinds and standings against their own evidence; C2's S41 Q6; the untouched definitions upstream of the explanation definition; unlisted gaps; V3.6's history). A second round needed.
- **The orchestrator** (8e8179e): (1) all 13 to one second checker; (2) the L538.s2 finding recorded for later, not fixed in Part A; (3) V1.6's formula, without its sentence, to round 2 for section 2; V1.7, and V2.8's part on L315.s7, to Part B; V2.8's D16.XV part is V4.4, not implemented again; (4) a second round of Part A, four GLM agents, the same template, aimed at the readings the candidates rest on, the seven untouched upstream definitions, the edges claimed only; (5) round 2's whole-suite runs to the Sonnet harness; (6) a plain-words file after the second checker.
- **Second checker** (2548f9f; a fresh Opus 5.5 agent): O1, O2, O4–O13 the review's fix; O3 a third fix: with the output's construction trace spanning an unrecorded change of contract, V3.5 moves Dec T → F on 45,072 of 90,144 held-output chains (n ≤ 4, cuts T′ and T); 0 for a trace at o_t. The map rebuilt by `s108_map_build_second_checker.py`; the list corrected. Section files left as they are, with four wordings the map no longer uses (section 4's "the owner's one-part sign (S44)"; section 1's "D13.4's reflexivity"; section 3's S108-3-I4 history and its V3.5 "contradicted").

## 9. A finding about the theory after round 4 (O4; the orchestrator's decision 2)

- L538: "**(Nec) Necessity.** A candidate such that an argument not using (E) rules out the claim that it is a non-explanation, whose organization no transport can preserve under any contract on its target. Eliminative explanation (Part VII) is the exposed case."
- Acc ⇒ F1 ∧ F2 = Faithful_C(t), so no candidate meeting (E) is exposed (C′ = C, t′ = t witness it); FC62 has E5 meet (E). So L538.s2 is not met by E5's encodings, off and on alike (section 4, E4.5c).
- On one reading ("the exposed case" names only a kind (Nec) must answer) the finding narrows (the review's §4). Recorded for the paused review rounds; not changed in Part A.

## 10. Inventions (S36), all recorded in the section files, none applied to the theory

- Section 1: S108-1-I1 (ℰ_bv at a ≠ 1), I2 (generator encodings follow V1.1 in the suite, fixed in the worlds), I4 (b0 where a helper has none), I5 (a question with no recorded contract history is declared).
- Section 2: P-S2-1 to P-S2-6 (where the variant replaces the definition; V2.7's deleted disjunct False; the four hand-set histories; L311 not built; L307, L309 realizations; kinds of difference).
- Section 3: S108-3-I1 to I6 (ExplUse's Acc on cases with no ℰ; CT reading ExplUse; the parts clause; parts and stated construction; the claim used on the widest contract; circuits enumerated).
- Section 4: S108-4-I1 to I9 (Slot under 'every'; (Suff)'s shapes; Sel ∨ CT at the holding; the rival's Acc as given; the class of transports searched; the designation of Q; V4.7's toy; "a function of (𝒯,H)"; hand-set provenance).
- The second checker: the output's trace over o_s..o_t (O3), one encoding of several.

## 11. The owner's words during the round; the Sonnet 5.5 trial

- **S53** (e3c2119), while Part A's reading ran: "Ok. Try Sonnet 5.5 and then review it's output. Sonnet 5.5 got a massive boost artificial analysis intelligence index, now only 2 points behind Opus 5.5 vs 20 points before".
- The trial runs separately, on section 2 (`S108 Part A - Sonnet 5.5 trial/`; snapshots eda455c, 0333043, 940e289). Not opened here; nothing in this record rests on it. Whether it changes who computes in round 2 is decided when its review is in (the orchestrator's decision 5).
- No owner question arose; S52's yes or no comes after Part B.

## 12. Departures

- **The whole-suite runs** were made by the computing agents' own scripts, not by Sonnet workers through the harness as the rule assigned: a subagent cannot start another agent. The off runs matched the committed printouts; the review's eight reruns agree. Round 2's go to the harness (decision 5).
- **Load.** Suites ran beside other sections' on four CPUs; parts that reached the 45 s cap were re-run at cap 300, where each matched the default's result (FC23.new1 (c)'s "no witness found" at cap 45 was the cap).
- **Section 3's first suites** under V3.1, V3.2, V3.3 and V3.5 were made before two fixes to the copy's own code (FC84.new2's own encodings of D13.8's record clause had not been switched with V3.5; FC90.new1's note printed under every variant); they were replaced by second runs.
- **The plain file's name.** The rule names `plain words/108 Part A - what the variations found, in plain words.md`; it is written as `… Part A round 1 …`, since a second round follows.
- **The frozen set** went to the agents as Claude's reading; the rule's note that the orchestrator shows it to the owner before the launch has no answer in the record.

## 13. Not tested, and unsure

- The frozen set is Claude's reading, not the owner's.
- C2 rests wholly on S108-1-I5, C8 on S108-3-I2; C5's flag on reading the owner's changes as boundaries; C6's and C11's S44 on D6.3's quantifier; C7, C9, C10, C12, C13 on hand-set histories, whose counts equal the population meeting (E) by construction of the history.
- The program tries small candidates only; generated "smallest witnesses" are the first found in ascending size.
- Each section computed by one agent; the review's objections ruled by one checker.
- 647 of 815 items untouched; silence is not agreement (rule 3). 31 edges rest on argument alone.
- V1.6, V1.7, V2.8 not run.
- No outside reader has seen the computations; the GLM replies' traces were claims until computed.
- The everyday cases were not read.

## 14. What follows

- Round 2 of Part A (the orchestrator's decision 4), under its own rule, written and committed before sending; aimed at the gaps in the review's order (§8).
- Then Part B: V1.7 and V2.8's part on L315.s7 go there.
- Then Claude flags the candidates the two parts find that "don't appear to fit decisions I've made in the past", and the owner answers each yes or no. Then stop (S52).

## Files

- The instruction: decision S52 in `records/Semantics - Decisions.md`.
- `results/S108 Part A - the frozen set.md`, `.json`; `plain words/108 Part A - the frozen parts, in plain words.md`.
- `results/S108 Part A - the frozen template.md`; `results/S108 Part A - how the replies will be read, written before sending.md`; `results/S108 Part A - material for the readers/`; `results/S108 Part A - returns/`.
- `results/S108 Part A - tabulation of the replies, before any ruling.md`.
- `results/S108 Part A - section 1 - variants computed.md` to `section 4`, each with its `.json`; the copies and runs in `results/S108 Part A - computation/`.
- `results/S108 Part A - the dependency map.md`, `.json` (corrected); `results/S108 Part A - candidate definitions of explanation.md` (corrected).
- `results/S108 Part A - critical review.md`; `results/S108 Part A - the orchestrator's decisions on the critical review.md`; `results/S108 Part A - the second checker on the critical review.md`.
- For the owner: `plain words/108 Part A round 1 - what the variations found, in plain words.md`.
