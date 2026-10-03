# S103 Round 1 — ruling on C06 (L115–L117)

*Written on 27 September 2026 by a fresh Opus 5.5 checker that built nothing of this round, read no reply before this task, and rules on no other candidate of it (rule 5 of `results/S103 Round 1 - how the replies will be read, written before sending.md`). This file obeys decision S23 except where it quotes the text, a reply or the owner. Nothing here is settled (S28): the ruling is reasons why this and not that, open to any later criticism.*

**Ruling: KEEP.** The display stands as it is.

**File name.** The reading rule (rule 11) names `results/S103 Round 1 - rulings/ruling C<nn> L<line>.md`; this file is at the path the orchestrator's task gave, `results/S103 Round 1 - reading/rulings/ruling C06.md`, as the other rulings of this round are.

## What was read

- The text under review, `tests/99 The semantics, standing alone.md` (md5 74f4a4c7619345747f4fa976ddac9548, checked before reading): L1–L200 whole, and every line that uses (K) or a signature (found by searching for `sig`, `(K)` and `signature`): L11, L37, L57, L103, L109, L111–L127, L229–L247, L279–L281, L345–L347, L518–L528, L550–L568.
- The part 1 brief's section for C06 (`tests/S103 Round 1 - trying to vary the strong candidates - part 1, Parts 0 and II.md`, lines 131–141), which points the readers to L85–L105, L233–L253, L281, L554–L558 and L520.
- The tabulation's section for C06 (`results/S103 Round 1 - reading/tabulation.md`, lines 517–629).
- Mimo's section on C06 (`s103_vary_mimo_1.response.txt`, lines 120–150) and GLM's (`s103_vary_glm_1.response.txt`, lines 111–135), and every other line of the six replies that names C06, (K), L115–L117 or `sig` (a search): none of those other lines alleges anything about (K) itself; they use it in arguing about C04, C05, C07–C12 and C29.
- The S98 ledger's entry for this display (`results/S98 Ledger of edits and recommendations/line-up/groups/02 Organizations and their changes (Part II).md`, "L115.s1 · display · lines 115–117 · no change recorded"), and the S89 case book, searched for cases that turn on signatures or kinds (none does).
- The owner's decisions S20–S35 in `records/Semantics - Decisions.md`.

Every quotation of the text below was compared with file 99 by program (`grep -F` on its own line); every one was found there.

## The sentence

L115–L117, completing the sentence begun at L113 ("The **signature** of component \(j\) on \(C\) is"):

```
\[
\operatorname{sig}_C(j)=\{(a,b,L_j(a,b)):(a,b)\in C\}. \tag{K}
\]
```

Its terms: \(C\subseteq A\times B\) (L113); for each \(j\), \(a\) and \(b\), "the interpretation supplies" (L91) \(L_j(a,b)\subseteq\prod_{v\in V_j}X_v\) (L94). So (K) is defined at every pair of \(C\), and each third entry is a relation on \(j\)'s footprint.

## What the text asks of it

Read by line, the text uses (K) for these, and for nothing else:

1. **Kinds, compared under a footprint bijection.** L119: "Two components \(j,j'\) are **of one kind on \(C\)** when there is a bijection of their footprints under which \(\operatorname{sig}_C(j)\) and \(\operatorname{sig}_C(j')\) coincide." and "A kind is an equivalence class of components under this relation."
2. **Kinds relative to the contract, and built from relations, not values.** L119: "Kinds are therefore relative to the contract; a coarser contract identifies more components, and two components of one kind on \(C\) may separate on a finer contract. A signature is built from a component's relation under each \((a,b)\in C\), not from the values its ports take in a solution; two components that differ only in those values are of one kind on \(C\), whatever the difference is called." and "An edit that sets a port replaces only the component that assigns the port (above), not the relations of the components that read it, and an edit under which the two relations stay equal does not separate the components."
3. **The families of signatures, which need each relation tied to the pair it answers.** L123–L125, for instance L124: "a **measurement** has a signature invariant under interventions on the measured port and variable under edits to the measuring relation;"; L127: "These are descriptions of patterns in (K), not additional data."; L109: "that is, when the component assigning it has a measurement's signature (below)"; L347: "Its signature under (K) is invariant under interventions on \(Z\) and variable under edits to \(C_r\)."; and the grievances that point here, L37 ("That is a difference in edit-response, which is what the semantics asks about") and L57 ("That is a difference in edit-signature (Part II), and the semantics represents it exactly.").
4. **The step from (F1) to kinds.** L245: "By (K), no component of \(E\) whose signature on \(C\) differs from its counterpart's meets (F1); there is no further condition about kinds to state (Argument 1)."; L281: "Where \(C\) contains a change separating two kinds, (F1) already fails for a component whose counterpart is of the other kind. Where \(C\) contains no such change, the two are one kind on \(C\) by (K), and the condition would be asserting a distinction that \(C\) does not contain. There is no third case."; Argument 1, L556: "*Why this and not its denial.* By (K), \(\operatorname{sig}_C(\lambda(k))=\{(a,b,\operatorname{proj}^{\lambda}_{V_k}\operatorname{Sol}_{\lambda(k)}(a,b))\}\) and \(\operatorname{sig}_{\tau[C]}(k)=\{(\tau(a),\sigma(b),L_k(\tau(a),\sigma(b)))\}\). (F1) equates the third coordinates pointwise. ∎"; its consequence, L558: "The word "kind" is therefore eliminable from the definition of an account, and its elimination loses no case."; and Argument 2, L564: "(ii) By Argument 1, \(k\) has the signature of its counterpart on the ports its translation names".
5. **Its place in the order.** L520: "Kinds, from signatures (K)."; L526: "(K) depends on (O) and a contract. (F1), (F2), (A) depend on (O), (Q), (K)."
6. **What a kind is, in the front matter.** L11: "a *kind* is nothing over and above how a component responds to the changes that level admits. Two components no admitted change can separate are one kind at that level, whatever labels anyone attaches to them (Part II, Argument 1)."

So what the theory needs from (K) is this: a component's own relation under each admitted pair, each relation kept with the pair it answers, over the contract and nothing wider, with no port values in it and no other component's constraints in it.

## The readers' points, weighed

Both readers close HOLDS. Neither alleges a failure of the sentence itself. Each proposed wording is weighed here on its own argument; how many readers tried which is not weighed.

**Mimo (a), `\operatorname{sig}_C(j)=L_j|_C`, and GLM's function form, `\operatorname{sig}_C(j):C\to\bigcup_j\{L_j(a,b)\},\quad (a,b)\mapsto L_j(a,b)`.** Both readers say these break L556. They name the same object as (K): \(L_j\), taken as the assignment \((a,b)\mapsto L_j(a,b)\) that L91 supplies, restricted to \(C\), is as a set \(\{((a,b),L_j(a,b)):(a,b)\in C\}\), which is (K) itself wherever a triple is read as a pair whose first entry is a pair, and which carries the same information on any reading. Nothing in items 1 to 6 changes under them: kinds, their relativity to the contract, the families and (F1) all read a relation at each pair of \(C\), which both forms supply. What they would change is only L556's wording, "(F1) equates the third coordinates pointwise", which would be read as "equates the values at each pair". Mimo's "a restriction has no third coordinate" and GLM's "the pointwise-equality step loses its referent" therefore name a change of notation in L556, not a loss of anything Argument 1 does. On this reading these are rewordings that change nothing the theory needs, and (K) is easy to vary in its notation. Neither is clearer than (K): (a) hides the triples that L556 writes out, so L556 would have to be reworded to match; GLM's form has a codomain in which \(j\) is at once bound by the union and free on the left, and \(a,b\) are free, so it is not well formed as written. A rewording that is not clearer is no reason to change the display (rule 5): KEEP.

**Mimo (b) and GLM's coordinate-free form, `\operatorname{sig}_C(j)=\{L_j(a,b):(a,b)\in C\}`.** A different claim. It keeps which relations occur and drops which pair each answers. Take \(C=\{(1,b_0),(a_1,b_0)\}\), a component \(j\) with relation \(R\) at the baseline and \(R'\) under \(a_1\), and \(j'\) with \(R'\) at the baseline and \(R\) under \(a_1\), on one footprint. Under this form their signatures coincide and they are one kind, though the baseline itself separates them. That breaks L11 ("nothing over and above how a component responds to the changes that level admits"), L281 ("Where \(C\) contains no such change, the two are one kind on \(C\) by (K)", which no longer follows, since here \(C\) holds a separating change and they are still one kind), and the families at L123–L125, which ask under which edit the relation changes (Mimo's point on L57; GLM's on L119's reading "through \(\tau\) and \(\tau'\)", which has no pairs left to translate). The break is shown; the rival is set aside.

**Mimo (c), `\operatorname{sig}_C(j)=(V_j,\{(a,b,L_j(a,b)):(a,b)\in C\})`.** Either idle or a different claim. If L119's bijection is applied to the first entry too, it always carries \(V_j\) onto \(V_{j'}\), so the added entry does no work and the kind relation is that of (K). If it is not, coincidence asks \(V_j=V_{j'}\), and no two components on different ports are ever one kind; that breaks L119's "bijection of their footprints" (Mimo's point) and, across organizations, L119's "up to the port translation" and L564's composed translations. The footprint is already carried by (K), since each third entry is a relation on \(\prod_{v\in V_j}X_v\) (L94). Set aside.

**Mimo (d), `\operatorname{sig}_C(j)=\{(a,b,\operatorname{Sol}_D(a,b)|_{V_j}):(a,b)\in C\}`.** A different claim. It builds the signature from the values the ports take in solutions of the whole of \(D\), which L119 excludes in so many words ("not from the values its ports take in a solution"). It also moves every reading component: let \(c\) assign \(x\) and \(m\) report \(x\) as \(y\) (\(y=x\)); an edit \(a\) that sets \(x\) replaces \(c\) (L103) and leaves \(L_m(a,b)=L_m(1,b)\) (L119, "not the relations of the components that read it"), but it changes \(\operatorname{Sol}_D(a,b)|_{\{x,y\}}\). Under (d), \(m\)'s signature would vary under intervention on the measured port, against L124, L109 and L127 ("change the part and the reading follows", where what follows is the value, while the relation stays). Mimo's break of L556's second display and (F1) stands as well: (F1) equates a component's own relation, \(L_k(\tau(a),\sigma(b))\), not a projection of all of \(E\)'s solutions. Set aside.

**GLM's baseline form, `\operatorname{sig}_C(j)=L_j(1,b_0)`.** A different claim. It no longer depends on \(C\) beyond one pair, so L119's "a coarser contract identifies more components" loses its content (GLM's point), and a cause and a measurement with one baseline relation become one kind, against L123–L124 and L37's "a difference in edit-response". Set aside.

## A failure of the sentence itself, sought

- **Defined where used.** \(L_j(a,b)\) is supplied for every component, edit and boundary (L91), so (K) is defined at every pair of any \(C\subseteq A\times B\). GLM's point that "(K) is total on \(C\)" stands.
- **No circularity.** (K) uses only \(L_j\), from (O)'s data, and \(C\); L526's order ("(K) depends on (O) and a contract") matches it.
- **No part idle.** Each entry of the triple is used: the pair, by L119's reading through \(\tau\) and by the families; the relation, by (F1) and L119's last sentences. The subscript \(C\) is used by L119's relativity.
- **The kind relation is an equivalence under (K).** The identity bijection, the inverse and the composite of footprint bijections give reflexivity, symmetry and transitivity, as L119's "equivalence class" asks.
- **A subnetwork read by (K).** L556 writes the signature of \(\lambda(k)\), a subnetwork of \(D\), not a component; (K) is stated for a component. The reading is supplied at L119 ("its counterpart \(\lambda(k)\), read on \(C\) directly with its hidden ports projected away, up to the port translation") and at L233, which names the projection ("(write \(\operatorname{proj}^{\lambda}_{V_k}\) for this projection)"): the subnetwork is taken as one component whose relation is that projection, and (K) is then applied as it stands. That bridge belongs to L119 and L556, not to this display, and it asks nothing of (K). Noted for whoever reads L119 or L556 next; not a point against C06.
- **No record doing the content's work (S20).** A signature is the component's own relations on the contract, which L127 says are "not additional data"; it lists no rivals and keeps no record of rescues.

No failure of the display itself was found.

## Cases

KEEP moves no case verdict. The cases the text ties to (K) are its own: the missing counterpart-kind condition (L281), constitutive rules (L347), Arguments 1 and 2 (L554–L568), and grievances 1 and 11 (L37, L57); the S98 ledger records no change and no case on L115.s1, and no S89 case turns on signatures. Each of them reads (K) as it stands.

## The owner's decisions

KEEP leaves the display unchanged, and this ruling proposes no wording. The display holds no word or idea S23 forbids, says nothing about what must happen (S21), brings in no physical possibility (S25–S27), settles nothing (S28), and says nothing about what hard to vary covers (S33, S34): no proposal here is parked, and no value is moved in or out. "Easy to vary" in this ruling is meant plainly, as the brief asks, not as the text's own term.

## For the structured result

- **Ruling:** KEEP.
- **Old = new (L115–L117):** `\[` / `\operatorname{sig}_C(j)=\{(a,b,L_j(a,b)):(a,b)\in C\}. \tag{K}` / `\]`
- **Easy to vary:** in notation only. Mimo's (a) and GLM's function form name the same object and change nothing the theory needs, and neither is clearer; every rival that changes what (K) says breaks a named use (L11, L119, L124, L281, L556).
- **Depends on it** (for the record; nothing changes): L109, L119, L121–L127, L245, L281, L347, L520, L526, L554–L558, L562–L564; and L11, L37 and L57, which point to Part II's kinds.
