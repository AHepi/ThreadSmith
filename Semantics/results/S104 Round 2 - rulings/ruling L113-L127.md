# S104 Round 2 - ruling L113-L127

*Written by a fresh Opus 5.5 checker on 28 September 2026, which built nothing of this round and rules on no other group. Created at once and filled as it goes. The text under review is `tests/103 The semantics, standing alone, after round 1.md`, md5 f31ebb1f050783f1a84f6136cec20fcd (checked before reading; not written to). Nothing in `authority/`, no theory text, brief, reply, reading rule, addendum, grouping record, tabulation or committed maths file was written. This file obeys decision S23 except where it quotes the text, a reply, a brief, the external document, the maths or the owner.*

## Header

- **Group:** L113-L127 (the grouping record, JSON entry "L113-L127"; parts 1, 2, 3, 5, 7).
- **Lines ruled here:** L113, L119, L121, L123, L124, L125, L127.
- **Primary items:** D4.2, D4.3, D4.4, D4.5, D4.6, FC05, FC06, FC07, FC08, FC09, FC12, FC13, FC14, I07, I08, I10, I11, I12, I93, I94, I102, U4, U5, H01, H02, matter 4, E05.
- **Shared items (lines here):** D2.1 (L119), FC18 (L119), I09 (L119), matter 5 (L113), L123 (the round-1 change; L123), E04 (L119).
- **Context item:** E07.
- **Read:** the reading rule and both addenda; the grouping record; the tabulation's rows for every item above (parts 1, 2, 3, 5, 7 and section 3); the replies `s104_maths_mimo_1/2/3` and `s104_maths_glm_1/2/3` whole, the part 5 and part 7 replies' passages on D4.3 and D2.1, and every passage of the 34 replies that names an item of this group or one of its lines (searched by program); the part 2 and part 3 briefs; the formal core §2 and §4; the formal claims FC05-FC14, FC18 and the external addendum's FC-E2, FC-E3, FC-E4; the register's I04-I14, I80, I93, I94, I102 and the external addendum; the check of the program (§2 FC05, §4.2, §4.4) and the check of the formalization (§1 H01, H02; §2 T02, T03, T04, T05, T13; §3 R01-R05, R13); the external document's sections 2.3 and 3.1 whole and the items file's E04, E05, E07; the round-1 critical review (C07 and the matters); the owner's decisions S20, S21, S23, S25-S28, S31, S33, S34, S36, S37.

**Rulings in one place:** L113 KEEP; L119 FIX (settles I93 reading (i); settles I12 in part, σ on boundaries, as L556 already writes it); L121 FIX; L123 KEEP; L124 KEEP; L125 KEEP; L127 FIX. The exact old and new spans are given under each line, copied by program from the text and checked to occur once in their line.

**Models checked (rule 11).** Every model a reader gave by hand on an item of this group was checked, by hand or by the program (`model/` unchanged, run from `results/S104 Round 2 - maths` with a timeout), and each is named where it is used: FC05's model (program, `--claim FC05`, and by hand); FC07's pole contracts (program, `--claim FC07`); FC08's witness (program, `--claim FC08`, and by hand); the external FC-E3 (program, `s104_external.py FC-E3`); Mimo's FC06, FC07 (d), FC09 (d), FC13 and FC03/I10 (b) models (by hand); GLM's FC07 (d) second attack and GLM part 1's "model two" (by hand, and against `model/cases.py`). Every quotation of the text this ruling relies on was compared by program with the line it names; all were found. No reply quotation this ruling relies on was not found; the tabulation's "not found" entries (for example Mimo's "sets a port directly", GLM's "does not itself determine") are the readers' own words or proposals, and are ruled on as such.

## Line by line

### L113

> L113 | Fix an organization \(D\) and a contract \(C\subseteq A\times B\) (Part III). The **signature** of component \(j\) on \(C\) is

**Challenges.**
- GLM (part 1, reply line 23 and proposal G1-B6, reply line 93; item D4.5, and matter 5): the comparison baseline of "changes under" (I09) is invented; the vacuity of invariance is "a real semantic choice the text never faces"; proposes replacing L113 by its first sentence followed by a definition of "changes under" and "invariant under" (at the identity edit at the same boundary; vacuous where C holds no edit of the class).
- Mimo (part 1, reply lines 92-96, proposal M1-B8; matter 5, shared, primary at L109): "L109 gives roles under A while (K) builds signatures on a contract C"; proposes to add after L113 "Roles (input, output, observation) are defined under A; signatures (causal assignment, measurement, rule) are defined under a contract C ⊆ A × B."
- Against both, on I09: Mimo (part 2, reply line 65): the baseline comparison "is not settled by the words and should stay open", vacuity "is the natural reading of 'invariant'", and the existential reading of "changes under" "is settled, by L123's own contrast". GLM (part 3, reply line 13): D4.5 is "Faithful given I09's reading ..., which is forced: 'changes under an edit' has no other referent in (K)".

**Ruling: KEEP.**

Reasons, why this and not the readers' wordings:
1. **G1-B6 would break the definition it sits in.** L113 ends "The **signature** of component \(j\) on \(C\) is" and leads into the display (K) at L116. G1-B6 replaces the whole line and drops that lead-in, so (K) would stand with no sentence introducing it; and it would define "changes under" for a signature one sentence before a signature is defined.
2. **The text's own words give what G1-B6 would write in, except one residue that no result turns on.**
   - A signature is indexed pair by pair: L119, "A signature is built from a component's relation under each \((a,b)\in C\)". To say it "changes under" an edit is to compare its relation at that edit with its relation where the edit is not made, at the same pair's boundary; GLM itself (part 2, line 19) says the same-boundary comparison "matches L119".
   - "Invariant under" a class is a statement about every edit of the class; read as the universal it is, it holds where C holds none. "Variable under" (L124, L125) is set against "invariant under", so it says some edit of the class alters the relation. Mimo's reply line 65 gives this reading from L123's own contrast; GLM's reply line 13 calls it forced.
   - What the words leave open is I09's alternative (b), "compare only pairs that are both in C". It differs from I09 only where C holds (a,b) without (1,b). No search result, and no sentence of the text, turns on that case.
   So by rule 6 the line stays as it is; I09 stays recorded (its primary checker is the checker of L57).
3. **M1-B8 would add a sentence that says something the text does not.** It places "output" among the roles "defined under A"; L109 defines output without A ("determined by \(L_j\) given the other ports of \(V_j\) across \(B\)"), and FC02 (b) is the maths' statement that output status does not use A. It also calls the families "signatures", where L121 calls them "families of signatures". And "Add after L113" would put a sentence between "is" and the display (K). What matter 5 points at is L109's "that is" clause, which equates a role read off A with a signature on C; L113 already names the contract ("a contract \(C\subseteq A\times B\)"), so the separation Mimo asks for is stated here, and the clause at L109 is the checker of L109's to rule on (shared note below).

The owner's words: the line holds no word S23 forbids, no list, count, grade or record (S20), nothing about what must happen (S21), no physical possibility (S25-S27), settles nothing (S28), and says nothing about hard to vary or where values are placed.

### L119

> L119 | Two components \(j,j'\) are **of one kind on \(C\)** when there is a bijection of their footprints under which \(\operatorname{sig}_C(j)\) and \(\operatorname{sig}_C(j')\) coincide. A kind is an equivalence class of components under this relation. For two explanatory candidates (Part V), let \(E\) and \(E'\) be their organizations and \(t=(\pi,\tau,\sigma,\lambda)\) and \(t'=(\pi',\tau',\sigma',\lambda')\) their transports from \(D\), where \(\pi\) translates valuations, \(\tau\) translates edits, \(\sigma\) translates boundaries, and \(\lambda\) assigns each component of \(E\) a subnetwork of \(D\), its counterpart, with a port translation (Part IV). A component of \(E\) and a component of \(E'\) are of one kind on \(C\) when their signatures, read on \(C\) through \(\tau\) and \(\tau'\), coincide under a footprint bijection; Argument 2 uses kinds in this sense. Argument 1 makes the like comparison between an active component \(k\) of \(E\), read on \(C\) through \(\tau\), and its counterpart \(\lambda(k)\), read on \(C\) directly with its hidden ports projected away, up to the port translation. Kinds are therefore relative to the contract; a coarser contract identifies more components, and two components of one kind on \(C\) may separate on a finer contract. A signature is built from a component's relation under each \((a,b)\in C\), not from the values its ports take in a solution; two components that differ only in those values are of one kind on \(C\), whatever the difference is called. An edit that sets a port replaces only the component that assigns the port (above), not the relations of the components that read it, and an edit under which the two relations stay equal does not separate the components.

The line has eight sentences (S1 to S8 below). Challenges fall on S1, S4, S5, S6 and S8; S2, S3 and S7 are not challenged (S2 is relied on below). The ruling is **FIX** of S4, S5 and the second clause of S8; the rest of the line stands as it is.

**S1 (D4.2, I10; E04 shared).** "Two components \(j,j'\) are **of one kind on \(C\)** when there is a bijection of their footprints under which \(\operatorname{sig}_C(j)\) and \(\operatorname{sig}_C(j')\) coincide."
- GLM (part 3, reply lines 7 and 44-49, G3-B2): the sentence cannot be applied "until values are handled somehow"; "since signatures cannot 'coincide' across differing domains without some value handling, the text should say which"; proposes "Two components j,j′ are of one kind on C when there is a bijection of their footprints, carrying each port to a port with the same values, under which sig_C(j) and sig_C(j′) coincide, values compared as values."
- Mimo (part 3, reply lines 3 and 61): the renaming of coordinates is what "coincide" needs; "A kind is an equivalence class" (S2) rules out I10 (b), which is not transitive (model in its (d)); equal domains against a value bijection is left open, which Mimo calls "the owner's question (where values are placed)".
- **KEEP S1.** GLM's premise does not hold: two relations on footprints of different domains can coincide as sets once the ports are renamed (for example the full relation {0,1} on a port with domain {0,1}, and the relation {0,1} on a port with domain {0,1,2}); the sentence applies as written, with "coincide" as sameness of the renamed relations. What I10 adds beyond the words is the equal-domain clause, which makes that pair two kinds. No result of the text turns on the clause: FC18's counterexample needs it together with I94, which the text excludes (S5 below; the check's T03), and under D4.4's reading both signatures stand on \(V_k\) with \(E\)'s domains, so the domains agree. So the clause stays an open choice of the maths (rule 6), and GLM's wording, whose "with the same values" and "values compared as values" are themselves open to two readings (the same value domain, or the same values in a solution), is not adopted. Mimo's model for I10 (b) was checked by hand: ports p, q, r in {0,1}; \(L_j=\{(0,0),(0,1)\}\) on (p,q), \(L_{j'}=\{(0,0),(1,0)\}\) on (q,r), \(L_{j''}=\{(0,0),(1,0)\}\) on (p,r); p↦r, q↦q carries \(L_j\) to \(L_{j'}\) and fixes the shared q; q↦p, r↦r carries \(L_{j'}\) to \(L_{j''}\) and fixes the shared r; the only bijection fixing the shared p of j and j'' is p↦p, q↦r, which gives {(0,0),(0,1)} on (p,r), not \(L_{j''}\). The relation under I10 (b) is not transitive, and S2 asks for an equivalence relation. The owner-question mark is taken up under "Owner questions" below.

**S4 (D4.3, I12).** "A component of \(E\) and a component of \(E'\) are of one kind on \(C\) when their signatures, read on \(C\) through \(\tau\) and \(\tau'\), coincide under a footprint bijection; Argument 2 uses kinds in this sense."
- Mimo (part 3, reply lines 5-10, M3-B1): "the sentence names τ alone, while boundaries need σ (L189)"; proposes "read on \(C\) through \(\tau,\sigma\) and \(\tau',\sigma'\)".
- GLM (part 3, reply lines 9 and 58-62, G3-B4): "a signature is a function of edit *and* boundary, so translating the edit and holding the boundary fixed (I12's other choice (a)) would not read the signature on C at all"; proposes "read on C through τ and τ′ and through the boundary translations of the two transports".
- **FIX S4.** Both readers' argument holds: a pair of \(C\) has a boundary of \(D\), and a component of \(E\) has a relation only at boundaries of \(E\), so reading it "on \(C\)" needs the boundary translation. The text itself writes it so at L556, \(\operatorname{sig}_{\tau[C]}(k)=\{(\tau(a),\sigma(b),L_k(\tau(a),\sigma(b)))\}\), and S3, the sentence just before, names σ as what "translates boundaries". So the words of S4 fall short of the text's own formula, and they leave room for I12's alternative (a) (\(E\)'s boundary held at σ(b0)), which no line of the text uses. Mimo's wording is taken for the phrase, because it names the maps S3 has just named, in S3's own notation, and changes nothing else; GLM's "through the boundary translations of the two transports" says the same at greater length. Mimo's block would replace the whole sentence and drop "; Argument 2 uses kinds in this sense", which no reader challenged; the FIX keeps it. This writes into L119 the part of I12 that L556 already fixes (the check's T04); the part I12 still chooses, comparing the two signatures as functions on \(C\), is not written in. **Settles I12, in part (σ on boundaries).**

**S5 (D4.4, I94; FC18 shared).** "Argument 1 makes the like comparison between an active component \(k\) of \(E\), read on \(C\) through \(\tau\), and its counterpart \(\lambda(k)\), read on \(C\) directly with its hidden ports projected away, up to the port translation."
- Mimo (part 3, reply lines 12-17 and 57, M3-B2): whether the counterpart is read on \(D\)'s own ports and domains (I94) or carried to \(V_k\) (D4.4) is open, since "read on C directly" gives the other reading room; proposes ending the sentence "... read on \(C\) directly with its hidden ports projected away and what remains carried to \(V_k\) by the port translation of \(\lambda\)."
- GLM (part 3, reply lines 40 and 86): settled by the text: "up to the port translation" carries the counterpart to \(V_k\); I94 should be recorded as a stress test of I10, not as a reading.
- **KEEP the counterpart's reading; FIX "through \(\tau\)" to "through \(\tau,\sigma\)", for the reason given at S4.** On the counterpart, GLM's argument holds and Mimo's does not require a change: "directly" says that the counterpart, a subnetwork of \(D\), is read on \(D\)'s own pairs with no \(\tau\); "up to the port translation" says the comparison is made once the port translation is applied; and the text writes the counterpart's signature with \(\operatorname{proj}^{\lambda}_{V_k}\) at L556, which L233 defines as "carrying what remains to \(V_k\) by the port translation of \(\lambda\)". That is D4.4's reading, and the untranslated reading (I94) is not a reading of these words (the check's T03). Mimo's ending would repeat L233 in L119 with no change of content. The added σ keeps S5 in step with S4 and with L556's second formula; without it, S4 and S5 of one line would read the candidate's component in two ways.

**S6 (I11).** "Kinds are therefore relative to the contract; a coarser contract identifies more components, and two components of one kind on \(C\) may separate on a finer contract."
- GLM (part 3, reply lines 51-56, G3-B3): not settled; "substantive under the subset reading and tautological under the distinguishable-pairs reading"; proposes writing in "a contract is coarser than another when, at the same baseline, it holds a subset of the other's pairs".
- Mimo (part 3, reply line 63): settled by L317's "a finer contract that contains a change" and by this sentence; no change.
- **KEEP S6.** Mimo's argument holds, and the text says it in a third place: L39, "At a finer level with more admitted changes they may separate", and L317, "A finer contract that contains a change at which two rivals conflict makes a new question". A finer contract is one with more admitted changes, which is I11's reading; the quotient and "distinguishable pairs" readings are not what these words say. GLM's definition would repeat, at L119, what L39 and L317 already give.

**S7.** Not challenged (FC05's first half, which holds on every model tried). KEEP.

**S8, first clause (D2.1 and E04, shared; FC06; H01; I09 shared).** "An edit that sets a port replaces only the component that assigns the port (above), not the relations of the components that read it"
- GLM (part 2, reply lines 83-87, G2-B6; H01): the default reading follows "most literally from L119's 'only'", but with L91's closure it classes composites as rule edits and collapses the families on C2*; proposes adding "An edit that replaces several components together sets no port, edits no rule, and is an intervention on none of them alone."
- Mimo (part 2, reply lines 71-76, M2-B9; H01): L119's "only" answers whether readers are touched, and L103 is met by a composite; proposes "An edit that sets a port replaces the component that assigns the port (above), not the relations of the components that read it; an edit that sets several ports at once sets each of them."
- GLM (part 2, reply lines 71-75, G2-B5; I09): proposes adding a definition of "changes" and "invariant" here (the same content as G1-B6 at L113).
- The external reader (doc L138, E04): the "component that 'assigns' the port" "needs either an independent definition from the edit structure or explicit inclusion in the supplied data".
- **KEEP the first clause.** Reasons:
  - Mimo's wording keeps "not the relations of the components that read it" and makes a composite that sets H and L "set each of them". As a setting of H, that composite then replaces \(c_L\), a component that reads H. So the new sentence would contradict itself on exactly the edits it adds.
  - GLM's wording says of every edit "that replaces several components together" that it "edits no rule". That takes in a change of rule that alters two components at once, which is an edit to a rule on any reading. And "sets no port" said of a joint setting of H and L runs against the plain sense of "sets".
  - What the text says about composites is less than either reader writes. The "only" of S8 says that an edit that sets a port, in this sentence's sense, replaces one component. So a composite that replaces two is not such an edit, which is D2.1's reading (GLM's "most literally"). L57 sets editing a rule against intervening: "a rule's application changes when the rule is edited and not when the world is intervened on". So a composite of settings is an intervention and not an edit to a rule. The maths' classing of it as "an edit to the rule of each component it alters" (the check's H01, through I08) is the maths' choice, and the collapse of the families on C2* tells against that choice, not against the text (see H01 under the items).
  - Whether a composite of settings counts as an intervention "on its output port" (L123) or "on the measured port" (L124), the text leaves open. Neither reader's wording settles it without saying what the text should not. So it stays open (rule 6), recorded as H01.
  - G2-B5 is not adopted, for the reasons given at L113, point 2.
  - On E04: this clause refers back with "(above)" to L103, where "the component assigning that port" is first used. Whatever the checker of L103 and L109 rules on that phrase reaches this clause through "(above)", and nothing needs to change here.

**S8, second clause (FC05, I93, U4).** "and an edit under which the two relations stay equal does not separate the components."
- The counterexample (search results, FC05 (ii); reproduced by this checker with `python3 -m model.run --claim FC05 --scale 4 --time-cap 45`, and worked by hand): D has p0, p1 in {0,1} and components c0, c1 on (p0, p1). At (1,b0), \(L_{c1}=\{(0,0),(0,1)\}\) and \(L_{c0}=\{(0,0),(1,0)\}\); at (e1,b0) both are {(0,1),(1,1)}; C = {(1,b0)}. The swap of p0 and p1 carries \(L_{c1}(1,b0)\) to \(L_{c0}(1,b0)\), so c1 and c0 are of one kind on C. At (e1,b0) the two relations are equal under the identity and not under the swap, which gives {(1,0),(1,1)}. On C ∪ {(e1,b0)} no one bijection serves both pairs, so the edit separates them.
- Mimo (part 3, reply lines 42, 50-55, M3-B6): the clause does not say which bijection; under the one that witnesses the kind it follows from the definition, under "some bijection" or "each relation as at the baseline" it fails; proposes "and an edit at which the two relations, compared under that same footprint bijection, stay equal does not separate the components."
- GLM (part 3, reply lines 21, 38, 74-84, G3-B6, G3-B7): the counterexample is to I93 (ii) only; the sentence "is either true but adds nothing beyond D4.2 (readings (i) and U4) or false (reading (ii))"; "The change to the text is to say which"; proposes reading (i) ("and an edit under which the two signatures still coincide under a bijection that witnesses the two components being of one kind on C does not separate them") or, "if the owner wants the sentence to say something with content", U4's ("and an edit that leaves each of the two relations as it was at the baseline does not separate the components").
- The check of the formalization (T02, withheld from the readers): "'Stay' presupposes the equality that already holds, under the bijection that makes j and j' one kind", so reading (ii) is excluded by the words.
- **FIX the second clause, writing in I93's reading (i).**
  - *Whether the words exclude (ii).* T02's argument leans on "stay", but it does not close the matter. Two relations on two footprints can be "equal" only under some footprint bijection. If "equal" is read so, "the two relations stay equal" can be read as "at the new pair, as before, they are equal under some bijection", which is reading (ii). In the counterexample they are equal under the swap at (1,b0) and under the identity at (e1,b0); on that reading they stay equal, and the clause then says the edit does not separate them, which fails.
  - *So both readers' argument holds.* The words admit a reading under which the clause says what the definition in S1 denies. The smallest change that removes it is to name the bijection.
  - *Why the clause is not dropped.* GLM's point that reading (i) "adds nothing beyond D4.2" is not a reason to drop it: the clause states a consequence of S1, as "Kinds are therefore relative to the contract" does, and joined to the first clause it says that setting a port the two components read does not by that alone separate them where the relations stay equal.
  - *Why not U4's wording.* It does not say what "stay equal" says: two relations staying equal to each other is not each relation staying as it was. It speaks of "the baseline" where a setting edit at another boundary leaves a reader's relation as it was at its own boundary. And the second check found the U4 reading failing on 82 of the 1,752 models that met its premise, every one of them with (1,b) not in C.
  - *Why this wording.* It keeps the text's "relations" and "stay equal". It names the bijection within the clause, as "a footprint bijection by which the two components are of one kind on \(C\)". Mimo's "that same footprint bijection" would find its nearest antecedent in S4's "a footprint bijection", which is the bijection for two candidates' components, not S1's. GLM's G3-B6 speaks of "signatures" coinciding at an edit that may lie outside C, where the signature on C records nothing.
  - *It holds.* If β makes j and j′ one kind on C and \(\beta_*L_j(x)=L_{j'}(x)\) at the new pair x, then β serves every pair of C ∪ {x}. This is FC05's reading (i), which held on every model tried and holds by construction.
  - **Settles I93 (reading (i)).** U4's condition is left as what it is: where (1,b) ∈ C it gives equality under the witnessing bijection, so the clause covers it; it is not a reading of "stay equal".

**Ruling on L119: FIX.**

- old (exact span of L119, from S4 to the end of the line):

```
read on \(C\) through \(\tau\) and \(\tau'\), coincide under a footprint bijection; Argument 2 uses kinds in this sense. Argument 1 makes the like comparison between an active component \(k\) of \(E\), read on \(C\) through \(\tau\), and its counterpart \(\lambda(k)\), read on \(C\) directly with its hidden ports projected away, up to the port translation. Kinds are therefore relative to the contract; a coarser contract identifies more components, and two components of one kind on \(C\) may separate on a finer contract. A signature is built from a component's relation under each \((a,b)\in C\), not from the values its ports take in a solution; two components that differ only in those values are of one kind on \(C\), whatever the difference is called. An edit that sets a port replaces only the component that assigns the port (above), not the relations of the components that read it, and an edit under which the two relations stay equal does not separate the components.
```

- new:

```
read on \(C\) through \(\tau,\sigma\) and \(\tau',\sigma'\), coincide under a footprint bijection; Argument 2 uses kinds in this sense. Argument 1 makes the like comparison between an active component \(k\) of \(E\), read on \(C\) through \(\tau,\sigma\), and its counterpart \(\lambda(k)\), read on \(C\) directly with its hidden ports projected away, up to the port translation. Kinds are therefore relative to the contract; a coarser contract identifies more components, and two components of one kind on \(C\) may separate on a finer contract. A signature is built from a component's relation under each \((a,b)\in C\), not from the values its ports take in a solution; two components that differ only in those values are of one kind on \(C\), whatever the difference is called. An edit that sets a port replaces only the component that assigns the port (above), not the relations of the components that read it, and an edit under which the two relations stay equal under a footprint bijection by which the two components are of one kind on \(C\) does not separate them.
```

- The three changes within the span: "through \(\tau\) and \(\tau'\)" → "through \(\tau,\sigma\) and \(\tau',\sigma'\)"; "read on \(C\) through \(\tau\), and its counterpart" → "read on \(C\) through \(\tau,\sigma\), and its counterpart"; "stay equal does not separate the components." → "stay equal under a footprint bijection by which the two components are of one kind on \(C\) does not separate them." Every other word of the span is unchanged; the span is given whole so that one exact match applies all three.
- **Dependents.**
  - L556: its formula is what the S4/S5 change aligns with; it is unchanged.
  - L554 ("no active component \(k\) of \(E\) has a signature on \(\tau[C]\) that differs from the one its counterpart \(\lambda(k)\) has on \(C\), up to the port translation"): reads as before; its \(\tau[C]\) is the checker of L554's.
  - L562 and L564 (Argument 2, "read on \(C\), coincide"): read as before, now with S4 saying how.
  - L11, L39 and L558 speak of kinds without the clause changed and read as before.
- **The owner's words.** The new words are symbols the text already defines and one phrase naming S1's own bijection. They hold no word S23 forbids, no list, count, grade or record (S20), nothing about what must happen (S21), no physical possibility (S25-S27), and settle nothing (S28). They say nothing about hard to vary and move no value.

### L121

> L121 | What ordinary language calls a cause, a measurement, a rule or a constitutive status are families of signatures:

**Challenges (matter 4, FC09, E05).**
- Mimo (part 2, reply lines 32 and 96-101, M2-B10): the words name four things and the bullets give three; "the third bullet covers a rule and a constitutive status"; the maths (a constitutive status is \(\mathrm{Rule}_C\)) should stand, since L347 "gives the constitutive rule the rule family's shape"; proposes "... are families of signatures; a constitutive status has a rule application's signature (below):".
- GLM (part 2, reply lines 113-117, G2-B7): "L347 already assigns the constitutive status to the rule-application family, so the maths and the text agree; but a reader counting names against bullets is misled"; proposes "... are families of signatures, the rule and the constitutive status one and the same family:".
- Mimo (part 2, reply line 86, FC09 (d)): the computation runs under I08 and "cannot distinguish I08 from its alternative (b)", under which the rule family is empty.
- The external reader (doc L140-L142, E05): the listed patterns "do not automatically provide the sharp semantic classification the surrounding prose suggests".

**Ruling: FIX.**

Reasons:
- **The two readers agree on the fault and it holds.** L121 gives four names and the bullets that follow give three families. Which bullet the fourth name falls under is said only at L347, in Part VII: "Its signature under (K) is invariant under interventions on \(Z\) and variable under edits to \(C_r\)". That is the rule-application bullet of L125 word for word, with \(Z\) for "the world" and \(C_r\) for "the rule". So the mapping is the text's own, and needs no invention. Mimo's FC09 (d) concerns the maths' formal check, which cannot tell I08 from its alternative (b); at the level of the words, L347's pattern and L125's are the same pattern. Mimo's own argument (reply line 58) is that I08 (b) would leave the rule family empty, since by L119 settings of a port the component does not assign never alter it. Checked by hand.
- **Why this wording.** It gives the mapping where the four names are given, names the family by its bullet's own name, and points to the place that shows it, in the text's style of cross-reference ("(Part VI, redundant routes)" at L566). Mimo's "(below)", after a semicolon and before the colon that introduces the bullets, can be read as pointing to the bullet just below, which does not mention a constitutive status. GLM's wording says the two are one family without saying which bullet it is.
- **On E05.** L121 says the four are "families of signatures", not that the families exclude one another, and the FIX adds no such claim; see E05 under the items.

- old (exact span of L121):

```
are families of signatures:
```

- new:

```
are families of signatures, a constitutive status having a rule application's signature (Part VII, constitutive rules):
```

- **Dependents.**
  - L122 to L125 (the bullets) follow the colon as before.
  - L347 is what the new words point to; it is unchanged.
  - L57 ("A rule and a cause differ ...") reads as before.
- **The owner's words.** No word S23 forbids; no list, count, grade or record doing the work of content (S20): the words state which family, and count nothing. Nothing about what must happen (S21), no physical possibility (S25-S27), nothing settled (S28), nothing about hard to vary or values.

### L123

> L123 | - a **causal assignment** has a signature that changes under intervention on its output port and is invariant under observation edits;

**Challenges.**
- Mimo (part 2, reply lines 8-13, M2-B2; D4.6, H02, I102, FC07): the maths reads "its output port" as the port the component assigns; L109 defines "output" otherwise, and on the pole H and θ are outputs of \(c_L\) too; "the words should name the assigner"; proposes "- a **causal assignment** has a signature that changes under intervention on the ports it assigns and is invariant under observation edits; a part that reads a port another part assigns has no such signature on any contract;".
- Mimo (part 2, reply line 84, FC07 (d)): under I04 and R-i, a setting of \(o\) that alters \(L_j\) is itself an observation edit whenever \(j\) reads a port another part assigns, so \(\mathrm{Causal}_C(j)\) implies that \(j\) reads no such port, on every contract; the invariance clauses of L124 and L125 hold of every non-assigner, so "the only discriminating clause is L123's invariance under observation edits".
- GLM (part 2, reply line 91, H02): "The text settles it, against the maths as written": L109 defines an output, "and 'its output port' in L123 should mean that, not `asg`"; the maths should use D2.3's outputs with I102's union; no change to the text.
- GLM (part 2, reply line 79, I102): the union rule "is unsettled and reasonable".
- The round-1 change (shared; primary at L109): all four replies keep the removal of "and under replacement of the component". Mimo (part 1, reply line 90; part 2, reply line 103), and GLM (part 1, reply line 83; part 2, reply line 111): "by L103 an intervention on the output port *is* a replacement of the component". GLM part 1 adds that under R-i "L123 as it stands after round 1 becomes unsatisfiable in any contract containing an intervention on the output port" (its "model two", reply line 79).
- The external reader (doc L140, E05): "For a component Y := X, intervening upstream on X changes the solution but normally leaves the relation Y = X unchanged. A measuring component N := X has the same property."

**Ruling: KEEP.**

Reasons:
1. **"its output port" (H02).** Mimo's argument is that "intervention on" a port is a setting edit, which by L103 and L119 replaces only the component assigning the port. So the only interventions that can change \(j\)'s signature are interventions on ports \(j\) assigns. GLM's is that "output" is the text's own defined term. Both hold, and together they show the words need no change:
   - The change clause asks that some intervention in \(C\) on an output port of \(j\) changes \(j\)'s signature.
   - By L119 an intervention on an output port that \(j\) does not assign (H or θ for \(c_L\)) never changes \(j\).
   - So the clause picks out the same components on L109's reading of "output" as on the assigner's, except for a component that assigns a port its relation leaves undetermined. That is a case where the text's own "output" and "the component assigning" come apart, and it is the matter E04 raises at L103 and L109, not a matter for this bullet.
   - Mimo's first clause would tie L123 to "the ports it assigns", which E04 says the text has not defined. The check's H02 reasons that on the pole's C1 and C2 the families come out the same under both readings.
   - H02 is therefore a departure of the maths from the words that changes no family in any case the text works. It is recorded and left to the maths: GLM's D2.3 with a union, or a recorded departure.
2. **Mimo's added clause is I06's reading R-i written into L123.** "A part that reads a port another part assigns has no such signature on any contract" follows under R-i. Mimo's reasoning was checked by hand:
   - Let \(j\) assign \(o\) and read \(m\), with \(\operatorname{asg}(m)=k\neq j\).
   - A setting of \(o\) that changes \(L_j\) alters \(j\) and, by D2.1, leaves \(k\) at every boundary, so under R-i it is in \(\mathrm{Obs}(o,m)\).
   - Invariance under observation edits then fails at the very pair where the change clause is met.
   - The program agrees: FC07, \(c_L\) on C2 under R-i; FC-E3, \(c_Y\) and \(c_N\) under R-i.

   Under R-ii the added clause fails: on C2, \(c_L\) reads H and θ and is a causal assignment (FC07, computed; this checker reran it). Which reading L109's observation takes is I06, which belongs to the checker of L109 (shared note below). A clause at L123 that holds under one reading of L109 only would settle I06 from a line that does not define it.
3. **GLM part 1's "model two" does not bear on L123 as the pole has it.** It takes the pole, a contract holding a setting h of H, and R-i, and says h is in Obs(H, θ), so that \(c_H\) cannot be causal. Obs(o, m) needs \(m\) in the footprint of the component assigning \(o\). \(c_H\)'s footprint is {H} alone (`model/cases.py`, `foot = {"c_H": ("H",), ...}`; L325 gives \(H:=U_H\)), so there is no such \(m\). FC07's computation has \(c_H\) causal on C1 and C2 under R-i. The case that does exist under R-i is Mimo's (point 2): a component that reads a port another component assigns. The round-1 removal stands on the argument all four replies give.
4. **E05's first example.** L123 speaks of intervention on the component's *own* output port, not of an upstream intervention. The external reader's own words, that the distinction "cannot come merely from whether their own relation changes under that upstream intervention", are not a claim L123 makes. What separates a response from a reading in the text is an edit to the reading alone (L109's observation edit). The external addendum's FC-E3, rerun by this checker, shows the two parting once such an edit is in the contract, and sharing their families where none is. The text says the second itself: "Two components no admitted change can separate are one kind at that level" (L11).
5. **I102.** The text presumes one assigning component per port and one output port per causal assignment ("its output port"). The union for a component that assigns several ports is not in the words and changes nothing in any case the text works. It stays open (rule 6).

The owner's words: unchanged line; nothing added.

### L124

> L124 | - a **measurement** has a signature invariant under interventions on the measured port and variable under edits to the measuring relation;

**Challenges.**
- GLM (part 2, reply lines 23, 45-51, 67, 81; G2-B2; D4.6, I07, U5, FC08): three departures (the measured port "as though unique"; "the measuring relation" read as the component's own relation; "Nothing in the definition makes the reading *depend* on the measured port"); FC08's witness is "a counterexample to the **text**"; "A measurement that can ignore what it measures is also not what L124 should allow"; proposes "- a **measurement** has, for a port it reads and does not itself determine, a signature invariant under interventions on that port and variable under edits to the measuring relation, and a reading that depends on that port in the relation itself;", which "uses L109's own output definition, which kills the U5 case".
- Mimo (part 2, reply lines 56 and 69; I07, U5): I07 is settled: L109's "No role assignment is supplied" with L127's "another part" give the measured port as one another part assigns; L116 and L103 give "the measuring relation" as the component's relation; read per port; "No text change; but asg(m) must be *defined* and different from j (this removes U5)".
- Mimo (part 2, reply lines 40-48; FC08): the witness tells against L127's gloss, "not to the definitions, and not to an invention"; "The words overstate; the maths stands."
- The external reader (E05), as at L123.

**Ruling: KEEP.**

Reasons:
1. **G2-B2's "does not itself determine" would empty the family of the text's own measurements.** L109's "output" is "determined by \(L_j\) given the other ports of \(V_j\)". A relation that can be inverted determines each of its ports given the others: \(c_L\), \(L=H\cot\theta\), determines H given L and θ (FC02 (c); FC-E2 for {(0,0),(1,1)}); the external reader's reading N := X determines X given N. So "a port it reads and does not itself determine" excludes H and θ from \(c_L\)'s measured ports, and X from \(c_N\)'s. \(c_L\) would then be a measurement of nothing on C2, against FC07's R-i result and against L127's own "a part that reads or reports another part". This was checked by hand from L109's words, and it is the same failure of "output" to pick out a port that E04 raises.
2. **G2-B2's dependence clause is a new condition on the family, and the fault FC08 finds is at L127.**
   - FC08's witness was rerun (`--claim FC08`) and checked by hand. \(h_{p0}\) has relation {p0 = 1}, constant in p1. It reads p1, which \(h_{p1}\) assigns, and is unchanged by the setting of p1. An edit makes it full. So both clauses of L124 hold, and after the setting of p1 the reading p0 stays 1.
   - The mismatch is between L119 ("not from the values its ports take in a solution") and L127's gloss ("change the part and the reading follows"), as both readers say. L124 says only what it says: two patterns in (K).
   - Whether a measurement must depend on what it measures within its relation is a choice about the family that neither the text nor the owner has made. The smallest change that removes what holds is at L127 (below), and it adds no condition to the family. GLM's dependence clause is recorded as a proposal for a later round, not applied.
3. **I07 is settled in substance by the words.**
   - *The measuring relation.* It is the measuring component's own relation. L124's grammar says so: the measurement's *own* signature is "variable under edits to the measuring relation", which it cannot be if that relation belongs to another component (GLM's argument, reply line 67). L127's "change only the reading" says the same.
   - *The measured port.* It is a port the measuring component reads and another part assigns: L127, "a part that reads or reports another part".
   - *No declared port.* "the measured port" names no declared port: L109, "No role assignment is supplied"; L127, "not additional data".
   - *Several read ports.* For a component that reads several ports, the definite article is relative to the port measured, as "another part" at L127 is read one part at a time (Mimo). GLM's worry about uniqueness is answered so.
   - No change is needed.
4. **U5.** The consequence (under I102 a component can have the measurement signature for its own output port, when no edit sets that port) comes from the maths' I102, which counts a port with no assigning component among "the ports j does not assign". Both readers hold that the text is against it: "another part" (L127), and "the component assigning it" (L109), where the observation is reported by the component that assigns the reading. The repair belongs in the maths (I102 trimmed so that such a port is not \(j\)'s measured port), not in L124. GLM's wording would close U5 only through point 1's failure.

### L125

> L125 | - a **rule application** has a signature invariant under interventions on the world and variable under edits to the rule.

**Challenges.**
- Mimo (part 2, reply lines 58-62, M2-B8; I08): the main line is settled ("variable under edits to the rule" can only mean \(L_j\) varies; I08 (b) would leave the family empty); open is whether the component's own settings count as rule edits, and "L57's contrast ... says not"; proposes "- a **rule application** has a signature invariant under interventions on the world, that is, settings of the ports it does not assign, and variable under edits to the rule, that is, edits that alter the relation it applies other than by setting the ports it assigns." (writes I08 in).
- GLM (part 2, reply lines 25 and 69; I08): "The rule" as the component itself "is settled by L347's wording"; "the world" as all ports not assigned against the ports read "is not settled — but given D2.1 the two differ in nothing observable"; "it should stay open and be recorded in I08 as making no difference".
- The external reader (E05), as at L123; the check's H01 (a composite of settings counted as an edit to the rule).

**Ruling: KEEP.**

Reasons:
- **"The rule" is settled by the words.** L347's "variable under edits to \(C_r\)" stands where L125 has "variable under edits to the rule", with \(C_r\) the rule relation. Since the component's own signature varies under edits to the rule, the rule is its relation.
- **A setting of the component's own output is not an edit to the rule.** L57 says so: "a rule's application changes when the rule is edited and not when the world is intervened on; a cause's assignment changes under intervention". It sets editing a rule against intervening. If a setting of its own output counted, every causal assignment would meet the rule bullet's change clause (GLM part 1, reply line 25, makes the same point).
- **"The world" makes no difference.** Its two readings (every port the component does not assign, or the ports it reads) give the same family, because by L119 an intervention on a port the component does not assign never alters it. GLM's argument holds, and Mimo agrees that the main line is settled.
- **So Mimo's rewrite repeats the text in the maths' words.** Its "settings of the ports it does not assign" would also fix which edits count as settings when a composite sets several ports. That is H01, which L119 and L57 leave where the L119 ruling puts it.
- **The same contrast of L57 bears on H01.** A composite of settings is an intervention, not an edit to a rule. The maths' classing of it as "an edit to the rule of each component it alters" is I08's choice and not the text's, so the collapse of the families on C2* tells against that choice (see H01).
- **I08** comes to: settled in the respects that matter (L347, L57); its "world" alternative is idle under L119 and stays open.

### L127

> L127 | These are descriptions of patterns in (K), not additional data. The semantics never asks whether a component "is" a cause. It asks what its signature is. In particular, a part that reads or reports another part has a measurement's signature: change only the reading and the part it reports stays as it was; change the part and the reading follows. Which of the two an account offers as producing an outcome is fixed by that signature, not by the account's wording.

Five sentences (S1 to S5). Challenges fall on S1, S2-S3 and S4; S5 is named by the external reader's E05 and E07.

**S1 (FC13).** "These are descriptions of patterns in (K), not additional data."
- Mimo (part 2, reply lines 22-30 and 90; M2-B5): "The classification of an edit is read off the whole organization, not off j's own (K)"; hand model: two organizations with the same \(\operatorname{sig}_C(c_o)\) and the same C in which \(\mathrm{Rule}_C(c_o)\) fails in one and holds in the other, because whether the edit is a setting or observation edit depends on \(c_m\); "the maths should stand; the words should widen (K)"; proposes "These are descriptions of patterns in (K) and in how the edits of the contract touch the other components, not additional data."
- GLM (part 2, reply lines 39 and 105): "Holds by construction; and its one worry — that under a declared `asg` the classification would need data beyond D and C — is settled by the text itself: 'No role assignment is supplied'".
- **FIX S1, with Mimo's wording.**
  - *GLM's argument answers a different point.* It answers the declared-assigner worry of FC13's Look, which is L109's first sentence's matter and which Mimo does not dispute ("not additional data" stays). It does not answer Mimo's point.
  - *Mimo's point, checked by hand.* Mimo's model: \(X_m=X_o=\{0,1\}\), one boundary. \(c_o\) on (m, o) with \(L(1,b)=\{o=m\}\) and \(L(a,b)=\{o=0\}\) in both organizations. In D1, \(c_m\) assigns m and \(a\) leaves it, so \(a\) is a setting of o and, under R-i, an observation edit, and \(\mathrm{Rule}_C(c_o)\) fails. In D2, \(a\) also replaces \(c_m\) by {m = 0}, so \(a\) is no setting edit, I08 counts it an edit to \(c_o\)'s rule, and \(\mathrm{Rule}_C(c_o)\) holds.
  - *That model rests on the classing of a composite of settings as a rule edit (H01, I08).* The L125 ruling finds that classing the maths' choice, not the text's.
  - *The point stands without it, from L109's own words.* An observation edit is one that "alters the relation reporting it without altering what it reports". Whether an edit of C is an observation edit for \(j\)'s reading therefore turns on whether it alters the reported part, which is another component, and \(j\)'s own signature does not record that.
  - *Example (by hand), resting on I04, I06 (R-ii, "what it reports" compared at the level of relations) and I09, and not on H01 or I08.* Let \(c_m\) have footprint {m}, and let \(C\) hold the baseline, a setting \(s\) of o that replaces \(c_o\) only, and an edit \(r\) that alters \(c_o\)'s relation without setting o. In one organization \(r\) leaves \(c_m\) as it was; in the other \(r\) also alters \(c_m\)'s relation without setting m. \(\operatorname{sig}_C(c_o)\) is the same in both, and so is \(C\).
    - In the first organization, \(r\) is an observation edit for (o, m) under R-ii, and \(c_o\) changes under it, so \(c_o\) is no causal assignment.
    - In the second, \(r\) alters what \(c_o\) reports, so it is no observation edit; \(s\), a setting of o, is not one under R-ii; so \(c_o\), which changes under \(s\), is a causal assignment.
    - Under R-i the families of this pair coincide, but whether \(r\) is an observation edit still differs between the two organizations.
  - *So the families are patterns in \(j\)'s (K) read against classes of edits fixed by how the edits touch the other components.* FC13's own formal statement says so ("of sig_C(j) and of how each edit of C is classed"). S1 as written invites the reading that a component's family can be read off its own signature, which the words of L109 and L119 do not give. Mimo's wording says what the families use, and keeps "not additional data".
- **S2-S3 (FC14).** "The semantics never asks whether a component "is" a cause. It asks what its signature is." Mimo (part 2, reply line 92) notes that the program's syntactic scan "is weaker than the sentence (it cannot rule out an equivalent definition); what carries the sentence is that every family predicate is indexed by C". That is a remark on the maths' evidence; it proposes no change and none is needed. **KEEP S2 and S3.**

**S4 (FC07, FC08, D4.6, I06, U5; E05).** "In particular, a part that reads or reports another part has a measurement's signature: change only the reading and the part it reports stays as it was; change the part and the reading follows."
- GLM (part 2, reply lines 29, 37, 97; G2-B3; FC07 (d)): "on the contract C1 of settings of H and θ — the text's own worked case ... c_L is in **no** family on C1, under either reading ... L127's unhedged 'a part that reads or reports another part has a measurement's signature' is therefore false of the text's own example on one of its own contracts; the failure needs no invention"; proposes "In particular, a part that reads or reports another part has a measurement's signature on a contract that holds an edit altering its reading: change only the reading and the part it reports stays as it was; change the part and the reading follows where the reading depends on it."
- Mimo (part 2, reply lines 40-48; M2-B7; FC08): the witness is "a counterexample to L127's gloss as an unpacking of the signature"; L119 keeps solution conditions out of (K), "so the family cannot carry 'the reading follows'"; proposes "change only the reading and the part it reports stays as it was; change the part and the reading follows — the first is a pattern in (K); the second is a condition on the solutions, which (K) does not carry and the family does not require."
- Mimo (part 2, reply line 54; I06): L127's "a part that reads or reports another part has a measurement's signature" with "change only the reading" settles I06 for R-i (that item is the checker of L109's).
- The external reader (doc L140-L142, E05): the patterns "do not automatically provide the sharp semantic classification the surrounding prose suggests".
- **FIX S4.** Two faults hold, each on the text's own words.
  - **(a) The sentence names no contract.** Every family is a pattern on a contract (L113, "Fix an organization \(D\) and a contract \(C\)"). The measurement bullet has a change clause, "variable under edits to the measuring relation", which a contract meets only if it holds such an edit (FC12, which neither reader disputes).
    - On the pole's C1 (settings of H and θ), no edit alters \(c_L\), and \(c_L\), which reads H and θ, is in no family under either reading of observation edits. FC07 computes this; this checker reran it.
    - So the sentence, unhedged, fails on the text's own case. GLM's argument holds, with one precision: it rests on "variable under" read as "some edit of the class alters it", which is the contrast the text itself draws with "invariant under" (L113 ruling, point 2). Under a universal reading, "variable" would hold vacuously on C1.
  - **(b) The gloss's second clause concerns solutions, not (K).** "change the part and the reading follows" speaks of values in a solution; L119 says a signature is built "not from the values its ports take in a solution".
    - FC08's witness (point 2 of the L124 ruling) meets both clauses of L124 and its reading does not follow the part.
    - Both readers agree on this, and so does the formal core's §4 Vague note.
- **Why this wording, and not either reader's.**
  - *The hedge.* It names "an edit to its measuring relation", the class of L124's own change clause. The sentence then holds under whichever reading L109's checker gives observation edits, since each reading of "edits to the measuring relation" (I07) follows it. The invariance clause holds of every part that reads a port another part assigns (L119; FC06).
  - *GLM's hedge does not do this.* "an edit altering its reading" includes a setting of the reading under R-ii, where L124's change clause does not count one. On the pole's C2 under R-ii, \(c_L\) reads H and θ, C2 holds a setting of L that alters its relation, and \(c_L\) is a causal assignment and no measurement (FC07). GLM's sentence would still fail there. Its "where the reading depends on it" goes with its L124 dependence clause, which the L124 ruling does not adopt.
  - *The gloss.* It keeps both of the text's plain-language clauses, which say how a measurement shows. It says of each what it is: the first a pattern in (K), the second a pattern in the values of a solution, which (K) does not record and the family does not require. This is Mimo's content in the text's words; "(above)" points to L119's "the values its ports take in a solution".
  - *Why not "the first ... the second".* Mimo's "the first ... the second" is not used, because S5 goes on "Which of the two", and "the two" there means the reading part and the part it reports.
- **E05 on L127.** The FIX removes what E05 finds the prose around the bullets suggesting beyond the patterns: that a reading part has a measurement's signature whatever the contract, and that its reading follows. Where the contract holds no edit to the reading alone, the reading part and a response share their families (FC-E3), which the text says itself at L11 and in S6 of L119.

**S5 (E05, E07).** "Which of the two an account offers as producing an outcome is fixed by that signature, not by the account's wording." Not challenged by Mimo or GLM. The external reader's E07 (context) credits the text with separating a readout from a cause once the contract holds an edit that changes the readout without changing the memory (FC-E4). That is an instance of S5 read with the S4 hedge: "that signature" is the measurement's signature on such a contract. **KEEP S5.**

**Ruling on L127: FIX.**

- old (exact span of L127, S1 to S4):

```
These are descriptions of patterns in (K), not additional data. The semantics never asks whether a component "is" a cause. It asks what its signature is. In particular, a part that reads or reports another part has a measurement's signature: change only the reading and the part it reports stays as it was; change the part and the reading follows.
```

- new:

```
These are descriptions of patterns in (K) and in how the edits of the contract touch the other components, not additional data. The semantics never asks whether a component "is" a cause. It asks what its signature is. In particular, a part that reads or reports another part has a measurement's signature on a contract that holds an edit to its measuring relation: change only the reading and the part it reports stays as it was, a pattern in (K); change the part and the reading follows, a pattern in the values the ports take in a solution (above), which (K) does not record and the family does not require.
```

- S2 and S3 are unchanged inside the span; the span is given whole so that one exact match applies both changes.
- **Dependents.**
  - L109's "that is, when the component assigning it has a measurement's signature (below)" points here and at L124. It reads as before, though "has a measurement's signature" now depends on the contract holding an edit to the measuring relation. That matches FC11 and matter 5's point that L109 equates a condition on A with a signature on C; the clause is the checker of L109's (shared note).
  - L151 ("A measure that identifies an outcome ...") reads as before.
  - L37 and L57 read as before.
  - L325 ("An intervention on \(L\) replaces its component and leaves \(H,\theta\) unchanged") reads as before.
  - I06's register entry quotes the old gloss, and the round-1 critical review's C07 reasoning ("an intervention on the reading is, by L109, an observation edit") quotes nothing of S4; both are records, not text.
- **The owner's words.** No word S23 forbids ("require", "record" and "pattern" are not among them). No list, count, grade or record doing the explanation's work (S20); "(K) does not record" speaks of the display (K). Nothing about what must happen (S21), no physical possibility (S25-S27), nothing settled (S28), nothing about hard to vary or values.

## Item by item (primary items: what each comes to)

**D4.2 (one kind on C; L119 S1).** The words should stand, and the maths may stand beside them as a reading with one recorded addition. D4.2 says what S1 says once coordinates are renamed (β_*), which is what "coincide" asks. I10's equal-domain clause is more than the words say, and no result of the text turns on it (L119 ruling, S1). No change to either is required by this round; the maths keeps the clause as I10.

**D4.3 (reading through a transport).** The maths should stand, and the words now carry it. D4.3 reads the candidate's component at \((\tau(a),\sigma(b))\), as L556's formula does; L119's S4 and S5 named τ only and now name σ (FIX). The comparison as functions on C stays I12's choice.

**D4.4 (signature of a counterpart).** The maths and the words agree. "up to the port translation" (L119), with L233's and L556's \(\operatorname{proj}^{\lambda}_{V_k}\), is D4.4's carrying to \(V_k\). The part of D4.4 that is the maths' own is I13 (extending (K) to a subnetwork), which is L556's matter (matter 1; the checker of L554-L558).

**D4.5 (change and invariance on a contract).** The maths stands as a reading of the words, and the words stand. The same-boundary comparison, the existential "variable" set against the universal "invariant", and vacuous invariance are what the words give (L113 ruling, point 2). The residue, I09's alternative (b), turns no result, so I09 stays open. GLM's L113 wording is not adopted (it drops (K)'s lead-in).

**D4.6 (families).** The maths stands as a reading of L123-L125 with the inventions it names (I04, I06, I07, I08, I102) and two it does not (H01, H02). The words stand at L123-L125. L121 now says which bullet the fourth name falls under (FIX), and L127 now says that a reading part's measurement signature needs a contract holding an edit to its measuring relation, and that "the reading follows" is not part of the family (FIX). What the maths should look at again:
- under R-ii the measurement and rule-application change clauses coincide for a component reading a port another assigns (Mimo, part 2, line 84; checked by hand), so the two families overlap wherever such a component's relation is edited other than by setting its own output;
- H01 and H02 (below).

**FC05 (kinds fixed by relations).** The counterexample tells against one reading of L119's last clause, I93's reading (ii), which the words admitted ("stay equal", with "equal" for relations on two footprints read as "equal under some footprint bijection"). It does not tell against FC05's formal sentence (one bijection throughout), which holds and holds by construction, nor against (K). The FIX of L119 writes reading (i) in, and the counterexample no longer bears on any reading of the sentence. Reproduced by this checker with the program, and worked by hand.

**FC06 (a setting edit leaves every reader's relation as it was).** The claim stands; it is L119's first clause read for single settings, which is what the "only" of that clause says. Mimo's two breaks:
- (1) Two components each replaced by a setting of p, so asg(p) is undefined. Checked by hand. It tells against the formal statement's wording in `formal claims.md` ("every component j ≠ asg(m)"), not against the text. The program already quantifies only over ports with a defined assigning component (`model/claims_a.py`, `fc06`: `for m, jm in R.asg.items()`), which the formal statement does not say (a new unrecorded choice, below).
- (2) A composite in Set_H alters \(c_L\). This rests on H01's first alternative, which L119's "only" does not give.

**FC07 (the families on the pole's contracts).** The computations stand; this checker reran them. They tell against the text at one place, L127's unhedged "a part that reads or reports another part has a measurement's signature", which fails on C1 under both readings (GLM's attack; no invention beyond the text's own "variable"). The L127 FIX removes that.
- The C2 results differ between R-i and R-ii. That is I06's fork, the checker of L109's.
- Mimo's reasoning that under R-i no component reading a port assigned by another is ever causal was checked by hand, and agrees with the program. It shows what R-i costs the causal family, and it is a point for I06's ruling.
- The C2* part rests on H01's default with I08, which the text does not give (see H01).
- GLM's second attack (one-valued domains empty the causal family) fails as stated. With \(X_o=\{x\}\) and \(j\) on (u, o) with relation {(0, x)}, the setting o = x replaces \(j\) by {(0, x), (1, x)}, which alters it. Checked by hand.

**FC08 (L127's gloss has a clause about solutions).** The witness tells against the text, at L127's gloss, and not against L124 or an invention. The mismatch is between L119 ("not from the values its ports take in a solution") and L127 ("change the part and the reading follows"), on the text's own words; the witness's construction uses I04, I06 and I07 only to exhibit it. Rerun and checked by hand. Removed by the L127 FIX. GLM's repair at L124 is not adopted (L124 ruling).

**FC09 (four names, three families).** The maths and the words agree. L347's pattern is L125's word for word with \(Z\) and \(C_r\) in place of "the world" and "the rule", so a constitutive status falls under the rule-application family without I08. Mimo's point that the program cannot tell I08 from its alternative (b) concerns the maths' evidence; (b) is excluded by L125's own "variable under edits to the rule", since under (b) the family is empty (L119). The words now say so at L121 (FIX).

**FC12 (invariance clauses can be vacuous; change clauses cannot).** The maths stands, and it is the text's own structure (both readers). It is the ground of the L127 FIX's hedge: a change clause needs a witness in the contract. The external reader's E05 bears on it only through L127.

**FC13 (the families are patterns in (K), not additional data).** The maths' formal statement stands ("of sig_C(j) and of how each edit of C is classed"). The words said less: the widened S1 of L127 (FIX) now says what the formal statement says. The declared-assigner half is settled by L109's "No role assignment is supplied" (GLM). Mimo's model, and this checker's variant that does not rest on H01, were checked by hand.

**FC14 (no definition asks whether a component "is" a cause).** Words and maths agree; L127's S2 and S3 stand. Mimo's remark concerns the strength of the program's syntactic scan, not the sentence.

**I07 ('the measured port', 'the measuring relation').** The text settles it in substance.
- The measuring relation is the measuring component's own relation (L124's grammar: its own signature is "variable under edits to the measuring relation"; L127, "change only the reading").
- The measured port is a port it reads and another part assigns (L127, "a part that reads or reports another part").
- No port is declared (L109, "No role assignment is supplied"; L127, "not additional data").
- "the measured port" is read per port measured.
- No wording is needed. GLM's G2-B2 is not adopted (L124 ruling, point 1).

**I08 ('the world', 'the rule').** The text settles "the rule" as the component's own relation (L347's "edits to \(C_r\)"; L125's "variable under edits to the rule"). It also settles that a setting of the component's own output is no edit to its rule (L57's contrast of editing a rule with intervening). "The world" as every port it does not assign, against the ports it reads, is left open, and makes no difference to the family under L119. One further point for the maths, from the same contrast: I08's "edits that alter L_j without setting j's output" counts a composite of settings as an edit to the rule, which L57 does not (H01).

**I10 (kinds: a footprint bijection between equal value domains).**
- The text settles it against the register's alternative (b): L119, "A kind is an equivalence class of components under this relation"; Mimo's non-transitivity model was checked by hand.
- The text settles it against the value-recoding alternative (a): "a bijection of their footprints" names a map of ports, and "coincide" is sameness of the renamed relations.
- It leaves the equal-domain clause open, and it should stay open: no result of the text turns on it once I94 is excluded.
- The owner-question mark is taken up below.

**I11 (coarser and finer: fewer and more pairs).** The text settles it: L39, "At a finer level with more admitted changes they may separate"; L317, "A finer contract that contains a change at which two rivals conflict makes a new question". No wording needed.

**I12 (reading a candidate's component through the transport; τ[C]).**
- The text settles σ on boundaries and τ[C] as a set of pairs at L556 (the check's T04). The FIX writes σ into L119 so that L119 agrees with L556 (**settles I12, in part**).
- What I12 still chooses, comparing the two signatures as functions on C and not as sets of triples, stays open. L556's "(F1) equates the third coordinates pointwise" leans to it, and Mimo's FC16 attack found no fault in the text there.
- τ[C] at L554 is the checker of L554's.

**I93 ('the two relations stay equal': under which bijection).** The text should now settle it, and the L119 FIX does: reading (i), the bijection by which the two components are of one kind on C. Reading (ii) is what the words admitted and what fails (FC05).

**I94 (the counterpart read untranslated).** The text settles it against the invention: L119's "up to the port translation" with L233's "carrying what remains to \(V_k\) by the port translation of \(\lambda\)" and L556's \(\operatorname{proj}^{\lambda}_{V_k}\) (the check's T03; GLM). I94 is a stress test of I10's equal-domain clause, not a reading of the text, and FC18's counterexample under it tells against no sentence.

**I102 (a component assigning several ports, or a port assigned by none).** The text leaves it open: it presumes one assigning component per port (L103, L109, L119) and one output port per causal assignment (L123). It should stay open in the text. The maths should record U5 as a consequence of I102's second clause and trim that clause so that a port no edit sets is not counted among a component's measured ports when the component is the one that computes it. Both readers agree the text's "another part" (L127) is against U5's case.

**U4 (a third reading of 'stay equal').** Settled by the L119 FIX, which writes I93 (i). U4's condition, each relation as it was at (1,b), is a sufficient condition for (i) where (1,b) ∈ C, and not a reading of "stay equal": two relations staying equal to each other is not each relation staying as it was. GLM's U4 wording (G3-B7) is not adopted.

**U5 (under I102 a component can have the measurement signature for its own output port).** The text is against it: L127's "another part" and L109's "the component assigning it". The fault is in the maths' I102, and the fix is there. GLM's closure through "does not itself determine" is not adopted, because it removes every invertible reading from the family (L124 ruling, point 1).

**H01 (a composite of settings is no setting edit, so it is an edit to the rule).** The text settles the first half and not the second.
- *The first half.* L119's "only", as D2.1 reads it (GLM: "most literally"): an edit that sets a port in that sentence's sense replaces one component, so a composite that replaces two is not such an edit.
- *The second half.* It is the maths' choice through I08, against L57's contrast of editing a rule with intervening. So the collapse of the families on C2* tells against I08's classing of composites, not against the text.
- *What stays open.* Whether a composite of settings is an intervention "on its output port" (L123) or "on the measured port" (L124), the text leaves open, and should leave open for now. Mimo's wording contradicts L119's "only ... not the relations of the components that read it" on the edits it adds; GLM's declares every edit that replaces several components together "no rule" edit, which a joint change of rule is.
- *For the maths.* Record the choices and compute the families under them in a later round (D2.1, D4.6, I08 to be formalized again).

**H02 ("its output port" read as the port the component assigns).**
- The words point to L109's "output" (GLM's argument: the text's own defined term).
- By L119 the two readings pick out the same causal assignments except for a component that assigns a port its relation leaves undetermined. That case is the text's "output" and "assigning" coming apart, which is E04's matter at L103 and L109.
- The maths should record the departure, or use D2.3's outputs with a union, as GLM says. No text change.

**matter 4 (L121 names four things and gives three bullets).** The text needed a change and has it: the L121 FIX says, where the four names are given, that a constitutive status has a rule application's signature, pointing to L347.

**E05 (the families do not give a sharp classification; kinds beyond the signatures).**
- *Where it tells against the text.* It tells against L127's second sentence, which gave every reading part a measurement's signature whatever the contract, and glossed it with a clause about solutions. The L127 FIX removes both.
- *Where it does not.* It does not tell against L121-L125. They define families by patterns on a contract and do not say that the families exclude one another. The text says in three places that components no admitted change separates are one kind at that level (L11; L39; L119's S6).
- *Reproduced.* The external addendum's FC-E3 (rerun by this checker): the response Y := X and the reading N := X share every family on contracts without an edit to the reading alone, and part once such an edit is in the contract.
- *Second half.* "Argument 1 ... does not independently establish that those signatures exhaust every scientifically important sense of kind" is a finding about scope. It concerns what the text's "kind" covers (L11, L558, (Elim) at L540), and changes no line of this group.

## Shared items (weighed on this group's lines only; what each comes to is its primary checker's)

- **D2.1 (here L119).** GLM's G2-B6 at L119 (a composite "sets no port, edits no rule") is not adopted. Mimo's M7-B1 and GLM's G7-B1 and G1-B3 and Mimo's M1-B3 fall on L103, not here. L119's first clause stands and refers to L103 by "(above)".
- **FC18 (here L119).** Mimo's M3-B2 at L119 is not adopted: L119's "up to the port translation", with L233 and L556, already gives D4.4's reading, under which FC18 holds (the check's T03; GLM). The σ added to S5 does not touch the counterpart's reading. The counterexample rests on I94 with I10's equal domains and I14's value maps, and tells against no sentence of L119.
- **I09 (here L119).** GLM's G2-B5 at L119 (and G1-B6 at L113) is not adopted; reasons at L113, point 2.
- **matter 5 (here L113).** Mimo's M1-B8 and GLM's G1-B6 at L113 are not adopted (L113 ruling, points 1 and 3). L113 already names the contract.
- **L123 (the round-1 change; here L123).** The removal stands on the reason all four replies give. GLM part 1's "model two" does not hold for the pole's \(c_H\), whose footprint is {H} (L123 ruling, point 3). Mimo's reasoning for components that read a port another assigns does hold under R-i.
- **E04 (here L119).** Nothing changes at L119: "(above)" carries whatever L103 and L109 are ruled to say about the component assigning a port.
- **E07 (context).** L127's last sentence stands; the external reader's example is an instance of it read with the L127 FIX's hedge (FC-E4, as recorded by the addendum; not rerun here).

## Shared notes (for the checkers of other lines; no ruling on them here)

1. **For the checker of L109 (I06, matter 5, D2.4, E04).**
   - *Under R-i, no component that reads a port assigned by another component is ever a causal assignment, on any contract.* Mimo, part 2, reply line 84; checked by hand, and it agrees with FC07 (\(c_L\) under R-i) and FC-E3 (\(c_Y\), \(c_N\) under R-i). A setting of the component's own output alters it and leaves the other assigner, so under R-i it is an observation edit, and the invariance clause of L123 fails at the pair where the change clause is met. This is what R-i costs L123's family; the pole's forward component \(c_L\) is then never causal.
   - *GLM's two parts take opposite readings of I06.* Part 1 adopts R-ii ("R-ii should stand", reply line 19); part 2 adopts R-i ("It should take R-i", reply line 59). GLM part 1's "model two" (\(c_H\) unsatisfiable under R-i) does not hold on the pole as the text gives it (\(H:=U_H\); footprint {H}).
   - *The L127 FIX is written to hold under either reading.* Its hedge names L124's own class ("an edit to its measuring relation"), whichever reading L109's observation takes.
   - *The "that is" clause.* L109's "that is, when the component assigning it has a measurement's signature (below)" now points to a sentence (L127) that makes the measurement's signature depend on the contract holding an edit to the measuring relation. That agrees with matter 5's point that the clause equates a condition on \(A\) with a signature on \(C\).
2. **For the checker of L91-L103 (D2.1, E04).**
   - L119's first clause refers to L103 by "(above)". Any wording given at L103 for "the component assigning that port" reaches L119 unchanged, and needs no echo here.
   - H01's first half (a composite that replaces two components is not an edit that sets a port in L119's sense) is what L119's "only" says. A rewrite of L103 that made a composite "set each" port would contradict L119's "not the relations of the components that read it" on those composites.
3. **For the checker of L554-L558 (FC18, I12, I13, matter 1).** L119 now reads the candidate's component "through \(\tau,\sigma\)", as L556's second formula has it. L554's \(\tau[C]\) and L556's "By (K)" are that checker's; nothing at L119 depends on how they are ruled.
4. **For the checker of L57 (FC10, I09).** The L113 ruling reads "variable under" as the contradictory of "invariant under" (some edit of the class alters the relation). That is the existential reading Mimo gives from L123's own contrast, and it is what the L127 FIX's hedge relies on. Nothing in this group depends on how L57's "changes when the rule is edited" is ruled.
5. **For the orchestrator and the maths (not a text change).** The families L123-L125, as the maths writes them, carry most of their content in their change clauses. Under L119 the invariance clauses of L124 and L125 hold of every component that does not assign the port intervened on (FC06). So under R-ii measurement and rule application coincide for a component reading a port another assigns, and under R-i measurement contains rule application for such a component. The text does not say that the families exclude one another, and nothing here asks it to. It is recorded so that a later round formalizes the families with H01's choices and asks what, if anything, keeps rule application apart from measurement.

## New inventions (choices no register entry records)

1. **FC06 as computed quantifies only over ports whose assigning component is defined.** `model/claims_a.py`, `fc06`, loops `for m, jm in R.asg.items()`, and its statement string says "∀m with asg(m) defined". The formal statement in `formal claims.md` says "for every port m, every setting edit a of m and every component j ≠ asg(m)", with no such restriction. Mimo's first break of FC06 (two components each replaced by a setting of p) falls in the gap.
2. **I08's reading of "edits to the rule", applied to an edit that sets \(j\)'s output together with a change to another component that sets no port.** It counts such an edit as an edit to \(j\)'s rule, since the edit is no setting under D2.1 and alters \(L_j\). The check's H01 records this for composites of settings only; the mixed case (a setting of one port with a rule change of another component) is not recorded. Mimo's FC13 model in D2 is of the composite kind; the mixed kind arises in the same way.

## Owner questions

1. **D4.2, I10, FC18: Mimo's mark "the owner's question (where values are placed)".** Recorded with both sides, as rule 9 asks.
   - *Mimo's side* (part 3, reply lines 3, 57, 61): whether a footprint bijection may recode port values (I10 (a)) or must join ports of equal domains is "where values are placed", which the owner has reserved; so the equal-domain clause stays open, with no proposal.
   - *GLM's side* (part 3, reply line 44): "nothing in the owner's decisions points either way"; write in the equal-domain choice.
   - *This ruling.* The owner's words that name the question are S31's: "maybe even figure out, for example, whether values should be part of the theory, or separate". The maths reads them so: "The appraisal relation 𝒩 appears only as a typed input (D14.8); where values are placed is the owner's question". On that reading the phrase concerns values that an appraisal places, not the value domains of ports. So the point is ruled on its arguments (I10: settled against (a) and (b) by the words; the equal-domain clause left open), and nothing at L119 moves any value in the owner's sense.
   - *The present wording leaves the matter as the owner's words leave it.* L119 says nothing about appraisal or values in that sense. If the owner reads "where values are placed" as including port values, the open equal-domain clause is where that question would sit; nothing in this ruling closes it.

## Parked points

None. No point on the items of this group concerns what hard to vary covers.

## Claims and definitions to formalize again (their sentences change)

- From the L119 FIX:
  - D4.3 and D4.4 (S4 and S5 now name σ);
  - FC05 and FC06 (they quote S8, whose second clause changes; FC05's formal reading (i) is now the sentence's);
  - FC16 (it quotes S4);
  - I12, I93, I94 and U4 (register entries quoting S4, S5 or S8);
  - the check's T02 and T04 (they reason from the old wording).
- From the L121 FIX: FC09, D4.6 (its line "A constitutive status is Rule_C (L347; FC09)").
- From the L127 FIX:
  - FC13 and FC14 (they quote S1 to S3);
  - FC07 and FC08 (they quote S4's old wording);
  - D4.6's closing note ("Each family predicate is a function of D and C alone (FC13)");
  - I06 (it quotes S4's old gloss);
  - the formal core's §4 Vague note on L127's gloss;
  - the external addendum's FC-E3, which quotes S4's old wording ("a part that reads or reports another part has a measurement's signature"), read again against the hedge.
- Also (H01; no sentence changed): D2.1 with I08 on composites of settings, and D4.6 under H01's choices.

END OF RULING
