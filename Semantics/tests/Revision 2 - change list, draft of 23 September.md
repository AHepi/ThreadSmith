# Revision 2 - change list, draft of 23 September

**DRAFT — not frozen. Made from file 11, md5 5e494c1095d920d128b9a79de378f923. W19, W20 and W31 are drafted from the settled S88 positions (3ebb6d8); no outside reader has seen their final wordings.**

*Written on 23 September 2026 by a Claude subagent for the orchestrator. This is the change list from which revision 2 (file 13) is to be made by program (decision D6). It assembles the entries drafted in five groups (A, B1, B2, C and M) under decisions D1–D11, with every correction the two adversarial checks made and without the one entry they dropped. The working files it was assembled from (the decisions, the item skeleton, the five entry files and the two checks) are in the session scratchpad and are not in the repository. File 11 was read only; its md5 was the same before and after. No S87 or S88 return was opened. Nothing was written into `authority/`. Later on 23 September another Claude subagent replaced the three placeholders with seven entries drafted from `results/S88 Reading of Mimo's reply in three parts, and the settled positions.md` (committed at 3ebb6d8), and brought the frame of this list up to date with them. It opened no S87, S88 or S90 return and wrote nothing into `authority/`.*

## What this is

This list gives every change that revision 2 makes to file 11, in the order of file 11's text. The program `tools/s89_apply_changes.py` reads it, checks every entry against file 11 and applies the entries in order. It refuses on any mismatch. It writes the result to a path given on its command line, never into `authority/`. The draft note for file 13, with its declarations and the second layer of the record, is `tests/Revision 2 - revision note, draft of 23 September.md`.

The list rests on D1. If Mimo's cross-examination of the S81 determination overturns S81, every entry is re-examined under plan 2.2 B or C before anything is built.

W19, W20 and W31 waited for Mimo's S88 reply (D2). They are now drafted from the settled S88 positions as seven entries, and the note's counts include them ("The held items, drafted from the settled S88 positions", below). No outside reader has seen their final wordings, and the cross-examination of revision 2 (X1) must carry them.

The list is withheld from every test brief (D6), as are the note, the sources note and the record it puts into file 13.

## Counts

- **Entries that change the theory text: 55.** Expected ruling CLAIM 48, WORDING 5, ORDER 2. By group: A 14 of 18, B1 13 of 15, B2 11 of 11, C 10 of 11. The note reads "48 of the 55 changes". Before the held items were drafted it read "41 of the 48 changes".
- **Meta entries applied: 3.** W1.1 (the note, replacing file 11's line 5), W38.1 (the note of sources and departures, before Part 0) and W1.2 (the revision record, after the last line). They are not counted in the note's N or M.
- **Record-only entries: 5.** W3.1–W3.5 declare five places in layer 2 of the record. They change no text, and the program locates them without applying them.
- **Held: 0.** The placeholders for W19, W20 and W31 are replaced by seven entries (W19.1–W19.3, W20.1–W20.3 and W31.1), each expected CLAIM. All seven are group A.
- **The checks.** Check 1 (groups A, B1 and B2, 38 entries): SOUND 26, FIX 11 (nine change the new text, two change only the expected ruling), DROP 1. Check 2 (groups C and M, 18 entries): SOUND 10, FIX 8, DROP 0, and one companion entry added (W35.4). In all, 19 entries were fixed, 1 was dropped and 1 was added. Every fix is applied below. The seven entries drafted later from the settled S88 positions were checked by their drafter only; see "The held items, drafted from the settled S88 positions".
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
- **No outside reader has seen these wordings in their final form.** The cross-examination of revision 2 (X1) must carry all seven; the S90 brief carries only the first 48 changes. Within X1, the deletion rider (W20.2) and the Derivation 10 sentence (W19.3) are the least tested. The rider was never put to either reply, and the Derivation 10 sentence was rewritten in settling.
- **The fallback for W20** is settled with it and written in W20.2's CHECK. It applies if X1 finds that the rider breaks a worked case. If both options break something, only the \(\tau,\sigma\) erratum is taken (plan 1.3.4).
- **The entries of other groups** that refer to W19, W20 or W31 as not yet drafted (W30.1, W33.1, W39.1, W9.1, W24.1, W21.1, W7.5, W3.2, W10a.1 and W1.2) were written before this drafting. They are left as their groups and checks wrote them. The rechecks they ask for (skeleton conflicts 1–5, 11 and 12) are done in the seven entries.
- **The S90 brief's ids no longer match the R2 numbers from C08 on.** The S90 brief was sent before these entries were drafted. It cites the first 48 changes as C01–C48, in file-11 order, which were R2-01–R2-48 in the note of that time (commit 12e73da). The program numbers the applied entries in file-11 order, so every entry from W19.1 (L121) on now has a higher number: C01–C07 are still R2-01–R2-07, C08 (W30.1) is now R2-09, and C48 (W10a.1) is R2-54. The note's map (its section 5) gives each entry's S90 id beside its R2 number. Read S90's replies through the entry ids.
- **Checked by the drafter, not by check 1 or check 2.** The whole list was applied by `tools/s89_apply_changes.py` into a scratch draft, never into `authority/`, with `--self-test`. It parsed 63 entries: 58 applied (55 theory, 3 meta), 5 record-only, none held. Every OLD, locator and anchor occurs once in file 11, and no applied OLDs overlap; W19.1 and W30.1 share L121, and W39.1 and W20.2 share L257, with disjoint OLD texts. The result is file 11 with exactly the listed replacements, in 54 diff hunks, each inside an entry, and the self-test refused both planted edits. N = 48 of M = 55, K = 42. The draft's md5 is 1d51c77eb591ace473e556568a7c4636, at 25,696 words (theory text alone 11,501).
  - Each new paragraph was read in place. Three notation points are carried forward below (Part II's forward notation; "active"; the two readings of "including any that assigns an input").
  - The guard rows were worked through the new text: O2, O4, O5, O7, O10, O24, O33, O36, O45, O46 and O47; N1, N3, N17, N20, N23 and N25; Part VII's production case and the skew-symmetric case. No fixed verdict moves on a reading the text supports.
  - Watched, with a risk away: O45 under W20.1, where "those the candidate offers as doing the work" meets "never described as doing anything"; N1, as W33.1 records, now on fidelity rather than membership; and N25's second question under W19.2, for a reader who rested it on the old slogan.
  - Toward: O5 and O7 (W20.2), O46 on firmer text and N17 on its first two questions (W19.2), and the first half of N23 (W20.2).
  - The settling's scripts were rerun (`f1_check.py`, `f3_check.py` and `d10_exchange.py` in `results/S88 Mimo reading parts/checks/`), and their outputs match the readings and the settled file.

## Findings carried forward

These were found while drafting and checking. None is an entry.

- **\(U_c\) and \(A_p\)** in (U1)–(U2) are undefined in file 11 (group A, C3). Defining them is one clause at L489 and a CLAIM, outside every item taken.
- **The dependence order is still a summary** (group B1, finding 9). After W7.4–W7.5 it omits (K2), receipts, (K3), (CA), (CT2)–(CT4), Barriers, Enable, Scrutinizability, Membership, Result, ProducesVia and Cap. "(P), (EK) depend on (G), (E), Deploy" over-states (P)'s dependence and is kept.
- **04's O40 ruling cites the old L27 s2** (group B1, finding 12). After W6.1 that sentence no longer says it. The ruling's items 1–3 carry O40 without it; S81 Results should note the change.
- **The plan's prediction P2(d)** names O54, O57, O59, O60, O61, O62, O66, O70 and O73 as rows whose ruled marks stay equal. O57 (W17.2), O61 (W23.2) and O62 (W12.1, W13.2) can move toward the thoughtful person under these entries (group B2, conflict 1), and N4 (O56, Q2) and N1 (O53) are watched under W34.1, W36.1, W41.1 and W33.1 (check 2). Before the freeze the plan should move these rows into P2(b)'s aimed set, or record that a change toward on them traces to these entries.
- **Records misread where (I4) points** (group A, C2). No verdict rests on it, and nothing is changed.
- **f10 L294 s2 became f11 L279 s2** with no layer-2 row (check 2, on W1.2). It is plausibly WORDING, and layer 2 follows 03, so no row is added.
- **Line numbers move.** W41.1 adds four lines after L401, and the meta blocks add lines at the head. The note, the record, the diff map and every brief use file-11 numbering. The program does not assert an unchanged line count, and it allows W35.1's two hunks (L219 and L223) for one entry.
- **The withheld-word check** on briefs must use the marker strings, "Revision 2", "revision record", "file 13", "Deutsch" and "Marletto", and not the bare word "record", which the theory itself uses (group M, conflict 3).
- **The note's form.** Plan 2.5 makes the note one paragraph. W1.1 gives the paragraph and, in the same block, one line per change of claim (group M, conflict 2).
- **Layer 2 rests on 03 and on D1** (group M, conflict 5). If Mimo's cross-examination changes a ruling of 03, a row is added or removed, and K with it.
- **The declared inputs (L514) do not list Part VI's declared restriction operation** (settled S88 positions, "Found in settling", point 4). (S) and (B) depend on it (L289: "Fix \(\mathcal E\) and a declared restriction operation"). Derivation 6 is not made false: L586 allows declared indices and declared inputs, and Part VI declares the operation where it uses it. The looseness predates every S88 repair, and under the rider W20.2 adds nothing to it. The candidate clause for L514 is "the restriction operation of Part VI (\(E|W\))". It is not an entry.
- **Part II uses the notation of Parts IV and V before they introduce it** (W19.1, read in place). The new sentences at L121 use \(E\), \(E'\), \(\tau\), \(\tau'\), \(\lambda\) and "hidden ports", which L191, L233 and L235 introduce, with no pointer. A pointer such as "(Parts IV and V)" would close it, but it would change the settled wording, so it is left for X1 or the orchestrator.
- **"Active" is still undefined** (W20.1, read in place). L233 has "active commitments", and (F1) at L235 has "every active component". W20.1 makes Γ a set of components and puts the components that assign inputs in the named background. If "active component" is read as "member of Γ", (F1) no longer checks the named-background components one by one; (F2) still checks the whole. The settled position declined Mimo's "active" because it is undefined, and nothing is changed.
- **W20.1's "including any that assigns an input" has two readings.** On one, every component that assigns an input is outside Γ. On the other, any such component that the candidate leaves out of Γ is named background. The named verdicts are the same on both (the F3 reading's models 1a and 1b).
- **O45 against W20.1's "those the candidate offers as doing the work".** The phrase meets the case's "never described as doing anything". The entry holds the AGREE on L309 s3, W28.1 and W58(i).1, and asks X1 to test the row.

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
- **GROUP:** M
- **ITEM:** W38
- **FILE-11 LINE:** 7–9
- **WHERE:** front matter, after the note. It is inserted before the rule `---` at L7 that opens Part 0. The anchor is L7–L9 (the rule, the blank line and the Part 0 heading), kept byte for byte. L7–L9 belong to no group.
- **REASON WORD:** meta
- **KIND:** META
- **CHECK:** check 2, FIX. Five statements were inaccurate: what file 00 cites, Marletto's page for interoperability, Deutsch's definition of a problem, the Derivation 6 clause, and the stated-limits line against B1's wording. Three lines follow C's fixes (physical media, a separate matter, does no work by itself). The fallback table's substrate row now cites chapter 3, pp.88 and 95. The assembler also gave the fallback for "Surprise and problems" the corrected account of Deutsch's "problem", which check 2's fix (c) implies but did not write out.
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
- *Idle parts.* Deutsch counts superfluous features as a defect of an explanation (chapter 1, p.25). Here (E) has no condition that each commitment do work: a commitment that does no work by itself is critical in no support, and how hard an account is to vary grades nothing (Part VI).
- *Reach.* Deutsch's reach is the power of an explanation to solve problems beyond those it was made for (chapter 1, p.28). Here the reach of an account is the set of jobs on which it is an account, fixed by the account and the world (Part VI).
- *Stated limits.* Both books hold that a limit of scope needs an explanation (Deutsch, chapter 1, pp.27–28; Marletto, chapter 1, p.24). Here a stated limit is recorded and not certified: meeting the conditions of an account on a restricted contract certifies nothing about the restriction, and a verdict on a restriction whose ground the claim states is given with that ground (Part III).
- *Selection.* Deutsch calls criticism and experiment a selection (chapter 4, p.78). Here selection is blind: its history holds no represented target (Parts 0 and IV).
- *Surprise and problems.* For Deutsch a problem is a situation in which conflicting ideas are experienced, and a problem can arise without any observation (chapter 1, p.17). Here surprise is kept for selected transports (Part IV). A problem in his sense is a recognized difficulty (Part X): a failure of a claimed obligation, or a conflict in which meeting a claimed obligation fails a protected one (Part XI), when the system represents it.
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
  - **Named and not named.** The decision number (S19) is not named, because no meta block names a record file. The third book is mentioned and not named or cited, since plan 1.3.6 says it is not cited.
  - Each line that rests on another group's entry has a fallback, given below, for use if that entry is dropped under plan 1.5's cap.
- **CASES AT RISK:** none. The block is cut from every brief (D6), and "Deutsch" and "Marletto" are on the build's withheld list (plan 2.5). If it reached a tester, the departures would steer readings toward the books' judgements at exactly the guard rows: idle parts (N1, N25), stated limits (O1, O5, O8, N7), selection (O11, N11), surprise (O3, N18, N19) and elimination (N22).
- **GAIN:** Lineage, and honesty about where the semantics departs from its two sources.
- **LOSS:** Readers may hold the theory to the books (worklist W38). The authority file grows by about 720 words.
- **FALLBACKS:** if an entry a line of the sources note rests on is dropped under plan 1.5's cap, the line is replaced by the fallback, or dropped where none is given.

  | line | rests on | fallback |
  |---|---|---|
  | Inexplicit representation (parallels) | C W41.1 | drop the sentence |
  | Part I's substrate independence (parallels) | C W45.1 | Part I's substrate independence is stated without condition; Marletto treats the interoperability of carriers as a law of physics that may fail (chapter 3, pp.88 and 95). |
  | Explanation | C W36.1 | - *Explanation.* Deutsch counts a false myth as an explanation (chapter 1, p.19). Here that is an explanatory candidate (Part V), and Part I's fallibility commitment uses "explanation" for what is not in error in the dependence alleged to do the work. |
  | Idle parts | C W33.1 (the words 'grades nothing'); the claim itself holds on file 11 | - *Idle parts.* Deutsch counts superfluous features as a defect of an explanation (chapter 1, p.25). Here a commitment that does no work does not stop a candidate from being an account; Part VI reports it. |
  | Reach | C W34.1 | - *Reach.* Deutsch's reach is the power of an explanation to solve problems beyond those it was made for (chapter 1, p.28). Here the word is used once, for the jobs an account is held to (Part VI), and is not defined. |
  | Stated limits | B1 W57.1 + W32(b).1 | - *Stated limits.* Both books hold that a limit of scope needs an explanation (Deutsch, chapter 1, pp.27–28; Marletto, chapter 1, p.24). Here a stated limit is recorded, and what makes it appropriate is a criticizable part of the claim that the semantics does not certify (Part III). |
  | Selection | A W37.1 for 'Parts 0 and'; the claim holds on file 11's Part IV | (replace "(Parts 0 and IV)" with "(Part IV)") |
  | Surprise and problems | C W35.1-W35.3 | - *Surprise and problems.* For Deutsch a problem is a situation in which conflicting ideas are experienced, and a problem can arise without any observation (chapter 1, p.17). Here surprise is kept for selected transports (Part IV), and the recognized difficulty of a critical episode (Part X) is not defined. |
  | Elimination | C W40.1 | drop the sentence |

### W37.1 — Restore "blind" in Part 0's account of selection

- **STATUS:** applied
- **GROUP:** A
- **ITEM:** W37
- **FILE-11 LINE:** 15
- **WHERE:** Part 0, "What this document claims", paragraph 2 (L15), sentence 3. The skeleton's "L15 s2" is this sentence: L15 s1 is "Correspondence … is not a primitive here" and s2 is "It is a relation with a provenance".
- **REASON WORD:** erratum
- **KIND:** ORDER
- **CHECK:** check 1, FIX (kind only). The added words copy what L197 and L203 already state, so the change is ORDER, as 03 ruled the same place (M2, upheld). Declaring it would put a false line in the note. KIND is ORDER and the declaration is none; if a checker rules CLAIM, the drafted line below is used.
- **OLD:**
````text
A correspondence can be *selected*, produced by variation and survival on a history of encountered changes;
````
- **NEW:**
````text
A correspondence can be *selected*, produced by blind variation and survival on a history of encountered changes, with no represented target in that history;
````
- **DECLARATION:** none (ORDER, after check 1; listed in the record). If a checker rules CLAIM: "Part 0 again calls selection blind, and says what that means: the selection history holds no represented target, as Part IV states."
- **REASON:** W37 (source point 9; verify obs 9, CONFIRMED: "File 11 made the vocabulary clash worse"). File 10 L13 had "blind variation and survival"; file 11 dropped "blind" while the body keeps the blindness (L197: no member of the history represents t, H or the survival condition; L203: a selected transport has no represented target and no criticism in its history). The added words pin "blind" to the body's sense, so the ordinary wider use of "selection" (which includes choice by a critic) is not read into Part 0. The departure from the books' wider usage goes in the sources note (W38), not in the theory. KIND: 03 ruled the drop (M2) WORDING, but as a named close call, and all four readers ruled it CLAIM; under the strict rule this entry is CLAIM. The plan's expected ruling was WORDING, so the checkers may rule it down; declaring it costs one line in the note.
- **CASES AT RISK:** O11 (Monday's key-trying is variation and survival with no represented target): holds AGREE, toward if anything. N9 (selection puts the wing colour in what the moths inherit): holds. N11 (the teacher chooses among Jana's drafts): watched; the added words make plain that a chooser who represents what she wants is not a selection history in this sense, which fits the verdict's "the teacher's choice" and moves no mark I can find. No other O- or N-case turns on Part 0's wording of selection.
- **GAIN / LOSS:** GAIN: Part 0 and Part IV say the same thing in the same word as file 10, and "selection" cannot be read as criticism-by-choice. LOSS: None in the theory; "selection" stays narrower than ordinary use (recorded in the sources note).

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
- **WHERE:** Part II, "Kinds are edit-signatures" (L121). Two sentences are inserted after sentence 2, "A kind is an equivalence class of components under this relation.", the anchor W19's placeholder reserved. Sentences 1–2 are kept byte for byte. W30.1 appends its sentences after sentence 3; the two OLD texts do not overlap (skeleton conflict 1).
- **REASON WORD:** clarification
- **KIND:** CLAIM
- **CHECK:** not put to check 1 or check 2, which ran before S88 was settled. The text is the settled wording (`results/S88 Reading of Mimo's reply in three parts, and the settled positions.md`, F1, block 2; committed at 3ebb6d8), copied byte for byte. Checked by its drafter: the whole list applied by the program into a scratch draft with no refusal and no overlap, the new text read in place, and the guard rows worked below. No outside reader has seen this wording; the cross-examination of revision 2 (X1) must carry it.
- **OLD:**
````text
A kind is an equivalence class of components under this relation.
````
- **NEW:**
````text
A kind is an equivalence class of components under this relation. A component of \(E\) and a component of \(E'\) are of one kind on \(C\) when their signatures, read on \(C\) through \(\tau\) and \(\tau'\), coincide under a footprint bijection; Derivation 2 uses kinds in this sense. Derivation 1 makes the like comparison between a component \(k\) of \(E\), read on \(C\) through \(\tau\), and its anchor \(\lambda(k)\), read on \(C\) directly with its hidden ports projected away, up to the port translation.
````
- **DECLARATION:** Part II now defines when a component of one candidate's organization and a component of another's are of one kind on C: their signatures, read on C through the two candidates' transports, coincide under a footprint bijection. It says that Derivation 2 uses kinds in this sense, and that Derivation 1 makes the like comparison between a component, read through its transport, and its anchor, read on C directly with its hidden ports projected away.
- **REASON:**
  - W19 (S88 finding F1, settled UPHELD; plan 1.3.3, which takes the sentence after (K) with either wording of Derivation 2). (K) at L121 defines a kind for two components of one organization under one contract. No sentence says how a component of \(E\) and a component of \(E'\) are compared, and Derivation 2 compares them (the F1 reading, 3.4; Mimo's F1 point 3, kept). W19.2 needs the comparison stated.
  - **The second sentence** is the settled change 2. Derivation 1 (L546) compares a component of \(E\), read through \(\tau\), with its anchor subnetwork of \(D\), read on \(C\) directly; it does not compare a component of \(E\) with a component of \(E'\). The post-Atria sentence said "Derivations 1 and 2 use kinds in this sense" (Mimo's F1 point 4; the F1 reading's change B). Settling reworded the reader's proposal so that it names \(k\) and says which side is read through \(\tau\).
  - **Placed at the reserved anchor.** After this entry and W30.1 the paragraph reads: the definition within one organization; the equivalence class; the two new sentences; sentence 3 ("Kinds are therefore relative to the contract …"); W30.1's sentences on what a signature is built from. "Therefore" still follows from definitions that are both contract-relative.
  - **Notation, read in place.** \(E\), \(E'\), \(\tau\), \(\tau'\), \(\lambda\) and "hidden ports" are introduced in Parts IV and V (L191, L233, L235). Here Part II uses them before those Parts, with no pointer. Part II already points forward (to Part III, L121 s1), and "Derivation 2 uses kinds in this sense" names where the sentence is used. The settled wording is kept; the point is carried forward below.
- **CASES AT RISK:**
  - O10 holds AGREE, toward if anything under W30.1. Rosa's two thermostats are compared within one organization by (K); the new sentence compares components of two candidates for one question, which O10 does not raise.
  - O22 and O9 hold: the linkage's lead and the float and dial are compared within one organization.
  - N25 (O75), second question: watched under W19.2, which uses this sentence.
  - No other O- or N-case compares the components of two candidates.
- **GAIN:** Derivation 2's kinds across candidates have a definition, and Derivation 1's comparison is described as what it is.
- **LOSS:** Part II grows by two sentences, and it uses the notation of Parts IV and V before those Parts introduce it.

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
- **OLD:**
````text
Let \(t\) be selected on history \(H\) with contract \(C\). For an edit–boundary pair \((a,b)\in C\) actually occurring:

- the **expectation** is \(\operatorname{Ans}_S(\tau(a),\sigma(b))\);
- a **violation** occurs when fidelity fails at \((a,b)\);
- **surprise** is a violation at \((a,b)\notin H\).
````
- **NEW:**
````text
Let \(t\) be a transport with contract \(C\) and, where \(t\) is selected, history \(H\). For an edit–boundary pair \((a,b)\in C\) actually occurring:

- the **expectation** is \(\operatorname{Ans}_S(\tau(a),\sigma(b))\);
- a **violation** occurs when fidelity fails at \((a,b)\);
- **surprise** is a violation of a selected transport at \((a,b)\notin H\).
````
- **DECLARATION:** Part IV now defines expectation and violation for every transport, and keeps surprise for a violation of a selected transport at a pair outside its history.
- **REASON:** Worklist W35, variant (b′) (D3; plan 1.2; source point 13, verify obs 13, PARTLY CONFIRMED; M2). In file 11 the section opens "Let t be selected on history H". Expectation and violation therefore exist only for selected transports, and a constructed theory that fails has no violation to report. Under (b′), expectation and violation are defined for every transport, surprise is kept for a selected one, and H is introduced only where t is selected. Derivations 4 and 10 are unchanged and stay true word for word. Derivation 4 reads "A system can be surprised only if it holds a transport selected on a history H …" and its proof reads "Surprise is defined as a violation at (a,b)∉H". In Derivation 10, t_0 is selected on H_0. File 12's tested-history surprise (12:215–225, variant (c)) is not adopted (D3). The expectation keeps \(\operatorname{Ans}_S\): S is the organization the transport serves in this section, and constructed transports sit there too (L203). The OLD block runs over five lines so that the widened opening and the narrowed third bullet form one change: applied alone, either half would leave surprise ill-typed.
- **CASES AT RISK:**
  - O3 holds AGREE. Nadia predicts with a transport selected on the cards played, so her "often surprised" is still surprise in the technical sense. The verdict turns on construction (L401), not on surprise.
  - N18: toward on Q2 ("the swaying went against what both expected"). Rhea's constructed transport now has an expectation and a violation.
  - O-cases that mention expectation or surprise were searched; O3 is the only one. O5, O11, O24 and O48 are untouched: no expectation is at issue in them. Derivation 10's worked episode is unchanged.
- **GAIN:** A constructed theory that fails is violated in the text's own terms.
- **LOSS:** "Surprise" stays narrower than ordinary use.

### W35.2 — Part IV: a constructed transport is violated, not surprised

- **STATUS:** applied
- **GROUP:** C
- **ITEM:** W35 (b′)
- **FILE-11 LINE:** 225
- **WHERE:** Part IV, "Expectation, surprise, violation" (L225). One sentence is added after s4; s1–s4 are unchanged.
- **REASON WORD:** clarification
- **KIND:** CLAIM
- **CHECK:** check 2, FIX. File 11 says a system is surprised and a transport is violated, never surprised; NEW reads "is violated, and the failure is not surprise". N18 Q3's Dov half stays watched (his transport need not be read as selected). Companion entry W35.4 added.
- **OLD:**
````text
Whether the correspondence could have been otherwise at such a change is a fact about its population (Derivation 3).
````
- **NEW:**
````text
Whether the correspondence could have been otherwise at such a change is a fact about its population (Derivation 3). Expectation and violation are defined for every transport, surprise only for a selected one: a constructed transport that fails at a pair of its contract is violated, and the failure is not surprise; a violation the system represents can be a recognized difficulty (Part X).
````
- **DECLARATION:** Part IV now says that a constructed transport that fails at a pair of its contract is violated, that the failure is not surprise, and that a violation the system represents can be a recognized difficulty.
- **REASON:** Worklist W35 (b′). Plan 1.2 asks for surprise to be kept for selected transports "and said so". This sentence says it. It also joins a represented violation to Part X's recognized difficulty (W35.3). That is how the refutation of a constructed theory gets a place in the semantics without being called surprise (source point 13: "the refutation of a constructed theory is not surprise"). The sentence says "can be" because a violation is a recognized difficulty only when fidelity at that pair is a claimed obligation and the system represents its failure (W35.3).
- **CASES AT RISK:**
  - N18: toward on Q3. Rhea's bridge fails at a pair her contract covers, so her grounds are contradicted: a constructed transport is violated. Dov's copy, read as selected on the village bridge's record, meets a change outside that record. That is surprise, and nothing Dov had grounds for is contradicted. The Dov half depends on reading his transport as selected, and is watched.
  - O3 holds. No other O-case turns on a constructed transport's failure; O13 and O23 were checked.
- **GAIN:** The text says what the narrow sense of surprise leaves out, and where that goes.
- **LOSS:** None beyond W35.1's.

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
- **OLD:**
````text
and an identified set \(\Gamma\) of active commitments in \(E\).
````
- **NEW:**
````text
and an identified set \(\Gamma\) of active commitments in \(E\). The commitments \(\Gamma\) are components of \(E\), those the candidate offers as doing the work; the boundary values of \(E\) and the components of \(E\) outside \(\Gamma\), including any that assigns an input, belong to the named background of Part VI.
````
- **DECLARATION:** Part V now types a candidate's commitments: they are components of its organization, those the candidate offers as doing the work, and the organization's boundary values and its other components, including any that assigns an input, belong to the named background of Part VI.
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
- **CASES AT RISK:**
  - **O45: watched, with a risk away.** "Those the candidate offers as doing the work" meets the case's "The second is never described as doing anything".
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

### W34.1 — Part VI: reach defined

- **STATUS:** applied
- **GROUP:** C
- **ITEM:** W34
- **FILE-11 LINE:** 315
- **WHERE:** Part VI, "Hard-to-vary" (L315). One sentence is added after s1, before "More reach constrains variation".
- **REASON WORD:** clarification
- **KIND:** CLAIM
- **CHECK:** check 2, SOUND.
- **OLD:**
````text
\(\operatorname{Pres}(F)=\{v\in\mathcal V:\forall f\in F,\operatorname{Account}(E_v,f)\}\).
````
- **NEW:**
````text
\(\operatorname{Pres}(F)=\{v\in\mathcal V:\forall f\in F,\operatorname{Account}(E_v,f)\}\). The **reach** of \(E\) is the set of jobs \(f\) with \(\operatorname{Account}(E,f)\); it is fixed by \(E\) and the world, not by which jobs anyone has checked.
````
- **DECLARATION:** Part VI now defines the reach of an organization as the set of jobs for which it is an account, fixed by the organization and the world and not by which jobs anyone has checked.
- **REASON:** Worklist W34 (source point 5; verify obs 5, the fourth of "most worth acting on"). "Reach" occurs once in the theory (L315, "More reach constrains variation") and is never defined. File 10 dropped 00:383's definition. The plan chose to define reach from Part VI rather than restore 00:383 (1.2; 1.3.7 rank 4). The definition uses only Account and Part VI's "jobs", and adds no primitive. It also makes the source's "determined by the content of the explanation itself" a definition. "Not by which jobs anyone has checked" separates a content's reach from whether anyone has used it on a job. That remains a matter for Deploy, Attempt and Origin (Part X). The sentence stands before "More reach constrains variation", so the lemma's word is defined where it is first used. The other uses of "reach" in file 11 are verbs or "reachability" (L247, L333, L399) and are unaffected.
- **CASES AT RISK:**
  - N4: toward on Q1. The idea accounted for the midnight sun before anyone worked it out, because reach is fixed by E and the world. Q2 ("had anyone explained it") rests on Deploy and Attempt (Part X), which are unchanged.
  - N5 holds, and is watched. The rule's two readings are two organizations whose reach differs at the southern change. The definition does not say which organization the rule is, and the verdict's "cannot say which cue matters" rests on Derivation 3.
  - O-cases: none uses reach. O36 was checked: reach concerns the questions a written content answers, not unwritten candidates, so it does not pull against W58(i).1.
- **GAIN:** The lemma's key word has a definition.
- **LOSS:** "Reach" is a set of jobs, not the source's "problems solved beyond those it was created to solve". The difference goes in the sources note.

### W33.1 — Part VI: (E) tolerates a commitment that does no work; (B) marks it

- **STATUS:** applied
- **GROUP:** C
- **ITEM:** W33
- **FILE-11 LINE:** 315
- **WHERE:** Part VI, "Hard-to-vary" (L315). Three sentences are added after the last sentence; the paragraph's existing text is unchanged.
- **REASON WORD:** clarification
- **KIND:** CLAIM
- **CHECK:** check 2, FIX. Four defects: under the drafted test every commitment of L313's infinitary support "does no work"; "any support" could be read as "some support"; the declaration's "or" let one half of the test suffice; and "measure", as in W36.1. NEW scopes the label ("does no work by itself in the candidate"), states both halves for every support, says what happens when Γ is infinite, and reads "a separate matter, shown by Pres". Cases: O2's "this derives L275 s2's rule" is struck (circular); O19 is added, watched.
- **OLD:**
````text
More reach constrains variation; the containment need not be strict; counting jobs is not a warrant.
````
- **NEW:**
````text
More reach constrains variation; the containment need not be strict; counting jobs is not a warrant. (E) has no condition that each commitment do work. A commitment \(d\) does no work by itself in the candidate when every support stays a support after \(d\) is added to it and after \(d\) is removed from it: a candidate carrying \(d\) then meets (E) exactly when it meets (E) without \(d\), and \(\{d\}\) is critical in no support (B). When \(\Gamma\) is infinite, a block of such commitments can still be critical (Infinitary support). How hard an account is to vary is a separate matter, shown by \(\operatorname{Pres}\), and it grades nothing.
````
- **DECLARATION:** Part VI now says that (E) has no condition that each commitment do work; that a commitment such that every support stays a support when it is added and when it is removed does no work by itself in the candidate, leaves the candidate's standing under (E) unchanged and is critical in no support; that when the commitments are infinitely many a block of such commitments can still be critical; and that how hard an account is to vary is a separate matter, shown by Pres, which grades nothing.
- **REASON:** Worklist W33 (source point 2; verify obs 2, PARTLY CONFIRMED; M7). The source counts superfluous features as a defect. (E) accepts a candidate that carries a commitment doing no work, and Part VI reports such a commitment only through (S) and (B). The text never says this (worklist). The plan's wording, "(E) is fidelity: a commitment that does no work passes (E) …", is made exact in two places. (i) (E) is not only fidelity: non-circular dependence and non-vacuity are also conjuncts. So the sentence says instead that (E) has no condition that each commitment do work. That is true, because non-circular dependence asks only for some nonempty block. (ii) "Does no work" is given a test in Part VI's own terms: adding the commitment to any support, or removing it from any support, leaves a support. Both halves of the claim follow from that test: Γ is a support exactly when Γ∖{d} is, and {d} is critical in no support. The addition half excludes an interfering commitment (Part VI, Interference). The removal half excludes a redundant route (Redundant routes; L309), since removing it from the support in which it is the only route leaves no support. The sentence states no condition (plan 1.2; conflict 12). The departure from the source goes in the sources note (W38). It holds under every W20 option, because it is stated through (S) and (B), not through the wording of non-circular dependence (skeleton conflict 11).
- **CASES AT RISK:**
  - O36, O45 and O47 hold. P in O36 is critical, not idle. The second spring in O45 fails the removal test: removing it from the support in which it is the only spring leaves no support. So it is a route, not idle. The locked room in O47 fails the addition test, so it is interference, not idle.
  - O2 holds. The bell part does no work for the tide question. The candidate meets (E) with it exactly when it meets (E) without it, and without it the almanac restates the answer (L275), so it fails either way. This derives L275 s2's rule.
  - N1: toward if the sun-god sentence constrains nothing, or is not among the active commitments. Watched: if it is read as a second component that keeps the tilt steady, it is either a redundant route or an unfaithful component. As a redundant route it fails the removal test, and the verdict "not part of what explains" moves to DISAGREE. As an unfaithful component it fails the addition test; that is interference, and "Tomas explains" is at risk. Which reading applies turns on how Γ is typed (W20, held).
  - N25 does not move: the difference between dog and turtle is a matter of Derivation 2's kinds (W19, held). N2 does not move: the patch was fitted after the fact, which is the historical index. N7 and O8 hold: scope is untouched.
- **GAIN:** The split between (E) and (B) is stated, with a test for idleness that excludes interference and redundant routes.
- **LOSS:** The theory now says openly that it tolerates idle parts, which the source counts as defects.

### W40.1 — Part VII: why the absent structure appears is a separate question

- **STATUS:** applied
- **GROUP:** C
- **ITEM:** W40
- **FILE-11 LINE:** 337
- **WHERE:** Part VII, "Explanations that remove structure" (L337). One sentence is added after the last sentence, which is kept byte for byte, attack pointer included (D9).
- **REASON WORD:** clarification
- **KIND:** CLAIM
- **CHECK:** check 2, FIX. "Why does X appear?" used a bare X where the paragraph defines only "X-effect"; NEW reads "the question why it appears". Inserted before "This is the semantics' treatment …", the new sentence took over the antecedent of "This"; the entry is now anchored on the paragraph's last sentence, which it keeps byte for byte, attack pointer included (D9).
- **OLD:**
````text
This is the semantics' treatment of eliminative explanation; it is offered as adequate and is listed under attack (B) in Part XV as a place where it may not be.
````
- **NEW:**
````text
This is the semantics' treatment of eliminative explanation; it is offered as adequate and is listed under attack (B) in Part XV as a place where it may not be. Where the absent structure appears to be present, the question why it appears is a separate question with its own target and contract (Part III): an account of the absence neither answers that question nor needs to, and a bare denial, which offers no component that responds to a change in what produces the appearance, is not an account of it.
````
- **DECLARATION:** Part VII now says that where an absent structure appears to be present, why it appears is a separate question with its own target and contract, which an account of the absence neither answers nor needs to answer, and of which a bare denial is not an account.
- **REASON:** Worklist W40 (M6; source point 15; the source holds that to deny a thing exists one must also explain why it seems to). Part VII's treatment asks nothing about the appearance. The plan takes a clarification, not a condition (1.2). The appearance question is another question in Part III's sense (L153: "Two questions with the same D and different (C, Q) are different questions, and an answer to one is not an answer to the other"). So an account of the absence is judged on its own contract and needs no answer to the appearance question. A bare denial has no component that answers to changes in what produces the appearance, so it cannot meet (F1) or non-circular dependence on that second question. The pointer "attack (B) in Part XV" is not touched (D9); group A's check W27.0 found it CORRECT. W49 (absence and prevention) is left out.
- **CASES AT RISK:**
  - N22: toward. Wren offers no component for the appearance question. Yuri offers one, machinery that reads memories and produces reports; the question does not ask whether that candidate is adequate.
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
- **OLD:**
````text
**Functional transport.** If \(\pi\circ S_a=T_a\circ\pi\) for every generator \(a\),
````
- **NEW:**
````text
**Functional transport.** Let \(S_a\) be a target process and \(T_a\) a represented process for each admitted generator \(a\). If \(\pi\circ S_a=T_a\circ\pi\) for every generator \(a\),
````
- **DECLARATION:** none (WORDING: the typing follows from \(\pi:X_D\to X_E\) and from Part II's composition of admitted edits; listed in the record). If a checker rules CLAIM: "The functional transport result now says that \(S_a\) and \(T_a\) are target and represented processes for each admitted generator."
- **REASON:** W24 (trial A3 = Mimo M7, VALID). 00:518: "Suppose a target process \(S_a\) and a represented process \(T_a\) satisfy … for every admitted generator \(a\)." 00's sentence is restored in file 11's "Let … If …" form, with 00's words for the typing. It must land before W31 (held), whose \(S\) and \(T\) refer to these processes; the two entries touch different lines (L351, L361).
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

### W22.1 — Define \(p_\delta\) and \(\mathcal E_c\) in (K1)

- **STATUS:** applied
- **GROUP:** A
- **ITEM:** W22
- **FILE-11 LINE:** 373
- **WHERE:** Part IX, "Bearing" (L373), sentence 2; the display (K1) at L376 is unchanged.
- **REASON WORD:** erratum
- **KIND:** CLAIM
- **CHECK:** check 1, FIX. "The criticism's interpreted structural account" is file 00's term. File 11 calls such a pair an explanatory candidate (L233), and a criticism can exist when (K1) fails, so the drafted words would call a failed candidate an account (against C's W36.1). NEW now reads "the explanatory candidate (Part V) that the criticism offers for p_δ".
- **OLD:**
````text
Let \(p_\delta\) be the question about the defect. Then
````
- **NEW:**
````text
Let \(p_\delta\) be the question whether \(z\) has \(\delta\) in respect of \(p\), and \(\mathcal E_c\) the explanatory candidate (Part V) that the criticism offers for \(p_\delta\). Then
````
- **DECLARATION:** (K1) now defines its terms: \(p_\delta\) is the question whether the target has the alleged defect in respect of \(p\), and \(\mathcal E_c\) is the explanatory candidate the criticism offers for that question.
- **REASON:** W22 (trial M2, VALID: \(\mathcal E_c\) occurs once, undefined; neither \(p\) nor \(z\) appears on the right of (K1)). 00:620: "\(\mathcal E_c\) is the criticism's interpreted structural account." The gloss of \(p_\delta\) brings \(z\) and \(p\) into (K1) through \(p_\delta\).
- **CASES AT RISK:** None found. Checked: N11 (Kasia's written faults are criticisms; Jana's bare marks are not), O27, O40 and O50 (the robot notices the test's assumption); none turns on (K1)'s terms.
- **GAIN / LOSS:** GAIN: (K1) is well typed and can be evaluated. LOSS: Nothing.

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
- **KIND:** WORDING
- **CHECK:** check 1, SOUND.
- **OLD:**
````text
declared as a substantive input when aesthetic value is claimed.
````
- **NEW:**
````text
taken as a substantive input when aesthetic value is claimed.
````
- **DECLARATION:** None, because the entry is WORDING. It is listed in the record.
- **KIND AS DRAFTED:** WORDING, given W6.2 and W6.4. With them in place, both texts send \(\mathcal N\) to the same place: an input the semantics takes and does not derive, under L514's rule for a missing input. If W6.4's clause on the normative relation is dropped, rule this entry CLAIM and declare it as: "Part XI no longer calls the aesthetic normative relation a declared input."
- **REASON:** Worklist W6 (03 §8 item 4: \(\mathcal N\) is a "declared input" at L27 and at L447). If this clause were left, it would bring back, one sentence after W6.2, the category that W6.2 removes. The skeleton scopes W6 at L447 to s2 only. This entry goes one sentence past that scope, for the same reason, and it can be dropped without harm to any other entry.
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
- **OLD:**
````text
Build depends on histories and (E). (N), (G) depend on Deploy and Build. (P), (EK) depend on (G), (E), Deploy.
````
- **NEW:**
````text
Ownership depends on histories and a declared boundary, and owned capability on Ownership, (CT1) and a declared continuity (Part XII). Build depends on histories, Ownership and (E). (N), (G) depend on Deploy and Build. (P), (EK) depend on (G), (E), Deploy; (P) also on ProducedBy and on the declared obligations with their occasions, and ProducedBy on histories and their active routes.
````
- **DECLARATION:** Part XIV's dependence order now places Ownership on histories and a declared boundary, owned capability on Ownership, (CT1) and a declared continuity, Build on Ownership, and (P) on ProducedBy and the declared obligations with their occasions, and ProducedBy on histories and their active routes.
- **REASON:**
  - Worklist W7 (XR6: the order lists "none of the definitions that rest on one (L419, L433, L465)"; 03 §5; plan 1.3.1).
    - Ownership (L419) rests on the declared boundary.
    - Owned capability (L467) rests on Ownership and on the continuity and resource contract.
    - ProducedBy (L433 s4) rests on active routes read from histories (L371).
    - (P) rests on \(O\) and \(P\) with their occasions (L433 s1).
    - Build (L401) is defined on an owned subhistory.
  - **Left free for W20.** Two sentences are left untouched: "(E) depends on those." and "(S), (B), (D) depend on (E)." W20's held rider can be entered at either one later, through B1, without overlapping any entry here (skeleton conflict 3).
  - **Kept.** L518's last two sentences are kept word for word: M49, declared against file 10 by W3.
  - **Not corrected.** "(P), (EK) depend on (G), (E), Deploy" is kept, although (P)'s definition does not use (G), (E) or Deploy. As a dependence it is an over-statement and does not harm well-foundedness. Correcting it lies outside W7.
- **CASES AT RISK:**
  - O49 stays AGREE. The order now puts Ownership before owned capability, which the verdict ("The definition goes in a circle") needs. This secures the mark and moves nothing.
  - O37 stays AGREE. Its circle is ruled by L518's last sentence, which is unchanged.
  - O35 and O38: the obligations with their occasions are L514's unchanged input.
  - The boundary rows are as in W7.3: restated, not changed.
  - No N-case cites the dependence order. This was checked.
- **GAIN:** Derivation 6's proof has an order that reaches the declared inputs and the definitions that rest on them.
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
  - **O36 holds AGREE.** The unwritten route with another premise cuts \(D\) at a different place, so it is a different candidate, and P stays critical in each route as written.
  - **O24 holds AGREE, toward if anything.** The two wiring arrangements are different organizations (L25). File 11's Consequence ("Underdetermination of an account by a contract is not a failure of the semantics to decide …") could be read to make two arrangements that agree on every tested pair one account. The new Consequence covers only anchor assignments. The verdict rests on Derivation 3 (L562; W17.3), which is untouched.
  - **O10 holds** (see W19.1).
  - **N17 (O67): toward on the first two questions; the plan predicts no mark.** Answers A and B cut \(D\) at different places, the electrons against the stored factors. The added paragraph makes them different candidates with one answer profile, so each can tell the asker something the other does not. File 11's "one account … their components are pairwise of one kind" pulled against that. The third question ("B explains, and A does so only in a thin sense") is not reached.
  - **N25 (O75).** The first question holds; it rests on non-circular dependence (W20.2). The second question is watched.
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
