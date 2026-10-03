# Which execution environments learn new things. In plain words

*Updated on 30 September 2026: **this page now follows GLM's check.** GLM raised 30 points. A Claude agent that had not done the work weighed each one: 21 hold, 9 hold in part, none fails. Where they hold, the page is corrected below, and section 8 says what changed. No main number changed. One part of the direct answer did: "the count stopped rising in every run" was too strong. The weighing is in "Semantics/results/S113 Which execution environments learn - the GLM cross-examination, settled.md". The corrected record is "Semantics/results/S113 Which execution environments learn - results, after the cross-examination.md".*

*The first note, as written before the check. Written on 30 September 2026 by a Claude agent, for you, **before GLM's check** of the work behind it; GLM's points, once weighed, may change it, and this note will then say so. It uses your Avida terms (the list you gave, kept in "Semantics/records/Semantics - Avida terms, given by the owner.md") and none of the words you asked to be removed, except inside quotations. The full record is "Semantics/results/S113 Which execution environments learn - results.md" (with a data file beside it); the plan, written and saved before anything was run, is "Semantics/results/S113 Which execution environments learn - how it will be tested, written before running.md". Nothing in the theory was changed.*

---

## 1. Your question, answered directly

You asked: "what kind of execution environment can use these machines to progressively learn how to do new things".

**In these runs, the environment that made the program population learn the most new things was one whose list of paid problems grew as the population got better**: it started by paying only for the two easiest sums, and each time the population had made one of the hardest sums on offer common, it added the next harder ones. By the end, between 48 and 65 of 77 possible sums were done by at least one program in ten, in the three runs. That is more than any other environment tried, in every run, and more than an environment that paid for **all 77 sums from the start** (at most 41).

**An environment that paid for one hard sum only taught nothing.** No program ever did that sum, in any run, so the pay was never collected: those runs came out exactly the same, number for number, as runs where nothing was paid at all.

**But no environment tried here was shown to keep the learning going.** In 11 of the 12 runs where something was paid, the number of sums done commonly rose for a while and then nearly stopped: at the end it was at most one sum above where it stood at update 40,000. Most of the rise came in the first 10,000 to 25,000 updates. One run of the all-77 environment was still rising at the end (37 sums at 45,000, 41 at 50,000). Whether longer runs would have kept rising was not tried. The growing list grew to the end of the list someone had written in advance, and then the population nearly stopped too.

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

What was counted: how many sums were present and common over time; when each first appeared; whether sums once common stayed common; whether the count kept rising or stopped; and, in the most common program of each run, whether the instructions a later sum needs overlap with those an earlier sum needs. An instruction counts as **needed** for a sum if, when it is swapped for a step that does nothing and the program is run alone, that sum stops while the copying goes on (the "instruction ablation" of your list). This was done for every instruction of that one program in each run.

## 4. What was found

**One hard sum only.** In none of the three runs did any program ever do EQU. The easier sums turned up here and there by chance (NOT, NAND, ORN and ANDN in every run), but none became common, because nothing paid for them. With the easier sums paid as well (the fixed list), EQU became common in all three runs. So, in these runs, a pay for a sum that no program ever did never reached the population. Whether pay reaches a population only when some program is already close to the sum was not measured; it is a guess to test. (Claude had recalled a published study reporting this; it is not relied on here: what is reported is what these runs did.)

**Paying for more kinds of sum gave more new sums.** Nine sums on offer: 7 or 8 became common. All 77 on offer: 13 to 41 (counting run 3 the second way, section 5; counted Avida's own way, run 3 shows 0, and then the two are not clearly apart). And **what was on offer mattered less than the order**: the growing list and the all-77 environment were paying for (nearly) the same 77 sums from update 11,000 on, yet the growing list ended with more in every run. Starting with the easy sums and adding harder ones only when the population was ready left it able to do more than offering everything at once. Why, these runs do not show.

**Making common sums pay less** did not clearly change the count against the fixed list with the same nine sums (17, 9, 8 against 7, 8, 8); in one run it went on to seven or eight three-number sums that nobody paid for. The stores did run low, so a common sum really did pay less: through most of each run the stores of the common sums stood well under the level for full pay.

**Sums once common were mostly kept**: 73 to 100 in 100 of the sums that had ever been common were still common at the end, counted Avida's own way, in every run but one. In that run (section 5), counted the second way, 62 in 100 were kept.

**The count nearly stopped rising in every run but one.** For example, in the growing list, runs 1 and 3 made their last new high at 37,000 and 31,500; after 25,000 no growing-list run added more than 4 sums. The fixed list stopped at 7 to 9. Claude had expected the growing list and the all-77 environment to keep rising to the end. They did not, except one run of the all-77 environment, still rising at the end (37 common at 45,000, 41 at 50,000). Three runs made a new high after update 40,000.

**Later sums reuse earlier ones' instructions.** An example: in the most common program of growing-list run 1 (134 instructions, doing 64 sums), for each pair of sums, the one that appeared first in the run and the one that appeared later, on average 60 in 100 of the instructions the later sum needs are also needed by the earlier one, where chance would give 18 in 100. In all 12 runs where this could be measured, the overlap was above chance. Each run's number comes from one program's instructions, and in some runs that program was shared by only 4 to 8 of about 3,600 programs. But part of it may simply be the instructions that read the numbers in, which every sum needs; the measure cannot yet tell the two apart.

## 5. Something that went wrong, and was caught

To let the growing list grow, each run was cut into 50 pieces: after every 1,000 updates the whole population was saved, and the next piece started by loading it. A loaded program starts with an empty record of which sums it did, until it next copies itself. In one run of the all-77 environment (run 3), the simulated computer's time was shared so unevenly that many programs did not copy themselves within a whole piece, and Avida's own count said, at 10 of the last 19 piece ends, that **no** sum was common. Running every saved program alone in Avida's test processor (a separate small simulated computer that runs one program at a time) showed 13 common at each of the three of those times when a copy of the whole population had been kept (updates 35,000, 45,000 and 50,000); at the other seven the population was not kept, so it cannot be counted the second way now. So the table above uses 13 for that run. The record gives Avida's own count every 250 updates and the second count every 5,000 updates. For the other runs the two ways of counting agree exactly at most of the times compared, and otherwise within 6 sums. An agent working on log S114 found the same fault independently, from Avida's source.

## 6. Tested, not tested, unsure

**Tested:** six environments, three runs each, 50,000 updates, the 77 sums counted every 250 updates in the world and every 5,000 updates in the test processor; the overlap of needed instructions in the most common program of each run. Before running: that listing a sum without paying for it changes nothing (checked: the run came out identical). After GLM's check this was tried again on a population that did many sums, and again the runs came out identical.

**Changed from the plan, and said so in the record:** the second way of counting (section 5); each piece in fact ran 1,001 updates, not 1,000 (found by the S115 checks), so a run is 50,050 updates; the search for how hard each sum is stopped at 9 steps, so the hardest sum's "10" means "10 or more".

**Not tested:** sums other than these 77; other simulated computers, world sizes or rates of instruction change; longer runs; more than three runs of each; a list that grows beyond what was written in advance; a growing list with stores that run down; whether the growing list's lead comes from the order of pay or from its smaller pay in the first 10,000 updates.

**Unsure:** three runs of each environment is few; "more" here means every run of one above every run of the other, and several comparisons did not meet that. The overlap of instructions may be mostly the shared reading of numbers. Cutting runs into pieces may itself have changed them a little (section 8).

## 7. What this says about your question

Put together, in these runs: **the environments that taught new things were those that paid for easy things as well as hard ones, and the one that taught the most was the one that added harder problems as the population mastered easier ones.** A single hard problem taught nothing, and paying for nothing taught nothing. **What none of them did was keep going**: each environment's supply of problems was a list written in advance, and when the population had filled what it could of that list, learning stopped. In none of them did new problems come from anywhere but a list written in advance. Whether a longer list, or a longer run, would have kept the learning going was not tried.

## 8. What GLM's check changed, and what the save-and-reload test means for it

**What changed.** No main number changed. The growing list still ended with the most sums in every run (65, 48, 55), the all-77 environment with 32, 41 and 13, and one hard sum alone still taught nothing. What changed is how strongly some things were said:
- "The count stopped rising everywhere" was too strong. Nearly stopped in 11 of the 12 paid runs; one run was still rising at the end (sections 1 and 4).
- The rule about pay for something too hard is now said of these runs only (section 4).
- How "needed" instructions were found is now said (section 3). The overlap of needed instructions comes from one program per run (section 4).
- The second way of counting covered three of the ten bad times in run 3, not all ten (section 5).
- The kept share goes down to 62 in 100 in one run (section 4).
- The claim that learning *would have to* come from outside a fixed list is gone; it was not tested (section 7).

The check also brought new counts from the stored runs, and they show:
- the stores in "common sums pay less" really ran low;
- the growing list's steps were not held back by the counting fault of section 5;
- listing unpaid sums changes nothing even in a population that does many sums.

**What the save-and-reload test means.** Each run here was cut into 50 pieces; between pieces the population was saved and loaded again. Another check (log S114) ran two of these environments both ways, in pieces and in one go, and compared them:
- **The fixed list** came out the same both ways, within the spread of three runs. Its numbers here can be read as if the runs had not been cut.
- **"Common sums pay less"** may have come out a little low in pieces. After each load there were 5 to 10 in 100 fewer copies, and slightly fewer common sums, in all three runs, though never by enough to count as a difference. So its comparison with the fixed list (17, 9, 8 against 7, 8, 8), which turns on one or two sums in two runs, is uncertain; if the pieces changed anything, they made "common sums pay less" come out lower.
- **The growing list and the all-77 environment** were not tested this way. The growing list changes its pay only at the cuts, so the cuts are part of it and cannot be taken out.
- A load also restarts each program's count of generations, so generation counts from these runs are not used anywhere.

## 9. One next step

The next step I propose: run an environment whose **new problems come from the program population itself** (for example, where what some programs hand out becomes the numbers that others must work on, so that each new sum a program can do makes new problems for the others), started from the same program and counted the same way, to see whether its count of new sums keeps rising where these all stopped. Log S115 is already checking designs of this kind proposed by GPT 6 Astra. Which way to take it is yours to choose.
