# S103 Round 1 — the cases re-read on the new text

*Written on 27 September 2026 by a fresh Opus 5.5 case checker, under rule 13 of `results/S103 Round 1 - how the replies will be read, written before sending.md` ("The cases the changed sentences bear on … are re-read on the new copy by a fresh agent"). Filled as it went. Not committed. The old text is `tests/99 The semantics, standing alone.md` (md5 74f4a4c7619345747f4fa976ddac9548); the new text is `tests/103 The semantics, standing alone, after round 1.md` (md5 f31ebb1f050783f1a84f6136cec20fcd). Both md5s were checked before reading, and neither file was written to. The fixed verdicts come from the S81 case book (O1–O52, md5 4f488d149e44669240d5db546c8e946a), the S89 candidate cases N1–N25 (md5 b2e535777976a511935430bd089ba500; numbered O53–O75 under decision D8 of the change list, with N6 and N14 left out) and D3-T (`final.md`, md5 6b211dea40d735abf50426e56344f161; O76). None of them is changed here. This file obeys decision S23 except where it quotes the text, a case, a record or the owner. Nothing here is settled (S28).*

## In brief

The two texts are the same line for line except at four lines (found by `diff`; each line is quoted whole below). Every case that could turn on one of those four lines was re-read on both texts.

**No case moves.** No case moves toward its fixed verdict, none moves away, and none becomes silent. Each case gives on the new text what it gave on the old, on the same lines.

- **L123 (the causal assignment).** The cases that turn on the pattern are O9, which the S81 determination ties to this very sentence, and O4, O6 and O7. **SAME** for all four. For O9 and O7 one reading of the old sentence is closed. On that reading, which the C07 ruling records as its "third reading", the deleted clause asked the contract to hold a replacement of the component other than the intervention. Neither case's contract holds one, so on that reading the old bullet did not reach the float or the salt. The verdicts never rested on the bullet reaching them. **Watch, O4:** a contrary reading that S81 testers raised now meets L123's wording on every reading. It still fails at L255 and L273, as before.
- **L443 (the explanatory aim).** The cases are O13, which the S81 determination and two S81 testers tie to this sentence, N10 and the text's own worked case at L628. O13: **SAME**, and the literal reading of the old grammar is closed. The S81 readers had already read the sentence the way the new wording puts it. N10: **SAME**. It is silent in both texts on the case's word "knowledge", which neither text uses, and on the formal conditions both texts give the same. L628: **SAME**. The new first disjunct is in the worked case's own words.
- **L471 ((CT2)).** No case turns on it. O14, N20 and the others that turn on retention were read. They use (CT1), tolerances or (T2), never the third clause of (CT2). **SAME.**
- **L520 (the Account gloss).** Every case verdict that turns on Account rests on Part V (L255, L257, L262, L269, L273), not on the gloss. **SAME** throughout. For the cases whose verdicts turn on non-circular dependence or non-vacuity, one reading is closed: the old gloss taken at its word, "Account, from fidelity under change". No record shows anyone reading a case that way.

These counts describe the work. They order nothing (S20).

## Marks

- **SAME.** The new text gives the fixed verdict, or leaves the same part of it silent, as the old text does, on the same lines.
- **SAME, a reading closed.** As SAME. In addition, a reading of the old sentence under which that sentence did not give, or seemed to deny, a step the verdict could use is no longer open on the new sentence. The verdict never rested on that step: other lines gave it in both texts.
- **MOVED TOWARD.** The new text gives a part of the verdict that the old text gave only on one reading of a sentence of its own, where another reading, taking the sentence as written, denied it.
- **MOVED AWAY.** The new text gives something against a part of the verdict that the old text gave.
- **NOW SILENT.** The new text does not give a part of the verdict that the old text gave.
- **Watch.** A reading the new wording leaves open that would move the case, with the reason it is not the reading the text gives.

## How the cases were found

- **Where the four sentences stand in earlier files.** These are their lines in file 10, file 11 and files 99/103, found by search:

  | sentence | file 10 | file 11 | file 99 = file 103 |
  |---|---|---|---|
  | the causal assignment | L140 | L125 | L123 |
  | the explanatory aim ("epistemic obligation" in files 10–11) | L446 | L435 | L443 |
  | (CT2) | L474 | L463 | L471 |
  | "Account, from fidelity under change (E)" | L521 | L512 | L520 |

  Each of the four stands in the same words in files 10 and 11 (checked by search). Only L443's was changed before file 99, by the scrub: "explanatory aim" and "an account" where files 10 and 11 have "epistemic obligation" and "a correct account" (ledger D-699, D-689).
- **The S81 determination** (`results/S81 File 11 against every case - outputs/determination/01 …`). It ties each case to the lines it turns on. It cites F10 L140 for **O9** only ("F10 L140: 'a **causal assignment** has a signature …'"), and F10 L446 for **O13** only. It cites no file-10 or file-11 line of (CT2) or of the Account gloss for any case.
- **The S81 Stage 1 returns** (`returns/s81_1C_A`, `_1C_B`, `_1K_A`, `_1K_B`), searched for the four sentences. "Causal assignment" is used in reading O7 (1C_A, 1C_B), O9 (1C_A, 1K_A) and, as a contrary reading, O4 (1C_A). The old L443 sentence is quoted for O13 (1K_A, 1K_B). Nothing quotes (CT2) or the Account gloss.
- **The S98 ledger.** It records no case. Of the four units, L123.s1, L471.s1 and L471.s2 are headed "no change recorded". L520.s7 holds one superseded vocabulary record (D-663). L443.s2 holds four vocabulary records from the scrub (D-591 "open for the owner" on the name, and D-689, D-699, D-715). None names a case.
- **The change list's CASES AT RISK** (`tests/Revision 2 - change list, draft of 23 September.md`), for the entries next to the four sentences. W7.2 (file 11 L512 s1, the lead of L520): "None; no case cites L512". W19.1 and W30.1 (the kinds paragraph beside the causal bullet): O9, O10 and O22 are compared "within one organization". W23.2 (after (EK)): O13 and N10. W39.1, W20.2, W11.1 and W9.1 (non-circular dependence, the table): O2, O4, O5, O7, O33, N2, N3, N8, N17, N23 and N25. W7.4 and W7.5 (the dependence order): O37 and O49. W25.1 (the tolerances): N24. No entry touched any of the four sentences themselves.
- **The S95 and S96 case re-reads.** S96 marks N10 NOW SILENT on the name at l. 443. It cites no l. 123, l. 471 or l. 520 for any case.
- **A program search** of all 78 case texts (O1–O52, N1–N25, D3-T) for the words each sentence turns on:
  - cause, intervention, replacement, measure, reading, meter, instrument, sensor, signature, kind;
  - aim, deploy, correct, repair, create, knowledge;
  - retain, keep, repeat, invariant, "any number", "any size";
  - circular, restate, "written down", vacuous, empty, scope, limit, idle.

  Every hit was read. The cases below are those it left.
- **The six S103 returns** name no case. Their only "O1" is the obstruction tag (O1) at L546.

---

## 1. L123 — the causal assignment (C07)

**Old (L123):** `- a **causal assignment** has a signature that changes under intervention on its output port and under replacement of the component, and is invariant under observation edits;`

**New (L123):** `- a **causal assignment** has a signature that changes under intervention on its output port and is invariant under observation edits;`

**What the change does to a case.** Clause 1 (intervention on the output port) and clause 3 (invariance under observation edits) stand in both texts. By L103, "An edit that sets a port replaces the component assigning that port", so on the C07 ruling's points 1 and 2 the deleted clause was met by the intervention itself, or by any component whose replacement the contract holds. On those readings nothing changes for any case. On the ruling's "third reading", the deleted clause asked the contract to hold a replacement of the component other than the intervention on its output, such as a change of mechanism. On that reading a component whose contract holds no such edit fell outside the causal family as the old bullet worded it. The new bullet has no such clause, so that reading is gone. The bullets are, in both texts, "descriptions of patterns in (K), not additional data" (L127). So falling inside or outside the family never by itself gives or denies a verdict.

### O9 — The float that does two jobs

**Fixed verdict.** "Milan is right, Lena is wrong. The float is read by the dial and also does the work."

**The S81 ties.** The determination cites F10 L140 (this sentence) and F10 L144 (now L127). Testers 1C_A and 1K_A read the float as having "the causal assignment toward the valve" or "a causal assignment to the valve".

**Old text.** The case has exactly two edits.

- "Hold the float up with a wire" sets the float's port. So it replaces the float's component (L103) and is an intervention on its output port: clause 1.
- "Bend the needle to read 'full'" is an observation edit. By L109, a port is an **observation** when \(A\) contains an edit that "alters the relation reporting it without altering what it reports". The float's component is unchanged under it: clause 3.
- The dial's component changes under the bent needle and stays as it was under the wire. By L119, "An edit that sets a port replaces only the component that assigns the port (above), not the relations of the components that read it". That is L124's measurement: "invariant under interventions on the measured port and variable under edits to the measuring relation".
- L127 then gives the verdict: "change only the reading and the part it reports stays as it was; change the part and the reading follows. Which of the two an account offers as producing an outcome is fixed by that signature, not by the account's wording."
- The deleted clause, on the ruling's points 1 and 2, was met by the wire. On the third reading, O9's contract holds no other replacement of the float's component, so the old bullet did not call the float a causal assignment on O9's contract. The verdict still stood on L127 and on L151's production question.

**New text.** The same lines give the same verdict. The new bullet's two clauses are exactly the case's two edits: the float's component changes under the wire and is invariant under the bent needle.

**Mark: SAME, a reading closed** (the third reading of the deleted clause). (L103, L109, L119, L123, L124, L127, L151)

### O4 — Dormitive power, with a meter

**Fixed verdict.** "Dario has a useful measure and a reliable prediction. He has said almost nothing about why the syrup causes sleep. The index is the sleepiness itself, observed in a mouse."

**Old text.**

- The recalibration is an observation edit ("every syrup reads ten points higher, and people who take the syrup sleep exactly as before"). So the reading has a measurement's signature (L124, L127).
- The measure answers the identification question and not the production question (L151: "whether the measured part also produces the outcome is the production question, and the first answer is not the second").
- "The index is the sleepiness itself" is non-circular dependence. L255: "The target's answer does not appear, at the declared grain, as an unanalysed boundary input or as a component". L273 adds: "So does an account whose only substantive component restates the answer it was asked for".
- S96 read the case on l. 127, l. 151 and l. 255, and these lines are the same in files 99 and 103.

**New text.** The same, on the same lines.

**Watch.** S81 tester 1C_A wrote as its contrary: "one could read the index as a causal assignment that passes the production contract". Tester 1K_A marked SPLIT on a reading that "makes it a coarse cause, like the salt in O7". The component the index tracks, the syrup's strength, has its port set by dilution. It is unchanged by the recalibration. So in the new text it meets both clauses on every reading. In the old text it met clauses 1 and 3, and missed the family only on the third reading of the deleted clause. That is the first step of the contrary reading, and the verdict never denies it: the verdict speaks of "why the syrup causes sleep". The second step, from there to "Dario has a coarse account", fails at L255 and L273 in both texts, as tester 1C_A's own reply and the S81 reconciliation found (O4: both readers AGREE under file 11). Nothing in the change reaches L255 or L273.

**Mark: SAME** (with the watch). (L124, L127, L151, L255, L273)

### O6 — The fever and the thermometer

**Fixed verdict.** "Her first statement is a good reason to believe there is a fever. Her second statement mistakes the instrument for the illness."

**Old text.**

- Warming the thermometer is an observation edit (L109): "the reading climbs while the child shivers exactly as before". So the reading has a measurement's signature (L124, L127).
- The cool bath is an intervention on the child's temperature. The temperature's component changes under it (clause 1), and it is unchanged under the warmed thermometer (clause 3).
- So the second statement puts the reading where the temperature is. L127's last sentence gives "mistakes the instrument for the illness".
- The first statement rests on L151's identification question: "A measure that identifies an outcome, together with a prediction of the outcome from it through a transport faithful on the contract, answers the identification question". That line is not among the four changed ones. How the scrub's vocabulary meets the verdict's own words "reason to believe" is outside this check (the change list's W6.1 watched it).

**New text.** The same. The case holds no edit that the deleted clause named.

**Mark: SAME.** (L109, L124, L127, L151)

### O7 — Salt on the icy step

**Fixed verdict.** "Ines has a genuine explanation, a coarse one. The salt is what produced the melting."

**The S81 ties.** The determination cites F10 L32 (now L37: "A correlation has no component that responds to an intervention on its supposed input; a cause does.") and F11 L279 (now L277). Testers 1C_A and 1C_B read the salt as "a causal assignment's signature".

**Old text.**

- Production is given by L37, by L151's production question ("a \(C\) containing interventions on upstream ports") and by L277: "It does not exclude a coarse dependence for omitting finer workings or an instrument: an account at a coarse grain is an account of the coarse question".
- The salt's component has its port set by spreading and sweeping (clause 1). No instrument is involved, so clause 3 excludes nothing.
- On the third reading of the deleted clause, O7's contract holds no replacement of the salt's component other than those interventions, so the old bullet did not reach the salt. The testers' route through the bullet then failed at that clause, while the verdict stood on L37, L151 and L277.

**New text.** The same lines give the verdict, and the testers' route through L123 is open on every reading.

**Mark: SAME, a reading closed.** (L37, L123, L151, L277)

### Read, and not reached by the change at L123

| case | what the verdict turns on, in both texts | why L123's change does not reach it | mark |
|---|---|---|---|
| O10 Two thermostats | L119: "two components that differ only in those values are of one kind on \(C\), whatever the difference is called" (W30.1's CASES AT RISK) | kinds of components within one organization, not the causal family | SAME |
| O22 Two knobs, one linkage | the lead is part of the linkage's relation (W30.1) | no signature family is asked | SAME |
| N23 (O73) The planets tonight and a thousand years ago | direction from the admitted edits (L103, L109, L151, L325), the reversed calculation (L271), non-circular dependence for the forward account (W20.2) | the contracts the records read it on hold interventions on positions (W20.2) and no replacement of a law. The verdict's "together with the laws of motion" is (E)'s non-circular dependence (L255), not a replacement clause of the causal bullet | SAME |
| O46 The cable that used to be a spring | L307: "a component reassigned to a new target after a deletion belongs to a new candidate with its own assessment" | the replacement is of a candidate's component, and the verdict is about which candidate. No signature family is asked | SAME |
| O42 New board, old memory | L473: "A replaced part that preserves the declared continuity leaves the same system" | a replaced physical part and continuity, not a signature | SAME |
| O19 The diagram in his hand | active routes (L375) | which input the cut depended on, read from the history | SAME |
| O25, O39, O52 (meters); O27, O40, O50 (sensors) | attribution (L375, L441); episodes and a test's background and instruments (L429; K3 at L395) | a meter or sensor there is a record or a test's instrument, not a component whose family is asked | SAME |
| N16 (O66), N17 (O67) | L255, L269, L273, L277 | "causal" there names a physical trace, not the Part II family | SAME |
| D3-T (O76) | Argument 3 (L572, L574) and L195 | designs that pass or fail a test, not signature families | SAME |

### The text's own worked cases on L123

- **L269**, the table: "A **table of observed answers** has no component whose relation is replaced by an intervention; it fails (F1) under any contract containing one." This rests on clause 1. SAME.
- **L271 and L325**, the reversed calculation and the pole and shadow: "An intervention on \(L\) replaces its component and leaves \(H,\theta\) unchanged." The contract holds interventions on \(H\), \(\theta\) and \(L\), and no other replacement. SAME.
- **L331**, the two balances, and **L347**, constitutive rules ("invariant under interventions on \(Z\) and variable under edits to \(C_r\)"): these are measurement and rule patterns, untouched. SAME.
- **L626**, Argument 10. The persistence components "respond to displacement and velocity edits as things do, and are invariant under occlusion as things are". That is the new bullet's two clauses: interventions on the ports they assign, and an edit that changes what the field reports without changing the thing. The text names it "the signature of things", not the causal family, and its contract holds no replacement of a persistence component other than those edits. The text's conclusion reads the same in both texts. SAME.

---

## 2. L443 — the explanatory aim (C27)

**Old (L443, second sentence):** `An explanatory aim requires an account, or the correction of a use through one, to be deployable.`

**New (L443, second sentence):** `An explanatory aim requires a deployable account, or the correction of a use through one.`

The bold heading "**Created explanation.**", the next sentence and (EX) at L447–L449 are the same in both texts.

**What the change does to a case.** There are two kinds of aim.

- **An aim to hold an account.** Old and new give the same condition for it: the old words read "requires an account … to be deployable", the new "requires a deployable account".
- **An aim that a use be corrected through an account.** The old words, taken as written, asked the correction itself to be deployable. The C27 ruling shows that this is ill-typed, since Deploy (L403) takes a content. The new words ask for the correction of a use through a deployable account.

(EX), ProducesVia (L453) and Deploy (L403) are unchanged, so every case whose verdict turns on them reads the same.

### O13 — Two plumbers

**Fixed verdict.** "Ben's act stopped the leak. Ana's explanation is correct and produced nothing. Nobody here made a repair that came from an explanation."

**The S81 ties.** The determination cites F10 L446 (this sentence, in file 10's words) and notes that "The conjuncts Account and ProducesVia of (EK) are separate (F10 L452)". Testers 1K_A and 1K_B quote file 10's form of the sentence and read it as asking a repair through the account. 1K_A: "Created explanatory knowledge would need a repair produced through a deployed account". 1K_B: "Created explanatory knowledge needs the account to produce the repair (ProducesVia)".

**Old text.**

- "Ben's act stopped the leak" is ProducedBy (L441): "\(\operatorname{ProducedBy}\) is met when an active route (Part IX) runs from \(\Delta\) to the repair".
- Ana's explanation, in the text's word, is "an account". L441 gives the three attributions: "An account that produced nothing, an act that repaired without an account, and a repair produced through use of an account are three different attributions."
- "Nobody here made a repair that came from an explanation" is (EX)'s ProducesVia (L453): "\(\operatorname{ProducesVia}(\Delta,c,o;\xi,\xi')\) is met when an active route that runs from \(\Delta\) to the repair of \(o\) contains the relevant binding of \(c\)." No route from Ana's account ran to the stop.
- The old L443, taken as written, would put deployability on the correction when the leak aim is read as explanatory. The S81 readers did not read it so. The verdict does not turn on it either way: if the leak aim is not explanatory, (EX) is not in play; if it is, ProducesVia fails.

**New text.** The same lines give all three sentences. The new second disjunct says in its own words what the S81 readers read: the correction of a use goes "through" a deployable account. That is where the case turns (ProducesVia).

**Mark: SAME, a reading closed** (the old grammar taken as written). (L441, L443, L447–L449, L453)

### N10 (O61) — The burned notebook

**Fixed verdict.** "Yes, she created knowledge: she worked out, correctly and for the first time, why that design would fail. No, that knowledge does not exist now."

**What earlier re-reads found.** S95 and S96 marked the case NOW SILENT, relative to draft 5, because the scrub removed the word "knowledge" and marked the name "Created explanation" as provisional, for the owner (S96: "(EX) still carries a provisional name (l. 443)"). The ledger's D-591 on that name is still "open for the owner".

**Old text.**

- L443 reads "**Created explanation.**" with no bracket. The bracket marking the name as provisional was removed when file 99 was made (`tests/99 The semantics, standing alone - what was removed.md`, item 17).
- The word "knowledge" stands nowhere in file 99 (search).
- So the text still neither uses the case's word nor says which of its terms answers to it, and the case stays silent on its word.
- On the formal conditions, Halima's aim is of the first kind: to hold an account of why the design would fail.
  - The old words ask that account "to be deployable". She held it at \(\xi'\) in her notebook and her mind (Deploy, L403).
  - "Does not exist now" is no Deploy at a later \(\xi\): no system "holds a representation of \(c\)" (L403).

**New text.**

- "Knowledge" stands nowhere in file 103 either, and the heading is the same.
- For the first kind of aim the new words, "requires a deployable account", ask the same as the old.
- (EX), L403 and L453 are unchanged.

**Mark: SAME** (silent in both on the case's word; the same in both on the formal conditions). If the owner rules that the case's word is (EX), both answers read the same on either text. (L403, L443, L447–L449, L453)

### The worked case of Argument 10 (L628)

**The text's conclusion.** "If it repairs the aim 'possess a deployable account of re-emergence after occlusion' while protecting 'predict the displacements that occur,' then (P) is met; and since \(S_1\) is an account on its contract and deployable, (EX) is met."

**Old text.** The aim is of the first kind. The old sentence asks for "an account … to be deployable", which \(S_1\) is, so (EX) is met.

**New text.** The same. The new first disjunct, "a deployable account", is in the aim's own words.

**Mark: SAME.** (L443, L628)

### Read, and not reached by the change at L443

| case | what the verdict turns on, in both texts | why L443's change does not reach it | mark |
|---|---|---|---|
| O20, O25, O26, O39, O52 (attributions of stopping a leak) | ProducedBy and active routes (L375, L441) | no explanatory aim is asked (W23.1: "ProducedBy is unchanged") | SAME |
| O32 Found aloud, drawn later | attribution of a found dependence and a drawn bypass | "(EK) is not asked" (W23.2) | SAME |
| O12 The rota | L455: "Repairing an aim repairs it and says nothing about how anyone appraises the aim" | the worth of an aim, not what an explanatory aim requires | SAME |
| O31 The wrong valve | L405: "A small binding newly prepared inside received content is construction of that binding, and the rest of the content keeps its inherited provenance." | the verdict attributes a correction (received vs hers), not an explanatory aim | SAME |
| N15 (O65) The miscopied notes | L403, L405, L407 (S96), L397 | the verdict turns on Deploy and Build. If her question 2 were read through (EX), her aim would be of the first kind, which reads the same on both texts | SAME |
| N18 (O68) Two footbridges | L223, L395, L397, L429 (S96) | the case defines its own "problem" ("something he or she must now understand and fix"). L429 gives a recognized difficulty from any failed claimed aim, explanatory or not | SAME |
| N19 (O69) The novelist's two demands | L429, and (P) at L438 (S96: l. 429, l. 437) | her aims are about prose and pace, not explanatory aims | SAME |
| N11 (O62) Two students | Build, Origin (G) | (EX) is not asked | SAME |

---

## 3. L471 — (CT2) (C28)

**Old (L471, second sentence):** `\(F\) is monotone; \(C\subseteq F(C)\) is the invariant form; the union of post-fixed sets is the greatest fixed point. (CT2)`

**New (L471, second sentence):** `\(F\) is monotone; \(C\subseteq F(C)\) is the invariant form; the greatest fixed point is the union of the sets \(D\) with \(D\subseteq F(D)\). (CT2)`

**No case turns on (CT2).**

- No case text holds "fixed point", "post-fixed", "(CT", "RetReal" or "monoton".
- No record ties a case to file 10 L474, file 11 L463 or l. 471.
- In file 99, (CT2) is named only at L471 and L546.
- The new clause names the same sets as the old one read as the C28 ruling reads "post-fixed". Read the other way, the old clause would have made a claim with counterexamples, and no case used that reading.

The cases that turn on retention were read:

| case | what the verdict turns on, in both texts | why the change at L471 does not reach it | mark |
|---|---|---|---|
| O14 The phrasebook | L403: "A narrow retained use is what it is"; owned capability, L475 ("requires an owned retained realization or an owned, physically admitted, finite construction of one") | a retained realization of one narrow task is (CT1). The greatest fixed point is not used | SAME |
| N20 (O70) Keeping count with string | (T2) at L363 ("Without a modulus, no accumulated bound follows."), tolerances at L479 ("Capability at a given tolerance does not imply possibility at every tolerance."), L461 | the rounding method's lengths return into themselves after each step, which is (CT1)'s return condition. A reader could state the first method's failure through the largest retained set, but no record does, and the verdict is given without it. The sets named are the same in both texts | SAME |
| N13 (O64) The parrot | Deploy "as a retained capability" (L403), relay (L405, L409) | retention is used through Deploy, not (CT2) | SAME |
| N24 (O74) Two sealed sorts of matter | L75, L461, L495 ("in the sense of (CT1)"), L497 | (CT1), not the third clause of (CT2) | SAME |
| O42, O49 | continuity (L473); owned capability and the order (L475, L526) | (CT1) through owned capability, not (CT2) | SAME |

The text's own lines: L477 ("retention is applied to the inquiry-enabling organization") and L546 read the same in both texts.

---

## 4. L520 — the Account gloss (C29)

**Old (L520, seventh sentence):** `Account, from fidelity under change (E).`

**New (L520, seventh sentence):** `Account, from fidelity under change, non-circular dependence and non-vacuity (E).`

**What the change does to a case.** The tag (E) points in both texts to L262, "\operatorname{Account}(\mathcal E)\iff \text{(F1)}\land\text{(F2)}\land\text{(A)}\land\text{NonCircular}\land\text{NonVacuous}. \tag{E}", with its conditions at L233–L257. Every case verdict that turns on Account rests on those lines, which are the same in both texts.

The old gloss, taken at its word on the pattern of its own list, said that Account is made from fidelity under change. On that reading a faithful restatement would be an account. The new gloss also names the two conditions that keep an account apart from a faithful restatement.

No record reads any case through the gloss. So the change gives no verdict and takes none away. For the cases whose verdicts use one of the two conditions it now names, the reading of the old gloss at its word is closed.

| case | fixed verdict (the part that uses the condition) | lines, in both texts | mark |
|---|---|---|---|
| O2 The tide table with a real bell attached | "The almanac is the answer written down." | L255, and L273 "So does an account whose only substantive component restates the answer it was asked for". W11.1 closed the same reading at the table sentence (now L269: "it is an account when it meets the other conjuncts of (E)") | SAME, a reading closed |
| O4 Dormitive power, with a meter | "The index is the sleepiness itself, observed in a mouse." | L255, L273 (as in section 1) | SAME, a reading closed |
| N2 (O54) The myth amended | "What the myth now says about the south is the sailor's report retold in the myth's terms." | L255 (W39.1: "the southern seasons are the report written into the myth") | SAME, a reading closed |
| N3 (O55) A myth about winter | "The yearly return is simply written into the terms of the bargain." | L255 (W20.2, W39.1) | SAME, a reading closed |
| N16 (O66) The domino that never falls | Answer A "restates it in terms of dominoes" | L255, L273 (S96: l. 255, l. 273) | SAME, a reading closed |
| N25 (O75) What holds the universe up | "None of the three explains what holds the universe up." | L255, L275 (a contrast no admitted edit realizes fails non-circular dependence), L161, L315 | SAME, a reading closed |
| N8 (O59) The machine that runs forever | "Only Quentin's does." | L151, L269, L315, L335, L495 (S96). W39.1 watched non-circular dependence here ("a reader may call the energy law a restatement of the answer") | SAME |
| N23 (O73) The planets | "The arrangement a thousand years ago, together with the laws of motion, explains where the planets are tonight." | the forward account meets non-circular dependence by deleting the laws (W20.2); the backward one fails (F2) (L271) | SAME |
| N17 (O67) The transistor | "B explains, and A does so only in a thin sense." | L269's "it is an account when it meets the other conjuncts of (E)" (W11.1 watched A as an encoding), L277 | SAME ("thin" was silent on the S96 repaired copy; the lines it turns on are the same in files 99 and 103) |
| O1 The forecaster who keeps finding honest limits | "Each limit is honest taken alone" | L257: "every edit the target admits that is excluded from \(C\) is excluded by a stated scope, not silently"; L159; L369 | SAME ("retreat" was silent on the S96 repaired copy; the lines it turns on are the same in files 99 and 103) |
| O5 Greta's dough | "This is a legitimate narrowing." | L43, L159, L257, L522 | SAME |
| O8 Petra's own ovens | "The limit says what she is asking about." | L43, L141, L159, L257 | SAME |
| N7 (O58) Two bakers | "Maya's limits are an honest statement of where she has seen it work." | L159, L257, L315, L317, L522 | SAME |

**The text's own worked cases.**

- **L273**: "'\(p\) because \(p\)' fails non-circular dependence".
- **L275**: a contrast no admitted edit realizes.
- **L331**: "it is circular, though the value it sets might be the target's".
- **L343**: "Non-circular dependence is met" … "Non-vacuity is met" … "The expansion is an account."
- **L536**: "conclusion-as-premise fails non-circular dependence".

Each reads the same. The new gloss names, by the text's own headings (L255, L257), the conditions that L343 checks by name. SAME.

### Read, and not reached by the change at L520

| case | what the verdict turns on, in both texts | why the change does not reach it | mark |
|---|---|---|---|
| O37 The uncited textbook | L526: "The order has no cycle and no endless descent." and its last sentence | the words "non-circular dependence" now stand at L520 as well. They name (E)'s condition at L255, where the target's answer appears as an input, not the order's cycle, which is where O37 turns. The case's circle is not a target's answer entered as a component | SAME |
| O49 Owned means capable | L475, L526; L520's last item "capability … from those", unchanged | the circle is ownership and capability, not Account | SAME |
| O33 The table with empty columns | "The table is faithful." | fidelity, which both glosses name | SAME |
| N1 (O53) The seasons and the sun god | L313: "(E) has no condition that each commitment do work." | neither gloss names a condition that each part do work, and (E) has none | SAME |
| N25 (O75), second question | the idle difference (L313, L315, Argument 2's Consequence) | not a condition of (E) | SAME |

---

## Summary

| case | changed line it could turn on | old text gives | new text gives | mark |
|---|---|---|---|---|
| O9 | L123 | the verdict (L103, L109, L119, L124, L127, L151); the float outside the old family only on the third reading | the same; the float inside the family on every reading | SAME, a reading closed |
| O4 | L123, L520 | the verdict (L124, L127, L151, L255, L273) | the same | SAME, a reading closed (L520); watch (L123) |
| O6 | L123 | the second statement (L109, L124, L127); the first on L151 | the same | SAME |
| O7 | L123 | the verdict (L37, L151, L277); the salt outside the old family only on the third reading | the same; the salt inside the family on every reading | SAME, a reading closed |
| O13 | L443 | the verdict (L441, L453) | the same | SAME, a reading closed |
| N10 (O61) | L443 | silent on "knowledge"; the formal conditions (L403, L447–L449, L453) | the same | SAME |
| worked case, L628 | L443 | (EX) met | the same | SAME |
| O14, N20, N13, N24, O42, O49 | L471 | as their own lines give (L363, L403, L461, L475, L479, L495) | the same | SAME |
| O2, N2, N3, N16, N25 | L520 | the verdict on L255, L273, L275 | the same | SAME, a reading closed |
| N8, N23, N17, O1, O5, O8, N7 | L520 | as their own lines give (L159, L257, L269, L271, L277, L315) | the same | SAME |
| the cases read and not reached (the tables above) | — | as before | the same | SAME |

## The owner's decisions

- **S20.** Nothing here lists, counts, grades or ranks rivals. The counts in "In brief" describe the work and order nothing.
- **S21.** Nothing here says what must happen to any candidate or case.
- **S23.** No word or idea the decision forbids is used, except inside quotations of the text, a case or a record. Where a case's verdict uses such a word ("reason to believe" in O6, "correct" in O13 and N10), it is quoted and its standing on the scrubbed text is not re-ruled here.
- **S25–S27.** None of the four changes touches physical possibility. The cases that meet it (N20, N24) meet it on lines that are unchanged.
- **S28.** Every mark is open. A SAME settles nothing.
- **S33–S34.** Nothing here concerns what hard to vary covers. Nothing is parked. No value is moved in or out.

## Quotations checked

Every quotation of file 99 or file 103 above was compared by program with the line given, and found there (`s103_cases_qcheck.py` in the session scratchpad: 160 checks, none failed). The quotations of lines other than L123, L443, L471 and L520 were found on the same line in both files. The four old and new wordings were found in file 99 and file 103 respectively, byte for byte. The case verdicts were compared with the case books. Where a quoted passage holds double quotation marks of its own, they are set here as single quotation marks: O9's 'full', the S81 determination's quotation of F10 L140, L273's '\(p\) because \(p\)', and the two aims quoted at L628. The S81 readers' words were compared with their returns, and the records' words (S96, the ledger, the change list, the removals list) with their files. No book is quoted.

## What this check does not show

- That a reader of the new text would reach the verdicts marked SAME. The marks come from reading the lines the verdicts turn on. No tester was run on file 103.
- Whether the old text gives, on the scrub's vocabulary, parts of verdicts whose own words the scrub no longer uses ("reason to believe" in O6, "knowledge" in N10). This check marks only what the four changed lines do to them.
- Anything about the 25 candidates that the rulings kept. Their lines did not change.
