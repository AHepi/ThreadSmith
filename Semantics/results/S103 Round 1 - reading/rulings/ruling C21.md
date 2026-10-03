# S103 Round 1 — ruling on C21 (L273)

*Written by a fresh checker (Opus 5.5), 27 September 2026, filled as it goes. Not committed. This file obeys decision S23 except where it quotes the text, a reader or the owner.*

**Ruling: KEEP.** The sentence stands as it is.

- **Old (L273, first sentence of the line):** `"\(p\) because \(p\)" fails non-circular dependence.`
- **New:** `"\(p\) because \(p\)" fails non-circular dependence.` (unchanged)
- **Easy to vary on this reading (rule 5):** yes, in the plain sense the brief asks about, and recorded as such. Mimo's rival, `Conclusion-as-premise fails non-circular dependence.`, is a rewording that changes nothing the theory needs from the sentence: it names the same case by the name L536 gives it, assigns it to the same conjunct, and leaves every sentence that leans on L273's first sentence reading as before. It is not clearer than the text's wording (reasons below), so the ruling is KEEP, not FIX.

## What was read

- The text under review, `tests/99 The semantics, standing alone.md`, md5 74f4a4c7619345747f4fa976ddac9548 (checked before reading; not written to): L135–L161 (Part III, what a question \(p\) is), L215–L225, L229–L283 (Part V whole), L315–L317, L331, L343, L369, L377, L395–L399, L530–L540.
- The reading rule, `results/S103 Round 1 - how the replies will be read, written before sending.md`, whole.
- The part 3 brief (md5 44ef4fbdb179963c3e76fcdaf60ecf27): sections 1 and 2, the C21 entry of section 3, and sections 5 and 6.
- The tabulation, `results/S103 Round 1 - reading/tabulation.md`: C21's section (lines 2018–2124) and the notes that name C21 (lines 32 and 3051).
- The replies: `s103_vary_mimo_3.response.txt` lines 1–32 (C21) and `s103_vary_glm_3.response.txt` lines 1–16 (its heading and C21). All six replies were searched for "C21", "L273" and the formula; the only other hit is GLM's C24 section (line 56), which cites L273 only for the text's use of "fails". No reasoning file was opened.
- The owner's decisions S20–S35 in `records/Semantics - Decisions.md` (md5 71459192867b1ebcf1bae914c9297129).
- For ties to cases: the S98 ledger (`results/S98 Ledger of edits and recommendations/line-up/`), group 05, entry L273.s1, and `data/by sentence.csv`; `results/S96 Check of the repaired copy - cases.md`, the cases there that cite l. 273 or the formula (O2, O16, N8 (O59)).

## The sentence and where it stands

L273 (whole line):

> "\(p\) because \(p\)" fails non-circular dependence. So does an account whose only substantive component restates the answer it was asked for; packaging a dependence that answers a different question beside it does not repair this.

It is the third of three classic attempts that the section headed "What (E) excludes, and what it does not" (L267) assigns each to a conjunct of (E):

- L269: "A **table of observed answers** has no component whose relation is replaced by an intervention; it fails (F1) under any contract containing one."
- L271: "A **reversed calculation**, identification presented as production, fails (F2) under the production contract"
- L273: the sentence.

The conjunct is defined at L255: "**Non-circular dependence.** The answer follows by evaluating \(E\) under its independent boundary conditions. The target's answer does not appear, at the declared grain, as an unanalysed boundary input or as a component; moving an assertion from an input slot into a component named "law" does not discharge this. Identity of that assertion with the target's answer is structural at the declared grain, not the indiscriminate identification of all logically equivalent mathematical statements." It is the conjunct "NonCircular" of (E), whose display line is L262: `\operatorname{Account}(\mathcal E)\iff \text{(F1)}\land\text{(F2)}\land\text{(A)}\land\text{NonCircular}\land\text{NonVacuous}. \tag{E}`.

What the sentence does: it displays the classic circular shape by its form and says which conjunct of (E) that shape fails. The recap at L536 leans on it: "Part V says which of the four each classic attempt fails: a table of observed answers fails (F1); a reversed calculation fails (F2) under the production contract; conclusion-as-premise fails non-circular dependence." The next sentence on L273 extends it ("So does an account whose only substantive component restates the answer it was asked for"). L397 uses the same formula for an argument, as one against a claim, whose conclusion is among its premises.

## Each side's argument (rule 7)

**Mimo (VARIES).** The sentence's work is "the classification of the classic circular shape by the named conjunct, so that the recap can point back" (reply line 9). The rival `Conclusion-as-premise fails non-circular dependence.` "names the case exactly as that recap names it, and names the same conjunct"; L273's next sentence "still extends from it"; and "The instance string keeps its own anchor at L397" (line 9). Mimo's step 3 finds no contradiction and no vacuity (line 29).

**GLM (HOLDS).** The sentence's work: "give the canonical circular case, name the conjunct of (E) it fails, and stand as the account-level twin of the argument-level rule in Part IX" (reply line 5). Against a rival that drops the formula: "The identical formula in L273 and L397 is what makes the parallel between Part V's structural reading of identity and Part IX's structural reading of a premise-that-is-the-denial visible. Dropping the formula from L273 breaks that tie." (line 10). Its fault search: "\(p\) because \(p\)" fails the part of L255 that reads "The target's answer does not appear… as a component", "so "fails non-circular dependence" is correct as stated" (line 13).

**Where they differ, and the ruling between them.** They differ on one thing: whether dropping the formula from L273 breaks the tie with L397. It does not break any sentence, and here Mimo's reading is the one the text gives. L397's formula stands in its own sentence, introduced by "as in", as its own example: "Such an argument, as one against that claim, has its conclusion among its premises, as in "\(p\) because \(p\)", and does not rule that claim out for anyone." L397's pointer to Part V is not the formula but the words "read structurally as non-circular dependence reads identity (Part V) and not by logical equivalence alone", which point to L255's sentence on identity. So every sentence of L397 reads and holds as before under Mimo's rival. What GLM names is a real loss, but of a visible echo between Part V and Part IX, not of anything a sentence depends on; it is weighed below as a matter of clarity, not as a break.

On the rest they agree: the sentence is not at fault, and the variations that change which conjunct is named, or the reading of identity, or the verb, break something. GLM's "first part" is a loose label (the words it quotes are L255's second sentence, the first of its exclusions); its point holds.

## Is the rival a rewording or a different claim?

A rewording that changes nothing the theory needs. Checked point by point:

- **The case.** "\(p\) because \(p\)" displays a candidate that offers the answer as its own ground; "conclusion-as-premise" names that shape. L536 treats them as one case: it says that Part V says what conclusion-as-premise fails, and the only place Part V says it is L273. If "conclusion-as-premise" is read more widely, as the answer standing among other grounds, the wider case fails non-circular dependence too, by L255 ("The target's answer does not appear, at the declared grain, as an unanalysed boundary input or as a component"), and L273's next sentence already covers the answer with other things packaged beside it ("packaging a dependence that answers a different question beside it does not repair this"). So the wider reading adds no claim the text does not already make.
- **The conjunct.** Both wordings name non-circular dependence, the conjunct L536 requires Part V to name ("which of the four each classic attempt fails").
- **The reading of identity.** Neither wording says "logically equivalent"; both leave the reading of identity to L255 ("structural at the declared grain").
- **Dependents.** L273's next sentence ("So does …") reads the same after either; L536 reads the same, and under the rival its name for the case would stand word for word in Part V; L397 reads and holds the same (above); no case moves under either (below).
- **The owner's words.** Neither wording has a word or idea S23 forbids, says what must happen (S21), lists or counts rivals (S20), or brings in physical possibility (S25–S27).

So the rival does not make a different claim, and it is not weighed as a challenge. The sentence is easy to vary on this reading, and that is recorded.

## Is the rival clearer?

No. For the rival:

1. It gives the case at L273 the name L536 gives it, so a reader of L536 who looks in Part V for "conclusion-as-premise" finds those words.
2. It would give the third attempt a name, as L269 and L271 give the first two theirs ("A **table of observed answers**", "A **reversed calculation**").

Against its being clearer:

1. The match L536 asks the reader to make is made at once with the present wording: in "\(p\) because \(p\)" the ground given is the conclusion itself, so "conclusion-as-premise" is a description of the formula. No reader showed a reader of L536 failing to find the case in Part V.
2. At L273 the reader has not yet met L536. The formula shows the shape in four symbols; the hyphenated name must be unpacked into that shape before it can be set against L255.
3. "Premise" and "conclusion" are the vocabulary of arguments, defined in Part IX: L397, "An argument is an argument tree: argument steps whose leaves are premises, which are record leaves or stated assumptions and definitions." Non-circular dependence is a condition on an explanatory candidate (L231: "an organization \(E\), a transport \(t=(\pi,\tau,\sigma,\lambda)\) from \(D\) to \(E\), and an identified set \(\Gamma\) of active commitments in \(E\)"), which has components, boundary inputs and an answer, and L255 is written in those terms. "Because" is the connective of an offered explanation and needs no term from Part IX. The rival would put Part IX's words into Part V before they are defined, for a thing that is not an argument. That breaks nothing, since L536 already uses the name loosely in a recap, but it is not a gain in clarity where the condition is stated.
4. The formula keeps the visible echo with L397 ("as in "\(p\) because \(p\)""), where the same shape is ruled on as an argument; the rival would lose it (GLM's point, weighed here as clarity).

Weighed together, the rival trades one echo (with L536) for another (with L397), and a displayed form for a name in another Part's vocabulary. It is not clearer. KEEP.

A third wording was considered and is not taken: `Conclusion-as-premise, "\(p\) because \(p\)", fails non-circular dependence.` It would keep both echoes. It is not taken because its only gain over the text is the word match with L536, which the reader already makes (point 1), while it still brings Part IX's vocabulary into Part V (point 3). What holds in Mimo's challenge is that the rival works as well, not that the text falls short; the smallest change that meets that is none. Whether a named form, for symmetry with L269 and L271, is wanted is for the person choosing (S21).

## The variations that change the claim, and what each breaks

Each is weighed on its own argument; none is a repair of a fault in the sentence, and none is taken.

- `"\(p\) because \(p\)" is not an account.` (Mimo, reply line 14). It names no conjunct, so Part V would no longer say which condition the case fails, and L536's "Part V says which of the four each classic attempt fails: … conclusion-as-premise fails non-circular dependence" would no longer hold of Part V. L275 names non-circular dependence for another case, not this one. The break is real.
- `"\(p\) because \(p\)" fails (E).` (Mimo, line 18). The same break: (E) is the conjunction at L262, and "fails (E)" does not say which conjunct. Real.
- `An account whose premise is logically equivalent to its answer fails non-circular dependence.` (Mimo, line 24). It breaks L255 ("not the indiscriminate identification of all logically equivalent mathematical statements") and L397's "read structurally as non-circular dependence reads identity (Part V) and not by logical equivalence alone". Real.
- `"\(p\) because \(p\)" violates non-circular dependence.` (GLM, line 9). Besides splitting the text's verb "fails" (L269 "it fails (F1)", L271 "fails (F2)", L275 "and fails non-circular dependence", L536), "violation" is a defined term of Part IV: L220, "a **violation** occurs when fidelity fails at \((a,b)\);", for a pair "actually occurring" (L217). "Violates" here would invite that sense, which concerns fidelity at an occurring pair, not non-circular dependence. The break is real.
- `An explanation whose premise is its own conclusion fails non-circular dependence.` (GLM, line 10). It calls "an explanation" a candidate that fails a conjunct of (E), while L536 keeps "the claim that it is an explanation" as what an argument not using (E) might rule out; and it brings in Part IX's "premise" and "conclusion" (point 3 above) and drops the formula (the echo loss, weighed above as clarity). The first is a real break; the others are losses, not breaks.
- `"The answer because the answer" fails non-circular dependence.` (GLM, line 11). "The answer" is ambiguous in Part V between the target's answer, \(\operatorname{Ans}_p\), and the candidate's, \(\operatorname{Ans}_E\) (L250), and L255 excludes the target's; and the echo with L397 is lost. A real cost.

What the variations show between them: every change tried to the claim (which conjunct, which reading of identity, which verb, what the case is called as a kind of thing) meets a named line of the text; the one change that meets none, Mimo's rival, changes how the case is named and not what is claimed of it.

## Failures of the sentence itself

None found. Sought:

- **Which clause of L255 the case fails.** Read as a candidate, "\(p\) because \(p\)" has the answer as its only ground, whether in a component or as an unanalysed boundary input; L255 excludes both ("does not appear, at the declared grain, as an unanalysed boundary input or as a component"), so the sentence need not say which slot. The case fails that clause whatever the contrast clause of L255 gives.
- **The letter \(p\).** In the text \(p\) names a question (L135, "A question is", followed by the display at L138, `p=(D,\ C,\ b_0,\ \mathcal Q,\ O_p,\ \rho_p).`; L231, "An explanatory candidate for question \(p\)"), while in the quoted formula it stands for what is claimed, as at L397. Read with \(p\) as the question, the formula offers the question's answer as its own ground, which is what L255 excludes; read as the familiar formula, it offers a claim as its own ground. Both readings give the same conjunct, and the quotation marks mark the formula as mentioned. No misreading follows. A change of letter would have to be made at L397 too to keep the echo; no reader asked for one, and none is made.
- **Is the formula a candidate?** L231 defines a candidate as an organization, a transport and a set of commitments; the formula is a shape of candidate, as "table of observed answers" (L269) and "reversed calculation" (L271) are, and L273's next sentence gives its reading as an organization ("an account whose only substantive component restates the answer it was asked for"). Not a fault.
- **Vacuity, a part doing no work.** Each part works: the formula shows the case; "fails" is the text's verb for not meeting a condition; "non-circular dependence" names the conjunct L536 requires. Dropping any one loses what the variations above lose.
- **Only this shape excluded?** Mimo's step 3 raises that a reader might take the shown shape to be the only one excluded; the next sentence and L255 reach further, and the sentence does not say "only". Not a fault.
- **The owner's words.** S20: no list, count or grade of rivals. S21: the sentence says what a definition gives for a shape, not what must happen. S23: no forbidden word or idea; "fails" means only "does not meet"; the classification is held, like everything else, tentatively. S25–S27: no physical possibility. S28: whether anyone rules a given candidate out, and whether by a claim taken as given, is left to L397, where "the ruling out is a choice the person using it made, not something the claim does by itself (Part 0)".

## Cases

No fixed case verdict moves under this KEEP, and none would have moved under the rival.

- The S98 ledger records one record against L273.s1: CH-1131 / D-690 (S95), a vocabulary recommendation on "genuine, genuinely", marked superseded; it does not touch this sentence's words.
- `results/S96 Check of the repaired copy - cases.md`: **O2** ("The tide table with a real bell attached"; fixed verdict "Carla has explained the bell. She has explained nothing about the tide. The almanac is the answer written down."), recorded there as "l. 151, l. 255 and l. 273 give the verdict as before"; the almanac is a candidate whose only substantive component restates the answer, L273's second sentence, and it fails L255 under either wording of the first. **N8 (O59)** ("The machine that runs forever"): "A third answer, "because perpetual motion is impossible", would put the answer in as its only component and fail non-circular dependence (l. 255, l. 273)." The same under either wording. **O16** ("The worn key and the diary") turns on L397's formula, which neither wording touches.
- The text's own worked passages do not cite L273's first sentence: L331 ("it is circular", on a value set because it gives the mass favoured) turns on its own line; L343 ("Non-circular dependence is met") turns on L255.

## Dependents (named for the record; none is affected by a KEEP)

- L273, second sentence: "So does an account whose only substantive component restates the answer it was asked for; packaging a dependence that answers a different question beside it does not repair this."
- L536: "Part V says which of the four each classic attempt fails: a table of observed answers fails (F1); a reversed calculation fails (F2) under the production contract; conclusion-as-premise fails non-circular dependence."
- L397 (an echo, not a dependence): "Such an argument, as one against that claim, has its conclusion among its premises, as in "\(p\) because \(p\)", and does not rule that claim out for anyone."
- The S96 cases O2 and N8 (O59), which cite l. 273.

## Outside this item (not ruled here)

For the orchestrator only; nothing in this ruling rests on it. L273's second sentence says "So does an account whose only substantive component restates the answer it was asked for", that is, that an account fails non-circular dependence, while by (E) at L262 an account meets it. "Account" there is used for what is offered as one, where L269 ("it is an account when it meets the other conjuncts of (E)") and L277 use it strictly. Mimo's third variation follows the same pattern. That sentence is not C21 and is not ruled here.

## Parked (S34)

No point of either reader proposes anything about what hard to vary covers, and nothing here does. "Easy to vary" is used in the plain sense the brief gives it (section 5), not as the text's term at L317. The placement of values is not touched.

Nothing here is settled (S28): this ruling keeps the sentence tentatively, open to any later argument against it.
