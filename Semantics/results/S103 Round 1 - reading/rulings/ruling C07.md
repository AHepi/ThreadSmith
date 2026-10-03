# S103 Round 1 — ruling on C07 (L123)

*Written on 27 September 2026 by a fresh Opus 5.5 checker that built nothing of this round, read no reply before this task, and rules on no other candidate of it (rule 5 of `results/S103 Round 1 - how the replies will be read, written before sending.md`). This file obeys decision S23 except where it quotes the text, a reply, a case or the owner. Nothing here is settled (S28): this is a ruling on the arguments the two replies make, open to the critical review of rule 12 and to any later criticism.*

## The ruling

**FIX.** Line 123 of file 99 changes from

> - a **causal assignment** has a signature that changes under intervention on its output port and under replacement of the component, and is invariant under observation edits;

to

> - a **causal assignment** has a signature that changes under intervention on its output port and is invariant under observation edits;

The change deletes the words "and under replacement of the component" and the comma after them. The new wording is GLM's variation at reply line 154, byte for byte. Mimo wrote the same words with the comma kept (reply line 172).

**On Mimo's VARIES:** Mimo's rival (reply line 156, its closing line) rewords the sentence and changes nothing the theory needs from it. On that reading the sentence is easy to vary in its wording, in the plain sense of the brief (section 5, item 1), not in the text's defined sense (L317). That is recorded. The rival is not adopted because it is not clearer (below). The FIX does not come from the rival. It comes from the fault that Mimo's own fault check names: the replacement clause does no work. GLM's reply argues against that fault, and this ruling finds that argument does not hold (rule 7, below).

## What was read

- File 99, `tests/99 The semantics, standing alone.md`, md5 74f4a4c7619345747f4fa976ddac9548 (checked before reading; not written to): lines 1–200 whole, and every other line that uses a signature, a cause, a port's role or a replacement (L245, L269, L325, L327–L331, L347, L520, L552–L558).
- The part 1 brief, `tests/S103 Round 1 - trying to vary the strong candidates - part 1, Parts 0 and II.md`: section 1, the C07 entry (lines 143–149 of the brief) and section 5.
- The reading rule, whole.
- The tabulation's C07 section (`results/S103 Round 1 - reading/tabulation.md`, lines 631–737) and its header.
- The replies: `s103_vary_mimo_1.response.txt` lines 152–176 (C07), 178–218 (C08 and C09, which name C07's replacement clause and C07's pattern); `s103_vary_glm_1.response.txt` lines 137–161 (C07), 163–207 (C08 and C09). No other passage of any reply names C07 in a way that bears on this ruling. The lines found were Mimo 256 and 262, on C11, and GLM 223, on C10. No `.reasoning.txt` file was opened.
- `records/Semantics - Decisions.md`, S20 to S35.
- The S98 ledger's entry for L123.s1 ("no change recorded") and its neighbours in `line-up/groups/02 Organizations and their changes (Part II).md`.
- The S81 case book (`tests/S81 Case book - the 52 cases, situations and fixed verdicts, as the tested agent sees them.md`), searched for cases that turn on cause, measurement, reading or intervention. O4, O6, O7 and O9 were read whole. The S89 candidate cases were searched in the same way; none turns on a signature.

## The sentence and what the theory needs from it

L121 introduces three bullets: "What ordinary language calls a cause, a measurement, a rule or a constitutive status are families of signatures". L127 says what they are: "These are descriptions of patterns in (K), not additional data." A signature is defined at L116 by \(\operatorname{sig}_C(j)=\{(a,b,L_j(a,b)):(a,b)\in C\}\). L119 says: "A signature is built from a component's relation under each \((a,b)\in C\), not from the values its ports take in a solution". So a signature "changes under" an edit when the component's relation at that edit differs from its relation at the baseline.

The C07 bullet has three clauses:

1. The signature changes under an intervention on the component's output port.
2. It changes under replacement of the component.
3. It is invariant under observation edits.

These are the definitions the clauses rest on:

- L103: "An edit that sets a port replaces the component assigning that port; it does not add an equation beside an incompatible one. A changed rule is a changed component."
- L109: "A port is an **output** of component \(j\) when its value is determined by \(L_j\) given the other ports of \(V_j\) across \(B\)". Also: "A port is an **observation** when \(A\) contains an edit that alters the relation reporting it without altering what it reports, that is, when the component assigning it has a measurement's signature (below)."
- L119: "An edit that sets a port replaces only the component that assigns the port (above), not the relations of the components that read it".

The rest of the text uses this pattern for four things:

- L37 tells a cause from a correlation: "A correlation has no component that responds to an intervention on its supposed input; a cause does."
- L57 tells a cause from a rule: "a rule's application changes when the rule is edited and not when the world is intervened on; a cause's assignment changes under intervention."
- L127 tells the part that produces an outcome from the part that reads it: "change only the reading and the part it reports stays as it was; change the part and the reading follows. Which of the two an account offers as producing an outcome is fixed by that signature, not by the account's wording."
- L325 fixes production and direction: "An intervention on \(L\) replaces its component and leaves \(H,\theta\) unchanged."

## Each side (rule 7)

### Mimo: VARIES, with a fault check that finds a clause doing no work

- **Rival (line 156):** "- a **causal assignment** has a signature that moves when an edit sets its output port or replaces the component, and that observation edits leave unchanged;". Mimo says that "an edit that sets" is the wording of L103 and L109, that all three clauses stay, and that the rival "Breaks nothing."
- **Variations that break:**
  - "input port" breaks L103 with L109. A port whose setting changes \(j\)'s signature is one that \(j\) assigns, which makes it \(j\)'s output. The contrast with C08's measured port is also lost.
  - "variable under observation edits" breaks L109 and L127.
- **Fault check (lines 170–174):** "'and under replacement of the component' applies to every component, since (K) builds the signature from \(L_j\)". Dropping the clause "breaks nothing" (wording at line 172). Mimo then adds "But L127 allows descriptions that include general features … and C08, C09 carry the same general clause in their own words. Inertness, not contradiction." Mimo keeps the clause in its closing rival.
- **On C08 (line 196):** "The bullet's second clause, like C07's replacement clause, applies to any component under (K); its discriminating partner is the first."

### GLM: HOLDS

- **Polarity swap (line 142):** breaks L127's test and its last sentence, and breaks L37.
- **"input port" (line 148):** breaks L103, because the edit replaces the component that assigns the input, "not the causal component". It also misdescribes the responsiveness that L37 makes the difference between a cause and a correlation.
- **Replacement clause dropped (line 154):** "Without it, a signature sensitive only positionally — because the output-setting edit replaces the occupant (L103) — would count as causal while the relation depended on nothing about the component itself". GLM says that L127's verdict "needs the assignment tied to the component". It also says the clause "is also what lets L57 pair cause with rule in component-sensitivity ('A changed rule is a changed component', L103)".
- **Faults sought (line 159):** the first clause is not idle. It "locates the sensitivity at the *output* port", in contrast with L124, and the pattern obtains only where \(C\) contains such pairs (L37). There is no circularity.

### Between them

The readers agree on the two variations that break: the input port and the swapped polarity. They also agree that the first clause does work. They differ on one point: whether the replacement clause does work.

Mimo says the clause does no work. That claim holds, for four reasons:

1. **The first clause already contains a replacement.** By L103, "An edit that sets a port replaces the component assigning that port". By L109, a component's output port is the port its relation determines. So an intervention on the output port is itself a replacement of the component, and clause 1 already names a replacement under which the signature changes. The C07 bullet's own clause 1 edit is therefore a case of its clause 2.
2. **Every other replacement changes every component's signature.** The signature is the component's relation under each pair (L116, L119). Replacing a component replaces that relation, whatever the relation was. So the clause holds for any component whose replacement \(C\) contains. That is Mimo's point, and it is why the clause marks no family off from another. The other two bullets say the same of their own families: L124 "variable under edits to the measuring relation", and L125 "variable under edits to the rule", with L103 "A changed rule is a changed component".
3. **The measurement is kept out without the clause.** Clause 1 with clause 3 separates the causal family from the measurement. Setting a reading replaces the relation reporting what the reading reports (L103), and it leaves unchanged what the reading reports. That makes it an edit that "alters the relation reporting it without altering what it reports" (L109), which is an observation edit. A measurement's signature changes under that edit. So a measurement can meet clause 1 only by failing clause 3, and the replacement clause adds nothing to this.
4. **No sentence of file 99 uses the clause.**
   - L37 speaks of a component that "responds to an intervention on its supposed input".
   - L57 says "a cause's assignment changes under intervention".
   - L127's test changes "only the reading" or "the part".
   - L151's production question has "a \(C\) containing interventions on upstream ports".
   - L269 speaks of a relation "replaced by an intervention".
   - L325 says "An intervention on \(L\) replaces its component".

   None of these needs the signature to change under a replacement other than the intervention.

GLM's argument that the clause ties the assignment to the component does not hold. The positional sensitivity GLM finds in clause 1 applies just as much to the replacement clause. Replacing a component changes its signature whatever the component's relation was, so the clause ties nothing to the component that clause 1 leaves untied (points 1 and 2 above). Where the text does tie an assignment to its component, it does so through (K) itself ("the signature of component \(j\)", L113 and L116), through the port roles of L109, and through clause 3.

GLM's appeal to L57 also points the other way. L57 names change under an edit to the component as the *rule's* mark ("a rule's application changes when the rule is edited"). It names change under intervention as the cause's mark ("a cause's assignment changes under intervention"). So L57 does not give the cause a separate sensitivity to replacement for C07's clause 2 to carry. As for L127's verdict ("fixed by that signature, not by the account's wording"), it turns on the reading-or-part test, which clauses 1 and 3 carry (point 3).

Mimo's reason for tolerating the clause ("Inertness, not contradiction", resting on L127 and on C08 and C09) does not hold for C07 either:

- L127 says the bullets are "descriptions of patterns in (K), not additional data". That allows a general feature in a description. It does not make a clause that marks nothing and that nothing uses do any work.
- In C08 and C09, the second clause is the only side of the pattern that varies. Without it, "invariant under interventions on the measured port" would be met by any component that \(C\) leaves untouched. So there the general clause does work. In C07, the varying side is carried by clause 1, which is itself a replacement (point 1).

This ruling says nothing about the second clauses of C08 and C09. Their own checkers rule on them.

**There is a third reading.** On it, the clause asks \(C\) to hold a replacement of the component other than the intervention on its output, such as a change of mechanism. On that reading the clause is not idle. But it asks of the contract what no passage of the text asks:

- The worked case of production and direction (L325) states a contract of interventions on \(H\), \(\theta\) and \(L\), with no change to any component's mechanism.
- The fixed case O9 (below) has exactly two edits, the bent needle and the wire, and no such replacement.

On this reading too, dropping the clause removes something that nothing in the text uses.

## The rival: a rewording, not a different claim

Mimo's rival keeps all three clauses:

- "changes" becomes "moves".
- "under intervention on its output port" becomes "when an edit sets its output port". This is the wording of L103 and L109 for the same edit, which L325 calls an intervention: "Under \(A\) containing interventions on \(H\) and \(\theta\), these ports are inputs", with L109 "an **input** under \(A\) when \(A\) contains an edit that sets \(v\) directly".
- "and under replacement of the component" becomes "or replaces the component".
- "is invariant under observation edits" becomes "that observation edits leave unchanged".

On the text's own usage, the rival picks out the same components on every contract. It is a rewording that changes nothing the theory needs from the sentence, so on this reading the sentence is easy to vary in its wording. That is recorded.

**Why neither the text's wording nor the rival is kept, and why this wording is.** The text's wording carries a clause that does no work (above). The rival keeps that clause and is not clearer, for three reasons:

- "moves" is used nowhere in file 99 of a signature.
- "when an edit sets its output port or replaces the component" can be read as "moves under one or the other". That is weaker than "changes under … and under …".
- The rival gives up the words the neighbouring lines use: L57 "a cause's assignment changes under intervention", L124 and L125 "invariant under interventions on", and L347 "invariant under interventions on \(Z\) and variable under edits to \(C_r\)".

The new wording keeps the text's own words, so it keeps those links. It removes only the idle clause. That leaves each of the three bullets with one side that varies and one that stays the same:

- the causal assignment varies under intervention on its output port and stays the same under observation edits;
- the measurement stays the same under interventions on the measured port and varies under edits to the measuring relation;
- the rule application stays the same under interventions on the world and varies under edits to the rule.

**Why this wording and not Mimo's line 172.** GLM's line 154 and Mimo's line 172 have the same words. Mimo's keeps the comma before "and is invariant", which was needed only while three clauses stood in a series. Without the comma, the bullet has the form L124 and L125 use ("invariant under … and variable under …").

## The variations and what they break

- **Input port (Mimo line 162, GLM line 148).** An edit that sets the input replaces the component that assigns the input, "not the relations of the components that read it" (L119). So a causal assignment's signature does not change under it, and the bullet would describe no component that reads its input. This breaks L103 and L119 with L109, and loses the contrast with L124's measured port. Both readers find this break, and so does this ruling.
- **Swapped polarity (GLM line 142) and "variable under observation edits" (Mimo line 166).** These give the causal family the measurement's pattern of L127 ("change only the reading and the part it reports stays as it was"), and they break L109's observation port. Both readers find these breaks, and so does this ruling.
- **Replacement clause dropped (Mimo line 172, GLM line 154).** This breaks nothing, for the reasons above. It is the FIX.

## What depends on the sentence, and what becomes of each

- **L37** ("A correlation has no component that responds to an intervention on its supposed input; a cause does. That is a difference in edit-response, which is what the semantics asks about (Part II, 'Kinds are edit-signatures')."): unaffected. It uses intervention only.
- **L57** ("a cause's assignment changes under intervention. That is a difference in edit-signature (Part II)"): unaffected. The new bullet says what L57 attributes to the cause, in L57's own verb.
- **L109** (an observation port, glossed through the measurement's signature): unaffected. C07 still uses observation edits, as before.
- **L121** (the lead-in): unaffected.
- **L124 and L125** (C08, C09): unaffected. Their second clauses are not touched by this ruling.
- **L127** ("These are descriptions of patterns in (K), not additional data. … Which of the two an account offers as producing an outcome is fixed by that signature, not by the account's wording."): unaffected. The reading-or-part test runs on clause 1 and clause 3, which both stay.
- **L151** (a production question with interventions on upstream ports): unaffected.
- **L245 and Argument 1 (L552–L558)**: unaffected. They use (K), not the causal family.
- **L269** ("A **table of observed answers** has no component whose relation is replaced by an intervention"): unaffected. It rests on the relation replaced by an intervention, which is clause 1.
- **L325** ("An intervention on \(L\) replaces its component and leaves \(H,\theta\) unchanged"): unaffected. The new bullet asks of the contract no edit that L325 does not state.
- **L520** ("Kinds, from signatures (K).") and **L347**: unaffected.

## Cases

No fixed verdict moves. The S98 ledger ties no case to L123.s1 ("no change recorded"). These are the cases that turn on the pattern:

- **S81 O9, "The float that does two jobs".** Its verdict reads "Milan is right, Lena is wrong. The float is read by the dial and also does the work." Its two edits are an observation edit and an intervention on the float's port:
  - "Bend the needle to read 'full': the float is where it was and the valve opens as before."
  - "Hold the float up with a wire: the dial reads 'full' and the valve stays shut."

  Those are exactly the edits of the new wording's two clauses. The float's component changes under the wire, which sets its port (L103), and stays the same under the bent needle. The dial's component changes under the bent needle. No other replacement appears, so the verdict needs no replacement clause.
- **S81 O6, "The fever and the thermometer".** The verdict, that her second statement "mistakes the instrument for the illness", rests on two things. One is warming the thermometer, an edit to the measuring relation under which "the reading climbs while the child shivers exactly as before". The other is the cool bath. The first is clause 3 and L127's test, and both stay.
- **S81 O4, "Dormitive power, with a meter".** The recalibration is an observation edit ("every syrup reads ten points higher, and people who take the syrup sleep exactly as before"). The verdict, that Dario "has said almost nothing about why the syrup causes sleep", rests on it. Unaffected.
- **S81 O7, "Salt on the icy step".** Production is shown by spreading and sweeping the salt (interventions upstream, L151), and no instrument is involved. Unaffected.
- **The text's own worked cases**, L269 (the table), L325 (pole and shadow) and L331 (the two balances): unaffected. None needs the replacement clause.

## The owner's decisions

- **S20:** nothing here lists, counts, grades or ranks rivals. Each wording stands or falls on what it breaks or leaves idle, and no side is weighed by how many readers take it.
- **S21:** the new wording says nothing about what must happen to any candidate.
- **S23:** the new wording removes words and adds none. It contains no word or idea the decision forbids.
- **S25–S27:** physical possibility is not touched.
- **S28:** the ruling is open, like every sentence of the text.
- **S33–S34:** nothing here proposes anything about what hard to vary covers. "A part that does no work" is the brief's own plain test (section 5, item 3), not the text's defined term. No point of either reader on C07 is parked.
- **Values:** not touched.

## Quotations compared with file 99

Every quotation of file 99 in this ruling was compared by program with file 99. Each was found on the line given, with LaTeX delimiters and bold marks set aside where the quotation includes them. The lines are 37, 57, 103, 109, 113, 116, 119, 121, 123, 124, 125, 127, 151, 269, 325 and 347. The quotations of the replies were compared with the reply files, and those of the cases with the S81 case book, and each was found. Where a quoted passage holds double quotation marks of its own, they are set here as single quotation marks: Mimo line 170, GLM line 157, L37's "Kinds are edit-signatures", and O9's "full". No book is quoted.

## Where this file stands

The reading rule's rule 11 names `results/S103 Round 1 - rulings/ruling C<nn> L<line>.md`. The task names this path, `results/S103 Round 1 - reading/rulings/ruling C07.md`, and this path was used. No second copy was written. Nothing was committed.

## Result

- **Ruling:** FIX, at L123.
- **Old:** `- a **causal assignment** has a signature that changes under intervention on its output port and under replacement of the component, and is invariant under observation edits;`
- **New:** `- a **causal assignment** has a signature that changes under intervention on its output port and is invariant under observation edits;`
- **Easy to vary:** Mimo's rival rewords the sentence and changes nothing the theory needs, so the sentence is easy to vary in its wording on this reading. That is recorded, and the rival is not adopted because it is not clearer. The FIX comes from the fault Mimo named and GLM contested: the replacement clause does no work.
- **Parked (S34):** none.
