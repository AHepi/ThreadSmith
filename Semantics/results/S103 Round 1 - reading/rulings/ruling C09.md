# S103 Round 1 — ruling on C09 (L125)

*Written on 27 September 2026 by a fresh Opus 5.5 checker. It built nothing of this round, read no reply before this task, and rules on no other candidate of it (rule 5 of `results/S103 Round 1 - how the replies will be read, written before sending.md`). This file obeys decision S23 except where it quotes the text, a reply or the owner. Nothing here is settled (S28). This is a ruling on the reasons the two replies give, and it stays open to the critical review of rule 12 and to any later criticism.*

## The ruling

**KEEP.** Line 125 of `tests/99 The semantics, standing alone.md` (md5 74f4a4c7619345747f4fa976ddac9548, checked before reading) stands as it is:

> - a **rule application** has a signature invariant under interventions on the world and variable under edits to the rule.

- **Mimo's rival is a rewording that changes nothing the theory needs from the sentence.** So on this reading the sentence's *wording* is easy to vary, in the plain sense the brief gives (section 5, item 1), not in the sense of the text's term at L317. That is recorded here. The rival is not clearer than the text's wording (reasons below), so the ruling is KEEP, not FIX (rule 5).
- **GLM's HOLDS:** every variation GLM tried changes what the sentence says, and each one breaks something named below. One of GLM's reasons does not hold as given: L127 does not keep the families apart. The variation still breaks L57 and L347 for GLM's other reason.
- **Mimo's two fault-check points** (the line 174 remark in C07, and the "same profile shape" remark in C09) do not show a failure of this sentence. The second clause is not inert here, as it is argued to be in C07. The shared shape with C08 is what the text itself says follows when no admitted change separates two components.
- **Parked (S34):** nothing. **Values (S33–S34):** none moved in or out.

## What was read

- The text under review, L1–L140 and L330–L360, with the lines each quoted definition stands on. Other lines were found by search: every use of "rule", "world" and "edit-signature". The file was not written to.
- The part 1 brief (`tests/S103 Round 1 - trying to vary the strong candidates - part 1, Parts 0 and II.md`): section 1, section 2 (the owner's words), C07–C09 of section 3, and sections 5 and 6.
- The reading rule, whole.
- The tabulation's C09 section and its general sections: the method, the list for checkers, the passages that name a candidate outside its own section, and the points that allege a defect.
- Mimo's reply, `s103_vary_mimo_1.response.txt`, lines 160–221: the C07 fault check that names C09 at line 174, the C08 section, and the whole C09 section (lines 200–220).
- GLM's reply, `s103_vary_glm_1.response.txt`, lines 180–208: the end of C08 and the whole C09 section (lines 189–207).
- No `.reasoning.txt` file was opened.
- The S98 ledger (`results/S98 Ledger of edits and recommendations/line-up/groups/02 Organizations and their changes (Part II).md`), at L125.s1 and L57. The S98 sentence index row L125.s1. The S101 node `sigfam` and its edges.
- The S81 case book (`tests/S81 Case book - the 52 cases, situations and fixed verdicts, as the tested agent sees them.md`), searched for rules, statuses and kinds. O6, O10, O12, O14 and O49 were read.
- The heads of the rulings on C07 and C08, read only to see how the same idiom and the same general clause were ruled on beside this one. This ruling rests on its own reasons.
- `records/Semantics - Decisions.md`, S20–S35, as the brief quotes them and as the record lists them.

## The sentence in (K)'s terms

(K) builds a component's signature from its relation under each admitted pair: "\operatorname{sig}_C(j)=\{(a,b,L_j(a,b)):(a,b)\in C\}" (L116). Three lines fix what the sentence's two clauses come to.

- L103: "An edit that sets a port replaces the component assigning that port; it does not add an equation beside an incompatible one. A changed rule is a changed component."
- L119: "An edit that sets a port replaces only the component that assigns the port (above), not the relations of the components that read it, and an edit under which the two relations stay equal does not separate the components."
- L347: "A rule relation \(C_r\subseteq Z\times S\) answers "which status under this rule?" by its fibre. Its signature under (K) is invariant under interventions on \(Z\) and variable under edits to \(C_r\)."

Read with these lines, the sentence says two things of a rule application. First, no admitted intervention on what the rule reads (L347's \(Z\), "the world") alters its relation. By L119, such an intervention replaces the component that assigns the port set, not the rule application that reads it. Second, the contract holds edits to the rule under which the relation differs. By L103, "A changed rule is a changed component". L57 cites exactly this pair of clauses as the difference between a rule and a cause: "a rule's application changes when the rule is edited and not when the world is intervened on; a cause's assignment changes under intervention. That is a difference in edit-signature (Part II)".

## The two readers' sides (rule 7)

**Mimo: VARIES** (reply line 220), with the rival at reply line 204.

- The rival "Keeps both clauses; matches L347 ("Its signature under (K) is invariant under interventions on \(Z\) and variable under edits to \(C_r\)") and L57. Breaks nothing." (reply line 206)
- Its fault check, in its own words (the inner quotation marks are Mimo's): `"the world" is ordinary language whose formal reading is L347's \(Z\); the word itself is not pinned`, and "under (K), C08 and C09 have the same profile shape (invariant on the worldly input, variable on the relation), and L121 does not claim the families are distinct. No failure." (reply line 218)
- In C07 (reply line 174): "C08, C09 carry the same general clause in their own words. Inertness, not contradiction."

**GLM: HOLDS** (reply line 207).

- Every variation GLM tried "lost the world/rule contrast of L57 and L347, or conflated the rule family with the observation notion defined at L109".
- Faults sought: "None: the line is consistent with L57, L347, and L103 ("A changed rule is a changed component"), which is what an "edit to the rule" is." (reply line 205)

**Where they differ.** They do not differ on content. Both find the world-invariant, rule-variable pattern needed, and neither finds a variation of that content that breaks nothing. They differ only on whether a change of idiom that keeps the content counts as a working rival. Rule 5 says how to rule on that: a rewording that changes nothing the theory needs is recorded as showing the wording easy to vary, and it is a FIX only if it is clearer. This ruling weighs the reasons on each side. It gives no weight to how many readers stand on a side.

## The rival offered as working (Mimo, reply line 204)

```
- a **rule application** has a signature that interventions on the world leave unchanged and edits to the rule change.
```

**What changes.** "invariant under interventions on the world" becomes "that interventions on the world leave unchanged". "variable under edits to the rule" becomes "[that] edits to the rule change". Both clauses keep their roles ("the world", "the rule") and their direction. The rival makes the same two demands of a rule application's relation that the text's wording makes. L57 and L347 read the same with it, and so do L121 and L127. No case verdict moves (see "Cases" below). So the rival is **a rewording that changes nothing the theory needs**. On this reading the sentence's wording is easy to vary, and that is recorded. This concerns the idiom only. It proposes nothing about what hard to vary covers (S34).

**Why the rival is not clearer, and so no FIX:**

1. **L347 is this bullet's worked instance, and the text's wording says so word for word.** L347 reads "invariant under interventions on \(Z\) and variable under edits to \(C_r\)". The bullet reads "invariant under interventions on the world and variable under edits to the rule". Only the ordinary names ("the world", "the rule") stand where L347 has \(Z\) and \(C_r\). A reader sees at once that L347 is the formal statement of the bullet. The rival loses that match. Mimo says the rival "matches L347", but it matches L347 only in content, which the text's wording does too.
2. **The bullets share one idiom.** C08 (L124) reads "a signature invariant under interventions on the measured port and variable under edits to the measuring relation", and its checker kept it. Changing C09 alone would give two neighbouring bullets different idioms with no difference in claim, and a reader would look for a difference that is not there.
3. **"variable under" asks less than the rival's plain verb invites.** "variable under edits to the rule" says the relation varies across the rule edits in \(C\). The rival's "edits to the rule change" can be read as saying that every edit to the rule changes it. The text allows edits under which relations stay equal: "an edit under which the two relations stay equal does not separate the components" (L119). This is a reading the rival invites, not one it forces, so it does not make the rival a different claim. It is one more reason why the rival is not the clearer wording.
4. **The point for the rival, and why it does not decide the matter.** The rival's verbs are nearer to L57's ordinary-language idiom ("changes when the rule is edited and not when the world is intervened on"). But L35 says of the front matter that it "states nothing the body does not state more exactly". The bullet belongs to the body, and the body's more exact statement of the pattern is L347's idiom. The text's wording shares that idiom.

## Variations said to break

Each variation is weighed on what it breaks, not on how many there are (S20).

**Mimo, reply line 210 (rule and world swapped):**
```
- a **rule application** has a signature that interventions on the rule leave unchanged and edits to the world change.
```
This breaks L57 ("a rule's application changes when the rule is edited and not when the world is intervened on"), which says the opposite on both counts, and it breaks L347 ("invariant under interventions on \(Z\) and variable under edits to \(C_r\)"). It also conflicts with L103: "A changed rule is a changed component". An edit to the rule changes the component's relation, so the signature cannot stay unchanged under it wherever the edit alters the relation. **Mimo's point holds.**

**Mimo, reply line 214 ("output port" for "the world"):**
```
- a **rule application** has a signature invariant under interventions on the output port and variable under edits to the rule.
```
This breaks L347, whose invariant side is \(Z\), the side the rule reads, not its status. It breaks more directly than Mimo says. By L103 ("An edit that sets a port replaces the component assigning that port") and L119, an intervention on the rule application's own output port replaces the rule application, so its relation is not invariant there. The variation asks for something no component that assigns its output port can have. That is the reverse of C07's pattern ("changes under intervention on its output port", L123), not a collapse into it. **Mimo's point that it breaks holds. Its reason is sharpened here.**

**GLM, reply line 194 (world side dropped):**
```
- a **rule application** has a signature invariant under interventions and variable under edits to the rule.
```
This breaks L57, whose contrast is "not when the world is intervened on" against "a cause's assignment changes under intervention". It breaks L347's "interventions on \(Z\)". With no object, "interventions" also covers an intervention setting the rule application's own output port. By L103 and L119 that intervention replaces the component. So on any contract that holds that edit, the unqualified clause describes no rule application. **GLM's point holds.**

**GLM, described and not written out (polarities swapped):** "variable under interventions on the world and invariant under edits to the rule" would say the opposite of L57 and L347, and it would conflict with L103 as the first variation does. **GLM's point holds.**

**GLM, reply line 200 ("observation edits" for "interventions on the world"):**
```
- a **rule application** has a signature invariant under observation edits and variable under edits to the rule.
```
GLM gives two reasons.

- **The first holds.** The variation drops the world side, so L57's "not when the world is intervened on" and L347's "invariant under interventions on \(Z\)" would no longer have their pattern in Part II. L57 points to Part II for this difference ("That is a difference in edit-signature (Part II)").
- **The second does not hold as given.** GLM says the variation mixes "the two families L127 keeps apart". L127 does not keep the measurement and rule families apart. It says "These are descriptions of patterns in (K), not additional data", and its "Which of the two an account offers as producing an outcome is fixed by that signature" contrasts a reading part with the part it reports, not a measurement with a rule. Nor is "observation" a circle here: C07 (L123) uses "observation edits" in another family without one.

So the variation breaks L57 and L347, for GLM's first reason only.

## Faults sought in the sentence itself

**"The world" is not pinned (Mimo, reply line 218).** Mimo draws no failure from this, and this ruling finds none. The bullets are announced as ordinary language: "What ordinary language calls a cause, a measurement, a rule or a constitutive status are families of signatures:" (L121). They are "descriptions of patterns in (K), not additional data" (L127). The formal reading is given where the text works the case: \(Z\) in L347, the side that \(C_r\subseteq Z\times S\) reads. L57 uses "the world" in the same sense.

A reader might ask whether an edit that sets the status port directly is an "intervention on the world". The text answers that by L103: such an edit replaces the component assigning the status, which is the rule application, and "A changed rule is a changed component". So it falls on the sentence's rule side, not its world side, and the first clause is not broken by it.

Nor does the sentence bring in physical possibility. "An admitted change need not be a physical intervention" (L49), and \(Z\) is whatever the rule reads, which may be a game, a practice or a mathematical structure (L277: "why does this follow under these rules?"). The sentence says nothing about what can be carried out, so S25–S27 are not engaged.

**The second clause is said to be general, like C07's replacement clause (Mimo, reply line 174).** For C09 this does not hold, and the reason is specific to this sentence. In C07, the first clause ("changes under intervention on its output port") already requires the contract to hold an edit that replaces the component, since by L103 setting a port replaces its assigning component. That is why a replacement clause there can add nothing (C07 is for its own checker).

In C09 the first clause is an invariance. On its own it would also hold of any component that no edit in \(C\) touches, and so it would count such a component as a rule application on \(C\). The second clause rules that out: it requires the contract to hold edits to the rule under which the relation differs. This is L57's last sentence at work: "What it denies is that the difference is available before the admitted changes are fixed, or independently of them." A rule application is picked out only on a contract that edits the rule. Dropping the clause would widen the family to components the contract leaves untouched, and L57's "a rule's application changes when the rule is edited" would lose its Part II counterpart. **The clause does work, so there is no FIX on this point.**

**C08 and C09 have the same profile shape under (K) (Mimo, reply line 218).** This holds, and it is no failure of the sentence. The text says it itself:

- L119: two components whose signatures coincide on \(C\) under a footprint bijection "are of one kind on \(C\)", and the sentence on port values ends "whatever the difference is called".
- L11: "Two components no admitted change can separate are one kind at that level, whatever labels anyone attaches to them".
- L127: "a part that reads or reports another part has a measurement's signature". A rule application reads the world, so by L127 it has a measurement's signature in that sense.

The families are told apart, where they are told apart at all, by which ports and edits the contract holds: a measured port and a measuring relation, or the world and a rule (L57's last sentence). L121 does not say the families are disjoint, and nothing in the text needs them to be.

**Circularity, vacuity, contradiction.**

- No circle: "rule application" is described, not defined through itself, and "the rule" is given by L103 as a component.
- Not vacuous: the pattern excludes components that assign a world port (L103, L119) and components the contract never edits (above).
- No contradiction was found with L57, L103, L109, L119, L121, L127, L151 or L347.

**The owner's words.** The sentence uses no word or idea S23 forbids. It says nothing about what must happen (S21) and grades nothing (S20). It brings in physical possibility nowhere (S25–S27) and settles nothing (S28). It touches neither what hard to vary covers nor the placement of values (S33–S34). KEEP changes none of this.

## Cases the sentence bears on

KEEP moves no fixed verdict. The cases below read the same on the kept sentence. None of them turns on the idiom, so Mimo's rival would move none of them either.

- **Grievance 11, L57** ("Kinds exist. A rule is not a cause."): its answer points to Part II. The kept bullet, beside C07, is where that pointer lands.
- **Constitutive rules, L347:** the worked instance of the bullet. It stands word for word in the same idiom.
- **The rule-status question type, L151:** "The rule-status and purpose-achievement cases are given with constitutive rules (Part VII)". This reaches the bullet through L347 and does not change.
- **The S81 case book:** no case turns on the rule family. O1 and O5 use "rule" for a predictive rule, not a constitutive one. O6 turns on the measurement's signature (L127) and O10 on L119. Neither reads the rule bullet.
- **The S98 ledger** records L125.s1 as "no change recorded". No proposal against it is on file.

## Parked, and values

- **Parked:** no point of either reader on C09 proposes anything about what hard to vary covers, so nothing is parked (S34). The record above that the wording is easy to vary on this reading is the one rule 5 asks for, in the brief's plain sense. It is not a proposal about what hard to vary covers. Whether a change of idiom bears on the text's own term (L317) is not asked here and is not ruled.
- **Values:** nothing is moved in or out (S33–S34).

## What depends on the sentence

These are named for the record. With KEEP, each stands as it is.

- **L121** "What ordinary language calls a cause, a measurement, a rule or a constitutive status are families of signatures:". The bullet is the family L121 names as "a rule". L121 names four things and the list gives three bullets. By L347, a constitutive status is what the rule relation assigns, so the rule-application bullet covers both "a rule" and "a constitutive status". That is L121's wording, not C09's. It is recorded here and not ruled.
- **L127** "These are descriptions of patterns in (K), not additional data." This describes the bullets, C09 among them.
- **L57** "a rule's application changes when the rule is edited and not when the world is intervened on; ... That is a difference in edit-signature (Part II)". Its pointer lands on this bullet.
- **L347** "Its signature under (K) is invariant under interventions on \(Z\) and variable under edits to \(C_r\)." This is the bullet's worked instance.
- **L151**, through L347, as above.

## File name

Rule 11 of the reading rule names `results/S103 Round 1 - rulings/ruling C<nn> L<line>.md`. The task named this path, `results/S103 Round 1 - reading/rulings/ruling C09.md`, next to the rulings already there, so it was used. No second copy was written. Moving or copying it is the orchestrator's choice.
