# What the evolved sums actually are. In plain words

*Note added 30 September 2026 (log S114): the programs studied here came from the runs of page 111, where, at every split, besides the copying mistakes, there was a one-in-twenty chance of one added instruction and a one-in-twenty chance of one removed instruction; this page names those runs by their copying-mistake rate only. No number here changes (the removals here were all made in the private test computer, where no change happens). Details: "Semantics/results/S114 Checking GPT 6 Astra's reply.md", section 4.*

*A note first. Written on 30 September 2026 by a Claude agent, for you, before GLM's check, and **now corrected to follow the check**: GLM went over the work behind this page in four parts and raised 32 points; another Claude agent weighed each one and ran what needed running again; section 7 says what the check changed. The page as it was before the check is kept in the project's history. It uses your Avida terms (the list you gave, kept in "Semantics/records/Semantics - Avida terms, given by the owner.md") and none of the words you asked to be removed, except inside quotations. The full record is "Semantics/results/S112 What the evolved sums are - what had to be removed and what it is, after the cross-examination.md" (with a data file beside it; the record as it was before the check is kept beside it); how each of GLM's points was settled is in "Semantics/results/S112 What the evolved sums are - the GLM cross-examination, settled.md"; the plan, written before anything was run, is "Semantics/results/S112 What the evolved sums are - how it will be found, written before running.md". Nothing in the theory was changed.*

---

## 1. Your two questions, answered directly

You asked: of the Avida programs that could do the small sums, what had to be removed for them to stop, and, setting aside that they were evolved, what that evolved information actually is, given the environment it was in.

**What had to be removed.** In almost every Avida program (98 in 100), taking out **one single instruction** was enough to stop a given sum while the program went on copying itself. Each program has a handful of such instructions for each sum: about 5 for the simplest sum (NOT), about 22 for EQU, about 27 for XOR. They are always of the same few kinds: the one instruction that both hands a number out and reads the next number in, the one instruction that combines numbers, the small markers that say which storage place each of these uses, the instructions that move numbers between storage places, and, surprisingly, some extra "read a number" instructions whose only job is to make sure the right number arrives at the right moment. In the other 2 in 100, a second copy of the sum inside the same program almost always meant two instructions had to go together; a few needed three, and 4 were not stopped by anything tried (section 3 comes to these).

**What it is.** When those instructions run, they make up a **small fixed wiring diagram**, called here a **circuit**: the numbers handed in go through a few steps of one basic operation (and sometimes an addition or subtraction that behaves the same way), and the result is handed out. For the sum NOT, most programs (63 in 100) do it with one step. For EQU, the hardest sum, most do it with five to eight steps. The same circuit turns up in thousands of programs written with different instructions. And it is that circuit **only in Avida**: change what one of Avida's instructions means, and the same programs do different sums, or none.

The rest of this page explains each of these, with examples.

## 2. The words used, with an example

**Avida** is a research program that runs a simulated computer. Inside it are small programs, each a list of instructions; you asked that each be called an **Avida program**, and its list an **instruction sequence**. An **instruction** is one step, like one line of a recipe. Everything here ran inside Avida's simulated computer; nothing that copies itself ran on a real one.

A **sum** here is one of Avida's nine small logic tasks: the simulated computer hands a program numbers, and the program earns a reward if it hands back certain combinations of them. The simplest, NOT, is a number that has a 1 wherever the number handed in has a 0, and a 0 wherever it has a 1. The hardest, EQU, marks, place by place, where two numbers agree. The nine are NOT, NAND, AND, ORN, OR, ANDN, NOR, XOR, EQU.

The simulated computer has three **storage places** (Avida calls them registers) and two piles of numbers (stacks). One single instruction both hands a number out and reads the next number in; below it is called the read-and-hand-out instruction. An instruction such as "combine" acts on the storage places; a small **marker** instruction placed right after it can say which storage place it uses.

Avida has **one instruction that combines numbers**: it is called `nand`, and it gives, place by place, a 1 unless both numbers have a 1 there. Every one of the nine sums can be built out of it, the way every electronic circuit in a computer can be built out of one kind of switch. Avida also has instructions that add, subtract, add one and take one away.

Avida hands a program **three fixed numbers** when it tests it alone. They are handed out **in turn**: the first "read a number" instruction gets the first number, the next gets the second, then the third, then the first again.

To **remove** an instruction here means to put in its place an instruction that does nothing (researchers call this instruction ablation; you listed it). A program **stops a sum** if, after the removal, it still copies itself but no longer does the sum.

## 3. What had to be removed

**An example first.** The most common program doing NOT in one of the nine runs has 110 instructions and is carried by 44 Avida programs in its program population. Avida's own step-by-step record of it shows what happens: instruction 11 reads a number in; instruction 12 puts it on a pile; instruction 16 takes it off into the second storage place, so the same number now sits in two places; instruction 20, the `nand`, combines the number with itself, which gives NOT of it; instruction 21 moves the result to the place the output instruction will use; instruction 26 hands it out.

Removing each of the 110 instructions in turn, and running the program again each time: **five** of them stop NOT while the program still copies itself: the pile instruction at 12, the marker at 15 (it belongs to a take-one-away instruction at 14 that is not on the path; without the marker, that instruction takes one from the number just read in, so the combining step gets two different numbers and NOT is gone), the `nand` at 20, the move at 21, and the marker at 27 that says which storage place the answer is handed out from. Two instructions on the path do **not** stop it when removed: the read at 11 (another read supplies a number instead, and NOT of any number is still NOT) and the hand-out at 26 (the answer stays where it is, and a later hand-out instruction, at 34, hands out a NOT made another way). So what had to be removed, in this program, is the one combining step and the moves and markers that bring one number to both sides of it and the result to the hand-out.

**Now across all the programs.** This was done for every distinct instruction sequence alive at the end of the nine runs: 23,332 of them, carried by 32,193 Avida programs; every single instruction of each removed in turn (2.3 million runs of Avida), and, in every program that copies itself and does a sum, every pair of instructions each of which can be removed alone without stopping the copying (52 million runs).

- For **98 in 100** pairs of an instruction sequence and one of its sums, one instruction was enough. The number of such instructions per program: about 5 for NOT and NAND, 7 for ORN, 10 for ANDN, 13 for AND and OR, 16 for NOR, 22 for EQU, 27 for XOR.
- They are the same few kinds everywhere: the read-and-hand-out instruction (a quarter to two fifths of them), `nand` (about a fifth), the markers (about a fifth to a quarter), and the move instructions; for some sums also add, subtract, add one, take one away.
- About one in six of them is not on the path from the numbers to the answer at all. Most of these are markers of instructions off the path, instructions that decide which instruction runs next, and **extra reads**; for AND, ORN and EQU the extra reads are the largest group. The extra reads are the surprising ones: since the numbers are handed out in turn, removing a read that nobody uses shifts every later read by one, so the program combines the wrong numbers. An example: in the most common EQU program of another run, removing an unused read at instruction 45 made the reads at 47, 53 and 66 receive the third, second and first numbers instead of the first, third and second, and the answer came out wrong: no longer EQU, nor any of the nine sums.
- **In the other 2 in 100**, no single removal stopped the sum, almost always because the program did it in two places; there, a pair of instructions had to go together, one from each place, or one extra read and one from the only place. Two programs needed three.
- **89 pairs** (NOT and ORN only, 95 Avida programs, in two runs) looked, before the check, as if they could not be stopped at all. The check ran them again. In 80 of them, every path of the sum does go through an instruction the program also needs to copy itself. But in 85 of the 89, a pair does stop the sum: one instruction whose removal alone stops the copying, and a second whose removal lets the copying work again. Only **4** (NOT, 4 Avida programs) were stopped by nothing tried.

So the direct answer to "what needed to be removed": for each program and each sum, **one of a small, listed set of instructions**, and those sets, across thousands of programs, are made of the same kinds of instruction doing the same jobs.

## 4. What it is

**An example first: EQU**, in the most common EQU program of one run (108 instructions, 28 Avida programs). With the three numbers called A, B and C, Avida's step-by-step record shows these steps, in order:

1. combine B and A with `nand`: "not both A and B"; put it on a pile;
2. read C and A, and with one `nand`, one addition, one "add one" and one subtraction, turn them into **not A** (C goes in and cancels out);
3. read B; two `nand` steps turn "not A" and B into **A or B**;
4. take "not both A and B" off the pile; one last `nand` of it with "A or B" gives **A equals B, place by place**, which is EQU;
5. hand it out.

That is a **circuit**: a fixed wiring diagram of a few kinds of step, from the numbers handed in to the number handed out. What the removals found in section 3 is this circuit's instructions, plus the moves, markers and reads that wire it together.

**Across all the programs.** Avida's step-by-step record of every one of the 23,332 instruction sequences was followed and checked, number by number, against what Avida itself recorded, with no difference anywhere. For each sum, the circuit of every program was written down in one standard way, so that programs doing the same circuit are counted together however their instructions are written.

- **A few circuits cover most programs.** NOT: one `nand` of a number with itself, 63 in 100 of the NOT programs. NAND: one `nand` of two numbers, 82 in 100. ORN: two `nand` steps, 69 in 100. For the harder sums the circuits are longer, and each run's program ancestry (its line of parent and descendant programs) found its own; EQU: four circuits cover 81 in 100 of the EQU programs, each of five to eight steps.
- **One circuit, many programs.** The most common NOT circuit is carried by 13,557 Avida programs with 7,959 different instruction sequences, and the instructions on its path are written in 352 different ways.
- **Some circuits use addition and subtraction** where you might expect only `nand`. These are exact: for example "not both A and C, plus A, plus one" is always "A and not C", for any numbers. Checked on all eight combinations of three digits, every circuit that could be checked this way gives its sum, except one.
- **The smallest possible circuits are there.** For seven of the nine sums, the smallest circuit found uses as few steps as the smallest possible with `nand` alone (NOT 1, NAND 1, AND 2, ORN 2, OR 3, ANDN 3, EQU 5); for NOR one uses fewer, by using a subtraction; for XOR the smallest found has 5 steps, one more than possible.
- **There are many circuits in all**: from 35 (XOR) to 404 (OR) different ones per sum (a few more, up to 417, if circuits that use different fixed numbers are counted apart) over all nine runs, most of them rare variants with extra steps that cancel out.

So the direct answer to "what that evolved information actually is": in Avida, it is **a small circuit of Avida's own operations, wired from the input channel to the output channel**, written into the instruction sequence in one of many possible spellings.

## 5. What it depends on

Each of these was tested by running the same programs, letters unchanged, with one thing of Avida changed. Before each run, the step-by-step records were used to say what should happen.

- **Change what `nand` means.** Make the letter for `nand` mean `nor` instead (a 1 only where both numbers have a 0): 98 in 100 programs still copy themselves, but what sums they do changes: of the NAND programs, 97 in 100 now do NOR instead; only 2 in 100 of the OR programs still do OR. What each program then does was said beforehand from its own circuit, and that was right for 99 in 100 of the programs that still copied themselves. Make it mean `and`: almost all sums vanish except AND (73 in 100 remain) and some NOT and ANDN.
- **Remove the input and output channel.** Make the read-and-hand-out letter do nothing: **no program does any sum**, though 83 to 89 in 100 still copy themselves. That no sum is done follows from Avida's own rules (numbers come in and go out only through that one instruction); what the test adds is that most programs go on copying.
- **Hand in other numbers.** Numbers of the kind Avida hands out in its runs: 99 to 100 in 100 still do each sum. Completely random numbers: 66 to 90 in 100. Some programs' other instructions compare the numbers handed in and take a different path when they change, and a few circuits give the right answer only for some numbers.
- **Change all the meanings.** Give the 26 letters the 26 meanings in another order (tried three times; a few letters kept their meaning by chance): no program copies itself or does anything.

So the circuit is a circuit **only relative to Avida**: to what its letters mean, to its read-and-hand-out channel, and to the numbers it hands in, in turn. The same letters under the other meanings tried are other circuits, or nothing; other changes of meaning were not tried.

## 6. Tested, not tested, unsure

**Tested:** every single removal in every program; every pair of instructions that can each be removed alone without stopping the copying, in every program that copies itself and does a sum; for the 91 cases left over, also every pair that includes an instruction the copying needs; every three together in the nine most common programs; Avida's step-by-step record of every program, followed with no difference; each circuit's answer checked against Avida's own check, on the three fixed numbers, on all eight combinations of digits, and on 200 other sets of numbers; four kinds of change to Avida.

**Changed from the plan, and said so in the record:** the first way of writing the circuits down grew too large for the computer's memory in programs that reuse their steps many times, so the job was stopped and the circuits written down more compactly; Avida would not take a reshuffled instruction set with its markers anywhere, so the markers were kept in front; and some programs that split off an inexact copy are still credited with sums by Avida, which the plan had not expected; they are counted separately.

**Not tested:** removing an instruction by cutting it out (which shifts all later positions), rather than putting a do-nothing in its place; pairs that include an instruction the copying needs, except in the 91 cases left over; all sets of three or more in every program; the programs inside the full program population, with neighbours, rather than alone.

**Unsure:** "the same circuit" counts two circuits as different if they reach the same answer through different additions and subtractions; the job of an instruction that is off the path (for instance an extra read) was read from Avida's record, and checked by removal only in three cases; one step-by-step record per program, on one set of numbers; circuits that differ only in a fixed number they use are counted as one (the count with them apart is given); the step-by-step check compares numbers, not where each number came from.

## 7. What the check changed

GLM raised 32 points; 26 stood, 6 stood in part, none fell. Nothing changed in the direct answers of section 1 or in the main numbers (98 in 100 stopped by one instruction; the circuits and their shares; the tests of section 5). What changed:

- **The 89 that seemed impossible to stop.** The first search never tried removing an instruction the program needs for copying together with a second one. Tried now, 85 of the 89 stop with such a pair, because the second removal lets the copying work again. The earlier explanation (that their sum and their copying share every instruction) was a guess; it holds for the paths of 80 of them, but it did not stop the pairs from working. 4 remain.
- **The marker at 15** in the NOT example belongs to an instruction off the path, not to the pile instruction; rerun, it was explained (section 3).
- **A small fault in how circuits were written down**: one kind of step that always gives zero was kept as a step. Fixed and rerun for the 1,399 programs concerned: a few circuits merged with shorter ones (for example 404 rather than 409 circuits for OR; 13,557 rather than 13,520 programs for the top NOT circuit). No share of the main table moved.
- **Wording held back to what was shown**: "only in Avida" became "under the meanings tried"; the numbers are counted per instruction sequence, and now say so; about one in six required instructions stop the sum without cutting every path of it, which the plan said would count against "what had to be removed is the path's instructions", and the record now reports it; the kinds of instruction required are the same in every run, but their shares differ a lot from run to run.
- Smaller fixes on this page: "almost always two places", the one read-and-hand-out instruction, "program population", "a few kinds of step", the reshuffled meanings.

## 8. One next step

The next step I propose, now that the check has been read and this page corrected: take one program and cut it down, removal by removal, to the **smallest instruction sequence that still copies itself and still does one sum** (you listed this as a minimal instruction sequence), so that you can see the whole thing, copying part and circuit, in one short list. Which way to take it is yours to choose.
