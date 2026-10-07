# S107 Round 4 — inventions register, addendum after round 4

*Integration of round 4 (log S107; reading rule, rules 6 and 7; S36: "if implementation forces invention, that needs to be recorded"), 28 September 2026. Numbered after I191, the last number in use (register I01–I102; addenda I103–I121, I122–I166, I167–I183, I184–I191; checked by a search of results/, tests/, tools/ and records/: no I192 or higher in use). Where used: `formal core, after round 4.md`, `formal claims, after round 4.md`, `model after round 4/`, `text changes after round 4.json`. Recording an invention is not a move (rule 16). Nothing here is the text's own content.*

## Numbering (provisional id → I number)

| provisional | I | area | settled in the text |
|---|---|---|---|
| R4A1-01 | I192 | 1 | no (recorded; Con and Build do not turn on it; (EX) reads the criticism label, which L377 and L429 type) |
| R4A2-01 | I193 | 2 | yes, by L271's own words (its colon); no text change (R4A2-T1, R4INT-T1 withdrawn: second check, O2) |
| R4A2-02 | I194 | 2 | no |
| R4A2-03 | I195 | 2 | no (D7.4 only; L302 unchanged) |
| R4A3-01 | I196 | 3 | no (D16.XV writes the symbol) |
| R4A3-02 | I197 | 3 | no (an encoding for a test claim) |

The program's comments and prints keep the provisional ids (claims_s41.py, claims_r4a2.py, claims_r4a3.py); this table maps them.

**Counts.** 6 inventions, I192–I197. Settled in the text: I193, by L271's own words (second check, O2: no text change).

## The inventions

| I | fills (line; item) | choice | other choices | why this one | used by |
|---|---|---|---|---|---|
| I192 | S47's "a question occurs as potentially important and worth investigating", for the bridge (S41 Q6); I191's "no question about the brief occurred to the agent"; L13, L55 | recorded, not chosen anew: I190/I191 stand (a question about the brief that occurs is read, through Θ, as a criticism (D9.10) aimed at the brief) | (d) a question-occurrence is its own Θ label, apart from criticism, with or without an alleged defect; a criticism can be used with no question occurring (a claim taken as given, S27); (e) a question that occurs is a question found (L15, L155; L161), operative at its occurrence, so q(o) is not the brief there | under D13.8 as S41 has it, Con and Build at the output are the same under all three (FC84.new1 (a3)); (EX) reads the criticism label through CompleteCritical (FC32.new1 (f); FC84.new1 (a4)), and the text types a criticism by its alleged defect (L377; D9.10) and (EX)'s episode by "a conjectural objection" (L429); Episode of a whole chain reads q(o), which (e) sets (FC84.new1 (a4)); S47: "The math doesn't ask for anything." [second check, O1: was 'no value of (R), Sel, Con, Dec, Episode, Build or (EX) reads the labels; …'] | claims_s41.no_question_about_brief; FC84.new1 (a3); D12.2, D13.8 marks |
| I193 | L271's and L536's "the production contract" (the step's reading, in no register) | settled by L271's colon: the transport carries the intervention on the upstream port to itself ("intervening on the upstream port changes the target's downstream value but not the calculation's"); under it E_rev fails (F2) on every production contract tried, C1 and C_H (FC27.new1 (b)); L536 reports Part V | (a) every production contract under any transport: τ′ on C_H meets (E) (FC27.new1 (d)), a candidate L271 does not describe (τ′ sets the calculation's L); (c) E1's C1 alone (the integration's choice, R4A2-T1, R4INT-T1; withdrawn: it narrows Part V's sentence to one example's contract) | the colon writes which transport the line speaks of; rule 6: nothing in the text changes [second check, O2: was 'E1's C1 … (L325)', (b) the other choice] | E1's mark; FC27, FC27.new1 |
| I194 | Pin (I184) at a pair whose own edit alters k (B9) | counts as a pin (I184 as registered) | exempt there, I136's "some-exempt" at one pair: every pin of c_L on C2 would go (FC23.new4 (d)) | I184's registered choice; the exemption was registered for Slot's quantifier (I136), not for Pin; (E) reads neither | D6.3 (Pin; mark); FC23.new3 (d), FC23.new4 (d) |
| I195 | D7.4's designation of E_v (N1) | δ_v, the designation the operation carries δ_E to, declared with t_v and Γ_v | (a) quantified, ∃δ_v, as D14.7 (I180) and D16.4 (I183): an edit moving the answer onto another port keeps Acc (FC42.new1 (d)); (b) δ_E unchanged: no value where the edit renames the port (FC42.new1 (c)) | L231's pattern ("the transport the operation carries t to"); L253: the query is held fixed; D7.1 carries δ_E | D7.4; core.boundary; FC42.new1 |
| I196 | "an argument not using (E)" (L536, L538; D16.XV's Uses) | the symbol: no leaf or form of α uses (E), Acc of any candidate | the instance: no use of Acc(ℰ) for the candidate ℰ at issue (the program's reading before round 4; W5's "does not use (E) on ℰ") | the text names (E), not (E) on ℰ; D16.XV writes the symbol; the readings part only on an argument whose only use of (E) is Acc(ℰ′) (FC30.new1 (h)) | D16.XV (mark); claims_s41.not_using_E (USES_READINGS, default "symbol"); FC30.new1 (a), (b), (g), (h); FC23.new2 (f) |
| I197 | the myth about winter and the seasons (file 93, file 96; K1 of the addendum), encoded | target: ports sun ∈ {high, low}, temp ∈ {warm, cold}; c_sun by (edit, boundary) as the tilt gives it, c_temp warm iff high; edits 1 (June), dec; boundaries N (the Greeks'), S; the query reads temp. The myth: one part writing the answer (a slot), or two parts (the bargain places Persephone, grief sets the cold; π reads her place off the sun's height) | the answer read off a calendar port; months finer than two; the myth's parts given no counterparts in the target (none encoded) | the smallest target on which the Greeks' contract and the south part the two, and both readings of "assumes its own answer" can be computed | FC72.new2; D9.7's mark |

## Registered inventions whose standing changes (not new)

| I | after round 4 | where |
|---|---|---|
| I184 | Pin's "t translates (a,b)" now also inside D6.3's ∀ (A2 F1), so Slot ⟺ Det_C ≠ ∅ ∧ Pin at every pair holds of D6.3 as written; its reading at a pair whose own edit alters k recorded as I194 | D6.3; FC23.new3 (a), FC23.new4 |
| I136 | its exempt reading, at one pair, is I194's other choice (not taken) | D6.3 |
| I191 | kept; recorded beside two other readings (I192) | D12.2, D13.8 marks; FC84.new1 (a3) |
| I20 | the designation now carried in D7.4 (δ_v, I195) | D7.4 |
| I180, I183 | ∃δ kept in D14.7, D16.4: a different use (a created content, a universal class), I195's other choice (a) | D14.7, D16.4 |
| I147 | ℰ_c's designation written δ_Conn (A3 F5; notation) | D9.10 |
| I14 | κ keeps its one sense, D5.1's value maps; (Elim)'s kind-label written kl (A3 F6; notation) | D16.XV (Elim) |
| I151 | "subhistory" is D11.3's, no longer among D0.2's primitives (A3 F3) | D0.2 |
| I162 | T′ unchanged; Build reads Held under every reading in D18.1's graph (A3 F2); FC83's build_at keeps round 2's reading under the rejected cuts U and K (pair 5) | D18.1 |
| I65 | E1's C1 and C_H: under the transport L271's colon describes, E_rev fails (F2) on both (I193; FC27.new1 (b)) | E1 |
| I189 | on a target with one part, ℰ_two fails (F1) (FC23.new5): I189's target holds the parts, as S44's words have it | FC23.new2, FC23.new5 |
