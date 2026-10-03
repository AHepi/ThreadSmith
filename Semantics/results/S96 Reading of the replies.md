# S96: reading of the replies to the cross-examination of the repaired copy

*Written by agent 15 of the owner's 15 for this task (decision S24), the one fresh Claude reader named by the reading rule; it did not build, repair, read or test the repaired copy and did not write the briefs. Begun 26 September 2026, after decision S29 and after the S96 run was stopped (about 09:15 UTC). Read under `results/S96 How the cross-examination of the repaired copy will be read - written before sending.md` (the rule) and `results/S96 GLM 5.3 pilot - written before sending.md` (the pilot note). This file obeys decision S23 except where it quotes the owner or a reply. Filled as it goes (lesson S28).*

## 0. Declared departures from the rule

1. **Atria's part B is not waited for** (decision S29). The owner wrote "Nah get rid of Atria. Too slow", and Claude stopped the run at about 09:15 UTC with no reply of part B returned. Lines 373–632 therefore have Mimo's parts 3 and 4 as their only outside reading. The rule's point 1 (wait until every call has ended its last pass, or 36 hours) is not kept for part B; it is kept for the other five calls and for the pilot, all of which had returned.
2. **File name.** The rule's point 8 names the reader's file `results/S96 Reading of the cross-examination of the repaired copy.md`; the orchestrator named this one, `results/S96 Reading of the replies.md`. Nothing else differs: one file, every ruling with an id naming model, part and finding.
3. **The owner's words of S28** (26 September, after the briefs were sent) bound the rulings as well as S20 to S27: "A theory is never settled." and "That "ruling out" is a choice that was made." The replies did not see them.

## 1. Receipts

Every reply read here counts as returned under the rule (finish `stop`, END OF REPORT on the last line), and each `.response.txt` has the sha256 its receipt gives. Only the `.response.txt` files were opened; no reasoning file was read.

| tag | model | part, lines examined | attempts | seconds | finish | prompt / completion / reasoning tokens | response sha256 (first 12) | words |
|---|---|---|---|---|---|---|---|---|
| s96_xexam_atria_A | Atria-Dawn-Preview, medium | A, 1–372 | 1 (status 200) | 920.6 | stop | 19,796 / 53,488 / 50,231 | 3d75c22580a8 | 1,901 |
| s96_xexam_mimo_1 | mimo-v2.6-pro, medium | 1, 1–164 | 1 (200) | 1,109.9 | stop | 12,500 / 59,922 / 55,683 | 974c9781fc8f | 2,600 |
| s96_xexam_mimo_2 | mimo-v2.6-pro, medium | 2, 165–320 | 1 (200) | 1,411.7 | stop | 12,832 / 73,074 / 69,088 | 1eeb93a21ac8 | 2,246 |
| s96_xexam_mimo_3 | mimo-v2.6-pro, medium | 3, 321–484 | 1 (200) | 1,002.7 | stop | 13,670 / 53,128 / 48,948 | 2eaea5429f88 | 1,971 |
| s96_xexam_mimo_4 | mimo-v2.6-pro, medium | 4, 485–632 | 1 (200) | 1,398.0 | stop | 13,214 / 63,472 / 58,912 | 9068e9951e86 | 2,786 |
| s96_xexam_glm_A (pilot) | glm-5.3, high | A, 1–372 | 1 (200), 0 connection failures, 0 rejected | 474.7 | stop | 19,796 / 36,086 / 33,051 | e5eda63aac0d | 1,708 |
| s96_xexam_atria_B | Atria-Dawn-Preview, medium | B, 373–632 | pass 1: 6, each status 0 (no HTTP status) after 1,801.9–1,802.2 s | — | none | — | — | — |

**Atria's part B.** Pass 1 failed on the connection: all six attempts ended with no HTTP status, each at about 1,802 seconds, the thirty-minute cut of lesson S21; no answer from the model came back (error class: connection failure, not a model failure). Its error file was not read. Pass 2 (sent 07:58 UTC with a byte-identical request) was stopped with the run at about 09:15 (decision S29) and returned nothing. Lines 373–632 are examined by Mimo's parts 3 (to 484) and 4 only.

The text read against: `tests/Revision 2 - scrubbed copy, repaired (S96), theory text.md`, md5 8bb4d19d5aad53de2492b2193fd23ff1 (checked). The briefs have the md5s the rule gives (checked).

## 2. Verdict lines, per question and part

| reply | lines | Q1 | Q2 | Q2 targets | Q3 | Q4 | Q5 | Q6 | OVERALL |
|---|---|---|---|---|---|---|---|---|---|
| Atria A | 1–372 | NOTHING LEFT | KEPT OUT | ALL THREE | SAID | ALLOWED, AND NOT REQUIRED | BREAKS — L329–331, L325, L47/L201, L61/L339, L301–302, L231 | FAITHFUL | NEEDS REPAIR |
| GLM A (pilot) | 1–372 | LEFT — L53 | KEPT OUT | ALL THREE | SAID | ALLOWED, AND NOT REQUIRED | BREAKS — L233–L236, L329 | FAITHFUL | NEEDS REPAIR |
| Mimo 1 | 1–164 | LEFT — L49, L105 | KEPT OUT | ALL THREE | SAID | ALLOWED, AND NOT REQUIRED | BREAKS — L17, L31, L43, L61, L109, L119–120, L141, L151, L155, L159 | SAYS MORE — L15 | NEEDS REPAIR |
| Mimo 2 | 165–320 | NOTHING LEFT | KEPT OUT | ALL THREE | SAID | ALLOWED, AND NOT REQUIRED | BREAKS — L193–L211, L245, L255, L257, L287–L303, L305, L311 | SAYS MORE — L245, L317 | NEEDS REPAIR |
| Mimo 3 | 321–484 | NOTHING LEFT | KEPT OUT | ALL THREE | SAID | ALLOWED, AND NOT REQUIRED | BREAKS — L375, L377–L381, L387, L421–L422, L446–L453; L413–L417; L369; L455; L329; L339, L347 | FAITHFUL | NEEDS REPAIR |
| Mimo 4 | 485–632 | LEFT — L600 | KEPT OUT | ALL THREE | SAID | ALLOWED, AND NOT REQUIRED | BREAKS — L497–L506, L526, L536, L538, L540, L562–L564, L582, L588–L590, L596–L598, L610–L612, L626, L630 | SAYS MORE — L568, L608 | NEEDS REPAIR |

("KEPT OUT" is `KEPT OUT OF WHAT DEFINES EXPLANATION`; "ALL THREE" is `ALL THREE CAN BE TARGETS`.)

**Per question, in one line each.** Q1: three places were named, by three readers, each once (L53 by GLM, L49 and L105 by Mimo 1, L600 by Mimo 4); the other three found nothing left. Q2 and its targets: all six give the pass lines; no reply found physical possibility defining a question, its range, an account or a conflict, and all six name a piece of mathematics, a melody and a philosophical claim as possible targets; Mimo 1's L17 point bears on Q2 and is ruled below. Q3: all six say SAID. Q4: all six say ALLOWED, AND NOT REQUIRED. Q5: all six say BREAKS, 44 numbered findings between them, almost all on symbols, types, cross-references and the wording of definitions. Q6: three places say more than the owner's words (L15; L245 and L317; L568 and L608). No verdict line settles anything by itself (rule, point 2); each place is ruled in section 3.

## 3. Challenges and rulings

Every numbered finding, and every paragraph that names a fault whatever its verdict line says, in the order of the lines. Each: the id (model, part, finding), the place, the claim, what the reply proposed, the quotation check, the arguments, and the ruling with why this ruling and not another. The exact new wording of every FIX is the entry of the same id in `tests/S96 Repair - scripts/replacements_stage3.json`, printed in Appendix A by program; where the ruling's wording differs from the reply's, the reason is given here. Quotations were compared with the text by program and by eye: every quotation a challenge uses is found at the line it names, allowing for capital letters, the text's mathematical markup and the kind of quotation mark; the exceptions are named where they occur.

**L8, L315, L317, L369, L397, L606: the owner's words of S28.** Not a reply's challenge; see section 4.

**mimo 1 8, L15 (Q6).** Claim: "question-finding is at least half of creativity" (found at L15) is a proportion of something the semantics never measures, and no word of the owner's gives it. Proposed: "question-finding is part of creativity itself, not only the answering of questions". Atria, on the same line, called it "rhetoric the theory does not rest on" and let it stand. Ruling **FIX**. Why: the sentence gives a count (S20's words exclude grades and counts, and L25 says the semantics supplies no function that orders), and the sentence it serves needs only that question-finding belongs to creativity. That nothing depends on it, as Atria says, is a reason it can go, not a reason to keep it. The wording is simplified ("creativity includes finding questions, not only answering them") because the reply's reads as if question-finding were not answering.

**mimo 1 1, L17 (Q5, with Q2); joined with mimo 4 F3 (ii) at L538.** Claim: "rules out as a non-explanation" (found at L17 and L538) reads two ways: ruling the candidate out, as a non-explanation, or ruling out the claim that it is one; only the second makes the case that would rule the conjecture out work. "(iv) their physical realization" has no clear antecedent, and "a candidate that meets all four" makes physical realization a condition a candidate meets, against S25. Proposed: a rewrite of L17 whose (iv) says physical possibility enters "nowhere else" and whose necessity clause says the argument "shows the candidate to be an explanation". Ruling **FIX**, in a third wording. Why: the ambiguity is there (the scrub put "rules out as" where draft 5 had a positive status), and both halves of the conjecture turn on it. The reply's "nowhere else" says less than S27, where a claim about what is possible can be conflicted with, and "shows ... to be" brings back the shape S23 removes. The applied wording names the claim ruled out, gives (iv) its antecedent ("the instantiation and transformation of these contents in carriers (Part I)"), and writes "meets (E)" for "meets all four", which is what Part XV's sufficiency entry says. Marked as a change of claim.

**mimo 4 F1, L31, L520, L596 (Q5).** Claim: Argument 6's claim names the imports, indices and inputs as the only endpoints, while its reasons end also at "(O) and (Q), which depend on nothing" (found at L598 and L526). Proposed: add "the structural vocabulary of (O) and (Q)". Ruling **FIX**, at L596 and L520 as proposed and at L31, which carries the same sentence. Why: the claim and its reasons should name the same endpoints; (O) and (Q) are definitions, so the addition brings in no import.

**mimo 1 3, L31, L43, L155, L159, L257 (Q5).** Claim: "declared" has two senses: a contract is "a declared subset" (found at L43, L159, L257) and a declared index (L31), and "declared" is also one of three provenances ("A **declared** contract is stipulated by the modeller", found at L155), so a selected contract is both declared and not. Proposed: "stated subset" at L43, L159, L257, and at L31 calling the contract an index with a provenance of its own. Ruling **FIX**. Why: the clash is in the words, not the ideas, and "stated" is already the text's word for scope. L31 is left as it is, since Part XIV (L524) also calls the contract a declared index; instead L155 says which sense the provenance uses.

**atria A 3, L47 with L201 (Q5).** Claim: L47 says flatly that selection produces the object layer; L201 says this is "one arrangement, not a requirement" (both found). Proposed: a clause saying Part IV presents this as one possibility. Ruling **FIX**. Why: L35 promises that "the front matter states nothing the body does not state more exactly", and here it states more. The word "once" goes too, since selection enters elsewhere (contracts may be selected, L155; Arguments 3 and 4). No other reply raised it.

**mimo 1 7, L49, L105 (Q1); applied also at L277 and L343.** Claim: "A mathematical argument explains" (found at L49) uses "argument" for a candidate explanation, where Part 0 defines an argument as reasons why this and not that; L105 makes "mathematical arguments" port values. Proposed: "mathematical construction". Ruling **FIX**, with other words. Why: one defined word in two senses is a fault the scrub was meant to prevent; whether the second sense is "reasons for", as the reply says, is not needed for the ruling. "Construction" is itself a defined word (the provenance), so the applied wording is "a piece of mathematics" (L49, L277, L343) and "mathematical structures" (L105).

**glm A 3, L53 (Q1).** Claim: "fallible but testable in principle" (found at L53) is in-principle testability, the absolute sense S23 names, and it sits against L275, where a contrast no one could produce is still a contrast. Proposed: a longer sentence saying the semantics does not say a test can be carried out. Atria cleared the same words ("concerns a physical-history claim and denies absoluteness"). Ruling **FIX**. Why: read next to the next sentence, "A kind-label is not a claim about anything", "testable in principle" makes testability the mark of a claim, which is the verificationist criterion itself; Atria's point, that "fallible" denies finality, leaves that pairing untouched. The grievance's contrast needs only that selection is a physical claim. Applied: "fallible as any claim about it is (Part XII)". L481's "fallible and testable as any physical claim is" is in the physical module, where testing belongs (S25, S26), carries no "in principle" and no pairing with meaning, was cleared by Mimo 3, and is left. From the pilot only.

**atria A 4, L61, L339, L536–L544; joined with mimo 1 4.** Claim: Part XV's labels (A) to (E) are also the tags of question fidelity, the account relation and others (all found); "the four conditions of Account" are never four (Mimo). Proposed: (Suff), (Nec), (Elim), (Prov), (QF) (Atria); (P1)–(P5) (Mimo). Ruling **FIX** with Atria's labels. Why: "(A) Sufficiency. A candidate meeting all four conditions of (E)" uses one letter in two roles in one line. Mimo's (P…) would collide with the repair tag (P) and the object layer P. Mimo's "four" point is not taken up: the four are the four named conditions of L231 to L257 (component fidelity, question fidelity, non-circular dependence, non-vacuity); Mimo had not been given L231–257.

**mimo 1 6, L109 (Q5).** Claim: the observation role is defined through "the relation reporting it" under a heading that says no role is supplied. Proposed: a formula. Ruling **FIX** by a pointer, not the formula. Why: the reply's formula asks that the port's values stay unchanged, which is the reverse: an edit to a reporting relation changes the reading and leaves the thing reported. The fault is only that the role word is not tied to the signature it comes from (L124, L127); the pointer does that.

**mimo 1 9 (b), L119.** Four translations introduced, three glossed. Ruling **FIX** ("\(\pi\) translates valuations", as at L189).
**mimo 1 9 (a), L11, L15.** "(Part II, Argument 1)" read as placing Argument 1 in Part II. Ruling **KEEP**: two pointers; the Arguments are numbered once, in Part XVI.
**mimo 1 9 (c), L31.** "(EX)" taken for the account relation (E). Ruling **KEEP**: (EX) is the created-explanation relation (L450), a different thing; the reply had not been given L450.
**mimo 1 9 (d), L257.** "the active commitments" said to be used nowhere else. Ruling **KEEP**: defined at L231, which the reply had not been given.

**mimo 1 2, L15, L141–L155 (Q5).** Claim: question-finding is reduced to finding a contract, since \(\rho_p\) is the provenance of the contract only; a question's target and query are left out. Proposed: \(\rho_p\) over target, contract and query. Ruling **KEEP**. Why: by L151 two questions with one target and a different contract or query are different questions, and Argument 5's contract-content carries the query and admits edits that alter it (L588–L590); so constructing a contract is finding a question in the text's own sense. Extending provenance to the target would be a change of claim no reply showed to be needed; it is left for a later revision (section 7).

**mimo 1 5, L141, L151 (Q5).** Claim: of five respects, rule-status and purpose-achievement are given no query type or contract shape, and purpose-achievement needs the appraisal relation, which \(\mathcal Q\)'s domain leaves out. Ruling **FIX** by pointers only. Why: the two are worked elsewhere (constitutive rules, L347; achievement, (AR), L455), so a pointer is enough. The appraisal point is not taken up: (AR) defines achievement with no appraisal; \(\mathcal N\) enters only where aesthetic value is claimed (L455). The reply's added sentence with \(\mathcal N\) would therefore say more than the text.

**mimo 2 5, L193, L205 (Q5).** Claim: provenance is defined for transports "between organizations of a physical system", but (R) gives one to a transport from an occurrence's organization to a content; "admits a transport" uses the verb for edits; (R)'s \(\operatorname{Sel}(t)\), \(\operatorname{Con}(t)\) drop parameters silently. Ruling **FIX**, close to the reply's wording, the abbreviation written out as the forms "for some such parameters". Why: each is a gap between a definition and its use.

**mimo 2 4, L197, L211 (Q5).** Claim: "the content's transport to its target" (found at L211) runs against the definition: transports go from the target to the candidate (L183, L231); "the organization it targets" (L197) uses "target" for a codomain. Ruling **FIX** as proposed. Why: a reader can reverse \(t\) from these words, and the fix costs nothing.

**mimo 2 6 and atria A 6, L231, L257, L290, L302 (Q5).** Claim: a quadruple is called "The pair" (found at L231), and Account is applied with two arguments to \((E|W,p)\) and \((E_v,p)\) with no word on what that abbreviates or which transport goes with the restricted or edited organization; L257 says a contract "does not meet non-circular dependence", a condition on a candidate. GLM saw the same abbreviation and judged that it "held rather than broke". Ruling **FIX**, with one abbreviation sentence at L231 that covers both uses (Atria's and Mimo's proposals each covered one), and Mimo's wording at L257. Why: As GLM says, a reader can recover the sense, and that is exactly why one sentence recovering it costs nothing; (F1) needs \(\lambda\) and (F2) needs \(\pi\), and neither was said for \(E|W\) or \(E_v\).

**glm A 1, L233–L236, L556 (Q5).** Claim: in (F1), \(\operatorname{Sol}_{\lambda(k)}\) is over ports of \(D\) while \(V_k\) is a footprint of \(E\), so the projection onto \(V_k\) is undefined without the port translation that L119 names ("up to the port translation", found). Proposed: a translated projection \(\operatorname{proj}^{\lambda}_{V_k}\). Ruling **FIX**, applied also in Argument 1's reasons (L556), which uses the same projection. Why: the first conjunct of (E) should say what L119 and Argument 1's claim already say. From the pilot only; neither Atria nor Mimo 2 raised it.

**mimo 2 3, L245 (Q5, Q6).** Claim: "no component of \(E\) whose signature differs from its counterpart's meets (F1)" is unqualified, while (F1) and L281 are on \(C\). Ruling **FIX** ("signature on \(C\)"). Why: signatures are defined on a contract (K), so the claim was meant this way; the Q6 reading, that it says more than the owner, is not needed.

**mimo 2 1, L255 (Q5).** Claim: in non-circular dependence, "the answer profile at \((a,b)\) … or is not determined there in the claimed way" (found) leaves unclear whose answer and which "there"; on one reading it contradicts (A) and no candidate could meet (E). Proposed: a rewrite that sets the contrast between \(E\)'s answers at the two points and lets the difference in determination be at either point, plus a sentence on the two prohibitions. Ruling **FIX**, minimal: the applied wording names \(E\)'s answers and the point, and keeps the original direction. Why: the loss clause speaks of \(E\)'s answers at \((\tau(a),\sigma(b))\) and \((1,\sigma(b_0))\), and by (A) and \(\tau(1)=1\) the first disjunct is unchanged by naming \(E\). The contradiction the reply draws needs (A) to require that \(E\) "determine" its answer; (A) equates answers and says nothing of how they are determined, so it is not forced. The reply's widening to either point would change the claim with no argument given for the change.

**mimo 2 7, L305 (Q5).** Claim: singletons are equated with commitments, and "globally indispensable" is used before it is defined. Ruling **FIX** as proposed, adding "contributory" (used at L307) as the name of the first. Worked through: with \(\Gamma\) finite, \(\mathsf S\) upward closed and \(\Gamma\in\mathsf S\), \(d\) is critical for some route exactly when it lies in a minimal route, and \(\Gamma\setminus\{d\}\notin\mathsf S\) exactly when every minimal route contains \(d\); the text's reasons go through unchanged.

**mimo 2 8, L311.** The set-builder \(\{d_n:|x|\le 1/n\}\) has its condition on \(x\). Ruling **FIX** as proposed; worked through: every index set unbounded in \(\mathbb N\) forces \(x=0\), a bounded one does not, and removing one index from an unbounded set leaves it unbounded, so no route is minimal.

**mimo 2 2, L317 (Q6, with Q5).** Claim: "a **test** that solves the problem for that assessor whatever it records, so long as the premises about the test's background and instruments are live" (found) states an outcome on a condition that does not give it: usability (K2) asks admitted forms and a declared scope as well as live premises; and stating what a test does for a person runs against S21 ("Notice I never once claimed what must happen."). Ruling **FIX**, with the owner's S28 applied in the same place. Why: the reply's argument goes through on the text's own (K2). The applied wording names all three parts of usability and says that taking the test's premises as given, and the ruling out that uses them, is the assessor's choice, which the test does not make by itself (S28, section 4).

**mimo 2 remarks under Q5.** "(Part VIII)" at L317 for the persistence of a ruling out: **KEEP**; L369, in Part VIII, states it. The bracket "(S95, hard case 1)": replaced under S28 (section 4).

**atria A 5, L299–L302 (Q5).** Claim: in (D), \(v\) and \(w\) are organization edits and \(\mathcal V\) is one letter from the port set \(V\). Proposed: \(\mathcal A\), \(e_1\), \(e_2\). Ruling **KEEP**. Why: the display binds its letters in the sentence before it ("For a declared family \(\mathcal V\) of organization edits"), so no reader can take \(v\) there for a port, and the proposed \(\mathcal A\) is one letter from the edit set \(A\), the same distance as before. Nothing breaks.

**atria A 2, L325 (Q5).** Claim: \(U_H\), \(U_\theta\) are used only here and defined nowhere. Proposed: drop them and name the ports. Ruling **FIX**, with a gloss instead. Why: the stipulation gives each of \(H\) and \(\theta\) a component that sets it, which the next sentences intervene on and replace; naming the ports alone would lose those components. The gloss says what \(U_H\), \(U_\theta\) and \(L\) are.

**atria A 1, glm A 2, mimo 3 5, L329–L331 (Q5).** Claims: (a) \(A\) is the matrix of a linear measurement here and the set of admitted edits everywhere else (L91, L325, found); (b) the tags run (I1), (I2), (I4); (c) \(x\), \(b_A\), \(b_B\) are never introduced, and the kernel claim goes through only in the order \((x,b_A,b_B)\). GLM adds that the likeliest cause of (b) is a sentence removed by the scrub or the repair, so that the dated note's claim to list every change would say more than was done. Ruling **FIX** on (a), (b) and (c): "\(\ker g\)" for linear \(g\); (I4) renamed (I3), which no line cites; the unknowns named in order. GLM's account of the cause is **not taken up**: the same (I1), (I2), (I4) stand in draft 5 and in file 10, and the predecessor of file 10 had an (I3), an approximate-identification bound not carried into file 10; the gap predates the scrub. The kernel claim, worked through: the rows \((1,1,0)\) and \((1,0,1)\) have kernel spanned by \((1,-1,-1)\); \(b_B-b_A\) is constant on it and \(x\) is not.

**mimo 3 6, L339, L347 (Q5).** Claim: the bare tags "(O)" and "(K)" name nothing, and collide with (O1) and (K1)–(K3). Ruling **FIX at L339, KEEP at L347**. Why: both tags are printed, (O) at L100 and (K) at L116, which the reply had not been given, so its argument fails. But at L339 "full by (O)" points to another place: that a deleted component's relation is full is said at L103, beside (O), not by it; so "full (Part II)". At L347 "Its signature under (K)" points to the definition of signatures and stays.

**atria A 4 at L339.** Applied with the labels (above).

**mimo 3 3, L369 (Q5).** Claim: "no candidate becomes an account by that (K2)" cites the usability rule where the account relation is meant. Ruling **FIX** as proposed ((K2) after "not usable", (E) at the end). Why: the lapse is (K2)'s and becoming an account is (E)'s; the fix makes each citation name what it bears on.

**Lines 373–484 (Mimo 3 only; Atria's part B never returned).**

**mimo 3 1, L375, L377–L381, L387, L421–L422, L446–L453 (Q5).** Claims: (K1) and (EX) use Account with two arguments, and (EX) with a content \(c\) whose transport and commitments are never given; \(\xi,\xi'\) and \(U_c\) are free in (EX); \(\preceq_h\) is never defined; (G) leaves its arguments off; "essential premises" is never said. Ruling **FIX** on each. Why: each is a gap between a definition and its use, and every proposed repair adds no claim, except one point: the reply binds \(U_c\) existentially in (EX) while glossing it as the use task the aim declares, which disagree; the applied wording leaves \(U_c\) free and glosses it as "the declared use task for \(c\) (Deploy, Part X)", Deploy's declared \(U\), which is also how Part XIII uses \(U_c\).

**mimo 3 2, L413 (Q5).** Claim: \(\equiv_\ell\) is called an equivalence and is not given as transitive. Ruling **FIX**, in a third wording. Why: the relation is defined on \(c\)'s contract, so it is not even symmetric in general (the reply calls it symmetric); (N) uses it only with \(c\) fixed. The applied wording drops "equivalence" and says how (N) uses it, without the reply's added claim of transitivity under matching scopes.

**mimo 3 4, L455 (Q5).** \(\mathsf{Rsn}\) and \(\mathcal V_A\) unglossed; \(A\), \(K\), \(F\) reused. (The text prints the reasons set as \(\mathcal Rsn\); the reply wrote it \(\mathsf{Rsn}\), a difference of markup only.) Ruling **FIX** as proposed.

**Lines 485–632 (Mimo 4 only).**

**mimo 4 F5, L491–L506 (Q5).** Claim: (U1)–(U3) and (RC) use \(U_c\), \(A_p\), \(\operatorname{Can}\), \(\operatorname{CanAdv}\), \(J_p\), \(C_I\), "admitted target chains" and "an owned enabling continuation" with no definition here; \(\operatorname{Enable}\) is circular; \(\xi_0\) is free in (U3). Ruling **FIX in part**. Taken up: glosses and pointers (\(\operatorname{Can}\), \(\operatorname{CanAdv}\), \(J_p\), \(C_I\) are defined in Part XII, L475 and L477, not in Part X as the reply says; \(U_c\) as at L453; \(A_p\) as the task for \(p\) that \(\operatorname{CanAdv}\) describes); \(\xi_0\) bound in (U3); "enabling condition" pointed to (CT1), where \(\chi\) is a parameter, which answers the circularity. Not applied: "admitted target chain" and "owned enabling continuation" are defined nowhere, and the reply's pointer is not borne out; a definition would add a claim, and none is proposed that the text can bear (section 7). \(M\models\operatorname{UU}\) is kept: UU is defined as a formula.

**mimo 4 F10, L526.** The well-foundedness sentence has four referents for "it". Ruling **FIX**, the reply's split with "the result it is defined through" kept, which the reply's wording lost.

**mimo 4 F3, L536, L538 (Q5).** (i) "with a non-declared transport" named as vacuous, a transport never being a declared input. (ii) "rules out as a non-explanation" reads both ways (with mimo 1 1). Ruling **FIX** on both, (i) on another argument: "non-declared" is the provenance of L199 (\(\operatorname{Dec}(t)\)), not a declared input, so it is not vacuous; but with two senses of "declared" in the text (mimo 1 3) it is ambiguous, and it now reads "a transport whose provenance is not declared (Part IV)".

**mimo 4 F9, L540, L562–L564 (Q5).** (i) A kind-label doing explanatory work would rule out Argument 1's Consequence (that "kind" is eliminable), not its Claim about signatures. (ii) The argument's reasons compose one port translation with "the inverse of the other" while the premise asks only translations "onto the same ports". Ruling **FIX** on both; (ii) narrows the premise and is marked a change of claim.

**mimo 4 F2, L568 (Q6).** Claim: "must supply it. The remedy is a finer contract" prescribes, against S21. Ruling **FIX in part**. "The remedy is …" names what is to happen and goes; it now says that a finer contract is a new question and whether anyone asks it is that person's choice. "must supply it" is **kept**: it is a condition on what a claim is (a claim that a change separates two pairings names one), of the same form as L317's "A criticism that a candidate is easy to vary must supply such a rival", and says nothing about what a person must do. The reply's longer wording about missing inputs is not needed for the point.

**mimo 4 F4, L580–L582, L622–L624 (Q5).** Claim: Argument 4 assumes occurring changes lie in \(C\), so its claim fails for violations outside \(C\); and the example cites Argument 4 without stating \(S_0\)'s contract. Ruling **FIX**, on the second argument and a narrower reading of the first. The claim does not fail: Part IV defines prediction, violation and surprise only "For an edit–boundary pair \((a,b)\in C\) actually occurring" (found at L217, which the reply had not been given). The argument's reasons now say so, and the example states \(C_0\) with the occlusion in \(C_0\setminus H_0\).

**mimo 4 F7, L588–L590 (Q5).** Claim: Argument 5's claim says a contract "is an organization", while its reasons build one; "closure conditions" is undefined; what (O) asks of components is not supplied. Ruling **FIX in part**: the claim now says a contract "can be given the structure of an organization in the sense of (O)", and the reasons give each component its relation, as (O) asks. Marked a change of claim (the claim now says what its reasons give). "Closure conditions" stays undefined; the reply's gloss is its own guess (section 7).

**mimo 4 F8, L612 (Q5).** Argument 8 omits the declared inputs that (P) and (EX) depend on (L526). Ruling **FIX** as proposed, less "weights"; marked a change of claim (the transported data widened).

**mimo 4 F11, L600 (Q1).** "a theory of reasons" reads as reasons for or against, where the import is the appraisal relation. Ruling **FIX** ("a theory of appraisal"), the name L31 and L518 use.

**mimo 4 F12, L608 (Q6).** Claim: "a failure of the record" makes a record do the work S20 gives to the explanation ("A record is redundant."). Ruling **FIX**, the reply's first sentence. Why: the argument before it already puts the two claims at different indices whatever is written down; the index does the work. The reply's last sentence, on a log kept beside the history, adds a claim and is not used.

**mimo 4 F6, L626, L630 (Q5).** (i) "They are objects because they respond as objects do" brings back a kind-label and is circular. Ruling **FIX** as proposed. (ii) "distinguishes them" means the pairings, and the next sentence's "separates the two things" means the things. Ruling **FIX** in part: "them" is named as the two pairings; the reply's rewrite of the last sentence is not taken up, since "identity, at this grain, is exhausted by trajectory" is consistent with the swap being invisible at this grain and is the point the example makes.

**atria A, paragraph under Q5, L195.** "No member of the history represents \(t\), \(H\), or the survival condition": members of \(H\) are pairs. Atria says it breaks nothing. **KEEP**: the sentence says that nothing in the history represents the target, which is what separates selection from construction; that pairs cannot represent anything makes it trivially so, not false.

**mimo 3, paragraph under Q6, L369's header.** "A failed answer stays failed" "reads like a verdict". Not a challenge (the reply says the text does not force that reading); taken up under S28 in section 4.

### Count

53 rulings: **45 FIX, 8 KEEP, 0 DROP**. By reply: Atria A 5 FIX, 1 KEEP; GLM A 3 FIX (one joined with Atria's and Mimo's); Mimo 1 8 FIX, 4 KEEP; Mimo 2 8 FIX; Mimo 3 6 FIX, 1 KEEP; Mimo 4 15 FIX; two paragraph points KEEP. Within the FIXes, five arguments were not taken up although the place was changed for other reasons (GLM's account of the missing (I3); Mimo 1's appraisal point at L151; Mimo 1's formula at L109; Mimo 4's "vacuous" at L536; Mimo 4's failing claim at L582), and three parts were not applied (RC's two terms; "closure conditions"; the rest of mimo 4 F6 (ii)).

## 4. The owner's words of S28, applied

No reply saw S28; the orchestrator asked that both points go in whether or not a reader raised them.

**(i) "A theory is never settled."** Wherever the text said that whether a candidate meets the requirements is fixed, or used a word that reads as final, it now says that this depends on the thing explained and not on anyone's view of it, and that nothing about it is settled; any acceptance is tentative. Changed: L8 (one sentence in Part 0, where the two words are defined, quoting the owner); L317 ("is fixed by the candidate, the question and its target" becomes "depends on …, and not on anyone's view of them", with "nothing about it is ever settled, and whatever anyone accepts about it, that a candidate is an account or that it is not, is accepted tentatively"; the bracket marking the owner's open question, hard case 1, is replaced by the owner's words of S28); L315 (whether two candidates conflict "depends on", not "is fixed by"); L369 ("the failure on \(p\) stands" becomes "it leaves the failure on \(p\) as it was"); L606 ("is fixed at that index" becomes "is a claim at that index"). Considered and left: "is fixed by (E)" (L497), "is fixed by the type of \(\mathcal Q\)" (L151), "is fixed by its contract" (L277), "is fixed by that signature" (L127), "fixed by its population" (L315) and "the population fixes it" (L574), each of which says what a definition makes something depend on, not that anyone's view is final; and the header "A failed answer stays failed" (L369), which is S20's "the mistake shouldn't be able to creep back in", whose body makes every ruling out last only while its argument is usable, and whose world-level sentence (by (A), a candidate with a failed answer is not an account) now falls under L8's "nothing is settled" (see section 6, question 3).

**(ii) "That "ruling out" is a choice that was made."** Wherever a claim taken as given rules out a rival for a person, the text now says that this ruling out is a choice the person made, not something the claim does by itself. Changed: L8 (Part 0); L315 (conflict with a claim: "Nor is the conflict enough to do anything about it (S27): ruling the candidate out by \(\chi\) is already doing something about it, and is a choice the person made in taking \(\chi\) as given, not something \(\chi\) does by itself (S28)"); L317 twice (the test, with mimo 2 2: taking the test's premises as given is the assessor's choice, and so is the ruling out that uses them; and the problem solved with no test: the sentence "it is not a response to the conflict with the claim" is reversed, since the owner answered "Also, yes." to whether such a ruling out is already doing something about it); L397 (Part IX: where an argument with no record leaf uses a claim taken as given, the ruling out is the person's choice). The S27 words, that the bare claim "is not enough for a creative agent to do anything about it", are kept beside the S28 words: the claim alone does nothing; a person taking it as given and ruling a candidate out has done something, by choice.

## 5. Points that dispute a fixed case verdict

None. No brief carried the case book, and no reply named a case or a case verdict.

## 6. Findings that are the owner's choice (set out, not settled)

1. **Whether the S28 rendering is what the owner means.** The owner twice wrote "unless you mean something else". The text now says that whether a candidate is an account depends on the candidate, the question and the thing explained, not on anyone's view of them, and that nothing about it is ever settled. Claude's reading is that this keeps the relation hard case 1 asked about, with finality taken out, as the owner's "1. That is correct." says. If the owner meant that the relation itself should go, Part VI's test and the world level of "A failed answer stays failed" would have to be rebuilt (S95's condition).
2. **How far "ruling out is a choice" reaches.** The owner said it of ruling out a rival by a claim taken as given. Every argument's premises are tentatively accepted and its forms admitted, each a person's choice (Part 0), so on Claude's reading every ruling out is a choice the person made. The text applies it only where a claim taken as given is used (including a test's background and instruments); whether it is to be said of every ruling out is the owner's.
3. **"A failed answer stays failed" next to "A theory is never settled."** Kept; Claude reads the two as going together (the failure depends on the thing explained; anyone's acceptance of it is tentative). The owner may read the header as the finality S28 removes.
4. **S27 and S28 together.** The text keeps S27's "the conflict is not enough to do anything about it" and adds S28's "ruling out … is already doing something about it". Claude reads them as one position (the bare claim does nothing; a person's choice to rule out by it does something). If the owner meant otherwise, L315 and L317 change again.
5. **Unchanged from before:** the provisional names ("surprise", "understanding", "recognized difficulty", "created explanation"); S95's questions on "knowledge" and worth; S94's and S93's questions. This reading settles none of them.

## 7. Not ruled, or left for a later revision

- (RC)'s "admitted target chain" and "owned enabling continuation" (L492), and Argument 5's "closure conditions" (L590), are defined nowhere; a definition would add a claim.
- Extending question provenance to the target (mimo 1 2): a possible change of claim, not needed on the text's own identity of questions.
- Lines 373–632 have one outside reader (Mimo); lines 1–372 have three (Atria, GLM, Mimo). Silence is not agreement (rule, point 2).
- No reader, inside or outside, has read stage 3.

## 8. GLM 5.3 against Atria and Mimo, on part A (the pilot)

**What was compared.** GLM's one reply on lines 1–372 against Atria's part A on the same lines, and against Mimo's parts 1 and 2 (lines 1–320) with Mimo's part 3 on lines 321–372 only (the pilot note's section "Declared addition", point 3).

**Findings GLM made that the others did not.** Two of GLM's three: (F1)'s projection needs the port translation (glm A 1, FIX, also applied to Argument 1's reasons), and "testable in principle" at L53 (glm A 3, FIX; Atria had looked at the same words and cleared them). Both were taken up, and both are marked as from the pilot only.

**Findings both made.** The missing (I3) at L329 (GLM, Atria, and Mimo 3). GLM's account of its cause was not borne out (section 3).

**Findings the others made and GLM did not, on lines 1–372.** Atria: the double use of \(A\) and the unnamed unknowns at L329–331, \(U_H\) at L325, L47 against L201, the Part XV labels, and (with Mimo 2) the two-argument Account, which GLM saw and judged not to break. Mimo 1: L17's conjecture, "declared" in two senses, the labels, the observation role, "mathematical argument", "at least half of creativity", L151, L119. Mimo 2: non-circular dependence at L255, the test sentence at L317, L245, the direction of transport at L197 and L211, the scope of provenance and (R) at L193 and L205, L305, L311, L257. Mimo 3 on 321–372: L369's citations, L339. Every one of these was taken up as a FIX (section 3).

**Did GLM challenge anything?** Yes: three findings, each with a proposed wording, and two verdict lines other than the pass lines (Q1 and Q5). It did not behave like DeepSeek in S83 (lesson recorded then: matched the others' verdicts and chose to report no holes). It also said, of an abbreviation it saw, that it "held rather than broke", where Atria and Mimo asked for a repair.

**Verdict lines** (section 2): GLM's differ from Atria's on Q1 (LEFT — L53 against NOTHING LEFT) and in the places under Q5; from Mimo 1 on Q1's places and on Q6 (FAITHFUL against SAYS MORE — L15); from Mimo 2 on Q1 and on Q6 (FAITHFUL against SAYS MORE — L245, L317). All three give OVERALL: NEEDS REPAIR.

**Time, attempts, tokens.**

| | GLM A (pilot) | Atria A | Mimo 1 + 2 (lines 1–320) |
|---|---|---|---|
| effort | high | medium | medium |
| attempts / connection failures / rejected answers | 1 / 0 / 0 | 1 / 0 / 0 | 1 each / 0 / 0 |
| seconds | 474.7 | 920.6 | 1,109.9 + 1,411.7 |
| prompt tokens | 19,796 | 19,796 | 12,500 + 12,832 |
| completion (reasoning) tokens | 36,086 (33,051) | 53,488 (50,231) | 59,922 (55,683) + 73,074 (69,088) |
| reply words | 1,708 | 1,901 | 2,600 + 2,246 |
| findings / taken up, in whole or part | 3 / 3 | 6 / 5 | 17 / 16 |
| taken up that no other reply on these lines made | 2 | 3 (\(A\) and the unknowns at L329–331; \(U_H\); L47) | 14 |

**What one call can and cannot tell.** From it: GLM 5.3, at high effort, through the Coding Plan endpoint and the project's own script, returned a full-size cross-examination (13,571 words in) in under eight minutes on its first attempt, inside a 65,536-token cap, with findings and wordings, two of which were taken up that neither other reader on these lines made. It does not tell: how GLM does at medium (the owner's rule; Z.ai takes "medium", effect unknown); how it does through Claude Code, the supported tool, which is how any further call goes (decision S29); how often its calls fail over many calls, or at larger sizes; whether its misses overlap Mimo's (one part is one sample, and Mimo's two blind readings of one text in S81 differed on 36 of 52 rows); or anything about Atria's part B, which never came back. It was also a comparison on unequal terms: GLM ran at high effort, the others at medium, and GLM read once what Mimo read in two smaller parts. Counts of findings are not a measure of anything by themselves; each finding was ruled on its argument.

## 9. Stage 3 as applied

- **Program.** `tests/S96 Repair - scripts/repair_apply.py --stage3` rebuilds stage 1 (md5 c1eecbd1587e5aec91fd0ba7d46e1469) and stage 2 in memory, refuses unless stage 2 has md5 8bb4d19d5aad53de2492b2193fd23ff1 (the S96 final, which it does not write), applies `replacements_stage3.json` (made by `replacements_stage3_source.py`, with `replacements_stage3_extra.json` for the notes) under the same span rules, and writes only the new file.
- **Entries.** 85 applied: 74 from the replies' challenges (X), 8 from S28 (O), 3 to the dated note (N); 11 change a claim (L8, L15, L17, L315, L317 three times, L397, L562, L588, L612); 72 lines differ from the S96 final; 632 lines, line for line; words 15,979 to 16,839 (`split`).
- **The new text.** `tests/Revision 2 - scrubbed copy, repaired (S96), after cross-examination, theory text.md`, md5 ebca15a047f686b15d5f5766b69825c9. The S96 final is unchanged (md5 8bb4d19d5aad53de2492b2193fd23ff1, checked before and after). Draft 5, the scrubbed copy and the change list are not touched.
- **S95 residue scan** on the new text: 82 hits, 82 noted with a reason, 0 unexplained (S96 final: 71, 71, 0). The 11 new hits are "settled" (4, each a denial of settling or the owner's words), "accepts"/"accepted" (6, each tentative) and "correct" (1, quoting the owner). Four notes from earlier stages are stale (l. 75, 315 and 526 "adopted", l. 461 "permitted"), as they were in the S96 final.
- **S96 physical scan** on the new text: 201 physical-tie words on 81 lines (S96 final: 195 on 80), each line with a reason; two new reasons (l. 47, "one possibility", the ordinary sense; l. 453, Deploy's use task); one reason now stale (l. 626, where the word left the line with mimo 4 F6).
- **Not applied, with reasons:** the 8 KEEPs; the parts of FIX rulings not taken up (section 3, "Count"); the S28 places considered and left (section 4). Each is listed in the JSON's `not_applied`.

## 10. What this reading is and is not

One Claude reader ruled every challenge; no second reader has seen the rulings or stage 3, and no outside reader has seen stage 3. Lines 373–632 had one outside reader. The rulings weigh arguments, not the number of replies. The new text is an experiment on a copy, as the S96 text was; draft 5 stays the current draft.

## Appendix A. Stage 3 entries as applied (printed from `replacements_stage3.json`)

Each: line; ruling id; group; whether it changes a claim; the old span; the new span; the reason. Spans are the text's own markup.

**A1. l. 2, note, N.** The note names the log entries and decisions the text now answers to.

```
OLD: (log S96, on decisions S23 to S27)
NEW: (logs S96 and S97, on decisions S23 to S28)
```

**A2. l. 2, note, N.** The note says how the text was made; it now names the third stage and where its rulings are.

```
OLD: made by program (`tests/S96 Repair - scripts/repair_apply.py`, from `replacements.json` and `replacements_stage2.json` beside it),
NEW: made by program (`tests/S96 Repair - scripts/repair_apply.py`, from `replacements.json` and `replacements_stage2.json` beside it), and a third stage after the outside cross-examination and the owner's words of 26 September (decision S28), from `replacements_stage3.json` (rulings in `results/S96 Reading of the replies.md`),
```

**A3. l. 2, note, N.** The plan covers stages 1 and 2 only.

```
OLD: Every change, with its reason, is in `tests/S96 Repair of the scrubbed copy - plan.md`.
NEW: Every change of the first two stages, with its reason, is in `tests/S96 Repair of the scrubbed copy - plan.md`, and of the third in the reading of the replies.
```

**A4. l. 8, S28 (i), S28 (ii), O, changes a claim.** Decision S28, both points, stated once where the two words are defined; the owner's words quoted verbatim.

```
OLD: A premise of an argument can be a claim tentatively accepted as given, and an argument need not cite a test (Part IX).
NEW: A premise of an argument can be a claim tentatively accepted as given, and an argument need not cite a test (Part IX). Nothing in the semantics is settled: whether a candidate meets the conditions of an account depends on the candidate, its question and its target, not on anyone's view of them, and whatever anyone accepts about it is accepted tentatively (Part VI); in the owner's words, "A theory is never settled." Where a claim taken as given is used to rule out a rival, that ruling out is a choice the person made, not something the claim does by itself; in the owner's words, "That "ruling out" is a choice that was made."
```

**A5. l. 315, S28 (i), O.** S28 (i): no wording implying finality; 'depends on ... not on anyone's view' is the owner's point applied to conflict, next to the relation it pairs with.

```
OLD: Whether two candidates conflict is fixed by their organizations and transports and by the target's ports and components;
NEW: Whether two candidates conflict depends on their organizations and transports and on the target's ports and components, not on anyone's view of them;
```

**A6. l. 315, S28 (ii), O, changes a claim.** S28 (ii): 'Also, yes. That "ruling out" is a choice that was made.' The bare claim is still not enough (S27); the ruling out that uses it is the person's choice.

```
OLD: Nor is the conflict enough to do anything about it: a response that changes the candidate, the claim or the question is construction and repair (Parts X, XI), and \(\chi\) alone does not say where the candidate is in error.
NEW: Nor is the conflict enough to do anything about it (S27): ruling the candidate out by \(\chi\) is already doing something about it, and is a choice the person made in taking \(\chi\) as given, not something \(\chi\) does by itself (S28); a response that changes the candidate, the claim or the question is construction and repair (Parts X, XI); and \(\chi\) alone does not say where the candidate is in error.
```

**A7. l. 317, S28 (ii), O, changes a claim.** S28 (ii) reverses 'it is not a response to the conflict with the claim': the owner answered 'Also, yes.' 'While the argument stays usable' covers the circular case too, which has no claim.

```
OLD: Solving a problem so rules one rival out for that assessor while the claim stays live for that assessor; it is not a response to the conflict with the claim, which does not say where the rival is in error, and what the person goes on with stays the person's choice (conflict with a claim, above).
NEW: Solving a problem so rules one rival out for that assessor while the argument stays usable for that assessor. Where the argument uses a claim the assessor tentatively accepts, that ruling out is a choice the assessor made, in taking the claim as given and going on with it, and not something the claim does by itself; it is already something done about the conflict with the claim, which does not say where the rival is in error, and what the person goes on with stays the person's choice (conflict with a claim, above).
```

**A8. l. 317, mimo 2 2; S28 (ii), X, changes a claim.** Live premises alone do not make an argument usable (K2 asks forms and scope as well), and 'solves the problem whatever it records' stated an outcome (S21); the ruling out is the assessor's choice (S28).

```
OLD: is a **test** that solves the problem for that assessor whatever it records, so long as the premises about the test's background and instruments are live for that assessor (K2, K3): an argument from what it records then rules out at least one of them for that assessor, while it stays usable;
NEW: is a **test**. Whatever it records, an argument from what it records rules out at least one of them for an assessor who can use it, that is, for whom its steps' forms are admitted, its scope is the one declared and its premises about the test's background and instruments are live (K2, K3), while it stays usable; taking those premises as given is that assessor's choice, and so is the ruling out that uses them, which the test does not make by itself (Part 0);
```

**A9. l. 317, S28 (i), O, changes a claim.** S28 (i): 'fixed by' read as final; the owner's answer to hard case 1 replaces the open-question bracket.

```
OLD: whether a candidate is an account of a question is fixed by the candidate, the question and its target, not by when anyone first asks the question or by whether anyone has tested the candidate on it (Parts I and V) [whether this relation, which names no assessor, stays in the theory is the owner's open question (S95, hard case 1)].
NEW: whether a candidate is an account of a question depends on the candidate, the question and its target, and not on anyone's view of them, on when anyone first asks the question or on whether anyone has tested the candidate on it (Parts I and V); nothing about it is ever settled, and whatever anyone accepts about it, that a candidate is an account or that it is not, is accepted tentatively (Part 0) [the owner's words of 26 September (S28): "A theory is never settled."; the owner called "correct" the reading that the thing explained is however it is and that everything anyone accepts about it stays tentative].
```

**A10. l. 397, S28 (ii), O, changes a claim.** S28 (ii), where Part IX says an argument with no record leaf rules a candidate out.

```
OLD: is read from the owner's definition of argument (S23)].
NEW: is read from the owner's definition of argument (S23)]. Where such an argument uses a claim taken as given, the ruling out is a choice the person using it made, not something the claim does by itself (Part 0; the owner's words, S28).
```

**A11. l. 369, S28 (i), O.** S28 (i): 'stands' can be read as final; the point is only that a new question does not change the old one.

```
OLD: and the failure on \(p\) stands (Historical index).
NEW: and it leaves the failure on \(p\) as it was (Historical index).
```

**A12. l. 606, S28 (i), O.** S28 (i): 'fixed' can be read as final; the argument needs only that the claim is indexed.

```
OLD: and whether \(\mathcal E\) meets (E) on \(C\) is fixed at that index (Part VIII, historical index).
NEW: and whether \(\mathcal E\) meets (E) on \(C\) is a claim at that index (Part VIII, historical index).
```

**A13. l. 15, mimo 1 8, X, changes a claim.** A proportion the semantics never measures and no word of the owner's gives (S20: no count).

```
OLD: and question-finding is at least half of creativity.
NEW: and creativity includes finding questions, not only answering them.
```

**A14. l. 17, mimo 1 1; mimo 4 F3 (ii), X, changes a claim.** 'Rules out as a non-explanation' reads both ways; 'their' had no clear antecedent; 'meets all four' made physical realization a condition a candidate meets (against S25), and is aligned with Part XV's (Suff).

```
OLD: and (iv) their physical realization. A candidate that an argument not using these four rules out as a non-explanation of its question, and that these four cannot represent, would conflict with the conjecture; so would a candidate that meets all four and that such an argument rules out as an explanation on its question and contract.
NEW: and (iv) their physical realization, the instantiation and transformation of these contents in carriers (Part I). A candidate would conflict with the conjecture if an argument not using these four ruled out the claim that it is a non-explanation of its question while these four cannot represent it; so would a candidate that meets (E) on its question and contract (Part V) when such an argument rules out the claim that it is an explanation there.
```

**A15. l. 31, mimo 4 F1, X.** Argument 6's reasons end at (O) and (Q) as well; the front matter says what the claim now says.

```
OLD: Everything else is defined in terms of the two imports, the declared indices and the **declared inputs**,
NEW: Everything else is defined in terms of the two imports, the structural vocabulary of (O) and (Q), the declared indices and the **declared inputs**,
```

**A16. l. 43, mimo 1 3, X.** 'Declared' is also one of three provenances (Part III); 'stated' removes the clash.

```
OLD: A contract is a declared subset of the changes its target admits (Part II)
NEW: A contract is a stated subset of the changes its target admits (Part II)
```

**A17. l. 47, atria A 3, X.** The front matter said flatly what Part IV (l. 201) calls one arrangement, not a requirement; l. 35 promises the front matter says nothing the body does not.

```
OLD: Selection appears once, at the bottom, to produce the object layer of persistent things that explanation operates on.
NEW: Selection appears at the bottom: in the arrangement Part IV describes, as one possibility and not a requirement, it produces the object layer of persistent things that explanation operates on.
```

**A18. l. 49, mimo 1 7, X.** 'Argument' is defined in Part 0 as reasons why this and not that; a candidate explanation is another thing.

```
OLD: A mathematical argument explains, relative to a question,
NEW: A piece of mathematics explains, relative to a question,
```

**A19. l. 53, glm A 3, X.** 'Testable in principle', set against 'a kind-label is not a claim about anything', reads as a criterion of meaning by testability (S23); the contrast needs only the physical claim.

```
OLD: Whether it occurred is a claim about the physical module, fallible but testable in principle.
NEW: Whether it occurred is a claim about the physical module, fallible as any claim about it is (Part XII).
```

**A20. l. 61, atria A 4; mimo 1 4, X.** The labels (A) to (E) are also the tags of question fidelity, the account relation and others.

```
OLD: In short: (A) sufficiency of the four conditions of Account; (B) their necessity; (C) the eliminability of kinds; (D) the two provenances
NEW: In short: (Suff) sufficiency of the four conditions of Account; (Nec) their necessity; (Elim) the eliminability of kinds; (Prov) the two provenances
```

**A21. l. 61, atria A 4; mimo 1 4, X.** As above.

```
OLD: (E) the representability of question-finding.
NEW: (QF) the representability of question-finding.
```

**A22. l. 105, mimo 1 7, X.** As at l. 49.

```
OLD: mathematical arguments or histories.
NEW: mathematical structures or histories.
```

**A23. l. 109, mimo 1 6, X.** 'Reporting' is a role word under a heading that supplies no roles; the pointer names the signature it comes from.

```
OLD: A port is an **observation** when \(A\) contains an edit that alters the relation reporting it without altering what it reports.
NEW: A port is an **observation** when \(A\) contains an edit that alters the relation reporting it without altering what it reports, that is, when the component assigning it has a measurement's signature (below).
```

**A24. l. 119, mimo 1 9 (b), X.** Four components introduced, three glossed.

```
OLD: where \(\tau\) translates edits,
NEW: where \(\pi\) translates valuations, \(\tau\) translates edits,
```

**A25. l. 151, mimo 1 5, X.** Two of the five respects had no pointer; the fix points to where they are worked, and adds no claim.

```
OLD: An obstruction question has a \(\mathcal Q\) that returns reachable or unreachable.
NEW: An obstruction question has a \(\mathcal Q\) that returns reachable or unreachable. The rule-status and purpose-achievement cases are given with constitutive rules (Part VII) and with achievement, (AR) (Part XI).
```

**A26. l. 155, mimo 1 3, X.** Two senses of 'declared' named apart.

```
OLD: A **declared** contract is stipulated by the modeller.
NEW: A **declared** contract is stipulated by the modeller, with neither selection nor construction in its history; this is its provenance, and not the sense in which every contract, whatever its provenance, is a declared index of the claims made on it (Part XIV).
```

**A27. l. 159, mimo 1 3, X.** As at l. 43.

```
OLD: A contract is a declared subset of the changes its target admits (Part II), and a stated scope is what makes it one.
NEW: A contract is a stated subset of the changes its target admits (Part II), and a stated scope is what makes it one.
```

**A28. l. 193, mimo 2 5, X.** (R) gives a provenance to a transport from an occurrence's organization to a content, which need not be an organization of a physical system.

```
OLD: A transport \(t\) between organizations of a physical system has exactly one of three provenances,
NEW: A transport \(t\) whose domain is an organization of a physical system has exactly one of three provenances,
```

**A29. l. 197, mimo 2 4, X.** 'Target' is the question's target elsewhere; here it meant the transport's codomain.

```
OLD: or the organization it targets,
NEW: or the organization it carries to,
```

**A30. l. 205, mimo 2 5, X.** 'Admits' is the verb for edits (Part II); the parameters of Sel and Con were suppressed without a word.

```
OLD: when the organization that \(o\) instantiates under the physical module, at grain \(\ell\), admits a transport to \(c\) that is faithful on \(c\)'s contract and whose provenance is selected or constructed:
NEW: when there is a transport from the organization that \(o\) instantiates under the physical module, at grain \(\ell\), to \(c\), faithful on \(c\)'s contract, whose provenance is selected or constructed; in (R), \(\operatorname{Sel}(t)\) and \(\operatorname{Con}(t)\) abbreviate \(\operatorname{Sel}(t;\mathcal T,\mu,H)\) and \(\operatorname{Con}(t;h,e)\) for some such parameters:
```

**A31. l. 211, mimo 2 4, X.** Transports run from the target to the candidate (l. 183, l. 231).

```
OLD: while the content's transport to its target fails.
NEW: while the transport from the content's target to the content fails.
```

**A32. l. 231, atria A 6; mimo 2 6, X.** A quadruple was called a pair, and Account was used with two arguments (ll. 290, 302) with no word saying what they abbreviate.

```
OLD: The pair \(\mathcal E=(E,p,t,\Gamma)\) meets \(\operatorname{Account}(\mathcal E)\) exactly when the following four conditions are met, each a condition on supplied relations under the changes in \(C\).
NEW: The candidate together with its question, \(\mathcal E=(E,p,t,\Gamma)\), meets \(\operatorname{Account}(\mathcal E)\) exactly when the following four conditions are met, each a condition on supplied relations under the changes in \(C\). Where an organization \(E'\) is obtained from \(E\) by a declared operation (Part VI), \(\operatorname{Account}(E',p)\) abbreviates \(\operatorname{Account}\big((E',p,t',\Gamma')\big)\), with \(t'\) the transport the operation carries \(t\) to and \(\Gamma'\) the commitments it leaves; for \(E|W\), \(t'\) is \(t\) with \(\lambda\) restricted to the components of \(E|W\), and \(\Gamma'\) is \(W\).
```

**A33. l. 233, glm A 1, X.** V_k is a footprint of E and Sol of lambda(k) is over ports of D; the projection needs the port translation that l. 119 and Argument 1 name.

```
OLD: the relation obtained by imposing the constraints of \(\lambda(k)\) and projecting away its hidden ports equals the component relation of \(k\) under the translated edit:
NEW: the relation obtained by imposing the constraints of \(\lambda(k)\), projecting away its hidden ports and carrying what remains to \(V_k\) by the port translation of \(\lambda\) (write \(\operatorname{proj}^{\lambda}_{V_k}\) for this projection) equals the component relation of \(k\) under the translated edit:
```

**A34. l. 236, glm A 1, X.** As at l. 233.

```
OLD: \operatorname{proj}_{V_k}\!\big[
NEW: \operatorname{proj}^{\lambda}_{V_k}\!\big[
```

**A35. l. 245, mimo 2 3, X.** (F1) quantifies over C; l. 281 reads kinds on C.

```
OLD: By (K), no component of \(E\) whose signature differs from its counterpart's meets (F1);
NEW: By (K), no component of \(E\) whose signature on \(C\) differs from its counterpart's meets (F1);
```

**A36. l. 255, mimo 2 1, X.** Whose answer and which 'there' were unstated; the loss clause is about E's answers at these two points, and by (A) the first disjunct is unchanged.

```
OLD: such that the answer profile at \((a,b)\) differs from its value at \((1,b_0)\), or is not determined there in the claimed way,
NEW: such that the answer of \(E\) at \((\tau(a),\sigma(b))\) differs from its answer at \((1,\sigma(b_0))\), or is not determined at \((\tau(a),\sigma(b))\) in the claimed way,
```

**A37. l. 257, mimo 1 3, X.** As at l. 43.

```
OLD: The contract \(C\) is a declared subset of the edits the target admits,
NEW: The contract \(C\) is a stated subset of the edits the target admits,
```

**A38. l. 257, mimo 2 6, X.** Non-circular dependence is a condition on a candidate, not on a contract.

```
OLD: does not meet non-circular dependence and is therefore not a contract
NEW: admits no candidate that meets non-circular dependence, and is therefore not a contract
```

**A39. l. 305, mimo 2 7, X.** Singletons were equated with commitments, and 'globally indispensable' (and l. 307's 'contributory') had no definition before use; the argument's reasons are unchanged and read as before.

```
OLD: then the critical singletons are exactly \(\bigcup\min\mathsf S\) and the globally indispensable ones are exactly \(\bigcap\min\mathsf S\).
NEW: then \(d\in\Gamma\) is critical for some route (**contributory**) exactly when \(d\in\bigcup\min\mathsf S\), and \(d\) is **globally indispensable**, \(\Gamma\setminus\{d\}\notin\mathsf S_{E,p}\), exactly when \(d\in\bigcap\min\mathsf S\).
```

**A40. l. 311, mimo 2 8, X.** The set-builder had its condition on x, not on n.

```
OLD: \(\Gamma=\{d_n:|x|\le 1/n\}\): every unbounded index set determines \(x=0\);
NEW: \(\Gamma=\{d_n:n\in\mathbb N\}\), \(d_n\) the constraint \(|x|\le 1/n\): every set of indices unbounded in \(\mathbb N\) determines \(x=0\);
```

**A41. l. 325, atria A 2, X.** U_H and U_theta occur only here; the gloss keeps the components the rest of the paragraph intervenes on.

```
OLD: Stipulate \(H:=U_H,\ \theta:=U_\theta,\ L:=H\cot\theta\).
NEW: Stipulate \(H:=U_H,\ \theta:=U_\theta,\ L:=H\cot\theta\), where \(U_H\) and \(U_\theta\) are exogenous values setting the pole's height \(H\) and the sun's elevation \(\theta\), and \(L\) is the length of the pole's shadow.
```

**A42. l. 329, atria A 1; glm A 2; mimo 3 5, X.** A is the set of admitted edits (l. 91); the tag (I3) was missing since file 10, not dropped by the scrub or the repair (looked up in draft 5 and file 10); no line cites (I4).

```
OLD: For linear \(A\) and feature \(c^\top\), identification is \(\ker A\subseteq\ker c^\top\). (I4)
NEW: For linear \(g\) and linear feature \(c^\top\), identification is \(\ker g\subseteq\ker c^\top\). (I3)
```

**A43. l. 331, atria A 1, X.** x, b_A and b_B were never introduced, and the kernel claim goes through only in that order.

```
OLD: For the two balances \(\begin{pmatrix}1&1&0\\1&0&1\end{pmatrix}\), the kernel
NEW: For the two balances \(\begin{pmatrix}1&1&0\\1&0&1\end{pmatrix}\), reading an unknown mass \(x\) with biases \(b_A,b_B\), in that order, the kernel
```

**A44. l. 339, mimo 3 6, X.** Fullness of a deleted component's relation is stated at l. 103, beside (O), not by (O).

```
OLD: whose relation is full by (O).
NEW: whose relation is full (Part II).
```

**A45. l. 339, atria A 4; mimo 1 4, X.** The Part XV labels, renamed.

```
OLD: is listed under attack (B) in Part XV
NEW: is listed under attack (Nec) in Part XV
```

**A46. l. 343, mimo 1 7, X.** As at l. 49.

```
OLD: That a three-line mathematical argument is shorter
NEW: That a three-line piece of mathematics is shorter
```

**A47. l. 369, mimo 3 3, X.** The lapse is (K2)'s; becoming an account is (E)'s.

```
OLD: the argument is not usable and those candidates are no longer ruled out by it, every such candidate alike; no candidate becomes an account by that (K2).
NEW: the argument is not usable (K2) and those candidates are no longer ruled out by it, every such candidate alike; no candidate becomes an account by that (E).
```

**A48. l. 375, mimo 3 1, X.** (EX) uses a relation never defined.

```
OLD: with an acyclic causal precedence \(\prec_h\) and a physical
NEW: with an acyclic causal precedence \(\prec_h\) (write \(\preceq_h\) for its reflexive closure) and a physical
```

**A49. l. 377, mimo 3 1, X.** Account takes the whole candidate, question included (l. 231).

```
OLD: and \(\mathcal E_c\) the criticism's connection from \(g\) to \(\delta\), interpreted as an explanatory candidate (Part V) for \(p_\delta\).
NEW: and \(\mathcal E_c\) the explanatory candidate (Part V) for \(p_\delta\) whose organization is the criticism's connection from \(g\) to \(\delta\), with its transport and its identified commitments.
```

**A50. l. 380, mimo 3 1, X.** As at l. 377.

```
OLD: \operatorname{Account}(\mathcal E_c,p_\delta)
NEW: \operatorname{Account}(\mathcal E_c)
```

**A51. l. 387, mimo 3 1, X.** 'Essential' was never said.

```
OLD: with essential premises \(\operatorname{Prem}(u)\):
NEW: with essential premises \(\operatorname{Prem}(u)\), the premises its inference form uses:
```

**A52. l. 413, mimo 3 2, X.** Faithful on c's contract makes the relation neither symmetric nor transitive in general; (N) needs neither.

```
OLD: The equivalence is structural at the stated grain, not string equality or similarity.
NEW: The relation is structural at the stated grain, not string equality or similarity; it is read with \(c\) and its contract fixed, and (N) uses it only so, testing each \(d\) against \(c\).
```

**A53. l. 422, mimo 3 1, X.** The arguments, written out; no change of claim.

```
OLD: \iff\operatorname{Attempt}\land\operatorname{New}\land\operatorname{Build}.
NEW: \iff\operatorname{Attempt}(s,c,p,h,e)\land\operatorname{New}(s,c,h,e)\land\operatorname{Build}_{\beta,\ell}(s,c,h,e).
```

**A54. l. 447, mimo 3 1, X.** xi and xi' were free in (EX).

```
OLD: \land\operatorname{Repair}_{O,P}(\xi,\xi';\Delta)\\
NEW: \land\exists\xi,\xi'\,\bigl[\operatorname{Repair}_{O,P}(\xi,\xi';\Delta)\\
```

**A55. l. 448, mimo 3 1, X.** Account needs a transport and commitments for c.

```
OLD: \exists c,p_c,e_c\,[e_c\preceq_h e\land\neg o(\xi)\land o(\xi')\land\operatorname{Origin}(s,c,p_c,h,e_c)\\
NEW: \exists c,p_c,e_c,t_c,\Gamma_c\,[e_c\preceq_h e\land\neg o(\xi)\land o(\xi')\land\operatorname{Origin}_{\beta,\ell}(s,c,p_c,h,e_c)\\
```

**A56. l. 449, mimo 3 1, X.** As at l. 447 and l. 448.

```
OLD: \land\operatorname{Account}(c,p_c)\land c\in\operatorname{Result}(\Delta)\land\operatorname{Deploy}(s,c,\xi';U_c)\land\operatorname{ProducesVia}(\Delta,c,o;\xi,\xi')].
NEW: \land\operatorname{Account}\big((c,p_c,t_c,\Gamma_c)\big)\land c\in\operatorname{Result}(\Delta)\land\operatorname{Deploy}_{\beta,\ell}(s,c,\xi';U_c)\land\operatorname{ProducesVia}(\Delta,c,o;\xi,\xi')]\bigr].
```

**A57. l. 453, mimo 3 1, X.** Glosses for the new bound variables and for U_c, which was free.

```
OLD: The scope of \(\operatorname{Account}(c,p_c)\) is the contract fixed at \(e_c\).
NEW: In (EX), \(t_c\) and \(\Gamma_c\) are the transport and the identified commitments that make \(c\), with \(p_c\), an explanatory candidate (Part V), and \(U_c\) is the declared use task for \(c\) (Deploy, Part X). The scope of \(\operatorname{Account}((c,p_c,t_c,\Gamma_c))\) is the contract fixed at \(e_c\).
```

**A58. l. 455, mimo 3 4, X.** A, K and F already name edits, the signature tag and the feature space.

```
OLD: \(\mathcal R\subseteq A\times K\times F\); a purpose \(G\subseteq K\times F\);
NEW: \(\mathcal R\subseteq \mathit{Act}\times\mathit{Occ}\times\mathit{Eff}\); a purpose \(G\subseteq \mathit{Occ}\times\mathit{Eff}\);
```

**A59. l. 455, mimo 3 4, X.** Rsn and V_A were never glossed.

```
OLD: \(\mathcal N\subseteq A\times K\times\mathcal Rsn\times\mathcal V_A\) taken as a substantive input when aesthetic value is claimed.
NEW: \(\mathcal N\subseteq \mathit{Act}\times\mathit{Occ}\times\mathsf{Rsn}\times\mathcal V_A\) taken as a substantive input when aesthetic value is claimed, where \(\mathit{Act}\) is a set of actions, \(\mathit{Occ}\) of occasions, \(\mathit{Eff}\) of effects, \(\mathsf{Rsn}\) of aesthetic reasons and \(\mathcal V_A\) of aesthetic values, the last two not further specified here.
```

**A60. l. 495, mimo 4 F5, X.** Enable read as circular; 'enabling condition' is the chi of (CT1).

```
OLD: enabling condition for \(s\) and the task \(T\).
NEW: enabling condition for \(s\) and the task \(T\), in the sense of (CT1).
```

**A61. l. 497, mimo 4 F5, X.** Symbols used in (U1) to (U3) with no gloss or pointer.

```
OLD: both specified independently of the candidate,
NEW: both specified independently of the candidate, with \(\operatorname{Can}\), \(\operatorname{CanAdv}\), \(J_p\) and \(C_I\) as in Part XII, \(U_c\) the declared use task for \(c\) (Deploy, Part X), \(A_p\) the task for \(p\) that \(\operatorname{CanAdv}\) describes, and \(\xi_0\) the index at which the claim is made,
```

**A62. l. 506, mimo 4 F5, X.** xi_0 was free in (U3).

```
OLD: \mathsf{UECS}=\{(M,s,\Omega,\beta):
NEW: \mathsf{UECS}=\{(M,s,\xi_0,\Omega,\beta):
```

**A63. l. 520, mimo 4 F1, X.** As at l. 31.

```
OLD: Everything else is defined in terms of the two imports, the declared indices and the declared inputs (below).
NEW: Everything else is defined in terms of the two imports, the structural vocabulary of (O) and (Q), the declared indices and the declared inputs (below).
```

**A64. l. 526, mimo 4 F10, X.** One sentence with four referents for 'it'; split, with each named.

```
OLD: The order has no cycle and no endless descent: a representation defined only by its own construction, or an ownership and a capability each defined only by the other, has not supplied its place in it, and a separate definition that would supply it, or a separate argument that rules out the denial of the result it is defined through without using it, is part of the account only when the account uses it.
NEW: The order has no cycle and no endless descent. A representation defined only by its own construction, or an ownership and a capability each defined only by the other, has not supplied its place in the order; a separate definition that would supply that place, or a separate argument that rules out the denial of the result the definition goes through without using that result, is part of the account only when the account uses it.
```

**A65. l. 536, atria A 4; mimo 1 4, X.** The Part XV labels, renamed.

```
OLD: **(A) Sufficiency.**
NEW: **(Suff) Sufficiency.**
```

**A66. l. 536, mimo 4 F3, X.** 'Non-declared' could be read as a declared input; it is the provenance. 'Rules out as' made one-way.

```
OLD: with a non-declared transport, that an argument not using (E) rules out as an explanation of what its question asks.
NEW: with a transport whose provenance is not declared (Part IV), such that an argument not using (E) rules out the claim that it is an explanation of what its question asks.
```

**A67. l. 536, mimo 4 F3, X.** As above.

```
OLD: and such an argument rules it out as an explanation.
NEW: and such an argument rules out the claim that it is an explanation.
```

**A68. l. 538, atria A 4; mimo 1 4; mimo 4 F3 (ii), X.** The Part XV label, renamed; 'rules out as a non-explanation' reads both ways.

```
OLD: **(B) Necessity.** A candidate that an argument not using (E) rules out as a non-explanation,
NEW: **(Nec) Necessity.** A candidate such that an argument not using (E) rules out the claim that it is a non-explanation,
```

**A69. l. 540, atria A 4; mimo 1 4, X.** The Part XV labels, renamed.

```
OLD: **(C) Reinstatement of kinds.**
NEW: **(Elim) Reinstatement of kinds.**
```

**A70. l. 540, mimo 4 F9 (i), X.** The kind-label case bears on the Consequence (the word 'kind' eliminable), not on the signature Claim.

```
OLD: would rule out the Claim of Argument 1,
NEW: would rule out the Consequence of Argument 1,
```

**A71. l. 542, atria A 4; mimo 1 4, X.** The Part XV labels, renamed.

```
OLD: **(D) Genesis.**
NEW: **(Prov) Genesis.**
```

**A72. l. 544, atria A 4; mimo 1 4, X.** The Part XV labels, renamed.

```
OLD: **(E) Question-finding.**
NEW: **(QF) Question-finding.**
```

**A73. l. 556, glm A 1, X.** As at l. 233; Argument 1's reasons use the same projection.

```
OLD: \operatorname{proj}_{V_k}\operatorname{Sol}_{\lambda(k)}(a,b)
NEW: \operatorname{proj}^{\lambda}_{V_k}\operatorname{Sol}_{\lambda(k)}(a,b)
```

**A74. l. 562, mimo 4 F9 (ii), X, changes a claim.** The argument's reasons compose one translation with the inverse of the other.

```
OLD: with port translations onto the same ports of \(D\)
NEW: with port translations that are bijections onto the same ports of \(D\)
```

**A75. l. 568, mimo 4 F2, X.** 'The remedy is' names what must happen (S21); 'must supply it' is a condition on a claim and stays.

```
OLD: and must supply it. The remedy is a finer contract, which is a new question.
NEW: and must supply it. A finer contract that contains such a change is a new question (Part III); whether anyone asks it is that person's choice (Part 0).
```

**A76. l. 582, mimo 4 F4, X.** Part IV (l. 217) defines surprise only at occurring pairs of C; the reasons now say so.

```
OLD: Surprise is defined as a violation of a selected transport at \((a,b)\notin H\). If there is no transport there is no prediction and hence no violation. If \(H=C\), every occurring \((a,b)\) is in \(H\), so no violation at \((a,b)\notin H\) exists.
NEW: Surprise is defined (Part IV) as a violation of a selected transport at an occurring \((a,b)\in C\) with \((a,b)\notin H\). If there is no transport there is no prediction and hence no violation. If \(H=C\), every such \((a,b)\) is in \(H\), so no violation at a pair of \(C\) outside \(H\) exists.
```

**A77. l. 588, mimo 4 F7, X, changes a claim.** The reasons build the organization; the claim now says what they give.

```
OLD: **Claim.** A contract \(C\) is an organization (a set of edits with a query), and can be the content \(c\) in (G).
NEW: **Claim.** A contract \(C\), taken with its edits and its query, can be given the structure of an organization in the sense of (O), and can be the content \(c\) in (G).
```

**A78. l. 590, mimo 4 F7, X.** (O) asks for a relation for each component.

```
OLD: components (the closure conditions), and admitted edits
NEW: components (the closure conditions, each with the relation it imposes on its ports, as (O) requires), and admitted edits
```

**A79. l. 596, mimo 4 F1, X.** The reasons end at (O) and (Q) as well.

```
OLD: together with declared indices and declared inputs.
NEW: together with the structural vocabulary of (O) and (Q), declared indices and declared inputs.
```

**A80. l. 600, mimo 4 F11, X.** The second import is the appraisal relation (l. 31, l. 518).

```
OLD: a theory of reasons.
NEW: a theory of appraisal.
```

**A81. l. 608, mimo 4 F12, X.** The index does the work, not a record (S20: 'A record is redundant').

```
OLD: Goalpost-moving is the act of changing the index without recording the change, and it is a failure of the record, not an operation the semantics admits.
NEW: Goalpost-moving is the act of passing off a claim at one index as a claim at another; it is not an operation the semantics admits, since every claim is relative to its declared index (Part XIV).
```

**A82. l. 612, mimo 4 F8, X, changes a claim.** (P) and (EX) depend on the declared aims with their occasions (l. 526).

```
OLD: Transporting all carriers, relations, transports, histories, and contracts along structure-preserving bijections preserves (E), (G), (P), (EX). *Why this and not its denial.* Each is a conjunction of equalities and existence claims over the transported data; bijections preserve them.
NEW: Transporting all carriers, relations, transports, histories, contracts and declared inputs along structure-preserving bijections preserves (E), (G), (P), (EX). *Why this and not its denial.* Each is a conjunction of equalities and existence claims over the transported data, the declared aims and occasions of (P) and (EX) among them; bijections preserve them.
```

**A83. l. 622, mimo 4 F4, X.** The example cites Argument 4 without stating the contract the occlusion lies in.

```
OLD: A simulation layer \(S_0\) with a transport \(t_0\) selected on a history \(H_0\) containing displacements and velocity changes but no occlusions.
NEW: A simulation layer \(S_0\) with a contract \(C_0\) containing the occlusion edit, and a transport \(t_0\) selected on a history \(H_0\subsetneq C_0\) containing displacements and velocity changes but no occlusions.
```

**A84. l. 626, mimo 4 F6 (i), X.** The sentence brought back a kind-label and read as circular.

```
OLD: They are objects because they respond as objects do to what the contract admits.
NEW: On this contract the word adds nothing to the signatures they already have (Argument 1).
```

**A85. l. 630, mimo 4 F6 (ii), X.** 'Them' was the pairings here and the things in the next sentence.

```
OLD: is a claim that some admitted change distinguishes them, and on this contract none does.
NEW: is a claim that some admitted change separates the two pairings of persistence components to things, and on this contract none does.
```
