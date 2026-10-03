# S106 — the written-in test taken out: what changed

*Written on 28 September 2026 by a Claude subagent (Opus 5.5), the records step of log S106 (decision S48), from the files named below; it ruled on nothing. Input text: `tests/105 The semantics, standing alone, after round 3.md` (md5 da9a30cd052d46f2a5ead259cea97d3c, unchanged). New text: `tests/106 The semantics, standing alone, without the written-in test.md` (md5 c7af964c329ab7959243405d394e6574, 632 lines; checked). Where `S106 report.md` and the second checker differ, the second checker's file is the later and governs (its md5s, moves and D6.11). Terse by decision S40. Obeys decision S23 except where it quotes the owner. Nothing here is settled (S28).*

## In brief

- **The owner's words.** A candidate with the answer simply written in is an explanation, a bad one (S44); the test comes out "everywhere" (S45). The maths asks for nothing; the agent asks (S47).
- **Removed.** NC1, the written-in test, from (E) (D6.5, D6.7); every sentence of the text that stated its result or used it as a ground for ruling out.
- **Kept.** Dependence (NC2): the answer depends on the commitments at all. The exclusions of tables and reversed calculations, which rest on (F1) and (F2). The block on arguments whose premise is their conclusion. Slot and Pin (D6.3), as content criticism can point at.
- **Cases.** Of 28 worked cases, 10 move to meeting (E), 5 more under readings round 3 never adopted, and 13 are unchanged.
- **S47.** " and criticism" restored at L13 (a checked revert). The bridge re-encoded as "no question about the brief occurred to the agent", with and without a criticism of an earlier design.
- **Review.** A fresh Opus 5.5 critical review (the first after Fable, S42) raised 1 objection that matters and 4 minor ones. A second checker withdrew D6.11 (b), (c) ("the questions it leaves open"; parked, P8) and kept the pin.
- **Claims.** 125 / 2 / 7 of 134 → **128 / 2 / 7 of 137**. No earlier status changed.
- **Text.** 14 changes on 11 lines, no prose added. Words outside formulas **15,322 → 15,204**.
- **Moves: 16**, so round 4 follows (log S107, being built).

## 1. The owner's words

| decision | commit | words | here |
|---|---|---|---|
| S44 | 810459f | "Neither. … In either case, it is an explanation. Just not a good one, and partly for the reasons I just explained." | the two-part sign is an explanation, a bad one |
| S45 | c7e619f | "Yes, take the test out" ("A written-in answer never stops something being an explanation. It only makes it a bad one, through the questions it leaves open. The theory changes everywhere the test is used.") | NC1 out of (E), everywhere |
| S46 | 5ee3827 | "maybe analysis isn't something it should be used for. Unless it's something that genuinely helps." | Sonnet only for mechanical jobs; tabulation and records with Opus |
| S47 | ee03765 | "The math doesn't ask for anything. The agent does when a question occurs as potentially important and worth investigating. … it sounds like you're making a stronger claim than \"no questions occured to the agent\"." | §5 |
| S48 | 3f77cbc | "These round X files are very helpful. Keep them coming." | a plain file for every round and step; this record and file 106 |

S44 to S46 were first logged in S105; S47 and S48 are first logged here. S44 was Claude's reading of one example, confirmed with the owner (S45) before it was applied generally.

## 2. The map: what was removed, what was kept

From `S106 report.md` §1 (24 rows, M1–M24); lines are those of texts 105 and 106.

| use | removed / kept | why |
|---|---|---|
| NC1 (D6.3): the answer not an unanalysed input or component, "structural at the declared grain" (L255 s2–s3) | **removed** from (E) (S106-T3); Slot and NC1 kept as defined notions | it only says "the answer is written in" |
| "independent" boundary conditions (L255, NC0) | deleted (S106-T2; I187) | vacuous as I23 reads it; its other reading is the test on a boundary |
| L273: "p because p" fails; a restating component fails; packaging does not repair | **removed**; now the pointer "(D6.3, FC23, FC24)." (S106-T6) | states the old result |
| L317, L397: an argument with no test finding that a candidate "assumes its own answer" rules it out | clause deleted (S106-T8, T10) | the test used as a ground for ruling out (E) |
| L536 (Suff): "conclusion-as-premise fails non-circular dependence" | clause deleted (S106-T13) | states the old result |
| L397's "as non-circular dependence reads identity (Part V)" | → "(D9.7)" (S106-T11) | its target is deleted |
| the name "Non-circular dependence" (L255, L257, L262, L275, L343, L520) | → the formal name Dependence (S106-T1, T4, T5, T7, T9, T12; I188) | the name is the test's |
| NC2 (D6.4): a contrast lost when a block of Γ is deleted | **kept** as Dependence (D6.5) | not the test: written-in candidates meet it wherever their answer varies (FC23 (b), (e); the one-part sign); it fails a mechanism and a lookup alike where the commitments carry no contrast (FC21, FC22, FC29) |
| L269: E_tab fails; E_enc "is an account when it meets the other conjuncts" | kept | E_tab fails (F1); E_enc's sentence still holds, and now E_enc meets (E) (FC25.new2) |
| L271, L325: the reversed calculation fails | kept | (F2), direction of production; excluded on L325's contract even under Mimo's τ′, where NC1 also failed (FC27) |
| L331 "… is circular"; L397's block on a premise that is the claim's denial ("p because p" as an argument) | kept | about arguments, not explanations: (E) never read L331 (FC60 (a)); the block is D9.7's (FC72) |
| L339 "a bare denial … is not an account" | kept | (F1) / Dependence |
| Parts XV and XVI (Nec, Elim, Prov, QF; Arguments 1–10) | kept | none uses NC1 |

## 3. Formal changes (`formal core, after S106.md`, final md5 40d7c80ec78574794962fece34a4cb51)

| def | old | new |
|---|---|---|
| D6.5 | NonCircular :⟺ NC0 ∧ NC1 ∧ NC2 | **Dependence :⟺ NC0 ∧ NC2** (⟺ NC2) |
| D6.7 | Acc :⟺ F1 ∧ F2 ∧ A ∧ NonCircular ∧ NonVacuous; the grain ℓ an argument | Acc :⟺ F1 ∧ F2 ∧ A ∧ Dependence ∧ NonVacuous; no grain; round 3's (E) = Acc ∧ NC1 |
| D6.8 | heading "Non-circular dependence" | "Dependence" |
| D6.3 | Slot (NC1's 'every' quantifier) | Slot kept; **Pin**(ℰ,k;a,b) written in as its clause at one pair (I184): at a pair (a,b) of Det_C, part k's relation by itself fixes the answer; Slot = Pin at every pair (FC23.new3 (a), 25,920 models) |
| D6.11 | — | built by S106 (a) Pin, (b) the further question at a part, (c) LeavesOpen; **withdrawn** by the second checker: (a) moved to D6.3, (b) and (c) deleted and parked (P8) |
| D18.1 | NonCircular → (O), (Q), C, ℓ, δ | Dependence → (O), (Q), C, δ; Slot node; DEP 83 nodes |
| D12.2, D13.8, §12 Vague (S47) | r3 mark "Con with no criticism" | withdrawn; I190 |

Program (`model after S106/`, from round 3's): `core.dep()`; `core.account(reading=)`, "S106" by default (conjuncts F1, F2, A, Dep, NonVacuous; NC1 reported, not a conjunct) or "r3", also by env `S106_ACCOUNT_READING`; `pin`, `pins`. `RelQuery`, `further_question` and `leaves_open` were built and then deleted. New `claims_s106.py` (FC23.new2, FC23.new3, FC25.new2) and `s106_cases.py`. `claims_s41.py` has `no_brief_question`.

## 4. The cases that moved (`s106_cases.py`, output md5 043aeb3647a9004ae43009a7fed50b4e, rerun for this record: identical)

Round 3's (E) under its default reading 'every' against (E) after S106. Readings in brackets: every, some, some-exempt, some-exempt-set.

| moved (10) | round 3 | after | why it failed before |
|---|---|---|---|
| the encoding table E_enc, pole C1; and C2 (L269; FC25.new2) | F,F,F,F | T | NC1 (slot 'tab') |
| "p because p": the pole's L written into one component (L273; FC23) | F,F,F,F | T | NC1 |
| M1, M2, M3, the readers' disguised lookups (FC23 (c)) | F,F,F,F | T | NC1 |
| the hand-turned vane, "north when turned" (R3-Q1) | F,F,T,T | T | NC1 |
| E8: the identity candidate for the criticism question p_δ (L590, L377; FC107) | F,F,F,F | T | NC1 |
| the owner's shop sign, **one part** (red on Monday, blue on Tuesday) (FC23.new2 (b)) | F,F,F,F | T | NC1 |
| the reversed calculation under Mimo's τ′ on a contract of H settings only (review, objection 5) | F,F,F,F | T | NC1 alone; on L325's C1 (F2) still excludes it |

**Moved under another reading only (5):** the pole's forward organization on C2 and on C3; M5; the eliminative construction (FC62's encoding); **the owner's two-part sign, as S44 words it** (FC23.new2 (a)). Each was T under 'every' in round 3, F under at least one reading never adopted, and is T under all four now.

**Unchanged (13):** the pole on C1; the reversed calculation, production C1 (fails F1, F2, A) and under τ′ on C1 (fails F2); identification C_id (meets); E_tab on C1 and C2 (fail F1); the relabeling contract (fails F2); M13, the owner's weathervane; the second eliminative encoding; E9's S1 with t1 and with t1∘ψ; the palette sign (I189). E6 (FC63) is computed as before: (c-i) not as claimed, (c-ii) as claimed. E2, E3, E4, E7 and Part VI's route examples compute no candidate's (E).

"p because p" now meets (E) wherever its answer varies. It fails Dependence only where every candidate does (no contrast on C, FC21, FC22), or where a background part leaves it no solution, and there (A) fails as well. It is an explanation when its link was found or worked out, and not when the link was declared (S41 Q2; FC30.new1 (b); FC23.new2 (f), now computed).

## 5. S47 (applied inside S106, fc64e29)

| where | old | new |
|---|---|---|
| L13 | "produced by an episode of conjecture;" (round 3's R3SC-L13) | "produced by an episode of conjecture and criticism;" (S47-T1, kind revert; checked against round 3's change list and against L13 of text 104, byte for byte) |
| FC84.new1 (a), the bridge | o1 ≺ o2, one contract, Con, no criticism encoded | (a1) no criticism in the history; (a2) a criticism of an earlier design before the one built. In both, no question about the brief occurred to the agent (NoBriefQuestion, I191), and Con holds. With the criticism aimed at the brief, NoBriefQuestion fails and Con still holds |
| D12.2's round-3 mark "Con with no criticism" | stood | withdrawn; I190: L13's phrase names D13.8's episode, which includes one in which no question occurred to the agent; the maths asks for no criticism event; a criticism, when there is one, is the agent's asking |
| FC32.new1 (f) | "the criticism L13 names is (EX)'s, not construction's" | computation unchanged; the reading restated as the row above |

Kept: L201's pointer, which claims nothing about criticism. Also kept, with an [S47] note: §12 Vague's round-2 mark ("D12.2 asks no criticism") and D13.8's CompleteCritical. Not edited: round 3's second-checker file, plain file 105 and log S105 (records of round 3). Plain file 105 says "the maths asks for no criticism, and the bridge counts as worked out with none"; the owner found this a stronger claim than the owner's answer, and this record and file 106 correct it. The suite after S47: 128 / 2 / 7 of 137, unchanged; FC84.new1 (a1), (a2) as claimed.

## 6. The critical review, the decisions and the second checker

- **Review** (cdffbba; a fresh Opus 5.5 agent that built nothing of S106; S42).
  - Reruns agree: 128 / 2 / 7 of 137. With round 3's (E) (`S106_ACCOUNT_READING=r3`), 126 / 4 / 7: only FC23.new2 and FC25.new2 change, the two claims that say written-in candidates meet (E).
  - The text md5 and 15,205 words agree.
  - Its own cases: a kettle "whistle part that whistles when heated" meets (E) after S106 and failed round 3's.
  - Nothing more to remove. "p because p" matches S45. Neither knock-on conflicts with the owner's words. S47 is as applied. No owner question.
  - **Objection 1 (matters):** D6.11 (b), (c) build "the questions it leaves open", which the text never uses and which S44's reading puts under what hard to vary covers (parked). Computed: LeavesOpen reads a candidate only through dom τ × dom σ, so every candidate for the sign, the palette sign with no pin included, leaves p^r open. (b) is (F1) restated at a pin.
  - **Minor objections:**
    - 2: L273's formula is not the sentence's formal statement.
    - 3: FC23.new2 (f), (g) were set by hand.
    - 4: I186's "true".
    - 5: a moved case was missed.
- **The orchestrator's decisions** (cbbcaf5; Claude, under S13, not the owner): all five objections to one second checker, leaning to the review's fixes; tests/106 rebuilt by program; then this record; then round 4.
- **Second checker** (b73d9bf; a fresh Opus 5.5 agent):

| # | ruling | result |
|---|---|---|
| 1 | review's fix | D6.11 withdrawn whole; Pin kept as D6.3's clause; I185, I186 withdrawn; FC23.new2 (c)–(e), FC23.new3 (b), (c), D⁺, p^r and the node Open deleted; P8 rewritten with S44's and S45's words |
| 2 | own fix | L273 → pointer "(D6.3, FC23, FC24)." (FC23.new2 has no source line) |
| 3 | review's fix | FC23.new2 (f) computed (`provenance_of`, `expl_ruled_out`, `suff_defeats`); (g) a look |
| 4 | review's fix | moot for I186 (withdrawn); the report's "stays true" read as "still holds" |
| 5 | review's fix | the row added: 10 move (was 9) |

The suite after the second checker: 128 / 2 / 7 of 137, 516.5 s, no traceback. Only the ruled parts of the printout differ: FC23.new2 has 4 parts (was 7), FC23.new3 has 2 (was 4), FC14 reads 118 definition lines, FC32.new1 reads 114 paragraphs, and DEP has 83 nodes.

## 7. Claims (scale 4, cap 45 s, PYTHONHASHSEED=0)

| run | hold | counterexample | not tested | of |
|---|---|---|---|---|
| after round 3 (rerun here) | 125 | 2 | 7 | 134 |
| (E) after S106, claims as round 3 left them (the raw effect) | 124 | 3 | 7 | 134 |
| after S106, S47 and the second checker | **128** | **2** | **7** | **137** |

The raw effect: FC23.new1 H → CEX (it read (E)); it is restated to read round 3's (E) as Acc ∧ NC1_q, with (h): (E) after S106 is the same under all four readings. New test claims: FC23.new2 (the owner's sign), FC23.new3 (Slot and Pin), FC25.new2 (E_enc), each H. Counterexamples: FC23 (its (b) as stated), FC63 (c-i). Not tested: FC31, FC35, FC89, FC94, FC104, FC105, FC110. Hypotheses met rose (FC37 120 → 1661, FC46 66 → 962, FC51 15 → 265): more candidates meet (E). `s104_external.py` and `s104_creative_transport.py` outputs are identical to round 3's.

## 8. The text

`apply text changes.py --rebuild` from tests/105: **14 changes on 11 lines** (L13, L255 ×3, L257, L262, L273, L275, L317, L343, L397 ×2, L520, L536), 0 refused.

| kind | n | ids |
|---|---|---|
| deletion | 5 | S106-T2, T3, T8, T10, T13 |
| span replaced by its formal name | 6 | S106-T1, T4, T5, T7, T9, T12 |
| pointer | 2 | S106-T6, T11 |
| revert | 1 | S47-T1 |

- Checks: each span is unique and equal byte for byte; each undoes byte for byte; 632 lines. The S95 scan gives 80 → 80 (0 new; S23's list 0), and the S96 scan 196 → 196 (0 new). Headings 55, terms 154, formulas 23, none missing. One term is replaced on purpose ("Non-circular dependence."). L255 is no longer held.
- **Words outside formulas: 15,322 → 15,204** (−118); without S47's revert, 15,202. All words: 16,221 → 16,102.
- tests/106 md5: 0e56b581… (S106) → 7d58eeec… (with S47) → **c7af964c329ab7959243405d394e6574** (second checker). Only L273 differs between the last two.

## 9. Inventions (`inventions register - addendum after S106.md`, md5 4c19472b4f097fc5698e8e4722017100)

I184–I191 are numbered; 6 are in use.

| I | what | standing |
|---|---|---|
| I184 | Pin: a part that by itself fixes the answer at one pair | in use, now in D6.3 |
| I185 | the further question at a part | **withdrawn** (P8) |
| I186 | LeavesOpen | **withdrawn** (P8) |
| I187 | L255's "independent" read as the test and deleted | in use |
| I188 | the name Dependence | in use |
| I189 | the owner's sign encoded (two parts; one part; a palette sign) | in use; D⁺, p^r and the edit "plain" deleted |
| I190 | L13's "conjecture and criticism" names D13.8's episode; the maths asks for no criticism event | in use (S47) |
| I191 | NoBriefQuestion: the brief is the contract throughout, and no criticism is aimed at it | in use (S47) |

Standing changed, not new: I23 (other choice closed), I24 (other choice (a) taken), I25, I28 (the grain out of (E)), I39 (D9.7 alone), I79, I82, I83, I135, I136, I176 (bear on Slot and Pin only; the R3-Q1 quantifier changes no value of (E)). None is a move.

## 10. Parked and owner questions

- **P8 (new)**: the owner's words, S44's "Why blue and not any other colour? …" and S45's "It only makes it a bad one, through the questions it leaves open". What makes an explanation bad, and which questions it leaves open, touch what hard to vary covers (S33, S34). Nothing is built. D6.11 (b), (c) were built and deleted, and the computed reason is recorded with them.
- Kept from P8: Slot and Pin, content with no grade, count or order (S20, S21, S23). A further question stays expressible as a question of its own. P1–P7 are untouched.
- **Owner questions:** none new. R3-Q1 is answered by S44 and S45. Q2, Q6, Q15 and Q23 (S41) are not reversed or weakened; Q6's bridge is re-encoded per S47.

## 11. Moves (round 3's rule 16, strictly; the second checker's count)

| | formal | text applied | moves |
|---|---|---|---|
| S106 as built | 2 (D6.5; D6.11) | 13 | 15 |
| S47 | 1 (FC84.new1 (a)) | 1 | 2 |
| second checker | −1 (D6.11 withdrawn; Pin is D6.3's clause, not a change in form) | 0 | −1 |
| **total** | **2** | **14** | **16** |

The report's 17 is superseded. Not counted: D6.7, D6.8 and D18.1, the DEP and `account` (the D6.5 fix in its other places; 18 if D6.7 and D18.1 were counted apart); restated or re-based claims; test claims and parts; the new case row; I184–I191; P8. The ground of these moves is the owner's decisions, not findings. **16, not 0: the series goes on.**

## 12. Not tested, and unsure

- No outside reader has seen tests/106 or the maths after S106. Round 4 (log S107) is aimed at them.
- One critical review and one second checker ruled the five objections.
- The program tries small models only, and seven claims are not tested. The project's everyday cases were not read again on tests/106.
- Nothing in the theory now says why a written-in explanation is bad. The slot and the pin are content only; the rest is parked (P8).
- Two knock-ons follow from S45's "everywhere" and were not asked:
  - (K1): a criticism whose connection writes its defect in now has bearing when it meets the rest of (E) (FC107).
  - (Suff): its range now includes written-in candidates.
- The conjunct's name is a formula. S40's kinds (delete, formula, pointer) gave no plain-word rename.
- Deleting "independent" (I187) rests on its two readings being vacuous or the test.
- NoBriefQuestion encodes "a question about the brief occurred to the agent" as a criticism aimed at the brief (I191). Which occurrences are criticisms, and of what, is read through Θ (I90).
- An older owner question is touched: file 96's question 2 and file 93's first, on the myth about winter. It asks whether finding, by argument, that a candidate assumes its own answer rules it out on a question about the world. L317 and L397 said yes, as Claude's reading; S106-T8 and T10 deleted that clause. Whether S45 answers the older question is not decided here.
- The report's §12, §14 and §15 md5s, its moves (17) and D6.11 are superseded by the second checker's file. The report's "stays true" is not edited.

## Files

- In `results/S106 The written-in test taken out/`:
  - `S106 report.md` (with its §15, S47); `S106 critical review.md`; `S106 the orchestrator's decisions on the critical review.md`; `S106 the second checker on the critical review.md`.
  - `formal core, after S106.md`; `formal claims, after S106.md` / `.json` and their builder; `inventions register - addendum after S106.md`; `parked after S106.md`; `owner questions after S106.md`.
  - `text changes for S106.json`, `text changes for S47.json`, `apply text changes.py`; `S106 - runs.txt`, `S106 - whole suite, printout.txt`; `model after S106/`; this file.
- `tests/106 The semantics, standing alone, without the written-in test.md`.
- `plain words/106 The written-in test taken out, in plain words.md`, for the owner.
- Commits: snapshots 9dfabe3, c42f024, 90bdb1b; c23045c (S106); fc64e29 (S47); cdffbba (review); cbbcaf5 (decisions); b73d9bf (second checker).
