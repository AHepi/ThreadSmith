# S78 Results - the two-stage pattern reviewed by five readers: what stands, what is corrected, what to repair before S76

*Written by Claude on 22 September 2026 from the five returns held unchanged in `S78 Two-stage pattern review - return/`. The owner's words (decision S10): "use 5 Opus 5 subagents on extra effort to review whether the review patterns make sense. Arm each with the hard to vary skill", and on the target, "I meant the two stage testing". The pattern under review is decision S7: each round runs as two stages by two fresh agents, testing then audit, with Claude reading both and determining the results.*

## How it was run

Five fresh Opus 5 agents at extra-high effort, in one workflow run (wf_ee79e5f3-ef4), each working alone. Each read the hard-to-vary skill first (`HV Skill/authority/hard-to-vary/SKILL.md` and its modules the-idea-in-depth, testing-against-cases, question-bank, reporting), then the pattern's files: decision S7, story entries S72 to S76, the single-stage S71 the split replaced, the S72 and S76 instructions for both stages, the pack read-me and prompt, `Instruction pack - build.py`, both S72 returns, S75, files 10 and 11, and file 24. Each led with one lens and covered the whole: Stage 1 as a test; Stage 2 run on what it should catch and its innocent neighbour; independence from the author; the determination step and the S76 prediction; the pattern against rival methods. Each returned a structured report: the question frozen, parts with one of the eight marks, findings with a fully stated scenario and the evidence in S72, whole-pattern checks, what would tighten it, what it does not show, one next step. Tokens across the five: 967,347; wall clock 34 minutes. The readers' word counts are in the return folder's manifest.

## The verdict

All five: **makes sense with repairs**. None said it does not make sense; none said it makes sense as it stands. Reader 5 put the agreement in one sentence: the two-stage pattern is a sound checking pattern carrying the name of a finding pattern. As a check it works, and the S72 returns show it working: an identifier on every verdict, 119 quotations resolved, the audit moving O24 from CHANGED to SAME and O52 off its original pair, a fix card that runs its restatement on the forcing case and on cases it must leave alone. As a finder it can subtract findings and has never added one, because the answer travels in the packs, the auditor reads the answer before writing its own, and the audit's reach is set by the labels of the return it audits.

## What the readers found, checked by hand

Each item names the readers who found it and what Claude checked against the files.

1. **The answer travels in the pasted part.** The S72 Stage 1 and Stage 2 instructions say at line 5, above the owner line (71 and 55): "found one place where it does (O24 and O48 against Derivation 3). This stage finds every such place." Stage 1 returned exactly those two rows CHANGED and no others. The S76 Stage 1 instruction carries "Predictions, fixed before the run" at line 5, above the owner line at 57; its column 3 asks for S72's verdicts quoted; and `build.py` puts S75 and the S72 Stage 2 return into the S76-1 pack (lines 32 and 47). Readers 1, 3, 4, 5. Checked. Lesson 50 had already recorded the mechanism on an earlier round.
2. **The auditor reads the answer first.** Stage 2 Part 1 fixes the print order: Stage 1's verdicts quoted, then the auditor's own reading. The auditor's return says so itself (file 01, line 16): "not a claim that I had never seen Stage 1's answer." Readers 1 to 5. Checked. Nineteen of nineteen agreement on both columns is therefore one reading read twice, and the pattern holds nothing that tells that apart from two readings that met.
3. **The audit's reach.** Three of the four triggers are Stage 1's own labels. The residual every-fifth sequence is fixed, printed in the return (file 01, line 14), and that return is in the S76-1 pack. The clause is ambiguous ("of the remaining rows ... counting from O1" while O1 is a mandatory SILENT row), and two of its eleven indices, O1 and O21, fall inside the mandatory set, so the fresh sample was nine rows of forty-two, not eleven. By Claude's count nineteen rows name an amendment in column 5 and ten of them were left unaudited, among them O37, O39 and O49, which make the very judgement the audit overturned on O24, in the other direction. Readers 2, 3, 4, 5. Checked.
4. **The audit can only subtract.** No heading in either stage's return admits a change Stage 1 did not mark, and heading (11)'s three lists have no home for a defect that no amendment cures. The one round's yield is two removals. Readers 1, 2, 5.
5. **SAME and CHANGED were defined by the tested agent, after the data.** The instruction's column 5 says only "SAME or CHANGED between columns 3 and 4". Stage 1's preamble (file 01, line 8) supplies the rule; eighteen rows carry "clarification is not itself a changed verdict"; Stage 2 restates it; S75 calls it "the instruction's own terms". Readers 4, 5. Checked. Corrected below.
6. **"Explicit already" was not established.** W08's warrant is [T-E16; T-C03]; T-C03 is H65, tagged in Stage 1's own quotations file "Not authority text". File 10's Repair line (438) says nothing of occasions; file 11 (427) adds "each as a stated condition over stated occasions, and a protected condition is lost exactly when it fails on an occasion it covers." So at least one wording line put into file 11 a sentence file 10 does not carry, and file 11's note that one claim changes is a prediction under test, not a fact. Reader 4. Checked. Corrected below.
7. **The reference verdicts are the author's.** Cases O15 to O52 were written by Claude with the verdict fixed first (story S63, S65, S70); "an outside author" in the read-me means "not you, the agent"; no mark lets either agent dispute a case, and column 6 charges every disagreement to the theory. Readers 2, 3, 4. The counterweight readers 1 and 3 record: O48, the round's one finding, came from a Claude-written case and went against the theory Claude stewards, and the outside judge at S73 reached it from file 10 alone.
8. **R2 is copy-checked.** Of 119 quotations, 76 resolve to earlier returns and 43 to file 10; VERBATIM on the 76 means the copy matches the copy. Readers 1 to 5; S75 already says the R2 file has never been in the repository. The Derivation 3 finding does not need R2: file 10's proof step "any other admitted relation" already assumes what the claim omits, and S73 found it without R2. The repair is to report the two counts apart wherever the number appears.
9. **S76 imports an unaudited baseline.** Column 3 quotes S72's verdicts, thirty-three of which no auditor opened, and S76 Stage 2 audits column 4 only. Readers 3, 4, 5. Checked against the S76 instructions.
10. **R2 J's second qualification has no case.** Its Part VIII sentence on the accumulated-error bound with unmatched initial states was named unresolved by Stage 2, is absent from S75, and is unchanged in file 11; the word "initial" occurs in neither file 10 nor file 11. Reader 3. Checked. A gap in the case set that S75 should have listed.
11. **The negative-wording search stopped after S62.** Two instruction-bearing negatives sit in the pasted part of S76 Stage 1: "with no amendment read in" and "with no row changed except". Reader 5. Checked by the same search.
12. **Smaller, each found by one or two readers:** the fix card is written by the auditor and checked by nobody, and its attack case D3-T never entered the case set (readers 2, 5); the coverage file that picks the next rows is unaudited (reader 2); the manifests record no model or date, so the fixed requirement of a fresh agent leaves no trace (readers 2, 3); the read-me's "Give every theory verdict under the earlier version" contradicts S76 (reader 1); `build.py`'s single cut strips the reading guidance together with the owner block (reader 1); five gauges read zero at once with nothing asked of the zero (reader 5); Part 4 commissions the fix card before Part 1 decides whether the row survives (readers 1, 3).
13. **The pattern has never been run on a theory known to be wrong.** The project's own Lesson 26 asks that of every test it writes. Reader 3.

## Where the readers erred, and where Claude differs

- Reader 3 wrote that in all 52 rows column 6 is "No disagreement" or SILENT. O48's column 6 records the disagreement in full: "The bare claim asserts a differently valued survivor at every unseen pair, while the proof's 'any other admitted relation' does not establish one in this population." Reader 1 had it right: one disagreement in 52.
- Reader 4 wrote that forty-four rows carry the boilerplate sentence. The count is eighteen. The finding stands at eighteen.
- Reader 2 counted twenty-two rows naming an amendment in column 5; Claude counts nineteen. The ten unaudited rows include the three that matter.
- Reader 5's repair of reversing the print order is enough only if Stage 1's row stays closed until the auditor's reading is written, which the instruction must say and the return must show. Reader 3's form, a first pass with Stage 1's columns withheld and a second pass with them opened, is the one to take.
- The seeded-error trial (reader 3) is the one repair that tests the pattern instead of patching it. It costs one round by two agents on a doctored file 10, and it is the owner's call.

## Corrections to S75

S75 stands as written; these are read with it.

- Point 11, "Stage 2 is right on the instruction's own terms": the rule that column 5 asks whether the case's own verdict changes was Stage 1's, adopted by Stage 2; the instruction stated no rule. O24's settlement as SAME stands on its reasons; its status is a reading rule adopted at S75, after the data, and dated there.
- Point 2, the twelve wording lines "explicit already": the bin tested that the bare and amended readings agree, as Stage 2's own file 05 says, and did not test that file 10 says the sentence. W08 is sourced to a clause. File 11's count of one claim change is therefore under test in S76, and the S76 difference table with its CLAIM and WORDING marks is where it is tested.
- Line 23, "the audited sample of every fifth row agreed 19 of 19": nine of the nineteen came from the fixed sample; ten were rows Stage 1 had itself marked out.
- "What this does not show" should have listed R2 J's Part VIII qualification, untested by any case.

## What stands

The substance of the S72 result: one amendment changes one verdict, O48 against Derivation 3, reached by Stage 1, confirmed by Stage 2, corroborated from file 10 alone by the outside judge at S73, and independent of R2's wording because file 10's proof already assumes what its claim omits. Nothing in the five reports touches that finding, and four readers say so in as many words. What the reports touch is the confidence that nothing else moved: the forty rows that agree with the thoughtful person were never put under the pressure the two changed rows faced.

## Repairs, in the order they bite

All inside `Semantics/`; the owner's fixed parts (two stages, fresh agents, zips, returns held unchanged, push to main) untouched.

**A. Before S76 is run.** The packs are in the owner's hands and, as far as the record shows, unrun.

1. Strip the answer from the tested agent's pack. Move "Predictions, fixed before the run" below the owner line, which `build.py` already strips; the prediction stays frozen in story S76. Drop S75 and the S72 Stage 2 return from the S76-1 pack and keep them for S76-2. Column 3: worked from file 10 with the passage quoted for the thirty-three rows S72 left unaudited, quoted from S72 for the nineteen it audited, each row saying which.
2. Stage 2 Part 1 in two passes: first, for the sampled rows, the auditor's own readings worked from the source with Stage 1's columns withheld; second, Stage 1's row opened, quoted, and marked AGREE or DISAGREE. The residual sample chosen by Claude after the Stage 1 return arrives, written into the Stage 2 instruction as row identifiers, the every-fifth clause dropped.
3. The mandatory set gains three kinds: every row whose column 4 or 5 names a sentence of file 11 that differs from file 10 (in the S72 form, an amendment); every row whose column 6 is anything but a plain no-disagreement or a plain SILENT; and a stopping rule, that a DISAGREE widens the audit to every remaining row of that kind.
4. The definitions written into the instruction before the run: SAME and CHANGED as two columns (does the case's own verdict change; does the claim of the passage it rests on change); SILENT with a recorded search, the Parts read and the words looked for.
5. Two headings added to Stage 2, each with its count stated even at zero: "Changes Stage 1 did not mark" and "Wrong, with no amendment that fixes it"; and a CASE DISPUTED mark for either stage with the required field "what in the case, and not in the theory, decides this", for Claude to rule on.
6. Quotation counts reported in two: source-checked against the authority; copy-checked against an earlier return, marked CHAINED.
7. One manifest line: the model, the date, and "opened in a chat holding no earlier stage of this round". The negative-wording search restored in `build.py` at pack time, printing its hits. The read-me sentence made conditional on which file the column is read against. D3-T entered as O53 with its verdict frozen. Part 4's fix card made conditional on Part 1 confirming the row.

**B. The test of the pattern itself** (reader 3's next step). A seeded-error round: file 10 copied, one error planted in a Part four cards touch and one in Part VIII where no card does, the two-line list sealed in the story first, the S72 packs run unchanged against the doctored file, and what each stage reported written beside the sealed list. That single round says whether the pattern can fail a wrong theory and where its reach stops.

**C. Cases out of the determiner's hands** (readers 2, 3). A block of cases written by an agent that has never read file 10, verdicts sealed until the return is in, mixed into the table unmarked. This changes who writes cases and is the owner's call.

## What this does not show

Five readings by one model family at one effort; reader 3's own point about shared blind spots applies to this review. No reader ran a stage; the verdict "makes sense with repairs" is a reading of the pattern's files and one completed round, not a run of the pattern on a known-wrong theory. The readers were given the lenses by Claude, who wrote the pattern; the lenses name where to look and not what to find, and the findings that came back include four against Claude's own determination S75.

## Next step

The owner's word on A (rebuild the S76 packs with the repairs before the round runs) and on B (the seeded-error round). Claude can make the A edits and rebuild both packs on the word; S76 as sent stands until then.
