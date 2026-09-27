# S103 Round 1 — ruling on C05 (L113)

*Written on 27 September 2026 by a fresh Opus 5.5 checker that built nothing of this round, read no reply before this task, and rules on no other candidate of it (rule 5 of `results/S103 Round 1 - how the replies will be read, written before sending.md`). This file obeys decision S23 except where it quotes the text, a reply or the owner. Nothing here is settled (S28).*

## The ruling

**KEEP.** Line 113, the second sentence of the line, stands as it is:

> The **signature** of component \(j\) on \(C\) is

**Mimo's rival is a rewording that changes nothing the theory needs from the sentence.** On this reading the sentence is easy to vary in its wording, in the plain sense of the brief (section 5, item 1: "If one works as well, say so: the sentence is then easy to vary on what the theory asks of it"), not in the text's defined sense (L317). That is recorded. What varies is the syntax of the lead-in only; the parts the sentence carries (the term, the component, the index "on \(C\)") are kept by the rival, and each reader shows a break where one of them is dropped or replaced. The rival is not adopted because it is not clearer than the text's wording (below). No FIX, so no case verdict moves and no sentence is affected.

## What was read

- **File 99**, `tests/99 The semantics, standing alone.md`, md5 74f4a4c7619345747f4fa976ddac9548 (checked before reading): L85–L127 (organizations, roles, "Kinds are edit-signatures"), L135–L147, L183, L245, L281, L287, L293, L347, L355, L520, L526, L548–L558 (Argument 1), and every line of the text that leads into a display. Not written to.
- **The brief**, part 1: C05's section (brief lines 121–129, which name as the definitions it uses "organization, component, footprint, L_j: L85–L105; contract: L141") and section 5, item 1 (brief line 419).
- **The tabulation**, `results/S103 Round 1 - reading/tabulation.md`: its C05 section, its list of passages naming a candidate outside its own section (none names C05), and its list of points alleging a defect (none for C05).
- **The replies**: `s103_vary_mimo_1.response.txt` line 1 (its standing note) and lines 98–119 (C05); `s103_vary_glm_1.response.txt` lines 1–3 and 91–110 (C05). No `.reasoning.txt` was opened. Neither reply names C05 elsewhere (searched).
- **The reading rule** named above; **decisions S20–S35** in `records/Semantics - Decisions.md` (md5 71459192867b1ebcf1bae914c9297129).
- **The S98 ledger**: L113.s2, "no change recorded"; no proposal on record against it. **The S101 graph**: L113.s2 sits under node 20, flagged as untouched in substance, with no record against it.

## The sentence and what the theory needs from it

The sentence is the lead-in to the display (K) at L115–L117 (C06). It follows C04 on the same line, "Fix an organization \(D\) and a contract \(C\subseteq A\times B\) (Part III).", which fixes the organization whose component \(j\) is meant (L91: "\(J\) indexes components; each component \(j\) has a footprint \(V_j\subseteq V\)") and types \(C\).

What the theory takes from it:

- **The term.** "Signature" is the word every later passage uses: L109 points forward to it ("that is, when the component assigning it has a measurement's signature (below)"); L119 builds "of one kind on \(C\)" from it; L121–L127 read the causal, measuring and rule families as "families of signatures"; L245, L281, L347, L520 ("Kinds, from signatures (K).") and Argument 1 (L554–L558) use it.
- **The component.** The signature belongs to a component \(j\), since (K) is built from \(L_j\), which "the interpretation supplies" (L91).
- **The index "on \(C\)".** It names in words the subscript of \(\operatorname{sig}_C(j)\), and it is the idiom of every later use: "of one kind on \(C\)" and "Kinds are therefore relative to the contract" (L119), "whose signature on \(C\) differs from its counterpart's" (L245), "a signature on \(\tau[C]\)" (L554); and "(K) depends on (O) and a contract" (L526).

## Each side (rule 7)

### Mimo: VARIES

Closing line (reply line 118): `C05: VARIES — For a component \(j\) of \(D\), its **signature** on \(C\) is`.

Mimo's argument: with (K) unchanged, the rival "Keeps the bold term, the component parameter, and the contract index L119 needs" and "Breaks nothing" (reply line 104). Dropping "on \(C\)" ("The **signature** of component \(j\) is") "breaks L119 and L526, and no longer matches the subscript in (K)" (line 110); putting "kind" for "signature" ("The **kind** of component \(j\) on \(C\) is") breaks L119, where a kind is a class built from signatures, and L558 (line 114). Fault check: "The lead-in carries only a term and two parameters. Nothing fails." (line 116).

### GLM: HOLDS

Closing line (reply line 109): "C05: HOLDS — rivals departed from the definitional display idiom shared with L97 and L141, or suggested a supply relation the text reserves for the interpretation's data (L91)."

GLM's argument: the wordings it tried, "The **signature** of component \(j\) on \(C\) is given by" and "Define the **signature** of component \(j\) on \(C\) as", "depart from the display convention by which the text marks a definition by form alone" (reply line 105), citing "The compatible valuations are" (L97) and "The answer profile is" (L141); "Is given by" also "quietly suggests a supplier, which the text reserves for the interpretation's data (L91: "the interpretation supplies")". Faults sought: none; "on \(C\)" is "load-bearing and correctly placed" (line 107), the idiom of L554 and L119.

### Between them

The readers do not contest the same wording. GLM's HOLDS rests on the wordings GLM tried; its argument, that they leave the bare "is" before the display, does not reach Mimo's rival, which keeps it. Mimo's VARIES rests on a wording GLM did not try. On what the sentence carries they agree: each takes "on \(C\)" as load-bearing and shows or names a break without it. So the ruling turns on one thing only: whether Mimo's rival changes anything the theory needs, and, if not, whether it is clearer.

GLM's idiom argument, compared with the text, is weaker than stated. The text leads into its displays in more than one way: "An organization is" (L85), "The compatible valuations are" (L97), "A question is" (L135), "The answer profile is" (L141) and "A transport from an organization \(D\) to an organization \(E\) is" (L183), but also "Define" (L287), "For nonempty \(B\subseteq W\)," (L293) and "For \(R\subseteq Z_D\times Z_E\), forward preservation is" (L355). "Define … as" would not break a convention the text keeps everywhere, and "is given by" in mathematical prose reads as "equals" at least as readily as it suggests a supplier. Since no one proposes either of GLM's wordings, this bears only on how much GLM's HOLDS rests on, and a HOLDS records only the wordings tried (Mimo's standing note, reply line 1; S28).

## The rival: a rewording, not a different claim

Mimo's rival keeps the bold term, the component \(j\), the index "on \(C\)" and the bare "is" before (K), and leaves (K) as it is. Its one addition is "of \(D\)". In the text, component \(j\) already belongs to \(D\): the sentence before it fixes \(D\), and \(J\), the footprints and the relations \(L_j\) are \(D\)'s data (L91). So "of \(D\)" states in words what the text already carries.

Does "of \(D\)" narrow the definition where the text applies it to another organization? L119 speaks of "A component of \(E\) and a component of \(E'\)" whose "signatures, read on \(C\) through \(\tau\) and \(\tau'\), coincide under a footprint bijection"; L554 of "no active component \(k\) of \(E\)" with "a signature on \(\tau[C]\)"; L556 writes \(\operatorname{sig}_{\tau[C]}(k)=\{(\tau(a),\sigma(b),L_k(\tau(a),\sigma(b)))\}\). These read (K) with \(E\) in the place of \(D\) and \(\tau[C]\) in the place of \(C\). Under the text's wording, "Fix an organization \(D\)" makes \(D\) stand for any organization; under the rival, "of \(D\)" names that same organization, so the same reading goes through. Nothing moves.

The counterpart \(\lambda(k)\) is "a subnetwork of \(D\)" (L119), not a component, and L556 writes "By (K), \(\operatorname{sig}_C(\lambda(k))=\{(a,b,\operatorname{proj}^{\lambda}_{V_k}\operatorname{Sol}_{\lambda(k)}(a,b))\}\)". Neither the sentence nor the rival speaks of subnetworks; L119 gives the reading ("its counterpart \(\lambda(k)\), read on \(C\) directly with its hidden ports projected away, up to the port translation"). The sentence and the rival stand alike on this, so it does not separate them. (Recorded for the orchestrator as outside this candidate: whether L556's "By (K)" for a subnetwork needs a word is a matter for L119 and L556, not raised by either reader. Widening this sentence to subnetworks would be a different claim and would move L119's "A kind is an equivalence class of components under this relation"; it is not ruled here.)

So the rival is a rewording that changes nothing the theory needs from the sentence.

## Why KEEP, and not the rival

Rule 5: for a rewording, FIX only if the rival is clearer. It is not, for these reasons, each a reason why the text's wording and not Mimo's:

- **"of \(D\)" adds words and no content.** It repeats what the sentence before it, on the same line, has just fixed.
- **It gives a slight cue in the wrong direction.** From Part III on, \(D\) names the target ("\(D\) is the target", L141) and \(E\) the candidate's organization, and L119, L245 and L554–L556 apply signatures to components of \(E\). An explicit "of \(D\)" gives a reader who meets \(\operatorname{sig}_{\tau[C]}(k)\) at L556 one more cue to take signatures as defined for the target's components only; the unqualified "component \(j\)" under "Fix an organization \(D\)" leaves nothing extra to undo. The effect is slight, but it counts against the rival, not for it.
- **The text's wording has the shape of the text's other named definitions at the head of a passage**: the object named first, then "is" or "are", as in "The compatible valuations are" (L97) and "The answer profile is" (L141). The rival puts a quantifier phrase first and the bold term after it. L355 shows the text also uses the rival's shape, so the rival is not unclear; it is only not clearer.

No third wording is proposed: no reader shows an unclarity in the sentence for one to remove.

## The variations and what they break

- **"The **signature** of component \(j\) is"** (Mimo, reply line 108). The display would still carry \(C\) in its subscript, so (K) itself would stand; what breaks is the agreement between the words and their display, and the idiom of every later use in words: "of one kind on \(C\)" and "Kinds are therefore relative to the contract" (L119), "whose signature on \(C\) differs" (L245), "a signature on \(\tau[C]\)" (L554). Mimo's break stands, in this narrower form: the loss is to the words, not to (K)'s content. GLM's fault search names the same load ("it cannot be dropped without losing the contract-relativity the section goes on to state", reply line 107).
- **"The **kind** of component \(j\) on \(C\) is"** (Mimo, reply line 112). A kind would become a set of triples, against "A kind is an equivalence class of components under this relation" (L119) and "Kinds, from signatures (K)." (L520), and "kind" would become a defined term the account cannot do without, against "The word "kind" is therefore eliminable from the definition of an account, and its elimination loses no case." (L558). Mimo's break stands.
- **"… is given by"** and **"Define … as"** (GLM, reply lines 96 and 102). Weighed above: they are rewordings as well, and they depart from the sentence's shape less than GLM says; no one proposes them, and neither is clearer than the text's wording.

## The points that allege a defect

None. Neither reader alleges a fault in the sentence, and the tabulation lists no defect point for C05. Sought here as well: the sentence is a lead-in completed by (K), so its "is" is not left open; its term is used once before it, at L109, with a forward pointer "(below)", not a circle; its index \(C\) is typed by C04. No fault is shown.

## The owner's decisions

KEEP writes nothing new. The sentence holds no word or idea S23 forbids and no physical possibility (S25–S27); it says nothing about what must happen to candidates (S21) and nothing about what hard to vary covers (S33–S34; parked: nothing, since no point of either reader proposes anything about it). It does not touch the placement of values. This ruling uses no count of rivals or of readers (S20; rule 7) and settles nothing (S28).

## Cases

A KEEP moves no case verdict. The cases the text ties to this sentence's term were read: grievance 1, cause and correlation (L37: "which is what the semantics asks about (Part II, "Kinds are edit-signatures")"); grievance 11, a rule and a cause (L57: "That is a difference in edit-signature (Part II)"); the kind condition set aside at L245 and L281; the rule relation at L347; and Argument 1, whose consequence says of "kind" that "its elimination loses no case" (L558). The S98 ledger ties no case and no proposal to L113.s2. Had Mimo's rival been applied, none of these would move either, since (K) and every use of "signature on \(C\)" would be as they are.

## Quotations compared with file 99

Every quotation of file 99 above was compared with the file: L37, L57, L91, L97, L109, L119, L141, L183, L245, L287, L293, L355, L520, L526, L554, L556 and L558 as quoted here; the readers' quotations of L97, L141, L91, L119, L554 and L558, found where they cite them (as the tabulation also records). No book is quoted.

## Where this file stands

Written to the task's path, `results/S103 Round 1 - reading/rulings/ruling C05.md`. The reading rule, rule 11, names `results/S103 Round 1 - rulings/ruling C<nn> L<line>.md`; the difference is the orchestrator's to settle. Not committed.

## Result

- **old** (L113): The **signature** of component \(j\) on \(C\) is
- **new** (L113): The **signature** of component \(j\) on \(C\) is
- **ruling:** KEEP
- **easy to vary:** yes, in wording, on this reading: Mimo's rival is a rewording that changes nothing the theory needs; not adopted, since it is not clearer.
