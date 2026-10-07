# S103 Round 1 — ruling on C27 (L443)

*Written by a fresh checker (Opus 5.5), 27 September 2026, filled as it goes. Not committed. This file obeys decision S23 except where it quotes the text, a reader, a record or the owner.*

**Ruling: FIX.**

- **Old (L443, the second sentence of the line):** `An explanatory aim requires an account, or the correction of a use through one, to be deployable.`
- **New:** `An explanatory aim requires a deployable account, or the correction of a use through one.`
- **The change:** "an account" becomes "a deployable account", and ", to be deployable" leaves the end. Nothing else on L443 changes: the bold heading, its bracket and the next sentence ("With \(O_{\mathrm{ex}}\subseteq O\) the explanatory aims,") stand as they are.
- **The new wording is Mimo's own rival at reply line 200**, the one Mimo calls "the repair" (line 203), not the wording of Mimo's closing line (line 221) nor GLM's (line 103). Why this one and not those is set out below.
- **Easy to vary on this reading:** not a VARIES verdict. Both readers closed FAILS, and the fault is shown (below), so the rivals are repairs of a fault, not rewordings of a sentence that works. Of the repair wordings, the one ruled here changes nothing the theory needs from the sentence; the others either keep the fault or say something different (below).

## What was read

- The text under review, `tests/99 The semantics, standing alone.md`, md5 74f4a4c7619345747f4fa976ddac9548 (checked before reading; not written to): L380–L470 whole (the end of Part IX, Part X and Part XI whole, the start of Part XII), L526–L528, L620–L632, and the whole file searched by program for "explanatory aim", "(EX)", "CreateEx", "deployable", "correction of a use" and every quotation below.
- The reading rule, `results/S103 Round 1 - how the replies will be read, written before sending.md`, whole.
- The part 3 brief, `tests/S103 Round 1 - trying to vary the strong candidates - part 3, Parts V to XIV.md` (md5 44ef4fbdb179963c3e76fcdaf60ecf27): the C27 entry (brief lines 147–171).
- The tabulation, `results/S103 Round 1 - reading/tabulation.md` (md5 51e752c3e26ab822e69daf8e9ec9f387): line 44, C27's section (from line 2675) and the notes at lines 3041 and 3048.
- The replies: `s103_vary_mimo_3.response.txt` (md5 a1491ae7b541cf691c5760cf07c93d44) lines 191–222 and `s103_vary_glm_3.response.txt` (md5 540429867c7029b78bcb9ad72c1af834) lines 89–108. All six replies were searched for "C27"; there is no hit outside those two sections. No reasoning file was opened.
- The owner's decisions S20–S35 in `records/Semantics - Decisions.md` (md5 71459192867b1ebcf1bae914c9297129).
- For ties to cases and history: the S98 ledger, group 11, entry L443.s2 (and L443.s1), with `line-up/data/by sentence.csv` searched for "L443"; `results/S96 Check of the repaired copy - cases.md` (md5 3ab6bf93a5f7df386a726c631e550123) and `results/S95 Scrub - cases re-read on the scrubbed text.md`, searched for "l. 443", "(EX)", "explanatory aim" and "correction of a use"; the S81 case book of 52 cases (md5 4f488d149e44669240d5db546c8e946a), case O13, and the S81 results table row for it; the S89 candidate cases N1 to N25 (md5 b2e535777976a511935430bd089ba500), case N10; files 10, 11 and 12 and the plain-words working record of S92, searched (read only) for "correction of a use".

**File name.** Written to the task's path, `results/S103 Round 1 - reading/rulings/ruling C27.md`, not to the reading rule's `results/S103 Round 1 - rulings/ruling C27 L443.md` (rule 11); the other checkers' rulings stand in the same folder. The difference is the orchestrator's to settle.

## The sentence and where it stands

L443 opens Part XI's "Created explanation" and introduces (EX):

> **Created explanation.** An explanatory aim requires an account, or the correction of a use through one, to be deployable. With \(O_{\mathrm{ex}}\subseteq O\) the explanatory aims,

It is the only place in the text that says what an explanatory aim is: which of the claimed aims \(O\) belong to \(O_{\mathrm{ex}}\), the set (EX) quantifies over at L448 ("\exists o\in O_{\mathrm{ex}}"). Aims are "declared inputs: \(O\) says what is to be repaired and \(P\) what is to be protected, each as a stated condition over stated occasions" (L441).

The terms it uses:

- **Deploy** (L403): "\(\operatorname{Deploy}_{\beta,\ell}(s,c,\xi;U)\) is met when \(s\) at \(\xi\) holds a representation of \(c\), by (R) a faithful transport with selected or constructed provenance, integrated into problem-directed activity and serving the declared use task \(U\) as a retained capability (Part XII). The repertoire \(R_{\beta,\ell}(s,\xi)\) is the set of contents deployable in some nontrivial use respect."
- **Content** (L425): "The content \(c\) may be an organization, a transport, or a contract."
- **Repair and its contribution** (L435): "The contribution \(\Delta\) of a repair is a subhistory together with the changes of content it makes." (P) at L438 is a relation on two states and a contribution.
- **(EX)** (L447–L449): for some \(o\in O_{\mathrm{ex}}\), \(\neg o(\xi)\land o(\xi')\), Origin, "\operatorname{Account}\big((c,p_c,t_c,\Gamma_c)\big)\land c\in\operatorname{Result}(\Delta)\land\operatorname{Deploy}_{\beta,\ell}(s,c,\xi';U_c)\land\operatorname{ProducesVia}(\Delta,c,o;\xi,\xi')".
- **ProducesVia and \(U_c\)** (L453): "\(\operatorname{ProducesVia}(\Delta,c,o;\xi,\xi')\) is met when an active route that runs from \(\Delta\) to the repair of \(o\) contains the relevant binding of \(c\)." and "\(U_c\) is the declared use task for \(c\) (Deploy, Part X)".

**History.** The sentence has stood since file 10, where it read "An epistemic obligation requires a correct account, or the correction of a use through one, to be deployable." (file 10, line 446, read only). The S95 scrub changed "epistemic obligation" to "explanatory aim" (D-699) and "a correct account" to "an account" (D-689); the grammar of "or the correction of a use through one, to be deployable" was never touched. No earlier round proposed anything about it alone (S100: "never challenged"). The plain-words working record of S92 carried the same shape ("a demand that a correct account, or the correction of a use through one, be understood"), and its cold reader wrote at that line: "Confused: "the correction of a use through one"?" and "Question: What is a correction of a use?" (`plain words/92 working record/cold read 1.md`, lines 639–641). That is background, not a count.

## What the theory needs from the sentence

1. To say which aims are explanatory, so that "\(o\in O_{\mathrm{ex}}\)" in (EX) has a meaning.
2. Two kinds of explanatory aim. The first is an aim whose meeting asks for a deployable account; the worked case names one: "the aim "possess a deployable account of re-emergence after occlusion"" (L628). The second is an aim that a use be corrected through an account: an aim about something other than holding an account, which is explanatory because the account is the route of the correction. (EX) checks that route with ProducesVia (L453), and L441 names the attribution: "a repair produced through use of an account".
3. That what is to be deployable is the account, in both kinds: (EX) deploys \(c\) and nothing else, "\operatorname{Deploy}_{\beta,\ell}(s,c,\xi';U_c)" (L449), whichever kind \(o\) is; and Deploy's first argument is a content (L403).
4. Deploy kept among what (EX) uses, as the dependence order says: "(P), (EX) depend on (G), (E), Deploy;" (L526).

## Each side's argument (rules 5 and 7)

**Mimo (FAILS; reply lines 191–221).** Step 3: "In the sentence as it stands, "to be deployable" governs the disjunction "an account, or the correction of a use through one", so a *correction* is made deployable. Deploy is a relation on contents … A correction of a use is a change, not a content. The charitable reading needs the complement moved onto "an account" alone; the words do not do that." (line 219). Rivals: line 196, "An explanatory aim requires an account, or a use corrected through one, to be deployable.", which "keeps the fault"; line 200, "An explanatory aim requires a deployable account, or the correction of a use through one.", which "types correctly, and is the repair" (line 203). Variations: line 208, "An explanatory aim requires an account to be deployable.", which "Drops the alternative the sentence marks"; line 214, "An explanatory aim requires the correction of a use through one to be deployable.", said to break L403 and L449. Closing-line repair (line 221): "An explanatory aim requires an account to be deployable, or a use to be corrected through one."

**GLM (FAILS; reply lines 89–108).** The same fault, with a second reading: on the "repair-event reading" the second disjunct "cannot be deployable", since correction "is repair, a relation on histories and contributions" (L438); "On the charitable reading — that "the correction of a use" denotes a corrected content — (EX) still deploys the account, not a corrected use" (L449, with \(U_c\) at L453). "What (EX) actually requires, in both kinds of explanatory aim, is a deployable account that runs to the repair" (line 93). Variations: "An explanatory aim requires a deployable account." drops the correction coverage (line 97); "An explanatory aim requires an account, or a corrected use, to be deployable." has the "same type fault" (line 98). Repair (line 103): "An explanatory aim requires an account to be deployable, whether the aim is that account or the correction of a use through it."

**Where they agree and where they differ.** They agree on the fault, on its grounds (L403, L449) and on which variations break. They differ only on the repair wording; Mimo's own section holds two repairs that differ from each other (line 200 and line 221). The number of readers decides nothing here; what follows weighs the wordings.

## Is the failure shown?

Yes.

- **The grammar.** In "requires X, or Y, to be deployable", the infinitive "to be deployable" takes the whole coordinated object as its subject; the commas set "or the correction of a use through one" in the same slot as "an account". So the words say that the aim requires the correction of a use to be deployable. The reading in which "deployable" belongs to the account alone ("the correction of a use through a deployable one") is what a charitable reader supplies; the words do not give it, as Mimo says.
- **The types.** Deploy's first argument is a content, of which the system "holds a representation" (L403), and the repertoire is "the set of contents deployable" (L403). The contents the text names are organizations, transports and contracts (L425). A correction is a repair: a relation between two states brought about by a contribution, "a subhistory together with the changes of content it makes" (L435, L438). It is not a content, and nothing in the text defines what it would be for one to be deployable.
- **GLM's second reading does not rescue the sentence.** If "the correction of a use" is read as the corrected use, a use is what Deploy's last argument \(U\) names ("serving the declared use task \(U\)", L403), not its first; and (EX) still deploys only \(c\), with \(U_c\) "the declared use task for \(c\)" (L453). Either way the second disjunct asks deployability of something (EX) never deploys, and says nothing of the deployability of the account (EX) does deploy.

So on its own words the sentence, for the second kind of aim, misstates what (EX) asks: need 3 above fails. The fault is small in effect, since (EX) states Deploy of \(c\) outright, but it is a fault of the sentence itself, and it sits in the only place that says what an explanatory aim is.

## The repair wordings, weighed

**Mimo, line 200 (ruled): "An explanatory aim requires a deployable account, or the correction of a use through one."**

- Need 1 and need 2: kept. The first disjunct is the first kind in the worked case's own words ("possess a deployable account", L628); the second keeps the text's phrase "the correction of a use through one" word for word.
- Need 3: met. "Deployable" now stands on "account", where Deploy applies (L403, L449). "One" takes up "deployable account", so the account through which a use is corrected is a deployable one, as (EX) asks of every \(o\in O_{\mathrm{ex}}\). Were a reader to take "one" as "an account" alone, the second disjunct would say less than (EX), not something against it, and nothing ill-typed would remain.
- Need 4: kept ("deployable").
- It is the smallest change that removes the fault: one adjective moved from a trailing infinitive onto the noun it belongs to, the article changed to suit it, and nothing else. It says no more and no less than the text meant, and it keeps "deployable" over both kinds, as the text's trailing "to be deployable" was placed to do.

**Mimo, line 221 (the closing line): "An explanatory aim requires an account to be deployable, or a use to be corrected through one."** Well-typed, and it removes the fault. But "one" here takes up "an account", not "a deployable account" (the infinitive "to be deployable" is not part of the noun phrase), so the second kind of aim no longer says that the account through which the use is corrected is deployable: need 3 is met for the first kind only, where the text's wording (and the line 200 wording) carries deployability across both. It also rewrites "the correction of a use" into "a use to be corrected", a larger change than the fault asks for. Not taken: a larger change that says less of the second kind.

**GLM, line 103: "An explanatory aim requires an account to be deployable, whether the aim is that account or the correction of a use through it."** Well-typed in "an account to be deployable", but "the aim is that account" makes an aim an account. An aim is "a stated condition over stated occasions" (L441), and the text's own explanatory aim is "possess a deployable account of re-emergence after occlusion" (L628): the aim is the possessing, not the account. The wording repairs one slip between kinds of thing by making another. It is also longer than the fault asks for. Not taken. GLM's matching point, that (EX) deploys the account in both kinds of aim (line 93, line 106), is kept: it is need 3, and the ruled wording meets it.

**The wordings that keep the fault or drop a kind.** Mimo line 196 ("a use corrected through one, to be deployable") and GLM line 98 ("a corrected use, to be deployable") keep "deployable" on the use: the fault stays, as both readers say. Mimo line 208 and GLM line 97 ("requires a deployable account") drop the second kind: need 2 fails, as both say. GLM's ground for keeping the second kind, S20's "Once the explanation is rescued, the mistake shouldn't be able to creep back in" (line 97), is GLM's reading, not something S20 says about aims; the ground used here is the text's own: ProducesVia (L453) and L441's "a repair produced through use of an account". Mimo line 214 ("the correction of a use through one to be deployable") keeps only the ill-typed half; "one" there also has no antecedent.

## The owner's decisions

- **S20:** the new wording lists, counts and grades nothing, and this ruling weighs named wordings on their arguments, not by how many proposed them.
- **S21:** it says what an explanatory aim asks for its meeting, not what must happen to any candidate or what a person must choose. "Requires" is the text's word and stays in the same role.
- **S23:** no forbidden word or idea enters; "account", "deployable", "correction" and "use" are the text's own terms, and "correction" is the error correction the owner's words name (S27), with no measure attached. The words S95 took out of this sentence ("epistemic obligation", "a correct account") stay out.
- **S25–S27:** nothing about physical possibility enters or leaves.
- **S28:** nothing is settled by the new wording; it changes what the sentence says of a kind of aim, not the standing of any candidate.
- **S33–S34:** no proposal on either reader's C27 section, or in this ruling, is about what hard to vary covers; nothing is parked. The placement of values is not touched.

## Cases and dependents: no fixed verdict moves

- **The worked case (L620–L630).** Its aim, "possess a deployable account of re-emergence after occlusion", is an explanatory aim under the old wording and under the new; the new first disjunct uses the case's own words. Its verdict, "since \(S_1\) is an account on its contract and deployable, (EX) is met" (L628), turns on (EX), which is unchanged. SAME.
- **N10 (O61), the burned notebook** (S89 case book). S96 marks it "NOW SILENT" until the owner rules on the provisional name at L443; the ruled change does not touch the name, its bracket or (EX). If the owner rules that the case's word is (EX), Halima's aim (to hold a deployable account of why the design would fail) is of the first kind under either wording. Unchanged.
- **O13, two plumbers** (S81 case book; the S81 table reads it as an application of (P) and (EK)). Its verdict, "Nobody here made a repair that came from an explanation", turns on ProducesVia and on L441's "three different attributions", neither of which changes. If Ben's leak is read under an aim that a use be corrected through an account, the new wording says, more plainly than the old, that the correction must come through the account, which is where the case turns. SAME.
- **L443.s3 and (EX) (L443–L453):** unchanged; "the explanatory aims" now follows a sentence that says of them what (EX) checks.
- **L526 (dependence order: "(EX) depend on … Deploy"):** unchanged; Deploy is still used.
- **L528 (the explanation-creation class) and L600, L612 (Arguments that name (EX)):** unchanged; none uses the sentence's wording.
- No other line of file 99 uses "correction of a use" or "to be deployable"; "deployable" stands only at L403, L443 and L628.

## Result

FIX at L443. Old: `An explanatory aim requires an account, or the correction of a use through one, to be deployable.` New: `An explanatory aim requires a deployable account, or the correction of a use through one.`
