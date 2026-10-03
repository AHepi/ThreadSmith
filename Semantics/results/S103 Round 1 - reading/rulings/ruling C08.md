# S103 Round 1 — ruling on C08 (L124)

*Written on 27 September 2026 by a fresh Opus 5.5 checker that built nothing of this round, read no reply before this task, and rules on no other candidate of it (rule 5 of `results/S103 Round 1 - how the replies will be read, written before sending.md`). This file obeys decision S23 except where it quotes the text, a reply, a case or the owner. Nothing here is settled (S28): the ruling is a choice made on the reasons given, open to being taken up again by whoever chooses to.*

## The ruling

**KEEP.** Line 124 of `tests/99 The semantics, standing alone.md` (md5 74f4a4c7619345747f4fa976ddac9548, checked before reading) stands as it is:

> - a **measurement** has a signature invariant under interventions on the measured port and variable under edits to the measuring relation;

- **Mimo's rival is a rewording that changes nothing the theory needs from the sentence.** On this reading the sentence's *wording* is easy to vary (in the plain sense the brief gives, not the text's term at L317), and that is recorded here. The rival is not clearer than the text's wording, so the ruling is KEEP, not FIX (rule 5).
- **What the sentence says could not be varied without a break.** Each variation of its content, tried by either reader or here, broke L109 or L127.
- **Mimo's fault point does not show a defect.** The point is that the second clause does not tell one component from another. So it is, among components; but that clause carries L109's requirement that the admitted edits hold one that alters the reporting relation.
- **No case verdict moves.**

## What was read

- **File 99:** lines 85–127 whole, and L37, L49, L57, L151, L159, L269–L271, L325, L329 and L347, where the item's words or its pattern recur.
- **The tabulation** (`results/S103 Round 1 - reading/tabulation.md`): the C08 section (its lines 736–828), and its sections "Passages that name a candidate outside its own section" and "Points that allege a defect, whatever the closing line".
- **The replies.**
  - Mimo, `s103_vary_mimo_1.response.txt`: line 1 (its standing note) and lines 152–220. That span holds C07 to C09, because Mimo's C07 and C09 sections name C08.
  - GLM, `s103_vary_glm_1.response.txt`: lines 137–207 (C07 to C09).
  - No reasoning file was opened.
- **The part 1 brief:** its entries for C07 to C09. For C08 it gives "observation, defined by a measurement's signature: L109; component, port: L85–L105".
- **The reading rule.** Also the owner's decisions S20 to S28, S33 and S34 in `records/Semantics - Decisions.md`.
- **The S98 ledger, Part II group.**
  - L124.s1 is "no change recorded".
  - L109.s4's "that is" gloss was added from an S96 ruling. A formal wording proposed at the same time was superseded.
  - L127.s4–s5 were added at place M13 of the S81 determination. That place ties them to cases O4, O6 and O9, all recorded there as "AGREE→AGREE".
- **The S81 case book** (`tests/S81 Case book - the 52 cases, situations and fixed verdicts, as the tested agent sees them.md`): O4, O6 and O9.
- **The S101 graph.** C08 stands in the node "families of signatures", with L121, L123 and L125. No loop through it is read from the wording.

## The sentence in (K)'s terms

(K) builds a component's signature from its relation and not from values. L119: "A signature is built from a component's relation under each \((a,b)\in C\), not from the values its ports take in a solution". Two further lines fix what the two clauses of L124 come to:

- L103: "An edit that sets a port replaces the component assigning that port; it does not add an equation beside an incompatible one."
- L119: "An edit that sets a port replaces only the component that assigns the port (above), not the relations of the components that read it".

In what follows, \(j\) is the component that assigns a reading and \(m\) is the port it reads.

**The first clause.** "invariant under interventions on the measured port" says that setting \(m\) leaves \(L_j\) as it was. By L103 and L119, that holds exactly when \(j\) is not the component that assigns \(m\). This clause does three jobs:

- **It fixes the direction:** the reading does not produce the part it reads.
- **It is the (K)-side of L109's "without altering what it reports".** Editing \(j\) alters how \(m\) is assigned only if \(j\) is what assigns \(m\).
- **It is what L127's "change the part and the reading follows" needs.** The reading follows because its relation is left as it was and takes the part's new value.

**The second clause.** "variable under edits to the measuring relation" says the contract holds edits under which \(L_j\) differs. Under (K), an edit to \(j\)'s relation alters \(j\)'s signature. So this clause does not tell one component from another. What it tells apart is a contract that admits a reporting edit and a contract that does not. It is:

- the (K)-side of L109's "\(A\) contains an edit that alters the relation reporting it";
- the first step of L127's "change only the reading and the part it reports stays as it was".

So L124 states the pattern that L109 names with "has a measurement's signature (below)", and that L127 restates in values: "In particular, a part that reads or reports another part has a measurement's signature: change only the reading and the part it reports stays as it was; change the part and the reading follows."

## The two readers' sides (rule 7)

**Mimo closes VARIES** (reply line 198), with the rival of its line 182. Its reasons:

- The rival "Keeps both clauses and both roles, which L109's gloss needs ... and L127 restates".
- A role swap breaks L109. A polarity swap breaks "L127 with L119".
- Its fault check finds L109's gloss "definitional, not circular". It adds that "The bullet's second clause, like C07's replacement clause, applies to any component under (K); its discriminating partner is the first."

**GLM closes HOLDS** (reply line 187). Its reasons:

- The polarity swap "Breaks L127 outright".
- A value-tracking wording breaks L109, which "needs the measurement's signature statable as an edit-response pattern in (K)'s coordinates".
- Using "observation edits" "creates a circle with L109".
- The standing wording avoids that circle "by using "the measured port" and "the measuring relation" as plain glosses fixed by signature conditions".

**Where they agree and differ.** The readers do not meet on the same ground:

- GLM tried only variations of what the sentence says. Mimo tried a variation of its idiom as well as variations of what it says.
- On what the sentence says they agree: every such variation broke L109 or L127.
- They differ only on whether a change of idiom counts. Rule 5 answers that: a rewording that changes nothing the theory needs shows the sentence easy to vary on this reading, is recorded, and is a FIX only if it is clearer.

This ruling weighs the reasons on each side. It gives no weight to how many readers stand on a side.

## The rival offered as working (Mimo, reply line 182)

```
- a **measurement** has a signature that interventions on the measured port leave unchanged and edits to the measuring relation change;
```

**It is a rewording, not a different claim.** Under (K), each pair of phrasings says the same of \(\operatorname{sig}_C(j)\):

- "invariant under interventions on the measured port" and "that interventions on the measured port leave unchanged": every intervention on \(m\) in \(C\) leaves \(L_j\) as it was.
- "variable under edits to the measuring relation" and "that ... edits to the measuring relation change": an edit to \(j\)'s relation alters \(L_j\).

One might read "variable under" as "can vary", and "change" as "each such edit alters it". For what the theory uses, the two readings coincide under (K). An edit that left \(j\)'s relation equal would not be an edit to the measuring relation in the sense the clause needs. The text also treats an edit under which relations stay equal as making no difference to kinds (L119: "an edit under which the two relations stay equal does not separate the components").

Both clauses, both roles and the direction stay. No line of the text reads differently with the rival, and no case verdict does. So the sentence's wording is easy to vary on this reading, and that is recorded. This concerns the idiom only. It proposes nothing about what hard to vary covers (S34).

**Why the text's wording and not the rival's.** The rival is not clearer:

- **It would split one list across two idioms.**
  - The idiom is shared with L125, "- a **rule application** has a signature invariant under interventions on the world and variable under edits to the rule."
  - It is shared with L347, which restates the rule pattern in the text's own formal words: "Its signature under (K) is invariant under interventions on \(Z\) and variable under edits to \(C_r\)."
  - L123 uses "is invariant under observation edits".
  - The bullets under L121 describe patterns in (K) in one idiom. Changing C08's alone would make one list use two idioms for one kind of statement, and would part C08 from L347.
  - Mimo offers the same change of idiom for C07 and C09. Those are for their own checkers. Even with all three changed, L347 would keep "invariant under ... variable under".
- **It can be misread.** The rival's relative clause makes "a signature" the object of both "leave unchanged" and "change", with the second verb at the very end: "edits to the measuring relation change;". That can first be read with "change" as intransitive, as if the edits themselves change. The text's "invariant under X and variable under Y" has no such reading.
- **Its one gain is plainer words.** But "invariant" and "variable" are the words the text itself uses for a relation staying equal or not, at L119's last sentence and at L347.

So: KEEP, not FIX.

## Variations said to break

The reasoning here is about what each variation alone breaks, not about how many were tried (S20).

**Mimo's role swap** (reply line 188) breaks L109 and L127:

```
- a **measurement** has a signature that interventions on the measuring relation leave unchanged and edits to the measured port change;
```

- If edits to the measuring relation left \(j\)'s signature unchanged, \(C\) would hold no edit that alters the relation reporting the reading. That goes against L109's "\(A\) contains an edit that alters the relation reporting it".
- If setting the measured port changed \(j\)'s signature, then by L103 \(j\) would be what assigns \(m\). The reading would then produce the part it reports, against L127's "change only the reading and the part it reports stays as it was".

**The polarity swap** breaks L127, as both readers say, and L109 with it. Mimo (reply line 192) and GLM (reply line 168) give it in the same words:

```
- a **measurement** has a signature variable under interventions on the measured port and invariant under edits to the measuring relation;
```

- "variable under interventions on the measured port" makes \(j\) the component that assigns \(m\), by L103.
- "invariant under edits to the measuring relation" says an edit to \(j\)'s relation leaves that relation as it was. Under (K) that holds only if \(C\) holds no such edit.
- So L127's "change the part and the reading follows" fails, since the reading follows only if its own relation stays. L127's "change only the reading and the part it reports stays as it was" fails too.
- L109's "that is" would then equate an observation with a pattern that admits no reporting edit.

**GLM's value-tracking wording** (reply line 174) breaks L109, L121 and L127:

```
- a **measurement** is one whose reading follows what it reports and changes when its own relation is edited;
```

- It drops "has a signature" and speaks of the reading's values. L119 builds signatures from relations, "not from the values its ports take in a solution".
- L109's "has a measurement's signature (below)" and L121's "families of signatures" would then point at a pattern stated in values.
- L127's "These are descriptions of patterns in (K), not additional data" would no longer describe the bullet.

**GLM's "observation edits" wording** (reply line 180) breaks L109 and L127:

```
- a **measurement** has a signature invariant under observation edits and variable under edits to the measuring relation;
```

- GLM finds a circle here, since L109 defines an observation by the measurement's signature.
- It is more than a circle. By L109, an edit that alters the measuring relation while leaving what it reports as it was is an edit of the kind that makes the reading an observation. That is how "observation edits" at L123 is read from L109. So the wording asks one signature both to stay and to vary under the same edits.
- It would also give the measurement the causal assignment's third clause at L123 ("is invariant under observation edits"), and blur the difference L127 relies on ("Which of the two an account offers as producing an outcome is fixed by that signature").

**Dropping the second clause** was tried here, to weigh Mimo's fault point. It breaks L109:

```
- a **measurement** has a signature invariant under interventions on the measured port;
```

- With it, any component that does not assign \(m\) would have the pattern, whether or not \(C\) holds any edit to it.
- L109's "that is" would then equate "\(A\) contains an edit that alters the relation reporting it" with a pattern that asks for no such edit.
- So the second clause does work, though not the work of telling components apart.

## Faults sought in the sentence itself

- **The second clause (Mimo).** No defect is shown, for the reasons above. Each clause does its own job:
  - The first clause tells the reading's component apart from the part's, by L103 and L119.
  - The second clause ties the pattern to a contract that admits a reporting edit, which L109 needs.
  - The same holds of C07's replacement clause, on Mimo's own comparison. That is for C07's checker.
- **Circularity with L109.** There is none:
  - L124 uses no role term. L109 points forward at it ("(below)").
  - "measured port" and "measuring relation" name the two places of the pattern: the port the component reads, and the component's own relation. They do this the same way as L109's "what it reports" and L127's "a part that reads or reports another part".
  - Both readers found no circle, and this reading agrees.
- **The footprint.** The sentence does not say in so many words that the measured port lies in the component's footprint. The word "measured" carries it, as "reports" does at L109 and "read" does at L119 and L127.
  - Read otherwise, any component would have a measurement's signature relative to any port it neither assigns nor reads.
  - That is not the text's reading: L127 names the pattern "a part that reads or reports another part".
  - No failure is shown, and no wording is needed.
- **The owner's decisions.**
  - The sentence has no word or idea that S23 forbids.
  - Its "interventions" are admitted edits that set a port (L109: "an edit that sets \(v\) directly"; L325: "Under \(A\) containing interventions on \(H\) and \(\theta\), these ports are inputs and \(L\) is an output, by Part II"). Admitting an edit is not a claim that it can be carried out (L49; L159: "admitting a change is not a claim that it can be carried out or come about"). So the sentence brings in no physical possibility (S25 to S27).
  - It grades nothing and lists no rivals (S20). It says nothing about what must happen (S21) and settles nothing (S28).
  - It says nothing about what hard to vary covers, or about where values stand (S33, S34).
- **Noticed, outside this item and not ruled.**
  - L109 gives the roles "under \(A\)", while (K) builds a signature on a contract \(C\) (L113, L119).
  - L109's "that is" is read here with any contract that holds the edit L109 names.
  - That is a matter for L109's wording, if anyone chooses to take it up. It does not bear on C08's wording.

## Cases the sentence bears on

KEEP moves no fixed verdict. The cases below read the same on the kept sentence. None of them turns on the idiom, so Mimo's rival would move none of them either.

**The cases tied to it through L127** (S81 place M13) are O4, O6 and O9:

- **O9.** "Bend the needle to read "full": the float is where it was and the valve opens as before." That is an edit to the measuring relation, and the part it reports stays as it was.
  - "Hold the float up with a wire: the dial reads "full" and the valve stays shut." That is an intervention on the measured port, and the reading follows.
  - So the dial has a measurement's signature relative to the float, and the fixed verdict stands: "The float is read by the dial and also does the work."
- **O6.** Warming the thermometer alters the reading "while the child shivers exactly as before". The cool bath alters the temperature and the shivering, and the reading follows.
  - The fixed verdict stands: "Her second statement mistakes the instrument for the illness."
- **O4.** The recalibration is an edit to the measuring relation. It moves every reading "ten points higher, and people who take the syrup sleep exactly as before".
  - The fixed verdict stands: "He has said almost nothing about why the syrup causes sleep."

**The text's own cases.** These go through L127's "Which of the two an account offers as producing an outcome is fixed by that signature":

- L151: "whether the measured part also produces the outcome is the production question, and the first answer is not the second."
- The reversed calculation at L271.
- The pole and its shadow at L325: "Direction is set by the admitted edits; the nouns "pole" and "shadow" fix nothing."

## Parked, and values

- **Parked:** no point of either reader on C08 proposes anything about what hard to vary covers, so nothing is parked (S34). The record here that the wording is easy to vary on this reading is the one rule 5 asks for, in the brief's plain sense. It is not a proposal about what hard to vary covers.
- **Values:** no value is moved in or out (S33, S34).

## What depends on the sentence

Recorded for completeness. Nothing is dropped, so nothing happens to any of these:

- **L109**, "A port is an **observation** when \(A\) contains an edit that alters the relation reporting it without altering what it reports, that is, when the component assigning it has a measurement's signature (below)."
- **L121**, the heading of the list ("a measurement").
- **L123**, "is invariant under observation edits", through L109's observation.
- **L127:**
  - "These are descriptions of patterns in (K), not additional data."
  - "In particular, a part that reads or reports another part has a measurement's signature: ..."
  - "Which of the two an account offers as producing an outcome is fixed by that signature, not by the account's wording."
- **L151's last sentence**, and through L127 the cases above.

## File name

Rule 11 of the reading rule names `results/S103 Round 1 - rulings/ruling C<nn> L<line>.md`. The task named this path, `results/S103 Round 1 - reading/rulings/ruling C08.md`, next to the rulings already there, so it was used. No second copy was written. Moving or copying it is the orchestrator's choice.
