# S131 Explanation by construction carried into copies: what changes

*Log S131, 2 October 2026, decision S86. One Opus 5.5 agent doing the whole job (S56, S68; no subagent or workflow), beside the S132 agent in the same working tree. No Avida run; no outside model; no GLM check (S70); no book file opened. **The theory itself is unchanged**: `tests/107 The semantics, standing alone, after round 4.md` (md5 c7af964c329ab7959243405d394e6574, checked before and after), the formal core, claims and program in `results/S107 Round 4 - maths after the reading/`, every S108 to S130 file (S129's copies included: copied, never edited), the decisions file, the S61 terms and `authority/` were read and not written. The third decision was carried into COPIES of S129's copies, exactly as S129 carried the first two. The semantics is cited from text 107 by line ("L536"); in text 131 every line of text 107 stands 24 lines further down (two 12-line notes). The core copy's provisional inventions are I202 and I203 (section 1.2), after S129's I198 to I201, not in the register. Avida is described in the owner's terms (S61).*

**The owner's words (S86)**, after plain file 130 put the choice (keep "explanation" for what was worked out, or keep the theory as it is): "Correct. Knowledge doesn't need to be worked out, explanation does." Earlier words that bear on it: S41 (Q2: a candidate meeting (E) whose transport is simply declared is no explanation); S44 and S45 (the one-part shop sign "an explanation. Just not a good one"); S57; S59 ("the explanation kind comes next"); S85 ("It seems like it counts as knowledge, not explanation"). Claude's reading (S86): "explanation" is kept for an account whose transport was constructed; an account whose transport was selected is a representation, what the owner calls knowledge (evolved knowledge where selected, created knowledge where constructed), and not an explanation.

## 0. In short

- **Written in, on copies only, in S130's smallest wording.** Text 131 (a copy of text 129): "Account(ℰ) ∧ ¬Dec(t)" becomes "Account(ℰ) ∧ Con(t)" at L17, L49, L61 and L69; (Suff) at L536 reads "with a transport whose provenance is constructed"; Argument 6 at L47 reads "every explanation and every creative attribution requires it". Only those six lines differ from text 129 (checked by program). Core copy: D16.XV's owner's condition is Acc(ℰ) ∧ ¬Con_β(t) ⇒ ¬Expl_β(ℰ) and (Suff)'s defeat condition ∃ℰ [Acc(ℰ) ∧ Con_β(t) ∧ ∃α ∈ X_j(Expl_β(ℰ)): Acc ∉ Uses(α)], read at the declared boundary (S129's K1); FC30 is untouched: (E) still takes no provenance. Program copy: a third switch beside S129's two, so all eight settings run.
- **The suites: no flip.** The whole suite (142 claims) and the three worked-case scripts, run under all eight settings of the three switches, give S129's statuses and part statuses exactly (133 H, 2 CEX, 7 NT) once the two claims that encode the owner's condition and (Suff) are reworded in the copy (section 2.1). **As written** (round-4 wording checked against the decision), two claims would flip to COUNTEREXAMPLE FOUND: FC30.new1 at parts (a), (b), (c), (e), (g), and FC23.new2 at part (f), each because it states that a selected transport is treated as a non-declared one. Of the 142 claims, six mention Dec, Expl or (Suff) (one of them, FC72.new2, only as "Dec" for December); three are touched by the decision (FC30.new1, FC23.new2, and FC32.new1 through D18.1's graph); FC12.new2 and FC78 are about provenance alone and are not.
- **Where the decision bites**: exactly where an account's transport is **selected**. Before S86 such an account was an explanation by (Suff)'s conjecture; now it is no explanation, by the owner's condition. Declared and constructed accounts keep their verdicts. In the narrower-boundary sweep, FC30.new1 and FC23.new2 build 21 distinct histories; the verdict changes on 5 of them on the whole history (selected there) and at 5 of 21 narrower boundary pairs; one of these is new: the student's copied formula at the student's own boundary, where Reading C made it selected (section 2.2).
- **The map** (S117's, recounted by program): all three decisions at the S72 boundary **122 / 28 / 18 / 116**, the same counts as S129's "both" and as S130's hand count; no verdict moves, only the wording of R117 (D16.XV, FC30.new1) and R003 (T01). New: with S86 alone (no Reading C), **116 / 34 / 18 / 116**: the two defeat-condition units (D16.XV, FC30.new1) move from "in part" to "exactly", because under S117's readings A and B alike the NOT program is not constructed, so both give "no explanation" (section 4).
- **What it commits the theory to** (section 5): every adaptation in nature is evolved knowledge where faithful and never an explanation; a proof found by blind search is no explanation until someone works it through; learning from a teacher's answers is constructed (S128), so its account can be an explanation (**a question for the owner**); the one-part shop sign is an explanation only if someone worked it out; the student's copy is no explanation at the student's own boundary whichever way the copy is read (S129's open point closes); content learned by rote is no explanation at the learner's boundary, but on a boundary taking in the teacher it inherits the teacher's construction and is one; the creative-episode classes (L528) and question-finding are untouched; the NOT program is evolved knowledge of NOT at the S72 boundary and declared at a boundary taking in Avida's authors, no explanation at either; and the one-transport-two-boundaries conflict S129 found (K1) disappears for selected and declared pairs, but stays for constructed and declared ones, so Expl_β is still needed.
- **Not computed**: whether every created explanation (EX) has a constructed transport; the definitions do not guarantee it (section 5, item 9).

## 1. The changes made

### 1.1 The text copy

`tests/131 The semantics, standing alone, after round 4, with Reading C and explanation by construction.md`, written by `tools/s131_write_the_text_copy_with_explanation_by_construction.py`: it checks text 107's md5, applies six exact replacements to text 129 (each must match once on its line, and each line must still be text 107's line, which none of S129's changes touched), puts a dated 12-line note at the top, and checks line by line that, the note apart, only those six lines differ from text 129. Text 107 md5 c7af964c329ab7959243405d394e6574 (unchanged); text 129 md5 f3624126ad21f9fdf01588c6c2351905 (unchanged); text 131 md5 9594298edb1ddf68486202ce0dae2a2a (657 lines).

| Change | Text 107 line | Text 129 line | Text 131 line | Was | Now |
|---|---|---|---|---|---|
| 1 | L17 (the constitutive conjecture) | 29 | 41 | \(\operatorname{Account}(\mathcal E)\land\neg\operatorname{Dec}(t)\) | \(\operatorname{Account}(\mathcal E)\land\operatorname{Con}(t)\) |
| 2 | L49 (grievance 7, mathematics) | 61 | 73 | the same | the same |
| 3 | L61 (where to attack) | 73 | 85 | the same | the same |
| 4 | L69 (fallibility without error-as-work) | 81 | 93 | the same | the same |
| 5 | L536 ((Suff)) | 548 | 560 | "with a transport whose provenance is not declared (Part IV)" | "with a transport whose provenance is constructed (Part IV)" |
| 6 | L47 (Argument 6, "You have replaced explanation with evolution") | 59 | 71 | "and every creative attribution requires it." | "and every explanation and every creative attribution requires it." |

Two notes on S130's wording. S130 section 4.1 said "L17 (twice)": L17 holds the formula once (its other mention of explanation, "the claim that it is an explanation there", carries no formula), so it was changed once, and the program checks that the formula occurs nowhere else in the copy. S130 called the L47 change "two words"; the words added, from its section 4.3 table, are "every explanation and".

Not written in: the owner's two phrases as names of kinds (S130 section 4.2: not needed); "explanation" read at the declared boundary at L536 (S129's K1 proposal), which the core copy carries but the text does not; any change to L13, L201, L211, L528, L538 or L542, which S86 reaches without needing a change (section 5).

### 1.2 The formal core copy

`results/S131 Explanation by construction carried into copies/formal core, after round 4, with Reading C, the graded survival condition and explanation by construction - a copy.md` (S129's copy md5 bb57e39737f541fe20ae3fae0e8185b4, unchanged; S107's core d6e6ec62acbc6ef763e07b7cd7b29540, unchanged; this copy 53829949d16da3ed01d14cf3718b3063), written by `tools/s131_write_the_core_and_program_copies.py`. Every change is marked [S131: S86 …] with what it was; no definition paragraph is added or removed.

| Where | Was (S129's copy) | Now | Invention |
|---|---|---|---|
| D16.XV, the atom | "Expl(ℰ): an atom, no definition uses it" | the same, "read at the boundary β declared for the claim, Expl_β(ℰ) (L524)" (S129's K1 proposal) | I202 |
| D16.XV, the owner's condition | "Acc(ℰ) ∧ Dec(t) ⇒ ¬Expl(ℰ) [owner S41: Q2]: a candidate meeting (E) whose transport is declared is no explanation" | "Acc(ℰ) ∧ ¬Con_β(t) ⇒ ¬Expl_β(ℰ) [owner S41: Q2; S85; S86]: a candidate meeting (E) whose transport is declared or selected at β is no explanation at β"; a construction whose target is held only outside β is declared at β (D12.2 of the copy, I201) | I203 |
| D16.XV, beside (E) | "¬Dec(t) stands beside it (FC30.new1)" | "Con_β(t) stands beside it (FC30.new1)" | |
| D16.XV, (Suff) | "defeated for j ⟺ ∃ℰ [Acc(ℰ) ∧ ¬Dec(t) ∧ ∃α ∈ X_j(Expl(ℰ)): Acc ∉ Uses(α)]" | "defeated for j ⟺ ∃ℰ [Acc(ℰ) ∧ Con_β(t) ∧ ∃α ∈ X_j(Expl_β(ℰ)): Acc ∉ Uses(α)]" | |
| D16.XV, note | – | a consequence, not a change: Expl_β := Acc ∧ Con_β is a common model at every β; the round-4 (Suff) and S86's owner's condition have none wherever an account is selected, so the two lines change together or not at all; with (Nec), Acc ∧ Con_β becomes necessary as well as conjectured sufficient | |
| D14.7 (EX), note | – | a consequence, not a change: no conjunct of (EX) asks Con_β(t_c) (section 5, item 9) | |
| FC30's line ((E) takes no provenance) | | not touched | |

The copy's inventions, provisional (the register is the theory's): **I202** Expl read at the declared boundary, with Con_β; a claim with no boundary declared is read as S129's copy reads it (I198) (other: Expl unindexed; S129 computed that it then has no common model with the owner's condition once a transport has two provenances at two boundaries; section 5, item 10 shows where that still happens). **I203** the owner's condition widened from "declared" to "not constructed", the smallest rung of S130's ladder (¬Dec ⊃ Con ⊃ Build with ExplUse ⊃ (EX)) (others: Build with ExplUse, or (EX) only, if the owner also withholds "explanation" from what is learned from a teacher's answers; section 5, item 3).

### 1.3 The program copy

`results/S131 Explanation by construction carried into copies/model after Reading C and explanation by construction/`: S129's program copy (26 files), 22 byte-equal to S129's, four changed (checked by the builder; S107's program and S129's copy unchanged, by md5 of every file before and after):

- `model/claims_b.py` (S129 6efd639fa44852358cd23f5ac49d3eb7, S131 676cb8def8ba37a356e21764a4bcb388): beside S129's `S129_READING_C` and `S129_GRADED`, the switch **`S131_EXPL_BY_CONSTRUCTION`** (on by default; 0 computes what S129's copy does) and **`S131_CLAIMS_REWORDED`** (on by default; 0 makes the claims check their round-4 wording against the decision, to show what would flip as written; it changes nothing with the decision off); D18.1's node for D16.XV (`DefeatConds`) reads Con in place of Dec when the decision is on.
- `model/claims_s41.py` (S129 fcacbcae7b4665bb97b041d76b749a65, S131 c2cbfa32485274147d492e4f11abf1d2): `suff_defeats` asks Acc ∧ Con(t) ∧ an argument not using (E) at L536 and L17 (S41), and `expl_ok` asks Acc ∧ ¬Con ⇒ ¬Expl, when the decision is on; both then need Con and stop with an error if a caller does not give it, so no caller was missed. FC30.new1's parts pass Con; (a) also checks what its statement in the claims file says of a selected transport (S131 wording: as a declared one; round-4 wording: in all three defeat sets); (b), (c), (e), (g) check their S131 wording (below).
- `model/claims_s106.py` (S129 0a07401b7f1b84e3be05a46b82ff2afc, S131 9ad5d05c2370af7f63d8fa988d581b83): FC23.new2 (f) passes Con, uses Expl := Acc ∧ Con as its common model, and checks that a selected sign is no explanation.
- `model/corefile.py` (S129 962bb729c81bc7b0a851c7dd9544fd71, S131 4dcc56febb29954ed7aa374bb90227de): FC14 and FC32.new1 read the S131 core copy.

The claims adjusted in the copy (statement and check, both shown in each printout):

| Claim, part | Round-4 wording | S131 wording |
|---|---|---|
| FC30.new1 (a) | "with a constructed or a selected transport it is in all three" defeat sets | constructed: in all three; selected: as declared, in Def(L17 as text 104 words it) only |
| FC30.new1 (b) | Def(L17 as text 104) = Def(L536) ∪ {ℰ : Acc ∧ Dec(t) ∧ Expl ruled out} | … ∪ {ℰ : Acc ∧ ¬Con(t) ∧ Expl ruled out} |
| FC30.new1 (c) | Expl := Acc ∧ ¬Dec meets (Suff) and the owner's condition (four values of Acc, Dec) | Expl := Acc ∧ Con meets Acc ∧ Con ⇒ Expl and Acc ∧ ¬Con ⇒ ¬Expl, on the six values of Acc and the three provenances; and the round-4 (Suff) beside S86's owner's condition has no common model (none at Acc with a selected transport) |
| FC30.new1 (e) | the link no pair tried is selected after round 2, "so ¬Dec and Q2's condition misses it" | selected or declared, never constructed, so the owner's condition applies under both D12.1s |
| FC30.new1 (g) | L61's "their" read as necessity of Account ∧ ¬Dec: differs from L538 "exactly on Dec" | necessity of Account ∧ Con: differs from L538 on every transport not constructed (a selected one too) |
| FC23.new2 (f) | common model Expl := Acc ∧ ¬Dec; a selected sign not checked | Expl := Acc ∧ Con; a selected sign is no explanation, as a declared one |
| FC30.new1 (d), (h) | – | pass Con; statement and verdict unchanged |

## 2. The suites' results

### 2.1 The whole suite and the worked cases, on the copy

`tools/s131_run_the_suites_on_the_copy_and_compare.py`: the record's settings, as S129 ran them (scale 4, time cap 45 s, PYTHONHASHSEED=0, `--no-write`), three settings at a time; the three worked-case scripts likewise. Baseline: S129's own printout of its copy under both decisions (its scratch file `s129/suite C on, graded on.txt`). Data: `results/S131 Explanation by construction carried into copies/suite runs.json`.

| Run (Reading C, graded, S86) | Claims: H / CEX / NT | Status or part status different from S129 both | Different from the record (after_round4) | Printed results different from S129 both (times and capped counts left out) | The three case scripts |
|---|---|---|---|---|---|
| S129 both (its own printout; the baseline) | 133 / 2 / 7 of 142 | – | none | – | – |
| on, on, off (this copy computing as S129's) | 133 / 2 / 7 | none | none | FC14, FC32.new1: only the name and md5 of the core file read | byte-equal to S129 both |
| **on, on, on (all three)** | 133 / 2 / 7 | **none** | none | FC14, FC32.new1 (the core file); FC23.new2, FC30.new1 (their S131 statements and rows: Con passed, the selected transport's verdict) | byte-equal |
| **off, off, on (S86 alone)** | 133 / 2 / 7 | **none** | none | the same four | byte-equal |
| on, off, on | 133 / 2 / 7 | none | none | the same four | byte-equal |
| off, on, on | 133 / 2 / 7 | none | none | the same four | byte-equal |
| off, off, off | 133 / 2 / 7 | none | none | FC14, FC32.new1 | byte-equal |
| on, off, off | 133 / 2 / 7 | none | none | FC14, FC32.new1 | byte-equal |
| off, on, off | 133 / 2 / 7 | none | none | FC14, FC32.new1 | byte-equal |
| on, on, on, **claims in their round-4 wording** | **131 / 4 / 7** | **FC30.new1** HOLDS → COUNTEREXAMPLE FOUND, parts (a), (b), (c), (e), (g) not as claimed; **FC23.new2** HOLDS → COUNTEREXAMPLE FOUND, part (f) not as claimed | the same 8 | the same four | byte-equal |

**No verdict flips** under any of the eight settings once the two claims are reworded: every claim's status and every part's status is S129's, and the case scripts (s106_cases.py's 79 lines, s104_external.py's FC-E1 to FC-E5, s104_creative_transport.py's CT1 to CT8) print byte for byte what they printed for S129. They do not evaluate the owner's condition or (Suff), so S86 cannot reach them. Why the round-4 wording flips, part by part: (a) its claims-file statement puts a selected transport in all three defeat sets, and under S86 a selected account is no longer in Def(L536) or Def(L17, S41); (b) L17 as text 104 words it then adds the accounts that are not constructed, not only the declared ones; (c) Expl := Acc ∧ ¬Dec makes a selected account an explanation, which S86's owner's condition forbids; (e) the link no pair tried, selected after round 2, is no longer missed by the owner's condition; (g) L61's "their" now reads Account ∧ Con, so the selected transport falls in (Nec)'s defeat set too; FC23.new2 (f) the same as (c) for the shop signs. Each is the decision itself, not a defect of the copy.

### 2.2 Where explanation is evaluated, at every narrower boundary

`tools/s131_sweep_the_boundaries_where_explanation_is_evaluated.py` runs the two claims that evaluate the owner's condition or (Suff) (found by searching the program for `suff_defeats` and `expl_ok`: FC30.new1 and FC23.new2), with the copy's `sel` and `prov_fixed_points` wrapped as S129's sweep wrapped them, and records each provenance verdict on the whole stated history and at every narrower boundary (every proper subset of the stated occurrences; for chains of holdings, those keeping the last holding). S86 changes what the semantics says of a candidate exactly where its transport is Sel there; nowhere else. Data: `suite boundary sweep where explanation is evaluated.json`.

| Claim | Distinct histories | On the whole history: Dec / Con / Sel | Narrower boundary pairs | At those: Dec / Con / Sel / no fixed point | S86 changes the verdict |
|---|---|---|---|---|---|
| FC23.new2 | 3 | 1 / 1 / 1 | 5 | 3 / 1 / 1 / 0 | the selected sign, whole and narrow |
| FC30.new1 | 18 | 12 / 2 / 4 | 16 | 10 / 1 / 4 / 1 | 4 selected on the whole history; at narrower boundaries 4 pairs, 2 of them only there |

The two that change only at a narrower boundary are the student's copied formula (FC30.new1 (d)) under cuts T and T′ with one pair tried: on the whole history (book and student) the student's holding is declared; at the student's own boundary {o2} it is selected (Reading C: the book, which represented the formula earlier, is outside). Under S129's rule that made it an explanation by (Suff)'s conjecture there, against the owner's S41 verdict (S129 section 5, item 12, K2); under S86 it is no explanation there either. The other pairs are the selected histories of the random candidates and signs, where S86 changes the verdict whether or not a boundary is declared. (The one "no fixed point" is cut U, already rejected, FC98.new1 (c).)

**Count.** Of the 142 claims, six mention Dec, Expl or (Suff) in their statements (FC12.new2, FC23.new2, FC30.new1, FC32.new1, FC72.new2, FC78; FC72.new2's "Dec" is December). The decision touches three: FC30.new1 and FC23.new2, which encode the owner's condition and (Suff), and FC32.new1, through D18.1's node for D16.XV, which now reads Con (its part (e), "only D16.XV reaches the atom Expl", still holds). FC12.new2 and FC78 are about provenance alone. With the S131 wording none flips; as written, FC30.new1 and FC23.new2 flip (six parts).

## 3. The formal claims the decision reaches

| Claim | On the copy, S86 on (S131 wording) | As written (round-4 wording) | Verdict |
|---|---|---|---|
| FC30 (E) takes no provenance | H | H | **holds, unchanged**: S86 changes what suffices for "explanation", not (E) |
| FC30.new1 (a), (b), (c), (e), (g) | H | COUNTEREXAMPLE at each | **needs rewording** (section 1.3), applied in the copy |
| FC30.new1 (d), (f), (h) | H | H | holds; (d) now holds at the student's own boundary too (section 2.2) |
| FC23.new2 (f) | H | COUNTEREXAMPLE | **needs rewording**, applied in the copy |
| FC32.new1 (e) only D16.XV reaches Expl | H | H | holds; D16.XV's node reads Con, not Dec |
| FC12.new1, FC12.new2, FC77, FC78, FC80, FC80.new1, FC83, FC98, FC98.new1 (the (Prov) claims and provenance) | H | H | **unchanged in content**: they compute provenance, not explanation |
| FC84 every creative attribution requires construction | H | H | unchanged; L47 now says the same of explanation |
| FC90, FC90.new1 ((EX)) | H | H | unchanged in wording; whether (EX) gives Con(t_c) not computed (section 5, item 9) |

## 4. The map under the three decisions

`tools/s131_feed_avida_cases_to_the_copy_with_explanation_by_construction.py` loads S129's feeding script unchanged, with only its folder and output names pointed at the S131 copy, so S117's four Avida cases are built exactly as S129 built them, and runs them under the eight settings; with S86 off it reproduces every value S129 recorded (checked by program, all four S129 settings). Data: `map feeding with explanation by construction.json` (S129's file unchanged). `tools/s131_build_the_map_with_explanation_by_construction.py` loads S129's map rule unchanged for every unit it moves, except the two defeat-condition units (D16.XV, FC30.new1), which with S86 on move to LINES UP EXACTLY when the NOT program taken whole meets (E) and every reading in force gives the same verdict on whether it is an explanation (S117 had them "in part" only because A and B disagreed). Written beside S117's and S129's: `results/S117 The Avida work against the semantics - relationship map, under Reading C and explanation by construction.json` (md5 a35131d2e7e5750179a6f3920c30a23e).

MC1, the NOT program taken whole (meets (E); cut into its instructions it fails F1, every setting), graded-pay run:

| Reading or boundary | Sel | Con | Dec | stands for NOT | S86 off (S129) | S86 on |
|---|---|---|---|---|---|---|
| A (S117), no boundary declared | yes | no | no | yes | an explanation by (Suff), narrow, never created | no explanation; evolved knowledge |
| B (S117), no boundary declared | no | no | yes | no | no explanation (S41) | no explanation (S41, S86) |
| C, the S72 boundary | yes | no | no | yes | an explanation by (Suff), narrow | **no explanation; evolved knowledge of NOT** |
| C, a boundary taking in Avida's authors | no | no | yes | no | no explanation (S41) | no explanation |
| MC1b (paid for nothing), C at S72, graded on | no | no | yes | no | no explanation | no explanation |

| Setting | Exact | In part | Does not | Nothing | Checked against |
|---|---|---|---|---|---|
| S117 as published | 114 | 36 | 18 | 116 | S117: agree |
| S129: Reading C alone | 121 | 29 | 18 | 116 | S129, S127: agree |
| S129: graded alone | 114 | 36 | 18 | 116 | S129: agree |
| S129: both (the baseline) | 122 | 28 | 18 | 116 | S129, S127: agree |
| S86 alone (hinge left open) | **116** | **34** | 18 | 116 | new |
| Reading C and S86 | 121 | 29 | 18 | 116 | new |
| graded and S86 (hinge open) | 116 | 34 | 18 | 116 | new |
| **all three, the S72 boundary (this map)** | **122** | **28** | **18** | **116** | S130's hand count ("unchanged"): agree |
| all three, a boundary taking in Avida's authors | 116 | 29 | 23 | 116 | as S129's at that boundary |

**Which pieces move, and why.** Between S129's map and this one (all three at S72): no verdict; the wording of R117 (D16.XV, FC30.new1: "the semantics calls it an explanation of NOT in its narrow sense" becomes "evolved knowledge, not an explanation", with S130 section 5 item 4's qualification of the question) and of R003 (T01, the constitutive conjecture: "its one point of contact, a candidate that meets the test of an explanation and is not declared" becomes "nothing in Avida is an explanation at all, since nothing works anything out"), each keeping S129's wording beside it. S130 section 4.3 moved R117 and R003 by hand and said the counts stay 122 / 28 / 18 / 116: **checked, it agrees**. Against S117 as published, with S86 alone: D16.XV and FC30.new1 move to exact, because the hinge no longer matters for them; the six provenance units (D11.4, D12.1, D12.3, D12.5, FC75, T10) still need Reading C, since whether the program stands for NOT still turns on it. MC1b (the run that paid for nothing): no explanation in every setting with S86.

**What the map now says, in one line:** the structural half of the Avida work lines up; the explanatory half has nothing in Avida, and now the theory says so of the evolved programs too: what passes the test of an account there is evolved knowledge, not explanation, as the owner read it.

## 5. What explanation by construction commits the theory to

Each item with its line in the text (text 107's numbering) and, where computed, its case in `what explanation by construction commits the theory to - computed.json` (`tools/s131_compute_what_explanation_by_construction_commits_the_theory_to.py`; Reading C and the graded condition on; each case with S86 on and off; the encodings, Θ by hand, are this job's or S129's K-cases; any account serves where the verdict turns only on the history, as S129 did).

1. **Every adaptation in nature is knowledge and not explanation** (N1; L13, L195, L205, L536). A trait with no chooser and no checker anyone wrote, whose doing raised its carriers' copying: selected, represents (evolved knowledge), and where it meets (E) taken whole, **no explanation** (S129's copy: an explanation in the narrow sense). Where the trait changed nothing about copying: declared, represents nothing, no explanation (as before). This is S85's "Knowledge evolved through natural selection is case closed", and the line between the adaptive and the explanatory kinds as S110 (O4, O10, O11) and S123 (H4) give them becomes the line between representation and explanation.
2. **A proof found by blind search is no explanation** (N2; L49, Grievance 7). At the search's boundary (the checker inside, its writers outside): selected, evolved knowledge, no explanation; at a boundary taking in the people who wrote the checker: declared, no explanation. A mathematician who later works it through, holding what it is to prove, constructs an account at the mathematician's boundary: an explanation by (Suff)'s conjecture, and new to that mathematician (S129 item 9). This is what S130 section 4.4, item 6, said would count against the decision for some readers; the theory now holds it.
3. **Learning from a teacher's answers stays an explanation** (N3; S128 (i), S129 K8; L405). The answers are a record of the teacher's representation (declared at the learner's boundary, representing nothing there); the learner's weights, built by its training with the target held, are constructed at the learner's boundary and at a boundary taking in the teacher. So, where the learner's account meets (E), (Suff) conjectures it an explanation, under S86 as before. **For the owner, not decided:** if the owner would call this "knowledge, not explanation" too, the line must sit higher (Build with ExplUse: the content built and used as an account; or (EX) only), S130 section 4.4, item 4. A classifier trained on labels is the plainest case.
4. **The one-part shop sign** (N4; S44, S45; FC23.new2). Both signs meet (E). Declared (written up): no explanation, as before. Selected (kept by trial with no target held): **no explanation** (before: an explanation). Constructed (worked out): an explanation, a narrow and bad one, as the owner said in S44 and S45. So the owner's "an explanation, just not a good one" holds of a sign someone worked out; of a sign simply written up it never held (S41). Whether "found by trial" in S41 meant an agent's trials against a target it holds (construction) or blind trial (selection) is still the owner's to say (S130 section 4.4, item 2); under S86 the answer decides whether such a sign explains.
5. **The student's copy that enters whole** (N5; S41 Q2; FC30.new1 (d); S129 K2). With the suite's encoding (components copied, bindings declared): on the whole history declared, at the student's own boundary selected when one pair was tried, declared when none was; under S86 **no explanation in every case**, so S129's open point (the owner's verdict kept at the student's boundary only if a copied formula enters whole) no longer matters for explanation. Read as a transfer from the book: on the whole history the copy inherits the author's construction and is an explanation (as before; FC30.new1 (f) is why the suite does not encode it so); at the student's boundary it is declared.
6. **Content learned by rote** (N6; S129 K9; L403, L405). At the learner's own boundary the rote copy is declared: no explanation, and not in the repertoire; the learner's later reconstruction is constructed there: an explanation by the conjecture, and new to the learner. On a boundary taking in the teacher the rote copy is a record of the teacher's construction and inherits it, so it counts as an explanation there; S86 does not change this (the provenance is constructed, not selected), but it means "worked out" is read at the boundary: by whom it was worked out is fixed by where the boundary is drawn.
7. **Question-finding (QF) and the creative-episode classes (L528)**: unchanged. No definition uses Expl (D16.XV; FC32.new1 (e), computed: only D16.XV reaches it), so membership of the base, creative-episode, explanation-creation, recursive and universal classes is as before; (QF) at L544 and (G), (N) do not mention explanation. The explanation-creation class is defined by (EX), not by Expl (item 9).
8. **Argument 6 (L47) with its two words.** "Construction is a separate provenance with a separate trace, and every explanation and every creative attribution requires it": the grievance "You have replaced explanation with evolution" is now answered for explanation as for creativity. L13 ("Creativity lives in construction. Selection produces the raw material construction works on") and L201 (selected transports at the object layer, constructed at the simulation layer) read the same and now hold for explanation too: selected representations below, constructed explanations above, as one arrangement.
9. **(EX) and Con(t_c)** (D14.7; L447 to L449; not computed). Origin asks Build of c, a trace that prepares the organization c and holds it; Con(t_c) asks a trace that holds the transport t_c at its output, and a transport assembled later from a trace's outputs is not thereby prepared by it (I168). So no conjunct of (EX) gives Con(t_c): an instance of (EX) whose t_c was not constructed would be in the explanation-creation class while D16.XV of the copy says it is no explanation at β. The program's (EX) witnesses (FC90, FC90.new1) do not encode t_c's history, so this was not computed. Whether (EX) should carry Con_β(t_c) as a conjunct is the owner's; noted in the core copy, not changed.
10. **One transport at two boundaries** (N7; S129 K1; D16.XV). Selected at one boundary and declared at another: under S86 neither is an explanation, so one unindexed Expl (false) meets both; the conflict S129 found is gone for this pair. Constructed at one boundary and declared at another (a construction whose target is held only outside, I201): still no unindexed common model; read per boundary, an explanation at the first and not at the second. So Expl_β (S129's K1, I202 here) is still needed, now only where construction is boundary-relative.
11. **The (Prov) claims** (L542; FC12.new1 to FC12.new3, FC77, FC78, FC80, FC83): unchanged in content and status. (Prov)'s second clause (a method rewriting every construction trace as a selection history without loss) would now remove explanation from the semantics as well as creativity, which raises its stakes; its third clause (explanation operates on the object layer) reads more simply, since L201's arrangement is now the rule for explanation (S130 section 4.3).
12. **The NOT program, MC1** (N8; section 4). At the S72 boundary (the whole execution environment, its task checker inside, the checker's writers outside): selected, stands for NOT on its two input pairs, meets (E) taken whole, **no explanation: evolved knowledge of NOT**. At a boundary taking in Avida's authors: declared, represents nothing, no explanation. In the run that paid for nothing: declared at both, no explanation. With S86 the semantics agrees with the owner at every boundary, and with S86 alone (no Reading C) it already agrees under S117's readings A and B.
13. **Necessity as well as sufficiency.** With (Nec) as conjectured (only candidates some transport preserves are explanations) and the owner's condition, Acc ∧ Con_β becomes necessary for an account to be an explanation at β, and (Suff) conjectures it sufficient: within accounts, "explanation" now means exactly "worked out" (a consequence, noted in the core copy).
14. **What S117's map now says in one line**: the Avida programs hold evolved knowledge where they are faithful and selected, and nothing in Avida is an explanation (section 4).

## 6. Corrections to S117's and S129's wording (from S130 section 5): listed, applied to nothing

These files are not written (S108 to S130 are read only). Each with where it stands and what it would say under S86:

| # | File, line | Now says | Under S86 would say |
|---|---|---|---|
| 1 | `results/S129 Reading C carried into copies - what changes.md`, line 5 (the owner's words and Claude's reading) | "stands for its task and, taken whole, is a narrow explanation of it, never a created one" | "stands for its task and, taken whole, meets (E) on the two-pair question S117 declared for it; with S86, evolved knowledge of its task and no explanation" (S130's wording 1 without S86: "… so (Suff) conjectures that it is an explanation in the narrow sense …") |
| 2 | the same file, line 155 (section 4's table, last column) | "(Suff) defeated by an argument not using (E)" | "(Suff) defeated *for an assessor who holds* an argument not using (E) that it is no explanation (stipulated)"; with S86 the column is False throughout, since (Suff) no longer claims the program |
| 3 | `plain words/129 Reading C carried through, in plain words.md`, line 15 | "it passes the theory's test, so it counts as a narrow explanation of NOT, with nothing in it built" | "it passes the theory's test of an account, so it is evolved knowledge of NOT; with your word it is not an explanation, since nothing in it was worked out" |
| 4 | `results/S117 The Avida work against the semantics - relationship map, under Reading C.json`, line 5817 (R117, what_matches) | "so the semantics calls it an explanation of NOT in its narrow sense" | carried into the S131 map (R117) |
| 5 | `results/S117 The Avida work against the semantics - results.md`, line 13 (and the D16.XV and FC30.new1 rows, lines 398 and 401) | "as one block, passes as an explanation" | "as one block, passes the test of an account (E), on a question declared by the modeller" |
| 6 | `results/S127 The Avida findings turned back on the semantics - the hinge.md`, lines 9, 41, 88, 140 (and 46, 89) | "an explanation of it in the semantics' narrow sense"; "taken whole, an explanation of NOT, never created"; adaptations "narrow explanations where (E) holds" | "evolved knowledge of NOT, not an explanation"; adaptations "evolved knowledge, never explanations"; its row 92 ("Owner's 'Avida programs are not explanations', held in the narrow sense": "rules out (Suff) for the owner") would read "agrees" under every reading |
| 7 | `plain words/127 What Avida taught us about the semantics, in plain words.md`, line 17 | "taken whole the theory counts it as an explanation of NOT. A bad one" | "taken whole it is knowledge of NOT; under your word, not an explanation" |

Everywhere "explanation of NOT" is said of MC1 (S130 item 7: "an account of the two-pair NOT question") the S86 wording is "evolved knowledge of NOT on its two input pairs". The S131 map carries 4 (and R003); nothing else is applied.

## 7. What is unsure

- **The claims were reworded in the copy.** No flip with the S131 wording is by construction of the rewording; the run with the round-4 wording shows exactly what the decision contradicts (six parts of two claims), and the rewording is the smallest that makes each part say what the decision says. A checker should read the six rewordings before anything is written into the claims.
- **Teacher's answers** (section 5, item 3): constructed under every reading (S128), so explanation under S86; the owner may want the line higher. Not decided here.
- **S41's "found by trial"** (section 5, item 4): Claude's reading (an agent's trials against a held target are construction) differs from S108's (C16); under S86 it decides whether a sign found by trial explains. The owner's to say.
- **(EX) and Con(t_c)** (section 5, item 9): not computed; the definitions leave it open.
- **The encodings are this job's or S129's** (Θ by hand, I90): which occurrences represent what, which holding is a record of which. Where a verdict turns only on the history, a stand-in account (the pole's forward candidate) is used, as S129 did; whether each encoding fits the real case (a beak, a proof search, a classifier) is argument.
- **The map** moves only what the model's values say; the wording of R117 and R003 is Claude's. S86 alone closing the defeat-condition units without Reading C is computed on S117's two readings; it says nothing about the provenance units, which still need Reading C.
- **The sweep** takes S129's subsets of occurrences (including boundaries that leave out the holding itself, for tagged histories), for comparability with S129.

## 8. What was done

- Read: decisions S41, S44, S45, S57, S59, S83 to S86 with Claude's readings; S130's theory point (sections 0 to 7); S129's results, copies, data and tools; text 129; text 107's L13, L17, L47, L49, L61, L69, L201, L205, L211, L524, L528, L536 to L544; the formal core's D12.2, D13.3, D13.6, D14.7, D16.XV; the claims FC12.new2, FC23.new2, FC30, FC30.new1, FC32.new1, FC72.new2, FC78, FC90.new1; S117's results and map units.
- Written: text 131; in `results/S131 Explanation by construction carried into copies/`: the core copy, the program copy, `suite runs.json`, `suite boundary sweep where explanation is evaluated.json`, `map feeding with explanation by construction.json`, `what explanation by construction commits the theory to - computed.json`; the map beside S117's and S129's; this file; plain file 131; seven tools `tools/s131_*.py`.
- Computer time: nine whole-suite runs (three at a time, about 9 minutes a batch, 28 minutes in all), the case scripts under nine settings, the sweep (2 s), the feeding and the map (seconds); no Avida.
- Checked by md5 before and after: text 107, text 129, S107's core, claims and every program file, S129's core copy and every program file.
- Failures caught before commit: the first program copy added a check for a selected transport to FC30.new1 (a) even with the decision off, which changed the printout against S129's; it was limited to the decision on, so with it off the copy prints what S129's does.
