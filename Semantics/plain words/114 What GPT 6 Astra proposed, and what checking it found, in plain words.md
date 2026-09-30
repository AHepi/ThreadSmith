# What GPT 6 Astra proposed, and what checking it found. In plain words

*A note first. Written on 30 September 2026 by a Claude agent, for you. It uses your Avida terms (the list you gave, kept in "Semantics/records/Semantics - Avida terms, given by the owner.md") and none of the words you asked to be removed, except inside quotations. Everything here ran inside Avida's simulated computer; nothing that copies itself ran on a real one. The full records are "Semantics/results/S114 Checking GPT 6 Astra's reply.md" (every claim, with where in Avida's code it was checked) and "Semantics/results/S114 Restart audit - results.md" (with its plan, written before anything was run, beside it). Nothing in the theory was changed. **No GLM check was made of this job**, on purpose: the job is itself a check of an outside model's claims against Avida's own code, and its main finding, the restart audit, is to be used in reading S113's results, which GLM will check.*

---

## 1. What Astra proposed, in a few lines

You sent GPT 6 Astra the brief about Avida execution environments that keep a program population learning new things, and brought back its reply. In short, Astra:

- **said first: check the saving and reloading before reading any learning curve.** S113 runs each experiment in 50 pieces of 1,000 time steps; at the end of each piece the whole program population is saved to a file and the next piece is a fresh Avida that loads it. Astra read Avida's code and said the file does not keep everything, so the reloading might itself change what happens. It proposed a test: the same run in pieces and in one go, side by side.
- **criticised the six S113 environments one by one**: most of them reward a list of tasks you or I wrote down beforehand, so a rising count of tasks shows the programs meeting our list, not the environment making up new problems.
- **proposed three new environments** where the problems come from the programs themselves: (1) the world asks for an answer different from the one most programs currently give; (2) one group of programs makes up small puzzles and another group has to solve them; (3) one group builds mazes and another has to find its way through. And (4) a fourth, where some programs act as **judges** choosing between other programs' answers, and the judges can change too.
- **proposed ways to measure learning that do not use our list**: test later program populations on earlier problems (do they still solve them?), on problems nobody rewarded, and on how fast they pick up a new problem.
- said plainly that (1) to (4) **need changes to Avida's own code** (from about 150 to 1,800 lines each) before they can run; only the save-and-reload test runs on Avida as it is.

## 2. What held, and what did not, when checked against Avida's code

**An example first.** Astra said that when Avida reloads a saved program population, each program starts over "with fresh CPU state": its working memory empty and its place in its own instructions back at the start. To check this, the part of Avida's code that reloads was read line by line. It makes a brand-new program for every saved one and fills in, of what matters here, only three things from the file: its instructions, where it sits, and how much processor time it gets. Nothing about where it was in its work is filled in. So the claim holds.

That was done for **41 checkable claims** in Astra's reply (a **claim** here is one statement about what Avida does or where in its code something is). **35 hold, 3 hold in part, none fails, 1 was not checked**, and 2 were for the save-and-reload test to answer (section 4). Five were also tried out by running Avida: Astra's own save-and-reload files work; its commands for testing programs one by one work; and Avida does refuse the new commands Astra invented, as Astra said it must.

What mattered most:
- **What a reload loses** (all of Astra's points hold): each program's working memory and its place in its instructions; the dice Avida throws (the file has no record of them, and S113 starts each piece with new dice); and the resources that run down (the file has none; S113's own program carries their levels over by hand).
- **Four more losses Astra did not name**, found while checking: after a reload, every program's **count of generations goes back to 0**; its **record of the tasks it did** is emptied until it finishes its next copy; every program of the same instruction sequence gets the **same average processor-time share**, averaged over that sequence's whole history; and Avida's own count of births shows **a burst of about 3,600 "births"** in the first time step, which are only the reloaded programs.
- **The three "in part"**: Astra wrote that a reload could refill a resource that had run down; in Avida it actually sets it back to its starting level, which in S113 would be empty, not full (S113 avoids this by carrying the levels over). Astra named the wrong file for adding new commands (they are added in a neighbouring file). And Astra assumed our Avida is exactly the released version 2.14.0; ours is a later copy, but in everything checked the code is the same.
- **One Astra point that confirms S113's design**: Avida records a task done by a program even when the task earns nothing, so S113's way of counting all 77 tasks while rewarding only some of them works as intended.

## 3. A correction: the added and removed instructions

**An example first.** When an Avida program copies itself, each instruction it copies has a small chance (in the usual setting, 1 in 133) of coming out as a random instruction instead: a copying mistake. But Avida also does something else, once per copy: with a chance of 1 in 20 it **adds** one random instruction somewhere in the new copy, and, separately, with a chance of 1 in 20 it **removes** one. Both can happen to the same copy (1 in 400).

This was on in S111, S112 and S113, as it is in Avida's standard settings. The question was whether our files said so. Checked file by file:
- **Page 111 and S111's records did say so**, correctly ("at each split the world also, one time in twenty each, adds one random instruction to the copy or takes one away"). The only looseness is "or": the two are separate chances.
- **S113's plan said so**, correctly.
- **Page 112 did not mention it**: it names the runs only by their copying-mistake rate. S113's program note and the brief sent to Astra did not mention it either, which is why Astra called our settings unknown.
- The note written into your decisions record when you brought Astra's reply said S111 to S113 "did not describe" it; that is not right for S111 or for S113's plan.

**What it changes: no number.** S111's numbers were measured with the adding and removing on. Its test of how programs stand up to change tried only swapping one instruction for another, never adding or removing one, and it said so. S112's removals were all made in Avida's private test computer, where no change happens. One dated line saying this has been added at the top of pages 111 and 112; nothing else in them was touched.

## 4. The save-and-reload test, and what it means for S113

RESULTS_PENDING

## 5. Tested, not tested, unsure

TESTED_PENDING

## 6. One next step

NEXT_PENDING
