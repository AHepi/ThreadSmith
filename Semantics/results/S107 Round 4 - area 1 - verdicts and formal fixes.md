# S107 Round 4 - area 1 (L1-L228, Parts 0 to IV): verdicts and formal fixes

*Checker of area 1 under rule 5 of `results/S107 Round 4 - how the replies will be read, written before sending.md` and its addendum (both read whole first): a fresh Opus 5.5 agent that built nothing of this round, 28 September 2026. Findings: the 15 the tabulation (`… tabulation of the replies, before any ruling.md`, §0) assigns to area 1, each passage read whole in its `.response.txt` (breaker r48-r72, r103, r107; maths_words r11-r16, r42, r81, r93-r109; structure r15, r47-r48, r92-r99, r117, r121; cases r56-r58, r112-r121, r157-r159, r165, r170, r174). K1 (the winter-myth knock-on) is area 3's (tabulation §0, §3.5; addendum 1): not ruled here. Text under review: `tests/106 The semantics, standing alone, without the written-in test.md` (md5 c7af964c329ab7959243405d394e6574), not written. Maths: `results/S106 The written-in test taken out/` (core 40d7c80ec78574794962fece34a4cb51, claims c0884083daae9b95be0c36d111d71019, not written). Program copy: `results/S107 Round 4 - maths after the reading/area 1 model/` (copied from `model after S106/`, every md5 checked equal before any change). Runs: `… maths after the reading/area 1 - runs.txt`. Text changes: `… maths after the reading/area 1 - text changes.json` (none). Expected claims for the harness: `… maths after the reading/area 1 - expected claims.json`. Decisions S20-S49 read; S23, S40, S41, S43, S44, S45, S47 bind every row. "Model" here means only a small structure the program builds, or the program's folder; for what the theory judges, "candidate" or "explanation" (S43).*

Codes (as rounds 2 and 3): **M** holds against the maths or the program; **W** against the words; **I** against an invention only; **N** does not hold. Rule 3: every computation a reply marks not run was run before its row (runs §3). Rule 10: agreement among replies counts for nothing.

## 1. Verdicts (one row per finding)

| # | finding | lines | v | why (one line) | fix |
|---|---|---|---|---|---|
| 1 | B11 = B-N6 | N6: L13, L55 | I | I191 writes S47's "no question about the brief occurred to the agent" as "one contract throughout, no criticism (D9.10) aimed at the brief"; B11's (i) (a question, no defect alleged) and (ii) (a criticism used as a given, no asking; S27) part the two only if a question-occurrence is a Θ label apart from criticism (R4A1-01 (d)), a reading no register entry records; the text's nearest notion is a question found (L15, L155; L161 "another question with its own contract"), a third reading (R4A1-01 (e)); under D13.8 as S41 has it, Con and Build at the output are the same under all three | R4A1-01 (register); FC84.new1 (a3) (test part; run: as claimed). B11's restated gloss not taken: rule 11, second limb (it writes the bridge as "no criticism (D9.10) aimed at the brief" where S47 writes "no question about the brief occurred to the agent"). B11's (a3) code run as written (runs §3.1: both rows as B11 expects) and not taken as is: its "asked" is a hand-set tag compared with nothing computed (lesson S39); its two cases are (a3)'s (i), (ii) |
| 2 | W-N6 = W8 | N6 | I | as row 1 (W: "the gap is in the encoding of 'a question occurred', not in Con") | as row 1. W's P5 run as written (runs §3.2): on its own case it returns yes (its topic string "what the brief's load case means" does not begin with the brief's key), not the no W expects; with the question's target keyed as crit's z is, no. Taken as `no_question_about_brief` (quest[o] = the target of the question that occurred), in (a3) |
| 3 | S-N6 = S5 | N6 | N | NoBriefQuestion's content is in the core, D12.2's [S47] note, "(one contract throughout, no criticism aimed at it, [I191])"; the name is FC84.new1's own label; no definition reads it (S47); D9.10's z is "a target", and L73 names "a contract" among the targets | none. P3 (D12.2.new) not taken: rule 11, second limb (tabulation "check"): it would define in the core the bridge's "no question about the brief occurred" as "no criticism aimed at the brief", one of two readings that part ways (FC84.new1 (a3)), for a notion no definition uses |
| 4 | C-N6 = C-K6 | N6 | N | no defect claimed ("a reading tag no conjunct reads"); NC4 run as written (runs §3.3): NoBriefQuestion no, Con [yes], Build yes, as C expects | none; NC4 is (a3)'s case (iii) |
| 5 | B-N2 | N2: L61 | M | FC31's statement: "'The four conditions' at L61, L231 and L536 are the four headings"; L61 has no such phrase since R3A1-T1 (it writes Account(ℰ) ∧ ¬Dec(t), D16.XV); "four conditions" stands at L231 and L536 only | F1 (FC31 re-based) |
| 6 | W-N2 | N2 | M | as row 5 | F1. W's P2 not taken as worded: it keeps "L520's three sources … Fid⁺ (I49)", stale since round 2 (A3-L520.1; now S106-T12): L520 writes (E)'s five conjuncts |
| 7 | S-N2 | N2 (and L520) | M | as row 5, and FC31's L520 sentence stale (L520: "Account, from (F1)∧(F2)∧(A)∧Dependence∧NonVacuous (E)"; D5.7's Vague note: Fid⁺ open only at L630 after R3A1-T5 settled L220) | F1 (S's P5 in substance) |
| 8 | C-N2 = C-K4 | N2 | M | as row 5 | F1 (C's M1 keeps the stale L520 sentence; its "status stays NT" kept) |
| 9 | R3A1-T1 | L61 | N | "more" is Q2 (S41) written in: the declared copy meets (E) and is not an explanation (FC30.new1 (a), run: as claimed); the reply proposes none | none |
| 10 | R3A1-T4 | L69 | N | as row 9 | none |
| 11 | R3A1-T2 = W1 | L49 | N | "more" is what round 3 ruled (its area 1 rows 16-19, W: L49's words said less than Account ∧ ¬Dec) and wrote as R3A1-T2; on a contract of relabelings no candidate with (A) and τ(1) = 1 meets Dependence (FC21 (a), run H), so components can respond as the target does with no account there; the reply proposes none | none |
| 12 | R3A1-T5 = W2 | L220 | N | witness run (runs §3.4): τ(a2)·τ(a1) = a21 ≠ c = τ(a2·a1), (F1) and F2eq at every pair: Viol (D12.7) no at every pair, Hom no, Faithful_C no. The replaced words and D12.7 differ only under I50's registered other choice "the whole of (F2), homomorphism clause included" (I18's "the clause counted at each pair"), which D5.7 closes ("Hom is a condition on τ as a whole, never at a pair") and R3A1-T5 settled at L220 (round 3, rule 6) | none |
| 13 | R3A1-T6 | L201 | N | "less" is what R3A1-T6 did and S47 keeps (D12.2's [S47] note): the replaced words put criticism in every constructed history and none in a selected one, which D12.1, D12.2 do not carry; FC84.new1 (a1), run: Con with no criticism | none |
| 14 | W-b | L13 | N | I190 fills the whole phrase "an episode of conjecture and criticism" (it names D13.8's episode, in which Con's construction trace prepares t), not " and criticism" alone; the conjecture is the trace, as the reply says; nothing turns on it; no proposal | none |
| 15 | C-K2 | L199, L193 | N | T2's old span is not in the text (tabulation §2; rule 15): its first sentence was round 1's, deleted in round 2 by T10, which answered C01 (round 2, area 1: C01 ruled W), so C01 was ruled; L199 now reads "Neither of the above. Write Dec(t).", D12.3's Dec by exclusion, which is what C-K2 asks; CT8 run (output md5 d473944e74d2f349b1fdfb83277843cf, as recorded): R2, R4 "neither (declared by exclusion)"; L193's "exactly one of three" is FC12.new1, FC83 (run H) | none |

**Counts.** M 4 (rows 5-8, one point); W 0; I 2 (rows 1-2, one point); N 9. The two "check" marks of the tabulation (B11, S-N6): neither proposal taken (rows 1, 3).

## 2. Formal fixes (old → new; ids kept)

| fix | item | old | new | answers | counted |
|---|---|---|---|---|---|
| F1 | FC31 (statement; NT) | … 'The four conditions' at L61, L231 and L536 are the four headings. L520's three sources cover the four headings exactly when 'fidelity under change' has the wide extent Fid⁺ (I49); with the narrow extent L189 defines, L520 names no source for (A). | (E) has five conjuncts (D6.7); Part V has four headed conditions (D6.8): Component fidelity = (F1) ∧ (F2), Question fidelity = (A), Dependence, Non-vacuity. 'The four conditions' at L231 and L536 are the four headings. L520 writes (E)'s five conjuncts, (A) among them; the extent of 'fidelity' is open at L630 alone (FC104; L220 narrow, R3A1-T5, D5.7). | N2: B-N2, W-N2, S-N2, C-N2 | no: re-based (rule 16): the statement follows R3A1-T1 (L61) and round 2's A3-L520.1 (L520), result NT unchanged |
| — | FC84.new1 (statement) | (a) … (d) as after S106 | the same, and: (a3) which occurrences are a question about the brief is read through Θ (I90): as criticisms (D9.10) aimed at the brief (I191); as question-occurrences, with or without an alleged defect (R4A1-01 (d)); or as a question found (L15, L155, L161), operative at its occurrence (R4A1-01 (e)). The readings part ways (a question with no defect alleged; a criticism used as a given with no question; a question found and operative) and agree on (a1)'s chain; under D13.8 as S41 has it, Con and Build at the output are the same in every case, one fixed point each (T′): no computed value reads the labels; under L55 as text 104 words it, only a recorded change of contract moves Con, as in (b) | N6: B11, W-N6, C-N6 | no: a new test part |

No definition of the formal core changes. D12.2's and D13.8's [S47] notes stand as written.

## 3. Code (in `area 1 model/`)

| file | change | fix |
|---|---|---|
| model/claims_s41.py | `no_question_about_brief(qs, quest)`, beside `no_brief_question`: R4A1-01's reading (d), quest[o] the target of a question that occurred at o (Θ by hand, I90); nothing in (R), Sel, Con, Dec, Episode or Build reads it | R4A1-01 |
| model/claims_s41.py | FC84.new1 (a3): six cases on (a1)'s chain (base; B11 (i); B11 (ii); C-N6's NC4; a question found at o1 and operative there, the change back to the brief recorded (iv-r) or not (iv-u)); the three readings computed from the labels and contracts (I191 yes, yes, no, no, no, no; (d) yes, no, yes, no, no, no; (e) yes, yes, yes, yes, no, no), Con and Build from the chain under T′ and both episode readings; as claimed iff the readings are so, S41 gives one fixed point with Con yes and Build yes in all six, and L55 gives Con no, Build yes in all but iv-r (Con yes: a recorded change, as (b)) | row 1 |
| model/claims_a.py | FC31's not-tested statement: "L61, L231, L520, L536" → "L231, L520, L536"; label kept | F1 |

Whole suite, scale 4, cap 45 (runs §1): baseline on the unchanged copy 128 hold, 2 counterexamples, 7 not tested, of 137, every claim and part equal to `formal claims, after S106.json` (after_s106); after area 1: 128 hold, 2 counterexamples, 7 not tested, of 137, no error; one claim differs from the baseline, FC84.new1, by its added part (a3) (computed: as claimed); no status changed. Recorded for the harness in `area 1 - expected claims.json` (key area1_r4; 137 claims, parts as (label, kind, status)). Case scripts on the changed copy: `s104_external.py`, `s104_creative_transport.py`, `s106_cases.py` outputs md5-identical to the records (86a67664a9a3584351fd4836a4140b69, d473944e74d2f349b1fdfb83277843cf, 043aeb3647a9004ae43009a7fed50b4e).

Harness job (rule 5.3), run after this hands back: `tools/sonnet_harness/specs/r4 claim suite, area 1 copy.json` (25 inputs with md5s, the copy's 23 files, the record and the round-3 core FC14 and FC32.new1 read; the whole suite compared with `area 1 - expected claims.json`, key area1_r4, counts H=128, CEX=2, NT=7, of 137; a spot re-run of ten claims). Its inputs were checked here by `run_task.py --phase validate` under a run label of its own (a1-selfcheck: ok, no command run); its brief printed under `--run r4-reading`.

A layout fact, not a fix here (area 3's B14, W6, S1): from this folder FC14 and FC32.new1 find no `formal core, after S106.md` at the places they try and read `results/S105 Round 3 - maths after the reading/formal core, after round 3.md` instead (runs §1); both hold, as recorded.

## 4. Text changes (`area 1 - text changes.json`)

None. No finding of area 1 holds against the words (W 0); rows 1-2 rest on an invention only, which changes nothing in the text by itself (rule 6); C-K2's T2 has no old span in the text. Words outside formulas unchanged.

## 5. Inventions (provisional id; rule 6: numbered at integration after I191)

| id | fills (line; item) | choice | other choices | why this one | used by |
|---|---|---|---|---|---|
| R4A1-01 | S47's "a question occurs as potentially important and worth investigating", for the bridge (S41 Q6: "the brief never changes during the work"; I191's "no question about the brief occurred to the agent"); L13, L55 | recorded, not chosen anew: I190/I191 stand (a question about the brief that occurs is read, through Θ, as a criticism (D9.10) aimed at the brief) | (d) a question-occurrence is its own Θ label, apart from criticism, with or without an alleged defect, and a criticism can be used with no question occurring (a claim taken as given, S27) (B11, W-N6); (e) a question that occurs is a question found (L15, L155; L161: "another question with its own contract"), operative at its occurrence, so q(o) is not the brief there (this checker); I191, (d) and (e) part ways (FC84.new1 (a3): (i), (ii), (iv)) | no value of (R), Sel, Con, Dec or Build reads the labels, and under D13.8 as S41 has it Con and Build at the output are the same under all three (FC84.new1 (a3)); S47: "The math doesn't ask for anything." | `claims_s41.no_question_about_brief`; FC84.new1 (a3) |

## 6. Owner questions

None. Whether every question that occurs to an agent as worth investigating alleges a defect is left open by S47 ("The agent does when a question occurs as potentially important and worth investigating") and by the texts; a computation settles that nothing the maths computes turns on it (FC84.new1 (a3): under D13.8 as S41 has it, Con and Build the same under all three readings), which is S47's own point. (a1)'s chain holds no criticism and no question of any kind, so it is the owner's bridge under every reading, S47's "no questions occured to the agent" included. Rule 12 sends a question only where neither the texts nor a computation settles it; no line is held.

## 7. Parked

None. No finding of area 1 bears on what hard to vary covers or on what makes an explanation a bad one (P1 to P8).

## 8. Quotations relied on (rule 15; each found)

L13 "produced by an episode of conjecture and criticism"; L15 "can be found as well as answered"; L55 "An episode is a history in which every change"; L61 "(Suff) sufficiency of \(\operatorname{Account}(\mathcal E)\land\neg\operatorname{Dec}(t)\) (D16.XV)"; L73 "a question, a contract, a transport, a method, an attention policy, can become a target"; L193 "exactly one of three provenances"; L199 "Neither of the above. Write"; L201 "Neither provenance is reducible to the other: (D12.1, D12.2)."; L155 "found* a question requires" (with ρ_p = constructed); L161 "Exposing the defect is another question with its own contract."; L231 "exactly when the following four conditions are met"; L520 "Account, from (F1)∧(F2)∧(A)∧Dependence∧NonVacuous (E)" (as formula); L536 "all four conditions of (E)"; S47 "The math doesn't ask for anything."; D5.7 "Hom is a condition on τ as a whole, never at a pair"; I50 (register) "the whole of (F2), homomorphism clause included". Replies' quotations not found (tabulation §2): C-K2's T2 old span (row 15), ruled on the text.

## 9. Moves (rule 16, counted strictly)

| counted | n |
|---|---|
| formal (changed or new definition, changed claim or encoding answering a finding that holds, change to the program's reading of a definition) | 0 |
| text | 0 |
| **moves** | **0** |

Not counted: F1 (FC31 re-based, NT unchanged); FC84.new1 (a3) and `no_question_about_brief` (a new test part); R4A1-01 (register entry); no owner question, nothing parked.

## 10. Pairs of fixes that bear on one another (for integration, rule 7)

- R4A1-01 and FC84.new1 (a3) with area 3's B12 ((EX): CompleteCritical's criticism, D13.8's [S47] note "because the agent asked", I190): the note reads a criticism as the agent's asking; R4A1-01 records the reading in which a question can occur with no criticism. Neither changes a value of (EX); both bear on how D13.8's note is worded.
- F1 (FC31) with area 3's N4 (L536 "the four") and area 2's N5, B2 (D6.5, the heading at L255): FC31 names D6.8's headings; a change to D6.5 or D6.8 re-bases FC31 again.
- `model/claims_a.py`: my hunk is FC31's return line; area 3's B14, W6, S1 edit FC14's `tries` list in the same file and `claims_r3a3.core_def_ids` (different hunks).
- `model/claims_s41.py`: my hunks sit beside `no_brief_question` and inside `fc84_new1` after the (a) loop; area 3's B12 (FC84.new3, if made) may add to the same claim family.
