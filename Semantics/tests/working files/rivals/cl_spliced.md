# Revision 2 - change list, draft of 23 September

**DRAFT 3 — after the S90 cross-examination by Atria and Mimo; not frozen. Made from file 11, md5 5e494c1095d920d128b9a79de378f923. W19, W20 and W31 are drafted from the settled S88 positions (3ebb6d8). Every S90 ruling is applied: 10 entries fixed, 14 kept, none dropped. No outside reader has seen the texts and declarations the fixes wrote.**

*Written on 23 September 2026 by a Claude subagent for the orchestrator. This is the change list from which revision 2 (file 13) is to be made by program (decision D6). It assembles the entries drafted in five groups (A, B1, B2, C and M) under decisions D1–D11, with every correction the two adversarial checks made and without the one entry they dropped. The working files it was assembled from (the decisions, the item skeleton, the five entry files and the two checks) are in the session scratchpad and are not in the repository. File 11 was read only; its md5 was the same before and after. No S87 or S88 return was opened. Nothing was written into `authority/`. Later on 23 September another Claude subagent replaced the three placeholders with seven entries drafted from `results/S88 Reading of Mimo's reply in three parts, and the settled positions.md` (committed at 3ebb6d8), and brought the frame of this list up to date with them. It opened no S87, S88 or S90 return and wrote nothing into `authority/`. On 24 September 2026 another Claude subagent applied every S90 ruling to this list in one pass, which makes this draft 3. It read the S90 rules, the three S90 readings (`results/S90 Reading of the replies - batch 1 …`, `… batch 2 …` and `… batch 3 …`, whose batch 3 holds the cumulative list of edits) and the ruling files in `results/S90 reading rulings/`, and it took every ruled text from them byte for byte. It opened no S90 reply, receipt, reasoning file or attempt file, wrote no ruling, and wrote nothing into `authority/`.*

## What this is

This list gives every change that revision 2 makes to file 11, in the order of file 11's text. The program `tools/s89_apply_changes.py` reads it, checks every entry against file 11 and applies the entries in order. It refuses on any mismatch. It writes the result to a path given on its command line, never into `authority/`. The draft note for file 13, with its declarations and the second layer of the record, is `tests/Revision 2 - revision note, draft of 23 September.md`.

The list rests on D1. If Mimo's cross-examination of the S81 determination overturns S81, every entry is re-examined under plan 2.2 B or C before anything is built.

W19, W20 and W31 waited for Mimo's S88 reply (D2). They are now drafted from the settled S88 positions as seven entries, and the note's counts include them ("The held items, drafted from the settled S88 positions", below). The cross-examination of revision 2 (S90, the X1 of the plan) carried them, with the other 48 changes, to both outside readers in five parts. Its rulings are applied in this draft 3 ("What the checks changed", "After the cross-examination (S90)"), and what the readings passed on without a ruling is in "Carried forward after S90".

The list is withheld from every test brief (D6), as are the note, the sources note and the record it puts into file 13.

## Counts

- **Entries that change the theory text: 55.** Expected ruling CLAIM 49, WORDING 4, ORDER 2. By group: A 14 of 18, B1 14 of 15, B2 11 of 11, C 10 of 11. The note reads "49 of the 55 changes". Before the S90 rulings were applied it read "48 of the 55 changes" (W6.3 was then expected WORDING, and B1 was 13 of 15), and before the held items were drafted "41 of the 48 changes".
- **Meta entries applied: 3.** W1.1 (the note, replacing file 11's line 5), W38.1 (the note of sources and departures, before Part 0) and W1.2 (the revision record, after the last line). They are not counted in the note's N or M.
- **Record-only entries: 5.** W3.1–W3.5 declare five places in layer 2 of the record. They change no text, and the program locates them without applying them.
- **Held: 0.** The placeholders for W19, W20 and W31 are replaced by seven entries (W19.1–W19.3, W20.1–W20.3 and W31.1), each expected CLAIM. All seven are group A.
- **The checks.** Check 1 (groups A, B1 and B2, 38 entries): SOUND 26, FIX 11 (nine change the new text, two change only the expected ruling), DROP 1. Check 2 (groups C and M, 18 entries): SOUND 10, FIX 8, DROP 0, and one companion entry added (W35.4). In all, 19 entries were fixed, 1 was dropped and 1 was added. Every fix is applied below. The seven entries drafted later from the settled S88 positions were checked by their drafter only; see "The held items, drafted from the settled S88 positions". **After the cross-examination (S90):** ten calls, all accepted (five of them in pass 2 after the container restart); 32 rulings on 24 entries: 10 entries fixed, 14 kept, none dropped; 22 changes contested by at least one reply, 2 more (R32, R33) listed and ruled KEEP although found not contested, and 31 contested by neither reply. Every S90 ruling is applied below; see "What the checks changed".
- **Layer 2 of the record: 42 places.** These are the 41 places inside the theory and M7 that 03 rules CLAIM and file 11's note did not declare (S81 determination, file 03, section 2).

## How an entry is written

Every entry is a `###` section whose heading is its drafting id and title. The id is the worklist item with an entry number (W37.1 is the first entry for W37). The program numbers the applied theory entries R2-01 onward in file-11 order when it writes layer 1 of the record, and no W-number reaches file 13.

- **STATUS.** "applied" (the program applies it), "record-only" (located and not applied) or "held" (a placeholder; nothing applied). No entry is now held.
- **GROUP**, **ITEM** and **WHERE** give the drafting group, the worklist item and the place in file 11 in words.
- **FILE-11 LINE.** The file-11 line on which OLD begins, or its first and last lines. The program checks it.
- **REASON WORD.** Why the change is made, in plan 1.1's words: erratum, clarification or change of claim. It becomes the "Reason" of the change's layer-1 entry.
- **KIND.** The expected ruling under 03's definitions: CLAIM, WORDING or ORDER. META marks the three meta entries. Every entry whose KIND is CLAIM is declared in the note by its DECLARATION.
- **CHECK.** The adversarial check's verdict on the entry and what the fix changed. Where the drafter's text below it differs from this field, this field governs.
- **OLD** and **NEW.** Exact text, byte for byte, between four-backtick fences; the fence lines are not part of it. OLD occurs exactly once in file 11. An insertion is written as its anchor in OLD and the anchor with the inserted text in NEW.
- **LOCATOR**, **LAYER-2 ROW** and **LAYER-2 LOCATORS.** For the record-only entries and the record: the exact file-11 text of a declared place, and the row it writes.
- **ANCHOR** and **CANDIDATE WORDING.** For the held entries: the file-11 text each will replace, and the wordings now in view.
- **DECLARATION**, **REASON**, **CASES AT RISK**, **GAIN** and **LOSS** are the drafter's, with the checks' corrections. REASON is the drafter's argument; it is not the REASON WORD.

Slots written `@@NAME@@` in the meta entries are filled by the program: the date, N, M, K, the declarations, layer 1 of the record, and the last column of layer 2.

## The decisions D1–D11

Claude took these decisions on 23 September 2026, under decisions S13 and S18. They are given here in the words in which they were taken, each with its reason and what it gives up, as recorded in the working file of that day.

**Names.** These follow the plan draft. "F11 L514" means file 11, line 514. "Plan 2.2" is a section of the plan draft. "03", "06" and "07" are files in the S81 determination folder.

**D1.** base = file 11, conditional on Mimo's cross-examination of the S81 determination (pending) not overturning it; Atria's did not (06) and the supplementary audit changed no ruling (07).
- *Reason.* S81 holds file 11 as the authority under its second clause. If S81 fell on test (b), the repairs needed (W57 and W12) are already in scope.
- *Gives up.* It gives up the file-10 base of plan 2.2 C and the smaller revision that base would allow. If Mimo's reply overturns S81, everything drafted on file 11 is re-examined under plan 2.2 B or C before any of it is built.

**D2.** Derivation 2, (T2), Γ typing (W19, W31, W20) wait for Mimo's S88 reply; draft nothing for them yet except placeholders naming the current candidate wordings in "Semantics/results/S88 Reading of Atria's reply - the three defects.md".
- *Reason.* Plan 1.3.2–1.3.4 fix each of these wordings from the S88 rulings. The reading of Atria's reply alone changed all three repairs after the cross-examination.
- *Gives up.* It costs time. The three repairs that the defeat list exposes are drafted last. The paragraphs they share with other items (F11 L121, L257 and L518) must be finished around them.

**D3.** no default inputs; "mostly" in its weak form; scope as a clarification joined with W57; the surprise variant the plan recommends.
- *Reason.* A default input chooses the input from the verdict wanted, against F11 L514 and L465. A weighting or a scope measure would bring back grading. Surprise (b′) keeps Derivations 4 and 10 whole.
- *Gives up.* O35, O21, O27 and O50 stay SILENT, and so does O1. "Surprise" stays narrower than ordinary use. The Part VI measure of loose limits (W32(c)) and file 12's tested-history surprise wait for a later revision.

**D4.** from the Derivation 3 family only W17.
- *Reason.* W17 makes Derivation 3's claim and proof match by definition. No case earns W16, and re-widening the refuter risks O48. W18 has no usable case while N14 is set aside.
- *Gives up.* Derivation 3's defeat limb stays close to analytic. Whose knowledge a population fixes stays unstatable.

**D5.** from file 12 only the missing-input sentence pattern; W46–W50 left.
- *Reason.* File 12 is under no round, and a claim change is earned by a case. The pattern of 12:554 is wording, limited to the inputs that Part XIV lists.
- *Gives up.* Several things stay in file 12: realized and joint edits, causal dependence, actual causation, absence and prevention, and what a failed intervention refutes. Conflict 14 stays open for revision 3.

**D6.** revision 2 is made by applying a change list by program to file 11, with a two-layer record (revision 2 against file 11; file 11's undeclared places against file 10), all withheld from test briefs.
- *Reason.* File 11 was a full rewrite, and its note missed 41 CLAIM places. A patch applied by program makes every difference an entry. The second layer declares what file 11 did not.
- *Gives up.* It gives up rewriting for flow. The authority file grows by the note, the sources note and the record, and the build must cut all three from every brief.

**D7.** the new file is authority/13; its log entry takes the next shared number when written.
- *Reason.* 13 is the next free number in the authority folder's own sequence, which every plan uses. The log number is read from all three logs when the entry is written (lesson S5), and S89 has already gone to the source audit and the candidate cases.
- *Gives up.* The file name will not match its log number. The round's file names will not carry the "S89" the plan expected.

**D8.** cases for the test: O1–O52 plus N1–N5, N7–N13, N15–N25 as O53–O75; D3-T as O76 after its reworded form is checked by a fresh pair of authors.
- *Reason.* The 23 cases taken were agreed under the N-case rules, and their authors never read the theory. N6 and N14 are set aside by the rule as written. D3-T's first verdict was written by a reader of the theory.
- *Gives up.* N6 and N14 are out until they are rewritten and judged again. The new cases are not held out, because the worklist chose items with them.

**D9.** attack labels: keep the existing labels (continuity with 60+ records outweighs tidiness); fix only pointers that are wrong — W27 is narrowed to that.
- *Reason.* The records refer to the attacks by these letters. S81 ruled every attack-label pointer in file 11 CORRECT (03 §5: XR8, XR11 and XR12).
- *Gives up.* The attack labels (A), (B), (D) and (E) still share letters with the equation tags, and a reader tells them apart by context. The record's old→new map of the labels is dropped.

**D10.** done (b6aba4c).
- *Reason.* The plan cites the working files, and the scratchpad can be lost (plan R7).
- *Gives up.* Nothing further. The files stand in the repository as drafts marked "not frozen".

**D11.** the full test design, with auditor briefs split into parts of at most 13 rows and repeats where the budget allows (Mimo's single readings vary run to run: 36 of 52 rows differed between two 2a runs).
- *Reason.* With one reading per part, a change in the text cannot be told apart from reader variation. Smaller parts and repeats measure that variation. The full design keeps 2a-K and X2.
- *Gives up.* It costs time and calls. The plan's five parts of 11–18 rows (3.6) become at least six parts of at most 13 rows. The call count and the 22–26 hours of section 5 rise, and repeats run only where the budget allows.

### What the decisions change in the plan draft

- **W27** (1.2, 2.5, 2.6). Nothing is renamed, and only a pointer that is wrong is fixed. The record's label map is dropped, and so is the build's check of that map.
- **W19, W20 and W31** (1.2, 1.3.2–1.3.4, 1.5). These are held. The skeleton names their current candidate wordings as placeholders. (Now drafted from the settled S88 positions; see below.)
- **W4, W14's strong form, W32(c) and W35(c)** stay left out (1.2, 1.4).
- **W16, W18 and W46–W50** stay left out (1.2, 1.4).
- **The log number** (2.3). It is the next shared number when the entry is written, not the expected S89.
- **The parts** (3.6). They are recut to at most 13 rows each, and the word counts, call counts and times in 3.6 and section 5 are redone.
- **D3-T** (3.3). Its reworded form is checked by two fresh authors before it enters as O76.

## What the checks changed

**Fixed: 19 entries.** Each fix is applied in the entry, and its CHECK field says what changed.

| entry | line | check | what the fix changed |
|---|---|---|---|
| W37.1 | 15 | 1 | expected ruling CLAIM → ORDER; no declaration |
| W22.1 | 373 | 1 | \(\mathcal E_c\) is "the explanatory candidate (Part V) that the criticism offers for \(p_\delta\)", not an "account" |
| W22.2 | 379 | 1 | a criticism needs a signal represented "as grounds for an alleged defect in a target" |
| W30.1 | 121 | 1 | the second sentence states L105's port-setting link in place of "fixed by the organization D" |
| W39.1 | 257 | 1 | "identity of that assertion with the target's answer" |
| W7.3 | 516 | 1 | a declared input is "something a claim takes as stated"; "the boundary and continuity of an attribution" |
| W58(ii).1 | 33 | 1 | expected ruling CLAIM → WORDING; no declaration |
| W57.1 + W32(b).1 | 161 | 1 | "does not certify the restriction as appropriate" |
| W17.2 | 473 | 1 | "candidate transports", not "realizable transports" |
| W12.1 | 465 | 1 | "Where the system's boundary is not declared explicitly"; the guard covers only a statement of ownership "which does not say where it runs" |
| W23.1 | 427 | 1 | Δ is typed without making "contribution" a defined word |
| W36.1 | 71 | 2 | "a separate matter", not "a separate measure" |
| W45.1 | 77 | 2 | "physical medium" in place of "kind of carrier" |
| W35.2 | 225 | 2 | a constructed transport "is violated, and the failure is not surprise" |
| W33.1 | 315 | 2 | "does no work by itself in the candidate"; both halves of the test, for every support; the infinite case; "a separate matter, shown by Pres" |
| W40.1 | 337 | 2 | anchored after the paragraph's last sentence; "the question why it appears" |
| W41.1 | 401 | 2 | "A system's realization"; fidelity and provenance named; "Use does not by itself construct …"; the declaration completed |
| W1.1 | 5 | 2 | the note names its test in place of "every change of that last kind" |
| W38.1 | 7 | 2 | seven lines of the sources note corrected: file 00's references; interoperability, now "physical media" and pp.87–88; Deutsch's "problem"; the knowledge line; stated limits; "a separate matter"; "does no work by itself". One fallback page corrected |

**Added: 1 entry.** W35.4 (L227, WORDING), check 2's companion to its W35.2 fix: "A **selection response** extends the history \(H\) of a selected transport and lets \(\mu\) act:".

**Also from check 1.** W8.1's expected ruling is written ORDER, the reading check 1 gives ("ORDER is right": 03 ruled the L63 short form ORDER, M12). The drafter wrote WORDING (ORDER). Neither is declared.

**Dropped: 1 entry.**
- **W26.1** (L327, renumber tag (I4) as (I3)). Check 1 dropped it under D9's weighing, as skeleton conflict 15 asked:
  - A gap in a tag sequence is not a wrong pointer, and D9 fixes only wrong pointers.
  - "(I4)" is cited outside the theory: by the hard-to-vary skill's word list (twice) and its unrun rig copy, by the S81 rulings, the S88 files, the plan and the worklist. Renaming it would leave every one of those pointers stale.
  - The inline tags can be read either way (group A's finding C2), so renumbering would move the ambiguity, not remove it.
  - The new (I3) would collide with file 00's (I3), a different result (approximate identification).

  The record says instead that the tags follow file 00's numbering, whose (I3) the theory does not carry. Plan 2.6's inventory check "(I4) renamed to (I3)" is dropped.

**After the cross-examination (S90): 10 entries fixed, 14 kept, none dropped.** The five parts of the S90 cross-examination went to Atria and to Mimo, ten calls in all, and every call was accepted (five of them in pass 2, after the container restart). Each change a reply contested went to a fresh Claude checker, who ruled keep, fix or drop. Where two checkers ruled one entry, the readings reconciled their rulings into one. The rulings are in `results/S90 reading rulings/`, and the readings that record and reconcile them are `results/S90 Reading of the replies - batch 1 (Mimo A1, Mimo A2, Atria B1).md`, `… batch 2 (Atria A2, Mimo B1).md` and `… batch 3 (Mimo B2, Mimo C, Atria B2, Atria A1, Atria C).md`. Every edit is made in its entry and marked there as after the cross-examination, and every ruling, keep or fix, has its line in the entry's CHECK field, beginning "S90 cross-examination:". No outside reader has seen the texts and declarations the ten fixes wrote.

| entry | line | R2 | calls and points | ruling | what the fix changed |
|---|---|---|---|---|---|
| W37.1 | 15 | R2-01 | Mimo A1 point 3; Atria A1 point 1 (pass 2) | FIX (two rulings, same text) | "blind" deleted, so Part 0 states only the body's "no represented target"; REASON WORD erratum → clarification; the CLAIM fallback line reworded; KIND ORDER and no declaration, unchanged |
| W19.1 | 121 | R2-08 | Mimo A1 point 1 | FIX | a typing sentence, in Part IV's and Part V's words with pointers, inserted before the two settled sentences, which stay byte for byte; KIND and declaration unchanged |
| W35.1 | 219–223 | R2-12 | Mimo C point 1 | FIX | the preamble reads "a transport to the simulation layer \(S\)"; the declaration reads "for every transport to the simulation layer, whatever its provenance" |
| W35.2 | 225 | R2-13 | Mimo C point 4; Atria C point 1 | FIX (two rulings, reconciled to Mimo C's text) | the opening clause reads "for every transport to the simulation layer", and its instance "a constructed one"; the declaration includes the restated clause; REASON takes Atria C's reason |
| W20.1 | 233 | R2-15 | Mimo A1 point 2 | FIX | "whether or not anyone has described their work" added, from L309 s3; the declaration follows; O45 holds AGREE on firmer text |
| W40.1 | 337 | R2-25 | Atria C point 3; Mimo C point 5 | FIX, declaration only (KEEP and FIX reconciled to the FIX) | the declaration carries NEW's clause on what makes a denial bare, word for word; OLD, NEW and KIND unchanged |
| W24.1 | 351 | R2-26 | Mimo A2 point 4 | FIX, wording only | the condition reads "for every admitted generator \(a\)", so the two quantifiers match; KIND WORDING, no declaration |
| W22.1 | 373 | R2-28 | Mimo A2 point 1 | FIX | \(\mathcal E_c\) is "the criticism's connection from \(g\) to \(\delta\), interpreted as an explanatory candidate (Part V) for \(p_\delta\)"; the declaration says "says what its terms are" |
| W6.3 | 447 | R2-39 | Atria B1 point 1; Mimo B1 point 2 | FIX (two rulings, one edit) | KIND WORDING → CLAIM, declaration added; OLD and NEW unchanged; the REASON no longer says the entry can be dropped |
| W7.5 | 518 | R2-48 | Mimo B1 point 3 | FIX | "(EK) also on (P)" added to NEW and to the declaration; the over-statement for (P) kept |

**Kept after the cross-examination: 14 entries.** Their texts do not change, and each CHECK field records its ruling: W58(ii).1 (R04), W36.1 (R06), W45.1 (R07), W20.2 (R17), W58(i).1 (R21), W33.1 (R24), W41.1 (R30), W21.1 (R31), W13.1 (R32), W13.2 + W12.2 (R33), W35.3 (R34), W17.2 (R42), W19.2 (R51) and W17.3 (R52). W19.2's rulings also ask for two notes in its CASES AT RISK (O36, and N25's second question), and they are made.

**Dropped after the cross-examination: none.** No ruling dropped an entry, so no entry leaves the list and "Dropped" above is unchanged.

**Also changed with the rulings.** W37.1's title, since the old one ("Restore 'blind' …") no longer described the entry, as both R01 rulings offer. W6.3's KIND moves the counts (see "Counts"). The frame of this list no longer calls the seven S88 entries unseen or O45 watched under W20.1, and it closes the finding on Part II's forward notation and the finding on O45 ("Findings carried forward").

**The build.** `tools/s89_apply_changes.py --self-test` applies this list with no refusal: 63 entries parsed, 58 applied (55 theory, 3 meta), 5 record-only, none held; CLAIM 49, WORDING 4, ORDER 2; N = 49 of M = 55, K = 42; 54 diff hunks, each inside an entry; both planted edits refused. The theory text of draft 3 is committed as `tests/Revision 2 - file 13 draft 3, theory text.md` (md5 403c4f2fb3e5d57bb48a5647011c9f91, 11,574 words by the runner's count and 11,546 by `wc -w`). The full draft 3, with its meta blocks and the date text "draft of 24 September 2026, not frozen", has md5 e33624e73da8c31e33a8e8df222931af and 26,026 words by the runner's count (25,984 by `wc -w`). Against draft 2 (md5 9aecf2f30ce0b4523606b2b8409fdf37), the theory text differs in exactly the eight entries whose NEW the fixes changed: W37.1, W19.1, W35.1, W35.2, W20.1, W24.1, W22.1 and W7.5. Nothing was written into `authority/`.

## Checked, with no change entry

**W27, attack-label pointers (narrowed by D9).** Group A read every pointer to a Part XV label in file 11 (L5, L19, L49, L63, L337, L528, L534 and L536) against its target. Each is correct, as 03 §5 rules (XR8, XR11, XR12). L63's "(B) their necessity" is loose, not wrong, and is left. The labels are not renamed, and the record carries no old→new map. New text that refers to a Part XV label writes "attack (X) in Part XV". Check 1 confirmed the record.

## The held items, drafted from the settled S88 positions (D2)

W19 (Derivation 2, with the sentence after (K), Derivation 10 and W10(b)), W20 (non-circular dependence and the typing of Γ) and W31 ((T2)) were held under D2 until Mimo's S88 reply had been read. They are now drafted from `results/S88 Reading of Mimo's reply in three parts, and the settled positions.md` (committed at 3ebb6d8). That file settles F1 as UPHELD, F2 as NARROWED and F3 as NARROWED, and gives each repair's final wording as exact text. The entries carry those wordings byte for byte: OLD is cut from file 11 and NEW from the settled file by script, never retyped. There are seven entries, and each stands in file-11 order among the others:

| entry | file-11 line | what it changes | plan rule applied | expected ruling |
|---|---|---|---|---|
| W19.1 | 121 | the sentence after (K): kinds across two candidates | 1.3.3 (taken with either wording) | CLAIM |
| W20.1 | 233 | Γ typed; the rest of \(E\) is named background | 1.3.4, "take B, with the rider" | CLAIM |
| W20.2 | 257 | S3: option B with the deletion rider | 1.3.4, "take B, with the rider" | CLAIM |
| W20.3 | 289 | Part VI: a restricted candidate's commitments are the ones it retains | 1.3.4 (settled change 4) | CLAIM |
| W31.1 | 361 | (T2): the erratum; the general bound waits | 1.3.2 | CLAIM |
| W19.2 | 552–558 | Derivation 2: "Same anchors, one account", wording (i) | 1.3.3, "F1 UPHELD: take (i)" | CLAIM |
| W19.3 + W10(b).1 | 620 | Derivation 10's identity sentence, through the exchange of the two things | 1.3.3; 1.3.1 (NEW-XR1) | CLAIM |

- **The dependence order (L518) is not changed.** Under the rider, (E) uses (O)'s deletion rule, which the order already lists under (F1), (F2) and (A). The two sentences B1 left free stay free.
- **No outside reader has seen these wordings in their final form.** The cross-examination of revision 2 (X1) must carry all seven; the S90 brief carries only the first 48 changes. Within X1, the deletion rider (W20.2) and the Derivation 10 sentence (W19.3) are the least tested. The rider was never put to either reply, and the Derivation 10 sentence was rewritten in settling. After S90: both outside readers read all seven as drafted, in parts A1 and A2. W19.1 and W20.1 were then fixed after the cross-examination, and no outside reader has seen their fixed wordings. W20.2 and W19.2 were ruled KEEP, and W20.3, W31.1 and W19.3 + W10(b).1 were contested by neither reply.
- **The fallback for W20** is settled with it and written in W20.2's CHECK. It applies if X1 finds that the rider breaks a worked case. If both options break something, only the \(\tau,\sigma\) erratum is taken (plan 1.3.4). After the cross-examination: no reply found a worked case that the rider breaks (S90, the R17 ruling on Atria A1, point 2; Mimo A1 gave R17 STANDS), so the fallback is not triggered.
- **The entries of other groups** that refer to W19, W20 or W31 as not yet drafted (W30.1, W33.1, W39.1, W9.1, W24.1, W21.1, W7.5, W3.2, W10a.1 and W1.2) were written before this drafting. They are left as their groups and checks wrote them. The rechecks they ask for (skeleton conflicts 1–5, 11 and 12) are done in the seven entries.
- **The S90 brief's ids no longer match the R2 numbers from C08 on.** The S90 brief was sent before these entries were drafted. It cites the first 48 changes as C01–C48, in file-11 order, which were R2-01–R2-48 in the note of that time (commit 12e73da). The program numbers the applied entries in file-11 order, so every entry from W19.1 (L121) on now has a higher number: C01–C07 are still R2-01–R2-07, C08 (W30.1) is now R2-09, and C48 (W10a.1) is R2-54. The note's map (its section 5) gives each entry's S90 id beside its R2 number. Read S90's replies through the entry ids.
- **Checked by the drafter, not by check 1 or check 2.** The whole list was applied by `tools/s89_apply_changes.py` into a scratch draft, never into `authority/`, with `--self-test`. It parsed 63 entries: 58 applied (55 theory, 3 meta), 5 record-only, none held. Every OLD, locator and anchor occurs once in file 11, and no applied OLDs overlap; W19.1 and W30.1 share L121, and W39.1 and W20.2 share L257, with disjoint OLD texts. The result is file 11 with exactly the listed replacements, in 54 diff hunks, each inside an entry, and the self-test refused both planted edits. N = 48 of M = 55, K = 42. The draft's md5 is 1d51c77eb591ace473e556568a7c4636, at 25,696 words (theory text alone 11,501).
  - Each new paragraph was read in place. Three notation points are carried forward below (Part II's forward notation; "active"; the two readings of "including any that assigns an input").
  - The guard rows were worked through the new text: O2, O4, O5, O7, O10, O24, O33, O36, O45, O46 and O47; N1, N3, N17, N20, N23 and N25; Part VII's production case and the skew-symmetric case. No fixed verdict moves on a reading the text supports.
  - Watched, with a risk away: O45 under W20.1, where "those the candidate offers as doing the work" meets "never described as doing anything"; N1, as W33.1 records, now on fidelity rather than membership; and N25's second question under W19.2, for a reader who rested it on the old slogan. After the cross-examination, O45 holds AGREE on firmer text: W20.1 now adds "whether or not anyone has described their work" (S90, Mimo A1, point 2).
  - Toward: O5 and O7 (W20.2), O46 on firmer text and N17 on its first two questions (W19.2), and the first half of N23 (W20.2).
  - The settling's scripts were rerun (`f1_check.py`, `f3_check.py` and `d10_exchange.py` in `results/S88 Mimo reading parts/checks/`), and their outputs match the readings and the settled file.

## Findings carried forward

These were found while drafting and checking. None is an entry.

- **\(U_c\) and \(A_p\)** in (U1)–(U2) are undefined in file 11 (group A, C3). Defining them is one clause at L489 and a CLAIM, outside every item taken.
- **The dependence order is still a summary** (group B1, finding 9). After W7.4–W7.5 it omits (K2), receipts, (K3), (CA), (CT2)–(CT4), Barriers, Enable, Scrutinizability, Membership, Result, ProducesVia and Cap. "(P), (EK) depend on (G), (E), Deploy" over-states (P)'s dependence and is kept. After the cross-examination W7.5 also states that (EK) depends on (P), and the over-statement is still kept (S90, Mimo B1, point 3). What an active route depends on is carried forward after S90, below.
- **04's O40 ruling cites the old L27 s2** (group B1, finding 12). After W6.1 that sentence no longer says it. The ruling's items 1–3 carry O40 without it; S81 Results should note the change.
- **The plan's prediction P2(d)** names O54, O57, O59, O60, O61, O62, O66, O70 and O73 as rows whose ruled marks stay equal. O57 (W17.2), O61 (W23.2) and O62 (W12.1, W13.2) can move toward the thoughtful person under these entries (group B2, conflict 1), and N4 (O56, Q2) and N1 (O53) are watched under W34.1, W36.1, W41.1 and W33.1 (check 2). Before the freeze the plan should move these rows into P2(b)'s aimed set, or record that a change toward on them traces to these entries.
- **Records misread where (I4) points** (group A, C2). No verdict rests on it, and nothing is changed.
- **f10 L294 s2 became f11 L279 s2** with no layer-2 row (check 2, on W1.2). It is plausibly WORDING, and layer 2 follows 03, so no row is added.
- **Line numbers move.** W41.1 adds four lines after L401, and the meta blocks add lines at the head. The note, the record, the diff map and every brief use file-11 numbering. The program does not assert an unchanged line count, and it allows W35.1's two hunks (L219 and L223) for one entry.
- **The withheld-word check** on briefs must use the marker strings, "Revision 2", "revision record", "file 13", "Deutsch" and "Marletto", and not the bare word "record", which the theory itself uses (group M, conflict 3).
- **The note's form.** Plan 2.5 makes the note one paragraph. W1.1 gives the paragraph and, in the same block, one line per change of claim (group M, conflict 2).
- **Layer 2 rests on 03 and on D1** (group M, conflict 5). If Mimo's cross-examination changes a ruling of 03, a row is added or removed, and K with it.
- **The declared inputs (L514) do not list Part VI's declared restriction operation** (settled S88 positions, "Found in settling", point 4). (S) and (B) depend on it (L289: "Fix \(\mathcal E\) and a declared restriction operation"). Derivation 6 is not made false: L586 allows declared indices and declared inputs, and Part VI declares the operation where it uses it. The looseness predates every S88 repair, and under the rider W20.2 adds nothing to it. The candidate clause for L514 is "the restriction operation of Part VI (\(E|W\))". It is not an entry.
- **Part II uses the notation of Parts IV and V before they introduce it** (W19.1, read in place). The new sentences at L121 use \(E\), \(E'\), \(\tau\), \(\tau'\), \(\lambda\) and "hidden ports", which L191, L233 and L235 introduce, with no pointer. A pointer such as "(Parts IV and V)" would close it, but it would change the settled wording, so it is left for X1 or the orchestrator. **Closed after the cross-examination:** W19.1 now types these terms inline, with pointers to Parts IV and V, before the settled sentences, which stay byte for byte (S90, Mimo A1, point 1).
- **"Active" is still undefined** (W20.1, read in place). L233 has "active commitments", and (F1) at L235 has "every active component". W20.1 makes Γ a set of components and puts the components that assign inputs in the named background. If "active component" is read as "member of Γ", (F1) no longer checks the named-background components one by one; (F2) still checks the whole. The settled position declined Mimo's "active" because it is undefined, and nothing is changed.
- **W20.1's "including any that assigns an input" has two readings.** On one, every component that assigns an input is outside Γ. On the other, any such component that the candidate leaves out of Γ is named background. The named verdicts are the same on both (the F3 reading's models 1a and 1b).
- **O45 against W20.1's "those the candidate offers as doing the work".** The phrase meets the case's "never described as doing anything". The entry holds the AGREE on L309 s3, W28.1 and W58(i).1, and asks X1 to test the row. **Closed after the cross-examination:** Mimo (part A1, point 2) named the move away on one reading, and W20.1 now adds "whether or not anyone has described their work", so O45 holds AGREE on firmer text (S90).

## Carried forward after S90

The S90 readings passed these on without a ruling, or the rulings named them as options. None is an edit in this draft. Each is to be decided by the orchestrator or taken up in a later revision, and any that changes the theory text needs an entry of its own.

**Notation.**
- **The letter \(G\)** (Mimo A1, point 4; batch 1). W20.2's block \(G\subseteq\Gamma\) shares its letter with the equation tag (G) of Part X and with the variable \(G\subseteq K\times F\) of Part XI. The reply proposes a new symbol. If one is adopted, it must also replace \(G\) in the fallback text in W20.2's CHECK (the R17 ruling).
- **Revised L339 names no block** (Atria A1, point 3; batch 3). Part VII's unchanged sentence names a pair but no block \(G\). It could name the deleted block, for example "with the skewness commitment as the deleted block". If adopted, it is a new entry.
- **R55's bijection** (Mimo A2, point 2; batch 1). W19.3 + W10(b).1 cites Derivation 2(ii) at revised L624 without exhibiting the bijection that meets its premise. Atria (A2, point 1; batch 2) exhibits it: \(\varphi\) is the exchange of the two things. Both replies find the premise met, and neither contests R55. An inserted clause is possible.

**Presentation.**
- **"The ground of its restriction"** at revised L159 (W57.1 + W32(b).1, R10; Mimo B1, point 4; batch 2). It is not defined, it meets Part IX's "grounds \(g\)", and its pointer to Part XIV and Part XIV's pointer back to Part III never say that the two expressions are the same. The reply offers a gloss and says that no verdict moves.
- **Bolded "declared inputs" at revised L31** (W7.1, R03; Mimo B1, point 5; batch 2). Now that W6.1 has removed the earlier mention at L25, the bolded term comes before any gloss of it. The reply offers a gloss.
- **Revised L51, "In Part XI, as a declared normative relation"** (file-11 L53, which no entry touches; the R39 rulings, batches 1 and 2). It is the one place left that calls \(\mathcal N\) "declared". It does not say "declared input", so the declarations of W6.1, W6.2, W6.3 and W6.4 + W14.1 stay true.

**Gaps in file-11 text outside the 55 changes.**
- **What an active route depends on** (the R48 ruling; batch 2). L369 defines an active route "under the declared contrasts", the dependence order does not place active routes, and L514 does not list declared contrasts. It is the same summary looseness as finding 9 above, and no reply raised it.
- **When a transport into \(c\) is faithful on \(c\)'s contract** (both R31 rulings; batch 3). A sentence at Part IV (L189) or at (R) (L205–208) could say that a transport into \(c\) is faithful on \(c\)'s contract when it is faithful on the pairs it carries into that contract. That would state in words the reading W21.1's \(\equiv_\ell\) and (N) already need.

**Reconciliations the pass relies on.**
- **R13 (W35.2) and R25 (W40.1).** In each, two checkers of batch 3 ruled one entry differently, and the batch-3 recorder, not a third checker, chose the text: Mimo C item 4's wording for R13, and Atria C item 5's FIX for R25. The pass uses those choices. The orchestrator may send either to a fresh checker, and a different ruling would change the entry again.

**Options the rulings left open, not taken in this pass.**
- **W19.2's declaration**: "differ in which component" could read "differ in nothing but which component" (batch 1, R51; batch 2 found the declaration accurate as it stands).
- **W38.1's line on selection**: "Here selection is blind: its history holds no represented target (Parts 0 and IV)" could read "Here selection has no represented target in its history (Parts 0 and IV)", so that the strict sense of "blind" appears in the sources note no more than in Part 0 (both R01 rulings). The pointer still lands as it stands.
- **W20.2's CASES AT RISK, O33**: the reply's "toward" reading could be recorded beside "holds AGREE", as "toward for accounts of the joint question on the mechanism-only reading, which the case does not claim" (the R17 ruling).
- **W17.2's heading** still says "the population is of realizable transports", the wording from before check 1's fix; NEW says "candidate transports" (the R42 ruling). It appears in neither the note nor the record.
- **W33.1's CASES AT RISK** still ends its O2 item with "this derives L275 s2's rule", which check 2 struck, and does not name O19, which check 2 added as watched (the R24 ruling). The theory text is unaffected.
- **W41.1's CHECK** says "O15 toward"; after the cross-examination it is read as support for the passage only, since file 11 already gives O15 AGREE (the R30 rulings). The S90 line in the same CHECK field says so.

## The entries

### W1.1 — The note replaces file 11's note

- **STATUS:** applied
- **GROUP:** M
- **ITEM:** W1
- **FILE-11 LINE:** 5
- **WHERE:** front matter, L5, file 11's italic revision note, the whole line. L6 (blank) is kept, and separates the note from the sources note (W38.1).
- **REASON WORD:** meta
- **KIND:** META
- **CHECK:** check 2, FIX. "Every change of that last kind" could be read as the reason word "change of claim"; the sentence now names the test.
- **OLD:**
````text
*Revision 1 (file 11), 22 September 2026. A rewrite of file 10 for coherence: the same primitives, definitions, conditions, constructions and derivations, in the same names and notation, reordered and restated so that every front-matter sentence defers to the exact statement in the body and every restatement of a theorem carries the theorem's own qualification. One claim changes: Derivation 3, whose unqualified form gave the wrong verdict on the audit's case O48 and whose proof already assumed the qualification (Semantics results S75). The three sentences that restated it (the answer to grievance 3, attack point (D), the Part XV entry) change with it. Nothing else changes in what is claimed.*
````
- **NEW:**
````text
<!-- META:NOTE BEGIN -->
*Revision 2 (file 13), @@DATE@@. File 11 with the changes listed in the revision record at the end of this document, and no other. The record gives each change with its old and new text, the reason it is made (erratum, clarification or change of claim), and whether a reader can conclude from it something file 11 left unconcluded. Every change from which a reader can conclude something file 11 left unconcluded is declared as a change of claim, one line each, below: @@N@@ of the @@M@@ changes. The record also lists every change in claim that file 11 made against file 10 and that file 11's own note did not declare: @@K@@ places. This note replaces file 11's note. This note, the note of sources and departures after it, and the record are not part of the theory and add nothing to it. Nothing else differs.*

**Changes of claim, in the order of the text.**

@@DECLARATIONS@@
<!-- META:NOTE END -->
````
- **DECLARATION:** made by the note itself ("This note replaces file 11's note. This note, the note of sources and departures after it, and the record are not part of the theory and add nothing to it."). Not counted in N or M.
- **REASON:**
  - Worklist W1 (XR1, XR2; det 02 C1; 03 M1, §5 XR1–XR2, §8 item 12; plan 1.3.1, 2.5; D6). File 11's note says "the same … definitions, conditions", which is false against L419, L433, L465, L473 and L514. It says "Nothing else changes in what is claimed", which is false against 41 places. Its list of restating sentences follows file 10's layout, and it names a case and a results file (XR2).
  - The paragraph follows plan 2.5's four sentences nearly word for word. Two sentences are added: the count of layer 2 ("@@K@@ places"), and the sentence that says what the note, the sources note and the record are. The latter declares the three meta entries.
  - The task template puts each CLAIM entry's DECLARATION line in the note. So the paragraph is followed, inside the same NOTE block, by one line per CLAIM entry, in the order of the text (conflict 2).
  - N, M, K and the list are filled by program from the change list, so the counts cannot drift from the entries.
  - The note names no case, record file, round or model. The fixed text was checked by script, and the build must re-check the filled note, since its lines come from the other groups.
- **CASES AT RISK:** none. The block is cut from every brief by construction (D6), as S81 withheld L5, and the cut restores exactly the text S81 sent (checked). No O- or N-case can move through it. The risk is a failed cut: the list would then point testers at every changed place, which is XR2's steering, widened. The build's md5 of the cut text and its withheld-word check guard against that.
- **GAIN:** A note a reader can trust. Every change of claim in this revision is named and counted, and file 11's silent changes are counted and pointed to.
- **LOSS:** The head of the authority file grows by about 50 lines once the list is filled. Plan 2.5's one-paragraph form becomes a paragraph and a list.

### W38.1 — The note of sources and departures

- **STATUS:** applied
- **GROUP:** M; edited 25 September (group H)
- **ITEM:** W38
- **FILE-11 LINE:** 7–9
- **WHERE:** front matter, after the note. It is inserted before the rule `---` at L7 that opens Part 0. The anchor is L7–L9 (the rule, the blank line and the Part 0 heading), kept byte for byte. L7–L9 belong to no group.
- **REASON WORD:** meta
- **KIND:** META
- **CHECK:** check 2, FIX. Five statements were inaccurate: what file 00 cites, Marletto's page for interoperability, Deutsch's definition of a problem, the Derivation 6 clause, and the stated-limits line against B1's wording. Three lines follow C's fixes (physical media, a separate matter, does no work by itself). The fallback table's substrate row now cites chapter 3, pp.88 and 95. The assembler also gave the fallback for "Surprise and problems" the corrected account of Deutsch's "problem", which check 2's fix (c) implies but did not write out.
  - **25 September:** four lines of NEW changed for W59.1 and the edits to W34.1 and W33.1, and the fallback table with them. *Idle parts* no longer says that how hard an account is to vary grades nothing, since Pres goes; it says that nothing grades a candidate for carrying a commitment that does no work. A line *Hard to vary* is added after it. *Reach* no longer gives a definition by jobs. *Surprise and problems* now names the problem for a question of Part VI and says that a problem in the wider sense "can be" a recognized difficulty, where it said "is", to agree with Part VI's "can be". Every other line is byte for byte as before. Checked by the drafter only; no outside reader has seen these lines.
- **OLD:**
````text
---

# Part 0 — Read this first
````
- **NEW:**
````text
<!-- META:SOURCES BEGIN -->
*Sources and departures.*

**Sources.** The semantics has two sources, named as such by its owner: Chiara Marletto, *The Science of Can and Can't* (2021), and David Deutsch, *The Beginning of Infinity* (2011). Its predecessor is the FW5 construction of 8 September 2026 (file 00), whose reference list cites articles by the two authors, not these books. The task wording of the physical module (Part XII) is constructor theory's, from Deutsch's paper "Constructor Theory", *Synthese* 190 (2013), which file 00 cites. The definitions, conditions and derivations are this document's own. None is attributed to either book, and this note says nothing about what follows from them.

**Close parallels, named and not claimed as derived.** Derivation 9's last sentence, declared provenance, "relay is not" construction (Part X) and reason use (Part IX) have close parallels in Deutsch, chapter 7, pp.155–161, and chapter 16, p.406. Inexplicit representation (Part X) has one in Deutsch, chapter 16, pp.405 and 412. Part I's substrate independence, held so far as the adopted physics lets contents pass between physical media, matches the interoperability principle as Marletto states it (chapter 3, pp.87–88; its consequence for universal computers, p.95).

**Departures.** The semantics departs from the books on purpose at these places.
- *Explanation.* Deutsch counts a false myth as an explanation (chapter 1, p.19). Here that is an explanatory candidate (Part V). Part I's fallibility commitment uses "explanation" for an account on a contract, and how hard an account is to vary is a separate matter (Part VI).
- *Idle parts.* Deutsch counts superfluous features as a defect of an explanation (chapter 1, p.25). Here (E) has no condition that each commitment do work: a commitment that does no work by itself is critical in no support, and nothing in the semantics grades a candidate for carrying one (Parts 0 and VI).
- *Hard to vary.* Deutsch calls an explanation good or bad as it is hard or easy to vary while still accounting for what it purports to account for (chapter 1, p.31), and a myth easy to vary because its details could be changed without changing its predictions (pp.20–22). Here hard-to-vary is stated through rivals and problems, with no measure or count of variants (Part VI). Two rivals that both fit what is established pose a problem, a conflict between ideas in his sense (p.17); a pair of the question's contract at which they conflict is a test that solves it, as an experiment decides between two viable theories whose predictions conflict (p.16); and a candidate is easy to vary when it has a rival that fits as well and conflicts with it nowhere the question covers, as his variant of the myth in which Demeter sends the warmth south agrees with the myth on every season the Greeks knew (p.21). Three departures remain. He judges ease of variation before any variant is offered, and would reject a bad explanation without any experiment (p.25); here it is shown only by offering the rival, which is the criticism. He holds that an explanation able to fit anything in its field explains nothing (p.22); here a candidate with such a rival is an account of its question when it meets (E), and the remedy is a finer question. And variants whose differing details do no work, which he finds reduce to one core explanation (p.21), are here one account written two ways, not rivals (Derivation 2).
- *Reach.* Deutsch's reach is the power of an explanation to solve problems beyond those it was made for (chapter 1, p.28). Here the word is not defined, and nothing is measured by how many questions a candidate answers; whether a candidate is an account of a question is fixed by the candidate and the world, whether or not anyone has asked the question (Parts I and VI).
- *Stated limits.* Both books hold that a limit of scope needs an explanation (Deutsch, chapter 1, pp.27–28; Marletto, chapter 1, p.24). Here a stated limit is recorded and not certified: meeting the conditions of an account on a restricted contract certifies nothing about the restriction, and a verdict on a restriction whose ground the claim states is given with that ground (Part III).
- *Selection.* Deutsch calls criticism and experiment a selection (chapter 4, p.78). Here selection is blind: its history holds no represented target (Parts 0 and IV).
- *Surprise and problems.* For Deutsch a problem is a situation in which conflicting ideas are experienced, and a problem can arise without any observation (chapter 1, p.17). Here surprise is kept for selected transports (Part IV). A problem for a question is narrower: two rivals that both fit what is established (Part VI). A problem in his wider sense can be a recognized difficulty (Part X): a failure of a claimed obligation, or a conflict in which meeting a claimed obligation fails a protected one (Part XI), when the system represents it.
- *Elimination.* Deutsch asks an eliminative explanation to explain why what it denies seems to exist (chapter 7, p.154). Here why the absent structure appears is a separate question with its own contract, which an account of the absence neither answers nor needs to (Part VII).
- *Acquisition.* Deutsch holds that grasping any idea takes conjecture (chapter 4, p.94; chapter 16, pp.403–406). Here not every acquisition is construction: reconstruction by a learner is, and relay is not (Part X).
- *Knowledge as self-preserving information.* Marletto defines knowledge as information that can keep itself instantiated in physical systems (chapter 5, p.155). The semantics leaves this out: its class is explanatory creativity, and knowledge in that sense would be an attribution of the physical module, outside the class.
- *Universality and aesthetics.* Deutsch holds that people are universal explainers (chapter 6, p.146) and that there are objective truths in aesthetics (chapter 14, p.368). The semantics abstains on both. It defines the universal class and shows no one to belong to it (Parts 0 and XIII), and it takes worth as an input and derives no aesthetics (Part XI).

Page numbers are the printed pages of the editions named. A third book, named by the owner as further reading, is not a source and is not cited.
<!-- META:SOURCES END -->

---

# Part 0 — Read this first
````
- **DECLARATION:** made by the note ("the note of sources and departures after it … not part of the theory and add nothing to it"). Not counted in N or M.
- **REASON:**
  - Worklist W38 (verify obs 1, 3 and 10; decision S19); plan 1.3.6.
  - The content is plan 1.3.6's: the sources; the constructor-theory lineage of Part XII (00:910 and 00:1416, [R2]); the FW5 predecessor; the close parallels (Deutsch, chapters 7 and 16); and the eight departures it lists.
  - Added, because other groups' entries send them here:
    - reach (C's C12 on W34.1);
    - elimination (C's C12 on W40.1);
    - the mapping of "problem" to the recognized difficulty (C's W35.3 reason);
    - interoperability, a term kept out of the theory (C's W45.1 reason);
    - blind selection (A's W37.1 reason).
  - Also added: inexplicit representation as a parallel (D pp.405, 412), since C's W41.1 restores it from file 00.
  - No book is quoted, so plan 1.3.6's 25-word limit is met trivially.
  - **Page numbers.** Each was checked against the extracted text of the named editions, by locating a phrase from the page with `sources/locate.py`: Deutsch pp.17, 19, 25, 27–28, 28, 78, 94, 146, 154, 155, 156, 160–161, 368, 405, 406 and 412, and Marletto pp.24, 95 and 155, each in the chapter named. Deutsch pp.403–406 was read (the passage on how memes are acquired, which runs across those pages). Plan 1.3.6 asks the writer to recheck at freeze.
  - **25 September: hard to vary.** The owner's position of 24–25 September states hard-to-vary through rivals and problems (W59.1), and this note says so. Deutsch p.17 on problems as conflicts, p.16 on experiment between two viable theories, pp.20–22 on ease of variation (p.21, the southern variant and the one core of the Persephone and Freyr myths; p.22, an explanation that could explain anything), p.25 on rejection without experiment, and p.31 (glossary, good and bad explanation). Each page was checked with `sources/locate.py` on a phrase from the page. No book is quoted: the lines paraphrase. The departures recorded are the three that remain after the change: judgement before a rival is offered, the name of explanation kept for an account with an easy rival, and label-only variants read as one account. The *Surprise and problems* line changes "is" to "can be" for the wider sense, since Part VI now says a represented problem for a question "can be" a recognized difficulty, and "is" would contradict it.
  - **Named and not named.** The decision number (S19) is not named, because no meta block names a record file. The third book is mentioned and not named or cited, since plan 1.3.6 says it is not cited.
  - Each line that rests on another group's entry has a fallback, given below, for use if that entry is dropped under plan 1.5's cap.
- **CASES AT RISK:** none. The block is cut from every brief (D6), and "Deutsch" and "Marletto" are on the build's withheld list (plan 2.5). If it reached a tester, the departures would steer readings toward the books' judgements at exactly the guard rows: idle parts (N1, N25), hard to vary (N2, N3, N5, N25, O24), stated limits (O1, O5, O8, N7), selection (O11, N11), surprise (O3, N18, N19) and elimination (N22).
- **GAIN:** Lineage, and honesty about where the semantics departs from its two sources.
- **LOSS:** Readers may hold the theory to the books (worklist W38). The authority file grows by about 720 words.
- **FALLBACKS:** if an entry a line of the sources note rests on is dropped under plan 1.5's cap, the line is replaced by the fallback, or dropped where none is given.

  | line | rests on | fallback |
  |---|---|---|
  | Inexplicit representation (parallels) | C W41.1 | drop the sentence |
  | Part I's substrate independence (parallels) | C W45.1 | Part I's substrate independence is stated without condition; Marletto treats the interoperability of carriers as a law of physics that may fail (chapter 3, pp.88 and 95). |
  | Explanation | C W36.1 | - *Explanation.* Deutsch counts a false myth as an explanation (chapter 1, p.19). Here that is an explanatory candidate (Part V), and Part I's fallibility commitment uses "explanation" for what is not in error in the dependence alleged to do the work. |
  | Idle parts | C W33.1 (the words 'does no work by itself'); H W59.1 ('Nothing here … grades'); the claim itself holds on file 11 | - *Idle parts.* Deutsch counts superfluous features as a defect of an explanation (chapter 1, p.25). Here a commitment that does no work does not stop a candidate from being an account; Part VI reports it. |
  | Hard to vary | H W59.1 | - *Hard to vary.* Deutsch calls an explanation good or bad as it is hard or easy to vary while still accounting for what it purports to account for (chapter 1, p.31). Here no measure of variation is stated and nothing is graded (Parts 0 and XIV). |
  | Reach | H W59.1 (the sentence on questions nobody has asked) | - *Reach.* Deutsch's reach is the power of an explanation to solve problems beyond those it was made for (chapter 1, p.28). Here the word is not used, and whether a transport is faithful on a contract does not depend on anyone's accepting it (Part I). |
  | Reach, if W34.1 as edited is dropped | C W34.1 | - *Reach.* Deutsch's reach is the power of an explanation to solve problems beyond those it was made for (chapter 1, p.28). Here the word is used once, for the jobs an account is held to (Part VI), and is not defined. |
  | Stated limits | B1 W57.1 + W32(b).1 | - *Stated limits.* Both books hold that a limit of scope needs an explanation (Deutsch, chapter 1, pp.27–28; Marletto, chapter 1, p.24). Here a stated limit is recorded, and what makes it appropriate is a criticizable part of the claim that the semantics does not certify (Part III). |
  | Selection | A W37.1 for 'Parts 0 and'; the claim holds on file 11's Part IV | (replace "(Parts 0 and IV)" with "(Part IV)") |
  | Surprise and problems, if W59.1 is dropped | H W59.1 | - *Surprise and problems.* For Deutsch a problem is a situation in which conflicting ideas are experienced, and a problem can arise without any observation (chapter 1, p.17). Here surprise is kept for selected transports (Part IV). A problem in his sense is a recognized difficulty (Part X): a failure of a claimed obligation, or a conflict in which meeting a claimed obligation fails a protected one (Part XI), when the system represents it. |
  | Surprise and problems | C W35.1-W35.3 | - *Surprise and problems.* For Deutsch a problem is a situation in which conflicting ideas are experienced, and a problem can arise without any observation (chapter 1, p.17). Here surprise is kept for selected transports (Part IV), and the recognized difficulty of a critical episode (Part X) is not defined. |
  | Elimination | C W40.1 | drop the sentence |

### W37.1 — Part 0's account of selection: no represented target in the history

- **STATUS:** applied
- **GROUP:** A
- **ITEM:** W37
- **FILE-11 LINE:** 15
- **WHERE:** Part 0, "What this document claims", paragraph 2 (L15), sentence 3. The skeleton's "L15 s2" is this sentence: L15 s1 is "Correspondence … is not a primitive here" and s2 is "It is a relation with a provenance".
- **REASON WORD:** clarification
- **KIND:** ORDER
- **CHECK:** check 1, FIX (kind only). The added words copy what L197 and L203 already state, so the change is ORDER, as 03 ruled the same place (M2, upheld). Declaring it would put a false line in the note. KIND is ORDER and the declaration is none; if a checker rules CLAIM, the drafted line below is used.
  - S90 cross-examination: s90_xexam_mimo_A1, point 3 (R01 STANDS, naming an undeclared change of claim on a strict reading); s90_xexam_atria_A1, pass 2, point 1 (R01 FALLS) — FIX (two rulings, same text), after the cross-examination. S90: FIX (Mimo A1 point 3, batch 1; Atria A1 point 1, reconciled, same text)
- **OLD:**
````text
A correspondence can be *selected*, produced by variation and survival on a history of encountered changes;
````
- **NEW:**
````text
A correspondence can be *selected*, produced by variation and survival on a history of encountered changes, with no represented target in that history;
````
- **DECLARATION:** none (ORDER, after check 1; listed in the record). If a checker rules CLAIM: "Part 0 now says that a selection history holds no represented target, as Part IV states." (Fallback line reworded after the cross-examination, S90, since the old one began "Part 0 again calls selection blind".)
- **REASON:** W37 (source point 9; verify obs 9, CONFIRMED: "File 11 made the vocabulary clash worse"). File 10 L13 had "blind variation and survival"; file 11 dropped "blind" while the body keeps the blindness (L197: no member of the history represents t, H or the survival condition; L203: a selected transport has no represented target and no criticism in its history). The added words pin "blind" to the body's sense, so the ordinary wider use of "selection" (which includes choice by a critic) is not read into Part 0. The departure from the books' wider usage goes in the sources note (W38), not in the theory. KIND: 03 ruled the drop (M2) WORDING, but as a named close call, and all four readers ruled it CLAIM; under the strict rule this entry is CLAIM. The plan's expected ruling was WORDING, so the checkers may rule it down; declaring it costs one line in the note.
  - After the cross-examination (Mimo, part A1, point 3; Atria, part A1, pass 2, point 1), "blind" is deleted.
  - Its ordinary strict sense, variation not directed in any way (for example by a cue or a gradient that represents nothing), says more than Parts I–XVI state (S81 03 M2, R1's close call). That breaks Part 0's rule that "the front matter states nothing the body does not state more exactly".
  - The clause alone states the body's sense.
  - Atria's alternative, adding blindness to Part IV's Selected, is refused as an undeclared CLAIM change to the body.
- **CASES AT RISK:** O11 (Monday's key-trying is variation and survival with no represented target): holds AGREE, toward if anything. N9 (selection puts the wing colour in what the moths inherit): holds. N11 (the teacher chooses among Jana's drafts): watched; the added words make plain that a chooser who represents what she wants is not a selection history in this sense, which fits the verdict's "the teacher's choice" and moves no mark I can find. No other O- or N-case turns on Part 0's wording of selection.
- **GAIN / LOSS:** GAIN: Part 0 and Part IV say the same thing, and "selection" cannot be read as criticism-by-choice. LOSS: None in the theory; "selection" stays narrower than ordinary use (recorded in the sources note). After the cross-examination (S90), Part 0 no longer uses file 10's word "blind".

### W6.1 — L27 s2: what the semantics does with the measures it does not supply

- **STATUS:** applied
- **GROUP:** B1
- **ITEM:** W6
- **FILE-11 LINE:** 27
- **WHERE:** Part 0, "What this document does not claim", L27 s2.
- **REASON WORD:** erratum
- **KIND:** CLAIM
- **CHECK:** check 1, SOUND. O6 and O8 are real watches: the new text says outright that a claim needing a merit function or a probability of truth is unsettled.
- **OLD:**
````text
Where a claim needs one of these, the semantics takes it as a **declared input** and marks the place (Parts XI, XIV).
````
- **NEW:**
````text
Where a claim needs one of these, the semantics does not supply it and marks the place: a claim of worth or of aesthetic value takes the normative relation as an input (Parts XI, XIV), and a claim that needs any of the others is unsettled (Part XIV).
````
- **DECLARATION:** Part 0 no longer says that each measure it does not supply is taken as a declared input: a claim of worth or of aesthetic value takes the normative relation as an input, and a claim that needs a probability of truth, a merit function or a ranking of thinkers is unsettled.
- **REASON:** Worklist W6 (XR3; det 02 C7 and C10; 03 M3 and 03 §8 item 4). L27 s2 sends all five measures to "a declared input" in Parts XI and XIV. The body carries only worth and aesthetics, through \(\mathcal N\). L514 excludes \(\mathcal N\) from the declared inputs ("Besides the two primitives"), and no place carries a probability of truth. So L37's rule ("the front matter states nothing the body does not state more exactly") is false of L27. NEW is XR3's sentence (plan 1.3.1) with one addition, "or of aesthetic value". Without it, the aesthetic case of L447 would be read among "the others" and made unsettled even when \(\mathcal N\) is given. L27 s3 is kept, as the plan requires. The pointer "(Part XIV)" in NEW is made true by W6.4.
- **CASES AT RISK:**
  - O12 stays SILENT on the worth point ("its merit is real"). It now rests on stated words, together with W6.4. Its SILENT point may also take in "better question", since a ranking of questions is unsettled. The mark is the same.
  - O40 stays AGREE. 04 §2.2 item 4 cited L27 s2's "declared input" for a ranking. Under NEW, a claim that needs a ranking is unsettled, so neither party can make the "mostly" claim, and the verdict is still reached by 04 §2.2 items 1–3. It moves AGREE→SILENT (away) only for a reader who takes "unsettled" to cover a verdict that denies the claim can be made.
  - O21, O27 and O50 stay SILENT. They need a weighting of credit, not a ranking of thinkers, and W6.4 names that weighting.
  - O6 ("a good reason to believe") and O8 ("a good explanation") are watched. They move away (AGREE→SILENT) only if "good" is read as needing a merit function. O6's point is identification (L153), and O8's is scope (L161 s1–s2).
  - O35 and O38 are untouched: neither makes a worth claim.
  - N-cases: N11 is watched only if "what is good in her final essay" is read as a worth claim, but the situation states that the essays are good. No other N-case turns on worth, merit, probability or a ranking; the case books were searched for these words.
- **GAIN:** Part 0 claims only what the body carries, and L37's rule holds of L27.
- **LOSS:** Old L27 held that a stated probability, merit function or ranking would settle a claim as a declared input, though no part of the body supported this. That reading is withdrawn.

### W7.1 — L33 s3: derived from the primitives, the indices and the inputs

- **STATUS:** applied
- **GROUP:** B1
- **ITEM:** W7
- **FILE-11 LINE:** 33
- **WHERE:** Part 0, "What is primitive, what is an index, and what is derived", L33 s3.
- **REASON WORD:** erratum
- **KIND:** CLAIM
- **CHECK:** check 1, SOUND.
- **OLD:**
````text
Everything else is derived, in the order Part XIV states.
````
- **NEW:**
````text
Everything else is derived from the two primitives, the declared indices and the **declared inputs**, in the order Part XIV states.
````
- **DECLARATION:** Part 0 now says that everything else is derived from the two primitives, the declared indices and the declared inputs, where it said only that everything else is derived.
- **REASON:** Worklist W7 (XR6; det 02 C66 and C80). 03 §8 item 2: "everything else is derived" at L33 and L512 stands against L514's declared inputs. Derivation 6's claim (L586) already names declared indices and declared inputs, and L33 now says the same (plan 1.2 wording). "declared inputs" is bold because, after W6.1, L33 is the place where Part 0 names the category, as it names "declared indices" in s2.
- **CASES AT RISK:** None. O37 and O49 rest on L518's last sentence, which is kept. No case cites L33 s3; 03 ties L33 only to O12 and O35, through s1 (M5). This was checked.
- **GAIN:** Part 0 no longer says that everything is derived from the primitives while Part XIV takes inputs it does not supply.
- **LOSS:** None.

### W58(ii).1 — L33 s4: no such predicate is primitive or depended on

- **STATUS:** applied
- **GROUP:** B1
- **ITEM:** W58(ii)
- **FILE-11 LINE:** 33
- **WHERE:** Part 0, "What is primitive, what is an index, and what is derived", L33 s4. It is in the same paragraph as W7.1, and the two anchors do not overlap.
- **REASON WORD:** clarification
- **KIND:** WORDING
- **CHECK:** check 1, FIX (kind only). 03 ruled L33 s2–s4 ORDER (M6, upheld) and read "appears anywhere" as L590's "no residual predicate" (03 §8 item 11), so the new words say what the old ones meant. KIND is WORDING and the declaration is none; if a checker rules CLAIM, the drafted line below is used.
  - S90 cross-examination: s90_xexam_mimo_B1, point 1 (R04 FALLS) — KEEP, after the cross-examination. After the cross-examination (s90_xexam_mimo_B1, point 1, R04 FALLS: 'weaker claim in WORDING guise'): KEEP. The reply reads 'a predicate meaning …' and L590's 'residual' as covering derived predicates. On that reading, both OLD and L518 are false in file 11 itself, which defines explanation (L13), a proof's explaining (L51), the causal assignment (L125–129) and knowledge and representation (L512), and whose (RC) depends on (EK) and (E). On the only reading the text bears, the unanalyzed predicate, OLD and NEW say the same thing. The second half copies L518. Derivation 6's proof reaches L518/L520. Atria (s90_xexam_atria_B1, point 2) found the entry standing.
- **OLD:**
````text
No predicate meaning "really explains", "is a cause" or "is knowledge" appears anywhere (Derivation 6).
````
- **NEW:**
````text
No predicate meaning "really explains", "is a cause" or "is knowledge" is taken as primitive, and no definition depends on one (Derivation 6).
````
- **DECLARATION:** none (WORDING, after check 1: ORDER against L518 and L590; listed in the record). If a checker rules CLAIM: "Part 0 now says that no predicate meaning "really explains", "is a cause" or "is knowledge" is taken as primitive or depended on by any definition, where it said that none appears anywhere."
- **KIND AS DRAFTED:** CLAIM. The claim is the one already made at L518 ("Nothing depends on a predicate meaning …") and L590 ("There is no residual predicate meaning …"). But the entry closes a reading that is literally false, since file 11 mentions "is a cause" at L55, L123 and L129. Under plan 1.1, closing an open reading is CLAIM. If the checkers rule it ORDER against L518 and L590, it moves to the record's WORDING list.
- **REASON:** W58 (plan section 0 and 1.2; 03 §8 item 11: "'appears anywhere' at L33 s4 must mean L590's 'no residual predicate'").
  - **Departure from the skeleton's wording.** The skeleton and plan give "is defined or presupposed (Derivation 6)". That wording is not used, because "defined" would contradict the text at three places:
    - Derivation 6 claims that every predicate in Parts II–XIII *is* defined (L586).
    - (EK) defines a predicate of knowledge creation (L437–443).
    - Part II describes "a causal assignment" as a family of signatures (L123–129).
  - NEW uses the words of L518 and L590 instead.
- **CASES AT RISK:** None. No O-case or N-case turns on L33 s4. 03 records M6 (L33 s2–s4) as touching no case. This was checked.
- **GAIN:** Part 0 no longer states something the document itself contradicts.
- **LOSS:** None.

### W8.1 — Qualify Part 0's short form of attack (D)

- **STATUS:** applied
- **GROUP:** A
- **ITEM:** W8
- **FILE-11 LINE:** 63
- **WHERE:** Part 0, "Where to attack this" (L63), the fourth item of the "In short" list.
- **REASON WORD:** erratum
- **KIND:** ORDER
- **CHECK:** check 1, SOUND. KIND is ORDER, as check 1 reads it: 03 ruled the L63 short form ORDER (M12), and the entry copies L534. The drafter wrote WORDING (ORDER).
- **OLD:**
````text
(D) the two provenances and the underdetermination of selected transports;
````
- **NEW:**
````text
(D) the two provenances and the underdetermination of selected transports at unseen changes where their population admits a differing survivor;
````
- **DECLARATION:** none (WORDING, ORDER: copies the qualification Part XV states at L534; listed in the record). If a checker rules CLAIM: "Part 0's short form of the genesis claim now carries Derivation 3's qualification."
- **REASON:** W8 (det 02 C22 and §5(i); 03 M12 ORDER, UPHELD, no reader dissent; 03 §5 XR12 note). The short form is the only restatement of Derivation 3 without the theorem's qualification; L43, L534 and L562 all carry it. The words follow L534 ("at an unseen change … its population admits a differing survivor there"). The labels themselves are untouched (D9).
- **CASES AT RISK:** O48 (weak): toward, or holds AGREE; a reader who cites L63 alone can no longer read an unqualified underdetermination claim (03 §6 lists "any reading that cites L63"). O24: holds AGREE (the differing arrangement is reachable, so the qualification is met). No N-case (N14, the robot population, is set aside).
- **GAIN / LOSS:** GAIN: Every restatement of Derivation 3 carries its qualification. LOSS: The short list is a little longer.

### W36.1 — Part I: which sense of "explanation" the fallibility commitment uses

- **STATUS:** applied
- **GROUP:** C
- **ITEM:** W36
- **FILE-11 LINE:** 71
- **WHERE:** Part I, "Fallibility without falsehood-as-work" (L71). One sentence is added after s2; s1 and s2, the commitment, are unchanged.
- **REASON WORD:** clarification
- **KIND:** CLAIM
- **CHECK:** check 2, FIX. "A separate measure" meets L27's "a measure of worth" and B1's "no merit function"; NEW reads "a separate matter". Cases: as drafted, plus N1 watched (the Γ question, as C's C7) and N4 Q2 watched (with W34.1).
  - S90 cross-examination: s90_xexam_atria_C, point 3 (R06 STANDS, naming a move toward on N3) — KEEP, after the cross-examination. Cross-examination of revision 2 (S90 part C): Atria gave STANDS and named, under (d), a move toward the fixed verdict on N3: the candidate/account distinction gives "No, it does not explain" with "Yes, an explanation … only in form", which the old s2 read literally denied. Mimo gave STANDS with no point. Ruled KEEP after the cross-examination: the move is toward, and it follows from the declaration's two clauses ("explanation" means an account; a false theory offered as an answer is a candidate that ordinary usage may call an explanation). The "No" rests on (F1) and non-circular dependence (L255, L273). N1 holds (s1, L231, R24), N2 holds or moves toward, and O8, O15 and N22 hold. The pointers to Part V and to Part VI (L313) are exact.
- **OLD:**
````text
What cannot count as explanation is an error in the very dependence alleged to do the work.
````
- **NEW:**
````text
What cannot count as explanation is an error in the very dependence alleged to do the work. "Explanation" in this commitment means an account, an explanatory candidate satisfying \(\operatorname{Account}\) on its contract (Part V); a false theory offered as an answer is an explanatory candidate, which ordinary usage may still call an explanation, and how hard an account is to vary is a separate matter (Part VI).
````
- **DECLARATION:** Part I now says that "explanation" in its fallibility commitment means an account in Part V's sense, that a false theory offered as an answer is an explanatory candidate which ordinary usage may still call an explanation, and that how hard an account is to vary is a separate matter (Part VI).
- **REASON:** Worklist W36 (source point 4; verify obs 4, CONFIRMED as a difference of terms; raw 01c O15, a hard case; det 01 O15, confidence medium-low). L71 s2 says "What cannot count as explanation is an error in the very dependence alleged to do the work." In ordinary usage, and in the source the audit read, a false theory is still an explanation. File 11's own word for that sense is "explanatory candidate" (L233), and it lets such a content be false (L213: "A system can represent a false theory"; L399: "A system may understand a false theory"). The new sentence says which sense L71 uses. As plan 1.2 and plan conflict 10 require, a sentence is added, the commitment sentence is left as it is, and nothing is capitalized. The skeleton's "how good an explanation is belongs to Part VI" is written as "how hard an account is to vary is a separate measure (Part VI)". This places the source's "good" without naming it and without a grade, which L27 would forbid, and W33.1 says that measure grades nothing. "A false theory" is file 11's own phrase. "Myth" is not used, so the text does not echo a candidate case. KIND: the sentence states for the first time which of two senses a commitment sentence uses, and so closes a reading (plan: clarification → CLAIM).
- **CASES AT RISK:**
  - O15: watched. It holds AGREE, toward if anything. Its "his account" is the ordinary sense. The sentence marks the technical sense as Part V's, so it moves only for a reader who now reads every "account" as Account.
  - O8: watched. "A good explanation with an honest scope" moves AGREE→SILENT (away) only for a reader who takes "good" to need Part VI's measure, which the sentence calls separate. O8's point is scope (L161). B1's W6.1 carries the same watch.
  - O1 stays SILENT. Its point is the retreat, not the sense of "explanation". O2, O4, O7 and O13 hold: their "explains" is Account on the question asked.
  - N3: toward on both questions. "It does not explain … it is an explanation only in form, an attempt, a false one" describes a candidate that fails Account and that ordinary usage calls an explanation. N2 holds, or moves toward (the patched myth is a candidate that fails).
  - N1, N7, N8, N16, N22 and N25 hold. N17 carries no mark prediction; its "only in a thin sense" belongs to W44, which is left out, and this sentence does not move it.
- **GAIN:** The commitment's "explanation" is tied to Part V, and a false theory has a named place.
- **LOSS:** Part I grows by one sentence.

### W45.1 — Part I: substrate independence holds relative to the physics' interoperability

- **STATUS:** applied
- **GROUP:** C
- **ITEM:** W45
- **FILE-11 LINE:** 77
- **WHERE:** Part I, "Substrate independence with physical obligations" (L77). Two sentences are added after s2; s1 and s2 are unchanged.
- **REASON WORD:** change of claim
- **KIND:** CLAIM
- **CHECK:** check 2, FIX. "Kind of carrier" used "kind", a defined, contract-relative word of the theory (L13; attack (C) in Part XV). NEW reads "physical medium". The sources note follows.
  - S90 cross-examination: s90_xexam_mimo_C, point 2 (R07 FALLS) — KEEP, after the cross-examination. Cross-examination of revision 2 (S90 part C): Mimo said FALLS (the declaration omits that bearability and passage between media are "fixed by the adopted physics"); Atria said STANDS. Ruled KEEP after the cross-examination: bearability is the physical module's to fix already in file 11 (L33, L215, L509; Part XII L453), and passage is in the declaration's "so far as the adopted physics lets contents pass", so the clause changes no claim and the declaration is exact.
- **OLD:**
````text
Every attribution of an organization to a physical system must be permitted by the adopted physics.
````
- **NEW:**
````text
Every attribution of an organization to a physical system must be permitted by the adopted physics. Which organizations a carrier can bear, and whether what carriers of one physical medium bear can pass to carriers of another, are fixed by the adopted physics, and substrate independence holds so far as that physics lets contents pass between media. Where two media cannot exchange what they bear, the contents that only one of them can bear form, for a system built of the other, a barrier in the sense of Part XIII.
````
- **DECLARATION:** Part I's substrate independence now holds only so far as the adopted physics lets contents pass between physical media; where two media cannot exchange what they bear, the contents only one of them can bear form a barrier, in Part XIII's sense, for a system built of the other.
- **REASON:** Worklist W45 (missed relation M4; 00:912 [R3], which file 10 dropped). Part I states "Any carrier may bear an organization" without condition. The source treats interoperability, the passing of what one kind of carrier holds to another, as a contingent law of physics. Where it fails, a universe has no universal computer. File 00 cited that principle, and files 10 and 11 dropped it. The added sentences make substrate independence relative to the adopted physics, which L77 s2 already makes the judge of every attribution. They also say what a failure of interoperability gives, in Part XIII's own terms: a barrier is "an independently characterized domain for which every admitted, non-question-begging enabling condition leaves the relevant capability unavailable" (L487). "Whether what one kind bears can pass to another" is interoperability in plain words. The term itself stays out of the theory and goes to the sources note (W38). KIND: it narrows a commitment (skeleton: "a narrowed commitment").
- **CASES AT RISK:**
  - N24: toward. For a system of either sort, the calculations only the other sort allows are a barrier, so (U1) and (U2) fail for every system. Bram's reason explains this together with the stated fact that each sort allows calculations the other cannot, which is the sentence's "contents that only one kind can bear".
  - O-cases: none moves. O28, O42, O43 and O44 (transfers between carriers) were checked. Each situation states that the transfer took place, so the physics permits it. Interoperability belongs to the physical module and is not a declared input (L514), so no case becomes unsettled for want of it. O14 and O49 are not affected.
  - No other N-case turns on transfer between kinds of matter.
- **GAIN:** Part I no longer commits the semantics to what only the physics can supply, and the barrier in a world without interoperability can be stated.
- **LOSS:** Substrate independence is no longer unconditional.

### W19.1 — The sentence after (K): kinds across two candidates

- **STATUS:** applied
- **GROUP:** A
- **ITEM:** W19
- **FILE-11 LINE:** 121
- **WHERE:** Part II, "Kinds are edit-signatures" (L121). Three sentences are inserted after sentence 2, "A kind is an equivalence class of components under this relation.", the anchor W19's placeholder reserved: a typing sentence, added after the cross-examination (s90_xexam_mimo_A1, point 1), and the two settled sentences. Sentences 1–2 are kept byte for byte. W30.1 appends its sentences after sentence 3; the two OLD texts do not overlap (skeleton conflict 1).
- **REASON WORD:** clarification
- **KIND:** CLAIM
- **CHECK:** not put to check 1 or check 2, which ran before S88 was settled. The text is the settled wording (`results/S88 Reading of Mimo's reply in three parts, and the settled positions.md`, F1, block 2; committed at 3ebb6d8), copied byte for byte. Checked by its drafter: the whole list applied by the program into a scratch draft with no refusal and no overlap, the new text read in place, and the guard rows worked below. No outside reader has seen this wording; the cross-examination of revision 2 (X1) must carry it.
  - S90 cross-examination: s90_xexam_mimo_A1, point 1 (R08 FALLS) — FIX, after the cross-examination. The two settled sentences use \(E\), \(E'\), \(\tau\), \(\tau'\), \(\lambda\), "hidden ports" and "the port translation" before Parts IV and V define them, with no pointer; the content is sound. A typing sentence in Part IV's and Part V's own words is inserted before them, and they stay byte for byte (NEW grows from 84 to 131 words). KIND CLAIM and the declaration are unchanged: the added sentence restates definitions and makes no claim. The reply's move to Part V is refused (it would overlap W20.1's place, take the definition across candidates away from (K), and leave "Kinds are edit-signatures" without the sense of "one kind" that Derivation 2 uses). O9, O10 and O22 hold; N25's second question is as before. Atria (s90_xexam_atria_A1, pass 2, point 4) found the declaration accurate and the forward notation a blemish, not incoherence, and gave STANDS; this fix answers that blemish.
- **OLD:**
````text
A kind is an equivalence class of components under this relation.
````
- **NEW:**
````text
A kind is an equivalence class of components under this relation. For two explanatory candidates (Part V), let \(E\) and \(E'\) be their organizations and \(t=(\pi,\tau,\sigma,\lambda)\) and \(t'=(\pi',\tau',\sigma',\lambda')\) their transports from \(D\), where \(\tau\) translates edits, \(\sigma\) translates boundaries, and \(\lambda\) assigns each component of \(E\) a subnetwork of \(D\), its anchor, with a port translation (Part IV). A component of \(E\) and a component of \(E'\) are of one kind on \(C\) when their signatures, read on \(C\) through \(\tau\) and \(\tau'\), coincide under a footprint bijection; Derivation 2 uses kinds in this sense. Derivation 1 makes the like comparison between a component \(k\) of \(E\), read on \(C\) through \(\tau\), and its anchor \(\lambda(k)\), read on \(C\) directly with its hidden ports projected away, up to the port translation.
````
- **DECLARATION:** Part II now defines when a component of one candidate's organization and a component of another's are of one kind on C: their signatures, read on C through the two candidates' transports, coincide under a footprint bijection. It says that Derivation 2 uses kinds in this sense, and that Derivation 1 makes the like comparison between a component, read through its transport, and its anchor, read on C directly with its hidden ports projected away.
- **REASON:**
  - W19 (S88 finding F1, settled UPHELD; plan 1.3.3, which takes the sentence after (K) with either wording of Derivation 2). (K) at L121 defines a kind for two components of one organization under one contract. No sentence says how a component of \(E\) and a component of \(E'\) are compared, and Derivation 2 compares them (the F1 reading, 3.4; Mimo's F1 point 3, kept). W19.2 needs the comparison stated.
  - **The second sentence** is the settled change 2. Derivation 1 (L546) compares a component of \(E\), read through \(\tau\), with its anchor subnetwork of \(D\), read on \(C\) directly; it does not compare a component of \(E\) with a component of \(E'\). The post-Atria sentence said "Derivations 1 and 2 use kinds in this sense" (Mimo's F1 point 4; the F1 reading's change B). Settling reworded the reader's proposal so that it names \(k\) and says which side is read through \(\tau\).
  - **Placed at the reserved anchor.** After this entry and W30.1 the paragraph reads: the definition within one organization; the equivalence class; the typing sentence; the two settled sentences; sentence 3 ("Kinds are therefore relative to the contract …"); W30.1's sentences on what a signature is built from. "Therefore" still follows from definitions that are both contract-relative. The typing sentence was added after the cross-examination (s90_xexam_mimo_A1, point 1).
  - **Notation, read in place.** \(E\), \(E'\), \(\tau\), \(\tau'\), \(\lambda\) and "hidden ports" are introduced in Parts IV and V (L191, L233, L235). As drafted, Part II used them before those Parts, with no pointer. Part II already points forward (to Part III, L121 s1), and "Derivation 2 uses kinds in this sense" names where the sentence is used. After the cross-examination (s90_xexam_mimo_A1, point 1), a typing sentence is inserted before the two settled sentences, in Part IV's and Part V's own words and with pointers to them. It types \(E\) and \(E'\) as the organizations of two explanatory candidates, \(t\) and \(t'\) as their transports from \(D\), \(\tau\) and \(\sigma\) as the translations of edits and boundaries, and \(\lambda\) as the assignment to each component of its anchor with a port translation. It restates definitions of Parts IV and V and makes no claim, so KIND and the declaration are unchanged, and the two settled sentences stay byte for byte. The reply's other repair, moving the sentences to Part V after \(t\) is defined, is refused: W20.1 inserts its sentence there, and the move would take the definition across candidates away from (K) and leave Part II without the sense of "one kind" that Derivation 2 uses. The finding carried forward below is closed.
- **CASES AT RISK:**
  - O10 holds AGREE, toward if anything under W30.1. Rosa's two thermostats are compared within one organization by (K); the new sentence compares components of two candidates for one question, which O10 does not raise.
  - O22 and O9 hold: the linkage's lead and the float and dial are compared within one organization.
  - N25 (O75), second question: watched under W19.2, which uses this sentence.
  - No other O- or N-case compares the components of two candidates.
- **GAIN:** Derivation 2's kinds across candidates have a definition, and Derivation 1's comparison is described as what it is.
- **LOSS:** Part II grows by three sentences, and it uses the notation of Parts IV and V before those Parts, typed inline with pointers to them. (After the cross-examination, S90; as drafted, Part II grew by two sentences and used that notation with no pointer.)

### W30.1 — A difference in port values is not a difference of kind

- **STATUS:** applied
- **GROUP:** A
- **ITEM:** W30
- **FILE-11 LINE:** 121
- **WHERE:** Part II, "Kinds are edit-signatures" (L121), two sentences added after sentence 3. Sentences 1–2 are left free for W19's held sentence after (K) (see "Reserved anchors").
- **REASON WORD:** clarification
- **KIND:** CLAIM
- **CHECK:** check 1, FIX. The drafted second sentence ("fixed by the organization D") repeated the SPLIT readers' own conditional on O10, and no case gives D. NEW states the link the O10 ruling rests on (L105): an edit that sets a port replaces only the component that assigns the port, not the relations of the components that read it, and it keeps "whatever the difference is called". Cases: O10 toward AGREE; O22 holds; O9 supported; N25 (O75) toward.
- **OLD:**
````text
and two components of one kind on \(C\) may separate on a finer contract.
````
- **NEW:**
````text
and two components of one kind on \(C\) may separate on a finer contract. A signature is built from a component's relation under each \((a,b)\in C\), not from the values its ports take in a solution; two components that differ only in those values are of one kind on \(C\), whatever the difference is called. An edit that sets a port replaces only the component that assigns the port (above), not the relations of the components that read it, and an edit under which the two relations stay equal does not separate the components.
````
- **DECLARATION:** Part II now states three things. A signature is built from a component's relations and not from the values its ports take, so components that differ only in port values are of one kind whatever the difference is called. An edit that sets a port replaces only the component that assigns it, not the relations of the components that read it. An edit under which both relations stay equal separates nothing.
- **REASON:** W30 (trial §2: two readers got the kind mechanics wrong on one S81 row, one taking a setting edit and one taking the removal of edits to separate two components). (K) gives \(\operatorname{sig}_C(j)=\{(a,b,L_j(a,b))\}\), relations only; L121 s3 already says a coarser contract identifies more. The new sentences say what (K) implies and where the difference lives. "Fixed by the organization \(D\), not by what the difference is called" is used instead of the skeleton's "how the organization is written", so that the clause is not read as a missing input. No case wording is used.
- **CASES AT RISK:** O10: holds AGREE, toward if anything; small risk of SILENT if a reader says the situation does not give the organization (the words "not by what the difference is called" are there to prevent it). O22: holds AGREE (the lead is part of the linkage's relation). No N-case turns on kinds against states (N16, N17 are about level, checked).
- **GAIN / LOSS:** GAIN: The hazard two readers fell into is closed in the text they read. LOSS: Part II grows by two sentences.

### W57.1 + W32(b).1 — L161 s3: what an account on a restricted contract certifies, and a stated ground

- **STATUS:** applied
- **GROUP:** B1
- **ITEM:** W57, W32(b)
- **FILE-11 LINE:** 161
- **WHERE:** Part III, "Scope, and a question that can be wrong", L161 s3. Two sentences are appended after s3.
- **REASON WORD:** clarification
- **KIND:** CLAIM
- **CHECK:** check 1, FIX. "Certifies nothing about the restriction" is false against Part V's non-vacuity (L259), which does certify that a restriction is stated and does not empty the contract. NEW reads "does not certify the restriction as appropriate", which is W32(b)'s point. The second new sentence is kept.
- **OLD:**
````text
What makes a restriction appropriate to the question asked is a substantive, criticizable part of the claim; the semantics records the restriction and supplies no rule that certifies it.
````
- **NEW:**
````text
What makes a restriction appropriate to the question asked is a substantive, criticizable part of the claim; the semantics records the restriction and supplies no rule that certifies it. Meeting the conditions of an account (Part V) on the restricted contract does not certify the restriction as appropriate. Where the claim states the ground of its restriction, a verdict on the restriction is given with that ground; where it states none and a verdict turns on one, the ground is a missing declared input (Part XIV).
````
- **DECLARATION:** Part III now says two things. Meeting the conditions of an account on a restricted contract does not certify the restriction as appropriate. A verdict on a restriction is given with the ground the claim states for it; where no ground is stated and a verdict turns on one, the verdict lacks a declared input.
- **REASON:**
  - **W57** (plan section 0 and 1.2, from 04 §7.10). Four of five file-11 readings of O5 took "supplies no rule that certifies it" to withhold a verdict even where the claim states its own ground. In 06, Atria called this the strongest challenge on O5 and rejected it only on L514's contrast. Test (b) turned on O5 (04 §7.11).
  - **W32(b)** (worklist W32, from verify obs 6 and 03 M17; D3: "scope as a clarification joined with W57"; plan 1.3.7 rank 1). The first new sentence says in words that satisfying (E) on a scoped contract certifies no limit.
  - **The second new sentence** is W57's rule in the plan's words, narrowed twice:
    - "a verdict on the restriction" replaces "the verdict", so the rule does not reach a verdict about the account at the stated scope (s2);
    - "and a verdict turns on one" means that a restriction which only says what is asked is not a missing-input case when no verdict turns on a further ground.
    - Both narrowings guard O8 and N7.
  - **No bare tag.** "Meeting the conditions of an account (Part V)" is written instead of a bare "(E)". Part III comes before (E) is stated, and a bare letter would meet attack (E) of Part XV (skeleton conflict 16).
  - **Left out.** W32(c), the Part VI measure of loose limits, is left out (D3).
- **CASES AT RISK:**
  - **O5 stays AGREE, and the hazard is closed.** Greta's claim states its ground ("the yeast that makes the gas works slowly in the cold"), so the verdict on her narrowing is given with it. Fewer non-AGREE readings are expected (E1).
  - **O1 stays SILENT.** Bruno states limits but no ground for them, and "a retreat" and "no explanation" both turn on one.
    - Risk toward DISAGREE (away): a reader who takes the first new sentence, with s2, to grant Bruno an account at each stated scope.
    - No route toward AGREE: W32(c) is left out.
  - **O8 stays AGREE.** Petra's scope was her question from the start. "An honest scope" and "the limit says what she is asking about" rest on s1–s2 and on non-vacuity, not on a further ground. Risk AGREE→SILENT (away) for a reader who takes "a good explanation" to turn on an unstated ground. The words "a verdict on the restriction" and "and a verdict turns on one" are there for this row.
  - **O33 stays AGREE.** The joint-turn contract is the question asked, so the change does not reach it.
  - **O22 and O34 are unaffected.** Their verdicts concern what the question is, not the ground of a restriction.
  - **N7 (O58), the guard, stays AGREE.** Maya's limits are unexplained and she still explains the rising. The first new sentence keeps the account apart from the limit. Bea's stated ground is given with her verdict, and her verdict is "fuller". Risk AGREE→SILENT (away): a reader who takes Maya's missing ground to leave "does Maya explain" unsettled.
  - **N2 (O54) and N5 (O57) are unaffected.** The patch is a new claim at a new index (s2, unchanged), and the rule has no restriction ground to turn on. N6 is set aside.
- **GAIN:** A claim that states its ground gets its verdict. The text says in words that an account on a restricted contract does not certify the restriction.
- **LOSS:** O1 stays SILENT, and "loose limits" stays unstatable until W32(c).

### W17.1 — L197: surviving on H is defined

- **STATUS:** applied
- **GROUP:** B2
- **ITEM:** W17
- **FILE-11 LINE:** 197
- **WHERE:** Part IV, "Three provenances", **Selected**, L197. Inserted after s2, which is kept byte for byte.
- **REASON WORD:** clarification
- **KIND:** CLAIM
- **CHECK:** check 1, SOUND.
- **OLD:**
````text
The transport \(t\) is a member of \(\mathcal T\) that survived.
````
- **NEW:**
````text
The transport \(t\) is a member of \(\mathcal T\) that survived. A transport **survives on \(H\)** when it is a member of \(\mathcal T\) that meets the survival condition on \(H\); fidelity on \(H\) without membership in \(\mathcal T\) is not survival.
````
- **DECLARATION:** Part IV now defines surviving on H: a transport survives on H when it is a member of the population that meets the survival condition on H, and fidelity on H without membership in the population is not survival.
- **REASON:**
  - Worklist W17 (det 02 §5(i), "My addition"). "Surviving on H" can mean a member of \(\mathcal T\) that survived, which is Sel's own definition here. It can also mean any transport that meets fidelity on H. File 10 leaves both open, and file 11 does not settle them. The note's claim that the proof "already assumed the qualification" holds only on the first reading.
  - Plan 1.2 and D4 take W17 alone from the Derivation 3 family. With this sentence, the claim (L562: "some \(t'\in\mathcal T\), also surviving on \(H\)") and the proof (L564: "that transport survives on \(H\)") use one defined notion. They match by definition, which is the gain D4 names.
  - The clause after the semicolon drops file 10's other reading in the text itself. The worklist says that reading is to be "dropped openly".
  - W16's refuter is not re-widened, and W18's provenance of the population is not added (D4).
- **CASES AT RISK:**
  - O48 stays AGREE, and more securely. The wired arrangement is outside \(\mathcal T\), and fidelity on H without membership is not survival.
  - O24 stays AGREE. Both arrangements are members, both meet the survival condition on every tested setting, and they differ at the reachable joint setting.
  - D3-T (O76, if adopted): AGREE is secured. The discarded design is a member that failed the survival condition, so it does not survive on H and witnesses nothing. That is its fixed verdict ("not another survivor of this testing history"). If file 11's ruled mark there is not AGREE, the row is a change toward.
  - O11 is not reached. Monday's fitting raises no question of a differing survivor.
  - N5 (O57), N9 (O60) and N18 (O68) are not reached by this entry. For N5, see W17.2. In N9 the question is whether the correspondence is knowledge. In N18, Dov's copied bridge raises no comparison of survivors.
  - Derivation 10's "no member survives the extended history" (L616) reads as before.
  - I checked for any other row, and none turns on who counts as a survivor.
- **GAIN:** Derivation 3's claim and proof use one defined notion of survival, and O48's verdict rests on a definition.
- **LOSS:** File 10's other reading is withdrawn openly: an unconditional theorem about any alternative faithful on H, whatever the population.

### W35.1 — Part IV: expectation and violation for every transport; surprise kept for selected ones

- **STATUS:** applied
- **GROUP:** C
- **ITEM:** W35 (b′)
- **FILE-11 LINE:** 219–223
- **WHERE:** Part IV, "Expectation, surprise, violation", L219 s1 and the third bullet at L223. The OLD block runs from L219 to L223; L221 and L222 are carried unchanged.
- **REASON WORD:** clarification
- **KIND:** CLAIM
- **CHECK:** check 2, SOUND. Widening violation leaves L227's selection response speaking of an H that a constructed transport lacks; the companion entry W35.4 fixes that. The diff shows two hunks for this one entry (L219 and L223).
  - S90 cross-examination: s90_xexam_mimo_C, point 1 (R12 FALLS) — FIX, after the cross-examination. S90, Mimo part C, R12 FALLS (Atria part C makes the same typing point but rules R12 STANDS and R13 FALLS); fresh checker FIX after the cross-examination. The preamble reads 'a transport to the simulation layer \(S\), with contract \(C\)', since \(\operatorname{Ans}_S(\tau(a),\sigma(b))\) is typed only when \(t\)'s target is \(S\). The declaration reads 'for every transport to the simulation layer, whatever its provenance'. The \(\operatorname{Ans}_E\) alternative is not adopted: a general \(E\) supplies no query, and L177 keeps expectation at \(S\).
- **OLD:**
````text
Let \(t\) be selected on history \(H\) with contract \(C\). For an edit–boundary pair \((a,b)\in C\) actually occurring:

- the **expectation** is \(\operatorname{Ans}_S(\tau(a),\sigma(b))\);
- a **violation** occurs when fidelity fails at \((a,b)\);
- **surprise** is a violation at \((a,b)\notin H\).
````
- **NEW:**
````text
Let \(t\) be a transport to the simulation layer \(S\), with contract \(C\) and, where \(t\) is selected, history \(H\). For an edit–boundary pair \((a,b)\in C\) actually occurring:

- the **expectation** is \(\operatorname{Ans}_S(\tau(a),\sigma(b))\);
- a **violation** occurs when fidelity fails at \((a,b)\);
- **surprise** is a violation of a selected transport at \((a,b)\notin H\).
````
- **DECLARATION:** Part IV now defines expectation and violation for every transport to the simulation layer, whatever its provenance, and keeps surprise for a violation of a selected one at a pair outside its history.
- **REASON:** Worklist W35, variant (b′) (D3; plan 1.2; source point 13, verify obs 13, PARTLY CONFIRMED; M2). In file 11 the section opens "Let t be selected on history H". Expectation and violation therefore exist only for selected transports, and a constructed theory that fails has no violation to report. Under (b′), expectation and violation are defined for every transport, surprise is kept for a selected one, and H is introduced only where t is selected. Derivations 4 and 10 are unchanged and stay true word for word. Derivation 4 reads "A system can be surprised only if it holds a transport selected on a history H …" and its proof reads "Surprise is defined as a violation at (a,b)∉H". In Derivation 10, t_0 is selected on H_0. File 12's tested-history surprise (12:215–225, variant (c)) is not adopted (D3). The expectation keeps \(\operatorname{Ans}_S\): S is the organization the transport serves in this section, and constructed transports sit there too (L203). The OLD block runs over five lines so that the widened opening and the narrowed third bullet form one change: applied alone, either half would leave surprise ill-typed.
- **CASES AT RISK:**
  - O3 holds AGREE. Nadia predicts with a transport selected on the cards played, so her "often surprised" is still surprise in the technical sense. The verdict turns on construction (L401), not on surprise.
  - N18: toward on Q2 ("the swaying went against what both expected"). Rhea's constructed transport now has an expectation and a violation.
  - O-cases that mention expectation or surprise were searched; O3 is the only one. O5, O11, O24 and O48 are untouched: no expectation is at issue in them. Derivation 10's worked episode is unchanged.
- **GAIN:** A constructed theory that fails is violated in the text's own terms.
- **LOSS:** "Surprise" stays narrower than ordinary use. After the cross-examination (S90), the drafted, unscoped "for every transport" goes; it was false for expectation.

### W35.2 — Part IV: a constructed transport is violated, not surprised

- **STATUS:** applied
- **GROUP:** C
- **ITEM:** W35 (b′)
- **FILE-11 LINE:** 225
- **WHERE:** Part IV, "Expectation, surprise, violation" (L225). One sentence is added after s4; s1–s4 are unchanged.
- **REASON WORD:** clarification
- **KIND:** CLAIM
- **CHECK:** check 2, FIX. File 11 says a system is surprised and a transport is violated, never surprised; NEW reads "is violated, and the failure is not surprise". N18 Q3's Dov half stays watched (his transport need not be read as selected). Companion entry W35.4 added.
  - S90 cross-examination: s90_xexam_mimo_C, point 4 (R13 STANDS, naming an undeclared clause); s90_xexam_atria_C, point 1 (R13 FALLS) — FIX (two rulings, reconciled to one text), after the cross-examination. S90, Mimo part C point 4 (closing line R13 STANDS, but it names an undeclared clause) and Atria part C point 1 (R13 FALLS); fresh checker FIX after the cross-examination. The opening clause reads 'for every transport to the simulation layer', since \(\operatorname{Ans}_S(\tau(a),\sigma(b))\) is typed only when \(t\)'s target is \(S\); its instance reads 'a constructed one', parallel to 'a selected one', so that 'violated' stays inside that scope. The declaration now includes the restated clause, which the REASON names as the sentence's purpose. Follows the R12 (W35.1) fix. Atria C (item 1) ruled FIX to the same effect with 'into the simulation layer' and 'a constructed transport'; the batch-3 reading takes this wording, which R12's fix shares.
- **OLD:**
````text
Whether the correspondence could have been otherwise at such a change is a fact about its population (Derivation 3).
````
- **NEW:**
````text
Whether the correspondence could have been otherwise at such a change is a fact about its population (Derivation 3). Expectation and violation are defined for every transport to the simulation layer, surprise only for a selected one: a constructed one that fails at a pair of its contract is violated, and the failure is not surprise; a violation the system represents can be a recognized difficulty (Part X).
````
- **DECLARATION:** Part IV now says, restating its definitions, that expectation and violation are defined for every transport to the simulation layer and surprise only for a selected one; that a constructed transport to the simulation layer that fails at a pair of its contract is violated, and the failure is not surprise; and that a violation the system represents can be a recognized difficulty.
- **REASON:** Worklist W35 (b′). Plan 1.2 asks for surprise to be kept for selected transports "and said so". This sentence says it. It also joins a represented violation to Part X's recognized difficulty (W35.3). That is how the refutation of a constructed theory gets a place in the semantics without being called surprise (source point 13: "the refutation of a constructed theory is not surprise"). The sentence says "can be" because a violation is a recognized difficulty only when fidelity at that pair is a claimed obligation and the system represents its failure (W35.3). After the cross-examination (S90, Atria C point 1; Mimo C point 4): The expectation \(\operatorname{Ans}_S(\tau(a),\sigma(b))\) is well typed only for a transport whose target is the simulation layer, as (A) at L250 shows. Part IV also has transports into the primitive layer (L201) and carrier-to-content transports under (R). So "every transport" said more than the formula defines. The sentence is narrowed to the scope that W35.1's REASON and L177 already give. No case moves: N18 holds as CHECK states it, and O23, O3 and D3-T are not reached.
- **CASES AT RISK:**
  - N18: toward on Q3. Rhea's bridge fails at a pair her contract covers, so her grounds are contradicted: a constructed transport is violated. Dov's copy, read as selected on the village bridge's record, meets a change outside that record. That is surprise, and nothing Dov had grounds for is contradicted. The Dov half depends on reading his transport as selected, and is watched.
  - O3 holds. No other O-case turns on a constructed transport's failure; O13 and O23 were checked.
- **GAIN:** The text says what the narrow sense of surprise leaves out, and where that goes.
- **LOSS:** None beyond W35.1's. After the cross-examination (S90), a constructed transport with another target (a Part V candidate's, or (R)'s carrier-to-content transport) is not called violated by this section; it was not in file 11 either, where the section covered only selected transports.

### W35.4 — Part IV: the selection response extends a selected transport's history

- **STATUS:** applied
- **GROUP:** C
- **ITEM:** W35 (b′), companion entry
- **FILE-11 LINE:** 227
- **WHERE:** Part IV, "Expectation, surprise, violation", L227 s2 (new companion entry, group C's paragraph).
- **REASON WORD:** clarification
- **KIND:** WORDING
- **CHECK:** check 2, new companion entry, proposed with the W35.2 fix. WORDING against file 11, where every t of this section is selected.
- **OLD:**
````text
A **selection response** extends \(H\) and lets \(\mu\) act:
````
- **NEW:**
````text
A **selection response** extends the history \(H\) of a selected transport and lets \(\mu\) act:
````
- **DECLARATION:** none (WORDING against file 11; listed in the record). If a checker rules CLAIM: "Part IV now says that a selection response extends the history of a selected transport."
- **REASON:** Check 2's companion to its W35.2 fix. After W35.1, violation is defined for every transport, and a constructed transport has no history H and no μ. L227's selection response is typed to a selected transport, so that its H has a referent. In file 11 every t of the section is selected, so against file 11 the change is one of wording.
- **CASES AT RISK:** None moves. O3 (a selection response against a construction response) holds; N18 is not reached (Rhea's response is construction).
- **GAIN:** L227 stays well typed after W35.1.
- **LOSS:** None.

### W20.1 — Γ typed: the components the candidate offers as doing the work; the rest is named background

- **STATUS:** applied
- **GROUP:** A
- **ITEM:** W20
- **FILE-11 LINE:** 233
- **WHERE:** Part V, the opening paragraph (L233). One sentence is inserted after sentence 1, which ends "… and an identified set \(\Gamma\) of active commitments in \(E\)."; sentence 1 is kept byte for byte, and "The pair \(\mathcal E=(E,p,t,\Gamma)\) satisfies …" follows unchanged.
- **REASON WORD:** clarification
- **KIND:** CLAIM
- **CHECK:** not put to check 1 or check 2, which ran before S88 was settled. The text is the settled wording (F3, block 2), copied byte for byte. Checked by its drafter as W19.1 was. No outside reader has seen this wording; X1 must carry it.
  - S90 cross-examination: s90_xexam_mimo_A1, point 2 (R15 STANDS, naming a move away on O45 on one reading) — FIX, after the cross-examination. Settled wording (F3, block 2) with one clause added after the cross-examination (S90, Mimo A1, point 2): 'whether or not anyone has described their work', from L309 s3; the reply's 'identifies as active' is not taken ('active' is undefined). The declaration follows the new clause. O45 moves from "watched, with a risk away" to "holds AGREE, on firmer text". Atria (s90_xexam_atria_A1, pass 2, point 5) read O45's second spring as a route "whether or not anyone described its work" and gave STANDS, which agrees.
- **OLD:**
````text
and an identified set \(\Gamma\) of active commitments in \(E\).
````
- **NEW:**
````text
and an identified set \(\Gamma\) of active commitments in \(E\). The commitments \(\Gamma\) are components of \(E\), those the candidate offers as doing the work, whether or not anyone has described their work; the boundary values of \(E\) and the components of \(E\) outside \(\Gamma\), including any that assigns an input, belong to the named background of Part VI.
````
- **DECLARATION:** Part V now types a candidate's commitments: they are components of its organization, those the candidate offers as doing the work, whether or not anyone has described their work, and the organization's boundary values and its other components, including any that assigns an input, belong to the named background of Part VI.
- **REASON:**
  - **W20** (S88 finding F3, settled NARROWED from the finding as sent). The narrowed finding stands, with the F3 reading's precision: Γ is untyped, and the operative gap is membership, whether a component that assigns an input is a commitment or named background. No sentence of file 11 types Γ. L233, L257 and L289 are the only relevant sentences, and "the named background" occurs only at L289.
  - **Plan 1.3.4's rule**, fixed before any S88 reply was read: "F3 UPHELD: take B, with the rider unless X1 finds that the rider breaks a worked case". Settling applied its first branch. The narrowing (O33) is against the finding's instances, not against option B, and B holds on O33, O5, O7, Part VII's production case and the skew-symmetric case. The rule has no branch for a narrowing that leaves B intact.
  - **The wording** is the settled change 3.
    - The sentence in view after Atria's reading ("the boundary values of \(E\) belong to the named background") put a component that lies outside Γ and is not a boundary value in no class, so its fate under restriction was undefined.
    - "Including any that assigns an input" is Mimo's point 7. "Those the candidate offers as doing the work" is the rider's sentence in plan 1.3.4.
    - Not adopted from Mimo: "active", which is undefined; and "every verdict is relative to it", since L233 already makes Γ a coordinate of \(\mathcal E=(E,p,t,\Gamma)\).
  - **It agrees with the rider** (skeleton conflict 4). Deleting \(G\) from \(E\) leaves \(\Gamma\setminus G\) and everything this sentence puts in the named background, which is \(E|(\Gamma\setminus G)\) whenever Part VI's operation is deletion.
  - **What it settles.** The candidate's identification decides membership. Option B (W20.2) makes the named verdicts insensitive to that choice: in the F3 reading's models 1a and 1b, production holds whether or not the input-assigning components are listed.
  - **Read in place.**
    - The sentence sits between the definition of a candidate and "The pair \(\mathcal E\) … satisfies \(\operatorname{Account}(\mathcal E)\) exactly when", and it points forward to Part VI, where the named background is used (L289).
    - "Including any that assigns an input" has two readings: every component that assigns an input is outside Γ; or any such component the candidate leaves out of Γ is named background. The named verdicts are the same on both (models 1a and 1b). Carried forward below.
    - "Active" (L233's "active commitments", L235's "every active component") is still undefined. Carried forward below.
  - **After the cross-examination (S90, Mimo A1, point 2).** The record of the fix: settled wording (F3, block 2) with one clause added after the cross-examination (S90, Mimo A1, point 2): 'whether or not anyone has described their work', from L309 s3; the reply's 'identifies as active' is not taken ('active' is undefined). Read in place, "those the candidate offers as doing the work" admitted a reading on which a component whose work nobody has described is not a commitment, and the rescue lay only in Part VI text whose subject presupposes membership; the definition now carries the answer itself.
- **CASES AT RISK:**
  - **O45: holds AGREE, on firmer text (W20.1 now states that membership does not wait on a description; L309 s3, W28.1 and W58(i).1 agree).** So after the cross-examination (S90, Mimo A1, point 2). As drafted it was watched, with a risk away: "Those the candidate offers as doing the work" meets the case's "The second is never described as doing anything".
    - A reader who takes "offers as doing the work" to need a description of the work puts the second spring in the named background. It is then no route, and "It was already a route" moves AGREE→SPLIT.
    - The account contains the second spring, connected and sufficient, and that is offering it as part of the mechanism. L309 s3 ("a route whether or not anyone has described its work"), W28.1 and W58(i).1 ("whether or not anyone has set them out") hold the AGREE.
    - X1 should test this row.
  - **O7 holds AGREE, on firmer text.** The component that spreads or sweeps the salt assigns an input and is named background, and the salt's action on the ice is the commitment. File 11's S3, on the mechanism-only reading, had no edit in the salt contract that removes a commitment; under W20.2, deleting the salt's action loses the contrast.
  - **O5** holds AGREE (W20.2).
  - **Part VII's production case** holds. \(H:=U_H\) and \(\theta:=U_\theta\) assign inputs and are named background, and the law is Γ. It holds under W20.2 on both identifications (models 1a and 1b).
  - **The skew-symmetric case** holds. "Field arithmetic and determinant–invertibility held fixed" are components outside Γ, so named background, as L341 treats them.
  - **O2 holds AGREE.** Carla offers both parts, so both are in Γ. The almanac is the answer written as a component, and the verdict rests on S2 and L275's rule (W9.1).
  - **N1 (O53): watched both ways, as W33.1 records** (skeleton conflict 11, rechecked).
    - Tomas offers the sun-god sentence as keeping the tilt steady, so under this sentence it is a commitment wherever it is a component. The membership question that W33.1 left to W20 is settled, and the watch moves to fidelity.
    - Read as a redescription of the spinning-body component, or as constraining nothing, it does no work, and the verdict holds (toward).
    - Read as a second faithful component, it is a redundant route, and "not part of what explains" is at risk (away).
    - Read as an unfaithful component, it is interference, and "Tomas explains" is at risk.
  - **O36, O46 and O47** hold. Part VI's supports are subsets of the written Γ (W58(i).1), and the typing moves none of them.
- **GAIN:** Γ has a type and a rule of membership, and every component of \(E\) has a class, so restriction is defined on all of \(E\).
- **LOSS:** Membership is the candidate's identification, not a test. A candidate that leaves out of Γ a component that does the work has it fixed as background, and non-circular dependence then has only the listed commitments to witness it.

### W39.1 — Identity of the answer is structural at the declared grain

- **STATUS:** applied
- **GROUP:** A
- **ITEM:** W39
- **FILE-11 LINE:** 257
- **WHERE:** Part V, "Non-circular dependence" (L257), a new sentence after S2; S3 is left for W20 (held).
- **REASON WORD:** clarification
- **KIND:** CLAIM
- **CHECK:** check 1, FIX. Restored after file 11's S2, "Identity of that assertion" no longer said what the assertion is identical with. NEW adds "with the target's answer", which restores file 00's sense and matches the declaration. Cases: as drafted, plus N16 (O66) toward.
- **OLD:**
````text
moving an assertion from an input slot into a component named "law" does not discharge this.
````
- **NEW:**
````text
moving an assertion from an input slot into a component named "law" does not discharge this. Identity of that assertion with the target's answer is structural at the declared grain, not the indiscriminate identification of all logically equivalent mathematical truths.
````
- **DECLARATION:** Non-circular dependence now states that identity of an assertion with the target's answer is structural at the declared grain, not the identification of all logically equivalent mathematical truths.
- **REASON:** W39 (source point 12; verify obs 12). 00:210's sentence, restored word for word. Files 10 and 11 kept "at the declared grain" and dropped the sentence that says what identity at the grain is. Its second half protects the Part VII odd-order skew-symmetric construction, whose premises are logically equivalent to its conclusion. 00:210's counterfactual-law sentence is not restored (plan conflict 14).
- **CASES AT RISK:** O2: holds AGREE, toward (the almanac entry is the answer, structurally, at the grain). O4: weak, either direction (a reader may now deny that the index is structurally the answer); its AGREE rests on L129 and L153. N25 and N3: toward (the same assertion restated one level down, and the yearly return written into the bargain). N2: toward (the southern seasons are the report written into the myth). N8: weak risk away (a reader may call the energy law a restatement of the answer); expected to hold, since the law constrains every design and the answer is one consequence of it.
- **GAIN / LOSS:** GAIN: Same-form restatement is caught in words, and mathematical accounts are protected in words. LOSS: Nothing; the sentence was in file 00.

### W20.2 — Non-circular dependence, S3: option B with the deletion rider

- **STATUS:** applied
- **GROUP:** A
- **ITEM:** W20
- **FILE-11 LINE:** 257
- **WHERE:** Part V, "Non-circular dependence" (L257), sentence 3 (S3), the whole sentence. S1 and S2 are unchanged. W39.1's sentence lands after S2 and before this one; the two OLD texts do not overlap (skeleton conflict 2).
- **REASON WORD:** change of claim
- **KIND:** CLAIM
- **CHECK:** not put to check 1 or check 2. The text is the settled wording (F3, block 1), copied byte for byte. Checked by its drafter as W19.1 was.
  - The deletion rider was never put to either outside reply. With W19.3 it is the least tested wording in this list, and X1 must test it (plan 1.3.4).
  - The fallback, if X1 finds that the rider breaks a worked case, is settled with it: S3 reads "… and this contrast is lost in \(E|(\Gamma\setminus G)\) with the named background fixed: evaluated at \((\tau(a),\sigma(b))\) and at \((1,\sigma(b_0))\), its two answers are determined and equal, or an answer that \(E\) determines at one of these points is not determined at that point."; L516's declared indices gain "the restriction operation of Part VI"; and W20.3's clause ends "…, and \((E|W)|W'=E|W'\) for \(W'\subseteq W\)". If both options break something, only the \(\tau,\sigma\) erratum is taken.
  - S90 cross-examination: s90_xexam_atria_A1, pass 2, point 2 (R17 STANDS, naming a move toward on O33) — KEEP, after the cross-examination. After the cross-examination (S90, part A1): Atria's reply (pass 2, attempt 5) gave STANDS and named a move on O33, toward and declared; kept. O33's ruled mark rests on L151 and L189 ("faithful"), which S3 does not touch, and its table is the question's form, not a candidate (the O33 flip was withdrawn in S88). The move the reply names is the entry's GAIN, that accounts of input-only contracts can now witness. The reply's "'p because p' fails through S2" agrees with S88. Its point 3 (L339 names no block) is a notation point, passed on. Mimo's reply gave STANDS and did not contest the change.
- **OLD:**
````text
There exists \((a,b)\in C\) that removes or replaces a nonempty block of \(\Gamma\) while preserving the other boundary conditions, under which the answer profile changes or ceases to be determined in the claimed way.
````
- **NEW:**
````text
There exist \((a,b)\in C\) and a nonempty block \(G\subseteq\Gamma\) such that the answer profile at \((a,b)\) differs from its value at \((1,b_0)\), or is not determined there in the claimed way, and this contrast is lost when the components of \(G\) are deleted from \(E\) (a deleted component imposes the full relation on its ports, Part II): evaluated at \((\tau(a),\sigma(b))\) and at \((1,\sigma(b_0))\), the answers of \(E\) with \(G\) deleted are determined and equal, or an answer that \(E\) determines at one of these points is not determined there once \(G\) is deleted.
````
- **DECLARATION:** Non-circular dependence now requires a pair of the contract and a nonempty block of the commitments such that the answer profile at the pair differs from its value at the baseline, or is not determined there in the claimed way, and this contrast is lost when the block's components are deleted from the organization: at the translated pair and the translated baseline, the answers of the organization with the block deleted are determined and equal, or an answer it determined there is no longer determined. It no longer asks for a pair of the contract that itself removes or replaces a block of the commitments.
- **REASON:**
  - **W20** (S88 finding F3; the settled status and the plan's rule are under W20.1).
  - **The defect.** File 11's S3 asks for a pair of \(C\) "that removes or replaces a nonempty block of \(\Gamma\) while preserving the other boundary conditions". With Γ untyped, a pair that only sets inputs witnesses it on one identification and not on another.
    - Part VII's production account fails S3 on its production contract of interventions on \(H\) and \(\theta\) when Γ is the law alone (the F3 reading's model 1a).
    - O5 flips on a narrowed contract with no edit that removes a mechanism commitment (model 8a).
  - **What option B does.** It puts the dependence in a restriction, not in the reach of an edit.
    - The witnessing contrast stays in \(C\), so non-vacuity's last sentence (L259) stays true.
    - An idle block can never witness, which agrees with L275's rule (W9.1) and with W33.1.
    - A composite edit lets an idle block witness file 11's S3 and option A (model 4). It cannot witness B.
  - **Settled change 1: the explicit test for "lost".** The wording in view after Atria's reading, "that difference is lost or the answer ceases to be determined", has no antecedent when the first conjunct holds by non-determination. On the loose reading, an idle Γ passes (model 3, a contract with a law-deleting edit). The explicit test gives no witness there. Mimo's own wording leaks on the same model and is not adopted (prompted by Mimo's point 5(ii)).
  - **Settled change 2: the deletion rider** (plan 1.3.4, fixed before any S88 reply was read).
    - The restriction is deletion under (O), which the text already has (L105). So Account takes no new declared input.
    - This answers Mimo's point 5(i), that Account would depend on Part VI's declared restriction operation. It does so without the F3 reading's change 3, which would have named that operation among the declared indices.
    - The F3 reading's models implement restriction as deletion (`f3_check.py`, function `restrict`), so their "proposed" column is the rider's test: production on both identifications, O33 on the mechanism-only reading, O5 on both formalizations, and no witness for relabelings or an idle block.
  - **The dependence order (L518) is not changed.** (E) now uses (O)'s deletion rule, and L518 already has "(F1), (F2), (A) depend on (O), (Q), (K). (E) depends on those." The two sentences B1 left free stay free (skeleton conflict 3).
  - **Read in place.**
    - "The answer profile" is the one file 11's S3 names. \((\tau(a),\sigma(b))\) and \((1,\sigma(b_0))\) are Part V's translations, with \(\tau(1)=1\) from (F2). The parenthesis restates L105's first sentence and points to Part II.
    - L341 still reads true: "Non-circular dependence is witnessed by \(I_3\) under removal of skewness …". The pair "remove skewness" with \(G\) the skewness commitment is a witness, since with skewness deleted the family contains an invertible matrix at both points (the F3 reading's determinant check).
    - L259's "excluding every change under which the active commitments could matter" still names what a contract must not do: under B the commitments matter through a contrast in \(C\).
  - **Classification:** a change of claim. The logical form of a defining clause changes.
- **CASES AT RISK:**
  - **O5 holds AGREE, on firmer text** (models 8a and 8b).
  - **O7 holds AGREE, toward.** Deleting the salt's action loses the melting contrast (see W20.1).
  - **O33 holds AGREE.** "The table is faithful" is a verdict of fidelity, which S3 does not touch; model 6a holds under B.
  - **O2 holds AGREE**, on S2 and L275. Deleting the bell loses no contrast in the tide question, so the bell cannot carry it.
  - **O4 holds AGREE.** The index is the answer observed (S2, L129, L153), and B does not reach it.
  - **O36, O45, O46 and O47** hold. (S) and (B) are unchanged, and each support's S3 now quantifies over its own commitments (W20.3). O45's two springs witness together: deleting both loses the door's return.
  - **N25 (O75): the first question holds.** No admitted change alters the answer, so the first conjunct fails and no block witnesses.
  - **N3 (O55) holds, toward on its first question with W39.1.** The yearly return is written into the bargain (S2).
  - **N23 (O73): toward on its first half.**
    - The forward account's commitments are the laws of motion. The positions a thousand years ago are set by components that assign inputs, which W20.1 puts in the named background.
    - Deleting the laws loses the contrast, so the forward account meets S3. File 11's S3, on the mechanism-only reading, had no witness for it.
    - The backward account still fails. It fails (F2), as L323's reversed calculation does, under a contract of interventions on the earlier positions. It fails S3 under a contract of interventions on tonight's positions, which leave the target's past as it was.
  - **N1 (O53):** as W20.1. Deleting the sun-god component alone loses no contrast while the spinning-body point remains, so it never witnesses alone.
  - **Part VII's production case and the skew-symmetric case** hold (above).
- **GAIN:** The condition is well typed. O5, O7, O33 and Part VII's production case are secured on the text. An idle block cannot witness. Account takes no new declared input.
- **LOSS:** The logical form of a defining clause changes: dependence is shown by deleting commitments, not by an admitted edit that reaches them. The test has not been put to an outside reader.

### W11.1 — L271 s2: the encoding table is an account only when it meets the rest of (E)

- **STATUS:** applied
- **GROUP:** B1
- **ITEM:** W11
- **FILE-11 LINE:** 271
- **WHERE:** Part V, "What (E) excludes, and what it does not", L271 s2.
- **REASON WORD:** clarification
- **KIND:** CLAIM
- **CHECK:** check 1, SOUND.
- **OLD:**
````text
A table that genuinely encodes an organization's response to every admitted change is not a table in that sense: it satisfies (F1) as a decomposition does, and it is an account.
````
- **NEW:**
````text
A table that genuinely encodes an organization's response to every admitted change is not a table in that sense: it satisfies (F1) as a decomposition does, and it is an account when it meets the other conjuncts of (E).
````
- **DECLARATION:** Part V no longer says outright that a table encoding an organization's response to every admitted change is an account: it satisfies (F1), and it is an account when it meets the other conjuncts of (E).
- **REASON:**
  - Worklist W11 (det 02 C38 and C70; 03 M22). L271 grants Account on (F1) alone, without (F2), (A), non-circular dependence or non-vacuity. S2 of non-circular dependence (L257) forbids the answer appearing "as a component", and L275 forbids restating the answer. An encoding table can do either.
  - **Departure from the skeleton's wording.** The skeleton and plan give "is not excluded by (F1), and is an account when it meets the other conditions of (E)". NEW keeps file 11's "it satisfies (F1) as a decomposition does", because W11 faults the account clause and not the (F1) clause. This is the smaller change. If the orchestrator prefers the plan's text, replace "it satisfies (F1) as a decomposition does" in NEW with "it is not excluded by (F1)". No other entry depends on the choice.
  - "Conjuncts" follows (E)'s own form and L267 ("Every conjunct is a condition …"). (F1) is one conjunct, while "the four conditions" of L233 count (F1) and (F2) as one condition.
  - S70's deference of the front matter to Part V is kept: Part 0 says nothing about tables.
- **CASES AT RISK:**
  - O2 stays AGREE, and more securely. The entry removes a reading in which the almanac, taken as an encoding table, is an account by L271 alone.
  - O33 stays AGREE. "The table is faithful" is a claim of fidelity, which "satisfies (F1)" keeps.
  - O7 stays AGREE. It is not a table.
  - O4 stays AGREE. It is a measure, not a table.
  - N17 (O67) is watched. Answer A is a full derivation. A reader who takes it as an encoding of every admitted change now finds it an account only when it meets the other conjuncts. Its point may change without its direction changing, and the plan predicts no mark for O67.
  - N16 (O66) is not reached, because its Answer A is a summary.
- **GAIN:** No Account is granted without checking the other conditions, and L271 no longer clashes with L257 S2 and L275.
- **LOSS:** File 11's crisp closure of the lookup-table question is lost.

### W9.1 — Drop the "bell and tide" parenthesis and keep the rule

- **STATUS:** applied
- **GROUP:** A
- **ITEM:** W9
- **FILE-11 LINE:** 275
- **WHERE:** Part V, "What (E) excludes, and what it does not" (L275), end of sentence 2.
- **REASON WORD:** erratum
- **KIND:** WORDING
- **CHECK:** check 1, SOUND.
- **OLD:**
````text
does not repair this (the bell does not explain the tide).
````
- **NEW:**
````text
does not repair this.
````
- **DECLARATION:** none (WORDING; listed in the record). If a checker rules CLAIM (on the view that file 11 stated an instance that revision 2 leaves to the rule): "Part V's rule on a restated answer packaged beside a genuine dependence no longer names an instance."
- **REASON:** W9 (XR4; det 02 C40). The parenthesis names content with no referent in the document (the example is a case's content) and reached the file-11 testers inside the theory text. 03 §5 ruled XR4 a SLIP: "The rule in the sentence stands without the parenthesis, so this is not claim-changing." The rule (C40) is kept word for word; it holds under every W20 option (plan 1.3.4; conflict 2).
- **CASES AT RISK:** O2: may move away (AGREE → SPLIT) if a reader leaned on the parenthesis, which stated the verdict's own point; expected to hold AGREE on the rule itself and on S2 of non-circular dependence. No N-case turns on it (N1's idle sentence is the converse case and is read on other text).
- **GAIN / LOSS:** GAIN: No case content inside the theory; O2 is read on the rule, not steered. LOSS: A vivid example.

### W20.3 — Part VI: the commitments of \(E|W\) are \(W\)

- **STATUS:** applied
- **GROUP:** A
- **ITEM:** W20
- **FILE-11 LINE:** 289
- **WHERE:** Part VI, the opening paragraph (L289), sentence 2. A clause is appended after its last word. Sentence 1 ("Fix \(\mathcal E\) and a declared restriction operation.") and "Define" are unchanged. No other entry touches L289.
- **REASON WORD:** clarification
- **KIND:** CLAIM
- **CHECK:** not put to check 1 or check 2. The text is the settled wording (F3, block 3), copied byte for byte. Checked by its drafter as W19.1 was.
- **OLD:**
````text
For \(W\subseteq\Gamma\), let \(E|W\) retain the commitments in \(W\) with the named background fixed.
````
- **NEW:**
````text
For \(W\subseteq\Gamma\), let \(E|W\) retain the commitments in \(W\) with the named background fixed; the commitments of \(E|W\) are \(W\).
````
- **DECLARATION:** Part VI now says that the commitments of a restricted candidate E|W are W.
- **REASON:**
  - **W20, settled change 4.** (S) applies Account to \(E|W\), and non-circular dependence, under either option, quantifies over blocks of that candidate's Γ. L289's "retain the commitments in \(W\)" suggests that the commitments of \(E|W\) are \(W\) but does not state it. The gap predates option B (the F3 reading).
  - **Only part of the F3 reading's change 3 is kept.** That change also named the restriction operation among the declared indices and stated that restriction composes. Under the rider, (E) does not use Part VI's operation (W20.2), so neither is needed. Both return in the fallback (W20.2's CHECK).
  - Prompted by Mimo's point 5(i), on composition, kept in narrowed form.
  - **KIND.** The clause states for the first time what the old words suggest, which is CLAIM under the record's definition. A checker may rule it WORDING; the declaration then leaves the note, and N falls by one.
- **CASES AT RISK:**
  - **O36 holds AGREE.** P is critical in each route as written. Each route's \(E|W\) now has \(W\) as its commitments, so its S3 quantifies over \(W\).
  - **O45 holds AGREE.** \(E|\{\text{second spring}\}\) has the second spring as its commitment, and deleting it loses the door's return. So the singleton is a support, and the spring is a route.
  - **O46 and O47 hold.** The cable belongs to a new candidate (L309 s3), and the interference case is unchanged.
  - **N1:** as W20.1.
  - **W33.1** reads each support with its own commitments ("every support stays a support after \(d\) is added to it and after \(d\) is removed from it"), as this clause says.
- **GAIN:** Part VI's supports are well typed under non-circular dependence.
- **LOSS:** None.

### W58(i).1 — Part VI: the supports assessed are the subsets of the written Γ

- **STATUS:** applied
- **GROUP:** C
- **ITEM:** W58(i)
- **FILE-11 LINE:** 301
- **WHERE:** Part VI, the paragraph after (B) (L301), s2, last clause.
- **REASON WORD:** clarification
- **KIND:** CLAIM
- **CHECK:** check 2, SOUND. O36 is watched, not held on firmer text: a reader who takes the rewritten route's premise to be one Γ already carries would have it assessed.
  - S90 cross-examination: s90_xexam_atria_C, point 3 (R21 STANDS, naming a move toward on O45) — KEEP, after the cross-examination. Cross-examination of revision 2 (S90 part C): Atria gave STANDS and named, under (d), a declared move toward the fixed verdict on O45: 'whether or not anyone has set them out' has the second spring's support assessed from the start, in line with (S). Mimo gave STANDS with no point. Ruled KEEP after the cross-examination. The move is toward and follows from the declaration's own clause. On the S81 reading file 11 was already AGREE on O45 through L309 s3, so the mark holds on firmer text; only old L301's narrow reading ('only the supports someone has set out') pulled against it, and the reply's 'contradicted (S) and the verdict' overstates that ambiguity. N1 holds. O36 holds AGREE on the case's natural reading (the replacement premise is outside Γ, which NEW's last clause excludes), and stays watched as check 2 says: on the other reading, (S) already assessed the rewritten route in file 11, and P stays critical in each route as written. O46 and O47 hold.
- **OLD:**
````text
and the supports assessed are the ones actually written, not a support someone could write in their place.
````
- **NEW:**
````text
and the supports assessed are subsets of the written \(\Gamma\), whether or not anyone has set them out, not a support someone could write with commitments outside \(\Gamma\).
````
- **DECLARATION:** Part VI now says that the supports assessed are the subsets of the written commitments, whether or not anyone has set them out, and not supports that need commitments outside them.
- **REASON:** Worklist W58(i), from 03 §8 item 10 ("'the supports actually written' at L301 has two readings, one of which narrows (S)"; M26; 02 C43). (S) at L292 ranges over every W ⊆ Γ. "The ones actually written" can also be read as "only the supports someone has set out", which would narrow (S). NEW keeps the intended reading and closes the other one. The intended reading is 01's at O36: "(S) and (B) … range only over subsets of the written Γ". "With commitments outside Γ" says what "a support someone could write in their place" is: one that needs a commitment the candidate does not carry. Such a support belongs to another candidate, as L309 s3 says of a reassigned component. KIND: it closes a reading that narrows (S). The plan offered "WORDING or CLAIM"; ruled strictly, it is CLAIM.
- **CASES AT RISK:**
  - O36 holds AGREE, on firmer text. P is critical in each written route, and the rewritten route needs a premise outside Γ.
  - O45 holds, or moves toward. "Whether or not anyone has set them out" says that a support nobody described is still assessed, as L309 s3 says of a route.
  - O46 holds: the cable is a commitment outside Γ, and so belongs to another candidate (L309 s3). O47 holds.
  - No N-case turns on which supports are assessed. N1's support without the sun-god sentence is a subset of the written Γ on either reading.
- **GAIN:** (S) has one reading.
- **LOSS:** None.

### W28.1 — L309: a Part VI route, a Part IX active route, and where they meet

- **STATUS:** applied
- **GROUP:** B2
- **ITEM:** W28
- **FILE-11 LINE:** 309
- **WHERE:** Part VI, **Redundant routes**, L309. Inserted after s2, which is kept byte for byte. S3, including its first clause (03 M28), follows unchanged.
- **REASON WORD:** clarification
- **KIND:** CLAIM
- **CHECK:** check 1, SOUND.
- **OLD:**
````text
may differ in which routes are active; the semantics represents the difference (Derivation 9).
````
- **NEW:**
````text
may differ in which routes are active; the semantics represents the difference (Derivation 9). Here a route is a support of the candidate, a member of \(\mathsf S\), and is a route whether or not any history runs it; it is active in a system when occurrences that realize it form an active route (Part IX), a subnetwork of actual occurrences in the system's history. The two meet in \(\operatorname{ProducedBy}\) (Part XI), which credits a repair to the contributions whose active routes ran to it, not to the routes a candidate contains.
````
- **DECLARATION:** Part VI now says four things. A route is a support of the candidate, a route whether or not any history runs it. It is active in a system when occurrences that realize it form an active route in Part IX's sense. ProducedBy credits a repair to the contributions whose active routes ran to it, not to the routes a candidate contains.
- **REASON:**
  - Worklist W28 (trial §3b, J-4, JUDGEMENT; trial §2 on DeepSeek's O45 and Mimo's O19). Part VI's "route" is undefined and read by example. Part IX defines only the active route, in a history. Readers used the difference to split cases that the fixed verdicts settle.
  - Plan 1.2 gives three parts: "a Part VI route is a support of the candidate, a Part IX active route is a subnetwork of actual occurrences, and the two meet in ProducedBy". NEW states all three.
  - One link is added. S2's "which routes are active" needs to say when a support is active, and the link says so.
  - L309 s3's first clause (M28) is kept byte for byte (skeleton conflict 10). "Whether or not any history runs it" stands beside s3's "whether or not anyone has described its work", which is description, not running.
- **CASES AT RISK:**
  - O45: AGREE is secured. The second spring's commitments form a support, so it "was already a route", whether or not it ran. That closes the active-route reading behind DeepSeek's split (trial §2).
  - O46 stays AGREE. S3's second clause is unchanged.
  - O19 stays AGREE. The diagram's route is not an active route, so it is credited with nothing.
  - O39 and O20 stay AGREE, with both active routes credited. O25 and O52 stay AGREE: only the route that ran is credited.
  - O36 stays AGREE. "Each route as written" is a support of the written candidate, which agrees with L301.
  - O13 stays AGREE. Ana's account is a candidate's route, and no active route of hers ran to the repair.
  - I checked the N-cases and none is reached. N1, N2 and N25 turn on idle parts and criticality, not on routes. N23 turns on direction.
- **GAIN:** "Route" has one meaning in Part VI and "active route" one meaning in Part IX, and the text says where credit is read.
- **LOSS:** None.

### W3.5 — Declare L309 s3, a route present from the start, and reassignment (layer 2, row L2-17)

- **STATUS:** record-only
- **GROUP:** M
- **ITEM:** W3, with M28
- **FILE-11 LINE:** 309
- **WHERE:** Part VI, Redundant routes, L309 s3, both clauses; file 10 L324. Record only: layer 2, row L2-17.
- **REASON WORD:** meta (record only)
- **KIND:** CLAIM (layer 2)
- **CHECK:** check 2, SOUND.
- **LOCATOR:** exact file-11 text, occurring once. It is located, not applied, and it is left out of the overlap check.
````text
A route already present in the candidate is a route whether or not anyone has described its work; a component reassigned to a new target after a deletion belongs to a new candidate with its own assessment, and the new candidate's success is not the old one's.
````
- **LAYER-2 ROW:** the row this entry writes into layer 2 of the record (inside W1.2's NEW).
````text
| L2-17 | Part VI, Redundant routes | L324 | L309, sentence 3 | A route already present in the candidate is a route whether or not anyone has described its work, and a component reassigned to a new target after a deletion belongs to a new candidate, whose success is not the old one's. | @@REV2:L2-17@@ |
````
- **DECLARATION:** (layer 2, row L2-17) A route already present in the candidate is a route whether or not anyone has described its work, and a component reassigned to a new target after a deletion belongs to a new candidate, whose success is not the old one's.
- **REASON:**
  - Plan section 0 and 1.2 (W3 "and M28"): 04 §4 finds P2 failing at O45 alone (the row is in 04 §3), SPLIT under file 10 (corrected) → AGREE under file 11, a theory change toward the thoughtful person, through L309 s3's first clause. 03 M28: CLAIM (new), all five readers; not declared; none shown harmful.
  - The skeleton names "L309 s3's first clause". 03's place M28 (02's C45) is the whole of s3: the reassignment clause is new too, and O46 reads it. So the row declares both clauses (conflict 6).
  - B2's W28.1 inserts its route sentence before s3 and keeps s3 byte for byte. The row reads "kept".
- **CASES AT RISK:** None through this entry: it changes no text. O45 keeps the AGREE it gained under file 11, and O46 keeps AGREE (second clause). B2's W28.1 guards O45, O19, O39, O52, O25 and O20 (skeleton conflict 10).
- **GAIN:** The one sentence behind the only verdict S81 found changed between the files, apart from O48, is declared.
- **LOSS:** None.

### W34.1 — Part VI: the job-counting lemma and Pres are dropped, and reach with them

- **STATUS:** applied
- **GROUP:** C; edited 25 September (group H)
- **ITEM:** W34; W59
- **FILE-11 LINE:** 315
- **WHERE:** Part VI, "Hard-to-vary" (L315), from the bold label through the end of the first sentence, where Pres is defined. **Edited on 25 September.** Before, this entry's OLD was only the Pres clause (the last part of that sentence) and its NEW added the definition of reach. The OLD is now widened back to the start of the line, taking in the label and the lemma, which are file-11 text that no other entry touches. The NEW is now only the label of the paragraph that W33.1 writes. The single space after this OLD and W33.1's OLD are unchanged.
- **REASON WORD:** change of claim
- **KIND:** CLAIM
- **CHECK:** check 2, SOUND, on the text before 25 September. W34.1 was contested by neither S90 reply. **25 September:** OLD widened and NEW replaced under the owner's position of 24–25 September (see REASON). Checked by the drafter only. OLD occurs once in file 11, starts and ends on L315, and ends where W33.1's OLD begins less one space, so the two do not overlap. The whole list, spliced, applies with `tools/s89_apply_changes.py --self-test`. No outside reader has seen this text.
- **OLD:**
````text
**Hard-to-vary.** For explanatory jobs \(F\subseteq F'\), \(\operatorname{Pres}(F')\subseteq\operatorname{Pres}(F)\), where \(\operatorname{Pres}(F)=\{v\in\mathcal V:\forall f\in F,\operatorname{Account}(E_v,f)\}\).
````
- **NEW:**
````text
**Commitments that do no work.**
````
- **DECLARATION:** Part VI no longer states that, for sets of explanatory jobs \(F\subseteq F'\), \(\operatorname{Pres}(F')\subseteq\operatorname{Pres}(F)\), and no longer defines \(\operatorname{Pres}\); its paragraph on commitments that do no work is headed as such.
- **REASON:**
  - **The owner's position (24–25 September).** Hard-to-vary is not a count over a listed set of versions. No one can list all rivals, even in principle, and the set does not matter. File 11's lemma is exactly such a count: an inclusion between subsets of a family \(\mathcal V\) of variants of \(E\), indexed by sets of "explanatory jobs". It is replaced by rivals and problems (W59.1).
  - **The containment is dropped, not kept under another name.** Five reasons.
    1. It is trivial. Its proof is one line from the definition: "Preserving every job in the larger family includes preserving every job in the smaller family" (F00:L377). No case, derivation or definition uses it: in draft 3, Pres occurs only at D3:L313.
    2. The only content it could add beyond that line is strictness. Strictness needs a witness in the family, and whether one exists turns on the menus and on how \(E\) is written. The same correction has a witness when written as a changed rule (2 → 1) and none when written as a mechanism (1 → 1). (Correction-sticks analysis, §1(3), §2 limit (iv), CE1–CE2.)
    3. Its counts follow the declared family and the wording, not the explanation. They flip with the menus: 1:96 against 64:1. They flip with redescription: one rain part written as one, two or five parts gives 2 → 1, 4 → 3 and 32 → 31 (correction-sticks analysis, §2, "What kind of text"). Inside its own family a bad rescue even registers as harder to vary, 4 → 2 (§1(2), A4(ii)). So it cannot carry the idea its label names.
    4. It rests on two inputs the theory never supplies. "Explanatory job" is defined nowhere (correction-sticks analysis, §5 item 3, and its Appendix A (a)). The family \(\mathcal V\) is neither a declared input nor an index (§4, losses; error-correction analysis, option (c), costs).
    5. Kept under another name, it would still invite reading as a grade. The error-correction analysis finds that "A Pres grade would mostly re-measure how narrow the question is" (option (c)). D3:L25 and D3:L516 refuse a merit function.
  - **What is lost.** Nothing that a verdict, a derivation or another definition uses. Deutsch's comparative usage ("most constrained") gets no home, and it had none that D3:L516 allowed.
  - **Reach goes with the lemma.** W34.1 defined reach so that the lemma's one noun use, "More reach constrains variation", was defined where it was first used. With the lemma gone, the theory has no noun use of "reach": the uses at D3:L151, L245, L331, L397, L556 and L624 are verbs or "reachability". A definition that no text uses would keep "jobs" in the theory. Its one clause that a verdict used, that standing is fixed by the candidate and the world and not by what anyone has checked (N4), is kept in W59.1, stated for questions.
  - **The two gaps found earlier.**
    - "Job is undefined": closed. After the change "job" occurs nowhere in the theory text (grep, 0 hits).
    - "The variation family is not a declared input": closed in substance. \(\mathcal V\) now occurs only as the domain of (D), \(\operatorname{Boundary}_{E,p}\), where whether a pair \((v,w)\) belongs is fixed by \(v\) and \(w\) alone. No claim about a candidate or a pair of edits turns on which family is declared, and no case or other definition uses (D).
  - **The label.** W33.1's sentences on commitments that do no work stay, so the paragraph needs a label in place of "Hard-to-vary". Every paragraph of Part VI after (D) has one. "Commitments that do no work" uses W33.1's own phrase and adds no new word.
- **CASES AT RISK:**
  - **O36: toward.** Pres counted variants nobody wrote, which the error-correction analysis found in tension with O36 (option (c)). Nothing in Part VI now speaks of an unwritten route, and W59.1 says that a candidate nobody has offered is no one's rival.
  - **N4 (O56).** Q1 was "toward" through reach being "fixed by E and the world". It stays toward through W59.1's sentence: whether a candidate is an account of a question is fixed by the candidate and the world, whether or not anyone has asked the question. If W59.1 were dropped, Q1 would hold on realism alone (D3:L67), and the declared move toward would go. Q2 rests on Deploy and Attempt, which are unchanged.
  - **N5 (O57)** was watched under reach. It holds under this entry and moves toward under W59.1.
  - **N7 (O59).** "Bea's account is fuller" was read as reach (correction-sticks analysis, §3, row N7). It now rests on (E): Bea's account is also an account of the further question why the rise works only in that range, and Maya's is not. It holds.
  - **No row rested on the lemma.** N1, N2, N3, N24, N25, O24, O45, O46, O47, O48 and D3-T hold.
- **GAIN:** Part VI no longer carries a count over a family nobody declares, on jobs nobody defines. Both undefined inputs leave with it.
- **LOSS:** The containment (H) inherited from file 00 goes, and with it "the containment need not be strict" (W33.1). Reach is no longer defined, and Deutsch's reach has no named counterpart (sources note).

### W33.1 — Part VI: (E) tolerates a commitment that does no work; (B) marks it

- **STATUS:** applied
- **GROUP:** C; edited 25 September (group H)
- **ITEM:** W33; W59
- **FILE-11 LINE:** 315
- **WHERE:** Part VI, "Hard-to-vary" (L315), the lemma's last sentence ("More reach constrains variation; …"). **Edited on 25 September.** Before, NEW kept that sentence and added four after it. It now drops that sentence and the last of the four, on Pres, and keeps the three on commitments that do no work, byte for byte. W34.1's new label heads the paragraph.
- **REASON WORD:** change of claim
- **KIND:** CLAIM
- **CHECK:** check 2, FIX. Four defects: under the drafted test every commitment of L313's infinitary support "does no work"; "any support" could be read as "some support"; the declaration's "or" let one half of the test suffice; and "measure", as in W36.1. NEW scopes the label ("does no work by itself in the candidate"), states both halves for every support, says what happens when Γ is infinite, and reads "a separate matter, shown by Pres". Cases: O2's "this derives L275 s2's rule" is struck (circular); O19 is added, watched.
  - S90 cross-examination: s90_xexam_atria_C, point 3 (R24 STANDS, naming a move toward on N1) — KEEP, after the cross-examination. Cross-examination of revision 2 (S90 part C): Atria gave STANDS and named, under (d), a declared move toward the fixed verdict on N1 ("Strike it out and the account works exactly as before" read as the no-work test, with \(\{d\}\) critical in no support), and claimed that the test is equivalent to "\(\{d\}\) critical in no support". Mimo gave STANDS with no point. Ruled KEEP after the cross-examination. The move on N1 is toward, on the reading where the sentence constrains nothing, and the declaration accounts for it. The claimed equivalence is false (Interference, L309: \(\{b\}\) is critical in no support but fails the addition half), and NEW does not assert it; NEW's "then" consequences follow from the two-halved test. N1's watch on the redundant-route and unfaithful readings stays as recorded. It comes from (B), L307 and (F1), not from this entry. O45, N2 and O8 hold.
  - **25 September:** NEW and the declaration edited under the owner's position of 24–25 September. Two sentences are removed: file 11's "More reach constrains variation; the containment need not be strict; counting jobs is not a warrant.", which NEW had kept, and NEW's last sentence, "How hard an account is to vary is a separate matter, shown by \(\operatorname{Pres}\), and it grades nothing." The three sentences between them are unchanged, and R24's KEEP was ruled on them. The REASON WORD moves from clarification to change of claim, because a file-11 sentence is now withdrawn. Checked by the drafter only; no outside reader has seen this text.
- **OLD:**
````text
More reach constrains variation; the containment need not be strict; counting jobs is not a warrant.
````
- **NEW:**
````text
(E) has no condition that each commitment do work. A commitment \(d\) does no work by itself in the candidate when every support stays a support after \(d\) is added to it and after \(d\) is removed from it: a candidate carrying \(d\) then meets (E) exactly when it meets (E) without \(d\), and \(\{d\}\) is critical in no support (B). When \(\Gamma\) is infinite, a block of such commitments can still be critical (Infinitary support).
````
- **DECLARATION:** Part VI no longer says that more reach constrains variation, that the containment need not be strict, or that counting jobs is not a warrant; it now says that (E) has no condition that each commitment do work; that a commitment such that every support stays a support when it is added and when it is removed does no work by itself in the candidate, leaves the candidate's standing under (E) unchanged and is critical in no support; and that when the commitments are infinitely many a block of such commitments can still be critical.
- **REASON:** Worklist W33 (source point 2; verify obs 2, PARTLY CONFIRMED; M7). The source counts superfluous features as a defect. (E) accepts a candidate that carries a commitment doing no work, and Part VI reports such a commitment only through (S) and (B). The text never says this (worklist). The plan's wording, "(E) is fidelity: a commitment that does no work passes (E) …", is made exact in two places. (i) (E) is not only fidelity: non-circular dependence and non-vacuity are also conjuncts. So the sentence says instead that (E) has no condition that each commitment do work. That is true, because non-circular dependence asks only for some nonempty block. (ii) "Does no work" is given a test in Part VI's own terms: adding the commitment to any support, or removing it from any support, leaves a support. Both halves of the claim follow from that test: Γ is a support exactly when Γ∖{d} is, and {d} is critical in no support. The addition half excludes an interfering commitment (Part VI, Interference). The removal half excludes a redundant route (Redundant routes; L309), since removing it from the support in which it is the only route leaves no support. The sentence states no condition (plan 1.2; conflict 12). The departure from the source goes in the sources note (W38). It holds under every W20 option, because it is stated through (S) and (B), not through the wording of non-circular dependence (skeleton conflict 11).
  - **25 September.** The owner's position is that hard-to-vary is not a count over a listed set of versions (W34.1, REASON). File 11's sentence "More reach constrains variation; the containment need not be strict; counting jobs is not a warrant." comments on the containment that W34.1 drops, and its words "reach", "containment" and "jobs" have nothing left to refer to. The last sentence named Pres, which W34.1 drops. "It grades nothing" is still true, and it stays said where it belongs: D3:L25 and D3:L516 supply no merit function, and W59.1 says that nothing in rivals and problems counts, grades or ranks. W36.1's "how hard an account is to vary is a separate matter (Part VI)" still lands, on W59.1's "easy to vary". The three kept sentences answer the source's point on superfluous features and do not depend on Pres, as the error-correction analysis confirms (section 2, "What the three situations show": "An idle part cannot make a candidate an account").
- **CASES AT RISK:**
  - O36, O45 and O47 hold. P in O36 is critical, not idle. The second spring in O45 fails the removal test: removing it from the support in which it is the only spring leaves no support. So it is a route, not idle. The locked room in O47 fails the addition test, so it is interference, not idle.
  - O2 holds. The bell part does no work for the tide question. The candidate meets (E) with it exactly when it meets (E) without it, and without it the almanac restates the answer (L275), so it fails either way. This derives L275 s2's rule.
  - N1: toward if the sun-god sentence constrains nothing, or is not among the active commitments. Watched: if it is read as a second component that keeps the tilt steady, it is either a redundant route or an unfaithful component. As a redundant route it fails the removal test, and the verdict "not part of what explains" moves to DISAGREE. As an unfaithful component it fails the addition test; that is interference, and "Tomas explains" is at risk. Which reading applies turns on how Γ is typed (W20, held).
  - N25 does not move: the difference between dog and turtle is a matter of Derivation 2's kinds (W19, held). N2 does not move: the patch was fitted after the fact, which is the historical index. N7 and O8 hold: scope is untouched.
  - **25 September.** No row rested on the two removed sentences. N1 keeps R24's move toward, which came from the three kept sentences. N2 and N25 now also have W59.1's reasons (see there). O36 moves toward under W34.1.
- **GAIN:** The split between (E) and (B) is stated, with a test for idleness that excludes interference and redundant routes. After 25 September the paragraph says only that, and no longer comments on a count.
- **LOSS:** The theory now says openly that it tolerates idle parts, which the source counts as defects. The explicit "it grades nothing" moves out of this paragraph (W59.1; D3:L25; D3:L516).

### W59.1 — Part VI: hard-to-vary stated through rivals and problems

- **STATUS:** applied
- **GROUP:** H
- **ITEM:** W59 (new: the owner's position of 24–25 September on hard-to-vary)
- **FILE-11 LINE:** 317–319
- **WHERE:** Part VI, after its last paragraph (L315, headed "Commitments that do no work" after W34.1) and before the rule at L317 that opens Part VII. Two paragraphs are inserted, "Rivals" and "Problems". The anchor is L317–L319 (the rule, the blank line and the Part VII heading), kept byte for byte, as W38.1 anchors on L7–L9. No other entry touches L316–L319.
- **REASON WORD:** change of claim
- **KIND:** CLAIM
- **CHECK:** drafted 25 September; checked by the drafter only. OLD occurs once in file 11 and overlaps no other OLD. The whole list, spliced, applies with `tools/s89_apply_changes.py --self-test`: one diff hunk, beside this entry. Every sentence was checked against its pointer in draft 3 (see REASON, "What each sentence rests on"). No outside reader has seen this text.
- **OLD:**
````text
---

# Part VII — Exact constructions
````
- **NEW:**
````text
**Rivals.** Two explanatory candidates for one question \(p\) are **rivals** when each is offered as an answer to \(p\) in place of the other and they differ in what they claim on \(C\), not only in how it is written: they are not one account on \(C\) in the sense of Derivation 2 (paired active components with one anchor and one kind on \(C\), and one answer profile). Each is offered for the whole of \(p\), and so claims the conditions of (E) at every pair of \(C\), tested or not. Two candidates **conflict** at a pair \((a,b)\) when, whatever the target's relations there, not both meet (F1), (F2) and (A) there, as when their answers there differ, or two of their active components with one anchor have different relations there. A result is **established** for an assessor who holds a usable receipt for it (Part IX); by (K3), a result that tells against a candidate tells against it only together with the background and instruments of the test that yields it. A candidate **fits** what is established when no established result shows it failing a condition of (E). No list of all rivals is supposed: the rivals of a candidate are those someone has conjectured, and a candidate that nobody has offered is no one's rival.

**Problems.** Two rivals that both fit what is established pose a **problem for \(p\)**: a conflict between ideas that what is established has not settled. It is of one of two kinds. (i) The rivals conflict at some \((a,b)\in C\). Establishing what the target does there is then a **test** that solves the problem whatever it shows, since afterwards at most one of them fits; an answer it refutes stays refuted on \(p\) (Part VIII). (ii) They conflict at no pair of \(C\): the contract does not contain their conflict. Their answers then agree at every pair of \(C\), so no established answer holds one of them to account without the other, no test the question admits is sure to solve the problem, and where both meet (E) on \(C\) both are accounts of \(p\). A candidate is **easy to vary**, in the sense used here, when it and a rival pose a problem of the second kind, and a criticism that it is easy to vary supplies such a rival (Part IX). Where both rivals are accounts on \(C\), a claim that one is right and the other wrong is a claim that some admitted change separates them, and must supply it, as a claim that one assignment of anchors is "really" right must (Derivation 2, Consequence). The remedy is a finer contract, which is a new question (Part III); whether a candidate is an account of a question is fixed by the candidate and the world, whether or not anyone has asked the question (Part I). Nothing here counts rivals, grades a candidate or ranks candidates. A problem that a system represents can be a recognized difficulty (Part X), as when giving one answer to \(p\) meets a claimed obligation only by dropping a rival that fits as well, and keeping such a rival is protected (Part XI).

---

# Part VII — Exact constructions
````
- **DECLARATION:** Part VI now defines rivals for a question (candidates each offered as an answer in place of the other that are not one account on its contract), when two candidates conflict at a pair, when a result is established (a usable receipt, with (K3)'s caveat) and when a candidate fits what is established; it says that no list of all rivals is supposed; that two rivals that both fit pose a problem for the question, which a test at a pair of the contract where they conflict solves whatever it shows; that where they conflict at no pair of the contract their answers agree at every pair and no test the question admits is sure to solve it; that a candidate is easy to vary when it and a rival pose a problem of that second kind, and a criticism that it is easy to vary supplies such a rival; that where both rivals are accounts, a claim that one is right and the other wrong must supply an admitted change that separates them, the remedy being a finer contract, which is a new question; that whether a candidate is an account of a question is fixed by the candidate and the world, whether or not anyone has asked it; that nothing here counts, grades or ranks; and that a represented problem can be a recognized difficulty.
- **REASON:**
  - **The owner's position (agreed in conversation, 24–25 September).** Hard-to-vary is not a count over a listed set of versions: no one can list all rivals, even in principle, and the set does not matter. A variation is a competitor, and two discovered rival explanations that both fit constitute a problem. Three refinements were agreed:
    1. Rivals must differ in what they claim, not only in wording, since a redescription is one explanation (Derivation 2).
    2. "Fit" means fit the whole question, every admitted change, tested or not. This splits problems into two kinds. Rivals that differ at some change the question covers are settled by a test there. Rivals that differ nowhere the question covers cannot be held to account by the question, and that is the mark of an easily varied explanation ("Demeter grieves" against "Persephone is underground").
    3. Deutsch's "easy to vary" judges an explanation before anyone offers a rival. On this view the criticism is the producing of the rival, and no grade or count is needed.
  - **What the theory already half-said.**
    - Revised Derivation 2's Consequence (D3:L562): two candidates with one answer profile; a claim that one is "really" right must supply a separating admitted change; "The remedy is a finer contract, which is a new question".
    - The recognized difficulty (W35; D3:L223, L423).
    - Grievance 4 (D3:L43): an exclusion is caught "by any criticism that supplies the excluded change". This is the model for "a criticism that it is easy to vary supplies such a rival".
    - The error-correction analysis lists what the theory leaves open: "A choice between candidates the contract does not tell apart" (section 1, citing D3:L562). It also finds that a new adjustable part is "caught in the verdict whenever the question is left open … only as a fact that a later test would show" (section 2). That is the first kind of problem, and the test is the later test.
  - **Why it is stated this way.**
    - *Rivals.* "Offered as an answer to \(p\) in place of the other" makes a rival a competitor, as the owner's "a variation is a competitor" asks. So two compatible accounts are not rivals merely because they differ. A fuller account beside a leaner one (N7), and two real springs (O45), are compatible accounts of this kind.
    - *Not one account.* "Not one account on \(C\) in the sense of Derivation 2" is refinement (1), in the theory's own relation. The parenthesis gives that relation's content, as Derivation 2's (ii) states it: paired active components with one anchor and one kind on \(C\), and one answer profile. With "one anchor" in it, the parenthesis keeps O46's spring and cable apart, as W19.2's REASON requires.
    - *The whole of \(p\).* "Each is offered for the whole of \(p\) … at every pair of \(C\), tested or not" is refinement (2). It rests on realism and on (E) quantifying over every pair (D3:L67, L265).
    - *Conflict.* It is defined so that the two kinds are exhaustive and each claim about them is true. The two named ways follow from (Q) and (F1). \(\operatorname{Ans}_p(a,b)\) is one value, so candidates with different answers there cannot both meet (A). An anchor's projected relation is one relation, so two components with one anchor and different relations there cannot both meet (F1).
    - *Established.* The (K3) clause is K3's own caveat (D3:L389). What is established is read through Part IX's usable receipts, so the semantics gains no new input. The same definition serves W60.1.
    - *Problem for \(p\).* The bold term is "problem for \(p\)", not "problem". The bare word keeps the passing sense it has at D3:L397 ("problem-directed activity") and D3:L399 ("an available problem"). There a first representation is built from a problem, and two rivals would make no sense.
  - **What each sentence rests on (checked in draft 3).**
    - Kind (i). "At most one of them fits": at the pair, not both meet the conditions whatever the target does. "An answer it refutes stays refuted on \(p\)": W60.1.
    - Kind (ii).
      - "Their answers then agree at every pair of \(C\)": different answers at a pair would be a conflict there.
      - "No established answer holds one of them to account without the other": equal answers stand or fall together under (A).
      - "No test the question admits is sure to solve the problem": at every pair some relations of the target let both meet the conditions.
      - "Where both meet (E) on \(C\) both are accounts of \(p\)": this is (E) itself.
      - The sentence claims no more than this. A test can still refute one of the two for an error of its own, as when an anchor that only one of them uses fails (F1). That is why the text says "no test … is sure to", not "no test can".
    - "Where both rivals are accounts on \(C\), a claim that one is right and the other wrong … must supply" a separating change. If both meet (E) on \(C\), nothing in \(C\) separates them, so such a claim is about a change outside \(C\), as in Derivation 2's Consequence. The qualifier "where both … are accounts" is needed: without it, an (F1) failure of one rival inside \(C\) would be a counterexample.
    - "Whether a candidate is an account of a question is fixed by the candidate and the world, whether or not anyone has asked the question": (E) uses neither \(O_p\) nor \(\rho_p\) (D3:L231–265), and whether a transport is faithful is independent of acceptance (D3:L67). This is W34.1's reach clause, kept and stated for questions.
    - The recognized-difficulty sentence is an instance of W35.3's second clause (D3:L423): "what the system holds meets a claimed obligation only by failing a protected one". It says "can be", as D3:L223 does for a violation.
  - **The easy-to-vary sentence is a definition, not a grade.** It needs an offered rival, which is refinement (3). It is relative to \(p\) and to what is established. It is symmetric between the two rivals. It counts nothing and ranks nothing.
  - **The correction-sticks analysis supports this form.** It found that no Pres statement can separate a good rescue from a bad one on the symmetric record (1:1, 4:4, 6:6). Only "a job holding a pair where they differ" can, and "it is (E) on that job, not a count" (§1(2); §2, limit (iii)). That job is kind (i)'s test.
  - **The owner's example.** "Demeter grieves" and "Persephone is underground" (as the cause, with no grief) cut the target differently: grief is a mediating component that the other lacks. So they are not one account on \(C\). On the Greek question they give one answer at every pair, so they conflict at no pair of \(C\), which is kind (ii). A change that set the mediating state on its own would lie outside that contract.
  - **Labels do not make rivals.** Two tellings that differ only in labels, a dog or a turtle (N25), are one account in Derivation 2's sense, not rivals. This agrees with Deutsch's own reduction of the Persephone and Freyr myths to one core explanation (p.21). The sources note records it.
- **CASES AT RISK:**
  - **O24 (the unused joint setting): toward.** The two arrangements fit every tested setting and conflict at one untested joint setting, reachable by hand and so a pair of \(C\). That is kind (i). "the record has not chosen between them" is a conflict that what is established has not settled, and "One reachable setting is enough" is the test that solves it whatever it shows. File 11 carried O24 through Derivation 3 and L257 s2 (W19.2, CASES AT RISK). It now has a direct statement.
  - **O36 (a premise both routes use): toward.** "A candidate that nobody has offered is no one's rival", with "no list of all rivals is supposed", is O36's "a fact about a candidate nobody has written". Pres, which counted such candidates, goes (W34.1).
  - **O45 (the spring nobody mentioned): holds.** The account holds both springs as one candidate, and no candidate is offered in its place. Two real springs are compatible, and a fuller candidate is not a rival for being different. The verdict rests on D3:L231 (W20.1) and D3:L307, which are untouched.
  - **O46 (the cable that used to be a spring): holds, on firmer text.** The cable account anchors a different subnetwork, so it is not one account with the spring account. Offered in its place, it would be a rival, not a survivor. Its success is its own (D3:L307).
  - **O48 (the forbidden wire): holds; watched.** A reader might take a conjectured arrangement with the forbidden wire as a rival that keeps the unseen setting open. It poses no problem. A rival must fit what is established, and a candidate whose component needs a wire the devices are established to lack fails (F1) against that result. O48 rests on Derivation 3 and D3:L475, which are untouched. This entry speaks of candidates for a question, not of a selection population.
  - **D3-T (O76): holds, and moves toward on its reason.** The discarded design failed a tried setting, so it does not fit what is established and poses no problem. "Ivo would need two designs that both pass and still differ at the untried setting" describes a problem of kind (i), and none exists. The verdict rests on Derivation 3, which is untouched.
  - **N1 (the sun god): holds.** No candidate is offered in place of Tomas's. The sun-god sentence is W33.1's matter, a commitment that does no work, not a rival. A telling that swaps the god for another god is one account with Tomas's on \(C\), not a rival.
  - **N2 (the myth amended): holds (No), and moves toward on its reason.**
    - The original myth fails the southern reports, so it no longer fits.
    - The amended myth's "No" rests on (E): (F1), and non-circular dependence as W20.2 words it. This entry does not touch that.
    - "Had the sailor reported something different, the storyteller could as easily have changed the story another way" is now statable. Before the report, a variant that sends the warmth south conflicts with the myth at no pair of the Greek question, so the myth was easy to vary in the new sense (kind (ii)). The sailor's report is a pair at which the two conflict.
  - **N3 (a myth about winter): holds on both questions, and moves toward on the reason.**
    - "Its details … could be swapped for others that fit the Greeks' facts just as well" is a rival of kind (ii).
    - Q1's "No" rests on non-circular dependence, since the yearly return is written into the bargain. Q2's "an explanation … only in form" rests on W36.1. Neither moves.
    - Watched: a reader might carry "both are accounts of \(p\)" over to the myth. The text says so only "where both meet (E) on \(C\)", and the myth does not.
  - **N4 (O56).** Q1 stays toward through the sentence on questions nobody has asked (see W34.1). Q2 is unchanged.
  - **N5 (O57): toward.** The rule's two readings, by months and by seasons, are rivals. They conflict at no pair of the home question, and they conflict at the southern change. At home that is a problem of kind (ii). The remedy is a finer question, and a trial in the south is a test that solves it. "The rule itself cannot tell him which reading to trust … he needs what the rule leaves out … or else trial" says the same.
  - **N7 (two bakers): holds; watched.**
    - As written, the bakers do not offer their accounts in place of each other, so they are not rivals, and "both explain" rests on (E).
    - A reader who treats them as rivals finds that they conflict at no pair of Maya's contract. Each is then "easy to vary" relative to the other, in the defined sense. Nothing is graded, both remain accounts, and Bea's is also an account of why the rise works only in that range.
    - Risk: a reader who takes "easy to vary" as a defect pulls against "Leaving them unexplained does not weaken her explanation".
  - **N24 (two sealed sorts of matter): holds.** Asha's weak reading and Bram's claim use different queries, so they answer different questions and are not rivals for one \(p\) (D3:L151). The verdict rests on W45.1 and Part XIII's barrier.
  - **N25 (what holds the universe up).** Q1 holds on non-circular dependence. Q2 moves toward.
    - The dog and turtle stories pair their components with one anchor and one kind, and they have one answer profile. They are one account written two ways, not rivals.
    - Taken as rivals, a claim that one is right must supply an admitted change that separates them, and nothing inside the universe can supply one.
    - "As explanations they make the same empty claim … the difference between them is idle" is this. Q2 was watched under W19.2 and now has a direct statement.
  - **Others.** O1: its second half ("the series … is a retreat") stays SILENT, since nothing here reads a series; for its first half see W60.1. O27: holds. "The one test that would separate them" is a kind (i) test, and the robot's reinterpretation is (K3)'s caveat, which the established clause states. The attribution ("mostly") is not reached. O2, O8 and O47 hold.
- **GAIN:** The theory says what hard-to-vary comes to without a count, a family or a grade. An easily varied candidate is one with a rival that fits as well and that the question cannot separate from it. The remedy is a finer question, and the criticism is the rival. Case (i) states the crucial test, O24's case, directly.
- **LOSS:**
  - Two paragraphs (about 470 words) and five defined terms.
  - "Easy to vary" is symmetric and relative to what is established. It gives no ground for preferring either of two kind-(ii) rivals, which is Deutsch's comparative use.
  - A candidate nobody has challenged with a rival is not called easy to vary, however loose it is. That is refinement (3), and it gives up Deutsch's judgement before any rival is offered.
  - A candidate with a kind-(ii) rival is still an account of its question if it meets (E). Deutsch would say such an explanation explains nothing (sources note).

### W40.1 — Part VII: why the absent structure appears is a separate question

- **STATUS:** applied
- **GROUP:** C
- **ITEM:** W40
- **FILE-11 LINE:** 337
- **WHERE:** Part VII, "Explanations that remove structure" (L337). One sentence is added after the last sentence, which is kept byte for byte, attack pointer included (D9).
- **REASON WORD:** clarification
- **KIND:** CLAIM
- **CHECK:** check 2, FIX. "Why does X appear?" used a bare X where the paragraph defines only "X-effect"; NEW reads "the question why it appears". Inserted before "This is the semantics' treatment …", the new sentence took over the antecedent of "This"; the entry is now anchored on the paragraph's last sentence, which it keeps byte for byte, attack pointer included (D9).
  - S90 cross-examination: s90_xexam_atria_C, point 3 (R25 STANDS, naming a move toward on N22); s90_xexam_mimo_C, point 5 (R25 STANDS, naming an undeclared description) — FIX, declaration only (KEEP and FIX reconciled to the FIX), after the cross-examination. After the cross-examination (S90: Atria C point 3, R25 STANDS, naming a declared move toward N22; Mimo C point 5, R25 STANDS, saying the declaration leaves "bare denial" uncharacterised): FIX, declaration only. The clause "which offers no component that responds to a change in what produces the appearance" is the only place in file 11 or the draft that says what makes a denial bare, and it is what puts N22's Wren under the exclusion and Yuri outside it; the declaration now carries it in NEW's words. OLD, NEW and KIND unchanged. A second checker (Mimo C, item 5) ruled KEEP on the same replies, finding the drafted declaration exact; the batch-3 reading takes the FIX, whose declaration quotes NEW's clause word for word and so is exact on both rulings' tests.
- **OLD:**
````text
This is the semantics' treatment of eliminative explanation; it is offered as adequate and is listed under attack (B) in Part XV as a place where it may not be.
````
- **NEW:**
````text
This is the semantics' treatment of eliminative explanation; it is offered as adequate and is listed under attack (B) in Part XV as a place where it may not be. Where the absent structure appears to be present, the question why it appears is a separate question with its own target and contract (Part III): an account of the absence neither answers that question nor needs to, and a bare denial, which offers no component that responds to a change in what produces the appearance, is not an account of it.
````
- **DECLARATION:** Part VII now says that where an absent structure appears to be present, why it appears is a separate question with its own target and contract, which an account of the absence neither answers nor needs to answer, and of which a bare denial, which offers no component that responds to a change in what produces the appearance, is not an account.
- **REASON:** Worklist W40 (M6; source point 15; the source holds that to deny a thing exists one must also explain why it seems to). Part VII's treatment asks nothing about the appearance. The plan takes a clarification, not a condition (1.2). The appearance question is another question in Part III's sense (L153: "Two questions with the same D and different (C, Q) are different questions, and an answer to one is not an answer to the other"). So an account of the absence is judged on its own contract and needs no answer to the appearance question. A bare denial has no component that answers to changes in what produces the appearance, so it cannot meet (F1) or non-circular dependence on that second question. The pointer "attack (B) in Part XV" is not touched (D9); group A's check W27.0 found it CORRECT. W49 (absence and prevention) is left out.
- **CASES AT RISK:**
  - N22: toward. Wren offers no component for the appearance question. Yuri offers one, machinery that reads memories and produces reports; the question does not ask whether that candidate is adequate. After the cross-examination (S90): Atria C (point 3) reads the same move toward; with the clause declared, both halves are accounted for.
  - N8 holds: it is obstruction, and there is no appearance to explain. N25 holds.
  - O34 was checked. The colleague's supplied meaning is a different question (L163), not an eliminative account, and O34 does not move. No other O-case is eliminative.
- **GAIN:** An account of an absence and an account of an appearance are kept apart, and a bare denial has a stated place. Attack (B) in Part XV has a sharper exposed case.
- **LOSS:** None: no condition is added to the first question.

### W24.1 — Type \(S_a\), \(T_a\) and the generators in functional transport

- **STATUS:** applied
- **GROUP:** A
- **ITEM:** W24
- **FILE-11 LINE:** 351
- **WHERE:** Part VIII, "Functional transport" (L351), before sentence 1.
- **REASON WORD:** erratum
- **KIND:** WORDING
- **CHECK:** check 1, SOUND. For W31 (held): the current W31 candidate writes an unsubscripted S; when W31 is drafted it must say which process S is (for example, the target next-step map S).
  - S90 cross-examination: s90_xexam_mimo_A2, point 4 (R26 STANDS, naming an undeclared change of claim on one reading) — FIX, wording only, after the cross-examination. The scope-change claim fails: "generator" occurs nowhere else, the only generated structure is Part II's admitted edits \(A\), and 00:518 says "for every admitted generator", so the two terms are coextensive. The quantifier mismatch is real, and the condition now reads "for every admitted generator \(a\)", 00:518's phrase. KIND WORDING, DECLARATION none and the CLAIM fallback line are unchanged. Atria (s90_xexam_atria_A2, point 8) found that the typing sentence binds free notation and restricts nothing, which agrees.
- **OLD:**
````text
**Functional transport.** If \(\pi\circ S_a=T_a\circ\pi\) for every generator \(a\),
````
- **NEW:**
````text
**Functional transport.** Let \(S_a\) be a target process and \(T_a\) a represented process for each admitted generator \(a\). If \(\pi\circ S_a=T_a\circ\pi\) for every admitted generator \(a\),
````
- **DECLARATION:** none (WORDING: the typing follows from \(\pi:X_D\to X_E\) and from Part II's composition of admitted edits; listed in the record). If a checker rules CLAIM: "The functional transport result now says that \(S_a\) and \(T_a\) are target and represented processes for each admitted generator."
- **REASON:** W24 (trial A3 = Mimo M7, VALID). 00:518: "Suppose a target process \(S_a\) and a represented process \(T_a\) satisfy … for every admitted generator \(a\)." 00's sentence is restored in file 11's "Let … If …" form, with 00's words for the typing. It must land before W31 (held), whose \(S\) and \(T\) refer to these processes; the two entries touch different lines (L351, L361).
  - After the cross-examination (S90): The condition carries 00:518's 'admitted generator' as well, so the two quantifiers match (S90, Mimo A2, R26).
- **CASES AT RISK:** None: no O- or N-case turns on functional transport. N20 (error piling up) is read on (T2), not here.
- **GAIN / LOSS:** GAIN: A readable theorem; W31's S and T have a referent. LOSS: Nothing.

### W31.1 — (T2): the hypotheses restored and \(e_n\) defined

- **STATUS:** applied
- **GROUP:** A
- **ITEM:** W31
- **FILE-11 LINE:** 361
- **WHERE:** Part VIII, "Approximate transport" (L361), sentence 1, before the tag. The tag "(T2)" and the two sentences after it are unchanged, so the line reads as the settled wording, which replaces all of L361. W24.1 lands first, at L351.
- **REASON WORD:** erratum
- **KIND:** CLAIM
- **CHECK:** not put to check 1 or check 2. The text is the settled wording (F2), copied byte for byte. Checked by its drafter as W19.1 was. Check 1's note on W24.1 is met: "when W31 is drafted it must say which process S is". The sentence introduces \(S\) and \(T\) and ties them to functional transport.
- **OLD:**
````text
**Approximate transport.** With one-step discrepancy \(\varepsilon\) and an \(L\)-Lipschitz next-step map, \(e_n\le\varepsilon\sum_{k<n}L^k\).
````
- **NEW:**
````text
**Approximate transport.** Let \(S\) be a target next-step process and \(T\) a represented next-step process, as \(S_a\) and \(T_a\) are in functional transport, and let \(d\) be a metric on \(X_E\). With one-step discrepancy \(d(\pi Sz,T\pi z)\le\varepsilon\) at every state \(z\) of a stated scope, and with \(T\) \(L\)-Lipschitz for \(d\), the discrepancy after \(n\) steps from one state \(z\), \(e_n=d(\pi S^nz,T^n\pi z)\) (so \(e_0=0\)), satisfies \(e_n\le\varepsilon\sum_{k<n}L^k\) whenever \(z,Sz,\dots,S^{n-1}z\) lie in that scope.
````
- **DECLARATION:** (T2) now states its hypotheses and defines its quantity. S is a target and T a represented next-step process, as in functional transport; d is a metric on the represented states; the one-step discrepancy d(πSz, Tπz) is at most ε at every state z of a stated scope; and T is L-Lipschitz for d. The discrepancy after n steps from one state z, e_n = d(πSⁿz, Tⁿπz), with e_0 = 0, satisfies the bound whenever z and its first n−1 successors under S lie in that scope.
- **REASON:**
  - **W31** (S88 finding F2, settled NARROWED: (h1) is restated as an undefined \(e_n\), not an omitted hypothesis on starts). The settled finding: "(T2) omits two hypotheses its proof needs, namely whose Lipschitz constant (h2) and where ε holds (h3), and it leaves \(e_n\) undefined (h1), so the start is fixed by no words. On readings that leave these open it has counterexamples (2b for h2, 2c for h3). … This is a drafting omission, fixed by an erratum that restores the predecessor's hypotheses and defines \(e_n\)."
  - **Plan 1.3.2's rule**, fixed before any S88 reply was read.
    - The erratum is taken "unless the S88 reading rules one of the three hypotheses false or excessive". Neither reading does. The narrowing turns (h1) into a definition, and the erratum keeps that definition word for word.
    - The general bound (option B) waits. The F2 reading found it vacuous as worded, since the erratum's definition makes \(e_0=0\) for every system.
  - **Changes since the position after Atria's reading**, all in the settled wording:
    - \(S\) and \(T\) are introduced and tied to functional transport, in W24.1's words "target process" and "represented process" (Mimo's F2 point 7; check 1's note on W24.1). The theory's only other bare \(S\) is the simulation layer (L179, L221), a representing organization.
    - "The stated scope" becomes "a stated scope" (Mimo's point 4(a), partly right). (T2) states no scope of its own, and the predecessor says "on a stated scope".
    - "Let \(d\) be a metric on \(X_E\)" and "\(T\) \(L\)-Lipschitz for \(d\)" are added. The erratum used a \(d\) that no line of file 11 defines, and "Lipschitz" presupposes a metric (found in settling; the predecessor writes \(d_Z\)).
    - The unequal-start clause is dropped (Mimo's point 5). Under the definition, \(e_0=0\) for every system.
  - **Unchanged.** The containment clause stays: Mimo's scope instance defeats the wording as sent at \(n=5\), while this wording claims only \(n\le4\) there, where the bound holds with equality. The Lipschitz hypothesis stays global.
  - **The proof goes through under these words.** For \(k<n\), \(e_{k+1}\le\varepsilon+L\,e_k\) with \(e_0=0\). The first term is bounded because \(S^kz\) lies in the scope, and the second because \(T\) is Lipschitz globally.
  - **Read in place.**
    - OLD is sentence 1 only, so the record shows the one sentence that changes. The tag and the two sentences after it follow NEW unchanged.
    - \(\pi:X_D\to X_E\) (L191), so a metric on \(X_E\) types every term. The letter \(S\) here is the target's step, as \(S_a\) is in W24.1's sentence ten lines above, and the clause "as \(S_a\) and \(T_a\) are in functional transport" ties it.
    - The letter \(z\) is bound twice, once by "at every state \(z\) of a stated scope" and again by "from one state \(z\)". That reads as two quantifiers and needs no change.
    - \(L\) still also names the component relations \(L_j\), which plan 1.3.2 leaves alone.
  - **Classification:** an erratum that restores the predecessor's hypotheses; CLAIM, narrowed, as plan 1.2 expects.
- **CASES AT RISK:**
  - **N20 (O70), weakly: holds, or toward on the first method.**
    - For a method that only joins, cuts and measures lengths, \(L=1\), and the bound gives \(n\varepsilon\) after \(n\) operations. That grows without limit, as the verdict's "the accumulated error grows larger than a goat" says. The bound is an upper bound; it does not show that the error must grow.
    - The second method's rounding is not Lipschitz, and error correction (W42) is left out, so (T2) says nothing of it. Its verdict rests on the case's own reasoning.
  - **No O-case turns on accumulated error.** The S81 case book was searched for "error", "approximat", "accumulat" and "drift".
- **GAIN:** (T2) is a theorem under its stated hypotheses, and Part XV's test on it (L538) can be run.
- **LOSS:** None. The general bound for an unequal start is not added, and the theory nowhere uses a second start.

### W60.1 — Part VIII: a failed answer stays failed

- **STATUS:** applied
- **GROUP:** H
- **ITEM:** W60 (new: the owner's position of 24–25 September, "correction sticks without any record")
- **FILE-11 LINE:** 365
- **WHERE:** Part VIII, "Historical index" (L365). A paragraph is added after it, before the rule that closes Part VIII. The anchor is the paragraph's last sentence, kept byte for byte. No other entry touches L365.
- **REASON WORD:** clarification
- **KIND:** CLAIM
- **CHECK:** drafted 25 September; checked by the drafter only. OLD occurs once in file 11. The whole list, spliced, applies with `tools/s89_apply_changes.py --self-test`. Each claim was checked against (A), D3:L151, D3:L159, D3:L363 and (K3) in draft 3 (see REASON). No outside reader has seen this text.
- **OLD:**
````text
A new index is a new claim.
````
- **NEW:**
````text
A new index is a new claim.

**A failed answer stays failed.** Fix a question \(p\), a pair \((a,b)\in C\) and a value \(y\neq\operatorname{Ans}_p(a,b)\). By (A), a candidate for \(p\) whose answer at \((a,b)\) is \(y\), \(\operatorname{Ans}_E(\tau(a),\sigma(b))=y\), is not an account of \(p\), whether it is the candidate that gave \(y\) there and failed, that candidate offered again, a rival, or a changed candidate that keeps \(y\) there; and the same holds on every question with the same target and query whose contract contains \((a,b)\). Once it is established that the target's answer at \((a,b)\) is not \(y\), this is established of every such candidate alike, with no record of which candidates failed before or of how any was changed. Here "established" is meant as in Part VI: the assessor holds a usable receipt for the target's answer at \((a,b)\) (Part IX), and by (K3) the test that yields it tells against a candidate only together with the background and instruments it relies on; if they come into question, the exclusion does too, for every such candidate alike. A contract that omits \((a,b)\) makes a different question (Part III): an account on it does not answer \(p\), and the failure on \(p\) stands (Historical index).
````
- **DECLARATION:** Part VIII now states that on a question, a candidate whose answer at a pair of the contract differs from the target's is not an account of it, nor of any question with the same target and query whose contract contains that pair, whatever candidate it is; that once the target's answer there is established, by a usable receipt, this is established of every such candidate alike, with no record of earlier failures or changes; that by (K3) the exclusion stands or falls with the background and instruments of the test, for all such candidates alike; and that a contract omitting the pair makes a different question, an account on which does not answer the original, whose failure stands.
- **REASON:**
  - **The owner's position (24–25 September).** Correction sticks without any record. On a fixed question, any explanation that repeats the failed answer fails the basic test. A narrowing of the question after a failure is a different claim that does not answer the original, which stays failed (F11:L161; D3:L159).
  - **The correction-sticks analysis proves the true part and marks its limits.**
    - Its §1(1): "At the failed summer, yes, and no record is needed. (A) holds 'For every (a,b) ∈ C' … any candidate that answers 'south first' at the failed summer is no account on any job whose contract holds that summer: a rival, a rescue, or E0 offered again. This holds while the job is kept."
    - Its limits, all respected here. "Beyond the failed summer, no": the result speaks only of the pair \((a,b)\), and makes no claim about other pairs. "It is not a ratchet": the narrowing clause says a narrowed contract is a different question, not that narrowing is forbidden. "The binding is by the world's answer, not by the recorded observation" (Appendix A (b)): hence the receipt and (K3) clauses.
    - The theory text needs nothing from the analysis's Pres lemma (H\*), which W34.1 drops.
  - **The error-correction analysis** (section 1) lists "The failed claim stays failed" as [TEXT] and "A failed test refutes the conjunction of theory, background and the claim that the test did what was intended" (K3). It also names the save by blaming the background or the test (section 2). The (K3) clause answers it without a record: blaming the background or the instruments reopens the exclusion for every candidate alike, and exempts none.
  - **The hypotheses, stated in the text.**
    - A fixed question \(p\), and a pair of its contract.
    - A value that is not the target's answer there. \(\operatorname{Ans}_p(a,b)\) is one value of \(Y_p\) by (Q).
    - For the second clause, the same target and query, so that \(\operatorname{Ans}_{p'}(a,b)=\mathcal Q(D,a,b)=\operatorname{Ans}_p(a,b)\).
    - For "established", a usable receipt (Part IX), with (K3)'s caveat. The first sentence is a fact of (A) and needs no receipt. Only its being established does.
  - **Each clause, checked in draft 3.**
    - (A), D3:L247–251: the first sentence.
    - D3:L151 ("Two questions with the same \(D\) and different \((C,\mathcal Q)\) are different questions, and an answer to one is not an answer to the other") and D3:L159 ("it does not answer a broader question that failed, and a narrowing adopted after a failure is a new claim at a new index"): the last sentence.
    - D3:L363 (Historical index): "the failure on \(p\) stands".
    - Receipts, D3:L391: a receipt against each such candidate is a derivation over the same leaf, so it needs no record of the candidate.
  - **The place.** Part VIII, directly after "Historical index", whose last sentence it continues, and which W59.1 points to ("an answer it refutes stays refuted on \(p\) (Part VIII)"). It is not a Part XVI derivation, because its proof is (A) read once. Part XV's list of results open to a counterexample is left unchanged: a counterexample to this one would be a counterexample to (A).
- **CASES AT RISK:**
  - **O1 (Bruno): toward on the first half, and the second half stays SILENT.** Each restated rule narrows the contract, so it is a different question that does not answer when the stream floods. The flood question's failures stand, so Bruno has no account of the floods ("Bruno has no explanation of the floods"). Nothing here reads the series, so "the series as a whole is a retreat" is not reached.
  - **D3-T (O76): holds, and moves toward on its reason.** The discarded design's answer at the tried setting (A on, B off) is not the target's, so the design fails there. Any design with that answer fails there too, which is why it "says nothing about controllers that pass".
  - **O27 (the test that fitted neither): holds.** The robot's move puts the instrument in question. The (K3) clause says the exclusion of both diagnoses then reopens alike, which fits the case, and the re-run with the second sensor establishes a new result. The attribution verdict is not reached.
  - **O8 (Petra's own ovens) and N7 (two bakers): hold; N7 is watched.** A scope stated from the start involves no failed answer. N7 is read with Maya's limits "found … by experience". If a reader takes them as narrowings after failures, each narrower claim is a different question. That is D3:L159's point, and "Maya explains" is a verdict on her stated question. The error-correction analysis flagged this reading (option (b), cases).
  - **N2 (the myth amended): holds.** The original myth's answer at the southern pairs stays failed on any question that contains them. The amended myth changes the answer there, so this entry does not bear on it, and its "No" rests on (E).
  - **Untouched: O24, O36, O45, O46, O47, O48, N1, N3, N4, N5, N24 and N25.** None has a failed answer at a pair of a contract. In O46 the deletion is an organization edit, not a failure at a pair (error-correction analysis, option (b), cases).
- **GAIN:** The theory says in one paragraph why a correction sticks on its question with no record of rescues. It says what "established" requires, and why blaming the test exempts no candidate.
- **LOSS:** About 220 words. It does not reach pairs beyond the failed one, runs of saves, or grain changes: the limits the correction-sticks analysis found (§1(1); §4, losses).

### W22.1 — Define \(p_\delta\) and \(\mathcal E_c\) in (K1)

- **STATUS:** applied
- **GROUP:** A
- **ITEM:** W22
- **FILE-11 LINE:** 373
- **WHERE:** Part IX, "Bearing" (L373), sentence 2; the display (K1) at L376 is unchanged.
- **REASON WORD:** erratum
- **KIND:** CLAIM
- **CHECK:** check 1, FIX. "The criticism's interpreted structural account" is file 00's term. File 11 calls such a pair an explanatory candidate (L233), and a criticism can exist when (K1) fails, so the drafted words would call a failed candidate an account (against C's W36.1). NEW now reads "the explanatory candidate (Part V) that the criticism offers for p_δ".
  - S90 cross-examination: s90_xexam_mimo_A2, point 1 (R28 FALLS) — FIX, after the cross-examination. S90, Mimo part A2, R28 FALLS; fresh checker FIX after the cross-examination: \(\mathcal E_c\) is 'the criticism's connection from \(g\) to \(\delta\), interpreted as an explanatory candidate (Part V) for \(p_\delta\)', not the candidate 'the criticism offers'; the declaration says 'says what its terms are', not 'defines its terms'. The reply's own repair, a fifth part for every criticism, is refused. Atria (s90_xexam_atria_A2, point 7) read the wording as sent and gave STANDS without taking up "offers"; its \(p_\delta\) clause is kept word for word.
- **OLD:**
````text
Let \(p_\delta\) be the question about the defect. Then
````
- **NEW:**
````text
Let \(p_\delta\) be the question whether \(z\) has \(\delta\) in respect of \(p\), and \(\mathcal E_c\) the criticism's connection from \(g\) to \(\delta\), interpreted as an explanatory candidate (Part V) for \(p_\delta\). Then
````
- **DECLARATION:** (K1) now says what its terms are: \(p_\delta\) is the question whether the target has the alleged defect in respect of \(p\), and \(\mathcal E_c\) is the criticism's connection from its grounds to the alleged defect, interpreted as an explanatory candidate for that question.
- **REASON:** W22 (trial M2, VALID: \(\mathcal E_c\) occurs once, undefined; neither \(p\) nor \(z\) appears on the right of (K1)). 00:620: "\(\mathcal E_c\) is the criticism's interpreted structural account." The gloss of \(p_\delta\) brings \(z\) and \(p\) into (K1) through \(p_\delta\).
- **CASES AT RISK:** None found. Checked: N11 (Kasia's written faults are criticisms; Jana's bare marks are not), O27, O40 and O50 (the robot notices the test's assumption); none turns on (K1)'s terms.
- **GAIN / LOSS:** GAIN: (K1) is well typed and can be evaluated. LOSS: Nothing. After the cross-examination (S90), \(\mathcal E_c\) interprets a part that every criticism has, and the drafted verb "offers" goes from this clause; nothing else is lost.

### W22.2 — An adverse signal becomes a criticism by a represented alleged connection

- **STATUS:** applied
- **GROUP:** A
- **ITEM:** W22
- **FILE-11 LINE:** 379
- **WHERE:** Part IX, "Bearing", the paragraph after (K1) (L379), sentence 2.
- **REASON WORD:** erratum
- **KIND:** CLAIM
- **CHECK:** check 1, FIX. The drafted condition asked only for a represented connection to a target and dropped the alleged defect, so a bare adverse signal represented as being about a draft would count. NEW reads "represents it as grounds for an alleged defect in a target". N11 (O62) holds: Jana's marks allege no defect, Kasia's written faults do.
- **OLD:**
````text
An adverse signal is not a criticism until an organization represents how it bears.
````
- **NEW:**
````text
An adverse signal is not a criticism until an organization represents it as grounds for an alleged defect in a target.
````
- **DECLARATION:** The condition for an adverse signal to be a criticism is now that an organization represents it as grounds for an alleged defect in a target, not that it represents how the signal bears.
- **REASON:** W22 (trial M1, JUDGEMENT: "represents how it bears" sits uneasily with "A criticism occurrence can exist when (K1) fails"). A criticism that does not bear has no "how it bears" to represent; it has an alleged connection, which L373 already lists among a criticism's parts.
- **CASES AT RISK:** None found. Checked: N11 (bare marks carry no represented connection under either wording), O3 (Nadia's surprises; her verdict is about construction), O27, O40, O50.
- **GAIN / LOSS:** GAIN: The sentence agrees with the one before it. LOSS: Nothing; the condition is weaker than before only for criticisms that fail to bear, which L379 s1 already admits.

### W41.1 — Part X: inexplicit representation, and a witness identified by use, with the relay guard

- **STATUS:** applied
- **GROUP:** C
- **ITEM:** W41
- **FILE-11 LINE:** 401
- **WHERE:** Part X, "Construction": two new paragraphs after L401, anchored on L401's last sentence, which is unchanged. L403 ("Construction is not selection") follows them unchanged.
- **REASON WORD:** clarification
- **KIND:** CLAIM
- **CHECK:** check 2, FIX. "The realization" had no antecedent (NEW: "A system's realization"). The paraphrase of what (R) asks dropped fidelity and provenance (NEW states them). The relay sentence put O18's "The rest is relay" at risk; NEW adds "Use does not by itself construct: received content used as it was received keeps its inherited provenance." The declaration is completed. Cases: as drafted, plus O18 guarded, O11 and O15 toward, O23 watched (the shared word "investigator"), N4 Q2 and N12 (Mr Okafor) watched.
  - S90 cross-examination: s90_xexam_mimo_C, point 3 (R30 FALLS); s90_xexam_atria_C, point 3 (R30 STANDS, naming moves toward) — KEEP (two rulings, one line), after the cross-examination. Cross-examination of revision 2 (S90 part C): Atria said STANDS (declared moves toward on N21, 'she knows it, tacitly' and 'her grasp of it was not handed to her'; O15 kept a hole in the diagrams, not in Sam's construction). Mimo said FALLS (the witness criteria differ from Part IX's reason use: the binding for 'the operative deliberative rule', no structural map, 'lie on' for 'lands on'). Ruled KEEP after the cross-examination. N21 moves toward on both questions, as declared (no format for Deploy; a witness by use for Build). O15 holds at AGREE, which is file 11's mark (S81 01): R30 only supports the passage, and 'toward' above means no more than that. 'As reason use asks of an objection' is a marked parallel. The binding must replace the deliberative rule as specifier, because a verbatim copy would fail N21. (R)'s fidelity and provenance (L401), Build (L399) and the active-route clause keep the map's guard. 'In the manner of' already means 'modelled on'. No case moves away.
- **OLD:**
````text
A small binding newly prepared inside received content is construction of that binding, and the rest of the content keeps its inherited provenance.
````
- **NEW:**
````text
A small binding newly prepared inside received content is construction of that binding, and the rest of the content keeps its inherited provenance.

An inexplicit representation is not an absent one. A pianist can imagine a passage without playing it. A geometer can manipulate a spatial relation without naming every component. An investigator can notice an inconsistency before articulating its premises. None of (R), Deploy and Build asks whether the relevant distinctions and transformations are written in a particular format: what they ask is whether those distinctions and transformations are instantiated, with the fidelity and provenance (R) requires, and used where use is asked.

A system's realization can use a partial, distributed, or temporally extended representation. The relevant bindings can be available through memory, imagery, action rehearsal, or interaction with an artifact. Not every representation must be simultaneously explicit. Retaining a critical target can consist in being able to re-present the relevant distinction, not in storing a complete verbal transcript. A construction witness may therefore identify a binding constructed in the subhistory by its use rather than by a statement of it: by responses that preserve its role bindings, send content-preserving recodings to the same transition and content changes to the changes the binding specifies, and lie on an active route, as reason use asks of an objection (Part IX). Use does not by itself construct: received content used as it was received keeps its inherited provenance. A carrier that passes content on without such use has relayed it, and relay is not construction.
````
- **DECLARATION:** Part X now says that an inexplicit representation is not an absent one; that (R), Deploy and Build ask for no particular format, only whether the relevant distinctions and transformations are instantiated, with the fidelity and provenance (R) requires, and used where use is asked; that a representation can be partial, distributed or extended in time and need not be explicit all at once; that retaining a critical target can consist in being able to re-present the relevant distinction; that a construction witness may identify a constructed binding by its use, in the manner of reason use; that use does not by itself construct, so received content used as received keeps its inherited provenance; and that a carrier that passes content on without such use has relayed it.
- **REASON:** Worklist W41 (source point 14; verify obs 14: "inexplicit" CONFIRMED missing; 00:855–861). Build's witness must identify "the bindings constructed" (L401). A tacit construction cannot show them by a statement. The first new paragraph restores 00:856–857, with two edits. The heading "Inexplicit representation is not absent representation" becomes the opening sentence. 00's "The semantic question is whether the relevant distinctions and transformations are instantiated and used" is narrowed to what each definition asks, because (R) asks for no use and would otherwise gain a use condition. The second paragraph restores 00:858 word for word and adds the plan's relay guard (1.2). A witness may identify a binding by its use. That use is spelled out in the four clauses of reason use (L381), which are what separate use from recitation. A carrier that passes content on without such use has relayed it (L401: "relay is not"). 00:860 (recursive scrutiny) is not restored; the plan takes "the first two paragraphs". No bold label is used, because L403 ("Construction is not selection …") follows and must still read as part of Construction.
- **CASES AT RISK:**
  - N21: toward. She was given examples, never the rule. Her use of the rule on phrases she has never heard identifies the binding, and the binding is not a composition of content-preserving transfers.
  - N13 holds AGREE (the guard). The parrot's responses follow wording, not content. A rephrasing would be repeated differently, a question about the content gets another sentence or a squawk, and recipes would have been repeated as readily. So it has relayed the sentences.
  - N12 holds: Ms Varga's use is Deploy, and Mr Okafor recites. N15 holds: her correction is a small constructed binding (L401, last sentence).
  - O14 holds, and is watched. Kofi uses his retained phrases to order those dishes, which is sensitive to content for that narrow task, so it is not relay. His failure on a new sentence keeps the use narrow (L399).
  - O23 is watched. The passing mention of the seal is not made an inexplicit port: the new text asks whether a distinction is instantiated and used, and L417 makes a dimension mentioned in passing a port only when the account admits changes to it. It holds.
  - O19 holds: the diagram in his hand did no work, and the witness clause asks for an active route. O3, O11, O15, O18, O31, O43, O44 and O49 hold. O32 holds, and moves toward if anything: a dependence found aloud is represented without a drawing.
- **GAIN:** A tacit construction can be witnessed, and relay stays excluded.
- **LOSS:** The witness is harder to check, and Part X grows by two paragraphs.

### W3.1 — Declare L401 s5, a small binding inside received content (layer 2, row L2-24)

- **STATUS:** record-only
- **GROUP:** M
- **ITEM:** W3
- **FILE-11 LINE:** 401
- **WHERE:** Part X, Construction, L401 s5; file 10 L414 (Build). Record only: layer 2, row L2-24.
- **REASON WORD:** meta (record only)
- **KIND:** CLAIM (layer 2)
- **CHECK:** check 2, SOUND.
- **LOCATOR:** exact file-11 text, occurring once. It is located, not applied, and it is left out of the overlap check.
````text
A small binding newly prepared inside received content is construction of that binding, and the rest of the content keeps its inherited provenance.
````
- **LAYER-2 ROW:** the row this entry writes into layer 2 of the record (inside W1.2's NEW).
````text
| L2-24 | Part X, Construction | L414 | L401, sentence 5 | A small binding newly prepared inside received content is construction of that binding, and the rest of the content keeps its inherited provenance; file 10's Build asked for a nontrivial binding construction and said nothing of the rest of the content. | @@REV2:L2-24@@ |
````
- **DECLARATION:** (layer 2, row L2-24) A small binding newly prepared inside received content is construction of that binding, and the rest of the content keeps its inherited provenance; file 10's Build asked for a nontrivial binding construction and said nothing of the rest of the content.
- **REASON:**
  - Worklist W3: O18 moved SPLIT→AGREE on det 01 through this sentence. 03 M35: CLAIM (new), all five readers; not declared.
  - Plan section 0: under 04's rule, O18 is AGREE under file 10 as well (04 §7.9: "M35, O18 AGREE→AGREE (by rule)"). So the sentence is not a changed verdict, but it is an undeclared CLAIM, and it is to be declared only (plan 1.2 W3; D1: file-11 base).
  - C's W41.1 uses this sentence as its anchor and keeps it byte for byte (checked), so the row's last column reads "kept; … adds text beside it".
- **CASES AT RISK:** None through this entry: it changes no text. The rows the sentence carries keep their file-11 marks: O18 (AGREE), O31 (passage changed, AGREE), with O15 and O11 weak, and N15 (O65, a small repair inside received content). C's W41.1 adds text after it, and C watches O18, O31 and N15 there. Skeleton conflict 18: the checkers confirm that O18 keeps its mark.
- **GAIN:** The sentence behind one of the three toward-rows of det 01 is declared, with what file 10 left open.
- **LOSS:** None.

### W21.1 — L405: ≡_ℓ is defined, and 00:746's first sentence is restored

- **STATUS:** applied
- **GROUP:** B2
- **ITEM:** W21
- **FILE-11 LINE:** 405
- **WHERE:** Part X, **Newness**, L405, before the display (N). The clause "With \(R_{<e}\) …" is kept byte for byte, and the display (L407–409) is not touched.
- **REASON WORD:** clarification
- **KIND:** CLAIM
- **CHECK:** check 1, SOUND.
  - S90 cross-examination: s90_xexam_mimo_B2, point 1 (R31 FALLS); s90_xexam_atria_B2, pass 2, point 3 (R31 STANDS, naming moves toward) — KEEP (two rulings, one append), after the cross-examination. After the cross-examination:
    - s90_xexam_mimo_B2 (point 1, R31 FALLS: 'ill-typed and non-symmetric'): KEEP.
      - The transport from d to c is judged on c's contract as (R) judges a transport into c (L205–208, file-11 text unchanged, on which Deploy and so (N)'s repertoire rest). The transport from c to d is typed as in Part V. Both are checked on the changes c commits to.
      - The relation is taken on the contract of the content whose newness is in question. (N) is its only use, and nothing uses symmetry. 'Equivalence' is the file's two-direction sense (L357).
      - The declaration states the definition word for word.
      - The proposed 'each faithful on the contract of its source' would make c new whenever an earlier content commits beyond c. That is a change of claim, against plan row W21, and it could reopen N4.
    - s90_xexam_atria_B2 (point 3, R31 STANDS; names moves 'from unsettled to settled, all toward the fixed verdicts' on O11, O18, O31, N15 and N21): KEEP.
      - It gives the same typing.
      - On O11, O18 and O31, file 11's ruled marks are already AGREE, through Build and L401 s5, so no mark moves. NEW makes New checkable, which is the 'more securely' recorded here.
      - O11's 'Wednesday is neither' rests on the absence of Build. The case says only that the key 'looks like' Tuesday's, which NEW excludes as a criterion.
      - N15 and N21 have no file-11 baseline yet. A move toward on either, if the test round finds one, traces to this declared definition.
- **OLD:**
````text
**Newness.** With \(R_{<e}(s,h)=\bigcup_{\xi\text{ before }e}R_{\beta,\ell}(s,\xi)\),
````
- **NEW:**
````text
**Newness.** Write \(d\equiv_\ell c\) when there are transports from \(d\) to \(c\) and from \(c\) to \(d\), both faithful on \(c\)'s contract at grain \(\ell\). The equivalence is structural at the stated grain, not string equality or similarity. With \(R_{<e}(s,h)=\bigcup_{\xi\text{ before }e}R_{\beta,\ell}(s,\xi)\),
````
- **DECLARATION:** Part X now defines the equivalence in (N): d ≡_ℓ c when there are transports from d to c and from c to d, both faithful on c's contract at grain ℓ. The equivalence is structural at that grain, not string equality or similarity.
- **REASON:**
  - Worklist W21 (Mimo M4, VALID, raised on O3, O11, O18, O27 and O31). (N) uses \(\equiv_\ell\), which is defined nowhere, and (G) and (EK) rest on it.
  - Plan 1.2 asks for a definition by faithful transports both ways on c's contract at grain ℓ, with only the first sentence of 00:746 restored. That sentence is restored word for word. 00:746's reacquisition sentences stay out.
  - The typing follows the file's own usage:
    - a transport to c that is "faithful on \(c\)'s contract" is (R)'s wording (L207);
    - a transport from c faithful on c's contract is Part V's (L233, with C a contract of the source).
  - Written independently of Derivation 2 (worklist conflict 7; skeleton conflict 12). The definition uses no kind-pairing across candidates and no shared anchors, so W19's narrowing, when it lands, does not change it.
  - It is placed before the display so that (N) uses a defined symbol.
- **CASES AT RISK:**
  - O11 stays AGREE, and more securely. Suppose Wednesday's content is equivalent to Tuesday's on its contract. Then it is not new, and it has no Build in any case. So "Wednesday is neither" holds on either reading.
  - O3 stays AGREE. The tally of unseen cards has no equivalent in her earlier repertoire.
  - O18 and O31 stay AGREE. The corrected content is not equivalent to the received one, because they differ at the new lock and at this plant's valve. So it is new to her, and L401 s5 credits the binding.
  - O27 stays SILENT, on the "mostly" point. The reinterpretation is new, and this is unchanged.
  - O15 is not reached: its point is the history of the arrows.
  - N15 (O65): AGREE on "new to her, not to the world" is secured. (N) is relative to her own repertoire, and the miscopied content ("less") is not equivalent to the teacher's.
  - N21 (O71) stays AGREE. Her grasp has no equivalent in her earlier repertoire, which never held the community's convention.
  - N10 (O61): newness for Halima is unchanged.
  - N4 (O56) is watched.
    - The tilt idea as she held it may be equivalent, on the midnight-sun contract, to the account of the midnight sun. If so, a later working-out is not new for someone who already held the idea. That agrees with "working out the connection added nothing to the idea".
    - "Nobody had explained it" turns on use and Deploy, which this entry does not touch.
    - The point may shift. The direction is not away.
  - Away (AGREE→SILENT) only for a reader who takes "faithful on c's contract" to demand fidelity at every grain. The definition fixes grain ℓ.
- **GAIN:** New and Origin become checkable. (N) can no longer be read as string identity or as similarity.
- **LOSS:** Newness now depends on whether transports exist both ways, and a case must supply that or leave it open. Reacquisition (the rest of 00:746) stays unaddressed.

### W3.3 — Declare L419, Ownership (layer 2, row L2-26)

- **STATUS:** record-only
- **GROUP:** M
- **ITEM:** W3
- **FILE-11 LINE:** 419
- **WHERE:** Part X, Ownership, L419, the whole paragraph; file 10 has none (f10 uses "owned" at L414, L476, L488 and L493 without defining it). Record only: layer 2, row L2-26.
- **REASON WORD:** meta (record only)
- **KIND:** CLAIM (layer 2)
- **CHECK:** check 2, SOUND.
- **LOCATOR:** exact file-11 text, occurring once. It is located, not applied, and it is left out of the overlap check.
````text
**Ownership.** The subhistory in Build is owned by \(s\) when its processes run inside the system boundary and resource contract declared for \(s\) (Part XII). Work supplied from outside that boundary, a diagnosis, a decisive question, an instruction about what to read, remains an outside contribution however it is executed inside; a process that runs inside the boundary is the system's own today whoever wrote it; and where the boundary is drawn decides, not where the process sits in the casing. Ownership is not defined by the capability it is meant to ground (Part XII).
````
- **LAYER-2 ROW:** the row this entry writes into layer 2 of the record (inside W1.2's NEW).
````text
| L2-26 | Part X, Ownership | none | L419 | Ownership of Build's subhistory is defined: its processes run inside the system boundary and resource contract declared for the system. Work supplied from outside that boundary remains an outside contribution however it is executed inside; a process that runs inside the boundary is the system's own today whoever wrote it; where the boundary is drawn decides, not where the process sits; and ownership is not defined by the capability it grounds. File 10 used "owned" without defining it. | @@REV2:L2-26@@ |
````
- **DECLARATION:** (layer 2, row L2-26) Ownership of Build's subhistory is defined: its processes run inside the system boundary and resource contract declared for the system. Work supplied from outside that boundary remains an outside contribution however it is executed inside; a process that runs inside the boundary is the system's own today whoever wrote it; where the boundary is drawn decides, not where the process sits; and ownership is not defined by the capability it grounds. File 10 used "owned" without defining it.
- **REASON:**
  - Worklist W3: O41 moved SPLIT→AGREE on det 01 through this definition, with L465. 03 M37: CLAIM (new definition), all five readers; not declared.
  - 04 §7.9: O41 is AGREE→AGREE by rule. 04 §7.10 records the boundary hazard (O30, O17) that B2's W12 and W13 now address.
  - The row declares the paragraph as file 11 has it, "today" included. B2's W13.1 drops "today", and W13.2 + W12.2 adds a sentence. So the row's last column reads "changed by …", and layer 1 carries both changes.
- **CASES AT RISK:** None through this entry: it changes no text. The rows L419 carries: O41 (AGREE); O17, O21, O30, O40, O49 and O51 (passage changed); O27 and O50 (SILENT); O3, O14, O18 and O31 (weak); and N11, N15 and N21 through B2's entries. The marks are guarded by B2's W12 and W13, not by this entry.
- **GAIN:** File 11's new definition of ownership, the one test (b) turned on, is declared as a new definition.
- **LOSS:** None.

### W13.1 — L419 s2: "today" is dropped

- **STATUS:** applied
- **GROUP:** B2
- **ITEM:** W13
- **FILE-11 LINE:** 419
- **WHERE:** Part X, **Ownership**, L419 s2, the middle clause.
- **REASON WORD:** clarification
- **KIND:** CLAIM
- **CHECK:** check 1, SOUND.
  - S90 cross-examination: s90_xexam_atria_B2, pass 2, point 5 (R32 STANDS; listed, found not contested) — KEEP, after the cross-examination. After the cross-examination (S90, part B2): Atria's reply (pass 2) gave STANDS and noted only that "today" is gone, matching Part XII; no move named; kept. Mimo's reply gave STANDS with no point.
- **OLD:**
````text
is the system's own today whoever wrote it
````
- **NEW:**
````text
is the system's own whoever wrote it
````
- **DECLARATION:** Part X no longer says that a process run inside the boundary is the system's own "today", which matches Part XII.
- **KIND AS DRAFTED:** CLAIM. This is strict. It could be ruled WORDING, since L465 says the same without the word. But "today" can be read as limiting ownership of a process to the day it runs, a reading that L465 does not carry, and removing a reading is CLAIM under 03's definitions.
- **REASON:** 03 §8 item 9 (M37): "'today' in L419 … has no counterpart in L465". Plan 1.2, under W13: "drop 'today' from L419 to match L465".
- **CASES AT RISK:**
  - O30 stays AGREE. "Was the robot's work today" is the fixed verdict's phrase about the history that ran, and the history is still dated.
  - O17 and O51 ("today's diagnosis") use the word for the history, not for the time of ownership. They are not reached.
  - I checked for any other row that needs a time limit on ownership, and none does.
- **GAIN:** L419 and L465 state the same rule in the same terms.
- **LOSS:** None.

### W13.2 + W12.2 — L419: credit for content and ownership of a process are different attributions

- **STATUS:** applied
- **GROUP:** B2
- **ITEM:** W13, W12
- **FILE-11 LINE:** 419
- **WHERE:** Part X, **Ownership**, L419. Inserted after s2, whose last clause is kept byte for byte. S3 ("Ownership is not defined by …") is unchanged.
- **REASON WORD:** clarification
- **KIND:** CLAIM
- **CHECK:** check 1, SOUND, on the condition that W23.1 is corrected (it is): "contribution" here keeps L419's ordinary sense.
  - S90 cross-examination: s90_xexam_atria_B2, pass 2, point 5 (R33 STANDS; listed, found not contested) — KEEP, after the cross-examination. After the cross-examination (S90, part B2): Atria's reply (pass 2) gave STANDS; its "lets the theory accept the verdicts' weightings rather than contest them" (O21, O50) names no move. On the texts O21, O27 and O50 stay SILENT on "mostly", since the new sentence supplies no weighting and L516 bars taking it from the verdict. O50's discovery point is secured, as 07 ruled for file 11. O30 stays AGREE. Kept. The weighting clause the reply cites is W6.4 + W14.1's. Mimo's reply gave STANDS with no point.
- **OLD:**
````text
and where the boundary is drawn decides, not where the process sits in the casing.
````
- **NEW:**
````text
and where the boundary is drawn decides, not where the process sits in the casing. Credit for content and ownership of a process are different attributions: a routine written outside the boundary and run inside it is the system's own process, and its content remains its writer's contribution.
````
- **DECLARATION:** Part X now says that credit for content and ownership of a process are different attributions. A routine written outside the boundary and run inside it is the system's own process, while its content remains its writer's contribution.
- **REASON:**
  - **W13.** Trial §3a A4 was ruled INVALID as a hole. Its drafting note says: "one clause saying that the two halves assign different things … would stop the misreading". Trial §2 gives Atria's split on O30. Plan 1.2 asks for "one clause saying credit for content and ownership of a process are different attributions".
  - **W12's L419 half.** 04 §7.10's second suggestion is that "a process written outside and run inside is not 'work supplied from outside'". The skeleton places W12 at L419 as well as L465. This sentence carries that suggestion in the terms of the two attributions: the routine's running is owned, and its content is not.
  - 07 had to rule that the two clauses of L419 s2 are "complementary clauses of one rule", not two readings (O50's discovery point). The text now says so.
  - "Credit" is L433 s4's word, and "outside contribution" is L419 s2's.
- **CASES AT RISK:**
  - O30: AGREE is secured ("Ownership of today's history is the robot's; the origin of the routine is the person's").
  - O40 stays AGREE. "Theirs together" is secured: the robot saw the assumption, and the expert's fix is outside content that the robot ran.
  - O41 stays AGREE. The instruction's content stays outside, so robot-only credit is not available.
  - O50 stays SILENT on "mostly", and its discovery point is secured.
  - O21 and O27 stay SILENT. They move toward (SILENT→AGREE) only for a reader who takes credit for content as a weighting of the achievement. None is supplied: B1's W6.4 lists the weighting as a declared input.
  - O17 stays AGREE, and O49 is not reached.
  - N11 (O62) stays AGREE. The teacher added no content, and the writing is each student's.
  - N15 (O65) stays AGREE. The explanation is the teacher's content, and the correction is her own.
  - N13 (O64) is not reached.
- **GAIN:** The two halves of the Ownership sentence cannot be read as a tension. A routine uploaded from outside has a stated place on each side.
- **LOSS:** None.

### W35.3 — Part X: what a recognized difficulty is

- **STATUS:** applied
- **GROUP:** C
- **ITEM:** W35 (b′)
- **FILE-11 LINE:** 421
- **WHERE:** Part X, "Episodes" (L421). One sentence is added after s1; s1–s3 are unchanged.
- **REASON WORD:** clarification
- **KIND:** CLAIM
- **CHECK:** check 2, SOUND. N19 is watched, not simply toward (a reader has to take one demand as claimed and the other as protected); N18 Q1 is watched (L514 lists obligations "of a repair").
  - S90 cross-examination: s90_xexam_atria_C, point 3 (R34 STANDS, naming a move toward on N19) — KEEP, after the cross-examination. Cross-examination of revision 2 (S90 part C): Atria gave STANDS and named, under (d), a declared move toward the fixed verdict on N19 (the foreseen clash is a represented conflict, a recognized difficulty before any reader), and said the change also fits N18 and O27. Mimo gave STANDS with no point. Ruled KEEP after the cross-examination. N19 Q1 moves toward (SILENT to AGREE) by the declaration's second clause, under every declaration that puts one demand in O and the other in P (O = P included), which the situation supplies. It is a reading only in taking the question's "problem" as the recognized difficulty. N19 Q2 holds or moves toward: what it turns on through (P) is (P)'s and W5.1's, not this entry's. N18 Q1 moves toward for both designers by the first clause. L516's "of a repair" names the same O and P. O27 holds SILENT on "mostly": the robot's "fits neither" is a represented failure of its diagnostic obligation, and the expert's diagnoses are candidates, not claimed obligations. O12 holds SILENT: the failure was represented, and the need met was stated afterwards. D3-T is untouched. "(Part XI)" is exact, and L223's "can be a recognized difficulty (Part X)" agrees.
- **OLD:**
````text
A complete critical episode contains a recognized difficulty, a target available before its criticism, a conjectural objection, and a content-sensitive response.
````
- **NEW:**
````text
A complete critical episode contains a recognized difficulty, a target available before its criticism, a conjectural objection, and a content-sensitive response. A **recognized difficulty** is a failure of a claimed obligation, or a conflict in which what the system holds meets a claimed obligation only by failing a protected one (Part XI), when the system represents it.
````
- **DECLARATION:** Part X now defines a recognized difficulty as a represented failure of a claimed obligation, or a represented conflict in which what the system holds meets a claimed obligation only by failing a protected one.
- **REASON:** Worklist W35 (b′). The worklist notes that the episode's "recognized difficulty" (F10 L432, F11 L421) is undefined. The sources in file 00 are 00:754 (an attempt addresses "a recognized difficulty"), 00:785 and 00:804 ("their reconciliation is a further problem about purposes and obligations"). Missed relation M2 says that Repair "is exactly 'meet o without losing any protected r'" and that what is missing is "a definition of 'recognized difficulty'". The definition uses only Part XI's claimed and protected obligations (L427, L433), so it adds no primitive and no input. Its second limb, a conflict, lets a difficulty exist before any observation bears on it, because nothing in the definition asks for an observation. The word "problem" is not defined in the theory (L399 and L401 use it in passing). The mapping from the source's "problem" to this definition goes in the sources note (W38).
- **CASES AT RISK:**
  - N19: toward. Her two demands conflict in the planned chapter before anyone reads it, and that is a recognized difficulty. The first draft meets one demand by failing the other, so it is not a Repair; the second draft is.
  - N18: toward on Q1. Both designers represent a failure of a claimed obligation, a bridge that stays steady.
  - O12 stays SILENT on its worth point. "The need it met was only recognised afterwards" fits the definition: the difficulty the team represented was that the work was not getting done, and the obligation the question met was stated afterwards. Watched: a reader who requires the met obligation itself to be recognized in advance would read O12's episode as incomplete. The mark is SILENT either way.
  - O27 stays SILENT on "mostly". The robot's "fits neither" is a represented failure, so its episode is complete. That is toward on the episode, with no change of mark. O21, O40 and O50 do not move.
  - O13, O35 and O38 (Repair) are untouched. The sentence defines the difficulty, not Repair.
- **GAIN:** The episode's first ingredient is defined from Part XI, with no new primitive, and a difficulty can come before any observation.
- **LOSS:** A difficulty that the system does not represent as a failure or a conflict of obligations is not a recognized difficulty.

### W23.1 — L427: the contribution Δ is typed

- **STATUS:** applied
- **GROUP:** B2
- **ITEM:** W23
- **FILE-11 LINE:** 427
- **WHERE:** Part XI, **Repair**, L427, before the display (P). The existing clause is kept byte for byte after the inserted sentence.
- **REASON WORD:** clarification
- **KIND:** CLAIM
- **CHECK:** check 1, FIX. The bold definition of "contribution" as a subhistory would make L419 ("a diagnosis, a decisive question"), L536 and L582 (a contract as "the originative contribution") and W13.2's clause into type slips. NEW types Δ without redefining the word: "The contribution Δ of a repair is a subhistory together with the changes of content it makes."
- **OLD:**
````text
**Repair.** For claimed obligations \(O\) and protected obligations \(P\), fixed for the comparison,
````
- **NEW:**
````text
**Repair.** The contribution \(\Delta\) of a repair is a subhistory together with the changes of content it makes. For claimed obligations \(O\) and protected obligations \(P\), fixed for the comparison,
````
- **DECLARATION:** Part XI now types the contribution \(\Delta\) of a repair as a subhistory together with the changes of content it makes.
- **REASON:**
  - Worklist W23 (trial §3b, Mimo on O13, VALID). Δ is never typed, although (P), ProducedBy (L433 s4) and (EK) all take it as an argument.
  - Plan 1.2: "Δ typed as a subhistory with its content changes".
  - The name "contribution" is 00:787's ("a local repair by contribution Δ") and L433 s4's ("it credits each contribution the history establishes").
  - It is placed before (P) so that every later use has a type.
- **CASES AT RISK:**
  - O13 stays AGREE. Ben's tightening is a contribution that makes no change of content, and ProducedBy credits it with the stop.
  - O20, O25, O26, O39 and O52 stay AGREE. Each act is a subhistory, and ProducedBy is unchanged.
  - N19 (O69) and N10 (O61) are supported: each draft, and Halima's month of work, is a contribution.
- **GAIN:** (P) and (EK) have a typed argument.
- **LOSS:** None.

### W5.1 — L433: r(ξ′) over the occasions a protected condition covers

- **STATUS:** applied
- **GROUP:** B2
- **ITEM:** W5
- **FILE-11 LINE:** 433
- **WHERE:** Part XI, the paragraph after (P), L433. Inserted after s1, which is kept byte for byte (03 M38). S2–s5, including s4 (ProducedBy, skeleton conflict 7), are unchanged. The display (P) at L430 is not touched.
- **REASON WORD:** clarification
- **KIND:** CLAIM
- **CHECK:** check 1, SOUND.
- **OLD:**
````text
and a protected condition is lost exactly when it fails on an occasion it covers.
````
- **NEW:**
````text
and a protected condition is lost exactly when it fails on an occasion it covers. In (P), accordingly, \(r(\xi')\) says of a protected condition \(r\) that it held on every occasion it covers from \(\xi\) to \(\xi'\), not only at \(\xi'\).
````
- **DECLARATION:** Part XI now says that in (P), for a protected condition r, r(ξ′) means that r held on every occasion it covers from ξ to ξ′, not only at ξ′.
- **REASON:**
  - Worklist W5 (det 02 §5(ii), C56; 03 M38). (P)'s protection clause \(\forall r\in P[r(\xi)\Rightarrow r(\xi')]\) checks two configurations. L433 s1 defines loss as failure on any covered occasion, and such an occasion can fall between ξ and ξ′. The formula and the prose agree only on this reading.
  - Plan 1.2 asks for the reading "in words". The formula is kept, so (P)'s tag, shape and pointers are unchanged.
  - **Derivation 8 checked** (L602). It transports "histories" along structure-preserving bijections, and the occasions lie in the histories. So it carries them without a change to its text. L602 belongs to no group and is not edited.
- **CASES AT RISK:**
  - O38: AGREE is secured. The stated condition "runs at all times during the work" fails on the four seconds, so r(ξ′) is false and the protection clause fails in the formula as well as in the prose.
  - O35 stays SILENT. Its occasions are not stated, and the entry supplies none (D3: no default input). It moves away (SILENT→DISAGREE) only for a reader who supplies "at all times" as its occasions. L433 s1 already carries the same risk, and the entry does not add to it.
  - N19 (O69) stays AGREE. The first draft fails the protected condition on the chapter it covers, so it is not a Repair.
  - N18 (O68) is not a Repair question and is not reached.
  - O13, O20, O25, O26, O39 and O52 turn on ProducedBy, not on P, and are not reached.
- **GAIN:** (P)'s formula and its prose say one thing.
- **LOSS:** (P)'s protection clause is now history-valued, not a comparison of two endpoints. An endpoint reading of (P) is no longer available.

### W23.2 — L445: Result and ProducesVia are defined

- **STATUS:** applied
- **GROUP:** B2
- **ITEM:** W23
- **FILE-11 LINE:** 445
- **WHERE:** Part XI, after (EK), L445. Inserted before s1, which is kept byte for byte. The display (EK) at L437–443 is not touched.
- **REASON WORD:** clarification
- **KIND:** CLAIM
- **CHECK:** check 1, SOUND. The change from file 00's "requires" to "holds when" stays recorded as a departure.
- **OLD:**
````text
The scope of \(\operatorname{Account}(c,p_c)\) is the contract fixed at \(e_c\).
````
- **NEW:**
````text
\(\operatorname{Result}(\Delta)\) is the set of contents at \(\xi'\) that \(\Delta\) prepared. \(\operatorname{ProducesVia}(\Delta,c,o;\xi,\xi')\) holds when an active route that runs from \(\Delta\) to the repair of \(o\) contains the relevant binding of \(c\). The scope of \(\operatorname{Account}(c,p_c)\) is the contract fixed at \(e_c\).
````
- **DECLARATION:** Part XI now defines Result(Δ) as the set of contents at ξ′ that Δ prepared. It defines ProducesVia(Δ,c,o;ξ,ξ′) as holding when an active route that runs from Δ to the repair of o contains the relevant binding of c.
- **REASON:**
  - Worklist W23. Result and ProducesVia each occur once in (EK), undefined.
  - Plan 1.2: "Result(Δ) as the contents at ξ′ that Δ prepared; 00:839's ProducesVia restored". "Prepared" is Build's verb (L401).
  - 00:839 reads: "ProducesVia requires the construction account of the repair to contain the relevant binding of \(c\) on its active route". File 11 has no "construction account of the repair". Its ProducedBy is an active route from Δ to the repair (L433 s4). So the restored sentence uses those words.
  - It is written as a definition ("holds when"), not as 00's necessary condition ("requires"), so that (EK) can be evaluated as the plan's gain requires. This is a departure from word-for-word restoration and is listed in conflict 3.
  - 00:800's transport clause, which interprets o and r across changed representations, was "to be considered" in the worklist. It is not taken, because no item in scope needs it.
- **CASES AT RISK:**
  - O13 stays AGREE, and more securely: "Nobody here made a repair that came from an explanation". Ana's account is in no Result of Ben's act, and no active route that ran to the repair contains its binding. L433 s5 is unchanged.
  - N10 (O61): "She created knowledge" can now be evaluated. Her explanation is in the Result of her month's work, and the route to the repair of the epistemic obligation contains its binding. "It does not exist now" is Deploy at a later ξ, which is untouched. If file 11's ruled mark is SILENT for want of these definitions, the row moves toward. See conflict 1.
  - O32 is not reached, since (EK) is not asked. O20 and O39 are not reached, since only ProducedBy is at issue there.
- **GAIN:** Every symbol of (EK) is defined, and a repair through use of an account is told apart from a repair beside one by a stated condition.
- **LOSS:** ProducesVia is now fixed by one sufficient condition. A reader who wanted 00's weaker necessary condition, with other routes left open, loses that reading.

### W6.2 — L447 s2: the normative relation is primitive 2, not a declared input

- **STATUS:** applied
- **GROUP:** B1
- **ITEM:** W6
- **FILE-11 LINE:** 447
- **WHERE:** Part XI, "Worth, and the normative relation", L447 s2.
- **REASON WORD:** erratum
- **KIND:** CLAIM
- **CHECK:** check 1, SOUND.
- **OLD:**
````text
Where a claim invokes worth, the semantics takes a **normative relation** \(\mathcal N\) as a declared input and marks the place (Part XIV).
````
- **NEW:**
````text
Where a claim invokes worth, the semantics takes the **normative relation** \(\mathcal N\) (primitive 2, Part XIV) as an input and marks the place.
````
- **DECLARATION:** Part XI now names the normative relation as primitive 2 of Part XIV, taken as an input where a claim invokes worth, and no longer calls it a declared input.
- **REASON:** Worklist W6 (XR5; 03 M42 and 03 §8 item 4). L447 calls \(\mathcal N\) "a declared input" and points to Part XIV. There, L510 makes \(\mathcal N\) primitive 2, and L514 excludes the primitives from the declared inputs. NEW is XR5's fix (plan 1.3.1) word for word. The old closing "(Part XIV)" moves into the new parenthesis, so it is not written twice.
- **CASES AT RISK:** O12 stays SILENT on the same point. O35 and O38 were touched weakly under M42; neither makes a worth claim, so neither moves. No N-case invokes worth. None other: the O-cases that 03 and 04 tie to L447 were checked, and those are O12, O35 and O38.
- **GAIN:** \(\mathcal N\) has one status in Parts 0, XI and XIV.
- **LOSS:** None.

### W6.3 — L447 s3: "declared as" becomes "taken as"

- **STATUS:** applied
- **GROUP:** B1
- **ITEM:** W6
- **FILE-11 LINE:** 447
- **WHERE:** Part XI, "Worth, and the normative relation", L447 s3, last clause.
- **REASON WORD:** erratum
- **KIND:** CLAIM
- **CHECK:** check 1, SOUND.
  - S90 cross-examination: s90_xexam_atria_B1, point 1; s90_xexam_mimo_B1, point 2 (both R39 FALLS) — FIX (two rulings, one edit), after the cross-examination. After the cross-examination (s90_xexam_atria_B1, point 1, and s90_xexam_mimo_B1, point 2; both R39 FALLS): FIX. KIND WORDING → CLAIM, declaration added; OLD and NEW unchanged. Both replies' repairs refused: folding into W6.2 (R38) would renumber the record and merge disjoint OLDs; W6.2's declaration, and Mimo's "consistent with its status as primitive 2", give R39 a content its NEW does not carry.
- **OLD:**
````text
declared as a substantive input when aesthetic value is claimed.
````
- **NEW:**
````text
taken as a substantive input when aesthetic value is claimed.
````
- **DECLARATION:** Part XI no longer calls the aesthetic normative relation a declared input: it is taken as a substantive input when aesthetic value is claimed.
- **KIND AS DRAFTED:** WORDING, given W6.2 and W6.4. With them in place, both texts send \(\mathcal N\) to the same place: an input the semantics takes and does not derive, under L514's rule for a missing input. If W6.4's clause on the normative relation is dropped, rule this entry CLAIM and declare it as: "Part XI no longer calls the aesthetic normative relation a declared input." (After the cross-examination the entry is ruled CLAIM although W6.4's clause stays, with the fuller declaration above; see CHECK.)
- **REASON:** Worklist W6 (03 §8 item 4: \(\mathcal N\) is a "declared input" at L27 and at L447). If this clause were left, it would bring back, one sentence after W6.2, the category that W6.2 removes. The skeleton scopes W6 at L447 to s2 only. This entry goes one sentence past that scope, for the same reason. It cannot be dropped: without it, s3 would still call \(\mathcal N\) declared one sentence after W6.2, W6.2's declaration would be false of Part XI, and the paragraph would pull against L510 and L514. After the cross-examination (s90_xexam_atria_B1, point 1; s90_xexam_mimo_B1, point 2) it is ruled CLAIM, with the declaration drafted above as its fallback.
- **CASES AT RISK:** None. No O-case or N-case claims aesthetic value; the case books were searched for "aesthet" and "beaut".
- **GAIN:** No sentence calls \(\mathcal N\) a declared input.
- **LOSS:** None.

### W3.4 — Declare L465, System boundary and continuity (layer 2, row L2-33)

- **STATUS:** record-only
- **GROUP:** M
- **ITEM:** W3
- **FILE-11 LINE:** 465
- **WHERE:** Part XII, System boundary and continuity, L465, the whole paragraph; file 10 has none (β and Ω only as indices, f10 L523). Record only: layer 2, row L2-33.
- **REASON WORD:** meta (record only)
- **KIND:** CLAIM (layer 2)
- **CHECK:** check 2, SOUND.
- **LOCATOR:** exact file-11 text, occurring once. It is located, not applied, and it is left out of the overlap check.
````text
**System boundary and continuity.** A capability is attributed to a system under a declared boundary (which processes and resources are the system's) and a declared continuity \(\Omega\) (what makes it the same system through change). A replaced part that preserves the declared continuity leaves the same system; a process run inside the boundary is the system's whoever wrote it; a process run outside it is not the system's however close it sits. Both are declared before the attribution, not chosen after it.
````
- **LAYER-2 ROW:** the row this entry writes into layer 2 of the record (inside W1.2's NEW).
````text
| L2-33 | Part XII, System boundary and continuity | none; compare L523 | L465 | A capability is attributed under a declared boundary and a declared continuity, both declared before the attribution and not chosen after it; a replaced part that preserves the continuity leaves the same system; a process run inside the boundary is the system's whoever wrote it, and one run outside it is not, however close it sits. File 10 had boundary and continuity only as indices. | @@REV2:L2-33@@ |
````
- **DECLARATION:** (layer 2, row L2-33) A capability is attributed under a declared boundary and a declared continuity, both declared before the attribution and not chosen after it; a replaced part that preserves the continuity leaves the same system; a process run inside the boundary is the system's whoever wrote it, and one run outside it is not, however close it sits. File 10 had boundary and continuity only as indices.
- **REASON:**
  - Worklist W3 names L419 for O41's move; 03's table adds this paragraph to the same move (M44: O41 toward). 03 M44: CLAIM (new), all five readers; not declared.
  - 04 §7.9: O41 is AGREE→AGREE by rule.
  - B2's W12.1 keeps the last sentence byte for byte and appends the rule for what declares a boundary. The row's last column reads "kept; … adds text beside it".
- **CASES AT RISK:** None through this entry: it changes no text. O41 (AGREE); O42, O30 and O51 (passage changed); O17 (weak). B2's W12.1 guards O51 and O41.
- **GAIN:** The paragraph that makes boundary and continuity declared attributions, not only indices, is declared.
- **LOSS:** None.

### W12.1 — L465: what declares a boundary, in form (a′)

- **STATUS:** applied
- **GROUP:** B2
- **ITEM:** W12 (form (a′))
- **FILE-11 LINE:** 465
- **WHERE:** Part XII, **System boundary and continuity**, L465. Inserted after the last sentence, which is kept byte for byte (03 M44).
- **REASON WORD:** clarification
- **KIND:** CLAIM
- **CHECK:** check 1, FIX. "Where no boundary is declared explicitly" could be read process by process, so that O51's module, about which its explicit boundary says nothing, would be placed inside; NEW reads "Where the system's boundary is not declared explicitly". The guard clause could be turned against O30 ("compares the pressures itself"); NEW limits it to a statement of ownership "which does not say where it runs", which still covers O17's manual.
- **OLD:**
````text
Both are declared before the attribution, not chosen after it.
````
- **NEW:**
````text
Both are declared before the attribution, not chosen after it. Where the system's boundary is not declared explicitly, a statement that names the system and says whether a process runs inside it or outside it declares the boundary for that process; a statement that the process is the system's own, which does not say where it runs, is the attribution, not its boundary.
````
- **DECLARATION:** Part XII now says two things. Where the system's boundary is not declared explicitly, a statement that names the system and says whether a process runs inside or outside it declares the boundary for that process. A statement that the process is the system's own, which does not say where it runs, is the attribution, not its boundary.
- **REASON:**
  - Worklist W12. The reading hazard is 04 §7.10: three of five readings on O30, and two of five on O17, left ownership unsettled for want of a boundary declared in words. Test (b) turned on these rows (04 §7.11).
  - Plan 1.2 takes form (a′), in 04's wording: "a boundary is stated when the situation names the system and places a process inside or outside it". D3 says it is not a default.
  - The sentence says what counts as declaring the input, and it supplies nothing where no such statement is made. L514's rule for a missing input is untouched.
  - Two guards go beyond the plan's words. Each keeps a named case, and neither adds an input.
    1. **"Where no boundary is declared explicitly."** An explicit boundary governs. Take O51: "A controller runs a diagnostic module" could be read as placing the module inside. Its explicit boundary names the controller and its routines and leaves the module out, and it is not overridden. O41's "robot-only" is kept the same way.
    2. **"A statement that the process is the system's own is the attribution, not its boundary."** Without it, the maker's manual in O17 ("the routine is the robot's own") would declare the boundary. That would contradict "keep only the manual's sentence and there is nothing". It would also bypass L465's "declared before the attribution" and L467's "owned because it can, and can because owned grounds neither".
  - "Situation", the plan's word, is not a word of the theory. It is written as "a statement".
  - The entry agrees with B1's W7.3 (skeleton conflict 8). W7.3 says that the boundary an attribution states is a declared input. This entry says what stating it consists in.
- **CASES AT RISK:**
  - O30: AGREE is secured. "The robot compares the pressures itself" says the comparison runs inside the robot. The entry closes the AGREE→SILENT reading of 04 §7.10.
  - O17: AGREE is secured. The log shows the routine "running inside the robot". The manual's sentence is an attribution, not a boundary.
  - O51 stays AGREE, because the explicit boundary governs. It moves away (AGREE→SPLIT) only for a reader who takes "runs a diagnostic module" as a placement that overrides the explicit boundary. The first clause excludes that reading.
  - O41 stays AGREE, on its explicit robot-only boundary.
  - O3, O14, O18 and O31 stay AGREE, and O21 stays SILENT on "mostly", with its "choosing is the robot's" point secured. Each says the process runs in the named system: "she starts keeping a tally", "he can order the same dishes with the book shut", "files one tooth", "corrects that one line", "the robot runs the test". Away (AGREE→SILENT) only for a reader who requires the word "boundary".
  - O40 stays AGREE and O50 stays SILENT on "mostly". The expert's proposal is stated as coming from outside.
  - O42 (continuity) and O49 (a circular definition, which is an attribution) stay AGREE.
  - N11 (O62), N15 (O65) and N21 (O71): "hers" and "formed it herself" now rest on a stated placement. If file 11's ruled mark is not AGREE, the row moves toward. See conflict 1 for O62.
  - N13 (O64): the parrot is a carrier, and the row is not reached.
- **GAIN:** "Her own" and "the robot's own" rest on stated words wherever the case says who runs the process, and no boundary is supplied where none is said.
- **LOSS:** A case that names no system, or says nothing about where a process runs, still leaves ownership unsettled, as L514 already says. The rule is also one sentence longer than the plan's words.

### W25.1 — Define the grades, Admit, Cap and Poss

- **STATUS:** applied
- **GROUP:** A
- **ITEM:** W25
- **FILE-11 LINE:** 471
- **WHERE:** Part XII, "Grades" (L471), before the inclusions.
- **REASON WORD:** erratum
- **KIND:** CLAIM
- **CHECK:** check 1, SOUND. Small points, not defects: Cap says "owned realization" where L467 says "owned retained realization" (the retention grade r carries retention), and "as owned capability requires" points to L467 without naming it.
- **OLD:**
````text
**Grades.** \(\mathsf{Cap}^{q,r}_\Omega(\xi)\subseteq\mathsf{Admit}^{q,r}_\Theta\);
````
- **NEW:**
````text
**Grades.** The accuracy grades of the physical module (Part XIV) form a directed preorder \(Q_\Theta\), increasingly demanding and short of perfection; \(q\in Q_\Theta\) is a grade of performance and \(r\in Q_\Theta\) a grade of retention. \(\mathsf{Admit}^{q,r}_\Theta\) is the set of tasks physically achievable at grades \((q,r)\); \(\mathsf{Cap}^{q,r}_\Omega(\xi)\) is the set of tasks with an owned realization, or an owned construction of one, at those grades, as owned capability requires; and \(\mathsf{Poss}_\Theta=\bigcap_{q,r}\mathsf{Admit}^{q,r}_\Theta\) is the set of tasks achievable at every grade, which is what possibility means under Tasks. Then \(\mathsf{Cap}^{q,r}_\Omega(\xi)\subseteq\mathsf{Admit}^{q,r}_\Theta\);
````
- **DECLARATION:** Part XII now defines the grades \(q,r\), \(\mathsf{Admit}^{q,r}_\Theta\), \(\mathsf{Cap}^{q,r}_\Omega\) and \(\mathsf{Poss}_\Theta\) that (CT3) and (CT4) relate, with \(\mathsf{Poss}_\Theta\) the tasks achievable at every grade.
- **REASON:** W25 (trial M8, VALID in part, and §4, "found by no reader"). Restores 00:1015 (Admit, Cap) and 00:1154 (the grades \(Q_\Theta\)), one clause each. Poss is given as \(\bigcap_{q,r}\mathsf{Admit}^{q,r}_\Theta\), which is 00:1164's (CT4) once Admit is defined; file 11 has neither Approx nor PhysicallyConstructible to state (CT4) in 00's form. "Accuracy grades" is already listed in the physical module at L509; "possibility" is L453's. Cap's "owned realization, or an owned construction of one" is L467's owned capability, so (CT3) stays a result (forget ownership), not a definition.
- **CASES AT RISK:** None among O1–O52. Checked: O49 (Cap rests on ownership, which rests on the boundary, so no circle is added), O42. N24: toward (the universality claims become evaluable at a grade).
- **GAIN / LOSS:** GAIN: Part XII's inclusions can be read and checked. LOSS: The paragraph grows from two sentences to four.

### W17.2 — L473 s1: the population is of realizable transports

- **STATUS:** applied
- **GROUP:** B2
- **ITEM:** W17
- **FILE-11 LINE:** 473
- **WHERE:** Part XII, "Selection in the physical module", L473 s1. The last sentence (03 M46) is kept byte for byte and becomes the single wording of membership.
- **REASON WORD:** clarification
- **KIND:** CLAIM
- **CHECK:** check 1, FIX. "Realizable" alone suggests physics alone, the reading under which O48's wired arrangement is a member. NEW uses L197's word, "candidate", and the paragraph's last sentence stays the one wording of membership.
  - S90 cross-examination: s90_xexam_atria_B2, pass 2, point 1 (R42 STANDS, naming moves toward) — KEEP, after the cross-examination. After the cross-examination (S90, part B2): Atria's reply (pass 2) gave STANDS and named moves on O24 and N5, both toward and both declared; kept. The reply's O24 quotation "reachable by hand" is said of the setting, not the arrangement; on the texts O24 stays AGREE, and the change closes the "realized" reading that 03 watched for harm. Mimo's reply gave STANDS and did not contest it.
- **OLD:**
````text
a population of realized transports
````
- **NEW:**
````text
a population of candidate transports
````
- **DECLARATION:** Part XII now describes the population of a selection history as candidate transports, as Part IV does, not realized ones. The population is the set its own last sentence gives: the transports the physics and the stated construction admit.
- **REASON:**
  - Worklist W17, with 03 §8 item 1: "L473 has 'realized' and 'admit'; L562 has 'admitted, realizable, a member of \(\mathcal T\)'" (M46, M54). Plan 1.2 asks for "one wording of population membership at L473 and L562".
  - L473 s1 calls the population "realized transports". Its last sentence defines it as "the set of transports the physics and the stated construction admit". An admitted transport need not have been realized.
  - Derivation 3 needs members that were never realized. Its proof (L564) says "Where \(\mathcal T\) contains a transport with \(L_j(a,b)\) altered". Its consequence (L566) says "wherever its population admits an alternative".
  - One word makes s1 agree with the last sentence. W17.3 then cites that sentence at L562.
  - The sentence is shared with file 10 (f10 L482). Layer 1 of the record shows the change.
- **CASES AT RISK:**
  - O48 stays AGREE. It moves away (AGREE→SPLIT) only for a reader who takes "realizable" as "physically possible" alone and ignores the unchanged last sentence. That sentence says the population is what "the physics and the stated construction admit", and that "a transport that would need a part every member of the population is built without is not in it".
  - O24 stays AGREE. The second arrangement need not have been realized to be a member.
  - N5 (O57) stays AGREE, or moves toward it. A reader who takes file 11's "realized" at its word finds no realized second reading of the village rule. There is then no differing survivor, and the rule fixes the value in the new land, against the verdict. Under the new word, both readings are members and both survive the home history. See conflict 1: the plan's P2(d) predicts no change on O57.
  - D3-T: both designs were realized, so it is unaffected.
  - O11 is not reached.
- **GAIN:** Parts IV, XII and XVI give one notion of population membership, and the tension 03 §8 item 1 records is closed.
- **LOSS:** A selection claim is no longer described as being about realized alternatives only. A reader who took it that way loses that reading.

### W25.2 — Define Enable in the Barriers paragraph's terms

- **STATUS:** applied
- **GROUP:** A
- **ITEM:** W25
- **FILE-11 LINE:** 487
- **WHERE:** Part XIII, "Barriers" (L487), a new last sentence; (U1) and (U2) at L491–495 are unchanged.
- **REASON WORD:** erratum
- **KIND:** CLAIM
- **CHECK:** check 1, SOUND. A's finding C3 stands: U_c and A_p in (U1)–(U2) are still undefined; that is a separate CLAIM at L489, outside the item.
- **OLD:**
````text
A finite list of failures is not a barrier proof; a bypass refutes a proposed barrier.
````
- **NEW:**
````text
A finite list of failures is not a barrier proof; a bypass refutes a proposed barrier. \(\operatorname{Enable}(s,T,\chi)\) holds when \(\chi\) is an admitted, non-question-begging enabling condition for \(s\) and the task \(T\).
````
- **DECLARATION:** Part XIII now defines Enable in (U1) and (U2): it holds when \(\chi\) is an admitted, non-question-begging enabling condition for the system and the task.
- **REASON:** W25 (trial M8; Enable is undefined in file 00 too, 00:1113, 1124). The definition uses only the Barriers sentence's own words and L455's "enabling conditions \(\chi\)", so no new term enters. It must match W45's pointer to "barriers in Part XIII's sense" at L77 (group C; skeleton conflict 14): it does, since the barrier sentence is unchanged.
- **CASES AT RISK:** N24: toward (joining the two sorts of matter is not an admitted enabling condition, so no \(\chi\) makes the pair one universal constructor). No O-case uses (U1)–(U3); checked O49.
- **GAIN / LOSS:** GAIN: (U1) and (U2) have no undefined predicate. LOSS: Nothing.

### W7.2 — L512 s1: the same, in Part XIV

- **STATUS:** applied
- **GROUP:** B1
- **ITEM:** W7
- **FILE-11 LINE:** 512
- **WHERE:** Part XIV, the paragraph after the primitives, L512 s1.
- **REASON WORD:** erratum
- **KIND:** CLAIM
- **CHECK:** check 1, SOUND.
- **OLD:**
````text
Everything else is derived. Roles, from admitted edits (Part II).
````
- **NEW:**
````text
Everything else is derived from the two primitives, the declared indices and the declared inputs (below). Roles, from admitted edits (Part II).
````
- **DECLARATION:** Part XIV now says that everything else is derived from the two primitives, the declared indices and the declared inputs, where it said only that everything else is derived.
- **REASON:** Worklist W7. This is the same tension as W7.1 (03 §8 item 2) and uses the same plan wording. "(below)" follows file 11's own use at L149, and it points to L514 and L516.
- **CASES AT RISK:** None; no case cites L512. This was checked against 03's table (M47 touches O12 only, and that is at L510).
- **GAIN:** Part XIV's own summary agrees with its Declared inputs paragraph.
- **LOSS:** None.

### W6.4 + W14.1 — L514: the declared inputs, the normative relation, and the measures not supplied

- **STATUS:** applied
- **GROUP:** B1
- **ITEM:** W6, W14 (weak form)
- **FILE-11 LINE:** 514
- **WHERE:** Part XIV, "Declared inputs", L514 (the whole paragraph, one line).
- **REASON WORD:** erratum and clarification
- **KIND:** CLAIM
- **CHECK:** check 1, SOUND.
- **OLD:**
````text
**Declared inputs.** Besides the two primitives, some claims take stated inputs that the semantics records and does not supply: the obligations \(O\) and \(P\) of a repair, with the occasions each covers (Part XI); the scope of a contract and what makes a restriction appropriate (Part III); the system boundary and continuity of an attribution (Part XII). A verdict that depends on one of these is a verdict given the input; where the input is missing, the verdict is unsettled and the semantics says so rather than choosing the input from the verdict wanted.
````
- **NEW:**
````text
**Declared inputs.** Besides the two primitives, some claims take stated inputs that the semantics records and does not supply: the obligations \(O\) and \(P\) of a repair, with the occasions each covers (Part XI); the scope of a contract and what makes a restriction appropriate (Part III); the system boundary and continuity of an attribution (Part XII); a weighting of credit among several contributions to one achievement, beyond any division of credit its history contains (Part XI). A verdict that depends on one of these, or on the normative relation where a claim invokes worth, is a verdict given the input; where the input is missing, the verdict is unsettled and the semantics says so rather than choosing the input from the verdict wanted. The semantics supplies no probability of truth, no merit function and no ranking of thinkers, and a claim that needs one is unsettled.
````
- **DECLARATION:** Part XIV now does three things. It lists among the declared inputs a weighting of credit among several contributions to one achievement, beyond any division its history contains. It applies its rule for a missing input to the normative relation where a claim invokes worth. And it says that a claim needing a probability of truth, a merit function or a ranking of thinkers is unsettled.
- **REASON:** The entry carries two items.
  - **W6.** XR3's "(Part XIV)" is made true of the three measures. The rule for a missing input is extended to \(\mathcal N\), as the worklist's handling of W6 proposes ("for a claim of worth, the normative relation (primitive 2), under the same rule"), so that O12's SILENT has a stated rule (det 01 SILENT table; 04 §7.8: "\(\mathcal N\) … not named in L514"). "Besides the two primitives" is kept (plan 1.2).
  - **W14, weak form only** (D3; plan 1.2 and conflict 2): "a weighting of several contributions to one achievement is a declared input the semantics does not supply, and a claim that needs one is unsettled. No premise that credit goes with the originative act." The evidence is 04 §7.8 (L514 names no input for O21, O27 or O50) and 04 §7.9 (the step to "mostly X's" "needs a premise that credit goes with the originative part, and neither file states it"). 07 re-read O50 on the same weighting.
  - **Two limits on the wording**, both in file 11's own words.
    - "Beyond any division of credit its history contains" takes its limit from L27 s3 ("beyond what a history establishes") and L433 s4 ("the history supplies no division of credit that it does not contain"). A division the history records is therefore not an input.
    - "Weighting of credit" ties the input to Part XI's credit. It does not reach the explanatory work of an explanation's parts.
  - **What is kept.** The rule sentence, with "rather than choosing the input from the verdict wanted", is kept word for word apart from the inserted clause, so no default input is added (D3; conflict 6). L27 s3 and L433 s4 are not touched (conflict 7).
- **CASES AT RISK:**
  - O21, O27 and O50 stay SILENT, now on a named input. They move toward AGREE only if a reader counts "who did the decisive step" as a division of credit that the history contains. The entry adds no premise that credit goes with the originative act. That would be a change toward the thoughtful person against P1.
  - O40 stays AGREE. "Neither can say 'mostly'" holds because a claim that needs the missing weighting is unsettled (04 §2.2). The risk of AGREE→SILENT is as for W6.1.
  - O26 stays AGREE: "the meters on each feed show which half each stopped" is a division of credit the history contains. It moves AGREE→SILENT (away) if the clause "beyond any division of credit its history contains" is dropped. The clause is there for this row.
  - O44 stays AGREE. "Most of the copy depends on the source … the record says which part is which" is a division the record contains, and it concerns dependence, not credit.
  - O20 and O39 stay AGREE: two sufficient acts, no division, and L433 s4 decides. O32 stays AGREE: two contents, each credited to the one who found it.
  - O12 stays SILENT, now under the rule by its words. O8 and O6 are watched, as in W6.1.
  - O1, O5, O17, O30, O35, O41 and O51, and weakly O3, O14, O18 and O31: the list items they rest on are unchanged, so no move is expected.
  - N-cases:
    - N23 (O73) is watched. "Most of the work is done by the laws" is explanatory work, not credit, and "weighting of credit" keeps it out. A reader who takes it as a weighting would give a change away on that bullet.
    - N11 is watched as in W6.1.
    - N14 is set aside (D8).
    - No other N-case asserts a weighting of credit; the case books were searched for "mostly", "most of" and "share".
- **GAIN:** The SILENT rows on "mostly" and on worth rest on stated words. L27's pointers to Part XIV become true, and Part XIV still supplies no input.
- **LOSS:** None of those rows can reach AGREE unless the case states a weighting or \(\mathcal N\). A reader who wanted "mostly" derived from the originative act has no route to it.

### W7.3 — L516: an index is not a declared input, and where the two meet

- **STATUS:** applied
- **GROUP:** B1
- **ITEM:** W7
- **FILE-11 LINE:** 516
- **WHERE:** Part XIV, "Indices, not primitives", L516. Two sentences are appended.
- **REASON WORD:** erratum
- **KIND:** CLAIM
- **CHECK:** check 1, FIX. "A declared input is a stated value" mistyped two of L514's inputs (the obligations are conditions over occasions, and a ground is not a value), and "the boundary and continuity an attribution states" could be read against W12.1. NEW reads "something a claim takes as stated" and uses L514's own "the boundary and continuity of an attribution".
- **OLD:**
````text
**Indices, not primitives.** Grain \(\ell\), boundary \(\beta\), continuity \(\Omega\), and the contract \(C\) are declared indices. Every claim is relative to them; none is a predicate that could be true or false.
````
- **NEW:**
````text
**Indices, not primitives.** Grain \(\ell\), boundary \(\beta\), continuity \(\Omega\), and the contract \(C\) are declared indices. Every claim is relative to them; none is a predicate that could be true or false. An index is what a claim is relative to; a declared input is something a claim takes as stated, which the semantics records and does not supply. The boundary and continuity of an attribution, and the scope a claim states for its contract, are values of indices and are declared inputs (above).
````
- **DECLARATION:** Part XIV now separates an index, which is what a claim is relative to, from a declared input, which is something a claim takes as stated and the semantics records and does not supply. It says that the boundary and continuity of an attribution, and the scope a claim states for its contract, are both.
- **REASON:**
  - Worklist W7 (det 02 C66). 03 §8 item 3: boundary, continuity and the contract are "declared indices" at L33 and L516, and they are declared inputs at L514. The plan asks for "one sentence [that] separates indices from declared inputs". Here it is two short sentences, one for the distinction and one for where the two meet.
  - The worklist's wording named "the indices' values" in general. Grain is left out on purpose. L514 does not list grain. Making a stated grain a declared input would give every case that leaves its grain to its question a missing-input reading that no case has earned.
  - The wording matches L514's own list: "the system boundary and continuity of an attribution" and "the scope of a contract".
- **CASES AT RISK:**
  - The boundary rows: O17 and O30; weakly O3, O14, O18, O21, O31, O41 and O51; and N11, N13, N15 and N21. The sentence repeats what L514 already lists, so no mark should move. It does restate the ground of 04 §7.10's boundary hazard: readers who left ownership unsettled for want of a boundary "declared in words". If a mark moved, it would be AGREE→SILENT (away). The fix for that hazard is W12(a′), in group B2 (conflict 8).
  - The scope rows O1, O5 and O8 rest on L514's unchanged item, so no move is expected.
  - The grain rows O7, O10 and O43 are not reached, because grain is not made an input.
- **GAIN:** L33, L514 and L516 no longer give boundary, continuity and the contract two statuses that read as incompatible.
- **LOSS:** Grain's status as a value stays implicit.

### W7.4 — L518 s1: the indices and the inputs in the dependence order

- **STATUS:** applied
- **GROUP:** B1
- **ITEM:** W7
- **FILE-11 LINE:** 518
- **WHERE:** Part XIV, "Dependence order", L518 s1.
- **REASON WORD:** erratum
- **KIND:** CLAIM
- **CHECK:** check 1, SOUND.
- **OLD:**
````text
**Dependence order.** (O) and (Q) depend on nothing.
````
- **NEW:**
````text
**Dependence order.** (O) and (Q) depend on nothing; nor do the declared indices and the declared inputs, which are stated, not derived.
````
- **DECLARATION:** Part XIV's dependence order now says that the declared indices and the declared inputs depend on nothing in the semantics, because they are stated, not derived.
- **REASON:** Worklist W7 (XR6: "the order at L518 lists no declared input"; 03 §5 and 03 §8 item 5; plan 1.3.1 XR6). Derivation 6's claim (L586) bases every predicate on the primitives "together with declared indices and declared inputs". The order its proof cites now names both as bases.
- **CASES AT RISK:** None. O37 and O49 turn on L518's last sentence, which is unchanged (M49, declared by W3 in layer 2). This was checked.
- **GAIN:** The order names every base that Derivation 6's claim names.
- **LOSS:** None.

### W7.5 — L518 s9–s11: Ownership, owned capability, ProducedBy and the obligations

- **STATUS:** applied
- **GROUP:** B1
- **ITEM:** W7
- **FILE-11 LINE:** 518
- **WHERE:** Part XIV, "Dependence order", L518, the sentences on Build, (N) and (G), and (P) and (EK).
- **REASON WORD:** erratum
- **KIND:** CLAIM
- **CHECK:** check 1, SOUND. The order still omits Result, ProducesVia, Cap and Enable (B1 finding 9).
  - S90 cross-examination: s90_xexam_mimo_B1, point 3 (R48 STANDS, naming an undeclared change of claim on one reading) — FIX, after the cross-examination. After the cross-examination (Mimo B1, point 3): FIX, '(EK) also on (P)' added; the over-statement for (P) kept.
- **OLD:**
````text
Build depends on histories and (E). (N), (G) depend on Deploy and Build. (P), (EK) depend on (G), (E), Deploy.
````
- **NEW:**
````text
Ownership depends on histories and a declared boundary, and owned capability on Ownership, (CT1) and a declared continuity (Part XII). Build depends on histories, Ownership and (E). (N), (G) depend on Deploy and Build. (P), (EK) depend on (G), (E), Deploy; (P) also on ProducedBy and on the declared obligations with their occasions, (EK) also on (P), and ProducedBy on histories and their active routes.
````
- **DECLARATION:** Part XIV's dependence order now places Ownership on histories and a declared boundary, owned capability on Ownership, (CT1) and a declared continuity, Build on Ownership, (P) on ProducedBy and the declared obligations with their occasions, (EK) on (P), and ProducedBy on histories and their active routes.
- **REASON:**
  - Worklist W7 (XR6: the order lists "none of the definitions that rest on one (L419, L433, L465)"; 03 §5; plan 1.3.1).
    - Ownership (L419) rests on the declared boundary.
    - Owned capability (L467) rests on Ownership and on the continuity and resource contract.
    - ProducedBy (L433 s4) rests on active routes read from histories (L371).
    - (P) rests on \(O\) and \(P\) with their occasions (L433 s1).
    - Build (L401) is defined on an owned subhistory.
  - **Left free for W20.** Two sentences are left untouched: "(E) depends on those." and "(S), (B), (D) depend on (E)." W20's held rider can be entered at either one later, through B1, without overlapping any entry here (skeleton conflict 3).
  - **Kept.** L518's last two sentences are kept word for word: M49, declared against file 10 by W3.
  - **Not corrected.** "(P), (EK) depend on (G), (E), Deploy" is kept, although (P)'s definition does not use (G), (E) or Deploy. As a dependence it is an over-statement and does not harm well-foundedness. Correcting it lies outside W7. Kept after the cross-examination: only (G) is plainly idle for (P), and (E) and Deploy carry (P)'s route to (R) through active routes and epistemic obligations.
  - **After the cross-examination (S90, Mimo B1, point 3).** (EK) uses Repair_{O,P} and the obligations O_ep ⊆ O (L440–443). As drafted, the order gave (P) its bases in ProducedBy and the declared obligations and left (EK), in the same sentence, with no route to them. Derivation 6's proof as W7.6 words it follows each definition to the declared inputs through this order. The clause states a dependence (EK)'s definition already has. It moves no case, touches neither W20's two free sentences nor the last sentence, and creates no circle (Mimo, s90_xexam_mimo_B1, point 3).
- **CASES AT RISK:**
  - O49 stays AGREE. The order now puts Ownership before owned capability, which the verdict ("The definition goes in a circle") needs. This secures the mark and moves nothing.
  - O37 stays AGREE. Its circle is ruled by L518's last sentence, which is unchanged.
  - O35 and O38: the obligations with their occasions are L514's unchanged input.
  - The boundary rows are as in W7.3: restated, not changed.
  - No N-case cites the dependence order. This was checked.
- **GAIN:** Derivation 6's proof has an order that reaches the declared inputs and the definitions that rest on them. (EK) reaches the declared obligations through (P).
- **LOSS:** None; the order grows by two sentences.

### W3.2 — Declare L518's last sentence, the well-founded order (layer 2, row L2-38)

- **STATUS:** record-only
- **GROUP:** M
- **ITEM:** W3
- **FILE-11 LINE:** 518
- **WHERE:** Part XIV, Dependence order, L518, last sentence; file 10 L525. Record only: layer 2, row L2-38.
- **REASON WORD:** meta (record only)
- **KIND:** CLAIM (layer 2)
- **CHECK:** check 2, SOUND.
- **LOCATOR:** exact file-11 text, occurring once. It is located, not applied, and it is left out of the overlap check.
````text
The order is well founded: a representation justified only by its own construction, or an ownership and a capability justified only by each other, has not supplied its place in it, and a separate proof that would supply it counts only when the account uses it.
````
- **LAYER-2 ROW:** the row this entry writes into layer 2 of the record (inside W1.2's NEW).
````text
| L2-38 | Part XIV, Dependence order | L525 | L518, last sentence | The dependence order is well founded: a representation justified only by its own construction, or an ownership and a capability justified only by each other, has not supplied its place in it, and a separate proof that would supply that place counts only when the account uses it. | @@REV2:L2-38@@ |
````
- **DECLARATION:** (layer 2, row L2-38) The dependence order is well founded: a representation justified only by its own construction, or an ownership and a capability justified only by each other, has not supplied its place in it, and a separate proof that would supply that place counts only when the account uses it.
- **REASON:**
  - Worklist W3: O37 moved SPLIT→AGREE on det 01 through this sentence. 03 M49: CLAIM (new), all five readers; not declared.
  - 04 §7.9: O37 is AGREE→AGREE under the rule. So this is not a changed verdict, and it is to be declared only (plan 1.2 W3).
  - B1 keeps the sentence word for word (W7.4, W7.5), and leaves the order's middle sentences free for W20's held rider (skeleton conflict 3).
- **CASES AT RISK:** None through this entry: it changes no text. O37 keeps AGREE; O49 and O17 keep AGREE. B1's W7.5 checks them against the fuller order.
- **GAIN:** The well-foundedness clause, which the order itself did not list, is declared.
- **LOSS:** None.

### W15.1 — L526: the new Part XV sentence

- **STATUS:** applied
- **GROUP:** B1
- **ITEM:** W15
- **FILE-11 LINE:** 526
- **WHERE:** Part XV, the opening paragraph, L526. One sentence is appended after s2.
- **REASON WORD:** clarification
- **KIND:** CLAIM
- **CHECK:** check 1, SOUND.
- **OLD:**
````text
None is protected by notation, by the availability of this document, or by any version label.
````
- **NEW:**
````text
None is protected by notation, by the availability of this document, or by any version label. A case whose verdict turns on an input the case does not state, where the input is one of the declared inputs Part XIV lists or the normative relation, is a case with a missing input, not a refutation.
````
- **DECLARATION:** Part XV now says that a case whose verdict turns on an unstated declared input of Part XIV, or on an unstated normative relation, is a case with a missing input, not a refutation.
- **REASON:**
  - Worklist W15. The sentence follows the pattern of 12:554, which is the only thing D5 takes from file 12: "A case whose verdict turns on a contrast the statement omits is a case with a missing declared input, not a refutation." The rows it serves are det 01's SILENT table: O1, O12, O35 and O50.
  - It is limited to Part XIV's list and to \(\mathcal N\), as plan 1.2 requires, so that nothing outside the list can be called an input to shelter a claim. After W6.4, the list includes the weighting of credit. The three measures that are "not supplied" are not inputs, so they are not covered.
  - It is placed in Part XV's opening paragraph so that it governs every attack. B1 owns L526 (skeleton, section 1).
- **CASES AT RISK:**
  - O1, O12, O35 and O50 stay SILENT. The sentence says that these are not defeats. No verdict passage rests on Part XV's opening.
  - O21 and O27 are the same, since the weighting is on the list after W6.4.
  - O48 rests on L534, which is untouched.
  - No AGREE row cites L526.
  - No N-case turns on it.
  - This was checked.
- **GAIN:** SILENT rows for a missing listed input are not read as refutations.
- **LOSS:** The attacks narrow. A case that shows a verdict hanging on an unstated ground of appropriateness, boundary, occasion, weighting or worth, as O1 does, can be offered only as a missing input, no longer as a refutation.

### W11.2 — L528 s3: the encoding table stays inside the sufficiency attack

- **STATUS:** applied
- **GROUP:** B1
- **ITEM:** W11
- **FILE-11 LINE:** 528
- **WHERE:** Part XV, "(A) Sufficiency", L528 s3.
- **REASON WORD:** clarification
- **KIND:** CLAIM
- **CHECK:** check 1, SOUND.
- **OLD:**
````text
A table that encodes the response to every admitted change fails none and is an account, so it is not a counterexample; a new attempt must fail none and still explain nothing.
````
- **NEW:**
````text
A table that encodes the response to every admitted change does not fail (F1); like any new attempt, it is a counterexample only if it fails none of the four and still explains nothing.
````
- **DECLARATION:** Part XV no longer sets the encoding table outside the sufficiency attack: like any candidate, it refutes sufficiency if it meets all four conditions of (E) and still explains nothing.
- **REASON:**
  - Worklist W11 (03 M50; det 02 C70). L528 s3 drops the encoding table from what could refute sufficiency, on the strength of L271's unchecked "is an account". With W11.1, the table is an account only when it meets the rest of (E). So the sufficiency attack stays honestly open to an encoding table that meets all four conditions and still explains nothing, as the worklist's "Gained" line asks.
  - The pointer "(A) Sufficiency" and its label are kept (D9).
  - S70's fix is kept: Part 0's short form of attack (A) (L63) names no table.
- **CASES AT RISK:** O2 and O33 stay AGREE, as for W11.1, and no case turns on Part XV's attack (A). N17 is watched, as for W11.1. This was checked.
- **GAIN:** Part XV no longer shelters a candidate class from its own sufficiency attack.
- **LOSS:** The lookup-table question is open again in Part XV, now as a live attack and not as a closed one.

### W19.2 — Derivation 2: "Same anchors, one account"

- **STATUS:** applied
- **GROUP:** A
- **ITEM:** W19
- **FILE-11 LINE:** 552–558
- **WHERE:** Part XVI, Derivation 2 (L552–558), the whole derivation from its heading "## 2. Indistinguishable is identical" through its Consequence. The heading, claim, proof and Consequence are replaced, and one paragraph is added between the proof and the Consequence. The blank L559 and Derivation 3 (L560 on) are untouched.
- **REASON WORD:** change of claim
- **KIND:** CLAIM
- **CHECK:** as W19.1. The text is the settled wording (F1, block 1), copied byte for byte.
  - S90 cross-examination: s90_xexam_mimo_A2, point 3 and task (d); s90_xexam_atria_A2, point 2 (all R51 STANDS) — KEEP (three rulings, reconciled), after the cross-examination. After the cross-examination (S90, Mimo A2, point 3, R51 STANDS): the reply's claim that the declaration understates an added claim ('different candidates with one answer profile') and the loss of the old Consequence's general principle was re-examined and ruled KEEP. 'Different candidates' is file 11's own premise, 'one answer profile' is (i), the paragraph's pointers restate unchanged L23, L307 and Derivations 8–9, and the narrowing of the Consequence is stated in the declaration's last sentence and in LOSS.
    After the cross-examination (S90, task (d): Mimo A2 on O24, O46, N17 and N25, and Atria A2, point 2, on O24, O36 and O46; both R51 STANDS): the moved verdicts both replies name were re-examined and ruled KEEP. Every move named is toward the fixed verdict, and both replies grant that the declaration accounts for it. On the S81 reading file 11 was already AGREE on O24, O36 and O46, so no mark moves; what goes is file 11's "one account … pairwise of one kind", which pulled against them, and the declaration's first sentence and its "without that premise nothing more follows" state that withdrawal. The verdicts rest on text W19.2 leaves unchanged: L23, Derivation 9 and L307's reassigned-component clause (O46), L299 as W58(i).1 words it (O36), and Derivation 3 (W17.3) with L257 s2 (O24), whose old support in file 11's general Consequence is narrowed as the declaration's last sentence says. "Different candidates" in L560 holds by Part V's definition of a candidate, and "one answer profile" is (i). No case moves away: N17 moves toward on its first two questions or not at all, and N25's second question holds on either reading.
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
- **DECLARATION:** Derivation 2 no longer says that two candidates for one question that satisfy (F1), (F2) and (A) on C are one account whose components are pairwise of one kind. It now says that their answer profiles coincide on C; that where a bijection of their active components gives each pair one anchor, the same subnetwork of D with port translations onto the same ports of D, each pair is of one kind on C and, so far as (F1), (F2) and (A) reach, the two are one account; and that without that premise nothing more follows. Its Consequence now covers only candidates that differ in which component carries which anchor.
- **REASON:**
  - **W19** (S88 finding F1, settled UPHELD). Both readings rule UPHELD: Atria's reading from the frozen position, and the reading of Mimo's reply from the position after Atria's reading. The component half of the claim is false under its stated assumptions, on two counter-instances checked in exact arithmetic for every real \(c\) (`results/S88 Mimo reading parts/checks/f1_check.py`). The answer-profile half follows from (A). The proof, "Immediate from Derivation 1 and (A)", omits the pairing step: Derivation 1 relates each component only to its own anchor.
  - **Plan 1.3.3's rule**, fixed before any S88 reply was read: "F1 UPHELD: take (i)". Wording (i), "Same anchors, one account", is taken as settled.
  - **Changes since the position after Atria's reading**, all in the settled wording:
    - Clause (ii) says what "one account" is. File 11 gave the phrase content only through the colon at L554, and the repair had dropped it (Mimo's F1 point 4; the F1 reading's change A).
    - The Consequence says "candidates that satisfy (F1), (F2) and (A)" in place of "faithful candidates", because L191 defines "faithful" by (F1) and (F2) only, and the claim's premise includes (A) (the F1 reader's own note).
    - The sentence after (K) (W19.1) and Derivation 10's sentence (W19.3) change with it.
  - **The premise of (ii)** is "port translations onto the same ports of \(D\)". The premise as sent to both outside readers ("\(\lambda'(\varphi(k))=\lambda(k)\) … up to port translation") is false on the F1 reader's \(E_3\), \(E_4\), which are the Atria reading's P and Q: two components anchored to one subnetwork on different ports. Mimo endorsed the premise as sent; that bears only on wording since tightened. Under the current premise the proof holds, with the footprint bijection \(\rho'^{-1}\circ\rho\).
  - **"The same subnetwork", not "anchors of one kind"** (plan 1.3.3). The weaker premise would make O45's two springs, and O46's spring and cable, one account, against Part VI's redundant routes and L309 s3.
  - **Not adopted:** the smaller wording (ii). It fails on \(E_3\), \(E_4\).
  - **Read in place.**
    - The heading keeps file 11's "## n. Title" form, so the program still names the place "Derivation 2".
    - The primes (\(E'\), \(\tau'\), \(\sigma'\)) name the second candidate's parts, as \(\mathcal E'\) does, and "active components" is (F1)'s phrase (L235).
    - The added paragraph cites Derivation 9, Part VI's redundant routes and Derivation 8, and each says what the paragraph uses.
    - Part XV's "Derivations 1–3 under their stated assumptions" (L538) now lists a result that holds. Part 0 (L13, L41) says that components no admitted change separates are one kind at a level; that stands. No line of file 11 cites the old title or its slogan. The only other citation of Derivation 2 is L620 (W19.3).
  - **Skeleton conflict 12, rechecked.** W21.1 defines \(\equiv_\ell\) by faithful transports both ways, with no pairing of components across candidates, so it stands as drafted. O11, O18 and N15 keep W21.1's readings.
- **CASES AT RISK:**
  - **O46 (the decisive guard) holds AGREE, on firmer text.** The cable is anchored to a different subnetwork from the spring, so the premise of (ii) fails and "nothing more follows": they are different candidates with one answer profile. File 11's slogan let a reader call the spring account and the cable account one account, since both are faithful with one answer profile, and so call the spring account a survivor. That reading is gone. L309 s3's second clause is unchanged.
  - **O45 holds AGREE.** The two springs anchor different subnetworks, so (ii) makes them neither one kind nor one account. The added paragraph points to Part VI's redundant routes, which carry the verdict with L309 s3 and W28.1.
  - **O36 holds AGREE.** The unwritten route with another premise cuts \(D\) at a different place, so it is a different candidate, and P stays critical in each route as written. Atria (S90, part A2) reads this as a move toward: file 11's "one account … pairwise of one kind" could have merged the written candidate with the unwritten one. The move is the declared withdrawal, and no mark moves (S81 read file 11 AGREE, on L301).
  - **O24 holds AGREE, toward if anything.** The two wiring arrangements are different organizations (L25). File 11's Consequence ("Underdetermination of an account by a contract is not a failure of the semantics to decide …") could be read to make two arrangements that agree on every tested pair one account. The new Consequence covers only anchor assignments. The verdict rests on Derivation 3 (L562; W17.3), which is untouched.
  - **O10 holds** (see W19.1).
  - **N17 (O67): toward on the first two questions; the plan predicts no mark.** Answers A and B cut \(D\) at different places, the electrons against the stored factors. The added paragraph makes them different candidates with one answer profile, so each can tell the asker something the other does not. File 11's "one account … their components are pairwise of one kind" pulled against that. The third question ("B explains, and A does so only in a thin sense") is not reached.
  - **N25 (O75).** The first question holds; it rests on non-circular dependence (W20.2). The second question is watched. Mimo (S90, part A2, task (d)) reads it as a move toward; after the cross-examination it holds on either reading, and "watched" stays.
    - "The difference between them is idle" can rest on (ii) and the Consequence, where the dog and the turtle are read as components with one anchor on the same ports.
    - A reader who rested it on file 11's slogan, which goes, may leave it unsettled (away, AGREE→SILENT).
    - W30.1's "whatever the difference is called" and the Consequence's "a claim that one assignment is 'really' right … must supply it" hold it.
  - **O11, O18 and N15** (skeleton conflict 12) are unchanged.
  - The two case books were searched for rows that compare the components of two candidates. No other row turns on Derivation 2.
- **GAIN:** Part XVI no longer carries a derivation that is false under its stated assumptions. Part XV's list of results open to a counterexample now lists a true one. "One account" has stated content.
- **LOSS:** The slogan "indistinguishable is identical" goes. The Consequence reaches only anchor assignments. Whether two differently decomposed candidates are one account is left undefined.

### W17.3 — L562 s3: Derivation 3's condition in the two defined terms

- **STATUS:** applied
- **GROUP:** B2
- **ITEM:** W17
- **FILE-11 LINE:** 562
- **WHERE:** Part XVI, Derivation 3, **Claim**, L562 s3, from "it must be" to the end.
- **REASON WORD:** clarification
- **KIND:** CLAIM
- **CHECK:** check 1, SOUND. CLAIM is defensible; a checker may rule it WORDING, given W17.1 and L473.
  - S90 cross-examination: s90_xexam_mimo_B2, point 2 (R52 STANDS, saying the change is under-declared) — KEEP, after the cross-examination. After the cross-examination (S90, Mimo B2, point 2, R52 STANDS): the claim that the declaration does not say whether "realizable" is dropped was re-examined and ruled KEEP. "Realizable" is entailed by membership in both texts: file 11's population is of realized transports (L473 s1), and the revised text's population is what the physics and the stated construction admit (L475), which is physical possibility in Part XII's sense (Tasks) together with the construction. No condition of Derivation 3 is lost, and the declaration shows both lists. The reply's suggested addition ("the separate realizability condition is dropped") is not taken, because it would declare a weakening the new text does not make. (CT1) is typed on protocols and tasks, not on population members, and the realized-only reading belongs to W17.2, which declares it.
- **OLD:**
````text
it must be admitted, realizable, a member of \(\mathcal T\), and a survivor of \(H\).
````
- **NEW:**
````text
it must be a member of \(\mathcal T\), a transport the physics and the stated construction admit (Part XII), and it must survive on \(H\) (Part IV).
````
- **DECLARATION:** Derivation 3's claim now requires the differing transport to be a member of the population, a transport the physics and the stated construction admit, that survives on H. This replaces the list "admitted, realizable, a member of the population, and a survivor of H".
- **REASON:**
  - Worklist W17; 03 §8 item 1 (M54).
  - The old sentence lists four conditions. Two of them, "admitted" and "realizable", are what L473 says membership is. "A survivor of H" was the ambiguous phrase that W17.1 now defines.
  - The new text states the condition through the two defined terms and points to each definition. It is the one wording of membership that the plan asks for.
  - L562 s1–s2 and the proof (L564) are unchanged.
- **CASES AT RISK:**
  - O48 stays AGREE, on the same point ("there is no alternative in that population").
  - O24 stays AGREE.
  - D3-T is secured, as for W17.1.
  - N5 is as for W17.2.
  - Part XV's (D) (L534) and Part 0 (L43, and L63 as group A's W8.1 leaves it) speak of a "differing survivor". They now use the defined term and read the same. None of these lines is edited here.
- **GAIN:** Derivation 3 states its condition once, in defined terms, and cannot be read with a non-member as the witness.
- **LOSS:** None.

### W7.6 — L588: Derivation 6's proof cites the fuller order

- **STATUS:** applied
- **GROUP:** B1
- **ITEM:** W7
- **FILE-11 LINE:** 588
- **WHERE:** Part XVI, Derivation 6, proof, L588.
- **REASON WORD:** erratum
- **KIND:** CLAIM
- **CHECK:** check 1, SOUND.
- **OLD:**
````text
*Proof.* By the dependence order of Part XIV, following each definition to its base. ∎
````
- **NEW:**
````text
*Proof.* By the dependence order of Part XIV, which lists the declared indices and the declared inputs with the definitions that rest on them, following each definition to its base in the primitives, the indices and the inputs. ∎
````
- **DECLARATION:** Derivation 6's proof now follows each definition to the primitives, the declared indices and the declared inputs, as Part XIV's dependence order lists them.
- **REASON:** Worklist W7 (XR6; 03 M58 and 03 §8 item 5: the claim at L586 includes declared inputs, but the order its proof cites lists none). The proof now cites the order as W7.4 and W7.5 extend it. The claim at L586 is unchanged.
- **CASES AT RISK:** None; no case cites Derivation 6's proof. This was checked against 03's table (M58 is "only through M48").
- **GAIN:** The proof covers its claim.
- **LOSS:** None. The order is still a summary; see conflict 9.

### W10a.1 — Drop Derivation 10's gloss on Derivation 3

- **STATUS:** applied
- **GROUP:** A
- **ITEM:** W10(a)
- **FILE-11 LINE:** 616
- **WHERE:** Part XVI, Derivation 10 (L616), the "Selection" response, end of its last sentence.
- **REASON WORD:** erratum
- **KIND:** CLAIM
- **CHECK:** check 1, SOUND.
- **OLD:**
````text
the fidelity failure is structural, not parametric, and this is Derivation 3's qualification seen from the other side, a population that admits no survivor at the new change.
````
- **NEW:**
````text
the fidelity failure is structural, not parametric.
````
- **DECLARATION:** Derivation 10 no longer describes its structural fidelity failure as Derivation 3's qualification seen from the other side.
- **REASON:** W10(a) (XR7; det 02 C81; 03 M59, CLAIM, and §8 item 6). The gloss misdescribes the qualification: Derivation 3's is no differing survivor, the gloss says no survivor at all, and Derivation 10 does not state that every \(H_0\)-survivor agrees at the occlusion. Derivation 10's conclusions do not rest on the clause. "The fidelity failure is structural, not parametric" is kept. W10(b) goes with W19 (held) at L620, a different paragraph.
- **CASES AT RISK:** None: no case touches M59 (03). Checked O48 and O24, which rest on L562 and L534.
- **GAIN / LOSS:** GAIN: No inexact pointer to Derivation 3. LOSS: A link between Derivations 3 and 10 that was wrong as stated.

### W19.3 + W10(b).1 — Derivation 10: the swap, through an exchange of the two things

- **STATUS:** applied
- **GROUP:** A
- **ITEM:** W19, W10(b)
- **FILE-11 LINE:** 620
- **WHERE:** Part XVI, Derivation 10 (L620), sentence 2. Sentences 1, 3 and 4 are unchanged. W10a.1 changes L616, a different paragraph, and W1.2 anchors on L622.
- **REASON WORD:** change of claim
- **KIND:** CLAIM
- **CHECK:** as W19.1. The text is the settled wording (F1, block 3), copied byte for byte. The sentence was rewritten in settling and has been put to no outside reader in any form. With the rider in W20.2 it is the least tested wording in this list (settled positions, "What this means for the held entries").
- **OLD:**
````text
On any contract containing it, the two persistence components are of one kind (Derivation 2).
````
- **NEW:**
````text
On any contract containing it that admits each edit for both things alike, composing \(t_1\) with the exchange of the two things gives a second transport, which sends each persistence component to the other thing's continuity subnetwork. The two things are built alike in \(P\), and their persistence components alike in \(S_1\), so the exchange carries the fidelity and the answers of \(t_1\) over to the second transport (Derivation 8); so far as (F1), (F2) and (A) reach, the two candidates are one account (Derivation 2).
````
- **DECLARATION:** Derivation 10 no longer says that the two persistence components are of one kind on any contract containing the swap edit. It now says that on such a contract that admits each edit for both things alike, composing the transport with the exchange of the two things gives a second transport, which sends each persistence component to the other thing's continuity subnetwork and has the first transport's fidelity and answers (Derivation 8), and that so far as (F1), (F2) and (A) reach, the two candidates are one account (Derivation 2).
- **REASON:**
  - **W19, with W10(b).** Plan 1.3.1 hands L620's "(Derivation 2)" (NEW-XR1, which 03 ruled CORRECT, loose) to W19's restatement of this sentence, and plan 1.2 replaces W10(b) with it.
  - **The old sentence is false as literally read.** The extended contract on which \(t_1\) is faithful contains displacements. "Displace thing 1" replaces persistence component 1's relation and not component 2's, so under (K) no footprint bijection makes their signatures coincide (Mimo's F1 point 4; the F1 reading, 3.5(f)).
  - **The replacement in view after Atria's reading was false as literally read too.** It said that exchanging the two components' anchors gives a second faithful transport. With \(\lambda\) alone exchanged, (F1) fails at "displace thing 1": the \(S_1\) component that \(\tau\) displaces is anchored to thing 2's continuity subnetwork, which the edit leaves alone. The exchange must run through \(\pi\), \(\tau\), \(\sigma\) and \(\lambda\) together. The settling's script checks this exactly (`results/S88 Mimo reading parts/checks/d10_exchange.py`): \(\lambda\) alone gives (F1) False; the whole exchange gives (F1) and (F2) True.
  - **Why these words.**
    - The exchange is faithful because it is a structure-preserving bijection. That needs the two things alike in \(P\) and their components alike in \(S_1\). "Built alike" states the symmetry that L610 ("two things, each with a position and a velocity") and L616 ("a component per thing") imply.
    - Derivation 8 carries the contract along the exchange. So the second transport is faithful on \(C\) when \(t_1\) is faithful on the exchanged \(C\), and the two are the same exactly when \(C\) admits each edit for both things alike.
    - Derivation 2 speaks of candidates, and it carries the qualifier "so far as (F1), (F2) and (A) reach". This answers skeleton conflict 5: on a contract other than the one where L618 calls the account adequate, nothing else supplies the rest of (E).
  - **Read in place.**
    - Under the second transport, persistence component 2 and thing 1's continuity subnetwork share one anchor on thing 1's ports. So W19.2's premise holds, with \(\varphi\) the exchange of the two components, and its colon gives the pairing: each pair is of one kind on \(C\), read through the two transports (W19.1). That is the content the old sentence aimed at.
    - In the next sentence, "them" now takes "the two candidates" as its antecedent. "A claim that component 1 is *really* thing 1" is the claim that \(t_1\) is right and the second transport is not, and on a contract that admits each edit for both things alike no admitted change separates them. "This contract" there is such a contract.
    - "The two candidates" are the candidate with \(S_1\) and \(t_1\) and the candidate with \(S_1\) and the second transport. Derivation 10 does not use the word "candidate" before this sentence; the reader supplies the pairing from Part V (L233).
- **CASES AT RISK:** None. No O- or N-case turns on Derivation 10's worked episode (N14, the walking robot, is set aside, D8). O43 (a declared recoding, Derivation 8) is not reached: the sentence uses Derivation 8 as L602 states it.
- **GAIN:** The worked episode's identity sentence is true, and it says what makes it true. L620's loose pointer to Derivation 2 becomes exact.
- **LOSS:** The sentence now holds only on contracts that treat both things alike, and it says "one account" only so far as (F1), (F2) and (A) reach.

### W1.2 — The revision record closes the document

- **STATUS:** applied
- **GROUP:** M
- **ITEM:** W1, W3
- **FILE-11 LINE:** 622
- **WHERE:** Part XVI, Derivation 10, L622, the last line of file 11. The record is inserted after it, and L622 is kept byte for byte. L622 belongs to no group. Group A's reserved L620 is not touched.
- **REASON WORD:** meta
- **KIND:** META
- **CHECK:** check 2, SOUND. All 42 locators and rows were checked. Finding: f10 L294 s2 became f11 L279 s2 with no row; it is plausibly WORDING, and layer 2 follows 03, so no row is added.
- **OLD:**
````text
This episode is a relative-consistency witness for the class. It is not a claim that any actual infant, animal, or program has been shown to instantiate it.
````
- **NEW:**
````text
This episode is a relative-consistency witness for the class. It is not a claim that any actual infant, animal, or program has been shown to instantiate it.

<!-- META:RECORD BEGIN -->
---

# Revision record

This record belongs to the note at the head of this document. It has two layers. Layer 1 is this revision against file 11. Layer 2 is file 11 against file 10, as file 11's note should have said. Line numbers are file 11's unless file 10 is named.

The record rules with three words. A change is **CLAIM** when a reader can conclude from one of the two texts something the other leaves unconcluded: an assertion added or dropped; a narrowing, widening or qualification; a requirement, condition, exception, quantifier or outside input added or removed; or something derivable from the old text stated for the first time. A change is **WORDING** when both texts assert the same thing and every conclusion drawn from one can be drawn from the other. A change is **ORDER** when the same claim is moved or copied to another place.

## Layer 1: this revision against file 11

Each entry gives its place in file 11, the reason it is made (erratum, clarification or change of claim), the ruling expected for it, its old and new text, and what a reader can now conclude that file 11 left unconcluded. Every entry expected as CLAIM is declared in the note. Besides these entries, this revision replaces file 11's note (line 5) with the note at the head of this document, and adds the note of sources and departures after it and this record at the end. The three are not part of the theory.

@@LAYER1@@

## Layer 2: file 11 against file 10, undeclared by file 11's note

File 11's note said that one claim changed, Derivation 3, together with the sentences that restated it, and that nothing else changed in what is claimed. The declared change stands: Derivation 3 (lines 560–566), the answer to grievance 3 (line 43), and attack (D) in Part XV (line 534), which is both "attack point (D)" and "the Part XV entry" of that note. The rest of that note did not hold. File 11 added five definitions (rows L2-26, L2-29, L2-33, L2-35 and L2-37), and at every place below it changed what is claimed.

At each place below, a reader can conclude from one of the two files something the other leaves unconcluded, and file 11's note did not say so. Rows L2-09, L2-11, L2-35 and L2-42 carry the declared change to Derivation 3 at places the note did not name. Rows L2-03 and L2-36 are one change, made at two places. Row L2-04 is a rule for reading the document, not a claim of the theory. The last column says whether the place stands word for word in this revision, and which entry of layer 1 changes it or adds text beside it.

| row | Part and heading | file 10 | file 11 | what a reader can now conclude | in this revision |
|---|---|---|---|---|---|
| L2-01 | Part 0, What this document does not claim | L25 | L27, sentences 1–2 | A measure of worth is among the things the semantics does not supply, and a claim that needs any of them takes it as a declared input at a marked place; file 10 left each such place empty. | @@REV2:L2-01@@ |
| L2-02 | Part 0, What this document does not claim | none | L27, sentence 3 | The semantics supplies no division of credit among contributors beyond what a history establishes. | @@REV2:L2-02@@ |
| L2-03 | Part 0, What is primitive, what is an index, and what is derived | L519; compare L458, L593, L597 | L33, sentence 1 | The normative relation is taken as an input wherever a question invokes worth; file 10 took it when a question invokes a normative relation. One change with row L2-36. | @@REV2:L2-03@@ |
| L2-04 | Part 0, Grievances, anticipated | none | L37 | The front matter states nothing the body does not state more exactly, so where the two differ the body's statement is the claim. This is a rule for reading the document. | @@REV2:L2-04@@ |
| L2-05 | Part II, Kinds are edit-signatures | none; compare L126, L138–L144 | L129, sentences 4–5 | A part that reads or reports another part has a measurement's signature, and which of the two an account offers as producing an outcome is settled by that signature, not by the account's wording. | @@REV2:L2-05@@ |
| L2-06 | Part III, The respect is the query | none; compare L168 | L153, last sentence | A measure that identifies an outcome, with a reliable prediction from it, answers the identification question and does not answer the production question. | @@REV2:L2-06@@ |
| L2-07 | Part III, Scope, and a question that can be wrong | none | L161, sentence 3 | What makes a restriction appropriate to the question asked is a substantive, criticizable part of the claim, which the semantics records and does not certify. | @@REV2:L2-07@@ |
| L2-08 | Part III, Scope, and a question that can be wrong | none; compare L168, L176, L268 | L163, last sentence | Supplying a meaning for a replacement query can make a coherent new question, and it does not answer the original one. | @@REV2:L2-08@@ |
| L2-09 | Part IV, Three provenances (Selected) | L210 | L197, last sentence | The population of a selection is part of the claim, and what the history leaves open about a selected transport is what its population leaves open. This carries the declared change to Derivation 3. | @@REV2:L2-09@@ |
| L2-10 | Part IV, Representation is derived | none; compare L208, L226, L342 | L213, last sentence | A carrier keeps its provenance when present access to it is lost, and a later record derived from the carrier is not a second, independent witness to its history. | @@REV2:L2-10@@ |
| L2-11 | Part IV, Expectation, surprise, violation | L238 | L225, last sentence | Whether a selected correspondence could have been otherwise at an unseen change is a fact about its population. This carries the declared change to Derivation 3. | @@REV2:L2-11@@ |
| L2-12 | Part V, What (E) excludes, and what it does not | L284, sentence 2 | L271, sentences 2–3 | A table that encodes an organization's response to every admitted change satisfies (F1) and is an account; file 10 said only that it is not excluded. | @@REV2:L2-12@@ |
| L2-13 | Part V, What (E) excludes, and what it does not | L288 | L275, sentence 2 | An account whose only substantive component restates the answer it was asked for fails non-circular dependence, and a genuine dependence that answers a different question, packaged beside it, does not repair this. | @@REV2:L2-13@@ |
| L2-14 | Part V, What (E) excludes, and what it does not | L294, sentence 1 | L279, sentence 1 | A true mechanism guessed for bad reasons is not excluded by (E); file 10 said that it satisfies (E), and that can no longer be concluded from this sentence. | @@REV2:L2-14@@ |
| L2-15 | Part V, What (E) excludes, and what it does not | none | L279, sentence 3 | (E) does not reject a coarse dependence for omitting finer workings or an instrument: an account at a coarse grain is an account of the coarse question, and its strength is fixed by its contract, not by what a finer contract would add. | @@REV2:L2-15@@ |
| L2-16 | Part VI, Work, support, and interference (opening) | L316 | L301, sentence 2 | Criticality is relative to the support it is assessed in; a commitment critical in one successful support need not be critical in the full candidate; and the supports assessed are the ones actually written. | @@REV2:L2-16@@ |
| L2-17 | Part VI, Redundant routes | L324 | L309, sentence 3 | A route already present in the candidate is a route whether or not anyone has described its work, and a component reassigned to a new target after a deletion belongs to a new candidate, whose success is not the old one's. | @@REV2:L2-17@@ |
| L2-18 | Part VIII, Recoding | none; compare L609 | L363, sentence 1 | A declared, invertible recoding of a carrier preserves the content when a reader who applies the declared convention recovers every pairing. | @@REV2:L2-18@@ |
| L2-19 | Part VIII, Recoding | none | L363, sentence 2 | A section of a carrier filled from another source keeps that other source's history, whatever it happens to match. | @@REV2:L2-19@@ |
| L2-20 | Part IX, Histories | L384 | L371, last sentence | A route that started and did no work, or that was already at rest when the result occurred, is not active for that result, and whether a route is active is read from the history, not from the result. | @@REV2:L2-20@@ |
| L2-21 | Part IX, Receipts | L406 | L393, last sentence | A record reconstructed from the claim it is meant to support is not a receipt for that claim. | @@REV2:L2-21@@ |
| L2-22 | Part X, Deployment | L412 | L399, last sentence | A narrow retained use establishes neither the wider understanding it falls short of nor a permanent inability to reach it. | @@REV2:L2-22@@ |
| L2-23 | Part X, Construction | L414 | L401, sentence 4 | A first representation may be constructed from an available problem without prior observation of what it represents. | @@REV2:L2-23@@ |
| L2-24 | Part X, Construction | L414 | L401, sentence 5 | A small binding newly prepared inside received content is construction of that binding, and the rest of the content keeps its inherited provenance; file 10's Build asked for a nontrivial binding construction and said nothing of the rest of the content. | @@REV2:L2-24@@ |
| L2-25 | Part X, Origin | L430 | L417, last sentence | A dimension of variation mentioned in passing is not a port of the account until the account admits changes to it, and adding it is construction. | @@REV2:L2-25@@ |
| L2-26 | Part X, Ownership | none | L419 | Ownership of Build's subhistory is defined: its processes run inside the system boundary and resource contract declared for the system. Work supplied from outside that boundary remains an outside contribution however it is executed inside; a process that runs inside the boundary is the system's own today whoever wrote it; where the boundary is drawn decides, not where the process sits; and ownership is not defined by the capability it grounds. File 10 used "owned" without defining it. | @@REV2:L2-26@@ |
| L2-27 | Part XI, Repair | L438–L444 | L433, sentence 1 | The obligations of a repair are declared inputs, each a stated condition over stated occasions, and a protected condition is lost exactly when it fails on an occasion it covers; file 10 checked a protected condition at the two ends of the comparison and named no occasions. | @@REV2:L2-27@@ |
| L2-28 | Part XI, Repair | L444 | L433, sentence 2 | Declaring the obligations makes no claim that the aims are worth pursuing; file 10 said only that (P) does not rank alternatives. | @@REV2:L2-28@@ |
| L2-29 | Part XI, Repair | none; compare L441 | L433, sentence 4 | ProducedBy is defined: it holds when an active route runs from the contribution to the repair; it credits each contribution the history establishes; and where two sufficient contributions both ran, both are credited and no division of credit is supplied that the history does not contain. File 10 used ProducedBy in (P) without defining it. | @@REV2:L2-29@@ |
| L2-30 | Part XI, Repair | none | L433, sentence 5 | A correct account that produced nothing, an act that repaired without an account, and a repair produced through use of an account are three different attributions. | @@REV2:L2-30@@ |
| L2-31 | Part XI, Worth, and the normative relation | L458 | L447, heading and sentences 1–2 | The normative relation is taken as an input wherever a claim invokes worth, not only where aesthetic value is claimed, and repairing an obligation establishes nothing about whether it, or the question that led to it, was worth having. | @@REV2:L2-31@@ |
| L2-32 | Part XI, Worth, and the normative relation | L458, last two sentences | L447, last clause | No aesthetics follows from achieving a stated effect; file 10 said only that none of the aesthetic relations is defined as another and that the semantics does not derive the normative relation. | @@REV2:L2-32@@ |
| L2-33 | Part XII, System boundary and continuity | none; compare L523 | L465 | A capability is attributed under a declared boundary and a declared continuity, both declared before the attribution and not chosen after it; a replaced part that preserves the continuity leaves the same system; a process run inside the boundary is the system's whoever wrote it, and one run outside it is not, however close it sits. File 10 had boundary and continuity only as indices. | @@REV2:L2-33@@ |
| L2-34 | Part XII, Owned capability | L476 | L467, last sentence | Ownership is grounded in the processes and resources the boundary includes, never in the capability being attributed. | @@REV2:L2-34@@ |
| L2-35 | Part XII, Selection in the physical module | L482 | L473, last sentence | The population of a selection is the set of transports the physics and the stated construction admit, and a transport that would need a part every member of the population is built without is not in it. This carries the declared change to Derivation 3. | @@REV2:L2-35@@ |
| L2-36 | Part XIV, Primitives | L519 | L510 | The normative relation is a primitive when a question invokes worth, taken as an input and never derived, and the aesthetic relation of Part XI is one instance of it. One change with row L2-03. | @@REV2:L2-36@@ |
| L2-37 | Part XIV, Declared inputs | none; compare L521–L523 | L514 | Some claims take stated inputs that the semantics records and does not supply: the obligations of a repair with the occasions each covers, the scope of a contract and what makes a restriction appropriate, and the boundary and continuity of an attribution. A verdict that depends on one is a verdict given the input, and where the input is missing the verdict is unsettled. | @@REV2:L2-37@@ |
| L2-38 | Part XIV, Dependence order | L525 | L518, last sentence | The dependence order is well founded: a representation justified only by its own construction, or an ownership and a capability justified only by each other, has not supplied its place in it, and a separate proof that would supply that place counts only when the account uses it. | @@REV2:L2-38@@ |
| L2-39 | Part XV, (A) Sufficiency | L68; compare L284, L533 | L528, sentence 3 | A table that encodes the response to every admitted change fails none of the four conditions and is an account, so it is not a counterexample to sufficiency; under file 10 it was not excluded and stayed open as a possible one. | @@REV2:L2-39@@ |
| L2-40 | Part XVI, Derivation 5, Consequence | L589 | L582, last sentence | That a question was found says nothing about its worth. | @@REV2:L2-40@@ |
| L2-41 | Part XVI, Derivation 6, Claim | L593 | L586 | Every predicate of Parts II–XIII is defined from the primitives together with the declared indices and the declared inputs; file 10 named the declared indices only. | @@REV2:L2-41@@ |
| L2-42 | Part XVI, Derivation 10 | L623 | L616, one clause | The structural failure of the selection response is given as Derivation 3's qualification seen from the other side, a population with no survivor at the new change. Derivation 3's qualification concerns a differing survivor, so the gloss is inexact. This carries the declared change to Derivation 3. | @@REV2:L2-42@@ |
<!-- META:RECORD END -->
````
- **DECLARATION:** made by the note ("the changes listed in the revision record at the end of this document"; "@@K@@ places"). Each layer-2 row is itself a declaration of a change of claim of file 11 against file 10. Not counted in N or M.
- **REASON:**
  - Worklist W1 and W3; plan 1.3.5 and 2.5; D6 ("a two-layer record (revision 2 against file 11; file 11's undeclared places against file 10)").
  - **Layer 1** is generated from the applied change list (form under "For the record writer"), because it must match what the builder applied.
  - **Layer 2** is written now, from 03's master table: all 42 undeclared CLAIM places, 41 inside the theory and M7 (03 §2). Each row gives Part and heading, file-10 line, file-11 line, and one line on what a reader can now conclude, as plan 1.3.5 asks.
    - The four Derivation 3 places the note missed are named: rows L2-09, L2-11, L2-35 and L2-42 (L197, L225, L473, L616; XR1).
    - Attack point (D) and the Part XV entry are treated as one passage, L534 (plan 1.3.1, XR1).
    - M5 and M47 are one change at two places (rows L2-03, L2-36).
    - M59's clause, which revision 2 removes (group A's W10a.1), is still declared, as file 11 had it (row L2-42).
  - The record names no M-number, case or record file (plan 1.3.5). The map from rows to 03's places is given below, for S81 Results.
  - Plan 2.5's old→new map of the attack labels is left out (D9).
  - The three ruling words are 03's definitions, restated so that the record can be read alone.
  - The last column is computed, not written by hand. For each row it says whether the file-11 place survives word for word in the cut draft, and which layer-1 entries change it or add text beside it. The provisional values are given below.
- **CASES AT RISK:** none. The block is cut from every brief (D6). The cut is checked above.
- **GAIN:** Every change of claim that file 11 made without saying so gets one line. A reader of revision 2 sees what changes now and what changed silently before, and whether each earlier change still stands.
- **LOSS:** The authority file grows by about 2,700 words for layer 2 and the frame, plus layer 1. Plan 2.7 estimated layer 1 at about 3,000 words.
- **LAYER-2 LOCATORS:** for each layer-2 row, the exact file-11 text of the place it declares (once in file 11). The program uses them to fill the row's last column. One row per line: the row id, one space, the locator.
````text
L2-01 It does not supply an objective aesthetics, a probability of truth, a merit function, a measure of worth, or a ranking of thinkers. Where a claim needs one of these, the semantics takes it as a **declared input** and marks the place (Parts XI, XIV).
L2-02 It does not supply a division of credit among contributors beyond what a history establishes (Part XI).
L2-03 taken as an input wherever a question invokes worth.
L2-04 Each answer points at the part of the document that carries it; the front matter states nothing the body does not state more exactly.
L2-05 In particular, a part that reads or reports another part has a measurement's signature: change only the reading and the part it reports stays as it was; change the part and the reading follows. Which of the two an account offers as producing an outcome is settled by that signature, not by the account's wording.
L2-06 A measure that identifies an outcome, with a reliable prediction from it, answers the identification question; whether the measured part also produces the outcome is the production question, and the first answer is not the second.
L2-07 What makes a restriction appropriate to the question asked is a substantive, criticizable part of the claim; the semantics records the restriction and supplies no rule that certifies it.
L2-08 Supplying a meaning for a replacement query can make a coherent new question; it does not answer the original one.
L2-09 The population \(\mathcal T\) is part of the claim: what \(H\) leaves open about \(t\) is what \(\mathcal T\) leaves open (Derivation 3).
L2-10 A carrier keeps its provenance when present access to it is lost, and a later record derived from the carrier is not a second, independent witness to its history.
L2-11 Whether the correspondence could have been otherwise at such a change is a fact about its population (Derivation 3).
L2-12 A table that genuinely encodes an organization's response to every admitted change is not a table in that sense: it satisfies (F1) as a decomposition does, and it is an account. The word "table" settles nothing; the response under the admitted changes does.
L2-13 So does an account whose only substantive component restates the answer it was asked for; packaging a genuine dependence that answers a different question beside it does not repair this (the bell does not explain the tide).
L2-14 (E) does not exclude a true mechanism guessed for bad reasons; the reasons for adopting it are assessed elsewhere (Part IX).
L2-15 It does not reject a coarse dependence for omitting finer workings or an instrument: an account at a coarse grain is an account of the coarse question, and its strength is fixed by its contract, not by what a finer contract would add.
L2-16 Criticality is relative to the support \(W\) it is assessed in: a commitment critical in one successful support need not be critical in the full candidate, and the supports assessed are the ones actually written, not a support someone could write in their place.
L2-17 A route already present in the candidate is a route whether or not anyone has described its work; a component reassigned to a new target after a deletion belongs to a new candidate with its own assessment, and the new candidate's success is not the old one's.
L2-18 A declared, invertible recoding of a carrier preserves the content when a reader who applies the declared convention recovers every pairing (Derivation 8).
L2-19 A section of a carrier filled from another source keeps that other source's history, whatever it happens to match.
L2-20 A route that started and did no work, or that was already at rest when the result occurred, is not active for that result; whether a route is active is read from the history, not from the result.
L2-21 A record reconstructed from the claim it is meant to support is not a receipt for that claim.
L2-22 A narrow retained use is what it is: it establishes neither the wider understanding it falls short of nor a permanent inability to reach it.
L2-23 A first representation may be constructed from an available problem without prior observation of what it represents.
L2-24 A small binding newly prepared inside received content is construction of that binding, and the rest of the content keeps its inherited provenance.
L2-25 A dimension of variation mentioned in passing is not thereby a port of the account; it becomes one when the account admits changes to it, and adding it is construction.
L2-26 **Ownership.** The subhistory in Build is owned by \(s\) when its processes run inside the system boundary and resource contract declared for \(s\) (Part XII). Work supplied from outside that boundary, a diagnosis, a decisive question, an instruction about what to read, remains an outside contribution however it is executed inside; a process that runs inside the boundary is the system's own today whoever wrote it; and where the boundary is drawn decides, not where the process sits in the casing. Ownership is not defined by the capability it is meant to ground (Part XII).
L2-27 The obligations are declared inputs: \(O\) says what is to be repaired and \(P\) what is to be protected, each as a stated condition over stated occasions, and a protected condition is lost exactly when it fails on an occasion it covers.
L2-28 Their declaration makes no claim that the aims are worth pursuing, and (P) does not rank alternatives.
L2-29 \(\operatorname{ProducedBy}\) holds when an active route (Part IX) runs from \(\Delta\) to the repair; it credits each contribution the history establishes, and where two sufficient contributions both ran, both are credited and the history supplies no division of credit that it does not contain.
L2-30 A correct account that produced nothing, an act that repaired without an account, and a repair produced through use of an account are three different attributions.
L2-31 **Worth, and the normative relation.** Repairing an obligation establishes that it was repaired; it establishes nothing about whether the obligation, or the question that led to it, was worth having. Where a claim invokes worth, the semantics takes a **normative relation** \(\mathcal N\) as a declared input and marks the place (Part XIV).
L2-32 and no aesthetics follows from achieving a stated effect.
L2-33 **System boundary and continuity.** A capability is attributed to a system under a declared boundary (which processes and resources are the system's) and a declared continuity \(\Omega\) (what makes it the same system through change). A replaced part that preserves the declared continuity leaves the same system; a process run inside the boundary is the system's whoever wrote it; a process run outside it is not the system's however close it sits. Both are declared before the attribution, not chosen after it.
L2-34 Ownership is grounded in the processes and resources the boundary includes, never in the capability being attributed: "owned because it can, and can because owned" grounds neither.
L2-35 The population is the set of transports the physics and the stated construction admit; a transport that would need a part every member of the population is built without is not in it.
L2-36 2. The **normative relation** \(\mathcal N\), when a question invokes worth. It is taken as an input and never derived; the aesthetic relation of Part XI is one instance.
L2-37 **Declared inputs.** Besides the two primitives, some claims take stated inputs that the semantics records and does not supply: the obligations \(O\) and \(P\) of a repair, with the occasions each covers (Part XI); the scope of a contract and what makes a restriction appropriate (Part III); the system boundary and continuity of an attribution (Part XII). A verdict that depends on one of these is a verdict given the input; where the input is missing, the verdict is unsettled and the semantics says so rather than choosing the input from the verdict wanted.
L2-38 The order is well founded: a representation justified only by its own construction, or an ownership and a capability justified only by each other, has not supplied its place in it, and a separate proof that would supply it counts only when the account uses it.
L2-39 A table that encodes the response to every admitted change fails none and is an account, so it is not a counterexample; a new attempt must fail none and still explain nothing.
L2-40 That a question was found says nothing about its worth (Part XI).
L2-41 **Claim.** Every predicate in Parts II–XIII is defined from \(\Theta\) (including \(\operatorname{Org}_\ell\)) and, where invoked, \(\mathcal N\), together with declared indices and declared inputs.
L2-42 and this is Derivation 3's qualification seen from the other side, a population that admits no survivor at the new change
````
