# The Semantics project, in plain words

*Written for the owner on 24 September 2026. It tells the same story as the project's log (`records/Semantics - project story.md`), without the technical shorthand. Every special word is explained in the word list, and each thing keeps one name all the way through. Nothing in it waits on a result still out: every reply that was asked for has come back and been read.*

## The goal

The project tests a theory of what makes an explanation a real explanation. The theory is written down in numbered files. The aim is to find out where the theory gives the wrong answer, fix it, and check the fix, using ordinary situations where a thoughtful person already knows the right answer.

In short: try hard to break the theory, repair what breaks, and keep an honest record of every step, including what went wrong.

## Where things stand

- **File 11 is the authority, and that ruling is now final.** File 11 is the first revised version of the theory. Claude ruled that it replaces file 10, the older version, after testing both on 52 cases. Two outside models, Atria and Mimo, then tried to overturn that ruling. Nothing they said changed it. On one case, O5, Mimo said the ruling was wrong; a fresh Claude subagent went back to the theory's text and found that the ruling holds.
- **Three faults in the theory itself were found and confirmed.** One of them is serious: a proof in the theory is wrong, and the theory's own list of what would defeat it names exactly that kind of fault. Repairs are written for all three.
- **The theory was compared with its two source books.** Most of the comparison's points held up, some only in part, and one fell. Twenty-five new cases were written from the books, and 24 of them have agreed answers. One more case, aimed at the weakest sentence of an earlier fix, also has an agreed answer.
- **A second revision is drafted, cross-examined and redrafted.** It is a list of 55 small, exact changes to file 11. Both outside models cross-examined it in five pieces. 24 of the changes were challenged: 10 were reworded, 14 were kept as they were, and none was dropped. A third draft with every one of those decisions applied has been made, and an independent check of it passed on every point.
- **Nothing is frozen yet for the second revision,** and it has not been tested on the cases. Whether to freeze it and test it is the owner's decision.
- **The work sits on a side branch**, with a draft pull request (number 1) against main, not on main itself as decision S6 says. Whether to merge it is also the owner's decision.

## How the pieces fit

Each piece below says what it does and what it hands on to the next.

1. **The theory files** (`authority/`). File 10 is the older version, kept unchanged forever. File 11 is the first revision. A second revision would become file 13. *Hands on:* the text that every test is run against.
2. **The cases** (`tests/`). Short everyday situations, each with the answer a thoughtful person would give. *Hands on:* the questions the theory must answer.
3. **The testers.** Claude subagents that read one version of the theory and mark every case. Each tester works alone and never sees the expected answer. *Hands on:* a mark for every case.
4. **The auditors.** Two outside models, Atria and Mimo, which check the testers' marks and also give their own reading of the cases without seeing the expected answers first. *Hands on:* a second, independent opinion, from models that did not write the theory.
5. **The ruling.** Claude reads everything, goes back to the text of the theory for every disputed case, and makes the ruling. The owner made Claude the one who decides (decision S13). *Hands on:* a ruling, with every reason written down, in a Results file.
6. **The cross-examination.** Atria and Mimo are asked to attack Claude's ruling, or a draft. Anything they say is re-checked by a fresh Claude subagent that did not make the ruling or write the draft. *Hands on:* either a ruling or draft that survived attack, or a corrected one.
7. **The revision.** Faults found along the way become a list of exact changes, applied to the theory by a program so that nothing slips in unrecorded. *Hands on:* a new version to test from the start.
8. **The record** (`records/`). The log of what happened, the owner's decisions in the owner's words, the lessons (only failures), and a status summary. *Hands on:* a true account for anyone who comes later.

## Word list

- **Theory.** The written account of what makes an explanation real, in numbered parts.
- **Authority.** The version of the theory that is currently in force and under test. Once used in a test it is never edited; a new version gets a new file number.
- **File 10, file 11, file 13.** File 10 is the older version of the theory. File 11 is the first revision. File 13 would be the second revision; it does not exist yet, only drafts of it.
- **Case.** A short everyday situation, written so that a thoughtful person can say what is going on.
- **Thoughtful person's verdict.** The answer a careful, reasonable person would give about a case. It is fixed before any test, so the theory can be checked against it.
- **Mark.** A tester's one-word reading of a case: AGREE (the theory gives the thoughtful person's verdict), SILENT (the theory does not settle it, because something it needs is missing), SPLIT (the theory can be read two ways), DISAGREE (the theory gives a different verdict).
- **Toward and away.** A change between versions moves a case toward the thoughtful person's verdict (better) or away from it (worse). A change away is the thing the tests most need to catch.
- **Claude subagent.** A separate copy of Claude given one job, with its own instructions, working alone. The owner allows at most five at a time.
- **Outside model.** A language model made by someone else. This project now uses two, Atria and Mimo, which Claude calls directly, because they did not write the theory and may see its faults differently. Earlier rounds used the owner's own outside model, which the owner ran by hand.
- **Tester.** A Claude subagent that reads a version of the theory and marks every case, without seeing the expected answers.
- **Control.** A copy of a test run on the older version, which the tester cannot tell apart from the real one, so that differences caused by the reader can be told apart from differences caused by the theory.
- **Auditor.** An outside model that checks a tester's marks, case by case.
- **Blind reading.** An auditor's own reading of the cases before it is shown any expected answer.
- **Round.** One complete test: the plan, the runs, the reading of the results.
- **Plan.** The written design of a round, including what Claude expects to happen, fixed before the round starts. Changing it afterwards means writing a new version of the plan, openly.
- **Prediction.** What the plan expects to happen, written down before the data exists and kept away from the testers.
- **Reading rule.** A short note, written before a reply is opened, that says how the reply will be read and what could change because of it. It stops the reader from bending the rules to fit what came back.
- **Determination.** Claude's final ruling on a round, made from the text of the theory, with reasons. In these notes it is called the ruling.
- **Cross-examination.** Asking the outside models to attack a ruling or a draft, and then re-checking every attack that lands.
- **Checker.** A fresh Claude subagent that takes one challenged change, reads the challenge and the theory, and decides: keep the change as it is, fix it with new exact wording, or drop it.
- **Re-reading.** When an outside model says a ruling on a case is wrong, a fresh Claude subagent that did not make the ruling goes back to the theory's text and rules on that case again.
- **Derivation.** A numbered proof inside the theory: a short argument that something follows from what the theory says.
- **Defeat list.** A list inside the theory (its Part XV) of the kinds of finding that would show the theory is wrong. A false proof is one of them.
- **Counterexample.** A worked example that meets everything a claim assumes and still breaks the claim.
- **Claim change.** A change to the theory's wording that lets a reader conclude something they could not conclude before. These must be declared openly.
- **Undeclared claim change.** A claim change that a new version made without saying so in its opening note.
- **Erratum.** A correction of a slip in the writing, so that the text says what it was meant to say.
- **Clarification.** A sentence added so that a passage is read the way it was meant, without changing the rules.
- **Worklist.** The list of every known problem that a revision might fix, before any choice is made.
- **Change list.** The exact list of changes, word for word, that a program applies to file 11 to make the next version.
- **Draft 3.** The third draft of the second revision's text, made after the cross-examination, with every checker's decision applied.
- **Freeze.** To fix a draft as a numbered theory file (here, file 13), after which it is never edited, and to test it.
- **Candidate case.** A new case whose answer has been agreed but which has not yet been used in a round. It gets a permanent number (O53 and upward) only when a round uses it.
- **Effort.** A setting that tells an outside model how hard to think before answering: high or medium.
- **Token ceiling.** The most an outside model is allowed to write in one reply, counting its thinking. When the thinking uses it all up, no answer comes out.
- **Attempt.** One try at a call to an outside model. A call is allowed a fixed number of attempts.
- **Pass.** One full run of a call, with all its attempts. Normally a call gets one pass; a second pass needs a note, written before it is sent, saying why.
- **Disconnect.** An attempt where the connection dropped and nothing came back at all.
- **Container restart.** The working computer this session runs on restarted. When it came back, the route it used to reach the outside models had moved, and calls already under way could not reach them.
- **Repository.** The shared store of all the project's files and their full history.
- **Main, branch and pull request.** The repository keeps its agreed copy on main. Work in progress can sit on a separate copy, a branch, until it is merged into main. A pull request is the request to merge it; a draft pull request is one not yet put forward for merging.
- **Scratch space.** A private working folder that belongs to one working session and can be lost when the session ends. Nothing the record depends on should stay there.
- **Revision.** A new version of the theory made by changing the old one; it gets a new file number.
- **Log entry.** One numbered paragraph in the project's log (S80, S81 and so on). The numbers are shared with the other two projects in the repository, so some numbers are skipped here.

## What was tried and what happened

Before S80, the project had built its way of testing over many rounds: file 10 was fixed as the authority, 52 cases were collected over several rounds with the owner's own outside model, and file 11 was written to repair one known wrong answer (the case O48). A five-reader review (S78) said the two-step test design made sense with repairs.

**S80. Does the hard-to-vary skill help?** The owner gave access keys for three outside models and asked whether a writing aid called the hard-to-vary skill helps a reader find errors. Claude planted eight errors in a copy of file 10 and planned a comparison: readers with the skill, readers with a dummy text of the same length, and readers with nothing. The outside models criticised the first plan and were right: it would have been unfair, so it was changed. The owner then cut the test short to a quick verdict. *Failure:* Mimo's thinking reached its token ceiling on every run and it wrote no answer at all, six times out of six. *Failure:* the log entry was given the wrong number.

**S81. The main round is built.** A fresh test of file 11 against all 52 cases was built, with file 10 run alongside as a hidden control, and with the outside models checking the testers. The prediction, kept out of every test: only case O48 changes, and it changes for the better.

**S82. The owner's verdict on the skill.** From the unmarked results, the owner judged the skill not worth it as an aid for finding errors (decision S14). The results were stored; the full marking was never run.

**S83. Changes before the main round ran.** The owner asked that all analysis be done by one particular Claude model, so the six first tester runs, made by another, were set aside and done again. Each outside model's token ceiling was raised to the highest it allows. A third outside model was tried as an extra auditor and not added, because it reported no problems by choice. Mimo found several real holes in the theory, which went onto the list for a later revision. *Failure:* the program meant to catch a tester seeing what it should not threw out all six first runs for harmless reasons, because it had only been tried on made-up examples.

(Numbers S84 to S86 belong to no entry here. From S87 on, each entry takes the next number shared across the three projects.)

**S87. The main round is decided, and cross-examined.** Two Claude testers and two outside auditors read file 11 and file 10 against all 52 cases. Claude ruled every case from the text first, before opening any reply, and only then read the replies.
- *The result:* file 11 stands as the authority. Case O48 moved to the thoughtful person's verdict, as predicted. One more case, O45, also moved the right way, through a sentence the revision's note did not mention. No case moved the wrong way. But the note that said "nothing else changes" was wrong: 41 other places changed what the theory claims without saying so, though no case shows any of them doing harm. Three answers in an older result were corrected, and seven places where file 11 refers to another part of itself point to the wrong place.
- *The cross-examination:* Atria tried to overturn the ruling on the seven cases most open to doubt and could not; it found no case that moved the wrong way. Mimo's attempt at the whole task failed, so it was split into three pieces; one piece came back and agreed on its two cases, and the other two failed. The three cases of the first failed piece were then sent to Mimo one case at a time, and all three came back. On two of them, O17 and O30, Mimo agreed with the ruling. On the third, O5 (Greta and her dough), Mimo said the ruling was wrong: it read the theory as refusing to say whether Greta's limit is sensible even though she gives her reason. A fresh Claude subagent that had not made the ruling went back to the theory's text and found that the ruling holds: the theory gives a verdict when the reason is stated, and stays silent only when the reason is missing, as it is in another case, O1. Atria had tried the same objection and rejected it on the same grounds. So no ruling changed, and file 11's standing is final. Mimo looked at five of the seven doubtful cases; the other two, and the overall conclusion, were looked at by Atria alone.
- *A partial replacement check:* Mimo's audit of one tester had failed twice, so it was sent again in four pieces. Two pieces came back, covering half the cases; they agreed with the ruling, and the two small differences were re-checked from the text and did not hold.
- *A check of the effort setting:* sending the same task to Mimo at medium effort made it think more, not less, and its answers differed from the high-effort answers on 36 of 52 cases. With only one try at each setting, this says nothing firm about the setting, but it does show how much one model's readings can vary from run to run.
- *Failures:* Mimo's audit of one tester is missing, so that tester had one outside check instead of two. Twice a reading rule was written after the replies had already arrived (though before anyone opened them). A Claude subagent that was told to wait for a long run stopped waiting after a minute. The frozen plan was changed several times before a new version of it was written. The owner's instruction about medium effort was applied too widely at first. Two of the owner's decisions had Claude's own words mixed into them. The container restarted while two of Mimo's one-case checks were under way, and both failed for that reason alone; they were sent again and came back. One re-reading was asked for on the mistaken belief that Mimo had objected to a ruling; it changed nothing. Two of the Claude subagents writing up these checks looked at earlier write-ups before finishing their own, which the reading rules asked them not to do; they said so, and the re-readings themselves were made without them. The work sits on a side branch, not on main as decision S6 says; merging it is the owner's call.

**S88. Three faults in the theory itself.** While the main round was being decided, Claude subagents checked holes Mimo had reported, and a third subagent argued the theory's side as hard as it honestly could. Three faults stood, in both file 10 and file 11:
- one proof (Derivation 2) claims more than it proves, and a counterexample breaks it; by the theory's own defeat list, this counts as a real defeat;
- one formula leaves out conditions that an earlier version had stated;
- one key term is never defined, and on one reading some case answers flip.

Both outside models cross-examined these findings. Atria agreed with two and partly with the third, and found a fourth fault, in file 10's Derivation 3, which file 11 had already fixed. Mimo's whole attempt failed, so it was split into three pieces, one per fault, and all three came back. The settled result: the first fault stands in full; the second and third stand in a narrower form. Exact repairs are written for all three, and they became changes in the second revision, where the outside models saw them again (S90). *Failure:* the reading rule for Atria's reply was written after the reply had arrived (though before it was opened).

**S89. The theory against its source books.** The owner named two source books, by Deutsch and by Marletto (decision S19). A Claude subagent compared the theory with the books and made fifteen observations; a second tried to knock each one down. Six held, eight held in part, and one fell. The comparison suggests saying where the theory comes from and where it departs from the books, and adding some explaining sentences, rather than adding new rules. A third book, by Pinker, was named as worth exploring; reading it was stopped by a safety check after its first chapter, and that was not worked around.

From the books, 25 new cases were written. Their answers were fixed by Claude subagents that had never read the theory, two at a time, over three rounds, the later rounds without the books in front of them. 24 answers were agreed; one case was set aside because the two could not agree. One older case aimed at the weakest sentence in the fix to Derivation 3, called D3-T, finally had its answer agreed by two separate pairs; it becomes candidate case O76, and its files are now saved in the repository. *Failure:* its files, like some other working files, sat for a while only in the scratch space before they were saved.

**S90. The second revision, drafted, cross-examined and redrafted.** Every known problem went on a worklist (56 items, and the plan added two more). A plan chose what to fix and how the second revision would be tested. Claude took the eleven decisions the plan left open. The result is a change list of 55 exact changes to file 11; the new version's note declares every change that alters what the theory claims, and also lists the 42 places where file 11 changed its claims without saying so. A program applies the list to file 11 and refuses if anything does not match.
- *The cross-examination:* the draft was cut into five pieces, and each piece was sent to both Atria and Mimo, ten calls in all. All ten came back. Every change either model challenged went to a fresh Claude checker. 24 changes were challenged or looked at: 10 were reworded (fixed), 14 kept as they were, and none dropped. 31 changes were challenged by neither model; that does not prove them right, only that no one found fault with them. Mimo said nothing at all about 15 of the changes.
- *The third draft:* every checker's decision was applied to the change list in one go, word for word, and the program made draft 3. After the decisions, 49 of the 55 changes are declared as changes to what the theory claims. A Claude subagent that had no part in drafting or checking then checked draft 3 on five points: that every fix is exactly the wording the checker gave; that nothing else changed; that the program still refuses planted errors; that file 11 itself was not touched; and that six key cases still get the thoughtful person's answer. Every point passed. No outside model has seen the ten reworded changes.
- *Failures:* the draft was first sent to Atria as one large task, and it failed after more than two hours, mostly on disconnects. The container restarted while five of the ten pieces were still under way, and all five failed for that reason alone, along with two of Mimo's one-case checks from S87; all seven were sent again under a note written first, and all came back. In the first batch of readings, two checkers were told to save their decisions under the same file name, so one decision's file was lost; its outcome survived in a summary, and the change was checked again in the next batch. On two changes the two checkers disagreed, and the Claude subagent writing up the batch, not a third checker, chose which wording to use, from the checkers' own reasons; the owner can ask for a fresh checker on either. Some working files behind the change list are still only in the scratch space.

**Lessons from these entries, in short.**
- Large single tasks for the outside models kept failing; splitting them by finding, by case or by group of changes worked, and should be done from the start.
- Disconnects wasted many attempts, sometimes most of them; the number of attempts and the time allowed must allow for them.
- The limit of five Claude subagents at a time was kept by the machine's own cap, not by a count Claude kept itself.
- A reading rule must be written and saved before the task is sent, every time.
- After the working computer restarts, every call that was under way must be started again, and a call that failed only because the connection was cut does not count as an answer.
- Every file that a checker or tester writes must have a name of its own, so that no one's work can overwrite another's.

## The next step

1. **For the owner to decide:** whether to freeze draft 3 as file 13 and run its test round, the full test, which needs many calls to the outside models, or a smaller one; and whether to merge the branch this work is on (draft pull request number 1) into main.
2. **If the owner says freeze and test:** first save the remaining working files in the repository; settle the small points the cross-examination passed on without a decision; have the test plan itself cross-examined; try each outside model at full size; then freeze file 13 and the plan, and test file 13 on all the cases, the 52 old ones, the new candidates and D3-T.
3. **Still waiting from before:** the reply to the round with deliberately planted errors (S79), from the owner's own outside model; the marking of the skill test; the first 32 lines of an early results table, which were never recovered.
