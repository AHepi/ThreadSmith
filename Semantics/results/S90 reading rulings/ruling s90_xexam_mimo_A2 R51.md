# Ruling: s90_xexam_mimo_A2, R51 (W19.2)

*A fresh Claude checker, 23 September 2026, under the S90 rule as extended by "S90 Parts - how they will be read, written before sending.md" (rule 2: an undeclared change of claim that a reply names is re-examined whatever line the reply gives it). This checker did not draft, assemble or check the change list and did not write the part briefs. It read only the reply's point 3 (R51, task (a)), the task (d) paragraph that follows it and names R51's cases, the closing lines, and the receipt (finish "stop", END OF REPORT last). Sources: change list as of 587eebf (unchanged at HEAD); revised text md5 9aecf2f30ce0b4523606b2b8409fdf37; file 11 md5 5e494c1095d920d128b9a79de378f923.*

## 1. The entry and its checkers' verdict

W19.2, "Derivation 2: 'Same anchors, one account'". Part XVI, Derivation 2, file-11 L552–558, revised-text L554–562. KIND: CLAIM. REASON WORD: change of claim. Revision-note id R2-51 = R51.

- **OLD:**

````text
## 2. Indistinguishable is identical

**Claim.** Two candidates \(\mathcal E,\mathcal E'\) for the same \(p\) that both satisfy (F1), (F2), and (A) on \(C\) are one account at grain \(C\): their components are pairwise of one kind on \(C\) and their answer profiles coincide.

*Proof.* Immediate from Derivation 1 and (A). ∎

**Consequence.** Underdetermination of an account by a contract is not a failure of the semantics to decide; it is the semantics reporting that the contract does not contain the distinction. The remedy is a finer contract, which is a new question. A claim that two such candidates "really" differ is a claim that some admitted change separates them, and must supply it.
````

- **NEW:**

````text
## 2. Same anchors, one account

**Claim.** Let \(\mathcal E,\mathcal E'\) be candidates for the same \(p\) that both satisfy (F1), (F2) and (A) on \(C\). (i) Their answer profiles coincide on \(C\). (ii) If a bijection \(\varphi\) of their active components gives each \(k\) and \(\varphi(k)\) one anchor, the same subnetwork of \(D\) with port translations onto the same ports of \(D\), then \(k\) and \(\varphi(k)\) are of one kind on \(C\) for every \(k\); so far as (F1), (F2) and (A) reach, the two are one account on \(C\): \(\varphi\) pairs their active components, each pair of one kind on \(C\), and by (i) their answer profiles coincide.

*Proof.* (i) By (A), \(\operatorname{Ans}_E(\tau(a),\sigma(b))=\operatorname{Ans}_p(a,b)=\operatorname{Ans}_{E'}(\tau'(a),\sigma'(b))\) for every \((a,b)\in C\). (ii) By Derivation 1, \(k\) has the signature of its anchor on the ports its translation names, and \(\varphi(k)\) the signature of the same anchor on the same ports; composing the one translation with the inverse of the other gives a footprint bijection under which the two signatures, read on \(C\), coincide. ∎

Without the premise of (ii) nothing more follows: candidates that anchor different subnetworks, or cut \(D\) at different places, are different candidates with one answer profile (Derivation 9; Part VI, redundant routes). A coarsening is not a recoding (Derivation 8).

**Consequence.** Where two candidates that satisfy (F1), (F2) and (A) differ only in which component carries which anchor, the contract does not contain the distinction; a claim that one assignment is "really" right is a claim that some admitted change separates them, and must supply it. The remedy is a finer contract, which is a new question.
````

- **DECLARATION:** "Derivation 2 no longer says that two candidates for one question that satisfy (F1), (F2) and (A) on C are one account whose components are pairwise of one kind. It now says that their answer profiles coincide on C; that where a bijection of their active components gives each pair one anchor, the same subnetwork of D with port translations onto the same ports of D, each pair is of one kind on C and, so far as (F1), (F2) and (A) reach, the two are one account; and that without that premise nothing more follows. Its Consequence now covers only candidates that differ in which component carries which anchor."
- **Checkers' verdict (CHECK):** "as W19.1. The text is the settled wording (F1, block 1), copied byte for byte." W19.1's CHECK: not put to check 1 or check 2, which ran before S88 was settled; checked by its drafter only (applied by program with no refusal or overlap, read in place, guard rows worked); no outside reader had seen the wording. No FIX/SOUND history. The entry's own LOSS already reads: "The slogan 'indistinguishable is identical' goes. The Consequence reaches only anchor assignments. Whether two differently decomposed candidates are one account is left undefined." Its CASES AT RISK work O46, O45, O36, O24, O10, N17 and N25, and flag N25's second question as watched (a reader who rested "idle" on the old slogan may go AGREE→SILENT).

## 2. The reply's argument

Closing line: "R51: STANDS". The change is re-examined because point 3 names an undeclared change of claim. Point 3 (task (a)), whole:

> "The declaration says 'without that premise nothing more follows.' But the new wording does claim something more, at lines 561–562: 'candidates that anchor different subnetworks, or cut \(D\) at different places, are different candidates with one answer profile (Derivation 9; Part VI, redundant routes).' The old Consequence's general principle—'A claim that two such candidates "really" differ is a claim that some admitted change separates them, and must supply it'—applied to *all* pairs satisfying (F1), (F2) and (A). The new Consequence (line 564) restricts this to candidates that 'differ only in which component carries which anchor.' For candidates with genuinely different decompositions (different wiring, different subnetworks cut from \(D\)), the 'must supply an admitted change' requirement is gone; the text now treats structural distinctness as sufficient for being different candidates. The declaration's phrase understates both the added claim (being different candidates) and the loss of the general distinguishing principle."

Its task (d) paragraph says R51 moves O24, O46, N17 and N25 toward the fixed verdicts, that "the declaration ('change of claim'; 'no longer says … are one account') accounts for this direction of movement, though the specific 'different candidates' characterization it omits (point 3) is what carries the verdicts." It proposes no repair for R51.

## 3. The texts

- **Quotations (S90 rule 8).** All found verbatim. The line numbers are off: the added paragraph is revised-text L560 (not 561–562) and the Consequence L562 (not 564); the brief itself gives R51 as L554–562, matching the committed draft. The old Consequence sentence is file 11 L558. "Such candidates" there does refer back to the old Claim's "Two candidates ... that both satisfy (F1), (F2), and (A) on \(C\)", so the reply is right that the old principle reached every such pair.

- **Half 1, "the added claim (being different candidates)", fails.**
  - "Different candidates" is not new. File 11's own Claim was about "Two candidates \(\mathcal E,\mathcal E'\)": it already took them to be two candidates, and said they were one *account*. A candidate is \((E,t,\Gamma)\) with \(\lambda\) in \(t\) (Part IV L189, Part V L231); two that anchor different subnetworks or cut \(D\) differently are different structures, hence different candidates, under both texts. The reply's "the text now treats structural distinctness as sufficient for being different candidates" confuses candidate with account: structural distinctness was always sufficient for that.
  - "With one answer profile" is (i), which the declaration states.
  - So L560's colon clause is file 11's Claim with its retracted half removed: it says what is left without the premise, which is exactly "nothing more follows". It does not say "not one account"; the entry's LOSS says that question is left undefined, and "nothing more follows" forbids reading it as derived.
  - What the paragraph points to is unchanged text: revised L23 (= file 11 L25) "Two systems with identical outputs and different internal routes are different organizations here, and the semantics says so (Derivation 9)"; L307 (= file 11 L309) "Two systems with the same output table may differ in which routes are active; the semantics represents the difference (Derivation 9)"; Derivation 9 L610; and for "A coarsening is not a recoding", Derivation 8 L606 (= file 11 L604) "The result does not apply to coarsenings, changed boundaries, or lost event identities." Nothing there is new to the text.
  - The reply's own task (d) concedes that the declaration's retraction ("no longer says … are one account") accounts for the direction of every move it names. The "different candidates" wording carries those verdicts only because the retracted "one account … pairwise of one kind" no longer blocks them, and that retraction is declared.

- **Half 2, "the loss of the general distinguishing principle", fails.** The declaration's last sentence states it: "Its Consequence now covers only candidates that differ in which component carries which anchor." The reply faults only the phrase "nothing more follows" and does not engage that sentence. It is true of the text: every pair the new Consequence covers (those that "differ only in which component carries which anchor", L562) differs in anchor assignment. The entry's LOSS records the same loss. The declaration omits the text's second "only", but "covers only" already bounds the reach. That is not an understatement a reader could act on, and it is not the reply's argument.

- **Where the lost principle still lives.** The component-level form stands unchanged: Part 0 objection 2 (L39 = file 11 L41), "components that no change at that level separates ... are one kind *at that level*", and (K) with W30.1 at L119. The account-level form stands for anchor assignments in the new Consequence. Its only other use, Derivation 10 L624 ("A claim that 'component 1 is *really* thing 1' is a claim that some admitted change distinguishes them"), is an anchor-assignment case and stays inside the narrowed scope. For differently decomposed candidates the old principle pulled against L23, L307 and Derivation 9, which the entry keeps. Losing it there is the intended repair (S88 F1, UPHELD), and it is declared.

- **Cases worked** (S81 book md5 4f488d14…, S89 book md5 b2e53577…).
  - **O24** ("They are two arrangements, and the record has not chosen between them. One reachable setting is enough."): holds AGREE. The old text reached the verdict through the old principle, with the reachable setting as the separating change. The new text reaches it without that principle: the arrangements are different organizations (L23), and the record's silence is Derivation 3 (L566, W17.3). If anything it moves toward, since the old "one account" could have merged two arrangements that agree on every tested pair. That move is carried by the declared retraction.
  - **O46** ("What survived is a new account with a cable in it"): holds AGREE, on firmer text. The spring and the cable anchor different subnetworks, so (ii) does not apply. L307's "a component reassigned to a new target after a deletion belongs to a new candidate with its own assessment" carries the verdict. The old slogan's "one account" was the risk, and the declaration retracts it.
  - **N17** (Q1 and Q2 "Yes; yes"): moves toward on the first two questions. A and B cut \(D\) at different places, and file 11's "one account … pairwise of one kind" pulled against each telling the asker something the other does not. The retraction is declared, and the reply agrees it is. Q3 is not reached.
  - **N25** (dog and turtle "different in words", "the difference between them is idle"): the only case where the lost general principle bears. "Idle" still rests on unchanged text. Nothing inside the universe can reach the holder, so no admitted change separates dog from turtle, and Part 0 L39 and (K) make them one kind at that level. Read as one anchor carried by different components, the new Consequence also covers them. The second question therefore stays AGREE on text the entry does not touch, and the watched away move does not happen. The reply claims a move toward on N25; the retraction is declared, so that move, if it happens, is declared too.
  - No case moves away, and no case moves in a way the declaration does not account for.

## 4. Ruling: KEEP

The argument fails on both halves.
1. The "added claim" is not an added claim. That the candidates are different candidates was already file 11's own premise ("Two candidates"). "One answer profile" is (i), which is declared. The paragraph's pointers restate unchanged text (L23, L307, Derivations 8 and 9). So L560 says exactly what the declaration says: without the premise, nothing more follows.
2. The declaration states the "lost principle" in its last sentence, and the entry's LOSS records it. The reply did not read that sentence against its point.

The entry stands as drafted: OLD, NEW, KIND (CLAIM) and DECLARATION unchanged. Under rule 3, the keep is recorded in the entry's CHECK field.

**Suggested CHECK-field line:** "After the cross-examination (S90, Mimo A2, point 3, R51 STANDS): the reply's claim that the declaration understates an added claim ('different candidates with one answer profile') and the loss of the old Consequence's general principle was re-examined and ruled KEEP. 'Different candidates' is file 11's own premise, 'one answer profile' is (i), the paragraph's pointers restate unchanged L23, L307 and Derivations 8–9, and the narrowing of the Consequence is stated in the declaration's last sentence and in LOSS."

**Conflicts.** A keep changes nothing, so it conflicts with no entry. Related entries this checker read and did not rule on:
- R55 (W19.3 + W10(b).1, L624), whose use of Derivation 2(ii) is this reply's point 2. It is for its own checker. It depends on (ii), not on L560 or the Consequence's scope, and it falls inside that scope.
- R08 (W19.1, L119), which defines the cross-candidate kinds that (ii) uses. It is unaffected.

**Not ruled (outside the argument):** the declaration's "differ in which component carries which anchor" could echo the text's "differ only in …". A strict reading gives the declaration a hair's breadth more reach than the text. The declaration stays true as written ("covers only"), so no fix is required. If the orchestrator wants the declaration verbatim to the text, the one-word change is "Its Consequence now covers only candidates that differ in nothing but which component carries which anchor." It touches no other entry.
