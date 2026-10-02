# S129 Reading C carried into copies: what changes

*Log S129, 2 October 2026, decisions S83 and S84. One Opus 5.5 agent doing the whole job (S56, S68; no subagent or workflow). No Avida run; no outside model; no GLM check (S70); no book file opened. **The theory itself is unchanged**: `tests/107 The semantics, standing alone, after round 4.md`, the formal core, claims and program in `results/S107 Round 4 - maths after the reading/`, every S108 to S128 file, the decisions file, the S61 terms and `authority/` were read and not written. Both decisions were carried into COPIES. The semantics is cited from text 107 by line ("L195"; in the copy, text 129, every line stands 12 lines further down, its note being the first 12 lines: L195 is its line 207); the formal core by definition id; inventions by register number; the copy's own provisional inventions are I198 to I201 (section 1.2), not in the register. Avida is described in the owner's terms (S61).*

**The owner's words.** S83, after file 127 was sent again: "Oh clearly C." S84, after Claude set out the second decision: "Well yes. That is how selected is defined. But does that help us understand what knowledge is? Or what counts as knowledge?" (Claude answered the question directly, as recorded with S84; this job carries the first half.) Claude's reading (S83): the history in the definition of a selected correspondence (D12.1) is read inside the system boundary declared for the claim; with the owner's boundary (S72, the whole Avida execution environment as the selector) a task checker written by people belongs to the world's rules, so an evolved program's correspondence with its task can be selected, stands for its task and, taken whole, is a narrow explanation of it, never a created one. Claude's reading (S84): D12.1's survival condition is a graded advantage in copying, S127's needed word.

## 0. In short

- **Written in, on copies only.** Text: S127's three sentences for Reading C after D12.1's formula at L195, "inside the declared boundary" at L193, "the boundary of a provenance claim" among the declared inputs at L522; and S127's wording for a graded survival condition at L195 (`tests/129 The semantics, standing alone, after round 4, with Reading C.md`; text 107 md5 c7af964c329ab7959243405d394e6574, copy f3624126ad21f9fdf01588c6c2351905; only those three lines differ). Formal core: the history of a holding read inside a declared boundary β (h_β(t)), a holding whose correspondence entered β whole declared there, and a further conjunct Adv in the survival condition (D12.1 to D12.5, D15.4). Program: three optional fields on a history (its boundary, which holding is a record of which, a stated rate fact) and the provenance functions reading them (`model/claims_b.py`), with two switches.
- **The suites.** The whole claim suite (142 claims) and the three worked-case scripts gave, on the copy, the original's status and every part's status under all four settings of the switches (neither decision, Reading C alone, the graded condition alone, both): **no flip** (section 2.1). This is by construction where a case declares no boundary and states no rate fact, and it was checked, not assumed.
- **Where Reading C does bite in the suites.** Recomputed at every narrower boundary, the provenance verdicts of 16 claims' histories turn out to be boundary-relative in four ways (section 2.2): an earlier representation left outside no longer blocks selection; a record whose source is outside is declared; a construction whose target is held only outside is declared; the rejected reading U loses its fixed point. FC12.new1's exclusion, the one fixed point under T′ and FC83 hold at every boundary; FC78 and FC12.new2 (a), (d) hold at each boundary and need rewording; D16.XV and FC30.new1 (c) need "explanation" read per boundary; FC30.new1 (d), the student's copy, keeps the owner's verdict at the student's own boundary only if a copied formula counts as entering whole (section 3).
- **The map.** Recomputed by program from the model's own verdicts: S117 as published 114 / 36 / 18 / 116; Reading C alone 121 / 29 / 18 / 116; the graded condition alone 114 / 36 / 18 / 116 (the hinge still open, nothing moves); **both 122 / 28 / 18 / 116** (exact, in part, does not line up, nothing in Avida); all four agree with S127's hand count. The corrected map is `results/S117 The Avida work against the semantics - relationship map, under Reading C.json`, beside S117's, which is unchanged (section 4).
- **What C commits the theory to** (section 5): provenance, representation and explanation relative to a declared boundary, declared before the attribution; a breeder, a person scoring by hand and a live driver judged by where the boundary falls, with no line needed between a rule and an occurrence; dog breeds, crops and searches people scored selected inside the run or the lineage, declared at a boundary taking in the people; traits shaped by mate choice still declared at any boundary holding the choosers; learning from a teacher still constructed; and two new findings: content learned only by rote represents nothing at the learner's boundary, so a later reconstruction is new to the learner and an origin; and Enable's non-question-begging clause is never met at β.
- **The second decision (S84), decided** (section 6): the 11 programs doing NOT in the run that paid for nothing are no longer selected for NOT; the programs of the graded-pay runs are selected where doing the task raised their copying; adaptations of living species are selected where the trait raised copying.

## 1. The changes made

### 1.1 The text copy

`tests/129 The semantics, standing alone, after round 4, with Reading C.md`, written by `tools/s129_write_the_text_copy_with_reading_c.py`, which applies four exact replacements (each must match once), puts a dated note of 12 lines at the top, and checks line by line that, the note apart, only text 107's L193, L195 and L522 differ. Text 107 md5 c7af964c329ab7959243405d394e6574 (632 lines), unchanged on disk; the copy md5 f3624126ad21f9fdf01588c6c2351905.

| Change | Decision | Text 107 line (copy line) | What |
|---|---|---|---|
| 1 | S83 | L195 (207) | After "(D12.1).", S127's three sentences word for word: "The history of a holding is read inside the system boundary declared for the claim (Part XII). A process inside the boundary whose correspondence entered it whole from outside has, there, neither a selected nor a constructed history, and represents nothing there; what it carries is a contribution from outside the boundary (Part X, Ownership). A provenance is relative to the boundary declared, as a capability is, and the boundary is declared before the attribution, not chosen after it." |
| 2 | S83 | L193 (205) | "determined by its history in the physical module" becomes "… in the physical module inside the declared boundary" |
| 3 | S83 | L522 (534) | "the boundary of a provenance claim (Part IV);" added to the declared inputs, after "the system boundary and continuity of an attribution (Part XII);" (the pointer "(Part IV)" is the copy's) |
| 4 | S84 | L195 (207) | "a survival condition requiring fidelity on \(H\)" becomes "a survival condition under which fidelity on \(H\) changes which members persist or are copied (a requirement is one such condition; a higher rate of copying for members faithful on \(H\) is another)": S127's smaller form (hinge file, section 7); the companion's "at each stage of the history" is left out, since with \(H\) a set of pairs there are no stages to quantify over (S128's P1, not applied) |

Not written in: S127's sentence for L481; S128's P1 to P3; and the lines Reading C reaches but S127 did not name (section 3.3).

### 1.2 The formal core copy

`results/S129 Reading C carried into copies/formal core, after round 4, with Reading C and the graded survival condition - a copy.md` (original md5 d6e6ec62acbc6ef763e07b7cd7b29540, unchanged; copy bb57e39737f541fe20ae3fae0e8185b4), written by `tools/s129_write_the_core_and_program_copies.py`. Every change is marked [S129: S83 …] or [S129: S84 …] with what it was, as the core marks its own rounds; no definition paragraph is added or removed (FC32.new1 still reads 114 paragraphs, FC14 118 definition lines).

| Definition | Change | Why it is the smallest that does it |
|---|---|---|
| D12.1 Selected | the exclusion reads ¬∃o ≺_{h_β(t)} o_t … Rep_β(o, x), with h_β(t) := the occurrences of h(t, o_t) inside the declared β, ≺ restricted, and a holding inside β whose correspondence entered β whole representing nothing at β **[I198, I200]**; and ¬∃h′ ⊆ h_β(t): CT(h′, t) **[I201]** | a boundary index on the history (what S127's formal sketch proposed: "h(t) := h(t, o_t) restricted to the occurrences inside β"); nothing else in D12.1 moves |
| D12.1 surv (S84) | surv(t, H) :⟺ Faithful_H(t) ∧ Env_{h(t)}(value_t│_H) ∧ **Adv_{h(t)}(H)**, Adv: in h(t), fidelity on H changes which members of 𝒯 persist or are copied (faithful members persist or are copied at a higher rate, other things equal, read through Θ); a requirement is one such condition; a history in which fidelity on H made no difference gives ¬Adv **[I199]** | a further conjunct, leaving I177's Env (a condition on t's values at H) as it was, so FC80.new1 is untouched |
| D12.2 Constructed | Con reads an episode of h_β **[I201]** | the text's "A provenance is relative to the boundary declared" read as said of all three |
| D12.3 Declared | the record clause applies to transfers from a holding inside β; a holding inside β reached by such transfers from outside β has EnteredWhole_β and Dec_β, represents nothing at β, and carries a contribution from outside β (L427); a routine written outside β and run inside it is such a holding (its correspondence a record of its writers', L211) **[I200]** | S127's "D12.3's record clause applies to transfers inside β; a holding whose correspondence enters β whole gets Dec inside β" |
| D12.4 | a transfer gives each part its value only inside β; from outside, Dec_β | the per-part form of D12.3's change |
| D12.5 (R) | Sel or Con at β; Rep_ℓ with no β written is Rep_{ℓ,β} at the boundary declared for the claim (L524) | representation follows provenance |
| D15.4 | β also indexes a provenance claim, declared before the attribution | the index's new use |
| D13.1, D16.3, D16.XV | notes only, marked "a consequence, not a change" | what C asks of them is in section 3.3 |

The copy's inventions, provisional (the register is the theory's): **I198** h_β(t), and a case that declares no boundary read with every occurrence it states inside (others: left open, as text 129's L522 would read strictly; the holder's own occurrences only). **I199** Adv read through Θ, by hand in the program; a case stating no rate fact read as a requirement of fidelity (other: left open; "other things being equal" made a computed comparison). **I200** EnteredWhole computed from D12.3's chain of transfers (other: a primitive read through Θ; or "whole" read part by part, D12.4). **I201** C applied to Con and to Sel's ¬CT as well as to Sel's exclusion (other: C applied only where S127's sketch names, D12.1's exclusion and D12.3's record clause).

### 1.3 The program copy

`results/S129 Reading C carried into copies/model after Reading C/`: the 26 files of `model after round 4/`, 24 byte-equal to the original, two changed (checked by the builder):

- `model/claims_b.py` (original md5 931262d306e91896c727e369b79af36f, copy 6efd639fa44852358cd23f5ac49d3eb7): `Hist` takes three optional fields, `beta` (the occurrences inside the declared boundary; none: every stated occurrence inside, I198), `source` (which holding is a content-preserving transfer of which, for EnteredWhole, I200) and `advantage` (the rate fact: True, False, or not stated, I199); new helpers `inside`, `entered_whole`, `rep_at_beta`, `held_at_beta`; `sel` counts only the tags of occurrences inside β that did not enter it whole, and fails on a history whose advantage is stated False; `con` counts the held targets inside β; `prov_fixed_points`, `_prov_step`, `_con_at` and `build_at` take `beta` (an occurrence outside β has no provenance at β; a record whose source is outside β is Dec_β; the exclusions and Con's held targets range over β); `DEP` gains edges Sel, Con, Dec → β (β is a declared index, a sink: no cycle); the sink note for `surv` names Adv. Two switches, read from the environment: `S129_READING_C` and `S129_GRADED` (both on by default; both off computes what the original does).
- `model/corefile.py` (original 28a9ccc47054786ada7f1fce57c324d6, copy 962bb729c81bc7b0a851c7dd9544fd71): FC14 and FC32.new1 read the core copy beside the program.

## 2. The suites' results

### 2.1 The whole suite and the worked cases, on the copy

`tools/s129_run_the_suites_on_the_copy_and_compare.py`: the record's settings (scale 4, time cap 45 s, PYTHONHASHSEED=0, `--no-write`), the original run from a byte-equal scratch copy (never in place), then the copy under four settings, two at a time; `s106_cases.py`, `s104_external.py` and `s104_creative_transport.py` likewise. Data: `results/S129 Reading C carried into copies/suite runs.json`.

| Run | Claims: H / CEX / NT | Status or part status different from the original | Different from the record (after_round4) | Printed results different from the original (times and time-capped counts left out) | s106_cases.py, s104_external.py, s104_creative_transport.py |
|---|---|---|---|---|---|
| original (byte-equal scratch copy) | 133 / 2 / 7 of 142 | – | none | – | – |
| copy: C off, graded off | 133 / 2 / 7 | none | none | FC14, FC32.new1: only the name and md5 of the core file read | byte-equal output |
| copy: C on, graded off | 133 / 2 / 7 | none | none | the same two, the same reason | byte-equal output |
| copy: C off, graded on | 133 / 2 / 7 | none | none | the same two, the same reason | byte-equal output |
| copy: C on, graded on | 133 / 2 / 7 | none | none | the same two, the same reason | byte-equal output |

**No verdict flips**, under Reading C alone, the graded condition alone, or both, in the claims (every part of every claim compared) or in the worked cases (s106_cases.py's 79 lines; s104_external.py's FC-E1 to FC-E5; s104_creative_transport.py's CT1 to CT8). The reason is the same throughout: no case of the suites declares a system boundary (so its history is read with everything it states inside, I198, which is the original's reading), and no case states that fidelity made no difference to copying (so the graded condition is met as a requirement, I199). Reading C changes a verdict only where a boundary leaves part of a stated history outside (section 2.2), and the graded condition only where a history is stated to give no advantage (MC1b, K5). The DEP edges Sel, Con, Dec → β leave FC32.new1's checks as they were (no cycle; L526's pairs still paths).

### 2.2 Every provenance computation of the suites, at every narrower boundary

The suites' histories declare no boundary, so on the copy they are read whole (I198), which is why nothing flips. `tools/s129_sweep_the_boundaries_of_every_provenance_case.py` asks what Reading C does to them at a narrower boundary: it wraps the copy's `prov_fixed_points`, `sel` and `con`, runs every claim once (scale 1, cap 20 s; the claims' own results are the copy's) and recomputes each provenance computation at every proper sub-boundary that keeps the holding in question (for the tag histories, every subset of the named occurrences). Data: `suite boundary sweep.json` in the S129 folder.

Sixteen claims compute provenance (FC12.new1, FC12.new2, FC12.new3, FC23.new2, FC30.new1, FC77, FC78, FC80.new1, FC81, FC82, FC83, FC84.new1, FC98, FC98.new1, FC102.new1, FC104.new1; every claim's status at this scale is the record's, 133 H, 2 CEX, 7 NT). Of the distinct histories they build, those whose verdict changes at some narrower boundary:

| Function | Distinct histories | Change at some narrower boundary |
|---|---|---|
| the fixed points of (R) (`prov_fixed_points`, chains of holdings) | 3,058 | 1,435 |
| `sel` on a tagged history | 2,629 | 3 |
| `con` on a tagged history | 16 | 9 |

How they change, counting distinct histories (one history can change in more than one way at different boundaries); the cut T′ is the one the text uses (I162):

| Change of the last holding's verdict | T′ | T | K | U |
|---|---|---|---|---|
| Dec → Sel: an earlier holding that represents the content (or t, H, surv) is left outside, and no longer blocks selection | 303 | 111 | 34 | – |
| Sel → Dec: a record whose selected source is outside the boundary has entered it whole | 88 | 1 | 1 | – |
| Con → Dec: a record whose constructed source is outside, or a construction whose target is held only outside (I201) | 449 | 8 | 37 | – |
| only an earlier holding inside the boundary changes | 302 | 41 | 4 | 63 |
| the number of fixed points changes (U's known defect, FC98.new1 (c)) | 0 | 0 | 0 | 110 |

`sel`: three histories go from not selected to selected when the one occurrence tagged as representing t, H or the survival condition is left outside (FC12.new1's comparisons with round 2's D12.1). `con`: nine go from constructed to not when the occurrence holding the target is left outside (FC23.new2 (f), FC30.new1, FC78, FC81, FC82, FC84.new1, FC12.new1). Each kind is what the copy's D12.1 to D12.3 say at a boundary that leaves part of the stated history outside; none is an error of the copy. Under T′ no history loses or gains a fixed point at any boundary.

`tools/s129_check_the_provenance_claims_at_every_boundary.py` recomputes the universal provenance statements on their exhaustive family (every chain of up to three holdings, each a record of an earlier one or not: 3,208 chains, 9,344 narrower chain-boundary pairs; data `the provenance claims at every boundary.json`):

| Statement | At every narrower boundary |
|---|---|
| FC12.new1: ¬(Sel ∧ Con), cuts U, K, T, T′ | holds (0 failures) |
| FC98.new1 (b), FC12.new2 (d): one fixed point under T′ | holds (0 failures) |
| FC12.new2 (d): a record has its source's provenance | holds for every record whose source is inside β (0 failures); the 5,696 records whose source is outside β are all Dec_β, 2,880 of them with a source Sel or Con on the whole history |
| FC78: exactly one provenance per holding | holds at each boundary; across two boundaries, 4,232 of 15,488 holdings inside a narrower β have another verdict there than on the whole history |
| FC83: no Sel and Build at one holding (holdings that are not records, FC83's family) | holds (0 failures) |

## 3. The formal claims that touch D12.1, D12.3, D12.5, D16.XV and FC30.new1

### 3.1 Recomputed

Every claim below has, on the copy, the original's status and part statuses under all four settings (section 2.1). The column "per boundary" is what Reading C adds when a claim is made at a narrower declared boundary (sections 2.2, 5).

| Claim | On the copy | Per boundary | Verdict |
|---|---|---|---|
| FC12.new1 Sel and Con exclude each other | H | holds at every boundary | **holds** |
| FC12.new2 provenance per holding; a record carries its source's | H | (a), (d): only for a source inside β; a record of a source outside β is Dec_β | **needs rewording**: "a record made inside β from a holding inside β" |
| FC12.new3 CT's 'prepares' exact | H | no history boundary-relative | **holds** |
| FC23.new2 (f) the shop sign with a constructed transport | H | Con needs the target held inside β | holds per boundary |
| FC30 (E) takes no provenance | H | (E) takes no boundary either | **holds**: only provenance, and so ¬Dec and Expl, become boundary-relative |
| FC30.new1 (a), (b), (e) to (h) | H | hold at each boundary | holds per boundary |
| FC30.new1 (c) the owner's condition and (Suff) have a common model | H | with Expl unindexed, no common model once one transport is Sel at one boundary and Dec at another (K1); with Expl read per boundary, one | **needs rewording** (Expl_β), with D16.XV |
| FC30.new1 (d) the student's copy | H | at the student's own boundary: Dec if the copy counts as a transfer from the book (I200); Sel, with one pair tried, under the suite's own encoding (bindings declared, not transferred) (K2) | **changes** unless "entered whole" covers a copied formula |
| FC77 no selection without a witness | H | no history boundary-relative; with Adv, still none | **holds** |
| FC78 exactly one of three provenances | H | at each boundary; not across boundaries | **needs rewording**: "at each declared boundary" |
| FC79 fidelity takes no population | H | Faithful takes no history or boundary | **holds** |
| FC80 Argument 3 | H | Adv is a fact of the history, the same for t and its altered twin, so (d) holds | **holds** |
| FC80.new1 the survival condition enacted by the environment | H | gains a further witness under S84 (K5: faithful on H, fidelity made no difference: Sel with surv as after round 3, not with Adv) | **holds**; a test part could be added (not added) |
| FC81 Argument 4 | H | holds at each boundary (Con at β) | holds per boundary |
| FC82 the two responses have no common result | H | holds at each boundary | holds per boundary |
| FC83 only the construction response is originative | H | holds at every boundary | **holds** |
| FC84 creative attribution requires construction | H | unaffected; but see K9 (rote content and newness) | **holds** |
| FC84.new1 constructed where the question never changes | H | Con needs the brief held inside the engineer's boundary (K11: held as a record inside, Con) | holds per boundary |
| FC95 represent a theory in error | H | a witness at any boundary that holds the history | **holds** |
| FC97.new1 H and surv as contents | H | unaffected | **holds** |
| FC98, FC98.new1, FC98.new2 the dependence order, the T′ equations | H | T′: one fixed point at every boundary; T's blocking by an earlier declared holder disappears when that holder is outside β; U loses its fixed point at some narrow boundaries (U already rejected) | **holds** |
| FC102, FC102.new1 Argument 10, E9 | H | t₀'s history has one occurrence: no history boundary-relative | **holds** |
| FC32.new1 the dependence graph | H | Sel, Con, Dec → β added; no cycle; L526's pairs are paths | **holds** |

D12.1, D12.3, D12.5 themselves are what changed (section 1.2). D16.XV needs its atom read at a boundary (K1): **needs rewording**.

### 3.2 S84's effect on the claims

No suite case states a rate fact, so S84 moves no suite verdict (section 2.1). It moves exactly the histories in which fidelity is stated to have made no difference: MC1b, K5. FC80.new1's statement still holds; the S84 witness could be its part (c).

### 3.3 Lines Reading C reaches that S127 did not name (not changed; for the owner)

- **L536, D16.XV, (Suff) and the owner's condition (S41 Q2).** Dec is now Dec_β; "explanation" must be read at the same declared boundary (L524 already says every claim is relative to β), or the owner's condition and (Suff) contradict each other on any transport selected at one boundary and declared at another (K1, computed). Proposed: write Expl_β(ℰ) in D16.XV and "at the boundary declared" at L536.
- **L495, D16.3, Enable's non-question-begging clause.** "an occurrence o with Rep_ℓ(o, c) whose provenance was relayed from outside β": at β such an occurrence never represents (D12.3 in the copy), so the clause is never met and Enable asks nothing (K10: 0 of 9,344 narrower chain-boundary pairs, against 2,880 relayed-in representing holdings on the whole history). Proposed: "an occurrence o with Held_ℓ(o, c) whose content entered β whole".
- **L403, D13.1 Deploy, and so the repertoire and (N), (G).** Rep is read at Deploy's own β: content relayed in whole is not deployable at the learner's boundary until it is reconstructed there (K9). Consequence in section 5, item 8.
- **L211, L405.** "a later record made from the carrier carries that provenance" and "the rest of the content keeps its inherited provenance" hold inside β; from outside β the record is declared there. The C sentence at L195 says so; L211 and L405 could point to it.
- **L13, L520.** "told apart by their histories" and "Provenance, from physical history" would read "… inside a declared boundary".

## 4. The map under Reading C

`tools/s129_feed_avida_cases_to_the_copy_under_reading_c.py` (S117's feeding script, copied and pointed at the copy; data `map feeding under Reading C.json`) feeds the copy S117's four Avida cases under all four settings. MC1 is the most common NOT program of run low seed 2 (S112; 110 instructions; 44 copies; it hands back nand(x, x)), taken whole and cut into its instructions, with its history read four ways: S117's A and B (no boundary declared), Reading C at the S72 boundary (the whole execution environment from the start of the run, the task-checking code inside it as a record of its writers, who are outside), and Reading C at a wide boundary taking in Avida's authors; MC1 in a run where doing NOT raised the rate of copying, MC1b in the run that paid for nothing.

| MC1, the NOT program, taken whole | Sel | Dec | stands for NOT | (Suff) defeated by an argument not using (E) |
|---|---|---|---|---|
| A (S117), any setting | yes | no | yes | yes |
| B (S117), any setting | no | yes | no | no |
| C, S72 boundary, Reading C on | **yes** | no | **yes** | **yes** |
| C, wide boundary, Reading C on | no | **yes** | no | no |
| C, S72 boundary, Reading C off (the copy computing as the original) | no | yes | no | no |
| MC1b (paid for nothing), C at S72, graded on | **no** | **yes** | no | no |
| MC1b (paid for nothing), C at S72, graded off | yes | no | yes | yes |

Taken whole, (E) holds; cut into its instructions it fails (F1), in every setting. MC2 (Argument 3) is unchanged: at the S72 boundary with a graded advantage both programs are selected and differ at the order the world never gives. MC3 and MC4 have no provenance and are unchanged.

`tools/s129_build_the_map_under_reading_c.py` moves a unit only where these values say so, and recounts:

| Setting | Exact | In part | Does not | Nothing | S127 by hand |
|---|---|---|---|---|---|
| S117 as published | 114 | 36 | 18 | 116 | 114 / 36 / 18 / 116 (S117) |
| Reading C alone (S83), S72 boundary | 121 | 29 | 18 | 116 | 121 / 29 / 18 / 116, agree |
| the graded condition alone (S84), hinge open | 114 | 36 | 18 | 116 | (not counted by S127) |
| **both, S72 boundary (the corrected map)** | **122** | **28** | **18** | **116** | 122 / 28 / 18 / 116, agree |
| for comparison: both, a boundary taking in Avida's authors | 116 | 29 | 23 | 116 | 116 / 29 / 23 / 116 (B), agree |

Moved with Reading C: D11.4 and FC75 (relation R061: the routes in Avida's traces are active routes from a represented input), D12.3 (R065: the task list and checking code are declared at the S72 boundary, the programs' correspondences selected), D12.5 (R077), T10 (R086), D16.XV and FC30.new1 (R117), each from LINES UP IN PART to LINES UP EXACTLY; with S84 too, D12.1 (R063). With S84 alone nothing moves, because S117's readings A and B still differ. No unit outside S117's eight moves at the S72 boundary; at the wide boundary FC80 would move from exact to in part, as S127 said. The corrected map (`results/S117 The Avida work against the semantics - relationship map, under Reading C.json`) keeps each moved relation's S117 verdict and wording beside the new one (`verdict_in_S117`, `why_in_S117`), names the computed values it rests on, marks the eight as decided (S83; D12.1 S83 and S84), recounts the groups and lines, notes breaks B1 and B4 as decided, and carries every setting's counts and the check against S127.

## 5. What Reading C (with S84) commits the theory to

Each item with its line in the text copy (text 107's numbering), its definition in the core copy, and, where computed, its case in `what Reading C commits the theory to - computed.json` (`tools/s129_compute_what_reading_c_commits_the_theory_to.py`; every encoding is Θ by hand, I90, and is this job's; the verdicts are the copy's).

1. **Provenance relative to a declared boundary** (S127). L193, L195; D12.1, D12.3, D12.5, D15.4. One holding can be selected at one boundary and declared at another, both true at their indices: the NOT program (MC1), any transport whose selector was written outside the system (K1). Exactly one provenance holds at each boundary, not across boundaries (FC78, section 2.2).
2. **Every provenance claim states its boundary** (S127). L522 (declared inputs): where the boundary is missing, the assessment is left open. The copy reads a case that states its history but no boundary with everything it states inside (I198); read strictly, L522 would leave those cases open instead.
3. **The boundary is declared before the attribution, not chosen after it** (S127). L195's third C sentence, as L473 says for capability. The map shows why it matters: the same program gives 122 / 28 / 18 / 116 or 116 / 29 / 23 / 116 by the boundary alone.
4. **A breeder or a live driver as an occurrence** (S127). L195's second C sentence; D12.3 (EnteredWhole). Under C a chooser is an occurrence wherever it acts; what decides is the boundary: a chooser inside it whose criterion was formed inside it (a breeder on the farm, K3; a person scoring by hand, K6) makes the result declared; a chooser whose criterion entered whole (a breed standard written outside and applied by a hired hand inside, K3; Claude's growing-list runner, written by Claude, inside the boundary, K7) represents nothing there, and the result is selected; a chooser outside the boundary is a contribution from outside (L427), and the result is selected (K3, K6, K7). Unlike Reading A, C needs no line between a fixed rule and a live chooser.
5. **Dog breeds and crops** (S127). Selected at the boundary of the line of animals or plants, declared at the boundary of the farm with its breeder (K3), as S127 said.
6. **Searches people scored** (S127). A program or design found by a search whose scoring code people wrote: selected inside the run's boundary, declared at a boundary taking in the people (K6). The owner's own creative transport experiment (S104, CT8): no change, since the expression trees built in the run already represent the target, so its readings R1 and R2 give constructed and declared at both boundaries (K12).
7. **Genes: adaptations of living species** (S127). With no chooser, selected where the trait raised its carriers' copying, not where it made no difference (K5, S84). **A correction to S127's table**: a trait shaped by mates choosing (a peacock's tail) is declared at any boundary that holds the choosers, because the peahens' preference, itself selected inside that boundary, represents the survival condition earlier than the tail's holding (K4; the same on the whole history, so as under the original and B). S127 listed this only under B; it follows from D12.1's clause whenever a chooser represents the criterion inside the boundary, under A and C too. Whether a peahen's preference represents the survival condition is Claude's argument, not computed from any peahen.
8. **A program learning from a teacher within its life** (S128). Constructed under C at both boundaries (K8): the teacher's labels, a record of the teacher's representation, are declared at the learner's boundary and represent nothing there, but construction asks only that the target be held (D12.2, D18.1). S128's finding stands.
9. **Found here: rote content and newness.** L403 (Deploy), L405 ("Reconstruction by a learner is construction; relay is not"), L413 to L416 (N), L422 (G); D13.1, D13.5, D13.6. At the learner's boundary, content relayed in whole (learned only by rote) is declared there and represents nothing, so it is not in the learner's repertoire; a later reconstruction by the learner is new to the learner and, with an attempt and the construction, an origin. At a boundary taking in the teacher it is not new (K9). Under the original it was never new.
10. **Found here: Enable's clause empties** (L495, D16.3; K10), and **"explanation" must be read per boundary** (L536, D16.XV; K1). Section 3.3.
11. **Found here: construction needs its target held inside the boundary** (I201; D12.2 in the copy). A construction whose target is held only outside the boundary is declared there (the sweep's Con → Dec cases); the bridge stays constructed when the brief is held inside the engineer's boundary (K11). Under I201's other choice (C only in Sel's exclusion), Con would not be boundary-relative.
12. **Found here: the student's copied formula** (FC30.new1 (d), S41 Q2). At the student's own boundary the owner's verdict (declared, not an explanation) holds only if a copied formula counts as a correspondence entering whole (I200; K2). Under the suite's own encoding (components copied, bindings declared, not a transfer), a student who tried the formula on one pair would count as selecting it there. And on the whole history, reading the copy as a transfer gives it the author's constructed provenance, which is why the suite encodes it as it does (FC30.new1 (f)).

## 6. The second decision (S84), decided: what it changes

S127 left open whether a graded advantage, being copied more often, counts as the survival condition's fidelity requirement. The owner decided it (S84): it does. In the copies: L195's wording (change 4) and Adv in D12.1 (section 1.2). What it changes, under Reading C at the S72 boundary:

- **The 11 programs doing NOT in the run that paid for nothing** (S117 B4; 3,600 programs at update 50,000): no longer selected for NOT (MC1b: Sel false with the graded condition, true without it), so they do not stand for NOT and are not explanations of it. The formal core's old reading (Env none) counted them selected, which S127 argued cannot be what "selected" means.
- **The programs of the graded-pay runs** (S111, S112, S113's paying environments, S116): selected wherever doing the task raised their rate of copying (MC1), where a strict reading of "requiring" would have declared them all. S117's D12.1 moves to LINES UP EXACTLY.
- **Adaptations of living species**: selected where the trait raised copying (K5), as the text's picture of selection producing the object layer assumes (Part IV); the strict reading would have declared them.
- **Argument 3 and FC80**: untouched; the graded condition is a fact of the history, the same for a transport and its altered twin.
- **What it does not settle**: a correspondence that rises because a linked one is paid (S127 item 4 (b); S113's shared instructions); "other things in the population being equal" is read through Θ, by hand here (I199). S128's P1 (H with stages) is not needed for the smaller wording used.

## 7. What is unsure

- **The encodings are this job's.** Every case of sections 4 and 5 sets by hand which occurrences represent what, which holding is a record of which, and the rate fact (I90). The verdicts follow from the copy's definitions; whether the encodings fit the cases (the checker as a record of its writers; a peahen's preference as representing the survival condition; a copied formula as a transfer) is argument.
- **No flip in the suites is by construction** of I198 and I199 (a case with no boundary or rate fact keeps the original's reading). Read strictly, text 129's L522 would leave every such case's provenance open; nothing here decides between the two.
- **I201** (C applied to Con as well as Sel) makes construction boundary-relative (section 5, item 11). S127's sketch named only D12.1's exclusion and D12.3; the other choice is set out.
- **The rote-content finding** (item 9) and the **student's copy** (item 12) follow from the copy's D12.3 and Deploy; whether the owner wants either is the owner's word. If not, "entered whole" would need narrowing (for example to processes, as the text sentence says, and not held content), which the formal sketch S127 gave does not do.
- **The program's trace** (`prepares`) is not located inside or outside a boundary in the tag histories; a trace is taken to be inside.
- **The map** moves only S117's eight units at the S72 boundary; no other unit was re-examined by hand, though the sweep found no Avida unit whose verdict rests on a history this job changed.
- The counts agree with S127's, which was done by hand from the same units; agreement checks the program against the hand count, not the verdicts themselves.

## 8. What was done

- Read: decisions S72, S83, S84 and Claude's readings; S127's two files; S128's results (P1 to P3, the teacher finding, the warning); S117's results, data and map, its tools (the feeding and the build scripts); text 107; the formal core, claims and program after round 4; the S61 terms.
- Written: the text copy (section 1.1); the core and program copies (1.2, 1.3); in `results/S129 Reading C carried into copies/`: `suite runs.json`, `suite boundary sweep.json`, `the provenance claims at every boundary.json`, `map feeding under Reading C.json`, `what Reading C commits the theory to - computed.json`; the corrected map beside S117's; this file; plain file 129; seven tools `tools/s129_*.py`.
- Computer time: five whole-suite runs of about 8 minutes each (two at a time), the sweep (about 4 minutes, three times) and the case scripts; no Avida.
- Failures caught before commit: a first check of FC83 at every boundary reported 624 cases of Sel and Build at one holding; all were records with a trace of their own, an encoding D12.3 does not cover and FC83's family does not contain, present on the whole history too; the check was restricted to FC83's family (0 failures). The first sweep recorded which histories change but not how; it was rerun twice, to classify the changes and then to split them by cut. The first comparison of the two S104 case scripts set the original's output against a scratch copy that could not find text 103 (it reads it from beside its own folder); the baseline was laid out as the original expects (a link to `tests/`) and the scripts rerun: byte-equal.
