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

That was done for **41 checkable claims** in Astra's reply (a **claim** here is one statement about what Avida does or where in its code something is). **37 hold, 3 hold in part, none fails, 1 was not checked**; two of the 37 were answered by the save-and-reload test (section 4). Five were also tried out by running Avida: Astra's own save-and-reload files work; its commands for testing programs one by one work; and Avida does refuse the new commands Astra invented, as Astra said it must.

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

**An example first.** One of the two environments tested was COMMON TASKS PAY LESS, where each task is paid out of a store that fills a little every time step and runs down when many programs do that task. Take the store for the task NOT at one break between pieces: at the end of the piece it held 125.7. The next piece started with exactly 125.7, so nothing was lost. But in the first time steps after the reload it went 52, 52, 95, 107, 114, 112, 97, 76, 68, 87, 115, 137, 169: big swings, where in an unbroken run it moves by a few in a hundred per step. The likely reason (not tested): every reloaded program starts its instructions from the top at the same moment, so they all do their tasks in waves until they drift out of step.

**What was done.** Two of S113's environments, FIXED GRADED (the nine tasks rewarded) and COMMON TASKS PAY LESS, three seeds each (a **seed** is the number that starts Avida's dice; different seeds give different runs of the same experiment). Each was run twice: in ten pieces of 1,000 time steps by S113's own program, unchanged, and in one go. What would count as the pieces changing things was written down and saved before anything ran. In the first 1,000 steps the two ways matched exactly, as they should.

**What it found.**
- **FIXED GRADED: nothing moved the same way in all three seeds.** The number of tasks most programs do, how common each task is, and the count of generations came out higher in pieces in some seeds and lower in others. But the two ways differ from each other about as much as two seeds do: in one seed EQU was done by about two programs in three in pieces and by none in the run made in one go.
- **COMMON TASKS PAY LESS: a lean in one direction, mostly below the lines set beforehand.** In all three seeds the runs in pieces had fewer copies made per time step (5 to 10 in a hundred fewer), and fewer tasks done by most programs just after each reload; over the second half, about two fewer common tasks in two seeds and the same number in the third. By the rule written beforehand, none of these counts as a change; it is not ruled out either.
- **One line was crossed, but it turned out to be the ruler.** The count of **generations** (how many times, along a line of descent, a program has been copied) came out 15 to 30 in a hundred lower in pieces, in all three seeds of COMMON TASKS PAY LESS. A further check, added after seeing this, reloaded the same program population once and watched it: it went on making copies at the same rate as without the reload, yet its generation count still came out lower. The reason is how Avida counts: a reload sets every program's count back to 0, so a line of descent that had been copied many times more than others loses that lead in the count. So most, perhaps all, of this difference is in the count, not in what the programs do.

**What it means for S113.**
- Its results for FIXED GRADED can be read as if run in one go, within the lines set beforehand; the same is assumed, not shown, for ONE HARD TASK ONLY, NO TASK REWARDS and FIXED LARGE LIST. Because one run can differ this much from another, only the spread over three seeds says anything.
- Its COMMON TASKS PAY LESS results may come out a little low from the pieces: any comparison that turns on one or two tasks between it and another environment should be read with that in mind.
- Its generation counts should not be used as they are, nor compared with page 111's runs; the number of copies made per time step is the safer measure.
- For GROWING LIST the breaks are where the new tasks are added, so this test cannot separate the two.

## 5. Tested, not tested, unsure

**Tested:** 41 claims of Astra's reply against Avida's code, five of them also by running Avida; the added and removed instructions in every file of S111 to S113 and the brief; the saving and reloading, in two environments, three seeds each, 10,000 time steps, both ways, with a check that one piece gives the same result when run again, and the further check that reloaded the same program population six times.

**Not tested:** the other four S113 environments; more seeds or longer runs; how long the swings in the stores last after a reload (they were watched for 20 time steps only); Astra's new environments, which need changes to Avida's code; the one Astra claim left unchecked (whether a reward already earned lasts after the target changes).

**Unsure:** whether COMMON TASKS PAY LESS really comes out lower in pieces (three seeds lean that way, below every line set beforehand); why the swings in the stores happen (the reason given is a likely one, not tested); how much of the lower generation count is left once the counting is allowed for.

**Changed from the plan, and said so in the record:** the further check was added after the first results were seen; one of the lines set beforehand (about the stores at the first time step) assumed Avida prints the store before anything runs, which is wrong, so it is reported both by its letter and by what it actually shows; copies per time step at the ends of pieces were compared though no line had been set for them. Also: the task given to me said pages 111 and 112 described only the copying mistakes; page 111 did describe the added and removed instructions, so its dated line says so rather than correcting it.

## 6. One next step

For S113's reading, which is being written now: take this audit into it, so that COMMON TASKS PAY LESS is compared with caution, generations are not used as they stand, and FIXED GRADED is read through the spread over its three seeds. Which of Astra's new environments to try, if any, is yours to choose; each needs changes to Avida's own code first.
