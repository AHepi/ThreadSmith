# S107: Round 4 — tabulation of the replies, before any ruling

*Written by the tabulating agent of rule 4 (a fresh Opus 5.5 agent that built nothing of this round and had read no reply when this file was created), 28 September 2026. Created at once, filled as it goes (lesson S28). Rules on nothing: "fails" says what a reply claims, not whether it holds. No Sonnet agent took part (S46). No theory text, rule, addendum, reply, decision or committed file of an earlier round or step was written. Obeys S23 except where it quotes; says "candidate" or "explanation", never "model", for what the theory judges (S43); "model" here means only a small structure the program builds, or the program's folder.*

## 0. Counts per area (rule 5, lesson S36)

Counted by program (scratchpad `s107tab/count.py`) from the tables of §3, before any checker starts. K1 (the winter-myth knock-on) is counted as an item of area 3 (addendum 1).

| area | lines | findings | N answers among them | with a proposed change (maths, code or text) | text proposals | S40 flags | S41 flags | S44/45 flags | S47 flags / checks | other items | **area total** | ties and choices (§1, §7) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | L1–L228 (Parts 0–IV) | 15 | 8 (N2, N6 ×4) | 9 | 1 (old span not in the text) | 0 | 0 | 0 | 0 / 2 (B11, S-N6) | — | **15** | — |
| 2 | L229–L372 (Parts V–VIII) | 20 | 8 (N1, N5 ×4) | 12 | 2 | 2 (B4, C-K1) | 0 | 0 | 0 / 0 | — | **20** | C-K3 |
| 3 | L373–L632 (Parts IX–XVI) | 24 | 8 (N3, N4 ×4) | 9 | 0 | 0 | 0 | 0 | 0 / 0 | K1 (the winter-myth knock-on) | **25** | S2, S-d, S-κ, S-f |
| all | | **59** | 24 | 30 | 3 | 2 | 0 | 0 | 0 / 2 | 1 | **60** | 5 |

| job | findings | area 1 | area 2 | area 3 |
|---|---|---|---|---|
| 1 breaker | 13 | 2 | 7 | 4 |
| 2 maths_words | 21 | 8 | 5 | 8 |
| 3 structure | 15 | 2 | 3 | 10 |
| 4 cases | 10 | 3 | 5 | 2 |
| item K1 (addendum) | 1 | — | — | 1 |

No proposal is flagged under S41, S44/S45 or S47. Two are marked **check** under rule 11's second limb (B11, S-N6): each writes the bridge's NoBriefQuestion as no criticism aimed at the brief. Two text proposals put a word outside formulas into L271 (S40): B4 and C-K1, "on" for "under". One text proposal's old span is not in the text under review (C-K2 at L199, §2). Points that several findings share: §6.

## 1. How made

- Read first, whole: the rule (`results/S107 Round 4 - how the replies will be read, written before sending.md`) and its addendum (`… addendum to the reading rule, the winter-myth knock-on, written before any reply was opened.md`); decisions S20–S48 (`records/Semantics - Decisions.md`, md5 33561d7f15ef470cbd68d2efcb0b522d, the rule's).
- Replies: the four `.response.txt` only, in `results/S107 Round 4 - returns/` (no receipt, reasoning, request, attempt, stream or guard file opened). All four end with END OF REPORT. Reply lines cited as r*n*.

| job | tag | md5 of the reply | lines | words |
|---|---|---|---|---|
| 1 breaker | `s107_glm_breaker` | 6f09f6c50fdc3464a7227a1e4c88c64b | 108 | 2,698 |
| 2 maths against the words | `s107_glm_maths_words` | 12267e61b686bfa50c1597d2b09171fc | 110 | 2,140 |
| 3 structure | `s107_glm_structure` | b5446cf8efaf963b44b49e58c291fb0d | 122 | 2,000 |
| 4 cases | `s107_glm_cases` | 4685c10892711d6f410fee7008360432 | 177 | 2,944 |

- Text under review: `tests/106 The semantics, standing alone, without the written-in test.md`, md5 c7af964c329ab7959243405d394e6574 (checked), 632 lines. Maths: `results/S106 The written-in test taken out/formal core, after S106.md` (40d7c80ec78574794962fece34a4cb51, checked), `formal claims, after S106.md` (c0884083daae9b95be0c36d111d71019, checked), the program `model after S106/model/`.
- The replies cite sandbox paths. By the sandbox manifest (7ef114056251fddb8daf1ed52635820e): `maths/formal core, now.md` = the formal core after S106; `model/` = `model after S106/model/`; `program printouts/…` = the build's printouts in `results/S107 Round 4 - material for the readers/`; `the step/report.md` = `S106 report.md`.
- **Finding** = a point a reply says fails, departs (maths says more / less / other than the words), or proposes a change for, whatever the reply's own label; each reply's answer to N1–N6 is a finding (rule 11 sends N1–N6 "like findings"). Where a reply's own finding is its N answer (it says so), the two are one row. Points a reply marks held, same, clean or agreeing are listed in §5, not counted (silence and agreement are not rulings, rule 3).
- **Ids**: the reply's own, prefixed: B- breaker, W- maths_words, S- structure, C- cases (the breaker's B*n* kept bare). The cases reply's own K1–K4, K6 are written **C-K1 … C-K6**, and the addendum's item is **K1 (the winter-myth knock-on)**, §3.5; the text's (K1) is the bearing condition. Unlabelled points get a letter of their section (W-b, S-d, S-δ, S-κ, S-f).
- **Lines it bears on** (rule 5): the text lines the finding names; a line cited only as the ground for saying the text is not at fault is not counted (marked). **Maths alone** (no line named): the lines its definition or claim formalizes: D6.2, D6.3, D6.5 L255; FC23 L273 (it is cited there), L255; D6.9 L257; D7.4 L302; D9.10 L377; D11.3 L375; D12.2 L197; D12.3 L199; D13.3 L405; D14.7 L447–L449; D16.XV L536–L544 ((Suff) L536, (Nec) L538, (Elim) L540); D18.1, FC14, FC32.new1 L526; D0.2 L31, L520–L522, L596; D5.1 L231. **N1–N6** go where rule 11 sends them: N2 (L61) and N6 (L13, L55) area 1; N1 (D7.4, L302) and N5 (L255) area 2; N3 (D9.10, L385) and N4 (L536) area 3. **Tie**: the area of the line of the definition the proposal changes (else the one attacked), as round 3; every tie and choice is marked. Area 1 L1–L228, area 2 L229–L372, area 3 L373–L632.
- **K1 (the winter-myth knock-on)** is an item like a finding (addendum 1): L317 [2] and L397 [3], so area 3; any reply's point on L317 or L397 goes with it (§3.5).
- **Form**: maths; code; or text: delete / formula (span replaced by its formal statement) / pointer; register (an invention recorded, not a move, rule 16); none.
- **Flags** (rule 4): **S40** a text proposal whose new span has words outside formulas and pointers that the old span lacks (counted by program, §2); **S41** a proposal that would reverse or weaken Q2, Q6 (with S47), Q15 or Q23; **S44/45** one that would put the written-in test back into what makes something an explanation, by any name; **S47** one that would have the maths ask for a criticism event, or (rule 11) read the bridge as having had no criticism where only no question about the brief occurred to the agent. "FLAG" is the mechanical mark; "check" marks a proposal whose words come near a flag and which the checker should look at; "note" says what an owner's answer it bears on, with no flag.
- **Inventions**: the I-numbers the finding rests on, as the reply names them; "new, unnumbered" where the reply asks for one (rule 6 numbers them after I191 at integration, §7).
- **Run?**: as the reply reports it; "**not run**" marks every computation the reply marks not run, or gives as expected output only (rule 3: the checker runs it before ruling).
- Tools: the harness's `tabulation.py quote` for the look-ups of §2 (rule 4 allows it); a word count in the scratchpad (`s107tab/prose.py`) for the S40 column. No harness job was named for this step (§7).

## 2. Quotations and text proposals compared (rule 15)

**Text proposals** (old span searched byte for byte in the cited line and the whole text; words outside `\(…\)` formulas and pointers such as `(F2)`, `(E1, FC27)`, `(D12.3)` counted, old → new; "new words" = words of the new span the old span lacks).

| id | line | kind | old span | words old → new | new words | S40 |
|---|---|---|---|---|---|---|
| B4 | L271 | formula / pointer (the reply: "kind 2/3") | found once, L271 (with ":"; the same words end in "." at L536) | 5 → 5 | on | FLAG ("on" for "under") |
| C-K1 (T1) | L271 | formula | found once, L271 (as B4) | 5 → 2 | on | FLAG ("on" for "under") |
| C-K2 (T2) | L199 | formula | **not in the text under review**: its first sentence ("The transport is entered into …") is nowhere in the text; its second, "Write \(\operatorname{Dec}(t)\).", is in L199, which reads "**Declared.** Neither of the above. Write \(\operatorname{Dec}(t)\)." Round 3's tabulation found the first sentence in the round-1 text (tests/103) L199, removed in round 2 (T10) | 11 → 0 | — | not counted (old span not found) |

**Quotations the findings rest on**

| quotation (as the reply gives it) | by | cited | result |
|---|---|---|---|
| "fails (F2) under the production contract" | B4, C-K1 | L271 | found L271 and L536 |
| "The transport is entered into the model by its author" (round-1 wording, where "model" is L13's "whoever writes the model down", not a candidate) | C-K2 | L199 | **not in the text under review** (above) |
| "exactly one of three" | C-K2 | L193 | found L193 |
| "The answer follows by evaluating E under its boundary conditions" | B2 | L255 | found L255 (E as \(E\)) |
| NC0 "holds of every candidate" | B2 | D6.2 | found (formal core D6.2) |
| "an account when it meets the other conjuncts" | B (a), W (c) | L269 | found L269 |
| "read structurally (D9.7)" | B6 | L397 | found L397 |
| "has its conclusion among its premises, as in 'p because p'" | S (a) | L397 | found L397 |
| "not a fifth condition" | B (f) | L343 | found L343 |
| "all four conditions of (E)"; "which of the four" | B (f), C-N4, W-N4 | L536 | found L536 |
| "an episode of conjecture and criticism"; " and criticism" | B13, B (f), W (b), W-b | L13 | "conjecture and criticism" found L13 ("produced by an episode of conjecture and criticism") |
| "An argument not using (E)" | W5 | D16.XV, (Suff) | found L536 and L538 |
| "admits no candidate that meets non-circular dependence" | W4 | D6.9's quote | found in the formal core (D6.9's quoted span); not in the text: L257 has "admits no candidate that meets (F2), (A) and \(\operatorname{Dependence}\) (FC21)" |
| "a criticism occurrence can exist when (K1) fails" | C-N3 (NC5) | L383 | found L383 |
| "The expansion is an account" | C-E6 | L343 | found L343 |
| "not an account" (the bare denial) | B7, C (a) | L339 | found L339 ("is not an account of it") |
| "circular" kept at L331, L397; "written in" at L407; no "slot", "unanalysed", "conclusion-as-premise", "assumes its own" | W residue scan, S (a) | whole text | as the replies say (grep, case-insensitive: "circular" 2 lines, "written in" 1, the four others 0) |
| "Held(o', x) for some o' ⪯ o_t of h'"; "Prepares(h', o, c) ∧ Held_ℓ(o, c) ∧ ExplUse(o, c)"; "Con → CT, Episode" | S2 | D12.2, D13.3, D18.1 | found in the formal core |
| `DEP["Con"] = ["h","CT","Episode",("<","(R)")]`; `DEP["Build"] = […, "ExplUse", ("<","(R)")]` | S2 | `claims_b.py` | found in `DEP` (claims_b.py L2556, L2563; `DEP` opens at L2530; `DEP_R2` at L2514 is round 2's, kept for comparison) |
| "Slot_C(ℰ,k) ⟺ Det_C ≠ ∅ ∧ Pin … at every (a,b) ∈ Det_C" | S3 | D6.3 | found (formal core D6.3: "Det_C ≠ ∅ ∧ Pin", "at every (a,b) ∈ Det_C") |
| "a subhistory is a subset closed under the interpretation, with ≺ restricted" | S4 | D11.3 | found |
| "c = (z, δ, g, Conn, occ)"; "ℰ_c := (Conn, …, δ_c)" | S-δ | D9.10 | found; the core has "ℰ_c := (Conn, Qf(z,δ,p), t_c, Γ_c, δ_c)" (the reply elides the middle) |
| "a kind-label κ(ℰ) ≠ κ(ℰ')" | S-κ | D16.XV (Elim) | found |
| NoBriefQuestion "defined nowhere in the core" | S-N6 (S5) | — | 0 hits for "NoBriefQuestion" in the formal core; 1 line in the formal claims (FC84.new1) |
| "an episode in which no question about the brief occurred to the agent as worth investigating" | B11 | FC84.new1 (a1) | found in the formal claims after S106 |
| "because the agent asked" ([S47] note) | B12 | D14.7 | found in the formal core |
| "a criticism (D9.10) of it, and a response that uses the criticism as a reason" | B12 | CompleteCritical | found in the formal core |
| "written-in candidates meet it where their answer varies (FC23 (b), (e))" | B15 | S106 report §1 M4 | found in `S106 report.md`'s M4 row; the parenthesis continues "; the sign, FC23.new2)" |
| "it sounds like you're making a stronger claim than 'no questions occured to the agent'" | B11 | S47 | found (S47; "but" before it, double quotes inside) |
| "the maths doesn't ask for anything" (B13); "the math doesn't ask for anything" (C-N6) | B13, C-N6 | S47 | S47 has "The math doesn't ask for anything." (B13 writes "maths") |
| "In either case, it is an explanation. Just not a good one" | B1 | S44 | found S44 |
| "No, not if just declared" | B1 | S41 | found S41 |

## 3. Findings

### 3.1 Job 1, the breaker (`s107_glm_breaker`), 13 findings

Runs the reply reports (r3): the whole suite, `python3 -m model.run --brief` (220.7 s, exit 0); case rows from the build's printout `the cases the step moved, now.txt`.

| id (r) | items | lines [area] | what fails, as claimed | model / computation; run? | proposal (§4) | form | inventions | S40 | S41 | S44/45 | S47 | area |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| B2 (r21–22) | D6.5, D6.2, NC0, FC108 | L255 [2] | NC0 idle in D6.5: D6.2 has it hold of every candidate, so Dependence ⟺ NC2; L255's first sentence under the heading states the vacuous part and "reads as the condition and is not"; "Not a counterexample" | FC108 run (suite): "NC0 adds no condition — holds by construction" | D6.5 Dependence :⟺ NC2 (was NC0 ∧ NC2); D6.2 unchanged; the text sentence may stay | maths | I23, I187 | — | — | — | — | 2 |
| B4 (r28–29) | E1, τ′ on C_H, D3.3, FC27, the second checker of S106 | L271, L325 [2] | L271's "a reversed calculation … fails (F2) under the production contract", read of every production contract, "is false after S106": on C_H (a production contract by D3.3) the reversed calculation under τ′ meets F1, F2, A, Dep, NonVacuous (slot r_L; round 3's (E) F,F,F,F); on C1 it fails by (F2)'s homomorphism clause; the second checker's "no text change" rests on a reading (which contract "the" names) the reply calls an invention of the step | the build's case printout row ("E1 pole, reversed calculation under Mimo's τ′, H only"); FC27 run: "Hom False … (F2)'s homomorphism clause still excludes it" | L271: "fails (F2) under the production contract:" → "fails (F2) on the production contract \(C_1\) (E1, FC27):" | text: formula / pointer | new, unnumbered (the step's reading of "the production contract") | FLAG ("on") | — | — (the reply: "Keeps S44/S45") | — | 2 |
| B8 (r39–40) | D6.3 Slot, Pin (I184, S106b), `core.slot`, FC23.new3 (a) | maths alone: D6.3 L255 [2] | D6.3's displayed Slot has no "t translates (a,b)"; where τ(a) or σ(b) is undefined its condition is undefined; Pin and `core.slot` have the clause, FC23.new3 (a) identifies Slot with Pin at every pair: "formal D6.3, the code and the claim disagree in that corner"; (E) unaffected | FC23.new3 (a) run, H on 6480 models; the fix not run separately | D6.3 with "t translates (a,b) ∧" inside the ∀ | maths | I184 | — | — | — | — | 2 |
| B9 (r42) | Pin at one pair, FC23.new3 (d), FC23.new1 (a), I184 (b) | maths alone: D6.3 L255 [2] | on C2, c_L pins exactly at the settings of L: "Pin at one pair is not 'the answer written in' there"; under 'every' the mechanism is never a slot, under 'some' it is; I184's registered alternative (b) at pair level (the reply's label: examined, no fix) | FC23.new3 (d) run | none ("no fix — recorded already") | none | I184 (b) | — | — | — | — | 2 |
| B11 = B-N6 (r48–72, r107) | NoBriefQuestion, FC84.new1 (a1), (a2), I191, D9.10, I90, S47 | N6: L13, L55 [1] | NoBriefQuestion (one contract ∧ no D9.10 criticism aimed at the brief) and "a question about the brief occurred to the agent" part both ways: (i) a question occurs, no defect alleged, the brief kept: NoBriefQuestion True, so the encoding "says less than the owner's words" and FC84.new1 (a1)'s gloss "overstates"; (ii) a criticism aimed at the brief taken as given with no question occurring: False, "the stronger claim S47 rejects"; the maths honours S47 (`con`, `prov_fixed_points` take no criticism); the defect is I191's identification, not the text's | Θ by hand (I90), cases (i), (ii); FC84.new1 (a1), (a2) run, hold; code (a3) **not run** (expected "(a3-i) … True", "(a3-ii) … False") | restate FC84.new1 (a1), (a2)'s gloss; new part (a3) in `claims_s41.py` | maths (claim restated) + code | I191, I90 | — | — | — | **check** (rule 11, second limb): the restated gloss writes the bridge as "an episode with one contract throughout and no criticism (D9.10) aimed at the brief" | 1 |
| B12 (r74–75) | (EX) D14.7, CreativeCriticalEpisode, CompleteCritical, FC84.new1 (a1), the [S47] note, D14.5, P8 | L429, L447–L449 [3] | "The one place the maths still asks a criticism of a creation is (EX)": CreateEx → CreativeCriticalEpisode → CompleteCritical → "a criticism (D9.10) of it, and a response that uses the criticism as a reason"; on the bridge (a1) Build and Con hold and CreateEx fails only there, where no question occurred, so the [S47] note's "because the agent asked" covers nothing; whether this clashes with Q6 + S47 "turns on whether the bridge's created thing is a created explanation, which no record fixes"; L429 not touched | FC84.new1 (a1) run (Build, Con hold); FC84.new3 **not run** | new claim FC84.new3; "a look at whether L447–L449 read the bridge's content as an explanatory aim (D14.5)" | maths (new claim) | Θ (Origin's conjuncts, I90); P8 | — | note: bears on Q6 with S47 (the reply leaves it open) | — | note: names an ask already in (EX); proposes none | 3 |
| B14 (r88–89) | FC14, FC32.new1; `claims_r3a3.core_def_ids`, `claims_a.py`'s FC14 path list | maths alone: FC14, FC32.new1 L526 [3] | both read hard-coded paths outside `model/` absent from the shipped layout: FC14's H "silently became NT", FC32.new1 raises FileNotFoundError (suite exit 0); "128 H, 2 CEX, 7 NT of 137" not reproducible from the sandbox as shipped | suite run: FC14 NOT TESTED; FC32.new1 traceback | add the path "maths/formal core, now.md" to both | code, **not run** (expected FC14 H, FC32.new1 computes, 128/2/7) | — | — | — | — | — | 3 |
| B15 (r91–92) | FC23 (b), `S106 report.md` §1 M4, NC2 | maths alone: FC23 L273, L255 [2] | M4 keeps NC2 by citing FC23 (b), (e); FC23 (b) as stated is CEX (the lookup's background empties Sol_E, no contrast); the satisfiable-background sub-part holds | run: FC23 (b) counterexample; sub-part H, 3935 models | restate FC23 (b) as its satisfiable-background sub-part; the unrestricted wording to a look | maths (claim restated) | — | — | — | — | — | 2 |
| B-N1 (r102) | N1, D7.4, D16.4, D14.7 | N1 [2] | D7.4 declares no δ_v (N1) | none | D7.4 with δ_v; Boundary through Acc((E_v, p, t_v, Γ_v, δ_v)) | maths | — | — | — | — | — | 2 |
| B-N2 (r103) | N2, FC31, D6.8, D16.XV | N2 [1] | FC31 cites L61's replaced wording (N2) | none | FC31 restated | maths (claim restated) | — | — | — | — | — | 1 |
| B-N3 (r104) | N3, (K1), FC107 | N3 [3] | none needed: S45's "everywhere"; Bearing reads Acc once, no regress | FC107 run: Acc True, NC1 False | none | none | — | — | — | — | — | 3 |
| B-N4 (r105) | N4, (Suff), D16.XV, FC23.new2 (f) | N4 [3] | none needed: S44/S45's upshot; Q2's ¬Dec(t) still removes declared ones | FC23.new2 (f) run | none | none | — | — | — | — | — | 3 |
| B-N5 (r106) | N5, the heading at L255, I188, B2 | N5 [2] | none needed; "The vacuous first sentence beneath it is B2's, not the heading's" | none | none | none | I188 | — | — | — | — | 2 |

### 3.2 Job 2, the maths against the words (`s107_glm_maths_words`), 21 findings

Runs the reply reports (r3): `--claim FC23.new2` (H), `FC84.new1` (H), `FC107` (H), `FC90.new1` (H), `FC32.new1` (**traceback**); "Everything else is from the records and the files." Rows of its table (a) with verdict more, less or other are findings, the proposal cell copied whole; its W1, W2, W3 are those rows.

| id (r) | items | lines [area] | what fails, as claimed | model / computation; run? | proposal (whole, or §4) | form | inventions | S40 | S41 | S44/45 | S47 | area |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| R3A1-T1 (r11) | R3A1-T1, D16.XV, Q2 | L61 [1] | more: the student's declared copy: the old span counts it, the new excludes it (¬Dec) | FC30.new1 (a), run | "none — Q2 (S41) fixes ¬Dec; maths stands" | none | — | — | — | — | — | 1 |
| R3A1-T2 = W1 (r12) | R3A1-T2, (Suff), FC21 | L49 [1] | more: the pole's forward organization on a contract of relabelings: "components respond as the target does" holds, Account fails; the gloss named only fidelity, the span is all of (E) ∧ ¬Dec | FC21 (recorded) | "none — the sentence glosses (Suff); maths stands (W1)" | none | — | — | — | — | — | 1 |
| R3A1-T4 (r14) | R3A1-T4, Q2 | L69 [1] | more: as R3A1-T1 | as R3A1-T1 | "none (Q2)" | none | — | — | — | — | — | 1 |
| R3A1-T5 = W2 (r15) | R3A1-T5, D12.7, I50 | L220 [1] | other: τ with τ(a₂a₁) ≠ τ(a₂)τ(a₁) while both equations hold at (a,b): "fidelity fails" on a wide reading, D12.7 gives no violation | witness described, **not run** | "none — narrow extent settled by round 3, invention I50; the text leaves it open (W2)" | none | I50 | — | — | — | — | 1 |
| R3A1-T6 (r16) | R3A1-T6, D12.1, D12.2, the bridge | L201 [1] | less: the words said a constructed history "has" criticism and a selected one none; D12.1/D12.2 carry only the represented-target halves | FC84.new1 (a1), run | "none — the dropped halves are what S47 rejects; maths stands" | none | — | — | — | — | — | 1 |
| R3A3-T1 (r17) | R3A3-T1, D9.6, I166, Q23, FC72.new1 (a) | L397 [3] | more: ¬PM alone, for j who never took it up: the words make it usable, D9.6's acceptance clause does not | FC72.new1 (a) (recorded) | "none — Q23 + I166; maths stands" | none | I166 | — | — | — | — | 3 (K1's line) |
| R3A3-T4 (r20) | R3A3-T4, Held_ℓ, (R), I162 | L405 [3] | less: a holding by a declared transport: Held_ℓ holds, "represented" (Sel or Con) does not | none | "none — cut T′ (I162, Q1 ruled); L526 itself names the loop; text need not settle" | none | I162 | — | — | — | — | 3 |
| R3A3-T5 = W3 (r21) | R3A3-T5, D11.3, I169, FC98.new1 (a) | L375 [3] | more: ≺_h acyclic with an infinite descending chain: the words allow it as a history, D11.3 excludes it; without it T′ has no fixed point | FC98.new1 (a) (recorded) | "none — I169; the maths needs it, the text is silent (W3)" | none | I169 | — | — | — | — | 3 |
| S106-T3 (r25) | S106-T3, E_lk, FC23 (e), FC23.new2, S45 | L255 [2] | other (mandated): E_lk with a varying answer meets (E) | FC23.new2 run: (E) True, NC1 False | "none — S45" | none | — | — | — | — | — | 2 |
| S106-T6 (r28) | S106-T6, the one-part sign, FC23.new2 (b), S44, S45 | L273 [2] | other (mandated): the old words "fails"; FC23.new2 (b) meets (E) under every reading | FC23.new2 (b), run | "none — S44, S45" | none | — | — | — | — | — | 2 |
| S106-T11 (r33) | S106-T11, D9.7, I24, I28, I39 | L397 [3] | other: premises r ∧ ¬φ against ¬φ alone: the same under D9.7's flattened-conjunct reading; NC1's "structural at the declared grain" was never defined | none | "none — the defined reading replaces an undefined one (I39); text need not settle" | none | I24, I28, I39 | — | — | — | — | 3 (K1's line) |
| W-b (r42) | L13 "conjecture", I190 | L13 [1] | residue of the revert: "conjecture" stands where "criticism" stands; no definition reads a conjecture event (the construction trace the nearest); I190 covers only "and criticism"; "Nothing turns on it" | none | none ("no proposal") | none | I190 | — | — | — | — | 1 |
| W4 (r65; P3 r83) | D6.9's quoted L257 span, round 3's A2-T3 | L257 [2] | D6.9's quote still reads "admits no candidate that meets non-circular dependence"; the text has "(F2), (A) and Dependence (FC21)"; no mark records it; the formula unaffected | none | P3: D6.9's quoted span replaced by the current L257 span, with an [r3: A2-T3] mark | maths (editorial) | — | — | — | — | — | 2 |
| W5 (r66) | D16.XV's Uses, FC30.new1, (Suff) | L536, L538 [3] | "An argument not using (E)" read at symbol level ((E), Acc ∉ Uses(α)); an argument whose only Acc-use is Acc(ℰ′) for another candidate is outside the defeat set formally, though in words it does not use (E) on ℰ; at instance level FC30.new1's defeat sets change; the text does not fix which: an unregistered choice | none | "register it (no formal change; the symbol reading is what FC30.new1 computes and is the conservative one)" | register | new, unnumbered | — | note: bears on Q2's defeat set; proposes no change | — | — | 3 |
| W6 (r3, r42, r91; P4 r85–91) | FC32.new1, `claims_r3a3.core_def_ids` | maths alone: FC32.new1 L526 [3] | FC32.new1 "crashes in this folder" (FileNotFoundError …/formal core, after round 2.md); "its H rests on a printout made elsewhere" | run: traceback | P4: the path "maths/formal core, now.md" added | code, **not run** | — | — | — | — | — | 3 |
| W-N1 = W7 (r104; P1 r73–79) | N1, D7.4, D16.4, D14.7, FC90.new1 (c) | N1 [2] | Boundary(v,w) undetermined until δ_v is fixed | FC90.new1 run: "Acc differs between δ_E = L and δ_E = H …" | P1: D7.4 with δ_v, Boundary through Acc(E_v, p, δ_v) | maths | none new (D16.4's I183) | — | — | — | — | 2 |
| W-N2 (r105; P2 r81) | N2, FC31 | N2 [1] | FC31's stale L61 reference | none | P2: FC31 restated | maths (claim restated) | I49 | — | — | — | — | 1 |
| W-N3 (r106) | N3, (K1), FC107 | N3 [3] | none needed | FC107 run: Acc True, NC1 False | none | none | — | — | — | — | — | 3 |
| W-N4 (r107) | N4, (Suff), FC23.new2 (f) | N4 [3] | none needed | FC23.new2 (f) run | none | none | — | — | — | — | — | 3 |
| W-N5 (r108) | N5, I188 | N5 [2] | none needed: S40's kinds give no plain-word rename | none | none | none | I188 | — | — | — | — | 2 |
| W-N6 = W8 (r109; P5 r93–100) | N6, NoBriefQuestion, I191, I90 | N6 [1] | the gap is in the encoding of "a question occurred", not in Con; tells against that way of writing the owner's words, not against the text | code **not run** (expected `no_brief_question` True, `no_question_about_brief` False, Con True) | P5: `no_question_about_brief` beside `no_brief_question` in `claims_s41.py` | code | I191, I90 | — | — | — | — | 1 |

### 3.3 Job 3, the structure of the formal core (`s107_glm_structure`), 15 findings

Runs the reply reports (r3, r22–24, r60): `--claim FC32` (H), `--claim FC14` (NOT TESTED), `--claim FC32.new1` (NOT TESTED, FileNotFoundError), `--claim FC23.new3` (H, (a) 6480 models); the rest by reading, with the printout lines it cites.

| id (r) | items | lines [area] | what fails, as claimed | model / computation; run? | proposal (§4) | form | inventions | S40 | S41 | S44/45 | S47 | area |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| S1 (r24; P7 r103–108) | FC14, FC32.new1 | maths alone: FC14, FC32.new1 L526 [3] | hard-coded paths absent from the delivered layout: FC14 NT, FC32.new1 NT with FileNotFoundError; "The two claims that check the core's own structure are not reproducible as delivered" | run, as above | P7: the delivered core's path first in both lists | code, **not run** (expected FC14 H, FC32.new1 H, as printout 350, 1117) | — | — | — | — | — | 3 |
| S2 (r26, r28–37; P2 r84–90) | DEP, D18.1's edge note, D12.2, D13.3, `dep_edges` | maths alone: D18.1 L526, D13.3 L405 [3]; D12.2 L197 [1] | DEP and D18.1's note omit Con → Held and Build → Held, though D12.2 and D13.3 name Held unconditionally; the Held edge enters only through `dep_edges`' T/T′ substitution and vanishes under K; no cycle either way | FC32 run, H; the fix **not run** (expected FC32.new1 (b) as given, FC98 (a), (a′) unchanged) | P2: D18.1's note and `claims_b.py` DEP | maths + code | — | — | — | — | — | 3 (2:1) |
| S3 (r60; P1 r79–82) | D6.3, Pin, I184, I16, I81, FC23.new3 (a) | maths alone: D6.3 L255 [2] | two definitions of Slot: D6.3's clause lacks the translation conjunct Pin has; with π partial exactly off Sol_D(a,b) at a determined pair, D6.3's Slot holds and Pin fails, while the core asserts they are equivalent; they coincide where π is total, and the program's π is total, "so the divergence is untestable there" | FC23.new3 run, H ((a) 6480 models) | P1: D6.3 with the translation clause | maths | I16, I81, I184 | — | — | — | — | 2 |
| S4 (r62; P6 (i) r101) | "subhistory", D11.3, D0.2, `D0_2`, `DEP["Episode"]` | maths alone: D11.3 L375; D0.2 L520–L522, L596 [3] | "subhistory" is at once a primitive read through Θ (D0.2, `D0_2`) and defined (D11.3) | none | P6 (i): D0.2 drops it; `D0_2`, `D0_2_R3A3`; optionally `DEP["Episode"]` | maths + code, **not run** (expected FC32.new1 (c), FC98 (b) unchanged) | I151 | — | — | — | — | 3 |
| S6 (r49; P6 (ii) r101) | D16.XV (L540–L544), D0.2 | L540, L542, L544 [3] | Work(κ), "without loss", "operates on", "fails to capture", "not creative": noted "no definition" in D16.XV, absent from D0.2 | none | P6 (ii): append them to D0.2 | maths | — | — | — | — | — | 3 |
| S-d (r56) | D7.4, D12.6, D14.8, D15.6, D16.1, D16.3; D2.5's dir; D16.2/D16.4's RC, UU, UC, UECS | by definition: L302 [2]; L175–L179, L109 [1]; L455, L477, L487, L495 [3] | definitions that no claim's statement or the program uses; "The text needs every one"; testing them needs Θ | reading | none ("No fix") | none | Θ | — | — | — | — | 3 (4 of 7 definitions) |
| S-δ (r70; P9 r112) | δ: the designation (D3.1 δ_D, I20) and the alleged defect (D9.10, L377's letter) | L377 [3] | δ used two ways; D9.10 uses both in one paragraph ("c = (z, δ, g, Conn, occ)", "ℰ_c := (Conn, …, δ_c)"): δ_c "can be misread as 'the defect of c'" | reading | P9: δ_D/δ_E renamed ι_D/ι_E in D3.1, D3.2, D5.3, D6.3, D6.7, D7.4 (with P4), D14.7, D16.4, D18.1's δ-edges | maths (rename) | I20 (its other choice recorded) | — | — | — | — | 3 |
| S-κ (r71; P8 r110) | κ: D5.1's value maps (I14) and D16.XV (Elim)'s kind-label | maths alone: D16.XV (Elim) L540 [3]; D5.1 L231 [2] | κ used two ways | reading | P8: κ(ℰ) → kl(ℰ) in D16.XV (Elim) | maths (rename) | I14 | — | — | — | — | 3 (tie 1:1 → D16.XV (Elim), the definition P8 changes) |
| S-f (r72–74) | "Dependence" (D6.5; "Dependence order", L526, D18.1); C (D3.1; D15.2–D15.3); the program's `core.dep`, `claims_b.DEP`, node "Dep", `account(reading="r3")` | L262 [2]; L526, D15.2 [3] | one name or letter for two or three things, in three places | reading | none ("none needed" each: L526's words and D18.1's title keep them apart; D15.2's note; scopes disjoint) | none | I188 | — | — | — | — | 3 (2:1) |
| S-N1 (r116; P4 r97) | N1, D7.4, D5.3, D16.4, D14.7 | N1 [2] | D7.4 declares no δ_v | none | P4: D7.4 with δ_v, "the designation of Q in E_v (D5.3)" | maths | — | — | — | — | — | 2 |
| S-N2 = (a)'s FC31 row, "S13" (r15, r117; P5 r99) | N2, FC31 | N2 [1] | FC31 stale: L61 now writes Account(ℰ) ∧ ¬Dec(t); L520 now writes (E)'s five conjuncts | none (FC31 is NT) | P5: FC31 restated | maths (claim restated) | — | — | — | — | — | 1 |
| S-N3 (r118) | N3, (K1), FC107, P8 | N3 [3] | none needed; which questions a slot leaves open is parked (P8) | FC107, H | none | none | — | — | — | — | — | 3 |
| S-N4 (r119) | N4, (Suff), FC23.new2 (f) | N4 [3] | none needed; "bad" is parked; Q2 kept | FC23.new2 (f), H | none | none | — | — | — | — | — | 3 |
| S-N5 (r120) | N5, D6.5, I188 | N5 [2] | none needed | none | none | none | I188 | — | — | — | — | 2 |
| S-N6 = S5 (r47–48, r121; P3 r92–95) | N6, NoBriefQuestion, D9.10's z, I191, I90 | N6 [1] | NoBriefQuestion "defined nowhere in the core"; the brief as a criticism's target: D9.10's z untyped | look-up here: no "NoBriefQuestion" in the formal core (§2) | P3: new definition D12.2.new NoBriefQuestion | maths | I191, I90 | — | — | — | **check** (rule 11, second limb): defines NoBriefQuestion in the core as "no occurrence of h′ is a criticism … with z = C_b" | 1 |

### 3.4 Job 4, the cases (`s107_glm_cases`), 10 findings

Runs the reply reports (r3): `--claim FC23.new2 --claim FC23.new3 --claim FC25.new2 --scale 4` and `--claim FC84.new1 --claim FC107 --claim FC30.new1 --scale 4`, all "HOLDS ON ALL MODELS TRIED"; the case scripts' printouts. New cases NC1, NC3, NC4, NC5, NC6 **not run**; NC2 run (within FC23.new2).

| id (r) | items | lines [area] | what fails, as claimed | model / computation; run? | proposal (§4) | form | inventions | S40 | S41 | S44/45 | S47 | area |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| C-K1 (r12, r29; T1 r155) | E1, τ′ on C_H, D3.3, FC27's look, L271, L325 | L271 [2] | L271's "fails (F2) under the production contract", read of production contracts generally, "states a result the computation does not give": on C_H the reversed calculation under τ′ meets all five conjuncts (printout row 16), its (F2) already held in round 3 (the exclusion was NC1's); read of E1's C1, "it is true" | the build's case printout, row 16 | T1: L271 "fails (F2) under the production contract:" → "fails (F2) on \(C_1\) (E1):"; L325 unchanged | text: formula | I65 | FLAG ("on") | — | — | — | 2 |
| C-K2 (r58; T2 r157) | CT8 R2, R4; D12.3 (Dec := ¬Sel ∧ ¬Con); round 2's C01 | L199, L193 [1] | on R2 and R4 the pair is "neither (declared by exclusion)"; the reply takes L199 to hold a sentence describing a history the run's is not (the pair computed, not written); L193's "exactly one of three" holds only because Dec is by exclusion | the CT8 printout | T2 at L199; "If C01 is ruled the other way, withdraw this" | text: formula | C01 (never ruled on), I53, I118 | — (old span not found, §2) | note: bears on Dec(t), Q2's lever | — | — | 1 |
| C-K3 (r84; C1 r163; NC6 r136–151) | the owner's two-part sign, FC23.new2 (a), I189 | maths alone: FC23.new2 (a) (FC23 L273; (E) L255, L262) [2]; L31 cited only as ground | on a behaviour-only target (one component, red on Mondays, blue on Tuesdays) no λ lets the two-part candidate meet (F1) at both pairs: "the owner's sign meets (E) only on I189's grain"; "this tells against the encoding, not the text" | NC6 code **not run** (expected F1 False at one pair under every λ) | C1: code recording that FC23.new2 (a) holds on I189's target only | code | I189 | — | — | — | — | 2 (choice: L31 is the reply's ground, not the line attacked) |
| C-E6 (r26) | E6 (skew, Leibniz), FC63 (c-i), I99 | L343 [2] | the text: "The expansion is an account"; FC63 (c-i) "computed not as claimed (CEX, I99)"; unmoved: "round 3's standing counterexample" | recorded printout | none | none | I99 | — | — | — | — | 2 |
| C-N1 (r169; M2 r161) | N1, D7.4, D5.3, I20 | N1 [2] | D7.4 declares no δ_v | none | M2: D7.4 with δ_v | maths | I20 | — | — | — | — | 2 |
| C-N2 = C-K4 (r170; M1 r159) | N2, FC31, round 3's R3SC-L61 | N2 [1] | FC31 cites L61, where the phrase was removed | none | M1: FC31 restated (L61 dropped), status stays NT | maths (claim restated) | — | — | — | — | — | 1 |
| C-N3 (r171; NC5 r123–134) | N3, (K1), FC107, L383 | N3 [3] | no fix; L383 keeps its truth; no line states the old result | FC107 run; NC5 **not run** (expected account False) | none | none | — | — | — | — | — | 3 |
| C-N4 (r172) | N4, (Suff), FC23.new2 (f) | N4 [3] | no fix | FC23.new2 (f), run | none | none | — | — | — | — | — | 3 |
| C-N5 (r173) | N5 | N5 [2] | no fix: S40's kinds admit no plain-word rename | none | none | none | — | — | — | — | — | 2 |
| C-N6 = C-K6 (r174; C2 r165; NC4 r112–121) | N6, NoBriefQuestion, I191, I90 | N6 [1] | no formal change: NoBriefQuestion "a reading tag no conjunct reads"; "not pursued" is not represented | NC4 code **not run** (expected `False` / `[True] True`) | C2: code (NC4) | code | I191, I90 | — | — | — | — | 1 |

### 3.5 Item K1, the winter-myth knock-on (addendum), area 3

| item | lines [area] | what the addendum asks | where the replies touch its lines (they go with it) | area |
|---|---|---|---|---|
| K1 (the winter-myth knock-on) | L317 [2] (S106-T8), L397 [3] (S106-T10): two areas, so the area holding L397 | The checker says what the theory now says about the myth about winter; computes it where the program can encode it; says whether the owner's words settle the older question (file 96's question 2, `plain words/96 …` L76; file 93's first, `plain words/93 …` L79): S44, S45, S28, S21, S27, S41 (Q23). The orchestrator's reading, a reading and not a decision, is in the addendum (point 2). If neither the owner's words, the texts nor a computation settle it: an owner question (rule 12), both sides, an everyday example, never "model" for a candidate. Any fix: maths, code, or a delete, formula or pointer; no new prose (S40). The record of the point: `S106 what changed.md` L191. | **Findings** (counted in §3.2, area 3 already): R3A3-T1 (L397, D9.6's acceptance clause), S106-T11 (L397, the pointer to D9.7). **Held, not counted** (§5): B (f) r83 (L317: "the 'assumes its own answer' ground deleted; the remaining ground is conflict with a claim (D8.5) — consistent with S45 and S27/S28"); B6 r33 (L397: "read structurally (D9.7)" "a self-pointer", "harmless"); W S106-T8 r30 (L317 same), S106-T10 r32 (L397 same), R3A3-T2 r18, R3A3-T3 r19 (L397 same); W residue scan r38 (no "assumes its own" left; "circular" at L397 is D9.7's block); S (a) r10 (L397 keeps D9.7's block, "not the slot test"). **No reply names the myth**: "winter" and "myth" occur in none of the four replies; the briefs did not ask (addendum point 3). | 3 |

## 4. Proposals whole

Copied by program from the replies, line for line (reply lines given); nothing added inside a block. The tables of job 2's part (a) carry their proposals whole in §3.2. Every code block below is marked **not run** by its reply or given with expected output only (rule 3).

### `s107_glm_breaker`

#### B2 (r22)

*Fix (maths):* **D6.5** Dependence(ℰ) :⟺ NC2(ℰ) 〔was NC0 ∧ NC2; NC0 holds of every candidate (D6.2, FC108), so the conjunct is idle; D6.2 unchanged〕. The text sentence may stay (true of every candidate); rests on I23/I187, already registered.

#### B4 (r29)

*Fix (text, L271, kind 2/3):* old "fails (F2) under the production contract:" → new "fails (F2) on the production contract \(C_1\) (E1, FC27):". Keeps S44/S45 (the candidate on C_H remains an explanation, a bad one).

#### B8 (r40)

*Fix (maths):* **D6.3** Slot_C(ℰ, k) :⟺ δ_E ∈ V_k ∧ Det_C ≠ ∅ ∧ ∀(a,b) ∈ Det_C [t translates (a,b) ∧ {w_δE : w ∈ L^E_k(τ(a),σ(b))} = {Ans_p(a,b)}] 〔adds Pin's translation clause; matches `core.slot` and FC23.new3 (a), which held on 6480 models (run)〕.

#### B11 = B-N6 (r53–r72)

*Fix (maths):* restate **FC84.new1 (a1), (a2)**: replace "an episode in which no question about the brief occurred to the agent as worth investigating (NoBriefQuestion: one contract throughout, no criticism aimed at it, I191)" by "an episode with one contract throughout and no criticism (D9.10) aimed at the brief (NoBriefQuestion, I191); whether a question about the brief occurred to the agent is read through Θ (I90)".
*Fix (code, not run)* — new part (a3) in `model/claims_s41.py`, `fc84_new1`, after the (a2) loop:

```python
    # (a3) S47: NoBriefQuestion and "a question about the brief occurred" part ways (I191's reading; Θ by hand, I90)
    cases3 = (("i", "a question occurred, no defect alleged, the brief kept",
               ["o1", "o2"], [0, 1], [0, 1], [None, None], True),
              ("ii", "a criticism aimed at the brief, no question occurred to the agent",
               ["o1", "o2"], [0, 1], [0, 1], [("C_brief (the contract)", "the brief is wrong"), None], False))
    for key, lab, occ, held_, trace_, crit, asked in cases3:
        qs = ["C_brief"] * len(occ)
        noq = no_brief_question(qs, crit)
        parts.append(computed("(a3-%s) NoBriefQuestion against 'a question occurred' (%s)" % (key, lab),
                              "NoBriefQuestion and 'a question about the brief occurred to the agent' part ways: expected (i) True/True, (ii) False/False (the encoding both under- and over-shoots I191's gloss)",
                              noq is True and asked is True if key == "i" else noq is False and asked is False,
                              "chain %s; q = C_brief throughout; criticism per occurrence %s; a question occurred: %s; NoBriefQuestion: %s"
                              % (" ≺ ".join(occ), crit, asked, noq), ["I90", "I191"]))
```

Expected output (not run): "(a3-i) … NoBriefQuestion: True", "(a3-ii) … NoBriefQuestion: False" — the two rows exhibit both directions.

#### B12 (r75)

*Fix (maths, new claim, not run):* **FC84.new3** — on the chains of FC84.new1 (a1) (held, trace, q = C_brief throughout, no criticism), Build holds and CreateEx fails only through CreativeCriticalEpisode's criticism clause; a look at whether L447–L449 read the bridge's content as an explanatory aim (D14.5).

#### B14 (r89)

*Fix (code, not run):* in `model/claims_r3a3.py::core_def_ids` and `model/claims_a.py`'s FC14 path list, add the candidate path `"maths/formal core, now.md"`. Expected: FC14 reads the 118 definition lines (H restored); FC32.new1 computes (115 paragraphs, DEP 83 nodes) and the suite returns to 128 H, 2 CEX, 7 NT.

#### B15 (r92)

*Fix (maths):* restate **FC23 (b)**: "Ans_p not constant on C ∧ Sol_E(τa,σb) ≠ ∅ on C ⇒ NC2(E_lk) with G = {k}" (the existing sub-part), moving the unrestricted wording to a look; the record then agrees with what M4 cites.

#### N1–N6 (B-N1 … B-N6) (r100–r107)

| # | fix |
|---|---|
| N1 | **Maths:** D7.4 — "each v ∈ 𝒱 declaring (E_v, t_v, Γ_v, **δ_v**)" and Boundary := {(v,w) ∈ 𝒱² : Acc((E_v, p, t_v, Γ_v, δ_v)) ≠ Acc((E_w, p, t_w, Γ_w, δ_w))} 〔brings D7.4 in line with D16.4 and D14.7, which quantify δ〕 |
| N2 | **Maths:** restate FC31 — "five conjuncts (D6.7) under four headings (D6.8); L61 writes Account(ℰ) ∧ ¬Dec(t) (D16.XV); L536's 'the four' reads D6.8's headings against L262/L520's five conjuncts" 〔drops the stale reference to L61's replaced wording〕 |
| N3 | None needed: S45's "the theory changes everywhere the test is used" gives it; Bearing reads Acc once, so no regress, and D6.3 is what criticism points at (FC107, run: Acc True, NC1 False, noted) |
| N4 | None needed: (Suff)'s range holding slot candidates is S44/S45's upshot (D16.XV's [S106] note says so); Q2's ¬Dec(t) still removes the declared ones (FC23.new2 (f), run) |
| N5 | None needed: S40's kinds allow a formal name only, and I188 recorded the alternatives; the heading is a kind-2 change. The vacuous first sentence beneath it is B2's, not the heading's |
| N6 | B11: restate FC84.new1 (a1), (a2) and add (a3); the identification of question-occurrences with criticisms is I191's invention, and the counterexamples tell against that way of writing the owner's words, not against the text |

### `s107_glm_maths_words`

#### W5 (its proposal ends the paragraph) (r66)

- **W5 (D16.XV's Uses is an unregistered choice).** "An argument not using (E)" is read at symbol level: (E), Acc ∉ Uses(α). An argument whose only Acc-use is Acc(ℰ′) for another candidate ℰ′ (leaf "Acc(ℰ′) → ¬Expl(ℰ)") is outside the defeat set formally, though in words it does not use (E) *on ℰ*. Changes FC30.new1's defeat sets if read at instance level. The text does not fix symbol vs instance; this is a choice that should be registered as an invention. Proposal: register it (no formal change; the symbol reading is what FC30.new1 computes and is the conservative one).

#### W-N1 = W7: P1 (r73–r79)

**P1 (maths, N1/W7).** Beside D7.4, replace:
> Boundary := {(v,w) ∈ 𝒱² : Acc(E_v, p) ≠ Acc(E_w, p)}, each v ∈ 𝒱 declaring (E_v, t_v, Γ_v), …

with:
> **D7.4** Boundary := {(v,w) ∈ 𝒱² : Acc(E_v, p, δ_v) ≠ Acc(E_w, p, δ_w)}, each v ∈ 𝒱 declaring (E_v, t_v, Γ_v, δ_v), t_v the transport the operation carries t to, Γ_v the commitments it leaves and δ_v the designation it carries (L231) — as D16.4 and D14.7 quantify δ.

Witness (run: `--claim FC90.new1`, result "Acc differs between δ_E = L and δ_E = H … (True, …A: True…) / (False, …A: False…)"): Boundary(v,w) is undetermined until δ_v is fixed. Inventions: none new (follows D16.4's I183).

#### W-N2: P2 (r81)

**P2 (maths, N2).** FC31 restated: "'The four conditions' at L231 and L536 are the four headings of Part V (Component fidelity = (F1) ∧ (F2), Question fidelity = (A), Dependence, Non-vacuity); (E) writes them as five conjuncts. L61 writes Account(ℰ) ∧ ¬Dec(t) (D16.XV). L520's three sources cover the four headings exactly when 'fidelity under change' has the wide extent Fid⁺ (I49)…" — dropping the stale L61 reference.

#### W4: P3 (r83)

**P3 (maths, W4).** D6.9's quoted span replaced by the current L257 span: "admits no candidate that meets (F2), (A) and \(\operatorname{Dependence}\) (FC21)", with an [r3: A2-T3] mark.

#### W6: P4 (r85–r91)

**P4 (code, W6 — not run).** In `model/claims_r3a3.py`, `core_def_ids()`:
```python
for alt in (os.path.join(HERE, "..", "..", "formal core, after S106.md"),
            os.path.join(HERE, "..", "..", "maths", "formal core, now.md"),  # + this line
            os.path.join(HERE, "..", "..", "..", "S105 Round 3 - maths after the reading", "formal core, after round 3.md")):
```
Expected: `FC32.new1 HOLDS ON ALL MODELS TRIED`, part (a) reading the core's paragraphs as the recorded printout does (line 1113–1117 of `whole suite now, scale 4, time cap 45.txt`). As it stands the claim crashes in this folder (`FileNotFoundError: …/S104 Round 2 - maths after the reading/formal core, after round 2.md`), so its H rests on a printout made elsewhere.

#### W-N6 = W8: P5 (r93–r100)

**P5 (code, N6/W8 — not run).** In `model/claims_s41.py`, beside `no_brief_question`:
```python
def no_question_about_brief(qs, quest, brief="C_brief"):
    """N6, the wider reading of I191: a question about the brief is any question-event whose topic is the brief,
    whether or not it alleges a defect (a criticism, D9.10). quest[o]: None, or a topic, read through Θ (I90)."""
    return all(q == brief for q in qs) and not any(t is not None and t.startswith(brief) for t in quest)
```
Expected output on the (a1) chain with `quest = ["what the brief's load case means", None]`: `no_brief_question → True` (I191: no criticism aimed at the brief), `no_question_about_brief → False`, `Con → True` either way. This shows the gap is in the encoding of "a question occurred", not in Con. Rests on inventions I191 and I90; the text does not settle which occurrences are questions, so the finding tells against that way of writing the owner's words, not against the text.

#### N1–N6 (W-N1 … W-N6) (r104–r109)

- **N1** → P1 (witness run, FC90.new1 (c)).
- **N2** → P2.
- **N3** → none needed: (K1)'s words say Bearing ⟺ Account(ℰ_c) and the formula says the same; that slot connections now have bearing is S45's "everywhere", computed (FC107, run: Acc True, NC1 False).
- **N4** → none needed: (Suff)'s range holding slot-bearers follows from S45, and they are explanations (bad ones) by S44, so no argument ruling them explanations-based defeats anything the owner excludes; L536's "all four conditions of (E)" still names the four headings (D6.8); Q2's ¬Dec is kept (FC23.new2 (f), run).
- **N5** → none needed: S40's three kinds give no plain-word rename; the formal name is the condition's own (I188), and any plain-word name would be new prose.
- **N6** → P5; the choice is I191's, registered with its other readings.

### `s107_glm_structure`

#### S3: P1 (r79–r82)

**P1 (maths, D6.3).** Beside the current clause, write:
> Slot_C(ℰ, k) :⟺ δ_E ∈ V_k ∧ Det_C ≠ ∅ ∧ ∀(a,b) ∈ Det_C [t translates (a,b) ∧ {w_δE : w ∈ L^E_k(τ(a),σ(b))} = {Ans_p(a,b)}]

so D6.3's Slot is exactly Pin at every pair of Det_C (FC23.new3 (a) as stated; `core.slot` under "every" already requires `cand.translates`). Inventions: none new (the two readings differ only over I16's open π domain; I184 unchanged).

#### S2: P2 (r84–r90)

**P2 (maths + code).** Maths, D18.1's edge note: "Con → CT, Episode" → "Con → CT, Episode, Held"; "Build → ExplUse → (E)" → "Build → ExplUse, Held; ExplUse → (E)". Code, `model/claims_b.py` DEP:
```python
"Con": ["h", "CT", "Episode", "Held"],                       # S2: D12.2 reads Held outright
"Build": ["h", "Owned", "Prepares", "BindingConstruction", "TransferComposite",
          "ExplUse", "Held"],                                # S2: D13.3 reads Held_ℓ(o, c)
```
(Sel keeps its staged Rep use; `dep_edges` unchanged.) Not run; expected: FC32.new1 (b) "U: Live → (K2) → Live (through (R): (R) → Sel → (R)); K: None; T: None; T′: None"; FC98 (a), (a′) unchanged; no status changes.

#### S-N6 = S5: P3 (r92–r95)

**P3 (maths, new definition beside D12.2).**
> **D12.2.new NoBriefQuestion.** NoBriefQuestion(h′, C_b) :⟺ every o ∈ h′ has q(o) = C_b, and no occurrence of h′ is a criticism c = (z, δ, g, Conn, occ) (D9.10) with z = C_b **[I191]**; which occurrences are criticisms, and of what, is read through Θ (I90).

Used by FC84.new1 (a1), (a2). Inventions: I191, already registered; no new choice.

#### S-N1: P4 (r97)

**P4 (maths, D7.4).** "each v ∈ 𝒱 declaring (E_v, t_v, Γ_v)" → "each v ∈ 𝒱 declaring (E_v, t_v, Γ_v, δ_v), δ_v the designation of Q in E_v (D5.3)". (N1; matches D7.1 and D16.4/D14.7.)

#### S-N2: P5 (r99)

**P5 (maths, FC31 restated).** Statement → "(E) has five conjuncts; Part V has four headed conditions: Component fidelity = (F1) ∧ (F2), Question fidelity = (A), Dependence, Non-vacuity. 'The four conditions' at L231 and L536 are the four headings (L61's phrase was replaced by Account(ℰ) ∧ ¬Dec(t) in round 3); L520 names (E)'s conjuncts, so it names a source for (A), and FC104's open extent is L630's alone." (N2.)

#### S4, S6: P6 (r101)

**P6 (maths, D0.2).** (i) "Org_ℓ(h) and subhistory [I151]" → "Org_ℓ(h) [I151]; a subhistory is defined (D11.3)". (ii) append: "Work(κ) [L540]; 'without loss' and 'operates on' [L542]; 'fails to capture' and 'not creative' [L544]: used by D16.XV's shapes, defined nowhere". Code: `D0_2` drop `"subhistory"`; `D0_2_R3A3["subhistory"] = "defined (D11.3, I151)"`; optionally `DEP["Episode"]` drop `"subhistory"`. Not run; expected: FC32.new1 (c) "After area 3: none" unchanged, FC98 (b) unchanged.

#### S1: P7 (r103–r108)

**P7 (code).** In `claims_r3a3.core_def_ids` and the `tries` list of `claims_a` (FC14), put the delivered core first:
```python
for alt in (os.path.join(HERE, "..", "maths", "formal core, now.md"),
            os.path.join(HERE, "..", "..", "formal core, after S106.md"), ...):
```
Not run (nothing can be written here). Expected: FC14 → "HOLDS ON ALL MODELS TRIED … 118 definition lines; matching 'is a cause' / 'IsCause' / 'Cause(': 0"; FC32.new1 → "HOLDS ON ALL MODELS TRIED … 114 paragraphs read from the formal core; not mapped: none …", as in printout 350 and 1117.

#### S-κ: P8 (r110)

**P8 (maths, D16.XV (Elim)).** "a kind-label κ(ℰ) ≠ κ(ℰ')" → "a kind-label kl(ℰ) ≠ kl(ℰ′)" (κ stays D5.1's value map, I14).

#### S-δ: P9 (r112)

**P9 (maths, the designation's letter).** Rename δ_D/δ_E (I20) to ι_D/ι_E in D3.1, D3.2, D5.3, D6.3, D6.7's argument list, D7.4 (with P4), D14.7, D16.4 and D18.1's δ-edges (Dep, Slot), so that D9.10's δ (the alleged defect, L377's own letter) is the only δ. A rename only, no content; I20's other choice recorded.

#### N1–N6 (S-N1 … S-N6) (r116–r121)

- **N1** — fix P4 (D7.4 names δ_v; D16.4 and D14.7 already quantify δ).
- **N2** — fix P5 (FC31 restated; it is NT, so nothing is recomputed).
- **N3** — none needed: it is S45's own consequence (Bearing reads Acc, D9.10's [S106] note, FC107 H); which questions a slot leaves open is parked (P8 of the register).
- **N4** — none needed: (Suff)'s range holding slot candidates is what S44/S45 say ("it is an explanation … just not a good one"); "bad" is parked; S41 (Q2) is kept (FC23.new2 (f), H).
- **N5** — none needed: the heading names D6.5 (I188, S40's formal-statement kind); the plain-word name the condition has lost was the removed test's own ("non-circular"), and the kinds of change allowed are D6.4's, quoted in full at L255.
- **N6** — fix P3: NoBriefQuestion defined in the core with the criticism's target z typed to the contract, its Θ-reading (I90) kept as I191 states it.

### `s107_glm_cases`

#### C-K1: T1 (r155)

**T1 (text, K1; L271).** Kind: span replaced by its formal statement. Line L271; old span: `fails (F2) under the production contract:`; new span: `fails (F2) on \(C_1\) (E1):`. The rest of the sentence stays. (L325 speaks inside E1's stipulation and needs no change.) Inventions: I65 (E1's contracts).

#### C-K2: T2 (old span not in the text under review, §2; its 'model' is round-1 wording in L13's sense, not a candidate) (r157)

**T2 (text, K2; L199).** Kind: span replaced by its formal statement. Line L199; old span: `The transport is entered into the model by its author. Write \(\operatorname{Dec}(t)\).`; new span: `\(\operatorname{Dec}(t)\) (D12.3).` Rests on round 2's C01 (never ruled on) and I53/I118: CT8's R2/R4 are Dec by exclusion, and the deleted sentence describes a history a computed transport is not. If C01 is ruled the other way, withdraw this.

#### C-N2 = C-K4: M1 (r159)

**M1 (maths, K4/N2; FC31).** Old: `| FC31 | 'The four conditions', five conjuncts, and L520's three sources | (E) has five conjuncts; Part V has four headed conditions: … 'The four conditions' at L61, L231 and L536 are the four headings. …` New: the same statement with `'The four conditions' at L231 and L536 are the four headings` (L61 dropped: round 3's R3SC-L61 removed the phrase there). Status stays NT.

#### C-N1: M2 (r161)

**M2 (maths, N1; D7.4).** Old: `each v ∈ 𝒱 declaring (E_v, t_v, Γ_v), t_v the transport the operation carries t to and Γ_v the commitments it leaves (L231).` New: `each v ∈ 𝒱 declaring (E_v, t_v, Γ_v, δ_v), t_v the transport the operation carries t to, Γ_v the commitments it leaves and δ_v the designation carried to E_v (L231; D5.3, I20).` Invention: I20.

#### C-K3: C1 (r163)

**C1 (code, K3; NC6 above).** Not run; expected output as annotated. Records that FC23.new2 (a) holds on I189's target only.

#### C-N6 = C-K6: C2 (r165)

**C2 (code, N6/K6; NC4 above).** Not run; expected `False` / `[True] True`.

#### C-N6's code, NC4 (r112–r121)

**NC4 — the bridge with a question about the brief that occurred and was not pursued.** Under I191 an occurrence is a criticism aimed at the brief; "not pursued" is not represented — the label reads occurrence, not pursuit, through Θ (I90). Con and Build are unchanged. Agreement with S47: the maths asks nothing. *Not run.*
```python
from model.claims_s41 import no_brief_question
from model.claims_b import prov_fixed_points, build_at, chain_eps
qs, recs = ["C_brief","C_brief"], [False, False]
crit = [("C_brief (the contract)", "why this brief?"), None]   # occurred at o1, not pursued
print(no_brief_question(qs, crit))   # expected False
fps = prov_fixed_points(2, [0,1], [0,1], [0,0], "T'", True, chain_eps(qs, recs, "S41"))
print([sc[1][1] for R, sc in fps], build_at(2, [0,1], [0,1], "T'", fps[0][0], 1))  # expected [True], True
```

#### C-K3's code, NC6 (r136–r151)

**NC6 — the two-part sign of a behaviour-only target (K3).** *Not run.*
```python
from model.core import ONE, Question, PortQuery, Candidate, Translation, account
from model.claims_s106 import _org, _T, COLOURS
Db = _org("D_beh", ["colour"], {"colour": COLOURS}, ["c"], {"c":("colour",)}, ["b0"], [ONE,"tue"],
          {("c",ONE,"b0"):{("red",)},("c","tue","b0"):{("blue",)}})
pb = Question(Db, [(ONE,"b0"),("tue","b0")], "b0", PortQuery(), "colour", name="p_beh")
E2 = _org("E_2parts", ["colour"], {"colour": COLOURS}, ["r","u"], {"r":("colour",),"u":("colour",)}, ["b0"], [ONE,"tue"],
          {("r",ONE,"b0"):{("red",)},("u","tue","b0"):{("blue",)}})
for lam in ({k:(frozenset(["c"]),_T("colour")) for k in "ru"},
            {"r":(frozenset(),_T("colour")), "u":(frozenset(["c"]),_T("colour"))}):
    print(lam, account(Candidate(E2, pb, _T("colour"), {ONE:ONE,"tue":"tue"}, {"b0":"b0"}, lam, ["r","u"], "colour"),
                       detail=True))
# expected: F1 False at one of the two pairs under every λ: {c} projects {blue} at Tuesday against r's full relation,
# ∅ projects full at Monday against {red}. S44's sign meets (E) only on I189's target (grain a declared index, L31).
```

#### N1–N6 (C-N1 … C-N6) (r169–r174)

- **N1** — fix M2 above (δ_v added to D7.4's declarations).
- **N2** — fix M1 above (FC31 restated); no text change: L61 no longer contains the phrase.
- **N3** — no fix: (K1) is Bearing ⟺ Account; after S45 the written-in connection meets (E) where it meets the rest, as S44 says of it; L383 keeps its truth and no line states the old result (FC107's note says the same).
- **N4** — no fix: (Suff)'s defeat set is unchanged in shape; that its range now holds candidates with a slot is S44/S45's own content (they are explanations, bad ones), and Q2 still removes the declared ones (FC23.new2 (f), run).
- **N5** — no fix: S40's three kinds admit no plain-word rename (the step's §13); nothing rests on a plain name; every use of the heading is by the formula or the pointer.
- **N6** — fix C2 above; no formal change: NoBriefQuestion is a reading tag no conjunct reads, which is what S47 asks ("the math doesn't ask for anything"); which occurrences are criticisms stays Θ's, with the other readings recorded at I191.

## 5. Examined and held by the replies (not findings, not counted; silence and agreement are not rulings, rule 3)

| job | what the reply examined and marks held, same, clean or agreeing (reply lines) |
|---|---|
| breaker | (a) r9–13: E_enc on C1, C2 meets (E) ("L269's own second sentence allows it"; FC25.new2 H, 3726/3726); "p because p" (S45; L273 the pointer); M1–M3, the hand-turned vane, the one-part sign, the E8 identity candidate ("S44/S45's own cases"). B1 r15, the Q2 probe: the declared pendulum formula meets (E) and is removed only by D16.XV, "Nothing here clashes". r17: no worked exclusion the reply could build is admitted by (E) against the text or the owner's words; the 10 moved and 5 reading-relative cases held. B3 r24: Dependence "is not the test by another name and not empty". B5 r31 tables. B6 r33 circular arguments, with a residue at L397 ("read structurally (D9.7)", "a self-pointer", "harmless"; goes with K1). B7 r35 the bare denial (L339). B10 r44: nothing reads Slot or NC1 as a condition of (E). B13 r77, "held, with a note": a brief changed with no criticism and no question, Con by the record; I190 makes L13's phrase non-restrictive, "the words stretch but the owner's S47 endorses exactly this inclusion"; Con, CT, Episode, Sel, Dec, Build read no Crit. (f) r81–86: the L13 revert byte-exact; L49, L61, L69 consistent; L317 (goes with K1); L343; L536 (to N2); L520, L262, L257, L275 match. (g) r96. |
| maths_words | (a), verdict same: R3A1-T3 (L69), R3A3-T2 and R3A3-T3 (L397, go with K1), R3SC-L61 (L61), S106-T1 and T2 (L255), T4 (L257), T5 (L262), T7 (L275), T8 (L317, goes with K1), T9 (L343), T10 (L397, goes with K1), T12 (L520), T13 (L536), S47-T1 (L13). r38 residue scan. (b) r42 the revert "Same", I190 as S47 (its residue on "conjecture" is W-b). (c) r46–53: D6.2, D6.3 with Pin, D6.5, D6.7, D6.8, D6.10, D18.1 and the renamed conjunct, same. (d) r57–61: Q2, Q6 with S47, Q15, Q23, S44/S45 "written". (e) r69 examined and clean: D6.4, D6.6, D6.8, D6.10; D9.2, D9.6, D9.7, D9.10 against L397, L377; D12.1–D12.3; D12.7; D13.8; L31 against (E) with no grain; FC23's CEX standing. |
| structure | (a) r9–14, r16, r18: no text line, claim, note or DEP node still reads NC1, the grain ℓ or the slot test as a condition of (E) (r10: L397 keeps D9.7's block, "not the slot test"; goes with K1). (b) r22 FC32 H; the dependence table's ✓ rows; r39 cycles: under U, Live → (K2) → Live and one through (R); under K, T, T′ none; S2's edges add none; D6.10 folded into node "(E)", "harmless … no fix". (c) ✓ rows: Pin, Det_C, Held, CT defined; the §§7–16 symbols classed by D0.2. (e) r64 "Examined and nothing against": D6.5 against D6.2 (I187); D16.XV's Expl atom against FC30.new1 (c); D14.7 and D16.4 on δ; D7.1's Acc arity (to N1). (f) r75: ⊥, primes and superscripts applied uniformly. |
| cases | (a): unmoved rows (E1 forward on C1/C2/C3, reversed on C1, C_id, E_tab, the relabeling contract, M5, M13, E5, E9) and moved rows that agree with S44/S45 (E_enc, "p because p", M1–M3, the hand-turned vane, E8); the bare denial (not encoded; ¬Acc by (F1)/Dep); E2, E3, E4, E7, the routes (no (E) computed). (b) r35–41: FC-E1–FC-E5 unmoved, outputs md5-identical. (c) r45–56: CT1–CT8, nothing moved by the step or the revert; CT8: "constructed" for R1/R3 "now rests on I190's reading of L13's phrase — an invention, the text not fixing whether an episode with no question occurring to the agent is one 'of conjecture and criticism'", "correctly none". (d) r64–74: every moved case agrees with the owner's words but τ′ on C_H (C-K1); r72 note: under round 3's 'some' reading the owner's two-part sign and the pole's forward organization on C2 were excluded. (e) r80–83: the student (Q2), the bridge (Q6 with S47), the weathervane (Q15), "perpetual motion is impossible" (Q23): the maths gives the owner's answer. (f) NC1 r88–98 (a constant sign fails Dependence; **not run**), NC2 r100 (run within FC23.new2: the contrast carried by a pinned part), NC3 r102–110 ("The pair's content is unregistered, but the candidate fails (E) there anyway. No fix needed."; **not run**), NC5 r123–134 (C-N3's case; **not run**). r176 examined, nothing found against. |

## 6. One point, several findings (for the orchestrator; no ruling)

1. **L271, the reversed calculation on C_H**: B4 [2], C-K1 [2]. Two text proposals for one span, both FLAG ("on" for "under"): B4 keeps "the production contract" and adds "\(C_1\) (E1, FC27)"; C-K1 puts "\(C_1\) (E1)" in its place. The same words, ending ".", stand at L536 ((Suff), N4's line, area 3), which neither reply names.
2. **D6.3's Slot without Pin's translation clause**: B8 [2], S3 [2]: the same formula (B8 r40; S's P1 r80). B9 [2] bears on Pin at one pair.
3. **FC14 and FC32.new1 do not find the formal core in the sandbox**: B14 [3], W6 [3], S1 [3]. The result is reported three ways: "raises FileNotFoundError … (traceback printed, suite exit 0 anyway)" (B14, whole suite), "traceback" (W6), "NOT TESTED … FileNotFoundError" (S1). Three code fixes to the same path lists: `claims_r3a3.core_def_ids` in all three, and `claims_a.py`'s FC14 `tries` in B14 and S's P7; the sandbox path added (B14), as a second choice (W's P4), first (S's P7). For the checker, a fact of layout: the program's paths are relative to `model/` and name `formal core, after S106.md` two folders up, where it stands in the repository (`results/S106 The written-in test taken out/`) and where the build's printout (128/2/7) was made; the sandbox puts the core at `maths/formal core, now.md` (manifest).
4. **N6, NoBriefQuestion and I191**: B11 = B-N6, W-N6 = W8, S-N6 = S5, C-N6 = C-K6, all area 1, four different proposals: FC84.new1's gloss restated and a code part added (B); a wider reading as a second function (W); a definition in the core (S); a code probe, no formal change (C). Two are marked **check** under S47 (B11, S-N6). B12 [3] bears on the bridge (Q6 with S47) through (EX); R3A1-T6 and W-b [1] on the criticism wording of L201 and L13.
5. **N1, D7.4's δ_v**: B-N1, W-N1, S-N1, C-N1, all area 2, all add δ_v to D7.4's declarations; B and W also write Boundary with δ; S and C gloss δ_v by D5.3 (C adds I20). S-δ's P9 [3] renames the same letter in D7.4 and eight other definitions: the two bear on one another.
6. **N2, FC31**: B-N2, W-N2, S-N2, C-N2, all area 1, all restate FC31 without L61; the wordings differ (W keeps the Fid⁺/I49 sentence; S adds an L520 clause; C keeps status NT).
7. **N3, N4, N5**: all four replies: none needed.
8. **L255, L273 and FC23 after S106**: B2, B8, B9, B15, S106-T3, S106-T6, S3, B-N5, C-K3 (all area 2). B-N5 points to B2.
9. **L317 and L397 with K1**: R3A3-T1 and S106-T11 (area 3) and the held points on those lines go with K1 (§3.5).
10. **`claims_b.py` DEP**: S2's P2 and S4's P6 (optional, `DEP["Episode"]`) edit the same table.
11. **D0.2**: S4's P6 (i) and S6's P6 (ii) edit it together.

## 7. Notes for the orchestrator

- **Harness.** This step names no harness job: rule 4 keeps the tabulation with Opus, no Sonnet agent (S46). The rule's table lists `r4 key grep` "before every commit of the round" as a harness job; with no Sonnet agent at this step, this agent ran the orchestrator's key pattern itself before the commit (file names only; none listed): a departure from the table, recorded where it happens (lesson S19). `tabulation.py quote` was used as a tool (rule 4).
- **Rules 1, 2.** Only the four `.response.txt` were opened. The returns' commit (2c55cbb) records 4 of 4 accepted on pass 1, no key in any output, every sandbox unchanged; the receipts were not opened here, so that is not checked here.
- **New inventions named, unnumbered** (rule 6: numbered after I191 at integration): (a) W5, whether D16.XV's Uses is read at symbol level or at instance level; (b) B4, which contract "the production contract" names at L271 ("an invention of the step's"). Named existing entries: I20's other choice (S-δ), I184 (b) (B9), I191's other readings (W-N6, C-N6), round 2's C01 ("never ruled on", C-K2).
- **Not run** (rule 3: the checker runs each before ruling): B11's (a3); B12's FC84.new3; B14's path; R3A1-T5's witness; W's P4, P5; S's P2, P6 (code), P7; C's NC1, NC3, NC4 (C2), NC5, NC6 (C1).
- **Ids.** The cases reply's K1–K4, K6 are written C-K*; the addendum's K1 is §3.5's item; the text's (K1) is Bearing. The structure reply's "S13" ((a), FC31 row) is defined nowhere in it; read as its P5, N2 (r99, r117).
- **Labels read.** The breaker's "examined, no fix" (B9) counted as a finding (it says Pin at one pair "is not 'the answer written in' there"); its "held" and "held, with a note" (B13) not counted. The maths_words rows "other (mandated)" (S106-T3, S106-T6) counted by round 3's rule (verdict other), each with the reply's "none".
- **Areas decided.** C-K3: the only text line it names, L31, is its ground for saying the text is not at fault; counted by the claim it attacks (FC23.new2 (a), FC23's family, L255/L273), area 2; with L31, area 1. S-κ tie 1:1 (D5.1 L231 [2]; D16.XV (Elim) L540 [3]) → area 3, the definition P8 changes. S2 2:1, S-f 2:1, S-d 4 of 7 definitions: area 3. W5 names L536, L538: area 3.
- **Register only.** W5's proposal is a register entry alone; rule 16: not a move.
- **Names.** B4 and C-K1 name the τ′ of the case printout by an outside reader's name; who made a point decides nothing (rule 10).
- **K1.** No reply names the myth about winter (grep of the four replies: 0 for "winter", "myth"); the briefs did not ask (addendum 3). The item stands as the addendum writes it (§3.5).
- **S49**, committed while this file was filled (53c5e1b), keeps the code runnable and tested, "in a state where it can be used outside the review rounds" (Claude's reading); it bears on B14, W6 and S1 (§6, 3). Read here after S20–S48; it changes nothing in the tabulation.
