# Probe pass 02e: the same ledger with the range written C1 to C3. Expected: passes.
C1. "Version 7 answers the support questions correctly 92% of the time on our 500-question set."
C2. "Version 7 is better than version 6 on that set."
C3. "Version 7 costs less per answer than version 6."
Source: the model team's weekly note, "Evaluation" section.

| F | Claim | Falsifier | Status | Receipt | Effect on claim |
|---|---|---|---|---|---|
| F1 | C1 | A grader who did not build version 7 marks at least 60 of the 500 answers wrong | missing | none | C1 held if the team's own marking is right |
| F2 | C2 | On the same 500 questions, version 6 wins at least as many questions as version 7, counted one by one | missing | none | C2 held if the gain is not luck |
| F3 | C3 | The billing log for one day shows a cost per answer for version 7 at or above version 6's | reported | weekly note: "cost per answer down 18%" | none, as reported |

| Q | Claims | Answer | Where or why |
|---|---|---|---|
| Q1 | C1 to C3 | missing | F1, F2: one question set, one week |
| Q2 | C1 to C3 | does not apply | considered answers handed in with the questions; the note says the set has "no reference answers shown to the model" |
| Q3 | C1 to C3 | missing | F2: version 6 run under the same conditions is not reported |
| Q4 | C1 to C3 | does not apply | considered two measures agreeing by construction; correctness and cost are measured apart |
| Q5 | C1 to C3 | missing | F1: 92% hides the worst topic |
| Q6 | C1 to C3 | missing | F2: same set, but versions may differ in prompt as well |
| Q7 | C1 to C3 | missing | F1: correct by the team's marking, not by the customer |
| Q8 | C1 to C3 | missing | F1: version 7 was tuned on questions like these |
| Q9 | C1 to C3 | missing | F2: 500 questions, one run each |
| Q10 | C1 to C3 | missing | F1: the note does not say when the pass mark was set |
| Q11 | C1 to C3 | missing | F1: marking done by the team that built version 7 |
| Q12 | C1 to C3 | covered | F3: "cost per answer down 18%", as reported |
| Q13 | C1 to C3 | missing | F1: the note does not say whether questions were dropped |

Claim as it stands: on one set of 500 questions marked by the builders, version 7 scored 92%; held if an outside grader agrees.

Next test: an outside grader marks a random 100 of the 500 answers (F1).
