# Which execution environments learn new things. In plain words

*A note first. Written on 30 September 2026 by a Claude agent, for you, **before GLM's check** of the work behind it; GLM's points, once weighed, may change it, and this note will then say so. It uses your Avida terms (the list you gave, kept in "Semantics/records/Semantics - Avida terms, given by the owner.md") and none of the words you asked to be removed, except inside quotations. The full record is "Semantics/results/S113 Which execution environments learn - results.md" (with a data file beside it); the plan, written and saved before anything was run, is "Semantics/results/S113 Which execution environments learn - how it will be tested, written before running.md". Nothing in the theory was changed.*

---

## 1. Your question, answered directly

You asked: "what kind of execution environment can use these machines to progressively learn how to do new things".

**In these runs, the environment that made the program population learn the most new things was one whose list of paid problems grew as the population got better**: it started by paying only for the two easiest sums, and each time the population had made one of the hardest sums on offer common, it added the next harder ones. By the end, between 48 and 65 of 77 possible sums were done by at least one program in ten, in the three runs. That is more than any other environment tried, in every run, and more than an environment that paid for **all 77 sums from the start** (at most 41).

**An environment that paid for one hard sum only taught nothing.** No program ever did that sum, in any run, so the pay was never collected: those runs came out exactly the same, number for number, as runs where nothing was paid at all.

**But no environment tried here made the learning go on.** In every one, the number of sums the population could do rose for a while and then stopped rising, mostly within the first quarter to half of the run, and never beyond the 77 sums the list was made from. The growing list grew to the end of the list someone had written in advance, and then the population stopped too.

The rest of this page explains what was done, with examples.

## 2. The words used, with an example

**Avida** is the research program from the last two pages: a simulated computer with small **Avida programs** inside, each a list of instructions, each copying itself. All of them together in one run are the **program population**. When a program copies itself, the simulated computer now and then gets an instruction wrong; that is an **instruction change**.

A **sum** here is one of Avida's small logic tasks: the simulated computer hands a program numbers, and the program does a sum if it hands back a certain combination of them. Last time there were nine sums on two numbers (NOT, NAND, AND, ORN, OR, ANDN, NOR, XOR, EQU). Avida also has **68 sums on three numbers**; together with the nine, they are every such combination it knows, 77 in all. **A new sum** is what your terms call a new computational capability: none of the 77 is done by the program every run starts from.

The **Avida execution environment**, below just the **environment**, is the rules of the simulated world: which sums pay, and how much. "Pay" means the program gets more of the simulated computer's time, so it copies itself faster and its copies spread. Nothing else about the world was changed between runs.

**How hard a sum is**: Avida has one instruction that combines numbers (`nand`). Every sum can be built from it, in a number of steps. NOT takes 1 step; EQU takes 5; the hardest of the 77 takes 10 or more. The number of steps is the sum's **level**, and a sum paid in these runs pays more the higher its level, as in the earlier runs.

**Common** means done by at least one program in ten. **Present** means done by at least one program.

## 3. What was tested

**An example first.** One run of the growing list, run 1: at the start only NOT and NAND paid. After 1,500 time steps (Avida calls them updates) both were common, so at 2,000 the three sums of level 2 were added; one of them was common by 2,250, so at 3,000 level 3 was added; and so on, one level at a time, up to level 9 at 9,000. By 10,000 the population did 43 sums commonly, by 25,000 it did 62, and at the end, 50,000, it did 65, and 74 were present.

**Six environments**, each run three times with different chance events (called seeds), each for 50,000 updates, every run starting from the same program, which does no sum:

| environment | what paid | sums common at the end, in the three runs | sums present at the end |
|---|---|---|---|
| **growing list** | at first NOT and NAND; the next level added whenever one sum of the top level was common | **65, 48, 55** | **74, 67, 72** |
| **all 77 from the start** | every sum, from the start | 32, 41, and 0 (13 when counted the second way, section 5) | 54, 67, 32 (51 the second way) |
| **common sums pay less** | the nine two-number sums, each paid from a store that runs down when many programs use it | 17, 9, 8 | 45, 29, 26 |
| **fixed list** | the nine two-number sums, harder ones paying more (as in the earlier runs) | 7, 8, 8 | 20, 30, 19 |
| **one hard sum only** | EQU only | 0, 0, 0 | 3, 2, 0 |
| **nothing pays** | nothing (for comparison) | 0, 0, 0 | 3, 2, 0 |

What was counted: how many sums were present and common over time; when each first appeared; whether sums once common stayed common; whether the count kept rising or stopped; and, in the most common program of each run, whether the instructions a later sum needs overlap with those an earlier sum needs.

## 4. What was found

**One hard sum only.** In none of the three runs did any program ever do EQU. The easier sums turned up here and there by chance (NOT, NAND, ORN and ANDN in every run), but none became common, because nothing paid for them. With the easier sums paid as well (the fixed list), EQU became common in all three runs. So a pay for something that no program can nearly do yet never reaches the population. (Claude had recalled a published study reporting this; it is not relied on here: what is reported is what these runs did.)

**Paying for more kinds of sum gave more new sums.** Nine sums on offer: 7 or 8 became common. All 77 on offer: 13 to 41 (counting run 3 the second way, section 5). And **what was on offer mattered less than the order**: the growing list and the all-77 environment were paying for (nearly) the same 77 sums from update 11,000 on, yet the growing list ended with more in every run. Starting with the easy sums and adding harder ones only when the population was ready left it able to do more than offering everything at once. Why, these runs do not show.

**Making common sums pay less** did not clearly change the count against the fixed list with the same nine sums (17, 9, 8 against 7, 8, 8); in one run it went on to seven or eight three-number sums that nobody paid for.

**Sums once common were mostly kept**: 73 to 100 in 100 of the sums that had ever been common were still common at the end, in every run but one (section 5).

**The count stopped rising everywhere.** For example, in the growing list, runs 1 and 3 made their last new high at 37,000 and 31,500; after 25,000 no growing-list run added more than 4 sums. The fixed list stopped at 7 to 9. Claude had expected the growing list and the all-77 environment to keep rising to the end; they did not, except one run of the all-77 environment, still rising at the end (37 common at 45,000, 41 at 50,000).

**Later sums reuse earlier ones' instructions.** An example: in the most common program of growing-list run 1 (134 instructions, doing 64 sums), for each pair of sums, the one that appeared first in the run and the one that appeared later, on average 60 in 100 of the instructions the later sum needs are also needed by the earlier one, where chance would give 18 in 100. In all 12 runs where this could be measured, the overlap was above chance. But part of it may simply be the instructions that read the numbers in, which every sum needs; the measure cannot yet tell the two apart.

## 5. Something that went wrong, and was caught

To let the growing list grow, each run was cut into 50 pieces: after every 1,000 updates the whole population was saved, and the next piece started by loading it. A loaded program starts with an empty record of which sums it did, until it next copies itself. In one run of the all-77 environment (run 3), the simulated computer's time was shared so unevenly that many programs did not copy themselves within a whole piece, and Avida's own count said, at 10 of the last 19 piece ends, that **no** sum was common. Running every saved program alone in Avida's test processor (a separate small simulated computer that runs one program at a time) showed 13 common at each of those times. So the table above uses 13 for that run; the record gives both counts everywhere. For the other runs the two ways of counting agree exactly at most of the times compared, and otherwise within 6 sums. An agent working on log S114 found the same fault independently, from Avida's source.

## 6. Tested, not tested, unsure

**Tested:** six environments, three runs each, 50,000 updates, the 77 sums counted every 250 updates in the world and every 5,000 updates in the test processor; the overlap of needed instructions in the most common program of each run. Before running: that listing a sum without paying for it changes nothing (checked: the run came out identical).

**Changed from the plan, and said so in the record:** the second way of counting (section 5); each piece in fact ran 1,001 updates, not 1,000 (found by the S115 checks), so a run is 50,050 updates; the search for how hard each sum is stopped at 9 steps, so the hardest sum's "10" means "10 or more".

**Not tested:** sums other than these 77; other simulated computers, world sizes or rates of instruction change; longer runs; more than three runs of each; a list that grows beyond what was written in advance; a growing list with stores that run down; whether the growing list's lead comes from the order of pay or from its smaller pay in the first 10,000 updates.

**Unsure:** three runs of each environment is few; "more" here means every run of one above every run of the other, and several comparisons did not meet that. The overlap of instructions may be mostly the shared reading of numbers. Cutting runs into pieces may itself have changed them a little (the S114 check found no consistent difference for the fixed list, and a small lean to fewer common sums for "common sums pay less").

## 7. What this says about your question

Put together, in these runs: **the environments that taught new things were those that paid for easy things as well as hard ones, and the one that taught the most was the one that added harder problems as the population mastered easier ones.** A single hard problem taught nothing, and paying for nothing taught nothing. **What none of them did was keep going**: each environment's supply of problems was a list written in advance, and when the population had filled what it could of that list, learning stopped. For learning to go on, the problems themselves would have to keep coming from somewhere other than a fixed list; none of these environments had such a source.

## 8. One next step

The next step I propose: run an environment whose **new problems come from the program population itself** (for example, where what some programs hand out becomes the numbers that others must work on, so that each new sum a program can do makes new problems for the others), started from the same program and counted the same way, to see whether its count of new sums keeps rising where these all stopped. Log S115 is already checking designs of this kind proposed by GPT 6 Astra. Which way to take it is yours to choose.
