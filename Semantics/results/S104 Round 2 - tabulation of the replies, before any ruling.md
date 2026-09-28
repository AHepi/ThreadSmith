# S104: Round 2 (the maths) — tabulation of the replies, before any ruling

*Written by the tabulating agent of rule 4 (a fresh Opus 5.5 agent that built nothing of this round and had read no reply before this file was created), on 28 September 2026. Created at once and filled as it goes (lesson S28). It rules on nothing: it records what each reader said, copies each proposal exactly, names the lines each proposal would change, compares each quotation with the text under review, and says, under rule 5 and the two addenda, whether each item goes to a checker. No theory text, brief, reply, reading rule, addendum or committed maths file was written; nothing in `authority/` was written. This file obeys decision S23 except where it quotes the text, a reply, a brief, the external document, the case card or the owner.*

## How this file was made

- **Read first, whole:** the reading rule (`results/S104 Round 2 - how the replies will be read, written before sending.md`) and its two addenda (the external cross-examination; the creative transport case); the owner's decisions S20 to S39 in `records/Semantics - Decisions.md`.
- **The text under review:** `tests/103 The semantics, standing alone, after round 1.md`, md5 checked: f31ebb1f050783f1a84f6136cec20fcd (as the rule states), 632 lines, read whole.
- **The briefs:** the seventeen part briefs in `tests/`; the items of each part (definitions and encodings printed in section 3, claims, inventions in full, U- and H-entries, NF entries, round-1 matters and changes) and the lines each quotes were taken from the briefs by program and checked by reading.
- **The replies:** for each of the 34 tags, the receipt, then the `.response.txt` only. The replies were read whole. Proposals are copied from the reply files by program, byte for byte, between fence lines (a reader's own fence lines are not repeated; a reader's proposal written as a quoted line `> Lnnn | …` is copied whole, with its `>`). Each proposal is given an id: the reader's letter (M Mimo, G GLM), the part, and the block's number in that reply (for example `G1-B3`: GLM, part 1, block 3). "Reply lines" are line numbers of the `.response.txt`.
- **Quotations:** every quotation in the reply lines a point rests on (text in double quotation marks, or a quoted line `> Lnnn | …` that stands in the text) was compared by program with the text under review, after normalizing markup (the text's `\(…\)` and `\operatorname` and the like, Greek letters and symbols written in Unicode or in markup, spacing and punctuation); " … " joins fragments that must stand in one line. Each is recorded "found at L…" or "not found in the text"; where not found in the text, the part brief was searched as well and the record says "found in the brief" where it stands there (the maths' own wording, the owner's words, or the search's printouts). A quotation of a single word is compared too; one that stands on many lines is recorded with its first lines found.
- **What goes to a checker** follows rule 5 and the addenda: an item goes when any point challenges it (the maths says other than the sentence; a counterexample tells against the text; the text settles an invention or should carry wording that settles it; a counterexample to a claim that held; a proposed change for a round-1 matter or change; any other proposed change to the text; in doubt, it goes), and the twelve counterexamples the second check reproduced go whether raised or not. The external reader's findings that challenge the text, and the case card's C01 to C07 and C11, go too. A point that only says the maths should change (a register entry, a formal statement) is still a point that the maths says other than the sentence, and sends its item.
- **Marks** (rule 9; addendum points 8; decisions S33, S34): **PARKED** where a point is about what hard to vary covers; **OWNER QUESTION** where a point would move where values are placed, turns on the reading of "argument" (L8, L397; decision S23), or turns on a choice the owner has not made. Marked, not weighed.
- **Lines** given for an item going to a checker are the lines its proposals would change; for an item whose points change no line of the text, the lines its claim, definition or invention formalizes (the lines the brief quotes for it).
- **How to read an entry of section 2.** Each item of a part is headed by its id, kind and title, with the lines the brief quotes for it. Under it, each reader's points in the order of the reply, each with its reply lines and whether it challenges the item in the sense of rule 5 ("challenges" or "does not challenge"; a point that says only that the text settles an invention, or that the maths departs from the words, is a challenge by rule 5's list), a digest in one or two sentences, each proposal copied whole with the lines it would change, and the quotation checks. A proposal shared by several items is printed in full at its first item in the part and named at the others. A point that only names the item among those "with nothing to add" is recorded as such. An item printed in several parts is tabulated in each. Then whether the item goes to a checker, why, the lines at stake, and any mark. Items of a part on which neither reader said anything are named at the end of the part.
- **Sections.** 1 receipts; 2 the seventeen parts; 3 the external reader's findings E01–E22; 4 the case card's items C01–C14; 5 what goes to a checker, in one table, with the context items; 6 rule 7's records; 7 the marks; 8 notes for the orchestrator. The same items, with their lines, are in `results/S104 Round 2 - tabulation of the replies, before any ruling.json`.
- Nothing here is a ruling: "challenges" names what a point does, not whether it holds.

## 1. Receipts (rule 2)

Each receipt was read (`.receipt.json`), then the reply (`.response.txt`) only; no reasoning file, request file or attempt file was opened. Every tag is pass 1: no `_pass2` or `_pass3` file exists in the returns folder. The last non-blank line of every reply was checked by program.

| tag | accepted | pass | how | last line END OF REPORT | words (`wc -w` count) |
|---|---|---|---|---|---|
| `s104_maths_mimo_1` | accepted | 1 | finish "stop"; 1 attempt(s) | yes | 1373 |
| `s104_maths_mimo_2` | accepted | 1 | finish "stop"; 1 attempt(s) | yes | 2007 |
| `s104_maths_mimo_3` | accepted | 1 | finish "stop"; 1 attempt(s) | yes | 2022 |
| `s104_maths_mimo_4` | accepted | 1 | finish "stop"; 1 attempt(s) | yes | 2237 |
| `s104_maths_mimo_5` | accepted | 1 | finish "stop"; 1 attempt(s) | yes | 2407 |
| `s104_maths_mimo_6` | accepted | 1 | finish "stop"; 1 attempt(s) | yes | 2627 |
| `s104_maths_mimo_7` | accepted | 1 | finish "stop"; 1 attempt(s) | yes | 2101 |
| `s104_maths_mimo_8` | accepted | 1 | finish "stop"; 1 attempt(s) | yes | 1672 |
| `s104_maths_mimo_9` | accepted | 1 | finish "stop"; 1 attempt(s) | yes | 2779 |
| `s104_maths_mimo_10` | accepted | 1 | finish "stop"; 1 attempt(s) | yes | 1899 |
| `s104_maths_mimo_11` | accepted | 1 | finish "stop"; 1 attempt(s) | yes | 1920 |
| `s104_maths_mimo_12` | accepted | 1 | finish "stop"; 1 attempt(s) | yes | 2171 |
| `s104_maths_mimo_13` | accepted | 1 | finish "stop"; 1 attempt(s) | yes | 2063 |
| `s104_maths_mimo_14` | accepted | 1 | finish "stop"; 2 attempt(s); attempt 1 ended with no HTTP status (status 0, no answer: a connection failure, not counted against the reader, rule 2), attempt 2 accepted | yes | 2037 |
| `s104_maths_mimo_15` | accepted | 1 | finish "stop"; 1 attempt(s) | yes | 2460 |
| `s104_maths_mimo_16` | accepted | 1 | finish "stop"; 1 attempt(s) | yes | 1948 |
| `s104_maths_mimo_17` | accepted | 1 | finish "stop"; 1 attempt(s) | yes | 2613 |
| `s104_maths_glm_1` | accepted | 1 | 1 attempt(s); connection failures 0; answers rejected 0; rule "the reply's last non-blank line carries END OF REPORT" | yes | 2756 |
| `s104_maths_glm_2` | accepted | 1 | 1 attempt(s); connection failures 0; answers rejected 0; rule "the reply's last non-blank line carries END OF REPORT" | yes | 2413 |
| `s104_maths_glm_3` | accepted | 1 | 1 attempt(s); connection failures 0; answers rejected 0; rule "the reply's last non-blank line carries END OF REPORT" | yes | 2503 |
| `s104_maths_glm_4` | accepted | 1 | 1 attempt(s); connection failures 0; answers rejected 0; rule "the reply's last non-blank line carries END OF REPORT" | yes | 2430 |
| `s104_maths_glm_5` | accepted | 1 | 1 attempt(s); connection failures 0; answers rejected 0; rule "the reply's last non-blank line carries END OF REPORT" | yes | 2280 |
| `s104_maths_glm_6` | accepted | 1 | 1 attempt(s); connection failures 0; answers rejected 0; rule "the reply's last non-blank line carries END OF REPORT" | yes | 2514 |
| `s104_maths_glm_7` | accepted | 1 | 1 attempt(s); connection failures 0; answers rejected 0; rule "the reply's last non-blank line carries END OF REPORT" | yes | 2335 |
| `s104_maths_glm_8` | accepted | 1 | 1 attempt(s); connection failures 0; answers rejected 0; rule "the reply's last non-blank line carries END OF REPORT" | yes | 2013 |
| `s104_maths_glm_9` | accepted | 1 | 1 attempt(s); connection failures 0; answers rejected 0; rule "the reply's last non-blank line carries END OF REPORT" | yes | 2425 |
| `s104_maths_glm_10` | accepted | 1 | 1 attempt(s); connection failures 0; answers rejected 0; rule "the reply's last non-blank line carries END OF REPORT" | yes | 2479 |
| `s104_maths_glm_11` | accepted | 1 | 1 attempt(s); connection failures 0; answers rejected 0; rule "the reply's last non-blank line carries END OF REPORT" | yes | 2122 |
| `s104_maths_glm_12` | accepted | 1 | 1 attempt(s); connection failures 0; answers rejected 0; rule "the reply's last non-blank line carries END OF REPORT" | yes | 2156 |
| `s104_maths_glm_13` | accepted | 1 | 1 attempt(s); connection failures 0; answers rejected 0; rule "the reply's last non-blank line carries END OF REPORT" | yes | 2564 |
| `s104_maths_glm_14` | accepted | 1 | 1 attempt(s); connection failures 0; answers rejected 0; rule "the reply's last non-blank line carries END OF REPORT" | yes | 2096 |
| `s104_maths_glm_15` | accepted | 1 | 1 attempt(s); connection failures 0; answers rejected 0; rule "the reply's last non-blank line carries END OF REPORT" | yes | 2772 |
| `s104_maths_glm_16` | accepted | 1 | 1 attempt(s); connection failures 0; answers rejected 0; rule "the reply's last non-blank line carries END OF REPORT" | yes | 1773 |
| `s104_maths_glm_17` | accepted | 1 | 1 attempt(s); connection failures 0; answers rejected 0; rule "the reply's last non-blank line carries END OF REPORT" | yes | 2558 |

All 34 calls accepted on pass 1; every reply ends with END OF REPORT. No item of any part is "not examined" by either reader (rule 7's second and third forms do not arise).

## 2. Part by part, item by item

### Part 1: Organizations, setting edits and roles

Brief: `tests/S104 Round 2 - the maths against the words - part 01, Organizations, setting edits and roles.md`. Replies: `s104_maths_mimo_1.response.txt` (Mimo), `s104_maths_glm_1.response.txt` (GLM).

#### D1.1 · definition · Organization

Lines it formalizes or quotes (from the brief): L88, L91, L94.

- **Mimo** (reply lines 3–7; challenges): The text does not settle how strong "partial associative" is; the maths' Kleene (strong) associativity (I01) should stand, since under weak associativity a composite could be defined under one bracketing and not the other, leaving the edit ambiguous; the text should carry it.
  - Proposal `M1-B1` (reply lines 4–7), would change L91:

````
Replace in L91 the sentence "A is a set of admitted edits, closed under a partial associative composition with identity 1." with:
A is a set of admitted edits, closed under a partial composition · : A × A ⇀ A that is strongly associative: a3·(a2·a1) is defined exactly when (a3·a2)·a1 is, and then they are equal; and with identity 1 such that 1·a = a·1 = a for every a.
````

  - Quotations: “closed under a partial associative composition with identity 1” — found at L91.
- **GLM** (reply line 5; challenges): The tuple matches L88/L91; three additions go beyond the words (I01 Kleene associativity, I02 no law on composites, I03 V and J fixed under every edit); none distorts the sentence; handled under (c).
  - Proposal `G1-B2` (reply lines 43), would change L91:

````
> L91 | \(V\) is a set of ports, each with a nonempty value domain \(X_v\). A valuation is an element of \(X_D=\prod_v X_v\). \(J\) indexes components; each component \(j\) has a footprint \(V_j\subseteq V\). \(B\) is a set of boundary conditions. \(A\) is a set of admitted edits, closed under a partial composition with identity \(1\), associative in this sense: \(a_3\cdot(a_2\cdot a_1)\) is defined exactly when \((a_3\cdot a_2)\cdot a_1\) is, and then the two are equal.
````

  - Proposal `G1-B3` (reply lines 51), would change L103:

````
> L103 | An edit that sets a port replaces, at every boundary, the component assigning that port; it does not add an equation beside an incompatible one. The component assigning a port is the one its setting edits replace; where setting edits of one port replace two different components, no one component assigns it. A changed rule is a changed component. A deleted component imposes the full relation on its ports; a port is absent when every component imposes the full relation on it; and no edit adds or removes a port or component.
````

  - Quotations: “Kleene-associative” — not found in the text; found in the brief; “no law ties L_j(a2·a1, b) to its parts” — not found in the text; not in the brief; “V and J are the same under every edit” — not found in the text; found in the brief.
- **Goes to a checker** (rule 5): challenged by GLM and Mimo. Lines at stake: L91, L103.

#### D1.2 · definition · Solutions (O)

Lines it formalizes or quotes (from the brief): L100, L105.

- **Mimo** (reply line 48; does not challenge): Named among the items with nothing to add.
- **GLM** (reply line 7; does not challenge): Faithful: (O) is the text's own display.
- **Goes to no checker**: no point challenges it and it is not one of the twelve; recorded under rule 7 below.

#### D1.3 · definition · Deletion and absence

Lines it formalizes or quotes (from the brief): L103, L339.

- **Mimo** (reply lines 9–13; challenges): The deletion sentence matches the maths; "absent" is not defined in the text, and the maths' reading of it is consistent; the text should define absence.
  - Proposal `M1-B2` (reply lines 10–13), would change L339:

````
Add after L339:
A component is absent in D when it is deleted; a port is absent when every component that includes it imposes the full relation on its ports.
````

  - Quotations: “A deleted component imposes the full relation on its ports” — found at L103, L255; “absent” — found at L339, L407.
- **GLM** (reply line 9; challenges): Deletion as the full relation is the text's own sentence; the maths adds absence of a port (L339 uses "absent" of ports without defining it) and the fixedness of V and J; the words are thinner than L339 needs; the maths should stand and be written in (the L103 rewrite under I03).
  - Proposal `G1-B3` (reply lines 51; printed in full under D1.1 above), would change L103.
  - Quotations: “absent” — found at L339, L407.
- **Goes to a checker** (rule 5): challenged by GLM and Mimo. Lines at stake: L103, L339.

#### D1.4 · definition · Subnetwork

Lines it formalizes or quotes (from the brief): none.

- **Mimo** (reply line 15; does not challenge): No counterpart in the given text; no claim of this part uses it; no change.
- **GLM** (reply line 11; does not challenge): No sentence of Part II is quoted against it in this part; nothing to compare.
- **Goes to no checker**: no point challenges it and it is not one of the twelve; recorded under rule 7 below.

#### D2.1 · definition · Setting edit; the assigning component

Lines it formalizes or quotes (from the brief): L103, L119.

- **Mimo** (reply lines 17–26; challenges): "Sets a port directly" is not defined; the maths' surgical setting edit (I04) captures L103's "replaces the component assigning that port" and "does not add an equation beside an incompatible one", and the text should adopt it; the text should also say that the assigning component is read off A.
  - Proposal `M1-B3` (reply lines 18–21), would change L103:

````
Replace L103 with:
An edit a sets port v at boundary b through component j when L_j(a,b) = {w ∈ ∏_{v∈V_j} X : w_v = x} for some x ∈ X_v, and L_k(a,b) = L_k(1,b) for every k ≠ j. Such an edit replaces the component assigning that port and does not add an equation beside an incompatible one. A changed rule is a changed component.
````

  - Proposal `M1-B4` (reply lines 23–26), would change L109:

````
Add after L109:
The component assigning v, asg(v), is the component through which the edits of Set_v set v, when there is exactly one; otherwise it is undefined.
````

  - Quotations: “sets a port directly” — not found in the text; not in the brief; “replaces the component assigning that port” — found at L103; “does not add an equation beside an incompatible one” — found at L103.
- **GLM** (reply line 13; challenges): The surgical reading is what L103 says, and I04's alternative (c) is excluded by its words; two partings: the text presupposes a unique assigning component without saying what happens when setting edits of one port replace two, and the boundary quantifier is open (H03); both written in by the L103 rewrite.
  - Proposal `G1-B3` (reply lines 51; printed in full under D1.1 above), would change L103.
  - Quotations: “replaces the component … does not add an equation beside an incompatible one” — found at L103; “the component assigning that port” — found at L103.
- **External reader and case card:** E04 (the external reader) challenges the sentence this item formalizes (section 3 below).
- **Goes to a checker** (rule 5): challenged by GLM and Mimo; challenged by E04 (the external reader). Lines at stake: L103, L109.

#### D2.2 · definition · Input

Lines it formalizes or quotes (from the brief): L109.

- **Mimo** (reply line 48; does not challenge): Named among the items with nothing to add.
- **GLM** (reply line 15; does not challenge): Faithful, apart from I80 (whether the identity can set a port).
- **Goes to no checker**: no point challenges it and it is not one of the twelve; recorded under rule 7 below.

#### D2.3 · definition · Output

Lines it formalizes or quotes (from the brief): L109.

- **Mimo** (reply lines 28–32; challenges): The text's "output" is ambiguous over edits and boundaries; the maths (I05) reads it at the identity edit and "across B" as every boundary, a natural reading; the text should settle it.
  - Proposal `M1-B5` (reply lines 29–32), would change L109:

````
Replace in L109 the sentence "A port is an output of component j when its value is determined by L_j given the other ports of V_j across B." with:
A port v is an output of component j when, at the identity edit and for every boundary b ∈ B, and all w, w' ∈ L_j(1,b), if w and w' agree on V_j ∖ {v} then w_v = w'_v.
````

  - Quotations: “across B” — found at L109.
- **GLM** (reply line 17; challenges): "Across B" settles every boundary; it does not settle at which edit, nor at most one against exactly one; the pole settles at most one (L = H cot θ determines nothing for H ≤ 0, so exactly one would deny L its output status, against L325); with L103 and L574, I05's alternative (a) collapses into the identity reading; the maths should stand and be written in (wording under I05).
  - Proposal `G1-B4` (reply lines 59), would change L109:

````
> L109 | No role assignment is supplied. A port \(v\) is an **input** under \(A\) when \(A\) contains an edit other than the identity that sets \(v\) directly — directly, by replacing only the component assigning \(v\) and leaving every other component as it is. A port is an **output** of component \(j\) when its value is determined by \(L_j\) at the identity edit, given the other ports of \(V_j\) across \(B\) — determined as at most one value.
````

  - Quotations: “Determined … across B” — found at L109; “A changed rule is a changed component” — found at L103.
- **External reader and case card:** E04 (the external reader) challenges the sentence this item formalizes (section 3 below).
- **Goes to a checker** (rule 5): challenged by GLM and Mimo; challenged by E04 (the external reader). Lines at stake: L109.

#### D2.4 · definition · Observation edits (two readings)

Lines it formalizes or quotes (from the brief): L109.

- **Mimo** (reply lines 34–38; challenges): The text equates observation edits with a measurement's signature ("that is"); the maths separates them and gives two readings; the equivalence does not hold, so the text should define observation edits directly.
  - Proposal `M1-B6` (reply lines 35–38), would change L109:

````
Replace in L109 the sentence "A port is an observation when A contains an edit that alters the relation reporting it without altering what it reports, that is, when the component assigning it has a measurement's signature (below)." with:
A port o is an observation when there exists a port m ∈ V_{asg(o)} ∖ {o} and an edit a ∈ A such that L_{asg(o)}(a,b) ≠ L_{asg(o)}(1,b) for some b, and L_{asg(m)}(a,b) = L_{asg(m)}(1,b) for every b. Whether setting edits of o are included is left open; both readings are considered where relevant.
````

  - Quotations: “that is” — found at L11, L37, L39, L57 and 9 more lines.
- **GLM** (reply line 19; challenges): Three partings: "what it reports" must be another port of the footprint; reading R-ii should stand (under R-i every setting edit of o counts as an observation edit, observation collapses into input, and L123 as it stands becomes unsatisfiable in any contract containing an intervention on the output port); the "that is" clause equates a condition on A with a signature on C (matter 5); wording in the L109 rewrite under matter 5.
  - Proposal `G1-B5` (reply lines 87), would change L109:

````
> L109 | No role assignment is supplied. A port \(v\) is an **input** under \(A\) when \(A\) contains an edit other than the identity that sets \(v\) directly — directly, by replacing only the component assigning \(v\) and leaving every other component as it is. A port is an **output** of component \(j\) when its value is determined by \(L_j\) at the identity edit, given the other ports of \(V_j\) across \(B\) — determined as at most one value. A port is an **observation** when \(A\) contains an edit that alters the relation reporting it without altering the port it reports in the same footprint; an edit that sets the port itself alters what it reports and does not count; under a contract \(C\) this role is read through the measurement signature of the component assigning it (below).
````

  - Quotations: “What it reports” — found at L109; “that is” — found at L11, L37, L39, L57 and 9 more lines.
- **Goes to a checker** (rule 5): challenged by GLM and Mimo. Lines at stake: L109.

#### D2.5 · definition · Direction

Lines it formalizes or quotes (from the brief): L109.

- **Mimo** (reply line 40; challenges): The maths makes direction the pair (Input_A, asg) where the text says only that direction is a consequence of the admitted edits; the formal statement is kept as a working definition; no change to the text.
- **GLM** (reply line 21; challenges): The words should stand: the text says what direction is a consequence of and refuses a stipulation; D2.5's pair is a reading, has no invention number (H04), and is thin (observation roles depend on A too); register it, do not write it into the text.
- **Goes to a checker** (rule 5): challenged by GLM and Mimo. Lines at stake: L109.

#### D4.5 · definition · Change and invariance on a contract

Lines it formalizes or quotes (from the brief): L123, L124, L125.

- **Mimo:** no point on this item.
- **GLM** (reply line 23; challenges): The comparison baseline "from the identity edit at the same boundary" is invented (I09); the words say only "changes under", "invariant under"; the vacuity clause is a semantic choice the text never faces; proposes a sentence appended to L113, naming I09.
  - Proposal `G1-B6` (reply lines 93), would change L113:

````
> L113 | Fix an organization \(D\) and a contract \(C\subseteq A\times B\) (Part III). A signature changes under a class of edits when some edit of that class in \(C\) alters the relation from what it is at the identity edit at the same boundary, and is invariant under it otherwise; invariance holds vacuously where \(C\) contains no edit of that class.
````

  - Quotations: “from the identity edit at the same boundary” — not found in the text; not in the brief; “changes under” — found at L57, L123; “invariant under” — found at L123, L124, L125, L347 and 1 more lines.
- **Goes to a checker** (rule 5): challenged by GLM. Lines at stake: L113.

#### D4.6 · definition · Families

Lines it formalizes or quotes (from the brief): L123, L124, L125, L347.

- **Mimo:** no point on this item.
- **GLM** (reply line 25; does not challenge): Causal matches L123 after round 1; Meas and Rule inherit the R-i/R-ii fork, which R-ii makes consistent; Rule's exclusion of Set_{o_j} sits oddly with L103's "A changed rule is a changed component" but is the right exclusion; not this part's to settle.
  - Quotations: “edits to the rule” — found at L125; “A changed rule is a changed component” — found at L103.
- **External reader and case card:** E05 (the external reader) challenges the sentence this item formalizes (section 3 below).
- **Goes to a checker** (rule 5): challenged by E05 (the external reader). Lines at stake: L123, L124, L125.

#### FC01 · claim · Solutions shrink as relations shrink; deletion never removes a solution

Lines it formalizes or quotes (from the brief): L100, L103.

- **Mimo** (reply line 42; does not challenge): The formal statement matches (O) and the deletion sentence.
- **Mimo** (reply lines 50–52; does not challenge): No counterexample in this part; the look's witness (deletion can make an undetermined answer determined) does not contradict FC01 and shows a property not claimed.
- **Mimo** (reply line 82; does not challenge): Attack: were deletion to remove ports or components, Sol would live in another space; the text forces I03 ("full relation"), so no counterexample; monotonicity holds under the definitions.
  - Quotations: “full relation” — found at L103, L255.
- **GLM** (reply line 27; does not challenge): The formal statement follows from (O) and L103; the title's "deletion never removes a solution" holds because V is fixed (I03), which L91 and L103 settle; the look's witness is no counterexample to any sentence of this part and bears on NC2's wording (L255, not given in this part).
  - Quotations: “deletion never removes a solution” — not found in the text; found in the brief.
- **GLM** (reply line 75; challenges): Monotonicity follows from (O) for any domains and cannot be broken while (O) and I03 stand; a hand model reproduces the look's witness (a component with empty relation at (1,b); deleting it makes the query determined); the reader says this tells against NC2's wording only (L255, a line not given in this part), not against any sentence of this part.
- **Goes to a checker** (rule 5): challenged by GLM. Lines at stake: L255.

#### FC02 · claim · Direction is read from the admitted edits; output status is not

Lines it formalizes or quotes (from the brief): L109, L325.

- **Mimo** (reply line 44; does not challenge): The formal statement matches the text given the inventions.
- **Mimo** (reply line 84; challenges): Attack by hand: if "output" were read at every edit of A rather than at the identity, a one-component model makes output depend on A, against FC02 (b); the text's "across B" does not force that reading, so the counterexample tells against the other choice of I05; the text should settle the reading (wording under D2.3).
  - Proposal `M1-B5` (reply lines 29–32; printed in full under D2.3 above), would change L109.
  - Quotations: “across B” — found at L109; “across A” — not found in the text; not in the brief.
- **GLM** (reply lines 29–31; challenges): Parts (a) and (b) faithful; (c) is faithful on determination, but L325's "these ports are inputs and L is an output" reads as if L's output status followed from A, which by D2.3 it does not, and "the direction H,θ → L is carried by asg" overstates, since under the A L325 describes asg(L) is undefined; proposes a new L325.
  - Proposal `G1-B1` (reply lines 31), would change L325:

````
> L325 | Under \(A\) containing interventions on \(H\) and \(\theta\), these ports are inputs and \(L\) is not; \(L\), \(H\) and \(\theta\) are alike outputs of the relation \(L=H\cot\theta\), and the direction \(H,\theta\to L\) is carried by the edits \(A\) admits, not by output status.
````

  - Quotations: “Under A containing interventions on H and θ, these ports are inputs and L is an output” — found at L325; “the direction H,θ → L is carried by asg” — not found in the text; found in the brief.
- **GLM** (reply line 77; challenges): (b) cannot fail while D2.3 stands; attack on (c)'s wording: with A exactly as L325 describes, Set_L is empty and asg(L) undefined, so L's tie to its component rests on output status, not on asg; the computed claim rests on the pole encoding's fuller A (I65, I92); no change beyond the L325 rewrite.
  - Proposal `G1-B1` (reply lines 31; printed in full under FC02 above), would change L325.
- **External reader and case card:** E04 (the external reader) challenges the sentence this item formalizes (section 3 below).
- **Goes to a checker** (rule 5): challenged by GLM and Mimo; challenged by E04 (the external reader). Lines at stake: L109, L325.

#### FC11 · claim · Roles are relative to A; families are relative to C

Lines it formalizes or quotes (from the brief): L109, L113.

- **Mimo** (reply line 46; does not challenge): The formal statement matches the text.
- **Mimo** (reply line 86; does not challenge): Attack: C outside A × B is excluded by the text; an undefined asg(v) leaves the existence claim standing; no counterexample.
- **GLM** (reply line 33; challenges): Faithful, both halves by construction; it exposes that the "that is" clause of L109 asserts the equivalence FC11 denies (matter 5).
  - Proposal `G1-B5` (reply lines 87; printed in full under D2.4 above), would change L109.
  - Quotations: “that is” — found at L11, L37, L39, L57 and 9 more lines.
- **GLM** (reply line 79; challenges): The attack lands on the sentence behind the claim: on the pole with C = {(1,b0)} the "that is" clause equates what A gives with what C leaves unsettled; with C holding one intervention on H under reading R-i, Causal_C(c_H) needs L_{c_H} both to change and not to change under it, so L123 cannot hold in any contract containing an intervention on the output port; hence the L109 rewrite adopts R-ii.
  - Proposal `G1-B5` (reply lines 87; printed in full under D2.4 above), would change L109.
  - Quotations: “that is” — found at L11, L37, L39, L57 and 9 more lines.
- **Goes to a checker** (rule 5): challenged by GLM. Lines at stake: L109.

#### I01 · invention · Composition of edits: a partial monoid with Kleene associativity

Lines it formalizes or quotes (from the brief): L91.

- **Mimo** (reply line 56; challenges): Not settled: "partial associative" is ambiguous; the wording proposed under D1.1 settles strong associativity.
  - Proposal `M1-B1` (reply lines 4–7; printed in full under D1.1 above), would change L91.
  - Quotations: “partial associative” — found at L91.
- **GLM** (reply lines 41–45; challenges): Not settled: "partial associative composition" does not choose between Kleene and weak associativity; Kleene should be written in, since under weak associativity whether an edit of an edit exists depends on bracketing; proposes a new L91 (writes in I01).
  - Proposal `G1-B2` (reply lines 43; printed in full under D1.1 above), would change L91.
  - Quotations: “partial associative composition” — found at L91.
- **Goes to a checker** (rule 5): challenged by GLM and Mimo. Lines at stake: L91.

#### I02 · invention · No law links a composite edit's relations to its parts' relations

Lines it formalizes or quotes (from the brief): L91, L574.

- **Mimo** (reply line 58; challenges): Settled by the text: L574's "supplied independently for each (a,b)" means no law ties composites to their parts.
  - Quotations: “The component relations \(L_j(a,b)\) are supplied independently for each \((a,b)\).” — found at L574.
- **GLM** (reply line 47; challenges): Settled by L574 ("supplied independently for each (a,b)" covers composite pairs); no change; G-surg's action law is still a legitimate interpretation, and both families were used.
  - Quotations: “The component relations \(L_j(a,b)\) are supplied independently for each \((a,b)\)” — found at L574.
- **Goes to a checker** (rule 5): challenged by GLM and Mimo. Lines at stake: L91, L574.

#### I03 · invention · Ports and components are fixed; deletion and absence are the full relation

Lines it formalizes or quotes (from the brief): L103, L339.

- **Mimo** (reply line 60; challenges): Partly settled: deletion is settled ("full relation"); that V and J are fixed is not explicit; the reader says the wording proposed under (a) adds the invariance of V and J (the one proposal under D1.3, printed here, defines absence and does not state it).
  - Proposal `M1-B2` (reply lines 10–13; printed in full under D1.3 above), would change L339.
  - Quotations: “full relation” — found at L103, L255.
- **GLM** (reply lines 49–53; challenges): Half settled: L103's deletion sentence fixes deletion; absence of a port and the fixedness of V and J are not settled and L339 needs both; proposes a new L103 (writes in I03, I04's residue and H03).
  - Proposal `G1-B3` (reply lines 51; printed in full under D1.1 above), would change L103.
  - Quotations: “A deleted component imposes the full relation on its ports” — found at L103, L255.
- **Goes to a checker** (rule 5): challenged by GLM and Mimo. Lines at stake: L103, L339.

#### I04 · invention · Setting a port: a surgical edit, and the assigning component read off the edits

Lines it formalizes or quotes (from the brief): L103, L109, L119.

- **Mimo** (reply line 62; challenges): Not settled: "sets a port directly" is undefined; the wording proposed under D2.1 defines it surgically.
  - Proposal `M1-B3` (reply lines 18–21; printed in full under D2.1 above), would change L103.
  - Proposal `M1-B4` (reply lines 23–26; printed in full under D2.1 above), would change L109.
  - Quotations: “sets a port directly” — not found in the text; not in the brief.
- **GLM** (reply line 55; challenges): Partly settled: L109's "No role assignment is supplied" excludes alternative (a); L103's "does not add an equation beside an incompatible one" excludes (c); (b) fails on the pole; the residue (asg read off the setting edits, undefined when two) is written in by the L103 rewrite.
  - Proposal `G1-B3` (reply lines 51; printed in full under D1.1 above), would change L103.
  - Quotations: “No role assignment is supplied” — found at L109; “it does not add an equation beside an incompatible one” — found at L103.
- **External reader and case card:** E04 (the external reader) challenges the sentence this item formalizes (section 3 below).
- **Goes to a checker** (rule 5): challenged by GLM and Mimo; challenged by E04 (the external reader). Lines at stake: L103, L109.

#### I05 · invention · 'Output': at the identity edit, and 'determined' as at most one value

Lines it formalizes or quotes (from the brief): L109.

- **Mimo** (reply line 64; challenges): Not settled: which edit, and "across B", are ambiguous; the wording proposed under D2.3 fixes the identity edit and every boundary.
  - Proposal `M1-B5` (reply lines 29–32; printed in full under D2.3 above), would change L109.
  - Quotations: “across B” — found at L109.
- **GLM** (reply lines 57–61; challenges): Not settled by the words; settled by the pole (at most one value, at the identity edit, across all of B); proposes a new L109 (writes in I05 and I80).
  - Proposal `G1-B4` (reply lines 59; printed in full under D2.3 above), would change L109.
- **External reader and case card:** E04 (the external reader) challenges the sentence this item formalizes (section 3 below).
- **Goes to a checker** (rule 5): challenged by GLM and Mimo; challenged by E04 (the external reader). Lines at stake: L109.

#### I77 · invention · Finite models and the bounds of the search

Lines it formalizes or quotes (from the brief): L91, L105.

- **Mimo** (reply line 66; does not challenge): Not settled; the text allows arbitrary domains; the search's finiteness is an implementation choice and should stay open.
- **GLM** (reply line 63; does not challenge): Not the text's to settle: bounds of a search; stays recorded; FC01 is provable by hand anyway.
  - Quotations: “holds on all models tried” — not found in the text; found in the brief.
- **Goes to no checker**: no point challenges it and it is not one of the twelve; recorded under rule 7 below.

#### I78 · invention · Two families of generated organizations: surgical edits with override, and free edits

Lines it formalizes or quotes (from the brief): L91, L574.

- **Mimo** (reply line 68; does not challenge): Not settled; the text does not say how organizations are generated; should stay open.
- **GLM** (reply line 65; does not challenge): Same status as I77; no change.
- **Goes to no checker**: no point challenges it and it is not one of the twelve; recorded under rule 7 below.

#### I80 · invention · The identity edit can be a setting edit

Lines it formalizes or quotes (from the brief): L109.

- **Mimo** (reply lines 70–74; challenges): Not settled whether the identity edit can set a port; proposes wording that lets 1 belong to Set_v where the assigning component's relation at 1 is a slice at every boundary (placed "after the definition of Set_v", the maths' D2.1; no line of the text named; the nearest sentence is L109's).
  - Proposal `M1-B7` (reply lines 71–74), would change L109:

````
Add after the definition of Set_v:
The identity edit 1 may belong to Set_v if for every b, L_{asg(v)}(1,b) is a slice w_v = x; in that case v is an input.
````

- **GLM** (reply line 67; challenges): Not settled; the identity should be excluded (if 1 could set H, A = {1} would make H an input of an unedited organization, emptying L109's "which edits it admits" and making L325's conditional pointless); written in by the L109 rewrite under I05.
  - Proposal `G1-B4` (reply lines 59; printed in full under D2.3 above), would change L109.
  - Quotations: “which edits it admits” — found at L109; “Under A containing interventions…” — found at L325.
- **Goes to a checker** (rule 5): challenged by GLM and Mimo. Lines at stake: L109.

#### H03 · H-entry · A setting edit sets its port at every boundary (D2.1)

Lines it formalizes or quotes (from the brief): L109.

- **Mimo** (reply line 76; challenges): Not settled: the quantifier over boundaries is unrecorded; the reader says the wording proposed under (a) includes "at every boundary b" (the L103 proposal printed here says "at boundary b"; the output proposal under D2.3 says "for every boundary b").
  - Proposal `M1-B3` (reply lines 18–21; printed in full under D2.1 above), would change L103.
  - Quotations: “at every boundary b” — not found in the text; not in the brief.
- **GLM** (reply line 69; challenges): Not settled; the every-boundary reading should stand (L109 states input as a property of A alone; a some-boundary reading would let inputhood flicker with b); written into the L103 rewrite.
  - Proposal `G1-B3` (reply lines 51; printed in full under D1.1 above), would change L103.
  - Quotations: “at every boundary” — not found in the text; found in the brief.
- **Goes to a checker** (rule 5): challenged by GLM and Mimo. Lines at stake: L103.

#### H04 · H-entry · Direction defined as (Input_A, asg) (D2.5)

Lines it formalizes or quotes (from the brief): L109.

- **Mimo** (reply line 78; challenges): The text says direction is a consequence, not a pair; (Input_A, asg) is an invention; FC02 can be stated without defining direction; no change to the text.
- **GLM** (reply line 71; challenges): The words deliberately say what direction is a consequence of, not what it is; no text change; D2.5's pair should get an invention number and be noted as thin.
- **Goes to a checker** (rule 5): challenged by GLM and Mimo. Lines at stake: L109.

#### L123 · round-1 change · the round-1 change at L123

Lines it formalizes or quotes (from the brief): L123.

- **Mimo** (reply line 90; does not challenge): The removal of "and under replacement of the component" matches D4.6; no further change.
  - Quotations: “and under replacement of the component” — not found in the text; found in the brief.
- **GLM** (reply line 83; challenges): The removal should stand (by L103 a changed rule is a changed component, so the clause was redundant); with R-ii adopted L123 is satisfiable and needs no change; under R-i it is not (the FC11 model), which makes settling I06 urgent; no wording for L123 itself.
  - Quotations: “and under replacement of the component” — not found in the text; found in the brief.
- **Goes to a checker** (rule 5): challenged by GLM. Lines at stake: L109, L123.

#### matter 5 · round-1 matter · L109 gives roles "under A" while (K) builds a signature on a contract C.

Lines it formalizes or quotes (from the brief): L109.

- **Mimo** (reply lines 92–96; challenges): L109 gives roles under A while (K) builds signatures on C; the text should say these are separate; proposes a sentence after L113.
  - Proposal `M1-B8` (reply lines 93–96), would change L113:

````
Add after L113:
Roles (input, output, observation) are defined under A; signatures (causal assignment, measurement, rule) are defined under a contract C ⊆ A × B.
````

- **GLM** (reply lines 85–93; challenges): Yes, a change: the "that is" clause equates a role read off A with a signature on C ⊆ A × B, and FC11's computation shows they come apart; proposes the full L109 rewrite (writes in I05, I06, I80; its last clause gives a contract-relative reading) and a sentence appended to L113 (writes in I09).
  - Proposal `G1-B5` (reply lines 87; printed in full under D2.4 above), would change L109.
  - Proposal `G1-B6` (reply lines 93; printed in full under D4.5 above), would change L113.
  - Quotations: “that is” — found at L11, L37, L39, L57 and 9 more lines.
- **Goes to a checker** (rule 5): challenged by GLM and Mimo. Lines at stake: L109, L113.

#### Part 1: items no point addresses

Items of this part on which neither reader made any point (both replies read whole): E1. Each is recorded under rule 7 in section 6 unless a point on it in another part sends it to a checker.

### Part 2: The three families of signatures

Brief: `tests/S104 Round 2 - the maths against the words - part 02, The three families of signatures.md`. Replies: `s104_maths_mimo_2.response.txt` (Mimo), `s104_maths_glm_2.response.txt` (GLM).

#### D2.1 · definition · Setting edit; the assigning component

Lines it formalizes or quotes (from the brief): L103, L119.

- **Mimo:** no point on this item.
- **GLM** (reply line 5; challenges): The surgical form is what L119's "only … not the relations of the components that read it" says, and L103's last sentence is mirrored; what a composite of settings is is not fixed (H01); the words need the addition proposed under H01.
  - Proposal `G2-B6` (reply lines 85–87), would change L119:

````
> L119 | An edit that sets a port replaces only the component that assigns the port (above), not the relations of the components that read it. An edit that replaces several components together sets no port, edits no rule, and is an intervention on none of them alone.
````

  - Quotations: “only … not the relations of the components that read it” — found at L119.
- **External reader and case card:** E04 (the external reader) challenges the sentence this item formalizes (section 3 below).
- **Goes to a checker** (rule 5): challenged by GLM; challenged by E04 (the external reader). Lines at stake: L119.

#### D2.2 · definition · Input

Lines it formalizes or quotes (from the brief): L109.

- **Mimo** (reply line 34; does not challenge): Named among the items with nothing to add.
- **GLM** (reply lines 7–13; challenges): The formal drops "directly"; under H01's default and under the reader's H01 wording no edit sets a port except a single setting, so "directly" does no work; proposes dropping it from L109 (or leaving it, inert).
  - Proposal `G2-B1` (reply lines 9–11), would change L109:

````
> L109 | A port \(v\) is an **input** under \(A\) when \(A\) contains an edit that sets \(v\).
````

  - Quotations: “directly” — found at L109, L119.
- **Goes to a checker** (rule 5): challenged by GLM. Lines at stake: L109.

#### D2.4 · definition · Observation edits (two readings)

Lines it formalizes or quotes (from the brief): L109.

- **Mimo** (reply lines 3–6; challenges): The maths carries two readings where the words carry one: a setting of the reading alters the relation that reports it and leaves what it reports, and L127 names "change only the reading"; so R-i is what the words say and should stand, and R-ii is a hedge the text does not warrant, to be recorded as a departure.
  - Quotations: “A port is an **observation** when \(A\) contains an edit that alters the relation reporting it without altering what it reports, that is, when the component …” — found at L109; “change only the reading” — found at L127.
- **GLM** (reply line 15; does not challenge): Carrying both readings is right, since the sentence does not decide whether replacing the reporting component alters the relation reporting it; which reading the text should take is under I06.
- **Goes to a checker** (rule 5): challenged by Mimo. Lines at stake: L109.

#### D4.1 · definition · Signature (K)

Lines it formalizes or quotes (from the brief): L116.

- **Mimo** (reply line 34; does not challenge): Named among the items with nothing to add.
- **GLM** (reply line 17; does not challenge): Exact.
- **GLM** (reply line 119; does not challenge): Named among the items with nothing to add (with FC09's computation and FC14's scan).
- **Goes to no checker**: no point challenges it and it is not one of the twelve; recorded under rule 7 below.

#### D4.5 · definition · Change and invariance on a contract

Lines it formalizes or quotes (from the brief): L123, L124, L125.

- **Mimo** (reply line 34; does not challenge): Named among the items with nothing to add.
- **GLM** (reply line 19; challenges): The same-boundary comparison matches L119; the vacuity of invariance and the existential reading of "changes" are not in the words (see I09).
  - Proposal `G2-B5` (reply lines 73–75), would change L119:

````
> L119 | An edit that sets a port replaces only the component that assigns the port (above), not the relations of the components that read it. A signature changes under a class of edits on a contract when some edit of that class on the contract alters it, and is invariant under the class when none does — invariant under a class the contract does not touch.
````

  - Quotations: “a component's relation under each \((a,b)\in C\)” — found at L119; “changes” — found at L11, L13, L15, L17 and 33 more lines.
- **Goes to a checker** (rule 5): challenged by GLM. Lines at stake: L119.

#### D4.6 · definition · Families

Lines it formalizes or quotes (from the brief): L123, L124, L125, L347.

- **Mimo** (reply lines 8–13; challenges): The maths reads L123's "its output port" as the port the component assigns, where L109 defines "output" otherwise (on the pole H and θ are outputs of c_L too, H02); the maths should stand, since L123 speaks of an intervention, and interventions are setting edits that replace only the assigning component; the words should name the assigner; proposes a new causal bullet at L123 (writes I04 and I102 into the text; answers H02 for the assigner).
  - Proposal `M2-B2` (reply lines 10–12), would change L123:

````
> L123 | - a **causal assignment** has a signature that changes under intervention on the ports it assigns and is invariant under observation edits; a part that reads a port another part assigns has no such signature on any contract;
````

  - Quotations: “its output port” — found at L123; “output” — found at L13, L23, L109, L123 and 7 more lines; “its value is determined by \(L_j\) given the other ports” — found at L109.
- **GLM** (reply line 21; does not challenge): Causal: exact against L123 as it stands after round 1.
- **GLM** (reply line 23; challenges): Meas: three departures from L124: "the measured port" as though unique, where the maths relates measurement to each port read (I07); "the measuring relation" read as the component's own relation (I07 b); nothing makes the reading depend on the measured port (FC08), which L127's gloss does say; (i) and (iii) should go into the words (the L124 wording under (b)).
  - Proposal `G2-B2` (reply lines 47–49), would change L124:

````
> L124 | - a **measurement** has, for a port it reads and does not itself determine, a signature invariant under interventions on that port and variable under edits to the measuring relation, and a reading that depends on that port in the relation itself;
````

  - Quotations: “the measured port” — found at L124; “The measuring relation” — found at L124.
- **GLM** (reply line 25; does not challenge): Rule: reading "interventions on the world" as settings of every port the component does not assign is defensible; the rival makes no difference given D2.1 (see I08).
  - Quotations: “Interventions on the world” — found at L125; “the world” — found at L11, L57, L125, L397 and 1 more lines.
- **External reader and case card:** E05 (the external reader) challenges the sentence this item formalizes (section 3 below).
- **Goes to a checker** (rule 5): challenged by GLM and Mimo; challenged by E05 (the external reader). Lines at stake: L123, L124.

#### FC06 · claim · A setting edit leaves every reader's relation as it was

Lines it formalizes or quotes (from the brief): L119, L124.

- **Mimo** (reply line 34; does not challenge): Named among the items with nothing to add in (a) (its wording defect is taken up in (d)).
- **Mimo** (reply line 82; challenges): Two breaks in the claim's wording: (1) a model with two components each set through by an edit setting p, so asg(p) is undefined and "j ≠ asg(m)" has no value; (2) on the pole, if a composite setting of H and L is a setting edit of H (H01's alternative), c_L's relation changes and the universal fails; repair the claim's wording, not the text (rests on I04, H01).
  - Quotations: “j ≠ asg(m)” — not found in the text; found in the brief; “j is not a component through which a sets m” — not found in the text; not in the brief.
- **GLM** (reply line 27; does not challenge): The statement is the sentence and holds by D2.1.
- **GLM** (reply line 95; does not challenge): Unbreakable except through H01; with the H01 wording it survives composites.
- **Goes to a checker** (rule 5): challenged by Mimo. Lines at stake: L119, L124.

#### FC07 · claim · The three families on the pole's contracts, under both readings of 'observation edit'

Lines it formalizes or quotes (from the brief): L109, L123, L127, L325.

- **Mimo** (reply line 50; challenges): The computation "pole C2 with composites" (no component causal, every component rule) is as claimed but shows the families collapsing, a consequence of H01 (treated under H01).
  - Proposal `M2-B9` (reply lines 73–75), would change L119:

````
> L119 | An edit that sets a port replaces the component that assigns the port (above), not the relations of the components that read it; an edit that sets several ports at once sets each of them.
````

  - Quotations: “pole C2 with composites” — not found in the text; found in the brief.
- **Mimo** (reply line 84; challenges): Holds beyond the search but not as worded: under I04 and R-i a setting of o that changes L_j is itself an observation edit whenever j reads a port another part assigns, so Causal_C(j) implies that j reads no such port on every contract (the "contract that sets every port" hypothesis is idle); by FC06 the invariance clauses of L124 and L125 hold automatically for non-assigners, so the only discriminating clause is L123's invariance under observation edits (rests on I04, I06, I102); the L123 proposal records the consequence.
  - Proposal `M2-B2` (reply lines 10–12; printed in full under D4.6 above), would change L123.
  - Quotations: “on a contract that sets every port” — not found in the text; found in the brief.
- **GLM** (reply line 29; challenges): Computations as claimed; but L127, one of its target sentences, is not a consequence of anything here (see (d)).
  - Proposal `G2-B3` (reply lines 53–55), would change L127:

````
> L127 | In particular, a part that reads or reports another part has a measurement's signature on a contract that holds an edit altering its reading: change only the reading and the part it reports stays as it was; change the part and the reading follows where the reading depends on it.
````

- **GLM** (reply line 97; challenges): The attack succeeds against L127: on the pole with C1 (settings of H and θ), c_L is in no family under either reading, so L127's "a part that reads or reports another part has a measurement's signature" does not hold of the text's own example on one of its contracts, with no invention needed; the hedge in the L127 wording removes it; a smaller attack: with one-valued domains Causal is empty everywhere, just outside the bounds searched, and nothing in the text says ports can differ.
  - Proposal `G2-B3` (reply lines 53–55; printed in full under FC07 above), would change L127.
  - Quotations: “a part that reads or reports another part has a measurement's signature” — found at L127; “on a contract that holds an edit altering its reading” — not found in the text; not in the brief.
- **External reader and case card:** E05 (the external reader) challenges the sentence this item formalizes (section 3 below).
- **Goes to a checker** (rule 5): challenged by GLM and Mimo; challenged by E05 (the external reader). Lines at stake: L119, L123, L124, L125, L127.

#### FC08 · claim · L127's gloss of a measurement's signature has a clause about solutions

Lines it formalizes or quotes (from the brief): L119, L127.

- **Mimo** (reply lines 38–48; challenges): The witness (a component meeting both clauses of L124 whose reading never follows m) is a counterexample to L127's gloss as an unpacking of the signature, not to the definitions and not to an invention: L119 keeps solution conditions out of (K), so the family cannot carry "the reading follows"; the words overstate and the maths stands; proposes a new gloss at L127 (rests on I06, I07).
  - Proposal `M2-B7` (reply lines 45–47), would change L127:

````
> L127 | change only the reading and the part it reports stays as it was; change the part and the reading follows — the first is a pattern in (K); the second is a condition on the solutions, which (K) does not carry and the family does not require.
````

  - Quotations: “A signature is built from a component's relation under each \((a,b)\in C\), not from the values its ports take in a solution” — found at L119; “the reading follows” — found at L127.
- **GLM** (reply line 31; challenges): The claim rightly finds that L127's second clause is about solutions while the bullets and L119 are about relations (see (b)).
  - Proposal `G2-B3` (reply lines 53–55; printed in full under FC07 above), would change L127.
- **GLM** (reply lines 45–55; challenges): The witness is a counterexample to the text, not to an invention: the mismatch is between L119 ("not from the values its ports take in a solution") and L127 ("change the part and the reading follows"), and a measurement that can ignore what it measures is not what L124 should allow; proposes a new L124 (writes I07 in and closes U5 through L109's output definition) and a new L127 sentence.
  - Proposal `G2-B2` (reply lines 47–49; printed in full under D4.6 above), would change L124.
  - Proposal `G2-B3` (reply lines 53–55; printed in full under FC07 above), would change L127.
  - Quotations: “not from the values its ports take in a solution” — found at L119; “change the part and the reading follows” — found at L127; “Does not itself determine” — not found in the text; not in the brief.
- **External reader and case card:** E05 (the external reader) challenges the sentence this item formalizes (section 3 below).
- **Goes to a checker** (rule 5): challenged by GLM and Mimo; challenged by E05 (the external reader). Lines at stake: L124, L127.

#### FC09 · claim · Four names, three families: a constitutive status is a rule application

Lines it formalizes or quotes (from the brief): L121, L347.

- **Mimo** (reply line 32; challenges): The maths maps a constitutive status onto Rule_C while the words name four things and give three bullets; the maths should stand (L347 gives the constitutive rule the rule family's shape); wording under matter 4.
  - Proposal `M2-B10` (reply lines 98–100), would change L121:

````
> L121 | What ordinary language calls a cause, a measurement, a rule or a constitutive status are families of signatures; a constitutive status has a rule application's signature (below):
````

- **Mimo** (reply line 86; challenges): The computation runs under I08 and cannot tell I08 from its alternative (b), under which the rule family is empty; the claim is the invention restated.
- **GLM** (reply line 33; does not challenge): Exact, given I08's reading of L347, which L347's wording ("edits to C_r", "interventions on Z") bears out.
  - Quotations: “edits to \(C_r\)” — found at L347; “interventions on \(Z\)” — found at L347.
- **GLM** (reply line 99; does not challenge): Definitional apart from I08; the two readings of "the world" do not differ observably.
  - Quotations: “the world” — found at L11, L57, L125, L397 and 1 more lines.
- **Goes to a checker** (rule 5): challenged by Mimo. Lines at stake: L121.

#### FC10 · claim · L57 against the new L123

Lines it formalizes or quotes (from the brief): L57, L123.

- **Mimo** (reply lines 15–20; challenges): I09 reads "changes under" existentially, L57's "changes when the rule is edited" universally; the maths should stand (L123's "changes under" and "invariant under" are contradictories only when change is existential), and L57 should carry the same; proposes a new sentence at L57.
  - Proposal `M2-B3` (reply lines 17–19), would change L57:

````
> L57 | a rule's application can change when the rule is edited and not when the world is intervened on; a cause's assignment can change under intervention.
````

  - Quotations: “changes under” — found at L57, L123; “changes when the rule is edited” — found at L57; “changes under …” — found at L57, L123; “invariant under …” — found at L123, L124, L125, L347 and 1 more lines.
- **Mimo** (reply line 88; challenges): Hand model: Rule_C(j) holds while an edit to the rule has a pair in C that leaves the signature unchanged, so L57's clause fails if "changes when" is universal (rests on I08, I09 (c)).
  - Proposal `M2-B3` (reply lines 17–19; printed in full under FC10 above), would change L57.
  - Quotations: “changes when” — found at L11, L57.
- **GLM** (reply line 35; does not challenge): The searched part holds by the definitions; the untested part is settled by reading: L57 names rule edits, world interventions and intervention on the output, and the clause removed in round 1 has no counterpart in L57; both readings of the untested part hold.
  - Quotations: “and under replacement of the component” — not found in the text; found in the brief.
- **GLM** (reply line 101; does not challenge): Holds, and the untested part passes by reading; L57's "not when the world is intervened on" and Rule's Inv are both universal, so the implication survives either reading.
  - Quotations: “not when the world is intervened on” — found at L57.
- **Goes to a checker** (rule 5): challenged by Mimo. Lines at stake: L57.

#### FC12 · claim · Invariance clauses can be vacuous; change clauses cannot

Lines it formalizes or quotes (from the brief): L124, L125.

- **Mimo** (reply line 34; does not challenge): Named among the items with nothing to add in (a).
- **Mimo** (reply line 92; does not challenge): Nothing to break; the asymmetry is only half the story, since the invariance clauses are automatic as well as vacuous.
- **GLM** (reply line 37; does not challenge): Follows from I09's definitions; the asymmetry is the text's own structure, not a defect; the defect is L127's unhedged gloss.
- **GLM** (reply line 103; does not challenge): Definitional under I09; the thing to fix is L127, not this.
- **External reader and case card:** E05 (the external reader) challenges the sentence this item formalizes (section 3 below).
- **Goes to a checker** (rule 5): challenged by E05 (the external reader). Lines at stake: L124, L125.

#### FC13 · claim · The families are patterns in (K), not additional data

Lines it formalizes or quotes (from the brief): L127.

- **Mimo** (reply lines 22–30; challenges): The formal statement is honest but not what the words say: how an edit is classed is read off the whole organization, not off j's own (K) (hand model in (d)); the maths should stand and the words should widen (K); separately, "not additional data" settles I04's alternative (a), since a declared assigner would be additional data; proposes a new sentence at L127.
  - Proposal `M2-B5` (reply lines 27–29), would change L127:

````
> L127 | These are descriptions of patterns in (K) and in how the edits of the contract touch the other components, not additional data.
````

  - Quotations: “of sig_C(j) and of how each edit of C is classed” — not found in the text; found in the brief; “These are descriptions of patterns in (K), not additional data.” — found at L127; “not additional data” — found at L127.
- **Mimo** (reply line 90; challenges): Hand model: two organizations with the same sig_C(c_o) and the same C in which Rule_C(c_o) fails in one and holds in the other, because whether the edit is a setting or observation edit depends on c_m; so the family is not a pattern in (K) (rests on I04, I08, I09).
  - Proposal `M2-B5` (reply lines 27–29; printed in full under FC13 above), would change L127.
- **GLM** (reply line 39; does not challenge): Holds by construction; its worry about a declared asg is settled by L109's "No role assignment is supplied"; FC13 needs no invention.
  - Quotations: “No role assignment is supplied” — found at L109.
- **GLM** (reply line 105; does not challenge): Holds by construction; L109 forecloses the declared-asg rival; under H01's default the classing is still read off (A, L).
  - Quotations: “No role assignment is supplied” — found at L109.
- **External reader and case card:** E05 (the external reader) challenges the sentence this item formalizes (section 3 below).
- **Goes to a checker** (rule 5): challenged by Mimo; challenged by E05 (the external reader). Lines at stake: L127.

#### FC14 · claim · No definition asks whether a component 'is' a cause

Lines it formalizes or quotes (from the brief): L127.

- **Mimo** (reply line 34; does not challenge): Named among the items with nothing to add in (a).
- **Mimo** (reply line 92; challenges): The scan is weaker than the sentence (it cannot rule out an equivalent definition); what carries the sentence is that every family predicate is indexed by C.
- **GLM** (reply line 41; does not challenge): Syntactic and exact.
- **GLM** (reply line 107; does not challenge): Syntactic; nothing to attack.
- **Goes to a checker** (rule 5): challenged by Mimo. Lines at stake: L127.

#### I06 · invention · Observation edits: two readings of 'the relation reporting it'

Lines it formalizes or quotes (from the brief): L109, L127.

- **Mimo** (reply line 54; challenges): Settled in favour of R-i by L109 as quoted and by L127's "a part that reads or reports another part has a measurement's signature" with "change only the reading"; R-ii stays a recorded departure; no text change.
  - Quotations: “a part that reads or reports another part has a measurement's signature” — found at L127; “change only the reading” — found at L127.
- **GLM** (reply lines 59–65; challenges): The text settles the identification of the observed port (on alternative (a) the "that is" clause could not hold); it does not settle R-i against R-ii; it should take R-i (by L103 an intervention on a port replaces the reporting component, which alters its relation; R-i alone gives the pole's C2 the reading the worked case wants); proposes a new observation sentence at L109 (writes I06's R-i into the text).
  - Proposal `G2-B4` (reply lines 61–63), would change L109:

````
> L109 | A port is an **observation** when \(A\) contains an edit that alters the relation reporting it without altering what it reports — an edit that sets the port among them — that is, when the component assigning it has a measurement's signature (below).
````

  - Quotations: “that is” — found at L11, L37, L39, L57 and 9 more lines; “the component assigning it has a measurement's signature” — found at L109.
- **External reader and case card:** E05 (the external reader) challenges the sentence this item formalizes (section 3 below).
- **Goes to a checker** (rule 5): challenged by GLM and Mimo; challenged by E05 (the external reader). Lines at stake: L109.

#### I07 · invention · 'The measured port' and 'the measuring relation'

Lines it formalizes or quotes (from the brief): L124.

- **Mimo** (reply line 56; challenges): Settled: L109 ("No role assignment is supplied") with L127's "another part" gives the measured port as one another part assigns; L116 and L103 give "the measuring relation" as the component's relation; read per port; no text change, but asg(m) must be defined and differ from j (which removes U5).
  - Quotations: “No role assignment is supplied” — found at L109; “another part” — found at L127; “A changed rule is a changed component” — found at L103; “the measuring relation” — found at L124.
- **GLM** (reply line 67; challenges): Not settled (uniqueness of "the measured port"; several read ports); L127's "a part that reads or reports another part" points to I07's per-part choice, and L124's grammar excludes the rival (b); adopt the L124 wording (writes I07 in).
  - Proposal `G2-B2` (reply lines 47–49; printed in full under D4.6 above), would change L124.
  - Quotations: “the measured port” — found at L124; “a part that reads or reports another part” — found at L127; “the measuring relation” — found at L124; “its signature … variable under edits to the measuring relation” — not found in the text; found in the brief.
- **External reader and case card:** E05 (the external reader) challenges the sentence this item formalizes (section 3 below).
- **Goes to a checker** (rule 5): challenged by GLM and Mimo; challenged by E05 (the external reader). Lines at stake: L124.

#### I08 · invention · 'Interventions on the world' and 'the rule'

Lines it formalizes or quotes (from the brief): L125.

- **Mimo** (reply lines 58–63; challenges): The main line is settled ("variable under edits to the rule" can only mean L_j varies; I08's alternative (b) would leave the family empty); open is whether the component's own setting edits count as rule edits, and L57's contrast says not; proposes a new rule bullet at L125 (writes I08 into the text).
  - Proposal `M2-B8` (reply lines 60–62), would change L125:

````
> L125 | - a **rule application** has a signature invariant under interventions on the world, that is, settings of the ports it does not assign, and variable under edits to the rule, that is, edits that alter the relation it applies other than by setting the ports it assigns.
````

  - Quotations: “variable under edits to the rule” — found at L125; “the rule is edited” — found at L57; “a cause's assignment changes under intervention” — found at L57.
- **GLM** (reply line 69; challenges): "The rule" as the component itself is settled by L347's wording; "the world" as all ports j does not assign against the ports j reads is not settled, but given D2.1 the two differ in nothing observable; should stay open, recorded in I08 as making no difference.
  - Quotations: “The rule” — found at L57, L125, L151, L347; “The world” — found at L11, L57, L125, L397 and 1 more lines.
- **Goes to a checker** (rule 5): challenged by GLM and Mimo. Lines at stake: L125.

#### I09 · invention · 'Changes under', 'invariant under', 'variable under': compared with the identity edit at the same boundary

Lines it formalizes or quotes (from the brief): L123.

- **Mimo** (reply line 65; challenges): The baseline comparison is not settled and should stay open (the searched choice and vacuous invariance are the natural readings); the existential reading of "changes under" is settled by L123's own contrast; L57 needs "can" (the proposal under FC10).
  - Proposal `M2-B3` (reply lines 17–19; printed in full under FC10 above), would change L57.
  - Quotations: “invariant” — found at L123, L124, L125, L335 and 3 more lines; “changes under” — found at L57, L123.
- **GLM** (reply lines 71–77; challenges): The same-boundary comparison is settled by L119; vacuous invariance and existential "changes" are not settled and should be written in; proposes a new L119 (writes I09 into the text).
  - Proposal `G2-B5` (reply lines 73–75; printed in full under D4.5 above), would change L119.
  - Quotations: “changes” — found at L11, L13, L15, L17 and 33 more lines.
- **Goes to a checker** (rule 5): challenged by GLM and Mimo. Lines at stake: L57, L119.

#### I102 · invention · A component assigning several ports, or a port assigned by none

Lines it formalizes or quotes (from the brief): L109, L123.

- **Mimo** (reply line 67; challenges): The text presumes a unique assigner (L103, L109), so a port with two assigners lies outside its scope; the several-ports case is carried by the L123 proposal; the clause that lets an unassigned port count among "the ports j does not assign" must not make it a measured port of j, nor its settings interventions on the world for components they alter; trim the invention; no text change.
  - Proposal `M2-B2` (reply lines 10–12; printed in full under D4.6 above), would change L123.
  - Quotations: “the component assigning that port” — found at L103; “the component assigning it” — found at L109; “the ports j does not assign” — not found in the text; found in the brief; “the world” — found at L11, L57, L125, L397 and 1 more lines; “the rule” — found at L57, L125, L151, L347.
- **GLM** (reply line 79; challenges): The union rule is unsettled and reasonable; the undefined-asg clause has U5's consequence and should be replaced by determination (L109's output), as the L124 wording does; on the causal side "its output port" is H02's question.
  - Proposal `G2-B2` (reply lines 47–49; printed in full under D4.6 above), would change L124.
  - Quotations: “its output port” — found at L123.
- **Goes to a checker** (rule 5): challenged by GLM and Mimo. Lines at stake: L123, L124.

#### U5 · U-entry · Under I102 a component can have the measurement signature for its own output port

Lines it formalizes or quotes (from the brief): L124, L127.

- **Mimo** (reply line 69; challenges): Settled against U5's consequence: L127's "another part" and L109's "the component assigning it" need the measured port assigned by another component; fix in I07 and I102 (asg(m) defined and different from j); no text change.
  - Quotations: “another part” — found at L127; “the component assigning it” — found at L109.
- **GLM** (reply line 81; challenges): Record the consequence in I102 and close it with L124's "does not itself determine"; a component measuring the port it assigns is against L109's output definition, so the text already settles it against the maths.
  - Proposal `G2-B2` (reply lines 47–49; printed in full under D4.6 above), would change L124.
  - Quotations: “does not itself determine” — not found in the text; not in the brief.
- **Goes to a checker** (rule 5): challenged by GLM and Mimo. Lines at stake: L124.

#### H01 · H-entry · A composite of settings is no setting edit, so it is an edit to the rule (D2.1 with D4.6 and I08)

Lines it formalizes or quotes (from the brief): L103, L119, L125.

- **Mimo** (reply lines 71–76; challenges): Not settled: L119's "only" answers whether readers are touched, and L103's sentence is satisfied by a composite; the collapse of the families comes from D2.1's single-edit restriction, not from the words; proposes a new L119 (writes H01's first alternative into the text).
  - Proposal `M2-B9` (reply lines 73–75; printed in full under FC07 above), would change L119.
  - Quotations: “does it touch readers?” — not found in the text; not in the brief.
- **GLM** (reply lines 83–89; challenges): The default follows most literally from L119's "only", but with L91's closure it classes composites as rule edits and collapses the families on C2*, and the first recorded rival collapses them too; the stable choice is an unrecorded third one (a composite is a joint intervention, on none alone, and an edit to no rule); proposes a new L119 (writes H01 into the text).
  - Proposal `G2-B6` (reply lines 85–87; printed in full under D2.1 above), would change L119.
- **Goes to a checker** (rule 5): challenged by GLM and Mimo. Lines at stake: L119.

#### H02 · H-entry · "its output port" read as the port the component assigns (D4.6)

Lines it formalizes or quotes (from the brief): L109, L123.

- **Mimo** (reply line 78; challenges): Settled by the intervention wording (see D4.6); the L123 proposal writes it in.
  - Proposal `M2-B2` (reply lines 10–12; printed in full under D4.6 above), would change L123.
- **GLM** (reply line 91; challenges): The text settles it against the maths: L109 defines an output, and L123's "its output port" should mean that, not asg; D4.6 should use D2.3's outputs with I102's union rule; random families were not searched under the text's reading, a gap for a later round, not a change to the text.
  - Quotations: “A port is an **output** of component \(j\) when its value is determined by \(L_j\)…” — found at L109; “its output port” — found at L123.
- **Goes to a checker** (rule 5): challenged by GLM and Mimo. Lines at stake: L123.

#### L123 · round-1 change · the round-1 change at L123

Lines it formalizes or quotes (from the brief): L123.

- **Mimo** (reply line 103; challenges): The removal is sound and needs no restoration; it leaves a causal assignment with no condition under edits to its own relation, and with R-i the family then covers only parts that read nothing (FC07); the L123 proposal under D4.6 records that consequence.
  - Proposal `M2-B2` (reply lines 10–12; printed in full under D4.6 above), would change L123.
- **GLM** (reply line 111; does not challenge): The text should stand as it is: by L103 an intervention on the output port is a replacement of the component, so the removed clause was implied by the kept one; L57 names no replacement condition either.
  - Quotations: “and under replacement of the component” — not found in the text; found in the brief.
- **Goes to a checker** (rule 5): challenged by Mimo. Lines at stake: L123.

#### matter 4 · round-1 matter · L121 names four things and gives three bullets; by L347 the rule-application bullet covers "a rule" and "a constitutive status".

Lines it formalizes or quotes (from the brief): L121, L347.

- **Mimo** (reply lines 96–101; challenges): Needs a change: the third bullet covers a rule and a constitutive status; proposes a new sentence at L121.
  - Proposal `M2-B10` (reply lines 98–100; printed in full under FC09 above), would change L121.
- **GLM** (reply lines 113–117; challenges): L347 already assigns the constitutive status to the rule family, so maths and text agree, but a reader counting names against bullets is misled; proposes a new L121.
  - Proposal `G2-B7` (reply lines 115–117), would change L121:

````
> L121 | What ordinary language calls a cause, a measurement, a rule or a constitutive status are families of signatures, the rule and the constitutive status one and the same family:
````

- **Goes to a checker** (rule 5): challenged by GLM and Mimo. Lines at stake: L121.

#### Part 2: items no point addresses

Items of this part on which neither reader made any point (both replies read whole): E1. Each is recorded under rule 7 in section 6 unless a point on it in another part sends it to a checker.

### Part 3: Kinds, and kinds read through a transport

Brief: `tests/S104 Round 2 - the maths against the words - part 03, Kinds, and kinds read through a transport.md`. Replies: `s104_maths_mimo_3.response.txt` (Mimo), `s104_maths_glm_3.response.txt` (GLM).

#### D4.1 · definition · Signature (K)

Lines it formalizes or quotes (from the brief): L116.

- **Mimo** (reply line 46; does not challenge): Named among the items with nothing to add.
  - Quotations: “descriptions of patterns in (K)” — found at L127.
- **GLM** (reply line 5; does not challenge): Faithful; nothing to add.
- **Goes to no checker**: no point challenges it and it is not one of the twelve; recorded under rule 7 below.

#### D4.2 · definition · One kind on C

Lines it formalizes or quotes (from the brief): L119.

- **Mimo** (reply line 3; challenges **OWNER QUESTION**): The maths adds a clause the words lack (β takes each port to a port with the same domain, values compared as elements, I10); β_* is what "coincide" needs; the reader calls the domain clause "the owner's question (where values are placed)" and leaves it open (the reader reads the phrase as the value domains of ports; recorded as the reader states it); L119's "A kind is an equivalence class" settles against I10 (b), which is not transitive (model under FC03).
  - Quotations: “a bijection of their footprints” — found at L119; “coincide” — found at L119, L562, L564; “A kind is an equivalence class of components under this relation” — found at L119.
- **GLM** (reply line 7; challenges): The maths says what the sentence says only after I10 fills two gaps (what a footprint bijection does to values; what "coincide" means across footprints); the maths should stand, but the text should say which way (wording under I10).
  - Proposal `G3-B2` (reply lines 46–48), would change L119:

````
Two components j,j′ are of one kind on C when there is a bijection of their footprints, carrying each port to a port with the same values, under which sig_C(j) and sig_C(j′) coincide, values compared as values.
````

  - Quotations: “a bijection of their footprints” — found at L119; “coincide” — found at L119, L562, L564.
- **Goes to a checker** (rule 5): challenged by GLM and Mimo. Lines at stake: L119.
- Marks: OWNER QUESTION points present.

#### D4.3 · definition · Reading through a transport

Lines it formalizes or quotes (from the brief): L119.

- **Mimo** (reply lines 5–10; challenges): The sentence names τ alone while boundaries need σ (L189), and L554 writes τ[C] as if τ acted on pairs; the maths stands and the words should carry it; proposes a new sentence in L119 (writes I12 in, names σ).
  - Proposal `M3-B1` (reply lines 7–9), would change L119:

````
A component of \(E\) and a component of \(E'\) are of one kind on \(C\) when their signatures, read on \(C\) through \(\tau,\sigma\) and \(\tau',\sigma'\), coincide under a footprint bijection.
````

- **GLM** (reply line 9; challenges): Faithful given I12; holding the boundary fixed would not read the signature on C at all; the text should name the boundary translation (wording under I12).
  - Proposal `G3-B4` (reply lines 60–62), would change L119:

````
A component of E and a component of E′ are of one kind on C when their signatures, read on C through τ and τ′ and through the boundary translations of the two transports, coincide under a footprint bijection
````

- **Goes to a checker** (rule 5): challenged by GLM and Mimo. Lines at stake: L119.

#### D4.4 · definition · Signature of a counterpart

Lines it formalizes or quotes (from the brief): L119.

- **Mimo** (reply lines 12–17; challenges): Open whether the counterpart is read on D's own ports and domains (I94) or carried to V_k by λ (D4.4); "read on C directly" leaves room for the first, "up to the port translation" points to the second; proposes a new sentence in L119 mirroring L233 (writes I94's disambiguation in).
  - Proposal `M3-B2` (reply lines 14–16), would change L119:

````
Argument 1 makes the like comparison between an active component \(k\) of \(E\), read on \(C\) through \(\tau\), and its counterpart \(\lambda(k)\), read on \(C\) directly with its hidden ports projected away and what remains carried to \(V_k\) by the port translation of \(\lambda\).
````

  - Quotations: “read on C directly” — found at L119; “read on C through τ” — found at L119; “up to the port translation” — found at L119, L554.
- **GLM** (reply line 11; challenges): "By (K)" at L556 cannot give sig_C(λ(k)), since (K) is stated for a component and λ(k) is a subnetwork; the maths' extension (I13) is legitimate, the text's "By (K)" an overreach; the words should change (matter 1); D4.4's carrying to V_k is what L119's "up to the port translation" asks.
  - Proposal `G3-B9` (reply lines 118–120), would change L556:

````
By (K), read on λ(k) taken as one component of D whose relation at (a,b) is proj^λ_{V_k} Sol_{λ(k)}(a,b), sig_C(λ(k)) = {(a,b, proj^λ_{V_k} Sol_{λ(k)}(a,b))}.
````

  - Quotations: “up to the port translation” — found at L119, L554.
- **Goes to a checker** (rule 5): challenged by GLM and Mimo. Lines at stake: L119, L556.

#### D4.5 · definition · Change and invariance on a contract

Lines it formalizes or quotes (from the brief): L123, L124, L125.

- **Mimo** (reply line 46; does not challenge): Named among the items with nothing to add; rests on inventions given in other parts (I04, I06–I09).
  - Quotations: “descriptions of patterns in (K)” — found at L127.
- **GLM** (reply line 13; does not challenge): Faithful given I09's reading, which the reader calls forced ("changes under an edit" has no other referent in (K)); the vagueness named belongs to other parts; nothing to add.
  - Quotations: “changes under an edit” — not found in the text; not in the brief; “observation edits” — found at L123; “the measured port” — found at L124.
- **GLM** (reply line 125; does not challenge): Named among the items with nothing to add.
- **Goes to no checker**: no point challenges it and it is not one of the twelve; recorded under rule 7 below.

#### D4.6 · definition · Families

Lines it formalizes or quotes (from the brief): L121, L123, L124, L125, L347.

- **Mimo** (reply line 46; does not challenge): Named among the items with nothing to add; L127's "descriptions of patterns in (K)" is what D4.6's predicates being functions of D and C give.
  - Quotations: “descriptions of patterns in (K)” — found at L127.
- **GLM** (reply line 15; does not challenge): The three family predicates match the three bullets given I04, I06–I08; L121's four against three is FC09's matter; the maths should stand.
- **GLM** (reply line 125; does not challenge): Named among the items with nothing to add.
- **External reader and case card:** E05 (the external reader) challenges the sentence this item formalizes (section 3 below).
- **Goes to a checker** (rule 5): challenged by E05 (the external reader). Lines at stake: L121, L123, L124, L125.

#### D5.1 · definition · Transport

Lines it formalizes or quotes (from the brief): L186, L189.

- **Mimo** (reply lines 19–24; challenges **OWNER QUESTION**): π has a total arrow but "on the stated scope"; τ and σ carry no domain clause; the maths' λ carries value maps (I14); partiality (I17) is not in the words, and (F1) over C needs τ, σ defined at every pair of C; proposes a new clause in L189 (writes I17 in); whether a port translation may carry values across differing domains stays open, called "owner's question" by the reader.
  - Proposal `M3-B3` (reply lines 21–23), would change L189:

````
where \(\pi:X_D\to X_E\) on the stated scope, \(\tau\) translates edits, \(\sigma\) translates boundaries, and \(\lambda\) assigns each component of \(E\) a subnetwork of \(D\) with a port translation; \(t\) translates \((a,b)\) when \(\tau\) and \(\sigma\) are defined there and \(\pi\) is defined on \(\operatorname{Sol}_D(a,b)\), and \((F1)\) is read over the pairs \(t\) translates.
````

  - Quotations: “on the stated scope” — found at L189; “a subnetwork of D with a port translation” — found at L189.
- **GLM:** no point on this item.
- **Goes to a checker** (rule 5): challenged by Mimo. Lines at stake: L189.
- Marks: OWNER QUESTION points present.

#### D5.2 · definition · Projection

Lines it formalizes or quotes (from the brief): L233.

- **Mimo** (reply lines 26–31; challenges): "Imposing the constraints of λ(k)" means the subnetwork's own constraints (I14), not the whole of D; one word keeps the words from drifting; proposes adding "alone" in L233 (writes I14's reading in).
  - Proposal `M3-B4` (reply lines 28–30), would change L233:

````
the relation obtained by imposing the constraints of \(\lambda(k)\) alone, projecting away its hidden ports and carrying what remains to \(V_k\) by the port translation of \(\lambda\)
````

  - Quotations: “imposing the constraints of λ(k)” — found at L233.
- **GLM:** no point on this item.
- **Goes to a checker** (rule 5): challenged by Mimo. Lines at stake: L233.

#### D5.4 · definition · (F1)

Lines it formalizes or quotes (from the brief): L236.

- **Mimo** (reply lines 33–38; challenges): (F1)'s display has no quantifier; the maths reads it over Γ (I15); L554 says "no active component k of E" while L245 says "no component of E"; Γ stands with L554 and L245 should follow; proposes new wording in L245.
  - Proposal `M3-B5` (reply lines 35–37), would change L245:

````
By (K), no active component of \(E\) whose signature on \(C\) differs from its counterpart's meets (F1)
````

  - Quotations: “no active component k of E” — found at L554; “no component of E” — found at L245; “up to the port translation” — found at L119, L554; “each component” — found at L91, L119, L189, L281 and 1 more lines.
- **GLM:** no point on this item.
- **Goes to a checker** (rule 5): challenged by Mimo. Lines at stake: L245.

#### FC03 · claim · 'Of one kind on C' is an equivalence relation

Lines it formalizes or quotes (from the brief): L119.

- **Mimo** (reply line 46; does not challenge): Named among the items with nothing to add in (a).
  - Quotations: “descriptions of patterns in (K)” — found at L127.
- **Mimo** (reply line 83; does not challenge): Under I10 (b) the relation is not transitive (hand model on three ports); that alternative is ruled out by L119's words, so FC03 stands as the maths has it.
- **GLM** (reply line 17; does not challenge): Says what the sentence says; reflexive, symmetric and transitive follow by reasoning from D4.2; the status should be "holds by construction" (a change to the maths' record only).
  - Quotations: “holds on all models tried” — not found in the text; found in the brief.
- **GLM** (reply line 92; does not challenge): Tried and found nothing; follows by reasoning from D4.1–D5.4; should be re-statused "holds by construction".
  - Quotations: “holds on all models tried” — not found in the text; found in the brief.
- **Goes to no checker**: no point challenges it and it is not one of the twelve; recorded under rule 7 below.

#### FC04 · claim · A coarser contract identifies more components; a finer one can separate them

Lines it formalizes or quotes (from the brief): L119.

- **Mimo** (reply line 46; does not challenge): Named among the items with nothing to add in (a).
  - Quotations: “descriptions of patterns in (K)” — found at L127.
- **Mimo** (reply line 102; does not challenge): No attack to add: both halves follow from the definitions.
- **GLM** (reply line 19; does not challenge): Faithful given I11; (a) holds by construction, (b) is witnessed by any two components agreeing on a proper subset of C; the content is in I11's reading of "coarser".
  - Quotations: “coarser” — found at L119.
- **GLM** (reply line 92; does not challenge): (a): tried and found nothing; re-status "holds by construction".
  - Quotations: “holds on all models tried” — not found in the text; found in the brief.
- **Goes to no checker**: no point challenges it and it is not one of the twelve; recorded under rule 7 below.

#### FC05 · claim · Kinds are fixed by relations, not by solution values

Lines it formalizes or quotes (from the brief): L119.

- **Mimo** (reply line 42; challenges): The formal statement uses one bijection throughout; L119's "an edit under which the two relations stay equal" does not say which; the formal statement is a reading, not what the words force, and under the other readings the sentence fails.
  - Proposal `M3-B6` (reply lines 52–54), would change L119:

````
and an edit at which the two relations, compared under that same footprint bijection, stay equal does not separate the components.
````

  - Quotations: “an edit under which the two relations stay equal” — found at L119.
- **Mimo** (reply lines 50–55; challenges): The counterexample tells against the sentence's wording, not against the formal claim or (K): under "equal under the bijection that witnesses ~_C" the clause follows from the definition; under "some bijection" or "each relation as at the baseline" it fails; proposes replacing the clause in L119 (also removes U4's reading).
  - Proposal `M3-B6` (reply lines 52–54; printed in full under FC05 above), would change L119.
  - Quotations: “equal under the footprint bijection that witnesses ~_C” — not found in the text; not in the brief; “equal under some bijection” — not found in the text; not in the brief; “each relation stays as at the baseline” — not found in the text; not in the brief.
- **Mimo** (reply line 102; does not challenge): No attack to add: both parts follow from the definition under reading (i).
- **GLM** (reply line 21; challenges): The formal statement uses one bijection throughout (I93 (i)) and holds, by construction; the counterexample is to reading (ii) only; the claim should stand, with the sentence reworded.
  - Proposal `G3-B6` (reply lines 76–78), would change L119:

````
and an edit under which the two signatures still coincide under a bijection that witnesses the two components being of one kind on C does not separate them.
````

- **GLM** (reply line 38; challenges): Not a counterexample to the text nor to FC05 as formalized, but to I93's reading (ii) (worked by hand: the swap of p0 and p1 witnesses the kind at the baseline but not at (e1,b0)); under reading (i) the sentence holds unconditionally, and under U4's reading it holds on contracts as L141 defines them; the sentence either holds and adds nothing to D4.2 or fails; the change is to say which (under I93).
  - Proposal `G3-B6` (reply lines 76–78; printed in full under FC05 above), would change L119.
  - Proposal `G3-B7` (reply lines 81–83), would change L119:

````
and an edit that leaves each of the two relations as it was at the baseline does not separate the components.
````

  - Quotations: “stay equal” — found at L119.
- **GLM** (reply line 94; does not challenge): FC05 (i) holds unconditionally: D4.1 defines the signature from the relations alone; every sub-result is a consequence of the definitions except reading (ii), which fails.
- **Goes to a checker** (rule 5): challenged by GLM and Mimo; one of the twelve counterexamples the second check reproduced (FC05). Lines at stake: L119.

#### FC15 · claim · τ[C] is a contract of the candidate's organization

Lines it formalizes or quotes (from the brief): L141, L242, L554.

- **Mimo** (reply line 44; challenges): The formal statement hedges and silently takes σ(b0) to be E's baseline, which the words do not; relies on L141, L242 and the definition of an account, not given here (attacked in (d)).
  - Quotations: “as far as a contract is a set of pairs holding the baseline” — not found in the text; found in the brief.
- **Mimo** (reply line 85; challenges): Hand counterexample: with σ(b0) = b1 not E's baseline, τ[C] = {(1,b1)} holds no baseline of E and is not a contract in L141's sense; with partial τ, σ (I17) a pair of C left untranslated makes (F1) on C ill-formed; rests on I12, I17 and the words' silence; the reader says it is removed by "the L554 proposal in (a)", which the reply does not contain.
- **GLM** (reply line 23; challenges): The formal statement formalizes only one clause of L141; whether τ[C] is a contract of E in L141's full sense is not settled by what the reader can read (relies on L141 beyond the fragment given); the statement needs t to translate every pair of C (I17) and σ(b0) to exist; the maths should stand as a partial check, and L554's "has a signature on τ[C]" is the right commitment.
  - Quotations: “it contains the baseline (1,b0)” — found at L141; “as far as a contract is a set of pairs holding the baseline” — not found in the text; found in the brief; “it contains” — found at L141; “τ, σ map into A_E, B_E” — not found in the text; found in the brief; “has a signature on τ[C]” — found at L554.
- **GLM** (reply lines 96–108; challenges): Hand counterexample to the sentence "τ[C] is a contract of E", conditional on L141 requiring closure under composition (the reader relies on L141 beyond the fragment given; L141 as it stands reads "…the set of admitted edit–boundary pairs the claim ranges over; it contains the baseline (1,b0)" and names no closure condition): τ[C] lacks a composite pair; tells against FC15's formalization being the whole of the sentence, not against the text; the claim's premise should be strengthened to "t translates every pair of C" (the model is given in a fence at reply lines 98–107; it is a model, not a proposal).
  - Quotations: “τ[C] is a contract of E” — not found in the text; found in the brief; “it contains the baseline (1,b0)” — found at L141; “t translates every pair of C” — not found in the text; not in the brief.
- **Goes to a checker** (rule 5): challenged by GLM and Mimo. Lines at stake: L554.

#### FC16 · claim · Reading a candidate's components through the transport agrees with (K) on τ[C]

Lines it formalizes or quotes (from the brief): L119.

- **Mimo** (reply line 46; does not challenge): Named among the items with nothing to add in (a).
  - Quotations: “descriptions of patterns in (K)” — found at L127.
- **Mimo** (reply line 87; does not challenge): Under the set-of-triples comparison (I12 (c)) the two writings come apart when τ × σ collapses pairs (hand model); L556's "equates the third coordinates pointwise" is the reason for the pointwise reading, so the attack fails against the text; the maths stands.
  - Quotations: “equates the third coordinates pointwise” — found at L556.
- **GLM** (reply line 25; does not challenge): Says what the sentence says and holds by construction (re-status).
- **GLM** (reply line 92; does not challenge): Tried and found nothing; re-status "holds by construction".
  - Quotations: “holds on all models tried” — not found in the text; found in the brief.
- **Goes to no checker**: no point challenges it and it is not one of the twelve; recorded under rule 7 below.

#### FC17 · claim · Argument 1: (F1) makes each commitment's signature its counterpart's

Lines it formalizes or quotes (from the brief): L245, L554, L556.

- **Mimo** (reply lines 33–38; challenges): FC17's formal statement is (F1) read pointwise (L556); "up to the port translation" is D4.4's carrying, not a further weakening; L245 should say "active component" (proposal under D5.4); the quantifier question is FC18's.
  - Proposal `M3-B5` (reply lines 35–37; printed in full under D5.4 above), would change L245.
  - Quotations: “no active component k of E” — found at L554; “no component of E” — found at L245; “up to the port translation” — found at L119, L554; “each component” — found at L91, L119, L189, L281 and 1 more lines.
- **Mimo** (reply line 89; does not challenge): No counterexample under D4.4; the only bite is the quantifier question (FC18's second attack).
- **GLM** (reply lines 27–32; challenges): Holds by construction; says what L554 says given I12–I15; L245 says "no component of E whose signature on C differs", but a component of E has no signature on C, D's contract; L554's phrase is "on τ[C]"; proposes replacing "on C" by "on τ[C]" in L245.
  - Proposal `G3-B1` (reply lines 29–31), would change L245:

````
By (K), no component of E whose signature on τ[C] differs from its counterpart's meets (F1)
````

  - Quotations: “no component of E whose signature on C differs from its counterpart's meets (F1)” — found at L245; “on τ[C]” — found at L554.
- **GLM** (reply line 92; does not challenge): Tried and found nothing; re-status "holds by construction".
  - Quotations: “holds on all models tried” — not found in the text; found in the brief.
- **GLM** (reply line 110; challenges): L245's "on C" for a component of E is a wording fault the formal claim does not inherit (fixed in (a)).
  - Proposal `G3-B1` (reply lines 29–31; printed in full under FC17 above), would change L245.
- **Goes to a checker** (rule 5): challenged by GLM and Mimo. Lines at stake: L245.

#### FC18 · claim · Argument 1's Consequence: a same-kind condition adds nothing; no third case

Lines it formalizes or quotes (from the brief): L281, L558.

- **Mimo** (reply line 40; challenges): The formal statement's SameKind runs over k ∈ Γ with the counterpart carried to V_k, while L558 says "each component's counterpart must be a component of the same kind", both wider; both widenings can add a case (attacks in (d)); the words should follow L554 and the composite-component reading; L281's "There is no third case" is not formalized or searched here.
  - Proposal `M3-B8` (reply lines 97–99), would change L558:

````
A condition "each active component's counterpart must be a component of the same kind" adds nothing to (F1) on any contract.
````

  - Quotations: “each component's counterpart must be a component of the same kind” — found at L558; “each component” — found at L91, L119, L189, L281 and 1 more lines; “a component” — found at L11, L119, L127, L255 and 4 more lines; “There is no third case” — found at L281.
- **Mimo** (reply line 57; challenges **OWNER QUESTION**): The counterexample rests on I94, I10 (equal domains) and I14 (value maps) and fails wherever domains agree; it tells against the wording of L119 and the untranslated reading, not against what L233 gives; the D4.4 proposal removes it; if the owner rules that a footprint bijection may recode values (I10 (a)) it also disappears; the two hand attacks in (d) are not removed by that change.
  - Proposal `M3-B2` (reply lines 14–16; printed in full under D4.4 above), would change L119.
- **Mimo** (reply lines 91–100; challenges): Two attacks beyond the models tried: (i) a counterpart that is a two-component subnetwork is not "a component" of D, so the condition fails while (F1) holds (rests on I13; removed by the L556 proposal); (ii) a background component k1 ∉ Γ whose counterpart's projected relation differs: (F1) over Γ holds while the condition over all components fails (rests on I15 and L558's "each component"); proposes a new L558 sentence (or, if the definition of an account imposes (F1) on every component, the other direction: drop L554's "active", keep L245).
  - Proposal `M3-B7` (reply lines 69–71), would change L556:

````
By (K), reading \(\lambda(k)\) as one composite component whose relation is \(\operatorname{proj}^{\lambda}_{V_k}\operatorname{Sol}_{\lambda(k)}\), \(\operatorname{sig}_C(\lambda(k))=\{(a,b,\operatorname{proj}^{\lambda}_{V_k}\operatorname{Sol}_{\lambda(k)}(a,b))\}\)
````

  - Proposal `M3-B8` (reply lines 97–99; printed in full under FC18 above), would change L558.
  - Quotations: “a component” — found at L11, L119, L127, L255 and 4 more lines; “each component” — found at L91, L119, L189, L281 and 1 more lines; “active” — found at L119, L231, L233, L257 and 11 more lines.
- **GLM** (reply line 34; does not challenge): Faithful under D4.4's reading, and by construction; the counterexample is to I94's untranslated reading only.
- **GLM** (reply line 40; does not challenge): Not a counterexample to the text: it rests on I94 with I10's equal domains; L119's "up to the port translation" settles against the untranslated reading; no change to the text; the register should record that L119 settles I94.
  - Quotations: “read on C directly with its hidden ports projected away, **up to the port translation**” — found at L119; “up to the port translation” — found at L119, L554.
- **GLM** (reply line 92; does not challenge): Under D4.4's reading: tried and found nothing; re-status "holds by construction".
  - Quotations: “holds on all models tried” — not found in the text; found in the brief.
- **GLM** (reply line 112; does not challenge): Tried the empty subnetwork and non-injective κ: no counterexample; the only pressure point was I94, which the text settles.
- **Goes to a checker** (rule 5): challenged by Mimo; one of the twelve counterexamples the second check reproduced (FC18). Lines at stake: L119, L556, L558.
- Marks: OWNER QUESTION points present.

#### I10 · invention · Kinds: a footprint bijection between equal value domains, relations compared as sets

Lines it formalizes or quotes (from the brief): L119.

- **Mimo** (reply line 61; challenges **OWNER QUESTION**): Settled in one respect: "A kind is an equivalence class" rules out I10 (b); not settled: equal domains against a value bijection, which the reader leaves open as the owner's reserved question ("where values are placed", read as port values); the coordinate renaming is what "coincide" needs; no change.
  - Quotations: “A kind is an equivalence class” — found at L119; “coincide” — found at L119, L562, L564.
- **GLM** (reply lines 44–49; challenges): Not settled: "a bijection of their footprints" does not say whether ports must carry the same values or values may be recoded; the text should say which; proposes writing I10's main choice into the first sentence of L119 (nothing in the owner's decisions points either way; the searches used the main choice).
  - Proposal `G3-B2` (reply lines 46–48; printed in full under D4.2 above), would change L119.
  - Quotations: “A bijection of their footprints” — found at L119; “coincide” — found at L119, L562, L564.
- **Goes to a checker** (rule 5): challenged by GLM and Mimo. Lines at stake: L119.
- Marks: OWNER QUESTION points present.

#### I11 · invention · 'Coarser' and 'finer' contracts: fewer and more pairs

Lines it formalizes or quotes (from the brief): L119, L317.

- **Mimo** (reply line 63; challenges): Settled: L317's "a finer contract that contains a change" and L119's "a coarser contract identifies more components" give the subset reading, not the quotient alternative; no change.
  - Quotations: “a finer contract that contains a change” — found at L317; “a coarser contract identifies more components” — found at L119.
- **GLM** (reply lines 51–56; challenges): Not settled: "a coarser contract identifies more components" is substantive under the subset reading and tautological under the distinguishable-pairs reading; proposes writing the subset reading into L119 (names I11).
  - Proposal `G3-B3` (reply lines 53–55), would change L119:

````
Kinds are therefore relative to the contract: a contract is coarser than another when, at the same baseline, it holds a subset of the other's pairs, and a coarser contract identifies more components, while two components of one kind on C may separate on a finer contract.
````

  - Quotations: “A coarser contract identifies more components” — found at L119.
- **Goes to a checker** (rule 5): challenged by GLM and Mimo. Lines at stake: L119.

#### I12 · invention · Reading a candidate's component on C through the transport; τ[C]

Lines it formalizes or quotes (from the brief): L119, L554.

- **Mimo** (reply line 65; challenges): Not settled (τ named alone; τ[C] unwritten); written in by the proposals in (a) (the L119 proposal under D4.3; the reply names a second, L554 proposal that it does not contain).
  - Proposal `M3-B1` (reply lines 7–9; printed in full under D4.3 above), would change L119.
- **GLM** (reply lines 58–68; challenges): Not settled, and "τ[C]" is loose (τ maps edits, C is a set of pairs); proposes naming the boundary translation in L119 and defining τ[C] in L554 (both name I12).
  - Proposal `G3-B4` (reply lines 60–62; printed in full under D4.3 above), would change L119.
  - Proposal `G3-B5` (reply lines 65–67), would change L554:

````
has a signature on τ[C] = {(τ(a), σ(b)) : (a,b) ∈ C}
````

  - Quotations: “has a signature on τ[C]” — found at L554.
- **Goes to a checker** (rule 5): challenged by GLM and Mimo. Lines at stake: L119, L554.

#### I13 · invention · (K) extended from components to subnetworks

Lines it formalizes or quotes (from the brief): L556.

- **Mimo** (reply lines 67–71; challenges): Not settled: (K) is stated for a component (L116) and L556 says "By (K)" of a subnetwork; proposes replacing the fragment of L556 (writes I13 (a) in).
  - Proposal `M3-B7` (reply lines 69–71; printed in full under FC18 above), would change L556.
- **GLM** (reply line 70; challenges): Not settled: "By (K)" where (K) does not reach; matter 1's wording.
  - Proposal `G3-B9` (reply lines 118–120; printed in full under D4.4 above), would change L556.
- **Goes to a checker** (rule 5): challenged by GLM and Mimo. Lines at stake: L556.

#### I14 · invention · Subnetworks, their solutions, and port translations with value maps

Lines it formalizes or quotes (from the brief): L189, L233.

- **Mimo** (reply line 73; challenges): Partly settled: L233's "imposing the constraints of λ(k)" gives the subnetwork's own constraints and "projecting away its hidden ports" gives the hidden ports; written in by the L233 proposal; not settled: value maps κ and whether several ports of D may be carried into one of E (I14 (b)); both stay open.
  - Proposal `M3-B4` (reply lines 28–30; printed in full under D5.2 above), would change L233.
  - Quotations: “imposing the constraints of λ(k)” — found at L233; “projecting away its hidden ports” — found at L233.
- **GLM** (reply line 72; challenges): Partly settled: L233's "imposing the constraints of λ(k), projecting away its hidden ports" settles alternative (a) against, and "carrying what remains to V_k" settles that a carrying of values exists; whether value maps may collapse values should stay open (a substantive question about accounts); no wording.
  - Quotations: “imposing the constraints of λ(k), projecting away its hidden ports” — found at L233; “carrying what remains to V_k by the port translation” — found at L233.
- **Goes to a checker** (rule 5): challenged by GLM and Mimo. Lines at stake: L233.

#### I93 · invention · 'The two relations stay equal': under which footprint bijection

Lines it formalizes or quotes (from the brief): L119.

- **Mimo** (reply line 75; challenges): Not settled (three readings, with U4); written in by the FC05 proposal.
  - Proposal `M3-B6` (reply lines 52–54; printed in full under FC05 above), would change L119.
- **GLM** (reply lines 74–84; challenges): Not settled; reading (ii) fails (FC05), reading (i) holds but restates D4.2, U4's holds given L141; proposes reading (i) made explicit in L119, and U4's wording as the alternative "if the owner wants the sentence to say something with content".
  - Proposal `G3-B6` (reply lines 76–78; printed in full under FC05 above), would change L119.
  - Proposal `G3-B7` (reply lines 81–83; printed in full under FC05 above), would change L119.
- **Goes to a checker** (rule 5): challenged by GLM and Mimo. Lines at stake: L119.

#### I94 · invention · The counterpart's signature 'read on C directly … up to the port translation': untranslated

Lines it formalizes or quotes (from the brief): L119.

- **Mimo** (reply line 77; challenges): Not settled as written; written in by the D4.4 proposal.
  - Proposal `M3-B2` (reply lines 14–16; printed in full under D4.4 above), would change L119.
- **GLM** (reply line 86; challenges): Settled by the text: "up to the port translation" (L119) carries the counterpart to V_k, which is D4.4; the untranslated reading should be marked in the register as a stress test of I10, not a reading of the text.
  - Quotations: “up to the port translation” — found at L119, L554.
- **Goes to a checker** (rule 5): challenged by GLM and Mimo. Lines at stake: L119.

#### U4 · U-entry · A third reading of 'the two relations stay equal' (L119)

Lines it formalizes or quotes (from the brief): L119.

- **Mimo** (reply line 79; challenges): The third reading held wherever (1,b) ∈ C and failed in 82 of 1,752 models otherwise; not settled; blocked by the FC05 proposal.
  - Proposal `M3-B6` (reply lines 52–54; printed in full under FC05 above), would change L119.
  - Quotations: “stay equal” — found at L119.
- **GLM** (reply line 88; challenges): See I93; every failure had (1,b) ∉ C, and L141 puts the baseline in a contract, so the reading holds on contracts as the text defines them; record it as a reading the text permits, with that dependence named (the alternative wording printed under I93).
  - Proposal `G3-B7` (reply lines 81–83; printed in full under FC05 above), would change L119.
  - Quotations: “it contains the baseline (1,b0)” — found at L141.
- **Goes to a checker** (rule 5): challenged by GLM and Mimo. Lines at stake: L119.

#### matter 1 · round-1 matter · (K) applied beyond components of D. Argument 1 reads (K) on τ[C], a set of E's pairs, and whether τ[C] is a contract of E in L141's sense is a question for L554–L556 and L119. L556 writes "By (K)" of a subnetwork λ(k), while (K) is stated for a component. The bridge is supplied at L119 and L233.

Lines it formalizes or quotes (from the brief): L119, L141, L233, L554, L556.

- **Mimo** (reply line 106; challenges): (K) is stated at L116 for a component of one organization; Argument 1 uses it on τ[C] (L554–L556) and on the subnetwork λ(k) (L556); the text needs "the L554 proposal" (τ[C] a contract of E with baseline σ(b0), which the reply does not contain) and the L556 proposal; then L116 and (K) need no change.
  - Proposal `M3-B7` (reply lines 69–71; printed in full under FC18 above), would change L554, L556.
  - Quotations: “on τ[C]” — found at L554.
- **GLM** (reply lines 116–121; challenges): The text needs a change: L556's "By (K)" invokes (K) where it does not apply (λ(k) is a subnetwork); proposes writing I13's choice (a) into L556 rather than widening (K), since it changes one sentence and keeps L119 and L233 as the bridge.
  - Proposal `G3-B9` (reply lines 118–120; printed in full under D4.4 above), would change L556.
- **Goes to a checker** (rule 5): challenged by GLM and Mimo. Lines at stake: L554, L556.

#### Part 3: items no point addresses

Items of this part on which neither reader made any point (both replies read whole): I81. Each is recorded under rule 7 in section 6 unless a point on it in another part sends it to a checker.

### Part 4: Questions and contracts

Brief: `tests/S104 Round 2 - the maths against the words - part 04, Questions and contracts.md`. Replies: `s104_maths_mimo_4.response.txt` (Mimo), `s104_maths_glm_4.response.txt` (GLM).

#### D3.1 · definition · Question

Lines it formalizes or quotes (from the brief): L138, L141, L147.

- **Mimo** (reply line 3; challenges): The maths adds δ_D to the six items; the words stand, since L141 makes Q an operation on D; a designation is needed only where Q is read at another organization ((A), L250); no change at L138; the cross-application is a separate sentence (under I20).
  - Proposal `M4-B7` (reply lines 77–79), would change L253:

````
> L253 | The query \(\mathcal Q\) is held fixed; an account of a different query is not an account of this one. Where \(\mathcal Q\) is applied to another organization, the ports and components it reads there are named with the transport, and the answer is \(\mathcal Q\) read at those names.
````

- **GLM** (reply line 5; challenges): The maths adds δ_D; L141's "on D, its solutions and its component structure" cannot be written without naming what Q reads, which the text does not say; so the text's tuple is not yet a usable question; the words should change (under I20).
  - Proposal `G4-B2` (reply lines 43–46), would change L138:

````
p=(D,\ C,\ b_0,\ \mathcal Q,\ \delta_D,\ O_p,\ \rho_p), where \(\delta_D\) names
the ports and components \(\mathcal Q\) reads in \(D\).
````

  - Proposal `G4-B3` (reply lines 49–53), would change L253:

````
Applied to a candidate's organization, the query reads the ports and
components the transport names as counterparts of those \(\delta_D\) names
in the target; the query itself is unchanged.
````

  - Quotations: “on D, its solutions and its component structure” — found at L141.
- **Goes to a checker** (rule 5): challenged by GLM and Mimo. Lines at stake: L138, L253.

#### D3.2 · definition · Query and answers

Lines it formalizes or quotes (from the brief): L144, L253.

- **Mimo** (reply lines 5–11; challenges): Two partings: the maths adds ⊥ to the codomain because answers can fail to be fixed, and the words should change (the text speaks of an answer being determined at L255; the reader relies on the rest of that line); and Q read at another organization is not said (I20); proposes a new L141 (writes I21 in).
  - Proposal `M4-B1` (reply lines 8–10), would change L141:

````
> L141 | The **contract** \(C\subseteq A\times B\) is the set of admitted edit–boundary pairs the claim ranges over; it contains the baseline \((1,b_0)\). \(\mathcal Q\) is a specified set-theoretic operation on \(D\), its solutions and its component structure, with codomain \(Y_p\); where the operation fixes no value at some pair of \(C\), the answer there is undetermined.
````

- **GLM** (reply line 7; challenges): Q read at another organization through a designation is the gap the Vague note names; L253's "held fixed" gestures at it; the maths should stand and the words carry it (I20); ⊥ goes beyond the codomain Y_p (I21).
  - Proposal `G4-B3` (reply lines 49–53; printed in full under D3.1 above), would change L253.
  - Quotations: “held fixed” — found at L253, L343.
- **Goes to a checker** (rule 5): challenged by GLM and Mimo. Lines at stake: L141, L253.

#### D3.3 · definition · Respects

Lines it formalizes or quotes (from the brief): L151.

- **Mimo** (reply lines 13–21; challenges): Three partings: (i) the maths' upstream chain as printed is no chain (every port in some component is upstream of every port), and the reader gives the corrected chain, which the words should carry unless the organization sections already fix "upstream"; (ii) the maths sets Q = Q_w exactly where the words say Q "reads an output port" (words stand); (iii) "returns reachable or unreachable" is what the query returns, not its codomain (words stand); proposes a new first sentence of L151.
  - Proposal `M4-B2` (reply lines 17–19), would change L151:

````
> L151 | A production question has a \(\mathcal Q\) that reads an output port \(w\) and a \(C\) containing interventions on ports upstream of \(w\), where \(v\) is upstream of \(w\) when components \(j_1,\ldots,j_n\) chain from \(v\) to \(w\): \(v\) enters \(j_1\), each \(j_i\) for \(i<n\) outputs a value that enters \(j_{i+1}\), and \(w\) is the output of \(j_n\).
````

  - Quotations: “upstream” — found at L151, L271; “has a Q that reads an output port” — found at L151; “returns reachable or unreachable” — found at L151.
- **Mimo** (reply line 101; challenges): Hand counter-model to the respect as printed: with the chain as printed, a port feeding a component that writes a third port counts as upstream of w; under the corrected chain it does not.
  - Proposal `M4-B2` (reply lines 17–19; printed in full under D3.3 above), would change L151.
- **GLM** (reply lines 9–15; challenges): The text's three sentences read as necessary conditions, the maths makes them sufficient; with "fixed by … not by a label" the respect is read off (Q, C) both ways, which I72's sufficient-only reading under-writes; the words stand; overlap of respects is consistent with the words and should be said; proposes a new sentence after L151.
  - Proposal `G4-B1` (reply lines 11–14), would change L151:

````
A question may meet the shapes of more than one respect, and then asks
more than one thing at once.
````

  - Quotations: “A production question **has** a Q that…” — found at L151; “fixed by the type of Q and the shape of C, not by a label” — found at L151; “fixed by … not by a label” — found at L151.
- **Goes to a checker** (rule 5): challenged by GLM and Mimo. Lines at stake: L151.

#### D3.4 · definition · Provenance of a contract

Lines it formalizes or quotes (from the brief): L155.

- **Mimo** (reply line 23; does not challenge): The words stand and the maths reads them so; "found" is tied to the contract, not to Q, and "requires" is only a requirement.
  - Quotations: “requires” — found at L47, L155, L223, L407 and 6 more lines.
- **GLM** (reply line 17; does not challenge): Says what L155 says.
- **GLM** (reply line 148; does not challenge): Named among the items with nothing to add (with FC35 beyond (e), I85, I101).
- **Goes to no checker**: no point challenges it and it is not one of the twelve; recorded under rule 7 below.

#### D3.5 · definition · Scope statement

Lines it formalizes or quotes (from the brief): L159, L257.

- **Mimo** (reply lines 25–31; challenges): L141 writes C as edit–boundary pairs, L257 as "edits"; the pair reading (I27's) stands; "the edits the target admits" is not defined in these lines; proposes a new L257 (settles I27); L159's "why" is a declared input.
  - Proposal `M4-B3` (reply lines 28–30), would change L257:

````
> L257 | The contract \(C\) is a stated subset of the edit–boundary pairs the target admits, and every pair the target admits that is excluded from \(C\) is excluded by a stated scope, not silently. The pairs the target admits are all \((a,b)\) of its edits and boundaries.
````

  - Quotations: “the edits the target admits” — found at L257, L343.
- **GLM** (reply line 19; challenges): L257 says "a stated subset of the edits" while L141 defines C as pairs: the text contradicts itself; the maths follows L141 (wording under I27).
  - Proposal `G4-B4` (reply lines 59–63), would change L257:

````
The contract \(C\) is a stated subset of the admitted edit–boundary pairs,
and every admitted pair excluded from \(C\) is excluded by a stated scope,
not silently.
````

  - Quotations: “a stated subset of the edits” — found at L257.
- **External reader and case card:** E13 (the external reader) challenges the sentence this item formalizes (section 3 below).
- **Goes to a checker** (rule 5): challenged by GLM and Mimo; challenged by E13 (the external reader). Lines at stake: L257.

#### D3.6 · definition · Defects; indexing

Lines it formalizes or quotes (from the brief): L161, L367.

- **Mimo** (reply lines 33–39; challenges): "Alleged target" carries a description whose source is not said; the words should carry the three senses (I76); the maths' second clause of BadBaseline (b0 ∉ B) cannot occur, since L141 forces (1,b0) ∈ C ⊆ A × B, and should come out; the words stand against the maths where it adds that no account follows (FC106); proposes a new first sentence of L161 (writes I76 in).
  - Proposal `M4-B4` (reply lines 36–38), would change L161:

````
> L161 | A question may fail to pick out its alleged target, assume an incompatible baseline, or combine incompatible requirements. The alleged target is the one a description names; the question fails to pick it out where no organization answers to that description or more than one does. The baseline is incompatible where the target has no solutions at it. The requirements are incompatible where the description puts conditions on the contract and the query that no pair of contract and query meets.
````

  - Quotations: “alleged target” — found at L161; “\(b_0\notin B\)” — not found in the text; found in the brief.
- **GLM** (reply line 21; challenges): The three defects are written only by adding a description (I76); "its alleged target" presupposes one; the indexing matches L367 except δ_D (wording under I76).
  - Proposal `G4-B7` (reply lines 91–98), would change L161:

````
A question may fail to pick out its alleged target, assume an incompatible
baseline, or combine incompatible requirements. The alleged target and the
requirements are stated with the question: it fails to pick the target out
when no organization meets the statement or several do, and combines
incompatible requirements when the statement's conditions on the contract
and query have no joint instance.
````

  - Quotations: “Fails to pick out its alleged target” — not found in the text; found in the brief; “its alleged target” — found at L161.
- **Goes to a checker** (rule 5): challenged by GLM and Mimo. Lines at stake: L161.

#### D3.7 · definition · Different questions

Lines it formalizes or quotes (from the brief): L151.

- **Mimo** (reply lines 41–46; challenges): On the answer-profile reading L151's sentence stands; on the reading that no candidate can account for two questions at once it does not; the narrow reading is what the words can carry; proposes "not by itself" in L151's second sentence (writes I73's narrow reading in).
  - Proposal `M4-B5` (reply lines 44–46), would change L151:

````
> L151 | Two questions with the same \(D\) and different \((C,\mathcal Q)\) are different questions, and an answer to one is not by itself an answer to the other.
````

- **GLM** (reply line 23; challenges): The narrow/wide fork is the ambiguity of "an answer to one is not an answer to the other" (FC34, I73).
  - Proposal `G4-B6` (reply lines 80–85), would change L151:

````
Two questions with the same \(D\) and different \((C,\mathcal Q)\) are different
questions; an account of one is an account of the other only if it meets
the account conditions on that other question, and answers shared on
shared pairs do not make the questions one.
````

  - Quotations: “an answer to one is not an answer to the other” — found at L151.
- **Goes to a checker** (rule 5): challenged by GLM and Mimo. Lines at stake: L151.

#### FC34 · claim · Two questions, one target: what 'an answer to one is not an answer to the other' allows

Lines it formalizes or quotes (from the brief): L151.

- **Mimo** (reply lines 41–46; challenges): As for D3.7: the sentence stands on the answer-profile reading and fails on the wide reading; proposes the narrow reading in L151 (printed under D3.7).
  - Proposal `M4-B5` (reply lines 44–46; printed in full under D3.7 above), would change L151.
- **Mimo** (reply lines 66–68; challenges): The witness is a counterexample to I73's wide reading and tells against the text only as far as the wording carries that reading; the "not by itself" change removes it; the reported models are copies of the target (U6), but the mechanism survives without a copy: a hand model (y = x with x carried at b1, E with y = 1) meets (E) on C and fails NC1 on C′ (rests on I83, I21, I79).
  - Proposal `M4-B5` (reply lines 44–46; printed in full under D3.7 above), would change L151.
  - Quotations: “not by itself” — found at L159, L315, L409.
- **Mimo** (reply line 70; does not challenge): The monotonicity and NC1-on-C′ results are witnesses of properties of (E), not counterexamples; L367 and the frozen-contract sentence already keep the contract inside the claim; no change.
- **Mimo** (reply line 105; does not challenge): The narrow reading needs one failure, and the non-copy model is one; nothing breaks it; the witness families rest on I83, and the other reading gives another witness.
- **GLM** (reply line 25; does not challenge): Testing both readings is the right treatment of an ambiguous sentence; the monotonicity clauses are context, harmless; the results stand as witnesses.
- **GLM** (reply line 37; challenges): FC34's witness against the wide reading rests on inventions (I21, I24/I83, I85): a copy of the target escaping NC1 through one undetermined pair; under I83's other choice another witness was found; it tells against the text only if the text means the wide reading, which it does not say; the changes that remove it are the I73 and U6 proposals.
  - Proposal `G4-B6` (reply lines 80–85; printed in full under D3.7 above), would change L151.
  - Proposal `G4-B8` (reply lines 110–115), would change L255:

````
The target's answer does not appear, at the declared grain, as an
unanalysed boundary input or as a component: a component that fixes the
answer wherever the answer is determined is that appearance, undetermined
pairs notwithstanding.
````

  - Quotations: “a candidate meeting (E) on two questions with one target” — not found in the text; not in the brief.
- **GLM** (reply line 142; does not challenge): The narrow reading is consistent; no attack beyond (b).
- **Goes to a checker** (rule 5): challenged by GLM and Mimo. Lines at stake: L151, L255.

#### FC35 · claim · 'Prediction' at L151 is outside L219's definition

Lines it formalizes or quotes (from the brief): L151, L217.

- **Mimo** (reply lines 109–114; challenges): Handled under matter 6 (the reply's FC35 entry points there).
  - Proposal `M4-B8` (reply lines 112–114), would change L151:

````
> L151 | A measure that identifies an outcome, together with a prediction of the outcome from it through a transport faithful on the contract to the simulation layer \(S\), answers the identification question
````

  - Quotations: “prediction” — found at L23, L151, L177, L215 and 4 more lines.
- **GLM** (reply line 27; challenges): Correctly diagnosed: L151 uses the defined term outside its definition, and I51 papers over the gap; a fault in the sentence (see matter 6).
  - Proposal `G4-B5` (reply lines 68–72), would change L151:

````
A measure that identifies an outcome, together with the outcome computed
from it through a transport faithful on the contract, answers the
identification question.
````

- **Goes to a checker** (rule 5): challenged by GLM and Mimo. Lines at stake: L151.

#### FC36 · claim · What a question asks is fixed by the query and the contract, not by a label

Lines it formalizes or quotes (from the brief): L151.

- **Mimo** (reply lines 48–54; challenges): The maths reads the three sentences as sufficient conditions, while "is fixed by the type of Q and the shape of C, not by a label" makes them the asks themselves (words stand); the sentence claims for five asks what the maths writes for three; purpose-achievement reads the aims (L147; (AR)); proposes a new last sentence of L151 (unnecessary if (AR) reads only Q and C).
  - Proposal `M4-B6` (reply lines 51–53), would change L151:

````
> L151 | What a question asks, production, identification, obstruction or rule-status, is fixed by the type of \(\mathcal Q\) and the shape of \(C\), not by a label; purpose-achievement is fixed by those and by the aims \(O_p\).
````

  - Quotations: “is fixed by the type of Q and the shape of C, not by a label” — found at L151.
- **Mimo** (reply line 101; challenges): FC36 still stands under the corrected chain; a second attack: two questions with the same type of Q and shape of C and different aims ask different things (purpose-achievement).
  - Proposal `M4-B6` (reply lines 51–53; printed in full under FC36 above), would change L151.
- **GLM** (reply line 29; challenges): The computation covers three respects only while the sentence claims five; the claim as computed is narrower than the sentence, and the sentence has a hand counterexample for purpose-achievement (in (d)).
  - Proposal `G4-B9` (reply lines 123–127), would change L151:

````
What a question asks, production, identification, obstruction, rule-status
or purpose-achievement, is fixed by the type of \(\mathcal Q\) and the shape of
\(C\), and for purpose-achievement by the aims \(O_p\), not by a label.
````

- **GLM** (reply lines 121–129; challenges): The attack succeeds for purpose-achievement: two questions with the same D, C, b0, Q and different aims O_p (L147) ask different things while (Q, C) is the same, so purpose-achievement is not fixed by Q and C; proposes a new "fixed by" sentence of L151; the rule-status half cannot be attacked here, and the renaming half holds by construction.
  - Proposal `G4-B9` (reply lines 123–127; printed in full under FC36 above), would change L151.
  - Quotations: “fixed by” — found at L127, L151, L277, L315 and 1 more lines; “computed: as claimed” — not found in the text; found in the brief; “holds by construction” — not found in the text; found in the brief.
- **Goes to a checker** (rule 5): challenged by GLM and Mimo. Lines at stake: L151.

#### FC106 · claim · A question's three defects, as far as they can be written

Lines it formalizes or quotes (from the brief): L161.

- **Mimo** (reply line 56; challenges): The formal statement says more than L161, which calls the question defective and no more; the added clause (no account follows) should come out of the claim's statement and stand as a conjecture of the encoding (attacked in (d)).
- **Mimo** (reply line 103; challenges): Hand model against "an incompatible baseline admits no account": a target with no solutions at the baseline and a candidate answering 0 there meet (E) where (F1) and (A) ask agreement only where the target's answer is determined (I21) and non-vacuity asks only the candidate's own; where (F2) is read into the target's relation the empty relation blocks it; the clause turns on readings L161 does not fix, and the sentence does not claim it.
- **GLM** (reply line 31; challenges): "Incompatible baseline" written as Sol_D(1,b0) = ∅ or b0 ∉ B is one reading; the baseline conflicting with the stated requirements is another; the words do not settle it (inside I76).
  - Quotations: “Incompatible baseline” — found at L161; “assume an incompatible baseline” — found at L161.
- **GLM** (reply line 131; challenges): Attack on the held part: the argument runs through non-vacuity (not given in this part); if it demands a determined answer off the baseline, an empty baseline no longer blocks an account; the claim is hostage to non-vacuity's content and should be re-searched (a two-pair contract, baseline undetermined, one intervention pair determined).
  - Quotations: “An incompatible baseline admits no account” — not found in the text; found in the brief.
- **Goes to a checker** (rule 5): challenged by GLM and Mimo. Lines at stake: L161.

#### FC107 · claim · Exposing a question's defect is another question

Lines it formalizes or quotes (from the brief): L161.

- **Mimo** (reply line 58; challenges): "Another question with its own contract" already gives p_δ ≠ p; the maths adds a target and a query of its own, which the words do not; the words stand.
  - Quotations: “another question with its own contract” — found at L161.
- **GLM** (reply line 33; challenges): Faithful, but it silently assumes that p_δ has a target, an organization, since (E) demands one; the text never says a question can be a target (see (d)).
  - Proposal `G4-B10` (reply lines 135–138), would change L161:

````
Exposing the defect is another question with its own target, contract and
query.
````

  - Quotations: “Exposing the defect is another question with its own contract” — found at L161.
- **GLM** (reply lines 133–140; challenges **OWNER QUESTION**): The definitional step holds only if p_δ has a target that is an organization; the text says nothing that makes a question or a defect an organization; not a counterexample, a gap; proposes a new last sentence of L161, if the owner means p_δ to be assessable; whether a question can serve as a target is "a decision for the owner".
  - Proposal `G4-B10` (reply lines 135–138; printed in full under FC107 above), would change L161.
  - Quotations: “Exposing the defect is another question with its own contract” — found at L161.
- **Goes to a checker** (rule 5): challenged by GLM and Mimo. Lines at stake: L161.
- Marks: OWNER QUESTION points present.

#### I20 · invention · How the fixed query is applied to a candidate's organization

Lines it formalizes or quotes (from the brief): L141, L253.

- **Mimo** (reply lines 74–79; challenges): Not settled; L151's "not by a label" fixes that what Q reads must travel with the organization it is read at; proposes a new L253 (writes I20 in).
  - Proposal `M4-B7` (reply lines 77–79; printed in full under D3.1 above), would change L253.
  - Quotations: “not by a label” — found at L151.
- **GLM** (reply lines 41–55; challenges): Not settled: L141 and L253 require Q to read E but never say how; proposes writing I20's default into the tuple (replacing L138) and a new sentence after L253.
  - Proposal `G4-B2` (reply lines 43–46; printed in full under D3.1 above), would change L138.
  - Proposal `G4-B3` (reply lines 49–53; printed in full under D3.1 above), would change L253.
- **Goes to a checker** (rule 5): challenged by GLM and Mimo. Lines at stake: L138, L253.

#### I27 · invention · The stated scope: a declared statement over pairs

Lines it formalizes or quotes (from the brief): L257.

- **Mimo** (reply line 81; challenges): Partly settled: L257 requires every excluded item to be covered by a stated scope; pairs against edits is the text's own inconsistency, which the L257 change settles along with what the target admits.
  - Proposal `M4-B3` (reply lines 28–30; printed in full under D3.5 above), would change L257.
- **GLM** (reply lines 57–64; challenges): Not settled; the text is self-contradictory (L141 pairs, L257 edits); follow L141; proposes a new L257.
  - Proposal `G4-B4` (reply lines 59–63; printed in full under D3.5 above), would change L257.
- **Goes to a checker** (rule 5): challenged by GLM and Mimo. Lines at stake: L257.

#### I51 · invention · 'Prediction' for a transport not said to reach the simulation layer

Lines it formalizes or quotes (from the brief): L151.

- **Mimo** (reply line 83; challenges): Not settled; the L151 change under matter 6 names the codomain and makes the invention unneeded; the alternative is to widen L219.
  - Proposal `M4-B8` (reply lines 112–114; printed in full under FC35 above), would change L151.
- **GLM** (reply lines 66–74; challenges): Not settled; either reword L151 (preferred, keeping "prediction" tied to the simulation layer, which L175–L177 make load-bearing) or extend L219; proposes the first, and gives the L219 alternative (which writes I51 in).
  - Proposal `G4-B5` (reply lines 68–72; printed in full under FC35 above), would change L151.
  - Inline proposal (reply line 74; written in the reader's running text, not in a fence), would change L219 — the reader's alternative, not the one it proposes:

````
Let \(t\) be a transport; the prediction of \(t\) at \((a,b)\) is \(\operatorname{Ans}_{\mathcal E}(\tau(a),\sigma(b))\), of which the prediction of L219 is the case \(t\) ends at \(S\).
````

  - Quotations: “prediction” — found at L23, L151, L177, L215 and 4 more lines; “Let \(t\) be a transport; the prediction of \(t\) at \((a,b)\) is \(\operatorname{Ans}_{\mathcal E}(\tau(a),\sigma(b))\), of which the prediction of L219 is …” — not found in the text; not in the brief.
- **Goes to a checker** (rule 5): challenged by GLM and Mimo. Lines at stake: L151, L219.

#### I72 · invention · Respects as sufficient conditions; 'upstream'

Lines it formalizes or quotes (from the brief): L151.

- **Mimo** (reply line 85; challenges): Settled against sufficiency by "fixed by the type of Q and the shape of C, not by a label"; not settled: "upstream" (wording under D3.3) and exclusivity of the asks, which should stay open (no line decides it; nothing in the owner's words asks for a ruling).
  - Proposal `M4-B2` (reply lines 17–19; printed in full under D3.3 above), would change L151.
  - Quotations: “fixed by the type of Q and the shape of C, not by a label” — found at L151.
- **GLM** (reply line 76; challenges): Partly settled: "fixed by … not by a label" settles both directions; exclusivity of the respects is not settled (proposal under D3.3); the register should note that the built reading is weaker than the sentence.
  - Proposal `G4-B1` (reply lines 11–14; printed in full under D3.3 above), would change L151.
  - Quotations: “fixed by the type of Q and the shape of C, not by a label” — found at L151.
- **Goes to a checker** (rule 5): challenged by GLM and Mimo. Lines at stake: L151.

#### I73 · invention · 'An answer to one is not an answer to the other': the narrow reading

Lines it formalizes or quotes (from the brief): L151.

- **Mimo** (reply line 87; challenges): Not settled; the L151 change writes the narrow reading in.
  - Proposal `M4-B5` (reply lines 44–46; printed in full under D3.7 above), would change L151.
- **GLM** (reply lines 78–87; challenges): Not settled; the wide reading fails under the inventions (FC34); state the narrow reading, which L367 and D3.6 already bear out; proposes a new last sentence of L151 (names I73).
  - Proposal `G4-B6` (reply lines 80–85; printed in full under D3.7 above), would change L151.
- **Goes to a checker** (rule 5): challenged by GLM and Mimo. Lines at stake: L151.

#### I76 · invention · The three defects of a question, formally

Lines it formalizes or quotes (from the brief): L161.

- **Mimo** (reply line 89; challenges): "Alleged target" fixes that a description is involved, not where it comes from or what the other two senses read; the L161 change writes the rest in.
  - Proposal `M4-B4` (reply lines 36–38; printed in full under D3.6 above), would change L161.
  - Quotations: “alleged target” — found at L161.
- **GLM** (reply lines 89–100; challenges): Partly settled: "its alleged target" presupposes a statement of the target, whose form the text never gives; proposes a new first sentence of L161 (names I76).
  - Proposal `G4-B7` (reply lines 91–98; printed in full under D3.6 above), would change L161.
  - Quotations: “its alleged target” — found at L161.
- **Goes to a checker** (rule 5): challenged by GLM and Mimo. Lines at stake: L161.

#### I79 · invention · Boundary inputs and exogenous values are carried by components

Lines it formalizes or quotes (from the brief): L255, L325.

- **Mimo** (reply line 91; challenges **OWNER QUESTION**): L255's "as an unanalysed boundary input or as a component" separates the two, so the words carry I79's other choice (boundary coordinates of their own); U6 records no status change either way; no change proposed, the reader saying "where values sit is the owner's question" (read as where coordinate values sit).
  - Quotations: “as an unanalysed boundary input or as a component” — found at L255.
- **GLM** (reply line 102; does not challenge): Not settled whether a boundary carries its own coordinates; should stay open for now (how information is carried into components, decisions S25–S26; the physical module not computed, I90); the dependence should be recorded: NC1's verdict on "unanalysed boundary input" changes with it, and claims resting on NC1 inherit I79.
  - Quotations: “unanalysed boundary input” — found at L255.
- **Goes to a checker** (rule 5): challenged by Mimo. Lines at stake: L255, L325.
- Marks: OWNER QUESTION points present.

#### I85 · invention · The default scope statement states every excluded pair

Lines it formalizes or quotes (from the brief): L257.

- **Mimo** (reply line 93; does not challenge): The requirement is the text's own (L257); the default is a program device; no change.
- **GLM** (reply line 104; does not challenge): Should stay an invention: a search default; writing it in would say every question states its full scope, which L159 does not mean.
- **Goes to no checker**: no point challenges it and it is not one of the twelve; recorded under rule 7 below.

#### I101 · invention · Which models count as witnesses: the proper-model filter

Lines it formalizes or quotes (from the brief): L91.

- **Mimo** (reply line 95; does not challenge): A device; L91 fixes only nonempty domains; universal searches carry no filter; no change.
- **GLM** (reply line 106; does not challenge): Should stay an invention: a degenerate witness is no witness, a degenerate counterexample is a counterexample; no change.
- **Goes to no checker**: no point challenges it and it is not one of the twelve; recorded under rule 7 below.

#### U6 · U-entry · Inventions acting inside every computation of (E) and (F2) are not carried to the results

Lines it formalizes or quotes (from the brief): L242, L255.

- **Mimo** (reply line 97; does not challenge): The register should carry I83 and I84 into every result they act in (a change to the maths' record); the self-account question should stay open until non-circular dependence's lines are read.
- **GLM** (reply lines 108–117; challenges): Register fix: I83 and I84 run inside every computation of (E), so FC34's "Rests on" should list them; text fix: whether a component that fixes the answer wherever it is determined counts as the answer appearing as a component should be said; proposes a new L255 sentence (adopts I83's other choice, and says so); with it the FC34 wide-reading witness falls.
  - Proposal `G4-B8` (reply lines 110–115; printed in full under FC34 above), would change L255.
  - Quotations: “Rests on” — not found in the text; found in the brief.
- **Goes to a checker** (rule 5): challenged by GLM. Lines at stake: L255.

#### NF08 · NF entry

Lines it formalizes or quotes (from the brief): L151.

- **Mimo:** no point on this item.
- **GLM** (reply line 146; does not challenge): NF08 stands: the candidate made of a measure and a prediction is not specified enough to check against (E); neither wording changes that; L151's sentence remains an illustration until its candidate's organization and transport are given.
  - Quotations: “the outcome computed from it through a transport faithful on the contract” — not found in the text; not in the brief; “a prediction of the outcome from it” — found at L151; “prediction” — found at L23, L151, L177, L215 and 4 more lines.
- **Goes to no checker**: no point challenges it and it is not one of the twelve; recorded under rule 7 below.

#### matter 6 · round-1 matter · L151's "prediction" is used of a transport not said to be to the simulation layer, while L219 defines the term for transports to S only.

Lines it formalizes or quotes (from the brief): L151, L219.

- **Mimo** (reply lines 109–114; challenges): L151 uses "prediction" of a transport with no codomain named, while L217–L219 define it for transports to S; the words should name the codomain, which removes I51 (alternative: widen L219); proposes a new measure sentence in L151.
  - Proposal `M4-B8` (reply lines 112–114; printed in full under FC35 above), would change L151.
  - Quotations: “prediction” — found at L23, L151, L177, L215 and 4 more lines.
- **GLM** (reply line 146; challenges **OWNER QUESTION**): The text needs a change: L219 should stay tied to the simulation layer and L151 should stop borrowing the term (wording under I51); if instead the owner wants "prediction" for any faithful transport, the L219 extension writes I51 in and should be marked so.
  - Proposal `G4-B5` (reply lines 68–72; printed in full under FC35 above), would change L151.
  - Quotations: “the outcome computed from it through a transport faithful on the contract” — not found in the text; not in the brief; “a prediction of the outcome from it” — found at L151; “prediction” — found at L23, L151, L177, L215 and 4 more lines.
- **Goes to a checker** (rule 5): challenged by GLM and Mimo. Lines at stake: L151.
- Marks: OWNER QUESTION points present.

#### Part 4: items no point addresses

Items of this part on which neither reader made any point (both replies read whole): D6.7, D12.6. Each is recorded under rule 7 in section 6 unless a point on it in another part sends it to a checker.

### Part 5: Transports, fidelity and the transport results

Brief: `tests/S104 Round 2 - the maths against the words - part 05, Transports, fidelity and the transport results.md`. Replies: `s104_maths_mimo_5.response.txt` (Mimo), `s104_maths_glm_5.response.txt` (GLM).

Mimo and GLM both propose a new L520 and a new L220, with different wordings; each is copied under the items that carry it.

#### D5.1 · definition · Transport

Lines it formalizes or quotes (from the brief): L186, L189.

- **Mimo** (reply line 3; challenges): Three things are added: π partial (I16), τ and σ partial (I17), a map on values for each named port (I14); the arrow settles that π is a function; "on the stated scope" names a domain without saying how far π is defined; "carrying" makes a map on values the natural reading but says nothing of what it may do to values; the shape of the maths stands and the words must carry the map and the scopes (wording at I16, L189).
  - Proposal `M5-B2` (reply lines 57–59), would change L189:

````
> L189 | where \(\pi:X_D\to X_E\) on the stated scope, \(\tau\) translates edits, \(\sigma\) translates boundaries, and \(\lambda\) assigns each component of \(E\) a subnetwork of \(D\) with a port translation: an injection of the ports of \(k\) into the ports of the subnetwork, values carried along each named port by a map of that port; \(\pi\) is defined at every valuation of every scope the transport translates and is not required elsewhere; \(\tau\) and \(\sigma\) may name only some edits and boundaries, and a pair is translated when they name its edit and boundary and \(\pi\) is defined on its solutions.
````

  - Quotations: “on the stated scope” — found at L189; “With a port translation” — found at L119, L189; “carrying what remains to \(V_k\) by the port translation of \(\lambda\)” — found at L233; “carrying” — found at L75, L169, L233, L313 and 1 more lines.
- **GLM** (reply lines 5–7; challenges): The words and the maths part twice: the total arrow with "on the stated scope" says two things, and the partial reading (I16) should stand (L315 translates pairs outside C; no total map need exist between arbitrary value spaces), so the arrow should change; and λ assigns a subnetwork to each component while (F1) binds only "every active component", undefined (I15); I16 and I17 make a small circle, so the text should define "translates" once and let π's scope follow it.
  - Proposal `G5-B3` (reply lines 37), would change L189:

````
> L189 | where \(\pi:X_D\rightharpoonup X_E\) is defined on the stated scope, at least on \(\operatorname{Sol}_D(a,b)\) at every admitted pair \((a,b)\) whose edit and boundary \(\tau\) and \(\sigma\) translate, \(\tau\) translates edits, \(\sigma\) translates boundaries, and \(\lambda\) assigns each component of \(E\) a subnetwork of \(D\) with a port translation.
````

  - Proposal `G5-B2` (reply lines 31), would change L231:

````
> L231 | An explanatory candidate for question \(p\) is an organization \(E\), a transport \(t=(\pi,\tau,\sigma,\lambda)\) from \(D\) to \(E\), and an identified set \(\Gamma\) of active commitments in \(E\). The commitments \(\Gamma\) are the active components of \(E\), the components the candidate offers as doing the work, whether or not anyone has described their work; the boundary conditions of \(E\) and the components of \(E\) outside \(\Gamma\), including any of them that assigns an input, belong to the named background of Part VI.
````

  - Proposal `G5-B4` (reply lines 41), would change L315:

````
> L315 | they conflict at some admitted edit–boundary pair \((a,b)\) of the target that both their transports translate — both \(\tau\)'s defined at \(a\), both \(\sigma\)'s at \(b\), both \(\pi\)'s on \(\operatorname{Sol}_D(a,b)\) — in \(C\) or outside it.
````

  - Quotations: “on the stated scope” — found at L189; “to each component of \(E\)” — not found in the text; not in the brief; “every active component” — found at L233; “translates” — found at L119, L189, L315.
- **Goes to a checker** (rule 5): challenged by GLM and Mimo. Lines at stake: L189, L231, L315.

#### D5.2 · definition · Projection

Lines it formalizes or quotes (from the brief): L233.

- **Mimo** (reply line 5; challenges): Given I14 the formula is the sentence read part by part; the maths silently fixes that the hidden ports are exactly the rest of the subnetwork's ports, which the L189 wording makes determined; the words stand.
  - Proposal `M5-B2` (reply lines 57–59; printed in full under D5.1 above), would change L189.
  - Quotations: “imposing the constraints of \(\lambda(k)\)” — found at L233; “projecting away its hidden ports” — found at L233; “carrying what remains” — found at L233.
- **GLM** (reply line 9; does not challenge): Says what the sentence says.
- **Goes to a checker** (rule 5): challenged by Mimo. Lines at stake: L189.

#### D5.3 · definition · Candidate

Lines it formalizes or quotes (from the brief): L231.

- **Mimo** (reply line 7; challenges): The tuple adds δ_E; without a designation Ans_E is undefined and (A) cannot be written; the maths must invent (I20); the words should carry it (wording at L231).
  - Proposal `M5-B3` (reply lines 63–65), would change L231:

````
> L231 | An explanatory candidate for question \(p\) is an organization \(E\), a transport \(t=(\pi,\tau,\sigma,\lambda)\) from \(D\) to \(E\), an identified set \(\Gamma\) of active commitments in \(E\), and a designation of the ports of \(E\) at which the query of \(p\) is read; the active components of \(E\) are the members of \(\Gamma\). The commitments \(\Gamma\) are components of \(E\), those the candidate offers as doing the work, whether or not anyone has described their work; the boundary conditions of \(E\) and the components of \(E\) outside \(\Gamma\), including any of them that assigns an input, belong to the named background of Part VI.
````

- **GLM** (reply line 9; challenges): Adds δ_E, which L231 does not mention (I20); the words should say where the candidate's designation comes from if they mean to fix it (the reader relies on L231 as quoted).
- **Goes to a checker** (rule 5): challenged by GLM and Mimo. Lines at stake: L231.

#### D5.4 · definition · (F1)

Lines it formalizes or quotes (from the brief): L236.

- **Mimo** (reply line 9; does not challenge): Given I14's Sol_N the formula is the sentence; the words stand.
- **GLM** (reply line 9; does not challenge): Says what the sentence says.
- **Goes to no checker**: no point challenges it and it is not one of the twelve; recorded under rule 7 below.

#### D5.5 · definition · (F2)

Lines it formalizes or quotes (from the brief): L242.

- **Mimo** (reply line 11; challenges): The valuation equation is the sentence; the range of the homomorphism clause (I18), a composite τ does not name (I84), and "(F2) at a pair" (needed by L220) are absent from the words; the maths' reading is the only one L220 can carry; the words should say so (wording at L242).
  - Proposal `M5-B4` (reply lines 69–71), would change L242:

````
> L242 | \pi[\operatorname{Sol}_D(a,b)]=\operatorname{Sol}_E(\tau(a),\sigma(b)),\qquad \tau(1)=1,\quad \tau(a_2a_1)=\tau(a_2)\tau(a_1)\ \text{for every pair of edits }\tau\text{ names, a composite it does not name failing here, and these two holding of }\tau\text{ as a whole}. \tag{F2}
````

  - Quotations: “F2 at a pair” — not found in the text; found in the brief.
- **GLM** (reply line 9; does not challenge): Says what the sentence says.
- **Goes to a checker** (rule 5): challenged by Mimo. Lines at stake: L242.

#### D5.6 · definition · (A)

Lines it formalizes or quotes (from the brief): L250.

- **Mimo** (reply line 13; challenges): The equation is the sentence; ⊥ = ⊥ and the treatment of ⊥ are added (I21, U1); wording at L250.
  - Proposal `M5-B5` (reply lines 75–77), would change L250:

````
> L250 | \operatorname{Ans}_E(\tau(a),\sigma(b))=\operatorname{Ans}_p(a,b),\ \bot=\bot,\ \text{and a map on values has }\bot\ \text{outside its domain}. \tag{A}
````

- **GLM** (reply line 9; does not challenge): Says what the sentence says.
- **Goes to a checker** (rule 5): challenged by Mimo. Lines at stake: L250.

#### D5.7 · definition · Faithful; two extents

Lines it formalizes or quotes (from the brief): L189, L245, L247, L520, L630.

- **Mimo** (reply line 15; challenges): I49 is a patch, not a reading the words force: L189 and L245 carry (F1) and (F2), L247's heading and L520 need (A) inside the word, L630 keeps them apart; one word cannot do all three; keep faithful = (F1) ∧ (F2) and name (A) question fidelity (wordings at L245 and L520).
  - Proposal `M5-B6` (reply lines 83–85), would change L245:

````
> L245 | (F1) prevents an assembled match from hiding a decomposition in error, so far as error is a projection that does not match; it does not name the right counterpart. (F2) prevents a set of pieces each faithful locally from hiding a lost shared constraint. Together (F1) and (F2) are fidelity; (A) is question fidelity, a further condition on the answers, which faithful (L189) does not include.
````

  - Proposal `M5-B11` (reply lines 115–117), would change L520:

````
> L520 | Everything else is defined in terms of the two imports, the structural vocabulary of (O) and (Q), the declared indices and the declared inputs (below). Roles, from admitted edits (Part II). Kinds, from signatures (K). The respect of a question, from its query (Part III). Representation, from fidelity and provenance (R). Provenance, from physical history (Parts IV, XII). Account, from fidelity and question fidelity under change, non-circular dependence and non-vacuity (E). Understanding, construction, newness, origin, repair, created explanation, capability, recursion, universality, from those.
````

  - Quotations: “faithful on \(C\)” — found at L41, L189, L205, L413; “Together they are fidelity” — found at L245; “the fidelity and the answers” — found at L630.
- **GLM** (reply line 11; challenges): The maths splits one word into two extents because the text does: L189 narrow, L247's heading calls (A) a fidelity, L520 must source (A), L630 keeps them apart, and L219–L220 pair a prediction with a violation in the wide extent; FC104's finding is right; the narrow extent should stand, with (A) named wherever it is meant (wordings under I49 and matter 12).
  - Proposal `G5-B6` (reply lines 73), would change L520:

````
> L520 | Everything else is defined in terms of the two imports, the structural vocabulary of (O) and (Q), the declared indices and the declared inputs (below). Roles, from admitted edits (Part II). Kinds, from signatures (K). The respect of a question, from its query (Part III). Representation, from fidelity and provenance (R). Provenance, from physical history (Parts IV, XII). Account, from fidelity, answer agreement, non-circular dependence and non-vacuity (E). Understanding, construction, newness, origin, repair, created explanation, capability, recursion, universality, from those.
````

  - Proposal `G5-B7` (reply lines 77), would change L247:

````
> L247 | **Answer agreement.**
````

  - Proposal `G5-B8` (reply lines 81), would change L220:

````
> L220 | - a **violation** occurs when fidelity or the answer fails at \((a,b)\);
````

  - Quotations: “the component and global fidelity conditions of Part V” — found at L189; “from fidelity under change” — found at L520; “the fidelity and the answers” — found at L630; “fidelity fails” — found at L220.
- **Goes to a checker** (rule 5): challenged by GLM and Mimo. Lines at stake: L220, L245, L247, L520.

#### D4.3 · definition · Reading through a transport

Lines it formalizes or quotes (from the brief): L119.

- **Mimo** (reply line 25; does not challenge): Named among the items with nothing to add.
- **GLM** (reply line 9; does not challenge): Says what the sentence says.
- **Goes to no checker**: no point challenges it and it is not one of the twelve; recorded under rule 7 below.

#### D6.7 · definition · Account (E)

Lines it formalizes or quotes (from the brief): L262.

- **Mimo** (reply line 25; does not challenge): Named among the items with nothing to add.
- **GLM** (reply line 9; does not challenge): Says what the sentence says.
- **Goes to no checker**: no point challenges it and it is not one of the twelve; recorded under rule 7 below.

#### E7 · encoding · Transport results

Lines it formalizes or quotes (from the brief): L353, L361, L363, L365.

- **Mimo:** no point on this item.
- **GLM** (reply line 17; does not challenge): Named among the items with nothing to add (with D5.4, D5.5, D5.6 taken singly, D4.3, D6.7).
- **Goes to no checker**: no point challenges it and it is not one of the twelve; recorded under rule 7 below.

#### FC19 · claim · (F1) and (F2) do different work

Lines it formalizes or quotes (from the brief): L245.

- **Mimo** (reply line 19; challenges): The two existence claims track the sentence; the glosses over-read the conditions (see (d)).
  - Proposal `M5-B6` (reply lines 83–85; printed in full under D5.7 above), would change L245.
- **Mimo** (reply lines 81–85; challenges): The existence claims stand; the first gloss over-reads: a hand model with two target components projecting alike lets (F1), (F2) and (A) hold with any of three counterparts, so "a decomposition in error" survives (F1) whenever two subnetworks project alike (rests on I14); the second gloss survives (no model found); proposes a new L245 recording the two extents.
  - Proposal `M5-B6` (reply lines 83–85; printed in full under D5.7 above), would change L245.
  - Quotations: “a decomposition in error” — found at L245.
- **GLM** (reply line 13; does not challenge): The formal statement says what the sentence says.
  - Quotations: “not tested” — not found in the text; found in the brief.
- **GLM** (reply line 57; does not challenge): Both witnesses survive by hand (a lost shared constraint caught by (F2); an error hidden in a background component caught by (F1)); the sentence holds; background components should be kept visible somewhere.
- **Goes to a checker** (rule 5): challenged by Mimo. Lines at stake: L245.

#### FC20 · claim · When (F2) at a pair gives (A) at that pair (violation in either extent)

Lines it formalizes or quotes (from the brief): L219, L220, L250.

- **Mimo** (reply line 21; challenges): The formal statement is a lemma about (F2), not a sentence of the text (see (b)).
- **Mimo** (reply lines 29–35; challenges): The counterexample tells not against the text (no line says (F2) gives (A)) but against the claim's wording and against I81 (a value map may merge values) with U1 (κ(⊥) := ⊥); the second check's refinement stands (where Ans_p is determined (F2) gives κ(Ans_p)); the claim should be restated; what the text should record is that a violation of fidelity and a failure of (A) are not one event; proposes a new L220 (writes I50's distinction in); were (F2) to carry the answers, L189's value maps would be made injective, which L247 and L630 show the text does not want.
  - Proposal `M5-B1` (reply lines 31–33), would change L220:

````
> L220 | - a **violation** occurs when fidelity fails at \((a,b)\), that is when (F1) or the valuation equation of (F2) fails there; a failure of (A) is a violation of question fidelity, and the two need not occur together;
````

  - Quotations: “violation” — found at L215, L220, L221, L223 and 2 more lines.
- **GLM** (reply line 15; challenges): The claim's own wording needs repair: wherever Ans_p is determined, (F2)'s valuation equation forces κ(y) for every κ; failure needs Ans_p = ⊥ and a κ merging the values Sol_D takes; the claim should be restated so and record U1.
  - Quotations: “(F2) at a pair gives (A) there only if κ is injective” — not found in the text; not in the brief.
- **GLM** (reply lines 21–25; challenges **OWNER QUESTION**): The counterexample tells against the inventions, not the text (value maps are I14's, the merging is I14's allowance of non-injective maps, κ(⊥) = ⊥ is U1); it survives I81's alternative (a); first remedy: require I14's value maps to be injective (a merging κ hides a difference, which L245 says (F1) prevents; FC96 (ii) then holds without its caveat), with no change to the text; second, "if the owner wants the text to settle it", a new L189 (writes I14 in).
  - Proposal `G5-B1` (reply lines 23), would change L189:

````
> L189 | where \(\pi:X_D\to X_E\) on the stated scope, \(\tau\) translates edits, \(\sigma\) translates boundaries, and \(\lambda\) assigns each component of \(E\) a subnetwork of \(D\) with a port translation that carries distinct values to distinct values.
````

- **Goes to a checker** (rule 5): challenged by GLM and Mimo; one of the twelve counterexamples the second check reproduced (FC20). Lines at stake: L189, L220.
- Marks: OWNER QUESTION points present.

#### FC96 · claim · Argument 2: same counterparts, one account

Lines it formalizes or quotes (from the brief): L562.

- **Mimo** (reply line 17; challenges): (i) parts company: the words give "Their answer profiles coincide on C" as part of the claim, while the formal statement is a consequence of both candidates meeting (A); the consequence stands as a remark but is not (i); the words stand; (ii) is the sentence only under I10 and I14 (see (d)).
  - Quotations: “Their answer profiles coincide on \(C\)” — found at L562.
- **Mimo** (reply lines 87–91; challenges): (ii) fails outside the models tried: a hand model where two candidates share the counterpart {c0} with bijective port translations onto the same ports but one value map swaps values, so the signatures differ as sets (I10); (ii) needs the value maps to carry values the same way; L562 stands as long as the words carry no values; once I14 is written in, L562 must say so; proposes a new L562.
  - Proposal `M5-B7` (reply lines 89–91), would change L562:

````
> L562 | (i) Their answer profiles coincide on \(C\). (ii) If a bijection \(\varphi\) of their active components gives each \(k\) and \(\varphi(k)\) one counterpart, the same subnetwork of \(D\) with port translations that are bijections onto the same ports of \(D\) and carry values the same way, then \(k\) and \(\varphi(k)\) are of one kind on \(C\) for every \(k\);
````

- **GLM** (reply line 13; does not challenge): The formal statement says what the sentence says; (ii)'s value-map caveat is noted (see (d)).
  - Quotations: “not tested” — not found in the text; found in the brief.
- **GLM** (reply line 59; does not challenge): (i) holds; (ii) cannot be broken when the value maps agree; the caveat vanishes under injective κ between equal domains.
- **Goes to a checker** (rule 5): challenged by Mimo. Lines at stake: L562.

#### FC104 · claim · The two extents of 'fidelity' across the text

Lines it formalizes or quotes (from the brief): L189, L245, L247, L520, L630.

- **Mimo** (reply line 23; challenges): A reading of thirty lines, not a claim about models; answered at D5.7.
  - Proposal `M5-B6` (reply lines 83–85; printed in full under D5.7 above), would change L245.
  - Proposal `M5-B11` (reply lines 115–117; printed in full under D5.7 above), would change L520.
- **GLM** (reply lines 11–13; challenges): FC104's claim that no single extent serves every line is right on the reader's reading; its "not tested" status is honest; the repair is the matter 12 package.
  - Proposal `G5-B6` (reply lines 73; printed in full under D5.7 above), would change L520.
  - Proposal `G5-B7` (reply lines 77; printed in full under D5.7 above), would change L247.
  - Proposal `G5-B8` (reply lines 81; printed in full under D5.7 above), would change L220.
  - Quotations: “the component and global fidelity conditions of Part V” — found at L189; “from fidelity under change” — found at L520; “the fidelity and the answers” — found at L630; “fidelity fails” — found at L220; “not tested” — not found in the text; found in the brief.
- **Goes to a checker** (rule 5): challenged by GLM and Mimo. Lines at stake: L220, L245, L247, L520.

#### FC64 · claim · Functional transport

Lines it formalizes or quotes (from the brief): L353.

- **Mimo** (reply lines 105–109; challenges): The induction stands; "with matching scopes" does not say whose; with π partial (I16) the equation needs every intermediate state in π's scope; proposes a new L353.
  - Proposal `M5-B10` (reply lines 107–109), would change L353:

````
> L353 | If \(\pi\circ S_a=T_a\circ\pi\) for every admitted generator \(a\), the same equation is met by every admitted finite composition whose intermediate states all lie in the scope of \(\pi\).
````

  - Quotations: “with matching scopes” — found at L353.
- **GLM** (reply line 13; does not challenge): The formal statement says what the sentence says.
  - Quotations: “not tested” — not found in the text; found in the brief.
- **GLM** (reply line 61; does not challenge): Holds by induction; "matching scopes" supplies what each step needs.
  - Quotations: “matching scopes” — found at L353.
- **Goes to a checker** (rule 5): challenged by Mimo. Lines at stake: L353.

#### FC65 · claim · Relational transport: simulations compose

Lines it formalizes or quotes (from the brief): L361.

- **Mimo** (reply line 25; does not challenge): Named among the items with nothing to add.
- **GLM** (reply line 13; does not challenge): The formal statement says what the sentence says.
  - Quotations: “not tested” — not found in the text; found in the brief.
- **GLM** (reply line 63; challenges): If the forward simulation clause ranges over all admitted edits, a partial τ makes the composite's condition fail with no fault in R or R′ (hand model); L361's "when intermediate scopes agree" gestures at the other reading without saying it; L361 should say "over edits both translations carry".
  - Inline proposal (reply line 63; written in the reader's running text, not in a fence), would change L361 — a phrase for L361; the reader gives no whole sentence:

````
over edits both translations carry
````

  - Quotations: “when intermediate scopes agree” — found at L361; “over edits both translations carry” — not found in the text; not in the brief.
- **Goes to a checker** (rule 5): challenged by GLM. Lines at stake: L361.

#### FC66 · claim · (T2): the accumulated bound, and none without a modulus

Lines it formalizes or quotes (from the brief): L363.

- **Mimo** (reply lines 93–97; challenges): (a) the recursion gives the sum only with e_0 = 0, and the reader says the words name only the states in scope (the reader has not the lines that define e_k, ε, L; L363 as it stands contains "(so \(e_0=0\))"); a first state matched only to within e_0 gives a larger bound; (b) "Without a modulus, no accumulated bound follows" is stronger than the computed result (hand model T(x) = sin(1/x): e_n ≤ 2 for every n); proposes a new fragment of L363.
  - Proposal `M5-B8` (reply lines 95–97), would change L363:

````
> L363 | meets the bound \(e_n\le\varepsilon\sum_{k<n}L^k\) whenever \(z,Sz,\dots,S^{n-1}z\) lie in that scope and the discrepancy at the first state is zero. (T2) Without a modulus, no bound in terms of \(\varepsilon\) and \(n\) alone follows.
````

  - Quotations: “Without a modulus, no accumulated bound follows” — found at L363.
- **GLM** (reply line 13; does not challenge): The formal statement says what the sentence says.
  - Quotations: “not tested” — not found in the text; found in the brief.
- **GLM** (reply line 65; does not challenge): (a) holds by induction; (b) as claimed (hand model).
- **Goes to a checker** (rule 5): challenged by Mimo. Lines at stake: L363.

#### FC67 · claim · A declared invertible recoding keeps the content

Lines it formalizes or quotes (from the brief): L365.

- **Mimo** (reply lines 99–103; challenges): Two gaps in "preserves the content": a recoding that touches the port the query reads preserves the answers only through a reader applying the convention where the answer is read (hand model with the swap); and the recoded carrier's history is the original's followed by the recoding; proposes a new L365.
  - Proposal `M5-B9` (reply lines 101–103), would change L365:

````
> L365 | A declared, invertible recoding of a carrier preserves the fidelity and, with the same convention applied where the answer is read, the answers; the provenance of the recoded carrier is the history of the original followed by the recoding (Argument 8).
````

  - Quotations: “Preserves the content” — found at L365.
- **GLM** (reply line 13; does not challenge): The formal statement says what the sentence says.
  - Quotations: “not tested” — not found in the text; found in the brief.
- **GLM** (reply line 67; challenges): The fidelity half holds; the provenance half is "holds by construction" (I54), written in, not searched; a recoding transforms information, so by decisions S25–S26 its provenance must record it; the sentence should not be counted beyond the fidelity half until I54's part is read.
  - Quotations: “holds by construction” — not found in the text; found in the brief.
- **Goes to a checker** (rule 5): challenged by GLM and Mimo. Lines at stake: L365.

#### I15 · invention · 'Active component' means a member of Γ

Lines it formalizes or quotes (from the brief): L233.

- **Mimo** (reply line 39; challenges): Settled in substance by L231 ("an identified set Γ of active commitments in E. The commitments Γ are components of E") with L233's "active component"; the identification is only implied; written in at L231.
  - Proposal `M5-B3` (reply lines 63–65; printed in full under D5.3 above), would change L231.
  - Quotations: “an identified set \(\Gamma\) of active commitments in \(E\). The commitments \(\Gamma\) are components of \(E\)” — found at L231; “active component” — found at L119, L233, L315, L554 and 1 more lines.
- **GLM** (reply lines 29–33; challenges): The text half settles it (L231's "identified set Γ of active commitments", "those the candidate offers as doing the work"), but L233's "active component" is never defined and L189's "each component" pulls the other way; proposes a new L231 (writes I15 in).
  - Proposal `G5-B2` (reply lines 31; printed in full under D5.1 above), would change L231.
  - Quotations: “an identified set \(\Gamma\) of active commitments” — found at L231; “those the candidate offers as doing the work” — found at L231; “active component” — found at L119, L233, L315, L554 and 1 more lines; “each component” — found at L91, L119, L189, L281 and 1 more lines.
- **Goes to a checker** (rule 5): challenged by GLM and Mimo. Lines at stake: L231.

#### I16 · invention · The domain of π: 'on the stated scope'

Lines it formalizes or quotes (from the brief): L189.

- **Mimo** (reply line 41; challenges): Not settled: the arrow fixes a function, "on the stated scope" does not say how far π is defined; written in at L189 (the maths' choice, not forced); the same wording records I14's map on values and I17's partiality.
  - Proposal `M5-B2` (reply lines 57–59; printed in full under D5.1 above), would change L189.
  - Quotations: “on the stated scope” — found at L189.
- **GLM** (reply lines 35–37; challenges): Not settled: "on the stated scope" names no scope and the arrow says total; should be settled because L315 needs pairs outside C carried; proposes a new L189 (writes I16 and part of I17 in).
  - Proposal `G5-B3` (reply lines 37; printed in full under D5.1 above), would change L189.
  - Quotations: “on the stated scope” — found at L189.
- **Goes to a checker** (rule 5): challenged by GLM and Mimo. Lines at stake: L189.

#### I17 · invention · Partial τ and σ; which pairs a transport 'translates'

Lines it formalizes or quotes (from the brief): L315.

- **Mimo** (reply line 43; challenges): Not settled: L315 uses "translate" of pairs and L189 does not say whether τ and σ name every edit and boundary; written in at L189.
  - Proposal `M5-B2` (reply lines 57–59; printed in full under D5.1 above), would change L189.
  - Quotations: “translate” — found at L119, L189, L233, L315.
- **GLM** (reply lines 39–41; challenges): Partly settled: "in C or outside it" rules out reading "translates" as "is in C" (alternative (b)); the partiality of τ and σ and the meaning of "translates" are not settled; proposes new wording for a fragment of L315.
  - Proposal `G5-B4` (reply lines 41; printed in full under D5.1 above), would change L315.
  - Quotations: “in \(C\) or outside it” — found at L315.
- **Goes to a checker** (rule 5): challenged by GLM and Mimo. Lines at stake: L189, L315.

#### I18 · invention · The homomorphism clause of (F2): its range, and that it is not pointwise

Lines it formalizes or quotes (from the brief): L242.

- **Mimo** (reply line 45; challenges): Not settled: neither the range of the clause nor whether it holds at a pair; written in at L242.
  - Proposal `M5-B4` (reply lines 69–71; printed in full under D5.5 above), would change L242.
- **GLM** (reply lines 43–45; challenges): Not settled: τ(a2a1) = τ(a2)τ(a1) presumes τ total on composites; with I84's default almost every partial transport fails (F2) and L315's conflicts outside C become nearly unsatisfiable; the clause should ask nothing of composites outside the domain; proposes a sentence after L242 (writes I84 (a) in).
  - Proposal `G5-B5` (reply lines 45), would change L242:

````
> after L242 | The clause \(\tau(a_2a_1)=\tau(a_2)\tau(a_1)\) is required when \(a_2\), \(a_1\) and \(a_2a_1\) lie in the domain of \(\tau\); it asks nothing of other composites, and it is a condition on \(\tau\) as a whole, not at a pair.
````

- **Goes to a checker** (rule 5): challenged by GLM and Mimo. Lines at stake: L242.

#### I49 · invention · 'Faithful' and 'fidelity': the narrow extent by default, the wide one where a line asks for it

Lines it formalizes or quotes (from the brief): L189, L247, L520, L630.

- **Mimo** (reply line 47; challenges): Not a settling but a patch; the words change at L245 and L520.
  - Proposal `M5-B6` (reply lines 83–85; printed in full under D5.7 above), would change L245.
  - Proposal `M5-B11` (reply lines 115–117; printed in full under D5.7 above), would change L520.
- **GLM** (reply line 47; challenges): Not settled; L189 should stand as the narrow definition and the lines that reach for (A) should name it (the matter 12 package).
  - Proposal `G5-B6` (reply lines 73; printed in full under D5.7 above), would change L520.
  - Proposal `G5-B7` (reply lines 77; printed in full under D5.7 above), would change L247.
  - Proposal `G5-B8` (reply lines 81; printed in full under D5.7 above), would change L220.
- **Goes to a checker** (rule 5): challenged by GLM and Mimo. Lines at stake: L220, L245, L247, L520.

#### I81 · invention · Transports as port translations; computed ports; generated candidates; the transport space searched for ≡

Lines it formalizes or quotes (from the brief): L189, L343, L413.

- **Mimo** (reply line 49; challenges): Not settled; half belongs to the record (generated candidates, the transport space searched for ≡, π induced by λ's translations are search choices); the text should stay open on whether π is induced; the rest of I14 is written in at L189 only because "carrying" needs a map on values.
  - Proposal `M5-B2` (reply lines 57–59; printed in full under D5.1 above), would change L189.
  - Quotations: “carrying” — found at L75, L169, L233, L313 and 1 more lines.
- **GLM** (reply line 49; does not challenge): Not settled; π induced by port translations, computed ports, generated candidates and the ≡ search space are search design and should stay inventions; the FC20 counterexample does not turn on this choice; proposes nothing.
  - Quotations: “a port translation” — found at L119, L189.
- **Goes to a checker** (rule 5): challenged by Mimo. Lines at stake: L189.

#### I84 · invention · The homomorphism clause when a composite lies outside τ's domain

Lines it formalizes or quotes (from the brief): L242.

- **Mimo** (reply line 51; challenges): Not settled; written in at L242: a composite τ does not name fails the clause (the alternative leaves a change of the target with no counterpart).
  - Proposal `M5-B4` (reply lines 69–71; printed in full under D5.5 above), would change L242.
- **GLM** (reply lines 43–45; challenges): As for I18: proposes the sentence after L242 writing I84's alternative (a) into the text.
  - Proposal `G5-B5` (reply lines 45; printed in full under I18 above), would change L242.
- **Goes to a checker** (rule 5): challenged by GLM and Mimo. Lines at stake: L242.

#### I14 · invention · Subnetworks, their solutions, and port translations with value maps

Lines it formalizes or quotes (from the brief): L189, L233.

- **Mimo** (reply lines 55–59; challenges): (Given in another part.) One wording carries I14, I16 and I17: a new L189 with port translations as injections of ports and value maps per port, π defined on every translated scope, τ and σ partial.
  - Proposal `M5-B2` (reply lines 57–59; printed in full under D5.1 above), would change L189.
- **GLM** (reply lines 21–25; challenges **OWNER QUESTION**): (Given in another part.) The FC20 remedy: make I14's value maps injective; if the text is to settle it, the L189 proposal under FC20 writes I14 in.
  - Proposal `G5-B1` (reply lines 23; printed in full under FC20 above), would change L189.
- **Goes to a checker** (rule 5): challenged by GLM and Mimo. Lines at stake: L189.
- Marks: OWNER QUESTION points present.

#### I20 · invention · How the fixed query is applied to a candidate's organization

Lines it formalizes or quotes (from the brief): L141, L253.

- **Mimo** (reply lines 61–65; challenges): (Given in another part.) Proposes a new L231 adding a designation of the ports of E at which the query is read, with the active components the members of Γ (writes I15 and I20 in).
  - Proposal `M5-B3` (reply lines 63–65; printed in full under D5.3 above), would change L231.
- **GLM:** no point on this item.
- **Goes to a checker** (rule 5): challenged by Mimo. Lines at stake: L231.

#### I21 · invention · Undetermined answers: a value ⊥

Lines it formalizes or quotes (from the brief): L255.

- **Mimo** (reply lines 73–77; challenges): (Given in another part.) Proposes a new L250 adding ⊥ = ⊥ and that a map on values has ⊥ outside its domain (writes I21's comparison and U1 in).
  - Proposal `M5-B5` (reply lines 75–77; printed in full under D5.6 above), would change L250.
- **GLM:** no point on this item.
- **Goes to a checker** (rule 5): challenged by Mimo. Lines at stake: L250.

#### I50 · invention · A violation at a pair: which conditions fail

Lines it formalizes or quotes (from the brief): L220.

- **Mimo** (reply lines 29–35; challenges): I50 (given in another part): the proposed L220 writes its distinction in (a failure of (A) is a violation of question fidelity, apart from a violation of fidelity).
  - Proposal `M5-B1` (reply lines 31–33; printed in full under FC20 above), would change L220.
  - Quotations: “violation” — found at L215, L220, L221, L223 and 2 more lines.
- **GLM** (reply line 53; challenges): Named among the inventions with nothing to add, "I50 is settled by the L220 proposal under matter 12".
  - Proposal `G5-B8` (reply lines 81; printed in full under D5.7 above), would change L220.
- **Goes to a checker** (rule 5): challenged by GLM and Mimo. Lines at stake: L220.

#### U1 · U-entry · κ(⊥) := ⊥ in FC20

Lines it formalizes or quotes (from the brief): L220, L250.

- **Mimo** (reply line 53; challenges): Not settled and recorded nowhere before the check; written in at L250 in a form that leaves ⊥ outside a value map's domain, making κ(⊥) := ⊥ a reading of the program, not the text's.
  - Proposal `M5-B5` (reply lines 75–77; printed in full under D5.6 above), would change L250.
- **GLM** (reply line 51; does not challenge): Not recorded, and it should be: κ maps port values, ⊥ is an answer value, so κ(⊥) is undefined until declared; the register should carry "κ extended to answers by κ(⊥)=⊥; used by FC20", or FC20 be restated so no extension is needed.
  - Quotations: “κ extended to answers by κ(⊥)=⊥; used by FC20.” — not found in the text; not in the brief.
- **Goes to a checker** (rule 5): challenged by Mimo. Lines at stake: L250.

#### L520 · round-1 change · the round-1 change at L520

Lines it formalizes or quotes (from the brief): L520.

- **Mimo** (reply lines 113–117; challenges): The round-1 change added "non-circular dependence and non-vacuity"; (E) also names (A), which under L189's "faithful" is not fidelity; proposes a further change to L520.
  - Proposal `M5-B11` (reply lines 115–117; printed in full under D5.7 above), would change L520.
  - Quotations: “non-circular dependence and non-vacuity” — found at L520; “faithful” — found at L41, L43, L67, L69 and 14 more lines.
- **GLM** (reply lines 71–73; challenges): The round-1 addition was right but did not go far enough: (A) is unsourced if fidelity is narrow; proposes a new L520 (writes I49's resolution in).
  - Proposal `G5-B6` (reply lines 73; printed in full under D5.7 above), would change L520.
  - Quotations: “non-circular dependence and non-vacuity” — found at L520.
- **Goes to a checker** (rule 5): challenged by GLM and Mimo. Lines at stake: L520.

#### matter 12 · round-1 matter · The two extents of "fidelity": L189 and L245 give (F1) and (F2); L247's heading ("Question fidelity") and L520 reach (A); L630 keeps "the fidelity and the answers" apart.

Lines it formalizes or quotes (from the brief): L189, L245, L247, L520, L630.

- **Mimo** (reply line 119; challenges): Answered by the wordings at L245 and L520: "faithful" and "fidelity" stay narrow, (A) is question fidelity, L247's heading names that condition, L630 reads as it stands; no further change.
  - Proposal `M5-B6` (reply lines 83–85; printed in full under D5.7 above), would change L245.
  - Proposal `M5-B11` (reply lines 115–117; printed in full under D5.7 above), would change L520.
  - Quotations: “faithful” — found at L41, L43, L67, L69 and 14 more lines; “fidelity” — found at L17, L23, L37, L41 and 14 more lines.
- **GLM** (reply lines 75–83; challenges): The text needs the change: L189, L245, L630 stand; L247's heading should stop calling (A) a fidelity; L220 should let a wrong answer be a violation without calling answers fidelity (this settles I50, taking Violation⁺, since L219 defines the prediction as an answer); proposes a new L247 heading and a new L220.
  - Proposal `G5-B7` (reply lines 77; printed in full under D5.7 above), would change L247.
  - Proposal `G5-B8` (reply lines 81; printed in full under D5.7 above), would change L220.
  - Quotations: “the fidelity and the answers” — found at L630; “violation” — found at L215, L220, L221, L223 and 2 more lines.
- **Goes to a checker** (rule 5): challenged by GLM and Mimo. Lines at stake: L220, L245, L247, L520.

#### Part 5: items no point addresses

Items of this part on which neither reader made any point (both replies read whole): none. Each is recorded under rule 7 in section 6 unless a point on it in another part sends it to a checker.

### Part 6: Account - non-circular dependence and non-vacuity

Brief: `tests/S104 Round 2 - the maths against the words - part 06, Account - non-circular dependence and non-vacuity.md`. Replies: `s104_maths_mimo_6.response.txt` (Mimo), `s104_maths_glm_6.response.txt` (GLM).

#### D6.1 · definition · Deletion in a candidate

Lines it formalizes or quotes (from the brief): L255.

- **Mimo** (reply line 47; does not challenge): Named among the items with nothing to add.
- **GLM** (reply line 108; does not challenge): Named among the items with nothing to add.
- **Goes to no checker**: no point challenges it and it is not one of the twelve; recorded under rule 7 below.

#### D6.2 · definition · NC0

Lines it formalizes or quotes (from the brief): L255.

- **Mimo** (reply line 47; does not challenge): Named among the items with nothing to add.
- **GLM** (reply line 5; does not challenge): The maths reads the first sentence ("follows by evaluating") as adding nothing; a computation condition cannot be written without a module the text lacks (and S25 keeps physical possibility out); the gloss reading should stand; nothing to change.
  - Quotations: “follows by evaluating” — found at L255.
- **Goes to no checker**: no point challenges it and it is not one of the twelve; recorded under rule 7 below.

#### D6.3 · definition · NC1 (no answer slot)

Lines it formalizes or quotes (from the brief): L255.

- **Mimo:** no point on this item.
- **GLM** (reply line 7; challenges): The maths and the words part, and the words should stand: "does not appear … as a component" is not restricted to a component that constrains nothing else, as I24 adds; the model in (d) passes NC1 and meets (E); the maths should adopt I24's alternative (b).
  - Quotations: “The target's answer does not appear … as a component.” — found at L255; “and constrains nothing else” — not found in the text; found in the brief; “moving an assertion from an input slot into a component named 'law' does not discharge this” — found at L255; “structural at the declared grain” — found at L255.
- **External reader and case card:** E19 (the external reader) challenges the sentence this item formalizes (section 3 below).
- **Goes to a checker** (rule 5): challenged by GLM; challenged by E19 (the external reader). Lines at stake: L255.

#### D6.4 · definition · NC2 (a contrast lost under deletion)

Lines it formalizes or quotes (from the brief): L255.

- **Mimo** (reply line 5; challenges): The words give two contrasts; with undetermined answers equal only to themselves, "differs" also covers a value at (τ(a),σ(b)) against an undetermined answer at (1,σ(b0)), a case the maths counts nowhere; the deletion clause is written as the maths writes it; the words should stand and be made explicit (wording under I22).
  - Proposal `M6-B5` (reply lines 68–72), would change L255:

````
> L255 | There exist \((a,b)\in C\) and a nonempty block \(G\subseteq\Gamma\) such that the answer of \(E\) at \((\tau(a),\sigma(b))\) differs from its answer at \((1,\sigma(b_0))\), or is not determined at \((\tau(a),\sigma(b))\) in the claimed way, and this contrast is lost when the components of \(G\) are deleted from \(E\)

There exist \((a,b)\in C\) and a nonempty block \(G\subseteq\Gamma\) such that the answer of \(E\) at \((\tau(a),\sigma(b))\) and its answer at \((1,\sigma(b_0))\) are two values that differ, or the answer of \(E\) at \((\tau(a),\sigma(b))\) is undetermined while its answer at \((1,\sigma(b_0))\) is a value, and this contrast is lost when the components of \(G\) are deleted from \(E\)
````

  - Quotations: “differs” — found at L45, L245, L255, L397 and 2 more lines; “is not determined … in the claimed way” — found at L255; “an answer that \(E\) determines at one of these points is not determined there once \(G\) is deleted” — found at L255.
- **GLM** (reply lines 9–11; challenges **OWNER QUESTION**): Faithful to the sentence; "in the claimed way" under I22; the maths reads "block" as any nonempty subset of Γ with no recorded choice; with G = Γ and a two-valued answer port, deletion leaves the answer undetermined, so NC2 asks only for a contrast on C and all the bite against lookups lies in NC1; if "block" is not fixed elsewhere the text should say whether G may be Γ; one wording "if the owner wants a proper part deleted (this writes content in; the owner decides)".
  - Proposal `G6-B1` (reply lines 11), would change L255:

````
> L255 | There exist \((a,b)\in C\) and a nonempty block \(G\subseteq\Gamma\), \(G\neq\Gamma\), such that the answer of \(E\) at \((\tau(a),\sigma(b))\) differs from its answer at \((1,\sigma(b_0))\), or is not determined at \((\tau(a),\sigma(b))\) in the claimed way, and this contrast is lost when the components of \(G\) are deleted from \(E\)
````

  - Quotations: “in the claimed way” — found at L255; “several values → ⊥” — not found in the text; not in the brief; “through NC1 only” — not found in the text; found in the brief.
- **GLM** (reply line 94; challenges): NC2 near-trivial under the unrecorded reading "block = subset": with G = Γ and a two-valued answer port any candidate with a contrast meets NC2, so the held results involving NC2 show little about the clause (rests on that reading and I21); not a counterexample to a claim.
  - Quotations: “block = subset” — not found in the text; not in the brief.
- **Goes to a checker** (rule 5): challenged by GLM and Mimo. Lines at stake: L255.
- Marks: OWNER QUESTION points present.

#### D6.5 · definition · Non-circular dependence

Lines it formalizes or quotes (from the brief): L255.

- **Mimo** (reply line 47; does not challenge): Named among the items with nothing to add.
- **GLM** (reply line 108; does not challenge): Named among the items with nothing to add.
- **External reader and case card:** E19 (the external reader) challenges the sentence this item formalizes (section 3 below).
- **Goes to a checker** (rule 5): challenged by E19 (the external reader). Lines at stake: L255.

#### D6.6 · definition · Non-vacuity

Lines it formalizes or quotes (from the brief): L257.

- **Mimo** (reply line 47; does not challenge): Named among the items with nothing to add.
- **GLM** (reply line 13; does not challenge): Faithful on both conjuncts; the second conjunct is a condition on a stated scope, which makes L265's first sentence false (FC33).
- **Goes to no checker**: no point challenges it and it is not one of the twelve; recorded under rule 7 below.

#### D6.7 · definition · Account (E)

Lines it formalizes or quotes (from the brief): L262.

- **Mimo** (reply line 47; does not challenge): Named among the items with nothing to add.
- **GLM** (reply line 15; challenges): Five conjuncts under four headings is consistent if "the four conditions" names Part V's headings; L520's sources then leave (A) with no source unless "fidelity under change" is read wide, against L189 (wording in (e)).
  - Proposal `G6-B9` (reply lines 102), would change L520:

````
> L520 | Everything else is defined in terms of the two imports, the structural vocabulary of (O) and (Q), the declared indices and the declared inputs (below). Roles, from admitted edits (Part II). Kinds, from signatures (K). The respect of a question, from its query (Part III). Representation, from fidelity and provenance (R). Provenance, from physical history (Parts IV, XII). Account, from component fidelity under change, question fidelity, non-circular dependence and non-vacuity (E). Understanding, construction, newness, origin, repair, created explanation, capability, recursion, universality, from those.
````

  - Quotations: “the four conditions” — found at L61; “fidelity under change” — found at L520.
- **Goes to a checker** (rule 5): challenged by GLM. Lines at stake: L520.

#### D6.8 · definition · The four conditions

Lines it formalizes or quotes (from the brief): L231, L262.

- **Mimo** (reply line 47; does not challenge): Named among the items with nothing to add.
- **GLM** (reply line 15; challenges): As for D6.7 (the reply heads the entry "D6.7–D6.8 / FC31").
  - Proposal `G6-B9` (reply lines 102; printed in full under D6.7 above), would change L520.
  - Quotations: “the four conditions” — found at L61; “fidelity under change” — found at L520.
- **Goes to a checker** (rule 5): challenged by GLM. Lines at stake: L520.

#### D6.9 · definition · Relabeling

Lines it formalizes or quotes (from the brief): L257.

- **Mimo** (reply lines 21–29; challenges): With "relabeling" read on the target's answer, a candidate meeting (A) answers constantly across a relabeling-only contract, so NC2 has nothing to hold on, but a candidate not meeting (A) can answer differently at two relabelings; the sentence is not carried as written; proposes "meets (A) and non-circular dependence" in L257.
  - Proposal `M6-B2` (reply lines 23–27), would change L257:

````
> L257 | A contract consisting only of relabelings, or excluding every change under which the active commitments could matter to \(\mathcal Q\), admits no candidate that meets non-circular dependence

A contract consisting only of relabelings, or excluding every change under which the active commitments could matter to \(\mathcal Q\), admits no candidate that meets (A) and non-circular dependence
````

  - Quotations: “relabeling” — found at L257.
- **GLM** (reply line 108; does not challenge): Named among the items with nothing to add.
- **Goes to a checker** (rule 5): challenged by Mimo. Lines at stake: L257.

#### D6.10 · definition · Tables

Lines it formalizes or quotes (from the brief): L269.

- **Mimo** (reply line 47; does not challenge): Named among the items with nothing to add.
- **GLM** (reply lines 17–19; challenges): The words overstate: under I32 the table's relation is the baseline projection held fixed, and a contract may hold an intervention on a port outside the table's ports, or one the projected solutions are indifferent to, and the table then meets (F1); proposes a new L269 sentence.
  - Proposal `G6-B2` (reply lines 19), would change L269:

````
> L269 | A **table of observed answers** has no component whose relation is replaced by an intervention; it fails (F1) under any contract containing an intervention that changes the solutions its component's counterpart admits.
````

- **Goes to a checker** (rule 5): challenged by GLM. Lines at stake: L269.

#### FC22 · claim · The baseline alone gives no contrast

Lines it formalizes or quotes (from the brief): L141, L255.

- **Mimo** (reply line 43; does not challenge): With C = {(1,b0)} and τ(1) = 1 the two points coincide; a consequence of the definitions; nothing to change.
  - Quotations: “differs” — found at L45, L245, L255, L397 and 2 more lines.
- **Mimo** (reply line 126; does not challenge): No attack held.
- **GLM** (reply line 21; does not challenge): Follows from the words alone: with C = {(1,b0)} the comparison is of a point with itself; holds unconditionally; no change.
- **GLM** (reply line 96; does not challenge): Could not break it: a point compared with itself cannot differ; holds unconditionally.
- **Goes to no checker**: no point challenges it and it is not one of the twelve; recorded under rule 7 below.

#### FC23 · claim · 'p because p' fails non-circular dependence through NC1 only

Lines it formalizes or quotes (from the brief): L273.

- **Mimo** (reply line 7; challenges): For the single lookup with an exact slot relation the maths says what the sentence says, but L273 says "p because p" without qualification while NC1 bars only one component whose relation is exactly the slot relation and constrains nothing else; candidates restating the answer in other shapes meet (E) (two in (d)); the words stand and the test is widened (under I24).
  - Proposal `M6-B6` (reply lines 80–84), would change L255:

````
> L255 | The target's answer does not appear, at the declared grain, as an unanalysed boundary input or as a component; moving an assertion from an input slot into a component named "law" does not discharge this. Identity of that assertion with the target's answer is structural at the declared grain, not the indiscriminate identification of all logically equivalent mathematical statements.

The target's answer does not appear, at the declared grain, as an unanalysed boundary input or as a component; moving an assertion from an input slot into a component named "law" does not discharge this. The answer appears as a component when the relations of one component, or of a block of components, fix the answer ports of \(E\) to the target's answer at every pair of \(C\) at which that answer is determined; what else those relations constrain does not discharge this. Identity of that assertion with the target's answer is structural at the declared grain, not the indiscriminate identification of all logically equivalent mathematical statements.
````

  - Quotations: “p because p” — found at L273, L397.
- **Mimo** (reply line 51; does not challenge): FC23 (b): the lookup whose background component is empty at both pairs meets neither NC1 nor NC2; a counterexample to the claim's phrasing ("through NC1 only"), resting on U3 and the claim's premise, not to the text; L273 stands; no text change removes it because it does not tell against the text; with the premise "the other components are jointly satisfiable at both points" the claim held; its lesson: NC2 alone does not exclude a lookup, so the exclusion of "p because p" rests on the "does not appear" sentence, where the vagueness is.
  - Quotations: “through NC1 only” — not found in the text; found in the brief; “the other components are jointly satisfiable at both points” — not found in the text; not in the brief; “p because p” — found at L273, L397; “does not appear” — found at L255.
- **Mimo** (reply lines 102–112; challenges): Hand model against L273 under I83: a target undetermined at (e1,b0) and a candidate component k restating the answer where the target has one; (F1), (F2), (A), NC1 and NC2 hold, so (E) holds for a component that restates the answer wherever the target has one (within the bounds searched; rests on I83 and I21's equality of undetermined answers); removed by the I24 wording (the model is given in a fence at reply lines 103–111).
  - Proposal `M6-B6` (reply lines 80–84; printed in full under FC23 above), would change L255.
- **Mimo** (reply lines 114–124; challenges): Hand model against L273 under I24's "constrains nothing else": one component fixing the answer port and a second port meets (E) (within the bounds searched); removed by the same wording (the model is given in a fence at reply lines 115–123).
  - Proposal `M6-B6` (reply lines 80–84; printed in full under FC23 above), would change L255.
  - Quotations: “constrains nothing else” — not found in the text; found in the brief; “and constrains nothing else” — not found in the text; found in the brief.
- **GLM** (reply line 39; does not challenge): FC23 (b) tells against the claim's wording and U3's footprint reading, not the text: the lookup fails NC1, so L273's verdict stands; under the solutions reading the model leaves the premise; restate the claim with a satisfiable background; the text needs nothing.
  - Quotations: “p because p” — found at L273, L397; “through NC1 only” — not found in the text; found in the brief; “no other component constraining the answer ports” — not found in the text; found in the brief.
- **GLM** (reply lines 73–92; challenges): The decorated lookup confines FC23 (a)'s "holds" to exact slots (model under I24).
  - Quotations: “constrains nothing else” — not found in the text; found in the brief.
- **Goes to a checker** (rule 5): challenged by GLM and Mimo; one of the twelve counterexamples the second check reproduced (FC23 (b)). Lines at stake: L255.

#### FC24 · claim · L273's second sentence uses 'account' for a candidate

Lines it formalizes or quotes (from the brief): L273.

- **Mimo** (reply line 47; does not challenge): Nothing to add in (a); its content is matter 7 (under (e)).
- **Mimo** (reply line 126; does not challenge): No attack held.
- **GLM** (reply line 25; challenges): The reading is right: nothing meeting (E) fails non-circular dependence, so "an account" there names a candidate offered as an account (wording under matter 7); under I24's alternative (b) the conclusion is unchanged.
  - Proposal `G6-B10` (reply lines 106), would change L273:

````
> L273 | So does a candidate offered as an account whose only substantive component restates the answer it was asked for; packaging a dependence that answers a different question beside it does not repair this.
````

  - Quotations: “an account” — found at L8, L43, L69, L75 and 18 more lines.
- **GLM** (reply lines 73–92; challenges): The decorated lookup confines FC24's "holds" to exact slots (model under I24).
  - Quotations: “constrains nothing else” — not found in the text; found in the brief.
- **Goes to a checker** (rule 5): challenged by GLM. Lines at stake: L273.

#### FC30 · claim · (E) takes no assessor, history, provenance or wording

Lines it formalizes or quotes (from the brief): L43, L67, L277.

- **Mimo** (reply line 9; challenges): The formal statement is what the words say (no assessor, history or provenance among (E)'s arguments); the heading's "or wording" is not carried by it, since (E) takes the stated scope Σ, a declared statement; no change.
  - Quotations: “or wording” — not found in the text; found in the brief.
- **Mimo** (reply line 126; does not challenge): No attack held.
- **GLM** (reply line 27; does not challenge): Holds by construction and matches L43, L67, L277; Σ and ℓ are arguments, which L526's "stated, not defined" covers; no parting.
  - Quotations: “stated, not defined” — found at L526.
- **GLM** (reply line 96; does not challenge): Could not break it; holds by construction.
- **Goes to a checker** (rule 5): challenged by Mimo. Lines at stake: L43, L67, L277.

#### FC31 · claim · 'The four conditions', five conjuncts, and L520's three sources

Lines it formalizes or quotes (from the brief): L61, L231, L262, L520, L536.

- **Mimo** (reply line 31; challenges): (E) has five conjuncts under four headings; "the four conditions" at L231 and L536 names the headings, nothing to change there; L520's three sources cover the four headings only at the wide extent of "fidelity" (I49); at L189's narrow extent (A) has no source named (wording under L520 in (e)).
  - Proposal `M6-B9` (reply lines 132–136), would change L520:

````
> L520 | Account, from fidelity under change, non-circular dependence and non-vacuity (E).

Account, from component fidelity and question fidelity under change, non-circular dependence and non-vacuity (E).
````

  - Quotations: “the four conditions” — found at L61; “fidelity” — found at L17, L23, L37, L41 and 14 more lines.
- **GLM** (reply line 15; challenges): As for D6.7: L520 leaves question fidelity without a source at the narrow extent (wording in (e)).
  - Proposal `G6-B9` (reply lines 102; printed in full under D6.7 above), would change L520.
  - Quotations: “the four conditions” — found at L61; “fidelity under change” — found at L520.
- **Goes to a checker** (rule 5): challenged by GLM and Mimo. Lines at stake: L520.

#### FC32 · claim · L520 (after round 1) against L526's dependence order

Lines it formalizes or quotes (from the brief): L520, L526.

- **Mimo** (reply lines 33–41; challenges): (E) uses (O), (Q), (K), t, Γ, δ, Σ and ℓ; L526 names (F1), (F2), (A) and "those", not non-circular dependence, non-vacuity, or the indices and inputs among (E)'s ancestors, while L520 now names the first two; proposes a new L526 sentence.
  - Proposal `M6-B3` (reply lines 35–39), would change L526:

````
> L526 | (F1), (F2), (A) depend on (O), (Q), (K). (E) depends on those.

(F1), (F2), (A) depend on (O), (Q), (K). Non-circular dependence and non-vacuity depend on (O), (Q), (K), the declared indices and the declared inputs. (E) depends on (F1), (F2), (A), non-circular dependence and non-vacuity.
````

  - Quotations: “at the declared grain” — found at L255.
- **GLM** (reply lines 29–31; challenges): After round 1, (E) has two conjuncts for which L526 names no ancestors; NC1 also uses the grain and the designation; proposes a new L526 passage.
  - Proposal `G6-B3` (reply lines 31), would change L526:

````
> L526 | (F1), (F2), (A), non-circular dependence and non-vacuity depend on (O), (Q), (K) and on the declared indices and the declared inputs. (E) depends on those. (O) and (Q) depend on nothing; nor do the declared indices and the declared inputs, which are stated, not defined.
````

- **Goes to a checker** (rule 5): challenged by GLM and Mimo. Lines at stake: L526.

#### FC33 · claim · 'Every conjunct is a condition on supplied relations; none inspects a label'

Lines it formalizes or quotes (from the brief): L265.

- **Mimo** (reply lines 11–19; challenges): L265's "Every conjunct is a condition on how supplied relations behave under the changes in C" is not carried by non-vacuity as L257 writes it (a condition on a statement of scope and on the baseline); part (a) (renaming) is what the words say; proposes a narrower L265 (moving the scope condition out of (E) would change L262 and L257).
  - Proposal `M6-B1` (reply lines 13–17), would change L265:

````
> L265 | Every conjunct is a condition on how supplied relations behave under the changes in \(C\). None inspects a label.

(F1), (F2), (A) and non-circular dependence are conditions on how supplied relations behave under the changes in \(C\); non-vacuity is a condition on the target at the baseline and on the statement of the scope of \(C\). None inspects a label.
````

  - Quotations: “Every conjunct is a condition on how supplied relations behave under the changes in \(C\)” — found at L265.
- **Mimo** (reply line 126; does not challenge): No attack held on part (a).
- **GLM** (reply lines 33–35; challenges): The claim's own part (b) concedes that L265's first sentence fails of non-vacuity's second conjunct and needs the grain reading for NC1; proposes a new L265.
  - Proposal `G6-B4` (reply lines 35), would change L265:

````
> L265 | (F1), (F2), (A) and the final sentence of non-circular dependence are conditions on how supplied relations behave under the changes in \(C\); the other sentences of non-circular dependence are read at the declared grain, and non-vacuity's second sentence is a condition on what is stated about the contract. None inspects a label.
````

- **GLM** (reply line 96; does not challenge): Part (a): could not break it (invariance under bijection).
- **Goes to a checker** (rule 5): challenged by GLM and Mimo. Lines at stake: L265.

#### FC108 · claim · The first sentence of non-circular dependence adds no condition

Lines it formalizes or quotes (from the brief): L255.

- **Mimo** (reply line 45; does not challenge): See I23: the words do not say whether the first sentence is a condition or a gloss.
- **Mimo** (reply line 126; does not challenge): No attack held.
- **GLM** (reply line 5; does not challenge): As for D6.2: the gloss reading should stand; nothing to change.
  - Quotations: “follows by evaluating” — found at L255.
- **GLM** (reply line 96; does not challenge): Could not break it; holds by construction.
- **Goes to no checker**: no point challenges it and it is not one of the twelve; recorded under rule 7 below.

#### I21 · invention · Undetermined answers: a value ⊥

Lines it formalizes or quotes (from the brief): L255.

- **Mimo** (reply lines 55–64; challenges): Not fixed: L141 gives Q a codomain Y_p while L255 speaks of answers "not determined"; nothing says whether that covers empty and many-valued results alike, or whether two undetermined answers are equal in (A); proposes a sentence after (A) at L250 (writes I21 in).
  - Proposal `M6-B4` (reply lines 57–62), would change L250:

````
> L250 | \operatorname{Ans}_E(\tau(a),\sigma(b))=\operatorname{Ans}_p(a,b). \tag{A}

\operatorname{Ans}_E(\tau(a),\sigma(b))=\operatorname{Ans}_p(a,b). \tag{A}
An answer is one value of \(Y_p\) or the undetermined answer, which the query yields when its value is not a single value of \(Y_p\); the undetermined answer equals itself and no value of \(Y_p\).
````

  - Quotations: “not determined” — found at L255.
- **GLM** (reply lines 43–45; challenges): Not settled; the text silently contradicts itself: L141 gives Y_p no member for "not determined" while L255 speaks of answers not determined; proposes an addition to L141 (writes I21 in).
  - Proposal `G6-B5` (reply lines 45), would change L141:

````
> L141 (addition) | with codomain \(Y_p\), which contains the value \(\bot\), read "not determined"; a query returns \(\bot\) when the solutions do not fix a single value of the designated ports, and two \(\bot\) answers are equal wherever answers are compared.
````

  - Quotations: “not determined” — found at L255.
- **Goes to a checker** (rule 5): challenged by GLM and Mimo. Lines at stake: L141, L250.

#### I22 · invention · 'Not determined … in the claimed way'

Lines it formalizes or quotes (from the brief): L255.

- **Mimo** (reply lines 66–74; challenges): Not fixed: "in the claimed way" has no referent; with I21 in place (A) makes the candidate's undeterminacy the target's own, so the phrase adds nothing inside (E); proposes new wording for L255's contrast clause (writes I22 in, with the asymmetry of the deletion clause).
  - Proposal `M6-B5` (reply lines 68–72; printed in full under D6.4 above), would change L255.
  - Quotations: “in the claimed way” — found at L255; “an answer that \(E\) determines at one of these points” — found at L255.
- **GLM** (reply lines 47–49; challenges): Not settled: "in the claimed way" has no antecedent; drop the clause or fix the reading; proposes new wording of L255's contrast clause (writes I22 in).
  - Proposal `G6-B6` (reply lines 49), would change L255:

````
> L255 | There exist \((a,b)\in C\) and a nonempty block \(G\subseteq\Gamma\) such that the answer of \(E\) at \((\tau(a),\sigma(b))\) differs from its answer at \((1,\sigma(b_0))\), or is not determined at \((\tau(a),\sigma(b))\) while it is determined at \((1,\sigma(b_0))\), and this contrast is lost when the components of \(G\) are deleted from \(E\)
````

  - Quotations: “in the claimed way” — found at L255.
- **Goes to a checker** (rule 5): challenged by GLM and Mimo. Lines at stake: L255.

#### I23 · invention · The first sentence of non-circular dependence, read as a heading gloss

Lines it formalizes or quotes (from the brief): L255.

- **Mimo** (reply line 76; does not challenge): Not fixed; a computation condition needs a notion of computation the two imports do not give, so it stays open and the invention stays recorded (S36); no change.
- **GLM** (reply line 51; does not challenge): Not settled and should stay open: any condition needs a notion of how an answer is computed, which the text lacks and S25 bars importing from physical possibility.
- **Goes to no checker**: no point challenges it and it is not one of the twelve; recorded under rule 7 below.

#### I24 · invention · NC1: the target's answer as an unanalysed boundary input or component, read structurally

Lines it formalizes or quotes (from the brief): L255.

- **Mimo** (reply lines 78–86; challenges): Not fixed: "unanalysed", "at the declared grain", "structural" have no definition in (O) or (Q); the words fix that a component named "law" does not help and that identity is not logical equivalence; the maths' test bars one exact slot relation only, and two restating candidates meet it (d); proposes a new L255 passage defining appearance as a component or block fixing the answer ports at every pair where the answer is determined, whatever else is constrained (writes I24 as amended; takes I28's reading).
  - Proposal `M6-B6` (reply lines 80–84; printed in full under FC23 above), would change L255.
  - Quotations: “unanalysed” — found at L255; “at the declared grain” — found at L255; “structural” — found at L3, L8, L31, L45 and 7 more lines; “moving an assertion … does not discharge this” — found at L255.
- **GLM** (reply line 53; challenges): Settled against the invention: "does not appear … as a component" with "moving an assertion from an input slot into a component named 'law' does not discharge this" closes the decoration escape that "constrains nothing else" opens; the maths should move to alternative (b); no text change.
  - Quotations: “The target's answer does not appear … as a component” — found at L255; “moving an assertion from an input slot into a component named 'law' does not discharge this” — found at L255; “constrains nothing else” — not found in the text; found in the brief.
- **GLM** (reply lines 73–92; challenges): The decorated lookup: a hand model in which a component fixes the answer port to the target's answer at every pair and also pins another port, so under I24 it is no slot, NC1 passes and (E) holds, exactly what L273's second sentence condemns (rests on I24, I82, I83, I21); under I24's alternative (b) NC1 fails as the words require; the worked cases should be re-run under (b) before it is adopted (the model is given in a fence at reply lines 75–90).
  - Quotations: “constrains nothing else” — not found in the text; found in the brief.
- **External reader and case card:** E19 (the external reader) challenges the sentence this item formalizes (section 3 below).
- **Goes to a checker** (rule 5): challenged by GLM and Mimo; challenged by E19 (the external reader). Lines at stake: L255.

#### I25 · invention · Non-circular dependence is the conjunction of its sentences

Lines it formalizes or quotes (from the brief): L255.

- **Mimo** (reply line 88; challenges): Fixed by the words: L273 makes "p because p" fail non-circular dependence while a lookup with satisfiable background meets the final sentence alone (FC23), so the earlier sentence is a condition; L257's relabeling sentence needs the contrast clause; no change.
  - Quotations: “p because p” — found at L273, L397.
- **GLM** (reply line 55; challenges): Settled by L273: under alternative (a) FC23's lookup meets non-circular dependence, against L273; the earlier sentences are conditions; no change.
- **Goes to a checker** (rule 5): challenged by GLM and Mimo. Lines at stake: L255.

#### I28 · invention · The grain as a label on the organizations compared

Lines it formalizes or quotes (from the brief): L255.

- **Mimo** (reply line 90; does not challenge): Not fixed; the imports give no map between grains; stay open (the block clause covers a restatement spread over components at the given grain).
- **GLM** (reply line 57; challenges): Settled in effect: L520 and L526 make the declared indices "stated, not defined"; alternative (a) would make the grain defined; no change.
  - Quotations: “stated, not defined” — found at L526.
- **Goes to a checker** (rule 5): challenged by GLM. Lines at stake: L255.

#### I32 · invention · A table of observed answers: its counterpart and its relation

Lines it formalizes or quotes (from the brief): L269.

- **Mimo** (reply line 92; does not challenge): Not fixed: L269 says only that a table's relation is not replaced by an intervention; its counterpart is not fixed; stay open.
- **GLM** (reply line 59; challenges): Partly settled: "has no component whose relation is replaced by an intervention" fixes the constant relation; the counterpart stays open; L269's "under any contract containing one" should be qualified (the D6.10 proposal).
  - Proposal `G6-B2` (reply lines 19; printed in full under D6.10 above), would change L269.
  - Quotations: “has no component whose relation is replaced by an intervention” — found at L269; “under any contract containing one” — found at L269.
- **Goes to a checker** (rule 5): challenged by GLM. Lines at stake: L269.

#### I82 · invention · Queries in the program; NC1 only for a query that reads a port

Lines it formalizes or quotes (from the brief): L141.

- **Mimo** (reply line 94; does not challenge): Not fixed: L141 gives a general query while the slot test is written for answer ports; stay open (a notion of a component fixing a query's value is not in (O) and (Q)).
- **GLM** (reply line 61; challenges): Not settled, and the invention narrows the text: for a query that is not a port reader NC1 never fires in the maths though it does in the words; should stay open and be recorded, not silently narrowed.
  - Quotations: “fixing a query's value” — not found in the text; not in the brief.
- **Goes to a checker** (rule 5): challenged by GLM. Lines at stake: L141.

#### I83 · invention · An answer slot needs a determined target answer at every pair

Lines it formalizes or quotes (from the brief): L255.

- **Mimo** (reply line 96; challenges): Not fixed; under the recorded choice a lookup restating the answer wherever there is one meets (E) (model in (d)); the alternative (the slot asked at pairs where the answer is determined) is what L273 needs; the I24 wording writes it in.
  - Proposal `M6-B6` (reply lines 80–84; printed in full under FC23 above), would change L255.
- **GLM** (reply lines 63–65; challenges): Not settled ("does not appear" is silent where there is no answer); the choice can stay, recorded; if the text is to speak, proposes an addition after L255's second sentence (writes I83 in).
  - Proposal `G6-B7` (reply lines 65), would change L255:

````
> L255 (addition after the second sentence) | Where the target's answer is not determined at a pair of \(C\), nothing is asked to appear there.
````

  - Quotations: “does not appear” — found at L255.
- **Goes to a checker** (rule 5): challenged by GLM and Mimo. Lines at stake: L255.

#### I79 · invention · Boundary inputs and exogenous values are carried by components

Lines it formalizes or quotes (from the brief): L255, L325.

- **Mimo:** no point on this item.
- **GLM** (reply line 67; challenges): Licensed by the text's sentence "moving an assertion from an input slot into a component named 'law' does not discharge this": the two routes name one failure; no change.
  - Quotations: “moving an assertion from an input slot into a component named 'law' does not discharge this” — found at L255.
- **Goes to a checker** (rule 5): challenged by GLM. Lines at stake: L255, L325.

#### U3 · U-entry · 'No other component constraining the answer ports', read by footprints

Lines it formalizes or quotes (from the brief): L255, L273.

- **Mimo** (reply line 98; does not challenge): Not fixed and not needed by the text: it decides only FC23 (b)'s premise; under the solutions reading the counterexample does not arise; stay open.
- **GLM** (reply line 69; does not challenge): Not the text's choice; resolve it in the maths toward the solutions reading; FC23 (b)'s model then leaves the premise.
  - Quotations: “satisfiable background” — not found in the text; found in the brief.
- **Goes to no checker**: no point challenges it and it is not one of the twelve; recorded under rule 7 below.

#### L520 · round-1 change · the round-1 change at L520

Lines it formalizes or quotes (from the brief): L520.

- **Mimo** (reply lines 130–138; challenges): The addition is what L262 and L257 ask and disturbs nothing at L61, L231, L536; it leaves (A)'s source unnamed at the narrow extent (I49); proposes a new L520 clause naming component fidelity and question fidelity; L526 needs the FC32 change.
  - Proposal `M6-B9` (reply lines 132–136; printed in full under FC31 above), would change L520.
  - Quotations: “fidelity under change” — found at L520; “fidelity” — found at L17, L23, L37, L41 and 14 more lines.
- **GLM** (reply lines 100–102; challenges): The change left (A) hanging on "fidelity under change", which L189 defines narrowly (I49); proposes a new L520.
  - Proposal `G6-B9` (reply lines 102; printed in full under D6.7 above), would change L520.
  - Quotations: “non-circular dependence and non-vacuity” — found at L520; “fidelity under change” — found at L520.
- **Goes to a checker** (rule 5): challenged by GLM and Mimo. Lines at stake: L520.

#### matter 7 · round-1 matter · L273's second sentence says an account fails non-circular dependence, where L269 and L277 use "account" strictly.

Lines it formalizes or quotes (from the brief): L269, L273, L277.

- **Mimo** (reply lines 140–148; challenges): L231 and L277 use "account" for a candidate meeting (E), while L273's second sentence speaks of an account that does not meet non-circular dependence; the words change, not the maths; proposes "candidate" in L273.
  - Proposal `M6-B10` (reply lines 142–146), would change L273:

````
> L273 | So does an account whose only substantive component restates the answer it was asked for; packaging a dependence that answers a different question beside it does not repair this.

So does a candidate whose only substantive component restates the answer it was asked for; packaging a dependence that answers a different question beside it does not repair this.
````

  - Quotations: “account” — found at L8, L43, L61, L69 and 37 more lines.
- **GLM** (reply lines 104–106; challenges): Needs the change: on the strict reading the sentence is empty (FC24); proposes "a candidate offered as an account" in L273.
  - Proposal `G6-B10` (reply lines 106; printed in full under FC24 above), would change L273.
- **Goes to a checker** (rule 5): challenged by GLM and Mimo. Lines at stake: L273.

#### Part 6: items no point addresses

Items of this part on which neither reader made any point (both replies read whole): D5.4, D5.5, D5.6, I81. Each is recorded under rule 7 in section 6 unless a point on it in another part sends it to a checker.

### Part 7: What (E) excludes - relabelings, tables, and the pole and its shadow

Brief: `tests/S104 Round 2 - the maths against the words - part 07, What (E) excludes - relabelings, tables, and the pole and its shadow.md`. Replies: `s104_maths_mimo_7.response.txt` (Mimo), `s104_maths_glm_7.response.txt` (GLM).

#### D2.1 · definition · Setting edit; the assigning component

Lines it formalizes or quotes (from the brief): L103, L119.

- **Mimo** (reply lines 3–7; challenges): D2.1 requires the replacement relation to be exactly {w : w_v = x}, leaving the component's other ports free, where L103 says only "replaces the component assigning that port"; an edit that sets v and constrains another port of j is a setting edit by the words and none by the maths; the maths should stand (otherwise "intervening on the upstream port" at L271 would carry extra constraints); the narrowing is I04's and the words should carry it; proposes a new L103.
  - Proposal `M7-B1` (reply lines 5–7), would change L103:

````
L103 | An edit that sets a port replaces the component assigning that port and leaves the rest of that component's ports free; it does not add an equation beside an incompatible one. A changed rule is a changed component.
````

  - Quotations: “replaces the component assigning that port” — found at L103; “sets a port” — found at L103, L119; “intervening on the upstream port” — found at L271.
- **GLM** (reply lines 5–10; challenges): L119 fixes that only the assigning component changes; the words do not fix what the replacement does to the assigning component's other ports (L103 rules out conjoining, not a replacement that keeps the other constraints); D2.1 frees them (I04); proposes a new L103 (writes I04's surgical form in).
  - Proposal `G7-B1` (reply lines 7–9), would change L103:

````
An edit that sets a port replaces the component assigning that port with one that sets that port and leaves that component's other ports free; it does not add an equation beside an incompatible one. A changed rule is a changed component.
````

  - Quotations: “does not add an equation beside an incompatible one” — found at L103; “replaces, does not conjoin” — not found in the text; not in the brief.
- **External reader and case card:** E04 (the external reader) challenges the sentence this item formalizes (section 3 below).
- **Goes to a checker** (rule 5): challenged by GLM and Mimo; challenged by E04 (the external reader). Lines at stake: L103.

#### D6.3 · definition · NC1 (no answer slot)

Lines it formalizes or quotes (from the brief): L255.

- **Mimo** (reply lines 9–13; challenges): Slot asks the relation to be the answer at every pair of C, while L255 says the answer does not appear as a component; they part on a contract holding a pair where one component's relation is exactly the answer, e.g. a setting of the answer port (FC26's look); the maths should stand, since a per-pair reading would fail every faithful decomposition under an intervention on the answer port; proposes a clause in L255 (writes I24's reading in).
  - Proposal `M7-B2` (reply lines 11–13), would change L255:

````
L255 | The target's answer does not appear, at the declared grain, as an unanalysed boundary input or as a component; moving an assertion from an input slot into a component named "law" does not discharge this. Identity of that assertion with the target's answer is structural at the declared grain — a component whose relation is the answer at every pair of the contract, not one an intervention replaces at a single pair — not the indiscriminate identification of all logically equivalent mathematical statements.
````

  - Quotations: “structural at the declared grain” — found at L255; “structural” — found at L3, L8, L31, L45 and 7 more lines.
- **GLM** (reply line 12; challenges): Faithful on the structural clause ("structural at the declared grain" backs I24); "at every (a,b) ∈ C" is a choice no entry records: a component that is the answer at some pairs and not at the baseline escapes NC1, as the FC26 look found (proposal in (b)).
  - Proposal `G7-B5` (reply lines 59–61), would change L255:

````
The target's answer does not appear, at the declared grain, as an unanalysed boundary input or as a component at any pair of the contract, save that a component the contract's own edit replaces at a pair is not, at that pair, the answer's appearing, the value there being the edit's, an edit the target admits as well; moving an assertion from an input slot into a component named "law" does not discharge this.
````

  - Quotations: “structural at the declared grain” — found at L255; “at every (a,b) ∈ C” — not found in the text; not in the brief.
- **External reader and case card:** E19 (the external reader) challenges the sentence this item formalizes (section 3 below).
- **Goes to a checker** (rule 5): challenged by GLM and Mimo; challenged by E19 (the external reader). Lines at stake: L255.

#### D6.4 · definition · NC2 (a contrast lost under deletion)

Lines it formalizes or quotes (from the brief): L255.

- **Mimo** (reply line 15; challenges): Contrast's second disjunct adds Ans_E(x0) ≠ ⊥ to the words; the words do not say what happens when the baseline is undetermined; under D1.3 deletion only frees, so the gap admits no model; the words stand as far as they go; no change.
  - Quotations: “or is not determined at \((\tau(a),\sigma(b))\) in the claimed way” — found at L255.
- **GLM** (reply lines 14–19; challenges): The Lost disjuncts match; Contrast does not: both disjuncts require Ans_E(x0) ≠ ⊥ while the words require only "differs from its answer at (1,σ(b0))"; the demand should stand (a contrast needs two determined ends); proposes a new L255 contrast sentence (writes the I21/I22 choice in).
  - Proposal `G7-B2` (reply lines 16–18), would change L255:

````
There exist \((a,b)\in C\) and a nonempty block \(G\subseteq\Gamma\) such that the answer of \(E\) is determined at \((1,\sigma(b_0))\) and the answer of \(E\) at \((\tau(a),\sigma(b))\) differs from it or is not determined at \((\tau(a),\sigma(b))\) in the claimed way, and this contrast is lost when the components of \(G\) are deleted from \(E\)
````

  - Quotations: “differs from its answer at (1,σ(b0))” — found at L255; “differs from ⊥” — not found in the text; not in the brief.
- **Goes to a checker** (rule 5): challenged by GLM and Mimo. Lines at stake: L255.

#### D6.6 · definition · Non-vacuity

Lines it formalizes or quotes (from the brief): L257.

- **Mimo** (reply line 31; does not challenge): Nothing to add: the formal is the sentence.
- **GLM** (reply line 21; challenges): Matches, but "excluded by a stated scope, not silently" does not say where or by whom the scope is stated; under I85 the second conjunct is never at risk in a search (see FC26 in (d)).
  - Quotations: “excluded by a stated scope, not silently” — found at L257.
- **Goes to a checker** (rule 5): challenged by GLM. Lines at stake: L257.

#### D6.9 · definition · Relabeling

Lines it formalizes or quotes (from the brief): L257.

- **Mimo:** no point on this item.
- **GLM** (reply line 23; challenges): The maths' reading is the only one of the register's under which L257 can hold, and even it needs the (A) amendment (see I26 and (b)).
  - Proposal `G7-B6` (reply lines 70–72), would change L257:

````
A relabeling is an edit \(a\) such that at every pair \((a,b)\) of the contract the target's answer to \(\mathcal Q\) is determined and equal to its answer at the baseline pair.
````

  - Proposal `G7-B4` (reply lines 52–54), would change L257:

````
A contract consisting only of relabelings, or excluding every change under which the active commitments could matter to \(\mathcal Q\), admits no candidate that answers as the target does and meets non-circular dependence
````

- **Goes to a checker** (rule 5): challenged by GLM. Lines at stake: L257.

#### D6.10 · definition · Tables

Lines it formalizes or quotes (from the brief): L269.

- **Mimo** (reply line 17; challenges): The words allow several components in a table; I32 encodes one active component whose counterpart is the whole target; the narrowing changes nothing found; no change.
  - Quotations: “no component whose relation is replaced by an intervention” — found at L269.
- **GLM** (reply line 25; does not challenge): I32's fixed relation matches "no component whose relation is replaced by an intervention"; FC25 (a) says what the amended wording says; (b) is broken by an artefact.
  - Quotations: “no component whose relation is replaced by an intervention” — found at L269.
- **Goes to a checker** (rule 5): challenged by Mimo. Lines at stake: L269.

#### E1 · encoding · The pole and its shadow

Lines it formalizes or quotes (from the brief): L325.

- **Mimo** (reply line 31; does not challenge): Nothing to add: the pole's encoding is I65 (under (c)).
- **GLM** (reply line 117; does not challenge): Nothing further to add as such (treated under I65).
- **Goes to no checker**: no point challenges it and it is not one of the twelve; recorded under rule 7 below.

#### FC21 · claim · A contract of relabelings admits no candidate meeting (A) and non-circular dependence

Lines it formalizes or quotes (from the brief): L257.

- **Mimo** (reply line 19; challenges): The formal needs (A) where L257 says "admits no candidate that meets non-circular dependence" (the gap is (b)'s); the second clause is rendered as ¬NC2 by definition, so that half is analytic, not searched; no change there.
  - Proposal `M7-B3` (reply lines 37–39), would change L257:

````
L257 | A contract consisting only of relabelings — edits under which the target's answer to \(\mathcal Q\) does not change — or excluding every change under which the active commitments could matter to \(\mathcal Q\), admits no candidate that meets (A) and non-circular dependence.
````

  - Quotations: “admits no candidate that meets non-circular dependence” — found at L257; “excluding every change under which the active commitments could matter to \(\mathcal Q\)” — found at L257.
- **Mimo** (reply lines 35–39; challenges): FC21 (b)'s witness (on a contract of relabelings a candidate whose own answers vary meets NC2, since (A) is not assumed) is a counterexample to L257 read literally, not to a text where "candidate" means one meeting (E); the text uses "candidate" both ways; proposes a new L257 (writes I26's reading of "relabelings" in, naming I26).
  - Proposal `M7-B3` (reply lines 37–39; printed in full under FC21 above), would change L257.
  - Quotations: “admits no candidate that meets non-circular dependence” — found at L257; “candidate” — found at L8, L17, L49, L69 and 26 more lines; “relabelings” — found at L257.
- **Mimo** (reply line 69; challenges): Hand model under I26's automorphism reading: an edit exchanging two components' values is a relabeling, and E = D meets (A) and NC2 on that contract; FC21 held because I26 chose answer-constancy; the L257 wording removes the lever (rests on I26 (a), I03, I78's free edits).
  - Proposal `M7-B3` (reply lines 37–39; printed in full under FC21 above), would change L257.
- **GLM** (reply line 27; challenges): The formal (a) says what the sentence says only with (A) in the antecedent; the sentence as written is refuted by the (b) witness.
  - Proposal `G7-B4` (reply lines 52–54; printed in full under D6.9 above), would change L257.
- **GLM** (reply lines 50–55; challenges): FC21 (b)'s witness refutes the sentence under any reading of "relabeling", since NC2 concerns the candidate's own answers; the sentence must demand agreement; proposes a new L257 sentence.
  - Proposal `G7-B4` (reply lines 52–54; printed in full under D6.9 above), would change L257.
  - Quotations: “relabeling” — found at L257.
- **GLM** (reply line 101; does not challenge): Near holds-by-construction with (A) and I26; the search adds models, not strength.
  - Quotations: “holds by construction” — not found in the text; found in the brief.
- **Goes to a checker** (rule 5): challenged by GLM and Mimo. Lines at stake: L257.

#### FC25 · claim · Tables: a fixed table fails (F1) where the projection moves; an encoding table meets it

Lines it formalizes or quotes (from the brief): L269.

- **Mimo** (reply line 21; challenges): Part (a)'s biconditional is what the definitions give and is narrower than "fails (F1) under any contract containing one"; part (b) matches "it meets (F1) as a decomposition does" except where D has a port in no footprint (both in (b)).
  - Proposal `M7-B4` (reply lines 43–45), would change L269:

````
L269 | A **table of observed answers** has no component whose relation is replaced by an intervention; it fails (F1) under any contract containing an intervention that changes what it records.
````

  - Quotations: “fails (F1) under any contract containing one” — found at L269; “it meets (F1) as a decomposition does” — found at L269.
- **Mimo** (reply lines 41–45; challenges): FC25 (a)'s witness stands (a setting edit that does not move what the table records leaves it faithful; the second check built another) and tells against the text: "under any contract containing one" does not hold; proposes a new L269.
  - Proposal `M7-B4` (reply lines 43–45; printed in full under FC25 above), would change L269.
  - Quotations: “under any contract containing one” — found at L269.
- **Mimo** (reply line 47; does not challenge): FC25 (b) (a port of D in no footprint cannot be carried by λ) tells against I14 and U2, not the text, which says nothing of ports no component touches; no text change; the invention should extend V_N to the whole port set.
  - Quotations: “it meets (F1) as a decomposition does” — found at L269.
- **GLM** (reply line 29; challenges): Part (a)'s first bullet matches; the witness refutes "under any contract containing one"; part (b) fails on a port in no footprint, an artefact of I14 with U2.
  - Proposal `G7-B3` (reply lines 45–47), would change L269:

````
A **table of observed answers** has no component whose relation is replaced by an intervention; it fails (F1) under any contract containing an intervention that changes the target's answers on the table's ports.
````

  - Quotations: “under any contract containing one” — found at L269.
- **GLM** (reply line 41; does not challenge): FC25 (b), the free port: against the inventions (I14's V_N from footprints, with U2), not the text; the fix belongs to the maths (V_N = V_D, or U2 as "no candidate at all"); the claim should carry the condition its result names; no text change.
  - Quotations: “meets (F1) as a decomposition does” — found at L269; “no candidate at all” — not found in the text; found in the brief; “E_enc meets (F1) on every C” — not found in the text; found in the brief.
- **GLM** (reply lines 43–48; challenges): FC25 (a), the faithful table, tells against the text: an intervention on a port the table does not read, or to its baseline value, leaves it meeting (F1); response to intervention is (F2)'s business (L271); proposes a new L269.
  - Proposal `G7-B3` (reply lines 45–47; printed in full under FC25 above), would change L269.
  - Quotations: “under any contract containing one” — found at L269.
- **GLM** (reply line 103; does not challenge): (a): the equivalence follows from L_k fixed at the baseline projection; robust at any size.
- **Goes to a checker** (rule 5): challenged by GLM and Mimo; one of the twelve counterexamples the second check reproduced (FC25 (b)). Lines at stake: L269.

#### FC29 · claim · A contrast no admitted edit realizes witnesses nothing

Lines it formalizes or quotes (from the brief): L275.

- **Mimo** (reply line 23; challenges): The formal drops "substantive" and reads "no edit the target admits realizes" as "off τ[C]"; since C ⊆ A_D × B_D the conclusion follows; the formal also covers an admitted edit excluded by a stated scope, on which the sentence is silent; the words stand; no change.
  - Quotations: “substantive” — found at L159, L273, L275, L455; “no edit the target admits realizes” — found at L275; “off \(\tau[C]\)” — not found in the text; found in the brief; “the target admits” — found at L257, L275, L343.
- **Mimo** (reply line 77; does not challenge): Nothing to break: every pair of C is an admitted edit.
  - Quotations: “substantive” — found at L159, L273, L275, L455; “admits” — found at L8, L11, L41, L43 and 17 more lines.
- **GLM** (reply line 31; does not challenge): The formal is the sentence with a weaker hypothesis; the sentence holds; no change.
  - Quotations: “realizes” — found at L275.
- **GLM** (reply line 105; does not challenge): Holds by construction (NC2 quantifies over τ[C]); rests on I12's reading.
  - Quotations: “varies against the baseline” — not found in the text; not in the brief; “varies at all on τ[C] ∪ {x0}” — not found in the text; not in the brief.
- **Goes to a checker** (rule 5): challenged by Mimo. Lines at stake: L275.

#### FC26 · claim · The pole: the forward organization meets (E) on the production contract

Lines it formalizes or quotes (from the brief): L325.

- **Mimo** (reply line 25; challenges): The formal tests C1 and C2, while L325's "this contract" is the production contract and the lines given say only "intervening on the upstream port"; C2 and the look's C3 are the invention's; the text does not say which edits the production contract holds; nothing endangers the claim.
  - Quotations: “this contract” — found at L325, L626, L630; “intervening on the upstream port” — found at L271.
- **Mimo** (reply line 49; challenges): The look (not as expected) is no counterexample to L325, which holds on C1, C2 and C3; NC1 did not fail on settings of L because D6.3 wants a slot at every pair; the surprise lies in the reading of L255, which the D6.3 proposal removes.
  - Proposal `M7-B2` (reply lines 11–13; printed in full under D6.3 above), would change L255.
- **Mimo** (reply line 71; does not challenge): Two levers, no break: the hand-set transport, and I92's grid.
- **GLM** (reply line 33; does not challenge): Matches given I65's contract and D6.3's NC1 reading, both at issue below; the quoted lines do not show whether the production contract includes settings of L.
- **GLM** (reply lines 57–62; challenges): The look exposes D6.3's unrecorded every-pair choice; under the some-pair reading the forward organization fails NC1 on any contract with settings of L, which may be what the words want, but then L325 depends on the production contract excluding them; recommends the some-pair reading with an exemption for components the contract's own edit replaces; proposes a new first sentence of L255 (writes the unrecorded choice in, kin to I24).
  - Proposal `G7-B5` (reply lines 59–61; printed in full under D6.3 above), would change L255.
- **GLM** (reply line 107; challenges): Two attacks: the non-vacuity leg is never tested under I85, and the text should say where the scope is stated (I27's part); and a hand model against D6.3's every-pair form: a candidate component m is the target's answer at the edited pair but not at the baseline, so NC1 holds and (E) holds while the answer appears as a component, against L255; under the reader's L255 wording NC1 fails and the computed results stand (rests on the unrecorded every-pair form, I12, I21, I03, I04).
  - Proposal `G7-B5` (reply lines 59–61; printed in full under D6.3 above), would change L255, L257.
  - Quotations: “not silently” — found at L257, L363.
- **Goes to a checker** (rule 5): challenged by GLM and Mimo. Lines at stake: L255, L257.

#### FC27 · claim · The pole: the reversed calculation fails (F2) on the production contract

Lines it formalizes or quotes (from the brief): L271, L325.

- **Mimo** (reply line 27; challenges): The formal fixes τ(set H := h) = set H := h; the words presuppose that the intervention is carried to the calculation's H; the clause is that presupposition written down (I65, I92), not settled by these lines (see (d)).
  - Quotations: “intervening on \(H\) changes the target's \(L\) but not the calculation's” — found at L325.
- **Mimo** (reply line 73; challenges): Hand model: a transport carrying set H := h to set L := h cot θ makes E_rev meet (F1) and (F2) at the image pair; the failure of (F2) rests on carrying an intervention on a port to an intervention on the corresponding port, which the words already presuppose, so the text stands and the maths should state the clause (rests on I65/I92's identity transport, I04).
  - Quotations: “intervening on \(H\) … but not the calculation's” — found at L325.
- **GLM** (reply line 35; does not challenge): Matches directly; the computed divergence is the one the words assert.
- **GLM** (reply line 109; does not challenge): Definitional; nothing found beyond the bounds.
  - Quotations: “translates C” — not found in the text; found in the brief.
- **Goes to a checker** (rule 5): challenged by Mimo. Lines at stake: L271, L325.

#### FC28 · claim · The pole: the reversed calculation meets (F1), (F2), (A) on the identification contract

Lines it formalizes or quotes (from the brief): L325.

- **Mimo** (reply line 29; challenges): The formal matches L325 only under I65's reading of "edits that alter the observed L" as boundary changes; the look shows the other reading undoes the claim (wording in (b)).
  - Proposal `M7-B5` (reply lines 53–55), would change L325:

````
L325 | It is faithful under the identification contract, whose edits change what is observed of \(L\) rather than setting it, and whose question asks which \(H\) goes with the observed \(L\).
````

  - Quotations: “edits that alter the observed \(L\)” — not found in the text; found in the brief.
- **Mimo** (reply lines 51–55; challenges): The look: with edits that set L, E_rev fails (F1), (F2) and (A), and the encoded query returns {H : H cot θ = l}, not every H; not a counterexample to the text, which does not fix what the identification contract's edits are, but to the setting reading; the claim's scope is open as the line stands; proposes a new L325 sentence (writes I65's reading and the I65/I92 question in, naming them).
  - Proposal `M7-B5` (reply lines 53–55; printed in full under FC28 above), would change L325.
- **Mimo** (reply line 75; does not challenge): No break within I65's reading; the levers are the contract's reading and the transport point of FC27.
- **GLM** (reply line 37; challenges): Matches only under I65's reading of "whose edits alter the observed L" (see (b), (c)).
  - Proposal `G7-B7` (reply lines 77–79), would change L325:

````
It is faithful under the identification contract, whose pairs vary the exogenous \(U_H\) so that the observed \(L\) alters with it, and which holds no edit that sets any port.
````

  - Quotations: “whose edits alter the observed L” — found at L325.
- **GLM** (reply line 64; challenges): The look: under I65's boundary reading, which L325's stipulation H := U_H bears out, no counterexample; but "whose edits alter the observed L" admits the setting reading, under which L325 fails outright; the words must pin the mechanism (wording under I65).
  - Proposal `G7-B7` (reply lines 77–79; printed in full under FC28 above), would change L325.
  - Quotations: “whose edits alter the observed L” — found at L325.
- **GLM** (reply line 111; challenges): Hand model: varying u_θ as well leaves E_rev faithful, but one edit setting θ makes (F1) fail (target L = √3/3, E_rev's L = 1); L325 fails for any contract that both varies boundaries and holds a setting; the I65 wording removes this.
  - Proposal `G7-B7` (reply lines 77–79; printed in full under FC28 above), would change L325.
  - Quotations: “alters the observed L” — not found in the text; not in the brief.
- **Goes to a checker** (rule 5): challenged by GLM and Mimo. Lines at stake: L325.

#### I26 · invention · 'Relabelings'

Lines it formalizes or quotes (from the brief): L257.

- **Mimo** (reply line 59; challenges): Not fixed: "relabelings" and nothing more; the L257 proposal writes I26's reading in and excludes its alternatives.
  - Proposal `M7-B3` (reply lines 37–39; printed in full under FC21 above), would change L257.
  - Quotations: “relabelings” — found at L257.
- **GLM** (reply lines 68–73; challenges): Not settled: "relabeling" occurs once, undefined; the automorphism reading lets the contract hold contrasts, the no-relation-change reading falls to FC21 (b), the answer-invariance reading carries the point once (A) is added; proposes a new sentence at L257 (writes I26 in).
  - Proposal `G7-B6` (reply lines 70–72; printed in full under D6.9 above), would change L257.
  - Quotations: “relabeling” — found at L257.
- **Goes to a checker** (rule 5): challenged by GLM and Mimo. Lines at stake: L257.

#### I65 · invention · The pole and its shadow, encoded

Lines it formalizes or quotes (from the brief): L325.

- **Mimo** (reply line 61; challenges **OWNER QUESTION**): Partly fixed: the law and the two contracts are fixed; the identification contract's edits are not (the L325 wording); whether U_H, U_θ are ports or boundary values (I65 (a)) the reader calls "where values are placed, the owner's question" and makes no proposal (read as where the exogenous values sit); the production contract's edits should stay open (FC26 holds on C1, C2, C3).
  - Proposal `M7-B5` (reply lines 53–55; printed in full under FC28 above), would change L325.
- **GLM** (reply lines 75–80; challenges): "H:=U_H, θ:=U_θ" makes the exogenous values boundary-borne; the identification contract's edits are not settled, and under the setting reading L325 fails; proposes a new L325 sentence (writes I65's choice in; "no edit that sets any port" also blocks the θ-setting extension in (d)); grids and finite stand-ins need no text.
  - Proposal `G7-B7` (reply lines 77–79; printed in full under FC28 above), would change L325.
  - Quotations: “H:=U_H, θ:=U_θ” — found at L325; “No edit that sets any port” — not found in the text; not in the brief.
- **Goes to a checker** (rule 5): challenged by GLM and Mimo. Lines at stake: L325.
- Marks: OWNER QUESTION points present.

#### I92 · invention · The pole in exact arithmetic, with its grids, baseline, contracts and fibre query

Lines it formalizes or quotes (from the brief): L325.

- **Mimo** (reply line 63; challenges): Not fixed and should stay open (grids, baseline, exact values, contracts, the fibre query); one point is fixed by the L325 wording: when L is set, the identification question asks which H goes with that value, answered by {l tan θ} ∩ X_H, not every H.
  - Proposal `M7-B5` (reply lines 53–55; printed in full under FC28 above), would change L325.
- **GLM** (reply line 82; challenges): Mostly should stay open; one part the text should settle: what the fibre query returns when the target does not determine H singly (the program answers ⊥); the reader relies on FC28's statement of the fibre sentence (not quoted); if it leaves the non-single case open it should say "and not determined otherwise".
  - Inline proposal (reply line 82; written in the reader's running text, not in a fence), would change L325 — a phrase for the fibre sentence; the reader names no line of the text for it, relying on FC28's statement:

````
and not determined otherwise
````

  - Quotations: “every H” — not found in the text; found in the brief; “and not determined otherwise” — not found in the text; not in the brief.
- **Goes to a checker** (rule 5): challenged by GLM and Mimo. Lines at stake: L325.

#### I03 · invention · Ports and components are fixed; deletion and absence are the full relation

Lines it formalizes or quotes (from the brief): L103, L339.

- **Mimo:** no point on this item.
- **GLM** (reply lines 84–89; challenges): The reader says the text never says what deletion does, and NC2 turns on it (L103 and L255 as they stand contain "a deleted component imposes the full relation on its ports"); proposes a sentence at L255 (writes I03's deletion half in).
  - Proposal `G7-B8` (reply lines 86–88), would change L255:

````
Deleting a component removes its constraint and changes nothing else in \(E\).
````

- **Goes to a checker** (rule 5): challenged by GLM. Lines at stake: L255.

#### I04 · invention · Setting a port: a surgical edit, and the assigning component read off the edits

Lines it formalizes or quotes (from the brief): L103, L109, L119.

- **Mimo:** no point on this item.
- **GLM** (reply line 91; challenges): The D2.1 proposal writes in what L103 leaves open.
  - Proposal `G7-B1` (reply lines 7–9; printed in full under D2.1 above), would change L103.
- **External reader and case card:** E04 (the external reader) challenges the sentence this item formalizes (section 3 below).
- **Goes to a checker** (rule 5): challenged by GLM; challenged by E04 (the external reader). Lines at stake: L103.

#### I14 · invention · Subnetworks, their solutions, and port translations with value maps

Lines it formalizes or quotes (from the brief): L189, L233.

- **Mimo:** no point on this item.
- **GLM** (reply line 93; does not challenge): Not the text's to settle; V_N = V_D for the full subnetwork is a change to the invention.
- **Goes to no checker**: no point challenges it and it is not one of the twelve; recorded under rule 7 below.

#### I32 · invention · A table of observed answers: its counterpart and its relation

Lines it formalizes or quotes (from the brief): L269.

- **Mimo:** no point on this item.
- **GLM** (reply line 95; challenges): The fixed relation is settled by L269's first clause; the counterpart being the whole target is bookkeeping the text need not fix; leave open.
- **Goes to a checker** (rule 5): challenged by GLM. Lines at stake: L269.

#### U2 · U-entry · An ill-formed λ(k) counts as a failure of (F1)

Lines it formalizes or quotes (from the brief): L269.

- **Mimo** (reply line 65; does not challenge): Not fixed; should stay open (how the program scores an ill-formed port translation); under either choice FC25 (b) is not as stated; the change is I14's.
- **GLM** (reply line 97; does not challenge): The text settles nothing; record it and take "no candidate at all"; either way FC25 (b) fails as stated; the condition belongs to the claim.
  - Quotations: “no candidate at all” — not found in the text; found in the brief.
- **Goes to no checker**: no point challenges it and it is not one of the twelve; recorded under rule 7 below.

#### Part 7: items no point addresses

Items of this part on which neither reader made any point (both replies read whole): none. Each is recorded under rule 7 in section 6 unless a point on it in another part sends it to a checker.

### Part 8: Identification, obstruction, removed structure, skew-symmetric matrices

Brief: `tests/S104 Round 2 - the maths against the words - part 08, Identification, obstruction, removed structure, skew-symmetric matrices.md`. Replies: `s104_maths_mimo_8.response.txt` (Mimo), `s104_maths_glm_8.response.txt` (GLM).

#### D6.3 · definition · NC1 (no answer slot)

Lines it formalizes or quotes (from the brief): L255.

- **Mimo** (reply line 5; challenges): L255 also carries "Identity of that assertion with the target's answer is structural at the declared grain, not the indiscriminate identification of all logically equivalent mathematical statements", which no clause of D6.3 states; the words should stand (they add a constraint the maths leaves to I24 and I28); no proposal.
  - Quotations: “Identity of that assertion with the target's answer is structural at the declared grain, not the indiscriminate identification of all logically equivalent ma…” — found at L255.
- **GLM** (reply line 5; challenges): The maths requires the slot relation to be exactly the answer "and constrain nothing else", while the words ("does not appear … as a component"; "structural at the declared grain"; the "law" sentence) catch a component whose relation entails the answer and also does other work; the words should stand and the maths widen to entailment.
  - Quotations: “does not appear … as a component” — found at L255; “identity of that assertion with the target's answer is structural at the declared grain” — found at L255; “and constrain nothing else” — not found in the text; not in the brief; “moving an assertion from an input slot into a component named 'law' does not discharge this” — found at L255.
- **External reader and case card:** E19 (the external reader) challenges the sentence this item formalizes (section 3 below).
- **Goes to a checker** (rule 5): challenged by GLM and Mimo; challenged by E19 (the external reader). Lines at stake: L255.

#### D6.4 · definition · NC2 (a contrast lost under deletion)

Lines it formalizes or quotes (from the brief): L255.

- **Mimo** (reply line 7; does not challenge): Contrast and Lost match; "in the claimed way" collapsed to one ⊥ is I22's recorded choice, not a divergence.
  - Quotations: “differs” — found at L45, L245, L255, L397 and 2 more lines; “is not determined at x in the claimed way” — not found in the text; not in the brief; “in the claimed way” — found at L255.
- **GLM** (reply lines 7–11; challenges **OWNER QUESTION**): Faithful, including the asymmetry (only undeterminedness at the edit point counts as a contrast); "whether the words want that asymmetry is the owner's"; gives a wording if not, and proposes nothing "until the owner says whether the baseline is meant to be the point that is always determined".
  - Proposal `G8-B1` (reply lines 9), would change L255:

````
> L255 | There exist \((a,b)\in C\) and a nonempty block \(G\subseteq\Gamma\) such that the answer of \(E\) at \((\tau(a),\sigma(b))\) differs from its answer at \((1,\sigma(b_0))\), or is not determined at one of these points in the claimed way while determined at the other, and this contrast is lost when the components of \(G\) are deleted from \(E\)
````

- **Goes to a checker** (rule 5): challenged by GLM. Lines at stake: L255.
- Marks: OWNER QUESTION points present.

#### E2 · encoding · Identification

Lines it formalizes or quotes (from the brief): L329.

- **Mimo:** no point on this item.
- **GLM** (reply line 27; does not challenge): Nothing to add.
  - Quotations: “relation is full” — found at L339.
- **Goes to no checker**: no point challenges it and it is not one of the twelve; recorded under rule 7 below.

#### E4 · encoding · Obstruction

Lines it formalizes or quotes (from the brief): L335.

- **Mimo:** no point on this item.
- **GLM** (reply line 27; does not challenge): Nothing to add.
  - Quotations: “relation is full” — found at L339.
- **Goes to no checker**: no point challenges it and it is not one of the twelve; recorded under rule 7 below.

#### E5 · encoding · Explanation that removes structure

Lines it formalizes or quotes (from the brief): L339.

- **Mimo:** no point on this item.
- **GLM** (reply line 27; does not challenge): Matches its sentence under I03 (the text's own "relation is full").
  - Quotations: “relation is full” — found at L339.
- **Goes to no checker**: no point challenges it and it is not one of the twelve; recorded under rule 7 below.

#### E6 · encoding · Odd-order skew-symmetric matrices

Lines it formalizes or quotes (from the brief): L343.

- **Mimo:** no point on this item.
- **GLM** (reply line 27; does not challenge): E6 is I66 (under (c)).
  - Quotations: “relation is full” — found at L339.
- **Goes to no checker**: no point challenges it and it is not one of the twelve; recorded under rule 7 below.

#### FC57 · claim · (I2): identified at every attainable value exactly when the feature factors through the measurement

Lines it formalizes or quotes (from the brief): L329.

- **Mimo** (reply lines 9–17; challenges): The maths writes "on Z"; the words do not say on what domain f = f̄ ∘ g holds; the maths should stand and the sentence fix it; proposes new wording in L329 (writes I64 in, adds "on Z").
  - Proposal `M8-B1` (reply lines 11–13), would change L329 — the reader's own quotation, in a fence, of the words to be replaced:

````
> L329 | It is identified on every attainable \(y\) exactly when \(f=\bar f\circ g\) for some \(\bar f\).
````

  - Proposal `M8-B2` (reply lines 14–16), would change L329:

````
Write \(Z_y=\{z\in Z:g(z)=y\}\); \(y\) is attainable when \(Z_y\neq\varnothing\). It is identified on every attainable \(y\) exactly when \(f=\bar f\circ g\) on \(Z\) for some \(\bar f\).
````

- **Mimo** (reply line 93; challenges): Dropping I64's "attainable" breaks it (empty fibres), which shows the word is load-bearing though no counterexample to L329; reading f = f̄ ∘ g on the domain of f rather than on Z can break the ⟸ direction (hand model); the maths' "on Z" avoids this and the proposal writes it in.
  - Proposal `M8-B2` (reply lines 14–16; printed in full under FC57 above), would change L329.
  - Quotations: “attainable” — found at L329.
- **GLM** (reply line 13; does not challenge): Says the sentence; a set-theoretic theorem (see (d)).
- **GLM** (reply line 61; does not challenge): Cannot be broken inside or beyond the bounds (an argument given by hand).
- **Goes to a checker** (rule 5): challenged by Mimo. Lines at stake: L329.

#### FC58 · claim · (I3): the kernel criterion; repeated rows; an independent calibration

Lines it formalizes or quotes (from the brief): L329.

- **Mimo** (reply lines 19–26; challenges): The maths reads "an independent calibration" as "a row outside the row space"; a calibration can land inside the row space and leave the kernel alone; the words are looser than the maths, which should stand; proposes new wording in L329.
  - Proposal `M8-B3` (reply lines 21–23), would change L329 — the reader's own quotation, in a fence, of the words to be replaced:

````
> L329 | Repeating rows changes no kernel; an independent calibration can.
````

  - Proposal `M8-B4` (reply lines 24–26), would change L329:

````
Repeating rows, or adding any row in the row space, changes no kernel; a calibration whose row lies outside the row space lowers the dimension of the kernel by one.
````

  - Quotations: “Repeating rows changes no kernel; an independent calibration can” — found at L329; “an independent calibration” — found at L329; “a row outside the row space” — not found in the text; not in the brief.
- **Mimo** (reply line 95; challenges): On a proper Z the kernel criterion is sufficient but not necessary (hand model: Z = {(0,0),(1,0),(2,0)}, g = x + y, f = x − y); rests on I64's alternative (a); L329's "For linear g and linear feature c^⊤" does not restrict Z; the reader says "the proposal's 'In the linear case Z = ℝ^n'" removes the mismatch (the reply contains no proposal with those words).
  - Quotations: “For linear g and linear feature c^⊤” — found at L329; “In the linear case Z = ℝ^n” — not found in the text; not in the brief.
- **GLM** (reply line 15; challenges): Says the sentence; the look shows the sentence as written fails if the admitted states are a proper subset, a matter for I64, not a fault of the formal statement.
  - Proposal `G8-B3` (reply lines 45), would change L329:

````
> L329 | For linear \(g\) and linear feature \(c^\top\), with the admitted states the whole space, identification is \(\ker g\subseteq\ker c^\top\); on a proper set of admitted states the criterion is sufficient, and at a single attainable \(y\) it need not be.
````

- **GLM** (reply line 63; does not challenge): Holds over any field and dimension; the only break is the proper-subset one, which belongs to I64's alternative.
  - Quotations: “Repeating rows changes no kernel” — found at L329.
- **Goes to a checker** (rule 5): challenged by GLM and Mimo. Lines at stake: L329.

#### FC59 · claim · The two balances

Lines it formalizes or quotes (from the brief): L331.

- **Mimo** (reply line 28; does not challenge): Computed as claimed; the maths matches the words.
- **Mimo** (reply line 97; does not challenge): Repeated readings would identify neither quantity, but the setup is fixed at L331; not a counterexample.
- **GLM** (reply line 17; does not challenge): Says the sentence; checked by hand.
- **GLM** (reply line 65; does not challenge): Nothing further to attack.
- **Goes to no checker**: no point challenges it and it is not one of the twelve; recorded under rule 7 below.

#### FC60 · claim · Setting a bias from the favoured mass: where the circularity can be registered

Lines it formalizes or quotes (from the brief): L331.

- **Mimo** (reply line 30; challenges): The words say the choice "is not an inference from the readings; it is circular"; formal (a) says only that (E) and NC1 cannot tell the two candidates apart, a claim about the framework's blindness; (b) registers the circularity via MadeFrom; the words stand as a claim about the choice; no proposal at L331.
  - Quotations: “is not an inference from the readings; it is circular” — found at L331.
- **Mimo** (reply line 99; does not challenge): Dropping I39's structural reading of "among its premises" lets the argument rule out x ≠ m*; rests on I39; L397's "read structurally" is on the invention's side; no change.
  - Quotations: “among its premises” — found at L8, L397; “read structurally as non-circular dependence reads identity (Part V)” — found at L397.
- **GLM** (reply line 19; does not challenge): Says the sentence and puts its two halves where the words put them; (E) not reading how a boundary value was chosen matches S25–S27.
  - Quotations: “not an inference from the readings” — found at L331; “it is circular” — found at L331.
- **GLM** (reply line 67; challenges): (a) stands; for (b), with a second premise the block depends on D9.7's exact clause and on essentiality: I89's filling makes every premise essential, so it blocks, while under I89's alternative (a) an assessor could make the record premise inessential and the argument would rule out x ≠ m*; so "it is circular" is carried by the maths only under the filling.
  - Quotations: “it is circular” — found at L331.
- **Goes to a checker** (rule 5): challenged by GLM and Mimo. Lines at stake: L331.

#### FC61 · claim · (O1): an invariant blocks paths; equal values do not give paths; twenty-three tokens

Lines it formalizes or quotes (from the brief): L335.

- **Mimo** (reply line 32; does not challenge): All three parts match; (c) is arithmetic beside (a) and (b).
- **Mimo** (reply line 101; does not challenge): (b) needs at least two states; beyond the bounds the statement stands.
  - Quotations: “there are R, I, z, z'” — not found in the text; found in the brief.
- **GLM** (reply line 21; does not challenge): Says the sentence, with (O1) naming the first clause per I63.
- **GLM** (reply line 69; does not challenge): Holds (hand witness for (b) with four tokens).
- **Goes to no checker**: no point challenges it and it is not one of the twelve; recorded under rule 7 below.

#### FC62 · claim · Eliminative explanation: the rival's structure as a deleted counterpart

Lines it formalizes or quotes (from the brief): L339.

- **Mimo** (reply lines 34–41; challenges): "Their absence leaves both unchanged": unchanged from what? the maths reads it as (F1) at the baseline pair, trivially met; the maths' reading should stand and the words say it; proposes new wording in L339.
  - Proposal `M8-B5` (reply lines 36–38), would change L339 — the reader's own quotation, in a fence, of the words to be replaced:

````
> L339 | An account is faithful when introducing those components changes the answer in \(E\) as it does in \(D\), and their absence leaves both unchanged.
````

  - Proposal `M8-B6` (reply lines 39–41), would change L339:

````
An account is faithful when introducing those components changes the answer in \(E\) as it does in \(D\), and their absence leaves both at the answer they gave before those components were introduced.
````

  - Quotations: “their absence leaves both unchanged” — found at L339.
- **Mimo** (reply line 103; challenges): Beyond the one-component set-up: with two drivers of the answer and E carrying one, deleting {k} does not lose the contrast, so NC2 with G = {k} does not witness (rests on I78's single-component encoding); L339 says "those components" and "a deleted subnetwork"; the words need no change; the formal should let G range over the counterparts of all introduced components.
  - Quotations: “those components” — found at L339; “a deleted subnetwork” — found at L339.
- **GLM** (reply line 23; does not challenge): Says the sentence.
  - Quotations: “Whose relation is full (Part II)” — found at L339.
- **GLM** (reply line 71; challenges **OWNER QUESTION**): No break, but a text-level risk: where D's answer takes few values, the rival's counterpart component can be exactly the answer port pinned to the target's answer, a slot, so NC1 fails E; the sentence does not say the counterpart is never a slot; "a boundary the owner may want the text to speak to"; no wording (it belongs with NC1).
  - Quotations: “E *can* meet (E)” — found at L606.
- **Goes to a checker** (rule 5): challenged by GLM and Mimo. Lines at stake: L339.
- Marks: OWNER QUESTION points present.

#### FC63 · claim · Odd-order skew-symmetric matrices

Lines it formalizes or quotes (from the brief): L343.

- **Mimo** (reply lines 43–51; challenges): (a) and (b) match; (c) does not: "The full Leibniz expansion with skewness substituted meets (F1) and (F2)" does not say what relation the sum component carries, and the candidate needs term ports D lacks, which I14 excludes; the maths shows the words ambiguous between two readings, one of which fails; proposes new wording in L343 (writes I99's variant (c-ii) in and admits I81's computed ports, a departure from I14).
  - Proposal `M8-B7` (reply lines 45–47), would change L343 — the reader's own quotation, in a fence, of the words to be replaced:

````
> L343 | The full Leibniz expansion with skewness substituted meets (F1) and (F2)
````

  - Proposal `M8-B8` (reply lines 48–50), would change L343:

````
The full Leibniz expansion with skewness substituted, its term ports read as functions of the matrix entries and its sum restricted to the tuples of term values some matrix gives, meets (F1) and (F2)
````

  - Quotations: “The full Leibniz expansion with skewness substituted meets (F1) and (F2)” — found at L343.
- **Mimo** (reply lines 55–57; challenges): FC63 (c-i): the sum relation read as every tuple of term values with its sum includes tuples no matrix gives, so (F1) fails at every pair; a counterexample to I99's choice, not to L343, whose words do not fix the relation; the L343 change removes it; the second failure (the candidate cannot be written under I14) is against I14 and the words' silence on D's ports, and the same change removes it.
  - Proposal `M8-B7` (reply lines 45–47; printed in full under FC63 above), would change L343 — the reader's own quotation, in a fence, of the words to be replaced.
  - Proposal `M8-B8` (reply lines 48–50; printed in full under FC63 above), would change L343.
- **Mimo** (reply line 105; does not challenge): Over GF(2), n = 1, M = [1] is skew-symmetric with det 1, so the theorem fails there; the contract holds field arithmetic fixed and the question is about ℝ, so this is against I66's choice (b) being excluded, not the words; in characteristic ≠ 2 the argument goes through.
- **GLM** (reply line 25; challenges): (a) and (b) say the sentences; (c-i) does not say "The full Leibniz expansion with skewness substituted meets (F1) and (F2)" (see (b)).
  - Quotations: “The full Leibniz expansion with skewness substituted meets (F1) and (F2)” — found at L343.
- **GLM** (reply lines 31–37; challenges **OWNER QUESTION**): FC63 (c-i) is a counterexample to an invention, not the text: "with skewness substituted" fixes that the terms are read off the matrix, so only realizable term tuples enter (hand check: the all-ones tuple needs 1 = −1 over the reals too); (c-ii) is the sentence's own candidate and meets (E); the second failure (computed ports excluded by I14) tells against I14, and I81's computed ports should become part of the core; no text change; "if the owner wants the terms' reading made explicit", a new L343 fragment.
  - Proposal `G8-B2` (reply lines 37), would change L343:

````
> L343 | The full Leibniz expansion, its terms read from the matrix entries, with skewness substituted meets (F1) and (F2)
````

  - Quotations: “The full Leibniz expansion *with skewness substituted*” — found at L343; “The expansion is an account” — found at L343; “only for the term ports of the Leibniz candidate” — not found in the text; found in the brief.
- **Goes to a checker** (rule 5): challenged by GLM and Mimo; one of the twelve counterexamples the second check reproduced (FC63 (c-i)). Lines at stake: L343.
- Marks: OWNER QUESTION points present.

#### I63 · invention · A tag such as (I2) names the sentence before it

Lines it formalizes or quotes (from the brief): L329, L335, L471.

- **Mimo** (reply lines 61–69; challenges): The words never say what a parenthesized tag names; at L471 only the "follows" reading works, L329 and L335 allow either; the invention is the only reading that survives all three; proposes new wording in L329 (writes I63 in).
  - Proposal `M8-B9` (reply lines 63–65), would change L329 — the reader's own quotation, in a fence, of the words to be replaced:

````
> L329 | The feature is identified at \(y\) exactly when \(Z_y\neq\varnothing\land|f[Z_y]|=1\). (I1)
````

  - Proposal `M8-B10` (reply lines 66–68), would change L329:

````
The feature is identified at \(y\) exactly when \(Z_y\neq\varnothing\land|f[Z_y]|=1\). Each parenthesized tag names the statement it follows; (I1) names this one.
````

  - Quotations: “follows” — found at L127, L255, L363, L455 and 1 more lines.
- **GLM** (reply line 41; challenges): Settled, by lines not given (L395, L471, where nothing follows the tag; the reader relies on the invention's statement); a tag names the sentence before it; no change.
- **Goes to a checker** (rule 5): challenged by GLM and Mimo. Lines at stake: L329.

#### I64 · invention · Identification: 'attainable', and the admitted states in the linear case

Lines it formalizes or quotes (from the brief): L329.

- **Mimo** (reply line 71; challenges): Not settled: "attainable" is undefined and the linear case's Z is unstated; the FC57 proposal writes I64 in.
  - Proposal `M8-B1` (reply lines 11–13; printed in full under FC57 above), would change L329 — the reader's own quotation, in a fence, of the words to be replaced.
  - Proposal `M8-B2` (reply lines 14–16; printed in full under FC57 above), would change L329.
  - Quotations: “attainable” — found at L329.
- **GLM** (reply lines 43–47; challenges): Not settled: nothing says the admitted states are the whole space in the linear case, and the look shows the kernel sentence fails without it (Z = {0,1}², g = x + y, f = x); proposes a new L329 sentence (writes I64 in).
  - Proposal `G8-B3` (reply lines 45; printed in full under FC58 above), would change L329.
- **Goes to a checker** (rule 5): challenged by GLM and Mimo. Lines at stake: L329.

#### I66 · invention · The odd-order skew-symmetric case, encoded

Lines it formalizes or quotes (from the brief): L343.

- **Mimo** (reply lines 73–81; challenges): Not settled on components (the words name the edits and what is held fixed, not what carries order, entries, determinant, invertibility); the field is fixed by "real"; GF(3) is a search bound; proposes new contract wording in L343 (writes I66's ports and components in).
  - Proposal `M8-B11` (reply lines 75–77), would change L343 — the reader's own quotation, in a fence, of the words to be replaced:

````
> L343 | Contract: remove skewness; remove oddness; remove both; field arithmetic and determinant–invertibility held fixed.
````

  - Proposal `M8-B12` (reply lines 78–80), would change L343:

````
Contract: order, matrix entries, determinant, invertibility as the components; skewness and oddness as the constraints; remove skewness; remove oddness; remove both; field arithmetic and determinant–invertibility held fixed.
````

- **GLM** (reply line 49; challenges): Partly settled: "real" and "field arithmetic … fixed" settle the field and exclude GF(2); GF(p), p odd, is a surrogate; the edits are settled by the contract line; the query's phrasing is not settled and can stay open; no change.
  - Quotations: “every odd-order *real* skew-symmetric matrix” — found at L343; “field arithmetic … fixed” — found at L343; “does the family contain an invertible matrix?” — not found in the text; found in the brief.
- **Goes to a checker** (rule 5): challenged by GLM and Mimo. Lines at stake: L343.

#### I87 · invention · Claims as propositional formulas, read structurally

Lines it formalizes or quotes (from the brief): L397.

- **Mimo** (reply line 83; does not challenge): "Read structurally … not by logical equivalence alone" constrains the reading but fixes no language; leave open.
  - Quotations: “read structurally … not by logical equivalence alone” — found at L397.
- **GLM** (reply line 51; challenges): Partly settled: "read structurally as non-circular dependence reads identity (Part V) and not by logical equivalence alone" settles a structural reading and, the reader holds, alternative (b) too; propositional against first-order can stay open.
  - Quotations: “Read structurally as non-circular dependence reads identity (Part V) and not by logical equivalence alone” — found at L397.
- **Goes to a checker** (rule 5): challenged by GLM. Lines at stake: L397.

#### I89 · invention · The inference forms: MP, MT, AND-introduction, AND-elimination and a free form

Lines it formalizes or quotes (from the brief): L387, L393.

- **Mimo** (reply line 85; does not challenge): "The inference form of u is one j admits" declares forms per assessor; leave open.
  - Quotations: “the inference form of u is one j admits” — found at L393.
- **GLM** (reply line 53; challenges): Not settled: "the inference form of u is one j admits" leaves the forms to the assessor; alternative (a) is the closer reading of the words and the five fixed forms are a filling that lets FC60 (b) hold; should stay open (S21 leaves what an agent does with its arguments to the agent).
  - Quotations: “the inference form of \(u\) is one \(j\) admits” — found at L393.
- **Goes to a checker** (rule 5): challenged by GLM. Lines at stake: L387, L393.

#### I99 · invention · The odd-order skew-symmetric case in GF(3), and the Leibniz candidate's sum component

Lines it formalizes or quotes (from the brief): L343.

- **Mimo** (reply line 87; challenges): Covered by the FC63 proposal.
  - Proposal `M8-B7` (reply lines 45–47; printed in full under FC63 above), would change L343 — the reader's own quotation, in a fence, of the words to be replaced.
  - Proposal `M8-B8` (reply lines 48–50; printed in full under FC63 above), would change L343.
- **GLM** (reply line 55; challenges **OWNER QUESTION**): The sum relation is settled by the words against (c-i); alternative (b), D given term ports, is not settled; the text should say which, by the wording in (b).
  - Proposal `G8-B2` (reply lines 37; printed in full under FC63 above), would change L343.
  - Quotations: “The expansion is an account” — found at L343.
- **Goes to a checker** (rule 5): challenged by GLM and Mimo. Lines at stake: L343.
- Marks: OWNER QUESTION points present.

#### I03 · invention · Ports and components are fixed; deletion and absence are the full relation

Lines it formalizes or quotes (from the brief): L103, L339.

- **Mimo:** no point on this item.
- **GLM** (reply line 23; challenges): (Given in another part.) "Whose relation is full (Part II)" at L339 is the text's own phrase, so I03's clause that a deleted component carries the full relation is the words' own here, not an invention.
  - Quotations: “Whose relation is full (Part II)” — found at L339.
- **Goes to a checker** (rule 5): challenged by GLM. Lines at stake: L103, L339.

#### Part 8: items no point addresses

Items of this part on which neither reader made any point (both replies read whole): E3, I27, I81, I82. Each is recorded under rule 7 in section 6 unless a point on it in another part sends it to a checker.

### Part 9: Routes, and active routes in a history

Brief: `tests/S104 Round 2 - the maths against the words - part 09, Routes, and active routes in a history.md`. Replies: `s104_maths_mimo_9.response.txt` (Mimo), `s104_maths_glm_9.response.txt` (GLM).

#### D7.1 · definition · Restriction

Lines it formalizes or quotes (from the brief): L231, L287.

- **Mimo** (reply lines 3–11; challenges): The words fix only that a restriction operation is declared, that E|W keeps the named background and that its commitments are W; the maths fixes deletion (I29); the words should stand (deletion is one declaration among others); the text should say that the operation is an input (I29 notes it is not among the declared inputs at L522; the reader relies on that note); proposes a new L287 (writes that the operation decides, not deletion).
  - Proposal `M9-B1` (reply lines 7–9), would change L287:

````
L287 | Fix \(\mathcal E\) and a declared restriction operation — one of the theory's declared inputs. For \(W\subseteq\Gamma\), let \(E|W\) retain the commitments in \(W\) with the named background fixed; the commitments of \(E|W\) are \(W\), and what becomes of the components carrying the other commitments is the declared operation's business.
````

- **GLM** (reply line 25; does not challenge): Named among the items with nothing to add.
- **External reader and case card:** E02 (the external reader) challenges the sentence this item formalizes (section 3 below).
- **Goes to a checker** (rule 5): challenged by Mimo; challenged by E02 (the external reader). Lines at stake: L287.

#### D7.2 · definition · Routes (S)

Lines it formalizes or quotes (from the brief): L290, L293.

- **Mimo** (reply line 75; does not challenge): Named among the items with nothing to add.
  - Quotations: “nonempty \(B\subseteq W\)” — found at L293.
- **GLM** (reply line 25; does not challenge): Named among the items with nothing to add.
- **Goes to no checker**: no point challenges it and it is not one of the twelve; recorded under rule 7 below.

#### D7.3 · definition · Critical block (B)

Lines it formalizes or quotes (from the brief): L296.

- **Mimo** (reply line 75; does not challenge): Named among the items with nothing to add ("nonempty B ⊆ W" of L293 is carried).
  - Quotations: “nonempty \(B\subseteq W\)” — found at L293.
- **GLM** (reply line 5; does not challenge): The maths adds ∅ ≠ B; harmless (L293 says "For nonempty B ⊆ W"); no change.
  - Quotations: “For nonempty B ⊆ W” — found at L293.
- **External reader and case card:** E02 (the external reader) challenges the sentence this item formalizes (section 3 below).
- **Goes to a checker** (rule 5): challenged by E02 (the external reader). Lines at stake: L296.

#### D7.4 · definition · Boundary (D)

Lines it formalizes or quotes (from the brief): L302.

- **Mimo** (reply lines 13–19; challenges): Nothing says that E_v is the candidate the edit v gives, nor what its transport and commitments are; the maths fills both in with no register entry; the words should stand, the gap is the text's, and the clause should be registered as an invention; proposes a new L302.
  - Proposal `M9-B2` (reply lines 17–19), would change L302:

````
L302 | For a declared family \(\mathcal V\) of organization edits, each \(v\in\mathcal V\) carries \(E\)'s transport \(t\) and commitments \(\Gamma\) to those of \(E_v\), the candidate \(v\) gives. \(\operatorname{Boundary}_{E,p}=\{(v,w)\in\mathcal V^2:\operatorname{Account}(E_v,p)\neq\operatorname{Account}(E_w,p)\}. \tag{D}\)
````

- **GLM** (reply lines 7–9; challenges): The definition's parenthesis on E_v's transport and commitments is a choice with alternatives recorded nowhere; L231 fixes the transport only for E|W; it should have an entry and the text should say what an edit does to t and Γ; proposes a new L302.
  - Proposal `G9-B1` (reply lines 9), would change L302:

````
> L302 | For each \(v\in\mathcal V\), \(E_v\) is \(E\) with the edit applied; the transport and commitments are those the edit names, and are those of \(E\) where it names none.
````

  - Quotations: “with E_v's transport and commitments those the edit carries t and Γ to (L231; the text does not fix them further)” — not found in the text; found in the brief.
- **Goes to a checker** (rule 5): challenged by GLM and Mimo. Lines at stake: L302.

#### D7.5 · definition · Contributory; globally indispensable

Lines it formalizes or quotes (from the brief): L305.

- **Mimo** (reply lines 21–27; challenges): L305 reads both as a definition ("exactly when") and as a claim under the finite monotone hypotheses; the maths separates them and should stand, since read as definitions they fail off the hypotheses (hand model: Γ = {a,b,c}, S = {{a},{a,b,c}}; c critical in {a,b,c} and not in ⋃min S); proposes a new sentence at L305.
  - Proposal `M9-B3` (reply lines 25–27), would change L305:

````
L305 | Call \(d\in\Gamma\) **contributory** when it is critical in some route (B), and **globally indispensable** when \(\Gamma\setminus\{d\}\notin\mathsf S_{E,p}\). **Finite monotone claim.** If \(\Gamma\) is finite, \(\mathsf S\) is upward closed, and \(\Gamma\in\mathsf S\), then \(d\) is contributory exactly when \(d\in\bigcup\min\mathsf S\), and \(d\) is globally indispensable exactly when \(d\in\bigcap\min\mathsf S\).
````

  - Quotations: “exactly when” — found at L231, L305, L313, L329 and 1 more lines.
- **GLM** (reply lines 11–13; challenges): Defining contributory by (B) and reading "exactly when d ∈ ⋃min S" as a theorem under the hypotheses is the right order (outside them the text's "exactly when" cannot be the definition); proposes new wording at L305 marking which clause is the definition.
  - Proposal `G9-B2` (reply lines 13), would change L305:

````
> L305 | then \(d\in\Gamma\) is **contributory** when \(\{d\}\) is critical in some route (B), and \(d\) is **globally indispensable**, \(\Gamma\setminus\{d\}\notin\mathsf S_{E,p}\); under these hypotheses \(d\) is contributory exactly when \(d\in\bigcup\min\mathsf S\), and globally indispensable exactly when \(d\in\bigcap\min\mathsf S\).
````

  - Quotations: “exactly when d ∈ ∪min S” — not found in the text; not in the brief; “exactly when” — found at L231, L305, L313, L329 and 1 more lines.
- **External reader and case card:** E02 (the external reader) challenges the sentence this item formalizes (section 3 below).
- **Goes to a checker** (rule 5): challenged by GLM and Mimo; challenged by E02 (the external reader). Lines at stake: L305.

#### D7.6 · definition · No work by itself

Lines it formalizes or quotes (from the brief): L313.

- **Mimo** (reply line 29; does not challenge): Reads the words correctly; d ∈ Γ omitted harmlessly; no change.
  - Quotations: “every route stays a route after \(d\) is added to it and after \(d\) is removed from it” — found at L313; “a candidate that has a route” — found at L313; “a commitment \(d\) of a candidate” — found at L313.
- **GLM** (reply line 15; does not challenge): Faithful; L313's two glosses are entailed; no change.
- **External reader and case card:** E02 (the external reader) challenges the sentence this item formalizes (section 3 below).
- **Goes to a checker** (rule 5): challenged by E02 (the external reader). Lines at stake: L313.

#### D11.1 · definition · Occurrence; event

Lines it formalizes or quotes (from the brief): L169.

- **Mimo** (reply line 31; challenges): "Event" is used and defined nowhere; "nonempty set of occurrences" (I45) is a reading, not content; the text has to change (wording under matter 2).
  - Proposal `M9-B9` (reply lines 133–135), would change L169:

````
L169 | An **occurrence** is a physically located carrier. An **event** is a nonempty set of occurrences of one history. A **content** is an organization together with its contract-relative commitments. Occurrences are not identified by carrying the same words; contents are not identified by having the same outputs.
````

  - Quotations: “nonempty set of occurrences” — not found in the text; found in the brief.
- **GLM** (reply line 25; does not challenge): Named among the items with nothing to add.
- **Goes to a checker** (rule 5): challenged by Mimo. Lines at stake: L169.

#### D11.2 · definition · Content

Lines it formalizes or quotes (from the brief): L169.

- **Mimo** (reply line 33; challenges): The words deny only output-identity; the maths positively compares contents by transports (D13.4, another part); the words should stand here (content identity by transports belongs where transports are defined); I48's triple matches "contract-relative commitments".
  - Quotations: “contract-relative commitments” — found at L169.
- **GLM** (reply line 25; does not challenge): Named among the items with nothing to add.
- **Goes to a checker** (rule 5): challenged by Mimo. Lines at stake: L169.

#### D11.3 · definition · History

Lines it formalizes or quotes (from the brief): L375.

- **Mimo** (reply lines 35–41; challenges): The words fix acyclicity and ⪯_h as ≺_h's reflexive closure; the maths makes ≺_h transitive (I44); under the words ⪯_h need not be transitive; the words should change; H19's additions (Org_ℓ(h), "subhistory") have no words and D11.4 needs Org_ℓ(h); proposes a new first sentence of L375 (writes I44, H19 and the timing and persistence I95 lists as an alternative).
  - Proposal `M9-B4` (reply lines 39–41), would change L375:

````
L375 | A history \(h\) is a set of occurrences with a causal precedence \(\prec_h\), irreflexive and transitive (write \(\preceq_h\) for its reflexive closure), and a physical interpretation supplying process occurrences, their ports, the connections actually instantiated, when each occurrence runs and what it produced that persists, and the organization \(\operatorname{Org}_\ell(h)\) of \(h\) at each grain \(\ell\). A subhistory is a subset of occurrences closed under the interpretation, with \(\prec_h\) restricted to it.
````

  - Quotations: “precedence” — found at L375; “subhistory” — found at L405, L409, L427, L435 and 1 more lines.
- **GLM** (reply line 17; challenges): "Acyclic" does not give transitivity (I44).
  - Proposal `G9-B4` (reply lines 45), would change L375:

````
> L375 | A history \(h\) is a set of occurrences with an acyclic, transitive causal precedence \(\prec_h\) (write \(\preceq_h\) for its reflexive closure) and a physical interpretation supplying process occurrences, their ports, and the connections actually instantiated.
````

  - Quotations: “Acyclic” — found at L375.
- **Goes to a checker** (rule 5): challenged by GLM and Mimo. Lines at stake: L375.

#### D11.4 · definition · Active route

Lines it formalizes or quotes (from the brief): L375.

- **Mimo** (reply lines 43–49; challenges): Three partings: the chain clause is an addition that excludes a connected route with a side component (model B), and the words should stand; the four phrases have no words; the dependence clause reads only the endpoints, so dependence may run outside R (model A), and "which has nonconstant dependence" should be read as carrying it; proposes a new active-route sentence in L375 (writes I46's phrases, drops its chain clause, adds the carrying clause).
  - Proposal `M9-B5` (reply lines 47–49), would change L375:

````
L375 | An **active route** for a result is a connected subnetwork of actual occurrences joining a represented input to an operative result: the represented input is an occurrence whose port carries a represented distinction, the operative result is a designated result occurrence, the applicable relations are the relations the physical interpretation gives the route's components at the declared grain, and the route has nonconstant dependence on the represented distinction under the declared contrasts — for some pair of the declared values of the input's port, the two values give different values at the result along the route's own connections.
````

  - Quotations: “every occurrence of \(R\) lies on a \(\prec_h\)-chain from \(i\) to \(r\) inside \(R\)” — not found in the text; found in the brief; “a connected subnetwork ... joining a represented input to an operative result” — found at L375; “which has nonconstant dependence” — found at L375.
- **GLM** (reply line 19; challenges): The "already at rest" clause is dropped (H11): the words say more and should stand; clause (c) reads "read from the history, not from the result" as "not of r's value alone", weaker but compatible; no change to the words.
  - Proposal `G9-B7` (reply lines 65), would change L375:

````
> A route is **at rest for** a result when every process occurrence of the route is complete before the process occurrence that carries the result begins; a route at rest for a result is not active for it, whatever of its product persists and feeds the result.
````

  - Quotations: “already at rest” — found at L375; “read from the history, not from the result” — found at L375; “not of r's value alone” — not found in the text; found in the brief.
- **Goes to a checker** (rule 5): challenged by GLM and Mimo. Lines at stake: L375.

#### D11.5 · definition · Occurring pairs

Lines it formalizes or quotes (from the brief): L217.

- **Mimo** (reply lines 51–57; challenges): The words say only "actually occurring"; the maths indexes a pair at a place ξ of a history; proposes a new L217.
  - Proposal `M9-B6` (reply lines 55–57), would change L217:

````
L217 | For an edit–boundary pair \((a,b)\in C\) actually occurring in the system's history:
````

  - Quotations: “actually occurring” — found at L217, L223.
- **GLM** (reply line 25; does not challenge): Named among the items with nothing to add.
- **Goes to a checker** (rule 5): challenged by Mimo. Lines at stake: L217.

#### FC37 · claim · The finite monotone claim

Lines it formalizes or quotes (from the brief): L305.

- **Mimo** (reply line 71; does not challenge): Matches, once D7.5's reading is fixed.
- **Mimo** (reply line 119; does not challenge): Hand argument for every finite Γ; the bound does not bind.
- **GLM** (reply line 25; does not challenge): Named among the items with nothing to add in (a).
- **GLM** (reply line 73; does not challenge): Holds for every finite Γ (argument given); the finiteness hypothesis is indispensable (hand model on ℤ), which confirms L305's conditioning and D7.5's order.
- **Goes to no checker**: no point challenges it and it is not one of the twelve; recorded under rule 7 below.

#### FC38 · claim · Redundant routes

Lines it formalizes or quotes (from the brief): L307.

- **Mimo** (reply line 75; does not challenge): Named among the items with nothing to add in (a).
  - Quotations: “nonempty \(B\subseteq W\)” — found at L293.
- **Mimo** (reply line 125; does not challenge): Realized (a and b each the constraint x = 0); survives.
- **GLM** (reply line 25; does not challenge): Named among the items with nothing to add in (a).
- **GLM** (reply line 75; does not challenge): Checked by hand on the display.
- **Goes to no checker**: no point challenges it and it is not one of the twelve; recorded under rule 7 below.

#### FC39 · claim · Interference

Lines it formalizes or quotes (from the brief): L305, L309.

- **Mimo** (reply line 75; does not challenge): Named among the items with nothing to add in (a).
  - Quotations: “nonempty \(B\subseteq W\)” — found at L293.
- **Mimo** (reply line 125; does not challenge): Realized (a: x = 0, b: x = 1); survives.
- **GLM** (reply line 25; does not challenge): Named among the items with nothing to add in (a).
- **GLM** (reply line 75; does not challenge): Checked by hand on the display.
- **Goes to no checker**: no point challenges it and it is not one of the twelve; recorded under rule 7 below.

#### FC40 · claim · Infinitary routes: collective criticality, and the step the first sentence leaves unsaid

Lines it formalizes or quotes (from the brief): L311, L313.

- **Mimo** (reply line 59; challenges): (a) and (b) match, the maths stating more than the words, all following from (S), (B) and I31; step (c) is not in the words (matter 8).
  - Proposal `M9-B10` (reply lines 143–145), would change L311:

````
L311 | \(\Gamma=\{d_n:n\in\mathbb N\}\), \(d_n\) the constraint \(|x|\le 1/n\): every set of indices unbounded in \(\mathbb N\) determines \(x=0\), and no other set does; no minimal route, and no route of one commitment, exists. Removing any one \(d_n\), or adding it back, leaves the determination of \(x=0\) in place: each \(d_n\) does no work by itself. (B) records the collective criticality.
````

- **Mimo** (reply line 123; does not challenge): Holds for arbitrary subsets of ℕ; I91 does not bind.
- **GLM** (reply line 21; challenges): Part (c) (each d_n does no work by itself) is said by the maths and not by the words; the words should change (matter 8).
  - Proposal `G9-B9` (reply lines 91), would change L311:

````
> L311 | \(\Gamma=\{d_n:n\in\mathbb N\}\), \(d_n\) the constraint \(|x|\le 1/n\): every set of indices unbounded in \(\mathbb N\) determines \(x=0\); each \(d_n\) does no work by itself, one index added or removed leaving every unbounded set unbounded; no minimal route, and no route of one commitment, exists.
````

- **GLM** (reply line 77; does not challenge): Holds for all subsets of ℕ; I91's bound drops away.
- **Goes to a checker** (rule 5): challenged by GLM and Mimo. Lines at stake: L311.

#### FC41 · claim · Commitments that do no work, and why 'when Γ is infinite'

Lines it formalizes or quotes (from the brief): L313.

- **Mimo** (reply lines 61–67; challenges): (a) and (b) match; (c) holds, but "When Γ is infinite" is coarser than needed: what must be infinite is the block; proposes a new last sentence of L313 (writes FC41 (c)).
  - Proposal `M9-B7` (reply lines 65–67), would change L313:

````
L313 | A finite block of such commitments is critical in no route; when \(\Gamma\) is infinite, an infinite block of them can still be critical (Infinitary routes).
````

  - Quotations: “When \(\Gamma\) is infinite” — found at L313.
- **Mimo** (reply line 121; does not challenge): Holds for all families (argument by hand).
- **GLM** (reply line 25; does not challenge): Named among the items with nothing to add in (a).
- **GLM** (reply line 79; does not challenge): Holds for arbitrary Γ; L311 shows "when Γ is infinite" cannot be dropped; the sentence holds.
  - Quotations: “when Γ is infinite” — found at L313.
- **Goes to a checker** (rule 5): challenged by Mimo. Lines at stake: L313.

#### FC42 · claim · Criticality is relative to the route

Lines it formalizes or quotes (from the brief): L299.

- **Mimo** (reply line 75; does not challenge): Named among the items with nothing to add in (a).
  - Quotations: “nonempty \(B\subseteq W\)” — found at L293.
- **Mimo** (reply line 125; does not challenge): Survives with FC38 and FC39's realizations.
- **GLM** (reply line 25; does not challenge): Named among the items with nothing to add in (a).
- **GLM** (reply line 75; does not challenge): Checked by hand on the display.
- **Goes to no checker**: no point challenges it and it is not one of the twelve; recorded under rule 7 below.

#### FC75 · claim · Active routes: the excluded routes fail the definition's own clauses

Lines it formalizes or quotes (from the brief): L375.

- **Mimo** (reply line 69; challenges): The formal (a) is I46's join clause, not the words' "started and did no work", which is better read as the absence of nonconstant dependence, (b); (c) matches "whether a route is active is read from the history, not from the result".
  - Quotations: “started and did no work” — found at L375; “whether a route is active is read from the history, not from the result” — found at L375.
- **Mimo** (reply lines 79–81; challenges): The look (a route finished at step 1 whose product persists to r at step 9) is counted active by D11.4 while L375 excludes a route "already at rest when the result occurred"; they disagree only if that route is "at rest", which the words do not fix; a counterexample to the invention (I46, H11), not the text; removed by a wording of "at rest" (under H11), or by adding the clause back into D11.4.
  - Proposal `M9-B8` (reply lines 105–107), would change L375:

````
L375 | A route that started and did no work, or that was already at rest when the result occurred, is not active for that result. A route is at rest at a time when none of its occurrences runs at that time and nothing it produced is carried on to the result after it; a route that finished earlier and whose product persists and is carried to the result is not at rest. Whether a route is active is read from the history, not from the result.
````

  - Quotations: “already at rest when the result occurred” — found at L375; “at rest” — found at L375, L522.
- **Mimo** (reply line 115; challenges): Hand model, dependence outside the route: R = {i, r} is connected and chained and r's value varies with i's port only via c, m outside R; D11.4 counts R active though nothing R carries produced r's value (rests on I46 and I95); not a counterexample to the text; the words should be read as carrying the dependence (the D11.4 proposal).
  - Proposal `M9-B5` (reply lines 47–49; printed in full under D11.4 above), would change L375.
  - Quotations: “which has nonconstant dependence” — found at L375.
- **Mimo** (reply line 117; challenges): Hand model, side component: a constant source c feeding m lies on no chain from i to r, so D11.4 excludes a route the words count active (rests on I46's chain clause); the words should stand.
  - Proposal `M9-B5` (reply lines 47–49; printed in full under D11.4 above), would change L375.
- **GLM** (reply line 29; challenges): The look is a counterexample only to the invention (I46 with I95): L375 excludes a route "already at rest" and the formalization fails to; the words should stand; whether a finished route whose product persists is "at rest" must be fixed in words (wording under H11).
  - Proposal `G9-B7` (reply lines 65; printed in full under D11.4 above), would change L375.
  - Quotations: “already at rest when the result occurred, is not active for that result” — found at L375; “at rest” — found at L375, L522.
- **GLM** (reply line 81; challenges): (a) and (b) follow from D11.4; (c) holds by construction; a softer attack: D11.4 assesses dependence by intervening on i's port while L375 says activity "is read from the history"; if a history never varies i, the intervention reading can call a route active that a reading from the actual occurrences (I46 (b)) would not; the text should say which (wording under I46).
  - Proposal `G9-B6` (reply lines 55), would change L375:

````
> A **represented input** is an input occurrence whose port carries a represented distinction; the **operative result** is the result occurrence the active route is named for; the **applicable relations** are the relations the physical interpretation gives each occurrence at the grain in force; the **declared contrasts** are the pairs of values of the represented input's port named when the route is assessed.
````

  - Quotations: “is read from the history” — found at L375; “Under the declared contrasts” — found at L375; “read from the history” — found at L375.
- **Goes to a checker** (rule 5): challenged by GLM and Mimo. Lines at stake: L375.

#### FC105 · claim · 'Event' is used and never defined; 'occurrence' is defined

Lines it formalizes or quotes (from the brief): L161, L169, L604.

- **Mimo** (reply line 73; does not challenge): Matches: "occurrence" defined, "event" not; the other uses are not given (the reader relies on the register's list); "not tested" is right.
  - Quotations: “occurrence” — found at L31, L167, L169, L205 and 6 more lines; “Not tested” — not found in the text; found in the brief.
- **GLM** (reply line 23; challenges): Not tested, correctly; under I45 the reading is strained at two of the six uses (see (d)).
- **GLM** (reply line 83; challenges **OWNER QUESTION**): Under I45, L604's "An assessment event with contract C" is readable only by a gloss, and L612's "lost event identities" (known only through FC105's quotation) reads as identities beyond occurrence sets (I45's alternative (a)); the proposed definition settles the reading one way; "whether that is the owner's way is not for the maths to say".
  - Quotations: “An assessment event with contract C” — found at L604; “lost event identities” — found at L612.
- **Goes to a checker** (rule 5): challenged by GLM. Lines at stake: L161, L169, L604.
- Marks: OWNER QUESTION points present.

#### I29 · invention · The restriction operation (E restricted to W): deletion

Lines it formalizes or quotes (from the brief): L287.

- **Mimo** (reply line 85; challenges): The text settles that the operation is declared and constrains every declaration (L287, L231); which operation stays open by design; the D7.1 proposal records that it is an input.
  - Proposal `M9-B1` (reply lines 7–9; printed in full under D7.1 above), would change L287.
  - Quotations: “Fix \(\mathcal E\) and a declared restriction operation” — found at L287.
- **GLM** (reply lines 35–37; challenges): Not settled: L231's "the components of E|W" presupposes that components are removed, but the text never says the ports of Γ ∖ W go with them; proposes a new L287 (writes I29 in).
  - Proposal `G9-B3` (reply lines 37), would change L287:

````
> L287 | Fix \(\mathcal E\) and a declared restriction operation. For \(W\subseteq\Gamma\), let \(E|W\) be \(E\) with every component of \(\Gamma\setminus W\) deleted, its ports removed, and the named background unchanged; the commitments of \(E|W\) are \(W\).
````

  - Quotations: “With the named background fixed” — found at L287; “the components of E\|W” — found at L231.
- **External reader and case card:** E02 (the external reader) challenges the sentence this item formalizes (section 3 below).
- **Goes to a checker** (rule 5): challenged by GLM and Mimo; challenged by E02 (the external reader). Lines at stake: L287.

#### I30 · invention · The worked examples of routes are set systems

Lines it formalizes or quotes (from the brief): L307.

- **Mimo** (reply line 87; challenges): Settled by the text: L307 states a family directly; both examples are realizable ((d)).
  - Quotations: “\(\Gamma=\{a,b\}\), \(\mathsf S=\{\{a\},\{b\},\{a,b\}\}\)” — found at L307.
- **GLM** (reply line 39; challenges): Settled by the text's own display at L307; nothing to write.
- **Goes to a checker** (rule 5): challenged by GLM and Mimo. Lines at stake: L307.

#### I31 · invention · The routes of the infinitary example

Lines it formalizes or quotes (from the brief): L311.

- **Mimo** (reply line 89; challenges): Settled as to the question and the negatives; not settled that bounded sets are no routes; the matter 8 proposal adds "and no other set does" (writes I31).
  - Proposal `M9-B10` (reply lines 143–145; printed in full under FC40 above), would change L311.
  - Quotations: “determines \(x=0\)” — found at L311; “no minimal route, and no route of one commitment, exists” — found at L311; “and no other set does” — not found in the text; not in the brief.
- **GLM** (reply line 41; challenges): Settled, and by more than the drafters used: "no minimal route … exists" forces bounded sets out (a finite route would contain a minimal one), closing I31's alternative (a) too; nothing to write.
  - Quotations: “Every set of indices unbounded in ℕ determines x = 0” — found at L311; “is x determined to be 0?” — not found in the text; found in the brief; “no minimal route … exists” — found at L311.
- **Goes to a checker** (rule 5): challenged by GLM and Mimo. Lines at stake: L311.

#### I44 · invention · Causal precedence in a history is transitive

Lines it formalizes or quotes (from the brief): L375.

- **Mimo** (reply line 91; challenges): Not settled: "acyclic" leaves transitivity open; written by the D11.3 proposal.
  - Proposal `M9-B4` (reply lines 39–41; printed in full under D11.3 above), would change L375.
  - Quotations: “acyclic” — found at L375.
- **GLM** (reply lines 43–45; challenges): Not settled: "acyclic" permits an intransitive precedence, and then ⪯_h is not an order; proposes a new first sentence of L375 (writes I44 in).
  - Proposal `G9-B4` (reply lines 45; printed in full under D11.3 above), would change L375.
  - Quotations: “acyclic” — found at L375; “its reflexive closure” — found at L375.
- **Goes to a checker** (rule 5): challenged by GLM and Mimo. Lines at stake: L375.

#### I45 · invention · 'Event' is a set of occurrences

Lines it formalizes or quotes (from the brief): L161, L169, L397.

- **Mimo** (reply line 93; challenges): Not settled; written in part by the matter 2 proposal.
  - Proposal `M9-B9` (reply lines 133–135; printed in full under D11.1 above), would change L169.
- **GLM** (reply lines 47–51; challenges **OWNER QUESTION**): Not settled (matter 2); proposes a definition of event (no line named; placed with L169 by matter 2); "if the owner wants events with identities of their own, the sentence should instead say so — the choice is the owner's, not the maths'".
  - Proposal `G9-B5` (reply lines 49), would change L169:

````
> An **event** is a nonempty set of occurrences in one history; an assessment and a formulation are events, and a record leaf refers to one.
````

- **Goes to a checker** (rule 5): challenged by GLM and Mimo. Lines at stake: L169.
- Marks: OWNER QUESTION points present.

#### I46 · invention · Active route: 'represented input', 'operative result', 'applicable relations', 'declared contrasts'

Lines it formalizes or quotes (from the brief): L375.

- **Mimo** (reply line 95; challenges): Not settled: four phrases undefined, "nonconstant dependence" readable with or without setting the input's port; the D11.4 proposal writes the phrases and the setting reading, drops the chain clause and adds the carrying condition; I46's entry does not record dropping the chain clause among its alternatives.
  - Proposal `M9-B5` (reply lines 47–49; printed in full under D11.4 above), would change L375.
  - Quotations: “nonconstant dependence” — found at L375.
- **GLM** (reply lines 53–57; challenges): Not settled; the four phrases are defined nowhere (matter 11); proposes a sentence after the active-route sentence of L375 (writes I46 in).
  - Proposal `G9-B6` (reply lines 55; printed in full under FC75 above), would change L375.
  - Quotations: “at rest” — found at L375, L522.
- **Goes to a checker** (rule 5): challenged by GLM and Mimo. Lines at stake: L375.

#### I91 · invention · The infinitary routes on eventually periodic index sets

Lines it formalizes or quotes (from the brief): L311.

- **Mimo** (reply line 97; does not challenge): A search device with no bearing on the text; the hand argument covers arbitrary sets; no change.
- **GLM** (reply line 59; does not challenge): A search bound; stays out of the text; the hand argument removes the bound for FC40.
- **Goes to no checker**: no point challenges it and it is not one of the twelve; recorded under rule 7 below.

#### I95 · invention · Toy histories for active routes

Lines it formalizes or quotes (from the brief): L375.

- **Mimo** (reply line 99; challenges): The timing and persistence are the entry's own alternative, which L375's "already at rest" needs; the D11.3 proposal writes it; the dependence reading is written at D11.4.
  - Proposal `M9-B4` (reply lines 39–41; printed in full under D11.3 above), would change L375.
  - Quotations: “already at rest” — found at L375; “Setting the input's port ... recomputed” — not found in the text; not in the brief.
- **GLM** (reply line 61; challenges): A search bound; stays out; its other choice (a), time stamps and persistence, is what the H11 wording needs and goes into the text there.
  - Proposal `G9-B7` (reply lines 65; printed in full under D11.4 above), would change L375.
- **Goes to a checker** (rule 5): challenged by GLM and Mimo. Lines at stake: L375.

#### H11 · H-entry · The "already at rest" clause dropped from active routes (D11.4)

Lines it formalizes or quotes (from the brief): L375.

- **Mimo** (reply lines 101–109; challenges): The text settles that an at-rest route is not active; it does not settle "at rest" for a finished route whose product persists; proposes a new second sentence of L375 defining "at rest" (a persisting product carried to the result is not at rest), with reasons against the stricter reading (which would leave temporally separated work with no active route).
  - Proposal `M9-B8` (reply lines 105–107; printed in full under FC75 above), would change L375.
  - Quotations: “at rest” — found at L375, L522.
- **GLM** (reply lines 63–65; challenges): A real omission: D11.4 says less than L375 and nothing records it; the text should define "at rest" (a route whose processes are all complete before the result's process begins is at rest, whatever of its product persists); proposes a new sentence for L375 (takes from I95's other choice (a)).
  - Proposal `G9-B7` (reply lines 65; printed in full under D11.4 above), would change L375.
  - Quotations: “at rest” — found at L375, L522.
- **Goes to a checker** (rule 5): challenged by GLM and Mimo. Lines at stake: L375.

#### H19 · H-entry · Org_ℓ extended from occurrences to histories; "subhistory" (D11.3)

Lines it formalizes or quotes (from the brief): L375.

- **Mimo** (reply line 111; challenges): The text gives Org_ℓ for an occurrence (L213, as the entry notes) and not for a history, and "subhistory" has no words; written by the D11.3 proposal.
  - Proposal `M9-B4` (reply lines 39–41; printed in full under D11.3 above), would change L375.
  - Quotations: “subhistory” — found at L405, L409, L427, L435 and 1 more lines.
- **GLM** (reply lines 67–69; challenges): The extension of Org_ℓ to histories and "subhistory" are used and unnumbered; proposes new wording at L375 (writes H19 in).
  - Proposal `G9-B8` (reply lines 69), would change L375:

````
> L375 | … and a physical interpretation supplying process occurrences, their ports, the connections actually instantiated, and, at each grain, the organization of the history. A **subhistory** is a set of a history's occurrences closed under the interpretation, with \(\prec_h\) restricted to it.
````

  - Quotations: “subhistory” — found at L405, L409, L427, L435 and 1 more lines.
- **Goes to a checker** (rule 5): challenged by GLM and Mimo. Lines at stake: L375.

#### matter 2 · round-1 matter · "event" is used at L53, L55, L161, L397, L604 and L612 and defined nowhere; "occurrence" is defined at L169; the text does not say how they are related (to be read with L596's claim).

Lines it formalizes or quotes (from the brief): L53, L55, L161, L169, L397, L604, L612.

- **Mimo** (reply lines 129–137; challenges): A change is needed: "event" is used at six lines and defined nowhere; proposes a new L169 defining an event as a nonempty set of occurrences of one history (writes I45); relies on the register's list for the other uses; L612's "lost event identities" then reads as losing which occurrences a record refers to, else events need a sort of their own.
  - Proposal `M9-B9` (reply lines 133–135; printed in full under D11.1 above), would change L169.
  - Quotations: “lost event identities” — found at L612.
- **GLM** (reply line 87; challenges): Needs the change: the definition proposed under I45; until then the six uses of "event" have no fixed sort.
  - Proposal `G9-B5` (reply lines 49; printed in full under I45 above), would change L169.
- **Goes to a checker** (rule 5): challenged by GLM and Mimo. Lines at stake: L169.

#### matter 8 · round-1 matter · L311's first sentence does not say in words that each d_n does no work by itself, which L313's "such commitments" needs; one step shows it.

Lines it formalizes or quotes (from the brief): L311, L313.

- **Mimo** (reply lines 139–145; challenges): A change is needed: L313's "such commitments" needs the step that each d_n does no work, and the route family is not stated in full; proposes a new L311 (fragments joined; writes I31 and FC40 (c)).
  - Proposal `M9-B10` (reply lines 143–145; printed in full under FC40 above), would change L311.
  - Quotations: “such commitments” — found at L313.
- **GLM** (reply lines 89–91; challenges): Needs the change; L313's "such commitments" has no antecedent without it; proposes a new L311.
  - Proposal `G9-B9` (reply lines 91; printed in full under FC40 above), would change L311.
  - Quotations: “such commitments” — found at L313.
- **Goes to a checker** (rule 5): challenged by GLM and Mimo. Lines at stake: L311.

#### matter 11 · round-1 matter · "operative result", "applicable relations" (L375), "deliberative", "structural map" (L385) occur only there and are defined nowhere; round 1 read them as plain words.

Lines it formalizes or quotes (from the brief): L375, L385.

- **Mimo** (reply line 147; challenges): L375's "operative result" and "applicable relations" are written by the D11.4 proposal; "deliberative" and "structural map" at L385 are defined nowhere and need a change, but no wording is given for a line not before the reader.
  - Proposal `M9-B5` (reply lines 47–49; printed in full under D11.4 above), would change L375, L385.
  - Quotations: “operative result” — found at L375; “applicable relations” — found at L375; “Deliberative” — found at L385; “structural map” — found at L385.
- **GLM** (reply line 93; challenges): For L375's phrases, the I46 definitions and the H11 at-rest sentence; L385's "deliberative" and "structural map" are not this part's, and round 1's ruling (read them as plain words) can stand only while nothing in the maths turns on them; the part covering L385 should settle them.
  - Proposal `G9-B6` (reply lines 55; printed in full under FC75 above), would change L375.
  - Proposal `G9-B7` (reply lines 65; printed in full under D11.4 above), would change L375.
  - Quotations: “operative result” — found at L375; “applicable relations” — found at L375; “represented input” — found at L375; “declared contrasts” — found at L375; “deliberative” — found at L385; “structural map” — found at L385.
- **Goes to a checker** (rule 5): challenged by GLM and Mimo. Lines at stake: L375, L385.

#### matter 13 · round-1 matter · "contribution" in Part VI and Part XI (L305; L435, L441), each sense fixed where it stands.

Lines it formalizes or quotes (from the brief): L305, L435, L441.

- **Mimo** (reply line 149; challenges): No change at L305 (the D7.5 proposal keeps "contributory" defined); at L311 the matter 8 proposal names "collective criticality"; L435 and L441 are dealt with where they stand.
  - Proposal `M9-B10` (reply lines 143–145; printed in full under FC40 above), would change L311.
  - Quotations: “contributory” — found at L305, L307; “collective criticality” — not found in the text; found in the brief.
- **GLM** (reply line 95; does not challenge): No change: each sense of "contribution" is fixed where it stands; nothing here turns on the other sense.
  - Quotations: “contribution” — found at L307, L311, L427, L435 and 4 more lines.
- **Goes to a checker** (rule 5): challenged by Mimo. Lines at stake: L311.

#### Part 9: items no point addresses

Items of this part on which neither reader made any point (both replies read whole): NF18. Each is recorded under rule 7 in section 6 unless a point on it in another part sends it to a checker.

### Part 10: Conflict and rivals

Brief: `tests/S104 Round 2 - the maths against the words - part 10, Conflict and rivals.md`. Replies: `s104_maths_mimo_10.response.txt` (Mimo), `s104_maths_glm_10.response.txt` (GLM).

#### D8.1 · definition · Meeting at a pair under hypothetical relations

Lines it formalizes or quotes (from the brief): L315.

- **Mimo** (reply line 5; challenges): Matches L315's "each of them could meet … each a relation on the component's footprint (Part II)"; the maths drops the homomorphism clause at a pair (I18), which is faithful only if Part II's (F1) carries such a clause (lines not before the reader; see I19).
  - Proposal `M10-B3` (reply lines 47–49), would change L315:

````
each of them could meet (F1) without its homomorphism clause, (F2) and (A) there
````

  - Quotations: “each of them could meet (F1), (F2) and (A) there under some relations of the target's components at that pair, each a relation on the component's footprint (…” — found at L315.
- **GLM** (reply line 5; challenges): Matches; one part of the invention is not in the sentence: that the homomorphism clause is left out at a pair (I18; the reader relies on the register's remark); see I19.
  - Proposal `G10-B3` (reply lines 43), would change L315:

````
> Meeting (F1), (F2) and (A) at a pair under hypothetical relations takes those conditions as they hold at that pair alone; nothing they say of other pairs, or of whole edits, is in question there.
````

- **GLM** (reply line 79; does not challenge): Nothing to add beyond the I18 remark.
- **Goes to a checker** (rule 5): challenged by GLM and Mimo. Lines at stake: L315.

#### D8.2 · definition · Conflict

Lines it formalizes or quotes (from the brief): L315.

- **Mimo** (reply line 7; challenges): Domain mismatch: the words fix "some admitted edit–boundary pair of the target that both their transports translate, in C or outside it"; the maths drops "admitted" (also in D8.3); the words stand and the maths must restrict to admitted pairs; no text change.
  - Quotations: “at some admitted edit–boundary pair of the target that both their transports translate, in \(C\) or outside it.” — found at L315; “a pair (a,b) of the target that both transports translate” — not found in the text; found in the brief; “admitted” — found at L8, L11, L15, L31 and 31 more lines.
- **GLM** (reply line 7; does not challenge): Faithful; the second disjunct covers answer-difference when both can meet, and the first does its work only where one or both can meet under no relations, which is what the "or" intends; the words should stand.
  - Quotations: “answers differ, or each could meet under some relations and no such relations let both” — not found in the text; not in the brief; “∃R Meets(ℰ,R) ∧ ∃R' Meets(ℰ',R')” — not found in the text; not in the brief; “each of them could meet … under some relations” — found at L315; “no such relations let both” — found at L315.
- **Goes to a checker** (rule 5): challenged by Mimo. Lines at stake: L315.

#### D8.3 · definition · Offer; rivals

Lines it formalizes or quotes (from the brief): L315.

- **Mimo** (reply line 9; challenges): The maths makes rivals of two candidates whenever one is offered in place of the other, but the words add "a candidate that nobody has offered is no one's rival", so if A is offered in place of B and nobody offered B, B is still A's rival under D8.3; the words stand; the maths must require that both have been offered.
  - Quotations: “a candidate's rivals are among the candidates someone has offered, and a candidate that nobody has offered is no one's rival.” — found at L315.
- **GLM** (reply line 9; challenges): (i) the sentence says "at some admitted edit–boundary pair", D8.3 only "some pair both translate": the maths should carry "admitted"; (ii) the symmetry of the offer is settled by the words ("one of them has been offered … in place of the other"), so I33's symmetric reading is the text's own.
  - Quotations: “at some admitted edit–boundary pair” — found at L315; “some pair both translate” — not found in the text; found in the brief; “admitted” — found at L8, L11, L15, L31 and 31 more lines; “one of them has been offered as an answer to p in place of the other” — found at L315; “one of them” — found at L75, L223, L315, L317 and 1 more lines.
- **Goes to a checker** (rule 5): challenged by GLM and Mimo. Lines at stake: L315.

#### D8.4 · definition · A claim at a pair

Lines it formalizes or quotes (from the brief): L315.

- **Mimo** (reply line 27; does not challenge): Nothing to add on wording (matches).
- **GLM** (reply line 11; does not challenge): Faithful and consistent with S27.
  - Quotations: “It is not enough for a creative agent to do anything about it though” — not found in the text; found in the brief.
- **GLM** (reply line 79; does not challenge): Named among the items with nothing to add.
- **Goes to no checker**: no point challenges it and it is not one of the twelve; recorded under rule 7 below.

#### D8.5 · definition · Conflict with a claim

Lines it formalizes or quotes (from the brief): L315.

- **Mimo** (reply lines 11–21; challenges): Vacuity: "every relation … under which it could meet" holds of an empty set, so a candidate that can meet under no relation conflicts with χ, which the words ("χ excludes what the candidate's organization and transport give there") do not say; redundancy: because Meets includes (A), the first branch entails the second (FC52), and with the empty case excluded the "or" is genuine; proposes replacing the sentence of L315 "when χ excludes … (A) there.".
  - Proposal `M10-B1` (reply lines 19–21), would change L315:

````
when \(\chi\) excludes what the candidate's organization and transport give there: its answer, or, where some relation of the target's components lets it meet (F1), (F2) and (A) there, every such relation.
````

  - Quotations: “every relation … under which it could meet” — found at L315; “χ excludes what the candidate's organization and transport give there” — found at L315; “when \(\chi\) excludes … (A) there.” — found at L315.
- **GLM** (reply lines 13–15; challenges): The maths and the words part, and the words should stand: D8.5 lacks the existence condition its neighbours have, so a candidate that can meet under no relations, or whose answer no relations give, conflicts with every claim there, even one that allows everything; the words presuppose that it could meet; an unrecorded choice bearing on FC52; proposes a new L315 sentence (making the two disjuncts independent).
  - Proposal `G10-B1` (reply lines 15), would change L315:

````
> A candidate **conflicts with** a claim \(\chi\) at an admitted pair of the target that its transport translates, in \(C\) or outside it, when \(\chi\) excludes what the candidate's organization and transport give there: its answer — some relations of the target's components would give that answer there, and none that \(\chi\) allows would — or it could meet (F1), (F2) and (A) there under some relations of the target's components, and \(\chi\) excludes every such relation.
````

  - Quotations: “every R with Meets_ab(ℰ,R) lies outside Allow_χ(a,b)” — not found in the text; found in the brief; “what the candidate's organization and transport give there” — found at L315; “every relation … under which it could meet” — found at L315.
- **Goes to a checker** (rule 5): challenged by GLM and Mimo. Lines at stake: L315.

#### D8.6 · definition · Conflict given χ; rivals given χ

Lines it formalizes or quotes (from the brief): L315.

- **Mimo** (reply line 27; does not challenge): Nothing to add on wording (matches; its words settle I35).
- **GLM** (reply line 17; does not challenge): Faithful, existence condition included (see I35).
- **GLM** (reply line 79; does not challenge): Named among the items with nothing to add.
- **Goes to no checker**: no point challenges it and it is not one of the twelve; recorded under rule 7 below.

#### FC43 · claim · Conflict, rivals, problems and 'easy to vary' are symmetric

Lines it formalizes or quotes (from the brief): L317.

- **Mimo** (reply line 25; challenges): Conf and Riv are symmetric by construction; the step to Prob_j, its kind and ETV_j goes beyond "the rival is then easy to vary too" and rests on lines not given; the words stand.
  - Quotations: “so Prob_j and its kind are symmetric, and ETV_j(\(\mathcal E\)) through \(\mathcal E'\) gives ETV_j(\(\mathcal E'\))” — not found in the text; found in the brief; “the rival is then easy to vary too” — found at L317.
- **Mimo** (reply line 93; challenges **PARKED**): Conf/Riv symmetry cannot be broken, but the sentence can: under a reading of L317's "easy to vary" as "has a variation that still meets", one candidate with two admissible relations is easy to vary and its rival with one is not, so "the rival is then easy to vary too" fails; it rests on that reading; the reader says it proposes nothing about what hard to vary covers (S33–S34).
  - Quotations: “easy to vary” — found at L69, L317, L526; “has a variation that still meets” — not found in the text; not in the brief; “the rival is then easy to vary too” — found at L317.
- **GLM** (reply line 19; challenges): The formal statement is mostly about Conf and Riv, while the sentence quoted is about easy to vary, defined in another part (I37); only partly formalized here; the symmetry leg is sound, the ETV leg cannot be judged from this part.
  - Quotations: “the rival is then easy to vary too” — found at L317.
- **GLM** (reply line 67; challenges): Conf's symmetry holds by logic; Riv's, under I86, by construction, so the search tested nothing about it; "the rival is then easy to vary too" rests on I37 and on fixing the assessor: if easy to vary is relative to an assessor, "too" needs the same one, and nothing here fixes that; flagged, not proposed.
  - Quotations: “the rival is then easy to vary too” — found at L317.
- **Goes to a checker** (rule 5): challenged by GLM and Mimo. Lines at stake: L317.
- Marks: PARKED points present. 

#### FC44 · claim · Two commitments with one counterpart and different relations cannot both meet (F1)

Lines it formalizes or quotes (from the brief): L315.

- **Mimo** (reply line 27; does not challenge): Nothing to add on wording.
- **Mimo** (reply line 31; challenges): The witness under "one counterpart = the same subnetwork" is a counterexample to that reading, an invention, not to the text; the phrase is open and the clause uncheckable while it is; the I36 wording makes the witness's pair fail the definition.
  - Proposal `M10-B6` (reply lines 75–77), would change L315:

````
as none do when two of their active components have one counterpart — the same subnetwork of the target, reached by port translations with the same image and a bijection of their variables that matches values — and have different relations there, that is, when carrying the one relation to the other's variables does not give the other's relation.
````

  - Quotations: “one counterpart” — found at L315, L562; “different relations there” — found at L315; “one counterpart = the same subnetwork” — found at L562.
- **Mimo** (reply line 95; challenges): Tried to break it under I36 with an order-3 bijection: it fails; a break survives only where a transport is partial (I17), comparing relations on the translated part alone (rests on I14, I17); the loose-reading witness is the standing problem.
  - Quotations: “relations there” — found at L315.
- **GLM** (reply line 21; does not challenge): Says what the sentence says under I36 (see (b)).
- **GLM** (reply lines 33–35; challenges): The witness refutes the reading "one counterpart = the same subnetwork, whatever the port translations", not I36's; it tells against leaving the words as they stand, since on the loose reading the sentence fails; proposes a new conflict sentence in L315 (writes I36 in).
  - Proposal `G10-B2` (reply lines 35), would change L315:

````
> Two candidates **conflict** at such a pair \((a,b)\) when their answers there differ, or when each of them could meet (F1), (F2) and (A) there under some relations of the target's components at that pair, each a relation on the component's footprint (Part II), and no such relations let both, as none do when two of their active components have one counterpart — the same subnetwork of the target, their ports carried by translations that agree up to a bijection of ports with matching value maps — and their relations there differ under that bijection.
````

  - Quotations: “one counterpart = the same subnetwork, whatever the port translations” — not found in the text; found in the brief.
- **Goes to a checker** (rule 5): challenged by GLM and Mimo. Lines at stake: L315.

#### FC45 · claim · Recoded candidates, and candidates some relations let both meet, conflict nowhere

Lines it formalizes or quotes (from the brief): L315.

- **Mimo** (reply line 27; does not challenge): Nothing to add on wording.
- **Mimo** (reply line 97; does not challenge): Both parts hold; dropping "takes its transport with it" breaks (a); the words are exactly as strong as the claim needs.
  - Quotations: “takes its transport with it” — found at L315.
- **GLM** (reply line 23; does not challenge): Both parts faithful; (b) by construction; (a) arguably by construction too, its content being I20/I81's equivariance.
- **GLM** (reply line 69; does not challenge): No break; the argument for it needs meeting to transfer under φ (I20 and I81's equivariance).
- **Goes to no checker**: no point challenges it and it is not one of the twelve; recorded under rule 7 below.

#### FC52 · claim · Conflict with a claim: the first disjunct implies the second

Lines it formalizes or quotes (from the brief): L315.

- **Mimo** (reply lines 11–21; challenges): As for D8.5: FC52's implication holds only through the vacuity; the D8.5 wording makes the "or" genuine.
  - Proposal `M10-B1` (reply lines 19–21; printed in full under D8.5 above), would change L315.
  - Quotations: “every relation … under which it could meet” — found at L315; “χ excludes what the candidate's organization and transport give there” — found at L315; “when \(\chi\) excludes … (A) there.” — found at L315.
- **Mimo** (reply line 99; challenges): Hand countermodel to D8.5 as written: χ allows every relation, the candidate's answer is allowed and no R makes it meet, so it conflicts with χ vacuously; the D8.5 wording removes it, and FC52's implication then fails in the empty case, as the words want.
  - Proposal `M10-B1` (reply lines 19–21; printed in full under D8.5 above), would change L315.
- **GLM** (reply line 25; challenges): The result is an artifact of D8.5's vacuity; once D8.5 is repaired the first disjunct no longer implies the second and FC52 fails (model in (d)); the sentence's two independent conditions should stay; the words stand, the maths changes.
  - Proposal `G10-B1` (reply lines 15; printed in full under D8.5 above), would change L315.
  - Quotations: “result” — found at L73, L155, L335, L351 and 7 more lines.
- **GLM** (reply line 65; challenges): Broken by hand: with a candidate that meets under no R and a permissive χ, D8.5 gives a conflict by vacuity; with χ excluding every R giving answer q, the repaired D8.5 makes the first disjunct hold and the second fail, so FC52's implication fails; both breaks rest only on the missing existence condition; the maths changes, the sentence needs only the (a) wording.
  - Proposal `G10-B1` (reply lines 15; printed in full under D8.5 above), would change L315.
- **Goes to a checker** (rule 5): challenged by GLM and Mimo. Lines at stake: L315.

#### FC53 · claim · Conflict with a claim rules a candidate out only with the premise that the claim speaks of the target

Lines it formalizes or quotes (from the brief): L315.

- **Mimo** (reply line 23; challenges): Formal (a) asserts that an argument exists; the words say only what "that argument" does; the words stand and the maths should state (a) conditionally on an argument being there (the reader relies on the earlier part of L315).
  - Quotations: “that argument” — found at L315; “that argument rules out that the candidate meets (E) for any assessor \(j\) who can use it, and so who tentatively accepts \(\chi\) (K2)” — found at L315.
- **Mimo** (reply line 101; challenges): (a) as computed is not general: with χ and Applies as atoms (I87), the forms of I89 and no premise linking χ to meeting, X_j(Acc(ℰ)) is empty while ConfCl holds; the pendulum encoding supplies that link by hand (I90); (a) is a property of the encoding.
  - Quotations: “nothing moves here” — not found in the text; not in the brief.
- **GLM** (reply line 27; does not challenge): Faithful on both legs and consistent with S27 and S28; an encoding check resting on I90 and I88.
  - Quotations: “That 'ruling out' is a choice that was made” — not found in the text; found in the brief.
- **GLM** (reply line 71; does not challenge): An argument lacking the Applies premise "rules out no candidate there" by the text's own sentence; no break of the sentences.
  - Quotations: “rules out no candidate there” — found at L315; “no argument in X_j” — not found in the text; not in the brief.
- **GLM** (reply line 79; does not challenge): Named among the items with nothing to add.
- **Goes to a checker** (rule 5): challenged by Mimo. Lines at stake: L315.

#### FC54 · claim · Rivals given χ conflict nowhere without χ at that pair

Lines it formalizes or quotes (from the brief): L315.

- **Mimo** (reply line 27; does not challenge): Nothing to add on wording.
- **Mimo** (reply line 103; does not challenge): Holds by construction given (A) ∈ Meets; under I35's option (a) it would fail, which the words exclude.
- **GLM** (reply line 29; does not challenge): Faithful; the implication holds by logic; the concluding clause matches "for one who does not …, they pose none on that account".
  - Quotations: “a pair of rivals given χ that conflicts at no other pair is not a pair of rivals” — not found in the text; found in the brief; “for one who does not [tentatively accept χ], they pose none on that account” — not found in the text; not in the brief.
- **GLM** (reply line 73; does not challenge): Holds by logic; the pressure point is I35's alternative, which the text settles against; recorded, not repaired: a χ excluding every behaviour at a pair makes any two candidates that could jointly meet there rivals given χ, recodings included; the text's own consequence (S27); no change (S21, S28).
- **GLM** (reply line 79; does not challenge): Named among the items with nothing to add.
- **Goes to no checker**: no point challenges it and it is not one of the twelve; recorded under rule 7 below.

#### I19 · invention · Meeting (F1), (F2) and (A) at one pair under hypothetical relations of the target

Lines it formalizes or quotes (from the brief): L315.

- **Mimo** (reply lines 37–51; challenges): Partly settled: "each a relation on the component's footprint (Part II)" fixes footprints; "it does not turn on what any physics admits (Part I)" rules out option (b); not settled: R's range and the dropping of the homomorphism clause; proposes a new clause in L315, and conditionally a second wording if Part II's (F1) carries a homomorphism clause.
  - Proposal `M10-B2` (reply lines 41–43), would change L315:

````
each any relation of the component's footprint (Part II), whether or not any physics admits it
````

  - Proposal `M10-B3` (reply lines 47–49; printed in full under D8.1 above), would change L315.
  - Quotations: “each a relation on the component's footprint (Part II)” — found at L315; “it does not turn on what any physics admits (Part I)” — found at L315.
- **GLM** (reply lines 41–45; challenges): The text settles R's range ("under some relations of the target's components at that pair, each a relation on the component's footprint"; "does not turn on what any physics admits" rules out (b); the subjunctive rules out (c)); not settled whether meeting at a pair includes clauses reaching beyond the pair (I18); if I18's part does not settle it, proposes a sentence for L315 (writes I19's exclusion of the homomorphism clause in).
  - Proposal `G10-B3` (reply lines 43; printed in full under D8.1 above), would change L315.
  - Quotations: “under some relations of the target's components at that pair, each a relation on the component's footprint” — found at L315; “it does not turn on what any physics admits” — found at L315; “could meet … there under some relations” — found at L315.
- **Goes to a checker** (rule 5): challenged by GLM and Mimo. Lines at stake: L315.

#### I33 · invention · The offer of one candidate in place of another: a primitive

Lines it formalizes or quotes (from the brief): L315.

- **Mimo** (reply lines 53–59; challenges): Not settled: "offered … as an answer to p in place of the other" has no definition, and L522 does not list offers (not given; relied on); proposes a sentence added to L315.
  - Proposal `M10-B4` (reply lines 57–59), would change L315:

````
An **offer** is a record of what someone has offered as an answer to \(p\) in place of another; whether an offer has been made is not settled here.
````

  - Quotations: “offered … as an answer to \(p\) in place of the other” — found at L315; “…in \(C\) or outside it.” — found at L315.
- **GLM** (reply lines 47–51; challenges): The text settles symmetry but not what an offering is; consistently with S20 and S21 proposes a sentence for L315 making an offer a matter of record (writes I33's choice in).
  - Proposal `G10-B4` (reply lines 49), would change L315:

````
> Whether one candidate has been offered in place of another is a matter of record, not of the semantics: someone put it forward as an answer to \(p\) in place of the other, and the semantics carries that fact and nothing more; no list of offerings is supposed either.
````

  - Quotations: “one of them … in place of the other” — found at L315.
- **Goes to a checker** (rule 5): challenged by GLM and Mimo. Lines at stake: L315.

#### I34 · invention · A claim χ as a set of allowed behaviours at a pair, and the premise that it speaks of the target

Lines it formalizes or quotes (from the brief): L315.

- **Mimo** (reply lines 61–67; challenges): Partly settled: "χ need not be an explanation", the perpetual-motion example and "every relation … under which it could meet" fix that a claim speaks of relations (option (b) out); what a claim is is not settled; proposes replacing the χ sentence of L315.
  - Proposal `M10-B5` (reply lines 65–67), would change L315:

````
A claim \(\chi\) is given at each pair by the relations of the target's components it allows there; it need not be an explanation or come with one, and it may be a claim about what is possible or impossible: the bare claim that perpetual motion is impossible is enough for a conflict with a candidate whose organization gives perpetual motion.
````

  - Quotations: “\(\chi\) need not be an explanation or come with one” — found at L315; “every relation of the target's components under which it could meet” — found at L315; “\(\chi\) need not be an explanation or come with one, and it may be a claim about what is possible or impossible: …” — found at L315.
- **GLM** (reply line 53; challenges): The text rules out answers-only exclusion (b); between a sentence with its own semantics (a) and a set of allowed behaviours the text should stay open (S27); the premise that χ speaks of the target is already in the text; no wording.
  - Quotations: “a candidate whose organization gives perpetual motion” — found at L315; “It's also a detail that exists outside the process” — not found in the text; found in the brief; “perpetual motion is impossible” — found at L315; “the premise that \(\chi\) speaks of the target under that pair's edit” — found at L315.
- **Goes to a checker** (rule 5): challenged by GLM and Mimo. Lines at stake: L315.

#### I35 · invention · Conflict given χ: no requirement that each candidate can meet under χ

Lines it formalizes or quotes (from the brief): L315.

- **Mimo** (reply line 69; challenges): Settled by the words: "Two candidates that some relations of the target's components would let both meet … when χ excludes every such relation" requires some relations letting both meet, excluding option (a); no change.
  - Quotations: “Two candidates that some relations of the target's components would let both meet (F1), (F2) and (A) at a pair, when \(\chi\) excludes every such relation” — found at L315.
- **GLM** (reply line 55; challenges): The text settles it (quotes the rivals-given-χ sentence); alternative (a) is not the text's; no change.
  - Quotations: “Two candidates that some relations of the target's components would let both meet (F1), (F2) and (A) at a pair, when \(\chi\) excludes every such relation, c…” — found at L315.
- **Goes to a checker** (rule 5): challenged by GLM and Mimo. Lines at stake: L315.

#### I36 · invention · 'Two of their active components with one counterpart'

Lines it formalizes or quotes (from the brief): L315.

- **Mimo** (reply lines 71–77; challenges): Not settled; proposes replacing "as none do when two of their active components with one counterpart have different relations there." in L315.
  - Proposal `M10-B6` (reply lines 75–77; printed in full under FC44 above), would change L315.
  - Quotations: “as none do when two of their active components with one counterpart have different relations there.” — found at L315.
- **GLM** (reply line 57; challenges): Not settled; the wording under (b) writes it in and should be adopted.
  - Proposal `G10-B2` (reply lines 35; printed in full under FC44 above), would change L315.
- **Goes to a checker** (rule 5): challenged by GLM and Mimo. Lines at stake: L315.

#### I86 · invention · Every pair of candidates examined counts as offered one in place of the other

Lines it formalizes or quotes (from the brief): L315.

- **Mimo** (reply line 79; challenges): A search choice: the harness sets Offered for every pair it examines, which "a candidate that nobody has offered is no one's rival" cannot honour; stays out of the text; FC43's symmetry holds for any content of Offered.
  - Quotations: “a candidate that nobody has offered is no one's rival” — found at L315.
- **GLM** (reply line 59; does not challenge): A search device: the text's rivals require an actual offering; setting Offered for every examined pair tests conflict-symmetry; see (d) on what FC43's result is worth.
- **Goes to a checker** (rule 5): challenged by Mimo. Lines at stake: L315.

#### I88 · invention · X_j ranges over a finite set of arguments; an argument has a step

Lines it formalizes or quotes (from the brief): L397.

- **Mimo** (reply lines 81–87; challenges **OWNER QUESTION**): Partly settled: "An argument is an argument tree: argument steps whose leaves are premises" fixes a tree with steps; whether a bare premise is an argument is open; finiteness is a search bound; S23 ("something that can be strung together into a coherent structure") bears on requiring a step; proposes a new L397 sentence (adding to what the text says an argument is; marked because it bears on the reading of "argument" at L397, addendum point 8).
  - Proposal `M10-B7` (reply lines 85–87), would change L397:

````
An argument is an argument tree: argument steps whose leaves are premises, which are record leaves or stated assumptions and definitions; a premise on its own is not an argument.
````

  - Quotations: “An argument is an argument tree: argument steps whose leaves are premises” — found at L397; “something that can be strung together into a coherent structure” — found at L8.
- **GLM** (reply line 61; challenges): The text settles that an argument has a step (rules out (b)); the finite range of X_j is a search bound; no text change.
  - Quotations: “An argument is an argument tree: argument steps whose leaves are premises” — found at L397.
- **Goes to a checker** (rule 5): challenged by GLM and Mimo. Lines at stake: L397.
- Marks: OWNER QUESTION points present.

#### Part 10: items no point addresses

Items of this part on which neither reader made any point (both replies read whole): none. Each is recorded under rule 7 in section 6 unless a point on it in another part sends it to a checker.

### Part 11: Problems, tests and easy to vary

Brief: `tests/S104 Round 2 - the maths against the words - part 11, Problems, tests and easy to vary.md`. Replies: `s104_maths_mimo_11.response.txt` (Mimo), `s104_maths_glm_11.response.txt` (GLM).

#### D10.1 · definition · Problem

Lines it formalizes or quotes (from the brief): L317.

- **Mimo** (reply line 3; challenges): The object of "decided" ("no argument usable by that assessor has decided") is the conflict, and the maths gives one way of deciding it only (NotOut_j on the two Acc claims); a conflict can also be decided with neither candidate ruled out, by an argument ruling out that they conflict at the pair; "decided" is wider than "solved"; the words stand; the maths should add NotOut_j('Conf(ℰ,ℰ′)') and record it as an invention.
  - Quotations: “that no argument usable by that assessor has decided” — found at L317; “decided” — found at L71, L317; “solved” — found at L317; “a candidate is ruled out for j when the claim that it meets (E) is” — found at L315.
- **GLM** (reply line 5; does not challenge): Faithful; "decided" as "ruled out by a usable argument" is the natural reading of D9.8 and keeps to S23.
  - Quotations: “a conflict between ideas that no argument usable by that assessor has decided” — found at L317; “decided” — found at L71, L317; “ruled out by a usable argument” — not found in the text; not in the brief; “for that assessor” — found at L317, L369.
- **Goes to a checker** (rule 5): challenged by Mimo. Lines at stake: L317.

#### D10.2 · definition · The two kinds

Lines it formalizes or quotes (from the brief): L317.

- **Mimo** (reply lines 5–9; challenges): Both D10.2 and D8.2 drop "admitted": L315 makes conflict a relation on an "admitted edit–boundary pair … that both their transports translate", two conditions, the maths has one; the words stand; the gap is unrecorded and breaks FC49 under one reading; proposes a new (ii) clause of L317 (also fixing FC48's pair restriction).
  - Proposal `M11-B1` (reply lines 7–9), would change L317:

````
> L317 | (ii) They conflict at no pair of \(C\), only at admitted pairs outside it that both their transports translate: the contract does not contain their conflict. Their answers then agree at every pair of \(C\) that both their transports translate, so no argument from an answer recorded in \(C\) rules out one of them without the other;
````

  - Quotations: “admitted” — found at L8, L11, L15, L31 and 31 more lines; “admitted edit–boundary pair … that both their transports translate” — found at L315.
- **GLM** (reply line 7; does not challenge): Faithful; "that both translate" is what L315 already requires; exclusiveness and exhaustiveness are forced (FC49).
  - Quotations: “that both translate” — not found in the text; found in the brief; “admitted edit–boundary pair … that both their transports translate” — found at L315.
- **Goes to a checker** (rule 5): challenged by Mimo. Lines at stake: L317.

#### D10.3 · definition · Test

Lines it formalizes or quotes (from the brief): L317.

- **Mimo** (reply lines 11–15; challenges): The words make a test a record "where their answers there agree"; D10.3 omits the clause and so counts a record where the answers differ; the words stand; D10.3 also adds the record's (K3) premises (I43), not the text's content; R* is called a reflexive-transitive closure in the conventions and "the recorded relations" in D10.3 (leave open); proposes new wording in L317.
  - Proposal `M11-B2` (reply lines 13–15), would change L317:

````
> L317 | recording it, the target's relations as well as its answer, at a pair where their answers agree, is a **test**.
````

  - Quotations: “the recorded relations” — not found in the text; found in the brief; “the target's relations” — found at L317.
- **GLM** (reply lines 9–11; challenges): Parts company in one clause: "where their answers there agree" either restricts what counts as a test or explains; D10.3 defines a test at any conflict pair; the broader reading should stand (where answers differ, recording the target's answer decides between them, which L317 (i) needs); proposes new wording in L317.
  - Proposal `G11-B1` (reply lines 11), would change L317:

````
> L317 | recording it, the target's relations as well as its answer, is a **test**; where their answers there agree, the relations decide, and where they differ, the recorded answer does.
````

  - Quotations: “recording it, the target's relations as well as its answer **where their answers there agree**, is a test.” — found at L317; “Whatever the target does there, at most one of them is an account” — found at L317.
- **Goes to a checker** (rule 5): challenged by GLM and Mimo. Lines at stake: L317.

#### D10.4 · definition · Easy to vary

Lines it formalizes or quotes (from the brief): L317.

- **Mimo** (reply line 17; challenges): See I37; proposal there.
  - Proposal `M11-B3` (reply lines 39–41), would change L317:

````
> L317 | A candidate is **easy to vary**, in the sense used here, for an assessor when it and a rival, neither ruled out for that assessor, pose a problem of the second kind for that assessor;
````

- **GLM** (reply line 13; does not challenge): Faithful under I37; ETV holds of both rivals or neither; the words already say this; no change.
  - Quotations: “it and a rival pose a problem” — found at L317.
- **Goes to a checker** (rule 5): challenged by Mimo. Lines at stake: L317.

#### D10.5 · definition · Problem given χ

Lines it formalizes or quotes (from the brief): L315.

- **Mimo** (reply line 19; challenges): Matches; only the negative clause ("for one who does not, they pose none on that account") is not written, and the maths should carry it; no change to the words.
  - Quotations: “for one who does not, they pose none on that account” — found at L315.
- **GLM** (reply line 15; does not challenge): Faithful; matches S27's footnote.
  - Quotations: “they pose none on that account” — found at L315.
- **Goes to a checker** (rule 5): challenged by Mimo. Lines at stake: L315.

#### D10.6 · definition · Solved

Lines it formalizes or quotes (from the brief): L317.

- **Mimo** (reply line 21; challenges): "While the argument stays usable for that assessor" is dropped; if time is an external index (I90), Out_j holding is the reading and the words survive; the clause "Where the argument uses a claim taken as given, that is j's choice (D9.8)" cites D9.8, which as printed carries no choice clause; the choice is the assessor's (S28) and belongs where ruling out is defined.
  - Quotations: “while the argument stays usable for that assessor” — found at L317; “Where the argument uses a claim taken as given, that is j's choice (D9.8)” — not found in the text; found in the brief.
- **GLM** (reply line 17; challenges **OWNER QUESTION**): Faithful, and the state reading is right; the text is silent on a corollary: if the argument that ruled a rival out ceases to be usable, the problem reopens and a candidate can become easy to vary again; S20 ("Once the explanation is rescued, the mistake shouldn't be able to creep back in") points the other way; no wording, since "what must happen to a problem's resolution is the owner's to settle (S21)"; records that the words permit reopening.
  - Quotations: “solved **while** the argument stays usable” — not found in the text; not in the brief; “Once the explanation is rescued, the mistake shouldn't be able to creep back in” — not found in the text; found in the brief.
- **Goes to a checker** (rule 5): challenged by GLM and Mimo. Lines at stake: L317.
- Marks: OWNER QUESTION points present.

#### D8.2 · definition · Conflict

Lines it formalizes or quotes (from the brief): L315.

- **Mimo** (reply lines 5–9; challenges): As for D10.2: D8.2 drops "admitted" (proposal printed under D10.2).
  - Proposal `M11-B1` (reply lines 7–9; printed in full under D10.2 above), would change L317.
  - Quotations: “admitted” — found at L8, L11, L15, L31 and 31 more lines; “admitted edit–boundary pair … that both their transports translate” — found at L315.
- **GLM:** no point on this item.
- **Goes to a checker** (rule 5): challenged by Mimo. Lines at stake: L317.

#### D8.3 · definition · Offer; rivals

Lines it formalizes or quotes (from the brief): L315.

- **Mimo** (reply line 27; does not challenge): Named among the items with nothing to add.
- **GLM:** no point on this item.
- **Goes to no checker**: no point challenges it and it is not one of the twelve; recorded under rule 7 below.

#### D9.8 · definition · Ruled out; not ruled out

Lines it formalizes or quotes (from the brief): L315.

- **Mimo** (reply line 27; does not challenge): Named among the items with nothing to add.
- **GLM:** no point on this item.
- **Goes to no checker**: no point challenges it and it is not one of the twelve; recorded under rule 7 below.

#### FC46 · claim · A conflict inside the contract: at most one account

Lines it formalizes or quotes (from the brief): L317.

- **Mimo** (reply line 27; does not challenge): Nothing to add on its formal statement.
- **Mimo** (reply line 55; challenges): Attack through scope: a hand model with ℰ′ answering only on part of C, both meeting (E) on their stated scopes, conflicting at a pair of C under the strict reading of "differ" (rests on I27, I16, I21 and that reading, and on reading "meets (E) on a contract" as meeting at the pairs within the scope); the sentence that would fix it is not given in this part, and the reader names the clause needed.
  - Inline proposal (reply line 55; written in the reader's running text, not in a fence), would change none — a clause for a sentence the reader does not have; no line named:

````
every pair of the contract lies within the candidate's stated scope
````

  - Quotations: “differ” — found at L23, L37, L41, L45 and 29 more lines; “meets (E) on a contract” — found at L317.
- **GLM** (reply line 19; does not challenge): Says what the sentence says.
  - Quotations: “at most one of them is an account of p” — found at L317; “whether or not anyone records what it does” — found at L317; “two accounts on C conflict only outside it” — not found in the text; not in the brief.
- **GLM** (reply line 53; does not challenge): Attack through hypothetical relations: two candidates meeting under different hypothetical relations conflict at a pair of C and would both be accounts if "account" meant meeting under some relations; the text settles it against the attack (the thing explained is however it is, S28; "whether or not anyone records what it does"), so FC46 holds; the maths should say that Acc is meeting under the target's relations as they are.
  - Quotations: “account” — found at L8, L43, L61, L69 and 37 more lines; “could meet under some relations of the target's components” — not found in the text; not in the brief; “under the target's own relations R*” — not found in the text; found in the brief; “1. That is correct” — not found in the text; found in the brief; “whether or not anyone records what it does” — found at L317.
- **Goes to a checker** (rule 5): challenged by Mimo. Lines at stake: L317.

#### FC47 · claim · A test at a conflict pair rules out at least one, for an assessor who can use it

Lines it formalizes or quotes (from the brief): L317.

- **Mimo** (reply line 23; challenges): The formal unpacks "for an assessor who can use it" into forms admitted, scope and live (K3) premises; a reading, not content the words force; the words stand.
  - Quotations: “for an assessor who can use it” — found at L317; “can use it” — found at L8, L17, L55, L315 and 4 more lines.
- **Mimo** (reply line 57; does not challenge): No counterexample to the qualified formal, only to the words read without the qualification; the words stand.
- **GLM** (reply line 21; does not challenge): Faithful; the unpacking of "for an assessor who can use it" is fair.
  - Quotations: “for an assessor who can use it” — found at L317.
- **GLM** (reply line 57; challenges): Against the claim without I89: a j admitting only MP and MT may be unable to assemble the argument, so (b) fails; against the sentence, no counterexample ("an assessor who can use it").
  - Quotations: “Acc(ℰ) requires Meets_ab” — not found in the text; not in the brief; “an assessor who can use it” — found at L317.
- **Goes to a checker** (rule 5): challenged by GLM and Mimo. Lines at stake: L317.

#### FC48 · claim · No conflict inside the contract: answers agree there

Lines it formalizes or quotes (from the brief): L317.

- **Mimo** (reply line 31; challenges): The H10 case is a counterexample to FC48's consequent under L255's reading of "differs" (change under H10).
  - Proposal `M11-B4` (reply lines 47–49), would change L315:

````
> L315 | Two candidates **conflict** at such a pair \((a,b)\) when their answers there differ, an undetermined answer differing from a determined one, or when each of them could meet (F1), (F2) and (A) there under some relations of the target's components at that pair, each a relation on the component's footprint (Part II), and no such relations let both
````

  - Quotations: “Their answers then agree at every pair of \(C\)” — found at L317; “differs” — found at L45, L245, L255, L397 and 2 more lines; “no conflict in C … Their answers then agree” — not found in the text; found in the brief.
- **Mimo** (reply line 51; challenges): Among further unrecorded choices: FC48's conclusion is written over every pair of C, including pairs one transport does not translate (fixed by the D10.2 proposal); the others named ("admitted" folded into translation; the test's agreement clause; "decided" narrowed; "stays usable" as Out_j) are each to be recorded as inventions or removed by the proposals named.
  - Proposal `M11-B1` (reply lines 7–9; printed in full under D10.2 above), would change L317.
  - Quotations: “admitted” — found at L8, L11, L15, L31 and 31 more lines; “decided” — found at L71, L317; “stays usable” — found at L8, L17, L317.
- **Mimo** (reply line 59; challenges): Attack through partial transports: ℰ′ translates only one pair of C, so at the other "their answers agree" fails (Ans_E′ is not even formed); rests on I17 and a contract with a pair one transport does not translate; the reader says the H10 proposal's second clause removes it.
  - Proposal `M11-B4` (reply lines 47–49; printed in full under FC48 above), would change L315.
  - Quotations: “their answers agree at every pair of C” — not found in the text; not in the brief.
- **GLM** (reply line 23; challenges): Says what the sentence says only under D8.2's reading of "differ" (H10); under the other reading "Their answers then agree at every pair of C" fails (see (c)).
  - Proposal `G11-B3` (reply lines 47), would change L315:

````
> L315 | Two candidates **conflict** at such a pair \((a,b)\) when their answers there differ — an answer undetermined for one of them differing from an answer determined for the other as two determined answers differ — or when each of them could meet (F1), (F2) and (A) there under some relations of the target's components at that pair, each a relation on the component's footprint (Part II), and no such relations let both
````

  - Quotations: “differ” — found at L23, L37, L41, L45 and 29 more lines; “Their answers then agree at every pair of C” — found at L317; “no argument from an answer recorded in C rules out one without the other” — not found in the text; not in the brief.
- **GLM** (reply line 55; challenges): The H10 model is the whole threat; with the L315 wording FC48 holds (resting on the wording and I21).
  - Proposal `G11-B3` (reply lines 47; printed in full under FC48 above), would change L315.
- **Goes to a checker** (rule 5): challenged by GLM and Mimo. Lines at stake: L315, L317.

#### FC49 · claim · The two kinds of problem exclude each other and cover every pair of rivals

Lines it formalizes or quotes (from the brief): L317.

- **Mimo** (reply line 27; does not challenge): Nothing to add on its formal statement.
- **Mimo** (reply line 61; challenges): Attack through "admitted": with the rivals conflicting only at a pair both translate but not admitted, under the words it is neither kind, and the claimed dichotomy fails; under the maths (which drops "admitted") it is kind (ii); the D10.2 proposal removes it, or the maths carries Adm and the text says every pair both transports translate is admitted.
  - Proposal `M11-B1` (reply lines 7–9; printed in full under D10.2 above), would change L317.
  - Quotations: “admitted” — found at L8, L11, L15, L31 and 31 more lines.
- **GLM** (reply line 25; does not challenge): Faithful; forced by D8.2 and D8.3.
  - Quotations: “follows from the definitions” — not found in the text; found in the brief.
- **Goes to a checker** (rule 5): challenged by Mimo. Lines at stake: L317.

#### FC50 · claim · A finer contract makes a problem of the first kind; a narrowed one leaves the problem on p

Lines it formalizes or quotes (from the brief): L317.

- **Mimo** (reply line 25; challenges): (b) is wording beyond the sentence: "a function of p's data and j alone" (see (d)); the words stand and the formal should be tightened.
  - Quotations: “a function of p's data and j alone” — not found in the text; found in the brief; “for a permutation ψ of Γ” — not found in the text; found in the brief.
- **Mimo** (reply line 63; challenges): Attack on (b): narrowing the contract and the declared scope makes j's argument unusable (I42), so a problem for p is posed again; the narrowed contract is not inert for j, and "a function of p's data and j alone" fails (rests on I42, I88); the words survive ("it solves nothing on p"); the formal statement should be weakened.
  - Quotations: “a function of p's data and j alone” — not found in the text; found in the brief; “it solves nothing on p” — found at L317.
- **GLM** (reply line 27; does not challenge): Faithful; "while neither is ruled out" does real work; relies on Part III (not given); (b)'s "holds by construction" adds nothing independent.
  - Quotations: “while neither is ruled out” — found at L317; “makes a new question (Part III)” — found at L317, L335; “Holds by construction” — not found in the text; found in the brief; “it solves nothing on p” — found at L317.
- **GLM** (reply line 59; does not challenge): Attack (a) blocked by "while neither is ruled out"; one untested link, that adding pairs makes a new question (Part III).
  - Quotations: “while neither is ruled out” — found at L317.
- **Goes to a checker** (rule 5): challenged by Mimo. Lines at stake: L317.

#### FC51 · claim · A change that separates two accounts lies outside their shared contract

Lines it formalizes or quotes (from the brief): L317, L568.

- **Mimo** (reply line 25; challenges): (b) is wording beyond the sentences: "for a permutation ψ of Γ" allows counterparts with different footprints (see (d)); the words stand and the formal should be tightened.
  - Quotations: “a function of p's data and j alone” — not found in the text; found in the brief; “for a permutation ψ of Γ” — not found in the text; found in the brief.
- **Mimo** (reply line 65; challenges): (a): under a reading of "finer" as specifying more at the changes already in C, the separating change lies at a pair of C (rests on an alternative to I11; the words stand); (b): ψ need not preserve footprints (hand model with a silent pairing at one pair and answers determined against ⊥); L568's words survive only where the counterparts share a footprint; the formal should say ψ preserves footprints (rests on I24, I16, the H10 reading).
  - Quotations: “must supply” — found at L317, L568.
- **GLM** (reply line 29; challenges): (a) faithful; (b) states less than L568: it checks only the projected relations under (F1), while the sentence also implicates the (F2) equation and (A); the maths should be extended; the words need no change.
  - Quotations: “a claim … must supply it” — found at L317, L568; “meet (F1), (F2) and (A) and differ only in which component has which counterpart” — not found in the text; not in the brief.
- **GLM** (reply line 61; does not challenge): (b) could not be broken within its hypothesis; the (F2) and (A) half of L568 stays untested.
  - Quotations: “must supply it” — found at L317, L568.
- **Goes to a checker** (rule 5): challenged by GLM and Mimo. Lines at stake: L317, L568.

#### FC55 · claim · Nothing in Part VI counts rivals or orders candidates

Lines it formalizes or quotes (from the brief): L317.

- **Mimo** (reply line 27; does not challenge): Nothing to add on its formal statement.
- **Mimo** (reply line 67; does not challenge): The words' "at most one of them is an account of p" and "rules one rival out" are statements about a pair, not counts; no change.
  - Quotations: “at most one of them is an account of \(p\)” — found at L317; “rules one rival out” — found at L317.
- **GLM** (reply line 31; does not challenge): Faithful; the syntactic check is the right kind of check; D8.3's note matches S20.
  - Quotations: “nothing here ranges over the rivals of a candidate” — not found in the text; found in the brief.
- **GLM** (reply line 63; does not challenge): Holds; D10.4's "for some ℰ′" ranges over candidates offered, consistent with S20.
  - Quotations: “for some ℰ′” — not found in the text; found in the brief; “Whether anyone can list all variations that still fit is beside the point” — not found in the text; found in the brief.
- **Goes to no checker**: no point challenges it and it is not one of the twelve; recorded under rule 7 below.

#### I37 · invention · 'Easy to vary' is relative to an assessor

Lines it formalizes or quotes (from the brief): L317.

- **Mimo** (reply lines 37–43; challenges): By inheritance the text fixes that easy to vary is relative to an assessor (a problem is "for that assessor"), but the inheritance is unstated, and the phrase is used more widely in the project (S33–S34); proposes new wording in L317 (writes I37 in; the reader says it touches only "easy to vary", not what hard to vary covers).
  - Proposal `M11-B3` (reply lines 39–41; printed in full under D10.4 above), would change L317.
  - Quotations: “for that assessor” — found at L317, L369; “pose a problem of the second kind” — found at L317; “easy to vary” — found at L69, L317, L526.
- **GLM** (reply lines 39–43; challenges): The text settles it implicitly (a problem is posed "for that assessor"); since the alternatives were live enough to invent, the words should say it; proposes new wording in L317 (writes I37 in).
  - Proposal `G11-B2` (reply lines 41), would change L317:

````
> L317 | A candidate is **easy to vary**, for an assessor, in the sense used here, when it and a rival pose, for that assessor, a problem of the second kind;
````

  - Quotations: “for that assessor” — found at L317, L369; “a problem of the second kind” — found at L317; “for some assessor” — not found in the text; found in the brief.
- **Goes to a checker** (rule 5): challenged by GLM and Mimo. Lines at stake: L317.

#### H10 · H-entry · "differ" read two ways (D8.2 against D6.4)

Lines it formalizes or quotes (from the brief): L255, L315.

- **Mimo** (reply line 31; challenges): The check's case is a counterexample to FC48's consequent and to L317 (ii)'s "Their answers then agree at every pair of C" under the reading L255 carries ("differs" only between two determined answers): E1 answers 0, E2 answers ⊥ with a background component emptying Sol_E; it tells against the text only insofar as one word is used in two places with no record of which reading each carries; L317's own argument forces the reading where an undetermined answer differs from a determined one; rests on I21 and that reading (change under H10 in (c)).
  - Proposal `M11-B4` (reply lines 47–49; printed in full under FC48 above), would change L315.
  - Quotations: “Their answers then agree at every pair of \(C\)” — found at L317; “differs” — found at L45, L245, L255, L397 and 2 more lines; “no conflict in C … Their answers then agree” — not found in the text; found in the brief.
- **Mimo** (reply lines 45–49; challenges): The text does not fix it: neither L315 nor L255 records which answers differ from which, and I21 records only ⊥ = ⊥; fix it in the conflict clause (L255 keeps its own reading); proposes new wording in L315.
  - Proposal `M11-B4` (reply lines 47–49; printed in full under FC48 above), would change L315.
- **GLM** (reply lines 35–49; challenges): The text does not settle which reading of "differ" L315 carries; L317 (ii) holds under D8.2's reading and fails under D6.4's (H10's model); D8.2's should stand, since L317 (ii)'s argument needs a 0/⊥ pair to count as a conflict; proposes new wording in L315; L255 keeps its reading, and the register should carry the two readings as distinct entries.
  - Proposal `G11-B2` (reply lines 41; printed in full under I37 above), would change L315.
  - Proposal `G11-B3` (reply lines 47; printed in full under FC48 above), would change L315.
  - Quotations: “differ” — found at L23, L37, L41, L45 and 29 more lines; “for that assessor” — found at L317, L369; “a problem of the second kind” — found at L317; “for some assessor” — not found in the text; found in the brief; “Their answers then agree at every pair of C, so no argument from an answer recorded in C rules out one of them without the other” — found at L317.
- **Goes to a checker** (rule 5): challenged by GLM and Mimo. Lines at stake: L315.

#### Part 11: items no point addresses

Items of this part on which neither reader made any point (both replies read whole): D8.1. Each is recorded under rule 7 in section 6 unless a point on it in another part sends it to a checker.

### Part 12: Arguments, criticism and reason use

Brief: `tests/S104 Round 2 - the maths against the words - part 12, Arguments, criticism and reason use.md`. Replies: `s104_maths_mimo_12.response.txt` (Mimo), `s104_maths_glm_12.response.txt` (GLM).

#### D9.1 · definition · Claims

Lines it formalizes or quotes (from the brief): L397.

- **Mimo** (reply lines 42–47; challenges): "Inconsistent" is read classically; the words only set structural reading against "logical equivalence alone", presupposing a classical background without saying so; proposes "classically inconsistent" in L397's sentence "An argument is usable by…" (writes I38 in).
  - Proposal `M12-B6` (reply lines 44–47), would change L397:

````
replaces L397, the sentence beginning "An argument is usable by", whole as it would stand
An argument is usable by \(j\) when each of its steps is (K2), and it rules out a claim when the claim is classically inconsistent with its conclusion and the claim's denial is not among its premises (below).
````

  - Quotations: “inconsistent” — found at L8, L397; “logical equivalence alone” — found at L397.
- **GLM** (reply line 19; does not challenge): Named among the items with nothing to add.
- **Goes to a checker** (rule 5): challenged by Mimo. Lines at stake: L397.

#### D9.2 · definition · Argument

Lines it formalizes or quotes (from the brief): L397.

- **Mimo** (reply line 55; does not challenge): Named among the items with nothing to add.
- **GLM** (reply line 19; does not challenge): Named among the items with nothing to add.
- **Goes to no checker**: no point challenges it and it is not one of the twelve; recorded under rule 7 below.

#### D9.3 · definition · Essential premises

Lines it formalizes or quotes (from the brief): L387.

- **Mimo** (reply line 55; does not challenge): Named among the items with nothing to add.
- **GLM** (reply line 19; does not challenge): Named among the items with nothing to add.
- **Goes to no checker**: no point challenges it and it is not one of the twelve; recorded under rule 7 below.

#### D9.4 · definition · Live

Lines it formalizes or quotes (from the brief): L393.

- **Mimo** (reply lines 3–8; challenges): The maths reads "a step of the same argument as u" as a step below u; the words say only "of the same argument"; on the words a premise can be made live by a step above u (model (1) under FC69), and on the two-step loop the words give two fixed points, so Usable is not a definition; the maths should stand and the words carry the direction; proposes a new Live clause of L393 (writes I40's below-reading in).
  - Proposal `M12-B1` (reply lines 5–8), would change L393:

````
replaces L393, the \(\operatorname{Live}_j(d;u)\) clause, whole as it would stand
\(\operatorname{Live}_j(d;u)\): \(d\) is the conclusion of a step of the same argument as \(u\), lower in the tree than \(u\), that is usable by \(j\), or a premise \(j\) tentatively accepts, having taken it up, for whatever reason, and not withdrawn it, whether or not \(j\) holds an explanation of \(d\); a claim \(j\) has never taken up is not live for \(j\).
````

  - Quotations: “a step of the same argument as \(u\)” — found at L393; “of the same argument” — found at L393.
- **GLM** (reply line 19; does not challenge): Named among the items with nothing to add.
- **Goes to a checker** (rule 5): challenged by Mimo. Lines at stake: L393.

#### D9.5 · definition · Form and scope

Lines it formalizes or quotes (from the brief): L393.

- **Mimo** (reply lines 35–40; challenges): "Within the contract, grain and boundary j has declared" does not say whether grain and boundary are contained or equal; the maths takes containment for the contract and equality for the other two, one way and not the words'; the words should fix it; proposes a new Scope clause of L393 (writes I42 in).
  - Proposal `M12-B5` (reply lines 37–40), would change L393:

````
replaces L393, the \(\operatorname{Scope}_j(u)\) clause, whole as it would stand
\(\operatorname{Scope}_j(u)\): \(u\)'s contract is contained in the contract \(j\) has declared for it, and \(u\)'s grain and boundary are the grain and boundary \(j\) has declared for it;
````

  - Quotations: “within the contract, grain and boundary \(j\) has declared” — found at L393.
- **GLM** (reply line 5; does not challenge): The maths reads "applied within the contract … j has declared" as containment with equality of grain and boundary; "within" bears out containment, which the text settles; nothing to change.
  - Quotations: “applied within the contract … j has declared” — found at L393; “Within” — found at L43, L225, L393, L608 and 1 more lines.
- **Goes to a checker** (rule 5): challenged by Mimo. Lines at stake: L393.

#### D9.6 · definition · Usability (K2)

Lines it formalizes or quotes (from the brief): L390.

- **Mimo** (reply lines 3–8; challenges): As for D9.4 (the reply heads the entry "D9.4, D9.6 · L390, L393 · FC69").
  - Proposal `M12-B1` (reply lines 5–8; printed in full under D9.4 above), would change L393.
  - Quotations: “a step of the same argument as \(u\)” — found at L393; “of the same argument” — found at L393.
- **GLM** (reply line 19; does not challenge): Named among the items with nothing to add.
- **Goes to a checker** (rule 5): challenged by Mimo. Lines at stake: L393.

#### D9.7 · definition · Rules out

Lines it formalizes or quotes (from the brief): L397.

- **Mimo** (reply lines 42–47; challenges): As for D9.1 (the reply heads the entry "D9.1, D9.7 · L397"; proposal printed under D9.1).
  - Proposal `M12-B6` (reply lines 44–47; printed in full under D9.1 above), would change L397.
  - Quotations: “inconsistent” — found at L8, L397; “logical equivalence alone” — found at L397.
- **GLM** (reply line 7; does not challenge): The maths keeps both levels (a step rules out a case, an argument a claim); restricting the non-circularity check to leaves matches L397's "argument steps whose leaves are premises"; they agree.
  - Quotations: “argument steps whose leaves are premises” — found at L397.
- **Goes to a checker** (rule 5): challenged by Mimo. Lines at stake: L397.

#### D9.8 · definition · Ruled out; not ruled out

Lines it formalizes or quotes (from the brief): L315.

- **Mimo** (reply line 55; does not challenge): Named among the items with nothing to add.
- **GLM** (reply line 19; does not challenge): Named among the items with nothing to add.
- **Goes to no checker**: no point challenges it and it is not one of the twelve; recorded under rule 7 below.

#### D9.9 · definition · (K3)

Lines it formalizes or quotes (from the brief): L395.

- **Mimo** (reply lines 12–17; challenges): Two gaps: the words make (K3) unconditional while the machinery needs the conditional live for j and modus tollens admitted (model (1) under FC71); "and nothing narrower" read flatly says no argument of j rules out B alone, which an unrelated argument can (model (2)); the machinery gives "from those premises alone"; the maths' reading should stand; proposes a new L395 (writes I43's conditions in).
  - Proposal `M12-B2` (reply lines 14–17), would change L395:

````
replaces L395 in full
For \(T\land B\land I\Rightarrow O\), an argument usable by \(j\) that rules out \(O\), where that conditional is live for \(j\) and \(j\) admits modus tollens, rules out \(T\land B\land I\) together for \(j\), and from those premises alone rules out nothing narrower. (K3)
````

  - Quotations: “and nothing narrower” — found at L395; “from those premises alone” — not found in the text; found in the brief.
- **GLM** (reply lines 9–13; challenges): Small parting: the maths makes (K3) conditional on the conditional being live and modus tollens admitted, conditions (K2) itself demands, so the words should carry them; real parting: the maths reads "and nothing narrower" as "from those premises no argument at all rules out T, B or I", stronger than the sentence's natural reading, and false given that admitted forms need not be classically sound (L397; model in (d)); the words should stand and the maths should read "nothing narrower" as scoping the argument's ruling-out (proposal under I43).
  - Proposal `G12-B3` (reply lines 47–49), would change L395:

````
> L395 | For \(T\land B\land I\Rightarrow O\), an argument usable by \(j\) that rules out \(O\), with the conditional live for \(j\) and the step it needs admitted, rules out \(T\land B\land I\) together for \(j\), and by that ruling-out nothing narrower. (K3)
````

  - Quotations: “and nothing narrower” — found at L395; “for someone who admits its inference form” — found at L397; “nothing narrower” — found at L395.
- **Goes to a checker** (rule 5): challenged by GLM and Mimo. Lines at stake: L395.

#### D9.10 · definition · Criticism and bearing (K1)

Lines it formalizes or quotes (from the brief): L377, L380.

- **Mimo** (reply lines 19–26; challenges): Here the maths should change: Bearing(c,z,p) is defined from data supplied with c, so p drops out and two criticisms differing only in p bear alike, while the words make bearing relative to p; the words should also say who carries ℰ_c when the connection does not single one out; proposes a new L377 (writes H12's choice for ℰ_c in and refuses its choice for p_δ).
  - Proposal `M12-B3` (reply lines 21–24), would change L377:

````
replaces L377 in full
Let \(p_\delta\) be formed from \(z\), \(\delta\) and \(p\) as the question whether \(z\) has \(\delta\) in respect of \(p\), and \(\mathcal E_c\) the explanatory candidate (Part V) for \(p_\delta\) whose organization is the criticism's connection from \(g\) to \(\delta\), with its transport and its identified commitments; where the connection does not single one out, the criticism carries \(\mathcal E_c\).
````

  - Quotations: “in respect of \(p\)” — found at L377; “the explanatory candidate” — found at L377.
- **GLM** (reply line 15; challenges): Matches; the one parting is that the text constructs p_δ ("Let p_δ be the question whether z has δ in respect of p") while the maths supplies it with c (H12); the text should stand.
  - Quotations: “Let p_δ be the question whether z has δ in respect of p” — found at L377.
- **Goes to a checker** (rule 5): challenged by GLM and Mimo. Lines at stake: L377.

#### D9.11 · definition · Reason use

Lines it formalizes or quotes (from the brief): L383, L385.

- **Mimo** (reply lines 28–33; challenges): "Structural map", "role bindings", "the same transition", "operative deliberative rule" are defined nowhere; the maths' precisification makes reason use decidable where the words leave it open; the four phrases should stay open (S21), but the words should say the data is declared; proposes a new L385 (writes I47's declared-inputs choice in).
  - Proposal `M12-B4` (reply lines 30–33), would change L385:

````
replaces L385 in full
A response uses a reason when a structural map from the represented objection into the response suborganization preserves role bindings, sends content-preserving recodings to the same transition, sends content changes to the changes specified by the operative deliberative rule, and lands on an active route; the map, the role bindings, the recodings, the changes and the operative deliberative rule are declared for the system, and reason use holds when some declaration of them makes all four conditions hold.
````

  - Quotations: “structural map” — found at L385; “role bindings” — found at L385, L409; “the same transition” — found at L385, L409; “operative deliberative rule” — found at L385.
- **GLM** (reply line 17; does not challenge): Every operative word of the sentence is undefined, so the maths fills a silence; the independence reading ("does not give") is right; a universal reading would be too strong.
  - Quotations: “does not give” — found at L385; “structural map” — found at L385; “role bindings” — found at L385, L409; “the same transition” — found at L385, L409; “operative deliberative rule” — found at L385.
- **Goes to a checker** (rule 5): challenged by Mimo. Lines at stake: L385.

#### FC56 · claim · Ruling out grows with what is accepted; withdrawal rules nothing out; absence rules out nothing

Lines it formalizes or quotes (from the brief): L393, L397.

- **Mimo** (reply line 49; challenges): (b) is the sentence exactly; (a) (monotonicity in what j accepts and admits) is not a sentence of the text; the text asserts only the two clauses quoted.
- **Mimo** (reply line 88; challenges): Monotonicity cannot fail at any size; it can break in grain and boundary: j declares a coarser grain for u, Scope fails and a ruling out is lost; the claim excludes this by holding grain and boundary fixed, which the words do not; it rests on I42's equality.
- **GLM** (reply lines 69–75; challenges): A near miss: after withdrawing d, the withdrawal taken up as a claim W with a free form from W to ¬d rules d out, by j's unsound form on the withdrawal's record, not by the withdrawal; "it does not rule the conclusion out" read without the same line's choice clause says more than (K2) gives; proposes a new L393 sentence (belonging with matter 9's fix); part (a)'s monotonicity could not be broken.
  - Proposal `G12-B6` (reply lines 71–73), would change L393:

````
> L393 | Withdrawing a premise makes the step unusable when nothing else keeps that premise live; it does not by itself rule the conclusion out.
````

  - Quotations: “does not rule the conclusion out” — found at L393; “d is withdrawn” — not found in the text; not in the brief; “it does not rule the conclusion out” — found at L393; “the ruling out is a choice the person using it made” — found at L397.
- **Goes to a checker** (rule 5): challenged by GLM and Mimo. Lines at stake: L393.

#### FC68 · claim · A failed answer stays failed

Lines it formalizes or quotes (from the brief): L369.

- **Mimo** (reply line 51; challenges): (a) is the text's; (b) and (c) have no sentence of the text behind them; they report what the argument machinery does with a failed answer and rest on I89's free form (see (d)).
- **Mimo** (reply line 90; challenges): (b) can break: j admits modus ponens only and has an argument against Ans_p(a,b) = y, but nothing joins the answer to (E), so X_j(Acc(ℰ)) is empty; (b) holds only because I89's free form and I20's encoding supply the link; "the forms are admitted" should say which forms.
  - Quotations: “the forms are admitted” — not found in the text; found in the brief; “\(\operatorname{Ans}_E(\tau a,\sigma b)=y\)” — found at L369; “\(\operatorname{Ans}_p(a,b)\neq y\)” — not found in the text; not in the brief.
- **GLM** (reply line 77; challenges): A wording caution on part (c): each candidate's ruling out needs its own premise live, so the lapse is "for all alike" only if the lapsed premise is the shared one; the reader says L369 does not state the lapsing part at all and any failure tells against the claim's wording, not the text; the formal statement should say "the shared premise" (L369 as it stands contains "If a premise about them ceases to be live, the argument is not usable (K2) and those candidates are no longer ruled out by it, every such candidate alike").
  - Quotations: “If a premise of that argument stops being live, the ruling out lapses for all alike.” — not found in the text; found in the brief; “the shared premise” — not found in the text; not in the brief; “Ans_p(a,b) = y” — not found in the text; found in the brief.
- **Goes to a checker** (rule 5): challenged by GLM and Mimo. Lines at stake: L369.

#### FC69 · claim · (K2) is well founded; the loop an earlier study read closes below the step

Lines it formalizes or quotes (from the brief): L390, L393.

- **Mimo** (reply lines 3–8; challenges): As for D9.4: without a direction (K2) answers nothing (proposal printed under D9.4).
  - Proposal `M12-B1` (reply lines 5–8; printed in full under D9.4 above), would change L393.
  - Quotations: “a step of the same argument as \(u\)” — found at L393; “of the same argument” — found at L393.
- **Mimo** (reply line 92; challenges): Two models: (1) a step above u makes u's premise live on the words, not under I40; (2) a two-step loop gives both usable or both not; "holds" holds only under the invention; the words give no answer.
  - Proposal `M12-B1` (reply lines 5–8; printed in full under D9.4 above), would change L393.
- **GLM** (reply line 79; challenges): Attacked through the tree assumption: with arguments as finite acyclic graphs (I40's alternative (b)) "below" is ill-defined; an invention-bound attack; it strengthens the case for writing "below u" in (I40).
  - Proposal `G12-B2` (reply lines 37–39), would change L393:

````
> L393 | … \(\operatorname{Live}_j(d;u)\): \(d\) is the conclusion of a step below \(u\) in the same argument that is usable by \(j\), or a premise \(j\) tentatively accepts, having taken it up, for whatever reason, and not withdrawn it, whether or not \(j\) holds an explanation of \(d\); a claim \(j\) has never taken up is not live for \(j\).
````

  - Quotations: “below u” — not found in the text; found in the brief.
- **Goes to a checker** (rule 5): challenged by GLM and Mimo. Lines at stake: L393.

#### FC70 · claim · Withdrawing a premise that is live twice over leaves the step usable

Lines it formalizes or quotes (from the brief): L393.

- **Mimo** (reply line 10; challenges): The formal statement is the narrower one and should stand (a premise live twice over stays live after withdrawal); the sentence says more than (K2) gives (wording under matter 9).
  - Proposal `M12-B9` (reply lines 115–118), would change L393:

````
replaces L393, the first sentence, whole as it would stand
Withdrawing a premise that is live only by acceptance makes the step unusable; it does not rule the conclusion out.
````

- **Mimo** (reply line 94; challenges): No model breaks the formal claim; the sentence breaks in the configuration FC70 exhibits (see matter 9).
  - Proposal `M12-B9` (reply lines 115–118; printed in full under FC70 above), would change L393.
- **GLM** (reply line 81; challenges): The attack is matter 9 itself: the claim holds because the maths quietly restricts L393's first clause to premises live by acceptance.
  - Proposal `G12-B7` (reply lines 95–97), would change L393:

````
> L393 | Withdrawing a premise makes the step unusable when nothing else keeps that premise live; it does not by itself rule the conclusion out.
````

- **Goes to a checker** (rule 5): challenged by GLM and Mimo. Lines at stake: L393.

#### FC71 · claim · (K3): a failed prediction rules out the conjunction, and nothing narrower

Lines it formalizes or quotes (from the brief): L395.

- **Mimo** (reply lines 12–17; challenges): As for D9.9 (the reply heads the entry "D9.9 · L395 · FC71"; proposal printed under D9.9).
  - Proposal `M12-B2` (reply lines 14–17; printed in full under D9.9 above), would change L395.
  - Quotations: “and nothing narrower” — found at L395; “from those premises alone” — not found in the text; found in the brief.
- **Mimo** (reply line 96; challenges): Two models: (1) with modus ponens only, nothing concludes ¬(T ∧ B ∧ I) while O is ruled out; (2) an unrelated accepted s, s → ¬B rules out B alone; both break the words, not I43.
  - Proposal `M12-B2` (reply lines 14–17; printed in full under D9.9 above), would change L395.
- **GLM** (reply line 67; challenges): Hand counterexample to part (ii): j admits a free, classically unsound form F from ¬O to ¬T (D9.7 allows it), so from exactly the premises of the failed prediction T alone is ruled out (rests on I38, I89); it breaks I43's strong reading of "nothing narrower", not the text read as scoping the argument; the I43 wording removes it; the ruling out by F is j's choice (L397, S28).
  - Proposal `G12-B3` (reply lines 47–49; printed in full under D9.9 above), would change L395.
  - Quotations: “nothing narrower” — found at L395.
- **Goes to a checker** (rule 5): challenged by GLM and Mimo. Lines at stake: L395.

#### FC72 · claim · The block on a premise that is the denial, and a premise taken as given

Lines it formalizes or quotes (from the brief): L397.

- **Mimo** (reply line 98; challenges): Two ways: (1) on a dependence reading, a leaf stating ¬φ that no step uses should not block a ruling out that does not depend on it, and FC72 (a) then fails (it holds on I39's leaf-level reading); (2) a clash: a record leaf carrying "r → ¬Acc(ℰ)" made from a record of ¬Acc(ℰ) makes the "made from" clause and the "premise taken as given" sentence of the same line contradict each other; the gamble sentence should stand (it matches S27) and the clause be narrowed (the I39 proposal).
  - Proposal `M12-B7` (reply lines 67–70), would change L397:

````
replaces L397, the sentence beginning "An argument does not rule out a claim", whole as it would stand
An argument does not rule out a claim when the claim's denial is among its premises, alone or joined to other claims by "and", read structurally as non-circular dependence reads identity (Part V) and not by logical equivalence alone; nor does an argument whose record leaf was made from a claim rule out that claim's denial, where a record leaf is made from a claim when the event it refers to is an occurrence of that claim.
````

  - Quotations: “non-circular dependence” — found at L255, L257, L273, L275 and 4 more lines; “made from” — found at L211, L397; “premise taken as given” — found at L397.
- **GLM** (reply line 83; does not challenge): Tried flattening, equivalence and intermediate conclusions; holds.
- **Goes to a checker** (rule 5): challenged by Mimo. Lines at stake: L397.

#### FC73 · claim · Inconsistent accepted premises rule out a claim and its denial alike

Lines it formalizes or quotes (from the brief): L397.

- **Mimo** (reply line 100; does not challenge): Holds because the words say "can rule out"; read as "arguments from them rule out", a model with only conjunction steps breaks the sentence.
  - Quotations: “can rule out” — found at L317, L397, L429; “arguments from them rule out” — not found in the text; not in the brief.
- **GLM** (reply line 85; does not challenge): A paraconsistent reading breaks the witness, but that is I38's alternative and L397 commits to an explosive reading; holds as the text reads.
- **Goes to no checker**: no point challenges it and it is not one of the twelve; recorded under rule 7 below.

#### FC74 · claim · A criticism occurrence can exist without bearing

Lines it formalizes or quotes (from the brief): L383.

- **Mimo** (reply line 102; challenges): The witness rests on H12 and on D12.5's representation being present; if the model carries no organization representing g as the premise of a criticism, L383's own condition is not met and the witness shows data rather than a criticism (rests on I45, H12).
  - Quotations: “An adverse signal is not a criticism until an organization represents it as the premise of a criticism alleging a defect in a target” — found at L383.
- **GLM** (reply line 87; does not challenge): Tried making every connection an account by fiat; L383 forbids it and the witness respects it; holds.
  - Quotations: “A criticism occurrence can exist when (K1) fails” — found at L383.
- **Goes to a checker** (rule 5): challenged by Mimo. Lines at stake: L383.

#### FC76 · claim · Reason use gives neither bearing nor usability

Lines it formalizes or quotes (from the brief): L385.

- **Mimo** (reply lines 28–33; challenges): As for D9.11 (the reply heads the entry "D9.11 · L385 · FC76"; proposal printed under D9.11).
  - Proposal `M12-B4` (reply lines 30–33; printed in full under D9.11 above), would change L385.
  - Quotations: “structural map” — found at L385; “role bindings” — found at L385, L409; “the same transition” — found at L385, L409; “operative deliberative rule” — found at L385.
- **Mimo** (reply lines 104–109; challenges): Holds by construction under I47; the sentence can break: j uses an objection and also takes up its claim with "d → ¬Acc(ℰ)" and modus ponens, so an argument from the objection is usable; the sentence should say "by itself"; proposes a new last sentence of L385.
  - Proposal `M12-B8` (reply lines 106–109), would change L385:

````
replaces L385, the last sentence, whole as it would stand
Using an objection does not by itself give it bearing (K1) or make any argument from it usable (K2).
````

  - Quotations: “by itself” — found at L8, L159, L313, L315 and 3 more lines.
- **GLM** (reply line 89; does not challenge): Holds, resting on I47 being written in (the proposal under I47), so that the independence is the text's own.
- **Goes to a checker** (rule 5): challenged by Mimo. Lines at stake: L385.

#### I38 · invention · Claims, their denials, and 'inconsistent with its conclusion'

Lines it formalizes or quotes (from the brief): L397.

- **Mimo** (reply line 63; challenges): Not settled: the words name "inconsistent" and "and" and set structural reading against "logical equivalence alone", but say nothing of language or classicality; nothing says an admitted form is classically sound; the D9.1 wording writes classicality in; the soundness of forms should stay open (S21, S27).
  - Proposal `M12-B6` (reply lines 44–47; printed in full under D9.1 above), would change L397.
  - Quotations: “inconsistent” — found at L8, L397; “logical equivalence alone” — found at L397; “for someone who admits its inference form” — found at L397.
- **GLM** (reply lines 27–31; challenges): Not settled; the text excludes the equivalence reading for premises and states FC73's result, which needs an explosive notion, so alternative (a) is out; between classical inconsistency and situation-disjointness no claim here divides; proposes the text stay open, or, if anything is said, a colourless gloss in L397.
  - Proposal `G12-B1` (reply lines 29–31), would change L397:

````
> L397 | … it rules out a claim when the claim is inconsistent with its conclusion — no situation in which both hold — and the claim's denial is not among its premises (below).
````

  - Quotations: “inconsistent with” — found at L8, L397; “RO does not depend on j” — not found in the text; found in the brief.
- **Goes to a checker** (rule 5): challenged by GLM and Mimo. Lines at stake: L397.

#### I39 · invention · 'Among its premises', read structurally; records made from a claim

Lines it formalizes or quotes (from the brief): L397.

- **Mimo** (reply lines 65–72; challenges): Partly settled: premises are leaves and "alone or joined to other claims by 'and'" fixes conjuncts; "read structurally as non-circular dependence reads identity (Part V)" points at NC1, itself undefined (I24), so the structural reading stays open; "made from a claim" is used and never defined, and creates a clash (FC72); proposes a new sentence of L397 (writes a narrowing in, named).
  - Proposal `M12-B7` (reply lines 67–70; printed in full under FC72 above), would change L397.
  - Quotations: “alone or joined to other claims by 'and'” — found at L397; “read structurally as non-circular dependence reads identity (Part V)” — found at L397; “made from a claim” — found at L397.
- **GLM** (reply line 33; challenges): The text settles the structural reading ("read structurally as non-circular dependence reads identity (Part V) and not by logical equivalence alone"); "made from" is primitive in the text too, and what makes a record made from a claim belongs with records (D11.1).
  - Quotations: “read structurally as non-circular dependence reads identity (Part V) and not by logical equivalence alone” — found at L397; “Made from” — found at L211, L397; “whose record leaf was made from a claim” — found at L397.
- **Goes to a checker** (rule 5): challenged by GLM and Mimo. Lines at stake: L397.

#### I40 · invention · Live through a step: a step below, and essential premises

Lines it formalizes or quotes (from the brief): L387, L393.

- **Mimo** (reply line 74; challenges): Mostly settled ("argument tree", "whose leaves are premises", "essential premises Prem(u), the premises its inference form uses"); the direction of Live is not; the D9.4 wording fixes it.
  - Proposal `M12-B1` (reply lines 5–8; printed in full under D9.4 above), would change L393.
  - Quotations: “argument tree” — found at L397; “whose leaves are premises” — found at L397; “essential premises \(\operatorname{Prem}(u)\), the premises its inference form uses” — found at L387.
- **GLM** (reply lines 35–39; challenges): Not settled where the live-making step lies; FC69 shows the alternative makes (K2) ill-founded with two fixed points; the text should say "below u"; proposes a new Live clause of L393 (writes I40 in).
  - Proposal `G12-B2` (reply lines 37–39; printed in full under FC69 above), would change L393.
  - Quotations: “below u” — not found in the text; found in the brief.
- **Goes to a checker** (rule 5): challenged by GLM and Mimo. Lines at stake: L393.

#### I41 · invention · Tentative acceptance over time; withdrawal

Lines it formalizes or quotes (from the brief): L393.

- **Mimo** (reply line 76; challenges): Settled as to shape: "having taken it up … and not withdrawn it" fixes taking up, withdrawal and time; that Accepted_j is an input is at L522 (not quoted; relied on); no change.
  - Quotations: “having taken it up … and not withdrawn it” — found at L393.
- **GLM** (reply line 41; challenges): The text settles the substance ("having taken it up … and not withdrawn it"; "a claim j has never taken up is not live"); the evaluation time ξ is the maths' harmless addition.
  - Quotations: “having taken it up … and not withdrawn it” — found at L393; “a claim j has never taken up is not live” — found at L393.
- **Goes to a checker** (rule 5): challenged by GLM and Mimo. Lines at stake: L393.

#### I42 · invention · Scope_j: within the declared contract, grain and boundary

Lines it formalizes or quotes (from the brief): L393.

- **Mimo** (reply line 78; challenges): Not settled; the D9.5 wording writes the choice in.
  - Proposal `M12-B5` (reply lines 37–40; printed in full under D9.5 above), would change L393.
- **GLM** (reply line 43; challenges): "Within the contract" settles containment over equality; whether every step carries an index (alternative (b)) is not said; leave open.
  - Quotations: “Within the contract” — found at L393.
- **Goes to a checker** (rule 5): challenged by GLM and Mimo. Lines at stake: L393.

#### I43 · invention · (K3): what it adds and what 'nothing narrower' says

Lines it formalizes or quotes (from the brief): L395.

- **Mimo** (reply line 80; challenges): Not settled; the D9.9 wording writes it in.
  - Proposal `M12-B2` (reply lines 14–17; printed in full under D9.9 above), would change L395.
- **GLM** (reply lines 45–49; challenges): The text states (K3) without the conditions its own (K2) imposes, and with a "nothing narrower" the strong reading cannot deliver; proposes a new L395 (writes I43's conditions in and scopes "nothing narrower" to the argument).
  - Proposal `G12-B3` (reply lines 47–49; printed in full under D9.9 above), would change L395.
  - Quotations: “nothing narrower” — found at L395.
- **Goes to a checker** (rule 5): challenged by GLM and Mimo. Lines at stake: L395.

#### I47 · invention · Reason use: 'structural map', 'role bindings', 'the same transition', 'operative deliberative rule'

Lines it formalizes or quotes (from the brief): L385.

- **Mimo** (reply line 82; challenges): Not settled; the D9.11 wording writes the declared stance in and leaves the four phrases open.
  - Proposal `M12-B4` (reply lines 30–33; printed in full under D9.11 above), would change L385.
- **GLM** (reply lines 51–57; challenges): All four phrases undefined; since the owner asked that implementation-forced invention be recorded (S36), the text should define them or mark them per system; proposes declaring, not defining, in a new L385 (writes I47's declared-input structure in).
  - Proposal `G12-B4` (reply lines 53–55), would change L385:

````
> L385 | A response uses a reason when a structural map from the represented objection into the response suborganization preserves role bindings, sends content-preserving recodings to the same transition, sends content changes to the changes specified by the operative deliberative rule, and lands on an active route; which map, bindings, recodings, changes and rule count is declared for the system, and nothing in bearing (K1) or usability (K2) fixes them.
````

- **Goes to a checker** (rule 5): challenged by GLM and Mimo. Lines at stake: L385.

#### H12 · H-entry · Bearing: p_δ and ℰ_c supplied with the criticism; the tag names an entry for another sentence (D9.10)

Lines it formalizes or quotes (from the brief): L377.

- **Mimo** (reply line 84; challenges): Not settled; the D9.10 wording makes ℰ_c carried by the criticism and keeps p in play; the tag [I76] does not cover these choices (I76 fills for L161 only), so the entry should stand on its own.
  - Proposal `M12-B3` (reply lines 21–24; printed in full under D9.10 above), would change L377.
- **GLM** (reply lines 59–63; challenges): The text does not leave p_δ to be supplied (it constructs it from z, δ and p) and says the candidate comes "with its transport and its identified commitments"; the maths' "supplied with c" under-reads, and the tag [I76] names another sentence's entry; the register should record the choice as an invention; one gap: "the explanatory candidate" presumes one; proposes a new L377 fragment ("all of which the criticism supplies").
  - Proposal `G12-B5` (reply lines 61–63), would change L377:

````
> L377 | … and \(\mathcal E_c\) the explanatory candidate (Part V) for \(p_\delta\) whose organization is the criticism's connection from \(g\) to \(\delta\), with its transport and its identified commitments, all of which the criticism supplies.
````

  - Quotations: “with its transport and its identified commitments” — found at L377; “supplied with c” — not found in the text; found in the brief; “the explanatory candidate” — found at L377.
- **Goes to a checker** (rule 5): challenged by GLM and Mimo. Lines at stake: L377.

#### NF13 · NF entry

Lines it formalizes or quotes (from the brief): L8.

- **Mimo** (reply line 53; does not challenge): Should stand unchanged: the maths can say only that no predicate is triggered, which is what the sentence says.
- **GLM:** no point on this item.
- **Goes to no checker**: no point challenges it and it is not one of the twelve; recorded under rule 7 below.

#### NF14 · NF entry

Lines it formalizes or quotes (from the brief): L397.

- **Mimo** (reply line 53; does not challenge): Should stand unchanged: the maths can say only that no cost is measured, which is what the sentence says.
- **GLM:** no point on this item.
- **Goes to no checker**: no point challenges it and it is not one of the twelve; recorded under rule 7 below.

#### matter 9 · round-1 matter · A premise live twice over (a leaf that is also a usable step's conclusion): withdrawing it leaves the step usable by the first disjunct of Live, so L393's "Withdrawing a premise makes the step unusable", read without restriction, says more than (K2) gives in that narrow configuration.

Lines it formalizes or quotes (from the brief): L393.

- **Mimo** (reply lines 113–118; challenges): A change is needed: the first clause holds only of a premise live by acceptance; proposes a new first sentence of L393's closing sentences.
  - Proposal `M12-B9` (reply lines 115–118; printed in full under FC70 above), would change L393.
- **GLM** (reply lines 93–99; challenges): The text needs a change: "Withdrawing a premise makes the step unusable" is false of a premise that is also the conclusion of a usable step below; since S20 wants a correction logged once, the sentence should say exactly what withdrawal does; proposes a new L393 sentence (the same wording as under FC56, which it subsumes).
  - Proposal `G12-B7` (reply lines 95–97; printed in full under FC70 above), would change L393.
  - Quotations: “Withdrawing a premise makes the step unusable” — found at L393.
- **Goes to a checker** (rule 5): challenged by GLM and Mimo. Lines at stake: L393.

#### Part 12: items no point addresses

Items of this part on which neither reader made any point (both replies read whole): none. Each is recorded under rule 7 in section 6 unless a point on it in another part sends it to a checker.

### Part 13: Selection, construction and representation

Brief: `tests/S104 Round 2 - the maths against the words - part 13, Selection, construction and representation.md`. Replies: `s104_maths_mimo_13.response.txt` (Mimo), `s104_maths_glm_13.response.txt` (GLM).

#### D12.1 · definition · Selected

Lines it formalizes or quotes (from the brief): L193, L195.

- **Mimo** (reply lines 3–7; challenges): Three departures: (1) "No member of the history represents t, H, or the survival condition" is said of H, a set of pairs, which cannot represent; the maths reads occurrences of a physical history (I52), so the words must change; (2) "represents" is (R)'s, and (R) needs the provenance D12.1 is defining, a loop in the text; (3) the maths lets H be empty and the population one, so Sel can hold with no encounter, where L193 and L195 want at least one pair encountered; and "a survival condition requiring fidelity on H" is narrowed by the maths to exactly Faithful_H; proposes a new L195.
  - Proposal `M13-B1` (reply lines 5–7), would change L195:

````
> L195 | **Selected.** There is a population \(\mathcal T\) of candidate transports, a variation operator \(\mu\) on \(\mathcal T\), a finite history \(H\subseteq C\) of edit–boundary pairs actually encountered in the physical module, at least one pair being so encountered, and a survival condition requiring fidelity on \(H\) and nothing beyond it. A transport **survives on \(H\)** when it is a member of \(\mathcal T\) that meets the survival condition on \(H\); fidelity on \(H\) without membership in \(\mathcal T\) is not survival. No occurrence of the history stands for \(t\), \(H\), or the survival condition, standing for being read in the physical module and not as the representation of (R).
````

  - Quotations: “No member of the history represents \(t\), \(H\), or the survival condition” — found at L195; “represents” — found at L13, L15, L57, L195 and 9 more lines; “determined by its history in the physical module” — found at L193; “actually encountered” — found at L195; “a survival condition requiring fidelity on \(H\)” — found at L195.
- **GLM** (reply lines 5–11; challenges): Two partings: "No member of the history represents" is said of H, whose members cannot represent, so I52's reading is forced and the words should say it; and D12.1 forbids only representations of t, H and the survival condition while L201 and L411 say more, so the words should stand and the maths carry them (H05); proposes a new second sentence of L195 (writes I52's reading and H05's other choice in).
  - Proposal `G13-B2` (reply lines 9–11), would change L195:

````
No occurrence in the selection history represents \(t\), \(H\), the survival condition, \(t\)'s target, or a criticism: a selected transport has no represented target in its history.
````

  - Quotations: “No member of the history represents” — found at L195; “a selected transport has no represented target and no criticism in its history” — found at L201; “No member of the history represents \(t\), \(H\), or the survival condition.” — found at L195.
- **External reader and case card:** C02 (the case card) challenges the sentence this item formalizes (section 4 below); C03 (the case card) challenges the sentence this item formalizes (section 4 below); C04 (the case card) challenges the sentence this item formalizes (section 4 below).
- **Goes to a checker** (rule 5): challenged by GLM and Mimo; challenged by C02 (the case card), C03 (the case card), C04 (the case card). Lines at stake: L195.

#### D12.2 · definition · Constructed

Lines it formalizes or quotes (from the brief): L197.

- **Mimo** (reply line 9; does not challenge): "The organization it carries to" read as the codomain stands; "Part X" is a placeholder the maths resolves to D13.3, D13.8; no proposal.
  - Quotations: “the organization it carries to” — found at L197; “\(t\), or the organization it carries to” — found at L197.
- **GLM** (reply line 13; does not challenge): Says what the sentence says; the disjunction "t, or the organization it carries to" is the sentence's own.
  - Quotations: “t, or the organization it carries to” — found at L197.
- **GLM** (reply line 141; does not challenge): Nothing further to add.
- **External reader and case card:** E03 (the external reader) challenges the sentence this item formalizes (section 3 below); C07 (the case card) challenges the sentence this item formalizes (section 4 below).
- **Goes to a checker** (rule 5): challenged by E03 (the external reader), C07 (the case card). Lines at stake: L197.

#### D12.3 · definition · Declared

Lines it formalizes or quotes (from the brief): L199.

- **Mimo** (reply line 11; does not challenge): "Entered into the model by its author" needs no clause; Dec as neither Sel nor Con is what "Neither of the above" says; the words stand; exclusivity then depends on H05.
  - Quotations: “The transport is entered into the model by its author” — found at L199; “Neither of the above” — found at L199.
- **GLM** (reply line 15; challenges): Dec := ¬Sel ∧ ¬Con matches "Neither of the above" only once Sel carries L201's exclusion; as written the formal core is at odds with itself (I53's gloss against D12.1); the defect is in D12.1.
  - Quotations: “Neither of the above” — found at L199; “Sel has none” — not found in the text; found in the brief.
- **External reader and case card:** C01 (the case card) challenges the sentence this item formalizes (section 4 below).
- **Goes to a checker** (rule 5): challenged by GLM; challenged by C01 (the case card). Lines at stake: L199.

#### D12.4 · definition · Provenance per part; inherited provenance

Lines it formalizes or quotes (from the brief): L211, L405.

- **Mimo** (reply lines 13–17; challenges): The maths adds a unit (each component with its counterpart binding) and a rule of carrying over (I54); the words give the rule (L211, L409) and that content has parts, not the unit; L211's first clause (a carrier keeps its provenance when access is lost) is written nowhere in the formal core and should be carried; proposes a new sentence at L405.
  - Proposal `M13-B2` (reply lines 15–17), would change L405:

````
> L405 | A small binding newly prepared inside received content is construction of that binding, and the rest of the content keeps its inherited provenance. The parts of a content are its components together with their bindings, and inheritance is the carrying of a part's provenance from one carrier to the next on a content-preserving transfer.
````

  - Quotations: “the rest of the content” — found at L405; “A small binding newly prepared…” — found at L405.
- **GLM** (reply lines 17–25; challenges): The maths' per-part provenance is forced: L405's "the rest of the content keeps its inherited provenance" cannot be written on whole transports, and "inherited" as a fourth value contradicts L193's "exactly one of three"; the words leave "inherited" undefined and should say the rule; proposes a new L409 (names I54).
  - Proposal `G13-B4` (reply lines 21–23), would change L409:

````
Use does not by itself construct: received content used as it was received keeps its inherited provenance. "Inherited" is not a fourth provenance: provenance is carried by each part of a transport, each component with its counterpart binding. A part transferred to a new carrier without being newly built keeps the provenance it had; a binding newly built is constructed; and a transport whose history holds both is constructed, while the parts beneath keep the provenance they had.
````

  - Quotations: “the rest of the content keeps its inherited provenance” — found at L405; “inherited” — found at L405, L409; “exactly one of three” — found at L193; “Use does not by itself construct: received content used as it was received keeps its inherited provenance.” — found at L409; “Construction may operate on selected material. Selection may continue to operate beneath construction” — found at L201.
- **Goes to a checker** (rule 5): challenged by GLM and Mimo. Lines at stake: L405, L409.

#### D12.5 · definition · Representation (R)

Lines it formalizes or quotes (from the brief): L205, L208.

- **Mimo** (reply lines 19–25; challenges): "Faithful on c's contract" is asked of a transport into c, whose own ports are not c's; a way to bring c's contract to them is needed (I48), the preimage reading being one; proposes a new L205 (writes I48's preimage reading and L169's commitments in).
  - Proposal `M13-B3` (reply lines 21–23), would change L205:

````
> L205 | An occurrence \(o\) **represents** content \(c\) at grain \(\ell\) when there is a transport from the organization that \(o\) instantiates under the physical module, at grain \(\ell\), to \(c\), faithful on the pairs it sends into \(c\)'s contract and with \(c\)'s commitments as its active components, whose provenance is selected or constructed;
````

  - Quotations: “faithful on \(c\)'s contract” — found at L205, L413.
- **GLM** (reply line 27; does not challenge): Says what (R) says, given I48.
  - Quotations: “c's contract” — found at L205, L413.
- **GLM** (reply line 141; does not challenge): Nothing further to add.
- **External reader and case card:** C03 (the case card) challenges the sentence this item formalizes (section 4 below).
- **Goes to a checker** (rule 5): challenged by Mimo; challenged by C03 (the case card). Lines at stake: L205.

#### D12.6 · definition · Layers

Lines it formalizes or quotes (from the brief): L175, L177.

- **Mimo** (reply line 27; does not challenge): Typed as the words say; L177's "queries are predictions" has no clause in the formal core, and nothing in this group needs it.
  - Quotations: “queries are predictions” — found at L177.
- **GLM** (reply line 29; does not challenge): Matches, keeping L179.
  - Quotations: “nothing assumes either exists” — not found in the text; found in the brief.
- **GLM** (reply line 141; does not challenge): Nothing further to add.
- **Goes to no checker**: no point challenges it and it is not one of the twelve; recorded under rule 7 below.

#### D12.7 · definition · Prediction, violation, surprise

Lines it formalizes or quotes (from the brief): L219, L220, L221.

- **Mimo** (reply lines 29–41; challenges): "A violation occurs when fidelity fails at (a,b)" cannot be written, since fidelity is a condition on the transport as a whole (I18); the maths keeps the conditions at a pair (I50) and should stand, the words change; for surprise the words give a definite H ("its history") while the maths lets any witnessing (𝒯, μ, H) do, and the words should be made definite; proposes new L220 and L221; prediction extended beyond S (I51) is not in these lines.
  - Proposal `M13-B4` (reply lines 31–33), would change L220:

````
> L220 | - **a violation** occurs when the fidelity conditions at \((a,b)\) fail;
````

  - Proposal `M13-B5` (reply lines 37–39), would change L221:

````
> L221 | - **surprise** is a violation of a selected transport at \((a,b)\notin H\), where \(H\) is the history on which that transport was selected.
````

  - Quotations: “a violation occurs when fidelity fails at \((a,b)\)” — found at L220; “its history” — found at L41, L155, L193, L201 and 5 more lines; “Sel(t; 𝒯, μ, H) for some 𝒯, μ, H with (a,b) ∉ H” — not found in the text; found in the brief.
- **GLM** (reply line 31; does not challenge): Matches; I51 flagged and confined.
- **GLM** (reply line 141; does not challenge): Nothing further to add.
- **Goes to a checker** (rule 5): challenged by Mimo. Lines at stake: L220, L221.

#### D12.8 · definition · Responses

Lines it formalizes or quotes (from the brief): L225.

- **Mimo** (reply line 43; challenges): "Lets μ act: the transport is re-tuned within the population" is written t′ ∈ μ*(t), and the maths adds that t′ survives on H ∪ {(a,b)}; that addition says what a response must leave behind, a matter of what must happen to a candidate, which by S21 stays open; no proposal.
  - Quotations: “lets \(\mu\) act: the transport is re-tuned within the population” — found at L225.
- **GLM** (reply line 33; challenges): SelResp uses μ* (reflexive-transitive), so t′ = t is a "selection response", while "lets μ act: the transport is re-tuned" is not zero applications; the words stand; the maths should use μ⁺; no text change.
  - Quotations: “selection response” — found at L225; “lets μ act: the transport is re-tuned within the population” — found at L225.
- **External reader and case card:** C05 (the case card) challenges the sentence this item formalizes (section 4 below).
- **Goes to a checker** (rule 5): challenged by GLM and Mimo; challenged by C05 (the case card). Lines at stake: L225.

#### D12.9 · definition · Value at a pair; underdetermination

Lines it formalizes or quotes (from the brief): L572.

- **Mimo** (reply line 45; challenges **PARKED**): "Value" is fixed nowhere; the maths gives one (I71) and restricts the population to members sharing the codomain's ports and components; the reader calls this "the argument about hard to vary" and leaves it open as parked (S33, S34); no proposal.
- **GLM** (reply line 35; challenges): L572 uses "a different value from t" without defining a transport's value at a pair; I71 supplies one; the words need the definition (under I71).
  - Proposal `G13-B11` (reply lines 95–97), would change L572:

````
The value of a transport at an edit–boundary pair is what it carries there: the translated edit, the translated boundary, and the relations of its organization at them.
````

  - Quotations: “a different value from t” — found at L572.
- **Goes to a checker** (rule 5): challenged by GLM and Mimo. Lines at stake: L572.
- Marks: PARKED points present. 

#### FC77 · claim · Without a physical witness, selection is met by every transport

Lines it formalizes or quotes (from the brief): L195, L205.

- **Mimo** (reply line 49; challenges): The counterexample is to the claim's own wording ("fidelity on ∅ is vacuous" fails because (F2)'s homomorphism clause is on τ as a whole, I18); nothing follows against the text from the model; the residue against the text: L195 as written is met with 𝒯 = {t}, μ the identity and H = ∅, so (R) can hold with no encounter; the L195 proposal removes it, and L481 ("The population is the set of transports the physics and the stated construction admit; …") removes the population of one wherever more are admitted; the claim should read "every transport whose τ is a homomorphism".
  - Proposal `M13-B1` (reply lines 5–7; printed in full under D12.1 above), would change L195.
  - Quotations: “fidelity on \(\emptyset\) is vacuous” — not found in the text; found in the brief; “The population is the set of transports the physics and the stated construction admit; a transport that would need a part every member of the population is b…” — found at L481; “every transport whose \(\tau\) is a homomorphism” — not found in the text; found in the brief.
- **GLM** (reply line 37; challenges): The formal statement's own clause "fidelity on ∅ is vacuous" is false under the maths' (F2) (I18); the claim's wording was wrong (see (b)).
  - Quotations: “fidelity on ∅ is vacuous” — not found in the text; found in the brief.
- **GLM** (reply lines 47–55; challenges): Not a counterexample to the text: its witness is a population of one with no variation, and L481 ("The population is the set of transports the physics and the stated construction admit") is an equality, not D12.1's inclusion (H09); the owner's "A variation is a competitor" (S20) is never provided by an identity operator; it tells against I52's rejected alternative and the hand-set Θ; no text change required, but proposes a sharpened first sentence of L195 (names I52, H09; "competitor" the owner's word); H may stay possibly empty.
  - Proposal `G13-B6` (reply lines 51–53), would change L195:

````
There is a population \(\mathcal T\) of candidate transports — the set of transports the physics and the stated construction admit — a variation operator \(\mu\) on \(\mathcal T\) under which \(t\) has a competitor in \(\mathcal T\), a finite history \(H\subseteq C\) of edit–boundary pairs actually encountered in a physical selection history, and a survival condition requiring fidelity on \(H\).
````

  - Quotations: “The population is the set of transports the physics and the stated construction admit” — found at L481; “A variation is a competitor” — not found in the text; found in the brief; “There is a population \(\mathcal T\) of candidate transports, a variation operator \(\mu\) on \(\mathcal T\), a finite history \(H\subseteq C\) of edit–bound…” — found at L195; “competitor” — not found in the text; found in the brief; “a finite history” — found at L195, L572.
- **GLM** (reply line 135; does not challenge): The held part holds under I18's reading of the homomorphism clause; no reading found making it pointwise; its force is nil once the (b) wording is in.
  - Quotations: “the trivial witness exactly when τ is a homomorphism” — not found in the text; found in the brief.
- **Goes to a checker** (rule 5): challenged by GLM and Mimo; one of the twelve counterexamples the second check reproduced (FC77). Lines at stake: L195.

#### FC78 · claim · Exactly one of three provenances

Lines it formalizes or quotes (from the brief): L193, L201.

- **Mimo** (reply line 51; does not challenge): The counterexample is to H05, D12.1's reading of L195 alone: the text carries the clause at L201 ("a selected transport has no represented target and no criticism in its history; a constructed one has both") and L411, and with it the history gives Con and not Sel; no text change removes it because the words already carry what removes it; everything turns on the occurrence representing the codomain; residue: L201's "Construction may operate on selected material. Selection may continue to operate beneath construction." must be read of the material and the process, not of one transport's own provenance.
  - Quotations: “a selected transport has no represented target and no criticism in its history; a constructed one has both” — found at L201; “A selected transport has no represented target in its history; a constructed one does.” — found at L411; “exactly one” — found at L193; “Construction may operate on selected material. Selection may continue to operate beneath construction.” — found at L201.
- **GLM** (reply line 39; challenges): The formal core does not use L201; the sentence group it formalizes does (see (b)).
- **GLM** (reply lines 57–67; challenges): Not a counterexample to the text but to D12.1 as written: L201 and L411 state the exclusion, so under the text's words Sel fails and Con holds; the formal core quotes neither (H05) and I53's gloss imports what D12.1 lacks; change to the maths: write "no represented target and no criticism" into Sel and record H05; residual tension L193 against L201 (construction on selected material) needs the per-part rule; proposes a new L193 (names I54); with it, the reader says, FC81 (d), FC82 and FC83 share the history and fall with FC78, one finding.
  - Proposal `G13-B8` (reply lines 63–65), would change L193:

````
A transport \(t\) whose domain is an organization of a physical system has exactly one of three provenances, determined by its history in the physical module and carried by each of its parts separately:
````

  - Quotations: “a selected transport has no represented target and no criticism in its history” — found at L201; “A selected transport has no represented target in its history; a constructed one does” — found at L411; “exactly one of three” — found at L193; “no represented target and no criticism” — found at L201; “A transport \(t\) whose domain is an organization of a physical system has exactly one of three provenances, determined by its history in the physical module:” — found at L193.
- **External reader and case card:** C01 (the case card) challenges the sentence this item formalizes (section 4 below); C11 (the case card) challenges the sentence this item formalizes (section 4 below).
- **Goes to a checker** (rule 5): challenged by GLM; one of the twelve counterexamples the second check reproduced (FC78, FC81 (d) and FC82, one finding); challenged by C01 (the case card), C11 (the case card). Lines at stake: L193, L195, L201.

#### FC79 · claim · Survival is how the transport got there; fidelity is what it is

Lines it formalizes or quotes (from the brief): L41.

- **Mimo** (reply line 77; does not challenge): Hand attack fails: since survival requires fidelity on H, every failure of a survivor lies outside H, and the sentence comes to faithfulness on C; it would be empty only if I48's or I49's settings were fixed by what survived, which the words do not allow; no change.
  - Quotations: “faithful on changes it was never selected against” — found at L41.
- **GLM** (reply line 41; does not challenge): Says what the line says (see (d)).
- **GLM** (reply lines 117–125; challenges): Holds by construction; attack (1): reading a selected transport's contract as its history (C := H) makes "faithful on changes it was never selected against" vacuous, a reading nothing quoted forbids; proposes a new L41 with a guard (writes a new choice in, that contracts are not scoped by selection histories, and says so); attack (2) fails.
  - Proposal `G13-B15` (reply lines 121–123), would change L41:

````
Whether that transport is faithful on changes it was never selected against turns on the transport and the target alone, not on whether it survived; a contract is never fixed by what a transport was selected against.
````

  - Quotations: “faithful on changes it was never selected against” — found at L41; “Whether that transport is faithful on changes it was never selected against turns on the transport and the target alone, not on whether it survived.” — found at L41; “faithful” — found at L41, L43, L67, L69 and 14 more lines.
- **Goes to a checker** (rule 5): challenged by GLM. Lines at stake: L41.

#### FC95 · claim · A system can represent a theory in error

Lines it formalizes or quotes (from the brief): L211.

- **Mimo** (reply line 79; does not challenge): Two attacks fail: individuating a content by its target is ruled out by L211's own words; reading carrier-to-content faithfulness as carrying the target's relations would collapse the two transports L211 keeps apart; the nearest model rests on I90, I92.
  - Quotations: “represent a theory in error” — found at L211; “faithful on \(c\)'s contract” — found at L205, L413.
- **GLM** (reply line 43; does not challenge): Says what the line says, assuming two transports may share domain and codomain and differ (see (d)).
- **GLM** (reply lines 127–133; challenges): The witness rests on two transports sharing domain and codomain; if a transport were fixed by its domain and codomain L211 would be contradictory; nothing quoted settles that transports may so differ (I81's space allows it, the text does not say it); proposes a sentence after L211's first sentence; a second attack fails.
  - Proposal `G13-B16` (reply lines 129–131), would change L211:

````
The transport by which a carrier represents a content and a candidate's transport from the content's target to that content need not be the same transport.
````

  - Quotations: “the transport from carrier to content… while the transport from the content's target to the content fails” — found at L211.
- **Goes to a checker** (rule 5): challenged by GLM. Lines at stake: L211.

#### I48 · invention · Contents, 'c's contract', and transports into a content

Lines it formalizes or quotes (from the brief): L169, L205, L413.

- **Mimo** (reply line 55; challenges): Not fixed: no line says how c's contract reaches the ports of a transport into c; the L205 proposal writes the preimage reading in, naming I48; whether the commitments are exactly the active components stays open.
  - Proposal `M13-B3` (reply lines 21–23; printed in full under D12.5 above), would change L205.
  - Quotations: “\(c\)'s contract” — found at L205, L413.
- **GLM** (reply lines 71–77; challenges): The text settles that a content has a contract, not where it lives for a transport into the content; the preimage reading is the only one that lets L205 bind a transport from a carrier; the text should settle it; proposes sentences after L169 (names I48).
  - Proposal `G13-B9` (reply lines 73–75), would change L169:

````
The contract of a content is on the content's own organization. A transport into a content is faithful on that contract when it meets the conditions of fidelity at each pair of its own domain whose image lies in the contract.
````

  - Quotations: “an organization together with its contract-relative commitments” — found at L169; “faithful on c's contract” — found at L205, L413.
- **Goes to a checker** (rule 5): challenged by GLM and Mimo. Lines at stake: L169, L205.

#### I52 · invention · Selection: the parameters witnessed in a physical history

Lines it formalizes or quotes (from the brief): L195.

- **Mimo** (reply line 57; challenges): The L195 proposal writes in the parts the words lean to; μ's type stays open.
  - Proposal `M13-B1` (reply lines 5–7; printed in full under D12.1 above), would change L195.
  - Quotations: “a variation operator on \(\mathcal T\)” — not found in the text; not in the brief.
- **GLM** (reply line 79; challenges): Partly settled: "member of the history" cannot stand; the physical witness is settled by the module's role (L31, L481); whether μ must move is settled by "A variation is a competitor" (S20); the wording under FC77 writes all three in; "H required to be nonempty" should stay rejected.
  - Proposal `G13-B6` (reply lines 51–53; printed in full under FC77 above), would change L195.
  - Quotations: “member of the history” — found at L195; “A variation is a competitor” — not found in the text; found in the brief; “H required to be nonempty” — not found in the text; found in the brief.
- **External reader and case card:** C04 (the case card) challenges the sentence this item formalizes (section 4 below).
- **Goes to a checker** (rule 5): challenged by GLM and Mimo; challenged by C04 (the case card). Lines at stake: L195.

#### I53 · invention · 'Exactly one of three provenances': one whole history

Lines it formalizes or quotes (from the brief): L193, L201.

- **Mimo** (reply line 59; challenges): The words fix it: L193's "determined by its history in the physical module" and L201's "in its history" are one history of t, and L201's two clauses give the exclusion; the maths needs H05's clause beyond that.
  - Quotations: “determined by its history in the physical module” — found at L193; “in its history” — found at L155, L201, L411.
- **GLM** (reply line 81; challenges): The text settles it (L201, L411); what it does not say is that the exclusion is per part, which L201's "beneath" needs; the L409 wording supplies it.
  - Proposal `G13-B4` (reply lines 21–23; printed in full under D12.4 above), would change L409.
  - Quotations: “beneath” — found at L201.
- **External reader and case card:** C01 (the case card) challenges the sentence this item formalizes (section 4 below).
- **Goes to a checker** (rule 5): challenged by GLM and Mimo; challenged by C01 (the case card). Lines at stake: L409.

#### I54 · invention · Inherited provenance: a rule of carrying over, per part

Lines it formalizes or quotes (from the brief): L211, L405, L409.

- **Mimo** (reply line 61; challenges): The rule is carried by L211 and L409, the unit is not; the L405 proposal writes both in, naming I54 (the brief prints two different sentences under L405, not the same claim).
  - Proposal `M13-B2` (reply lines 15–17; printed in full under D12.4 above), would change L405.
- **GLM** (reply line 83; challenges): Not settled: "inherited" is used twice and defined nowhere; settled by the L409 wording.
  - Proposal `G13-B4` (reply lines 21–23; printed in full under D12.4 above), would change L409.
  - Quotations: “inherited” — found at L405, L409.
- **Goes to a checker** (rule 5): challenged by GLM and Mimo. Lines at stake: L405, L409.

#### I56 · invention · Build: 'prepares', 'nontrivial binding construction', 'content-preserving transfer'

Lines it formalizes or quotes (from the brief): L405.

- **Mimo** (reply line 63; does not challenge): "Prepares", "nontrivial binding construction", "content-preserving transfer" carry Build and Con and are undefined; they should stay open as notions the physical module carries (S25, S26); no proposal.
  - Quotations: “nontrivial binding construction” — found at L405, L628; “content-preserving transfer” — found at L405.
- **GLM** (reply lines 85–91; challenges): Not settled: "prepares", "nontrivial binding construction", "content-preserving transfer" are facts about actual subhistories, so reading them through the physical module is where S25–S27 put physical possibility; the text should say so; proposes a sentence after L405 (names I56).
  - Proposal `G13-B10` (reply lines 87–89), would change L405:

````
Whether a subhistory prepares an organization for a use, whether a binding construction is nontrivial, and whether a composition is of content-preserving transfers, are read through the physical module.
````

  - Quotations: “prepares” — found at L197, L405; “nontrivial binding construction” — found at L405, L628; “content-preserving transfer” — found at L405.
- **External reader and case card:** E03 (the external reader) challenges the sentence this item formalizes (section 3 below); C06 (the case card) challenges the sentence this item formalizes (section 4 below).
- **Goes to a checker** (rule 5): challenged by GLM; challenged by E03 (the external reader), C06 (the case card). Lines at stake: L405.

#### I71 · invention · The 'value' of a transport at a pair (Argument 3)

Lines it formalizes or quotes (from the brief): L572.

- **Mimo** (reply line 65; does not challenge **PARKED**): Stays open, beside the parked question; no proposal.
- **GLM** (reply lines 93–99; challenges): Not settled: L572 turns on what a value is, and I71's choice is the only one under which members of one population can differ; the text should carry it; proposes a sentence before L572 (names I71).
  - Proposal `G13-B11` (reply lines 95–97; printed in full under D12.9 above), would change L572.
  - Quotations: “some t′ ∈ 𝒯 … has a different value” — found at L572.
- **Goes to a checker** (rule 5): challenged by GLM. Lines at stake: L572.
- Marks: PARKED points present. 

#### I90 · invention · The physical module supplied by hand: histories and provenance as free predicates

Lines it formalizes or quotes (from the brief): L31, L195, L197, L405.

- **Mimo** (reply line 67; does not challenge): A choice about the program; the words say what Θ does and no more; nothing needs to change; with the L195 proposal the representing Sel forbids is the physical module's.
  - Quotations: “which says what organization a physical occurrence instantiates at a grain” — found at L31.
- **GLM** (reply line 101; does not challenge): Not settled, rightly: a device of the search; its caveat should stay with every result using it; its alternative (a), a toy physics, belongs to FC98's part; no text change.
- **Goes to no checker**: no point challenges it and it is not one of the twelve; recorded under rule 7 below.

#### H05 · H-entry · Selection limited by L195 alone; L201 and L411 left out (D12.1)

Lines it formalizes or quotes (from the brief): L193, L195, L197, L201, L411.

- **Mimo** (reply line 69; challenges): The words carry the clause twice (L201, L411); the formal core must take it in; no text change.
- **GLM** (reply line 103; challenges): The text settles the choice (L201, L411); the register should carry it with its rejected alternative and D12.1 be rewritten; FC78, FC81 (d), FC82 and FC83 then change as the check computed; no text change beyond (a)'s.
- **External reader and case card:** C02 (the case card) challenges the sentence this item formalizes (section 4 below).
- **Goes to a checker** (rule 5): challenged by GLM and Mimo; challenged by C02 (the case card). Lines at stake: L193, L195, L197, L201, L411.

#### H09 · H-entry · The population: D12.1's "the members of 𝒯 are admitted by the physics" against L481's "The population is the set" (D12.1, D15.8, model)

Lines it formalizes or quotes (from the brief): L481.

- **Mimo** (reply line 71; challenges): The words fix the population as the whole admitted set (L481); the maths' inclusion departs from it, and its witnesses use a population of one; "parts(t)" is fixed nowhere and stays open.
  - Quotations: “parts(t)” — not found in the text; found in the brief.
- **GLM** (reply line 105; challenges): The text settles the population: L481 is an equality, D12.1's inclusion should become it; "parts(t)" should be defined through I54's parts; no text change.
  - Quotations: “The population is the set of transports the physics and the stated construction admit” — found at L481; “the members of 𝒯 are admitted by the physics” — not found in the text; found in the brief; “parts(t)” — not found in the text; found in the brief.
- **Goes to a checker** (rule 5): challenged by GLM and Mimo. Lines at stake: L481.

#### H13 · H-entry · "actually occurring" as a primitive with no entry (D11.5)

Lines it formalizes or quotes (from the brief): L217.

- **Mimo** (reply line 73; challenges): Carried by the L195 proposal ("actually encountered in the physical module").
  - Proposal `M13-B1` (reply lines 5–7; printed in full under D12.1 above), would change L195.
  - Quotations: “actually encountered in the physical module” — not found in the text; not in the brief.
- **GLM** (reply lines 107–113; challenges): Occurrence is the physical module's business (L31); the primitive needs an invention entry, and one phrase closes it; proposes a new L217.
  - Proposal `G13-B13` (reply lines 111–113), would change L217:

````
For an edit–boundary pair \((a,b)\in C\) actually occurring in the physical module:
````

  - Quotations: “For an edit–boundary pair \((a,b)\in C\) actually occurring:” — found at L217.
- **Goes to a checker** (rule 5): challenged by GLM and Mimo. Lines at stake: L195, L217.

#### Part 13: items no point addresses

Items of this part on which neither reader made any point (both replies read whole): I18, I81, I92. Each is recorded under rule 7 in section 6 unless a point on it in another part sends it to a checker.

### Part 14: Prediction, violation, surprise and the two responses

Brief: `tests/S104 Round 2 - the maths against the words - part 14, Prediction, violation, surprise and the two responses.md`. Replies: `s104_maths_mimo_14.response.txt` (Mimo), `s104_maths_glm_14.response.txt` (GLM).

#### D12.1 · definition · Selected

Lines it formalizes or quotes (from the brief): L193, L195.

- **Mimo** (reply line 15; does not challenge): Named among the items with nothing to add.
- **GLM** (reply line 18; challenges): Faithful to L195 as written, and that list is the source of this part's troubles (see FC81).
  - Proposal `G14-B2` (reply lines 37), would change L195:

````
> L195 | A transport **survives on \(H\)** when it is a member of \(\mathcal T\) that meets the survival condition on \(H\); fidelity on \(H\) without membership in \(\mathcal T\) is not survival. No member of the history represents \(t\), \(H\), the survival condition, or an organization \(t\) carries to.
````

- **External reader and case card:** C02 (the case card) challenges the sentence this item formalizes (section 4 below); C03 (the case card) challenges the sentence this item formalizes (section 4 below); C04 (the case card) challenges the sentence this item formalizes (section 4 below).
- **Goes to a checker** (rule 5): challenged by GLM; challenged by C02 (the case card), C03 (the case card), C04 (the case card). Lines at stake: L195.

#### D12.2 · definition · Constructed

Lines it formalizes or quotes (from the brief): L197.

- **Mimo** (reply line 15; does not challenge): Named among the items with nothing to add.
- **GLM** (reply line 20; does not challenge): Faithful; its availability clause is what lets Sel and Con co-hold.
  - Quotations: “available as a represented target” — found at L197.
- **External reader and case card:** E03 (the external reader) challenges the sentence this item formalizes (section 3 below); C07 (the case card) challenges the sentence this item formalizes (section 4 below).
- **Goes to a checker** (rule 5): challenged by E03 (the external reader), C07 (the case card). Lines at stake: L197.

#### D12.6 · definition · Layers

Lines it formalizes or quotes (from the brief): L175, L177.

- **Mimo** (reply line 15; does not challenge): Named among the items with nothing to add.
- **GLM** (reply line 32; does not challenge): Named among the items with nothing to add.
- **Goes to no checker**: no point challenges it and it is not one of the twelve; recorded under rule 7 below.

#### D12.7 · definition · Prediction, violation, surprise

Lines it formalizes or quotes (from the brief): L219, L220, L221.

- **Mimo** (reply line 3; challenges): Scope of "fidelity fails": the narrow Viol drops (F2)'s homomorphism clause, which I50 lists as an alternative, so if fidelity includes it the narrow reading silently narrows a defined term; Viol⁺ imports (A), which L220 does not name; the words should stand (a violation is the failure of the defined fidelity at the pair, homomorphism clause included, (A) not part of it); S27 is cited against a reading needing a wrong answer against the world; no change of wording; the maths must record which condition it carries.
  - Quotations: “fidelity fails” — found at L220; “fidelity” — found at L17, L23, L37, L41 and 14 more lines; “at the level of explanation without ever having to be tested against reality” — not found in the text; found in the brief.
- **Mimo** (reply line 5; challenges): Binding of the selection parameters: the formula's "for some 𝒯, μ, H" against L217's "where t is selected, history H" and L193's "determined by its history": H is t's own history; the existential reading is a different sentence; "(a,b) ∉ H" does no work but states content.
  - Quotations: “Let \(t\) be a transport to the simulation layer \(S\), with contract \(C\) and, where \(t\) is selected, history \(H\).” — found at L217; “… exactly one of three provenances, determined by its history in the physical module” — found at L193; “(a,b) ∉ H” — found at L221, L574, L582.
- **GLM** (reply lines 5–10; challenges): Violation: fidelity is the text's defined whole, and the narrow Viol (I50) drops clauses; the words should stand and the maths take its other choice (b); FC81 (d) and FC20 rest on I50; if clarity is wanted, a new L220; surprise: Occurs is faithful, but "for some 𝒯, μ, H" departs from L217's and L193's one history (H07); the words stand; the maths should bind H.
  - Proposal `G14-B1` (reply lines 8), would change L220:

````
> L220 | - a **violation** occurs when fidelity fails at \((a,b)\), in any of its clauses;
````

  - Quotations: “a violation occurs when fidelity fails at (a,b)” — found at L220; “occurs when fidelity fails” — found at L220; “Sel(t; 𝒯, μ, H) **for some** 𝒯, μ, H” — not found in the text; found in the brief; “a transport … with contract C and, where t is selected, history H” — found at L217; “determined by its history” — found at L41, L193, L542.
- **Goes to a checker** (rule 5): challenged by GLM and Mimo. Lines at stake: L220.

#### D12.8 · definition · Responses

Lines it formalizes or quotes (from the brief): L225.

- **Mimo** (reply lines 7–11; challenges): Three partings: (i) the formula extends H by exactly the failing pair while the words say only "extends the history H", and the words should change (writing H08's choice in, and saying so); (ii) μ* lets t′ = t, which the words do not fix (leave open); (iii) the formula has no place for a response introducing an organization with no transport (the words stand); proposes a new L225 (its third sentence predicates originativity of the content a response introduces).
  - Proposal `M14-B1` (reply lines 9–11), would change L225:

````
> L225 | A **selection response** to a failure at \((a,b)\) extends the history \(H\) of a selected transport by \((a,b)\) and lets \(\mu\) act: the transport is re-tuned within the population. A **construction response** introduces a new organization or a new transport with a construction trace. Only the second response introduces content that is originative under Part X.
````

  - Quotations: “extends the history H” — found at L225; “the transport is re-tuned” — found at L225; “response” — found at L37, L225, L269, L315 and 6 more lines.
- **GLM** (reply lines 12–16; challenges): Three departures, the definitions writing less than the sentence: no trigger (the responses carry no violation condition; H08); a dangling modifier ("a new organization or a new transport with a construction trace"), the maths being the better reading of the intent, the words to be repaired; "new" relative to what is not settled (wordings under FC82).
  - Proposal `G14-B3` (reply lines 42), would change L225:

````
> L225 | A **selection response** to a violation extends the history \(H\) of a selected transport and lets \(\mu\) act: the transport is re-tuned within the population, which already holds every transport \(\mu\) can return. A **construction response** to a violation introduces, with a construction trace, a new organization or a new transport — new relative to any population \(\mathcal T\) on which selection is running and to anything the system already holds. Only the second can be originative under Part X.
````

  - Quotations: “the two responses” — found at L584; “(a new organization) or (a new transport with a construction trace)” — found at L225; “introduces a new organization or a new transport” — found at L225.
- **External reader and case card:** C05 (the case card) challenges the sentence this item formalizes (section 4 below).
- **Goes to a checker** (rule 5): challenged by GLM and Mimo; challenged by C05 (the case card). Lines at stake: L225.

#### D13.3 · definition · Build; construction trace

Lines it formalizes or quotes (from the brief): L405.

- **Mimo** (reply line 15; does not challenge): Named among the items with nothing to add.
- **GLM** (reply line 22; challenges): Faithful given I56; the reader says L409's "a binding may be identified by its use" is not formalized even as a primitive; left open with I56.
  - Quotations: “a binding may be identified by its use” — not found in the text; found in the brief.
- **External reader and case card:** E03 (the external reader) challenges the sentence this item formalizes (section 3 below); C06 (the case card) challenges the sentence this item formalizes (section 4 below).
- **Goes to a checker** (rule 5): challenged by GLM; challenged by E03 (the external reader), C06 (the case card). Lines at stake: L405.

#### FC80 · claim · Argument 3: underdetermination where the population leaves room

Lines it formalizes or quotes (from the brief): L572, L574.

- **Mimo** (reply line 50; challenges): Three hand attacks: (i) reading "the value at (a,b)" as the target's value makes it a function of (𝒯, H, D), not (𝒯, H); (ii) under I02's alternative (an action law) nothing is underdetermined at a pair tied to H, so the claim survives only if the pair's orbit under the law avoids H; (iii) beyond the bounds, composite edits without a law give the witness's shape at a composite pair outside H.
  - Quotations: “the value at (a,b)” — found at L574; “altered at one pair gives another admitted relation” — not found in the text; found in the brief.
- **GLM** (reply line 24; does not challenge): Says what the argument says; (b) as "a function of (𝒯, H)" is the right reading; nothing settled for the world (S28).
  - Quotations: “the population fixes it” — found at L574; “that value is a function of (𝒯, H)” — not found in the text; found in the brief.
- **GLM** (reply line 68; does not challenge): Hand model for the untested part (c): with an action law binding a composite, two lawful survivors agreeing on H differ at a pair of C ∖ H, so Argument 3's conclusion does not need I02 though its route does; (b) in context the population fixes the value; could not break the sentence.
- **Goes to a checker** (rule 5): challenged by Mimo. Lines at stake: L572, L574.

#### FC81 · claim · Argument 4, and who can be surprised

Lines it formalizes or quotes (from the brief): L223, L580.

- **Mimo** (reply lines 19–24; challenges): The model gives one transport both provenances; L193 forbids that outright, so it is not a model of the text and tells against I52 and I53 (whose mechanism the clauses do not deliver); but L195 and L197 permit the model while L193 forbids it: the text asserts exclusivity its clauses do not carry; proposes a new sentence at L195 adding "or the organization t carries to" (writes I53's mechanism and I52's occurrence reading in); L223 then stands unchanged.
  - Proposal `M14-B2` (reply lines 21–23), would change L195:

````
> L195 | No occurrence of the history represents \(t\), \(H\), the survival condition, or the organization \(t\) carries to.
````

  - Quotations: “… exactly one of three provenances, determined by its history in the physical module” — found at L193; “Con puts a represented target in that history; Sel has none” — not found in the text; found in the brief; “member of the history” — found at L195; “No member of the history represents \(t\), \(H\), or the survival condition.” — found at L195; “a constructed one that fails at an actually occurring pair of its contract is violated, and the failure is not surprise” — found at L223.
- **Mimo** (reply line 52; challenges): (a) and (c) hold by construction only because Surp's formula puts (a,b) in C ∖ H; under H07's "for some" binding, a second population with H′ ⊊ C gives surprise while t's own history exhausts C; broken by the binding, not by the words.
  - Quotations: “holds by construction” — not found in the text; found in the brief; “for some” — found at L8, L205, L305, L329 and 1 more lines; “A system can be surprised only if it holds a transport selected on a history \(H\) strictly smaller than its contract \(C\)” — found at L580.
- **GLM** (reply line 26; challenges): (d) relies on Surp ⇒ Sel (L221's) and on Sel excluding Con (L193's "exactly one of three provenances"), which L195 fails to deliver; the statement says what the sentence says only if the two lines agree, and they do not.
  - Proposal `G14-B2` (reply lines 37; printed in full under D12.1 above), would change L195.
  - Quotations: “a constructed one … is violated, and the failure is not surprise” — found at L223; “exactly one of three provenances” — found at L193.
- **GLM** (reply lines 36–39; challenges): FC81 (d) tells against the text through one gap: L195's non-representation clause omits the organization t carries to, which L197's Con needs, so the text's own clauses let a transport be both selected and constructed, and L223's "the failure is not surprise" then fails; proposes a new L195 passage; the reader flags the cost (a transport selected by trial and error whose target is itself held in a carrier, S26's first example, would not be selected), which is FC78's question.
  - Proposal `G14-B2` (reply lines 37; printed in full under D12.1 above), would change L195.
  - Quotations: “exactly one of three provenances, determined by its history” — found at L193; “t, H, or the survival condition” — found at L195; “the failure is not surprise” — found at L223.
- **GLM** (reply line 70; does not challenge): Attack on (a)–(c) via H ⊄ C dies on L195's "a finite history H ⊆ C": the text settles H ⊆ C; could not break them.
  - Quotations: “H strictly smaller than C” — not found in the text; not in the brief; “a finite history \(H\subseteq C\)” — found at L195.
- **Goes to a checker** (rule 5): challenged by GLM and Mimo; one of the twelve counterexamples the second check reproduced (FC78, FC81 (d) and FC82, one finding). Lines at stake: L193, L195, L201.

#### FC82 · claim · The two responses to a violation have no common result

Lines it formalizes or quotes (from the brief): L225.

- **Mimo** (reply line 26; does not challenge): Weakened twice: it rests on FC78's one-history model, and per H08 no response was computed (t′ = t, no μ step, no failure); it tells against the inventions and the model's reading of "response", not the text; with the exclusivity wording and a model of an actual response the claim stands.
  - Quotations: “response” — found at L37, L225, L269, L315 and 6 more lines.
- **GLM** (reply line 28; challenges): The formal statement matches the sentence; it follows only under an exclusion L195 does not give.
  - Proposal `G14-B2` (reply lines 37; printed in full under D12.1 above), would change L195.
  - Quotations: “no transport is the result of both” — not found in the text; found in the brief; “follow from the definitions as written” — not found in the text; not in the brief.
- **GLM** (reply lines 41–44; challenges): As first computed, a counterexample only to the model (t′ = t, no violation, H08); the second check's stronger case stands against the text only through the L193/L195 gap and "new relative to what"; proposes a new L225 closing the second (writes two choices in: new relative to any running population, and the population's prior hold on μ's results); under it no transport is the result of both responses.
  - Proposal `G14-B3` (reply lines 42; printed in full under D12.8 above), would change L225.
  - Quotations: “new relative to what” — not found in the text; not in the brief; “new relative to any population on which selection is running” — not found in the text; not in the brief.
- **External reader and case card:** C05 (the case card) challenges the sentence this item formalizes (section 4 below).
- **Goes to a checker** (rule 5): challenged by GLM; one of the twelve counterexamples the second check reproduced (FC78, FC81 (d) and FC82, one finding); challenged by C05 (the case card). Lines at stake: L193, L195, L201, L225.

#### FC83 · claim · Only the construction response can be originative

Lines it formalizes or quotes (from the brief): L225.

- **Mimo** (reply line 13; challenges): The sentence predicates originativity of the response, the formal statement predicates Origin of the content t′ carries to: different sentences; the words in their intent stand, the formula does not; the third sentence of the L225 proposal fixes the mismatch.
  - Proposal `M14-B1` (reply lines 9–11; printed in full under D12.8 above), would change L225.
  - Quotations: “Only the second can be originative” — found at L225.
- **Mimo** (reply line 28; challenges): The counterexample survives exclusivity (nothing ties Build's subhistory to the selection history), but it attacks the formal statement, not the sentence as intended (the content was prepared earlier, so the selection response introduces nothing); still the text asserts the claim without its definitions delivering it; the change is the third sentence of the L225 proposal; the model stipulates Attempt, New and Build's primitives by hand (I56, I90).
  - Proposal `M14-B1` (reply lines 9–11; printed in full under D12.8 above), would change L225.
- **GLM** (reply line 30; challenges): The formal statement is stronger than the sentence: the sentence says only the second response can be originative (re-tuning is never itself the originative doing); a history with a selection response and a separate originative construction episode does not refute it; the words stand; the claim should be restated ("no originative episode is part of a selection response's own working of μ").
  - Quotations: “no originative episode is part of a selection response's own working of μ” — not found in the text; not in the brief.
- **GLM** (reply line 46; challenges **OWNER QUESTION**): A counterexample only to the claim's formal statement and I90's hand-set conjuncts; nothing in the sentence is refuted; restate the claim, and, if the text is to make the sentence follow, adopt the L225 wording; the reader notes the owner's own words cut both ways (S20's "a variation is a competitor … two discovered variations" allows a population to hold variants whose content is discovered new), and the wording chooses the other side.
  - Proposal `G14-B3` (reply lines 42; printed in full under D12.8 above), would change L225.
  - Quotations: “a variation is a competitor … two discovered variations” — not found in the text; found in the brief.
- **Goes to a checker** (rule 5): challenged by GLM and Mimo; one of the twelve counterexamples the second check reproduced (FC83). Lines at stake: L225.
- Marks: OWNER QUESTION points present.

#### I50 · invention · A violation at a pair: which conditions fail

Lines it formalizes or quotes (from the brief): L220.

- **Mimo** (reply line 32; challenges **OWNER QUESTION**): Settled through the defined term: L220 names fidelity, whose scope is fixed by its definition, so (A) is out and the homomorphism clause in if fidelity has it; nothing to propose; "if the owner wants a failed prediction to count as violation, the words must say so".
  - Quotations: “- a **violation** occurs when fidelity fails at \((a,b)\);” — found at L220.
- **GLM** (reply line 50; challenges): The text settles it: "when fidelity fails" means the defined whole fails; the narrow reading is the wrong choice; the maths should take option (b), and FC20 and FC81 (d) be re-run.
  - Quotations: “when fidelity fails” — found at L220.
- **Goes to a checker** (rule 5): challenged by GLM and Mimo. Lines at stake: L220.
- Marks: OWNER QUESTION points present.

#### I52 · invention · Selection: the parameters witnessed in a physical history

Lines it formalizes or quotes (from the brief): L195.

- **Mimo** (reply line 34; challenges): Partly settled (population, variation operator, pairs "actually encountered", survival condition, non-representation); not settled: μ's type (left open) and the category slip in "member of the history" (fixed by the L195 proposal).
  - Proposal `M14-B2` (reply lines 21–23; printed in full under FC81 above), would change L195.
  - Quotations: “No member of the history represents \(t\), \(H\), or the survival condition.” — found at L195; “actually encountered” — found at L195; “requiring fidelity on \(H\)” — found at L195; “a variation operator \(\mu\) on \(\mathcal T\)” — found at L195; “member of the history” — found at L195.
- **GLM** (reply line 52; challenges **PARKED**): Not settled, and rightly open: "a survival condition requiring fidelity on H" states a lower bound, and the reader cites S20 ("Good explanations make bad ones harder to fit") as making the strength of survival conditions a live question; the occurrence reading of "member of the history" is forced (H's members are pairs) and harmless.
  - Quotations: “a survival condition requiring fidelity on H” — found at L195; “Good explanations make bad ones harder to fit” — not found in the text; found in the brief; “member of the history” — found at L195.
- **External reader and case card:** C04 (the case card) challenges the sentence this item formalizes (section 4 below).
- **Goes to a checker** (rule 5): challenged by GLM and Mimo; challenged by C04 (the case card). Lines at stake: L195.
- Marks: PARKED points present. 

#### I53 · invention · 'Exactly one of three provenances': one whole history

Lines it formalizes or quotes (from the brief): L193, L201.

- **Mimo** (reply line 36; challenges): Settled in content: L193 fixes one history and exclusivity; the invented mechanism fails as written; the L195 proposal carries the text's own words into the clauses.
  - Proposal `M14-B2` (reply lines 21–23; printed in full under FC81 above), would change L195.
  - Quotations: “… has exactly one of three provenances, determined by its history in the physical module” — found at L193.
- **GLM** (reply line 54; challenges): The text settles the one-history reading ("determined by its history", singular); the corollary that Con excludes Sel is a hope until L195 is amended (under FC81).
  - Proposal `G14-B2` (reply lines 37; printed in full under D12.1 above), would change L195.
  - Quotations: “determined by its history” — found at L41, L193, L542.
- **External reader and case card:** C01 (the case card) challenges the sentence this item formalizes (section 4 below).
- **Goes to a checker** (rule 5): challenged by GLM and Mimo; challenged by C01 (the case card). Lines at stake: L195.

#### I56 · invention · Build: 'prepares', 'nontrivial binding construction', 'content-preserving transfer'

Lines it formalizes or quotes (from the brief): L405.

- **Mimo** (reply line 38; challenges): Not settled (L405 names the three conditions but not how they are recognized); stay open, read through the physical module; what this part needs is that Build concerns the episode preparing content, not the response delivering it, which the L225 proposal carries.
  - Proposal `M14-B1` (reply lines 9–11; printed in full under D12.8 above), would change L225.
  - Quotations: “… contains a nontrivial binding construction relevant to that use, and is not a composition of content-preserving transfers.” — found at L405.
- **GLM** (reply line 56; does not challenge): Not settled; should stay open this round; FC83's weight depends on them being set by hand.
  - Quotations: “prepares” — found at L197, L405; “nontrivial binding construction” — found at L405, L628; “content-preserving transfer” — found at L405.
- **External reader and case card:** E03 (the external reader) challenges the sentence this item formalizes (section 3 below); C06 (the case card) challenges the sentence this item formalizes (section 4 below).
- **Goes to a checker** (rule 5): challenged by Mimo; challenged by E03 (the external reader), C06 (the case card). Lines at stake: L225.

#### I90 · invention · The physical module supplied by hand: histories and provenance as free predicates

Lines it formalizes or quotes (from the brief): L31, L195, L197, L405.

- **Mimo** (reply line 40; does not challenge): Not settled and should stay open; the flag stands.
  - Quotations: “… determined by its history in the physical module” — found at L193.
- **GLM** (reply line 58; does not challenge): Not a text matter; its caveat should travel with every counterexample.
- **Goes to no checker**: no point challenges it and it is not one of the twelve; recorded under rule 7 below.

#### I92 · invention · The pole in exact arithmetic, with its grids, baseline, contracts and fibre query

Lines it formalizes or quotes (from the brief): L325.

- **Mimo** (reply line 42; does not challenge): Nothing to add.
- **GLM** (reply line 64; does not challenge): Nothing to add (by title only).
- **Goes to no checker**: no point challenges it and it is not one of the twelve; recorded under rule 7 below.

#### H07 · H-entry · Surprise with the selection parameters bound by "for some" (D12.7)

Lines it formalizes or quotes (from the brief): L217, L221.

- **Mimo** (reply line 44; challenges): Settled against the invention: L217 gives t one history H and L193 makes it determined by history; the "for some" binding contradicts both; no change of wording; the maths must bind H to t's selection history; the redundant "(a,b) ∉ H" is harmless.
  - Quotations: “for some” — found at L8, L205, L305, L329 and 1 more lines; “(a,b) ∉ H” — found at L221, L574, L582.
- **GLM** (reply line 60; challenges): The text settles the fixed H; "for some" should go; the noted redundancy is an artifact of reading Faithful_H as a standing condition: L195's pairs are "actually encountered", so a present failure at a pair of the same kind as one in H is a violation and not surprise (the reader cites S20's "Once the explanation is rescued, the mistake shouldn't be able to creep back in"); no text change; the maths should adopt the historical reading.
  - Quotations: “for some” — found at L8, L205, L305, L329 and 1 more lines; “(a,b) ∉ H does no work” — not found in the text; found in the brief; “actually encountered” — found at L195; “Once the explanation is rescued, the mistake shouldn't be able to creep back in” — not found in the text; found in the brief.
- **Goes to a checker** (rule 5): challenged by GLM and Mimo. Lines at stake: L217, L221.

#### H08 · H-entry · The two responses (D12.8), and the model's responses

Lines it formalizes or quotes (from the brief): L225.

- **Mimo** (reply line 46; challenges): Two unrecorded choices: whether μ must change t is left open, but the model's sel(c, H + [x], h) with t′ = t and no failure is not a response at all and must not stand as one; "new" is left open (picking a repertoire writes an invention in).
  - Quotations: “lets \(\mu\) act: the transport is re-tuned” — found at L225.
- **GLM** (reply line 62; challenges): The trigger is settled by the text (L225's responses answer L220–L223's violation); D12.8 must add it; zero μ-steps: "re-tuned" leans to t′ ≠ t without settling it; the L225 wording leaves it to μ (a choice written in, named).
  - Proposal `G14-B3` (reply lines 42; printed in full under D12.8 above), would change L225.
  - Quotations: “re-tuned” — found at L225; “which already holds every transport μ can return” — not found in the text; not in the brief.
- **External reader and case card:** C05 (the case card) challenges the sentence this item formalizes (section 4 below).
- **Goes to a checker** (rule 5): challenged by GLM and Mimo; challenged by C05 (the case card). Lines at stake: L225.

#### matter 3 · round-1 matter · "signature" in the everyday sense at L584 ("the signature of a selected transport meeting a change outside its history"), beside the defined term.

Lines it formalizes or quotes (from the brief): L584.

- **Mimo** (reply lines 56–61; challenges): "Signature" in the everyday sense beside a defined term is a clash; proposes "the mark of" in place of "the signature of" in the fragment of L584 (only the fragment is given; the rest of the line stands).
  - Proposal `M14-B3` (reply lines 58–60), would change L584:

````
> L584 | … the mark of a selected transport meeting a change outside its history …
````

  - Quotations: “signature” — found at L37, L57, L109, L111 and 14 more lines.
- **GLM** (reply lines 74–77; challenges): A defined term used in the everyday sense invites equivocation; proposes "the mark of" within the fragment of L584 (only the fragment is given).
  - Proposal `G14-B4` (reply lines 75), would change L584:

````
> L584 | … the mark of a selected transport meeting a change outside its history …
````

- **Goes to a checker** (rule 5): challenged by GLM and Mimo. Lines at stake: L584.

#### Part 14: items no point addresses

Items of this part on which neither reader made any point (both replies read whole): none. Each is recorded under rule 7 in section 6 unless a point on it in another part sends it to a checker.

### Part 15: Construction, newness, origin, repair and created explanation

Brief: `tests/S104 Round 2 - the maths against the words - part 15, Construction, newness, origin, repair and created explanation.md`. Replies: `s104_maths_mimo_15.response.txt` (Mimo), `s104_maths_glm_15.response.txt` (GLM).

#### D13.1 · definition · Deploy

Lines it formalizes or quotes (from the brief): L403.

- **Mimo** (reply line 3; challenges): Three ways apart: (1) L403 asks the representation to be "by (R) a faithful transport with selected or constructed provenance", D13.1 only Rep_ℓ(o,c), so D13.1 must add the provenance; (2) "serving the declared use task U as a retained capability" becomes Can with a realization using o, and "retained" is not carried; (3) "integrated into problem-directed activity" and "nontrivial use respect" are primitives (I55); the words stand where they speak (wording under I55).
  - Proposal `M15-B5` (reply lines 47–49), would change L403:

````
L403 (replaces) | \(\operatorname{Deploy}_{\beta,\ell}(s,c,\xi;U)\) is met when \(s\) at \(\xi\) holds a representation of \(c\), by (R) a faithful transport with selected or constructed provenance, integrated into problem-directed activity and serving the declared use task \(U\) as a retained capability (Part XII), where "integrated", "retained" and "nontrivial" are declared inputs of that module. The repertoire \(R_{\beta,\ell}(s,\xi)\) is the set of contents deployable in some nontrivial use task \(U\).
````

  - Quotations: “by (R) a faithful transport with selected or constructed provenance” — found at L403; “serving the declared use task U as a retained capability” — found at L403; “retained” — found at L403, L461, L463, L475; “integrated into problem-directed activity” — found at L403; “nontrivial use respect” — found at L403; “use respect” — found at L403.
- **GLM** (reply line 5; challenges): Two divergences: L403's provenance is carried only inside Rep_ℓ(o,c), defined in a part the reader lacks; and substantively, "serving the declared use task U as a retained capability" becomes a capability at ξ with nothing retained, so a content flash-present at ξ sits in the repertoire and blocks New forever after; the words should stand (retention makes R_<e a past-possession test); the text should say what retained comes to (wording under I55), and the maths should carry an occasion after ξ on which the capability is met again.
  - Proposal `G15-B2` (reply lines 59), would change L403:

````
> L403 | … integrated into problem-directed activity — the occurrence lies on an active route (Part IX) to the result of a problem s is engaged with — and serving the declared use task U as a retained capability: on an occasion after ξ that asks for U, the capability is met again (Part XII). The repertoire R_{β,ℓ}(s,ξ) is the set of contents deployable in some nontrivial use respect: a respect whose removal changes whether the task is met.
````

  - Quotations: “(R) a faithful transport with selected or constructed provenance” — found at L403; “serving the declared use task U **as a retained capability**” — found at L403.
- **Goes to a checker** (rule 5): challenged by GLM and Mimo. Lines at stake: L403.

#### D13.2 · definition · Repertoire

Lines it formalizes or quotes (from the brief): L403.

- **Mimo** (reply line 37; does not challenge): Named among the items with nothing to add.
  - Quotations: “Closing an episode is a choice” — found at L429.
- **GLM** (reply line 41; does not challenge): Named among the items with nothing to add.
- **Goes to no checker**: no point challenges it and it is not one of the twelve; recorded under rule 7 below.

#### D13.3 · definition · Build; construction trace

Lines it formalizes or quotes (from the brief): L405.

- **Mimo** (reply line 5; challenges): D13.3 drops "a represented organization" and "for explanatory use" (without the latter a subhistory building a bridge would supply an explanation's construction trace); the words stand; D13.3 should read Prepares as preparing a represented organization for explanatory use of c; no text change.
  - Quotations: “a represented organization” — found at L405; “for explanatory use” — found at L405; “nontrivial” — found at L403, L405, L628; “relevant to that use” — found at L405.
- **GLM** (reply line 7; does not challenge): Faithful; the open terms are registered as I56.
  - Quotations: “prepares” — found at L197, L405; “nontrivial binding construction” — found at L405, L628; “content-preserving transfers” — found at L405.
- **External reader and case card:** E03 (the external reader) challenges the sentence this item formalizes (section 3 below); C06 (the case card) challenges the sentence this item formalizes (section 4 below).
- **Goes to a checker** (rule 5): challenged by Mimo; challenged by E03 (the external reader), C06 (the case card). Lines at stake: L405.

#### D13.4 · definition · Matching

Lines it formalizes or quotes (from the brief): L413.

- **Mimo** (reply lines 7–11; challenges): "Both faithful on c's contract" cannot be read the same way twice (preimage for the transport into c, domain for the one from c); the maths' reading lets c ≡ c hold; the ≡ sign promises a symmetry the definition does not deliver (FC85 (b)), and (N) reads it with c fixed; the words should say so, and fix c's contract at e; proposes a new L413.
  - Proposal `M15-B1` (reply lines 9–11), would change L413:

````
L413 (replaces) | Write \(d\equiv_\ell c\) when there are transports from \(d\) to \(c\) and from \(c\) to \(d\), both faithful on \(c\)'s contract at grain \(\ell\): the first on the preimage of \(c\)'s contract, the second on \(c\)'s contract itself. The relation is read with \(c\) fixed, on the contract \(c\) has at \(e\), and is not symmetric.
````

  - Quotations: “both faithful on c's contract” — found at L413.
- **GLM** (reply line 9; does not challenge): The one-way reading is the text's own ("both faithful on c's contract"); FC85 (b)'s asymmetry is content, not artefact; matches.
  - Quotations: “both faithful on **c's** contract” — found at L413.
- **Goes to a checker** (rule 5): challenged by Mimo. Lines at stake: L413.

#### D13.5 · definition · New (N)

Lines it formalizes or quotes (from the brief): L416.

- **Mimo** (reply line 37; does not challenge): Named among the items with nothing to add.
  - Quotations: “Closing an episode is a choice” — found at L429.
- **GLM** (reply line 41; does not challenge): Named among the items with nothing to add.
- **Goes to no checker**: no point challenges it and it is not one of the twelve; recorded under rule 7 below.

#### D13.6 · definition · Attempt; Origin (G)

Lines it formalizes or quotes (from the brief): L422.

- **Mimo** (reply line 37; does not challenge): Named among the items with nothing to add.
  - Quotations: “Closing an episode is a choice” — found at L429.
- **GLM** (reply line 41; does not challenge): Named among the items with nothing to add.
- **Goes to no checker**: no point challenges it and it is not one of the twelve; recorded under rule 7 below.

#### D13.7 · definition · Ownership

Lines it formalizes or quotes (from the brief): L427.

- **Mimo** (reply line 37; does not challenge): Named among the items with nothing to add.
  - Quotations: “Closing an episode is a choice” — found at L429.
- **GLM** (reply line 41; does not challenge): Named among the items with nothing to add.
- **Goes to no checker**: no point challenges it and it is not one of the twelve; recorded under rule 7 below.

#### D13.8 · definition · Episodes

Lines it formalizes or quotes (from the brief): L429.

- **Mimo:** no point on this item.
- **GLM** (reply line 11; challenges): Four readings are read in, none registered (see H15).
  - Proposal `G15-B8` (reply lines 91), would change L429:

````
> L429 | A complete critical episode contains a recognized difficulty, a target represented before its criticism, a criticism of it (Part IX), and a response that uses that criticism as a reason (Part IX).
````

  - Proposal `G15-B9` (reply lines 93), would change L429:

````
> L429 | A creative critical episode contains an instance of (G) whose Attempt addresses the question its difficulty poses.
````

  - Proposal `G15-B10` (reply lines 97), would change L429:

````
> L429 | In (EX), Δ is the subhistory of the creative critical episode and s the owner of the (G) instance's subhistory.
````

- **Goes to a checker** (rule 5): challenged by GLM. Lines at stake: L429.

#### D14.1 · definition · Aims

Lines it formalizes or quotes (from the brief): L435, L441.

- **Mimo** (reply lines 13–17; challenges): Three ways apart: (1) the words' "a protected condition is lost exactly when it fails on an occasion it covers" is unbounded while (P) reads r over [ξ, ξ'] (FC86's look and the hand case disagree); (2) the left r(ξ) is unspecified (I57); (3) the words make each aim "a stated condition over stated occasions" while D14.1 reads O's aims pointwise; proposes new first two sentences of L441 (writes I57 in); under it the occasions of an O-aim do no work, which the text should accept or say what they delimit.
  - Proposal `M15-B2` (reply lines 15–17), would change L441:

````
L441 (first two sentences, replacing) | The aims are declared inputs: \(O\) says what is to be repaired and \(P\) what is to be protected, each as a stated condition over stated occasions; for \(o\in O\), \(o(\xi)\) and \(o(\xi')\) say that its condition was met at \(\xi\) and at \(\xi'\), and in a repair from \(\xi\) to \(\xi'\) a protected condition is lost exactly when it fails on an occasion it covers between \(\xi\) and \(\xi'\). In (P), accordingly, \(r(\xi)\) says that \(r\) was met at \(\xi\) when \(\xi\) is an occasion it covers and says nothing otherwise, and \(r(\xi')\) says of a protected condition \(r\) that it was met on every occasion it covers from \(\xi\) to \(\xi'\), not only at \(\xi'\).
````

  - Quotations: “a protected condition is lost exactly when it fails on an occasion it covers” — found at L441; “a stated condition over stated occasions” — found at L441; “from ξ to ξ'” — found at L441.
- **GLM** (reply line 13; challenges): The right-hand interval reading is quoted from the text; the left-side convention (r(ξ) holds when ξ ∉ Occ_r) is invented inside I57 and harmless, but it makes a protected aim whose occasions exclude ξ protected unconditionally; the text is silent; this should be recorded, not folded into I57.
  - Quotations: “holds otherwise” — not found in the text; found in the brief.
- **Goes to a checker** (rule 5): challenged by GLM and Mimo. Lines at stake: L441.

#### D14.2 · definition · Repair (P)

Lines it formalizes or quotes (from the brief): L438.

- **Mimo** (reply line 37; does not challenge): Named among the items with nothing to add.
  - Quotations: “Closing an episode is a choice” — found at L429.
- **GLM** (reply line 41; does not challenge): Named among the items with nothing to add.
- **Goes to no checker**: no point challenges it and it is not one of the twelve; recorded under rule 7 below.

#### D14.3 · definition · ProducedBy

Lines it formalizes or quotes (from the brief): L441.

- **Mimo** (reply lines 19–23; challenges): D14.3 lets the route run to the repair of any o with ¬o(ξ) ∧ o(ξ′), while the words' "the repair" is the one (P) is about; the words stand; proposes a new ProducedBy sentence in L441.
  - Proposal `M15-B3` (reply lines 21–23), would change L441:

````
L441 (replaces) | \(\operatorname{ProducedBy}\) is met when an active route (Part IX) runs from \(\Delta\) to the repair of an aim \(o\) with \(\neg o(\xi)\land o(\xi')\); it attributes the repair to each contribution whose active route ran to it in the history, and where two sufficient contributions both ran, the repair is attributed to both and the history supplies no division of the attribution that it does not contain.
````

  - Quotations: “runs from Δ to the repair” — found at L441, L453; “attributes the repair to each contribution whose active route ran to it” — found at L441.
- **GLM** (reply line 15; challenges): Attr matches "attributes the repair to each contribution whose active route ran to it"; "the history supplies no division of the attribution that it does not contain" is matched only negatively; the positive half (a division the history does contain is supplied by it) is written nowhere; the words stand; the omission is in the maths (FC87).
  - Quotations: “Attributes the repair to each contribution whose active route ran to it” — found at L441; “the history supplies no division of the attribution that it does not contain” — found at L441.
- **Goes to a checker** (rule 5): challenged by GLM and Mimo. Lines at stake: L441.

#### D14.4 · definition · Losses outside P

Lines it formalizes or quotes (from the brief): L441.

- **Mimo** (reply line 37; does not challenge): Named among the items with nothing to add.
  - Quotations: “Closing an episode is a choice” — found at L429.
- **GLM** (reply line 17; does not challenge): Exposure as a well-formedness condition on the claim is the right reading; matches; the open terms are I58.
  - Quotations: “Losses outside P must be exposed” — found at L441.
- **Goes to no checker**: no point challenges it and it is not one of the twelve; recorded under rule 7 below.

#### D14.5 · definition · Explanatory aims

Lines it formalizes or quotes (from the brief): L443.

- **Mimo** (reply line 25; challenges): The maths reads "requires" as a characterization; the words say "requires", a necessary condition, then declare O_ex ⊆ O; the words stand; neither names the use whose correction the second kind is about; the change under L443 in (e) carries it.
  - Proposal `M15-B10` (reply lines 101–103), would change L443:

````
L443 (replaces) | **Created explanation.** An explanatory aim requires a deployable account, or the correction of a use through one: its condition is that \(s\) possesses a deployable account of a stated question, or that a declared use of \(s\) is corrected through one. With \(O_{\mathrm{ex}}\subseteq O\) the explanatory aims,
````

  - Quotations: “requires” — found at L47, L155, L223, L407 and 6 more lines; “o is explanatory when...” — not found in the text; found in the brief.
- **GLM** (reply line 19; challenges): The round-1 wording fixed a real type mismatch, but "requires" is read as a characterization of O_ex when it reads at least as naturally as necessary-only (see I59).
  - Proposal `G15-B5` (reply lines 73), would change L443:

````
> L443 | An aim of O is explanatory when its condition is that s possesses a deployable account of a stated question, or that a use of an account be corrected through it.
````

  - Quotations: “requires” — found at L47, L155, L223, L407 and 6 more lines.
- **Goes to a checker** (rule 5): challenged by GLM and Mimo. Lines at stake: L443.

#### D14.6 · definition · Result; ProducesVia

Lines it formalizes or quotes (from the brief): L453.

- **Mimo** (reply lines 27–31; challenges): "The relevant binding of c" is not defined (I60); the maths takes the binding named in c's construction trace; the words stand and should name the binding; proposes a new L453.
  - Proposal `M15-B4` (reply lines 29–31), would change L453:

````
L453 (replaces) | \(\operatorname{Result}(\Delta)\) is the set of contents at \(\xi'\) that \(\Delta\) prepared. \(\operatorname{ProducesVia}(\Delta,c,o;\xi,\xi')\) is met when an active route that runs from \(\Delta\) to the repair of \(o\) contains an occurrence of the binding that \(c\)'s construction trace names (L405).
````

  - Quotations: “the relevant binding of c” — found at L453.
- **GLM** (reply line 21; challenges): Result matches; "the relevant binding of c" is nearly settled by L405's own list (see I60).
  - Proposal `G15-B6` (reply lines 79), would change L453:

````
> L453 | … contains the relevant binding of c — the binding named in its construction trace. For an aim whose condition is the correction of a use, that route is the correction's running through the account; for an aim whose condition is possession, Deploy and Account carry it.
````

  - Quotations: “The relevant binding of c” — found at L453.
- **Goes to a checker** (rule 5): challenged by GLM and Mimo. Lines at stake: L453.

#### D14.7 · definition · Created explanation (EX)

Lines it formalizes or quotes (from the brief): L447, L448, L449.

- **Mimo** (reply line 33; challenges): As displayed; CreativeCriticalEpisode(s,Δ,h,e) takes s and Δ, which its definition never uses (H15); "the contract of p_c fixed at e_c (L453)" is cited to L453, whose quoted words do not say it.
  - Quotations: “the contract of p_c fixed at e_c (L453)” — not found in the text; found in the brief.
- **GLM** (reply line 23; does not challenge): As displayed; nothing to add.
- **Goes to a checker** (rule 5): challenged by Mimo. Lines at stake: L447, L448, L449.

#### D14.8 · definition · Appraisal, typed only

Lines it formalizes or quotes (from the brief): L455.

- **Mimo** (reply line 35; challenges): The maths types 𝓡 ⊆ Act × Occ × Eff and G ⊆ Occ × Eff, so k is an occasion; the words do not type k; a choice no entry records, to be recorded, since (AR) is empty unless it is fixed; NF19 rightly stays unformalized.
  - Quotations: “None is defined as another” — found at L51, L455.
- **GLM** (reply line 25; does not challenge): Typed only, 𝒩 an input with V_A unspecified; the reader calls this restraint correct, since "where values are placed is the owner's question and is not touched here".
- **Goes to a checker** (rule 5): challenged by Mimo. Lines at stake: L455.

#### FC84 · claim · Every creative attribution requires construction

Lines it formalizes or quotes (from the brief): L47.

- **Mimo** (reply line 87; does not challenge): Hand model: assembling known contents by content-preserving transfers meets Attempt and New but not Build, so (G) fails; FC84 is not broken; the sentence's reach: assembling by transfer is not construction; rests on I56 and L405's exclusion; the words stand.
- **GLM** (reply line 27; does not challenge): Holds by construction because (G) is a conjunction containing Build, which is how the text writes it; the second half of L47 is argued from lines the reader lacks (see (d)).
  - Quotations: “separate provenance with a separate trace” — found at L47.
- **GLM** (reply line 105; does not challenge): Cannot break it inside the lines given; "holds by construction" means written into the program; L47 is substantive only if no other part of the text attributes creation outside these definitions, a reading of L528 and Part IV the reader lacks; not to be counted as tested until checked there.
  - Quotations: “holds by construction” — not found in the text; found in the brief.
- **External reader and case card:** E14 (the external reader) challenges the sentence this item formalizes (section 3 below).
- **Goes to a checker** (rule 5): challenged by E14 (the external reader). Lines at stake: L47.

#### FC85 · claim · A content matches itself; the matching is read one way

Lines it formalizes or quotes (from the brief): L413, L416.

- **Mimo** (reply line 41; does not challenge): FC85's "no witness found" on the generated families is no evidence against the asymmetry; the constructed computation shows d ≡ c with c ≢ d.
- **Mimo** (reply line 89; challenges): (a) holds only where the identity is a transport; if the transport space (I81) holds only translations that alter a port, (N) calls a content already deployable new; whether the text's "transports" admit the identity must be checked at lines not given; second, contracts are fixed at events, and (N) does not say which contract it uses; the L413 wording removes the second point.
  - Proposal `M15-B1` (reply lines 9–11; printed in full under D13.4 above), would change L413.
  - Quotations: “transports” — found at L17, L61, L67, L119 and 13 more lines.
- **GLM** (reply line 29; does not challenge): Says what the sentences say (see (d)).
- **GLM** (reply lines 101–103; challenges): Hand model: if I81's generated translations exclude the identity (x ↦ x + k), no transport from E_c to E_c is faithful, c ≢ c, and the system's own content counts as new, defeating (N); rests on I81 and I77, against the invention, not the text; proposes a sentence for L413 closing it for every implementation (the identity counts as a transport both ways).
  - Proposal `G15-B11` (reply lines 103), would change L413:

````
> L413 | The identity on c's own organization counts as a transport in both directions.
````

- **Goes to a checker** (rule 5): challenged by GLM and Mimo. Lines at stake: L413.

#### FC86 · claim · Repair: a protected aim failed in between is lost

Lines it formalizes or quotes (from the brief): L438, L441.

- **Mimo** (reply line 41; challenges): FC86's look came out as expected; its divergence (L441's "lost" against (P)) is a matter of wording, dealt with under D14.1.
  - Proposal `M15-B2` (reply lines 15–17; printed in full under D14.1 above), would change L441.
- **Mimo** (reply line 91; challenges): Hand model: r fails at 0 and holds at 1, 2, 3; repair from 1 to 3; under I57 r is kept, under L441's words ("a protected condition is lost exactly when it fails on an occasion it covers") r is lost; not a counterexample to FC86's claim but to the sentence as written; the D14.1 wording removes it (rests on I57, I96).
  - Proposal `M15-B2` (reply lines 15–17; printed in full under D14.1 above), would change L441.
  - Quotations: “a protected condition is lost exactly when it fails on an occasion it covers” — found at L441.
- **GLM** (reply line 31; challenges): The formal claim matches (P) under the interval reading; L441's "exactly when" is stronger than the claim tested (see (b)).
  - Proposal `G15-B1` (reply lines 49), would change L441:

````
> L441 | a protected condition met at ξ is lost exactly when it fails on an occasion it covers from ξ to ξ'.
````

  - Quotations: “exactly when” — found at L231, L305, L313, L329 and 1 more lines.
- **GLM** (reply lines 45–51; challenges): The look (r failing at 0 and 1, ξ = 0): (P) asks nothing of r, yet L441's words call it lost; not against I57 or (P) but against the unconditional "exactly when" in L441 (an aim already failing at ξ was lost before the repair); proposes a new clause for L441 ("a protected condition met at ξ is lost exactly when …").
  - Proposal `G15-B1` (reply lines 49; printed in full under FC86 above), would change L441.
  - Quotations: “fails on an occasion it covers” — found at L441; “exactly when” — found at L231, L305, L313, L329 and 1 more lines; “protected” — found at L147, L315, L317, L429 and 3 more lines; “what is to be repaired” — found at L441.
- **GLM** (reply line 107; challenges): The formal claim survives on discrete and continuous time; the break is the one in (b), of the sentence.
  - Proposal `G15-B1` (reply lines 49; printed in full under FC86 above), would change L441.
  - Quotations: “exactly when” — found at L231, L305, L313, L329 and 1 more lines.
- **Goes to a checker** (rule 5): challenged by GLM and Mimo. Lines at stake: L441.

#### FC87 · claim · Two sufficient contributions that both ran are both attributed

Lines it formalizes or quotes (from the brief): L441.

- **Mimo** (reply line 93; challenges): Hand model: two contributions each with a route to o1's coming-to-be-met and none to o2's are, under I57, attributed to the repair of o2; the sentence is not broken; the wrong attribution comes from I57 and is removed by the L441 wording; "sufficient" is nowhere defined.
  - Proposal `M15-B3` (reply lines 21–23; printed in full under D14.3 above), would change L441.
  - Quotations: “Sufficient” — found at L441.
- **GLM** (reply line 33; challenges): The both-attributed half matches; the no-division half is matched only by the absence of a definition; the sentence's positive implication is not carried.
- **GLM** (reply line 109; challenges): Hand model: two routes to the same aim, one completing it, the other running on; both attributed, as the text says; but the history contains a division the maths cannot read out (it has only declared weightings, L522); a counterexample to the formalization's completeness against the sentence's second half; the words stand; the maths should add a division read from the history.
- **Goes to a checker** (rule 5): challenged by GLM and Mimo. Lines at stake: L441.

#### FC88 · claim · Losses outside P are exposed in the claim, not in (P)

Lines it formalizes or quotes (from the brief): L441.

- **Mimo** (reply line 95; challenges): Hand model: a held aim a2 lost between ξ and ξ′ is unexposed while the claim is well formed, since "Losses outside P must be exposed" is checked only on declared aims (rests on I58); the I58 wording removes it.
  - Proposal `M15-B6` (reply lines 55–57), would change L441:

````
L441 (replaces) | Losses outside \(P\) must be exposed: the repair claim lists every aim the system holds outside \(P\) that was met at \(\xi\) and is not met at \(\xi'\).
````

  - Quotations: “Losses outside P must be exposed” — found at L441.
- **GLM** (reply line 35; does not challenge): Computed as claimed; the reading is right; matches.
- **GLM** (reply line 111; does not challenge): Could not break it; the I58 wording fixes the universe as the aims under consideration.
- **Goes to a checker** (rule 5): challenged by Mimo. Lines at stake: L441.

#### FC89 · claim · L443 (after round 1) puts 'deployable' where Deploy's type allows it

Lines it formalizes or quotes (from the brief): L443, L449.

- **Mimo:** no point on this item.
- **GLM** (reply line 37; challenges): Not tested, rightly; the reading is sound (after round 1 both kinds put Deploy on the account c; the second kind is carried by ProducesVia); (EX) does not check that an aim of the first kind is met by possession and one of the second by correction; if the text wants kind-matching, one sentence after L453 settles it (under I60).
  - Proposal `G15-B6` (reply lines 79; printed in full under D14.6 above), would change L453.
  - Quotations: “through one” — found at L443.
- **Goes to a checker** (rule 5): challenged by GLM. Lines at stake: L453.

#### FC90 · claim · The worked case's '(EX) is met' against (EX)'s conjuncts

Lines it formalizes or quotes (from the brief): L628.

- **Mimo:** no point on this item.
- **GLM** (reply line 53; challenges): Not a counterexample but a stated result the case's description does not deliver: the case stipulates Build and New, (P), Account and "deployable", but (EX) needs the episode's four parts, Attempt, c ∈ Result(Δ), ProducesVia and e_c ⪯_h e, none stated, and "deployable" is not Deploy at a use U_c; L628's final sentence asserts more than the case gives (fix in (e)).
  - Proposal `G15-B12` (reply lines 117), would change L628:

````
> L628 | The episode contains the difficulty, the target before its criticism, the objection and the response (Part X); S_1's construction was used in it to address the question the difficulty poses; the aim is explanatory, not met at ξ and met at ξ'; the binding of the persistence component to the continuity subnetwork lies on an active route from Δ to that aim's being met; e_c precedes e in h. Since S_1 is an account on its contract and deployable at ξ' at a use, (EX) is met.
````

  - Quotations: “deployable” — found at L403, L443, L628.
- **Goes to a checker** (rule 5): challenged by GLM. Lines at stake: L628.

#### I55 · invention · Deploy: 'integrated into problem-directed activity', 'nontrivial use respect'

Lines it formalizes or quotes (from the brief): L403.

- **Mimo** (reply lines 45–49; challenges): Not settled: L403 gives the words and no conditions; proposes a new L403 (writes I55 in, as declared inputs of the physical module).
  - Proposal `M15-B5` (reply lines 47–49; printed in full under D13.1 above), would change L403.
- **GLM** (reply lines 57–59; challenges): On what is given here "integrated into problem-directed activity", "nontrivial use respect" and "retained" are not settled (the text defers to Part XII, not given); proposes new wording in L403 (writes I55's alternative (a) and a retention clause in).
  - Proposal `G15-B2` (reply lines 59; printed in full under D13.1 above), would change L403.
  - Quotations: “integrated into problem-directed activity” — found at L403; “nontrivial use respect” — found at L403; “retained” — found at L403, L461, L463, L475.
- **Goes to a checker** (rule 5): challenged by GLM and Mimo. Lines at stake: L403.

#### I57 · invention · Repair: how the aims are read at ξ and over [ξ, ξ']; which aim ProducedBy runs to

Lines it formalizes or quotes (from the brief): L441.

- **Mimo** (reply line 51; challenges): Not settled (the left reading of r(ξ), which aim ProducedBy's route runs to, how O's occasions are read); the wordings under D14.1 and D14.3 write I57 in.
  - Proposal `M15-B2` (reply lines 15–17; printed in full under D14.1 above), would change L441.
  - Proposal `M15-B3` (reply lines 21–23; printed in full under D14.3 above), would change L441.
- **GLM** (reply lines 61–63; challenges): The interval reading is settled, quoted ("met on every occasion it covers from ξ to ξ′, not only at ξ′"); the ProducedBy target is not; the invented choice and its alternative coincide in force; proposes a sentence for L441.
  - Proposal `G15-B3` (reply lines 63), would change L441:

````
> L441 | The route runs to an aim of O that was not met at ξ and is met at ξ'; it need not be the aim picked for (P)'s first conjunct, since (P) asks only that some aim of O be so.
````

  - Quotations: “met on every occasion it covers from ξ to ξ', not only at ξ'” — found at L441.
- **Goes to a checker** (rule 5): challenged by GLM and Mimo. Lines at stake: L441.

#### I58 · invention · 'Losses outside P': the aims considered, and 'exposed'

Lines it formalizes or quotes (from the brief): L441.

- **Mimo** (reply lines 53–57; challenges): Not settled: "Losses outside P must be exposed" names no universe of aims and no place of exposure; the words bind on every aim the system holds, and that reading stands; proposes a new sentence in L441.
  - Proposal `M15-B6` (reply lines 55–57; printed in full under FC88 above), would change L441.
  - Quotations: “Losses outside P must be exposed” — found at L441.
- **GLM** (reply lines 65–69; challenges): Not settled (neither the universe of losses nor "exposed"); proposes a sentence for L441 (writes I58 in: aims under consideration, named in the claim's record of losses).
  - Proposal `G15-B4` (reply lines 67), would change L441:

````
> L441 | Losses outside P — aims under consideration when the claim is made, met at ξ and not met at ξ' — are named in the claim's record of losses. The aims under consideration include O and P.
````

  - Quotations: “exposed” — found at L441, L538.
- **Goes to a checker** (rule 5): challenged by GLM and Mimo. Lines at stake: L441.

#### I59 · invention · Explanatory aims: L443 read as a characterization of O_ex

Lines it formalizes or quotes (from the brief): L443.

- **Mimo** (reply line 59; challenges): Not settled; the wording under L443 in (e) writes I59 in.
  - Proposal `M15-B10` (reply lines 101–103; printed in full under D14.5 above), would change L443.
- **GLM** (reply lines 71–75; challenges **OWNER QUESTION**): Not settled: "requires" reads as necessary-only at least as easily as a characterization; proposes a new sentence at L443 (writes I59 in, keeping the round-1 fix); "If instead the owner wants necessary-only, say so at L443".
  - Proposal `G15-B5` (reply lines 73; printed in full under D14.5 above), would change L443.
  - Quotations: “requires” — found at L47, L155, L223, L407 and 6 more lines; “With O_ex ⊆ O the explanatory aims” — found at L443.
- **Goes to a checker** (rule 5): challenged by GLM and Mimo. Lines at stake: L443.
- Marks: OWNER QUESTION points present.

#### I60 · invention · ProducesVia: 'the relevant binding of c'

Lines it formalizes or quotes (from the brief): L453.

- **Mimo** (reply line 61; challenges): Not settled; the D14.6 wording writes I60 in.
  - Proposal `M15-B4` (reply lines 29–31; printed in full under D14.6 above), would change L453.
  - Quotations: “the relevant binding of c” — found at L453.
- **GLM** (reply lines 77–79; challenges): Largely settled: L405 lists a trace's parts ("the incoming carriers, the bindings constructed, the resulting representation") and L409 lets a binding be identified by its use; proposes a sentence for L453 closing it, with the kind-matching FC89 found missing.
  - Proposal `G15-B6` (reply lines 79; printed in full under D14.6 above), would change L453.
  - Quotations: “the incoming carriers, **the bindings constructed**, the resulting representation” — not found in the text; found in the brief; “The relevant binding of c” — found at L453.
- **Goes to a checker** (rule 5): challenged by GLM and Mimo. Lines at stake: L453.

#### I68 · invention · Argument 10's two-layer episode, encoded; 'recent occupancy'

Lines it formalizes or quotes (from the brief): L620, L622.

- **Mimo** (reply lines 63–67; challenges): Not settled: L620–L622 stipulate the layer but not S_0's window or the rule at the ends, and the case's criticism turns on the window against the occlusion; proposes a new L622 (a fixed window shorter than any occlusion the criticism admits), which the reader says removes the resting point of FC102's counterexample.
  - Proposal `M15-B7` (reply lines 65–67), would change L622:

````
L622 (replaces) | \(S_0\) predicts occupancy at \(t+1\) from the occupancy of the last \(w\) steps, \(w\) fixed and shorter than any occlusion the criticism admits.
````

- **GLM:** no point on this item.
- **External reader and case card:** E10 (the external reader) challenges the sentence this item formalizes (section 3 below).
- **Goes to a checker** (rule 5): challenged by Mimo; challenged by E10 (the external reader). Lines at stake: L622.

#### I96 · invention · Aims on discrete time

Lines it formalizes or quotes (from the brief): L441.

- **Mimo** (reply line 69; does not challenge): Should stay open: "stated occasions" is already a declared input; discrete time is the search's domain.
  - Quotations: “stated occasions” — found at L441.
- **GLM:** no point on this item.
- **Goes to no checker**: no point challenges it and it is not one of the twelve; recorded under rule 7 below.

#### H06 · H-entry · An episode is any subhistory (D13.8), against L55's sentence

Lines it formalizes or quotes (from the brief): L55, L197.

- **Mimo** (reply lines 71–75; challenges): Not settled: the body never defines "episode"; L55's front-matter sentence is the only definition; the body's uses (L197, L405, L429) need only a delimited subhistory, and the contract-change clause would silently add a condition to Con and (EX); the body stands and L55 should be narrowed; proposes a new L55 (writes H06 in).
  - Proposal `M15-B8` (reply lines 73–75), would change L55:

````
L55 (replaces) | An episode is a delimited subhistory of a history. An episode of provenance is one in which contracts change, and every change carries a provenance record.
````

  - Quotations: “episode” — found at L13, L31, L55, L155 and 12 more lines.
- **GLM** (reply lines 81–85; challenges **OWNER QUESTION**): The text conflicts with itself: L55 defines an episode by contract changes with records, while the body uses "episode" as a bounded stretch and never defines it; L35 makes the body govern; the body should carry the definition, merging L55's demand; proposes a new L429 opening (writes H06's reading in); "If the owner wants L55's stricter reading, that is a different theory of (G) and should be decided, not left".
  - Proposal `G15-B7` (reply lines 83), would change L429:

````
> L429 | **Episodes.** An episode is a subhistory delimited by the occasions that bound it; where contracts change in it, every change carries a provenance record. A complete critical episode contains a recognized difficulty, a target available before its criticism, a conjectural objection, and a content-sensitive response.
````

  - Quotations: “delimited at e” — found at L405; “contains” — found at L25, L39, L49, L109 and 13 more lines; “episode” — found at L13, L31, L55, L155 and 12 more lines.
- **External reader and case card:** C07 (the case card) challenges the sentence this item formalizes (section 4 below).
- **Goes to a checker** (rule 5): challenged by GLM and Mimo; challenged by C07 (the case card). Lines at stake: L55, L429.
- Marks: OWNER QUESTION points present.

#### H14 · H-entry · Contribution of content as a primitive (D13.7)

Lines it formalizes or quotes (from the brief): L427.

- **Mimo** (reply line 77; challenges): No wording: L427 states the distinction and no definition uses Contrib; it should be dropped from the maths.
- **GLM** (reply line 87; challenges): The text settles only the separation ("different attributions"); who supplied a content should stay open, like L522's weighting; no wording; the primitive should have been registered.
  - Quotations: “different attributions” — found at L427, L441.
- **Goes to a checker** (rule 5): challenged by GLM and Mimo. Lines at stake: L427.

#### H15 · H-entry · The four parts of a critical episode, and "connected to its inquiry" (D13.8)

Lines it formalizes or quotes (from the brief): L429.

- **Mimo** (reply lines 79–83; challenges): Not settled: "available", "a conjectural objection", "a content-sensitive response", "connected to its inquiry" are read in for the first time, and s and Δ are never taken up; proposes a new L429 (writes H15 in).
  - Proposal `M15-B9` (reply lines 81–83), would change L429:

````
L429 (replaces) | **Episodes.** A complete critical episode contains a recognized difficulty, a target represented before its criticism, a conjectural objection (D9.10) of it, and a content-sensitive response that uses the objection as a reason (D9.11). A **recognized difficulty** is a failure of a claimed aim, or a conflict in which what the system holds meets a claimed aim only by failing a protected one (Part XI), when the system represents it. A creative critical episode contains an instance of (G) whose attempt addresses the question the episode's difficulty poses; in \(\operatorname{CreativeCriticalEpisode}(s,\Delta,h,e)\), \(s\) is the system whose episode it is and \(\Delta\) is the contribution of its content-sensitive response.
````

  - Quotations: “available” — found at L57, L197, L405, L409 and 2 more lines; “a conjectural objection” — found at L429; “a content-sensitive response” — found at L429; “connected to its inquiry” — found at L429.
- **GLM** (reply lines 89–97; challenges): None of the four readings is settled; proposes three sentences for L429 (a represented target, a criticism, a response using it as a reason; (G)'s Attempt addressing the difficulty's question; how s and Δ enter (EX)) (writes H15 in).
  - Proposal `G15-B8` (reply lines 91; printed in full under D13.8 above), would change L429.
  - Proposal `G15-B9` (reply lines 93; printed in full under D13.8 above), would change L429.
  - Proposal `G15-B10` (reply lines 97; printed in full under D13.8 above), would change L429.
  - Quotations: “available” — found at L57, L197, L405, L409 and 2 more lines; “conjectural objection” — found at L429; “content-sensitive response” — found at L429; “connected to its inquiry” — found at L429.
- **Goes to a checker** (rule 5): challenged by GLM and Mimo. Lines at stake: L429.

#### NF07 · NF entry

Lines it formalizes or quotes (from the brief): L201.

- **Mimo** (reply line 37; does not challenge): Named among the items with nothing to add.
  - Quotations: “Closing an episode is a choice” — found at L429.
- **GLM:** no point on this item.
- **External reader and case card:** E14 (the external reader) challenges the sentence this item formalizes (section 3 below); C02 (the case card) challenges the sentence this item formalizes (section 4 below).
- **Goes to a checker** (rule 5): challenged by E14 (the external reader), C02 (the case card). Lines at stake: L201.

#### NF09 · NF entry

Lines it formalizes or quotes (from the brief): L407.

- **Mimo** (reply line 37; does not challenge): Nothing to add: Deploy rightly takes no format argument.
  - Quotations: “Closing an episode is a choice” — found at L429.
- **GLM:** no point on this item.
- **Goes to no checker**: no point challenges it and it is not one of the twelve; recorded under rule 7 below.

#### NF10 · NF entry

Lines it formalizes or quotes (from the brief): L429.

- **Mimo** (reply line 37; does not challenge): Nothing to add: "Closing an episode is a choice"; no definition outputs a choice, as S21 and S28 require.
  - Quotations: “Closing an episode is a choice” — found at L429.
- **GLM:** no point on this item.
- **Goes to no checker**: no point challenges it and it is not one of the twelve; recorded under rule 7 below.

#### L443 · round-1 change · the round-1 change at L443

Lines it formalizes or quotes (from the brief): L443.

- **Mimo** (reply lines 99–103; challenges): The round-1 change stands (before it "to be deployable" could attach to the correction, which Deploy cannot take); the line still names no use, and (EX) has no condition that c corrected one (FC89); proposes a new L443 keeping the change and naming the two conditions (writes I59 in); with it and the L453 wording (EX) needs nothing further (the reply heads this "matter 1 · L443").
  - Proposal `M15-B10` (reply lines 101–103; printed in full under D14.5 above), would change L443.
  - Quotations: “to be deployable” — not found in the text; found in the brief; “the correction of a use through one” — found at L443; “a deployable account” — found at L443, L628.
- **GLM** (reply lines 115–119; challenges): The change was needed and is right (a correction, a subhistory, was asked to be deployable, and Deploy takes a content); the "requires" ambiguity remains, settled by the I59 proposal, which supersedes the round-1 sentence while keeping its fix; what the change may have disturbed ((EX), ProducesVia, the worked case at L628) needs the FC89 kind-matching sentence and a repair of the worked case; proposes a new L628 passage (relying on L620–L628 beyond the fragments quoted).
  - Proposal `G15-B5` (reply lines 73; printed in full under D14.5 above), would change L443.
  - Proposal `G15-B6` (reply lines 79; printed in full under D14.6 above), would change L453.
  - Proposal `G15-B12` (reply lines 117; printed in full under FC90 above), would change L628.
  - Quotations: “requires” — found at L47, L155, L223, L407 and 6 more lines; “deployable” — found at L403, L443, L628.
- **Goes to a checker** (rule 5): challenged by GLM and Mimo. Lines at stake: L443, L453, L628.

#### Part 15: items no point addresses

Items of this part on which neither reader made any point (both replies read whole): NF19. Each is recorded under rule 7 in section 6 unless a point on it in another part sends it to a checker.

### Part 16: The physical module, recursion, universality and the class collected

Brief: `tests/S104 Round 2 - the maths against the words - part 16, The physical module, recursion, universality and the class collected.md`. Replies: `s104_maths_mimo_16.response.txt` (Mimo), `s104_maths_glm_16.response.txt` (GLM).

#### D15.1 · definition · Tasks

Lines it formalizes or quotes (from the brief): L461.

- **Mimo** (reply line 3; challenges): D15.1 records resources and side effects as "stated" (I61) and no definition consults them, so "explicit" is inert (two tasks with one input/output relation are one task); the words stand (resources and side effects are parts of the task); the maths must carry them as components of T; no wording change forced.
  - Quotations: “… a task a specified input-to-output attribute transformation with explicit resources and side effects.” — found at L461; “stated” — found at L43, L61, L159, L189 and 14 more lines; “explicit” — found at L407, L409, L461, L473.
- **GLM** (reply line 5; does not challenge): The maths writes a task as a relation where "a specified input-to-output attribute transformation" suggests one output per input; the text does not settle it; leave open; the maths' choice does no work against the words.
  - Quotations: “a specified input-to-output attribute transformation” — found at L461.
- **Goes to a checker** (rule 5): challenged by Mimo. Lines at stake: L461.

#### D15.2 · definition · Retained realization (CT1)

Lines it formalizes or quotes (from the brief): L466, L469.

- **Mimo** (reply line 43; does not challenge): Named among the items with nothing to add.
  - Quotations: “that would need a part every member of the population is built without” — found at L481.
- **GLM** (reply line 26; does not challenge): Named among the items with nothing to add.
- **External reader and case card:** E17 (the external reader) challenges the sentence this item formalizes (section 3 below).
- **Goes to a checker** (rule 5): challenged by E17 (the external reader). Lines at stake: L466.

#### D15.3 · definition · Retention operator; (CT2)

Lines it formalizes or quotes (from the brief): L471.

- **Mimo** (reply line 43; does not challenge): Nothing to add (see (e)).
  - Quotations: “that would need a part every member of the population is built without” — found at L481.
- **GLM** (reply line 26; does not challenge): Named among the items with nothing to add.
- **Goes to no checker**: no point challenges it and it is not one of the twelve; recorded under rule 7 below.

#### D15.4 · definition · Boundary and continuity

Lines it formalizes or quotes (from the brief): L473.

- **Mimo** (reply line 5; challenges): The text's continuity is "what makes it the same system through change"; D15.4 writes Ω as a relation on states, an extensional shadow, dropping "through change"; the words stand; the maths should say which is which.
  - Quotations: “… a continuing organization in \(C_I\).” — found at L477; “what makes it the same system through change” — found at L473; “through change” — found at L473; “ends with an organization in C_I” — not found in the text; found in the brief; “continuing” — found at L477; “the independently specified \(J_p\)” — found at L477.
- **GLM** (reply line 26; does not challenge): Named among the items with nothing to add.
- **External reader and case card:** E13 (the external reader) challenges the sentence this item formalizes (section 3 below).
- **Goes to a checker** (rule 5): challenged by Mimo; challenged by E13 (the external reader). Lines at stake: L473.

#### D15.5 · definition · Owned capability

Lines it formalizes or quotes (from the brief): L475.

- **Mimo** (reply lines 7–11; challenges): "Requires" states necessity where D15.5 writes :⟺; the header makes the line a definition, so the biconditional is the reading the text allows but does not force; proposes a new L475 making it explicit.
  - Proposal `M16-B1` (reply lines 9–11), would change L475:

````
> L475 | **Owned capability.** \(\operatorname{Can}_{\Omega,\beta}(\xi,T;\chi)\) is had exactly when there is an owned retained realization or an owned, physically admitted, finite construction of one under the same continuity and resource contract.
````

  - Quotations: “… \(\operatorname{Can}_{\Omega,\beta}(\xi,T;\chi)\) requires …” — found at L475; “requires” — found at L47, L155, L223, L407 and 6 more lines.
- **GLM** (reply line 26; does not challenge): Named among the items with nothing to add.
- **Goes to a checker** (rule 5): challenged by Mimo. Lines at stake: L475.

#### D15.6 · definition · Advancing capability (CA)

Lines it formalizes or quotes (from the brief): L477.

- **Mimo** (reply line 5; challenges): L477's "a continuing organization in C_I" becomes "ends with an organization in C_I", losing "continuing"; "the independently specified J_p" is a requirement the maths takes as a parameter without enforcing independence, an invention to record; the words stand.
  - Quotations: “… a continuing organization in \(C_I\).” — found at L477; “what makes it the same system through change” — found at L473; “through change” — found at L473; “ends with an organization in C_I” — not found in the text; found in the brief; “continuing” — found at L477; “the independently specified \(J_p\)” — found at L477.
- **GLM** (reply line 16; challenges): D15.6 takes J_p as a parameter and drops "independently specified"; the words demand an independence the maths cannot state, beside NF11's "independently characterized"; no change to the text; the omission should be recorded.
  - Quotations: “independently specified” — found at L477; “independently characterized” — found at L495.
- **Goes to a checker** (rule 5): challenged by GLM and Mimo. Lines at stake: L477.

#### D15.7 · definition · Tolerances; Admit, Cap, Poss

Lines it formalizes or quotes (from the brief): L479.

- **Mimo** (reply lines 13–23; challenges): The order matches, but it orders performances while Admit is a set of tasks, so Admit's antitonicity is I62's step; larger: L461's possibility ("the absence of a law-imposed limit, short of exact") equals ⋂Admit only if tolerances are unbounded in strictness; L479 rules out an exact member but allows a strictest non-exact one; proposes two new L479 passages (no strictest tolerance; Admit as the tasks with a realization, writing I62's main reading in and making (CT3) a consequence).
  - Proposal `M16-B2` (reply lines 15–17), would change L479:

````
> L479 | The tolerances of the physical module (Part XIV) form a directed preorder \(Q_\Theta\), in which \(q\) precedes \(q'\) when \(q'\) admits no performance \(q\) excludes, none of them is exact, and none of them is strictest: for every \(q\) there is a \(q'\) that excludes at least what \(q\) excludes and excludes something \(q\) admits;
````

  - Proposal `M16-B3` (reply lines 19–21), would change L479:

````
> L479 | \(\mathsf{Admit}^{q,r}_\Theta\) is the set of tasks physically achievable at tolerances \((q,r)\), that is, the tasks with a realization at those tolerances;
````

  - Quotations: “q' admits no performance q excludes” — found at L479; “q' excludes at least what q excludes” — not found in the text; found in the brief; “the absence of a law-imposed limit, short of exact, on the tolerance” — found at L461; “short of exact” — found at L461.
- **GLM** (reply line 7; challenges): Poss_Θ = ⋂Admit and L461's "the absence of a law-imposed limit, short of exact" part company if a task is not law-excluded yet has no realization at some tolerance; the words at L461 should stand; the link is I62's (under I62).
  - Proposal `G16-B2` (reply lines 39–42), would change L479:

````
L479 (replaces current line; inserts one clause after "physically achievable at tolerances \((q,r)\)")
… \(\mathsf{Admit}^{q,r}_\Theta\) is the set of tasks physically achievable at tolerances \((q,r)\), where a task with a physically admitted realization at \((q,r)\), owned or not, counts as achievable; …
````

  - Quotations: “the absence of a law-imposed limit, short of exact, on the tolerance to which a task can be performed and retained” — found at L461.
- **External reader and case card:** E17 (the external reader) challenges the sentence this item formalizes (section 3 below).
- **Goes to a checker** (rule 5): challenged by GLM and Mimo; challenged by E17 (the external reader). Lines at stake: L479.

#### D15.8 · definition · Selection's population

Lines it formalizes or quotes (from the brief): L481.

- **Mimo** (reply line 43; challenges): Nothing to add, save that the words exclude only a transport "that would need a part every member of the population is built without", while D15.8 requires parts(t) within the stated construction's parts and drops that clause; the words stand; no claim here rests on it.
  - Quotations: “that would need a part every member of the population is built without” — found at L481.
- **GLM** (reply lines 9–14; challenges): L481's second clause is circular ("a part every member of the population is built without" presupposes the population it defines); the maths silently anchors it to the stated construction's parts, a choice no entry records; proposes a new L481 (writing D15.8's choice in; it should also be registered).
  - Proposal `G16-B1` (reply lines 10–13), would change L481:

````
L481 (replaces current line)
The population is the set of transports the physics and the stated construction admit; a transport that would need a part the stated construction is built without is not in it.
````

  - Quotations: “a part every member of the population is built without” — found at L481; “the parts of the stated construction” — not found in the text; found in the brief.
- **Goes to a checker** (rule 5): challenged by GLM and Mimo. Lines at stake: L481.

#### D16.1 · definition · Scrutinizable

Lines it formalizes or quotes (from the brief): L487.

- **Mimo** (reply line 25; challenges): H16 stands against the maths: L487's "the result can affect its operative use" is modal, D16.1's "a result on an active route" structural and stronger; the words stand.
  - Quotations: “the result can affect its operative use.” — found at L487; “a result on an active route to d's operative use” — not found in the text; found in the brief; “enabling” — found at L463, L477, L492, L495.
- **GLM** (reply line 18; challenges): See H16.
- **Goes to a checker** (rule 5): challenged by GLM and Mimo. Lines at stake: L487.

#### D16.2 · definition · Recursive capacity (RC)

Lines it formalizes or quotes (from the brief): L492.

- **Mimo** (reply lines 25–31; challenges): L492's "an owned enabling continuation" is read by I74 as a continuation meeting Scr(d_n), while "enabling" is L495's term for an enabling condition χ; the line serves both readings and must say which; proposes a new L492 (writes I74's reading in).
  - Proposal `M16-B4` (reply lines 27–29), would change L492:

````
> L492 | \(\forall n<\omega\ \forall\) admitted target chains of length \(n\), \(\exists\) an owned continuation making the last link scrutinizable. \tag{RC}
````

  - Quotations: “the result can affect its operative use.” — found at L487; “a result on an active route to d's operative use” — not found in the text; found in the brief; “enabling” — found at L463, L477, L492, L495; “… in the sense of (CT1).” — found at L495; “non-question-begging” — found at L495.
- **GLM** (reply line 20; challenges): The words say only "an owned enabling continuation"; I74's reading is natural but not in the sentence (under I74).
  - Proposal `G16-B3` (reply lines 46–50), would change L492:

````
L492 (replaces current line; adds one sentence after the displayed formula)
\forall n<\omega\ \forall\text{ admitted target chains of length }n,\ \exists\text{ an owned enabling continuation}. \tag{RC}
An enabling continuation for a chain is an owned, physically admitted continuation in which the last description of the chain becomes a represented target, criticism can be directed at it, and the result can affect its operative use.
````

  - Quotations: “an owned enabling continuation” — found at L492.
- **Goes to a checker** (rule 5): challenged by GLM and Mimo. Lines at stake: L492.

#### D16.3 · definition · Enable

Lines it formalizes or quotes (from the brief): L495.

- **Mimo** (reply line 43; does not challenge): L495's definition of Enable otherwise matches.
  - Quotations: “that would need a part every member of the population is built without” — found at L481.
- **GLM:** no point on this item.
- **External reader and case card:** E17 (the external reader) challenges the sentence this item formalizes (section 3 below).
- **Goes to a checker** (rule 5): challenged by E17 (the external reader). Lines at stake: L495.

#### D16.4 · definition · Universality

Lines it formalizes or quotes (from the brief): L497, L500, L503, L506.

- **Mimo** (reply lines 33–39; challenges): As for D16.5 (i): (U3)'s typing against L528's classes (proposal printed under D16.5); on L497, I75's "Θ admits a carrier instantiating c" is what "that some carrier can hold under the physical module" says, and the added Acc clause is settled only if "explanatory content" is defined earlier as an account (no line here does).
  - Proposal `M16-B5` (reply lines 35–37), would change L528:

````
> L528 | **Membership.** The base class: interpretations supplying these data with typing as declared, meeting physical realization wherever a physical attribution is made. The creative-episode class: base interpretations with an instance of (G) connected to a critical episode. The explanation-creation class: an instance of (EX). The recursive class: (RC). The universal class: base interpretations \(M\) for which some \((s,\xi_0,\Omega,\beta)\) is in (U3).
````

  - Quotations: “the universal class” — found at L528; “… an instance of (G) connected to a critical episode.” — found at L528; “in a critical episode” — not found in the text; found in the brief; “that some carrier can hold under the physical module” — found at L497; “Θ admits a carrier instantiating c” — not found in the text; found in the brief; “explanatory content” — found at L497.
- **GLM** (reply line 22; challenges **OWNER QUESTION**): 𝔓^adv_Θ is not defined beyond its name (NF12), so (U2) and UECS are open until "the coherently posed advanceable challenges" (L497) is defined; the words should define it or say that (U3) is conditional on it; no wording, "it is the owner's question".
  - Quotations: “not defined beyond its name” — not found in the text; found in the brief; “the coherently posed advanceable challenges” — found at L497.
- **Goes to a checker** (rule 5): challenged by GLM and Mimo. Lines at stake: L528.
- Marks: OWNER QUESTION points present.

#### D16.5 · definition · Classes

Lines it formalizes or quotes (from the brief): L528.

- **Mimo** (reply lines 33–39; challenges): (i) L528's classes are classes of interpretations while (U3) is a set of tuples, so "the universal class" is typed differently; the words at L528 stand and the pointer should match; proposes a new L528; (ii) D16.5 writes "in a critical episode" for L528's "connected to a critical episode", narrower (the maths follows); (iii) L528 names "(EX)", D16.5 CreateEx, a naming slip.
  - Proposal `M16-B5` (reply lines 35–37; printed in full under D16.4 above), would change L528.
  - Quotations: “the universal class” — found at L528; “… an instance of (G) connected to a critical episode.” — found at L528; “in a critical episode” — not found in the text; found in the brief; “that some carrier can hold under the physical module” — found at L497; “Θ admits a carrier instantiating c” — not found in the text; found in the brief; “explanatory content” — found at L497.
- **GLM** (reply line 24; does not challenge): Matches, including that no axiom places a system in a class.
- **Goes to a checker** (rule 5): challenged by Mimo. Lines at stake: L528.

#### FC91 · claim · (CT1) is C ⊆ F(C) only with (CT1)'s completion read into F

Lines it formalizes or quotes (from the brief): L466, L471.

- **Mimo** (reply line 47; does not challenge): FC91's witness shows the reading without the output condition is strictly weaker, an argument for the fix in (e), not against the text once the fix is in.
- **Mimo** (reply line 71; challenges): Hand model: without I61's restriction of F to the task's inputs, RetReal holds and C ⊄ F(C) (an execution on an input outside dom T fails); the claim rests on F read over the task's inputs, which the (e) wording carries.
  - Proposal `M16-B7` (reply lines 83–85), would change L471:

````
> L471 | **Retention fixed point.** \(F(C)\) = states whose executions on the task's inputs all complete as in (CT1) and return into \(C\). \(F\) is monotone; \(C\subseteq F(C)\) is the invariant form; the greatest fixed point is the union of the sets \(D\) with \(D\subseteq F(D)\). (CT2)
````

- **GLM** (reply line 30; challenges): The witness is not against the text; it tells only against I61's alternative (a) and confirms matter 10 (the invariant form is (CT1) only if "complete" carries the output condition); wording under matter 10.
  - Proposal `G16-B5` (reply lines 81–84), would change L471:

````
L471 (replaces current line)
**Retention fixed point.** \(F(C)\) = states whose executions all complete with \(o\in T[i]\) and return into \(C\). \(F\) is monotone; \(C\subseteq F(C)\) is the invariant form; the greatest fixed point is the union of the sets \(D\) with \(D\subseteq F(D)\). (CT2)
````

- **GLM** (reply line 66; does not challenge): Definitional under I61; holds by construction; L469 forecloses the deadlock residue.
- **Goes to a checker** (rule 5): challenged by GLM and Mimo. Lines at stake: L471.

#### FC92 · claim · (CT2): monotone F and its greatest fixed point

Lines it formalizes or quotes (from the brief): L471, L546.

- **Mimo** (reply line 73; challenges): Monotonicity and the greatest fixed point survive every reading; but "the greatest fixed point is the states that can retain" fails where Exec can be empty (hand model: a state with no executions lies in gfp(F), against L469's "deadlock is not a vacuous performance of the task"); rests on I61's scoping; removed by the L469 wording; FC92 (c) rests on lines not given.
  - Proposal `M16-B6` (reply lines 53–55), would change L469:

````
> L469 | Execution families are nonempty on admitted inputs and at every constructor state; a deadlocked execution is an execution that does not complete, and is not a performance of the task.
````

  - Quotations: “deadlock is not a vacuous performance of the task” — found at L469; “complete” — found at L223, L409, L429, L466 and 3 more lines; “the greatest fixed point is the states that can retain” — not found in the text; not in the brief; “the \(D\) is not a question's target” — not found in the text; not in the brief.
- **GLM** (reply line 68; does not challenge): Holds by construction under either reading (Knaster–Tarski); should be reclassified; the round-1 wording at L471 is right.
  - Quotations: “holds on all models tried” — not found in the text; found in the brief.
- **Goes to a checker** (rule 5): challenged by Mimo. Lines at stake: L469.

#### FC93 · claim · (CT3), (CT4), and capability at one tolerance

Lines it formalizes or quotes (from the brief): L479.

- **Mimo** (reply line 47; does not challenge): FC93 (c)'s witness is L479's last sentence as it stands; nothing needs a change.
- **Mimo** (reply line 75; does not challenge): (a), (b) hold at any size; L479's last sentence must be read as a non-implication, which the text allows and the maths took; no change.
  - Quotations: “Capability at a given tolerance does not imply possibility at every tolerance.” — found at L479.
- **GLM** (reply line 32; does not challenge): The witness is the text's own last sentence of L479; no change.
  - Quotations: “Capability at a given tolerance does not imply possibility at every tolerance” — found at L479.
- **GLM** (reply line 70; challenges): Under I62, (CT3) and (CT4) are analytic; without I62's clause (choice (a)) both fail trivially (an Admit family omitting one owned-realized task); the holding rests wholly on I62.
  - Proposal `G16-B2` (reply lines 39–42; printed in full under D15.7 above), would change L479.
- **Goes to a checker** (rule 5): challenged by GLM. Lines at stake: L479.

#### FC94 · claim · Recursion does not entail universality

Lines it formalizes or quotes (from the brief): L509.

- **Mimo** (reply line 41; challenges): The formal statement carries clauses one and three of L509 only; "a historical extension" is not defined in L485–L511 and no NF entry records the gap; clause three ("does not suffice for it") is written in both directions; the maths' (b) should read "no finite set of performed tasks establishes UU".
  - Quotations: “Recursion does not entail universality; a historical extension leaves it open; a finite performance record does not suffice for it.” — found at L509; “A historical extension” — found at L509; “does not suffice for it” — found at L509; “no finite set of performed tasks decides UU” — not found in the text; found in the brief; “no finite set of performed tasks establishes UU” — not found in the text; not in the brief.
- **GLM** (reply line 72; challenges): Hand model for (a): RC holds and UU fails with free predicates set by hand (I74, I75), confirming L509's first clause and nothing more; (b) holds only if 𝔈_Θ is infinite, which the text does not fix.
- **Goes to a checker** (rule 5): challenged by GLM and Mimo. Lines at stake: L509.

#### FC110 · claim · The classes are defined; no membership is asserted

Lines it formalizes or quotes (from the brief): L27, L528.

- **Mimo:** no point on this item.
- **GLM** (reply line 74; does not challenge): Syntactic; matches L27 and L528.
- **Goes to no checker**: no point challenges it and it is not one of the twelve; recorded under rule 7 below.

#### I61 · invention · Tasks and executions; 'complete' in F read as (CT1)'s completion

Lines it formalizes or quotes (from the brief): L461, L469, L471.

- **Mimo** (reply lines 51–57; challenges): Partly settled: (CT1) fixes what an execution reports and L469 fixes nonemptiness "on admitted inputs"; not settled: whether "complete" carries the output condition (matter 10), the scope of nonemptiness, whether Exec may hold non-completing executions, resources and side effects as components; proposes a new L469 (writes I61's two choices in).
  - Proposal `M16-B6` (reply lines 53–55; printed in full under FC92 above), would change L469.
  - Quotations: “on admitted inputs” — found at L469; “complete” — found at L223, L409, L429, L466 and 3 more lines.
- **GLM** (reply line 36; challenges): Nonemptiness is settled by L469 ("Execution families are nonempty on admitted inputs; deadlock is not a vacuous performance of the task"), which the maths should cite; whether "complete" in F carries the output condition is not settled (matter 10 wording); the remaining choice is then inert.
  - Proposal `G16-B5` (reply lines 81–84; printed in full under FC91 above), would change L471.
  - Quotations: “Execution families are nonempty on admitted inputs; deadlock is not a vacuous performance of the task.” — found at L469.
- **Goes to a checker** (rule 5): challenged by GLM and Mimo. Lines at stake: L469, L471.

#### I62 · invention · Tolerances: stricter tolerances admit fewer tasks; Admit contains every realized task

Lines it formalizes or quotes (from the brief): L479.

- **Mimo** (reply line 59; challenges): Not settled: "physically achievable" is never said to mean having a realization; that step is I62's and makes (CT3) follow; the L479 proposal writes it in.
  - Proposal `M16-B3` (reply lines 19–21; printed in full under D15.7 above), would change L479.
  - Quotations: “physically achievable” — found at L479.
- **GLM** (reply lines 38–43; challenges **OWNER QUESTION**): "q′ excludes at least what q excludes" is settled by L479, and Admit's antitonicity follows; "a task with a realization, owned or not, is in Admit" is not settled and makes (CT3) analytic; "If the owner wants (CT3) as a claim and not a definition", proposes inserting a clause in L479 (writes I62 in); if (CT3) is meant as an assumption, leave the line and mark I62's clause as invented.
  - Proposal `G16-B2` (reply lines 39–42; printed in full under D15.7 above), would change L479.
  - Quotations: “q′ excludes at least what q excludes” — not found in the text; found in the brief; “q′ admits no performance q excludes” — found at L479; “A task with a realization, owned or not, is in Admit” — not found in the text; not in the brief; “physically achievable” — found at L479.
- **Goes to a checker** (rule 5): challenged by GLM and Mimo. Lines at stake: L479.
- Marks: OWNER QUESTION points present.

#### I74 · invention · Recursive capacity: target chains and enabling continuations

Lines it formalizes or quotes (from the brief): L492.

- **Mimo** (reply line 61; challenges): Not settled: "admitted target chains" is not defined in the lines given and "enabling continuation" is ambiguous; I74 quotes L487 as "can change its operative use" where the text says "affect", and the text's word stands; the L492 proposal writes I74's reading in.
  - Proposal `M16-B4` (reply lines 27–29; printed in full under D16.2 above), would change L492.
  - Quotations: “admitted target chains” — found at L492; “enabling continuation” — found at L492; “can change its operative use” — not found in the text; found in the brief; “affect” — found at L487.
- **GLM** (reply lines 45–51; challenges): Not settled; I74's reading should be the words'; proposes a sentence after L492's display defining an enabling continuation in L487's own words (writes I74 in).
  - Proposal `G16-B3` (reply lines 46–50; printed in full under D16.2 above), would change L492.
  - Quotations: “enabling continuation” — found at L492; “active route” — found at L299, L307, L375, L385 and 4 more lines.
- **Goes to a checker** (rule 5): challenged by GLM and Mimo. Lines at stake: L492.

#### I75 · invention · The explanatory contents 𝔈_Θ

Lines it formalizes or quotes (from the brief): L497.

- **Mimo** (reply line 63; challenges): Partly settled: "some carrier can hold" is the "admits a carrier" reading; whether 𝔈_Θ is infinite is not settled; FC94 (b) needs it; it should stay open in the text and be carried by the maths as a stated assumption.
  - Quotations: “some carrier can hold” — found at L497; “admits a carrier” — not found in the text; found in the brief; “holds at present” — not found in the text; found in the brief.
- **GLM** (reply lines 53–58; challenges): The membership reading is settled by L497's "can hold"; the infinitude of 𝔈_Θ is not, and FC94 (b) leans on it (with k contents, a record of k tasks would decide UU); gives a clause for L497 writing I75's infinitude in, but prefers to keep the line and mark FC94 (b) as resting on an unsettled assumption (the cardinality of 𝔈_Θ is a question about Θ).
  - Proposal `G16-B4` (reply lines 54–57), would change L497 — the reader's alternative, which it does not prefer:

````
L497 (replaces current line; adds one clause)
With \(\mathfrak E_\Theta\) the explanatory contents that some carrier can hold under the physical module, taken without any fixed finite bound, …
````

  - Quotations: “the explanatory contents that some carrier *can* hold” — found at L497; “taken to be infinite where FC94 needs it” — not found in the text; found in the brief.
- **Goes to a checker** (rule 5): challenged by GLM and Mimo. Lines at stake: L497.

#### I97 · invention · Tasks and executions on finite state sets

Lines it formalizes or quotes (from the brief): L466.

- **Mimo** (reply line 65; does not challenge): A search bound, not content.
- **GLM** (reply line 60; does not challenge): Program bounds; stay open.
- **Goes to no checker**: no point challenges it and it is not one of the twelve; recorded under rule 7 below.

#### I98 · invention · Tolerances as a 3 × 3 grid of performance and retention

Lines it formalizes or quotes (from the brief): L479.

- **Mimo** (reply line 65; does not challenge): A search bound, not content; its direction is consistent with L479's order.
- **GLM** (reply line 60; does not challenge): Program bounds; stay open.
- **Goes to no checker**: no point challenges it and it is not one of the twelve; recorded under rule 7 below.

#### H16 · H-entry · "can affect its operative use" read as "on an active route" (D16.1)

Lines it formalizes or quotes (from the brief): L487.

- **Mimo** (reply line 67; challenges): Not settled; the words "can affect" stand and the maths must not strengthen them to an active route; stays open.
  - Quotations: “can affect” — found at L487.
- **GLM** (reply line 62; challenges **OWNER QUESTION**): The words do not settle "on an active route" (not in the sentence, and not found defined in this part's lines); D16.1 and I74 disagree, a fault of the maths; D16.1 should read L487's own "can affect d's operative use", "unless the owner means the route machinery, in which case the text, not the definition, must say so".
  - Quotations: “on an active route” — found at L385, L409; “and the result can affect d's operative use” — not found in the text; not in the brief.
- **Goes to a checker** (rule 5): challenged by GLM and Mimo. Lines at stake: L487.
- Marks: OWNER QUESTION points present.

#### NF11 · NF entry

Lines it formalizes or quotes (from the brief): L495.

- **Mimo** (reply line 31; challenges): One further unanchored phrase, recorded nowhere: L495's "in the sense of (CT1)" — (CT1) defines no enabling conditions, taking χ as a parameter; the maths echoes the phrase and marks only "non-question-begging" (NF11).
  - Quotations: “… in the sense of (CT1).” — found at L495; “non-question-begging” — found at L495.
- **GLM:** no point on this item.
- **External reader and case card:** E17 (the external reader) challenges the sentence this item formalizes (section 3 below).
- **Goes to a checker** (rule 5): challenged by Mimo; challenged by E17 (the external reader). Lines at stake: L495.

#### L471 · round-1 change · the round-1 change at L471

Lines it formalizes or quotes (from the brief): L471.

- **Mimo** (reply lines 81–85; challenges): No further change to the round-1 clause (the union of the sets D with D ⊆ F(D) binds D); but the same sentence carries matter 10 and the domain gap of (d); proposes a new L471.
  - Proposal `M16-B7` (reply lines 83–85; printed in full under FC91 above), would change L471.
  - Quotations: “the greatest fixed point is the union of the sets \(D\) with \(D\subseteq F(D)\)” — found at L471.
- **GLM** (reply line 78; does not challenge): The new wording is right and disturbed nothing; no further change beyond matter 10's.
- **Goes to a checker** (rule 5): challenged by Mimo. Lines at stake: L471.

#### matter 10 · round-1 matter · "complete" in L471's first sentence must be read as (CT1)'s "completes with o∈T[i]" for clause 2 of (CT2) to be (CT1).

Lines it formalizes or quotes (from the brief): L471.

- **Mimo** (reply line 87; challenges): Change needed; the L471 proposal writes I61's reading of "complete" in.
  - Proposal `M16-B7` (reply lines 83–85; printed in full under FC91 above), would change L471.
  - Quotations: “complete” — found at L223, L409, L429, L466 and 3 more lines.
- **GLM** (reply lines 80–84; challenges): The text needs the change: "complete" admits the weaker reading and the invariant form is then weaker than (CT1) (FC91's witness); proposes a new L471 ("complete with o ∈ T[i]").
  - Proposal `G16-B5` (reply lines 81–84; printed in full under FC91 above), would change L471.
- **Goes to a checker** (rule 5): challenged by GLM and Mimo. Lines at stake: L471.

#### matter 14 · round-1 matter · L27 gives no pointer to Part XIV where L23 and L25 give theirs.

Lines it formalizes or quotes (from the brief): L23, L25, L27.

- **Mimo** (reply lines 89–95; challenges): Change needed (relying on FC110's quotation of L27): proposes adding "(Part XIV)" to L27, as L23 and L25 give their pointers.
  - Proposal `M16-B8` (reply lines 91–93), would change L27:

````
> L27 | It does not decide whether any human, machine, institution or lineage belongs to the classes defined. It defines the classes (Part XIV).
````

- **GLM** (reply lines 86–90; challenges): The text needs the pointer on the pattern of L23 and L25 (relied on as described); proposes a new L27 adding "physical attributions in them are read through the physical module (Part XIV)".
  - Proposal `G16-B6` (reply lines 87–90), would change L27:

````
L27 (replaces current line)
It does not decide whether any human, machine, institution or lineage belongs to the classes defined. It defines the classes; physical attributions in them are read through the physical module (Part XIV).
````

- **Goes to a checker** (rule 5): challenged by GLM and Mimo. Lines at stake: L27.

#### Part 16: items no point addresses

Items of this part on which neither reader made any point (both replies read whole): NF12, NF16, NF17. Each is recorded under rule 7 in section 6 unless a point on it in another part sends it to a checker.

### Part 17: The Arguments of Part XVI, and what would rule the class out

Brief: `tests/S104 Round 2 - the maths against the words - part 17, The Arguments of Part XVI, and what would rule the class out.md`. Replies: `s104_maths_mimo_17.response.txt` (Mimo), `s104_maths_glm_17.response.txt` (GLM).

H20 ("Smaller unregistered choices") names five definitions of other parts (D3.4, D13.6, D10.3, D15.5, D16.5); the readers took them one by one, and their points are tabulated under those ids, which are added to this part's items for that purpose. H20 itself is recorded as a context item (section 5 of this file).

#### D18.1 · definition · The dependence graph

Lines it formalizes or quotes (from the brief): L526.

- **Mimo** (reply lines 5–11; challenges): L526 says the order has no cycle; the definitions have one if "represented" in L405's "prepares a represented organization" is read through (R): Build asks for (R), (R) for Sel or Con, Con for the construction trace Build's subhistory is; the maths closes it by making Prepares a primitive (I56), which hides the loop; the K2 loop is closed below the step; the words stand (L526's own warning names the fault); proposes new wording at L526 reading the trace as stated data (writes I56's second reading in; the reader has only fragments of L526).
  - Proposal `M17-B1` (reply lines 7–9), would change L526:

````
L526 | **Dependence order.** (O) and (Q) depend on nothing; nor do the declared indices and the declared inputs, which are stated, not defined. A construction trace is stated data: Build, Con and Rep take it as an input and not through (R); a representation defined only by its own construction has not supplied its place in the order.
````

- **GLM:** no point on this item.
- **External reader and case card:** E03 (the external reader) challenges the sentence this item formalizes (section 3 below).
- **Goes to a checker** (rule 5): challenged by Mimo; challenged by E03 (the external reader). Lines at stake: L526.

#### D18.2 · definition · Structure-preserving bijections

Lines it formalizes or quotes (from the brief): L612.

- **Mimo** (reply line 13; does not challenge): "Structure-preserving bijections" is nowhere defined in the words; I70 must supply it; the exclusion sentence is the words' own and matches I45's event (see FC100).
- **GLM:** no point on this item.
- **Goes to no checker**: no point challenges it and it is not one of the twelve; recorded under rule 7 below.

#### E8 · encoding · A contract as an organization

Lines it formalizes or quotes (from the brief): L588, L590.

- **Mimo:** no point on this item.
- **GLM:** no point on this item.
- **External reader and case card:** E20 (the external reader) challenges the sentence this item formalizes (section 3 below).
- **Goes to a checker** (rule 5): challenged by E20 (the external reader). Lines at stake: L590.

#### E9 · encoding · The two-layer episode

Lines it formalizes or quotes (from the brief): L620, L622, L624, L626, L628, L630.

- **Mimo:** no point on this item.
- **GLM:** no point on this item.
- **External reader and case card:** E10 (the external reader) challenges the sentence this item formalizes (section 3 below).
- **Goes to a checker** (rule 5): challenged by E10 (the external reader). Lines at stake: L622, L626.

#### FC97 · claim · Argument 5: a contract can be an organization and a content

Lines it formalizes or quotes (from the brief): L588, L590.

- **Mimo** (reply lines 15–21; challenges): L590 makes the ports "the edits and their boundaries" and the components "the closure conditions", yet lets an admitted edit "alter 𝒬", and C must contain x0; I67 places 𝒬 in a port and the baseline in a component, without which "alter 𝒬" is no edit of the organization and nothing forces x0 into C; the words should change; proposes a new L590 (writes I67's query port and baseline component in); "the closure conditions" rules out I67's option (b); L588's second half is untested.
  - Proposal `M17-B2` (reply lines 17–19), would change L590:

````
L590 | Give it ports (the edits and their boundaries; and \(\mathcal Q\), which the admitted edits can alter), components (the baseline membership of \(x_0\) and the closure conditions, each with the relation it imposes on its ports, as (O) requires), and admitted edits (add or remove a change; alter \(\mathcal Q\)).
````

- **Mimo** (reply line 95; challenges): Beyond the bounds: with edits ℤ under addition, closure relates the memberships of every triple at once, one relation over infinitely many ports; if (O) gives each component a fixed footprint, the contract is not an organization (rests on (O)'s footprints and I77); L588's "can be the content c in (G)" is untyped by the search.
- **GLM** (reply line 5; challenges): The formal covers the first conjunct and only asserts the second; the headline "holds on all models tried" covers half the sentence and should say so; the words should stand.
  - Quotations: “HOLDS ON ALL MODELS TRIED” — not found in the text; found in the brief; “ports (the edits and their boundaries)” — found at L590.
- **GLM** (reply line 78; challenges): Attack on the untested conjunct: under a strict I55 (Deploy's binding of the content's ports to the activity's), nothing guarantees an activity matching a query-valued port, so "can be the content c in (G)" fails for want of a binding; under a permissive one it holds trivially; unearned; mark or test.
  - Quotations: “integrated into problem-directed activity” — found at L403; “can be the content c in (G)” — found at L588.
- **External reader and case card:** E20 (the external reader) challenges the sentence this item formalizes (section 3 below).
- **Goes to a checker** (rule 5): challenged by GLM and Mimo; challenged by E20 (the external reader). Lines at stake: L590.

#### FC98 · claim · Argument 6 and the dependence order: acyclic, and ending where the text says

Lines it formalizes or quotes (from the brief): L526, L596.

- **Mimo** (reply lines 23–29; challenges): L596 claims every predicate of Parts II–XIII rests on Θ, 𝒩, (O), (Q), declared indices and inputs; the formal core needs δ, ⊥, Excl(Σ), restriction, Offered, Allow_χ, Applies, MadeFrom, K, Rule/Rec/Chg, Integrated, Nontrivial, Prepares, BindingConstruction, TransferComposite, Aims*, O_ex's marking, Occurs and Attempt, none on that list; the words stand as a requirement, so the text must carry the terms; proposes a new L596 claim (writes I20, I21, I27, I29, I33, I34, I39, I46, I47, I55, I56, I58, I59 and Attempt into the frame; L522's listing must follow).
  - Proposal `M17-B3` (reply lines 25–27), would change L596:

````
L596 | **Claim.** Every predicate in Parts II–XIII is defined in terms of \(\Theta\) (including \(\operatorname{Org}_\ell\)) and, where invoked, \(\mathcal N\), together with the structural vocabulary of (O) and (Q), declared indices and declared inputs; a term named but not defined is a primitive of the frame and is listed with the declared inputs at L522.
````

- **GLM** (reply lines 7–17; challenges **OWNER QUESTION**): Two partings: the graph is acyclic only because I56 makes Prepares a primitive (read through (R), L405's "prepares a represented organization" reopens the loop L526 names); and the sink test asks of fourteen symbols whether each is read through Θ or an unlisted primitive, which the text leaves open; FC98 records that L596 does not yet hold of the formal core; the words should stand and the text close both gaps; proposes a sentence after L526 and a sentence after L596 (answering the open question one way; "the owner may instead define some of them").
  - Proposal `G17-B1` (reply lines 10–12), would change L526:

````
A construction trace is a sequence of occurrences and is not itself read through (R); a represented organization enters a construction only through a representation separately given.
````

  - Proposal `G17-B2` (reply lines 14–16), would change L596:

````
The predicates this leaves stated and not defined — among them the offer of one candidate in place of another, the restriction of a candidate, integration into problem-directed activity, preparation, construction from a content, the contrasts of an active route, the uses of a reason, occurrence, and the designation of a query — are primitives of the semantics, stated as the indices are stated, not defined.
````

  - Quotations: “prepares a represented organization” — found at L405; “a claim read through Θ, or a primitive the text does not list” — not found in the text; found in the brief.
- **External reader and case card:** E03 (the external reader) challenges the sentence this item formalizes (section 3 below).
- **Goes to a checker** (rule 5): challenged by GLM and Mimo; challenged by E03 (the external reader). Lines at stake: L526, L596.
- Marks: OWNER QUESTION points present.

#### FC99 · claim · Argument 7: an account on C can fail on C'

Lines it formalizes or quotes (from the brief): L606.

- **Mimo** (reply line 31; challenges): The formal writes Acc where the fragment writes meeting (E); if Acc is acceptance with (E) as one clause, the formal asserts more; the words stand; the formal should write meeting (E) and hold the rest fixed across C and C′.
- **Mimo** (reply line 97; does not challenge): The witness is close to trivial; the one risk is the Acc/(E) mismatch.
- **GLM** (reply line 19; does not challenge): Says what the sentence says, with Acc read as meeting (E); no parting.
- **GLM** (reply line 90; does not challenge): No attack found; the construction is generic.
- **Goes to a checker** (rule 5): challenged by Mimo. Lines at stake: L606.

#### FC100 · claim · Argument 8: structure-preserving bijections keep (E), (G), (P), (EX)

Lines it formalizes or quotes (from the brief): L612.

- **Mimo** (reply lines 33–39; challenges): I70 transports ports, values, components, edits, boundaries, occurrences, the query, its designation and declared inputs, and keeps Θ's interpretation; the sentence's "carriers" is not placed by I70, and (G), (EX) need the physical module; the words should say it; proposes a new L612 (writes I70's carrying of the physical module in); (G), (P), (EX) are untested.
  - Proposal `M17-B4` (reply lines 35–37), would change L612:

````
L612 | Transporting all carriers (the physical module's interpretation among them), relations, transports, histories, contracts and declared inputs along structure-preserving bijections preserves (E), (G), (P), (EX).
````

- **Mimo** (reply line 99; challenges): Two attacks: (1) two organizations differing only in the grain label (I28) give different verdicts of (E), and I70 does not carry the label, so the identity bijection flips (E); (2) (P) reads a contract's provenance through a population, which the transported list does not name; both fixes are additions to I70, not to the words.
- **GLM** (reply line 21; does not challenge): Only (E) was searched; "all carriers" settles I70's question; with everything carried, preservation is by construction; no wording change; the untested three stay marked.
  - Quotations: “all carriers” — found at L612.
- **GLM** (reply line 80; does not challenge): Attacking (G) with swapped carrier names: if the physical module is not carried (I70 (a)) (G) fails; L612's "all carriers" excludes (a), so the attack fails against the sentence; the searched (E) is the easy quarter.
  - Quotations: “all carriers” — found at L612.
- **Goes to a checker** (rule 5): challenged by Mimo. Lines at stake: L612.

#### FC101 · claim · Argument 9: an input–output description does not fix an account

Lines it formalizes or quotes (from the brief): L616.

- **Mimo** (reply line 41; challenges): Two mismatches: the formal (b) constructs "a candidate that meets (E) for one and not the other" while the words say the two "differ on an account claim" (words stand; the formal should name the differing claim); and "edits deleting internal components" were encoded as knock-outs (H18), which L103 settles against; the result stands only after hand reasoning.
- **Mimo** (reply line 101; challenges): Under L103's full relation, deleting both routes leaves the output relation full; if (E) is existential over C's pairs, the candidate meets (E) for M1 as well and the models do not differ on an account claim; open on the quantifier of (E), not before the reader.
- **GLM** (reply line 23; does not challenge): (a) is a fact about functions, the sentence's point; (b) under L103's full-relation deletion comes out the same (H18); no parting beyond H18's registration.
  - Quotations: “holds by construction” — not found in the text; found in the brief; “deleting” — not found in the text; found in the brief.
- **GLM** (reply line 86; does not challenge): With L103's full relation the outcome stands; the instance clause needs the routes to agree on every input; the text's instance is the agreeing case.
- **Goes to a checker** (rule 5): challenged by Mimo. Lines at stake: L616.

#### FC102 · claim · Argument 10: surprise, the structural failure of selection, and the constructed layer

Lines it formalizes or quotes (from the brief): L624, L626.

- **Mimo** (reply lines 43–49; challenges): The formal's (b) second half has no counterpart in the words and does not hold in the encoding; the words' claim carries an unstated bound: "can only predict from occupancy" admits a predictor over the whole occupancy history, which reads the velocity before the hidden run; proposes a new L626 (writes I68's window bound, I100's run occlusion and the two-frame threshold in); L624's "the thing re-emerges" presupposes one track.
  - Proposal `M17-B5` (reply lines 45–47), would change L626:

````
L626 | If the population's transports can only predict from a bounded window of recent occupancy, and the hidden run leaves that window holding fewer than two frames in which a thing is visible, no member survives the extended history: the fidelity failure is structural, not parametric.
````

- **Mimo** (reply line 57; challenges): (1) The counterexample to the formal's second half is against the invention: the threshold is w = L + 2, not "w at least as long as the occlusion"; written into the L626 proposal; (2) the two-thing finding touches the text's episode: with two things and occupancy-only readings, crossing and standing give equal readings, so a window predictor fails with no occlusion, and L624's "the thing re-emerges at a cell consistent with its velocity" names no determined thing; this does not contradict L626 but the stated diagnosis is not the only failure; the L620 proposal records the geometry.
  - Proposal `M17-B5` (reply lines 45–47; printed in full under FC102 above), would change L626.
  - Proposal `M17-B7` (reply lines 77–79), would change L620:

````
L620 | Stipulate an object layer \(P\): a line of cells; two things, each with a position and a velocity, which may occupy one cell and pass through one another without interacting; continuity components; admitted edits: displace a thing, set its velocity, occlude a cell or a run of cells, swap the two identities.
````

- **GLM** (reply line 25; challenges): The formal adds a second half the text does not state, and that half is what failed; L626's own claim computed as claimed; the words should stand and the formal be corrected (for one thing the boundary is w ≥ L + 2; with two things and occupancy without identity no window makes the failure parametric); (a) and (c) untested, (a) carried by hand in (d).
  - Quotations: “if w is at least that long, an occupancy predictor can extrapolate and the failure is not structural” — not found in the text; found in the brief.
- **GLM** (reply lines 35–39; challenges **OWNER QUESTION**): FC102 (b) second half is a counterexample to the claim's own wording, resting on I68 and I100; against the text only in that L626 does not say what the failure turns on (for one thing, the window; for two, occupancy carrying no identity); no change required; "If the owner wants the boundary in the words", proposes a new clause of L626 (writes I68/I100's finding in).
  - Proposal `G17-B3` (reply lines 36–38), would change L626:

````
If the population's transports can only predict from occupancy, no member survives the extended history: the fidelity failure is structural, not parametric — with one thing it turns on the window being too short to carry position and velocity both; with two, on occupancy carrying no identity, which no window cures.
````

  - Quotations: “structural, not parametric” — found at L626.
- **GLM** (reply line 84; challenges): (a) by hand: during the occlusion every window predictor's output is constant; faithfulness on H0 forces it to miss some cell, so at re-emergence it is violated at a pair of C0 ∖ H0; this uses faithfulness on H0, which H17's crossings would destroy; the H17 changes make it go for two things.
  - Proposal `G17-B6` (reply lines 57–59), would change L620:

````
Stipulate an object layer \(P\): a line of cells, with a stated rule at each end; two things, each with a position and a velocity, that do not act on one another and may share a cell; continuity components; admitted edits: displace a thing, set its velocity, occlude a cell or a run of cells, swap the two identities.
````

  - Proposal `G17-B7` (reply lines 63–65), would change L622:

````
\(H_0\) is a history in which the two things never share a cell.
````

  - Quotations: “every cell” — not found in the text; not in the brief.
- **External reader and case card:** E10 (the external reader) challenges the sentence this item formalizes (section 3 below).
- **Goes to a checker** (rule 5): challenged by GLM and Mimo; one of the twelve counterexamples the second check reproduced (FC102 (b), second half); challenged by E10 (the external reader). Lines at stake: L620, L622, L624, L626.
- Marks: OWNER QUESTION points present.

#### FC103 · claim · Argument 10: the swap, two pairings, one account

Lines it formalizes or quotes (from the brief): L630.

- **Mimo** (reply line 51; challenges): The formal (a) says t1 ∘ ψ meets (F1), (F2) and (A) exactly when t1 does; the words claim only the composition and that no admitted change separates the pairings; if (A) carries a designation naming thing 1 (I20), t1 ∘ ψ fails (A); the words stand; the formal should drop (A) or require ψ to preserve the designation; "built alike" is defined nowhere (I69).
- **Mimo** (reply line 103; challenges): Hand model: with a designation naming thing 1, t1 ∘ ψ fails (A) while t1 meets it; the words' conclusion is untouched; fix: ψ preserves the designation, or drop (A) from (a).
- **GLM** (reply line 27; challenges): Faithful with one gap: I69's "maps C onto C" is stronger than the premise "admits each edit for both things alike" (proposal under I69).
  - Proposal `G17-B4` (reply lines 46–48), would change L630:

````
The two things are built alike in \(P\), and their persistence components alike in \(S_1\): the exchange of the two things carries the ports, edits and boundaries of the one onto the other, carries the contract onto itself and leaves the query's answers unchanged, and the same holds in \(S_1\) for the exchange of the persistence components.
````

  - Quotations: “maps C onto C” — not found in the text; found in the brief; “admits each edit for both things alike” — found at L630.
- **GLM** (reply line 82; challenges): Hand attack with an asymmetric contract (an edit naming both things whose exchanged image is not in C): ψ does not carry C onto itself, t1 ∘ ψ is no transport on C, and (a) fails while the premise holds; the I69 wording cures it; (d) rests on occupancy without identity, which L622 bears out.
  - Proposal `G17-B4` (reply lines 46–48; printed in full under FC103 above), would change L630.
  - Quotations: “move thing 1 to the cell of thing 2” — not found in the text; not in the brief; “move thing 2 to the cell of thing 1” — not found in the text; not in the brief; “predicts occupancy” — found at L622.
- **Goes to a checker** (rule 5): challenged by GLM and Mimo. Lines at stake: L630.

#### FC109 · claim · 'A mathematical error': the named claims, each under its stated assumptions

Lines it formalizes or quotes (from the brief): L546.

- **Mimo** (reply line 53; does not challenge): The formal matches the words; where an assumption is stated only in vague words (NC1's "unanalysed", "at the declared grain"), the class of errors cannot be read off the text, a reason to sharpen those assumptions, not to widen L546.
- **Mimo** (reply line 105; does not challenge): No model (the named sentences are not before the reader); the assumptions are stated in words whose formal reading is an invention, so a counterexample under one reading is, by L546's "under their stated assumptions", no mathematical error; the sharpening belongs at the assumptions.
- **GLM** (reply line 29; does not challenge): Matches; its protection is conditional on the inventions of the named claims, settled in other parts.
- **GLM** (reply line 88; does not challenge): Nothing new within this part.
- **Goes to no checker**: no point challenges it and it is not one of the twelve; recorded under rule 7 below.

#### I67 · invention · A contract as an organization (Argument 5), encoded

Lines it formalizes or quotes (from the brief): L590.

- **Mimo** (reply line 61; challenges **OWNER QUESTION**): The words settle the ports and the components as the closure conditions, not where 𝒬 lives or where x0's baseline membership is imposed; the L590 proposal writes both in; option (b) is ruled out by the words; I67's value set for the membership and query ports is left open, "that placement being the owner's question".
  - Proposal `M17-B2` (reply lines 17–19; printed in full under FC97 above), would change L590.
- **GLM** (reply line 5; challenges): One invention choice is settled by the text: L590's "ports (the edits and their boundaries)" makes boundaries ports, excluding I67's other choice (a).
  - Quotations: “HOLDS ON ALL MODELS TRIED” — not found in the text; found in the brief; “ports (the edits and their boundaries)” — found at L590.
- **GLM** (reply line 43; challenges): The text settles the shape (ports "the edits and their boundaries"; closure conditions with the question; "alter Q" makes the query ported); the boolean membership encoding may stay open; no wording.
  - Quotations: “the edits and their boundaries” — found at L590; “alter Q” — found at L590; “add or remove a change” — found at L590.
- **External reader and case card:** E20 (the external reader) challenges the sentence this item formalizes (section 3 below).
- **Goes to a checker** (rule 5): challenged by GLM and Mimo; challenged by E20 (the external reader). Lines at stake: L590.
- Marks: OWNER QUESTION points present.

#### I69 · invention · 'Built alike': the exchange is an automorphism

Lines it formalizes or quotes (from the brief): L630.

- **Mimo** (reply lines 63–69; challenges): Not settled: "built alike" is undefined and the composition needs ψ to act on P; under the weaker reading t1 ∘ ψ is not defined unless the subnetworks are disjoint; proposes new wording in L630 (writes I69's automorphism reading in).
  - Proposal `M17-B6` (reply lines 65–67), would change L630:

````
L630 | The two things are built alike in \(P\): the exchange of them is an automorphism of \(P\), carrying the relations and preserving \(\mathcal L\); and their persistence components are alike in \(S_1\) in the same sense.
````

- **GLM** (reply lines 45–49; challenges): Not settled: "built alike" could mean an isomorphism of the two things' subnetworks only; the argument needs the exchange to preserve the whole contract and the answers; proposes a new opening of L630 (writes I69 in).
  - Proposal `G17-B4` (reply lines 46–48; printed in full under FC103 above), would change L630.
  - Quotations: “Built alike” — found at L630.
- **Goes to a checker** (rule 5): challenged by GLM and Mimo. Lines at stake: L630.

#### I70 · invention · A structure-preserving bijection of all the data (Argument 8)

Lines it formalizes or quotes (from the brief): L612.

- **Mimo** (reply line 71; challenges): The words nearly settle it; "carriers" and the physical module are the gaps, covered by the L612 proposal; alternative (a) cannot stand with (G) and (EX) in the conclusion.
  - Proposal `M17-B4` (reply lines 35–37; printed in full under FC100 above), would change L612.
- **GLM** (reply lines 51–54; challenges): Largely settled: "all carriers … and declared inputs" with "structure-preserving" excludes alternative (a), read with S26; the query and its designation δ are not named; proposes a new first sentence of L612.
  - Proposal `G17-B5` (reply lines 52–54), would change L612:

````
Transporting all carriers, relations, transports, histories, contracts, the query and its designation, and declared inputs along structure-preserving bijections preserves (E), (G), (P), (EX).
````

  - Quotations: “All carriers, relations, transports, histories, contracts and declared inputs” — found at L612; “structure-preserving” — found at L315, L610, L612.
- **Goes to a checker** (rule 5): challenged by GLM and Mimo. Lines at stake: L612.

#### I100 · invention · The two-layer episode's object layer: cells, occlusion and windows

Lines it formalizes or quotes (from the brief): L620, L622.

- **Mimo** (reply line 73; challenges): Settled by the words on identity: L620 and L622's "S0 predicts occupancy from recent occupancy" carry no identity, ruling out choice (c); not settled: "occlude a cell" against a run, the rule at the ends, the bounds; with one occluded cell a window-2 predictor extrapolates the velocity, so the episode's surprise needs a run or a thing staying in the hidden cell; the words should say which (the L620 proposal under H17 writes the run in).
  - Proposal `M17-B7` (reply lines 77–79; printed in full under FC102 above), would change L620.
- **GLM** (reply lines 56–60; challenges **OWNER QUESTION**): Not settled on four counts: cell and step counts (may stay open), the rule at the ends (reflection invented), interaction (H17), one cell or a run (the text says "occlude a cell"); proposes a new L620 (writes I100's "stated rule", H17's no-interaction and the run in); "the owner chooses the rule".
  - Proposal `G17-B6` (reply lines 57–59; printed in full under FC102 above), would change L620.
  - Quotations: “a line of cells” — found at L620; “occlude a cell” — found at L620; “stated rule” — not found in the text; found in the brief.
- **External reader and case card:** E10 (the external reader) challenges the sentence this item formalizes (section 3 below).
- **Goes to a checker** (rule 5): challenged by GLM and Mimo; challenged by E10 (the external reader). Lines at stake: L620.
- Marks: OWNER QUESTION points present.

#### I52 · invention · Selection: the parameters witnessed in a physical history

Lines it formalizes or quotes (from the brief): L195.

- **Mimo:** no point on this item.
- **GLM:** no point on this item.
- **External reader and case card:** C04 (the case card) challenges the sentence this item formalizes (section 4 below).
- **Goes to a checker** (rule 5): challenged by C04 (the case card). Lines at stake: L195.

#### I68 · invention · Argument 10's two-layer episode, encoded; 'recent occupancy'

Lines it formalizes or quotes (from the brief): L620, L622.

- **Mimo:** no point on this item.
- **GLM:** no point on this item.
- **External reader and case card:** E10 (the external reader) challenges the sentence this item formalizes (section 3 below).
- **Goes to a checker** (rule 5): challenged by E10 (the external reader). Lines at stake: L622.

#### H17 · H-entry · Two things that may share a cell and pass through each other (E9, I68, I100; FC102)

Lines it formalizes or quotes (from the brief): L620.

- **Mimo** (reply lines 75–81; challenges): Not settled (L620 says nothing of interaction); proposes a new L620 (writes H17's non-interaction and I100's occlusion run in); the other choice changes FC102's two-thing findings.
  - Proposal `M17-B7` (reply lines 77–79; printed in full under FC102 above), would change L620.
- **GLM** (reply lines 62–65; challenges): The text does not settle interaction, and two results depend on it (FC102 (b)'s two-thing failure; L622's "It is faithful on H0", which a crossing in H0 would defeat); the L620 wording and an addition after L622's faithfulness stipulation (relying on FC102's fragment).
  - Proposal `G17-B6` (reply lines 57–59; printed in full under FC102 above), would change L620.
  - Proposal `G17-B7` (reply lines 63–65; printed in full under FC102 above), would change L622.
  - Quotations: “It is faithful on H0” — found at L622.
- **External reader and case card:** E10 (the external reader) challenges the sentence this item formalizes (section 3 below).
- **Goes to a checker** (rule 5): challenged by GLM and Mimo; challenged by E10 (the external reader). Lines at stake: L620, L622.

#### H18 · H-entry · FC101's "edits deleting internal components" encoded as knock-outs (the model)

Lines it formalizes or quotes (from the brief): L103.

- **Mimo** (reply line 83; challenges): Settled by L103 ("A deleted component imposes the full relation on its ports."); the encoding should impose the full relation; no change to the text.
- **GLM** (reply line 67; challenges): The text settles it (L103, "A deleted component imposes the full relation on its ports."); the program's flags are an implementation gap that should have been recorded (S36); reasoned with the full relation, FC101 (b)'s status does not change; no text change.
  - Quotations: “A deleted component imposes the full relation on its ports.” — found at L103, L255.
- **Goes to a checker** (rule 5): challenged by GLM and Mimo. Lines at stake: L103.

#### H20 · H-entry · Smaller unregistered choices

Lines it formalizes or quotes (from the brief): L155, L317, L422, L475, L528.

- **Mimo** (reply lines 85–91; does not challenge): Takes H20's items one by one (tabulated under D3.4, D13.6, D15.5 and D16.5 below).
- **GLM** (reply lines 69–74; does not challenge): Takes H20's five items one by one (tabulated under D3.4, D13.6, D10.3, D15.5 and D16.5).
  - Quotations: “the surviving member of a population under a variation-and-survival history” — found at L155; “as for transports (D12.1, D12.2)” — not found in the text; found in the brief; “Connected to a critical episode” — found at L528; “has an instance of (G) in a critical episode” — not found in the text; found in the brief.
- **Goes to no checker**: no point challenges it and it is not one of the twelve; recorded under rule 7 below.

#### NF01 · NF entry

Lines it formalizes or quotes (from the brief): L17.

- **Mimo:** no point on this item.
- **GLM** (reply line 31; does not challenge): None of NF01–NF06, NF15 needs a change; L536–L542 speak at the level of arguments (S23), which the semantics need not define.
  - Quotations: “explanatory work” — found at L540.
- **External reader and case card:** E06 (the external reader) challenges the sentence this item formalizes (section 3 below); E22 (the external reader) challenges the sentence this item formalizes (section 3 below).
- **Goes to a checker** (rule 5): challenged by E06 (the external reader), E22 (the external reader). Lines at stake: L17.

#### NF02 · NF entry

Lines it formalizes or quotes (from the brief): L536.

- **Mimo:** no point on this item.
- **GLM** (reply line 31; does not challenge): No change; its formal part is written and the residue rightly left.
  - Quotations: “explanatory work” — found at L540.
- **External reader and case card:** E06 (the external reader) challenges the sentence this item formalizes (section 3 below).
- **Goes to a checker** (rule 5): challenged by E06 (the external reader). Lines at stake: L536.

#### NF03 · NF entry

Lines it formalizes or quotes (from the brief): L538.

- **Mimo:** no point on this item.
- **GLM** (reply line 31; does not challenge): No change; its formal part is written and the residue rightly left.
  - Quotations: “explanatory work” — found at L540.
- **External reader and case card:** E06 (the external reader) challenges the sentence this item formalizes (section 3 below); E15 (the external reader) challenges the sentence this item formalizes (section 3 below).
- **Goes to a checker** (rule 5): challenged by E06 (the external reader), E15 (the external reader). Lines at stake: L538.

#### NF04 · NF entry

Lines it formalizes or quotes (from the brief): L540.

- **Mimo:** no point on this item.
- **GLM** (reply line 31; does not challenge): No change this round; the reader would not leave "explanatory work" forever ((Elim)'s work is done in the core by FC18 and FC96).
  - Quotations: “explanatory work” — found at L540.
- **Goes to no checker**: no point challenges it and it is not one of the twelve; recorded under rule 7 below.

#### NF05 · NF entry

Lines it formalizes or quotes (from the brief): L542.

- **Mimo:** no point on this item.
- **GLM** (reply line 31; does not challenge): No change.
  - Quotations: “explanatory work” — found at L540.
- **External reader and case card:** E14 (the external reader) challenges the sentence this item formalizes (section 3 below).
- **Goes to a checker** (rule 5): challenged by E14 (the external reader). Lines at stake: L542.

#### NF06 · NF entry

Lines it formalizes or quotes (from the brief): L544.

- **Mimo:** no point on this item.
- **GLM** (reply line 31; does not challenge): No change.
  - Quotations: “explanatory work” — found at L540.
- **Goes to no checker**: no point challenges it and it is not one of the twelve; recorded under rule 7 below.

#### NF15 · NF entry

Lines it formalizes or quotes (from the brief): L45.

- **Mimo:** no point on this item.
- **GLM** (reply line 31; does not challenge): No change.
  - Quotations: “explanatory work” — found at L540.
- **Goes to no checker**: no point challenges it and it is not one of the twelve; recorded under rule 7 below.

#### D3.4 · definition (named under H20) · Provenance of a contract

Lines it formalizes or quotes (from the brief): L155.

- **Mimo** (reply line 85; challenges): (Under H20.) Settled: L155 gives contracts their own provenance ("the surviving member of a population under a variation-and-survival history", as H20 quotes it); D3.4 should quote it and not borrow the transports' provenance; where the two differ the words decide.
- **GLM** (reply line 70; challenges): (Under H20.) The words should stand: L155 gives contracts their own provenance; the maths' "as for transports (D12.1, D12.2)" drops different content; register it or rewrite D3.4 on L155's words (relying on L155 as quoted in H20).
  - Quotations: “the surviving member of a population under a variation-and-survival history” — found at L155; “as for transports (D12.1, D12.2)” — not found in the text; found in the brief.
- **Goes to a checker** (rule 5): challenged by GLM and Mimo. Lines at stake: L155.

#### D13.6 · definition (named under H20) · Attempt; Origin (G)

Lines it formalizes or quotes (from the brief): L422.

- **Mimo** (reply line 87; challenges): (Under H20.) Not settled: "attempt" is named and undefined; it joins the L596 proposal.
  - Proposal `M17-B3` (reply lines 25–27; printed in full under FC98 above), would change L596.
- **GLM** (reply line 71; challenges): (Under H20.) Not settled; Attempt belongs on D0.2's list and in the L596 addition.
  - Proposal `G17-B2` (reply lines 14–16; printed in full under FC98 above), would change L596.
- **Goes to a checker** (rule 5): challenged by GLM and Mimo. Lines at stake: L596.

#### D10.3 · definition (named under H20) · Test

Lines it formalizes or quotes (from the brief): L317.

- **Mimo:** no point on this item.
- **GLM** (reply line 72; does not challenge): (Under H20.) A numbering matter of the maths; no text change.
- **Goes to no checker**: no point challenges it and it is not one of the twelve; recorded under rule 7 below.

#### D15.5 · definition (named under H20) · Owned capability

Lines it formalizes or quotes (from the brief): L475.

- **Mimo** (reply line 89; challenges): (Under H20.) Not settled here: ownership is defined for subhistories (D13.7) and the formal applies it to a protocol and a constructor attribute; no wording; stays open until that clause is read; the extension should be recorded as an invention and both readings tested.
- **GLM** (reply line 73; challenges): (Under H20.) D13.7 defines ownership for subhistories only; applying it to a protocol and a constructor attribute extends it; register the extension; no words added.
- **Goes to a checker** (rule 5): challenged by GLM and Mimo. Lines at stake: L475.

#### D16.5 · definition (named under H20) · Classes

Lines it formalizes or quotes (from the brief): L528.

- **Mimo** (reply line 91; challenges): (Under H20.) Settled by the words' "connected to a critical episode"; the formal's "has an instance of (G) in a critical episode" is stronger and should read "connected".
- **GLM** (reply line 74; challenges): (Under H20.) The words should stand: "connected to a critical episode" is broader than "has an instance of (G) in a critical episode"; the narrowing should be registered or dropped.
  - Quotations: “Connected to a critical episode” — found at L528; “has an instance of (G) in a critical episode” — not found in the text; found in the brief.
- **Goes to a checker** (rule 5): challenged by GLM and Mimo. Lines at stake: L528.

#### Part 17: items no point addresses

Items of this part on which neither reader made any point (both replies read whole): D0.1, D0.2. Each is recorded under rule 7 in section 6 unless a point on it in another part sends it to a checker.


## 3. The external reader's findings, E01 to E22

From the document itself (`results/S104 Round 2 - external cross-examination supplied by the owner.txt`, read whole; line numbers are the document's, "doc L…"), with the items file (`… - items.md` and `.json`) used as an index to it; where the two differ the document's words govern (addendum point 2). Each finding is marked as addendum point 7 says: "challenges the text", "a finding about scope; no line challenged" (section 3 of the document, E07 to E12, except E10), or "challenges no line". Its repairs have no exact wording; each is copied exactly from the document between fence lines as the proposal it makes (addendum point 6). Its quotations of the text (in quotation marks) are compared with the text under review. The external reader's silence on an item records nothing (addendum point 10).

#### E01 · What it finds stands

Document section 1, doc L13–L21. Marked: **challenges no line (what it finds stands; addendum point 5)**. Places in the text it names or the items file gives: L159, L211, L245, L367, L407, L409.

- **Finding:** The strongest part is the three fidelities together, which keep a correct answer from vindicating the proposed mechanism; the text keeps a representation of a theory in error apart from an erroneous representation, admits inexplicit, distributed and temporally extended representation, and treats a narrower claim as a new index; these strengths do not show that the class captures everything called explanatory creativity.
  - Quotations: “people can understand false theories” (doc L17) — not found in the text; “people sometimes reason without verbalizing the steps” (doc L17) — not found in the text.
- **Goes to no checker by itself**; context for the checker of any group whose lines it names (addendum point 4): L159, L211, L245, L367, L407, L409.

#### E02 · The contribution test can make irrelevant material “indispensable”

Document section 2.1, doc L25–L85. Marked: **challenges the text**. Places in the text it names or the items file gives: L103, L231, L287, L296, L299, L305, L313.

- **Finding:** With k: Y = X and an unrelated d: V = U both in Γ, identity transports and a contract of the baseline and the partial interventions setting X and U, the full candidate meets (F1), (F2) and (A); deleting d (ports kept) leaves the answer about Y correct throughout the contract but leaves V unconstrained, so (F2) fails; so CriticalBlock({d}; {k,d}, p) holds and d is globally indispensable though deleting it never changes the answer about Y; the definitions run together indispensability to the fidelity of the whole represented organization and contribution to explaining the question. Its own verdict: a classification problem in the interpretation of explanatory contribution, not a refutation of sufficiency (the full candidate still explains Y through k). It considers and answers two defences (d should not have been a commitment; delete d's ports and change the projection).
  - Repair or proposal in its own words (doc L84–L85), would change L287, L296, L299, L305, L313 (no exact wording given):

````
Repair:
Distinguish structural-fidelity criticality from question-relative explanatory contribution. The latter needs a relevance condition or an explicit question-preserving reduction, not merely failure of Account after deletion.
````

  - Quotations: “indispensable” (doc L25) — found at L305, L307.
  - Note: The items file records it reproduced as FC-E1 on the S104 model, resting on I29 and I103 (addendum point 9). The repair has no exact wording (addendum point 6); the lines given are those of the definitions it names (the restriction L287, (B) L296, route and criticality L299, contributory and globally indispensable L305, no work L313); the items file adds L231 through "the work".
- **Goes to a checker** (addendum point 4; rule 5): the finding challenges the text or it is in doubt whether it does. Lines at stake: L287, L296, L299, L305, L313.

#### E03 · Representation and construction appear to depend on each other

Document section 2.2, doc L87–L121. Marked: **challenges the text**. Places in the text it names or the items file gives: L197, L208, L405, L520, L526.

- **Finding:** Read literally, (R) needs Sel or Con; constructed provenance needs an episode with a construction trace and a represented target; Build prepares "a represented organization" and its trace includes "the resulting representation"; so Rep → Con → Build → Rep; L526's order lists Build without (R) and says there is no cycle; L526's warning names the risk and does not supply the missing construction. The strongest defence (a construction trace recognizable from physical processes without applying Rep to its output) could work but must be the actual definition. Its verdict, in its words: "An unresolved foundational dependency, not a proof that no coherent version of the framework exists."
  - Repair or proposal in its own words (doc L117–L118), would change L197, L405, L526 (no exact wording given):

````
Repair:
Define a raw physical construction relation first. Its premises may refer to representations at strictly earlier stages; its output should initially be a carrier with specified structural properties. Then derive representation of that output. A ranked inductive definition would make the intended grounding explicit.
````

  - Quotations: “This occurrence represents because it was constructed; it was constructed because the relevant physical process produced this representation.” (doc L106) — not found in the text; “Construction trace” (doc L113) — found at L155, L197, L225, L405 and 3 more lines.
  - Note: No wording; the items file notes the bearing on Argument 6 (L596).
- **Goes to a checker** (addendum point 4; rule 5): the finding challenges the text or it is in doubt whether it does. Lines at stake: L197, L405, L526.

#### E04 · Functional determination does not uniquely identify outputs

Document section 2.3, first half, doc L123–L138; doc L144–L145. Marked: **challenges the text**. Places in the text it names or the items file gives: L103, L109, L119, L325.

- **Finding:** By L109's output criterion both ports of L = {(0,0),(1,1)} are outputs (a finite check confirms it), so the criterion does not tell Y := X from X := Y; the edits tell them apart once it is said which component an intervention replaces, but the text calls that "the component that 'assigns' the port", which needs an independent definition from the edit structure or explicit inclusion in the supplied data. Verdict: repairable under-specification.
  - Repair or proposal in its own words (doc L138), would change L103, L109, L119 (no exact wording given):

````
That assignment relation needs either an independent definition from the edit structure or explicit inclusion in the supplied data.
````

  - Quotations: “assigns” (doc L138) — found at L119, L189, L231.
  - Note: The items file records it reproduced as FC-E2 (resting on I05 and I105). It is the point of I04's alternatives and FC02 (c), on which Mimo and GLM made points in part 1.
- **Goes to a checker** (addendum point 4; rule 5): the finding challenges the text or it is in doubt whether it does. Lines at stake: L103, L109, L119.

#### E05 · The families of signatures do not give a sharp classification; kinds beyond the signatures

Document section 2.3, second half, doc L140–L145. Marked: **challenges the text (in doubt: the items file sends it to a checker)**. Places in the text it names or the items file gives: L11, L121, L123, L124, L125, L127, L558.

- **Finding:** A causal assignment Y := X and a measuring component N := X both keep their own relation under an upstream intervention on X, so their distinction cannot come merely from whether their relation changes under it; the listed patterns do not give the sharp classification the prose around them suggests (measurements can be causal processes). Argument 1 keeps the text's own signatures; it does not show that they exhaust every scientifically important sense of kind.
  - Note: No repair beyond "Repairable under-specification". The second half (L11, L558, bearing on (Elim) at L540) is recorded by the items file as a question of scope; the lines given are the families' (L121–L127). Reproduced as FC-E3 (resting on I06, I107).
- **Goes to a checker** (addendum point 4; rule 5): the finding challenges the text or it is in doubt whether it does. Lines at stake: L121, L123, L124, L125, L127.

#### E06 · The proposed falsification tests are narrower than some of the claims

Document section 2.4, doc L147–L173. Marked: **challenges the text**. Places in the text it names or the items file gives: L17, L61, L277, L536, L538.

- **Finding:** The denial of necessity on a question p is a candidate that explains p and fails Account on p's contract, but Part XV (L538) asks for a candidate whose organization no transport can preserve under any contract on its target, a much stronger demand; two theses (every explanation of a specified question meets the conditions there; every explanation is representable somewhere) have different counterexamples; and (Suff) (L536) adds a non-declared provenance though Account does not require it. Verdict: the central claims and their admissible refutations need to be aligned.
  - Repair or proposal in its own words (doc L172–L173), would change L17, L536, L538 (no exact wording given):

````
Verdict:
The statements of the central claims and their admissible refutations need to be aligned. Otherwise, a critic can defeat one claim while the document answers by defending a weaker one.
````

  - Note: The items file adds L61's summary.
- **Goes to a checker** (addendum point 4; rule 5): the finding challenges the text or it is in doubt whether it does. Lines at stake: L17, L536, L538.

#### E07 · Neural readout against causal mechanism: a successful test

Document section 3.1, doc L187–L223. Marked: **a finding about scope; no line challenged (addendum point 7)**. Places in the text it names or the items file gives: L37, L127, L151, L159, L606.

- **Finding:** On the memory system M := X, N := M, Y := M, the proposal Y := N meets the matching conditions on cue changes and fails (F1), (F2) and answer fidelity once the contract holds X = 1, do(N = 0): the framework separates an adequate scoped dependence from a stronger causal attribution ("a real success"); it does not find which neural intervention isolates the readout.
  - Note: Reproduced as FC-E4 (resting on I108). What it credits counts for nothing either way (addendum point 5).
- **Goes to no checker by itself**; context for the checker of any group whose lines it names (addendum point 4): L37, L127, L151, L159, L606.

#### E08 · Surprise: the clearest cognitive mismatch

Document section 3.2, doc L225–L273. Marked: **a finding about scope; no line challenged (addendum point 7)**. Places in the text it names or the items file gives: L25, L221, L223, L584.

- **Finding:** (A) A correct probabilistic model can meet a surprising outcome (P(B) = 0.01, about 6.64 bits) without any unfaithful representation; (B) two agents with the same expectation and response differ only in how the expectation was acquired, and the text calls one violation surprise and the other not; a cognitive application needs an argument that this historical difference marks a psychological one. The strongest defence (surprise is a technical term) answers logical inconsistency; Argument 4 follows from the definition; the price is that the text's surprise is not a general account of psychological surprise.
  - Repair or proposal in its own words (doc L269–L270), would change none (no exact wording given):

````
Repair:
Distinguish statistical unexpectedness, subjective prediction discrepancy, recognized model inadequacy, and the provenance of the expectation. Those can interact without being defined as the same thing.
````

  - Quotations: “Surprise” (doc L265) — found at L215, L221, L223, L576 and 5 more lines.
  - Note: Its repair is a proposal about scope; no line named. The items file notes that its point (B) meets FC81 (d) and H05.
- **Goes to no checker by itself**; context for the checker of any group whose lines it names (addendum point 4): L25, L221, L223, L584.

#### E09 · Infant exploration: representable, but not yet classified

Document section 3.3, first part, doc L275–L293; doc L297–L300. Marked: **a finding about scope; no line challenged (addendum point 7)**. Places in the text it names or the items file gives: L405, L407, L409, L429, L632.

- **Finding:** The framework can describe an infant case (object layer, predictions, a represented difficulty, a construction or selection response), but exploration behaviour does not show that the infant represented a defect in its own account or built a new binding rather than recruiting an existing capacity; tacit representation is allowed, but that does not show the representations Build or a critical episode need were present; representability succeeds while the empirical classification stays underdetermined.
- **Goes to no checker by itself**; context for the checker of any group whose lines it names (addendum point 4): L405, L407, L409, L429, L632.

#### E10 · “Predicts from occupancy” does not fix a memoryless predictor

Document section 3.3, second part, doc L295. Marked: **challenges the text (a finding of section 3 that bears on sentences of the text, L622 and L626; addendum point 7)**. Places in the text it names or the items file gives: L620, L622, L624, L626.

- **Finding:** "Predicts from occupancy" does not by itself fix a memoryless architecture: a predictor using occupancy histories may carry information through an occlusion; for no member of a selected population to survive the extended history, its state and memory restrictions must be specified, not only its sensory input.
  - Repair or proposal in its own words (doc L295), would change L622, L626 (no exact wording given):

````
To establish the claimed impossibility for a selected population, one must specify its state and memory restrictions, not just describe its sensory input.
````

  - Quotations: “Predicts from occupancy” (doc L295) — not found in the text.
  - Note: The same point as FC102 (b), one of the twelve; Mimo and GLM made points on FC102 in part 17 (and Mimo proposed a new L622 under I68 in part 15).
- **Goes to a checker** (addendum point 4; rule 5): the finding challenges the text or it is in doubt whether it does. Lines at stake: L622, L626.

#### E11 · Model-based learning: no ready-made psychological distinction

Document section 3.4, doc L302–L328. Marked: **a finding about scope; no line challenged (addendum point 7)**. Places in the text it names or the items file gives: L13, L225, L584.

- **Finding:** Selection is not model-free learning and construction is not model-based learning: planning can use a learned model through a retained procedure with no new binding and no criticism, and criticism can revise a simple value-based policy; the distinctions concern different things (computational organization against the history of a correspondence), and trial-by-trial predictions come from supplied mechanisms, not from Account or provenance.
  - Repair or proposal in its own words (doc L323), would change none (no exact wording given):

````
A cognitive application must measure both rather than substituting one for the other.
````

- **Goes to no checker by itself**; context for the checker of any group whose lines it names (addendum point 4): L13, L225, L584.

#### E12 · Finding questions: recording the event is not explaining its occurrence

Document section 3.5, doc L330–L347. Marked: **a finding about scope; no line challenged (addendum point 7)**. Places in the text it names or the items file gives: L15, L544, L588, L592.

- **Finding:** The semantics can record that an agent changed its aims, hypotheses or questions, and supplies no mechanism that selects which change occurs; Argument 5 gives an encoding possibility, not a theory of why particular questions are found; a problem only where representability is treated as the explanatory achievement.
- **Goes to no checker by itself**; context for the checker of any group whose lines it names (addendum point 4): L15, L544, L588, L592.

#### E13 · Declared indices: objective, or merely conditional

Document section 4.1, doc L351–L369. Marked: **challenges the text (in doubt: the items file sends it to a checker)**. Places in the text it names or the items file gives: L31, L43, L159, L473, L522, L608.

- **Finding:** Conditionality is not subjectivity, but the assessment turns on the choice of target, grain, decomposition, counterparts, admitted changes and scope, and the text leaves the justification of a restricted scope as a criticizable input; recording the choices makes adjustment after the result visible and does not show that the question is the one a theory needed to answer; without a procedural protection the framework risks becoming a precise language for whatever interpretation the investigator favours.
  - Repair or proposal in its own words (doc L367), would change L159, L473, L522 (no exact wording given):

````
For cognitive-science applications, the protection should be procedural: specify the relevant grain, contrasts, component mappings, and admissible revisions before testing the decisive cases.
````

  - Quotations: “Everything is relative, so nothing matters.” (doc L359) — not found in the text.
  - Note: No wording. The items file: the text asks for declaration before attribution for boundary and continuity (L473) and records scope (L159, L522); whether grain, counterparts and contrasts call for the same is the question. The same point as its closing question (E22).
- **Goes to a checker** (addendum point 4; rule 5): the finding challenges the text or it is in doubt whether it does. Lines at stake: L159, L473, L522.

#### E14 · Selection and construction: separate mechanisms, or separate labels on histories

Document section 4.2, doc L371–L384. Marked: **challenges the text (in doubt: the items file sends it to a checker)**. Places in the text it names or the items file gives: L47, L77, L201, L411, L542.

- **Finding:** Argument 3's qualified underdetermination is sound, with the population restriction doing the work, but it gives no general discontinuity between selection and construction: an evolutionary search with represented candidates, explicit counterexamples and content-sensitive revision might count as construction, so "selection" here is narrower than variation and selection in general; the ban on represented targets in selected histories gives a difference of classification, not a mechanistic irreducibility result.
  - Repair or proposal in its own words (doc L381–L382), would change L47, L77, L201, L542 (no exact wording given):

````
The adversarial demand:
Identify what a construction mechanism does that is not already captured by the independently specified physical processes, representations, memory, and feedback in its history.
````

  - Quotations: “selection” (doc L379) — found at L13, L21, L41, L47 and 12 more lines.
  - Note: No wording. The items file: whether L47, L77, L201 and L542 claim more than a difference of classification. The case card's C02 bears on the same place.
- **Goes to a checker** (addendum point 4; rule 5): the finding challenges the text or it is in doubt whether it does. Lines at stake: L47, L77, L201, L542.

#### E15 · Exact fidelity and explanatory idealization

Document section 4.3, doc L386–L399. Marked: **challenges the text (in doubt: the items file sends it to a checker)**. Places in the text it names or the items file gives: L242, L250, L277, L363, L538.

- **Finding:** (F1), (F2) and (A) are exact equalities; the approximate transport bound does not replace Account with an approximate account; a model may capture a dependence while simplifying its realization; the text's two answers (an exact coarse-grained dependence, or a question about the approximation) do not show that every useful idealization is handled without changing what it was offered to explain; the burden is to show that exactness tracks the intended distinction rather than classing most working explanations as candidates.
  - Repair or proposal in its own words (doc L398–L399), would change L277, L363, L538 (no exact wording given):

````
Verdict:
A substantive necessity question, not an immediate contradiction. A worked cognitive idealization is needed, with the coarse-graining and preserved dependence written out.
````

  - Note: No wording; it asks for a worked cognitive idealization.
- **Goes to a checker** (addendum point 4; rule 5): the finding challenges the text or it is in doubt whether it does. Lines at stake: L277, L363, L538.

#### E16 · Does the argument machinery explain reasoning?

Document section 4.4, doc L401–L412. Marked: **challenges no line (a finding about scope)**. Places in the text it names or the items file gives: L8, L393, L397, L429.

- **Finding:** Usability records what an agent admits and retains and can model the consequences of its commitments, but does not explain why an agent adopts a premise, notices a conflict, drops an assumption or stops; the text calls these choices, which is no logical error, but in cognitive science they are phenomena to be explained; "redescribing an argument for a conclusion as an argument against its denial does not by itself explain the psychological operation or settle its epistemic status". Verdict: useful bookkeeping; incomplete as a theory of reasoning dynamics.
  - Note: Its remark on arguments bears on L8 and L397's reading of "argument", the owner's decision S23; a point against that reading is a question for the owner and no ruling may change it (addendum point 8): marked OWNER QUESTION, not weighed.
  - Marks: OWNER QUESTION.
- **Goes to no checker by itself**; context for the checker of any group whose lines it names (addendum point 4): L8, L393, L397, L429.

#### E17 · The capability conditions and ordinary fallible performance

Document section 4.5, doc L414–L424. Marked: **challenges the text**. Places in the text it names or the items file gives: L466, L479, L495, L509.

- **Finding:** (CT1) quantifies over every admitted execution, so a task with a small nonzero chance of failure, the failures in the execution family, fails it where ordinary usage would call the ability retained; the text has tolerances, but must show whether a tolerance ranges over a distribution of executions or only over the quality of each output; "non-question-begging" enabling conditions must exclude supplying the very explanation being attributed while permitting teaching and scaffolding; finite performance does not suffice for universality, and nothing here shows the universal class empty or non-empty.
  - Repair or proposal in its own words (doc L420), would change L466, L479, L495 (no exact wording given):

````
The document includes tolerances, so it has resources for responding. But it needs to show explicitly how reliability is represented—particularly whether tolerance applies to a distribution of executions rather than only to the quality of each output.
````

  - Repair or proposal in its own words (doc L422), would change L466, L479, L495 (no exact wording given):

````
At the universal level, the existential enabling conditions need equally careful treatment. “Non-question-begging” must exclude supplying the very explanation or discovery being attributed, while still permitting genuine teaching and scaffolding.
````

  - Quotations: “Non-question-begging” (doc L422) — found at L495.
  - Note: No wording.
- **Goes to a checker** (addendum point 4; rule 5): the finding challenges the text or it is in doubt whether it does. Lines at stake: L466, L479, L495.

#### E18 · Tables (set aside by the external reader)

Document section 5, doc L430–L431. Marked: **challenges no line (an attack it sets aside)**. Places in the text it names or the items file gives: L269, L536.

- **Finding:** "A complete counterfactual lookup table cannot explain" is no argument by itself: the text allows such a table when it keeps the component structure and meets the other conditions; repackaging a mechanism this way gave no sufficiency counterexample.
  - Quotations: “A complete counterfactual lookup table cannot explain.” (doc L430) — not found in the text.
  - Note: The items file notes that the S104 search found FC25 (b) against L269's "it meets (F1)", one of the twelve.
- **Goes to no checker by itself**; context for the checker of any group whose lines it names (addendum point 4): L269, L536.

#### E19 · The transport could hide the answer (set aside as open)

Document section 5, doc L433–L434. Marked: **challenges the text (it names an obligation L255 leaves open; addendum point 5)**. Places in the text it names or the items file gives: L255, L273.

- **Finding:** Hiding the answer in the flexible translations is a serious line of attack; the non-circularity clause may exclude plain versions, but encoded variants need a more exact account of structural answer-identity at the declared grain before they can be decided: an unresolved formalization obligation, not an exhibited counterexample.
  - Repair or proposal in its own words (doc L434), would change L255 (no exact wording given):

````
Encoded variants require a more exact account of structural answer-identity at the declared grain before they can be adjudicated.
````

  - Quotations: “The transport could hide the answer.” (doc L433) — not found in the text.
  - Note: Mimo and GLM made points on L255's NC1 in parts 6, 7 and 8 (I24, I83, D6.3).
- **Goes to a checker** (addendum point 4; rule 5): the finding challenges the text or it is in doubt whether it does. Lines at stake: L255.

#### E20 · Fixed port sets (set aside as repairable)

Document section 5, doc L436–L437. Marked: **challenges the text (in doubt: the items file sends it to a checker)**. Places in the text it names or the items file gives: L105, L425, L590.

- **Finding:** Organizations have fixed port sets, so adding structure (a new question, a new component) needs dormant slots, structure-valued ports or a meta-organization; the value domains look broad enough that this is repairable, not a demonstrated impossibility.
  - Repair or proposal in its own words (doc L437), would change L425, L590 (no exact wording given):

````
Some of the exact constructions need clearer encoding: adding structure requires dormant slots, structure-valued ports, or a meta-organization.
````

  - Quotations: “New questions or new components are impossible because the organizations have fixed port sets.” (doc L436) — not found in the text.
  - Note: The items file: L425 and L590 speak of adding a port and adding a change; (O) fixes the port set (I03).
- **Goes to a checker** (addendum point 4; rule 5): the finding challenges the text or it is in doubt whether it does. Lines at stake: L425, L590.

#### E21 · The finite monotone claim (set aside: no counterexample)

Document section 5, doc L439–L440. Marked: **challenges no line (an attack it sets aside)**. Places in the text it names or the items file gives: L305.

- **Finding:** Every upward-closed route family containing the whole commitment set, for one to four commitments (193 families), gives no counterexample to the finite monotone claim; the problem of 2.1 survives because the theorem can hold while its criticality predicate is read too strongly.
  - Quotations: “The finite-monotone theorem is wrong.” (doc L439) — not found in the text.
  - Note: Reproduced as FC-E5 (the items file).
- **Goes to no checker by itself**; context for the checker of any group whose lines it names (addendum point 4): L305.

#### E22 · The overall verdict, the revision priorities and the proposed benchmark

Document section opening, 5 (last paragraph), 6 and 7, doc L5–L9; doc L442; doc L444–L460; doc L462–L494. Marked: **challenges the text (in doubt: the items file sends it to a checker)**. Places in the text it names or the items file gives: L3, L17, L27, L546.

- **Finding:** Its verdict: promising as a framework for auditing explanatory claims, but, in its words, "it has not established its stronger claim to fully characterize explanatory creativity"; no decisive counterexample to sufficiency found; the small mathematical results do much less than the central claim ("Their correctness should not be mistaken for proof of the constitutive conjecture"); its strongest shown achievement is an audit language for scoped explanatory structure, its strongest advertised one a full characterization. Its revision priorities (explanatory relevance apart from whole-model fidelity; construction grounded without presupposing its result; surprise apart from fidelity failure; then an operational account of component mappings, traces and scope choices), its proposed benchmark (a known mechanism with hidden state, an editable measurement channel, an unrelated subsystem, classifications fixed before the critical interventions), and its decisive question (what the framework forces before grain, contract, counterparts and provenance are adjusted to the outcome).
  - Repair or proposal in its own words (doc L488), would change L3, L17 (no exact wording given):

````
The highest-priority revisions are to separate explanatory relevance from whole-model fidelity, ground construction without presupposing its resulting representation, and separate surprise from objective fidelity failure. The next priority is an operational account of the key inputs—especially component mappings, construction traces, and scope choices—so that empirical applications constrain those inputs rather than infer them from the classification desired.
````

  - Note: The items file: whether L3 and L17 say more than the text's results; the text calls the characterization a conjecture (L17). Its benchmark and priorities are proposals (addendum point 6). The scope findings (E07, E08, E09, E11, E12) and E16 bear on L17 through this item.
- **Goes to a checker** (addendum point 4; rule 5): the finding challenges the text or it is in doubt whether it does. Lines at stake: L3, L17.


## 4. The case card's items, C01 to C14

From the case card (`results/S104 Round 2 - case card, the creative transport experiment.md`, read whole), its table of findings (card lines 404–417) and the sections it points to; where the card and the case files differ the files govern (creative transport addendum, point 2). C01 to C07 and C11 (marked "yes" or "in doubt") go to a checker; C08 to C10 and C12 to C14 (marked "no") go to none by themselves and are context for the checker of any group whose lines they name. The card has no fixed verdict: no ruling may treat its classification (CT8) as a case result (the addendum, point 3). The card proposes no wording; each item's finding is copied exactly from the card's table between fence lines, with the lines it names, and the card's quotations of the text in that row are compared with the text under review.

#### C01

Card line 409. Lines named: L193, L199 (with L13). Marked by the card: **yes**. S104 on the same place (the card's column): FC78; D12.3; I53, I54; H05.

- **Finding (digest):** Where neither Sel nor Con holds (R2; R4 with L201 and L411), the case's transport has exactly one provenance only because Dec is defined by exclusion, and L199's "The transport is entered into the model by its author" and L13's "merely declared by whoever writes the model down" describe a history this is not (the pair was computed, not written); whether a deterministic routine's output is its writer's content (L427) is not said.
  - The card's own words (card line 409), no wording proposed; the lines it bears on: L13, L193, L199:

````
Where neither Sel nor Con holds (R2; R4 with L201 and L411), the case's transport has exactly one provenance only because Dec is defined by exclusion, and L199's "The transport is entered into the model by its author" and L13's "merely *declared* by whoever writes the model down" describe a history this is not: the pair was computed, not written. Whether a deterministic routine's output is its writer's content (L427) is not said.
````

  - Quotations: “The transport is entered into the model by its author” — found at L199; “merely *declared* by whoever writes the model down” — found at L13.
- **Goes to a checker** (creative transport addendum, point 2): marked yes. Lines at stake: L13, L193, L199.

#### C02

Card line 410. Lines named: L201, L411, L195. Marked by the card: **yes**. S104 on the same place (the card's column): E14; NF07; H05; FC78, FC82, FC83.

- **Finding (digest):** L201 tells the provenances apart by two profiles (no represented target and no criticism, or both); on the ordinary sense of "represents" the run's history has a represented target (its coded task, the codomain it builds) and no criticism (L383), and the novelty archive beneath retains by novelty with no fidelity condition; neither profile, nor L195's survival condition, describes these.
  - The card's own words (card line 410), no wording proposed; the lines it bears on: L195, L201, L411:

````
L201 tells the two provenances apart by two profiles: no represented target and no criticism, or both. The run's history, on the ordinary sense of "represents", has a represented target (its coded task and the codomain it builds) and no criticism (L383). The novelty archive beneath it retains by novelty, with no fidelity condition. Neither profile, and not L195's survival condition, describes these.
````

  - Quotations: “represents” — found at L13, L15, L57, L195.
- **Goes to a checker** (creative transport addendum, point 2): marked yes. Lines at stake: L195, L201, L411.

#### C03

Card line 411. Lines named: L195, L205–L211. Marked by the card: **in doubt**. S104 on the same place (the card's column): E03; FC98; D18.1; I56, I90, I114.

- **Finding (digest):** Whether L195's "No member of the history represents t, H, or the survival condition" holds of a machine search that codes its own task and scoring turns, under (R), on the provenance of the code's writing (declared: L211 makes the code represent nothing and the condition holds; constructed: it fails); the classification of the run turns on its carriers' history, which the case does not supply: E03's loop, met concretely.
  - The card's own words (card line 411), no wording proposed; the lines it bears on: L195, L205, L211:

````
Whether "No member of the history represents \(t\), \(H\), or the survival condition" holds of a machine search that codes its own task and scoring turns, under (R), on the provenance of the code's writing. If that writing is declared, L211 makes the code represent nothing and the condition holds; if constructed, it fails. The classification of the run turns on the classification of its carriers' history, which the case does not supply: E03's loop, met concretely.
````

  - Quotations: “No member of the history represents \(t\), \(H\), or the survival condition” — found at L195.
- **Goes to a checker** (creative transport addendum, point 2): marked in doubt. Lines at stake: L195, L205, L211.

#### C04

Card line 412. Lines named: L195 ("a survival condition requiring fidelity on \(H\)"). Marked by the card: **in doubt**. S104 on the same place (the card's column): I49, I50, I52; FC80.

- **Finding (digest):** The experiment's survival condition is answers at the pairs of H; on the eight cases it picks the same pairs as fidelity (CT2), on the four noninverted cases it keeps four pairs where fidelity keeps two (CT5); read as fidelity (I52) the noninverted training selects no direct pair, read as answers it does and Argument 3 applies; which extent of "fidelity" L195 asks for is I49's question.
  - The card's own words (card line 412), no wording proposed; the lines it bears on: L195:

````
The experiment's survival condition is answers at the pairs of H. On the eight cases it picks the same pairs as fidelity (CT2); on the four noninverted cases it keeps four pairs where fidelity keeps two (CT5). Read as fidelity (I52), the noninverted training is not a selection of the direct pair at all; read as answers, it is, and Argument 3 applies as written. Which extent of "fidelity" L195 asks for is I49's question.
````

  - Quotations: “fidelity” — found at L17, L23, L37, L41.
- **Goes to a checker** (creative transport addendum, point 2): marked in doubt. Lines at stake: L195.

#### C05

Card line 413. Lines named: L225 (with L481, L427). Marked by the card: **in doubt**. S104 on the same place (the card's column): FC82, FC83; H08; E11.

- **Finding (digest):** The interface change is a third kind of response to a failure, which L225 does not name: it neither extends H and lets μ act, nor is a construction in the system's own trace; it widens the population by a part supplied from outside the boundary; read as a construction response by the designer, L225 covers it and leaves "by whom" to L427.
  - The card's own words (card line 413), no wording proposed; the lines it bears on: L225:

````
The interface change is a third kind of response to a failure, which L225 does not name: it neither extends H and lets μ act, nor is a construction in the system's own trace. It widens the population by a part supplied from outside the boundary. Read as a construction response by the designer, L225 covers it and leaves "by whom" to L427.
````

  - Quotations: “by whom” — not found in the text.
- **Goes to a checker** (creative transport addendum, point 2): marked in doubt. Lines at stake: L225.

#### C06

Card line 414. Lines named: L405, L409 (Build). Marked by the card: **in doubt**. S104 on the same place (the card's column): I56, I115; FC83, FC84; E03, E14.

- **Finding (digest):** Whether exhaustive composition, blind to the task and scored against a coded task, is "a nontrivial binding construction relevant to that use", and whether use on a task is "explanatory use", is not said; between R1 and R2, and R3 and R4, the class turns on it.
  - The card's own words (card line 414), no wording proposed; the lines it bears on: L405, L409:

````
Whether exhaustive composition, blind to the task and scored against a coded task, is "a nontrivial binding construction relevant to that use", and whether use on a task is "explanatory use", is not said. Between R1 and R2, and between R3 and R4, the class turns on it.
````

  - Quotations: “a nontrivial binding construction relevant to that use” — found at L405; “explanatory use” — found at L405.
- **Goes to a checker** (creative transport addendum, point 2): marked in doubt. Lines at stake: L405, L409.

#### C07

Card line 415. Lines named: L55, L197 (and L429). Marked by the card: **in doubt**. S104 on the same place (the card's column): H06; I116.

- **Finding (digest):** Con asks for "an episode" (L197); under L55's sentence the run is none (no contract changes in it) and Con fails on every reading; under D13.8 any subhistory is one; the body of the text does not define "episode" by itself.
  - The card's own words (card line 415), no wording proposed; the lines it bears on: L55, L197:

````
Con asks for "an episode" (L197). Under L55's sentence the run is none, since no contract changes in it, and Con fails on every reading. Under D13.8 any subhistory is one. The text's body does not define "episode" by itself.
````

  - Quotations: “an episode” — found at L13, L31, L55, L155; “episode” — found at L13, L31, L55, L155.
- **Goes to a checker** (creative transport addendum, point 2): marked in doubt. Lines at stake: L55, L197.

#### C08

Card line 416. Lines named: L217–L223. Marked by the card: **no (a finding about scope)**. S104 on the same place (the card's column): I51, I119; E08; H13.

- **Finding (digest):** Prediction, violation and surprise are defined for transports to the simulation layer; the ablations' failures are violations or surprise only under I51's extension.
  - The card's own words (card line 416), no wording proposed; the lines it bears on: L217, L219, L220, L221, L223:

````
Prediction, violation and surprise are defined for transports to the simulation layer. The ablations' failures are violations or surprise only under I51's extension.
````

- **Goes to no checker by itself** (marked no (a finding about scope)); context for the checker of any group whose lines it names: L217, L219, L220, L221, L223.

#### C09

Card line 417. Lines named: L413–L416, L473. Marked by the card: **no**. S104 on the same place (the card's column): FC85; I112, I120.

- **Finding (digest):** (N) is relative to the system's repertoire: the protocol is new for the executed constructor and not for its designer; the README's "not a new-to-the-world" and "rediscovered" are about the world, which (N) does not use; the sentence works as written, given a declared boundary.
  - The card's own words (card line 417), no wording proposed; the lines it bears on: L413, L416, L473:

````
(N) is relative to the system's repertoire. The protocol is new for the executed constructor and not for its designer, and the README's "not a new-to-the-world" and "rediscovered" are about the world, which (N) does not use. The sentence works as written, given a declared boundary.
````

  - Quotations: “not a new-to-the-world” — not found in the text; “rediscovered” — not found in the text.
- **Goes to no checker by itself** (marked no); context for the checker of any group whose lines it names: L413, L416, L473.

#### C10

Card line 418. Lines named: L429, L441, L443–L453, L522, L534. Marked by the card: **no**. S104 on the same place (the card's column): FC86–FC90; E09.

- **Finding (digest):** (EX) is not met by the run (no conjectural objection, no content-sensitive response); its aims are a missing declared input; the designer's history is not supplied.
  - The card's own words (card line 418), no wording proposed; the lines it bears on: L429, L441, L443, L453, L522, L534:

````
(EX) is not met by the run: it holds no conjectural objection and no content-sensitive response. Its aims are a missing declared input. The designer's history, which may hold criticism (README L55–L58), is not supplied.
````

- **Goes to no checker by itself** (marked no); context for the checker of any group whose lines it names: L429, L441, L443, L453, L522, L534.

#### C11

Card line 419. Lines named: L193 (with L159). Marked by the card: **in doubt**. S104 on the same place (the card's column): I90, I111.

- **Finding (digest):** Provenance is defined only for a transport "whose domain is an organization of a physical system"; a target given only in code is a mathematical structure (L159) run on a physical computer; whether the case has a provenance at all turns on that (I111).
  - The card's own words (card line 419), no wording proposed; the lines it bears on: L193:

````
Provenance is defined only for a transport "whose domain is an organization of a physical system". A target given only in code is a mathematical structure (L159) run on a physical computer. Whether the case has a provenance at all turns on that (I111).
````

  - Quotations: “whose domain is an organization of a physical system” — found at L193.
- **Goes to a checker** (creative transport addendum, point 2): marked in doubt. Lines at stake: L193.

#### C12

Card line 420. Lines named: L231, L262 (with L466). Marked by the card: **no (a finding about scope)**. S104 on the same place (the card's column): I109, I110.

- **Finding (digest):** The protocol meets (E) only on a question whose target includes its own sender (CT1); on the channel alone no pair meets (E) (CT3); for a design, (E) reaches the designed system, not the world before the design.
  - The card's own words (card line 420), no wording proposed; the lines it bears on: L231, L262, L466:

````
The protocol meets (E) only on a question whose target includes its own sender (CT1). On the channel alone no pair meets (E) (CT3). For a design, (E) reaches the designed system, not the world before the design.
````

- **Goes to no checker by itself** (marked no (a finding about scope)); context for the checker of any group whose lines it names: L231, L262, L466.

#### C13

Card line 421. Lines named: L481, L572–L576, L195 (last sentence). Marked by the card: **no**. S104 on the same place (the card's column): FC80; H09.

- **Finding (digest):** The no-history population holds no pair meeting (E) (CT4), as L481's second clause says; Argument 3 works as written on the noninverted history (CT5) and on the twelve-bit words.
  - The card's own words (card line 421), no wording proposed; the lines it bears on: L195, L481, L572, L574, L576:

````
The no-history population holds no pair meeting (E) (CT4), as L481's second clause says of a part every member is built without. Argument 3 works as written on the noninverted history (CT5) and on the twelve-bit words.
````

- **Goes to no checker by itself** (marked no); context for the checker of any group whose lines it names: L195, L481, L572, L574, L576.

#### C14

Card line 422. Lines named: L427, L441. Marked by the card: **no**. S104 on the same place (the card's column): E17.

- **Finding (digest):** The previous-level access is "an instruction about what to read", L427's own example of an outside contribution; ProducedBy attributes the result to the designer's contribution and the run's search, with no division (L441); the sentences work as written.
  - The card's own words (card line 422), no wording proposed; the lines it bears on: L427, L441:

````
The previous-level access is "an instruction about what to read", L427's own example of an outside contribution. ProducedBy attributes the result to the designer's contribution and to the run's search, with no division (L441). The sentences work as written.
````

  - Quotations: “an instruction about what to read” — found at L427.
- **Goes to no checker by itself** (marked no); context for the checker of any group whose lines it names: L427, L441.


## 5. What goes to a checker (rule 5 and the addenda)

Every item a reader challenges, every one of the twelve counterexamples the second check reproduced, every external finding that challenges the text or may, and the case card's C01 to C07 and C11. "Lines" are the lines of the text under review its proposals would change or, where its points change no line, the lines its claim, definition or invention formalizes (for the one finding FC78, FC81 (d) and FC82, the lines of that finding, L193, L195 and L201, are added to each so that they fall in one group). Items that share a line fall in one group (rule 5); this file does not form the groups.

| id | kind | parts | raised by | lines | why | parked | owner question |
|---|---|---|---|---|---|---|---|
| D1.1 | definition | 1 | Mimo, GLM | L91, L103 | Mimo and GLM challenge it, with proposed wording for L91, L103. |  |  |
| D1.3 | definition | 1 | Mimo, GLM | L103, L339 | Mimo and GLM challenge it, with proposed wording for L103, L339. |  |  |
| D2.1 | definition | 1, 2, 7 | Mimo, GLM, external reader | L103, L109, L119 | Mimo and GLM challenge it, with proposed wording for L103, L109, L119; also E04, on the same sentence. |  |  |
| D2.2 | definition | 1, 2 | GLM | L109 | GLM challenges it, with proposed wording for L109. |  |  |
| D2.3 | definition | 1 | Mimo, GLM, external reader | L109 | Mimo and GLM challenge it, with proposed wording for L109; also E04, on the same sentence. |  |  |
| D2.4 | definition | 1, 2 | Mimo, GLM | L109 | Mimo and GLM challenge it, with proposed wording for L109. |  |  |
| D2.5 | definition | 1 | Mimo, GLM | L109 | Mimo and GLM challenge it (the maths departs from the words, the text settles an invention, or a counterexample), with no wording for the text. |  |  |
| D3.1 | definition | 4 | Mimo, GLM | L138, L253 | Mimo and GLM challenge it, with proposed wording for L138, L253. |  |  |
| D3.2 | definition | 4 | Mimo, GLM | L141, L253 | Mimo and GLM challenge it, with proposed wording for L141, L253. |  |  |
| D3.3 | definition | 4 | Mimo, GLM | L151 | Mimo and GLM challenge it, with proposed wording for L151. |  |  |
| D3.4 | definition | 4, 17 | Mimo, GLM | L155 | Mimo and GLM challenge it (the maths departs from the words, the text settles an invention, or a counterexample), with no wording for the text. |  |  |
| D3.5 | definition | 4 | Mimo, GLM, external reader | L257 | Mimo and GLM challenge it, with proposed wording for L257; also E13, on the same sentence. |  |  |
| D3.6 | definition | 4 | Mimo, GLM | L161 | Mimo and GLM challenge it, with proposed wording for L161. |  |  |
| D3.7 | definition | 4 | Mimo, GLM | L151 | Mimo and GLM challenge it, with proposed wording for L151. |  |  |
| D4.2 | definition | 3 | Mimo, GLM | L119 | Mimo and GLM challenge it, with proposed wording for L119. |  | yes |
| D4.3 | definition | 3, 5 | Mimo, GLM | L119 | Mimo and GLM challenge it, with proposed wording for L119. |  |  |
| D4.4 | definition | 3 | Mimo, GLM | L119, L556 | Mimo and GLM challenge it, with proposed wording for L119, L556. |  |  |
| D4.5 | definition | 1, 2, 3 | GLM | L113, L119 | GLM challenges it, with proposed wording for L113, L119. |  |  |
| D4.6 | definition | 1, 2, 3 | Mimo, GLM, external reader | L121, L123, L124, L125 | Mimo and GLM challenge it, with proposed wording for L123, L124; also E05, on the same sentence. |  |  |
| D5.1 | definition | 3, 5 | Mimo, GLM | L189, L231, L315 | Mimo and GLM challenge it, with proposed wording for L189, L231, L315. |  | yes |
| D5.2 | definition | 3, 5 | Mimo | L189, L233 | Mimo challenges it, with proposed wording for L189, L233. |  |  |
| D5.3 | definition | 5 | Mimo, GLM | L231 | Mimo and GLM challenge it, with proposed wording for L231. |  |  |
| D5.4 | definition | 3, 5, 6 | Mimo | L245 | Mimo challenges it, with proposed wording for L245. |  |  |
| D5.5 | definition | 5, 6 | Mimo | L242 | Mimo challenges it, with proposed wording for L242. |  |  |
| D5.6 | definition | 5, 6 | Mimo | L250 | Mimo challenges it, with proposed wording for L250. |  |  |
| D5.7 | definition | 5 | Mimo, GLM | L220, L245, L247, L520 | Mimo and GLM challenge it, with proposed wording for L220, L245, L247, L520. |  |  |
| D6.3 | definition | 6, 7, 8 | Mimo, GLM, external reader | L255 | Mimo and GLM challenge it, with proposed wording for L255; also E19, on the same sentence. |  |  |
| D6.4 | definition | 6, 7, 8 | Mimo, GLM | L255 | Mimo and GLM challenge it, with proposed wording for L255. |  | yes |
| D6.5 | definition | 6 | external reader | L255 | Challenged only by the external reader (E19), on the sentence it formalizes; no reader point challenges it. |  |  |
| D6.6 | definition | 6, 7 | GLM | L257 | GLM challenges it, with proposed wording for L257. |  |  |
| D6.7 | definition | 4, 5, 6 | GLM | L520 | GLM challenges it, with proposed wording for L520. |  |  |
| D6.8 | definition | 6 | GLM | L520 | GLM challenges it, with proposed wording for L520. |  |  |
| D6.9 | definition | 6, 7 | Mimo, GLM | L257 | Mimo and GLM challenge it, with proposed wording for L257. |  |  |
| D6.10 | definition | 6, 7 | Mimo, GLM | L269 | Mimo and GLM challenge it, with proposed wording for L269. |  |  |
| D7.1 | definition | 9 | Mimo, external reader | L287 | Mimo challenges it, with proposed wording for L287; also E02, on the same sentence. |  |  |
| D7.3 | definition | 9 | external reader | L296 | Challenged only by the external reader (E02), on the sentence it formalizes; no reader point challenges it. |  |  |
| D7.4 | definition | 9 | Mimo, GLM | L302 | Mimo and GLM challenge it, with proposed wording for L302. |  |  |
| D7.5 | definition | 9 | Mimo, GLM, external reader | L305 | Mimo and GLM challenge it, with proposed wording for L305; also E02, on the same sentence. |  |  |
| D7.6 | definition | 9 | external reader | L313 | Challenged only by the external reader (E02), on the sentence it formalizes; no reader point challenges it. |  |  |
| D8.1 | definition | 10, 11 | Mimo, GLM | L315 | Mimo and GLM challenge it, with proposed wording for L315. |  |  |
| D8.2 | definition | 10, 11 | Mimo | L315, L317 | Mimo challenges it, with proposed wording for L317. |  |  |
| D8.3 | definition | 10, 11 | Mimo, GLM | L315 | Mimo and GLM challenge it (the maths departs from the words, the text settles an invention, or a counterexample), with no wording for the text. |  |  |
| D8.5 | definition | 10 | Mimo, GLM | L315 | Mimo and GLM challenge it, with proposed wording for L315. |  |  |
| D9.1 | definition | 12 | Mimo | L397 | Mimo challenges it, with proposed wording for L397. |  |  |
| D9.4 | definition | 12 | Mimo | L393 | Mimo challenges it, with proposed wording for L393. |  |  |
| D9.5 | definition | 12 | Mimo | L393 | Mimo challenges it, with proposed wording for L393. |  |  |
| D9.6 | definition | 12 | Mimo | L393 | Mimo challenges it, with proposed wording for L393. |  |  |
| D9.7 | definition | 12 | Mimo | L397 | Mimo challenges it, with proposed wording for L397. |  |  |
| D9.9 | definition | 12 | Mimo, GLM | L395 | Mimo and GLM challenge it, with proposed wording for L395. |  |  |
| D9.10 | definition | 12 | Mimo, GLM | L377 | Mimo and GLM challenge it, with proposed wording for L377. |  |  |
| D9.11 | definition | 12 | Mimo | L385 | Mimo challenges it, with proposed wording for L385. |  |  |
| D10.1 | definition | 11 | Mimo | L317 | Mimo challenges it (the maths departs from the words, the text settles an invention, or a counterexample), with no wording for the text. |  |  |
| D10.2 | definition | 11 | Mimo | L317 | Mimo challenges it, with proposed wording for L317. |  |  |
| D10.3 | definition | 11, 17 | Mimo, GLM | L317 | Mimo and GLM challenge it, with proposed wording for L317. |  |  |
| D10.4 | definition | 11 | Mimo | L317 | Mimo challenges it, with proposed wording for L317. |  |  |
| D10.5 | definition | 11 | Mimo | L315 | Mimo challenges it (the maths departs from the words, the text settles an invention, or a counterexample), with no wording for the text. |  |  |
| D10.6 | definition | 11 | Mimo, GLM | L317 | Mimo and GLM challenge it (the maths departs from the words, the text settles an invention, or a counterexample), with no wording for the text. |  | yes |
| D11.1 | definition | 9 | Mimo | L169 | Mimo challenges it, with proposed wording for L169. |  |  |
| D11.2 | definition | 9 | Mimo | L169 | Mimo challenges it (the maths departs from the words, the text settles an invention, or a counterexample), with no wording for the text. |  |  |
| D11.3 | definition | 9 | Mimo, GLM | L375 | Mimo and GLM challenge it, with proposed wording for L375. |  |  |
| D11.4 | definition | 9 | Mimo, GLM | L375 | Mimo and GLM challenge it, with proposed wording for L375. |  |  |
| D11.5 | definition | 9 | Mimo | L217 | Mimo challenges it, with proposed wording for L217. |  |  |
| D12.1 | definition | 13, 14 | Mimo, GLM, case card | L195 | Mimo and GLM challenge it, with proposed wording for L195; also C02, C03, C04, on the same sentence. |  |  |
| D12.2 | definition | 13, 14 | external reader, case card | L197 | Challenged only by the external reader (E03) and the case card (C07), on the sentence it formalizes; no reader point challenges it. |  |  |
| D12.3 | definition | 13 | GLM, case card | L199 | GLM challenges it (the maths departs from the words, the text settles an invention, or a counterexample), with no wording for the text; also C01, on the same sentence. |  |  |
| D12.4 | definition | 13 | Mimo, GLM | L405, L409 | Mimo and GLM challenge it, with proposed wording for L405, L409. |  |  |
| D12.5 | definition | 13 | Mimo, case card | L205 | Mimo challenges it, with proposed wording for L205; also C03, on the same sentence. |  |  |
| D12.7 | definition | 13, 14 | Mimo, GLM | L220, L221 | Mimo and GLM challenge it, with proposed wording for L220, L221. |  |  |
| D12.8 | definition | 13, 14 | Mimo, GLM, case card | L225 | Mimo and GLM challenge it, with proposed wording for L225; also C05, on the same sentence. |  |  |
| D12.9 | definition | 13 | Mimo, GLM | L572 | Mimo and GLM challenge it, with proposed wording for L572. | yes |  |
| D13.1 | definition | 15 | Mimo, GLM | L403 | Mimo and GLM challenge it, with proposed wording for L403. |  |  |
| D13.3 | definition | 14, 15 | Mimo, GLM, external reader, case card | L405 | Mimo and GLM challenge it (the maths departs from the words, the text settles an invention, or a counterexample), with no wording for the text; also E03, C06, on the same sentence. |  |  |
| D13.4 | definition | 15 | Mimo | L413 | Mimo challenges it, with proposed wording for L413. |  |  |
| D13.6 | definition | 15, 17 | Mimo, GLM | L596 | Mimo and GLM challenge it, with proposed wording for L596. |  |  |
| D13.8 | definition | 15 | GLM | L429 | GLM challenges it, with proposed wording for L429. |  |  |
| D14.1 | definition | 15 | Mimo, GLM | L441 | Mimo and GLM challenge it, with proposed wording for L441. |  |  |
| D14.3 | definition | 15 | Mimo, GLM | L441 | Mimo and GLM challenge it, with proposed wording for L441. |  |  |
| D14.5 | definition | 15 | Mimo, GLM | L443 | Mimo and GLM challenge it, with proposed wording for L443. |  |  |
| D14.6 | definition | 15 | Mimo, GLM | L453 | Mimo and GLM challenge it, with proposed wording for L453. |  |  |
| D14.7 | definition | 15 | Mimo | L447, L448, L449 | Mimo challenges it (the maths departs from the words, the text settles an invention, or a counterexample), with no wording for the text. |  |  |
| D14.8 | definition | 15 | Mimo | L455 | Mimo challenges it (the maths departs from the words, the text settles an invention, or a counterexample), with no wording for the text. |  |  |
| D15.1 | definition | 16 | Mimo | L461 | Mimo challenges it (the maths departs from the words, the text settles an invention, or a counterexample), with no wording for the text. |  |  |
| D15.2 | definition | 16 | external reader | L466 | Challenged only by the external reader (E17), on the sentence it formalizes; no reader point challenges it. |  |  |
| D15.4 | definition | 16 | Mimo, external reader | L473 | Mimo challenges it (the maths departs from the words, the text settles an invention, or a counterexample), with no wording for the text; also E13, on the same sentence. |  |  |
| D15.5 | definition | 16, 17 | Mimo, GLM | L475 | Mimo and GLM challenge it, with proposed wording for L475. |  |  |
| D15.6 | definition | 16 | Mimo, GLM | L477 | Mimo and GLM challenge it (the maths departs from the words, the text settles an invention, or a counterexample), with no wording for the text. |  |  |
| D15.7 | definition | 16 | Mimo, GLM, external reader | L479 | Mimo and GLM challenge it, with proposed wording for L479; also E17, on the same sentence. |  |  |
| D15.8 | definition | 16 | Mimo, GLM | L481 | Mimo and GLM challenge it, with proposed wording for L481. |  |  |
| D16.1 | definition | 16 | Mimo, GLM | L487 | Mimo and GLM challenge it (the maths departs from the words, the text settles an invention, or a counterexample), with no wording for the text. |  |  |
| D16.2 | definition | 16 | Mimo, GLM | L492 | Mimo and GLM challenge it, with proposed wording for L492. |  |  |
| D16.3 | definition | 16 | external reader | L495 | Challenged only by the external reader (E17), on the sentence it formalizes; no reader point challenges it. |  |  |
| D16.4 | definition | 16 | Mimo, GLM | L528 | Mimo and GLM challenge it, with proposed wording for L528. |  | yes |
| D16.5 | definition | 16, 17 | Mimo, GLM | L528 | Mimo and GLM challenge it, with proposed wording for L528. |  |  |
| D18.1 | definition | 17 | Mimo, external reader | L526 | Mimo challenges it, with proposed wording for L526; also E03, on the same sentence. |  |  |
| E8 | encoding | 17 | external reader | L590 | Challenged only by the external reader (E20), on the sentence it formalizes; no reader point challenges it. |  |  |
| E9 | encoding | 17 | external reader | L622, L626 | Challenged only by the external reader (E10), on the sentence it formalizes; no reader point challenges it. |  |  |
| FC01 | claim | 1 | GLM | L255 | GLM challenges it, with proposed wording for L255. |  |  |
| FC02 | claim | 1 | Mimo, GLM, external reader | L109, L325 | Mimo and GLM challenge it, with proposed wording for L109, L325; also E04, on the same sentence. |  |  |
| FC05 | claim | 3 | Mimo, GLM, second check | L119 | Mimo and GLM challenge it, with proposed wording for L119; also one of the twelve (FC05). |  |  |
| FC06 | claim | 2 | Mimo | L119, L124 | Mimo challenges it (the maths departs from the words, the text settles an invention, or a counterexample), with no wording for the text. |  |  |
| FC07 | claim | 2 | Mimo, GLM, external reader | L119, L123, L124, L125, L127 | Mimo and GLM challenge it, with proposed wording for L119, L123, L124, L125, L127; also E05, on the same sentence. |  |  |
| FC08 | claim | 2 | Mimo, GLM, external reader | L124, L127 | Mimo and GLM challenge it, with proposed wording for L124, L127; also E05, on the same sentence. |  |  |
| FC09 | claim | 2 | Mimo | L121 | Mimo challenges it, with proposed wording for L121. |  |  |
| FC10 | claim | 2 | Mimo | L57 | Mimo challenges it, with proposed wording for L57. |  |  |
| FC11 | claim | 1 | GLM | L109 | GLM challenges it, with proposed wording for L109. |  |  |
| FC12 | claim | 2 | external reader | L124, L125 | Challenged only by the external reader (E05), on the sentence it formalizes; no reader point challenges it. |  |  |
| FC13 | claim | 2 | Mimo, external reader | L127 | Mimo challenges it, with proposed wording for L127; also E05, on the same sentence. |  |  |
| FC14 | claim | 2 | Mimo | L127 | Mimo challenges it (the maths departs from the words, the text settles an invention, or a counterexample), with no wording for the text. |  |  |
| FC15 | claim | 3 | Mimo, GLM | L554 | Mimo and GLM challenge it, with proposed wording for L554. |  |  |
| FC17 | claim | 3 | Mimo, GLM | L245 | Mimo and GLM challenge it, with proposed wording for L245. |  |  |
| FC18 | claim | 3 | Mimo, second check | L119, L556, L558 | Mimo challenges it, with proposed wording for L119, L556, L558; also one of the twelve (FC18). |  | yes |
| FC19 | claim | 5 | Mimo | L245 | Mimo challenges it, with proposed wording for L245. |  |  |
| FC20 | claim | 5 | Mimo, GLM, second check | L189, L220 | Mimo and GLM challenge it, with proposed wording for L189, L220; also one of the twelve (FC20). |  | yes |
| FC21 | claim | 7 | Mimo, GLM | L257 | Mimo and GLM challenge it, with proposed wording for L257. |  |  |
| FC23 | claim | 6 | Mimo, GLM, second check | L255 | Mimo and GLM challenge it, with proposed wording for L255; also one of the twelve (FC23 (b)). |  |  |
| FC24 | claim | 6 | GLM | L273 | GLM challenges it, with proposed wording for L273. |  |  |
| FC25 | claim | 7 | Mimo, GLM, second check | L269 | Mimo and GLM challenge it, with proposed wording for L269; also one of the twelve (FC25 (b)). |  |  |
| FC26 | claim | 7 | Mimo, GLM | L255, L257 | Mimo and GLM challenge it, with proposed wording for L255, L257. |  |  |
| FC27 | claim | 7 | Mimo | L271, L325 | Mimo challenges it (the maths departs from the words, the text settles an invention, or a counterexample), with no wording for the text. |  |  |
| FC28 | claim | 7 | Mimo, GLM | L325 | Mimo and GLM challenge it, with proposed wording for L325. |  |  |
| FC29 | claim | 7 | Mimo | L275 | Mimo challenges it (the maths departs from the words, the text settles an invention, or a counterexample), with no wording for the text. |  |  |
| FC30 | claim | 6 | Mimo | L43, L67, L277 | Mimo challenges it (the maths departs from the words, the text settles an invention, or a counterexample), with no wording for the text. |  |  |
| FC31 | claim | 6 | Mimo, GLM | L520 | Mimo and GLM challenge it, with proposed wording for L520. |  |  |
| FC32 | claim | 6 | Mimo, GLM | L526 | Mimo and GLM challenge it, with proposed wording for L526. |  |  |
| FC33 | claim | 6 | Mimo, GLM | L265 | Mimo and GLM challenge it, with proposed wording for L265. |  |  |
| FC34 | claim | 4 | Mimo, GLM | L151, L255 | Mimo and GLM challenge it, with proposed wording for L151, L255. |  |  |
| FC35 | claim | 4 | Mimo, GLM | L151 | Mimo and GLM challenge it, with proposed wording for L151. |  |  |
| FC36 | claim | 4 | Mimo, GLM | L151 | Mimo and GLM challenge it, with proposed wording for L151. |  |  |
| FC40 | claim | 9 | Mimo, GLM | L311 | Mimo and GLM challenge it, with proposed wording for L311. |  |  |
| FC41 | claim | 9 | Mimo | L313 | Mimo challenges it, with proposed wording for L313. |  |  |
| FC43 | claim | 10 | Mimo, GLM | L317 | Mimo and GLM challenge it (the maths departs from the words, the text settles an invention, or a counterexample), with no wording for the text. | yes |  |
| FC44 | claim | 10 | Mimo, GLM | L315 | Mimo and GLM challenge it, with proposed wording for L315. |  |  |
| FC46 | claim | 11 | Mimo | L317 | Mimo challenges it (the maths departs from the words, the text settles an invention, or a counterexample), with no wording for the text. |  |  |
| FC47 | claim | 11 | Mimo, GLM | L317 | Mimo and GLM challenge it (the maths departs from the words, the text settles an invention, or a counterexample), with no wording for the text. |  |  |
| FC48 | claim | 11 | Mimo, GLM | L315, L317 | Mimo and GLM challenge it, with proposed wording for L315, L317. |  |  |
| FC49 | claim | 11 | Mimo | L317 | Mimo challenges it, with proposed wording for L317. |  |  |
| FC50 | claim | 11 | Mimo | L317 | Mimo challenges it (the maths departs from the words, the text settles an invention, or a counterexample), with no wording for the text. |  |  |
| FC51 | claim | 11 | Mimo, GLM | L317, L568 | Mimo and GLM challenge it (the maths departs from the words, the text settles an invention, or a counterexample), with no wording for the text. |  |  |
| FC52 | claim | 10 | Mimo, GLM | L315 | Mimo and GLM challenge it, with proposed wording for L315. |  |  |
| FC53 | claim | 10 | Mimo | L315 | Mimo challenges it (the maths departs from the words, the text settles an invention, or a counterexample), with no wording for the text. |  |  |
| FC56 | claim | 12 | Mimo, GLM | L393 | Mimo and GLM challenge it, with proposed wording for L393. |  |  |
| FC57 | claim | 8 | Mimo | L329 | Mimo challenges it, with proposed wording for L329. |  |  |
| FC58 | claim | 8 | Mimo, GLM | L329 | Mimo and GLM challenge it, with proposed wording for L329. |  |  |
| FC60 | claim | 8 | Mimo, GLM | L331 | Mimo and GLM challenge it (the maths departs from the words, the text settles an invention, or a counterexample), with no wording for the text. |  |  |
| FC62 | claim | 8 | Mimo, GLM | L339 | Mimo and GLM challenge it, with proposed wording for L339. |  | yes |
| FC63 | claim | 8 | Mimo, GLM, second check | L343 | Mimo and GLM challenge it, with proposed wording for L343; also one of the twelve (FC63 (c-i)). |  | yes |
| FC64 | claim | 5 | Mimo | L353 | Mimo challenges it, with proposed wording for L353. |  |  |
| FC65 | claim | 5 | GLM | L361 | GLM challenges it, with proposed wording for L361. |  |  |
| FC66 | claim | 5 | Mimo | L363 | Mimo challenges it, with proposed wording for L363. |  |  |
| FC67 | claim | 5 | Mimo, GLM | L365 | Mimo and GLM challenge it, with proposed wording for L365. |  |  |
| FC68 | claim | 12 | Mimo, GLM | L369 | Mimo and GLM challenge it (the maths departs from the words, the text settles an invention, or a counterexample), with no wording for the text. |  |  |
| FC69 | claim | 12 | Mimo, GLM | L393 | Mimo and GLM challenge it, with proposed wording for L393. |  |  |
| FC70 | claim | 12 | Mimo, GLM | L393 | Mimo and GLM challenge it, with proposed wording for L393. |  |  |
| FC71 | claim | 12 | Mimo, GLM | L395 | Mimo and GLM challenge it, with proposed wording for L395. |  |  |
| FC72 | claim | 12 | Mimo | L397 | Mimo challenges it, with proposed wording for L397. |  |  |
| FC74 | claim | 12 | Mimo | L383 | Mimo challenges it (the maths departs from the words, the text settles an invention, or a counterexample), with no wording for the text. |  |  |
| FC75 | claim | 9 | Mimo, GLM | L375 | Mimo and GLM challenge it, with proposed wording for L375. |  |  |
| FC76 | claim | 12 | Mimo | L385 | Mimo challenges it, with proposed wording for L385. |  |  |
| FC77 | claim | 13 | Mimo, GLM, second check | L195 | Mimo and GLM challenge it, with proposed wording for L195; also one of the twelve (FC77). |  |  |
| FC78 | claim | 13 | GLM, case card, second check | L193, L195, L201 | GLM challenges it, with proposed wording for L193; also C01, C11, on the same sentence; also one of the twelve (FC78, FC81 (d) and FC82, one finding). |  |  |
| FC79 | claim | 13 | GLM | L41 | GLM challenges it, with proposed wording for L41. |  |  |
| FC80 | claim | 14 | Mimo | L572, L574 | Mimo challenges it (the maths departs from the words, the text settles an invention, or a counterexample), with no wording for the text. |  |  |
| FC81 | claim | 14 | Mimo, GLM, second check | L193, L195, L201 | Mimo and GLM challenge it, with proposed wording for L195; also one of the twelve (FC78, FC81 (d) and FC82, one finding). |  |  |
| FC82 | claim | 14 | GLM, case card, second check | L193, L195, L201, L225 | GLM challenges it, with proposed wording for L195, L225; also C05, on the same sentence; also one of the twelve (FC78, FC81 (d) and FC82, one finding). |  |  |
| FC83 | claim | 14 | Mimo, GLM, second check | L225 | Mimo and GLM challenge it, with proposed wording for L225; also one of the twelve (FC83). |  | yes |
| FC84 | claim | 15 | external reader | L47 | Challenged only by the external reader (E14), on the sentence it formalizes; no reader point challenges it. |  |  |
| FC85 | claim | 15 | Mimo, GLM | L413 | Mimo and GLM challenge it, with proposed wording for L413. |  |  |
| FC86 | claim | 15 | Mimo, GLM | L441 | Mimo and GLM challenge it, with proposed wording for L441. |  |  |
| FC87 | claim | 15 | Mimo, GLM | L441 | Mimo and GLM challenge it, with proposed wording for L441. |  |  |
| FC88 | claim | 15 | Mimo | L441 | Mimo challenges it, with proposed wording for L441. |  |  |
| FC89 | claim | 15 | GLM | L453 | GLM challenges it, with proposed wording for L453. |  |  |
| FC90 | claim | 15 | GLM | L628 | GLM challenges it, with proposed wording for L628. |  |  |
| FC91 | claim | 16 | Mimo, GLM | L471 | Mimo and GLM challenge it, with proposed wording for L471. |  |  |
| FC92 | claim | 16 | Mimo | L469 | Mimo challenges it, with proposed wording for L469. |  |  |
| FC93 | claim | 16 | GLM | L479 | GLM challenges it, with proposed wording for L479. |  |  |
| FC94 | claim | 16 | Mimo, GLM | L509 | Mimo and GLM challenge it (the maths departs from the words, the text settles an invention, or a counterexample), with no wording for the text. |  |  |
| FC95 | claim | 13 | GLM | L211 | GLM challenges it, with proposed wording for L211. |  |  |
| FC96 | claim | 5 | Mimo | L562 | Mimo challenges it, with proposed wording for L562. |  |  |
| FC97 | claim | 17 | Mimo, GLM, external reader | L590 | Mimo and GLM challenge it, with proposed wording for L590; also E20, on the same sentence. |  |  |
| FC98 | claim | 17 | Mimo, GLM, external reader | L526, L596 | Mimo and GLM challenge it, with proposed wording for L526, L596; also E03, on the same sentence. |  | yes |
| FC99 | claim | 17 | Mimo | L606 | Mimo challenges it (the maths departs from the words, the text settles an invention, or a counterexample), with no wording for the text. |  |  |
| FC100 | claim | 17 | Mimo | L612 | Mimo challenges it, with proposed wording for L612. |  |  |
| FC101 | claim | 17 | Mimo | L616 | Mimo challenges it (the maths departs from the words, the text settles an invention, or a counterexample), with no wording for the text. |  |  |
| FC102 | claim | 17 | Mimo, GLM, external reader, second check | L620, L622, L624, L626 | Mimo and GLM challenge it, with proposed wording for L620, L622, L624, L626; also E10, on the same sentence; also one of the twelve (FC102 (b), second half). |  | yes |
| FC103 | claim | 17 | Mimo, GLM | L630 | Mimo and GLM challenge it, with proposed wording for L630. |  |  |
| FC104 | claim | 5 | Mimo, GLM | L220, L245, L247, L520 | Mimo and GLM challenge it, with proposed wording for L220, L245, L247, L520. |  |  |
| FC105 | claim | 9 | GLM | L161, L169, L604 | GLM challenges it (the maths departs from the words, the text settles an invention, or a counterexample), with no wording for the text. |  | yes |
| FC106 | claim | 4 | Mimo, GLM | L161 | Mimo and GLM challenge it (the maths departs from the words, the text settles an invention, or a counterexample), with no wording for the text. |  |  |
| FC107 | claim | 4 | Mimo, GLM | L161 | Mimo and GLM challenge it, with proposed wording for L161. |  | yes |
| I01 | invention | 1 | Mimo, GLM | L91 | Mimo and GLM challenge it, with proposed wording for L91. |  |  |
| I02 | invention | 1 | Mimo, GLM | L91, L574 | Mimo and GLM challenge it (the maths departs from the words, the text settles an invention, or a counterexample), with no wording for the text. |  |  |
| I03 | invention | 1, 7, 8 | Mimo, GLM | L103, L255, L339 | Mimo and GLM challenge it, with proposed wording for L103, L255, L339. |  |  |
| I04 | invention | 1, 7 | Mimo, GLM, external reader | L103, L109 | Mimo and GLM challenge it, with proposed wording for L103, L109; also E04, on the same sentence. |  |  |
| I05 | invention | 1 | Mimo, GLM, external reader | L109 | Mimo and GLM challenge it, with proposed wording for L109; also E04, on the same sentence. |  |  |
| I06 | invention | 2 | Mimo, GLM, external reader | L109 | Mimo and GLM challenge it, with proposed wording for L109; also E05, on the same sentence. |  |  |
| I07 | invention | 2 | Mimo, GLM, external reader | L124 | Mimo and GLM challenge it, with proposed wording for L124; also E05, on the same sentence. |  |  |
| I08 | invention | 2 | Mimo, GLM | L125 | Mimo and GLM challenge it, with proposed wording for L125. |  |  |
| I09 | invention | 2 | Mimo, GLM | L57, L119 | Mimo and GLM challenge it, with proposed wording for L57, L119. |  |  |
| I10 | invention | 3 | Mimo, GLM | L119 | Mimo and GLM challenge it, with proposed wording for L119. |  | yes |
| I11 | invention | 3 | Mimo, GLM | L119 | Mimo and GLM challenge it, with proposed wording for L119. |  |  |
| I12 | invention | 3 | Mimo, GLM | L119, L554 | Mimo and GLM challenge it, with proposed wording for L119, L554. |  |  |
| I13 | invention | 3 | Mimo, GLM | L556 | Mimo and GLM challenge it, with proposed wording for L556. |  |  |
| I14 | invention | 3, 5, 7 | Mimo, GLM | L189, L233 | Mimo and GLM challenge it, with proposed wording for L189, L233. |  | yes |
| I15 | invention | 5 | Mimo, GLM | L231 | Mimo and GLM challenge it, with proposed wording for L231. |  |  |
| I16 | invention | 5 | Mimo, GLM | L189 | Mimo and GLM challenge it, with proposed wording for L189. |  |  |
| I17 | invention | 5 | Mimo, GLM | L189, L315 | Mimo and GLM challenge it, with proposed wording for L189, L315. |  |  |
| I18 | invention | 5, 13 | Mimo, GLM | L242 | Mimo and GLM challenge it, with proposed wording for L242. |  |  |
| I19 | invention | 10 | Mimo, GLM | L315 | Mimo and GLM challenge it, with proposed wording for L315. |  |  |
| I20 | invention | 4, 5 | Mimo, GLM | L138, L231, L253 | Mimo and GLM challenge it, with proposed wording for L138, L231, L253. |  |  |
| I21 | invention | 5, 6 | Mimo, GLM | L141, L250 | Mimo and GLM challenge it, with proposed wording for L141, L250. |  |  |
| I22 | invention | 6 | Mimo, GLM | L255 | Mimo and GLM challenge it, with proposed wording for L255. |  |  |
| I24 | invention | 6 | Mimo, GLM, external reader | L255 | Mimo and GLM challenge it, with proposed wording for L255; also E19, on the same sentence. |  |  |
| I25 | invention | 6 | Mimo, GLM | L255 | Mimo and GLM challenge it (the maths departs from the words, the text settles an invention, or a counterexample), with no wording for the text. |  |  |
| I26 | invention | 7 | Mimo, GLM | L257 | Mimo and GLM challenge it, with proposed wording for L257. |  |  |
| I27 | invention | 4, 8 | Mimo, GLM | L257 | Mimo and GLM challenge it, with proposed wording for L257. |  |  |
| I28 | invention | 6 | GLM | L255 | GLM challenges it (the maths departs from the words, the text settles an invention, or a counterexample), with no wording for the text. |  |  |
| I29 | invention | 9 | Mimo, GLM, external reader | L287 | Mimo and GLM challenge it, with proposed wording for L287; also E02, on the same sentence. |  |  |
| I30 | invention | 9 | Mimo, GLM | L307 | Mimo and GLM challenge it (the maths departs from the words, the text settles an invention, or a counterexample), with no wording for the text. |  |  |
| I31 | invention | 9 | Mimo, GLM | L311 | Mimo and GLM challenge it, with proposed wording for L311. |  |  |
| I32 | invention | 6, 7 | GLM | L269 | GLM challenges it, with proposed wording for L269. |  |  |
| I33 | invention | 10 | Mimo, GLM | L315 | Mimo and GLM challenge it, with proposed wording for L315. |  |  |
| I34 | invention | 10 | Mimo, GLM | L315 | Mimo and GLM challenge it, with proposed wording for L315. |  |  |
| I35 | invention | 10 | Mimo, GLM | L315 | Mimo and GLM challenge it (the maths departs from the words, the text settles an invention, or a counterexample), with no wording for the text. |  |  |
| I36 | invention | 10 | Mimo, GLM | L315 | Mimo and GLM challenge it, with proposed wording for L315. |  |  |
| I37 | invention | 11 | Mimo, GLM | L317 | Mimo and GLM challenge it, with proposed wording for L317. |  |  |
| I38 | invention | 12 | Mimo, GLM | L397 | Mimo and GLM challenge it, with proposed wording for L397. |  |  |
| I39 | invention | 12 | Mimo, GLM | L397 | Mimo and GLM challenge it, with proposed wording for L397. |  |  |
| I40 | invention | 12 | Mimo, GLM | L393 | Mimo and GLM challenge it, with proposed wording for L393. |  |  |
| I41 | invention | 12 | Mimo, GLM | L393 | Mimo and GLM challenge it (the maths departs from the words, the text settles an invention, or a counterexample), with no wording for the text. |  |  |
| I42 | invention | 12 | Mimo, GLM | L393 | Mimo and GLM challenge it, with proposed wording for L393. |  |  |
| I43 | invention | 12 | Mimo, GLM | L395 | Mimo and GLM challenge it, with proposed wording for L395. |  |  |
| I44 | invention | 9 | Mimo, GLM | L375 | Mimo and GLM challenge it, with proposed wording for L375. |  |  |
| I45 | invention | 9 | Mimo, GLM | L169 | Mimo and GLM challenge it, with proposed wording for L169. |  | yes |
| I46 | invention | 9 | Mimo, GLM | L375 | Mimo and GLM challenge it, with proposed wording for L375. |  |  |
| I47 | invention | 12 | Mimo, GLM | L385 | Mimo and GLM challenge it, with proposed wording for L385. |  |  |
| I48 | invention | 13 | Mimo, GLM | L169, L205 | Mimo and GLM challenge it, with proposed wording for L169, L205. |  |  |
| I49 | invention | 5 | Mimo, GLM | L220, L245, L247, L520 | Mimo and GLM challenge it, with proposed wording for L220, L245, L247, L520. |  |  |
| I50 | invention | 5, 14 | Mimo, GLM | L220 | Mimo and GLM challenge it, with proposed wording for L220. |  | yes |
| I51 | invention | 4 | Mimo, GLM | L151, L219 | Mimo and GLM challenge it, with proposed wording for L151, L219. |  |  |
| I52 | invention | 13, 14, 17 | Mimo, GLM, case card | L195 | Mimo and GLM challenge it, with proposed wording for L195; also C04, on the same sentence. | yes |  |
| I53 | invention | 13, 14 | Mimo, GLM, case card | L195, L409 | Mimo and GLM challenge it, with proposed wording for L195, L409; also C01, on the same sentence. |  |  |
| I54 | invention | 13 | Mimo, GLM | L405, L409 | Mimo and GLM challenge it, with proposed wording for L405, L409. |  |  |
| I55 | invention | 15 | Mimo, GLM | L403 | Mimo and GLM challenge it, with proposed wording for L403. |  |  |
| I56 | invention | 13, 14 | Mimo, GLM, external reader, case card | L225, L405 | Mimo and GLM challenge it, with proposed wording for L225, L405; also E03, C06, on the same sentence. |  |  |
| I57 | invention | 15 | Mimo, GLM | L441 | Mimo and GLM challenge it, with proposed wording for L441. |  |  |
| I58 | invention | 15 | Mimo, GLM | L441 | Mimo and GLM challenge it, with proposed wording for L441. |  |  |
| I59 | invention | 15 | Mimo, GLM | L443 | Mimo and GLM challenge it, with proposed wording for L443. |  | yes |
| I60 | invention | 15 | Mimo, GLM | L453 | Mimo and GLM challenge it, with proposed wording for L453. |  |  |
| I61 | invention | 16 | Mimo, GLM | L469, L471 | Mimo and GLM challenge it, with proposed wording for L469, L471. |  |  |
| I62 | invention | 16 | Mimo, GLM | L479 | Mimo and GLM challenge it, with proposed wording for L479. |  | yes |
| I63 | invention | 8 | Mimo, GLM | L329 | Mimo and GLM challenge it, with proposed wording for L329. |  |  |
| I64 | invention | 8 | Mimo, GLM | L329 | Mimo and GLM challenge it, with proposed wording for L329. |  |  |
| I65 | invention | 7 | Mimo, GLM | L325 | Mimo and GLM challenge it, with proposed wording for L325. |  | yes |
| I66 | invention | 8 | Mimo, GLM | L343 | Mimo and GLM challenge it, with proposed wording for L343. |  |  |
| I67 | invention | 17 | Mimo, GLM, external reader | L590 | Mimo and GLM challenge it, with proposed wording for L590; also E20, on the same sentence. |  | yes |
| I68 | invention | 15, 17 | Mimo, external reader | L622 | Mimo challenges it, with proposed wording for L622; also E10, on the same sentence. |  |  |
| I69 | invention | 17 | Mimo, GLM | L630 | Mimo and GLM challenge it, with proposed wording for L630. |  |  |
| I70 | invention | 17 | Mimo, GLM | L612 | Mimo and GLM challenge it, with proposed wording for L612. |  |  |
| I71 | invention | 13 | GLM | L572 | GLM challenges it, with proposed wording for L572. | yes |  |
| I72 | invention | 4 | Mimo, GLM | L151 | Mimo and GLM challenge it, with proposed wording for L151. |  |  |
| I73 | invention | 4 | Mimo, GLM | L151 | Mimo and GLM challenge it, with proposed wording for L151. |  |  |
| I74 | invention | 16 | Mimo, GLM | L492 | Mimo and GLM challenge it, with proposed wording for L492. |  |  |
| I75 | invention | 16 | Mimo, GLM | L497 | Mimo and GLM challenge it, with proposed wording for L497. |  |  |
| I76 | invention | 4 | Mimo, GLM | L161 | Mimo and GLM challenge it, with proposed wording for L161. |  |  |
| I79 | invention | 4, 6 | Mimo, GLM | L255, L325 | Mimo and GLM challenge it (the maths departs from the words, the text settles an invention, or a counterexample), with no wording for the text. |  | yes |
| I80 | invention | 1 | Mimo, GLM | L109 | Mimo and GLM challenge it, with proposed wording for L109. |  |  |
| I81 | invention | 3, 5, 6, 8, 13 | Mimo | L189 | Mimo challenges it, with proposed wording for L189. |  |  |
| I82 | invention | 6, 8 | GLM | L141 | GLM challenges it (the maths departs from the words, the text settles an invention, or a counterexample), with no wording for the text. |  |  |
| I83 | invention | 6 | Mimo, GLM | L255 | Mimo and GLM challenge it, with proposed wording for L255. |  |  |
| I84 | invention | 5 | Mimo, GLM | L242 | Mimo and GLM challenge it, with proposed wording for L242. |  |  |
| I86 | invention | 10 | Mimo | L315 | Mimo challenges it (the maths departs from the words, the text settles an invention, or a counterexample), with no wording for the text. |  |  |
| I87 | invention | 8 | GLM | L397 | GLM challenges it (the maths departs from the words, the text settles an invention, or a counterexample), with no wording for the text. |  |  |
| I88 | invention | 10 | Mimo, GLM | L397 | Mimo and GLM challenge it, with proposed wording for L397. |  | yes |
| I89 | invention | 8 | GLM | L387, L393 | GLM challenges it (the maths departs from the words, the text settles an invention, or a counterexample), with no wording for the text. |  |  |
| I92 | invention | 7, 13, 14 | Mimo, GLM | L325 | Mimo and GLM challenge it, with proposed wording for L325. |  |  |
| I93 | invention | 3 | Mimo, GLM | L119 | Mimo and GLM challenge it, with proposed wording for L119. |  |  |
| I94 | invention | 3 | Mimo, GLM | L119 | Mimo and GLM challenge it, with proposed wording for L119. |  |  |
| I95 | invention | 9 | Mimo, GLM | L375 | Mimo and GLM challenge it, with proposed wording for L375. |  |  |
| I99 | invention | 8 | Mimo, GLM | L343 | Mimo and GLM challenge it, with proposed wording for L343. |  | yes |
| I100 | invention | 17 | Mimo, GLM, external reader | L620 | Mimo and GLM challenge it, with proposed wording for L620; also E10, on the same sentence. |  | yes |
| I102 | invention | 2 | Mimo, GLM | L123, L124 | Mimo and GLM challenge it, with proposed wording for L123, L124. |  |  |
| U1 | U-entry | 5 | Mimo | L250 | Mimo challenges it, with proposed wording for L250. |  |  |
| U4 | U-entry | 3 | Mimo, GLM | L119 | Mimo and GLM challenge it, with proposed wording for L119. |  |  |
| U5 | U-entry | 2 | Mimo, GLM | L124 | Mimo and GLM challenge it, with proposed wording for L124. |  |  |
| U6 | U-entry | 4 | GLM | L255 | GLM challenges it, with proposed wording for L255. |  |  |
| H01 | H-entry | 2 | Mimo, GLM | L119 | Mimo and GLM challenge it, with proposed wording for L119. |  |  |
| H02 | H-entry | 2 | Mimo, GLM | L123 | Mimo and GLM challenge it, with proposed wording for L123. |  |  |
| H03 | H-entry | 1 | Mimo, GLM | L103 | Mimo and GLM challenge it, with proposed wording for L103. |  |  |
| H04 | H-entry | 1 | Mimo, GLM | L109 | Mimo and GLM challenge it (the maths departs from the words, the text settles an invention, or a counterexample), with no wording for the text. |  |  |
| H05 | H-entry | 13 | Mimo, GLM, case card | L193, L195, L197, L201, L411 | Mimo and GLM challenge it (the maths departs from the words, the text settles an invention, or a counterexample), with no wording for the text; also C02, on the same sentence. |  |  |
| H06 | H-entry | 15 | Mimo, GLM, case card | L55, L429 | Mimo and GLM challenge it, with proposed wording for L55, L429; also C07, on the same sentence. |  | yes |
| H07 | H-entry | 14 | Mimo, GLM | L217, L221 | Mimo and GLM challenge it (the maths departs from the words, the text settles an invention, or a counterexample), with no wording for the text. |  |  |
| H08 | H-entry | 14 | Mimo, GLM, case card | L225 | Mimo and GLM challenge it, with proposed wording for L225; also C05, on the same sentence. |  |  |
| H09 | H-entry | 13 | Mimo, GLM | L481 | Mimo and GLM challenge it (the maths departs from the words, the text settles an invention, or a counterexample), with no wording for the text. |  |  |
| H10 | H-entry | 11 | Mimo, GLM | L315 | Mimo and GLM challenge it, with proposed wording for L315. |  |  |
| H11 | H-entry | 9 | Mimo, GLM | L375 | Mimo and GLM challenge it, with proposed wording for L375. |  |  |
| H12 | H-entry | 12 | Mimo, GLM | L377 | Mimo and GLM challenge it, with proposed wording for L377. |  |  |
| H13 | H-entry | 13 | Mimo, GLM | L195, L217 | Mimo and GLM challenge it, with proposed wording for L195, L217. |  |  |
| H14 | H-entry | 15 | Mimo, GLM | L427 | Mimo and GLM challenge it (the maths departs from the words, the text settles an invention, or a counterexample), with no wording for the text. |  |  |
| H15 | H-entry | 15 | Mimo, GLM | L429 | Mimo and GLM challenge it, with proposed wording for L429. |  |  |
| H16 | H-entry | 16 | Mimo, GLM | L487 | Mimo and GLM challenge it (the maths departs from the words, the text settles an invention, or a counterexample), with no wording for the text. |  | yes |
| H17 | H-entry | 17 | Mimo, GLM, external reader | L620, L622 | Mimo and GLM challenge it, with proposed wording for L620, L622; also E10, on the same sentence. |  |  |
| H18 | H-entry | 17 | Mimo, GLM | L103 | Mimo and GLM challenge it (the maths departs from the words, the text settles an invention, or a counterexample), with no wording for the text. |  |  |
| H19 | H-entry | 9 | Mimo, GLM | L375 | Mimo and GLM challenge it, with proposed wording for L375. |  |  |
| NF01 | NF entry | 17 | external reader | L17 | Challenged only by the external reader (E06, E22), on the sentence it formalizes; no reader point challenges it. |  |  |
| NF02 | NF entry | 17 | external reader | L536 | Challenged only by the external reader (E06), on the sentence it formalizes; no reader point challenges it. |  |  |
| NF03 | NF entry | 17 | external reader | L538 | Challenged only by the external reader (E06, E15), on the sentence it formalizes; no reader point challenges it. |  |  |
| NF05 | NF entry | 17 | external reader | L542 | Challenged only by the external reader (E14), on the sentence it formalizes; no reader point challenges it. |  |  |
| NF07 | NF entry | 15 | external reader, case card | L201 | Challenged only by the external reader (E14) and the case card (C02), on the sentence it formalizes; no reader point challenges it. |  |  |
| NF11 | NF entry | 16 | Mimo, external reader | L495 | Mimo challenges it (the maths departs from the words, the text settles an invention, or a counterexample), with no wording for the text; also E17, on the same sentence. |  |  |
| matter 1 | round-1 matter | 3 | Mimo, GLM | L554, L556 | Mimo and GLM challenge it, with proposed wording for L554, L556. |  |  |
| matter 2 | round-1 matter | 9 | Mimo, GLM | L169 | Mimo and GLM challenge it, with proposed wording for L169. |  |  |
| matter 3 | round-1 matter | 14 | Mimo, GLM | L584 | Mimo and GLM challenge it, with proposed wording for L584. |  |  |
| matter 4 | round-1 matter | 2 | Mimo, GLM | L121 | Mimo and GLM challenge it, with proposed wording for L121. |  |  |
| matter 5 | round-1 matter | 1 | Mimo, GLM | L109, L113 | Mimo and GLM challenge it, with proposed wording for L109, L113. |  |  |
| matter 6 | round-1 matter | 4 | Mimo, GLM | L151 | Mimo and GLM challenge it, with proposed wording for L151. |  | yes |
| matter 7 | round-1 matter | 6 | Mimo, GLM | L273 | Mimo and GLM challenge it, with proposed wording for L273. |  |  |
| matter 8 | round-1 matter | 9 | Mimo, GLM | L311 | Mimo and GLM challenge it, with proposed wording for L311. |  |  |
| matter 9 | round-1 matter | 12 | Mimo, GLM | L393 | Mimo and GLM challenge it, with proposed wording for L393. |  |  |
| matter 10 | round-1 matter | 16 | Mimo, GLM | L471 | Mimo and GLM challenge it, with proposed wording for L471. |  |  |
| matter 11 | round-1 matter | 9 | Mimo, GLM | L375, L385 | Mimo and GLM challenge it, with proposed wording for L375, L385. |  |  |
| matter 12 | round-1 matter | 5 | Mimo, GLM | L220, L245, L247, L520 | Mimo and GLM challenge it, with proposed wording for L220, L245, L247, L520. |  |  |
| matter 13 | round-1 matter | 9 | Mimo | L311 | Mimo challenges it, with proposed wording for L311. |  |  |
| matter 14 | round-1 matter | 16 | Mimo, GLM | L27 | Mimo and GLM challenge it, with proposed wording for L27. |  |  |
| L123 | round-1 change | 1, 2 | Mimo, GLM | L109, L123 | Mimo and GLM challenge it, with proposed wording for L109, L123. |  |  |
| L443 | round-1 change | 15 | Mimo, GLM | L443, L453, L628 | Mimo and GLM challenge it, with proposed wording for L443, L453, L628. |  |  |
| L471 | round-1 change | 16 | Mimo | L471 | Mimo challenges it, with proposed wording for L471. |  |  |
| L520 | round-1 change | 5, 6 | Mimo, GLM | L520 | Mimo and GLM challenge it, with proposed wording for L520. |  |  |
| E02 | external finding | — | external reader | L287, L296, L299, L305, L313 | The external reader's finding challenges the text (addendum point 4). |  |  |
| E03 | external finding | — | external reader | L197, L405, L526 | The external reader's finding challenges the text (addendum point 4). |  |  |
| E04 | external finding | — | external reader | L103, L109, L119 | The external reader's finding challenges the text (addendum point 4). |  |  |
| E05 | external finding | — | external reader | L121, L123, L124, L125, L127 | The external reader's finding may challenge the text (in doubt) (addendum point 4). |  |  |
| E06 | external finding | — | external reader | L17, L536, L538 | The external reader's finding challenges the text (addendum point 4). |  |  |
| E10 | external finding | — | external reader | L622, L626 | The external reader's finding challenges the text (addendum point 4). |  |  |
| E13 | external finding | — | external reader | L159, L473, L522 | The external reader's finding may challenge the text (in doubt) (addendum point 4). |  |  |
| E14 | external finding | — | external reader | L47, L77, L201, L542 | The external reader's finding may challenge the text (in doubt) (addendum point 4). |  |  |
| E15 | external finding | — | external reader | L277, L363, L538 | The external reader's finding may challenge the text (in doubt) (addendum point 4). |  |  |
| E17 | external finding | — | external reader | L466, L479, L495 | The external reader's finding challenges the text (addendum point 4). |  |  |
| E19 | external finding | — | external reader | L255 | The external reader's finding challenges the text (addendum point 4). |  |  |
| E20 | external finding | — | external reader | L425, L590 | The external reader's finding may challenge the text (in doubt) (addendum point 4). |  |  |
| E22 | external finding | — | external reader | L3, L17 | The external reader's finding may challenge the text (in doubt) (addendum point 4). |  |  |
| C01 | case card item | — | case card | L13, L193, L199 | The case card marks it yes (creative transport addendum, point 2). |  |  |
| C02 | case card item | — | case card | L195, L201, L411 | The case card marks it yes (creative transport addendum, point 2). |  |  |
| C03 | case card item | — | case card | L195, L205, L211 | The case card marks it in doubt (creative transport addendum, point 2). |  |  |
| C04 | case card item | — | case card | L195 | The case card marks it in doubt (creative transport addendum, point 2). |  |  |
| C05 | case card item | — | case card | L225 | The case card marks it in doubt (creative transport addendum, point 2). |  |  |
| C06 | case card item | — | case card | L405, L409 | The case card marks it in doubt (creative transport addendum, point 2). |  |  |
| C07 | case card item | — | case card | L55, L197 | The case card marks it in doubt (creative transport addendum, point 2). |  |  |
| C11 | case card item | — | case card | L193 | The case card marks it in doubt (creative transport addendum, point 2). |  |  |

**The twelve counterexamples** (rule 5, second kind), each going to a checker whether or not a reader raised it: FC05 (part 3); FC18 (part 3); FC20 (part 5); FC23 (b) (part 6); FC25 (b) (part 7); FC63 (c-i) (part 8); FC77 (part 13); FC78, FC81 (d) and FC82, one finding (parts 13 and 14); FC83 (part 14); FC102 (b), second half (part 17). Every one of them was also raised by at least one reader; the table's "raised by" names who.

**Context items** (no checker by themselves; given to the checker of any group whose lines they name): E01 (L159, L211, L245, L367, L407, L409); E07 (L37, L127, L151, L159, L606); E08 (L25, L221, L223, L584); E09 (L405, L407, L409, L429, L632); E11 (L13, L225, L584); E12 (L15, L544, L588, L592); E16 (L8, L393, L397, L429); E18 (L269, L536); E21 (L305); C08 (L217, L219, L220, L221, L223); C09 (L413, L416, L473); C10 (L429, L441, L443, L453, L522, L534); C12 (L231, L262, L466); C13 (L195, L481, L572, L574, L576); C14 (L427, L441); H20 (L155, L317, L422, L475, L528). H20 (part 17) is listed here because its five sub-items are tabulated, and go to checkers, under their own ids (D3.4, D13.6, D10.3, D15.5, D16.5).


## 6. Rule 7's records

Every item of the parts that no point of either reader challenges, that is not one of the twelve, and that no external finding and no card item challenges (addendum point 10; creative transport addendum, point 6). Both readers' replies came back for every part, so the second and third forms of rule 7 do not arise. An item addressed in one part and challenged in another goes to a checker and is not listed here. The places of the external findings and card items that go to a checker were compared with each item's lines; where the finding bears on the sentence the item formalizes, the item goes to a checker (listed in section 5 with "external reader" or "case card" among who raised it). The external reader's silence records nothing (addendum point 10).

| id | kind | parts | record |
|---|---|---|---|
| D0.1 | definition | 17 | not challenged by either reader; not thereby final (no point) |
| D0.2 | definition | 17 | not challenged by either reader; not thereby final (no point) |
| D1.2 | definition | 1 | not challenged by either reader; not thereby final (addressed without challenge) |
| D1.4 | definition | 1 | not challenged by either reader; not thereby final (addressed without challenge) |
| D4.1 | definition | 2, 3 | not challenged by either reader; not thereby final (addressed without challenge) |
| D6.1 | definition | 6 | not challenged by either reader; not thereby final (addressed without challenge) |
| D6.2 | definition | 6 | not challenged by either reader; not thereby final (addressed without challenge) |
| D7.2 | definition | 9 | not challenged by either reader; not thereby final (addressed without challenge) |
| D8.4 | definition | 10 | not challenged by either reader; not thereby final (addressed without challenge) |
| D8.6 | definition | 10 | not challenged by either reader; not thereby final (addressed without challenge) |
| D9.2 | definition | 12 | not challenged by either reader; not thereby final (addressed without challenge) |
| D9.3 | definition | 12 | not challenged by either reader; not thereby final (addressed without challenge) |
| D9.8 | definition | 11, 12 | not challenged by either reader; not thereby final (addressed without challenge) |
| D12.6 | definition | 4, 13, 14 | not challenged by either reader; not thereby final (addressed without challenge) |
| D13.2 | definition | 15 | not challenged by either reader; not thereby final (addressed without challenge) |
| D13.5 | definition | 15 | not challenged by either reader; not thereby final (addressed without challenge) |
| D13.7 | definition | 15 | not challenged by either reader; not thereby final (addressed without challenge) |
| D14.2 | definition | 15 | not challenged by either reader; not thereby final (addressed without challenge) |
| D14.4 | definition | 15 | not challenged by either reader; not thereby final (addressed without challenge) |
| D15.3 | definition | 16 | not challenged by either reader; not thereby final (addressed without challenge) |
| D18.2 | definition | 17 | not challenged by either reader; not thereby final (addressed without challenge) |
| E1 | encoding | 1, 2, 7 | not challenged by either reader; not thereby final (addressed without challenge) |
| E2 | encoding | 8 | not challenged by either reader; not thereby final (addressed without challenge) |
| E3 | encoding | 8 | not challenged by either reader; not thereby final (no point) |
| E4 | encoding | 8 | not challenged by either reader; not thereby final (addressed without challenge) |
| E5 | encoding | 8 | not challenged by either reader; not thereby final (addressed without challenge) |
| E6 | encoding | 8 | not challenged by either reader; not thereby final (addressed without challenge) |
| E7 | encoding | 5 | not challenged by either reader; not thereby final (addressed without challenge) |
| FC03 | claim | 3 | not challenged by either reader; not thereby final (addressed without challenge) |
| FC04 | claim | 3 | not challenged by either reader; not thereby final (addressed without challenge) |
| FC16 | claim | 3 | not challenged by either reader; not thereby final (addressed without challenge) |
| FC22 | claim | 6 | not challenged by either reader; not thereby final (addressed without challenge) |
| FC37 | claim | 9 | not challenged by either reader; not thereby final (addressed without challenge) |
| FC38 | claim | 9 | not challenged by either reader; not thereby final (addressed without challenge) |
| FC39 | claim | 9 | not challenged by either reader; not thereby final (addressed without challenge) |
| FC42 | claim | 9 | not challenged by either reader; not thereby final (addressed without challenge) |
| FC45 | claim | 10 | not challenged by either reader; not thereby final (addressed without challenge) |
| FC54 | claim | 10 | not challenged by either reader; not thereby final (addressed without challenge) |
| FC55 | claim | 11 | not challenged by either reader; not thereby final (addressed without challenge) |
| FC59 | claim | 8 | not challenged by either reader; not thereby final (addressed without challenge) |
| FC61 | claim | 8 | not challenged by either reader; not thereby final (addressed without challenge) |
| FC73 | claim | 12 | not challenged by either reader; not thereby final (addressed without challenge) |
| FC108 | claim | 6 | not challenged by either reader; not thereby final (addressed without challenge) |
| FC109 | claim | 17 | not challenged by either reader; not thereby final (addressed without challenge) |
| FC110 | claim | 16 | not challenged by either reader; not thereby final (addressed without challenge) |
| I23 | invention | 6 | not challenged by either reader; not thereby final (addressed without challenge) |
| I77 | invention | 1 | not challenged by either reader; not thereby final (addressed without challenge) |
| I78 | invention | 1 | not challenged by either reader; not thereby final (addressed without challenge) |
| I85 | invention | 4 | not challenged by either reader; not thereby final (addressed without challenge) |
| I90 | invention | 13, 14 | not challenged by either reader; not thereby final (addressed without challenge) |
| I91 | invention | 9 | not challenged by either reader; not thereby final (addressed without challenge) |
| I96 | invention | 15 | not challenged by either reader; not thereby final (addressed without challenge) |
| I97 | invention | 16 | not challenged by either reader; not thereby final (addressed without challenge) |
| I98 | invention | 16 | not challenged by either reader; not thereby final (addressed without challenge) |
| I101 | invention | 4 | not challenged by either reader; not thereby final (addressed without challenge) |
| U2 | U-entry | 7 | not challenged by either reader; not thereby final (addressed without challenge) |
| U3 | U-entry | 6 | not challenged by either reader; not thereby final (addressed without challenge) |
| NF04 | NF entry | 17 | not challenged by either reader; not thereby final (addressed without challenge) |
| NF06 | NF entry | 17 | not challenged by either reader; not thereby final (addressed without challenge) |
| NF08 | NF entry | 4 | not challenged by either reader; not thereby final (addressed without challenge) |
| NF09 | NF entry | 15 | not challenged by either reader; not thereby final (addressed without challenge) |
| NF10 | NF entry | 15 | not challenged by either reader; not thereby final (addressed without challenge) |
| NF12 | NF entry | 16 | not challenged by either reader; not thereby final (no point) |
| NF13 | NF entry | 12 | not challenged by either reader; not thereby final (addressed without challenge) |
| NF14 | NF entry | 12 | not challenged by either reader; not thereby final (addressed without challenge) |
| NF15 | NF entry | 17 | not challenged by either reader; not thereby final (addressed without challenge) |
| NF16 | NF entry | 16 | not challenged by either reader; not thereby final (no point) |
| NF17 | NF entry | 16 | not challenged by either reader; not thereby final (no point) |
| NF18 | NF entry | 9 | not challenged by either reader; not thereby final (no point) |
| NF19 | NF entry | 15 | not challenged by either reader; not thereby final (no point) |


## 7. Marks: PARKED and OWNER QUESTION (rule 9; addendum points 8; decisions S33, S34)

Marked, not weighed. PARKED: a point about what hard to vary covers. OWNER QUESTION: a point that would move where values are placed, that turns on the reading of "argument", or that turns on a choice the owner has not made (or that the reader itself puts to the owner). Where a reader uses "where values are placed" of the value domains of ports or of exogenous values, the mark records the reader's own words; whether that is the owner's question is not this file's to say.

| item | part | reader | mark | the point, in brief |
|---|---|---|---|---|
| D4.2 | 3 | Mimo | OWNER QUESTION | The maths adds a clause the words lack (β takes each port to a port with the same domain, values compared as elements, I10); β_* is what "coincide" needs; the reader calls the domain clause "the owner's question (where values are placed)" and leaves it open (the reader reads the phrase as the value … |
| D5.1 | 3 | Mimo | OWNER QUESTION | π has a total arrow but "on the stated scope"; τ and σ carry no domain clause; the maths' λ carries value maps (I14); partiality (I17) is not in the words, and (F1) over C needs τ, σ defined at every pair of C; proposes a new clause in L189 (writes I17 in); whether a port translation may carry value… |
| D6.4 | 6 | GLM | OWNER QUESTION | Faithful to the sentence; "in the claimed way" under I22; the maths reads "block" as any nonempty subset of Γ with no recorded choice; with G = Γ and a two-valued answer port, deletion leaves the answer undetermined, so NC2 asks only for a contrast on C and all the bite against lookups lies in NC1; … |
| D6.4 | 8 | GLM | OWNER QUESTION | Faithful, including the asymmetry (only undeterminedness at the edit point counts as a contrast); "whether the words want that asymmetry is the owner's"; gives a wording if not, and proposes nothing "until the owner says whether the baseline is meant to be the point that is always determined". |
| D10.6 | 11 | GLM | OWNER QUESTION | Faithful, and the state reading is right; the text is silent on a corollary: if the argument that ruled a rival out ceases to be usable, the problem reopens and a candidate can become easy to vary again; S20 ("Once the explanation is rescued, the mistake shouldn't be able to creep back in") points t… |
| D12.9 | 13 | Mimo | PARKED | "Value" is fixed nowhere; the maths gives one (I71) and restricts the population to members sharing the codomain's ports and components; the reader calls this "the argument about hard to vary" and leaves it open as parked (S33, S34); no proposal. |
| D16.4 | 16 | GLM | OWNER QUESTION | 𝔓^adv_Θ is not defined beyond its name (NF12), so (U2) and UECS are open until "the coherently posed advanceable challenges" (L497) is defined; the words should define it or say that (U3) is conditional on it; no wording, "it is the owner's question". |
| FC18 | 3 | Mimo | OWNER QUESTION | The counterexample rests on I94, I10 (equal domains) and I14 (value maps) and fails wherever domains agree; it tells against the wording of L119 and the untranslated reading, not against what L233 gives; the D4.4 proposal removes it; if the owner rules that a footprint bijection may recode values (I… |
| FC20 | 5 | GLM | OWNER QUESTION | The counterexample tells against the inventions, not the text (value maps are I14's, the merging is I14's allowance of non-injective maps, κ(⊥) = ⊥ is U1); it survives I81's alternative (a); first remedy: require I14's value maps to be injective (a merging κ hides a difference, which L245 says (F1) … |
| FC43 | 10 | Mimo | PARKED | Conf/Riv symmetry cannot be broken, but the sentence can: under a reading of L317's "easy to vary" as "has a variation that still meets", one candidate with two admissible relations is easy to vary and its rival with one is not, so "the rival is then easy to vary too" fails; it rests on that reading… |
| FC62 | 8 | GLM | OWNER QUESTION | No break, but a text-level risk: where D's answer takes few values, the rival's counterpart component can be exactly the answer port pinned to the target's answer, a slot, so NC1 fails E; the sentence does not say the counterpart is never a slot; "a boundary the owner may want the text to speak to";… |
| FC63 | 8 | GLM | OWNER QUESTION | FC63 (c-i) is a counterexample to an invention, not the text: "with skewness substituted" fixes that the terms are read off the matrix, so only realizable term tuples enter (hand check: the all-ones tuple needs 1 = −1 over the reals too); (c-ii) is the sentence's own candidate and meets (E); the sec… |
| FC83 | 14 | GLM | OWNER QUESTION | A counterexample only to the claim's formal statement and I90's hand-set conjuncts; nothing in the sentence is refuted; restate the claim, and, if the text is to make the sentence follow, adopt the L225 wording; the reader notes the owner's own words cut both ways (S20's "a variation is a competitor… |
| FC98 | 17 | GLM | OWNER QUESTION | Two partings: the graph is acyclic only because I56 makes Prepares a primitive (read through (R), L405's "prepares a represented organization" reopens the loop L526 names); and the sink test asks of fourteen symbols whether each is read through Θ or an unlisted primitive, which the text leaves open;… |
| FC102 | 17 | GLM | OWNER QUESTION | FC102 (b) second half is a counterexample to the claim's own wording, resting on I68 and I100; against the text only in that L626 does not say what the failure turns on (for one thing, the window; for two, occupancy carrying no identity); no change required; "If the owner wants the boundary in the w… |
| FC105 | 9 | GLM | OWNER QUESTION | Under I45, L604's "An assessment event with contract C" is readable only by a gloss, and L612's "lost event identities" (known only through FC105's quotation) reads as identities beyond occurrence sets (I45's alternative (a)); the proposed definition settles the reading one way; "whether that is the… |
| FC107 | 4 | GLM | OWNER QUESTION | The definitional step holds only if p_δ has a target that is an organization; the text says nothing that makes a question or a defect an organization; not a counterexample, a gap; proposes a new last sentence of L161, if the owner means p_δ to be assessable; whether a question can serve as a target … |
| I10 | 3 | Mimo | OWNER QUESTION | Settled in one respect: "A kind is an equivalence class" rules out I10 (b); not settled: equal domains against a value bijection, which the reader leaves open as the owner's reserved question ("where values are placed", read as port values); the coordinate renaming is what "coincide" needs; no chang… |
| I14 | 5 | GLM | OWNER QUESTION | (Given in another part.) The FC20 remedy: make I14's value maps injective; if the text is to settle it, the L189 proposal under FC20 writes I14 in. |
| I45 | 9 | GLM | OWNER QUESTION | Not settled (matter 2); proposes a definition of event (no line named; placed with L169 by matter 2); "if the owner wants events with identities of their own, the sentence should instead say so — the choice is the owner's, not the maths'". |
| I50 | 14 | Mimo | OWNER QUESTION | Settled through the defined term: L220 names fidelity, whose scope is fixed by its definition, so (A) is out and the homomorphism clause in if fidelity has it; nothing to propose; "if the owner wants a failed prediction to count as violation, the words must say so". |
| I52 | 14 | GLM | PARKED | Not settled, and rightly open: "a survival condition requiring fidelity on H" states a lower bound, and the reader cites S20 ("Good explanations make bad ones harder to fit") as making the strength of survival conditions a live question; the occurrence reading of "member of the history" is forced (H… |
| I59 | 15 | GLM | OWNER QUESTION | Not settled: "requires" reads as necessary-only at least as easily as a characterization; proposes a new sentence at L443 (writes I59 in, keeping the round-1 fix); "If instead the owner wants necessary-only, say so at L443". |
| I62 | 16 | GLM | OWNER QUESTION | "q′ excludes at least what q excludes" is settled by L479, and Admit's antitonicity follows; "a task with a realization, owned or not, is in Admit" is not settled and makes (CT3) analytic; "If the owner wants (CT3) as a claim and not a definition", proposes inserting a clause in L479 (writes I62 in)… |
| I65 | 7 | Mimo | OWNER QUESTION | Partly fixed: the law and the two contracts are fixed; the identification contract's edits are not (the L325 wording); whether U_H, U_θ are ports or boundary values (I65 (a)) the reader calls "where values are placed, the owner's question" and makes no proposal (read as where the exogenous values si… |
| I67 | 17 | Mimo | OWNER QUESTION | The words settle the ports and the components as the closure conditions, not where 𝒬 lives or where x0's baseline membership is imposed; the L590 proposal writes both in; option (b) is ruled out by the words; I67's value set for the membership and query ports is left open, "that placement being the … |
| I71 | 13 | Mimo | PARKED | Stays open, beside the parked question; no proposal. |
| I79 | 4 | Mimo | OWNER QUESTION | L255's "as an unanalysed boundary input or as a component" separates the two, so the words carry I79's other choice (boundary coordinates of their own); U6 records no status change either way; no change proposed, the reader saying "where values sit is the owner's question" (read as where coordinate … |
| I88 | 10 | Mimo | OWNER QUESTION | Partly settled: "An argument is an argument tree: argument steps whose leaves are premises" fixes a tree with steps; whether a bare premise is an argument is open; finiteness is a search bound; S23 ("something that can be strung together into a coherent structure") bears on requiring a step; propose… |
| I99 | 8 | GLM | OWNER QUESTION | The sum relation is settled by the words against (c-i); alternative (b), D given term ports, is not settled; the text should say which, by the wording in (b). |
| I100 | 17 | GLM | OWNER QUESTION | Not settled on four counts: cell and step counts (may stay open), the rule at the ends (reflection invented), interaction (H17), one cell or a run (the text says "occlude a cell"); proposes a new L620 (writes I100's "stated rule", H17's no-interaction and the run in); "the owner chooses the rule". |
| H06 | 15 | GLM | OWNER QUESTION | The text conflicts with itself: L55 defines an episode by contract changes with records, while the body uses "episode" as a bounded stretch and never defines it; L35 makes the body govern; the body should carry the definition, merging L55's demand; proposes a new L429 opening (writes H06's reading i… |
| H16 | 16 | GLM | OWNER QUESTION | The words do not settle "on an active route" (not in the sentence, and not found defined in this part's lines); D16.1 and I74 disagree, a fault of the maths; D16.1 should read L487's own "can affect d's operative use", "unless the owner means the route machinery, in which case the text, not the defi… |
| matter 6 | 4 | GLM | OWNER QUESTION | The text needs a change: L219 should stay tied to the simulation layer and L151 should stop borrowing the term (wording under I51); if instead the owner wants "prediction" for any faithful transport, the L219 extension writes I51 in and should be marked so. |
| E16 | — | external reader | OWNER QUESTION | Its remark that redescribing an argument for a conclusion as an argument against its denial does not settle its status bears on L8 and L397 (decision S23; addendum point 8). |


## 8. Notes for the orchestrator (no ruling)

- **Counts.** Items tabulated from the seventeen parts: 399 (definitions and encodings printed in the parts, claims, inventions in full or "what was invented", U- and H-entries, NF entries, round-1 matters and changes; H20's five named definitions added in part 17). Going to a checker: 349 — 313 challenged by Mimo or GLM (of which 12 are among the twelve), 15 challenged only by the external reader or the case card, 13 external findings and 8 card items. Rule 7 records: 70. Context items: 16.
- **Proposals.** 255 distinct proposals are copied in full in section 2 (fenced or quoted-line proposals, and a few written in the running text). The lines with the most proposals: L315 (13), L119 (11), L255 (11), L109 (8), L151 (8), L329 (7), L375 (7), L257 (6), L393 (6), L441 (6), L343 (5), L317 (5), L195 (5), L429 (5), L103 (4). On most of these lines Mimo and GLM propose different wordings; rule 8 has the checker state each side's argument and rule between them or write a third wording.
- **References a reply makes to a proposal it does not contain.** Mimo, part 3 (FC15 and matter 1: "the L554 proposal in (a)"); Mimo, part 8 (FC58: "the proposal's 'In the linear case Z = ℝ^n'"); Mimo, part 11 (FC48: "The H10 proposal's second clause"). Recorded under those items as the reader states them.
- **Headings that differ from the brief's ids.** Mimo, part 15, heads its entry on the round-1 change at L443 "matter 1 · L443" (tabulated under L443). Several entries head two or three ids at once (for example "D9.4, D9.6 · L390, L393 · FC69"); the point is tabulated under each id, the proposal printed once and referred to thereafter.
- **"Where values are placed".** Mimo (parts 3, 4, 7 and 17) calls the value domains of ports, the placing of exogenous values and the value sets of I67's ports "the owner's question (where values are placed)" and leaves them open; these points are marked OWNER QUESTION in the reader's own terms (section 7). No reader proposes to move values in the sense of decision S31's question.
- **Points that cite the owner's words about hard to vary.** Mimo, part 10 (FC43: a reading of "easy to vary" as "has a variation that still meets"), part 13 (D12.9 and I71: "the argument about hard to vary", parked); GLM, part 14 (I52: S20's "Good explanations make bad ones harder to fit" cited for survival conditions). Marked PARKED; not weighed. GLM also cites S20's "A variation is a competitor" for a selection population's variation operator (part 13, FC77 and I52; part 14, FC83, where it says the owner's words cut both ways, marked OWNER QUESTION).
- **Factual comparisons made while checking quotations** (recorded under the items, not weighed): L363 as it stands contains "(so \(e_0=0\))" (Mimo, part 5, FC66, says the words name only the states in scope); L369 contains "If a premise about them ceases to be live, the argument is not usable (K2) and those candidates are no longer ruled out by it, every such candidate alike" (GLM, part 12, FC68, says L369 does not state the lapsing part); L103 and L255 contain "a deleted component imposes the full relation on its ports" (GLM, part 7, I03, says the text never says what deletion does); L141 names no closure condition (GLM, part 3, FC15, reasons conditionally on one).
- **Lines not given to a reader.** Many points say the reader relies on a line not given in its part (for example L141, L231, L255, L405, L522, L526, L584, L612); the quotation checks above compare what they quote with the text whole.
- **No TEXT- ids.** Every sentence of the text a reader names or proposes to change falls under an item of its part (for example L57 under FC10, L41 under FC79, L325 under FC02, L385 under FC76 and D9.11, L584 under matter 3, L27 under matter 14), so no item needed a TEXT-L<line> id.
- **One finding in two parts.** FC78 (part 13) and FC81 (d), FC82 (part 14) are one finding (the second check); each carries L193, L195 and L201 so that they fall in one group; GLM (part 13) adds FC83 to it, which the second check keeps separate.

