# A program with the three properties: Avida's digital organisms measured. In plain words

*Note added 30 September 2026 (log S114): this page's description of the changes the world makes at each split (section 2: one time in twenty an added instruction, one time in twenty a removed one, besides the copying mistakes) was checked against Avida's own code in log S114 and holds; the only looseness is "or": the adding and the removing are separate chances, and both can happen at the same split. No number here changes. Details: "Semantics/results/S114 Checking GPT 6 Astra's reply.md", section 4.*

*A note first. Written on 29 September 2026 by a Claude agent, for you, and **now following GLM's check**: GLM went over the work behind this page, a second Claude agent that had not done the work weighed each of its 30 objections, and this page was corrected to match (section 9 says what changed). It uses none of the words you asked to be removed, except inside quotations. The full record, as corrected, is "Semantics/results/S111 Avida - the three properties measured, after the cross-examination.md" (with a data file beside it; the version before the check is kept unchanged beside it), and the weighing of each objection is in "Semantics/results/S111 Avida - the GLM cross-examination, settled.md"; the plan, written before anything was run, is "Semantics/results/S111 Avida - how the three properties will be measured, written before running.md". Nothing in the theory was changed.*

---

## 1. What happened, and what it means for your idea

You described knowledge as information that can cause itself to be copied, can cause itself to resist change, and can cause itself to remain, and asked for a type of program with exactly those properties. The answer was the self-copying programs of artificial-life research, and the next step was to run one of the existing simulators, Avida, and measure the three properties. That has been done.

**What happened.** One small program, 100 instructions long, was put into Avida's simulated computer, called here the **world**, and left for 50,000 time steps, nine times over (three rates of copying mistakes, three runs each). In every run the one program became about 3,600 programs within the first 1,000 time steps, and the population lasted to the end, over about 6,300 to 15,900 generations of copies. Along the way the programs changed: they learned to do small sums on numbers the world gave them, because the world rewarded that, and in six of the nine runs they learned the hardest of the nine sums on offer.

**Each of the three properties was found, in the sense the plan set out before anything was run, and each has two halves.**

- **Copied.** The copying is done by 15 of the program's 100 instructions: switch off any one of those 15 and the program no longer makes a copy of itself; switch off any of the other 85 and nothing changes. Not one of 10,000 random programs of the same length could copy itself. But the actual carrying out of each step, and the copying mistakes, belong to the world.
- **Resists change.** In two ways. First, most single changes to an evolved program (69% to 79%) leave it still able to copy itself, though far fewer leave it copying at exactly the same speed; and programs that evolved with more copying mistakes lose less to a change. Second, the 15 copying instructions stay the same across the population far more than the other 85 do. But nothing in a program repairs anything: the first kind of resistance is how the program is arranged, an arrangement shaped by which programs the world let last, and the second is the world removing the copies that broke.
- **Remains.** The population and its line of descent remained to the end. But not one program identical to the first remained, and even its copying instructions were rewritten into a faster version. And a program that cannot copy itself also remains in a world where nothing dies of old age: in the test, for all 2,000 time steps it was run.

**What it means for your idea.** The three properties can be found, measured, in programs that hold no problem, do no criticism, and have nothing in them that stands for something outside them. In each of the three, "causes itself" turned out to mean something definite and checkable: the program's own instructions are a part without which the thing does not happen, and the world's rules are the other part. Whether "causes itself" should ask for more than that is yours to say. Nothing here settles it.

## 2. What Avida is, with the first program as the example

**Avida** is a research program, made at Michigan State University, that runs a simulated computer. Inside it live small programs, each a list of instructions. An **instruction** is one step, like one line of a recipe: "make some empty room", "copy one instruction into the room", "split off the copy". Researchers call these programs digital organisms; here they are simply called **programs**. Everything in this work ran inside Avida's simulated computer; nothing that copies itself ran on a real one.

The **world** is Avida's simulated computer: a grid of 3,600 places, each holding one program. The world hands out time to run instructions, a little to every program. When a program splits off a **copy** of itself, the copy goes into a neighbouring place, taking it over from whatever program was there. A program that has run for a long time dies of old age. Sometimes, when an instruction is copied, the world writes in a random instruction, which can even be the same one again: a **copying mistake**. How often that happens was set at three rates: about 1 in 400 copied instructions (low), 1 in 133 (Avida's usual), 1 in 50 (high). At each split the world also, one time in twenty each, adds one random instruction to the copy or takes one away.

The **first program**, which Avida's makers wrote by hand, has 100 instructions: 5 at the start that make room for a copy and find its end, 86 in the middle that do nothing at all, and 9 at the end that copy one instruction at a time, check whether the end has been reached, and if so split off the copy. It takes 389 steps to make one copy.

Avida can also run one program alone in a private **test computer**, with no copying mistakes and no neighbours, and report whether it makes an exact copy of itself. Most of the checks below use it.

## 3. Copied

**An example first.** Take the first program and **switch off** one instruction, that is, replace it with an instruction that does nothing. Switch off the "copy one instruction" step, the one step that does the copying, and no copy is made. Switch off one of the 86 do-nothing instructions in the middle, and it copies itself exactly as before.

Doing this for each of the 100 instructions in turn: **15 stop the copying**, the 5 at the start, the first of the middle ones (the instruction before it reads it as a marker), and the 9 at the end. **The other 85 change nothing**, not even the speed.

**Controls**: things that should not copy, checked in the same way. Not one of **10,000 random programs** of 100 instructions made an exact copy of itself; 100 of them put into the world made no copies and were all gone, dead of old age, after 66 time steps. The first program with its "copy one instruction" step switched off, put into the world alone, made no copies and was gone after 65.

**How often a copy is exact** depends on the rate the world sets: in the world, about 69 in 100 copies were exact at the low rate, 40 at Avida's usual rate, and 13 at the high rate. That is close to what one expects from the copying mistakes together with the one-in-twenty added and removed instructions, once one allows for the programs in the world having grown or shrunk from 100 instructions.

So: the copying is caused by the program's own 15 instructions, in the sense that without any one of them no copy is made; the world carries each step out, and decides how often the copy comes out wrong.

## 4. Resists change

"Resisting change" can mean two different things here, and both were measured.

**First: what the program does stays the same when an instruction changes.** An example: take the most common program in a run at the end, and make every program that differs from it in exactly one instruction (for 100 instructions, 2,500 of them). Run each in the test computer. In the nine runs, **69% to 79% of these one-change programs still copy themselves**; 21% to 31% no longer do. The plan had asked for more than that: that a large share keep both their copying and their speed. Copying, yes; speed, no: only 14% to 36% copy themselves at exactly the same speed (20% to 49% within one part in a hundred).

And the programs that evolved with more copying mistakes lose less to a change: by the end, the share of one-change programs that copy themselves **at exactly the same speed** was 14% to 19% at the low rate and 27% to 36% at the high rate, and every high-rate run was above every low-rate run. Researchers have reported something like this before under the name "survival of the flattest"; here it rests only on these runs. The high-rate programs were also shorter, which the comparison does not separate.

**Second: the instructions themselves stay the same across the population.** An example: at the end of a low-rate run, 84% of the programs (on average over the three runs) still had the first program's instruction at the places of the 15 copying instructions; at the other 85 places, only 18% did. The copying places stayed the same far more than the rest in **every run, at every one of the six moments measured**. The same held when the copying places were found afresh in each run's most common evolved program, rather than taken from the first program. With every kind of change switched off (the copying mistakes and the added and removed instructions), nothing changed at all: after 5,000 time steps all 3,600 programs were still the first program.

**But:** the copying instructions changed too. In all six runs at the low and usual rates, the first program's 9 copying instructions, letter for letter, were gone from every program by time step 20,000. The most common programs now copy two or three instructions each time round the loop instead of one: faster, the same job, different instructions.

So: nothing in a program repairs a mistake; no instruction in Avida's set checks a copy against the original. The first kind of resistance is how the program's instructions are arranged, an arrangement that came about because the world let some arrangements last and not others. The second kind is the world removing the programs whose change broke the copying: they make no copies and die of old age or are taken over.

## 5. Remains

**The population remained**: in every run, never fewer than 3,481 programs at the moments counted (every 1,000 time steps) from time step 1,000 to the end, all descended from the one first program, over 6,300 to 15,900 generations.

**What of the first program remained** at the end: not one program identical to it, in any run. Its 9 copying instructions, letter for letter, were in no program at the low and usual rates, and in 0% to 49% at the high rate. Its copying places held its instructions in 58% to 84% of cases (averages by rate). The plan's test asked for the first program's copying part to be in most programs at every moment measured; that held only loosely: in one high-rate run, at one moment, those places held its instructions in only 38% of cases. And the ability to make an exact copy of itself remained in 65% to 86% of the programs (averages by rate); at the high rate about a third of the programs cannot copy themselves, being the world's fresh mistakes, and the population goes on through the others.

**Controls.** The random programs and the switched-off first program were gone within 66 time steps, dead of old age. The same switched-off program, alone in a world where **nothing dies of old age**, stayed for all 2,000 time steps, doing nothing. Put beside the working first program in that same world, it was gone by time step 500, its place taken by the working program's copies.

So: in Avida, remaining depends on copying only because the world removes programs, by old age or by taking their place. A program remains by being copied faster than it is removed.

## 6. Marletto's test, on the sums

Marletto's test for knowledge (from her book, as the earlier file 110 quotes it): knowledge "is exactly the thing one would ultimately have to eliminate in order to prevent a particular transformation from being performed reliably."

The **sums**, called tasks in Avida: the world hands a program numbers, and rewards it with more running time if it writes back certain combinations of them. The hardest, **EQU**, is a number that marks, digit by digit, where two numbers agree. EQU was learned in six of the nine runs.

**An example.** In one low-rate run, the most common program does EQU with 26 instructions that have nothing to do with copying (they read numbers in and out, and combine and shuffle them). Switch those off in that one program and it stops doing EQU but still copies itself. Across the population, though, almost nothing changes: the share of programs doing EQU drops by 1.4 points, because that program makes up only 44 of the 3,600 (in the six runs, the drop was 0.15 to 1.4 points).

Now switch off, **in every program checked** (the most common ones, together 90% of the population), its own EQU instructions (found for each program separately). The share of programs doing EQU falls to **1% to 4%**, and 93% to 100% of the former EQU programs still copy themselves. The check showed what those 1% to 4% are: programs in which every EQU instruction is also a copying instruction, so nothing could be switched off in them without stopping the copying, and they were left as they were. In every program where the EQU instructions could be switched off, EQU stopped. So the test picks out something definite: about 19 to 26 instructions per program, separate from the copying instructions, spread over thousands of copies. Taking them out of one program leaves EQU done almost as before; taking them out of every program where they can be taken out stops it there.

The test computer hands every program the same three numbers. Tried again with two other sets of numbers, the share of programs doing each sum changed by less than 2 points.

Not completely: some programs can do a sum in more than one way, so switching off what the one-at-a-time test finds does not always stop it. For the sum NOT, about a fifth of the programs still did it afterwards (up to 46% in one run); about seven in ten of those still did it with their own NOT instructions switched off, and the rest were left untouched in the same way as above.

## 7. Tested, not tested, unsure

**Tested:** the three properties, as set out in the plan written before anything was run; the controls; Marletto's test on the sums.

**Changed from the plan, and said so in the record:** the plan's description of the first program was slightly off (it said 85 do-nothing instructions and a copying part of 10; there are 86 and 9); a second, looser measure of "the same speed" was added (within 1%), because the plan's measure counted a change of one step in 389 as a change; the share of programs still able to copy themselves was added, because the letter-for-letter measures came to nothing in most runs; in Marletto's test the planned limit of 300 programs covered too few of the population, so the test was also run on 90% of the population, and switching off only the instructions that do not also copy was added, because switching off all of them stops the copying too. The first try of the control runs went wrong: three stopped at once from a missing line break in a file, and the fourth ran without the switch-off instruction in it; nothing from that try was used, and all five controls were run again. A comparison the plan asked for, how fast the first program copies itself alone, was left out and is now given: about 0.077 copies per program per time step, against 0.075, 0.060 and 0.036 in the worlds.

**Not tested:** changes that add or remove an instruction (only swaps were tested); a head-to-head race between programs evolved at different rates (how "survival of the flattest" was first studied); longer runs; other worlds.

**Unsure:** three runs per rate is few; the high-rate programs were shorter, which could matter; lining up an evolved program against the first one is rough where the first one repeats the same instruction 86 times; Avida's own count of programs doing a sum is higher than the test computer's (for example 59% against 32% for EQU in one run), and why was not checked.

## 8. What these programs have and do not have, beside the explanation kind

Observations only; nothing is settled.

**They have** copying caused by their own instructions; an arrangement that keeps what they do through most single changes; parts that stay the same while the rest changes; a line that lasted thousands of generations; and, in six runs, instructions for EQU that pass Marletto's test.

**They do not have**:
- **a problem**: nothing in a program holds or states one; the sums are set, checked and paid for by the world;
- **criticism**: no program compares versions or finds a flaw in one; versions are removed by the world's rules;
- **anything standing for something outside them**: the EQU instructions turn two numbers into a third; nothing in them refers to where the numbers come from or to the reward;
- **any repair of their own mistakes**: no instruction checks or mends a copy.

In each of your three properties, the program's own instructions are a part without which it does not happen, and the world's rules are the other part.

## 9. What GLM's check changed

GLM raised 30 objections. Weighed one by one: 15 were right, 14 were partly right, 1 was wrong (it read one setting of a control run as a number of copies; it is the place in the grid, and the control ran as planned). Four new checks were run inside Avida's test computer.

- **One number moved**: the smallest drop in EQU when one program's EQU instructions are switched off is 0.15 points, not 0.2.
- **Three statements were cut back**: the first kind of resisting change keeps copying but not the exact speed; the first program's copying part was not in most programs at every moment; and "switched off in every program" means in every program checked, with the leftover 1% to 4% being programs where nothing could be switched off.
- **Things the check asked about, now tested, that left the results where they were**: other sets of numbers in the test computer; the copying places found afresh in the evolved programs; which single changes stop the first program copying.
- **Plain-words corrections on this page**: the added and removed instructions, the no-change control, the 2,000 time steps, the failed first try of the controls, and some wording.
- **One point left to you, not applied**: GLM argued that in neither kind of resisting change does the information itself do the resisting (the first is an arrangement the world's weeding shaped, the second is the world's weeding), so the second property, as you stated it, is not shown. The observations are on this page; how "causes itself" should be read is yours to say.

## 10. One next step

Now that GLM's check has been read and this page corrected, the next step I propose: write down, for the explanation kind, what these programs would have to have in addition (for instance a problem they hold, and criticism they do), each with a test of the same sort as the ones here, so that each addition can be tried and measured in the same way. Which way to take it is yours to choose.
