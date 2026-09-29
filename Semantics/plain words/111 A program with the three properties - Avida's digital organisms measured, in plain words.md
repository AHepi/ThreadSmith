# A program with the three properties: Avida's digital organisms measured. In plain words

*A note first. Written on 29 September 2026 by a Claude agent, for you, **before GLM checked it**: GLM is checking the work behind it now, and this page will be corrected where the checking finds mistakes. It uses none of the words you asked to be removed, except inside quotations. The full record is "Semantics/results/S111 Avida - the three properties measured.md" (with a data file beside it); the plan, written before anything was run, is "Semantics/results/S111 Avida - how the three properties will be measured, written before running.md". Nothing in the theory was changed.*

---

## 1. What happened, and what it means for your idea

You described knowledge as information that can cause itself to be copied, can cause itself to resist change, and can cause itself to remain, and asked for a type of program with exactly those properties. The answer was the self-copying programs of artificial-life research, and the next step was to run one of the existing simulators, Avida, and measure the three properties. That has been done.

**What happened.** One small program, 100 instructions long, was put into Avida's simulated computer, called here the **world**, and left for 50,000 time steps, nine times over (three rates of copying mistakes, three runs each). In every run the one program became about 3,600 programs within the first 1,000 time steps, and the population lasted to the end, over about 6,300 to 16,000 generations of copies. Along the way the programs changed: they learned to do small sums on numbers the world gave them, because the world rewarded that, and in six of the nine runs they learned the hardest of the nine sums on offer.

**The three properties were each found, and each has two halves.**

- **Copied.** The copying is done by 15 of the program's 100 instructions: switch off any one of those 15 and the program no longer makes a copy of itself; switch off any of the other 85 and nothing changes. Not one of 10,000 random programs of the same length could copy itself. But the actual carrying out of each step, and the copying mistakes, belong to the world.
- **Resists change.** In two ways. First, most single changes to an evolved program (69% to 79%) leave it still able to copy itself, and programs that evolved with more copying mistakes lose less to a change. Second, the 15 copying instructions stay the same across the population far more than the other 85 do. But nothing in a program repairs anything: the first kind of resistance is how the program is arranged, and the second is the world removing the copies that broke.
- **Remains.** The population and its line of descent remained to the end. But not one program identical to the first remained, and even its copying instructions were rewritten into a faster version. And a program that cannot copy itself also remains, for as long as you like, in a world where nothing dies of old age.

**What it means for your idea.** The three properties can be found, measured, in programs that hold no problem, do no criticism, and have nothing in them that stands for something outside them. In each of the three, "causes itself" turned out to mean something definite and checkable: the program's own instructions are a part without which the thing does not happen, and the world's rules are the other part. Whether "causes itself" should ask for more than that is yours to say. Nothing here settles it.

## 2. What Avida is, with the first program as the example

**Avida** is a research program, made at Michigan State University, that runs a simulated computer. Inside it live small programs, each a list of instructions. An **instruction** is one step, like one line of a recipe: "make some empty room", "copy one instruction into the room", "split off the copy". Researchers call these programs digital organisms; here they are simply called **programs**. Everything in this work ran inside Avida's simulated computer; nothing that copies itself ran on a real one.

The **world** is Avida's simulated computer: a grid of 3,600 places, each holding one program. The world hands out time to run instructions, a little to every program. When a program splits off a **copy** of itself, the copy goes into a neighbouring place, taking it over from whatever program was there. A program that has run for a long time dies of old age. Sometimes, when an instruction is copied, the world writes a random instruction instead: a **copying mistake**. How often that happens was set at three rates: about 1 in 400 copied instructions (low), 1 in 133 (Avida's usual), 1 in 50 (high).

The **first program**, which Avida's makers wrote by hand, has 100 instructions: 5 at the start that make room for a copy and find its end, 86 in the middle that do nothing at all, and 9 at the end that copy one instruction at a time, check whether the end has been reached, and if so split off the copy. It takes 389 steps to make one copy.

Avida can also run one program alone in a private **test computer**, with no copying mistakes and no neighbours, and report whether it makes an exact copy of itself. Most of the checks below use it.

## 3. Copied

**An example first.** Take the first program and **switch off** one instruction, that is, replace it with an instruction that does nothing. Switch off the "copy one instruction" step, and the program runs, makes room, and never fills it: no copy. Switch off one of the 86 do-nothing instructions in the middle, and it copies itself exactly as before.

Doing this for each of the 100 instructions in turn: **15 stop the copying**, the 5 at the start, the first of the middle ones (the instruction before it reads it as a marker), and the 9 at the end. **The other 85 change nothing**, not even the speed.

**Controls**: things that should not copy, checked in the same way. Not one of **10,000 random programs** of 100 instructions made an exact copy of itself; 100 of them put into the world made no copies and were all gone, dead of old age, after 66 time steps. The first program with its "copy one instruction" step switched off, put into the world alone, made no copies and was gone after 65.

**How often a copy is exact** depends on the rate the world sets: in the world, about 69 in 100 copies were exact at the low rate, 40 at Avida's usual rate, and 13 at the high rate, close to what the rates alone lead one to expect.

So: the copying is caused by the program's own 15 instructions, in the sense that without any one of them no copy is made; the world carries each step out, and decides how often the copy comes out wrong.

## 4. Resists change

"Resisting change" can mean two different things here, and both were measured.

**First: what the program does stays the same when an instruction changes.** An example: take the most common program in a run at the end, and make every program that differs from it in exactly one instruction (for 100 instructions, 2,500 of them). Run each in the test computer. In the nine runs, **69% to 79% of these one-change programs still copy themselves**; 21% to 31% no longer do.

And the programs that evolved with more copying mistakes lose less to a change: by the end, the share of one-change programs that copy themselves **at exactly the same speed** was 14% to 19% at the low rate and 27% to 36% at the high rate, and every high-rate run was above every low-rate run. Researchers have reported something like this before under the name "survival of the flattest"; here it rests only on these runs. The high-rate programs were also shorter, which the comparison does not separate.

**Second: the instructions themselves stay the same across the population.** An example: at the end of a low-rate run, 84% of the programs (on average over the three runs) still had the first program's instruction at the places of the 15 copying instructions; at the other 85 places, only 18% did. The copying places stayed the same far more than the rest in **every run, at every one of the six moments measured**. With the copying mistakes switched off entirely, nothing changed at all: after 5,000 time steps all 3,600 programs were still the first program.

**But:** the copying instructions changed too. In all six runs at the low and usual rates, the first program's 9 copying instructions, letter for letter, were gone from every program by time step 20,000. The most common programs now copy two or three instructions each time round the loop instead of one: faster, the same job, different instructions.

So: nothing in a program repairs a mistake; no instruction in Avida's set checks a copy against the original. The first kind of resistance is how the program's instructions are arranged, an arrangement that came about because the world let some arrangements last and not others. The second kind is the world removing the programs whose change broke the copying: they make no copies and die of old age or are taken over.

## 5. Remains

**The population remained**: in every run, never fewer than 3,481 programs from time step 1,000 to the end, all descended from the one first program, over 6,300 to 15,900 generations.

**What of the first program remained** at the end: not one program identical to it, in any run. Its 9 copying instructions, letter for letter, were in no program at the low and usual rates, and in 0% to 49% at the high rate. Its copying places held its instructions in 58% to 84% of cases (averages by rate). And the ability to make an exact copy of itself remained in 65% to 86% of the programs (averages by rate); at the high rate about a third of the programs cannot copy themselves, being the world's fresh mistakes, and the population goes on through the others.

**Controls.** The random programs and the switched-off first program were gone within 66 time steps, dead of old age. The same switched-off program, alone in a world where **nothing dies of old age**, stayed for all 2,000 time steps, doing nothing. Put beside the working first program in that same world, it was gone by time step 500, its place taken by the working program's copies.

So: in Avida, remaining depends on copying only because the world removes programs, by old age or by taking their place. A program remains by being copied faster than it is removed.

## 6. Marletto's test, on the sums

Marletto's test for knowledge (from her book, as the earlier file 110 quotes it): knowledge "is exactly the thing one would ultimately have to eliminate in order to prevent a particular transformation from being performed reliably."

The **sums**, called tasks in Avida: the world hands a program numbers, and rewards it with more running time if it writes back certain combinations of them. The hardest, **EQU**, is a number that marks, digit by digit, where two numbers agree. EQU was learned in six of the nine runs.

**An example.** In one low-rate run, the most common program does EQU with 26 instructions that have nothing to do with copying (they read numbers in and out, and combine and shuffle them). Switch those off in that one program and it stops doing EQU but still copies itself. Across the population, though, almost nothing changes: the share of programs doing EQU drops by 1.4 points, because that program makes up only 44 of the 3,600 (in the six runs, the drop was 0.2 to 1.4 points).

Now switch off, **in every program**, its own EQU instructions (found for each program separately). The share of programs doing EQU falls to **1% to 4%**, and 93% to 100% of them still copy themselves. So the test picks out something definite: about 19 to 26 instructions per program, separate from the copying instructions, spread over thousands of copies. Taking them out of one program leaves EQU done almost as reliably as before; taking them out of every program nearly stops it.

Not completely: some programs can do a sum in more than one way, so switching off what the one-at-a-time test finds does not always stop it. For the simplest sum, NOT, about a fifth of the programs still did it afterwards (up to 46% in one run).

## 7. Tested, not tested, unsure

**Tested:** the three properties, as set out in the plan written before anything was run; the controls; Marletto's test on the sums.

**Changed from the plan, and said so in the record:** the plan's description of the first program was slightly off (it said 85 do-nothing instructions and a copying part of 10; there are 86 and 9); a second, looser measure of "the same speed" was added (within 1%), because the plan's measure counted a change of one step in 389 as a change; the share of programs still able to copy themselves was added, because the letter-for-letter measures came to nothing in most runs; in Marletto's test the planned limit of 300 programs covered too few of the population, so the test was also run on 90% of the population, and switching off only the instructions that do not also copy was added, because switching off all of them stops the copying too. The first try of four control runs failed from a missing line break in a file and was run again.

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

## 9. One next step

Once GLM's check has been read and this page corrected, the next step I propose: write down, for the explanation kind, what these programs would have to have in addition (for instance a problem they hold, and criticism they do), each with a test of the same sort as the ones here, so that each addition can be tried and measured in the same way. Which way to take it is yours to choose.
