# D3-T: what it tests and where it came from

*What D3-T tests and where it came from, with how the first wording differs from the recorded text. Written by a Claude subagent on 23 September 2026 as a note for the orchestrator. This file travels in no brief: no author, tester or auditor is given it, and the authors who fixed the verdict never saw it. Moved into the repository on 23 September 2026 from the session scratchpad, where it was `d3t/why.md`, with only this paragraph added. Paths in it are relative to `Semantics/`.*

This note is for the orchestrator. The authors who fix the verdict never see it. They see only `prompt.md`.

## What it is

D3-T, "The controller that failed yesterday", is the attack case in the S72 Stage 2 auditor's fix card for Derivation 3. It sits in `Semantics/results/S72 Stage 2 audit - return/04 Fix card for Derivation 3.md`, field 4 ("Its weakest sentence, with one case aimed at it"), under the heading `#### D3-T — The controller that failed yesterday`, marked "Written by: me". The S72 Stage 2 instruction (`tests/S72 Stage 2 audit - check the testing return, …`, line 42) required the card to name "its weakest sentence with one case aimed at it".

Recorded text (fix card, field 4):
- **Situation.** "An automatic tester keeps lamp controllers that stay dark with one switch off and light with it on. Ivo has only two controller designs in the stated population. Both are physically permitted, and they differ at an untried joint setting of two switches. One design failed the earlier switch-on test and was discarded; only the other survived. Ivo points to the discarded design as proof that the survivors are undecided at the untried setting."
- **The auditor's thoughtful-person verdict.** "The discarded design is a permitted alternative, but it is not another survivor of this testing history. Its different response at the new setting does not undo the old failed test."
- **The restated theory's verdict.** The antecedent fails because the second design did not survive the same history, so there is no underdetermination among that history's survivors. This agrees with the thoughtful verdict "without asserting the remaining controller's truth at every future setting".
- **POKE (two controls).** (1) If the alternative also passes the switch-on test and keeps its different untried response, there are two survivors and the record is undecided. (2) Relabelling the alternative while keeping its failed test changes nothing.

## What it tests

- **The target sentence.** The first boxed sentence of the qualified Derivation 3: survival on a finite history leaves the value at an unseen pair underdetermined only when another admitted, realizable member of the same population also survives that history and has a different value there. That qualification is the S72 restatement that file 11 carries (worklist W16 places it at F11 L562–566).
- **The failure it would catch.** A reader who counts an imaginable or physically permitted alternative as another survivor, without checking whether it passed the history. D3-T grants physical permission and a differing untried response, and withholds survival.
- **The item in the Revision 2 worklist.** W17, "What 'surviving on H' means". It asks whether that means a member of \(\mathcal T\) that meets the survival condition (the Sel reading), or any transport that is faithful on H. The Revision 2 plan (line 107) takes W17 and lists D3-T among its guards, with O48, O24 and O11. The plan's line 106 leaves W16, noting that "D3-T tests W17 instead".
- **Its neighbours in the case book.** O24 (two arrangements that both pass and differ at one reachable untried setting, so the record has not chosen) is the positive control. O48 (the only differing arrangement lies outside the population) is the case that forced the restatement. D3-T is a third way to lack a rival: the rival is in the pool and can be built, but it failed.
- **Expected answer (not shown to the authors).** No. The discarded design failed the tested check, so it is not something that passed. Its different untried response does not show that what passes is undecided there. With only two designs in the pool and one of them failed, the test has picked the kept design, and with it that design's response at the untried setting. A fresh author may add that the untried setting is still untried. That fits the auditor's verdict, which does not claim the kept controller is right at every future setting.

## Its path through the records

1. **S72.** Written by the Stage 2 auditor, who had read the theory. The report addendum (`results/S72 Stage 2 audit - return/05 Report addendum.md`, line 136) calls it "self-authored": it "tests the survival qualification; it is not a new outside case or another independent changed-case warrant". S75 adopted the card's two sentences (D3-1, D3-2) and did not mention D3-T.
2. **S78.** Readers 2 and 5 flagged it (`results/S78 Two-stage pattern review - return/02 Reader 2 - stage2.md`, lines 88–93 and 249–251; `05 Reader 5 - rivals.md`, lines 100 and 234–236). Reader 2 wrote: "The card names its weakest sentence and then the round drops the test of it". Its scenario is that file 11 becomes the authority while "D3-T, the only case in the record that would have caught it" sits unrun. Reader 5 noted that the auditor wrote the wording, wrote the case that tests it, and was audited by nobody. Readers 1 and 4 (lines 92 and 99) credit the card for carrying it. `results/S78 Results - …` item 12 (line 28) records the finding, and group A repair 7 (line 64) reads "D3-T entered as O53 with its verdict frozen". The project story's S78 entry (`records/Semantics - project story.md`, line 84) lists "D3-T as O53" among the group A repairs.
3. **S81.** Not applied. Both the first and second S81 plans (`tests/S81 Plan - file 11 against every case, rebuilt with the S78 repairs, …`, lines 9, 120, 148; `tests/S81 Plan - second version, …`, lines 24, 183, 213) record: "D3-T stays out of the case book until Claude fixes its verdict". Row A7 gives the reason: the verdict was written by the S72 auditor, so it had not been fixed by the determiner. The same row says: "It is the one case aimed at the qualified Derivation 3's weakest sentence, so it is the first case to add; held for the orchestrator." The S81 determination file 04 (line 418) lists it as not entered, and the S81 case book holds only O1–O52.
4. **Revision 2 (drafts of 23 September).**
   - The worklist has W53, "S78 group A leftovers (D3-T as O53 not entered)": enter or drop (lines 114 and 1020–1022).
   - The plan routes it through the N-case method (lines 140, 453, 459–462, 642, 694 D8, 712, 785, 793, 811). Two fresh Claude authors who have never read the theory fix its verdict from the situation. The rules are agreement in substance and neither rating low. If they agree before the freeze, it enters as O76; otherwise it goes to "Not tested".
   - The plan's drafted question (line 460): "Does the discarded design show that what survives the testing is undecided at the untried setting?"

## How `prompt.md` differs from the recorded text

- **Title and id.** The heading is the neutral "Two lamp controllers". The recorded title stresses the failure, and round 2 of the N-cases already used neutral titles. There is no id: "D3" names Derivation 3, and O76 applies only if the case is adopted.
- **Theory words replaced.**
  - "in the stated population" became "to choose from; there are no others".
  - "physically permitted" became "can be built".
  - "differ" became "respond differently".
  - "survived" became "passed and was kept".
  - "the survivors" and "what survives" became "what passes the testing". "Survives on H" is the very phrase W17 tests, so the prompt does not use it.
- **One clause added.** "and discards the rest" makes plain what happens to controllers that fail.
- **The question.** It is the plan's drafted question with "survives" changed to "passes". Everything else in it is unchanged.
- **Left out.** The verdict, the theory's verdict, the POKE and every reference to how or why the case was made.

## Caveats

- The recorded verdict is the S72 auditor's, and that auditor had read the theory. It is not a fixed verdict until the two fresh authors agree.
- The case is close to analytic: once "passed" is read as "passed this test", the answer follows almost at once. It is a guard for how the theory reads its own word. It is not a hard case for a thoughtful person, and agreement from the authors is likely.
- "Undecided" is kept from the record. An author could read Ivo's claim in a weaker sense ("the untried setting has not been checked"), which is true. The question's "Does the discarded design show …" keeps the author on the thrown-out design as evidence. A reconciler should still check that both authors answered that point, and not only the weaker one.
