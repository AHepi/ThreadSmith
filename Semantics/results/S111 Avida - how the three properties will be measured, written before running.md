# S111 Avida: how the three properties will be measured, written before running

*Log S111, decision S59. Written on 29 September 2026 by one Opus 5.5 agent (S56), and committed **before any measuring run**. The only runs made before this file: the build, and one timing run (the default ancestor, seed 1, 3,000 updates, 104 seconds; its numbers are used below only to choose run lengths). Nothing in the theory's text, formal core, claims or program is touched by this work.*

## 0. What is being asked

The owner (S59): knowledge is information that "Can cause itself to be copied", "Can cause itself to resist change" and "Can cause itself to remain"; the owner asked for "a type of program with these exact properties". Claude named digital organisms and proposed to measure the three properties on Avida's organisms: a working case of knowledge without explanation, to build from. The owner: "Yup do the next step please."

Avida (Ofria and colleagues, Michigan State University) is a research simulator. Its organisms are short programs, each a list of instructions from a set of 26, run on a simulated processor inside a simulated world. An organism that copies its instructions into new memory and splits off the copy has an offspring. The world is a 60 by 60 grid; an offspring goes into a neighbouring cell, replacing whoever was there. Everything below runs inside Avida; nothing that copies itself runs on the real machine.

Throughout, the question for each measure is also **what causes it: the organism's own instructions, or the simulated world** (the scheduler that hands out processor time, the memory, the mutations the world applies when an instruction is copied, the removal of organisms when space runs short or when they grow old).

## 1. The setup

- **Avida** 2.14.0 at commit 47f13dad (github.com/devosoft/avida), with its library `libs/apto` at the pinned commit 02e18980; built in the scratch space with cmake and make, release build, the environment variable `AVIDA_DISABLE_BACKTRACE=1` (so the `libs/backward-cpp` library is not needed). No patch and no extra compiler flag were needed with g++ 13.3.0 (285 compiler warnings, no errors). The build notes go into `results/S111 Avida - the runs/`.
- **Ancestor**: Avida's default hand-written organism, `default-heads.org`, 100 instructions: a 5-instruction head (make room for the copy; find the end), 85 filler instructions (`nop-C`, doing nothing but able to be changed), and a 10-instruction copy loop (copy one instruction; check whether the end is reached; if so, split off the copy; if not, go back). Written as letters (one letter per instruction), it is `wzcag` + 85 × `c` + `zvfcaxgab`.
- **World**: Avida's default configuration (`avida.cfg`), except the copy error rate and the seed, and the output events below. Default: 60 × 60 cells on a torus; the offspring goes to a random neighbouring cell (an empty one first); an organism dies after executing 20 times its length in instructions; one instruction inserted with probability 0.05 and one deleted with probability 0.05 at each split; processor time handed out in proportion to "merit" (the organism's length executed, multiplied by the rewards for tasks).
- **Environment**: the default `environment.cfg`: nine logic tasks on two 32-bit numbers the world supplies (NOT, NAND, AND, OR-NOT, OR, AND-NOT, NOR, XOR, EQU), each rewarded with extra processor time, once per life each.
- **Conditions**, three copy error rates (the chance that each instruction copied is replaced by a random one): **low 0.0025**, **default 0.0075** (Avida's own), **high 0.02**; for the ancestor's 100 instructions, about 0.25, 0.75 and 2.0 copy errors per offspring. **Three seeds per condition** (1, 2, 3): nine runs.
- **Run length**: 50,000 updates each (an update is Avida's unit of time: about 30 instructions executed per organism). From the timing run, about 29 updates a second, so about 30 minutes a run; three runs at a time; each under a timeout of 2 hours. About 3,500 to 4,000 generations. If a run is cut by its timeout, its last saved state is used and the shortfall recorded.
- **Saved**: every 1,000 updates, the counts (organisms, births, births with an offspring identical to its parent, Avida's `num_breed_true`), the tasks performed, the dominant (most common) genotype, the average generation; the whole population (every genotype with its count and sequence) at updates 1,000, 10,000, 20,000, 30,000, 40,000 and 50,000.
- **Test processor**: Avida's analysis mode runs a program alone in a private processor, with no mutations and no neighbours. There Avida calls a program **viable** when it produces an offspring identical to itself (or one that, run in turn, cycles back to it). "Fitness" there is merit divided by the time taken to copy. Every knockout and mutant is judged there.
- **Knockout**: one instruction replaced by `nop-X`, an instruction that does nothing and, unlike `nop-C`, is not read as part of a label. `nop-X` is added, as a 27th instruction, only to the instruction set of the analysis runs and of the control worlds, never to the main runs.

## 2. COPIED: information that can cause itself to be copied

**Measures.**
- C1. The ancestor in the test processor: viable or not; instructions executed per copy; length copied.
- C2. **Knockout test on the ancestor**: each of the 100 instructions in turn replaced by `nop-X`; for each, viable or not. The sites whose knockout stops self-copying are the **essential sites**; the rest are the **non-essential sites**.
- C3. **Copy fidelity** at each error rate: (i) expected share of offspring identical to the parent, from the rates and the length; (ii) Avida's `SAMPLE_OFFSPRING`, 1,000 offspring of the ancestor made in the test processor under each condition's rates, the share identical to the parent; (iii) in the world, births with the offspring identical to the parent divided by all births, per run, averaged over updates 1,000 to 50,000.
- C4. **Offspring per organism**: in the world, births per organism per update, and the average generation reached at 50,000 updates; for comparison, the ancestor alone in the test processor.
- C5. From one injected ancestor, the population size over time.

**Counts as the property shown**: the ancestor is viable; a population grows from one injected ancestor; the knockouts split into a small set that stops copying and a large set that does not, and the small set is the instructions that ask for the copy (room, copy, split) and the labels that steer them.
**Counts against**: the ancestor is not viable; copying survives every knockout (then the copying would be the world's doing, whatever the program says); every knockout stops it (then nothing in the program marks what matters); random programs copy as often as the ancestor (control K1).
**Program or world**: the program's instructions ask for each step (`h-alloc` room, `h-copy` one instruction, `h-divide` split); the simulated processor carries each out, and the world supplies the time and places the offspring. The knockout test shows which part the program contributes: without those instructions the world copies nothing. Fidelity is set by the world: the program has no instruction that checks or repairs a copy against its original (checked by reading the instruction set; `if-label` compares the last copied instructions with a label, to find the end).

## 3. RESISTS CHANGE: information that can cause itself to resist change

Two senses are kept apart: (a) **what the program does** stays the same when its instructions change (robustness); (b) **the instructions themselves** stay the same in the population (conservation).

**(a) By its own structure: mutational robustness.**
- R1. For the dominant genotype of each run at updates 10,000, 30,000 and 50,000, and for the ancestor: **every single-point mutant** (each site replaced by each of the 25 other instructions of the set). For each mutant, in the test processor: viable or not; fitness. Shares reported: viable (still copies itself exactly); **neutral** (viable and fitness within one part in a million of the unmutated genotype's); lethal (not viable).
- R2. The shares compared between the low and the high error rate (three seeds each; the default rate between). Wilke and colleagues (2001), from memory and not checked here, reported that at a high error rate a population can come to favour genomes whose mutants lose less ("survival of the flattest"); **only these runs are used**, not that paper: the comparison either shows a higher neutral share at the high rate or it does not.

**(b) By the population: conservation.**
- R3. At each saved population (1,000 to 50,000), every genotype is aligned to the ancestor (a global alignment, one point for a match, minus one for a mismatch or a gap). For each ancestral site, the share of organisms (weighted by count) whose aligned instruction is the ancestor's. **Averaged over the essential sites and over the non-essential sites (from C2) separately.**
- R4. The same share in the no-mutation control (K5): the baseline where the world changes nothing.

**Counts as shown**: (a) a large share of single changes leave copying and fitness unchanged; the comparison tells whether the share moves with the error rate. (b) Essential sites stay the ancestor's in a larger share of the population than non-essential sites, at the same error rate.
**Counts against**: (a) most single changes stop copying; (b) essential and non-essential sites change at the same pace (the world's changes are not being undone).
**Program or world**: no instruction repairs anything. In (a), what buffers change is the arrangement of the program's instructions (which sites matter); that arrangement was itself shaped by which variants the world let persist. In (b), what keeps essential sites unchanged is the world: a variant that cannot copy leaves no offspring and dies of age or is overwritten; the program's part is only that its essential sites are the ones whose change stops copying.

## 4. REMAINS: information that can cause itself to remain

- M1. Population size over time in every run (above zero to the end or not).
- M2. **Persistence of the essential information**: at each saved population, the share of organisms carrying the ancestor's copy loop `zvfcaxgab` and its head `wzcag` exactly (anywhere in the genome); the essential-site conservation of R3; the share carrying the whole ancestral genome.
- M3. Generations elapsed; the ancestor's lineage (every organism descends from the one injected).

**Controls that should not remain** (each alone in a default world unless stated; one seed; 2,000 updates):
- K1. **Random programs**: 10,000 random genomes of length 100 (each instruction drawn evenly from the 26) tested in the test processor for viability; and 100 of them injected into the world, one per cell, followed.
- K2. **The ancestor with its copy loop knocked out** (`h-copy` replaced by `nop-X`): tested in the test processor; injected alone, followed.
- K3. K2 in a world where **nothing dies of age** (Avida's `DEATH_METHOD 0`): expected to remain, showing that when nothing removes it, a program that cannot copy remains too; remaining is then the world's doing.
- K4. K2 and the intact ancestor injected side by side, nothing dying of age: whether the non-copier is removed by the copier's offspring taking the space.
- K5. **No mutation**: the ancestor, error rates all set to 0, 5,000 updates, one seed: the baseline for R3 and M2.

**Counts as shown**: the populations last to 50,000 updates; the essential information is present in most organisms at every save; K1 and K2 vanish in the default world.
**Counts against**: runs die out; the essential information is lost; the controls remain as long as the copiers in the default world.
**Program or world**: the world removes (old age, overwriting); what remains is what is copied faster than it is removed. The program's part is the copying (section 2); K3 separates it from the world's removal rule.

## 5. Marletto's test on something beyond copying

The test, as file S110 quotes it: knowledge "is exactly the thing one would ultimately have to eliminate in order to prevent a particular transformation from being performed reliably." (Marletto, ch. 5)

**Applied only if logic tasks evolve.** For each run whose population performs any task at 50,000 updates, and for each task performed by at least 10% of the organisms there:
- T1. In the dominant genotype: each instruction knocked out in turn; the sites whose knockout stops the task (and whether copying survives).
- T2. **One copy against every copy**: the share of the population performing the task (weighted by count, each genotype run in the test processor) (i) as found; (ii) with the task's sites knocked out in the dominant genotype only; (iii) with each of the most common genotypes (together at least 90% of the organisms, at most 300 genotypes) given its own knockout map and all of its own task sites knocked out at once.
- Reported: how many and which instructions (e.g. `nand`, `IO`) one would have to eliminate, and whether eliminating them in one genotype stops the population performing the task reliably, or only eliminating them in every copy does.
**Counts against the test picking something out**: no knockout stops the task (it would be done by something other than the program), or eliminating it in one genotype already stops the population.
**Program or world**: the program's instructions compute the function (read inputs, `nand`, write output); the world supplies the inputs, checks the output and pays for it in processor time.

## 6. Replicates, summaries, what is not measured

- Every number over seeds is given per seed and as the mean with the smallest and largest. With three seeds a difference is called a difference only if every seed of one condition lies beyond every seed of the other; otherwise "no clear difference".
- Not measured: insertion and deletion mutants in the robustness scan (point changes only); competition between evolved genotypes (the design of Wilke and colleagues); anything about explanation, problems or criticism (the next kind, S59).
- Scripts in `Semantics/tools/` named in plain words; configurations, exact commands and summary tables in `results/S111 Avida - the runs/`; raw output only in the scratch space.
- Any departure from this plan is recorded in the results file with its reason.
