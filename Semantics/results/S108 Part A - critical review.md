# S108 Part A - critical review

*Rule 8 of `S108 Part A - how the replies will be read, written before sending.md`. A fresh Opus 5.5 agent that built nothing of Part A, 28 September 2026. Read whole: the rule; decisions S20–S53; the tabulation; the four "variants computed" files; the dependency map (.md, .json); the candidate list. Nothing here changes the theory (rule 11); nothing is ruled (the orchestrator's, rule 9). "Candidate" or "explanation" for what the theory judges; "model" below only in the program's folder names (S43). Not reviewed: the Sonnet 5.5 trial (S53), a separate job.*

## 0. Checks made

| check | result |
|---|---|
| rule 11: theory files | `tests/107` c7af964c…, formal core d6e6ec62…, the rule 0909c53d…, frozen set 367c4b1f…, template 0c5ad262…, four replies (md5s as the tabulation) unchanged; `model after round 4/` clean against HEAD; every Part A commit (dd73829 … dc3c193) touches only `results/S108 Part A - …` paths |
| copies | each section copy differs from the program after round 4 only in the files its setup names (section 1 also `claims_a.py`; section 3 also `claims_r3a1.py`, `claims_r3a3.py`, where FC84.new1 and FC90.new1 live) |
| "model" for a candidate | none in the candidate list or the map; S23's words only inside quotations of the owner or a reply |
| quotations of the owner in the list | each found verbatim in `records/Semantics - Decisions.md` |

**Reruns** (in the section copies, `python3 -B -m model.run … --scale 4 --time-cap 45 --no-write`, PYTHONHASHSEED=0, under `timeout`; no file of the copies changed, no `__pycache__`):

| copy | claims | readings | agrees with the file |
|---|---|---|---|
| section 1 | FC23.new2, FC22 | none, V1.1 | yes: (a) two-part sign and FC22 (b) M13 not as claimed under V1.1 |
| section 2 | FC23.new1, FC107 | off, V2.4 | yes: (h) counterexample; FC107 text Acc True → False, status kept |
| section 3 | FC72, FC90.new1 | none, V3.1, V3.4 | yes: FC72 (a)–(c), (e) move under V3.1; FC90.new1 (a) under V3.4 |
| section 4 | FC30.new1, FC23.new2 | none, V4.2 | yes: FC30.new1 (c) fails by construction; FC23.new2 (f) not as claimed |
| section 2 | new cases (§A): FC28.new2's weathervane, the two-part sign with days as boundaries | off, V2.3 | new; objection O1 |

## 1. Objections

| id | weight | what | exact fix |
|---|---|---|---|
| O1 | matters | **C5 (V2.3) is left unflagged; it drops the owner's weathervane and sign where the change is a boundary.** The list marks it "not computed". Computed here (§A): FC28.new2's D_vane (wind W as boundaries; the program's own "Q15's contrast"), C = {(1,b_still),(1,b_north)}, the identity candidate, Γ = {cP} or {cW,cP}. Off: Acc T, witness ((1,b_north),[cP]). V2.3: Acc F (Dep F; F1, F2, A, NonVacuous T). The two-part sign with Monday/Tuesday as boundaries (B = {mon, tue}, A = {1}) gives Acc T → F too. By V2.3's form no candidate meets (E) on any {1}×B contract. M13 and `claims_s106`'s sign stay only because the program encodes the wind as the edit e and Tuesday as the edit tue | In the candidate list: flag C5 with **S41 Q15** ("Yes, it can be explained") and **S44** ("In either case, it is an explanation."), each "where the change (the wind, the day) is read as a boundary; with it read as an edit (M13, `claims_s106`) nothing moves". Add C5 to §2 in plain words. Change "Seven are flagged" to eight. In the map: add to §2's V2.3 row and §6.3 "rests on: whether the owner's changes are edits or boundaries" |
| O2 | matters | **C6 (V2.4) and C11 (V4.1) name the wrong case as S44's.** They mark ℰ_one "the one-part shop sign (S44)" and flag S44. The owner's S44 case is ℰ_two ("a red part … and a blue part …"; FC23.new2 (a) "S44: the two-part sign"). ℰ_one is the program's companion case, R3-Q1's side 1 (`claims_s106.py`, ℰ_one's docstring). Under 'every' ℰ_two **stays** under V2.4 (section 2 §2) and V4.1 (section 4 §4). It drops only under 'some', 'some-exempt' and 'some-exempt-set' (FC23.new2 (a): round 3's (E) (T,F,F,F)). §2's plain words put S44's "In either case" beside the one-part example | In C6 and C11: remove "(S44)" after the one-part sign. Decision named: **S45** ("Yes, take the test out"). S44 only "under D6.3's quantifier read other than 'every' (FC23.new2 (a)), where the owner's two-part sign drops too". In §2 (C6, C11): say that the owner's red-part/blue-part sign stays under the program's reading and drops under the other three. Section 4's §3 and §9 use the same label ("the owner's one-part sign (S44)"): note it for the records |
| O3 | matters | **e3.25a (V3.5 → Dec, "contradicted under T′") holds only in the program's encoding of a construction trace.** In that encoding the trace is a label at one occurrence (`claims_b._con_at`: `trace[o]`, Prepares a primitive, I56), so h′ = {o_t} carries CT(h′,t) and the record clause is never read for a held t. D12.2 reads "a construction trace **of h′**"; D13.3 and L405 make a trace the tuple (h′, the controlled processes, the incoming carriers, the bindings constructed, the resulting representation). Where the trace spans an unrecorded change of contract, h′ must hold the change, and D13.8's record clause decides Con. The program cannot state such a trace | e3.25a: "contradicted where the trace lies at o_t (the program's Prepares, I56); not settled for a trace spanning a change of contract". Settle: make Prepares(h′,o,·) require h′ to hold the trace's occurrences, then recompute V3.5 on chains with an unrecorded change inside the trace. Also amend: map §2, bullets 2–3 ("screened by Held at o_t" → "…when the trace lies at o_t"); C9's "With D12.2's cut T′ (and T): nothing …" (add "for a trace at o_t"); map §6.3 (add the row) |
| O4 | matters | **e4.29 "V4.5 moves L538.s2, computed" shows no move, and it hides a finding about the state after round 4.** Section 4 (E4.5c, §4): neither E5 encoding is exposed "now or under V4.5". Every candidate meeting (E) is unexposed by definition: Acc ⇒ F1 ∧ F2 = Faithful_C(t). FC62 has E5 meet (E). So L538.s2 ("Eliminative explanation (Part VII) is the exposed case") does not hold of E5 as encoded, off and on alike | e4.29 → "V4.5 independent of L538.s2 (computed)". Add to map §6: "L538.s2 [S4] is not met by E5's encodings under (Nec)'s current shape; no candidate meeting (E) is exposed (section 4, E4.5c)". This is for the orchestrator's records and the paused review rounds, not for change in Part A (rule 11) |
| O5 | minor | **e1.08 "V1.1 blocks D13.4, D13.5 [FROZEN]" overstates.** Both definitions stay readable. "A content matches itself" is FC85 (a)'s claim, not D13.4's words: D13.4 says only "read with c fixed (L413) and … not claimed symmetric (FC85)", and L413 states no reflexivity. Computed: FC85 (a) fails; (N) can call a content already held new | e1.08 → "blocks FC85 (a) [claim]; changes with D13.4, D13.5 [FROZEN]". Remove D13.4 and D13.5 from map §3's "blocks computed" list, from §2's "frozen words" bullet, and from C1's "FROZEN items it blocks" (D4.4 stays, so C1's standing is unchanged) |
| O6 | minor | **e2.13 "V2.5 blocks L211.s3, computed" contradicts its own evidence.** The evidence ends "the transport is no longer declared, so L211.s3 still holds formally". The .json keeps "in effect"; the md drops it | Kind → "changes with (in effect)": what counts as declared moves (FC30.new1 (e): Dec → Sel) |
| O7 | minor | **e4.25 "V4.4 blocks L556.s3 [FROZEN], claimed only" is not the reply's edge.** The reply called L556.s3 "the nearest" and "about Argument 1's proof". Section 4 found no FROZEN item that holds "not using" or Uses | Move e4.25 to "rows with no edge" (a 'none found' finding); drop L556.s3 from map §3 |
| O8 | minor | **Two "contradicted" edges contradict only the reply's wording; the movement itself is computed.** e3.09b: V3.2 moves D10.1, and problems grow (FC47.new1); only "fewer" is contradicted. e2.04b: V2.2 moves (E), T→F on 23/20/4 (s04); only "such a candidate now fails (E)" is contradicted, by one witness with a critical singleton outside the block | e3.09b: standing computed, note "the reply's direction contradicted". e2.04b: retarget to "every candidate realizing L299.s1 fails (E)": contradicted as worded; computed for candidates whose only witness is a block of two or more. Update §5 |
| O9 | minor | **e4.19 "V4.3 changes with L17.n2, L49.n3, L61.n2, L69.n3, FC25.new2: contradicted".** The four sentences write being an explanation, which V4.3 redefines; they change with it at relayed holdings (e4.18: 24 + 24 worked, 2,692 chain holdings). The same edges are marked computed for V4.1 (e4.01) and V4.2 (e4.13). Only the reply's reason, E_enc with no record (FC25.new2), is contradicted | Split e4.19: the four sentences computed; FC25.new2 and "the encoding table stops being an explanation" contradicted |
| O10 | minor | **C2 (V1.5) leaves out a decision section 1 named.** Section 1 §9 lists S41 Q6 (the bridge's fixed brief) as not computed. A brief stipulated for the engineer is "declared" in L155's sense ("stipulated by the modeller, with neither selection nor construction") | In C2 add: "S41 Q6 ('Yes, it can'): not computed (FC84.new1 builds no candidate; the brief's ρ_p is not recorded)" |
| O11 | minor | **Map §6.1 lists the 17 untouched middle definitions without saying which bear on the explanation definition.** From the map's own D18.1 ancestors: D6.9 is upstream of (E); D11.2, D11.3 of Dec; D6.8, D9.1, D9.2 also of Expl, (Suff), (Nec). D5.7 (Faithful_H) is read by Dec's statement | Mark these seven in §6.1 and put them first in §7's list for round 2 |
| O12 | minor | **Gaps the map does not list.** (a) The bridge (FC84.new1), E2, E3, E4 and E7 carry no candidate and no (E), so no variant's effect on them as explanations is computed (sections 1, 2, 4 say so). (b) The edit-or-boundary reading of the owner's cases (O1). (c) The four whole-suite runs were made by the computing agents' own scripts. The rule gives that job to Sonnet workers who must agree by script (sections 2 and 3 say so). The eight reruns here agree | Add (a)–(c) to map §6.3 |
| O13 | minor | **The map misdescribes the history behind V3.6's counts.** Map §6.3 and e3.30a give S108-3-I4 as "stated construction := t's own". The counts (22 worked; 1,013 / 881 / 232 / 1,670) come from 'Sel-parts', whose stated construction is "all but E's last component" (`s108_s3_cases.py` l.11–12, 94). With the stated construction t's own, t does not move; only t′ does | Correct the wording. Add: "the counts equal the population meeting (E), by construction of the history". The same holds for V2.5's 'nothing tried', V3.5's tag history, and V4.2's and V4.3's histories. Each row of the list names its history, so only the map's §2 and §6.3 need the note |

## 2. Where I find nothing to object to

- **Rule 11.** No text, formal core, claim, program, rule, reply or decision file was written (§0).
- **The tabulation.** Its three flags (V1.6: another section's item and a new sentence, S40; V1.7: D3.5 [FROZEN] in effect; V2.8: names L315.s7 [FROZEN]) follow rule 4. Its quotation table (§9) and its S23 and "model" notes (§10) stand.
- **The implementations.** Each deviation from a variant as written is stated and recorded as the agent's own invention (S36): V1.5 (S108-1-I5), V3.4's CT (S108-3-I2), V3.6 (S108-3-I3, I4), V4.3 (S108-4-I3), V4.5 (S108-4-I5), V4.6 (S108-4-I6), V4.7 (a toy, S108-4-I7), V2.7 (P-S2-2). I found no variant implemented other than as written without saying so.
- **The other contradicted edges.** Each checked against the core: e2.05 (Prob reads Riv and NotOut, not Acc: D10.1, D8.3); e2.06a (identification (I1) at L329.s3 reads no (E)); e3.20a (CT reads Prepares, not ExplUse, D12.2); e4.02 (L269–L277 speak of (E)); e4.05, e4.28 (E5), e1.04, e1.20.
- **Flags on C1, C7, C8, C12.** The decisions are named with the owner's words, and the computed cases match them: C1 drops the owner's two-part sign (S44; FC23.new2 (a) rerun); C7 is S41 Q2, in part; C8 is S41 Q2, under S108-3-I2; C12 is S41 Q2. The flag on C2 is right, with O10's addition.
- **The list's §3.** The owner's words beside V2.6, V2.7, V3.1, V3.3 and V3.8 are quoted verbatim, and none of these five is wrongly left out as a candidate (they move neither (E) nor being an explanation).

## 3. Is a second round of Part A needed?

**Yes.** Rule 10's condition holds: 473 of 577 middle items are untouched, 32 edges are claimed only, and O1 and O3 add two gaps a run can settle. Before the round-2 rule is written:

1. The orchestrator rules on the tabulation's three flags (rule 4); V1.6, V1.7 and V2.8 wait on that ruling.
2. The readings each candidate rests on are computed under their other choices: S108-1-I5 (C2); S108-3-I2 (C8); the trace's extent and the tag encoding (C9, O3); S108-3-I4 (C10); S108-4-I3 (C13); edit or boundary for the owner's cases (C5, O1).
3. Variants go first to the untouched middle definitions that are upstream of the explanation definition: D6.9, D11.2, D11.3, D6.8, D9.1, D9.2, D5.7 (O11).
4. The suite's two D6.4 blind spots (e2.38, e2.39) get cases.

One round of four agents cannot cover every untouched item, so the round-2 rule should name which gaps it takes.

## 4. Unsure

- O1 turns on reading the wind and the day as boundaries. The theory's word "boundary" and FC28.new2's own encoding favour that reading for the wind; M13 and `claims_s106` chose edits. Which reading the owner meant is the owner's.
- O3 is an argument from the words of D12.2, D13.3 and L405 plus the program's code. No run settles it, because the program cannot state a trace that spans a change.
- O4 is a reading of L538.s2. If "the exposed case" names only a kind that (Nec) must answer, and not one that is exposed, the finding narrows to e4.29's kind.

## A. The check behind O1 (run in `S108 Part A - computation/section 2 model/`, S108_S2_VARIANT = off, then V2.3)

```
from model.core import Org, Question, Candidate, Translation, PortQuery, ONE, account, NC2
def Lf(j, a, b):   # FC28.new2's D_vane, as the program builds it
    if j == "cW": return frozenset([({"b_still": 0, "b_north": 1, "b_gusty": 2}[b],)])
    return frozenset([(0, "n"), (0, "s"), (1, "n"), (2, "s"), (2, "e")])
D = Org("D_vane", ["W", "P"], {"W": (0, 1, 2), "P": ("n", "s", "e")}, ["cW", "cP"], {"cW": ["W"], "cP": ["W", "P"]},
        ["b_still", "b_north", "b_gusty"], [ONE], lambda a2, a1: ONE, Lf)
p = Question(D, [(ONE, "b_still"), (ONE, "b_north")], "b_still", PortQuery(), "P")
lam = {"cP": (frozenset(["cP"]), {"W": Translation(["W"]), "P": Translation(["P"])})}
c = Candidate(D, p, {v: Translation([v]) for v in ("W", "P")}, {ONE: ONE}, {b: b for b in D.B}, lam, ["cP"], "P")
print(account(c, detail=True), NC2(c, witness=True))
```

| encoding | off | V2.3 |
|---|---|---|
| D_vane, Γ = {cP} | Acc T; witness ((1,b_north),[cP]); answers ⊥, n | Acc F: Dep F; F1, F2, A, NonVacuous T |
| D_vane, Γ = {cW,cP} | Acc T; witness ((1,b_north),[cW]) | Acc F: Dep F |
| sign, B = {mon,tue}, A = {1}, red part r, blue part u (identity candidate) | Acc T; witness ((1,tue),[r]) | Acc F: Dep F |

Reviewed by one Opus 5.5 agent under rule 8, 28 September 2026. Nothing ruled; nothing applied to the theory (rule 11).
