# Ruling: s90_xexam_mimo_A2, R28 (W22.1)

*A fresh Claude checker, 23 September 2026, under the S90 rule as extended by "S90 Parts - how they will be read, written before sending.md" (rule 3). This checker did not draft, assemble or check the change list and did not write the part briefs. It read only the R28 point of the reply (its point 1, with the repair), its closing lines, and the receipt (finish "stop", END OF REPORT on the last line, so the call counts). Sources: change list as of 587eebf; revised text md5 9aecf2f30ce0b4523606b2b8409fdf37; file 11 md5 5e494c1095d920d128b9a79de378f923; reply md5 4ba1fdf27d0d4e2e0a3060707ddae40f. Map: part-rule table, "R28 | W22.1 | C23 | A2 | 373 | 371 | CLAIM | O27, O40, O50, N11".*

## 1. The entry and its checkers' verdict

W22.1, "Define \(p_\delta\) and \(\mathcal E_c\) in (K1)". Group A, item W22. Part IX, "Bearing", sentence 2; file-11 L373, revised-text L371. The display (K1) (file-11 L376, revised L374) is unchanged. REASON WORD: erratum. KIND: CLAIM.

- **OLD:** `Let \(p_\delta\) be the question about the defect. Then`
- **NEW:** `Let \(p_\delta\) be the question whether \(z\) has \(\delta\) in respect of \(p\), and \(\mathcal E_c\) the explanatory candidate (Part V) that the criticism offers for \(p_\delta\). Then`
- **DECLARATION:** "(K1) now defines its terms: \(p_\delta\) is the question whether the target has the alleged defect in respect of \(p\), and \(\mathcal E_c\) is the explanatory candidate the criticism offers for that question."
- **Checkers' verdict (CHECK):** check 1, FIX. The drafter had written file 00's term ("the criticism's interpreted structural account"). Check 1 found that a criticism can exist when (K1) fails, so that wording would call a failed candidate an account (against W36.1). It changed NEW to "the explanatory candidate (Part V) that the criticism offers for \(p_\delta\)". The list of what the checks changed records this (list L110).
- **Drafter's REASON:** trial M2 found \(\mathcal E_c\) used once and never defined, and found neither \(p\) nor \(z\) on the right of (K1). The drafter relied on 00:620: "\(\mathcal E_c\) is the criticism's interpreted structural account."
- **CASES AT RISK:** none found. The drafter checked N11, O27, O40 and O50.

## 2. The reply's argument (Mimo, part A2, point 1)

> At line 371 the new wording introduces \(\mathcal E_c\) as "the explanatory candidate (Part V) that the criticism offers for \(p_\delta\)." But the formal definition of criticism in the immediately preceding sentence—"A criticism has target \(z\), alleged defect \(\delta\), grounds \(g\), and a connection"—lists four relata, none of which is an explanatory candidate. The verb "offers" is not defined anywhere in the text as a relation between a criticism and a Part V structure \((E,t,\Gamma)\). Consequently \(\mathcal E_c\) has no determinate referent: the 4-tuple \((z,\delta,g,\text{connection})\) does not single out an organization, transport, and commitment set. (K1) cannot be evaluated, and the Bearing relation it defines is not well-defined. R29 compounds the problem: the relaxed criticism condition at line 377 ("an organization represents it as grounds for an alleged defect in a target") allows a criticism consisting of nothing more than identifying a signal as evidence—no explanatory structure need be attached—yet (K1) presupposes \(\mathcal E_c\) exists.
>
> The declaration states "(K1) now defines its terms." This is inaccurate: \(\mathcal E_c\) is described in terms of an undefined relation, not defined. The old text left \(\mathcal E_c\) wholly undefined, so R28 is directionally an improvement; but the declaration overstates what is achieved.
>
> *Repair.* Fold \(\mathcal E_c\) into the criticism definition so it becomes a relatum: "A criticism has target \(z\), alleged defect \(\delta\), grounds \(g\), a connection, and an explanatory candidate \(\mathcal E_c\) (Part V) for the question whether \(z\) has \(\delta\) in respect of \(p\). Write \(p_\delta\) for that question. Then…"

Closing line: "R28: FALLS — \(\mathcal E_c\) relies on an undefined "offers" relation; declaration's "defines its terms" is inaccurate". The same reply says "R29: STANDS".

**Quotations checked (rule 8).** All are found. The L371 phrase and the sentence listing the four relata are at revised L371. The W22.2 condition is at revised L377, where the reply places it. The declaration's words are in the change list at L1188.

## 3. The texts, and the cases

**Revised text, L371–377.** "A criticism has target \(z\), alleged defect \(\delta\), grounds \(g\), and a connection. Let \(p_\delta\) … Then (K1) … A criticism occurrence can exist when (K1) fails. An adverse signal is not a criticism until an organization represents it as grounds for an alleged defect in a target." File 11 (L373–379) is the same, except that it has the old sentence 2 and the old W22.2 sentence ("represents how it bears").

**"Offers" elsewhere.** The theory never defines "offers" as a relation. It does use the verb as its ordinary word for what a content puts forward. Part V's own definition of a candidate relies on it (L231: "those the candidate offers as doing the work"). So do L69 ("a false theory offered as an answer is an explanatory candidate"), L127 and L335. The theory also reads represented contents directly as Part V candidates elsewhere without saying how: (EK) at L443 has \(\operatorname{Account}(c,p_c)\) for a content \(c\). The charge that "offers" leaves (K1) impossible to evaluate is therefore too strong. The vocabulary of revised L371 is no less defined than Part V's own.

**Where the reply is right.** The Let-clause attaches \(\mathcal E_c\) to "the criticism" as a whole. The sentence just before it lists the criticism's parts, and the clause does not say which of them yields the candidate. The source did say. File 00:607 has "grounds \(g\), and a proposed connection from \(g\) to \(\delta\) relative to a question". File 00:620 makes \(\mathcal E_c\) "the criticism's interpreted structural account", which is that connection read as structure. W22.2's own REASON reads L373 the same way: a failing criticism "has an alleged connection, which L373 already lists among a criticism's parts". So the gap is real but small. It closes by naming the listed part that the candidate interprets, and "offers" is no longer needed. The declaration's "defines" over-claims for the drafted wording.

**The R29 point.** A criticism cannot lack a connection. L371 gives every criticism one, and W22.2 makes a signal a criticism only when it is represented "as grounds for an alleged defect in a target", which is to represent a connection from \(g\) to \(\delta\). A bare evidential connection, read as a candidate, has no nonempty block of commitments doing the work. Non-circular dependence (L255) asks for "a nonempty block \(G\subseteq\Gamma\)", so such a candidate fails (E), (K1)'s right side is false, and the criticism does not bear. "A criticism occurrence can exist when (K1) fails" (L377) already allows this. Once \(\mathcal E_c\) is tied to the connection, nothing is presupposed that might fail to exist.

**The reply's repair is not adopted.** (i) It makes a Part V candidate a fifth part of every criticism, beside the connection that the candidate interprets, and it widens OLD into sentence 1. That is a larger change of claim than the defect needs. (ii) It fixes the candidate "for the question whether \(z\) has \(\delta\) in respect of \(p\)" inside the account of what a criticism is, before \(p\) is bound, although \(p\) is an argument of \(\operatorname{Bearing}(c,z,p)\). (iii) It conflicts with W22.2 (R29), which the same reply says STANDS. A signal represented as grounds for an alleged defect would meet W22.2's condition and still not be a criticism if it carried no candidate. That brings back the very mismatch W22.2 was drafted to remove.

**Cases, worked on the fixed wording.**
- **N11 (S89):** holds. Jana's bare marks allege no defect and carry no connection, so they are not criticisms (W22.2), and (K1) is not reached. Each of Kasia's written faults ("a paragraph that repeats another") has a connection from its grounds (the two paragraphs' contents) to the defect in the draft. Read as a candidate, it bears or fails on the draft's text. The verdict ("both did", with the difference lying in Kasia's self-criticism) does not turn on how \(\mathcal E_c\) is typed.
- **O27, O40, O50 (S81):** hold. The robot's criticism of the test has this connection: the test's inference ran through the assumption that the pressure sensor read true, and that assumption misled it. Read as a candidate, that connection is the criticism's \(\mathcal E_c\). All three verdicts settle credit: whose reinterpretation it was, and the split across three achievements. None turns on (K1)'s terms.
- No other case in the S81 or S89 books turns on what \(\mathcal E_c\) is. The drafter's search stands.

## 4. Ruling: FIX

The argument partly fails. "Offers" is the theory's standing verb, and Part V's own definition uses it. The argument succeeds on two points. The drafted clause does not say which listed part of the criticism yields \(\mathcal E_c\), and the declaration's "defines" over-claims. The fix below ties \(\mathcal E_c\) to the listed connection and restores the source's "from \(g\) to \(\delta\)". It keeps check 1's point that a failing criticism's candidate is a candidate, not an account.

- **OLD:** unchanged: `Let \(p_\delta\) be the question about the defect. Then`
- **NEW:**
````text
Let \(p_\delta\) be the question whether \(z\) has \(\delta\) in respect of \(p\), and \(\mathcal E_c\) the criticism's connection from \(g\) to \(\delta\), interpreted as an explanatory candidate (Part V) for \(p_\delta\). Then
````
- **KIND:** CLAIM (unchanged). **REASON WORD:** erratum (unchanged).
- **DECLARATION:**
````text
(K1) now says what its terms are: \(p_\delta\) is the question whether the target has the alleged defect in respect of \(p\), and \(\mathcal E_c\) is the criticism's connection from its grounds to the alleged defect, interpreted as an explanatory candidate for that question.
````
- **For the CHECK field and the list of what the checks changed (after the cross-examination):** "S90, Mimo part A2, R28 FALLS; fresh checker FIX after the cross-examination: \(\mathcal E_c\) is 'the criticism's connection from \(g\) to \(\delta\), interpreted as an explanatory candidate (Part V) for \(p_\delta\)', not the candidate 'the criticism offers'; the declaration says 'says what its terms are', not 'defines its terms'."
- **What is lost:** the verb "offers" in this clause, and nothing else. What is gained: \(\mathcal E_c\) now interprets a part that every criticism has, so (K1) presupposes nothing that might fail to exist.

**Conflicts with other entries.** None found. W22.2 (R29) now agrees with this sentence: its "grounds for an alleged defect" is the connection from \(g\) to \(\delta\) that is read here as the candidate, and its REASON already calls L373's connection "an alleged connection". W36.1 (L69: "a false theory offered as an answer is an explanatory candidate") is untouched and consistent with calling a failing criticism's connection a candidate. No other entry has an OLD in L373 sentence 1 or in (K1). The (EK) use of \(\operatorname{Account}(c,p_c)\) and Part V's "offers" are not affected.
