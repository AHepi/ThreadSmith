# Ruling: s90_xexam_mimo_A2, R26 (W24.1)

Checker: a fresh Claude checker, working from the rule in "S90 How the cross-examination of the revision 2 draft will be read - written before sending.md" as extended by "S90 Parts - how they will be read, written before sending.md". The call is complete (receipt and response committed in f0ae2f2). Id map (Parts note, line 95): R26 = W24.1, C22, part A2, file-11 line 351, file-13 line 349, WORDING, N20.

What is contested: an undeclared claim change the reply names outside its FALLS lines. The reply's own line is "R26: STANDS" (task b), and its point is conditional.

## 1. The entry and its checkers

Source: "Semantics/tests/Revision 2 - change list, draft of 23 September.md" lines 1102-1125. The file has not changed since 587eebf.

- STATUS applied; GROUP A; ITEM W24; FILE-11 LINE 351; WHERE Part VIII, "Functional transport" (L351), before sentence 1; REASON WORD erratum.
- **KIND:** WORDING
- **OLD:** `**Functional transport.** If \(\pi\circ S_a=T_a\circ\pi\) for every generator \(a\),`
- **NEW:** `**Functional transport.** Let \(S_a\) be a target process and \(T_a\) a represented process for each admitted generator \(a\). If \(\pi\circ S_a=T_a\circ\pi\) for every generator \(a\),`
- **DECLARATION:** none (WORDING: the typing follows from \(\pi:X_D\to X_E\) and from Part II's composition of admitted edits; listed in the record). If a checker rules CLAIM: "The functional transport result now says that \(S_a\) and \(T_a\) are target and represented processes for each admitted generator."
- **REASON:** W24 (trial A3 = Mimo M7, VALID). 00:518: "Suppose a target process \(S_a\) and a represented process \(T_a\) satisfy ... for every admitted generator \(a\)." 00's sentence is restored in file 11's "Let ... If ..." form, using 00's words for the typing.
- **Checkers:** check 1 found it SOUND. Its only note concerns W31: the \(S\) that W31 introduces must be named. There is no FIX history. The revision note (line 144) lists W24.1 among the undeclared entries whose ruling a checker may raise to CLAIM, with "expected WORDING". The worklist item W24 is titled "\(S_a\), \(T_a\) and 'generator' are undefined", and its handling is "Erratum: restore 00:518's sentence."
- CASES AT RISK: none. N20 is read on (T2), not here.

## 2. The reply's argument (response line 17, verbatim)

> **4. R26, task (b).** At line 349 the definition quantifies over "admitted generator \(a\)" while the commuting condition directly after quantifies over "generator \(a\)." If these are coextensive—as seems intended, since generators generate the admitted edits of \(A\)—then "admitted" is redundant and the claim is unchanged. If "admitted generator" is narrower than "generator," then \(S_a\) and \(T_a\) are defined only for a proper subset of the generators the condition ranges over, and the functional transport theorem is silently restricted. A WORDING change must not alter scope; the text does not settle which reading holds. The simplest fix is to make the two quantifiers match: either add "admitted" in the condition or drop it from the definition.

Line 21: "R26: STANDS".

## 3. The text

- Revised text (file 13 draft 2), line 349: the NEW as above, followed by "the same holds for every admitted finite composition with matching scopes. *Proof.* \(\pi S_bS_a=T_b\pi S_a=T_bT_a\pi\); induct. ∎"
- File 11, line 351: the OLD. The word "generator" has only one quantifier there.
- "generator" appears at no other line in either file 13 draft 2 or file 11. The only structure the text says is generated under composition is Part II's \(A\) (file 13 draft 2, line 91): "\(A\) is a set of admitted edits, closed under a partial associative composition with identity \(1\)." The theorem's conclusion ranges over "admitted finite composition", so the generators are generators of \(A\), and every element of \(A\) is admitted.
- The predecessor source, 00:518-524, reads: "Suppose a target process \(S_a\) and a represented process \(T_a\) satisfy \(\pi\circ S_a=T_a\circ\pi\) for every admitted generator \(a\). Then the same equality holds for every admitted finite composition, provided the intermediate scopes match." So the source has "admitted generator" in the condition itself. File 11's bare "generator" is a condensation of that phrase.
- Cases: the argument names none. No case in the S81 case book or the S89 case book (N1-N25) turns on generators or functional transport. N20 is read on (T2) at L361, which this entry does not touch.

Working the reply's condition:

- **The narrow reading does not arise.** There is no second, wider class of "generators" anywhere in the text. A generator that was not admitted would not be in \(A\), and then it would generate nothing that the conclusion ranges over. \(S_a\) and \(T_a\) are also meaningless for it. In file 11 they were never typed for any \(a\) at all. The two terms are coextensive. The typing sentence restricts nothing, so no undeclared change of scope occurs, and KIND stays WORDING. The conditional scope-change claim fails.
- **The mismatch is still real.** W24.1 created it. It put a second quantifier, worded differently, next to file 11's one quantifier. Two phrases in consecutive sentences invite exactly the question the reply raised. W24's own handling is to restore 00:518, whose condition says "admitted generator". W24 also says "generator" is undefined, and "admitted" is the word that ties it to Part II's \(A\). Leaving it off the condition does only half of that job.

## 4. RULING: FIX (wording only)

The reply's conditional claim of a scope change fails, because the terms are coextensive. The quantifier mismatch it points to is a real defect of this entry's NEW. The repair makes both quantifiers read as 00:518 does.

Corrected NEW:

````text
**Functional transport.** Let \(S_a\) be a target process and \(T_a\) a represented process for each admitted generator \(a\). If \(\pi\circ S_a=T_a\circ\pi\) for every admitted generator \(a\),
````

- KIND: WORDING (unchanged).
- DECLARATION: unchanged ("none (WORDING: ...)"). The CLAIM fallback line is unchanged and already says "for each admitted generator".
- REASON: add "The condition carries 00:518's 'admitted generator' as well, so the two quantifiers match (S90, Mimo A2, R26)."
- Record the edit as made after the cross-examination. It lands in file 13 draft 2, line 349, where "for every generator \(a\)" becomes "for every admitted generator \(a\)". The rest of the line is unchanged.

Why this direction, rather than dropping "admitted" from the typing sentence: it is 00:518's exact phrase, which the entry's REASON and W24's handling both name. It also completes W24's "generator is undefined" repair by tying the generators to \(A\). Dropping "admitted" instead would leave "generator" as unanchored as it was in file 11.

What is lost: nothing. The theorem's scope is the same under either quantifier.

Conflicts with other entries: none found.
- W31.1 (L361) refers only to "\(S_a\) and \(T_a\) ... in functional transport". It uses no generator quantifier and is unaffected.
- The revision note's line 144 ("W24.1 ... expected WORDING") and its table row R2-26 (WORDING, not declared) still hold.
- No case is at risk.
