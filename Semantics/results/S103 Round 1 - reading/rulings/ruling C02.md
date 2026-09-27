# S103 Round 1 — ruling on C02 (L41)

*Written on 27 September 2026 by a fresh Opus 5.5 checker that built nothing of this round and rules on no other candidate of it, under rules 5, 7, 9 and 10 of `results/S103 Round 1 - how the replies will be read, written before sending.md`. It writes to the path the orchestrator's task names (`results/S103 Round 1 - reading/rulings/ruling C02.md`), not to rule 11's `results/S103 Round 1 - rulings/ruling C02 L41.md`; the difference is the orchestrator's to settle. This file obeys decision S23 except where it quotes a reply or the owner. Nothing here is settled (S28): a KEEP says only that the points made in this round, read against the text, give no reason why a changed wording and not this one.*

## The ruling

**KEEP.** Line 41, the whole sentence, stands as it is:

> Survival is how the transport got there; fidelity is what it is.

**Mimo's rival is a rewording that changes nothing the theory needs from the sentence.** On this reading the sentence is easy to vary, in the plain sense of the brief (section 5: "another wording would do the sentence's work as well"), not in the text's defined sense (L317). That is recorded. The rival is not adopted because it removes no unclarity that the reading of L41 leaves, and it brings one of its own (below). No FIX, so no case verdict moves and no sentence is affected.

## What was read

- **The text under review:** `tests/99 The semantics, standing alone.md`, md5 74f4a4c7619345747f4fa976ddac9548 (checked before reading; not written to): L1–L120, L180–L257, L566–L580, L618–L632, and every line quoted below.
- **The brief:** `tests/S103 Round 1 - trying to vary the strong candidates - part 1, Parts 0 and II.md`, md5 9c46307c5dc62368327e8a34c184a83d: sections 1, 2, 5 and 6, and the C02 section (its lines 65–76).
- **The reading rule**, whole.
- **The tabulation:** `results/S103 Round 1 - reading/tabulation.md`, its opening sections, the C02 section (its lines 150–240) and the lines that name C02 in "Points that allege a defect".
- **The replies:** `s103_vary_mimo_1.response.txt` line 1 (its standing note) and lines 28–49; `s103_vary_glm_1.response.txt` lines 29–48. No reasoning file was opened. No other passage of either reply names C02 (tabulation, "Passages that name a candidate outside its own section").
- **For what depends on the sentence:** the S98 ledger, group G04, section `sec-L41-41`; the S100 data row for L41.s4; the S101 graph, searched for `L41.s4`.
- No other checker's ruling was read.

## The sentence and what the theory needs from it

It closes the answer to grievance 3 (L41):

> **3. "If correspondences are selected, you have made fidelity a matter of survival."** No. Selection produces a transport. Whether that transport is faithful on changes it was never selected against turns on the transport and the target alone, not on whether it survived. Argument 3 says that a selected transport is underdetermined by its history on an unseen change wherever its population admits a differing survivor there. Survival is how the transport got there; fidelity is what it is.

The sentences before it carry the answer. The closing sentence puts the grievance's word "survival" on the side of the transport's history and "fidelity" on the side of what the transport is, and so turns down the grievance's "a matter of survival". What the theory needs from it is that split and nothing more. The body states the split more exactly, as L35 requires of the front matter ("the front matter states nothing the body does not state more exactly"):

- **survival is history:** L193, "has exactly one of three provenances, determined by its history in the physical module"; L195, "The transport \(t\) is a member of \(\mathcal T\) that survived.";
- **fidelity is a condition on the transport and its target, on a contract:** L189, "A transport is **faithful on \(C\)** when it meets the component and global fidelity conditions of Part V."; (F1) at L236 and (F2) at L242;
- **the two held apart:** (R) at L208 makes them separate conjuncts, \(\operatorname{Faithful}_C(t:\operatorname{Org}_\ell(o)\to c)\land(\operatorname{Sel}(t)\lor\operatorname{Con}(t))\); L211, "The carrier–content relation is thus a fidelity relation with a history.";
- **survival does not fix fidelity off the history:** L572, "survival on \(H\) does not distinguish \(t\) from \(t'\) there"; L576, "A correspondence produced by selection is faithful where it was tested and, wherever its population admits an alternative, unconstrained where it was not."

The link that does run between them runs the other way: the survival condition requires fidelity on \(H\) (L195, "a survival condition requiring fidelity on \(H\)"). The sentence does not deny that link; it denies that fidelity is a matter of survival, which is the grievance.

**No sentence depends on it.** No line of file 99 points to it. The S98 ledger holds one record at L41.s4, the vocabulary record D-536 (S95: "truth (objection, l. 41)" to "fidelity"), which changed the grievance's word; the sentence's own wording has stood since file 10. The S101 graph has no node or edge citing L41.s4.

## Each side (rule 7)

### Mimo: VARIES

Mimo's rival (reply line 32):

```
Survival is how the transport got there; fidelity is what the transport is on the contract.
```

Mimo's reasons: it "Keeps the split the grievance needs (provenance against property)" and "carries the index L189 requires", since (F1), (F2) and (A) range over \((a,b)\in C\); it "Breaks nothing I can name". Mimo's variations: "Survival is fidelity on the history." breaks L195 ("fidelity on \(H\) without membership in \(\mathcal T\) is not survival"); "Fidelity is what survived." breaks L572 and L67. Mimo's fault check: "it" can be read as the transport ("forced by the parallel") or as "fidelity", "which would make the clause do no work"; read as the transport, "the clause alone invites an absolute reading of fidelity", which the sentence before it and L189 exclude. Mimo's own verdict on the fault: "Readerly risk, not a forced failure."

On the variations I read as Mimo does, with one note: "Fidelity is what survived." runs against L41's own second sentence ("not on whether it survived") and L572; L67 concerns whether anyone tentatively accepts a transport, which the variation does not bring in, so the break stands without it.

### GLM: HOLDS

GLM's reasons: its rival "Selection is how the transport got there; fidelity is what it is." "loses grip on the grievance's own word", since the grievance is "you have made fidelity a matter of **survival**", and misassigns, since selection is the whole of L195 (population, variation operator, history, survival condition) while survival is the condition the grievance names and Argument 3 isolates (L572). Its rival "Survival concerns provenance; fidelity concerns the transport." "miscasts survival" (provenance classifies transports, L193), and "concerns" is too weak to carry fidelity as a condition on the transport on its contract (L189). The fatalist reading of "is what it is" is blocked by the sentence before; the compression of "survival" for selection by survival is covered by "Selection produces a transport". "No fault stands."

On GLM's points: the closing sentence's work is to answer the grievance in its own word, and Argument 3's point is about survival on \(H\); with "Selection" the sentence would still cohere with L41's opening but would no longer set the grievance's word against fidelity. On the second rival: survival is part of the selected provenance (L195 names "a survival condition" among its parts), so "Survival concerns provenance" does not clash with L193 outright; what it loses is the contrast of how the transport came to be held against what it is, which is the sentence's work. GLM put neither wording forward as a proposal, and neither is ruled on as one.

### Between them

The readers differ on whether the rival does the sentence's work "as well". It does, as far as content goes: it keeps the split, and nothing it adds or changes is anything the theory needs that the sentence lacks (next section). Where the readers part is on the closing line, and there the question under rule 5 is whether the rival is clearer. It is not (the section after next). So Mimo's rival is recorded as a rewording, and GLM's HOLDS is not adopted as its reason for the KEEP: GLM's rivals changed the sentence's words at the points where the sentence does its work (the grievance's word; the contrast), while Mimo's leaves those points alone.

## The rival: a rewording, not a different claim

The rival differs from the sentence at two places.

- **"the transport" for "it".** The parallel with "how the transport got there" gives "it" the transport, as Mimo says ("forced by the parallel"), and GLM reads it so. This changes nothing.
- **"on the contract" added.** The sentence already carries this index. L31: "Grain, boundary, continuity and the contract of admitted changes are **declared indices**: every claim is relative to them". The next grievance says it outright, L43: "Within any contract, whether a transport is faithful at a pair turns on the transport and the target". And fidelity is defined only on a contract (L189). A front-matter sentence naming fidelity without its contract is relative to one by L31; adding the index states what L31 already imposes.

So the rival is a rewording that changes nothing the theory needs from the sentence, and on this reading the sentence is easy to vary (in the brief's plain sense). That is recorded here. Nothing is proposed about what hard to vary covers (S34).

## Why KEEP, and not the rival

Rule 5: for a rewording, FIX only if the rival is clearer. The reasons why the text's wording and not the rival's:

1. **The rival removes no unclarity that reading L41 leaves.** "It" is given the transport by the parallel; the contract by L31, L43 and L189.
2. **The rival brings an unclarity of its own.** "fidelity is what the transport is on the contract" can be read as saying that fidelity is the transport as it stands on the contract, its translations \(\pi,\tau,\sigma\) and \(\lambda\) restricted to \(C\). Fidelity is not that. It is a condition the transport meets or fails there, and the condition compares relations of both organizations, not of the transport alone: (F1) at L236, \(\operatorname{proj}^{\lambda}_{V_k}\!\big[\operatorname{Sol}_{\lambda(k)}(a,b)\big]=L_k(\tau(a),\sigma(b))\), and (F2) at L242, \(\pi[\operatorname{Sol}_D(a,b)]=\operatorname{Sol}_E(\tau(a),\sigma(b))\). That is why the sentence before says "turns on the transport and the target alone". The text's "what it is", set against "how the transport got there", reads as the contrast of what a thing is against how it came about, and does not offer itself as a definition. With "on the contract" added, the clause reads more like a definition, and read as one it leaves out the target.
3. **Item 3 names no contract.** "The contract" in the rival has no antecedent inside the item; the nearest are L31's general index and L43's "any contract", which comes after it.

**A third wording was weighed and is not proposed:** "it" alone replaced by "the transport" ("Survival is how the transport got there; fidelity is what the transport is."). The parallel already gives "it" the transport, and with the pronoun spelled out the clause reads as a flat identity of fidelity with the transport, leaving out the target, which the idiom does not invite.

## The points that allege a defect

- **Mimo: "it" read as "fidelity" makes the clause do no work.** The parallel gives "it" the transport, and Mimo says so. On the other reading nothing breaks: the first clause and L41's second sentence carry the answer. Not shown as a failure; Mimo's own words are "Readerly risk, not a forced failure."
- **Mimo: read as the transport, the clause alone invites an absolute reading of fidelity.** The clause does not stand alone: L31 makes every claim relative to the contract, the sentence before names "the transport and the target", and L43 follows with "Within any contract". Not shown.
- **GLM (sought and set aside by GLM): the colloquial fatalist reading of "is what it is".** Set aside by the sentence before, as GLM says. A further check against the owner's words: on the idiom's reading, the sentence says that the transport's fidelity does not wait on anyone's view of it; it does not say that any claim about that fidelity is settled. The brief gives S28 as: "after Claude explained that the thing explained is however it is and everything anyone accepts about it stays tentative: "1. That is correct."" Neither reading of the sentence goes past that.

## The owner's decisions

KEEP changes no wording. Checked against the sentence as it stands: S23 — no word S23 forbids, no belief, ranking or foundation idea, no "accept", no "argument"; S20 — no list, count, grade or record; S21 — nothing about what must happen to candidates; S25 to S27 — no physical possibility; S28 — above; S33 and S34 — neither reader proposes anything on C02 about what hard to vary covers (tabulation: "Parked (S34): no"), and nothing is proposed here; nothing is parked. No value is moved in or out.

## Cases

No case of the text turns on this sentence's wording, and the S98 ledger ties none to it. The worked episode of Part XVI, section 10, "A two-layer episode, in exact form" (L618–L632), uses both terms in the split the sentence states: \(t_0\) is selected on \(H_0\) and "faithful on \(H_0\)" (L622), then violated off \(H_0\) (L624), and under the selection response "no member survives the extended history: the fidelity failure is structural, not parametric" (L626). A KEEP moves no case verdict.

## Quotations compared with file 99

Every quotation of file 99 above was compared with the text and stands on the line given: L31, L35, L41 (whole), L43, L189, L193, L195 (three pieces), L208 (the formula of (R)), L211, L236, L242, L572, L576, L622 ("It is faithful on \(H_0\)."), L626; L67 as the tabulation gives it. The readers' quotations used here are those the tabulation records as found (C02 section). The owner's words are quoted from section 2 of the brief. No book is quoted.
