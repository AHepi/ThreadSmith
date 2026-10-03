# S103 Round 1 — ruling on C29 (L520)

*Written by a fresh checker (Opus 5.5), 27 September 2026, filled as it goes. Not committed. This file obeys decision S23 except where it quotes the text, a reader or the owner.*

**Ruling: FIX.** The sentence changes; nothing else in the text does.

- **Old (L520, seventh sentence of the line):** `Account, from fidelity under change (E).`
- **New:** `Account, from fidelity under change, non-circular dependence and non-vacuity (E).`
- **Easy to vary on this reading:** neither reader closed VARIES. The one rewording offered of the present gloss, Mimo's `Account, from fidelity across the contract's changes (E)` (reply line 261), changes nothing the present sentence says (it rewords "under change"), so on that phrase alone the sentence is easy to vary in the plain sense; it is not clearer, and it keeps the same omission, so it is not taken. The FIX is not a rewording: it is a different, fuller claim about what Account is defined from, weighed here as Mimo's challenge (FAILS) against GLM's HOLDS.

This ruling settles nothing (decision S28).

## What was read

- The text under review, `tests/99 The semantics, standing alone.md` (md5 74f4a4c7619345747f4fa976ddac9548, checked before reading; not written to): L13–L25, L41–L61, L111–L121, L180–L280 (Part IV's transports and representation, Part V whole), L505–L540 (Part XIV whole, the head of Part XV), L590–L600 (Argument 6), and every line holding "fidelity" (L17, L23, L37, L41, L43, L49, L189, L195, L211, L220, L233, L245, L247, L277, L407, L520, L626, L630).
- The reading rule, `results/S103 Round 1 - how the replies will be read, written before sending.md`.
- The part 3 brief (md5 44ef4fbdb179963c3e76fcdaf60ecf27): its C29 entry (lines 197–207).
- The tabulation, `results/S103 Round 1 - reading/tabulation.md`: C29's section (lines 2900–3008) and the notes naming C29 (lines 34, 3042, 3052).
- The replies: `s103_vary_mimo_3.response.txt` lines 253–281 and `s103_vary_glm_3.response.txt` lines 125–140, whole. All six replies were searched for "C29", "L520" and "fidelity under change"; no other passage names this item. No reasoning file was opened.
- The owner's decisions S20–S35 in `records/Semantics - Decisions.md`.
- For ties to cases: the S98 ledger, group 14, entry L520.s7, and `line-up/data/by sentence.csv`; the case books `tests/S81 Case book - the 52 cases, situations and fixed verdicts, as the tested agent sees them.md` and `tests/S89 Case book - candidate cases N1 to N25 drawn from the sources.md`; `results/S96 Check of the repaired copy - cases.md`; `results/S95 Scrub - cases re-read on the scrubbed text.md`.
- For consistency with neighbouring rulings: the head of `ruling C21.md` and `ruling C18.md` (which rules on what the bare word "fidelity" names at L220).

## The sentence and what it uses

L520 (whole line):

> Everything else is defined in terms of the two imports, the structural vocabulary of (O) and (Q), the declared indices and the declared inputs (below). Roles, from admitted edits (Part II). Kinds, from signatures (K). The respect of a question, from its query (Part III). Representation, from fidelity and provenance (R). Provenance, from physical history (Parts IV, XII). Account, from fidelity under change (E). Understanding, construction, newness, origin, repair, created explanation, capability, recursion, universality, from those.

The definition the tag points to, L262:

> \operatorname{Account}(\mathcal E)\iff \text{(F1)}\land\text{(F2)}\land\text{(A)}\land\text{NonCircular}\land\text{NonVacuous}. \tag{E}

with L265: "Every conjunct is a condition on how supplied relations behave under the changes in \(C\). None inspects a label."

What the text calls fidelity:

- L189: "A transport is **faithful on \(C\)** when it meets the component and global fidelity conditions of Part V."
- L245, of (F1) and (F2): "Together they are fidelity at every level the contract reaches."
- L247: "**Question fidelity.** For every \((a,b)\in C\)," heading (A).
- L630: "so far as (F1), (F2) and (A) reach, the two candidates are one account (Argument 2)."

What the text counts as the conditions of Account:

- L231: "meets \(\operatorname{Account}(\mathcal E)\) exactly when the following four conditions are met, each a condition on supplied relations under the changes in \(C\)."
- L61: "(Suff) sufficiency of the four conditions of Account; (Nec) their necessity".
- L536: "A candidate meeting all four conditions of (E) on a contract of its question".
- The two conditions that are not fidelity have their own headings: L255 "**Non-circular dependence.** The answer follows by evaluating \(E\) under its independent boundary conditions." and L257 "**Non-vacuity.** \(\operatorname{Sol}_D(1,b_0)\neq\varnothing\)."

## The two sides (rule 7)

### Mimo: FAILS

Closing line (reply line 279): "C29: FAILS — the gloss names only the fidelity conjuncts, though (E) also requires non-circular dependence and non-vacuity (L262; L255; L257) — Account, from fidelity under change, non-circular dependence and non-vacuity (E)."

The argument: the list names the sources of each defined notion, as the item for (R) names both conjuncts of L208 ("from fidelity and provenance"); (E) has five conjuncts (L262); "fidelity" names only (F1), (F2) and (A) (L245); non-circular dependence (L255) and non-vacuity (L257) are not fidelity; so the gloss names one group of three and omits two. Mimo also shows that `Account, from (E).` drops the description every other item carries, and that `Account, from fidelity under change (F1), (F2), (A).` breaks L526, where the item must name (E).

### GLM: HOLDS

Closing line (reply line 138): "C29: HOLDS — the bare tag lost L265's characterization, enumeration broke the list's pattern and L265, \"the contract's edits\" under-described L255, and \"variation\" touched the parked question of S34."

The argument: "under change" summarizes L265 and is the theory's signature idea; `Account, from (F1), (F2), (A), non-circular dependence and non-vacuity.` is "a list, not a gloss", "suggests the conjuncts are independent sources, against L265's single characterization", and breaks the neighbouring entries, "each of which names a source by sense, not by enumeration"; "the contract's edits" under-describes (E), since non-circular dependence speaks of deletions of components (L255); "variation" is a loaded word (S20) and touches the question S34 parks; "fidelity" in two entries is not equivocation; the entry is consistent with Argument 6 (L596) and L526.

## Ruling between them

**The failure is shown.** Three things decide it.

1. **What the word names in this text.** Every line that defines or counts fidelity gives it (F1) and (F2) (L189, L245), with (A) as "Question fidelity" (L247) and the three together at L630. No line calls non-circular dependence or non-vacuity fidelity. They are not conditions on a correspondence between \(D\) and \(E\) at all: non-circular dependence is a condition on \(E\) and \(\Gamma\), a contrast lost when a block \(G\subseteq\Gamma\) is deleted (L255); non-vacuity is a condition on the target's baseline and on how \(C\) is stated (L257). Whichever of the two readings of the bare word the C18 ruling records (with or without (A)), these two conditions fall outside it.

2. **What the list's items say.** Each item names what its tagged definition is made from. "Kinds, from signatures (K)" names the content of (K) (L113–L116). "Representation, from fidelity and provenance (R)" names both conjuncts of L208, joined by "and". Read on that pattern, "Account, from fidelity under change (E)" says that account is made from fidelity under change. The tag is exact, so the list still points to the right definition; but the words beside it name three of five conjuncts as though they were all of them. The two it leaves out are the ones Part V uses to keep an account apart from a faithful restatement: L273, "\"\(p\) because \(p\)\" fails non-circular dependence. So does an account whose only substantive component restates the answer it was asked for"; L536, "conclusion-as-premise fails non-circular dependence". The text's own summary of what to attack counts "the four conditions of Account" (L61), not fidelity. So the gloss, on the pattern of its own list, says less than (E) (L262) in a way that misstates what Account is.

3. **GLM's defence does not reach this.** GLM reads "fidelity under change" as the whole of L265. But L265 says of every conjunct that it "is a condition on how supplied relations behave under the changes in \(C\)"; it does not say every conjunct is fidelity. What L265 shares with the gloss is "under change", not "fidelity". GLM's own third point (that "change" must cover the deletions of L255) shows what its reading needs: that "fidelity" stretch over a condition about deleting components of \(E\), which the text never calls fidelity. GLM's argument against enumerating was made against a different wording (bare tags, no word of sense, no (E)); it does not touch a wording that names the conditions by sense, with the text's own headings, as the item for (R) names two. And naming the conditions does not deny what L265 says they share: L265 speaks of "Every conjunct", and L231, L61 and L536 count four conditions. GLM's points on "the contract's edits" and "variation" concern wordings the FIX does not use. GLM's point that "fidelity" in two entries is not equivocation is agreed; the FIX keeps the word in both, in the sense of L189, L245 and L247.

GLM is right that the bare tag, `Account, from (E).`, loses the characterization, and Mimo agrees (reply line 269); the FIX keeps "fidelity under change" whole, so the phrase GLM defends, the one L23 also uses ("Fidelity is over **component structure under change**, not over outputs"), stays.

## Why this wording, and not the text's, nor others

- **Not the text's:** point 2 above.
- **The FIX is Mimo's repair, word for word** (reply lines 258 and 279). It is the smallest change that meets what holds: it keeps every word of the sentence, adds the two conditions by the names the text gives them (L255's heading; L43's "non-vacuity", L273's and L536's "non-circular dependence"), and joins the three as the item for (R) joins two. "Under change" stays attached to fidelity, where the text puts it ((F1) holds for "every \((a,b)\in C\)", L233; (A) opens "For every \((a,b)\in C\)", L247); L265 still says, in its own place, what all the conjuncts share.
- **Not** `Account, from fidelity, non-circular dependence and non-vacuity under change (E).`: it would make "under change" govern all three, as L265 does, but the phrase then reads as qualifying non-vacuity alone or all three, and non-vacuity's first clause is at the identity edit (L257, "\(\operatorname{Sol}_D(1,b_0)\neq\varnothing\)"); less clear than the FIX.
- **Not** `Account, from fidelity under change and non-circular dependence (E).`: it leaves non-vacuity out, which L231, L61 and L536 count among the four conditions; the same fault, smaller.
- **Not** `Account, from the four conditions of Part V (E).`: it drops the characterization both readers agree the items carry.
- **Not** Mimo's `Account, from fidelity across the contract's changes (E)`, nor GLM's variants (reply lines 131–134): the first keeps the omission; GLM's four each break what GLM says they break, or (the enumeration by tags) drop the sense words and the tag.

## Checks

- **The dependence order, L526:** "(F1), (F2), (A) depend on (O), (Q), (K). (E) depends on those." The two conditions the FIX names are not nodes of the order; they are stated inside (E), as signatures are stated inside (K), which the list likewise names ("Kinds, from signatures (K)") though L526 gives (K) only "(O) and a contract". They are stated in the vocabulary the lead of L520 already names: components and their deletion (L255: "a deleted component imposes the full relation on its ports, Part II"), \(\operatorname{Sol}_D\), boundary conditions, and "a stated scope" (L257), the scope of a contract being a declared input (L522). Nothing in L526 changes or conflicts.
- **Argument 6, L596–L598:** it rests on the dependence order of Part XIV (L598: "By the dependence order of Part XIV"), which is unchanged; its claim (L596) is unaffected.
- **The last item of L520,** "Understanding, construction, newness, origin, repair, created explanation, capability, recursion, universality, from those.": Account is still among "those"; unchanged.
- **Cases.** The S98 ledger holds one record on L520.s7, D-663, a superseded vocabulary recommendation on the lead sentence of L520; no case is tied to this sentence. No case in the S81 or S89 case books, nor in the S95 and S96 case re-reads, cites L520 or "fidelity under change". Every case verdict that turns on Account turns on (E) at L262 and on Part V's conditions, which the FIX leaves as they are; the FIX changes a gloss beside a tag, not a definition. No fixed verdict moves.
- **Quotations.** Every quotation of file 99 above was compared with it and stands on the line given. The readers' quotations were checked by the tabulation (all found).

## The owner's decisions

- **S20:** the FIX names the conditions of one definition, which is the explanation's own content; it adds no list, count, grade or record of rivals.
- **S21:** it says nothing about what must happen; the choice stays the person's.
- **S23:** no word or idea the scrub forbids; the words added are the text's own names for two of its conditions (L255, L257, L43, L273, L536), and "from" is the word every item of the list already uses.
- **S25–S27:** no physical possibility is introduced.
- **S28:** nothing is settled by this ruling.
- **S33–S34:** nothing here is a proposal about what hard to vary covers. GLM names S34 only to set aside the word "variation"; the FIX does not use it. Nothing is parked. No value is moved in or out.

## Dependents

No sentence of the text quotes or relies on the wording of this gloss. The FIX changes no definition, so nothing that depends on (E), L520 or L526 changes reading.
