# S106 — the written-in test taken out: report

*28 September 2026. A fresh Opus 5.5 agent, under decisions S44 and S45 (read with S20–S45 whole; S40: maths and code, no new prose; S20, S21, S23: no grade, no ranking, no record of rivals; S33, S34: what hard to vary covers is parked; S41 never reversed or weakened; S43: LLMs are not part of the semantics). Input: `tests/105 The semantics, standing alone, after round 3.md` (md5 da9a30cd052d46f2a5ead259cea97d3c, not written) and `results/S105 Round 3 - maths after the reading/` (not written). Every run: PYTHONHASHSEED=0, `-B`, under `timeout`. Nothing written outside `Semantics/`. Nothing is settled (S28).*

## 1. The map: every use of "the answer is written in"

Kept or removed, one line each. "Text" lines are of text 105 (line numbers as in texts 103–106).

| # | where | what it does | kept / removed | why |
|---|---|---|---|---|
| M1 | L255 heading "Non-circular dependence"; D6.5's name | names the condition by the test | renamed Dependence (formal name; S106-T1; I188) | "non-circular" is the test; what stays checks dependence |
| M2 | L255 s1, NC0 (D6.2) "evaluating E under its independent boundary conditions" | none: holds of every candidate (FC108) | kept; "independent" deleted (S106-T2; I187) | vacuous as I23 reads it; its only other reading (I23 (a)) is the test on a boundary |
| M3 | L255 s2–s3, NC1 (D6.3): the answer not an unanalysed input or component, "structural at the declared grain" | the written-in test itself | **removed from (E)** (D6.5, D6.7; S106-T3); Slot and NC1 kept as defined notions (D6.3), content for criticism (D6.11) | only expresses "the answer is written in" |
| M4 | L255 s4, NC2 (D6.4) | the answer depends on the commitments at all: a contrast lost when a block of Γ is deleted | **kept** as Dependence (D6.5) | not the test: written-in candidates meet it where their answer varies (FC23 (b), (e); the sign, FC23.new2); it fails a mechanism and a lookup alike on a contract with no contrast (FC21, FC22, FC29) |
| M5 | L257 relabelings / "excluding every change … could matter" admit no candidate (FC21) | holds through NC2 | kept; name only (S106-T4) | NC2's, not the test's |
| M6 | L262 (E) | NonCircular a conjunct | conjunct now Dependence (S106-T5) | the test out of (E) |
| M7 | L269 tables | E_tab fails (F1); E_enc "is an account when it meets the other conjuncts" | kept, unchanged | E_tab fails (F1), not the test; E_enc's sentence stays true and now holds (FC25.new2) |
| M8 | L271, L325 reversed calculation | fails (F2): direction of production | kept | (F2)'s homomorphism clause excludes it even under Mimo's τ', where NC1 also failed (FC27) |
| M9 | L273 "p because p" fails; a restating component; packaging does not repair | the test's stated result | **removed**; replaced by \(\operatorname{Slot}_C(\mathcal E,k)\not\Rightarrow\neg\operatorname{Account}(\mathcal E)\) (S106-T6) | states the old result |
| M10 | L275 a contrast no admitted edit realizes | NC2 (FC29) | kept; name only (S106-T7) | NC2's |
| M11 | L317 a problem solved with no test by finding a rival "assumes its own answer" | the test as a ground for ruling out (E) | **removed** (S106-T8) | that finding no longer rules out (E) |
| M12 | L331 "Set b_B = 0 because it gives the mass I favour … is circular" | an inference that assumes its conclusion | kept | about arguments; (E) never registered it (FC60 (a)); Part IX's block does (D9.7) |
| M13 | L339 "a bare denial … is not an account" | no component responds to the change | kept | (F1) / Dependence, not the test |
| M14 | L343 skew matrices "Non-circular dependence is met" | NC2's contrasts | kept; name only (S106-T9) | NC2's |
| M15 | L397 an argument with no test that finds a candidate "assumes its own answer" rules it out | the test as a ground for ruling out (E) | **removed** (S106-T10) | as M11 |
| M16 | L397 "read structurally as non-circular dependence reads identity (Part V)" | pointer to NC1's structural identity | pointer → "(D9.7)" (S106-T11) | its target is deleted; the block's reading is D9.7's own (I39) |
| M17 | L397 block: a premise that is the claim's denial; "as in 'p because p'" | about ruling a claim out | kept | not about what makes an explanation (FC72) |
| M18 | L520 Part XIV (E) | NonCircular | Dependence (S106-T12) | as M6 |
| M19 | L536 (Suff) "conclusion-as-premise fails non-circular dependence" | the test's stated result | **removed** (S106-T13); the table clause kept | states the old result |
| M20 | L277, L313 "(E) has no condition on how guessed / that each commitment do work" | unaffected | kept | no test in them |
| M21 | Part XV (Nec), (Elim), (Prov), (QF); Part XVI Arguments 1–10 | none uses NC1 | kept | Argument 8 keeps (E) after S106 (FC100 H); Argument 10's S1 meets (E) under both (E)s (E9 rows below) |
| M22 | formal core D9.10 (K1), D14.7 (EX), D16.4 (𝔈_Θ), D7 routes, D8–D10 | built on Acc | kept; follow (E) | a written-in criticism connection now has bearing (FC107) |
| M23 | D18.1; the program's DEP | NonCircular → ℓ | Dependence → (O), (Q), C, δ; Slot, Open nodes | only NC1 read the grain (I28) |
| M24 | program: `core.slot`, `NC1`, `SLOT_QUANTIFIER`; `core.account` | NC1 a conjunct | slot/NC1 kept, read by no conjunct; account's conjuncts F1, F2, A, Dep, NonVacuous | as M3 |

No owner question arose: every row is settled by S44, S45 or by a computation (`owner questions after S106.md` §C).

## 2. Formal changes, old → new (`formal core, after S106.md`, 19 [S106] marks)

| def | old | new |
|---|---|---|
| D6.5 | Non-circular dependence: NonCircular :⟺ NC0 ∧ NC1 ∧ NC2 | Dependence :⟺ NC0 ∧ NC2 (⟺ NC2) |
| D6.7 | Acc :⟺ F1 ∧ F2 ∧ A ∧ NonCircular ∧ NonVacuous; arguments with ℓ | Acc :⟺ F1 ∧ F2 ∧ A ∧ Dependence ∧ NonVacuous; no grain; round 3's (E) = Acc ∧ NC1 |
| D6.8 | heading "Non-circular dependence" | "Dependence" |
| D6.11 | — | new: Pin(ℰ,k;a,b); the further question at k, p^k (query: λ(k)'s relation); LeavesOpen(ℰ,p') :⟺ every pair of C' t translates is a relabeling for p' (D6.9) |
| D18.1 | NonCircular → (O), (Q), C, ℓ, δ | Dependence → (O), (Q), C, δ; Slot (D6.3), Open (D6.11) nodes |
| notes | — | D6.2, D6.3 (Slot kept; R3-Q1 answered), D6.10 (E_enc), D9.7, D9.10, D10.6, D16.XV, §6, §9 Vague, §18 item 2 |

## 3. Code changes (`model after S106/`, copied from round 3's)

- `core.py`: `dep()` (Dependence); `account(reading=)`: "S106" (default; conjuncts F1, F2, A, Dep, NonVacuous; NC1 reported, not a conjunct) or "r3" (round 3's); env `S106_ACCOUNT_READING`; D6.11: `pin`, `pins`, `RelQuery`, `further_question`, `leaves_open`.
- `claims_a.py`: FC14 reads this folder's core first; FC21 (d) without NC1; FC23 (c) restated, (e) new; FC24, FC26, FC27, FC33 texts; FC32 (Dep edges, no ℓ); `_acc_with(…, account_reading)`.
- `claims_b.py`: DEP "NC" → "Dep" (no ℓ), "Slot", "Open"; D_TO_NODE (D6.3 → Slot, D6.11 → Open); FC60, FC107, FC108 texts.
- `claims_r3a2.py`: FC23.new1's `acc_q` reads Acc ∧ NC1_q (round 3's (E)), parts relabelled, (h) added; `elim` at module level.
- `claims_r3a3.py`: FC32.new1 reads this folder's core first. `run.py`: registers `claims_s106.py` (new: FC23.new2, FC23.new3, FC25.new2). New script `s106_cases.py`.

## 4. Runs (scale 4, cap 45 s; `S106 - runs.txt`, `S106 - whole suite, printout.txt`)

| run | result |
|---|---|
| round 3's model, rerun here (read only) | 125 H, 2 CEX, 7 NT of 134 (514.6 s) |
| the copy with `S106_ACCOUNT_READING=r3` | printout identical to round 3's, part by part (0 lines differ, the added "Dep" key aside) |
| the copy, (E) after S106, claims as round 3 left them (the raw effect) | 124 H, 3 CEX, 7 NT: FC23.new1 H → CEX ((a), (g) not as claimed; (c), (d), (f) no witness: (E) no longer varies with the quantifier); FC23 (c) not as claimed (FC23 CEX already, by (b)); FC107's Acc False → True; FC34, FC74 other witnesses; FC37, FC46, FC51 more hypotheses met; nothing else |
| **the copy after S106 (final)** | **128 H, 2 CEX, 7 NT of 137** (533.9 s; no traceback): every earlier claim's status as round 3; parts changed only where restated (FC23 (d) relabelled, (e) new; FC23.new1 (a)–(g) relabelled, (h) ×2 new; FC32 (2) relabelled), all as claimed; hypotheses met: FC37 120 → 1661, FC46 66 → 962, FC51 15 → 265 (more candidates meet (E)); FC34, FC74 other first witnesses; FC14 reads this core (119 definition lines), FC32.new1 its 115 paragraphs, all mapped (DEP 84 nodes) |
| `s104_external.py` (FC-E1–FC-E5) | identical to round 3's printout (md5 86a67664a9a3584351fd4836a4140b69): NC1 holds in every example, nothing moves |
| `s104_creative_transport.py` (CT1–CT8) | identical (md5 d473944e74d2f349b1fdfb83277843cf); CT2's pairs meeting (E) still 2 of 256 |
| `s106_cases.py` | 28 rows; 9 move; 5 move under another reading only (§5) |

Changes against 125 / 2 / 7 of 134: three new claims (FC23.new2, FC23.new3, FC25.new2), each H. No earlier claim changed status. FC23 stays CEX (its (b) as stated, the claim's own wording, U3); FC63 stays CEX (I99). FC23.new1 would have become CEX had it kept reading (E); it is restated (§ `formal claims, after S106.md`) to read round 3's (E) as Acc ∧ NC1_q, content, with (h): (E) after S106 is the same under all four readings.

## 5. The cases that moved (`s106_cases.py`; round 3's (E) under 'every' → after S106)

| case | line / claim | round 3 (every, some, some-exempt, some-exempt-set) | after S106 |
|---|---|---|---|
| encoding table E_enc, pole C1 and C2 | L269; FC25.new2 | F,F,F,F | **T** |
| "p because p": the pole's L written into one component | L273; FC23 | F,F,F,F | **T** |
| M1, M2, M3 (the readers' lookups) | FC23 (c) | F,F,F,F | **T** |
| the hand-turned vane ("north when turned") | R3-Q1 | F,F,T,T | **T** |
| E8: the criticism question p_δ, identity candidate (a slot) | L590, L377; FC107 | F,F,F,F | **T** |
| the owner's shop sign, one part | S44; FC23.new2 (b) | F,F,F,F | **T** |
| moved under another reading only: the pole's forward organization on C2, C3; M5; the eliminative construction (FC62's encoding); **the owner's two-part sign** | FC26, FC23.new1, FC62, FC23.new2 (a) | T,F,…  | T under all |

Unchanged (14): the pole on C1; the reversed calculation (production: fails (F2); identification: meets (E)); E_tab (fails (F1)); the relabeling contract (fails (F2)); the weathervane M13; the second eliminative encoding; E9's S1 (t1 and t1∘ψ); E6 (fibre-free query, no slot); the palette sign; D⁺ on p^r. E2, E3, E4, E7 and Part VI's route examples compute no candidate's (E). Every text sentence that stated an old result is changed: L255, L273, L317, L397, L536 (§6); L269's sentence stays true.

The owner's shop sign (FC23.new2): the two-part candidate meets (E) under every reading; its red part pins the answer on Mondays, its blue part on Tuesdays (D6.11 (a)); the further question "why is the red part there in the first place?" is p^r on D⁺, where the shop owner's choice puts the part there, contrasted with "the owner decides otherwise": both sign candidates leave it open (D6.11 (c)), and D⁺'s own organization meets (E) on it. At each pin, the answer is read off the further question's answer (D6.11 (b)).

## 6. Text changes (`text changes for S106.json` → `tests/106 The semantics, standing alone, without the written-in test.md`)

13 changes on 10 lines, none refused: delete 5 (T2, T3, T8, T10, T13), formal 7 (T1, T4, T5, T6, T7, T9, T12), pointer 1 (T11). Input md5 checked; each span unique on its line; each applied span equal to its entry byte for byte; undoing each gives the input line back; line count kept (632). S95 residue scan: 80 → 80 hits, 0 new, 0 of S23's list anywhere. S96 physical scan: 196 → 196, 0 new. Headings 55, defined terms 154, labelled formulas 23: none missing; one term replaced on purpose by its formal name (L255, "Non-circular dependence."), which `apply text changes.py` now checks. L255 no longer held.

## 7. Word counts

Words outside formulas: **15,322 → 15,203 (−119)**; all words 16,221 → 16,104 (−117). No single change adds a word outside formulas.

## 8. New inventions (`inventions register - addendum after S106.md`)

I184 Pin; I185 the further question at a part (query: λ(k)'s relation); I186 LeavesOpen via relabelings; I187 L255's "independent" read as the test and deleted; I188 the name Dependence; I189 the sign's encodings. Changed standing: I24 (its other choice (a) taken), I25, I28 (the grain out of (E)), I136 and I176 (read Slot only), I23 (other choice closed), I39 (D9.7 alone).

## 9. Owner questions

None new (`owner questions after S106.md`). R3-Q1 is answered (S44, S45).

## 10. Parked

P1–P7 untouched. P8 new: "Why blue and not any other colour?" and "bad … through the questions it leaves open" touch what hard to vary covers: parked; D6.11 builds only questions whose contrast is a part there or not there, never a count or grade (`parked after S106.md`).

## 11. Moves (round 3's rule 16, strictly)

| # | move | kind |
|---|---|---|
| 1 | D6.5: Dependence := NC0 ∧ NC2 (NC1 out of (E)) | changed definition |
| 2 | D6.11: a pin, the further question, LeavesOpen | new definition |
| 3–15 | S106-T1 … T13 | text changes applied |

**Moves: 15.** The ground is the owner's decision (S45), not a finding. Not counted: D6.7, D6.8, D18.1 and the program's DEP and `account` (re-based on row 1: the one fix in its other places; 17 if D6.7 and D18.1 were counted apart); restated or re-based claims FC21, FC23, FC23.new1, FC24, FC30, FC31, FC32, FC34, FC108 (statement follows row 1, status unchanged); notes FC26, FC27, FC33, FC60, FC100, FC107; new test claims FC23.new2, FC23.new3, FC25.new2, FC23 (e), FC23.new1 (h); `s106_cases.py`; I184–I189; P8.

## 12. The new text

`tests/106 The semantics, standing alone, without the written-in test.md`: md5 **0e56b581a4b5f3c7a9e19bdceb4d8cb3**.

## 13. What is unsure

- D6.11 (I185, I186) is one way to write "the questions it leaves open" with the theory's own notions; other ways are recorded. It asks nothing of an agent, and grades nothing; whether it is the right content for criticism is open.
- The rename (I188): the heading now reads \(\operatorname{Dependence}\) in formula type; the kinds S40 allows gave no plain-word rename.
- Deleting "independent" (I187) rests on its two readings being vacuous or the test.
- (K1): a criticism whose connection writes its defect in now has bearing (FC107). (Suff): candidates with a slot are now in its range. Both follow from S45's "everywhere"; neither was asked about.
- S47 (the bridge; "and criticism" back into L13), recorded while this work ran, is not in text 106: it was not this task's. Text 106 is text 105 with S106's changes only.
- S48 (a plain-words file for every round, S106 included), recorded while this work ran: not written here; the records and plain files are the other agent's.
- FC23's CEX (its (b) as stated) and FC26's look "not as expected" are round 3's, unchanged.

## 14. Files written (md5)

| file | md5 |
|---|---|
| `tests/106 The semantics, standing alone, without the written-in test.md` | 0e56b581a4b5f3c7a9e19bdceb4d8cb3 |
| `formal core, after S106.md` | bcedecc8b98e75fe7b127702a589ab81 |
| `formal claims, after S106.md` / `.json` (built by `build formal claims after S106.py`) | 72a9806787ff47128eeeed8868a833e5 / 3d225297a9ea6179365debab0eab9b44 |
| `inventions register - addendum after S106.md` | daa17b946060094f6658091edb259300 |
| `owner questions after S106.md`, `parked after S106.md` | 2976cfbb463a63894e4d796a552b624f, d9053b6b5010895eef2504eabedd95ae |
| `text changes for S106.json`, `apply text changes.py` | 7db0fc5e136921a65b61a48d9eb858f2, 3b5ed14e52671072cfbdf7391d3f675e |
| `S106 - runs.txt`, `S106 - whole suite, printout.txt` | 16fb72dbc5b3570a4d9bdf898748d12a, a3cf40840ec4a0e9fc8f087f11cfe41d |
| `model after S106/` (core.py; claims_s106.py; s106_cases.py) | 964030de3cb4756e60aa61fdfe3aad78; 0ca6f373f3de5c8a84c9f7d0e4a0e9ef; 7e4212128446972d45cc6710ae24c528 |

