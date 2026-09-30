# What the routine runs from Astra's replies found. In plain words

*Written on 30 September 2026 by a Claude agent, for you, **before GLM's check** of the work behind it; GLM's points, once weighed, may change it, and this note will then say so. It uses your Avida terms (the list you gave, kept in "Semantics/records/Semantics - Avida terms, given by the owner.md") and none of the words you asked to be removed, except inside quotations. It follows the plan of runs in file 115 (its cheap, routine part) and one run proposed when GLM's check of file 113 was weighed. The full record is "Semantics/results/S116 Routine runs from Astra's replies - results.md" (with a data file beside it); the plan, written and saved before anything was run, is "Semantics/results/S116 Routine runs from Astra's replies - how they will be tested, written before running.md". No new word from you since "Noo too many agents"; one agent did all of it. Nothing in the theory was changed.*

---

## 1. What happened, and what it means for your question

You asked: "what kind of execution environment can use these machines to progressively learn how to do new things".

**First, the one run from file 113 that was still learning at the end has stopped.** It was a run of the environment that pays for all 77 sums from the start: 28 sums common at update 40,000, 37 at 45,000, 41 at 50,000. It was let go on for 25,000 more updates, in the same way as before. It stayed at exactly 41 the whole time, while its programs kept changing (about 3,200 different programs at every look). So in every environment tried so far, the programs learned part of the list someone wrote in advance and then stopped.

**Second, some of what the programs learned only works in their own world.** An example: in one run of the growing list, 2,377 of 3,489 programs do NOT (and copy themselves) when handed three numbers in the order their world always uses. Hand them the same three numbers in another order, and only 62 to 370 of them still do. In another run, most programs cannot even copy themselves when handed small numbers instead of the large ones their world gives. So a population can look able to do many sums in its own world and much less outside it. The world's habits became part of what the programs rely on.

**Third, what an environment pays for is what it adds; paying less for a common sum did not help a rare kind of program.** Details in section 4.

## 2. The words used, with an example

As on the earlier pages: **Avida** is the simulated computer with small **Avida programs** inside, each a list of instructions that copies itself; all of them together in one run are the **program population**. An **instruction change** is a slip when a program copies itself. The **environment** (your "Avida execution environment") is the rules of the simulated world: which sums pay, and how much. "Pay" means more of the simulated computer's time, so a program copies itself faster.

A **sum** is one of Avida's 77 small logic tasks, as on page 113 (for example NOT: hand back a number with every 0 and 1 swapped). **Common** means done by at least one program in ten; **present** means done by at least one program. An **update** is Avida's time step.

**Arithmetic sums** are different tasks Avida can also recognise, such as adding two numbers or handing a number back unchanged. No environment ever paid for them.

A **test** here means taking one kind of program out of its world and running it alone, handing it chosen numbers, and seeing what it hands back. Page 113 did this with one set of numbers. This page did it with the tool from Astra's first reply, which uses **8 sets of numbers** and counts a sum only if the program does it on **all 8**.

## 3. What was tested

Four things, all planned and written down before anything was run:

1. **Astra's yardstick on every population saved in file 113** (18 runs, a saved population every 5,000 updates): which sums, and which arithmetic sums, each population could do; whether sums, once there, stayed there; and how many of each program's instructions it relies on (a count from Astra's fifth reply: take out one instruction at a time and see whether the program gets less of the computer's time; this is the "instruction ablation" of your list).
2. **Astra's second reply**: programs that read a number from a neighbour, do a little arithmetic on it, and then give that neighbour energy or not. Six runs of 5,000 updates, then a test of every kind of program in them.
3. **Does "common sums pay less" help a rare kind grow?** Two kinds of program from that environment, one put in at 1 in 100 and the other filling the rest, then the reverse, and shares in between; 15 runs of 2,000 updates, with no instruction changes.
4. **The still-rising run of page 113, let go on** from 50,000 to 75,000 updates.

## 4. What was found

**The yardstick.** Counting only sums done on all 8 sets of numbers, most populations came out as page 113 said: for example the fixed list's three runs, 7, 8 and 8 sums common, exactly as before. But five of the twelve runs where something was paid came out lower, and two came out at none: one growing-list run (0 instead of 46) and one all-77 run (0 instead of 32). The reason is section 1's: those programs work only with numbers arranged as their world arranges them. Counted on the two sets of numbers that keep the world's order, every run gives page 113's numbers exactly. So page 113's finding that the growing list ended with the most holds for the numbers the programs' world gave them; on the stricter yardstick, the growing list and the all-77 environment are not clearly apart. Which of the two counts is the right one for your question is not settled here.

**Sums, once there, mostly stayed.** For example, in the growing list's middle run, 98.7 in 100 of the sums present both at update 25,000 and at 50,000 were present at every look in between. In every environment that paid, it was at least 87 in 100.

**Arithmetic sums that nobody paid for were just as common when nothing was paid at all.** With no pay: 11, 11 and 7 arithmetic sums present at the end. With pay, 8 to 15. Not clearly apart. So those came with programs that copy themselves, not with what the environment paid for.

**Programs came to rely on more of their instructions where sums were paid.** For example, in the growing list, taking out any one of about 37 to 53 instructions lowered a typical program's share of the computer's time at update 5,000, and 74 to 82 at 50,000. With nothing paid, it went down. But this count rises by itself when a program does more paid sums, so it tells little beyond the sums.

**Astra's second reply: the choice did not disappear, but nothing showed it was kept for its use.** At the start every program gave energy only to a neighbour showing "1". After 5,000 updates, 77 to 88 in 100 gave to nobody, 9 to 20 in 100 gave to some neighbours and not others, and the starting rule was down to 2 to 6 in 100. Giving brings the giver nothing, and a little choosing can be kept going just by instruction changes; so this does not show that the programs keep a choice because it helps them.

**"Common sums pay less" did not help the rare kind.** The two kinds, picked by a rule written in advance: one did all nine paid sums; the other did eight (all but AND) and copies itself about 5 in 100 faster. The one doing all nine took over the whole world from every start, even from 1 in 100, within 1,500 updates. When it was common, AND did pay less, but still well above nothing (about 1.6 to 2.3 times the time), so doing AND always beat leaving it out. For a rare kind to grow, it would need a sum of its own that the common kind lacks; no such pair was found in that population.

**The still-rising run stopped** (section 1): 41 sums common at every look from 50,000 to 75,000, counted both ways page 113 used. This run was made the same way as page 113's, stopping and restarting every 1,000 updates; that way was never checked for this environment against one unbroken run.

## 5. What was not tested, and what is unsure

**Not tested:** why some programs depend on the order or size of their numbers (which instructions do it was not looked at); other pairs of program kinds, or the pair with instruction changes on; whether Astra's giving choice would last if choosing well paid; any run longer than 75,000 updates, or other runs let go on; an environment where a sum stops paying altogether once many programs do it, or one that pays for problems no program has solved yet.

**Unsure:** the 8 sets of numbers are one draw, and only two of them keep the world's order; the still-rising run was let go on in one run only; the two kinds competed for 2,000 updates only. The whole job used about 3.8 hours of computer time, under the 4 allowed.

## 6. The next step

GLM's check of this work is being sent now. When its points have been weighed, this page will say what changed.
