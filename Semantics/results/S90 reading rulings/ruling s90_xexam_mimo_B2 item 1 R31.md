# Ruling: s90_xexam_mimo_B2, item 1, R31 (W21.1)

*A fresh Claude checker, 24 September 2026. It follows the S90 rule, as extended by "S90 Parts - how they will be read, written before sending.md" (rule 3), and "S90 and S87 - seven calls rerun after the container restart - written before sending.md" (§2 item 4: the pass-2 reply stands where the pass-1 reply would have stood). This checker did not draft, assemble or check the change list, and did not write the part briefs.*

*What it read:*
- *the whole reply (805 words by `wc -w`). The receipt shows it was accepted: pass 2, attempt 1, status 200, finish "stop", 0 bad chunks, and the last line is END OF REPORT. The response sha256 bbee0da8… matches the receipt.*
- *Pass 1 had two replies that came back and were rejected: first `content_filter`, then `length` with no content. They are recorded with pass 1 and were not read (rerun note §2 item 3; Parts rule 5).*
- *the batch 1 and batch 2 readings and the rulings folder, for any earlier ruling on this entry. There is none (see §1).*
- *the plan's row W21, the worklist's W21 and its conflict 7, and W19.2's recheck of skeleton conflict 12. These give the entry's history.*
- *file 00, L728–746, for the sentence the entry restores.*
- *the R31 section of the part B2 brief (md5 d214f495…), to see what the reply was given.*
- *Atria B2's point 3 on R31, which the orchestrator pointed to. It is read as another reader's view and is not counted (Parts rule 1). It opened no reasoning file.*

*Sources:*
- *the change list, md5 a5c92adc9f1e3806c0f9c6394cffde1e (as of 587eebf);*
- *the revised text, "Revision 2 - file 13 draft 2 …", md5 9aecf2f30ce0b4523606b2b8409fdf37;*
- *file 11, md5 5e494c1095d920d128b9a79de378f923, read only;*
- *the revision note, draft of 23 September (row R2-31);*
- *the S81 case book (md5 4f488d14…) and the S89 candidate book (md5 b2e53577…).*

## 1. The entry and its checkers' history

W21.1, "L405: ≡_ℓ is defined, and 00:746's first sentence is restored".
- **Place:** Part X, **Newness**, before the display (N). It is file-11 L405 and revised L407.
- **Group and reason word:** GROUP B2. REASON WORD clarification.
- **Record row:** R2-31, C26 in the S90 brief. The note lists it as CLAIM, declared.

- **OLD:** `**Newness.** With \(R_{<e}(s,h)=\bigcup_{\xi\text{ before }e}R_{\beta,\ell}(s,\xi)\),`
- **NEW:** `**Newness.** Write \(d\equiv_\ell c\) when there are transports from \(d\) to \(c\) and from \(c\) to \(d\), both faithful on \(c\)'s contract at grain \(\ell\). The equivalence is structural at the stated grain, not string equality or similarity. With \(R_{<e}(s,h)=\bigcup_{\xi\text{ before }e}R_{\beta,\ell}(s,\xi)\),`
- **KIND:** CLAIM.
- **DECLARATION:** "Part X now defines the equivalence in (N): d ≡_ℓ c when there are transports from d to c and from c to d, both faithful on c's contract at grain ℓ. The equivalence is structural at that grain, not string equality or similarity."

**The checkers' history:**
- **CHECK:** "check 1, SOUND."
- **W19.2's recheck of skeleton conflict 12** (change list, L2027): "W21.1 defines \(\equiv_\ell\) by faithful transports both ways, with no pairing of components across candidates, so it stands as drafted. O11, O18 and N15 keep W21.1's readings."
- **Where the choice of contract came from.** The plan's row W21 took "c's contract" on purpose ("**Take**: … both faithful on c's contract at grain \(\ell\); restore the first sentence of 00:746 only"). The worklist's W21 handling says the same.
- **The REASON field records the typing** that the reply disputes:
  - "a transport to c that is 'faithful on \(c\)'s contract' is (R)'s wording (L207)";
  - "a transport from c faithful on c's contract is Part V's (L233, with C a contract of the source)".
- **CASES AT RISK:**
  - O11, O3, O18, O31, O27, N15, N21 and N10 keep their marks.
  - N4 is watched: "The tilt idea as she held it may be equivalent, on the midnight-sun contract, to the account of the midnight sun. If so, a later working-out is not new for someone who already held the idea." Its direction is "not away".

**Other readers:**
- Atria (s90_xexam_atria_B2, point 3) found R31 standing. It gave the same two-part typing: "a transport to a content is assessed on the content's contract, as in (R); a transport from a content is assessed on its domain's contract, as in Part V". It did not contest the entry.
- **Batch 1 and batch 2 made no ruling on R31 or W21.1.** There is nothing to reconcile.

## 2. The reply's argument

The closing lines are "R31: FALLS — definition of ≡_ℓ applies \(c\)'s contract to a transport from \(d\) to \(c\), where Part V's (F1) requires the source's edits; the relation is non-symmetric despite ≡ notation" and "R31: FALLS — definition of ≡_ℓ ill-typed and non-symmetric". Point 1 (tasks (a) and (c)) argues this as follows.

**The phrase is ill-typed for the transport from d to c.**

> "The phrase "both faithful on \(c\)'s contract" is ill-typed for the transport from \(d\) to \(c\). … Here \(\lambda(k)\subseteq D\) is a subnetwork of the *source*, so \(\operatorname{Sol}_{\lambda(k)}(a,b)\) requires \((a,b)\) to be an edit–boundary pair of the source … For the transport from \(d\) to \(c\), the source is \(d\) … But "\(c\)'s contract" … ranges over \(c\)'s edits. The types do not match"

**(i) The relation is not symmetric.**

> "\(d\equiv_\ell c\) checks both transports against \(c\)'s contract; \(c\equiv_\ell d\) would check both against \(d\)'s contract. … Yet the text calls the result "The equivalence" and writes \(\equiv\), both of which standardly signal a symmetric relation."

**(ii) The declaration is misleading.**

> "If "the equivalence" denotes \(\equiv_\ell\) as a relation, the claim is false: the relation fails symmetry."

**(iii) "Faithful on" is used in two ways.**

> "The same phrase "\(c\)'s contract" appears in (R) at line 166–67 … for a transport from \(\operatorname{Org}_\ell(o)\) to \(c\)—again the target's contract on a source-to-target transport. R31 extends that second usage into the definition of \(\equiv_\ell\) and applies it to *both* directions at once"

**The repair it proposes.**

> "Replace "both faithful on \(c\)'s contract at grain \(\ell\)" with "each faithful on the contract of its source at grain \(\ell\)." … The declaration would then read: "\(d\equiv_\ell c\) when there are transports from \(d\) to \(c\) faithful on \(d\)'s contract and from \(c\) to \(d\) faithful on \(c\)'s contract, at grain \(\ell\).""

The reply names no case.

## 3. The texts

**1. The quotations (S90 rule 8).**
- NEW is found at revised L407. OLD is found once in file 11, at L405. Both match the brief byte for byte.
- The Part IV sentence "A transport is **faithful on \(C\)** when it satisfies the component and global fidelity conditions of Part V" is found at revised L189.
- The (F1) display is found at revised L236.
- "Part III: \(C\subseteq A\times B\) for a question with target \(c\)" is the reply's own paraphrase. Part III (L135–141) defines the contract \(C\subseteq A\times B\) of a question \(p\) whose target is \(D\).
- **One locator is wrong.** The (R) words "admits a transport to \(c\) that is faithful on \(c\)'s contract" are found at revised L205, and the display (R), with \(t:\operatorname{Org}_\ell(o)\to c\), is at L207–208. The reply's "line 166–67" is the heading "Occurrences and contents" and a blank line. The point is ruled on the text.
- The declaration's sentence is found in the DECLARATION field.

**2. Typing: NEW uses (R)'s own reading, and adds no usage the file lacks.**
- **What the reply gets right.** Part V states (F1), (F2) and (A) for a transport from \(D\) to \(E\) on a contract of the question whose target is \(D\), so on the source's pairs. The transport from c to d, on c's contract, is typed exactly that way.
- **The transport from d to c is (R)'s case.** (R) judges a transport *into* c on c's contract (L205, L208). The reply says so itself under (iii).
- **(R) is file-11 text** (file-11 L207), and none of the 55 changes touches it.
- **(N) is built on (R).** Deploy is "by (R) a faithful transport", and the repertoire, which gives (N)'s \(R_{<e}\), is the set of contents deployable (L397). So (N) already depends on the reading (R) needs.
- **What that reading is.** (R) can only be read with fidelity taken on the pairs the transport carries into c's contract, through \(\tau\) and \(\sigma\). Read that way, NEW's transport from d to c is typed like (R)'s, and its transport from c to d is typed like Part V's.
- **So there are not two meanings in one definition.** Both transports are checked on one set of changes, those c commits to: directly for c→d, and through the translation for d→c.
- The entry's REASON field records exactly this choice. Atria read it the same way.
- **Noted, not ruled.** Whether Part IV (L189) or (R) (L205–208) should state that reading in words is a question about file-11 text that no listed change alters. It is noted here for the change list's owner, and it is not a ground to change W21.1.

**3. Symmetry: true, harmless, and by design.**
- **What is true.** The reply is right that \(d\equiv_\ell c\) is taken on c's contract, so in general it is not the same condition as \(c\equiv_\ell d\).
- **Nothing uses symmetry.**
  - \(\equiv_\ell\) occurs only at L407 and in (N) at L410. A search of the revised text for `\equiv` finds no other occurrence.
  - (N) fixes c as the content whose newness is in question, and d ranges over the earlier repertoire.
  - No text swaps the arguments or relies on symmetry or transitivity. (G) and (EK) use New, not \(\equiv_\ell\).
- **"Equivalence" in the file's own sense.** Relational transport (L357) calls the two-direction condition "equivalence rather than one-sided abstraction", and NEW's two transports are that condition. The file's other equivalence, "of one kind on \(C\)" (L119), is also indexed by a contract.
- **The index is in plain view.** The definition writes the contract ("both faithful on \(c\)'s contract"), so a reader has no need to assume a symmetric relation.

**4. The declaration is not misleading.**
- It restates the definition word for word, "both faithful on c's contract" included.
- **Its second sentence says what kind of sameness is meant**, structural at the grain rather than string equality or similarity. It says nothing about symmetry. A relation that is not symmetric can still be structural, so the reply's (ii) does not follow.
- **The sentence is 00:746's first sentence** (file 00, L746), restored word for word as the plan asked. The declaration has "that grain" for "the stated grain".
- A reader of the declaration learns exactly what changed.

**5. The proposed repair changes the claim.** It is more than a typing fix.
- **What the repair demands.** Under "each faithful on the contract of its source", the transport from d to c must be faithful on *d's* contract.
- **What goes wrong.** Suppose an earlier content d commits on changes that c does not cover.
  - Then there is no such transport: \(\tau\) has no image for those changes in c, or c answers them differently.
  - So \(d\not\equiv_\ell c\), and c counts as new, although s already held a content that answers as c does on every change c commits to.
  - Newness would then turn on the whole contract of every earlier content, not on what c commits to.
- **It reverses a deliberate choice.** The plan's row W21 took c's contract on purpose.
- **It can reopen N4 in the away direction.**
  - The entry's N4 reading rests on equivalence "on the midnight-sun contract".
  - That reading agrees with the fixed verdict: "Working out the connection added nothing to the idea. It revealed what the idea already implied".
  - Take the account of the midnight sun as an organization narrower than the tilt idea as she held it. Under the repair, the working-out would be new for her.
- **Undeclared and untested.** The reply names no case and declares no such move. So the repair is refused.
- A repair that is symmetric and keeps the claim would only write the contract index into the notation, for example "≡ on \(C\)" with \(C\) c's contract. (N) already supplies that index, so it is not needed.

**6. Cases.**
- The reply names none.
- **The entry's cases keep its readings under NEW, as drafted:**
  - **O11.** "Wednesday is neither" holds whether or not Wednesday's content is equivalent to Tuesday's, because Wednesday has no Build. It is unchanged under either definition.
  - **O3 and N21.** No earlier content answers on the new content's contract (the tally of unseen cards; the grasp of the convention), so the content is new under either definition.
  - **O18, O31 and N15.** The corrected content differs from the received one at the new tooth, at the plant's valve, and at "more" for "less". So no transport between them is faithful on its contract, and it is new to her under either definition. Build credits only the binding (L399).
  - **O27 and N10** are unchanged.
  - **N4** is not away under NEW. It is reopened only under the reply's repair (point 5).
- No verdict moves under NEW.

## 4. Ruling: KEEP

The entry stands as drafted, byte for byte: OLD, NEW, KIND CLAIM and DECLARATION.

**Append to CHECK:** "After the cross-examination (s90_xexam_mimo_B2, point 1, R31 FALLS: 'ill-typed and non-symmetric'): KEEP.
- The transport from d to c is judged on c's contract as (R) judges a transport into c (L205–208, file-11 text unchanged, on which Deploy and so (N)'s repertoire rest). The transport from c to d is typed as in Part V. Both are checked on the changes c commits to.
- The relation is taken on the contract of the content whose newness is in question. (N) is its only use, and nothing uses symmetry. 'Equivalence' is the file's two-direction sense (L357).
- The declaration states the definition word for word.
- The proposed 'each faithful on the contract of its source' would make c new whenever an earlier content commits beyond c. That is a change of claim, against plan row W21, and it could reopen N4.
- Atria (s90_xexam_atria_B2, point 3) found the entry standing, on the same typing."

**No other field changes.** Nothing follows by program: the counts, the note's N and M, and record row R2-31 are unchanged.

**Conflicts:** none.
- W19.2's recheck of skeleton conflict 12 (no pairing across candidates) stands.
- W41.1 (R30) adds text at L399–403 and does not touch L407.

**Noted for the owner, not ruled:** a sentence at Part IV (L189) or (R) (L205–208), saying that a transport into c is faithful on c's contract when it is faithful on the pairs it carries into that contract, would state in words the reading the file already needs. It concerns file-11 text outside the 55 changes.
