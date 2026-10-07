# S103 Round 1 — ruling on C22 (L311)

*Written by a fresh checker (Opus 5.5), 27 September 2026, filled as it went (this file was created first as a stub and then filled; no other file was written over). Not committed by this checker. This file obeys decision S23 except where it quotes the text, a reader or the owner.*

**Ruling: KEEP.** The sentence stands as it is at L311 of `tests/99 The semantics, standing alone.md` (md5 74f4a4c7619345747f4fa976ddac9548, checked before reading; not written to):

> (B) records the collective contribution.

This ruling settles nothing (decision S28). It records that the sentence came through both readers' attempts and this checker's own; that Mimo's rival, "(B) records the contribution of a block.", is not a rewording that changes nothing the theory needs, since it drops the one word that says the contribution is not any single commitment's, and the words "a block" do not put that back, the text counting a one-commitment set as a block; that the doubt GLM raised and set aside (two senses of "contribution") shows no defect in this sentence; and that no wording tried reads more plainly while keeping what the theory needs from it.

## How this checker came to the item

The tabulation (`results/S103 Round 1 - reading/tabulation.md`, the C22 section at its lines 2125–2230, and its notes at lines 44, 3036 and 3051) sends C22 to a checker because Mimo closes VARIES (rule 5) and the readers differ (rule 7), and records that GLM's search for a fault notes two senses of "contribution" in the text and sets that aside. Parked (S34): nothing. This file stands where the task names it, not where rule 11 of the reading rule names it (`results/S103 Round 1 - rulings/ruling C<nn> L<line>.md`); the sibling rulings stand at the task's path too.

Read for this ruling: the reading rule (`results/S103 Round 1 - how the replies will be read, written before sending.md`); decisions S20 to S35 in `records/Semantics - Decisions.md`; the part 3 brief (`tests/S103 Round 1 - trying to vary the strong candidates - part 3, Parts V to XIV.md`), its entry for C22 (lines 67–82); the tabulation's C22 section; Mimo's C22 section (`s103_vary_mimo_3.response.txt`, lines 33–66) and GLM's (`s103_vary_glm_3.response.txt`, lines 17–30), whole; a search of all six replies for "C22", "L311" and "collective", which found nothing outside those two sections; no `.reasoning.txt` file. In file 99: L25, L229–L265, L285–L317, L427, L433–L441, L520–L526, L544, L588. Every use of "contribut" and "record" in file 99, found by search. The S98 ledger (`results/S98 Ledger of edits and recommendations/line-up/data/by sentence.csv`), searched by program for rows on L309–L313 and for "collective": it holds no row for L311.s2, the sentence under review; the rows on L311.s1 (CH-0698, CH-0699, CH-0925, CH-1013, CH-1065, CH-1110) change the heading and the first sentence of the paragraph, never this one. The sentence stands word for word in the earliest text the project holds of this theory (`authority/10 … standalone theory.md`, line 328), where it closes the paragraph on the same example under an earlier heading. The case books (`tests/S81 Case book - the 52 cases, situations and fixed verdicts, as the tested agent sees them.md`, `tests/S89 Case book - candidate cases N1 to N25 drawn from the sources.md`), searched for critical blocks, infinitary routes, "collective", "contributory", "no work", redundant routes and interference. Every quotation of file 99 below was compared with it by program, each found on the line given.

## The sentence in its place

> L309| **Interference.** \(\Gamma=\{a,b\}\), \(\mathsf S=\{\{a\}\}\): the full candidate fails (E) although a subset meets it. A subset can meet (E) while the whole fails it; \(b\) is not made "not a commitment" to repair this.
>
> L311| **Infinitary routes.** \(\Gamma=\{d_n:n\in\mathbb N\}\), \(d_n\) the constraint \(|x|\le 1/n\): every set of indices unbounded in \(\mathbb N\) determines \(x=0\); no minimal route, and no route of one commitment, exists. (B) records the collective contribution.
>
> L313| **Commitments that do no work.** (E) has no condition that each commitment do work. A commitment \(d\) of a candidate that has a route does no work by itself in it when every route stays a route after \(d\) is added to it and after \(d\) is removed from it: a candidate carrying \(d\) then meets (E) exactly when it meets (E) without \(d\), and \(\{d\}\) is critical in no route (B). When \(\Gamma\) is infinite, a block of such commitments can still be critical (Infinitary routes).

What it uses:

- **(S)**, L290: "\mathsf S_{E,p}=\{W\subseteq\Gamma:\operatorname{Account}(E|W,p)\}", with L287: "the commitments of \(E|W\) are \(W\)".
- **(B)**, L293 and L296: "No upward closure and no minimal member are assumed. For nonempty \(B\subseteq W\)," and "\operatorname{CriticalBlock}(B;W,p)\iff W\in\mathsf S_{E,p}\land W\setminus B\notin\mathsf S_{E,p}."
- **block and route**, L299: "A block may be critical while no singleton in it is. Criticality is relative to the route \(W\) it is assessed in, a **route** of the candidate being a member of \(\mathsf S_{E,p}\)".
- **contributory**, L305: "then \(d\in\Gamma\) is critical for some route (**contributory**) exactly when \(d\in\bigcup\min\mathsf S\)", under the assumptions "If \(\Gamma\) is finite, \(\mathsf S\) is upward closed, and \(\Gamma\in\mathsf S\)".
- **commitments**, L231: "those the candidate offers as doing the work, whether or not anyone has described their work".

## What the sentence does

1. **It names where the example's work shows up.** The paragraph's first sentence gives the routes (the unbounded index sets) and says "no minimal route, and no route of one commitment, exists". Nothing in that sentence says the commitments do anything. This sentence says they do, and that the definition that registers it is (B): in the example, with \(W\) a route, a block \(B\subseteq W\) is critical exactly when \(W\setminus B\) is bounded; every such block is infinite, and no one-commitment block is critical, since removing one index from an unbounded set leaves it unbounded.
2. **"Collective" says whose contribution it is: the commitments' together, and no single one's.** It is the collective counterpart of L305's "contributory", which is said of one commitment ("\(d\in\Gamma\) is critical for some route"). The pair of words carries L299's "A block may be critical while no singleton in it is" into the example.
3. **It is the instance L313 points to.** L313 ends: "When \(\Gamma\) is infinite, a block of such commitments can still be critical (Infinitary routes)." "Such commitments" are commitments that do no work by themselves; in the example each \(d_n\) is one (adding it to or removing it from an unbounded set leaves the set unbounded). The only sentence of the Infinitary routes paragraph that speaks of (B), and so of a critical block, is this one, and its "collective" is what says the contribution is not a single commitment's.
4. **"Contribution", not "work", matches what (B) tests.** (B) is a deletion test: \(W\setminus B\notin\mathsf S_{E,p}\). "Contributory" (L305) is the same test for one commitment. L313's "does no work by itself" is a two-sided test ("after \(d\) is added to it and after \(d\) is removed from it"), which (B) does not record. So "contribution" names what (B) records and "work" would name more than it records.

## The readers, weighed

The number of readers on a side decides nothing; each point is weighed on its argument.

**Mimo's rival, "(B) records the contribution of a block."** (reply line 38; closing line, reply line 65). Mimo's grounds: (B) assesses blocks (L296); a block is the collection whose contribution the sentence marks (L313); "contribution" keeps the reach to Part XI (L435); and (step 3, reply line 63) "\"Collective\" blocks the individual reading L313 denies; the block word carries that in the rival."

The last ground does not hold on the text's own terms. (B) is stated "For nonempty \(B\subseteq W\)" (L293), with no lower bound on size, and L313 applies (B) to a one-commitment block: "\(\{d\}\) is critical in no route (B)". So a block may be a single commitment, and "the contribution of a block" says as much of one commitment critical by itself as of an infinite family. The rival keeps the claim that (B) registers some block's contribution; it drops the claim that the contribution here is collective, that is, of no single commitment. In the example the two agree on which blocks are critical (every critical block there is infinite, as shown above), but the original says so and the rival leaves it to be worked out, and that is the half L313's pointer uses: "a block of *such* commitments", commitments each of which does no work by itself. The rival also loses the pairing with L305's "contributory", the word for one commitment's contribution, which "collective" answers. The change from "the" to "a" is a rewording and takes nothing away.

So the rival is **not a rewording that changes nothing the theory needs**. It is a different claim, weaker than the text's. Weighed as a challenge, it shows no defect in the text's wording, and taking it would thin the one statement in the paragraph that L313's closing sentence leans on. Not taken.

Mimo's variations that break, each weighed:

- "(S) records the collective contribution." (reply line 46). The point holds: (S) at L290 is the set of routes; it registers no criticality, so L313's "\(\{d\}\) is critical in no route (B)" and its "(Infinitary routes)" would point at an example whose recorded fact is about routes, not blocks.
- "(B) records each commitment's contribution." (reply line 52). The point holds: in the example no commitment is critical by itself (removing one index leaves an unbounded set unbounded), so the sentence would misstate the example and would contradict L313's closing sentence, which it exists to instance. Mimo's citation of L311's "no route of one commitment" for this break is not quite on target (that clause is about routes of one commitment, not about critical ones); the break stands on the deletion argument.
- "Each commitment is contributory." (reply line 58). The point holds, and more strongly than Mimo puts it: by the definition in L305 ("critical for some route"), no \(d_n\) is contributory in the example, so the sentence would misstate the example, whether or not L305's finite monotone assumptions are met.

Mimo's claim that "contribution" "keeps the reach to Part XI, L435" is weighed with GLM's below; it is not a tie the sentence needs.

**GLM's HOLDS** (closing line, reply line 29). GLM's grounds:

- "(B) records that the work can be collective." (reply line 23) — GLM: "\"work\" severs both links", the links being to L305 and to Part XI. The rejection holds, on a ground stronger than the one GLM gives: "work" is L313's two-sided test (added and removed), which (B) does not record; "contribution" names the deletion test (B) and "contributory" share (point 4 above). The softer "can be collective" would also say less than the example shows: here the contribution *is* collective, and only collective.
- "Only blocks are critical here; (B) says so." (reply line 24) — GLM: "true but loses the named definition and the term \"contribution\" again". The point holds in part. The wording keeps (B); what it loses is "contribution" and with it the pairing with "contributory" (L305). "Only blocks are critical" also needs the reading that a block has more than one commitment, which, as above, the text's (B) does not give. GLM's further remark that "here" points at the example "whereas the original states the general role of (B)" does not hold: the original too is said of the example, as its place in the paragraph shows. The first ground is enough.
- "(B) defines the collective contribution." (reply line 25) — GLM: "a definition defines criticality of blocks (L296); it does not define a contribution." The point holds: (B) defines CriticalBlock; the collective contribution is a fact about the example that (B) registers, and "records" is the text's verb for registering what is there, as in L159 ("the semantics records the restriction and supplies no rule that decides it") and L522 ("stated inputs that the semantics records and does not supply").

**The doubt GLM set aside: two senses of "contribution".** GLM (reply line 27): "\"Contribution\" is used in two senses in the text (L305's per-commitment sense, L435's subhistory sense); L307 explicitly separates route-criticality from ProducedBy attribution, so the sentence does not trespass on Part XI. No conflict found."

The doubt is real as a matter of the word across the text, and shows no defect in this sentence:

- Part XI defines one use: "**Repair.** The contribution \(\Delta\) of a repair is a subhistory together with the changes of content it makes." (L435); L441 attributes "the repair to each contribution whose active route ran to it in the history".
- L307, four lines before the sentence, uses the Part XI sense and keeps it apart from what a candidate contains: ProducedBy "attributes a repair to the contributions whose active routes ran to it, not to the routes a candidate contains."
- Elsewhere the word is ordinary: "an outside contribution", "Contribution of content and ownership of a process are different attributions" (L427); "a weighting of attribution among several contributions to one achievement" (L522); "the originative contribution of an episode" (L544). Part VI's own form is "contributory" (L305).

The sentence fixes its sense itself: it is the contribution that (B), a deletion test on commitments of one candidate, records. Read in the Part XI sense (a subhistory with its changes of content), it would say that a definition on subsets of \(\Gamma\) records a subhistory, which no reader can hold together with L296; and L307 has just said that the routes a candidate contains are not what Part XI attributes to. So there is no reading on which the sentence misstates the example or trespasses on Part XI. It follows that the tie both readers draw from "contribution" to L435 is not one the sentence carries or needs: the word it pairs with is L305's "contributory", and that tie is enough for GLM's HOLDS. The use of one word in two places, with each sense fixed where it stands, is a matter of the term across Parts VI and XI, not of C22; this ruling proposes nothing for L305, L307, L435 or L441.

## This checker's own attempts

- `(B) records their collective contribution.` A rewording; "their" must reach back past "no route of one commitment" and "indices" to the \(d_n\), so it is less plain, not more. Recorded, not taken.
- `(B) records the collective work.` A different claim: "work" is L313's two-sided test, and (B) records only the deletion side (point 4). Not taken.
- `CriticalBlock records the collective contribution.` A rewording; the text refers to its displays by tag, as L313 does ("critical in no route (B)") and L526 does ("(S), (B), (D) depend on (E)"). Not clearer. Recorded, not taken.
- `(B) records the contribution they make together, which none makes alone.` A different, longer claim: it states outright that no single commitment is critical, which "collective" already says and which the deletion argument shows. It says nothing the theory needs that the text's wording does not, and it is not the smallest change; no challenge calls for it. Not taken.
- `Every block whose removal leaves a bounded set is critical (B).` A different claim, more specific: it gives the critical blocks of the example and drops "contribution" and the pairing with "contributory". Not taken.

Every wording that changes what the sentence claims either says less of what L313 uses (Mimo's rival, "Only blocks are critical here"), misnames the definition ("(S) records", "defines"), misnames what (B) tests ("work"), or misstates the example ("each commitment's contribution", "Each commitment is contributory"). The rewordings that change nothing it needs ("their", "CriticalBlock", "the"→"a" alone) are not clearer. So, on this reading, the sentence is not easy to vary; the rewordings are recorded.

## Faults sought in the sentence itself

- **Whether it holds of the example.** With \(W\) a route and \(B\subseteq W\) holding all but finitely many of \(W\)'s indices, \(W\setminus B\) is bounded and is not a route (a bounded set leaves an interval of values of \(x\), so it does not determine \(x=0\)), and \(W\) is; so CriticalBlock\((B;W,p)\) holds. No one-commitment block is critical. What the sentence says holds of the example.
- **Circularity.** None: the sentence applies (B) to the example; (B) is defined without it (L293–L296).
- **Vacuity.** In any example where the empty set is not a route, a whole route \(W\) is a critical block of itself, so "(B) records a contribution" alone would say little. The word "collective" is what makes the sentence say something about this example: here only blocks of many commitments are critical. That is the work point 2 above gives it, and it is why Mimo's rival, which drops it, says less.
- **A part that does no work.** Each word does work: "(B)" names the deletion test; "records" says (B) registers a fact of the example and does not define it; "collective" says the contribution is no single commitment's; "contribution" pairs it with "contributory" (L305). The definite article refers to the family's contribution just shown.
- **The first sentence of the paragraph.** "No route of one commitment" (L311) is about routes, not about critical commitments; the text does not say in words that each \(d_n\) does no work by itself, which L313's "such commitments" needs. That is a matter of L311's first sentence, which is not before this checker, and the reader can work it out in one step (removing or adding one index leaves an unbounded set unbounded). It shows no defect in C22, whose "collective" is the only word in the paragraph that says it. Recorded for the orchestrator; nothing proposed.

## The owner's decisions

- **S20.** No list, count, grade or record of rivals does any work here. The verb "records" says what a definition registers about one candidate's commitments; it is not the record of rescues S20 calls redundant ("A record is redundant."), and it keeps no list of anything.
- **S21.** The sentence says nothing about what must happen to any candidate, nor about the person choosing.
- **S23.** No word or idea S23 removes: nothing of belief, verification, authority, foundation or ranking; "records" registers a relation that holds of the example, not a finding that settles it.
- **S25–S27.** The example is mathematical (constraints on \(x\)); the sentence puts no condition of physical possibility on an account, a question or a conflict.
- **S28.** KEEP settles nothing; this ruling records only that the attempts made broke what each is said above to break.
- **S33–S34 (parked).** No point of either reader proposes anything about what hard to vary covers, and this ruling proposes nothing about it. "Easy to vary" above is meant plainly, as the brief asks, not as the text's term at L317. No value is moved in or out.

## Fixed case verdicts

- **The worked cases of Part VI** (L305–L313): Redundant routes ("each is contributory, neither indispensable", L307), Interference ("the full candidate fails (E) although a subset meets it", L309), Infinitary routes (L311) and Commitments that do no work (L313) all stand; with KEEP nothing changes. The verdict that ties to this sentence, "When \(\Gamma\) is infinite, a block of such commitments can still be critical (Infinitary routes)" (L313), keeps its instance.
- **Case book O19** ("The diagram in his hand"; fixed verdict "The diagram was in his hand and did no work; the lock did it.") turns on what ran in a history (active routes, Parts IX and XI), not on a candidate's critical blocks. Nothing moves.
- **S89 case book, N1** (Tomas; "the sun-god sentence is no part of it", "no, it does no work") turns on an idle commitment, the first part of L313, in a finite candidate. Nothing moves.
- **The S98 ledger** has no row for L311.s2 and ties no case to it.

## What depends on the sentence (nothing changes under KEEP)

- L313: "When \(\Gamma\) is infinite, a block of such commitments can still be critical (Infinitary routes)." Its pointer lands on this sentence's claim.
- L299: "A block may be critical while no singleton in it is." The Infinitary routes paragraph, through this sentence, is the text's case of it.
- L305: "(**contributory**)", the one-commitment counterpart that "collective" answers.
- L526: "(S), (B), (D) depend on (E)." The dependence order is untouched: the sentence applies (B) and defines nothing.

## Result

- **Ruling:** KEEP.
- **old = new** (L311): `(B) records the collective contribution.`
- **Mimo's VARIES:** the rival "(B) records the contribution of a block." is a different, weaker claim, not a mere rewording: it drops "collective", the one word in the paragraph saying the contribution is no single commitment's, which L313's "a block of such commitments" uses and which answers L305's "contributory"; "a block" does not put it back, since the text's (B) takes any nonempty block and L313 applies it to \(\{d\}\). Weighed as a challenge, it shows no defect. Not taken.
- **GLM's HOLDS:** holds, on the tie to L305 and on the verb; its rejection of "work" holds on a stronger ground (work is L313's two-sided test; (B) records only deletion). The doubt it set aside, "contribution" in Part VI and Part XI (L307, L435, L441), is a matter of the term across Parts, with each sense fixed where it stands; no defect in C22. The tie both readers draw to L435 is not one the sentence carries or needs.
- **Easy to vary?** Not on this reading: the rewordings that change nothing it needs ("their", "CriticalBlock", "a" for "the") are recorded and are not clearer; every wording that changes the claim breaks a line named above.
- **Recorded for the orchestrator, nothing proposed:** L311's first sentence does not say in words that each \(d_n\) does no work by itself, which L313's "such commitments" needs; one step shows it.
- **Parked (S34):** nothing.
- **Recorded:** held under both readers' attempts and this checker's; not thereby final.
