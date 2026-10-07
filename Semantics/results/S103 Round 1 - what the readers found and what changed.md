# S103 Round 1 — what the readers found and what changed

*Written on 27 September 2026 by a Claude subagent (Opus 5.5), the records step of the round's reading, from the files named below; it read no reasoning file and ruled on nothing. The text under review is `tests/99 The semantics, standing alone.md` (md5 74f4a4c7619345747f4fa976ddac9548, checked before and after writing; not written to). The new text is `tests/103 The semantics, standing alone, after round 1.md` (md5 f31ebb1f050783f1a84f6136cec20fcd). Every quotation of file 99, file 103 and the replies here was compared by program with its source (`results/S103 Round 1 - reading/records - quotation check.py`). This file obeys decision S23 except where it quotes the text, a reply, a ruling or the owner. Nothing here is settled (S28): a KEEP is a sentence that stood under this round's attempts, not thereby final, and a FIX is a new wording open to the next round.*

## In brief

- **What was asked.** Round 1 of the review rounds of decision S35 ("Keep reviewing, editing, testing, updating until there are no moves left"). Mimo and GLM were each given the 29 strong candidates that had never been challenged (S100), C01 to C29, in three parts, and asked for each to try to vary it: rival wordings that keep what the theory needs, variations and what they would break, failures of the sentence itself, and one closing line `Cnn: HOLDS`, `VARIES` or `FAILS`.
- **What came back.** All six replies, each accepted on pass 1 at its first attempt. Every candidate was examined by both readers.
- **The rulings.** Every one of the 29 went to a fresh Opus 5.5 checker of its own: **25 KEEP, 4 FIX, no DROP.** The FIXes: C07 (line 123, the causal assignment), C27 (line 443, the explanatory aim), C28 (line 471, (CT2)) and C29 (line 520, the Account gloss).
- **Easy to vary, in the brief's plain sense and on this reading** (never the text's own term at L317; nothing here is about what hard to vary covers, S34): on 17 candidates a reader's rival was ruled a rewording that changes nothing the theory needs (C01–C05, C07–C12, C19, C21, C24–C26, C28). One of those rivals was clearer and was taken (C28); the other sixteen were not, so the text's wording stayed (for C07 the FIX came from another point). On five, a reader's rival was ruled a different claim and weighed as a challenge (C13, C15, C20, C22, C23; C20 is a rewording only on a narrow reading). On six more, the checkers recorded smaller re-spellings that say the same (notation, a synonym, a spelling of a concession, one phrase): C06, C14, C16, C17, C18, C29. C27 was a shown fault, not a question of varying.
- **The critical review** (Fable 5.1) read all 29 rulings and objected to none. Nothing was re-checked.
- **Applied** by program to a new copy, file 103: four lines differ from file 99 (123, 443, 471, 520); every scan passes.
- **Cases.** Every case that could turn on the four lines was re-read on both texts: **none moves**.
- **Parked.** No candidate. GLM's standing note on what counts as a variation is recorded as parked in so far as it bears on what hard to vary covers (rulings C19 and C20); nothing rests on it and nothing was applied from it.
- **Moves: 4.** So the series does not end (rule 14): round 2 goes to file 103, under its own reading rule, written and committed before sending.

These counts describe the work. They order nothing and grade nothing (S20); each ruling was made on its arguments, not on how many readers stood on a side (rule 7).

## What was examined and asked

- **The text:** file 99, 632 lines (16,366 words by `wc -w`; 16,394 by whitespace split). The reading rule mapped each candidate to file 99 by program; none had moved from its line in the latest text.
- **The briefs**, the same three to both readers, built and checked by `tools/s103_build.py`: part 1, C01–C12 (Part 0 and Part II; 6,800 words by the runner's count; md5 9c46307c5dc62368327e8a34c184a83d); part 2, C13–C20 (Parts III and IV; 6,546; 387f826f93ba0922458007feefc6bd61); part 3, C21–C29 (Parts V to XIV; 7,677; 44ef4fbdb179963c3e76fcdaf60ecf27). Each carried the owner's words of S20, S21, S23, S25–S28, S33 and S34, each candidate with the lines around it and the definitions it uses, and the task. "Easy to vary" was to be read plainly, not as the text's own term (L317); nothing about what hard to vary covers was asked (S34).
- **The reading rule**, `results/S103 Round 1 - how the replies will be read, written before sending.md`, committed with the briefs before anything was sent (3c7806a, 12:38 UTC).

## Receipts

Both runs were launched at 12:39:02 UTC on 27 September. Nothing was opened before both were over (rule 1): the Mimo log ends `loop ended 2026-09-27T14:14:58Z`; the GLM log ends `s103_glm_loop: every pass ended; accepted 3 of 3 parts` and then `loop ended 2026-09-27T12:52:50Z`. The replies were committed unread (b516968). Only the `.response.txt` files were read for arguments. The tabulator and the critical reviewer record that they opened no `.reasoning.txt` file; 26 of the 29 rulings say the same, and the other three (C06, C13, C17) say nothing either way and cite only reply lines; this recorder opened none (of the receipts it read only the fields given below).

| tag | part | back (UTC) | attempts | what the receipt records | reply words (`wc -w`) |
| --- | --- | --- | --- | --- | --- |
| s103_vary_mimo_1 | 1 (C01–C12) | 13:03:32 | pass 1, attempt 1 | mimo-v2.6-pro; `finish_reason` "stop", `saw_done` true, accepted, status 200; 71,980 output tokens (67,849 of them reasoning) of the 131,072 ceiling | 2,440 |
| s103_vary_mimo_3 | 3 (C21–C29) | 13:32:07 | pass 1, attempt 1 | as above; 77,995 output tokens (73,606 reasoning) | 2,525 |
| s103_vary_mimo_2 | 2 (C13–C20) | 14:14:57 | pass 1, attempt 1 | as above; 102,970 output tokens (99,631 reasoning) | 1,884 |
| s103_vary_glm_1 | 1 (C01–C12) | 12:43:49 | pass 1, attempt 1, 0 connection failures | glm-5.3 via Claude Code, effort medium, 286.1 s; accepted ("the reply's last non-blank line carries END OF REPORT"); `brief_md5` 9c46307c… | 2,880 |
| s103_vary_glm_2 | 2 (C13–C20) | 12:48:21 | pass 1, attempt 1, 0 connection failures | as above, 272.6 s; `brief_md5` 387f826f… | 2,156 |
| s103_vary_glm_3 | 3 (C21–C29) | 12:52:50 | pass 1, attempt 1, 0 connection failures | as above, 268.3 s; `brief_md5` 44ef4fbd… | 2,482 |

Mimo ran one call at a time (its slot limit of 1, from decision S35), in the order 1, 3, 2. Each Mimo request's user message hashes to the sha256 of its part brief; every reply's last non-blank line is END OF REPORT, and every `response_sha256` in a receipt equals the file's hash (the tabulation, "Receipts"). Mimo's part 2 used about 79 per cent of the output ceiling, mostly on reasoning; a part of that size is near the limit for the next round (lesson S20).

## How the reading ran, and where it departs from the reading rule

- **Tabulation (rule 4):** one fresh Opus 5.5 agent that built nothing of this round, `results/S103 Round 1 - reading/tabulation.md` (3,053 lines; finished 14:36 UTC). It copied every closing line and written-out wording by program with its reply line, digested every point, and found every quotation of file 99 or of the owner's words that either reader relies on; one was cited to another line (GLM at C21: "it fails (F1)" cited as L267, found at L269). It ruled on nothing.
- **Checkers (rule 5):** 29 fresh Opus 5.5 checkers, one per candidate, each ruling on no other. Their files finished between 14:43 and 16:21 UTC. **Departure:** under rule 6 the tabulation held C06, C14, C16 and C17 (both readers HOLDS, no point showing a defect) and sent them to no checker; the workflow sent every candidate to a checker, these four included. That is more checking than rule 6 asks, not less; each of the four was ruled KEEP and is also recorded, as rule 6 asks, "held under both readers' attempts; not thereby final". C18, held by both readers, went under rule 5's clause on doubt (Mimo's step 3 on the extent of "fidelity"). Rule 5 also says the checkers run at most five at a time; the records of this round hold no count of how many ran at once, so whether that limit was kept is not shown here.
- **Critical review (rule 12):** one review by Fable 5.1, written before anything was applied (finished 16:32 UTC). No objection, so no second checker was needed (the "Re-check" step ran on nothing).
- **Applying (rule 13):** one Opus 5.5 agent wrote `results/S103 Round 1 - reading/apply.py`, which checks file 99's md5, refuses any old span that is missing or ambiguous on its line or in the whole text, compares each FIX's old and new wording byte for byte with its ruling, keeps the text one line to one line, and never writes over a different existing output (a rerun reported "already present, identical"; the run's output is saved beside it as `apply - output.txt`). It imports the S95 and S96 scan scripts unchanged. Then a fresh Opus 5.5 case checker re-read the cases (`results/S103 Round 1 - reading/cases.md`).
- **File names (departure, lesson S19):** the rulings stand at `results/S103 Round 1 - reading/rulings/ruling Cnn.md`, not at rule 11's `results/S103 Round 1 - rulings/ruling C<nn> L<line>.md`; the tabulation at `results/S103 Round 1 - reading/tabulation.md`, not rule 4's `results/S103 Round 1 - tabulation of the replies, before any ruling.md`; the critical review at `results/S103 Round 1 - reading/critical review.md`, not rule 12's `results/S103 Round 1 - critical review of the rulings.md`. The workflow named these paths; every agent noted the difference; no second copy was made. They stay where they are, and every record points to them there.
- **Work-in-progress commits.** 2e7d8cf (15:28 UTC) and d34c929 (15:34) saved the files then written, among them early stubs of the rulings on C16, C17 and C18 that their own checkers then filled in. The finished files replace only those stubs; no finished ruling was written over.
- **Quotations (rule 10):** no reply quotes a book. The checkers compared their quotations of file 99 and the replies by program. The C28 checker read one outside web page on how the name "post-fixed" is used; it is not a book.

## Candidate by candidate

For each: the sentence in file 99 as the briefs give it, byte for byte; each reader's closing line as written, with its reply line; the ruling; whether it was found easy to vary in the plain sense, on this reading; and the reasons, in short. The full reasons are in each ruling file, `results/S103 Round 1 - reading/rulings/ruling Cnn.md`. Where a closing line carries backticks (every Mimo line in parts 1 and 2, and three GLM lines), they are the reply's own.

### C01 · L27 — KEEP

> It defines the classes.

- Mimo (`s103_vary_mimo_1`, line 26): `` `C01: VARIES — It does define the classes.` ``
- GLM (`s103_vary_glm_1`, line 27): `C01: HOLDS — every rival either blurred the define/decide contrast or downgraded the classes from defined (L528) to described.`
- **Ruling: KEEP.** Easy to vary: Yes, in wording (recorded): Mimo's rival is a rewording that changes nothing the theory needs. Not clearer, so not taken.

The readers differ (rule 7). Mimo's "It does define the classes." only adds emphasis; it is not clearer: the emphatic "does" answers a doubt nothing on the line raises, can read as a concession, and breaks the plain pattern, a denial answered by "It defines …", that L21 sets for the section ("It does not define reference in terms of uninterpreted matter. It defines reference in terms of matter **plus a selection or construction history**."). GLM's variations change the claim and each loses something the text uses: "fixes" blurs define against decide and leans toward settling (S28); "says" drops the classes' place among what the document defines (L29, L520, L526); "the class" loses the plural that L27's "the classes defined" and L528's five classes carry; "decides" goes against the line's own first sentence, L632 and L8. Mimo's fault check ("a role, not new content") shows no idle part: the first sentence's "the classes defined" has no agent, and this sentence supplies it, as L21, L23 and L25 do for theirs.

### C02 · L41 — KEEP

> Survival is how the transport got there; fidelity is what it is.

- Mimo (`s103_vary_mimo_1`, line 48): `` `C02: VARIES — Survival is how the transport got there; fidelity is what the transport is on the contract.` ``
- GLM (`s103_vary_glm_1`, line 47): `C02: HOLDS — rivals lost the grip on the grievance's word "survival" or miscast survival against L193/L195; the compression is licensed in context.`
- **Ruling: KEEP.** Easy to vary: Yes, in wording (recorded). Not clearer, so not taken.

Mimo's rival adds "the transport" and "on the contract"; both are already fixed, the first by the parallel with "how the transport got there", the second by L31 and L43 ("Within any contract, whether a transport is faithful at a pair turns on the transport and the target"). It clears up nothing that is unclear now, and "what the transport is on the contract" can be read as fidelity being the transport as restricted to \(C\), which drops the target that fidelity compares ((F1), (F2)); "the contract" also has no antecedent inside grievance 3. GLM's rivals, which GLM itself set aside, change the grievance's own word "survival" or the contrast between how the transport got there and what it is. Mimo's points on "it" (read as "fidelity", or read without a contract) are closed by the parallel and by L31 and L43; the "it is what it is" reading claims nothing settled and stays inside S28.

### C03 · L47 — KEEP

> Construction is a separate provenance with a separate trace, and every creative attribution requires it.

- Mimo (`s103_vary_mimo_1`, line 74): `` `C03: VARIES — Constructed correspondence is a separate provenance with a separate trace, and every creative attribution requires construction.` ``
- GLM (`s103_vary_glm_1`, line 73): `C03: HOLDS — rivals broke L199/L13 (declared transports), the attribution unit (G) at L422/L528, or the provenance classification at L193.`
- **Ruling: KEEP.** Easy to vary: Yes, in wording (recorded). Not clearer, so not taken.

The readers differ (rule 7), and GLM's argument stands. Mimo's charge that "is a separate provenance" is loose against L193 does not hold: the body itself uses the noun for construction and selection ("Neither provenance is reducible to the other", L201; "the two provenances", L542). Mimo's rival is not clearer: its subject "Constructed correspondence" makes a relation a provenance, against L13 ("It is a **relation with a provenance**"), and it has to spell out "construction" only because of that change of subject. Of the variations the readers said would break, one of Mimo's reasons is not shown (that a contract has no transport, L425: Build yields a representation, L405, and a representation is a transport, L205); that variation still breaks, on L193 and on (G) at L422. Every attribution the text calls creative contains (G) and so Build (L429, L447–L448, L528, L592).

### C04 · L113 — KEEP

> Fix an organization \(D\) and a contract \(C\subseteq A\times B\) (Part III).

- Mimo (`s103_vary_mimo_1`, line 96): `` `C04: VARIES — Take an organization \(D\) and a contract \(C\subseteq A\times B\) (Part III).` ``
- GLM (`s103_vary_glm_1`, line 89): `C04: VARIES — Let \(D\) be an organization and \(C\subseteq A\times B\) a contract (Part III).`
- **Ruling: KEEP.** Easy to vary: Yes, on both readers' rivals (recorded). Neither clearer, so not taken.

Both readers close VARIES, with different rivals, and agree that only the verb is free. "Take" is never a set-up verb in file 99: the text uses it for adopting and for premises taken as given (L75, L397), and six lines on for the values ports take (L119). "Let" is as plain as "Fix" but gives up the text's own idiom for holding named objects while others range (L287, L369) and reverses the noun-then-symbol order; its only gain, against reading "fix" as "repair", is idle, since file 99 never uses "fix" that way. Mimo's point that the typing is the sentence's "only strict content" shows no idle part: the sentence also names \(D\) and \(C\) as the parameters that (K), L119 and L121–L127 are indexed to. The break the readers named for "a set C of changes" is a loss of the word "contract", its index and the pair typing, not a contradiction of L141 (L159 itself calls a contract's members changes). Noted for the next round, not ruled: Argument 1 reads (K) on \(\tau[C]\) (L556), a reading that comes from L119, not from this sentence.

### C05 · L113 — KEEP

> The **signature** of component \(j\) on \(C\) is

- Mimo (`s103_vary_mimo_1`, line 118): `` `C05: VARIES — For a component \(j\) of \(D\), its **signature** on \(C\) is` ``
- GLM (`s103_vary_glm_1`, line 109): `C05: HOLDS — rivals departed from the definitional display idiom shared with L97 and L141, or suggested a supply relation the text reserves for the interpretation's data (L91).`
- **Ruling: KEEP.** Easy to vary: Yes, in wording (recorded). Not clearer, so not taken.

The readers do not contest the same wording: GLM's HOLDS rests on the rivals GLM tried ("is given by", "Define … as"), and its idiom argument does not reach Mimo's rival, which keeps the bare "is"; it also overstates how uniform the text is (L287 uses "Define"; L293 and L355 use Mimo's "For …," shape). Mimo's "of \(D\)" adds words and no content (L113's "Fix an organization \(D\)" and L91 carry it), gives a slight cue toward reading signatures as defined only for the target's components, while L119, L245 and L554–L556 apply them to components of \(E\), and gives up the shape of L97 and L141, a definite noun phrase followed by "is". Dropping "on \(C\)" or putting "kind" for "signature" breaks the lines the readers name (L119, L245, L554; L520, L558). Noted for the next round, not ruled: L556 writes "By (K)" of \(\lambda(k)\), a subnetwork, not a component; L119 gives how to read that.

### C06 · L115–L117 — KEEP

> \[
> \operatorname{sig}_C(j)=\{(a,b,L_j(a,b)):(a,b)\in C\}. \tag{K}
> \]

- Mimo (`s103_vary_mimo_1`, line 150): `` `C06: HOLDS — each variation above loses a named clause of L556, L119 or L57.` ``
- GLM (`s103_vary_glm_1`, line 135): `C06: HOLDS — the graph form is used verbatim at L556 and acted on by L119; function-form, coordinate-free, and baseline rivals each broke a named use.`
- **Ruling: KEEP.** Easy to vary: In notation only (recorded): two rivals name the same object. Neither clearer.

Both readers close HOLDS, and the tabulation held it under rule 6; the workflow sent it to a checker as well (see "How the reading ran"). Mimo's restriction \(L_j|_C\) and GLM's function form name the same object as (K); neither is clearer: the first hides the triples L556 writes out, and the second's codomain binds \(j\) twice and leaves \(a\) and \(b\) free. Every rival that changes what (K) says breaks a named use: dropping which pair each relation answers merges components whose relations are swapped across edits (L11, L281, L123–L125); adding the footprint is idle or bars every cross-footprint kind (L119, L564); a solution-based form uses port values that L119 excludes (and L124, L109, L127); a baseline form loses contract relativity (L119) and merges cause with measurement (L37, L123–L124). The checker's own search found the display defined at every pair of \(C\) (L91, L94), not circular, every part used, and the kind relation an equivalence as L119 asks. Recorded as held under both readers' attempts; not thereby final.

### C07 · L123 — FIX

> - a **causal assignment** has a signature that changes under intervention on its output port and under replacement of the component, and is invariant under observation edits;

- Mimo (`s103_vary_mimo_1`, line 176): `` `C07: VARIES — - a **causal assignment** has a signature that moves when an edit sets its output port or replaces the component, and that observation edits leave unchanged;` ``
- GLM (`s103_vary_glm_1`, line 161): `C07: HOLDS — polarity and port swaps broke L127, L37, and L103's replacement structure; dropping the replacement clause untied the assignment from the component.`
- **Ruling: FIX.** Easy to vary: Yes, in wording, on Mimo's rival (recorded); the rival is not clearer and is not taken. The FIX comes from Mimo's fault check, not from its rival.
- **Old (L123):** `- a **causal assignment** has a signature that changes under intervention on its output port and under replacement of the component, and is invariant under observation edits;`
- **New (L123):** `- a **causal assignment** has a signature that changes under intervention on its output port and is invariant under observation edits;`

The readers differ on whether "and under replacement of the component" does any work (rule 7). Mimo: "Inertness, not contradiction" (reply `s103_vary_mimo_1`, line 174). GLM: dropping it "untied the assignment from the component" (line 161). The checker rules with Mimo's fault check. By L103, "An edit that sets a port replaces the component assigning that port", so an intervention on a component's output port is itself a replacement of that component, and clause 1 already carries a replacement under which the signature changes; any other replacement changes any component's signature, since the signature is built from the component's relation (L116, L119). So the clause marks no family off from another. A measurement is still kept out by clauses 1 and 3 together: setting a reading is an observation edit (L109). GLM's defence does not hold: the replacement clause is as positional as clause 1, and L57 names editing as the rule's mark, not the cause's. On one further reading the clause is not idle (the contract must hold a change of mechanism other than the intervention), but no passage asks that, and neither the text's production case (L325) nor case O9 has one. The new wording is GLM's own variation at reply line 154, byte for byte (Mimo's line 172 differs only by a comma). No sentence of file 99 relies on the deleted clause (L37, L57, L127, L151, L269, L325 read as before).

### C08 · L124 — KEEP

> - a **measurement** has a signature invariant under interventions on the measured port and variable under edits to the measuring relation;

- Mimo (`s103_vary_mimo_1`, line 198): `` `C08: VARIES — - a **measurement** has a signature that interventions on the measured port leave unchanged and edits to the measuring relation change;` ``
- GLM (`s103_vary_glm_1`, line 187): `C08: HOLDS — polarity swap broke L127; tracking idiom broke L109's definitional use; "observation edits" would circle with L109.`
- **Ruling: KEEP.** Easy to vary: Yes, in wording (recorded); its content is not easy to vary. Not clearer, so not taken.

Mimo's rival changes only the idiom ("leave unchanged" and "change" for "invariant under" and "variable under"); under (K) both say the same of the signature. It is not clearer: it would split L121's list across two idioms, while L125 and L347 keep the text's ("invariant under interventions on \(Z\) and variable under edits to \(C_r\)", L347), and its closing bare "change;" can first be read as intransitive. Every variation of content broke L109 or L127: the role swap, the polarity swap, GLM's value-tracking wording, and GLM's "observation edits" wording, which asks one signature to stay and to vary under the same edits. Mimo's point that the second clause, like C07's replacement clause, applies to any component shows no defect: dropping it breaks L109 ("A port is an **observation** when \(A\) contains an edit that alters the relation reporting it without altering what it reports"), so it does work. The C08 checker added that the same held of C07's clause "on Mimo's own comparison" and left it to C07's checker; the C09 ruling and the critical review give why the two differ (below, and "What the critical review changed"). Noted, not ruled: L109 gives roles "under \(A\)", while signatures are built on a contract \(C\).

### C09 · L125 — KEEP

> - a **rule application** has a signature invariant under interventions on the world and variable under edits to the rule.

- Mimo (`s103_vary_mimo_1`, line 220): `` `C09: VARIES — - a **rule application** has a signature that interventions on the world leave unchanged and edits to the rule change.` ``
- GLM (`s103_vary_glm_1`, line 207): `C09: HOLDS — rivals lost the world/rule contrast of L57 and L347, or conflated the rule family with the observation notion defined at L109.`
- **Ruling: KEEP.** Easy to vary: Yes, in wording (recorded). Not clearer, so not taken.

Mimo's rival changes only the idiom, as in C08. It is not clearer: the text's wording repeats L347's predicate word for word, which shows at a glance that L347 is the bullet's formal instance; it would break the idiom shared with L124 while claiming nothing different; and "edits to the rule change" invites an every-edit reading that "variable under" does not, while L119 allows edits under which relations stay equal. GLM's variations each break what GLM names, or more: dropping the world side breaks L57 and L347, and L103 and L119 too; swapping the polarities reverses L57 and L347 and conflicts with L103 ("A changed rule is a changed component."). GLM's further claim that the "observation edits" wording mixes "the two families L127 keeps apart" does not hold: L127 contrasts a reading part with the part it reports, not a measurement with a rule. Mimo's fault points show no failure: "the world" has its formal reading \(Z\) at L347; the second clause is not inert as C07's is, because C09's first clause is an invariance, met by any component the contract never edits, so the second clause is what asks the contract to hold an edit to the rule; and that C08 and C09 share one profile shape under (K) is the pattern L11, L119 and L127 describe, while L121 does not say the families are disjoint. Noted, not ruled: L121 names four things and gives three bullets; by L347 the rule bullet covers a rule and a constitutive status.

### C10 · L127 — KEEP

> These are descriptions of patterns in (K), not additional data.

- Mimo (`s103_vary_mimo_1`, line 242): `` `C10: VARIES — These describe patterns in (K); they add no data.` ``
- GLM (`s103_vary_glm_1`, line 233): `C10: HOLDS — "derived" is forbidden (S23), "consequences" overclaims against L558 and L11, "inputs" collides with the defined port notion at L109.`
- **Ruling: KEEP.** Easy to vary: Yes, in wording (recorded). Not clearer, so not taken.

Mimo's "These describe patterns in (K); they add no data." keeps both halves. It is not clearer: it gives up the text's "X, not Y" form, the form of "Roles are defined, not supplied" (L107), "Representation is defined, not supplied" (L203) and "stated, not defined" (L526), and "they add no data" can be read more loosely, as "they contribute nothing", while L109 and the rest of L127 use the families. GLM's rivals are not rewordings: "derived from" is out on S23; "consequences of (K)" is a different claim, since (K) alone yields no family (which family a signature falls in depends on the supplied relations, L91, and on the contract, L119); "not additional inputs" collides with the input port of L109 and the declared inputs of L522. The two closing lines do not contradict each other: GLM's reply never meets Mimo's rival.

### C11 · L127 — KEEP

> The semantics never asks whether a component "is" a cause.

- Mimo (`s103_vary_mimo_1`, line 264): `` `C11: VARIES — The semantics never asks an "is a cause" question of a component.` ``
- GLM (`s103_vary_glm_1`, line 253): `C11: HOLDS — rivals weakened the L11 parallel and its level-relativity, or destroyed the ask/ask structure that carries into the next sentence.`
- **Ruling: KEEP.** Easy to vary: Yes, in wording (recorded). Not clearer, so not taken.

Mimo's rival names the same question, kept apart by quotation marks. It is not clearer: it loses the word-for-word echo of L11 ("The definition never asks whether a piece of the explanation "is the same kind of thing" as a piece of the world."), the contrast between the scare-quoted "is" and the next sentence's plain "what its signature is", and some plainness; quoting the whole predicate also puts "cause" in quotation marks, though the text uses the word plainly (L37, L57, L121). GLM's rivals fail as GLM says: "does not ask" loses the echo of L11; "contains no predicate" turns the sentence into a claim about vocabulary, orphans the next sentence's "asks", and drops L600's "undefined", so it runs against the defined causal family at L123. The two readers tried different wordings and do not contradict each other. No conflict with "causal precedence" (L375, a relation among occurrences) or with "what caused this?" (L277, a production question).

### C12 · L127 — KEEP

> It asks what its signature is.

- Mimo (`s103_vary_mimo_1`, line 286): `` `C12: VARIES — It asks what the component's signature on \(C\) is.` ``
- GLM (`s103_vary_glm_1`, line 269): `C12: VARIES — It asks what its signature on \(C\) is.`
- **Ruling: KEEP.** Easy to vary: Yes, on both readers' rivals (recorded). Neither clearer, so not taken.

Both close VARIES with rivals one word apart, each adding "on \(C\)". The text defines no signature without a contract (L113, L116, L119), so "on \(C\)" writes out what the defined term already carries, as both readers say. Neither is clearer: an index here would make this the only indexed use in L121–L127, beside five unindexed uses under the same fixed \(C\), and so mark a difference that is not there; where the text does write the index (L119, L245, L554, L626), it marks something the context does not carry. Of the variations offered as breaking: "what kind the component is" asks for the defined thing in place of what defines it (L119, L558, L11) and brings back the "is" question the previous sentence turns away; "its signature on the history" breaks against L119 and the split L41 and L572 keep between survival and fidelity (not at L67, which is about assessors); "how it responds to changes" loses the defined term and its index but contradicts nothing. Noted: this sentence and the previous one are a pair; L584 uses "signature" in the everyday sense.

### C13 · L161 — KEEP

> A question may fail to pick out its alleged target, assume an incompatible baseline, or combine incompatible requirements.

- Mimo (`s103_vary_mimo_2`, line 25): `` `C13: VARIES — A question may fail to pick out its alleged target, assume a baseline incompatible with its remaining terms, or combine requirements that cannot be met together.` ``
- GLM (`s103_vary_glm_2`, line 25): `C13: HOLDS — every rival either presupposes a target ("wrong about", "miss"), imports physical impossibility against S25/S26 and L159, or collapses the three distinct failure modes into one graded verdict.`
- **Ruling: KEEP.** Easy to vary: Not shown easy to vary: Mimo's rival is a different claim, weighed as a challenge and not taken.

GLM's HOLDS stands, on a ground other than the one it cites. Mimo's first change ("a baseline incompatible with its remaining terms") narrows what the baseline can be incompatible with to the question's own parts. The text leaves that open here and states it where the defect is exposed: the next sentence but one, and L377 ("A criticism has target \(z\), alleged defect \(\delta\), premise \(g\), and a connection"), whose premise may be a claim taken as given (S27; S28 "That "ruling out" is a choice that was made."; S21 "The problem may, for whatever reason, be ill posed."). "Terms" is also not the text's word for a question's parts. Mimo's second change ("requirements that cannot be met together") keeps the claim but is not clearer: it swaps the text's structural word (a compatible valuation, (O) at L97–L100; the empty solution set at L257) for a modal of unstated kind, opening a reading on which the question is whether anyone could meet them, which L159 and L75 keep out of a question (S25, S26). Both readers' breaks ("must", "identify", "wrong about", "physically impossible change") stand, and both say "alleged" does work. GLM's closing line names a rival with "miss" that its section never gives.

### C14 · L161 — KEEP

> Its formulation is still an event.

- Mimo (`s103_vary_mimo_2`, line 50): `` `C14: HOLDS — every change of "event" breaks L55, L397, L592 or S23, and dropping the concession loses the error case.` ``
- GLM (`s103_vary_glm_2`, line 47): `C14: HOLDS — every rival severs the tie to "event" at L397, L55 and L604, or drops the concession that a defective question still counts.`
- **Ruling: KEEP.** Easy to vary: Only in how the concession and the act are spelled (recorded); not in what the sentence claims. Neither re-spelling clearer.

Both readers close HOLDS, and the tabulation held it under rule 6 (with a note that the orchestrator might read two remarks otherwise); the workflow sent it to a checker as well. "Its formulation" separates the event from the question structure (L138, L151); "an event" puts the formulation where records refer (L397), in the same class as an assessment (L55, L604, L612), so that the criticism question of L161's next sentences can take it as its target (L377). The only changes that leave the claim as it was are re-spellings of the concession (Mimo, reply line 46) and the checker's "Formulating it is still an event."; neither is clearer. Every other written-out change breaks a named line: "occurrence" moves the formulation to the carrier side of L169; "input" goes against L592; "fact" against S23 and L397; "It is still an event." makes the question itself an event, against L151 and L169; "Its statement" pulls against "statement" as a content at L159, L409 and L473. Mimo's and GLM's own remarks in step 3 name no defect. Recorded as held under both readers' attempts; not thereby final. Noted for the next round (it bears on every use of the word, not on this sentence alone): "event" is used at L53, L55, L161, L397, L604 and L612 and defined nowhere, while "occurrence" is defined at L169, and the text does not say how they are related.

### C15 · L161 — KEEP

> Exposing the defect is another question with its own contract.

- Mimo (`s103_vary_mimo_2`, line 81): `` `C15: VARIES — Exposing the defect poses another question, with a contract of its own.` ``
- GLM (`s103_vary_glm_2`, line 73): `C15: HOLDS — dropping "its own contract" breaks L151 and the line's final sentence; fixing the target breaks L377; shifting to "alleged" untethers the sentence from the defects just listed and duplicates Part IX.`
- **Ruling: KEEP.** Easy to vary: Not shown easy to vary: one half of Mimo's rival is a rewording that is not clearer; the other ("poses") is a different claim, weighed and not taken.

Mimo holds that "is" is loose against L377, which gives the exposing a premise and a connection beyond the question. The text uses the same idiom at L271 ("which is a different question (Part III)"): "is another question" places the matter under another question and says nothing about the exposing being nothing beyond it, and "poses" leaves the premise and connection just as unsaid. "Poses" also puts the exposing outside the other question, so that L161's next sentence ("An assessment is an event with a frozen contract") no longer applies to it on its own contract, and it opens a reading as a follow-on, replacement question, which L161's last sentence keeps apart and says only "can" happen. ", with a contract of its own" is a rewording and not clearer: with the comma, the phrase can attach to the whole clause instead of binding the contract to "another question", where L151 and L367 need it. GLM's variations break where GLM says (no contract: L367, L55, L151; p's contract: L367; an answer to p: L151; the same target: L377), with one ground added (a question that fails to pick out its alleged target has no target to share) and one narrowed.

### C16 · L217 — KEEP

> For an edit–boundary pair \((a,b)\in C\) actually occurring:

- Mimo (`s103_vary_mimo_2`, line 106): `` `C16: HOLDS — admitted, encountered and coming about each break L159, L195, L223, L582 or S25.` ``
- GLM (`s103_vary_glm_2`, line 99): `C16: HOLDS — removing "actually occurring" breaks L582 and L159; "encountered" breaks L223 and L195; "physically realized" crosses the S25/S26 boundary and mismatches L582.`
- **Ruling: KEEP.** Easy to vary: Only in its verb, at the level of a synonym (recorded). Not clearer.

Both readers close HOLDS, and the tabulation held it under rule 6; the workflow sent it to a checker as well. "Actually occurring" is the sentence's content and does work: every pair of \(C\) is admitted (L141), and the qualifier picks out the pair that occurs, so that a violation (L220) and a surprise (L221) are events, not lasting features of the transport; L41 keeps that apart. L223 and L582 restate the qualifier, and Argument 10 (L624) reaches its fixed verdict "This is surprise" through it. Mimo's "actually coming about" and the checker's "that occurs" are synonyms; Mimo said "coming about" breaks L159 and S25, and the checker finds no break there; neither is clearer, since each parts the sentence from the words L223 and L582 use to restate it. Every wording that changes the claim breaks something named: dropping the qualifier or writing "admitted" (L220, L223, L582, Argument 10); "encountered" (L195, L223, L225); "physically realized" (L159, L179, and Argument 10's stipulated episode); \(H\) for \(C\) (L221). Recorded as held under both readers' attempts, and this checker's; not thereby final.

### C17 · L219 — KEEP

> - the **prediction** is \(\operatorname{Ans}_S(\tau(a),\sigma(b))\);

- Mimo (`s103_vary_mimo_2`, line 129): `` `C17: HOLDS — dropping the translations, changing whose answer it is, or adding a faithfulness condition each break (A) at L250, L189, L177 or L223.` ``
- GLM (`s103_vary_glm_2`, line 121): `C17: HOLDS — the formula's positions are fixed by L189 and mirrored by (A) at L250; the verbal rival uncouples it from (A), and defining the prediction as $\operatorname{Ans}_p(a,b)$ abolishes violation.`
- **Ruling: KEEP.** Easy to vary: In notation only (recorded). The verbal re-spelling is not clearer.

Both readers close HOLDS, and the tabulation held it under rule 6; the workflow sent it to a checker as well. The theory needs the prediction to be \(S\)'s own answer (L177, "\(S\) is where prediction lives."), through the transport's translations, as L582 needs; to exist whether or not the transport is faithful (L223); to be able to differ from what occurs (L622–L630; case N18); and to share the form of (A) at L250. GLM's verbal wording ("what $S$ answers at the translated edit and boundary") says the same, but leaves unsaid whose translations are meant and hides the shared form with (Q) at L144 and (A) at L250. Every other wording breaks a named line: \(\operatorname{Ans}_S(a,b)\) (L189, L582); \(\operatorname{Ans}_p(a,b)\) (L177, L582, and the case at L624); adding "when t is faithful" (L223, L624); swapping the translations (L189). One amendment to GLM's argument: L220 defines violation as a failure of fidelity, not as a failed prediction, so the \(\operatorname{Ans}_p\) wording does not do away with violation; it takes away the prediction's ability to differ from what occurs. Recorded as held under both readers' attempts; not thereby final. Noted, not ruled: L151 uses "prediction" of a transport not said to be to \(S\), in the ordinary sense.

### C18 · L220 — KEEP

> - a **violation** occurs when fidelity fails at \((a,b)\);

- Mimo (`s103_vary_mimo_2`, line 152): `` `C18: HOLDS — prediction-failure and breakdown break S27, L189, L233–L245 and L582; what survives re-spells the same criterion.` ``
- GLM (`s103_vary_glm_2`, line 147): `C18: HOLDS — "wrong prediction" drops (F1)/(F2) against L245; "reality falsifies" violates S23; globalizing over $C$ breaks L221 and L582.`
- **Ruling: KEEP.** Easy to vary: Yes, in this respect (recorded): the narrow and wide re-spellings change nothing the passage uses. None clearer.

Both readers close HOLDS; the tabulation sent it to a checker under rule 5's clause on doubt. The doubt stands, but it is about the word "fidelity" across the text, not a defect of this sentence. The text uses the word narrowly, for (F1) and (F2) (L189 "component and global fidelity conditions"; L245 "Together they are fidelity at every level the contract reaches"), and widely, taking in (A) (the heading "Question fidelity" at L247; L520). The two readings differ only where (A) fails at a pair while (F1) and (F2) hold. On the simulation layer that case does not arise: its queries predict a port of \(P\) (L177), and wherever (F2) holds at the pair, a prediction read through the transport is the target's answer. So a failed prediction is a violation on either reading, and every use of the sentence (L223, L225, L582, L624, L626) lies where the readings agree. Mimo's "when (F1) or (F2) fails" and the wide re-spelling are rewordings, not clearer: each parts L220 from the word L195, L576 and L626 use for the same relation, and the wide one opens, on paper, a violation inside \(H\) while survival holds. Mimo's S27 and L582 grounds against "prediction fails" do not stand; the L245 and L195 break does. The extent of "fidelity" across L189, L245, L247, L520 and L630 is recorded for the next round as a question about the term.

### C19 · L225 — KEEP

> Two responses to a violation are distinguished.

- Mimo (`s103_vary_mimo_2`, line 183): `` `C19: VARIES — The semantics distinguishes two responses to a violation.` ``
- GLM (`s103_vary_glm_2`, line 173): `C19: HOLDS — exhaustivity breaks S21 and L429; prescription breaks S21 and L429; outcome-naming breaks L584's "by their traces, not by their outcomes".`
- **Ruling: KEEP.** Easy to vary: Yes, in wording (recorded). Not clearer, so not taken.

On what the rival does, the readers agree: Mimo's active rival changes the voice and names the distinguisher, and changes no term or dependency. GLM calls that a recasting, "not a variation", under the note that opens its second reply ("A note on what counts as a variation", `s103_vary_glm_2`, lines 1–3). Rule 5 says what comes of that: a rewording that changes nothing the theory needs is recorded as showing the sentence easy to vary, and is taken only if clearer. In so far as GLM's note proposes what counts as a variation for hard to vary, it is recorded as parked (S34); the ruling does not rest on it. The rival is not clearer: the bold definitions that follow and L584 already answer "distinguished by whom?", and the passive matches the text's own wording for the same kind of sentence (L77 "They are distinguished by their histories."; L13 "are told apart by their histories"). Each change of claim breaks a named line: "kinds" (L39, L111, L245, L558); opening with "There are two responses to a violation" makes the pair exhaustive (S21; L429); "admits" (L141, L257); "demands" (S21; L429); "learning and creating" names the responses by outcome, against L584's "by their traces, not by their outcomes". Choosing the active voice is for the person choosing (S21).

### C20 · L225 — KEEP

> Only the second can be originative under Part X.

- Mimo (`s103_vary_mimo_2`, line 211): `` `C20: HOLDS — is, dropping Only, creative and must each break (G)/(N), L201/L405/L584, L425/L429 or S21/L429.` ``
- GLM (`s103_vary_glm_2`, line 199): `C20: VARIES — Only a construction response can be originative under Part X.`
- **Ruling: KEEP.** Easy to vary: On the reading GLM's own ground gives it, a different claim; on a narrow reading, a rewording (recorded) that is not clearer.

GLM's rival stands "on the defined term alone". Without the ordinal, "Only" ranges over everything originative, and the rival makes a response to a violation necessary for (G). That wider claim meets (G) itself (L422, which has no violation conjunct), question-finding (L425, L588, L592), construction from an available problem (L405), construction answering a conflict found by argument with no test (L315; S27) and recognized difficulties other than violations (L317, L429). Read narrowly, with the pair supplied from context, it is a rewording that leaves to context the bound the text states. "Only" holds by Build (L405) and L411, and by L201 ("a selected transport has no represented target and no criticism in its history"); "can be" is apt, since a construction response can fail New (L416), Attempt or ownership (L427). Dropping "Only" loses the exclusion but contradicts nothing (Mimo's "breaks" is more exactly a loss); "is" and "must" break (G) and S21; "creative" is Part X's word for episodes (L429). Two of GLM's grounds go beyond the text (its reading of L195, and L626 taken as general); the exclusion does not rest on them. A third wording, "Of the two, only the construction response can be originative under Part X.", was considered and not taken; taking it is the choice of the person choosing (S21). GLM's standing note is recorded as parked, as at C19.

### C21 · L273 — KEEP

> "\(p\) because \(p\)" fails non-circular dependence.

- Mimo (`s103_vary_mimo_3`, line 31): `C21: VARIES — Conclusion-as-premise fails non-circular dependence.`
- GLM (`s103_vary_glm_3`, line 15): `C21: HOLDS — every variation broke the verbatim echo at L397 or the "fails" usage at L275 and L536.`
- **Ruling: KEEP.** Easy to vary: Yes, in wording (recorded). Not clearer, so not taken.

Mimo's "Conclusion-as-premise fails non-circular dependence." names the same case (L536 treats the name and the formula as one case) and the same conjunct. It is not clearer: at L273 the formula shows the shape while the name has to be unpacked; "premise" and "conclusion" are Part IX's vocabulary for arguments (L397), brought into Part V, where a candidate has components, boundary inputs and an answer (L231, L255); and the formula keeps the visible echo with L397. GLM says dropping the formula breaks the tie to L397; that overstates it (L397 points to Part V through L255, not through L273), so what is lost is an echo, weighed here as clarity. The variations that change the claim break named lines: "is not an account" and "fails (E)" (L536); "logically equivalent" (L255, L397); "violates" (the term "violation", L220); "The answer because the answer" (ambiguous between two answers, L250). A third wording, naming the case beside the formula, was considered and not taken; whether to name it, for symmetry with L269 and L271, is for the person choosing (S21). Noted, not ruled: L273's second sentence says an "account" fails, using the word loosely against L262. GLM cites "it fails (F1)" as L267; it stands at L269.

### C22 · L311 — KEEP

> (B) records the collective contribution.

- Mimo (`s103_vary_mimo_3`, line 65): `C22: VARIES — (B) records the contribution of a block.`
- GLM (`s103_vary_glm_3`, line 29): `C22: HOLDS — replacements of "contribution" broke the ties to L305, L307 and L435, and "defines" misstates what (B) is.`
- **Ruling: KEEP.** Easy to vary: Not easy to vary: Mimo's rival is a different, weaker claim. The pure rewordings tried are recorded; none is clearer.

Mimo's "(B) records the contribution of a block." drops "collective", the one word in the paragraph that says the contribution belongs to no single commitment. Its step 3 held that "the block word carries" that reading; it does not, since the text counts a one-commitment set as a block (L293 "For nonempty \(B\subseteq W\),"; L313 applies (B) to \(\{d\}\)). L313's "a block of such commitments" uses what "collective" says, and "collective" also answers L305's "contributory". GLM's HOLDS stands, and its rejection of "work" stands on a stronger ground than GLM gives: "work" is L313's two-sided test (\(d\) added and \(d\) removed), while (B) records deletion only. Mimo's breaking wordings each break what Mimo says: "(S) records" misnames the definition (L290); "each commitment's contribution" and "Each commitment is contributory" misstate the example, since no singleton is critical. The doubt GLM set aside, that "contribution" has a Part VI sense (L305) and a Part XI sense (L435), applies to the word across the text and shows no defect here: this sentence fixes its sense through (B). Noted, not ruled: L311's first sentence does not say in words that each \(d_n\) does no work by itself, which L313's "such commitments" needs; one step supplies it.

### C23 · L375 — KEEP

> An **active route** is a connected subnetwork of actual occurrences joining a represented input to an operative result, whose components meet the applicable relations and which has nonconstant dependence on the represented distinction under the declared contrasts.

- Mimo (`s103_vary_mimo_3`, line 95): `C23: VARIES — An active route is a connected subnetwork of actual occurrences joining a represented input to an operative result, whose components meet the applicable relations and whose result varies with the represented distinction under the declared contrasts.`
- GLM (`s103_vary_glm_3`, line 44): `C23: HOLDS — every removal contradicted L307, L375's own following sentence, L255, or L524.`
- **Ruling: KEEP.** Easy to vary: Not easy to vary: Mimo's rival is a different claim. The one wording tried that changes nothing ("does not have constant dependence") is not clearer; recorded, not taken.

Mimo's rival binds the dependence to the operative result; the text binds it to the route ("whose components … and which has" both hang on "subnetwork"). Every route to a result shares that result, so the rival's clause is met or unmet by all of them alike: it would count the gated route of priority wiring as active, against L307 ("Two systems with the same output table may differ in which routes are active"), L616 and L375's own "read from the history, not from the result". On a contract that varies one valve while the other stays as it was, it would leave ProducedBy with no route in O25, O20 and O39, against their fixed verdicts and L441's "attributed to both". Mimo's step 3 (read as exhaustive, the definition clashes with the exclusion of a route "already at rest when the result occurred") shows no defect: each exclusion in L375's third sentence fails the definition's own join or dependence clause, read in the history for that result. GLM's HOLDS stands removal by removal, with two amendments: dropping "connected" breaks at L453 (a padded route would meet ProducesVia), not L307; dropping "under the declared contrasts" leaves "nonconstant" with no range across contrasts, which L524 alone does not supply. "Operative result" and "applicable relations" are defined nowhere in file 99; they read as plain words beside L73, L385, L487, L606 and L91, and no conflict was shown.

### C24 · L383 — KEEP

> A criticism occurrence can exist when (K1) fails.

- Mimo (`s103_vary_mimo_3`, line 129): `C24: VARIES — A criticism occurrence can exist whether or not (K1) holds.`
- GLM (`s103_vary_glm_3`, line 58): `` C24: VARIES — `A criticism occurrence need not meet (K1).` ``
- **Ruling: KEEP.** Easy to vary: Yes, on both readers' rivals (recorded). Neither clearer, so not taken.

Both readers read "(K1) fails" as saying that bearing is not met, which is the text's own usage for a tag as the name of its condition (L281 "(F1) already fails"; L220; L277 and L606 for (E)). Mimo's "can exist whether or not (K1) holds" is not clearer: "holds" is a verb the text never applies to a tag (it says "meets" and "fails": L277, L281, L606), and if "(K1)" is read as the biconditional, "whether or not (K1) holds" quietly collapses to "can exist" and the point about bearing is lost without the reader noticing. GLM's "need not meet (K1)" makes the occurrence, a physically located carrier (L169), the thing that meets (K1), which is a relation of the criticism with its target and question, and drops "exist", so it no longer pairs with the next sentence's condition on existence. GLM's other wording, "can exist while it lacks bearing (K1)", was weighed as a FIX and not taken. The variations that change the claim each break or lose something: "exists when" breaks L383's second sentence; "cannot exist" goes against L67 and L71 and leaves L385 idle; "(E) fails" loses the pointer to bearing; "can be mistaken" drops (K1) and "occurrence". GLM's S23 argument against "mistaken" is weaker than GLM puts it, since the text itself speaks of error about criticisms at L67.

### C25 · L385 — KEEP

> **Reason use.** A response uses a reason when a structural map from the represented objection into the response suborganization preserves role bindings, sends content-preserving recodings to the same transition, sends content changes to the changes specified by the operative deliberative rule, and lands on an active route.

- Mimo (`s103_vary_mimo_3`, line 159): `C25: VARIES — Reason use. A response uses a reason when there is a structural map from the represented objection into the response suborganization that lands on an active route, preserves role bindings, sends content-preserving recodings to the same transition, and sends content changes to the changes the operative deliberative rule specifies.`
- GLM (`s103_vary_glm_3`, line 72): `C25: HOLDS — each clause-drop contradicted L409's cited paraphrase, and loosening the structural-map head stranded it.`
- **Ruling: KEEP.** Easy to vary: Yes, in wording (recorded). Not clearer, so not taken.

Mimo's rival keeps the map, its direction, "structural", "represented" and all four clauses; it adds "there is … that" and moves the last clause into the active voice. It is not clearer: the existential reading is already clear, since the text uses the same indefinite-subject form for existential definitions (L441, L453); the rival's "that" comes right after "the response suborganization", so its four verbs can be read as attaching there; and reordering the clauses breaks the order L409 points back to with "as reason use asks of an objection (Part IX)". The readers agree on what L409 matches: it transposes reason use onto a binding, so its specifier is "the binding" where L385 has "the operative deliberative rule", by design. Each clause drop makes L409 misdescribe reason use, and in turn touches L377, case N13's reading, L429 and L375; "specified by the role bindings" would count only concessions as use, against L71; GLM's "correspondence" head drops "represented" and "structural" and takes over the text's term for relations between a representation and what it represents (L13, L77). Mimo's step 3: "the same transition" has its comparison in the map's own argument; "operative deliberative rule" and "structural map" occur only at L385, built from the text's own words (rule, L125; operative, L375, L487, L606; structural, L413, L397, L520), and neither reader calls them a failure.

### C26 · L393 — KEEP

> Withdrawing a premise makes the step unusable; it does not rule the conclusion out.

- Mimo (`s103_vary_mimo_3`, line 189): `C26: VARIES — Withdrawing a premise makes the step unusable and rules out no claim.`
- GLM (`s103_vary_glm_3`, line 87): `C26: HOLDS — alternatives lost the named conclusion, contradicted L8/L315/L369, or imported wording S23 forbids.`
- **Ruling: KEEP.** Easy to vary: Yes, in wording (recorded). Not clearer, so not taken.

Mimo's "Withdrawing a premise makes the step unusable and rules out no claim." keeps the first clause word for word; what its wider second clause adds beyond the conclusion the text already holds (L315: only an argument usable by \(j\) rules a claim out; L397: dropping a claim is the person's choice, "not a ruling out"). GLM's objections to the near wording "rules nothing out" do not meet Mimo's (the coordination gives both verbs one subject). One holds as a point of clarity: the rival loses the named conclusion, the one claim the guarded misreading bears on (the move from a lost premise to the conclusion's denial; S98 records D-161 and D-686), and it drops the semicolon contrast that pairs with L369's two halves. GLM's "undermines" and "refuted" bring back wording the S95 scrub removed (D-499); "leaves the step usable" breaks (K2); "rules the conclusion out" breaks L315, L8 and L369; dropping the second clause is a loss, not a break. Mimo's point on "a premise" is not a fault: the sentence picks up the Live clause on the same line, where \(d\) ranges over \(\operatorname{Prem}(u)\). Recorded for the next round, not applied: the Live clause has two disjuncts, so a premise \(j\) withdraws that is also the conclusion of a usable step of the same argument stays live, and the step stays usable; read without restriction, the first clause then says more than (K2) gives. The case is narrow, and no reader tested it.

### C27 · L443 — FIX

> An explanatory aim requires an account, or the correction of a use through one, to be deployable.

- Mimo (`s103_vary_mimo_3`, line 221): `C27: FAILS — "to be deployable" governs both disjuncts, so a correction of a use is made deployable, though Deploy is a relation on contents (L403; L449) — An explanatory aim requires an account to be deployable, or a use to be corrected through one.`
- GLM (`s103_vary_glm_3`, line 108): `` C27: FAILS — "to be deployable" cannot apply to "the correction of a use": Deploy takes a content (L403), a correction is a repair on histories (L438), and (EX) deploys the account (L449) — `An explanatory aim requires an account to be deployable, whether the aim is that account or the correction of a use through it.` ``
- **Ruling: FIX.** Easy to vary: Not a VARIES question: both readers closed FAILS and the fault is shown; the rivals are repairs.
- **Old (L443):** `An explanatory aim requires an account, or the correction of a use through one, to be deployable.`
- **New (L443):** `An explanatory aim requires a deployable account, or the correction of a use through one.`

Both readers close FAILS on the same fault. Read by its grammar, "to be deployable" governs both disjuncts, so a correction of a use is asked to be deployable. But Deploy takes a content (L403: "\(s\) at \(\xi\) holds a representation of \(c\)"; the repertoire is "the set of contents deployable"), a correction is a repair ("The contribution \(\Delta\) of a repair is a subhistory together with the changes of content it makes", L435), and (EX) deploys only the account \(c\) (L449). The new wording is Mimo's own repair at reply line 200 (`s103_vary_mimo_3`): it moves "deployable" onto the account, keeps "the correction of a use through one" word for word, and "one" takes up "a deployable account", so deployability still covers both kinds of aim (L628's "possess a deployable account"; a use corrected through an account, which ProducesVia takes up at L453). Mimo's closing-line wording (line 221) says less about the second kind; GLM's (line 103, "whether the aim is that account or the correction of a use through it") makes an aim into an account, while an aim is "a stated condition over stated occasions" (L441). "Requires" is the text's own word in this definitional role: it says which aims are explanatory, not what must happen to anyone (S21).

### C28 · L471 — FIX

> \(F\) is monotone; \(C\subseteq F(C)\) is the invariant form; the union of post-fixed sets is the greatest fixed point. (CT2)

- Mimo (`s103_vary_mimo_3`, line 251): `C28: VARIES — F is monotone; C ⊆ F(C) is the invariant form; the greatest fixed point is the union of the sets D with D ⊆ F(D). (CT2)`
- GLM (`s103_vary_glm_3`, line 123): `` C28: HOLDS — merging lost the separately citable claims that L546 targets, "an invariant" broke the tie to (CT1)'s `z'∈C` (L466), and "pre-fixed" is false. ``
- **Ruling: FIX.** Easy to vary: Yes, in wording (recorded), and the rival is clearer: taken.
- **Old (L471):** `\(F\) is monotone; \(C\subseteq F(C)\) is the invariant form; the union of post-fixed sets is the greatest fixed point. (CT2)`
- **New (L471):** `\(F\) is monotone; \(C\subseteq F(C)\) is the invariant form; the greatest fixed point is the union of the sets \(D\) with \(D\subseteq F(D)\). (CT2)`

Mimo closes VARIES with this wording (its fenced rival at reply line 228, in LaTeX; its closing line gives it in plain characters); GLM closes HOLDS. The checker went through each clause and found no fault in the sentence: \(F\) is monotone, \(C\subseteq F(C)\) is (CT1), and the third clause is the fixed-point step, with L469 blocking the vacuous reading. The rival names the same sets and states the same identity, keeping "\(F\) is monotone", "the invariant form", the three clauses and the label (CT2) that L546 names. It is clearer: "post-fixed" occurs only here and is defined nowhere in file 99; authors use the name in two opposite ways (the checker read one outside web page on this, not a book); read the other way the clause fails, and L546 names (CT2) as a claim open to counterexample ("A counterexample to the finite monotone claim, (I2), (O1), (T2), (CT2), or Arguments 1–3 under their stated assumptions."). None of GLM's grounds reaches this rival: it does not merge the clauses, it keeps "the invariant form", and it uses neither name. Mimo's word order is kept, not a bare swap of words, which would put a formula just before "is" and invite reading "\(D\subseteq F(D)\) is the greatest fixed point". The costs are small: a few more words, and a local letter \(D\) that the text also uses elsewhere (its letters are local; \(C\) is reused at L463).

### C29 · L520 — FIX

> Account, from fidelity under change (E).

- Mimo (`s103_vary_mimo_3`, line 279): `C29: FAILS — the gloss names only the fidelity conjuncts, though (E) also requires non-circular dependence and non-vacuity (L262; L255; L257) — Account, from fidelity under change, non-circular dependence and non-vacuity (E).`
- GLM (`s103_vary_glm_3`, line 138): `C29: HOLDS — the bare tag lost L265's characterization, enumeration broke the list's pattern and L265, "the contract's edits" under-described L255, and "variation" touched the parked question of S34.`
- **Ruling: FIX.** Easy to vary: Not a VARIES question: Mimo closed FAILS and the failure is shown. Mimo's other rival ("fidelity across the contract's changes") rewords one phrase (recorded), is not clearer, and keeps the omission.
- **Old (L520):** `Account, from fidelity under change (E).`
- **New (L520):** `Account, from fidelity under change, non-circular dependence and non-vacuity (E).`

The readers differ (rule 7). Mimo: the gloss names only the fidelity conjuncts, though (E) also requires non-circular dependence and non-vacuity (L262, L255, L257). GLM: the gloss names the source by sense, as L265 characterizes every conjunct. The checker rules with Mimo. In file 99 "fidelity" names (F1), (F2) and (A) (L189; L245; the heading "Question fidelity", L247), and never the two conditions Part V uses to keep an account apart from a faithful restatement (L269 "it is an account when it meets the other conjuncts of (E)"; L273, whose first sentence says that the formula in quotation marks "fails non-circular dependence"). Each item of L520's list names what its tagged definition is made from ("Representation, from fidelity and provenance (R)" names both conjuncts of L208); read on that pattern, the Account item presents three of (E)'s five conjuncts (L262) as the whole, and lets a faithful table be an account, which L269 denies. The text counts "the four conditions of Account" (L61; also L231, L536). GLM's defence reads the gloss as L265, but L265 says every conjunct "is a condition on how supplied relations behave under the changes in \(C\)": it shares "under change" with the gloss, not "fidelity". The FIX is Mimo's repair word for word (reply line 279): it keeps every word of the gloss and adds the two conditions by the text's own headings (L255, L257), joined as the (R) item joins its two. No sentence quotes or relies on the gloss; L526 and Argument 6 rest on the dependence order, unchanged. The critical review notes that the ruling cites L245 and L630 loosely for the extent of "fidelity"; the outcome does not turn on it.

## The exact changes

Each line whole, old (file 99) and new (file 103), byte for byte:

- **C07, line 123.**
  - Old: `- a **causal assignment** has a signature that changes under intervention on its output port and under replacement of the component, and is invariant under observation edits;`
  - New: `- a **causal assignment** has a signature that changes under intervention on its output port and is invariant under observation edits;`
- **C27, line 443.**
  - Old: `**Created explanation.** An explanatory aim requires an account, or the correction of a use through one, to be deployable. With \(O_{\mathrm{ex}}\subseteq O\) the explanatory aims,`
  - New: `**Created explanation.** An explanatory aim requires a deployable account, or the correction of a use through one. With \(O_{\mathrm{ex}}\subseteq O\) the explanatory aims,`
- **C28, line 471.**
  - Old: `**Retention fixed point.** \(F(C)\) = states whose executions all complete and return into \(C\). \(F\) is monotone; \(C\subseteq F(C)\) is the invariant form; the union of post-fixed sets is the greatest fixed point. (CT2)`
  - New: `**Retention fixed point.** \(F(C)\) = states whose executions all complete and return into \(C\). \(F\) is monotone; \(C\subseteq F(C)\) is the invariant form; the greatest fixed point is the union of the sets \(D\) with \(D\subseteq F(D)\). (CT2)`
- **C29, line 520.**
  - Old: `Everything else is defined in terms of the two imports, the structural vocabulary of (O) and (Q), the declared indices and the declared inputs (below). Roles, from admitted edits (Part II). Kinds, from signatures (K). The respect of a question, from its query (Part III). Representation, from fidelity and provenance (R). Provenance, from physical history (Parts IV, XII). Account, from fidelity under change (E). Understanding, construction, newness, origin, repair, created explanation, capability, recursion, universality, from those.`
  - New: `Everything else is defined in terms of the two imports, the structural vocabulary of (O) and (Q), the declared indices and the declared inputs (below). Roles, from admitted edits (Part II). Kinds, from signatures (K). The respect of a question, from its query (Part III). Representation, from fidelity and provenance (R). Provenance, from physical history (Parts IV, XII). Account, from fidelity under change, non-circular dependence and non-vacuity (E). Understanding, construction, newness, origin, repair, created explanation, capability, recursion, universality, from those.`

No other line differs (`diff` of the two files: lines 123, 443, 471 and 520 only). No line carried more than one FIX, so nothing needed combining. The removed wordings ("under replacement of the component", "to be deployable", "post-fixed") occur nowhere in file 103.

## What the critical review changed

Nothing. Fable 5.1 read all 29 rulings against file 99, the owner's decisions S20–S35, the reading rule, the tabulation's closing sections and, for each FIX, the reply line its wording comes from; it objected to none (`results/S103 Round 1 - reading/critical review.md`). On the four FIXes it found that each says what the challenge calls for and no more, brings back no word or idea S23 forbids, adds no list, count, grade or record (S20), says nothing about what must happen (S21), puts physical possibility nowhere new (S25–S27), settles nothing (S28), and touches neither what hard to vary covers nor the placement of values (S33–S34). It went through C07's reasoning again, since the C08 checker had remarked the other way: C08's and C09's first clauses are invariances, met by any component the contract never edits, so their second clauses do work; C07's first clause is a change, and by L103 already asks for an edit that replaces the component. On C29 it weighed GLM's side again (the list's other items are not exhaustive either) and found the FIX stands because "fidelity" is a defined term that never covers the two added conditions. It found no conflict between rulings and recorded five places where rulings touch the same matter (C07 with C08 and C09; C18 with C29; C11 with C12; C19 with C20; C04, C05 and C06), each consistent.

It recorded small points in the rulings' own prose, none bearing on an outcome: C04 uses "false" in the checker's own voice (line 48 of that ruling), a word of the kind S23 scrubs; C29 cites L245 and L630 loosely for the extent of "fidelity"; the file paths. One slip in the review's own prose, recorded here: its sentence on "Fifteen rulings" lists sixteen candidates in its parenthesis, C06 among them, though no reader closed C06 VARIES. It bears on nothing.

## Parked

No candidate was parked, and no proposal about what hard to vary covers was applied (S34). No point of either reader proposed anything about it. GLM's second reply opens with "A note on what counts as a variation" (`s103_vary_glm_2`, lines 1–3); the C19 and C20 rulings record it as parked in so far as it proposes what counts as a variation for hard to vary, and neither ruling rests on it. GLM mentioned S34 once more, at C29, only to decline the word "variation". No value was moved in or out.

## The new text

`tests/103 The semantics, standing alone, after round 1.md`, md5 f31ebb1f050783f1a84f6136cec20fcd, 632 lines (by `wc -l`), made by `results/S103 Round 1 - reading/apply.py` from file 99 one line to one line; file 99 unchanged; nothing written into `authority/`. The scans, all passing:

- **Forbidden words** (the S95 word families, imported unchanged from `tests/S95 Scrub - scripts/scrub_apply.py`): 76 hits in each text, none added, none removed; the noted scan finds no unexplained hit in either.
- **Physical possibility** (the S96 list, from `tests/S96 Repair - scripts/repair_apply.py`): 198 mentions in each, none added or removed; no line with a mention lacks its S96 reason.
- **Structure:** 55 headings, 154 bold terms (137 distinct), 23 formula tags and 223 parenthesised labels (35 distinct) in each; none lost or gained.
- **Words:** 16,394 by whitespace split in both (16,366 by `wc -w`); the losses and gains balance. Each of the 25 KEEP spans stands once on its line in both texts.

## The cases

A fresh Opus 5.5 case checker re-read, on file 99 and on file 103, every case that could turn on one of the four lines (`results/S103 Round 1 - reading/cases.md`). It found them through the S81 determination's ties of cases to lines, the S81 Stage 1 returns, the S98 ledger (which ties no case to any of the four units), the change list's CASES AT RISK for the entries beside them, the S95 and S96 re-reads, and a program search of all 78 case texts; 160 comparisons of lines and quotations by program, none failed. **No case moves**: none toward its fixed verdict, none away, none silent.

- **Line 123 (C07).** O9 (which the S81 determination ties to this sentence), O4, O6 and O7: SAME. For O9 and O7 one reading of the old sentence is closed (the deleted clause read as asking for a replacement other than the intervention); neither verdict rested on it. **Watch, O4:** the contrary reading two S81 testers raised (the index as a causal assignment) now meets the bullet's wording on every reading; its step to "Dario has a coarse account" still fails at L255 and L273, as before. Also read and not reached: O10, O22, O19, O42, O46, O25, O39, O52, O27, O40, O50, N16, N17, N23, D3-T, and the text's own cases at L269, L271/L325, L331, L347 and L626.
- **Line 443 (C27).** O13 (tied to this sentence by the determination and by testers 1K_A and 1K_B): SAME; the literal old grammar is closed, and the S81 readers had already read it as the new wording says. N10: SAME; both texts are silent on the case's word "knowledge"; the name of the defined term is still open for the owner (ledger record D-591). The worked case at L628: SAME; its aim now stands in the new first disjunct's own words. Also read: O20, O25, O26, O39, O52, O32, O12, O31, N11, N15, N18, N19.
- **Line 471 (C28).** No case turns on (CT2). O14, N20, N13, N24, O42 and O49 use (CT1), tolerances or (T2): SAME.
- **Line 520 (C29).** Every Account verdict rests on Part V (L255, L257, L262, L269, L273), not on the gloss: SAME throughout. For O2, O4, N2, N3, N16 and N25 one reading is closed (the old gloss taken at its word, which would have made a faithful restatement an account); no record shows anyone reading a case that way. O37 still turns on L526's "no cycle", which is not the non-circular dependence the gloss now names.

The fixed verdicts themselves (the S81 case book O1–O52, the S89 cases N1–N25, D3-T) are unchanged. The cases were re-read by one agent; no outside reader has seen file 103.

## Moves

**4** (the four FIXes applied; no DROP). By rule 14 a round with a FIX or DROP does not end the series: "no moves left" (decision S35) is not reached. The next round goes to file 103.

## What points to the next round

### Raised by the readers, beside their items

- **Undefined phrases in Part IX.** "Operative result" and "applicable relations" (L375), "operative deliberative rule" and "structural map" (L385) are defined nowhere in file 99; Mimo (C23, C25) and GLM (C25) could not find them in the lines given. The checkers read them as plain words fixed by the text's other uses and found no conflict; no reader called them a failure.
- **The extent of "fidelity".** Mimo's step 3 at C18: L189 makes a transport's fidelity the component and global conditions, while the heading at L247 and L520 take in (A). The C18 checker found the two readings agree on every use of that sentence; the word's extent across L189, L245, L247, L520 and L630 is open. C29's FIX was checked against both extents.
- **"Contribution" in two senses** (GLM, set aside by GLM, at C22): Part VI (L305) and Part XI (L435, L441). Each sense is fixed where it stands.
- **"the same transition"** at L385 (Mimo, C25) and **"a premise"** at L393 (Mimo, C26): answered in their rulings from the lines themselves.

### Noted by the checkers, outside their candidates

Collected by the critical review; none is a ruling, and none was applied.

1. **(K) applied beyond components of the target.** Three checkers, independently (C04, C05, C06): Argument 1 reads (K) on \(\tau[C]\), and L556 writes "By (K)" of the subnetwork \(\lambda(k)\), while (K) is stated for a component; L119 and L233 supply the reading. A question for L119 and L554–L556.
2. **"Event" and "occurrence"** (C14): "event" is used at L53, L55, L161, L397, L604 and L612 and defined nowhere; "occurrence" is defined at L169; the text does not say how they are related. To be read with L596.
3. **"Signature" in the everyday sense at L584**, beside the defined term (C12).
4. **L121 names four things and gives three bullets**; by L347 the rule bullet covers a rule and a constitutive status (C09).
5. **L109 gives roles "under \(A\)"**, while (K) builds a signature on a contract \(C\) (C08).
6. **"Prediction" at L151** is used of a transport not said to be to the simulation layer, while L219 defines it for transports to \(S\) (C17).
7. **L273's second sentence** uses "account" loosely (C21).
8. **L311's first sentence** does not say in words that each \(d_n\) does no work by itself, which L313's "such commitments" needs (C22).
9. **A premise live twice over** (C26): withdrawing a premise that is also a usable step's conclusion leaves the step usable, so C26's first clause, read without restriction, says more than (K2) gives in that narrow case.
10. **"Complete" in L471's first sentence** must be read as (CT1)'s "completes with \(o\in T[i]\)" for clause 2 of (CT2) to be (CT1) (C28).
11. **The undefined phrases of L375 and L385** (C23, C25), as above.
12. **The two extents of "fidelity"** (C18), as above.
13. **"Contribution" in Part VI and Part XI** (C22), as above.
14. **L27 gives no pointer to Part XIV**, where L23 and L25 give theirs (C01).

### What the four changes may have disturbed

- **Line 123:** the three bullets of L123–L125 now each have one side that changes and one that stays; the next round should read L57, L109, L121 and L127 against the new bullet, and the asymmetry the critical review gives between C07 and C08/C09.
- **Line 443:** the antecedent of "one" (now "a deployable account") and the two kinds of explanatory aim, against (EX) at L447–L449, ProducesVia at L453 and the worked case at L628.
- **Line 471:** the letter \(D\), bound locally, beside the \(D\) of a question's target; and (CT2) as L546 names it.
- **Line 520:** the Account item is now the only item of the list that names more than two sources; the list's pattern, L526's order, and "the four conditions" at L61, L231 and L536.

### Left to the person choosing

Three rulings leave a choice of wording open, for the person choosing, not a question the text must answer (S21): the active voice at C19; the wording "Of the two, only the construction response can be originative under Part X." at C20; and naming the case beside the formula at C21, for symmetry with L269 and L271.

## Agents and outside calls

- **Before sending** (committed 12:18–12:38 UTC): decisions S34 and S35 entered verbatim with every key withheld, the GLM caller through Claude Code and the one-call-at-a-time slot limit (1f8df4b); then one Claude subagent built the three briefs, the two job lists, the GLM loop and the reading rule (3c7806a). Set-up calls, from the session's scratch space: one tiny Mimo call and two tiny GLM calls through Claude Code, each answered; a listing of OpenAI's models and three tiny calls to its responses endpoint for Astra Max (model `gpt-6-astra`), none answered: two refused because the account has no credits left, one for a setting value given on purpose to learn the allowed ones. So Astra Max was not used; the owner wrote "If not don't worry." (decision S35). The key itself is not in any record.
- **The round's outside calls:** six, three to Mimo (mimo-v2.6-pro, effort medium) and three to GLM (glm-5.3 through Claude Code, effort medium), one Mimo and one GLM at a time (decision S35). All six accepted on their first attempt; no disconnect.
- **The reading:** one tabulator (Opus 5.5); 29 checkers (Opus 5.5), one per candidate; one critical review (Fable 5.1, used once, as decision S35 asks: "sparingly for critical reviews"); no re-checks; one agent to apply (Opus 5.5); one case checker (Opus 5.5); and this recorder (Opus 5.5). 34 agents in the reading, 33 of them Opus 5.5. Decision S35 allows "as many Opus 5.5 agents as you deem necessary".
- **Other outside reading:** the C28 checker read one web page on the name "post-fixed".

## Not done, and unsure

- No outside reader has read file 103. The four FIXes were each ruled by one checker and read by one review; they have not been varied by the readers themselves.
- The seven strong candidates challenged and kept before this round (S100) were not in it; nor were their maps (S101).
- "Easy to vary" is recorded on this reading only, in the plain sense; it is not the text's term and says nothing about what hard to vary covers (S34).
- Whether the checkers ran at most five at a time (rule 5) is not recorded.
- The owner's earlier open questions stand as they were (file 102's question, parked by the owner in decision S34; file 97, section 4; the ledger's 26 records open for the owner; "or by any version label"). This round answers none of them.

## Files

- Reading rule: `results/S103 Round 1 - how the replies will be read, written before sending.md`
- Briefs: `tests/S103 Round 1 - trying to vary the strong candidates - part 1, Parts 0 and II.md`, `... part 2, Parts III and IV.md`, `... part 3, Parts V to XIV.md`; builder `tools/s103_build.py`; job lists `tools/s103_jobs - round 1, Mimo.json` and `... GLM.json`; GLM loop `tools/s103_glm_loop.py`
- Returns: `results/S103 Round 1 - returns/` (six requests, replies, receipts and reasoning files)
- Reading: `results/S103 Round 1 - reading/` (`tabulation.md`, `rulings/ruling C01.md` to `ruling C29.md`, `critical review.md`, `apply.py` and its output `apply - output.txt`, `cases.md`, and `records - quotation check.py`, which checks this file's quotations)
- New text: `tests/103 The semantics, standing alone, after round 1.md`
- For the owner: `plain words/103 Round 1 - what the readers found and what changed, in plain words.md`
