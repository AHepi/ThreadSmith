# S103 Round 1 — ruling on C16 (L217)

*Written by a fresh checker (Opus 5.5), 27 September 2026, filled as it went (this file was created first as a stub and then filled; no other file was written over). Not committed.*

**Ruling: KEEP.** The sentence stands as it is at L217 of `tests/99 The semantics, standing alone.md` (md5 74f4a4c7619345747f4fa976ddac9548, checked before reading; not written to):

> For an edit–boundary pair \((a,b)\in C\) actually occurring:

This ruling settles nothing (decision S28). It records that the sentence came through both readers' attempts and this checker's own, that no attempt found a wording that keeps what the theory needs from it and reads more plainly, and that no point of either reader, nor any this checker could find, shows a defect in it. This file obeys decision S23 except where it quotes a reply or the owner.

## How this checker came to the item

The tabulation (`results/S103 Round 1 - reading/tabulation.md`, the C16 section and the note under "Candidates held under both readers' attempts") records both readers closing HOLDS and marks C16 under rule 6 of the reading rule: no checker, to be recorded "held under both readers' attempts; not thereby final". The orchestrator sent it to a checker all the same. This file stands where the task names it (`results/S103 Round 1 - reading/rulings/ruling C16.md`), not where rule 11 of the reading rule names it (`results/S103 Round 1 - rulings/ruling C<nn> L<line>.md`); the sibling rulings stand at the task's path too.

Read for this ruling: the reading rule (`results/S103 Round 1 - how the replies will be read, written before sending.md`); decisions S20 to S35 in `records/Semantics - Decisions.md`; the part 2 brief's entry for C16 (`tests/S103 Round 1 - trying to vary the strong candidates - part 2, Parts III and IV.md`, md5 387f826f93ba0922458007feefc6bd61, lines 81–104); the tabulation's C16 section; Mimo's C16 section (`s103_vary_mimo_2.response.txt`, lines 83–106) and GLM's (`s103_vary_glm_2.response.txt`, lines 75–99), whole; a search of all six replies for "C16", "L217", "occurring" and "actually occur" (nothing else names the item); no `.reasoning.txt` file. In file 99: L23, L39–L47, L53, L83–L105, L131–L161, L165–L225, L229–L265, L307, L315–L317, L375, L429, L459–L481, L562–L584, L618–L632. The S98 ledger (`results/S98 Ledger of edits and recommendations/line-up/data/by sentence.csv`): it has rows for L217.s1 (the "Let \(t\) be …" sentence, changed in S90) and for the heading and the name "surprise" (S95 proposals open for the owner), and none for L217.s2, the sentence under review, which stands as it stood in file 11. The case books (`tests/S81 Case book - the 52 cases, situations and fixed verdicts, as the tested agent sees them.md`, `tests/S89 Case book - candidate cases N1 to N25 drawn from the sources.md`), searched for surprise, violation, occlusion and occurring. Every quotation below was compared with file 99 by program, each found on the line given.

## The sentence in its place

L217 holds two sentences; C16 is the second, the head of the three definitions under it:

> L217| Let \(t\) be a transport to the simulation layer \(S\), with contract \(C\) and, where \(t\) is selected, history \(H\). For an edit–boundary pair \((a,b)\in C\) actually occurring:
>
> L219| - the **prediction** is \(\operatorname{Ans}_S(\tau(a),\sigma(b))\);
>
> L220| - a **violation** occurs when fidelity fails at \((a,b)\);
>
> L221| - **surprise** is a violation of a selected transport at \((a,b)\notin H\).

What it uses:

- **contract**, L141: "The **contract** \(C\subseteq A\times B\) is the set of admitted edit–boundary pairs the claim ranges over". Every pair of \(C\) is admitted; the contract does not say which pairs ever occur.
- **admission is not occurrence**, L159: "admitting a change is not a claim that it can be carried out or come about".
- **history**, L195: "a finite history \(H\subseteq C\) of edit–boundary pairs actually encountered"; and L225: "A **selection response** extends the history \(H\) of a selected transport and lets \(\mu\) act". \(H\) grows by a selection response, not by an occurrence as such.
- **fidelity**, L189: "A transport is **faithful on \(C\)** when it meets the component and global fidelity conditions of Part V." Fidelity at a pair is a relation between the transport and the target at that pair, whether or not the pair occurs; L41: "Whether that transport is faithful on changes it was never selected against turns on the transport and the target alone, not on whether it survived." and "Survival is how the transport got there; fidelity is what it is."
- **prediction**, L177: the simulation layer's "queries are predictions: what a port of \(P\) will take under an admitted edit."

## What the sentence does

It is the quantifier head of L219–L221, and its one piece of content is the qualifier "actually occurring". The contract ranges over admitted pairs (L141); the qualifier picks out, among them, a pair that occurs. That is what turns the three definitions under it into definitions of events:

- a **violation** "occurs" (L220): it is an event at an occurring pair, not the standing fact that fidelity fails at some pair of \(C\). The standing fact is what L41 calls fidelity, "what it is"; the event is what happens when a change the transport is unfaithful at comes about;
- **surprise** (L221) is such an event for a selected transport at a pair outside \(H\). L223 spells the qualifier out twice: "the contract must contain changes the system's correspondence was never shaped against, and one of them must occur (Argument 4)", and "a constructed one that fails at an actually occurring pair of its contract is violated, and the failure is not surprise"; L582, Argument 4's reason why this and not its denial, restates the definition as "Surprise is defined (Part IV) as a violation of a selected transport at an occurring \((a,b)\in C\) with \((a,b)\notin H\)"; L584 reads it as "the signature of a selected transport meeting a change outside its history";
- the **prediction** (L219) is the value the simulation layer gives at that pair, the one a violation contradicts. L177 already gives predictions under every admitted edit; L219 names the one in play at an occurrence.

The worked case that turns on it is Argument 10: a transport \(t_0\) "selected on a history \(H_0\subsetneq C_0\) containing displacements and velocity changes but no occlusions" (L622); then L624: "An occlusion occurs." … "is violated when the thing re-emerges at a cell consistent with its velocity. This is surprise (Argument 4)." The occlusion pair is in \(C_0\), outside \(H_0\), and occurs; the verdict "This is surprise" is reached through this sentence's qualifier.

## The readers' points, weighed

Both readers close HOLDS; they do not differ, so rule 7 has no disagreement to rule between. Each point is weighed on its argument.

**Dropping the qualifier** (GLM, reply line 81: `For an edit–boundary pair $(a,b)\in C$:`). GLM: prediction and violation would be defined on pairs that never occur; L582 would no longer restate the definition; what L159 keeps apart would be undone. The point holds, and this checker adds three places it reaches. (i) L220's "a violation occurs" would lose its event: a violation would be no more than a failure of fidelity at a pair of \(C\), which L41 keeps as what the transport is, apart from what happens to it. (ii) Surprise would become a standing property of every selected transport unfaithful at some pair outside \(H\), there before any change comes about; L223's "and one of them must occur" would do no work. (iii) In Argument 10, \(t_0\) would count as surprised before any occlusion, and L624's "An occlusion occurs." would do no work for the verdict "This is surprise". Mimo's rival `For an admitted edit–boundary pair \((a,b)\in C\):` (reply line 88) is the same move, since every pair of \(C\) is admitted (L141); Mimo's reason, "admission is not occurrence", with L159, L223 and L582, is the same point and holds for the same reasons.

**"Encountered"** (Mimo, reply line 93: `For an edit–boundary pair \((a,b)\in C\) actually encountered:`; GLM, reply line 87: `For an encountered edit–boundary pair $(a,b)\in C$:`). Both: "encountered" is the word L195 uses for the pairs of the history \(H\), which only a selected transport has, while L223 defines prediction and violation "for every transport to the simulation layer", declared ones included (L199: "**Declared.** Neither of the above. The transport is entered into the model by its author."). The point holds. This checker adds: \(H\) grows only by a selection response (L225), so a pair can occur and stay outside \(H\), which is exactly the surprise case; heading the definitions with L195's word for the members of \(H\) would invite reading every pair that meets the definitions as a member of \(H\), against L221's "\((a,b)\notin H\)".

**"Coming about"** (Mimo, reply line 98: `For an edit–boundary pair \((a,b)\in C\) actually coming about:`). Mimo says it breaks L159 ("whether anyone could carry a change out, or whether it could come about, is a matter of instantiation and transformation (Part XII)") and S25. This checker does not find the break. L159 speaks of whether a change *could* come about, a matter of physical possibility; "actually coming about" speaks of a change that does come about, as "actually occurring" does. Neither wording makes physical possibility a condition of a question, an account or a conflict (S25; L461: the physical module "does not define a question, an account or a conflict between candidates (Parts III, V, VI)"). The rival is a rewording: it changes nothing the theory needs from the sentence. It is not clearer, and it would part the sentence from the words L223 ("an actually occurring pair of its contract") and L582 ("an occurring \((a,b)\in C\)") use to restate it. On the reading rule's rule 5 it is recorded, not taken: the sentence is easy to vary in this verb, at the level of a synonym, and that changes none of its content.

**"Physically realized"** (GLM, reply line 93: `For a physically realized edit–boundary pair $(a,b)\in C$:`). GLM: occurrence is the right notion, but the wording invites reading physical realization as a precondition inside the theory, against S26, and moves away from L582's phrase. The point holds, and this checker finds a sharper break: it is a different claim, a narrowing. Contracts range over changes "in whatever the target is: a garden, a mathematical structure, a melody or a philosophical claim" (L159), and "Neither layer is presupposed to exist in any particular physical system" (L179). Argument 10 is a stipulated episode: "This episode is a relative-consistency instance for the class." (L632). Its occlusion occurs in the stipulated episode; nothing in it is physically realized. Under GLM's rival, L624's verdict "This is surprise" would no longer be reached, and a fixed verdict of the text would move.

**\(C\) replaced by \(H\)** (Mimo, described, no wording written out). With the pair taken from \(H\), L221's "\((a,b)\notin H\)" could never be met, and prediction and violation would be undefined for transports with no \(H\). The point holds.

## This checker's own attempts

- **"that occurs"**: `For an edit–boundary pair \((a,b)\in C\) that occurs:` is a rewording, as "coming about" is. It is not clearer, and it drops the word "actually", which marks the contrast with admission (L141) and which L223 repeats ("an actually occurring pair of its contract"); taking it would ask L223 to follow for no gain.
- **"observed" or "detected"**: this would tie violation and surprise to a record of the change, which is the verificationist reading decision S23 removes, and it would merge two things L223 keeps apart: a violation, and "a violation the system represents", which "can be a recognized difficulty (Part X)". The present wording keeps them apart.
- **The qualifier moved off the prediction bullet**: one might say the qualifier should govern only L220–L221, since L177 gives predictions under every admitted edit and L630 says the swap edit "leaves every prediction unchanged" without that edit's occurring. This checker finds no conflict to repair: L177's predictions are the simulation layer's queries at any admitted edit; L219 names, at an occurring pair, the one a violation contradicts; the two agree wherever both apply, and L582 ("If there is no transport there is no prediction and hence no violation.") reads the same either way. Moving the qualifier would rebuild L217–L221 and touch C17 and C18, with nothing gained that the present wording lacks.
- **Where the pair occurs**: the sentence does not name where. The contract \(C\) is a set of pairs of the transport's domain (L141, L189), so the pair occurs there; for a transport from the object layer, that is the system meeting the change, as L584 has it. No reading was found on which the place is in doubt.

## The owner's decisions

- **S25–S27.** "Actually occurring" is a condition of actuality, not of physical possibility, and it defines no question, account or conflict. Where the target is physical, the occurrence is a physical change meeting a transport a system holds, which is knowledge instantiated in a carrier and transformed by the change (L461 names "testing" among the transformations of a content); that is where S26 lets physical possibility come in. Where the episode is stipulated, as in Argument 10, the occurrence is stipulated. No reader's point and no attempt of this checker's finds the sentence crossing S25.
- **S28.** The sentence says what the definitions are at an occurring pair; it does not say that anyone knows a pair occurred. Whether something occurred stays a claim that can be in error; L53, on selection: "Whether it occurred is a claim about the physical module, fallible as any claim about it is (Part XII)." Nothing is settled.
- **S23.** No word or idea S23 removes; "actually" is not an accepting word.
- **S20, S21.** No list, count, grade or record of rivals; nothing about what must happen to a candidate. (L223's "one of them must occur" is a condition of the definition of surprise, not a claim about what a person does.)
- **S33–S34 (parked).** No point of either reader proposes anything about what hard to vary covers, and this ruling proposes nothing about it. "Easy to vary" above is meant plainly, as the brief asks. No value is moved in or out.

## Fixed case verdicts

- **Argument 10** (L618–L632), the worked case the text ties to this sentence: "This is surprise (Argument 4)." stands; with KEEP nothing changes. Of the rivals, dropping the qualifier (and "admitted") would make the occlusion idle for that verdict, and "physically realized" would block it.
- **Case book O3** (Nadia and the cards she has never seen), whose situation says she "is often surprised": its fixed verdict ("Nadia built something new: a part that stands for cards she has never observed. That is construction, and it is her own.") turns on construction, not on this sentence; nothing moves.
- **S89 case book**: its one mention of surprise (line 499) is a note on a rewrite of a candidate case, not a verdict tied to this sentence.
- **The S98 ledger** has no row for L217.s2 and ties no case to it.

## What depends on the sentence (nothing changes under KEEP)

- L219–L221, the three definitions in its scope.
- L223: "Surprise requires an incomplete selection history: the contract must contain changes the system's correspondence was never shaped against, and one of them must occur (Argument 4)." and "Prediction and violation are defined for every transport to the simulation layer, surprise only for a selected one: a constructed one that fails at an actually occurring pair of its contract is violated, and the failure is not surprise; a violation the system represents can be a recognized difficulty (Part X)."
- L225: "Two responses to a violation are distinguished." and the two responses defined after it.
- L576: "It is also why surprise is possible."
- L580–L584: Argument 4, its claim, its reasons (L582, which restates this sentence) and its consequence.
- L622–L626: Argument 10's occlusion, violation, surprise and the two responses.

## Result

- **Ruling:** KEEP.
- **old = new** (L217): `For an edit–boundary pair \((a,b)\in C\) actually occurring:`
- **Easy to vary?** No reader closed VARIES. One tried wording ("actually coming about", Mimo, reply line 98) and one of this checker's ("that occurs") are rewordings that change nothing the theory needs; neither is clearer, and each would part the sentence from the words L223 and L582 use to restate it, so each is recorded, not taken. Every wording that changes what the sentence claims (no qualifier, "admitted", "encountered", "physically realized", \(H\) for \(C\)) breaks a named line or Argument 10's verdict.
- **Parked (S34):** nothing.
- **Recorded:** held under both readers' attempts and this checker's; not thereby final.
