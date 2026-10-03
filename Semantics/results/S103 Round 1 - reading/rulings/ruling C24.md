# S103 Round 1 — ruling on C24 (L383)

*Written by a fresh checker (Opus 5.5), 27 September 2026, filled as it goes. Not committed. This file obeys decision S23 except where it quotes the text, a reader or the owner.*

**Ruling: KEEP.** The sentence stands as it is.

- **Old (L383, first sentence of the line):** `A criticism occurrence can exist when (K1) fails.`
- **New:** `A criticism occurrence can exist when (K1) fails.` (unchanged)
- **Easy to vary on this reading (rule 5):** yes, in the plain sense the brief asks about, and recorded as such. Both closing rivals are rewordings that change nothing the theory needs from the sentence: Mimo's `A criticism occurrence can exist whether or not (K1) holds.` and GLM's `A criticism occurrence need not meet (K1).` each say that being a criticism occurrence does not ask for bearing, each keeps the pointer to (K1), and every sentence that leans on L383's first sentence reads as before under either. Neither is clearer than the text's wording (reasons below), so the ruling is KEEP, not FIX.

## What was read

- The text under review, `tests/99 The semantics, standing alone.md`, md5 74f4a4c7619345747f4fa976ddac9548 (checked before reading; not written to): L360–L399 (the end of Part VIII and Part IX whole), L13, L67–L73, L165–L171, L199–L201, L215–L220, L229–L233, L257–L281, L315–L317, L429, L520–L526, L606; and the whole file searched by program for "(K1)", "Bearing", "bearing", "criticism", "objection", "adverse signal", "fails" and "holds".
- The reading rule, `results/S103 Round 1 - how the replies will be read, written before sending.md`, whole.
- The part 3 brief, `tests/S103 Round 1 - trying to vary the strong candidates - part 3, Parts V to XIV.md` (md5 44ef4fbdb179963c3e76fcdaf60ecf27): sections 1 and 2, the C24 entry of section 3 (brief lines 95–114), and sections 5 and 6.
- The tabulation, `results/S103 Round 1 - reading/tabulation.md` (md5 51e752c3e26ab822e69daf8e9ec9f387): its opening (lines 1–60), C24's section (lines 2340–2442) and the note that names C24 (line 3038).
- The replies: `s103_vary_mimo_3.response.txt` (md5 a1491ae7b541cf691c5760cf07c93d44) lines 97–130 and `s103_vary_glm_3.response.txt` (md5 540429867c7029b78bcb9ad72c1af834) lines 44–59. All six replies were searched for "C24", "L383", "(K1)", "K1" and "Bearing"; there is no hit outside those two sections. No reasoning file was opened.
- The owner's decisions S20–S35 in `records/Semantics - Decisions.md` (md5 71459192867b1ebcf1bae914c9297129).
- For ties to cases: the S98 ledger (`results/S98 Ledger of edits and recommendations/line-up/`), group 09, entries L383.s1 and L383.s2, `data/by sentence.csv` (the rows of section sec-L377-383 and of L385) and `data/records.jsonl` (no record names L383.s1); the S100 data row for L383.s1; `results/S96 Check of the repaired copy - cases.md`, searched for "l. 383", "(K1)", "bearing", "criticism" and "objection"; the S81 case book of 52 cases and the S89 candidate cases N1 to N25, searched for the same.

## The sentence and where it stands

L383 (whole line):

> A criticism occurrence can exist when (K1) fails. An adverse signal is not a criticism until an organization represents it as the premise of a criticism alleging a defect in a target.

It follows the definition of bearing. L377: "**Bearing.** A criticism has target \(z\), alleged defect \(\delta\), premise \(g\), and a connection. Let \(p_\delta\) be the question whether \(z\) has \(\delta\) in respect of \(p\), and \(\mathcal E_c\) the explanatory candidate (Part V) for \(p_\delta\) whose organization is the criticism's connection from \(g\) to \(\delta\), with its transport and its identified commitments. Then" and L380: `\operatorname{Bearing}(c,z,p)\iff\operatorname{Account}(\mathcal E_c). \tag{K1}`.

The terms it uses: an **occurrence** is "a physically located carrier" (L169: "An **occurrence** is a physically located carrier. A **content** is an organization together with its contract-relative commitments."); **Account** is (E) (L262: `\operatorname{Account}(\mathcal E)\iff \text{(F1)}\land\text{(F2)}\land\text{(A)}\land\text{NonCircular}\land\text{NonVacuous}. \tag{E}`), met by an explanatory candidate as L231 defines one.

What the sentence does: it separates a criticism's existence, as an occurrence, from its bearing. With the second sentence of L383, the line says what a criticism's existence asks for (that an organization represent an adverse signal "as the premise of a criticism alleging a defect in a target") and what it does not ask for (bearing, (K1)). It makes precise, for bearing, two commitments of Part 0: L71, "A criticism has a target and is itself conjectural.", and L67, "Systems can be in error about their transports, their observations, their criticisms and their own capacities." L385 then says the same of use: "Using an objection does not give it bearing (K1) or make any argument from it usable (K2)."

## Each side's argument (rule 7)

**Mimo (VARIES).** Rival: `A criticism occurrence can exist whether or not (K1) holds.` (reply line 102). It "Keeps the modality "can exist" and the (K1) pointer of L380"; "it says existence is possible with and without bearing, which is the separation the sentence draws" (line 105). Three variations are said to break something (lines 110–125; weighed below). Step 3: ""(K1) fails" reads as "the condition (K1) states is unmet", the same idiom as L269's "it fails (F1)"; taken as the biconditional coming apart it would be nonsense, but nothing forces that reading." (line 127).

**GLM (VARIES).** The sentence's work: "block the inference from "a criticism occurred" to "it had bearing"" (reply line 48), which GLM ties to S27 and to L71. Rival: `A criticism occurrence need not meet (K1).`: ""meet" is the text's verb for satisfying a condition (L277: "a mechanism meets (E) or fails it"); it states the same non-necessity, pairs unchanged with the next sentence […], and breaks nothing I can find: L377–L381 define Bearing only, not occurrence, and L385 presupposes exactly this independence" (line 53). A second wording, `A criticism occurrence can exist while it lacks bearing (K1).`, is called "same content, slightly longer" (line 52). Fault search: ""(K1) fails" follows the text's usage (L267, L271, L273); the only way K1 can fail for a criticism c is ¬Account(ℰ_c), so the sentence is coherent." (line 56).

**Where they differ, and the ruling between them.** They do not differ on the sentence's work, on its standing (neither finds a fault), or on the idiom. They differ only in which rival they close with, and each rival is weighed on its own below. On the idiom both readers take "(K1) fails" to mean that the condition (K1) names, bearing, is not met, and that is the reading the text's own usage gives. The text uses a tag as the name of the condition it defines, and a condition as the subject of "fails": L281, "(F1) already fails for a component whose counterpart is of the other kind"; L220, "a **violation** occurs when fidelity fails at \((a,b)\);". It does the same with (E), which is itself tagged on a biconditional (L262): L277, "a mechanism meets (E) or fails it"; L606, "\(\mathcal E\) can meet (E) on \(C\) and fail it on \(C'\)". And it uses "(K1)" for bearing itself: L385, "does not give it bearing (K1)"; L526, "(K1) depends on (E)." The readers' own citations are looser than the point needs: Mimo's L269 ("it fails (F1)") and GLM's L271 and L273 show a thing failing a condition, not a condition failing, and GLM's L267 is the heading "## What (E) excludes, and what it does not", which holds no "fails". The point stands on L281 and L220.

## Is each rival a rewording or a different claim?

What the theory needs from the sentence:

1. that being a criticism occurrence does not ask for bearing: a criticism can occur while \(\mathcal E_c\) is not an account of \(p_\delta\);
2. the pointer to (K1), so that what may be lacking is bearing as L377–L380 define it, the same bearing L385 names;
3. that it leaves the existence condition to the next sentence and does not itself make a failure of bearing enough for existence (Mimo's first variation, below, shows the break).

**Mimo's rival** keeps (1) in its "or not" half, keeps (2), and keeps (3) ("can exist", not "exists"). It adds the other half: that a criticism occurrence can exist when (K1) is met. The theory already has that. (K1) is defined over criticisms, and a criticism with bearing is a criticism by the same condition as one without (L383's second sentence names no condition on bearing); L317's "A criticism that a candidate is easy to vary must supply such a rival (Part IX)" speaks of criticisms whatever their bearing. The added half adds no claim. A rewording.

**GLM's rival** keeps (1) ("need not meet (K1)"), keeps (2), and keeps (3) (it makes no existence claim). It drops "exist", and so leaves unsaid what the "need not" is relative to; read with the next sentence, it is relative to being a criticism. A rewording.

**Dependents under either.** L383's second sentence reads the same after either; so do L385, L429 ("a conjectural objection"), L201 and L13 (criticism in the history of a constructed transport), L71 and L67. No case moves under either (below).

**The owner's words.** Neither rival has a word or idea S23 forbids; neither says what must happen (S21: "need not" says what is not asked for, not what must happen); neither lists or counts rivals (S20); neither brings in physical possibility (S25–S27).

So neither rival makes a different claim, and neither is weighed as a challenge. The sentence is easy to vary on this reading, and that is recorded.

## Is either rival clearer?

**Mimo's rival.** For it: it states the separation both ways at once. Against it:

1. "(K1) holds" brings in a verb the text never uses of a tag. The text says a condition is met or fails (L277, L281, L606); it never says "(E) holds" or "(F1) holds". In the text "holds" is what a person or a system does with a transport, an explanation or an argument: L201, "A physical system may hold selected transports"; L393, "whether or not \(j\) holds an explanation of \(d\)"; L397, "by someone who holds no explanation of it".
2. The reading both readers set aside, (K1) taken as the biconditional, does more harm under "holds" than under "fails". Taken so, "(K1) fails" names a case that never occurs, since a definition does not come apart; the text's sentence then reads as plain nonsense, and a reader drops that reading and takes the one the usage above gives (Mimo's step 3). Taken so, "(K1) holds" names every case, so "whether or not (K1) holds" collapses to "A criticism occurrence can exist": not nonsense, and a reader need not notice that the point about bearing has gone.
3. The added half is not a point anyone needs made at L383. The point needed is the one direction a reader of (K1) could miss, that a criticism without bearing is still a criticism; the text says that direction alone.

**GLM's rival.** For it: "meet" is the text's verb for a condition (L277), and "need not" puts the non-necessity in so many words. Against it:

1. It makes the occurrence the thing that meets or fails (K1). By L169 an occurrence is "a physically located carrier", while (K1) is a relation of the criticism \(c\), with its target \(z\) and question \(p\), through the candidate \(\mathcal E_c\) formed from the criticism's connection (L377). The text's sentence keeps the occurrence as the subject of existence only and makes (K1) the subject of "fails", as L281 does with (F1). The shorthand in the rival is readable ("the criticism it carries"), so this is a loss of precision, not a break.
2. It drops "exist", so the "need not" loses its relatum. The text names it, existence, and pairs it with the next sentence's condition on existence ("is not a criticism until …"): one sentence says what a criticism's existence does not ask for, the next what it does.
3. "Need not" can be heard as what a criticism is permitted; "can exist" says only what can be the case.

**GLM's second wording**, `A criticism occurrence can exist while it lacks bearing (K1).` (not its closing rival), was weighed as a third candidate for a FIX. For it: it names bearing in words, as L385 does ("does not give it bearing (K1)"), and so avoids the idiom both readers discussed. Against it: it is longer; its "it" makes the occurrence the bearer of bearing (point 1 against GLM's rival); and the idiom it avoids reads as the text means on the text's own usage (L281, L220, L277, L606), which both readers found. Not taken.

Weighed together, no rival is clearer than the text's wording. What holds in the challenge is that the sentence can be reworded without loss, not that the text falls short; the smallest change that meets that is none. KEEP.

## The variations that change the claim, and what each breaks

Each is weighed on its own argument; none is a repair of a fault in the sentence, and none is taken.

- `A criticism occurrence exists when (K1) fails.` (Mimo, reply line 110). On Mimo's reading, a failure of bearing is enough for existence; that breaks L383's second sentence, "An adverse signal is not a criticism until an organization represents it as the premise of a criticism alleging a defect in a target.", as Mimo says. On a stricter reading, where "(K1) fails" already presupposes a criticism \(c\), the variation turns the sentence's "can" into a claim about every criticism without bearing that the text does not make and nothing in it needs. Either way the break or the loss is real.
- `A criticism occurrence cannot exist when (K1) fails.` (Mimo, line 116). It makes bearing a condition of existence. Then no existing criticism could be in error as to its bearing, against L67 ("Systems can be in error about their transports, their observations, their criticisms and their own capacities.") and L71 ("A criticism has a target and is itself conjectural."), which Mimo names; L429's "a conjectural objection" would lose its point, and L385's "Using an objection does not give it bearing (K1)" would be idle. Real.
- `A criticism occurrence can exist when (E) fails.` (Mimo, line 122). "(E)" names no candidate. Read as the target's candidate failing (E), it says that a criticism can exist when its target is not an account, which says nothing about bearing (a criticism with bearing of such a target is that very case): Mimo's break of L377–L380's separation is real on that reading. Read as \(\mathcal E_c\) failing (E), it says what the text says, by (K1), but loses the name "bearing" that L385 picks up ("bearing (K1)"). A real cost either way.
- `A criticism can be mistaken.` (GLM, line 54). It drops "occurrence" and "(K1)", so it no longer says what the criticism may lack (bearing as L377–L380 define it), nor that the point concerns existence; and "mistaken" is not a term the semantics defines for a criticism. That is the ground it is not taken on. GLM's further ground, that "mistaken" "trends toward the forbidden truth-language of S23" (GLM's words), is weaker than GLM puts it: S23's words are "true, not true, more true", not error, and the text itself says at L67 that systems "can be in error about … their criticisms".

What the variations show between them: every change to the claim (existence made to follow from, or to require, a failure of bearing; the pointer moved from (K1) to (E); the pointer dropped) meets a named line of the text; the changes that meet none, the two closing rivals, change how the separation is worded and not what is claimed.

## Failures of the sentence itself

None found. Sought:

- **The idiom "(K1) fails" for a biconditional.** Weighed above: the text uses tags as names of the conditions they define and conditions as the subject of "fails" (L281, L220; with (E) at L277 and L606). The biconditional reading gives nonsense and is dropped by any reader who meets it; nothing forces it. Not a fault.
- **For what (K1) fails.** The sentence leaves unsaid that (K1) fails for the criticism the occurrence carries, with its own target \(z\) and the \(p\) in respect of which it alleges the defect (L377). The sentence claims a possibility, so it holds if some criticism occurrence can lack bearing on its own \(z\) and \(p\); no choice of other indices changes that. Not a fault.
- **"Can" and physical possibility (S25–S27).** An occurrence is "a physically located carrier" (L169), so a criticism occurrence is a place where a criticism is instantiated. If "can exist" is read as physical possibility, it stands where S25 and S26 put it ("instantiation and transformation of information and knowledge"); if read as what the definitions allow, no physical possibility is in play. Either way it ties nothing about what an explanation, a question or a conflict is to physical possibility. Not a fault.
- **The owner's other words.** S23: no forbidden word or idea; "fails" means only "is not met". S21: the sentence says what can be, not what must happen. S20: no list, count or grade. S28: the sentence does not say that anyone finds or knows that (K1) fails; whether \(\mathcal E_c\) is an account is, like fidelity, "independent of whether anyone tentatively accepts it" (L67, of transports), and what a person goes on with is left to Part IX and Part 0. The sentence sits with S27 and L397: a criticism from a premise taken as given exists, and can be used, whatever its bearing, and where the argument it serves "uses a claim taken as given, the ruling out is a choice the person using it made, not something the claim does by itself (Part 0)" (L397). GLM's tie to S27 is looser than GLM puts it (S27 concerns using a premise without its explanation, not bearing), but it meets the sentence at this point.
- **Vacuity, or a part doing no work.** Each part works: "criticism occurrence" puts the claim on the occurrence (L169), the thing whose existence the next sentence conditions; "can exist" gives possibility, not sufficiency (Mimo's first variation); "(K1)" points to bearing as defined (the "(E)" variation loses it); "fails" is the text's verb. Nor is the sentence idle beside L71 ("is itself conjectural") and L377's "alleged defect": those leave open whether bearing belongs to what a criticism is, and once (K1) defines bearing for a criticism a reader could take a criticism without bearing to be no criticism at all. L383's first sentence closes that where (K1) is defined.
- **Contradiction.** With L201 ("a constructed one has both", a represented target and criticism in its history): the criticisms in a constructed transport's history need not have had bearing, and nothing there says they must. With L317 ("A criticism that a candidate is easy to vary must supply such a rival (Part IX)"): a condition on what such a criticism contains, not on its bearing. With L385: the parallel for use. None found.

## Cases

No fixed case verdict moves under this KEEP, and none would have moved under either rival.

- **S98 ledger.** Group 09 records "L383.s1 · line 383 · no change recorded"; `records.jsonl` holds no record naming L383.s1. The records against L383.s2 (CH-0452, CH-0570, CH-0738, CH-1055, CH-1120) concern the second sentence's wording ("grounds" to "premise"), not this one. The S100 data row for L383.s1 records it as "never challenged".
- **S96 cases.** No case cites l. 383, (K1) or bearing. The one S96 case that cites the next line (its mark reads "(l. 75, l. 385, l. 403, l. 405, l. 409, l. 461)") turns on reason use, not on L383's first sentence.
- **The S81 case book (52 cases) and the S89 candidate cases (N1 to N25).** No case speaks of bearing, (K1) or a criticism occurrence. The only hit for "criticism" is N11 ("Two students, ten drafts each"), whose verdict turns on who made what is good in each essay, not on whether a criticism without bearing is a criticism.
- **The text's own passages.** None turns on L383's first sentence: L409 cites reason use; L429's "a conjectural objection" is a case the sentence allows.

## Dependents (named for the record; none is affected by a KEEP)

- L383, second sentence: "An adverse signal is not a criticism until an organization represents it as the premise of a criticism alleging a defect in a target." (the existence condition the first sentence leaves to it).
- L385, second sentence: "Using an objection does not give it bearing (K1) or make any argument from it usable (K2)." (the same separation, for use).
- L429: "A complete critical episode contains a recognized difficulty, a target available before its criticism, a conjectural objection, and a content-sensitive response." (an objection that may lack bearing).
- L201 and L13: "a selected transport has no represented target and no criticism in its history; a constructed one has both" (L201); "*constructed*, produced by an episode of conjecture and criticism" (L13): criticism in a history, whatever its bearing.
- L71 and L67, the commitments it makes precise: "A criticism has a target and is itself conjectural."; "Systems can be in error about their transports, their observations, their criticisms and their own capacities."

## Outside this item (not ruled here)

For the orchestrator only; nothing in this ruling rests on it.

- **File name.** Rule 11 of the reading rule names `results/S103 Round 1 - rulings/ruling C<nn> L<line>.md`; the task named `results/S103 Round 1 - reading/rulings/ruling C24.md`, and that path was used. No second copy was written.
- **A reader's citation.** GLM cites L267 among the lines that show the text's use of "fails"; L267 is the heading "## What (E) excludes, and what it does not". The tabulation's quotation check lists no quotation from it, so nothing there is affected.

## Parked (S34)

Nothing. No point of either reader on C24 proposes anything about what hard to vary covers, and this ruling proposes nothing about it.

## Quotations checked

Every quotation of file 99 above was compared by program with the line named (LaTeX delimiters as in the file); every quotation of a reader with the reply line named; the owner's words with `records/Semantics - Decisions.md`. The results are listed below.

- **File 99:** 32 quotations, each found on the line named: L13, L67 (four), L71, L169 (two), L201 (three), L220, L262, L267, L269, L277, L281, L317, L377 (two), L380, L383 (two), L385 (two), L393, L397 (two), L429 (two), L526, L606.
- **Readers:** Mimo, reply lines 102, 105 (two), 110, 116, 122 and 127; GLM, reply lines 48, 52 (two), 53 (three), 54 (two) and 56. Each found on the line named.
- **The owner's words:** "instantiation and transformation of information and knowledge" (S25) and "true, not true, more true" (S23), found in the record.
- **Other records:** the S96 mark "(l. 75, l. 385, l. 403, l. 405, l. 409, l. 461)", the S98 heading "L383.s1 · line 383 · no change recorded", the S100 row's "never challenged", the S98 change ids against L383.s2 (CH-0452, CH-0570, CH-0738, CH-1055, CH-1120) and the S89 case heading "N11 - Two students, ten drafts each", each found.
- No quotation of any book is made or copied here.

*Finished 27 September 2026. Ruling: KEEP.*
