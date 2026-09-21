# Checked reasoning language - Lessons

Only cases where something failed while being made or tested, and how it was fixed.

1. The first round-trip picture was laid out sideways with a loop. It came out very wide and too small to read on a phone. Fix: rebuilt it top to bottom, with no loop and fewer boxes.
2. Whimsical hands out pictures at one fixed width. A wide diagram therefore gets tiny text. Fix: keep each diagram narrow, and let wide ones scroll sideways in the page.
3. After a wording change on a Whimsical board, the picture link kept showing the old wording. Fix: build the board again to get a fresh picture, and remove the old board.
4. The improved skill's description ran 28 characters over the length limit and failed the validator. Fix: trimmed two trigger phrases; validator passed.
5. Opening a paper's web page was refused (too many page requests). Fix: searched for the paper by its exact title and read the summary that came back. Cost: only the summary and introduction were read.
6. The skill said "look at what a tool does, not what it says", and I could not: desk research only reaches what makers say. Fix: added the tag "claimed" so this shows in every write-up.
7. Installing s(CASP) the standard way failed twice: the package list was stale, and the add-on server refused the older Prolog version. Fix: refreshed the package list, then took s(CASP) straight from its makers' code store.
8. One command hung for five minutes because s(CASP) was waiting for keyboard input. Fix: every run now gets a time limit and no keyboard.
9. The driver misread s(CASP)'s answers because of a trailing comma, so the first tomato report wrongly said "jump" and "nothing known". Fix: strip the comma. The first output was kept as it came.
10. A quote mark inside a paragraph's name broke its wording file. Fix: removed the quote marks.
11. s(CASP)'s printout drops the number from names like "number_9", so two buses printed as one. Fix: renamed them in the ledger. Recorded as a trap.
12. A check added while working on paragraph A raised a false alarm on the fault-free paragraph B. Caught only because the checker had been frozen. Fix: patch 1.
13. The frozen checker could not tell "how we know" from "what produced it", and called a real cause idle in paragraph E. Fix: patch 3.
14. After patch 4 the same departure was reported twice, once wrongly pointing at the sentence "Sally threw the ball", because s(CASP) found two routes to it. Fix: keep one answer per exception, the one using fewest lines. All ledgers rerun.
15. Two of my own test commands failed on quoting slips. Fix: rewrote them. No result was affected.
16. Both research connectors returned "no approval received" on the first try, because the permission prompt on the owner's phone was not answered in time. Fix: stopped, told the owner, reran when asked. No memory or web search was used to fill the gap.
17. alphaXiv allows two searches per message and returns only titles and opening lines. Fix: made each search broad, and tagged those results as thinner than "claimed".
18. The first run of rig 2 ran out of time (20 seconds) and, as a side effect, wrongly flagged the bounce. A ledger line said "the ball hits the wall only if it could move toward the wall", which made the laws refer back to themselves. Fix: chain lines must name the earlier happening they depend on. Recorded as a trap.
19. The first report said "the sally" and "toward the he". Fix: display names for things; direction wording corrected in the patched copy.
20. The frozen rig raised false alarms on an influence with no body (the wind) and on a verb missing from the shape book (kick). Found only because cases were added to break it after a clean sweep. Fix: patches 1 and 2 of rig 2.
21. No execution failures in logs 18 to 20. Recorded so the gap in numbering is not read as something missing.
22. Rig 1 raised a false alarm (JUMP) on the owner's Markus paragraph. Cause: patch 3, made three stages earlier, tested BECAUSE only on what MAKES things happen, and nobody had recorded that this gave up "a reason to expect". Fix: patch 6 (SINCE). A list of what each patch gives up is now kept in the project story.
23. Patch 6, fitted to the two-step Markus paragraph, named every conclusion of a seven-step chain as "the point" and judged steps alone. Predicted before the run. Fix: patch 7.
24. The first form of patch 7 broke the Markus report (two reasons for one conclusion were counted as one step, and the failed one overwrote the good one). Caught by rerunning every ledger. Fix: a conclusion stands if any step for it holds.
25. The first form of patch 7 also listed four "final" conclusions, because it looked for a conclusion that is nobody's reason, and the reasons pass through general lines. Fix: the final conclusion is the one argued for last.
26. Both clauses Claude wrote for round 4 had faults that Claude's own checks missed and the other model found: one conflated "loose" with "fitted"; the other stated its passing condition on the outcome alone, which the thing it was meant to exclude also met. Fix: revised clauses for round 5, and a line in the skill: run any test you write on the thing it is meant to catch and on its nearest innocent neighbour.
27. The first draft of prompt 30 contained one negative word in an instruction ("when they cannot"). Caught by the program that searches each prompt for negative wording. Fix: reworded as "when either one is missing".
28. Rulebook 23 contradicted rig 1 on BECAUSE: rule 11 allowed the effect to be tested through any general lines, while the rig (since patch 3) tests BECAUSE only on lines that MAKE. Found by the other model's audit, not by Claude. Cause: the rulebook was written from memory of the rigs and never checked line by line against what they actually do. Fix: pending (sort the 25 findings; correct the wording that the rigs already get right).
29. Two of Claude's shell commands in log 34 failed on a bracket the shell did not accept, which cut a rerun short. Fix: reran the comparison as its own command; all results were then obtained. No finding was affected.
30. Rig 2 gave a false alarm ("a change from nothing") when a thing's response to a press was not stated. Found by running the other model's case F01. Fix: rig 2 patch 3.
31. In the joined run, the checker's own comparison of strengths ("far smaller than") was printed as one of the writer's unstated assumptions. Fix: such comparisons are left out of that list. All paragraphs rerun, unchanged.
32. The set-aside rule (patch 13) gives a wrong "holds" when a result has two stated causes and only one is withdrawn. Found by a case written to break it. Not fixed; recorded as a limit and as a trap in file 36.
33. A told story written as a named what-if case produced a false contradiction (text T07-B of the other model's corpus). Predicted before the run. Fix: rig 1 patch 15, a told world stands alone.
34. A plan about which the ledger said nothing was reported as a kind mistake that "cannot work". Found by comparing with the corpus answer key for T10-B. Fix: rig 1 patch 16, "cannot tell".

## Traps
- Assuming a picture has updated because the board has. Look at the picture itself before using it.
